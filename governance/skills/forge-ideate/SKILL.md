---
name: forge-ideate
description: "Create one scoped Forge research idea."
user-invocable: false
disable-model-invocation: false
---

# Forge Ideate -- Researcher Stage 1

Creates one narrow research question from one optional anchor path. It does
not create an artifact merely to keep a cron run busy.

## When to Use

Use only when `STATUS.md` says `state: ready`, `stage: ideate`, and
`owner: Researcher`. Otherwise return `NO-OP` without writes.

## Procedure

1. Read the startup context required by `forge/protocol.md` and
   `governance/skills/forge-ideate/assets/template.md`.
2. Invoke `forge-loop-feynman`. Generate candidate questions from the two
   anchor paths before searching prior work.
3. Search `forge/`, graveyard, and `LEARNINGS.md` for overlap. Optionally use
   read-only `query-brain-vps`, then read relevant returned files. Use web
   search only to establish that evidence is likely available.
4. Compare candidates by importance, non-duplication, falsifiability,
   evidence availability, and whether one reviewable build can answer them.
5. Choose exactly one path and one question. Do not alternate paths by quota
   and do not open parallel pipelines.
6. If no candidate passes, return `NO-OP` with no artifact, status change, or
   log entry.
7. Generate the current UTC ID with `date -u +'%Y%m%dT%H%M%SZ'`. Write
   `forge/ideas/<slug>-r01.md` from the template. Its `pipeline` equals its
   `id`, `parent` is `root`, and `supersedes` is `none`.
8. Return artifact path, ID, path choice, and a concise gate reason to
   `forge-loop-researcher`. The loop owns status, logbook, validation, and
   commit.

## Idea Gate -- HARD GATE

PASS only when the question:

- belongs to exactly one current anchor path;
- is not a renamed duplicate of prior Forge or brain work;
- is falsifiable and names what evidence could reverse it;
- is narrow enough for one bounded proposal, research run, and build;
- has a plausible implementation or framework output; and
- has explicit kill criteria.

Any missing condition is HALT with no idea artifact. Candidate rejection is
not a graveyard event because no pipeline exists yet.

## Related

- `governance/skills/forge-ideate/assets/template.md`
- `governance/skills/forge-loop-researcher/SKILL.md`
- `governance/skills/forge-propose/SKILL.md`
- `ANCHOR.md`