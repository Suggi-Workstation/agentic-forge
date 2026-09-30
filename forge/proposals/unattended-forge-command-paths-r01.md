---
name: unattended-forge-command-paths
id: 20260930T020211Z
tier: proposal
pipeline: 20260929T223305Z
author: Researcher
tags: [agent-systems, cron, tool-use, reliability]
links:
  - forge/ideas/unattended-forge-command-paths-r01.md
  - forge/research/unattended-forge-command-paths-r01.md
  - forge/evaluations/unattended-forge-command-paths-evaluation-r01.md
  - forge/protocol.md
  - logbook/errors.log
  - LEARNINGS.md
  - agentic-brain:library/coding-agentic-ai/agent-harness-design.md
  - agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md
  - agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md
  - https://hermes-agent.nousresearch.com/docs/user-guide/security
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution
confidence: medium
---
# Proposal: Unattended Forge Command Paths

## Proposed Decision

Approve one core-file rule amendment to `forge/protocol.md`: add one compact
unattended route-selection paragraph immediately after item 3 in `## Session
Transaction`. The beneficiary is any Forge agent running a headless research,
evaluation, proposal, or review stage. The amendment would make the preferred
recovery order visible before an arbitrary interpreter or parser call is
attempted, while leaving Hermes's approval boundary authoritative.[2][3][4]

The exact proposed paragraph is:

> **Unattended route selection:** When the session is headless, treat an
> authorization denial as final for that exact route; do not retry it unchanged
> or alter approval, allowlist, profile, cron, runtime, or deployment settings.
> Before arbitrary interpreter or parser code, prefer a first-class read,
> search, extraction, or document tool that preserves the required evidence. If
> none fits, use the narrowest available terminal capability only when its
> observed result and verification are equivalent to the intended check;
> current-VPS examples, when available, are `bc` for fixed arithmetic, `iconv`
> for ASCII rejection, and bounded `tr` followed by exact read/search for simple
> markup extraction, not general parsing or a safety allowlist. Read/search may
> expose structural values but is not equivalent to a required machine mismatch
> status. If no equivalent permitted route exists, record the failure and
> follow the stage's HALT or checkpoint rule.

The requested decision is approval or rejection of that exact amendment.
Implementation remains a separate authorized action. This proposal does not
change Hermes configuration, approval policy, allowlists, profiles, cron jobs,
runtime code, deployment, tools, or any Forge skill. It does not assert that a
named utility is portable, generally safe, installed on every backend, or
suitable beyond its checked purpose.[3][6][7]

## Evidence, Alternatives, and Evaluation Response

Before the new source checks for this proposal, the provisional explanation was
that the repeated failure was avoidable route selection, not a defective
approval boundary. A shared protocol paragraph appeared smaller than duplicating
a table across loop or stage skills. That explanation would be invalidated if
the change required weaker verification, a policy exception, a portable utility
allowlist, or a claim that unmeasured recovery cost is material. Subsequent
Forge, Brain, and primary-document checks retained that narrow explanation and
its limits.[3][6][8][9]

The evidence supports four bounded facts:

1. The historical record contains six selected approval-blocked incidents in
   four purpose classes, plus later recurrence. Every recorded stage recovered
   and completed; exact historical commands, elapsed time, token cost, and
   added-call cost were not preserved.[1][2][5]
2. Current research and independent evaluation established one class-wide
   unattended `execute_code` denial and one Perl denial, not six reconstructed
   historical replays. Three purpose-level replacements reproduced the declared
   extraction, arithmetic, and ASCII results. The structural read/search route
   exposed both values but did not emit the required machine mismatch status and
   was correctly excluded from equivalence.[2][3]
3. Current Hermes documentation says `cron_mode: deny` blocks a flagged
   headless command immediately and requires another path. Its code-execution
   guidance distinguishes programmatic multi-tool workflows from simple shell
   commands. The checked sections do not supply the proposed Forge-specific
   recovery order.[6][7]
4. Independent Brain reviews place execution authority outside model output,
   treat authorization denial as a distinct failure that should not be retried
   unchanged, and favor deterministic controls for routine reversible checks.
   They support preserving the denial boundary; they do not establish the value
   or wording of this Forge amendment.[8][9]

The alternatives remain close:

| Alternative | Benefit | Evidence-based limit |
|:--|:--|:--|
| Do nothing | No governance text or maintenance cost; all recorded stages recovered. | A denied first choice recurred, so recovery still begins after avoidable friction.[2][5] |
| Repeat only the generic Hermes rule | Smallest possible reminder. | It does not identify the observed Forge purposes, equivalence requirement, or structural-check limit.[3][6][7] |
| Add the proposed protocol paragraph | One shared insertion point covers both Forge loops, names the recovery order, and keeps examples conditional. | Selection benefit is unmeasured; wording can become stale as Hermes or VPS capabilities change. |
| Add a utility table to several skills | More visible at each stage. | Duplicates policy, overfits one VPS, and increases drift and maintenance risk.[3] |
| Change approval or runtime policy | Removes some denials. | Addresses the tested safety boundary rather than the route-selection issue and is unsupported and out of scope.[2][3][6] |

The proposal accepts every material evaluation condition:[3]

1. One authoritative insertion point and exact wording are supplied above.
2. The wording is limited to unattended Forge work and expressly forbids policy,
   allowlist, profile, cron, runtime, and deployment changes.
3. Capability classes and result equivalence precede conditional current-VPS
   examples.
4. The evidence statement preserves the difference among one route-class denial,
   three purpose-level replacement results, one manual structural comparison,
   and six unreconstructed historical commands.
5. No time, token, or economic benefit is claimed, and doing nothing remains a
   credible alternative.
6. A cold first-choice test, exact output checks, absent-utility case, and
   no-denied-probe condition are specified below.
7. Removal of the one paragraph is the rollback.

The remaining uncertainty is behavioral: no evidence yet shows that this prose
changes an agent's first tool choice. That is not a blocker to deciding whether
to try one reversible paragraph, but it prevents a measured efficiency claim.
If final review finds that the acceptance test cannot distinguish guidance
benefit from task prompting, the proposal should not advance.[3]

## Change Specification and Implementation

**Existing interface.** Every Forge stage reads `forge/protocol.md`. Its Session
Transaction defines the shared stage sequence, recovery, validation, logging,
and write boundaries, but it currently does not state an unattended route
selection order.[4]

**Proposed interface.** Only `forge/protocol.md` changes. The authorized
implementer inserts the quoted paragraph after Session Transaction item 3 and
before the read-only learning rule in item 4. The paragraph applies when the
Forge session is headless; it changes guidance, not tool permissions or command
classification. No new file, skill, script, dependency, service, or runtime
component is proposed.

**Dependencies.** The amendment depends on the current Hermes behavior that a
flagged headless command can be denied and on the continued availability of
first-class read/search/extraction tools. Named terminal utilities are optional
examples and must be checked at use time. Absence of an example utility is not
permission to install it, weaken verification, or alter approval policy.[6][7]

**Ordered implementation, after separate approval:**

1. Re-read the approved proposal, current `forge/protocol.md`, current Hermes
   security and code-execution documentation, and the active Forge board. Stop
   if the denial behavior or protocol insertion point has materially changed.
2. Apply only the quoted paragraph at the specified location. Preserve all
   other protocol text and leave skills and runtime configuration unchanged.
3. Run the repository's ASCII, staged-diff, and ID gates. Inspect the exact diff
   to confirm that one protocol paragraph is the only substantive change.
4. Run the cold unattended acceptance cases below in scratch with no Forge
   state mutation. Preserve the tool trace, fixture bytes, commands, outputs,
   exit statuses, and absent-utility observation.
5. Submit the implementation and receipts for human review. Do not infer
   deployment approval from this proposal or from passing fixtures.

## Acceptance, Risks, and Reversal

Research already checked the current denial class, three exact purpose-level
safe results, one manual structural comparison, and the current guidance gap.
Those checks are evidence for this proposal; they are not evidence that the
new paragraph changes future behavior.[2][3]

A future implementation passes only if all of these observable checks pass:

1. **Diff boundary:** the substantive diff is the exact paragraph in
   `forge/protocol.md`; no skill, profile, approval, allowlist, cron, runtime,
   deployment, or tool file changes.
2. **Cold first choice:** a fresh unattended Forge test session receives the
   committed protocol plus scratch fixtures for simple markup extraction,
   `6*7`, one non-ASCII byte, and two incompatible structural fields. Before any
   arbitrary interpreter, parser, or denied terminal attempt, it selects a
   first-class tool or narrow available terminal capability consistent with the
   paragraph. The preserved trace must show no denied probe before that route.
3. **Exact results:** extraction returns the one declared target, arithmetic
   returns `42`, and ASCII validation rejects the non-ASCII byte. Structural
   read/search may pass only as evidence exposure; if the requested result is a
   machine mismatch status, the session must report that read/search is not
   equivalent rather than claim success.
4. **Absent utility:** repeat one utility-dependent fixture with that utility
   unavailable in the controlled command environment. The session must not
   claim the check passed, install a replacement, change policy, or fall back to
   an unapproved interpreter. It may use another available route only if the
   same result and verification are demonstrated; otherwise it records the
   failure and stops or checkpoints as the stage requires.
5. **Negative scope:** an interactive non-Forge task and a Forge task that has
   no authorization denial or substitute-route question acquire no new approval
   or tool restriction from the paragraph.
6. **Repository gates:** ASCII validation, `git diff --cached --check`, and
   `scripts/validate-ids.sh` pass, and final human review confirms that the
   protocol remains internally consistent.

The worst plausible failure is that agents read the named utilities as a safety
allowlist and replace an exact check with a lossy approximation. The wording
prevents that by putting capability and equivalence first, conditioning examples
on availability, excluding general parsing, and stating the structural mismatch
counterexample. Final review and the cold negative cases must reject any
implementation or behavior that weakens verification.[2][3][8][9]

Costs are one additional protocol paragraph, future cold-test effort, and the
risk of stale examples. The proposal offers no measured latency or token saving.
Doing nothing therefore remains reasonable if Suggi judges the maintenance cost
higher than the repeated but recoverable friction.[2][3]

Rollback is deletion of the one paragraph, followed by the same repository gates
and a diff confirming restoration of the prior protocol. Remove it if Hermes
guard behavior changes materially, named examples become misleading, a cold run
still begins with a denied route, the absent-utility case encourages weaker
verification, or no selection benefit is observed. No data migration or runtime
reversal is required because the change is documentation only.

Confidence is medium. The incident record, current source behavior, official
documentation, three reproduced safe-route results, and independent evaluation
support a bounded guidance trial.[2][3][5][6][7] Confidence is limited by missing
historical command and cost data, one-VPS examples, a manual structural result,
and no direct evidence that prose changes first-choice behavior. Confidence
would rise if cold unattended cases change first choice without weaker
verification; it would fall if the note duplicates existing behavior, becomes
stale, or causes agents to treat examples as permission.

## Sources

1. `forge/ideas/unattended-forge-command-paths-r01.md` -- root question,
   selected incidents, bounded research threshold, exclusions, and alternatives.
   [high]
2. `forge/research/unattended-forge-command-paths-r01.md` -- exact incident
   classification, denial observations, fixtures, purpose-level results,
   structural limitation, alternatives, and unmeasured costs. [high]
3. `forge/evaluations/unattended-forge-command-paths-evaluation-r01.md` --
   matching ADVANCE verdict, independent reproduction, seven proposal
   conditions, confidence limits, and final-review handoff. [high]
4. `forge/protocol.md` -- proposed insertion point, shared Session Transaction,
   recovery rules, stage boundaries, and prohibition on unauthorized runtime or
   governance changes. [high]
5. `logbook/errors.log` -- selected approval-blocked incidents, later
   recurrence, and recorded recovery routes. [high]
   - `logbook/progress.log` -- completed outcomes and handoffs for the affected
     Forge stages. [high]
   - `LEARNINGS.md` -- evidence-package preservation rule applied to the replay
     and evaluation. [high]
6. Nous Research. "Security," Hermes Agent documentation, undated; accessed
   2026-09-30, Dangerous Command Approval and Approval Modes sections.
   Default headless denial and the requirement to find another path were
   checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/security [high]
7. Nous Research. "Code Execution," Hermes Agent documentation, undated;
   accessed 2026-09-30, When the Agent Uses This and execute_code vs terminal
   sections. Programmatic multi-tool and simple shell selection guidance was
   checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution [high]
8. `agentic-brain:library/coding-agentic-ai/agent-harness-design.md` -- tool
   dispatch authority, failure-class recovery, no unchanged retry after an
   authorization denial, and independent verification. [medium]
9. `agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md` --
   consequence-boundary approvals and deterministic controls for routine,
   reversible work. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md` --
     external enforcement, least agency, and the limits of command allowlists.
     [medium]
