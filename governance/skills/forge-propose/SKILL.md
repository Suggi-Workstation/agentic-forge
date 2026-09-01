---
name: forge-propose
description: "Design the evidence plan for a Forge idea."
user-invocable: false
disable-model-invocation: false
---

# Forge Propose -- Researcher Stage 2

Turns an accepted idea into an executable evidence plan. Proposal precedes
research so the later report can be checked against a declared method.

## When to Use

Use only when `STATUS.md` says `stage: propose`, `owner: Researcher`, and
the named idea chain resolves. A revision may supersede an older proposal.

## Procedure

1. Read the startup context, active idea, any Analyst return criteria, and
   `governance/skills/forge-propose/assets/template.md`.
2. Invoke `forge-loop-feynman` on the method, not on the desired conclusion.
3. Convert the idea into a claim map: each material claim, evidence that
   could support it, evidence that could falsify it, and source quality
   required.
4. Define the method, search strategy, primary-source targets, independent
   corroboration, contradiction search, and how uncertainty will be handled.
5. Define acceptance tests and kill criteria before gathering evidence.
   The plan must fit one bounded research stage; narrow the question if not.
6. Identify dependencies, likely blind spots, and the worst way the method
   could produce a convincing but false conclusion. Add a prevention check.
7. Generate a current UTC ID. Write one
   `forge/proposals/<slug>-rNN.md`. Set `parent` to the idea or the artifact
   named by the return transition and `supersedes` to the previous proposal
   ID when revising.
8. Return artifact path, ID, and gate reason to `forge-loop-researcher`.

## Proposal Gate -- HARD GATE

PASS only when:

- every material idea claim appears in the claim map;
- support and falsification evidence are both defined;
- source quality is appropriate to the claim;
- method steps and dependencies are executable in one bounded run;
- acceptance tests, kill criteria, and stop conditions are explicit;
- counter-hypotheses are plausible rather than strawmen; and
- the output remains a review package, not an external implementation.

HALT on any missing item. Operational failure returns to the loop; it does
not create a fake proposal or Analyst verdict.

## Related

- `governance/skills/forge-propose/assets/template.md`
- `governance/skills/forge-ideate/SKILL.md`
- `governance/skills/forge-research/SKILL.md`
- `forge/protocol.md`