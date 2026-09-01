---
name: forge-loop-feynman
description: "Run blank-page-first reasoning inside the Forge."
user-invocable: false
disable-model-invocation: false
---

# Forge Feynman Loop

Uses blank-page-first reasoning without creating a separate repository
artifact. The invoking stage owns all output.

## When to Use

Run inside Researcher stages before ideation, method design, research, or
build synthesis. Analyst skills carry their own cold-baseline procedure and
do not depend on this skill.

## Procedure -- HARD GATE

1. **Blank page.** After reading the anchor, status, and active parent, state
   the current understanding from memory. Do not search or consult sources.
2. **Gap list.** List unknowns, hidden assumptions, uncertain numbers,
   missing mechanisms, and plausible counter-hypotheses.
3. **Research.** Fill each material gap with web sources, prior Forge work,
   and optional read-only `query-brain-vps`. Query results are leads; read
   the underlying source before using a claim.
4. **Fresh synthesis.** Rewrite from scratch. State what changed, what
   remains uncertain, and confidence per material claim.
5. **Cross-check.** Test against `ANCHOR.md`, `LEARNINGS.md`, graveyard
   post-mortems, the active chain, and contrary evidence.
6. **Hand off.** Give the synthesis and unresolved gaps to the invoking
   stage skill. This skill itself writes nothing.

PASS only when steps 1-6 occurred in order and every material gap was
resolved or explicitly bounded. HALT if source consultation happened before
the blank page, a citation was not read, or a contradiction was suppressed.

## Confinement

- Forge repository reads and writes only.
- `query-brain-vps` and brain file reads are read-only.
- No brain reflection, memory write, investing-hub write, profile change,
  skill deployment, or cron change.

## Related

- `forge/protocol.md`
- `ANCHOR.md`
- `LEARNINGS.md`