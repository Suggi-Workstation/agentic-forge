---
name: forge-evaluate
description: "Evaluate Forge research as the Analyst."
user-invocable: false
disable-model-invocation: false
---

# Forge Evaluate -- Analyst Stage 4

Independently decides whether the evidence justifies spending a Researcher
run on a build package. It judges the declared method rather than rewarding
volume or confident prose.

## When to Use

Use only when `STATUS.md` says `stage: evaluate`, `owner: Analyst`, and
names a complete research artifact. Otherwise return `NO-OP` without writes.

## Procedure

1. Read the startup context and
   `governance/skills/forge-evaluate/assets/template.md`.
2. From the idea and proposal, write the expected claim map, acceptance
   tests, and kill criteria before reading the research conclusions.
3. Read the research cold. Check plan execution, every material claim,
   source quality, citation accuracy, contradictory evidence, method
   deviations, and uncertainty.
4. Re-open sources for every disputed or load-bearing claim. Search for
   missing counter-evidence when the report's contradiction search is weak.
5. Test whether the evidence can support a concrete build without claiming
   more than it proves. For value-investing work, require Buffett-Munger
   alignment and separate framework research from security advice.
6. Render exactly one verdict:
   - `PASS`: all load-bearing criteria pass and remaining gaps can be bounded
     inside the build.
   - `HALT-REVISE`: name failed criteria and return to `research` or
     `propose`.
   - `HALT-REJECT`: the question is duplicative, false, infeasible, outside
     the anchor, or fails its kill criteria.
7. Generate a current UTC ID. Write one
   `forge/evaluations/<slug>-rNN.md`; set `parent` to the research artifact
   and `supersedes` when revising an evaluation.
8. Return artifact path, ID, verdict, return stage, and reason to
   `forge-loop-analyst`.

## Evaluation Gate -- HARD GATE

PASS requires all load-bearing checks:

- anchor alignment and non-duplication;
- declared method substantially executed;
- material claims trace to accurately represented sources;
- source quality matches claim consequence;
- contrary evidence and uncertainty are handled honestly;
- proposal acceptance tests pass and kill criteria do not fire; and
- a bounded, actionable build is feasible.

There is no average score that can hide a fatal weakness. Any failed
load-bearing check produces HALT-REVISE or HALT-REJECT.

## Related

- `governance/skills/forge-evaluate/assets/template.md`
- `governance/skills/forge-loop-analyst/SKILL.md`
- `governance/skills/forge-research/SKILL.md`
- `governance/skills/forge-build/SKILL.md`
- `forge/protocol.md`