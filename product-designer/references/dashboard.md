# Dashboard Design

## Start with Decisions

先问“用户看完后要判断什么、采取什么动作”，再决定指标和图表。每个 Dashboard 定义：角色、决策频率、时间窗口、数据新鲜度、错误成本和后续动作。

## Information Hierarchy

推荐结构：

1. 当前范围、时间、数据更新时间与全局状态；
2. 需要注意的异常、风险或待办；
3. 核心结果及与基线/目标的比较；
4. 趋势、分布、贡献与原因；
5. 可筛选、排序、导出或下钻的细节；
6. 数据定义、来源和限制。

不要创建等权 KPI 卡片墙。规模、变化、目标、基线和不确定性必须有上下文，避免 vanity metrics。

## Chart and Table Choice

- 趋势用位置连续的时间序列；
- 分类比较优先共同基线；
- 部分与整体仅在总量明确时使用；
- 精确查找、密集比较和操作使用表格；
- 地理图只在空间关系影响判断时使用；
- 颜色表达一个清楚维度，避免彩虹与 3D。

标题应直接说明指标和范围；单位、分母、时区、缺失值、估算和数据更新时间可见。

## Interaction

全局筛选影响范围必须明确；筛选条件可查看、清除、分享或恢复。下钻后保留上下文和返回路径。危险批量操作显示影响范围并可撤销或确认。

## Required States

设计 loading、empty、no result、partial data、stale data、error、offline、permission、read-only 和 export pending。骨架屏只在结构稳定时使用；不确定时优先进度与说明。

## Accessibility and Responsive

图表提供文本摘要、可访问名称和数据替代；不要只靠颜色。窄屏按任务优先级重排，而不是横向压缩全部卡片；高价值异常和动作先于次要趋势。

## Sources

- [NN/g: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Material Design: Color](https://m3.material.io/styles/color/overview)
- [WCAG 2.2: Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
