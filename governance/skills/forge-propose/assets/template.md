---
name: template-forge-propose
tier: template
stage: proposals
version: 1.0
---

# Forge Propose Template -- Implementation Plan Format

## What This Template Defines

The format for Stage 4 artifacts: implementation plans in
`forge/proposals/`. Every plan MUST follow this structure exactly.
For the writing procedure and quality gates, see
`skills/forge-propose/SKILL.md`.

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>        # ISO 8601 UTC, generated with date -u +'%Y%m%dT%H%M%SZ'
stage: proposals                # always proposals
parent: <id>                   # id of the evaluation verdict this builds on
status: active                 # active, halted, or complete
confidence: <0.0-1.0>          # confidence in this plan
created: <YYYY-MM-DD>
tags: [<tag>, <tag>]           # lowercase, hyphens for spaces
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, max 60 chars, unique.
- `id` is ISO 8601 UTC. MUST generate with `date -u +'%Y%m%dT%H%M%SZ'`.
  Never estimate, never round. Never reuse.
- `stage` is always `proposals`.
- `parent` is the exact `id` of the evaluation verdict this plan
  addresses. Provenance: proposal -> evaluation -> research -> idea.
- `status` starts as `active`. Changes to `halted` if validation fails
  fatally, `complete` when built.
- `confidence` is 0.0-1.0 reflecting confidence in this plan's
  feasibility.
- `tags` use lowercase, hyphens for spaces.

## Body Structure

### Problem
*What problem does this solve, and for whom?*

One to three sentences. Must reference the evidence from the research
stage. What is broken, missing, or underserved? Who experiences the
pain? How do they solve it today?

### Solution
*How does this work? What is the technical architecture?*

Describe the solution in concrete terms. What does the system do?
How does the user interact with it? What are the core components?
Include enough detail that another agent could build a prototype
from this description.

### Business Model
*How does this make money? What are the unit economics?*

Revenue model: subscription, usage-based, marketplace, advertising,
or other. Pricing: per-user, per-usage, tiered. Cost structure:
what are the major cost drivers? Unit economics: revenue per
customer minus cost per customer.

### Competitive Moat
*Why is this defensible? What prevents copying?*

Moat sources: network effects, data advantages, switching costs,
brand, economies of scale, regulatory barriers, or intellectual
property. Be specific -- "better UX" is not a moat. Reference
the competitive analysis from the evidence report.

### Implementation Steps
*What are the concrete steps to build this?*

Ordered list. Each step is one concrete, verifiable action. Another
agent should be able to execute these steps sequentially. Include
estimated effort for each step (hours/days).

### Risk Matrix
*What could go wrong, and how is each risk mitigated?*

Top 3-5 risks, each with:
- Risk: what could fail
- Likelihood: low/medium/high
- Impact: low/medium/high
- Mitigation: what reduces the likelihood or impact

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars. Unique within
  `forge/proposals/`.
- Example: `ai-code-review-service-plan.md`

## Example -- Minimal Valid Implementation Plan

```markdown
---
name: ai-code-review-service-plan
id: 20260801T150000Z
stage: proposals
parent: 20260801T140000Z
status: active
confidence: 0.60
created: 2026-08-01
tags: [code-review, developer-tools, saas]
---

# [PROPOSAL-001] AI Code Review Service -- Implementation Plan

## Problem
Development teams rely on automated tools (linters, SAST) that catch
syntax and known vulnerability patterns but miss semantic logic errors.
The human code review bottleneck slows deployment. An AI agent that
understands code semantics can fill this gap, as documented in the
evidence report (parent: 20260801T130000Z).

## Solution
A GitHub App that performs automated semantic code review on every
pull request. The agent analyzes code changes for logic errors,
edge cases, and security vulnerabilities using an LLM with code
understanding capabilities. Results are posted as inline PR comments.

Core components:
1. GitHub App webhook receiver -- triggers on PR events
2. Code analysis engine -- diffs the PR, chunks large files, sends
   to LLM with review prompt
3. Review output formatter -- converts LLM output to GitHub PR
   review comments
4. Dashboard -- tracks review history, accuracy metrics, team usage

## Business Model
- Freemium: free for public repos (5 PRs/month), paid for private
  repos and higher volume.
- Pricing: $29/month for individuals, $99/month for teams (up to
  10 developers), $499/month for enterprises.
- Cost: LLM API calls (~$0.50 per PR review), hosting (~$50/month),
  GitHub App infrastructure.
- Unit economics: at $99/team/month, with 50 PRs per team per month
  ($25 in API costs), gross margin ~75%.

## Competitive Moat
- Data advantage: review accuracy improves with more PRs reviewed.
  Early mover accumulates training data for fine-tuning.
- Integration depth: deep GitHub integration creates switching costs.
- Brand/trust: developers trust a tool that consistently catches
  real bugs their linter misses.
- Weakness: features can be copied. Moat is moderate at best.

## Implementation Steps
1. Build GitHub App skeleton with webhook receiver (2 days).
2. Implement PR diff extraction and chunking (1 day).
3. Build LLM review prompt and output parser (2 days).
4. Implement PR comment posting via GitHub API (1 day).
5. Build usage dashboard (1 day).
6. Deploy to VPS, test with own repos (1 day).
7. Submit to GitHub Marketplace (1 day).
Total: ~9 days for MVP.

## Risk Matrix

| Risk | Likelihood | Impact | Mitigation |
|:--|:--|:--|:--|
| LLM accuracy insufficient for real codebases | Medium | High | Start with narrow language support (Python only); expand with evidence |
| GitHub rate limits block PR comment posting | Low | Medium | Use batch commenting, respect rate limit headers |
| AI coding assistants absorb this feature | High | Medium | Differentiate on depth (semantic review) and integration (native GitHub) |
| No willingness to pay at proposed price points | Medium | High | Validate with landing page + waitlist before full build |
```
