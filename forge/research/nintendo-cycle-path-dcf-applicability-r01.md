---
name: nintendo-cycle-path-dcf-applicability
id: 20261001T051357Z
tier: research
pipeline: 20261001T033647Z
author: Researcher
tags: [value-investing, valuation, cyclicality, dcf]
links:
  - forge/ideas/nintendo-cycle-path-dcf-applicability-r01.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - governance/template-research.md
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
# Research: Nintendo Cycle-Path DCF Applicability

## Question and Method

This report tests the exact question in the root idea: whether Nintendo's
published smooth two-stage simple DCF remains applicable when the report itself
identifies a console-driven cash cycle, and whether one matched timing test
changes a valuation type, confidence, case ordering, price boundary, thesis
status, or price conclusion beyond enforcement of the current rule.[1]
Research began at clean Forge HEAD
`dfcf0ce75e5ecb9d7e8811b5a274a36ed629b852`. The selected idea was authored by
Analyst, so Researcher satisfies the separate-author gate. The unrelated older
human-review row and newer liquidity-research row remained untouched.
`LEARNINGS.md` was read and remained unchanged.[9]

Before further targeted research, the provisional explanation was that the
simple-DCF gate already rejects Nintendo's current presentation. A positive
average starting amount cannot make a smooth positive path represent annual
benefits when known console-cycle cash includes a negative year and launch
funding swings. The contrary explanation was that a normalized full-cycle V0
can legitimately stand in for unpredictable phase timing, so the current
smooth model may remain a useful through-cycle cash valuation. The decisive
gaps were method classification under the full current contract, exact baseline
reproduction, whether FY2022-FY2026 is a comparable full cycle, the value effect
of timing alone, and whether a narrower cycle criterion adds anything beyond
the current rule.[1][2][3]

The investigation used this fixed order:

1. Freeze the idea, current simple-DCF and method-selection rules, company
   template, Nintendo report, Crocs control, current Forge method memory, and
   the selected repository snapshot.[1][2][3][9]
2. Before calculation, obtain two isolated cold readings of Nintendo under the
   full current contract. Preserve each classification and reason separately;
   their common model family and evidence mean agreement is a reproducibility
   observation, not independent domain evidence.
3. Inspect Nintendo's 2017, 2021, and 2026 annual-report key-data tables using
   native PDF text and rendered-page checks. Record fiscal headings, signs,
   units, operating profit, and operating cash flow. Use issuer evidence to
   test cycle coverage and scale comparability.[4][5][6]
4. Freeze the baseline and matched-path rules before viewing calculated values.
   Run one Decimal/Python calculator and one separately written Node.js
   calculator. Compare every numeric output recursively under a fixed tolerance.
5. Apply the full current rule to Crocs as a control without rebuilding its
   valuation. Compare doing nothing, report-only correction, framework
   clarification, and a new cycle-schedule method.

The predeclared timing test holds the Base ten-year undiscounted cash total,
Base year-10 terminal cash, 12 times terminal multiple, 10% required return,
Base equity adjustment, Base associate value, and shares fixed. It scales the
published signed five-year core-cash profile by one factor and orders it as two
five-year paths: launch-first and expansion-first. This isolates discounting
order only. It is not a forecast, probability model, or proof that the five-year
profile is a complete cycle.

## Evidence and Findings

### The current full contract already halts Nintendo's smooth model

The simple-DCF framework permits the model only when a positive two-stage path
represents annual benefits. It sends known zero or negative years and uneven
funding needs to a dated schedule or another method, says not to normalize those
events away, and halts an unrepresentable path or unsupported valuation
claim.[2] Nintendo's report states that cash earnings swing with the console
cycle, uses a five-year average as V0, and discloses signed annual core cash of
JPY278.7 / 283.7 / 409.3 / -49.1 / 226.1 billion. Every published smooth path
is positive because V0 is positive and each growth rate is greater than -100%.[3]

The two readers independently reached the same procedural classification:

| Reader | Classification | Decisive contract reading | Required current-rule result |
|:--|:--|:--|:--|
| A | HALT | `simple-dcf.md` lines 14, 20, 55-56, 80 and 90; `NTDOY.md` lines 24-26, 46-50 and 142-155. The positive formula cannot represent the known negative year or launch-related uneven cash. | Mark simple DCF Not applicable; use a dated signed schedule or another method; until then values are N/A rather than completed Cash DCF. |
| B | HALT | `simple-dcf.md` lines 20, 26, 55-56 and 80; `NTDOY.md` lines 24-26, 46-50, 142-155 and 168-170. Positive V0 does not override the path gate. | Same correction; the mixed associates-at-a-multiple basis also cannot silently support the combined intrinsic-value label. |

Both readers also identified unresolved support for the five-year V0 as a
valuation-date run rate, forecast reinvestment and cash conversion, case-specific
growth and terminal assumptions, and the retained second-calculation record.
Their agreement receives no extra evidentiary weight because both used the same
model family and frozen sources. The decisive evidence is the exact current
rule and report text.[2][3]

The Crocs control also returns HALT under the full contract, but for a different
reason. Its report provides only three annual observations of the selected
owner-cash metric, while the rule requires five to ten years including a weak
period. Historical operating losses do not by themselves prove recurring
negative owner cash. Crocs therefore lacks enough same-metric evidence to
validate normalized V0 and the positive path; Nintendo supplies a signed
negative core-cash observation and names a recurring platform cycle. The
current rule distinguishes an established unrepresentable path from ordinary
demand uncertainty, while halting both unsupported published applications for
their respective defects.[2][3]

### Primary history does not establish one comparable cash cycle

The annual-report tables are unambiguous native-text tables, and rendered pages
confirmed every sign, year heading, unit, and row association below. Values are
JPY billions; CFO is cash flow from operating activities.[4][5][6]

| FY | Operating profit | CFO | Analytical phase context (not an issuer label) |
|--:|--:|--:|:--|
| 2013 | -36.410 | -40.390 | Pre-Switch loss and cash-use year.[4] |
| 2014 | -46.425 | -23.114 | Pre-Switch loss and cash-use year.[4] |
| 2015 | 24.770 | 60.293 | Recovery before Switch.[4] |
| 2016 | 32.881 | 55.190 | Recovery before Switch.[4] |
| 2017 | 29.362 | 19.101 | Switch launched worldwide on March 3, 2017.[4] |
| 2018 | 177.557 | 152.208 | Switch expansion.[5] |
| 2019 | 249.701 | 170.529 | Switch expansion.[5] |
| 2020 | 352.370 | 347.753 | Switch expansion.[5] |
| 2021 | 640.634 | 612.106 | Strong Switch software and hardware year.[5] |
| 2022 | 592.760 | 289.661 | Late Switch period.[6] |
| 2023 | 504.375 | 322.843 | Late Switch period.[6] |
| 2024 | 528.941 | 462.097 | Late Switch period.[6] |
| 2025 | 282.553 | 12.069 | Pre-Switch-2 inventory build year.[6] |
| 2026 | 360.117 | 289.789 | Switch 2 launched in June 2025.[6] |

Nintendo says new-product launch periods can temporarily move receivables,
payables, inventories, and operating cash. Its FY2026 statement shows inventory
cash use of JPY333.837 billion in FY2025 and JPY27.591 billion in FY2026.[6]
That timing is economically relevant rather than a detached accounting anomaly.

The history proves a large operating and cash cycle but does not supply a
comparable signed core-cash series across one unchanged business cycle. Net
sales rose from JPY489.095 billion in FY2017 to JPY2,313.051 billion in FY2026,
and Switch 2 succeeds a much larger Switch installed base.[4][6] Damodaran's
normalization guidance says absolute averaging should cover an entire cycle and
is best suited to firms that have not changed scale. It also says replacing
current earnings with normalized earnings assumes first-period normalization;
if normalization takes several periods, that value is too high.[7] Brain prior
work independently requires scale, profit, reinvestment, working capital,
claims, and terminal state to describe one coherent condition and treats path
and scenario models as alternatives when phase timing is uncertain.[8]

Therefore the published FY2022-FY2026 core-cash series is useful for exposing a
signed path and launch working-capital effect, but it cannot establish a normal
future console cycle. The matched tests below are timing sensitivities only.
A coherent second comparator linking software mix, hardware economics,
inventory, facilities, research spending, taxes, and terminal state was not
built because the checked evidence does not support those forward phase values.
Inventing them would defeat the test.

### Baseline arithmetic reproduces; the method label does not

The displayed annual core-cash figures average to JPY229.74 billion, shown as
V0 = 229.7 in the report. Two independent calculations using V0 = 229.74
reproduced the published scenario components and rounded per-share values:

| Case | Reproduced PV years 1-10 | Published | Reproduced PV terminal | Published | Reproduced value/share | Published |
|:--|--:|--:|--:|--:|--:|--:|
| Bear | 1,050.092 | 1,050.1 | 467.024 | 467.0 | 2,267.913 | 2,268 |
| Base | 1,610.161 | 1,610.1 | 1,360.436 | 1,360.4 | 3,656.341 | 3,656 |
| Bull | 2,122.554 | 2,122.5 | 2,429.785 | 2,429.7 | 5,250.396 | 5,250 |

Using the displayed one-decimal V0 = 229.7 reproduces the Base no-growth value
at JPY3,225.697, which rounds to the published JPY3,226. It also reproduces the
case ordering, 30% and 50% price levels, and price premiums. The arithmetic is
not the defect. The defect is that mechanically reproducible outputs are
presented as an applicable completed Cash DCF and combined intrinsic value after
the method gate has failed.[2][3]

The executed displayed-input raw outputs are below. `cash` and `pv` give years
1 through 10 in JPY billions. Price premium is relative to modeled value.

```text
case=Bear
cash=211.324000,194.418080,178.864634,164.555463,151.391026,151.391026,151.391026,151.391026,151.391026,151.391026
pv=192.112727,160.676099,134.383647,112.393595,94.001916,85.456287,77.687534,70.625031,64.204574,58.367794
pv_explicit=1049.909204 terminal_pv=466.942353 value_per_share=2267.683914 price_premium_pct=248.20

case=Base
cash=236.591000,243.688730,250.999392,258.529374,266.285255,271.610960,277.043179,282.584043,288.235724,294.000438
pv=215.082727,201.395645,188.579558,176.579041,165.342193,153.317306,142.166956,131.827541,122.240084,113.349896
pv_explicit=1609.880948 terminal_pv=1360.198752 value_per_share=3655.892452 price_premium_pct=115.98

case=Bull
cash=252.670000,277.937000,305.730700,336.303770,369.934147,384.731513,400.120773,416.125604,432.770629,450.081454
pv=229.700000,229.700000,229.700000,229.700000,229.700000,217.170909,205.325223,194.125666,183.536993,173.525884
pv_explicit=2122.184675 terminal_pv=2429.362378 value_per_share=5249.708383 price_premium_pct=50.41
```

### Matched timing changes the number, not the decision

The predeclared displayed-input smooth Base has ten-year undiscounted cash of
JPY2,669.568094 billion. Each matched path scales the two repeated signed
five-year profiles by 1.16199534 so its ten-year total is identical. Both hold
terminal cash, terminal PV, equity adjustment, associates, shares, and required
return fixed.

| Path | PV years 1-10 | Value/share | Change from smooth Base | Price premium | Decision result |
|:--|--:|--:|--:|--:|:--|
| Smooth positive Base | 1,609.881 | 3,655.892 | Baseline | 115.98% | Price remains far above Base. |
| Launch-first signed path | 1,707.721 | 3,740.759 | +2.32% | 111.08% | No method, case-order, price-boundary, thesis, or price-conclusion change. |
| Expansion-first signed path | 1,717.059 | 3,748.858 | +2.54% | 110.62% | No method, case-order, price-boundary, thesis, or price-conclusion change. |

The signed paths are worth slightly more, not less, because the largest positive
amounts occur earlier than in the smooth growth path and the negative amounts
occur later. This contradicts the provisional directional expectation that a
cycle-explicit path would necessarily lower value. It does not contradict the
method-fit result. Equal total cash can move value in either direction depending
on order, and these two arbitrary phase placements do not validate a forecast.

```text
path=launch-first
cash=262.727146,323.848101,475.604693,329.658078,-57.053971,262.727146,323.848101,475.604693,329.658078,-57.053971
pv=238.842860,267.643059,357.328845,225.160903,-35.426027,148.302625,166.185282,221.873099,139.807206,-21.996776
pv_explicit=1707.721076 terminal_pv=1360.198752 value_per_share=3740.758807 price_premium_pct=111.08

path=expansion-first
cash=323.848101,475.604693,329.658078,-57.053971,262.727146,323.848101,475.604693,329.658078,-57.053971,262.727146
pv=294.407365,393.061729,247.676993,-38.968630,163.132887,182.803810,244.060409,153.787926,-24.196453,101.292688
pv_explicit=1717.058726 terminal_pv=1360.198752 value_per_share=3748.858267 price_premium_pct=110.62
```

### Executed calculation package

The exact predeclaration, Python Decimal calculator, Node.js calculator, and raw
JSON outputs were frozen before comparison. Their SHA-256 values were:

```text
predeclaration 9739d021c63bb9df91515afd6b3b61f8dd5b9daaa5ee96b6c7f1b8cf62329a21
python         8733a68e12c7ba18ead54b0369024b7073873b260d41e93d74502677655fd2e0
node           dc166f37177743d887ab4f3449ee29cda8f6284552ac6091c9d2ffa707926d23
python-json    f088b5d8cb658ac15478b4f72c5a15a3c58159332e7d9fd1bfe1acae4f4f8366
node-json      4a9eb007c31da960d1ab83741e49bdcdd2b0896881998ce55bf97276d113e420
```

The verifier compared 221 numeric fields and returned zero failures at relative
tolerance 1e-11 and absolute tolerance at least 1e-9. The two calculators used
separate implementations: iterative Decimal arithmetic and vectorized
JavaScript Number arithmetic. The full material raw outputs are preserved above;
the exact governing formulas are those in the current simple-DCF framework.[2]
No claim of blind or model-independent calculation is made.

The exact predeclaration bytes used before calculation are preserved here:

```text
Nintendo cycle-path DCF applicability - predeclared calculation contract
Pipeline: 20261001T033647Z
Recorded before any valuation-result calculation in this session.

Published smooth baseline to reproduce
- V0: JPY 229.7 billion.
- Required return: 10%.
- Base: g1 3%, g2 2%, X 12.
- Bull: g1 10%, g2 4%, X 14.
- Bear: g1 -8%, g2 0%, X 8.
- Common pre-associate equity adjustment: JPY 924.7 billion.
- Associate values: Bear 27*8*0.8; Base 40*10*0.8; Bull 60*12*0.8.
- Shares: 1.152873 billion. Price: JPY 7,896.
- Reproduce each of ten annual cash flows, their PVs, terminal cash, terminal value and PV, total equity value, value/share, 30% and 50% price levels, price premium, and the Base no-growth sensitivity.

Matched timing test fixed before viewing its values
- Purpose: isolate timing only; this is not a forecast.
- Historical signed core-cash profile from the current report: JPY 278.7, 283.7, 409.3, -49.1, and 226.1 billion.
- Phase labels used for ordering: launch 226.1; expansion 278.7; peak 409.3; fade 283.7; trough -49.1. The labels are an analytical mapping, not issuer labels.
- Launch-first path: [226.1, 278.7, 409.3, 283.7, -49.1] repeated twice.
- Expansion-first alternative: [278.7, 409.3, 283.7, -49.1, 226.1] repeated twice. This represents the valuation date already being in the post-launch expansion year.
- For each path, multiply every signed profile amount by one common factor k = the smooth Base ten-year undiscounted cash total divided by the unscaled path total. This keeps the ten-year undiscounted cash total exactly equal to smooth Base and preserves the observed signed relative shape.
- Hold the terminal cash equal to smooth Base year-10 cash, apply X=12, and discount it from year 10 exactly as in the baseline. Hold the Base equity adjustment, associate value, shares, and required return fixed.
- Compare explicit-period PV, operating PV, total equity value, value/share, and price premium with smooth Base.
- A second calculation must independently reproduce all outputs before they are used.

Decision rules fixed before viewing results
- A numerical difference is decision-relevant only if it changes method applicability, valuation type, confidence, Bear/Base/Bull ordering, a 30% or 50% price boundary, thesis status, or the price conclusion.
- If the full current applicability contract already requires the same method correction, the timing calculation cannot by itself justify a framework amendment.
- If the five-year profile cannot establish a comparable full cycle or phase timing, label the paths as matched timing sensitivities, not forecasts or cycle-normalized intrinsic values.
```

The exact first calculator bytes were:

```python
#!/usr/bin/env python3
from decimal import Decimal, getcontext
import json

getcontext().prec = 40
D = Decimal
V0 = D('229.7')
R = D('0.10')
ONE = D('1')
COMMON_A = D('924.7')
SHARES = D('1.152873')
PRICE = D('7896')

SCENARIOS = {
    'Bear': (D('-0.08'), D('0'), D('8'), D('27') * D('8') * D('0.8')),
    'Base': (D('0.03'), D('0.02'), D('12'), D('40') * D('10') * D('0.8')),
    'Bull': (D('0.10'), D('0.04'), D('14'), D('60') * D('12') * D('0.8')),
}

def calc(g1, g2, x, associate):
    cash = []
    pv = []
    for t in range(1, 11):
        if t <= 5:
            c = V0 * (ONE + g1) ** t
        else:
            c = V0 * (ONE + g1) ** 5 * (ONE + g2) ** (t - 5)
        cash.append(c)
        pv.append(c / (ONE + R) ** t)
    terminal_cash = cash[-1]
    terminal_value = terminal_cash * x
    terminal_pv = terminal_value / (ONE + R) ** 10
    adjustment = COMMON_A + associate
    equity = sum(pv, D('0')) + terminal_pv + adjustment
    value_per_share = equity / SHARES
    return {
        'cash': cash,
        'pv': pv,
        'cash_total': sum(cash, D('0')),
        'pv_explicit': sum(pv, D('0')),
        'terminal_cash': terminal_cash,
        'terminal_value': terminal_value,
        'terminal_pv': terminal_pv,
        'associate': associate,
        'adjustment_total': adjustment,
        'equity_value': equity,
        'value_per_share': value_per_share,
        'price_at_30_discount': value_per_share * D('0.70'),
        'price_at_50_discount': value_per_share * D('0.50'),
        'price_premium_to_value': PRICE / value_per_share - ONE,
    }

def path_calc(label, raw, base):
    raw_total = sum(raw, D('0'))
    k = base['cash_total'] / raw_total
    cash = [v * k for v in raw]
    pv = [cash[t - 1] / (ONE + R) ** t for t in range(1, 11)]
    terminal_cash = base['terminal_cash']
    terminal_value = terminal_cash * D('12')
    terminal_pv = terminal_value / (ONE + R) ** 10
    adjustment = COMMON_A + D('320')
    equity = sum(pv, D('0')) + terminal_pv + adjustment
    value_per_share = equity / SHARES
    return {
        'label': label,
        'raw': raw,
        'raw_total': raw_total,
        'scale_factor': k,
        'cash': cash,
        'pv': pv,
        'cash_total': sum(cash, D('0')),
        'pv_explicit': sum(pv, D('0')),
        'terminal_cash': terminal_cash,
        'terminal_value': terminal_value,
        'terminal_pv': terminal_pv,
        'adjustment_total': adjustment,
        'equity_value': equity,
        'value_per_share': value_per_share,
        'price_at_30_discount': value_per_share * D('0.70'),
        'price_at_50_discount': value_per_share * D('0.50'),
        'price_premium_to_value': PRICE / value_per_share - ONE,
        'delta_vs_smooth_value_per_share': value_per_share - base['value_per_share'],
    }

def encode(value):
    if isinstance(value, Decimal):
        return format(value, 'f')
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, list):
        return [encode(v) for v in value]
    return value

results = {name: calc(*params) for name, params in SCENARIOS.items()}
no_growth = calc(D('0'), D('0'), D('12'), D('320'))
base = results['Base']
launch_cycle = [D('226.1'), D('278.7'), D('409.3'), D('283.7'), D('-49.1')]
expansion_cycle = [D('278.7'), D('409.3'), D('283.7'), D('-49.1'), D('226.1')]
paths = {
    'launch_first': path_calc('launch-first', launch_cycle + launch_cycle, base),
    'expansion_first': path_calc('expansion-first', expansion_cycle + expansion_cycle, base),
}
output = {
    'method': 'Python Decimal iterative annual cash and PV calculation',
    'inputs': {'V0': V0, 'required_return': R, 'common_A': COMMON_A, 'shares': SHARES, 'price': PRICE},
    'scenarios': results,
    'base_no_growth': no_growth,
    'paths': paths,
}
print(json.dumps(encode(output), indent=2, sort_keys=True))
```

The exact second calculator bytes were:

```javascript
#!/usr/bin/env node
'use strict';

const V0 = 229.7;
const r = 0.10;
const commonA = 924.7;
const shares = 1.152873;
const price = 7896;

const scenarios = {
  Bear: {g1: -0.08, g2: 0, x: 8, associate: 27 * 8 * 0.8},
  Base: {g1: 0.03, g2: 0.02, x: 12, associate: 40 * 10 * 0.8},
  Bull: {g1: 0.10, g2: 0.04, x: 14, associate: 60 * 12 * 0.8}
};

function sum(values) {
  return values.reduce((a, b) => a + b, 0);
}

function calc({g1, g2, x, associate}) {
  const cash = Array.from({length: 10}, (_, index) => {
    const t = index + 1;
    return t <= 5
      ? V0 * Math.pow(1 + g1, t)
      : V0 * Math.pow(1 + g1, 5) * Math.pow(1 + g2, t - 5);
  });
  const pv = cash.map((value, index) => value / Math.pow(1 + r, index + 1));
  const terminalCash = cash[9];
  const terminalValue = terminalCash * x;
  const terminalPv = terminalValue / Math.pow(1 + r, 10);
  const adjustment = commonA + associate;
  const equity = sum(pv) + terminalPv + adjustment;
  const valuePerShare = equity / shares;
  return {
    cash,
    pv,
    cash_total: sum(cash),
    pv_explicit: sum(pv),
    terminal_cash: terminalCash,
    terminal_value: terminalValue,
    terminal_pv: terminalPv,
    associate,
    adjustment_total: adjustment,
    equity_value: equity,
    value_per_share: valuePerShare,
    price_at_30_discount: valuePerShare * 0.70,
    price_at_50_discount: valuePerShare * 0.50,
    price_premium_to_value: price / valuePerShare - 1
  };
}

function pathCalc(label, raw, base) {
  const rawTotal = sum(raw);
  const scaleFactor = base.cash_total / rawTotal;
  const cash = raw.map(value => value * scaleFactor);
  const pv = cash.map((value, index) => value / Math.pow(1 + r, index + 1));
  const terminalCash = base.terminal_cash;
  const terminalValue = terminalCash * 12;
  const terminalPv = terminalValue / Math.pow(1 + r, 10);
  const adjustment = commonA + 320;
  const equity = sum(pv) + terminalPv + adjustment;
  const valuePerShare = equity / shares;
  return {
    label,
    raw,
    raw_total: rawTotal,
    scale_factor: scaleFactor,
    cash,
    pv,
    cash_total: sum(cash),
    pv_explicit: sum(pv),
    terminal_cash: terminalCash,
    terminal_value: terminalValue,
    terminal_pv: terminalPv,
    adjustment_total: adjustment,
    equity_value: equity,
    value_per_share: valuePerShare,
    price_at_30_discount: valuePerShare * 0.70,
    price_at_50_discount: valuePerShare * 0.50,
    price_premium_to_value: price / valuePerShare - 1,
    delta_vs_smooth_value_per_share: valuePerShare - base.value_per_share
  };
}

const results = Object.fromEntries(Object.entries(scenarios).map(([name, values]) => [name, calc(values)]));
const noGrowth = calc({g1: 0, g2: 0, x: 12, associate: 320});
const base = results.Base;
const launchCycle = [226.1, 278.7, 409.3, 283.7, -49.1];
const expansionCycle = [278.7, 409.3, 283.7, -49.1, 226.1];
const paths = {
  launch_first: pathCalc('launch-first', launchCycle.concat(launchCycle), base),
  expansion_first: pathCalc('expansion-first', expansionCycle.concat(expansionCycle), base)
};

console.log(JSON.stringify({
  method: 'Node.js Number vectorized annual cash and PV calculation',
  inputs: {V0, required_return: r, common_A: commonA, shares, price},
  scenarios: results,
  base_no_growth: noGrowth,
  paths
}, null, 2));
```

The exact comparison bytes were:

```python
#!/usr/bin/env python3
import json
import math
import sys

if len(sys.argv) != 3:
    raise SystemExit('usage: compare-dcf.py decimal.json node.json')

with open(sys.argv[1], encoding='ascii') as handle:
    left = json.load(handle)
with open(sys.argv[2], encoding='ascii') as handle:
    right = json.load(handle)

failures = []
checked = 0

def numeric(value):
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return None
    return None

def compare(a, b, path='root'):
    global checked
    if isinstance(a, dict) and isinstance(b, dict):
        keys = (set(a) | set(b)) - {'method'}
        for key in sorted(keys):
            if key not in a or key not in b:
                failures.append(f'{path}.{key}: missing key')
            else:
                compare(a[key], b[key], f'{path}.{key}')
        return
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            failures.append(f'{path}: length {len(a)} != {len(b)}')
            return
        for index, (x, y) in enumerate(zip(a, b)):
            compare(x, y, f'{path}[{index}]')
        return
    x = numeric(a)
    y = numeric(b)
    if x is not None and y is not None:
        checked += 1
        tolerance = max(1e-9, 1e-11 * max(abs(x), abs(y), 1.0))
        if not math.isclose(x, y, rel_tol=1e-11, abs_tol=tolerance):
            failures.append(f'{path}: {x} != {y}')
        return
    if a != b:
        failures.append(f'{path}: {a!r} != {b!r}')

compare(left, right)
print(f'CHECKED_NUMERIC_FIELDS={checked}')
print(f'FAILURES={len(failures)}')
for failure in failures:
    print(failure)
raise SystemExit(1 if failures else 0)
```

## Alternatives and Implications

| Alternative | Evidence-supported effect | Cost and disposition |
|:--|:--|:--|
| Do nothing | Preserves the current report and its price conclusion. | Leaves an inapplicable positive path labeled completed Cash DCF and intrinsic value despite the explicit current gate.[2][3] |
| Correct report application only | Mark simple DCF Not applicable; retain the smooth calculation only as a separately labeled what-if if useful; show unsupported values as N/A until a fitting method is completed. | Smallest response already required by the current framework and company template; no Forge implementation authority follows. |
| Clarify the existing applicability sentence | Could make the negative-year consequence harder to overlook. | The exact rule already states the consequence, and both cold readers applied it. This test found no unique decision value from another sentence. |
| Add a Nintendo cycle-schedule method now | Would represent signed years and uneven funding explicitly. | Not supported: the five-year core-cash series is not a comparable full cycle, scale changed, and forward phase cash, reinvestment, working capital, and terminal state are unknown. |
| Use coherent cycle scenarios | Avoids pretending that one phase order is known and matches Brain prior work. | Potentially appropriate future research, but current evidence does not support complete cash-system scenarios; inventing them would add false precision.[8] |

For a Buffett and Munger style decision, the important result is not that one
path produces JPY85-93 more per share. It is that the current price remains more
than twice both matched values, while the evidence does not support calling
those values cycle forecasts. A good business and a reproducible spreadsheet do
not remove the need for a method that represents the business's cash pattern or
a margin of safety against model uncertainty.[3][8]

The bounded evidence supports a report-application correction, not a framework
amendment or a new cycle model. It also exposes a second current application
issue in Crocs: the full current rule requires more same-metric history and a
cash-conversion bridge before its completed Cash DCF label is supported. That
control does not prove every existing report is wrong; the current corpus has
only two reports.

## Response to Feedback and Remaining Questions

No prior evaluation exists for this pipeline.

The root idea's material tasks are answered as follows:

- The exact current applicability contract was frozen and applied before the
  timing calculation. Two isolated readers separately returned HALT for
  Nintendo; their outputs are preserved without independent-evidence weight.
- The published Bear/Base/Bull arithmetic, terminal values, share basis,
  price levels, case ordering, and no-growth check reproduce. Arithmetic does
  not rescue method applicability.
- Issuer tables establish large operating and operating-cash variation from
  FY2013-FY2026, two launch dates, and launch-related working-capital timing.
  They do not provide a comparable signed core-cash cycle at unchanged scale.
- The predeclared matched timing test preserves total explicit cash and terminal
  cash. Both plausible orderings raise rather than lower value by 2.32%-2.54%,
  but change no decision-relevant field.
- A coherent full cash-system comparator was not performed because phase cash,
  investment, working capital, tax, and terminal assumptions are unsupported.
  This is an evidence limit, not a zero result.
- Crocs does not establish the same recurring signed-benefit cycle, but its
  published valuation separately lacks the five-to-ten-year same-metric history
  and forward cash-conversion support required by the full current rule.
- The smallest supported response is application correction. Another framework
  rule or a Nintendo-specific schedule has no demonstrated incremental value.

Remaining decision-relevant questions are whether a later Nintendo source set
can support coherent console-cycle cash scenarios at current scale, whether
retained report workings can establish the forward cash-conversion and terminal
basis, and whether the same applicability failures recur prospectively after
explicit enforcement of the current rule. Those questions require changed
evidence. Repeating the present five-year timing exercise would not answer them.

Confidence is medium. Confidence is high that the current rule returns HALT for
Nintendo and that the published arithmetic and matched-path outputs reproduce:
exact source text, rendered issuer tables, two cold readings, two calculator
implementations, and 221 matched fields agree.[2][3][4][5][6] Overall confidence
remains medium because the core-cash profile covers only five years, phase labels
are analytical rather than issuer-defined, two readers share one model family,
and no complete current-scale console-cycle cash schedule exists. Confidence
would rise if a retained full-cycle cash bridge and coherent phase scenarios
were independently reproduced. It would fall if a resolving current-framework
passage or complete cash record showed that the positive two-stage path already
represents Nintendo's annual benefits despite the signed cycle.

This report issues no ADVANCE verdict, proposal, company-report edit, framework
change, or implementation. `LEARNINGS.md` remains unchanged as required for a
research stage.[9]

## Sources

1. `forge/ideas/nintendo-cycle-path-dcf-applicability-r01.md` -- root question,
   frozen test plan, decision-value threshold, alternatives, and stop conditions.
   [high]
2. `investing-hub:frameworks/simple-dcf.md` -- exact positive-path applicability
   gate, input, scenario, arithmetic, verification, type-label, and HALT rules.
   [high]
   - `investing-hub:frameworks/sector-metrics.md` -- cycle-normalized method
     selection, uneven signed cash schedule, and method-fit gate. [high]
   - `investing-hub:governance/template-company.md` -- alternative-method,
     Not-applicable, Not-calculable, type-label, and N/A output requirements.
     [high]
3. `investing-hub:companies/NTDOY.md` -- current console-cycle description,
   signed five-year core cash, DCF inputs and outputs, associates basis, price,
   confidence, and thesis conclusion. [high]
   - `investing-hub:companies/CROX.md` -- current positive-path control,
     three-year owner-cash history, historical operating-loss references,
     DCF inputs, and fashion-demand uncertainty. [high]
4. Nintendo Co., Ltd. "Annual Report 2017," 2017, pp. 2 and 7.
   FY2013-FY2017 key financial data, signs and units, and the March 3, 2017
   worldwide Switch launch were checked in native text and a rendered table.
   https://www.nintendo.co.jp/ir/pdf/2017/annual1703e.pdf [high]
5. Nintendo Co., Ltd. "Annual Report 2021," 2021, pp. 2 and 12-13.
   FY2017-FY2021 key financial data, signs and units, and the strong Switch
   software and hardware period were checked in native text and a rendered table.
   https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf [high]
6. Nintendo Co., Ltd. "Annual Report 2026," 2026, pp. 2, 8, 15-16, and
   62-63. FY2022-FY2026 key data, June 2025 Switch 2 launch, launch-period
   working-capital warning, inventory cash movements, and operating cash flows
   were checked in native text and a rendered table.
   https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf [high]
7. Aswath Damodaran. "More on normalizing earnings," undated; accessed
   2026-10-01. Entire-cycle averaging, scale limits, and the timing consequence
   of immediate versus multi-period normalization were checked.
   https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/normearn.htm
   [high]
8. `agentic-brain:library/valuation-screening/valuation-of-cyclical-companies-normalizing-earnings-across-the-business-cycle.md` -- full-cycle normalization, scale, complete cash-system consistency, path and scenario alternatives, and terminal-state limits. [medium]
   - `agentic-brain:library/valuation-screening/discounted-cash-flow-dcf-methodology.md` -- claim-matched cash, reinvestment, scenarios, terminal state, and model uncertainty. [medium]
9. `forge/protocol.md` -- selection, research independence, artifact, source,
   transaction, handoff, and read-only-learning rules. [high]
   - `STATUS.md` -- selected pipeline and preserved unselected rows at starting
     HEAD. [high]
   - `LEARNINGS.md` -- preserved evidence, full-contract comparator, and
     unattended-tool lessons read before research and kept unchanged. [high]
   - `logbook/progress.log` -- exact prior handoff through ENT-030. [high]
   - `logbook/errors.log` -- prior pipeline fault boundary through ENT-036.
     [high]
