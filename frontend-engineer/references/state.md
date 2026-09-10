# State and Data Flow

## Classify Before Choosing a Library

| State kind | Examples | Preferred owner |
| --- | --- | --- |
| URL / navigation | query, filter, tab, pagination, resource id | Router / URL |
| Local UI | open, hover, draft selection | Nearest component |
| Form | values, touched, validation, submission | Form boundary |
| Shared client | cross-feature session UI, collaborative draft | Context/store when proven |
| Server state | records, cache, freshness, mutations | Framework/query cache |
| Persistent preference | theme, density, locale | Server or storage with hydration plan |

## Rules

- 保存最小且完整的事实；其余从事实派生。
- 每条数据只有一个权威 owner；不要在 URL、store、props 与本地 state 中重复。
- state 放到需要它的最近共同所有者；只有清晰的跨层需求才提升。
- 全局 store 是架构选择，不是默认收纳箱。
- 复杂状态使用明确 action/transition 或 state machine，避免多个 boolean 组合出不可能状态。
- SSR 中禁止跨请求共享用户可变状态；持久化必须处理版本、失效、隐私和 hydration。

## Async State Model

不要只用 `isLoading`。至少考虑：idle、loading、success、empty、refreshing、partial、stale、validation error、unauthorized、server error、offline、cancelled、retrying。

为 mutation 定义：optimistic update 是否合适、冲突如何处理、失败如何 rollback、重复提交是否幂等、成功后哪些缓存失效。

## Data Flow Contract

对共享状态记录：

- source of truth；
- readers / writers；
- allowed transitions；
- persistence 与 lifecycle；
- server/client boundary；
- stale 与 invalidation；
- error/recovery；
- test strategy。

## Review Smells

- Effect/watch 在两个 state 之间同步；
- 一组 `isX` boolean 可以同时互相矛盾；
- store 包含一次性组件样式或临时 hover；
- 网络响应未经校验直接成为全局真相；
- URL 可分享状态只存在内存；
- logout 后敏感 state 未清理。

## Sources

- [React: Managing State](https://react.dev/learn/managing-state)
- [Vue: State Management](https://vuejs.org/guide/scaling-up/state-management.html)
