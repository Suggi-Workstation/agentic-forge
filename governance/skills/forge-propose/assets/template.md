---
name: template-forge-propose
tier: template
stage: proposal
version: 2.0
---

# Forge Proposal Template

Write `forge/proposals/<slug>-rNN.md` with this exact section order.

## Frontmatter

```yaml
---
name: <slug>
id: <YYYYMMDDTHHMMSSZ>
pipeline: <idea id>
research_path: <agent-systems|value-investing-systems>
stage: proposal
owner: Researcher
status: complete
parent: <idea or return-artifact id>
supersedes: <prior proposal id or none>
confidence: <0.0-1.0>
created: <YYYY-MM-DDTHH:MM:SSZ>
---
```

## Body

```markdown
# <Title> -- Evidence Plan

## Research Question
<Exact question inherited from the idea, narrowed if required.>

## Decision This Research Will Inform
<What the eventual reviewer could decide.>

## Claim and Evidence Map
| Claim | Support evidence | Falsification evidence | Required source quality |
|:--|:--|:--|:--|
| <claim> | <target> | <target> | <primary/best available> |

## Method
1. <Ordered, reproducible step.>

## Source Strategy
<Primary sources, independent corroboration, recency, and optional brain leads.>

## Counter-Hypotheses
- <Plausible alternative and discriminating evidence.>

## Acceptance Tests
- <Binary condition the research must meet.>

## Kill Criteria and Stop Conditions
- <Condition that ends or narrows the pipeline.>

## Worst Failure and Prevention
<How this method could produce a persuasive false answer and the structural check.>

## Execution Bound
<Why this fits one bounded research stage; dependencies and unavailable inputs.>
```