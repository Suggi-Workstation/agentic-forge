---
name: forge-history-duplicate-receipt
id: 20260930T180714Z
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
  - forge/proposals/forge-history-duplicate-receipt-r02.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r02.md
  - governance/skills/forge-ideate/SKILL.md
  - forge/protocol.md
  - LEARNINGS.md
  - forge-index/README.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md
  - agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md
  - agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md
  - https://git-scm.com/docs/git-cat-file.html
  - https://git-scm.com/docs/partial-clone
  - https://git-scm.com/docs/git-log
  - https://git-scm.com/docs/git-rev-list
  - https://git-scm.com/docs/git-ls-tree
  - https://docs.python.org/3.14/library/resource.html
  - https://docs.python.org/3.14/library/subprocess.html
  - https://docs.python.org/3.14/library/time.html
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
artifact.[1][4]

This r03 proposal preserves the evaluated purpose and replaces four blocked r02
contracts. It enforces actual accepted body bytes at the operating-system file
sink, applies one absolute deadline to child commands and decision-relevant
in-process transitions, gives the acceptance harness an independently owned
operation ledger, and rejects shallow or partial/promisor repositories before
historical object access. Every other reachability, identity, exact-body,
unknown-state, acceptance, rollback, and no-implementation boundary remains in
force.[2][3]

The output type is a skill/rule amendment. The requested decision is to approve
this corrected design for later implementation, executable fixture testing,
independent review, propagation, and deployment. This proposal changes no skill,
installs no helper, creates no durable receipt, and grants no implementation
authority.[5]

The beneficiaries are Forge agents and Suggi. Exact prior state can prevent a
false novelty or reopening judgment, but the retrieval mechanism must not exceed
its own hard resource boundary, continue judgment after its deadline, treat an
uninstrumented call as absent, or lazily fetch and mutate a supposedly read-only
clone.[1][3][6][7]

Non-goals are:

- archival completeness or recovery of unreachable, pruned, unfetched,
  rewritten, or never-committed work;
- a history-aware semantic index or any change to index scope, freshness,
  watcher, cron, model, runtime, or query ranking;
- a durable tombstone, receipt, cache, status file, tag, branch, helper, service,
  or competing decision record;
- automatic duplicate classification, reopening, closure, or an inference that
  READY means approved;
- support for shallow, partial, or promisor repositories in this first design;
- edits to `forge/protocol.md`, `STATUS.md`, logs, templates, other skills, or
  any external repository during implementation of the amendment; and
- a claim that the 8 MiB, 60-second, or other ceilings are measured optima,
  service levels, or exact process-lifetime guarantees.

## Evidence, Alternatives, and Evaluation Response

### Provisional explanation, gaps, and checked result

The selected chain, method memory, current proposal contract, and fresh Forge and
Brain retrieval were read before the provisional explanation. The provisional
explanation was therefore recorded honestly after discovery: r02 measured four
boundaries after a prohibited action could already occur or outside the
instrumented surface. The smallest correction was to move byte enforcement into
the file sink, move every decision-relevant transition behind one deadline-aware
dispatcher, let the fixture harness observe that dispatcher from outside the
driver, and reject partial/promisor state before any object lookup. The design
would be disproved if a sink file could exceed its remaining allowance, an
overrun could still publish a display or disposition, a prohibited in-process
call could bypass the harness ledger, a rejected promisor fixture could contact
a remote or change Git state, or the correction required durable machinery.

The checked evidence supports the narrower design:

- Python documents `RLIMIT_FSIZE` as the maximum size of a file a process may
  create and `setrlimit()` as the soft/hard limit interface. On this Linux host,
  a proposal-stage compatibility probe ran `/usr/bin/printf` with stdout bound
  directly to a new regular file and set the child limit before `exec`: an
  8-byte payload under an 8-byte limit exited 0 with an 8-byte file; a 9-byte
  payload ended by signal with the file still 8 bytes; and a 1-byte payload
  under a zero-byte limit left a zero-byte file. This is interface evidence, not
  the future Git driver or acceptance package.[11]
- Python documents that a POSIX `preexec_fn` runs in the child immediately before
  execution and is unsafe when the application has threads. The proposed driver
  is therefore a standalone, single-threaded POSIX process; any extra live thread
  or unavailable `RLIMIT_FSIZE` halts before a body child is created.[12]
- Git distinguishes information-only `cat-file --batch-check` output from body-
  producing `--batch` or typed-object output. The metadata-first gate from r02
  remains valid and precedes the new sink limit.[8]
- Git documents that partial clone is independent of shallow clone, missing
  objects may be demand-fetched, a fetch subprocess performs that retrieval, and
  promisor state is identified by `extensions.partialClone`,
  `remote.<name>.promisor`, or `remote.<name>.partialCloneFilter`. R03 rejects
  every such local configuration before historical enumeration or object access
  instead of assuming that an interrogation command is write-free.[9]
- Brain prior work independently requires resource limits at the consuming
  boundary, downward deadline propagation, observable application-owned steps,
  revision-specific evidence, and a state machine whose accepted transitions are
  distinct from diagnostic traces.[7]

The current clone compatibility checks reported Git 2.43.0, Python 3.14.7,
Linux, literal `false` shallow state, no `extensions.partialClone`, and no
promisor remote configuration. The local Git rejected the newer global
`--no-lazy-fetch` option, so this design does not rely on that option or on an
environment variable that this installed version may ignore. It uses the
version-independent fail-closed choice: reject partial/promisor state before any
historical object command.

The rebuilt explanation is:

- **Known:** the frozen research and independent evaluation agree on 8 current
  paths, 39 reachable paths, 34 logical IDs, 5 roots, 5 alias groups, zero
  cross-pipeline ID conflicts, and two bounded decision changes.[1]
- **Known:** both prior final reviews reproduced the decision evidence. R01 found
  pre-body and running-command defects; r02 found sink, whole-driver,
  instrumentation, and partial-clone defects.[2][3]
- **Known:** current documented and locally checked interfaces can cap a regular
  output file before excess bytes are accepted, separate object metadata from
  contents, expose partial/promisor configuration, and provide monotonic timing
  plus child timeouts.[8][9][11][12][13]
- **Inferred:** one standalone scratch driver can compose those interfaces into
  the state machine below. That composition remains future implementation work.
- **Disputed:** none of the r02 review findings is disputed. All four are accepted
  and answered below.[3]
- **Unknown:** future history size, duplicate frequency, reviewer time, root-view
  utility, merge-heavy behavior, operating-system portability, and the economic
  value of the chosen limits remain unmeasured. The evidence sample remains five
  pipelines in one repository history.

No new decision-critical research gap blocks a corrected proposal. The research
question - whether exact reachable history can change a bounded Forge decision -
was answered and independently evaluated. The remaining issues are enforceable
implementation contracts whose interfaces and negative cases can be stated and
reviewed.[1][3]

### Response to the r02 REVISE review

| Review requirement | R03 response |
|:--|:--|
| Enforce the remaining actual-output allowance at the sink or process boundary and prove the maximum bytes physically accepted. | Each body child writes directly to a new exclusive regular file, not a pipe or in-memory capture. Immediately before `exec`, the standalone child sets `RLIMIT_FSIZE` to the shared remaining allowance. The parent charges the file's actual `st_size`; the file must never exceed that allowance. Exact-fit, plus-one, declared/actual mismatch, timeout, and partial-output fixtures inspect the sink bytes and child state.[11][12] |
| Apply one deadline before and after every decision-relevant in-process operation as well as every child. | One immutable `deadline_ns` covers clone guards, commands, parsing, counter transitions, identity grouping, event normalization, presentations, display construction, classification, disposition computation, and disposition publication. A central dispatcher checks before and after each operation; a late result is discarded and cannot be committed or published.[7][13] |
| Make all oracle-relevant in-process calls and prohibited later actions independently observable. | Production state changes occur only through typed dispatcher operations. In fixtures, a harness-owned wrapper records callable entry, return, exception, and state transition outside the driver trace. The oracle uses that ledger, child-stub records, and sink files; an AST structural check rejects direct calls to protected operations or direct disposition output outside the dispatcher.[6][7] |
| Reject partial/promisor clones or disable lazy fetching and prove zero network, fetch child, and object-database writes. | Before any historical enumeration or object lookup, reject shallow state and any local `extensions.partialClone`, `remote.*.promisor`, or `remote.*.partialCloneFilter` key. A disposable promisor fixture uses a logging remote helper and before/after Git-state hashes; PASS requires zero helper or fetch invocation and no object, ref, log, `FETCH_HEAD`, config, index, or worktree change.[9] |
| Preserve every other r02 boundary. | Current retrieval remains first; exact `START_HEAD` bounds reachability; complete bodies precede decisions; path/commit/blob provenance and `(pipeline, artifact-id)` identity remain; READY stays nonapproval; unknown stays unknown; all ceilings fail closed; rollback is one subsection deletion; implementation remains separately authorized.[1][2][3] |

The ordinary correction budget is exhausted after the two completed REVISE
reviews. This proposal remains eligible for final review because the r02 verdict
itself authorized this proposal pass. A further REVISE or REFRAME would require
DEFER or an explicit human extension; this proposal does not reset the count.[3]
[5]

### Alternatives

| Alternative | Evidence-supported benefit | Cost and disposition |
|:--|:--|:--|
| Keep current-tree enumeration and current hybrid search only | Simplest and correct for live files; it recovered the current bounded-freshness control.[1][4] | It exposed only one of five exact roots at the frozen revision, omitted deleted bodies, and supplied no maintenance-capex clue. Retain as the first phase and direct rollback. |
| Use clue-led Git history only | Smallest historical method when a current file already names prior work.[1][10] | Three deleted roots had clues, but maintenance capex had none and the SBC clue omitted its terminal verdict. Retain as lower-cost drill-down, not the only discovery route. |
| Trust Git's declared object size and narrow the claim | Avoids a process-level sink cap. | Rejected for this revision: it would abandon the reviewed hard actual-output contract and require fresh comparison with the original resource-displacement purpose.[3] |
| Stream through an in-process pipe and stop after the allowance | Portable and avoids `preexec_fn`. | Rejected: producer bytes can already occupy the kernel pipe, and detecting one extra byte would itself accept a byte beyond an exact remaining allowance. A direct limited regular-file sink has the clearer physical boundary. |
| Use a newer Git no-lazy-fetch switch instead of rejecting partial clones | Could permit read-only work in a partial repository. | Rejected: local Git 2.43.0 does not expose the global option, and version-dependent lazy-fetch suppression needs separate compatibility research. This first design halts earlier. |
| Add the corrected scratch-only state machine | Enforces sink bytes, deadline, operation observability, and no-fetch behavior without durable production state. | Adds POSIX/Linux assumptions, a single-thread restriction, a harness-owned ledger, structural checks, and more fixtures. Recommend only with the complete package below. |
| Add a repository helper, archive, tombstone, or history index | Could make repeated use shorter or semantic. | Rejected: each creates durable state or a larger retrieval system outside the evaluated one-skill scope. |
| Do nothing | No new procedure or review burden. | Credible if resets remain rare and clues normally suffice, but accepts the demonstrated no-clue and omitted-verdict cases.[1] |

## Change Specification and Implementation

### Affected interface and exact placement

The only proposed production-source edit is one subsection named
`Reachable-history receipt` at the end of Step 2 in
`governance/skills/forge-ideate/SKILL.md`. Current live-file enumeration,
candidate and synonym search, plausible-overlap reads, exact-proposal decision
checks, active and archived log checks, and the fresh `query-forge-vps` hybrid
query remain first. Brain prior-work retrieval remains Step 3.[4]

The subsection instructs an agent to create, inspect, and execute one task-owned
standalone scratch Python driver. The driver is not committed, installed, or
retained as runtime state. It uses the Python standard library, read-only Git
commands, POSIX resource limits, and a single thread. Its exact bytes, arguments,
child results, sink files, driver trace, external fixture ledger, counters, and
fixture results must be preserved by the separately authorized acceptance
package before concise skill wording is inserted.[6][7][11][12]

### Normative procedure

A separately authorized implementer should encode these rules concisely in the
skill and map every rule to the acceptance oracle:

1. **Complete current retrieval first.** Enumerate live Forge tier files, search
   candidate wording and synonyms, run the fresh hybrid Forge query, inspect the
   board, and inspect active and archived current logs. Record exact clues and
   paths. An index miss is not historical absence.[1][4]
2. **Freeze the transaction.** Record full `START_HEAD`, repository root, clean
   worktree bytes, board bytes, and active log bytes. The revision set is exactly
   `START_HEAD`, not `--all`, changing refs, reflogs, or an inferred remote set.
   Every negative claim states the tested revision, paths, and budgets.[5][10]
3. **Create task-owned scratch only.** Use a mode-0700 directory under the
   configured scratch root. Create no Forge file, ref, index, archive, tag,
   branch, worktree, installed helper, service, or external state while building
   the receipt. Every sink is a new mode-0600 regular file opened with exclusive
   creation and no symlink following.
4. **Start one whole-driver deadline.** Immediately before the first clone guard,
   set `start_ns = time.monotonic_ns()` and
   `deadline_ns = start_ns + 60_000_000_000`. The deadline never resets. It ends
   only after a permitted disposition has passed its final post-operation gate;
   cleanup may run after expiry but no judgment may be produced.[7][13]
5. **Reject unsupported clone state before history.** Through the deadline-aware
   command wrapper, require literal `false` from
   `git rev-parse --is-shallow-repository`. Read only local repository config in
   NUL-delimited form, compare key names case-insensitively, and reject any
   `extensions.partialClone`, `remote.*.promisor`, or
   `remote.*.partialCloneFilter` key, regardless of value. Malformed config,
   ambiguous output, a config-command error other than documented no-match, or
   any unsupported repository layout halts. No `git log`, `rev-list`, `ls-tree`,
   or `cat-file` call may precede this gate.[9]
6. **Require the supported execution boundary.** Before any body child, require
   POSIX `resource.RLIMIT_FSIZE`, successful scratch-file checks, and exactly one
   live Python thread. Read the inherited soft/hard file-size limits and require
   the hard limit to be infinite or at least the admission-time remaining body
   allowance; never raise it. Do not use `shell=True`. Unavailable or insufficient
   limits, an extra thread, inability to lower the child limit, or inability to
   verify the sink descriptor halts before body output.[11][12]
7. **Dispatch every decision-relevant operation.** Represent receipt state as an
   immutable value changed only by `dispatch(operation, inputs, callable)`. The
   protected operation set is: command admission and completion, object-info
   parsing, sink creation and accounting, frontmatter parsing, counter update,
   alias registration, identity/root grouping, event normalization and
   deduplication, candidate classification, full-body presentation, display
   construction, disposition computation, and disposition publication. Direct
   calls or direct state mutation outside the dispatcher are invalid.
8. **Gate before and after each operation.** The dispatcher checks monotonic time
   before entry; on nonpositive remaining time it records
   `deadline-before-operation` and does not call the operation. It then invokes
   the operation through the configured observer, checks time immediately after
   return or exception, and commits a typed state event only when the post-check
   is within the deadline. A late result is discarded, records
   `deadline-after-operation`, and permits only cleanup and failure reporting.
   Loops dispatch per path, object, event, presentation, and counter transition;
   one broad parsing call cannot hide unbounded later work.[7][13]
9. **Wrap every child command.** Immediately before spawn, compute the one
   deadline's positive remaining interval. Use a full argument vector,
   `shell=False`, fixed repository cwd, stdin appropriate to the exact command,
   separated stdout/stderr sinks, and that remaining interval as the child
   timeout. Timeout, spawn failure, signal, nonpermitted exit, or late return
   stops all later receipt and judgment operations. The Python-documented
   process-creation caveat remains a limitation; the post-return gate rejects
   rather than accepts a late result.[12]
10. **Enumerate paths without bodies.** Under `START_HEAD`, use bounded
    `git log <START_HEAD> --full-history --name-only --format=` over the seven
    Forge artifact directories and compare with `git ls-tree -r --name-only
    <START_HEAD> -- <directories>`. Retain only `.md` paths in scope. Enforce 250
    unique paths and 25 roots before a supported classification.[10]
11. **Resolve object metadata before body output.** For each path, enumerate
    candidate containing commits newest first. Send each exact `commit:path` to
    NUL-delimited `git cat-file -Z --batch-check` and require one unambiguous OID,
    literal `blob`, and nonnegative decimal size. A missing record may advance to
    the next candidate while the deadline remains. Malformed, late, ambiguous,
    or non-blob information halts without a body call.[8]
12. **Reserve the shared body allowance.** Maintain
    `accepted_body_bytes` with hard ceiling 8,388,608 across artifact and
    historical-log bodies. An already materialized OID registers only a
    provenance alias. For a new OID require
    `declared_size <= 8,388,608 - accepted_body_bytes`; otherwise record
    `byte-budget-before-body` and issue zero body calls. The reservation is an
    admission check, not the enforcement boundary.[3]
13. **Enforce the allowance at the body sink.** Open a new empty regular-file
    sink and pass its descriptor directly as the body child's stdout. In the
    single-threaded POSIX child immediately before `exec`, call
    `resource.setrlimit(resource.RLIMIT_FSIZE, (remaining, remaining))`, where
    `remaining` is the shared allowance at admission. No stdout pipe or parent
    in-memory capture is permitted. Run `git cat-file blob <oid>` through the
    child deadline wrapper. The operating system, not a post hoc counter, limits
    the maximum file size the child can create.[11][12]
14. **Charge accepted bytes before interpreting the result.** After success,
    failure, signal, or timeout has terminated and reaped the child, obtain the
    exclusive sink's actual `st_size` and add it to `accepted_body_bytes` before
    any parse or classification. Require `st_size <= remaining` as an invariant.
    A file larger than the allowance is an acceptance failure even if later
    deleted. Successful materialization additionally requires exit 0, empty
    stderr, `st_size == declared_size`, an unchanged file identity, and the
    post-child deadline gate. A plus-one producer, partial output, size mismatch,
    timeout, `SIGXFSZ`, or any other failure permits no registration, parse,
    display, or judgment. Cleanup never subtracts consumed bytes.
15. **Apply identical gates to historical logs.** Enumerate reachable versions of
    `logbook/progress.log` and `logbook/archive/progress-*.log` without bodies.
    Resolve each OID and size through the information-only path, deduplicate OIDs,
    and materialize through the same shared limited sink. Normalize a complete
    event only after its accepted bytes and metadata pass. Replacing only the
    header's `ENT-NNN` for comparison does not merge blocks that differ elsewhere.
16. **Group and classify only through typed transitions.** Group artifacts by
    `(pipeline, artifact-id)` while retaining every path, commit, OID, tier, and
    schema alias. Derive roots only from exact idea bodies whose `pipeline`
    equals the root ID. Event normalization, root classification, candidate
    classification, and each counter delta are separate dispatcher operations.
    Literal historical tiers such as `review` remain unchanged.[1][6]
17. **Read exact evidence before deciding.** Present each plausible candidate
    root, decisive artifact, and claimed human-decision event in full through the
    dispatcher. Increment the 20-presentation counter before admission. READY
    remains nonapproval; no exact human decision remains `unknown`. Historical
    records establish recorded Forge state, not every domain claim's truth.[5]
18. **Separate computation from publication.** Build the complete root-first
    display as a typed operation, enforce its 16 KiB ceiling, then compute the
    proposed novelty/reopening disposition as another operation. A final
    `publish-disposition` operation performs a before gate, writes only after the
    computed result is available, and performs a post gate before the result may
    leave scratch or enter an idea. If that post gate is late, the disposition is
    invalid and only the deadline failure is reported.
19. **Stop on every unsupported boundary.** Missing objects, malformed metadata,
    cross-pipeline ID collision, unsupported historical-tier mapping, unreadable
    decisive evidence, counter inconsistency, dispatcher bypass, ledger loss,
    deadline failure, clone-state rejection, or any ceiling breach stops novelty
    and reopening judgment. Use the protocol checkpoint or HALT route; never
    truncate into a completeness claim.[5][6]
20. **Recheck and clean.** Before any stage write, compare HEAD, worktree, board,
    and logs byte-for-byte with the transaction snapshot. Remove only task-owned
    scratch under the existing policy. Cleanup failure is a real error and never
    converts an incomplete receipt into a passed gate.[5]

### Independent operation ledger and counters

The production driver may emit a diagnostic trace, but the acceptance oracle
must not treat that self-report as proof that omitted operations did not occur.
For fixtures, the driver receives a harness-owned dispatcher wrapper and
capability object. The harness records callable entry, return, exception,
operation type, immutable input-state hash, proposed output-state hash,
monotonic values, sink identity, child-stub invocation, and accepted counter
delta before returning control to the driver. The driver cannot write, delete,
or summarize that ledger. Fixture child stubs and sink files are also owned by
the harness.[6][7]

A source-level AST check is part of acceptance. It must show that protected
functions are referenced only through the dispatcher registration table; that
only the reducer commits receipt state; and that display or disposition output
cannot be written directly. Dynamic fixtures then replace each protected
capability with a spy or fault and derive invocation counts from the external
ledger. The static check covers an uninstrumented bypass; the dynamic ledger
covers actual tested execution. Neither is represented as proof about code paths
outside the inspected exact driver bytes.[6]

The oracle derives these counters from child records, sink files, and external
operation events:

| Counter | Increment rule | Non-increment rule |
|:--|:--|:--|
| Reachable paths | One reducer event per unique in-scope path after complete enumeration. | Duplicate path observations. |
| Root pipelines | One reducer event per valid exact root body. | Candidate filenames or snippets. |
| Accepted body bytes | Actual `st_size` of every artifact or log body sink after the child is reaped, including partial failures and accidental repeats. | Information output, path lists, hashes, and alias registration. |
| Unique materialized OIDs | One reducer event after the first exit-0, empty-stderr, size-matched, deadline-valid body for an OID. | Aliases and failed, limited, partial, or late calls. |
| Full-body presentations | One admission event before every complete body presentation used for disposition, including rereads. | Metadata inspection and alias registration. |
| Deduplicated events | One reducer event per complete normalized event block. | Provenance aliases of the same normalized complete block. |
| In-process operations | One harness-owned entry event for every protected callable invocation. | Driver summaries or unregistered helper calls; the latter fail the structural gate. |
| Elapsed receipt time | Current monotonic value minus the one `start_ns`, through disposition publication. | No reset or per-path allowance. |
| Context display bytes | Exact bytes of the complete root-first display after its post-operation gate. | Complete scratch receipt outside model context. |

Initial ceilings remain 250 unique paths, 25 roots, 8 MiB of accepted artifact
plus log body bytes, 500 deduplicated events, 20 full-body presentations, 60
monotonic seconds through final disposition publication, and 16 KiB for the
complete root-first display. A ceiling is a stop boundary, not permission to
return a judgment from a prefix. The frozen positive case remains below each
reported logical bound, but that does not validate future adequacy or economic
value.[1]

### Ordered implementation

A separately authorized implementation should:

1. Freeze the current ideation skill, protocol, r03 proposal, Python and Git
   versions, and exact primary documentation used by the design.
2. Build the standalone scratch driver, immutable reducer, harness-owned
   dispatcher wrapper, AST structural checker, and synthetic fixture builder.
   Preserve exact bytes, hashes, arguments, stdout, stderr, sink files, child
   records, external ledger, driver trace, counters, clock values, exception
   states, and cleanup results outside the repository.
3. Run the frozen real-history case and every synthetic row below. Use only a
   disposable repository for synthetic Git histories and partial/promisor state;
   do not alter the live clone's refs, files, index, watcher, or history.
4. Map every proposed skill sentence and result claim to one positive control,
   one failure-directed negative case where applicable, and its exact observable
   predicate. Remove any claim whose action or absence is not observable.
5. Insert one concise subsection into `governance/skills/forge-ideate/SKILL.md`
   only after the pre-insertion package passes. Rerun the same package against
   the exact inserted procedure and disposable repositories.
6. Verify format, links, ASCII, exact diff scope, task-owned cleanup, and that no
   production file except the separately authorized ideation skill changed.
7. Stop for independent review, approval, propagation, and deployment. A passing
   implementation package does not authorize any of those actions.[5][6]

## Acceptance, Risks, and Reversal

### Checks already performed and checks still future

Research and independent evaluation already reproduced the frozen corpus,
logical identities, exact decision records, and bounded decision changes.[1]
Both prior final reviews reproduced those facts and identified the six proposal
blockers across r01 and r02.[2][3] This proposal stage inspected the current
target skill, current Brain prior work, Git partial-clone and object interfaces,
Python resource/subprocess/time interfaces, the current clone configuration, and
one bounded `RLIMIT_FSIZE` compatibility probe.[4][7][8][9][11][12][13]

No reachable-history driver, root-first display, independent fixture ledger,
promisor fixture, synthetic matrix, or modified skill was implemented or
executed in this proposal stage. Every row below is future acceptance work.

### Frozen real-history control

Against revision `d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06` in a full,
non-shallow, non-partial, non-promisor clone, the exact future package must
reproduce:

- 8 current artifact paths, 39 reachable artifact paths, 34 logical artifact
  IDs, 5 root pipelines, 5 alias groups, and 0 cross-pipeline ID conflicts;
- 693,114 accepted artifact body bytes before historical-log additions, with
  every byte derived from inspected sink files and child records;
- the maintenance-capex REFRAME and SBC REJECT decision changes;
- the transaction-checker DEFER and exhausted budget without reopening;
- the unattended-command READY review plus exact proposal, with no explicit
  human disposition and therefore `unknown`;
- the bounded-freshness discovery as the current-corpus human-review control;
- one successful body materialization per unique OID despite path aliases; and
- exact agreement among root-first display, complete scratch receipt, immutable
  state, external ledger, sink files, decisions, unknown state, and operation
  order.[1][2][3]

### Sink, deadline, ledger, and clone-state matrix

| Fixture | Required observable result |
|:--|:--|
| Declared body size is one byte above remaining allowance | Information call only; zero sink/body child; `byte-budget-before-body`; no parse, display, or disposition. |
| Body emits exactly the remaining allowance | Sink size equals allowance; success only when return code, stderr, declared size, and deadline also pass; next positive-size body is rejected before spawn. |
| Body attempts one byte beyond remaining allowance | Sink size never exceeds allowance; child fails or is signaled; accepted counter equals sink size; no registration, parse, or later judgment. |
| Declared size is smaller than actual output but both fit remaining allowance | Actual sink size is charged; size mismatch HALTs; no parse or later call. |
| Declared size is larger than actual output | Actual sink size is charged; size mismatch HALTs; no registration or judgment. |
| Body command times out after partial output | Child is terminated and reaped; partial sink size is charged and stays within allowance; no registration, retry, parse, display, or disposition. |
| Zero-byte blob with zero remaining allowance | One limited body child may exit 0 with a zero-byte sink and exact size match; no positive byte is accepted. |
| `RLIMIT_FSIZE` is unavailable or the inherited hard limit is below the remaining allowance | HALT before any body child; the driver does not raise the inherited hard limit or narrow the claimed allowance silently. |
| `setrlimit`, exclusive open, descriptor check, or post-child `stat` fails | HALT before interpretation; no judgment; partial sink retained only until verified cleanup. |
| A second Python thread exists | HALT before any body child; the unsafe `preexec_fn` path is not entered. |
| Body OID appears under several paths or commits | One successful limited body child and one charge; every provenance alias retained. |
| Driver attempts a second body child for a materialized OID | Second sink bytes are charged; oracle fails the one-materialization invariant; no judgment. |
| Deadline expires before a child or in-process operation | External ledger records no protected call entry and child ledger records no spawn; only failure/cleanup follows. |
| Child times out or returns after the absolute deadline | Returned bytes are charged when applicable but never parsed; no later protected operation entry. |
| Clock crosses the deadline during frontmatter parsing | Harness entry and return appear; output-state hash is not committed; zero later grouping, display, classification, or disposition calls. |
| Clock crosses during grouping, event normalization, presentation, display, classification, or disposition computation | The late operation's result is discarded; the external ledger proves zero later protected calls and zero disposition publication. |
| Clock crosses during disposition publication | No disposition is accepted into a root idea; only a typed deadline failure leaves scratch. |
| Protected helper is called directly outside the dispatcher | AST structural gate fails before fixtures or skill insertion. |
| Driver omits, rewrites, or deletes a harness ledger event | Harness-owned sequence/hash check fails; driver summary is ignored. |
| Driver summary disagrees with sink, child, or external-ledger evidence | Oracle fails the run and uses the independent evidence values. |
| Shallow repository | HALT at clone guard; no history or object command. |
| `extensions.partialClone` exists | HALT before history; no object access, remote helper, fetch child, or Git-state write. |
| Any `remote.*.promisor` key exists | Same immediate fail-closed result, including a key set false. |
| Any `remote.*.partialCloneFilter` key exists | Same immediate fail-closed result. |
| Promisor repository has a missing object and a logging remote helper | Guard halts before object lookup; helper log stays empty; before/after object, ref, log, `FETCH_HEAD`, config, index, and worktree hashes match. |
| Partial/promisor config output is malformed or ambiguous | HALT; no attempt to infer a safe full clone. |
| Full clone has a genuinely missing object | Exact missing-object HALT; no absence, novelty, closure, or approval claim. |

Positive controls must prove that valid config, metadata, sink, parser, grouping,
event, display, and disposition operations still occur in the required order.
Every negative row asserts exact prohibited invocation counts, not only a final
HALT label. Injected clocks test pre-entry and post-return boundaries separately;
fixture-owned callables expose all in-process operation entries independently of
the driver trace.[3][6][7]

### Regression gates

The complete r01 and r02 matrices remain binding except where r03 strengthens
their byte, deadline, trace, or partial-clone oracle. They include missing
revision/commit/blob/body, path copy, old tier, reset or renumbered logs, READY
without a decision, different-artifact human decision, every independent
ceiling, current live duplicate, no-current-clue historical root, and
out-of-corpus work.[2][3]

PASS additionally requires:

- current-tree, synonym, hybrid-query, board, and current-log checks before
  historical work;
- clone-state rejection before every history or object command;
- no body sink larger than its admission-time remaining allowance;
- the accepted-byte total equal to the sum of all body sink `st_size` values,
  including failed, signaled, timed-out, and repeated children;
- every protected operation behind both deadline gates and the externally
  observed dispatcher;
- zero display, classification, disposition, or publication after any failed
  clone, metadata, sink, counter, deadline, or cleanup gate;
- AST proof over the exact driver bytes that protected operations and output
  paths cannot bypass the dispatcher;
- zero network helper, fetch child, or Git-state change in partial/promisor
  fixtures;
- the displayed root count equal to the complete receipt root count;
- exact reachability wording, full reads before disposition, and truthful
  `unknown` states;
- preserved exact driver, harness, fixture, ledger, sink, and oracle bytes for
  independent review; and
- ASCII, resolving links, task-owned cleanup, and an exact one-file production
  diff during any separately authorized implementation.

### Worst failure, costs, and residual uncertainty

The worst plausible failure is a partial or mis-grouped receipt being presented
as complete, causing a repeated idea to be called novel, closed work to be
reopened, or READY to be treated as approval. Closely related failures are a
byte gate that reports HALT only after its sink exceeded the ceiling, a deadline
that allows a late disposition, a trace that cannot reveal prohibited in-process
calls, and a read-only object lookup that demand-fetches into the repository.
Prevention is fail-closed composition: metadata before body, an operating-system
file-size boundary before `exec`, one immutable deadline around every operation,
an external fixture ledger plus structural bypass check, clone-state rejection
before history, exact bodies before decisions, and no later invocation after a
failed gate.[3][6][7][9][11]

Costs are one additional fresh query, bounded Git traversal, one standalone
scratch Python driver, POSIX/Linux resource-limit dependence, a single-thread
restriction, metadata and sink files, immutable state events, a harness-owned
fixture ledger, AST checks, partial-clone fixtures, historical-schema handling,
up to 20 full-body presentations, and more failure modes than doing nothing.
Review time remains unmeasured. The limits are design choices, not economic
optima.[1]

Residual uncertainty remains for merge-heavy histories, object pruning,
rewritten refs, many archive files, unusual path bytes, evolving schemas,
file-system-specific `RLIMIT_FSIZE` behavior, process-creation tails, and future
artifact volume. The proposal-stage limit probe used `/usr/bin/printf`, not Git
or every target filesystem. Atomic repository immutability across all reads is
not claimed. The protocol's pre-write state recheck remains mandatory; a changed
HEAD, board, log, or worktree invalidates the receipt rather than rebasing its
conclusion.[5][11][12]

### Reversal and confidence

Rollback is direct: remove the inserted reachable-history subsection from
`governance/skills/forge-ideate/SKILL.md` and restore the current live-tree,
current-log, Forge-query, and Brain-query procedure. No receipt, index, archive,
ref, status migration, package, service, partial-clone conversion, or external
cleanup must be reversed because the design creates no durable production state.

Confidence is medium. Confidence is high in the frozen object counts, identity
result, and two decision changes because research and independent checks agree.
[1][2] Confidence that r03 addresses the four r02 blockers is medium: primary
interfaces and the local bounded probe support a pre-exec file limit, Git
publishes partial/promisor state, one dispatcher can gate state transitions, and
an external harness ledger can expose fixture calls.[7][8][9][11][12][13]
Overall confidence remains medium because the complete driver, Git body sink,
promisor fixture, root-first display, external-ledger matrix, and final skill
bytes are unexecuted; the sample is one repository history; and the exact limits
are design choices.

Confidence would rise after the exact driver and harness bytes pass every real
and synthetic row, a separate reviewer derives the same counters from sink and
external-ledger evidence, and a later reset changes a novelty decision without a
false merge. It would fall if any sink exceeds its allowance, any protected call
bypasses the dispatcher, any late result reaches publication, a rejected
promisor fixture contacts a remote or changes Git state, clue-led history
produces the same decisions more cheaply, or ordinary full-clone history exceeds
the bounds.

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
2. `forge/proposals/forge-history-duplicate-receipt-r01.md` -- first design,
   normative order, counters, limits, acceptance matrix, and rollback. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r01.md` -- first
     REVISE, pre-body byte blocker, remaining-deadline blocker, required
     corrections, and corrective-cycle count. [high]
3. `forge/proposals/forge-history-duplicate-receipt-r02.md` -- second design,
   metadata-first order, child deadlines, counters, trace contract, acceptance
   matrix, and retained limits. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r02.md` -- second
     REVISE, sink-byte, whole-driver, in-process-observability, partial-clone
     blockers, exact correction request, and exhausted ordinary budget. [high]
4. `governance/skills/forge-ideate/SKILL.md` -- exact proposed target and current
   live-tree, overlap, log, Brain, full-read, and novelty procedure. [high]
   - `forge-index/README.md` -- live-repository hybrid corpus and current query
     interface. [high]
5. `forge/protocol.md` -- correction budget, proposal handoff, exact decisions,
   transaction rechecks, checkpoint route, scope, and no-implementation boundary.
   [high]
   - `STATUS.md` -- selected r02 REVISE handoff and preserved unselected rows at
     starting HEAD `48bb270869b610af0c0f9adf4e2a2467d9d0c54c`. [high]
   - `logbook/progress.log` -- pipeline handoffs through ENT-016 at the same
     starting HEAD. [high]
   - `logbook/errors.log` -- failure record through ENT-021 at the same starting
     HEAD. [high]
6. `LEARNINGS.md` -- evidence-preservation, claimed-result-contract,
   pre-consumption resource, observable-operation, and historical-identity
   lessons. [high]
7. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- revision-specific provenance, bounded repository search, exact receipts, current-state rereading, and verified handoff. [medium]
   - `agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md` -- authoritative state transitions, distinction between traces and control state, finite recovery, and failure-boundary tests. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md` -- consuming-boundary budgets, downward deadlines, trace-level attribution, and fail-closed exhaustion. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md` -- application-owned instrumentation, trace-coverage limits, observable controls, and separate process/outcome evidence. [medium]
8. Git project. "git-cat-file Documentation," updated 2026-09-28; accessed
   2026-09-30, Options, Output, and Batch Output sections. Information-only
   metadata, body-producing modes, object size, and missing-object behavior were
   checked.
   https://git-scm.com/docs/git-cat-file.html [high]
9. Git project. "Partial Clone," updated 2026-09-23; accessed 2026-09-30,
   introduction, Non-Goals, Handling Missing Objects, Fetching Missing Objects,
   and Using Many Promisor Remotes sections. Independence from shallow clone,
   demand-fetch behavior, fetch-subprocess behavior, and promisor configuration
   keys were checked.
   https://git-scm.com/docs/partial-clone [high]
10. Git project. "git-log Documentation," accessed 2026-09-30, Description,
    path limiting, and History Simplification sections. Supplied-revision
    traversal and `--full-history` behavior were checked.
    https://git-scm.com/docs/git-log [high]
    - Git project. "git-rev-list Documentation," accessed 2026-09-30,
      Description and commit-set semantics. Supplied-revision reachability was
      checked. https://git-scm.com/docs/git-rev-list [high]
    - Git project. "git-ls-tree Documentation," accessed 2026-09-30,
      Description, `-r`, `--name-only`, and tree-ish semantics. Frozen-tree path
      enumeration was checked. https://git-scm.com/docs/git-ls-tree [high]
11. Python Software Foundation. "resource - Resource usage information," Python
    3.14.7 documentation, 2026-09-18; accessed 2026-09-30, Resource Limits,
    `setrlimit()`, and `RLIMIT_FSIZE`. Soft/hard limit setting and maximum file
    size were checked.
    https://docs.python.org/3.14/library/resource.html [high]
12. Python Software Foundation. "subprocess - Subprocess management," Python
    3.14.7 documentation, 2026-09-19; accessed 2026-09-30, `Popen`, argument
    vectors, timeouts, POSIX `preexec_fn`, and its thread-safety warning. Child
    execution, timeout, and pre-exec limits were checked.
    https://docs.python.org/3.14/library/subprocess.html [high]
13. Python Software Foundation. "time - Time access and conversions," Python
    3.14.7 documentation; accessed 2026-09-30, `monotonic()` and
    `monotonic_ns()`. Nondecreasing, system-clock-independent elapsed timing was
    checked.
    https://docs.python.org/3.14/library/time.html [high]
