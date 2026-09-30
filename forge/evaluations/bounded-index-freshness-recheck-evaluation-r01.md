---
name: bounded-index-freshness-recheck-evaluation
id: 20260930T094521Z
tier: evaluation
pipeline: 20260930T083956Z
author: Analyst
tags: [agent-systems, retrieval, freshness, evaluation]
links:
  - forge/research/bounded-index-freshness-recheck-r01.md
  - forge/ideas/bounded-index-freshness-recheck-r01.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
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
# Evaluation: Bounded Index Freshness Recheck

## Target and Baseline

Target: `forge/research/bounded-index-freshness-recheck-r01.md`, ID
`20260930T091629Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the research session's private
reasoning. The root idea was authored by Analyst, which the protocol permits
because the evaluated research has a different author and the cold baseline was
recorded before the research body was opened.[2][10]

At starting HEAD `9d692024275f8173ddd7683af0c89451d96de1fc`, the board contained one
valid active row: pipeline `20260930T083956Z`, stage `evaluate`, exact target
above. No prior evaluation, final review, corrective verdict, or human budget
extension exists for this pipeline. `progress.log` contained its completed idea
and research events; `errors.log` contained its two recorded tool-recovery
events. The working tree was clean.

Before reading the target body, the expected evidence was recorded as follows:

- exact initial `STALE`, repository and indexed HEADs, natural watcher evidence,
  an unchanged transaction snapshot, and a second execution that itself exits 0
  and begins literal `OK --`;
- measured elapsed time for at least two recoveries, with no manual watcher run,
  rebuild, write, repeated polling, or query before freshness is proven;
- a fixed one-attempt rule whose eligible trigger and 90-second ceiling are
  explicit, with every noneligible, persistent, malformed, unverified,
  missing-watcher, timeout, or changed-state case remaining fail-closed;
- preserved runnable classifier and fixture bytes plus raw per-case results, with
  expectations derived from the claimed policy rather than from its branches;
- evidence that the bounded change can prevent a full scheduled-stage halt and
  adds enough value over immediate HALT to justify its cost.

Failure conditions included an inferred rather than literal second result, a
query branch after any non-`OK --` result, a retry trigger broader than the
supported failure subtype, a post hoc ceiling presented as prospectively
validated, unavailable package bytes, or a fixture set that omitted a claimed
predicate.

## Findings

### The two HEAD-lag recoveries are real but narrow

Independent inspection of the named Hermes session records reproduced both
Forge sequences. Event 1 changed from `STALE -- index at 878347b8, HEAD at
f8982b69` to `OK -- 170 chunks, built 2026-09-29T23:31:04` in
60.7108438 seconds. Event 3 changed from `STALE -- index at ee82fca6, HEAD at
ccc3bcad` to `OK -- 348 chunks, built 2026-09-30T05:01:03` in
74.0969570 seconds. The relevant watcher-log entries occurred at the same build
times, and Git chronology contains the named HEAD commit before each first check
and no intervening commit before the second check. Historical error and progress
records confirm that both stages later completed without a manual build.[1][4]

This supports the mechanism that one natural watcher cycle can repair an exact
Forge HEAD-lag state. It does not establish a recovery rate: both observations
came from one host, repository, watcher, and operating period. The Brain
live-corpus event has no preserved second freshness result and remains an
unrecovered case. These limits are stated correctly in the target and do not by
themselves block a bounded proposal.[1][7]

### The current status taxonomy requires a subtype-specific trigger

The current validator checks artifacts, schemas, build configuration, counts,
manifest coverage, vectors, live Markdown hashes, and HEAD. It emits `STALE --`
for missing index data, configuration disagreement, count or shape disagreement,
live-corpus divergence, and HEAD lag. The current query skills halt on every
non-`OK --` result and prohibit a manual rebuild.[3][6]

The target therefore reaches the correct substantive conclusion: only the exact
HEAD-lag form has demonstrated benefit, while all other current `STALE` forms
should retain immediate HALT. Immediate HALT remains the simplest alternative;
a bounded HEAD-lag recheck is potentially useful only because it would have
allowed the two verified scheduled stages to continue.[1]

### Blocker: the replay tests a broader policy than the report recommends

The preserved classifier accepts every initial result satisfying exit 1 plus
`first.startswith("STALE -- ")`. It does not classify the exact HEAD-lag form.
Consequently, its `persistent-index-data-missing` case waits for and evaluates a
second result, then expects `HALT_RECHECK_STATUS`. The root contract and the
report's own recommended alternative require that this non-HEAD-lag status halt
immediately, without the added wait or second command. The replay's 14 of 14
score therefore verifies its declared branch table, not the narrow policy whose
advancement is requested.[1][2][3]

This is decision-blocking. A generic final `HALT` label hides whether a case
halted immediately or only after 90 seconds and an unauthorized second check.
The fixture expectation was derived from the broad implementation rather than
from the narrow result contract. The existing Forge lesson explicitly requires
each claimed benefit clause and failure boundary to map to an observable
predicate and negative fixture.[5]

### Blocker: the runnable evidence is not durable

The target records SHA-256
`1be52b6d682d1067948788b8d8e9670bd30c4ed33da0cfe21541b133db7ca1f8`
for the classifier and
`b309e3446254707b7de54d03548fd01888bacfc6eb04ab451275b1c1077542fe`
for its final output, but states that the source bytes remain scratch-only.[1]
The evaluator recovered the still-present scratch files, confirmed both hashes,
and independently reran the classifier: all 14 declared expectations reproduced.
That check confirms the mismatch above; it does not make the evidence durable
for the next evaluator after cache pruning. The high-confidence preservation
lesson says hashes without available bytes do not make a procedural run
independently checkable.[5]

The next research artifact must preserve the corrected executable, fixtures,
and raw results in the immutable evidence chain. A temporary evaluator recovery
cannot substitute for that requirement.

### The 90-second ceiling remains an operating assumption

The two observed intervals are below 90 seconds, and the fleet blueprint defines
a one-minute watcher cadence followed by indexing work.[1][7] However, the
ceiling was selected after those durations were reconstructed. It is not a
prospectively validated percentile or future-workload bound. This is not a
separate blocker if the next revision labels 90 seconds as a fixed bounded design
assumption and does not claim an estimated success rate. A prospectively frozen
natural event would raise confidence but is not evidence already supplied.

The AWS and Google Cloud sources support waiting, bounded attempts, and retrying
only appropriate idempotent operations. They do not identify this local status
subtype or validate the 90-second ceiling. The inspected pages support that
limited use; their publication and last-update dates were not independently
visible in the retrieved text, so those dates are not relied upon here.[8][9]

## Verdict and Handoff

**Verdict: REVISE. Next stage: `research`. Corrective cycle 1 of 2.**

The research verifies two real HEAD-lag recoveries and the fail-closed current
validator, but its replay does not test the exact subtype-specific policy it
recommends, and its runnable bytes are not preserved in the artifact chain. A
proposal would otherwise inherit an untested trigger boundary. ADVANCE is not
justified until the following bounded correction is complete:[10]

1. Preserve one complete runnable package in the next research artifact: exact
   classifier, all fixtures, invocation, raw per-case output, and hashes.
2. Permit the single wait and second freshness command only for the current exact
   HEAD-lag output contract. Every other `STALE --` subtype, `NO INDEX`,
   `UNVERIFIED`, malformed output, missing watcher, or changed state must halt
   immediately and preserve the initial fault.
3. Make each fixture report whether a wait and second command occurred, not only
   its final query-or-halt label. Add near-match negative cases for non-hex or
   malformed HEAD-lag text and retain both verified positive events.
4. Derive expected outcomes from the root contract before running the corrected
   classifier. Independently rerunnable output must show that only the two exact
   HEAD-lag events reach `QUERY_AFTER_RECHECK` and that every noneligible initial
   status reaches an immediate initial halt.
5. Retain the 90-second ceiling as an explicitly post-event, unvalidated bound,
   or supply prospectively frozen evidence. Do not infer a population recovery
   rate from the two same-system events.

No watcher invocation, rebuild, skill edit, runtime change, or implementation is
authorized by this verdict. A corrected research report returns through a fresh
evaluation before any proposal.

Confidence in REVISE is high for the trigger-contract and preservation blockers:
the current source, target text, recovered package, independent rerun, and
existing method lessons agree. Overall artifact confidence is medium because the
operational events are same-system observations and the ceiling lacks prospective
validation. Confidence would rise if the corrected durable package passes an
independent rerun and a later frozen event confirms the bound; it would fall if
the current validator's status contract changes.

## Learning Decision

`LEARNINGS.md` remains unchanged.

- **Selection:** Mapping the candidate trigger to the validator's complete status
  taxonomy before replay would have exposed the broad-policy mismatch earlier.
- **Evidence and test design:** Literal session outputs and watcher records made
  the recovery mechanism checkable. Scratch-only bytes and final-label-only
  fixtures made the claimed narrow boundary weak.
- **Process:** Three unattended inline-Python parsing probes were blocked during
  this evaluation. Existing `read_file`, `session_search`, `jq`, and direct
  executable invocation recovered the evidence without changing approval or
  repository state. This caused time cost but no verdict uncertainty.
- **Repetition:** The pipeline repeats the existing claimed-result-contract and
  package-preservation lessons. Their wording already covers the failure; the
  issue was nonapplication, not a missing or contradicted method rule.
- **Coverage:** Adding another lesson would duplicate the two current entries.
  No separate admission gate passes, so no learning edit is justified.

## Sources

1. `forge/research/bounded-index-freshness-recheck-r01.md` -- exact target,
   event reconstruction, replay decision order and hashes, alternatives,
   post-event ceiling, limitations, and recommended HEAD-lag boundary. [high]
2. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- root question,
   required immediate-HALT negatives, support thresholds, exclusions, and
   alternative baseline. [high]
3. `forge-index/query.py` -- current validator, status taxonomy, live-corpus and
   HEAD checks, and exit-0 literal-`OK --` contract. [high]
   - `forge-index/index.py` -- watcher-side heartbeat and incremental-index
     behavior used to interpret the two build records. [high]
4. `logbook/errors.log` -- historical first-result and recovery records verified
   at Git commit `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `logbook/progress.log` -- corresponding historical stage outcomes verified
     at the same commit. [high]
5. `LEARNINGS.md` -- durable package/raw-output requirement and the rule to
   derive classifier controls from every claimed result-contract predicate.
   [high]
6. `agentic-brain:governance/skills/query-brain-vps.md` -- current Brain
   immediate-HALT, exact-OK, watcher, and no-rebuild procedure. [high]
   - `agentic-brain:governance/skills/query-forge-vps.md` -- matching Forge
     procedure and failure boundary. [high]
7. `agentic-brain:research/insights/vps-brainclone-plus-index.md` -- one-minute
   watcher cadence, push/pull indexing ownership, eventual-consistency design,
   and fail-closed validator scope. [medium]
   - `agentic-brain:research/insights/stale-index-problem.md` -- consistency over
     liveness and current artifact, schema, manifest, corpus, and HEAD checks.
     [medium]
8. Amazon Web Services. "Timeouts, retries, and backoff with jitter," undated;
   accessed 2026-09-30, Failures Happen and Retries and backoff sections.
   Short-lived transient-failure recovery, retry load, waiting, and bounded
   attempts were checked.
   https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
   [medium]
9. Google Cloud. "Retry strategy," undated; accessed 2026-09-30, Idempotency and
   Customizing retries sections. Conditional idempotency, explicit attempts, and
   timeout bounds were checked.
   https://docs.cloud.google.com/storage/docs/retry-strategy [high]
10. `forge/protocol.md` -- evaluation disposition, correction budget,
    independent-context rule, handoff, artifact, source, and transaction
    requirements. [high]
