---
name: evidence-gated-forge-transaction-checker-evaluation
id: 20260930T045604Z
tier: evaluation
pipeline: 20260921T152802Z
author: Analyst
tags: [agent-systems, forge, verification, evaluation]
links:
  - forge/research/evidence-gated-forge-transaction-checker-r03.md
  - forge/ideas/evidence-gated-forge-transaction-checker-r01.md
  - forge/research/evidence-gated-forge-transaction-checker-r01.md
  - forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md
  - forge/research/evidence-gated-forge-transaction-checker-r02.md
  - forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r02.md
  - forge/protocol.md
  - logbook/protocol.md
  - STATUS.md
  - logbook/progress.log
  - scripts/validate-ids.sh
  - .github/workflows/ascii-guard.yml
  - forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md
  - LEARNINGS.md
  - agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
confidence: high
---
# Evaluation Revision 3: Evidence-Gated Forge Transaction Checker

## Target and Baseline

Target: `forge/research/evidence-gated-forge-transaction-checker-r03.md`, ID
`20260930T031626Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
fresh context that did not inherit the drafting session's private reasoning.
Pipeline `20260921T152802Z` has two prior `REVISE` verdicts and no recorded
human extension. Its ordinary correction budget is exhausted.[3][4][5]

At starting HEAD `8a9fca9bee6e2e67d8e8009268191489bc44a06b`, a cold baseline
was recorded at `2026-09-30T04:48:42Z` before target lines 28-979 were read.
Expected evidence was:

- an explicit partial-result boundary derived from the fields and relationships
  the checker claims to validate;
- a complete package containing the specification, checker, runner, fixtures,
  commands, raw results, hashes, and metrics;
- two valid controls plus all eleven prior mutants and result, category, and
  author mutants for both retained shapes;
- no false acceptance, false rejection, harness error, proxy targeting, write,
  lifecycle expansion, or implication of full transaction validity;
- successful use on valid real records where the claimed transaction shapes
  exist; and
- evidence that a 540-line two-shape package offers decision value over an
  explicit manual checklist.

Failure conditions were an unreconstructable package, any declared
classification mismatch, rejection of a valid claimed-shape record, an
undocumented parser constraint, scope expansion, or no demonstrated value over
the manual alternative. A negative result was acceptable. Because the budget
was exhausted, a remaining correction could not receive another ordinary
`REVISE` or `REFRAME`.[2][3][4]

## Findings

### The package and declared matrix are independently reproducible

The specification, checker, runner, static review, and reported output were
extracted from the exact target line ranges into task-owned scratch. All four
reported package files matched the target:[1]

| File | Lines | Bytes | SHA-256 |
|:--|--:|--:|:--|
| `pre-run-spec-v5.md` | 79 | 6,411 | `ba607ea4d85bac5faf6776732e270a9f085e79a545ba601b3864fa2d4c7050dc` |
| `check-transaction.sh` | 270 | 9,680 | `4d9e097af487e70bd62ea43df249e76ddc5028aff7f890eda5217c5eea63e347` |
| `run-fixtures.sh` | 270 | 12,170 | `779f656175469fb4571983fd910003ec702989ad888831bab8bd5a6e37a5345e` |
| `final-static-review.txt` | 9 | 795 | `7e2c9870d5f9654a91a877025c9d057d25562881befd2d954e6b5a7b2116755a` |

Both shell files passed `bash -n`. A separate fixture run exited 0 and returned
exactly two `PARTIAL_PASS` controls, seventeen expected `FAIL` mutants, and:

```text
SUMMARY|total=19|matched=19|all_expected=true
```

There were no `HARNESS_ERROR` classifications. This independently confirms the
package identity and all nineteen declared classifications. The corrected result
boundary is also materially narrower than revision 2: `PARTIAL_PASS` covers only
I01-I13 and expressly excludes complete protocol validity, semantic quality,
actual identity, independence, and production readiness.[1][3]

### A valid current open transaction is falsely rejected

The synthetic controls do not establish acceptance of valid current records.
The unchanged checker was therefore invoked read-only against the exact current
open research transaction selected for this evaluation:

```text
bash --noprofile --norc check-transaction.sh \
  /srv/forge/agentic-forge \
  open-research \
  20260921T152802Z \
  forge/research/evidence-gated-forge-transaction-checker-r03.md \
  20260930T031626Z \
  ENT-015 \
  research
```

It exited 1:

```text
FAIL linked artifact pipeline missing or ambiguous
```

The r03 artifact, matching STATUS row, and ENT-015 event form a valid current
open research-to-evaluate transaction.[1][5] The artifact links several
same-pipeline inputs and also links `forge/protocol.md`. That repository source
correctly has no `pipeline` field because it is a protocol rather than a
pipeline artifact.[4]

Specification I08 requires only one local `forge/` artifact link that resolves
and carries the selected pipeline. The implementation instead attempts to parse
a matching `pipeline` field from every frontmatter link beginning `forge/` and
fails immediately when any such link lacks one.[1] This is stricter than the
specified partial boundary and conflicts with the protocol's permission for
repository-relative source links and explicit cross-pipeline prior-work
comparisons.[4] A valid source link therefore becomes an undocumented rejection
condition.

The same checker was also invoked against the real terminal evaluation-REJECT
transaction at ENT-005. It exited 0:

```text
PARTIAL_PASS closed-evaluation-reject 20260921T114301Z forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md ENT-005
```

The closed real record passes while the current valid open record fails because
its permitted link set is richer than the synthetic fixture.[7] This is an
in-scope false rejection in one of the two claimed modes. It contradicts the
root idea's requirement that valid controls produce no false failure and blocks
advancement.[2]

### The automation gap is real, but this candidate's value is unproved

Full-file inspection confirms that `scripts/validate-ids.sh` checks timestamp
shape, suspicious rounding, duplicate IDs, and future IDs. The ASCII workflow
scans tracked text and invokes that script. Neither parses artifact-STATUS-event
relationships.[6] The idea therefore addresses a real executable-gate gap; the
false rejection does not show that every narrow checker is infeasible.

It does show that this package is not ready for proposal work. Its declared
suite uses minimal synthetic parser controls and omits valid repository
structure outside the selected predicates. The target also concedes that 270
checker lines plus 270 runner lines have no measured maintenance cost, live
integration evidence, or demonstrated advantage over an explicit manual
checklist.[1] Running the checker on the actual selected transaction converts
that limitation into a reproduced failure.

The historical validator is correctly reported as 707 lines. Direct Git
inspection found 44 changed paths in its addition commit and 44 in the immediate
revert, rather than the target's 43-file figure.[8] This count error is
non-blocking but should not be repeated.

The evidence is therefore asymmetric:

- all nineteen declared classifications are exact and independently reproduced;
- the partial label is appropriately narrow;
- the existing automation gap is real;
- one of two real claimed-shape records is falsely rejected by an undocumented
  constraint; and
- incremental review value and maintenance economics remain unmeasured.

A proposal is not justified on this record.

## Verdict and Handoff

**Verdict: DEFER.**

**Next stage: closed.** This evaluation is the closure record in
`forge/graveyard/`. Remove only pipeline `20260921T152802Z` from `STATUS.md`;
pipeline `20260929T223305Z` remains unchanged.

Two prior `REVISE` verdicts exhausted the correction budget, and no human
extension exists.[3][4][5] Correcting I08, adding real-record controls,
rerunning the package, and establishing incremental value would require another
corrective cycle. The protocol therefore requires `DEFER`, not a third `REVISE`
or `REFRAME`.[4]

`REJECT` is not selected because the current-gate gap and bounded technical
feasibility remain established. The remaining evidence could change: the false
rejection has a concrete cause, and comparative value has not been measured.
Missing correction budget and decision evidence do not prove that every narrow
checker is uneconomic.

Reopening requires all of the following:

1. a human-directed handoff with an explicit bounded correction-budget extension
   recorded under the protocol;
2. I08 behavior that matches the declared partial contract, permitting
   repository source links and protocol-valid cross-pipeline prior-work links
   while requiring the stated same-pipeline artifact witness;
3. unchanged full real records for every retained mode as positive controls,
   including the r03/ENT-015 transaction or an equivalent current-schema record;
4. continued success for both controls and M01-M17, plus a regression for this
   valid-link false rejection; and
5. comparative evidence that the partial receipt materially improves reviewer
   accuracy, effort, or failure detection over an explicit manual checklist
   without adding lifecycle modes, automatic target inference, CI, runtime
   machinery, or semantic claims.

Confidence is high. Package identity, declared classifications, the real-record
false rejection, its source-code cause, the correction count, and the missing
economics are directly verifiable. Confidence would fall if the protocol
prohibited the valid source link or required every `forge/` link to carry the
selected pipeline; it does neither.[4]

## Learning Decision

Strengthen the existing low-confidence lesson, `Derive checker fixtures from the
claimed PASS contract`, rather than add a duplicate or raise its confidence.[9]

- **Selection:** One unchanged full real record for each claimed mode would have
  exposed the false rejection before three research revisions.
- **Evidence and test design:** The preserved package made the declared success
  independently reproducible. Real positive controls then exposed an
  undocumented rejection condition that minimal synthetic controls did not
  contain. Accepted-output auditing must include valid structural variation,
  not only one minimal accepted example.[10]
- **Process:** The decisive step was invoking the unchanged checker on the actual
  selected transaction; no new lifecycle mode or production installation was
  needed.
- **Repetition:** This extends the existing lesson within the same pipeline. It
  is not independent evidence for a confidence increase.
- **Coverage:** The existing entry covers contract-derived negative fixtures but
  not false rejection caused by constraints outside the declared result map.
  Update that entry instead of adding another.

The lesson remains low confidence and now requires negative fixtures from every
claimed field and relationship plus positive controls from complete valid
records and permitted orthogonal variation. Its consequence is to run unchanged
current records for every supported mode before proposing a deterministic
checker. This method edit grants no governance, implementation, or deployment
authority.

## Sources

1. `forge/research/evidence-gated-forge-transaction-checker-r03.md` -- exact
   target, partial-result map, embedded package, nineteen reported
   classifications, scope, economics, and source claims. [high]
2. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- root
   question, valid-control requirement, support and stop conditions, manual
   alternative, and warning against false confidence. [high]
3. `forge/research/evidence-gated-forge-transaction-checker-r02.md` -- prior
   complete package, two-shape scope, target interface, declared matrix, and
   measured size. [high]
   - `forge/research/evidence-gated-forge-transaction-checker-r01.md` -- first
     matrix, current-gate gap, and missing durable package. [high]
   - `forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md`
     -- first REVISE, preservation blocker, and corrective-cycle count. [high]
   - `forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r02.md`
     -- independent r02 reproduction, three same-shape false positives, final
     correction requirements, and second corrective cycle. [high]
4. `forge/protocol.md` -- artifact links, cross-pipeline comparisons, stage
   dispositions, correction budget, graveyard routing, transaction agreement,
   and reopening requirements. [high]
   - `logbook/protocol.md` -- progress categories, actual-agent header,
     Stage/Result form, PASS meaning, exact references, and event agreement.
     [high]
5. `STATUS.md` -- selected r03 evaluate row, exhausted-budget notice, and
   unselected pipeline state at starting HEAD. [high]
   - `logbook/progress.log` -- ENT-015 r03 research handoff, both prior REVISE
     events, correction count, and absence of a human extension. [high]
6. `scripts/validate-ids.sh` -- executable ID checks and exclusion of transaction
   relationships. [high]
   - `.github/workflows/ascii-guard.yml` -- tracked-text ASCII scan and invocation
     of the ID validator, with no transaction checker. [high]
7. `forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md` -- valid real
   closed-evaluation-REJECT artifact used with ENT-005 for the real-record
   control. [high]
8. `scripts/validate-forge.py` -- historical 707-line validator verified at Git
   commit `682fbb4a3184654e62e70fc2d1fa620af2fbee7d`; that commit and immediate
   revert `35b8213f39e6d813c00ec1b36776d077a697b27c` each changed 44 paths. [high]
9. `LEARNINGS.md` -- package-preservation lesson, existing contract-derived
   fixture lesson, capture questions, and admission gate. [high]
10. `agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md`
    -- bidirectional auditing of accepted and rejected cases, grader validity,
    representative coverage, and bounded interpretation of deterministic
    results. [medium]
    - `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md`
      -- contract-first verification, pass-to-pass preservation, exact revision
      receipts, and bounded meaning of passing tests. [medium]
