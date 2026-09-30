---
name: forge-discover
description: "Use when condensing a READY proposal into a Forge discovery."
user-invocable: false
disable-model-invocation: false
---
# Forge Discover

Write the one file Suggi decides on. It condenses the proposal that passed
final review; it is not a new proposal and not an approval. Run through
`forge-loop-research` at `discover`. Read `forge/protocol.md` and
`governance/template-discovery.md` before writing.

## Procedure

1. Read the selected STATUS row's input: the READY final review. Read the
   exact proposal it names and the root idea. HALT if the review is not
   READY, names a different proposal revision, or the proposal author is
   not eligible under the protocol's stage-independence rule.
2. Condense the proposal under the template. Take every statement from the
   proposal or the final review. Add no change, claim, scope, evidence, or
   opinion, and keep every limitation and unmeasured benefit. If the
   proposal cannot be condensed faithfully, HALT and record why; do not
   fix it here.
3. Write one file in `forge/discoveries/` with the protocol's ordered
   metadata and Sources Format. Return it to the loop for the
   `human-review` handoff.

## Verification

Before writing, PASS requires the READY review for this exact proposal and
the template checklist. After writing, every statement traces to the
proposal or review. Otherwise HALT the write. LEARNINGS is read-only here;
no runtime change and no implementation occur.
