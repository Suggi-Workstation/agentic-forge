---
name: auditable-maintenance-capex-research
id: 20260921T081621Z
tier: research
pipeline: 20260921T060750Z
author: Researcher
links:
  - forge/ideas/auditable-maintenance-capex-r01.md
  - forge/research/auditable-maintenance-capex-r01.md
  - forge/evaluations/auditable-maintenance-capex-evaluation-r01.md
  - agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md
  - agentic-brain:library/accounting-financial-shenanigans/cookie-jar-reserves-and-expense-manipulation.md
  - agentic-brain:library/value-investing/intrinsic-value-estimation-methods.md
  - agentic-brain:library/valuation-screening/discounted-cash-flow-dcf-methodology.md
  - agentic-brain:library/value-investing/berkshire-annual-reports-1986-1995.md
  - https://www.sec.gov/Archives/edgar/data/2809/000110465926014451/aem-20251231xex99d1.htm
  - https://www.teck.com/media/2025-Annual-Report.pdf
  - https://lundingold.com/site/assets/files/111721/lug_2025_annual_report_final_23apr.pdf
  - https://web.archive.org/web/20260414223700/https://www.newmont.com/investors/news-release/news-details/2026/Newmont-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Provides-2026-Guidance-and-Announces-Enhanced-Capital-Allocation-Framework/default.aspx
  - https://s204.q4cdn.com/896213035/files/doc_financials/2025/ar/FSC-00000129-Kinross-AR-bookmark_eProofHR.pdf
tags: [maintenance-capex, owner-earnings, validation, reproducibility]
confidence: medium
---
# Auditable Maintenance-Capex Estimation: Blind-Validation Correction

## Question and Method

This revision addresses the bounded correction in
`forge/evaluations/auditable-maintenance-capex-evaluation-r01.md`: can one
recent public-company source package support a genuinely blind,
project-dollar maintenance-capex classification by two independent readers,
with an exact bridge to an audited capital-expenditure base and a withheld
issuer reference?

### Preserved source order and provisional explanation

At 2026-09-21T08:02:05Z, before the targeted issuer review, the following
provisional explanation and protocol were frozen outside the Forge working
tree. An independent result requires an audited cash-capex total or exact
PP&E additions and quantified project or purpose amounts that can be
classified without showing the issuer's sustaining-versus-growth answer.
Arithmetic reconciliation alone is insufficient. Missing project dollars,
material definition disagreement, or dependence on an issuer label requires
`indeterminate`.

The frozen rules were:

1. Start with the audited cash PP&E line or exact audited PP&E additions.
   Keep acquisitions, lease principal, working capital, expensed repairs,
   capitalized software, and capitalized interest separate.
2. Include in a direct maintenance lower bound only quantified replacement,
   rebuild, safety, environmental, or other spending explicitly needed to
   preserve current unit volume or competitive position.
3. Add mixed-purpose and unallocated eligible capex to the upper bound. Exclude
   only quantified projects that create a new operation or materially increase
   productive capacity.
4. Return `bounded` only if every eligible dollar is mapped and the bridge
   reconciles exactly. Otherwise return `indeterminate` and name the missing
   amount or definition.
5. Require two classifiers to agree on the decision. For a bounded result,
   require at least 80% dollar-weighted classification agreement and endpoint
   differences no greater than 10% of eligible capex. For an indeterminate
   result, require the same blocking omission or definition class.
6. Compare a bounded interval with the absolute depreciation-to-eligible-capex
   spread. If either classifier is indeterminate, quantified information gain
   is not established.

The case-selection rule limited the search to five recent annual-report
packages and required all three conditions before exposing classifiers: an
exact audited base, project- or purpose-level dollars capable of a complete
bridge, and a separately disclosed issuer reference that could be withheld.
The packages were reviewed in this order: Agnico Eagle, Teck, Lundin Gold,
Newmont, and Kinross. The issuer category totals were used only after checking
whether a label-free source package could be formed. No prior Barrick result or
first-report conclusion was given to a classifier because no package passed
selection.

The Brain index freshness check returned `OK` on 2026-09-21, and the query for
maintenance-capex blind classification returned the accounting and valuation
sources linked above. Their full-file conclusions remain unchanged: reconcile
capitalized assets and cash flows visibly; do not infer maintenance from a
capitalization label; and treat depreciation and total capex as comparison
cases rather than project evidence.

### Limitations

This is a bounded availability test, not proof that no public company can ever
support blind classification. It covers five recent mining issuers because
that sector commonly publishes sustaining-capital measures. Newmont's live
page was blocked by Cloudflare; the checked copy is the Wayback snapshot dated
2026-04-14 and is cited as an archived snapshot, not as a live page. Search
snippets selected documents but were not used as evidence where the underlying
annual report or results release was readable.

## Evidence and Findings

### Candidate-screen result

| Order | Package and checked result | Gate result |
|:--|:--|:--|
| 1 | Agnico Eagle's 2025 results release reports $2,072.952 million of non-GAAP capital expenditures, split into $931.198 million of sustaining and $1,141.754 million of development capital, with mine rows under those issuer headings.[3] | **Fail.** The mine dollars are disclosed inside the reference classification. Removing the headings removes the purpose classification, while the release does not provide a complete independent project-dollar schedule that recreates the total. The reference cannot be both withheld and used as the source map. |
| 2 | Teck's audited annual report reports $1,838 million of PP&E expenditures, $1,021 million of sustaining capital, $801 million of growth capital, and $16 million of corporate capital.[4] It separately identifies $611 million at QB, $123 million at Antamina, and $96 million at HVC within sustaining spending, and $330 million for HVC MLE, $187 million for Zafranal, and $127 million for Red Dog MLE within growth spending.[4] | **Fail.** The named amounts leave $191 million of sustaining and $157 million of growth spending without project-level dollar descriptions, or $348 million in total. The remaining dollars can be reconciled only by retaining Teck's issuer categories. |
| 3 | Lundin Gold's audited 2025 PP&E additions are $81.157 million. Its non-IFRS table reconciles $60.268 million of sustaining and $20.889 million of non-sustaining expenditures exactly to that amount.[5] The report names the tailings raise, camp and administration facilities, generators, mobile-equipment work, infrastructure, plant expansion, conversion drilling, permitting, and studies.[5] | **Fail.** The named projects have no individual dollar amounts. The only complete dollar map is the issuer's two-category reference itself. Withholding that answer leaves no reproducible allocation. |
| 4 | Newmont's 2025 results release reports GAAP cash-flow capital expenditures of $3,035 million and defines sustaining spending as necessary to maintain current production and the current mine plan.[6] Its appendix supplies selected site development expenditures but no complete project-dollar bridge for the $3,035 million base; the page checked here states that an individual site or project reconciliation is unavailable without unreasonable effort for a related non-GAAP reconciliation.[6] | **Fail.** Selected project and site amounts do not map every eligible capital dollar independently of Newmont's sustaining/development taxonomy. The 2026 guidance split is forward-looking and cannot validate 2025 actual classification. |
| 5 | Kinross's audited cash-capex total is $1,194.2 million, and its site table reconciles to that total.[7] Its reference split is on an attributable basis: $587.8 million sustaining plus $587.4 million non-sustaining equals $1,175.2 million.[7] | **Fail.** The audited and reference perimeters differ by $19.0 million because the site total includes 100% of Manh Choh while attributable measures include 70%. Site totals also combine multiple purposes. The report describes growth and maintenance drivers but does not assign all site dollars to those purposes without using the issuer split. |

The arithmetic was recomputed directly. Agnico's reference categories sum to
$2,072.952 million; Lundin Gold's sum to $81.157 million; Kinross's sum to
$1,175.2 million; and Kinross's perimeter difference is $19.0 million. For
Teck, the disclosed named sustaining projects sum to $830 million, leaving
$191 million; named growth projects sum to $644 million, leaving $157 million.

### Why no classifier outputs exist

No package passed the pre-specified selection gate. Running two classifiers on
one of these packages would require one of three invalid substitutions:

- disclose the issuer's category table and call agreement independent;
- omit unallocated dollars and falsely claim a complete reconciliation; or
- let classifiers assign unlabeled residuals without project evidence.

The frozen protocol prohibited all three. Consequently, no source package was
released to classifiers and no blind classification, inter-rater concordance,
or independently derived bound was produced. This is an unavailable test, not
a passed reproducibility result. It also means no information-gain calculation
is valid: the only narrower intervals in these packages depend on issuer
categories that the test was designed to withhold.

### No-double-counting correction

The evaluation requested an item-by-item matrix for the validation case. No
validation case exists, so such a matrix cannot be completed honestly. The
screen nevertheless found why a base alone is insufficient:

- Teck reports PP&E expenditure and capitalized stripping separately, but its
  project descriptions do not allocate every PP&E dollar.[4]
- Lundin Gold's non-IFRS categories reconcile to PP&E additions, while its cash
  investing outflow and VAT lines use different bases.[5]
- Kinross separately reports capitalized interest and lease obligations, but
  its issuer reference and audited total use different ownership perimeters.[7]

These checks prevent false reconciliation. They do not supply the missing
project-purpose dollars. Acquisitions, leases, capitalized interest,
capitalized software, working capital, and expensed repairs therefore remain
unvalidated at the project-classification level rather than being assumed
absent.

### Synthesis

**Known:** all five issuers disclose total capital measures and some
sustaining/development information. Teck and Kinross expose residual or
perimeter mismatches; Lundin Gold reconciles exactly but only through the
issuer category being tested. Agnico's mine rows and Newmont's selected project
amounts do not create an independent complete map.[3][4][5][6][7]

**Inferred:** public mining disclosure is adequate for auditing an issuer's
reported split more often than for reproducing it blind. A reconciliation is
not an independent classification when the same issuer table supplies both the
dollars and the labels.

**Unknown:** whether a wider issuer search, technical-report cost schedules, or
non-public project ledgers would yield a qualifying case; whether two readers
would agree if such a package existed; and whether an independently bounded
range would predict later maintenance needs.

This result contradicts the first report's hope that a disclosed project case
might be found quickly, but it supports that report's refusal rule. It neither
proves the issuer classifications wrong nor validates them.

## Alternatives and Implications

1. **Universal estimator.** The correction supplies no support. Advancing one
   would violate the root idea's stop condition because blind reproduction and
   independent information gain remain unavailable.
2. **Larger blind search.** Searching more issuers or technical reports could
   locate a qualifying package, but that is a new research unit. It would need
   a new bounded authorization rather than being represented as completed here.
3. **Disclosure-audit and refusal checklist.** This smaller option remains
   supported. It can reconcile totals, expose definition and perimeter changes,
   list missing project dollars, and return `indeterminate`. It must not be
   described as an estimator or as independently validated classification.
4. **Depreciation and total-capex sensitivities.** Doing nothing beyond these
   simple cases remains the most reproducible numerical alternative when
   project dollars are absent. The interval may be wide, but it does not hide
   issuer dependence.
5. **Issuer sustaining measures.** They can be reported as
   `issuer-indicated`, with reconciliation and definition checks. They are not
   ground truth and should not set a lower bound without independent evidence.

Under Buffett and Munger's owner-earnings framing, false precision is the worst
outcome. The evidence favors preserving a margin of safety through explicit
refusal, not narrowing the deduction by relabeling unknown capital.

## Response to Feedback and Remaining Questions

The five material evaluation findings are answered as follows:

1. **Freeze rules and exposure order:** completed. The protocol and provisional
   explanation were frozen at 2026-09-21T08:02:05Z before targeted issuer
   review and are reproduced above.
2. **Two independent classifiers:** blocked by the pre-specified selection
   gate. No eligible label-free package existed, so no classifier was exposed
   and no concordance is claimed.
3. **Complete project-dollar reconciliation:** unavailable in the bounded
   five-package search. The exact candidate failures and Teck's $348 million
   unmapped amount are documented above.
4. **Acquisitions, leases, interest, software, working capital, and repairs:**
   no validation-case matrix is claimed. Available separate lines and the
   unresolved project-level coverage are distinguished rather than treated as
   zero.
5. **Independent information gain and exact audited source:** no independent
   bound exists, so information gain is not computed. Teck, Lundin Gold, and
   Kinross figures are pinned to their annual reports; Newmont is pinned to a
   dated archive of its official results release; Agnico is pinned to its
   official results release. Audited figures and issuer non-GAAP categories are
   identified separately.

The blocking question for evaluation is whether this negative availability
result warrants `REFRAME` to a disclosure-audit/refusal checklist or `DEFER`
pending a source package with project-level dollars. The present evidence does
not warrant an estimator proposal.

Confidence is medium. The negative result is directly supported within the
bounded five-package sample and the arithmetic reconciles. Confidence is not
high because the search is sector-limited, one Newmont source was available
only as an archived snapshot, and public technical reports outside the bounded
unit may contain more granular cost schedules.

## Sources

[1] `forge/research/auditable-maintenance-capex-r01.md`

[2] `forge/evaluations/auditable-maintenance-capex-evaluation-r01.md`

[3] https://www.sec.gov/Archives/edgar/data/2809/000110465926014451/aem-20251231xex99d1.htm

[4] https://www.teck.com/media/2025-Annual-Report.pdf

[5] https://lundingold.com/site/assets/files/111721/lug_2025_annual_report_final_23apr.pdf

[6] https://web.archive.org/web/20260414223700/https://www.newmont.com/investors/news-release/news-details/2026/Newmont-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Provides-2026-Guidance-and-Announces-Enhanced-Capital-Allocation-Framework/default.aspx (official page archived 2026-04-14)

[7] https://s204.q4cdn.com/896213035/files/doc_financials/2025/ar/FSC-00000129-Kinross-AR-bookmark_eProofHR.pdf
