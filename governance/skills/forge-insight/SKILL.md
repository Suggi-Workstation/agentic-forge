---
name: forge-insight
description: "Extract a durable, transferable principle from a validated research pipeline. Produces insight artifacts in forge/insights/. Invoked by the forge loop when a PASS validation exists in Stage 5."
user-invocable: false
disable-model-invocation: false
---

# Forge Insight -- Stage 6

## What This Skill Does

Extracts the durable principle from a completed forge pipeline.
Produces a Stage 6 artifact in `forge/insights/` following the
format specified in `skills/forge-insight/assets/template.md`.

This is the final stage. The pipeline from idea to insight is
complete. The output is not working code -- it is transferable
knowledge that Suggi can review and implement.

## When to Invoke

Invoke when the forge loop detects a PASS validation in Stage 5
(`forge/validations/` with `status: active`). This is the sixth and
final link in the provenance chain: insight -> validate -> propose ->
evaluate -> research -> idea.

Skip for:
- Plans that have not passed the validate gate
- Plans returned for revision (fix first, then re-validate)
- Plans already completed (pipeline finished)

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed: all 8 steps executed in order (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Forge Gate: PASS (insight extracted, pipeline complete) or HALT (principle not clear, document why) -- decision documented (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before extracting the insight, invoke the `loop-feynman` skill.
Complete all 6 steps. Focus the blank page on: "What is the ONE
thing someone should take away from this entire pipeline? If Suggi
reads only one sentence from this work, what should it be?"

See `skills/loop-feynman/SKILL.md` for the full procedure and
self-check.

### 2. Read the Full Provenance Chain

Read every artifact in the pipeline from idea to validation:

- Idea brief: what was the original hypothesis?
- Evidence report: what did the research find?
- Evaluation verdict: what gate did it pass and why?
- Research plan: what method was proposed?
- Validation result: what stress-testing revealed

The insight must be grounded in the full chain. It cannot claim
more than the evidence supports.

### 3. Distill the Principle

Extract the durable principle. This is the hardest step. Ask:

- What pattern emerges from this pipeline that was NOT obvious
  before the research?
- What would another agent learn from reading this pipeline?
- What can Suggi DO with this knowledge?
- What is the ONE sentence that captures the finding?

The principle MUST be:
- **Specific.** "Harness design matters" is not an insight.
  "Agents with maker-checker gates produce 30% fewer factual
  errors than agents without" is.
- **Evidence-backed.** Every claim traces to a source in the
  research stage.
- **Transferable.** Another agent studying a different domain
  could apply this principle.
- **Actionable.** Suggi can implement or test this.

### 4. Read the Format Specification

Read `skills/forge-insight/assets/template.md`. It defines the insight
artifact format: frontmatter schema, body structure (Principle,
Evidence Summary, Actionability, Confidence, Limitations, Provenance
Chain), and an example. Follow it exactly.

### 5. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 6. Write the Insight

Write ONLY to the forge pipeline.

Path: `forge/insights/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique within
`forge/insights/`. Should reference the research domain for
discoverability (e.g., `maker-checker-reduces-errors.md`).

### 7. Apply the Forge Gate

Apply the Stage 6 gate: "Is this principle actionable AND transferable?"

- **Actionable:** Suggi can implement or test this. It is not
  abstract -- it describes a concrete change, pattern, or design
  choice with clear implications.
- **Transferable:** The principle applies beyond this specific
  pipeline. Another agent or another domain could use it.

**PASS:** The principle is clear, evidence-backed, actionable,
and transferable. Write insight to `forge/insights/<short-slug>.md`.
The `status` field is `complete`. Log pipeline completion to
`logs/progress.log`.

Update the parent artifacts: mark the validation result, proposal,
evaluation, research, and idea brief as `status: complete`. The
full provenance chain is now closed.

Update `LEARNINGS.md` with a new entry summarizing the principle,
confidence, and which pipelines contributed evidence.

Every 10th session: also write a synthesis to the agentic-brain as
a durable artifact (per ANCHOR.md iteration rule 4).

**HALT -- graveyard:** The research produced valid findings but
no actionable principle emerged, OR the principle cannot be
extracted with sufficient clarity. Write a post-mortem to
`forge/graveyard/<short-slug>-postmortem.md`. Documents: what was
found, why an insight could not be extracted, and what was learned.
The pipeline ends here. Next session: invoke `forge-ideate` for a
new idea.

### 8. Commit and Push

```bash
git add -A
git diff --cached --stat
git -c user.name="Forge" -c user.email="forge@suggi-workspace.dev" \
  commit -m "forge: insight <short-slug> -- complete"
git push origin main
```

If the push fails, pull first, resolve, then push.

## Sub-Checklists -- HARD GATE

Verify every Sub-Checklist item below. Each maps to the template.
HALT on any failure; fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, max 60 chars, unique within forge/insights/ (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed (PASS / HALT)
- [ ] stage: "insights" (PASS / HALT)
- [ ] parent: exact id of the validation result this synthesizes (PASS / HALT)
- [ ] status: "complete" (insight extracted) -- no halted state; if insight cannot be extracted, pipeline goes to graveyard (PASS / HALT)
- [ ] confidence: 0.0-1.0, final confidence in the principle (PASS / HALT)
- [ ] created: YYYY-MM-DD, matches the session date (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Principle: one sentence capturing the durable finding. Specific, not generic. Evidence-backed, not asserted (PASS / HALT)
- [ ] Evidence Summary: key sources and findings that support the principle. Traces to specific claims in the research stage (PASS / HALT)
- [ ] Actionability: what Suggi can DO with this. Concrete change, testable hypothesis, or design decision. Not abstract advice (PASS / HALT)
- [ ] Confidence: 0.0-1.0, explained. States what would change confidence up or down (PASS / HALT)
- [ ] Limitations: what this insight does NOT cover. Boundaries, caveats, contexts where it may not apply (PASS / HALT)
- [ ] Provenance Chain: full linked chain from insight back to idea. Every parent id listed and correct (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Feynman Loop): completed: blank page before synthesis, all 6 steps confirmed (PASS / HALT)
- [ ] G2 (Grounded in Evidence): every claim in the principle traces to at least one source in the research stage. No free-floating assertions (PASS / HALT)
- [ ] G3 (Specific, Not Generic): the principle names a specific pattern, mechanism, or tradeoff. "X matters" is generic; "X improves Y by Z under conditions A, B" is specific (PASS / HALT)
- [ ] G4 (Actionable): Suggi can implement or test the principle with available resources. If it requires infrastructure Suggi does not have, that limitation is stated (PASS / HALT)
- [ ] G5 (Transferable): the principle applies beyond this specific research question. Another domain, agent, or pipeline could use it (PASS / HALT)
- [ ] G6 (Honest Limitations): boundaries and caveats are stated explicitly. Overclaiming is worse than underclaiming (PASS / HALT)
- [ ] G7 (Provenance Complete): the provenance chain links every stage correctly. Each parent id is the exact id of the prior artifact (PASS / HALT)
- [ ] G8 (Pipeline Closed): if PASS, all parent artifacts are marked `status: complete`. The pipeline is finished (PASS / HALT)
- [ ] G9 (LEARNINGS.md Updated): a new entry added to LEARNINGS.md summarizing the principle, confidence, and pipeline provenance (PASS / HALT)
- [ ] G10 (Frontmatter Complete): all 8 fields present (name, id, stage, parent, status, confidence, created, tags) (PASS / HALT)
- [ ] G11 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug, max 60 chars (PASS / HALT)
- [ ] Written ONLY to forge/insights/ -- NOT to memory/, NOT to agentic-brain (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G11) (PASS / HALT)

## Forge Gate

**Stage 6 Gate: Is this principle actionable AND transferable?**

This is the final gate. The idea has survived ideation, research,
evaluation, planning, and validation. Now it must produce knowledge
that compounds -- a principle Suggi can use and another agent can
learn from.

**PASS outcome:** Insight written to `forge/insights/` with
`status: complete`. All parent artifacts marked complete. Pipeline
finished. LEARNINGS.md updated. Logged to `progress.log`.

**HALT outcome (graveyard):** No actionable principle could be
extracted. Post-mortem written to `forge/graveyard/`. Documents
what was found and why an insight could not be produced. Next
session: invoke `forge-ideate` for a new idea.

**Verification:** Before committing, the PASS/HALT decision MUST be
explicitly stated in `logs/progress.log` with the insight id and
reasoning.

## Related

- `skills/forge-insight/assets/template.md` -- insight artifact format, example
- `skills/forge-validate/SKILL.md` -- prior stage (validation)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite)
- `forge/protocol.md` -- full pipeline specification
- `LEARNINGS.md` -- cross-pipeline compound knowledge
- `ANCHOR.md` -- iteration rule 4 (every 10th session synthesis)
