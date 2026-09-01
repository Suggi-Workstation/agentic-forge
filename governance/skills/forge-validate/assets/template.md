---
name: template-forge-validate
tier: template
stage: validations
version: 1.0
---

# Forge Validate Template -- Validation Result Format

## What This Template Defines

The format for Stage 5 artifacts: stress-test results in
`forge/validations/`. Every validation result MUST follow this structure
exactly. For the writing procedure and quality gates, see
`skills/forge-validate/SKILL.md`.

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>        # ISO 8601 UTC, generated with date -u +'%Y%m%dT%H%M%SZ'
stage: validations              # always validations
parent: <id>                   # id of the proposal this validates
status: active                 # active, halted, or complete
confidence: <0.0-1.0>          # final confidence after all validation
created: <YYYY-MM-DD>
tags: [<tag>, <tag>]           # lowercase, hyphens for spaces
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, max 60 chars, unique.
- `id` is ISO 8601 UTC. MUST generate with `date -u +'%Y%m%dT%H%M%SZ'`.
  Never estimate, never round. Never reuse.
- `stage` is always `validations`.
- `parent` is the exact `id` of the proposal this validates.
  Provenance: validation -> proposal -> evaluation -> research -> idea.
- `status` is `active` if the proposal survives stress-testing,
  `halted` if it does not.
- `confidence` is 0.0-1.0 reflecting final confidence in the plan
  after all validation and mitigation.
- `tags` use lowercase, hyphens for spaces.

## Body Structure

### Method
*How was the proposal stress-tested?*

Describe the testing approach. What dimensions were tested? What
criteria defined PASS/HALT for each dimension? What adversarial
scenarios were explored? The method should be reproducible.

### Result
*What was the outcome for each dimension?*

For each dimension tested:
- Dimension: what was tested (e.g., business model viability,
  technical feasibility, competitive defensibility, unit economics)
- Result: PASS or HALT
- Evidence: what the test revealed

### Weak Points Found
*What did the stress-test reveal as fragile?*

List every weakness discovered during validation. Be specific.
A proposal with no weak points found was not stress-tested
thoroughly enough.

### Mitigations Added
*What does the proposal now include that it did not before validation?*

For each weak point, describe the mitigation. If a weak point has
no viable mitigation, state that explicitly -- this is a HALT
condition.

### Final Confidence
*How confident am I that this plan will work?*

0.0-1.0. Compare to the confidence level from the evaluation stage.
Explain what changed and why. State the single largest remaining
uncertainty.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars. Unique within
  `forge/validations/`.
- Example: `ai-code-review-service-validation.md`

## Example -- Minimal Valid Validation Result

```markdown
---
name: ai-code-review-service-validation
id: 20260801T160000Z
stage: validations
parent: 20260801T150000Z
status: active
confidence: 0.50
created: 2026-08-01
tags: [code-review, developer-tools, saas]
---

# [VALID-001] AI Code Review Service -- Validation Result

## Method
Stress-tested the proposal against four dimensions:
1. Business model: does the unit economics hold at scale?
2. Technical feasibility: can the LLM review real code accurately?
3. Competitive defensibility: can moat be built before incumbents copy?
4. Market timing: is the window open or closing?

Each dimension tested by searching for counter-evidence, modeling
worst-case scenarios, and identifying unstated assumptions.

## Result

| Dimension | Result | Evidence |
|:--|:--|:--|
| Business model | PASS | Unit economics are plausible. At $99/team, 50 PRs/month, gross margin ~75%. Break-even at ~20 paying teams. |
| Technical feasibility | PASS (conditional) | LLM code review is proven at small scale. Large codebase handling requires chunking strategy -- added to mitigations. |
| Competitive defensibility | HALT (mitigated) | Moat is weak. AI coding assistants adding review features. Mitigation: focus on depth over breadth (deep semantic analysis they do not offer). |
| Market timing | PASS | Window exists but is narrowing. Move fast. |

## Weak Points Found
1. Competitive moat is the weakest dimension. AI coding assistants
   (Cursor, Copilot, CodeRabbit) are converging on code review.
   Differentiation must come from depth, not breadth.
2. Large codebase handling (>10K LOC per PR) is unsolved. LLM context
   windows limit analysis scope. Chunking may miss cross-file logic
   errors.
3. Pricing assumptions are untested. No direct survey data on
   willingness to pay for standalone AI code review.

## Mitigations Added
1. Competitive strategy: focus exclusively on deep semantic review
   (logic errors, edge cases) that pattern-based tools cannot do.
   Do not compete on syntax/style.
2. Large codebase: implement hierarchical chunking -- review file-by-
   file first, then cross-file dependency analysis as a second pass.
3. Pricing validation: build a landing page with "join waitlist"
   before full build. Measure conversion rate by price point.

## Final Confidence
0.50 (down from 0.60 at evaluation). The competitive moat weakness
is structural -- it cannot be fully mitigated, only managed through
speed and differentiation. The idea is still viable but carries
higher risk than initially assessed. Largest remaining uncertainty:
will developers pay for standalone code review when their AI coding
assistant already offers basic review?
```
