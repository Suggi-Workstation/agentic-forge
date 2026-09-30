---
name: forge-proposal-claim-verification-map
id: 20260930T173859Z
tier: idea
pipeline: 20260930T173859Z
author: Analyst
tags: [agent-systems, forge, proposals, verification]
links:
  - ANCHOR.md
  - forge/protocol.md
  - LEARNINGS.md
  - governance/template-proposal.md
  - governance/skills/forge-propose/SKILL.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r01.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r02.md
  - forge/final-reviews/bounded-index-freshness-recheck-review-r02.md
  - forge/ideas/forge-history-duplicate-receipt-r01.md
  - agentic-brain:library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md
  - agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md
  - https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix
  - https://www.nasa.gov/reference/5-3-product-verification
confidence: low
---
# Forge Proposal Claim-to-Verification Map

## Question and Value

Can a compact claim-to-verification map in the Forge proposal gate expose
unobservable result claims, incorrectly ordered resource gates, and unsupported
no-action assertions before final review, without forcing a large test matrix on
proposals that do not make procedural or resource-bound claims?

The target improvement is the proposal-writing contract in
`governance/template-proposal.md` and, only if needed to make that contract
usable, its execution procedure in `governance/skills/forge-propose/SKILL.md`.
Forge proposal authors, independent reviewers, and Suggi benefit if a blueprint
shows how each decision-relevant normative claim can be checked before the
proposal consumes a corrective cycle. This is direct ANCHOR Path A work on agent
skills, self-correction, and a confirmed Forge method lesson.[1][2][3]

The observed problem is narrow. The current template requires observable
acceptance, regression, and negative checks, and the propose skill requires an
implementable scope. Neither requires a trace from each material normative
claim, resource boundary, operation order, or prohibited action to its exact
predicate and controls.[3] In pipeline `20260930T124036Z`, final review of r01
found a body-producing call before its byte gate and no running-command deadline
predicate. Final review of r02 then found four remaining blockers: the actual
output sink could cross its stated ceiling, in-process work could cross the
whole-driver deadline, command-only traces could not expose all claimed calls,
and a partial clone could lazy-fetch despite the no-network/no-write claim.
These two reviews are repeated evidence from one pipeline, not independent
trials.[2][4]

The provisional hypothesis is that a short, bidirectional map from claim to
verification method, observable predicate, positive control, negative
counterexample, and operation order would have exposed those contradictions
before final review. A credible alternative is that the current checklist and
high-confidence lesson are already sufficient, and that another table would add
ceremony without improving author behavior. The idea is not worth pursuing if a
predeclared map misses any known blocker, falsely blocks the READY bounded-
freshness proposal, merely restates its acceptance matrix, or cannot remain a
small template or skill amendment with no checker, runtime, or deployment
component.[2][3][5]

## Origin and Prior Work

This is direct ideation under ANCHOR Path A, Agent Systems. Discovery and method
memory preceded the provisional explanation. `LEARNINGS.md` records at high
confidence that evaluator and checker controls must be derived from the claimed
result contract, with resource gates placed before the consuming operation and
prohibited later actions made observable. The same lesson records both a
successful corrected application in pipeline `20260930T083956Z` and the later
proposal-order failures in pipeline `20260930T124036Z`.[2]

At starting HEAD `3e2c9f2dc403f2df389b7c57f401f6146f05cb66`, the duplicate
check enumerated every current Markdown file in `forge/ideas/`,
`forge/proposals/`, and `forge/graveyard/`, searched the candidate and synonyms
through the fresh Forge hybrid index, inspected active progress through ENT-015,
and checked reachable idea additions in Git history. The current tree contained
two ideas, three proposals, and no graveyard Markdown. Reachable history named
six substantive root ideas: maintenance capex, SBC buyback, transaction checker,
unattended command paths, bounded freshness, and history duplicate receipt.[6]

The closest historical overlap is the transaction-checker pipeline. Its root
asked whether a read-only checker could validate artifact, STATUS, and progress-
event agreement after a stage transaction. Its r03 checker reproduced its
synthetic matrix but falsely rejected a valid current record; the exhausted-
budget evaluation closed DEFER and required a human extension plus real-record
controls and comparative value before reopening.[6] This candidate neither
reopens that pipeline nor proposes an executable checker. It asks whether a
manual pre-write proposal map can expose contradictions between a blueprint's
own claims and tests. The target, lifecycle point, artifact, and failure mode are
different.

The bounded-freshness pipeline is a positive comparison, not a duplicate. Its
READY review found that the proposal's trigger, action, negative cases, and
invocation counts were mapped to observable outcomes while unperformed shell
work remained explicitly future work.[5] The active history-receipt pipeline is
the negative comparison: two successive proposal revisions contained extensive
acceptance text but still lacked complete bidirectional coverage of claimed
resource and no-action boundaries.[4]

The historical unattended-command proposal reached READY but has no explicit
recorded human disposition. It already addresses authoritative command denial,
route selection, and no-bypass behavior, so the repeated scratch-cleanup lead is
not a distinct new question. The current bounded-freshness discovery remains
pending human review, and the history-receipt pipeline remains active at
`propose`. No explicit accepted Forge proposal was found in the current or
reachable historical progress evidence inspected.[6][10]

Brain prior work supports the method without deciding the local change. Systems
engineering links requirements to verification methods and acceptance criteria,
while agent-observability work warns that a trace proves only the operations its
instrumentation emits.[7] NASA's example verification matrix likewise assigns
each requirement a unique source and verification approach; its product-
verification guidance says acceptance criteria should be identified for each
requirement and results traced back to them.[8][9] These sources support a bounded
traceability experiment, not a mandatory large matrix for every Forge proposal.

The strongest alternative candidate was a direct study of repeated safety-
blocked scratch cleanup. It lost because the prior unattended-command pipeline
already covers authoritative denials and has an unresolved recorded human
disposition. A conversion of the historical-identity lesson also lost because
pipeline `20260930T124036Z` is already actively proposing that improvement.[6]

## Research Plan

Use one frozen, scratch-only retrospective comparison. Do not edit the proposal
template, skill, reviewed artifacts, or runtime during research.

1. Freeze the current template, propose skill, high-confidence lesson, the two
   history-receipt proposals and reviews, and the bounded-freshness READY
   proposal and review. Record the known review outcomes before constructing the
   instrument; this is a retrospective diagnostic, not a blind trial.
2. Before applying it to any target, define a compact map with one row per
   decision-relevant normative claim or grouped invariant. Candidate fields are
   claim ID and source passage, required operation and order, observable
   predicate, valid positive control, failure-directed negative case, prohibited
   later action, and evidence state (`performed`, `future`, or `unknown`). Permit
   `not applicable` with a reason so descriptive and non-procedural proposals do
   not inherit ceremonial rows.
3. Apply the unchanged map to history-receipt r01 and r02, using the completed
   reviews as disclosed answer keys rather than claiming a blind test. Grade
   whether a mechanical application marks each of the six known blockers as an
   absent, contradictory, or unverifiable mapping, and preserve every filled
   map and classification.
4. Apply the same map to bounded-freshness r02 as a positive control. It should
   trace the material trigger, state-race, cleanup, query, rollback, and future-
   test claims without converting disclosed unperformed implementation work into
   a blocker. Record any redundant or false-blocking row.
5. Have a separate reader use the frozen artifacts and map to reproduce every
   classification. Compare the result with the current checklist alone, doing
   nothing, prose-only strengthening of the existing lesson, and an executable
   checker. The checker remains excluded unless separately researched and
   authorized; the historical DEFER is counterevidence against automation.[6]
6. Measure map rows, words, completion time, disagreements, blockers detected,
   false blockers, and claims that cannot be classified. Identify the smallest
   wording that preserves the useful fields and whether the target should be the
   template alone or the template plus one propose-skill instruction.
7. Stop without a proposal if the map adds no detection over an explicit reading
   of the current checklist, if authors cannot identify the complete claim set,
   if the positive control is falsely blocked, if classifications are not
   reproducible, or if usefulness requires a script, repository-wide validator,
   runtime gate, or new lifecycle state.

Research supports a proposal only if the predeclared map exposes all six known
history-receipt blockers, produces no unresolved false blocker for the READY
bounded-freshness proposal, and a separate reader reproduces the classifications
from the same frozen artifacts. It must demonstrate incremental value over the
current checklist and fit as one concise, reversible template or skill gate.
The research must report retrospective and same-pipeline limits rather than
claiming a measured reduction in future revision rates.

Confidence is low. Two reviews directly show a gap between broad acceptance
language and complete claim coverage, another pipeline supplies a positive
comparison, and the current template lacks explicit bidirectional mapping.[2]
[3][4][5] Confidence remains low because the negative cases come from one
complex pipeline, the desired outcome is already known, author compliance may
be the real cause, and the map has not been tested. Confidence would rise if the
frozen comparison detects every blocker without a positive-control false alarm
and a separate reader reproduces the result. It would fall if the existing
checklist performs equally, the map depends on hindsight, or the added structure
becomes larger than the proposal defects it is meant to prevent.

## Sources

1. `ANCHOR.md` -- Path A mission fit, confirmed-learning prompt, selection
   criteria, smallest-test preference, and no-duplicate boundary. [high]
2. `LEARNINGS.md` -- high-confidence claimed-result-contract lesson,
   pre-consumption resource gates, observable prohibited actions, positive and
   negative controls, and current evidence-pipeline limits. [high]
3. `governance/template-proposal.md` -- current proposal sections, observable
   acceptance requirement, checklist, and separate-authorization boundary.
   [high]
   - `governance/skills/forge-propose/SKILL.md` -- current proposal procedure,
     implementation-detail, acceptance, feedback, and handoff gates. [high]
4. `forge/final-reviews/forge-history-duplicate-receipt-review-r01.md` -- first
   proposal-only REVISE, body-before-byte and unenforced-deadline blockers, and
   required claim-to-predicate correction. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r02.md` -- second
     proposal-only REVISE, sink-byte, in-process deadline, trace-coverage, and
     partial-clone blockers. [high]
5. `forge/final-reviews/bounded-index-freshness-recheck-review-r02.md` -- READY
   positive comparison with mapped trigger, action, invocation-count, negative,
   rollback, and future-test boundaries. [high]
6. `forge/ideas/forge-history-duplicate-receipt-r01.md` -- verified current and
   reachable-history duplicate scope, historical dispositions, and unresolved
   unattended-command decision. [high]
   - `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- historical
     post-write checker question, manual alternative, and automation boundary,
     verified at Git commit `4bc2896bf5398e36dec2f4ec2ffc3791efaec554`.
     [high]
   - `forge/graveyard/evidence-gated-forge-transaction-checker-evaluation-r03.md`
     -- historical DEFER closure, real-record false rejection, exhausted budget,
     and reopening conditions, verified at Git commit
     `ee82fca6dc9c6ab654ffb294152a5f12756ecb6c`. [high]
7. `agentic-brain:library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md` -- requirements-to-verification traceability, acceptance criteria, configuration identity, and proportional tailoring. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md` -- instrumentation-coverage limits, observable predicates, and separation of outcome, process, and operational evidence. [medium]
8. National Aeronautics and Space Administration. "Appendix D: Requirements
   Verification Matrix," NASA Systems Engineering Handbook, accessed 2026-09-30.
   Unique requirement source and verification-approach fields were checked.
   https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix
   [high]
9. National Aeronautics and Space Administration. "5.3 Product Verification,"
   NASA Systems Engineering Handbook, page updated 2023-09-29; accessed
   2026-09-30. Per-requirement acceptance criteria, verification methods, and
   result traceability were checked.
   https://www.nasa.gov/reference/5-3-product-verification [high]
10. `forge/protocol.md` -- duplicate and reopening rules, exact human decisions,
   artifact contract, board selection, and one-stage transaction boundary.
   [high]
   - `STATUS.md` -- two preserved open rows and their exact current dispositions
     at starting HEAD `3e2c9f2dc403f2df389b7c57f401f6146f05cb66`.
     [high]
   - `logbook/progress.log` -- current stage evidence through ENT-015 and no
     explicit accepted-proposal decision at the same starting HEAD. [high]
