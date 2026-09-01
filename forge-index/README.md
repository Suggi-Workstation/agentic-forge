# forge-index -- Agentic Forge Search

Hybrid semantic and keyword retrieval over this repository's Markdown
control files, canonical skills, protocols, and stage artifacts.

## Production Ownership

The VPS repository watcher owns indexing. It runs after repository changes
and stores index data in `~/.forge-index/`. Agents check freshness and query;
they do not rebuild a healthy production index manually.

```bash
python forge-index/query.py --check-freshness
python forge-index/query.py "Researcher Analyst handoff" --top-k 20
python forge-index/eval.py --verbose
```

For corruption recovery only, after diagnosis:

```bash
python forge-index/index.py --force
```

## Retrieval

- Dense retrieval uses the configured embedding model.
- Sparse retrieval uses BM25.
- Reciprocal Rank Fusion combines the rankings.
- Results are deduplicated by file.
- The optional reranker is controlled by `config.yaml`.

## Files

| File | Purpose |
|:--|:--|
| `index.py` | Incremental/full index builder and freshness check. |
| `query.py` | Hybrid query and watcher-facing freshness check. |
| `eval.py` | Recall, MRR, and nDCG evaluation. |
| `gold-queries.yaml` | Forge-native expected retrieval targets. |
| `config.yaml` | Model, chunking, fusion, and storage settings. |

## Scope

The index reads Markdown in this repository and excludes logs, scripts,
GitHub metadata, git metadata, and generated data. Brain knowledge remains
in the brain index and is accessed separately through `query-brain-vps`.

## Gates

- Every gold target must exist in this repository.
- `scripts/validate-forge.py` checks target existence before commit.
- `query.py --check-freshness` must match repository HEAD.
- `eval.py` must meet its configured recall gate after watcher reindexing.