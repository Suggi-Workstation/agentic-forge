---
name: bounded-index-freshness-recheck
id: 20260930T110901Z
tier: proposal
pipeline: 20260930T083956Z
author: Researcher
tags: [agent-systems, retrieval, freshness, reliability]
links:
  - forge/ideas/bounded-index-freshness-recheck-r01.md
  - forge/research/bounded-index-freshness-recheck-r01.md
  - forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md
  - forge/research/bounded-index-freshness-recheck-r02.md
  - forge/evaluations/bounded-index-freshness-recheck-evaluation-r02.md
  - forge/protocol.md
  - LEARNINGS.md
  - forge-index/query.py
  - agentic-brain:governance/skills/query-brain-vps.md
  - agentic-brain:governance/skills/query-forge-vps.md
  - agentic-brain:research/insights/vps-brainclone-plus-index.md
  - agentic-brain:research/insights/stale-index-problem.md
  - https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
  - https://docs.cloud.google.com/storage/docs/retry-strategy
confidence: medium
---
# Proposal: Bounded Exact-HEAD-Lag Freshness Recheck

## Proposed Decision

The current VPS query skills halt after every failed freshness command. That
rule protects retrieval consistency, but it also ends a scheduled stage when
the sole fault is that the index heartbeat trails the repository `HEAD` until
the next watcher tick.[1] Two preserved Forge events changed from that exact
fault to literal `OK --` in 60.7108438 and 74.0969570 seconds without a manual
build, and both stages then completed.[2][3]

The requested decision is to approve, for separate implementation and review,
a narrow skill-rule amendment in exactly these existing source files:

- `agentic-brain:governance/skills/query-brain-vps.md`;
- `agentic-brain:governance/skills/query-forge-vps.md`.

The amendment permits one bounded wait and one second execution of the same
read-only freshness command only when the first command exits 1 and emits the
current exact one-line HEAD-lag form:

```text
STALE -- index at <8 hexadecimal characters>, HEAD at <8 hexadecimal characters>
```

Retrieval remains forbidden unless the second command exits 0 and its output
begins literal `OK --`. The queried repository's `HEAD` and byte-exact worktree
status must remain equal to their pre-check snapshots before and after the wait
and across the second check. Every other failed initial result retains immediate
HALT, its original fault, no wait, and no second command.[3][5]

This is a skill/rule amendment, not an indexer, watcher, or runtime change. Its
beneficiaries are unattended agents whose required Brain or Forge query begins
inside the short interval between a committed repository change and the next
watcher-owned index update. It changes when one second measurement is allowed;
it does not change what counts as fresh.

Non-goals are automatic rebuilds, manual watcher invocation, repeated polling,
a retry for any other `STALE` subtype, a fallback to another repository, cron
or validator changes, edits to `query-investing-vps`, deployment, or a claim
that the 90-second ceiling is a measured service level. The Forge loop grants
no implementation authority.[12]

## Evidence, Alternatives, and Evaluation Response

### Smallest useful change

In plain terms, the watcher may be one cycle behind even though nothing is
broken. The smallest useful response is not to trust stale data and not to
repair the producer. It is to recognize only the validator's exact HEAD-lag
message, wait once for the already configured producer, prove that repository
state did not change, and ask the same validator once more. A fresh second
result permits the existing query; any ambiguity still halts.

The corrected research package froze 22 expectations before execution. The
preserved package and two independent evaluator runs each returned 22/22. Only
the two observed exact HEAD-lag events reached `QUERY_AFTER_RECHECK`; every
noneligible initial status halted without a wait or second command.[2][3] The
prior REVISE had identified the broad trigger and unavailable package bytes as
blocking defects; the correction applies the Forge's existing requirements for
durable evidence and controls derived from the claimed boundary.[4][6] The
current validator emits the eligible text only after artifact, schema,
configuration, count, vector, manifest, live-corpus, and metadata checks have
passed and the heartbeat SHA alone differs from current `HEAD`.[5] The current
skills instead halt on every non-`OK --` result.[7][8]

The result remains narrow:

- **Known:** the preserved classifier boundary reproduces; the two same-system
  historical events reached literal `OK --`; the watcher runs each minute; and
  the present validator has a distinct final HEAD-lag branch.[2][3][5][9]
- **Inferred:** one skill-level recheck could avoid the same full-stage halt if
  the observed condition recurs and repository state stays fixed.
- **Unknown:** the prospective recovery rate, future watcher duration, and net
  fleet benefit. The 90-second maximum was selected after the two events and is
  not a percentile or guarantee.[2][3]
- **Disconfirmation:** the proposal should be reversed or redesigned if the
  validator text changes, the shell path cannot reject state-change races, a
  prospective exact HEAD-lag event does not recover inside the frozen bound, or
  the maintenance burden exceeds the avoided halts.

AWS describes retries as useful for short transient failures but warns that
retries add load and can repeat side effects. Google Cloud distinguishes
idempotent or conditionally idempotent operations and exposes explicit attempt
and timeout controls.[10][11] Those sources support the shape of one bounded,
read-only attempt. They do not validate this local status, ceiling, or benefit.

### Alternatives

| Alternative | Benefit | Cost and disposition |
|:--|:--|:--|
| Keep immediate HALT | Zero waiting and the simplest fail-closed rule.[7][8] | Would have ended both verified Forge sessions before their later `OK --`; retain as rollback and the default for every noneligible result. |
| Proposed exact-text recheck | Recovers both preserved positive cases while the 22-case control keeps every noneligible initial status immediate.[2][3] | Adds shell logic, exact-text coupling, and at most 90 seconds to one subtype; recommend only with the acceptance gate below. |
| Recheck every `STALE --` | One generic branch would be shorter. | Rejected: current `STALE` also reports missing data, incompatible configuration, shape/count faults, and live-corpus drift; no benefit was demonstrated for those states.[2][5] |
| Structured validator status | Avoids coupling eligibility to human-readable text. | More robust in principle, but requires an unresearched tool interface change and broader tests; defer rather than hiding it inside a skill amendment. |
| Rebuild, invoke the watcher, or poll | May alter or observe more producer states. | Rejected: changes producer behavior, can mask a persistent fault, and exceeds the read-only query boundary.[7][8][9] |

### Response to the ADVANCE evaluation

1. **Exact files and unchanged freshness definition:** the decision names the
   two source skills. Both still require command exit 0 and output beginning
   literal `OK --` before retrieval.[3]
2. **Exact trigger:** eligibility requires initial exit 1 and the complete
   one-line, two-eight-hex-field HEAD-lag text. Every other first result halts
   before a wait or second command.[3][5]
3. **One attempt and state controls:** the specification below defines watcher
   presence, pre-check `HEAD` and worktree snapshots, one computed sleep, a
   90-second elapsed ceiling, comparisons before and after the second command,
   timeout handling, and fault reporting. It never invokes the watcher,
   rebuilds, polls, or changes repository state.
4. **Shell-level tests:** the acceptance matrix covers byte capture, exit and
   whitespace handling, every initial fail-closed class, state changes at each
   boundary, sleep/ceiling failures, second-result failures, and command counts.
   The 22-case classifier is retained only as a control; it is not treated as
   proof of shell wiring.[3]
5. **Evidence limits:** the ceiling remains a post-event design assumption, the
   two positives remain observations from one host/repository/watcher period,
   and implementation benefit remains unestimated.[2][3]
6. **Alternatives and rollback:** immediate HALT, generic retry, structured
   status, and producer-side action are compared above; rollback is the deletion
   of the amendment from the two skills.

No unresolved decision-critical evidence gap prevents specifying the bounded
change. Shell integration and a prospective event remain acceptance and
post-implementation evidence obligations, not completed research.

## Change Specification and Implementation

### Affected interfaces

The only proposed production-source edits are the freshness sections, failure
handling, and hard-gate checklists in:

1. `agentic-brain:governance/skills/query-brain-vps.md`;
2. `agentic-brain:governance/skills/query-forge-vps.md`.

Their repository paths, watcher lines, Python commands, logs, and scope stay
repository-specific. The new decision sequence must otherwise be identical.
Installed copies, profile skills, the three index packages, `/opt/repo-tools`,
cron, services, and runtime configuration are not changed by this proposal.
Any later propagation or deployment requires separate authorization.

### Normative decision sequence

The implementation must express one auditable Bash sequence in each skill:

1. Verify the existing exact watcher line. A missing or unreadable crontab
   immediately halts exactly as it does now.
2. Create a task-owned scratch directory outside the repository. Before the
   first freshness command, capture `git rev-parse HEAD` and the bytes from
   `git status --porcelain=v1 -z --untracked-files=all` into separate files.
   Capture failures halt; do not replace a failed snapshot with an empty value.
3. Execute the existing freshness command once with stdout and stderr captured
   separately and preserve its exit code. Exit 0 plus stdout beginning literal
   `OK --` follows the unchanged immediate-query path. No retry rule broadens
   that success definition.
4. A failed first command is retry-eligible only when all of these are true:
   the exit code is exactly 1; stderr is empty; stdout is exactly one newline-
   terminated line matching
   `STALE -- index at [0-9A-Fa-f]{8}, HEAD at [0-9A-Fa-f]{8}`; and fresh
   `HEAD` and NUL-delimited status captures byte-compare equal to the pre-check
   files. Any leading/trailing space, missing final newline, extra blank or text
   line, wrong-width/nonhex field, different exit code, or state change halts
   immediately and reports the original result.
5. Record the UTC epoch after the eligible first result. Calculate one sleep
   ending 30 seconds after the next minute boundary:
   `target=((epoch/60+1)*60)+30`; `delay=target-epoch`. Require
   `1 <= delay <= 90`. Execute `sleep` exactly once, use a monotonic elapsed
   counter for the 90-second ceiling, and halt on interruption, nonzero sleep,
   backward/invalid timing, or elapsed time above 90 seconds. Do not inspect a
   watcher log or run any command repeatedly while waiting.
6. After the wait, recapture `HEAD` and NUL-delimited worktree status. If either
   differs byte-for-byte from the original snapshot, halt with the initial
   fault and a state-change reason. Do not execute the second freshness command.
7. If state is unchanged, execute the same freshness command exactly once more,
   again preserving stdout, stderr, and exit code. Immediately recapture and
   compare `HEAD` and worktree status after that command. A change during the
   command halts even if its captured output says `OK --`.
8. Permit the existing query command only when both post-wait comparisons match
   the original snapshots and the second freshness command exits 0 with stdout
   beginning literal `OK --`. Every other second result halts and reports the
   original HEAD-lag line, elapsed time, second exit code, and captured second
   output. Do not infer success from elapsed time or a watcher event.
9. Remove only the task-owned scratch directory on every handled exit. A cleanup
   failure is reported but never converted into query permission.

The two state comparisons around the second command narrow the new race window;
they do not claim atomicity between the final comparison and query execution.
That residual check-to-use interval already exists on the immediate path. If
review requires atomic exclusion, this skill-only design is invalid and the
structured/helper alternative needs new research rather than an implied lock.

### Dependencies and ordered implementation

The amendment depends only on the existing Bash/GNU userland, Git, exact cron
ownership, and the existing repository-specific freshness/query commands. It
adds no service or package.

A separately authorized implementer should:

1. Freeze the two current skill files and current HEAD-lag producer text.
2. Build a scratch-only shell harness from the normative sequence, with the
   watcher, Git snapshots, clock/sleep, freshness command, and query command
   supplied by executable stubs that append to an invocation trace.
3. Run the acceptance matrix below against both repository substitutions. Keep
   fixtures, the exact tested shell bytes, raw traces, and results together.
4. Insert the tested sequence into both skills, update their failure handling
   and hard gates, and rerun the same harness against the exact inserted bytes.
5. Run the repository's applicable format, ASCII, link, and diff checks. Review
   that only the two authorized skill files changed.
6. Stop for separate approval, propagation, and deployment. Do not manufacture
   a live `STALE` state, invoke a watcher, or rebuild an index to demonstrate the
   proposal.

## Acceptance, Risks, and Reversal

### Shell-level acceptance matrix

Each fixture must assert the final decision and exact invocation counts for
watcher check, snapshot, freshness, wait, second freshness, and query. A
category containing several current messages runs one fixture per message, not
one representative. PASS requires the following traces from the exact proposed
shell bytes in both skill variants:

| Fixture | Required trace and result |
|:--|:--|
| Initial exit 0, stdout begins `OK --` | No wait; one freshness call; query once. |
| Exact lower-case HEAD lag, unchanged state, second exit 0 `OK --` | One wait; two freshness calls; query once. |
| Exact upper-case hexadecimal HEAD lag, unchanged state, second `OK --` | Same successful delayed trace; verifies the declared `[A-Fa-f]` contract. |
| Every current non-HEAD-lag `STALE --` string from `validate_index_state` | Immediate HALT; no wait, second call, or query; original fault preserved. |
| `NO INDEX`, each `UNVERIFIED` class, missing watcher, unreadable crontab | Immediate HALT; no wait, second call, or query. Missing watcher fails before freshness. |
| Nonhex, short field, missing comma, trailing text, leading/trailing space, missing final newline, extra blank line, extra text line | Immediate HALT; no wait, second call, or query. |
| Initial `OK --` with nonzero exit, exact HEAD lag with exit other than 1, or error text on stderr | Immediate HALT; no wait, second call, or query. |
| State changes between pre-check and post-first capture | Immediate HALT; no wait, second call, or query. |
| State changes during the one sleep | One wait; one freshness call; no second call or query. |
| State changes during the second freshness command | One wait; two freshness calls; no query even if the second stub emits `OK --`. |
| Delay outside 1-90, interrupted/nonzero sleep, or monotonic elapsed time above 90 | HALT; at most one wait; one freshness call; no second call or query. |
| Persistent exact HEAD lag; second `NO INDEX`, `UNVERIFIED`, malformed text, or `OK --` with nonzero exit | One wait; two freshness calls; no query; both results reported. |
| Scratch creation, snapshot, comparison, or cleanup failure | HALT and report the failing operation; never query because cleanup or instrumentation failed. |

Additional regression checks are mandatory:

- extract and rerun the research artifact's 22-case classifier and require
  22/22 as a boundary control, while labeling it non-shell evidence;[2][3]
- assert no fixture invokes an indexer, watcher, rebuild, fallback repository,
  or polling loop;
- run `bash -n` on the exact shell block and verify all written source bytes are
  ASCII;
- compare the two inserted decision blocks after replacing only repository-
  specific constants; semantic drift is a failure;
- preserve the existing immediate-HALT messages for all noneligible first
  results and the existing exit-0/literal-`OK --` retrieval gate.

These are future implementation checks. No modified skill or shell integration
was executed in this proposal stage.

### Worst failure and prevention

The worst plausible failure is stale or mismatched retrieval being permitted
because a broad text match, lost exit code, reused output, or state-change race
is mistaken for fresh evidence. Prevention is defense in depth: exact initial
bytes and exit 1, no retry for other statuses, byte-preserved command output,
pre/post `HEAD` and worktree comparisons, one live second command, final exit 0
plus literal `OK --`, invocation-count tests, and immediate rollback on any
contract drift. This retains consistency as the gate rather than substituting
liveness.[5][9]

Costs are up to 90 seconds of delay on an eligible failure, duplicated skill
text that can drift, exact coupling to the current human-readable validator
message, scratch cleanup, and more complex diagnosis than immediate HALT. The
proposal does not estimate how often those costs or benefits occur.

Rollback is reversible and has no data migration: remove the bounded-recheck
blocks from the two skills and restore unconditional immediate HALT on every
failed first freshness command. No index, watcher, cron, repository data, or
runtime state needs restoration. A validator-message change triggers this
rollback until the eligibility contract is reviewed.

Confidence is medium. The exact trigger and fail-closed classifier boundary are
high-confidence because preserved bytes, current source, and independent 22/22
runs agree.[2][3][5] Overall confidence remains medium because the positives are
two same-system observations, the 90-second ceiling is post-event, and the shell
path is specified but untested. Confidence would rise after the exact shell
bytes pass the full matrix in both skill variants and a prospective natural
HEAD-lag event is preserved under the frozen bound. It would fall on any output-
contract change, unhandled state race, persistent lag beyond the bound, or
maintenance cost disproportionate to observed avoided halts.

## Sources

1. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- root question,
   fail-closed boundary, support thresholds, exclusions, and immediate-HALT
   alternative. [high]
2. `forge/research/bounded-index-freshness-recheck-r02.md` -- corrected embedded
   22-case package, exact trigger, two event values, alternatives, and stated
   evidence limits. [high]
3. `forge/evaluations/bounded-index-freshness-recheck-evaluation-r02.md` --
   independent extraction and two 22/22 reruns, ADVANCE verdict, six proposal
   obligations, correction count, and confidence limit. [high]
4. `forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md` -- prior
   REVISE verdict, broad-trigger and preservation blockers, and the bounded
   correction request that the current research closed. [high]
5. `forge-index/query.py` -- current validator order, status taxonomy, exact
   HEAD-lag producer text, and exit-0 `OK --` contract. [high]
6. `LEARNINGS.md` -- durable-test-evidence requirement and the method rule to
   map every claimed result boundary to an observable control. [high]
7. `agentic-brain:governance/skills/query-brain-vps.md` -- current Brain watcher,
   freshness, immediate-HALT, no-rebuild, and literal-`OK --` procedure. [high]
8. `agentic-brain:governance/skills/query-forge-vps.md` -- matching current Forge
   query procedure and repository-specific interface. [high]
9. `agentic-brain:research/insights/vps-brainclone-plus-index.md` -- one-minute
   watcher cadence, ownership, three-repository architecture, natural-transition
   evidence, and fail-closed validator design. [medium]
   - `agentic-brain:research/insights/stale-index-problem.md` -- consistency over
     liveness and current artifact, schema, manifest, corpus, and HEAD checks.
     [medium]
10. Amazon Web Services. "Timeouts, retries, and backoff with jitter," Marc
    Brooker, undated; accessed 2026-09-30, Failures Happen and Retries and
    backoff sections. Transient-failure recovery, retry load, waiting, and
    idempotency were checked.
    https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
    [medium]
11. Google Cloud. "Retry strategy," undated; accessed 2026-09-30, idempotency,
    customization, and retry-setting sections. Conditional retries, attempt
    bounds, and timeout controls were checked.
    https://docs.cloud.google.com/storage/docs/retry-strategy [high]
12. `forge/protocol.md` -- stage permissions, evidence-gap routing, proposal
    contract, human-review boundary, transaction, and no-implementation scope.
    [high]
