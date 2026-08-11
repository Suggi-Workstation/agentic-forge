---
name: forge-propose
description: "Write an implementation plan for a forge idea that passed evaluation. Produces plans in forge/proposals/. Invoked by the forge loop when a PASS verdict exists in Stage 3."
user-invocable: false
disable-model-invocation: false
---

# Forge Propose -- Stage 4

## What This Skill Does

Guides writing a research plan for an idea that passed
Stage 3 evaluation. Produces a Stage 4 artifact in `forge/proposals/`
following the format specified in `skills/forge-propose/assets/template.md`.
The plan must be concrete enough that another agent could execute it
from the description alone.

## When to Invoke

Invoke when the forge loop detects a PASS verdict in Stage 3
(`forge/evaluations/` with `status: active`). This is the fourth link
in the provenance chain: propose -> evaluate -> research -> idea.

Skip for:
- Ideas that received a HALT verdict (they belong in the graveyard)
- Ideas where the evaluation's recommendation asks for narrowed scope
  (return to ideate first)
- Ideas without a complete evaluation verdict

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed: all 8 steps executed in order (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Forge Gate: PASS (write to proposals/, advance to validate) or HALT (return to research or graveyard) -- decision documented (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any planning, invoke the `loop-feynman` skill. Complete all
6 steps. The blank page (Step 1) MUST precede any source consultation
(Step 3). Focus the blank page on: "What is the simplest working
version of this idea? What are the irreducible components? What
assumptions am I making that need validation?"

See `skills/loop-feynman/SKILL.md` for the full procedure and
self-check.

### 2. Read the parent evaluation verdict and evidence report

Read the PASS verdict from `forge/evaluations/`. Note the recommendation
-- which dimensions need the most attention. Re-read the evidence
report from `forge/research/` and the original idea brief from
`forge/ideas/`. The plan must address the full provenance chain.

### 3. Design the research plan

Working from the evaluation's recommendation and the evidence report's
findings, design a concrete research plan:

- What is the specific research question this pipeline will answer?
- What method will be used? What sources, what analysis?
- What insight is expected if the hypothesis holds?
- What is the counter-hypothesis -- the alternative explanation?
- What are the top risks to this research succeeding?

The plan must be grounded in the evidence -- every methodological
choice should trace to a finding in the evidence report.

### 4. Read the format specification

Read `skills/forge-propose/assets/template.md`. It defines the research
plan format: frontmatter schema, body structure (Research Question,
Method, Expected Insight, Counter-Hypothesis, Risk Matrix),
and an example. Follow it exactly.

### 5. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 6. Write the implementation plan

Write ONLY to the forge pipeline.

Path: `forge/proposals/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique within
`forge/proposals/`. Should reference the parent evaluation slug for
traceability.

### 7. Apply the Forge Gate

Apply the Stage 4 gate: "Is the plan concrete AND feasible?"

- **Concrete:** Another agent could implement this from the description
  alone. Every implementation step is a specific, verifiable action.
  No hand-waving, no "figure it out later."
- **Feasible:** The implementation steps are within the agent's capabilities
  and available tools. The business model has unit economics (even if
  rough). The risk matrix covers the top 3-5 risks with mitigations.

**PASS:** The plan is concrete and feasible. Write to
`forge/proposals/<short-slug>.md`. The `status` field is `active`.
Log progress to `logs/progress.log`. The pipeline advances to Stage 5
(validate).

**HALT -- return to research:** The plan revealed an evidence gap that
needs filling before planning can proceed. Document the gap in
`logs/progress.log`. Return to Stage 2 (research) to fill the gap,
then re-plan.

**HALT -- graveyard:** The plan revealed a fatal feasibility issue
(cannot be researched with available tools, no viable method).
Write a post-mortem to `forge/graveyard/<short-slug>-postmortem.md`.
The `status` field is `halted`. Log to `progress.log`.

### 8. Commit and push

```bash
git add -A
git diff --cached --stat
git -c user.name="Forge" -c user.email="forge@suggi-workspace.dev" \
  commit -m "forge: propose <short-slug>"
git push origin main
```

If the push fails, pull first, resolve, then push.

## Sub-Checklists -- HARD GATE

Verify every Sub-Checklist item below. Each maps to the template.
HALT on any failure; fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, max 60 chars, unique within forge/proposals/ (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed (PASS / HALT)
- [ ] stage: "proposals" (PASS / HALT)
- [ ] parent: exact id of the evaluation verdict this builds on (PASS / HALT)
- [ ] status: "active" (PASS) or "halted" (HALT) (PASS / HALT)
- [ ] confidence: 0.0-1.0, reflecting confidence in this plan's feasibility (PASS / HALT)
- [ ] created: YYYY-MM-DD, matches the session date (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Problem: specific, evidence-backed, references the evidence report. One to three sentences (PASS / HALT)
- [ ] Research Question: the specific question this pipeline answers. Falsifiable and scoped (PASS / HALT)
- [ ] Method: research approach described. Sources, analysis steps, evaluation criteria. Reproducible by another agent (PASS / HALT)
- [ ] Expected Insight: what principle is expected if the hypothesis holds. Specific, not vague (PASS / HALT)
- [ ] Counter-Hypothesis: alternative explanation stated. What evidence would support it over the main hypothesis (PASS / HALT)
- [ ] Risk Matrix: top 3-5 risks with likelihood, impact, and mitigation for each (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Feynman Loop): completed: blank page before planning, all 6 steps confirmed (PASS / HALT)
- [ ] G2 (Problem Is Evidence-Backed): the problem statement references findings from the evidence report. Not restated from memory (PASS / HALT)
- [ ] G3 (Method Is Concrete): research method is specific enough for another agent to execute. Sources, steps, and evaluation criteria are clear. No hand-waving (PASS / HALT)
- [ ] G4 (Counter-Hypothesis Is Plausible): the alternative explanation is realistic, not a strawman. Evidence that would support it is specified (PASS / HALT)
- [ ] G5 (Expected Insight Is Falsifiable): the expected insight can be proven wrong. If the evidence contradicts it, the pipeline will detect that (PASS / HALT)
- [ ] G6 (Method Steps Are Ordered): research steps are in dependency order. Later steps do not depend on outcomes of earlier steps unless the dependency is explicit (PASS / HALT)
- [ ] G7 (Risks Have Mitigations): every risk in the matrix has a mitigation. No risk is listed as "unmitigatable" without explanation (PASS / HALT)
- [ ] G8 (Frontmatter Complete): all 8 fields present (name, id, stage, parent, status, confidence, created, tags) (PASS / HALT)
- [ ] G9 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug, max 60 chars (PASS / HALT)
- [ ] Written ONLY to forge/proposals/ -- NOT to memory/, NOT to agentic-brain (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G9) (PASS / HALT)

## Forge Gate

**Stage 4 Gate: Is the plan concrete AND feasible?**

This gate ensures the research plan is actionable. An idea can have
strong evidence and pass evaluation but still fail here if it cannot
be translated into a concrete, executable research plan.

**PASS outcome:** Research plan written to `forge/proposals/` with
`status: active`. Pipeline advances to Stage 5 (validate). Next session:
invoke `forge-validate` to stress-test the plan.

**HALT outcome (return to research):** Plan revealed an evidence gap.
Document the gap in `logs/progress.log`. The gap specifies: which
claim needs more evidence, what kind of evidence is needed, and where
to search. Next session: invoke `forge-research` to fill the gap, then
re-plan.

**HALT outcome (graveyard):** Plan revealed a fatal feasibility issue.
Post-mortem written to `forge/graveyard/`. Documents: what was planned,
why it is infeasible, and what was learned. Next session: invoke
`forge-ideate` for a new idea.

**Verification:** Before committing, the PASS/HALT decision MUST be
explicitly stated in `logs/progress.log` with the proposal id and
the reasoning.

## Related

- `skills/forge-propose/assets/template.md` -- implementation plan format, example
- `skills/forge-evaluate/SKILL.md` -- prior stage (evaluation)
- `skills/forge-validate/SKILL.md` -- next stage (validation)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite)
- `forge/protocol.md` -- full pipeline specification
