# Evaluation Template

Use the Artifact Contract in `forge/protocol.md`. Tier: `evaluation`.
Field order: `name`, `id`, `tier`, `pipeline`, `author`, `tags`, `links`,
`confidence`. Every field is mandatory; tags must be nonempty.
Destination: `forge/evaluations/`, or `forge/graveyard/` for REJECT/DEFER.
Link the exact research target, root/current idea, and any prior evaluation.

## Target and Baseline

Name the research path and ID. Record the expected evidence and failure
conditions formed from the assignment before reading the target body.

## Findings

Assess groundedness, coverage, source quality/independence, reasoning,
contradictions, alternatives, and potential usefulness. For each material
finding, cite what was independently checked, explain the consequence, and
state whether it blocks advancement. No mandatory numerical score exists.

## Verdict and Handoff

Choose ADVANCE, REVISE, REFRAME, REJECT, or DEFER under the protocol.
State the exact next stage, decisive reasons, and required evidence
or corrections. Count prior corrective cycles and cite any human extension.
For closure, explain why work stops and what would justify reopening.
ADVANCE means a proposal is justified, not that the idea is approved.
Justify confidence in the verdict with evidence, limitations, and what would change it.

## Learning Decision

State either the supported method lesson/change eligible for the LEARNINGS
admission gate after this evaluation, or why LEARNINGS stays unchanged.
Tentative single-incident observations remain here, not reusable lessons.

## Sources

Use the protocol's Sources Format: a numbered Library-style bibliography
with source-quality labels. External sources use author/organization, title,
known date, checked passage/use, and URL. Repository sources use a backticked
`repo:path` -- brief relevance, with the exact repo prefix for other repos
and an unprefixed path for this repo. Match every body citation to its entry.
This is the final artifact section; do not copy the checklist.

## Checklist -- Before Writing

PASS requires every item; any missing item HALTs the verdict write.

- [ ] Metadata order, exact target, input links, and revision meet the protocol.
- [ ] Nonempty tags and low/medium/high confidence are present; the body justifies confidence.
- [ ] Baseline preceded target-body reading; important sources were checked.
- [ ] Findings identify both supporting and contrary evidence and blockers.
- [ ] Verdict, budget, destination, and next stage agree with the protocol.
- [ ] Closure has a reason and reopening condition; feedback is actionable.
- [ ] Learning decision is explicit and does not invent repeated evidence.
- [ ] Sources follow the protocol's format; repo entries are path-first with ` -- ` relevance, correct prefixes, and verified targets; citations and entries agree.
