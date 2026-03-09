# Tooling and Path Strategy

## 1. Principle
Do not start by writing code or choosing tools.

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

For each stage, prefer:
1. existing wheel
2. adapted wheel
3. custom script

## 2. Desktop shortcut audit
If a desktop-like root is in scope, audit shortcuts before moving files.

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

Possible wheels:
- Windows COM shell link APIs
- Python libraries that parse `.lnk`
- scripts that inventory shortcut targets before moves

## 3. Path-type handling

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
- audit executable, config, and data folders first
- move as a unit

### Runtime or install roots
Main risk:
- breaking environments or installed software

Preferred approach:
- exclude by default

## 4. Wheel selection guidance
Typical wheel categories:
- inventory or indexing tools
- shortcut parsing tools
- content extraction libraries for documents, PDFs, and spreadsheets
- duplicate analysis tools
- rename or archive automation tools

Selection criteria:
- stable on the current platform
- supports preview mode
- produces auditable output
- does not force destructive behavior
- can be wrapped or adapted if partially suitable

Write a custom script when:
- no existing tool covers the stage safely
- the tool cannot expose the data needed for review
- the workflow requires a repeatable house rule not supported by the tool

## 5. Future portability note
Current implementation may rely on Windows-specific tooling for shortcut auditing and path semantics.

To keep future Linux or macOS expansion possible:
- isolate OS-specific path handling
- keep category logic OS-agnostic
- describe path types by behavior, not only by product name
- prefer pluggable scripts over monolithic one-OS implementations
