---
name: forge-research
description: "Research a forge idea with web and brain sources. Produces evidence reports in forge/research/. Invoked by the forge loop when an active idea exists in Stage 1."
user-invocable: false
disable-model-invocation: false
---

# Forge Research -- Stage 2

## What This Skill Does

Guides researching a forge idea with web and brain sources.
Produces a Stage 2 artifact in `forge/research/` following the format
specified in `skills/forge-research/assets/template.md`. The evidence report
tests each claim from the idea brief against independent sources.

## When to Invoke

Invoke when the forge loop detects an active idea in Stage 1
(`forge/ideas/` with `status: active`). This is the second link in
the provenance chain: research -> idea.

Skip for:
- Ideas that have not passed the ideate gate (no brief in forge/ideas/)
- Ideas already researched (advance to evaluate instead)
- Ideas where the parent idea brief is missing or incomplete

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed: all 8 steps executed in order (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Forge Gate: PASS (write to research/) or HALT (write post-mortem to graveyard/) -- decision documented (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `forge-loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). Focus the blank page on: "What evidence
would prove or disprove each claim in the idea brief? What sources
are most likely to have this evidence?"

See `skills/forge-loop-feynman/SKILL.md` for the full procedure and
self-check.

### 2. Read the parent idea brief

Read the active idea brief from `forge/ideas/`. Confirm it has:
- A clear hypothesis
- 2-3 specific, testable claims in "What I Need to Prove"
- `status: active`

If the idea brief is incomplete or missing claims, HALT and flag
in `logs/progress.log` -- the idea brief needs revision before
research can proceed.

### 3. Gather evidence

For each claim in the idea brief, search for independent evidence:

- `web_search` for market data, competitor analysis, industry reports,
  and news articles.
- `web_fetch` for reading specific pages (competitor websites, research
  papers, pricing pages, market reports).
- `query-brain` for prior agentic-brain work on this domain.
- Aim for at least 3 independent sources per claim. If fewer than 3
  exist, state that explicitly -- this IS evidence.

### 4. Read the format specification

Read `skills/forge-research/assets/template.md`. It defines the evidence
report format: frontmatter schema, body structure (Sources, Findings,
Contradictions, Updated Confidence), and an example. Follow it exactly.

### 5. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 6. Write the evidence report

Write ONLY to the forge pipeline.

Path: `forge/research/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique within
`forge/research/`. Should reference the parent idea slug for
traceability.

### 7. Apply the Forge Gate

Apply the Stage 2 gate: "Does the evidence support the hypothesis?"

- **Evidence sufficiency:** At least 3 independent sources per claim,
  OR a documented reason why fewer exist.
- **Contradictions surfaced:** Any evidence against the hypothesis is
  included in the Contradictions section. Nothing buried or omitted.
- **Honest confidence:** Updated confidence reflects the evidence.
  It went up (evidence supports), down (evidence contradicts), or
  stayed the same (inconclusive).

**PASS:** Evidence supports the hypothesis. Contradictions exist but
are not fatal. Write the artifact to `forge/research/<short-slug>.md`.
The `status` field is `active`. Log progress to `logs/progress.log`.
The pipeline advances to Stage 3 (evaluate).

**HALT:** Evidence contradicts the hypothesis OR fewer than 3
sources found per claim with no documented reason. Write a post-mortem
to `forge/graveyard/<short-slug>-postmortem.md` explaining what the
evidence showed and why the idea failed. The `status` field is
`halted`. Log to `progress.log`. Next session: invoke `forge-ideate`
for a new idea.

### 8. Commit and push

```bash
git add -A
git diff --cached --stat
git -c user.name="Forge" -c user.email="forge@suggi-workspace.dev" \
  commit -m "forge: research <short-slug>"
git push origin main
```

If the push fails, pull first, resolve, then push.

## Sub-Checklists -- HARD GATE

Verify every Sub-Checklist item below. Each maps to the template.
HALT on any failure; fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, max 60 chars, unique within forge/research/ (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed (PASS / HALT)
- [ ] stage: "research" (PASS / HALT)
- [ ] parent: exact id of the idea brief this researches (PASS / HALT)
- [ ] status: "active" (PASS) or "halted" (HALT) (PASS / HALT)
- [ ] confidence: 0.0-1.0, updated to reflect evidence found (PASS / HALT)
- [ ] created: YYYY-MM-DD, matches the session date (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Sources section: at least 3 sources per claim, OR documented reason why fewer exist. Each source has URL, date, and key excerpt (PASS / HALT)
- [ ] Findings section: organized by claim from the idea brief. Each claim addressed individually with evidence strength rating (strong/moderate/weak/none) (PASS / HALT)
- [ ] Contradictions section: evidence against the hypothesis surfaced. If none found, the search thoroughness is explained (PASS / HALT)
- [ ] Updated Confidence: 0.0-1.0, compared to initial confidence from idea brief. Change explained. States what would further change confidence (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Feynman Loop): completed: blank page before research, all 6 steps confirmed (PASS / HALT)
- [ ] G2 (Claims Addressed Individually): each claim from the idea brief addressed separately. No claims skipped or merged (PASS / HALT)
- [ ] G3 (Sources Are Independent): sources are from different publishers/domains. Not 3 pages from the same website (PASS / HALT)
- [ ] G4 (Sources Are Dated): publication dates included. No undated sources unless the source itself is undated (PASS / HALT)
- [ ] G5 (Contradictions Not Buried): evidence against the hypothesis is in the Contradictions section. Nothing suppressed or minimized (PASS / HALT)
- [ ] G6 (Confidence Is Honest): updated confidence reflects the evidence honestly. If evidence is weak, confidence is low. No false certainty (PASS / HALT)
- [ ] G7 (Frontmatter Complete): all 8 fields present (name, id, stage, parent, status, confidence, created, tags) (PASS / HALT)
- [ ] G8 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug, max 60 chars (PASS / HALT)
- [ ] Written ONLY to forge/research/ -- NOT to memory/, NOT to agentic-brain (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G8) (PASS / HALT)

## Forge Gate

**Stage 2 Gate: Does the evidence support the hypothesis?**

This gate determines whether the idea advances to Stage 3 (evaluate)
or dies here. It is the evidence threshold -- the idea survives if
independent sources support the claims and contradictions are either
absent or non-fatal.

**PASS outcome:** Evidence report written to `forge/research/`.
Pipeline active at Stage 2. Next session: invoke `forge-evaluate`
to score the evidence.

**HALT outcome:** Post-mortem written to `forge/graveyard/`. The
post-mortem MUST document: which claims failed, what the evidence
showed, why the idea cannot proceed, and what was learned. Log to
`progress.log`. Next session: invoke `forge-ideate` for a new idea.

**Edge case -- inconclusive:** If evidence is inconclusive (weak
evidence but no contradictions), the agent may PASS with low confidence
(0.2-0.4) and let evaluation decide. The HALT gate at evaluation
will catch ideas that cannot be scored.

**Verification:** Before committing, the PASS/HALT decision MUST be
explicitly stated in `logs/progress.log` with the research id and
the reasoning.

## Related

- `skills/forge-research/assets/template.md` -- evidence report format, example
- `skills/forge-ideate/SKILL.md` -- prior stage (idea generation)
- `skills/forge-loop-feynman/SKILL.md` -- Feynman Loop (prerequisite)
- `skills/query-brain/SKILL.md` -- brain search (for prior work)
- `forge/protocol.md` -- full pipeline specification
