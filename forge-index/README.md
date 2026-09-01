# Forge Index

Hybrid semantic and keyword search over this repository. The VPS watcher
keeps the shared index current; Forge agents query it but do not rebuild it.

## Commands

Run from the repository root with the watcher Python environment:

```bash
/opt/repo-tools/venv/bin/python forge-index/query.py --check-freshness
/opt/repo-tools/venv/bin/python forge-index/query.py "researcher analyst handoff" --top-k 20
/opt/repo-tools/venv/bin/python forge-index/eval.py --verbose
```

## Files

- `index.py`: watcher-owned index builder.
- `query.py`: hybrid retrieval and freshness check.
- `eval.py`: evaluates the small Forge-native gold set.
- `gold-queries.yaml`: retrieval questions whose targets live in this repo.
- `config.yaml`: embedding, chunking, and exclusion settings.

Index data lives outside the repository under the hermes user's shared
Forge index path. Generated vectors and evaluation output are ignored by
git.

## Scope

Markdown control files, Forge protocol, canonical skills, templates, and
stage artifacts are indexed. Active event logs, scripts, workflows, git
metadata, and non-Markdown data are excluded.

If freshness is STALE, diagnose the Forge watcher. Do not build a second
index or run a manual rebuild during a Forge agent session.