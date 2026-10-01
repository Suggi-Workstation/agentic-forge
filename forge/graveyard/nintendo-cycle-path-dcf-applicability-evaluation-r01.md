---
name: nintendo-cycle-path-dcf-applicability-evaluation
id: 20261001T053824Z
tier: evaluation
pipeline: 20261001T033647Z
author: Analyst
tags: [value-investing, valuation, cyclicality, evaluation]
links:
  - forge/research/nintendo-cycle-path-dcf-applicability-r01.md
  - forge/ideas/nintendo-cycle-path-dcf-applicability-r01.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - logbook/progress.log
  - logbook/errors.log
  - governance/template-evaluation.md
  - investing-hub:frameworks/simple-dcf.md
  - investing-hub:frameworks/sector-metrics.md
  - investing-hub:governance/template-company.md
  - investing-hub:companies/NTDOY.md
  - investing-hub:companies/CROX.md
  - agentic-brain:library/valuation-screening/valuation-of-cyclical-companies-normalizing-earnings-across-the-business-cycle.md
  - agentic-brain:library/valuation-screening/discounted-cash-flow-dcf-methodology.md
  - https://www.nintendo.co.jp/ir/pdf/2017/annual1703e.pdf
  - https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf
  - https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf
  - https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/normearn.htm
confidence: medium
---
# Evaluation: Nintendo Cycle-Path DCF Applicability

## Target and Baseline

Target: `forge/research/nintendo-cycle-path-dcf-applicability-r01.md`, ID
`20261001T051357Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the research session's private
reasoning. Analyst authored the root idea, but the protocol permits an ideator
to evaluate another agent's research after recording a cold baseline. The exact
research target therefore passes the independent-author and context gate.[2][9]

At starting HEAD `784639ef046f450c4db127d860b0e2b07823f465`, the worktree was
clean. The board contained three valid rows: an unrelated discovery awaiting
human review, this selected `evaluate` row with the exact target above, and a
newer unrelated `research` row. The discovery resolves to a READY final review,
and the research row resolves to its root idea. This was the only eligible
review row and therefore the oldest eligible assignment. Progress ended at
ENT-031 and errors at ENT-037. No prior REVISE, REFRAME, evaluation, final
review, or human budget extension exists in this pipeline; zero of two
corrective cycles were used.[9]

Before reading the target body, the expected evidence and failure conditions
were recorded in evaluator scratch. Expected evidence was:

- the full current simple-DCF applicability contract applied before a timing
  calculation, not a presence-only surrogate;
- preserved separate reader classifications, with agreement receiving no
  independent factual weight;
- reproduction of the published V0, annual cash, terminal, per-share,
  no-growth, and price calculations;
- a predeclared timing comparator with equal ten-year undiscounted cash,
  matched terminal cash, explicit signs and order, raw annual outputs, and at
  least one plausible alternative order;
- primary-source support for the historical cash pattern, cycle coverage,
  scale, launch timing, and working-capital effects;
- no coherent cycle forecast unless cash, investment, working capital, tax,
  claims, and terminal state could be supported together; and
- decision value measured against full current-rule enforcement in method,
  valuation type, confidence, thesis status, case order, price boundary, or
  price conclusion.[2][3][8]

Failure conditions were an unreproduced baseline, arbitrary or post-result
phase ordering, an unsupported full-cycle claim, unmatched totals or terminal
assumptions, missing primary support for material inputs, or treating a small
numerical delta as decision value after every supported decision field stayed
unchanged. ADVANCE required a unique, checked benefit beyond applying the
current gate. The root idea made current-rule sufficiency, arbitrary timing,
and zero decision change explicit stop conditions.[2]

## Findings

### The exact current contract already requires the correction

The simple-DCF framework requires five to ten years including a weak period and
permits its formula only when a positive two-stage path represents annual
benefits. It sends known zero or negative years and uneven funding needs to a
dated schedule or another method, prohibits normalizing those events away, and
requires Not applicable or Not calculable with N/A values when a completed
calculation is unsupported.[3]

Nintendo's report says cash earnings swing with the console cycle, uses the
FY2022-FY2026 core-cash average as V0, and reports annual amounts of JPY278.7,
283.7, 409.3, -49.1, and 226.1 billion. Every smooth scenario remains positive,
so the published path cannot represent the known negative year or launch-
related funding swing. The report nevertheless labels the result a completed
Cash DCF, calls the combined values intrinsic value, and uses them for price
conclusions.[3]

The evaluator therefore independently reaches HALT under the current rule:
mark simple DCF Not applicable, keep unsupported case values N/A, and use a
dated signed schedule or another supported method before restoring a completed
valuation. A separately labeled what-if may remain useful, but it cannot inherit
the Cash DCF or intrinsic-value label.[3]

The target reports two cold readers reaching the same result, but their
separate raw outputs are not retained. Their agreement receives no evidentiary
weight. Direct inspection of the rule and report is sufficient for the same
classification, so this preservation defect does not block the negative
comparison.[1][3]

Crocs is a useful boundary control, not a Nintendo analogue. Its report retains
only three detailed years of the selected owner-cash metric, below the current
rule's five-to-ten-year requirement. Historical operating losses do not by
themselves establish a recurring signed owner-cash path. The full gate therefore
halts both reports for different stated defects rather than mechanically
rejecting every volatile consumer business.[1][3]

### Primary history supports cyclicality but not one comparable cash cycle

Issuer key-data tables independently verify the research's signs, units, years,
and amounts. Nintendo reported operating profit/loss and operating cash flow of
JPY-36.410/-40.390 billion in FY2013, JPY-46.425/-23.114 billion in FY2014,
JPY29.362/19.101 billion in FY2017, JPY640.634/612.106 billion in FY2021, and
JPY360.117/289.789 billion in FY2026.[4][5][6] The same tables show net sales
rising from JPY489.095 billion in FY2017 to JPY2,313.051 billion in FY2026.[4][6]

The 2017 report states that Nintendo Switch launched worldwide on March 3,
2017. The 2026 report states that Nintendo Switch 2 launched in June 2025 and
that launch periods can temporarily increase trade receivables, trade payables,
and inventories, with an upward or downward operating-cash effect.[4][6] Its
cash-flow statement reports inventory cash uses of JPY333.837 billion in
FY2025 and JPY27.591 billion in FY2026.[6]

These checks support a recurring operating and cash cycle and the economic
relevance of launch working capital. They do not supply one signed core-cash
series across an unchanged business scale. Damodaran says absolute averaging
should span an entire cycle, works best when firm scale has not changed, and
overstates value when normalization takes several periods but is modeled as
immediate.[7] Brain prior work likewise requires normalized profit,
reinvestment, working capital, claims, and terminal state to describe one
coherent condition and prefers coherent scenarios when path timing is
unknown.[8]

The target's Nintendo 2026 source entry names pp. 15-16 and 62-63 for the
working-capital and inventory claims. Direct PDF text and 300-DPI page checks
locate the launch-period warning on printed p. 18 and the inventory cash-flow
row on printed p. 64. The URL, amounts, signs, and conclusion are correct, but
the pinpoint pages are not. This is a source-record defect, not a blocker to
closure, because the evaluator independently verified and correctly pinpoints
the passages here.[1][6]

### Independent arithmetic reproduces the baseline and timing result

A separately written Decimal calculation reproduced the research from the
published formulas and frozen inputs. The five displayed core-cash values
average JPY229.74 billion. Using that unrounded V0 reproduces:[1][3]

| Case | PV years 1-10 | PV terminal | Value per share |
|:--|--:|--:|--:|
| Bear | 1,050.092 | 467.024 | JPY2,267.913 |
| Base | 1,610.161 | 1,360.436 | JPY3,656.341 |
| Bull | 2,122.554 | 2,429.785 | JPY5,250.396 |

Using the displayed V0 of JPY229.7 billion reproduces the published rounded
Base and no-growth results: Base explicit PV JPY1,609.881 billion, terminal PV
JPY1,360.199 billion, value JPY3,655.892 per share, and no-growth value
JPY3,225.697 per share. The arithmetic supports the target's statement that the
calculation mechanics are not the method-fit defect.[1][3]

The evaluator also independently reproduced the predeclared matched paths. Each
has exactly the smooth Base ten-year undiscounted cash total of
JPY2,669.568094 billion and the same terminal cash, adjustment, associate value,
shares, and required return:[1]

| Path | PV years 1-10 | Value per share | Delta from smooth Base | Price premium |
|:--|--:|--:|--:|--:|
| Smooth positive Base | 1,609.881 | JPY3,655.892 | Baseline | 115.98% |
| Launch-first signed sensitivity | 1,707.721 | JPY3,740.759 | +2.321% | 111.08% |
| Expansion-first signed sensitivity | 1,717.059 | JPY3,748.858 | +2.543% | 110.62% |

The signed orders raise value because larger positive amounts arrive earlier and
the negative amount arrives later. This contradicts the provisional directional
expectation but changes no method classification, case ordering, 30% or 50%
price boundary, confidence, thesis status, or price conclusion. The phase labels
are analytical, and neither order is a supported forecast. The timing test is
therefore a valid sensitivity and a negative decision-value result, not a new
cycle valuation.[1]

### The smallest supported response is report application correction

The target covers groundedness, contrary evidence, alternatives, and
limitations sufficiently to decide the bounded question. It correctly declines
to build a coherent current-scale cycle forecast from unsupported cash,
investment, working-capital, tax, and terminal assumptions. Its exact scripts
and material annual outputs permit the numerical result to be checked, although
hashes do not substitute for the unavailable separate reader records.[1][9]

The alternatives resolve as follows:

- Doing nothing retains a completed Cash DCF and intrinsic-value claim after the
  governing method gate has failed.
- Correcting the Nintendo report application is already required and is the
  smallest reversible response.
- Clarifying the framework adds no demonstrated classification because the
  existing language was directly sufficient.
- Adding a Nintendo cycle schedule now would manufacture unsupported phase
  economics; coherent scenarios remain a changed-evidence research question.

The strongest contrary case is that a through-cycle normalized V0 can be useful
when the cycle and scale are comparable. That principle remains valid, but the
checked five-year profile does not establish those conditions, and the local
framework expressly routes known negative years away from its positive formula.
No proposal is justified by a mechanically reproducible but inapplicable model
or by a 2.32%-2.54% sensitivity that changes no supported decision.[1][3][7][8]

## Verdict and Handoff

**Verdict: REJECT. Next stage: closed in `forge/graveyard/`. Zero of two
corrective cycles were used; this closure consumes no corrective cycle.**

The research is grounded enough to decide the root question, and its negative
result survives independent source and arithmetic checks. The current framework
already forces the supported Nintendo application correction, while the matched
timing sensitivities add no decision-relevant result and cannot support a
coherent cycle forecast. A REVISE would request work whose absence does not
block this negative decision; a REFRAME would repeat the same problem without
changed evidence.[1][2][3]

Reopening requires changed evidence: a retained comparable full-cycle cash
bridge at current scale; coherent phase scenarios whose cash, investment,
working capital, tax, claims, and terminal state are independently reproducible;
or prospective repeated misapplication showing that explicit enforcement of the
current gate is insufficient. The changed evidence must alter a method,
valuation type, confidence, thesis, price boundary, or supported price
conclusion. This verdict authorizes no Investing Hub report edit, framework
change, valuation replacement, security recommendation, or implementation.[9]

Confidence is medium. Confidence is high in the current-rule HALT, issuer table
values, arithmetic reproduction, and zero decision delta for the tested paths.
Overall confidence remains medium because the corpus has two company reports,
the core-cash profile spans only five years, the phase labels are analytical,
two readers share one model family and lack separate retained outputs, and no
coherent current-scale console-cycle cash schedule exists. Confidence would
rise with independently reproduced changed evidence of the kind required for
reopening and would fall if a resolving current-framework passage or comparable
full-cycle record supported the published positive path.[1][3][4][5][6]

## Learning Decision

`LEARNINGS.md` remains unchanged.[9]

- **Selection:** The root idea's explicit current-rule and zero-decision-delta
  stop conditions made closure decisive. The existing full-contract-comparator
  lesson already captures that selection method.
- **Evidence and test design:** The exact framework, rendered issuer tables,
  corrected page pinpoints, and independent fixed arithmetic decided the
  question. Unretained reader outputs repeat the existing evidence-preservation
  lesson and receive no weight; they do not justify a duplicate lesson or a
  correction cycle.
- **Process:** Native PDF text plus targeted 300-DPI renders resolved table
  signs, headings, units, and two incorrect citation pinpoints. No recurring
  Forge handoff, template, or tool failure changed the verdict.
- **Repetition:** This pipeline again shows that a fair full semantic baseline
  can make an added rule or method unnecessary. That pattern is already covered
  by the current comparator lesson.
- **Coverage:** The result is a domain disposition, not a new transferable
  method. Existing package-preservation, claimed-contract, and bounded-tooling
  lessons cover the material procedure; the learning admission gate therefore
  does not pass for an edit.

## Sources

1. `forge/research/nintendo-cycle-path-dcf-applicability-r01.md` -- exact target,
   frozen method, source record, cold classifications, calculations, timing
   sensitivities, alternatives, limitations, and negative conclusion. [high]
2. `forge/ideas/nintendo-cycle-path-dcf-applicability-r01.md` -- root question,
   decision-value threshold, research plan, alternatives, and stop conditions.
   [high]
3. `investing-hub:frameworks/simple-dcf.md` -- positive-path applicability,
   five-to-ten-year history, dated-schedule, calculation, type-label, N/A, and
   HALT requirements. [high]
   - `investing-hub:frameworks/sector-metrics.md` -- method fit, cycle
     normalization, uneven signed schedule, and second-calculation gate. [high]
   - `investing-hub:governance/template-company.md` -- alternative-method,
     Not-applicable, Not-calculable, N/A, and valuation-label requirements.
     [high]
   - `investing-hub:companies/NTDOY.md` -- current cycle description, core-cash
     series, valuation inputs and outputs, Cash DCF label, confidence, and price
     conclusion. [high]
   - `investing-hub:companies/CROX.md` -- three-year owner-cash control,
     historical-loss references, valuation label, and limitations. [high]
4. Nintendo Co., Ltd. "Annual Report 2017," 2017, pp. 2 and 7.
   FY2013-FY2017 net sales, operating profit/loss and operating cash flow, and
   the March 3, 2017 worldwide Switch launch were checked in native text and
   300-DPI rendered pages.
   https://www.nintendo.co.jp/ir/pdf/2017/annual1703e.pdf [high]
5. Nintendo Co., Ltd. "Annual Report 2021," 2021, pp. 2 and 12.
   FY2017-FY2021 operating profit and operating cash flow plus the strong Switch
   hardware and software year were checked in native text and rendered pages.
   https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf [high]
6. Nintendo Co., Ltd. "Annual Report 2026," 2026, pp. 2, 8, 18, and 64.
   FY2022-FY2026 net sales, operating profit and operating cash flow, the June
   2025 Switch 2 launch, launch-period working-capital warning, and inventory
   cash-flow amounts were checked in native text and 300-DPI rendered pages.
   https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf [high]
7. Aswath Damodaran. "More on normalizing earnings," undated; accessed
   2026-10-01, entire-cycle averaging, scale limits, scaled alternatives, and
   immediate versus multi-period normalization.
   https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/normearn.htm
   [high]
8. `agentic-brain:library/valuation-screening/valuation-of-cyclical-companies-normalizing-earnings-across-the-business-cycle.md` -- full-cycle normalization, scale, complete cash-system consistency, cycle paths, coherent scenarios, and terminal-state limits. [medium]
   - `agentic-brain:library/valuation-screening/discounted-cash-flow-dcf-methodology.md` -- claim-matched cash, reinvestment, scenarios, terminal state, and model uncertainty. [medium]
9. `forge/protocol.md` -- independence, correction budget, closure, selection,
   artifact, source, learning, transaction, and no-implementation rules. [high]
   - `STATUS.md` -- selected exact target and preserved unselected rows at the
     starting snapshot. [high]
   - `logbook/progress.log` -- exact prior pipeline handoffs and zero prior
     corrective verdicts. [high]
   - `logbook/errors.log` -- recent retrieval and scratch-cleanup fault record.
     [high]
   - `LEARNINGS.md` -- package-preservation, full-contract-comparator,
     claimed-result, bounded-tooling lessons, and separate admission gate. [high]
   - `governance/template-evaluation.md` -- evaluation body and pre-write gate.
     [high]
