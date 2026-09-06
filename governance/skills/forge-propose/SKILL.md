---
name: forge-propose
description: "Use when drafting an evidence-backed Forge proposal."
user-invocable: false
disable-model-invocation: false
---
# Forge Propose

Turn evaluated evidence into a concrete blueprint for Suggi. This is the
proposal artifact, not a research-plan stage and not implementation.
Use `forge/protocol.md` and `governance/template-proposal.md`.

## Procedure

1. Run only through `forge-loop-research` at `propose`. Read LEARNINGS, the
   root/current idea, current research and its exact ADVANCE evaluation,
   and any revision request or human decision. HALT if the evaluation
   covers a different research revision or has unresolved blocking work.
2. Use `governance/skills/forge-loop-feynman/SKILL.md` to explain the smallest
   useful change and what would invalidate it. Address every material
   evaluation finding: accepted and fixed, disputed with evidence, or
   unresolved and blocking. A reasoned disagreement still needs review.
3. Describe the proposed change and actual affected interfaces/files,
   alternatives, scope/non-goals, dependencies, ordered implementation,
   acceptance/regression checks, worst failure, and reversal. Label new
   files as proposed; do not imply they exist or tests have already run.
4. If new decision-critical evidence is needed, request evaluation
   of the current research through the protocol's evidence-gap handoff;
   record the exact gap and write no proposal. Evaluation decides the bounded
   research correction or closure. Do not self-authorize more research or
   hide a research gap in implementation detail.
5. Complete the proposal template and write one file in `forge/proposals/`.
   Link the exact research, evaluation, and any reviewed prior proposal.
   Leave all previous artifacts unchanged. Return it to the loop for the
   final-review handoff; never claim approval or start implementation.

## Verification

Before writing, PASS requires a matching ADVANCE evaluation, explicit
responses, an evidence-supported implementable scope, and the complete
proposal checklist. Otherwise HALT the proposal or make the documented
evidence-gap handoff. LEARNINGS is read-only here; no runtime changes occur.
