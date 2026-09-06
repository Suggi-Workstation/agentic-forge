---
name: forge-loop-researcher
description: "Run one short Researcher turn in the Forge."
user-invocable: false
disable-model-invocation: false
---
# Forge Loop -- Researcher

The Researcher entrypoint advances at most one stage per bounded session.
It is a canonical blueprint, not an installed or scheduled runtime skill.

## Scope Gate

Apply the Session Transaction and Scope in `forge/protocol.md` before any
write. Resolve the authorized Forge root, not an arbitrary current repo.
PASS requires matching role/cursor and known clean inputs; HALT on dirty,
conflicting, missing, or out-of-scope state. Use the configured model.

## Procedure

1. Read `ANCHOR.md`, `STATUS.md`, `forge/protocol.md`, and `LEARNINGS.md`.
   Method memory is available before idea selection, not only afterwards.
2. If `owner` is not Researcher or `state` is awaiting-review, return NO-OP
   without writes.
3. Read and execute exactly one canonical skill under `governance/skills/`:
   - `ideate` -> `forge-ideate/SKILL.md`
   - `research` -> `forge-research/SKILL.md`
   - `propose` -> `forge-propose/SKILL.md`
   Any other owned stage HALTs. The selected skill owns its template and
   Feynman procedure; reading a blueprint is not permission to install it.
4. On a valid stage result, complete the protocol's artifact/STATUS/log
   transaction and commit only the intended Forge files as the actual
   author. A new evidence gap follows the protocol's Analyst handoff;
   timeout follows its resume handling. NO-OP produces no writes.
5. LEARNINGS is read-only for Researcher. Never add, edit, or retire a
   lesson here, even if a discovery seems useful. Analyst owns that gate.
6. Exit after this transaction; do not start the next Researcher stage.

## Failure

Use protocol recovery: keep the input/stage, clean only your own partial
writes, and record real errors. Do not discard unexplained prior changes,
declare unfinished work complete, or repair external systems.

## Completion Gate

PASS requires the selected skill and protocol gates, consistent handoff,
unchanged LEARNINGS, and no chained stage. Otherwise HALT faulty work;
no-lead or wrong-owner exits are legitimate NO-OPs, not fabricated progress.
