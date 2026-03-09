---
name: hybrid-file-organizer
description: Organize user files with a hybrid workflow that combines path and size inventory with targeted content reading, Chinese renaming, and category-based moves. Use when the user asks to scan, sort, rename, archive, deduplicate, or clean personal files or folders, especially mixed document collections, chat attachment folders, download buckets, portable apps, code folders, or previously half-organized archives.
---

# Hybrid File Organizer

## Overview
Use this skill to organize user files safely with a fixed sequence: inventory first, read representative content second, classify with a predefined dictionary, then rename and move with Chinese-friendly names.  
Treat paths as signals, not verdicts. Use content to confirm classification before final moves.

## Workflow

### Step 1: Confirm the scope
Do not assume the scope. Use the user-provided scope as the source of truth.

If the user has not clearly defined the scope:
- propose a candidate scope
- state any important inclusions or exclusions
- ask for confirmation before scanning broadly

If the scope is broad, break it into batches such as:
- root folders
- chat attachment folders
- code or portable-app folders
- previously organized result folders
- cloud-synced folders

Exclude high-risk areas unless the user explicitly includes them:
- operating-system directories
- installed runtime or application directories
- cloud-sync roots
- cache-only directories

### Step 2: Inventory before reading content
Run `python scripts/inventory_paths.py <path>...` on candidate roots before making any classification decisions.

Use the inventory to capture:
- root file count
- root directory count
- recursive file count
- total size
- extension distribution
- large or unusual subdirectories

Use this data to decide which directories deserve content sampling. Do not classify solely from the path.

### Step 3: Sample content from candidate files
Read only enough content to make a reliable decision:
- `docx`: title, first sections, key headings, first table
- `pdf`: first page, first two pages, fallback to filename when extraction is poor
- `xlsx/csv/tsv`: sheet names, headers, first 10-20 rows
- code folders: `README`, config files, entry files, project structure
- portable apps: executable names, readme files, version markers, config directories

If `doc`, `pdf`, or `spreadsheet` skills are available in the session, use them for the content-reading step.

### Step 4: Classify with a fixed dictionary
Use [references/classification-dictionary.md](references/classification-dictionary.md) as the source of truth.

Apply these rules:
- path and size choose what to inspect
- content decides the category
- mixed or sensitive material goes to `manual-review`
- preserve project and folder integrity when a directory is clearly single-theme
- do not overfit categories to one machine, one drive, or one app

### Step 5: Rename in Chinese before moving
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
4. prefer Chinese names
5. only add `_1`, `_2` after content-based disambiguation fails

### Step 6: Move and log
Move only after classification and renaming are set.

Always record:
- source path
- destination path
- category
- confidence
- skipped reason if not moved

### Step 7: Add user confirmation at key decision points
Ask for confirmation when any of these applies:
- the scope was not explicitly defined by the user
- duplicate handling could delete, merge, or overwrite files
- a move would affect portable apps, code projects, runtimes, or cloud-synced folders
- the operation is large enough that rollback would be expensive
- sensitive material is present

Prefer a two-phase pattern for risky work:
1. inventory and preview
2. apply after confirmation

### Step 8: Stop automation when risk is high
Stop and switch to `manual-review` when:
- a folder mixes work, research, personal, and finance content
- files contain sensitive identity data, contracts, or reimbursement originals
- extraction fails and the filename is too weak to trust
- moving the directory could break an installed runtime or application
- collisions are too dense to resolve safely in one pass

## Trigger examples
Use this skill for prompts like:
- "Organize this set of folders"
- "Scan these attachment directories and classify them"
- "Rename and move mixed files based on file content"
- "Inventory paths and sizes first, then read content before classifying"
- "Review duplicates and confirm before risky moves"

## References
- Read [references/classification-dictionary.md](references/classification-dictionary.md) for categories, fixed scan roots, WeChat and Tencent rules, and confidence guidance.
- Read [references/operating-procedure.md](references/operating-procedure.md) for the full SOP, renaming rules, logging, and completion criteria.

## Script
- Run `python scripts/inventory_paths.py <path>...` to generate a compact inventory before doing any content reads or file moves.
