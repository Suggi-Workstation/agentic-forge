---
name: anchor
id: 20260812T171239Z
tier: control
author: Suggi
approval_locked: true
approved_by: Suggi
---
# ANCHOR.md -- Eternal Forge Direction

## Mission

The Forge improves how agents research, reason, collaborate, learn, and
build useful systems. A successful pipeline ends in one evidence-backed
proposal for Suggi to decide on, not an automatic implementation. Stopping
an unsupported idea is also a useful result.

Each new idea starts from one path below. Paths A and B are subjects; Path C
is a discovery method that must lead to an A or B subject. Helper questions
are prompts for finding a lead, not a checklist to answer in full.

## Path A -- Agent Systems

Questions may improve:

- agent design, harnesses, context, memory, tools, and architecture;
- agent skills, self-correction, learning, and long-term growth;
- collaboration across research, evaluation, and proposal workflows;
- shared-brain quality, retrieval, observability, and coordination;
- practical methods used by strong AI labs and agent builders.

Helper questions:

- Where do agents repeatedly fail, stall, retry, or need Suggi's correction?
  Check logbook errors, evaluations, and graveyard verdicts.
- Which skill, template, protocol, or Brain insight is unclear, stale,
  duplicated, contradicted by current practice, or longer than it needs to be?
- Which confirmed `LEARNINGS.md` lesson should become a skill, template, or
  protocol change?
- Which proven method from strong AI labs or agent builders would remove a
  known failure here, and what would adopting it cost?

## Path B -- Value-Investing Systems

Questions may improve:

- Buffett and Munger style value-investing principles and process;
- circle of competence, business quality, moat, management, risk,
  intrinsic value, margin of safety, and capital allocation;
- accounting quality, owner earnings, and financial-shenanigan detection;
- how agents collect, challenge, and synthesize investing evidence;
- repeatable valuation frameworks, checklists, models, and skills.

Helper questions:

- Which step of the investing process -- screening, business analysis,
  valuation, or portfolio review -- relies on judgment that a clearer
  framework, checklist, or worked example could make repeatable?
- Where did a company report in `investing-hub:companies/` leave a decision
  unresolved, inconsistent, or dependent on a fragile assumption?
- Which Buffett or Munger principle in `agentic-brain:library/` lacks a
  practical test in `investing-hub:frameworks/`?
- Which common accounting or valuation error would the current frameworks
  fail to catch?

This path builds research systems and frameworks. It does not produce an
automatic security recommendation or portfolio action.

## Path C -- Reflection-Led Discovery

Use agent reflections in `agentic-brain:reflections/` to discover research
questions. Follow the caller's chosen reflections, topic, agent, or period;
otherwise take a genuinely random, bounded sample. Use `query-brain-vps` to
find related reflections and investigate overlapping accounts. Read selected
reflections in full before extracting a lead.

Helper questions:

- Was the reflection's actionable change implemented, and did it work?
- Which problem, friction, or surprise recurs across different agents or
  incidents?
- Which success could transfer to another agent, workflow, or path?
- Where do reflections disagree about a cause or a fix?

Separate observations from interpretations, check current evidence, and do
not mistake repeated accounts of one incident for independent confirmation.
A reflection supplies a hypothesis, not proof or permission to change the
system. Name the lead's subject, A or B, explain why it is worth pursuing
over overlapping leads, and cite its origins.

## Selection Rule

- No path has a quota; subject paths do not alternate mechanically.
- Read `LEARNINGS.md` at ideation, before choosing a question.
- Check `forge/graveyard/`, `forge/ideas/`, and `forge/proposals/`, including
  accepted and pending proposals and their recorded human decisions.
- Search existing Brain knowledge before starting new research.
- For every path, consider improving, correcting, simplifying, or extending
  existing files, skills, and frameworks before creating new ones. Existing
  coverage is not a reason to reject a concrete improvement. Identify the
  target, the specific gap, and how the proposed change would help.
- Prefer the candidate that best meets all of these:
  - observed evidence of a real problem or opportunity, not only a
    plausible risk;
  - a named target that a proposal would change;
  - decisive evidence obtainable with the available tools and sources;
  - a result that could change a decision compared with the simplest
    existing approach or doing nothing;
  - a first test small enough for one research stage.
- Name the strongest alternative candidate considered and why it lost.
- Choose one narrow, unresolved question; do not rename prior work as new.
  Reopening needs new evidence or a changed prerequisite.
- If no worthwhile question exists, do nothing and try again next session.

## Required End State

A successful pipeline produces one file in `forge/proposals/` containing:

- the decision or improvement proposed;
- evidence and contradictions;
- concrete changes, alternatives, and a simple implementation plan;
- tests, failure cases, and rollback;
- uncertainties and questions for Suggi.

Final review checks the actual proposal before it reaches Suggi. Outputs
may be skills, architecture blueprints, frameworks, or proposed core-file
and rule amendments, including simplification or removal. Approval and
implementation are separate decisions. Forge loops never implement their
proposals or edit this anchor; changes to direction require Suggi.
