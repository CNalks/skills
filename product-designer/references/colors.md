# Color System

## 从语义 token 开始

先定义角色，再选择具体颜色：

- `canvas`、`surface`、`surface-raised`；
- `text-primary`、`text-secondary`、`text-disabled`；
- `border-subtle`、`border-strong`、`focus-ring`；
- `action-primary`、`action-secondary`、`link`；
- `success`、`warning`、`danger`、`info`；
- 数据图表的 categorical、sequential 与 diverging palettes。

颜色名不要成为实现契约；`blue-500` 不能表达用途，`action-primary` 才能。

## 品牌与功能分离

- 品牌色表达身份，功能色表达状态；二者冲突时，状态识别优先。
- 主要动作不等于“全页面最亮颜色到处使用”。控制强调数量，保留清晰焦点。
- 浅色、深色和高对比模式分别验证，不用简单反相。
- 图表用形状、标签、纹理或位置补充颜色，不让颜色成为唯一线索。

## WCAG AA 基线

- 普通文本与背景至少 `4.5:1`；大文本至少 `3:1`。
- 重要控件边界、状态与图形对象通常至少 `3:1`，并按适用成功准则检查。
- 焦点、错误、选择和禁用状态不能只靠色相变化。
- 对比通过只是底线；仍要检查眩光、色弱、低质量屏幕和户外场景。

## 交付

为每个 token 记录用途、前景/背景配对、交互状态、浅/深模式映射与禁用组合。不要交付一张没有语义和用例的色板。

## Sources

- [Material Design: Color](https://m3.material.io/styles/color/overview)
- [Apple HIG: Color](https://developer.apple.com/design/human-interface-guidelines/color)
- [WCAG 2.2: Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [WCAG 2.2: Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- [WCAG 2.2: Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)
