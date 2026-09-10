# Minimal Design Language

## Intent

通过删减、秩序和准确细节降低认知负担。Minimal 不是“什么都没有”，而是每个留下的元素都有任务。

## Best For

单一任务工具、精品服务、作品集、专注型生产力产品、高端但克制的品牌。复杂平台若没有成熟 IA，极简会把复杂性藏给用户，应先解决结构。

## Principles

- 一个页面一个主要目标；
- 用信息层级、排版和空间代替多余容器；
- 控件少但可发现，标签清楚；
- 颜色与形状数量有限，状态完整；
- 内容短而具体，不用空白掩盖缺乏信息；
- 一个 signature detail 足够，其余保持安静。

## System Recipe

- **Layout**：有限最大宽度、强对齐、大块留白、少量稳定区域。
- **Typography**：少层级、明显但克制的尺度；正文与标签优先清晰。
- **Color**：中性基底、一个主强调、完整状态色。
- **Spacing**：大空间用于章节，小空间用于关联；避免所有间距都巨大。
- **Shape & Depth**：尽量平面；只有浮层或对象关系需要时使用深度。
- **Motion**：快速反馈和细微过渡，不做展示性等待。

## Component Families

Top/side navigation、content section、list row、form field、button/link、dialog、notice、empty state。组件数量少，但所有状态不能缺。

## Required States

为少量组件完整定义 focus、disabled、loading、empty、error、permission 和 success；极简不能只设计理想状态。

## Accessibility

遵循 [Accessibility](../../references/accessibility.md)。可见标签、焦点、对比和触控目标优先于“干净”；不通过移除说明来降低视觉噪声。

## Content Voice

短、具体、行动导向；必要解释就近出现，不用极短但含糊的单词迫使用户猜测。

## Avoid

隐藏导航、只有图标无标签、低对比灰字、巨大留白导致任务断裂、用一句空泛口号代替内容、移除必要边界和反馈。

## Review Gates

删除任意元素前说明其用户价值；首次用户能发现核心操作；错误与权限路径不比成功路径更难；高对比与键盘焦点不因“纯净”被弱化。

## Frontend Handoff

交付元素保留理由、最大宽度、对齐线、有限 tokens、所有交互状态与极端内容测试；不要让工程师自行决定哪些说明可删。
