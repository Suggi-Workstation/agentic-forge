---
name: company-report-cold-conformance-review
id: 20261001T091855Z
tier: research
pipeline: 20261001T083505Z
author: Researcher
tags: [value-investing, company-research, verification, review]
links:
  - forge/ideas/company-report-cold-conformance-review-r01.md
  - forge/protocol.md
  - governance/template-research.md
  - governance/skills/forge-research/SKILL.md
  - governance/skills/forge-loop-feynman/SKILL.md
  - LEARNINGS.md
  - forge/research/valuation-consistent-retained-earnings-test-r01.md
  - forge/graveyard/valuation-consistent-retained-earnings-test-evaluation-r01.md
  - forge/research/nintendo-cycle-path-dcf-applicability-r01.md
  - forge/graveyard/nintendo-cycle-path-dcf-applicability-evaluation-r01.md
  - forge/research/company-liquidity-stress-bridge-r01.md
  - forge/graveyard/company-liquidity-stress-bridge-evaluation-r01.md
  - forge/graveyard/forge-proposal-claim-verification-map-evaluation-r02.md
  - investing-hub:governance/template-company.md
  - investing-hub:frameworks/simple-management.md
  - investing-hub:frameworks/simple-dcf.md
  - investing-hub:frameworks/financial-health.md
  - investing-hub:companies/NTDOY.md
  - investing-hub:companies/CROX.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md
  - agentic-brain:library/communication/source-verification-and-fact-checking.md
  - https://www.berkshirehathaway.com/letters/1983.html
  - https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf
  - https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm
  - https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a
confidence: medium
---
# Research: Company Report Cold Conformance Review

## Question and Method

This report tests the root idea's exact question: can a separate, answer-key-
blind reader applying the complete current company-report contract detect the
three material application defects already established in the two current
Investing Hub company reports, while accepting paired corrected controls and
adding no unsupported material blocker?[1]

Research began from clean Forge HEAD
`8bcfe7c177ad32105619bdad908d06bc404c0a25`. The board contained the valid
unselected discovery awaiting human review and this selected `research` row.
The root idea was authored by Analyst, so Researcher satisfies the separate-
author research gate. Progress ended at ENT-035 and errors at ENT-041.
`LEARNINGS.md` was read and remained unchanged.[1][2]

The Forge index returned literal `OK --` before hybrid retrieval. The Brain and
Investing Hub indexes independently returned literal `OK --`; their top relevant
files were read in full. The frozen source revisions were Investing Hub
`0d7995529758257669bf1726c6692fac85b25f9c` and Brain
`08f174a93f60f432f7303ad4b5fe61bb37d9435d`, both with clean worktrees.
Repository search found the current idea, the three closed domain pipelines,
and the prior rejected claim-map comparison; no prior cold company-release
review answered this question.[1][3][4][5]

Before the reader runs, the provisional explanation was: the current contracts
already state the needed analytical rules, but a separate cold reader may apply
those rules more reliably than the author context that released the reports.
The strongest contrary explanation was that the later defects were discoverable
only because the experiment inherited adjudicated cases and source
reconstructions; a same-family cold reader might otherwise miss them or reject
valid corrections. The decisive gaps were original-versus-corrected
classification, false HALTs, unsupported additions, reviewer burden, answer-key
separation, and the unavailable author-side pre-release baseline.

The parent froze three paired units from the complete affected report passages
and exact current contracts:

1. Nintendo retained-capital wording: original market-only pass versus a
   denominator-, endpoint-, and uncertainty-qualified correction.
2. Nintendo DCF applicability: original completed smooth Cash DCF versus Not
   applicable / Not calculable with the arithmetic retained only as a what-if.
3. Crocs and Nintendo liquidity: original positive minima and classifications
   versus the current-contract shortfall and uncertainty corrections.[3][4]

The source packet contained official issuer links and the exact calculations
needed to challenge each claim, but no Forge verdict, expected label, or
indication of which unit was original or defective. The parent knew the
adjudicated outcomes because it constructed the truth set; the readers did
not. Reader A saw original retained
capital, corrected DCF, original liquidity, corrected retained capital,
original DCF, and corrected liquidity. Reader B saw corrected liquidity,
original DCF, corrected retained capital, original liquidity, corrected DCF,
and original retained capital. Each reader applied the complete company
template and the three current frameworks, not an item-presence checklist.
Appendices A-E preserve the reviewer goals, contexts, schema, exact 1,617-word
packs, complete outputs, order, and elapsed time.

A preliminary dry run returned the same three-PASS/three-HALT separation in each
order but was excluded from all counts because its output was not written as a
standalone exact record. The official runs wrote their JSON before returning.
Official Reader A used only the pack and four contracts. Official Reader B's
tool trace additionally shows one read of the generic `write-evaluation` skill,
despite its own output saying the context was limited to the pack and
contracts. That skill contained no target artifact, expected label, defect
location, or answer key, so answer-key blindness remains intact, but Reader B
was not a strict target-only context. This deviation is a limitation, not hidden
independence.[2][5]

Official primary-source checks were independent of the readers. Berkshire's
1983 letter states the five-year rolling test of at least USD1 of market value
per USD1 retained. Crocs' June 2026 Form 10-Q states USD170.276 million of cash,
USD134.0 million drawn, USD865.4 million of remaining main-revolver capacity,
a November 2027 revolver maturity, and USD1.3 billion total borrowings. Nintendo's
2026 annual report confirms large cash balances, highly variable operating cash,
operating leases, and financial-asset distinctions. CFA Standard V(A) requires
diligence, independence, thoroughness, and a reasonable basis supported by
appropriate research, and specifically warns that model inputs may not capture
positive and negative cycles.[6][7][8][9]

Fixed `bc` arithmetic independently reproduced every material packet value:
2.627051 and 3.432825 for the aligned Nintendo market ratios; 2.170334 and
1.660899 for the mismatched report-date variants; Crocs terminal cash of
USD169.2484 million, opening headroom of USD53.2484 million, and post-maturity
cash of USD-205.7516 million and USD-555.7516 million; and Nintendo corrected
second-checkpoint headroom of JPY680.958964208 billion plus cash-only fallback
headroom of JPY299.522764208 billion.[3][4]

## Evidence and Findings

### Both readers separated every original from its corrected control

The official pair produced 12 classifications: all six original-unit readings
HALTed and all six corrected-control readings PASSed. Neither reader added an
unsupported finding to any corrected control. Each reader returned three PASS
and three HALT decisions despite the counterbalanced order (Appendices B-E).

| Claim unit | Reader A | Reader B | Exact bounded result |
|:--|:--|:--|:--|
| Original retained capital | A1 HALT | B6 HALT | Both rejected the market-only pass and current-price intrinsic-value claim. Neither forced a score change; each required reassessment only if the invalid claims were score-bearing. |
| Corrected retained capital | A4 PASS | B3 PASS | Both accepted the aligned 2.627/3.433 cross-checks, the endpoint-mismatched 2.170 qualification, no clean incremental-return or opening intrinsic-value record, and no overall pass. |
| Original DCF | A5 HALT | B2 HALT | Both rejected Assessed/completed Cash DCF and intrinsic-value/price conclusions because the positive path cannot represent the known negative year and uneven funding. |
| Corrected DCF | A2 PASS | B5 PASS | Both accepted Limited, Not applicable, Not calculable, N/A values and mechanical-what-if-only treatment. |
| Original liquidity | A3 HALT | B4 HALT | Both rejected Crocs' USD69 million minimum and Adequate/Watch labels and Nintendo's dated minimum and Strong/Watch labels. |
| Corrected liquidity | A6 PASS | B1 PASS | Both accepted Crocs Fragile with a shortfall no later than 2029-02-17 and Nintendo Unknown/Unclear with the corrected checkpoint and fallback evidence. |

The retained-capital result meets the bounded disclosure threshold rather than
manufacturing a score change. Both readers removed the invalid pass and price
claim, accepted the corrected cross-check and unknowns, and left the 3/5 score
conditional on its independent scorecard evidence. This matches the current
management rule: actual-share reconciliation, full acquisition/project outcomes,
incremental returns and alternatives matter; share-price performance alone does
not decide stewardship.[3]

The DCF result is decision-changing. Both readers caught that correct arithmetic
cannot rescue an unrepresentable method. The current rule explicitly routes
known negative years and uneven funding needs to a dated schedule or another
method and reserves intrinsic-value language for a supported Cash DCF. Both
accepted the correction without inventing a replacement value.[3][4]

The liquidity result is also decision-changing. Both readers caught Crocs'
lower opening checkpoint and the uncovered 2029 maturity under the stated no-
refinancing stress, changing Adequate/Watch to Fragile. Both caught Nintendo's
lease double count and absent dated minimum, changing Strong/Watch at Medium to
Unknown/Unclear at Low while retaining contrary fallback headroom. The current
financial-health contract already requires usable cash, dated funding,
maturities, no double counting, no assumed refinancing, and the first shortfall
or credible headroom.[3][4]

### The result measures capability, not causal improvement

The official reviewers took 94 and 82 seconds from first UTC timestamp to final
UTC timestamp. Each read 9,755 words of complete contract text plus a 1,617-word
pack, for 11,372 input words. Their exact JSON outputs were 1,010 and 1,193
words. Pack SHA-256 values were
`a1ccf25286d4078eaa24c69e2943700926a135c8c864b3ce36f5ddbea81100de`
and `48423cfd80a976c7b855b3d30a8903459c288d5a189b4701d62338e83f34552e`;
output SHA-256 values were
`9b8a2959245dedf42d33dbf97dd0bb9e893884c9f37698785a3dc6f35d9b2da1`
and `e87738e22dde753e7c2901780de7f83c079529170f0a5156b1c360a8d5170834`.
Hashes identify the embedded bytes; Appendices B-E preserve those bytes.

This establishes that a cold same-family reader can apply the existing contracts
to this frozen six-unit package with no observed miss or corrected-control false
HALT. It does not establish why the original reports passed release, because no
pre-release author-side checklist execution or prompt survives. It does not
compare the cold step with a controlled same-context self-review, measure a
future error rate, or show that a reviewer will reconstruct these sources
without a curated packet. Reader time is model wall-clock time, not human cost.

The test is retrospective and answer-key-selected. Corrected controls were built
from adjudicated outcomes; the parent therefore could make relevant evidence
available without giving the labels to readers. That is appropriate for a
capability test but easier than discovering an unknown defect population. Both
readers share the parent model family and contracts. Their agreement is
reproducibility evidence, not independent factual corroboration. Reader B's
extra generic skill read adds a small context asymmetry. The complete official
outputs also contain several unsupported-added-finding notes on original units,
such as report claims outside the packet; these did not create corrected-control
false HALTs but show that packet completeness affects review scope.

### Existing rules, not a new field or map, supplied the detection

Every decisive reader citation points to the existing company template and
management, DCF, or financial-health framework. No new domain predicate,
mandatory report field, claim inventory, executable checker, or large retained
map was needed. Prior Forge comparisons found that added retained-earnings
labels, a cycle method, and a compact liquidity bridge changed no supported
field beyond full current-rule enforcement; a complete claim map also added no
disclosed detection over a semantic checklist and created larger, divergent
records.[4]

Brain prior work supports the method but not the local effect size. A fresh
context is a different evidence class from self-review, a reviewer should
receive a focused evidence packet rather than reconstruct a raw trace, and
review evidence should attach to the exact artifact. Source-verification prior
work likewise requires precise claims, upstream evidence, reproduced
calculations, independent paths where available, and conclusions no stronger
than the record. These sources explain why the experiment was structured as a
cold, paired, full-contract review; they do not prove that one permanent gate
will reduce future company-report errors.[5]

## Alternatives and Implications

| Alternative | Checked evidence | Implication |
|:--|:--|:--|
| Do nothing | Three distinct current-report applications contain material unsupported release claims under rules already in force.[1][4] | Retains known process risk and no pre-release evidence record. |
| Author self-review under the present hard gate | No original pre-release execution record exists. | Simplest formal baseline, but its actual performance and burden are unknown; this experiment cannot assign causality. |
| One cold full-contract review | Both readers HALTed every original and PASSed every corrected control in 82-94 seconds with exact outputs preserved. | Supports evaluation of one reversible, bounded trial; it does not support an unmeasured permanent mandate. |
| Correct the reports after discovery | Prior domain work identifies the smallest substantive repair.[4] | Fixes known text if separately authorized, but does not test prevention and is outside this Forge stage. |
| Add a field, rule, bridge, or claim map | Prior fair comparisons found zero unique decision value, and this run needed none.[4] | Rejected for this purpose unless prospective evidence shows unique detection or lower total cost. |

The evidence supports handing a narrow trial question to evaluation: whether a
separate cold reviewer should be tested prospectively as one pre-release step
using the exact current contracts, with full original/corrected controls and no
new analytical rule. A trial should measure miss rate, false HALT rate,
unsupported expansion, author and reviewer time, revision count, and whether a
focus packet can be assembled without hindsight. It should stop if a reader
misses a decision-changing DCF or liquidity defect, rejects a valid corrected
control, or requires reconstruction comparable to the original research
projects.

The worst failure is false assurance: a nominal second reader rubber-stamps a
report or broadens the scope while the workflow labels it independently
reviewed. Prevention is to bind review to the exact revision, use the complete
semantic contracts, withhold prior verdicts and expected labels, mix valid and
invalid controls, preserve exact prompts and outputs, record unsupported added
findings, and keep human authorization separate from this process result.[3][5]

## Response to Feedback and Remaining Questions

No prior evaluation exists for this pipeline.

The root idea's material questions are answered as follows:

- Both official readers detected all three original defect classes, including
  the decision-changing DCF and liquidity defects.
- Both treated retained capital as a bounded disclosure/application correction;
  neither forced an invented score change.
- Both accepted all three corrected controls and added no unsupported finding to
  a corrected unit.
- The review used the full current contracts and no claim map, new field,
  executable checker, or answer key.
- Exact prompts, packs, order, outputs, hashes, and elapsed times are preserved.
- The historical author-side checklist execution remains unknown, so capability
  and burden are established only for the curated retrospective package.

Decision-relevant unknowns remain: prospective defect prevalence; performance
on unseen reports and different companies; controlled self-review versus cold-
review increment; human or different-model agreement; focus-packet preparation
cost; downstream revision and decision value; and whether a strict target-only
Reader B would reproduce its result without the generic skill context. A
prospective predeclared sample is required before claiming error-rate reduction
or adopting a permanent gate.

Confidence is medium. Confidence is high in the frozen 12-classification result
because exact pack and output bytes, counterbalanced order, line-cited contracts,
fixed arithmetic, and independent parent source checks agree. Overall confidence
remains medium because the corpus is two reports and three known retrospective
defects, both readers share one model family, the parent curated the evidence
from adjudicated cases, Reader B loaded extra generic guidance, no author-side
baseline survives, and future burden and outcome improvement are unmeasured.
Confidence would rise after a prospective, predeclared, target-only review
reproduces material detection without corrected-control false HALTs and shows
net review value. It would fall after a missed unseen blocker, a false HALT on a
valid report, material unsupported scope expansion, or burden comparable to the
underlying research.

This report issues no ADVANCE verdict, proposal, company-report edit, framework
change, implementation, approval, or learning edit. It returns the completed
evidence to independent evaluation. `LEARNINGS.md` remains unchanged.[2]

## Appendix A - Exact Official Reader Instructions

Reader A goal:

```text
Perform and durably preserve one answer-key-blind cold full-contract review of all six pack-A units, writing the complete exact structured result to the authorized scratch JSON path and returning the same object.
```

Reader A context:

```text
You are Official Cold Reader A in a bounded Investing Hub company-report conformance experiment. This is read-only except for one authorized scratch result file. Before any document read, run `date -u +'%Y-%m-%dT%H:%M:%SZ %s'` and retain both values. Then read the complete pack `/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001/reader-pack-a.md` (SHA-256 expected `a1ccf25286d4078eaa24c69e2943700926a135c8c864b3ce36f5ddbea81100de`) and the four exact contract files it names. Review all six units in pack order under the complete semantic contracts. Follow the pack boundary literally: do not read any file under `/srv/forge/agentic-forge`; do not search the web; do not inspect other Investing Hub files; do not seek or infer an answer key. A negative or uncertain finding may PASS. HALT only unsupported or misleading tested claims. Cite exact contract paths and line numbers. For every unit, identify the exact challenged claim(s), required correction, any unsupported added finding, and material decision effect. Do not omit a unit. At the end run `date -u +'%Y-%m-%dT%H:%M:%SZ %s'`, calculate elapsed seconds with a tool. Construct one complete JSON object matching the supplied output schema. Use write_file to save that exact JSON, with no Markdown fences or omitted fields, to `/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001/official-reader-a.json`; then return the same JSON object. The saved file is the sole authorized write. State same-model-family/context limits; do not call yourself factually independent.
```

Reader B goal:

```text
Perform and durably preserve one answer-key-blind cold full-contract review of all six pack-B units, writing the complete exact structured result to the authorized scratch JSON path and returning the same object.
```

Reader B context:

```text
You are Official Cold Reader B in a bounded Investing Hub company-report conformance experiment. This is read-only except for one authorized scratch result file. Before any document read, run `date -u +'%Y-%m-%dT%H:%M:%SZ %s'` and retain both values. Then read the complete pack `/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001/reader-pack-b.md` (SHA-256 expected `48423cfd80a976c7b855b3d30a8903459c288d5a189b4701d62338e83f34552e`) and the four exact contract files it names. Review all six units in pack order under the complete semantic contracts. Follow the pack boundary literally: do not read any file under `/srv/forge/agentic-forge`; do not search the web; do not inspect other Investing Hub files; do not seek or infer an answer key. A negative or uncertain finding may PASS. HALT only unsupported or misleading tested claims. Cite exact contract paths and line numbers. For every unit, identify the exact challenged claim(s), required correction, any unsupported added finding, and material decision effect. Do not omit a unit. At the end run `date -u +'%Y-%m-%dT%H:%M:%SZ %s'`, calculate elapsed seconds with a tool. Construct one complete JSON object matching the supplied output schema. Use write_file to save that exact JSON, with no Markdown fences or omitted fields, to `/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001/official-reader-b.json`; then return the same JSON object. The saved file is the sole authorized write. State same-model-family/context limits; do not call yourself factually independent.
```

Shared output schema:

```json
{
  "type": "object",
  "required": ["reader", "pack_sha256", "started_utc", "ended_utc", "elapsed_seconds", "order", "units", "counts", "limitations"],
  "properties": {
    "reader": {"type": "string"},
    "pack_sha256": {"type": "string"},
    "started_utc": {"type": "string"},
    "ended_utc": {"type": "string"},
    "elapsed_seconds": {"type": "integer"},
    "order": {"type": "array", "items": {"type": "string"}},
    "units": {
      "type": "array",
      "minItems": 6,
      "maxItems": 6,
      "items": {
        "type": "object",
        "required": ["unit", "decision", "challenged_claims", "contract_citations", "required_change", "unsupported_added_findings", "material_effect"],
        "properties": {
          "unit": {"type": "string"},
          "decision": {"type": "string", "enum": ["PASS", "HALT"]},
          "challenged_claims": {"type": "array", "items": {"type": "string"}},
          "contract_citations": {"type": "array", "items": {"type": "string"}},
          "required_change": {"type": "string"},
          "unsupported_added_findings": {"type": "array", "items": {"type": "string"}},
          "material_effect": {"type": "string"}
        }
      }
    },
    "counts": {
      "type": "object",
      "required": ["pass", "halt"],
      "properties": {"pass": {"type": "integer"}, "halt": {"type": "integer"}}
    },
    "limitations": {"type": "array", "items": {"type": "string"}}
  }
}
```

Official trace control: Reader A read the pack and four contracts. Reader B
read the same classes of file and additionally loaded the generic
`write-evaluation` skill before the pack. Neither official trace contains a
Forge artifact read, web search, other Investing Hub file, prior verdict,
expected label, or answer key.

## Appendix B - Exact Reader A Pack

SHA-256:
`a1ccf25286d4078eaa24c69e2943700926a135c8c864b3ce36f5ddbea81100de`.

```text
# Cold company-report conformance pack A

## Review boundary

Review the six units below in the order shown. Treat each unit as a proposed replacement for only the affected Management, Valuation, or Financial Health passage. Do not fail a unit because unrelated company-report sections are absent. Apply the complete semantic requirements in these frozen current contracts, not a word-presence checklist:

- /srv/investing/investing-hub/governance/template-company.md
- /srv/investing/investing-hub/frameworks/simple-management.md
- /srv/investing/investing-hub/frameworks/simple-dcf.md
- /srv/investing/investing-hub/frameworks/financial-health.md

You may read those four files. Do not read any Forge idea, research, evaluation, proposal, discovery, STATUS, log, or graveyard file. Do not seek a verdict or answer key. The source and calculation record below is the complete evidence packet for the tested claims. Treat repeated report wording and the source record as dependent where both originate from the same issuer document.

For each unit decide RELEASE PASS or HALT under the full current contracts. A negative or uncertain conclusion can pass. HALT only an unsupported claim, misleading completion label, missing required tested output, or contradiction with the supplied evidence. Name the exact challenged claim, governing contract path and line(s), requested correction, unsupported added finding if any, and material effect on score, classification, confidence, method, valuation status, thesis, or price conclusion.

## Shared source and calculation record

### Retained-capital record

Nintendo's affected report passage assigns Capital allocation 3/5 at Medium confidence. The issuer records support these aligned March 31, 2021 to March 31, 2026 values: opening split-adjusted price JPY6,181.9758; opening actual shares 1,191,227,670; opening market capitalization JPY7,364,140.628 million; closing price JPY8,773.7557; closing actual shares 1,152,828,705; closing market capitalization JPY10,114,637.422 million; market-capitalization gain JPY2,750,496.793 million; FY2022-FY2026 owner profit JPY2,103,923 million; dividends JPY1,056,933 million; gross treasury-share purchases JPY245,756 million; retention after dividends JPY1,046,990 million; and net retention after dividends and buybacks JPY801,234 million. The resulting market ratios are 2.627 and 3.433 respectively.

Using the report-date price JPY7,896 and post-July actual shares 1,152,873,116 produces a JPY1,738,945.496 million market-capitalization gain from the March 2021 opening point. That is 2.170 against net-of-buybacks retention and 1.661 against retention after dividends only. This September 2026 market endpoint does not match the March 2026 earnings-and-distribution endpoint. The current record supplies no clean Nintendo incremental-capital denominator and no contemporaneous March 2021 intrinsic-value estimate.

Primary sources: Nintendo Annual Report 2021, pp. 1 and 19-25, https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf ; Nintendo Annual Report 2022, key data and statement of changes in equity, https://www.nintendo.co.jp/ir/pdf/2022/annual2203e.pdf ; Nintendo 2023 highlights, https://www.nintendo.co.jp/ir/pdf/2023/230509e.pdf ; Nintendo 2024 highlights, https://www.nintendo.co.jp/ir/pdf/2024/240507e.pdf ; Nintendo Annual Report 2026, pp. 1-2, 23-30, and 59-62, https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf ; Nintendo restricted-stock notice, https://www.nintendo.co.jp/ir/pdf/2026/260724e.pdf .

### DCF record

Nintendo's report says cash earnings swing with the console cycle. Its selected FY2022-FY2026 annual core-cash amounts are JPY278.7, 283.7, 409.3, -49.1, and 226.1 billion, averaging JPY229.74 billion. The published smooth formula uses positive V0 and growth rates above -100 percent, so all ten annual modeled amounts are positive. The formula arithmetic reproduces Bear/Base/Bull values of approximately JPY2,268/3,656/5,250 per share and a JPY3,226 Base no-growth sensitivity. The arithmetic is not disputed.

Issuer annual-report tables also show operating profit and CFO of JPY-36.410/-40.390 billion in FY2013, JPY-46.425/-23.114 billion in FY2014, JPY29.362/19.101 billion in FY2017, JPY640.634/612.106 billion in FY2021, and JPY360.117/289.789 billion in FY2026. Net sales rose from JPY489.095 billion in FY2017 to JPY2,313.051 billion in FY2026. Nintendo says launch periods can shift receivables, payables, inventory, and operating cash; FY2025 and FY2026 inventory cash uses were JPY333.837 and JPY27.591 billion. The five-year core-cash record does not establish a comparable full cycle at unchanged scale, and no complete current-scale dated console-cycle cash schedule is supplied.

Primary sources: Nintendo Annual Report 2017, pp. 2 and 7, https://www.nintendo.co.jp/ir/pdf/2017/annual1703e.pdf ; Nintendo Annual Report 2021, pp. 2 and 12, https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf ; Nintendo Annual Report 2026, pp. 2, 8, 18, and 64, https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf .

### Liquidity record

Crocs reported cash of USD170.276 million at June 30, 2026; USD134 million drawn on a main revolver whose USD1.0 billion commitment expires in November 2027; USD0.6 million of letters of credit; USD500 million Term Loan B principal due February 17, 2029; and USD350 million notes due March 15, 2029. The affected report assumes USD200 million annual stressed CFO, USD75 million annual capex, no buybacks, USD134 million revolver repayment, USD100 million tax payment, and a USD100 million cash floor. Its terminal figure reproduces only with an unstated 10 percent opening-cash haircut: 170.276 x 90% + 2 x (200 - 75) - 134 - 100 = 169.248; terminal headroom is 69.248. Inferred opening usable cash is 153.248, or 53.248 above the floor. Even crediting a full third year of USD125 million post-capex cash before the term maturity yields 294.248 before, -205.752 after the USD500 million maturity, and -555.752 after the notes. Exact earlier intra-period trough and the tax date remain unknown.

Nintendo reported JPY1,544.090 billion of cash and deposits, JPY423.818 billion of current securities, no borrowings, a JPY230 billion facilities plan with projects completing in March 2028 or March 2029 but no remaining-spend schedule, JPY7.525 billion of future non-cancelable operating-lease payments, and an FY2027 forecast dividend of JPY162 on 1,152,828,616 shares. The affected report's JPY1,173.434 billion terminal and JPY673.434 billion headroom reproduce only with a 10 percent haircut, two years of stressed CFO of -150 and -50, JPY25 billion annual ordinary capex, JPY76.7 billion annual facilities spending, one JPY186.758 billion dividend, and a separate JPY7.525 billion lease deduction. Starting from CFO and removing that separate operating-lease deduction gives annual checkpoints of JPY1,332.659 billion and JPY1,180.959 billion, or JPY680.959 billion headroom at the second annual checkpoint. Cash-only fallback headroom is JPY299.523 billion. Securities access, the JPY500 billion floor, haircut, capex, project-payment timing, dividend timing, and exact dated minimum are unsupported or unresolved.

Primary sources: Crocs Form 10-Q for June 30, 2026, balance sheet, Note 8, and liquidity section, https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm ; Crocs 2025 Form 10-K, borrowings and tax notes, https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/crox-20251231.htm ; Nintendo Annual Report 2026, pp. 22, 74, and 98-99, https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf ; Nintendo June 2026 highlights, pp. 1, 4, and 7, https://www.nintendo.co.jp/ir/pdf/2026/260806e.pdf ; Nintendo FY2026 highlights, pp. 1, 4, and 10, https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf .

## Unit A1

### Management - Nintendo

Capital allocation is 3/5, Medium confidence. Formula dividends returned JPY1,302.6 billion of JPY1,376.5 billion CFO in FY2022-FY2026. Liquid assets earn interest rather than operating returns; a JPY230 billion facilities plan is unproven. The one-dollar test passes only on market value: market capitalization rose about JPY2.2 per yen retained since March 2021, derived from reported PER, EPS, and the current price. The current price is above estimated intrinsic value. Overall management remains Adequate at 3.0/5 with no override.

## Unit A2

### Valuation - Nintendo

Coverage is Limited. Simple DCF is Not applicable because the supplied annual core-cash record contains a negative year and launch-related uneven funding that a positive two-stage path cannot represent. No comparable full-cycle, current-scale dated cash schedule or supported alternative valuation is available. Bear/Base/Bull values, intrinsic value, and price discount or premium are N/A. The reproducible smooth outputs of JPY2,268/3,656/5,250 may be retained only as a separately labeled mechanical what-if; they do not support a completed Cash DCF, intrinsic-value claim, or current price conclusion. Valuation status is Not calculable pending a claim-matched method.

## Unit A3

### Financial Health - Crocs and Nintendo

Crocs: Two-year stress from June 2026 ends USD69 million above a USD100 million cash floor. Liquidity is Adequate, Medium confidence. Overall is Watch, Medium confidence, with debt-funded buybacks plus the tax liability as the vulnerability. The USD69 million is the stress minimum.

Nintendo: Two-year stress from June 2026 keeps at least JPY1,173.4 billion of usable cash. Liquidity is Strong, Medium confidence. Overall is Watch, Medium confidence, with JPY673.4 billion headroom above a JPY500 billion operating floor at the stress minimum. Cyclical cash, not solvency, is the weakness.

## Unit A4

### Management - Nintendo

Capital allocation is 3/5, Medium confidence. Formula dividends and accumulated liquid assets show conservative but not clearly owner-optimal deployment; the JPY230 billion facilities plan remains unproven. The aligned March 2021-March 2026 market cross-check is favorable at JPY2.627 of market-capitalization gain per yen retained after dividends, or JPY3.433 per yen retained net of repurchases. The report-date JPY2.170 version uses the net-of-repurchases denominator and mismatched March/September endpoints, so it is only a qualified cross-check. No clean incremental-return denominator or contemporaneous opening intrinsic-value estimate is available; no overall retained-earnings pass is claimed. Overall management remains Adequate at 3.0/5 with no override.

## Unit A5

### Valuation - Nintendo

Coverage is Assessed. Simple DCF at a fixed 10 percent is completed as a Cash DCF for operations, with associates at an earnings multiple. V0 is JPY229.7 billion, the FY2022-FY2026 average of CFO less cash capex less after-tax interest and dividends received. Bear/Base/Bull values are JPY2,268/3,656/5,250 per share. The range turns on V0: annual core cash was JPY278.7/283.7/409.3/-49.1/226.1 billion. All arithmetic and a second calculation reproduce. At a JPY7,896 price, the stock is 116 percent above Base estimated intrinsic value and 50 percent above Bull; valuation is completed.

## Unit A6

### Financial Health - Crocs and Nintendo

Crocs: The two-year terminal calculation reproduces USD69.248 million of headroom but not a minimum; opening inferred headroom is USD53.248 million. Under the stated no-refinancing stress, even all third-year post-capex cash credited before February 17, 2029 leaves USD-205.752 million after the term maturity and USD-555.752 million after the March notes. The first proven shortfall is no later than February 17, 2029; the exact earlier trough is unknown. Liquidity and Overall are Fragile, Medium confidence.

Nintendo: The published terminal calculation reproduces, but its operating-lease deduction is duplicated after starting from CFO and the dated minimum is not established. Removing the duplicate yields JPY680.959 billion at a second annual checkpoint, not a verified minimum. Cash-only fallback headroom of JPY299.523 billion is contrary evidence against Fragile, but access, project, capex, floor, dividend, and intra-period timing remain unresolved. Liquidity is Unknown, Low confidence; Overall is Unclear, Low confidence.
```

## Appendix C - Exact Reader B Pack

SHA-256:
`48423cfd80a976c7b855b3d30a8903459c288d5a189b4701d62338e83f34552e`.

```text
# Cold company-report conformance pack B

## Review boundary

Review the six units below in the order shown. Treat each unit as a proposed replacement for only the affected Management, Valuation, or Financial Health passage. Do not fail a unit because unrelated company-report sections are absent. Apply the complete semantic requirements in these frozen current contracts, not a word-presence checklist:

- /srv/investing/investing-hub/governance/template-company.md
- /srv/investing/investing-hub/frameworks/simple-management.md
- /srv/investing/investing-hub/frameworks/simple-dcf.md
- /srv/investing/investing-hub/frameworks/financial-health.md

You may read those four files. Do not read any Forge idea, research, evaluation, proposal, discovery, STATUS, log, or graveyard file. Do not seek a verdict or answer key. The source and calculation record below is the complete evidence packet for the tested claims. Treat repeated report wording and the source record as dependent where both originate from the same issuer document.

For each unit decide RELEASE PASS or HALT under the full current contracts. A negative or uncertain conclusion can pass. HALT only an unsupported claim, misleading completion label, missing required tested output, or contradiction with the supplied evidence. Name the exact challenged claim, governing contract path and line(s), requested correction, unsupported added finding if any, and material effect on score, classification, confidence, method, valuation status, thesis, or price conclusion.

## Shared source and calculation record

### Retained-capital record

Nintendo's affected report passage assigns Capital allocation 3/5 at Medium confidence. The issuer records support these aligned March 31, 2021 to March 31, 2026 values: opening split-adjusted price JPY6,181.9758; opening actual shares 1,191,227,670; opening market capitalization JPY7,364,140.628 million; closing price JPY8,773.7557; closing actual shares 1,152,828,705; closing market capitalization JPY10,114,637.422 million; market-capitalization gain JPY2,750,496.793 million; FY2022-FY2026 owner profit JPY2,103,923 million; dividends JPY1,056,933 million; gross treasury-share purchases JPY245,756 million; retention after dividends JPY1,046,990 million; and net retention after dividends and buybacks JPY801,234 million. The resulting market ratios are 2.627 and 3.433 respectively.

Using the report-date price JPY7,896 and post-July actual shares 1,152,873,116 produces a JPY1,738,945.496 million market-capitalization gain from the March 2021 opening point. That is 2.170 against net-of-buybacks retention and 1.661 against retention after dividends only. This September 2026 market endpoint does not match the March 2026 earnings-and-distribution endpoint. The current record supplies no clean Nintendo incremental-capital denominator and no contemporaneous March 2021 intrinsic-value estimate.

Primary sources: Nintendo Annual Report 2021, pp. 1 and 19-25, https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf ; Nintendo Annual Report 2022, key data and statement of changes in equity, https://www.nintendo.co.jp/ir/pdf/2022/annual2203e.pdf ; Nintendo 2023 highlights, https://www.nintendo.co.jp/ir/pdf/2023/230509e.pdf ; Nintendo 2024 highlights, https://www.nintendo.co.jp/ir/pdf/2024/240507e.pdf ; Nintendo Annual Report 2026, pp. 1-2, 23-30, and 59-62, https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf ; Nintendo restricted-stock notice, https://www.nintendo.co.jp/ir/pdf/2026/260724e.pdf .

### DCF record

Nintendo's report says cash earnings swing with the console cycle. Its selected FY2022-FY2026 annual core-cash amounts are JPY278.7, 283.7, 409.3, -49.1, and 226.1 billion, averaging JPY229.74 billion. The published smooth formula uses positive V0 and growth rates above -100 percent, so all ten annual modeled amounts are positive. The formula arithmetic reproduces Bear/Base/Bull values of approximately JPY2,268/3,656/5,250 per share and a JPY3,226 Base no-growth sensitivity. The arithmetic is not disputed.

Issuer annual-report tables also show operating profit and CFO of JPY-36.410/-40.390 billion in FY2013, JPY-46.425/-23.114 billion in FY2014, JPY29.362/19.101 billion in FY2017, JPY640.634/612.106 billion in FY2021, and JPY360.117/289.789 billion in FY2026. Net sales rose from JPY489.095 billion in FY2017 to JPY2,313.051 billion in FY2026. Nintendo says launch periods can shift receivables, payables, inventory, and operating cash; FY2025 and FY2026 inventory cash uses were JPY333.837 and JPY27.591 billion. The five-year core-cash record does not establish a comparable full cycle at unchanged scale, and no complete current-scale dated console-cycle cash schedule is supplied.

Primary sources: Nintendo Annual Report 2017, pp. 2 and 7, https://www.nintendo.co.jp/ir/pdf/2017/annual1703e.pdf ; Nintendo Annual Report 2021, pp. 2 and 12, https://www.nintendo.co.jp/ir/pdf/2021/annual2103e.pdf ; Nintendo Annual Report 2026, pp. 2, 8, 18, and 64, https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf .

### Liquidity record

Crocs reported cash of USD170.276 million at June 30, 2026; USD134 million drawn on a main revolver whose USD1.0 billion commitment expires in November 2027; USD0.6 million of letters of credit; USD500 million Term Loan B principal due February 17, 2029; and USD350 million notes due March 15, 2029. The affected report assumes USD200 million annual stressed CFO, USD75 million annual capex, no buybacks, USD134 million revolver repayment, USD100 million tax payment, and a USD100 million cash floor. Its terminal figure reproduces only with an unstated 10 percent opening-cash haircut: 170.276 x 90% + 2 x (200 - 75) - 134 - 100 = 169.248; terminal headroom is 69.248. Inferred opening usable cash is 153.248, or 53.248 above the floor. Even crediting a full third year of USD125 million post-capex cash before the term maturity yields 294.248 before, -205.752 after the USD500 million maturity, and -555.752 after the notes. Exact earlier intra-period trough and the tax date remain unknown.

Nintendo reported JPY1,544.090 billion of cash and deposits, JPY423.818 billion of current securities, no borrowings, a JPY230 billion facilities plan with projects completing in March 2028 or March 2029 but no remaining-spend schedule, JPY7.525 billion of future non-cancelable operating-lease payments, and an FY2027 forecast dividend of JPY162 on 1,152,828,616 shares. The affected report's JPY1,173.434 billion terminal and JPY673.434 billion headroom reproduce only with a 10 percent haircut, two years of stressed CFO of -150 and -50, JPY25 billion annual ordinary capex, JPY76.7 billion annual facilities spending, one JPY186.758 billion dividend, and a separate JPY7.525 billion lease deduction. Starting from CFO and removing that separate operating-lease deduction gives annual checkpoints of JPY1,332.659 billion and JPY1,180.959 billion, or JPY680.959 billion headroom at the second annual checkpoint. Cash-only fallback headroom is JPY299.523 billion. Securities access, the JPY500 billion floor, haircut, capex, project-payment timing, dividend timing, and exact dated minimum are unsupported or unresolved.

Primary sources: Crocs Form 10-Q for June 30, 2026, balance sheet, Note 8, and liquidity section, https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm ; Crocs 2025 Form 10-K, borrowings and tax notes, https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/crox-20251231.htm ; Nintendo Annual Report 2026, pp. 22, 74, and 98-99, https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf ; Nintendo June 2026 highlights, pp. 1, 4, and 7, https://www.nintendo.co.jp/ir/pdf/2026/260806e.pdf ; Nintendo FY2026 highlights, pp. 1, 4, and 10, https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf .

## Unit B1

### Financial Health - Crocs and Nintendo

Crocs: The two-year terminal calculation reproduces USD69.248 million of headroom but not a minimum; opening inferred headroom is USD53.248 million. Under the stated no-refinancing stress, even all third-year post-capex cash credited before February 17, 2029 leaves USD-205.752 million after the term maturity and USD-555.752 million after the March notes. The first proven shortfall is no later than February 17, 2029; the exact earlier trough is unknown. Liquidity and Overall are Fragile, Medium confidence.

Nintendo: The published terminal calculation reproduces, but its operating-lease deduction is duplicated after starting from CFO and the dated minimum is not established. Removing the duplicate yields JPY680.959 billion at a second annual checkpoint, not a verified minimum. Cash-only fallback headroom of JPY299.523 billion is contrary evidence against Fragile, but access, project, capex, floor, dividend, and intra-period timing remain unresolved. Liquidity is Unknown, Low confidence; Overall is Unclear, Low confidence.

## Unit B2

### Valuation - Nintendo

Coverage is Assessed. Simple DCF at a fixed 10 percent is completed as a Cash DCF for operations, with associates at an earnings multiple. V0 is JPY229.7 billion, the FY2022-FY2026 average of CFO less cash capex less after-tax interest and dividends received. Bear/Base/Bull values are JPY2,268/3,656/5,250 per share. The range turns on V0: annual core cash was JPY278.7/283.7/409.3/-49.1/226.1 billion. All arithmetic and a second calculation reproduce. At a JPY7,896 price, the stock is 116 percent above Base estimated intrinsic value and 50 percent above Bull; valuation is completed.

## Unit B3

### Management - Nintendo

Capital allocation is 3/5, Medium confidence. Formula dividends and accumulated liquid assets show conservative but not clearly owner-optimal deployment; the JPY230 billion facilities plan remains unproven. The aligned March 2021-March 2026 market cross-check is favorable at JPY2.627 of market-capitalization gain per yen retained after dividends, or JPY3.433 per yen retained net of repurchases. The report-date JPY2.170 version uses the net-of-repurchases denominator and mismatched March/September endpoints, so it is only a qualified cross-check. No clean incremental-return denominator or contemporaneous opening intrinsic-value estimate is available; no overall retained-earnings pass is claimed. Overall management remains Adequate at 3.0/5 with no override.

## Unit B4

### Financial Health - Crocs and Nintendo

Crocs: Two-year stress from June 2026 ends USD69 million above a USD100 million cash floor. Liquidity is Adequate, Medium confidence. Overall is Watch, Medium confidence, with debt-funded buybacks plus the tax liability as the vulnerability. The USD69 million is the stress minimum.

Nintendo: Two-year stress from June 2026 keeps at least JPY1,173.4 billion of usable cash. Liquidity is Strong, Medium confidence. Overall is Watch, Medium confidence, with JPY673.4 billion headroom above a JPY500 billion operating floor at the stress minimum. Cyclical cash, not solvency, is the weakness.

## Unit B5

### Valuation - Nintendo

Coverage is Limited. Simple DCF is Not applicable because the supplied annual core-cash record contains a negative year and launch-related uneven funding that a positive two-stage path cannot represent. No comparable full-cycle, current-scale dated cash schedule or supported alternative valuation is available. Bear/Base/Bull values, intrinsic value, and price discount or premium are N/A. The reproducible smooth outputs of JPY2,268/3,656/5,250 may be retained only as a separately labeled mechanical what-if; they do not support a completed Cash DCF, intrinsic-value claim, or current price conclusion. Valuation status is Not calculable pending a claim-matched method.

## Unit B6

### Management - Nintendo

Capital allocation is 3/5, Medium confidence. Formula dividends returned JPY1,302.6 billion of JPY1,376.5 billion CFO in FY2022-FY2026. Liquid assets earn interest rather than operating returns; a JPY230 billion facilities plan is unproven. The one-dollar test passes only on market value: market capitalization rose about JPY2.2 per yen retained since March 2021, derived from reported PER, EPS, and the current price. The current price is above estimated intrinsic value. Overall management remains Adequate at 3.0/5 with no override.
```

## Appendix D - Complete Official Reader A Output

SHA-256:
`9b8a2959245dedf42d33dbf97dd0bb9e893884c9f37698785a3dc6f35d9b2da1`.

```json
{
  "reader": "Official Cold Reader A",
  "pack_sha256": "a1ccf25286d4078eaa24c69e2943700926a135c8c864b3ce36f5ddbea81100de",
  "started_utc": "2026-10-01T09:11:55Z",
  "ended_utc": "2026-10-01T09:13:29Z",
  "elapsed_seconds": 94,
  "order": [
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6"
  ],
  "units": [
    {
      "unit": "A1",
      "decision": "HALT",
      "challenged_claims": [
        "The one-dollar test passes only on market value: market capitalization rose about JPY2.2 per yen retained since March 2021, derived from reported PER, EPS, and the current price.",
        "The current price is above estimated intrinsic value."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:155-190",
        "/srv/investing/investing-hub/governance/template-company.md:302-309",
        "/srv/investing/investing-hub/frameworks/simple-management.md:28-45",
        "/srv/investing/investing-hub/frameworks/simple-management.md:47-59",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:14-20",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:80-90"
      ],
      "required_change": "Withdraw the one-dollar-test pass and the current-price-versus-intrinsic-value conclusion. Use actual shares and aligned March 2021-March 2026 endpoints to report JPY2.627 of market-capitalization gain per yen retained after dividends and JPY3.433 per yen retained net of repurchases only as qualified market cross-checks; identify the report-date JPY2.170 net-retention version as endpoint-mismatched. State that no clean incremental-return denominator or contemporaneous opening intrinsic-value estimate is available. Reassess the Capital allocation score, its confidence, and any dependent overall conclusion only if the withdrawn claims were score-bearing; do not change the overall classification merely because this bounded passage cannot retest unrelated categories.",
      "unsupported_added_findings": [
        "The added finding that the current price is above estimated intrinsic value is unsupported: the supplied cash record cannot support the completed simple DCF, and no supported alternative valuation is supplied."
      ],
      "material_effect": "The retained-earnings pass and price conclusion are removed. The market ratios become non-scoring cross-checks rather than proof of incremental owner value; Capital allocation 3/5, Medium confidence, and Overall Adequate 3.0/5 require reconsideration only to the extent they relied on those claims."
    },
    {
      "unit": "A2",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:103-108",
        "/srv/investing/investing-hub/governance/template-company.md:265-310",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:12-20",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:71-80",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:82-90"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "Coverage remains Limited and valuation remains Not calculable. Bear, Base, Bull, intrinsic value, and price discount or premium remain N/A; the reproducible smooth outputs may appear only as a separately labeled mechanical what-if and cannot affect the valuation status, thesis, or current-price conclusion."
    },
    {
      "unit": "A3",
      "decision": "HALT",
      "challenged_claims": [
        "Crocs: The USD69 million two-year terminal headroom is the stress minimum, Liquidity is Adequate, and Overall is Watch.",
        "Nintendo: The stress keeps at least JPY1,173.4 billion of usable cash and JPY673.4 billion of headroom at the stress minimum, Liquidity is Strong, and Overall is Watch."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:235-263",
        "/srv/investing/investing-hub/frameworks/financial-health.md:43-52",
        "/srv/investing/investing-hub/frameworks/financial-health.md:54-64",
        "/srv/investing/investing-hub/frameworks/financial-health.md:76-84"
      ],
      "required_change": "For Crocs, label USD69.248 million as two-year terminal headroom, not the minimum; disclose inferred opening headroom of USD53.248 million and the no-refinancing shortfall no later than February 17, 2029, including USD-205.752 million after the term maturity and USD-555.752 million after the notes, with the exact earlier trough unknown. Rate Liquidity and Overall Fragile, Medium confidence. For Nintendo, remove the duplicated operating-lease deduction after CFO; report JPY680.959 billion as headroom at the second annual checkpoint, not a verified minimum, and retain JPY299.523 billion cash-only fallback headroom. Because securities access, the cash floor, haircut, capex, project-payment timing, dividend timing, and intra-period minimum remain unresolved, rate Liquidity Unknown, Low confidence, and Overall Unclear, Low confidence.",
      "unsupported_added_findings": [
        "The supplied record does not establish the claim that Crocs' buybacks were debt-funded.",
        "Nintendo's JPY500 billion operating floor is treated as established even though the supplied record identifies it as unsupported.",
        "The statement that cyclical cash, rather than solvency, is the weakness suppresses the decisive unresolved access, spending, floor, dividend, and timing assumptions."
      ],
      "material_effect": "Crocs changes from Adequate liquidity and Watch overall to Fragile for both because the stated no-refinancing stress establishes a maturity shortfall. Nintendo changes from Strong liquidity and Watch overall to Unknown liquidity and Unclear overall because no dated minimum is established; confidence falls from Medium to Low."
    },
    {
      "unit": "A4",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:155-190",
        "/srv/investing/investing-hub/frameworks/simple-management.md:28-45",
        "/srv/investing/investing-hub/frameworks/simple-management.md:47-59"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "Capital allocation remains 3/5 at Medium confidence and Overall remains Adequate at 3.0/5 within the bounded replacement. The JPY2.627, JPY3.433, and endpoint-mismatched JPY2.170 market ratios remain explicitly qualified cross-checks; they do not produce a retained-earnings pass, incremental-return finding, or intrinsic-value conclusion."
    },
    {
      "unit": "A5",
      "decision": "HALT",
      "challenged_claims": [
        "Coverage is Assessed.",
        "Simple DCF at a fixed 10 percent is completed as a Cash DCF for operations, with associates at an earnings multiple.",
        "Bear/Base/Bull values of JPY2,268/3,656/5,250 per share are completed intrinsic values supporting the conclusions that JPY7,896 is 116 percent above Base and 50 percent above Bull."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:265-310",
        "/srv/investing/investing-hub/governance/template-company.md:337-358",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:12-20",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:71-80",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:82-90"
      ],
      "required_change": "Change Coverage to Limited and Simple DCF to Not applicable because the known negative year and launch-related uneven funding require a dated cash-flow schedule or another claim-matched method. Change valuation status to Not calculable; show Bear, Base, Bull, intrinsic value, and price comparisons as N/A. The JPY2,268/3,656/5,250 outputs may be retained only as a separately labeled mechanical what-if, with the blocker that no comparable current-scale full-cycle cash schedule or supported alternative valuation is supplied.",
      "unsupported_added_findings": [],
      "material_effect": "The Cash DCF label, completed valuation, intrinsic-value language, and 116 percent/50 percent price-premium conclusions are withdrawn. Arithmetic reproducibility does not cure method inapplicability, so valuation and any dependent thesis or price conclusion become Not calculable/N/A."
    },
    {
      "unit": "A6",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:235-263",
        "/srv/investing/investing-hub/frameworks/financial-health.md:43-52",
        "/srv/investing/investing-hub/frameworks/financial-health.md:54-64",
        "/srv/investing/investing-hub/frameworks/financial-health.md:76-84"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "Crocs is correctly classified Liquidity Fragile and Overall Fragile, Medium confidence, with the first proven shortfall no later than February 17, 2029 and the exact earlier trough unknown. Nintendo is correctly classified Liquidity Unknown and Overall Unclear, Low confidence; the corrected second annual checkpoint and cash-only fallback are retained as contrary evidence without being mislabeled as a dated minimum."
    }
  ],
  "counts": {
    "pass": 3,
    "halt": 3
  },
  "limitations": [
    "This answer-key-blind review was limited to reader-pack-a.md and the four contract files named in it; no source URLs, other Investing Hub files, Forge files, logs, graveyards, or answer key were inspected.",
    "The reviewer is a same-model-family subagent operating in the supplied task context, not a factually independent reviewer; shared model priors and shared context can correlate judgments.",
    "The findings test only the six proposed replacement passages against the supplied evidence packet and frozen contracts; they do not assess the completeness or accuracy of unrelated company-report sections."
  ]
}
```

## Appendix E - Complete Official Reader B Output

SHA-256:
`e87738e22dde753e7c2901780de7f83c079529170f0a5156b1c360a8d5170834`.

```json
{
  "reader": "Official Cold Reader B",
  "pack_sha256": "48423cfd80a976c7b855b3d30a8903459c288d5a189b4701d62338e83f34552e",
  "started_utc": "2026-10-01T09:11:52Z",
  "ended_utc": "2026-10-01T09:13:14Z",
  "elapsed_seconds": 82,
  "order": [
    "B1",
    "B2",
    "B3",
    "B4",
    "B5",
    "B6"
  ],
  "units": [
    {
      "unit": "B1",
      "decision": "PASS",
      "challenged_claims": [
        "Crocs: the first proven no-refinancing shortfall is no later than February 17, 2029, the exact earlier trough is unknown, and Liquidity and Overall are Fragile at Medium confidence.",
        "Nintendo: the published terminal is not a verified minimum, the separate operating-lease deduction duplicates an amount already reflected in CFO, and the corrected checkpoint plus unresolved timing and access assumptions support Liquidity Unknown and Overall Unclear at Low confidence."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/frameworks/financial-health.md:50",
        "/srv/investing/investing-hub/frameworks/financial-health.md:54-64",
        "/srv/investing/investing-hub/frameworks/financial-health.md:76-80",
        "/srv/investing/investing-hub/governance/template-company.md:235-263"
      ],
      "required_change": "None. Preserve the distinction between a reproduced terminal checkpoint and a dated minimum, the Crocs first-shortfall bound, the Nintendo duplicate-lease correction, and all stated unresolved inputs.",
      "unsupported_added_findings": [],
      "material_effect": "The passage correctly prevents false positive liquidity conclusions: Crocs remains Fragile because the no-refinancing bridge proves an uncovered 2029 maturity, while Nintendo remains Unknown/Unclear rather than Strong because credible dated minimum headroom is not established."
    },
    {
      "unit": "B2",
      "decision": "HALT",
      "challenged_claims": [
        "Coverage is Assessed and the smooth fixed-10-percent model is a completed Cash DCF with Bear/Base/Bull intrinsic values of JPY2,268/3,656/5,250 per share.",
        "At JPY7,896 the shares are 116 percent above Base and 50 percent above Bull, so valuation is completed."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:14-20",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:71-80",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:82-90",
        "/srv/investing/investing-hub/governance/template-company.md:265-310",
        "/srv/investing/investing-hub/governance/template-company.md:337-358"
      ],
      "required_change": "Set Coverage to Limited; mark the smooth simple DCF Not applicable and the current valuation Not calculable; report Bear/Base/Bull values, intrinsic value, and price comparisons as N/A. The JPY2,268/3,656/5,250 outputs may remain only as a separately labeled mechanical what-if. Supply a claim-matched dated cash schedule or supported alternative method before completing valuation, and remove the associates multiple unless its source, ownership perimeter, and equity adjustment are supplied.",
      "unsupported_added_findings": [
        "The associates-at-an-earnings-multiple component is not supported or reconciled in the bounded source and calculation record."
      ],
      "material_effect": "This invalidates the Cash DCF type, Assessed/completed labels, intrinsic-value figures, and current-price overvaluation conclusion; reproduction of the formula arithmetic does not cure the unrepresentable cash path."
    },
    {
      "unit": "B3",
      "decision": "PASS",
      "challenged_claims": [
        "The aligned March 2021-March 2026 market-capitalization cross-check is JPY2.627 per yen retained after dividends and JPY3.433 per yen retained net of repurchases.",
        "The JPY2.170 report-date ratio is only a qualified cross-check because it combines a March 2021 opening point with a September 2026 market endpoint, and no one-dollar-test pass is claimed without a clean incremental-return denominator or contemporaneous opening intrinsic value."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/frameworks/simple-management.md:24-45",
        "/srv/investing/investing-hub/frameworks/simple-management.md:47-59",
        "/srv/investing/investing-hub/governance/template-company.md:155-190"
      ],
      "required_change": "None. Keep the market result labeled as a qualified cross-check and do not convert it into a retained-earnings or one-dollar-test pass without claim-matched incremental-return evidence.",
      "unsupported_added_findings": [],
      "material_effect": "No score or classification change is required. The ratios may inform the 3/5 capital-allocation assessment, but the explicit qualification prevents share-price performance alone from proving owner-optimal allocation."
    },
    {
      "unit": "B4",
      "decision": "HALT",
      "challenged_claims": [
        "Crocs: USD69 million is the stress minimum, Liquidity is Adequate, and Overall is Watch despite the no-refinancing 2029 maturities.",
        "Nintendo: the stress keeps at least JPY1,173.4 billion of usable cash at the minimum, with JPY673.4 billion of minimum headroom, so Liquidity is Strong and Overall is Watch at Medium confidence."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/frameworks/financial-health.md:50",
        "/srv/investing/investing-hub/frameworks/financial-health.md:54-64",
        "/srv/investing/investing-hub/frameworks/financial-health.md:76-80",
        "/srv/investing/investing-hub/governance/template-company.md:235-263"
      ],
      "required_change": "For Crocs, relabel USD69.248 million as terminal headroom, disclose opening inferred headroom of USD53.248 million and the unknown earlier trough, extend the no-refinancing bridge through the February and March 2029 maturities, and report the first proven shortfall no later than February 17, 2029 with Liquidity and Overall Fragile. For Nintendo, remove the duplicate operating-lease deduction, label JPY1,180.959 billion and JPY680.959 billion as a second annual checkpoint rather than a minimum, disclose JPY299.523 billion cash-only fallback headroom and the unresolved access/timing/assumption gaps, and use Liquidity Unknown and Overall Unclear at Low confidence.",
      "unsupported_added_findings": [
        "Debt-funded buybacks are asserted as an established Crocs vulnerability without support in the bounded record.",
        "The Nintendo statement that cyclical cash, not solvency, is the weakness is too definitive while usable securities, project spending, the operating floor, dividend timing, and the dated minimum remain unresolved."
      ],
      "material_effect": "Crocs changes from a positive Adequate/Watch presentation to a demonstrated Fragile survival result. Nintendo loses the Strong/Watch conclusion and asserted minimum, becoming Unknown/Unclear with Low confidence pending a dated, non-duplicative funding bridge."
    },
    {
      "unit": "B5",
      "decision": "PASS",
      "challenged_claims": [
        "Simple DCF is Not applicable because a known negative year and launch-related uneven funding cannot be represented by the model's positive smooth two-stage path without a dated cash schedule.",
        "With no comparable full-cycle current-scale dated schedule or supported alternative, valuation is Not calculable and Bear/Base/Bull intrinsic values and price comparisons are N/A; the reproduced smooth outputs are only a mechanical what-if."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:12-20",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:71-80",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:82-90",
        "/srv/investing/investing-hub/governance/template-company.md:265-310"
      ],
      "required_change": "None. Retain the N/A outputs and keep any reproduced smooth values segregated as a mechanical what-if until a claim-matched dated schedule or supported alternative method is available.",
      "unsupported_added_findings": [],
      "material_effect": "The passage correctly removes the completed Cash DCF, intrinsic-value claim, and current-price conclusion, setting Coverage to Limited and valuation status to Not calculable rather than manufacturing a result."
    },
    {
      "unit": "B6",
      "decision": "HALT",
      "challenged_claims": [
        "Formula dividends returned JPY1,302.6 billion of JPY1,376.5 billion CFO in FY2022-FY2026.",
        "The one-dollar test passes on market value because market capitalization rose about JPY2.2 per yen retained since March 2021, derived from reported PER, EPS, and current price.",
        "The current price is above estimated intrinsic value, while Capital allocation remains 3/5 and Overall management remains Adequate at 3.0/5."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/frameworks/simple-management.md:24-45",
        "/srv/investing/investing-hub/frameworks/simple-management.md:47-59",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:20",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:78-90",
        "/srv/investing/investing-hub/governance/template-company.md:41-47",
        "/srv/investing/investing-hub/governance/template-company.md:302-309",
        "/srv/investing/investing-hub/governance/template-company.md:348-358"
      ],
      "required_change": "Remove or source-reconcile the JPY1,302.6 billion dividend and JPY1,376.5 billion CFO figures. Use actual aligned opening and closing shares and March endpoints for the JPY2.627 and JPY3.433 market-capitalization ratios, label them only as market cross-checks, and identify JPY2.170 as the mismatched-endpoint report-date variant. State that no clean incremental-capital denominator or contemporaneous opening intrinsic value exists, so no one-dollar-test pass is established. Remove the current-price-above-intrinsic-value claim. Retain 3/5 and Adequate 3.0/5 only if independent evidence in the surrounding Management record supports them; otherwise use N/A/INVESTIGATE.",
      "unsupported_added_findings": [
        "The JPY1,302.6 billion dividends and JPY1,376.5 billion CFO totals are not in the bounded evidence packet and conflict with its supplied retained-capital record as the stated basis.",
        "The PER/EPS/current-price derivation is not supplied and does not establish aligned opening and closing market capitalization using actual shares.",
        "The current-price-above-estimated-intrinsic-value statement relies on a valuation that the supplied cash record cannot support as a completed intrinsic-value calculation."
      ],
      "material_effect": "The one-dollar-test pass and intrinsic-value comparison are removed. Capital-allocation score, overall 3.0/5 classification, and Medium confidence must be reassessed if they depended materially on those unsupported claims; share-price appreciation alone cannot sustain them."
    }
  ],
  "counts": {
    "pass": 3,
    "halt": 3
  },
  "limitations": [
    "This is answer-key-blind but not factually independent: it is a bounded semantic review using only the supplied pack and four frozen contracts.",
    "The reader is in the same model family and shared task context as the surrounding evaluation, so model-correlated interpretation and context leakage risk remain.",
    "No web sources, Forge files, or other Investing Hub files were inspected; facts beyond the bounded evidence packet were not independently verified."
  ]
}
```

## Sources

1. `forge/ideas/company-report-cold-conformance-review-r01.md` -- root
   question, retrospective paired-review plan, support threshold, stop rules,
   alternatives, and limitations. [high]
   - `forge/protocol.md` -- research independence, artifact, source, board,
     transaction, handoff, and read-only-learning rules. [high]
   - `STATUS.md` -- selected research row and preserved unrelated human-review
     row at starting HEAD. [high]
   - `logbook/progress.log` -- exact prior handoffs through ENT-035. [high]
   - `logbook/errors.log` -- prior process-failure boundary through ENT-041.
     [high]
   - `LEARNINGS.md` -- full-contract comparator, package preservation,
     claimed-result, and bounded-tooling lessons kept read-only. [high]
2. `governance/template-research.md` -- research body and pre-write checklist.
   [high]
   - `governance/skills/forge-research/SKILL.md` -- evidence, Brain, web,
     alternatives, uncertainty, and evaluation-handoff procedure. [high]
   - `governance/skills/forge-loop-feynman/SKILL.md` -- provisional explanation,
     gaps, checked evidence, and fresh synthesis order. [high]
3. `investing-hub:governance/template-company.md` -- complete pre-release hard
   gate, framework application, report labels, sources, and tested outputs.
   [high]
   - `investing-hub:frameworks/simple-management.md` -- retained-capital,
     incremental-return, actual-share, score, confidence, and no-price-only
     requirements. [high]
   - `investing-hub:frameworks/simple-dcf.md` -- positive-path applicability,
     negative-year routing, input, verification, type-label, N/A, and HALT rules.
     [high]
   - `investing-hub:frameworks/financial-health.md` -- usable cash, dated bridge,
     maturities, no-double-count, no-refinancing, shortfall, confidence, and
     classification rules. [high]
   - `investing-hub:companies/NTDOY.md` -- original Nintendo Management,
     Financial Health, Valuation, thesis, and source trail. [high]
   - `investing-hub:companies/CROX.md` -- original Crocs Financial Health,
     thesis, and source trail. [high]
4. `forge/research/valuation-consistent-retained-earnings-test-r01.md` --
   retained-capital calculations, current-rule comparison, correction, and
   limitations. [high]
   - `forge/graveyard/valuation-consistent-retained-earnings-test-evaluation-r01.md`
     -- independent arithmetic, report-only correction, zero decision delta,
     and REJECT boundary. [high]
   - `forge/research/nintendo-cycle-path-dcf-applicability-r01.md` -- exact DCF
     applicability record, arithmetic, path sensitivities, and correction. [high]
   - `forge/graveyard/nintendo-cycle-path-dcf-applicability-evaluation-r01.md` --
     current-rule HALT, reproduced values, report correction, and REJECT boundary.
     [high]
   - `forge/research/company-liquidity-stress-bridge-r01.md` -- source-pinned
     stresses, formulas, current-contract comparison, and correction. [high]
   - `forge/graveyard/company-liquidity-stress-bridge-evaluation-r01.md` --
     independent arithmetic, supported classifications, and REJECT boundary.
     [high]
   - `forge/graveyard/forge-proposal-claim-verification-map-evaluation-r02.md` --
     equal detection, divergent inventories, record burden, and rejected map.
     [high]
5. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- fresh review, focused evidence packets, exact-artifact evidence, and review limits. [medium]
   - `agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md` --
     decision-complete packets, automation bias, review cost, and outcome metrics.
     [medium]
   - `agentic-brain:library/communication/source-verification-and-fact-checking.md`
     -- claim decomposition, upstream sources, calculation reproduction,
     independent review, and evidence-matched conclusions. [medium]
6. Berkshire Hathaway Inc. "Chairman's Letter - 1983," March 14, 1984,
   owner-related principles and retained-earnings passage. The USD1 market-value
   test and five-year rolling basis were checked.
   https://www.berkshirehathaway.com/letters/1983.html [high]
7. Crocs, Inc. "Form 10-Q for the quarterly period ended June 30, 2026,"
   July 30, 2026, balance sheet, Note 8, and liquidity section. Cash, revolver
   draw and capacity, expiry, international-cash qualification, repurchases, and
   total borrowings were checked.
   https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm
   [high]
8. Nintendo Co., Ltd. "Annual Report 2026," 2026, key-data, cash-flow,
   facilities, financial-asset, and lease passages. Cash variation, cash
   definition, facilities, investments, and operating leases were checked in
   extracted official PDF text.
   https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf [high]
9. CFA Institute. "Standard V(A) Diligence and Reasonable Basis," accessed
   2026-10-01. The Standard, Quantitative Research and Techniques, and
   Compliance Practices passages were checked for diligence,
   independence, research basis, cycle coverage, scenarios, output accuracy,
   and cash-flow sensitivity.
   https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a
   [high]
