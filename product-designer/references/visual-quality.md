# Visual Quality Framework

在 Wireframe、Design Spec 和最终成品上使用同一套评审语言。每项评为：

- **Pass**：有明确意图，满足当前目标；
- **Revise**：方向成立，但存在可修正缺口；
- **Block**：会妨碍核心任务、破坏系统一致性或造成可访问性失败。

## 十项评审

1. **Brief Fit**：视觉是否来自具体产品、受众、内容和使用情境，而非套模板。
2. **Goal & Task**：首屏论点、主要动作和页面节奏是否支持核心用户任务。
3. **Hierarchy**：3 秒内能否识别“这是什么、最重要的是什么、下一步做什么”。
4. **Composition**：网格、比例、对齐、留白、密度与视觉重心是否有意图。
5. **Typography**：字体角色、尺度、字重、行长、行高和数字样式是否形成稳定系统。
6. **Color**：品牌色、语义色、表面层级、状态与对比度是否完整，不靠颜色单独传意。
7. **Distinctiveness**：是否有一个与产品有关的 signature element；大胆之处是否集中而非到处抢戏。
8. **System Consistency**：token、组件族、圆角、边框、图标、文案和交互状态是否跨页面一致。
9. **Motion & States**：动效是否服务反馈、方向或连续性；空、错、加载、权限等是否被真正设计。
10. **Accessibility & Adaptation**：键盘、焦点、缩放、减少动效、触控与不同视口是否保持体验。

Product Goal、核心 User Flow 或 WCAG AA 出现 `Block` 时，不得交付工程实现。

## Anti AI Slop 检查

出现以下信号时，回到 brief 而不是继续润色：

- 无论产品是什么都使用同样的渐变、玻璃卡、发光光球和大圆角；
- Hero 只有空泛口号，构图与产品核心任务无关；
- 每个区块都是等权卡片，缺少主次和叙事；
- 无意义编号、装饰线、图标或数据被用来制造“设计感”；
- 文案全是“无缝、赋能、下一代”等不可验证词；
- 页面只在理想数据与桌面宽屏上成立；
- 视觉风格来自工具默认值，而非用户、内容或品牌依据。

## 两轮设计法

**Round 1 — Direction**：先写主题、受众、页面论点、字体角色、颜色策略、构图原则与唯一 signature risk，再画结构。

**Round 2 — Critique**：用真实内容与极端状态复查十项评审；删除无法解释的装饰；确认大胆表达只有一个中心，其余元素为它服务。

## Production Quality Mindset

最终 Review 必须基于接近真实的文案、数据长度、图片比例和状态，不使用只为好看而存在的占位内容。分别检查窄屏、宽屏、缩放、长文本、空数据、错误、加载、权限与高密度数据。

## Sources

- [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
- [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills)
- [Material Design 3](https://m3.material.io/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
