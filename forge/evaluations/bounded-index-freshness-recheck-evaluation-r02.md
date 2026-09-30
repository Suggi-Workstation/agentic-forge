---
name: bounded-index-freshness-recheck-evaluation
id: 20260930T103940Z
tier: evaluation
pipeline: 20260930T083956Z
author: Analyst
tags: [agent-systems, retrieval, freshness, evaluation]
links:
  - forge/research/bounded-index-freshness-recheck-r02.md
  - forge/ideas/bounded-index-freshness-recheck-r01.md
  - forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md
  - forge/research/bounded-index-freshness-recheck-r01.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - logbook/progress.log
  - logbook/errors.log
  - forge-index/query.py
  - agentic-brain:brain-index/query.py
  - agentic-brain:governance/skills/query-brain-vps.md
  - agentic-brain:governance/skills/query-forge-vps.md
  - agentic-brain:research/insights/stale-index-problem.md
  - agentic-brain:research/insights/vps-brainclone-plus-index.md
  - https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
  - https://docs.cloud.google.com/storage/docs/retry-strategy
confidence: medium
---
# Evaluation: Bounded Index Freshness Recheck, Corrected Replay

## Target and Baseline

Target: `forge/research/bounded-index-freshness-recheck-r02.md`, ID
`20260930T101043Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the research drafting session's
private reasoning. The root idea and prior evaluation were authored by Analyst;
the protocol permits this because the evaluated research has a different author
and the cold baseline preceded the target-body read.[2][3][12]

At starting HEAD `a36e81d195ded375e9e841406ab22d7023bff5a5`, the board
contained one valid active row: pipeline `20260930T083956Z`, stage `evaluate`,
and the exact target above. The working tree was clean. Current progress events
ended at ENT-004 with the corrected research handoff, current errors ended at
ENT-004, and no human budget extension was recorded.[9][13] One prior REVISE
verdict had used corrective cycle 1 of 2.[3][12]

Before reading the target body, the expected evidence and failure conditions
were recorded in evaluator task scratch. The expected evidence was:

- a complete classifier, frozen fixtures, invocation, raw per-case output, and
  hashes recoverable from the immutable target;
- an exact current HEAD-lag trigger, with observable `waited` and
  `second_checked` actions and an initial halt for every noneligible status;
- both verified positive events reaching query only after a second exit 0 and
  literal `OK --`, plus near-match and fail-closed controls;
- expectations derived from the root contract and prior evaluation before the
  classifier run, followed by an independent extraction and rerun; and
- explicit limits on the post-event 90-second ceiling, same-system events,
  shell integration, recovery rate, and implementation authority.

Failure conditions included missing or changed package bytes, a non-HEAD-lag
status that waited or ran a second command, query after any non-`OK --` result,
implementation-derived expectations, a hash or rerun mismatch, or a claim that
synthetic replay established future timing or live shell behavior.

## Findings

### The durable package reproduces exactly

The target embeds the complete classifier, 22 fixtures with expected action
fields, invocation, and raw output.[1] Independent extraction preserved the
final newlines and produced these exact hashes:

- classifier: `095f00ff91dae2d2cb0e7a862149a41d9e37931da469c7636ea912da29834f5f`;
- fixtures: `dfeb190028382e5f956189d06e4db041b925bf7f5510d8ead72929995db1dbeb`;
- reported raw output: `f1da6f6ff40ff9f35dd16684bb3a638dcb2ba6f875129fc9cb84ad8925302165`.

The extracted classifier compiled. Two independent executions each exited 0,
returned `summary=22/22`, and produced the same raw-output hash. Byte comparison
between the embedded output and each evaluator run exited 0. This closes the
prior package-preservation blocker: the result no longer depends on
scratch-only bytes or a hash without recoverable evidence.[1][3][6]

### The corrected trigger matches the current validator branch

The current Forge and Brain validators are identical in the relevant logic.
After artifact, schema, configuration, count, shape, corpus, and metadata checks,
each emits `STALE -- index at <8 chars>, HEAD at <8 chars>` only for heartbeat
HEAD inequality; success returns exit 0 with `OK --`.[5][8] The current query
skills require that success result, halt on all failed freshness results, and
prohibit a manual rebuild.[7]

The corrected classifier requires initial exit 1 and a full-string match on two
eight-character hexadecimal fields. In the reproduced output, only the two
historical exact HEAD-lag cases reached `QUERY_AFTER_RECHECK`. Live-corpus,
missing-data, configuration, `NO INDEX`, `UNVERIFIED`, missing-watcher,
nonhex, short, missing-comma, trailing-text, malformed, and nonzero-exit initial
cases all halted with `waited=false` and `second_checked=false`. Persistent exact
HEAD lag and failed second checks halted after one check; timeout, absent second
result, and changed state never reached that command. No case queried without
second exit 0 plus literal `OK --`.[1][5]

The fixtures now expose the action boundary that the first replay hid behind a
final HALT label. Their expected results were frozen before execution, and the
independent rerun verified the declared contract rather than only a broad
implementation branch.[1][3][6] This closes the prior trigger-contract blocker.

### The operational evidence remains narrow but sufficient for a proposal

Two preserved Forge sequences changed from exact HEAD-lag `STALE` to literal
`OK --` after 60.7108438 and 74.0969570 seconds, with no intervening Forge
commit or manual build; their stages then completed. Historical Forge logs
corroborate the faults and natural recovery.[1][3][4][9] These observations show
that the candidate could avoid a full scheduled-stage halt in the demonstrated
condition. They do not estimate a recovery probability: both events share one
host, repository, watcher, and operating period.

The 90-second ceiling was selected after those events. It is a bounded design
assumption, not a prospective percentile or service guarantee. The classifier
models elapsed time and `state_unchanged`; it does not perform a wait, capture a
live snapshot, invoke a query skill, or test the race between shell commands.[1]
Those limits are stated explicitly. They do not block a proposal, but they must
remain acceptance-test obligations rather than be described as validated
behavior.

Immediate HALT remains the simplest policy and avoids every wait. Exact-text
matching is coupled to the validator's current human-readable output, while a
structured status would be more robust but requires a larger, untested tool
change.[1][5] The two demonstrated avoided halts are enough to justify comparing
those alternatives in a concrete proposal; they are not enough to establish
that adoption has positive fleet-wide economics.

### External retry guidance supports the shape, not the local result

AWS describes bounded retry and backoff as protection against transient failure
while warning that retries add load and can repeat side effects. Google Cloud
distinguishes retryable and idempotent operations and exposes explicit attempt
and timeout controls.[10][11] A read-only freshness check with one subtype-bound
attempt fits that general shape. Neither source validates the local text
contract, the 90-second ceiling, the two events, or a future benefit rate. The
research correctly relies on local source and records for those claims.

No contrary source establishes that the candidate has already been integrated,
that all HEAD-lag events recover, or that every `STALE` should wait. The target
makes none of those claims.[1]

## Verdict and Handoff

**Verdict: ADVANCE. Next stage: `propose`. One prior REVISE has used corrective
cycle 1 of 2; this ADVANCE uses no additional corrective cycle.**

The corrected research answers every actionable item in the prior verdict. Its
package is durable and independently reproducible, the eligible trigger is the
exact current HEAD-lag branch, action fields distinguish immediate halt from a
wait and second command, near matches fail closed, expectations precede the
run, and the ceiling remains explicitly unvalidated.[1][3] The evidence now
supports drafting a bounded proposal. ADVANCE is not approval and grants no
implementation authority.[12]

The proposal must:

1. Name the exact query-skill files and preserve the existing freshness
   definition: retrieval remains forbidden until a freshness command exits 0
   and begins literal `OK --`.
2. Permit one wait and one second command only after initial exit 1 with the
   current full HEAD-lag text. Every other initial result must retain immediate
   HALT, its original fault, and no wait or second check.
3. Define the one-attempt ceiling, watcher-presence check, repository `HEAD` and
   worktree snapshots, post-wait comparison, timeout behavior, and reporting
   without invoking the watcher, rebuilding, polling repeatedly, or changing
   runtime state.
4. Include shell-level acceptance tests for output capture, whitespace and exit
   handling, unchanged-state checks, state-change races, timeout, and every
   fail-closed branch. The embedded 22-case package is a classifier control,
   not evidence that this wiring already works.
5. Keep the 90-second value labeled as a post-event assumption, the two events
   labeled same-system observations, and implementation benefit unestimated.
6. Compare exact-text coupling with immediate HALT and a structured validator
   status, including maintenance cost, failure modes, rollback, and the option
   to do nothing.

Confidence in the corrected classifier result and blocker closure is high
because exact target bytes, current validator source, independent execution,
and byte comparison agree. Overall artifact confidence is medium because the
operational positives are same-system historical observations, the ceiling is
post-event, and shell integration remains untested. Confidence would rise after
a proposal defines and then separately obtains authorization for a passing
shell-level acceptance test under a frozen bound. It would fall if the status
contract changes or state can change between checks without a fail-closed
result.

## Learning Decision

Update the existing `Derive evaluator and checker controls from the claimed
result contract` lesson; add no new lesson.[6]

- **Selection:** Mapping the proposed retry trigger to the validator's complete
  status taxonomy before the first replay would have exposed the overbroad
  `startswith("STALE -- ")` branch before research publication.
- **Evidence and test design:** Recoverable package bytes, expected action fields,
  near-match controls, and byte-identical independent output made the corrected
  boundary decisive. The same-system event set and untested shell layer keep the
  domain conclusion limited.
- **Process:** The first evaluator rerun command selected an output directory as
  its working directory before the extraction step had created it. The command
  failed without a repository write; rerunning extraction from its existing
  parent directory restored the intended sequence and changed no evidence. This
  local sequencing error warrants an error event, not a new method lesson.
- **Repetition:** The first research revision repeated the existing
  claimed-contract lesson. The corrected revision applied it: every claimed
  trigger and action boundary acquired an observable field or negative fixture,
  and the independent 22-case rerun matched all expectations.
- **Coverage:** The existing lesson already names this method. This third
  independent pipeline is a later application showing that the lesson enabled
  an independently checkable correction, so its confidence can rise from medium
  to high under the admission rule. The already-high package-preservation lesson
  needs no wording change.

This edit is a reusable evaluation-method update, cites the current pipeline,
and grants no governance, skill, runtime, or deployment permission. It passes
the separate admission gate after this completed evaluation.[6]

## Sources

1. `forge/research/bounded-index-freshness-recheck-r02.md` -- exact target,
   complete embedded package, frozen expectations, raw output, corrected
   boundary, alternatives, and stated limits. [high]
2. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- root question,
   support thresholds, fail-closed conditions, exclusions, and immediate-HALT
   alternative. [high]
3. `forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md` -- prior
   REVISE verdict, independently checked event evidence, exact correction
   requirements, and corrective-cycle count. [high]
4. `forge/research/bounded-index-freshness-recheck-r01.md` -- antecedent event
   reconstruction, first broad replay, operational limits, and narrow
   recommendation. [high]
5. `forge-index/query.py` -- current Forge validator taxonomy, hexadecimal SHA
   validation, HEAD-lag output branch, and exit-code contract. [high]
   - `agentic-brain:brain-index/query.py` -- matching Brain validator branch and
     success contract independently compared with the Forge source. [high]
6. `LEARNINGS.md` -- package-preservation admission standard and the existing
   lesson requiring controls from every claimed result-contract predicate.
   [high]
7. `agentic-brain:governance/skills/query-brain-vps.md` -- current Brain
   watcher, exact-OK, immediate-HALT, and no-rebuild procedure. [high]
   - `agentic-brain:governance/skills/query-forge-vps.md` -- matching Forge
     procedure and read-only freshness gate. [high]
8. `agentic-brain:research/insights/vps-brainclone-plus-index.md` -- natural
   one-minute watcher cadence, watcher ownership, fail-closed validation, and
   multi-repository architecture. [medium]
   - `agentic-brain:research/insights/stale-index-problem.md` -- consistency over
     liveness and current validator coverage. [medium]
9. `logbook/errors.log` -- current pipeline error state and historical STALE
   records ENT-009, ENT-016, and ENT-018 checked at Git commit
   `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `logbook/progress.log` -- current handoff chain and matching historical
     stage outcomes checked at the same commit. [high]
10. Amazon Web Services. "Timeouts, retries, and backoff with jitter," undated;
    accessed 2026-09-30, Failures Happen and Retries and backoff sections.
    Transient-failure recovery, retry load, waiting, and idempotency were
    checked.
    https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
    [medium]
11. Google Cloud. "Retry strategy," undated; accessed 2026-09-30, idempotency,
    customization, and retry-setting sections. Conditional retries, attempt
    bounds, and timeout controls were checked.
    https://docs.cloud.google.com/storage/docs/retry-strategy [high]
12. `forge/protocol.md` -- independence, disposition, correction budget,
    artifact, source, learning, handoff, and transaction requirements. [high]
13. `STATUS.md` -- selected row, exact target, and pre-write board state. [high]
