---
name: template-forge-ideate
tier: template
stage: idea
version: 2.0
---

# Forge Idea Template

Write `forge/ideas/<slug>-r01.md` with this exact section order.

## Frontmatter

```yaml
---
name: <slug>
id: <YYYYMMDDTHHMMSSZ>
pipeline: <same value as id>
research_path: <agent-systems|value-investing-systems>
stage: idea
owner: Researcher
status: complete
parent: root
supersedes: none
confidence: <0.0-1.0>
created: <YYYY-MM-DDTHH:MM:SSZ>
---
```

## Body

```markdown
# <Title>

## Research Path
<Chosen path and why it has the highest current learning value.>

## Research Question
<One narrow, falsifiable question.>

## Hypothesis
<Best current answer before research.>

## Why This Matters
<Decision or capability this could improve.>

## Prior Work and Non-Duplication
<Forge and brain searches performed; closest work and the unresolved gap.>

## Claims to Test
1. <Material claim and what could falsify it.>

## Expected Build
<Concrete framework, skill, protocol, test, architecture, or process package.>

## Kill Criteria
- <Evidence or condition that should stop this pipeline.>

## Initial Confidence
<0.0-1.0 with reason and what would change it.>
```

No invented evidence, generic topic, parallel path, or implementation.