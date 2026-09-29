---
name: evidence-gated-forge-transaction-checker
id: 20260929T232637Z
tier: research
pipeline: 20260921T152802Z
author: Researcher
tags: [agent-systems, forge, verification, state-consistency]
links:
  - forge/ideas/evidence-gated-forge-transaction-checker-r01.md
  - forge/protocol.md
  - logbook/protocol.md
  - scripts/validate-ids.sh
  - .github/workflows/ascii-guard.yml
  - agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md
  - agentic-brain:reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md
  - https://pitest.org/quickstart/basic_concepts
  - https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
confidence: medium
---
# Research: Evidence-Gated Forge Transaction Checker

## Question and Method

This report investigates the exact question in the root idea: can a bounded
negative-fixture study show that a small, read-only checker catches material
contradictions among a Forge artifact, its `STATUS.md` handoff, and its progress
event that the current executable gates do not catch, without recreating the
reverted broad validator or attempting semantic review?[1]

The study was frozen at Git commit
`878347b85da2f911c8b475b549dbbf390e832c95`. The protocol, research template,
board, progress log, ID validator, and ASCII workflow were identified by their
Git blob IDs before fixture construction. The live repository was clean at the
same commit before and after the scratch experiment. No live artifact, board,
log, workflow, profile, runtime, or service was used as a fixture or changed by
the experiment.

Before targeted evidence gathering, the provisional explanation was that the
current executable gates checked IDs and ASCII but not the protocol's relational
transaction contract. The disconfirming cases were also stated first: no
material mutant escapes the existing gates, a declared mutant escapes the
prototype, a valid control fails, or useful coverage requires semantic judgment
or broad machinery. This ordering followed the Feynman procedure and the Brain's
advice to use deterministic checks for schemas and external state while auditing
both accepted and rejected cases.[8]

The fixture specification contained ten protocol-derived invariants:

| ID | Mechanical invariant |
|:--|:--|
| I01 | An explicitly requested ENT header ID resolves to exactly one progress block. |
| I02 | Artifact `pipeline` equals the requested root pipeline. |
| I03 | Artifact directory and tier match the completed stage. |
| I04 | Event `ref` equals the target artifact path. |
| I05 | Event `Pipeline` equals the root pipeline. |
| I06 | Event stage maps to artifact tier: `ideate` to `idea`, `research` to `research`, `evaluate` to `evaluation`, `propose` to `proposal`, and `final-review` to `review`. |
| I07 | Event `Artifact` equals the artifact frontmatter ID and explicit target ID. |
| I08 | At least one direct frontmatter link resolves to a local Forge artifact with the same root pipeline. |
| I09 | For the open research handoff, one active STATUS row names the pipeline and artifact, both STATUS and event hand off to `evaluate`, and the row remains `active`. |
| I10 | For the exact terminal control, the pipeline is absent from STATUS and exact `REJECT` or `DEFER` markers agree between the artifact and event, whose `Next` begins `closed`. |

These checks map to the artifact contract, stage table, board rules, session
transaction, closure rules, and logbook format.[2][3] I08 deliberately checks
only a resolving same-pipeline local link, not whether prose makes that link the
correct intellectual input. I10 uses an exact marker in the frozen control; it
does not infer a verdict from free text.

Two controls and eleven one-fact mutants were constructed in complete local
scratch clones of the frozen commit:

1. The open control added one synthetic current-schema research artifact for
   pipeline `20260921T152802Z`, changed only that pipeline's STATUS row to an
   `evaluate` handoff, and appended matching `ENT-008`. The unrelated open row
   remained present.
2. The closed control was the unmodified frozen repository. Pipeline
   `20260921T114301Z` has a `REJECT` evaluation in the graveyard, matching
   `ENT-005`, and no STATUS row.[6]
3. Each mutant changed one header, scalar metadata field, link, event field, or
   STATUS cell. No source-quality, reasoning-quality, novelty, or authorship
   judgment was encoded.

The fixture definitions were frozen before execution. Their corrected
specification had SHA-256
`220d9f189ce0cff2b44bb8052f32669bb091ef641bfcecf24ec1b4dc949bb04b`.
A second model context inspected the definitions before results existed. Its
first review rejected an unstated uniqueness rule for event `see`, an incomplete
stage-to-tier statement, an underspecified closure extractor, an ambiguous input
link, and baselines whose exact bytes were not yet frozen. The definitions were
corrected to use an explicit unique ENT ID, the complete stage map, an exact
closure marker, a mechanical local-link rule, exact open-control bytes, and a
complete frozen-repository base. A fresh second-reader pass then returned no
remaining correction before execution. These disagreements are recorded here;
the two raw reader responses were not separately committed, so this report does
not claim independently auditable reader timing or blind reproducibility.[12]

Each fixture ran three gates:

- the exact tracked-text ASCII scan in the current workflow;
- the frozen `bash scripts/validate-ids.sh` command; and
- one scratch-only prototype supplied with explicit mode, pipeline, artifact
  path, artifact ID, and ENT ID.

The prototype and runner were temporary test instruments, not proposed code.
Their SHA-256 values were
`f8b39e4126e7d1347e3a8e446b3b5e1968125970202496c8806cd1ba83070926`
and
`62164eec1581384ab0d4a2aba80043f3360ec6c3eaaec9810368ce69151c28f0`.
The complete 13-case JSON result had SHA-256
`8b20a3a844bc09309981e46f862dadad09ada31bc5350379492ea9880d6c7efc`.
The result matrix below is the durable record; temporary fixture clones and
instruments are not production artifacts.

Mutation testing is an appropriate bounded analogy: a useful test should fail
when a non-equivalent in-scope fault is inserted, while equivalent or out-of-scope
mutants limit what a mutation score means.[10] The second-reader correction gate
therefore checked that each mutant was invalid under the current protocol before
execution. The method does not convert eleven selected mutants into complete
schema coverage.

## Evidence and Findings

### Current executable scope

`validate-ids.sh` scans Markdown frontmatter IDs for timestamp format,
suspiciously rounded seconds, duplicates, and future time. It does not parse the
STATUS table, progress events, artifact links, stage transitions, or closure
agreement.[4] The current `ascii-guard` workflow scans tracked text for non-ASCII
bytes and then invokes that ID script; it contains no other Forge transaction
command.[5] GitHub documents that a shell step is reported as success or failure
from its shell exit code, so the workflow's declared commands, not its name or a
successful run, define the mechanical claim it can support.[11]

This is a scope finding, not evidence that the existing gates malfunction. Both
do exactly what their checked source says. The uncovered question is whether the
protocol's additional relational requirements merit a separate narrow gate.

### Preserved result matrix

The following are direct session observations from the frozen scratch run. `P`
means the gate accepted the fixture; `R` means the prototype rejected it. The
failed-invariant column identifies the intended relationship, not every
downstream check that became unavailable after an ambiguous event target.

| Fixture | One changed fact | ASCII | ID | Prototype | Intended failed invariant |
|:--|:--|:--:|:--:|:--:|:--|
| valid-open-research | none | P | P | P | none |
| valid-closed-evaluation | none | P | P | P | none |
| M01 | later `ENT-006` header changed to duplicate `ENT-005` | P | P | R | I01 |
| M02 | artifact pipeline changed | P | P | R | I02 |
| M03 | artifact tier `research` changed to `idea` | P | P | R | I03, I06 |
| M04 | event `ref` changed to a missing research path | P | P | R | I04 |
| M05 | event `Pipeline` changed | P | P | R | I05 |
| M06 | event Stage `research` changed to `propose` | P | P | R | I03, I06 |
| M07 | event `Artifact` changed to the root idea ID | P | P | R | I07 |
| M08 | artifact input link changed to a missing idea path | P | P | R | I08 |
| M09 | STATUS `active-artifact` changed to a missing path | P | P | R | I09 |
| M10 | STATUS stage `evaluate` changed to `propose` | P | P | R | I09 |
| M11 | closure event verdict `REJECT` changed to `DEFER` | P | P | R | I10 |

All thirteen fixtures passed the existing ASCII and ID gates. The ID gate
reported zero errors and zero warnings while scanning twelve frontmatter files
in each closed-control fixture and thirteen in each open-control fixture. The
prototype accepted both unmodified controls and rejected all eleven declared
mutants. The runner's aggregate `all_expected` result was true for all thirteen
cases.

At least three escaped mutants are directly handoff-relevant rather than cosmetic:
M09 points STATUS at a nonexistent next input, M10 routes the completed research
directly to `propose` instead of independent evaluation, and M11 gives the event
a different terminal disposition from the exact evaluation artifact. M02, M04,
M05, and M07 also break the provenance chain that the protocol requires to agree
before a stage is complete.[2][3] No such contradiction was found in the live
repository; the finding is incremental detection on declared negative fixtures,
not current corruption.

The exact-target case matters. The closed control's target is `ENT-005` even
though valid later events exist. The first proposed specification incorrectly
used global uniqueness of `see`, which the protocol does not require. Independent
review replaced that proxy with an explicit ENT target and a duplicate-ENT
negative case. This matches prior Brain evidence that a validator can pass while
checking a nearby record rather than the requested one.[9]

### Contrary evidence and limitations

The strongest contrary evidence is the prior broad validator. Git confirms that
commit `682fbb4a3184654e62e70fc2d1fa620af2fbee7d` added a 707-line
`scripts/validate-forge.py` within a 43-file system change, and the immediately
following commit `35b8213f39e6d813c00ec1b36776d077a697b27c` reverted that
change.[7] This study does not establish that any production checker avoids the
same maintenance and false-confidence risks. It establishes only that ten
current relational invariants were expressible in a bounded prototype.

Coverage is narrow:

- two valid controls cannot estimate a general false-rejection rate;
- mutants were designed from the same ten rules used by the prototype, creating
  an overfitting risk despite the pre-run review;
- revision, reframe, proposal, final-review, human-decision, archived-log,
  malformed-Markdown, and concurrent-writer paths were not tested;
- explicit ENT selection would have to be supplied or derived by a future
  procedure, and that interface was not evaluated;
- the scratch prototype was not installed, committed, scheduled, or exercised
  by the normal watcher path;
- reader disagreements are preserved in this report, but separate immutable
  pre-comparison reader output is absent, so no blind or independently audited
  reproducibility claim is made.[12]

After the experiment, two compact Python result-extraction attempts and one
compound shell pre-write probe were approval-blocked in the unattended context.
The complete JSON result was instead read directly, and the pre-write checks were
split into simple commands. These post-run blocks caused no fixture or live-repo
change and do not alter the matrix, but they demonstrate that a future procedure
should not depend on inline interpreter probes.

## Alternatives and Implications

| Alternative | Evidence-supported benefit | Cost or limit |
|:--|:--|:--|
| Do nothing | No code, integration, or maintenance cost; current manual transaction review remains authoritative. | All eleven declared contradictions still pass the only current executable gates. |
| Shorter manual checklist | Could focus reviewers on artifact-board-event agreement without adding code. | Restates protocol obligations and supplies no machine evidence that the exact target was checked. |
| Narrow local read-only checker | Accepted two controls and rejected all eleven predeclared mutants using ten current invariants. | Evidence is fixture-bounded; an implementation needs broader valid controls, a stable explicit target, tests, and maintenance ownership. |
| Broad CI/runtime validator | Could attempt larger coverage. | The prior 707-line validator and associated machinery were reverted; this study supplies no evidence for locks, monitors, deployment controls, or semantic review.[7] |

The evidence supports independent evaluation of the narrow-checker alternative.
It does not support automatic implementation, deployment, or a claim that the
manual gate can be removed. The smallest plausible later proposal would preserve
manual research-quality review, accept explicit transaction identifiers, check
only protocol-stable relationships, include positive and negative fixtures, and
fail closed without changing repository state. Evaluation should reject or
revise that direction if the required interface expands beyond the ten bounded
invariants or if broader valid controls reveal false failures.

The result also supports a simpler fallback: if maintaining even the narrow
checker is not justified, retain the current process but replace vague final
review with the same explicit field list. That fallback would not add automated
detection, but it avoids the broad-validator failure mode and keeps the
unverified claim narrow.

## Response to Feedback and Remaining Questions

No prior evaluation exists for this pipeline.

The pre-run reader's material objections were answered as follows:

1. Global `see` uniqueness was removed. I01 now uses an explicitly requested,
   unique ENT header ID, and M01 duplicates that exact ID.
2. Literal Stage/tier equality was removed. I06 uses the complete protocol
   mapping, including `evaluate` to `evaluation` and `final-review` to `review`.
3. Closure interpretation was narrowed to one exact frozen control and literal
   verdict markers; no free-text classifier is used.
4. A direct input link now means a frontmatter `links` entry beginning `forge/`,
   resolving to an artifact whose `pipeline` equals the requested root.
5. Both controls now begin from the complete frozen repository, and the open
   overlay's artifact, STATUS, and progress bytes were hashed before execution.

The following questions remain decision-relevant for evaluation or a proposal:

- What additional valid controls are sufficient to test revisions, proposals,
  final reviews, reframes, and closures without rebuilding the broad validator?
- Should the caller supply the exact ENT ID, or can the protocol define another
  unambiguous target that does not select a convenient nearby event?
- Which of the ten invariants are stable enough to encode, and which should
  remain manual because their schema or meaning changes frequently?
- Would a small repository-local script plus fixture tests be cheaper and less
  error-prone than an explicit manual checklist over several future pipelines?
- How will a proposal prevent a green structural result from being described as
  evidence of research quality, independence, source validity, or deployment
  readiness?
- Can pre-comparison fixture definitions and reader output be preserved within
  the artifact contract without creating unauthorized supporting artifacts?

Confidence is medium. It is supported by a frozen source commit, two accepted
controls, eleven single-fact negative cases, exact gate outputs, corrected
pre-run fixture review, and unchanged live repository state. It is limited by
the small valid-control set, rule-derived mutants, lack of durable separate
reader output, untested lifecycle paths, and the historical failure of a broad
validator. Confidence would rise if a later evaluation independently reproduces
the matrix from this report and if additional valid transaction shapes pass
without relaxing the negative cases. It would fall if explicit targeting proves
awkward, if normal transactions produce false failures, or if useful coverage
requires volatile inventories, semantic inference, or deployment machinery.

## Sources

1. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- root
   question, bounded fixture plan, support conditions, stop conditions, and
   broad-validator exclusion. [high]
2. `forge/protocol.md` -- stage mapping, artifact contract, board selection,
   closure rules, session transaction, write boundaries, and required agreement
   among artifact, STATUS, and progress event at starting commit
   `878347b85da2f911c8b475b549dbbf390e832c95`. [high]
3. `logbook/protocol.md` -- ENT identity, append-only counters, event fields,
   exact references, and post-write agreement requirements at the starting
   commit. [high]
4. `scripts/validate-ids.sh` -- current executable checks for ID format,
   suspicious rounding, duplicates, and future timestamps; relational Forge
   fields are outside its parsed inputs. [high]
5. `.github/workflows/ascii-guard.yml` -- current tracked-text ASCII scan and
   invocation of `scripts/validate-ids.sh`; no transaction relationship command
   is present. [high]
6. `forge/graveyard/auditable-sbc-buyback-bridge-evaluation-r02.md` -- exact
   frozen terminal artifact and `REJECT` marker used by the closed control.
   [high]
   - `STATUS.md` -- absence of closed pipeline `20260921T114301Z` and the two
     unrelated active rows at the frozen commit. [high]
   - `logbook/progress.log` -- matching `ENT-005` closure event and later valid
     events used to test explicit target selection. [high]
7. `scripts/validate-forge.py` -- 707-line historical validator added at Git
   commit `682fbb4a3184654e62e70fc2d1fa620af2fbee7d` and removed by immediate
   revert commit `35b8213f39e6d813c00ec1b36776d077a697b27c`; verified from Git history and
   used only as scope counterevidence. [high]
8. `agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md`
   -- deterministic schema/state checks, bidirectional auditing of accepted and
   rejected cases, and limits of weak graders. [medium]
9. `agentic-brain:reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md`
   -- exact-target validator failure and counterexample fixtures; an internal
   operational account, not independent proof of this experiment. [medium]
10. PIT. "Basic Concepts," undated; accessed 2026-09-29, Mutants and Equivalent
    Mutations sections. Fault seeding, killed mutants, and equivalent-mutation
    limits were checked.
    https://pitest.org/quickstart/basic_concepts [medium]
11. GitHub. "Workflow syntax for GitHub Actions," undated; accessed 2026-09-29,
    `jobs.<job_id>.steps[*].shell` Exit codes and error action preference.
    Shell-step success and failure are derived from exit status.
    https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax [high]
12. `LEARNINGS.md` -- current requirement to preserve dated pre-comparison rules
    and unmerged per-reader outputs before claiming a blind or reproducible
    procedural validation. [high]
