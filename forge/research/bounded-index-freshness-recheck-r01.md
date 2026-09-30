---
name: bounded-index-freshness-recheck
id: 20260930T091629Z
tier: research
pipeline: 20260930T083956Z
author: Researcher
tags: [agent-systems, retrieval, freshness, reliability]
links:
  - forge/ideas/bounded-index-freshness-recheck-r01.md
  - forge/protocol.md
  - logbook/progress.log
  - logbook/errors.log
  - forge-index/query.py
  - forge-index/index.py
  - agentic-brain:governance/skills/query-brain-vps.md
  - agentic-brain:governance/skills/query-forge-vps.md
  - agentic-brain:research/insights/vps-brainclone-plus-index.md
  - agentic-brain:research/insights/stale-index-problem.md
  - https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
  - https://docs.cloud.google.com/storage/docs/retry-strategy
confidence: medium
---
# Research: Bounded Index Freshness Recheck

## Question and Method

This report investigates the root idea's exact question: can one bounded,
read-only freshness recheck after one natural watcher cycle avoid full Forge
session halts caused by transient index lag while every persistent, malformed,
unverified, missing-watcher, or changed-state case still halts before retrieval?[1]

Before targeted event reconstruction, the provisional explanation was that a
repository commit can move `HEAD` after the last completed index heartbeat. The
current freshness command will then correctly return `STALE`; the next existing
watcher tick can update the index, and the identical read-only command can then
return `OK --` without weakening the final gate. The principal gaps were whether
later literal `OK --` outputs were preserved, whether repository state stayed
unchanged between checks, whether a stage actually continued, and whether the
word `STALE` covers integrity faults that should not incur a wait.

The investigation used five source classes:

1. Historical `errors.log` and `progress.log` at Git commit
   `11b0425908ecdd0cc71bb54e483833ac466cdf55`, plus the corresponding Git commit
   chronology.[2]
2. Exact tool-result records from the three historical Hermes sessions named
   below. These operational records supplied second-level timestamps and literal
   command output, but they are not immutable repository artifacts.
3. Current Forge index source and the current Brain and Forge query skills, read
   in full.[3][4]
4. Current operational watcher and index-log windows, read without invoking the
   watcher or an index build. The checked fleet watcher script had SHA-256
   `9c31532554f233a7ed57cc49bde863f0bb400d3a1528089f96f937ef2a342031`.
   This runtime source is not stored in the Forge repository, so its exact bytes
   are a coverage limitation rather than durable artifact evidence.
5. The watcher blueprint, stale-index insight, and primary AWS and Google retry
   guidance.[5][6][7][8]

The replay candidate was frozen before executing its scratch classifier, but
after reconstructing the three events: at most one follow-up freshness check,
within 90 seconds of the first result. The ceiling was selected as one one-minute
cron interval plus 30 seconds for index work. This ordering creates tuning risk:
90 seconds was not preregistered before viewing the event durations. The policy
required the watcher line to remain present, the queried repository `HEAD` and
worktree snapshot to remain unchanged, and the second command itself to return
exit 0 with output beginning `OK --`. It never treated elapsed time, a watcher
log line, or stage completion as a substitute for that output.

No watcher, indexer, rebuild, cron, profile, runtime, or external repository was
changed. Source repositories and web sources were read-only. The scratch replay
was not installed or written into the Forge.

## Evidence and Findings

### The current gate is stronger than a simple HEAD check

The current validator permits retrieval only after exit 0 and a literal
`OK --`. It checks required artifacts, heartbeat and metadata schemas, model and
chunking agreement, counts, manifest coverage, chunk/vector shape and type,
live Markdown hashes, and `HEAD` equality.[3] The current query skills direct an
immediate HALT for `STALE`, `NO INDEX`, or `UNVERIFIED` and prohibit a manual
rebuild.[4] This is a consistency gate, not a liveness check, which matches the
stale-index lesson's central requirement.[6]

`STALE` is not one failure type. The current source emits that prefix for at
least missing index data, build-configuration disagreement, heartbeat/metadata
or count disagreement, vector inconsistency, live-corpus mismatch, and index
`HEAD` lag.[3] The two reconstructed successful recoveries are both the last
subtype. No preserved event demonstrates benefit for the other `STALE`
subtypes.

### Exact event reconstruction

The historical log records identify all three events and their eventual stage
outcomes.[2] Exact tool-result records add the literal first and second outputs:

| Event | Repository and first result | Natural-cycle evidence | Preserved second result | Elapsed between results | Stage outcome | Candidate replay |
|:--|:--|:--|:--|--:|:--|:--|
| 1 | Forge: `STALE -- index at 878347b8, HEAD at f8982b69` | Watcher heartbeat built at `2026-09-29T23:31:04` with no manual build | `OK -- 170 chunks, built 2026-09-29T23:31:04` | 60.7108438 s | Evaluation completed | Query after recheck |
| 2 | Brain: `STALE -- live corpus differs from manifest (new=0, changed=1, deleted=0)` | A natural watcher index run began at `2026-09-30T04:02:03`; no second freshness command was preserved | None | Unknown | Proposal session halted | HALT because the required second result is absent |
| 3 | Forge: `STALE -- index at ee82fca6, HEAD at ccc3bcad` | Watcher heartbeat built at `2026-09-30T05:01:03` with no manual build | `OK -- 348 chunks, built 2026-09-30T05:01:03` | 74.0969570 s | Proposal completed | Query after recheck |

The exact preserved windows were:

```text
Event 1 -- session cron_ba02ad681922_20260930_013012
2026-09-29T23:30:47Z  rc=1  STALE -- index at 878347b8, HEAD at f8982b69
2026-09-29T23:31:48Z  rc=0  OK -- 170 chunks, built 2026-09-29T23:31:04
```

```text
Event 2 -- session cron_efd72a9c8d29_20260930_060012
2026-09-30T04:01:30Z  rc=1  STALE -- live corpus differs from manifest (new=0, changed=1, deleted=0)
2026-09-30T04:01:50Z        Brain HEAD 7669b625e08f2b4e22c55a355a1ae54639863ec5; worktree clean
                         no second freshness result preserved
```

```text
Event 3 -- session cron_efd72a9c8d29_20260930_070012
2026-09-30T05:00:41Z  rc=1  STALE -- index at ee82fca6, HEAD at ccc3bcad
2026-09-30T05:01:55Z  rc=0  OK -- 348 chunks, built 2026-09-30T05:01:03
```

Git chronology shows no intervening Forge commit between either recovered pair.
The next Forge commit followed the second check in each case. Historical error
records also state that no manual rebuild or configuration change occurred.[2]

Events 1 and 3 are direct demonstrations of the proposed mechanism: the exact
same freshness command changed from a literal `STALE` to a literal `OK --`
inside the 90-second ceiling, and the selected stage subsequently completed.
However, both agents rechecked despite the then-current immediate-HALT rule.[4]
They are therefore evidence that the mechanism can work, but also evidence of a
procedural deviation. Event 2 is not a demonstrated recovery. A later watcher
log is suggestive, but the required second command is absent, so the replay
keeps it fail-closed rather than inferring success from later index or Git state.

### Frozen policy replay and negative fixtures

The scratch classifier used this decision order:

1. Missing watcher ownership -> HALT.
2. Initial exit 0 plus `OK --` -> query immediately.
3. Any initial result other than exit 1 plus `STALE --` -> HALT immediately.
4. Changed queried-repository `HEAD` or worktree before the second check -> HALT.
5. Missing second result or elapsed time above 90 seconds -> HALT.
6. Second exit 0 plus `OK --` -> query; every other second result -> HALT.

The classifier and output hashes were
`1be52b6d682d1067948788b8d8e9670bd30c4ed33da0cfe21541b133db7ca1f8`
and
`b309e3446254707b7de54d03548fd01888bacfc6eb04ab451275b1c1077542fe`.
The complete source bytes remain scratch-only, so the hashes do not establish an
independently reproducible package. The decision table below preserves every
reported classification:

| Case | Result |
|:--|:--|
| Event 1 Forge HEAD lag | `QUERY_AFTER_RECHECK` |
| Event 2 Brain, no preserved second check | `HALT_TIMEOUT_OR_MISSING_RECHECK` |
| Event 3 Forge HEAD lag | `QUERY_AFTER_RECHECK` |
| Persistent HEAD-lag `STALE` | `HALT_RECHECK_STATUS` |
| Persistent missing-index-data `STALE` | `HALT_RECHECK_STATUS` |
| Malformed second result | `HALT_RECHECK_STATUS` |
| Second result `UNVERIFIED` | `HALT_RECHECK_STATUS` |
| Initial `NO INDEX` | `HALT_INITIAL_STATUS` |
| Initial `UNVERIFIED` | `HALT_INITIAL_STATUS` |
| Missing watcher line | `HALT_MISSING_WATCHER` |
| Malformed initial output | `HALT_INITIAL_STATUS` |
| Repository state changed before recheck | `HALT_STATE_CHANGED` |
| Literal `OK --` after the 90-second ceiling | `HALT_TIMEOUT_OR_MISSING_RECHECK` |
| Initial literal `OK --` | `QUERY_INITIAL_OK` |

All 14 classifications matched their pre-run expected outcomes. This verifies
the classifier's declared branching, not the behavior of a modified query skill
or a live persistent failure. The negative fixtures are synthetic and derived
from the same policy they test. They show that the candidate contains no branch
that queries after a non-`OK --` result; they do not estimate production false
halts or prove the 90-second bound for future index workloads.

### Support criteria and contradictions

The root idea's affirmative thresholds are met only in a narrow sense:[1]

- Two preserved events reached literal `OK --` inside one 90-second ceiling.
- Both otherwise completed their Forge stage, so immediate HALT would have lost
  that scheduled stage.
- Every declared negative fixture halted before query.
- The candidate contains no query branch without a fresh literal `OK --`.
- The third named event is classifiable only as unrecovered because its second
  command is missing; no success is inferred.

The evidence does not justify treating every literal `STALE` alike. Current
source maps integrity and compatibility faults to the same prefix as ordinary
HEAD lag.[3] The strongest supported trigger is therefore smaller: one recheck
for an exact HEAD-lag result of the form `STALE -- index at <sha>, HEAD at <sha>`,
with immediate HALT for all other current `STALE` messages. That narrower rule
recovers both demonstrated events and avoids adding delay to missing-data,
configuration, shape, count, or live-corpus faults. Event 2 leaves the
live-corpus subtype unresolved.

AWS states that retries can absorb short-lived transient failures but can
increase load, and recommends waiting and limiting attempts.[7] Google Cloud
conditions retries on retryable status and idempotency and exposes explicit
attempt and timeout bounds.[8] These independent sources support the shape of a
single bounded retry for a read-only command. They do not establish that a
local Forge status is transient, choose the 90-second ceiling, or validate the
message subtype; the reconstructed events and current source must do that.

Source independence is limited. Events 1 and 3 occurred on the same repository,
same host, same watcher, and within one operating period. They are two events,
not two independent systems. The error log, Git history, watcher logs, and
session records are mutually corroborating records of those events, not
independent trials. No current production skill was modified or cold-tested.

## Alternatives and Implications

| Alternative | Evidence-supported benefit | Cost or limit |
|:--|:--|:--|
| Keep immediate HALT | Simplest rule and zero waiting; preserves the present fail-closed boundary.[4] | Would have stopped both exact HEAD-lag sessions that reached `OK --` in 60.7 and 74.1 seconds. |
| One recheck for exact HEAD-lag `STALE` | Recovers both demonstrated events while every other current status halts immediately. | Relies on the current text contract, uses a post-event 90-second ceiling, and has only two same-system examples. |
| One recheck for every literal `STALE` | The synthetic branch table still queries only after literal `OK --`. | Adds up to 90 seconds to integrity/configuration faults without demonstrated benefit; current evidence is overbroad for this option.[3] |
| Automatic rebuild, watcher invocation, or repeated polling | Could repair or observe more states. | Exceeds the idea and query-skill boundary, changes producer behavior, can hide a persistent fault, and is unsupported by this research.[4][6] |

The evidence supports independent evaluation of the exact HEAD-lag alternative,
not automatic implementation and not a general retry policy. A later proposal,
if evaluation advances the research, should require all of the following:

- verify the exact watcher line before the first check;
- snapshot the queried repository `HEAD` and worktree;
- permit exactly one wait and one second command only for the exact HEAD-lag
  message;
- use a fixed, explicit ceiling rather than polling;
- recheck the snapshot before the second command;
- continue only on second exit 0 plus literal `OK --`;
- report every other result and timeout as HALT;
- prohibit manual watcher runs, rebuilds, configuration changes, and a fallback
  to another repository index.

This would not weaken the consistency definition. It changes when a second
measurement is allowed. It also does not replace the Forge protocol's separate
pre-write check for board, log, `HEAD`, and worktree changes.

## Response to Feedback and Remaining Questions

No prior evaluation exists for this pipeline.

Confidence is medium for the narrow finding that one exact HEAD-lag recheck can
recover some transient Forge watcher intervals without querying stale data. It
rests on two literal STALE-to-OK sequences, unchanged Forge `HEAD`, completed
stages, exact current validator behavior, and a fail-closed branch replay. It is
low for generalizing to every `STALE` subtype or future workload. Confidence
would rise with a prospectively frozen 90-second rule that records another
natural HEAD-lag event, exact snapshots, and the second result before any policy
change. It would fall if a same-state HEAD-lag remains stale after one cycle, if
the message contract changes, or if waiting causes the Forge transaction
snapshot to change.

Decision-relevant questions remain:

- Is a fixed 90-second ceiling acceptable, or must a proposal obtain a
  prospective distribution of watcher start and build durations first?
- Should the eligible subtype be matched by exact output text, or should the
  query tool expose a structured status without changing the gate semantics?
- Does an unchanged queried-repository `HEAD` and clean worktree fully define
  unchanged state for Brain and Forge retrieval, or should manifest/heartbeat
  identities also be frozen before waiting?
- Is avoiding two same-hour scheduled-stage halts worth the added skill text and
  maximum wait when immediate HALT remains simpler?
- Can a prospective test preserve exact first and second outputs in a repository
  artifact without turning a research loop into a runtime monitor?

These are evaluation questions. This report does not issue `ADVANCE`, change a
query skill, or authorize deployment.

## Sources

1. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- root question,
   three-event reconstruction plan, fail-closed candidate, support thresholds,
   and excluded producer-side actions. [high]
2. `logbook/errors.log` -- historical ENT-009, ENT-016, and ENT-018 first-result
   and recovery summaries, verified at Git commit
   `11b0425908ecdd0cc71bb54e483833ac466cdf55`; exact tool outputs were
   cross-checked against the named Hermes session records. [high]
   - `logbook/progress.log` -- corresponding evaluation halt/completion and
     proposal completion records at the same historical commit. [high]
3. `forge-index/query.py` -- current full validator, status-message taxonomy,
   live-manifest and `HEAD` checks, and the exit-0 `OK --` contract. [high]
   - `forge-index/index.py` -- heartbeat update and incremental-reuse behavior
     checked for interpretation of the watcher build records. [high]
4. `agentic-brain:governance/skills/query-brain-vps.md` -- current Brain watcher,
   freshness, immediate-HALT, log-inspection, no-rebuild, and exact-OK procedure.
   [high]
   - `agentic-brain:governance/skills/query-forge-vps.md` -- matching current
     Forge procedure and failure boundary. [high]
5. `agentic-brain:research/insights/vps-brainclone-plus-index.md` -- one-minute
   watcher cadence, push/pull/index ownership, eventual-consistency design,
   fail-closed freshness requirement, and natural add/delete proofs. [medium]
6. `agentic-brain:research/insights/stale-index-problem.md` -- consistency versus
   liveness distinction and the current validator's artifact, schema, manifest,
   corpus, and `HEAD` coverage. [medium]
7. Amazon Web Services. "Timeouts, retries, and backoff with jitter," published
   2026-06-12 and modified 2026-06-15; accessed 2026-09-30, Failures Happen,
   Retries and backoff, and Conclusion sections. Transient-failure recovery,
   retry amplification, waiting, and attempt limits were checked.
   https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
   [medium]
8. Google Cloud. "Retry strategy," last updated 2026-08-26; accessed
   2026-09-30, idempotency, implementation, customization, and anti-pattern
   sections. Conditional retry, explicit attempts, timeout bounds, and
   non-idempotent retry risk were checked.
   https://docs.cloud.google.com/storage/docs/retry-strategy [high]
