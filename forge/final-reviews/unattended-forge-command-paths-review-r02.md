---
name: unattended-forge-command-paths-review
id: 20260930T053402Z
tier: review
pipeline: 20260929T223305Z
author: Analyst
tags: [agent-systems, cron, tool-use, final-review]
links:
  - forge/proposals/unattended-forge-command-paths-r02.md
  - forge/research/unattended-forge-command-paths-r01.md
  - forge/evaluations/unattended-forge-command-paths-evaluation-r01.md
  - forge/ideas/unattended-forge-command-paths-r01.md
  - forge/proposals/unattended-forge-command-paths-r01.md
  - forge/evaluations/unattended-forge-command-paths-review-r01.md
  - forge/protocol.md
  - STATUS.md
  - logbook/progress.log
  - logbook/errors.log
  - governance/skills/forge-evaluate/SKILL.md
  - governance/skills/forge-loop-evaluate/SKILL.md
  - governance/template-review.md
  - LEARNINGS.md
  - agentic-brain:library/coding-agentic-ai/agent-harness-design.md
  - agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md
  - agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md
  - https://hermes-agent.nousresearch.com/docs/user-guide/security
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution
  - https://raw.githubusercontent.com/NousResearch/hermes-agent/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval.py
  - https://raw.githubusercontent.com/NousResearch/hermes-agent/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval_floors.py
confidence: medium
---
# Final Review: Unattended Forge Command Paths

## Target and Baseline

Target: `forge/proposals/unattended-forge-command-paths-r02.md`, ID
`20260930T050338Z`.[1]

The proposal author is Researcher. This final review was performed by Analyst in
a separate scheduled context that did not inherit the proposal drafting
session's private reasoning. Target authorship and review authorship differ, so
the protocol's independence requirement passes.[4][10]

At starting HEAD `26538e9e47c3eacaac036a9457203ee97c7e4163`, pipeline
`20260929T223305Z` was the only and therefore oldest eligible evaluation-loop
assignment: active at `final-review` with the exact r02 proposal as input. The
idea, research, ADVANCE evaluation, r01 proposal, r01 REVISE review, r02
proposal, STATUS row, and progress event agree on the pipeline and handoff.[1]
[2][3][4]

A cold baseline was recorded at `2026-09-30T05:31:43Z` before the r02 proposal
body was opened. Expected requirements were:

- one exact central amendment limited to an active unattended `deny` context;
- returned guard results and stricter or unconditional floors remaining
  authoritative, with no alternate-path permission where a result forbids it;
- capability and same-result/no-weaker-verification rules before conditional
  current-VPS examples;
- a frozen route-neutral prompt, fixtures, model, harness, environment, pair
  order, first-choice rule, and variance disposition, with only the prior versus
  candidate protocol intentionally different within each cold pair;
- raw unmerged traces and exact result, absent-utility, allowed-context,
  stricter-denial, unrelated-scope, rollback, and no-authority checks; and
- evidence claims bounded to the evaluated current denials and purpose-level
  results, with no invented historical replay, portability, savings, or
  implementation claim.[2][3]

Failure conditions were overbroad scope, routing around a final denial, unmatched
or retrospectively graded runs, a control already exhibiting the claimed
behavior, a treatment beginning with a denied route, a result gate that could
pass weaker verification or ungraded route failures, or any authority or benefit
claim beyond the evidence.

Pipeline history contains one prior `REVISE`, no prior `REFRAME`, and no human
budget extension. Corrective cycle 1 of 2 was used by the r01 final review.[2]
[4]

## Findings

### The wording and scope corrections pass

The proposed insertion remains one paragraph after Session Transaction item 3,
and both Forge loops apply that protocol. The paragraph now conditions its
route-selection guidance on the active unattended approval context being in
`deny` mode, makes the actual guard result authoritative, prohibits rewording or
configuration changes, and forbids another route when the result says not to
attempt the same outcome.[1][4]

These corrections match the checked platform contract. Official documentation
distinguishes unattended `deny` from `approve`; `deny` blocks a flagged route
immediately and directs the agent to another path, while `approve` resolves the
unattended prompt differently.[6] The pinned source resolves active unattended
contexts and their configured modes, and it applies hardline and user-defined
deny floors before ordinary unattended approval handling. The floor messages
make their non-bypass semantics explicit.[8][9] The paragraph remains guidance,
not an enforcement claim, and says runtime results control.[1]

The capability-first order, conditional examples, structural non-equivalence,
absent-utility stop, evidence distinctions, no-savings disclaimer, separate
implementation authority, and paragraph-deletion rollback all remain within the
ADVANCE conditions and the prior review.[1][2][3] Official code-execution
guidance supplies only a general programmatic-tool versus shell-command rule,
not this Forge-specific route map.[7] No new research gap blocks a proposal-only
correction.

### The matched design is frozen, but its classifier does not cover its claimed result

The revision materially improves the comparison design. It freezes a
route-neutral prompt, fixture package, model-harness-environment contract,
sampling settings, three pair orders, exact outputs, first-choice labels,
dispositions, and raw unmerged traces. It also predeclares failure and
inconclusive outcomes rather than permitting selective reruns.[1] These controls
match the Brain's evaluation guidance that an agent result names the complete
system contract, trial and retry rules, grader, and raw artifacts.[5]

One blocking false-positive path remains. Each run receives one prompt containing
four distinct purposes: extraction, arithmetic, ASCII rejection, and structural
mismatch. The grader then classifies only "the first attempted route" for the
whole run. The PASS rule requires each treatment's single label to be
`safe-first` and the final results to be exact, but it does not reject a denied
first choice for any later purpose.[1]

For example, under the written rule a treatment can begin with first-class file
reading for extraction and receive the run-level `safe-first` label, later try a
guarded interpreter for arithmetic, recover with `bc`, and still produce every
exact final result. The treatment retains its `safe-first` label, the denied
later route has no predicate in the gate, and the candidate can pass despite the
route-order failure the paragraph is intended to prevent. This is a logical
counterexample to the declared decision rule, not a claim that the unexecuted
comparison produced that trace.

The same undercoverage limits causal interpretation of the controls. Two
run-level `denied-first` controls would show a difference in the earliest route,
not whether the paragraph changed first choice for each purpose represented by
its capability and utility guidance. Exact final outputs do not repair that gap:
outcome grading and trajectory grading answer different questions, and the route
sequence is material to this proposal's claim.[5]

The acceptance contract must therefore either:

1. classify each purpose's first attempted route separately and fail any
   treatment in which any claimed purpose takes a denied route before an
   equivalent permitted route, with a predeclared aggregate rule for the matched
   controls; or
2. split the purposes into independently frozen matched cases and narrow the
   claimed benefit to exactly the cases the classifiers cover.

The current wording needs no research change. The defect is confined to the
proposal's grader and claimed PASS boundary.

### Negative cases, worst failure, and reversal otherwise pass

The isolated allowed or approve case, ordinary recoverable denial, stricter
denial, unconditional floor, and unrelated-scope cases directly address the r01
review's missing regressions. They do not mutate a live profile and they keep
runtime policy, rather than prose, as the enforcement boundary.[1][2][6][8][9]

The stated worst failure remains correct: conditional examples or "another
path" could be mistaken for permission to bypass a guard or weaken a check. The
returned-result rule, stricter-denial stop, capability-first wording,
equivalence requirement, structural counterexample, and negative fixtures all
reduce that risk. Deleting one paragraph is a complete and reversible repository
rollback.[1][5]

## Verdict and Handoff

**Verdict: REVISE.**

**Next stage: propose.** Prior corrective-cycle count is 1; this verdict uses
corrective cycle 2 of 2. No human budget extension exists.[2][4]

Required proposal change: make the first-choice classifier and matched decision
rule cover every purpose for which the proposal claims route-selection benefit,
or narrow the claim and fixtures to the exact route decision the single
classifier covers. A treatment must not pass when any covered purpose attempts a
denied route before its equivalent permitted route. Preserve the corrected
deny-context wording, guard-result authority, frozen matched inputs, raw traces,
negative matrix, exact-result checks, and rollback.

This is a proposal-only design correction; no additional research stage is
required. READY is unavailable because the current PASS rule admits a trace that
violates the proposed behavior. The correction budget is now exhausted. A later
final review must close with `DEFER` rather than request another correction if a
blocker remains without an explicit human extension. Approval and implementation
remain separate human decisions.[4]

Confidence in REVISE is medium. The exact acceptance text supplies a direct
false-positive trace, and the prior correction, protocol, official approval
contract, pinned guard source, and evaluation-method sources agree on the
required boundaries.[1][2][4][5][6][8][9] Confidence is limited because the
matched comparison is a proposed, unexecuted adoption gate. It would rise if a
revision maps every claimed purpose-level route predicate to frozen classifier
output without weakening the existing negative and result gates.

## Learning Decision

The completed review supports one existing-lesson edit rather than a new lesson.
The transaction-checker pipeline previously showed that a checker can pass its
declared fixtures while omitting fields in the claimed result contract. This
independent pipeline now shows the same method failure in an evaluation grader:
a run-level first-route label omits later purpose-level route decisions while the
PASS claim spans all four purposes.[1][10]

- **Selection:** Mapping every claimed behavior to a grader predicate before
  drafting the matched schedule would have exposed the gap earlier.
- **Evidence and test design:** Matched inputs, raw traces, and exact outputs are
  necessary but insufficient when the classifier ignores a decision that the
  acceptance claim covers.
- **Process:** Final review found the false-positive route before execution; no
  tool or handoff failure caused it.
- **Repetition:** This is a second independent pipeline exhibiting the existing
  claimed-result-contract lesson, but in an evaluator rather than a checker.
- **Coverage:** Update that lesson to cover evaluators, classifiers, and
  purpose-level predicates, and raise confidence from low to medium; do not add
  a duplicate lesson or imply implementation authority.

The planned `LEARNINGS.md` edit passes its separate admission gate after this
completed final review: two independent pipelines support a transferable method,
the consequence is concrete, and the edit grants no governance or deployment
permission.[10]

## Sources

1. `forge/proposals/unattended-forge-command-paths-r02.md` -- exact target,
   revised paragraph, matched comparison, classifier, decision rule, negative
   matrix, limits, worst failure, and rollback. [high]
2. `forge/evaluations/unattended-forge-command-paths-review-r01.md` -- prior
   REVISE verdict, deny-context and guard-authority corrections, matched-design
   requirement, regressions, and first corrective cycle. [high]
3. `forge/evaluations/unattended-forge-command-paths-evaluation-r01.md` --
   ADVANCE conditions, independently reproduced evidence, scope, and limits.
   [high]
   - `forge/research/unattended-forge-command-paths-r01.md` -- current denial
   observations, purpose-level fixtures and results, structural limitation, and
   unmeasured costs. [high]
   - `forge/ideas/unattended-forge-command-paths-r01.md` -- root question,
   threshold, exclusions, and stop conditions. [high]
   - `forge/proposals/unattended-forge-command-paths-r01.md` -- prior paragraph
   and one-sided acceptance design corrected by the target. [high]
4. `forge/protocol.md` -- independence, correction budget, final-review
   disposition, Session Transaction insertion point, and no-implementation
   boundary. [high]
   - `STATUS.md` -- selected final-review row at starting HEAD. [high]
   - `logbook/progress.log` -- exact handoffs, r01 REVISE, r02 proposal, and
   correction history. [high]
   - `logbook/errors.log` -- denial incidents and recovery record checked for
   the pipeline context. [high]
5. `agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md`
   -- model-harness-environment contracts, outcome versus trajectory grading,
   repeated-run rules, raw artifacts, and predeclared aggregation. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-harness-design.md` --
   external authority, typed policy results, denial recovery, traces, and
   verification distinct from generation. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md`
   -- external enforcement, unconditional boundaries, and allowlist limits.
   [medium]
6. Nous Research. "Security," Hermes Agent documentation, undated; accessed
   2026-09-30, Approval Modes, Hardline Blocklist, User-Defined Deny Rules, and
   returned-block passages. Unattended `deny` and `approve` behavior and
   unconditional floor semantics were checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/security [high]
7. Nous Research. "Code Execution," Hermes Agent documentation, undated;
   accessed 2026-09-30, When the Agent Uses This and `execute_code` versus
   `terminal`. General route-selection guidance was checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution
   [high]
8. Nous Research. `tools/approval.py`, Hermes Agent commit
   `666f313d1d3abd8077291ba464cf0a10f1a6157f`; accessed 2026-09-30,
   `_unattended_contexts`, `_unattended_deny`, `_floor_block`, and
   `check_execute_code_guard`. Active-context resolution, mode handling, result
   authority, and pre-gate floor order were checked.
   https://raw.githubusercontent.com/NousResearch/hermes-agent/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval.py
   [high]
9. Nous Research. `tools/approval_floors.py`, Hermes Agent commit
   `666f313d1d3abd8077291ba464cf0a10f1a6157f`; accessed 2026-09-30, hardline and
   user-defined deny result builders. Unconditional returned instructions and
   pre-gate ordering were checked.
   https://raw.githubusercontent.com/NousResearch/hermes-agent/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval_floors.py
   [high]
10. `LEARNINGS.md` -- learning-capture questions, admission gate, existing
    claimed-result-contract lesson, and confidence rules. [high]
    - `governance/skills/forge-evaluate/SKILL.md` -- cold-baseline,
      independent-source, final-review, and correction-budget procedure. [high]
    - `governance/skills/forge-loop-evaluate/SKILL.md` -- one-verdict
      transaction, learning order, and no-implementation boundary. [high]
    - `governance/template-review.md` -- final-review findings, disposition,
      learning, and Sources checklist. [high]
