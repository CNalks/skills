# Tailwind Rules

## Version First

先确认 Tailwind 版本和现有配置。v4 使用 CSS-first theme variables 等机制；不要把 v3 的配置与插件写法盲目套入 v4 项目。

## Map Semantic Tokens

将 Product Designer 的语义 token 映射到主题变量：canvas、surface、text、border、action、status、spacing、type、radius、shadow、motion。组件使用语义 token，不直接散落品牌 hex、任意 spacing 或“blue-500”式用途不明值。

## Utility Rules

- 默认移动优先：无前缀是窄屏基线，再添加明确断点；
- class 名以完整静态字符串出现；动态 variant 使用显式映射，不拼接碎片；
- 重复出现且有系统意义的值提升为 token；任意值只用于真正一次性且有理由的局部场景；
- 使用语义 `variant`、`size` 和状态 props 组织组件，避免调用方堆叠冲突 class；
- 需要复杂选择器、动画或浏览器能力时直接使用原生 CSS，不滥用 `@apply`；
- RTL 优先 logical properties；检查打印、dark/high-contrast 和 forced colors（适用时）。

## State Coverage

为交互组件显式覆盖 hover（适用时）、active、focus-visible、disabled、aria/data state、invalid、loading、dark 与 reduced-motion。不要用 `outline-none` 移除焦点而不提供等价替代。

## Composition

UI primitive 管理基础样式与 variant；feature 组件组合行为和业务状态；页面不应重复同一长串 utilities。抽象发生在稳定重复之后，不把每个 `div` 封装成组件。

## Review

- [ ] 版本与配置匹配。
- [ ] class 静态可检测，production build 不丢样式。
- [ ] token 语义与设计交付一致。
- [ ] 响应式从内容断点出发，不只追设备名。
- [ ] state、dark、reduced-motion、RTL 与冲突 utilities 已检查。

## Sources

- [Tailwind CSS: Theme Variables](https://tailwindcss.com/docs/theme)
- [Tailwind CSS: Responsive Design](https://tailwindcss.com/docs/responsive-design)
- [Tailwind CSS: Detecting Classes](https://tailwindcss.com/docs/detecting-classes-in-source-files)
- [Tailwind CSS: States](https://tailwindcss.com/docs/hover-focus-and-other-states)
