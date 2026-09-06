---
name: forge-ideate
description: "Use when selecting or reframing a Forge idea."
user-invocable: false
disable-model-invocation: false
---
# Forge Ideate

Create one useful question, not a research report or an early proposal.
Run only through `forge-loop-research` at `ideate`; follow the common
transaction in `forge/protocol.md` and `governance/template-idea.md`.

## Procedure

1. Read ANCHOR, STATUS, protocol, and LEARNINGS before selecting a lead.
   For a reframe, read the existing idea and evaluation/review verdict;
   preserve the original pipeline ID. PASS when the assignment and method
   lessons are understood; HALT on missing or conflicting inputs.
2. Enumerate files in `forge/graveyard/`, `forge/ideas/`, and
   `forge/proposals/` with `search_files`. Search the candidate problem and
   synonyms, read plausible overlaps, and follow their research and verdict
   links. Check exact-proposal decisions in active and archived progress
   logs, including accepted and pending proposals. A search snippet is not
   a duplicate verdict. Record compared paths and why work is distinct.
3. Use `query-brain-vps` to check prior knowledge. If ANCHOR path C is chosen,
   use the caller's selection or a bounded random sample from enumerated
   reflection paths (actual tool sampling, not a hand-picked list called
   random). Record how selection was made and read chosen files in full.
   Search related reflections by problem, incident, and alternative wording;
   compare overlap, contradictions, shared origins, and present relevance.
   Prefer one unresolved question supported by this comparison, not one
   idea per reflection. Reflections are leads, not independent validation.
4. Consult `governance/skills/forge-loop-feynman/SKILL.md`. Discovery and
   method-memory reading come before the candidate's blank-page explanation.
   State a provisional hypothesis, alternative explanation, and unknowns;
   then check sources. New findings may expand or change the question.
5. Compare the final candidate again against prior work. If it is covered,
   already resolved, or closed without justified reopening, return NO-OP
   without a new artifact. A requested same-pipeline reframe is not a
   duplicate solely because its own earlier idea exists: explain the
   substantive correction and preserve the root ID and slug. If required
   prior-work checks are unavailable, HALT rather than claim novelty.
   A new label is not a new question.
6. Apply the idea template checklist. Write one idea with a small research
   plan in `forge/ideas/`; return its path and the protocol handoff to the
   loop. Do not perform the full research stage or write LEARNINGS here.

## Verification

Before writing, PASS requires completed duplicate/reflection checks,
mission fit, a narrow testable question, and the template checklist.
Otherwise HALT the artifact or return the legitimate no-lead NO-OP.
The loop owns state, logs, and commit; this skill never chains stages.
