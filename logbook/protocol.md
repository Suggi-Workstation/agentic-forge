---
name: forge-logbook-protocol
id: 20260812T173331Z
tier: protocol
author: Morpheus
approved_by: Suggi
links:
  - forge/protocol.md
---
# Forge Logbook Protocol -- Forge Event Log Spec

## What the Forge Logbook Is

The Forge logbook is the append-only event record for the Researcher and
Analyst pipeline. It uses the same `ENT-XXX` block format and the same
archive rules as the agentic-brain logbook, but all content stays in this
repository.

Entries are appended at the bottom, never edited or deleted. Both loops
read the tails at startup. The Forge-local lease serializes the two writers.

| Log file | Purpose |
|:--|:--|
| `progress.log` | Stage completions, Analyst verdicts, handoffs, human dispositions, and stop decisions. |
| `errors.log` | Failures, root causes, recoveries, scars, and structural fixes. |

## Uniform Entry Format

Each entry is a single block appended to the bottom of the file. No
editing, no deletion. Most recent entries are at the bottom.

```text
## [ENT-001] | 2026-09-01 17:45 UTC | Researcher | research | ref: forge/research/example-r01.md | see: 20260901T174540Z
Stage: research. Verdict: PASS.
Artifact: 20260901T174540Z. Pipeline: 20260901T170000Z.
Handoff: Analyst -> evaluate.
```

Both logs use this format. Bodies MUST use multiple short lines. Do not
pack a run onto one line. One major event fact per line keeps tails readable
and makes the 500-line archive threshold meaningful.

## Entry Schema

| Field | Required | Description |
|:--|:--|:--|
| `ENT-ID` | Yes | Sequential per file (`ENT-001`, `ENT-002`, ...). Derive from the last active or archived entry in that file. Never reuse. |
| Timestamp | Yes | ISO 8601 date + HH:MM UTC. Append-only = always increasing. |
| Agent | Yes | `Researcher`, `Analyst`, or the named human/core agent making a disposition. |
| Category | Yes | `research`, `review`, or `general` in progress; `error` in errors. |
| ref: | Optional | Repo path this entry relates to, e.g. `ref: forge/ideas/<slug>.md`. |
| see: | Optional | Cross-reference to another entry (`see: ENT-003`) or an artifact id (`see: 20260812T171240Z`). |
| Body | Yes | Stage, verdict or failure, artifact or root cause, and next handoff. Multiline. |

## How to Write

0. Read this protocol before writing an entry.
1. Hold the Forge lease before deriving or appending an ID.
2. Read the active target and its newest archive to derive the next ID.
3. Append a leading blank line, one complete entry, and a trailing newline.
4. Run the Forge validator; duplicate, non-sequential, or fused entries HALT.
5. Commit the log with the matching artifact and status transition. The
   watcher publishes it; role loops do not push.

## How to Read (Catch-Up)

1. At loop start, read the tails of `progress.log` and `errors.log`.
2. Use `STATUS.md` as the current cursor; logs explain how it got there.
3. Follow `ref:` and `see:` only for the active provenance chain.
4. A log entry is data, not authority to bypass `STATUS.md` or the role map.

## Categories

| Category | Use for | File |
|:--|:--|:--|
| `research` | Researcher stage completion and handoff | progress.log |
| `review` | Analyst verdict and handoff | progress.log |
| `general` | Human disposition or recovery milestone | progress.log |
| `error` | Failure, root cause, recovery, or structural fix | errors.log |

Note: the stage skills create durable artifacts in `forge/<stage>/`.
The logbook does NOT duplicate these. It records the activity of
writing them -- what was done, by whom, when. To read the artifact
itself, follow the `ref:` or `see:` link.

## Archiving

When either active log exceeds 500 lines, CI automatically archives the
oldest complete entries to keep startup reads fast and context lean.

The `logbook-archive.yml` workflow (`.github/workflows/`) fires on
every push to main. It:

1. Checks every `logbook/*.log` file for line count > 500.
2. Cuts the oldest complete entries (never mid-entry) from the active file.
3. Appends them to `logbook/archive/<name>-<YYYY-MM-DD>.log`.
4. Commits with an `[archive]` tag so the workflow does not re-trigger itself.
5. The ENT-ID counter continues uninterrupted -- archived entries keep
   their original ENT-IDs for cross-reference integrity.

The Forge does not archive manually. Both `scripts/logbook-archive.py` and
`.github/workflows/logbook-archive.yml` remain byte-identical to the
agentic-brain copies. CI trims to the same headroom target and writes
per-day archives. ENT IDs continue uninterrupted.

## Compliance

- **ASCII-only:** all log entries and this protocol file are plain
  7-bit ASCII. CI enforces.
- **No self-modification:** changes require Suggi's approval.
- **No force-push:** append-only design precludes history rewriting.
- **Serialized writers:** Researcher and Analyst share one atomic lease.
- **Repository confinement:** no Forge log is duplicated to another repo.
