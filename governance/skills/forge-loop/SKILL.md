---
name: forge-loop
description: "Orchestrate one bounded Forge iteration: lock, read anchor and status, run exactly one stage, verify, checkpoint, publish, stop. Neo's complete session lifecycle."
user-invocable: false
disable-model-invocation: false
---

# Forge Loop -- Session Lifecycle

## What This Skill Does

Runs exactly one bounded Forge iteration. It replaces the fleet
preflight and session-end workflow for Neo: each invocation reads the
checkpoint, advances the pipeline by exactly one stage, verifies,
publishes, and stops. A fresh invocation resumes from the repository
alone.

## Hard Gate -- PASS or HALT

Every step below MUST pass before the iteration proceeds. HALT on any
failure, record the stop reason, and stop. Do not skip steps.

## When to Invoke

- Every scheduled or manual Neo run.
- After a crash, to resume from the repository checkpoint.

## Preconditions

- Repo: `/srv/forge/agentic-forge` (VPS-resident working copy).
- Git identity: Neo's identity (pre-birth: Link).
- `ANCHOR.md` present and human-approved.

## Procedure

### 1. Acquire the single-writer lock

Lock file: `/srv/forge/agentic-forge.lock` (outside the repository).

- If absent, create it: owner, process id, UTC start time.
- If present and live (process exists, younger than 24h): stop.
- If present and stale: record owner, age, and recovery note in
  `errors.log`, then reclaim.

### 2. Read ANCHOR.md

Confirm the current objective. If missing, ambiguous, or unrelated to
the active pipeline: HALT.

### 3. Read the checkpoint

Read `STATUS.md`, the tail of `JOURNAL.md`, the tail of
`forge/logbook/progress.log`, and `LEARNINGS.md`. One canonical
cursor: `STATUS.md`. Do not duplicate its fields anywhere else.

### 4. Verify repository state

- Local HEAD equals `origin/main`.
- Working tree clean (no unrelated dirty changes).
- Active parent chain resolves (each artifact's `parent:` id exists).

### 5. Discover exactly one next stage

- Active pipeline: advance that pipeline only.
- No active pipeline: invoke `forge-ideate`.
- Conflicting pipelines vs STATUS: HALT. Never create a second active
  pipeline because the first is difficult.

### 6. Run the Feynman loop

Invoke `forge-loop-feynman` before any substantive work.

### 7. Invoke exactly one stage skill

The stage skill reads its parent, reads its template, generates the
exact UTC id, writes the artifact, applies its gate, and records PASS
or HALT.

### 8. Run structural checks

Frontmatter, required sections, correct directory, parent, status,
confidence, ASCII-only content, no secrets, no unrelated staged files.

### 9. Commit the provisional checkpoint

Commit the stage artifact and the updated `STATUS.md`. The repository
is now recoverable even if verification or the process fails.

### 10. Invoke forge-verify

Prefer a separate checker: different model, isolated workspace, zero
author context, reads the committed artifact cold. Fallback is a
degraded cold read -- label it `degraded-cold-read`. The verdict is
APPROVE, FLAG, or REJECT.

### 11. Act on the verdict

- APPROVE: append the verification record, update `STATUS.md` and
  `JOURNAL.md`, publish.
- FLAG: record required corrections, do not advance.
- REJECT: mark the artifact halted or returned per the stage rule.
- Missing verification: state `verification: pending`. Never treat a
  timeout as approval.

### 12. Publish and confirm

Push to origin. Confirm the remote commit. `publish-pending` is a real
state, not success. Do not start a new artifact while a checkpoint is
unpublished.

### 13. Release and stop

Release the lock. Append to `progress.log` (gate events) and to
`errors.log` if scars were earned. Stop after one stage. The next
iteration starts fresh from the repository.

## Stop Conditions

Stop and record the reason when any of these hold:

- A stage gate returns HALT.
- The verifier returns unresolved FLAG or REJECT.
- The time or iteration budget is exhausted.
- No new evidence, artifact, or commit appears within the idle limit.
- The same failure repeats beyond the retry limit.
- ANCHOR is missing, ambiguous, or unrelated to the active pipeline.
- The repository has unrelated dirty changes.
- Required sources or tools are unavailable.
- A credential, destructive operation, or governance change requires
  human approval.
- The repository cannot be published and the state is not safely
  recoverable.

A stop is a successful safety outcome. Record it in `STATUS.md`,
`JOURNAL.md`, and `progress.log`, then wait.

## Recovery

- STATUS `active` + artifact commit exists: resume the named next stage.
- STATUS `verification-pending`: rerun or retrieve verification; never
  create a duplicate artifact.
- STATUS `publish-pending`: verify origin before any new work.
- Uncommitted artifact: inspect against STATUS; complete the intended
  checkpoint or discard only the uncommitted duplicate.
- Missing parent: HALT and repair provenance.
- Checker flagged an artifact: next action is correction, not advance.
- Stale lock: record recovery before reclaiming.
- Same error beyond retry threshold: stop and surface it.

The loop is idempotent. A retry never creates a second idea for the
same status, re-runs an irreversible external action without a record,
or resets confidence without explanation.

## Pitfalls

- **One stage per iteration.** Two stages per run breaks the
  checkpoint discipline and the verifier's cold read.
- **Never self-certify.** The author's final check is not
  verification. Label degraded cold reads explicitly.
- **Never silently resume.** If STATUS and the repository disagree,
  HALT and surface the conflict.
- **Publication policy.** The Forge loop pushes the Forge repository
  directly. The brain repository is watcher-pushed. Do not conflate
  the two.
- **Lock is outside git.** The lock file must never be committed.

## Related

- `forge-loop-feynman` -- the thinking loop run inside every stage.
- `forge-verify` -- maker-checker orchestration.
- `forge/protocol.md` -- pipeline specification.
- `forge/logbook/protocol.md` -- log spec.
