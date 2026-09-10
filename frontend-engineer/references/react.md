# React and Next.js Rules

## Derive Components from Data and Tasks

1. 将设计稿中的对象映射到数据模型；
2. 按单一职责画组件树；
3. 先用静态数据完成组合与语义；
4. 找出最小、完整、不可派生的 state；
5. 把 state 放到需要它的最近共同所有者；
6. 再接入服务端数据、交互和状态边界。

## Component Rules

- Render 保持纯；相同 props/state/context 产生相同输出。
- 派生值在 render 或 selector 中计算，不复制到 state。
- 通过 props、children 和组合共享 UI；Context 用于真正的跨层稳定依赖。
- 列表 key 使用稳定身份，不用会变化的 index 或随机值。
- 明确 controlled/uncontrolled 契约，禁止生命周期中途切换。
- Custom Hook 复用有状态逻辑，不代表多个调用共享同一份 state。
- 只有 profiling 证明时才添加 memoization；不要用 `useMemo`/`useCallback` 修饰所有代码。

## Effects

Effect 只同步 React 外部系统，例如浏览器 API、订阅或第三方 widget。若值可从 props/state 推导、事件可直接处理、数据可由框架获取，就不要添加 Effect。

每个 Effect 明确依赖、setup、cleanup、竞争与取消。不要用 Effect 链驱动业务流程、同步重复 state 或绕过 lint。

## Next.js App Router

- `page`、`layout` 默认使用 Server Component；
- 仅在事件、本地 state、Effect 或浏览器 API 的最小边界添加 `use client`；
- 服务端获取和校验数据，避免把 secret 或大型依赖送到客户端；
- 并行无依赖请求，避免 request waterfall；
- 用 `loading`/Suspense、error boundary、`not-found` 与权限状态表达结果；
- 明确静态/动态渲染、缓存与 revalidation，不依赖模糊默认值；
- 交互 island 接收可序列化的最小数据，不把整个页面客户端化。

## Forms and Mutations

区分客户端即时验证与服务端权威验证。提交期间防止重复动作；保留用户输入；错误映射到字段或表单级；成功后明确缓存失效、导航和焦点/状态通知。

## Review

- [ ] 无重复/矛盾 state。
- [ ] Effect 均同步外部系统并有 cleanup。
- [ ] Client boundary 尽可能小且有理由。
- [ ] 异步、错误、空与权限状态完整。
- [ ] 语义、键盘、焦点与状态通知可测试。

## Sources

- [React: Thinking in React](https://react.dev/learn/thinking-in-react)
- [React: Sharing State Between Components](https://react.dev/learn/sharing-state-between-components)
- [React: You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect)
- [React: Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)
- [Next.js: Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Next.js: Fetching Data](https://nextjs.org/docs/app/getting-started/fetching-data)
