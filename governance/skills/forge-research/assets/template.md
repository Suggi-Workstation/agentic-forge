---
name: template-forge-research
tier: template
stage: research
version: 1.0
---

# Forge Research Template -- Evidence Report Format

## What This Template Defines

The format for Stage 2 artifacts: evidence reports in `forge/research/`.
Every evidence report MUST follow this structure exactly. For the writing
procedure and quality gates, see `skills/forge-research/SKILL.md`.

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>        # ISO 8601 UTC, generated with date -u +'%Y%m%dT%H%M%SZ'
stage: research                # always research
parent: <id>                   # id of the idea brief this researches
status: active                 # active, halted, or complete
confidence: <0.0-1.0>          # updated confidence after research
created: <YYYY-MM-DD>
tags: [<tag>, <tag>]           # lowercase, hyphens for spaces
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, max 60 chars, unique.
- `id` is ISO 8601 UTC. MUST generate with `date -u +'%Y%m%dT%H%M%SZ'`.
  Never estimate, never round. Never reuse.
- `stage` is always `research`.
- `parent` is the exact `id` of the idea brief this research addresses.
  The provenance chain starts here: research -> idea.
- `status` starts as `active`. Changes to `halted` if the pipeline dies
  here, `complete` when the full pipeline finishes.
- `confidence` is 0.0-1.0 adjusted for the evidence found.
- `tags` use lowercase, hyphens for spaces.

## Body Structure

### Sources
*What evidence was found?*

At least 3 independent sources per major claim from the idea brief.
For each source: URL, publication date, key excerpt. If a source is
behind a paywall but the abstract or summary is accessible, note that.
If fewer than 3 sources exist for a claim, state that explicitly --
this is evidence, not failure.

### Findings
*What does the evidence say?*

Organized by claim from the idea brief's "What I Need to Prove"
section. For each claim:
- Finding: what the sources say, collectively.
- Evidence strength: strong (multiple independent sources agree),
  moderate (some agreement, some gaps), weak (single source or
  conflicting sources), or none (no evidence found).
- Source citations: which sources support this finding.

### Contradictions
*What evidence contradicts the hypothesis?*

If any evidence contradicts the hypothesis, state it explicitly.
If no contradictions were found, state that and explain: was the
search thorough? Is contradictory evidence unlikely for this domain?
Hiding contradictions is a gate failure.

### Updated Confidence
*How likely is this to be viable, after research?*

0.0-1.0. Compare to the initial confidence from the idea brief.
Explain what changed and why. If confidence decreased, state what
would need to be true for it to recover.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars. Unique within `forge/research/`.
- Ideally matches the parent idea brief slug for traceability.
- Example: `ai-code-review-service-evidence.md`

## Example -- Minimal Valid Evidence Report

```markdown
---
name: ai-code-review-service-evidence
id: 20260801T130000Z
stage: research
parent: 20260801T120000Z
status: active
confidence: 0.55
created: 2026-08-01
tags: [code-review, developer-tools, saas]
---

# [RESEARCH-001] AI Code Review Service -- Evidence Report

## Sources

### Claim 1: Existing tools do not catch semantic logic errors
1. "CodeRabbit Review Capabilities" (coderabbit.ai, 2026-03)
   -- Documents supported checks: syntax, style, security patterns.
   Explicitly states it does NOT perform semantic analysis.
2. "SonarQube Rules List" (sonarsource.com, 2026-01)
   -- 600+ rules catalogued. All are pattern-based (style, bug
   patterns, vulnerabilities). None are semantic logic checks.
3. "State of Code Review 2025" (Greptile blog, 2025-11)
   -- Survey of 500 developers: 72% said their automated tools
   miss logic errors. "Tools catch syntax, humans catch logic."

### Claim 2: Developers will pay for AI code review
1. "CodeRabbit raises $16M Series A" (TechCrunch, 2025-06)
   -- $16M at ~$80M valuation. Suggests market validation.
2. "Developer Tools Spending Report 2025" (SlashData, 2025-09)
   -- Average developer team spends $1,200/year on code quality
   tools. Top quartile spends $5,000+.
3. "Cursor and the AI Developer" (a16z, 2025-12)
   -- Developers paying $20-40/month for AI coding assistants.
   Code review is a natural extension.

### Claim 3: AI can match human code review accuracy
1. "LLMs for Code Review: A Systematic Study" (arXiv 2025-08)
   -- GPT-4 catches 67% of bugs found by human reviewers.
   Claude catches 71%. Combined: 82%.
2. "CR-Scope: Benchmarking AI Code Review" (arXiv 2026-01)
   -- Best AI models score 0.74 F1 on bug detection vs. 0.82
   for senior developers. Gap is narrowing.
3. Only 2 sources found; this claim has moderate evidence.

## Findings

### Claim 1: Tools miss semantic logic errors -- STRONG
All three sources confirm: existing tools are pattern-based, not
semantic. The gap is real and documented by both vendor docs and
developer surveys. Evidence strength: strong.

### Claim 2: Developers will pay -- MODERATE
Market exists (CodeRabbit, general dev tools spending), but no
direct evidence of willingness to pay FOR AI code review specifically
vs. the broader AI coding assistant category. Evidence strength:
moderate.

### Claim 3: AI matches human accuracy -- MODERATE
LLMs are approaching but not yet matching senior developers. Gap
is narrow (0.74 vs 0.82 F1). Only 2 sources -- third source needed.
Evidence strength: moderate.

## Contradictions
- The a16z article notes that AI coding assistants (Cursor, Copilot)
  are already absorbing code review features. This could limit the
  addressable market for a standalone code review service.
- The arXiv study notes that LLMs perform poorly on large codebases
  (>10K LOC) due to context window limitations.

## Updated Confidence
0.55 (up from 0.40). The tool gap is real and well-documented. The
market signal is positive but the competitive threat from AI coding
assistants absorbing review features is a real risk. Technical
feasibility is plausible but not yet proven at scale.
```
