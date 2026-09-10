# Accessibility by Design

以 WCAG 2.2 AA 为交付基线，并结合产品用户、平台和法规提高要求。可访问性从目标、结构和流程开始，不是工程阶段的补丁。

## Structure and Meaning

- 页面标题、区域、标题层级和阅读顺序与视觉层级一致；
- 控件有可理解名称，图标不能是唯一说明；
- 链接说明目的，按钮说明动作；
- 复杂图表提供摘要、关键结论和可访问的数据替代；
- 内容在放大、重排和长文本下保持顺序与功能。

## Keyboard and Focus

- 所有操作都有键盘等价路径；
- 焦点顺序遵循任务与阅读逻辑；
- 焦点明显、对比充分且不被 sticky/fixed 内容遮挡；
- 模态、菜单、组合框等交互明确进入、移动、提交与退出方式；
- 不把 hover、拖拽、手势或时间限制作为唯一方法。

## Forms and Errors

- 标签持续可见，placeholder 不代替 label；
- 必填、格式和约束在输入前可理解；
- 错误同时指出对象、原因和修复方法，并保留用户输入；
- 高风险提交提供检查、确认、撤销或纠正；
- 成功、错误和后台进度等状态对辅助技术可感知。

## Visual and Motor

- 普通文本 `4.5:1`，大文本 `3:1`；重要非文本对象按 `3:1` 检查；
- 不只靠颜色、位置、形状或声音表达意义；
- WCAG AA 目标尺寸至少检查 `24 × 24 CSS px` 及例外；移动端优先更大的平台触控目标；
- 支持文本缩放、reflow、横竖屏和减少动效；避免闪烁与不必要自动播放。

## Inclusive States

为空、错误、权限不足、过期、离线、慢网和超时写出清晰恢复路径。不要把辅助说明藏在仅 hover 可见的 tooltip 中。

## Review Gate

设计交付至少包含：键盘顺序、焦点去向、可访问名称、状态通知、错误关联、对比度、目标尺寸、缩放/reflow、减少动效和媒体替代说明。

## Sources

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Material Design: Accessible design](https://m3.material.io/foundations/accessible-design/overview)
- [Apple HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
