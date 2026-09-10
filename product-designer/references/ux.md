# UX Framework

## 1. 从证据开始

把输入标成四类，防止把猜测包装成研究：

- **Evidence**：访谈、行为数据、工单、可用性测试或明确业务约束。
- **Assumption**：尚未验证、但为继续设计暂时采用的判断。
- **Constraint**：法规、平台、时间、技术、内容或运营限制。
- **Open question**：会改变目标、范围、流程或架构的未知项。

若没有真实研究，明确写“待验证”，并提出最低成本的验证方法；绝不虚构用户原话、样本量或数据。

## 2. Product Goal

用一句话描述：`帮助 [目标用户] 在 [情境] 完成 [关键结果]，从而 [用户/业务价值]。`

同时定义：

- 当前问题与证据；
- 成功指标与反指标；
- 本轮范围和非目标；
- 失败会造成的风险。

指标应衡量任务结果，不只衡量页面点击或停留时长。

## 3. Target User 与 User Tasks

优先描述行为与情境，而不是虚构完整 Persona：

- 用户角色、知识水平、设备与环境；
- 触发任务的事件；
- 用户想取得的结果；
- 频率、紧急程度、错误成本；
- 现有替代方案与主要障碍；
- 辅助技术、语言、认知或运动能力需求。

把任务按 `核心 / 支持 / 边缘` 排序。核心任务必须在主导航、主流程和首屏层级中得到相应权重。

## 4. Journey、Task Flow 与 User Flow

- **Journey**：跨渠道、跨时间观察用户的目标、行为、情绪和断点。
- **Task Flow**：完成单一任务的理想步骤。
- **User Flow**：包含入口、分支、决定、异常、取消和恢复的系统路径。

每条关键 Flow 至少标注：入口、前置条件、步骤、系统反馈、成功终点、失败/空/权限/离线路径、取消与恢复方式。

## 5. Information Architecture

按以下顺序建立 IA：

1. 列出用户需要寻找、理解、比较、创建和管理的内容与动作。
2. 按用户心智模型聚类，建立 taxonomy 与稳定命名。
3. 区分全局、局部、上下文与工具型导航。
4. 画 sitemap 或对象关系，标出层级、父子和交叉入口。
5. 用核心任务验证可发现性：用户是否知道“我在哪、能去哪、如何返回”。
6. 对不确定分组使用 card sorting 或 tree testing 验证。

导航标签使用用户语言；不要用内部组织架构、含糊图标或营销词代替信息气味。

## 6. Page Structure

页面不是组件清单，而是信息与动作的优先级：

- 用一句话定义页面唯一主要任务；
- 明确首要信息、主要动作、次要动作与补充证据；
- 先用真实内容验证阅读顺序，再决定卡片、分栏或容器；
- 对长流程提供进度、保存、返回和恢复；
- 对危险或不可逆操作提供预防、确认和补救。

## 7. Interaction State Model

每个关键对象或页面都检查：initial、loading、partial、empty、success、error、stale、offline、permission denied、read-only、disabled。状态必须解释发生了什么、为何发生、用户能做什么；恢复动作应靠近问题。

## 8. UX Review

按任务逐条检查：

- 系统状态是否可见，反馈是否及时；
- 语言是否贴近用户现实；
- 用户是否可撤销、返回或恢复；
- 相似行为是否一致；
- 是否预防高成本错误；
- 关键信息与操作是否可识别而非依赖记忆；
- 熟练用户是否有更高效路径；
- 错误信息是否具体、礼貌、可执行；
- 是否提供恰当帮助而不过度打断。

## Sources

- [NN/g: Task Analysis](https://www.nngroup.com/articles/task-analysis/)
- [NN/g: Journey Mapping 101](https://www.nngroup.com/articles/journey-mapping-101/)
- [NN/g: User Journeys vs. User Flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/)
- [NN/g: Information Architecture Study Guide](https://www.nngroup.com/articles/ia-study-guide/)
- [NN/g: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Apple HIG: Navigation and search](https://developer.apple.com/design/human-interface-guidelines/navigation-and-search)
