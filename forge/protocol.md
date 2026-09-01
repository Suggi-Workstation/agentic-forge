---
name: forge-protocol
id: 20260801T000008Z
tier: protocol
author: Morpheus
approved_by: Suggi
version: 2.0
---
# Forge Protocol -- Researcher and Analyst

## Purpose

The Forge turns one narrow question into one reviewed build. Researcher
creates the work. Analyst challenges it. Each session completes one small
stage in 10-15 minutes and exits.

## Pipeline

| Current stage | Owner | PASS moves to | REVISE moves to |
|:--|:--|:--|:--|
| `ideate` | Researcher | `propose` / Researcher | no artifact; try later |
| `propose` | Researcher | `research` / Researcher | narrow the proposal |
| `research` | Researcher | `evaluate` / Analyst | narrow the proposal |
| `evaluate` | Analyst | `build` / Researcher | `research` / Researcher |
| `build` | Researcher | `verify` / Analyst | return to `research` |
| `verify` | Analyst | `review` / Human | `build` / Researcher |

Analyst may also REJECT at evaluate or verify. Record the verdict, reset
STATUS to `ready`, and leave the immutable chain for future reference.

## Artifact Rule

Files use `<slug>-rNN.md`. The first stage artifact is `r01`; a correction
creates the next revision and names the prior same-stage ID in `supersedes`.
Never edit a completed artifact.

Every artifact uses:

```yaml
---
name: <slug>
id: <YYYYMMDDTHHMMSSZ>
pipeline: <idea r01 id>
research_path: <agent-systems|value-investing-systems>
stage: <idea|proposal|research|evaluation|build|verification>
owner: <Researcher|Analyst>
parent: <immediate parent artifact id or root>
supersedes: <prior same-stage id or none>
confidence: <0.0-1.0>
created: <YYYY-MM-DDTHH:MM:SSZ>
---
```

`parent` always names the artifact directly consumed. A revision requested
by Analyst parents the Analyst verdict that requested it.

## Session Rule

Every role session:

1. Confirm the repository root and current role ownership in `STATUS.md`.
2. Do one stage only. Keep it small enough for 10-15 minutes.
3. Write at most one immutable stage artifact.
4. Update `STATUS.md` and append one complete progress ENT block.
5. Run ASCII and ID checks.
6. Commit only the changed Forge paths as the active role.
7. Exit. The watcher handles publication.

If the role does not own the current stage, exit without writes.

## Researcher Ordering

Researcher reads `ANCHOR.md`, `STATUS.md`, and this protocol first. Then it
runs the blank-page and gap-list steps before reading LEARNINGS, prior
artifacts, brain material, or web sources. This preserves the Feynman order.

## Analyst Ordering

Analyst reads control files and the acceptance criteria in the ancestors,
but not the target body. It writes a short expected-results baseline first,
then reads the research or build and issues PASS, REVISE, or REJECT.

## Learning Cycle

Both roles read `LEARNINGS.md`. Either role may add or strengthen one short
method lesson after its stage when repeated pipeline evidence supports it.
Humans never edit LEARNINGS.

## Scope

- All writes stay inside this repository.
- Read-only brain or web evidence is allowed.
- If an external tool asks to write, repair, clone, rebuild, install, or
  configure anything outside the Forge, skip that action.
- No profile, shared-skill, cron, service, or runtime changes.
- No locks or monitor scripts. The future 30-minute stagger and 15-minute
  session cap prevent role overlap.

## Human Review

Verification PASS sets `state: awaiting-review`, `stage: review`, and
`owner: Human`. The future agents stop. Suggi may later approve, reject, or
request revision through a separate interactive task.