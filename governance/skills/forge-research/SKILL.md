---
name: forge-research
description: "Execute a Forge evidence plan with citations."
user-invocable: false
disable-model-invocation: false
---

# Forge Research -- Researcher Stage 3

Executes the accepted evidence plan claim by claim. It records what the
evidence says, including evidence that weakens the intended build.

## When to Use

Use only when `STATUS.md` says `stage: research`, `owner: Researcher`, and
the active proposal resolves. A revision may supersede an older report.

## Procedure

1. Read the startup context, idea, proposal, Analyst return criteria if any,
   and `governance/skills/forge-research/assets/template.md`.
2. Invoke `forge-loop-feynman`. Preserve the pre-search baseline and gap list
   in working context, not as a separate file.
3. Execute the proposal method. For every material claim, read the strongest
   available primary source and seek independent corroboration when the
   claim drives the recommendation.
4. Use web search and extraction for external evidence. Optional
   `query-brain-vps` is read-only; read every cited brain artifact in full.
   Do not query or write investing-hub from a Forge run.
   - Agent-systems path: prefer official lab engineering guidance, source
     code, reproducible evaluations, and peer-reviewed work over commentary.
   - Value-investing path: read the brain's value-investing anchor and
     primary Buffett/Munger or Berkshire material; use secondary summaries
     only as corroboration and produce no security recommendation.
5. Record source date, publisher, URL or repo path, source type, and the
   precise claim it supports or contradicts. Brain citations use
   `agentic-brain:<path>`. Separate fact, interpretation, and inference.
6. Search deliberately for contrary evidence, failure cases, base rates,
   and alternate explanations. Explain unresolved contradictions instead of
   voting sources by count.
7. Compare execution with every proposal acceptance test and kill criterion.
   State deviations and missing evidence plainly.
8. Generate a current UTC ID. Write one
   `forge/research/<slug>-rNN.md`; set `parent` to the current active
   artifact (the proposal or an Analyst return verdict) and `supersedes` to
   the prior report when revising.
9. Return artifact path, ID, coverage summary, unresolved gaps, and gate
   reason to `forge-loop-researcher`.

## Research Gate -- HARD GATE

PASS only when:

- every planned material claim is supported, contradicted, or explicitly
  unresolved;
- every citation was actually read and accurately represented;
- consequential claims use primary or best-available evidence;
- source independence, recency, and limitations are stated;
- contradiction search is visible and honest;
- method deviations and uncertainty are explicit; and
- the report is sufficient for an Analyst to reproduce the conclusion.

Insufficient evidence does not become a confident conclusion. Complete the
report honestly and hand it to the Analyst, who owns PASS or HALT.

## Related

- `governance/skills/forge-research/assets/template.md`
- `governance/skills/forge-propose/SKILL.md`
- `governance/skills/forge-evaluate/SKILL.md`
- `forge/protocol.md`