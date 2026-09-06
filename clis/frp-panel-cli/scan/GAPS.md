# lathe-scan gaps

1 input(s), 1 source(s), 1 usable.

## Sources

- **frp_panel** (recommended) — backend `openapi3`, confidence `medium`, 54 command(s)
  - origin: local_path `frp_panel`

## Blocking — must resolve before generating

- `proto-no-http-annotation` [input idl] 11 rpc across 1 service(s) but no google.api.http annotation; Lathe would emit no commands, so no proto source was written

## Advisory

- `body` [source frp_panel] request bodies were not recovered from source
- `response` [source frp_panel] response shapes were not recovered from source
- `auth` [source frp_panel] auth requirements were not recovered from source
- `dynamic-route` [source frp_panel] prefixes from route groups or class-level mappings may not be applied; verify full paths

## Next

Review sources and origins above. If this directory is your application's `specs/`, run:

```sh
lathe bootstrap
```

Otherwise name the manifest explicitly: `lathe bootstrap -sources <this-dir>/sources.yaml`.
