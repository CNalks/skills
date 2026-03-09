# Operating Procedure

## 1. Scope confirmation
Confirm the exact scope before scanning or moving.

If the user did not define it precisely:
- propose a concrete scope
- call out risky inclusions and exclusions
- get confirmation before broad scanning

If the user did define a broad scope, do not silently replace it with a narrower execution subset.
If you want to act on only one safer batch first:
- say which broader scope was requested
- say which exact batch you propose to apply now
- get confirmation before renaming or moving anything in that batch

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

Before the apply stage, define the destination strategy:
- in-place reorganization
- move into an existing result root
- create a new result root

If the strategy adds a new top-level directory or otherwise changes the visible layout of the scoped area, preview it and confirm it first.

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

Do not assign a semantic title that outruns the evidence.
If a proposed Chinese rename adds subject matter, organization, course name, or project theme beyond what is already explicit in the source path, validate it with content sampling or strong folder context first.
Filename-only renaming is acceptable only for high-confidence, low-sensitivity cases such as obvious media releases, software packages, or archive bundles whose topic is already explicit.

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
- executing only a subset from a broader confirmed scope
- introducing a new result root or top-level destination bucket
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
- any narrower apply batch was explicitly confirmed
- the stage plan was defined before selecting tools
- the destination strategy was stated before the first move
- any new top-level result root was previewed and confirmed
- the scan roots were inventoried first
- chat attachment folders were handled only if included in scope
- cloud-synced roots were excluded unless explicitly included
- shortcut targets were audited if desktop-like roots were included
- semantic renames were supported by content evidence or strong folder context
- renaming happened before the move
- moved items have logs
- unresolved items are in `manual-review`
- root clutter in desktop-like or download-like roots is reduced without breaking shortcuts or installed software

## 15. Reporting discipline
Describe the run precisely:
- say "inventory only" if no moves happened
- say "pilot batch" or "preview batch" if only a small confirmed subset was applied
- do not say the requested scope was "organized" when only one subset was handled
