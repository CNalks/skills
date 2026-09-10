# Vue Rules

## Component and Composition Model

- 使用 Single-File Components 与 Composition API 表达复杂功能；简单组件沿用项目既有风格。
- props 向下、events 向上；不要直接修改 props。
- slots 用于结构组合，composables 用于复用有状态逻辑，Pinia/store 用于经过证明的跨功能共享状态。
- `computed` 表达派生值；`watch`/`watchEffect` 只同步副作用，并处理 cleanup、竞态与 flush 时机。
- composable 以 `use` 命名，接受 ref/getter 时明确响应式契约，不隐藏全局可变状态。

## State Ownership

局部交互保留在组件；URL 查询属于路由；表单属于表单边界；远端数据属于请求/缓存层；跨页面业务状态才进入 store。避免同一数据同时存在 props、store 和本地副本。

## SSR and Nuxt

- 服务端状态按请求隔离，禁止共享用户相关 module singleton；
- 浏览器 API 放在客户端生命周期或明确边界；
- 检查 hydration 差异、持久化恢复和时区/随机值；
- 服务端优先获取敏感或首屏数据，客户端只接收所需可序列化结果；
- 对 loading、error、not-found 和权限使用框架原生边界。

## Performance

- props 尽量稳定，避免无意义触发子树更新；
- 大列表使用分页、虚拟化或稳定结构；
- 路由与重型功能异步加载；
- 对大型不可变数据评估 shallow reactivity；
- 优化前使用 production profile，不凭感觉添加缓存。

## Testing

测试用户可见输入、输出和事件，不依赖内部 ref 或实现细节。composable 的纯逻辑可单测；依赖 lifecycle/provide-inject 的逻辑在宿主组件中测试；关键流程使用浏览器级测试。

## Sources

- [Vue: Composables](https://vuejs.org/guide/reusability/composables.html)
- [Vue: State Management](https://vuejs.org/guide/scaling-up/state-management.html)
- [Vue: SSR](https://vuejs.org/guide/scaling-up/ssr.html)
- [Vue: Performance](https://vuejs.org/guide/best-practices/performance.html)
- [Vue: Testing](https://vuejs.org/guide/scaling-up/testing.html)
