---
name: forge-loop-analyst
description: "Run one short Analyst turn in the Forge."
user-invocable: false
disable-model-invocation: false
---
# Forge Loop -- Analyst

This is the future Analyst entrypoint. It advances at most one gate and
finishes within 10-15 minutes.

## Scope Gate

- Resolve the current git root and write only inside it.
- Never edit profiles, shared skills, cron, services, runtime config,
  agentic-brain, or investing-hub.
- Brain and web evidence are read-only.
- Never push directly; commit and let the watcher publish.

## Procedure

1. Read `ANCHOR.md`, `STATUS.md`, and `forge/protocol.md`.
2. If `owner` is not Analyst or `state` is awaiting-review, return NO-OP
   without writes.
3. Invoke exactly one skill; that skill owns the baseline and target-reading
   order:
   - `evaluate` -> `forge-evaluate`
   - `verify` -> `forge-verify`
4. Write at most one verdict artifact.
5. If repeated evidence supports one method lesson, update `LEARNINGS.md`.
6. Update `STATUS.md` and append one multiline `review` ENT block to
   `logbook/progress.log`.
7. Run `bash scripts/validate-ids.sh` and the ASCII gate.
8. Commit only the changed Forge files as Analyst, then exit.

## Failure

For a real tool or write failure, keep the cursor on the same stage and
append one multiline `error` ENT block. Never invent a verdict.

## Completion Gate

PASS when one independent gate is complete, the verdict/STATUS/log agree,
the checks pass, and the session stayed inside 15 minutes. Otherwise NO-OP
or HALT cleanly.
