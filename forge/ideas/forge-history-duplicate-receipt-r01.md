---
name: forge-history-duplicate-receipt
id: 20260930T124036Z
tier: idea
pipeline: 20260930T124036Z
author: Analyst
tags: [agent-systems, forge, retrieval, provenance]
links:
  - ANCHOR.md
  - forge/protocol.md
  - governance/skills/forge-ideate/SKILL.md
  - forge-index/README.md
  - forge/ideas/bounded-index-freshness-recheck-r01.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:research/insights/stale-index-problem.md
  - https://git-scm.com/docs/git-log
  - https://git-scm.com/docs/git-rev-list
confidence: low
---
# Forge History Duplicate Receipt

## Question and Value

Can one bounded, read-only history receipt during new ideation expose prior Forge
pipelines and exact disposition evidence that are reachable in Git but absent
from the current tree, so a reset-deleted question is not mistaken for new work,
without creating a second state board or changing the current-corpus index?

The target is the prior-work check in
`governance/skills/forge-ideate/SKILL.md`. Forge agents and Suggi benefit if a
novelty decision can distinguish current work, closed work, pending work, and an
unknown disposition after files leave the live tree. This is direct ANCHOR Path
A work on retrieval, shared-brain quality, and recurring workflow risk.[1]

The problem is observable at starting commit
`d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06`. Current tier directories contain
one root idea path and eight artifact Markdown paths. A read-only
`git log --all --full-history --name-only` traversal over the same tier pathspecs
names five root idea paths and 39 unique artifact paths. Four roots and 31 paths
are therefore reachable in repository history but absent from the current tree.
The clone reports `false` for `git rev-parse --is-shallow-repository`, so this is
not a shallow-clone artifact. These figures describe only objects reachable from
the refs inspected at that commit; they do not prove recovery of pruned,
unfetched, or rewritten history.[2][10][11]

The current Forge index is behaving correctly, not failing freshness. It indexes
the live repository corpus, and the shared index design intentionally removes a
deleted Markdown file from the manifest and query results after a natural
watcher transition.[4][9] The unresolved mismatch is between that correct
current-corpus behavior and ideation's broader requirement to check all open and
closed Forge work and exact proposal decisions.[2]

The provisional hypothesis, formed after the current-tree and Git-history
counts were compared, is that a scratch-only receipt containing each reachable
root pipeline, artifact path, containing commit, and exact decision-event
reference would make historical candidates visible before the novelty judgment.
A credible alternative is that the existing instruction plus targeted `git log`
and `git show` calls already suffice; a standard receipt may add noise, imply
false completeness, or cost more review than the rare reset case warrants.

The idea is not worth pursuing if the receipt cannot reconstruct dispositions
without inference, if current search already recovers every relevant historical
pipeline in a bounded comparison, if path and revision noise causes false
merges, or if no tested novelty decision changes. It is also not worth pursuing
if usefulness requires indexing Git history, restoring deleted artifacts to the
live tree, maintaining a second board, or treating reachable history as complete
history.

## Origin and Prior Work

This is direct ideation under ANCHOR Path A, Agent Systems. Discovery preceded
the blank-page explanation: the current board, active logs, every current Forge
artifact path, historical tier paths, and the reset diff were inspected before
the provisional hypothesis was stated. The candidate was then checked against
Forge, Brain, and primary Git documentation using `reset`, `history`, `deleted`,
`duplicate`, `prior proposal`, `decision`, `archive`, and `discoverability`
synonyms.

The current Forge protocol already owns the substantive rule: ideation checks
all open and closed work, proposal decisions, and relevant bodies before
claiming a distinct question.[2] This idea does not duplicate that rule or assume
a solution. It asks whether one bounded retrieval receipt makes the existing
rule reliably executable after a history-clearing commit.

The direct repository evidence is mixed:

- Commit `1221b88dec13f0934f06913ed83e012ac0b26d8b`, whose subject is
  `forge: fresh start -- clear artifacts, board and logs`, removed three then-
  current root ideas and their descendants from the live tree. An earlier
  maintenance-capex root is also reachable in history but not in that reset's
  parent tree.[5][7]
- The historical unattended-command pipeline reached a READY review for an
  exact r03 proposal, but its preserved progress log contains no explicit Suggi
  disposition before the reset. The proposal is therefore prior work with an
  unresolved recorded decision, not permission to recreate it under a new
  name.[5]
- The transaction-checker pipeline closed DEFER after exhausting its correction
  budget, and the SBC-buyback pipeline closed REJECT. The maintenance-capex
  pipeline received REFRAME before its files later left the live tree.[6][7]
  These cases require different duplicate outcomes; file existence alone cannot
  supply the disposition.
- The current bounded-index-freshness pipeline is pending human review in
  `STATUS.md`. Its question concerns one exact live-index HEAD-lag recheck, and
  its idea already used exact historical commits to avoid duplicating prior
  work.[3] It does not address systematic historical candidate discovery.

The current Forge hybrid query for the candidate problem returned live files,
including the current protocol and the bounded-freshness idea that cites old
work. It could not return the deleted artifact bodies as indexed files because
they are not in the current corpus.[3][4] This observation establishes a corpus
boundary, not a semantic recall rate and not a defect in the index.

Brain prior work supports the need for durable state but does not provide this
Forge method. Its coding-agent workflow treats Git history and append-only
records as recovery evidence after context loss, while requiring provenance and
revision-specific claims.[8] Its stale-index insight establishes that current-
corpus consistency includes removing deleted files from query results.[9]
Primary Git documentation establishes reachable-commit traversal, path-limited
history, and `--full-history`; it does not claim that path history alone performs
semantic duplicate detection or recovers unreachable objects.[10][11]

The strongest alternative candidate was a new study of repeated approval-blocked
scratch cleanup. It lost because the historical unattended-command proposal
already addresses authoritative denial results, route selection, and the
no-bypass boundary, reached READY, and has no explicit recorded human decision.[5]
The later cleanup incidents may be evidence relevant to that pending proposal,
but they do not justify a renamed pipeline. Reopening the transaction checker
also lost because its exact DEFER closure requires a human budget extension and
comparative evidence that do not exist.[6]

No accepted Forge proposal was found in the active or historical progress
records inspected. The current bounded-freshness discovery and the historical
unattended-command proposal are pending or lack an explicit disposition; neither
is implementation authority.[3][5]

## Research Plan

Use one bounded, read-only comparison at a frozen repository revision:

1. Freeze `HEAD`, refs, shallow-repository status, current tier paths, current
   `STATUS.md`, active and historical progress logs, the Forge index freshness
   result, and the exact current-tree duplicate-search procedure. Record any
   missing object, unreadable ref, or rewritten-history limit rather than
   treating absence as proof.
2. Define the truth set only as Forge root ideas and descendant artifact paths
   reachable from the frozen refs under the protocol's tier directories. Build a
   scratch receipt with read-only Git plumbing and porcelain commands. For each
   unique path, retain the exact containing commit used to read its body; for
   each root pipeline, retain artifact IDs and candidate decision-event
   references. Do not write an archive, index, board, tag, or repository file.
3. Compare two procedures on the five known root pipelines: (a) current-tree
   file enumeration, current hybrid query, and active/archive log search; and
   (b) the same procedure plus the history receipt. Use predeclared problem and
   synonym prompts derived from each root question. Grade exact root recovery,
   body availability, pipeline identity, correction state, and disposition as
   current, closed, pending, requested reframe, or unknown. A missing decision
   must remain unknown; READY must not be converted into approval.
4. Preserve every command, path, commit, classification, false merge, omission,
   and review correction before synthesis. Measure elapsed time, output size,
   and artifacts that require full reading. Compare with doing nothing, targeted
   Git history only when a clue exists, a current-tree tombstone manifest, and a
   history-aware index. The last two alternatives are comparison cases, not
   authorized implementation scope.
5. Test decision value with at least one predeclared candidate whose closest
   prior body is absent from the live tree. The receipt adds value only if it
   changes a supported novelty or reopening decision compared with the frozen
   current-tree baseline and the exact historical artifact justifies the change.
6. Stop without a proposal if current search already recovers every relevant
   root and exact disposition, if the receipt cannot separate unknown from
   closed work, if history traversal is materially noisier than targeted review,
   or if the method would imply completeness beyond reachable refs.

Research supports a proposal only if the receipt recovers all five reachable
root ideas and all 39 unique reachable tier paths at the frozen revision, maps
each tested pipeline to exact artifact and decision evidence without an inferred
approval or closure, and demonstrates at least one corrected novelty or reopening
decision over the current-tree baseline. Every current path must remain present,
and an intentionally missing or ambiguous decision must be reported as such.
The proposed change, if any, must remain a short ideation procedure or reference;
it must not create durable competing state, alter index semantics, or authorize
repository recovery.

Confidence is low. Exact Git traversal establishes a real difference between
the live corpus and reachable history, and historical artifacts show materially
different dispositions.[2][5][6][7] Confidence remains low because the receipt
has not been built, semantic recall and review cost are unmeasured, ref reachability
is not archival completeness, and the current procedure may already work when a
historical clue is known. Confidence would rise only after the frozen comparison
reproduces every path and decision boundary and changes a real duplicate
judgment without false completeness. It would fall if the added method produces
ambiguous mappings, high review burden, or no decision delta.

## Sources

1. `ANCHOR.md` -- Path A mission fit, recurring-failure prompt, selection
   criteria, smallest-test requirement, and duplicate/reopening boundary. [high]
2. `forge/protocol.md` -- all-work duplicate check, exact decision rules,
   current-board authority, source format, session transaction, and no second
   state cursor. [high]
   - `governance/skills/forge-ideate/SKILL.md` -- current enumeration, synonym
     search, body-read, historical-decision, and non-duplicate procedure. [high]
   - `governance/template-idea.md` -- required prior-work and strongest-
     alternative record. [high]
3. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- current example of
   exact-commit historical comparison, prior READY and DEFER checks, and the
   distinct live-index question. [high]
   - `STATUS.md` -- current bounded-freshness discovery awaiting exact human
     review at starting commit `d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06`.
     [high]
4. `forge-index/README.md` -- current-repository hybrid corpus, manifest target
   existence, freshness ownership, and query interface. [high]
5. `forge/ideas/unattended-forge-command-paths-r01.md` -- historical root,
   exact command-selection scope, and duplicate check, verified at Git commit
   `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `forge/proposals/unattended-forge-command-paths-r03.md` -- exact historical
     proposal and no-implementation boundary at the same commit. [high]
   - `forge/final-reviews/unattended-forge-command-paths-review-r03.md` -- READY
     verdict and human-review handoff at the same commit. [high]
   - `logbook/progress.log` -- historical ENT-007 through ENT-021 and no explicit
     Suggi disposition before reset at the same commit. [high]
6. `forge/graveyard/evidence-gated-forge-transaction-checker-evaluation-r03.md`
   -- exact DEFER closure, exhausted correction budget, current-record failure,
   and reopening conditions, verified at Git commit
   `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md` -- exact
     REJECT closure at the same commit. [high]
7. `forge/ideas/auditable-maintenance-capex-r01.md` -- earlier historical Path B
   root and its distinct estimation question, verified at Git commit
   `a88424a57f949a66996b6fb03d06c674087ec7c6`. [high]
   - `forge/evaluations/auditable-maintenance-capex-evaluation-r02.md` -- REFRAME
     verdict, exhausted ordinary correction budget, and required narrower
     question at the same commit. [high]
8. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md`
   -- revision-specific provenance, Git checkpoints, durable recovery state,
   and bounded repository search. [medium]
9. `agentic-brain:research/insights/stale-index-problem.md` -- current-corpus
   consistency, natural add/delete validation, and removal of deleted files from
   manifests and query results. [medium]
10. Git project. "git-log Documentation," undated; accessed 2026-09-30,
    Description, History Simplification, path limiting, and `--full-history`.
    Reachable commit and path traversal semantics were checked.
    https://git-scm.com/docs/git-log [high]
11. Git project. "git-rev-list Documentation," undated; accessed 2026-09-30,
    Description, Commit Limiting, History Simplification, and examples. Reachable
    set traversal and the limits of supplied refs were checked.
    https://git-scm.com/docs/git-rev-list [high]
