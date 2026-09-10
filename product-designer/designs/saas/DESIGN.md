# SaaS Design Language

## Intent

用清晰、可信和可扩展的模块帮助用户理解价值、快速上手并持续完成工作。兼顾营销承诺与产品内效率，但不让二者混成同一套页面模板。

## Best For

B2B 工具、团队协作、订阅软件、开发者产品和多角色工作流。消费品牌或文化内容若需要强烈情绪表达，应另选方向。

## Principles

- 围绕工作对象与任务，而不是功能列表组织 IA；
- 首次使用尽快达到真实价值，不用空洞 onboarding；
- 权限、计划限制、账单和协作状态透明；
- 复用 shell 与组件系统，页面层级保持稳定；
- 信任来自真实产品证据、清楚边界和可恢复操作；
- 营销页与应用内共享品牌 token，但各自服务不同任务。

## System Recipe

- **Layout**：应用 shell + 工作对象；营销页面使用清楚叙事与真实产品画面。
- **Typography**：中性清晰正文，有限品牌 display；标签和帮助文本具体。
- **Color**：品牌强调 + 完整语义状态；升级/付费提示不伪装成错误。
- **Spacing**：产品内适中到紧凑，营销页更舒展；用密度区分场景而非换一套品牌。
- **Shape**：模块化但避免卡片套卡片；表面层级少而稳定。
- **Motion**：工作流反馈与渐进披露，不做干扰式促销动画。

## Component Families

App shell、workspace/project switcher、resource list/detail、command/search、form、collaboration、permission、billing/plan、onboarding、notification、audit/history。

## Required States

New account、empty workspace、trial/expired、permission、invitation、sync、conflict、rate limit、integration disconnected、destructive action 和 recovery。

## Accessibility

遵循 [Accessibility](../../references/accessibility.md)。高频工作流优先键盘与焦点效率；账单、权限和协作状态用明确文本与语义，不只用 badge 颜色。

## Content Voice

专业、可信、具体；区分产品说明、帮助、升级提示与错误，不把付费转化压力混入故障恢复。

## Avoid

一切都做成 Bento 卡片、虚构客户 logo、把升级 CTA 放在每个错误里、含糊权限、无尽设置页、用渐变光球代替产品证据。

## Review Gates

新用户能完成首次价值任务；高频用户路径短；团队角色与权限清楚；营销承诺在产品中可兑现；关键状态可恢复。

## Frontend Handoff

交付 app shell、对象模型、权限矩阵、plan 状态、token、组件 variant、响应式密度与恢复路径；工程侧不自行改变商业或权限逻辑。
