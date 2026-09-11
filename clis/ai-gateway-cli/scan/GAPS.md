# lathe-scan gaps

1 input(s), 1 source(s), 1 usable.

## Sources

- **ai_gateway** (recommended) — backend `openapi3`, confidence `medium`, 262 command(s)
  - origin: local_path `ai_gateway`

## Advisory

- `body` [source ai_gateway] request bodies were not recovered from source
- `response` [source ai_gateway] response shapes were not recovered from source
- `auth` [source ai_gateway] auth requirements were not recovered from source
- `dynamic-route` [source ai_gateway] prefixes from route groups or class-level mappings may not be applied; verify full paths

## Next

Review sources and origins above. If this directory is your application's `specs/`, run:

```sh
lathe bootstrap
```

Otherwise name the manifest explicitly: `lathe bootstrap -sources <this-dir>/sources.yaml`.
