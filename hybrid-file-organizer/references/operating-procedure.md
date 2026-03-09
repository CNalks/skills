# Operating Procedure

## 1. Scope confirmation
Confirm the exact scope before scanning or moving.

If the user did not define it precisely:
- propose a concrete scope
- call out risky inclusions and exclusions
- get confirmation before broad scanning

## 2. Pre-scan
Inventory candidate roots before any move:
- file count
- directory count
- recursive size
- extension distribution
- obvious hot spots

Use `scripts/inventory_paths.py` for this step.

## 3. Candidate selection
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

## 4. Content sampling
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

## 5. Classification
Classify in this order:
1. choose the level-1 category
2. choose the subcategory
3. decide whether to move a whole folder or split individual files

Prefer folder-level moves when a directory is clearly single-theme.  
Prefer file-level moves when a folder is mixed or behaves like a download bucket.

## 6. Duplicate and conflict handling
Before applying duplicate actions, decide which mode is appropriate:
- rename only
- keep both with clearer names
- merge after review
- leave in `待人工复核`

Do not delete or overwrite duplicates without explicit user confirmation.

## 7. Renaming
Rename before moving.

Use Chinese names by default. Keep English only for:
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

## 8. High-risk confirmation gate
Ask the user before applying high-risk operations:
- large batch moves
- duplicate merge or overwrite decisions
- moving code projects or portable apps
- touching cloud-synced folders
- handling sensitive personal or financial files

Use a two-phase approach whenever practical:
1. preview
2. apply after confirmation

## 9. Logging
For every run, keep a CSV or markdown log with:
- source path
- destination path
- category
- confidence
- skipped reason

## 10. Safety gates
Stop and route to review when:
- a folder mixes work, research, personal, and finance files
- a file contains sensitive identity data
- a file is a contract or reimbursement original
- extraction fails and the filename is weak
- moving a folder could break an installed runtime or application

## 11. Completion checklist
Before closing a pass, verify:
- the user-confirmed scope was respected
- the scan roots were inventoried first
- chat attachment folders were handled only if included in scope
- cloud-synced roots were excluded unless explicitly included
- renaming happened before the move
- moved items have logs
- unresolved items are in `待人工复核`
- root clutter in Desktop or Downloads is reduced without breaking shortcuts or installed software
