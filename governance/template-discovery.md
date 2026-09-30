# Discovery Template

Use the Artifact Contract in `forge/protocol.md`. Tier: `discovery`.
Field order: `name`, `id`, `tier`, `pipeline`, `author`, `tags`, `links`,
`confidence`. Every field is mandatory; tags must be nonempty.
Destination: `forge/discoveries/`. Link the exact READY final review, the
proposal it passed, and the root idea.

A discovery is the one file Suggi decides on. It condenses the exact proposal
that passed final review; it adds no new change, claim, scope, or evidence.
Keep it short: about one page. The proposal and its chain remain the record.

## Decision

The exact change requested, in one or two sentences, and the decision
Suggi is asked to make.

## What Changes

The affected files or interfaces, current behavior, and intended behavior.
Quote exact wording where the proposal supplies it.

## Why

The problem, the decisive evidence, and the alternatives rejected, in plain
words. Carry over every limitation and unmeasured benefit stated in the
proposal or final review; do not soften them.

## How to Apply and Reverse

The ordered implementation steps, the acceptance check, and the rollback,
as the proposal specifies them. State that implementation is separately
authorized work.

## Confidence

Carry over the proposal's confidence and what would change it.

## Sources

Use the protocol's Sources Format. The proposal, final review, and root idea
are required entries; add only sources the proposal itself cites.

## Checklist -- Before Writing

PASS requires every item; any missing item HALTs the discovery write.

- [ ] The linked final review is READY for the exact proposal condensed here.
- [ ] Every statement traces to the proposal or final review; nothing new.
- [ ] Every limitation and unmeasured benefit from those files is retained.
- [ ] Rollback and separate implementation authorization are stated.
- [ ] Sources follow the protocol's format; citations and entries agree.
