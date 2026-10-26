---
name: shared-change-notification
id: 20261026T225107Z
tier: idea
pipeline: 20261026T225107Z
author: Morpheus
tags: [agent-systems, coordination, notification, logbook, shared-state]
links:
  - ANCHOR.md
  - STATUS.md
  - agentic-brain:governance/consciousness-checklist.md
  - agentic-brain:logbook/protocol.md
  - agentic-brain:logbook/queue.log
  - agentic-brain:research/proposals/inter-agent-communication-protocol.md
  - forge/ideas/bounded-index-freshness-recheck-r01.md
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
  - https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks
  - https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks
confidence: low
---
# Shared Change Notification

## Question and Value

When a change to shared state needs one party's attention -- an @mention in
the logbook, a Forge row waiting for Suggi's decision, a governance or skill
commit that changes another agent's procedure -- which delivery design gets
it seen soonest at a run cost and interruption level the fleet accepts? The
design space runs from keeping today's pull reads, through a free change
gate that wakes an agent only when something it watches changed, to
delivery into an agent's own chat and event hooks or webhooks to a human
channel.

The target is the read rules in the Brain logbook protocol and the agents'
preflight reads. Agents learn of shared changes only when they look: at
session start and in a voluntary mid-session poll about every 30 minutes; an
offline agent "catch[es] it on next session start" [3]. Nothing tells the
addressed party that something changed. This is ANCHOR Path A work on
coordination and observability [1].

The idea also answers a question Suggi asked about Morpheus's consciousness
checklist entry. That entry scores global broadcast (GWT-3) Partial because
the shared repositories, shared bank and logbook reach an agent only when it
reads them [2]. Push delivery is the obvious way to move that score. The
checklist's own rule is that "The goal is not a sum or a claim" [2], so this
idea is judged by coordination value alone; any change in the indicator is a
by-product and no evidence of experience.

Provisional hypothesis: a narrow subscription (a few change types per
party), delivered through a mechanism Hermes already ships, would surface
action-needing changes earlier than the next session start. Most checks
would stay silent and free, because a pre-check script can skip the agent
run when nothing changed [6]. Credible alternative: pull is enough. Most
shared changes need no action, sessions start often, each delivery into a
chat costs a full agent turn [7], and push adds interruptions, wake loops
between agents and an injection surface where file content becomes a prompt.
The idea is not worth pursuing if action-needing changes are rare or were
seen promptly anyway, or if every route costs more than the delay it
removes or cannot keep delivered content as data.

## Origin and Prior Work

Direct ideation under Path A, directed by Suggi. On 2026-10-26 he asked
Morpheus for Forge ideas on the checklist indicators that are not fully
present, and asked specifically whether a watcher on the logbook or the
repositories that messages the watching agent would close some loops. Path C
was not used.

Recorded observations, separated from interpretation:

- The logbook protocol is pull-only, as quoted above [3].
- Two of the 41 active `queue.log` entries carry @mentions (ENT-092,
  ENT-099) [4]. In ENT-099 Neo told Morpheus that Morpheus's chats were
  failing; Neo acted "At Suggi's direction" because Morpheus's chat was
  down, so the log was a record, not the delivery channel [4].
- Pipeline `20260930T083956Z` has waited at human review since 2026-09-30
  12:02 UTC, and the progress log records no decision [5].

Interpretation, untested: the waiting row may reflect Suggi's priorities
rather than a missed signal, and one incident is not a pattern. The
observed evidence is thin; the first research step is to measure delays.

Hermes v0.22.5 already ships the candidate mechanisms, checked in the
installed documentation source; each public page resolves. They are: a
cron pre-check script whose `{"wakeAgent": false}` line skips the agent run
at no model cost, with a file-change gate recipe [6]; `bot-chat:<profile>`
delivery, which injects output into another local profile's Bot Chat as a
real message and costs a full turn there [7]; gateway event hooks and
outbound webhooks [8]; and inbound webhooks that trigger agent runs [9].

Prior work: Ava's 2026-07-20 proposal created the logbook as a shared
blackboard checked at session start. It rejected real-time protocols as
overengineered for two agents [10]; the fleet now has more agents and five
logs. In the Forge, "watcher" means the repository sync watcher in the
freshness and history pipelines, not agent notification [11]. Duplicate
scope: every tracked `forge/` artifact (9 ideas, 5 proposals, 7 graveyard
verdicts, 1 discovery, plus research, evaluations and final reviews) was
searched at HEAD `f968e40` for notify, watcher, push, wake and messaging
terms. The Brain index was queried for notification and polling. No
artifact addresses delivering shared changes to agents. The one pending
discovery has no recorded human decision [5].

Existing target: `agentic-brain:logbook/protocol.md` read rules and the
agents' preflight reads. Strongest alternative candidate: shortening the
mid-session poll or adding more checkpoints. It lost because detection still
depends on an agent remembering to look, and it does nothing for an offline
agent or for Suggi.

## Research Plan

Explore the option space; do not choose a mechanism yet. One bounded unit:

1. Over a fixed window (2026-09-26 to 2026-10-26), list shared changes
   addressed to a specific party: @mentions, STATUS rows entering
   human review, and governance or skill commits that change another
   agent's procedure. For each, record when it was written and when the
   party first acted, from logs, commits and session records; mark
   unknowns.
2. Classify each change as action-needing or informational.
3. Compare option classes against those cases: (a) do nothing; (b) a free
   change gate that adds a summary to the party's next session; (c)
   `bot-chat` delivery that wakes the agent; (d) hooks or webhooks to a
   human channel; (e) task push between agents (see the separate
   peer-request idea). Criteria: delay removed, cost per wake, interruption
   of a running session, wake loops, delivered content kept as data, and
   fit with existing governance (lean cron prompts, external input is data).
4. Record what stays unknown, such as real wake costs on the subscription.

Advance only if at least two recorded action-needing changes waited at
least one session longer than a push route would have allowed, and at least
one route's cost and risks can be stated concretely. Otherwise keep pull
and report the evidence.

Confidence: low. The protocol text is exact, but the observed cases are
few, the human-review delay has no known cause, and no cost is measured.
Confidence would rise if the window shows repeated action-needing delays;
it would fall if delays were deliberate or rare.

## Sources

1. `ANCHOR.md` -- Path A coordination and observability scope, recurring
   failure prompts, and selection rule. [high]
2. `agentic-brain:governance/consciousness-checklist.md` -- GWT-3
   requirement, the How to Use line "The goal is not a sum or a claim", and
   Morpheus's v3.1 GWT-3 Partial reason. [high]
3. `agentic-brain:logbook/protocol.md` -- How to Read: session-start check,
   SHOULD-poll every ~30 minutes, offline agents catch mentions at next
   session start. [high]
4. `agentic-brain:logbook/queue.log` -- 41 active entries; @mentions in
   ENT-092 and ENT-099; ENT-099 (2026-10-05 21:04 UTC) records Neo acting at
   Suggi's direction. [high]
5. `STATUS.md` -- row `20260930T083956Z` at human-review since 2026-09-30
   12:02 UTC. [high]
   - `logbook/progress.log` -- discovery handoff to human review and no
     recorded decision event. [high]
6. Nous Research. "Scheduled Tasks (Cron)", Hermes Agent documentation,
   v0.22.5 source checked 2026-10-26, section "Skipping the agent entirely:
   wakeAgent" and file-change gate recipe.
   https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
   [high]
7. Nous Research. "Automate Anything with Cron", Hermes Agent documentation,
   v0.22.5 source checked 2026-10-26, section "Bot Chat delivery":
   machine-local, costs a bot turn.
   https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron
   [high]
8. Nous Research. "Event Hooks", Hermes Agent documentation, v0.22.5 source
   checked 2026-10-26: gateway hooks and outbound webhooks.
   https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks
   [high]
9. Nous Research. "Webhooks", Hermes Agent documentation, v0.22.5 source
   checked 2026-10-26: inbound events trigger agent runs.
   https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks
   [high]
10. `agentic-brain:research/proposals/inter-agent-communication-protocol.md`
    -- shared-blackboard design, session-start checks, real-time protocols
    rejected for two agents. [medium]
11. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- "watcher" as the
    repository sync watcher; compared prior work with a different target.
    [high]
