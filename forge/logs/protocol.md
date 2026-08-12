---
name: forge-logbook-protocol
id: 20260812T171239Z
tier: protocol
author: Link
approved_by: Suggi
links:
  - forge/protocol.md
---
# Forge Logbook Protocol -- Forge Event Log Spec

## What the Forge Logbook Is

The Forge logbook is an append-only event log for the Forge pipeline.
It is the Forge-local analogue of the agentic-brain logbook, scoped
to one agent: Neo (pre-birth entries are authored by Link).

Entries are appended at the bottom, never edited or deleted. The Forge
loop reads the tails at the start of every iteration to catch up;
Suggi reads it to audit pipeline health.

| Log file | Purpose |
|:--|:--|
| `forge-queue.md` | Pipeline activity: loop runs, stage results, gate decisions, commits, publishes, stops |
| `forge-errors.md` | Bugs, scars, fixes, gate additions |
| `progress.log` | Compact machine-oriented gate record written by the Forge loop: PASS/HALT decisions, artifact ids, stage transitions, checker verdicts, publish results, stop reasons. Not a narrative log. |

## Entry Format

Each entry is a single block appended to the bottom of the file. No
editing, no deletion. Most recent entries are at the bottom.

```text
## [ENT-001] | 2026-08-12 17:12 UTC | Neo | general | ref: forge/ideas/example.md | see: 20260812T171240Z
Workstream one -- one major point per line.
Workstream two.
```

Entry bodies MUST use multiple short lines. Do NOT pack an entire loop
iteration onto one line. One major point or workstream per line. This
keeps log files scannable with `tail` and ensures the 500-line CI
archive threshold works correctly.

## Entry Schema

| Field | Required | Description |
|:--|:--|:--|
| `ENT-ID` | Yes | Sequential per file (ENT-001, ENT-002...). Never reused. Derived from the last entry in the file + 1. |
| Timestamp | Yes | ISO 8601 date + HH:MM UTC. Append-only = always increasing. |
| Agent | Yes | Neo (pre-birth: Link or Ava). |
| Category | Yes | `general` (forge-queue.md) or `error` (forge-errors.md). |
| ref: | Optional | Repo path this entry relates to, e.g. `ref: forge/ideas/<slug>.md`. |
| see: | Optional | Cross-reference to another entry (`see: ENT-003`) or an artifact id (`see: 20260812T171240Z`). |
| Body | Yes | What was done, what file changed, what was discovered. Multiline. |

## How to Write

0. Read this protocol before writing an entry.
1. Read the tail of the target log file to get the last ENT-ID counter.
2. Append the new entry at the bottom, incrementing the counter.
3. Commit and push. No waiting.

## How to Read (Catch-Up)

1. At loop start, read the tails of `forge-queue.md`, `forge-errors.md`,
   and `progress.log`.
2. Read entries since the last-seen point (STATUS.md `last-commit` and
   the loop's own cursor).
3. Update the cursor to the current UTC time.
4. No reply mechanism is needed -- the Forge is a single writer.

## Categories

| Category | Use for | File |
|:--|:--|:--|
| `general` | Loop runs, stage transitions, gate results, commits, publishes, stops | forge-queue.md |
| `error` | Bugs found, scars earned, gates added | forge-errors.md |

The `error` category is only used in `forge-errors.md`.

Note: the stage skills create durable artifacts in `forge/<stage>/`.
The logbook does NOT duplicate these. It records the activity of
writing them -- what was done, by whom, when. To read the artifact
itself, follow the `ref:` or `see:` link.

## Archiving

When a log file exceeds 500 lines, CI automatically archives the
oldest entries to keep loop reads fast and context lean.

The `forge-logbook-archive.yml` workflow (`.github/workflows/`) fires
on every push to main. It:

1. Checks `forge-queue.md` and `forge-errors.md` for line count > 500.
2. Cuts the oldest complete entries (never mid-entry) from the active file.
3. Appends them to `forge/logs/archive/<name>-<YYYY-MM-DD>.md`.
4. Commits with an `[archive]` tag so the workflow does not re-trigger itself.
5. The ENT-ID counter continues uninterrupted -- archived entries keep
   their original ENT-IDs for cross-reference integrity.

The Forge does NOT archive manually. Push log entries as normal; CI
trims them when they exceed the threshold. `progress.log` is small by
design (one line per gate event) and is not archived by CI.

## Compliance

- **ASCII-only:** all log entries and this protocol file are plain
  7-bit ASCII. CI enforces.
- **No self-modification:** this protocol file is authored by agents
  and approved by Suggi. Changes require a proposal.
- **No force-push:** append-only design precludes history rewriting.
- **Single writer:** the Forge loop is the only writer. Pre-birth
  bootstrap entries are authored by Link and stop at birth.
