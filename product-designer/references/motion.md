# Motion

## 先说明目的

只为以下目的使用动效：

- **Feedback**：确认输入、状态或结果；
- **Direction**：解释对象从哪里来、到哪里去；
- **Continuity**：维持跨状态或跨页面的对象关系；
- **Hierarchy**：把注意力引到刚发生变化的关键区域；
- **Expression**：用一个克制的 signature moment 强化品牌或主题。

无法归入上述目的的动效优先删除。

## Motion Spec

对每个动效记录：触发条件、对象、起止状态、时长范围、easing、延迟/编排、可中断性、重复频率、降级与 `prefers-reduced-motion` 行为。

## Rules

- 高频交互比品牌开场更短、更直接；
- 空间移动应与真实导航方向和对象关系一致；
- 不让动画阻塞输入、延迟内容或掩盖错误；
- 不用持续漂浮、视差、滚动接管或多重 stagger 制造虚假精致；
- 关键状态不能只通过动画表达；暂停后仍能理解；
- 减少动效模式应去除大幅位移、缩放、闪烁和不必要循环，而不是简单加速。

## Review

分别检查首次、重复、高频、慢设备和减少动效场景。若用户第二次执行同一任务时仍被迫等待展示性动画，应缩短或移除。

## Sources

- [Material Design: Motion](https://m3.material.io/styles/motion/overview/how-it-works)
- [Apple HIG: Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- [WCAG 2.2: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
- [WCAG 2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
