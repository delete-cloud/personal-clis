The raw lathe-scan output is preserved in ../scan. Do not bootstrap that draft.

Reviewed input: VaalaCat/ai-gateway commit 7ab85dadbc4e5652181ef7c8036521dca33236de (tag v0.0.20).
lathe-scan recovered 262 gin routes at medium confidence but omitted group prefixes,
request bodies, response shapes, and auth. It also picked up test-only paths such as
/accepted from response_test.go.

scripts/review_contract.py reconstructs the management contract from setupRoutes in
internal/master/server.go. Each api.Adapt handler is joined to its request/response
Go types; JSON/form/uri tags become body, query, or path parameters. Bearer JWT
follows middleware/auth.go. /api/admin additionally requires the admin role.
JSON responses are the handler return value; this API does not wrap success in a
{code,msg,body} envelope. Errors use HTTP status with {"error": "..."} or
{"code","message","details"}.

Included: /ping, public login/register/enroll/public-config/oauth JSON endpoints,
user-authenticated /api/* portal routes, and /api/admin/* management routes.
Excluded: Prometheus /metrics, /ws/agent and /ws/agent-relay, agent usage ingest
/api/agents/usage, and browser OAuth authorize/callback/link redirects. Relay
OpenAI/Claude /v1 endpoints are out of scope; use an OpenAI-compatible client.

Channel export/import keep JSON file bodies. The import query `dry_run` becomes
CLI `--dry-run`, which shadows Lathe's HTTP preview flag; `channels-import --dry-run`
calls the API with `dry_run=true` instead of printing a request preview.
BodyMapSetter PATCH/PUT endpoints accept a free-form object. Schemas are discovery
metadata, not complete business validators. All POST commands conservatively retain
Lathe's write classification, including some read-oriented actions.

No production host or credentials are bundled. Tests must stay on loopback.
