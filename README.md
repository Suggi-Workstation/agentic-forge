# Agentic Forge

The Agentic Forge is a repository-only Researcher/Analyst pipeline. The
canonical skill blueprints live in `governance/skills/`. They are not
installed in any profile and no Forge cron jobs exist yet.

## Simple Pipeline

```text
Researcher: IDEATE -> PROPOSE -> RESEARCH
Analyst:                          EVALUATE
Researcher:                               BUILD
Analyst:                                        VERIFY -> HUMAN REVIEW
```

| Stage | Owner | Output |
|:--|:--|:--|
| Ideate | Researcher | `forge/ideas/` |
| Propose | Researcher | `forge/proposals/` |
| Research | Researcher | `forge/research/` |
| Evaluate | Analyst | `forge/evaluations/` |
| Build | Researcher | `forge/builds/` |
| Verify | Analyst | `forge/verifications/` |

Each session does one small stage and finishes within 10-15 minutes.
The roles never write outside this repository.

## Future Cadence -- Not Installed

When Suggi later deploys the profile-local copies:

- Researcher runs on the hour, for example 13:00, 14:00, 15:00.
- Analyst runs 30 minutes later, for example 13:30, 14:30, 15:30.
- The 15-minute session limit leaves at least a 15-minute buffer.

That simple stagger is the coordination mechanism. There is no file lock,
monitor script, wrapper, or runtime setup in this repository.

## Canonical Skill Bundles

Future Researcher bundle:

- `forge-loop-researcher`
- `forge-loop-feynman`
- `forge-ideate`
- `forge-propose`
- `forge-research`
- `forge-build`

Future Analyst bundle:

- `forge-loop-analyst`
- `forge-evaluate`
- `forge-verify`

These are blueprints only. Copying or scheduling them is a separate future
task requiring Suggi's instruction.

## State and Memory

- `ANCHOR.md`: eternal direction and the two optional research paths.
- `STATUS.md`: one small current-state cursor.
- `LEARNINGS.md`: agent-written cross-pipeline method memory.
- `logbook/progress.log`: multiline ENT stage events.
- `logbook/errors.log`: multiline ENT failures and fixes.
- `forge/archive/`: cold history that should not be read every session.

`JOURNAL.md` is intentionally absent. The logbook is the chronology.

## Boundaries

- Write only inside this repository.
- Brain and web sources are read-only evidence.
- Never write to agentic-brain or investing-hub from a Forge procedure.
- Never edit profiles, shared skills, cron, services, or runtime config.
- Never push directly; the VPS watcher publishes verified commits.
- ASCII only. Preserve immutable artifact provenance.

Full workflow: `forge/protocol.md`.