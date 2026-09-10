# Frontend API Contract

## Operation

- Name / owner：
- Method / path / version：
- Environment / base URL：
- Caller / rendering boundary：server / client / both
- User task：

## Request

| Location | Field | Type / schema | Required | Validation / encoding |
| --- | --- | --- | --- | --- |
| path / query / header / body |  |  |  |  |

- Authentication / authorization：
- CSRF / CORS：
- Idempotency：
- Sensitive data：

## Response

| Status | Schema / meaning | UI mapping | Retry / recovery |
| --- | --- | --- | --- |
| 2xx |  |  |  |
| 4xx |  |  |  |
| 5xx |  |  |  |

- Pagination / cursor：
- Partial data / warnings：
- Runtime validation：
- Stable domain error mapping：

## Request Lifecycle

- Timeout：
- `AbortSignal` / cancellation：
- Retry policy and backoff：
- Duplicate submission protection：
- Rate limit behavior：
- Offline behavior：

## Cache and State

- Cache owner / key：
- Freshness / revalidation：
- Invalidation triggers：
- Optimistic update：
- Rollback / conflict：
- URL / local / shared state interaction：

## UI State Matrix

| State | User message | Available action | Focus / announcement |
| --- | --- | --- | --- |
| Loading / refreshing |  |  |  |
| Empty / no result |  |  |  |
| Partial / stale |  |  |  |
| Validation error |  |  |  |
| Unauthorized / forbidden |  |  |  |
| Server error |  |  |  |
| Offline / timeout |  |  |  |
| Success |  |  |  |

## Security and Observability

- Secret handling（不得进入客户端 bundle）：
- PII / logging redaction：
- Request / trace ID：
- Metrics and failure signals：
- Audit requirements：

## Tests

- Contract/schema：
- Mock / fixture：
- Integration：
- Timeout/cancel/retry：
- Authorization/error：
- Cache/invalidation/rollback：

## Acceptance Checklist

- [ ] 类型与运行时校验同时存在于不可信边界。
- [ ] 权限、secret、PII 与错误信息不泄漏。
- [ ] loading/empty/partial/error/offline/retry 均映射到 UI。
- [ ] timeout、cancel、幂等、缓存和失效行为明确。
- [ ] 测试使用真实契约，不把被测逻辑全部 mock。
