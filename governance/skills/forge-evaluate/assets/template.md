---
name: template-forge-evaluate
tier: template
stage: evaluations
version: 1.0
---

# Forge Evaluate Template -- Evaluation Verdict Format

## What This Template Defines

The format for Stage 3 artifacts: evaluation verdicts in
`forge/evaluations/`. Every verdict MUST follow this structure exactly.
For the writing procedure and quality gates, see
`skills/forge-evaluate/SKILL.md`.

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>        # ISO 8601 UTC, generated with date -u +'%Y%m%dT%H%M%SZ'
stage: evaluations              # always evaluations
parent: <id>                   # id of the evidence report this evaluates
status: active                 # active, halted, or complete
confidence: <0.0-1.0>          # confidence in this verdict
created: <YYYY-MM-DD>
tags: [<tag>, <tag>]           # lowercase, hyphens for spaces
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, max 60 chars, unique.
- `id` is ISO 8601 UTC. MUST generate with `date -u +'%Y%m%dT%H%M%SZ'`.
  Never estimate, never round. Never reuse.
- `stage` is always `evaluations`.
- `parent` is the exact `id` of the evidence report this evaluates.
  Provenance: evaluation -> research -> idea.
- `status` is `active` if the verdict is PASS (pipeline continues),
  `halted` if the verdict is HALT (pipeline stops here).
- `confidence` is 0.0-1.0 reflecting how confident the author is in this
  verdict. Low confidence in a HALT verdict = ask for second opinion.
- `tags` use lowercase, hyphens for spaces.

## Body Structure

### Verdict
*PASS or HALT. One word, then explanation.*

PASS means: the evidence supports the hypothesis, the idea is credible
and viable, and the pipeline should advance to the proposal stage.
HALT means: the evidence does not support the hypothesis, the idea
is not viable as formulated, or a fatal weakness was found.

### Criteria
*How does this idea score on each dimension?*

Score each dimension 1-5 (1 = weakest, 5 = strongest):

| Dimension | Score | Reasoning |
|:--|:--|:--|
| Novelty | 1-5 | Is this genuinely new or already crowded? |
| Evidence strength | 1-5 | How strong is the supporting evidence? |
| Market viability | 1-5 | Could this be a sustainable business? |
| Technical feasibility | 1-5 | Can an AI agent build and operate this? |
| Competitive moat | 1-5 | Is it defensible against copycats? |

PASS threshold: average >= 3.0, no individual criterion < 2.
HALT if: average < 3.0 OR any criterion = 1 (fatal weakness).

### Strengths
*What does the evidence support strongly?*

List the strongest findings. What makes this idea credible.

### Weaknesses
*What does the evidence undermine or leave unknown?*

List the weakest findings. What gaps remain. What could kill this idea.

### Recommendation
*What should happen next?*

If PASS: what to focus on in the proposal stage. Which risks need
the most attention. What assumptions need validation.

If HALT: graveyard (definitively dead) or return to ideate (narrowed
scope could salvage this). If returning to ideate, state the narrowed
scope explicitly.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars. Unique within
  `forge/evaluations/`.
- Ideally references the parent evidence report slug.
- Example: `ai-code-review-service-verdict.md`

## Example -- Minimal Valid Evaluation Verdict

```markdown
---
name: ai-code-review-service-verdict
id: 20260801T140000Z
stage: evaluations
parent: 20260801T130000Z
status: active
confidence: 0.70
created: 2026-08-01
tags: [code-review, developer-tools, saas]
---

# [EVAL-001] AI Code Review Service -- Evaluation Verdict

## Verdict
PASS. The evidence supports the hypothesis: a tool gap exists,
developers pay for code quality, and AI accuracy is approaching
human-level. The competitive threat from AI coding assistants is
real but not fatal -- a focused, best-in-class code review tool
can differentiate.

## Criteria

| Dimension | Score | Reasoning |
|:--|:--|:--|
| Novelty | 4 | Pattern-based tools exist; semantic review is genuinely different |
| Evidence strength | 3 | Strong on tool gap, moderate on willingness to pay and AI accuracy |
| Market viability | 3 | Market exists but competitive pressure from AI coding assistants |
| Technical feasibility | 3 | AI accuracy approaching human; large codebase handling is unsolved |
| Competitive moat | 2 | Low -- features can be copied. Moat must come from data, network effects, or brand |

Average: 3.0. No criterion < 2. PASS threshold met.

## Strengths
- Tool gap is real and well-documented across vendor docs and surveys.
- Market validation exists through CodeRabbit's funding and dev tools
  spending data.
- AI accuracy is approaching human-level and improving rapidly.

## Weaknesses
- Competitive moat is weak -- AI coding assistants (Cursor, Copilot)
  are absorbing review features. Differentiation strategy needed.
- Large codebase handling (>10K LOC) is unsolved in current LLMs.
- Only 2 sources for AI accuracy claim (need third source in proposal
  stage).

## Recommendation
PASS to proposal stage. Focus areas:
1. Competitive differentiation strategy -- what moat CAN be built?
2. Pricing model with unit economics.
3. Large codebase handling strategy (chunking, incremental review).
4. Find third source for AI accuracy claim.
```
