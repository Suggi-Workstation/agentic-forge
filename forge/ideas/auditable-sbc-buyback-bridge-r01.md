---
name: auditable-sbc-buyback-bridge
id: 20260921T114301Z
tier: idea
pipeline: 20260921T114301Z
author: Analyst
tags: [stock-based-compensation, share-repurchases, owner-earnings, capital-allocation]
links:
  - agentic-brain:library/value-investing/capital-allocation.md
  - agentic-brain:library/finance/dividend-policy-and-share-buybacks.md
  - agentic-brain:library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md
  - agentic-brain:library/case-studies/berkshire-apple-investment-consumer-loyalty.md
  - https://experts.arizona.edu/en/publications/when-a-buyback-isnt-a-buyback-open-market-repurchases-and-employe
  - https://www.sec.gov/files/corpfin/pre-amendment-item-703.pdf
  - https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/01215202/a54gu6y5tegrrf.pdf
confidence: medium
---
# Auditable SBC and Buyback Bridge

## Question and Value

Can a public-filings-only bridge, applied independently by two readers to three
U.S. issuers, separate stock-based-compensation dilution from genuine
share-repurchase capital return while counting the compensation cost only once
in owner earnings?

The output would serve value investors who must distinguish cash returned to
continuing owners from cash used to prevent equity awards from diluting them.
Brain guidance already says that stock-based compensation is an economic cost,
that gross buybacks can mask employee-option dilution, and that net share count
matters more than an authorization headline.[1][2][3] The unresolved practical
problem is how to combine the compensation expense, award-related share flows,
withholding-tax payments, and repurchases without either calling compensation
free or deducting the same transfer twice.

The provisional hypothesis is that a source-pinned share and cash roll-forward
can classify each case as `net capital return`, `dilution offset`, or
`indeterminate`. It should keep two outputs separate: normalized owner earnings
and capital returned to continuing owners. A credible alternative is that no
issuer-level attribution is needed: deduct a consistent stock-compensation cost
once, track net diluted share count, and treat all repurchases separately as a
financing decision. Under that alternative, assigning repurchase dollars to
specific employee awards creates false precision.

The idea is not worth pursuing if the public filings cannot reconcile the
material share flows, if independent readers cannot reproduce the same
classification, or if the bridge provides no decision-relevant information
beyond the simpler expense-plus-net-share-count rule.

## Origin and Prior Work

This is direct ideation under ANCHOR Path B, value-investing systems. The
current Forge graveyard, idea, and proposal directories were enumerated. At base
commit `bcb3652564419f33f41975e36abfbeedeca173be`, the STATUS board
contained no open pipeline, and active and archived progress logs contained no
proposal decision. Git history contained one prior artifact family, auditable
maintenance capex, which concerns asset-maintenance spending rather than equity
compensation or payout authenticity.[8][9] Searches for
`stock-based compensation`, `share-based compensation`, `buyback`,
`repurchase`, `dilution`, and `double count` found no Forge artifact or
proposal covering this question. No explicit accepted, pending, changed,
deferred, or rejected proposal decision exists for it.

The Brain contains four close but incomplete precedents. `capital-allocation.md`
recommends evaluating buybacks through the net fully diluted share count and
warns that repurchases can offset stock compensation.[1]
`dividend-policy-and-share-buybacks.md` makes the same authenticity test and
cites evidence that employee options affect repurchase behavior.[2]
`non-gaap-metrics-and-pro-forma-manipulation.md` treats stock compensation as a
real cost and rejects routine exclusion from economic earnings.[3] The Apple
case study measures denominator reduction and repurchase effects on continuing
ownership, but it does not attribute repurchase cash to employee awards or
build a no-double-counting owner-earnings bridge.[4]

The external evidence establishes the problem, not the proposed solution.
Kahle found that repurchase amounts were positively related to exercisable
employee options and interpreted the result as consistent with funding option
exercises.[5] SEC Item 703 requires issuers to report repurchased shares,
average price, publicly announced plan purchases, and remaining authorization,
but it does not require an employee-award attribution.[6] Adobe's fiscal 2025
release separately reports stock-based compensation in operating cash flow,
common-stock repurchases, and cash paid for net settlement of equity awards; it
also excludes stock-based compensation from its non-GAAP measures.[7] Those
separate lines show why a bridge may be feasible, but they do not by themselves
show which repurchases offset awards or how to count the economic cost once.
The unresolved difference is therefore a reproducible issuer-level
reconciliation and refusal rule, not another statement that dilution matters.

## Research Plan

Use one bounded validation unit:

1. Freeze the accounting boundary before selecting cases. Start from beginning
   and ending common shares and reconcile award issuance or vesting, option
   exercises, employee tax withholding, issuer repurchases, acquisitions, and
   other equity issuance. Keep weighted diluted shares separate from
   point-in-time shares.
2. Define two non-additive cost views before seeing results: an expense view
   anchored to recognized stock-based compensation, and a cash-neutralization
   view anchored to documented award-related share flows and repurchases. Never
   subtract both as though they were independent costs. Return `indeterminate`
   when disclosure cannot connect the views.
3. Select three recent U.S. issuers with material stock compensation and
   repurchases: one that explicitly names dilution offset as an objective, one
   high-stock-compensation issuer, and one case where gross repurchases produce
   little or no net share reduction. Use Form 10-K, equity and compensation
   footnotes, cash-flow and stockholders' equity statements, Item 703 tables,
   and proxy disclosures. Do not use management intent as an allocation rule.
4. Give the same source package and frozen rules to two readers in separate
   contexts. Preserve both share roll-forwards, cash bridges, classifications,
   rationales, and unresolved differences before comparison.
5. Compare the result with the simpler alternative: count stock compensation
   once using the stated expense convention, report net share-count change,
   and evaluate gross repurchases separately. Test whether the bridge changes
   the classification of capital return or the owner-earnings range without an
   unsupported allocation.
6. Stop rather than propose if no case reconciles, material reader disagreement
   remains, or the richer bridge adds no information. Doing nothing beyond the
   simple rule is the default alternative.

Acceptance requires source-pinned arithmetic for every material share and cash
movement, no double counting across the two cost views, agreement by both
readers on each final classification or an explicit `indeterminate`, and a
clear comparison with the simple baseline. It does not require an affirmative
result.

Confidence is medium. The Brain sources, a peer-reviewed empirical study, SEC
repurchase disclosure requirements, and a current issuer release establish a
real measurement problem and plausible public inputs.[1][2][3][5][6][7]
Confidence is limited because no three-issuer bridge or independent
reproduction has yet been performed, and repurchase intent may remain
unobservable even when all reported totals reconcile.

## Sources

1. `agentic-brain:library/value-investing/capital-allocation.md` -- share
   repurchases and the stock-compensation treadmill. [medium]
2. `agentic-brain:library/finance/dividend-policy-and-share-buybacks.md` --
   evaluating payout quality and employee-option dilution. [medium]
3. `agentic-brain:library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md` --
   stock-based compensation and recurring exclusions. [medium]
4. `agentic-brain:library/case-studies/berkshire-apple-investment-consumer-loyalty.md` --
   repurchases, denominator reduction, and public-filing boundaries; reviewed
   2026-09-20. [medium]
5. Kahle, Kathleen M. "When a Buyback Isn't a Buyback: Open Market
   Repurchases and Employee Options," Journal of Financial Economics 63(2),
   2002, pp. 235-261. Abstract and bibliographic record checked for the tested
   relation between employee options and repurchases.
   https://experts.arizona.edu/en/publications/when-a-buyback-isnt-a-buyback-open-market-repurchases-and-employe [high]
6. U.S. Securities and Exchange Commission. "Item 703: Purchases of Equity
   Securities by the Issuer and Affiliated Purchasers," required table and
   instructions for repurchase counts, prices, plans, and remaining authority.
   https://www.sec.gov/files/corpfin/pre-amendment-item-703.pdf [high]
7. Adobe Inc. "Adobe Reports Record Q4 and FY2025 Revenue," fiscal 2025
   release, cash-flow and GAAP-to-non-GAAP tables. Checked the separately
   reported stock-compensation, repurchase, and equity-award settlement lines;
   the condensed financial statements are identified as unaudited.
   https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/01215202/a54gu6y5tegrrf.pdf [medium]
8. `forge/ideas/auditable-maintenance-capex-r01.md` -- historical root idea
   checked as the only prior Forge idea family and a different accounting
   question, at Git commit a88424a57f949a66996b6fb03d06c674087ec7c6. [high]
9. `STATUS.md` -- open work before selection, at base Git commit
   bcb3652564419f33f41975e36abfbeedeca173be. [high]
   - `logbook/progress.log` -- exact-proposal decisions in the same base
     snapshot. [high]
   - `logbook/archive/.gitkeep` -- archive placeholder in the same base
     snapshot. [high]
