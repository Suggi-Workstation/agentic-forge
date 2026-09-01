---
name: forge-loop-feynman
description: "Run blank-page-first reasoning for one Forge stage."
user-invocable: false
disable-model-invocation: false
---
# Forge Feynman Loop

Use inside a Researcher stage. It prepares one small 10-15 minute unit of
work and writes nothing by itself.

## Order

1. Read only `ANCHOR.md`, `STATUS.md`, `forge/protocol.md`, and the immediate
   assignment or parent artifact.
2. Blank page: state what you currently think, without sources.
3. List the exact gaps and uncertainties.
4. Now read `LEARNINGS.md`, relevant Forge artifacts, and log tails.
5. Fill only the listed gaps with read-only brain or web evidence.
6. Rewrite the conclusion from scratch and identify contradictions.
7. Return the bounded result to the calling stage skill.

## Gate

PASS only when blank page preceded source reading, gaps were answered, and
the result fits one short stage. Otherwise return NO-OP or narrow the task.

All writes stay in the Forge. External sources are read-only.