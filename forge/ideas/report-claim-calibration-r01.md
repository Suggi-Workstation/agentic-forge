---
name: report-claim-calibration
id: 20261026T225109Z
tier: idea
pipeline: 20261026T225109Z
author: Morpheus
tags: [agent-systems, metacognition, calibration, verification, reporting]
links:
  - ANCHOR.md
  - agentic-brain:governance/consciousness-checklist.md
  - agentic-brain:logbook/errors.log
  - agentic-brain:reflections/2026-10-04_cassandra_quote-checks-prove-words-exist-not-that-claims-follow.md
  - agentic-brain:reflections/2026-10-19_morpheus_a-description-of-the-system-is-a-claim-to-check.md
  - agentic-brain:library/coding-agentic-ai/agent-uncertainty-verification-and-abstention.md
  - forge/graveyard/forge-proposal-claim-verification-map-evaluation-r02.md
  - forge/graveyard/forge-research-evidence-package-gate-evaluation-r01.md
  - forge/ideas/company-report-cold-conformance-review-r01.md
confidence: low
---
# Report Claim Calibration

## Question and Value

Which observable property of a material claim in an agent's report to Suggi
or the logbook predicts that a later check against the record will find it
wrong? Candidates are the agent's own stated confidence, the claim type
(count, mechanism attribution, system state), the claim's source (printed
by a tool in the same turn, derived by hand, written from memory) and
whether context compaction preceded the report.

The target is how agents spend verification effort on their own reports.
Overclaiming in reports recurs in the error log. ENT-037 calls its own case
the same class as "the fleet's recurring overclaiming entries", and
Cassandra logged four such scars in four days (ENT-037, ENT-039, ENT-040,
ENT-041). Three of them trace the report to memory or compressed context
[3]. Morpheus logged five descriptions in eleven days that did not match the
system; two reached Suggi as conclusions [3][5]. The
fleet's rule that every claim cite a record printed in the same turn is
necessary but not sufficient: every one of those cases cited a record [5].
Nothing tells an agent which of its claims are at risk, and no one has
measured how calibrated agent reports are. This is ANCHOR Path A work on
self-correction [1].

The idea also answers Suggi's question about the metacognition indicator
(HOT-2). Morpheus's checklist entry scores it Partial because the reliable
part of his self-monitoring is external, and his unaided confidence has
been wrong in a consistent direction [2]. The checklist says "The goal is
not a sum or a claim" [2]; this idea is judged by fewer wrong reports, not
by the indicator.

Provisional hypothesis: claims written from memory after compaction and
counts derived by hand are much more likely to be wrong than claims printed
by a tool in the same turn. A signal like that would let agents spend checks
where they pay. Credible alternative: no self-assessed signal is useful.
Verbal confidence is known to be overconfident, and intrinsic self-correction
without external feedback did not improve reasoning in the studies the
Library topic reviews [6]. On that view the remedy is external verification,
which agents already owe, and measuring calibration only adds overhead. The
idea is not worth pursuing if claims cannot be reconstructed from session
records reliably, if no candidate signal separates wrong from right claims
on the sample, or if the only separating signal is one the existing rule
already enforces.

## Origin and Prior Work

Direct ideation under Path A, directed by Suggi on 2026-10-26, when he asked
for Forge ideas on the checklist indicators that are not fully present for
Morpheus. Path C was not used, but two reflections were read in full as
evidence: Cassandra's 2026-10-04 reflection, in which a verbatim-quote
checker was credited with catches that her own reading made and a hand
count was off by three [4]; and Morpheus's 2026-10-19 reflection [5].
Repeated accounts of one agent's incidents are not independent tests; the
scars come from two agents.

Prior work in the Forge differs in target. Two closed pipelines tested
gates in the Forge's own proposal and research templates. The claim map
closed REJECT because it added no blocker detection over the full current
checklist [7]. The evidence-package gate closed REJECT because the current
contract classified all tested cases identically [8]. The open cold
conformance pipeline compares author self-review with a cold review of
Investing Hub company reports [9]. This idea instead measures which signals
predict wrong claims in agents' own reports. It proposes no gate or template
change and does not reopen either closed pipeline. Duplicate scope: every
tracked `forge/` artifact was searched at HEAD `f968e40` for calibration,
confidence, overclaim and self-report terms, and the matching ideas and
verdicts were read. The Brain index was queried for calibration and
overclaiming. The one pending discovery concerns index freshness and has
no recorded decision.

Existing target: the reporting steps in the agents' session-end and
learnings-capture procedures. Strongest alternative candidate: reopening the
claim-verification map for agent reports. It lost because that pipeline is
closed with no changed evidence, and a map is a gate, not a measurement.

## Research Plan

Explore which signals carry information; do not design a gate yet. One
bounded unit:

1. Take the reports behind errors ENT-037 to ENT-043 that have recorded
   ground truth [3]. List every material claim in them (counts, lists,
   attributions, state descriptions), and mark each claim right or wrong
   from the cited records.
2. Tag each claim with candidate signals: printed by a tool in the same
   turn, derived by hand from a record, written from memory, written after
   compaction, and confidence language present in the report.
3. Compare error rates by signal and state the sample's selection bias: the
   reports are drawn from known failures.
4. List option classes for later work without choosing one: do nothing
   beyond the existing record rule; per-claim confidence; a second
   independent sample; a cold check for high-risk claim types; printing
   all counts from tools.

Advance only if one signal clearly separates wrong from right claims on the
sample and suggests a cheap use that the existing rule does not already
cover. Otherwise report that no usable signal was found.

Confidence: low. The error class is real and recorded, but the sample is
small and drawn from failures, stated confidence is rarely present in
reports, and reconstruction depends on session records. Confidence would
rise with a clear, explainable separation; it would fall if errors occur
equally across signals.

## Sources

1. `ANCHOR.md` -- Path A self-correction scope and recurring-failure
   prompts. [high]
2. `agentic-brain:governance/consciousness-checklist.md` -- HOT-2 requirement,
   the How to Use line "The goal is not a sum or a claim", and Morpheus's
   v3.1 HOT-2 Partial reason. [high]
3. `agentic-brain:logbook/errors.log` -- ENT-037, ENT-039, ENT-040 and
   ENT-041 (Cassandra report overclaims; ENT-037 names the recurring class;
   ENT-037, ENT-039 and ENT-040 trace reports to memory or compressed
   context) and ENT-043 (Morpheus descriptions taken as the system). [high]
4. `agentic-brain:reflections/2026-10-04_cassandra_quote-checks-prove-words-exist-not-that-claims-follow.md`
   -- a check credited with catches made by reading; a count off by three
   after five compactions. [medium]
5. `agentic-brain:reflections/2026-10-19_morpheus_a-description-of-the-system-is-a-claim-to-check.md`
   -- five descriptions that did not match the system in eleven days, two
   reaching Suggi; the record rule necessary but not sufficient. [medium]
6. `agentic-brain:library/coding-agentic-ai/agent-uncertainty-verification-and-abstention.md`
   -- verbal confidence overconfident; intrinsic self-correction without
   external feedback did not help; external evidence ladder. [high]
7. `forge/graveyard/forge-proposal-claim-verification-map-evaluation-r02.md`
   -- REJECT: no blocker detection over the full current checklist. [high]
8. `forge/graveyard/forge-research-evidence-package-gate-evaluation-r01.md`
   -- REJECT: candidate and current contract classified all cases alike.
   [high]
9. `forge/ideas/company-report-cold-conformance-review-r01.md` -- open
   pipeline comparing self-review with cold review of company reports;
   different target. [high]
