# Module `master`

## Source

- Backend: `openapi3`
- Repository: `unknown`
- Pinned tag: ``unknown``
- Files: `openapi.json`

## admin

### `ai-gateway-cli master admin agent-routes`

- Summary: POST /api/admin/agent-routes
- HTTP: `POST /api/admin/agent-routes`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin agent-routes-by-id-delete`

- Summary: DELETE /api/admin/agent-routes/{id}
- HTTP: `DELETE /api/admin/agent-routes/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agent-routes-by-id-get`

- Summary: GET /api/admin/agent-routes/{id}
- HTTP: `GET /api/admin/agent-routes/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agent-routes-by-id-update`

- Summary: PUT /api/admin/agent-routes/{id}
- HTTP: `PUT /api/admin/agent-routes/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agent-routes-get`

- Summary: GET /api/admin/agent-routes
- HTTP: `GET /api/admin/agent-routes`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--source-type` (query): source_type
  - `--source-id` (query): source_id
- Output: list path `data`; columns `id`, `agent_id`, `agent_tag`, `created_at`, `model`, `priority`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin agent-routes-overview-list`

- Summary: GET /api/admin/agent-routes/overview
- HTTP: `GET /api/admin/agent-routes/overview`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--q` (query): q
  - `--source-type` (query): source_type
  - `--source-id` (query): source_id
  - `--model` (query): model
  - `--agent-id` (query): agent_id
- Output: list path `data`; columns `id`, `agent_id`, `agent_name`, `agent_tag`, `created_at`, `model`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin agents-by-id-delete`

- Summary: DELETE /api/admin/agents/{id}
- HTTP: `DELETE /api/admin/agents/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-by-id-get`

- Summary: GET /api/admin/agents/{id}
- HTTP: `GET /api/admin/agents/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-by-id-update`

- Summary: PUT /api/admin/agents/{id}
- HTTP: `PUT /api/admin/agents/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-connections-diagnostics-list`

- Summary: GET /api/admin/agents/{id}/connections/diagnostics
- HTTP: `GET /api/admin/agents/{id}/connections/diagnostics`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-connections-targets-list`

- Summary: GET /api/admin/agents/{id}/connections/targets
- HTTP: `GET /api/admin/agents/{id}/connections/targets`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
  - `--cursor` (query): cursor
  - `--limit` (query): limit
  - `--expected-snapshot-epoch` (query): expected_snapshot_epoch
  - `--expected-snapshot-seq` (query): expected_snapshot_seq
- Output: response media `application/json`; pagination `cursor`

### `ai-gateway-cli master admin agents-connectivity-create`

- Summary: POST /api/admin/agents/{id}/connectivity
- HTTP: `POST /api/admin/agents/{id}/connectivity`
- Auth: required
- Body: optional; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-connectivity-list`

- Summary: GET /api/admin/agents/{id}/connectivity
- HTTP: `GET /api/admin/agents/{id}/connectivity`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
  - `--probe-id` (query): probe_id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-create`

- Summary: POST /api/admin/agents
- HTTP: `POST /api/admin/agents`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-detail-list`

- Summary: GET /api/admin/agents/{id}/detail
- HTTP: `GET /api/admin/agents/{id}/detail`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-enrollment-token`

- Summary: POST /api/admin/agents/enrollment-token
- HTTP: `POST /api/admin/agents/enrollment-token`
- Auth: required
- Body: optional; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-full-sync`

- Summary: POST /api/admin/agents/full-sync
- HTTP: `POST /api/admin/agents/full-sync`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-goroutines-list`

- Summary: GET /api/admin/agents/goroutines
- HTTP: `GET /api/admin/agents/goroutines`
- Auth: required
- Body: none
- Flags:
  - `--id` (query, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-inflight-all-list`

- Summary: GET /api/admin/agents/inflight/all
- HTTP: `GET /api/admin/agents/inflight/all`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-inflight-interrupt`

- Summary: POST /api/admin/agents/inflight/interrupt
- HTTP: `POST /api/admin/agents/inflight/interrupt`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-inflight-list`

- Summary: GET /api/admin/agents/inflight
- HTTP: `GET /api/admin/agents/inflight`
- Auth: required
- Body: none
- Flags:
  - `--id` (query, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin agents-list`

- Summary: GET /api/admin/agents
- HTTP: `GET /api/admin/agents`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--status` (query): status
- Output: list path `data`; columns `name`, `id`, `agent_id`, `configured_http_addresses`, `created_at`, `direct_inbound_enabled`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin agents-online-list`

- Summary: GET /api/admin/agents/online
- HTTP: `GET /api/admin/agents/online`
- Auth: required
- Body: none
- Flags: none
- Output: columns `name`, `agent_id`, `configured_http_addresses`, `effective_http_addresses`, `http_addresses`, `last_seen`; response media `application/json`

### `ai-gateway-cli master admin agents-operations-by-id-create`

- Summary: POST /api/admin/agents/{id}/operations/{operation}
- HTTP: `POST /api/admin/agents/{id}/operations/{operation}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
  - `--operation` (path, required): operation
- Output: response media `application/json`

### `ai-gateway-cli master admin api-access-grants-effective-list`

- Summary: GET /api/admin/api-access-grants/effective
- HTTP: `GET /api/admin/api-access-grants/effective`
- Auth: required
- Body: none
- Flags:
  - `--principal-type` (query, required): principal_type
  - `--principal-id` (query, required): principal_id
  - `--api-service-id` (query, required): api_service_id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-access-grants-get`

- Summary: GET /api/admin/api-access-grants
- HTTP: `GET /api/admin/api-access-grants`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--principal-type` (query): principal_type
  - `--principal-id` (query): principal_id
  - `--api-service-id` (query): api_service_id
  - `--search` (query): search
- Output: list path `data`; columns `api_service_id`, `api_service_name`, `principal_id`, `principal_label`, `principal_type`, `sources`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin api-access-grants-services-by-id-delete`

- Summary: DELETE /api/admin/api-access-grants/{principal_type}/{principal_id}/services/{service_id}
- HTTP: `DELETE /api/admin/api-access-grants/{principal_type}/{principal_id}/services/{service_id}`
- Auth: required
- Body: none
- Flags:
  - `--principal-type` (path, required): principal_type
  - `--principal-id` (path, required): principal_id
  - `--service-id` (path, required): service_id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-access-grants-services-by-id-update`

- Summary: PUT /api/admin/api-access-grants/{principal_type}/{principal_id}/services/{service_id}
- HTTP: `PUT /api/admin/api-access-grants/{principal_type}/{principal_id}/services/{service_id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--principal-type` (path, required): principal_type
  - `--principal-id` (path, required): principal_id
  - `--service-id` (path, required): service_id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-backends`

- Summary: POST /api/admin/api-backends
- HTTP: `POST /api/admin/api-backends`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-backends-by-id-delete`

- Summary: DELETE /api/admin/api-backends/{id}
- HTTP: `DELETE /api/admin/api-backends/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-backends-by-id-get`

- Summary: GET /api/admin/api-backends/{id}
- HTTP: `GET /api/admin/api-backends/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-backends-by-id-update`

- Summary: PUT /api/admin/api-backends/{id}
- HTTP: `PUT /api/admin/api-backends/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-backends-get`

- Summary: GET /api/admin/api-backends
- HTTP: `GET /api/admin/api-backends`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--api-service-id` (query): api_service_id
  - `--search` (query): search
- Output: list path `data`; columns `name`, `id`, `api_service_id`, `created_at`, `enabled_upstream_count`, `endpoint_hosts`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin api-request-logs-by-id-get`

- Summary: GET /api/admin/api-request-logs/{request_id}
- HTTP: `GET /api/admin/api-request-logs/{request_id}`
- Auth: required
- Body: none
- Flags:
  - `--request-id` (path, required): request_id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-request-logs-get`

- Summary: GET /api/admin/api-request-logs
- HTTP: `GET /api/admin/api-request-logs`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--api-service-id` (query): api_service_id
  - `--api-route-id` (query): api_route_id
  - `--api-upstream-id` (query): api_upstream_id
  - `--token-id` (query): token_id
  - `--status-code` (query): status_code
  - `--request-id` (query): request_id
- Output: list path `data`; columns `id`, `agent_route_id`, `agent_route_path`, `api_route_id`, `api_route_name`, `api_service_id`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin api-request-logs-trace-list`

- Summary: GET /api/admin/api-request-logs/{request_id}/trace
- HTTP: `GET /api/admin/api-request-logs/{request_id}/trace`
- Auth: required
- Body: none
- Flags:
  - `--request-id` (path, required): request_id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-request-traces-get`

- Summary: GET /api/admin/api-request-traces
- HTTP: `GET /api/admin/api-request-traces`
- Auth: required
- Body: none
- Flags:
  - `--request-id` (query, required): request_id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-role-bindings`

- Summary: POST /api/admin/api-role-bindings
- HTTP: `POST /api/admin/api-role-bindings`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-role-bindings-by-id-delete`

- Summary: DELETE /api/admin/api-role-bindings/{id}
- HTTP: `DELETE /api/admin/api-role-bindings/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-role-bindings-by-id-update`

- Summary: PUT /api/admin/api-role-bindings/{id}
- HTTP: `PUT /api/admin/api-role-bindings/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-role-bindings-get`

- Summary: GET /api/admin/api-role-bindings
- HTTP: `GET /api/admin/api-role-bindings`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--principal-type` (query): principal_type
  - `--principal-id` (query): principal_id
  - `--role-id` (query): role_id
- Output: list path `data`; columns `id`, `created_at`, `principal_id`, `principal_type`, `role_id`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin api-roles`

- Summary: POST /api/admin/api-roles
- HTTP: `POST /api/admin/api-roles`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-roles-by-id-delete`

- Summary: DELETE /api/admin/api-roles/{id}
- HTTP: `DELETE /api/admin/api-roles/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-roles-by-id-get`

- Summary: GET /api/admin/api-roles/{id}
- HTTP: `GET /api/admin/api-roles/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-roles-by-id-update`

- Summary: PUT /api/admin/api-roles/{id}
- HTTP: `PUT /api/admin/api-roles/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-roles-get`

- Summary: GET /api/admin/api-roles
- HTTP: `GET /api/admin/api-roles`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--status` (query): status
  - `--assignable` (query): assignable
- Output: list path `data`; columns `name`, `kind`, `id`, `built_in`, `created_at`, `description`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin api-routes`

- Summary: POST /api/admin/api-routes
- HTTP: `POST /api/admin/api-routes`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-routes-by-id-delete`

- Summary: DELETE /api/admin/api-routes/{id}
- HTTP: `DELETE /api/admin/api-routes/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-routes-by-id-get`

- Summary: GET /api/admin/api-routes/{id}
- HTTP: `GET /api/admin/api-routes/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-routes-by-id-update`

- Summary: PUT /api/admin/api-routes/{id}
- HTTP: `PUT /api/admin/api-routes/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-routes-get`

- Summary: GET /api/admin/api-routes
- HTTP: `GET /api/admin/api-routes`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--api-service-id` (query): api_service_id
  - `--search` (query): search
  - `--status` (query): status
- Output: list path `data`; columns `id`, `api_service_id`, `backend_id`, `created_at`, `forward_subpath`, `slug`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin api-routes-preview`

- Summary: POST /api/admin/api-routes/preview
- HTTP: `POST /api/admin/api-routes/preview`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-services`

- Summary: POST /api/admin/api-services
- HTTP: `POST /api/admin/api-services`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-services-by-id-delete`

- Summary: DELETE /api/admin/api-services/{id}
- HTTP: `DELETE /api/admin/api-services/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-services-by-id-get`

- Summary: GET /api/admin/api-services/{id}
- HTTP: `GET /api/admin/api-services/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-services-by-id-update`

- Summary: PUT /api/admin/api-services/{id}
- HTTP: `PUT /api/admin/api-services/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-services-get`

- Summary: GET /api/admin/api-services
- HTTP: `GET /api/admin/api-services`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--status` (query): status
- Output: list path `data`; columns `name`, `id`, `created_at`, `description`, `price_per_call`, `slug`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin api-services-openapi-import`

- Summary: POST /api/admin/api-services/openapi/import
- HTTP: `POST /api/admin/api-services/openapi/import`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-services-openapi-list`

- Summary: GET /api/admin/api-services/{id}/openapi
- HTTP: `GET /api/admin/api-services/{id}/openapi`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-services-openapi-preview`

- Summary: POST /api/admin/api-services/openapi/preview
- HTTP: `POST /api/admin/api-services/openapi/preview`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-services-openapi-update`

- Summary: PUT /api/admin/api-services/{id}/openapi
- HTTP: `PUT /api/admin/api-services/{id}/openapi`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-upstreams`

- Summary: POST /api/admin/api-upstreams
- HTTP: `POST /api/admin/api-upstreams`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin api-upstreams-by-id-delete`

- Summary: DELETE /api/admin/api-upstreams/{id}
- HTTP: `DELETE /api/admin/api-upstreams/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-upstreams-by-id-get`

- Summary: GET /api/admin/api-upstreams/{id}
- HTTP: `GET /api/admin/api-upstreams/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-upstreams-by-id-update`

- Summary: PUT /api/admin/api-upstreams/{id}
- HTTP: `PUT /api/admin/api-upstreams/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin api-upstreams-get`

- Summary: GET /api/admin/api-upstreams
- HTTP: `GET /api/admin/api-upstreams`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--api-service-id` (query): api_service_id
  - `--backend-id` (query): backend_id
  - `--search` (query): search
  - `--status` (query): status
- Output: list path `data`; columns `name`, `id`, `auth_type`, `backend_id`, `base_url`, `credential_configured`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin billing-channels-daily-list`

- Summary: GET /api/admin/billing/channels/{channel_id}/daily
- HTTP: `GET /api/admin/billing/channels/{channel_id}/daily`
- Auth: required
- Body: none
- Flags:
  - `--channel-id` (path, required): channel_id
  - `--start-date` (query): start_date
  - `--end-date` (query): end_date
- Output: response media `application/json`

### `ai-gateway-cli master admin billing-channels-list`

- Summary: GET /api/admin/billing/channels
- HTTP: `GET /api/admin/billing/channels`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--start-date` (query): start_date
  - `--end-date` (query): end_date
  - `--channel-id` (query): channel_id
  - `--search` (query): search
  - `--channel-type` (query): channel_type
  - `--min-tokens` (query): min_tokens
- Output: list path `data`; columns `cache_read_tokens`, `cache_write_tokens`, `channel_id`, `channel_name`, `channel_type`, `completion_tokens`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin billing-rebuild`

- Summary: POST /api/admin/billing/rebuild
- HTTP: `POST /api/admin/billing/rebuild`
- Auth: required
- Body: optional; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin billing-rebuild-jobs-by-id-get`

- Summary: GET /api/admin/billing/rebuild/jobs/{id}
- HTTP: `GET /api/admin/billing/rebuild/jobs/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin billing-rebuild-jobs-list`

- Summary: GET /api/admin/billing/rebuild/jobs
- HTTP: `GET /api/admin/billing/rebuild/jobs`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin byok-system-baseurls-get`

- Summary: GET /api/admin/byok-system-baseurls
- HTTP: `GET /api/admin/byok-system-baseurls`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin cache-stats-list`

- Summary: GET /api/admin/cache/stats
- HTTP: `GET /api/admin/cache/stats`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-batch-edit`

- Summary: POST /api/admin/channels/batch-edit
- HTTP: `POST /api/admin/channels/batch-edit`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-by-id-delete`

- Summary: DELETE /api/admin/channels/{id}
- HTTP: `DELETE /api/admin/channels/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-by-id-get`

- Summary: GET /api/admin/channels/{id}
- HTTP: `GET /api/admin/channels/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-by-id-update`

- Summary: PUT /api/admin/channels/{id}
- HTTP: `PUT /api/admin/channels/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-create`

- Summary: POST /api/admin/channels
- HTTP: `POST /api/admin/channels`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-dataflow-list`

- Summary: GET /api/admin/channels/{id}/dataflow
- HTTP: `GET /api/admin/channels/{id}/dataflow`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-export`

- Summary: POST /api/admin/channels/export
- HTTP: `POST /api/admin/channels/export`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-fetch-models`

- Summary: POST /api/admin/channels/fetch-models
- HTTP: `POST /api/admin/channels/fetch-models`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-import`

- Summary: POST /api/admin/channels/import
- HTTP: `POST /api/admin/channels/import`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--dry-run` (query): dry_run
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-list`

- Summary: GET /api/admin/channels
- HTTP: `GET /api/admin/channels`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--type` (query): type
  - `--status` (query): status
- Output: list path `data`; columns `name`, `type`, `id`, `api_version`, `auto_ban`, `auto_ban_revision`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin channels-test`

- Summary: POST /api/admin/channels/{id}/test
- HTTP: `POST /api/admin/channels/{id}/test`
- Auth: required
- Body: optional; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin channels-types-list`

- Summary: GET /api/admin/channels/types
- HTTP: `GET /api/admin/channels/types`
- Auth: required
- Body: none
- Flags: none
- Output: columns `name`, `id`, `i18n_key`; response media `application/json`

### `ai-gateway-cli master admin insights-list`

- Summary: GET /api/admin/insights
- HTTP: `GET /api/admin/insights`
- Auth: required
- Body: none
- Flags:
  - `--type` (query): type
  - `--id` (query): id
  - `--start` (query): start
  - `--end` (query): end
  - `--gran` (query): gran
- Output: response media `application/json`

### `ai-gateway-cli master admin invite-codes-by-id-delete`

- Summary: DELETE /api/admin/invite-codes/{id}
- HTTP: `DELETE /api/admin/invite-codes/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin invite-codes-get`

- Summary: GET /api/admin/invite-codes
- HTTP: `GET /api/admin/invite-codes`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--creator-id` (query): creator_id
- Output: list path `data`; columns `id`, `code`, `created_at`, `creator_id`, `expires_at`, `max_uses`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin limiter-bindings`

- Summary: POST /api/admin/limiter-bindings
- HTTP: `POST /api/admin/limiter-bindings`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin limiter-bindings-by-id-delete`

- Summary: DELETE /api/admin/limiter-bindings/{id}
- HTTP: `DELETE /api/admin/limiter-bindings/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin limiter-bindings-get`

- Summary: GET /api/admin/limiter-bindings
- HTTP: `GET /api/admin/limiter-bindings`
- Auth: required
- Body: none
- Flags:
  - `--limiter-id` (query, required): limiter_id
- Output: columns `id`, `created_at`, `enabled`, `limiter_id`, `target_id`, `target_type`; response media `application/json`

### `ai-gateway-cli master admin logs-list`

- Summary: GET /api/admin/logs
- HTTP: `GET /api/admin/logs`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--user-id` (query): user_id
  - `--token-id` (query): token_id
  - `--channel-id` (query): channel_id
  - `--model-name` (query): model_name
  - `--status` (query): status
  - `--private-channel-id` (query): private_channel_id
  - `--request-id` (query): request_id
- Output: list path `data`; columns `id`, `affinity_recorded`, `affinity_status`, `agent_id`, `agent_route_id`, `agent_route_path`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin logs-trace-list`

- Summary: GET /api/admin/logs/{request_id}/trace
- HTTP: `GET /api/admin/logs/{request_id}/trace`
- Auth: required
- Body: none
- Flags:
  - `--request-id` (path, required): request_id
- Output: columns `id`, `attempt_index`, `client_response_body`, `created_at`, `error_stage`, `inbound_body`; response media `application/json`

### `ai-gateway-cli master admin model-marketplace-detail-list`

- Summary: GET /api/admin/model-marketplace/detail
- HTTP: `GET /api/admin/model-marketplace/detail`
- Auth: required
- Body: none
- Flags:
  - `--token-id` (query): token_id
  - `--model` (query): model
  - `--window` (query): window
  - `--offer-ref` (query): offer_ref
- Output: response media `application/json`

### `ai-gateway-cli master admin model-marketplace-get`

- Summary: GET /api/admin/model-marketplace
- HTTP: `GET /api/admin/model-marketplace`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--token-id` (query): token_id
  - `--search` (query): search
  - `--provider` (query): provider
  - `--kind` (query): kind
- Output: response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin model-routings`

- Summary: POST /api/admin/model-routings
- HTTP: `POST /api/admin/model-routings`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin model-routings-by-id-delete`

- Summary: DELETE /api/admin/model-routings/{id}
- HTTP: `DELETE /api/admin/model-routings/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin model-routings-by-id-get`

- Summary: GET /api/admin/model-routings/{id}
- HTTP: `GET /api/admin/model-routings/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin model-routings-by-id-update`

- Summary: PUT /api/admin/model-routings/{id}
- HTTP: `PUT /api/admin/model-routings/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin model-routings-candidates-list`

- Summary: GET /api/admin/model-routings/candidates
- HTTP: `GET /api/admin/model-routings/candidates`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin model-routings-get`

- Summary: GET /api/admin/model-routings
- HTTP: `GET /api/admin/model-routings`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--scope` (query): scope
  - `--user-id` (query): user_id
  - `--token-id` (query): token_id
  - `--q` (query): q
- Output: list path `data`; columns `name`, `id`, `created_at`, `enabled`, `members`, `remark`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin model-routings-preview`

- Summary: POST /api/admin/model-routings/preview
- HTTP: `POST /api/admin/model-routings/preview`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin models-apply-pricing`

- Summary: POST /api/admin/models/apply-pricing
- HTTP: `POST /api/admin/models/apply-pricing`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin models-by-id-delete`

- Summary: DELETE /api/admin/models/{id}
- HTTP: `DELETE /api/admin/models/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin models-by-id-get`

- Summary: GET /api/admin/models/{id}
- HTTP: `GET /api/admin/models/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin models-by-id-update`

- Summary: PUT /api/admin/models/{id}
- HTTP: `PUT /api/admin/models/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin models-create`

- Summary: POST /api/admin/models
- HTTP: `POST /api/admin/models`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin models-fetch-pricing`

- Summary: POST /api/admin/models/fetch-pricing
- HTTP: `POST /api/admin/models/fetch-pricing`
- Auth: required
- Body: none
- Flags:
  - `--source` (query): source
- Output: response media `application/json`

### `ai-gateway-cli master admin models-list`

- Summary: GET /api/admin/models
- HTTP: `GET /api/admin/models`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--price-filter` (query): price_filter
- Output: list path `data`; columns `id`, `cache_read_price`, `cache_write_price`, `created_at`, `input_price`, `model_name`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin models-sync`

- Summary: POST /api/admin/models/sync
- HTTP: `POST /api/admin/models/sync`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin monitoring-insights-list`

- Summary: GET /api/admin/monitoring/insights
- HTTP: `GET /api/admin/monitoring/insights`
- Auth: required
- Body: none
- Flags:
  - `--start` (query): start
  - `--end` (query): end
  - `--gran` (query): gran
- Output: response media `application/json`

### `ai-gateway-cli master admin oauth-providers`

- Summary: POST /api/admin/oauth-providers
- HTTP: `POST /api/admin/oauth-providers`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin oauth-providers-by-id-delete`

- Summary: DELETE /api/admin/oauth-providers/{id}
- HTTP: `DELETE /api/admin/oauth-providers/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin oauth-providers-by-id-get`

- Summary: GET /api/admin/oauth-providers/{id}
- HTTP: `GET /api/admin/oauth-providers/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin oauth-providers-by-id-update`

- Summary: PUT /api/admin/oauth-providers/{id}
- HTTP: `PUT /api/admin/oauth-providers/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin oauth-providers-get`

- Summary: GET /api/admin/oauth-providers
- HTTP: `GET /api/admin/oauth-providers`
- Auth: required
- Body: none
- Flags: none
- Output: columns `name`, `id`, `authorization_endpoint`, `client_id`, `client_secret`, `created_at`; response media `application/json`

### `ai-gateway-cli master admin observability-breaker-board-get`

- Summary: GET /api/admin/observability/breaker-board
- HTTP: `GET /api/admin/observability/breaker-board`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin observability-delivery-board-get`

- Summary: GET /api/admin/observability/delivery-board
- HTTP: `GET /api/admin/observability/delivery-board`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin observability-delivery-op`

- Summary: POST /api/admin/observability/delivery-op
- HTTP: `POST /api/admin/observability/delivery-op`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin observability-limiter-usage-get`

- Summary: GET /api/admin/observability/limiter-usage
- HTTP: `GET /api/admin/observability/limiter-usage`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin observability-recent-health-get`

- Summary: GET /api/admin/observability/recent-health
- HTTP: `GET /api/admin/observability/recent-health`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin private-channels-baseurl-usage-list`

- Summary: GET /api/admin/private-channels/baseurl/usage
- HTTP: `GET /api/admin/private-channels/baseurl/usage`
- Auth: required
- Body: none
- Flags:
  - `--prefix` (query, required): prefix
- Output: response media `application/json`

### `ai-gateway-cli master admin private-channels-by-id-get`

- Summary: GET /api/admin/private-channels/{id}
- HTTP: `GET /api/admin/private-channels/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin private-channels-disable-create`

- Summary: POST /api/admin/private-channels/{id}/disable
- HTTP: `POST /api/admin/private-channels/{id}/disable`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin private-channels-get`

- Summary: GET /api/admin/private-channels
- HTTP: `GET /api/admin/private-channels`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--type` (query): type
  - `--status` (query): status
  - `--owner-id` (query): owner_id
- Output: list path `data`; columns `name`, `type`, `id`, `api_version`, `auto_ban`, `auto_ban_revision`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin rate-limiters`

- Summary: POST /api/admin/rate-limiters
- HTTP: `POST /api/admin/rate-limiters`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin rate-limiters-by-id-delete`

- Summary: DELETE /api/admin/rate-limiters/{id}
- HTTP: `DELETE /api/admin/rate-limiters/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin rate-limiters-by-id-update`

- Summary: PUT /api/admin/rate-limiters/{id}
- HTTP: `PUT /api/admin/rate-limiters/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin rate-limiters-get`

- Summary: GET /api/admin/rate-limiters
- HTTP: `GET /api/admin/rate-limiters`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
- Output: list path `data`; columns `name`, `id`, `action`, `capacity`, `channel_scope`, `created_at`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin scripts-by-id-delete`

- Summary: DELETE /api/admin/scripts/{id}
- HTTP: `DELETE /api/admin/scripts/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin scripts-by-id-get`

- Summary: GET /api/admin/scripts/{id}
- HTTP: `GET /api/admin/scripts/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin scripts-by-id-update`

- Summary: PUT /api/admin/scripts/{id}
- HTTP: `PUT /api/admin/scripts/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin scripts-create`

- Summary: POST /api/admin/scripts
- HTTP: `POST /api/admin/scripts`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin scripts-list`

- Summary: GET /api/admin/scripts
- HTTP: `GET /api/admin/scripts`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
- Output: list path `data`; columns `name`, `id`, `code`, `created_at`, `enabled`, `priority`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin stats-list`

- Summary: GET /api/admin/stats
- HTTP: `GET /api/admin/stats`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin system-cleanup-batch-create`

- Summary: POST /api/admin/system/cleanup/batch
- HTTP: `POST /api/admin/system/cleanup/batch`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin system-cleanup-preview-list`

- Summary: GET /api/admin/system/cleanup/preview
- HTTP: `GET /api/admin/system/cleanup/preview`
- Auth: required
- Body: none
- Flags:
  - `--database` (query): database
  - `--table` (query, required): table
  - `--cutoff-date` (query, required): cutoff_date
- Output: response media `application/json`

### `ai-gateway-cli master admin system-history-backfill-complete-create`

- Summary: POST /api/admin/system/history-backfill/complete
- HTTP: `POST /api/admin/system/history-backfill/complete`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin system-history-backfill-legacy-artifact-delete`

- Summary: DELETE /api/admin/system/history-backfill/legacy-artifact
- HTTP: `DELETE /api/admin/system/history-backfill/legacy-artifact`
- Auth: required
- Body: none
- Flags:
  - `--confirmation` (query): confirmation
- Output: response media `application/json`

### `ai-gateway-cli master admin system-history-backfill-retry-create`

- Summary: POST /api/admin/system/history-backfill/retry
- HTTP: `POST /api/admin/system/history-backfill/retry`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin system-history-backfill-skip-create`

- Summary: POST /api/admin/system/history-backfill/skip
- HTTP: `POST /api/admin/system/history-backfill/skip`
- Auth: required
- Body: none
- Flags:
  - `--confirm` (query): confirm
- Output: response media `application/json`

### `ai-gateway-cli master admin system-history-backfill-source-delete`

- Summary: DELETE /api/admin/system/history-backfill/source
- HTTP: `DELETE /api/admin/system/history-backfill/source`
- Auth: required
- Body: none
- Flags:
  - `--confirmation` (query): confirmation
- Output: response media `application/json`

### `ai-gateway-cli master admin system-log-queue-backlog-delete`

- Summary: DELETE /api/admin/system/log-queue/backlog
- HTTP: `DELETE /api/admin/system/log-queue/backlog`
- Auth: required
- Body: none
- Flags:
  - `--confirm` (query): confirm
- Output: response media `application/json`

### `ai-gateway-cli master admin system-log-queue-retry-create`

- Summary: POST /api/admin/system/log-queue/retry
- HTTP: `POST /api/admin/system/log-queue/retry`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin system-settings-list`

- Summary: GET /api/admin/system/settings
- HTTP: `GET /api/admin/system/settings`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin system-settings-update`

- Summary: PUT /api/admin/system/settings
- HTTP: `PUT /api/admin/system/settings`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin system-stats-list`

- Summary: GET /api/admin/system/stats
- HTTP: `GET /api/admin/system/stats`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin token-templates`

- Summary: POST /api/admin/token-templates
- HTTP: `POST /api/admin/token-templates`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin token-templates-by-id-delete`

- Summary: DELETE /api/admin/token-templates/{id}
- HTTP: `DELETE /api/admin/token-templates/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin token-templates-by-id-update`

- Summary: PUT /api/admin/token-templates/{id}
- HTTP: `PUT /api/admin/token-templates/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin token-templates-get`

- Summary: GET /api/admin/token-templates
- HTTP: `GET /api/admin/token-templates`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--status` (query): status
- Output: list path `data`; columns `name`, `id`, `byok_only`, `created_at`, `expiry_days`, `models`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin token-templates-sync`

- Summary: POST /api/admin/token-templates/{id}/sync
- HTTP: `POST /api/admin/token-templates/{id}/sync`
- Auth: required
- Body: optional; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin token-templates-sync-preview`

- Summary: POST /api/admin/token-templates/{id}/sync-preview
- HTTP: `POST /api/admin/token-templates/{id}/sync-preview`
- Auth: required
- Body: optional; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-by-id-delete`

- Summary: DELETE /api/admin/tokens/{id}
- HTTP: `DELETE /api/admin/tokens/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-by-id-get`

- Summary: GET /api/admin/tokens/{id}
- HTTP: `GET /api/admin/tokens/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-by-id-update`

- Summary: PUT /api/admin/tokens/{id}
- HTTP: `PUT /api/admin/tokens/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-create`

- Summary: POST /api/admin/tokens
- HTTP: `POST /api/admin/tokens`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-list`

- Summary: GET /api/admin/tokens
- HTTP: `GET /api/admin/tokens`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--user-id` (query): user_id
  - `--token-id` (query): token_id
  - `--status` (query): status
  - `--usable-only` (query): usable_only
  - `--api-role-mode` (query): api_role_mode
  - `--api-service-id` (query): api_service_id
  - `--api-route-id` (query): api_route_id
- Output: list path `data`; columns `name`, `id`, `api_role_mode`, `byok_only`, `created_at`, `expired_at`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin tokens-model-routings`

- Summary: POST /api/admin/tokens/{id}/model-routings
- HTTP: `POST /api/admin/tokens/{id}/model-routings`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-model-routings-by-id-delete`

- Summary: DELETE /api/admin/tokens/{id}/model-routings/{routing_id}
- HTTP: `DELETE /api/admin/tokens/{id}/model-routings/{routing_id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
  - `--routing-id` (path, required): routing_id
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-model-routings-by-id-get`

- Summary: GET /api/admin/tokens/{id}/model-routings/{routing_id}
- HTTP: `GET /api/admin/tokens/{id}/model-routings/{routing_id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
  - `--routing-id` (path, required): routing_id
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-model-routings-by-id-update`

- Summary: PUT /api/admin/tokens/{id}/model-routings/{routing_id}
- HTTP: `PUT /api/admin/tokens/{id}/model-routings/{routing_id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
  - `--routing-id` (path, required): routing_id
- Output: response media `application/json`

### `ai-gateway-cli master admin tokens-model-routings-get`

- Summary: GET /api/admin/tokens/{id}/model-routings
- HTTP: `GET /api/admin/tokens/{id}/model-routings`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--q` (query): q
- Output: list path `data`; columns `name`, `id`, `created_at`, `enabled`, `members`, `remark`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin tokens-model-routings-preview`

- Summary: POST /api/admin/tokens/{id}/model-routings/preview
- HTTP: `POST /api/admin/tokens/{id}/model-routings/preview`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin user-groups`

- Summary: POST /api/admin/user-groups
- HTTP: `POST /api/admin/user-groups`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin user-groups-by-id-delete`

- Summary: DELETE /api/admin/user-groups/{id}
- HTTP: `DELETE /api/admin/user-groups/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin user-groups-by-id-get`

- Summary: GET /api/admin/user-groups/{id}
- HTTP: `GET /api/admin/user-groups/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin user-groups-by-id-update`

- Summary: PUT /api/admin/user-groups/{id}
- HTTP: `PUT /api/admin/user-groups/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin user-groups-get`

- Summary: GET /api/admin/user-groups
- HTTP: `GET /api/admin/user-groups`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--status` (query): status
- Output: list path `data`; columns `name`, `id`, `byok_enabled`, `byok_max_channels`, `created_at`, `description`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin users-by-id-delete`

- Summary: DELETE /api/admin/users/{id}
- HTTP: `DELETE /api/admin/users/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin users-by-id-get`

- Summary: GET /api/admin/users/{id}
- HTTP: `GET /api/admin/users/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin users-by-id-update`

- Summary: PUT /api/admin/users/{id}
- HTTP: `PUT /api/admin/users/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master admin users-create`

- Summary: POST /api/admin/users
- HTTP: `POST /api/admin/users`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master admin users-list`

- Summary: GET /api/admin/users
- HTTP: `GET /api/admin/users`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--role` (query): role
  - `--group-id` (query): group_id
- Output: list path `data`; columns `id`, `avatar_url`, `created_at`, `display_name`, `email`, `group_id`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master admin users-quota-update`

- Summary: PUT /api/admin/users/{id}/quota
- HTTP: `PUT /api/admin/users/{id}/quota`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

## agents

### `ai-gateway-cli master agents enroll`

- Summary: POST /api/agents/enroll
- HTTP: `POST /api/agents/enroll`
- Auth: public
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## api_catalog

### `ai-gateway-cli master api_catalog api-catalog-effective-list`

- Summary: GET /api/api-catalog/effective
- HTTP: `GET /api/api-catalog/effective`
- Auth: required
- Body: none
- Flags:
  - `--service-id` (query, required): service_id
  - `--token-id` (query): token_id
- Output: response media `application/json`

### `ai-gateway-cli master api_catalog api-catalog-openapi-list`

- Summary: GET /api/api-catalog/openapi
- HTTP: `GET /api/api-catalog/openapi`
- Auth: required
- Body: none
- Flags:
  - `--service-id` (query, required): service_id
  - `--token-id` (query): token_id
- Output: response media `application/json`

### `ai-gateway-cli master api_catalog api-catalog-routes-list`

- Summary: GET /api/api-catalog/routes
- HTTP: `GET /api/api-catalog/routes`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--service-id` (query, required): service_id
  - `--search` (query): search
  - `--token-id` (query): token_id
- Output: list path `data`; columns `id`, `allowed_methods`, `api_service_id`, `protocols`, `slug`, `websocket_subprotocols`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master api_catalog api-catalog-services-detail-list`

- Summary: GET /api/api-catalog/services/detail
- HTTP: `GET /api/api-catalog/services/detail`
- Auth: required
- Body: none
- Flags:
  - `--id` (query, required): id
  - `--token-id` (query): token_id
- Output: response media `application/json`

### `ai-gateway-cli master api_catalog api-catalog-services-list`

- Summary: GET /api/api-catalog/services
- HTTP: `GET /api/api-catalog/services`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--token-id` (query): token_id
- Output: list path `data`; columns `name`, `id`, `description`, `slug`; response media `application/json`; pagination `offset`

## api_request_logs

### `ai-gateway-cli master api_request_logs api-request-logs-by-id-get`

- Summary: GET /api/api-request-logs/{request_id}
- HTTP: `GET /api/api-request-logs/{request_id}`
- Auth: required
- Body: none
- Flags:
  - `--request-id` (path, required): request_id
- Output: response media `application/json`

### `ai-gateway-cli master api_request_logs api-request-logs-get`

- Summary: GET /api/api-request-logs
- HTTP: `GET /api/api-request-logs`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--token-id` (query): token_id
  - `--status-code` (query): status_code
  - `--request-id` (query): request_id
- Output: list path `data`; columns `id`, `api_route_id`, `api_route_name`, `api_service_id`, `api_service_name`, `created_at`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master api_request_logs api-request-logs-trace-list`

- Summary: GET /api/api-request-logs/{request_id}/trace
- HTTP: `GET /api/api-request-logs/{request_id}/trace`
- Auth: required
- Body: none
- Flags:
  - `--request-id` (path, required): request_id
- Output: response media `application/json`

## api_request_traces

### `ai-gateway-cli master api_request_traces api-request-traces-get`

- Summary: GET /api/api-request-traces
- HTTP: `GET /api/api-request-traces`
- Auth: required
- Body: none
- Flags:
  - `--request-id` (query, required): request_id
- Output: response media `application/json`

## auth

### `ai-gateway-cli master auth login`

- Summary: POST /api/login
- HTTP: `POST /api/login`
- Auth: public
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master auth register`

- Summary: POST /api/register
- HTTP: `POST /api/register`
- Auth: public
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## billing

### `ai-gateway-cli master billing insights-list`

- Summary: GET /api/billing/insights
- HTTP: `GET /api/billing/insights`
- Auth: required
- Body: none
- Flags:
  - `--start` (query): start
  - `--end` (query): end
  - `--gran` (query): gran
  - `--stack` (query): stack
  - `--model` (query): model
  - `--user-id` (query): user_id
  - `--token-id` (query): token_id
  - `--top-n` (query): top_n
- Output: response media `application/json`

### `ai-gateway-cli master billing overview-list`

- Summary: GET /api/billing/overview
- HTTP: `GET /api/billing/overview`
- Auth: required
- Body: none
- Flags:
  - `--start-date` (query): start_date
  - `--end-date` (query): end_date
  - `--user-id` (query): user_id
- Output: response media `application/json`

### `ai-gateway-cli master billing tokens-daily-list`

- Summary: GET /api/billing/tokens/{token_id}/daily
- HTTP: `GET /api/billing/tokens/{token_id}/daily`
- Auth: required
- Body: none
- Flags:
  - `--token-id` (path, required): token_id
  - `--start-date` (query): start_date
  - `--end-date` (query): end_date
  - `--user-id` (query): user_id
- Output: response media `application/json`

### `ai-gateway-cli master billing tokens-list`

- Summary: GET /api/billing/tokens
- HTTP: `GET /api/billing/tokens`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--start-date` (query): start_date
  - `--end-date` (query): end_date
  - `--token-id` (query): token_id
  - `--user-id` (query): user_id
  - `--search` (query): search
  - `--min-tokens` (query): min_tokens
- Output: list path `data`; columns `cache_read_tokens`, `cache_write_tokens`, `completion_tokens`, `failed_count`, `input_cost`, `last_used_at`; response media `application/json`; pagination `offset`

## capabilities

### `ai-gateway-cli master capabilities list`

- Summary: GET /api/capabilities
- HTTP: `GET /api/capabilities`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

## invite_codes

### `ai-gateway-cli master invite_codes invite-codes`

- Summary: POST /api/invite-codes
- HTTP: `POST /api/invite-codes`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master invite_codes invite-codes-by-id-delete`

- Summary: DELETE /api/invite-codes/{id}
- HTTP: `DELETE /api/invite-codes/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master invite_codes invite-codes-get`

- Summary: GET /api/invite-codes
- HTTP: `GET /api/invite-codes`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--creator-id` (query): creator_id
- Output: list path `data`; columns `id`, `code`, `created_at`, `creator_id`, `expires_at`, `max_uses`; response media `application/json`; pagination `offset`

## logs

### `ai-gateway-cli master logs insights-list`

- Summary: GET /api/logs/insights
- HTTP: `GET /api/logs/insights`
- Auth: required
- Body: none
- Flags:
  - `--start` (query): start
  - `--end` (query): end
- Output: response media `application/json`

### `ai-gateway-cli master logs list`

- Summary: GET /api/logs
- HTTP: `GET /api/logs`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--user-id` (query): user_id
  - `--token-id` (query): token_id
  - `--channel-id` (query): channel_id
  - `--model-name` (query): model_name
  - `--status` (query): status
  - `--private-channel-id` (query): private_channel_id
  - `--request-id` (query): request_id
- Output: list path `data`; columns `id`, `affinity_recorded`, `affinity_status`, `agent_id`, `agent_route_id`, `agent_route_path`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master logs trace-list`

- Summary: GET /api/logs/{request_id}/trace
- HTTP: `GET /api/logs/{request_id}/trace`
- Auth: required
- Body: none
- Flags:
  - `--request-id` (path, required): request_id
- Output: columns `id`, `attempt_index`, `client_response_body`, `created_at`, `error_stage`, `inbound_body`; response media `application/json`

## model_marketplace

### `ai-gateway-cli master model_marketplace model-marketplace-detail-list`

- Summary: GET /api/model-marketplace/detail
- HTTP: `GET /api/model-marketplace/detail`
- Auth: required
- Body: none
- Flags:
  - `--token-id` (query): token_id
  - `--model` (query): model
  - `--window` (query): window
  - `--offer-ref` (query): offer_ref
- Output: response media `application/json`

### `ai-gateway-cli master model_marketplace model-marketplace-get`

- Summary: GET /api/model-marketplace
- HTTP: `GET /api/model-marketplace`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--token-id` (query): token_id
  - `--search` (query): search
  - `--provider` (query): provider
  - `--kind` (query): kind
- Output: response media `application/json`; pagination `offset`

## model_routings

### `ai-gateway-cli master model_routings model-routings`

- Summary: POST /api/model-routings
- HTTP: `POST /api/model-routings`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master model_routings model-routings-by-id-delete`

- Summary: DELETE /api/model-routings/{id}
- HTTP: `DELETE /api/model-routings/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master model_routings model-routings-by-id-get`

- Summary: GET /api/model-routings/{id}
- HTTP: `GET /api/model-routings/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master model_routings model-routings-by-id-update`

- Summary: PUT /api/model-routings/{id}
- HTTP: `PUT /api/model-routings/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master model_routings model-routings-get`

- Summary: GET /api/model-routings
- HTTP: `GET /api/model-routings`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--scope` (query): scope
  - `--user-id` (query): user_id
  - `--token-id` (query): token_id
  - `--q` (query): q
- Output: list path `data`; columns `name`, `id`, `created_at`, `enabled`, `members`, `remark`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master model_routings model-routings-global-routing-names-get`

- Summary: GET /api/model-routings/global-routing-names
- HTTP: `GET /api/model-routings/global-routing-names`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master model_routings model-routings-preview`

- Summary: POST /api/model-routings/preview
- HTTP: `POST /api/model-routings/preview`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## oauth

### `ai-gateway-cli master oauth bind-create`

- Summary: POST /api/oauth/bind
- HTTP: `POST /api/oauth/bind`
- Auth: public
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master oauth identities-by-id-delete`

- Summary: DELETE /api/oauth/identities/{id}
- HTTP: `DELETE /api/oauth/identities/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master oauth identities-list`

- Summary: GET /api/oauth/identities
- HTTP: `GET /api/oauth/identities`
- Auth: required
- Body: none
- Flags: none
- Output: columns `id`, `created_at`, `display_name`, `email`, `provider_display_name`, `provider_id`; response media `application/json`

### `ai-gateway-cli master oauth link-ticket`

- Summary: POST /api/oauth/link-ticket
- HTTP: `POST /api/oauth/link-ticket`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master oauth providers-list`

- Summary: GET /api/oauth/providers
- HTTP: `GET /api/oauth/providers`
- Auth: public
- Body: none
- Flags: none
- Output: columns `name`, `display_name`, `icon_url`; response media `application/json`

### `ai-gateway-cli master oauth register`

- Summary: POST /api/oauth/register
- HTTP: `POST /api/oauth/register`
- Auth: public
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## private_channels

### `ai-gateway-cli master private_channels private-channels`

- Summary: POST /api/private-channels
- HTTP: `POST /api/private-channels`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-available-models-get`

- Summary: GET /api/private-channels/available-models
- HTTP: `GET /api/private-channels/available-models`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-billing-by-channel-get`

- Summary: GET /api/private-channels/billing/by-channel
- HTTP: `GET /api/private-channels/billing/by-channel`
- Auth: required
- Body: none
- Flags:
  - `--from` (query): from
  - `--to` (query): to
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-billing-by-model-get`

- Summary: GET /api/private-channels/billing/by-model
- HTTP: `GET /api/private-channels/billing/by-model`
- Auth: required
- Body: none
- Flags:
  - `--from` (query): from
  - `--to` (query): to
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-billing-overview-list`

- Summary: GET /api/private-channels/billing/overview
- HTTP: `GET /api/private-channels/billing/overview`
- Auth: required
- Body: none
- Flags:
  - `--from` (query): from
  - `--to` (query): to
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-by-id-delete`

- Summary: DELETE /api/private-channels/{id}
- HTTP: `DELETE /api/private-channels/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-by-id-get`

- Summary: GET /api/private-channels/{id}
- HTTP: `GET /api/private-channels/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-by-id-update`

- Summary: PUT /api/private-channels/{id}
- HTTP: `PUT /api/private-channels/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-export`

- Summary: POST /api/private-channels/export
- HTTP: `POST /api/private-channels/export`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-get`

- Summary: GET /api/private-channels
- HTTP: `GET /api/private-channels`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--type` (query): type
  - `--status` (query): status
- Output: list path `data`; columns `name`, `type`, `id`, `api_version`, `auto_ban`, `auto_ban_revision`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master private_channels private-channels-import`

- Summary: POST /api/private-channels/import
- HTTP: `POST /api/private-channels/import`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--dry-run` (query): dry_run
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-key-update`

- Summary: PUT /api/private-channels/{id}/key
- HTTP: `PUT /api/private-channels/{id}/key`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-test`

- Summary: POST /api/private-channels/{id}/test
- HTTP: `POST /api/private-channels/{id}/test`
- Auth: required
- Body: optional; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master private_channels private-channels-types-list`

- Summary: GET /api/private-channels/types
- HTTP: `GET /api/private-channels/types`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

## profile

### `ai-gateway-cli master profile list`

- Summary: GET /api/profile
- HTTP: `GET /api/profile`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master profile password-update`

- Summary: PUT /api/profile/password
- HTTP: `PUT /api/profile/password`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master profile update`

- Summary: PUT /api/profile
- HTTP: `PUT /api/profile`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

## public

### `ai-gateway-cli master public ping-get`

- Summary: GET /ping
- HTTP: `GET /ping`
- Auth: public
- Body: none
- Flags: none
- Output: response media `application/json`

## stats

### `ai-gateway-cli master stats byok-overview-get`

- Summary: GET /api/stats/byok-overview
- HTTP: `GET /api/stats/byok-overview`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master stats channel-model-breakdown-get`

- Summary: GET /api/stats/channel-model-breakdown
- HTTP: `GET /api/stats/channel-model-breakdown`
- Auth: required
- Body: none
- Flags:
  - `--channel-id` (query): channel_id
  - `--start` (query): start
  - `--end` (query): end
  - `--gran` (query): gran
- Output: response media `application/json`

### `ai-gateway-cli master stats dashboard-list`

- Summary: GET /api/stats/dashboard
- HTTP: `GET /api/stats/dashboard`
- Auth: required
- Body: none
- Flags:
  - `--start` (query): start
  - `--end` (query): end
  - `--gran` (query): gran
  - `--model` (query): model
  - `--user-id` (query): user_id
  - `--top-n` (query): top_n
- Output: response media `application/json`

### `ai-gateway-cli master stats market-share-get`

- Summary: GET /api/stats/market-share
- HTTP: `GET /api/stats/market-share`
- Auth: required
- Body: none
- Flags:
  - `--dim` (query): dim
  - `--start` (query): start
  - `--end` (query): end
  - `--gran` (query): gran
  - `--model` (query): model
  - `--top-n` (query): top_n
- Output: response media `application/json`

### `ai-gateway-cli master stats metric-trend-get`

- Summary: GET /api/stats/metric-trend
- HTTP: `GET /api/stats/metric-trend`
- Auth: required
- Body: none
- Flags:
  - `--metric` (query): metric
  - `--stat` (query): stat
  - `--dim` (query): dim
  - `--start` (query): start
  - `--end` (query): end
  - `--gran` (query): gran
  - `--model` (query): model
  - `--top-n` (query): top_n
  - `--user-id` (query): user_id
- Output: response media `application/json`

### `ai-gateway-cli master stats model-distribution-get`

- Summary: GET /api/stats/model-distribution
- HTTP: `GET /api/stats/model-distribution`
- Auth: required
- Body: none
- Flags:
  - `--start` (query): start
  - `--end` (query): end
  - `--gran` (query): gran
  - `--model` (query): model
  - `--user-id` (query): user_id
  - `--top-n` (query): top_n
- Output: response media `application/json`

### `ai-gateway-cli master stats overview-list`

- Summary: GET /api/stats/overview
- HTTP: `GET /api/stats/overview`
- Auth: required
- Body: none
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master stats trend-list`

- Summary: GET /api/stats/trend
- HTTP: `GET /api/stats/trend`
- Auth: required
- Body: none
- Flags:
  - `--days` (query): days
- Output: response media `application/json`

## system

### `ai-gateway-cli master system public-config-get`

- Summary: GET /api/system/public-config
- HTTP: `GET /api/system/public-config`
- Auth: public
- Body: none
- Flags: none
- Output: response media `application/json`

## token_templates

### `ai-gateway-cli master token_templates token-templates-get`

- Summary: GET /api/token-templates
- HTTP: `GET /api/token-templates`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--status` (query): status
- Output: list path `data`; columns `name`, `id`, `byok_only`, `created_at`, `expiry_days`, `models`; response media `application/json`; pagination `offset`

## tokens

### `ai-gateway-cli master tokens by-id-delete`

- Summary: DELETE /api/tokens/{id}
- HTTP: `DELETE /api/tokens/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master tokens by-id-get`

- Summary: GET /api/tokens/{id}
- HTTP: `GET /api/tokens/{id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master tokens by-id-update`

- Summary: PUT /api/tokens/{id}
- HTTP: `PUT /api/tokens/{id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master tokens create`

- Summary: POST /api/tokens
- HTTP: `POST /api/tokens`
- Auth: required
- Body: required; media type `application/json`
- Flags: none
- Output: response media `application/json`

### `ai-gateway-cli master tokens list`

- Summary: GET /api/tokens
- HTTP: `GET /api/tokens`
- Auth: required
- Body: none
- Flags:
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--search` (query): search
  - `--user-id` (query): user_id
  - `--token-id` (query): token_id
  - `--status` (query): status
  - `--usable-only` (query): usable_only
  - `--api-role-mode` (query): api_role_mode
  - `--api-service-id` (query): api_service_id
  - `--api-route-id` (query): api_route_id
- Output: list path `data`; columns `name`, `id`, `api_role_mode`, `byok_only`, `created_at`, `expired_at`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master tokens model-routings`

- Summary: POST /api/tokens/{id}/model-routings
- HTTP: `POST /api/tokens/{id}/model-routings`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`

### `ai-gateway-cli master tokens model-routings-by-id-delete`

- Summary: DELETE /api/tokens/{id}/model-routings/{routing_id}
- HTTP: `DELETE /api/tokens/{id}/model-routings/{routing_id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
  - `--routing-id` (path, required): routing_id
- Output: response media `application/json`

### `ai-gateway-cli master tokens model-routings-by-id-get`

- Summary: GET /api/tokens/{id}/model-routings/{routing_id}
- HTTP: `GET /api/tokens/{id}/model-routings/{routing_id}`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
  - `--routing-id` (path, required): routing_id
- Output: response media `application/json`

### `ai-gateway-cli master tokens model-routings-by-id-update`

- Summary: PUT /api/tokens/{id}/model-routings/{routing_id}
- HTTP: `PUT /api/tokens/{id}/model-routings/{routing_id}`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
  - `--routing-id` (path, required): routing_id
- Output: response media `application/json`

### `ai-gateway-cli master tokens model-routings-get`

- Summary: GET /api/tokens/{id}/model-routings
- HTTP: `GET /api/tokens/{id}/model-routings`
- Auth: required
- Body: none
- Flags:
  - `--id` (path, required): id
  - `--page` (query): page
  - `--page-size` (query): page_size
  - `--q` (query): q
- Output: list path `data`; columns `name`, `id`, `created_at`, `enabled`, `members`, `remark`; response media `application/json`; pagination `offset`

### `ai-gateway-cli master tokens model-routings-preview`

- Summary: POST /api/tokens/{id}/model-routings/preview
- HTTP: `POST /api/tokens/{id}/model-routings/preview`
- Auth: required
- Body: required; media type `application/json`
- Flags:
  - `--id` (path, required): id
- Output: response media `application/json`
