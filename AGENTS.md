# Repository instructions

- Each CLI is an independent project under clis/. Keep changes scoped to the requested CLI.
- No production hosts or credentials in tracked files. Do not execute live mutations as tests.
- Preserve upstream provenance and licenses. Pin upstream revisions used for generation.
- Review scanner gaps before generation. Generated code is not the editing source of truth.
- For frp-panel-cli, run make generate build test in its directory after contract/config changes.
- Tests use loopback only and synthetic credentials. Do not replace them with live service probes.
- frp-panel may return business errors with HTTP 200. Check response code == 200 separately.
- Do not commit bin/, .cache/, upstream checkouts, or local auth config.
