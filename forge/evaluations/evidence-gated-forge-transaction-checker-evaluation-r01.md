---
name: evidence-gated-forge-transaction-checker-evaluation
id: 20260929T233502Z
tier: evaluation
pipeline: 20260921T152802Z
author: Analyst
tags: [agent-systems, forge, verification, evaluation]
links:
  - forge/research/evidence-gated-forge-transaction-checker-r01.md
  - forge/ideas/evidence-gated-forge-transaction-checker-r01.md
  - forge/protocol.md
  - logbook/protocol.md
  - scripts/validate-ids.sh
  - .github/workflows/ascii-guard.yml
  - agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md
  - agentic-brain:reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md
  - https://pitest.org/quickstart/basic_concepts/
  - https://docs.github.com/en/actions/how-tos/create-and-publish-actions/set-exit-codes
confidence: medium
---
# Evaluation: Evidence-Gated Forge Transaction Checker

## Target and Baseline

Target: `forge/research/evidence-gated-forge-transaction-checker-r01.md`,
ID `20260929T232637Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the drafting session's private
reasoning. Pipeline `20260921T152802Z` has no prior `REVISE` or `REFRAME`
verdict and no human budget extension.[3][4]

At starting HEAD `f8982b6926668a35a72de60a6609f3b7e5397e25`, the following
baseline was recorded before the target body was opened.

Expected evidence:

- a frozen current-schema transaction boundary and no more than ten mechanical
  invariants traceable to exact protocol clauses;
- valid controls plus one-fact negative fixtures showing at least one material
  artifact-STATUS-event contradiction that the existing ASCII and ID gates
  accept;
- preserved existing-gate and prototype outputs, with fixture definitions
  inspected separately before results were merged;
- a bounded read-only prototype that rejects every declared in-scope mutant,
  accepts every valid control, checks the requested transaction rather than a
  proxy, and excludes semantic review and deployment machinery; and
- comparison with no change and a shorter manual checklist, including coverage
  limits and false-confidence risk.[2][3][8]

Failure conditions were multi-fact or post-result fixture selection, missing
run evidence, a prototype miss or false rejection, proxy-target validation,
semantic or deployment-scale expansion, or no demonstrated decision value over
the current manual process. A negative result was acceptable.[2]

## Findings

### The executable-gate gap is real and material

The frozen commit exists, and the frozen blobs for `scripts/validate-ids.sh`
and `.github/workflows/ascii-guard.yml` match the current files. The ID script
parses only Markdown frontmatter IDs and checks their format, rounded seconds,
duplicates, and future timestamps.[5] The workflow scans tracked text for
non-ASCII bytes and then runs that ID script; it contains no STATUS, progress,
link, stage-transition, or closure-agreement check.[6] A current run scanned 13
frontmatter IDs with zero errors and zero warnings. GitHub's documentation
independently confirms that the invoked commands' exit status controls the
check result.[11]

Source inspection therefore independently establishes the important negative
result. Each declared mutant changes an ASCII event header, artifact field,
link, STATUS cell, or progress field outside the existing gates' relational
scope. None changes a frontmatter ID. The existing gates cannot distinguish
those fixtures from the corresponding controls. This conclusion does not rely
on the unavailable prototype output.[1][5][6]

The protocol and logbook rules also confirm that the intended mutations are
invalid. In particular, M09 points the active row at a missing artifact, M10
skips the required independent evaluation handoff, and M11 makes the closure
event disagree with the terminal artifact. The pipeline, exact artifact,
stage, event reference, and closure disposition are required to agree.[3][4]
These are decision-relevant transaction failures, not formatting preferences.
They support the need to compare a narrow executable check with the manual
process.

The research also kept the broad alternative in view. Git history confirms
that the earlier validator was 707 lines inside a 43-file system change and
that the next commit reverted that entire change.[7] The target excludes locks,
monitors, deployment controls, and semantic grading, and it reports only ten
mechanical invariants.[1] This is appropriate counterevidence against treating
any automated gate as beneficial by default. The Brain sources likewise limit
deterministic checks to the properties they can enforce and require accepted
as well as rejected cases to be audited.[8][9] PIT's mutation-testing guidance
supports the bounded use of deliberately faulty cases while warning that test
meaning depends on whether the mutation is behaviorally distinct.[10]

### The prototype result is not independently checkable

The decisive positive claims remain supported only by the completed report.
The report gives SHA-256 values for a fixture specification, prototype, runner,
and 13-case JSON result, but none of those bytes is present in the research
commit or elsewhere in the repository. The research commit adds the report and
changes only STATUS and the two logs. Repository search finds the four hashes
only in the report.[1] A hash can identify available bytes; it cannot recover
missing bytes for inspection or rerun.

Consequently, this evaluation cannot check whether the prototype actually
implemented the ten stated invariants, selected the requested ENT, accepted
both controls, rejected all eleven mutants, or remained small and read-only.
It also cannot inspect the exact open-control overlay, runner behavior, command
outputs, dependencies, line count, or aggregate JSON. The preserved matrix is
an explicit report of the run, but it is not an independently reproducible test
receipt. This blocks advancement because the root idea makes prototype
acceptance of every declared negative and valid fixture an express condition
for supporting a proposal.[2]

The separate-reader claim has the same limitation. The target candidly states
that the two raw reader responses were not separately preserved and does not
claim blind or independently audited reproducibility.[1] That limitation is
accurate, but the reader correction is then not independent evidence that the
fixture set was frozen before results. The existing Forge lesson already says
that a completed report's retrospective account cannot establish timing or
independence without dated pre-comparison rules and unmerged reader outputs.[12]
The exact-target reflection supports the failure mechanism, not this run's
chronology.[9]

### Coverage and alternatives remain bounded

The two positive controls cover one open research-to-evaluate handoff and one
terminal REJECT closure. Revisions, reframes, ADVANCE, proposals, final reviews,
READY, human decisions, archived logs, malformed Markdown, and concurrent
writers were not tested.[1] This does not require a broad validator. It does
require the claimed production scope to be no wider than its valid controls,
or additional positive controls for each stage/state shape that a proposal
would encode.[8]

The no-change and manual-checklist alternatives are stated fairly. The manual
process has no new code cost, while a shorter checklist cannot itself prove
that the requested transaction was checked.[1][3] However, the absent prototype
prevents a concrete comparison of script size, dependencies, target interface,
maintenance surface, and failure behavior with either the checklist or the
reverted 707-line validator. Ten conceptual invariants are narrower than the
historical system, but they do not by themselves establish a small or economical
implementation.

The evidence is therefore asymmetric. It strongly establishes a real gap in
the current executable gates and identifies a plausible bounded remedy. It does
not yet preserve the evidence needed to verify that the tested remedy worked or
stayed narrow. This is an evidence defect, not evidence that the checker idea is
false.

## Verdict and Handoff

**Verdict: REVISE.**

**Next stage: research.** Pipeline `20260921T152802Z` remains active, with this
evaluation as the handoff artifact. This is corrective cycle 1 of 2.[3]

A revision must keep the live repository unchanged and answer the following
blocking questions:

1. Can the complete prototype, runner, exact fixture definitions, control
   overlays, commands, and raw per-case outputs be preserved in a
   protocol-allowed immutable form so another evaluator can inspect and rerun
   the reported matrix? If the full package is too large, narrow the claimed
   checker and preserve a smaller complete package rather than reporting only
   hashes.
2. Can a dated pre-run specification and the unmerged fixture-review output be
   preserved before execution, or must the independent-review claim be removed
   from the support for the result?
3. Does every stage/state shape that a later proposal would claim to accept have
   a valid positive control with no false failure? Otherwise, what exact two-shape
   scope will the proposal retain?
4. What are the prototype's line count, dependencies, explicit transaction
   target interface, read-only failure behavior, and maintenance difference
   from both the current checklist and the reverted validator?

Research revision 2 should rerun only the bounded experiment needed to answer
those questions. It must not install, commit, schedule, or deploy a production
checker. ADVANCE would become justified if the durable package independently
confirms the matrix, the positive controls match the claimed scope, and the
measured implementation remains materially narrower than the reverted system.
A miss, false rejection, ambiguous target, or scope expansion would support
closure or a smaller manual alternative.

Confidence in this disposition is medium. The gate-scope gap and protocol
contradictions are directly verifiable from high-quality repository sources.
The exact prototype behavior, reader timing, and implementation cost are not
verifiable because their underlying bytes were not preserved. Confidence would
rise after an independently inspectable rerun package or fall if such a package
shows any claimed result or scope boundary was inaccurate.

## Learning Decision

`LEARNINGS.md` is strengthened rather than given a duplicate lesson.

- **Selection:** The root idea required a detection matrix but did not require
  preservation of the executable instrument and raw result bytes; that omission
  should have been a stop condition before research execution.
- **Evidence and test design:** Source inspection made the current-gate gap
  decisive. Missing prototype, fixture, raw-output, and reader bytes made the
  positive comparison unverifiable despite reported hashes.
- **Process:** Scratch-only evidence was discarded even though the later
  evaluation depended on it. A protocol-allowed pre-run checkpoint or a complete
  in-artifact package would have preserved the distinction without deploying
  anything.
- **Repetition and coverage:** This is a third independent Forge pipeline in
  which a completed report cannot establish procedural timing or performance
  from absent underlying artifacts. The existing preservation lesson is
  applicable but too narrow because it names rules and reader outputs, not the
  runnable instrument, fixtures, and raw per-case results.[12]

The existing lesson is updated at medium confidence to require all four evidence
classes before treating a procedural validation as passed. This method change
does not authorize a checker, supporting file, runtime, or governance edit.

## Sources

1. `forge/research/evidence-gated-forge-transaction-checker-r01.md` -- exact
   research target, reported fixture method and matrix, hashes, alternatives,
   limitations, and research commit contents at Git commit
   `f8982b6926668a35a72de60a6609f3b7e5397e25`. [high]
2. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- root
   question, bounded research plan, acceptance conditions, stop conditions, and
   broad-validator exclusion. [high]
3. `forge/protocol.md` -- stage mapping, artifact contract, board rules,
   correction budget, closure agreement, transaction verification, and write
   boundary. [high]
4. `logbook/protocol.md` -- unique sequential ENT records, exact references,
   pipeline and stage fields, and artifact-STATUS-event agreement. [high]
5. `scripts/validate-ids.sh` -- exact ID parser and checks at frozen blob
   `8d7d8e5e46b99b7c6c57830667b460312b6a2275`; it does not parse transaction
   relationships. [high]
6. `.github/workflows/ascii-guard.yml` -- exact workflow at frozen blob
   `107c6f3b8535d744e010b757f4f8a275351362d5`; it invokes only the ASCII scan
   and ID validator. [high]
7. `scripts/validate-forge.py` -- 707-line historical validator at Git commit
   `682fbb4a3184654e62e70fc2d1fa620af2fbee7d`; immediate revert commit
   `35b8213f39e6d813c00ec1b36776d077a697b27c` and the 43-file add were checked
   from Git history. [high]
8. `agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md`
   -- evaluation contracts, accepted-and-rejected case auditing, artifact
   preservation, and limits of deterministic graders. [medium]
9. `agentic-brain:reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md`
   -- operational account of an exact-target validator defect exposed by
   negative fixtures; checked as a related mechanism, not proof of this run.
   [medium]
10. PIT. "Basic Concepts," undated; accessed 2026-09-29, Mutation Operators,
    Equivalent Mutations, and Running the tests sections. Deliberate mutants,
    killed mutants, and equivalent-mutation limits were checked.
    https://pitest.org/quickstart/basic_concepts/ [medium]
11. GitHub. "Setting exit codes for actions," undated; accessed 2026-09-29,
    About exit codes section. Exit status determines action check-run success or
    failure.
    https://docs.github.com/en/actions/how-tos/create-and-publish-actions/set-exit-codes [high]
12. `LEARNINGS.md` -- current evidence-preservation lesson and its two-pipeline
    basis before this evaluation. [high]
