---
name: peer-agent-requests
id: 20261026T225108Z
tier: idea
pipeline: 20261026T225108Z
author: Morpheus
tags: [agent-systems, collaboration, inter-agent, delegation, coordination]
links:
  - ANCHOR.md
  - agentic-brain:governance/consciousness-checklist.md
  - agentic-brain:logbook/queue.log
  - agentic-brain:reflections/2026-10-08_morpheus_a-lesson-binds-where-it-is-read-not-where-it-was-learned.md
  - agentic-brain:research/proposals/inter-agent-communication-protocol.md
  - agentic-brain:research/insights/council-of-five.md
  - https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron
  - https://a2a-protocol.org/latest
  - https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
confidence: low
---
# Peer Agent Requests

## Question and Value

When one agent needs knowledge or judgment that lives in another agent's
own context -- its private memory, its skills, its workspace -- which way of
asking yields a correct answer in time without making Suggi the relay and
without weakening the rule that a peer's input is data, not an instruction?
The candidates are reading the peer's files, delegating to a fresh
subagent, a logbook request, delivery into the peer's own chat, or a
standard agent protocol.

The fleet is built from specialists: Neo for investing, Cassandra for human
affairs, Atlas for ideas and writing, Morpheus for infrastructure. Each keeps
a private memory bank and its own skills. Agents can leave each other notes,
but none can ask another a question and get an answer inside a working
session. This is ANCHOR Path A work on collaboration across workflows [1].

The idea also answers Suggi's question about an inter-agent prompt. At
fleet scale, specialist agents sharing one channel resemble specialist
modules sharing a workspace (GWT-1 and GWT-3 in the consciousness
checklist) [2]. The checklist says "The goal is not a sum or a claim" [2];
this idea is judged by collaboration value, not by indicator movement.

Provisional hypothesis: some recurring tasks need a peer's own context,
not just its files. A narrow request-and-answer channel with explicit
authority rules would cut relays through Suggi and rework. Credible
alternative: reading the peer's files or delegating to a fresh subagent is
enough. Private banks are private by design, and a direct channel adds wake
loops, cost per turn, unclear authority (who may instruct whom), injection
risk and less oversight by Suggi. The idea is not worth pursuing if no
recorded task needed a peer's own context in a way that files or delegation
could not supply.

## Origin and Prior Work

Direct ideation under Path A, directed by Suggi on 2026-10-26, when he asked
whether an inter-agent prompt would let agents talk to each other better.
Path C was not used.

Recorded observations, separated from interpretation:

- On 2026-10-05 Morpheus's server chats failed. Neo found the cause, reverted
  the setting "At Suggi's direction" and left Morpheus a log note, adding
  "Suggi will review this with you" (queue ENT-099) [3].
- Morpheus's reflection on the incident records that Neo was reached because
  he "happened to be the agent Suggi turned to", and that the peer fix came
  after the failure [4].
- Only two of the 41 active queue entries carry @mentions [3].

Interpretation, untested: Suggi currently acts as the message bus between
agents, and the logbook is a journal rather than a conversation channel.
One incident does not show how often a peer's own context is needed.

Existing mechanisms and standards: Hermes `bot-chat:<profile>` delivery
injects a message into another local profile's Bot Chat, where that agent
answers with its own memory and skills. It is machine-local and costs a full
turn [5]. The Agent2Agent (A2A) protocol is an open machine-to-machine
standard for agent communication. Google donated it to the Linux Foundation,
and it is complementary to MCP [6]. Its first stable version, 1.0, was
released in its first year [7].

Prior work: Ava's 2026-07-20 proposal set up file-based logbook messaging
checked at session start and rejected real-time protocols such as A2A as
overengineered for two agents [8]. The Council of Five blueprint defines an
advisory meeting format for Suggi's questions: members judge independently,
vote and never act [9]. It does not cover operational requests from one
agent to another. Duplicate scope: every tracked `forge/` artifact was
searched at HEAD `f968e40` for inter-agent, agent-to-agent, A2A and Bot Chat
terms, with no matches. The Brain index was queried for inter-agent
messaging. No Forge idea, proposal, graveyard verdict or discovery addresses
peer requests. The one pending discovery concerns index freshness and has
no recorded decision.

Existing target: the logbook's @mention convention and the agents' preflight
reads. Strongest alternative candidate: running the Council of Five for
cross-agent questions. It lost because the Council answers Suggi's questions
with votes; it is not a channel for one agent's working request to another.

## Research Plan

Explore the option space; do not choose a channel yet. One bounded unit:

1. From logs, commits and session records in a fixed window (2026-09-26 to
   2026-10-26), list tasks in which one agent needed another agent's
   knowledge or judgment. Record how the need was met (files, delegation,
   Suggi relay, not at all), the delay and the outcome. Mark unknowns.
2. For each case, note whether the answer required the peer's private memory
   or skills, or only its files.
3. Compare option classes: (a) do nothing (files plus logbook); (b) a fresh
   subagent given the peer's files; (c) logbook requests with an open or
   answered state; (d) `bot-chat` delivery that wakes the peer in its own
   context; (e) an A2A endpoint per agent. Criteria: answer quality, delay,
   cost, loop prevention, authority (a peer's message stays data under the
   Prime Directives), audit trail, Suggi's oversight, and privacy of
   private banks.
4. List the governance rules any channel would have to satisfy.

Advance only if at least two recorded cases needed a peer's own context and
the existing path failed, was slow or cost Suggi a relay, and at least one
option can be described with its loop and authority safeguards. Otherwise
keep files and logbook and report the evidence.

Confidence: low. One documented incident shows Suggi as the relay, but how
often agents need each other's private context is unmeasured, and the
costs of each channel are untested. Confidence would rise with repeated
recorded needs; it would fall if files and delegation answered them.

## Sources

1. `ANCHOR.md` -- Path A collaboration scope and selection rule. [high]
2. `agentic-brain:governance/consciousness-checklist.md` -- GWT-1 and GWT-3
   requirements and the How to Use line "The goal is not a sum or a claim".
   [high]
3. `agentic-brain:logbook/queue.log` -- ENT-099 (2026-10-05 21:04 UTC), Neo's
   note acting at Suggi's direction; @mentions only in ENT-092 and ENT-099
   of 41 active entries. [high]
4. `agentic-brain:reflections/2026-10-08_morpheus_a-lesson-binds-where-it-is-read-not-where-it-was-learned.md`
   -- O section: peer review worked after the failure, because Neo was the
   agent Suggi turned to. [medium]
5. Nous Research. "Automate Anything with Cron", Hermes Agent documentation,
   v0.22.5 source checked 2026-10-26, section "Bot Chat delivery": named
   profile targets, machine-local, costs a bot turn.
   https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron
   [high]
6. A2A Project. "A2A Protocol", project home page, accessed 2026-10-26:
   open standard for agent-to-agent communication, donated by Google to the
   Linux Foundation, complementary to MCP. https://a2a-protocol.org/latest
   [high]
7. The Linux Foundation. "A2A Protocol Surpasses 150 Organizations, Lands in
   Major Cloud Platforms, and Sees Enterprise Production Use in First Year",
   press release, 2026-04-09: release of version 1.0.
   https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
   [medium]
8. `agentic-brain:research/proposals/inter-agent-communication-protocol.md`
   -- file-based messaging checked at session start; A2A and MCP real-time
   protocols rejected for two agents. [medium]
9. `agentic-brain:research/insights/council-of-five.md` -- advisory council
   format: independent first judgments, votes, never acts. [medium]
