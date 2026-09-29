---
name: unattended-forge-command-paths
id: 20260929T223305Z
tier: idea
pipeline: 20260929T223305Z
author: Analyst
tags: [agent-systems, cron, tool-use, reliability]
links:
  - ANCHOR.md
  - logbook/errors.log
  - forge/protocol.md
  - governance/skills/forge-loop-evaluate/SKILL.md
  - governance/skills/forge-loop-research/SKILL.md
  - governance/skills/forge-evaluate/SKILL.md
  - governance/skills/forge-research/SKILL.md
  - forge/ideas/evidence-gated-forge-transaction-checker-r01.md
  - forge/ideas/auditable-sbc-buyback-bridge-r01.md
  - forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md
  - agentic-brain:library/coding-agentic-ai/agent-harness-design.md
  - agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md
  - https://hermes-agent.nousresearch.com/docs/user-guide/security
confidence: low
---
# Unattended Forge Command Paths

## Question and Value

Can a bounded replay of the Forge's six recorded approval-blocked command
incidents identify a small, stable safe-path table for unattended sessions that
avoids repeated denied probes while preserving Hermes's default denial boundary
and without changing runtime configuration?

The target improvement is command-selection guidance in the current Forge loop
and stage skills, not Hermes approval policy. Analyst and Researcher sessions
must finish bounded checks without a person present, yet six entries record
approval-blocked Python or Perl probes. Each session recovered through a
first-class retrieval/file tool or a simpler permitted utility, so the incidents
show repeated friction rather than missing capability.[1][3] This serves ANCHOR
Path A by testing a concrete improvement to agent tools, skills, and failure
recovery.[8]

The provisional hypothesis is that four recurring purposes - extraction,
arithmetic, ASCII verification, and structural verification - can be mapped to
already available safe paths before a denied shell command is attempted. A
credible alternative is that the denials are correctly placed, cheap, and too
task-specific for a durable table; ad hoc recovery may be better than adding
another rule. The idea is not worth pursuing if controlled replays do not
reproduce the denials, if the alternatives fail the same correctness checks, if
instructions already make the safe route unambiguous, or if useful coverage
requires changing approval settings, allowlists, runtime code, or broad tool
policy.

## Origin and Prior Work

This is direct ideation under ANCHOR Path A, Agent Systems. The observed record
is narrow: `logbook/errors.log` contains six literal `approval-blocked`
incidents across two pipelines. Five belong to the closed SBC-buyback pipeline
and one to the open transaction-checker pipeline. The recorded recoveries used
no approval bypass: official-document extraction, standard-library parsing,
`iconv`, `bc`, `tr`, and repository-native read/search checks completed the
work.[1] These are operational observations, not six independent experiments;
most occurred in one pipeline on one day.

Hermes's official security documentation makes the alternative explanation
material. The documented default for `approvals.cron_mode` is `deny`; when a
headless cron job triggers a dangerous-command prompt, Hermes blocks it and the
agent must find another path. The same fail-fast behavior applies to unattended
programmatic sessions.[4] The observed denials may therefore show the safety
boundary working as designed, while the possible defect lies only in repeated
command selection. This idea excludes `approvals.mode: off`, headless automatic
approval, permanent allowlisting, and every profile or runtime change.

The Brain evidence supports that distinction. Its harness review says an
authorization denial should not be retried unchanged and that failure classes
should map to bounded recovery actions.[5] Its human-oversight review places
approval at consequence boundaries and recommends deterministic controls for
routine, reversible checks rather than consuming human attention as a syntax
validator.[6] Neither source establishes that a Forge-specific command table
will improve outcomes; both define constraints for testing one.

The current Forge loop skills require protocol recovery, accurate tool-failure
logging, independent evidence checks, and exact validation, but they do not
provide a tested mapping from these four blocked command purposes to preferred
unattended routes.[2][3] A later proposal would have to show whether one compact
note in existing skills is better than doing nothing; this idea does not presume
that a new skill or runtime feature is warranted.

The duplicate check enumerated `forge/graveyard/`, `forge/ideas/`, and
`forge/proposals/`, searched command, approval, cron, unattended, fallback, and
tool-failure synonyms, queried the Forge index, inspected relevant history, and
checked active and archived progress records. There is no proposal artifact and
no explicit accepted or pending proposal decision. The closed SBC-buyback work
is a value-investing measurement pipeline.[7] The open
`evidence-gated-forge-transaction-checker` idea tests contradictions among an
artifact, `STATUS.md`, and a progress event; it explicitly limits itself to
transaction relationships and a read-only checker.[7] This question instead
tests whether agents can choose reliable existing execution paths before a
headless command denial. It neither extends that checker nor changes its waiting
research row.

The strongest alternative candidate was a dedicated publication-verification
path audit prompted by the missing optional watcher-log helper in error
`ENT-003`. It lost because that event had already passed exact ancestor
verification, records no publication failure, and has no recorded recurrence;
the approval-denial pattern has six occurrences and four distinct check
purposes.[1] This comparison establishes priority, not impact: the cost and
preventability of the six incidents remain unknown.

## Research Plan

Use one bounded, disposable replay unit:

1. Freeze the six error entries, current Forge skills, available first-class
   tools, and Hermes security documentation at the research starting commit.
   Classify each incident by intended check, denied command family, successful
   fallback, correctness evidence, extra tool calls, and whether the session
   still completed. Do not infer timing or exact command text when the record
   does not preserve it.
2. Build four scratch-only fixtures for the recorded purposes: extract a known
   HTML passage, perform fixed arithmetic, reject one non-ASCII byte, and detect
   one structural mismatch. State the expected result before execution and use
   no live repository mutation as a fixture.
3. Under the normal unattended context, compare the recorded interpreter or
   parser route with an existing first-class tool or bounded utility route.
   Preserve the exact call, approval result, exit status, output, and correctness
   check. Do not change approval configuration, use YOLO mode, add an allowlist,
   or request interactive approval.
4. Distinguish three outcomes: blocked but safely replaceable, blocked with no
   equivalent route, and no longer blocked. A denial is not an error in the
   approval system. Count only a replacement that produces the predeclared
   correct result and uses no weaker verification.
5. Compare doing nothing, a compact safe-path table in existing stage skills,
   and a runtime or permission change. Treat doing nothing as the baseline and
   exclude the runtime or permission change from recommendation unless Suggi
   separately authorizes investigation; this pipeline must not alter it.
6. Stop without a proposal if the denials do not reproduce, the safe paths are
   task-specific, the table would duplicate current tool instructions, or the
   observed extra work is immaterial. Also stop if the only apparent benefit
   comes from weakening the safety boundary.

A later proposal is supported only if at least three distinct recorded purposes
are reproducibly blocked through the old route, an existing safe route completes
each same check correctly without a denied call, and one compact instruction can
cover them without claiming general command safety. Preserve the replay matrix
before synthesis so evaluation can distinguish observed results from a
retrospective summary. The preferred result is the smallest justified change,
including no change.

Confidence is low. The Forge record establishes six denials and successful
fallbacks, and official documentation explains why unattended denial is the
safe default.[1][4] Confidence is limited because the incidents are concentrated
in two pipelines, exact commands and elapsed costs are not fully preserved, and
no controlled replay has measured preventability or benefit. Confidence would
rise if fixed fixtures reproduce several denials and the same compact guidance
selects correct safe paths; it would fall if current Hermes behavior, tools, or
instructions make the recorded pattern obsolete.

## Sources

1. `logbook/errors.log` -- six approval-blocked Python or Perl incidents,
   affected pipelines, and the recorded recovery route for each. [high]
2. `forge/protocol.md` -- session recovery, error logging, validation, write
   boundaries, and the prohibition on profile, runtime, cron, or service
   changes. [high]
3. `governance/skills/forge-loop-evaluate/SKILL.md` -- evaluation-loop recovery
   and bounded-stage requirements. [high]
   - `governance/skills/forge-loop-research/SKILL.md` -- research-loop recovery,
     error recording, and one-stage boundary. [high]
   - `governance/skills/forge-evaluate/SKILL.md` -- independent evidence and
     exact validation requirements. [high]
   - `governance/skills/forge-research/SKILL.md` -- approved retrieval routes,
     explicit tool failures, and evidence requirements. [high]
4. Nous Research. "Security," Hermes Agent documentation, undated; accessed
   2026-09-29, Dangerous Command Approval and Approval Modes sections.
   Default headless denial behavior and the requirement to find another path
   were checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/security [high]
5. `agentic-brain:library/coding-agentic-ai/agent-harness-design.md` --
   authorization-denial recovery, typed tool dispatch, and bounded verification
   guidance. [medium]
6. `agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md` --
   consequence-based approval placement and automated controls for routine,
   reversible checks. [medium]
7. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- compared
   open pipeline and its distinct artifact-STATUS-event consistency scope.
   [high]
   - `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- compared closed idea
     family and its value-investing measurement scope. [high]
   - `forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md` -- exact
     closure and reopening conditions for that prior pipeline. [high]
   - `STATUS.md` -- preserved open transaction-checker row and board state at
     starting commit `d18d08c495a26b3ede40ee39877c6224d2923bf9`. [high]
   - `logbook/progress.log` -- current handoffs and absence of an explicit
     proposal decision at the same commit. [high]
   - `forge/proposals/.gitkeep` -- no current proposal artifact at the same
     commit. [high]
8. `ANCHOR.md` -- Path A mission fit, recurring-failure prompt, selection
   criteria, and required non-duplicate bounded question. [high]
