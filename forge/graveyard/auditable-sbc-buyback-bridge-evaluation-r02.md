---
name: auditable-sbc-buyback-bridge-evaluation
id: 20260921T143617Z
tier: evaluation
pipeline: 20260921T114301Z
author: Analyst
tags: [stock-based-compensation, share-repurchases, owner-earnings, evaluation]
links:
  - forge/research/auditable-sbc-buyback-bridge-r02.md
  - forge/ideas/auditable-sbc-buyback-bridge-r01.md
  - forge/evaluations/auditable-sbc-buyback-bridge-evaluation-r01.md
  - agentic-brain:library/value-investing/capital-allocation.md
  - agentic-brain:library/finance/dividend-policy-and-share-buybacks.md
  - https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm
  - https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm
  - https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm
confidence: high
---
# Evaluation: Auditable SBC and Buyback Bridge, Revision 2

## Target and Baseline

Target: `forge/research/auditable-sbc-buyback-bridge-r02.md`, ID
`20260921T133154Z`.[1]

The target author is Researcher. This evaluation was performed by Analyst in a
separate scheduled context that did not inherit the drafting session's private
reasoning. Pipeline `20260921T114301Z` has one prior `REVISE` verdict and no
human budget extension.[2]

The following baseline was recorded before the target body was opened.

Expected evidence:

- the correction remains within the bounded three-issuer test and reuses the
  verified filing figures;
- dated rules, source package, comparison criterion, and two unmerged reader
  outputs establish their pre-comparison timing;
- both outputs preserve share and cash arithmetic, classifications, source pins,
  rationale, and unresolved items;
- the mechanical positive label is `net denominator reduction`, not `net
  capital return` absent valuation evidence;
- recognized SBC is counted once while repurchase and award-settlement cash stay
  separate and award-dollar attribution stays `indeterminate` absent direct
  disclosure; and
- the detailed bridge changes a classification, proxy, or refusal result, or
  identifies a concrete error unavailable to the simple endpoint rule.

Failure conditions were reconstructed or undated reader records, material
filing or arithmetic error, double counting, unsupported capital-return or
dollar-attribution claims, or no incremental decision value over the simple
rule. A negative result was acceptable and was not to be repaired by inventing
usefulness. These tests follow the root idea and first evaluation.[2][3]

## Findings

### Groundedness and primary-source checks

The material arithmetic is correct. Independent recalculation produced 413.2
million Adobe bridge shares and a signed ending-minus-bridge residual of -0.2
million, 259.131 million Workday ending shares with zero residual, and 343.918
million Snowflake ending shares with zero residual. The narrow cash proxies also
recalculated to USD 7,910 million, USD 1,151 million, and negative USD 479.233
million, respectively.[1]

The official filings support the checked inputs. Adobe reports 413 million and
441 million endpoint shares, USD 10,031 million of operating cash flow, and USD
11,281 million of repurchase cash.[4] Workday's equity statement reports 266.352
million beginning shares, 7.869 million employee-plan issuance, 2.700 million
withheld shares, 0.382 million other issuance, 12.772 million repurchased shares,
and 259.131 million ending shares.[5] Snowflake reports 333.865 million beginning
and 343.918 million ending shares, and its equity statement supplies the option,
ESPP, RSU, withholding, acquisition, repurchase, and treasury-reissuance terms
used by the target.[6]

The target correctly limits the cash measure to a narrow counting proxy rather
than complete owner earnings. It counts recognized SBC once, keeps repurchase
cash and award-settlement cash separate, and refuses matched award-dollar
attribution that the filings do not supply.[1] These points pass and do not
block the disposition.

### Reader preservation and independence

The revised report presents two unmerged worksheet sections and preserves one
real presentation difference: Reader A reports Adobe's residual as an absolute
0.2 million while Reader B reports the signed -0.2 million. The worksheets also
retain separate source-pin wording and unresolved-item lists.[1] This is a
material improvement over revision 1.

The timing and independence claim remains unauditable. The target says the rules
were frozen and each output returned before comparison, but it links no dated
pre-comparison rule record or separately committed reader output. Commit
`9214e7b4a65754b5a3bb3749f73a8578ba0d1eda` added only the consolidated research
report and its transaction files. A completed report's retrospective assertion
cannot establish when its embedded sections existed or when either reader saw
the other output. The existing method lesson requires linked pre-comparison
rules and unmerged per-reader outputs for that claim.[1][9]

The report appropriately states that both readers used one source package and
one model family. Agreement therefore supports arithmetic replication, not
independent source generation or freedom from correlated error.[1] The
remaining preservation gap blocks a claim of audited procedural
reproducibility, but it is not the decisive reason for closure.

### Incremental value and alternatives

The decisive result is negative. Under the target's own predeclared comparison,
the detailed bridges change no issuer classification, no cash proxy, and no
refusal result. They detect no omitted material flow or filing error. The Adobe
rounding and inferred withholding limitation was already known in revision 1.
The full bridge therefore supplies an audit trail, not a changed investment or
attribution decision, in the tested package.[1][2]

This result meets the root idea's explicit stop condition: the idea is not worth
pursuing if the bridge supplies no decision-relevant information beyond the
simpler expense-plus-net-share-count rule.[3] The Brain already supports the
smaller rule's elements: treat SBC as an economic cost, reconcile gross
repurchases with net share change, and separate denominator reduction from value
creation, which requires price relative to intrinsic value and comparison with
alternative capital uses.[7][8]

The three filings are high-quality primary evidence for reported totals, but the
sample is purposive and the filings are management-prepared. The evidence does
not establish that every future filing bridge will reconcile or that no issuer
will publish a matched award-and-repurchase schedule. Those unknowns do not
justify a proposal now. The current record shows neither a non-duplicative
system change nor evidence for the richer attribution method.[1][7][8]

Confidence in the disposition is high. The filing inputs and arithmetic pass,
the target reports the negative comparison directly, and that result triggers
the root idea's stated stop condition. Confidence would change if new evidence
showed a material mismatch that altered a classification or refusal decision,
or a direct matched schedule supported attribution without inference.

## Verdict and Handoff

**Verdict: REJECT.**

**Closure: remove pipeline `20260921T114301Z` from `STATUS.md`; there is no next
stage.**

One of two available corrective cycles was used by the prior `REVISE`; this
terminal verdict requests no further correction and relies on no human budget
extension.[2]

The rich filing bridge is not justified as a proposal. It reproduces the simple
mechanical result, catches no concrete error, and cannot establish genuine
capital return or award-dollar attribution. A reframe into the smaller rule
would restate guidance already present in the Brain rather than supply a
non-duplicative improvement.[1][3][7][8]

Reopening requires a human-directed handoff, an explicit budget, and changed
evidence: either a filing package with a material reconciliation mismatch that
changes a classification or refusal decision, or a direct matched schedule that
supports award-and-repurchase attribution. Any renewed reproducibility claim
must also link dated pre-comparison rules and separately preserved reader
outputs.[9]

## Learning Decision

`LEARNINGS.md` stays unchanged. The existing evidence-preservation lesson
already states the applicable rule. This evaluation adds no independent
pipeline and therefore does not satisfy the admission gate for a new or
strengthened reusable lesson.[9]

## Sources

1. `forge/research/auditable-sbc-buyback-bridge-r02.md` -- exact research target,
   embedded reader worksheets, filing checks, negative incremental-value result,
   and remaining limitations; checked at commit
   `9214e7b4a65754b5a3bb3749f73a8578ba0d1eda`. [high]
2. `forge/evaluations/auditable-sbc-buyback-bridge-evaluation-r01.md` -- prior
   `REVISE` verdict, first corrective-cycle count, preservation defect, label
   correction, and bounded usefulness test. [high]
3. `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- root question, acceptance
   conditions, simple alternative, and explicit stop condition. [high]
4. Adobe Inc. "Annual Report on Form 10-K," fiscal year ended November 28,
   2025, filed January 15, 2026; Consolidated Balance Sheets and Statements of
   Stockholders' Equity and Cash Flows, Notes 12 and 14. Endpoint shares, SBC,
   award activity, settlement cash, and repurchases were checked.
   https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm [high]
5. Workday, Inc. "Annual Report on Form 10-K," fiscal year ended January 31,
   2026, filed March 6, 2026; Consolidated Statements of Stockholders' Equity
   and Cash Flows and Note 14. Share-flow terms, SBC, settlement cash, plan
   proceeds, and repurchases were checked.
   https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm [high]
6. Snowflake Inc. "Annual Report on Form 10-K," fiscal year ended January 31,
   2026, filed March 20, 2026; Consolidated Balance Sheets, Consolidated
   Statements of Stockholders' Equity and Cash Flows, and Note 12. Endpoint
   shares, listed share flows, SBC, settlement cash, plan proceeds, and
   repurchases were checked.
   https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm [high]
7. `agentic-brain:library/value-investing/capital-allocation.md` -- net share
   count, the SBC dilution treadmill, repurchase price versus intrinsic value,
   and comparison with alternative capital uses. [medium]
8. `agentic-brain:library/finance/dividend-policy-and-share-buybacks.md` --
   buyback authenticity, denominator mechanics, and the distinction between EPS
   arithmetic and value creation. [medium]
9. `LEARNINGS.md` -- dated pre-comparison rules and unmerged reader outputs
   required before treating procedural reproducibility as established. [high]
