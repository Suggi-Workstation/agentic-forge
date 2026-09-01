---
name: forge-protocol
id: 20260801T000008Z
tier: protocol
author: Link
approved_by: Suggi
version: 1.0
---

# Forge Protocol -- Research-to-Insight Pipeline

## What the Forge Is

The forge is a 6-stage pipeline that converts raw ideas into durable
insights through structured research, evaluation, and validation.
Each stage produces an immutable artifact. Each gate is a binary
decision: PASS (advance to next stage) or HALT (pivot or abandon).

The final output is an INSIGHT -- a transferable principle about
agentic harness optimization that Suggi can review and implement.

## Pipeline

```
IDEA --> RESEARCH --> EVALUATE --> PROPOSE --> VALIDATE --> INSIGHT
  |         |           |            |            |           |
 Gate      Gate        Gate         Gate         Gate        Gate
```

| Stage | Folder | Input | Output | Gate |
|:--|:--|:--|:--|:--|
| 1. Ideate | `ideas/` | Raw insight from research | Scoped idea brief | Novel AND testable? |
| 2. Research | `research/` | Scoped idea brief | Evidence report with sources | Evidence supports? |
| 3. Evaluate | `evaluations/` | Evidence report | PASS/HALT verdict with reasoning | Credible AND viable? |
| 4. Propose | `proposals/` | PASS verdict | Research plan | Concrete AND feasible? |
| 5. Validate | `validations/` | Research plan | Stress-test result | Survives scrutiny? |
| 6. Insight | `insights/` | Validated plan + full chain | Durable principle | Actionable AND transferable? |

## Folder Map

```
forge/
  protocol.md         # this file
  ideas/              # stage 1: scoped idea briefs
  research/           # stage 2: evidence reports
  evaluations/        # stage 3: PASS/HALT verdicts
  proposals/          # stage 4: research plans
  validations/        # stage 5: stress-test results
  insights/           # stage 6: durable, transferable principles
  graveyard/          # definitively dead ideas + post-mortems
  archive/            # completed pipelines (idea through insight)
```

## Entry Format

Every artifact in the forge follows this frontmatter schema:

```yaml
---
id: <ISO-8601-timestamp>
stage: ideas|research|evaluations|proposals|validations|insights|graveyard
parent: <id of the artifact this derives from, or "root">
status: active|halted|complete
confidence: 0.0-1.0
created: <ISO-8601>
---
```

The `parent` field creates a provenance chain. Every artifact links
to the one it was derived from. The full chain from idea to insight is
traceable: `insight -> validation -> proposal -> evaluation -> research -> idea`.

### Stage 1: Idea Brief (`ideas/`)

```
# [IDEA-001] <One-line title>

## Hypothesis
What I think might be true about agentic harness optimization.
One clear, falsifiable statement.

## Why This Matters
Why this could improve agent self-development. What gap in current
understanding this addresses.

## What I Need to Prove
2-3 specific claims that must be true for this to hold.

## Initial Confidence
0.0-1.0, based on prior knowledge before research.
```

### Stage 2: Evidence Report (`research/`)

```
# [RESEARCH-001] <Title matching the idea>

## Sources
At least 3 independent sources per major claim. URL + key excerpt.

## Findings
What the evidence says. Organized by claim from the idea brief.

## Contradictions
Evidence that contradicts the hypothesis. If none, explain why.

## Updated Confidence
0.0-1.0, adjusted for evidence.
```

### Stage 3: Evaluation Verdict (`evaluations/`)

```
# [EVAL-001] <Title>

## Verdict
PASS or HALT. One word, then explanation.

## Criteria
Scored against: novelty, evidence strength, research feasibility,
potential impact on agent design. 1-5 each.

## Strengths
What the evidence supports strongly.

## Weaknesses
What the evidence undermines or what is unknown.

## Recommendation
If PASS: what to focus on in the research plan.
If HALT: graveyard or return to ideas/ with narrowed scope?
```

### Stage 4: Research Plan (`proposals/`)

```
# [PROPOSAL-001] <Title>

## Research Question
What specific question will the pipeline answer?

## Method
How the research will be conducted. What sources, what analysis.

## Expected Insight
What principle is expected to emerge if the hypothesis holds.

## Counter-Hypothesis
What alternative explanation could the evidence support?

## Risk Matrix
Top 3 risks + mitigation for each.
```

### Stage 5: Validation Result (`validations/`)

```
# [VALID-001] <Title>

## Method
How the plan was stress-tested. What criteria were used.

## Result
PASS or HALT for each dimension tested.

## Weak Points Found
What the stress-test revealed as fragile.

## Mitigations Added
What the plan now includes that it did not before.

## Final Confidence
0.0-1.0, after all validation.
```

### Stage 6: Insight (`insights/`)

```
# [INSIGHT-001] <Title>

## Principle
The durable principle discovered. One sentence. Transferable.

## Evidence Summary
What the full provenance chain proved. Key sources and findings.

## Actionability
What Suggi can DO with this insight. Concrete, specific.

## Confidence
0.0-1.0, final confidence in this principle.

## Limitations
What this insight does NOT cover. Boundaries and caveats.

## Provenance Chain
Linked list of all parent artifacts: idea -> research -> eval ->
proposal -> validation
```

## The Graveyard (`graveyard/`)

Ideas that failed a gate definitively. Each entry includes a
post-mortem:

```
# [GRAVE-001] <Title>

## What Died
The idea and its provenance chain.

## Why It Died
Which gate it failed and why.

## What We Learned
The scar. What this failure teaches for future research.

## Could It Be Revived?
Under what conditions (if any) would this idea become viable again?
```

## Gate Rules

1. Every stage transition requires an explicit PASS verdict.
2. A HALT at evaluation: write post-mortem to graveyard/, unless a
   narrowed scope could salvage it (return to ideas/).
3. A HALT at validation: return to proposals/ with specific fixes.
4. A HALT at insight: document what blocked the principle from
   emerging, iterate on the proposal.
5. No artifact is ever deleted. Archives preserve the full chain.

## How the Forge Is Used

Each working session:
1. Read the active pipeline state (or ANCHOR if one exists)
2. If no active pipeline: scan ideas/ for the next to develop
3. If active pipeline: advance it one stage
4. Write the artifact to the appropriate forge/ folder
5. Pass through forge-verify (maker-checker gate)
6. Log progress to logs/progress.log if present
7. Commit + push

## Provenance

Every artifact's `parent` field creates a chain:

```
insights/insight-001.md
  parent: validations/valid-001.md
    parent: proposals/proposal-001.md
      parent: evaluations/eval-001.md
        parent: research/research-001.md
          parent: ideas/idea-001.md
```

This is the forge's audit trail -- every insight is traceable to
its evidence and its origin idea.

---
