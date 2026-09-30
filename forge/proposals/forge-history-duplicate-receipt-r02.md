---
name: forge-history-duplicate-receipt
id: 20260930T160909Z
tier: proposal
pipeline: 20260930T124036Z
author: Researcher
tags: [agent-systems, forge, retrieval, provenance]
links:
  - forge/ideas/forge-history-duplicate-receipt-r01.md
  - forge/research/forge-history-duplicate-receipt-r01.md
  - forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md
  - forge/proposals/forge-history-duplicate-receipt-r01.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r01.md
  - governance/skills/forge-ideate/SKILL.md
  - forge/protocol.md
  - LEARNINGS.md
  - forge-index/README.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md
  - agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md
  - https://git-scm.com/docs/git-log
  - https://git-scm.com/docs/git-rev-list
  - https://git-scm.com/docs/git-cat-file.html
  - https://git-scm.com/docs/git-ls-tree
  - https://docs.python.org/3.14/library/time.html
  - https://docs.python.org/3.14/library/subprocess.html
confidence: medium
---
# Proposal: Bounded Reachable-History Receipt for Forge Ideation

## Proposed Decision

Approve, for separately authorized implementation and review, one bounded
amendment to the prior-work procedure in
`governance/skills/forge-ideate/SKILL.md`. The amendment adds a read-only,
scratch-only reachable-history receipt after current-tree enumeration and
current Forge hybrid search, but before a new-idea novelty judgment. It prevents
a deleted but reachable Forge pipeline from being mistaken for new work without
creating a second board, archive, index, manifest, repository helper, or restored
artifact.[1][3]

This r02 proposal replaces only the defective operation order and elapsed-time
contract in r01. Every other scope, provenance, full-body decision, unknown-state,
acceptance, rollback, and no-implementation boundary remains in force. The
revision requires object identity, type, and size to be established without body
output before any byte reservation or body call. It also gives every potentially
blocking receipt command the remaining portion of one monotonic 60-second
judgment deadline.[2]

The output type is a skill/rule amendment. The requested decision is to approve
this corrected design for later implementation, executable fixture testing,
independent review, propagation, and deployment. This proposal changes no skill,
installs no helper, and grants no implementation authority.[4]

The beneficiaries are Forge agents and Suggi. A novelty or reopening judgment
should use exact prior state when that state remains reachable in Git, but the
retrieval cost must be bounded before object bodies or blocking commands can
consume the resource the bound claims to protect.[1][5][8]

Non-goals are:

- archival completeness or recovery of unreachable, pruned, unfetched,
  rewritten, or never-committed work;
- a history-aware semantic index or any change to index scope, freshness,
  watcher, cron, model, runtime, or query ranking;
- a durable tombstone, receipt, cache, status file, tag, branch, or competing
  decision record;
- automatic duplicate classification, reopening, closure, or an inference that
  READY means approved;
- edits to `forge/protocol.md`, `STATUS.md`, logs, templates, other skills, or
  any external repository during implementation of this amendment; and
- a claim that the 8 MiB or 60-second ceilings are measured optima, service
  levels, or strict process-creation bounds.

## Evidence, Alternatives, and Evaluation Response

### Provisional explanation and checked correction

Before the additional Brain and primary-source checks, the provisional
explanation was that both r01 blockers were ordering defects, not evidence gaps.
A size ceiling is ineffective if an existence probe already emits the body, and
an elapsed ceiling is ineffective if it is inspected only after an unbounded
command returns. The smallest correction was therefore one gatekeeper that
first obtains metadata only, reserves bytes before a content call, and passes
one decreasing deadline into every receipt command. The correction would fail
if the metadata path emitted body bytes, aliases or repeated reads escaped the
counter, a timed-out command allowed later classification, or enforcing the
boundary required durable machinery.

The checked sources support that narrower design:

- Git `cat-file --batch-check` returns object information, whose default fields
  are object name, type, and size; body contents are produced by `--batch` or a
  `contents` command instead. Git also documents `-t`, `-s`, and `-e` as type,
  size, and existence operations rather than body output.[11]
- Python 3.14 documents `time.monotonic_ns()` as a nanosecond clock that cannot
  go backward and is unaffected by system clock updates.[13]
- Python 3.14 documents that `subprocess.run(..., timeout=...)` kills and waits
  for a child when the timeout expires, then raises `TimeoutExpired`. It also
  states that process creation itself may not be interruptible on some platform
  APIs; the corrected contract therefore adds a post-return monotonic gate and
  does not claim an exact process-lifetime service bound.[14]
- Brain prior work independently says that deadlines should flow down to child
  calls, budgets must be enforced at resource-consuming boundaries, and a
  terminal label is insufficient without the exact action receipt.[6][7][8]

One read-only proposal-stage compatibility probe against this clone executed:

```text
printf '%s\0' 'HEAD:STATUS.md' |
  git cat-file -Z --batch-check='%(objectname) %(objecttype) %(objectsize)'
```

It returned one NUL-terminated information record ending `blob 868` and no
`STATUS.md` body. This is a compatibility check for the local Git interface, not
the future acceptance package or proof that the complete receipt is correct.[11]

The rebuilt explanation is:

- **Known:** the frozen research and independent evaluation agree on 8 current
  paths, 39 reachable paths, 34 logical IDs, 5 roots, 5 alias groups, zero
  cross-pipeline ID conflicts, and two bounded decision changes. R01's final
  review independently reproduced those results and found two proposal-only
  blockers.[1][2]
- **Known:** information-only object queries, a monotonic clock, and per-command
  child timeouts exist in the current documented interfaces.[11][13][14]
- **Inferred:** a single scratch-only driver can compose those interfaces into a
  pre-body byte gate and remaining-deadline gate without a repository helper.
  That composition remains future implementation work.
- **Disputed:** none of the final-review findings is disputed. Both are accepted
  and corrected below.[2]
- **Unknown:** future history size, duplicate frequency, reviewer time, display
  utility, process-creation tail latency, and the economic value of the proposed
  limits remain unmeasured. The sample is still five pipelines in one history.

No new decision-critical research gap blocks a corrected proposal. The evidence
question - whether exact reachable history can change a bounded Forge decision -
was already answered and independently evaluated. The remaining work is to make
the proposed resource controls observable and correctly ordered.[1][2]

### Response to the REVISE review

| Review requirement | R02 response |
|:--|:--|
| Resolve object identity, type, and size without emitting body bytes; gate artifact and log bodies before materialization. | Use one NUL-delimited `git cat-file --batch-check` information call for each candidate `commit:path`; require type `blob`; compare its declared size with the shared remaining byte budget before any body call. Apply the same sequence to artifact and historical-log blobs.[11] |
| Define accounting for aliases, repeated reads, artifact bodies, and historical logs. | Count actual bytes from every body-producing call, including partial failed output. Materialize each unique blob OID at most once; aliases reuse that scratch body and retain provenance. Any accidental repeated body call consumes bytes again. Count every full-body presentation separately, including repeated presentations. Artifact and log bodies share one 8 MiB counter. |
| Enforce one monotonic deadline through remaining-time timeout on every potentially blocking receipt command. | A scratch-only Python driver owns one `deadline_ns`, recomputes positive remaining time before every Git child, passes it to `subprocess.run(timeout=...)`, and rejects returned output if the post-call monotonic check is late. Timeout, late return, or nonpositive remaining time stops all later body, display, and disposition calls.[13][14] |
| Add oversize-first-artifact, oversize-first-log, and blocking-command fixtures with prohibited-invocation assertions. | The acceptance matrix adds all three, plus exact-fit, partial-output timeout, alias-reuse, repeated-call, expired-before-spawn, and post-return-overrun fixtures. Raw traces must show zero prohibited later calls. |
| Map the corrected order and every counter to exact predicates while preserving all other boundaries. | The normative sequence and acceptance oracle below name each counter transition, command class, trace field, stop point, positive control, negative fixture, and regression obligation. All r01 reachability, identity, decision, current-search, rollback, and authority boundaries remain unchanged.[1][2][5] |

The earlier ADVANCE obligations also remain satisfied: the only production target
is the existing ideation skill; reachability is rooted at one exact starting
`HEAD`; the clone must be non-shallow; the view is root-first; logical identity
is `(pipeline, artifact-id)` with complete provenance aliases; exact bodies and
decision events precede disposition; current retrieval remains first; doing
nothing and clue-led history remain live alternatives; and implementation plus
deployment remain separately authorized.[1]

### Alternatives

| Alternative | Evidence-supported benefit | Cost and disposition |
|:--|:--|:--|
| Keep current-tree enumeration and current hybrid search only | Simplest and correct for live files; it recovered the current bounded-freshness control.[1][3] | It exposed only one of five exact roots at the frozen revision, omitted deleted bodies, and supplied no maintenance-capex clue. Retain as the first phase and direct rollback. |
| Use clue-led `git log` and exact-object reads only | Smallest historical method when a current file already names prior work.[1][9] | Three deleted roots had clues, but maintenance capex had none and the SBC clue omitted its verdict. Retain as lower-cost drill-down, not the only discovery route. |
| Keep r01's `git show` existence probe and end-of-command timer | Shorter wording. | Rejected: the probe emits a body before the byte gate, and a blocking command can exceed the elapsed ceiling before it is measured.[2] |
| Use metadata preflight but no per-command remaining timeout | Corrects byte order. | Rejected: it leaves the independent elapsed-time blocker unresolved.[2][8] |
| Add the corrected scratch-only driver | Makes object and command resource gates observable before later judgment, while retaining a complete trace. | Adds Python-standard-library orchestration, counters, fixtures, and failure modes. Recommend only with the complete acceptance package. |
| Add a repository helper, tombstone, archive, or history index | Could make future use shorter or semantic. | Rejected: each creates durable state or a larger retrieval system outside the evaluated one-skill scope. |
| Do nothing | No new procedure or review burden. | Credible if resets remain rare and clues normally suffice, but accepts the demonstrated no-clue and omitted-verdict cases.[1] |

## Change Specification and Implementation

### Affected interface and exact placement

The only proposed production-source edit is one subsection named
`Reachable-history receipt` at the end of Step 2 in
`governance/skills/forge-ideate/SKILL.md`. Current live-file enumeration,
candidate and synonym search, plausible-overlap reads, exact-proposal decision
checks, active and archived log checks, and the fresh `query-forge-vps` hybrid
query remain first. Brain prior-work retrieval remains Step 3.[3]

The subsection instructs an agent to create, inspect, and execute one task-owned
scratch Python driver for the historical receipt. The driver is not added to the
repository or installed. It uses only Python's standard library and read-only
Git commands. Its exact bytes, arguments, stdout, stderr, return states, trace,
and fixture results must be preserved by the separately authorized acceptance
package before the concise procedure is inserted into the skill.[5][6][7]

### Normative procedure

A separately authorized implementer should encode these rules concisely in the
skill and map every rule to the acceptance oracle:

1. **Freeze and label the corpus.** Record full `START_HEAD`, repository root,
   clean transaction state, and literal shallow status. Require literal `false`
   from `git rev-parse --is-shallow-repository`. The revision set is exactly
   `START_HEAD`, not `--all`, changing refs, reflogs, or an inferred remote set.
   Every negative claim states the tested revision, paths, and budgets.[4][9][10]
2. **Complete current retrieval first.** Enumerate live Forge tier files, search
   candidate wording and synonyms, run the fresh hybrid Forge query, inspect the
   board, and inspect active and archived current logs. Record clues and paths.
   An index miss is not historical absence.[3]
3. **Create task-owned scratch only.** Write the inspected driver, command trace,
   metadata records, object bodies, counters, compact display, and errors only
   under configured scratch. Create no Forge file, ref, index, archive, tag,
   branch, worktree, or external state while constructing the receipt.
4. **Start one monotonic judgment deadline.** Immediately before the first
   historical receipt command, set `start_ns = time.monotonic_ns()` and
   `deadline_ns = start_ns + 60_000_000_000`. All receipt Git commands - path and
   commit enumeration, tree comparison, object preflight, body materialization,
   and historical-log traversal - use the one wrapper below. The deadline never
   resets for a new path, candidate, retry, or log.[8][13]
5. **Wrap every receipt command.** Immediately before spawning a child, compute
   `remaining_ns = deadline_ns - time.monotonic_ns()`. If it is nonpositive,
   record `deadline-before-spawn` and spawn nothing. Otherwise call
   `subprocess.run` with an argument vector, `shell=False`, separated stdout and
   stderr, and `timeout=remaining_ns / 1_000_000_000`. A timeout records
   `TimeoutExpired`; no retry is permitted. After every return, read
   `time.monotonic_ns()` again. If it exceeds `deadline_ns`, classify the result
   as `deadline-after-return`, do not use its output, and run no later receipt,
   body, display, or disposition operation. The Python-documented process-
   creation caveat remains a stated limitation, not a reason to accept late
   output.[13][14]
6. **Enumerate paths without bodies.** Under `START_HEAD`, use bounded
   `git log <START_HEAD> --full-history --name-only --format=` over the seven
   Forge artifact directories and compare with bounded `git ls-tree -r
   --name-only <START_HEAD> -- <directories>`. Retain only `.md` paths in scope.
   Enforce the 250-path and 25-root ceilings before body classification.[9][12]
7. **Resolve metadata before body output.** For each path, enumerate candidate
   containing commits newest first. Supply each exact `commit:path` as
   NUL-delimited input to `git cat-file -Z
   --batch-check='%(objectname) %(objecttype) %(objectsize)'` through the deadline
   wrapper. A missing record may advance to the next candidate commit while time
   remains. A resolved record must contain one OID, literal `blob`, and one
   nonnegative decimal size. Malformed, ambiguous, non-blob, or late information
   halts without a body call.[11]
8. **Reserve bytes before each unique body call.** Maintain one
   `body_bytes_emitted` counter with ceiling 8,388,608 bytes across artifact and
   historical-log blobs. If the OID already has a successfully materialized
   scratch body, register the new path/commit as a provenance alias and issue no
   body call. Otherwise require `declared_size <= 8,388,608 -
   body_bytes_emitted` before spawning `git cat-file blob <oid>`. If the test
   fails, record `byte-budget-before-body` and issue zero body calls for that
   object.[2][11]
9. **Account for actual body emission.** Direct each body call's stdout to a new
   exclusive scratch file. After the child is killed, fails, or succeeds, obtain
   the file's actual byte count and add it to `body_bytes_emitted`; partial failed
   output counts. Success additionally requires return code 0, empty stderr,
   actual bytes equal declared size, the post-call deadline gate, and cumulative
   bytes at or below the ceiling. Only then atomically register the scratch body
   under its OID and parse it. Failure removes the partial file during cleanup
   but does not erase its trace or counter; no later classification is allowed.
10. **Define aliases and repeated reads explicitly.** Every OID may have at most
    one successful Git body-materialization call. Path, containing-commit, tier,
    and schema aliases all point to that exact scratch body. An accidental second
    body call for the OID is not deduplicated in accounting: its actual output is
    charged again and the acceptance oracle fails the run. Separately maintain
    `full_body_presentations`; increment it every time complete body bytes are
    presented for semantic disposition, even if the same OID is reread. Stop
    before presentation 21. Alias registration alone increments neither body
    bytes nor full-body presentations.
11. **Apply the same gates to historical logs.** Enumerate reachable versions of
    `logbook/progress.log` and `logbook/archive/progress-*.log` without bodies.
    Resolve each log OID, type, and size through the information-only preflight;
    deduplicate identical OIDs before body materialization; apply the same shared
    byte counter, body trace, and deadline; then deduplicate complete event blocks
    only after their bytes pass. Replacing only `ENT-NNN` for event comparison
    does not merge blocks that differ elsewhere.
12. **Group identities and build a root-first view.** Group artifacts by
    `(pipeline, artifact-id)` while retaining all aliases. Derive roots only from
    exact idea bodies whose `pipeline` equals their root ID. The compact display
    lists pipeline, root ID/path, current or historical presence, candidate
    terminal artifact, candidate event, and ambiguity before descendant detail.
    Literal historical tiers such as `review` remain unchanged.
13. **Read exact evidence before deciding.** Read each plausible candidate root,
    decisive artifact, and claimed human-decision event in full. Increment the
    presentation counter before each complete presentation. READY remains
    nonapproval; no exact human decision remains `unknown`. Historical records
    establish recorded Forge state, not every domain claim's truth.[4][7]
14. **Stop on every unsupported boundary.** Missing objects, malformed metadata,
    cross-pipeline ID collision, unsupported historical-tier mapping, unreadable
    decisive evidence, counter inconsistency, deadline failure, or any ceiling
    breach stops novelty and reopening judgment. Use the protocol checkpoint or
    HALT route; never truncate into a completeness claim.[4][5]
15. **Recheck and clean.** Before any stage write, recheck `HEAD`, board, logs,
    and worktree against the transaction snapshot. Remove only task-owned scratch
    under the existing policy. Cleanup failure is a real error and never converts
    an incomplete receipt into a passed gate.[4][6]

### Counters and trace contract

The scratch driver must emit one ordered machine-readable trace. Each command
record contains sequence, monotonic start and end values, remaining nanoseconds
at admission, command class, argument vector or stable redacted reference,
input kind, output kind (`info`, `body`, or `control`), candidate OID when known,
declared body size, actual body bytes written, return code or typed timeout,
stdout/stderr references, and whether any later operation was permitted.

The acceptance oracle derives, rather than trusts, these counters from the trace:

| Counter | Increment rule | Non-increment rule |
|:--|:--|:--|
| Reachable paths | One per unique in-scope path after complete enumeration. | Duplicate path observations. |
| Root pipelines | One per valid exact root body. | Candidate filenames or snippets. |
| Body bytes emitted | Actual bytes written by every artifact or log body call, including partial failures and accidental repeats. | `--batch-check` info output, path lists, hashes, and alias registration. |
| Unique materialized OIDs | One after the first successful size-matched body call for an OID. | Aliases and failed or partial calls. |
| Full-body presentations | One before every complete body presentation used for disposition, including rereads. | Metadata inspection and alias registration. |
| Deduplicated events | One per complete event block after permitted counter normalization. | Provenance aliases of the same normalized complete block. |
| Elapsed receipt time | `time.monotonic_ns() - start_ns`; one deadline for the whole driver. | No reset or per-path allowance. |
| Context display bytes | Exact bytes of the complete root-first display. | Complete scratch receipt retained outside model context. |

Initial ceilings remain 250 unique paths, 25 roots, 8 MiB of emitted artifact
plus log body bytes, 500 deduplicated events, 20 full-body presentations, 60
monotonic seconds for receipt commands, and 16 KiB for the complete root-first
display. A ceiling is a stop boundary, not permission to return a supported
judgment from a prefix. The frozen positive case remains below each declared
resource bound, but that does not validate future adequacy or economic value.[1]

### Ordered implementation

A separately authorized implementation should:

1. Freeze the current ideation skill, protocol, r02 proposal, Python and Git
   versions, and exact source documentation used by the reference design.
2. Build the scratch-only driver and synthetic fixture builder. Preserve exact
   bytes, hashes, arguments, stdout, stderr, traces, counters, exception states,
   elapsed values, and cleanup results outside the repository.
3. Run the frozen real-history case and every synthetic row below. Do not alter
   the live clone's refs, files, index, watcher, or history.
4. Map every proposed skill sentence to at least one positive, negative, or
   regression predicate. Remove any claim whose boundary is not observable.
5. Insert one concise subsection into `governance/skills/forge-ideate/SKILL.md`
   only after the pre-insertion package passes. Rerun the same package against
   the exact inserted procedure and disposable synthetic repositories.
6. Verify format, links, ASCII, exact diff scope, source cleanup, and that no
   production file except the separately authorized ideation skill changed.
7. Stop for independent review, approval, propagation, and deployment. A passing
   implementation package does not itself authorize any of those actions.[4][5]

## Acceptance, Risks, and Reversal

### Checks already performed and checks still future

Research and independent evaluation already reproduced the frozen corpus,
logical identities, exact decision records, and bounded decision changes.[1]
The r01 final review independently reproduced those facts and identified the
pre-consumption and running-command defects.[2] This proposal stage inspected the
current target skill, current Git/Python interfaces, Brain prior work, and one
information-only local `cat-file` compatibility control.[3][6][7][8][11][13][14]

No scratch receipt driver, root-first display, synthetic fixture package, or
modified skill was implemented or executed in this proposal stage. Every row
below is future acceptance work.

### Frozen real-history control

Against revision `d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06` in a non-shallow
clone, the exact future package must reproduce:

- 8 current artifact paths, 39 reachable artifact paths, 34 logical artifact
  IDs, 5 root pipelines, 5 alias groups, and 0 cross-pipeline ID conflicts;
- 693,114 successful artifact body bytes before any historical-log additions,
  with the complete emitted-byte total derived from body-call traces;
- the maintenance-capex REFRAME and SBC REJECT decision changes;
- the transaction-checker DEFER and exhausted budget without reopening;
- the unattended-command READY review plus exact proposal, with no explicit
  human disposition and therefore `unknown`;
- the bounded-freshness discovery as the current-corpus human-review control;
- one body-materialization call per unique OID despite path aliases; and
- exact agreement among root-first display, complete scratch receipt, counters,
  hashes, decisions, unknown state, and trace order.[1][2]

### Synthetic operation-order and resource matrix

| Fixture | Required trace and result |
|:--|:--|
| First artifact size is one byte above the remaining body budget | Information call returns OID/type/size; zero body calls; `byte-budget-before-body`; no parse, display, or disposition. |
| First historical-log size is one byte above the remaining body budget | Same pre-body stop; zero log body calls and zero event classification calls. |
| Object size exactly equals the remaining body budget | One permitted body call; success only if actual bytes exactly match; the next positive-size object is rejected before body. |
| Body output exceeds or differs from declared size | Actual bytes are charged; HALT; no parse or later call. |
| Body command times out after partial output | Partial file bytes are charged and traced; child termination is recorded; no registration, retry, parse, display, or disposition. |
| One blob appears under several paths or commits | One successful body call and one byte charge; every provenance alias retained. |
| Driver attempts a second body call for a materialized OID | Second output is charged; oracle fails repeated-body invariant; no judgment. |
| Same full body is presented twice | Presentation counter increments twice; byte counter does not change without a body call. |
| Deadline is exhausted before command admission | `deadline-before-spawn`; zero new child calls and zero later operations. |
| A receipt command blocks beyond its remaining interval | `TimeoutExpired`; child killed and waited; no later body, display, or disposition call. |
| Command returns after the absolute deadline, including simulated process-creation overrun | `deadline-after-return`; returned output is not classified; no later call. |
| Earlier commands consume most of the deadline | Every later trace shows a smaller remaining interval; no command receives a fresh 60 seconds. |
| Timeout or late return occurs on an information call | Zero body calls for that candidate and no absence claim. |
| Timeout or late return occurs on a body call | Actual partial bytes counted; no parsed body or judgment. |
| Timeout or late return occurs during log traversal | No event or human-disposition inference from the retained prefix. |
| Information record is missing, malformed, non-blob, negative, overflowed, or has extra fields | HALT before body output. |
| Same artifact ID appears under two pipelines | HALT; no merge or canonical path. |
| Historical `tier: review` body | Literal value retained; role mapping only after exact body and link evidence. |
| Malformed, missing, duplicated, or conflicting required frontmatter | HALT before root or disposition classification. |
| Active and archived event copies differ only in ENT counter | One normalized event, with every provenance alias retained. |
| Event blocks share pipeline and stage but differ elsewhere | Keep both; do not over-deduplicate. |
| READY review has no exact human decision | Disposition remains `unknown`. |
| Human decision names another discovery ID or path | Do not apply it; HALT unresolved ambiguity. |
| Root-first display would exceed 16 KiB or omit a root | Stop without a novelty judgment; no silent truncation. |
| Full-body presentation 21 would begin | Stop before presentation and name the unresolved candidate. |
| Any indexer, watcher, ref, worktree, archive, board, repository write, or shell execution outside the inspected driver occurs during receipt construction | Test failure. |

All negative rows assert exact prohibited invocation counts, not only a final
HALT label. The blocking-command fixtures use an injected monotonic clock and
controlled child stubs so the package can test expired-before-spawn,
in-command timeout, and post-return overrun separately. Positive controls prove
that valid info, body, alias, event, and decision calls still occur in the
required order.[5][8][13][14]

### Regression gates

The complete r01 matrix remains binding. It includes shallow repository, missing
revision/commit/blob/body, path copy, old tier, reset or renumbered logs, READY
without a decision, different-artifact human decision, every independent ceiling,
current live duplicate, no-current-clue historical root, and out-of-corpus work.
It also requires current-tree, synonym, hybrid-query, board, and current-log
checks before history; full reads before disposition; exact reachability wording;
ASCII; resolving links; task-owned cleanup; and an exact one-file production
diff.[1][2]

PASS additionally requires:

- source inspection or an execution trace proving that every receipt Git command
  uses the central remaining-deadline wrapper;
- an oracle-derived byte total equal to the sum of actual body-call output bytes;
- zero body calls after any failed information or reservation gate;
- zero classification calls after any timeout, late return, counter mismatch,
  body failure, or cleanup failure;
- no counter derived only from the driver's self-reported summary;
- the displayed root count equal to the complete receipt root count; and
- preserved exact driver bytes and raw per-fixture traces for independent review.

### Worst failure, costs, and residual uncertainty

The worst plausible failure is a partial or mis-grouped receipt being presented
as complete, causing a repeated idea to be called novel, closed work to be
reopened, or READY to be treated as approval. A closely related failure is a
resource gate that reports HALT only after it has consumed the body or waited on
the command the gate claimed to prevent. Prevention is operation order plus
observable negative invariants: metadata before body, reservation before body,
one decreasing deadline before every command, actual-output accounting, complete
trace-derived counters, full-body decision evidence, and no later invocation
after a failed gate.[2][5][8]

Costs are one additional fresh query, bounded Git traversal, one scratch Python
driver, metadata and body scratch bytes, historical-schema handling, up to 20
full-body presentations, fixture maintenance, and more failure modes than doing
nothing. Review time remains unmeasured. Python's documented process-creation
caveat means the deadline is a fail-closed judgment boundary with per-command
running timeout and post-return rejection, not a guarantee that an operating-
system process can never exist beyond exactly 60 seconds.[14]

Residual uncertainty remains for merge-heavy histories, object pruning, rewritten
refs, many archive files, unusual path bytes, evolving schemas, process-creation
tails, and future artifact volume. Atomic repository immutability across all
reads is not claimed. The protocol's pre-write state recheck remains mandatory;
a changed HEAD, board, log, or worktree invalidates the receipt rather than
rebasing its conclusion.[4]

### Reversal and confidence

Rollback is direct: remove the inserted reachable-history subsection from
`governance/skills/forge-ideate/SKILL.md` and restore the current live-tree,
current-log, Forge-query, and Brain-query procedure. No receipt, index, archive,
ref, status migration, package, service, or external cleanup must be reversed
because the design creates no durable production state.

Confidence is medium. Confidence is high in the frozen object counts, alias
identity result, and two decision changes because research and independent
checks agree.[1][2] Confidence that the corrected design addresses the two r01
blockers is medium: primary interfaces support information-only object metadata,
monotonic time, and per-command timeouts, and the proposed oracle observes
prohibited calls.[11][13][14] Overall confidence remains medium because the
scratch driver, root-first display, and synthetic matrix are unexecuted; the
sample is one repository history; the exact ceilings are design choices; and
process creation has a documented timeout caveat.

Confidence would rise after exact driver bytes pass every real and synthetic row,
a separate reviewer derives the same counters from raw traces, and a later reset
case changes a novelty decision without a false merge. It would fall if any
body appears before reservation, any command receives a reset deadline, a late
or timed-out result reaches classification, clue-led history produces the same
decisions more cheaply, or ordinary history exceeds the bounds.

## Sources

1. `forge/ideas/forge-history-duplicate-receipt-r01.md` -- root question,
   frozen baseline, thresholds, alternatives, and no-durable-state boundary.
   [high]
   - `forge/research/forge-history-duplicate-receipt-r01.md` -- exact runnable
     receipt, 39-path manifest, identity grouping, decision table, resource
     observations, alternatives, and reachability limits. [high]
   - `forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md` --
     independent reproduction, ADVANCE verdict, contrary evidence, and ten
     proposal obligations. [high]
2. `forge/proposals/forge-history-duplicate-receipt-r01.md` -- previous design,
   normative order, counters, limits, acceptance matrix, and rollback. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r01.md` -- exact
     REVISE verdict, reproduced corpus, pre-body byte blocker, remaining-deadline
     blocker, five correction requirements, and cycle count. [high]
3. `governance/skills/forge-ideate/SKILL.md` -- exact proposed target and current
   live-tree, overlap, log, Brain, full-read, and novelty procedure. [high]
   - `forge-index/README.md` -- live-repository hybrid corpus and query interface.
     [high]
4. `forge/protocol.md` -- correction budget, proposal handoff, exact decisions,
   transaction rechecks, checkpoint route, scope, and no-implementation boundary.
   [high]
   - `STATUS.md` -- selected r01 REVISE handoff and preserved human-review row at
     starting HEAD `1b18da4a71274ac8e4ea00988275fd178eb3c6ed`. [high]
   - `logbook/progress.log` -- selected pipeline handoffs through ENT-013 at the
     same starting HEAD. [high]
   - `logbook/errors.log` -- failure record through ENT-017 at the same starting
     HEAD. [high]
5. `LEARNINGS.md` -- evidence-preservation, claimed-result-contract, operation-
   order, resource-bound, and historical-identity lessons. [high]
6. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- revision-specific provenance, bounded repository search, exact command receipts, current-state rereading, and verified handoff. [medium]
7. `agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md` -- authoritative histories, exact operation receipts, finite deadlines, truthful unknown states, and failure-boundary tests. [medium]
8. `agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md` -- enforceable resource boundaries, downward deadline propagation, trace-derived counters, and prohibited silent truncation. [medium]
9. Git project. "git-log Documentation," undated; accessed 2026-09-30,
   Description and History Simplification sections. Supplied-revision traversal,
   path limiting, and `--full-history` were checked.
   https://git-scm.com/docs/git-log [high]
10. Git project. "git-rev-list Documentation," undated; accessed 2026-09-30,
    Description and commit-set semantics. Supplied-revision reachability and its
    limits were checked.
    https://git-scm.com/docs/git-rev-list [high]
11. Git project. "git-cat-file Documentation," updated 2026-09-28; accessed
    2026-09-30, Options, Output, and Batch Output sections. Information-only
    object name/type/size output, body-producing modes, and missing-object
    behavior were checked.
    https://git-scm.com/docs/git-cat-file.html [high]
12. Git project. "git-ls-tree Documentation," undated; accessed 2026-09-30,
    Description, `-r`, `--name-only`, and tree-ish interface. Exact frozen-tree
    enumeration was checked.
    https://git-scm.com/docs/git-ls-tree [high]
13. Python Software Foundation. "time - Time access and conversions," Python
    3.14.7 documentation; accessed 2026-09-30, `monotonic()` and
    `monotonic_ns()`. Nondecreasing, system-clock-independent elapsed timing was
    checked.
    https://docs.python.org/3.14/library/time.html [high]
14. Python Software Foundation. "subprocess - Subprocess management," Python
    3.14.7 documentation, 2026-09-19; accessed 2026-09-30, `run()`, timeout
    behavior, `TimeoutExpired`, and process-creation caveat. Child timeout,
    termination, waiting, exception, and limit qualifications were checked.
    https://docs.python.org/3.14/library/subprocess.html [high]
