---
name: forge-build
description: "Synthesize a reviewed Forge build package."
user-invocable: false
disable-model-invocation: false
---

# Forge Build -- Researcher Stage 5

Synthesizes Analyst-approved research into an implementation-ready review
package. It designs work; it does not implement outside this repository.

## When to Use

Use only when `STATUS.md` says `stage: build`, `owner: Researcher`, and the
active evaluation verdict is PASS. A revision may supersede an older build.

## Procedure

1. Read startup context, the complete accepted chain, Analyst requirements,
   and `governance/skills/forge-build/assets/template.md`.
2. Invoke `forge-loop-feynman` on the recommendation and simplest viable
   implementation or framework.
3. State the decision first: what should be built, tested, changed, or
   adopted, and what should not be done.
4. Map every material recommendation to research evidence and the Analyst
   criterion it satisfies. Separate proven facts, reasoned design choices,
   and unresolved assumptions.
5. Design the minimum coherent package:
   - architecture or framework and component boundaries;
   - ordered implementation steps and named target types;
   - acceptance and regression tests;
   - worst-case failure prevention, security and scope constraints;
   - rollback or reversibility plan;
   - alternatives rejected and why;
   - limitations, open questions, and decisions reserved for Suggi.
6. For agent-systems work, describe proposed changes without editing brain,
   profiles, runtime skills, or infrastructure. For value-investing work,
   produce a Buffett-Munger-aligned process/framework, not a security or
   portfolio recommendation.
7. Generate a current UTC ID. Write one `forge/builds/<slug>-rNN.md`; set
   `parent` to the current active artifact (the PASS evaluation or a
   verification return verdict) and `supersedes` to the prior build ID when
   revising.
8. Return artifact path, ID, acceptance-test summary, and output-gate reason
   to `forge-loop-researcher`.

## Build Gate -- HARD GATE

PASS only when:

- every material recommendation has traceable evidence;
- the package is concrete enough for a separate implementer to execute;
- scope, dependencies, ownership, tests, rollback, and risks are explicit;
- the simplest viable design is distinguished from optional extensions;
- the worst plausible failure has a structural prevention or containment;
- uncertainty and human decisions are visible; and
- no implementation or external write occurred.

A polished essay without a design and verification plan is HALT. The next
stage is Analyst verification, never implementation.

## Related

- `governance/skills/forge-build/assets/template.md`
- `governance/skills/forge-loop-researcher/SKILL.md`
- `governance/skills/forge-evaluate/SKILL.md`
- `governance/skills/forge-verify/SKILL.md`
- `forge/protocol.md`
