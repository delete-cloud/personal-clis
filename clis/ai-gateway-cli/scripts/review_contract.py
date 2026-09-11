"""Rebuild the master HTTP contract from pinned ai-gateway source, without running it."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

src = Path(sys.argv[1]).resolve()
root = Path(__file__).resolve().parents[1]
pinned = "7ab85dadbc4e5652181ef7c8036521dca33236de"
assert subprocess.check_output(["git", "-C", str(src), "rev-parse", "HEAD"], text=True).strip() == pinned, "Review required for new upstream revision"
assert not subprocess.check_output(
    ["git", "-C", str(src), "status", "--porcelain"], text=True
).strip(), "Review requires clean upstream"

API = src / "internal/master/api"
MODELS = src / "internal/models"
DAO = src / "internal/dao"
SERVER = src / "internal/master/server.go"

EXCLUDE = {
    ("GET", "/metrics"),
    ("GET", "/ws/agent"),
    ("GET", "/ws/agent-relay"),
    ("POST", "/api/agents/usage"),
    ("GET", "/api/oauth/:provider/authorize"),
    ("GET", "/api/oauth/:provider/callback"),
    ("GET", "/api/oauth/:provider/link"),
}
EXCLUDE_REASON = {
    "/metrics": "prometheus scrape, not a management JSON API",
    "/ws/agent": "WebSocket control sync",
    "/ws/agent-relay": "WebSocket relay tunnel",
    "/api/agents/usage": "agent-to-master usage ingest, not an operator command",
    "/api/oauth/:provider/authorize": "browser OAuth redirect",
    "/api/oauth/:provider/callback": "browser OAuth redirect",
    "/api/oauth/:provider/link": "browser OAuth redirect",
}

JSON_BODY_MODES = {
    "BindJSON",
    "BindOptionalJSON",
    "BindURIAndJSON",
    "BindURIAndOptionalJSON",
    "BindURIAndBodyMap",
    "BindStrictJSONText",
    "BindURIAndStrictJSONBodyMap",
    "BindURIAndStrictJSONText",
}
QUERY_MODES = {"BindQuery", "BindURIAndQuery"}
URI_MODES = {
    "BindURI",
    "BindURIAndJSON",
    "BindURIAndOptionalJSON",
    "BindURIAndQuery",
    "BindURIAndBodyMap",
    "BindURIAndStrictJSONBodyMap",
    "BindURIAndStrictJSONText",
}

STRUCT_RE = re.compile(r"type (\w+) struct \{", re.M)
ALIAS_RE = re.compile(r"type (\w+) = ([^\n]+)")
DEF_RE = re.compile(r"type (\w+) ([^*\n][^\n]*)")
FIELD_RE = re.compile(
    r"^\s*(?:([A-Z]\w*)\s+)?(\*?\[\]|\*)?([\w.\[\]\*{}]+)\s+`([^`]*)`"
)
EMBED_RE = re.compile(r"^\s*\*?((?:[\w]+\.)?\w+)\s*$")
SIG_RE = re.compile(
    r"func \([^)]+\) (\w+)\(\s*\w+\s+\*app\.Context,\s*(?:_\s+struct\{\}|\w+\s+(\*?[\w.]+(?:\[[^\]]+\])?))\)\s*\(([^)]+)\s*,\s*error\)",
)

def strip_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return "\n".join(
        line.split("//", 1)[0] if not line.strip().startswith("//go:") else line
        for line in text.splitlines()
    )


def read_pkg_files(directory: Path) -> str:
    parts = []
    for path in sorted(directory.glob("*.go")):
        if path.name.endswith("_test.go"):
            continue
        parts.append(path.read_text())
    return "\n".join(parts)


def extract_struct_body(text: str, start: int) -> str:
    i = text.find("{", start)
    depth = 0
    for j, ch in enumerate(text[i:], i):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1 : j]
    raise AssertionError("unclosed struct")


def load_package(directory: Path) -> dict:
    raw = read_pkg_files(directory)
    text = strip_comments(raw)
    structs, aliases = {}, {}
    for match in STRUCT_RE.finditer(text):
        structs[match.group(1)] = extract_struct_body(text, match.start())
    for match in ALIAS_RE.finditer(text):
        aliases[match.group(1)] = match.group(2).strip()
    for match in DEF_RE.finditer(text):
        name, rhs = match.group(1), match.group(2).strip()
        if name in structs or name in aliases or rhs.startswith("struct") or rhs.startswith("interface") or rhs.startswith("func"):
            continue
        if " " in rhs:
            continue
        aliases[name] = rhs
    methods = {}
    for match in SIG_RE.finditer(raw):
        methods[match.group(1)] = (match.group(2) or "struct{}", re.sub(r"\s+", " ", match.group(3)).strip())
    return {"structs": structs, "aliases": aliases, "methods": methods, "text": text}


packages = {}
for sub in sorted(p for p in API.iterdir() if p.is_dir()):
    packages[sub.name] = load_package(sub)
packages["api"] = load_package(API)
packages["models"] = load_package(MODELS)
packages["dao"] = load_package(DAO)

import_aliases = {}
for match in re.finditer(
    r'^\s*(?:(\w+)\s+)?"github.com/VaalaCat/ai-gateway/internal/master/api(?:/([^"]+))?"',
    SERVER.read_text(),
    re.M,
):
    alias, leaf = match.group(1), match.group(2)
    pkg = leaf or "api"
    import_aliases[alias or pkg] = pkg


def split_type(typename: str) -> tuple[str | None, str]:
    typename = typename.strip().lstrip("*")
    if "." in typename and not typename.startswith("map[") and not typename.startswith("["):
        pkg, name = typename.split(".", 1)
        return pkg, name
    return None, typename


def tag_value(tag: str, key: str) -> str | None:
    match = re.search(rf'{key}:"([^"]*)"', tag)
    if not match:
        return None
    value = match.group(1).split(",")[0]
    if value in ("", "-"):
        return None
    return value


schemas: dict = {}
building: set[str] = set()


def schema_ref(name: str) -> dict:
    return {"$ref": f"#/components/schemas/{name}"}

_alias_stack: list[str] = []


def field_schema(typename: str, origin: str) -> dict:
    typename = typename.strip()
    key = f"{origin}:{typename}"
    if key in _alias_stack:
        return {"type": "object", "additionalProperties": True}
    _alias_stack.append(key)
    try:
        return _field_schema(typename, origin)
    finally:
        _alias_stack.pop()


def _field_schema(typename: str, origin: str) -> dict:
    if typename.startswith("*"):
        return field_schema(typename[1:], origin)
    if typename in ("any", "interface{}", "json.RawMessage", "gin.H"):
        return {"type": "object", "additionalProperties": True}
    if typename in ("string", "json.Number"):
        return {"type": "string"}
    if typename == "bool":
        return {"type": "boolean"}
    if typename in {"int", "int8", "int16", "int32", "int64", "uint", "uint8", "uint16", "uint32", "uint64", "byte", "rune"}:
        return {"type": "integer"}
    if typename in {"float32", "float64"}:
        return {"type": "number"}
    if typename in {"time.Time"}:
        return {"type": "string", "format": "date-time"}
    if typename == "[]byte":
        return {"type": "string", "format": "byte"}
    if typename.startswith("[]"):
        return {"type": "array", "items": field_schema(typename[2:], origin)}
    if typename.startswith("map["):
        inner = typename[typename.find("]") + 1 :]
        return {"type": "object", "additionalProperties": field_schema(inner, origin)}
    generic = re.fullmatch(r"(?:api\.)?(Created|Accepted|PaginatedResponse)\[(.+)\]", typename)
    if generic:
        inner = field_schema(generic.group(2), origin)
        if generic.group(1) == "PaginatedResponse":
            return {
                "type": "object",
                "properties": {
                    "data": {"type": "array", "items": inner},
                    "total": {"type": "integer"},
                    "page": {"type": "integer"},
                    "page_size": {"type": "integer"},
                },
            }
        return inner
    pkg, name = split_type(typename)
    remap = {"api": "api", "models": "models", "dao": "dao"}
    pkg = remap.get(pkg, origin if pkg is None else remap.get(pkg, pkg))
    if pkg not in packages or (name not in packages[pkg]["structs"] and name not in packages[pkg]["aliases"]):
        if origin in packages and name in packages[origin]["structs"]:
            pkg = origin
        elif origin in packages and name in packages[origin]["aliases"]:
            pkg = origin
        else:
            return {"type": "object", "additionalProperties": True}
    if name in packages[pkg]["aliases"]:
        return field_schema(packages[pkg]["aliases"][name], pkg)
    schema_name = f"{pkg}_{name}"
    make_schema(pkg, name, schema_name)
    return schema_ref(schema_name)


def make_schema(pkg: str, name: str, schema_name: str) -> None:
    if schema_name in schemas or schema_name in building:
        return
    building.add(schema_name)
    body = packages[pkg]["structs"].get(name)
    if body is None:
        schemas[schema_name] = {"type": "object", "additionalProperties": True}
        building.discard(schema_name)
        return
    props, required = {}, []
    for raw_line in body.splitlines():
        field = FIELD_RE.match(raw_line)
        if field:
            tags = field.group(4)
            json_name = tag_value(tags, "json")
            form_name = tag_value(tags, "form")
            uri_name = tag_value(tags, "uri")
            prop_name = json_name or form_name or uri_name
            if not prop_name:
                continue
            props[prop_name] = field_schema(field.group(3), pkg)
            if 'binding:"required"' in tags and json_name:
                required.append(prop_name)
            continue
        embed = EMBED_RE.match(raw_line)
        if embed:
            embedded = field_schema(embed.group(1), pkg)
            if "$ref" in embedded:
                ref_name = embedded["$ref"].rsplit("/", 1)[-1]
                ref_schema = schemas.get(ref_name, {})
                props.update(ref_schema.get("properties", {}))
                required.extend(ref_schema.get("required", []))
            elif embedded.get("type") == "object":
                props.update(embedded.get("properties", {}))
    schema = {"type": "object", "properties": props}
    if required:
        schema["required"] = list(dict.fromkeys(required))
    schemas[schema_name] = schema
    building.discard(schema_name)


def request_properties(pkg: str, typename: str, mode: str):
    if typename in (None, "struct{}", "struct"):
        return {}, [], [], False
    pkg_name, name = split_type(typename)
    pkg = pkg_name or pkg
    if pkg not in packages:
        pkg = "api"
    if name in packages.get(pkg, {}).get("aliases", {}):
        return request_properties(pkg, packages[pkg]["aliases"][name], mode)
    body = packages.get(pkg, {}).get("structs", {}).get(name)
    json_props, required, params = {}, [], []
    free_form = False
    if body is None:
        return json_props, required, params, False
    if re.search(rf"func \(\w+ \*?{name}\) SetBodyMap\(", packages[pkg]["text"]):
        free_form = mode in JSON_BODY_MODES

    def consume_struct(current_pkg: str, struct_body: str) -> None:
        for raw_line in struct_body.splitlines():
            field = FIELD_RE.match(raw_line)
            if field:
                tags = field.group(4)
                json_name = tag_value(tags, "json")
                form_name = tag_value(tags, "form")
                uri_name = tag_value(tags, "uri")
                schema = field_schema(field.group(3), current_pkg)
                if uri_name and mode in URI_MODES:
                    params.append({"name": uri_name, "in": "path", "required": True, "schema": schema})
                if form_name and mode in QUERY_MODES:
                    params.append(
                        {
                            "name": form_name,
                            "in": "query",
                            "required": 'binding:"required"' in tags,
                            "schema": schema,
                        }
                    )
                if json_name and mode in JSON_BODY_MODES:
                    json_props[json_name] = schema
                    if 'binding:"required"' in tags:
                        required.append(json_name)
                continue
            embed = EMBED_RE.match(raw_line)
            if embed:
                epkg, ename = split_type(embed.group(1))
                epkg = epkg or current_pkg
                if epkg in import_aliases:
                    epkg = import_aliases[epkg]
                nested_body = packages.get(epkg, {}).get("structs", {}).get(ename)
                if nested_body:
                    consume_struct(epkg, nested_body)

    consume_struct(pkg, body)
    return json_props, list(dict.fromkeys(required)), params, free_form


def server_fn(name: str) -> str:
    text = SERVER.read_text()
    match = re.search(rf"func \(s \*Server\) {name}\(\) \{{", text)
    assert match, name
    return extract_struct_body(text, match.start())


def parse_handler_pkg(setup: str) -> dict[str, str]:
    mapping = {}
    for match in re.finditer(r"(\w+)\s*:?=.*?(?:&|\*)?([A-Za-z0-9_]+)\.Handler", setup):
        mapping[match.group(1)] = import_aliases.get(match.group(2), match.group(2))
    for match in re.finditer(r"(\w+)\s*:?=.*?([A-Za-z0-9_]+)\.NewHandler", setup):
        mapping[match.group(1)] = import_aliases.get(match.group(2), match.group(2))
    mapping.update(
        {
            "channelH": "channel",
            "oauthH": "oauth",
            "marketplaceH": "model_marketplace",
            "pcH": "private_channel",
            "userH": "user",
            "tokenH": "token",
            "modelH": "model",
            "agentH": "agent",
            "systemH": "system",
        }
    )
    return mapping


def gin_to_openapi(path: str) -> str:
    return re.sub(r":(\w+)", r"{\1}", path)


def path_params_from_gin(path: str) -> list[dict]:
    return [
        {"name": name, "in": "path", "required": True, "schema": {"type": "string"}}
        for name in re.findall(r":(\w+)", path)
    ]


def operation_meta(full_path: str, method: str) -> tuple[str, str]:
    if full_path == "/ping":
        return "public", "public_ping_get"
    if full_path.startswith("/api/admin/"):
        rest = full_path[len("/api/admin/") :]
        tag = "admin"
        prefix = ["admin"]
    elif full_path.startswith("/api/"):
        rest = full_path[len("/api/") :]
        prefix = []
        tag = None
    else:
        rest = full_path.lstrip("/")
        prefix = ["public"]
        tag = "public"
    segs = [s for s in rest.split("/") if s]
    static = [
        re.sub(r"[:{}]", "", s).replace("-", "_")
        for s in segs
        if not s.startswith(":") and not s.startswith("{")
    ]
    last_param = bool(segs) and (segs[-1].startswith(":") or segs[-1].startswith("{"))
    if tag is None:
        tag = static[0] if static else "api"
        if tag in {"login", "register"}:
            tag = "auth"
            if static and static[0] != "auth":
                static = ["auth", *static]
    parts = prefix + static
    if last_param:
        parts.append("by_id")
    verb = {
        "GET": "get" if last_param or (static and segs and "-" in segs[-1]) else "list",
        "POST": "create",
        "PUT": "update",
        "PATCH": "patch",
        "DELETE": "delete",
    }[method]
    if method == "POST" and static and not last_param:
        last = segs[-1]
        if "-" in last or last in {
            "login",
            "register",
            "enroll",
            "preview",
            "export",
            "import",
            "test",
            "sync",
            "interrupt",
            "rebuild",
        }:
            verb = last.replace("-", "_")
            if parts[-1] == last.replace("-", "_"):
                parts = parts[:-1]
    parts.append(verb)
    op_id = "_".join(x for x in parts if x)
    return tag, op_id


setup = server_fn("setupRoutes")
handler_pkg = parse_handler_pkg(setup)
groups = {"s.Router": ("", "public")}
paths, provenance, excluded, used_ids = {}, [], [], set()

ROUTE_RE = re.compile(
    r'(?P<recv>\w+(?:\.\w+)?)\.(?P<method>GET|POST|PUT|PATCH|DELETE)\("(?P<path>[^"]+)"(?P<rest>.*)$'
)
ADAPT_RE = re.compile(r"api\.Adapt\(\s*adapter,\s*api\.(?P<mode>\w+),\s*(?P<var>\w+)\.(?P<fn>\w+)\s*\)")
SPECIAL_RE = re.compile(r"(?P<var>\w+)\.(?P<fn>ExportHTTP|ImportHTTP)\(")
GROUP_RE = re.compile(r'(?P<name>\w+)\s*:?=\s*(?P<recv>\w+(?:\.\w+)?)\.Group\("(?P<prefix>[^"]+)"\)')

for lineno, raw in enumerate(setup.splitlines(), 1):
    line = raw.strip()
    if not line:
        continue
    group_match = GROUP_RE.search(line)
    if group_match:
        prefix = groups.get(group_match.group("recv"), ("", "public"))[0] + group_match.group("prefix")
        auth = "admin" if prefix.endswith("/admin") else "user" if prefix == "/api" else "public"
        groups[group_match.group("name")] = (prefix, auth)
        continue
    route = ROUTE_RE.search(line)
    if not route:
        continue
    method = route.group("method").lower()
    rel = route.group("path")
    prefix, auth = groups.get(route.group("recv"), ("", "public"))
    full = prefix + rel
    source = f"internal/master/server.go:setupRoutes:{lineno}"
    if (route.group("method"), full) in EXCLUDE:
        excluded.append({"method": method, "path": full, "reason": EXCLUDE_REASON[full], "source": source})
        continue
    adapt = ADAPT_RE.search(route.group("rest"))
    special = SPECIAL_RE.search(route.group("rest"))
    openapi_path = gin_to_openapi(full)
    tag, op_id = operation_meta(full, route.group("method"))
    while op_id in used_ids:
        op_id += "_dup"
    used_ids.add(op_id)
    security = [] if auth == "public" else [{"bearerAuth": []}]
    params = path_params_from_gin(full)
    request_body = None
    response_schema = {"type": "object", "additionalProperties": True}
    req_name = resp_name = None
    status = "201" if route.group("method") == "POST" and op_id.endswith("_create") else "200"
    if adapt:
        pkg = handler_pkg.get(adapt.group("var"))
        fn = adapt.group("fn")
        mode = adapt.group("mode")
        assert pkg and pkg in packages, (full, adapt.group("var"), pkg)
        assert fn in packages[pkg]["methods"], (full, pkg, fn, list(packages[pkg]["methods"])[:30])
        req_name, resp_name = packages[pkg]["methods"][fn]
        json_props, required, extra_params, free_form = request_properties(pkg, req_name, mode)
        by_name = {p["name"]: p for p in params}
        for item in extra_params:
            by_name[item["name"]] = item
        params = list(by_name.values())
        if mode in JSON_BODY_MODES:
            if free_form:
                body_schema = {"type": "object", "additionalProperties": True}
            else:
                body_schema = {"type": "object", "properties": json_props}
                if required:
                    body_schema["required"] = required
            request_body = {
                "required": mode not in {"BindOptionalJSON", "BindURIAndOptionalJSON"},
                "content": {"application/json": {"schema": body_schema}},
            }
        response_schema = field_schema(resp_name, pkg)
        if resp_name.startswith("api.Created") or resp_name.startswith("Created["):
            status = "201"
        if resp_name.startswith("api.Accepted") or resp_name.startswith("Accepted["):
            status = "202"
    elif special:
        req_name = special.group("fn")
        if special.group("fn") == "ExportHTTP":
            request_body = {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "additionalProperties": True,
                            "description": "channel export selection",
                        }
                    }
                },
            }
        else:
            params.append({"name": "dry_run", "in": "query", "required": False, "schema": {"type": "boolean"}})
            request_body = {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "additionalProperties": True,
                            "description": "channel import file",
                        }
                    }
                },
            }
        resp_name = "ChannelFile"
    elif full == "/ping":
        response_schema = {
            "type": "object",
            "properties": {"status": {"type": "string"}, "role": {"type": "string"}},
        }
        req_name, resp_name = None, "PingResponse"
    else:
        excluded.append(
            {
                "method": method,
                "path": full,
                "reason": "non-Adapt handler left as protocol-specific",
                "source": source,
            }
        )
        used_ids.discard(op_id)
        continue

    op = {
        "operationId": op_id,
        "tags": [tag],
        "summary": f"{method.upper()} {openapi_path}",
        "security": security,
        "responses": {
            status: {
                "description": "JSON body of the handler return value; errors use HTTP status plus error/code fields",
                "content": {"application/json": {"schema": response_schema}},
            },
            "400": {
                "description": "bad request",
                "content": {"application/json": {"schema": schema_ref("ErrorBody")}},
            },
            "401": {
                "description": "missing or invalid bearer token",
                "content": {"application/json": {"schema": schema_ref("ErrorBody")}},
            },
        },
    }
    if params:
        op["parameters"] = params
    if request_body:
        op["requestBody"] = request_body
    if auth == "admin":
        op["responses"]["403"] = {
            "description": "admin role required",
            "content": {"application/json": {"schema": schema_ref("ErrorBody")}},
        }
    assert method not in paths.get(openapi_path, {}), (method, openapi_path, op_id)
    paths.setdefault(openapi_path, {})[method] = op
    provenance.append(
        {
            "method": method,
            "path": openapi_path,
            "gin_path": full,
            "auth": auth,
            "bind": adapt.group("mode") if adapt else special.group("fn") if special else None,
            "request": req_name,
            "response": resp_name,
            "operationId": op_id,
            "source": source,
        }
    )

schemas["ErrorBody"] = {
    "type": "object",
    "properties": {
        "error": {"type": "string"},
        "code": {"type": "string"},
        "message": {"type": "string"},
        "details": {"type": "object", "additionalProperties": True},
    },
}

out = root / "specs"
out.mkdir(exist_ok=True)
contract = {
    "openapi": "3.0.3",
    "info": {
        "title": "AI Gateway master HTTP API",
        "version": pinned,
        "description": "Reviewed management API reconstructed from setupRoutes. Relay /v1 and WebSocket endpoints are out of scope.",
    },
    "paths": dict(sorted(paths.items())),
    "components": {
        "securitySchemes": {"bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}},
        "schemas": dict(sorted(schemas.items())),
    },
}
(out / "openapi.json").write_text(json.dumps(contract, indent=2) + "\n")
(out / "sources.yaml").write_text(
    "sources:\n  master:\n    local_path: .\n    backend: openapi3\n    openapi3:\n      files: [openapi.json]\n"
)
(out / "review.json").write_text(
    json.dumps({"commit": pinned, "tag": "v0.0.20", "operations": provenance, "excluded": excluded}, indent=2)
    + "\n"
)
print(f"Reviewed {len(provenance)} operations, {len(schemas)} schemas; excluded {len(excluded)} nonstandard endpoints")
