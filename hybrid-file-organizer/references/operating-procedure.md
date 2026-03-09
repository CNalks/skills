# Operating Procedure

## 1. Scope confirmation
Confirm the exact scope before scanning or moving.

If the user did not define it precisely:
- propose a concrete scope
- call out risky inclusions and exclusions
- get confirmation before broad scanning

## 2. Stage design and tool selection
Before selecting tools, define the stages of the job:
- inventory
- shortcut audit if desktop-like roots are included
- content sampling
- classification
- duplicate handling
- renaming
- moving
- logging

For each stage, decide in order:
1. existing wheel
2. adapted wheel
3. custom script

Do not start with implementation. Start with the stage plan.

## 3. Pre-scan
Inventory candidate roots before any move:
- file count
- directory count
- recursive size
- extension distribution
- obvious hot spots

Use `scripts/inventory_paths.py` for this step.

## 4. Shortcut audit for desktop-like roots
If the scope includes a desktop-like root:
- inventory `.lnk` and `.url` files
- extract their targets if possible
- check whether the target paths fall inside the planned move scope
- flag shortcut targets as high-risk dependencies

Default policy:
- do not move shortcuts themselves
- do not move shortcut targets blindly
- preview affected shortcuts before applying the move

## 5. Candidate selection
Prioritize:
- scattered user documents
- chat-received attachments
- code folders
- portable apps
- mixed download folders
- document-heavy directories with clear themes

De-prioritize:
- image pools without context
- caches
- databases
- ad resources
- runtime folders that could break installed software

## 6. Content sampling
Sample only what is needed:
- `docx`: title, first sections, first table
- `pdf`: first page and first two pages
- `xlsx/csv/tsv`: sheet names, headers, first 10-20 rows
- code folders: `README`, config, entry points
- portable apps: exe names, readme, config folders

Use the corresponding session skills when available:
- `doc`
- `pdf`
- `spreadsheet`

## 7. Classification
Classify in this order:
1. choose the level-1 category
2. choose the subcategory
3. decide whether to move a whole folder or split individual files

Prefer folder-level moves when a directory is clearly single-theme.  
Prefer file-level moves when a folder is mixed or behaves like a download bucket.

## 8. Duplicate and conflict handling
Before applying duplicate actions, decide which mode is appropriate:
- rename only
- keep both with clearer names
- merge after review
- leave in `manual-review`

Do not delete or overwrite duplicates without explicit user confirmation.

## 9. Renaming
Rename before moving.

Use Chinese names by default when the user wants Chinese naming. Keep English only for:
- software names
- protocol names
- market symbols
- versions
- established project identifiers

Recommended fields:
- subject
- date
- unit
- phase
- version

Strip:
- random download numbers
- repeated brackets
- hash fragments
- duplicated separators

Use `_1`, `_2` only after content-aware disambiguation fails.

## 10. High-risk confirmation gate
Ask the user before applying high-risk operations:
- large batch moves
- duplicate merge or overwrite decisions
- moving code projects or portable apps
- touching cloud-synced folders
- moving shortcut targets discovered in desktop-like roots
- handling sensitive personal or financial files

Use a two-phase approach whenever practical:
1. preview
2. apply after confirmation

## 11. Logging
For every run, keep a CSV or markdown log with:
- source path
- destination path
- category
- confidence
- skipped reason

## 12. Safety gates
Stop and route to review when:
- a folder mixes work, research, personal, and finance files
- a file contains sensitive identity data
- a file is a contract or reimbursement original
- extraction fails and the filename is weak
- moving a folder could break an installed runtime or application
- moving the target would likely orphan or destabilize a shortcut

## 13. Future portability note
This skill is currently optimized for Windows-heavy workflows, but the architecture should remain portable.

Future extension notes:
- keep path strategies abstract instead of hardcoding one OS
- isolate shortcut or alias auditing behind platform-specific tooling
- separate generic classification logic from OS-specific file metadata logic
- prefer scripts and references that can later be swapped for Linux or macOS equivalents

## 14. Completion checklist
Before closing a pass, verify:
- the user-confirmed scope was respected
- the stage plan was defined before selecting tools
- the scan roots were inventoried first
- chat attachment folders were handled only if included in scope
- cloud-synced roots were excluded unless explicitly included
- shortcut targets were audited if desktop-like roots were included
- renaming happened before the move
- moved items have logs
- unresolved items are in `manual-review`
- root clutter in desktop-like or download-like roots is reduced without breaking shortcuts or installed software
