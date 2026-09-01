---
name: forge-verify
description: "Orchestrate maker-checker verification: an independent reviewer (different model, zero shared context) checks a forge artifact cold and renders APPROVE, FLAG, or REJECT."
user-invocable: false
disable-model-invocation: false
---

# Forge-Verify -- Maker-Checker Orchestration

## What This Skill Does

Orchestrates independent verification of a forge artifact. The checker
must be a separate agent (different model, zero shared context) or, in
the absence of a dedicated verifier agent, a cold independent review
by the invoking agent itself -- never the author's warm self-check.
This skill handles orchestration only; the verdict is rendered by an
independent pass over the artifact.

## When to Invoke

Invoked automatically by forge-loop step 8 after every forge stage
commit. Can also be invoked manually by Suggi.

## Procedure

### 1. Identify the Target

The forge-loop passes the path to the newly committed forge artifact
and the workspace it lives in.

### 2. Spawn an Independent Reviewer

If a dedicated verifier agent is configured, spawn it with
instructions:

> Verify the artifact at `<artifact-path>` in workspace
> `Suggi-Workstation/<workspace>`.
> Render APPROVE, FLAG, or REJECT. Append verification block.
> Commit and push.

The reviewer agent must:
- Run in its own workspace (isolated from the author)
- Use a different model than the author
- Have zero access to the author's session context
- Read the artifact cold from the GitHub repo
- Append a verification block (verdict + reasoning), commit, push

If no dedicated verifier agent exists, fall back to a COLD READ:
the author re-reads the artifact as an independent reviewer would --
fresh eyes, checking against the stage template, answering: does this
artifact meet the stage's PASS criteria? Does it fabricate anything?
Is the provenance chain intact? Render APPROVE, FLAG, or REJECT
explicitly.

### 3. Read the Verdict

After the reviewer completes, read the artifact to extract the
verdict from the appended verification block. Pass the verdict
back to forge-loop for logging.

## Related

- `forge/protocol.md` -- pipeline specification
- `skills/forge-loop/SKILL.md` -- invokes this skill
- `governance/skills/forge-*/SKILL.md` -- the stage skills this gate verifies
