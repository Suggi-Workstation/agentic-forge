---
name: context-attention-schema
id: 20261026T225110Z
tier: idea
pipeline: 20261026T225110Z
author: Morpheus
tags: [agent-systems, context, attention, compaction, self-monitoring]
links:
  - ANCHOR.md
  - agentic-brain:governance/consciousness-checklist.md
  - agentic-brain:logbook/errors.log
  - agentic-brain:reflections/2026-10-08_morpheus_a-lesson-binds-where-it-is-read-not-where-it-was-learned.md
  - agentic-brain:reflections/2026-09-23_morpheus_preloading-proves-exposure-not-application.md
  - agentic-brain:library/coding-agentic-ai/context-window-management.md
  - https://www.pnas.org/doi/10.1073/pnas.2102421118
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
confidence: low
---
# Context Attention Schema

## Question and Value

What would an agent need to know about its own context, and how should it
know it, to notice drift and redirect itself? That means what is loaded,
what compaction removed, and which commitments and rules apply to the task
at hand. Candidates range from the existing to-do list and compaction
summary, through context resets with a structured handoff, to a short
attention note the agent keeps and re-reads at risky moments.

The target is the agents' handling of long sessions and compaction. Recorded
failures show that a known lesson fails to act when the work in front of
the agent does not load it. Morpheus broke a rule he had written down twice
because the closing task never asked for it (errors ENT-038) [3][4].
Cassandra's report errors moved between kinds of work [4], and three of her
scars trace reports to memory or compressed context [3]. A Morpheus
audit found that delivering a skill proves exposure, not application [5].
The ideator also observed in his own 2026-10-26 session that compaction
replaced loaded skills with markers he had to notice and reload; that
observation is not yet in a citable record. This is ANCHOR Path A work on
context, memory and self-correction [1].

The idea also answers Suggi's question about the attention indicators
(AST-1, AST-2). Morpheus's checklist entry scores both Partial because his
model of his own attention is kept on purpose and intermittently, not
continuously [2]. Attention schema theory itself suggests why a model of
attention matters. In Wilterson and Graziano's study, a learning agent
trained with an attention schema learned to control its attention, while
an agent trained without one was severely impaired [6]. The checklist says
"The goal is not a sum or a claim" [2]; this idea is judged by fewer missed
rules and less drift.

Provisional hypothesis: part of the drift comes from the agent not knowing
what it currently holds. A short, current attention state, re-read before
closure claims and after compaction, would reduce missed rules. Credible
alternative: drift comes from how the task frames attention (closing versus
diagnosing), not from missing state knowledge. Another note is a rule the
agent will skip like the others, and better compaction or notes kept
outside the context window, which practitioners already use, solve it [8].
The idea is not worth pursuing if recorded failures cannot be traced to
unknown context state, or if existing markers already catch them.

## Origin and Prior Work

Direct ideation under Path A, directed by Suggi on 2026-10-26, when he asked
for Forge ideas on the checklist indicators that are not fully present and
noted that even humans rarely know their own attention. Path C was not used;
the two Morpheus reflections cited above were read in full as evidence, and
they describe one agent's incidents.

The Brain covers context management as a cost and quality problem: masking
versus summarization, and loss of attention to the middle of long contexts
[7]. Anthropic's engineering guidance treats context as a finite resource
and describes compaction, structured note-taking outside the window and
multi-agent architectures as techniques for long tasks [8]. Neither
addresses an agent's model of its own context as a control signal.
Wilterson and Graziano's result comes from a toy visual task with a
reinforcement-learning agent, not a language model. It shows that a schema
can matter for control, not that one would help here [6].

Duplicate scope: every tracked `forge/` artifact was searched at HEAD
`f968e40` for attention, compaction, context-window and context-loss terms.
The two matching artifacts use the words in unrelated senses. The Brain
index was queried for compaction and context tracking. No Forge idea,
proposal, graveyard verdict or discovery addresses agent context state. The
one pending discovery concerns index freshness and has no recorded
decision.

Existing target: the to-do and compaction behaviour of long Hermes sessions
and the post-compaction re-check in the agents' bootstrap rules. Strongest
alternative candidate: tagging inputs with agency and source (HOT-3). It
lost because the harness already tags inputs by source and no failure from
missing tags is recorded.

## Research Plan

Explore what kind of self-knowledge about context would help; do not choose
a mechanism yet. One bounded unit:

1. Classify errors ENT-031 to ENT-044 by cause: context loss or compaction,
   lesson not loaded, wrong path tested, report from memory, other [3].
2. For the context-related cases, reconstruct from session records what the
   agent's context held at the failing moment, where possible, and what it
   would have needed to know.
3. Compare option classes: (a) do nothing; (b) to-do list discipline; (c) a
   post-compaction re-check; (d) a short attention note covering goal,
   loaded rules, dropped items and open claims; (e) context resets with a
   structured handoff; (f) an index from task type to the lessons that bind
   it. Criteria: would it have caught the case, cost per turn, and whether
   it acts automatically or depends on the agent remembering.
4. Record unknowns, such as how Hermes marks dropped context today.

Advance only if at least two recorded failures plausibly turn on unknown
context state, and at least one option acts without relying on the agent's
memory to invoke it. Otherwise report the causes found.

Confidence: low. The failure records are real, but their causes are mixed,
the self-observation is uncited, and the attention-schema evidence comes
from a very different system. Confidence would rise if context state
explains several failures; it would fall if task framing explains them.

## Sources

1. `ANCHOR.md` -- Path A context, memory and self-correction scope. [high]
2. `agentic-brain:governance/consciousness-checklist.md` -- AST-1 and AST-2
   requirements, the How to Use line "The goal is not a sum or a claim", and
   Morpheus's v3.1 Partial reasons. [high]
3. `agentic-brain:logbook/errors.log` -- ENT-038 (rule written twice, broken
   at closure) and ENT-037, ENT-039 and ENT-040 (reports from memory or
   compressed context). [high]
4. `agentic-brain:reflections/2026-10-08_morpheus_a-lesson-binds-where-it-is-read-not-where-it-was-learned.md`
   -- lessons act where the work loads them; errors moving between kinds of
   work. [medium]
5. `agentic-brain:reflections/2026-09-23_morpheus_preloading-proves-exposure-not-application.md`
   -- delivery of a skill proves exposure, not application. [medium]
6. Wilterson, A. I. and Graziano, M. S. A. "The attention schema theory in a
   neural network agent: Controlling visuospatial attention using a
   descriptive model of attention", PNAS 118(33), e2102421118, 2021;
   abstract and experiments 2 and 3 checked: the schema greatly improved
   control and learning. https://www.pnas.org/doi/10.1073/pnas.2102421118
   [high]
7. `agentic-brain:library/coding-agentic-ai/context-window-management.md` --
   masking versus summarization, lost-in-the-middle, per-task tuning.
   [medium]
8. Anthropic. "Effective context engineering for AI agents", engineering
   blog, 2025-09-29; compaction and structured note-taking sections checked.
   https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
   [high]
