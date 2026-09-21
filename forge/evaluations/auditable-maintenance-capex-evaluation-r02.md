---
name: auditable-maintenance-capex-evaluation
id: 20260921T083622Z
tier: evaluation
pipeline: 20260921T060750Z
author: Analyst
links:
  - forge/research/auditable-maintenance-capex-r02.md
  - forge/ideas/auditable-maintenance-capex-r01.md
  - forge/research/auditable-maintenance-capex-r01.md
  - forge/evaluations/auditable-maintenance-capex-evaluation-r01.md
  - agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md
  - agentic-brain:library/mathematics-statistics/experimental-design.md
  - agentic-brain:library/value-investing/intrinsic-value-estimation-methods.md
  - https://www.sec.gov/Archives/edgar/data/2809/000110465926014451/aem-20251231xex99d1.htm
  - https://www.teck.com/media/2025-Annual-Report.pdf
  - https://lundingold.com/site/assets/files/111721/lug_2025_annual_report_final_23apr.pdf
  - https://web.archive.org/web/20260414223700/https://www.newmont.com/investors/news-release/news-details/2026/Newmont-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Provides-2026-Guidance-and-Announces-Enhanced-Capital-Allocation-Framework/default.aspx
  - https://s204.q4cdn.com/896213035/files/doc_financials/2025/ar/FSC-00000129-Kinross-AR-bookmark_eProofHR.pdf
tags: [maintenance-capex, owner-earnings, evaluation, reproducibility]
confidence: medium
---
# Evaluation: Auditable Maintenance-Capex Blind-Validation Correction

## Target and Baseline

Target: `forge/research/auditable-maintenance-capex-r02.md`, ID
`20260921T081621Z`.

The target author is Researcher. This evaluation was performed by Analyst in a
separate cron context that did not inherit the drafting session's private
reasoning. The prior REVISE verdict, ID `20260921T074024Z`, used corrective
cycle 1 of 2. No human budget extension exists.

The following baseline was recorded before the target body was opened.

Expected evidence:

- classification rules and an agreement criterion frozen before case selection
  and before any classifier sees an issuer sustaining/project result;
- a documented, bounded search for a public case with enough project-level
  dollars to reconcile independent classifications to audited capital
  expenditure;
- if a case qualifies, at least two independent classifiers in separate
  contexts using the same label-free package, with outputs and rationales
  preserved before comparison with the issuer reference;
- an exact audited exhibit and pinpoint primary sources for project amounts and
  the issuer reference;
- a complete bridge identifying acquisitions, leases, capitalized interest,
  capitalized software, working capital, and expensed repairs as included,
  excluded, absent, or unresolved;
- independently derived bounds and an information-gain comparison against
  depreciation and total capex; and
- if no case qualifies, issuer-by-issuer exclusion evidence establishing only
  bounded search unavailability, not universal unavailability.

Failure conditions were reference exposure before classification, non-
independent classifiers, incomplete project-dollar data, an unreconciled base,
a reproducibility claim without two completed blind classifications, a no-
double-counting claim without item-level evidence, information gain obtained
from an issuer label, missing evidence treated as proof, or a five-issuer result
generalized beyond its sample.

The decision rule was to ADVANCE only if performed independent evidence
supported a useful range or clearly superior classification decision without
circular reliance on an issuer reference. A failed bounded search could support
reframe or closure, but not ADVANCE. A second correction would exhaust cycle 2
of 2.

## Findings

### Groundedness and independent source checks

The main reported figures and arithmetic are grounded in the checked primary-
source passages:

- Agnico Eagle reports $931.198 million of sustaining capital and $1,141.754
  million of development capital under issuer-supplied headings. They sum to
  $2,072.952 million. The checked table supports the report's circularity
  concern: the dollar map is presented with the classification being tested.[1]
- Teck reports $1,838 million of PP&E expenditures, including $1,021 million of
  sustaining, $801 million of growth, and $16 million of corporate capital.
  The named sustaining amounts sum to $830 million and leave $191 million; the
  named growth amounts sum to $644 million and leave $157 million. The reported
  $348 million residual therefore recalculates exactly. Teck also reports $224
  million of capitalized stripping separately from PP&E expenditures.[2]
- Lundin Gold reports $60.268 million of sustaining and $20.889 million of non-
  sustaining expenditure, totaling $81.157 million.[3] Contrary to the target's
  statement that the named projects have no individual dollar amounts, the
  annual report states that $24.5 million was spent on the fifth tailings-dam
  raise. This leaves $56.657 million without an independently checked complete
  project-purpose map, so the selection failure remains, but the source summary
  is overstated and must not be repeated in the reframe.[3]
- Newmont reports $3,035 million of 2025 capital expenditure. The checked
  official archived release also states that a site- or project-basis
  reconciliation for the related non-GAAP measure is unavailable without
  unreasonable effort. The release supports a missing complete project bridge,
  while the 2026 sustaining/development guidance cannot validate the 2025
  classification.[4]
- Kinross reports $1,194.2 million of capital expenditures and $1,175.2 million
  on an attributable basis. Its attributable sustaining and non-sustaining
  amounts, $587.8 million and $587.4 million, sum to $1,175.2 million. The $19.0
  million difference from the cash-capex total is confirmed by the source's
  ownership treatment, and the full site-category amounts of $606.8 million and
  $587.4 million sum to $1,194.2 million.[5]

These checks establish the cited positive figures, category dependence, and
specific residual or perimeter mismatches. They do not establish an exhaustive
absence of every project amount in five long reports. The Lundin contradiction
shows why the bounded result should be stated as "no complete label-free package
was demonstrated in the checked sample," not as a comprehensive source-
availability finding.

### Coverage, independence, and reasoning

The target makes the decisive negative result explicit: no package passed its
selection gate, no package went to classifiers, and no blind classification,
inter-rater concordance, independent bound, or information-gain calculation was
performed. That is an honest unavailable test. It cannot satisfy the root idea's
blind-reproduction acceptance condition and blocks ADVANCE.

The target also limits the result to five mining issuers and identifies wider
issuer searches, technical reports, and non-public project ledgers as unknown.
It therefore avoids converting missing evidence into proof of universal
unavailability. This limitation is correct.

Two method weaknesses remain:

1. The claimed `2026-09-21T08:02:05Z` freeze occurred outside the repository,
   but no immutable record or linked output preserves the pre-selection rules,
   search order, or exposure history. Reproducing those rules in the completed
   report does not independently establish when they were fixed. This does not
   turn the negative screen into a passed blind test.
2. The five-package selection is bounded but not systematic enough for an
   availability-rate claim: the target gives the order and eligibility gate,
   but not a defined issuer universe, sampling rule, or complete search ledger.
   Its conclusion is valid only for the reported screen.

The requested no-double-counting matrix remains unperformed because there is no
validation case. The target correctly labels acquisitions, leases, capitalized
interest, software, working capital, and expensed repairs as unvalidated rather
than absent. Teck's separate stripping line and Kinross's lease and interest
lines demonstrate why the matrix would matter, but they do not validate a
project classification.[2][5]

The Brain prior work already requires a transparent bridge from audited cash
flow, separate treatment of acquisitions and financing effects, and maintenance-
versus-growth judgment based on operating evidence rather than management
labels
[`agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md`].
A smaller Forge output therefore needs a demonstrated delta from that existing
method. Merely restating reconciliation and refusal would duplicate prior work.

### Alternatives and usefulness

The evidence does not justify a universal maintenance-capex estimator. It also
does not justify another autonomous search cycle: the performed correction was
bounded, its key validation test remained unavailable, and one source summary
was materially overbroad.

A narrower disclosure-audit and refusal checklist may still be useful. The five
cases show concrete failure modes: issuer-label circularity, unmapped residuals,
noncomparable ownership perimeters, separate capitalized items, and an honest
`indeterminate` output. This is a different question from estimating a
maintenance-capex range and must be ideated as such before proposal work.

## Verdict and Handoff

**Verdict: REFRAME.**

**Exact next stage: `ideate`.**

This REFRAME is the second corrective verdict in pipeline
`20260921T060750Z`: the prior REVISE and this REFRAME use 2 of 2 corrective
cycles. No human budget extension exists. A later evaluation or final review
cannot authorize another REVISE or REFRAME; if another correction would be
required, the protocol requires DEFER unless Suggi records an explicit bounded
extension.

The reframed ideation must:

1. Ask whether a disclosure-audit and refusal checklist can improve traceability
   over the existing Brain normalized-cash bridge without claiming that it
   estimates maintenance capex.
2. Preserve the same pipeline ID and treat the five-issuer screen as bounded
   evidence only.
3. Correct the Lundin source statement and distinguish a missing complete map
   from an absence of all project-level amounts.
4. Define the proposed delta, user, output, and stop condition before research.
   Candidate outputs may distinguish `issuer-indicated`, independently
   `bounded`, and `indeterminate`, but no status may imply validation that was
   not performed.
5. Compare the candidate directly with
   `agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md`
   and reject a duplicate checklist.

REFRAME is not approval to propose or implement the checklist. The ideation
stage must decide whether the narrower question is genuinely useful within the
exhausted correction budget.

## Learning Decision

`LEARNINGS.md` remains unchanged. The source-pinning, pre-registration, and
negative-search observations still come from one pipeline. The repeated
independent-pipeline evidence required for a reusable Forge method lesson is
absent.

## Sources

[1] https://www.sec.gov/Archives/edgar/data/2809/000110465926014451/aem-20251231xex99d1.htm - Agnico Eagle 2025 results exhibit
[2] https://www.teck.com/media/2025-Annual-Report.pdf - Teck 2025 Annual Report
[3] https://lundingold.com/site/assets/files/111721/lug_2025_annual_report_final_23apr.pdf - Lundin Gold 2025 Annual Report
[4] https://web.archive.org/web/20260414223700/https://www.newmont.com/investors/news-release/news-details/2026/Newmont-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Provides-2026-Guidance-and-Announces-Enhanced-Capital-Allocation-Framework/default.aspx - Newmont 2025 results release archived 2026-04-14
[5] https://s204.q4cdn.com/896213035/files/doc_financials/2025/ar/FSC-00000129-Kinross-AR-bookmark_eProofHR.pdf - Kinross 2025 Annual Report
