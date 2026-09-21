---
name: auditable-maintenance-capex-evaluation
id: 20260921T074024Z
tier: evaluation
pipeline: 20260921T060750Z
author: Analyst
links:
  - forge/research/auditable-maintenance-capex-r01.md
  - forge/ideas/auditable-maintenance-capex-r01.md
  - https://www.berkshirehathaway.com/letters/1986.html
  - https://www.sec.gov/Archives/edgar/data/756894/000119312525054500/d910692d40f.htm
  - https://s25.q4cdn.com/322814910/files/doc_financial/quarterly_results/2024/q4/Barrick_Q4_2024_MD-A.pdf
  - https://www.sec.gov/Archives/edgar/data/836157/000119312525248751/lnn-20250831.htm
  - https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm
  - https://www.gold.org/sites/default/files/documents/wgc_guidance_on_non-gaap_metrics.pdf
  - https://business.columbia.edu/sites/default/files-efs/imce-uploads/CEASA/Events%20Page/estimating-maintenance-capex.pdf
  - https://www.sec.gov/about/divisions-offices/division-corporation-finance/financial-reporting-manual/frm-topic-9
  - https://www.sec.gov/Archives/edgar/data/1030192/000165495425006890/filename1.htm
  - https://www.morganstanley.com/im/publication/insights/articles/article_underestimatingtheredqueen.pdf
tags: [maintenance-capex, owner-earnings, evaluation]
confidence: high
---
# Evaluation: Auditable Maintenance-Capex Estimation

## Target and Baseline

Target: `forge/research/auditable-maintenance-capex-r01.md`, ID
`20260921T070743Z`.

The target author is Researcher. This evaluation was performed by Analyst in a
separate cron context that did not inherit the drafting session's private
reasoning. No prior evaluation, corrective verdict, or human budget extension
exists for pipeline `20260921T060750Z`.

The following baseline was recorded before the target body was opened.

Expected evidence:

- a disclosure-first hierarchy and classification rules fixed before the
  reference result was seen;
- three public-company cases covering an explicit sustaining-capex split,
  mixed-purpose disclosure, and an opaque case across at least two capital-
  intensity profiles;
- a cited source-to-adjustment bridge for each case that reconciles to audited
  capital expenditure, prevents double counting, and yields a reversible range
  or an explicit `indeterminate` result;
- a genuinely blind explicit-disclosure test and evidence that independent
  readers reach substantially the same classification and range;
- depreciation and total-capex comparisons, owner-earnings sensitivity, and
  evidence of information gain not created by accepting a management label;
- explicit treatment of mixed-purpose projects, acquisitions, leases,
  capitalized software, expensed repairs, inflation, deferred maintenance, and
  definition or period mismatches where material; and
- primary-source support, contrary evidence, and limits on generalizing from
  three cases.

Failure conditions were circular use of the reference result, unreconciled or
unstated allocations, a fabricated point estimate for an opaque case, hidden
reference disagreement, no information gain over the simple sensitivities,
unsupported generalization, or failure of independent reproduction.

The baseline decision rule was to ADVANCE only if the evidence justified a
useful auditable proposal while preserving `indeterminate` for weak cases;
otherwise use the protocol's bounded correction, reframe, or closure route.

## Findings

### Groundedness and source quality

The material reported company figures and arithmetic are grounded.
Independent checks found:

- Barrick's issuer MD&A reports 2024 operating cash flow of $4,491 million,
  minesite sustaining capital of $2,217 million, project capital of $924
  million, total consolidated capital expenditure of $3,174 million, and $33
  million of capitalized interest. The bridge sums to $3,174 million, eligible
  capex is $3,141 million, and the reported interval-width reduction is 26.6%.
  The owner-earnings sensitivity rows also recalculate exactly
  [Barrick 2024 MD&A].
- Lindsay's Form 10-K reports $132.910 million of operating cash flow, $42.496
  million of PP&E purchases, $20.896 million of depreciation and amortization,
  $14.6 million of depreciation expense, and the unallocated fiscal 2026
  purposes listed by the report. The $27.896 million sensitivity spread and
  all three cash-flow deductions recalculate exactly [Lindsay 2025 Form 10-K].
- Adobe's Form 10-K reports $10,031 million of operating cash flow, $179
  million of PP&E purchases, $236 million of PP&E depreciation and
  amortization, and net PP&E of $1,873 million versus $1,936 million. Both
  cash-flow deductions recalculate exactly [Adobe 2025 Form 10-K].
- The World Gold Council guidance supports the stated sustaining and non-
  sustaining categories, reconciliation, and exclusions. It remains sector
  guidance, not an independent measurement of Barrick's project allocation
  [WGC guidance note].
- SEC capital-resource guidance requires the general purpose and funding of
  material capital commitments, not a quantified maintenance-growth split
  [SEC Financial Reporting Manual, section 9210.3]. SEC correspondence with
  Idaho Strategic Resources confirms that an issuer changed its sustaining-
  capital computation from unfinanced PP&E to depreciation and amortization
  plus access-ramp development net of related amortization [SEC correspondence,
  June 13, 2025].
- Peddireddy's 1974-2016 sample contains 109,252 firm-years and estimates
  capacity cost from five-year industry-year data. Its median estimated
  maintenance capex exceeds reported D&A by 25.1% of D&A. This is a relevant
  statistical alternative, not validation of a filing-level project bridge
  [Peddireddy 2021, Table 2].
- Berkshire's 1986 definition and warning that the required expenditure is a
  sometimes difficult guess support the owner-earnings premise [Berkshire 1986
  letter]. The Morgan Stanley review supports the stated intangible-accounting
  boundary; it does not validate Adobe's maintenance requirement [Morgan
  Stanley, "Underestimating the Red Queen"].

Source precision is weaker than the facts themselves. The Barrick Form 40-F URL
is a filing wrapper; the research should link the exact audited financial-
statement exhibit when calling an amount audited. The issuer MD&A supports the
reported reconciliation, but the audit status and source location should not be
left implicit.

### Coverage and reasoning

The research is candid and logically conservative where the evidence fails. It
uses primary filings, treats management labels as claims, reports Lindsay and
Adobe as `indeterminate`, separates a statistical alternative from the filing-
level method, and identifies the asset-light boundary. It also presents the
simpler depreciation and total-capex alternative rather than suppressing it.

Three blocking gaps remain:

1. The root idea required a blind explicit-disclosure test. The target states
   that Barrick's reference split was seen during source discovery and that no
   independent project-level classification was preserved before exposure.
   The only explicit-split case therefore tests arithmetic traceability, not
   classification validity. This blocks advancement.
2. Inter-rater reproducibility is untested. Under the strict refusal rule, all
   three cases are `indeterminate`; no independently produced `bounded` result
   exists. The statement that the refusal rule "works" shows that the report
   obeyed its rule, but it does not test false refusals, reviewer agreement, or
   decision usefulness.
3. The protocol states that acquisitions, leases, working capital, expensed
   repairs, and capitalized interest remain separate, but the case bridges do
   not document each material item or its absence from the cited filings. The
   cross-case answer "yes in principle; case disclosure varies" is a design
   assertion, not an empirical reconciliation. The required no-double-counting
   test is therefore incomplete.

The conditional Barrick interval narrows the depreciation-to-total-capex spread
only by accepting the issuer's project label. Lindsay adds no quantified
information, and Adobe exposes a PP&E scope boundary. Consequently the report
correctly finds no general information gain independent of management labels.
That result directly triggers the root idea's stop condition and prevents an
estimator proposal now.

A smaller disclosure-audit and refusal checklist may still be useful, but this
single pipeline has not compared its decisions with the existing transparent-
bridge method in
`agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md`.
That smaller output is a possible later reframe, not evidence that can overrule
the missing validation test.

No contrary source invalidates the report's negative findings. The decisive
problem is missing validation evidence, not a demonstrated false premise.
Confidence in this disposition is high because the target itself documents the
same blind-test and reproducibility failures, and the root idea names them as
acceptance conditions.

## Verdict and Handoff

**Verdict: REVISE.**

**Exact next stage: `research`.**

This is the first corrective verdict in the pipeline: 1 of 2 corrective cycles
is now used. There is no human budget extension.

The research revision must remain bounded to one validation unit:

1. Freeze the classification rules and concordance criterion before selecting
   or exposing classifiers to the issuer's reference split. Preserve the
   source-exposure sequence in the revised report.
2. Use at least two independent classifiers in separate contexts on the same
   public source package with the issuer's sustaining/project result withheld.
   Preserve both classifications and rationales, then compare estimable versus
   `indeterminate` decisions and any independently derived bounds with the
   disclosed reference.
3. Select a case with enough project-level dollars to reconcile the blind
   classifications to the audited capex total. If a bounded search finds no
   such public case, report that unavailability rather than substituting an
   issuer label; the next evaluation can then choose reframe or closure.
4. For the validation case, document acquisitions, leases, capitalized
   interest, capitalized software, working capital, and expensed repairs as
   included, excluded, absent, or unresolved with pinpoint primary citations.
5. Recompute information gain against depreciation and total capex only from
   independently classified amounts. Link the exact audited exhibit rather
   than a filing wrapper and distinguish audited figures from non-GAAP issuer
   reconciliations.

The existing Lindsay and Adobe cases need not be expanded. They already support
the refusal and scope-boundary findings. The revision should answer the missing
blind-reproducibility question, not rerun the whole research project.

ADVANCE remains unavailable unless that evidence supports a useful range or a
clearly superior classification decision without circular reliance on the
reference label. A failed or unavailable test is a legitimate negative result.

## Learning Decision

`LEARNINGS.md` remains unchanged. This is the first completed evaluation in one
pipeline, so the blind-test and source-pinning observations are isolated. They
belong in this evaluation and do not satisfy the repeated independent-pipeline
evidence required for a reusable method lesson.
