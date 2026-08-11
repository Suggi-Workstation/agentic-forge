---
name: forge-ideate
description: "Generate and scope ideas for the forge pipeline. Produces idea briefs in forge/ideas/. Invoked by the forge loop when no active pipeline exists."
user-invocable: false
disable-model-invocation: false
---

# Forge Ideate -- Stage 1

## What This Skill Does

Guides generating a scoped idea brief for the forge pipeline.
Produces a Stage 1 artifact in `forge/ideas/` following the format
specified in `skills/forge-ideate/assets/template.md`. The idea brief is the
first link in the provenance chain: idea -> research -> evaluate ->
propose -> validate -> insight.

## When to Invoke

Invoke when the forge loop detects no active pipeline and needs
to generate a new idea. Also invoke when a prior evaluation recommended
returning to ideate with a narrowed scope.

Skip for:
- Ideas already in `forge/ideas/` with status `active` (advance them instead)
- Ideas already researched and evaluated (they need a proposal, not re-ideation)
- Non-forge brainstorming (write to memory/, not forge/)

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed: all 8 steps executed in order (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Forge Gate: PASS (write to ideas/) or HALT (write post-mortem to graveyard/) -- decision documented (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). Focus the blank page on: "What novel
research questions could advance the current anchor goal? What gaps
exist in our current understanding?"

See `skills/loop-feynman/SKILL.md` for the full procedure and
self-check.

### 2. Read the anchor goal

Read `ANCHOR.md` to confirm the current objective. The idea MUST
align with the anchor goal currently defined in ANCHOR.md.

### 3. Scan for prior work

Check `forge/ideas/`, `forge/graveyard/`, and the agentic-brain
(via `query-brain`) for related ideas:
- Has this idea already been explored?
- Did a similar idea die in the graveyard? What killed it?
- Has another agent researched this domain?

If the idea is not novel (already extensively covered), HALT.
If a graveyard post-mortem covers the same ground, read it and
decide whether new evidence warrants reopening.

### 4. Read the format specification

Read `skills/forge-ideate/assets/template.md`. It defines the idea brief
format: frontmatter schema, body structure (Hypothesis, Why This
Matters, What I Need to Prove, Initial Confidence), and an example.
Follow it exactly.

### 5. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 6. Write the idea brief

Write ONLY to the forge pipeline. NEVER write idea briefs outside
the forge folder.

Path: `forge/ideas/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique within `forge/ideas/`.

### 7. Apply the Forge Gate

Apply the Stage 1 gate: "Is this idea novel AND testable?"

- **Novel:** Not already extensively covered in the agentic-brain or
  web. Graveyard post-mortems on related ideas have been read and
  distinguished.
- **Testable:** The "What I Need to Prove" section contains 2-3
  specific, falsifiable claims. Each claim could be answered with
  evidence from independent sources.

**PASS:** The idea is both novel and testable. Write the artifact to
`forge/ideas/<short-slug>.md`. The `status` field is `active`. Log
progress to `logs/progress.log`. The pipeline is now in Stage 1.

**HALT:** The idea is not novel OR not testable. Write a post-mortem
to `forge/graveyard/<short-slug>-postmortem.md` explaining why the
idea failed the gate. The `status` field is `halted`. Document the
reason in `logs/progress.log`. Generate a new idea.

### 8. Commit and push

```bash
git add -A
git diff --cached --stat
git -c user.name="Forge" -c user.email="forge@suggi-workspace.dev" \
  commit -m "forge: ideate <short-slug>"
git push origin main
```

If the push fails, pull first, resolve, then push.

## Sub-Checklists -- HARD GATE

Verify every Sub-Checklist item below. Each maps to the template.
HALT on any failure; fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, max 60 chars, unique within forge/ideas/ (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed (PASS / HALT)
- [ ] stage: "ideas" (PASS / HALT)
- [ ] parent: "root" (new idea) or id of triggering artifact (derived idea) (PASS / HALT)
- [ ] status: "active" (PASS) or "halted" (HALT) (PASS / HALT)
- [ ] confidence: 0.0-1.0, stated honestly (PASS / HALT)
- [ ] created: YYYY-MM-DD, matches the session date (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Hypothesis: one clear, falsifiable statement at the top. Not a question, not a wish (PASS / HALT)
- [ ] Why This Matters: market signal, trend, or gap cited. Problem and audience stated (PASS / HALT)
- [ ] What I Need to Prove: 2-3 specific, testable claims. Each claim is answerable with evidence (PASS / HALT)
- [ ] Initial Confidence: 0.0-1.0 with reasoning. States what would change the confidence level (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Feynman Loop): completed: blank page before research, all 6 steps confirmed (PASS / HALT)
- [ ] G2 (Aligned with Anchor): idea advances the goal currently defined in ANCHOR.md (PASS / HALT)
- [ ] G3 (Novel): not already extensively covered in brain or web. Prior art acknowledged. Graveyard post-mortems checked (PASS / HALT)
- [ ] G4 (Testable): claims are falsifiable with evidence from web search, brain search, or both. No unfalsifiable claims (PASS / HALT)
- [ ] G5 (Scoped): idea is narrow enough to research in 2-3 cron sessions. Not a sprawling vision (PASS / HALT)
- [ ] G6 (Honest Confidence): confidence reflects prior knowledge honestly. Low confidence is not hidden behind optimistic language (PASS / HALT)
- [ ] G7 (Frontmatter Complete): all 8 fields present (name, id, stage, parent, status, confidence, created, tags) (PASS / HALT)
- [ ] G8 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug, max 60 chars (PASS / HALT)
- [ ] Written ONLY to forge/ideas/ -- NOT to memory/, NOT to agentic-brain (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G8) (PASS / HALT)

## Forge Gate

**Stage 1 Gate: Is this idea novel AND testable?**

This gate determines whether the idea advances to Stage 2 (research)
or dies here. It is the first and most permissive gate in the pipeline --
most ideas should pass. The bar is low: the idea must be genuinely new
(to the agent's knowledge) and structured in a way that evidence can be
gathered for or against it.

**PASS outcome:** Idea brief written to `forge/ideas/`. Pipeline active
at Stage 1. Next session: invoke `forge-research` to gather evidence.

**HALT outcome:** Post-mortem written to `forge/graveyard/`. The
post-mortem MUST document what was attempted, why it failed the gate
(not novel, not testable, or both), and what was learned. Log to
`progress.log`. Next session: invoke `forge-ideate` for a new idea.

**Verification:** Before committing, the PASS/HALT decision MUST be
explicitly stated in `logs/progress.log` with the idea id and the
reasoning.

## Related

- `skills/forge-ideate/assets/template.md` -- idea brief format, example
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite)
- `skills/query-brain/SKILL.md` -- brain search (for prior art check)
- `forge/protocol.md` -- full pipeline specification
- `ANCHOR.md` -- the forge north star goal
- `logs/protocol.md` -- progress logging format
