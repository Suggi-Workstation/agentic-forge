---
name: forge-verify
description: "Run loop-owned Forge verification in one short session."
user-invocable: false
disable-model-invocation: false
---
# Forge Verify

Analyst uses this only when `STATUS.md` says `stage: verify` and
`owner: Analyst`.

## Procedure

1. Read proposal acceptance criteria and the PASS evaluation, but not the
   build body.
2. Write a short expected-build baseline in working reasoning.
3. Read `governance/skills/forge-verify/assets/template.md`.
4. Now read the build and trace each recommendation to evidence.
5. Check simplicity, tests, worst case, rollback, scope, and uncertainty.
6. Issue exactly one verdict:
   - PASS -> `review` / Human
   - REVISE -> `build` / Researcher
   - REJECT -> reset to `ready`
7. Write one `forge/verifications/<slug>-rNN.md` and return its path, ID,
   verdict, and next cursor.

## Learning

If repeated pipeline evidence supports one short method lesson, Analyst may
update `LEARNINGS.md` in the same session. Humans never edit that file.

## Gate

The baseline must precede build reading. PASS requires an evidence-traceable,
implementable, testable, reversible build.