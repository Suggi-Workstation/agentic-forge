---
name: forge-history-duplicate-receipt
id: 20260930T132200Z
tier: research
pipeline: 20260930T124036Z
author: Researcher
tags: [agent-systems, forge, retrieval, provenance]
links:
  - forge/ideas/forge-history-duplicate-receipt-r01.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - logbook/progress.log
  - logbook/errors.log
  - forge-index/README.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md
  - agentic-brain:library/history/historiography-and-historical-method.md
  - https://git-scm.com/docs/git-log
  - https://git-scm.com/docs/git-rev-list
  - https://git-scm.com/docs/git-show
  - https://git-scm.com/docs/git-ls-tree
confidence: medium
---
# Research: Forge History Duplicate Receipt

## Question and Method

This report tests the root idea's exact question: can one bounded, read-only Git
history receipt expose Forge pipelines and exact disposition evidence that are
reachable from a frozen revision but absent from its current tree, without
creating another state board, changing the live index, or implying archival
completeness?[1]

Before targeted historical reconstruction, the provisional explanation was
recorded in task-owned scratch: the current tree and current-corpus index cannot
return a deleted artifact body, while Git can read that body if a supplied
revision still reaches its commit. A useful receipt would therefore bind each
historical path to one containing commit, blob, artifact ID, tier, and pipeline,
then require full reading of the root and decisive disposition artifact. The
initial gaps were path and revision noise, disposition inference, false pipeline
merges, review burden, and whether any novelty or reopening decision would
actually change. Disconfirmation was predeclared as a count mismatch, unreadable
body, ambiguous pipeline, inferred disposition, false merge, or no supported
decision delta.[1][2][9][11]

The transaction started at clean HEAD
`b2ac06d2a42e079ecb41f9b5be896b838868f62e`. The experiment used revision
`d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06`, the pre-idea revision named by the
root artifact, so the selected idea could not serve as its own baseline. The
clone reported `false` for `git rev-parse --is-shallow-repository`; 91 commits
were reachable from that revision. The population was Markdown under the seven
Forge tier directories. `git ls-tree` defined the frozen current tree, while
`git log <revision> --full-history --name-only` defined historical path
candidates. Each candidate was read from the newest containing commit with
`git show <commit>:<path>` and bound to its blob ID with `git rev-parse`.[1]
[12][13][14][15]

Five prompts were frozen before the comparison:

| Root sought | Prompt |
|:--|:--|
| `auditable-maintenance-capex` | `maintenance capex estimation annual reports value investing framework` |
| `auditable-sbc-buyback-bridge` | `stock based compensation buyback bridge accounting dilution value investing` |
| `evidence-gated-forge-transaction-checker` | `Forge transaction checker current record validation false rejection` |
| `unattended-forge-command-paths` | `approval denied unattended Forge command selection command paths` |
| `bounded-index-freshness-recheck` | `index freshness watcher stale bounded recheck` |

The baseline combined frozen-tree enumeration, five current hybrid queries,
`STATUS.md`, and the active progress log. Because the exact historical index
snapshot at `d6137e3` was not preserved, rebuilding it would have changed the
normal query boundary. The current index at transaction HEAD was queried
instead, then results were restricted to paths present in the frozen tree and
the selected idea was excluded. This tests the current-corpus boundary and
candidate clues; it is not an exact reconstruction of historical ranking or a
semantic-recall estimate.[2][3]

The treatment added the history receipt. Predeclared grading fields were exact
root path and ID, body availability, pipeline identity, corrective state,
disposition and its exact evidence, false merge, decision delta, elapsed time,
output bytes, and full bodies requiring review. All writes before this report
were outside the repository in task-owned scratch. No watcher, indexer, rebuild,
ref, worktree, board, runtime, or external repository was changed.

### Preserved runnable instrument

The following exact ASCII instrument, SHA-256
`29cc2da6d5b3f18fc99a8c2623fef6ca67d7e40d3cefee169954deb57afcdfaa`,
produced the manifest below. It is a read-only instrument, not a proposed
repository tool.

```python
#!/usr/bin/env python3
import subprocess
from pathlib import Path

REPO = Path('/srv/forge/agentic-forge')
REV = 'd6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06'
DIRS = [
    'forge/ideas', 'forge/research', 'forge/evaluations',
    'forge/proposals', 'forge/final-reviews', 'forge/discoveries',
    'forge/graveyard',
]


def git(*args, check=True):
    p = subprocess.run(['git', *args], cwd=REPO, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode:
        raise SystemExit(p.stderr or p.stdout)
    return p


def show(commit, path):
    p = git('show', f'{commit}:{path}', check=False)
    return p.stdout if p.returncode == 0 else None


def meta(text):
    out = {}
    if not text.startswith('---\n'):
        return out
    end = text.find('\n---\n', 4)
    for line in text[4:end].splitlines():
        if ': ' in line and not line.startswith(' '):
            key, value = line.split(': ', 1)
            out[key] = value
    return out

current = sorted(x for x in git('ls-tree', '-r', '--name-only', REV,
                                '--', *DIRS).stdout.splitlines()
                 if x.endswith('.md'))
names = git('log', REV, '--full-history', '--name-only', '--format=',
            '--', *DIRS).stdout.splitlines()
paths = sorted({x for x in names if x.startswith('forge/') and x.endswith('.md')})
rows = []
for path in paths:
    commits = git('log', '--full-history', '--format=%H', REV, '--', path).stdout.splitlines()
    for commit in commits:
        text = show(commit, path)
        if text is None:
            continue
        fields = meta(text)
        blob = git('rev-parse', f'{commit}:{path}').stdout.strip()
        rows.append((path, commit, blob, fields.get('id', ''),
                     fields.get('tier', ''), fields.get('pipeline', '')))
        break
    else:
        raise SystemExit(f'unreadable path: {path}')
roots = [row for row in rows if row[0].startswith('forge/ideas/')]
logical_ids = {row[3] for row in rows}
for row in rows:
    print('\t'.join(row))
print(f'SUMMARY\tcurrent={len(current)}\tpaths={len(rows)}\tids={len(logical_ids)}\troots={len(roots)}')
```

## Evidence and Findings

### The final receipt recovered the declared population

The final instrument returned:

```text
SUMMARY current=8 paths=39 ids=34 roots=5
```

An independent verifier reread all 39 `commit:path` objects, compared each with
its copied bytes, blob ID, byte count, and SHA-256, checked ASCII, and tested
whether one artifact ID mapped to more than one pipeline. It returned:

```json
{
  "conflicting_id_pipeline_groups": 0,
  "errors": [],
  "experiment_revision": "d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06",
  "logical_ids_checked": 34,
  "object_byte_total": 693114,
  "pass": true,
  "paths_checked": 39,
  "roots_checked": 5
}
```

The complete machine receipt was 78,758 bytes with SHA-256
`a6eb47f2e59de6eac67eb7af350d1988239d0a37ba22bce93a714c09c168bd7f`.
The five query outputs totaled 22,208 bytes. In one measured run, the five
queries took 1.91488492 seconds and the history work took 0.937062729 seconds,
for 2.851947649 seconds through receipt assembly. These are one-host timing
observations, not a service bound or expected review time.

The first scratch run used wildcard pathspecs with `git ls-tree` and incorrectly
reported zero frozen-tree paths. That run was invalidated. Replacing the globs
with tier-directory pathspecs produced eight current paths, and the independent
39-object verifier passed. The failure shows that a future procedure must use an
executed and checked instrument rather than treating a plausible Git command as
validated.[9]

The durable path receipt is below. Columns are path, containing commit, blob,
artifact ID, tier, and root pipeline. Historical schema uses `review` for the
older final-review artifacts; the receipt preserves that fact instead of
normalizing it.

```text
forge/discoveries/bounded-index-freshness-recheck-r02.md d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06 8ff3f06a9e2da4c69b9d5cb9aeceadf2bfc4a75e 20260930T120257Z discovery 20260930T083956Z
forge/evaluations/auditable-maintenance-capex-evaluation-r01.md a702a85b02aa6d1f23cefee0cc0bee6d1086f7da 41b1c237b9ba91afdf533e7690e0cce4305b5831 20260921T074024Z evaluation 20260921T060750Z
forge/evaluations/auditable-maintenance-capex-evaluation-r02.md a88424a57f949a66996b6fb03d06c674087ec7c6 fbfe392922b485f2570c064c76d1cc1127f546f1 20260921T083622Z evaluation 20260921T060750Z
forge/evaluations/auditable-sbc-buyback-bridge-evaluation-r01.md 087a119eedf4bbe2547d0a59352d7dfb9fb2777b 261f0c9bf1ce779a6b48bf5c6c78c1e16746bb4a 20260921T123909Z evaluation 20260921T114301Z
forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md f484f0c4f5c53394debf26f90483317b512df5f3 2db9dfac57df96e7135099c14b9f5721f7d47faf 20260930T094521Z evaluation 20260930T083956Z
forge/evaluations/bounded-index-freshness-recheck-evaluation-r02.md c2edc702af59b9d126d1a27ea765e119b71a0ba9 3afc36ecb1c0fdd9d9c46119d98b5b0f2e9dd095 20260930T103940Z evaluation 20260930T083956Z
forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md 0a105387a0cf2c0e2699d3219bb9622bb698707b 676d4d47208c31648471908df4f274bf9ac9ddac 20260929T233502Z evaluation 20260921T152802Z
forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r02.md 6151f65a0618c338bc2e08c68e7ad589bd368a2c 953ceb51a110b7af978960874ee04342bd55d620 20260930T023515Z evaluation 20260921T152802Z
forge/evaluations/unattended-forge-command-paths-evaluation-r01.md 8b5434af35005156f31e2dff06c3dedf7b00b406 900a9eb4b7512d037948dc845378b3f0f570514d 20260930T003709Z evaluation 20260929T223305Z
forge/evaluations/unattended-forge-command-paths-review-r01.md 46ec84e3222e7b3eb1b65816ca5d81b391429d22 b975b9b4863c4b04bdf5cc35bd1965eb7627bb66 20260930T035205Z review 20260929T223305Z
forge/evaluations/unattended-forge-command-paths-review-r02.md 550ae2234d995604bf2c94b0cb9d0021f2f00392 511705e5336bfe44938887bf5667c59e8ec3395f 20260930T053402Z review 20260929T223305Z
forge/evaluations/unattended-forge-command-paths-review-r03.md 7f51c85431b0f6ca51241b209255a0307fc73acd 002c444f835344ff0fe389ef700fdbb29ca77634 20260930T063736Z review 20260929T223305Z
forge/final-reviews/bounded-index-freshness-recheck-review-r01.md 132fb33689b22ed02c5da721538f3b78fef1b2df ab925e4be364df7f37073d1516910de057a25a2c 20260930T113819Z final-review 20260930T083956Z
forge/final-reviews/bounded-index-freshness-recheck-review-r02.md c8b350737679bc9426947bb351c1b3a22b7a08fa b7949ee9ba18b4cb7fb142a0190e62390ecd2c6d 20260930T113819Z final-review 20260930T083956Z
forge/final-reviews/unattended-forge-command-paths-review-r01.md 11b0425908ecdd0cc71bb54e483833ac466cdf55 b975b9b4863c4b04bdf5cc35bd1965eb7627bb66 20260930T035205Z review 20260929T223305Z
forge/final-reviews/unattended-forge-command-paths-review-r02.md 11b0425908ecdd0cc71bb54e483833ac466cdf55 511705e5336bfe44938887bf5667c59e8ec3395f 20260930T053402Z review 20260929T223305Z
forge/final-reviews/unattended-forge-command-paths-review-r03.md 11b0425908ecdd0cc71bb54e483833ac466cdf55 002c444f835344ff0fe389ef700fdbb29ca77634 20260930T063736Z review 20260929T223305Z
forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md fea117df0e15835239b22959a7fb5268423891cf 8af08a6a7accc5d55ad88790570787150bbbf772 20260921T143617Z evaluation 20260921T114301Z
forge/graveyard/evidence-gated-forge-transaction-checker-evaluation-r03.md ee82fca6dc9c6ab654ffb294152a5f12756ecb6c 804b5b807eef7394b0ce640debedc65d93c2a08a 20260930T045604Z evaluation 20260921T152802Z
forge/ideas/auditable-maintenance-capex-r01.md 88f20c05e07424240cde4d49df5ea1eb9b0e9094 3ab502d88824005147ecf1c0145c2ae0c191bd83 20260921T060750Z idea 20260921T060750Z
forge/ideas/auditable-sbc-buyback-bridge-r01.md b48b52a10ed6079e84d0555ef482667efdd377fe 8125d289ada69084a648c8fed55fb250ba3dce4b 20260921T114301Z idea 20260921T114301Z
forge/ideas/bounded-index-freshness-recheck-r01.md fe142176729b572542224855882303a435a4949c 40f35b50b97833e76702cb00357d1bba2f9c2aa5 20260930T083956Z idea 20260930T083956Z
forge/ideas/evidence-gated-forge-transaction-checker-r01.md 4bc2896bf5398e36dec2f4ec2ffc3791efaec554 e6d3a241fe06baa7be8857ef5a35af6aca8413a1 20260921T152802Z idea 20260921T152802Z
forge/ideas/unattended-forge-command-paths-r01.md 878347b85da2f911c8b475b549dbbf390e832c95 f4793897539eaa85421ebb458290318e98fe6ec5 20260929T223305Z idea 20260929T223305Z
forge/proposals/bounded-index-freshness-recheck-r01.md e66e3c2fa7dcfcc7d47272845bd3d0c661c5c9d0 041959b06f8b62b96ef7e98125fb5b527ca155ed 20260930T110901Z proposal 20260930T083956Z
forge/proposals/bounded-index-freshness-recheck-r02.md c8b350737679bc9426947bb351c1b3a22b7a08fa 041959b06f8b62b96ef7e98125fb5b527ca155ed 20260930T110901Z proposal 20260930T083956Z
forge/proposals/unattended-forge-command-paths-r01.md 185464e6153d88a47828ce1481e2dd8efe0fdc79 6b4d5f17c0d9d928f53f18f7117d8bcc4f3577c9 20260930T020211Z proposal 20260929T223305Z
forge/proposals/unattended-forge-command-paths-r02.md 26538e9e47c3eacaac036a9457203ee97c7e4163 3f2ea66b27c0a0329417fe66e3b500fe271f7f4f 20260930T050338Z proposal 20260929T223305Z
forge/proposals/unattended-forge-command-paths-r03.md 2224f529b5198a7e1a20c9d692f72f94ca146351 1f0137b265ab227fc9dd862dc22e7f353b5aa21a 20260930T060651Z proposal 20260929T223305Z
forge/research/auditable-maintenance-capex-r01.md a0f235f7d3d4b6fb9a69043454efa7c28ce002e3 6710e13dd035cfa805e1ddb45ae0789565cf79fc 20260921T070743Z research 20260921T060750Z
forge/research/auditable-maintenance-capex-r02.md a84dd33b146fd50af5608d833fc8a0f6a8b0a2d3 7ad4e7aac34326dd3733c4828b19557e4d16cb79 20260921T081621Z research 20260921T060750Z
forge/research/auditable-sbc-buyback-bridge-r01.md b48b52a10ed6079e84d0555ef482667efdd377fe 4717f1d49cfc783eb7f57ab410977b4ad9350d85 20260921T121424Z research 20260921T114301Z
forge/research/auditable-sbc-buyback-bridge-r02.md 9214e7b4a65754b5a3bb3749f73a8578ba0d1eda c226185e78c2d25abc7f3c2e2cdfc57e0d7edfef 20260921T133154Z research 20260921T114301Z
forge/research/bounded-index-freshness-recheck-r01.md c4c16673925f87604fb9353385ee8966a5a1ff30 10a19f372ddac13ef505123ef04d152940701939 20260930T091629Z research 20260930T083956Z
forge/research/bounded-index-freshness-recheck-r02.md a36e81d195ded375e9e841406ab22d7023bff5a5 5eb12efcabfb3270f957284e760472b0dda79e9d 20260930T101043Z research 20260930T083956Z
forge/research/evidence-gated-forge-transaction-checker-r01.md f8982b6926668a35a72de60a6609f3b7e5397e25 19914c0198cbb0d5b635957c490f219b735bd2cb 20260929T232637Z research 20260921T152802Z
forge/research/evidence-gated-forge-transaction-checker-r02.md 77f2e25c1cdee027d876d598a30b7338212d1c0e a309c29d184bb1b3b95d0ce9bb48dd7727f22cff 20260930T012523Z research 20260921T152802Z
forge/research/evidence-gated-forge-transaction-checker-r03.md 10e32f6b5537fbef400596890593ec1a1535d0ef 075de063a35b9eb56eb164d1e976c28a442feae1 20260930T031626Z research 20260921T152802Z
forge/research/unattended-forge-command-paths-r01.md 114a0d25dac14dda2073c942774703f7e59b1248 2a95e7d9f5f7faeef220ec188f0334711b3cc44a 20260930T000632Z research 20260929T223305Z
```

### Path count is not artifact count

Five paths were historical rename copies of existing artifact IDs:

- bounded-freshness proposal ID `20260930T110901Z` appeared as proposal r01 and
  r02;
- bounded-freshness review ID `20260930T113819Z` appeared as review r01 and r02;
- unattended-command review IDs `20260930T035205Z`, `20260930T053402Z`, and
  `20260930T063736Z` each appeared once under `forge/evaluations/` and once
  under `forge/final-reviews/`.

Thus 39 reachable paths represented 34 logical artifact IDs. Every duplicate ID
remained in one pipeline, and the independent verifier found zero cross-pipeline
ID groups. A path-only receipt would overcount five artifacts and could present
renames as independent evidence. The stable grouping key is pipeline plus
artifact ID; paths and containing commits remain provenance, not identity.[2]

### The current-corpus baseline did not expose deleted bodies

No deleted historical path from the 39-path truth set appeared in any of the
five current hybrid query outputs. The selected idea, added after the frozen
revision, appeared in four outputs and was excluded as target leakage. The raw
ranked path sequences used for this corpus check were:

```text
auditable-maintenance-capex:
ANCHOR.md; governance/template-research.md; governance/skills/forge-research/SKILL.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r02.md; forge/ideas/forge-history-duplicate-receipt-r01.md; governance/template-evaluation.md; forge/protocol.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md; forge/discoveries/bounded-index-freshness-recheck-r02.md; forge/proposals/bounded-index-freshness-recheck-r02.md; governance/template-proposal.md; forge/research/bounded-index-freshness-recheck-r01.md; forge/ideas/bounded-index-freshness-recheck-r01.md; forge/final-reviews/bounded-index-freshness-recheck-review-r02.md; governance/template-idea.md; governance/template-final-review.md; LEARNINGS.md; README.md

auditable-sbc-buyback-bridge:
ANCHOR.md; forge/ideas/bounded-index-freshness-recheck-r01.md; forge/ideas/forge-history-duplicate-receipt-r01.md; forge/discoveries/bounded-index-freshness-recheck-r02.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r02.md; governance/template-research.md; governance/skills/forge-research/SKILL.md; forge/proposals/bounded-index-freshness-recheck-r02.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md; governance/template-idea.md; forge/protocol.md; README.md; governance/skills/forge-evaluate/SKILL.md; governance/skills/forge-discover/SKILL.md

evidence-gated-forge-transaction-checker:
forge/ideas/bounded-index-freshness-recheck-r01.md; forge/ideas/forge-history-duplicate-receipt-r01.md; governance/skills/forge-loop-research/SKILL.md; forge/proposals/bounded-index-freshness-recheck-r02.md; LEARNINGS.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r02.md; forge/final-reviews/bounded-index-freshness-recheck-review-r02.md; forge/research/bounded-index-freshness-recheck-r02.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md; forge/research/bounded-index-freshness-recheck-r01.md; governance/skills/forge-ideate/SKILL.md; governance/template-final-review.md; forge/protocol.md; STATUS.md; governance/skills/forge-loop-evaluate/SKILL.md

unattended-forge-command-paths:
forge/protocol.md; README.md; forge/ideas/forge-history-duplicate-receipt-r01.md; forge/discoveries/bounded-index-freshness-recheck-r02.md; governance/skills/forge-loop-evaluate/SKILL.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md; governance/skills/forge-ideate/SKILL.md; LEARNINGS.md; forge/ideas/bounded-index-freshness-recheck-r01.md; forge/proposals/bounded-index-freshness-recheck-r02.md; forge/final-reviews/bounded-index-freshness-recheck-review-r02.md; governance/skills/forge-loop-research/SKILL.md; forge/research/bounded-index-freshness-recheck-r01.md; ANCHOR.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r02.md; governance/template-evaluation.md; forge/research/bounded-index-freshness-recheck-r02.md; STATUS.md

bounded-index-freshness-recheck:
forge/ideas/bounded-index-freshness-recheck-r01.md; forge/research/bounded-index-freshness-recheck-r01.md; forge/discoveries/bounded-index-freshness-recheck-r02.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md; forge/research/bounded-index-freshness-recheck-r02.md; forge/proposals/bounded-index-freshness-recheck-r02.md; forge/final-reviews/bounded-index-freshness-recheck-review-r02.md; forge/evaluations/bounded-index-freshness-recheck-evaluation-r02.md; forge-index/README.md
```

The frozen tree supplied one exact root ID: the live bounded-freshness pipeline.
Its current idea also supplied path or slug clues for the SBC-buyback,
transaction-checker, and unattended-command pipelines, but not their root IDs.
It supplied no maintenance-capex clue. Baseline coverage was therefore one of
five exact root IDs and four of five candidate clues, not zero historical
awareness. The distinction matters: a clue can prompt targeted Git work, but it
is not the deleted body or exact decision record.[3][8]

### The history receipt recovered exact decision boundaries

The root and decisive artifact for each pipeline were read in full. Ten bodies -
one root and one decisive current or terminal artifact per pipeline - were the
minimum set needed to classify the five decisions. One additional unattended
proposal body was read to check the READY review's exact target.

| Pipeline | Frozen-tree baseline | Receipt evidence and exact bounded disposition | Decision effect |
|:--|:--|:--|:--|
| `20260921T060750Z` maintenance capex | No candidate clue or body. | Root `forge/ideas/auditable-maintenance-capex-r01.md`; evaluation r02 returned `REFRAME`, used corrective cycle 2 of 2, required same-pipeline ideation, and granted no proposal authority.[4] | Changes a plausible novelty decision: do not create a renamed maintenance-capex pipeline; the narrower disclosure-audit question is an exhausted-budget reframe. |
| `20260921T114301Z` SBC buyback | The live bounded-freshness idea named a distinct prior SBC idea, but did not expose the root ID, body, or terminal verdict. | Root plus graveyard evaluation r02 returned `REJECT`, removed the row, and named changed-evidence and human-budget reopening conditions.[5] | Changes an unknown-disposition lead into a closed pipeline that must not be reopened on unchanged evidence. |
| `20260921T152802Z` transaction checker | The live bounded-freshness idea summarized `DEFER` and exhausted budget, but no body or root ID was live. | Root plus graveyard evaluation r03 returned `DEFER` after two `REVISE` cycles, reproduced a false rejection, and required a human budget extension, real-record controls, and comparative value before reopening.[6] | Confirms rather than changes the safe baseline decision; adds exact ID, target failure, and reopening evidence. |
| `20260929T223305Z` unattended commands | The live bounded-freshness idea named the READY work and absence of an explicit decision, but no historical body was live. | Root, r03 proposal, final review r03, and nine deduplicated events show READY for exact proposal `20260930T060651Z`; no explicit Suggi decision was found in 42 reachable progress-log versions.[7] | Confirms rather than changes the safe baseline decision: prior work exists, READY is not approval, and disposition remains unrecorded. |
| `20260930T083956Z` bounded freshness | All eight logical artifacts, board row, and events were live. | Root and discovery show `awaiting-review` / `human-review`; no implementation authority exists.[8] | No decision change; this is the positive current-corpus control. |

The treatment therefore met the root idea's affirmative thresholds: five of five
reachable roots, 39 of 39 unique reachable tier paths, exact bytes for every
path, pipeline identity without a false merge, and at least one supported
novelty or reopening decision change. It also preserved unknown disposition:
the unattended READY review was not converted into approval, rejection, or
closure.[1][2][4][5][6][7][8]

The evidence does not establish that every ideation candidate needs all ten body
reads. Three deleted roots already had live clues, and targeted `git log` plus
`git show` would be cheaper when such a clue is present. The decision-relevant
increment is strongest for maintenance capex, which had no live clue, and for
SBC buyback, whose live clue omitted the terminal verdict. The receipt's value
is candidate discovery and exact provenance; semantic duplicate judgment still
requires full reading.[9][11]

### Reachability is a bounded corpus, not an archive guarantee

Git documentation defines revision traversal as commits reachable through parent
links from supplied revisions, with `--full-history` controlling path-history
simplification. `git show <commit>:<path>` returns the blob bytes at that exact
revision, and `git ls-tree` lists one tree's contents.[12][13][14][15] The run
therefore supports only this statement: all five roots and 39 named paths were
reachable from `d6137e3` in this non-shallow clone at execution time.

It does not support recovery of pruned objects, commits absent from supplied
refs, history rewritten beyond reachability, unfetched remote refs, or artifacts
never committed. A later garbage-collection or ref change may remove the
objects. Absence from the receipt is therefore absence from the tested reachable
corpus, not proof that no prior Forge work existed. This is consistent with the
Brain's historical-method warning that searchable digital collections reflect
selection, preservation, metadata, and retrieval boundaries.[11]

Source dependence is also limited. The historical artifacts and progress events
are repository records of the same Forge runs, not independent trials. Git
object identity and the independent verifier corroborate byte recovery, not the
truth of every claim inside those artifacts. The decision classifications are
high-quality internal evidence of recorded protocol state; they are not external
validation of the underlying proposals.[2][9][10]

## Alternatives and Implications

| Alternative | Evidence-supported benefit | Cost or limit |
|:--|:--|:--|
| Keep current-tree enumeration and current index only | Simple, fast, and correct for the live corpus; fully recovered the bounded-freshness control.[3][8] | Recovered one exact root ID, omitted every deleted body, and gave no maintenance clue. |
| Use targeted Git history only after a live clue | Smallest method for the three historically named candidates; exact bodies can be read with `git show`.[12][14] | Cannot expose an unmentioned deleted root such as maintenance capex; clue quality determines coverage. |
| Add one scratch-only root-first history receipt | Recovered all five roots and every reachable tier path in under one measured second of history work; preserved exact commit, blob, ID, tier, and pipeline. | Adds path noise, historical-schema handling, 39 paths, 34 logical IDs, and full-body review for actual candidates; reachable history is not complete history. |
| Maintain a tombstone manifest in the current tree | Could make deleted roots indexable without Git traversal. | Creates durable competing state that can drift, requires lifecycle and reset policy, and was not tested or authorized. |
| Build a history-aware semantic index | Could search deleted bodies semantically. | Changes index scope and freshness semantics, introduces a larger corpus and ranking problem, and exceeds the bounded result. |

The evidence supports evaluation of a small root-first, scratch-only receipt, not
an index, archive, board, or automatic duplicate verdict. The narrow form should:

1. freeze one revision and name exactly which refs or revision set defines
   reachability;
2. enumerate all tier paths and bind each to containing commit, blob, artifact
   ID, tier, and pipeline;
3. group by pipeline plus artifact ID so rename copies are visible but not
   double-counted;
4. surface root paths and candidate terminal artifacts first, then require full
   reading before a novelty, reopening, or disposition decision;
5. retain `unknown` when no exact human decision exists; and
6. label the receipt as reachable-history evidence, never archival completeness.

This result does not establish that the full 39-path manifest belongs inline in
every ideation session. A proposal should compare a concise root-first display
against the complete scratch receipt and keep the latter available only for
drill-down. It should also retain current-tree and current-index search because
history retrieval and current-state retrieval answer different questions.[2]
[3][9][10]

Doing nothing remains credible if resets are exceptional and reviewers already
follow clues with targeted Git inspection. Its cost is a demonstrated blind
spot: at the frozen revision, maintenance capex was reachable but absent from
both the tree and all baseline clues. A proposal is justified only if its exact
procedure remains shorter and safer than repeating the manual reconstruction
above.

## Response to Feedback and Remaining Questions

No prior evaluation exists for this pipeline.

Confidence is medium. Confidence is high in the bounded recovery result because
the exact instrument produced the declared counts, 39 Git objects were reread
and byte-checked independently, all five roots mapped to one pipeline each, and
the decisive artifact bodies were inspected.[4][5][6][7][8][12][13][14][15]
Overall confidence remains medium because the baseline uses current-index
results filtered to a historical tree rather than a preserved historical index
snapshot, the sample is five pipelines in one repository history, review effort
was not timed, and reachability can change. Confidence would rise after a cold
independent run reproduces the root-first receipt on a later reset and measures
candidate review effort without a false merge. It would fall if a renamed path
crossed pipelines, a recorded human decision was missed, a common history shape
escaped traversal, or the concise display failed to change a real ideation
decision.

Decision-relevant questions for evaluation are:

- Is the maintenance-capex decision delta large enough to justify a standard
  root-first step, or should ideation use targeted Git only when a live clue
  exists?
- Which revision set should define reachability: current `HEAD`, all local and
  remote refs, or an explicitly frozen subset? The choice changes the population
  and completeness wording.
- Should the procedure retain the full manifest only in task-owned scratch while
  presenting roots and terminal candidates in context?
- How should older tier names such as `review` map to current final-review
  semantics without rewriting historical metadata?
- What bounded test detects log resets, ENT renumbering, and copied paths without
  treating them as additional independent events?
- At what path count or elapsed time should the receipt stop and checkpoint
  rather than flood the ideation context?

These are evaluation and possible proposal questions. This report does not issue
`ADVANCE`, change the ideation skill, create a durable history index, restore a
deleted artifact, or authorize implementation. `LEARNINGS.md` remains unchanged
as required for a research stage.

## Sources

1. `forge/ideas/forge-history-duplicate-receipt-r01.md` -- root question,
   frozen comparison, five-root and 39-path thresholds, alternatives, limits,
   and no-durable-state boundary. [high]
2. `forge/protocol.md` -- duplicate, reachability-source, artifact, transaction,
   disposition, correction-budget, and one-stage rules. [high]
   - `STATUS.md` -- selected research row and bounded-freshness human-review row
     at transaction HEAD `b2ac06d2a42e079ecb41f9b5be896b838868f62e`.
     [high]
   - `logbook/progress.log` -- current stage events and handoffs at the same
     transaction HEAD. [high]
   - `logbook/errors.log` -- current failure record checked before research.
     [high]
   - `LEARNINGS.md` -- package-preservation and claimed-result-contract method
     lessons; read-only during this stage. [high]
3. `forge-index/README.md` -- live-repository hybrid corpus, file-level query
   interface, and current-corpus scope. [high]
4. `forge/ideas/auditable-maintenance-capex-r01.md` -- exact historical root ID
   and question, verified at Git commit
   `88f20c05e07424240cde4d49df5ea1eb9b0e9094`. [high]
   - `forge/evaluations/auditable-maintenance-capex-evaluation-r02.md` -- exact
     REFRAME, exhausted correction budget, narrower same-pipeline question, and
     no-proposal boundary, verified at commit
     `a88424a57f949a66996b6fb03d06c674087ec7c6`. [high]
5. `forge/ideas/auditable-sbc-buyback-bridge-r01.md` -- exact historical root ID,
   question, baseline, and stop rule, verified at Git commit
   `b48b52a10ed6079e84d0555ef482667efdd377fe`. [high]
   - `forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md` -- exact
     REJECT closure and reopening conditions, verified at commit
     `fea117df0e15835239b22959a7fb5268423891cf`. [high]
6. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- exact
   historical root ID, question, and manual alternative, verified at Git commit
   `4bc2896bf5398e36dec2f4ec2ffc3791efaec554`. [high]
   - `forge/graveyard/evidence-gated-forge-transaction-checker-evaluation-r03.md`
     -- exact DEFER closure, false rejection, exhausted budget, and reopening
     conditions, verified at commit
     `ee82fca6dc9c6ab654ffb294152a5f12756ecb6c`. [high]
7. `forge/ideas/unattended-forge-command-paths-r01.md` -- exact historical root
   ID, bounded question, and alternatives, verified at Git commit
   `878347b85da2f911c8b475b549dbbf390e832c95`. [high]
   - `forge/proposals/unattended-forge-command-paths-r03.md` -- exact READY target
     and purpose-separated adoption gate, verified at commit
     `2224f529b5198a7e1a20c9d692f72f94ca146351`. [high]
   - `forge/final-reviews/unattended-forge-command-paths-review-r03.md` -- exact
     READY verdict, proposal ID, human-review handoff, and no-approval boundary,
     verified at commit `11b0425908ecdd0cc71bb54e483833ac466cdf55`.
     [high]
   - `logbook/progress.log` -- deduplicated historical stage events and absence
     of an explicit human disposition through the pre-reset version at commit
     `7f51c85431b0f6ca51241b209255a0307fc73acd`. [high]
8. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- live current-corpus
   control, historical clues, and distinct freshness question. [high]
   - `forge/discoveries/bounded-index-freshness-recheck-r02.md` -- exact pending
     discovery and no-implementation boundary at frozen revision
     `d6137e30b8330fbaaf71a36c1f7cf2c9e3ba4f06`. [high]
9. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md`
   -- revision-specific evidence, provenance-preserving search, bounded context,
   checkpoints, and durable handoff requirements. [medium]
10. `agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md`
    -- distinction among authoritative history, current projections, replay, and
    current-world rereading. [medium]
11. `agentic-brain:library/history/historiography-and-historical-method.md` --
    provenance, archive selection, digital-corpus boundaries, negative-evidence
    limits, and explicit uncertainty. [medium]
12. Git project. "git-log Documentation," undated; accessed 2026-09-30,
    Description, path limiting, and History Simplification sections. Reachable
    commit traversal and `--full-history` behavior were checked.
    https://git-scm.com/docs/git-log [high]
13. Git project. "git-rev-list Documentation," undated; accessed 2026-09-30,
    Description, Commit Limiting, and History Simplification sections. Supplied-
    revision reachability and traversal limits were checked.
    https://git-scm.com/docs/git-rev-list [high]
14. Git project. "git-show Documentation," version 2.56.0 dated 2026-09-28;
    accessed 2026-09-30, Description and Examples sections. Exact historical
    blob retrieval with `<commit>:<path>` was checked.
    https://git-scm.com/docs/git-show [high]
15. Git project. "git-ls-tree Documentation," undated; accessed 2026-09-30,
    Description, `-r`, `--name-only`, and tree-ish sections. Frozen-tree path
    enumeration was checked.
    https://git-scm.com/docs/git-ls-tree [high]
