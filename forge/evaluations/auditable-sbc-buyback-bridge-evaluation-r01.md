---
name: auditable-sbc-buyback-bridge-evaluation
id: 20260921T123909Z
tier: evaluation
pipeline: 20260921T114301Z
author: Analyst
tags: [stock-based-compensation, share-repurchases, owner-earnings, evaluation]
links:
  - forge/research/auditable-sbc-buyback-bridge-r01.md
  - forge/ideas/auditable-sbc-buyback-bridge-r01.md
  - agentic-brain:library/value-investing/capital-allocation.md
  - https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm
  - https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm
  - https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm
confidence: high
---
# Evaluation: Auditable SBC and Buyback Bridge

## Target and Baseline

Target: `forge/research/auditable-sbc-buyback-bridge-r01.md`, ID
`20260921T121424Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the drafting session's private
reasoning. No prior corrective verdict or human budget extension exists for
pipeline `20260921T114301Z`.

The following baseline was recorded before the target body was opened.

Expected evidence:

- a frozen accounting boundary and separate expense, award-settlement, and
  repurchase-cash ledgers;
- three recent U.S. issuer cases with source-pinned point-share roll-forwards,
  cash inputs, and reproducible arithmetic;
- separation of point-in-time shares from weighted diluted shares and no
  additive use of the expense and cash-neutralization views;
- two independent readers using the same frozen rules and source package, with
  each output, rationale, and unresolved item preserved before comparison;
- a direct comparison with the simpler recognized-SBC-plus-net-share-count
  rule; and
- evidence that any richer bridge changes a decision-relevant classification
  or range without inferring repurchase-dollar attribution absent disclosure.

Failure conditions were an unreconciled material share flow, untraceable
filing inputs, double counting of SBC, unsupported dollar attribution,
unpreserved or materially inconsistent reader outputs, no incremental
information over the simple rule, or suppression of an `indeterminate`
result. These conditions follow the root idea's explicit acceptance and stop
tests.[2]

## Findings

### Groundedness and primary-source checks

The material filing figures and arithmetic are grounded.

- Adobe reports about 441 million beginning and 413 million ending shares,
  30.8 million shares repurchased for USD 11,281 million, 3.6 million restricted
  stock units released, 0.1 million performance shares released, and 1.1
  million ESPP shares purchased. Its equity statement reports 3 million net
  treasury shares reissued under compensation plans. The target's implied 1.8
  million withheld shares and 413.2 million expected ending balance are
  therefore transparent approximations within the filing's whole-million
  rounding, not direct disclosures. Adobe also reports USD 10,031 million of
  operating cash flow, USD 179 million of PP&E purchases, USD 1,942 million of
  SBC, USD 475 million of award-withholding tax cash, and USD 348 million of
  treasury-stock proceeds.[3]
- Workday reports every share term used by the target: 266.352 million
  beginning shares, 7.869 million employee-plan shares, 2.700 million withheld
  shares, 0.382 million other shares, 12.772 million repurchased shares, and
  259.131 million ending shares. It also reports USD 2,939 million of operating
  cash flow, USD 162 million of capital expenditure, USD 1,626 million of SBC,
  USD 616 million of withholding-tax cash, USD 192 million of employee-plan
  proceeds, and USD 2,895 million of repurchase cash.[4]
- Snowflake reports 333.865 million beginning and 343.918 million ending shares.
  Its equity statement supplies the target's 7.880 million option shares, 0.817
  million ESPP shares, 9.453 million vested RSU shares, 3.291 million withheld
  shares, 0.082 million acquisition shares, 4.925 million repurchased shares,
  and 0.037 million treasury shares reissued. It also reports USD 1,221.942
  million of operating cash flow, USD 101.628 million of PP&E purchases, USD
  1,599.547 million of SBC, USD 672.867 million of withholding-tax cash, USD
  172.253 million of employee-plan proceeds, and USD 873.537 million of
  repurchase cash.[5]

Independent recalculation reproduced Workday's 259.131 million ending shares
and Snowflake's 343.918 million ending shares exactly. The point-share changes
are -7.221 million (-2.711074%) for Workday and +10.053 million (3.011097%) for
Snowflake. Adobe's rounded endpoints imply -28 million (-6.349206%). The
reported `OCF - capex - SBC` results also recalculate exactly: USD 7,910 million,
USD 1,151 million, and negative USD 479.233 million for Adobe, Workday, and
Snowflake, respectively.[3][4][5]

The three cash-flow statements add recognized SBC back to GAAP income when
deriving operating cash flow. Subtracting that add-back once restores the
recognized compensation charge in the target's narrow cash proxy. Keeping
award-withholding cash and repurchase cash in separate ledgers avoids charging
the same compensation transfer again. This is a transparent counting
convention, not a complete owner-earnings estimate; the target correctly notes
that its capex term is not normalized maintenance capex.[1][3][4][5]

The checked compensation, equity, cash-flow, and repurchase sections contain no
matched schedule that assigns specified repurchase dollars to specified award
shares. Adobe states that minimizing dilution is one program objective, but it
does not allocate particular shares or dollars. The target's refusal of
repurchase-dollar attribution is therefore supported for these three filings.
[3][4][5]

### Coverage, independence, and reproducibility

The issuer sample covers the three intended mechanical outcomes: two net share
reductions and one case where gross repurchases coexist with net dilution. The
filings are high-quality primary evidence for reported totals, but they are
three management-prepared disclosures and do not independently establish
management intent or a dollar allocation.[1][3][4][5]

The reproducibility claim is not auditable. The target states that two readers
worked in separate contexts and agreed on every classification, but it does not
preserve either reader's pre-comparison worksheet, cash bridge, rationale, or
unresolved-item list. At base commit
`b48b52a10ed6079e84d0555ef482667efdd377fe`, this pipeline contains only the
root idea and the consolidated research artifact. The research commit
`e890fce4d147f8ca303a04f593c0a8ce268cbf81` added no reader output. The report
therefore documents an assertion of agreement, not the root idea's required
preserved independent test.[1][2] Independent recalculation by this evaluation
supports the arithmetic, but it cannot retroactively establish the readers'
independence or pre-comparison outputs. This blocks advancement.

### Reasoning, alternatives, and usefulness

The report correctly separates three conclusions: share movements are
reconcilable, recognized SBC can be counted once, and dollar attribution remains
indeterminate. It also presents the simple alternative rather than forcing a
richer estimator.[1]

Two limitations prevent a proposal now.

First, the label `net capital return` overstates what a lower ending share count
establishes. A point-share reduction is a mechanical denominator result.
Whether a repurchase creates value for continuing owners also depends on price
relative to intrinsic value and alternative uses of cash.[6] The tested filings
support `net denominator reduction`; they do not by themselves establish
value-creating capital return.

Second, the detailed roll-forward produced the same three classifications as
the simple recognized-SBC-plus-net-share-count rule. This equality is largely
structural because the target defines the classification by the sign of the
endpoint change. The bridge adds an audit trail and could add a refusal trigger
when material flows do not reconcile, but all three selected cases reconcile.
No case demonstrates that the richer method changes a decision, an owner-
earnings range, or a refusal outcome. Auditability may justify a small checklist,
but the current evidence has not yet established that incremental use while the
required reader test is unpreserved.[1][2]

Confidence in this disposition is high. The three primary filings independently
confirm the material figures and the dollar-attribution limit, while the root
idea and repository record make the missing reproducibility evidence explicit.
Confidence would fall if dated, separate pre-comparison reader outputs were
recovered and showed that the preservation requirement was met, or would rise
further if a corrected blind test also demonstrated a decision change over the
simple rule.

## Verdict and Handoff

**Verdict: REVISE.**

**Exact next stage: `research`.**

This is the first corrective verdict in pipeline `20260921T114301Z`: 1 of 2
corrective cycles is now used. There is no human budget extension.

The revision must remain bounded to one reproducibility and usefulness test:

1. Freeze the source package, calculation rules, simple baseline, detailed
   bridge, classification names, and comparison criterion before either reader
   starts.
2. Give the same package to two readers in separate contexts. Preserve each
   unmerged roll-forward, cash bridge, classification, rationale, source pins,
   arithmetic, and unresolved items before exposing either reader to the other
   output. Include those separately preserved results in the revised research
   artifact or in resolving linked artifacts.
3. Use `net denominator reduction` and `dilution offset` for the mechanical
   share result. Do not call the former `net capital return` unless separate
   valuation evidence addresses repurchase price versus intrinsic value. Keep
   repurchase cash separate and retain `indeterminate` for award-dollar
   attribution.
4. Predefine the decision supplied by the simple rule and by the detailed
   bridge. Report whether the bridge changes a classification, owner-earnings
   range, or reconciliation/refusal result. If it adds only an audit trail,
   identify the concrete omission or error that the audit trail detects; do not
   manufacture incremental value.
5. Reuse the verified filing figures. Do not broaden the issuer sample or rerun
   the whole research project. If preserved blind outputs or incremental value
   remain unavailable, report that negative result for the next evaluation.

ADVANCE remains unavailable until the independent-reader evidence is preserved
and the proposed method's incremental use is demonstrated without unsupported
dollar attribution. A failed test is a valid result and may support reframe or
closure in the next evaluation.

## Learning Decision

After this evaluation is completed, the intended admission decision is to add
one method lesson to `LEARNINGS.md`: preserve dated pre-comparison rules and
separate reader outputs before claiming a blind or reproducible test. This
pipeline independently repeats the evidence-preservation failure observed in
pipeline `20260921T060750Z`, where an asserted off-repository freeze could not
establish its timing and no classifier outputs existed.[7] The lesson is
transferable, supported by two pipeline IDs, non-duplicative in the current
empty lessons section, and grants no governance or deployment permission.

## Sources

1. `forge/research/auditable-sbc-buyback-bridge-r01.md` -- exact research
   target, filing bridges, alternatives, reader-agreement claim, and limits;
   checked at base commit `b48b52a10ed6079e84d0555ef482667efdd377fe` and
   against its originating commit `e890fce4d147f8ca303a04f593c0a8ce268cbf81`.
   [high]
2. `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- root acceptance tests,
   preserved-reader-output requirement, alternatives, and stop conditions.
   [high]
3. Adobe Inc. "Annual Report on Form 10-K," fiscal year ended November 28,
   2025; Consolidated Statements of Stockholders' Equity and Cash Flows, Notes
   12 and 14. Share, SBC, settlement, repurchase, and purpose disclosures
   checked.
   https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm [high]
4. Workday, Inc. "Annual Report on Form 10-K," fiscal year ended January 31,
   2026; Consolidated Statements of Stockholders' Equity and Cash Flows, Note
   14. Share, SBC, settlement, and repurchase disclosures checked.
   https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm [high]
5. Snowflake Inc. "Annual Report on Form 10-K," fiscal year ended January 31,
   2026; Consolidated Statements of Stockholders' Equity and Cash Flows, Note
   12. Share, SBC, settlement, acquisition-issuance, and repurchase disclosures
   checked.
   https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm [high]
6. `agentic-brain:library/value-investing/capital-allocation.md` -- repurchase
   value depends on price versus intrinsic value, while net share count exposes
   the SBC dilution treadmill. [medium]
7. `forge/evaluations/auditable-maintenance-capex-evaluation-r02.md` --
   historical evaluation at Git commit
   `a88424a57f949a66996b6fb03d06c674087ec7c6`; the asserted off-repository
   pre-selection freeze lacked an immutable linked record and no classifier
   outputs existed in pipeline `20260921T060750Z`. [high]
