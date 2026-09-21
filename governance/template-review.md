# Final Review Template

Use the Artifact Contract in `forge/protocol.md`. Tier: `review`.
Field order: `name`, `id`, `tier`, `pipeline`, `author`, `tags`, `links`,
`confidence`. Omit optional `tags`/`confidence` without reordering the rest.
Destination: `forge/evaluations/`, or `forge/graveyard/` for REJECT/DEFER.
Link the exact proposal, its research/evaluation, root/current idea, and
prior review where present. Review the proposal, not only its research.

## Target and Baseline

Name the exact proposal path and ID. Record expected design requirements
and failure conditions before reading the proposal body, using the idea,
evaluated research, and required corrections as the baseline.

## Findings

Check responses to evaluation, exact changes, feasibility/dependencies,
scope drift, unsupported new claims, acceptance/negative/regression checks,
worst failure, and reversal. Cite checked sources and affected definitions;
do not invent test execution. Distinguish blocking issues from suggestions.

## Verdict and Handoff

Choose READY, REVISE, REFRAME, REJECT, or DEFER under the protocol.
READY names this exact proposal for Suggi and grants no approval. REVISE
specifies research for evidence gaps or propose for design-only fixes.
State next stage, prior corrective-cycle count and any human extension,
required changes, or the reason and reopening condition for closure.

## Learning Decision

State the supported method change eligible for LEARNINGS after final
review, or the reason for leaving it unchanged. Follow its admission gate;
reviewing one incident twice does not establish repeated independent evidence.

## Sources

Use the protocol's Sources Format: a numbered Library-style bibliography
with author/organization, title, known date, checked passage/use, URL or
repository path, and source-quality label. Match every body citation to
its entry. This is the final artifact section; do not copy the checklist.

## Checklist -- Before Writing

PASS requires every item; any missing item HALTs the verdict write.

- [ ] Metadata order, exact target, links, and revision meet the protocol contract.
- [ ] Cold baseline and independently checked findings concern this proposal.
- [ ] All material objections, design additions, and scope changes assessed.
- [ ] READY has no unresolved blocker and grants no implementation authority.
- [ ] Other verdicts name an actionable route within budget or a closure.
- [ ] Learning decision follows LEARNINGS; previous artifacts stay unchanged.
- [ ] Sources follow the numbered bibliography format; citations and entries agree.
