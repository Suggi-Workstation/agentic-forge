---
name: learnings
id: 20260812T171242Z
tier: control
author: Link
---
# LEARNINGS.md -- Agent Method Memory

Reusable lessons about how the Forge selects, researches, evaluates, and
proposes. Read this file at the start of ideation and before later work.
Only a completed `evaluate` or `final-review` stage may change it, whichever
authorized agent runs that stage; `ideate`, `research`, and `propose` keep it
read-only. Lessons are agent-written, not human-authored.

## Learning-Capture Questions

Ask these after every completed evaluation or final review. They are lenses,
not quotas: one lesson may answer several. If nothing was learned, say so in
the artifact's Learning Decision.

1. **Selection:** What would have shown earlier whether this idea was worth
   pursuing? Ask especially after REVISE, REFRAME, REJECT, or DEFER.
2. **Evidence and test design:** What made the evidence decisive or weak --
   data availability, source access, baseline comparison, or test design?
3. **Process:** Did a handoff, template, tool, or recurring `errors.log`
   failure cost time or cause a mistake?
4. **Repetition:** Did this pipeline repeat a failure an existing lesson
   covers? Then that lesson is inadequate or unapplied: strengthen or
   correct it.
5. **Coverage:** Is this already a lesson here or a rule in the protocol,
   templates, or skills? Update the existing entry instead of adding one.

## Admission Rules

- A lesson is a transferable method, not an idea's verdict. Domain findings
  stay in research and proposals; chronology stays in the logbook.
- One completed pipeline may admit a lesson at `low` confidence when its
  evidence is checked and its consequence is concrete. Use `medium` for two
  or more independent pipelines and `high` when a later pipeline shows that
  applying the lesson helped. Repeated accounts of one incident are not
  independent trials. Lower or retire a lesson that later evidence contradicts.
- A `low` lesson is a caution to consider, not a binding rule.
- Name the evidence pipeline IDs and artifact links. Keep entries short:
  lesson, evidence, confidence, and consequence.
- Prefer updating an existing lesson to adding a duplicate. Retire stale
  lessons with a reason; Git preserves prior wording.
- A lesson may improve future behavior but cannot authorize governance,
  runtime, profile, or external-repository changes. A confirmed lesson that
  should become a skill, template, or protocol rule is a Path A idea.

## Learning Admission Gate

Before changing a lesson, PASS requires the current `evaluate` or
`final-review` stage to be completed, checked evidence with confidence
matching its independent pipeline count, a non-duplicate method lesson, and
no implied governance or deployment permission. Otherwise HALT the learning
edit; keep the legitimate stage result and this file unchanged.

## Learnings

### Preserve procedural validation evidence before comparison

- **Lesson:** Preserve dated pre-comparison rules, the exact runnable instrument
  and fixtures, raw per-case outputs, and each reader's separate output before
  claiming a blind, reproducible, or passed procedural validation; hashes
  without available bytes do not make the run independently checkable.
- **Evidence:** In three earlier pipelines, reports claimed blind or
  reproducible tests but kept only summaries or hashes, so evaluators could
  not check them. A fourth pipeline preserved its complete fixtures, calls,
  and raw result bytes, and a separate evaluator used them to reproduce every
  claimed outcome.
- **Confidence:** High for runnable-package and raw-output preservation. Three
  independent pipelines exposed the failure, and a later pipeline showed that
  applying the lesson made its procedural result independently checkable. Blind
  timing and separate-reader claims still require their own preserved evidence.
- **Consequence:** Require linked pre-comparison rules, executable and fixture
  bytes, raw results, and unmerged reader outputs before treating a procedural
  validation claim as passed; otherwise limit the claim and return for evidence.

### Derive evaluator and checker controls from the claimed result contract

- **Lesson:** Derive every checker predicate, evaluator classifier, negative
  fixture, and positive control from each field, relationship, and purpose-level
  behavior the result claims. A run-level label cannot validate unclassified
  later decisions; label the result partial when any claimed predicate is
  intentionally excluded.
- **Evidence:** In one earlier pipeline, a record checker reproduced all its
  declared results while contradicted required fields still passed; after a
  fix, it reproduced all declared outcomes but rejected a valid real record
  shape. In another, an evaluation design froze matched control and treatment
  runs but graded only each run's first command choice, so a denied attempt
  later in the run could still pass the claim.
- **Confidence:** Medium. Two independent pipelines expose the same
  claimed-contract undercoverage in a checker and an evaluation grader.
- **Consequence:** Before proposing a deterministic checker or evaluation gate,
  map every claimed PASS or benefit clause to an observable predicate, a
  false-positive counterexample or negative fixture, and a valid positive
  control. Narrow the result claim whenever the grader deliberately omits one.
