# Frontend Testing

## Test the Contract

测试用户可观察行为、组件契约、数据边界和风险，不测试内部实现细节。优先通过 role、name、label、text 等语义查询元素；避免脆弱 CSS selector、DOM 层级和任意 timeout。

## Layers

- **Static**：format、lint、typecheck、依赖/安全规则；
- **Unit**：纯函数、schema、selector、状态转换；
- **Component**：props/events/slots、交互状态、键盘、a11y；
- **Integration**：路由、API client、缓存、表单和 feature 协作；
- **E2E**：少量高价值用户流程和跨系统边界；
- **Visual**：Design System、响应式和高风险视觉回归；
- **Performance**：预算、关键路由和真实交互。

测试数量按风险分配，不追求固定金字塔比例。

## Stable Tests

- 每个测试独立创建数据，不依赖执行顺序；
- 使用真实用户可见 locator 和 web-first assertion；
- 等待状态条件，不使用固定 sleep；
- 外部依赖在明确边界 mock，避免把被测核心一起 mock 掉；
- 时间、随机、网络与动画有可控策略；
- 失败输出包含请求、截图、trace 或可定位证据。

## Required Scenarios

为关键功能覆盖 happy path、validation、empty、permission、server error、offline/timeout、retry/cancel、重复提交、刷新/返回和键盘路径。视觉组件覆盖 narrow/wide、dark/high contrast、long text 和 reduced motion。

## Accessibility Testing

自动规则 + 键盘 + accessibility tree/屏幕阅读器 + zoom/reflow 共同使用。不要把“axe 0 violations”等同 WCAG 合规。

## Completion Gate

运行仓库实际使用的 format、lint、typecheck、unit、integration、e2e 和 production build；若某项不存在或无法运行，明确说明原因、风险和替代证据。

## Sources

- [Testing Library: About Queries](https://testing-library.com/docs/queries/about/)
- [Playwright: Best Practices](https://playwright.dev/docs/best-practices)
- [Vue: Testing](https://vuejs.org/guide/scaling-up/testing.html)
- [W3C: Selecting Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/)
