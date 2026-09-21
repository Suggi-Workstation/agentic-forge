# Research Template

Use the Artifact Contract in `forge/protocol.md`. Tier: `research`.
Field order: `name`, `id`, `tier`, `pipeline`, `author`, `tags`, `links`,
`confidence`. Every field is mandatory; tags must be nonempty.
Destination: `forge/research/`. Link the root/current idea, any prior
research revision, and the feedback that this report addresses.

## Question and Method

Name the exact idea and questions investigated. Explain source selection,
checks actually performed, limitations, and alternatives considered.

## Evidence and Findings

For each important claim, identify the checked source path/URL, source date
or access date where appropriate, relevant passage/result, and what it
supports or contradicts. Distinguish facts, inferences, and unknowns.
Discuss source independence, quality, coverage gaps, and contrary evidence.
Citations must support the actual claim, not merely mention the subject.

## Alternatives and Implications

Compare available solutions, smaller changes, and doing nothing. Explain
what follows from the evidence and what does not. Negative results are
valid; separate insufficient evidence from evidence against the hypothesis.
Use value-investing principles for investing questions.

## Response to Feedback and Remaining Questions

Answer each material evaluation/review finding with evidence, a correction,
or a reasoned disagreement. Mark unresolved blockers and decision-relevant next
questions. On the first report, say no prior evaluation exists. Explain the
mandatory confidence's evidence, limitations, and what would change it.

## Sources

Use the protocol's Sources Format: a numbered Library-style bibliography
with source-quality labels. External sources use author/organization, title,
known date, checked passage/use, and URL. Repository sources use a backticked
`repo:path` -- brief relevance, with the exact repo prefix for other repos
and an unprefixed path for this repo. Match every body citation to its entry.
This is the final artifact section; do not copy the checklist.

## Checklist -- Before Writing

PASS requires every item; any missing item HALTs artifact creation.

- [ ] Metadata order and exact input/revision links meet the protocol contract.
- [ ] Nonempty tags and low/medium/high confidence are present; the body justifies confidence.
- [ ] Investigated questions and reproducible source checks are documented.
- [ ] Consequential claims are independently supported or explicitly unknown.
- [ ] Contradictions, source dependence, alternatives, and limitations appear.
- [ ] Every material feedback item has an explicit response or blocker.
- [ ] No invented sources, performed tests, approval, or learning edit.
- [ ] Sources follow the protocol's format; repo entries are path-first with ` -- ` relevance, correct prefixes, and verified targets; citations and entries agree.
