# personal-clis

个人常用项目的 CLI 集合。每个 CLI 放在 `clis/<name>/`，独立生成、构建和验证。
仓库只保存源码、API 合约、生成配置和测试，不包含访问凭据或默认生产地址。

| CLI | 上游 | 能力 |
| --- | --- | --- |
| [frp-panel-cli](clis/frp-panel-cli/) | [VaalaCat/frp-panel](https://github.com/VaalaCat/frp-panel) | 65 个 HTTP API 命令：client、server、proxy、worker、WireGuard 等 |

## 快速开始

构建要求：Go >= 1.25.13。运行测试还需 Python 3 和 make；重新生成需 lathe 0.6.1。

```sh
cd clis/frp-panel-cli
make build test
./bin/frp-panel-cli --help
./bin/frp-panel-cli commands show panel client list --json
./bin/frp-panel-cli panel client list --hostname http://127.0.0.1:9000 \
  --set page=1 --set page_size=20 --dry-run
```

`make test` 使用 loopback mock 和临时虚构凭据，不访问真实面板。
`--dry-run` 只预览请求；实际使用的主机和凭据由使用者自行配置。

可选安装：

```sh
mkdir -p "$HOME/.local/bin"
install -m 755 bin/frp-panel-cli "$HOME/.local/bin/frp-panel-cli"
```

## CLI 是怎么生成的

1. 固定上游源码 commit，以便追溯和重复审核。
2. 用 [lathe-scan](https://github.com/lathe-cli/lathe-scan) 静态发现 API，保留扫描报告和缺口。
3. 对照源码补齐并审核 OpenAPI：路径前缀、JSON 请求体、响应包裹、鉴权和协议边界。
4. 用 [lathe](https://github.com/lathe-cli/lathe) `bootstrap` 从合约生成 Cobra 命令、机器可读目录和 Agent Skill。
5. 编译 Go 二进制，检查 catalog、无网络 dry-run 和本地 mock 请求。

frp-panel 的扫描草稿有 54 个不完整候选；路由前缀缺失还造成同名路径合并。
审核脚本从 Gin 路由及 protobuf Go 类型重建出 65 个 HTTP 接口，排除了插件回调、
cookie logout、PTY/log WebSocket 和内部 gRPC 协议。详见
[合约审核说明](clis/frp-panel-cli/specs/REVIEW.md)。

frp-panel 可能用 HTTP 200 返回业务错误。CLI 保留响应包裹；自动化脚本必须检查
响应 `code == 200`，不能只依赖进程退出码。

## 添加项目

每个目录至少包含：README、上游版本与来源、合约/来源配置、生成入口、构建命令、
本地测试和许可证。优先使用上游正式 API 合约；扫描结果须审核后才能用于生成。
不要手工修改 `internal/generated/`；修改合约或生成配置后重新生成。

## 许可证

各项目按其目录中的许可证和来源说明分开管理，不假设所有上游代码具有相同许可。
frp-panel 派生部分保留上游 AGPL-3.0 许可证，见
[LICENSE.frp-panel](clis/frp-panel-cli/LICENSE.frp-panel)。
Lathe 自身为 Apache-2.0，并对生成输出有许可例外；其依赖的许可仍各自适用。
本仓库新增的集合文档及 frp-panel 集成脚本采用 AGPL-3.0，许可证原文见 [LICENSE](LICENSE)。
