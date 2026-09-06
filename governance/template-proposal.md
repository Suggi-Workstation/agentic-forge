# Proposal Template

Use the Artifact Contract in `forge/protocol.md`. Tier: `proposal`.
Destination: `forge/proposals/`. Link the root/current idea, current research
and its ADVANCE evaluation, previous proposal revision, and review/decision
feedback when present. This file requests a decision; it does not grant one.

## Proposed Decision

State the problem, beneficiary, proposed improvement, and exact decision
requested from Suggi. Name the output type: skill, architecture, framework,
core-file/rule amendment, or another concrete change. Define non-goals.

## Evidence, Alternatives, and Evaluation Response

Explain the rationale and contrary evidence. Compare reuse, a smaller
change, and doing nothing. Answer every material evaluation/review finding
with a correction or reasoned evidence-backed disagreement. Name remaining
uncertainties; an unresolved decision-critical blocker prevents submission.

## Change Specification and Implementation

Identify affected files/interfaces, current behavior, intended behavior,
dependencies, and ordered implementation steps. Distinguish existing
components from proposed ones. Supply enough detail for an implementer,
scaled to the change: exact wording for a rule; triggers/procedure for a
skill; interfaces/migration for architecture. No speculative machinery.

## Acceptance, Risks, and Reversal

Specify observable acceptance and regression checks, including when the
new behavior must not occur. Identify the worst plausible failure and its
prevention, costs/tradeoffs, rollback or reversal, and residual uncertainty.
Distinguish checks already performed during research from future tests.
Implementation and deployment remain separately authorized work.

## Checklist -- Before Writing

PASS requires every item; any missing item HALTs proposal creation.

- [ ] Metadata and exact evaluated-research/revision links meet the protocol.
- [ ] Current research has a matching ADVANCE evaluation; blockers resolved.
- [ ] Feedback, evidence, counterevidence, alternatives, and non-goals included.
- [ ] Change specification is feasible and detailed enough to implement.
- [ ] Acceptance/regression/negative tests and worst-case reversal specified.
- [ ] Future work is not claimed as performed, approved, or deployed.
