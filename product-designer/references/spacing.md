# Spacing and Layout Rhythm

## Spacing System

选择一个基础单位并建立有限、可命名的尺度，例如 micro、control、group、section、page。具体值可随平台与品牌调整，但必须满足：

- 小间距表达强关联，大间距表达分组与层级；
- 同类关系使用同类间距；
- 一次性数值仅用于有解释的光学校正；
- horizontal gutter、container、column gap 与 vertical rhythm 形成同一系统。

## Macro Layout

先定义内容最大宽度、列数、gutter、断点行为和主要对齐线，再放组件。结构应编码信息关系：宽度、位置、跨列和留白都要说明重要性，而不是只为填满画布。

## Density

- **Comfortable**：阅读、探索、营销和低频操作；
- **Compact**：高频专业工具、表格与大量比较；
- **Adaptive**：根据视口、输入方式或用户偏好切换。

高密度不等于无留白；应把空间保留在对象分组、关键动作和异常信息周围。

## Touch and Target Size

WCAG 2.2 AA 的 Target Size (Minimum) 基线为 `24 × 24 CSS px`，存在间距和其他例外。设计移动触控时优先采用更宽松的平台建议（常见为约 `44 pt` 或 `48 dp`），并检查相邻目标、拇指可达性和误触成本。

## Quality Gate

关闭容器边框与背景后，页面仍应仅凭对齐和间距看出分组。若必须依赖大量卡片框线才能理解结构，重新评估层级。

## Sources

- [Material Design: Layout](https://m3.material.io/foundations/layout/understanding-layout/overview)
- [Apple HIG: Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [WCAG 2.2: Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
