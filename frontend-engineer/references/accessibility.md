# Frontend Accessibility Checklist

以 WCAG 2.2 AA 为默认工程基线；结合目标市场法规、平台和产品风险提高要求。自动化工具只能发现部分问题，不能单独证明合规。

## Semantics

- 优先原生 `button`、`a`、`input`、`select`、`dialog`、landmark、heading、list 与 table；
- DOM/读屏顺序与视觉和键盘顺序一致；
- 所有控件有正确 accessible name、role、value/state；
- ARIA 只补语义缺口，不覆盖错误的原生语义；
- 图标、图片、图表和媒体有适合目的的替代。

## Keyboard and Focus

- 所有功能可用键盘完成，无 keyboard trap；
- Tab 顺序自然；方向键等复杂组件行为遵循可靠模式；
- `focus-visible` 清晰且不被 sticky header、toast 或浮层遮挡；
- 打开 modal/menu 后焦点进入合适位置，关闭后返回触发点；
- hover、drag、gesture 都有可发现的等价操作。

## Forms and Dynamic UI

- label 与字段程序化关联，说明和错误用正确关系连接；
- 客户端验证提供即时帮助，服务端仍执行权威验证；
- 错误摘要可聚焦并链接到字段，输入不丢失；
- loading、success、error、后台完成等使用恰当 live region/status，不制造重复朗读；
- 异步更新后管理焦点，不让用户丢失位置。

## Visual and Input

- 普通文本对比 `4.5:1`、大文本 `3:1`；必要控件/图形 `3:1`；
- 颜色不是唯一信息渠道；
- WCAG 2.2 AA 指针目标检查至少 `24 × 24 CSS px` 及例外，触控产品优先更舒适尺寸；
- 200% 文本缩放、400% reflow、窄屏、长语言和高对比模式可用；
- 支持 `prefers-reduced-motion`，避免闪烁和不可暂停内容。

## Test Matrix

1. 只用键盘完成核心流程；
2. 用浏览器 accessibility tree/屏幕阅读器检查名称、结构、状态与顺序；
3. 运行 axe 等自动检查并人工判断；
4. 检查 zoom、reflow、contrast、forced colors、reduced motion；
5. 对 Dialog、Menu、Tabs、Combobox、Data Grid 等复杂模式做组件级回归。

## Sources

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA APG: Keyboard Interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)
- [WAI-ARIA APG: Names and Descriptions](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/)
- [WAI: Form Validation](https://www.w3.org/WAI/tutorials/forms/validation/)
- [W3C: Selecting Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/)
