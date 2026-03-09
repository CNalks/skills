# Classification Dictionary

## Scope rule
The user defines the scope. Do not silently expand it.

If the user gives a broad target such as a whole drive, split it into reviewable candidate areas first and confirm any risky inclusions.

Common high-priority user-file areas, when included by the user:
- desktop-like roots
- downloads or inbox folders
- documents or archive folders
- chat attachment folders
- pictures and videos
- code folders
- portable app folders
- cloud-synced folders

## Core rule
Use path, size, and extension distribution to decide what to inspect.  
Use file content, titles, headers, README files, and nearby context to decide the final category.

## Level-1 categories

### 工作资料
Include:
- monitoring reports
- disease control work files
- notices, implementations, and work plans
- business project materials
- operational spreadsheets and tracking files

Typical signals:
- `监测`
- `流调`
- `防控`
- `疾控`
- `工作方案`
- `项目建设方案`
- `通报`

Suggested subcategories:
- `系统项目`
- `工作专题`
- `监测数据`
- `监测周报与通报`
- `疫情研判与防控`
- `培训与汇报材料`
- `校园卫生与学校防控`

### 科研资料
Include:
- papers
- modeling work
- research reports
- analysis outputs
- study data and appendices

Typical signals:
- `研究`
- `流行病学`
- `趋势预测`
- `模型`
- `神经网络`
- `appendix`
- `supplementary`

Suggested subcategories:
- `研究代码`
- `研究数据`
- `研究报告`
- `科研文献`

### 学习考试
Include:
- exam prep
- training content
- lecture material
- question practice
- interview prep

Typical signals:
- `面试`
- `练习题`
- `课程`
- `讲义`
- `训练`

Suggested subcategories:
- `专题资料`
- `培训与备考资料`

### 行政材料
Include:
- recruitment materials
- application forms
- approvals
- HR paperwork
- identity-related filing materials

Typical signals:
- `招聘`
- `岗位表`
- `报名`
- `审批`
- `证明`
- `政审`

Suggested subcategories:
- `招聘考试资料`
- `报名与审批材料`
- `简历与个人材料`

### 经费财务
Include:
- budgets
- reimbursements
- fiscal decisions
- department settlement documents
- fund allocation sheets

Typical signals:
- `经费`
- `预算`
- `绩效`
- `决算`
- `发票`
- `中央转移支付`

Suggested subcategories:
- `绩效与经费`
- `报销与采购`
- `台账与对账`

### 软件与脚本
Include:
- code folders
- script files
- portable apps
- strategy files
- local utilities

Typical signals:
- `README`
- `package.json`
- `pyproject.toml`
- `.mq4`
- `.mq5`
- `.ex4`
- `.py`
- `.ipynb`
- `portable`

Suggested subcategories:
- `代码项目`
- `脚本片段`
- `绿色软件`
- `交易记录`

### 图片与媒体
Include:
- photos
- screenshots
- videos
- voice notes
- exported charts

Suggested subcategories:
- `图片`
- `视频`
- `音频`
- `图表导出`

### 安装与压缩包
Include:
- installers
- archives
- software resource bundles
- download leftovers

Suggested subcategories:
- `安装包`
- `压缩包`
- `下载残留`

### 待人工复核
Use for:
- sensitive personal data
- contracts
- low-confidence classification
- unreadable files
- mixed-theme folders

## Chat attachment folder rule
When the scope includes chat application data, prioritize true attachment or received-file areas before caches.

Common patterns:
1. received files
2. attachment storage
3. favorites or saved files
4. backup file buckets

Lower priority:
- image pools without clear context
- audio or video caches
- applet or plugin bundles
- cache and database folders

## Confidence
- `high`: filename and sampled content agree
- `medium`: directory context is strong and sampled content partly supports it
- `low`: classification depends mostly on weak names or incomplete extraction

Do not perform final high-impact moves on `low` confidence items without routing them through `待人工复核`.
