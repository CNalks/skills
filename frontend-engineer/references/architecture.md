# Frontend Architecture

## 1. Inspect Before Changing

先读取仓库的 `AGENTS.md`/贡献规则、package manager、framework 与版本、目录、build/test 命令、Design System、API 客户端、lint/type 配置和 CI。沿用有效约定；不要仅为个人偏好迁移框架、状态库或目录。

记录：

- 目标路由、用户流程和验收条件；
- Product Designer 的 Wireframe、tokens、组件族与不可改决策；
- 服务端/客户端约束、浏览器范围、国际化与部署目标；
- 现有可复用组件以及缺口。

## 2. Organize by Route and Feature

优先让页面、功能组件、数据访问与测试就近放置。只有被多个独立功能稳定复用、语义一致且依赖方向清楚的内容才进入 shared。

```text
src/
  app-or-routes/
    feature-a/
      page
      components/
      data/
      tests/
  features/
  components/
    ui/          # primitives and design-system components
  lib/           # framework-agnostic utilities and clients
```

这是决策示意，不是强制目录。已有仓库约定优先。

## 3. Component Layers

依次推导，而非一次抽象全部：

1. **Primitive**：Button、Input、Dialog 等语义与交互基础；
2. **Composed component**：SearchField、DateRange、DataTable 等可复用组合；
3. **Feature component**：理解业务对象与用例；
4. **Page / route**：组合区域、数据和导航，不承载所有细节。

组件按数据模型和页面结构拆分。优先 `props/events/children/slots` 组合；出现真实重复后再抽象。不要用一个巨型“万能组件”或深层配置对象隐藏业务差异。

## 4. Dependency Rules

- 页面可依赖 feature、composed 和 primitive；反向依赖禁止。
- UI primitive 不导入业务模块、路由或具体 API。
- 数据层不依赖可视组件。
- 跨 feature 共享必须有稳定接口；禁止循环依赖。
- 浏览器专用代码留在明确 client 边界，服务端代码不进入客户端 bundle。

## 5. Rendering Decision

对每条路由与区域分别决定：

- 稳定公共内容：静态生成或预渲染；
- 请求相关、权限或个性化数据：服务端渲染/Server Component；
- 事件、本地 state、生命周期或浏览器 API：最小 Client Component；
- 慢数据：并行获取、streaming、Suspense/loading boundary；
- 搜索引擎不重要的高度交互工具：仍评估首屏与 bundle 后再决定纯客户端。

目标不是追逐一种渲染模式，而是缩小客户端 JavaScript 与 hydration 边界，同时保持正确缓存和用户反馈。

## 6. Data and API Boundaries

- 明确数据 owner、获取位置、缓存、失效、权限和运行时校验；
- 服务端组件能安全直连数据源时，不要绕行自己的公开 API；
- 公共 Route Handler/BFF 负责真正的客户端、外部消费者或安全边界；
- UI 不直接解释供应商错误；在边界映射为稳定的领域错误与恢复动作；
- 请求支持取消、超时、幂等与敏感信息保护。

## 7. Responsive and Progressive Enhancement

按 Product Designer 的优先级重排，不自行改变 IA。基础内容和关键动作在最小能力下可用，再增强交互；不要依赖 hover、JavaScript 动画或宽屏完成核心任务。

## Architecture Review

- [ ] 目录和依赖方向与现有项目一致。
- [ ] 组件边界对应数据与职责，不是视觉碎片。
- [ ] server/client 和缓存边界有理由。
- [ ] 没有重复真相源、跨请求可变 singleton 或泄漏 secret。
- [ ] loading、empty、partial、stale、error、offline、permission 有所有者。
- [ ] 可测试性、可访问性与性能不是事后补丁。

## Sources

- [React: Thinking in React](https://react.dev/learn/thinking-in-react)
- [Next.js: Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
- [Next.js: Backend for Frontend](https://nextjs.org/docs/app/guides/backend-for-frontend)
- [web.dev: Rendering on the Web](https://web.dev/articles/rendering-on-the-web)
- [Vue: Application Architecture](https://vuejs.org/guide/scaling-up/ssr.html)
