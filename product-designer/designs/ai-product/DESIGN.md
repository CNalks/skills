# AI Product Design Language

## Intent

让 AI 能力可理解、可控制、可校正，而不是以“魔法感”掩盖不确定性。产品价值来自人机协作结果，不来自聊天框、紫色渐变或发光效果。

## Best For

生成、分析、推荐、Agent、自动化与辅助决策产品。若 AI 只是后台实现细节，不应强迫整套产品使用 AI 视觉语言。

## Principles

- 清楚说明 AI 在做什么、需要什么输入、可能失败在哪里；
- 显示来源、状态、范围、时间和适当的不确定性；
- 人类能预览、编辑、批准、拒绝、撤销和接管；
- 自动化权限与影响范围逐级明确；
- 失败、部分结果和等待状态比成功 demo 更重要；
- 根据任务选择 form、canvas、table、workflow 或 chat，不把 chat 当默认 UI。

## System Recipe

- **Layout**：输入、上下文、过程、输出与控制区关系明确；长任务提供持久状态。
- **Typography**：区分用户输入、系统说明、生成内容、来源和元数据。
- **Color**：品牌与状态分离；AI 内容不用单一“紫色”编码；风险与权限使用语义色。
- **Spacing**：让来源、修改和确认靠近相关输出；避免把所有内容塞进气泡。
- **Shape**：对象与步骤优先，聊天气泡仅用于真正对话。
- **Motion**：进度表达真实阶段；禁止无意义“思考”动画掩盖未知等待。

## Component Families

Prompt/input、context/source manager、run status、step timeline、artifact/output、citation/provenance、diff/review、approval、feedback/correction、history/version、permission/scope。

## Required States

Queued、running、waiting for user、partial、tool failure、unsafe/refused、low confidence、stale source、cancelled、retrying、completed with warnings、permission escalation。

## Accessibility

遵循 [Accessibility](../../references/accessibility.md)。流式输出不应造成持续抢焦点或重复朗读；过程、来源、修改和批准均可键盘访问，并提供非动画状态。

## Content Voice

具体描述能力与限制，不拟人化保证、不夸大确定性。错误说明失败阶段、已完成部分、数据是否保存和可采取动作。

## Avoid

默认聊天框、闪烁光标冒充进度、伪造“置信度”、隐藏来源、自动执行高影响动作、不可撤销替换、紫色渐变 + 星星图标的通用 AI 包装。

## Review Gates

用户能区分建议与事实；来源和修改可追溯；自动化范围可见；高风险动作需确认并可恢复；无 AI 视觉装饰时产品价值仍成立。

## Frontend Handoff

交付任务状态机、来源/引用模型、人工批准点、diff 与恢复行为、权限范围、长任务通知和所有失败状态；工程侧不得把未知状态伪装成确定进度。
