# shadcn/ui Component Framework

## Mental Model

shadcn/ui 提供可拥有、可修改的组件源码与组合方式，不是不可见的黑盒组件包。先检查本地 `components.json`、style、底层 primitive（Radix/Base UI 等）、Tailwind 版本与实际源码；不要假定远端最新文档等于当前项目 API。

## Layers

- **Primitive wrapper**：保留语义、键盘、焦点、portal 与状态属性；
- **Design-system component**：映射 token、variant、size 和一致状态；
- **Feature composition**：组合产品对象、数据与业务行为；
- **Page**：只安排结构与流程。

产品级逻辑不要污染 primitive；业务组件也不要复制 primitive 的可访问性实现。

## Composition Rules

- 保留 compound component 的合法组合树和必需 wrapper；
- 根据当前底层库确认 `asChild`、render prop 或 slot API，不凭旧记忆；
- visual variant 不改变语义：导航保持链接，动作保持按钮；
- 使用 CSS semantic variables 映射主题，不在组件中散落品牌颜色；
- 扩展组件时保留 accessible name、label/description、focus management、escape、outside interaction 和 modal 行为；
- 新增 variant 使用项目既有 CVA/variant 方案，并写默认值与冲突规则。

## Update Strategy

组件源码属于项目：更新前先 diff 上游与本地定制，逐个合并并回归测试，不用覆盖式生成抹掉主题、行为或 bug fix。

## Critical Test Set

Button/link、Dialog/Sheet、Dropdown/Menu、Select/Combobox、Tabs、Tooltip、Toast、Form 在键盘、读屏、缩放、mobile 与 portal 场景下测试。自动化之外手动检查焦点进入、循环、恢复与状态公告。

## Sources

- [shadcn/ui Documentation](https://ui.shadcn.com/docs)
- [shadcn/ui Theming](https://ui.shadcn.com/docs/theming)
- [shadcn/ui Component Composition](https://ui.shadcn.com/docs/changelog/2026-04-component-composition)
