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
  and fixtures, raw per-case outputs, and each reader's separate output for every
  compared method before claiming a blind, reproducible, or passed procedural
  validation; hashes without available bytes do not make the run independently
  checkable. Apply each baseline to its full stated contract rather than a
  presence-only surrogate.
- **Evidence:** In three earlier pipelines, reports claimed blind or reproducible
  tests but kept only summaries or hashes, so evaluators could not check them. A
  fourth pipeline preserved its complete fixtures, calls, and raw result bytes,
  and a separate evaluator used them to reproduce every claimed outcome. In
  pipeline `20260930T173859Z`, the displayed map could be checked against six
  disclosed defects, but the hashed instrument bytes, separate reader output,
  and semantic checklist baseline were not preserved as distinct records; the
  evaluation could not verify the reproduction or incremental 6/6-versus-0/6
  comparison. See
  `forge/evaluations/forge-proposal-claim-verification-map-evaluation-r01.md`.
- **Confidence:** High for runnable-package, raw-output, and full-contract
  comparator preservation. Four independent pipelines exposed the failure, and
  a separate later pipeline showed that applying the lesson made its procedural
  result independently checkable. Blind timing and separate-reader claims still
  require their own preserved evidence.
- **Consequence:** Require linked pre-comparison rules, executable and fixture
  bytes, raw results, and unmerged reader outputs for every treatment and
  baseline before treating a procedural comparison as passed. Apply each
  comparator to its complete stated contract and preserve per-target outputs;
  otherwise narrow the result and return for evidence.

### Derive evaluator and checker controls from the claimed result contract

- **Lesson:** Derive every checker predicate, evaluator classifier, negative
  fixture, positive control, and operation order from each field, relationship,
  resource bound, effective configuration source, inherited override, and
  purpose-level behavior the result claims. A run-level label cannot validate
  unclassified later decisions or a gate applied only after its prohibited
  action; label the result partial when any claimed predicate is intentionally
  excluded.
- **Evidence:** In one earlier pipeline, a record checker reproduced all its
  declared results while contradicted required fields still passed; after a
  fix, it reproduced all declared outcomes but rejected a valid real record
  shape. In another, an evaluation design froze matched control and treatment
  runs but graded only each run's first command choice, so a denied attempt
  later in the run could still pass the claim. In pipeline `20260930T083956Z`,
  a first replay let every `STALE` subtype wait despite an exact-HEAD-lag claim;
  after the trigger and action clauses were mapped to controls, an independent
  rerun reproduced all 22 corrected expectations. In pipeline
  `20260930T124036Z`, a proposal probed a blob body before its declared size gate
  and named an elapsed ceiling without a running-command deadline predicate;
  final review returned REVISE before either bound was treated as testable. A
  later review in the same pipeline found that a local-only clone guard omitted
  command-scope Git configuration: a disposable fixture supplied a promisor key
  through `GIT_CONFIG_*`, after which the guarded object call spawned a fetch and
  added object-database files. See
  `forge/final-reviews/forge-history-duplicate-receipt-review-r01.md` and
  `forge/graveyard/forge-history-duplicate-receipt-review-r03.md`.
- **Confidence:** High. Four independent pipelines exposed claimed-contract or
  operation-order undercoverage, and pipeline `20260930T083956Z` showed that
  applying the lesson made its corrected trigger boundary and action sequence
  independently checkable. The later same-pipeline configuration-scope case
  strengthens the consequence but does not add an independent trial.
- **Consequence:** Before proposing a deterministic checker or evaluation gate,
  map every claimed PASS or benefit clause to an observable predicate, a
  false-positive counterexample or negative fixture, and a valid positive
  control. For resource bounds, enforce size and deadline gates before the
  consuming operation and assert that prohibited later invocations did not run.
  For environment-dependent guards, enumerate every effective configuration
  scope and inherited override or sanitize the exact child environment, then
  test an omitted-scope counterexample. Narrow the result claim whenever the
  grader deliberately omits one.

### Separate historical artifact identity from path provenance

- **Lesson:** When prior-work search traverses Git history, freeze the supplied
  revision or ref set, group logical artifacts by pipeline plus artifact ID, and
  retain path, containing commit, and blob as provenance. Describe absence only
  inside that reachable corpus, never as archival completeness.
- **Evidence:** Pipeline `20260930T124036Z` recovered 39 reachable Forge paths
  but only 34 logical artifact IDs at one frozen revision; five rename or move
  copies stayed within their pipelines, while exact historical bodies changed
  two bounded duplicate or reopening decisions without inventing a missing
  human disposition. See
  `forge/research/forge-history-duplicate-receipt-r01.md` and
  `forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md`.
- **Confidence:** Low. One pipeline and an independent evaluation reproduced the
  bounded corpus and identity result; behavior across later resets, larger
  histories, and other repositories is untested.
- **Consequence:** For historical duplicate checks, surface roots and decisive
  artifacts first, deduplicate path aliases by stable identity, require full
  body reads before disposition, preserve `unknown` for missing decisions, and
  halt or narrow the claim when reachability or identity is ambiguous.

### Prefer bounded native tools in unattended Forge sessions

- **Lesson:** In scheduled Forge work, prefer `read_file`, `search_files`, and
  fixed direct commands for log tails, metadata inspection, arithmetic, and
  state checks. Avoid inline interpreters, heredocs, and mixed commands when a
  bounded native tool can supply the same evidence; when code is necessary,
  write and inspect one task-owned scratch script before execution.
- **Evidence:** Unattended inline-interpreter or heredoc probes were blocked
  before execution in pipelines `20260930T083956Z`, `20260930T124036Z`,
  `20260930T173859Z`, and `20260930T223526Z`; bounded file tools and fixed
  commands recovered the required evidence in each case. See
  `logbook/errors.log` and
  `forge/graveyard/valuation-consistent-retained-earnings-test-evaluation-r01.md`.
- **Confidence:** Medium. Four independent pipelines, across Analyst and
  Researcher contexts and multiple stages, reproduce the failure and recovery
  pattern. No prospective stage has yet shown that applying this lesson removes
  every unattended approval block.
- **Consequence:** Select bounded native tools before optional interpreter
  wrappers, and never bundle a wait or state-changing command with dispensable
  parsing. A blocked call remains a failure to record; this lesson grants no
  approval, runtime, or governance permission.
