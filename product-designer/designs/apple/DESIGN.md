# Apple-inspired Design Language

> 独立的原创设计方向，不是 Apple 官方规范或资源包。不得声称获得 Apple 认可，也不要捆绑或再分发 Apple UI Kit、SF 字体或 SF Symbols。

## Intent

以 clarity、deference、depth 为灵感：界面安静、内容优先、交互自然，品牌感来自比例、材质、排版与细节，而不是装饰堆叠。

## Best For

高信任消费产品、个人工具、健康与生活方式、设备协同、内容与创作应用。若产品需要极高数据密度、强烈反文化表达或严肃工业控制，应评估其他语言。

## Principles

- 让内容与当前任务占据视觉中心，chrome 退后；
- 以少量清晰层级替代大量边框与卡片；
- 使用熟悉的平台行为，减少学习成本；
- 深度只表达层级、暂态或空间关系；
- 细腻反馈胜过持续动画；
- 每个页面只有一个明确主要动作。

## System Recipe

- **Layout**：宽松边距、稳定对齐、清楚内容区；大屏增加呼吸而非无限拉宽。
- **Typography**：中性高可读正文，克制的大标题；用字重、尺度和留白建立层级。
- **Color**：中性表面占主导，强调色集中于动作与关键状态；支持浅/深模式。
- **Spacing**：舒适密度，相关对象紧密、章节之间明显分隔。
- **Shape & Depth**：圆角与模糊只在能说明容器、浮层或材质时使用；避免“满屏玻璃”。
- **Motion**：短促、连续、可中断；减少动效时保留状态反馈。

## Component Families

Navigation bar、sidebar、segmented control、list row、form control、sheet/dialog、toolbar、content card、status/feedback、search。组件优先内容与行为一致，不追求视觉花样数量。

## Required States

为每个关键组件定义 default、hover（适用时）、pressed、focus、selected、disabled、loading、error；页面覆盖 empty、offline、permission 和 interrupted task。

## Accessibility

遵循 [Accessibility](../../references/accessibility.md)。克制视觉不能依赖低对比、隐藏标签或手势；动态字体、键盘、触控与减少动效必须保留清晰层级。

## Content Voice

简洁、直接、平静；解释下一步，不使用夸张承诺。错误文案帮助恢复，权限文案先说明用户价值。

## Avoid

仿制 Apple 产品页面、到处使用毛玻璃、把极细灰字当高级感、强迫手势、隐藏关键动作、滥用超大标题或设备 mockup。

## Review Gates

内容在移除阴影与背景模糊后仍有清晰层级；平台行为符合用户预期；文本、焦点、触控和减少动效通过检查；克制不以牺牲可发现性为代价。

## Frontend Handoff

交付语义 tokens、组件状态、平台差异、材质用途与 motion spec；不要要求工程侧复制 Apple 私有资源或像素级仿制系统界面。

## Sources

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
