---
name: forge-history-duplicate-receipt-review
id: 20260930T165635Z
tier: final-review
pipeline: 20260930T124036Z
author: Analyst
tags: [agent-systems, forge, retrieval, final-review]
links:
  - forge/proposals/forge-history-duplicate-receipt-r02.md
  - forge/ideas/forge-history-duplicate-receipt-r01.md
  - forge/research/forge-history-duplicate-receipt-r01.md
  - forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md
  - forge/proposals/forge-history-duplicate-receipt-r01.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r01.md
  - governance/skills/forge-ideate/SKILL.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - logbook/progress.log
  - logbook/errors.log
  - agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md
  - agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md
  - https://git-scm.com/docs/git-cat-file.html
  - https://git-scm.com/docs/partial-clone.html
  - https://docs.python.org/3.14/library/time.html
  - https://docs.python.org/3.14/library/subprocess.html
confidence: high
---
# Final Review: Bounded Reachable-History Receipt R02

## Target and Baseline

Target: `forge/proposals/forge-history-duplicate-receipt-r02.md`, ID
`20260930T160909Z`.[1]

The target author is Researcher. This review was performed by Analyst in a
separate scheduled context that did not inherit the proposal drafting session's
private reasoning. Target-author independence therefore passes.[1][5]

At starting HEAD `0baaeb3c0ad05738dade2c09361d5c67c594c9b2`, the worktree was
clean. The board contained one valid unselected human-review row for pipeline
`20260930T083956Z` and one valid selected row for pipeline
`20260930T124036Z`, stage `final-review`, with the exact target above.
`progress.log` ended at ENT-014 and `errors.log` ended at ENT-019. One prior
final-review REVISE used corrective cycle 1 of 2; no REFRAME or human budget
extension exists for this pipeline.[3][5]

Before reading the target body, the expected design evidence and failure
conditions were recorded in task-owned evaluator scratch. Expected evidence
was:

- the same one-skill, scratch-only, separately authorized scope;
- information-only object identity, type, and size resolution before every
  artifact or historical-log body call;
- a shared actual-output byte counter whose limit is enforced before body
  consumption, including aliases, repeated calls, and partial output;
- one monotonic deadline propagated as the remaining timeout to every
  potentially blocking receipt command, with no later classification or
  disposition after expiry or timeout;
- oversize-first-artifact, oversize-first-log, blocking-command, positive,
  negative, and regression fixtures with trace-derived prohibited-call
  assertions; and
- preservation of exact provenance, truthful unknown states, current retrieval,
  finite fail-closed limits, direct rollback, and no implementation authority.

Failure conditions included any body emission before the applicable metadata
and remaining-byte gates, actual output that can exceed a claimed hard byte
ceiling before detection, work or judgment after the absolute deadline, a
self-reported trace that cannot expose prohibited in-process calls, or a
nominally read-only Git operation that can fetch or write undeclared state.
These criteria follow the prior review, evaluated research, current method
lessons, and the claimed resource contract.[2][3][6][7]

## Findings

### The direct r01 operation-order defects are substantially corrected

R02 replaces the body-producing `git show` existence probe with a NUL-delimited
`git cat-file --batch-check` information call, requires a blob OID and declared
size, reserves remaining bytes before a body call, and applies the same sequence
to artifact and historical-log objects. It groups aliases by OID, charges
accidental repeated body calls again, charges partial failed output, and keeps
artifact and log bodies under one counter.[1]

The corrected command wrapper also establishes one `deadline_ns`, computes the
remaining interval before each receipt Git child, supplies that interval to
`subprocess.run(timeout=...)`, and rejects late output. Python documents that
`monotonic()` cannot go backward or follow system-clock updates and that a
`run()` timeout kills and waits for the child before raising `TimeoutExpired`.
R02 correctly retains Python's process-creation caveat and adds a post-return
clock gate rather than claiming an exact operating-system process-lifetime
bound.[1][10][11]

A read-only compatibility check against the proposal's starting commit
`1b18da4a71274ac8e4ea00988275fd178eb3c6ed` reproduced its 868-byte
`STATUS.md` object: metadata preflight reported a blob of size 868 and the
separate body call emitted 868 bytes. Git's documented interface distinguishes
`--batch-check` information from raw object contents and defines object size in
bytes.[8] This supports the chosen primitive, not the complete future driver or
acceptance package.

The proposal also preserves the evaluated scope. The only production target is
`governance/skills/forge-ideate/SKILL.md`; current-tree and hybrid search stay
first; full receipt state remains task-owned scratch; exact bodies precede
recorded-state judgments; READY remains nonapproval; and rollback removes one
subsection without a data or index migration.[1][2][4]

### The emitted-byte ceiling can still be exceeded before detection

This is blocking. Step 8 admits a body call when the Git-declared object size
fits the remaining budget. Step 9 measures and charges actual file bytes only
after the child succeeds, fails, or is killed. The acceptance matrix expressly
permits actual body output to exceed or differ from the declared size and then
returns HALT after charging those bytes.[1]

Those rules do not enforce the stated 8,388,608-byte ceiling on actual emitted
body bytes. If the declared size exactly equals the remaining allowance and the
body call writes one additional byte, the sink has already crossed the ceiling
before the mismatch is detected. The same failure can occur through partial
output from a faulty body producer. A correct final label and counter do not
restore a hard resource boundary after the resource was consumed. Brain prior
work likewise distinguishes a machine-enforced hard limit from a post hoc
observation and requires budgets at the consuming boundary.[6][7]

The corrected design must bound actual bytes at the output sink or process
boundary, not only reserve the producer's declared size. Its oracle must assert
the maximum bytes physically accepted for exact-fit, mismatch, timeout, and
partial-output fixtures. If the design instead trusts local Git object metadata,
it must narrow the claim and stop calling the 8 MiB value a hard actual-output
ceiling; that weaker contract would require fresh review against the original
resource-displacement goal.

### The whole-driver deadline omits in-process work

This is blocking. The central wrapper checks time before and after receipt Git
children. After a permitted child returns, however, the normative sequence can
count bytes, parse bodies and frontmatter, group identities, deduplicate events,
build the display, present full bodies, classify recorded state, and issue a
novelty or reopening judgment without another required deadline gate.[1]

The proposal nevertheless calls the value one monotonic judgment deadline and
defines elapsed receipt time as `time.monotonic_ns() - start_ns` for the whole
driver. A final child can return just before the absolute deadline, after which
in-process work can cross 60 seconds and still produce a display or judgment.
The current matrix tests admission expiry, child timeout, and late child return,
but not an injected-clock overrun during parsing, grouping, presentation,
display, or disposition.[1]

A deadline that flows to child calls is necessary but not sufficient for the
proposal's broader whole-driver claim.[7][10][11] The next revision must check
the same absolute deadline before and after each decision-relevant in-process
transition and add an in-process-overrun fixture proving that no display,
classification, or disposition follows expiry.

### The trace contract cannot derive all claimed counters or prohibited calls

This is blocking. The trace schema defines command records with child arguments,
input/output kinds, timing, output references, return state, and a field saying
whether later operation was permitted. The counters it claims to derive also
include valid root classification, full-body presentations, event
deduplication, and context-display bytes. Those are in-process operations, but
R02 defines no typed trace records for their invocation, result, or counter
transition.[1]

The same gap affects negative assertions. A child trace can show that no later
Git child ran, but it cannot independently prove that body parsing, event
classification, display generation, or disposition logic did not run. Nor can a
self-reported `later operation permitted` field prove absence of an operation
that the same driver failed to record. The existing method lessons require each
claimed result and prohibited action to have an observable predicate, while
Brain observability work warns that a trace records only what its instrumentation
emits.[6][7]

The next revision must define typed ordered events for every in-process
operation and counter transition used by the oracle, or define an independent
fixture ledger/state-machine observer that can detect omitted calls. The oracle
must derive the presentation, event, root, display, and disposition invariants
from those observations rather than trusting a summary field.

### Shallow-clone rejection does not prevent lazy fetches in partial clones

This is blocking because the proposal promises read-only, scratch-only receipt
construction with no external or repository state change. Step 1 rejects shallow
clones but does not reject partial/promisor clones or disable lazy fetching for
receipt Git children.[1]

Git documents that partial clone is independent of shallow clone, that missing
objects can be demand-fetched from a promisor remote, and that fetching a missing
object invokes a `git fetch` subprocess.[9] Therefore a nominally information-
only or body-read command can contact a remote and write new objects when the
repository is partial, instead of taking the proposal's missing-object HALT
route. The current Forge clone reported `shallow=false` and no configured
`extensions.partialClone` or promisor remote, so this is not evidence of current
repository corruption. It is an unguarded design state that contradicts the
proposed no-network/no-write contract.

The next revision must either reject every partial/promisor configuration before
historical commands or specify a version-verified no-lazy-fetch environment for
every Git child. Add a promisor/missing-object fixture that proves zero network,
fetch-child, and object-database writes before HALT.

## Verdict and Handoff

**Verdict: REVISE. Exact next stage: `propose`. This verdict uses corrective
cycle 2 of 2; the ordinary correction budget is now exhausted.**

R02 correctly replaces the r01 body-producing existence probe and adds a
remaining-time child timeout, but the exact proposal is not READY. Its actual
byte ceiling remains post-consumption under a declared/actual mismatch, its
whole-driver deadline omits in-process transitions, its command-only trace
cannot derive all acceptance counters or prohibited calls, and its shallow-only
clone gate permits partial-clone lazy fetching.[1][3][6][7][9]

The revised proposal must:

1. Enforce the remaining actual-output allowance at the sink or process boundary
   for artifact and historical-log bodies, and prove the maximum accepted bytes
   in exact-fit, mismatch, timeout, and partial-output fixtures.
2. Apply the one absolute monotonic deadline before and after every
   decision-relevant in-process operation as well as every child command. Add an
   injected-clock in-process-overrun fixture with zero later display,
   classification, or disposition calls.
3. Define independently observable trace or fixture events for parsing,
   identity/root classification, presentations, event deduplication, display,
   counter transitions, and disposition. Derive every claimed counter and
   prohibited-call assertion from those events.
4. Reject partial/promisor clones or disable lazy fetching through a
   version-verified fail-closed mechanism for every Git child. Test that a
   missing promised object causes no network, fetch child, or object-database
   write.
5. Preserve all other r02 scope, provenance, current-search, exact-body,
   unknown-state, rollback, acceptance, and no-implementation boundaries.

The next proposal remains eligible for final review because this verdict itself
uses the second permitted correction. A later request for another REVISE or
REFRAME would exceed the ordinary budget and must follow the protocol's DEFER or
explicit human-extension rule.[5]

Confidence in REVISE is high. The first three blockers follow from direct
comparison of R02's normative order, counters, and acceptance matrix; the fourth
follows from Git's documented partial-clone behavior. Confidence would fall if
a revised specification enforced actual sink bytes, gated every in-process
transition, exposed all oracle-relevant calls independently, and prevented lazy
fetch without expanding scope. Those corrections would remove the blockers and
permit a fresh final review.

## Learning Decision

`LEARNINGS.md` remains unchanged.[6]

- **Selection:** The historical-retrieval question remains worthwhile; the
  blockers concern the enforceability of one bounded design, not the evaluated
  decision value.
- **Evidence and test design:** Exact-fit-plus-extra-output, final-child-then-
  in-process-overrun, uninstrumented in-process calls, and partial-clone demand
  fetch are the decisive counterexamples.
- **Process:** Comparing the normative sequence with each claimed hard limit and
  its oracle exposed the gaps. Primary Git and Python documentation separated
  supported interface behavior from proposal inference.
- **Repetition:** The emitted-byte, deadline, and trace gaps repeat the existing
  claimed-result-contract lesson within the same pipeline. This is not another
  independent pipeline and does not justify a confidence change.
- **Coverage:** The existing lesson already requires resource gates before the
  consuming operation and observable prohibited-invocation predicates. The
  partial-clone case is one tool-specific design hazard, not yet a separate
  transferable lesson with independent pipeline evidence. No non-duplicate
  learning edit passes the admission gate.

## Sources

1. `forge/proposals/forge-history-duplicate-receipt-r02.md` -- exact target,
   corrected object and deadline sequence, counters, trace contract, acceptance
   matrix, risks, rollback, and authority boundary. [high]
2. `forge/ideas/forge-history-duplicate-receipt-r01.md` -- root question,
   thresholds, failure conditions, and excluded durable state. [high]
   - `forge/research/forge-history-duplicate-receipt-r01.md` -- frozen corpus,
     executable receipt, identity grouping, decision evidence, costs, and
     reachability limits. [high]
   - `forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md` --
     independent ADVANCE verdict, reproduced evidence, contrary evidence, and
     proposal obligations. [high]
3. `forge/proposals/forge-history-duplicate-receipt-r01.md` -- prior normative
   order, resource ceilings, acceptance matrix, and rollback. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r01.md` -- prior
     REVISE, pre-body and running-command blockers, required corrections, and
     corrective-cycle count. [high]
4. `governance/skills/forge-ideate/SKILL.md` -- exact proposed target and current
   live-tree, overlap, log, Brain, full-read, and novelty procedure. [high]
   - `forge-index/README.md` -- current-corpus hybrid query interface and watcher
     ownership. [high]
5. `forge/protocol.md` -- independence, correction budget, dispositions, board,
   transaction, checkpoint, and no-implementation rules. [high]
   - `STATUS.md` -- selected final-review row and preserved human-review row at
     starting HEAD `0baaeb3c0ad05738dade2c09361d5c67c594c9b2`. [high]
   - `logbook/progress.log` -- selected pipeline handoffs through ENT-014 at the
     same starting HEAD. [high]
   - `logbook/errors.log` -- failure record through ENT-019 at the same starting
     HEAD. [high]
6. `LEARNINGS.md` -- evidence-preservation, claimed-result-contract,
   operation-order, resource-bound, historical-identity, and learning-admission
   rules. [high]
7. `agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md` -- machine-enforced hard limits, consuming-boundary budgets, downward deadline propagation, and trace-level attribution. [medium]
   - `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- bounded repository search, exact receipts, revision evidence, and verification limits. [medium]
   - `agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md` -- exact operation receipts, finite deadlines, truthful unknowns, and failure-boundary tests. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md` -- instrumentation coverage, trace limits, and observable prohibited operations. [medium]
8. Git project. "git-cat-file Documentation," updated 2026-09-28; accessed
   2026-09-30, Options, Output, and Batch Output sections. Information-only
   object name/type/size output and raw body-producing modes were checked.
   https://git-scm.com/docs/git-cat-file.html [high]
9. Git project. "Partial Clone," updated 2026-09-28; accessed 2026-09-30,
   introduction, Non-Goals, Handling Missing Objects, and Fetching Missing
   Objects sections. Independence from shallow clone, promisor configuration,
   demand fetching, and fetch-subprocess behavior were checked.
   https://git-scm.com/docs/partial-clone.html [high]
10. Python Software Foundation. "time - Time access and conversions," Python
    3.14.7 documentation; accessed 2026-09-30, `monotonic()` and
    `monotonic_ns()`. Nondecreasing and system-clock-independent elapsed timing
    were checked.
    https://docs.python.org/3.14/library/time.html [high]
11. Python Software Foundation. "subprocess - Subprocess management," Python
    3.14.7 documentation, 2026-09-19; accessed 2026-09-30, `run()`, timeout
    behavior, `TimeoutExpired`, and process-creation caveat. Child termination,
    waiting, exception, and timing limits were checked.
    https://docs.python.org/3.14/library/subprocess.html [high]
