---
name: forge-logbook-protocol
id: 20260812T173331Z
tier: protocol
author: Morpheus
approved_by: Suggi
links:
  - forge/protocol.md
---
# Forge Logbook Protocol

Both Forge logs use the same multiline ENT block format as the Brain.
Entries are append-only and counters are sequential per file.

## Files

| File | Purpose | Categories |
|:--|:--|:--|
| `progress.log` | stage results and handoffs | `research`, `review`, `general` |
| `errors.log` | failures, causes, and fixes | `error` |

## Format

```text
## [ENT-001] | 2026-09-01 19:47 UTC | <actual agent> | research | ref: forge/ideas/example-r01.md | see: 20260901T194700Z
Stage: ideate. Result: PASS.
Artifact: 20260901T194700Z.
Next: research.
```

Rules:

- Derive the next ENT ID from that file's active and archived entries.
- Use UTC and one major fact per short body line.
- Record the actual agent in the header; use stage names for handoffs.
- Put one blank line before every entry header.
- Never edit, delete, or renumber an old entry.
- Do not write no-op entries.
- `ref:` paths are repository-relative; `see:` is an ENT or artifact ID.

## Session Use

1. Read this protocol and the tails of both active logs.
2. Append one progress entry after a completed stage, evidence-gap handoff,
   meaningful time-budget checkpoint, or explicitly directed human decision
   under `forge/protocol.md`. Do not describe an unfinished stage as complete.
3. Append one errors entry only when a real failure occurred.
4. Commit the entry with the stage transaction.

The future loop stagger assumes non-overlapping sessions, not guaranteed
mutual exclusion. Unexpected concurrent edits require a halt. No file lock
is part of this blueprint.

## Archiving

`scripts/logbook-archive.py`, invoked by
`.github/workflows/logbook-archive.yml`, owns the line limits and retention.
It moves complete oldest ENT blocks to
`logbook/archive/<name>-<YYYY-MM-DD>.log`. Enumerate archived `progress-*.log`
files when checking human decisions; do not assume monthly subdirectories.
ENT IDs never reset.