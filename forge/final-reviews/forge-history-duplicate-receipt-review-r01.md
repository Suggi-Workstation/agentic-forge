---
name: forge-history-duplicate-receipt-review
id: 20260930T154349Z
tier: final-review
pipeline: 20260930T124036Z
author: Analyst
tags: [agent-systems, forge, retrieval, final-review]
links:
  - forge/proposals/forge-history-duplicate-receipt-r01.md
  - forge/ideas/forge-history-duplicate-receipt-r01.md
  - forge/research/forge-history-duplicate-receipt-r01.md
  - forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md
  - governance/skills/forge-ideate/SKILL.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - logbook/progress.log
  - logbook/errors.log
  - forge-index/README.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md
  - agentic-brain:library/history/historiography-and-historical-method.md
  - https://git-scm.com/docs/git-log
  - https://git-scm.com/docs/git-rev-list
  - https://git-scm.com/docs/git-show
  - https://git-scm.com/docs/git-ls-tree
confidence: high
---
# Final Review: Bounded Reachable-History Receipt

## Target and Baseline

Target: `forge/proposals/forge-history-duplicate-receipt-r01.md`, ID
`20260930T150618Z`.[1]

The target author is Researcher. This review was performed by Analyst in a
separate scheduled context that did not inherit the proposal drafting session's
private reasoning. The root idea and prior evaluation were authored by Analyst,
but the protocol's independence test applies to the exact target artifact, so
target-author independence passes.[2][4]

At starting HEAD `2edb7f4e4431ebfc6de81538dcba6b71b92074aa`, the worktree was
clean. The board contained one valid unselected human-review row for pipeline
`20260930T083956Z` and one valid selected row for pipeline
`20260930T124036Z`, stage `final-review`, with the exact target above.
`progress.log` ended at ENT-012 and `errors.log` ended at ENT-014. No prior
`REVISE`, `REFRAME`, final review, or human budget extension exists for the
selected pipeline, so 0 of 2 corrective cycles were used.[4]

Before reading the target body, the expected design evidence and failure
conditions were recorded in task-owned evaluator scratch. Expected evidence was:

- one separately authorized amendment to the existing Forge ideation prior-work
  procedure, with no board, archive, index, manifest, restored artifact, ref,
  service, or runtime component;
- one explicit frozen revision boundary, a non-shallow check, current-tree and
  current-index retrieval first, and negative claims limited to the tested
  reachable corpus;
- a scratch-only root-first display, stable grouping by pipeline plus artifact
  ID, retained path/commit/blob provenance, and full reads before disposition;
- truthful `unknown` for missing human decisions and no conversion of READY into
  approval;
- path, root, byte, event, body-read, elapsed-time, and context ceilings that
  reject before unsupported consumption or judgment;
- an executable real-history and synthetic acceptance package covering every
  claimed trigger, action, limit, failure, and rollback behavior; and
- direct one-file rollback with no migration.

Failure conditions included durable competing state, scope drift, unbounded or
silently truncated traversal, alias overcounting, cross-pipeline merging,
inferred approval or closure, a resource gate applied only after the resource
was consumed, an unenforced time ceiling, or an acceptance package that did not
observe the exact command sequence it claimed to validate.[1][2][5]

## Findings

### The scope and most design obligations are satisfied

The proposal names one production target,
`governance/skills/forge-ideate/SKILL.md`, and leaves implementation, review,
propagation, and deployment separately authorized. Its normative procedure
freezes exact `HEAD`, requires a non-shallow clone, preserves current retrieval,
uses task-owned scratch, groups by `(pipeline, artifact-id)`, retains path,
commit, blob, tier, and historical schema values, reads exact bodies before
classification, preserves unknown dispositions, and halts on ambiguity. The
current skill confirms that this is a bounded extension of its existing
live-tree, overlap, log, Brain, full-read, and novelty procedure rather than a
second state board.[1][3]

The proposal responds to all ten ADVANCE obligations. It keeps the full receipt
outside model context, presents roots and candidate terminal evidence first,
defines seven finite ceilings, specifies a real-history and synthetic failure
matrix, compares current-only and clue-led alternatives, names the worst
failure, and provides direct deletion rollback. Brain prior work independently
supports revision-specific provenance, bounded context views, durable evidence,
finite recovery budgets, and truthful unknown states. Those sources support the
design boundaries, not the proposal's exact ceilings.[1][2][6]

The root-first display, synthetic package, and final skill bytes have not been
executed. The proposal states that limitation explicitly. Their absence is not
by itself a final-review blocker because this artifact is a reversible design
for separately authorized implementation, but the design must make the future
acceptance package capable of testing every claimed gate.[1][4][5]

### The bounded corpus and decision evidence independently reproduce

An evaluator-written traversal, independent of the research instrument,
recovered the following from frozen revision
`d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06`:

| Check | Result |
|:--|--:|
| Current artifact paths | 8 |
| Reachable artifact paths | 39 |
| Historical-only paths | 31 |
| Logical artifact IDs | 34 |
| Root ideas | 5 |
| Alias groups | 5 |
| Cross-pipeline ID conflicts | 0 |
| Artifact object bytes | 693,114 |

The clone reported `false` for shallow state. Exact object sizes equaled the
bytes returned by `git show <commit>:<path>` in the checked sample. These results
match the target's positive corpus claims. Git documentation supports the
bounded interpretation: log and revision traversal operate on commits reachable
from supplied revisions, `git show` emits the named blob contents, and
`git ls-tree` enumerates a named tree.[1][2][7][8][9][10]

Independent reads of the exact historical terminal artifacts reproduced
`REFRAME` for maintenance capex, `REJECT` for SBC buybacks, `DEFER` for the
transaction checker, and READY for the unattended-command proposal. A separate
traversal checked 42 versions and 41 unique blobs of historical
`progress.log`, recovered nine deduplicated unattended-command events, and found
no explicit human-decision event. The bounded decision claims therefore remain
supported: exact history changes two prior-work judgments while the unattended
READY state remains `unknown`, not approved.[2][4]

These records establish recorded Forge state, not archival completeness or the
truth of every domain claim in the historical artifacts. The proposal preserves
that distinction.[1][6]

### The byte ceiling is applied after a body-producing operation

This is a blocking design defect. The proposal's normative Step 5 first says to
find the newest containing commit whose
`git show <commit>:<path>` succeeds. Only afterward does it say to obtain the
blob and size and stop if the byte budget would be crossed. Its ceiling table,
however, requires stopping before the next object when cumulative artifact and
historical-log object bytes would exceed 8 MiB.[1]

`git show <commit>:<path>` presents the plain blob contents. In the independent
positive control, the first checked object had a blob size of 7,685 bytes and
the success probe emitted exactly 7,685 bytes. The proposal's own Step 5 text
places that body-producing call before its size gate. An oversized first object
would therefore be materialized before the procedure learned that reading it
was prohibited.[9]

The same ordering is not specified for historical progress-log blobs. The
synthetic matrix says that each ceiling must fail closed, but it does not require
an invocation trace proving that an oversized artifact or log body was never
emitted before the failure. A final result of HALT cannot validate a claimed
pre-consumption gate when the prohibited read already occurred. This repeats the
method failure covered by the claimed-result-contract lesson: the action order,
not only the terminal label, must be observable.[1][5]

This defect matters because the byte ceiling is one of the proposal's controls
against context and resource displacement. It does not invalidate the
historical evidence or require another research cycle. It requires a corrected
proposal sequence that resolves object identity, type, and size without emitting
body bytes, checks the remaining cumulative budget, and only then materializes
the artifact or log body.[1][9]

### The elapsed-time ceiling lacks an enforcement boundary

The proposal also declares a 60-monotonic-second receipt-assembly ceiling, but
its normative procedure does not specify a remaining-deadline timeout for each
Git operation. Measuring elapsed time only between completed commands cannot
stop one traversal or object operation that exceeds the declared ceiling. The
acceptance matrix tests ceiling outcomes generically but names no blocking-command
or timeout fixture and no assertion that later body or decision operations were
not invoked after the deadline.[1][5]

A corrected proposal must make the overall monotonic deadline enforceable at
each potentially blocking receipt command. Timeout, interruption, or an expired
remaining budget must use the checkpoint or HALT route with no novelty,
reopening, closure, or approval judgment. This is a design-only correction; it
does not require a measured service guarantee or a new runtime component.

## Verdict and Handoff

**Verdict: REVISE. Exact next stage: `propose`. This verdict uses corrective
cycle 1 of 2.**

The evidence supports the one-file, scratch-only receipt design, but the exact
proposal is not READY because two declared resource ceilings are not yet
implemented as pre-consumption gates. The defect is proposal-only; the current
research and ADVANCE evaluation remain the evidence inputs.[1][2][4]

The revised proposal must:

1. Replace every body-producing existence probe with a non-body object
   resolution, type, and size preflight. Check the remaining cumulative byte
   budget before emitting or copying any artifact body. Apply the same ordering
   to historical progress-log blobs.
2. Define byte accounting for aliases, repeated reads, artifact bodies, and
   historical-log bodies so the acceptance oracle can compare the declared
   counter with actual body-materialization calls.
3. Enforce one overall monotonic deadline through a remaining-time timeout on
   each potentially blocking receipt command. An expired deadline or timeout
   must stop the judgment without running later classification calls.
4. Add independent oversize-first-artifact and oversize-first-log fixtures. Their
   raw invocation traces must show zero body-emitting calls for the rejected
   object. Add a blocking-command fixture that exceeds the remaining deadline
   and proves that no later body, display, or disposition action ran.
5. Map the corrected normative order and every resource counter to exact
   positive, negative, and regression predicates. Preserve all other scope,
   provenance, unknown-state, acceptance, rollback, and no-implementation
   boundaries.

Confidence in REVISE is high. The target text, Git's documented blob-output
behavior, and an independent exact-object run agree on the ordering defect. The
timeout gap follows directly from the difference between measuring a completed
command and enforcing a deadline on a running command. Confidence would fall if
a revised normative sequence demonstrated a pre-body size gate and enforceable
remaining deadline without expanding scope; those changes would remove the two
blockers and permit a fresh final review.

## Learning Decision

Strengthen the existing high-confidence lesson, `Derive evaluator and checker
controls from the claimed result contract`, rather than add a new lesson.[5]

- **Selection:** The proposal remained worth pursuing; the defect concerns one
  bounded implementation contract, not the historical question or decision
  value.
- **Evidence and test design:** The proposal included overflow rows but omitted
  the operation-order predicate needed to prove that the object body was not
  consumed before the byte gate. It also named an elapsed ceiling without a
  running-command deadline fixture.
- **Process:** Reading the normative sequence against the acceptance oracle and
  executing one exact `git show` byte-count control exposed the mismatch before
  READY.
- **Repetition:** This independent pipeline repeats an existing class: a correct
  terminal label does not validate an unobserved later action or an incorrectly
  ordered gate. The current lesson should explicitly cover pre-consumption
  resource and deadline order.
- **Coverage:** Updating the existing lesson is non-duplicative and grants no
  governance or implementation authority. Confidence remains high because the
  lesson already rests on multiple independent pipelines and this review adds a
  directly observed ordering case.

## Sources

1. `forge/proposals/forge-history-duplicate-receipt-r01.md` -- exact target,
   proposed scope, normative sequence, resource ceilings, acceptance matrix,
   limitations, rollback, and no-implementation boundary. [high]
2. `forge/ideas/forge-history-duplicate-receipt-r01.md` -- root question,
   thresholds, failure conditions, prior-work comparison, and excluded durable
   state. [high]
   - `forge/research/forge-history-duplicate-receipt-r01.md` -- frozen corpus,
     executable receipt, raw 39-path manifest, decision evidence, costs, and
     reachability limits. [high]
   - `forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md` --
     independent ADVANCE verdict, reproduced counts, contrary evidence, and ten
     proposal obligations. [high]
3. `governance/skills/forge-ideate/SKILL.md` -- exact proposed target and current
   live-tree, overlap, log, Brain, full-read, and novelty procedure. [high]
   - `forge-index/README.md` -- current live-repository hybrid retrieval scope and
     query interface. [high]
4. `forge/protocol.md` -- review independence, correction budget, dispositions,
   board selection, transaction, checkpoint, and no-implementation rules. [high]
   - `STATUS.md` -- selected final-review row and preserved human-review row at
     starting HEAD `2edb7f4e4431ebfc6de81538dcba6b71b92074aa`. [high]
   - `logbook/progress.log` -- selected pipeline handoffs through ENT-012 at the
     same starting HEAD. [high]
   - `logbook/errors.log` -- failure record through ENT-014 at the same starting
     HEAD. [high]
5. `LEARNINGS.md` -- evidence-preservation, claimed-result-contract, and
   historical-identity lessons plus the separate admission gate. [high]
6. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- revision-specific provenance, bounded context, exact evidence packages, and verified handoffs. [medium]
   - `agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md` -- authoritative history, current projections, finite recovery budgets, and truthful unknown states. [medium]
   - `agentic-brain:library/history/historiography-and-historical-method.md` --
     provenance, retrieval boundaries, archive-selection limits, and cautious
     negative evidence. [medium]
7. Git project. "git-log Documentation," undated; accessed 2026-09-30,
   Description and History Simplification sections. Supplied-revision reachability,
   path limiting, and `--full-history` were checked.
   https://git-scm.com/docs/git-log [high]
8. Git project. "git-rev-list Documentation," undated; accessed 2026-09-30,
   Description and examples. Reachable commit-set and object traversal semantics
   were checked.
   https://git-scm.com/docs/git-rev-list [high]
9. Git project. "git-show Documentation," undated; accessed 2026-09-30,
   Description and examples. Plain-blob output and `<commit>:<path>` historical
   content retrieval were checked.
   https://git-scm.com/docs/git-show [high]
10. Git project. "git-ls-tree Documentation," undated; accessed 2026-09-30,
    Description, `-r`, `--name-only`, and tree-ish interface. Frozen-tree
    enumeration was checked.
    https://git-scm.com/docs/git-ls-tree [high]
