---
name: forge-verify
description: "Verify a Forge build package as the Analyst."
user-invocable: false
disable-model-invocation: false
---

# Forge Verify -- Analyst Stage 6

Independently verifies one Researcher build package. It produces an
immutable verdict artifact; it never edits the build it checks.

## When to Use

Use only when `STATUS.md` says `stage: verify`, `owner: Analyst`, and names
a build in `forge/builds/`. Otherwise return `NO-OP` without writes.

## Preconditions -- HARD GATE

- [ ] The Analyst loop holds the Forge lease. (PASS / HALT)
- [ ] The tree was clean before this run. (PASS / HALT)
- [ ] Build and complete parent chain resolve inside this repo. (PASS / HALT)
- [ ] The build is not already superseded or verified. (PASS / HALT)

## Procedure

1. Read `governance/skills/forge-verify/assets/template.md` and the startup
   context required by `forge/protocol.md`.
2. Before judging the build body, extract the accepted research claims and
   acceptance tests from the proposal, research, and evaluation artifacts.
   This is the comparison baseline.
3. Read the build cold. Check every material claim against the research
   citation that allegedly supports it. Read the cited source when the
   chain does not contain enough evidence to verify representation.
4. Test internal consistency: recommendation, design, sequence, tests,
   risks, rollback, and limitations must agree. Identify the worst plausible
   failure and whether the package structurally prevents or contains it.
5. Check confinement. The package may recommend future changes elsewhere,
   but this Forge run may create no external write or implementation.
6. Render exactly one verdict:
   - `PASS`: every material claim is traceable; the design is coherent,
     testable, bounded, and review-ready.
   - `HALT-REVISE`: name each failed criterion and return stage (`build`,
     `research`, or `propose`).
   - `HALT-REJECT`: the premise is false, unsafe, non-actionable, or cannot
     be repaired without becoming a different pipeline.
7. Generate the current UTC ID with `date -u +'%Y%m%dT%H%M%SZ'`. Write one
   new `forge/verifications/<slug>-rNN.md` from the template. Never append a
   verdict to the build and never edit an older verification.
8. Return the artifact path, ID, verdict, return stage, and concise reason
   to `forge-loop-analyst`. The loop owns status, logbook, validation, and
   commit.

## Learning Admission

After a verification artifact is complete, `LEARNINGS.md` may be updated
only when its method pattern already has the completed, non-rejected
pipeline evidence required by that file's admission rules. Domain findings
stay in the build.

## Output Gate -- HARD GATE

PASS only when:

- every material build claim maps to evidence in the parent chain;
- every acceptance test has a concrete pass/fail condition;
- limitations and counter-evidence are not suppressed;
- verdict and return stage follow the state machine;
- frontmatter and body match the template; and
- the only new stage artifact is inside `forge/verifications/`.

Any missing item is HALT. A timeout, tool failure, or uncertainty is never
treated as PASS.

## Related

- `governance/skills/forge-verify/assets/template.md`
- `governance/skills/forge-loop-analyst/SKILL.md`
- `governance/skills/forge-build/SKILL.md`
- `forge/protocol.md`