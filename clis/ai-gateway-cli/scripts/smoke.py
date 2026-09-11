"""Exercise generated commands against loopback only, using synthetic credentials."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json, os, re, subprocess, tempfile, threading

root = Path(__file__).resolve().parents[1]
binary = root / "bin/ai-gateway-cli"
calls = []
response = {"status": "ok", "items": []}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        self.reply()

    def do_POST(self):
        self.reply()

    def do_PUT(self):
        self.reply()

    def do_PATCH(self):
        self.reply()

    def do_DELETE(self):
        self.reply()

    def reply(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b""
        calls.append(
            (
                self.command,
                self.path,
                self.headers.get("Authorization"),
                json.loads(body) if body else None,
            )
        )
        data = json.dumps(response).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
try:
    with tempfile.TemporaryDirectory(prefix="ai-gateway-cli-test-") as tmp:
        env = dict(
            os.environ,
            AI_GATEWAY_CLI_CONFIG_DIR=tmp,
            AI_GATEWAY_HOST=f"http://127.0.0.1:{server.server_port}",
        )

        def run(*args, stdin=None):
            proc = subprocess.run(
                [str(binary), *args],
                input=stdin,
                text=True,
                capture_output=True,
                env=env,
                timeout=15,
            )
            assert proc.returncode == 0, (args, proc.stderr)
            if proc.stdout.strip().startswith("{") or proc.stdout.strip().startswith("["):
                return json.loads(proc.stdout)
            return proc.stdout

        assert run("__lathe", "verify", "--json")["ok"]
        catalog = run("commands", "--json")["commands"]
        review = json.loads((root / "specs/review.json").read_text())
        expected = {(item["method"].upper(), item["path"]) for item in review["operations"]}
        catalog_paths = {(item["http"]["method"], item["http"]["path_template"]) for item in catalog}
        assert catalog_paths == expected
        assert len(catalog) == 252
        run(
            "auth",
            "login",
            "--hostname",
            env["AI_GATEWAY_HOST"],
            "--with-token",
            "--skip-validate",
            stdin="synthetic-test-token\n",
        )
        assert not calls
        empty = Path(tmp) / "empty.json"
        empty.write_text("{}")

        def dummy(flag):
            kind = str(flag.get("type") or "string")
            if kind in {"integer", "int", "int32", "int64", "uint", "number"}:
                return "1"
            if kind in {"boolean", "bool"}:
                return "true"
            return f"smoke-{flag['name']}"

        def extra_flags(item):
            flags = []
            path = item["http"]["path_template"]
            names = re.findall(r"\{(\w+)\}", path)
            seen = set()
            for flag in item.get("flags") or []:
                if not flag.get("required"):
                    continue
                if flag.get("location") not in {"path", "query"}:
                    continue
                value = dummy(flag)
                flags.extend([f"--{flag['flag']}", value])
                seen.add(flag["name"])
                if flag.get("location") == "path":
                    path = path.replace("{" + flag["name"] + "}", value)
            for name in names:
                if name in seen:
                    continue
                value = f"smoke-{name}"
                flags.extend([f"--{name}", value])
                path = path.replace("{" + name + "}", value)
            return flags, path

        actual = set()
        for item in catalog:
            flag_args, filled = extra_flags(item)
            needs_body = bool(item.get("body"))
            body = ["--file", str(empty)] if needs_body else []
            args = [*item["path"], *flag_args]
            collides = any((flag.get("flag") == "dry-run") for flag in item.get("flags") or [])
            before = len(calls)
            if not collides:
                preview = run(*args, *body, "--dry-run")
                assert len(calls) == before, (item["path"], calls[before:])
                preview_path = preview["url"].split("?", 1)[0]
                assert preview_path == env["AI_GATEWAY_HOST"] + filled, (preview["url"], filled)
            got = run(*args, *body, "-o", "json")
            assert got == response
            method, path, auth, payload = calls[-1]
            actual.add((method, path.split("?", 1)[0]))
            assert method == item["http"]["method"]
            assert path.split("?", 1)[0] == filled
            if item["auth"]["required"]:
                assert auth == "Bearer synthetic-test-token"
            if needs_body:
                assert payload == {}
            else:
                assert payload is None
        assert len(actual) == 252
        print(
            "PASS: 252 catalog contracts, 252 network-free previews, 252 loopback HTTP requests, Bearer auth, and JSON body handling"
        )
finally:
    server.shutdown()
    server.server_close()
    thread.join()
