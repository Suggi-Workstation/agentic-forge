---
name: template-forge-evaluate
tier: template
stage: evaluation
version: 2.0
---

# Forge Evaluation Template

Write `forge/evaluations/<slug>-rNN.md` with this exact section order.

## Frontmatter

```yaml
---
name: <slug>
id: <YYYYMMDDTHHMMSSZ>
pipeline: <idea id>
research_path: <agent-systems|value-investing-systems>
stage: evaluation
owner: Analyst
status: complete
parent: <research id>
supersedes: <prior evaluation id or none>
confidence: <0.0-1.0>
created: <YYYY-MM-DDTHH:MM:SSZ>
---
```

## Body

```markdown
# <Title> -- Analyst Evaluation

## Verdict
<PASS|HALT-REVISE|HALT-REJECT>

## Pre-Read Acceptance Baseline
<Claims, acceptance tests, and kill criteria extracted before conclusions.>

## Claim Audit
| Claim | Evidence trace | Source check | Contradiction handling | Result |
|:--|:--|:--|:--|:--|
| <claim> | <citation> | <accurate/gap> | <adequate/gap> | <PASS|HALT> |

## Method and Coverage Audit
<Proposal execution, deviations, source quality, recency, and independence.>

## Build Feasibility
<What a build may safely recommend and what remains unsupported.>

## Failed Criteria
- <None, or exact failed criterion and evidence.>

## Return Stage
<build for PASS; proposal/research for revise; none for reject.>

## Rejection Root Cause and Revival Conditions
<Required for HALT-REJECT; otherwise none.>

## What Was Rejected
<Required for HALT-REJECT; otherwise none.>

## Failed Gate and Evidence
<Required for HALT-REJECT; otherwise none.>

## Provenance Chain
<Ordered artifact IDs from idea through research.>

## Analyst Confidence
<0.0-1.0 and largest remaining uncertainty.>
```

There is no compensating average: any failed load-bearing criterion blocks
PASS.