---
name: forge-history-duplicate-receipt-evaluation
id: 20260930T144144Z
tier: evaluation
pipeline: 20260930T124036Z
author: Analyst
tags: [agent-systems, forge, retrieval, evaluation]
links:
  - forge/research/forge-history-duplicate-receipt-r01.md
  - forge/ideas/forge-history-duplicate-receipt-r01.md
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
confidence: medium
---
# Evaluation: Forge History Duplicate Receipt

## Target and Baseline

Target: `forge/research/forge-history-duplicate-receipt-r01.md`, ID
`20260930T132200Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the research drafting session's
private reasoning. The independence requirement therefore passes.[1][3]

At starting HEAD `7c491b31c20604c49ef19fc1a80f141c9ab9cda3`, the worktree was
clean. The board contained one valid unselected human-review row and one valid
selected row: pipeline `20260930T124036Z`, stage `evaluate`, with the exact
target above. `progress.log` ended at ENT-010 and `errors.log` ended at ENT-012.
No prior evaluation, `REVISE`, `REFRAME`, or human budget extension exists for
this pipeline, so 0 of 2 corrective cycles were used.[3]

Before reading the target body, the following expected evidence and failure
conditions were recorded in evaluator scratch.

Expected evidence was:

- a frozen, non-shallow repository revision, explicit revision or ref boundary,
  current tree, board, active and archived logs, and current query procedure;
- a read-only reproducible receipt recovering all five reachable roots and all
  39 reachable tier paths, with exact containing commits, blobs, artifact IDs,
  tiers, pipelines, commands, and results;
- a fair current-tree baseline and receipt treatment using frozen prompts and
  grading fields, without treating the current index as historical semantic
  recall evidence;
- exact root and decisive-artifact reads that distinguish current, closed,
  pending, requested reframe, and unknown states without converting READY into
  approval or missing decisions into closure;
- stable identity grouping that exposes path aliases without counting them as
  independent artifacts or merging different pipelines;
- at least one supported novelty or reopening decision changed by exact
  historical evidence;
- bounded retrieval output, elapsed time, body-review count, alternatives, and
  explicit review-cost limits; and
- no archive guarantee, second board, restored artifact, history-aware index,
  repository recovery, or implementation authority.

Failure conditions were an unreproducible package, a missed reachable root or
path, lost current path, inferred disposition, cross-pipeline merge, unbounded
path or revision noise, no supported decision delta, or a result whose value
required durable competing state or completeness beyond supplied revisions.
The review would also block advancement if the baseline already recovered every
relevant root and exact decision, or if the observed review burden erased the
incremental value.[1][2]

## Findings

### The exact receipt and its identity boundary reproduce

The target embeds its complete ASCII receipt instrument. Evaluator extraction
matched the reported SHA-256
`29cc2da6d5b3f18fc99a8c2623fef6ca67d7e40d3cefee169954deb57afcdfaa`.
Executing those exact bytes against frozen revision
`d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06` returned the same 39 rows and:

```text
SUMMARY current=8 paths=39 ids=34 roots=5
```

A separate evaluator-written verifier traversed the revision again, recomputed
every Git blob ID from its bytes, parsed required metadata, and grouped artifact
IDs independently of path. It returned 91 reachable commits, `shallow: false`,
eight current paths, 39 reachable paths, 31 historical-only paths, 34 logical
IDs, five roots, 693,114 artifact bytes, zero errors, and zero cross-pipeline ID
conflicts. Git's documented semantics support the bounded interpretation:
`git log` traverses commits reachable through parent links, `--full-history`
changes path-history simplification, `git show <commit>:<path>` returns the
named object contents, and `git ls-tree -r --name-only` enumerates one tree.[11]
[12][13][14]

The five duplicate-ID groups also reproduced exactly: three unattended-command
reviews appeared once under `forge/evaluations/` and once under
`forge/final-reviews/`, while the bounded-freshness proposal and review each
appeared under two revision-number paths. Every group remained inside one
pipeline. The evidence therefore supports the target's central identity result:
path and containing commit are provenance, while pipeline plus artifact ID is
the stable logical identity for this corpus.[1]

This finding blocks a path-only procedure but does not block the idea. A proposal
can require both stable grouping and retained path aliases. It must not collapse
paths before preserving the commit and blob that make the historical body
auditable.

### The baseline comparison is useful but narrower than historical search quality

The target correctly states that the exact index snapshot at the frozen revision
was unavailable. It queried the transaction-time current index, restricted
results to frozen-tree paths, and excluded the selected idea. That design checks
the live-corpus boundary and candidate clues; it does not reconstruct historical
ranking or estimate semantic recall.[1] Current Forge-index documentation and a
fresh query confirm that the index searches the live repository corpus, while
the current bounded-freshness files show that deletion from the live corpus is
expected behavior rather than an index defect.[8]

The frozen current tree was not blind to all prior work. It supplied one exact
root and clues for three deleted roots through the bounded-freshness idea. It
supplied neither a maintenance-capex clue nor the exact terminal SBC verdict.
The target therefore reports one of five exact root IDs and four of five clues,
not zero historical awareness.[1][8] That qualification matters: clue-led
`git log` and `git show` remain a cheaper alternative when a precise clue exists.

The missing historical index snapshot prevents claims about ranking quality or a
history-aware semantic index. It does not defeat the demonstrated corpus gap:
current-corpus search cannot return a deleted body as an indexed file. Nor does
it defeat the decision comparison, which is grounded in exact Git objects rather
than an inferred search miss. This limitation is non-blocking for a proposal
limited to a scratch-only root-first receipt.

### Exact historical bodies change two bounded decisions without inventing state

Independent inspection of the exact historical roots and terminal artifacts
confirmed the five classifications.

- Maintenance capex had no frozen-tree clue. Its r02 evaluation returned
  `REFRAME`, consumed corrective cycle 2 of 2, required same-pipeline ideation,
  and granted no proposal authority. The exact body changes a plausible new-idea
  decision into an exhausted-budget same-pipeline question.[4]
- SBC buyback had a live clue but no exact terminal record. Its graveyard r02
  evaluation returned `REJECT`, removed the row, and required changed evidence
  and a human budget before reopening. The exact body changes unknown disposition
  into a closed pipeline on unchanged evidence.[5]
- The transaction-checker graveyard r03 evaluation returned `DEFER` after two
  prior `REVISE` verdicts and required a human extension, corrected real-record
  controls, and comparative value. This confirms the safe baseline rather than
  changing it.[6]
- The unattended-command r03 review returned READY for exact proposal
  `20260930T060651Z`, not approval. An evaluator traversal found 42 commits that
  touched `progress.log`, 41 unique log blobs, and nine unique events for that
  pipeline. The only apparent decision-like block was the READY event stating
  that the exact proposal awaited Suggi; no explicit human disposition appeared.
  `unknown` is therefore the supported decision state.[7]
- The bounded-freshness root and discovery were live and remain
  `awaiting-review` / `human-review`; this is the positive current-corpus
  control.[8]

These checks support more than path recovery. At least two actionable judgments
change: do not create a renamed maintenance-capex pipeline, and do not reopen the
rejected SBC pipeline on unchanged evidence. The treatment also preserves a
material unknown rather than manufacturing closure. This satisfies the root
idea's decision-value threshold and supports proposal work.[1][2]

The historical artifacts and progress events are nevertheless dependent records
from the same Forge runs. Git object checks establish exact recovery, not the
truth of every substantive claim inside the recovered reports. Their proper use
here is narrower: they are authoritative evidence of recorded Forge pipeline
state under the protocol.[3][9]

### Review burden, contrary evidence, and alternatives remain material

The target reports a complete receipt of 78,758 bytes, five query outputs of
22,208 bytes, one-host retrieval time of 2.851947649 seconds, ten minimum root
and decisive-artifact reads, and one additional proposal read for exact READY
target verification.[1] The evaluator reproduced the manifest counts but did
not treat the one timing run as a service bound. More importantly, candidate
review time was not measured. Ten or eleven full bodies are a real context and
human-review cost even when retrieval itself is subsecond.

Contrary evidence therefore limits the recommendation:

- three deleted roots already had live clues, so targeted history is smaller for
  those candidates;
- five pipelines from one repository history do not estimate future duplicate
  frequency, path growth, false-merge rate, or review economics;
- current `HEAD`, all local and remote refs, and an explicitly frozen revision
  define different reachable populations;
- old tier names, copied paths, reset logs, ENT renumbering, missing objects,
  rewritten history, and shallow clones need explicit fail-closed treatment;
- a concise display was not executed, so the full 39-path manifest has not shown
  that it improves review rather than flooding context; and
- doing nothing remains credible if resets are exceptional and a live clue is
  normally available.[1][2]

Brain prior work independently supports the method boundary. Repository search
should preserve path and revision provenance, durable records should remain
separate from current projections, and digital collection absence must be
bounded by selection and retrieval limits.[9] Those principles support a
root-first drill-down receipt; they do not prove that every Forge ideation needs
one.

No blocker requires another research cycle. The evidence establishes a real
current-corpus blind spot, exact bounded recovery, stable identity handling, and
decision value. The unresolved population, display, cost, and stop-policy issues
are design obligations that a proposal can answer and expose to final review.

## Verdict and Handoff

**Verdict: ADVANCE. Exact next stage: `propose`. No corrective cycle is used;
0 of 2 remain used.**

ADVANCE means that a bounded proposal is justified, not that a history receipt
is approved, implemented, or required in every ideation session.[3]

The proposal must:

1. Name the exact current target in
   `governance/skills/forge-ideate/SKILL.md` and propose only a short prior-work
   retrieval procedure or linked reference. It must not create another board,
   archive, index, manifest in the repository, restored artifact, ref, or runtime
   component.
2. Define the revision or ref set that bounds reachability, verify the clone is
   not shallow, and label every negative result as absence only from that tested
   reachable corpus. Missing, pruned, unfetched, rewritten, or never-committed
   history remains unknown.
3. Produce a root-first contextual display and retain the complete receipt only
   in task-owned scratch for drill-down. The display should surface pipeline,
   root ID/path, candidate terminal artifact, recorded disposition evidence, and
   ambiguity before listing every descendant path.
4. Group logical artifacts by pipeline plus artifact ID. Retain every path,
   containing commit, blob, tier, and historical schema value as provenance;
   never count aliases as independent evidence or normalize historical metadata
   silently.
5. Require full reading of each candidate root and exact decisive artifact before
   a novelty, reopening, closure, or approval judgment. Deduplicate copied or
   renumbered log events, preserve READY as nonapproval, and return `unknown`
   when no exact human decision exists.
6. Define path, byte, body-read, elapsed-time, and context limits. On overflow,
   missing objects, ambiguous identity, cross-pipeline ID collision, malformed
   metadata, or unreadable decisive evidence, checkpoint or HALT rather than
   truncate into false completeness.
7. Preserve current-tree enumeration and hybrid search. The history receipt is a
   supplement for deleted-body discovery, not a replacement for current-state
   retrieval or semantic duplicate judgment.
8. Include an executable acceptance package. At minimum it must reproduce, at
   frozen revision `d6137e3`, eight current paths, 39 reachable paths, 34 logical
   IDs, five roots, five alias groups, zero cross-pipeline conflicts, the
   maintenance and SBC decision deltas, the unattended unknown state, and the
   bounded-freshness current control. It must also test shallow or missing-object
   failure, same-ID cross-pipeline conflict, path copies, old tier names, reset or
   renumbered logs, READY without a human decision, and a receipt that exceeds
   its declared budget.
9. Compare doing nothing and clue-led targeted history as live alternatives.
   State that prospective duplicate frequency, review time, net benefit, and
   behavior after another reset are unknown. Do not turn the one-host retrieval
   timing into an operating guarantee.
10. Keep implementation, skill amendment, deployment, and any durable retention
    separately authorized. Rollback must be deletion of the proposed procedure,
    with no repository or index migration.

Confidence in ADVANCE is medium. Confidence is high in the frozen-revision
counts, exact-object recovery, alias groups, and two decision deltas because the
embedded instrument and an independent evaluator traversal agree.[1][4][5]
Overall confidence remains medium because the baseline lacks its exact historical
index snapshot, the sample is five pipelines from one history, review time was
not measured, the concise display is untested, and future ref reachability can
change. Confidence would rise after an independent cold run on a later reset and
a bounded root-first display changes a real novelty decision without a false
merge. It would fall if clue-led targeted history recovers the same decisions at
lower cost, a common history shape escapes traversal, or the proposed limits
hide a relevant pipeline.

## Learning Decision

Add one low-confidence method lesson to `LEARNINGS.md`: separate historical
artifact identity from path provenance.[10]

- **Selection:** The current-tree versus reachable-history count and one root
  with no live clue showed before deep review that the question could change a
  novelty decision.
- **Evidence and test design:** Exact executable bytes, the inline 39-row output,
  object-level verification, and stable ID grouping made recovery and rename
  noise decisive. The unavailable historical index snapshot correctly limited
  the semantic-search claim.
- **Process:** The research's invalid wildcard `git ls-tree` baseline showed that
  plausible path commands need an executed positive control. The corrected
  directory pathspec and independent object traversal prevented that failure
  from entering the result. Existing package-preservation and claimed-contract
  lessons cover execution evidence, but not historical path identity or
  reachability wording.
- **Repetition:** This is one pipeline, so the lesson enters at low confidence
  and is not a binding rule.
- **Coverage:** No current lesson states that renamed historical paths must be
  grouped by pipeline and artifact ID while commit/blob/path stay as provenance,
  or that absence must be bounded to supplied reachable revisions. The lesson is
  non-duplicative and grants no governance or implementation authority.

## Sources

1. `forge/research/forge-history-duplicate-receipt-r01.md` -- exact target,
   runnable instrument, frozen comparison, raw manifest, decision table,
   alternatives, costs, and limitations. [high]
2. `forge/ideas/forge-history-duplicate-receipt-r01.md` -- root question,
   affirmative thresholds, failure conditions, prior-work boundary, and
   excluded durable state. [high]
3. `forge/protocol.md` -- independence, artifact identity, dispositions,
   correction budget, board selection, transaction, and no-implementation
   boundary. [high]
   - `STATUS.md` -- selected evaluation row and preserved human-review row at
     starting HEAD `7c491b31c20604c49ef19fc1a80f141c9ab9cda3`. [high]
   - `logbook/progress.log` -- current pipeline handoffs through ENT-010 at the
     same starting HEAD. [high]
   - `logbook/errors.log` -- current failure record through ENT-012 at the same
     starting HEAD. [high]
4. `forge/ideas/auditable-maintenance-capex-r01.md` -- historical root question,
   verified at Git commit `88f20c05e07424240cde4d49df5ea1eb9b0e9094`.
   [high]
   - `forge/evaluations/auditable-maintenance-capex-evaluation-r02.md` -- exact
     REFRAME, exhausted ordinary correction budget, and no-proposal boundary,
     verified at commit `a88424a57f949a66996b6fb03d06c674087ec7c6`.
     [high]
5. `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- historical root question
   and explicit stop rule, verified at Git commit
   `b48b52a10ed6079e84d0555ef482667efdd377fe`. [high]
   - `forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md` -- exact
     REJECT closure and reopening conditions, verified at commit
     `fea117df0e15835239b22959a7fb5268423891cf`. [high]
6. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- historical
   root question, verified at Git commit
   `4bc2896bf5398e36dec2f4ec2ffc3791efaec554`. [high]
   - `forge/graveyard/evidence-gated-forge-transaction-checker-evaluation-r03.md`
     -- exact DEFER closure, false rejection, exhausted budget, and reopening
     conditions, verified at commit
     `ee82fca6dc9c6ab654ffb294152a5f12756ecb6c`. [high]
7. `forge/ideas/unattended-forge-command-paths-r01.md` -- historical root and
   bounded question, verified at Git commit
   `878347b85da2f911c8b475b549dbbf390e832c95`. [high]
   - `forge/proposals/unattended-forge-command-paths-r03.md` -- exact historical
     proposal, verified at commit
     `2224f529b5198a7e1a20c9d692f72f94ca146351`. [high]
   - `forge/final-reviews/unattended-forge-command-paths-review-r03.md` -- READY
     verdict, exact proposal ID, and no-approval boundary, verified at commit
     `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `logbook/progress.log` -- 42 reachable historical versions checked through
     frozen revision `d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06`;
     nine deduplicated pipeline events contain READY but no explicit human
     disposition. [high]
8. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- current-corpus control,
   historical clues, and distinct live-index question. [high]
   - `forge/discoveries/bounded-index-freshness-recheck-r02.md` -- exact pending
     discovery and no-implementation boundary. [high]
   - `forge-index/README.md` -- live-repository corpus, query interface, and
     current-corpus scope. [high]
9. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md`
   -- revision-specific provenance, bounded search, exact evidence packages, and
   context-cost limits. [medium]
   - `agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md`
     -- authoritative history, replaceable current projections, and truthful
     unknown states. [medium]
   - `agentic-brain:library/history/historiography-and-historical-method.md` --
     archive selection, provenance, digital-corpus boundaries, and negative-
     evidence limits. [medium]
10. `LEARNINGS.md` -- package-preservation and claimed-result-contract lessons,
    capture questions, and separate learning-admission gate. [high]
11. Git project. "git-log Documentation," undated; accessed 2026-09-30,
    Description, path limiting, and History Simplification sections. Reachable
    commit traversal and `--full-history` behavior were checked.
    https://git-scm.com/docs/git-log [high]
12. Git project. "git-rev-list Documentation," undated; accessed 2026-09-30,
    Description and commit-set semantics. Supplied-revision reachability was
    checked.
    https://git-scm.com/docs/git-rev-list [high]
13. Git project. "git-show Documentation," undated; accessed 2026-09-30,
    Description and examples. Exact historical blob retrieval with
    `<commit>:<path>` was checked.
    https://git-scm.com/docs/git-show [high]
14. Git project. "git-ls-tree Documentation," undated; accessed 2026-09-30,
    Description, `-r`, `--name-only`, and tree-ish semantics. Frozen-tree path
    enumeration was checked.
    https://git-scm.com/docs/git-ls-tree [high]
