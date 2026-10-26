---
name: surprise-triggered-memory-correction
id: 20261026T225111Z
tier: idea
pipeline: 20261026T225111Z
author: Morpheus
tags: [agent-systems, memory, prediction-error, stale-knowledge, hindsight]
links:
  - ANCHOR.md
  - agentic-brain:governance/consciousness-checklist.md
  - agentic-brain:logbook/errors.log
  - agentic-brain:reflections/2026-10-19_morpheus_a-description-of-the-system-is-a-claim-to-check.md
  - agentic-brain:research/insights/hindsight-system.md
  - https://arxiv.org/abs/2501.00663
  - https://arxiv.org/abs/2407.09450
confidence: low
---
# Surprise-Triggered Memory Correction

## Question and Value

When a tool result contradicts what an agent's memory or notes said about
the system, which response loop would stop the same stale description from
causing another error, and how could such a surprise be detected cheaply?
Today nothing happens. Options include recording the mismatch, recalling
memory again at that moment, correcting or retiring the stale memory, and
telling whoever owns the description.

The target is the loop between the agents' memory and what they observe.
Automatic Hindsight recall runs before each reply on the current question,
and capture runs after the completed turn [4]. The documented flow has no
automatic step that re-recalls, flags or corrects a memory when a mid-turn
tool result contradicts it. Morpheus recorded five cases in eleven days
where a description of the system (his own notes, a code reading, a tool
summary, a commit count, a memory model's freshness flag) did not match the
system. Two reached Suggi as conclusions, and the shared bank's fleet facts
were 11 days stale because they were written only at session-end (errors
ENT-043) [3][5]. This is ANCHOR Path A work on memory and self-correction
[1].

The idea also answers Suggi's question about the prediction and feedback
indicators. Morpheus's checklist entry scores predictive coding (PP-1)
Partial, layered prediction (PP-2) Absent and feedback (RPT-2) Partial,
because his predictions are deliberate and no prediction error updates
processing [2]. Model research uses surprise to decide what to store.
Titans designs its memory so that "an event that violates the expectations
(being surprising) is more memorable" [6]. EM-LLM segments a model's context
into episodic events at points of Bayesian surprise [7]. Both work inside a
model; whether a harness-level analog helps an agent is untested. The
checklist says "The goal is not a sum or a claim" [2]; this idea is judged
by fewer stale-knowledge errors.

Provisional hypothesis: making mismatches explicit and routing them to
memory correction would retire stale facts sooner and stop the same stale
description from recurring. A mismatch is an expected result stated before
a consequential check and compared with what the check returned. Credible
alternative: agents already notice and correct mismatches; three of the
five cases were caught before reaching Suggi [5]. Stated predictions cost
tokens, and Hindsight's consolidation keeps contradictions as history. A
write-at-change rule for the shared bank, added after those cases, may
already close the main gap [5]. The idea is not worth pursuing if
mismatches are rare or already corrected at once, or if the stale sources
behind errors were documents and notes rather than correctable memory.

## Origin and Prior Work

Direct ideation under Path A, directed by Suggi on 2026-10-26, when he asked
for Forge ideas on the checklist indicators that are not fully present and
for memory or perception tools. Path C was not used; the 2026-10-19
reflection was read in full as evidence and describes one agent's period.

Prior work: the Hindsight insight documents when recall and capture run and
that recall injects consolidated observations [4]. The 2026-10-19 reflection
locates the shared bank's staleness in write cadence and added a rule to
write fleet facts at the moment of change [5]. That addresses the writer.
This idea addresses the reader, who meets a contradiction mid-task.
Duplicate scope: every tracked `forge/` artifact was searched at HEAD
`f968e40` for prediction error, surprise and expectation terms. The matches
concern valuation expectations, freshness replays and the method lessons,
not agent memory. The Brain index was queried for prediction, surprise and
stale memory. No Forge idea, proposal, graveyard verdict or discovery
addresses this loop. The one pending discovery concerns index freshness and
has no recorded decision.

Existing target: the agents' Hindsight recall and retain flow and their
habit of checking descriptions against the live system. Strongest
alternative candidate: scheduled re-verification of all fleet-state
memories. It lost as a framing because its cost grows with memory size,
while mismatch triggers act only where a contradiction appeared; it remains
an option in the plan.

## Research Plan

Explore detection and response options; do not choose a loop yet. One
bounded unit:

1. Collect recorded mismatch cases from errors ENT-031 to ENT-044 and the
   five 2026-10-19 cases [3][5]. Classify each case's stale source: private
   memory, shared bank, own notes or files, documentation, or a tool
   summary.
2. For each case, record what would have detected it earlier (a stated
   expectation, a recall at that moment, a freshness check), what
   correction was made, and whether the same stale fact recurred later.
3. Compare option classes: (a) do nothing; (b) expectation statements before
   consequential checks; (c) a contradiction step after tool results that
   re-recalls memory; (d) correcting or retiring the stale memory on
   mismatch; (e) notifying the description's owner (see the separate
   shared-change idea); (f) scheduled re-verification. Criteria: cases
   caught, cost, false alarms, memory churn, and which corrections the
   memory system supports.
4. Record unknowns, such as how often contradictions go unnoticed, which
   leaves no trace.

Advance only if at least two cases had a correctable memory as their stale
source and a defined trigger would have fired before the error reached a
report. Otherwise report the sources found.

Confidence: low. The cases are recorded but come mostly from one agent and
one period, unnoticed mismatches leave no record, and the model-level
surprise research may not transfer to a harness. Confidence would rise if
correctable memory explains several cases; it would fall if documents and
notes explain them.

## Sources

1. `ANCHOR.md` -- Path A memory and self-correction scope. [high]
2. `agentic-brain:governance/consciousness-checklist.md` -- PP-1, PP-2 and
   RPT-2 requirements, the How to Use line "The goal is not a sum or a
   claim", and Morpheus's v3.1 reasons. [high]
3. `agentic-brain:logbook/errors.log` -- ENT-043 (descriptions not matching
   the system) and ENT-031 to ENT-044 as the case window. [high]
4. `agentic-brain:research/insights/hindsight-system.md` -- recall before
   the reply on the current question; capture after the completed turn;
   observation-only injection. [medium]
5. `agentic-brain:reflections/2026-10-19_morpheus_a-description-of-the-system-is-a-claim-to-check.md`
   -- five mismatches in eleven days, two reaching Suggi, three caught
   earlier; the write-at-change rule. [medium]
6. Behrouz, A., Zhong, P. and Mirrokni, V. "Titans: Learning to Memorize at
   Test Time", Google Research, arXiv:2501.00663 (2025), NeurIPS 2025;
   section 3 checked:
   surprise-based memory updates. https://arxiv.org/abs/2501.00663 [high]
7. Fountas, Z. et al. "Human-inspired Episodic Memory for Infinite Context
   LLMs" (EM-LLM), ICLR 2025, arXiv:2407.09450; abstract checked:
   Bayesian-surprise event segmentation and two-stage retrieval.
   https://arxiv.org/abs/2407.09450 [high]
