---
name: template-forge-verify
tier: template
stage: verification
version: 2.0
---

# Forge Verification Template

Write `forge/verifications/<slug>-rNN.md` with this exact section order.

## Frontmatter

```yaml
---
name: <slug>
id: <YYYYMMDDTHHMMSSZ>
pipeline: <idea id>
research_path: <agent-systems|value-investing-systems>
stage: verification
owner: Analyst
status: complete
parent: <build id>
supersedes: <prior verification id or none>
confidence: <0.0-1.0>
created: <YYYY-MM-DDTHH:MM:SSZ>
---
```

## Body

```markdown
# <Title> -- Analyst Verification

## Verdict
<PASS|HALT-REVISE|HALT-REJECT>

## Pre-Read Acceptance Baseline
<Accepted claims and tests extracted before judging the build body.>

## Claim Traceability
| Build claim | Evidence location | Representation accurate | Result |
|:--|:--|:--|:--|
| <claim> | <artifact/source> | <yes/no with reason> | <PASS|HALT> |

## Design Consistency Audit
<Recommendation, architecture/framework, sequence, dependencies, and limits.>

## Test and Rollback Audit
<Whether acceptance tests detect failure and rollback is real and sufficient.>

## Safety and Confinement Audit
<Worst failure, prevention, external-write boundary, and human approvals.>

## Failed Criteria
- <None, or exact failed criterion and evidence.>

## Return Stage
<review for PASS; build/research/proposal for revise; none for reject.>

## Rejection Root Cause and Revival Conditions
<Required for HALT-REJECT; otherwise none.>

## What Was Rejected
<Required for HALT-REJECT; otherwise none.>

## Failed Gate and Evidence
<Required for HALT-REJECT; otherwise none.>

## Provenance Chain
<Ordered artifact IDs from idea through build.>

## Analyst Confidence
<0.0-1.0 and largest remaining uncertainty.>
```

PASS means review-ready, not approved for implementation.
