---
name: forge-loop-research
description: "Run one research or proposal stage in the Forge."
user-invocable: false
disable-model-invocation: false
---
# Forge Loop -- Research

This entrypoint advances one `research` or `propose` stage per
bounded session, regardless of the executing agent's identity.
It is a canonical blueprint, not an installed or scheduled runtime skill.

## Scope Gate

Apply the Session Transaction and Scope in `forge/protocol.md` before any
write. Resolve the authorized Forge root, not an arbitrary current repo.
PASS requires a supported stage and known clean inputs; HALT on dirty,
conflicting, missing, or out-of-scope state. Use the configured model.

## Procedure

1. Read `ANCHOR.md`, `STATUS.md`, `forge/protocol.md`, and `LEARNINGS.md`.
   Method memory is available before evidence gathering and proposal work.
2. Validate the entire STATUS board and apply the protocol's Pipeline Board
   and Selection rule. Select the oldest eligible `research` or `propose`
   row. If none exists, return NO-OP without writes. Never ideate while
   waiting; that belongs to `forge-loop-evaluate`. Invalid rows or inputs
   HALT the invocation rather than being skipped.
3. Read and execute exactly one canonical skill under `governance/skills/`:
   - `research` -> `forge-research/SKILL.md`
   - `propose` -> `forge-propose/SKILL.md`
   The selected skill owns its template and
   Feynman procedure; reading a blueprint is not permission to install it.
4. On a valid stage result, complete the protocol's artifact/STATUS/log
   transaction for that pipeline only; preserve all unselected rows and
   include its Pipeline line in the ENT event. Commit only intended files as the actual
   author. A new evidence gap follows the protocol's `evaluate` handoff;
   timeout follows its resume handling. NO-OP produces no writes.
5. LEARNINGS is read-only throughout this loop. Never add, edit, or retire
   a lesson here, even if the executing agent also runs evaluation in other
   sessions. Only completed `evaluate` or `final-review` stages own that gate.
6. Exit after this transaction; do not start the next stage.

## Failure

Use protocol recovery: keep the input/stage, clean only your own partial
writes, and record real errors. Do not discard unexplained prior changes,
declare unfinished work complete, or repair external systems.

## Completion Gate

PASS requires the selected skill and protocol gates, consistent handoff,
unchanged LEARNINGS, and no chained stage. Otherwise HALT faulty work;
no eligible research/proposal is a write-free NO-OP, not fabricated progress.
