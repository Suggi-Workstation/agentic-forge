---
name: valuation-consistent-retained-earnings-test
id: 20260930T223526Z
tier: idea
pipeline: 20260930T223526Z
author: Analyst
tags: [value-investing, capital-allocation, management, retained-earnings]
links:
  - ANCHOR.md
  - forge/protocol.md
  - LEARNINGS.md
  - forge/ideas/forge-history-duplicate-receipt-r01.md
  - forge/research/forge-history-duplicate-receipt-r01.md
  - investing-hub:frameworks/simple-management.md
  - investing-hub:governance/template-company.md
  - investing-hub:companies/NTDOY.md
  - investing-hub:companies/CROX.md
  - agentic-brain:library/value-investing/capital-allocation.md
  - agentic-brain:library/value-investing/management-quality-evaluation.md
  - https://www.berkshirehathaway.com/letters/1983.html
confidence: low
---
# Valuation-Consistent Retained-Earnings Test

## Question and Value

Can the retained-earnings test in `investing-hub:frameworks/simple-management.md`
be made valuation-consistent, so a market-value gain remains a rough cross-check
rather than a supported pass when the same company report concludes that market
price materially exceeds intrinsic value? The bounded question is whether a
small clarification changes the capital-allocation judgment in the two current
Investing Hub company reports without requiring false precision or a new scoring
system.[1][2]

The existing target requires a five-year-or-longer one-dollar test, comparison
with alternative returns, and incremental after-tax operating-return evidence
where meaningful. It does not say how to classify a result when market value and
the report's own intrinsic-value evidence conflict.[2] The current Nintendo
report exposes that case: it says the test passes only on a roughly 2.2-yen
market-value gain per yen retained, immediately qualifies that market value as
above intrinsic value, and elsewhere estimates the quoted price at 116% above
Base value. It nevertheless assigns capital allocation 3/5.[3]

Value investors and company-research agents benefit if a management rating does
not treat market enthusiasm as proof that retained capital created owner value.
This is direct ANCHOR Path B work on repeatable management, capital-allocation,
and intrinsic-value analysis. The named target is the retained-earnings rule in
`frameworks/simple-management.md`; `governance/template-company.md` would need a
change only if research shows that the report output cannot express the result
clearly under its current Management section.[1][2]

The provisional hypothesis is that a frozen rule separating (a) market-value
change, (b) per-share operating or owner-cash outcomes, and (c) independently
supported intrinsic-value change will prevent an internally contradictory
`pass` while preserving `indeterminate` when historical intrinsic value cannot
be reconstructed. A credible alternative is that the current instruction to
compare incremental returns with alternatives already supplies the full
semantic rule, making Nintendo's wording an isolated report defect rather than
a framework gap. The idea is not worth pursuing if an explicit application of
the current rule already reaches the same supported judgment, if the proposed
clarification changes no score or decision, or if its apparent precision rests
on hindsight valuations that cannot be reproduced.[2][5][6]

## Origin and Prior Work

This is direct ideation under ANCHOR Path B, Value-Investing Systems. Discovery
preceded the provisional explanation. `LEARNINGS.md`, the current Forge board
and logs, every current idea, proposal, and graveyard artifact, the fresh Forge
hybrid index, and reachable historical Forge candidates were checked before the
question was fixed. At starting HEAD
`b42bd43e090b47a5cafee3be5fd726db2ff1fb04`, the only open board row was the
unrelated bounded-index-freshness discovery awaiting human review; no current
or historical retained-earnings-test proposal or human decision was found.[1][7]

The closest historical Path B work is not a duplicate. The SBC-buyback pipeline
asked whether a detailed filings bridge added decision value over the simpler
stock-compensation-expense plus net-share-count rule. It closed REJECT after the
bridge changed no classification, proxy, or refusal result. This candidate does
not attribute buyback dollars or reopen that pipeline; it tests a changed input:
a current company report now labels a market-value-only retained-earnings result
a pass while rejecting that market price as intrinsic evidence.[3][8]

The historical maintenance-capex pipeline is also distinct. It tested whether
public disclosures could support reproducible sustaining-capital ranges and was
reframed after the blind validation package proved unavailable. Its exact
question concerns the owner-earnings input, not whether a reported retention
result is consistent with a report's valuation. Its evidence reinforces the
need for an honest `indeterminate`, but its exhausted same-pipeline reframe does
not answer this question.[8]

Brain prior work states the governing distinction. The one-dollar market-value
test is a rough multiyear check, while allocation assessment should reconstruct
sources and uses, connect major uses to outcomes, evaluate incremental returns,
and judge long-term intrinsic value per share. Management quality should be
based on the multi-year cash-allocation record rather than charisma or one
market outcome.[5] Buffett's primary 1983 letter likewise places the objective
at intrinsic business value per share, but tests retained earnings by at least
one dollar of market value per dollar retained on a five-year rolling basis. It
therefore supports using market value as a test, not silently equating it with
intrinsic value.[6]

The Investing Hub has two current company reports. Nintendo is the only one that
states an explicit one-dollar result, and it records the market/intrinsic-value
conflict above.[3] Crocs instead grounds its 2/5 capital-allocation score in a
low-return acquisition, impairments, financing, and repurchase prices relative
to estimated value.[4] This comparison does not prove which treatment is right;
it supplies one contradiction and one decision-specific control for a small
research test.

The strongest alternative candidate was calibrating the overall management
score because both companies receive 3.0 despite different allocation records.
It lost because the framework deliberately averages five disclosed categories,
shows Nintendo and Crocs at 3 and 2 respectively for capital allocation, and
calls the overall mean a coarse descriptive index. Equal overall scores alone
do not establish a method failure. The retained-earnings conflict instead names
an exact rule, report passage, and falsifiable classification question.[2][3][4]

## Research Plan

Use one frozen, read-only retrospective unit. Do not edit Investing Hub, its
frameworks, or the published company reports during research.

1. Freeze the current management framework, company template, both company
   reports, their cited source records, and the Brain and Berkshire definitions.
   Preserve the exact current semantic reading as the baseline before designing
   a clarification.
2. Define the test before recalculation. For each company, identify the review
   interval, retained-capital denominator, dividends, repurchases, issuance,
   external financing, opening and closing share bases, market-value measure,
   per-share operating or owner-cash outcome, and any contemporaneously
   reconstructible intrinsic-value evidence. Keep reported fact, derived result,
   and interpretation separate.
3. Apply three separate labels rather than one blended pass: market-value
   cross-check, operating/incremental-return evidence, and intrinsic-value
   evidence. Permit `supported`, `unsupported`, and `indeterminate`; do not infer
   historical intrinsic value from the current share price or from a favorable
   market-capitalization change.
4. Have two separate readers apply the frozen baseline and candidate rule to
   Nintendo and Crocs. Preserve each reader's calculations, classifications,
   disagreements, and source pins before comparison. Do not count agreement from
   one shared arithmetic output as independent evidence.
5. Compare decision value. Record whether the candidate changes a capital-
   allocation score, confidence, override, report wording, or refusal result;
   whether it merely restates the existing semantic rule; and whether Crocs
   remains a valid control rather than being forced into an unavailable metric.
6. Compare doing nothing, a report-only correction, one sentence added to the
   framework, and a template output field. Reject any option that requires a new
   composite score, mandatory historical DCF, or unsupported endpoint value.

Research supports a proposal only if both readers reproduce the material
inputs, the candidate resolves Nintendo's market/intrinsic classification
without inventing a historical value, and it produces a decision-relevant
change or prevents a concrete misleading pass beyond an explicit application of
the current rule. It must fit as a concise, reversible framework clarification,
with a template change only if necessary. Stop without a proposal if the
baseline already forces the same result, if the only change is stylistic, if
Crocs cannot be assessed without false comparability, or if no reliable
retained-capital denominator can be reconciled.

Unknowns are material. The current corpus has only two company reports and one
explicit one-dollar application. Historical intrinsic value may be unavailable,
market capitalization can move for reasons unrelated to retained capital, and
buybacks or issuance can break a naive total-market-value comparison. A later
research result must narrow or preserve these limits rather than treat the
one-dollar test as a precise causal estimator.

Confidence is low. The target rule, primary Buffett wording, and one current
report establish a concrete semantic conflict, while the second report supplies
a bounded decision-specific comparison.[2][3][4][6] Confidence would rise if
separate readers reproduce the inputs and a concise rule changes a supported
classification beyond the current semantic baseline. It would fall if the issue
is only one report's phrasing, no decision changes, or endpoint intrinsic-value
estimates cannot be reconstructed without hindsight.

## Sources

1. `ANCHOR.md` -- Path B mission, practical-framework prompt, observed-problem,
   named-target, alternative, duplicate, and bounded-test selection rules. [high]
2. `investing-hub:frameworks/simple-management.md` -- current one-dollar test,
   incremental-return, sources-and-uses, scoring, override, and output rules.
   [high]
   - `investing-hub:governance/template-company.md` -- current Management output,
     framework-application, coverage, scorecard, and evidence gates. [high]
3. `investing-hub:companies/NTDOY.md` -- current explicit market-value-only
   one-dollar pass, intrinsic-value qualification, capital-allocation score, and
   valuation conclusion. [high]
4. `investing-hub:companies/CROX.md` -- current decision-specific allocation
   evidence, acquisition outcome, buyback valuation, score, and report basis.
   [high]
5. `agentic-brain:library/value-investing/capital-allocation.md` -- intrinsic
   value per share, five-year market-value test limits, incremental returns,
   sources-and-uses reconstruction, decision outcomes, and alternatives. [medium]
   - `agentic-brain:library/value-investing/management-quality-evaluation.md` --
     multi-year cash-allocation record and empirical management-quality tests.
     [medium]
6. Berkshire Hathaway Inc. "Chairman's Letter - 1983," retained-earnings test,
   five-year rolling horizon, intrinsic-business-value-per-share objective, and
   distinction between book input and discounted future cash output; accessed
   2026-09-30.
   https://www.berkshirehathaway.com/letters/1983.html [high]
7. `forge/research/forge-history-duplicate-receipt-r01.md` -- reachable current
   and historical Forge roots, exact disposition boundaries, and corpus limits.
   [high]
   - `forge/ideas/forge-history-duplicate-receipt-r01.md` -- duplicate-search
     question and historical-decision boundary. [high]
   - `forge/protocol.md` -- selection, duplicate, historical-source, artifact,
     and transaction rules. [high]
   - `STATUS.md` -- sole pending unrelated discovery at starting HEAD
     `b42bd43e090b47a5cafee3be5fd726db2ff1fb04`. [high]
   - `logbook/progress.log` -- current exact stage and disposition events through
     ENT-022 at the same starting HEAD. [high]
8. `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- historical distinct
   stock-compensation and repurchase-attribution question, verified at Git commit
   `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md` -- historical
     REJECT, negative incremental-value result, and reopening conditions,
     verified at the same commit. [high]
   - `forge/ideas/auditable-maintenance-capex-r01.md` -- historical distinct
     sustaining-capital estimation question, verified at Git commit
     `a88424a57f949a66996b6fb03d06c674087ec7c6`. [high]
   - `forge/evaluations/auditable-maintenance-capex-evaluation-r02.md` --
     historical REFRAME, unavailable blind validation, exhausted correction
     budget, and narrower-question boundary, verified at the same commit. [high]
