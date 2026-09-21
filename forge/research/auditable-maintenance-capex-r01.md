---
name: auditable-maintenance-capex-research
id: 20260921T070743Z
tier: research
pipeline: 20260921T060750Z
author: Researcher
links:
  - forge/ideas/auditable-maintenance-capex-r01.md
  - agentic-brain:library/valuation-screening/earnings-power-value-and-asset-based-valuation.md
  - agentic-brain:library/value-investing/berkshire-annual-reports-1986-1995.md
  - agentic-brain:library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md
  - agentic-brain:library/value-investing/intrinsic-value-estimation-methods.md
  - agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md
  - https://www.sec.gov/Archives/edgar/data/836157/000119312525248751/lnn-20250831.htm
  - https://www.berkshirehathaway.com/letters/1986.html
  - https://www.sec.gov/Archives/edgar/data/756894/000119312525054500/d910692d40f.htm
  - https://s25.q4cdn.com/322814910/files/doc_financial/quarterly_results/2024/q4/Barrick_Q4_2024_MD-A.pdf
  - https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm
  - https://www.gold.org/sites/default/files/documents/wgc_guidance_on_non-gaap_metrics.pdf
  - https://business.columbia.edu/sites/default/files-efs/imce-uploads/CEASA/Events%20Page/estimating-maintenance-capex.pdf
  - https://www.sec.gov/about/divisions-offices/division-corporation-finance/financial-reporting-manual/frm-topic-9
  - https://www.sec.gov/Archives/edgar/data/1030192/000165495425006890/filename1.htm
  - https://www.morganstanley.com/im/publication/insights/articles/article_underestimatingtheredqueen.pdf
tags: [maintenance-capex, owner-earnings, disclosure, valuation]
confidence: medium
---
# Auditable Maintenance-Capex Estimation: Evidence Report

## Question and Method

This report investigates the root idea's question: can a disclosure-first,
sector-aware protocol estimate a defensible maintenance-capital-expenditure
range from public filings while returning "indeterminate" when the evidence is
inadequate?

Buffett's 1986 owner-earnings definition deducts average annual capitalized
expenditures needed to maintain competitive position and unit volume and states
that the estimate is necessarily imprecise.[3] The checked Brain sources reach
the same analytical starting point: maintenance capex is an economic estimate,
not a GAAP subtotal; depreciation and total capex are comparison cases; and each
adjustment should remain visible in a normalized-cash bridge
[`agentic-brain:library/value-investing/berkshire-annual-reports-1986-1995.md`;
`agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md`].

### Provisional explanation and gaps

Before the company tests, the provisional explanation was that an auditable
range should begin with cash additions to long-lived operating assets, remove
separately reported acquisitions and financing items, classify only projects
whose purpose and amount are disclosed, and place unresolved mixed-purpose
spending in uncertainty rather than force an allocation. The principal gaps
were whether filings quantify project purposes, whether sector conventions are
independent of management judgment, whether depreciation supplies a usable
bound, and whether an asset-light case requires a different treatment.

### Pre-specified classification protocol

The following rules were applied to the three cases:

1. **Eligible total.** Start with the audited cash-flow line for property,
   plant, equipment, and separately disclosed capitalized operating assets.
   Keep acquisitions, lease principal, working capital, expensed repairs, and
   capitalized interest separate so that none is double counted.
2. **Direct maintenance lower bound.** Include only quantified replacement,
   rebuild, safety, environmental, or other spending explicitly required to
   preserve current unit volume or competitive position. A management label is
   evidence, not sufficient proof by itself.
3. **Uncertain upper bound.** Add mixed-purpose and unallocated eligible capex.
   Exclude a project only when a cited purpose and amount show a new operation
   or a material increase in productive capacity. Productivity, modernization,
   and compliance projects remain mixed unless the filing explains the
   preserved or added capacity.
4. **Cross-checks, not substitutes.** Compare the result with depreciation and
   total capex, asset age, output or capacity, and multi-year operating results.
   None of these proxies can create a bound that project evidence does not
   support.
5. **Refusal rule.** Return `indeterminate` if either bound cannot be quantified,
   the purpose categories do not reconcile to the audited total, or the result
   depends mainly on an issuer label that cannot be checked against project or
   operating evidence.

The protocol was tested on three public companies and two capital-intensity
profiles: Barrick Gold (mining, with a disclosed sustaining/project split),
Lindsay Corporation (industrial manufacturing, with mixed-purpose disclosure),
and Adobe (asset-light software, with no maintenance/growth split). Source
checks used one selected annual filing for each case and were performed on
2026-09-21. The figures below are nominal US dollars and company fiscal years;
no security recommendation is made.

The explicit-disclosure case was not a valid blind validation. The Barrick
reference split appeared during source discovery, and no contemporaneous,
independent project-level classification was preserved before exposure. The
report therefore tests reconciliation and traceability, not independent
reproduction. This is a blocking limitation, not a passed blinded test.

## Evidence and Findings

### 1. Reporting rules and sector conventions do not create a universal split

The SEC Financial Reporting Manual asks registrants to discuss material capital
commitments, their general purpose, funding, and material capital-resource
trends.[8] The checked passage does not itself prescribe a quantified
maintenance-versus-growth split. **Inference:** a US filing can satisfy the
cited capital-resources guidance while leaving the owner-earnings classification
unresolved.

The World Gold Council provides a stronger sector convention. Its 2013 guidance
classifies costs at new operations and major existing-operation projects that
materially increase production as non-sustaining; all other existing-operation
costs are sustaining. It calls for reconciliation to GAAP or IFRS and excludes
capitalized interest, business combinations, asset acquisitions, disposals,
working capital, and financing charges.[6] This directly supports the eligible-
total bridge and some mining classifications. It does not provide an independent
measurement of whether a particular project materially increases production;
that project judgment remains issuer-specific.

A 2025 SEC correspondence record illustrates the risk. SEC staff asked Idaho
Strategic Resources to explain and quantify its sustaining-capital calculation
and a change in method. The company responded that it used depreciation and
amortization plus mine-development costs less related amortization, whereas its
prior method included only unfinanced PP&E and omitted the access ramp.[9]
**Finding:** the label can be changed by management and can embed financing and
amortization choices. A reconciliation improves traceability but does not make
the classification independent.

### 2. Barrick Gold: reconciled disclosure, but no independent blind validation

Barrick's 2024 audited cash-flow statement reports $4,491 million of operating
cash flow and $3,174 million of cash capital expenditures. Its non-GAAP
reconciliation divides the latter into $2,217 million of minesite sustaining
capital, $924 million of project capital, and $33 million of capitalized
interest; the three amounts sum to the audited total.[1][4]

| Barrick 2024 bridge, $ millions | Amount | Protocol treatment |
|:--|--:|:--|
| Audited PP&E cash capex | 3,174 | Reconciliation base. |
| Capitalized interest | (33) | Excluded financing item under the WGC rule.[6] |
| Eligible operating-asset capex | 3,141 | Maximum before project classification. |
| Issuer-labeled project capex | (924) | Potential expansion exclusion; not independently reproduced. |
| Issuer-labeled sustaining capex | 2,217 | Reported reference, not validated ground truth. |
| Audited depreciation | 1,915 | Comparison case only. |

Barrick identifies major growth activity, including the Lumwana Super Pit
Expansion, Goldrush ramp-up, and Ren project, and reports equipment rebuilds,
capitalized stripping, mine development, tailings, and plant-throughput work
among site spending.[4] These descriptions are directionally consistent with
the WGC distinction. The public report checked here does not provide a complete
project-by-project dollar map that permits an independent analyst to reconstruct
all $924 million without using Barrick's own category.

Applying the strict refusal rule gives **indeterminate**. If Barrick's
reconciled category is accepted as a lower anchor rather than independent proof,
the visible sensitivity interval is $2,217-$3,141 million. Its width is $924
million, versus $1,259 million between depreciation and total capex, a 26.6%
reduction. That apparent information gain is conditional on trusting the
issuer's project label and therefore does not satisfy the blinded acceptance
criterion.

Owner-earnings sensitivity using operating cash flow is:

| Barrick 2024 case, $ millions | Maintenance-capex deduction | CFO less deduction |
|:--|--:|--:|
| Depreciation proxy | 1,915 | 2,576 |
| Disclosed sustaining category | 2,217 | 2,274 |
| Eligible-capex upper case | 3,141 | 1,350 |
| Total-capex conservative case | 3,174 | 1,317 |

The $1,350-$2,274 conditional interval is economically material. It demonstrates
why the classification matters but not that the lower endpoint is independently
correct.

### 3. Lindsay Corporation: mixed purposes without allocations

Lindsay's fiscal 2025 filing reports $132.910 million of operating cash flow and
$42.496 million of PP&E purchases. It reports $20.896 million of depreciation
and amortization and $14.6 million of PP&E depreciation. Fiscal 2025 capex was
$38.026 million in Irrigation and $4.147 million in Infrastructure.[2]

The same filing forecasts fiscal 2026 capex of $50-$55 million and names four
purposes: equipment replacement, productivity improvements, new-product
development, and commercial-growth investments. It does not allocate dollars
among those purposes.[2] The forecast therefore identifies both maintenance and
growth motives but does not quantify a current-year bridge.

The result is **indeterminate**. Replacement is a maintenance signal;
new-product and commercial-growth spending are growth signals; productivity
work can preserve competitiveness, reduce costs, or expand effective capacity.
Without dollar allocations, neither a direct lower bound nor a defensible
exclusion can be reconstructed.

| Lindsay fiscal 2025 comparison, $ millions | Deduction | CFO less deduction |
|:--|--:|--:|
| PP&E depreciation proxy | 14.600 | 118.310 |
| Depreciation and amortization proxy | 20.896 | 112.014 |
| Total-capex case | 42.496 | 90.414 |

The $27.896 million spread between PP&E depreciation and total capex remains
unresolved. The disclosure-first protocol prevents false precision but adds no
quantified information beyond the two simple cases.

### 4. Adobe: asset-light reporting exposes a boundary of the method

Adobe's fiscal 2025 filing reports $10,031 million of operating cash flow, $179
million of PP&E purchases, $236 million of PP&E depreciation and amortization,
and net PP&E of $1,873 million versus $1,936 million one year earlier.[5] The
filing calls the expenditures ongoing capital expenditures but supplies no
maintenance/growth purpose split.[5]

The result is **indeterminate**. Total PP&E purchases are below PP&E
depreciation, so depreciation cannot be treated mechanically as a lower bound
on current cash capex. The two simple owner-earnings cases are $9,852 million
using total capex and $9,795 million using depreciation. The reversal is not
proof of underinvestment: asset mix, useful lives, timing, disposals, and
replacement prices can produce it.

Adobe also demonstrates a scope boundary. Organic software development,
customer acquisition, and other intangible-preservation spending may be
expensed and already reduce operating cash flow rather than appear in PP&E
capex. Morgan Stanley's review of the Peddireddy method identifies inconsistent
accounting for organic versus acquired intangibles as its largest limitation and
also notes useful-life asymmetry and changes in acquisition accounting.[10]
Therefore a PP&E-only protocol must not claim to measure all spending needed to
maintain an asset-light company's competitive position.

### 5. Cross-case findings

| Acceptance question | Result | Evidence |
|:--|:--|:--|
| Can every audited capex base be reconstructed? | Yes. | All three filings provide cash capex totals.[2][4][5] |
| Can acquisitions, leases, interest, and repairs be kept separate? | Yes in principle; case disclosure varies. | WGC exclusions and filing cash-flow lines support the bridge.[2][4][6] |
| Can a management sustaining split be arithmetically reconciled? | Yes for Barrick. | $2,217m + $924m + $33m = $3,174m.[4] |
| Can that split be reproduced independently and blind? | Not established. | Project-level amounts were incomplete and reference exposure occurred first. |
| Can mixed-purpose industrial capex be bounded? | No. | Lindsay names purposes but does not allocate amounts.[2] |
| Can an opaque asset-light case be bounded? | No. | Adobe supplies totals but no purpose split; intangible upkeep is largely outside PP&E.[5][10] |
| Does the protocol improve on depreciation and total-capex cases? | Not generally established. | Conditional narrowing occurred only by accepting Barrick's issuer label. |
| Does the refusal rule work? | Yes. | Lindsay and Adobe remain indeterminate without fabricated allocations. |

**Known:** audited totals can be reconciled; sector guidance can standardize
what should be included; direct issuer splits can be made traceable; and missing
purpose allocations are common in the three-case sample.

**Inferred:** a common protocol is more reliable as a disclosure audit and
refusal mechanism than as a universal estimator. Its strongest contribution is
showing exactly which amount cannot be classified, not producing a narrower
number in every case.

**Unknown:** inter-rater reproducibility, performance over a larger sector
sample, whether project-level filings can support a true blind test, and whether
later operating outcomes validate any inferred range.

## Alternatives and Implications

### Existing and smaller alternatives

1. **Do nothing beyond two sensitivities.** Use depreciation and total capex as
   transparent cases. This is simple and avoids unsupported allocations, but the
   resulting interval can be decision-relevant, as Barrick and Lindsay show.
2. **Adopt a disclosure-audit checklist only.** Reconcile audited capex, list
   direct classifications, isolate mixed amounts, and return indeterminate. The
   evidence supports this smaller change now. It improves traceability without
   claiming estimation precision.
3. **Use sector-specific conventions.** The WGC framework is useful for mining
   because it defines sustaining and non-sustaining categories and exclusions.[6]
   Its application still depends on issuer project judgments and does not
   transfer automatically to industrial or software businesses.
4. **Use a statistical estimator.** Peddireddy's 2021 dissertation estimates
   five-year capacity cost by industry and applies the estimated cost-to-sales
   relation to current sales. Its 1974-2016 sample contains 109,252 firm-years;
   median estimated maintenance capex exceeded D&A by 25%, and the study tests
   links with later write-offs, earnings, and returns.[7] This is an empirical
   benchmark, not a source-to-project bridge. It requires historical panel data,
   industry estimation, and assumptions that are difficult for intangibles and
   acquisition accounting.[10]
5. **Require one universal project allocator.** The three cases do not support
   this option. Mining, industrial manufacturing, and software expose different
   asset, disclosure, and accounting boundaries.

Under Buffett and Munger criteria, an estimate should be no more precise than
the underlying business evidence. A framework that narrows uncertainty by
accepting a management label without an independent operating check weakens the
margin of safety rather than strengthening it. The evidence supports preserving
simple downside cases and widening the uncertainty interval when the business
cannot be understood from public disclosures.

The evidence does not support a proposal for a universal maintenance-capex
estimator at this stage. It does support evaluation of a smaller, sector-aware
**auditable classification and refusal protocol** with three explicit outputs:
`bounded`, `issuer-indicated but not independently validated`, or
`indeterminate`. A bounded result should require a project-level dollar map and
an independent second classification.

## Response to Feedback and Remaining Questions

No prior evaluation or review exists for this first research report, so there
are no prior findings to answer.

Blocking issues for evaluation:

1. A strict blind test was not completed. Reopening the empirical test would
   require pre-registration of the classification rules and an independent
   classifier who has not seen the issuer's sustaining result.
2. Inter-rater reproducibility is unknown. The same source package must be
   classified by at least two independent readers before a range can be called
   repeatable.
3. Barrick did not provide a complete project-level amount map in the checked
   report; its reconciled split is traceable but not independently reproduced.
4. The protocol does not capture expensed intangible maintenance separately
   from operating expenses. This limits claims about competitive-position
   maintenance for asset-light businesses.
5. Three cases are sufficient to expose failure modes, not to establish sector
   coverage or external validity.

Decision-relevant next questions are whether the smaller disclosure-audit
protocol is worth proposing without an estimator, whether a bounded revision
should perform the missing blinded test, and what minimum project-level
disclosure should be required before a result changes from `indeterminate` to
`bounded`.

Confidence is medium. Primary filings, a sector guidance document, an SEC staff
correspondence record, Brain prior work, and an empirical dissertation were
checked. Confidence is limited by the failed blind-validation condition, the
three-company sample, incomplete project-level amounts, and the untested
reproducibility of judgmental classifications.

## Sources

[1] https://www.sec.gov/Archives/edgar/data/756894/000119312525054500/d910692d40f.htm
[2] https://www.sec.gov/Archives/edgar/data/836157/000119312525248751/lnn-20250831.htm
[3] https://www.berkshirehathaway.com/letters/1986.html
[4] https://s25.q4cdn.com/322814910/files/doc_financial/quarterly_results/2024/q4/Barrick_Q4_2024_MD-A.pdf
[5] https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm
[6] https://www.gold.org/sites/default/files/documents/wgc_guidance_on_non-gaap_metrics.pdf
[7] https://business.columbia.edu/sites/default/files-efs/imce-uploads/CEASA/Events%20Page/estimating-maintenance-capex.pdf
[8] https://www.sec.gov/about/divisions-offices/division-corporation-finance/financial-reporting-manual/frm-topic-9
[9] https://www.sec.gov/Archives/edgar/data/1030192/000165495425006890/filename1.htm
[10] https://www.morganstanley.com/im/publication/insights/articles/article_underestimatingtheredqueen.pdf
