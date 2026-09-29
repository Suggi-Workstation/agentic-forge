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
- **Evidence:** Pipelines `20260921T060750Z`, `20260921T114301Z`, and
  `20260921T152802Z`, in
  `forge/evaluations/auditable-maintenance-capex-evaluation-r02.md` at Git
  commit `a88424a57f949a66996b6fb03d06c674087ec7c6`,
  `forge/evaluations/auditable-sbc-buyback-bridge-evaluation-r01.md`, and
  `forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md`.
- **Confidence:** Medium. Three independent Forge pipelines expose evidence-
  preservation failures, but no later pipeline yet shows that applying the
  strengthened package prevents them.
- **Consequence:** Require linked pre-comparison rules, executable and fixture
  bytes, raw results, and unmerged reader outputs before treating a procedural
  validation claim as passed; otherwise limit the claim and return for evidence.
