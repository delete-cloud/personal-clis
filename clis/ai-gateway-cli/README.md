# ai-gateway-cli

本地生成的 AI Gateway master HTTP API CLI，包含 252 个命令。这是集合仓库中的独立 Go 模块。API 合约来自固定版本的上游源码，生成与测试不需要线上网关。

## 使用

先运行 `make build`，再将 `bin/ai-gateway-cli` 放到 PATH（例如安装到 `~/.local/bin/`）：

```sh
ai-gateway-cli --help
ai-gateway-cli search 'channel list' --json
ai-gateway-cli commands show master admin channels-list --json
ai-gateway-cli master public ping-get --hostname http://127.0.0.1:8140 --dry-run
ai-gateway-cli master auth login --hostname http://127.0.0.1:8140 \
  --file /path/outside/repo/login.json --dry-run
```

普通命令的 `--dry-run` 只打印解析后的请求，不联网。例外是两个 import 命令
（`master admin channels-import`、`master private_channels private-channels-import`）：它们的 API query 参数
`dry_run` 占用了 `--dry-run` 这个名字，Lathe 的预览开关被挤到 `--lathe-dry-run`，所以
`channels-import --dry-run` 会真的发 HTTP（POST 到 import 路径，query `dry_run=true`），不打印预览。
这两条 import 的 body 都是必填 JSON，发请求（包括 `--dry-run`）必须带 `--file`；
只想看解析后的请求、不联网，用 `--file … --lathe-dry-run`。
未配置默认服务器；实际调用需要通过 `--hostname` 或 `AI_GATEWAY_HOST` 指定自己的 master 地址。

配置已有 JWT（用户手动执行；token 文件须放在仓库外）：

```sh
export AI_GATEWAY_HOST='https://your-gateway.example'
ai-gateway-cli auth login --hostname "$AI_GATEWAY_HOST" --with-token --skip-validate < /path/outside/repo/token.txt
ai-gateway-cli master admin channels-list --page 1 --page-size 20 -o json
```

`auth login` 保存已有 token，不是账号密码登录；`--skip-validate` 只保存，不证明凭据有效。
账号密码登录 API 是 `master auth login --file /path/outside/repo/login.json -o json`；
文件形状为 `{"username":"...","password":"..."}`，从响应 `token` 获取 JWT 后再保存。
凭据默认存储于 `~/.config/ai-gateway-cli/`，可用 `AI_GATEWAY_CLI_CONFIG_DIR` 覆盖。

成功响应是 handler 的 JSON 本体，没有 frp-panel 那种 `{code,msg,body}` 包裹。HTTP 4xx/5xx 才会带 `error` 或 `code`/`message`。管理接口在 `/api/admin`，需要 admin 角色的 JWT。

OpenAI/Claude 兼容的 `/v1/*` 中继、WebSocket 和控制面 Prometheus `/metrics` 不在本 CLI 范围内。

## 重新生成与验证

要求 Go >= 1.25.13、lathe 0.6.1、lathe-scan 0.1.0、Python 3、make。

```sh
cd clis/ai-gateway-cli
make generate build test
```

- `scan/`：lathe-scan 原始报告（绝对路径已改成相对路径）；草稿缺少路由前缀、请求体和鉴权，不能直接用作最终输入。
- `specs/openapi.json`：根据源码补齐、审核的 API 合约。
- `specs/review.json`、`specs/REVIEW.md`：逐路由来源和扫描缺口处理说明。
- `skills/ai-gateway-cli/`：生成的 Agent Skill。先 `make skill-install-dry` 查看 kitup 计划，确认后再 `make skill-install`。
- `scripts/smoke.py`：只在 loopback 上测试，使用临时配置和虚构 token。

复现扫描与合约审核：

```sh
git clone https://github.com/VaalaCat/ai-gateway.git upstream/ai-gateway
git -C upstream/ai-gateway checkout --detach 7ab85dadbc4e5652181ef7c8036521dca33236de
lathe-scan upstream/ai-gateway --out scan-recheck
python3 scripts/review_contract.py upstream/ai-gateway
make generate build test
```

审核脚本要求上游 checkout 干净且 commit 为 `7ab85dadbc4e5652181ef7c8036521dca33236de`（v0.0.20）；升级版本需重新核对。
252 个接口的 catalog、实际 loopback HTTP 方法/路径/请求体及鉴权均测试；其中 250 条普通命令用 `--dry-run` 验证了
network-free 预览（断言没有发出 HTTP），2 条 import 命令用 `--lathe-dry-run` 验证预览、用 `--dry-run` 按 API 语义发到
loopback（断言 POST 方法、路径和 query `dry_run=true`）。HTTP 次数是 252 次正式请求 + 2 次 import `--dry-run`，共 254 次。
这不代表已对真实网关做端到端验收。

初始验证使用的工具版本：gh 2.100.0、lathe 0.6.1、lathe-scan 0.1.0、Go 1.27.1。
官方来源：https://github.com/lathe-cli/lathe 、https://github.com/lathe-cli/lathe-scan 、https://github.com/lathe-cli/kitup 。
上游 AI Gateway 许可证原文保留于 `LICENSE.ai-gateway`。

## 删除本地安装

删除 `~/.local/bin/ai-gateway-cli` 即取消 CLI 命令；源码和配置可按需单独保留。
已安装的 Agent Skill 可用 `lathe skill uninstall` 或生成 CLI 的 `skill uninstall`（若存在）移除。
任何构建、测试或删除本地安装都不会修改线上 AI Gateway。
