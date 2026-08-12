# Agentic Forge

The agentic forge. Research is being done here.

## What This Repo Is

A structured research pipeline that converts raw ideas into durable,
transferable insights. Each artifact passes through six stages with
binary PASS/HALT gates at every step.

## Pipeline

```
IDEA --> RESEARCH --> EVALUATE --> PROPOSE --> VALIDATE --> INSIGHT
  |         |           |            |            |           |
 Gate      Gate        Gate         Gate        Gate        Gate
```

| Stage | Folder | Input | Output | Gate |
|:--|:--|:--|:--|:--|
| 1. Ideate | `forge/ideas/` | Raw insight from research | Scoped idea brief | Novel AND testable? |
| 2. Research | `forge/research/` | Scoped idea brief | Evidence report with sources | Evidence supports? |
| 3. Evaluate | `forge/evaluations/` | Evidence report | PASS/HALT verdict with reasoning | Credible AND viable? |
| 4. Propose | `forge/proposals/` | PASS verdict | Research plan | Concrete AND feasible? |
| 5. Validate | `forge/validations/` | Research plan | Stress-test result | Survives scrutiny? |
| 6. Insight | `forge/insights/` | Validated plan + full chain | Durable principle | Actionable AND transferable? |

Full spec: `forge/protocol.md`.

## Repository Hygiene

- **ASCII-only.** Every file is plain 7-bit ASCII. The local pre-commit
  hook and the CI gate (`ascii-guard.yml`) both enforce it.
- **Frontmatter IDs.** Generated with `date -u +'%Y%m%dT%H%M%SZ'`,
  validated by `scripts/validate-ids.sh` in CI.
- **Setup hooks once per machine:**
  ```bash
  bash scripts/setup-hooks.sh
  ```

## Layout

```
ANCHOR.md            # the forge direction -- set by Suggi
STATUS.md            # current pipeline cursor (where a fresh loop resumes)
JOURNAL.md           # chronological lab notebook (append-only)
LEARNINGS.md         # curated method memory
forge/               # the research pipeline (protocol, stage folders, logs/)
scripts/             # sanitize-ascii.py, setup-hooks.sh, validate-ids.sh, logbook-archive.py
.githooks/           # local pre-commit ASCII guard
.github/workflows/   # CI: ascii-guard.yml, forge-logbook-archive.yml
```

## For Contributors

1. Read `forge/protocol.md` before writing anything.
2. Start at `forge/ideas/` -- never skip stages.
3. Every artifact links to its parent (provenance chain).
4. Nothing is deleted; use `forge/graveyard/` for dead ideas.
