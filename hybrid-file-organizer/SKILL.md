---
name: hybrid-file-organizer
description: Organize user files with a hybrid workflow that combines path and size inventory with targeted content reading, Chinese renaming, category-based moves, duplicate review, and high-risk confirmation gates. Use when the user asks to scan, sort, rename, archive, deduplicate, or clean personal files or folders, especially mixed document collections, chat attachment folders, download buckets, portable apps, code folders, desktop-like roots, or previously half-organized archives.
---

# Hybrid File Organizer

## Overview
Use this skill to organize user files safely with a fixed sequence: confirm scope, define stages, audit risky path types, inventory first, read representative content second, classify with a predefined dictionary, then rename and move with Chinese-friendly names.  
Treat paths as signals, not verdicts. Use content to confirm classification before final moves.

## Workflow

### Step 1: Confirm the scope
Do not assume the scope. Use the user-provided scope as the source of truth.

If the user has not clearly defined the scope:
- propose a candidate scope
- state important inclusions or exclusions
- ask for confirmation before scanning broadly

If the scope is broad, break it into batches such as:
- root folders
- chat attachment folders
- code or portable-app folders
- previously organized result folders
- cloud-synced folders

Do not silently narrow execution from the user-stated scope to a smaller "safe subset" and then apply moves.
If you believe only a subset is safe to act on now:
- inventory the broader scope
- propose the exact subset you want to execute
- ask for confirmation before any move or rename in that subset

Exclude high-risk areas unless the user explicitly includes them:
- operating-system directories
- installed runtime or application directories
- cloud-sync roots
- cache-only directories

### Step 2: Design the execution plan before choosing tools
Break the job into explicit stages before selecting any wheel or script.

Use [references/tooling-and-path-strategy.md](references/tooling-and-path-strategy.md) to decide:
- which stages need only inventory
- which stages need content reading
- which stages need shortcut auditing
- which stages can use an existing tool
- which stages need a custom script or a modified tool

Default bundled tooling in this skill:
- `python scripts/inventory_paths.py` for inventory
- `powershell -ExecutionPolicy Bypass -File scripts/audit_shortcuts.ps1` for desktop shortcut audit
- `python scripts/find_duplicate_candidates.py` for duplicate preview

Before the first move, explicitly decide and state the destination layout:
- organize in place
- move into an existing result root
- create a new result root

If the destination layout introduces a new top-level bucket or materially changes the directory shape, preview it and get confirmation before moving files.

Optional external wheels already curated in this skill:
- `Everything` for fast interactive inventory and triage on Windows
- `File Juggler` for stable content-based inbox automation on Windows
- `DropIt` for stable rule-based move or rename pipelines on Windows
- `pylnk3` or `LnkParse3` only when deeper `.lnk` parsing is needed beyond the bundled shortcut audit

### Step 3: Inventory before reading content
Run `python scripts/inventory_paths.py <path>...` on candidate roots before making any classification decisions.

Use the inventory to capture:
- root file count
- root directory count
- recursive file count
- total size
- extension distribution
- large or unusual subdirectories

Use this data to decide which directories deserve content sampling. Do not classify solely from the path.

### Step 4: Audit special path types before moves
Use [references/tooling-and-path-strategy.md](references/tooling-and-path-strategy.md) for path-type handling.

Special attention is required for:
- desktop-like roots with `.lnk` or `.url` files
- cloud-synced roots
- chat attachment roots
- code project roots
- portable app roots
- runtime or install roots

If a desktop-like root is in scope:
- inventory `.lnk` and `.url` files first
- run `powershell -ExecutionPolicy Bypass -File scripts/audit_shortcuts.ps1 -Roots <desktop-root> -MoveScopeRoots <planned-move-roots>`
- identify whether their targets live inside the planned move scope
- avoid moving targets until the shortcut impact is understood
- keep shortcuts themselves in place unless the user explicitly asks otherwise

### Step 5: Sample content from candidate files
Read only enough content to make a reliable decision:
- `docx`: title, first sections, key headings, first table
- `pdf`: first page, first two pages, fallback to filename when extraction is poor
- `xlsx/csv/tsv`: sheet names, headers, first 10-20 rows
- code folders: `README`, config files, entry files, project structure
- portable apps: executable names, readme files, version markers, config directories

If `doc`, `pdf`, or `spreadsheet` skills are available in the session, use them for the content-reading step.

Do not invent a more specific semantic rename than the evidence supports.
If a rename introduces a subject, unit, or theme that is not already obvious from strong folder context or sampled content, sample content first.
Only use filename-only evidence for clearly non-sensitive, high-confidence cases such as obvious media series folders or disposable download-package names.

### Step 6: Classify with a fixed dictionary
Use [references/classification-dictionary.md](references/classification-dictionary.md) as the source of truth.

Apply these rules:
- path and size choose what to inspect
- content decides the category
- mixed or sensitive material goes to `manual-review`
- preserve project and folder integrity when a directory is clearly single-theme
- do not overfit categories to one machine, one drive, or one app

### Step 7: Rename before moving
Use [references/operating-procedure.md](references/operating-procedure.md) for naming rules.

Default naming pattern:
- `subject`
- `subject_date`
- `subject_org`
- `subject_phase`
- `subject_version`

Rename with these priorities:
1. extract the real subject
2. add date, unit, phase, or version if it reduces ambiguity
3. remove download noise, hashes, repeated brackets, and meaningless numbers
4. prefer Chinese-friendly names when the user wants Chinese naming
5. only add `_1`, `_2` after content-based disambiguation fails

### Step 8: Move and log
Move only after classification and renaming are set.

Always record:
- source path
- destination path
- category
- confidence
- skipped reason if not moved

If this is only a preview pass, inventory pass, or low-risk pilot batch, label it exactly that way.
Do not describe a limited pilot as if the requested scope has already been organized.

### Step 9: Add user confirmation at key decision points
Ask for confirmation when any of these applies:
- the scope was not explicitly defined by the user
- you want to execute only one batch or one safe subset from a broader user-confirmed scope
- you want to introduce a new result root or a new top-level destination layout
- duplicate handling could delete, merge, or overwrite files
- a move would affect portable apps, code projects, runtimes, or cloud-synced folders
- a move would affect the target of a desktop shortcut
- the operation is large enough that rollback would be expensive
- sensitive material is present

Prefer a two-phase pattern for risky work:
1. inventory and preview
2. apply after confirmation

### Step 10: Stop automation when risk is high
Stop and switch to `manual-review` when:
- a folder mixes work, research, personal, and finance content
- files contain sensitive identity data, contracts, or reimbursement originals
- extraction fails and the filename is too weak to trust
- moving the directory could break an installed runtime or application
- moving a target would likely break or orphan an existing shortcut
- collisions are too dense to resolve safely in one pass

## Execution contract
- Inventory may cover a broader scope than the current apply batch, but apply scope must be explicitly stated.
- A batch is not "done" unless its apply scope matches what was confirmed with the user.
- If you only completed a pilot batch, say "pilot batch" or "preview batch" in the final answer.
- Do not claim the skill was fully followed if content sampling, confirmation gates, or destination-layout confirmation were skipped.

## Trigger examples
Use this skill for prompts like:
- "Organize this set of folders"
- "Scan these attachment directories and classify them"
- "Rename and move mixed files based on file content"
- "Inventory paths and sizes first, then read content before classifying"
- "Review duplicates and confirm before risky moves"
- "Audit desktop shortcuts before reorganizing files"

## References
- Read [references/classification-dictionary.md](references/classification-dictionary.md) for categories, special path types, chat attachment rules, and confidence guidance.
- Read [references/operating-procedure.md](references/operating-procedure.md) for the full SOP, renaming rules, logging, duplicate handling, and completion criteria.
- Read [references/tooling-and-path-strategy.md](references/tooling-and-path-strategy.md) for shortcut auditing, wheel selection, and future cross-platform extension notes.

## Script
- Run `python scripts/inventory_paths.py <path>...` to generate a compact inventory before doing any content reads or file moves.
- Run `powershell -ExecutionPolicy Bypass -File scripts/audit_shortcuts.ps1 -Roots <path> -MoveScopeRoots <path>...` to audit `.lnk` and `.url` dependencies before moving targets.
- Run `python scripts/find_duplicate_candidates.py <path>...` to preview duplicate candidates before any merge, overwrite, or delete decision.
