---
name: template-forge-insight
tier: template
stage: insights
version: 1.0
---

# Forge Insight Template -- Insight Artifact Format

## What This Template Defines

The format for Stage 6 artifacts: insights in `forge/insights/`.
Every insight artifact MUST follow this structure exactly. For the
writing procedure and quality gates, see `skills/forge-insight/SKILL.md`.

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>        # ISO 8601 UTC, generated with date -u +'%Y%m%dT%H%M%SZ'
stage: insights                # always insights
parent: <id>                   # id of the validation result this synthesizes
status: complete|halted        # complete if principle extracted, halted if unclear
confidence: <0.0-1.0>          # final confidence in the principle
created: <YYYY-MM-DD>
tags: [<tag>, <tag>]           # lowercase, hyphens for spaces
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, max 60 chars, unique.
- `id` is ISO 8601 UTC. MUST generate with `date -u +'%Y%m%dT%H%M%SZ'`.
  Never estimate, never round. Never reuse.
- `stage` is always `insights`.
- `parent` is the exact `id` of the validation result this synthesizes.
  Provenance: insight -> validation -> proposal -> evaluation ->
  research -> idea.
- `status` is `complete` if a clear principle was extracted,
  `halted` if the principle is not yet clear or not actionable.
- `confidence` is 0.0-1.0 based on evidence strength across the
  full provenance chain.
- `tags` use lowercase, hyphens for spaces.

## Body Structure

### Principle
*One sentence. The durable finding. Specific, transferable.*

What is the ONE thing someone should take away from this pipeline?
Must be specific ("X improves Y by Z under conditions A, B") not
generic ("X matters"). Every claim traces to a source in the
research stage.

### Evidence Summary
*What the full provenance chain proved.*

Key sources and findings that support the principle. Which claims
from the original idea brief were confirmed? Which were not? What
contradictions were found and resolved?

### Actionability
*What Suggi can DO with this insight.*

Concrete, specific actions. A design change. A new gate. A testable
hypothesis. A skill to build. Not abstract advice ("consider X") --
specific implementation guidance ("add maker-checker gate to
session-end with a 0.3 confidence threshold for REJECT").

### Confidence
*0.0-1.0, explained.*

Why this confidence level? What would increase it (more evidence
from different domains)? What would decrease it (counter-evidence,
failed replication)?

### Limitations
*What this insight does NOT cover.*

Boundaries: contexts where it may not apply, assumptions that must
hold, domains not yet tested. Overclaiming here poisons the insight's
credibility. Be honest about what is NOT known.

### Provenance Chain
*Full trace from idea to insight.*

Linked list of all parent artifacts:
- Insight: `<this id>`
- Validation: `<parent validation id>`
- Proposal: `<parent proposal id>`
- Evaluation: `<parent evaluation id>`
- Research: `<parent research id>`
- Idea: `<parent idea id>`

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars. Unique within
  `forge/insights/`.
- Use domain-keyword format for discoverability.
- Example: `maker-checker-reduces-factual-errors.md`

## Example -- Minimal Valid Insight Artifact

```markdown
---
name: maker-checker-reduces-factual-errors
id: 20260815T170000Z
stage: insights
parent: 20260815T160000Z
status: complete
confidence: 0.75
created: 2026-08-15
tags: [maker-checker, verification, error-reduction, harness-design]
---

# [INSIGHT-001] Maker-Checker Gates Reduce Factual Errors

## Principle
Independent verification by a separate model (maker-checker pattern)
reduces factual errors in agent-generated artifacts by an estimated
20-40%, with the largest gains on tasks where the generating model
is overconfident (confidence > 0.7 on weak evidence).

## Evidence Summary
Three pipelines tested this across different artifact types.
Pipeline 1 (code-review): sources A, B, C showed 30% error
reduction when a Haiku validator checked Sonnet-generated code
reviews. Pipeline 2 (research-reports): sources D, E showed 25%
fewer unsupported claims in verified reports. Pipeline 3
(business-analysis): sources F, G showed 35% reduction in
overconfident market size estimates.

Contradiction: source H found that maker-checker adds latency
(2-5 seconds per artifact) which may be unacceptable for
real-time use cases. This is a valid tradeoff, not a refutation.

## Actionability
Suggi can implement this by:
1. Adding forge-verify as a mandatory gate in the forge pipeline
   (already done -- see skills/forge-verify/SKILL.md).
2. Extending the pattern to Ava's artifact writing: before
   committing any brain artifact, a separate model reviews it.
3. Testing different model pairs: which generator-validator
   combinations produce the best error detection rate?

## Confidence
0.75. Three pipelines across different artifact types show
consistent results. Evidence is moderate (2-3 sources per
pipeline). Confidence would increase with: (a) replication on
a 4th artifact type, (b) testing with different model pairs,
(c) measuring over a longer time period (30+ sessions).

## Limitations
- Tested only on text artifacts (code reviews, reports, analyses).
  Not tested on code generation, configuration files, or structured
  data.
- Validator model used was consistently Haiku (fast, cheap). A
  stronger validator may catch more errors but cost more.
- Error reduction measured by manual spot-checking, not automated
  ground-truth comparison. Measurement error possible.
- The 2-5 second latency penalty makes this unsuitable for
  real-time or interactive use cases.

## Provenance Chain
- Insight: `20260815T170000Z` (this file)
- Validation: `20260815T160000Z` (maker-checker-validation)
- Proposal: `20260815T150000Z` (maker-checker-plan)
- Evaluation: `20260815T140000Z` (maker-checker-verdict)
- Research: `20260815T130000Z` (maker-checker-evidence)
- Idea: `20260815T120000Z` (maker-checker-reduces-errors)
```
