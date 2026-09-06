---
name: forge-evaluate
description: "Use when evaluating research or reviewing a proposal."
user-invocable: false
disable-model-invocation: false
---
# Forge Evaluate

Independently review one Researcher artifact in a separate Analyst context.
The same skill handles research evaluation and final proposal review;
there is no third agent or automatic model switch.

## Procedure

1. Run through the Analyst loop and read `forge/protocol.md` and LEARNINGS.
   At `evaluate`, use `governance/template-evaluation.md`; at `final-review`,
   use `governance/template-review.md`. Any other stage is a HALT.
2. Inspect target metadata without reading its body. Read the root/current
   idea and required antecedents: for final review, include the research,
   its evaluation, and prior requested corrections. Record a short baseline
   of expected evidence and failure conditions before opening the target
   body. Do not inherit the Researcher's private reasoning.
3. Read the entire target. Check its actual claims against the baseline,
   primary sources, contrary evidence, and the exact artifact links. Check
   material citations independently; a reflection or earlier verdict does
   not validate a claim merely by repeating it. Unknown is allowed.
4. For research, assess groundedness, coverage, source quality, logical
   soundness, alternatives, and whether a useful change is justified.
   For final review, inspect the actual design, responses to evaluation,
   feasibility, scope drift, unsupported additions, tests, and reversal.
   Do not rerun the whole research project or require ceremonial criticism.
5. Select the target-appropriate verdict and next stage from the protocol.
   Count prior corrective verdicts and any explicit human budget extension
   before requesting another cycle. Name exact blocking questions and what
   evidence would change the decision. A score cannot overrule a blocker.
6. Write one evaluation or review under the corresponding template gate.
   REJECT/DEFER goes directly to `forge/graveyard/`; all other verdicts go
   to `forge/evaluations/`. The verdict itself is the closure record when
   stopping. Do not modify the Researcher's artifact.
7. Only after completing this evaluation or final review, apply the
   admission gate in LEARNINGS. Update an existing method lesson or add
   one only if supported; otherwise leave LEARNINGS unchanged. Return the
   verdict and permitted learning edit to the loop's transaction.

## Verification

Before the verdict write, PASS requires the recorded cold baseline,
independent evidence checks, exact target, explicit disposition within
budget, and the template checklist. Otherwise HALT; no assumed approval.
Afterwards, learning edits independently PASS the LEARNINGS gate or do not
occur. The loop verifies the artifact, cursor, event, and commit together.
