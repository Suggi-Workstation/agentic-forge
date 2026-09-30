---
name: forge-proposal-claim-verification-map-evaluation
id: 20260930T213528Z
tier: evaluation
pipeline: 20260930T173859Z
author: Analyst
tags: [agent-systems, forge, evaluation, verification]
links:
  - forge/research/forge-proposal-claim-verification-map-r02.md
  - forge/ideas/forge-proposal-claim-verification-map-r01.md
  - forge/research/forge-proposal-claim-verification-map-r01.md
  - forge/evaluations/forge-proposal-claim-verification-map-evaluation-r01.md
  - governance/template-proposal.md
  - governance/skills/forge-propose/SKILL.md
  - forge/proposals/forge-history-duplicate-receipt-r01.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r01.md
  - forge/proposals/forge-history-duplicate-receipt-r02.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r02.md
  - forge/proposals/bounded-index-freshness-recheck-r02.md
  - forge/final-reviews/bounded-index-freshness-recheck-review-r02.md
  - LEARNINGS.md
  - forge/protocol.md
  - STATUS.md
  - logbook/progress.log
  - logbook/errors.log
  - agentic-brain:library/communication/source-verification-and-fact-checking.md
  - agentic-brain:reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md
  - agentic-brain:library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md
  - agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md
  - agentic-brain:library/science/measurement-and-metrology.md
  - https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix
  - https://www.nasa.gov/reference/5-3-product-verification
confidence: high
---
# Evaluation: Forge Proposal Claim-to-Verification Map R02

## Target and Baseline

Target: `forge/research/forge-proposal-claim-verification-map-r02.md`, ID
`20260930T201801Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the research drafting session's
private reasoning. Target-author independence therefore passes.[1][8]

At starting HEAD `21c34bb060dcc79332d716167943dbdaed84ea77`, the worktree was
clean. The board contained one valid unselected human-review row for pipeline
`20260930T083956Z` and one valid selected row for pipeline
`20260930T173859Z`, stage `evaluate`, with the exact target above. Progress
ended at ENT-021 and errors at ENT-027. The prior evaluation returned REVISE,
so corrective cycle 1 of 2 was already used; no REFRAME or human budget
extension exists for this pipeline.[2][8]

Before opening the r02 body, the expected evidence and failure conditions were
recorded in task-owned evaluator scratch. Expected evidence was:

- exact instrument and semantic-checklist rule bytes, with verified hashes and
  a clear pre-answer-key boundary;
- distinct reader records for both methods on both negative proposals and the
  READY control;
- independent claim extraction, with omissions, grouping, unsupported blocker
  rows, unclassified claims, and disagreements retained rather than reconciled
  away;
- like-for-like application of the current checklist's full semantic contract,
  not an item-presence surrogate;
- per-method and per-reader record size, elapsed time, detections, false
  blockers, and unresolved comparison limits; and
- decision evidence that a mandatory map adds unique, proportionate value over
  the semantic checklist, or an honest negative result that stops or narrowly
  reframes the idea.[2][3][5]

Failure conditions included unavailable bytes behind a hash, merged reader
summaries, unequal method conditions, unsupported blocker labels, a
non-reproducible complete-inventory claim, no incremental or complementary
value at a proportionate burden, or a prospective-benefit claim from
retrospective cases. A complete-looking table or aggregate score could not
overrule a material failure condition.

## Findings

### The revised evidence package is independently checkable

The target embeds the complete 607-word comparison instrument and eight
separate JSON records for Reader A and Reader B. Independent extraction parsed
all nine fenced records. The instrument hash matches its exact bytes without
the fence-closing newline, and every declared JSON hash matches the embedded
record bytes on the same explicit boundary. Independent file hashing also
matched the recorded template, three proposal, and three final-review hashes.
No hash substitutes for unavailable bytes in this revision.[1][3][4]

The preserved records reproduce the reported method totals. Reader A produced
60 map rows and 24 checklist rows; Reader B produced 79 map rows and 24
checklist rows. Reader A's method intervals were 178 seconds for the map and 10
seconds for the checklist. Reader B's were 175 seconds for the checklist and
271 seconds for the map. Those intervals are order-confounded and do not
measure authoring cost, as the target states.[1]

This closes the prior preservation blocker. It makes the revised negative
result reviewable; it does not make either method complete or establish future
benefit.

### The full semantic checklist removes the claimed incremental detection benefit

Within each frozen reader pass, the map and checklist detected the same set of
disclosed blockers. Reader A found 4 of 6 with each method; Reader B found 5 of
6 with each method. Each reader had zero map-only and zero checklist-only
disclosed detections. The union across readers found all six, and neither
method produced a blocker on the READY control.[1]

This comparison is materially fairer than r01. The frozen checklist rule applies
all eight template items as semantic gates. In particular, C5 tests whether the
normative sequence can enforce every material behavior, resource bound,
operation order, external-state limit, and no-side-effect claim; C6 tests
whether acceptance and negative evidence observe those claims and prohibited
later actions. That reading matches the current template's feasibility,
implementation-detail, acceptance, regression, negative, worst-case, and
reversal contract.[1][3]

The corrected evidence therefore withdraws the r01 claim that the map added a
6-of-6 versus 0-of-6 detection advantage. The root idea required incremental
value over an explicit reading of the current checklist and named no added
detection as a stop condition. That support condition fails.[2]

### Independent extraction remains divergent and both methods overreach

The two readers extracted 60 and 79 map rows from the same three proposals.
Only three of the six disclosed blockers were detected by both readers. Reader
A missed the r02 in-process-deadline and partial-clone blockers; Reader B missed
the r02 command-trace blocker. The map did not make complete claim extraction
operationally reproducible.[1][5]

The disagreement is not limited to omissions. Reader A produced three map
blocker rows unsupported by the paired reviews; Reader B produced two. The
post-review records also identify six unsupported defect components embedded
inside Reader A's otherwise supported checklist FAIL rows and two inside Reader
B's. No complete checklist FAIL row was unsupported, but the broad C5/C6 rows
bundled supported and unsupported components. The map localizes those
components more precisely, while neither method turns one same-family reader
into a complete or error-free detector.[1][4]

This matters to the proposed gate. A mandatory complete map would preserve more
reasoning detail, but the same extraction judgment that created 60 versus 79
rows also created complementary misses and unsupported blockers. Source-
verification and observability prior work supports explicit evidence ledgers
and warns that a record proves only the operations and distinctions it actually
captures; it does not convert a detailed record into a correct verdict.[6]

### The map's added record burden is not matched by demonstrated decision value

The map preserved 5,715 and 6,423 words, compared with 756 and 689 words for the
checklist records. Its 60 and 79 rows provide finer source ranges, operation
order, predicates, controls, evidence state, and classes than the checklist's
fixed 24 rows. That is an auditable-record benefit, not an incremental detection
benefit.[1]

The experiment did not measure whether this granularity reduces final-review
time, improves corrections, prevents future omissions, or lowers total review
cost. It used two same-model-family readers, two negative revisions from one
pipeline, one READY procedural control, disclosed answer keys, and
counterbalanced but carryover-prone order. No evidence estimates false-blocker
rates on other proposal classes or causal effects on authors.[1]

NASA verification practice and Brain systems-engineering work support unique
requirement identity, traceability, acceptance evidence, and preserved results.
They also support tailoring evidence to consequence and decision need. Those
sources justify a map when its additional structure is fit for purpose; they do
not justify a mandatory Forge map after an equally explicit semantic checklist
found the same disclosed defects at much smaller record size.[6][7]

### The narrower alternatives are untested, not a basis for another correction

A map limited to hard resource bounds, required operation order, prohibited
actions, and no-side-effect claims is plausible because those categories contain
all six disclosed blockers. The current experiment did not freeze or test that
instrument. Nor did it test a procedural clarification that makes checklist C5
and C6 execution more explicit.[1]

Those alternatives do not repair the current hypothesis from the available
record. The complete map added no disclosed detection, produced divergent
inventories and unsupported blockers, and imposed substantially larger records.
Using the remaining correction cycle to assume that an untested subset will add
value would replace the tested question rather than answer its failed support
condition. New evidence may justify a later bounded question; it does not
justify advancement now.

## Verdict and Handoff

**Verdict: REJECT. Graveyard closure; there is no next stage. Corrective cycle 1
of 2 had been used, and this terminal verdict consumes no additional corrective
cycle.**

The research successfully produces a decisive negative result. Its repaired
records show that the proposed complete claim-to-verification map adds finer
localization but no disclosed blocker detection over the current checklist when
that checklist is applied as its full semantic contract. Independent map
inventories diverge, both readers miss material blockers, unsupported findings
remain, and the larger record has no measured prospective or reviewer benefit.
The root idea's incremental-value and reproducibility thresholds are therefore
not met.[1][2][3]

The selected pipeline closes. Remove only pipeline `20260930T173859Z` from
`STATUS.md`; preserve the unrelated human-review row. No proposal, discovery,
implementation, template change, or skill change is authorized.[8]

Reopening requires changed evidence: a predeclared, proportionate narrow map or
other procedure must show unique decision-relevant detection or lower total
review cost against an equally explicit semantic-checklist baseline, with
independent readers, preserved outputs, controlled false blockers, and evidence
outside these two revisions of one pipeline. A new label for the current map is
not a reopening condition.

Confidence in REJECT is high for the tested complete-map hypothesis. Exact
instrument and reader bytes, verified hashes, full-contract baseline outputs,
two counterbalanced reader passes, exact source proposals and reviews, and the
root idea's predeclared stop condition agree.[1][2][3][4] Confidence is not a
claim that every narrow map lacks value. It would fall if independent
prospective evidence showed a proportionate map finding decision-relevant
blockers that an equally explicit checklist repeatedly missed or showed lower
total review cost without new false blockers.

## Learning Decision

`LEARNINGS.md` remains unchanged.[5]

- **Selection:** A full semantic baseline before the first comparison would have
  exposed earlier that the original 6-of-6 versus 0-of-6 result tested item
  presence rather than the current checklist contract. The root idea's stop
  condition then correctly prevented a mandatory map from advancing.
- **Evidence and test design:** Exact bytes, unmerged reader records, independent
  extraction, order balancing, and full-contract comparator outputs made the
  negative result checkable. Same-family readers, one negative pipeline, one
  control, and order carryover still bound the result.
- **Process:** The r01 evaluation identified the comparator defect and the r02
  research corrected it. No new handoff, template, or tool defect changed this
  verdict.
- **Repetition:** This pipeline applies the existing lesson to preserve every
  comparator's complete stated contract. The corrected baseline reverses the
  apparent incremental benefit, but it remains evidence from the same pipeline
  already named in that lesson.
- **Coverage:** The existing high-confidence lesson already requires exact
  instruments, separate raw outputs, and each comparator's full contract. A new
  lesson or confidence change would duplicate that rule and overcount one
  pipeline. No learning edit passes the separate admission gate; no additional
  structural gate is warranted.

## Sources

1. `forge/research/forge-proposal-claim-verification-map-r02.md` -- exact target,
   frozen instrument, embedded reader and post-review records, hashes, method
   counts, corrected comparison, alternatives, limits, and confidence. [high]
2. `forge/ideas/forge-proposal-claim-verification-map-r01.md` -- root question,
   affirmative thresholds, stop conditions, alternatives, and proportionality
   requirement. [high]
   - `forge/research/forge-proposal-claim-verification-map-r01.md` -- original
     map records, item-presence comparator, 6-of-6 versus 0-of-6 claim, and
     missing preservation evidence. [high]
   - `forge/evaluations/forge-proposal-claim-verification-map-evaluation-r01.md`
     -- REVISE verdict, cold baseline, full-contract comparator blocker, four
     correction requirements, and cycle count. [high]
3. `governance/template-proposal.md` -- current semantic feasibility,
   implementation-detail, acceptance, regression, negative, worst-case,
   reversal, and future-work gates. [high]
   - `governance/skills/forge-propose/SKILL.md` -- current implementable-scope,
     evidence-gap, response, and proposal-handoff procedure. [high]
4. `forge/proposals/forge-history-duplicate-receipt-r01.md` -- first negative
   target and exact normative, resource, acceptance, and rollback claims. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r01.md` -- exact
     body-before-byte and running-command-deadline answer key. [high]
   - `forge/proposals/forge-history-duplicate-receipt-r02.md` -- second negative
     target and corrected object, deadline, trace, clone, and acceptance claims.
     [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r02.md` -- exact
     emitted-byte, in-process-deadline, trace-coverage, and partial-clone answer
     key. [high]
   - `forge/proposals/bounded-index-freshness-recheck-r02.md` -- READY control,
     trigger, state, cleanup, acceptance, rollback, and future-evidence contract.
     [high]
   - `forge/final-reviews/bounded-index-freshness-recheck-review-r02.md` -- READY
     verdict, implementation-conformance interpretation, and retained limits.
     [high]
5. `LEARNINGS.md` -- exact-instrument, raw-output, separate-reader, full-contract
   comparator, claimed-result, and learning-admission rules. [high]
6. `agentic-brain:library/communication/source-verification-and-fact-checking.md`
   -- claim decomposition, evidence ledgers, independent review, and conclusion-
   to-evidence matching. [medium]
   - `agentic-brain:reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md`
     -- complete semantic execution rather than checklist presence. [medium]
   - `agentic-brain:library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md`
     -- requirements traceability, verification evidence, and proportional
     tailoring. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md`
     -- instrumentation coverage, trace limits, and separate outcome, process,
     and operational evidence. [medium]
   - `agentic-brain:library/science/measurement-and-metrology.md` -- named
     repeatability and reproducibility conditions, independent error mechanisms,
     and fitness-for-purpose limits. [medium]
7. National Aeronautics and Space Administration. "Appendix D: Requirements
   Verification Matrix," publication date not shown in the retrieved passage;
   accessed 2026-09-30. Unique mandatory-requirement identity, source, and
   verification approach were checked.
   https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix
   [high]
   - National Aeronautics and Space Administration. "5.3 Product Verification,"
     publication date not shown in the retrieved passage; accessed 2026-09-30,
     sections 5.3.1.1 through 5.3.1.3. Per-requirement acceptance criteria,
     recorded methods and results, objective evidence, bidirectional
     traceability, and tailoring were checked.
     https://www.nasa.gov/reference/5-3-product-verification [high]
8. `forge/protocol.md` -- review independence, correction budget, REJECT
   closure, artifact contract, source format, board selection, transaction, and
   no-implementation scope. [high]
   - `STATUS.md` -- selected evaluate row and preserved human-review row at
     starting HEAD `21c34bb060dcc79332d716167943dbdaed84ea77`. [high]
   - `logbook/progress.log` -- pipeline handoffs through ENT-021 at the same
     starting HEAD. [high]
   - `logbook/errors.log` -- recorded failures through ENT-027 at the same
     starting HEAD. [high]
