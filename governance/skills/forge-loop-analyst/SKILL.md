---
name: forge-loop-analyst
description: "Run one short Analyst turn in the Forge."
user-invocable: false
disable-model-invocation: false
---
# Forge Loop -- Analyst

The Analyst entrypoint evaluates research or reviews a final proposal,
one bounded stage per session. It does not install or schedule itself.

## Scope Gate

Apply the Session Transaction and Scope in `forge/protocol.md`. Before
any write, PASS requires the authorized Forge root, valid ownership, and
known clean inputs; otherwise HALT. Use a separate Analyst context and the
configured model, not a self-review by the Researcher.

## Procedure

1. Read `ANCHOR.md`, `STATUS.md`, `forge/protocol.md`, and `LEARNINGS.md`.
2. If `owner` is not Analyst or `state` is awaiting-review, return NO-OP
   without writes.
3. At `evaluate` or `final-review`, read and execute
   `governance/skills/forge-evaluate/SKILL.md` in its corresponding mode.
   Any other owned stage HALTs. The skill records a cold baseline before
   reading the target body and selects the appropriate template.
4. Complete one verdict, including the exact next stage or graveyard
   closure. No missing source, timeout, or unperformed test implies READY.
   Record the intended learning decision before freezing that artifact.
5. Only after that completed evaluation or final review, apply LEARNINGS'
   admission gate. Make justified method edits or leave the file unchanged;
   never rewrite the completed verdict or manufacture a lesson quota. If
   a planned learning edit cannot pass its gate, report that in the progress
   event and leave LEARNINGS unchanged.
6. Complete the protocol transaction for the verdict, allowed learning
   edits, STATUS, and one review ENT event; commit as the actual author.
   This loop owns the transaction, not a second stage or a second verdict.
7. Exit. READY waits for Suggi; it grants no implementation authority.

## Failure

Use protocol recovery and resume handling. Preserve the same input/stage
on incomplete work and clean only your own partial writes. Unknown prior
edits require a recovery decision, never a guessed verdict or reset.

## Completion Gate

PASS requires the template/protocol gates, a checked independent verdict,
correct handoff and budget, and every learning edit passing its separate
admission gate. Otherwise HALT faulty writes; wrong ownership is NO-OP.
