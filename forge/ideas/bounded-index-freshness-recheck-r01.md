---
name: bounded-index-freshness-recheck
id: 20260930T083956Z
tier: idea
pipeline: 20260930T083956Z
author: Analyst
tags: [agent-systems, retrieval, freshness, reliability]
links:
  - ANCHOR.md
  - forge/protocol.md
  - agentic-brain:governance/skills/query-brain-vps.md
  - agentic-brain:governance/skills/query-forge-vps.md
  - agentic-brain:research/insights/vps-brainclone-plus-index.md
  - agentic-brain:research/insights/stale-index-problem.md
  - https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
  - https://docs.cloud.google.com/storage/docs/retry-strategy
confidence: low
---
# Bounded Index Freshness Recheck

## Question and Value

Can one bounded, read-only freshness recheck after the next existing watcher
cycle prevent avoidable Forge-stage halts caused by a transient literal `STALE`
result, while every persistent `STALE`, `NO INDEX`, `UNVERIFIED`, missing-watcher,
or changed-repository case remains fail-closed?

The target is the freshness procedure shared by the VPS repository-query skills,
starting with `query-brain-vps` and `query-forge-vps`. Both current skills require
an immediate HALT on any non-`OK --` result, while the documented producer is an
eventually consistent watcher that synchronizes and indexes each repository on
a one-minute schedule.[3][4] Forge agents benefit if a known transient producer
lag can be distinguished from a persistent integrity fault without running the
watcher, rebuilding an index, weakening the consistency check, or querying stale
content. This is direct ANCHOR Path A work on retrieval reliability and failure
recovery.[1]

The provisional hypothesis is that one recheck, only after a literal `STALE`
and one natural watcher cycle, will convert some recorded false starts to a
literal `OK --` while preserving the same final gate. A credible alternative is
that immediate HALT is the correct and simplest policy: `STALE` can signal a
failed producer or concurrent repository change, and waiting may merely delay a
necessary failure. The idea is not worth pursuing if the recorded events cannot
be reconstructed, if they do not resolve within one bounded cycle, if a recheck
could authorize a query without a new literal `OK --`, or if the saved work is
smaller than the added procedure and waiting cost.

## Origin and Prior Work

This is direct ideation under ANCHOR Path A, Agent Systems. The observed lead is
three exact historical Forge error records: ENT-009 and ENT-018 report an initial
Forge-index `STALE`, and ENT-016 reports a Brain-index `STALE` that prevented the
required query. The first and third records say the existing watcher later
indexed the relevant repository naturally; the middle record preserved the
stage input rather than treating missing retrieval as evidence.[2] These are
three operational events across two repositories, not three independent tests,
and the active logs were reset in the later fresh-start commit. Research must
therefore reconstruct their timing and exact HEAD transitions rather than infer
a retry policy from their summaries.

Current prior knowledge creates a deliberate tension. The VPS live-mirror
blueprint accepts a one-minute convergence bound, gives the watcher ownership of
push, pull, and incremental indexing, and requires read-time freshness checks to
fail closed.[4] The stale-index insight explains why a healthy-looking but
incomplete index must never be queried and records that the current validator
checks HEAD, manifests, Markdown hashes, shapes, and counts rather than mere
liveness.[5] The present query skills implement that safety boundary by halting
immediately on `STALE`, `NO INDEX`, or `UNVERIFIED`; they do not distinguish one
transient producer interval from a persistent fault.[3] The unresolved question
is therefore not whether stale search is acceptable. It is whether one bounded
second consistency check can reduce false starts without changing what counts
as fresh.

General retry guidance supports only a constrained experiment. Amazon reports
that retries can absorb short-lived transient failures but can also amplify load,
and recommends waiting and limiting attempts.[6] Google Cloud documentation
conditions retries on retryable errors and operation idempotency and exposes
explicit attempt and timeout bounds.[7] A repository freshness probe is
read-only, but those sources do not establish that this local `STALE` state is
transient or that one retry has net value; the Forge evidence must decide that.

At starting commit `1221b88dec13f0934f06913ed83e012ac0b26d8b`, the
`forge/graveyard/`, `forge/ideas/`, and `forge/proposals/` directories contained
no artifact Markdown files, and `STATUS.md` had no data row.[9] Historical ideas, proposals,
graveyard verdicts, final reviews, and the complete prior progress log were
searched for `stale`, `freshness`, `watcher`, `retry`, `recheck`, and `query`
terms. The closest historical pipeline, `unattended-forge-command-paths`,
reached READY for a Forge-protocol paragraph about approval-denied command
selection. It did not address index freshness, natural watcher lag, or a second
consistency check, and no explicit Suggi disposition was logged before the
fresh-start reset.[2][8] The transaction-checker pipeline closed DEFER after a
real-record false rejection and exhausted correction budget; reopening it would
require a human extension and comparative evidence, neither of which exists.[8]
The SBC-buyback pipeline is a distinct Path B accounting question.[8]

The strongest alternative candidate was reopening the transaction-checker work
to automate Forge transaction validation. It lost because that pipeline has an
exact DEFER closure, an exhausted correction budget, and no changed prerequisite.
The freshness question instead starts from three later tool-gate events, changes
no transaction checker, and can be tested with read-only historical sequences.

## Research Plan

Use one bounded reconstruction and replay unit:

1. Freeze the three historical error entries, the matching progress events,
   current Brain and Forge query-skill procedures, watcher documentation, and
   the relevant per-repository index-log windows. Keep query-reported `STALE`
   distinct from the watcher's own internal "stale without new sync event"
   message; they are not interchangeable observations.
2. For each event, reconstruct the queried repository HEAD, heartbeat HEAD,
   first freshness result, next natural watcher start and completion, and the
   first later literal `OK --` if one was actually preserved. Mark absent data
   unknown. Do not infer success from a later stage completion alone.
3. Compare the current immediate-HALT baseline with one candidate policy: only
   a literal `STALE` may wait for one predeclared watcher-cycle ceiling and run
   the same read-only freshness command once more. `NO INDEX`, `UNVERIFIED`, a
   missing watcher, malformed output, a still-stale recheck, or an unexpected
   repository/board/worktree change halts immediately. No query runs until the
   recheck itself returns exit 0 and begins `OK --`.
4. Replay both policies against the preserved event sequences. Preserve the
   decision table and raw source windows before synthesis. Count a recovered
   event only when the same repository reaches a verified matching HEAD inside
   the frozen ceiling without a manual watcher run, index build, repository
   write, or ignored transaction change.
5. Add negative fixtures for persistent `STALE`, `NO INDEX`, `UNVERIFIED`,
   missing cron ownership, malformed output, and changed repository state. The
   candidate must produce the same HALT and fault report as the current rule for
   every negative fixture.
6. Compare doing nothing, one bounded recheck, and automatic rebuild or repeated
   polling. Keep doing nothing as the baseline. Exclude rebuilds, watcher
   invocation, repeated polling, cron changes, and runtime changes from any
   recommendation.

Research supports a proposal only if the source record is complete enough to
classify every named event, at least two events reach a literal `OK --` within
one natural watcher cycle, at least one otherwise completed Forge stage would
avoid a full-session halt, every negative fixture remains fail-closed, and the rule
adds no query before freshness is proven. If any criterion fails, retain the
immediate-HALT procedure or report the evidence as insufficient.

Confidence is low. Exact error records, current skill text, and the watcher
blueprint establish a real policy boundary and a plausible transient interval,
but the event summaries do not preserve every first and second command or
elapsed duration.[2][3][4] Confidence would rise if the operational windows
reconstruct matching HEAD transitions and the frozen replay passes every
negative fixture. It would fall if any reported recovery lacks a literal later
`OK --`, exceeds one natural cycle, coincides with unexpected repository change,
or requires a producer-side action.

## Sources

1. `ANCHOR.md` -- Path A mission fit, recurring-failure selection prompt,
   bounded-test criteria, and non-duplicate requirement. [high]
2. `logbook/errors.log` -- historical ENT-009, ENT-016, and ENT-018 `STALE`
   records and recorded recoveries, verified at Git commit
   `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `logbook/progress.log` -- exact historical stage handoffs and absence of an
     explicit Suggi decision on the READY command-path proposal at the same
     commit. [high]
3. `agentic-brain:governance/skills/query-brain-vps.md` -- current watcher,
   freshness, immediate-HALT, log-inspection, and no-rebuild procedure. [high]
   - `agentic-brain:governance/skills/query-forge-vps.md` -- matching current
     Forge-index freshness and immediate-HALT procedure. [high]
4. `agentic-brain:research/insights/vps-brainclone-plus-index.md` -- one-minute
   watcher design, push/pull indexing ownership, eventual-consistency bound,
   fail-closed freshness check, and three-repository sibling architecture.
   [medium]
5. `agentic-brain:research/insights/stale-index-problem.md` -- stale-index failure
   modes, consistency-versus-liveness distinction, and current full-validator
   scope. [medium]
6. Amazon Web Services. "Timeouts, retries, and backoff with jitter," undated;
   accessed 2026-09-30, Failures Happen and Retries and backoff sections.
   Transient-failure benefit, retry load risk, waiting, and bounded attempts were
   checked.
   https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
   [medium]
7. Google Cloud. "Retry strategy," undated; accessed 2026-09-30, idempotency,
   implementation, customization, and anti-pattern sections. Conditional retry,
   attempt limits, and timeout bounds were checked.
   https://docs.cloud.google.com/storage/docs/retry-strategy [high]
8. `forge/ideas/unattended-forge-command-paths-r01.md` -- historical closest
   idea and its distinct approval-denial command-selection scope, verified at
   Git commit `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `forge/proposals/unattended-forge-command-paths-r03.md` -- exact historical
     pending proposal and bounded adoption design at the same commit. [high]
   - `forge/final-reviews/unattended-forge-command-paths-review-r03.md` -- READY
     verdict, remaining limits, and no-approval boundary at the same commit.
     [high]
   - `forge/graveyard/evidence-gated-forge-transaction-checker-evaluation-r03.md`
     -- DEFER closure, exhausted correction budget, and reopening conditions at
     the same commit. [high]
   - `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- compared historical
     Path B measurement question at the same commit. [high]
9. `STATUS.md` -- empty current board and new-idea selection baseline at starting
   commit `1221b88dec13f0934f06913ed83e012ac0b26d8b`. [high]
   - `logbook/progress.log` -- reset active progress log at the same commit.
     [high]
   - `logbook/errors.log` -- reset active error log at the same commit. [high]
