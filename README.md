# Agentic Forge

Two-agent research and verification for reviewable agent-system and
value-investing improvements.

## What This Repo Is

A repository-confined workflow for one Researcher and one Analyst. The
Researcher develops one question from either optional path in `ANCHOR.md`.
The Analyst challenges the evidence and final package. The only successful
final artifact is a build in `forge/builds/` awaiting human review.

## Pipeline

```
RESEARCHER                         ANALYST
IDEATE -> PROPOSE -> RESEARCH ---> EVALUATE
                    ^                |
                    |---- REVISE ----|
                                     v
                    BUILD <--------- PASS
                      |
                      +-----------> VERIFY -> HUMAN REVIEW
                                      |
                               REVISE OR REJECT
```

| Stage | Owner | Folder | Purpose |
|:--|:--|:--|:--|
| Ideate | Researcher | `forge/ideas/` | Select one path and one falsifiable question. |
| Propose | Researcher | `forge/proposals/` | Define the evidence plan and acceptance contract. |
| Research | Researcher | `forge/research/` | Execute the plan and preserve contradictory evidence. |
| Evaluate | Analyst | `forge/evaluations/` | PASS, HALT-REVISE, or HALT-REJECT the research. |
| Build | Researcher | `forge/builds/` | Synthesize an implementation-ready review package. |
| Verify | Analyst | `forge/verifications/` | Verify claims, traceability, tests, risks, and scope. |

Full spec: `forge/protocol.md`.

## State and Memory

- `ANCHOR.md`: eternal human-locked mission and two optional paths.
- `STATUS.md`: one compact authoritative cursor.
- `LEARNINGS.md`: bounded, cross-pipeline method memory.
- `logbook/progress.log`: append-only `ENT-XXX` stage and handoff events.
- `logbook/errors.log`: append-only `ENT-XXX` failure and fix events.
- `logbook/archive/`: CI archives either active log after 500 lines using
  the same script and workflow as the agentic-brain.

There is no separate journal. The logbook is the chronological record.

## Canonical Skills

`governance/skills/` contains canonical blueprints only. They are not
runtime-loaded from this repo. Runtime copies may be deployed to the two
profiles later, after review; this repository does not install them.

## Deferred Cron Deployment

No Forge cron job is active as part of this design. The recommended later
deployment is:

| Role | Suggested schedule | Entrypoint | Work directory |
|:--|:--|:--|:--|
| Researcher | `5 * * * *` | `forge-loop-researcher` | this repo root |
| Analyst | `35 * * * *` | `forge-loop-analyst` | this repo root |

Each prompt says to invoke its loop, advance at most one eligible stage,
and exit without writes when ineligible. Jobs start paused, are manually
dry-run against the real repo, and are enabled only after both dry-runs
prove correct behavior. Repository state replaces cron continuity.

Both future jobs use the absolute repo path to
`scripts/forge-status-monitor.py` as their Hermes cron `monitor` and set
continuity off. Delivery is local so stage ticks do not spam a chat.
Unchanged status skips the model entirely. While the Forge is `ready`, the
monitor adds one UTC-day cadence bucket so a no-idea result retries once the
next day; active, blocked, and review states wake only when `STATUS.md`
changes. Each profile has an independent monitor baseline.

Exact future prompts:

```text
Researcher: Invoke forge-loop-researcher. Advance at most one eligible
Researcher-owned Forge stage. If no work is eligible, exit without writes.

Analyst: Invoke forge-loop-analyst. Perform at most one eligible Analyst
Forge gate. If no work is eligible, exit without writes.
```

The future Researcher job must attach `forge-loop-researcher`,
`forge-loop-feynman`, `forge-ideate`, `forge-propose`, `forge-research`,
`forge-build`, and the existing read-only `query-brain-vps`. The future
Analyst job must attach `forge-loop-analyst`, `forge-evaluate`,
`forge-verify`, and `query-brain-vps`. No Forge skill is deployed by this
repository.

## Layout

```
ANCHOR.md             eternal mission
STATUS.md             current cursor
LEARNINGS.md          bounded method memory
forge/                protocol and immutable stage artifacts
logbook/              uniform event logs and archives
governance/skills/    canonical Forge skills
scripts/              locks, validators, and repository gates
tests/                workflow regression tests
```

## Repository Gates

- ASCII-only and unique timestamp IDs.
- One active pipeline, one stage per run, one role per stage.
- Immutable artifacts linked by `parent` and `supersedes`.
- Forge-local writes only; optional brain access is read-only through
  `query-brain-vps`.
- Exact-path commits; the VPS watcher publishes them.
- A verified build freezes at `awaiting-review` until Suggi acts.
