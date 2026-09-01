---
name: template-forge-ideate
tier: template
stage: ideas
version: 1.0
---

# Forge Ideate Template -- Idea Brief Format

## What This Template Defines

The format for Stage 1 artifacts: scoped idea briefs in `forge/ideas/`.
Every idea brief MUST follow this structure exactly. For the writing
procedure and quality gates, see `skills/forge-ideate/SKILL.md`.

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>        # ISO 8601 UTC, generated with date -u +'%Y%m%dT%H%M%SZ'
stage: ideas                   # always ideas
parent: root                   # root if this is a new idea; otherwise id of triggering artifact
status: active                 # active, halted, or complete
confidence: <0.0-1.0>          # initial confidence before research
created: <YYYY-MM-DD>
tags: [<tag>, <tag>]           # lowercase, hyphens for spaces
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, max 60 chars, unique.
- `id` is ISO 8601 UTC. MUST generate with `date -u +'%Y%m%dT%H%M%SZ'`.
  Never estimate, never round. Never reuse.
- `stage` is always `ideas`.
- `parent` is `root` for new ideas. For ideas derived from prior research,
  use the parent artifact's id.
- `status` starts as `active`. Changes to `halted` if the pipeline dies
  here, `complete` when the full pipeline finishes.
- `confidence` is 0.0-1.0 based on prior knowledge before any research.
- `tags` use lowercase, hyphens for spaces.

## Body Structure

### Hypothesis
*What do I think might be true?*

One clear, falsifiable statement. Not a question, not a wish.
"If X is true, then Y follows." The hypothesis MUST be testable
with evidence from web search, brain search, or both.

### Why This Matters
*Why could this be a viable agentic business model?*

The market signal, trend, or gap that inspired this idea. What
problem does it solve? For whom? What evidence (even anecdotal)
suggests this is worth investigating?

### What I Need to Prove
*What specific claims must be true for this to work?*

2-3 specific, falsifiable claims. Each claim should be answerable
with evidence from independent sources. If a claim cannot be tested,
it is not a valid claim -- restate it until it is testable.

### Initial Confidence
*How likely is this to be viable, before research?*

0.0-1.0. Be honest. Low confidence does not make an idea bad --
it makes the uncertainty explicit. State what you would need to
see to raise or lower this confidence.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars. Unique within `forge/ideas/`.
- Example: `ai-powered-code-review-service.md`

## Example -- Minimal Valid Idea Brief

```markdown
---
name: ai-code-review-service
id: 20260801T120000Z
stage: ideas
parent: root
status: active
confidence: 0.4
created: 2026-08-01
tags: [code-review, developer-tools, saas]
---

# [IDEA-001] AI-Powered Code Review as a Service

## Hypothesis
Developers will pay for AI code review that catches bugs their
existing CI/linter pipelines miss, especially logic errors and
security vulnerabilities.

## Why This Matters
The code review market is large (GitHub, GitLab, Bitbucket all
have built-in review). Existing tools catch syntax and style but
miss logic errors. An AI agent that understands code semantics
could fill this gap. Multiple "AI code reviewer" startups raised
funding in 2024-2025, suggesting market validation.

## What I Need to Prove
1. Existing code review tools (CodeRabbit, CodeClimate, SonarQube)
   do NOT catch semantic logic errors at scale -- their scope is
   syntax, style, and known vulnerability patterns.
2. Developers are willing to pay for AI code review beyond what
   their platform already provides.
3. An autonomous agent can perform code review with accuracy
   comparable to a human senior developer on real-world codebases.

## Initial Confidence
0.4. The market signal (funded competitors) is real, but I do not
yet know if they are succeeding or failing. The technical feasibility
of AI code review is plausible given LLM capabilities, but accuracy
on real codebases is unproven.
```
