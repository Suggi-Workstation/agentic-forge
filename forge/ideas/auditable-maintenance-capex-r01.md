---
name: auditable-maintenance-capex
id: 20260921T060750Z
tier: idea
pipeline: 20260921T060750Z
author: Researcher
links:
  - agentic-brain:library/value-investing/berkshire-annual-reports-1986-1995.md
  - agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md
  - agentic-brain:library/value-investing/intrinsic-value-estimation-methods.md
  - agentic-brain:library/valuation-screening/discounted-cash-flow-dcf-methodology.md
  - agentic-brain:reflections/2026-09-14_neo_better-indicators-can-hide-worse-owner-outcomes.md
  - https://www.berkshirehathaway.com/letters/1986.html
  - https://www.sec.gov/Archives/edgar/data/836157/000119312525248751/lnn-20250831.htm
---
# Auditable Maintenance-Capex Estimation

## Question and Value

Can a disclosure-first, sector-aware protocol estimate a defensible range for
maintenance capital expenditure from public-company filings while explicitly
flagging cases in which owner earnings cannot be estimated reliably?

The direct beneficiaries are value investors and research agents that must
reconcile reported cash flow to cash distributable without impairing a
business. This serves ANCHOR path B: it would convert a load-bearing but
judgment-heavy owner-earnings input into a repeatable research framework, not
a security recommendation.

The question matters because Buffett defines owner earnings by deducting the
average annual capitalized expenditure required to maintain competitive
position and unit volume, while stating that this amount is a sometimes very
difficult guess [Berkshire 1986 letter]. The Brain already explains that the
estimate should use operating evidence and that valuation must make
reinvestment assumptions explicit
[agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md;
agentic-brain:library/valuation-screening/discounted-cash-flow-dcf-methodology.md].
A current filing illustrates the disclosure problem: Lindsay Corporation
places equipment replacement, productivity improvements, new-product
investment, and commercial-growth investment inside one expected capital-
expenditure range without allocating the range among those purposes [Lindsay
2025 Form 10-K].

Provisional hypothesis: an evidence hierarchy that begins with issuer
breakdowns, reconciles them to audited capital expenditure, and then uses
sector-specific operating signals can produce an auditable range more useful
than either depreciation or total capital expenditure alone. It should return
"indeterminate" when the evidence cannot support a narrower range.

Credible alternative: capital projects often serve maintenance, productivity,
compliance, and growth simultaneously, while management labels may be
self-serving. A common protocol may create false comparability; simple
sensitivity cases using depreciation and total capital expenditure may be more
honest.

The idea is not worth pursuing if a blinded test cannot reproduce disclosed
sustaining-capital ranges, if independent classification depends mainly on
unstated judgment, or if the protocol narrows uncertainty without improving
traceability. An inability to estimate is a valid result, not a missing output.

## Origin and Prior Work

This is direct ideation in the value-investing subject area, not reflection-led
discovery. The exact candidate and synonyms were searched through the fresh
agentic-brain hybrid index using "maintenance capital expenditures," "growth
capital expenditures," "owner earnings," "depreciation," "company filings,"
and "estimation framework." The top relevant files were read in full.

The Brain contains the following adjacent work:

- `agentic-brain:library/value-investing/berkshire-annual-reports-1986-1995.md`
  defines owner earnings, records why maintenance capital is imprecise, and
  compares depreciation with Scott Fetzer's estimated requirement. It does not
  provide or test a reusable evidence hierarchy.
- `agentic-brain:library/accounting-financial-shenanigans/cash-flow-shenanigans.md`
  requires a transparent normalized-cash bridge and warns that maintenance and
  growth labels need operating evidence. It does not specify how to bound the
  maintenance-capital component across disclosure regimes.
- `agentic-brain:library/value-investing/intrinsic-value-estimation-methods.md`
  and `agentic-brain:library/valuation-screening/discounted-cash-flow-dcf-methodology.md`
  show that maintenance capital affects EPV and DCF and that growth must be
  reconciled to reinvestment. Neither validates an estimation protocol.
- `agentic-brain:reflections/2026-09-14_neo_better-indicators-can-hide-worse-owner-outcomes.md`
  was surfaced by the query and read in full. It supports testing whether a
  favorable proxy preserves the owner outcome, but it neither estimates
  maintenance capital nor supplies an independent trial of this method. It is
  not counted as validation.

Duplicate scope covered all files in `forge/graveyard/`, `forge/ideas/`, and
`forge/proposals/`, plus active and archived progress logs. Those three artifact
folders contain no prior artifacts, the progress log contains no prior event,
and no archived progress log exists. Therefore there is no accepted, pending,
rejected, or deferred Forge proposal and no explicit human decision to cite.
A final synonym search over all Forge artifacts returned no maintenance-capex,
owner-earnings, free-cash-flow, or capital-expenditure match.

The unresolved difference is empirical and procedural: prior work explains why
the estimate matters, but it does not define and test a public-evidence method
that yields a range, preserves source-level judgments, and refuses estimation
when disclosures are inadequate.

## Research Plan

Questions that would change the decision:

1. Which filing signals distinguish replacement needed to preserve unit volume
   and competitive position from expansion, acquisition, productivity, and
   compliance spending without relying only on management labels?
2. Which signals are sector-specific, and which can be used across businesses?
3. Can the same cited inputs lead an independent evaluator to substantially the
   same range and to the same "estimable" or "indeterminate" decision?
4. Does the protocol add information beyond depreciation and total-capex
   sensitivity cases, or only add unsupported precision?
5. How do mixed-purpose projects, capitalized software, leases, acquisitions,
   inflation, deferred maintenance, and expensed repairs alter the bridge?

Use audited annual reports and property, plant, and equipment notes as primary
evidence; reconcile issuer capital-allocation disclosures and project lists to
the audited cash-flow total. Treat earnings calls and management-defined
sustaining-capital figures as claims requiring reconciliation, not ground
truth. Use asset age, capacity, unit volume, replacement cycles, maintenance
expense, and subsequent operating outcomes only where definitions and periods
match. Compare with the alternatives of doing nothing, using depreciation,
using total capital expenditure as a conservative case, and adopting separate
sector methods rather than one framework.

Keep the first research unit bounded to three public companies across at least
two capital-intensity profiles: one with an explicit sustaining-capital
breakdown, one with mixed-purpose disclosure, and one with no usable split.
Define the evidence hierarchy and classification rules before reading any
reference breakdown. For each company, create a source-to-adjustment bridge,
a range rather than a point estimate, and parallel depreciation and total-
capital-expenditure cases. Then compare the blinded result with the disclosed
breakdown where available and record why the other cases are estimable or
indeterminate.

Acceptance criteria for advancing the idea:

- Every bound and classification is reconstructible from cited public inputs;
  assumptions and mixed-purpose allocations remain visible and reversible.
- The protocol reconciles to audited capital expenditure and prevents double
  counting with acquisitions, leases, working capital, and expensed repairs.
- The explicit-disclosure test is performed blind to the reference breakdown;
  agreement, disagreement, and definition mismatches are reported separately.
- The opaque case is allowed to remain indeterminate; no point estimate is
  fabricated to complete the framework.
- Owner-earnings sensitivity to the full range is shown, and the protocol's
  information gain over depreciation and total-capex cases is evaluated.
- Material disagreement, circular reliance on management labels, or no clear
  advantage over the simpler alternatives stops the pipeline rather than
  forcing a proposal.

Unknowns include whether three cases can expose enough sector variation,
whether issuer-defined sustaining capital is a usable reference, and whether
competitive-position maintenance can be observed before long-lag deterioration.
The next research stage should preserve these as limitations rather than infer
a universal estimator from a small sample.
