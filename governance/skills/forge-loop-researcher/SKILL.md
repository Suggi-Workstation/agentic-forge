---
name: forge-loop-researcher
description: "Run one short Researcher turn in the Forge."
user-invocable: false
disable-model-invocation: false
---
# Forge Loop -- Researcher

This is the future Researcher entrypoint. It advances at most one stage and
finishes within 10-15 minutes.

## Scope Gate

- Resolve the current git root and write only inside it.
- Never edit profiles, shared skills, cron, services, runtime config,
  agentic-brain, or investing-hub.
- Brain and web evidence are read-only.
- Never push directly; commit and let the watcher publish.

## Procedure

1. Read `ANCHOR.md`, `STATUS.md`, and `forge/protocol.md`.
2. If `owner` is not Researcher or `state` is awaiting-review, return NO-OP
   without writes.
3. Invoke exactly one skill from the current stage; that skill owns the
   Feynman ordering and artifact body:
   - `ideate` -> `forge-ideate`
   - `propose` -> `forge-propose`
   - `research` -> `forge-research`
   - `build` -> `forge-build`
4. Write at most one stage artifact.
5. Update the fixed fields in `STATUS.md` and append one multiline
   `research` ENT block to `logbook/progress.log`.
6. Run `bash scripts/validate-ids.sh` and the ASCII gate.
7. Commit only the changed Forge files as Researcher, then exit.

## Failure

For a real tool or write failure, keep the cursor on the same stage and
append one multiline `error` ENT block. Do not turn lack of evidence into a
confident result.

## Completion Gate

PASS when one bounded stage is complete, the artifact/STATUS/log agree, the
checks pass, and the session stayed inside 15 minutes. Otherwise NO-OP or
HALT cleanly.
