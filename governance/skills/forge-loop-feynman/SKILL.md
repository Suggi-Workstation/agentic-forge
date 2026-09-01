---
name: forge-loop-feynman
description: "Run the 6-step Feynman loop before any Forge stage work: blank page, gap list, research, fresh synthesis, cross-check, hand off to the stage skill."
user-invocable: false
disable-model-invocation: false
---

# Forge Loop Feynman -- Thinking Discipline

## Hard Gate (R4)

Run before any Forge stage skill does substantive work. The ordering
constraint (Step 1 before Step 3) prevents existing-knowledge bias.

## When to Apply

- Before every stage skill invocation in a Forge pipeline.
- Before answering a research question that feeds an artifact.

Skip for:
- Mechanical operations (git commits, file moves, log appends).
- Simple factual answers that do not feed an artifact.

## Self-Check -- HARD GATE

- [ ] Step 1 completed from memory (no sources, no search)  (PASS / HALT)
- [ ] Step 2 produced an explicit gap list  (PASS / HALT)
- [ ] Step 3 filled every gap  (PASS / HALT)
- [ ] Step 4 rewritten fresh (not edited Step 1)  (PASS / HALT)
- [ ] Step 5 cross-checked  (PASS / HALT)
- [ ] Step 6 hand-off: stage skill invoked with the synthesis  (PASS / HALT)
- [ ] Step 1 preceded Step 3  (PASS / HALT)

## Steps

### 1. Blank Page

Write everything known about the topic from memory alone. No sources,
no notes, no search. This is the diagnostic: it reveals what is
actually known vs what is assumed.

### 2. Identify Gaps

List every gap explicitly:

- what could not be explained;
- what was hedged;
- missing connections;
- approximate numbers or dates.

These gaps are the search targets for Step 3.

### 3. Search and Research

Fill every gap:

- `web_search` for current information and data;
- the agentic-brain for prior art (`query-brain-vps` or grep on
  `/srv/brain/agentic-brain`) -- read-only;
- the Forge repository for prior artifacts, graveyard post-mortems,
  and `LEARNINGS.md` -- a new idea must not rename an old one.

Cross-reference sources. When sources disagree, investigate which is
correct and document why. Never invent a citation to fill a gap.

### 4. Synthesize

Rewrite the understanding from scratch. Do not edit Step 1. State what
changed between Step 1 and now. State confidence per major claim.

### 5. Cross-Check

Check the synthesis against:

- the agentic-brain for contradictions with prior insights;
- `LEARNINGS.md` and `graveyard/` for repeated mistakes;
- the active ANCHOR for relevance.

Resolve contradictions explicitly: state them, state which source is
more current or reliable, and cross-link.

### 6. Hand Off

The synthesis is raw material for the stage skill. Invoke the stage
skill with it; the stage skill owns the artifact, the template, and
the gate. This skill writes nothing to the repository itself.

## Related

- `forge-loop` -- the orchestrator that invokes this skill.
- `forge/protocol.md` -- pipeline specification.
