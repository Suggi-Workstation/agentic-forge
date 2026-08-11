---
name: forge-evaluate
description: "Evaluate research evidence for a forge idea. Produces PASS/HALT verdicts in forge/evaluations/. Invoked by the forge loop when an evidence report exists in Stage 2."
user-invocable: false
disable-model-invocation: false
---

# Forge Evaluate -- Stage 3

## What This Skill Does

Guides evaluating the evidence from Stage 2 research against five
dimensions: novelty, evidence strength, market viability, technical
feasibility, and competitive moat. Produces a Stage 3 artifact in
`forge/evaluations/` following the format specified in
`skills/forge-evaluate/assets/template.md`. The verdict is a binary PASS or
HALT -- this is the pipeline's most critical gate.

## When to Invoke

Invoke when the forge loop detects an active evidence report in
Stage 2 (`forge/research/` with `status: active`). This is the third
link in the provenance chain: evaluate -> research -> idea.

Skip for:
- Evidence reports that have not passed the research gate
- Ideas without a complete evidence report (missing claims, no sources)
- Ideas already evaluated (advance to propose if PASS, graveyard if HALT)

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed: all 8 steps executed in order (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Forge Gate: PASS (write to evaluations/, advance to propose) or HALT (write post-mortem to graveyard/) -- decision documented (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any evaluation, invoke the `loop-feynman` skill. Complete all
6 steps. The blank page (Step 1) MUST precede any source consultation
(Step 3). Focus the blank page on: "What criteria would a fair evaluator
use to judge this evidence? What would make this idea succeed or fail?"

See `skills/loop-feynman/SKILL.md` for the full procedure and
self-check.

### 2. Read the parent evidence report

Read the active evidence report from `forge/research/`. Confirm it has:
- Sources for each claim from the original idea brief
- Findings organized by claim with evidence strength ratings
- Contradictions surfaced
- Updated confidence

Also re-read the parent idea brief from `forge/ideas/` to confirm
the original hypothesis and claims.

### 3. Score each dimension

Score the idea on five dimensions, 1-5 each:

| Dimension | What to assess |
|:--|:--|
| Novelty | Is this genuinely new? Check brain + web for prior art. A 5 means no existing work covers this. A 1 means thoroughly explored. |
| Evidence strength | How strong is the supporting evidence? Consider source count, source independence, and source recency. A 5 means multiple recent, independent, high-quality sources confirm every claim. A 1 means no credible evidence. |
| Logical soundness | Do conclusions follow from evidence? Are there gaps in reasoning? A 5 means every claim is fully supported. A 1 means claims are unsupported assertions. |
| Research feasibility | Can this be meaningfully researched with available tools? A 5 means web search and brain search are sufficient. A 1 means requires capabilities not available. |
| Potential impact | If true, how much would this finding matter? A 5 means game-changing for the anchor goal. A 1 means trivial even if proven true. |

### 4. Read the format specification

Read `skills/forge-evaluate/assets/template.md`. It defines the evaluation
verdict format: frontmatter schema, body structure (Verdict, Criteria,
Strengths, Weaknesses, Recommendation), and an example. Follow it
exactly.

### 5. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 6. Write the evaluation verdict

Write ONLY to the forge pipeline.

Path: `forge/evaluations/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique within
`forge/evaluations/`. Should reference the parent evidence report slug
for traceability.

### 7. Apply the Forge Gate

Apply the Stage 3 gate: "Is the idea credible AND viable?"

**PASS threshold:** Average score across all 5 dimensions >= 3.0,
AND no individual dimension scored 1 (fatal weakness).

**HALT if:** Average < 3.0 OR any dimension scored 1 (fatal weakness).

- A score of 1 on any dimension is a fatal weakness -- even if other
  dimensions score 5, the idea cannot proceed.
- A score of 2 on any dimension is a warning -- the proposal stage
  MUST address it explicitly.

**PASS:** Write verdict to `forge/evaluations/<short-slug>.md`. The
`status` field is `active`. Log progress to `logs/progress.log`.
The pipeline advances to Stage 4 (propose).

**HALT:** Write a post-mortem to `forge/graveyard/<short-slug>-postmortem.md`
explaining which dimensions failed, why, and what was learned. The
`status` field is `halted`. Log to `progress.log`.

**HALT with narrowed scope:** If a dimension scored 2 and the idea
could be salvaged with a narrower scope, write a post-mortem AND a
note in `logs/progress.log` recommending a return to ideate with
the narrowed scope.

### 8. Commit and push

```bash
git add -A
git diff --cached --stat
git -c user.name="Forge" -c user.email="forge@suggi-workspace.dev" \
  commit -m "forge: evaluate <short-slug> -- <PASS|HALT>"
git push origin main
```

If the push fails, pull first, resolve, then push.

## Sub-Checklists -- HARD GATE

Verify every Sub-Checklist item below. Each maps to the template.
HALT on any failure; fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, max 60 chars, unique within forge/evaluations/ (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed (PASS / HALT)
- [ ] stage: "evaluations" (PASS / HALT)
- [ ] parent: exact id of the evidence report this evaluates (PASS / HALT)
- [ ] status: "active" (PASS verdict) or "halted" (HALT verdict) (PASS / HALT)
- [ ] confidence: 0.0-1.0, reflecting confidence in this verdict (PASS / HALT)
- [ ] created: YYYY-MM-DD, matches the session date (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Verdict: "PASS" or "HALT" stated as the first word, followed by explanation (PASS / HALT)
- [ ] Criteria: all 5 dimensions scored 1-5 with reasoning for each score. Average calculated. PASS/HALT threshold applied (PASS / HALT)
- [ ] Strengths: strongest findings listed. What makes the idea credible (PASS / HALT)
- [ ] Weaknesses: weakest findings and gaps listed. What could kill the idea (PASS / HALT)
- [ ] Recommendation: concrete next step. If PASS: what to focus on. If HALT: graveyard or narrowed-scope return to ideate (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Feynman Loop): completed: blank page before evaluation, all 6 steps confirmed (PASS / HALT)
- [ ] G2 (All Dimensions Scored): novelty, evidence strength, logical soundness, research feasibility, and potential impact all scored 1-5 with reasoning (PASS / HALT)
- [ ] G3 (Threshold Applied Correctly): average >= 3.0 and no 1s = PASS. Average < 3.0 or any 1 = HALT. No exceptions, no hand-waving (PASS / HALT)
- [ ] G4 (Strengths and Weaknesses Both Present): both sections have content. A PASS verdict still lists weaknesses. A HALT verdict still lists strengths (PASS / HALT)
- [ ] G5 (Recommendation Is Actionable): the next step is concrete. Not "think about it more" but "focus competitive analysis on X" or "return to ideate with scope narrowed to Y" (PASS / HALT)
- [ ] G6 (Evidence Not Re-Argued): the evaluation judges the evidence, not redoes the research. No new sources introduced unless a fatal gap was found (PASS / HALT)
- [ ] G7 (Frontmatter Complete): all 8 fields present (name, id, stage, parent, status, confidence, created, tags) (PASS / HALT)
- [ ] G8 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug, max 60 chars (PASS / HALT)
- [ ] Written ONLY to forge/evaluations/ -- NOT to memory/, NOT to agentic-brain (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G8) (PASS / HALT)

## Forge Gate

**Stage 3 Gate: Is the idea credible AND viable?**

This is the pipeline's most critical gate. It separates ideas worth
planning from ideas that die here. The five-dimension scoring system
ensures a balanced assessment -- an idea must be good across ALL
dimensions, not just one.

**PASS outcome:** Evaluation verdict written to `forge/evaluations/` with
`status: active`. Pipeline advances to Stage 4 (propose). Next session:
invoke `forge-propose` to write an implementation plan.

**HALT outcome:** Post-mortem written to `forge/graveyard/`. The
post-mortem MUST document: which dimensions failed, the scores, the
reasoning, and what was learned. The idea is dead unless a narrowed
scope could salvage it.

**HALT with salvage:** If the idea failed primarily due to scope (too
broad, market too competitive for the full vision but a niche exists),
recommend a return to `forge-ideate` with a narrowed scope. The
post-mortem documents both the death of the broad idea and the
narrowed scope for the next attempt.

**Verification:** Before committing, the PASS/HALT decision MUST be
explicitly stated in `logs/progress.log` with the evaluation id, scores,
and reasoning.

## Related

- `skills/forge-evaluate/assets/template.md` -- evaluation verdict format, example
- `skills/forge-research/SKILL.md` -- prior stage (evidence gathering)
- `skills/forge-propose/SKILL.md` -- next stage (implementation planning)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite)
- `forge/protocol.md` -- full pipeline specification
