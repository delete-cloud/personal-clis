# frp-panel-cli

本地生成的 frp-panel HTTP API CLI，包含 65 个命令。这是集合仓库中的独立 Go 模块。API 合约来自固定版本的上游源码，生成与测试不需要线上面板。

## 使用

先运行 `make build`，再将 `bin/frp-panel-cli` 放到 PATH（例如安装到 `~/.local/bin/`）：

```sh
frp-panel-cli --help
frp-panel-cli search 'client list' --json
frp-panel-cli commands show panel client list --json
frp-panel-cli panel client list --hostname http://127.0.0.1:9000 \
  --set page=1 --set page_size=20 --dry-run
```

`--dry-run` 只打印请求，不联网。未配置默认服务器；实际调用需要通过 `--hostname` 或 `FRP_PANEL_HOST` 指定自己的面板地址。

配置已有 JWT（以下是用户手动执行步骤；token 文件须放在仓库外）：

```sh
export FRP_PANEL_HOST='https://your-panel.example'
frp-panel-cli auth login --hostname "$FRP_PANEL_HOST" --with-token --skip-validate < /path/outside/repo/token.txt
frp-panel-cli panel client list --set page=1 --set page_size=20 -o json
```

`auth login` 保存已有 token，不是账号密码登录；`--skip-validate` 只保存，不证明凭据有效。
账号密码登录 API 是 `panel auth login --file /path/outside/repo/login.json -o json`；
文件形状为 `{"username":"...","password":"..."}`，从响应 `body.token` 获取 JWT 后再保存。
凭据默认存储于 `~/.config/frp-panel-cli/`，可用 `FRP_PANEL_CLI_CONFIG_DIR` 覆盖。

```sh
frp-panel-cli panel server list --file /path/to/empty-object.json -o json
frp-panel-cli panel proxy list-configs --help
frp-panel-cli panel wg network-list --help
```

空请求也需要 JSON `{}`；可通过 `--file` 或 stdin 提供。复杂结构使用 `--file`、`--set nested.field=value`；字节字段使用 base64 字符串。参数的业务必填约束仍以服务端实现为准。

**业务错误检查：** frp-panel 的失败也可能返回 HTTP 200。CLI 保留原始 `{code,msg,body}` 响应，此时退出码可能仍为 0。脚本必须检查 `.code == 200`，不能只检查进程退出码。例如已有 jq 时：

```sh
set -o pipefail
frp-panel-cli panel client list --set page=1 -o json | jq -e 'select(.code == 200)'
```

所有 POST 在命令目录中保守标为 write，包括 list/get。修改命令先查看 `commands show` 和 `--dry-run`，实际执行需要用户明确选择目标和操作。

## 重新生成与验证

要求 Go >= 1.25.13、lathe 0.6.1、Python 3、make。

```sh
cd clis/frp-panel-cli
make generate build test
```

- `scan/`：lathe-scan 原始报告（仅将本机绝对路径替换成相对路径）；其中的草稿缺少路由前缀、请求体和鉴权，不能直接用作最终输入。
- `specs/openapi.json`：根据源码补齐、审核的 API 合约。
- `specs/review.json`、`specs/REVIEW.md`：逐路由来源和扫描缺口处理说明。
- `internal/generated/`：lathe 生成的 Go 命令。
- `skills/frp-panel-cli/`：生成的 Agent Skill，尚未安装到任何 agent。
- `scripts/smoke.py`：只在 loopback 上测试，使用临时配置和虚构 token。

复现扫描与合约审核：

```sh
git clone https://github.com/VaalaCat/frp-panel.git upstream/frp-panel
git -C upstream/frp-panel checkout --detach 1a58b856d7de19de8669b7072872986d2fa1604a
lathe-scan upstream/frp-panel --out scan-recheck
python3 scripts/review_contract.py upstream/frp-panel
make generate build test
```

审核脚本要求上游 checkout 干净且 commit 为 `1a58b856d7de19de8669b7072872986d2fa1604a`；升级版本需重新核对。
65 个接口的 catalog、dry-run、实际 loopback HTTP 方法/路径/请求体及鉴权均测试；这不代表已对真实面板做端到端验收。
未包含 FRP `/auth` 插件回调、cookie logout、PTY/log WebSocket、内部 gRPC agent 协议。

初始验证使用的工具版本：gh 2.100.0、lathe 0.6.1、lathe-scan 0.1.0（模块 `v0.0.0-20260818140519-11290dbf7071`）、Go 1.27.1。
官方来源：https://github.com/lathe-cli/lathe 和 https://github.com/lathe-cli/lathe-scan 。
上游 frp-panel 派生合约的许可证原文保留于 `LICENSE.frp-panel`。

## 删除本地安装

删除 `~/.local/bin/frp-panel-cli` 即取消 CLI 命令；源码和配置可按需单独保留。任何构建、测试或删除本地安装都不会修改线上 frp-panel。
