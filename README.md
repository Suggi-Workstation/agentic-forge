# Agentic Forge

The Agentic Forge turns useful questions into evidence-backed proposals
through a Researcher/Analyst workflow. This repository contains canonical
blueprints only. Installing skills or scheduling loops is a separate task
requiring Suggi's authorization; repository contents do not establish live
deployment state.

## Simple Pipeline

```text
IDEA -> RESEARCH -> EVALUATE -> PROPOSE -> FINAL REVIEW -> SUGGI
                       |                     |
                       +-> research / reframe / graveyard
```

| Stage | Owner | Output |
|:--|:--|:--|
| Idea and its research plan | Researcher | `forge/ideas/` |
| Evidence and alternatives | Researcher | `forge/research/` |
| Research evaluation | Analyst | `forge/evaluations/` |
| Concrete proposal and response to evaluation | Researcher | `forge/proposals/` |
| Review of the actual final proposal | Analyst | `forge/evaluations/` |
| Rejected or deferred work | Analyst | `forge/graveyard/` (closure verdict; evidence stays in place) |

Each session attempts one small stage in 10-15 minutes. An unfinished
stage does not advance. Suggi approves, requests changes, defers, or rejects
the exact proposal; implementation needs separate authorization.

## Future Cadence -- Not Installed

When Suggi later deploys the profile-local copies:

- Researcher runs on the hour, for example 13:00, 14:00, 15:00.
- Analyst runs 30 minutes later, for example 13:30, 14:30, 15:30.
- The 15-minute session limit leaves at least a 15-minute buffer.

That future cadence assumes sessions do not overlap; it is not proof of
mutual exclusion. There is no file lock, monitor, wrapper, or runtime setup
in this blueprint. Unexpected concurrent edits require a halt.

## Canonical Skill Bundles

Future Researcher bundle:

- `forge-loop-researcher`
- `forge-loop-feynman`
- `forge-ideate`
- `forge-propose`
- `forge-research`

Future Analyst bundle:

- `forge-loop-analyst`
- `forge-evaluate`

`forge-evaluate` handles both research evaluation and final proposal review.
Templates are separate files directly under `governance/`:
`template-idea.md`, `template-research.md`, `template-evaluation.md`,
`template-proposal.md`, and `template-review.md`.

These are blueprints only. Copying or scheduling them is a separate future
task requiring Suggi's instruction.

## State and Memory

- `ANCHOR.md`: agent/investing subjects and reflection-led discovery.
- `STATUS.md`: one small current-state cursor.
- `LEARNINGS.md`: Analyst-written method lessons after evaluation or final
  review; Researcher reads them from the start of idea selection.
- `logbook/progress.log`: multiline ENT stage events.
- `logbook/errors.log`: multiline ENT failures and fixes.

There is no Forge artifact archive. Git preserves edits to method lessons;
completed artifacts stay immutable. Existing `logbook/archive/` is only the
append-only log retention mechanism, not a research stage or artifact store.

At ideation, compare graveyard records, existing ideas, and proposals,
including accepted and pending proposals. Human dispositions are recorded
against exact artifacts in the logbook. Reflection discovery uses
`query-brain-vps`, reads full sources, compares overlap, and treats agents'
interpretations as hypotheses rather than established facts.

`JOURNAL.md` is intentionally absent. The logbook is the chronology.

## Boundaries

- Write only inside this repository.
- Brain and web sources are read-only evidence.
- Never write to agentic-brain or investing-hub from a Forge procedure.
- Never edit profiles, shared skills, cron, services, or runtime config.
- Never push directly; the VPS watcher publishes verified commits.
- ASCII only. All connected artifacts share `pipeline: <idea r01 id>`;
  lean metadata and explicit links preserve immutable provenance.

Full workflow: `forge/protocol.md`.