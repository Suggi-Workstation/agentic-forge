---
name: auditable-sbc-buyback-bridge
id: 20260921T133154Z
tier: research
pipeline: 20260921T114301Z
author: Researcher
tags: [stock-based-compensation, share-repurchases, owner-earnings, filing-reconciliation]
links:
  - forge/ideas/auditable-sbc-buyback-bridge-r01.md
  - forge/research/auditable-sbc-buyback-bridge-r01.md
  - forge/evaluations/auditable-sbc-buyback-bridge-evaluation-r01.md
  - agentic-brain:library/value-investing/capital-allocation.md
  - agentic-brain:library/finance/dividend-policy-and-share-buybacks.md
  - https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm
  - https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm
  - https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm
confidence: medium
---
# Auditable SBC and Buyback Bridge Research, Revision 2

## Question and Method

This revision addresses the first evaluation's bounded request: preserve two
separate reader outputs and test whether the detailed filing bridge changes a
mechanical classification, the narrow owner-earnings counting proxy, or a
reconciliation/refusal result relative to the simpler rule.[4] It does not
broaden the issuer sample or repeat the original research question.[5][6]

Before the reader test, the provisional explanation was recorded in plain
terms. The simple rule counts recognized stock-based compensation (SBC) once,
reports the beginning-to-ending point-share change, and keeps repurchase cash
separate. A detailed bridge can add decision-relevant information only if it
changes that result or detects a reconciliation defect that requires refusal.
The principal gaps were whether two readers could preserve separate worksheets,
whether every listed share flow would reconcile, and whether any concrete
omission or error would be detected. Disconfirmation would be reader
disagreement, an unreconciled material flow, or no changed decision beyond an
audit trail. This was provisional reasoning, not evidence.

The frozen source package comprised the same three official annual filings used
in revision 1: Adobe fiscal 2025, Workday fiscal 2026, and Snowflake fiscal
2026.[1][2][3] Both readers received the same reported inputs, source sections,
rules, labels, and comparison criterion. This was a reproducibility test of a
fixed package, not an independent data-discovery exercise.

The frozen rules were:

1. The simple baseline uses beginning and ending point-in-time shares. A lower
   ending count is `net denominator reduction`; a flat or higher ending count
   despite repurchases is `dilution offset`.
2. The narrow counting proxy is `OCF - capex - recognized SBC`. It subtracts
   the SBC add-back once. It is not a complete owner-earnings estimate because
   the package does not separate maintenance from growth capex.
3. Repurchase cash, award-withholding cash, and employee-plan proceeds remain
   separate ledgers. Repurchase-dollar attribution to employee awards is
   `indeterminate` absent a matched filing schedule.
4. The detailed bridge reconciles every listed share flow. Adobe's tolerance is
   1.0 million shares because its endpoint and equity tables use whole-million
   precision. Workday and Snowflake use 0.001 million. A residual above the
   tolerance or a material unclassified flow requires `indeterminate` and
   refusal.
5. A lower share count is not labeled `net capital return`. Value creation also
   requires price relative to intrinsic value and comparison with alternative
   uses of cash, neither of which is in this package.[7][8]
6. The predeclared comparison called a different classification, different
   proxy, or a concrete reconciliation/refusal result unavailable to the simple
   rule incremental. If the bridge added only detail, readers had to identify
   the exact omission, error, or limitation rather than invent one.

Reader A and Reader B ran in separate contexts from the same frozen package.
Each output was returned and preserved before either output was exposed to the
other, consistent with the admitted preservation lesson.[9] The readers
inspected the exact SEC filing URLs and used calculation tools. Direct browser
access returned the SEC automated-tool notice, but both readers retrieved the
complete filing HTML from the exact official URLs. The filing passages reported
below were then checked in the retrieved text. This access path is a limitation,
not a substitute source.

## Evidence and Findings

### Reader A output, preserved separately

Reader A recorded the following worksheet before comparison.

| Issuer | Share arithmetic, millions | Residual reported by reader | Simple result | Detailed result | OCF - capex - SBC, USD millions | Award-dollar attribution |
|:--|:--|--:|:--|:--|--:|:--|
| Adobe FY2025 | 441.0 + 3.6 + 0.1 + 1.1 - about 1.8 - 30.8 = 413.2; rounded cross-check 441 + 3 - 31 = 413 | 0.2 absolute | `net denominator reduction` | `net denominator reduction` | 10,031 - 179 - 1,942 = 7,910 | `indeterminate` |
| Workday FY2026 | 266.352 + 7.869 - 2.700 + 0.382 - 12.772 = 259.131 | 0.000 | `net denominator reduction` | `net denominator reduction` | 2,939 - 162 - 1,626 = 1,151 | `indeterminate` |
| Snowflake FY2026 | 333.865 + 7.880 + 0.817 + 9.453 - 3.291 + 0.082 - 4.925 + 0.037 = 343.918 | 0.000 | `dilution offset` | `dilution offset` | 1,221.942 - 101.628 - 1,599.547 = -479.233 | `indeterminate` |

Reader A's source pins were:

- Adobe: Consolidated Balance Sheets and Statements of Stockholders' Equity
  for 441 million beginning and 413 million ending shares, 3 million net
  treasury shares reissued under compensation plans, 31 million repurchased,
  and USD 1,942 million of SBC; Note 12 for 3.6 million RSUs released, 0.1
  million performance shares released, and 1.1 million ESPP shares purchased;
  Note 14 for 30.8 million shares delivered for USD 11,281 million; and the
  cash-flow statement for OCF, capex, award-withholding cash, treasury proceeds,
  and repurchase cash.[1]
- Workday: the stockholders' equity statement for every share-flow term; the
  cash-flow statement for OCF, capex, SBC, repurchase cash, withholding cash,
  and plan proceeds; and Note 14 for the repurchase and employee-plan
  disclosures.[2]
- Snowflake: the stockholders' equity statement for the option, ESPP, RSU,
  withholding, acquisition, repurchase, and treasury-reissuance flows; the
  cash-flow statement for the separate cash ledgers; and Note 12 for recognized
  SBC and equity-plan disclosures.[3]

Reader A found no filing error. Adobe's approximately 1.8 million withheld
shares were inferred from 4.8 million gross award and ESPP issuances less the
rounded 3 million net treasury reissuance; they were not directly tabulated.
Workday's repurchase note reports USD 2,894 million excluding excise tax and
commissions, while the cash-flow statement reports USD 2,895 million. Reader A
found no share-flow omission in Workday or Snowflake. The unresolved items were
Adobe's rounded endpoints and inferred withholding, the absence of matched
award-to-repurchase schedules for all three issuers, and the absence of a
maintenance-capex split.

Under the predeclared rule, Reader A called the reconciliation passes narrowly
incremental because the endpoint-only rule cannot establish that the detailed
flows reconcile. Reader A did not claim a changed classification, changed
proxy, valuation conclusion, or repurchase-dollar attribution.

### Reader B output, preserved separately

Reader B recorded the following worksheet before comparison.

| Issuer | Share arithmetic, millions | Residual reported by reader | Simple result | Detailed result | OCF - capex - SBC, USD millions | Award-dollar attribution |
|:--|:--|--:|:--|:--|--:|:--|
| Adobe FY2025 | 441.0 + 3.6 + 0.1 + 1.1 - about 1.8 - 30.8 = 413.2; rounded cross-check 441 + 3 - 31 = 413 | -0.2, ending minus bridge | `net denominator reduction` | `net denominator reduction` | 10,031 - 179 - 1,942 = 7,910 | `indeterminate` |
| Workday FY2026 | 266.352 + 7.869 - 2.700 + 0.382 - 12.772 = 259.131 | 0.000 | `net denominator reduction` | `net denominator reduction` | 2,939 - 162 - 1,626 = 1,151 | `indeterminate` |
| Snowflake FY2026 | 333.865 + 7.880 + 0.817 + 9.453 - 3.291 + 0.082 - 4.925 + 0.037 = 343.918 | 0.000 | `dilution offset` | `dilution offset` | 1,221.942 - 101.628 - 1,599.547 = -479.233 | `indeterminate` |

Reader B's source pins were:

- Adobe: the balance sheet for 441 million and 413 million shares; the equity
  statement for the rounded 3 million net reissuance, 31 million repurchase,
  and USD 1,942 million SBC entries; the cash-flow statement for all separate
  cash terms; Note 12 for gross award and ESPP activity; and Note 14 for the
  30.8 million shares and USD 11,281 million repurchase total.[1]
- Workday: the equity statement for 266.352 million beginning shares, 7.869
  million employee-plan shares, 2.700 million withheld shares, 0.382 million
  other shares, 12.772 million repurchased shares, and 259.131 million ending
  shares; the cash-flow statement for the separate cash terms; and Note 14 for
  the repurchase basis and plan disclosures.[2]
- Snowflake: the balance sheet and equity statement for both endpoints and all
  listed share flows; the cash-flow statement for OCF, capex, SBC,
  award-withholding cash, employee-plan proceeds, and repurchase cash; and Note
  12 for equity-plan and repurchase disclosures.[3]

Reader B found no simple-rule arithmetic or classification error. The detailed
bridge exposed the flow composition omitted by an endpoint-only presentation,
but it did not show that any disclosed flow was absent from the completed
worksheet. Reader B identified Adobe's inferred withholding and whole-million
rounding, Workday's one-million-dollar repurchase basis difference, and
Snowflake's USD 0.066 million difference between the note's repurchase amount
excluding transaction costs and excise tax and the cash-flow amount. The
unresolved items were the same substantive items as Reader A: no matched
award-to-repurchase schedule, no maintenance-capex split, and lower precision
for Adobe.

Under the predeclared rule, Reader B also called the reconciliation passes
narrowly incremental. Reader B did not claim that the bridge changed a
classification or proxy, established value creation, or supported dollar
attribution.

### Comparison after preservation

The readers independently agreed on all six classifications, all three proxy
results, all three reconciliation outcomes, and the refusal to attribute
repurchase dollars. The only presentation difference was Adobe's residual:
Reader A reported its absolute magnitude, 0.2 million, while Reader B reported
ending shares minus bridge, -0.2 million. Recalculation using the latter
convention produced -0.2 million for Adobe and zero for Workday and Snowflake.
There was no substantive reader disagreement.

The filings support the reported arithmetic. Adobe reports 441 million and 413
million endpoint shares, 3 million net compensation-plan treasury reissuance,
31 million repurchased shares, the gross award and ESPP activity, and the
separate cash lines used above.[1] Workday's equity statement supplies every
share term and reconciles exactly.[2] Snowflake's equity statement supplies all
listed inflows and outflows and also reconciles exactly.[3] The three cash-flow
statements add recognized SBC back to net income when deriving OCF, so the
narrow proxy removes that add-back once and does not treat withholding or
repurchase cash as a second compensation expense.[1][2][3]

The reader test repairs the evaluation's preservation defect but produces a
negative usefulness result. Neither bridge changes the simple mechanical label
or the narrow proxy. No bridge triggers a refusal. No concrete analyst omission
or filing error is detected in the completed package. Adobe's inferred
withholding and rounding are real disclosure limitations, but they were already
visible in revision 1 and do not change its result.[4][5]

Both readers applied the predeclared comparison literally and called a verified
reconciliation pass narrowly incremental. Fresh synthesis does not extend that
label into a decision-change claim. A pass proves that the detailed worksheet
is internally consistent; it does not demonstrate that an investor's
classification, proxy, refusal, valuation, or attribution decision changes.
Under the evaluation's stronger requirement, incremental decision value remains
undemonstrated. The bridge supplies audit assurance and flow explanation, not a
new decision in these three cases.

The resulting evidence states are:

- Known: the three bridges reconcile within the frozen tolerances; two preserved
  readers reproduce the arithmetic and labels; recognized SBC can be removed
  from OCF once; and the detailed method changes no classification or proxy.
- Inferred: Adobe's approximately 1.8 million withheld shares and the meaning of
  small note-to-cash-flow basis differences.
- Unknown: any matched repurchase-dollar attribution, repurchase value relative
  to intrinsic value, normalized maintenance capex, and whether a different
  issuer would trigger a refusal.

The two readers used the same reported-input package and the same model family.
Separate contexts and preserved outputs demonstrate procedural replication, not
independent source generation or freedom from correlated error. The three
issuer filings are primary evidence for their own reported figures but are not
independent evidence of management intent.

## Alternatives and Implications

### Rich attribution bridge

A model that assigns specified repurchase dollars to employee awards remains
unsupported. None of the three filing packages contains a matched schedule of
award shares, repurchase dates, prices, and designated purpose.[1][2][3]
Management's stated desire to limit dilution is not an allocation rule. This
alternative must return `indeterminate`.

### Smaller filing-only rule

The smaller rule remains sufficient for the tested decisions:

1. Count recognized SBC once.
2. Report beginning and ending point shares and label only the mechanical
   denominator outcome.
3. Report gross repurchase cash separately.
4. Use disclosed award and other share flows as an optional audit trail.
5. Refuse award-dollar attribution absent direct disclosure.

This rule yields the same classifications and proxy values as the detailed
bridges. The detailed worksheet can verify a reconciliation, but these cases do
not show a caught error or a changed refusal decision. Simplicity therefore
favors the smaller rule unless a future package contains an actual mismatch.

### Doing nothing

Using only gross repurchase announcements would omit whether the denominator
fell and would misdescribe Snowflake's outcome. Doing nothing is weaker than the
smaller rule. It does not follow that the full bridge is justified: the evidence
supports the endpoint check and one-time SBC treatment, while the additional
flow bridge remains an optional audit procedure for these cases.[7][8]

For a Buffett/Munger value-investing process, denominator reduction is necessary
information but not a capital-allocation verdict. Repurchases create value for
continuing owners only when price is favorable relative to intrinsic value and
the use of cash is superior to available alternatives.[7][8] This package does
not test those premises.

## Response to Feedback and Remaining Questions

The evaluation's five material requests are answered as follows.[4]

1. The source package, rules, labels, simple baseline, detailed bridge, filing
   tolerances, and comparison criterion were frozen before either reader began.
2. Two separate reader outputs are preserved above without merging their
   residual conventions, rationale, source pins, arithmetic, and unresolved
   items. Comparison occurred only after both outputs returned.
3. The mechanical labels are now `net denominator reduction`, `dilution
   offset`, and `indeterminate`. No `net capital return` claim is made.
4. The detailed bridges change no classification or proxy and trigger no
   refusal. They verify internal consistency but detect no new concrete error.
   The predeclared criterion's treatment of any reconciliation pass as narrowly
   incremental is weaker than a demonstrated decision change; this report does
   not convert that audit assurance into unsupported usefulness.
5. The verified filing figures were reused and the sample was not broadened.
   The negative incremental-value result is reported rather than repaired by an
   invented defect.

The blocking question for evaluation is whether a reconciliation-only audit
procedure, with no demonstrated changed result or caught error, warrants any
formal proposal. No further research cycle should repeat this same package
without new evidence. A future test would be informative only if a filing
package contains a material reconciliation mismatch or a direct matched
award-and-repurchase disclosure.

Confidence is medium. Confidence is high in the arithmetic because both
preserved readers agree and the filing passages and recalculation support it.
Overall confidence is reduced by the purposive three-issuer sample, Adobe's
rounding and inferred withholding, the shared input package and model family,
and the absence of a case that triggers refusal. Confidence would rise if a
separately sourced reader reproduced the result or a real mismatch demonstrated
when the detailed bridge changes a decision. It would fall if a material
unclassified flow were found in any of the three filings.

## Sources

1. Adobe Inc. "Annual Report on Form 10-K," fiscal year ended November 28,
   2025, filed January 15, 2026; Consolidated Balance Sheets, Consolidated
   Statements of Stockholders' Equity and Cash Flows, and Notes 12 and 14.
   Endpoint shares, award activity, SBC, settlement cash, and repurchases were
   checked.
   https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm [high]
2. Workday, Inc. "Annual Report on Form 10-K," fiscal year ended January 31,
   2026, filed March 6, 2026; Consolidated Statements of Stockholders' Equity
   and Cash Flows and Note 14. Every share-flow term, SBC, settlement cash,
   plan proceeds, and repurchases were checked.
   https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm [high]
3. Snowflake Inc. "Annual Report on Form 10-K," fiscal year ended January 31,
   2026, filed March 20, 2026; Consolidated Balance Sheets, Consolidated
   Statements of Stockholders' Equity and Cash Flows, and Note 12. Every listed
   share flow, SBC, settlement cash, plan proceeds, and repurchases were checked.
   https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm [high]
4. `forge/evaluations/auditable-sbc-buyback-bridge-evaluation-r01.md` -- first
   evaluation, REVISE disposition, preservation defect, label correction, and
   bounded incremental-value test. [high]
5. `forge/research/auditable-sbc-buyback-bridge-r01.md` -- prior research
   revision and verified three-issuer filing figures addressed by this report.
   [high]
6. `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- root question,
   acceptance tests, smaller-rule alternative, and stop conditions. [high]
7. `agentic-brain:library/value-investing/capital-allocation.md` -- net share
   count, repurchase price versus intrinsic value, and alternative capital uses.
   [medium]
8. `agentic-brain:library/finance/dividend-policy-and-share-buybacks.md` --
   denominator mechanics, buyback authenticity, and the distinction between
   EPS arithmetic and value creation. [medium]
9. `LEARNINGS.md` -- requirement to preserve dated pre-comparison rules and
   separate reader outputs before claiming a reproducible test. [high]
