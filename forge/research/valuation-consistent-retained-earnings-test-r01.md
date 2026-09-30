---
name: valuation-consistent-retained-earnings-test
id: 20260930T232329Z
tier: research
pipeline: 20260930T223526Z
author: Researcher
tags: [value-investing, capital-allocation, retained-earnings, valuation]
links:
  - forge/ideas/valuation-consistent-retained-earnings-test-r01.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - investing-hub:frameworks/simple-management.md
  - investing-hub:governance/template-company.md
  - investing-hub:companies/NTDOY.md
  - investing-hub:companies/CROX.md
  - investing-hub:data/crox-financial.md
  - agentic-brain:library/value-investing/capital-allocation.md
  - https://www.berkshirehathaway.com/letters/1983.html
  - https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf
  - https://www.nintendo.co.jp/ir/pdf/2022/annual2203e.pdf
  - https://www.nintendo.co.jp/ir/pdf/2023/230509e.pdf
  - https://www.nintendo.co.jp/ir/pdf/2024/240507e.pdf
  - https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf
  - https://www.sec.gov/Archives/edgar/data/1334036/000133403623000015/R11.htm
  - https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/R24.htm
  - https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/R12.htm
confidence: medium
---
# Research: Valuation-Consistent Retained-Earnings Test

## Question and Method

This report tests whether a small clarification to the retained-earnings rule in
`investing-hub:frameworks/simple-management.md` changes a supported capital-
allocation score, confidence, override, wording, or refusal result for Nintendo
and Crocs beyond an explicit application of the current rule.[1][2] The research
started at clean Forge HEAD `5d91a328ff64d70b567000272308e095e636e825`.
The selected idea was authored by Analyst, so Researcher satisfies the separate-
author research gate. The other open pipeline remained an unrelated discovery
awaiting human review. `LEARNINGS.md` was read and remained read-only.[13]

Before further targeted retrieval, the provisional explanation was that the
current rule already treats market value as a rough cross-check rather than a
substitute for incremental operating returns or intrinsic value. On that view,
Nintendo exposed a report-application defect, not necessarily a framework gap.
The contrary explanation was that the present wording permits a reader to call
a market-only result a pass, so separate labels could prevent a concrete error.
The decisive gaps were the retained-capital denominator, matching market dates
and share counts, a meaningful operating-capital denominator, contemporaneous
intrinsic-value evidence, and whether any score or refusal result changed.
Disconfirmation was predeclared as no decision change beyond the current rule,
only stylistic output changes, or reliance on hindsight valuation.[1][2][4]

The current baseline and candidate were frozen before two isolated readers
received the company evidence:

- **Current baseline:** over at least five years, each retained dollar should
  create at least one dollar of owner value through incremental returns at or
  above alternatives. Where a multi-year after-tax operating-profit-to-invested-
  capital denominator is distorted, inspect actual project or acquisition
  outcomes. Reconcile actual shares and score decisions, not share-price
  performance alone.[2]
- **Candidate rule:** report `supported`, `unsupported`, or `indeterminate`
  separately for (1) a market-value cross-check using explicit dates and actual
  shares, (2) operating or incremental-return evidence, and (3)
  contemporaneously reconstructible intrinsic-value-per-share evidence. A
  supported market cross-check alone cannot produce an overall pass.

Reader A applied the baseline first; Reader B applied the candidate first. Both
used the same disclosed evidence and model family, so agreement is a
reproducibility check, not independent domain evidence. Their separate outputs
were inspected; the material calculations, labels, disagreements, and source
pins are reproduced below. This report independently rechecked every material
number against the issuer records. The executed arithmetic used `bc`; one
unattended `execute_code` attempt was blocked before execution and is recorded
in `errors.log`.[6][7][8][9][10][11][12]

Berkshire's 1983 letter supplies the original test: retention should deliver at
least USD1 of market value for each USD1 retained over time, applied on a five-
year rolling basis. The same letter makes growth in intrinsic business value per
share the objective.[5] The current Investing Hub rule is stricter than a price
ratio alone: it requires incremental returns, alternatives, acquisition outcomes,
share reconciliation, and scoring that does not depend on share-price performance
alone.[2] Brain prior work independently describes the market test as a noisy
retrospective proxy that must be supplemented by incremental-return and per-share
value evidence.[4]

## Evidence and Findings

### Nintendo: the market cross-check passes, but the reported 2.2 needs a definition

Nintendo's published report assigns capital allocation 3/5 at Medium confidence.
It says the one-dollar test passes only on an approximately 2.2-JPY market-
capitalization gain per JPY retained, then states that the closing market price is
above intrinsic value and 116% above its Base estimate.[3] The two ideas are not
logically incompatible: a historical market cross-check can pass even when the
closing price exceeds a current intrinsic-value estimate. The defect is calling
that market-only observation a pass without showing the denominator, matching the
periods, or applying the rest of the current rule.[2][3][5]

The aligned five-year reconstruction uses March 31, 2021 and March 31, 2026:

| Item | Reproduced result | Source and qualification |
|:--|--:|:--|
| Opening split-adjusted price | JPY6,181.9758 | FY2021 EPS JPY4,032.60 x PER 15.33 / 10; both inputs are rounded.[6] |
| Opening actual shares | 1,191,227,670 | (131,669,000 issued - 12,546,233 treasury) x 10.[6] |
| Opening market capitalization | JPY7,364,140.628 million | Price x actual shares. |
| Closing price | JPY8,773.7557 | FY2026 EPS JPY364.51 x PER 24.07; both inputs are rounded.[10] |
| Closing actual shares | 1,152,828,705 | 1,287,260,000 issued - 134,431,295 treasury.[10] |
| Closing market capitalization | JPY10,114,637.422 million | Price x actual shares. |
| Market-capitalization gain | JPY2,750,496.793 million | Closing less opening. |
| FY2022-FY2026 owner profit | JPY2,103,923 million | Sum of the five annual amounts.[7][8][9][10] |
| Dividends | JPY1,056,933 million | Sum of the five equity-roll-forward amounts.[7][8][9][10] |
| Gross treasury-share purchases | JPY245,756 million | Sum of the five equity-roll-forward amounts.[7][8][9][10] |
| Earnings retained after dividends | JPY1,046,990 million | Profit less dividends. |
| Net capital retained after dividends and buybacks | JPY801,234 million | Profit less dividends and gross repurchases. |

The aligned cross-check equals 2.627 JPY of market-capitalization gain per JPY of
accounting-style earnings retained after dividends. Treating buybacks as owner
returns produces 3.433 JPY per JPY of net capital retained. Both conventions pass
the rough market test, but they answer different questions and must be named.
The FY2022 cancellation moved JPY31,607 million from retained earnings against
treasury shares, and FY2026 moved JPY28,795 million from retained earnings to
capital surplus; neither is another owner distribution. A simple retained-
earnings-balance change would therefore misstate the denominator.[7][10]

The published approximately 2.2 result is conditionally reproducible. Using the
September 29, 2026 report price of JPY7,896 and reconstructed post-July actual
shares of 1,152,873,116 gives a market-capitalization gain of JPY1,738,945.496
million from the 2021 opening point. Dividing by JPY801,234 million, which treats
both dividends and buybacks as owner returns, gives 2.170, which rounds to 2.2.
Dividing by earnings retained after dividends gives 1.661 instead. The report
states neither convention, and its September 2026 market endpoint is six months
later than the March 2026 earnings-and-distribution endpoint. The number is thus
a reproducible rough cross-check only under a disclosed net-of-buybacks convention
and an explicit period mismatch, not an unqualified retained-earnings result.[3]
[6][7][8][9][10]

The candidate labels for Nintendo are:

| Component | Finding | Evidence and limit |
|:--|:--|:--|
| Market-value cross-check | **Supported** | Both aligned denominator conventions exceed one; endpoint prices are inferred from rounded EPS and PER.[6][10] |
| Operating or incremental return | **Indeterminate** | Operating profit fell from JPY640,634 million in FY2021 to JPY360,117 million in FY2026, but the console cycle, expensed development, cash and securities, associates, and project timing prevent a meaningful corresponding invested-capital denominator. Switch 2 is a favorable outcome; the JPY230 billion facilities plan remains unproven.[3][6][10] |
| Intrinsic value per share | **Indeterminate** | The current report supplies a September 2026 DCF but no contemporaneous March 2021 intrinsic-value estimate. A hindsight DCF or current price cannot supply the opening value.[3] |
| Overall retained-earnings result | **No supported pass** | A market cross-check cannot fill both unresolved owner-value channels under either the candidate or current rule.[2][4][5] |

Reader A classified the operating component `indeterminate`; Reader B classified
it `unsupported` from the lower endpoint operating profit and weak named uses.
The stricter negative label overstates what the evidence can isolate across one
console cycle. The checked synthesis retains `indeterminate`: actual allocation
outcomes are mixed, and the current rule itself says not to force a distorted
incremental-return denominator.[2][3] Reader A's first retained-capital bridge
also omitted the FY2022 JPY31,607 million cancellation reclassification. The
annual roll-forwards exposed the omission; the corrected calculations above use
the explicit five-year dividend and repurchase amounts.[7][8][9][10]

Both readers left Nintendo's capital-allocation score at 3/5, confidence at
Medium, and all overrides and refusal results unchanged. Both required a wording
correction: replace the blended market-only pass with separate market,
operating, and intrinsic-value findings. An explicit application of the current
rule requires the same substantive correction, so the candidate changes
presentation but not the supported judgment.[2][3]

### Crocs: decision-specific evidence works without a forced market ratio

Crocs is the control for a company whose allocation record can be judged without
an explicit one-dollar calculation. Its report assigns capital allocation 2/5 at
Medium confidence. Crocs paid USD2.05 billion cash and issued 2,852,280 shares for
HEYDUDE; the cash was financed with a USD2.0 billion term loan and USD50 million
of revolver borrowing.[3][11] HEYDUDE generated USD137.401 million of segment
operating income in 2024, then reported USD714.840 million of 2025 revenue,
USD668.855 million of segment operating loss including USD737 million of
impairments, and downward revisions to expected growth and margins.[12]

The current report's approximately 5.2% after-tax return uses the cash price.
The primary record puts aggregate consideration at approximately USD2.3 billion,
including issued shares, before acquisition costs. Even the 2024 pre-tax segment
operating income was only about 6% of that approximate full price; an after-tax
return is lower. The later revenue decline and impairments do not duplicate the
cash outlay, but they contradict the acquisition expectations. This is adverse,
decision-specific operating evidence under the current rule's full-cost and
actual-outcome requirements.[2][3][11][12]

The candidate labels for Crocs are:

| Component | Finding | Evidence and limit |
|:--|:--|:--|
| Market-value cross-check | **Indeterminate** | The frozen company record has no matched five-year opening price, actual opening shares, closing price, and retained-capital bridge. Weighted-average EPS shares are not a substitute.[2][3] |
| Operating or incremental return | **Unsupported** | HEYDUDE's full acquisition cost, 2024 return, subsequent revenue decline, and USD737 million impairment are adverse decision-specific evidence.[11][12] |
| Intrinsic value per share | **Indeterminate** | The current USD133 Base estimate cannot be backcast as contemporaneous value at the acquisition or past repurchase dates.[3] |
| Overall retained-earnings result | **No supported pass** | The operating evidence is adverse; unavailable market and historical-value inputs remain unknown rather than being forced into comparison.[2] |

Both readers retained the Crocs capital-allocation score at 2/5, confidence at
Medium, and no override or refusal. The current rule already requires the full
acquisition cost and decision-specific outcome. The candidate would make the
missing market and intrinsic-value evidence explicit, but it changes no supported
classification. The report's statement that prior buybacks were below its current
Base value is a hindsight comparison, not evidence of contemporaneous intrinsic
value; that limit should remain visible without changing the score.[2][3]

### Source independence and coverage limits

Nintendo and Crocs filings are primary evidence for reported amounts but are not
independent assessments of management quality. The Investing Hub reports depend
on those issuer records; they are comparison targets, not corroboration. The
Berkshire letter is primary evidence for the original rule, while Brain's topic is
a sourced synthesis of its limits.[3][4][5][6][7][8][9][10][11][12] The two readers were isolated and
order-balanced but used the same model family and evidence, so they test
reproducibility rather than independent truth.

The population is two current company reports, one explicit market test, one
console-cycle company, and one acquisition control. No contemporaneous historical
intrinsic-value series exists for either company in the checked corpus. Crocs
lacks the frozen market endpoints needed for a five-year capitalization bridge.
Nintendo's market endpoint prices are reconstructed from rounded annual-report
ratios, and its report-date 2.2 calculation lacks a matching September retention
endpoint. These limits block a general claim that three labels improve decisions
across companies.

## Alternatives and Implications

| Alternative | Evidence-supported effect | Cost and implication |
|:--|:--|:--|
| Do nothing | Preserves the existing framework and scores. | Leaves Nintendo's denominator and market-only `pass` ambiguous despite the current rule.[2][3] |
| Correct report application only | Disclose Nintendo's denominator and period mismatch; label the market cross-check supported, operating and intrinsic evidence indeterminate, and no overall pass. Preserve Crocs' decision-specific result. | Smallest correction supported by this test; changes wording, not either score, confidence, override, or refusal. |
| Add one framework sentence with three labels | Makes the current semantics harder to compress into a blended pass. | Duplicates the present incremental-return, alternatives, actual-share, and no-price-only rules; changed zero tested decisions.[2] |
| Add a company-template field | Forces every report to display three results. | The template already requires management-framework application, capital deployment, actual-share evidence, limitations, and an override-aware scorecard. The sample does not justify another mandatory field.[2] |
| Require historical DCF endpoints | Would create an apparent intrinsic-value series. | Rejected: contemporaneous evidence is absent, and hindsight reconstruction would add false precision.[1][3][4] |

The bounded result supports a report-application correction, not a demonstrated
framework or template improvement. Both readers reached the same scores,
confidence, overrides, refusals, and no-overall-pass results under the candidate
and an explicit current baseline. The candidate's only incremental effect was a
clearer display. This does not establish that separate labels have no value in a
larger corpus; it establishes that this two-report test found no decision change
beyond the current semantic rule.

For value investors, the simplest interpretation is that market capitalization
is a noisy observation, not a causal measure of retained-capital productivity.
An owner-oriented review should name the cash actually retained, reconcile
shares, inspect incremental or project returns, and preserve `indeterminate` when
historical intrinsic value cannot be reconstructed.[2][4][5] A favorable market
cross-check can coexist with an overvalued closing price because the two claims
use different reference questions. Neither alone establishes that management
created intrinsic value with the retained capital.

## Response to Feedback and Remaining Questions

No prior evaluation exists for this pipeline.

The root idea's material questions are answered as follows:

- The approximately 2.2 Nintendo result is conditionally reproducible only after
  defining retained capital net of dividends and gross buybacks; the report does
  not disclose that denominator and mixes March and September endpoints.
- The aligned Nintendo market cross-check is supported under either disclosed
  denominator convention. Operating and historical intrinsic-value evidence are
  indeterminate, so neither the candidate nor the current rule supports an
  overall pass.
- Crocs remains a valid control without a forced market ratio. Its HEYDUDE record
  is adverse under the current full-cost, actual-outcome rule.
- The candidate changes wording for both reports but changes no score, confidence,
  override, refusal, or capital-allocation conclusion beyond an explicit current
  baseline.
- A report-only correction is the smallest supported response. The evidence does
  not demonstrate decision value for a framework sentence or template field.

Remaining decision-relevant questions are whether a larger set of company reports
contains repeated market-only misapplications despite the current rule, whether
three labels reduce those errors prospectively, and whether their review cost is
lower than enforcing the existing rule. Those questions require another bounded
sample or prospective test; this report does not answer them.

Confidence is medium. Confidence is high in the reproduced Nintendo source
amounts and conditional ratios because the annual roll-forwards, share tables,
and executed arithmetic agree.[6][7][8][9][10] Confidence is high that Crocs' acquisition
and impairment evidence is adverse because primary SEC tables state the full
consideration structure, segment outcome, and impairment trigger.[11][12]
Overall confidence remains medium because only two reports were tested, the two
readers share a model family, Nintendo lacks a clean incremental-capital and
historical intrinsic-value series, Crocs lacks a market bridge, and no prospective
reader outcome was measured. Confidence would rise if a larger frozen sample or
prospective control showed that separate labels uniquely prevent decision-
relevant errors. It would fall if a correct current-rule application produced
materially different scores or if exact endpoint records contradicted the
reproduced calculations.

This research issues no `ADVANCE` verdict, proposal, company-report edit, or
framework change. `LEARNINGS.md` remains unchanged as required for a research
stage.[13]

## Sources

1. `forge/ideas/valuation-consistent-retained-earnings-test-r01.md` -- root
   question, frozen candidate, two-reader comparison, decision-value threshold,
   alternatives, and stop conditions. [high]
2. `investing-hub:frameworks/simple-management.md` -- current one-dollar test,
   incremental-return and alternatives rules, full acquisition cost, actual-share
   reconciliation, scoring, confidence, and overrides. [high]
   - `investing-hub:governance/template-company.md` -- current Management output,
     framework-application, evidence, limitation, and scorecard requirements.
     [high]
3. `investing-hub:companies/NTDOY.md` -- Nintendo market-test wording, score,
   operating evidence, valuation, and report-date price. [high]
   - `investing-hub:companies/CROX.md` -- Crocs allocation score, HEYDUDE return,
     repurchases, valuation, and limitations. [high]
   - `investing-hub:data/crox-financial.md` -- Crocs historical statements,
     acquisition cash flow, repurchases, retained earnings, and share data. [high]
4. `agentic-brain:library/value-investing/capital-allocation.md` -- intrinsic-
   value-per-share objective, market-test limits, incremental returns, full
   acquisition cost, sources and uses, and opportunity-cost review. [medium]
5. Berkshire Hathaway Inc. "Chairman's Letter - 1983," March 14, 1984,
   owner-related principles and retained-earnings-test passages. Per-share
   intrinsic-value objective and five-year USD1 market-value test were checked.
   https://www.berkshirehathaway.com/letters/1983.html [high]
6. Nintendo Co., Ltd. "Annual Report 2021," July 2021, pp. 1, 19-25, and
   50-51. FY2021 EPS, PER, issued and treasury shares, split basis, operating
   profit, and opening retained earnings were checked.
   https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf [high]
7. Nintendo Co., Ltd. "Annual Report 2022," July 2022, key data and statements
   of changes in equity. FY2022 profit, dividends, repurchases, and cancellation
   reclassification were checked.
   https://www.nintendo.co.jp/ir/pdf/2022/annual2203e.pdf [high]
8. Nintendo Co., Ltd. "Consolidated Financial Highlights," May 9, 2023,
   operating results and statements of changes in equity. FY2023 profit,
   dividends, and repurchases were checked.
   https://www.nintendo.co.jp/ir/pdf/2023/230509e.pdf [high]
9. Nintendo Co., Ltd. "Consolidated Financial Highlights," May 7, 2024,
   operating results and statements of changes in equity. FY2024 profit,
   dividends, and repurchases were checked.
   https://www.nintendo.co.jp/ir/pdf/2024/240507e.pdf [high]
10. Nintendo Co., Ltd. "Annual Report 2026," July 2026, pp. 1-2, 23-30, and
    59-62. FY2022-FY2026 results, issued and treasury shares, dividends,
    repurchases, retained earnings, and capital-surplus transfer were checked.
    https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf [high]
11. Crocs, Inc. "Form 10-K for the fiscal year ended December 31, 2022,"
    February 16, 2023, Note 4, Acquisition of HEYDUDE. Cash consideration,
    issued shares, aggregate price, financing, and acquisition result were
    checked.
    https://www.sec.gov/Archives/edgar/data/1334036/000133403623000015/R11.htm
    [high]
12. Crocs, Inc. "Form 10-K for the fiscal year ended December 31, 2025,"
    February 12, 2026, operating-segment and goodwill/intangible-asset notes.
    HEYDUDE revenue, operating income/loss, impairments, and forecast-revision
    trigger were checked.
    https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/R24.htm
    [high]
    - Crocs, Inc. Same filing, goodwill and indefinite-lived intangible-assets
      note. The USD430 million trademark and USD307 million goodwill impairments
      and their stated causes were checked.
      https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/R12.htm
      [high]
13. `forge/protocol.md` -- selection, independence, artifact, handoff,
    transaction, and read-only-learning rules. [high]
    - `STATUS.md` -- selected research row and preserved unrelated human-review
      row at starting HEAD. [high]
    - `LEARNINGS.md` -- method lessons read before research and kept unchanged.
      [high]
    - `logbook/progress.log` -- prior handoff through ENT-023. [high]
    - `logbook/errors.log` -- prior errors through ENT-029 and current failure
      record boundary. [high]
