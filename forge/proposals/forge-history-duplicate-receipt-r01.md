---
name: forge-history-duplicate-receipt
id: 20260930T150618Z
tier: proposal
pipeline: 20260930T124036Z
author: Researcher
tags: [agent-systems, forge, retrieval, provenance]
links:
  - forge/ideas/forge-history-duplicate-receipt-r01.md
  - forge/research/forge-history-duplicate-receipt-r01.md
  - forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md
  - governance/skills/forge-ideate/SKILL.md
  - forge/protocol.md
  - LEARNINGS.md
  - forge-index/README.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md
  - https://git-scm.com/docs/git-log
  - https://git-scm.com/docs/git-rev-list
  - https://git-scm.com/docs/git-show
  - https://git-scm.com/docs/git-ls-tree
confidence: medium
---
# Proposal: Bounded Reachable-History Receipt for Forge Ideation

## Proposed Decision

Approve, for separately authorized implementation and review, one bounded
amendment to the prior-work procedure in
`governance/skills/forge-ideate/SKILL.md`. The amendment adds a read-only,
scratch-only reachable-history receipt after current-tree enumeration and
current Forge hybrid search, but before a new-idea novelty judgment. The
beneficiaries are Forge agents and Suggi: an idea should not be called new when
its closest pipeline and exact disposition remain reachable from the selected
Git revision but no longer exist in the live tree or live index.[1][2][3]

The output type is a skill/rule amendment. The requested decision is to approve
the design for later implementation, fixture execution, review, and deployment;
this proposal changes no skill and grants no implementation authority.[4]

The smallest useful change is one new subsection in the existing ideation skill,
not a second board, archive, index, manifest, repository tool, ref, or restored
artifact. It freezes the current `HEAD`, verifies that the clone is not shallow,
enumerates Forge artifacts reachable from that revision, groups logical
artifacts by root pipeline plus artifact ID, and presents roots and possible
decision evidence before path detail. Complete path and event receipts remain in
task-owned scratch for drill-down. Any unresolved identity, object, metadata,
decision, or budget condition blocks a novelty or reopening claim.[1][5]

Non-goals are:

- archival completeness, recovery of unreachable, pruned, unfetched, rewritten,
  or never-committed work;
- a history-aware semantic index or any change to live-index scope, freshness,
  watcher, cron, model, runtime, or query ranking;
- a durable tombstone, receipt, cache, status file, tag, branch, or competing
  decision record;
- automatic semantic duplicate classification, automatic reopening, or an
  inference that READY means approved;
- edits to `forge/protocol.md`, `STATUS.md`, logs, templates, other skills, or
  any external repository during implementation of this amendment; and
- proof that the proposed ceilings are economically optimal.

## Evidence, Alternatives, and Evaluation Response

### Explanation rebuilt from checked evidence

The provisional explanation before the additional Brain and Git checks was
simple: live search is a view of the current tree, while Git can still expose a
deleted body reachable from a frozen revision; therefore the smallest repair is
a temporary identity-preserving inventory, followed by full reading of only
plausible overlaps. The main ways this could fail were false completeness,
rename overcounting, cross-pipeline identity collision, inferred disposition,
context flooding, and review cost.

The checked evidence narrows that explanation. At frozen revision
`d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06`, the research instrument and an
independent evaluator traversal both found 8 current artifact paths, 39
reachable artifact paths, 34 logical artifact IDs, 5 roots, 5 alias groups, and
zero cross-pipeline ID conflicts. Exact historical bodies changed two bounded
decisions: one apparent new maintenance-capex lead was an exhausted-budget
same-pipeline reframe, and one uncertain SBC lead was a recorded REJECT with
reopening conditions. A READY unattended-command review remained unknown
because no explicit human disposition was found. The current bounded-freshness
pipeline remained a positive live-corpus control.[1]

Known facts are therefore limited but sufficient for a design:

- Git-object traversal and independent verification reproduced the frozen
  corpus and identity counts.[1]
- Paths alone overcounted five logical artifacts; pipeline plus artifact ID was
  stable in this corpus, while path, containing commit, and blob remained
  necessary provenance.[1][5]
- The current index searches the live repository corpus and returns one ranked
  result per live file; it is not a history archive.[3]
- Git documents that `git log` traverses commits reachable from supplied
  revisions, `git show <commit>:<path>` reads a historical path, and
  `git ls-tree` enumerates a named tree.[8][9][10][11]
- Brain prior work independently supports revision-specific provenance,
  bounded context, drill-down evidence, explicit current projections, and
  truthful unknown states.[6][7]

The inference is that a standard root-first receipt can make the existing
all-work duplicate rule more executable after a reset. Still unknown are future
reset frequency, prospective duplicate frequency, reviewer time, false-merge
rate outside the five-pipeline sample, behavior after rewritten or pruned
history, and whether clue-led targeted history usually reaches the same decision
more cheaply.[1]

The proposal is invalidated, or should be reversed, if a cold implementation
cannot reproduce the frozen corpus, a common history shape escapes the receipt,
identity grouping merges pipelines, a recorded human decision is missed, the
root-first view does not improve a real novelty decision, or normal review cost
exceeds the value of the recovered cases.

### Alternatives

| Alternative | Evidence-supported benefit | Cost and disposition |
|:--|:--|:--|
| Keep current-tree enumeration and current hybrid search only | Simplest and correct for live files; it recovered the current bounded-freshness control.[1][3] | It exposed only one of five exact roots at the frozen revision, omitted every deleted body, and supplied no maintenance-capex clue. Retain as the first phase and direct rollback, not as sufficient historical coverage. |
| Use clue-led `git log` and `git show` only | Smallest historical method when a current file or query already names the prior work.[1][8][10] | Three deleted roots had live clues, but maintenance capex had none and the SBC clue omitted its terminal verdict. Keep as a lower-cost drill-down path after a clue, not as the only discovery mechanism. |
| Add the proposed scratch-only root-first receipt | Recovered all five bounded roots and exact decision evidence without a durable state surface.[1] | Adds traversal, historical-schema handling, explicit ceilings, and candidate-body review. Recommend only with the fail-closed acceptance package below. |
| Add a tombstone manifest or archive to the live tree | Could make deleted roots directly searchable. | Rejected: creates durable competing state with lifecycle and drift risk; untested and outside the evaluated scope. |
| Build a history-aware semantic index | Could rank deleted bodies semantically. | Rejected: changes corpus and freshness semantics, adds a larger indexing problem, and exceeds the evidence. |
| Do nothing | No new procedure or review burden. | Credible if resets remain rare and clues are normally sufficient, but accepts the demonstrated no-clue and omitted-verdict cases. |

### Response to every ADVANCE obligation

1. **Exact target and bounded form:** the only proposed production-source edit is
   `governance/skills/forge-ideate/SKILL.md`. The insertion is a short
   reachable-history subsection in its prior-work procedure. No durable receipt,
   repository helper, board, archive, index, manifest, or restored artifact is
   proposed.[1][2]
2. **Explicit reachable population:** the procedure freezes one exact starting
   `HEAD` and uses that revision alone as the reachability root. It verifies
   `git rev-parse --is-shallow-repository` is literal `false`. Every negative
   statement is labeled "not found in the artifacts and logs reachable from
   `<full HEAD>` under the tested paths and budgets," never "no prior work
   exists." Missing or unreadable objects make the result unknown.[1][8][9]
3. **Root-first context:** the model receives a compact root table before any
   descendant-path manifest. Each row contains root pipeline, root artifact ID
   and path, current-versus-historical presence, candidate terminal artifact,
   candidate decision-event reference, and an ambiguity flag. The complete
   manifest remains in scratch for cited drill-down.[1][6]
4. **Identity and provenance:** logical artifacts are grouped only by
   `(pipeline, artifact-id)`. Every path alias keeps its containing commit, blob,
   literal tier, and literal historical schema values. A single artifact ID
   associated with different pipelines halts; path copies are not counted as
   independent evidence and are never silently normalized.[1][5]
5. **Full-body decision gate:** a possible overlap is not classified from the
   table, snippet, filename, or stage label. The agent reads the root and exact
   decisive artifact in full, then reads the exact decision event when one is
   claimed. READY remains nonapproval; absent exact human disposition remains
   `unknown`. Copied or renumbered log events are deduplicated without losing
   their path, commit, and blob aliases.[1][4]
6. **Finite resource limits:** path, root, byte, event, body-read, elapsed-time,
   and context-display ceilings are explicit below. Crossing any ceiling stops
   before a novelty, reopening, closure, or approval judgment; truncation is not
   represented as completeness. The loop uses the protocol's checkpoint or HALT
   route rather than fabricating a root idea.[1][4]
7. **Current retrieval remains first:** current-tree enumeration, keyword/synonym
   search, active and archived current-log checks, and the existing Forge hybrid
   query remain the first phase. The history receipt supplements deleted-body
   discovery and never substitutes for current state or semantic review.[1][2][3]
8. **Executable acceptance package:** a separately authorized implementer must
   run the frozen-revision and synthetic-repository matrix below from exact
   preserved bytes before inserting the skill text, then rerun it after the
   insertion and map every skill clause to an observable result.[1][5]
9. **Costs and unknowns:** clue-led history and doing nothing remain live
   alternatives. The one-host timing is an observation, not an operating bound;
   future duplicate frequency, review time, net benefit, and post-reset behavior
   remain unknown.[1]
10. **Authority and rollback:** implementation, skill modification, review,
    propagation, and deployment remain separately authorized. Rollback deletes
    the one inserted procedure and restores the existing current-tree-only prior-
    work sequence; no data or index migration exists.[4]

No new decision-critical research gap blocks this specification. The unmeasured
future frequency and review economics limit confidence and are explicit review
and observation questions. They do not prevent testing a reversible one-file
procedure whose failure path is to stop without a novelty judgment.

## Change Specification and Implementation

### Affected interface and exact placement

Current `forge-ideate` Step 2 enumerates live graveyard, idea, and proposal files,
searches the candidate and synonyms, follows plausible overlaps, and checks
current and archived progress logs. Step 3 queries Brain prior knowledge.[2]

The proposed implementation inserts a subsection named `Reachable-history
receipt` at the end of Step 2. It keeps every current check, explicitly includes
the existing `query-forge-vps` hybrid query for the candidate and synonyms, and
then runs the bounded historical procedure below before Step 3 and before a new-
idea novelty judgment. No other production file changes.

### Normative procedure

A separately authorized implementer should encode these rules concisely in the
skill:

1. **Freeze and label the corpus.** Record full `START_HEAD=$(git rev-parse
   HEAD)`, repository root, and literal shallow status before historical work.
   Require a clean transaction under `forge/protocol.md` and literal `false` from
   `git rev-parse --is-shallow-repository`. The revision set is exactly
   `START_HEAD`, not `--all`, changing refs, reflogs, or an inferred remote set.
   State this boundary in every receipt and conclusion.[4][8][9]
2. **Complete current retrieval first.** Enumerate live Forge tier files, run
   current keyword/synonym search, use the existing fresh `query-forge-vps`
   hybrid route, inspect the board, and check active and archived current logs.
   Record current clues and exact paths. Do not treat an index miss as historical
   absence.[2][3]
3. **Create task-owned scratch only.** Store command receipts, manifests, copied
   object bodies, event blocks, counters, elapsed time, and the compact display
   under the configured scratch directory. Write no Forge file, ref, index,
   archive, tag, branch, or worktree during receipt construction.
4. **Enumerate reachable artifact paths.** Under `START_HEAD`, use
   `git log <START_HEAD> --full-history --name-only --format=` limited to
   `forge/ideas`, `forge/research`, `forge/evaluations`, `forge/proposals`,
   `forge/final-reviews`, `forge/discoveries`, and `forge/graveyard`. Retain only
   `.md` paths in those directories. Compare them with `git ls-tree -r
   --name-only <START_HEAD> -- <tier directories>` so current and historical-only
   paths stay distinct.[8][11]
5. **Bind every path to exact bytes.** For each unique path, find the newest
   commit reachable from `START_HEAD` whose `git show <commit>:<path>` succeeds.
   Before reading the body, obtain its blob and size; stop if a budget would be
   crossed. Parse the required frontmatter without rewriting old values. Record
   path, containing commit, blob, byte count, SHA-256, artifact ID, literal tier,
   and pipeline. Unreadable bodies, missing metadata, duplicate keys, or a
   cross-pipeline artifact-ID collision halt the judgment.[5][10]
6. **Group identities and build the root view.** Group by `(pipeline,
   artifact-id)` while retaining every provenance alias. Derive root rows only
   from exact idea bodies whose `pipeline` equals the root idea ID. The compact
   display lists root first, then the furthest candidate artifact under the
   literal recorded chain, without assigning a disposition. Old tier values such
   as `review` remain literal and may be mapped to a current review candidate
   only when the artifact body and links establish that role.
7. **Recover candidate events on demand.** For a plausible overlapping root,
   inspect exact current and archived progress blocks first. If disposition is
   still unresolved, traverse versions of `logbook/progress.log` and
   `logbook/archive/progress-*.log` reachable from `START_HEAD`, preserving log
   path, containing commit, blob, and original block. For duplicate detection,
   hash the complete event block after replacing only the header's `ENT-NNN`
   counter with a fixed token. Keep all provenance aliases for matching hashes;
   do not merge blocks that differ anywhere else.
8. **Read before deciding.** Read the candidate root, exact terminal or decisive
   artifact, and any claimed human-decision event in full. Require an explicit
   verdict or an explicit human decision naming the exact artifact under the
   protocol. READY means ready for discovery or review, not approved. No exact
   decision means `unknown`. Historical records establish recorded Forge state,
   not the truth of every domain claim they contain.[4][7]
9. **Stop on ambiguity or budget.** A missing object, malformed metadata,
   ambiguous root, cross-pipeline identity collision, unreadable decisive body,
   unsupported historical-tier mapping, or any ceiling breach stops the novelty
   or reopening judgment. Record the exact bounded gap in the protocol's
   checkpoint or HALT route. Never truncate and then describe the result as a
   complete receipt.
10. **Clean and preserve the decision evidence.** Before the stage transaction,
    retain only the bounded evidence needed in the idea's Sources and reasoning;
    remove task-owned receipt scratch under the existing scratch policy. A
    cleanup failure is reported as a real error and does not turn an incomplete
    receipt into a passed gate.

### Initial ceilings

The following ceilings are design limits, not measured optima or service-level
claims. They are intentionally above the frozen positive case but finite:

| Resource | Initial ceiling | Required overflow result |
|:--|:--|:--|
| Unique reachable artifact paths | 250 | Stop before body classification; checkpoint or HALT. |
| Root pipelines | 25 | Stop; do not show a truncated root set as complete. |
| Artifact and historical-log object bytes read | 8 MiB total | Stop before the next object; report the tested prefix as incomplete. |
| Deduplicated progress events | 500 | Stop without inferring disposition from the retained prefix. |
| Full candidate bodies read for disposition | 20 | Stop before the next judgment; name the unresolved candidate. |
| Receipt assembly elapsed time | 60 monotonic seconds | Stop and checkpoint the exact resume boundary; no novelty judgment. |
| Root-first contextual display | 16 KiB | Stop or narrow through an explicit human-selected candidate; never silently omit roots. |

The frozen positive case used 39 paths, 5 roots, 693,114 artifact bytes, 10
minimum root/decisive reads plus 1 proposal read, and 2.851947649 seconds through
receipt assembly. Those observations show that the proposed ceilings admit the
known case; they do not establish future adequacy or optimal cost.[1]

### Ordered implementation

A separately authorized implementation should:

1. Freeze the current ideation skill, protocol, and exact proposal revision.
2. Build a scratch-only reference implementation of the normative receipt. Keep
   its exact bytes, fixture builders, command lines, stdout, stderr, exit codes,
   hashes, and elapsed-time outputs together outside the repository.
3. Run the frozen real-history case and every synthetic fixture below. Do not
   rebuild an index, alter refs, manufacture repository history in the live
   clone, or restore historical files.
4. Insert one concise subsection into
   `governance/skills/forge-ideate/SKILL.md`. Map each sentence to a passed
   reference-implementation predicate; remove wording that has no observable
   check.
5. Rerun the complete package against the exact final procedure and a disposable
   synthetic Git repository. Verify that no production repository file except
   the one authorized skill changed.
6. Run format, link, ASCII, diff, and applicable governance checks. Stop for
   separate review, approval, propagation, and deployment.

## Acceptance, Risks, and Reversal

### Executable acceptance package

The package is future implementation evidence; no skill amendment or package was
executed in this proposal stage. PASS requires preserved exact bytes and raw
results for all rows.

#### Frozen real-history control

Against revision `d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06` in a non-shallow
clone, the package must reproduce:

- 8 current artifact paths, 39 reachable artifact paths, 34 logical artifact
  IDs, 5 root pipelines, 5 alias groups, and 0 cross-pipeline ID conflicts;
- the maintenance-capex root and r02 REFRAME with exhausted ordinary correction
  budget, changing a plausible new idea into a same-pipeline issue;
- the SBC root and r02 REJECT, changing unknown disposition into closed work with
  explicit reopening conditions;
- the transaction-checker DEFER and exhausted budget without treating it as new;
- the unattended-command READY review and exact proposal, with deduplicated
  progress evidence but no explicit human disposition, therefore `unknown`;
- the bounded-freshness discovery as the live current-corpus control awaiting
  human review; and
- the exact root-first display plus a complete scratch manifest whose count,
  hashes, aliases, decisions, and unknown state agree with the full receipt.[1]

#### Synthetic failure and regression matrix

| Fixture | Required result |
|:--|:--|
| Shallow repository | Immediate HALT before historical classification; no absence claim. |
| Missing revision, commit, blob, or historical body | HALT with the exact missing object; result remains unknown. |
| Same artifact ID under two pipelines | HALT; no merge, novelty verdict, or selected canonical path. |
| One artifact copied or renamed across paths | One logical `(pipeline, id)` group; every path, commit, and blob alias retained. |
| Historical `tier: review` body | Literal value preserved; current-role mapping only after full body/link evidence. |
| Malformed, missing, duplicated, or conflicting required frontmatter | HALT before root or disposition classification. |
| Active and archived log copies with reset or changed ENT counter | One canonical event only when all non-counter bytes match; every source alias retained. |
| Two events share pipeline and stage but differ in time, body, artifact, or decision | Keep both; do not over-deduplicate. |
| READY final review with no exact human decision | Disposition `unknown`, never approved or closed. |
| Explicit human decision names a different discovery ID or path | Do not apply it to the candidate; HALT ambiguity if linkage cannot be resolved. |
| Each ceiling exceeded independently | Stop before the unsupported judgment; label retained data incomplete; use checkpoint or HALT. |
| Current live exact duplicate | Preserve the current-tree decision path; history is supplemental and grants no reopening. |
| Current search has no clue but history has one bounded root | Root appears in the root-first display and is read before novelty is judged. |
| Unreachable, pruned, rewritten, unfetched, or never-committed work | No completeness claim; report outside the tested reachable corpus. |
| Any attempted indexer, watcher, ref, worktree, archive, board, or repository write during receipt construction | Test failure. |

Additional PASS gates are:

- the current-tree, synonym, hybrid-query, board, and current-log checks still run
  before the receipt;
- exact command receipts prove that only read-only Git and repository-query paths
  ran during discovery;
- path, byte, event, body-read, elapsed-time, and context counters cannot be
  bypassed by malformed input;
- the displayed root count equals the complete receipt's root count, and every
  displayed terminal or decision reference resolves to preserved bytes;
- source cleanup touches only task-owned scratch and is verified;
- written skill bytes are ASCII, links resolve, and the final diff contains only
  the authorized ideation skill; and
- no test or report calls the receipt an archive, complete history, semantic
  duplicate detector, approval record, or implementation authority.

### Worst failure, costs, and residual uncertainty

The worst plausible failure is a partial or mis-grouped receipt being presented
as complete, causing an agent to declare a genuinely repeated idea novel, reopen
closed work, or treat READY as approval. Prevention is fail-closed at every
identity, object, metadata, decision, and resource boundary; root-first display
must agree with the complete scratch receipt; full bodies and exact decision
events precede disposition; and every absence claim names the exact revision,
paths, and ceilings.[1][4][5]

A second failure is context displacement: a correct but large history manifest
can consume the session and reduce semantic review quality. The 16 KiB display,
25-root limit, 20-body limit, and scratch drill-down separate the compact view
from the complete receipt. Brain evidence supports bounded views and durable
provenance, but does not validate these exact ceilings.[6][7]

Costs are one additional fresh query, bounded Git traversal, scratch bytes,
historical-schema handling, up to 20 full-body reads, and extra failure modes in
the ideation gate. Review time was not measured. The proposed 60-second and size
ceilings are design assumptions; future evidence may show that they are too high
to be economical or too low to admit ordinary histories. The sample remains five
pipelines from one repository history.[1]

Residual uncertainty remains for merge-heavy histories, object pruning, rewritten
refs, many archive files, evolving schemas, and future artifact volumes. Atomic
repository immutability during all reads is not claimed. The session transaction
must recheck HEAD and worktree before writing; if they change, the receipt is
stale and the invocation halts rather than rebasing its conclusion.[4]

### Reversal and confidence

Rollback is direct: delete the inserted reachable-history subsection from
`governance/skills/forge-ideate/SKILL.md` and restore the existing live-tree,
current-log, and Brain checks. No receipt, index, archive, ref, status migration,
or external cleanup is required because the design creates no durable production
state.

Confidence is medium. Confidence is high in the frozen object counts, identity
result, five alias groups, and two decision changes because the embedded research
instrument and an independent evaluator traversal agree.[1] Overall confidence
remains medium because the sample is one repository history, the historical
index snapshot and review timing are unavailable, future reachability can change,
the concise display is untested, and the proposed ceilings are design choices.
Confidence would rise after an independent cold implementation reproduces every
real and synthetic acceptance row and a later reset case changes a novelty
judgment without a false merge. It would fall if clue-led targeted history
produces the same decisions more cheaply, a normal history exceeds the bounds, a
human decision is missed, or reviewers cannot use the root-first view without
opening most of the receipt.

## Sources

1. `forge/ideas/forge-history-duplicate-receipt-r01.md` -- root question,
   frozen baseline, affirmative thresholds, alternatives, and no-durable-state
   boundary. [high]
   - `forge/research/forge-history-duplicate-receipt-r01.md` -- exact runnable
     receipt, 39-path manifest, 34-ID grouping, five roots, decision table,
     timings, alternatives, costs, and reachability limits. [high]
   - `forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md` --
     independent reproduction, ADVANCE verdict, contrary evidence, and ten
     binding proposal obligations. [high]
2. `governance/skills/forge-ideate/SKILL.md` -- exact proposed target and current
   live-tree, overlap, log, Brain, full-read, and novelty procedure. [high]
3. `forge-index/README.md` -- live-repository hybrid corpus, file-level retrieval
   interface, watcher ownership, and current-path requirement. [high]
4. `forge/protocol.md` -- exact decisions, READY and human-review boundaries,
   reachable-link rules, checkpoints, transaction rechecks, stage scope, and
   no-implementation authority. [high]
5. `LEARNINGS.md` -- high-confidence evidence-preservation and result-contract
   controls, plus the low-confidence separation of historical identity from
   path, commit, and blob provenance. [high]
6. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- revision-specific provenance,
   bounded context, drill-down evidence, current-state rereading, diff scope,
   and revision-specific handoff. [medium]
7. `agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md` -- authoritative history versus
   current projections, exact receipts, truthful unknown outcomes, finite
   recovery budgets, and current-world rereading. [medium]
8. Git project. "git-log Documentation," undated; accessed 2026-09-30,
   Description and History Simplification sections. Reachable parent traversal,
   supplied revisions, path limiting, and `--full-history` were checked.
   https://git-scm.com/docs/git-log [high]
9. Git project. "git-rev-list Documentation," undated; accessed 2026-09-30,
   Description and examples. Supplied-revision set semantics and reachable
   object traversal were checked.
   https://git-scm.com/docs/git-rev-list [high]
10. Git project. "git-show Documentation," undated; accessed 2026-09-30,
    Description and examples. Historical blob retrieval with
    `<commit>:<path>` was checked.
    https://git-scm.com/docs/git-show [high]
11. Git project. "git-ls-tree Documentation," undated; accessed 2026-09-30,
    Description, `-r`, `--name-only`, and tree-ish interface. Exact frozen-tree
    enumeration was checked.
    https://git-scm.com/docs/git-ls-tree [high]
