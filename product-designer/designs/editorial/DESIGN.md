# Editorial Design Language

## Intent

把界面视为有节奏的出版物：阅读、叙事、证据与作者声音优先。通过标题、导语、正文、图像、图注和留白建立时间与情绪。

## Best For

媒体、报告、研究、文化、品牌故事、长文知识产品和高质量内容营销。不适合以高频操作、实时监控或密集录入为核心的界面。

## Principles

- 内容模型决定页面结构；
- 首屏建立主题、来源和阅读承诺；
- 字体角色与 baseline rhythm 维持长阅读；
- 图像、引文和数据必须有来源与语境；
- 节奏通过宽窄、长短、留白和跨栏变化，而非装饰噪声；
- 导航与阅读进度不打断内容。

## System Recipe

- **Layout**：正文窄列与媒体宽区并存；章节、边注和图注有稳定位置。
- **Typography**：display/serif 可承担主题个性，正文优先耐读；区分标题、deck、byline、body、caption、footnote。
- **Color**：纸张/墨色式中性为主，主题色点到为止；链接与状态仍需明确。
- **Spacing**：以段落、章节与媒体节奏组织，不用等高卡片抹平内容差异。
- **Imagery**：真实图片与图表保留比例、来源、说明和替代文本。
- **Motion**：阅读进度、目录定位和媒体揭示保持克制。

## Component Families

Masthead、article header、table of contents、prose、figure、caption、pull quote、footnote、data callout、author/source、related stories、newsletter/CTA。

## Required States

覆盖图片失败、来源缺失、付费/权限、目录定位、搜索无结果、媒体加载和长内容；不伪造缺失的内容或元数据。

## Responsive

保持正文可读行长；边注转为内联或可访问的补充块；媒体与图注不分离；目录可折叠但始终可发现。

## Accessibility

遵循 [Accessibility](../../references/accessibility.md)。正文支持缩放与 text spacing；图注、脚注、引文和来源拥有清晰关系；视觉跨栏不改变阅读顺序。

## Content Voice

尊重作者与来源，标题准确，导语说明价值，图注与数据描述具体；营销 CTA 不伪装成正文。

## Avoid

假报纸纹理、伪造日期/作者/引用、每段一个 pull quote、难读 display 字体、无限滚动却没有位置感、用卡片墙替代叙事。

## Review Gates

使用完整真实文章测试；标题到正文的层级可扫描；来源与图注齐全；放大文本不截断；阅读顺序在窄屏与读屏中一致。

## Frontend Handoff

交付文本角色、正文宽度、媒体比例、图注/脚注关系、目录行为、长文与窄屏规则，以及内容缺失和权限状态。
