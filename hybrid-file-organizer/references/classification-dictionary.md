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

## Naming evidence rule
Category choice and filename choice do not have the same evidence threshold.

- category may use medium evidence when the bucket is broad and low-risk
- specific filename wording must use evidence that is at least as strong as the claim in the name
- when evidence is weak, keep the filename generic rather than specific

Examples:
- acceptable with weak evidence: `AQF_压缩包`
- acceptable with medium evidence: `AQF资料_压缩包`
- requires strong evidence: `量化金融分析师AQF实训课程资料包`

## Special path-type strategy

### Desktop-like roots
Examples:
- Desktop
- pinned work areas that behave like a user launch surface

Handling rule:
- audit `.lnk` and `.url` files before moving nearby targets
- preserve shortcuts by default
- treat shortcut targets as dependency edges, not ordinary files

### Cloud-sync roots
Examples:
- OneDrive
- Dropbox
- iCloud Drive
- synced team folders

Handling rule:
- high-risk by default
- do not move content across the sync boundary without explicit confirmation
- preserve folder structure when the sync model depends on path stability

### Chat attachment roots
Examples:
- WeChat attachment storage
- Tencent or QQ received-file areas
- Telegram export or attachment buckets

Handling rule:
- prioritize true received-file or attachment areas before caches
- treat image pools and media caches as lower-priority unless the user includes them

### Code project roots
Examples:
- source repositories
- experiment folders
- script bundles

Handling rule:
- prefer folder-level moves
- avoid splitting projects into flat file buckets
- preserve configuration, dependency files, and relative layout

### Portable app roots
Examples:
- green software
- unpacked app folders
- self-contained tool bundles

Handling rule:
- audit launchers, config files, data directories, and shortcut targets first
- prefer moving the whole app directory as a unit

### Runtime or install roots
Examples:
- Python runtimes
- Java runtimes
- application install directories

Handling rule:
- exclude by default
- only touch them when the user explicitly asks and accepts the risk

## Level-1 categories

### Work Materials
Include:
- monitoring reports
- disease control work files
- notices, implementations, and work plans
- business project materials
- operational spreadsheets and tracking files

Suggested subcategories:
- system-projects
- work-topics
- monitoring-data
- monitoring-briefs
- prevention-and-control
- training-and-briefing
- school-health

### Research Materials
Include:
- papers
- modeling work
- research reports
- analysis outputs
- study data and appendices

Suggested subcategories:
- research-code
- research-data
- research-reports
- research-literature

### Study and Exams
Include:
- exam prep
- training content
- lecture material
- question practice
- interview prep

Suggested subcategories:
- topic-materials
- training-and-prep

### Administrative Materials
Include:
- recruitment materials
- application forms
- approvals
- HR paperwork
- identity-related filing materials

Suggested subcategories:
- recruitment
- approvals
- personal-materials

### Finance Materials
Include:
- budgets
- reimbursements
- fiscal decisions
- department settlement documents
- fund allocation sheets

Suggested subcategories:
- budgets-and-funds
- reimbursement-and-procurement
- ledgers-and-reconciliation

### Software and Scripts
Include:
- code folders
- script files
- portable apps
- strategy files
- local utilities

Suggested subcategories:
- code-projects
- script-snippets
- portable-apps
- trading-records

### Images and Media
Include:
- photos
- screenshots
- videos
- voice notes
- exported charts

Suggested subcategories:
- images
- videos
- audio
- chart-exports

### Installers and Archives
Include:
- installers
- archives
- software resource bundles
- download leftovers

Suggested subcategories:
- installers
- archives
- download-leftovers

### Manual Review
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

Do not perform final high-impact moves on `low` confidence items without routing them through `manual-review`.
