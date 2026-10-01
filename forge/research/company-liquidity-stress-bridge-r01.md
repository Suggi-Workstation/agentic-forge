---
name: company-liquidity-stress-bridge
id: 20261001T063212Z
tier: research
pipeline: 20261001T043634Z
author: Researcher
tags: [value-investing, financial-health, liquidity, reproducibility]
links:
  - forge/ideas/company-liquidity-stress-bridge-r01.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - governance/template-research.md
  - investing-hub:frameworks/financial-health.md
  - investing-hub:governance/template-company.md
  - investing-hub:companies/CROX.md
  - investing-hub:companies/NTDOY.md
  - investing-hub:data/crox-financial.md
  - agentic-brain:library/finance/integrated-financial-modeling.md
  - agentic-brain:library/finance/working-capital-management-cash-conversion-cycle.md
  - https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm
  - https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/crox-20251231.htm
  - https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf
  - https://www.nintendo.co.jp/ir/pdf/2026/260806e.pdf
  - https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf
  - https://www.federalregister.gov/documents/full_text/xml/2010/09/28/2010-23744.xml
confidence: medium
---
# Research: Company Liquidity Stress Bridge

## Question and Method

This report tests the root idea's exact question: can an independent reader
reproduce the Crocs and Nintendo stressed-liquidity headroom figures, and does
one compact dated cash bridge change a financial-health classification,
confidence, thesis, final verdict, first-shortfall finding, or review trigger
beyond explicit application of the complete current contract?[1]

Research began at clean Forge HEAD
`b215f30c716bfbf8cc79b33e66480fc0ec53bbc9`. The root idea was authored by
Analyst, so Researcher satisfies the separate-author gate. The older discovery
row remained awaiting human review and unchanged. `LEARNINGS.md` was read and
remained read-only.[8]

Before further targeted retrieval, the provisional explanation was that both
reported terminal values could probably be reconstructed from hidden but simple
assumptions, while neither value established the first liquidity trough. The
contrary explanation was that the report narratives and cited filings already
fixed every material input and date, making a bridge only a larger display. The
decisive gaps were usable-cash perimeters, the two operating floors, cash-flow
and mandatory-use dates, facility availability, double counting, five-year debt
maturities, and whether the complete current contract already required every
correction.[1][2]

The investigation used this fixed order:

1. Freeze the root idea, current financial-health framework, company template,
   both company reports, Crocs statement history, Forge method memory, selected
   board, and repository snapshot.[1][2][3][8]
2. Before constructing a candidate display, obtain two isolated cold readings
   of both reports under the complete current contract. Preserve each material
   classification and reason separately. Both readers used the same model
   family and sources, so agreement tests reproducibility, not independent
   truth.
3. Inspect Crocs' June 2026 filing and 2025 annual filing for cash, restrictions,
   operating cash, capex, leases, tax claims, facilities, covenants, and exact
   debt maturities.[4]
4. Inspect Nintendo's annual report, June 2026 quarterly balance sheet, FY2027
   dividend forecast, project schedule, leases, and borrowings. Native PDF text
   was checked against 300-DPI renders of the material tables.[5]
5. Query fresh Forge, Brain, and Investing Hub indexes; read the relevant full
   files rather than snippets. Use Brain prior work only for method, not as a
   substitute for issuer facts.[6]
6. After the reconstructions and cold readings were known, freeze one candidate
   display and decision rule before the author's exact calculation. Run a
   Decimal/Python calculator and an independently written Node.js calculator;
   compare every numeric output under fixed tolerance.
7. Compare doing nothing, report-only correction, a retained working record,
   the compact report bridge, and a framework or template amendment. The
   candidate counts as useful only if it changes a supported decision beyond
   the complete current contract.[1][2]

SEC guidance independently supports disclosing internal and external liquidity
sources, known commitments and uncertainties, restrictions on material cash or
investment portfolios, and information necessary to understand contractual
amounts and timing. It does not prescribe this candidate table or either local
operating floor.[7]

## Evidence and Findings

### Both published terminal figures reproduce only after hidden assumptions

Crocs reported USD170.276 million of cash at June 30, 2026, USD134 million
borrowed under a revolver maturing in November 2027, USD500 million of Term Loan
B principal due February 17, 2029, and USD350 million of notes due March 15,
2029. The filing also reported USD865.4 million of remaining main-revolver
capacity, but that commitment expires in November 2027, and the term facility
was fully drawn.[4] The report publishes USD200 million of stressed annual CFO,
USD75 million of annual capex, no buybacks, a USD134 million revolver repayment,
a USD100 million tax payment, and USD100 million of minimum cash.[3]

The published two-year terminal value reproduces exactly, within rounding, only
with an unreported 10% opening-cash haircut:

```text
170.276 x 90% + 2 x (200 - 75) - 134 - 100 = 169.248
169.248 - 100 floor = 69.248 headroom
```

That reconstruction does not reproduce the word `minimum`. The inferred opening
usable cash is USD153.248 million, only USD53.248 million above the floor, before
any dated flow. The USD100 million tax amount and payment date are unsupported,
and the report does not show stressed covenant ratios or the timing of annual
cash generation and capex.[2][3][4]

Nintendo reported JPY1,544.090 billion of cash and deposits and JPY423.818
billion of current securities at June 30, 2026. The quarterly source reports no
borrowings and no quarterly cash-flow statement. The annual report shows a
JPY230 billion facilities plan whose projects began in April or December 2025
and finish in March 2028 or March 2029; it does not provide remaining spending
at June 2026 or an annual payment schedule. It also reports JPY7.525 billion of
future non-cancelable operating-lease payments and says finance leases are
immaterial.[5]

Nintendo's published terminal value likewise requires hidden assumptions: a
10% haircut to cash plus current securities, JPY25 billion of ordinary annual
capex, JPY76.7 billion of annual facilities spending, the entire JPY7.525
billion operating-lease commitment, and one FY2027 dividend of JPY162 on
1,152,828,616 shares. Exact arithmetic is:[3][5]

```text
opening liquid assets                  1,967.908000
less inferred 10% haircut               196.790800
less stressed CFO, years 1 and 2         200.000000
less inferred ordinary capex              50.000000
less inferred facilities spending        153.400000
less forecast FY2027 dividend             186.758236
less all operating-lease commitments        7.525000
published terminal reconstructed       1,173.433964
headroom above JPY500 floor               673.433964
```

The current contract says not to deduct operating leases already in cash
generation and, for operating leases, to retain rent without deducting the same
commitment again as debt.[2] Removing that separate lease deduction raises the
same annual-checkpoint terminal to JPY1,180.959 billion. The calculation remains
a convention, not a dated minimum: project payments, dividend installments,
within-year CFO, and the current securities' June maturity and access details
are not available. The JPY500 billion floor, 10% haircut, and JPY25 billion
ordinary capex are not disclosed. Ordinary capex may also overlap the gross
facilities plan; the source record cannot resolve that premise.[3][5]

### The separate cold baselines agree on failure but not severity

The following material outputs were preserved separately before the candidate
was built. No evidentiary weight is assigned to agreement because both readers
used the same model family and evidence. Auxiliary wording is not claimed as a
separate independent record.

| Reader | Crocs complete-current-contract result | Nintendo complete-current-contract result |
|:--|:--|:--|
| A | Positive two-year claim fails; the five-year no-refinancing contract exposes the USD500 million February 2029 term maturity and USD350 million March 2029 note. Reader A classified liquidity and Overall **Fragile / Medium**. | Positive Strong claim fails its dated and traceable gates. Large fallback headroom supported **Adequate / Medium** liquidity and retaining **Watch / Medium** overall, conditional on correction. |
| B | Positive claim fails because USD69 million is not the minimum and timing, usable cash, tax, floor, and covenants are unsupported. Reader B classified liquidity **Unknown / Low** and Overall **Unclear / Low**, declining to extend annual totals. | Positive Strong claim fails because timing, access, leases, projects, and capex are unresolved. Reader B classified liquidity **Unknown / Low** and Overall **Unclear / Low**. |

The Crocs disagreement is resolved by a bound that does not require prorating
cash inside 2029. Starting from the reconstructed June 2028 terminal, credit the
entire third year's USD125 million of stressed post-capex cash before February
17, 2029. Cash would still be only USD294.248 million before the USD500 million
term maturity and USD-205.752 million after it. The first proven shortfall is
therefore no later than February 17, 2029; the exact earlier trough remains
unknown. The later USD350 million note deepens the maximum-cash deficit to
USD-555.752 million. This is an established uncovered obligation under the
current scenario, so the framework's Fragile override applies even though an
earlier shortfall date cannot be determined.[2][4]

For Nintendo, the strict positive-claim gate controls. A cash-only fallback that
excludes all JPY423.818 billion of current securities, retains the 10% cash
haircut, and keeps every other conservative candidate use still ends at
JPY799.523 billion, or JPY299.523 billion above the floor. That is contrary
evidence against Fragile, but it does not establish a dated minimum. The
supportable current-contract result is therefore liquidity **Unknown / Low** and
Overall **Unclear / Low** until timing and access are resolved. Reader A's
conditional Adequate/Watch interpretation remains a documented contrary view,
not a hidden disagreement.[2][5]

### The compact candidate makes existing rules visible but adds no decision

The candidate was frozen only after both reconstructions. Unknown dates remain
unknown; annual rows are model conventions. Accessible funding is zero in the
stress because Crocs' main commitment expires before the 2029 maturities, its
USD15 million Asia facility has no verified 2029 commitment and cannot cure the
bounded deficit, and Nintendo discloses no committed facility used in the
analysis.[4][5]

Crocs candidate, USD millions:

| Checkpoint | Opening usable cash | Stressed cash generation | Accessible funding | Mandatory outflows | Closing usable cash | Floor / headroom | Evidence status |
|:--|--:|--:|--:|:--|--:|:--|:--|
| 2026-06-30 opening | 170.276 reported | 0 | 0 | 17.028 inferred access haircut | 153.248 | 100 / 53.248 | Haircut and floor unsupported; this is lower than the claimed terminal minimum. |
| 2028-06-30 annual checkpoint | 153.248 | +400.000 CFO | 0 | 150.000 capex; 134.000 revolver; 100.000 tax | 169.248 | 100 / 69.248 | Reproduces the report; flow dates and tax basis remain unknown. |
| 2029-02-17 after Term Loan B | 169.248 | +125.000 maximum third-year post-capex cash, all credited early | 0 | 500.000 term maturity | -205.752 | 100 / -305.752 | First proven shortfall no later than this date; refinancing unavailable. |
| 2029-03-15 after notes | -205.752 | 0, because the full third-year maximum was already credited | 0 | 350.000 notes | -555.752 | 100 / -655.752 | Deficit deepens; exact intra-period path remains unknown. |

Nintendo candidate, JPY billions:

| Checkpoint | Opening usable cash | Stressed cash generation | Accessible funding | Mandatory outflows | Closing usable cash | Floor / headroom | Evidence status |
|:--|--:|--:|--:|:--|--:|:--|:--|
| 2026-06-30 opening | 1,967.908 reported liquid assets | 0 | 0 | 196.791 inferred access haircut | 1,771.117 | 500 / 1,271.117 | Haircut, transferability, and floor unsupported. |
| FY2027 annual checkpoint | 1,771.117 | -150.000 CFO | 0 | 25.000 ordinary capex; 76.700 facilities; 186.758 forecast dividend | 1,332.659 | 500 / 832.659 | Dividend and project dates unknown; dividend is discretionary. |
| FY2028 annual checkpoint | 1,332.659 | -50.000 CFO | 0 | 25.000 ordinary capex; 76.700 facilities | 1,180.959 | 500 / 680.959 | No separate operating-lease deduction; exact minimum date unknown. |

The current framework already requires every decisive feature in these tables:
usable cash, accessible committed funding, maturities, mandatory uses, no
capacity reuse, no uncertain refinancing, shorter periods when annual netting
hides a shortfall, no lease or capex double count, and the first shortfall or
credible headroom.[2] The company template already requires the decisive result
and sufficient assumptions while allowing detailed workings to remain outside
the report.[2] The candidate therefore improves visibility but does not add a
new semantic gate.

The decision comparison is:

| Target | Original report | Complete current contract | Compact candidate | Increment beyond current contract |
|:--|:--|:--|:--|:--|
| Crocs | USD69 million minimum headroom; Adequate liquidity; Overall Watch / Medium. | USD69 is not the minimum; five-year no-refinancing stress has a proven shortfall no later than 2029-02-17; Fragile / Medium. | Same shortfall and classification, displayed row by row. | None. |
| Nintendo | JPY673.4 billion headroom; Strong liquidity; Overall Watch / Medium. | Positive Strong claim fails; exact dated minimum is unknown; liquidity Unknown / Low and Overall Unclear / Low, with large contrary fallback headroom. | Same uncertainty; removes the lease double count and shows JPY680.959 billion at an annual checkpoint. | None. |

The bridge changes both published applications, but explicit enforcement of the
current contract changes them first. A display cannot claim unique detection
when the governing rule already names the omitted maturity, unknown date,
access restriction, and double-count prohibition.

### Executed calculation package

The comparison contract was recorded after the source and reader checks, but
before the author's exact calculator run. It was not blind. Its decision rule
was: count a candidate benefit only if a supported field changes beyond the
complete current contract; unknown dates must remain unknown.

The exact Decimal/Python calculator was:

```python
#!/usr/bin/env python3
from decimal import Decimal, getcontext
import json

getcontext().prec = 40
D = Decimal

crocs_opening = D("170.276")
crocs_haircut = D("0.10")
crocs_floor = D("100")
crocs_cfo = D("200")
crocs_capex = D("75")
crocs_revolver = D("134")
crocs_tax = D("100")
crocs_term = D("500")
crocs_notes = D("350")
crocs_usable = crocs_opening * (D("1") - crocs_haircut)
crocs_terminal = crocs_usable + D("2") * (crocs_cfo - crocs_capex) - crocs_revolver - crocs_tax
crocs_third_year_net = crocs_cfo - crocs_capex
crocs_pre_term_max = crocs_terminal + crocs_third_year_net
crocs_post_term_max = crocs_pre_term_max - crocs_term
crocs_post_notes_max = crocs_post_term_max - crocs_notes

shares = D("1287260000") - D("134431384")
nintendo_opening_cash = D("1544.090")
nintendo_securities = D("423.818")
nintendo_haircut = D("0.10")
nintendo_floor = D("500")
nintendo_cfo_y1 = D("-150")
nintendo_cfo_y2 = D("-50")
nintendo_capex = D("25")
nintendo_facilities = D("76.7")
nintendo_dividend = D("162") * shares / D("1000000000")
nintendo_lease = D("7.525")
nintendo_usable = (nintendo_opening_cash + nintendo_securities) * (D("1") - nintendo_haircut)
nintendo_published_terminal = nintendo_usable + nintendo_cfo_y1 + nintendo_cfo_y2 - D("2") * nintendo_capex - D("2") * nintendo_facilities - nintendo_dividend - nintendo_lease
nintendo_candidate_y1 = nintendo_usable + nintendo_cfo_y1 - nintendo_capex - nintendo_facilities - nintendo_dividend
nintendo_candidate_y2 = nintendo_candidate_y1 + nintendo_cfo_y2 - nintendo_capex - nintendo_facilities
nintendo_cash_only_usable = nintendo_opening_cash * (D("1") - nintendo_haircut)
nintendo_cash_only_terminal = nintendo_cash_only_usable + nintendo_cfo_y1 + nintendo_cfo_y2 - D("2") * nintendo_capex - D("2") * nintendo_facilities - nintendo_dividend


def encode(value):
    if isinstance(value, Decimal):
        return format(value, "f")
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value

output = {
    "crocs": {
        "opening_reported": crocs_opening,
        "opening_usable_inferred": crocs_usable,
        "opening_headroom_inferred": crocs_usable - crocs_floor,
        "published_terminal_reconstructed": crocs_terminal,
        "published_terminal_headroom": crocs_terminal - crocs_floor,
        "max_cash_before_2029_term_maturity": crocs_pre_term_max,
        "max_cash_after_2029_term_maturity": crocs_post_term_max,
        "max_headroom_after_2029_term_maturity": crocs_post_term_max - crocs_floor,
        "max_cash_after_2029_notes": crocs_post_notes_max,
        "max_headroom_after_2029_notes": crocs_post_notes_max - crocs_floor,
    },
    "nintendo": {
        "outstanding_shares": shares,
        "forecast_dividend": nintendo_dividend,
        "opening_usable_inferred": nintendo_usable,
        "opening_headroom_inferred": nintendo_usable - nintendo_floor,
        "published_terminal_reconstructed": nintendo_published_terminal,
        "published_terminal_headroom": nintendo_published_terminal - nintendo_floor,
        "candidate_year1_closing": nintendo_candidate_y1,
        "candidate_year1_headroom": nintendo_candidate_y1 - nintendo_floor,
        "candidate_year2_closing": nintendo_candidate_y2,
        "candidate_year2_headroom": nintendo_candidate_y2 - nintendo_floor,
        "cash_only_terminal": nintendo_cash_only_terminal,
        "cash_only_headroom": nintendo_cash_only_terminal - nintendo_floor,
    },
}
print(json.dumps(encode(output), indent=2, sort_keys=True))
```

The independently written Node.js calculator used the same frozen scalar inputs
and direct formulas:

```javascript
#!/usr/bin/env node
'use strict';

const crocsOpening = 170.276;
const crocsHaircut = 0.10;
const crocsFloor = 100;
const crocsCfo = 200;
const crocsCapex = 75;
const crocsRevolver = 134;
const crocsTax = 100;
const crocsTerm = 500;
const crocsNotes = 350;
const crocsUsable = crocsOpening * (1 - crocsHaircut);
const crocsTerminal = crocsUsable + 2 * (crocsCfo - crocsCapex) - crocsRevolver - crocsTax;
const crocsThirdYearNet = crocsCfo - crocsCapex;
const crocsPreTermMax = crocsTerminal + crocsThirdYearNet;
const crocsPostTermMax = crocsPreTermMax - crocsTerm;
const crocsPostNotesMax = crocsPostTermMax - crocsNotes;

const shares = 1287260000 - 134431384;
const nintendoOpeningCash = 1544.090;
const nintendoSecurities = 423.818;
const nintendoHaircut = 0.10;
const nintendoFloor = 500;
const nintendoCfoY1 = -150;
const nintendoCfoY2 = -50;
const nintendoCapex = 25;
const nintendoFacilities = 76.7;
const nintendoDividend = 162 * shares / 1000000000;
const nintendoLease = 7.525;
const nintendoUsable = (nintendoOpeningCash + nintendoSecurities) * (1 - nintendoHaircut);
const nintendoPublishedTerminal = nintendoUsable + nintendoCfoY1 + nintendoCfoY2 - 2 * nintendoCapex - 2 * nintendoFacilities - nintendoDividend - nintendoLease;
const nintendoCandidateY1 = nintendoUsable + nintendoCfoY1 - nintendoCapex - nintendoFacilities - nintendoDividend;
const nintendoCandidateY2 = nintendoCandidateY1 + nintendoCfoY2 - nintendoCapex - nintendoFacilities;
const nintendoCashOnlyUsable = nintendoOpeningCash * (1 - nintendoHaircut);
const nintendoCashOnlyTerminal = nintendoCashOnlyUsable + nintendoCfoY1 + nintendoCfoY2 - 2 * nintendoCapex - 2 * nintendoFacilities - nintendoDividend;

console.log(JSON.stringify({
  crocs: {
    opening_headroom_inferred: crocsUsable - crocsFloor,
    opening_reported: crocsOpening,
    opening_usable_inferred: crocsUsable,
    published_terminal_headroom: crocsTerminal - crocsFloor,
    published_terminal_reconstructed: crocsTerminal,
    max_cash_before_2029_term_maturity: crocsPreTermMax,
    max_cash_after_2029_term_maturity: crocsPostTermMax,
    max_headroom_after_2029_term_maturity: crocsPostTermMax - crocsFloor,
    max_cash_after_2029_notes: crocsPostNotesMax,
    max_headroom_after_2029_notes: crocsPostNotesMax - crocsFloor
  },
  nintendo: {
    outstanding_shares: shares,
    forecast_dividend: nintendoDividend,
    opening_usable_inferred: nintendoUsable,
    opening_headroom_inferred: nintendoUsable - nintendoFloor,
    published_terminal_reconstructed: nintendoPublishedTerminal,
    published_terminal_headroom: nintendoPublishedTerminal - nintendoFloor,
    candidate_year1_closing: nintendoCandidateY1,
    candidate_year1_headroom: nintendoCandidateY1 - nintendoFloor,
    candidate_year2_closing: nintendoCandidateY2,
    candidate_year2_headroom: nintendoCandidateY2 - nintendoFloor,
    cash_only_terminal: nintendoCashOnlyTerminal,
    cash_only_headroom: nintendoCashOnlyTerminal - nintendoFloor
  }
}, null, 2));
```

The exact numeric comparator was:

```python
#!/usr/bin/env python3
import json
import math
import sys

if len(sys.argv) != 3:
    raise SystemExit("usage: compare_liquidity.py decimal.json node.json")
with open(sys.argv[1], encoding="ascii") as handle:
    left = json.load(handle)
with open(sys.argv[2], encoding="ascii") as handle:
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


def compare(a, b, path="root"):
    global checked
    if isinstance(a, dict) and isinstance(b, dict):
        for key in sorted(set(a) | set(b)):
            if key not in a or key not in b:
                failures.append(f"{path}.{key}: missing")
            else:
                compare(a[key], b[key], f"{path}.{key}")
        return
    x = numeric(a)
    y = numeric(b)
    if x is not None and y is not None:
        checked += 1
        if not math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-9):
            failures.append(f"{path}: {x} != {y}")
        return
    if a != b:
        failures.append(f"{path}: {a!r} != {b!r}")


compare(left, right)
print(f"CHECKED_NUMERIC_FIELDS={checked}")
print(f"FAILURES={len(failures)}")
for failure in failures:
    print(failure)
raise SystemExit(1 if failures else 0)
```

The complete executed package compared 22 numeric fields at relative tolerance
1e-12 and absolute tolerance 1e-9 and returned:

```text
CHECKED_NUMERIC_FIELDS=22
FAILURES=0
```

Material Decimal outputs were:

```text
CROX opening usable / headroom       153.248400 / 53.248400
CROX terminal / headroom             169.248400 / 69.248400
CROX pre-term maximum                294.248400
CROX post-term / post-notes         -205.751600 / -555.751600
Nintendo forecast dividend           186.758235792
Nintendo published terminal         1173.433964208
Nintendo candidate year 1 / year 2  1332.658964208 / 1180.958964208
Nintendo cash-only terminal           799.522764208
```

SHA-256 values of the executed scratch records were:

```text
predeclaration.txt    4c7109e25cdb0960d7d558a246e4d1798bec172f531d6a3675afb28216dbf9a0
liquidity_bridge.py   f4ca192e4455645445e4d8dadeafc1e06903f489b04633781eb9f744d7853868
liquidity_bridge.js   ba1956ef573bfcd07eea82f25df0daa3c3f107b6fb9be1e9181c8e21eeb6ea5a
python-output.json    7834c9e25bb325c0cfd6f8054278097a0228092c3e41a7c4b3a53ab4a116b597
node-output.json      7781327912060c8f241bfdd0bee9b9794df8f16945a72ece2b997827eb924d22
compare_liquidity.py  8830fee95411ce6f7e86dca24bd92ebb770237c08c8c9fd77b7496c7b3f9f1aa
comparison.txt        1ae53c2ef4a22c73e7be31d92ae62ffc610414d87a090d13f2ca51bbbb72ffe9
```

The hashes are identification evidence, not substitutes for the embedded
formulas, raw values, reader reasons, or source documents.

## Alternatives and Implications

| Alternative | Evidence-supported effect | Cost and disposition |
|:--|:--|:--|
| Do nothing | Preserves the concise reports. | Retains a Crocs `minimum` above a lower opening checkpoint, omits the first proven 2029 shortfall, and presents Nintendo's undated reconstruction as Strong. Not supported.[2][3][4][5] |
| Enforce the current contract and correct each report | Changes Crocs to Fragile under the no-refinancing stress and makes Nintendo's exact minimum Unknown while preserving contrary headroom. | Smallest supported response; it requires no framework or template amendment. Forge research grants no Investing Hub edit authority. |
| Retain a calculation record outside each report | Could preserve formulas, sources, dates, and sensitivities without enlarging the report. | Useful if separately authorized, but the template already allows retained workings and does not require a companion file.[2] |
| Add the compact bridge to every report | Makes timing, cash access, funding, uses, floor, and headroom easier to scan. | Adds rows but produced zero classification, confidence, thesis, verdict, or trigger change beyond the complete current contract. |
| Amend the framework or company template | Could make the required bridge harder to omit. | Duplicates explicit current requirements. This two-report retrospective test shows no unique semantic detection and no prospective author benefit. |

For a Buffett and Munger style decision, the decisive issue is not the elegance
of a table. Crocs' downside is permanent-loss exposure created by debt-funded
capital returns before concentrated maturities; Nintendo's balance sheet is
large, but cash abundance does not authorize an unsupported positive minimum.
The simplest rule is already present: use only accessible cash, show contractual
claims when they fall due, assume refinancing unavailable in stress, and refuse
positive confidence when the first trough is unknown.[2][6]

The evidence supports report-application correction, not a new mandatory bridge
rule. A future proposal would need changed evidence: a prospective sample in
which the full current contract passes an erroneous report but the candidate
uniquely catches a decision-relevant defect, or measured evidence that the
candidate lowers total review cost without new false confidence.

## Response to Feedback and Remaining Questions

No prior evaluation exists for this pipeline.

The root idea's material tasks are answered as follows:

- Both published terminal values reproduce only after a 10% access haircut and
  other assumptions that the reports do not disclose.
- Crocs' claimed USD69 million `minimum` is already contradicted by the inferred
  USD53 million opening headroom. More importantly, even crediting a full third
  year of post-capex cash early cannot fund the February 2029 term maturity;
  the first proven shortfall is no later than that date.
- Nintendo's JPY673.4 billion result reproduces, but it deducts the entire
  operating-lease commitment after starting from CFO and spreads gross project
  spending without a remaining-spend schedule. Removing the lease double count
  yields JPY681.0 billion at an annual checkpoint, not a verified dated minimum.
- The complete current contract independently detects every defect used by the
  candidate. The compact display changes zero supported decision fields beyond
  that baseline.
- The two cold readers disagree on the severity of incomplete timing, and the
  disagreement is preserved. The synthesis uses a timing-independent upper
  bound for Crocs and the current contract's strict positive-claim gate for
  Nintendo.
- The smallest supported response is report-only correction under the current
  framework. No proposal, company edit, framework amendment, or implementation
  is authorized by this research.

Remaining questions are the exact Crocs tax settlement and within-year cash
path, stressed Crocs covenant headroom, the legal accessibility of Nintendo's
cash and securities, Nintendo's remaining project-spend schedule, capex overlap,
and dividend timing. Those gaps limit exact trough dates. They do not create
incremental value for a new rule because the present rule already requires them
to be resolved or labeled unknown.

Confidence is medium. Confidence is high in the source amounts, debt dates,
reconstructed terminal arithmetic, lease treatment, and zero incremental
classification count because primary filings, rendered tables, two calculators,
and 22 matched fields agree.[2][4][5] Overall confidence remains medium because
the original working records are unavailable, the 10% haircuts and operating
floors are inferred, intra-period cash dates are missing, the readers share one
model family, and only two reports were tested. Confidence would rise after
source-dated working records reproduce the exact troughs and a prospective
full-contract-versus-candidate comparison is preserved. It would fall if a
retained source record establishes different usable-cash, tax, project, capex,
or lease treatment.

This report issues no ADVANCE verdict, proposal, company-report edit, framework
change, or learning edit. `LEARNINGS.md` remains unchanged as required.[8]

## Sources

1. `forge/ideas/company-liquidity-stress-bridge-r01.md` -- root question,
   two-report test, complete-contract comparator, alternatives, decision fields,
   and stop conditions. [high]
2. `investing-hub:frameworks/financial-health.md` -- usable cash, facilities,
   maturities, dated bridge, mandatory-use, no-double-count, no-refinancing,
   first-shortfall, confidence, and classification requirements. [high]
   - `investing-hub:governance/template-company.md` -- decisive Financial Health
     output, retained-working option, source traceability, thesis consistency,
     and report hard gate. [high]
3. `investing-hub:companies/CROX.md` -- published Crocs stress inputs, USD69
   million headroom, classification, confidence, thesis, and source trail.
   [high]
   - `investing-hub:companies/NTDOY.md` -- published Nintendo stress inputs,
     JPY673.4 billion headroom, classification, confidence, thesis, and source
     trail. [high]
   - `investing-hub:data/crox-financial.md` -- Crocs statement history and June
     2026 quarterly cash, debt, tax, lease, capex, and cash-flow values. [high]
4. Crocs, Inc. "Form 10-Q for the quarterly period ended June 30, 2026," July
   30, 2026, balance sheet, cash flows, Notes 5 and 8, and Financial Condition,
   Capital Resources, and Liquidity. Cash, foreign-cash access, operating cash,
   capex, leases, facilities, covenants, and maturities were checked.
   https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm
   [high]
   - Crocs, Inc. "Form 10-K for the fiscal year ended December 31, 2025,"
     February 12, 2026, liquidity, borrowings, leases, commitments, and Note 13
     Income Taxes. Tax-claim magnitude and timing uncertainty were checked.
     https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/crox-20251231.htm
     [high]
5. Nintendo Co., Ltd. "Annual Report 2026," 2026, pp. 22, 30, 57-64, 74-77,
   and 99. Project amounts and dates, dividends, cash, investments, operating
   leases, and absence of loans or bonds were checked in native text and
   300-DPI rendered tables.
   https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf [high]
   - Nintendo Co., Ltd. "Consolidated Financial Highlights for the Three Months
     Ended June 30, 2026," August 6, 2026, pp. 1, 4, and 7. Dividend forecast,
     exact shares, cash and deposits, securities, liabilities, and absence of a
     quarterly cash-flow statement were checked in native text and rendered
     tables. https://www.nintendo.co.jp/ir/pdf/2026/260806e.pdf [high]
   - Nintendo Co., Ltd. "Consolidated Financial Highlights for the Years Ended
     March 31, 2025 and 2026," May 8, 2026, pp. 1, 4, and 10. FY2027 dividend
     forecast, policy, annual operating cash, and financing cash flows were
     checked. https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf [high]
6. `agentic-brain:library/finance/integrated-financial-modeling.md` -- purpose,
   perimeter, time resolution, usable cash, explicit financing actions,
   scenarios, controls, and independent challenge. [medium]
   - `agentic-brain:library/finance/working-capital-management-cash-conversion-cycle.md`
     -- minimum-cash dates, facility constraints, annual-netting limits, linked
     operating and funding stresses, and persistence tests. [medium]
7. U.S. Securities and Exchange Commission. "Commission Guidance on
   Presentation of Liquidity and Capital Resources Disclosures in Management's
   Discussion and Analysis," Release Nos. 33-9144, 34-62934, and FR-83,
   effective September 28, 2010. Internal and external liquidity sources,
   restrictions, known commitments and uncertainties, contractual timing, and
   investor understanding of funding risk were checked.
   https://www.federalregister.gov/documents/full_text/xml/2010/09/28/2010-23744.xml
   [high]
8. `forge/protocol.md` -- selection, research independence, artifact, source,
   transaction, handoff, and read-only-learning rules. [high]
   - `governance/template-research.md` -- research body and pre-write gate.
     [high]
   - `LEARNINGS.md` -- full-contract comparator, evidence preservation,
     claimed-result, and bounded-tooling lessons read before research and kept
     unchanged. [high]
   - `STATUS.md` -- selected row and preserved human-review row at the starting
     snapshot. [high]
   - `logbook/progress.log` -- prior handoffs through ENT-032. [high]
   - `logbook/errors.log` -- prior error boundary through ENT-038 and the current
     validation-oracle and trailing-blank recovery at ENT-039. [high]
