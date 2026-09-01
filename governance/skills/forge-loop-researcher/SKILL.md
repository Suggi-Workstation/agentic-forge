---
name: forge-loop-researcher
description: "Advance one Researcher stage in the Forge."
user-invocable: false
disable-model-invocation: false
---

# Forge Researcher Loop

The sole autonomous and interactive entrypoint for Researcher work in the
Forge. One invocation advances at most one Researcher-owned stage.

## Scope Gate -- HARD GATE

WHAT: keep every side effect inside the current agentic-forge git root.

HOW: resolve the root with `git rev-parse --show-toplevel`, resolve each
write target, and compare paths before every side effect. External web reads
and read-only `query-brain-vps` use are allowed.

PASS: artifact, status, log, lock, git index, and commit all belong to this
repo; no other repository, profile, skill library, or cron state changes.

HALT: scope cannot be proven, a target escapes the root, the starting tree
is dirty, or any procedure asks for a brain or investing-hub write.

POSITION: before every tool call or command with side effects.

## Eligibility

Researcher owns these cursor stages:

| State | Stage | Skill |
|:--|:--|:--|
| `ready` | `ideate` | `forge-ideate` |
| `active` | `propose` | `forge-propose` |
| `active` | `research` | `forge-research` |
| `active` | `build` | `forge-build` |

Every other state/stage is `NO-OP`: release the lock and exit without a
file, status, or log change. In particular, `awaiting-review`, `blocked`,
and Analyst ownership never produce Researcher work.

## Procedure

1. Resolve and verify the Forge root. Acquire the ignored local lease with
   `python3 scripts/forge-lock.py acquire --owner researcher
   --lease-seconds 7200 --root <root>`. Code 2 means another valid run owns
   it: return `NO-OP`.
2. Save the returned token. In a finally path, release only with that token.
   Send a heartbeat before and after a long research/tool batch.
3. Fetch remote refs read-only. Require `git status --porcelain` to be empty
   and `HEAD` to equal `origin/main`. Otherwise release and HALT without
   touching human work. Record starting HEAD and a hash of `STATUS.md`; the
   repository watcher does not honor this lease.
4. Read in order, in full unless a tail is specified:
   - `ANCHOR.md`, then `STATUS.md`;
   - `forge/protocol.md`, then `logbook/protocol.md`;
   - `LEARNINGS.md`;
   - tails of `logbook/progress.log` and `logbook/errors.log`;
   - every artifact in the active parent chain.
5. Re-check eligibility from the table. Confirm one active pipeline at most,
   every parent resolves, and no newer same-stage artifact already completed
   the action. A retry must be idempotent.
6. Invoke exactly one mapped stage skill. Before its first file write, fetch
   again and confirm `HEAD`, `origin/main`, and the status hash still equal
   the recorded values. If not, stop for a fresh run without writing. The
   stage returns one artifact or `NO-OP`; never invoke the next stage.
7. For a completed artifact, update the fixed fields in `STATUS.md` using the
   state machine. Reset `failure-count`. Derive the next per-file ENT ID from
   active plus newest archive and append one multiline `research` entry to
   `logbook/progress.log`: stage, gate result, artifact/pipeline IDs, and
   next owner/stage. Set `last-event` to `progress:ENT-NNN`.
8. Run `python3 scripts/validate-forge.py` and the relevant regression tests.
   Verify the diff contains only the new artifact, `STATUS.md`, progress log,
   and an admitted `LEARNINGS.md` change when applicable.
9. Fetch and recheck starting HEAD plus `origin/main`. If either moved,
   restore only this run's edits and stop for a fresh run. Otherwise stage
   those exact paths with `git add -- <paths>`. Never stage every changed
   path implicitly.
   Commit as `Researcher (Hermes Agent)` with a stage-specific message. Do
   not push; the VPS watcher publishes committed work.
10. Verify the commit exists and the worktree is clean. Release the lease and
    stop. One completed stage is the full run.

## Failure Transaction

If the stage or checks fail after the clean-start gate:

1. Remove only the new uncommitted artifact and restore only status/progress
   changes made by this run.
2. Derive the next `errors.log` ENT ID under the lease. Append one multiline
   `error` entry with symptom, root cause if known, safe recovery, and whether
   a structural fix exists. Set `last-event` to `errors:ENT-NNN`.
3. Increment `failure-count`; keep stage/owner unchanged. On the third
   consecutive identical root cause, set `state: blocked`.
4. Validate and commit only `STATUS.md` plus `logbook/errors.log`. If even
   that checkpoint cannot validate, restore those two run-local edits.
5. Release the lease and HALT. Never report the stage as complete.

## Verification -- HARD GATE

- [ ] Scope gate passed before every side effect. (PASS / HALT)
- [ ] Lease held by the Researcher token. (PASS / HALT)
- [ ] Starting tree was clean and role owned the cursor. (PASS / HALT)
- [ ] Zero or one stage advanced; no chained stage. (PASS / HALT)
- [ ] Artifact, status, and progress ENT block agree. (PASS / HALT)
- [ ] Validator and relevant tests pass. (PASS / HALT)
- [ ] Exact paths committed; no direct push; clean tree. (PASS / HALT)
- [ ] Lease released on every exit path. (PASS / HALT)

## Related

- `forge/protocol.md`
- `logbook/protocol.md`
- `scripts/forge-lock.py`
