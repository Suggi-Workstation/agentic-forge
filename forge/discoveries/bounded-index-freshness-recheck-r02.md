---
name: bounded-index-freshness-recheck
id: 20260930T120257Z
tier: discovery
pipeline: 20260930T083956Z
author: Researcher
tags: [agent-systems, retrieval, freshness, discovery]
links:
  - forge/final-reviews/bounded-index-freshness-recheck-review-r02.md
  - forge/proposals/bounded-index-freshness-recheck-r02.md
  - forge/ideas/bounded-index-freshness-recheck-r01.md
confidence: medium
---
# Discovery: Bounded Exact-HEAD-Lag Freshness Recheck

## Decision

Approve, for separately authorized implementation and review, a narrow amendment
to the Brain and Forge VPS query skills: permit one bounded wait and one second
read-only freshness command only after the first command exits 1 with the exact
current HEAD-lag output. This discovery is not approval to implement the change.[1][2]

## What Changes

The only proposed production-source edits are the freshness procedure, failure
handling, and hard-gate checklist in:

- `agentic-brain:governance/skills/query-brain-vps.md`;
- `agentic-brain:governance/skills/query-forge-vps.md`.

Today, both skills halt after every failed freshness command. The amendment
recognizes only this complete newline-terminated one-line result, with empty
stderr and exit code 1:[1]

```text
STALE -- index at <8 hexadecimal characters>, HEAD at <8 hexadecimal characters>
```

Before the first check, the procedure verifies the existing watcher and captures
`HEAD` plus the byte-exact NUL-delimited worktree status. An eligible result may
sleep once until 30 seconds after the next minute boundary, provided the computed
delay is 1-90 seconds and monotonic elapsed time remains at most 90 seconds. It
then compares repository state, executes the same freshness command once, and
compares state again. The query may run only after unchanged-state checks, a
second exit code 0 with stdout beginning literal `OK --`, and successful cleanup
of task-owned scratch files. Every other initial or second result, state change,
timing fault, interruption, instrumentation failure, or cleanup failure halts;
the initial fault is preserved.[1][2]

No indexer, watcher, rebuild, polling loop, fallback repository, validator, cron,
service, runtime, installed skill, or `query-investing-vps` change is included.
The freshness definition does not change.[1]

## Why

Two preserved Forge events changed from the exact HEAD-lag result to literal
`OK --` after 60.7108438 and 74.0969570 seconds without a manual build, and both
stages then completed. A frozen 22-case classifier and two independent evaluator
runs each returned 22/22: only those exact HEAD-lag cases reached a query after
recheck, while every noneligible initial result halted without waiting or running
a second command.[1][2]

That evidence supports a bounded implementation test, not a measured operating
benefit. Both positive events came from one host, repository, watcher, and period;
the 90-second ceiling was selected after the events and is not a percentile or
service guarantee. Prospective recovery rate, future watcher duration, and net
fleet benefit are unknown. The classifier did not test shell-level waiting,
snapshot capture, cleanup ordering, or the exact skill bytes; the proposed shell
path remains unexecuted. Exact matching also couples the skills to human-readable
validator output. The two state comparisons narrow but do not remove the
check-to-use interval between the final comparison and query execution; atomic
exclusion is not claimed.[1][2]

Immediate HALT is the simplest alternative and remains the default for every
noneligible result and the rollback. Retrying every `STALE --` result is rejected
because other subtypes report integrity, configuration, shape, count, and live-
corpus faults. A structured validator status is more robust in principle but
requires an unresearched interface change. Rebuilds, watcher invocation, and
repeated polling exceed the read-only boundary. Costs include up to 90 seconds of
delay on an eligible result, duplicated skill logic that can drift, exact-text
coupling, scratch cleanup, and more complex diagnosis; their frequency is not
estimated.[1][3]

## How to Apply and Reverse

A separately authorized implementer should:[1][2]

1. Freeze both source skills and the current producer text. Build a scratch-only
   Bash harness whose watcher, Git snapshots, clock, sleep, freshness command,
   cleanup, and query are executable stubs with an invocation trace.
2. Run the proposal's complete matrix against both repository substitutions. It
   must grade the final decision and exact counts for watcher checks, snapshots,
   waits, freshness calls, cleanup, and queries. Coverage includes immediate
   success; lower- and upper-case eligible text; every current non-HEAD-lag
   `STALE`, `NO INDEX`, and `UNVERIFIED` class; watcher/crontab failure; malformed
   bytes, whitespace, newline, stderr, and exit-code cases; state changes before,
   during, and after the wait and second command; timer and sleep faults; every
   failed second result; and scratch, comparison, or cleanup failure.
3. Require no query after any failed gate, including cleanup. Also require the
   preserved classifier to return 22/22 while labeling it non-shell evidence;
   no producer-side action or polling; `bash -n`; ASCII-only source bytes;
   semantically equivalent decision blocks after repository constants are
   removed; and preservation of existing immediate-HALT messages and the literal-
   `OK --` retrieval gate.
4. Insert only the tested sequence into the two source skills, then rerun the
   matrix against the exact inserted bytes. Preserve fixtures, exact tested
   bytes, raw traces, and results. Run applicable format, ASCII, link, and diff
   checks and confirm that only the two authorized source files changed.
5. Stop for separate approval, propagation, deployment, and prospective
   observation. Do not manufacture a live stale state, invoke a watcher, or
   rebuild an index.

Rollback is direct: remove both bounded-recheck blocks and restore unconditional
immediate HALT after every failed first freshness command. No index, watcher,
cron, repository data, service, or runtime migration must be reversed. A
validator-message change triggers rollback until the eligibility contract is
reviewed. If atomic exclusion becomes required, this skill-only design is invalid
and the structured/helper alternative needs new research.[1][2]

## Confidence

Confidence is medium. Preserved bytes, current validator source, and independent
22/22 runs give high confidence in the exact classifier boundary, but the two
positive events are same-system observations, the ceiling is post-event, and the
shell integration is untested. Confidence would rise after the exact shell bytes
pass every matrix row in both skill variants and a prospective natural HEAD-lag
event is preserved. It would fall after producer-text drift, a failed state-race
fixture, lag beyond the bound, a query after any gate or cleanup failure, or
maintenance cost disproportionate to avoided halts.[1][2]

## Sources

1. `forge/proposals/bounded-index-freshness-recheck-r02.md` -- exact proposed
   change, evidence, limitations, alternatives, normative sequence, acceptance
   matrix, rollback, and separate-authorization boundary. [high]
2. `forge/final-reviews/bounded-index-freshness-recheck-review-r02.md` -- READY
   verdict for the exact proposal, implementation-conformance clarification,
   retained limitations, residual race, and no-implementation boundary. [high]
3. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- root question,
   fail-closed boundary, support threshold, excluded producer actions, and
   immediate-HALT alternative. [high]
