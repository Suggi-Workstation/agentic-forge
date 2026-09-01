---
name: forge-protocol
id: 20260801T000008Z
tier: protocol
author: Morpheus
approved_by: Suggi
version: 2.0
---

# Forge Protocol -- Research-to-Build Pipeline

## What the Forge Is

The Forge is a six-stage, two-role pipeline. Researcher creates and
synthesizes. Analyst independently challenges evidence and verifies the
final package. Every stage produces an immutable artifact. The final output
is a build package for human review, not an autonomous implementation.

## Pipeline

```
IDEATE -> PROPOSE -> RESEARCH -> EVALUATE -> BUILD -> VERIFY -> REVIEW
   R         R           R           A         R        A        H
```

| Stage | Owner | Folder | Gate |
|:--|:--|:--|:--|
| 1. Ideate | Researcher | `forge/ideas/` | Important, non-duplicate, path-aligned, falsifiable? |
| 2. Propose | Researcher | `forge/proposals/` | Evidence plan complete, feasible, and falsifiable? |
| 3. Research | Researcher | `forge/research/` | Plan executed; claims and contradictions sourced? |
| 4. Evaluate | Analyst | `forge/evaluations/` | Evidence sufficient for a build? |
| 5. Build | Researcher | `forge/builds/` | Review package actionable, testable, and bounded? |
| 6. Verify | Analyst | `forge/verifications/` | Claims traceable and implementation design safe? |

## Folder Map

```
forge/
  protocol.md
  ideas/
  proposals/
  research/
  evaluations/
  builds/
  verifications/
  graveyard/
  archive/
```

## Entry Format

Every stage artifact uses this frontmatter schema:

```yaml
---
name: <lowercase kebab-case slug>
id: <YYYYMMDDTHHMMSSZ generated from current UTC>
pipeline: <idea artifact id>
research_path: agent-systems|value-investing-systems
stage: idea|proposal|research|evaluation|build|verification|graveyard
owner: Researcher|Analyst
status: complete
parent: <immediate parent artifact id or root>
supersedes: <prior same-stage artifact id or none>
confidence: 0.0-1.0
created: <YYYY-MM-DDTHH:MM:SSZ>
---
```

The `pipeline` value is the first idea's `id`. `parent` points to the
artifact directly consumed by this artifact. A correction never edits old
content; it creates `<slug>-rNN.md` and names the old same-stage ID in
`supersedes`.

`r01` is the first artifact for that pipeline, stage, and slug. A revision
derives the next number from existing same-stage files and supersedes the
immediately prior revision. Numbers are never guessed, reused, or skipped.

## Stage Artifact Contracts

The canonical template in each stage skill is authoritative for body shape.
The minimum semantic contract is:

| Stage | Artifact must prove |
|:--|:--|
| Idea | path choice, non-duplication check, falsifiable question, expected build, kill criteria |
| Proposal | claim map, source strategy, method, counter-hypotheses, acceptance tests, stop conditions |
| Research | method execution, claim-level citations, source quality, contradictory evidence, unresolved gaps |
| Evaluation | independent claim audit, coverage, contradiction handling, feasibility, explicit verdict and return stage |
| Build | recommendation, evidence trace, design, implementation sequence, tests, risks, rollback, open questions |
| Verification | claim traceability, design consistency, test adequacy, confinement, risks, explicit verdict and return stage |

An artifact that merely describes intended future work cannot satisfy the
research or build contract. Citations must point to sources actually read.
Brain results are leads; the cited brain file or primary source must be
read before a claim is used.

## Rejection and the Graveyard (`graveyard/`)

An Analyst `HALT-REJECT` evaluation or verification is the pipeline's
canonical immutable post-mortem and includes:

```
## What Was Rejected
## Failed Gate and Evidence
## Root Cause
## Reuse or Revival Conditions
## Provenance Chain
```

No second artifact is created during that gate. `forge/graveyard/` is
reserved for a later human disposition summary when Suggi wants one.
Rejection is not a learning by itself; `LEARNINGS.md` requires repeated
cross-pipeline evidence.

## State Machine

`STATUS.md` is the only current cursor. Valid states are `ready`, `active`,
`awaiting-review`, and `blocked`.

| Current stage | Owner | PASS next stage | HALT disposition |
|:--|:--|:--|:--|
| `ideate` | Researcher | `propose` / Researcher | no worthwhile idea -> no-op |
| `propose` | Researcher | `research` / Researcher | operational failure -> retry or blocked |
| `research` | Researcher | `evaluate` / Analyst | operational failure -> retry or blocked |
| `evaluate` | Analyst | `build` / Researcher | revise proposal/research or reject |
| `build` | Researcher | `verify` / Analyst | operational failure -> retry or blocked |
| `verify` | Analyst | `awaiting-review` / Human | revise build/research or reject |

Researcher stages emit only their own structural output result: PASS when
the stage artifact is complete, or operational HALT when it cannot be
written honestly. Only the Analyst accepts, revises, or rejects research and
build claims. Analyst verdicts are:

- `PASS`: advance as shown.
- `HALT-REVISE`: set `stage` and `owner` to the named return point,
  increment `revision`, and preserve every old artifact.
- `HALT-REJECT`: the verdict artifact serves as the post-mortem; reset to
  `ready` only after that artifact and rejection transition commit together.

If the same acceptance criterion fails twice in succession, another
unchanged retry is forbidden. Return to `propose` with a different method
or reject the pipeline.

Operational failures are not research verdicts. Keep the same stage and
owner, increment `failure-count`, and append an error entry. Three
consecutive failures with the same root cause set `state: blocked`; only a
human may clear it. A successful stage resets `failure-count` to zero.

## One-Build-at-a-Time Review Gate

After verification PASS, set `state: awaiting-review`, `stage: review`, and
`owner: Human`. Both role loops then exit without writes. Suggi may:

- approve: keep the build and verification, then reset all active cursor
  fields to the `ready` schema;
- request revision: keep the verification as `active-artifact`, name the
  return stage and owner, increment `revision`, and set `state: active`;
- reject: retain the rejection verdict as the canonical post-mortem, then
  reset all active cursor fields to the `ready` schema;
- implement elsewhere: a separate human-authorized workflow, never a Forge
  cron action.

Every human disposition updates `STATUS.md` and appends one multiline
`general` ENT entry to `logbook/progress.log` in the same commit. Approval
or rejection is therefore durable evidence for future learning admission.
`last-event` records that entry as `progress:ENT-NNN`.

## Start-of-Run Context

Both loops read, in order:

1. `ANCHOR.md` and `STATUS.md` in full;
2. this protocol and `logbook/protocol.md` in full;
3. `LEARNINGS.md` in full;
4. tails of both active log files; and
5. the active artifact chain named by status.

Do not load all completed pipelines. Hot context is bounded by the active
chain, curated learnings, and CI-bounded log tails.

## Atomic Stage Transaction

Every eligible run:

1. Resolve the git root and prove every intended write is inside it.
2. Acquire `scripts/forge-lock.py`; a held lock is a no-op.
3. Fetch remote refs read-only. HALT without writes unless the tree is clean
   and `HEAD` equals `origin/main`. Record that HEAD and a hash of
   `STATUS.md`; the watcher does not share the Forge lease.
4. Read startup context and confirm role ownership.
5. Run exactly one stage skill. Immediately before its first write, fetch
   again and confirm `HEAD`, `origin/main`, and the status hash still match
   the start. Otherwise discard only run-local scratch reasoning and stop for
   a fresh run.
6. Write at most one stage artifact. Run `scripts/validate-forge.py` and
   relevant tests.
7. Update `STATUS.md` and append one complete progress `ENT-XXX` block.
8. On a failure, append one complete errors `ENT-XXX` block and apply the
   failure transition instead of pretending success.
9. Fetch and recheck starting HEAD plus `origin/main` before staging and
   commit. If either moved, restore only this run's file edits and retry in a
   fresh run. Otherwise stage exact paths, commit as the active role, and
   verify a clean tree.
10. Release the lock in all exit paths. The VPS watcher publishes commits;
    role loops never push directly.

If any write fails before commit, restore only files created or changed by
that run, release the lock, and leave a clean tree. Never discard
pre-existing human changes.

## Provenance

Every artifact's `parent` field creates a chain:

```
verifications/<slug>-r01.md
  parent: builds/<slug>-r01.md
    parent: evaluations/<slug>-r01.md
      parent: research/<slug>-r01.md
        parent: proposals/<slug>-r01.md
          parent: ideas/<slug>-r01.md
```

The chain, `STATUS.md`, and corresponding progress entries must agree. Any
disagreement is a validator HALT, not a judgment call.
