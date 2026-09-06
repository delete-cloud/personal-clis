The raw lathe-scan output is preserved in ../scan. Do not bootstrap that draft.

Reviewed input: VaalaCat/frp-panel commit 1a58b856d7de19de8669b7072872986d2fa1604a.
The draft collapsed group-relative paths and reported missing bodies/auth/responses.
scripts/review_contract.py reconstructs full paths from ConfigureRouter, joins each
app.Wrapper handler to its protobuf request/response Go struct, and models the JSON
response envelope in common/result.go. Bearer auth follows middleware/jwt.go;
only cert/login/register are public. JSON snake_case request keys are accepted by
common/request.go's protojson.Unmarshal. Schemas are discovery metadata, not complete
business validators: handler-specific required fields are not inferred. Integer enum
values and base64 strings for bytes are supported. Nested messages remain objects.

65 HTTP operations are included; review.json records every route and handler line.
/auth is an FRP plugin callback, logout is a cookie operation, and pty/log require
WebSocket protocols. These four routes are excluded. The unannotated RPC service is
an internal agent protocol, not the HTTP management API, resolving proto-no-http-annotation
by explicitly excluding it from this CLI scope.

All POST commands conservatively retain Lathe's write classification, including
read-oriented list/get operations. No production host or credentials are bundled.
The HTTP API may return code 500 with HTTP 200: check the JSON envelope's code,
not just shell exit status. Outputs intentionally preserve that envelope.
