---
name: auditable-sbc-buyback-bridge
id: 20260921T121424Z
tier: research
pipeline: 20260921T114301Z
author: Researcher
tags: [stock-based-compensation, share-repurchases, owner-earnings, filing-reconciliation]
links:
  - forge/ideas/auditable-sbc-buyback-bridge-r01.md
confidence: medium
---
# Auditable SBC and Buyback Bridge Research

## Question and Method

This report tests the root idea's question: can a public-filings-only bridge,
applied independently by two readers to three U.S. issuers, separate
stock-based-compensation dilution from genuine share-repurchase capital return
while counting compensation cost only once in owner earnings?[6]

Before targeted filing review, the provisional explanation was frozen as
follows. Recognized stock-based compensation (SBC) is an economic compensation
cost. Point-in-time shares, not weighted-average diluted shares, measure the
realized denominator outcome. Repurchase cash is a financing and
capital-allocation flow, while award withholding and employee-plan proceeds are
award-settlement flows. The three ledgers must remain separate. Starting from
GAAP net income counts SBC once because the expense is already included;
starting from operating cash flow requires subtracting the SBC add-back once.
Neither award-withholding cash nor repurchase cash is then deducted again as
compensation. This is consistent with the Brain's treatment of SBC as a real
cost and net share count as the buyback-authenticity test.[4][5]

The frozen outcome classifications were:

- `net capital return`: ending point shares are lower after all disclosed flows;
- `dilution offset`: gross repurchases occurred, but ending point shares are
  flat or higher and the roll-forward reconciles; and
- `indeterminate`: the filing inputs do not reconcile within reported rounding
  or a material share flow remains unclassified.

The test used Adobe fiscal 2025, Workday fiscal 2026, and Snowflake fiscal 2026.
The sample was purposive, not representative: Adobe directly describes dilution
minimization as one repurchase objective; Workday reports material SBC and
repurchases; Snowflake stress-tests a case in which gross repurchases coexist
with a higher ending share count.[1][2][3] For each issuer, the same source
package and frozen rules were given to two readers in separate contexts. Both
readers independently reproduced the figures and classifications below with no
material disagreement. This checks procedural reproducibility, not source
independence or model independence: both readers used the same filings, and
separate contexts do not eliminate correlated error.

The filing checks used the consolidated statements of stockholders' equity and
cash flows, the equity-compensation notes, and the repurchase notes. Amounts are
in millions of shares or USD millions unless noted. The owner-earnings test is a
narrow counting proxy, `OCF - capex - recognized SBC`; it is not a complete
intrinsic-value estimate because it does not distinguish maintenance from
growth capex or normalize working capital.

## Evidence and Findings

### Share roll-forwards

| Issuer | Filing-pinned point-share bridge | Reconciliation | Net outcome | Classification |
|:--|:--|:--|:--|:--|
| Adobe FY2025 | About 441.0 beginning + 4.8 gross award/ESPP releases - about 1.8 implied withholding - 30.8 repurchased = 413.2 expected. | The filing reports about 413 ending shares. The 0.2 difference is within whole-million share-table rounding. The equity statement independently shows 3 million net treasury shares reissued under compensation plans and 31 million repurchased. | About -28.0, or -6.3%. | `net capital return` |
| Workday FY2026 | 266.352 beginning + 7.869 employee-plan issuance - 2.700 withheld + 0.382 other issuance - 12.772 repurchased = 259.131 ending. | Exact to the filing's thousand-share units; residual 0. | -7.221, or -2.71%. | `net capital return` |
| Snowflake FY2026 | 333.865 beginning + 18.150 option, ESPP, and RSU issuance/vesting - 3.291 withheld + 0.082 acquisition issuance - 4.925 repurchased + 0.037 treasury reissuance on award settlement = 343.918 ending. | Exact to the filing's thousand-share units; residual 0. | +10.053, or +3.01%. | `dilution offset` |

Adobe's gross award and employee-stock-purchase activity comprises 3.6 million
restricted stock units released, 0.1 million performance shares released, and
1.1 million employee stock purchase plan shares. The filing reports only the
rounded 3 million net treasury-share reissuance in its stockholders' equity
statement, so the approximately 1.8 million withheld-share figure is inferred,
not directly disclosed. Adobe states that its repurchase program is designed
both to return value and to minimize dilution, but that purpose statement does
not allocate any particular repurchase share or dollar to an award.[1]

Workday directly reports each share term in the roll-forward. Gross employee
plan issuance of 7.869 million less 2.700 million withheld shares produced 5.169
million of net employee-plan issuance. Other issuance added 0.382 million
shares. Repurchases of 12.772 million shares exceeded those additions and
reduced the ending denominator by 7.221 million shares.[2]

Snowflake directly reports 7.880 million option-exercise shares, 0.817 million
employee-stock-purchase shares, 9.453 million vested restricted-stock-unit
shares, 3.291 million withheld shares, 0.082 million acquisition-related shares,
4.925 million repurchased shares, and 0.037 million treasury shares reissued on
award settlement. The complete bridge reconciles, but the ending denominator
increased by 10.053 million shares. The gross buyback therefore offset only part
of the disclosed issuance; it did not produce net capital return under the
frozen rule.[3]

The two readers agreed on all three classifications and every directly reported
share input. They also independently identified the same Adobe rounding and
withholding limitation. This meets the idea's reader-agreement test without
claiming that reader agreement validates management intent or dollar
attribution.

### Separate SBC, award-settlement, and repurchase-cash ledgers

| Issuer | Recognized SBC | Repurchase cash | Withholding-tax cash | Employee-plan or treasury proceeds | OCF | Capex | OCF - capex - SBC |
|:--|--:|--:|--:|--:|--:|--:|--:|
| Adobe FY2025 | 1,942 | 11,281 | 475 | 348 | 10,031 | 179 | 7,910 |
| Workday FY2026 | 1,626 | 2,895 | 616 | 192 | 2,939 | 162 | 1,151 |
| Snowflake FY2026 | 1,599.547 | 873.537 | 672.867 | 172.253 | 1,221.942 | 101.628 | -479.233 |

Each cash-flow statement adds recognized SBC back to GAAP income in arriving at
operating cash flow. The last column removes that add-back once after capex. It
does not subtract withholding-tax cash again: net share settlement converts part
of an equity award into a tax remittance while reducing shares issued. It also
does not subtract repurchase cash as compensation because repurchases are a
financing use of capital.[1][2][3]

The cash-flow repurchase amount is used for the cash ledger. Workday's cash-flow
outflow is USD 2,895 million, while its repurchase table reports USD 2,894
million excluding excise tax and commissions. Snowflake's cash-flow outflow is
USD 873.537 million, while its repurchase table reports USD 873.471 million
excluding transaction costs and excise tax. These are defined-basis differences,
not reconciliation failures.[2][3]

Recognized SBC expense, not the stockholders' equity entry, is used for the
counting proxy. Workday reports USD 1,626 million of recognized expense and a
USD 1,632 million additional-paid-in-capital entry; Snowflake reports USD
1,599.547 million of recognized expense and a USD 1,610.672 million equity
entry. Substituting the equity entry would change the expense convention rather
than improve the owner-earnings count.[2][3]

### Dollar attribution remains indeterminate

None of the three filings connects specified repurchase dollars to specified
award shares. The filings disclose annual share totals, cash totals, and some
award categories, but not a matched schedule of award issuance dates, withheld
shares, repurchase dates, and prices that would support a dollar allocation.
Adobe's explicit dilution-minimization purpose does not cure this gap.[1] The
share outcome is reproducible; the claim that a particular portion of repurchase
cash "paid for SBC" is not.

This is the decisive distinction:

- Known: recognized SBC expense, gross repurchase cash, award-settlement cash,
  employee-plan proceeds, disclosed share flows, and net point-share change.
- Inferred: whether gross repurchases produced a lower ending denominator.
- Unknown: which repurchase dollars, if any, should be assigned to particular
  employee awards or called genuine capital return.

The filings are independent issuer reports, but they are all management-prepared
corporate disclosures of the same general type. The audited financial statements
provide high-quality evidence for the reported totals; they do not provide
independent evidence of management intent or an allocation omitted from the
filings.[1][2][3]

## Alternatives and Implications

### Rich attribution bridge

A model could attempt to price award-related issuance and assign repurchase cash
to those shares. The evidence does not support that model. Annual totals do not
establish transaction-level matching, and management purpose statements do not
supply an allocation rule. Using average repurchase prices would add precision
without evidence. This alternative should return `indeterminate` for dollar
attribution.

### Smaller filing-only baseline

The smaller rule is:

1. Count recognized SBC once.
2. Report beginning and ending point shares and the net change.
3. Report gross repurchase cash separately.
4. Show disclosed award issuance, withholding, and other issuance only as an
   audit trail.
5. Refuse repurchase-dollar attribution unless a filing directly supplies it.

This baseline yields the same decision-relevant classifications as the detailed
bridges: Adobe and Workday delivered net denominator reduction, while Snowflake
did not.[1][2][3] The detailed bridge adds auditability and locates the share
flows responsible for the outcome, but it does not change the classification or
create a supportable dollar allocation.

### Doing nothing

Using only management's gross repurchase headline would classify all three as
capital return and would miss Snowflake's 3.01% increase in point shares.[3]
Using only recognized SBC would capture compensation expense but not whether
repurchases reduced continuing owners' denominator. Doing nothing is therefore
weaker than the simple baseline, but the evidence does not justify the richer
attribution model.

The bounded result supports a reproducible reconciliation and a refusal rule,
not an issuer-level allocation estimator. It does not establish that the three
cases represent all issuers, that every annual filing contains a complete share
roll-forward, or that a universal threshold should replace the sign of the net
point-share change.

## Response to Feedback and Remaining Questions

No prior evaluation exists. The first-report acceptance checks were answered as
follows:

- Three recent U.S. issuers were tested from their Form 10-K disclosures.[1][2][3]
- Every material share movement used in the classifications is source-pinned;
  Adobe's inferred withholding and rounding residual are explicit.
- Two readers using the same frozen rules independently reached identical final
  classifications.
- The expense and cash views remain non-additive, so SBC is counted once rather
  than combined with withholding or repurchase cash.
- The detailed bridge was compared with the simple baseline and did not change
  any decision-relevant classification.
- Specific repurchase-dollar attribution remains unresolved and blocking for
  any richer estimator.

Evaluation should determine whether auditability alone warrants a formal
filing-only checklist or whether the smaller baseline is already sufficient.
A proposal must not claim that the tested filings identify repurchase dollars
used to offset awards. Additional issuers could test coverage, but more cases
would not cure the missing transaction-level allocation unless their filings
contain materially different disclosure.

Confidence is medium. Confidence is high in the three filing-level arithmetic
because all roll-forwards reconcile within reported rounding and two readers
agreed. Confidence is lower in generalization because the sample is purposive,
the readers share a model family and source package, Adobe withholding is partly
inferred, and no case supports dollar-level attribution. Confidence would rise
if a broader filing sample preserved the same reproducibility or if an issuer
published a matched award-and-repurchase schedule. It would fall if an
independent reader found an unclassified material share flow or if the frozen
rules produced unstable classifications across periods.

## Sources

1. Adobe Inc. "Annual Report on Form 10-K," fiscal year ended November 28,
   2025, filed January 15, 2026; Consolidated Statements of Stockholders'
   Equity and Cash Flows, Notes 12, 14, and 15.
   Share, SBC, award-settlement, repurchase, and purpose disclosures checked.
   https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm [high]
2. Workday, Inc. "Annual Report on Form 10-K," fiscal year ended January 31,
   2026, filed March 6, 2026; Consolidated Statements of Stockholders' Equity
   and Cash Flows, Note 14.
   Share, SBC, award-settlement, and repurchase disclosures checked.
   https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm [high]
3. Snowflake Inc. "Annual Report on Form 10-K," fiscal year ended January 31,
   2026, filed March 20, 2026; Consolidated Statements of Stockholders' Equity
   and Cash Flows, Note 12.
   Share, SBC, award-settlement, acquisition-issuance, and repurchase disclosures checked.
   https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm [high]
4. `agentic-brain:library/value-investing/capital-allocation.md` --
   repurchases, SBC dilution, and net share count. [medium]
5. `agentic-brain:library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md` --
   SBC as an economic cost and recurring non-GAAP exclusions. [medium]
6. `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- root idea and acceptance
   plan for the three-issuer filing-only test. [high]
