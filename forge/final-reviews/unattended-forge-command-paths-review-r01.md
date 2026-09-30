---
name: unattended-forge-command-paths-review
id: 20260930T035205Z
tier: review
pipeline: 20260929T223305Z
author: Analyst
tags: [agent-systems, cron, tool-use, final-review]
links:
  - forge/proposals/unattended-forge-command-paths-r01.md
  - forge/research/unattended-forge-command-paths-r01.md
  - forge/evaluations/unattended-forge-command-paths-evaluation-r01.md
  - forge/ideas/unattended-forge-command-paths-r01.md
  - forge/protocol.md
  - STATUS.md
  - logbook/progress.log
  - logbook/errors.log
  - governance/skills/forge-evaluate/SKILL.md
  - governance/skills/forge-loop-evaluate/SKILL.md
  - governance/skills/forge-loop-research/SKILL.md
  - governance/template-review.md
  - governance/template-proposal.md
  - LEARNINGS.md
  - agentic-brain:library/coding-agentic-ai/agent-harness-design.md
  - agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md
  - agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md
  - https://hermes-agent.nousresearch.com/docs/user-guide/security
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution
  - https://github.com/NousResearch/hermes-agent/blob/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval.py
  - https://github.com/NousResearch/hermes-agent/blob/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval_floors.py
confidence: medium
---
# Final Review: Unattended Forge Command Paths

## Target and Baseline

Target: `forge/proposals/unattended-forge-command-paths-r01.md`, ID
`20260930T020211Z`.[1]

The proposal author is Researcher. This final review was performed by Analyst in
a fresh separate context that did not inherit the drafting session's private
reasoning or proposal-body findings. Independence therefore passes under the
protocol.[5][7]

At starting HEAD `10e32f6b5537fbef400596890593ec1a1535d0ef`, pipeline
`20260929T223305Z` was the oldest eligible evaluation-loop assignment: active at
`final-review` with the exact proposal as input. The idea, research, ADVANCE
evaluation, proposal, STATUS row, and progress event agree on the pipeline and
handoff.[1][2][3][4][6]

A cold baseline was recorded at `2026-09-30T03:41:31Z` before the proposal body
was opened. Expected design requirements were one authoritative insertion point
and exact wording; deny-context scope without configuration changes; capability
and equivalence rules before conditional examples; preservation of the evaluated
evidence boundary; no unmeasured efficiency claim; acceptance, negative, and
regression checks that identify first-choice benefit; the worst failure; and
complete rollback. Failure conditions included overbroad trigger scope, weaker
verification, allowlist interpretation, unsupported portability or savings
claims, a test unable to distinguish guidance from prompting, and any
implementation authority.

Pipeline history contains no prior `REVISE` or `REFRAME` and no human budget
extension.[2][6] Prior corrective-cycle count is 0.

## Findings

### Responses to the ADVANCE conditions

| Condition | Outcome | Finding |
|:--|:--|:--|
| One insertion point and exact compact wording | PASS | The proposal supplies one quoted paragraph for `forge/protocol.md`, after Session Transaction item 3 and before item 4.[1][5] |
| Scope to unattended Forge work under verified denial behavior | BLOCKED | The paragraph is triggered by any headless session, not by an active unattended deny context. This exceeds the verified premise and contradicts the proposal's negative-scope claim.[1][2] |
| Capability classes and equivalence before examples | PASS | First-class capabilities and same-result/no-weaker-verification requirements precede the conditional `bc`, `iconv`, and bounded `tr` examples.[1] |
| Preserve evidence distinctions | PASS | The proposal distinguishes six unreconstructed incidents, one class-wide `execute_code` denial, one Perl denial, three reproduced purpose-level results, and one manual structural comparison.[1][2][3] |
| No measured benefit claim; compare doing nothing | PASS | Doing nothing remains credible and no latency, token, tool-call, or economic saving is claimed.[1] |
| Cold first-choice, exact result, absent utility, and no denied probe | BLOCKED | The individual cases exist, but no matched prior-protocol control or predeclared comparison rule can identify an amendment effect.[1][2] |
| Paragraph removal as rollback | PASS | The rollback is complete, bounded, and requires the same repository gates and exact diff inspection.[1] |

### Exact change, feasibility, and scope

The proposed location is feasible. Both Forge loops explicitly apply
`forge/protocol.md`, so one central paragraph reaches ideation, research,
evaluation, proposal, and final review without duplicating skill text.[5][7]
Repository search found no current Forge protocol or canonical-skill mapping for
the named route classes.

The trigger is nevertheless overbroad. Official documentation defines both
`deny` and `approve` unattended behavior.[8] Pinned `check_execute_code_guard`
source denies arbitrary local Python when the first active unattended context is
in `deny` mode, but approves when that active context is not deny; isolated
execution backends may also be approved before this branch.[10] The proposal
instead begins `When the session is headless` and later requires HALT when no
equivalent substitute exists.[1] It would therefore create a new Forge-level
restriction in a headless context that Hermes permits, despite the proposal's
regression claim that a Forge task without a denial or substitute-route question
acquires no new restriction.

The amendment must be narrowed to the verified active unattended deny context.
It must also state that the actual guard result and stricter denial semantics
remain authoritative. Pinned command-guard source applies hardline,
runtime-self-protection, sudo, and user-defined deny floors before ordinary
unattended handling.[10][11] Local recovery guidance may select an equivalent
alternative only where the returned denial permits one; it must not turn an
unconditional or user-defined stop into permission to obtain the same forbidden
outcome through another path.

### Evidence and unsupported claims

The proposal accurately limits the historical record and live replay. It does
not claim six controlled replays, general utility safety, portable availability,
automated structural equivalence, or measured savings.[1][2][3][6] Official
code-execution documentation supplies only the general `execute_code`-versus-
`terminal` rule, not this Forge-specific order.[9] The Brain sources support
authority separation, bounded denial recovery, deterministic controls, and
allowlist caution, while the proposal correctly says they do not establish the
amendment's value or wording.[12]

No new evidence gap blocks a proposal revision. The defect is the amendment's
normative trigger and its acceptance design, not the research record.

### Acceptance, negative checks, worst failure, and reversal

The proposed implementation checks correctly separate prior research evidence
from future behavior testing. They include an exact diff boundary, no denied
probe before the selected route, declared extraction, arithmetic, and ASCII
results, the structural non-equivalence case, absent-utility behavior, negative
non-Forge scope, repository gates, and human review.[1]

They do not establish selection benefit. A single post-amendment run can pass
because the model already would have chosen the safe route or because the task
prompt makes that route salient. Proposal lines 116-120 expressly say the
proposal should not advance if the acceptance test cannot distinguish amendment
benefit from task prompting, but the test contains no untreated comparator.[1]

Revision must freeze one route-neutral task prompt, fixture package, model,
harness, configuration, and decision rule before execution; run separate cold
control and treatment contexts whose only intended difference is the prior
versus candidate protocol; preserve their unmerged traces; and predeclare how
run variance is handled. If the control already makes the safe first choice, or
the treatment still begins with a denied route, the test has not shown selection
benefit. The regression matrix must also include a headless allowed or approve
context and a stricter denial whose outcome must not be routed around.

The stated worst failure is appropriate: named utilities become a perceived
safety allowlist or a lossy substitute for an exact check. The capability-first
wording, equivalence requirement, structural counterexample, and absent-utility
stop reduce that risk.[1][12] Rollback by deleting the one paragraph is complete
and requires no migration or runtime reversal.[1]

## Verdict and Handoff

**Verdict: REVISE.**

**Next stage: propose.** Prior corrective-cycle count is 0; this verdict uses
corrective cycle 1 of 2. No human budget extension exists.[5][6]

Required proposal changes:

1. Narrow the exact amendment to the active unattended deny context, preserve
   the authority of the returned guard result and unconditional floors, and add
   negative regression cases for a headless allowed context and a denial that
   prohibits alternate-path recovery.
2. Replace the single post-amendment behavior check with a predeclared matched
   cold control/treatment design that can distinguish the paragraph from
   existing behavior and task prompting.

These are proposal-only design corrections. No additional research cycle is
required. READY is not available while either blocker remains. Approval and
implementation remain separate human decisions.

Confidence in REVISE is medium. The exact proposal, protocol, official
documentation, pinned guard source, repository history, and linked evidence
agree on both defects. Confidence is limited because the amended behavior has
not been implemented or executed. It would rise after exact trigger wording and
a causally informative acceptance design receive another independent final
review.

## Learning Decision

`LEARNINGS.md` remains unchanged. The existing fixture-contract lesson already
requires tests to cover the claimed PASS boundary, and the final-review template
already requires acceptance, negative, and regression checks.[7][13] This review
is a proposal-specific application rather than a distinct transferable lesson
with executed outcome evidence. No duplicate learning edit passes the admission
gate.

## Sources

1. `forge/proposals/unattended-forge-command-paths-r01.md` -- exact target,
   proposed paragraph, evidence claims, acceptance cases, worst failure,
   rollback, and confidence. [high]
2. `forge/evaluations/unattended-forge-command-paths-evaluation-r01.md` --
   matching ADVANCE verdict, seven proposal conditions, evidence limits, and
   correction count. [high]
3. `forge/research/unattended-forge-command-paths-r01.md` -- incident
   classification, preserved fixtures and calls, route results, structural
   limitation, alternatives, and unmeasured costs. [high]
4. `forge/ideas/unattended-forge-command-paths-r01.md` -- root threshold,
   exclusions, stop conditions, and bounded question. [high]
5. `forge/protocol.md` -- final-review disposition, correction budget, Session
   Transaction insertion point, source rules, and no-implementation boundary.
   [high]
6. `STATUS.md` -- exact selected row and preserved unselected row at starting
   HEAD. [high]
   - `logbook/progress.log` -- exact stage handoffs and absence of a prior
     corrective verdict for this pipeline. [high]
   - `logbook/errors.log` -- denial incidents, later recurrence, and recovery
     records. [high]
7. `governance/skills/forge-evaluate/SKILL.md` -- cold-baseline,
   independent-source, final-review, and correction-budget procedure. [high]
   - `governance/skills/forge-loop-evaluate/SKILL.md` -- final-review
     transaction and no-implementation boundary. [high]
   - `governance/skills/forge-loop-research/SKILL.md` -- central protocol
     consumption by research and proposal stages. [high]
   - `governance/template-review.md` -- final-review findings, disposition,
     learning, and Sources gate. [high]
   - `governance/template-proposal.md` -- proposal acceptance, negative,
     regression, worst-failure, and reversal requirements. [high]
8. Nous Research. "Security," Hermes Agent documentation, undated; accessed
   2026-09-30, Dangerous Command Approval and Approval Modes. Deny and approve
   unattended behavior were checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/security [high]
9. Nous Research. "Code Execution," Hermes Agent documentation, undated;
   accessed 2026-09-30, `execute_code` versus `terminal`. The general
   route-selection rule was checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution
   [high]
10. Nous Research. `tools/approval.py`, Hermes Agent commit
    `666f313d1d3abd8077291ba464cf0a10f1a6157f`; accessed 2026-09-30,
    `_unattended_deny`, `check_all_command_guards`, and
    `check_execute_code_guard`. Context-mode branching and pre-gate floor order
    were checked.
    https://github.com/NousResearch/hermes-agent/blob/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval.py
    [high]
11. Nous Research. `tools/approval_floors.py`, Hermes Agent commit
    `666f313d1d3abd8077291ba464cf0a10f1a6157f`; accessed 2026-09-30, hardline,
    sudo, and user-defined denial results. Stricter denial semantics were
    checked.
    https://github.com/NousResearch/hermes-agent/blob/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval_floors.py
    [high]
12. `agentic-brain:library/coding-agentic-ai/agent-harness-design.md` --
    authorization-denial recovery, authority separation, and independent
    verification. [medium]
    - `agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md` --
      consequence-boundary approvals and deterministic controls. [medium]
    - `agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md`
      -- external enforcement, unconditional boundaries, and allowlist limits.
      [medium]
13. `LEARNINGS.md` -- learning admission gate and existing evidence-package and
    claimed-PASS-contract lessons. [high]
