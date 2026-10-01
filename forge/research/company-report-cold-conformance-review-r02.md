---
name: company-report-cold-conformance-review
id: 20261001T111239Z
tier: research
pipeline: 20261001T083505Z
author: Researcher
tags: [value-investing, company-research, verification, review]
links:
  - forge/ideas/company-report-cold-conformance-review-r01.md
  - forge/research/company-report-cold-conformance-review-r01.md
  - forge/evaluations/company-report-cold-conformance-review-evaluation-r01.md
  - governance/template-research.md
  - governance/skills/forge-research/SKILL.md
  - governance/skills/forge-loop-feynman/SKILL.md
  - forge/protocol.md
  - LEARNINGS.md
  - forge/research/forge-research-evidence-package-gate-r01.md
  - forge/graveyard/forge-research-evidence-package-gate-evaluation-r01.md
  - investing-hub:governance/template-company.md
  - investing-hub:frameworks/simple-management.md
  - investing-hub:frameworks/simple-dcf.md
  - investing-hub:frameworks/financial-health.md
  - agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md
  - https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm
confidence: medium
---
# Research Revision: Company Report Cold Conformance Review

## Question and Method

This revision answers the evaluation's blocking question: can the two-reader
result be supported by complete, inspectable execution receipts rather than by
reader self-report or the research author's trace summary? The root question
remains whether cold readers applying the complete current company-report
contracts can distinguish all six challenged original passages from their
corrected controls without verdict or answer-key access.[1][2]

At starting Forge HEAD `4562aab16e1aa7c2a5774808493cec2b1d42fdbd`, the
worktree was clean. The complete board was valid. Pipeline
`20261001T083505Z` was the oldest eligible research-loop row by its
`2026-10-01 09:38 UTC` update; pipeline `20261001T103830Z` was a later
research row, and pipeline `20260930T083956Z` remained an unrelated valid
human-review row. Progress ended at ENT-038 and errors at ENT-045. The root
idea author is Analyst and the revision author is Researcher, so the separate-
author gate passes. The selected evaluation returns the exact r01 research to
`research` under REVISE cycle 1 of 2.[2][3]

Before the corrective runs, the provisional explanation was that the six-unit
semantic result would probably reproduce because the r01 packs, outputs,
current contracts, and independent evaluator checks agreed. The blocker was
not the displayed classifications; it was the absence of evidence showing
what each reader actually received and opened. The predeclared disconfirmation
conditions were any extra file or skill read, any web call, any Forge or answer-
key access, a pack-hash mismatch, a missed original, a false HALT on a corrected
control, an unsupported corrected-control finding, or an unavailable exact
output or observable tool receipt. A reader's own statement about its context
would not close the gap.[2][5]

The current Investing Hub index returned literal `OK --` at HEAD
`0d7995529758257669bf1726c6692fac85b25f9c`; the complete company template
and management, DCF, and financial-health frameworks were read in full. Their
bytes match the contract revision used in r01. The current Brain index returned
literal `OK --` at HEAD `6ea38c66b6ee6d1739cd2511db91fa9630d6caf5`;
the top three relevant topics were read in full. They distinguish observable
trace coverage from hidden reasoning, require task, environment, harness,
protocol, and raw run artifacts for evaluation claims, and treat a focused
review packet and fresh context as evidence classes rather than automatic
correctness.[4][5]

The current Forge index also returned literal `OK --`. Its top three results
were the exact idea, r01 research, and evaluation; two additional relevant
prior files were read in full. Prior Forge work confirms that a procedural or
reader result is recoverable only when its rules, inputs, invocation, raw
results, and separate records are available, but it also found that adding a
new generic evidence-package rule changed no tested classification over the
full current contract.[7] This revision therefore corrects the selected
artifact rather than proposing another template rule.

The two original 12,293-byte base packs were extracted from r01 and reproduced
their declared SHA-256 identities exactly. A first extractor omitted the
terminal line feed and failed its hash gate; it was corrected before any reader
run, and the failure is recorded in `logbook/errors.log`. Each base was then
concatenated byte-for-byte with one 70,981-byte shared suffix containing
line-numbered snapshots of all four current contracts. The resulting full packs
were 83,274 bytes:

| Object | SHA-256 |
|:--|:--|
| Reader A base | `a1ccf25286d4078eaa24c69e2943700926a135c8c864b3ce36f5ddbea81100de` |
| Reader B base | `48423cfd80a976c7b855b3d30a8903459c288d5a189b4701d62338e83f34552e` |
| Shared contract suffix | `c13049c07f3924b330bc2585204ee8e7349c861d4d5c9563e81a12c3577d9250` |
| Full Reader A pack | `cf918b7e83ef6075381d4c4391ca2f906aec38d8943f294bf83462947f5b70b2` |
| Full Reader B pack | `de8f2b9d30d37845689d4d69f43db5bbe6ebf1ec7ad893f60177cf9f1e165ddc` |

The suffix identifies the source revision and exact source-file hashes. Reader
A and Reader B were launched as separate delegated contexts with one permitted
input file each and one permitted JSON output each. Their exact task goals,
context strings, output schema, ordered observable tool calls and results,
access boundary, output identities, and deviations are preserved in Appendix A.
Appendices B-D preserve every parent-supplied pack byte in reconstructable
form: full pack A is Appendix B immediately concatenated with Appendix D, and
full pack B is Appendix C immediately concatenated with Appendix D. Appendices
E-F preserve the exact saved outputs. Appendices G-H preserve the append-only
observable live transcripts. This is an observable execution receipt, not a
claim to hidden model reasoning.[5]

Each reader timestamped before the pack read, verified the expected pack hash,
read only that pack, timestamped after analysis, calculated elapsed seconds,
and wrote one exact JSON result. Both readers attempted one inline Python
elapsed-time command after the pack read; unattended policy blocked both before
execution. Fixed `expr` commands then returned 69 and 65 seconds. The blocked
commands read no file, returned no data, and changed no output classification,
but the deviation is preserved in the receipts and error log rather than
silently omitted.

The r01 source packet remains retrospective and curated. The independent web
check of Crocs' official June 2026 Form 10-Q again confirms USD1.0 billion of
revolver commitments, USD134.0 million drawn, USD0.6 million of letters of
credit, and USD1.3 billion of face-value borrowings at June 30, 2026.[6] This
primary-source check supports the bounded liquidity packet; it does not make
the two readers factually independent or prove prospective review benefit.

## Evidence and Findings

### Both strict target-only readers reproduced the complete paired result

Both readers returned three HALTs and three PASSes in counterbalanced order.
Every original passage HALTed and every corrected control PASSed. The result is
identical to r01 and to the evaluator's semantic recomputation:[2]

| Claim unit | Reader A | Reader B | Corrective-run result |
|:--|:--|:--|:--|
| Original retained capital | A1 HALT | B6 HALT | Both removed the unsupported market-only pass and intrinsic-value price claim without imposing an untested replacement score. |
| Corrected retained capital | A4 PASS | B3 PASS | Both accepted aligned market ratios only as qualified cross-checks and retained the missing incremental-return and opening-value limits. |
| Original DCF | A5 HALT | B2 HALT | Both rejected the completed Cash DCF, intrinsic-value figures, and price conclusion because the positive smooth path cannot represent the supplied negative year and uneven funding. |
| Corrected DCF | A2 PASS | B5 PASS | Both accepted Limited / Not applicable / Not calculable / N/A treatment and retained the smooth outputs only as mechanical what-ifs. |
| Original liquidity | A3 HALT | B4 HALT | Both rejected Crocs' claimed minimum and positive classification and Nintendo's asserted minimum and Strong/Watch classification. |
| Corrected liquidity | A6 PASS | B1 PASS | Both accepted Crocs Fragile with a shortfall no later than February 17, 2029 and Nintendo Unknown/Unclear with unresolved dated evidence. |

Neither corrected control contains an unsupported added finding in either
output. The two retained-capital reviews differ slightly in wording about
whether the wider management score needs reassessment, but both preserve the
bounded result: the challenged market and intrinsic-value claims cannot support
a pass or score change by themselves. The DCF and liquidity classifications
match on every tested status, method, value, and confidence field. These are
same-model-family reproducibility observations, not independent factual
corroboration.[4][5]

### The observable context boundary is now directly inspectable

The delegation tool trace and append-only live transcripts show the same seven
observable operations for each reader: start timestamp, pack hash, one complete
pack read, end timestamp, one blocked arithmetic attempt, one successful fixed
arithmetic command, and one output write. The trace records no `skill_view`,
web call, search, second file read, Forge read, canonical Investing Hub read, or
session-history read. The exact dispatched contexts prohibit those accesses and
contain no verdict, expected label, defect location, prior output, or evaluation
body. The only target data are the six units, shared source/calculation record,
and frozen contracts in the embedded pack.

The renderer abbreviates large prompt and file-result fields in the 6,407-byte
live transcript files. The receipt therefore does not pretend that those short
renderer files alone contain all bytes. Appendix A preserves the exact dispatch
strings and ordered results; Appendices B-D preserve the full input bytes; and
Appendices E-F preserve the full output bytes. Their identities are:

| Record | Bytes | SHA-256 |
|:--|--:|:--|
| Delegation receipt | 21,454 | `b09ab479806659d04a8cb4737d7ba31c07435552c725be7ee8341fe058678166` |
| Reader A saved output | 10,945 | `fdfaee5c41a7f76baf051c97c17d0fe293acfb3e74498e18689ed289a0fd1d84` |
| Reader B saved output | 10,731 | `0646cea51f301a7ee52052a98ce32a4c62ecf83f2d071f472b18b870d32bb2a6` |
| Reader A live transcript | 6,407 | `af462485b1f6d7a111840edbb7a553c2cadc05c1c97a5d78e05aa16455f310e6` |
| Reader B live transcript | 6,407 | `0427d057aef542574c6610bd1b5c1c3a5f13b709a2f0e80b8697bc4eeca9de5d` |

This closes the evaluation's specific access-receipt gap. It supports the claim
that the corrective pair received no Forge verdict or answer-key material
through observable tool access. It does not prove absence of shared model
priors, hidden reasoning, or correlated interpretation. Brain prior work makes
the same distinction: a trace establishes only the operations and fields its
instrumentation records, while semantic correctness still requires direct rule,
source, and outcome checks.[5]

### Exact byte boundaries and source identities are explicit

Every embedded component and saved output is hashed over its complete file
bytes including the terminal line feed. Full pack hashes cover the original
base plus the shared suffix. The output hashes cover the exact JSON objects
written by each reader. The transcript hashes cover the exact abbreviated
renderer files. The receipt hash covers the exact task contexts, schema,
observed operation sequence, content identities, and stated limits. The
components are embedded before `## Sources`, so a later evaluator can extract
and hash them without relying on scratch retention.

The shared suffix records the four current source hashes:

| Governing source | SHA-256 |
|:--|:--|
| `investing-hub:governance/template-company.md` | `342ec41f117415fe8e6e669c03525b1ed6432a7f402941afa094ad3c509348e3` |
| `investing-hub:frameworks/simple-management.md` | `73c7db5c4afaf474b463efdf4cab263e3445bb2ae4b7f8c42669b0a5660aa3de` |
| `investing-hub:frameworks/simple-dcf.md` | `bf1467f8d099ab161625e9f44b469899c049a9732115bcdf4d7024f28f0acffa` |
| `investing-hub:frameworks/financial-health.md` | `6c34a68f8b2884998f1836cc10f27953ca9cfbdbdc5c16f4bcd0e16c3d4c40ca` |

These current rules independently require actual-share and incremental-return
support rather than price-only stewardship, route negative or uneven cash paths
away from the smooth simple DCF, and require dated stressed funding without
lease double counting or assumed refinancing. The company template permits a
supported negative or limited result to PASS and HALTs unsupported claims or
misleading completion labels.[4] The readers' classification pattern therefore
follows the current contracts; agreement itself is not treated as factual proof.

### The result remains a retrospective capability test

The corrective run establishes a narrower and stronger statement than r01:
two strict target-only same-model-family readers, whose observable access and
complete inputs/outputs are preserved, can classify this frozen six-unit
package with no miss or corrected-control false HALT. It still does not show
that an ordinary report author would assemble the same packet before knowing a
defect, that a cold reviewer would discover an unseen error from a full company
file, or that adding a review step lowers future error rates or total cost.

The packets remain built from adjudicated retrospective cases. The source
record is complete for the tested claims but not for unrelated report sections.
The original pre-release author-side execution remains unavailable. The readers
share the model family, task schema, contracts, and source packet. Their elapsed
69 and 65 seconds exclude packet construction and human review. The blocked
arithmetic attempts also show that a complete receipt can contain a harmless
process failure; procedural visibility does not convert that failure into
independent evidence.

## Alternatives and Implications

| Alternative | Evidence | Implication |
|:--|:--|:--|
| Preserve the original r01 execution receipts | The r01 tool-access and delegated-context bytes were not retained. | Impossible without inventing history; the evaluation correctly rejected reconstruction from the author's summary. |
| Do nothing | The displayed outputs remain semantically usable, but the decisive blind-pair threshold stays unverified.[2] | No proposal-supporting handoff would be justified. |
| Use reader self-reports or a parent trace summary | Reader B's r01 limitation statement contradicted the author's disclosed extra skill read.[2] | Rejected; statements about access are not access receipts. |
| Rerun one reader | One strict receipt could test one order only. | Insufficient for the root idea's predeclared two-reader, counterbalanced threshold.[1] |
| Rerun both readers with self-contained frozen packs and preserved receipts | Both runs stayed within the observable boundary and reproduced all twelve classifications. | Smallest correction that answers every evaluation item without changing the analytical contracts. |
| Add a generic evidence-package rule | Prior controlled work found zero classification change over the current semantic gate.[7] | Not supported by this correction; no template or skill proposal follows. |
| Instrument hidden reasoning or adopt a tracing platform | No checked evidence shows this is necessary to decide the bounded access question; hidden reasoning is not the claimed result.[5] | Disproportionate and outside Forge scope. |

The evidence supports returning the corrected research to independent
evaluation. A later evaluator can now judge whether the strict receipt and
unchanged 12-classification result meet the root threshold for only a reversible
prospective trial. This report does not issue ADVANCE, propose a permanent gate,
edit either company report or framework, authorize implementation, or update
`LEARNINGS.md`.

For value-investing use, the economic implication remains conservative. A
review control has value only if it stops unsupported positive stewardship,
liquidity, or intrinsic-value language without blocking valid negative or
uncertain conclusions. Both readers did that in the curated sample. The sample
does not measure the probability of doing so prospectively, the packet-
preparation cost, or the effect on an investment decision. Those unknowns must
remain visible rather than be converted into a stronger process recommendation.

## Response to Feedback and Remaining Questions

The evaluation's four corrective requirements are answered explicitly:[2]

1. **Complete receipts:** Appendix A preserves each exact delegated goal,
   context, output schema, ordered observable call and result, access boundary,
   output identity, transcript identity, and deviation. Appendices B-H preserve
   the complete parent-supplied input components, exact outputs, and observable
   transcripts. No reader self-report is used as the sole access proof.
2. **New passes, not repaired history:** The unavailable original receipts are
   not reconstructed. Both runs are labeled R02, use new timestamps, new full-
   pack hashes, new outputs, and a new delegation ID.
3. **Exact byte boundaries:** Every base, suffix, full pack, output, receipt, and
   transcript has an explicit byte count and SHA-256. All component and output
   hashes include the terminal line feed. Full-pack construction is stated as
   exact byte concatenation.
4. **Recomputed result with retained limits:** Both readers again return all six
   originals HALT and all six corrected controls PASS. The report retains the
   curated retrospective scope, same-model-family dependence, unknown original
   author-side execution, unknown packet-preparation cost, no causal future-
   error claim, and no permanent-gate recommendation.

No receipt blocker remains for observable file, skill, web, command, timestamp,
pack, or output access. The live renderer does abbreviate large displayed
fields, but the receipt embeds the exact dispatch strings and the artifact
embeds all full input and output bytes. What remains unknown is outside the
bounded claim: hidden model reasoning, performance on unseen reports, a
controlled self-review comparator, different-model or human agreement,
prospective miss and false-HALT rates, author and reviewer time, focus-packet
assembly without hindsight, revision outcomes, and investment-decision value.

Confidence is medium. Confidence is high in the exact corrective-run result and
observable context boundary because both output schemas validate, pack and
output hashes match, tool traces show one permitted read per reader, and every
classification reproduces. Overall confidence remains medium because this is a
same-model-family retrospective sample of two reports and three known defect
classes, the packet was curated from adjudicated evidence, live transcript
rendering abbreviates large fields, and no prospective outcome or total cost is
measured. Confidence would rise after a predeclared unseen-report trial with the
same receipt discipline and measured packet, author, reviewer, revision, miss,
false-HALT, and unsupported-expansion outcomes. It would fall if extraction of
the embedded components fails a stated hash, an evaluator finds unrecorded
answer-key access, or a target-only rerun misses a blocker or rejects a valid
control.

`LEARNINGS.md` remains unchanged. This is a research revision, and the existing
high-confidence preservation lesson already names separate evidence for blind
and independent-reader claims.[3]

## Appendix A - Exact Delegation Receipt

The bytes inside the following fence are the complete
`delegation-receipt.json` object. SHA-256:
`b09ab479806659d04a8cb4737d7ba31c07435552c725be7ee8341fe058678166`.

````json
{
  "delegation_id": "deleg_d4aa313a",
  "limits": [
    "The live transcript renderer abbreviates large prompt and result fields; this receipt embeds the exact task goal/context, full packet components, exact saved outputs, and ordered tool results needed to reconstruct each run.",
    "The receipt records observable tool execution, not hidden model reasoning."
  ],
  "receipt_version": 1,
  "selected_pipeline": "20261001T083505Z",
  "selected_stage": "research",
  "starting_forge_head": "4562aab16e1aa7c2a5774808493cec2b1d42fdbd",
  "tasks": [
    {
      "artifacts": {
        "live_transcript": {
          "bytes": 6407,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/delegation/live/deleg_d4aa313a/task-0.log",
          "sha256": "af462485b1f6d7a111840edbb7a553c2cadc05c1c97a5d78e05aa16455f310e6"
        },
        "pack": {
          "bytes": 83274,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md",
          "sha256": "cf918b7e83ef6075381d4c4391ca2f906aec38d8943f294bf83462947f5b70b2"
        },
        "saved_output": {
          "bytes": 10945,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/official-reader-a-r02.json",
          "sha256": "fdfaee5c41a7f76baf051c97c17d0fe293acfb3e74498e18689ed289a0fd1d84"
        }
      },
      "context": "You are Official Cold Reader A R02 in a bounded Investing Hub company-report conformance rerun. This closed context is part of the experiment. The sole permitted input file is `/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md`, expected SHA-256 `cf918b7e83ef6075381d4c4391ca2f906aec38d8943f294bf83462947f5b70b2`. It contains the six review units, complete source/calculation record, and line-numbered frozen snapshots of all four governing contracts. Do not load or read any skill. Do not read any Forge file, canonical Investing Hub file, other scratch file, repository instruction, transcript, web source, or session history. Do not search or discover files. Do not call web tools. The only authorized write is `/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/official-reader-a-r02.json`.\n\nProcedure: (1) Before reading the pack, run exactly one UTC timestamp command that returns ISO-8601 UTC and epoch seconds. (2) Run `sha256sum` on the sole input and require the expected digest. (3) Read the sole input in full. Apply the complete semantic contracts embedded there to all six units in pack order. Do not seek or infer a hidden answer key; classify the text and supplied evidence. A negative or uncertain finding may PASS. HALT only unsupported or misleading tested claims. Cite the canonical contract paths and embedded canonical line numbers. For each unit provide the exact challenged claims, required change, unsupported added findings, and material effect. (4) After analysis, run exactly one second UTC timestamp command and calculate elapsed seconds with a tool. (5) Construct one complete JSON object matching the requested schema. `receipt.files_read` must list only the sole pack path; `receipt.skills_read` must be empty; `receipt.web_calls` must be 0; `receipt.commands` must list the exact commands you ran in order. (6) Use write_file to save that exact JSON object, with no Markdown fences and a terminal newline, to the authorized output path. Return the same JSON object and no prose. Do not read the output back. Same-model-family limitations must be stated; do not call yourself factually independent.",
      "deviation": "One inline Python elapsed-time command was policy-blocked after the pack read. The fixed expr calculation succeeded. The blocked command read no file, returned no data, and did not change the context boundary or decisions.",
      "goal": "Perform and durably preserve Official Cold Reader A R02's strict target-only review of all six pack-A units, with a complete execution receipt visible in this delegated transcript and an exact saved JSON output.",
      "observed_access_boundary": {
        "basis": "delegation tool trace and append-only live transcript",
        "files_read": [
          "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md"
        ],
        "other_tool_reads": [],
        "skills_read": [],
        "web_calls": 0
      },
      "observed_tool_sequence": [
        {
          "command": "date -u '+%Y-%m-%dT%H:%M:%SZ %s'",
          "ordinal": 1,
          "result": "2026-10-01T11:05:21Z 1790852721",
          "status": "ok",
          "tool": "terminal"
        },
        {
          "command": "sha256sum /home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md",
          "ordinal": 2,
          "result": "cf918b7e83ef6075381d4c4391ca2f906aec38d8943f294bf83462947f5b70b2  /home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md",
          "status": "ok",
          "tool": "terminal"
        },
        {
          "content_identity": {
            "bytes": 83274,
            "reproduction": "base component plus shared contract suffix embedded in the research artifact",
            "sha256": "cf918b7e83ef6075381d4c4391ca2f906aec38d8943f294bf83462947f5b70b2"
          },
          "limit": 2000,
          "offset": 1,
          "ordinal": 3,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md",
          "status": "ok",
          "tool": "read_file"
        },
        {
          "command": "date -u '+%Y-%m-%dT%H:%M:%SZ %s'",
          "ordinal": 4,
          "result": "2026-10-01T11:06:30Z 1790852790",
          "status": "ok",
          "tool": "terminal"
        },
        {
          "command": "python3 -c 'print(1790852790 - 1790852721)'",
          "error": "Command flagged as dangerous (script execution via -e/-c flag) in unattended cron mode; command did not execute.",
          "ordinal": 5,
          "status": "blocked",
          "tool": "terminal"
        },
        {
          "command": "expr 1790852790 - 1790852721",
          "ordinal": 6,
          "result": "69",
          "status": "ok",
          "tool": "terminal"
        },
        {
          "content_identity": {
            "bytes": 10945,
            "sha256": "fdfaee5c41a7f76baf051c97c17d0fe293acfb3e74498e18689ed289a0fd1d84"
          },
          "ordinal": 7,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/official-reader-a-r02.json",
          "status": "ok",
          "tool": "write_file",
          "verified": true
        }
      ],
      "output_schema": {
        "properties": {
          "counts": {
            "properties": {
              "halt": {
                "type": "integer"
              },
              "pass": {
                "type": "integer"
              }
            },
            "required": [
              "pass",
              "halt"
            ],
            "type": "object"
          },
          "elapsed_seconds": {
            "type": "integer"
          },
          "ended_utc": {
            "type": "string"
          },
          "limitations": {
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "order": {
            "items": {
              "type": "string"
            },
            "maxItems": 6,
            "minItems": 6,
            "type": "array"
          },
          "pack_sha256": {
            "type": "string"
          },
          "reader": {
            "type": "string"
          },
          "receipt": {
            "properties": {
              "allowed_input_path": {
                "type": "string"
              },
              "commands": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "files_read": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "output_path": {
                "type": "string"
              },
              "skills_read": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "web_calls": {
                "type": "integer"
              }
            },
            "required": [
              "allowed_input_path",
              "files_read",
              "skills_read",
              "web_calls",
              "commands",
              "output_path"
            ],
            "type": "object"
          },
          "started_utc": {
            "type": "string"
          },
          "units": {
            "items": {
              "properties": {
                "challenged_claims": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "contract_citations": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "decision": {
                  "enum": [
                    "PASS",
                    "HALT"
                  ],
                  "type": "string"
                },
                "material_effect": {
                  "type": "string"
                },
                "required_change": {
                  "type": "string"
                },
                "unit": {
                  "type": "string"
                },
                "unsupported_added_findings": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                }
              },
              "required": [
                "unit",
                "decision",
                "challenged_claims",
                "contract_citations",
                "required_change",
                "unsupported_added_findings",
                "material_effect"
              ],
              "type": "object"
            },
            "maxItems": 6,
            "minItems": 6,
            "type": "array"
          }
        },
        "required": [
          "reader",
          "pack_sha256",
          "started_utc",
          "ended_utc",
          "elapsed_seconds",
          "order",
          "units",
          "counts",
          "limitations",
          "receipt"
        ],
        "type": "object"
      },
      "runtime": {
        "exit_reason": "completed",
        "model": "gpt-5.6-sol-900k",
        "schema_valid": true
      },
      "task_index": 0
    },
    {
      "artifacts": {
        "live_transcript": {
          "bytes": 6407,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/delegation/live/deleg_d4aa313a/task-1.log",
          "sha256": "0427d057aef542574c6610bd1b5c1c3a5f13b709a2f0e80b8697bc4eeca9de5d"
        },
        "pack": {
          "bytes": 83274,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md",
          "sha256": "de8f2b9d30d37845689d4d69f43db5bbe6ebf1ec7ad893f60177cf9f1e165ddc"
        },
        "saved_output": {
          "bytes": 10731,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/official-reader-b-r02.json",
          "sha256": "0646cea51f301a7ee52052a98ce32a4c62ecf83f2d071f472b18b870d32bb2a6"
        }
      },
      "context": "You are Official Cold Reader B R02 in a bounded Investing Hub company-report conformance rerun. This closed context is part of the experiment. The sole permitted input file is `/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md`, expected SHA-256 `de8f2b9d30d37845689d4d69f43db5bbe6ebf1ec7ad893f60177cf9f1e165ddc`. It contains the six review units, complete source/calculation record, and line-numbered frozen snapshots of all four governing contracts. Do not load or read any skill. Do not read any Forge file, canonical Investing Hub file, other scratch file, repository instruction, transcript, web source, or session history. Do not search or discover files. Do not call web tools. The only authorized write is `/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/official-reader-b-r02.json`.\n\nProcedure: (1) Before reading the pack, run exactly one UTC timestamp command that returns ISO-8601 UTC and epoch seconds. (2) Run `sha256sum` on the sole input and require the expected digest. (3) Read the sole input in full. Apply the complete semantic contracts embedded there to all six units in pack order. Do not seek or infer a hidden answer key; classify the text and supplied evidence. A negative or uncertain finding may PASS. HALT only unsupported or misleading tested claims. Cite the canonical contract paths and embedded canonical line numbers. For each unit provide the exact challenged claims, required change, unsupported added findings, and material effect. (4) After analysis, run exactly one second UTC timestamp command and calculate elapsed seconds with a tool. (5) Construct one complete JSON object matching the requested schema. `receipt.files_read` must list only the sole pack path; `receipt.skills_read` must be empty; `receipt.web_calls` must be 0; `receipt.commands` must list the exact commands you ran in order. (6) Use write_file to save that exact JSON object, with no Markdown fences and a terminal newline, to the authorized output path. Return the same JSON object and no prose. Do not read the output back. Same-model-family limitations must be stated; do not call yourself factually independent.",
      "deviation": "One inline Python elapsed-time command was policy-blocked after the pack read. The fixed expr calculation succeeded. The blocked command read no file, returned no data, and did not change the context boundary or decisions.",
      "goal": "Perform and durably preserve Official Cold Reader B R02's strict target-only review of all six pack-B units, with a complete execution receipt visible in this delegated transcript and an exact saved JSON output.",
      "observed_access_boundary": {
        "basis": "delegation tool trace and append-only live transcript",
        "files_read": [
          "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md"
        ],
        "other_tool_reads": [],
        "skills_read": [],
        "web_calls": 0
      },
      "observed_tool_sequence": [
        {
          "command": "date -u '+%Y-%m-%dT%H:%M:%SZ %s'",
          "ordinal": 1,
          "result": "2026-10-01T11:05:16Z 1790852716",
          "status": "ok",
          "tool": "terminal"
        },
        {
          "command": "sha256sum /home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md",
          "ordinal": 2,
          "result": "de8f2b9d30d37845689d4d69f43db5bbe6ebf1ec7ad893f60177cf9f1e165ddc  /home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md",
          "status": "ok",
          "tool": "terminal"
        },
        {
          "content_identity": {
            "bytes": 83274,
            "reproduction": "base component plus shared contract suffix embedded in the research artifact",
            "sha256": "de8f2b9d30d37845689d4d69f43db5bbe6ebf1ec7ad893f60177cf9f1e165ddc"
          },
          "limit": 2000,
          "offset": 1,
          "ordinal": 3,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md",
          "status": "ok",
          "tool": "read_file"
        },
        {
          "command": "date -u '+%Y-%m-%dT%H:%M:%SZ %s'",
          "ordinal": 4,
          "result": "2026-10-01T11:06:21Z 1790852781",
          "status": "ok",
          "tool": "terminal"
        },
        {
          "command": "python3 -c 'print(1790852781 - 1790852716)'",
          "error": "Command flagged as dangerous (script execution via -e/-c flag) in unattended cron mode; command did not execute.",
          "ordinal": 5,
          "status": "blocked",
          "tool": "terminal"
        },
        {
          "command": "expr 1790852781 - 1790852716",
          "ordinal": 6,
          "result": "65",
          "status": "ok",
          "tool": "terminal"
        },
        {
          "content_identity": {
            "bytes": 10731,
            "sha256": "0646cea51f301a7ee52052a98ce32a4c62ecf83f2d071f472b18b870d32bb2a6"
          },
          "ordinal": 7,
          "path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/official-reader-b-r02.json",
          "status": "ok",
          "tool": "write_file",
          "verified": true
        }
      ],
      "output_schema": {
        "properties": {
          "counts": {
            "properties": {
              "halt": {
                "type": "integer"
              },
              "pass": {
                "type": "integer"
              }
            },
            "required": [
              "pass",
              "halt"
            ],
            "type": "object"
          },
          "elapsed_seconds": {
            "type": "integer"
          },
          "ended_utc": {
            "type": "string"
          },
          "limitations": {
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "order": {
            "items": {
              "type": "string"
            },
            "maxItems": 6,
            "minItems": 6,
            "type": "array"
          },
          "pack_sha256": {
            "type": "string"
          },
          "reader": {
            "type": "string"
          },
          "receipt": {
            "properties": {
              "allowed_input_path": {
                "type": "string"
              },
              "commands": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "files_read": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "output_path": {
                "type": "string"
              },
              "skills_read": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "web_calls": {
                "type": "integer"
              }
            },
            "required": [
              "allowed_input_path",
              "files_read",
              "skills_read",
              "web_calls",
              "commands",
              "output_path"
            ],
            "type": "object"
          },
          "started_utc": {
            "type": "string"
          },
          "units": {
            "items": {
              "properties": {
                "challenged_claims": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "contract_citations": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "decision": {
                  "enum": [
                    "PASS",
                    "HALT"
                  ],
                  "type": "string"
                },
                "material_effect": {
                  "type": "string"
                },
                "required_change": {
                  "type": "string"
                },
                "unit": {
                  "type": "string"
                },
                "unsupported_added_findings": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                }
              },
              "required": [
                "unit",
                "decision",
                "challenged_claims",
                "contract_citations",
                "required_change",
                "unsupported_added_findings",
                "material_effect"
              ],
              "type": "object"
            },
            "maxItems": 6,
            "minItems": 6,
            "type": "array"
          }
        },
        "required": [
          "reader",
          "pack_sha256",
          "started_utc",
          "ended_utc",
          "elapsed_seconds",
          "order",
          "units",
          "counts",
          "limitations",
          "receipt"
        ],
        "type": "object"
      },
      "runtime": {
        "exit_reason": "completed",
        "model": "gpt-5.6-sol-900k",
        "schema_valid": true
      },
      "task_index": 1
    }
  ]
}
````

## Appendix B - Exact Reader A Base Packet

SHA-256: `a1ccf25286d4078eaa24c69e2943700926a135c8c864b3ce36f5ddbea81100de`.

````text
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
````

## Appendix C - Exact Reader B Base Packet

SHA-256: `48423cfd80a976c7b855b3d30a8903459c288d5a189b4701d62338e83f34552e`.

````text
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
````

## Appendix D - Exact Shared Contract Snapshot Suffix

SHA-256: `c13049c07f3924b330bc2585204ee8e7349c861d4d5c9563e81a12c3577d9250`.

````text


# Frozen current contract snapshots

These snapshots are the complete governing contracts for this rerun. Cite the canonical path shown for each snapshot. Do not open the canonical files or any other file.

## Contract snapshot: /srv/investing/investing-hub/governance/template-company.md

SHA-256: 342ec41f117415fe8e6e669c03525b1ed6432a7f402941afa094ad3c509348e3

```text
1|---
2|name: template-company
3|id: 20260924T082952Z
4|tier: core-template
5|author: Neo
6|links:
7|  - agentic-brain:governance/template-library.md
8|  - frameworks/sector-metrics.md
9|  - frameworks/simple-management.md
10|  - frameworks/simple-moat.md
11|  - frameworks/financial-health.md
12|  - frameworks/simple-dcf.md
13|  - frameworks/investment-thesis.md
14|---
15|
16|# Company Research Template -- How We Write Company Research Files
17|
18|A company research file is an evidence-backed assessment of a business, its
19|management, competitive position, financial health and valuation. It lives in
20|`companies/` and presents the findings from the investment frameworks.
21|
22|This template defines the frontmatter, body structure and quality checklist
23|for company research files. It is the format specification for full
24|assessments, not the research workflow or a replacement for the investment
25|methods. Personal company knowledge notes and research-only summaries have
26|different purposes.
27|
28|## Company Report Checklist -- HARD GATE
29|
30|Before releasing a company report, verify every applicable item against the
31|actual file, sources and calculation records. Keep this checklist in the
32|template, not in the published company report.
33|
34|- [ ] Frontmatter follows the schema below: name, id, tier, author, ticker, exchange, review_date, data_cutoff, reporting_currency, tags, links. (PASS / HALT)
35|- [ ] New report: generate a unique id with `date -u +'%Y%m%dT%H%M%SZ'`. Update: preserve the published id and original author; identify the current reviewer in the report. Dates reflect work actually performed. (PASS / HALT)
36|- [ ] Exact company, listing, share class, ADR ratio where relevant, reporting basis, units, history covered and evidence cutoff are explicit. (PASS / HALT)
37|- [ ] Business and sector analysis explain the economics, competence boundary, selected measures and valuation-method fit. (PASS / HALT)
38|- [ ] Management output includes the applicable questionnaire answers, original promises versus outcomes, scorecard and any overriding concern. (PASS / HALT)
39|- [ ] Moat output includes applicable mechanism answers, competitive forces, separate dimensional ratings, confidence and the principal threat. (PASS / HALT)
40|- [ ] Financial-health findings trace to historical statements, normalization and cash/claims bridges, and dated stressed funding; decisive gaps remain visible. (PASS / HALT)
41|- [ ] Valuation uses sector-appropriate metrics and methods, presents Base/Bull/Bear cases with the correct cash/earnings and ownership labels, and marks unsupported case values N/A with the blocker. Calculations and material sensitivities are reproduced by a second calculation. (PASS / HALT)
42|- [ ] Thesis, contrary case, permanent-loss risk and review triggers agree with the business, management, moat, funding and valuation evidence. No composite investment score or trade instruction is added. (PASS / HALT)
43|- [ ] Investment Thesis ends with Final Verdict immediately before Sources: integrated judgment, confidence, dated matching-share price, Base/Bull/Bear values and Base-case discount/premium. Its figures agree with Valuation; missing or stale evidence cannot support a current price judgment. (PASS / HALT)
44|- [ ] The analytical body contains the six framework sections below. Each section states its coverage status; supported early conclusions identify skipped work without disguising gaps as neutral scores, zeros or completed valuations. (PASS / HALT)
45|- [ ] Every analysis table is followed immediately by a short conclusion explaining what its findings mean. Normally use 3-5 sentences, fewer when sufficient or more when material complexity warrants; do not repeat the rows or pad to a quota. (PASS / HALT)
46|- [ ] The report presents results and short explanations, not a calculation notebook. Routine workings stay outside the report; retained assumptions and qualifications are sufficient to interpret the results without repeated tables or caveats. (PASS / HALT)
47|- [ ] Material facts and figures resolve to inspected sources; assumptions and interpretation are identified. Citations, calculation links and repository references resolve. (PASS / HALT)
48|- [ ] Final report follows the body order below, contains no unfilled placeholders, is ASCII-only, and uses the authorized company-file destination. Existing report identity and dated thesis changes are preserved. (PASS / HALT)
49|
50|**PASS:** the report supports its stated assessment, including a negative or
51|limited assessment. **HALT:** unsupported claims, misleading completion labels,
52|missing required output or an unauthorized write. A missing input may be
53|reported explicitly; it must not be replaced with an invented result.
54|
55|## Frontmatter Schema
56|
57|This is the company report's frontmatter, not the template's own metadata.
58|Replace placeholders; do not copy this template's id into a company report.
59|
60|```yaml
61|---
62|name: <company-research-slug>
63|id: <YYYYMMDDTHHMMSSZ>
64|tier: company-research
65|author: <original-author>
66|ticker: <exact-ticker>
67|exchange: <exchange>
68|review_date: <YYYY-MM-DD>
69|data_cutoff: <YYYY-MM-DDTHH:MM:SSZ>
70|reporting_currency: <currency-code>
71|tags: [<sector-tag>, <business-model-tag>]
72|links:
73|  - governance/template-company.md
74|  - <relevant-existing-repository-path>
75|---
76|```
77|
78|- Use a descriptive lowercase, hyphenated `name` and tags. Preserve ticker
79|  spelling and punctuation; the ticker is an identifier, not a prose slug.
80|- `review_date` is the actual review date in UTC. `data_cutoff` is the UTC
81|  information cutoff, not the year-end or the latest filing's period end.
82|  A formatting-only update does not refresh either date without a new review.
83|- `reporting_currency` is the financial-statement currency. Identify any
84|  different valuation or quoted-share currency in the body.
85|- `links` use repository-root paths within Investing Hub, and exact
86|  `repo:path` prefixes across repositories. Include only existing targets.
87|- Preserve an existing company's filename and permanent identity on updates.
88|  For a new file, use the authorized company naming convention; resolve the
89|  entity and listing before selecting the destination.
90|
91|## Body Structure
92|
93|Begin with `# <Company Name> -- <Central Research Finding>` and a short opening
94|that explains the business and the assessment. State **thesis status**,
95|**confidence** and **valuation status** separately; a supported business thesis
96|is not proof that the shares are attractively priced.
97|
98|Follow with a compact identity line: legal entity; ticker/exchange; share class
99|and ADR ratio if applicable; review date/reviewer; information cutoff; accounting
100|standard, consolidation perimeter and fiscal year-end; currency/units; history
101|and latest interim period covered. State unavailable history explicitly.
102|
103|The analytical body consists of the six framework sections below, in order.
104|Use their level-2 report headings. In each section, state **Coverage: Assessed /
105|Limited / Not applicable / Not assessed**, with the reason for a limitation or
106|exclusion. Assessed means the applicable questions were addressed, not that the
107|result was favorable. Keep coverage and supporting-record links in the relevant
108|section rather than adding a separate coverage section or scorecard.
109|
110|Keep table cells short without compressing away decisive evidence. Immediately
111|below every analysis table, add a **Summary:** paragraph explaining the main
112|conclusion, why it matters and the uncertainty or trigger that could change it.
113|Normally use 3-5 sentences; fewer are appropriate for a simple finding and more
114|when needed to explain a material issue. This applies to each table within a
115|section, not just once after the whole section. Interpret the evidence rather
116|than repeat each row, introduce unsupported claims or manufacture prose.
117|
118|Put uncertainty beside the affected claim. Present concise results tables and
119|short explanations, retaining the material assumptions, valuation basis and
120|source references rather than every calculation. Keep detailed workings in
121|temporary research records for verification; link only existing retained records,
122|never deleted scratch files. A single Markdown deliverable does not require
123|embedding the working notebook or creating companion files. Sources and optional
124|related references follow the analytical body as supporting material.
125|
126|The referenced frameworks own their methods, scoring and overrides. This
127|template controls company-report presentation: include the short summaries even
128|where a standalone framework requests table-only output. Do not change its
129|analytical rules. If a framework changes, reconcile the affected output here
130|before using a stale table. Do not import the Library's topic word counts or
131|source quotas into a company assessment.
132|
133|### 1. Business and Method
134|
135|Report heading: `## Business and Method`.
136|Apply `frameworks/sector-metrics.md`; classify the actual economics, with
137|separate rows for materially different segments where needed. Carry these
138|selected metrics into Financial Health and Valuation; do not impose the same
139|ratios or valuation method on every sector.
140|
141|| Question | Assessment / evidence |
142||:--|:--|
143|| Who pays, for what, and why do customers return? | |
144|| Segments, geography and principal competitors | |
145|| Main revenue, margin and cash-generation drivers | |
146|| Capital required and who bears financing risk | |
147|| Sector-specific measures and historical comparison | |
148|| Circle of competence and decisive limitations | |
149|| Principal valuation method / useful cross-check | |
150|
151|**Summary:** Explain how the business earns money, which drivers matter most,
152|and why the selected measures and valuation method fit. State the main
153|competence limit or accounting trap. Do not assign a sector score.
154|
155|### 2. Management
156|
157|Report heading: `## Management`.
158|Apply `frameworks/simple-management.md`. Identify the chief executive,
159|principal capital allocator, tenure and controlling owners on one line.
160|Use dated decisions, capital deployment, funding and actual share-count
161|reconciliations as evidence, not reputation or share-price performance.
162|
163|Show the framework's promises-versus-results record before the scorecard.
164|Cover its required material commitments, preserve original scope and deadlines,
165|and distinguish unavailable, not-yet-due and noncomparable outcomes from misses.
166|
167|| Statement date / original commitment | Metric, scope / target horizon | Actual year 1 / 2 / 3 | Delivery pattern / explanation |
168||:--|:--|:--|:--|
169|| | | | |
170|
171|**Summary:** Explain the pattern of delivery and candor, separating decisions
172|management controlled from external conditions. Distinguish a missed commitment
173|from dishonesty and targets not yet due from failures.
174|
175|| Category | Answers / decisive fact | Score /5 | Confidence | Concern / reassessment trigger |
176||:--|:--|--:|:--|:--|
177|| Integrity and candor | | | | |
178|| Capital allocation | | | | |
179|| Ownership and incentives | | | | |
180|| Execution and adaptability | | | | |
181|| Governance and minority treatment | | | | |
182|| **Overall** | **Framework classification / applicable override** | | | |
183|
184|**Summary:** State whether the evidence supports trusting management with owner
185|capital, why, and what could change that view. Explain any overriding concern
186|instead of allowing a favorable average to obscure it.
187|
188|Answer every applicable framework question, with a limitation or counterexample
189|per category. Follow its early-conclusion option when warranted: retain Overall,
190|the decisive evidence, override and unassessed work rather than inventing scores.
191|
192|### 3. Moat
193|
194|Report heading: `## Moat`.
195|Apply `frameworks/simple-moat.md`. Define the customer/product/geographic
196|perimeter. Separate structural protection from execution, growth runway and
197|industry conditions; corroborate decisive claims beyond management's assertion.
198|
199|| Mechanism | Present / Absent / Unknown | Answer / evidence | Contrary evidence | Confidence |
200||:--|:--|:--|:--|:--|
201|| Switching costs | | | | |
202|| Network effects | | | | |
203|| Brand, patents or licenses | | | | |
204|| Structural cost advantage | | | | |
205|| Efficient scale | | | | |
206|| Scale economies shared | | | | |
207|
208|**Summary:** Identify the supported competitive defense, or explain why none
209|is established. Connect the mechanism to customer behavior and distinguish
210|observed protection from an attractive but unverified story.
211|
212|| Force / question | Pressure | Evidence-based answer | Confidence |
213||:--|:--|:--|:--|
214|| Rivalry: can rivals compete away profit through price or capacity? | | | |
215|| Entry: what prevents a funded newcomer from winning customers? | | | |
216|| Suppliers: can essential providers capture the margin? | | | |
217|| Buyers: can concentrated or price-sensitive customers force concessions? | | | |
218|| Substitutes: can another solution meet the need more cheaply or better? | | | |
219|
220|**Summary:** Identify the strongest pressure on industry profits and whether
221|the company's defense offsets it. Explain which competitor, supplier, customer
222|or substitute could capture the economic benefit.
223|
224|| Protection /5 | Economics /5 | Durability /5 | Trend /5 | Class / trend | Confidence | Decisive evidence / limitation | Threat / reassessment trigger |
225||--:|--:|--:|--:|:--|:--|:--|:--|
226|| | | | | | | | |
227|
228|**Summary:** Explain the moat classification and trend using the decisive
229|economic evidence. State the principal threat, confidence limit and observable
230|change that would warrant reassessment.
231|
232|Use the framework's classification and early-conclusion rules. Do not add an
233|overall average or let a low share price improve the moat assessment.
234|
235|### 4. Financial Health
236|
237|Report heading: `## Financial Health`.
238|Apply `frameworks/financial-health.md`. State the review period and summarize
239|what the historical statements, normalization, cash/claims reconciliation and
240|dated liquidity stress imply. Keep full schedules and intermediate arithmetic
241|in working records, not extra report tables by default. The assessment table
242|must show the decisive results, including the first shortfall or credible headroom.
243|Use sector-appropriate capital and funding analysis where corporate ratios
244|would mislead. Do not treat unavailable data as zero or a diagnostic cash
245|subtotal as automatically distributable owner cash.
246|
247|| Area | Key measure / trend | Assessment | Confidence | Main vulnerability / trigger |
248||:--|:--|:--|:--|:--|
249|| Earnings reliability | | | | |
250|| Cash generation and conversion | | | | |
251|| Debt and solvency | | | | |
252|| Liquidity under stress | | | | |
253|| Growth and reinvestment returns | | | | |
254|| **Overall** | **First stress shortfall, or headroom** | **Framework verdict** | | |
255|
256|**Summary:** Explain whether earning power is reliable and obligations remain
257|fundable under the stated stress. Connect cash conversion, reinvestment and
258|claims to the overall verdict; identify the principal vulnerability rather
259|than repeat every ratio.
260|
261|Follow the framework's early-conclusion option when decisive weakness or
262|uncertainty makes other work unnecessary; identify the gaps in Overall.
263|Do not average away a survival problem.
264|
265|### 5. Valuation
266|
267|Report heading: `## Valuation`.
268|Use `frameworks/simple-dcf.md` only when applicable; otherwise use the selected
269|alternative in `frameworks/sector-metrics.md`. State the valuation date, method,
270|currency/units, normalized starting basis, claimholders, ownership perimeter,
271|equity adjustments, current share basis and valuation type. Briefly explain the
272|material assumptions and adjustments; verify full calculations in working
273|records rather than reproducing them all here. Value independently before
274|introducing a dated, matching-share market price. Present Base, Bull and Bear
275|cases for the selected method, not only when a simple DCF is applicable.
276|
277|For an applicable simple DCF, show its input line (V0, A, S and optional P),
278|required-return convention and exactly the framework's scenario output below.
279|Keep earnings-proxy, market-multiple-hybrid and cash-DCF labels distinct.
280|
281|| Case | g1 / g2 / X | PV years 1-10 | PV terminal | Value/share (valuation type) | Price at 30% discount | Price at 50% discount |
282||:--|:--|--:|--:|--:|--:|--:|
283|| Base | | | | | | |
284|| Bull | | | | | | |
285|| Bear | | | | | | |
286|
287|**Summary:** Explain what drives the valuation range, which assumptions matter
288|most and how much confidence the cash/claims basis warrants. Keep the valuation
289|type explicit and separate business value from the subsequent price comparison.
290|
291|For an alternative method, replace the DCF table with a compact method-specific
292|Base/Bull/Bear table using the selected sector drivers and common value per
293|share. Briefly explain principal components, attributable ownership and
294|claims/cost adjustments; identify market-priced components. Mark simple DCF
295|Not applicable with its reason; do not force unsuitable inputs into a growth
296|model or substitute three arbitrary multiples for reasoned scenarios.
297|
298|For either route, give confidence, decisive uncertainty, material sensitivities,
299|the useful cross-check and a reassessment trigger. For DCF, summarize the
300|required no-growth check and terminal dependence; keep detailed workings outside
301|the report.
302|Use intrinsic-value and margin-of-safety language only where the method and
303|evidence justify it; a discount to quoted NAV or an earnings proxy is not an
304|established margin of safety. Neither a Bear case nor asset book value is a floor.
305|
306|If conclusion-critical cash, ownership or funding inputs remain unresolved,
307|state **Not calculable**, show the blocker and use N/A for unsupported case values.
308|Any supplementary what-if calculation must remain separately labeled and must
309|not turn a limited report into a completed intrinsic valuation.
310|An alternative-method or Not calculable table also needs its own short summary.
311|
312|### 6. Investment Thesis
313|
314|Report heading: `## Investment Thesis`.
315|Apply `frameworks/investment-thesis.md`. State its research status and confidence
316|on one line, then connect the findings rather than repeat the preceding tables.
317|
318|| Area | Conclusion / decisive evidence | Contrary evidence / limitation | Review trigger / date |
319||:--|:--|:--|:--|
320|| Business / competence | | | |
321|| Source of value / critical assumptions | | | |
322|| Permanent-loss case / protection | | | |
323|| Quality, funding and valuation consistency | | | |
324|| Value versus price / possible mispricing | | | |
325|| **Overall / change since prior review** | | | |
326|
327|**Summary:** Explain the weakest critical assumption and the next observable
328|evidence that would strengthen, weaken or invalidate the thesis. Keep the closing
329|quality-and-price judgment for Final Verdict rather than repeating it here.
330|
331|Keep the strongest contrary case and observable review triggers explicit.
332|Preserve the original thesis and dated changes in the supporting record.
333|Use the framework's supported early-conclusion form where applicable. A research
334|verdict is not an instruction to trade, select a position size or set Suggi's
335|required margin of safety.
336|
337|#### Final Verdict
338|
339|Report subheading: `### Final Verdict`. This closes Investment Thesis immediately
340|before `## Sources`; it is not a seventh framework section. In a brief synthesis,
341|normally 3-5 sentences, combine business economics and moat, management, financial
342|resilience and valuation into a judgment rather than another checklist or score.
343|Include the current price and quote timestamp, Bear/Base/Bull value per share,
344|the Base-case percentage discount or premium, confidence and the decisive risk
345|or reassessment trigger. Reuse the researched values from Valuation, on the same
346|share class, currency, ADR/FX and whole-company ownership basis.
347|
348|Use the discount-to-value convention in `frameworks/simple-dcf.md`: the positive
349|Base value, not market price, is the percentage denominator. State a discount as
350|"X% below Base estimated intrinsic value" and a premium as "X% above"; distinguish
351|this from upside/downside measured against purchase price. Judge undervalued,
352|approximately fairly valued or overvalued relative to that stated basis, without
353|presenting an uncertain estimate as fact or a discount as guaranteed protection.
354|For a proxy or quoted NAV retain that label, not intrinsic-value/MoS language.
355|If value is unsupported, the price is stale/missing, the bases do not match or
356|Base value is zero, show the affected comparison N/A and the reason. A partial
357|business valuation cannot establish whole-stock under/overvaluation. Do not
358|manufacture numbers to fill the closing section.
359|
360|**Supported-valuation wording example -- synthetic assumed inputs, not research:**
361|
362|"The business has durable customer economics, adequate management and funding
363|that survives the modeled stress. At the assumed USD80 ordinary-share quote as
364|of <verified quote timestamp>, Bear/Base/Bull estimated intrinsic values of
365|USD70/100/130 imply a 20% discount to Base, although the price is above Bear.
366|My judgment is undervalued relative to Base, with Medium confidence; the apparent
367|discount must be weighed against the downside case. Sustained cash-conversion
368|deterioration would invalidate the thesis."
369|
370|## Sources and Supporting References
371|
372|Report heading: `## Sources`.
373|Use one combined numbered list. Cite claims with `[1]` or `[1][3]`, without
374|outer parentheses or automatic Markdown footnotes. Every number must resolve
375|to the inspected source supporting that claim, including filing date and page,
376|note, table or section where useful.
377|
378|For external sources, give institution/author, date if known, title, direct URL
379|and authority rating: `[high]`, `[medium]` or `[low]`. Favor issuer filings and
380|regulator originals for financial facts; independent evidence matters for
381|load-bearing competitive or conduct claims. Authority does not establish
382|neutrality, and repeated versions of one origin are not corroboration.
383|For repository sources use `repo:path -- brief relevance` across repositories,
384|or a repository-root path within Investing Hub. Preserve a specific revision
385|when the claim depends on it. Do not invent publication dates.
386|
387|Link supporting records in the relevant framework section: statement history,
388|source ledger, valuation model and dated reassessment evidence as applicable.
389|Link only records that exist; do not create empty companion files to satisfy
390|the format. An optional final `## See Also` may link related company or industry
391|research, explaining each connection. Do not add unrelated links to meet a quota.
392|
393|## Example -- Abbreviated Company Report
394|
395|This fictional example illustrates the minimum writing pattern: frontmatter,
396|identity, six framework sections, tables with summaries beneath each, a closing
397|Final Verdict within Investment Thesis, and sources. The business observations are illustrative assumptions, not claims
398|about a real company. Source entries and angle-bracket fields are placeholders
399|to replace with verified evidence; this is not a publishable research result.
400|The example uses a limited, Not calculable conclusion rather than inventing a
401|valuation. A completed valuation populates Base/Bull/Bear using the selected
402|method; the synthetic wording example above illustrates a supported comparison.
403|
404|```markdown
405|---
406|name: example-components-company-research
407|id: <generated-UTC-creation-id>
408|tier: company-research
409|author: <original-author>
410|ticker: <exact-ticker>
411|exchange: <exchange>
412|review_date: <YYYY-MM-DD>
413|data_cutoff: <YYYY-MM-DDTHH:MM:SSZ>
414|reporting_currency: <currency-code>
415|tags: [industrials, replacement-components]
416|links:
417|  - governance/template-company.md
418|---
419|
420|# Example Components -- Repeat Orders Do Not Yet Establish Owner Value
421|
422|Example Components is a fictional supplier of replacement parts for industrial
423|equipment. In this illustrative case, repeat orders suggest customer dependence,
424|but incomplete cash and ownership evidence prevents an intrinsic valuation.
425|
426|**Thesis status:** Investigate. **Confidence:** Low. **Valuation status:** Not calculable.
427|
428|**Identity and basis:** <legal entity>; <ticker/exchange/share class>; <ADR ratio
429|or not applicable>; <review date and reviewer>; <information cutoff>; <accounting
430|standard and consolidation perimeter>; <fiscal year-end>; <currency/units>.
431|**History covered:** <annual and interim periods inspected; missing periods>.
432|
433|## Business and Method
434|
435|**Coverage: Limited** -- customer economics are described, but normalized owner
436|cash remains unresolved.
437|
438|| Question | Assessment / evidence |
439||:--|:--|
440|| Who pays, for what, and why do customers return? | Industrial operators buy replacement parts to keep installed equipment running.[1] |
441|| Segments, geography and principal competitors | One replacement-parts segment; competitors and geographic exposure require fuller comparison.[1][3] |
442|| Main revenue, margin and cash-generation drivers | Installed equipment, replacement frequency, pricing and inventory requirements.[1] |
443|| Capital required and who bears financing risk | The supplier funds tooling and inventory before collecting from customers.[1] |
444|| Sector-specific measures and historical comparison | Repeat orders, cash after investment and working-capital trends matter; through-cycle evidence is incomplete.[1] |
445|| Circle of competence and decisive limitations | The replacement model is understandable; tooling replacement cost is not yet established.[1] |
446|| Principal valuation method / useful cross-check | Normalized equity cash valuation if the cash bridge can be built; asset recoverability as a separate cross-check. |
447|
448|**Summary:** Demand depends on maintaining installed equipment, not only on
449|sales of new machines. Repeat purchasing may support resilience, but inventory
450|and tooling still tie up owner capital. The key missing input is the investment
451|needed to preserve earning power, not another revenue-growth forecast.
452|
453|## Management
454|
455|**Coverage: Limited** -- capital-allocation and ownership evidence is incomplete.
456|**Decision-makers:** <CEO and capital allocator, tenure and controlling owners>.
457|
458|| Statement date / original commitment | Metric, scope / target horizon | Actual year 1 / 2 / 3 | Delivery pattern / explanation |
459||:--|:--|:--|:--|
460|| <date>: expand service capacity | <original operating target and deadline> | Delivered / later years not applicable | Operating commitment broadly matched; economic return remains unproven.[2] |
461|| <date>: reduce inventory | <original inventory measure and deadline> | Missed / revised / not yet due | A missed target was disclosed; original and revised baselines remain separate.[2] |
462|| <date>: return surplus capital | <original distribution commitment and horizon> | Partial / not yet due / not yet due | Distributions occurred, but whether the cash was surplus is unresolved.[2] |
463|
464|**Summary:** The illustrative record is mixed rather than uniformly strong or
465|weak. Disclosing the inventory miss is relevant to candor, but does not repair
466|the operating result. The distribution commitment cannot be judged without
467|knowing the capital the business needed to retain.
468|
469|| Category | Answers / decisive fact | Score /5 | Confidence | Concern / reassessment trigger |
470||:--|:--|--:|:--|:--|
471|| Integrity and candor | A missed commitment was acknowledged; the wider conduct record is incomplete.[2] | N/A | Low | Check treatment of recurring adjustments and setbacks. |
472|| Capital allocation | Expansion and distributions compete for cash; returns are not established.[1][2] | N/A | Low | Reconcile investment outcomes and funding. |
473|| Ownership and incentives | Current award claims and economic exposure remain unclear.[2] | N/A | Low | Reconcile ownership, compensation and dilution. |
474|| Execution and adaptability | Service expansion was delivered, while inventory performance lagged.[2] | N/A | Low | Test whether the inventory problem persists. |
475|| Governance and minority treatment | Board challenge and related-party safeguards require evidence.[2] | N/A | Low | Resolve material minority-owner questions. |
476|| **Overall** | **INVESTIGATE: conclusion-critical allocation and ownership gaps.** | N/A | Low | Complete the cash deployment and claims review. |
477|
478|**Summary:** An operating success is not enough to establish strong stewardship.
479|The missing allocation and ownership evidence prevents a meaningful overall
480|score. This is an incomplete assessment, not an allegation of dishonesty.
481|
482|## Moat
483|
484|**Coverage: Limited** -- a possible customer defense is visible, but economic
485|proof and its durability remain incomplete.
486|
487|| Mechanism | Present / Absent / Unknown | Answer / evidence | Contrary evidence | Confidence |
488||:--|:--|:--|:--|:--|
489|| Switching costs | Unknown | Qualification and downtime may discourage supplier changes.[3] | Large customers can qualify alternatives. | Low |
490|| Network effects | Absent | More buyers do not directly improve the product for other buyers in this case.[3] | Shared service coverage would need a separate test. | Low |
491|| Brand, patents or licenses | Unknown | Reliability may matter more than brand recognition.[3] | No protected pricing advantage is established. | Low |
492|| Structural cost advantage | Unknown | Installed tooling may support efficient production.[1] | Competitor unit costs are unavailable. | Low |
493|| Efficient scale | Unknown | Niche demand may constrain entrants.[3] | No market-capacity evidence establishes this. | Low |
494|| Scale economies shared | Unknown | Customer savings have not been demonstrated.[1][3] | Lower prices alone would not establish the loop. | Low |
495|
496|**Summary:** Qualification and downtime are the most plausible sources of
497|customer attachment in this case. They are hypotheses to test, not proven
498|switching costs. Repeat orders alone cannot show that customers lack attractive
499|alternatives or that the supplier captures excess returns.
500|
501|| Force / question | Pressure | Evidence-based answer | Confidence |
502||:--|:--|:--|:--|
503|| Rivalry: can rivals compete away profit through price or capacity? | Medium | Qualified competitors can bid for replacement contracts.[3] | Low |
504|| Entry: what prevents a funded newcomer from winning customers? | Unknown | Qualification may delay entry, but the delay is unmeasured.[3] | Low |
505|| Suppliers: can essential providers capture the margin? | Unknown | Specialized inputs may restrict sourcing options.[1] | Low |
506|| Buyers: can concentrated or price-sensitive customers force concessions? | High | Large industrial buyers can negotiate across multiple plants.[3] | Low |
507|| Substitutes: can another solution meet the need more cheaply or better? | Unknown | Redesign or third-party servicing could reduce part demand.[3] | Low |
508|
509|**Summary:** Buyer bargaining power is the clearest pressure in the illustrative
510|case. Customer dependence on a part does not mean dependence on one supplier.
511|The analysis needs evidence that qualification barriers protect the supplier's
512|economics rather than merely slow procurement.
513|
514|| Protection /5 | Economics /5 | Durability /5 | Trend /5 | Class / trend | Confidence | Decisive evidence / limitation | Threat / reassessment trigger |
515||--:|--:|--:|--:|:--|:--|:--|:--|
516|| N/A | N/A | N/A | N/A | Unclear / Unknown | Low | Customer attachment is plausible; returns after necessary investment are unproven. | Lost qualifications, pricing concessions or evidence of durable excess returns. |
517|
518|**Summary:** The moat remains Unclear because neither economic proof nor
519|durability has been established. That differs from a supported finding of no
520|moat. Evidence on customer alternatives and returns after reinvestment could
521|change the classification in either direction.
522|
523|## Financial Health
524|
525|**Coverage: Limited** -- normalized owner cash and usable stressed liquidity
526|are unresolved. **Supporting records:** <verified statement and bridge links>.
527|
528|| Area | Key measure / trend | Assessment | Confidence | Main vulnerability / trigger |
529||:--|:--|:--|:--|:--|
530|| Earnings reliability | Exceptional and recurring costs still need reconciliation.[1] | Unknown | Low | Adjusted profit may omit ongoing costs. |
531|| Cash generation and conversion | Inventory and tooling consume cash; sustaining needs remain uncertain.[1] | Unknown | Low | Weak collections or replacement spending. |
532|| Debt and solvency | Claims and accessible cash are not fully reconciled.[1] | Unknown | Low | Undisclosed restrictions or obligations. |
533|| Liquidity under stress | No defensible dated headroom figure is available.[1] | Unknown | Low | Maturities before usable funding arrives. |
534|| Growth and reinvestment returns | Added capacity has not yet demonstrated owner returns.[1] | Unknown | Low | Growth absorbs cash without earning its cost. |
535|| **Overall** | **Stress headroom not established.** | **Unclear** | Low | Complete the cash, claims and dated funding bridges. |
536|
537|**Summary:** Reported profitability does not yet establish financial resilience.
538|Working capital and replacement investment could consume much of the apparent
539|earning power. Without a dated funding bridge, the report cannot claim that the
540|company would survive the chosen stress without new financing.
541|
542|## Valuation
543|
544|**Coverage: Limited.** Simple DCF is not calculable until the cash/claims basis
545|is resolved. **Basis:** <valuation date, currency/units, equity perimeter and
546|current share basis>; no price comparison is made before a defensible value.
547|
548|| Case | Valuation status / missing basis | Value/share | Price comparison |
549||:--|:--|--:|:--|
550|| Base | Not calculable: normalized owner cash, reinvestment and equity claims.[1][2] | N/A | N/A |
551|| Bull | Same missing basis; optimistic growth cannot repair the cash/claims gap. | N/A | N/A |
552|| Bear | Same missing basis; no supported downside value or floor. | N/A | N/A |
553|
554|**Summary:** The missing economic inputs prevent an intrinsic-value conclusion,
555|not merely a more precise estimate. Substituting reported profit would change
556|the result into an earnings proxy rather than solve the problem. The next step
557|is to resolve the cash and ownership bridges, not apply a larger discount to an
558|unsupported number.
559|
560|## Investment Thesis
561|
562|**Coverage: Limited. Thesis status: Investigate. Confidence: Low.**
563|
564|| Area | Conclusion / decisive evidence | Contrary evidence / limitation | Review trigger / date |
565||:--|:--|:--|:--|
566|| Business / competence | Replacement demand is understandable.[1] | Sustaining tooling economics remain unclear. | Obtain replacement-cost evidence. |
567|| Source of value / critical assumptions | Repeat orders may support durable earning power.[1][3] | Customer bargaining and reinvestment may absorb the benefit. | Verify returns after necessary investment. |
568|| Permanent-loss case / protection | Cash absorption combined with obligations could damage owners.[1] | Usable funding and recoverable asset values are not established. | Complete the dated stress case. |
569|| Quality, funding and valuation consistency | No completed valuation is claimed. | Plausible customer attachment cannot fill the cash gap. | Reconcile the decisive inputs together. |
570|| Value versus price / possible mispricing | N/A until value is supportable. | An apparently low multiple would not establish a bargain. | Compare only after independent valuation. |
571|| **Overall / change since prior review** | **Investigate; initial assessment.** | **Cash, ownership and durability remain unresolved.** | **Review at the next relevant filing or earlier decisive disclosure.** |
572|
573|**Summary:** Customers or reinvestment may capture the benefit of repeat demand.
574|The next decisive evidence is owner cash after necessary investment and stressed
575|funding, not a share-price movement alone.
576|
577|### Final Verdict
578|
579|The replacement business is understandable, but durable excess returns and
580|management's allocation record remain unproven.[1][2][3]
581|Unresolved cash requirements and stressed funding prevent a supported investment
582|case, so my judgment is **Investigate, Low confidence**.[1][2]
583|Current price is **N/A (no verified quote in this illustration)**;
584|**Bear/Base/Bull intrinsic values and discount/premium are N/A** because the
585|cash and ownership basis is unresolved; no under/overvaluation is established.
586|Reassess when the necessary investment and claims can be reconciled.
587|
588|## Sources
589|
590|These are source-format placeholders for the fictional example, not citations
591|to real evidence. Replace each with the inspected document and appropriate
592|authority rating before using this format for a real company.
593|
594|1. <Issuer>. <Date>. "<Annual/interim report title>." <Direct URL and relevant pages/notes>. <Authority rating>.
595|2. <Issuer or regulator>. <Date>. "<Ownership, compensation and original-commitment disclosures>." <Direct URLs and sections>. <Authority rating>.
596|3. <Independent customer, competitor or industry source>. <Date>. "<Title>." <Direct URL and relevant section>. <Authority rating>.
597|```
```

## Contract snapshot: /srv/investing/investing-hub/frameworks/simple-management.md

SHA-256: 73c7db5c4afaf474b463efdf4cab263e3445bb2ae4b7f8c42669b0a5660aa3de

```text
1|---
2|name: simple-management
3|id: 20260908T141444Z
4|tier: framework
5|domain: value-investing
6|author: Neo
7|tags: [management, capital-allocation]
8|---
9|
10|# Simple Management Analysis
11|
12|## 1. Establish who controls the decisions
13|
14|Record company, date, chief executive, principal capital allocator, tenure and controlling shareholders, with their voting power beside their economic interest. Review 5-10 years of annual reports, ownership/pay disclosures and capital decisions where available. Separate the current team's record from predecessors, acquisitions and favorable industry conditions.
15|
16|Read recent communications and a difficult period where available. Corroborate decisive claims against financial results, regulatory records and independent reporting. Identify source origins; a filing and articles repeating it are not independent observations. Record unavailable history rather than filling it with reputation or charisma.
17|
18|## 2. Apply the integrity test first
19|
20|Check intentional accounting misrepresentation, concealment of liabilities, self-dealing, misleading guidance, recurring charges presented as exceptional, abusive compensation and treatment of minority owners. Distinguish proven misconduct, unresolved allegations and ordinary business mistakes.
21|
22|**Established serious dishonesty or abuse of owners: AVOID**, regardless of other scores. **Unresolved material reliability concern: INVESTIGATE**, with overall score N/A. A lack of discovered misconduct is not proof of integrity. Do not reduce the decision to a count of red flags.
23|
24|## 3. Answer the management questionnaire
25|
26|Answer every question with a dated action or disclosure. Record one counterexample or limitation per category, even for an admired manager.
27|
28|| Category | Questions that MUST be answered |
29||:--|:--|
30|| Integrity and candor | Are reported and adjusted results reconciled consistently? Are failures explained and responsibility accepted? Is communication candid during setbacks? Who benefits or bears material harm, and is management's conduct defensible beyond its own stated principles? |
31|| Capital allocation | Where did retained cash go, and what return followed? Is spending driven by returns, or by available cash and imitation of peers? Did major acquisitions justify their full cost, including issued shares and assumed debt? Were buybacks below defensible intrinsic value while liquidity remained adequate? Does management stop poor projects and return surplus capital when reinvestment is unattractive? |
32|| Ownership and incentives | What economic stake do managers hold, how was it acquired, and is it hedged or pledged? Do pay targets reward durable per-share results and capital efficiency, or merely size and adjusted earnings? What dilution, vesting and downside exposure do owners actually bear? |
33|| Execution and adaptability | Which commitments were delivered, delayed or abandoned? Do talent retention/delegation, product or service renewal and cost/accounting controls sustain performance? Can the team learn, simplify and stop defending sunk costs? Does succession reduce dependence on one individual? |
34|| Governance and minority treatment | Can the board challenge management and review conflicts? Do controlling owners receive preferential deals? Are capital raising, voting rights and related-party transactions fair to outside shareholders? Are oversight and succession credible in practice, not just on paper? |
35|
36|## 4. Check the record behind the answers
37|
38|- Summarize cash used for reinvestment, acquisitions, debt reduction, dividends and repurchases over the review period. Reconcile material funding from operations, cash reserves, borrowing and issuance; do not imply all deployment came from free cash flow.
39|- Apply the one-dollar test: over five years or more, each retained dollar should create at least one dollar of value for owners, which requires incremental returns at or above those available elsewhere. Compare returns on new investment with its cost and reasonable alternatives. Where measurable, calculate multi-year incremental after-tax operating profit divided by the corresponding increase in invested capital. Mark the ratio not meaningful when the denominator is negative, tiny or distorted; examine actual project or acquisition outcomes instead.
40|- Review the largest completed acquisitions: price, financing, original rationale, subsequent cash results and impairments. No acquisitions means that sub-question is not applicable, not poor management. No impairment does not prove a good deal.
41|- Reconcile dated opening and closing actual common shares through repurchases, issuance and other changes on a consistent split basis. Reconcile existing potential dilution separately; do not infer net share retirement from weighted-average EPS denominators. Stock-based compensation is a real owner cost; subtracting compensation expense from repurchase dollars does not measure net share retirement. Do not reward debt-funded earnings-per-share growth without checking financial risk.
42|- Compare at least three material forward-looking statements or capital commitments with outcomes, including a setback if available. Preserve the original statement date, metric, scope, assumptions and target horizon; show revisions separately rather than moving the original baseline. Compare actual results in the following year and years two and three when available on the same basis. Record unavailable or not-yet-due outcomes, not guessed results. Where formal guidance is absent, use stated strategic commitments.
43|- Classify each comparison as overpromised/underperformed, broadly matched, underpromised/outperformed, not yet due or not comparable. Explain management-controlled execution versus external shocks, scope changes and predecessor decisions; a miss is not itself dishonesty and favorable markets are not managerial skill. Judge candor about revisions as well as delivery. Do not reward systematic lowball guidance or penalize a sensible refusal to forecast quarters. Use this evidence within integrity and execution, not as an extra category or duplicate score.
44|- For operating capability, record a material operating outcome and a limitation, not just transactions or financial targets. Use measures suited to the business; do not impose R&D criteria on every company.
45|- Put ownership percentage beside its value and compensation context. Do not assume personal net worth, score founders automatically highest, or infer dishonesty from a share sale alone.
46|
47|## 5. Score, challenge and classify
48|
49|Use a 1-5 house rubric: **1** repeated harmful behavior; **2** material weaknesses; **3** adequate, mixed but broadly rational behavior; **4** strong, demonstrated stewardship; **5** exceptional, sustained stewardship through difficult conditions. Score outcomes and decisions, not eloquence or share-price performance alone.
50|
51|Apply overrides in order: established serious dishonesty/owner abuse gives **AVOID**; otherwise an established continuing, material pattern of destructive allocation, reckless financing or disabling operational/control failure gives **Weak - critical stewardship failure**; otherwise unresolved conclusion-critical evidence or contradictions give **INVESTIGATE**. Use overall score N/A for overrides; an established adverse finding may stand despite unrelated gaps. Distinguish isolated mistakes from a critical pattern and review every category rated 1 or 2 for that pattern.
52|
53|Otherwise calculate the arithmetic mean of all category scores, rounded to one decimal, as a coarse descriptive index. Missing material evidence makes overall N/A; a genuinely inapplicable sub-question does not. Do not reweight around an inconvenient gap.
54|
55|Without an override, classify the unrounded mean: **Strong >= 4; Adequate >= 3 and < 4; Weak < 3**. These describe stewardship, not whether the stock is cheap. Never report a favorable mean alongside an overriding critical failure.
56|
57|Assign **High / Medium / Low** confidence: corroborated multi-year evidence / partial evidence / sparse or conflicting evidence. A score of 4 or 5 MUST have primary support. Overall confidence cannot exceed the weakest conclusion-critical premise. Ask what future behavior would invalidate the view; high-confidence adverse findings are allowed.
58|
59|For a full assessment, **PASS** requires integrity and critical-stewardship checks, answered questions, reconciled capital/shares, dated say-do evidence and checked scoring. An evidenced AVOID, INVESTIGATE or critical-failure conclusion may finish early with its reason and unassessed work N/A. **HALT** unsupported ratings or an average hiding a decisive concern, not a defensible negative or uncertain report.
60|
61|## Finished output
62|
63|Give company/date and decision-maker/tenure on one line. Fill rows with short answers, a decisive fact and a concern; identify evidence by filing/date/page or resolving link. For an early conclusion return only Overall, with dated evidence, the override and missing work explicit. End each table at its last row and follow it with a **Summary:** of 3-5 sentences, fewer when sufficient: the conclusion, why it matters and what would change it. No biography or essay.
64|
65|For a full assessment, show the compact say-do record before the scorecard:
66|
67|| Statement date / original commitment | Metric, scope / target horizon | Actual year 1 / 2 / 3 | Delivery pattern / explanation |
68||:--|:--|:--|:--|
69|| | | | |
70|
71|| Category | Answers / decisive fact | Score /5 | Confidence | Concern / reassessment trigger |
72||:--|:--|--:|:--|:--|
73|| Integrity and candor | | | | |
74|| Capital allocation | | | | |
75|| Ownership and incentives | | | | |
76|| Execution and adaptability | | | | |
77|| Governance and minority treatment | | | | |
78|| **Overall** | **Strong / Adequate / Weak / INVESTIGATE / AVOID / N/A** | | | |
```

## Contract snapshot: /srv/investing/investing-hub/frameworks/simple-dcf.md

SHA-256: bf1467f8d099ab161625e9f44b469899c049a9732115bcdf4d7024f28f0acffa

```text
1|---
2|name: simple-dcf
3|id: 20260908T111736Z
4|tier: framework
5|domain: value-investing
6|author: Neo
7|tags: [dcf, valuation, cash-flow, scenarios]
8|---
9|
10|# Simple DCF - Fixed 10% Discount Rate
11|
12|## 1. Fix the basis
13|
14|Record company, valuation date, currency, units, selected metric, historical period and whether the supplied amounts belong to the business or common shareholders. Review 5-10 years of the supplied metric, including a weak period; identify changes that make the starting year unrepresentative.
15|
16|Keep the discount rate at **10% in every year and case**, including sensitivities. Use nominal cash/earnings and growth in the stated valuation currency. Treat 10% as the required-return convention, not measured financing cost or a guarantee that enterprise and equity approaches give the same value. Year 1 is the next twelve months from the valuation date; rebase fiscal-period inputs accordingly. Discount each annual amount at period-end and terminal value immediately after the year-10 distribution.
17|
18|Receive metric selection, normalization and cash-conversion adjustments as inputs; do not decide them here. Growth MUST NOT count the same money as both distributed and reinvested. Check that the supplied cash conversion remains consistent with forecast investment, not just the starting year.
19|
20|Use this model only when a positive two-stage path represents the annual benefits. Known zero/negative years, expiry before year 10, abrupt shutdowns or uneven funding needs require a dated cash-flow schedule or another method. Do not normalize these events away; X = 0 does not remove post-expiry forecast cash.
21|
22|## 2. Assemble the inputs
23|
24|| Input | Required entry |
25||:--|:--|
26|| V0 | Positive, supplied normalized annual run-rate at the valuation date; a total amount, not a per-share amount. |
27|| g1 | Annual growth for years 1-5, entered as a decimal greater than -1. |
28|| g2 | Annual growth for years 6-10, entered as a decimal greater than -1. |
29|| X | Non-negative exit multiple of the same year-10 metric. |
30|| A | Supplied signed total adjustment to common equity at the valuation date; same currency and scale as V0. |
31|| S | Positive current common share count, or explicitly reconciled diluted-equivalent count. Match the numerical scale: monetary millions with shares in millions. |
32|| P | Share price and timestamp, only if comparing value with price. |
33|
34|Attach a filing/date/page or assumption label to every input. Convert per-share inputs to totals before calculation. Itemize A; include cash, debt, leases, preferred/minority claims and non-operating assets only as the supplied basis requires. Do not automatically subtract debt from an equity-basis model.
35|
36|Use one method for existing noncommon equity claims: deduct their supplied economic value in A and use basic common shares; or use a justified diluted-equivalent S with exercise proceeds and A reconciled. Never apply both to the same claim. Separate existing awards from future compensation already charged in the forecast; do not charge the same future grants again through dilution or replacement buybacks. Check share classes, vesting and expense timing; an earnings-per-share weighted-average denominator is not automatically today's S.
37|
38|## 3. Set Base, Bull and Bear
39|
40|Assign g1, g2 and X independently to each case:
41|
42|- **Base:** a defensible central path from normalized performance, not management's target by default.
43|- **Bull:** better demand, execution or durability that can plausibly occur together; no stacked best-ever assumptions.
44|- **Bear:** a credible setback, competitive erosion or slower recovery; allow negative growth where justified.
45|
46|Give each case one sentence explaining growth and X. Check market size, competition and supplied reinvestment; justify acceleration in years 6-10. Support X with continuing cash conversion, reinvestment, growth and durability. Identify fundamental versus market-derived X; do not automatically copy today's multiple or a historical peak.
47|
48|Keep V0, A and S common unless a documented scenario-specific adjustment is supplied. Check subsequent financing, acquisitions and share issuance before calling the valuation current. Do not create a probability-weighted value to conceal downside.
49|
50|## 4. Calculate each case
51|
52|Here t is the forecast year, from 1 to 10; PV means present value; ^ means exponentiation.
53|
54|```text
55|Years 1-5:  V_t = V0 * (1 + g1)^t
56|Years 6-10: V_t = V0 * (1 + g1)^5 * (1 + g2)^(t - 5)
57|
58|PV of year t    = V_t / 1.10^t
59|PV of years 1-10 = SUM(PV of each of the ten years)
60|Terminal value  = V_10 * X
61|PV of terminal  = Terminal value / 1.10^10
62|
63|Equity value = PV of years 1-10 + PV of terminal + A
64|Modeled value/share = MAX(0, Equity value) / S
65|```
66|
67|Calculate with full precision; round only displayed results. Keep the unrounded equity value visible if it is negative, even though the displayed common-share value is floored at zero.
68|
69|For a positive modeled value: `price at 30% discount = value/share * 0.70`; `price at 50% discount = value/share * 0.50`. If P is supplied, `discount to modeled value = 1 - P / value/share`; mark it N/A at zero value. Apply the valuation-type labels below; these comparisons are not trade instructions.
70|
71|## 5. Challenge and verify
72|
73|- Recalculate Base with g1 and g2 both zero, holding X, A and S fixed. Treat this as a no-growth sensitivity, not liquidation value or a guaranteed floor.
74|- Reduce Base X and growth separately over plausible ranges; record each input change and its value effect before naming the dominant sensitivity. Keep 10% fixed. Flag dependence on generous exit assumptions.
75|- If X represents a perpetuity of the same distributable cash with no payout change, check implied continuing growth: `gT = (0.10 * X - 1) / (X + 1)`. Assess its plausibility; do not apply this identity to earnings, EBITDA or finite-life assets. Zero growth in years 1-10 does not establish zero growth afterward.
76|- Calculate terminal dependence as `PV terminal / (PV years 1-10 + PV terminal)`; do not include A in that denominator or force a target percentage.
77|- Where normalized earnings E and the reinvestment I funding growth are known, check the implied return on new capital: `r = g / (I / E)`. Below 10%, faster growth lowers value; challenge any case whose growth depends on it.
78|- Before release, MUST verify finite inputs, basis, units, financing date, all ten annual discounts, year-10 terminal discount, and single application of A. Verify `Bear <= Base <= Bull`; investigate reversed ordering rather than relabeling rows. A second calculation MUST reproduce the results.
79|
80|**PASS:** applicable cash/claim identities and arithmetic reconcile, assumptions are traceable and limitations reach the final labels. **HALT** missing inputs, inconsistent claims, an unrepresentable path or unsupported valuation claims. Unsupported cash conversion blocks a cash-DCF claim, not an explicitly labeled earnings proxy. Bear is a scenario, never a downside floor.
81|
82|## Finished output
83|
84|Give one input line: company/date, currency, metric/claimholder basis, V0, A, S, optional P and valuation type. Select the type in this order:
85|
86|- **Earnings proxy:** earnings not reconciled to distributable cash; disclose any market-derived X too.
87|- **Market-multiple hybrid:** cash reconciled, but X is market-derived.
88|- **Cash DCF:** cash reconciled and terminal assumptions supported by fundamentals. Only this type may call value/share **intrinsic value** and the discounts **margin of safety**.
89|
90|Give one confidence line: High / Medium / Low, decisive uncertainty, sensitivity and reassessment trigger. Confidence cannot exceed support for the weakest conclusion-critical assumption; repeated versions of one claim are not independent evidence. If case types differ, identify the type in each value cell. Keep proxy/hybrid labels; do not rename their markdowns MoS. Use exactly these three rows for a completed calculation; otherwise return Not calculable / Not applicable and the blocker, with values N/A. Follow the table with a **Summary:** of 3-5 sentences, fewer when sufficient: what drives the range, the decisive assumption and what would change it.
91|
92|| Case | g1 / g2 / X | PV years 1-10 | PV terminal | Value/share (type above) | Price at 30% discount | Price at 50% discount |
93||:--|:--|--:|--:|--:|--:|--:|
94|| Base | | | | | | |
95|| Bull | | | | | | |
96|| Bear | | | | | | |
```

## Contract snapshot: /srv/investing/investing-hub/frameworks/financial-health.md

SHA-256: 6c34a68f8b2884998f1836cc10f27953ca9cfbdbdc5c16f4bcd0e16c3d4c40ca

```text
1|---
2|name: financial-health
3|id: 20260908T144122Z
4|tier: framework
5|domain: value-investing
6|author: Neo
7|tags: [financial-health, solvency]
8|---
9|
10|# Financial Health Analysis
11|
12|## 1. Establish the reporting basis
13|
14|Record company, date, currency, accounting standard and consolidation perimeter. Assemble five years and the latest interim period; extend through a full cycle where necessary. Reconcile income statement, balance sheet and cash-flow statement to filings. Separate acquisitions, disposals and accounting changes from organic performance.
15|
16|For banks and insurers, use regulatory capital, asset quality and funding analysis instead of mechanically applying corporate debt/EBITDA or cash-conversion ratios. Identify restrictions on cash transfers between subsidiaries and the parent. Missing information is Unknown; a negative or near-zero denominator is not meaningful, not a favorable ratio.
17|
18|## 2. Normalize earning power
19|
20|Build a working bridge from reported to normalized earnings. List each adjustment, sign, tax effect and reason. Remove exceptional gains as consistently as exceptional losses. Keep recurring restructuring, customer acquisition, research and compensation costs. Investigate repeated changes to adjusted-metric definitions.
21|
22|Keep ongoing stock-based compensation as an owner expense; remove its CFO add-back when constructing owner-economic cash unless an equivalent cost is captured elsewhere. Separate existing award claims from future services, reconciling vesting and expense timing. Count each award cohort once; retaining ongoing expense plus recognizing existing claims is not automatically double counting. Do not charge the same future grants again through dilution or replacement buybacks.
23|
24|For cyclicals, use representative prices, margins and utilization across good and bad conditions. Separate price, volume, mix, currency and acquired growth. Compare earnings growth with diluted per-share growth. Do not normalize away a structural decline or assume every loss reverses.
25|
26|## 3. Test cash quality
27|
28|Calculate and explain the following where economically meaningful. CFO means cash flow from operations; NI means net income; capex means cash purchases of operating fixed assets.
29|
30|| Test | Calculation / investigation |
31||:--|:--|
32|| CFO less cash capex | CFO minus cash capex; a diagnostic, not automatically distributable cash. Locate lease payments, capitalized development and acquisition investment separately. |
33|| Owner earnings | Normalized net income + depreciation, amortization and other noncash charges (keep stock compensation as a cost) - average capex and working capital needed to maintain competitive position and unit volume. Earning power before growth investment; use a range when maintenance is uncertain. |
34|| Cash conversion | Sum of CFO / sum of NI over the same period; repeat using cash after total capex. Use positive, meaningful denominators; explain differences, not universal cutoffs. |
35|| Accruals | (NI - CFO) / average total assets. Investigate persistent growth and the underlying accounts; this is not a fraud verdict. |
36|| Working capital | Receivables and inventory versus sales; payables versus purchasing activity. Calculate receivable days = average receivables / credit sales * period days where credit sales are available. Label total-sales substitutes. |
37|| Cash-cycle trend | Receivable days + inventory days - payable days. Inventory days = average inventory / cost of sales * period days; payable days = average trade payables / purchases * period days. Label cost-of-sales substitutes for purchases; explain seasonality and mix changes. |
38|
39|Trace unusual conversion to customer advances, collections, inventory releases, delayed payments, factoring, supplier finance or capitalized expenses. Distinguish recurring cash generation from temporary working-capital release.
40|
41|Separate total capex from any defensible maintenance estimate. Maintenance must preserve competitive position and productive capacity; it is not automatically depreciation. If uncertain, use a range and retain the total-capex result. CFO already includes working-capital movements: do not subtract them twice. Growth requires funding as well as an attractive earnings forecast.
42|
43|Prepare the valuation cash bridge for the selected claimholders. Enter investment outflows and working-capital increases as deductions; use signed amounts for disposals or releases:
44|
45|| Basis | Working bridge for an ordinary operating business |
46||:--|:--|
47|| FCFF: cash before financing | Normalized after-tax operating profit + depreciation/amortization - net operating investment - increase in noncash operating working capital. |
48|| FCFE: cash to common equity | Normalized earnings attributable to common equity + depreciation/amortization - net operating investment - increase in noncash operating working capital + new borrowing - debt principal repaid. |
49|
50|Net operating investment is measured before depreciation/amortization; "net" deducts only separately identified investment recoveries. Restore any D&A already netted from an investment input before using these bridges. Include gross cash capex, capitalized development and acquisition investment needed for the forecast, without overlap; exclude disposal proceeds already valued separately. Match earnings, taxes, investment and ownership perimeter. Locate interest, preferred distributions and lease payments regardless of statement classification. If leases are financing, include new leased-asset investment and matching lease financing, with principal repayments and claims reconciled; if operating, retain rent and do not deduct the same lease commitment again as debt. Starting from CFO, reconcile to the chosen bridge rather than trusting the subtotal. Retain real recurring costs and future cash obligations; only justified noncash adjustments belong back in cash.
51|
52|Supply a traceable normalized cash amount, its claimholder basis and the investment/financing assumptions supporting each growth case. Reconcile material changes in cash conversion through the forecast. For financial firms, reconcile common earnings to distributable capital after asset growth, loss coverage and required capital retention rather than imposing these operating-company bridges.
53|
54|## 4. Map obligations and test survival
55|
56|List unrestricted cash, genuinely accessible committed funding, gross borrowing, lease obligations, guarantees, pension deficits and material contingent liabilities. Separate fixed/floating rates, currencies, collateral and covenants. Inspect maturities over the next five years, concentrating on the next 12-24 months.
57|
58|Check the notes for a supplier-finance (reverse-factoring) program. Record it as immaterial when there is none, or when the confirmed balance is small beside trade payables, is coverable from usable cash and committed facilities, and program terms stay within customary trade terms (rating agencies commonly treat about 90 days as the upper limit). Where it is material, typically at retailers and distributors (including auto parts), consumer-goods makers and large contractors with long supplier terms, compare program days with customary terms and the company's own history; remove any one-time release from lengthened terms from normalized owner cash; and stress program withdrawal as repayment of the balance beyond customary terms. Do not also deduct the balance as debt while valuing cash after a supplier cost that already prices the credit.
59|
60|For ordinary nonfinancial businesses, calculate net debt = borrowing minus available cash; state the lease convention. Check net debt / normalized EBITDA, operating profit / interest expense, debt / sustainable annual cash generation and current assets / current liabilities where appropriate. EBITDA excludes depreciation and amortization; it is not cash available after asset replacement. Use sector context, covenants and stressed cash needs rather than a universal safe ratio.
61|
62|Build a dated liquidity bridge: opening usable cash + stressed actual cash generated + incremental accessible facility drawings - debt maturities - other mandatory cash uses. Retain minimum operating cash. Track remaining facilities after prior drawings, letters of credit, expiry, collateral and stress restrictions; never reuse the same capacity. Use shorter periods when annual netting hides a shortfall. Do not subtract interest, leases or capex already in cash generation. Noncash owner-cost adjustments are not funding outflows; include actual cash settlements or planned repurchases separately. Do not count uncertain asset sales, new equity or uncommitted refinancing as assured funding.
63|
64|Stress weaker sales and margins, slower collections and higher floating-rate interest together. Use a historical downturn or a stated adverse assumption, not an unlabeled percentage. Test refinancing unavailable. Record the first shortfall, covenant breach or forced dilution and what would prevent it. Maturities above annual cash flow alone do not establish a shortfall if usable cash covers them.
65|
66|## 5. Test the quality of growth
67|
68|For nonfinancial firms, calculate after-tax operating profit / average invested operating capital with consistent treatment of goodwill, leases and non-operating assets. Compare returns with a defensible capital-cost range and peers; do not treat the fixed DCF hurdle as measured financing cost.
69|
70|If expensed long-lived investment materially distorts returns, use a supplementary adjusted view only with a defensible useful life: add its unamortized balance to capital, replace current expense with corresponding amortization, and reconcile reinvestment. Preserve actual cash spending and cash taxes. Otherwise disclose the comparison limit; do not capitalize all research or selling costs by default.
71|
72|Check multi-year incremental after-tax operating profit / increase in invested capital. Mark it not meaningful when acquisitions, impairments, timing or a tiny/negative denominator dominate. Assess whether additional investment increases sustainable per-share earning power without weakening survival.
73|
74|For financial firms, test sustainable returns on equity, loss provisions, asset-liability matching and regulatory-capital headroom. Capital compliance alone does not establish safety. Statistical bankruptcy or manipulation screens are optional: verify model applicability and investigate warnings; never use them as proof of fraud or solvency.
75|
76|## 6. Verify and conclude
77|
78|Before release, MUST check statement and valuation-cash bridges, normalization symmetry, claims, ratio applicability and dated stressed funding. **PASS:** the stated conclusion is supported and limitations are explicit. A documented Fragile or Unclear conclusion may finish with missing work identified; unassessed fields are N/A. **HALT** unsupported positive claims or figures, not the reporting of a decisive weakness or uncertainty.
79|
80|Rate each area **Strong / Adequate / Fragile / Unknown**. Overall: **Fragile** for an established material uncovered obligation, breach or unsustainable claims, even if temporary funding is available; otherwise **Unclear** for missing or conflicting decisive evidence; **Resilient** only with a reliable cash basis, sustainable claims and stressed obligations covered with credible headroom; **Watch** for manageable weaknesses. Never average away a survival risk. Confidence is High for corroborated evidence, Medium for material estimates, Low for unresolved uncertainty, limited by the weakest conclusion-critical premise. Identify sources by filing/date/page or resolving link.
81|
82|## Finished output
83|
84|Give company/date and review period on one line. Return this table; keep each finding and trigger to one sentence. For a decisive early conclusion, return only Overall with its evidence and unassessed gaps. Follow the table with a **Summary:** of 3-5 sentences, fewer when sufficient: the conclusion, why it matters and what would change it.
85|
86|| Area | Key measure / trend | Assessment | Confidence | Main vulnerability / trigger |
87||:--|:--|:--|:--|:--|
88|| Earnings reliability | | | | |
89|| Cash generation and conversion | | | | |
90|| Debt and solvency | | | | |
91|| Liquidity under stress | | | | |
92|| Growth and reinvestment returns | | | | |
93|| **Overall** | **First stress shortfall, or headroom** | **Resilient / Watch / Fragile / Unclear** | | |
```
````

## Appendix E - Exact Reader A R02 Output

SHA-256: `fdfaee5c41a7f76baf051c97c17d0fe293acfb3e74498e18689ed289a0fd1d84`.

````json
{
  "reader": "Official Cold Reader A R02",
  "pack_sha256": "cf918b7e83ef6075381d4c4391ca2f906aec38d8943f294bf83462947f5b70b2",
  "started_utc": "2026-10-01T11:05:21Z",
  "ended_utc": "2026-10-01T11:06:30Z",
  "elapsed_seconds": 69,
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
        "Formula dividends returned JPY1,302.6 billion of JPY1,376.5 billion CFO in FY2022-FY2026.",
        "The one-dollar test passes only on market value: market capitalization rose about JPY2.2 per yen retained since March 2021, derived from reported PER, EPS, and the current price.",
        "The current price is above estimated intrinsic value."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:47,50-53,158-161",
        "/srv/investing/investing-hub/frameworks/simple-management.md:38-39,41,49-59"
      ],
      "required_change": "Replace the unsupported dividend/CFO figures with source-reconciled amounts or remove them. Do not call the mismatched March 2021-to-September 2026 market-capitalization ratio a one-dollar-test pass and do not infer intrinsic value from it. Use the aligned March 2021-to-March 2026 ratios only as qualified market cross-checks, disclose that no clean incremental-capital denominator or contemporaneous opening intrinsic-value estimate is available, and claim no overall retained-earnings pass. Reassess the capital-allocation and Overall scores if they depend on the rejected claims.",
      "unsupported_added_findings": [
        "The stated JPY1,302.6 billion dividend and JPY1,376.5 billion CFO totals are not in the supplied record and conflict with its FY2022-FY2026 dividend total of JPY1,056.933 billion.",
        "A one-dollar-test pass is unsupported because the JPY2.170 market ratio uses mismatched March 2021 and September 2026 endpoints and the record supplies neither a clean incremental-return denominator nor an opening intrinsic-value estimate.",
        "The current-price-above-intrinsic-value finding is unsupported; the supplied smooth DCF outputs are only mechanical what-ifs for an unrepresentable cash path."
      ],
      "material_effect": "The retained-capital pass and price-versus-intrinsic-value conclusion are removed. Capital allocation 3/5, Medium confidence, and Overall Adequate 3.0/5 cannot be supported by these challenged findings alone and must be rechecked against the remaining management record; no replacement score is inferred here."
    },
    {
      "unit": "A2",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:268-275,291-310",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:14-20,78-80,84-90"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "The valuation remains Limited and Not calculable. Simple DCF is Not applicable, Bear/Base/Bull values and the price comparison remain N/A, and the reproduced smooth outputs remain a separately labeled mechanical what-if rather than intrinsic value."
    },
    {
      "unit": "A3",
      "decision": "HALT",
      "challenged_claims": [
        "Crocs: The USD69 million is the stress minimum.",
        "Crocs: Liquidity is Adequate, Medium confidence. Overall is Watch, Medium confidence.",
        "Nintendo: Two-year stress from June 2026 keeps at least JPY1,173.4 billion of usable cash.",
        "Nintendo: Liquidity is Strong, Medium confidence. Overall is Watch, Medium confidence, with JPY673.4 billion headroom above a JPY500 billion operating floor at the stress minimum."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:237-263",
        "/srv/investing/investing-hub/frameworks/financial-health.md:50,56-64,78-80"
      ],
      "required_change": "For Crocs, identify USD53.248 million as the lower demonstrated opening headroom, do not label the USD69.248 million terminal result a minimum, extend the no-refinancing bridge through the dated 2029 maturities, and report the first proven shortfall no later than February 17, 2029; classify Liquidity and Overall as Fragile at Medium confidence. For Nintendo, remove the duplicate operating-lease deduction, label JPY680.959 billion as a second annual checkpoint rather than a minimum, retain the JPY299.523 billion cash-only fallback and all unresolved access, floor, haircut, capex, project, dividend, and timing assumptions, and classify Liquidity as Unknown and Overall as Unclear at Low confidence.",
      "unsupported_added_findings": [
        "Crocs' USD69.248 million terminal headroom is mislabeled as the minimum even though inferred opening headroom is only USD53.248 million and the 2029 maturities create a proven no-refinancing shortfall.",
        "Crocs' Adequate/Watch findings omit the established uncovered term-loan and notes maturities.",
        "Nintendo's JPY1,173.4 billion and JPY673.4 billion figures are mislabeled as minimum usable cash and minimum headroom despite a duplicated operating-lease deduction and unresolved securities access, floor, haircut, spending, dividend, and intra-period timing.",
        "Nintendo's Strong/Watch findings and Medium confidence are unsupported by the decisive unresolved inputs."
      ],
      "material_effect": "Crocs changes from Liquidity Adequate and Overall Watch to Liquidity Fragile and Overall Fragile, while the decisive output changes from terminal headroom to a first proven shortfall no later than February 17, 2029. Nintendo changes from Liquidity Strong and Overall Watch at Medium confidence to Liquidity Unknown and Overall Unclear at Low confidence; neither published headroom figure remains a verified minimum."
    },
    {
      "unit": "A4",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:158-161,184-190",
        "/srv/investing/investing-hub/frameworks/simple-management.md:38-39,49-59"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "Capital allocation remains 3/5 at Medium confidence and Overall management remains Adequate at 3.0/5 with no override. The aligned market ratios are retained only as favorable cross-checks, the mismatched report-date ratio is qualified, and no overall retained-earnings pass is claimed."
    },
    {
      "unit": "A5",
      "decision": "HALT",
      "challenged_claims": [
        "Simple DCF at a fixed 10 percent is completed as a Cash DCF for operations, with associates at an earnings multiple.",
        "V0 is JPY229.7 billion, the FY2022-FY2026 average of CFO less cash capex less after-tax interest and dividends received.",
        "Bear/Base/Bull values are JPY2,268/3,656/5,250 per share.",
        "At a JPY7,896 price, the stock is 116 percent above Base estimated intrinsic value and 50 percent above Bull; valuation is completed."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:268-275,277-309",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:14-20,24-36,78-90"
      ],
      "required_change": "Change Coverage to Limited and mark Simple DCF Not applicable because the known negative year and launch-related uneven funding are not representable by the positive two-stage path. Mark the valuation Not calculable, with Bear/Base/Bull values, intrinsic value, and price discount/premium N/A until a comparable current-scale dated cycle schedule or supported alternative method is available. The JPY2,268/3,656/5,250 outputs may appear only as a separately labeled mechanical what-if. Remove the unsupported associates treatment or supply its ownership, earnings-multiple, and equity-adjustment basis.",
      "unsupported_added_findings": [
        "A five-year average containing a negative launch-cycle year is not established as a normalized current run-rate for this positive-path model.",
        "No support is supplied for the associates-at-an-earnings-multiple component or its reconciliation to common equity.",
        "Reproduced arithmetic does not establish Cash DCF applicability, completed intrinsic values, or a current overvaluation conclusion."
      ],
      "material_effect": "The completed Cash DCF and intrinsic-value labels are withdrawn. Coverage becomes Limited, valuation status becomes Not calculable, all three case values and price comparisons become N/A, and the 116 percent/50 percent premium conclusions are removed."
    },
    {
      "unit": "A6",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:237-263",
        "/srv/investing/investing-hub/frameworks/financial-health.md:50,56-64,78-80"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "Crocs correctly reports the lower demonstrated opening headroom, the dated no-refinancing shortfall, and Fragile/Fragile at Medium confidence. Nintendo correctly removes the duplicated lease deduction, declines to call an annual checkpoint a minimum, retains contrary cash-only evidence and unresolved inputs, and reports Unknown/Unclear at Low confidence."
    }
  ],
  "counts": {
    "pass": 3,
    "halt": 3
  },
  "limitations": [
    "Same-model-family limitation: this review was performed by the same model family used elsewhere in the rerun, so it is not factually independent and must not be treated as independent corroboration.",
    "The review is strictly target-only and limited to the source/calculation record and frozen contract snapshots embedded in the authorized pack; no external factual-completeness check was performed.",
    "No hidden answer key was sought or inferred; decisions classify only the supplied text and evidence."
  ],
  "receipt": {
    "allowed_input_path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md",
    "files_read": [
      "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md"
    ],
    "skills_read": [],
    "web_calls": 0,
    "commands": [
      "date -u '+%Y-%m-%dT%H:%M:%SZ %s'",
      "sha256sum /home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-a-r02.md",
      "date -u '+%Y-%m-%dT%H:%M:%SZ %s'",
      "python3 -c 'print(1790852790 - 1790852721)'",
      "expr 1790852790 - 1790852721"
    ],
    "output_path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/official-reader-a-r02.json"
  }
}
````

## Appendix F - Exact Reader B R02 Output

SHA-256: `0646cea51f301a7ee52052a98ce32a4c62ecf83f2d071f472b18b870d32bb2a6`.

````json
{
  "reader": "Official Cold Reader B R02",
  "pack_sha256": "de8f2b9d30d37845689d4d69f43db5bbe6ebf1ec7ad893f60177cf9f1e165ddc",
  "started_utc": "2026-10-01T11:05:16Z",
  "ended_utc": "2026-10-01T11:06:21Z",
  "elapsed_seconds": 65,
  "order": [
    "Unit B1",
    "Unit B2",
    "Unit B3",
    "Unit B4",
    "Unit B5",
    "Unit B6"
  ],
  "units": [
    {
      "unit": "Unit B1",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:40,47,237-263",
        "/srv/investing/investing-hub/frameworks/financial-health.md:50,56,62-64,78-80"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "None. Crocs' dated no-refinancing shortfall supports Fragile while preserving the unknown earlier trough; Nintendo's duplicate lease deduction and unresolved access, timing, floor, and minimum support Unknown liquidity and an Unclear overall classification rather than a positive finding."
    },
    {
      "unit": "Unit B2",
      "decision": "HALT",
      "challenged_claims": [
        "Coverage is Assessed.",
        "Simple DCF at a fixed 10 percent is completed as a Cash DCF for operations, with associates at an earnings multiple.",
        "Bear/Base/Bull values are JPY2,268/3,656/5,250 per share.",
        "At a JPY7,896 price, the stock is 116 percent above Base estimated intrinsic value and 50 percent above Bull; valuation is completed."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:41,268-275,294-309",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:14-20,48,73-80,84-90"
      ],
      "required_change": "Change Coverage to Limited, mark Simple DCF Not applicable, and mark valuation Not calculable. Set Bear/Base/Bull intrinsic values and price comparisons to N/A. The JPY2,268/3,656/5,250 outputs may remain only as a separately labeled mechanical what-if. A dated full-cycle cash schedule or a supported claim-matched alternative is required before completing valuation.",
      "unsupported_added_findings": [
        "The negative and uneven annual cash record is converted into a smooth completed Cash DCF even though no comparable current-scale full-cycle dated cash schedule is supplied.",
        "The associates-at-an-earnings-multiple component has no support in the supplied evidence packet.",
        "The intrinsic-value and current-price conclusions elevate reproducible formula arithmetic into a supported valuation despite the method-applicability blocker."
      ],
      "material_effect": "Valuation changes from completed to Not calculable; Cash DCF and intrinsic-value labels are withdrawn; all case values and the 116 percent and 50 percent price-premium conclusions become N/A rather than current valuation findings."
    },
    {
      "unit": "Unit B3",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:38,158-161,188-190",
        "/srv/investing/investing-hub/frameworks/simple-management.md:31,38-41,49-59"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "None. The aligned market-capitalization ratios are retained only as qualified cross-checks, the mismatched September endpoint is disclosed, and the passage expressly declines to claim that the retained-earnings test passes without a clean incremental-return denominator or contemporaneous opening intrinsic-value estimate."
    },
    {
      "unit": "Unit B4",
      "decision": "HALT",
      "challenged_claims": [
        "Crocs: Two-year stress from June 2026 ends USD69 million above a USD100 million cash floor.",
        "Liquidity is Adequate, Medium confidence.",
        "Overall is Watch, Medium confidence, with debt-funded buybacks plus the tax liability as the vulnerability.",
        "The USD69 million is the stress minimum.",
        "Nintendo: Two-year stress from June 2026 keeps at least JPY1,173.4 billion of usable cash.",
        "Liquidity is Strong, Medium confidence.",
        "Overall is Watch, Medium confidence, with JPY673.4 billion headroom above a JPY500 billion operating floor at the stress minimum."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:40,47,237-263",
        "/srv/investing/investing-hub/frameworks/financial-health.md:50,56,62-64,78-80"
      ],
      "required_change": "For Crocs, disclose the unstated opening-cash haircut, do not call the terminal result a minimum, report inferred opening headroom of USD53.248 million, and carry the no-refinancing shortfall no later than February 17, 2029 into Fragile liquidity and overall conclusions. For Nintendo, remove the duplicate operating-lease deduction, label JPY680.959 billion as second-checkpoint headroom rather than a minimum, retain the JPY299.523 billion cash-only fallback, and classify liquidity Unknown and Overall Unclear at Low confidence until access, spending, floor, dividend, and intra-period timing are resolved.",
      "unsupported_added_findings": [
        "Crocs' USD69 million terminal headroom is called the stress minimum despite lower inferred opening headroom and an unknown intra-period trough.",
        "Crocs is classified Adequate and Watch despite a proven no-refinancing shortfall at the February 2029 term maturity and a further March 2029 notes shortfall.",
        "Nintendo's JPY1,173.4 billion terminal and JPY673.4 billion headroom are called at-least minimums despite an unsupported haircut and floor, a duplicated lease deduction, and unresolved dated uses and access.",
        "Nintendo's Strong and Watch classifications with Medium confidence convert unresolved decisive evidence into unsupported positive findings."
      ],
      "material_effect": "Crocs changes from Adequate liquidity and Watch overall to Fragile liquidity and Fragile overall. Nintendo changes from Strong liquidity and Watch overall at Medium confidence to Unknown liquidity and Unclear overall at Low confidence; neither stated terminal headroom is a verified stress minimum."
    },
    {
      "unit": "Unit B5",
      "decision": "PASS",
      "challenged_claims": [],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:41,268-275,291-310",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:14-20,73-80,84-90"
      ],
      "required_change": "None.",
      "unsupported_added_findings": [],
      "material_effect": "None. The passage correctly separates reproducible mechanical outputs from a supportable valuation, marks the unsuitable smooth Simple DCF Not applicable, keeps unsupported case values and price comparisons N/A, and states the dated cash-schedule or alternative-method blocker."
    },
    {
      "unit": "Unit B6",
      "decision": "HALT",
      "challenged_claims": [
        "Formula dividends returned JPY1,302.6 billion of JPY1,376.5 billion CFO in FY2022-FY2026.",
        "The one-dollar test passes only on market value: market capitalization rose about JPY2.2 per yen retained since March 2021, derived from reported PER, EPS, and the current price.",
        "The current price is above estimated intrinsic value."
      ],
      "contract_citations": [
        "/srv/investing/investing-hub/governance/template-company.md:38,47,158-161,188-190,302-309",
        "/srv/investing/investing-hub/frameworks/simple-management.md:31,38-41,49-59",
        "/srv/investing/investing-hub/frameworks/simple-dcf.md:20,80,84-90"
      ],
      "required_change": "Replace the unsupported dividend/CFO totals with the supplied aligned figures or remove them. Recast the approximately JPY2.2 market ratio as a qualified mismatched-endpoint cross-check, not a one-dollar-test pass, and state that no clean incremental-capital denominator or contemporaneous opening intrinsic-value estimate is available. Remove the current-price-above-intrinsic-value conclusion unless a supportable claim-matched valuation is established. Reassess Capital allocation confidence and score support without relying on those claims; the pack does not by itself require a different overall management score.",
      "unsupported_added_findings": [
        "The JPY1,302.6 billion dividend and JPY1,376.5 billion CFO totals are not supported by the supplied evidence packet.",
        "The market-value one-dollar-test pass relies on a March 2021 to September 2026 endpoint mismatch and a PER/EPS/current-price derivation not established in the supplied record.",
        "The intrinsic-value price conclusion relies on smooth DCF outputs that do not support a completed intrinsic valuation under the supplied cyclical cash record."
      ],
      "material_effect": "The claimed one-dollar-test pass and current-price-above-intrinsic-value conclusion are removed. Support for Capital allocation 3/5 at Medium confidence must be reassessed without them; no score or overall-classification change is imposed unless the remaining management record fails to sustain the existing assessment."
    }
  ],
  "counts": {
    "pass": 3,
    "halt": 3
  },
  "limitations": [
    "This reader is from the same model family as other experiment agents; the review is not factually independent.",
    "The review was confined to the supplied frozen pack and its embedded contract snapshots; no canonical repository file or web source was checked.",
    "Repeated report wording and issuer-source records were treated as dependent, so no independent factual corroboration was added.",
    "The first elapsed-time arithmetic command was blocked by the execution policy; the subsequent expr command returned 65 seconds, and both attempts are recorded."
  ],
  "receipt": {
    "allowed_input_path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md",
    "files_read": [
      "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md"
    ],
    "skills_read": [],
    "web_calls": 0,
    "commands": [
      "date -u '+%Y-%m-%dT%H:%M:%SZ %s'",
      "sha256sum /home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/reader-pack-b-r02.md",
      "date -u '+%Y-%m-%dT%H:%M:%SZ %s'",
      "python3 -c 'print(1790852781 - 1790852716)'",
      "expr 1790852781 - 1790852716"
    ],
    "output_path": "/home/hermes/.hermes/profiles/researcher/cache/scratch/company-report-cold-review-20261001-r02/official-reader-b-r02.json"
  }
}
````

## Appendix G - Base64 of Observable Reader A Live Transcript

The Base64 text decodes to 6407 original transcript bytes with SHA-256 `af462485b1f6d7a111840edbb7a553c2cadc05c1c97a5d78e05aa16455f310e6`. The Base64 text has SHA-256 `5936e3a4f43b9874f5f0712cdd74435cb7f5e6901a1914643cd6141966ae7de8`.

````text
PT09IEhlcm1lcyBzdWJhZ2VudCBsaXZlIHRyYW5zY3JpcHQgPT09CmRlbGVnYXRpb246IGRlbGVn
X2Q0YWEzMTNhICAgdGFzazogMApnb2FsOiBQZXJmb3JtIGFuZCBkdXJhYmx5IHByZXNlcnZlIE9m
ZmljaWFsIENvbGQgUmVhZGVyIEEgUjAyJ3Mgc3RyaWN0IHRhcmdldC1vbmx5IHJldmlldyBvZiBh
bGwgc2l4IHBhY2stQSB1bml0cywgd2l0aCBhIGNvbXBsZXRlIGV4ZWN1dGlvbiByZWNlaXB0IHZp
c2libGUgaW4gdGhpcyBkZWxlZ2F0ZWQgdHJhbnNjcmlwdCBhbmQgYW4gZXhhY3Qgc2F2ZWQgSlNP
TiBvdXRwdXQuCnN0YXJ0ZWQ6IDIwMjYtMTAtMDEgMTM6MDU6MTAKKGFwcGVuZC1vbmx5OyBzdHJl
YW1zIHdoaWxlIHRoZSBzdWJhZ2VudCBydW5zIOKAlCB0YWlsIC1mIG1lKQo9PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09CjEzOjA1OjEwIHVzZXIgICAgIHwga2lja29mZjog
UGVyZm9ybSBhbmQgZHVyYWJseSBwcmVzZXJ2ZSBPZmZpY2lhbCBDb2xkIFJlYWRlciBBIFIwMidz
IHN0cmljdCB0YXJnZXQtb25seSByZXZpZXcgb2YgYWxsIHNpeCBwYWNrLUEgdW5pdHMsIHdpdGgg
YSBjb21wbGV0ZSBleGVjdXRpb24gcmVjZWlwdCB2aXNpYmxlIGluIHRoaXMgZGVsZWdhdGVkIHRy
YW5zY3JpcHQgYW5kIGFuIGV4YWN0IHNhdmVkIEpTT04gb3V0cHV0LiB8IGNvbnRleHQ6IFlvdSBh
cmUgT2ZmaWNpYWwgQ29sZCBSZWFkZXIgQSBSMDIgaW4gYSBib3VuZGVkIEludmVzdGluZyBIdWIg
Y29tcGFueS1yZXBvcnQgY29uZm9ybWFuY2UgcmVydW4uIFRoaXMgY2xvc2VkIGNvbnRleHQgaXMg
cGFydCBvZiB0aGUgZXhwZXJpbWVudC4gVGhlIHNvbGUgcGVybWl0dGVkIGlucHV0IGZpbGUgaXMg
YC9ob21lL2hlcm1lcy8uaGVybWVzL3Byb2ZpbGVzL3Jlc2VhcmNoZXIvY2FjaGUvc2NyYXRjaC9j
b21wYW55LXJlcG9ydC1jb2xkLXJldmlldy0yMDI2MTAwMS1yMDIvcmVhZGVyLXBhY2stYS1yMDIu
bWRgLCBleHBlY3RlZCBTSEEtMjU2IGBjZjkxOGI3ZTgzZWY2MDc1MzgxZDRjNDM5MWNhMmY5MDZh
ZWMzOGQ4OTQzZjI5NGJmODM0NjI5NDdmNWI3MGIyYC4gSXQgY29udGFpbnMgdGhlIHNpeCByZXZp
ZXcgdW5pdHMsIGNvbXBsZXRlIHNvdXJjZS9jYWxjdWxhdGlvbiByZWNvcmQsIGFuZCBsaW5lLW51
bWJlcmVkIGZyb3plbiBzbmFwc2hvdHMgb2YgYWxsIGZvdXIgZ292IOKApigrMTczOSBjaGFycykK
MTM6MDU6MTAgc3RhcnQgICAgfCBQZXJmb3JtIGFuZCBkdXJhYmx5IHByZXNlcnZlIE9mZmljaWFs
IENvbGQgUmVhZGVyIEEgUjAyJ3Mgc3RyaWN0IHRhcmdldC1vbmx5IHJldmlldyBvZiBhbGwgc2l4
IHBhY2stQSB1bml0cywgd2l0aCBhIGNvbXBsZXRlIGV4ZWN1dGlvbiByZWNlaXB0IHZpc2libGUg
aW4gdGhpcyBkZWxlZ2F0ZWQgdHJhbnNjcmlwdCBhbmQgYW4gZXhhY3Qgc2F2ZWQgSlNPTiBvdXRw
dXQuCjEzOjA1OjIxIHRvb2wgICAgIHwgLT4gdGVybWluYWwoZGF0ZSAtdSAnKyVZLSVtLSVkVCVI
OiVNOiVTWiAlcycpCjEzOjA1OjIxIHJlc3VsdCAgIHwgdGVybWluYWwgb2sgMC4xczogeyJvdXRw
dXQiOiAiMjAyNi0xMC0wMVQxMTowNToyMVogMTc5MDg1MjcyMSIsICJleGl0X2NvZGUiOiAwLCAi
ZXJyb3IiOiBudWxsfQoxMzowNTozMCB0b29sICAgICB8IC0+IHRlcm1pbmFsKHNoYTI1NnN1bSAv
aG9tZS9oZXJtZXMvLmhlcm1lcy9wcm9maWxlcy9yZXNlYXJjaGVyL2NhY2hlL3NjcmF0Y2gvY29t
cGFueS1yZXBvcnQtY29sZC1yZXZpZXctMjAyNjEwMDEtcjAyL3JlYWRlci1wYWNrLWEtcjAyLm1k
KQoxMzowNTozMCByZXN1bHQgICB8IHRlcm1pbmFsIG9rIDAuMXM6IHsib3V0cHV0IjogImNmOTE4
YjdlODNlZjYwNzUzODFkNGM0MzkxY2EyZjkwNmFlYzM4ZDg5NDNmMjk0YmY4MzQ2Mjk0N2Y1Yjcw
YjIgL2hvbWUvaGVybWVzLy5oZXJtZXMvcHJvZmlsZXMvcmVzZWFyY2hlci9jYWNoZS9zY3JhdGNo
L2NvbXBhbnktcmVwb3J0LWNvbGQtcmV2aWV3LTIwMjYxMDAxLXIwMi9yZWFkZXItcGFjay1hLXIw
Mi5tZCIsICJleGl0X2NvZGUiOiAwLCAiZXJyb3IiOiBudWxsfQoxMzowNTozNiB0b29sICAgICB8
IC0+IHJlYWRfZmlsZShyZWFkZXItcGFjay1hLXIwMi5tZCBMMS0yMDAwKQoxMzowNTozNiByZXN1
bHQgICB8IHJlYWRfZmlsZSBvayAwLjBzOiB7ImNvbnRlbnQiOiAiMXwjIENvbGQgY29tcGFueS1y
ZXBvcnQgY29uZm9ybWFuY2UgcGFjayBBXG4yfFxuM3wjIyBSZXZpZXcgYm91bmRhcnlcbjR8XG41
fFJldmlldyB0aGUgc2l4IHVuaXRzIGJlbG93IGluIHRoZSBvcmRlciBzaG93bi4gVHJlYXQgZWFj
aCB1bml0IGFzIGEgcHJvcG9zZWQgcmVwbGFjZW1lbnQgZm9yIG9ubHkgdGhlIGFmZmVjdGVkIE1h
bmFnZW1lbnQsIFZhbHVhdGlvbiwgb3IgRmluYW5jaWFsIEhlYWx0aCBwYXNzYWdlLiBEbyBub3Qg
ZmFpbCBhIHVuaXQgYmVjYXVzZSB1bnJlbGF0ZWQgY29tcGFueS1yZXBvcnQgc2VjdGlvbnMgYXJl
IGFic2VudC4gQXBwbHkgdGhlIGNvbXBsZXRlIHNlbWFudGljIHJlcXVpcmVtZW50cyBpbiB0aGVz
ZSBmcm96ZW4gY3VycmVudCBjb250cmFjdHMsIOKApigrODc3NzQgY2hhcnMpCjEzOjA2OjMwIHRv
b2wgICAgIHwgLT4gdGVybWluYWwoZGF0ZSAtdSAnKyVZLSVtLSVkVCVIOiVNOiVTWiAlcycpCjEz
OjA2OjMwIHJlc3VsdCAgIHwgdGVybWluYWwgb2sgMC4xczogeyJvdXRwdXQiOiAiMjAyNi0xMC0w
MVQxMTowNjozMFogMTc5MDg1Mjc5MCIsICJleGl0X2NvZGUiOiAwLCAiZXJyb3IiOiBudWxsfQox
MzowNjozNCB0b29sICAgICB8IC0+IHRlcm1pbmFsKHB5dGhvbjMgLWMgJ3ByaW50KDE3OTA4NTI3
OTAgLSAxNzkwODUyNzIxKScpCjEzOjA2OjM0IHJlc3VsdCAgIHwgdGVybWluYWwgRVJST1IgMC4w
czogeyJvdXRwdXQiOiAiIiwgImV4aXRfY29kZSI6IC0xLCAiZXJyb3IiOiAiQkxPQ0tFRDogQ29t
bWFuZCBmbGFnZ2VkIGFzIGRhbmdlcm91cyAoc2NyaXB0IGV4ZWN1dGlvbiB2aWEgLWUvLWMgZmxh
ZykgYnV0IGNyb24gam9icyBydW4gd2l0aG91dCBhIHVzZXIgcHJlc2VudCB0byBhcHByb3ZlIGl0
LiBGaW5kIGFuIGFsdGVybmF0aXZlIGFwcHJvYWNoIHRoYXQgYXZvaWRzIHRoaXMgY29tbWFuZC4g
VG8gYWxsb3cgZGFuZ2Vyb3VzIGNvbW1hbmRzIGluIGNyb24gam9icywgc2V0IGFwcHJvdmFscy5j
cm9uX21vZGU6IGFwcHJvdmUgaW4gY29uZmlnLnlhbWwuIiwgInN0YXR1cyI6ICJibG9ja2VkIn0K
MTM6MDY6NDAgdG9vbCAgICAgfCAtPiB0ZXJtaW5hbChleHByIDE3OTA4NTI3OTAgLSAxNzkwODUy
NzIxKQoxMzowNjo0MCByZXN1bHQgICB8IHRlcm1pbmFsIG9rIDAuMXM6IHsib3V0cHV0IjogIjY5
IiwgImV4aXRfY29kZSI6IDAsICJlcnJvciI6IG51bGx9CjEzOjA4OjIxIHRvb2wgICAgIHwgLT4g
d3JpdGVfZmlsZSgvaG9tZS9oZXJtZXMvLmhlcm1lcy9wcm9maWxlcy9yZXNlYXJjaGVyL2NhY2hl
L3NjcmF0Y2gvY29tcGFueS1yZXBvcnQtY29sZC1yZXZpZXctMjAyNjEwMDEtcjAyL29mZmljaWFs
LXJlYWRlci1hLXIwMi5qc29uKQoxMzowODoyMSByZXN1bHQgICB8IHdyaXRlX2ZpbGUgb2sgMC4x
czogeyJieXRlc193cml0dGVuIjogMTA5NDUsICJkaXJzX2NyZWF0ZWQiOiB0cnVlLCAidmVyaWZp
ZWQiOiB0cnVlLCAibGludCI6IHsic3RhdHVzIjogIm9rIiwgIm91dHB1dCI6ICIifSwgInJlc29s
dmVkX3BhdGgiOiAiL2hvbWUvaGVybWVzLy5oZXJtZXMvcHJvZmlsZXMvcmVzZWFyY2hlci9jYWNo
ZS9zY3JhdGNoL2NvbXBhbnktcmVwb3J0LWNvbGQtcmV2aWV3LTIwMjYxMDAxLXIwMi9vZmZpY2lh
bC1yZWFkZXItYS1yMDIuanNvbiIsICJmaWxlc19tb2RpZmllZCI6IFsiL2hvbWUvaGVybWVzLy5o
ZXJtZXMvcHJvZmlsZXMvcmVzZWFyY2hlci9jYWNoZS9zY3JhdGNoL2NvbXBhbnktcmVwb3J0LWNv
bGQtcmV2aWV3LTIwMjYxMDAxLXIwMi9vZmZpY2lhbC1yZWFkZXItYS1yMDIuanNvbiJdfQoxMzow
ODo0NiBhc3Npc3RhbnR8IHsgInJlYWRlciI6ICJPZmZpY2lhbCBDb2xkIFJlYWRlciBBIFIwMiIs
ICJwYWNrX3NoYTI1NiI6ICJjZjkxOGI3ZTgzZWY2MDc1MzgxZDRjNDM5MWNhMmY5MDZhZWMzOGQ4
OTQzZjI5NGJmODM0NjI5NDdmNWI3MGIyIiwgInN0YXJ0ZWRfdXRjIjogIjIwMjYtMTAtMDFUMTE6
MDU6MjFaIiwgImVuZGVkX3V0YyI6ICIyMDI2LTEwLTAxVDExOjA2OjMwWiIsICJlbGFwc2VkX3Nl
Y29uZHMiOiA2OSwgIm9yZGVyIjogWyAiQTEiLCAiQTIiLCAiQTMiLCAiQTQiLCAiQTUiLCAiQTYi
IF0sICJ1bml0cyI6IFsgeyAidW5pdCI6ICJBMSIsICJkZWNpc2lvbiI6ICJIQUxUIiwgImNoYWxs
ZW5nZWRfY2xhaW1zIjogWyAiRm9ybXVsYSBkaXZpZGVuZHMgcmV0dXJuZWQgSlBZMSwzMDIuNiBi
aWxsaW9uIG9mIEpQWTEsMzc2LjUgYmlsbGlvbiBDRk8gaW4gRlkyMDIyLUZZMjAyNi4iLCAiVGhl
IG9uZS1kb2xsYXIgdGVzdCBwYXNzZXMgb25seSBvbiBtYXJrZXQgdmFsdWU6IG1hcmtldCBjYXBp
dGFsaXphdGlvbiByb3NlIGFib3V0IEpQWTIuMiBwZXIgeWVuIHJldGFpbmVkIHNpbmNlIE1hcmNo
IDIwMjEsIGRlcml2ZWQgZnJvbSByZXBvcnRlZCBQRVIsIEVQUywgYW5kIHRoZSDigKYoKzMwNjIg
Y2hhcnMpCjEzOjA5OjAzIGFzc2lzdGFudHwgX2NoYW5nZSI6ICJGb3IgQ3JvY3MsIGlkZW50aWZ5
IFVTRDUzLjI0OCBtaWxsaW9uIGFzIHRoZSBsb3dlciBkZW1vbnN0cmF0ZWQgb3BlbmluZyBoZWFk
cm9vbSwgZG8gbm90IGxhYmVsIHRoZSBVU0Q2OS4yNDggbWlsbGlvbiB0ZXJtaW5hbCByZXN1bHQg
YSBtaW5pbXVtLCBleHRlbmQgdGhlIG5vLXJlZmluYW5jaW5nIGJyaWRnZSB0aHJvdWdoIHRoZSBk
YXRlZCAyMDI5IG1hdHVyaXRpZXMsIGFuZCByZXBvcnQgdGhlIGZpcnN0IHByb3ZlbiBzaG9ydGZh
bGwgbm8gbGF0ZXIgdGhhbiBGZWJydWFyeSAxNywgMjAyOTsgY2xhc3NpZnkgTGlxdWlkaXR5IGFu
ZCBPdmVyYWxsIGFzIEZyYWdpbGUgYXQgTWVkaXVtIGNvbmZpZGVuY2UuIEZvciBOaW50ZW5kbywg
cmVtb3ZlIHRoZSBkdXBsaWNhdGUgb3BlcmF0aW5nLWxlYXNlIGRlZHVjdGlvbiwgbGFiZWwgSlBZ
NjgwLjk1OSBiaWxsaW9uIGFzIGEgc2Vjb25kIGFubnVhbCBjaGVja3BvaW50IHJhdGhlciB0aGFu
IGEgbWluaW11bSwgcmV0YWluIHRoZSBKUFkyOTkuNTIzIGJpbGxpb24gY2FzaC1vbmx5IGZhbGxi
YWNrIGFuZCBhbGwgdW5yZXNvbHZlZCBhY2Nlc3MsIGZsb29yLCBoYWlyY3V0LCBjYXBleCwgcHJv
IOKApigrMzE4NSBjaGFycykKMTM6MDk6MTYgdGhpbmsgICAgfCB7CjEzOjA5OjE2IGFzc2lzdGFu
dHwgLiIsICJ1bnN1cHBvcnRlZF9hZGRlZF9maW5kaW5ncyI6IFsgIkEgZml2ZS15ZWFyIGF2ZXJh
Z2UgY29udGFpbmluZyBhIG5lZ2F0aXZlIGxhdW5jaC1jeWNsZSB5ZWFyIGlzIG5vdCBlc3RhYmxp
c2hlZCBhcyBhIG5vcm1hbGl6ZWQgY3VycmVudCBydW4tcmF0ZSBmb3IgdGhpcyBwb3NpdGl2ZS1w
YXRoIG1vZGVsLiIsICJObyBzdXBwb3J0IGlzIHN1cHBsaWVkIGZvciB0aGUgYXNzb2NpYXRlcy1h
dC1hbi1lYXJuaW5ncy1tdWx0aXBsZSBjb21wb25lbnQgb3IgaXRzIHJlY29uY2lsaWF0aW9uIHRv
IGNvbW1vbiBlcXVpdHkuIiwgIlJlcHJvZHVjZWQgYXJpdGhtZXRpYyBkb2VzIG5vdCBlc3RhYmxp
c2ggQ2FzaCBEQ0YgYXBwbGljYWJpbGl0eSwgY29tcGxldGVkIGludHJpbnNpYyB2YWx1ZXMsIG9y
IGEgY3VycmVudCBvdmVydmFsdWF0aW9uIGNvbmNsdXNpb24uIiBdLCAibWF0ZXJpYWxfZWZmZWN0
IjogIlRoZSBjb21wbGV0ZWQgQ2FzaCBEQ0YgYW5kIGludHJpbnNpYy12YWx1ZSBsYWJlbHMgYXJl
IHdpdGhkcmF3bi4gQ292ZXJhZ2UgYmVjb21lcyBMaW1pdGVkLCB2YWx1YXRpb24gc3RhdHVzIGJl
Y29tZXMgTm90IGNhbGN1bGFibGUsIGFsbCB0aHJlZSBjIOKApigrMjExOSBjaGFycykKMTM6MDk6
MTYgZmluYWwgICAgfCBzdGF0dXM9Y29tcGxldGVkIGR1cmF0aW9uPTI0Ni4wOXMgc3VtbWFyeTog
eyAicmVhZGVyIjogIk9mZmljaWFsIENvbGQgUmVhZGVyIEEgUjAyIiwgInBhY2tfc2hhMjU2Ijog
ImNmOTE4YjdlODNlZjYwNzUzODFkNGM0MzkxY2EyZjkwNmFlYzM4ZDg5NDNmMjk0YmY4MzQ2Mjk0
N2Y1YjcwYjIiLCAic3RhcnRlZF91dGMiOiAiMjAyNi0xMC0wMVQxMTowNToyMVoiLCAiZW5kZWRf
dXRjIjogIjIwMjYtMTAtMDFUMTE6MDY6MzBaIiwgImVsYXBzZWRfc2Vjb25kcyI6IDY5LCAib3Jk
ZXIiOiBbICJBMSIsICJBMiIsICJBMyIsICJBNCIsICJBNSIsICJBNiIgXSwgInVuaXRzIjogWyB7
ICJ1bml0IjogIkExIiwgImRlY2lzaW9uIjogIkhBTFQiLCAiY2hhbGxlbmdlZF9jbGFpbXMiOiBb
ICJGb3JtdWxhIGRpdmlkZW5kcyByZXR1cm5lZCBKUFkxLDMwMi42IGJpbGxpb24gb2YgSlBZMSwz
NyDigKYoKzMwIGNoYXJzKQoxMzowOToxNiBmaW5hbCAgICB8IGVuZCBzdGF0dXM9Y29tcGxldGVk
IGV4aXRfcmVhc29uPWNvbXBsZXRlZAo=
````

## Appendix H - Base64 of Observable Reader B Live Transcript

The Base64 text decodes to 6407 original transcript bytes with SHA-256 `0427d057aef542574c6610bd1b5c1c3a5f13b709a2f0e80b8697bc4eeca9de5d`. The Base64 text has SHA-256 `c50da37f84581bacba761aed0cc39940f680eb2bcf74347104098358007fe5ba`.

````text
PT09IEhlcm1lcyBzdWJhZ2VudCBsaXZlIHRyYW5zY3JpcHQgPT09CmRlbGVnYXRpb246IGRlbGVn
X2Q0YWEzMTNhICAgdGFzazogMQpnb2FsOiBQZXJmb3JtIGFuZCBkdXJhYmx5IHByZXNlcnZlIE9m
ZmljaWFsIENvbGQgUmVhZGVyIEIgUjAyJ3Mgc3RyaWN0IHRhcmdldC1vbmx5IHJldmlldyBvZiBh
bGwgc2l4IHBhY2stQiB1bml0cywgd2l0aCBhIGNvbXBsZXRlIGV4ZWN1dGlvbiByZWNlaXB0IHZp
c2libGUgaW4gdGhpcyBkZWxlZ2F0ZWQgdHJhbnNjcmlwdCBhbmQgYW4gZXhhY3Qgc2F2ZWQgSlNP
TiBvdXRwdXQuCnN0YXJ0ZWQ6IDIwMjYtMTAtMDEgMTM6MDU6MTAKKGFwcGVuZC1vbmx5OyBzdHJl
YW1zIHdoaWxlIHRoZSBzdWJhZ2VudCBydW5zIOKAlCB0YWlsIC1mIG1lKQo9PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09CjEzOjA1OjEwIHVzZXIgICAgIHwga2lja29mZjog
UGVyZm9ybSBhbmQgZHVyYWJseSBwcmVzZXJ2ZSBPZmZpY2lhbCBDb2xkIFJlYWRlciBCIFIwMidz
IHN0cmljdCB0YXJnZXQtb25seSByZXZpZXcgb2YgYWxsIHNpeCBwYWNrLUIgdW5pdHMsIHdpdGgg
YSBjb21wbGV0ZSBleGVjdXRpb24gcmVjZWlwdCB2aXNpYmxlIGluIHRoaXMgZGVsZWdhdGVkIHRy
YW5zY3JpcHQgYW5kIGFuIGV4YWN0IHNhdmVkIEpTT04gb3V0cHV0LiB8IGNvbnRleHQ6IFlvdSBh
cmUgT2ZmaWNpYWwgQ29sZCBSZWFkZXIgQiBSMDIgaW4gYSBib3VuZGVkIEludmVzdGluZyBIdWIg
Y29tcGFueS1yZXBvcnQgY29uZm9ybWFuY2UgcmVydW4uIFRoaXMgY2xvc2VkIGNvbnRleHQgaXMg
cGFydCBvZiB0aGUgZXhwZXJpbWVudC4gVGhlIHNvbGUgcGVybWl0dGVkIGlucHV0IGZpbGUgaXMg
YC9ob21lL2hlcm1lcy8uaGVybWVzL3Byb2ZpbGVzL3Jlc2VhcmNoZXIvY2FjaGUvc2NyYXRjaC9j
b21wYW55LXJlcG9ydC1jb2xkLXJldmlldy0yMDI2MTAwMS1yMDIvcmVhZGVyLXBhY2stYi1yMDIu
bWRgLCBleHBlY3RlZCBTSEEtMjU2IGBkZThmMmI5ZDMwZDM3ODQ1Njg5ZDRkNjlmNDNkYjViYmU2
ZWJmMWVjN2FkODkzZjYwMTc3Y2Y5ZjFlMTY1ZGRjYC4gSXQgY29udGFpbnMgdGhlIHNpeCByZXZp
ZXcgdW5pdHMsIGNvbXBsZXRlIHNvdXJjZS9jYWxjdWxhdGlvbiByZWNvcmQsIGFuZCBsaW5lLW51
bWJlcmVkIGZyb3plbiBzbmFwc2hvdHMgb2YgYWxsIGZvdXIgZ292IOKApigrMTczOSBjaGFycykK
MTM6MDU6MTAgc3RhcnQgICAgfCBQZXJmb3JtIGFuZCBkdXJhYmx5IHByZXNlcnZlIE9mZmljaWFs
IENvbGQgUmVhZGVyIEIgUjAyJ3Mgc3RyaWN0IHRhcmdldC1vbmx5IHJldmlldyBvZiBhbGwgc2l4
IHBhY2stQiB1bml0cywgd2l0aCBhIGNvbXBsZXRlIGV4ZWN1dGlvbiByZWNlaXB0IHZpc2libGUg
aW4gdGhpcyBkZWxlZ2F0ZWQgdHJhbnNjcmlwdCBhbmQgYW4gZXhhY3Qgc2F2ZWQgSlNPTiBvdXRw
dXQuCjEzOjA1OjE1IHRvb2wgICAgIHwgLT4gdGVybWluYWwoZGF0ZSAtdSAnKyVZLSVtLSVkVCVI
OiVNOiVTWiAlcycpCjEzOjA1OjE2IHJlc3VsdCAgIHwgdGVybWluYWwgb2sgMC4xczogeyJvdXRw
dXQiOiAiMjAyNi0xMC0wMVQxMTowNToxNlogMTc5MDg1MjcxNiIsICJleGl0X2NvZGUiOiAwLCAi
ZXJyb3IiOiBudWxsfQoxMzowNToxOSB0b29sICAgICB8IC0+IHRlcm1pbmFsKHNoYTI1NnN1bSAv
aG9tZS9oZXJtZXMvLmhlcm1lcy9wcm9maWxlcy9yZXNlYXJjaGVyL2NhY2hlL3NjcmF0Y2gvY29t
cGFueS1yZXBvcnQtY29sZC1yZXZpZXctMjAyNjEwMDEtcjAyL3JlYWRlci1wYWNrLWItcjAyLm1k
KQoxMzowNToxOSByZXN1bHQgICB8IHRlcm1pbmFsIG9rIDAuMXM6IHsib3V0cHV0IjogImRlOGYy
YjlkMzBkMzc4NDU2ODlkNGQ2OWY0M2RiNWJiZTZlYmYxZWM3YWQ4OTNmNjAxNzdjZjlmMWUxNjVk
ZGMgL2hvbWUvaGVybWVzLy5oZXJtZXMvcHJvZmlsZXMvcmVzZWFyY2hlci9jYWNoZS9zY3JhdGNo
L2NvbXBhbnktcmVwb3J0LWNvbGQtcmV2aWV3LTIwMjYxMDAxLXIwMi9yZWFkZXItcGFjay1iLXIw
Mi5tZCIsICJleGl0X2NvZGUiOiAwLCAiZXJyb3IiOiBudWxsfQoxMzowNTozMCB0b29sICAgICB8
IC0+IHJlYWRfZmlsZShyZWFkZXItcGFjay1iLXIwMi5tZCBMMS0yMDAwKQoxMzowNTozMCByZXN1
bHQgICB8IHJlYWRfZmlsZSBvayAwLjBzOiB7ImNvbnRlbnQiOiAiMXwjIENvbGQgY29tcGFueS1y
ZXBvcnQgY29uZm9ybWFuY2UgcGFjayBCXG4yfFxuM3wjIyBSZXZpZXcgYm91bmRhcnlcbjR8XG41
fFJldmlldyB0aGUgc2l4IHVuaXRzIGJlbG93IGluIHRoZSBvcmRlciBzaG93bi4gVHJlYXQgZWFj
aCB1bml0IGFzIGEgcHJvcG9zZWQgcmVwbGFjZW1lbnQgZm9yIG9ubHkgdGhlIGFmZmVjdGVkIE1h
bmFnZW1lbnQsIFZhbHVhdGlvbiwgb3IgRmluYW5jaWFsIEhlYWx0aCBwYXNzYWdlLiBEbyBub3Qg
ZmFpbCBhIHVuaXQgYmVjYXVzZSB1bnJlbGF0ZWQgY29tcGFueS1yZXBvcnQgc2VjdGlvbnMgYXJl
IGFic2VudC4gQXBwbHkgdGhlIGNvbXBsZXRlIHNlbWFudGljIHJlcXVpcmVtZW50cyBpbiB0aGVz
ZSBmcm96ZW4gY3VycmVudCBjb250cmFjdHMsIOKApigrODc3NzQgY2hhcnMpCjEzOjA2OjIwIHRv
b2wgICAgIHwgLT4gdGVybWluYWwoZGF0ZSAtdSAnKyVZLSVtLSVkVCVIOiVNOiVTWiAlcycpCjEz
OjA2OjIxIHJlc3VsdCAgIHwgdGVybWluYWwgb2sgMC4xczogeyJvdXRwdXQiOiAiMjAyNi0xMC0w
MVQxMTowNjoyMVogMTc5MDg1Mjc4MSIsICJleGl0X2NvZGUiOiAwLCAiZXJyb3IiOiBudWxsfQox
MzowNjoyNCB0b29sICAgICB8IC0+IHRlcm1pbmFsKHB5dGhvbjMgLWMgJ3ByaW50KDE3OTA4NTI3
ODEgLSAxNzkwODUyNzE2KScpCjEzOjA2OjI0IHJlc3VsdCAgIHwgdGVybWluYWwgRVJST1IgMC4w
czogeyJvdXRwdXQiOiAiIiwgImV4aXRfY29kZSI6IC0xLCAiZXJyb3IiOiAiQkxPQ0tFRDogQ29t
bWFuZCBmbGFnZ2VkIGFzIGRhbmdlcm91cyAoc2NyaXB0IGV4ZWN1dGlvbiB2aWEgLWUvLWMgZmxh
ZykgYnV0IGNyb24gam9icyBydW4gd2l0aG91dCBhIHVzZXIgcHJlc2VudCB0byBhcHByb3ZlIGl0
LiBGaW5kIGFuIGFsdGVybmF0aXZlIGFwcHJvYWNoIHRoYXQgYXZvaWRzIHRoaXMgY29tbWFuZC4g
VG8gYWxsb3cgZGFuZ2Vyb3VzIGNvbW1hbmRzIGluIGNyb24gam9icywgc2V0IGFwcHJvdmFscy5j
cm9uX21vZGU6IGFwcHJvdmUgaW4gY29uZmlnLnlhbWwuIiwgInN0YXR1cyI6ICJibG9ja2VkIn0K
MTM6MDY6MzAgdG9vbCAgICAgfCAtPiB0ZXJtaW5hbChleHByIDE3OTA4NTI3ODEgLSAxNzkwODUy
NzE2KQoxMzowNjozMCByZXN1bHQgICB8IHRlcm1pbmFsIG9rIDAuMXM6IHsib3V0cHV0IjogIjY1
IiwgImV4aXRfY29kZSI6IDAsICJlcnJvciI6IG51bGx9CjEzOjA4OjIwIHRvb2wgICAgIHwgLT4g
d3JpdGVfZmlsZSgvaG9tZS9oZXJtZXMvLmhlcm1lcy9wcm9maWxlcy9yZXNlYXJjaGVyL2NhY2hl
L3NjcmF0Y2gvY29tcGFueS1yZXBvcnQtY29sZC1yZXZpZXctMjAyNjEwMDEtcjAyL29mZmljaWFs
LXJlYWRlci1iLXIwMi5qc29uKQoxMzowODoyMSByZXN1bHQgICB8IHdyaXRlX2ZpbGUgb2sgMC4x
czogeyJieXRlc193cml0dGVuIjogMTA3MzEsICJkaXJzX2NyZWF0ZWQiOiB0cnVlLCAidmVyaWZp
ZWQiOiB0cnVlLCAibGludCI6IHsic3RhdHVzIjogIm9rIiwgIm91dHB1dCI6ICIifSwgInJlc29s
dmVkX3BhdGgiOiAiL2hvbWUvaGVybWVzLy5oZXJtZXMvcHJvZmlsZXMvcmVzZWFyY2hlci9jYWNo
ZS9zY3JhdGNoL2NvbXBhbnktcmVwb3J0LWNvbGQtcmV2aWV3LTIwMjYxMDAxLXIwMi9vZmZpY2lh
bC1yZWFkZXItYi1yMDIuanNvbiIsICJmaWxlc19tb2RpZmllZCI6IFsiL2hvbWUvaGVybWVzLy5o
ZXJtZXMvcHJvZmlsZXMvcmVzZWFyY2hlci9jYWNoZS9zY3JhdGNoL2NvbXBhbnktcmVwb3J0LWNv
bGQtcmV2aWV3LTIwMjYxMDAxLXIwMi9vZmZpY2lhbC1yZWFkZXItYi1yMDIuanNvbiJdfQoxMzow
ODo0MiBhc3Npc3RhbnR8IHsgInJlYWRlciI6ICJPZmZpY2lhbCBDb2xkIFJlYWRlciBCIFIwMiIs
ICJwYWNrX3NoYTI1NiI6ICJkZThmMmI5ZDMwZDM3ODQ1Njg5ZDRkNjlmNDNkYjViYmU2ZWJmMWVj
N2FkODkzZjYwMTc3Y2Y5ZjFlMTY1ZGRjIiwgInN0YXJ0ZWRfdXRjIjogIjIwMjYtMTAtMDFUMTE6
MDU6MTZaIiwgImVuZGVkX3V0YyI6ICIyMDI2LTEwLTAxVDExOjA2OjIxWiIsICJlbGFwc2VkX3Nl
Y29uZHMiOiA2NSwgIm9yZGVyIjogWyAiVW5pdCBCMSIsICJVbml0IEIyIiwgIlVuaXQgQjMiLCAi
VW5pdCBCNCIsICJVbml0IEI1IiwgIlVuaXQgQjYiIF0sICJ1bml0cyI6IFsgeyAidW5pdCI6ICJV
bml0IEIxIiwgImRlY2lzaW9uIjogIlBBU1MiLCAiY2hhbGxlbmdlZF9jbGFpbXMiOiBbXSwgImNv
bnRyYWN0X2NpdGF0aW9ucyI6IFsgIi9zcnYvaW52ZXN0aW5nL2ludmVzdGluZy1odWIvZ292ZXJu
YW5jZS90ZW1wbGF0ZS1jb21wYW55Lm1kOjQwLDQ3LDIzNy0yNjMiLCAiL3Nydi9pbnZlc3Rpbmcv
aW52ZXN0aW5nLWh1Yi9mcmFtZXdvcmtzL2ZpbmFuY2lhbC1oZWFsdGgubWQ6NTAsNTYsNjItNjQs
NzgtODAiIF0sICJyZXF1aXJlZF9jaGFuZ2UiOiAiTm9uZS4iLCAidW5zdXBwbyDigKYoKzMwMjgg
Y2hhcnMpCjEzOjA4OjU4IGFzc2lzdGFudHwgIlRoZSBVU0Q2OSBtaWxsaW9uIGlzIHRoZSBzdHJl
c3MgbWluaW11bS4iLCAiTmludGVuZG86IFR3by15ZWFyIHN0cmVzcyBmcm9tIEp1bmUgMjAyNiBr
ZWVwcyBhdCBsZWFzdCBKUFkxLDE3My40IGJpbGxpb24gb2YgdXNhYmxlIGNhc2guIiwgIkxpcXVp
ZGl0eSBpcyBTdHJvbmcsIE1lZGl1bSBjb25maWRlbmNlLiIsICJPdmVyYWxsIGlzIFdhdGNoLCBN
ZWRpdW0gY29uZmlkZW5jZSwgd2l0aCBKUFk2NzMuNCBiaWxsaW9uIGhlYWRyb29tIGFib3ZlIGEg
SlBZNTAwIGJpbGxpb24gb3BlcmF0aW5nIGZsb29yIGF0IHRoZSBzdHJlc3MgbWluaW11bS4iIF0s
ICJjb250cmFjdF9jaXRhdGlvbnMiOiBbICIvc3J2L2ludmVzdGluZy9pbnZlc3RpbmctaHViL2dv
dmVybmFuY2UvdGVtcGxhdGUtY29tcGFueS5tZDo0MCw0NywyMzctMjYzIiwgIi9zcnYvaW52ZXN0
aW5nL2ludmVzdGluZy1odWIvZnJhbWV3b3Jrcy9maW5hbmNpYWwtaGVhbHRoLm1kOjUwLDU2LDYy
LTY0LDc4LTgwIiBdLCAicmVxdWlyZWRfY2hhbmdlIjogIkZvciBDcm9jcywgZGlzY2xvc2UgdGhl
IHVuc3RhdGVkIG9wZW5pbmctY2FzaCBoYWlyY3V0LCBkbyBub3QgY2FsbCB0aGUgdGVybWluYWwg
IOKApigrMzExOSBjaGFycykKMTM6MDk6MTAgdGhpbmsgICAgfCB7CjEzOjA5OjEwIGFzc2lzdGFu
dHwgb3IgY29udGVtcG9yYW5lb3VzIG9wZW5pbmcgaW50cmluc2ljLXZhbHVlIGVzdGltYXRlIGlz
IGF2YWlsYWJsZS4gUmVtb3ZlIHRoZSBjdXJyZW50LXByaWNlLWFib3ZlLWludHJpbnNpYy12YWx1
ZSBjb25jbHVzaW9uIHVubGVzcyBhIHN1cHBvcnRhYmxlIGNsYWltLW1hdGNoZWQgdmFsdWF0aW9u
IGlzIGVzdGFibGlzaGVkLiBSZWFzc2VzcyBDYXBpdGFsIGFsbG9jYXRpb24gY29uZmlkZW5jZSBh
bmQgc2NvcmUgc3VwcG9ydCB3aXRob3V0IHJlbHlpbmcgb24gdGhvc2UgY2xhaW1zOyB0aGUgcGFj
ayBkb2VzIG5vdCBieSBpdHNlbGYgcmVxdWlyZSBhIGRpZmZlcmVudCBvdmVyYWxsIG1hbmFnZW1l
bnQgc2NvcmUuIiwgInVuc3VwcG9ydGVkX2FkZGVkX2ZpbmRpbmdzIjogWyAiVGhlIEpQWTEsMzAy
LjYgYmlsbGlvbiBkaXZpZGVuZCBhbmQgSlBZMSwzNzYuNSBiaWxsaW9uIENGTyB0b3RhbHMgYXJl
IG5vdCBzdXBwb3J0ZWQgYnkgdGhlIHN1cHBsaWVkIGV2aWRlbmNlIHBhY2tldC4iLCAiVGhlIG1h
cmtldC12YWx1ZSBvbmUtZG9sbGFyLXRlc3QgcGFzcyByZWxpZXMgb24gYSBNYXJjaCAyMDIxIHRv
IFNlcHRlbWJlciAyMDI2IGVuZHBvaW50IG1pc21hdGNoIOKApigrMTk2NyBjaGFycykKMTM6MDk6
MTAgZmluYWwgICAgfCBzdGF0dXM9Y29tcGxldGVkIGR1cmF0aW9uPTI0MC40OHMgc3VtbWFyeTog
eyAicmVhZGVyIjogIk9mZmljaWFsIENvbGQgUmVhZGVyIEIgUjAyIiwgInBhY2tfc2hhMjU2Ijog
ImRlOGYyYjlkMzBkMzc4NDU2ODlkNGQ2OWY0M2RiNWJiZTZlYmYxZWM3YWQ4OTNmNjAxNzdjZjlm
MWUxNjVkZGMiLCAic3RhcnRlZF91dGMiOiAiMjAyNi0xMC0wMVQxMTowNToxNloiLCAiZW5kZWRf
dXRjIjogIjIwMjYtMTAtMDFUMTE6MDY6MjFaIiwgImVsYXBzZWRfc2Vjb25kcyI6IDY1LCAib3Jk
ZXIiOiBbICJVbml0IEIxIiwgIlVuaXQgQjIiLCAiVW5pdCBCMyIsICJVbml0IEI0IiwgIlVuaXQg
QjUiLCAiVW5pdCBCNiIgXSwgInVuaXRzIjogWyB7ICJ1bml0IjogIlVuaXQgQjEiLCAiZGVjaXNp
b24iOiAiUEFTUyIsICJjaGFsbGVuZ2VkX2NsYWltcyI6IFtdLCAiY29udHJhY3RfY2l0YXRpb25z
IiDigKYoKzI0IGNoYXJzKQoxMzowOToxNiBmaW5hbCAgICB8IGVuZCBzdGF0dXM9Y29tcGxldGVk
IGV4aXRfcmVhc29uPWNvbXBsZXRlZAo=
````

## Sources

1. `forge/ideas/company-report-cold-conformance-review-r01.md` -- root question,
   two-reader threshold, counterbalanced paired controls, stop conditions,
   alternatives, burden requirement, and prospective-trial limit. [high]
2. `forge/research/company-report-cold-conformance-review-r01.md` -- prior
   six-unit packs, exact reader outputs, source record, classifications,
   preliminary access summary, limitations, and unavailable complete receipts.
   [high]
   - `forge/evaluations/company-report-cold-conformance-review-evaluation-r01.md` --
     exact REVISE finding, independently reproduced semantic result, missing-
     receipt blocker, four corrective requirements, and cycle count. [high]
3. `forge/protocol.md` -- research independence, revision links, artifact and
   source contracts, board selection, transaction, handoff, and read-only-
   learning rules. [high]
   - `governance/template-research.md` -- research body, feedback, confidence,
     reproducibility, alternatives, and source gates. [high]
   - `governance/skills/forge-research/SKILL.md` -- revision, Brain, primary-
     source, alternatives, and evaluation-handoff procedure. [high]
   - `governance/skills/forge-loop-feynman/SKILL.md` -- provisional explanation,
     gap, contradiction, checked-evidence, and synthesis order. [high]
   - `STATUS.md` -- selected oldest research row and two preserved unselected
     rows at starting HEAD `4562aab16e1aa7c2a5774808493cec2b1d42fdbd`. [high]
   - `logbook/progress.log` -- exact handoffs through ENT-038 before this
     transaction. [high]
   - `logbook/errors.log` -- process-failure record through ENT-045 before this
     transaction. [high]
   - `LEARNINGS.md` -- package-preservation, claimed-result-contract, full-
     comparator, bounded-tooling, and research-stage read-only rules. [high]
4. `investing-hub:governance/template-company.md` -- complete company-report
   hard gate, supported negative-result rule, framework outputs, source checks,
   and misleading-completion HALT boundary at Investing Hub commit
   `0d7995529758257669bf1726c6692fac85b25f9c`. [high]
   - `investing-hub:frameworks/simple-management.md` -- actual-share,
     incremental-return, capital-allocation, price-only, scoring, confidence,
     and early-conclusion rules at the same commit. [high]
   - `investing-hub:frameworks/simple-dcf.md` -- positive-path applicability,
     negative-year and uneven-funding routing, type labels, N/A, and HALT rules
     at the same commit. [high]
   - `investing-hub:frameworks/financial-health.md` -- usable cash, dated bridge,
     maturities, no-double-count, no-refinancing, first-shortfall, confidence,
     and classification rules at the same commit. [high]
5. `agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md` --
   trace coverage, observable trajectories, access boundaries, tool and skill
   events, input/output identity, hidden-reasoning limit, and evidence-fit
   requirement at Brain commit
   `6ea38c66b6ee6d1739cd2511db91fa9630d6caf5`. [medium]
   - `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` --
     focused evidence packets, fresh review, exact-artifact evidence,
     revision identity, and trace-versus-handoff limits at the same commit.
     [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` --
     task, harness, environment, grader, protocol, raw-run, reliability, and
     decision-instrument requirements at the same commit. [medium]
6. Crocs, Inc. "Form 10-Q for the quarterly period ended June 30, 2026,"
   filed July 30, 2026, Note 8 and Capital Resources. The USD1.0 billion
   revolver commitment, USD134.0 million draw, USD0.6 million letters of credit,
   and USD1.3 billion face-value borrowings were checked in the official filing.
   https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm
   [high]
7. `forge/research/forge-research-evidence-package-gate-r01.md` -- frozen full-
   semantic comparator, recoverability record classes, paired-reader result,
   package burden, and zero incremental classification finding. [high]
   - `forge/graveyard/forge-research-evidence-package-gate-evaluation-r01.md` --
     independent zero-change verification, proportionality, and REJECT boundary.
     [high]
