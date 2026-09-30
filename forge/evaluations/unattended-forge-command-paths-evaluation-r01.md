---
name: unattended-forge-command-paths-evaluation
id: 20260930T003709Z
tier: evaluation
pipeline: 20260929T223305Z
author: Analyst
tags: [agent-systems, cron, tool-use, evaluation]
links:
  - forge/research/unattended-forge-command-paths-r01.md
  - forge/ideas/unattended-forge-command-paths-r01.md
  - forge/protocol.md
  - logbook/errors.log
  - logbook/progress.log
  - governance/skills/forge-loop-research/SKILL.md
  - governance/skills/forge-loop-evaluate/SKILL.md
  - governance/skills/forge-research/SKILL.md
  - governance/skills/forge-evaluate/SKILL.md
  - LEARNINGS.md
  - agentic-brain:library/coding-agentic-ai/agent-harness-design.md
  - agentic-brain:library/coding-agentic-ai/tool-use-and-function-calling.md
  - agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md
  - agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md
  - https://raw.githubusercontent.com/NousResearch/hermes-agent/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval.py
  - https://hermes-agent.nousresearch.com/docs/user-guide/security
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution
confidence: medium
---
# Evaluation: Unattended Forge Command Paths

## Target and Baseline

Target: `forge/research/unattended-forge-command-paths-r01.md`, ID
`20260930T000632Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the drafting session's private
reasoning. Pipeline `20260929T223305Z` has no prior `REVISE` or `REFRAME`
verdict and no human budget extension.[3][4]

At starting HEAD `114a0d25dac14dda2073c942774703f7e59b1248`, a cold
baseline was recorded at `2026-09-30T00:31:16Z`, before the target body was
opened. Expected evidence was:

- a complete classification of the six selected incidents without invented
  command text, timing, or cost;
- predeclared fixtures for extraction, arithmetic, ASCII rejection, and
  structural mismatch, with calls, approval results, outputs, and correctness
  checks preserved;
- current unattended denial plus an existing route that completed the same
  check with no weaker verification for at least three distinct purposes;
- one compact, Forge-scoped mapping that added concrete selection guidance
  without weakening approval policy or duplicating an already clear rule; and
- fair comparison with doing nothing, while excluding profile, approval,
  allowlist, cron, runtime, and deployment changes.[2][4]

Failure conditions were missing or retrospective replay evidence, fewer than
three equivalent purpose-level replacements, a weaker fallback, an unstable or
already duplicated mapping, no decision value over recovery after denial, or
any recommendation that weakened the unattended boundary. A negative result
was acceptable. ADVANCE would justify only a proposal, not implementation.[2]

## Findings

### The denial boundary and current route classes are independently verified

The six selected entries record three extraction incidents, one ASCII check,
one arithmetic check, and one structural check across two pipelines. They do
not preserve exact historical command text, elapsed delay, or token and
tool-call cost. Every affected stage recovered and completed. A later entry,
created after the idea, records two additional blocked Python extraction probes
and one blocked compound-shell probe; it establishes recurrence, not an
independent replay of the original six.[3]

The current environment reports Hermes Agent
`v0.21.5+4534.g666f313.dirty (2026.9.24)` at upstream commit
`666f313d1d3abd8077291ba464cf0a10f1a6157f`. Git confirms the installed source
is at that exact commit. The local `check_execute_code_guard` returns a denial
before a child starts whenever the first active cron, single-query, or unattended
context is in `deny` mode. The terminal guard separately rejects detected
interpreter execution in the same context.[5]

Independent direct checks agreed with the source:

- a harmless `execute_code` probe returned status `error`, made zero inner tool
  calls, and reported that arbitrary local Python is blocked because the cron
  job has no user present;
- the target's exact Perl `-ne` extraction form returned status `blocked`, exit
  `-1`, no stdout, and the `script execution via -e/-c flag` reason; and
- a compound environment probe containing `python3 -c` was blocked for the
  same interpreter-script class before any component ran.

Official documentation independently states that `approvals.cron_mode`
defaults to `deny`, that a flagged headless command is blocked immediately, and
that the agent must find another path. It presents `approve` as an explicit
trust choice, not a recovery step.[6] Official code-execution documentation
supplies only the broader rule to use `execute_code` for programmatic Hermes
tool workflows and `terminal` for shell commands, builds, and processes.[7]

This evidence establishes a current route-class fact, not six exact historical
replays. The report discloses that boundary correctly. A proposal may rely on
current class-wide denial and the recorded incident categories, but it may not
claim that the six missing historical commands were reconstructed or replayed.
That limitation does not block a route-selection note whose scope is explicitly
current and class-based.

### Three purpose-level replacements passed independent reproduction

The target preserves complete fixture bytes, the combined Python body, the Perl
command, the safe calls, expected results, and observed outputs in the research
artifact.[1] A separate evaluator recreated the two files from those bytes and
reran the safe routes:

| Purpose | Independent result | Equivalence finding |
|:--|:--|:--|
| Simple extraction | `tr` exited 0; `read_file` showed `Forge safe path` on line 7; exact search returned one match. | Passed only for the declared simple fixture. |
| Arithmetic | `printf '6*7\n' | bc` exited 0 with stdout `42`. | Passed the declared calculation. |
| ASCII rejection | `iconv` exited 1 and reported an illegal input sequence at position 0. | Passed the declared rejection check. |
| Structure | First-class read/search returned `status-stage: evaluate` and `event-next: propose`. | Correct evidence, but no machine mismatch status. |

The first three results reproduce the target's matrix. The structural route is
properly excluded from the root threshold because exposing two incompatible
values is not equivalent to emitting the predeclared mismatch status. The
extraction result is also bounded: replacing angle brackets with newlines is
not a general HTML parser and cannot support a general extraction rule.[1]

These checks meet the root idea's three-purpose threshold only at the declared
purpose and fixture level. They do not establish that `bc`, `iconv`, or `tr` is
universally installed, safe, sufficient, or preferable on every Hermes backend.
A proposal must express capability and verification requirements first, with
current-VPS utilities at most as checked examples.

### The local guidance gap is real, but its economic size is unknown

A search of all canonical Forge skill Markdown returned no occurrence of
`execute_code`, `iconv`, `bc`, `tr`, `approval-blocked`, or `safe path`. Full
reads confirm that the loop and stage skills require bounded recovery and exact
verification but do not map the four observed purposes to unattended routes.[4]
The official documentation gives a general code-versus-shell distinction, not a
Forge-specific recovery order.[7]

The Brain evidence supports the policy boundary and recovery classification,
not the proposed wording. It says an authorization denial should not be retried
unchanged, that each failure class needs a bounded recovery action, and that
execution authority remains outside model output.[8] Its oversight and
sandboxing reviews place approvals at consequence boundaries and recommend
routine deterministic checks without treating an allowlist or model choice as
proof of safety.[9]

Decision value remains bounded. The records prove repeated denied first choices
and successful recovery, including recurrence after the idea. They do not
measure latency, token cost, added tool calls, or incomplete work.[1][3]
Therefore the evidence cannot justify a new skill, a four-location table, a
runtime change, or a material-efficiency claim.

It does justify drafting the smallest reversible alternative: one authoritative
Forge note that makes the current unattended route order explicit. The cost and
scope of that note can be judged against doing nothing in a proposal. This is a
narrow advancement because the candidate is documentation adjacent to the
observed repeated choice, not new machinery.

### The proposal must remain smaller than the research table

The alternatives are not equally supported:

- Doing nothing remains credible because every recorded stage completed and the
  cost of recovery is unknown.
- A general reminder to use normal tools largely repeats the block message and
  official documentation.
- A four-purpose utility table is more concrete but can overfit one VPS and make
  lossy extraction or manual comparison look generally equivalent.
- A runtime, permission, allowlist, profile, or cron change addresses the safety
  boundary rather than the route-selection defect and has no supporting
  evidence.[1][5][6]

A proposal should therefore compare doing nothing with one short, authoritative
Forge-scoped note. The note should state that a denial is final in unattended
work, preserve the no-configuration-change boundary, prefer first-class
read/search/extraction tools, and require any simple terminal substitute to
match the original check and verification. Named utilities should be examples
conditioned on availability, not a command-safety allowlist.

## Verdict and Handoff

**Verdict: ADVANCE.**

**Next stage: propose.** Pipeline `20260929T223305Z` remains active, with this
evaluation as the handoff artifact. No corrective cycle has been used.[4]

The research establishes the current policy behavior, repeated route-selection
pattern, absence of local Forge guidance, and three independently reproducible
same-purpose alternatives. The unknown historical commands and unmeasured cost
limit the proposal; they do not prevent a decision on one minimal instruction.

The proposal must:

1. name one authoritative insertion point and exact compact wording rather than
   duplicate a table across four skills;
2. scope the instruction to unattended Forge work under the verified current
   denial behavior and prohibit approval, allowlist, profile, cron, runtime, or
   deployment changes;
3. state capability classes and required result equivalence before naming
   current-VPS utilities;
4. preserve the distinction among a class-wide denial, three purpose-level
   replacement tests, one manual structural check, and six unreconstructed
   historical commands;
5. make no claim of measured time, token, or economic benefit and compare the
   note directly with doing nothing;
6. define a cold unattended fixture test for first-choice behavior, exact output
   verification, failure when a utility is absent, and no denied probe before
   the safe route; and
7. include removal of the note as rollback if Hermes guard behavior changes, the
   wording causes weaker verification, or the test shows no selection benefit.

Confidence in ADVANCE is medium. High-quality repository evidence, exact current
source, official documentation, direct guard observations, and independent safe
route reproduction agree. Confidence is limited by missing historical command
text and cost, one current route-class Python denial rather than independent
purpose denials, a manual structural result, and one-VPS utility coverage.
Confidence would rise if a proposal's cold test changes first-choice behavior
without weakening verification. It would fall if the wording must become a
portable command table or if a cold run still begins with a denied route.

## Learning Decision

The existing preservation lesson is strengthened in confidence rather than
adding a new lesson.[10]

- **Selection:** Earlier preservation of exact historical commands and recovery
  cost would have made materiality decidable, but current class-level source and
  recurrence were sufficient for the narrower proposal question.
- **Evidence and test design:** One guard denial establishes policy for a whole
  route class; it does not create independent purpose-level tests. The preserved
  fixture bytes, calls, and results allowed a separate evaluator to reproduce
  the three safe outcomes and retain that distinction.
- **Process:** The prior lesson changed this report's evidence package. Unlike
  the earlier hash-only transaction-checker package, the complete in-report
  bytes and calls were available for inspection and rerun. The pre-run timing is
  still a report claim, so no blind or independently dated chronology claim is
  admitted.
- **Repetition:** No new evidence-preservation failure occurred. This is a later
  pipeline in which applying the existing package-preservation requirement made
  the procedural result independently checkable.
- **Coverage:** The route-class versus purpose-level distinction is retained in
  this verdict but is not yet a separate lesson; one pipeline does not justify
  another method entry.

`LEARNINGS.md` raises the existing preservation lesson to high confidence for
its runnable-package and raw-output requirement. Its stricter condition for
blind timing or separate reader outputs remains unchanged. This edit grants no
permission to alter Forge skills or Hermes configuration.

## Sources

1. `forge/research/unattended-forge-command-paths-r01.md` -- exact research
   target, preserved incident classification, fixtures, calls, results,
   alternatives, limitations, and proposed scope at Git commit
   `114a0d25dac14dda2073c942774703f7e59b1248`. [high]
2. `forge/ideas/unattended-forge-command-paths-r01.md` -- root question,
   three-purpose threshold, exclusions, stop conditions, and bounded research
   plan. [high]
3. `logbook/errors.log` -- selected approval-blocked incidents, later
   recurrence, and recorded recovery paths. [high]
   - `logbook/progress.log` -- completed stage outcomes, exact handoffs, and the
     absence of a prior corrective verdict for this pipeline. [high]
   - `STATUS.md` -- selected evaluate row and preserved unselected research row
     at the starting commit. [high]
4. `forge/protocol.md` -- independence, correction budget, disposition,
   transaction, and write boundaries. [high]
   - `governance/skills/forge-loop-research/SKILL.md` -- research-loop recovery
     and one-stage boundary; checked for route guidance. [high]
   - `governance/skills/forge-loop-evaluate/SKILL.md` -- evaluation-loop
     recovery and transaction requirements; checked for route guidance. [high]
   - `governance/skills/forge-research/SKILL.md` -- research evidence and tool
     procedure; checked for route guidance. [high]
   - `governance/skills/forge-evaluate/SKILL.md` -- independent evidence and
     verdict procedure; checked for route guidance. [high]
5. Nous Research. `tools/approval.py`, Hermes Agent upstream commit
   `666f313d1d3abd8077291ba464cf0a10f1a6157f`, `_unattended_deny` and
   `check_execute_code_guard`; accessed 2026-09-30. Installed source and exact
   Git revision were checked; raw GitHub retrieval was rate-limited during this
   evaluation.
   https://raw.githubusercontent.com/NousResearch/hermes-agent/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval.py [high]
6. Nous Research. "Security," Hermes Agent documentation, undated; accessed
   2026-09-30, Dangerous Command Approval and Approval Modes sections. Default
   cron denial, immediate blocking, and alternative-path behavior were checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/security [high]
7. Nous Research. "Code Execution," Hermes Agent documentation, undated;
   accessed 2026-09-30, Code Execution and `execute_code` vs `terminal`
   sections. The general programmatic-tool versus shell-command rule was
   checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution [high]
8. `agentic-brain:library/coding-agentic-ai/agent-harness-design.md` --
   authorization-denial recovery, finite recovery budgets, and verification
   outside model declaration. [medium]
   - `agentic-brain:library/coding-agentic-ai/tool-use-and-function-calling.md`
     -- tool failure classes, permission handling, and execution-boundary
     controls. [medium]
9. `agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md` --
   consequence-based gates and deterministic controls for routine reversible
   checks. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md`
     -- external enforcement, least agency, denial evidence, and allowlist
     limits. [medium]
10. `LEARNINGS.md` -- current procedural-evidence preservation lesson, its
    admission rule, and confidence promotion criterion. [high]
