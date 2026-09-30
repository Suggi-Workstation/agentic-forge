---
name: forge-proposal-claim-verification-map
id: 20260930T191144Z
tier: research
pipeline: 20260930T173859Z
author: Researcher
tags: [agent-systems, forge, proposals, verification]
links:
  - forge/ideas/forge-proposal-claim-verification-map-r01.md
  - forge/proposals/forge-history-duplicate-receipt-r01.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r01.md
  - forge/proposals/forge-history-duplicate-receipt-r02.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r02.md
  - forge/proposals/bounded-index-freshness-recheck-r02.md
  - forge/final-reviews/bounded-index-freshness-recheck-review-r02.md
  - governance/template-proposal.md
  - governance/skills/forge-propose/SKILL.md
  - LEARNINGS.md
  - agentic-brain:library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md
  - agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md
  - agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md
  - https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix
  - https://www.nasa.gov/reference/5-3-product-verification
confidence: medium
---
# Research: Forge Proposal Claim-to-Verification Map

## Question and Method

This report tests whether one compact claim-to-verification map can expose the
six known blockers in two failed proposal revisions without falsely blocking one
READY control. The target is the current proposal-writing contract in
`governance/template-proposal.md` and, only if needed, its procedure in
`governance/skills/forge-propose/SKILL.md`. This is a retrospective diagnostic,
not a blind test and not evidence that future proposal revisions will decline.[1]

The provisional explanation, recorded after reading the idea, current template,
method memory, and target proposal chain but before the Brain and web checks, was:
a checklist can confirm that a proposal contains tests while still missing a
contradiction between a material claim and the operation or evidence that is
supposed to verify it. A short row per material claim should make the operation
order, predicate, controls, prohibited later action, and evidence state explicit.
The main risks were hindsight, subjective claim grouping, duplicating the current
checklist, and adding more form than value.[1][2][3]

The frozen instrument was 279 words, SHA-256
`da86c20771d99dc35af972e250bd8139dc6222f168324f351f6336e0b32a6d9f`.
It was fixed before applying it to any proposal. One row covers each material
normative claim or grouped invariant; grouping is permitted only when claims
share one gate, observable result, and evidence state. Each row records:

1. claim and source passage;
2. required operation and order (`O`);
3. observable predicate (`P`);
4. valid positive control (`+`);
5. failure-directed negative case and prohibited later action (`-`);
6. evidence state (`E`: performed, future, or unknown); and
7. `COMPLETE`, `ABSENT`, `CONTRADICTORY`, or `UNVERIFIABLE`.

A material non-`COMPLETE` row is a blocker. Future implementation evidence is not
a blocker when it is labeled future and the proposal fully specifies an
executable acceptance contract. `N/A` requires a reason. The target bytes, map,
and starting Forge HEAD
`6282662e1d6f347284c0163d2f5638fe6dcd58e1` were frozen before classification.
The paired reviews were disclosed answer keys, but each proposal was classified
before its review was consulted.[1][4][5][6]

The selected board row was a valid first `research` stage, the root idea was
written by Analyst rather than Researcher, and the transaction preserved the
unselected human-review row and left `LEARNINGS.md` unchanged.[11]

The first reader filled the maps from the complete source files. A separate
reader in an isolated context received the same frozen map and answer-key
boundary, saved each proposal-only map before opening its review, and then
compared the result. The separate reader took 487.61 seconds. The measured
freeze-to-comparison interval was 527 seconds. This separation reduces accidental
omission but is not model independence because both readers used the configured
model family.[4][5][6]

The current proposal checklist was then applied alone as a baseline. Relevant
Brain files were found through a fresh hybrid index and read in full. NASA's
Requirements Verification Matrix and Product Verification guidance were read as
external primary practice sources. NASA requires unique requirement identity,
source and verification approach, acceptance criteria for each verified
requirement, and reports that trace requirements to verification methods and
results. These sources support traceability and proportional tailoring; they do
not validate this Forge map or its effect on author behavior.[7][8][9][10]

## Evidence and Findings

### Frozen filled map: failed history-receipt r01

The compact notation below preserves every filled field. Source ranges refer to
`forge/proposals/forge-history-duplicate-receipt-r01.md`.[4]

| ID | Claim / lines | Filled verification record | Class |
|:--|:--|:--|:--|
| H1-01 | One-skill scope and rollback / 28-62, 129-133, 397-403 | O: amend one skill only. P: exact one-file diff and direct deletion rollback. +: authorized one-file change. -: any other production write -> fail. E: future. | COMPLETE |
| H1-02 | Current retrieval first / 161-168, 191-195, 208-212 | O: live enumeration, search, index, board, and logs before history. P: ordered trace. +: live duplicate found normally. -: historical judgment before live checks -> no novelty claim. E: future. | COMPLETE |
| H1-03 | Frozen corpus / 134-139, 202-207, 315-316, 336 | O: freeze `START_HEAD` and require non-shallow before traversal. P: exact revision and literal `false`. +: frozen real case. -: shallow or missing revision -> no classification. E: future. | COMPLETE |
| H1-04 | Scratch-only receipt / 213-216, 288-303, 350, 356-364 | O: write only task scratch. P: command receipt and exact production diff. +: scratch artifacts only. -: ref, index, worktree, archive, or board write -> fail. E: future. | COMPLETE |
| H1-05 | Reachable-path enumeration / 217-223, 318-330 | O: enumerate named tier paths, then compare frozen tree. P: complete path counts and current/history split. +: 39-path case. -: missing or out-of-scope path -> no complete receipt. E: performed/future. | COMPLETE |
| H1-06 | Pre-body byte gate / 224-230, 269-276, 334-346 | O: resolve size and reserve before body output. P: zero body bytes for an oversized first artifact or log. +: admitted ordinary blob. -: oversize object -> zero body call and no parse. E: future. The procedure first requires body-producing `git show` success, so the claimed order is violated. | CONTRADICTORY |
| H1-07 | Identity and root view / 145-149, 231-237, 338-341 | O: group by `(pipeline,id)` while retaining aliases, then derive roots. P: one logical identity and all provenance. +: renamed copy. -: cross-pipeline collision -> no merge or canonical path. E: future. | COMPLETE |
| H1-08 | Event recovery / 238-245, 342-343 | O: inspect current logs, then historical versions on demand. P: normalize only ENT counter. +: renumbered copy deduplicates. -: any other byte difference -> keep both. E: future. | COMPLETE |
| H1-09 | Exact evidence before disposition / 150-155, 246-251, 320-330 | O: read root, decisive artifact, and claimed decision event in full. P: exact path/ID and explicit decision. +: recorded REJECT/DEFER. -: READY without human decision -> `unknown`, not approved. E: performed/future. | COMPLETE |
| H1-10 | Ambiguity failure / 252-257, 336-345 | O: validate objects, metadata, identity, tiers, and decisions before judgment. P: typed gap and no disposition. +: valid historical schema. -: malformed or ambiguous input -> no novelty/reopening claim. E: future. | COMPLETE |
| H1-11 | Count and byte ceilings / 156-160, 269-275, 346 | O: test each limit before the next unsupported action. P: counters and incomplete-prefix label. +: frozen case under bounds. -: each independent overflow -> no judgment. E: future. | COMPLETE |
| H1-12 | Context-display ceiling / 277, 329-330, 360-361 | O: build complete root-first view within 16 KiB. P: display root count equals receipt. +: full five-root display. -: overflow or omitted root -> stop or human narrowing, no silent truncation. E: future. | COMPLETE |
| H1-13 | Whole-receipt elapsed ceiling / 156-160, 276, 346, 384-389 | O: enforce one remaining deadline at every blocking command. P: timeout/admission event and no later action. +: ordinary completion under 60 seconds. -: blocking command -> no body, display, or decision. E: future. No remaining-time timeout or blocking-command fixture exists. | ABSENT |
| H1-14 | Cleanup / 258-262, 362 | O: remove only task scratch before a passed transaction. P: verified cleanup result. +: successful cleanup. -: cleanup failure -> report error and no conversion of incomplete work into PASS. E: future. | COMPLETE |
| H1-15 | Preserved executable package / 165-168, 288-311, 352-366 | O: preserve and run exact bytes before and after insertion. P: commands, streams, codes, hashes, timing, and clause mapping. +: full real and synthetic package. -: missing raw evidence or unmapped clause -> fail. E: future. | COMPLETE |
| H1-16 | Frozen positive control / 315-330 | O: reproduce corpus, identities, decisions, and display agreement. P: named exact counts and dispositions. +: frozen revision. -: any mismatch -> no acceptance. E: performed source facts, future package. | COMPLETE |
| H1-17 | Reachability boundary / 134-139, 336-349, 365-366 | O: qualify every absence claim by revision, paths, and budgets. P: bounded wording. +: reachable known root. -: unreachable/pruned/unfetched work -> outside claim, not absence. E: future. | COMPLETE |
| H1-18 | Transaction staleness / 391-395 | O: recheck HEAD and worktree before write. P: byte/state equality. +: unchanged transaction. -: change -> halt without rebasing conclusion. E: future. | COMPLETE |
| H1-19 | Worst failure and reversal / 368-416 | O: fail closed on partial or mis-grouped receipt and retain direct rollback. P: no unsupported novelty/approval plus one-section deletion. +: valid receipt. -: partial evidence -> no claim. E: future. | COMPLETE |

Result: 19 rows, 17 `COMPLETE`, one `CONTRADICTORY`, and one `ABSENT`.
Both blocker rows match the later r01 review: a body can be emitted before the
byte gate, and a running command can exceed the named elapsed ceiling.[4]

### Frozen filled map: failed history-receipt r02

Source ranges refer to
`forge/proposals/forge-history-duplicate-receipt-r02.md`.[5]

| ID | Claim / lines | Filled verification record | Class |
|:--|:--|:--|:--|
| H2-01 | One-skill scope and rollback / 33-73, 175-187, 321-338, 461-467 | O: use one uninstalled scratch driver and change one skill only. P: exact diff and direct deletion rollback. +: one-file amendment. -: durable helper or other production write -> fail. E: future. | COMPLETE |
| H2-02 | Current retrieval first / 35-40, 175-180, 199-202 | O: complete live retrieval before history. P: ordered trace. +: live duplicate. -: history substitutes for live state -> no judgment. E: future. | COMPLETE |
| H2-03 | Frozen corpus / 62-73, 194-198 | O: freeze exact clean HEAD and require non-shallow. P: recorded revision and clone state. +: frozen case. -: missing/shallow corpus -> no absence or novelty claim. E: future. | COMPLETE |
| H2-04 | No network, repository write, or external state / 35-40, 182-206, 402 | O: exclude every clone state that can fetch or write before object reads. P: no network/fetch child/object-database change. +: complete local clone. -: promised missing object -> halt before fetch or write. E: future. The procedure checks only shallow state, so a partial/promisor clone can lazy-fetch. | CONTRADICTORY |
| H2-05 | Child-command deadline / 207-223, 385-391 | O: use one decreasing deadline for every Git child. P: pre-spawn, timeout, and late-return events with zero later child calls. +: child under remaining time. -: expiry/timeout -> no later body or decision. E: future. | COMPLETE |
| H2-06 | Whole-driver deadline / 42-48, 207-223, 299-317 | O: gate child and in-process parsing, grouping, presentation, display, cleanup, and disposition against one deadline. P: typed events around every transition. +: full driver under 60 seconds. -: injected in-process overrun -> no later display or decision. E: future. Only Git children are gated, so later in-process work may cross the deadline. | CONTRADICTORY |
| H2-07 | Body-free enumeration / 224-228, 303-304 | O: enumerate paths without bodies and admit path/root counts before classification. P: exact counters. +: bounded corpus. -: 251st path or 26th root -> no body classification. E: future. | COMPLETE |
| H2-08 | Information-only preflight / 92-116, 229-236, 392 | O: obtain OID, type, and size before body. P: strict record parse and zero body on invalid metadata. +: local 868-byte probe. -: missing/malformed/non-blob record -> no body. E: performed/future. | COMPLETE |
| H2-09 | Declared-size reservation / 237-244, 377-379 | O: compare declared size with remaining allowance before body call. P: zero body calls when declared size exceeds allowance. +: exact-fit object. -: oversize artifact/log -> no body or parse. E: future. | COMPLETE |
| H2-10 | Hard actual-output ceiling / 237-252, 379-383, 426-444 | O: enforce remaining bytes at the sink before accepting output. P: accepted bytes never exceed 8 MiB. +: exact-fit output. -: extra or partial output -> sink stops at allowance and no parse. E: future. The design measures only after output, so the sink can already cross the claimed ceiling. | CONTRADICTORY |
| H2-11 | Aliases, repeated calls, presentations / 237-261, 382-384 | O: materialize each OID once, retain aliases, and count every repeated call or presentation as specified. P: trace-derived counters. +: several aliases, one call. -: repeated body call or 21st presentation -> no judgment. E: future. | COMPLETE |
| H2-12 | Historical-log gates / 262-268, 378, 389-397 | O: apply the same metadata, byte, and deadline gates to logs before event classification. P: shared counters and exact event normalization. +: duplicate ENT copy. -: oversize/late/different event -> no inferred decision or over-deduplication. E: future. | COMPLETE |
| H2-13 | Identity and display / 269-274, 360-371, 393-400 | O: group exact identities, retain aliases and literal tiers, then build the complete root view. P: display/receipt agreement. +: five-root control. -: collision, malformed schema, or omitted root -> no decision. E: future. | COMPLETE |
| H2-14 | Full evidence before disposition / 275-279, 398-399 | O: read root, decisive artifact, and exact decision event fully. P: explicit exact-artifact decision. +: recorded terminal verdict. -: READY or different-artifact decision -> `unknown`/halt. E: future. | COMPLETE |
| H2-15 | Unsupported-boundary closure / 280-288, 392-402 | O: stop at every listed object, metadata, counter, deadline, or decision fault. P: typed terminal reason and zero judgment. +: valid path. -: each listed fault -> no novelty/reopening claim. E: future. | COMPLETE |
| H2-16 | Trace-derived in-process counters and prohibited calls / 290-310, 400-409, 422-432 | O: emit independently observable events for parsing, root classification, deduplication, presentation, display, cleanup, and disposition. P: oracle derives every counter and absence claim from events. +: complete valid path. -: omitted in-process call -> oracle detects it and no judgment. E: future. The schema records commands only, so these predicates cannot be derived. | UNVERIFIABLE |
| H2-17 | Transaction recheck and cleanup / 285-288, 335-336, 419, 429 | O: recheck repository state and clean task scratch before write. P: unchanged snapshot and cleanup receipt. +: clean transaction. -: state or cleanup failure -> no passed judgment. E: future. | COMPLETE |
| H2-18 | Preserved implementation package / 182-187, 319-353, 404-432 | O: preserve exact driver and fixture bytes and run pre/post insertion. P: raw arguments, outputs, traces, counters, exceptions, and cleanup. +: complete package. -: missing evidence or unmapped clause -> fail. E: future. | COMPLETE |
| H2-19 | Frozen real-history control / 344-371 | O: reproduce exact corpus, decisions, bytes, one-call rule, and display/trace agreement. P: named counts and outcomes. +: frozen revision. -: any mismatch -> no acceptance. E: performed source facts, future package. | COMPLETE |
| H2-20 | Inherited r01 regressions / 411-420 | O: retain all r01 reachability, schema, decision, ordering, cleanup, and diff tests. P: full regression results. +: prior valid cases. -: any regression -> fail. E: future. | COMPLETE |
| H2-21 | Worst failure and reversal / 434-484 | O: prevent partial-resource receipt from becoming a decision and preserve direct rollback. P: no unsupported judgment and one-section deletion. +: valid run. -: stale/partial/over-budget run -> no claim. E: future. | COMPLETE |

Result: 21 rows, 17 `COMPLETE`, three `CONTRADICTORY`, and one
`UNVERIFIABLE`. All four blocker rows match the later r02 review: actual output
can cross the byte ceiling; in-process work can cross the whole-driver deadline;
a command-only trace cannot establish in-process counters or prohibited calls;
and a shallow-only guard does not prevent partial-clone lazy fetch.[5]

### Frozen filled map: READY bounded-freshness r02 control

Source ranges refer to
`forge/proposals/bounded-index-freshness-recheck-r02.md`.[6]

| ID | Claim / lines | Filled verification record | Class |
|:--|:--|:--|:--|
| F2-01 | Two-skill scope and authority / 36-66, 153-165, 223-237 | O: change only two source skills after separate approval. P: exact two-file diff. +: two equivalent blocks. -: runtime, producer, installed-skill, or other file change -> fail. E: future. | COMPLETE |
| F2-02 | Watcher prerequisite / 169-172, 255 | O: verify exact watcher before freshness. P: watcher check precedes command. +: watcher present. -: missing/unreadable crontab -> no freshness or query. E: future. | COMPLETE |
| F2-03 | Scratch and snapshots / 173-176, 243-247, 263 | O: create task scratch and capture full HEAD plus NUL status before first check. P: byte-preserved files and invocation trace. +: successful captures. -: scratch/capture failure -> no query. E: future. | COMPLETE |
| F2-04 | Immediate success / 177-180, 251, 275-276 | O: preserve exit 0 plus literal `OK --` as immediate gate. P: one freshness call, no wait, one query. +: valid immediate result. -: nonzero `OK --` -> no query. E: future. | COMPLETE |
| F2-05 | Sole retry trigger / 42-54, 181-188, 252-258 | O: require exit 1, empty stderr, exact one-line bytes, and unchanged state. P: exact full match and counts. +: lower/upper hex cases. -: every near match or other status -> no wait, second call, or query. E: performed classifier/future shell. | COMPLETE |
| F2-06 | One bounded wait / 62-65, 189-195, 261 | O: calculate one 1-90 second delay and sleep once under monotonic ceiling. P: one wait and elapsed result. +: eligible recovery. -: invalid delay/interruption/overrun -> no second call or query. E: future. | COMPLETE |
| F2-07 | Post-wait state gate / 196-198, 259 | O: compare HEAD and status before second check. P: byte equality. +: unchanged state. -: any change -> no second call or query. E: future. | COMPLETE |
| F2-08 | Second check and state gate / 199-207, 260-262 | O: run the same command once, then compare state again. P: two calls maximum; exit 0, `OK --`, and unchanged state. +: exact recovery. -: state change or any failed second result -> no query. E: future. | COMPLETE |
| F2-09 | Cleanup before query / 208-209, 243-247, 263 | O: earn permission, complete cleanup, then invoke query. P: cleanup-failure fixture has zero query calls. +: successful cleanup then query. -: cleanup failure -> no query. E: future. | COMPLETE |
| F2-10 | No producer or fallback action / 62-66, 120, 235-237, 269-270 | O: observe only; never invoke watcher, indexer, rebuild, fallback, or poll. P: zero prohibited calls. +: natural watcher recovery. -: any prohibited call -> fail. E: future. | COMPLETE |
| F2-11 | Residual race boundary / 211-215 | O: state the remaining check-to-use interval. P: no atomicity claim. +: unchanged-state flow. -: atomic exclusion becomes required -> invalidate design and research anew. E: future. | COMPLETE |
| F2-12 | Executable two-variant harness / 223-234, 241-247 | O: test stubbed sequence in both substitutions before and after insertion. P: exact trace and preserved bytes/results. +: both variants pass. -: semantic drift or missing trace -> fail. E: future. | COMPLETE |
| F2-13 | Negative matrix / 249-264 | O: exercise every status, format, race, timing, second-result, instrumentation, and cleanup boundary. P: final result and exact invocation counts. +: valid controls. -: each failure -> named prohibited calls remain zero. E: future. | COMPLETE |
| F2-14 | Positive and regression controls / 251-253, 265-276 | O: retain immediate and delayed positives, 22-case classifier, syntax, ASCII, equivalence, and old failures. P: exact outcomes and 22/22 control. +: three success rows. -: producer-side action, syntax drift, or broadened gate -> fail. E: performed classifier/future shell. | COMPLETE |
| F2-15 | Worst-failure prevention / 281-290 | O: bind each stale/mismatched retrieval cause to a gate before query. P: no query after any failed gate. +: verified fresh path. -: broad match, lost status, reused output, or state change -> no query. E: future. | COMPLETE |
| F2-16 | Cost, rollback, drift, confidence / 292-311 | O: remove two blocks on failure or producer-text drift. P: immediate-HALT behavior restored without migration. +: tested exact bytes. -: contract drift or failed race fixture -> rollback. E: future. | COMPLETE |

Result: 16 rows, all `COMPLETE`, and zero false blockers. Step 8 grants
query permission before Step 9 cleanup, but the cleanup-failure acceptance row
requires zero query calls; the paired READY review confirms that actual query
execution follows successful cleanup. The map therefore records an implementation
conformance condition without converting it into a false design blocker.[6]

### Comparative result

| Target | Rows | Complete | Absent | Contradictory | Unverifiable | Blockers |
|:--|--:|--:|--:|--:|--:|--:|
| History receipt r01 | 19 | 17 | 1 | 1 | 0 | 2 |
| History receipt r02 | 21 | 17 | 0 | 3 | 1 | 4 |
| Bounded freshness r02 | 16 | 16 | 0 | 0 | 0 | 0 |
| Total | 56 | 50 | 1 | 4 | 1 | 6 |

The map found all six disclosed blockers and no positive-control false blocker.
The separate reader reproduced all six blocker classifications and all 56 row
classifications after reading proposals before reviews. There were no substantive
classification disagreements. Two labels admit reasonable alternatives:
H2-04 also lacks a partial-clone fixture and could be called `ABSENT`, but
`CONTRADICTORY` is more specific because the permitted procedure violates its
no-network/no-write claim; H1-13 could be framed as permitting overrun, but
`ABSENT` is more specific because both the running-command gate and fixture are
missing.[4][5][6]

The current proposal checklist represented all eight checklist items in each
of the three proposals and mechanically detected zero of the six blockers. It
asks for a feasible specification and observable acceptance, regression, and
negative tests, but it does not require a row from each material claim to its
operation order, consuming-boundary predicate, effective configuration scope,
or observable prohibited later actions. The stronger requirement exists in
`LEARNINGS.md`, but a prose lesson did not make compliance mechanically visible
in either failed revision.[2][3]

The result is consistent with external and Brain evidence. Systems engineering
uses traceability to connect requirements, design, verification method, and
acceptance evidence, while tailoring the artifact to consequence.[7][9][10]
Agent observability work warns that a trace proves only what its instrumentation
emits, and resource-governance work distinguishes a machine-enforced consuming-
boundary limit from post hoc measurement.[8] These sources explain why H2-10 and
H2-16 fail, but the six detections themselves come from exact Forge proposal and
review text, not from analogy.[4][5]

## Alternatives and Implications

| Alternative | Evidence | Implication |
|:--|:--|:--|
| Keep the current checklist and do nothing | All three proposals represented 8/8 checklist items; the failed revisions still contained six review blockers.[2][4][5] | Lowest ceremony, but this retrospective baseline detected 0/6 blockers before review. |
| Strengthen the existing lesson only | The high-confidence lesson already names predicates, negative fixtures, consuming-boundary order, prohibited calls, and effective configuration scope.[3] | Less template text, but r01 and r02 were written while related lesson text existed; prose alone supplied no per-proposal compliance record. |
| Add one compact claim-to-verification map | The 279-word instrument classified 56 grouped claims, detected 6/6 answer-key blockers, and produced 0/16 false blockers on the READY control.[4][5][6] | Supported for evaluation as a concise pre-write gate, provided it is tailored to material normative claims and permits justified `N/A`. |
| Require a large requirements matrix for every proposal | NASA practice supports requirement-to-verification traceability but also supports tailoring to project scope.[7][9][10] | Rejected: descriptive or low-risk proposals should not inherit ceremonial rows unrelated to their claims. |
| Build an executable checker | A prior Forge checker was deferred after rejecting a valid real record, and semantic claim extraction remains judgment-dependent.[1][3] | Rejected from this scope. The evidence supports a manual artifact, not automation, runtime, or repository-wide validation. |

The evidence supports a narrow implication: evaluation should consider adding a
small claim-to-verification table to the proposal gate for material normative,
resource-bound, operation-order, and no-action claims. A useful row needs the
claim/source, required order, predicate, positive control, failure-directed
negative case, prohibited later action, and performed/future/unknown evidence
state. The table should group only claims sharing one gate and evidence state,
and allow `N/A` with a reason. It should not require rows for descriptive
rationale, repeat the entire acceptance section, or become an executable checker.

The evidence does not establish fewer future revisions, lower authoring time,
better behavior on other proposal classes, or economic benefit. The negative
cases are two revisions of one unusually complex pipeline; the positive control
is one READY proposal; the answer keys were disclosed; and the second reader
used the same model family. The instrument's apparent precision also depends on
human claim extraction and grouping. A prospective trial on new proposals would
be needed before claiming a causal improvement.

## Response to Feedback and Remaining Questions

No prior evaluation of this research report exists. The root idea required a
retrospective test against two failed revisions, one READY control, the current
checklist, doing nothing, prose-only strengthening, and an executable checker.
All were addressed. Every filled map is preserved above; all six known blockers
were detected; the positive control had no false blocker; a separate reader
reproduced the classifications; and the current checklist detected none of the
six.[1]

No decision-critical evidence gap blocks independent evaluation of this result.
The remaining questions are proposal-design questions for evaluation:

1. Is 56 grouped rows across three complex proposals acceptably compact, or
   should a future gate apply only to claims containing hard bounds, required
   order, prohibited actions, or explicit no-side-effect assertions?
2. Should the map live in the proposal template alone, or should the propose
   skill contain one instruction defining row selection and justified `N/A`?
3. What prospective proposal sample and unchanged reviewer baseline would be
   sufficient to measure incremental detection, author time, and false blockers
   without using disclosed answer keys?
4. Can two reviewers agree on complete claim extraction when they do not share a
   model family or the known verdict?

Confidence is medium. Exact proposal/review comparisons, complete filled maps,
a frozen instrument, 6/6 blocker recovery, 0/16 positive-control false blockers,
and separate-reader agreement support the retrospective diagnostic. Confidence
is not high because the failed cases share one pipeline, the READY control is
single, answer keys were disclosed, grouping remains judgment-dependent, and no
prospective authoring outcome was measured. Confidence would rise after a cold,
different-model reader reproduces complete claim extraction and a prospective
trial detects decision-relevant defects without increasing false blockers or
review cost. It would fall if independent readers omit material claims, valid
proposals are blocked by ceremonial rows, or the map adds no detection beyond an
explicit reading of the current lesson.

## Sources

1. `forge/ideas/forge-proposal-claim-verification-map-r01.md` -- exact question,
   target, retrospective cases, disclosed thresholds, alternatives, research
   plan, and stated evidence limits. [high]
2. `governance/template-proposal.md` -- current proposal sections and eight-item
   checklist baseline, including acceptance, regression, negative, reversal, and
   future-work requirements. [high]
   - `governance/skills/forge-propose/SKILL.md` -- current proposal procedure,
     implementable-scope gate, Feynman use, evidence-gap route, and handoff.
     [high]
3. `LEARNINGS.md` -- high-confidence claim-contract lesson, pre-consumption
   resource gates, observable prohibited actions, effective configuration scope,
   and current evidence limits. [high]
4. `forge/proposals/forge-history-duplicate-receipt-r01.md` -- first negative
   target, normative sequence, resource ceilings, acceptance matrix, scope, and
   evidence-state claims. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r01.md` --
     disclosed answer key for the body-before-byte and running-command-deadline
     blockers. [high]
5. `forge/proposals/forge-history-duplicate-receipt-r02.md` -- second negative
   target, corrected metadata/deadline design, counters, trace, clone, and
   acceptance claims. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r02.md` --
     disclosed answer key for actual-output, in-process deadline, trace-coverage,
     and partial-clone blockers. [high]
6. `forge/proposals/bounded-index-freshness-recheck-r02.md` -- READY positive
   control, exact trigger, state gates, cleanup contract, acceptance matrix,
   rollback, and future-evidence boundary. [high]
   - `forge/final-reviews/bounded-index-freshness-recheck-review-r02.md` -- READY
     answer key, cleanup-order clarification, retained limits, and no-
     implementation boundary. [high]
7. `agentic-brain:library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md` -- requirements-to-verification traceability,
   acceptance evidence, lifecycle configuration, and proportional tailoring.
   [medium]
8. `agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md` -- instrumentation coverage, explicit control events, trace limits, and
   separation of outcome, process, and operational evidence. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md` -- hard limits at consuming boundaries, downward deadlines,
     trace-level attribution, and explicit terminal states. [medium]
9. National Aeronautics and Space Administration. "Appendix D: Requirements
   Verification Matrix," NASA Systems Engineering Handbook, page last updated
   2023-07-26; accessed 2026-09-30. Unique requirement identity, source, and
   verification approach were checked.
   https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix
   [high]
10. National Aeronautics and Space Administration. "5.3 Product Verification,"
    NASA Systems Engineering Handbook, accessed 2026-09-30, sections 5.3.1.1,
    5.3.1.2, 5.3.1.3. Per-requirement acceptance criteria, recorded methods and
    results, objective evidence, and bidirectional traceability were checked.
    https://www.nasa.gov/reference/5-3-product-verification [high]
11. `forge/protocol.md` -- artifact contract, board selection, one-stage
    transaction, source format, research-to-evaluate handoff, and read-only
    learning boundary. [high]
    - `STATUS.md` -- selected research row and preserved unselected human-review
      row at starting HEAD `6282662e1d6f347284c0163d2f5638fe6dcd58e1`.
      [high]
    - `logbook/progress.log` -- selected ideation handoff at ENT-016 and complete
      current pipeline state through ENT-018 at the same starting HEAD. [high]
