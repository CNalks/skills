# Dashboard Design Language

## Intent

为快速判断、异常发现、比较和行动建立高密度但可扫描的系统。品牌感来自数据表达、层级与操作效率，不来自装饰卡片。

## Best For

运营、监测、分析、管理后台、专业工作台和实时态势。若页面主要任务是讲故事或首次转化，选择 Editorial 或 SaaS/Landing 方向。

## Principles

- 先显示需要行动的异常，再显示摘要，再提供细节；
- 每个指标包含范围、单位、时间、基线与新鲜度；
- 颜色主要用于状态与数据编码，不用于随机卡片区分；
- 筛选、下钻、比较和返回保持上下文；
- 密度可调但关键动作始终可见；
- 表格是精确工作工具，不是图表失败后的退路。

## System Recipe

- **Layout**：稳定 shell、过滤区、摘要区、分析区、细节区；列与行对齐支持比较。
- **Typography**：标签、值、单位、变化和注释层次明确；数字使用稳定对齐。
- **Color**：中性表面 + 语义状态 + 有限数据 palette；完整图例与非颜色线索。
- **Spacing**：compact 为主，区域间保留明确分组空间。
- **Shape**：少量边框与表面层级，避免每项独立悬浮卡。
- **Motion**：刷新、筛选和下钻反馈；数据更新不造成无意义跳动。

## Component Families

App shell、global filter、date range、KPI/alert、chart、data table、detail drawer、status banner、saved view、export、audit/meta information。

## Required States

Loading、no data、no result、partial、stale、error、offline、permission、read-only、refreshing、export pending 必须有独立表达。

## Accessibility

遵循 [Accessibility](../../references/accessibility.md)。图表提供摘要与数据替代，表格保持标题/表头/排序语义，筛选与 drawer 有可预测键盘和焦点行为。

## Content Voice

用明确指标名、单位、范围、更新时间和动作描述；警报说明影响与下一步，不用“异常 1”式含糊文案。

## Avoid

等权 KPI 墙、彩虹图表、无单位大数字、只显示百分比变化、3D 图、hover 才能读值、自动轮播、为“科技感”使用发光深色背景。

## Review Gates

用户在短时间内能定位异常和下一动作；数据定义可追溯；筛选影响范围明确；表格支持键盘和缩放；窄屏按决策优先级重排。

## Frontend Handoff

交付数据定义、图表/表格契约、filter scope、density、semantic color、刷新与各状态；工程侧不得自行改变指标优先级。
