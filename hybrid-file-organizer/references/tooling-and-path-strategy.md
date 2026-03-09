# Tooling and Path Strategy

## 1. Default execution stack
This skill should not defer tool selection to a future run. The default stack is:

| Stage | Default tool in this skill | Optional external wheel | Notes |
| --- | --- | --- | --- |
| Inventory | `scripts/inventory_paths.py` | `Everything` | Use the bundled script for reproducible summaries. Use Everything for fast interactive triage on Windows. |
| Desktop shortcut audit | `scripts/audit_shortcuts.ps1` | `pylnk3`, `LnkParse3` | Use the bundled PowerShell script by default. Use Python `.lnk` parsers only when deeper shortcut metadata is needed. |
| Content sampling | Session skills: `doc`, `pdf`, `spreadsheet` | none required | Use built-in extraction workflows before introducing more tools. |
| Duplicate preview | `scripts/find_duplicate_candidates.py` | `Everything` dupe functions | Use the bundled script for hash-backed candidate groups. Everything duplicate functions are only rough guides. |
| Rule-based inbox automation | none by default | `File Juggler`, `DropIt` | Use only when the user wants long-lived automation for stable Windows inbox folders. |
| Final move and rename | Built from the task-specific workflow | `DropIt` for simple rule-only cases | Do not default to external automation for mixed high-risk collections. |

## 2. Stage-first decision rule
Start by defining the execution stages:
1. scope confirmation
2. inventory
3. special path audit
4. content sampling
5. classification
6. duplicate handling
7. renaming
8. moving
9. logging

Then choose tools in this order:
1. bundled script or built-in skill
2. curated external wheel already listed in this file
3. adapted external wheel
4. custom script only when the gap is real

## 3. Desktop shortcut audit
If a desktop-like root is in scope, audit shortcuts before moving files.

Default tool:
- `scripts/audit_shortcuts.ps1`

Audit targets:
- `.lnk`
- `.url`

Questions to answer:
- does the shortcut target live inside the planned move scope
- is the shortcut pointing to a portable app, code project, synced folder, or install directory
- would the move break user launch habits or app startup flows

Default behavior:
- keep shortcut files in place
- do not move targets blindly
- preview affected shortcuts and ask for confirmation

Use `pylnk3` or `LnkParse3` only when:
- the PowerShell shell-link resolver cannot extract enough metadata
- there is a need to inspect lower-level `.lnk` internals

## 4. Duplicate handling
Default tool:
- `scripts/find_duplicate_candidates.py`

Use it to:
- group same-size files first
- compute hashes only where size collisions exist
- preview duplicate groups before any destructive action

Use Everything duplicate functions only as a fast discovery layer. The official docs note they do not compare file contents, so they are guides, not final evidence.

## 5. External wheels already curated

### Everything
Use for:
- fast filename or path inventory
- triage by path, extension, modified time, or size
- rough duplicate discovery on Windows

Do not use as the final duplicate authority because its duplicate helpers are not content-hash based.

References:
- https://www.voidtools.com/support/everything/searching/

### File Juggler
Use for:
- stable Windows inbox directories
- content-based move or rename rules
- repeatable long-running automation after the workflow has been proven manually

Do not use as the first-line tool for mixed high-risk archives that still need human review.

References:
- https://www.filejuggler.com/organize-documents-by-their-content/

### DropIt
Use for:
- stable Windows rule-based move or rename pipelines
- simple folder-to-folder automation
- fixed archive or extract actions

Do not use as the main engine for high-risk semantic classification.

References:
- https://www.dropitproject.com/

### pylnk3
Use for:
- reading and writing `.lnk` files in Python
- deeper shortcut parsing than the bundled audit script

References:
- https://pypi.org/project/pylnk3/

### LnkParse3
Use for:
- lower-level `.lnk` parsing or forensic-style inspection

References:
- https://pypi.org/project/LnkParse3/

## 6. Path-type handling

### Desktop-like roots
Main risk:
- shortcut dependency breakage

Preferred approach:
- audit first
- file-level cleanup second

### Cloud-sync roots
Main risk:
- sync churn
- path instability
- remote deletion side effects

Preferred approach:
- explicit confirmation
- preserve structure
- avoid cross-boundary moves without preview

### Chat attachment roots
Main risk:
- mixing real attachments with caches

Preferred approach:
- prioritize received-file or attachment directories
- de-prioritize image pools and cache folders

### Code project roots
Main risk:
- breaking relative paths or project integrity

Preferred approach:
- move whole project folders when classification is clear
- avoid flattening

### Portable app roots
Main risk:
- breaking launchers, config, or user data paths

Preferred approach:
- audit executable, config, data folders, and shortcut targets first
- move as a unit

### Runtime or install roots
Main risk:
- breaking environments or installed software

Preferred approach:
- exclude by default

## 7. Future portability note
Current implementation is Windows-first because shortcut auditing relies on Windows shell behavior and common Windows file-organization tools.

To keep future Linux or macOS expansion possible:
- isolate OS-specific path handling
- keep category logic OS-agnostic
- describe path types by behavior, not only by product name
- prefer pluggable scripts over monolithic one-OS implementations
