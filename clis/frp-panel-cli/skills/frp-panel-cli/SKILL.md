---
name: frp-panel-cli
description: >
  Use when operating the frp-panel-cli generated CLI. Discover commands, inspect parameters,
  check auth state, and execute API operations safely.
---

# frp-panel-cli CLI

Use this skill when a user asks you to operate `frp-panel-cli`, inspect its API commands, or find the right generated command for an API task.

## Workflow

1. Search for candidates with `frp-panel-cli search "<intent>" --json`; use `--limit` when needed. Search is only candidate discovery.
2. Inspect the exact command with `frp-panel-cli commands show <path...> --json` before executing an unfamiliar command.
3. If the command detail has `auth.required=true`, run `frp-panel-cli auth status -o json` before execution and read `hostname` and `source`. Host resolution order: `--hostname` > `$FRP_PANEL_HOST` > the selected host (`frp-panel-cli auth use <host>`) > `http.default_hostname` > the single host in `hosts.yml`. If none applies, stop and ask the user to authenticate or select a host.
4. Execute only after flags, body, auth, HTTP path, `mutation`, `dry_run`, and output hints are clear from `commands show`. When `mutation` is not `read`, preview with `--<dry_run.flag>` if `dry_run.mode` is `http_preview`; if preview is unavailable, obtain explicit user confirmation before execution.

## General Commands

- `frp-panel-cli commands --json`: full generated command catalog.
- `frp-panel-cli commands --include-hidden --json`: include hidden generated commands.
- `frp-panel-cli commands show <path...> --json`: source of truth for one command.
- `frp-panel-cli commands schema --json`: catalog schema version, surfaces, and dry-run result shape.
- `frp-panel-cli search "<intent>" --json`: ranked candidate commands.
- `frp-panel-cli auth status -o json`: resolved `hostname`, its `source`, the `selected` host, and every logged-in host.

## Maintenance Commands

- `frp-panel-cli --version` or `frp-panel-cli -v`: print CLI build version.

## References

- Read `references/catalog.md` for the command discovery protocol and catalog field meanings.
- Read `references/modules/panel.md` for the `panel` module command index.

## Rules

- Do not guess flags or request body shape from command names.
- Do not execute directly from search results; confirm with `commands show` first.
- When `mutation` is not `read`, preview before execution if `dry_run.mode` is `http_preview`. If preview is unavailable, obtain explicit user confirmation before execution. `unknown` is not safe to treat as read.
- Prefer `-o json` for machine-readable command output unless the user asks for human-readable output.
- With `-o json` or `-o yaml`, branch on `error.code` and process exit status; `error.message` and `error.hint` are safe human guidance, and `error.http.status` is the only optional HTTP context.
- A configured stream pause is successful (`exit 0`); inspect the collected output field mapped from the pause event instead of treating it as an error.
- For collected streams, choose one mode: `-o json` for one stable document, `--stream` in the default output mode when catalog `output.streaming.policy.live` is present, or `-o raw` for wire events.
- Use `--file`, `--set`, or `--set-str` for JSON request bodies according to `commands show` body requirements.
- When `body.runtime_schema` is present, normal execution fetches and validates against that schema before the target request; an `http_preview` dry-run stays network-free and skips this preflight.
- For sensitive flags, prefer safe modes from `flags[].input_modes`: `--<flag>-env`, `--<flag>-file`, or `--<flag>-stdin`.
