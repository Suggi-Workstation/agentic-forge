---
name: forge-validate
description: "Stress-test a forge implementation plan before building. Produces validation results in forge/validations/. Invoked by the forge loop when a plan exists in Stage 4."
user-invocable: false
disable-model-invocation: false
---

# Forge Validate -- Stage 5

## What This Skill Does

Guides stress-testing a research plan before committing to the
insight stage. Produces a Stage 5 artifact in `forge/validations/`
following the format specified in `skills/forge-validate/assets/template.md`.
The validation applies adversarial scrutiny: "What could go wrong?
What assumptions are untested? Where are the weak points?"

## When to Invoke

Invoke when the forge loop detects a PASS proposal in Stage 4
(`forge/proposals/` with `status: active`). This is the fifth link
in the provenance chain: validate -> propose -> evaluate -> research
-> idea.

Skip for:
- Proposals that have not passed the propose gate
- Proposals returned for revision (fix the issues first, then validate)
- Proposals already validated (advance to build if PASS)

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed: all 8 steps executed in order (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Forge Gate: PASS (write to validations/, advance to build) or HALT (return to propose with fixes) -- decision documented (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any validation, invoke the `forge-loop-feynman` skill. Complete all
6 steps. The blank page (Step 1) MUST precede any source consultation
(Step 3). Focus the blank page on: "What is the single worst thing
that could go wrong with this plan? What assumptions, if wrong, would
break it? Where would an adversary attack?"

See `skills/forge-loop-feynman/SKILL.md` for the full procedure and
self-check.

### 2. Read the parent proposal and full provenance chain

Read the implementation plan from `forge/proposals/`. Then re-read
the full chain: evaluation verdict, evidence report, and idea brief.
The validation tests the plan against its own evidence -- every claim
in the plan should trace to evidence in the research stage.

### 3. Stress-test each dimension

Test the plan against each dimension. For each:

- **Evidence validity:** Are the cited sources real, accessible, and
  correctly represented? What if key sources are wrong or outdated?
- **Logical consistency:** Do conclusions follow from premises? Are
  there hidden assumptions? What if an assumption is false?
- **Method soundness:** Is the research method reproducible? Are there
  confounding variables? What if the method misses an important factor?
- **Counter-hypothesis strength:** Is the alternative explanation
  plausible? What evidence would support the counter-hypothesis over
  the main hypothesis?
- **Implementation feasibility:** Can the plan be executed with
  available tools and within practical constraints? What step is most
  likely to fail?

For each dimension, search for counter-evidence using `web_search`
and `query-brain`. Look for conflicting studies, methodological
critiques, or evidence that supports the counter-hypothesis.

### 4. Read the format specification

Read `skills/forge-validate/assets/template.md`. It defines the validation
result format: frontmatter schema, body structure (Method, Result,
Weak Points Found, Mitigations Added, Final Confidence), and an
example. Follow it exactly.

### 5. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 6. Write the validation result

Write ONLY to the forge pipeline.

Path: `forge/validations/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique within
`forge/validations/`. Should reference the parent proposal slug for
traceability.

### 7. Apply the Forge Gate

Apply the Stage 5 gate: "Does the plan survive scrutiny?"

- **Survives:** Every dimension tested. Weak points identified AND
  mitigated. Unmitigatable weak points are acknowledged honestly but
  are not fatal (accepted risk). The plan is stronger after validation
  than before.
- **Does not survive:** A dimension fails and cannot be mitigated.
  The failure is structural, not a gap that more research can fill.

**PASS:** The plan survives stress-testing. Write result to
`forge/validations/<short-slug>.md`. The `status` field is `active`.
Log progress to `logs/progress.log`. The pipeline advances to Stage 6
(build).

**HALT -- return to propose:** A dimension failed but CAN be fixed
with plan revision. Document the specific failure and required fix
in the validation result. Return to Stage 4 (propose) with the fix
list. The `status` field is `halted`. Log the return to
`progress.log`.

**HALT -- graveyard:** A dimension failed and CANNOT be fixed. The
failure is structural (market does not exist, impossible to build,
no viable moat). Write a post-mortem to
`forge/graveyard/<short-slug>-postmortem.md`. Log to `progress.log`.
Next session: invoke `forge-ideate` for a new idea.

### 8. Commit and push

```bash
git add -A
git diff --cached --stat
git -c user.name="Forge" -c user.email="forge@suggi-workspace.dev" \
  commit -m "forge: validate <short-slug> -- <PASS|HALT>"
git push origin main
```

If the push fails, pull first, resolve, then push.

## Sub-Checklists -- HARD GATE

Verify every Sub-Checklist item below. Each maps to the template.
HALT on any failure; fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, max 60 chars, unique within forge/validations/ (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed (PASS / HALT)
- [ ] stage: "validations" (PASS / HALT)
- [ ] parent: exact id of the proposal this validates (PASS / HALT)
- [ ] status: "active" (PASS) or "halted" (HALT) (PASS / HALT)
- [ ] confidence: 0.0-1.0, final confidence after all validation (PASS / HALT)
- [ ] created: YYYY-MM-DD, matches the session date (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Method: testing approach described. What dimensions were tested, what criteria defined PASS/HALT. Reproducible by another agent (PASS / HALT)
- [ ] Result: each dimension tested individually with PASS/HALT outcome and evidence (PASS / HALT)
- [ ] Weak Points Found: every fragility discovered. A plan with no weak points found was not stress-tested thoroughly enough (PASS / HALT)
- [ ] Mitigations Added: each weak point has a mitigation OR an acknowledgment that it is unmitigatable (accepted risk) (PASS / HALT)
- [ ] Final Confidence: 0.0-1.0, compared to evaluation confidence. Change explained. Largest remaining uncertainty stated (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Feynman Loop): completed: blank page before validation, all 6 steps confirmed (PASS / HALT)
- [ ] G2 (Adversarial Mindset): the stress-test searches for counter-evidence, not confirmation. At least one web search or brain query for counter-evidence per dimension (PASS / HALT)
- [ ] G3 (Every Dimension Tested): evidence validity, logical consistency, method soundness, counter-hypothesis strength, and implementation feasibility all tested individually (PASS / HALT)
- [ ] G4 (Weak Points Honest): weak points are specific, not generic ("execution risk" is not a weak point; "step 3 depends on an API with 100 req/min rate limit" is). At least one weak point found per dimension (PASS / HALT)
- [ ] G5 (Mitigations Concrete): mitigations are specific actions, not intentions. "Monitor the situation" is not a mitigation. "Add fallback to alternative API if rate limit hit" is (PASS / HALT)
- [ ] G6 (Confidence Calibrated): final confidence reflects the validation honestly. If multiple weak points are unmitigatable, confidence is low. Confidence never exceeds evaluation confidence without strong reason (PASS / HALT)
- [ ] G7 (Frontmatter Complete): all 8 fields present (name, id, stage, parent, status, confidence, created, tags) (PASS / HALT)
- [ ] G8 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug, max 60 chars (PASS / HALT)
- [ ] Written ONLY to forge/validations/ -- NOT to memory/, NOT to agentic-brain (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G8) (PASS / HALT)

## Forge Gate

**Stage 5 Gate: Does the plan survive scrutiny?**

This is the last gate before insight extraction. It applies adversarial
thinking: assume the plan will fail somewhere, and find where. A plan
that survives this gate is ready for the final stage.

**PASS outcome:** Validation result written to `forge/validations/` with
`status: active`. Pipeline advances to Stage 6 (insight). Next session:
invoke `forge-insight` to extract the durable principle.

**HALT outcome (return to propose):** Plan failed a dimension but is
fixable. Validation result documents the specific failures and required
fixes. The proposal is revised, then validation re-runs. Next session:
invoke `forge-propose` to revise, then `forge-validate` to re-test.

**HALT outcome (graveyard):** Plan failed fatally. Post-mortem written
to `forge/graveyard/`. Documents: what was stress-tested, which
dimension failed fatally, why it cannot be fixed, and what was learned.

**Verification:** Before committing, the PASS/HALT decision MUST be
explicitly stated in `logs/progress.log` with the validation id,
dimension results, and reasoning.

## Related

- `skills/forge-validate/assets/template.md` -- validation result format, example
- `skills/forge-propose/SKILL.md` -- prior stage (planning)
- `skills/forge-insight/SKILL.md` -- next stage (insight extraction)
- `skills/forge-loop-feynman/SKILL.md` -- Feynman Loop (prerequisite)
- `forge/protocol.md` -- full pipeline specification
