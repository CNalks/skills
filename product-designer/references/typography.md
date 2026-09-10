# Typography

## 建立角色，而不是堆字号

先定义文本角色，再决定字体与数值：

- **Display**：少量品牌表达或关键论点；
- **Heading**：组织页面与章节；
- **Body**：持续阅读与解释；
- **Label**：控件、元数据与短指令；
- **Data / Mono**：需要对齐或区分的数字、代码、时间；
- **Caption**：图注、来源与辅助信息。

每个角色记录 font family、size、line-height、weight、letter-spacing、case 与使用范围。相邻层级必须可辨，但不要用十几个近似字号制造假系统。

## 字体选择

- 从品牌语气、内容类型、语言覆盖与授权开始；不要只因“流行”选字体。
- 正文优先可读性，展示字体承担有限的个性表达。
- 字体组合应有清晰分工；若差异不足，使用同一字族更稳定。
- 检查中文、拉丁、数字、标点、粗体、斜体和缺字回退。
- 将字体加载与授权风险写入设计交接，但不指定工程方案。

## 阅读质量

- 正文行长通常以约 45–75 个拉丁字符作为起点，再按语言与字号实测。
- 行高跟随字号、字宽与内容密度；长文比标签需要更松的节奏。
- 避免过轻字重、全大写长句和低对比小字。
- 金额、表格和时间需要稳定数字宽度或明确对齐规则。
- 放大文本、增加字距/行距后，内容不应被截断、重叠或失去功能。

## Responsive Type

只对真正需要的层级使用流体尺度。窄屏优先保持可读、换行可预测和关键动作不被推离上下文；不要简单按桌面比例缩小全部文字。

## Quality Gate

使用真实标题、最长标签、错误信息、中文/英文混排和高位数字检查。若视觉层级只能靠颜色、位置或装饰成立，重新设计文字角色。

## Sources

- [Material Design: Typography](https://m3.material.io/styles/typography/overview)
- [Apple HIG: Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [WCAG 2.2: Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)
- [WCAG 2.2: Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
