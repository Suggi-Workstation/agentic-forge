---
name: evidence-gated-forge-transaction-checker-evaluation
id: 20260930T023515Z
tier: evaluation
pipeline: 20260921T152802Z
author: Analyst
tags: [agent-systems, forge, verification, evaluation]
links:
  - forge/research/evidence-gated-forge-transaction-checker-r02.md
  - forge/ideas/evidence-gated-forge-transaction-checker-r01.md
  - forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md
  - forge/protocol.md
  - logbook/protocol.md
  - STATUS.md
  - logbook/progress.log
  - scripts/validate-ids.sh
  - .github/workflows/ascii-guard.yml
confidence: medium
---
# Evaluation Revision 2: Evidence-Gated Forge Transaction Checker

## Target and Baseline

Target: `forge/research/evidence-gated-forge-transaction-checker-r02.md`, ID
`20260930T012523Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the drafting session's private
reasoning. Pipeline `20260921T152802Z` has one prior `REVISE` verdict and no
human budget extension, so one corrective cycle remained before this verdict.[3][4][6][7]

At starting HEAD `185464e6153d88a47828ce1481e2dd8efe0fdc79`, a cold baseline
was recorded before the target body was opened. Expected evidence was:

- a complete immutable package containing the prototype, runner, exact fixtures,
  control overlays, commands, and raw per-case outputs;
- an independent extraction and rerun that accepted both controls and rejected
  all eleven declared one-line mutants;
- no use of pre-run timing or separate-reader independence as support unless
  those claims were independently durable;
- an exact two-shape scope, explicit target arguments, read-only behavior, and
  measured comparison with the manual check and reverted validator; and
- no semantic review, deployment machinery, automatic target inference, or
  unsupported lifecycle coverage.[2][3]

Failure conditions were missing package bytes, a rerun mismatch, any false
acceptance or false rejection within a claimed shape, proxy targeting, broader
scope, unsupported chronology, or no demonstrated decision value over the
manual transaction check. A negative result was acceptable.

## Findings

### The preserved package is exact and independently rerunnable

The five embedded evidence files were extracted directly from the committed
research artifact. Their line counts, byte counts, and SHA-256 values matched
the target exactly: the specification was 77 lines and 4,717 bytes, the checker
246 lines and 8,716 bytes, the runner 238 lines and 9,658 bytes, the static
review 52 lines and 4,672 bytes, and the reported aggregate output 15 lines and
920 bytes.[1]

Both extracted shell files passed `bash -n`. A separate run then reproduced all
thirteen reported classifications: both positive controls returned `PASS` with
exit 0, all eleven declared mutants returned one `FAIL` line with exit 1, and
the summary was `total=13`, `matched=13`, `all_expected=true`. The extracted
checker and runner hashes remained unchanged after the run. This resolves the
prior evaluation's package-preservation blocker for the declared matrix.[1][3]

Independent full-file inspection also confirms the underlying gate gap.
`scripts/validate-ids.sh` checks frontmatter ID format, suspicious rounding,
duplicates, and future timestamps; the ASCII workflow scans bytes and invokes
that ID script. Neither parses artifact-STATUS-event relationships.[8][9]
Git history confirms that the compared historical validator was 707 lines in a
43-file system change and that the immediately following commit reverted that
change.[10] The target is materially narrower in stated modes and authority, but
size alone does not establish useful coverage or maintenance value.

### Three same-shape contradictions still receive PASS

The declared 13-case matrix is internally reproducible but incomplete against
the current contract. The checker parses the selected event's `Stage` by
truncating the line at its first period. It never parses the event's `Result`.
It requires a nonempty header author and category but does not compare the
header author with the artifact author or the category with the selected
stage.[1]

Three additional one-line mutants were applied separately to the valid
`open-research` fixture after the independent rerun:

1. `Stage: research. Result: PASS.` was changed to
   `Stage: research. Result: FAIL.`;
2. the selected event category was changed from `research` to `error`; and
3. the selected event author was changed from `Researcher` to `Analyst` while
   the research artifact author remained `Researcher`.

The unmodified extracted checker returned its generic `PASS` line with exit 0
for all three mutants. These are not additional lifecycle shapes or adversarial
filesystem cases. They alter required fields inside the package's claimed open
research-to-evaluate shape.

The Forge protocol requires actual artifact authorship and actual-agent event
recording. The logbook contract requires stage names, valid progress categories,
and the exact `Stage: <stage>. Result: <result>.` record, with `PASS` meaning the
artifact and handoff passed their gates.[4][5] A failed research event cannot
support an active evaluate handoff, and an error-category event cannot serve as
the required progress event. An event author that disagrees with the artifact
also defeats the transaction's authorship record.[4][5]

The package therefore demonstrates 13 correct classifications, not a sound PASS
condition for either claimed transaction shape. A generic PASS that accepts a
failed stage is a decision-relevant false positive. This blocks advancement even
though the original preservation defect is fixed.

### A bounded correction remains possible

The current executable-gate gap is real, the evidence package is now complete,
and the new false positives are directly reproducible. Those facts weigh
against rejection. However, the target still reports no live inconsistent Forge
commit, maintenance measurement, or integration test, and its 246-line checker
plus 238-line runner covers only two shapes.[1][2] A proposal is not justified
until the checker either rejects the contract-invalid fields within those shapes
or narrows its output and claims so that PASS cannot be mistaken for transaction
validity.

The correction need not add lifecycle modes, deployment controls, or semantic
review. It can remain bounded to the two declared shapes and derive fixtures
from the exact normative fields that its PASS result claims to validate.

## Verdict and Handoff

**Verdict: REVISE.**

**Next stage: research.** Pipeline `20260921T152802Z` remains active, with this
evaluation as the handoff artifact. This is corrective cycle 2 of 2.[4]

The final permitted correction must answer these blocking questions:

1. For each of the two claimed transaction shapes, which exact protocol and
   logbook fields does PASS mean are valid? Map every included field and
   relationship to its rule and fixture rather than selecting mutants first.
2. Can the checker reject, as separate one-line cases, a non-PASS stage result,
   a wrong progress category, and an event author that disagrees with the
   artifact author? If any field is intentionally excluded, replace the generic
   transaction PASS claim with an explicitly partial result whose meaning cannot
   imply full shape validity.
3. Can the corrected immutable package preserve and rerun both positive controls,
   all eleven existing mutants, and the newly required cases with no harness
   error, false rejection, or accepted in-scope contradiction?
4. After the exact PASS boundary is corrected, does two-shape coverage still
   offer enough value over the manual checklist to justify maintaining the
   measured checker and runner? Do not expand to other lifecycle shapes to make
   the economics appear stronger.

Another `REVISE` or `REFRAME` would exceed the correction budget. Without an
explicit human extension, the next evaluation must either support advancement
or use a non-corrective closure disposition.[4]

Confidence in this disposition is medium. The package identity, declared rerun,
current gate scope, and three additional false positives are directly
reproducible. Confidence is limited because the focused probes do not estimate
all possible omissions and maintenance value remains unmeasured. Confidence
would rise if a corrected package derives its PASS boundary from the full
claimed shape contract and independently rejects every included-field mutant;
it would fall if the intended output is narrowed enough that the three fields
are demonstrably outside a clearly labeled partial check.

## Learning Decision

`LEARNINGS.md` should add one low-confidence method lesson rather than change the
existing package-preservation lesson.[11]

- **Selection:** The root plan selected plausible contradictions but did not map
  the checker's generic PASS meaning to every normative field in either claimed
  shape. A contract-to-fixture map would have exposed the omitted result,
  category, and authorship checks before execution.
- **Evidence and test design:** Preserving the complete package made both the
  reported success and the unseeded false positives independently testable. A
  perfect result on declared mutants does not bound fields that the fixture set
  never mutates.
- **Process:** Two unattended extraction routes were blocked before execution;
  exact line-range extraction with non-deleting shell utilities preserved the
  bytes and completed the rerun. This is tool-recovery chronology, not a separate
  lesson about checker quality.
- **Repetition:** The historical broad validator supplied prior warning that a
  checker can accept contradictory states, but it is prior work from this idea's
  origin rather than an independent new pipeline. The new lesson therefore
  enters at low confidence.
- **Coverage:** The existing lesson governs evidence preservation, not whether
  a declared mutation matrix covers the semantics of PASS. The new lesson is
  non-duplicate and grants no implementation or governance authority.

The admitted lesson should require deterministic checker fixtures to derive from
the claimed PASS contract, or require the result to be labeled as a partial
check. Its concrete consequence is to prevent a 100% declared mutation result
from being reported as transaction validity while required fields remain
untested.

## Sources

1. `forge/research/evidence-gated-forge-transaction-checker-r02.md` -- exact
   research target, embedded specification, checker, runner, receipts, reported
   matrix, scope, limitations, and package hashes. [high]
2. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- root
   question, narrow-checker conditions, negative-fixture plan, stop conditions,
   and warning against false confidence and broad validation. [high]
3. `forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md`
   -- prior REVISE verdict, missing package evidence, exact blocking questions,
   and corrective-cycle count. [high]
4. `forge/protocol.md` -- authorship, stage independence, handoffs, correction
   budget, transaction agreement, dispositions, and scope boundaries. [high]
5. `logbook/protocol.md` -- actual-agent headers, progress categories, exact
   Pipeline and Stage/Result fields, PASS meaning, and event agreement. [high]
6. `STATUS.md` -- selected research-to-evaluate row and preserved unselected
   final-review row at starting HEAD
   `185464e6153d88a47828ce1481e2dd8efe0fdc79`. [high]
7. `logbook/progress.log` -- prior REVISE event, revision-2 research handoff,
   current correction count, and unselected pipeline handoff at the same starting
   HEAD. [high]
8. `scripts/validate-ids.sh` -- current ID parser and checks; no STATUS, event,
   link, stage-result, category, or authorship relationship parsing. [high]
9. `.github/workflows/ascii-guard.yml` -- current tracked-text ASCII scan and
   invocation of the ID validator; no transaction relationship check. [high]
10. `scripts/validate-forge.py` -- 707-line historical validator at Git commit
    `682fbb4a3184654e62e70fc2d1fa620af2fbee7d`, added in a 43-file change and
    removed by immediate revert commit
    `35b8213f39e6d813c00ec1b36776d077a697b27c`. [high]
11. `LEARNINGS.md` -- current package-preservation lesson and separate learning
    admission gate. [high]
