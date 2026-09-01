---
name: forge-evaluate
description: "Run loop-owned Forge evaluation in one short session."
user-invocable: false
disable-model-invocation: false
---
# Forge Evaluate

Analyst uses this only when `STATUS.md` says `stage: evaluate` and
`owner: Analyst`.

## Procedure

1. Read the idea and proposal acceptance criteria, but not the research
   report body.
2. Write a short expected-results baseline in working reasoning.
3. Read `governance/skills/forge-evaluate/assets/template.md`.
4. Now read the research report and check claims against cited sources.
5. Test method fit, evidence quality, contradictions, uncertainty, and value.
6. Issue exactly one verdict:
   - PASS -> `build` / Researcher
   - REVISE -> `research` / Researcher
   - REJECT -> reset to `ready`
7. Write one `forge/evaluations/<slug>-rNN.md` and return its path, ID,
   verdict, and next cursor.

## Gate

The baseline must precede target reading. PASS requires all material
criteria to pass; uncertainty is never silently averaged away.