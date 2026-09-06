# Agentic Forge

The Agentic Forge turns useful questions into evidence-backed proposals
through stage-based research and evaluation. This repository contains
canonical blueprints only. Installing skills or scheduling loops is a
separate task requiring Suggi's authorization; repository contents do not establish live
deployment state.

## Simple Pipeline

```text
IDEA -> RESEARCH -> EVALUATE -> PROPOSE -> FINAL REVIEW -> SUGGI
                       |                     |
                       +-> research / reframe / graveyard
```

| Stage | Output |
|:--|:--|
| Idea and its research plan | `forge/ideas/` |
| Evidence and alternatives | `forge/research/` |
| Research evaluation | `forge/evaluations/` |
| Concrete proposal and response to evaluation | `forge/proposals/` |
| Review of the actual final proposal | `forge/evaluations/` |
| Rejected or deferred work | `forge/graveyard/` (closure verdict; evidence stays in place) |

Each session attempts one small stage in 10-15 minutes. An unfinished
stage does not advance. Suggi approves, requests changes, defers, or rejects
the exact proposal; implementation needs separate authorization.

## Future Cadence -- Not Installed

When Suggi later deploys the profile-local copies:

- The research loop runs on the hour, for example 13:00, 14:00, 15:00.
- The evaluation loop runs 30 minutes later, for example 13:30, 14:30, 15:30.
- The 15-minute session limit leaves at least a 15-minute buffer.

That future cadence assumes sessions do not overlap; it is not proof of
mutual exclusion. There is no file lock, monitor, wrapper, or runtime setup
in this blueprint. Unexpected concurrent edits require a halt.

## Canonical Skill Bundles

Research workflow (`ideate`, `research`, `propose`):

- `forge-loop-research`
- `forge-loop-feynman`
- `forge-ideate`
- `forge-propose`
- `forge-research`

Evaluation workflow (`evaluate`, `final-review`):

- `forge-loop-evaluate`
- `forge-evaluate`

Agent assignments are deployment choices, not part of these skill names or
the state cursor. `forge/protocol.md` defines stage eligibility and independent
evaluation; actual authorship remains in artifacts and log events.
`forge-evaluate` handles both research evaluation and final proposal review.
Templates are separate files directly under `governance/`:
`template-idea.md`, `template-research.md`, `template-evaluation.md`,
`template-proposal.md`, and `template-review.md`.

These are blueprints only. Copying or scheduling them is a separate future
task requiring Suggi's instruction.

## State and Memory

- `ANCHOR.md`: agent/investing subjects and reflection-led discovery.
- `STATUS.md`: one small current-state cursor.
- `LEARNINGS.md`: method lessons written only after `evaluate` or
  `final-review`; read from the start of idea selection and during later work.
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