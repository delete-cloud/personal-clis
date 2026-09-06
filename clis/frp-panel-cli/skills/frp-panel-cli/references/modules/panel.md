# Module `panel`

## Source

- Backend: `openapi3`
- Repository: `unknown`
- Pinned tag: ``unknown``
- Files: `openapi.json`

## auth

### `frp-panel-cli panel auth cert`

- Summary: auth cert
- HTTP: `POST /api/v1/auth/cert`
- Auth: public
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel auth login`

- Summary: auth login
- HTTP: `POST /api/v1/auth/login`
- Auth: public
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel auth register`

- Summary: auth register
- HTTP: `POST /api/v1/auth/register`
- Auth: public
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## client

### `frp-panel-cli panel client delete`

- Summary: client delete
- HTTP: `POST /api/v1/client/delete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel client get`

- Summary: client get
- HTTP: `POST /api/v1/client/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel client init`

- Summary: client init
- HTTP: `POST /api/v1/client/init`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel client install-workerd`

- Summary: client install_workerd
- HTTP: `POST /api/v1/client/install_workerd`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel client list`

- Summary: client list
- HTTP: `POST /api/v1/client/list`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel client upgrade`

- Summary: client upgrade
- HTTP: `POST /api/v1/client/upgrade`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## frpc

### `frp-panel-cli panel frpc delete`

- Summary: frpc delete
- HTTP: `POST /api/v1/frpc/delete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel frpc start`

- Summary: frpc start
- HTTP: `POST /api/v1/frpc/start`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel frpc stop`

- Summary: frpc stop
- HTTP: `POST /api/v1/frpc/stop`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel frpc update`

- Summary: frpc update
- HTTP: `POST /api/v1/frpc/update`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## frps

### `frp-panel-cli panel frps delete`

- Summary: frps delete
- HTTP: `POST /api/v1/frps/delete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel frps update`

- Summary: frps update
- HTTP: `POST /api/v1/frps/update`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## platform

### `frp-panel-cli panel platform baseinfo`

- Summary: platform baseinfo
- HTTP: `GET /api/v1/platform/baseinfo`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel platform clientsstatus`

- Summary: platform clientsstatus
- HTTP: `POST /api/v1/platform/clientsstatus`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## proxy

### `frp-panel-cli panel proxy create-config`

- Summary: proxy create_config
- HTTP: `POST /api/v1/proxy/create_config`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel proxy delete-config`

- Summary: proxy delete_config
- HTTP: `POST /api/v1/proxy/delete_config`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel proxy get-by-cid`

- Summary: proxy get_by_cid
- HTTP: `POST /api/v1/proxy/get_by_cid`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel proxy get-by-sid`

- Summary: proxy get_by_sid
- HTTP: `POST /api/v1/proxy/get_by_sid`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel proxy get-config`

- Summary: proxy get_config
- HTTP: `POST /api/v1/proxy/get_config`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel proxy list-configs`

- Summary: proxy list_configs
- HTTP: `POST /api/v1/proxy/list_configs`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel proxy start-proxy`

- Summary: proxy start_proxy
- HTTP: `POST /api/v1/proxy/start_proxy`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel proxy stop-proxy`

- Summary: proxy stop_proxy
- HTTP: `POST /api/v1/proxy/stop_proxy`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel proxy update-config`

- Summary: proxy update_config
- HTTP: `POST /api/v1/proxy/update_config`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## server

### `frp-panel-cli panel server delete`

- Summary: server delete
- HTTP: `POST /api/v1/server/delete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel server get`

- Summary: server get
- HTTP: `POST /api/v1/server/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel server init`

- Summary: server init
- HTTP: `POST /api/v1/server/init`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel server list`

- Summary: server list
- HTTP: `POST /api/v1/server/list`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## user

### `frp-panel-cli panel user get`

- Summary: user get
- HTTP: `POST /api/v1/user/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel user sign-token`

- Summary: user sign-token
- HTTP: `POST /api/v1/user/sign-token`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel user update`

- Summary: user update
- HTTP: `POST /api/v1/user/update`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## wg

### `frp-panel-cli panel wg create`

- Summary: wg create
- HTTP: `POST /api/v1/wg/create`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg delete`

- Summary: wg delete
- HTTP: `POST /api/v1/wg/delete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg endpoint-create`

- Summary: wg endpoint create
- HTTP: `POST /api/v1/wg/endpoint/create`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg endpoint-delete`

- Summary: wg endpoint delete
- HTTP: `POST /api/v1/wg/endpoint/delete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg endpoint-get`

- Summary: wg endpoint get
- HTTP: `POST /api/v1/wg/endpoint/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg endpoint-list`

- Summary: wg endpoint list
- HTTP: `POST /api/v1/wg/endpoint/list`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg endpoint-update`

- Summary: wg endpoint update
- HTTP: `POST /api/v1/wg/endpoint/update`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg get`

- Summary: wg get
- HTTP: `POST /api/v1/wg/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg link-create`

- Summary: wg link create
- HTTP: `POST /api/v1/wg/link/create`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg link-delete`

- Summary: wg link delete
- HTTP: `POST /api/v1/wg/link/delete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg link-get`

- Summary: wg link get
- HTTP: `POST /api/v1/wg/link/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg link-list`

- Summary: wg link list
- HTTP: `POST /api/v1/wg/link/list`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg link-update`

- Summary: wg link update
- HTTP: `POST /api/v1/wg/link/update`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg list`

- Summary: wg list
- HTTP: `POST /api/v1/wg/list`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg network-create`

- Summary: wg network create
- HTTP: `POST /api/v1/wg/network/create`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg network-delete`

- Summary: wg network delete
- HTTP: `POST /api/v1/wg/network/delete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg network-get`

- Summary: wg network get
- HTTP: `POST /api/v1/wg/network/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg network-list`

- Summary: wg network list
- HTTP: `POST /api/v1/wg/network/list`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg network-topology`

- Summary: wg network topology
- HTTP: `POST /api/v1/wg/network/topology`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg network-update`

- Summary: wg network update
- HTTP: `POST /api/v1/wg/network/update`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg restart`

- Summary: wg restart
- HTTP: `POST /api/v1/wg/restart`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg runtime-get`

- Summary: wg runtime get
- HTTP: `POST /api/v1/wg/runtime/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel wg update`

- Summary: wg update
- HTTP: `POST /api/v1/wg/update`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## worker

### `frp-panel-cli panel worker create`

- Summary: worker create
- HTTP: `POST /api/v1/worker/create`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel worker create-ingress`

- Summary: worker create_ingress
- HTTP: `POST /api/v1/worker/create_ingress`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel worker get`

- Summary: worker get
- HTTP: `POST /api/v1/worker/get`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel worker get-ingress`

- Summary: worker get_ingress
- HTTP: `POST /api/v1/worker/get_ingress`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel worker list`

- Summary: worker list
- HTTP: `POST /api/v1/worker/list`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel worker redeploy`

- Summary: worker redeploy
- HTTP: `POST /api/v1/worker/redeploy`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel worker remove`

- Summary: worker remove
- HTTP: `POST /api/v1/worker/remove`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel worker status`

- Summary: worker status
- HTTP: `POST /api/v1/worker/status`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `frp-panel-cli panel worker update`

- Summary: worker update
- HTTP: `POST /api/v1/worker/update`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`
