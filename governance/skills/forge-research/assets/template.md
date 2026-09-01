---
name: template-forge-research
tier: template
stage: research
version: 2.0
---

# Forge Research Template

Write `forge/research/<slug>-rNN.md` with this exact section order.

## Frontmatter

```yaml
---
name: <slug>
id: <YYYYMMDDTHHMMSSZ>
pipeline: <idea id>
research_path: <agent-systems|value-investing-systems>
stage: research
owner: Researcher
status: complete
parent: <proposal or Analyst return-artifact id>
supersedes: <prior research id or none>
confidence: <0.0-1.0>
created: <YYYY-MM-DDTHH:MM:SSZ>
---
```

## Body

```markdown
# <Title> -- Evidence Report

## Method Execution
<What was run, deviations from proposal, and why.>

## Source Register
| Source | Date | Type | Claim use | Location |
|:--|:--|:--|:--|:--|
| <publisher/title> | <date> | <primary/secondary/brain> | <claim> | <URL or agentic-brain:path> |

## Findings by Claim
### Claim 1 -- <supported|contradicted|unresolved>
<Facts, interpretation, citations, and evidence quality.>

## Contradictory Evidence and Counter-Hypotheses
<Strongest contrary case; what discriminates between explanations.>

## Acceptance Tests and Kill Criteria
| Criterion | Result | Evidence |
|:--|:--|:--|
| <criterion> | <PASS|HALT|UNRESOLVED> | <citation> |

## Gaps, Limitations, and Method Deviations
<Missing evidence, recency limits, conflicts, and implications.>

## Research Conclusion
<What the evidence permits and does not permit the build to claim.>

## Updated Confidence
<0.0-1.0, change from idea, and sensitivity.>
```

Every cited source must have been read. Source count never substitutes for
source quality or claim coverage.