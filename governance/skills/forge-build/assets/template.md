---
name: template-forge-build
tier: template
stage: build
version: 2.0
---

# Forge Build Template

Write `forge/builds/<slug>-rNN.md` with this exact section order.

## Frontmatter

```yaml
---
name: <slug>
id: <YYYYMMDDTHHMMSSZ>
pipeline: <idea id>
research_path: <agent-systems|value-investing-systems>
stage: build
owner: Researcher
status: complete
parent: <PASS evaluation or verification return-artifact id>
supersedes: <prior build id or none>
confidence: <0.0-1.0>
created: <YYYY-MM-DDTHH:MM:SSZ>
---
```

## Body

```markdown
# <Title> -- Build Package

## Decision
<What should be built, changed, tested, or adopted; and what should not.>

## Evidence Trace
| Recommendation | Research claim/source | Analyst criterion | Confidence |
|:--|:--|:--|:--|
| <recommendation> | <artifact section/citation> | <criterion> | <value> |

## Design or Framework
<Components, boundaries, interfaces, data flow, or value-investing logic.>

## Simplest Viable Form
<Minimum coherent implementation or framework; optional extensions separate.>

## Implementation Sequence
1. <Specific, dependency-ordered action for a future authorized implementer.>

## Acceptance and Regression Tests
| Test | Method | PASS | HALT |
|:--|:--|:--|:--|
| <test> | <procedure> | <observable result> | <failure condition> |

## Worst Failure and Prevention
<Worst plausible outcome and the structural prevention or containment.>

## Risks and Rollback
| Risk | Trigger | Mitigation | Rollback |
|:--|:--|:--|:--|
| <risk> | <signal> | <action> | <reversal> |

## Alternatives Rejected
- <Alternative, evidence, and reason.>

## Limitations and Open Questions
- <Boundary or unresolved assumption.>

## Human Decisions Required
- <Choice Suggi must make before implementation.>

## Provenance Chain
<Ordered artifact IDs from idea through evaluation.>
```

The package may recommend external changes but performs none. For the value-
investing path, it is a process/framework package, not investment advice.
