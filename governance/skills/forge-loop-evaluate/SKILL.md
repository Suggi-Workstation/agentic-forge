---
name: forge-loop-evaluate
description: "Run one Forge ideation, evaluation, or final review."
user-invocable: false
disable-model-invocation: false
---
# Forge Loop -- Ideate and Evaluate

This entrypoint originates ideas, evaluates research, or reviews a final proposal,
one bounded stage per session. It does not install or schedule itself.

## Scope Gate

Apply the Session Transaction and Scope in `forge/protocol.md`. Before
any write, PASS requires the authorized Forge root, a supported stage, and
known clean inputs; otherwise HALT. Before evaluation or final review, verify the
protocol's independent-agent/context requirement. Use the configured model.

## Procedure

1. Read `ANCHOR.md`, `STATUS.md`, `forge/protocol.md`, and `LEARNINGS.md`.
2. Validate the entire STATUS board and apply the protocol's Pipeline Board
   and Selection rule: oldest eligible evaluation/final review first, then
   oldest requested reframe. With neither, attempt one new idea from ANCHOR,
   even if other pipelines await research or Suggi. Invalid rows or missing
   inputs HALT the invocation; they are not permission to start new work.
3. At `ideate`, read and execute `governance/skills/forge-ideate/SKILL.md`.
   A new idea adds its own row without changing waiting pipelines; a reframe
   retains its pipeline and correction history. Keep LEARNINGS read-only,
   complete only the idea transaction and exit. No new lead is a write-free
   NO-OP; a requested reframe with no viable correction follows protocol HALT.
4. At `evaluate` or `final-review`, read and execute
   `governance/skills/forge-evaluate/SKILL.md` in its corresponding mode.
   The skill records a cold baseline before
   reading the target body and selects the appropriate template.
5. Complete one verdict, including the exact next stage or graveyard
   closure. No missing source, timeout, or unperformed test implies READY.
   Record the intended learning decision before freezing that artifact.
6. Only after that completed evaluation or final review, apply LEARNINGS'
   admission gate. Make justified method edits or leave the file unchanged;
   never rewrite the completed verdict or manufacture a lesson quota. If
   a planned learning edit cannot pass its gate, report that in the progress
   event and leave LEARNINGS unchanged.
7. Complete the protocol transaction for the verdict, allowed learning
   edits, the selected STATUS row, and one review ENT event identifying its
   Pipeline. Preserve all other rows; commit as the actual author.
   This loop owns the transaction, not a second stage or a second verdict.
8. Exit. READY makes only that pipeline wait for Suggi; other pipelines
   remain eligible in later invocations. It grants no implementation authority.

## Failure

Use protocol recovery and resume handling. Preserve the same input/stage
on incomplete work and clean only your own partial writes. Unknown prior
edits require a recovery decision, never a guessed verdict or reset.

## Completion Gate

PASS requires the selected template/protocol gates, correct single-pipeline
handoff, unchanged unselected rows, and no chained stage. At evaluation or
final review, also require an independent verdict, correct correction budget,
and every learning edit passing its separate admission gate. Ideation keeps
LEARNINGS unchanged. Otherwise HALT faulty writes; no worthwhile new lead is NO-OP.
