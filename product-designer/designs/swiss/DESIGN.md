# Swiss Design Language

## Intent

用严格网格、客观层级、无衬线排版和非对称平衡传达秩序、精确与公共信息感。视觉表达来自结构本身。

## Best For

文化机构、知识产品、研究工具、专业服务、目录、活动与具有强内容结构的品牌。若内容高度情绪化、儿童化或需要柔软亲密感，应谨慎选择。

## Principles

- 网格先于装饰，所有关键元素共享可解释的对齐线；
- 强尺度对比建立层级，细小差异不承担重要区分；
- 非对称不等于随机，视觉重量必须平衡；
- 有限颜色与几何形态服务信息编码；
- 图片作为内容证据或构图对象，不作无意义填充；
- 文案客观、具体、短句优先。

## System Recipe

- **Layout**：定义列、gutter、baseline 与跨列规则；保留大面积主动留白。
- **Typography**：一到两个无衬线字族角色；明显的 display/body 比例；标签与编号遵循真实 taxonomy。
- **Color**：黑白/中性为主，一个高饱和强调色；状态色保持独立语义。
- **Spacing**：模数化节奏，章节间距显著大于对象内间距。
- **Shape**：矩形、线、色块和裁切；边框只表达结构。
- **Motion**：直接的位移、揭示与排序反馈，避免弹性玩具感。

## Component Families

Grid header、index/navigation、content block、fact row、data table、filter rail、poster/hero、figure/caption、notice、pagination。

## Required States

导航、筛选、表格与内容对象覆盖 focus、selected、disabled、loading、empty、error 和 no-result；状态仍遵循网格与标签系统。

## Responsive

窄屏减少列数但保留主对齐线、阅读顺序与尺度对比；不要把桌面错位构图机械堆叠。编号、标签和内容必须保持真实关系。

## Accessibility

遵循 [Accessibility](../../references/accessibility.md)。强尺度对比不能牺牲正文可读性；非对称构图的 DOM、键盘和读屏顺序保持任务逻辑。

## Content Voice

客观、精确、短句与名词优先；编号和标签必须来自真实信息结构。

## Avoid

无意义 `01/02/03`、随机错位、每区块一条红线、假网格、过度全大写、把低对比小字当现代感、忽略中文排版与长单词。

## Review Gates

关闭颜色后结构仍清楚；每条对齐线都能说明信息关系；非对称保持阅读顺序；强调色不过度使用；缩放和窄屏不破坏内容。

## Frontend Handoff

交付列网格、gutter、baseline、跨列规则、排版角色、强调色用途、窄屏重排和所有状态，不把随机坐标当规范。
