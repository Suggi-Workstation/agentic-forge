---
name: evidence-gated-forge-transaction-checker
id: 20260930T012523Z
tier: research
pipeline: 20260921T152802Z
author: Researcher
tags: [agent-systems, forge, verification, state-consistency]
links:
  - forge/ideas/evidence-gated-forge-transaction-checker-r01.md
  - forge/research/evidence-gated-forge-transaction-checker-r01.md
  - forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md
  - forge/protocol.md
  - logbook/protocol.md
  - LEARNINGS.md
  - scripts/validate-ids.sh
  - .github/workflows/ascii-guard.yml
  - forge/research/unattended-forge-command-paths-r01.md
  - forge/evaluations/unattended-forge-command-paths-evaluation-r01.md
  - agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md
  - https://pitest.org/quickstart/basic_concepts/
  - https://www.gnu.org/software/bash/manual/bash.html
  - https://docs.github.com/en/actions/how-tos/create-and-publish-actions/set-exit-codes
confidence: medium
---
# Research Revision 2: Evidence-Gated Forge Transaction Checker

## Question and Method

This revision answers the four blocking questions in the evaluation of research
revision 1.[3] It asks whether a complete, inspectable fixture package can be
preserved inside one protocol-allowed research artifact; whether the positive
scope can be made exact; whether the prototype remains materially narrower than
the reverted validator; and whether its target interface and failure behavior
are explicit.

The selected pipeline is `20260921T152802Z`. The root idea author is Analyst,
while this research author is Researcher, satisfying the stage-independence
rule.[1][4] The stage began from clean Forge HEAD
`8b5434af35005156f31e2dff06c3dedf7b00b406`. The selected input was
`forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md`,
which returned the work to `research` as corrective cycle 1 of 2.[3]

Before further targeted research, the provisional explanation was that the
current ASCII and ID gates leave the artifact-STATUS-event relationship manual,
but revision 1 failed to preserve the bytes needed to test its claimed
prototype.[2][3] The disconfirming conditions were a rejected valid control, an
accepted mutant, an ambiguous target, a checker write, a harness error counted
as an expected rejection, or expansion beyond two explicitly supported
transaction shapes. This was a hypothesis, not evidence.

The source order was:

1. read the root idea, revision 1, evaluation, protocol, template, current board,
   logs, and read-only `LEARNINGS.md`;
2. query and read the relevant Forge and Brain records in full;
3. inspect the current executable gates and the historical validator revision;
4. read primary documentation for mutation tests, Bash behavior, and exit-code
   semantics; and
5. freeze, statically review, syntax-check, and execute one self-contained Bash
   package in scratch without changing the live Forge repository.

The evaluation literature supports preserving the task version, harness,
grader, permissions, and raw case results, and auditing accepted as well as
rejected cases.[8][9] PIT defines mutants as deliberately changed programs that
should behave differently from the unmutated class; this supports fault seeding
but not a claim of complete coverage.[11] The exact-target reflection supplies a
contrary mechanism: a validator can report success while inspecting a nearby
record unless target identity and ambiguity are tested directly.[10]

## Evidence and Findings

### The current-gate gap remains independently visible

The current `scripts/validate-ids.sh` reads Markdown frontmatter IDs and checks
format, rounded seconds, duplicates, and future timestamps. It does not parse
`STATUS.md`, progress events, artifact links, stage transitions, or closure
agreement.[5] The current `ascii-guard` workflow scans tracked text for
non-ASCII bytes and then invokes only that ID script.[5] These full-file reads
agree with the evaluation's independent finding that the relational gap is real
without relying on revision 1's missing prototype bytes.[3]

This revision did not repeat the ASCII and ID fixture matrix. Their scope was
already established by current source inspection and the prior evaluation.[3][5]
The new experiment addresses the missing evidence: exact checker, runner,
fixture, target, and output bytes.

### The supported scope is exactly two transaction shapes

The package accepts only:

1. `open-research`: one research artifact handed to `evaluate` by one active
   STATUS row and one exact progress event; and
2. `closed-evaluation-reject`: one graveyard evaluation with exact `REJECT`
   agreement, one exact closure event, and no matching STATUS row.

The caller supplies seven explicit values: fixture root, mode, pipeline,
artifact path, artifact ID, ENT ID, and completed stage. The checker does not
infer a convenient latest event. It rejects unsupported modes, repeated or
malformed target headers, nested artifact paths, duplicate event body fields,
missing links, ambiguous STATUS rows, and mismatched closure tokens. This is a
mechanical two-shape instrument, not a lifecycle validator.

Revisions, reframes, ADVANCE evaluations, proposals, final reviews, READY,
human decisions, DEFER closures, archived logs, concurrent writers, symlink
substitution, and semantic research quality remain outside the tested scope.
The package therefore cannot support a proposal broader than the two positive
controls without new controls and another evaluation.

### Static review corrected the package before execution

Two separate static-reader contexts returned `CORRECT` before execution. Their
material findings included an M05 mutation that matched two lines, permissive
header parsing, a prefix-only closure check, a malformed duplicate-ID case,
nested path acceptance, and harness errors that could have been counted as
expected mutant failures. Each finding was corrected before the frozen v3
package. A third separate context returned `VERDICT: ACCEPT`; its exact output
is preserved below.

These contexts used the configured model and are not independent scientific
reviewers. The Git commit occurs after execution, so this artifact does not
claim that Git independently proves pre-run chronology, blindness, or model
independence. The reader output is design-correction evidence, not support for
the runtime result. Runtime support comes from the complete rerunnable package
and preserved outputs. This limitation follows the evaluation handoff and the
current evidence-preservation lesson.[3][4]

### One bounded run matched all thirteen expected classifications

Bash syntax checks returned `SYNTAX_OK`. The package then ran once under GNU
Bash `5.2.21(1)-release`. Both valid controls exited 0 with one `PASS` line.
All eleven one-line mutants exited 1 with one protocol-valid `FAIL` line. The
runner reported `total=13`, `matched=13`, and `all_expected=true`. No case was
classified `HARNESS_ERROR`.

The live Forge repository remained at
`8b5434af35005156f31e2dff06c3dedf7b00b406` with a clean working tree after the
scratch experiment. The checker source contains no file creation, truncation,
append, rename, deletion, permission change, or external command. It reads the
supplied files and emits one line. The runner, not the checker, owns fixture
creation and raw-output capture.

The result is bounded. Eleven rule-derived mutants do not estimate a general
false-acceptance rate. Two controls do not estimate a general false-rejection
rate. The result establishes only that the exact frozen package accepted those
two shapes and rejected those eleven changes.

### Size, dependencies, interface, and maintenance surface are measurable

The frozen package metrics are:

| Item | Lines | Bytes | SHA-256 |
|:--|--:|--:|:--|
| pre-run specification v3 | 77 | 4,717 | `59b19e04c2e060203a41de0f86a1f4d3e8a069e639d44e07d2c2293b9260d686` |
| read-only checker | 246 | 8,716 | `822063f44a8cfa64cb4bbb0398acf5b93e00c1a1c4455bd97a56e67f151fed42` |
| fixture runner | 238 | 9,658 | `14f89b62a25d030bbe72494efe43df5c686b978e54971d05be42fb3aeddd8e6f` |
| final static review | 52 | 4,672 | `52098b0f26f50858fcf43502c633e2fc4e1a5c78c0c7db55138e7846401f680c` |
| run summary | 15 | 920 | `f8415c47a46ba43344c4448b5d1978261c4910bf25110a5c4a01ce6ceacc9fbc` |

The checker requires Bash and uses Bash builtins only. The runner additionally
uses `mkdir` and invokes Bash. GNU's Bash Reference Manual identifies the
checked implementation as Bash and documents its conditional constructs and
exit-status behavior; this package records the actual version rather than
claiming POSIX portability.[12] GitHub independently documents nonzero exit
status as the failure signal for an action, but this package was exercised
locally, not in GitHub Actions.[13]

The checker is 246 lines versus 707 lines for historical
`scripts/validate-forge.py` at commit
`682fbb4a3184654e62e70fc2d1fa620af2fbee7d`. However, the complete executable
package is 484 shell lines before its specification and receipts. The historical
checker also belonged to a 43-file system change that the immediately following
commit `35b8213f39e6d813c00ec1b36776d077a697b27c` reverted.[6] The current package
is narrower in modes, target, and authority, but its size does not prove that
production integration or maintenance would be economical.

### Complete frozen package and receipts

The following sections preserve the complete v3 specification, checker, runner,
final static-reader output, exact commands, raw per-case lines, and aggregate
output. The package is evidence inside this immutable research artifact. It is
not installed code or permission to deploy it.

#### Pre-run specification v3

```text
# Pre-run Specification v3

Recorded: 2026-09-30T01:01:57Z
Revision reason: two independent static review passes found defects before execution; every material finding was corrected before this frozen version.
Forge starting HEAD: 8b5434af35005156f31e2dff06c3dedf7b00b406
Pipeline: 20260921T152802Z
Selected stage: research revision 2
Selected input: forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md

## Provisional explanation

The existing executable gates do not inspect relational agreement among one Forge artifact, its STATUS handoff, and its selected progress event. A narrow read-only checker may detect that gap, but revision 1 did not preserve the bytes needed to inspect or rerun its claimed result. This explanation is provisional, not evidence.

## Gaps and disconfirmation

- The complete checker, runner, fixtures, commands, and raw outputs must be preserved in the completed report, not only hashes.
- The supported positive scope is exactly two transaction shapes: open research-to-evaluate and terminal evaluation-REJECT closure. No other lifecycle shape may be claimed.
- The caller must supply the root, mode, pipeline, artifact path, artifact ID, and exact ENT ID. Automatic target inference is out of scope.
- Any accepted mutant, rejected valid control, write by the checker, unsupported dependency, or material expansion toward the reverted broad validator disconfirms the tested candidate.
- Pre-run chronology and reader independence are not independently durable until the completed report is committed. The report must not use them as support for the result.

## Frozen checks

I01: Every event-header occurrence of the requested bracketed ENT ID is counted independently; exactly one must exist. Its header must use the exact six pipe-delimited fields with one ref and one see field.
I02: Artifact pipeline equals the requested pipeline.
I03: Artifact is a direct child of the mode's exact directory, and its tier matches the declared transaction mode.
I04: Event ref equals the artifact path.
I05: Event Pipeline equals the requested pipeline.
I06: Event Stage maps to the mode's artifact tier.
I07: Event Artifact and header see equal the requested artifact ID.
I08: At least one local Forge artifact link resolves and shares the pipeline.
I09: Open research mode has one active STATUS row naming the artifact and evaluate handoff; event Next is exactly evaluate.
I10: Closed evaluation-REJECT mode has no STATUS row; artifact and event verdict are exactly REJECT; the event Next semantic token is exactly closed.

## Fixtures and expected outcomes

Positive controls:
- valid-open-research: PASS.
- valid-closed-evaluation-reject: PASS.

Single-line mutants, each expected FAIL:
- M01 duplicate the selected ENT header ID.
- M02 change artifact pipeline.
- M03 change artifact tier.
- M04 change event ref to a missing artifact.
- M05 change the selected event Pipeline.
- M06 change event Stage from research to propose.
- M07 change event Artifact to the root idea ID.
- M08 change the artifact link to a missing path.
- M09 change STATUS active-artifact to a missing path.
- M10 change STATUS stage from evaluate to propose.
- M11 change the closure event verdict from REJECT to DEFER.

## Corrections after static review and before execution

Review pass 1:
- The unrelated open-fixture event now uses a distinct valid pipeline, making the M05 target line unique.
- Positive-control identifiers now exactly match this specification.
- The checker parses a fixed event header rather than accepting duplicate ref or see clauses.
- The closure Next value is reduced to its semantic token before exact comparison with closed.
- The runner uses fail-fast setup and captures each checker's exact stdout/stderr file.

Review pass 2:
- Every bracketed requested ENT occurrence is counted before canonical header validation.
- Exactly five pipe delimiters are required, so an empty trailing seventh field is rejected.
- Artifact paths must be direct children of forge/research or forge/graveyard.
- The runner classifies FAIL only for exit 1 plus one protocol-valid FAIL line; other failures are HARNESS_ERROR and cannot satisfy an expected mutant.

## Frozen package

- pre-run-spec-v3.md
- check-transaction.sh
- run-fixtures.sh

## Execution rule

Obtain a third independent static review of the corrected bytes. Run Bash syntax checks, then run the fixture package once. Preserve the third reader response exactly and separately from run evidence. Record each case, expected class, observed class, exit status, exact checker output, aggregate result, Bash version, file hashes, and line counts. Do not change the live Forge repository during the experiment.
```

#### Read-only checker

```bash
#!/usr/bin/env bash
set -u

fail() {
  printf 'FAIL %s\n' "$1" >&2
  exit 1
}

trim() {
  local value=$1
  value="${value#"${value%%[![:space:]]*}"}"
  value="${value%"${value##*[![:space:]]}"}"
  REPLY=$value
}

safe_rel() {
  local value=$1
  [[ -n $value ]] || return 1
  case "$value" in
    /*|..|../*|*/..|*/../*) return 1 ;;
  esac
  return 0
}

yaml_scalar() {
  local file=$1 key=$2 line value='' opened=0 count=0
  while IFS= read -r line || [[ -n $line ]]; do
    if [[ $line == '---' ]]; then
      if (( opened == 0 )); then
        opened=1
        continue
      fi
      break
    fi
    if (( opened == 1 )) && [[ $line == "$key: "* ]]; then
      value=${line#*: }
      ((count += 1))
    fi
  done < "$file"
  (( count == 1 )) || return 1
  REPLY=$value
}

count_exact_line() {
  local file=$1 wanted=$2 line count=0
  while IFS= read -r line || [[ -n $line ]]; do
    [[ $line == "$wanted" ]] && ((count += 1))
  done < "$file"
  REPLY=$count
}

(( $# == 7 )) || fail 'usage: ROOT MODE PIPELINE ARTIFACT ARTIFACT_ID ENT_ID EXPECTED_STAGE'
root=$1
mode=$2
pipeline=$3
artifact_rel=$4
artifact_id=$5
ent_id=$6
expected_stage=$7

[[ -d $root ]] || fail 'root directory missing'
safe_rel "$artifact_rel" || fail 'artifact path is not repository-relative'
artifact="$root/$artifact_rel"
status="$root/STATUS.md"
progress="$root/logbook/progress.log"
[[ -f $artifact ]] || fail 'artifact missing'
[[ -f $status ]] || fail 'STATUS missing'
[[ -f $progress ]] || fail 'progress log missing'

yaml_scalar "$artifact" pipeline || fail 'artifact pipeline missing or ambiguous'
[[ $REPLY == "$pipeline" ]] || fail 'artifact pipeline mismatch'
yaml_scalar "$artifact" id || fail 'artifact id missing or ambiguous'
[[ $REPLY == "$artifact_id" ]] || fail 'artifact id mismatch'
yaml_scalar "$artifact" tier || fail 'artifact tier missing or ambiguous'
artifact_tier=$REPLY

case "$mode" in
  open-research)
    [[ $artifact_rel == forge/research/*.md ]] || fail 'artifact path does not match research mode'
    artifact_name=${artifact_rel#forge/research/}
    [[ $artifact_name != */* ]] || fail 'research artifact is not a direct child'
    [[ $artifact_tier == research ]] || fail 'artifact tier does not match research mode'
    [[ $expected_stage == research ]] || fail 'declared stage does not match research mode'
    ;;
  closed-evaluation-reject)
    [[ $artifact_rel == forge/graveyard/*-evaluation-*.md ]] || fail 'artifact path does not match closure mode'
    artifact_name=${artifact_rel#forge/graveyard/}
    [[ $artifact_name != */* ]] || fail 'closure artifact is not a direct child'
    [[ $artifact_tier == evaluation ]] || fail 'artifact tier does not match closure mode'
    [[ $expected_stage == evaluate ]] || fail 'declared stage does not match closure mode'
    ;;
  *) fail 'unsupported transaction mode' ;;
esac

link_count=0
opened=0
in_links=0
while IFS= read -r line || [[ -n $line ]]; do
  if [[ $line == '---' ]]; then
    if (( opened == 0 )); then
      opened=1
      continue
    fi
    break
  fi
  (( opened == 1 )) || continue
  if [[ $line == 'links:' ]]; then
    in_links=1
    continue
  fi
  if (( in_links == 1 )) && [[ $line == '  - '* ]]; then
    link=${line#  - }
    if [[ $link == forge/* ]]; then
      safe_rel "$link" || fail 'unsafe local artifact link'
      [[ -f "$root/$link" ]] || fail 'local artifact link does not resolve'
      yaml_scalar "$root/$link" pipeline || fail 'linked artifact pipeline missing or ambiguous'
      [[ $REPLY == "$pipeline" ]] || fail 'linked artifact pipeline mismatch'
      ((link_count += 1))
    fi
    continue
  fi
  if (( in_links == 1 )) && [[ $line != ' '* ]]; then
    in_links=0
  fi
done < "$artifact"
(( link_count >= 1 )) || fail 'no resolving same-pipeline local artifact link'

target_count=0
in_target=0
ref_count=0
pipeline_count=0
stage_count=0
artifact_count=0
next_count=0
verdict_count=0
event_ref=''
event_see=''
event_pipeline=''
event_stage=''
event_artifact=''
event_next=''
event_verdict=''
while IFS= read -r line || [[ -n $line ]]; do
  if [[ $line == '## [ENT-'* ]]; then
    in_target=0
    remaining=$line
    line_target_count=0
    needle="[$ent_id]"
    while [[ $remaining == *"$needle"* ]]; do
      remaining=${remaining#*"$needle"}
      ((line_target_count += 1))
    done
    ((target_count += line_target_count))
    if (( line_target_count > 0 )); then
      (( line_target_count == 1 )) || fail 'selected ENT repeats within one header'
      in_target=1
      remaining=$line
      pipe_count=0
      while [[ $remaining == *'|'* ]]; do
        remaining=${remaining#*|}
        ((pipe_count += 1))
      done
      (( pipe_count == 5 )) || fail 'target event header field count mismatch'
      IFS='|' read -r header_entry header_time header_author header_category header_ref header_see <<< "$line"
      trim "$header_entry"
      [[ $REPLY == "## [$ent_id]" ]] || fail 'target event header identity mismatch'
      trim "$header_time"
      [[ -n $REPLY ]] || fail 'target event header lacks time'
      trim "$header_author"
      [[ -n $REPLY ]] || fail 'target event header lacks author'
      trim "$header_category"
      [[ -n $REPLY ]] || fail 'target event header lacks category'
      trim "$header_ref"
      header_ref=$REPLY
      trim "$header_see"
      header_see=$REPLY
      [[ $header_ref == 'ref: '* ]] || fail 'target event header lacks one ref'
      [[ $header_see == 'see: '* ]] || fail 'target event header lacks one see'
      event_ref=${header_ref#ref: }
      event_see=${header_see#see: }
      [[ -n $event_ref ]] || fail 'target event header has empty ref'
      [[ -n $event_see ]] || fail 'target event header has empty see'
      ((ref_count += 1))
    fi
    continue
  fi
  (( in_target == 1 )) || continue
  case "$line" in
    'Pipeline: '*) event_pipeline=${line#Pipeline: }; ((pipeline_count += 1)) ;;
    'Stage: '*) event_stage=${line#Stage: }; event_stage=${event_stage%%.*}; ((stage_count += 1)) ;;
    'Artifact: '*) event_artifact=${line#Artifact: }; event_artifact=${event_artifact%.}; ((artifact_count += 1)) ;;
    'Next: '*) event_next=${line#Next: }; event_next=${event_next%%;*}; event_next=${event_next%.}; trim "$event_next"; event_next=$REPLY; ((next_count += 1)) ;;
    'Verdict: '*) event_verdict=${line#Verdict: }; event_verdict=${event_verdict%%;*}; event_verdict=${event_verdict%.}; ((verdict_count += 1)) ;;
  esac
done < "$progress"

(( target_count == 1 )) || fail 'selected ENT is absent or ambiguous'
(( ref_count == 1 )) || fail 'event ref is ambiguous'
(( pipeline_count == 1 )) || fail 'event Pipeline is missing or ambiguous'
(( stage_count == 1 )) || fail 'event Stage is missing or ambiguous'
(( artifact_count == 1 )) || fail 'event Artifact is missing or ambiguous'
(( next_count == 1 )) || fail 'event Next is missing or ambiguous'
[[ $event_ref == "$artifact_rel" ]] || fail 'event ref mismatch'
[[ $event_see == "$artifact_id" ]] || fail 'event see mismatch'
[[ $event_pipeline == "$pipeline" ]] || fail 'event Pipeline mismatch'
[[ $event_stage == "$expected_stage" ]] || fail 'event Stage mismatch'
[[ $event_artifact == "$artifact_id" ]] || fail 'event Artifact mismatch'

status_count=0
status_state=''
status_stage=''
status_artifact=''
while IFS= read -r line || [[ -n $line ]]; do
  [[ $line == '|'* ]] || continue
  IFS='|' read -r _ row_pipeline row_state row_stage row_artifact row_next row_updated row_extra <<< "$line"
  trim "$row_pipeline"
  row_pipeline=$REPLY
  [[ $row_pipeline == "$pipeline" ]] || continue
  ((status_count += 1))
  trim "$row_state"
  status_state=$REPLY
  trim "$row_stage"
  status_stage=$REPLY
  trim "$row_artifact"
  status_artifact=$REPLY
done < "$status"

case "$mode" in
  open-research)
    (( status_count == 1 )) || fail 'open pipeline STATUS row is absent or ambiguous'
    [[ $status_state == active ]] || fail 'open pipeline state mismatch'
    [[ $status_stage == evaluate ]] || fail 'open pipeline handoff stage mismatch'
    [[ $status_artifact == "$artifact_rel" ]] || fail 'open pipeline active-artifact mismatch'
    [[ $event_next == evaluate ]] || fail 'open event Next mismatch'
    ;;
  closed-evaluation-reject)
    (( status_count == 0 )) || fail 'closed pipeline remains in STATUS'
    (( verdict_count == 1 )) || fail 'closure event Verdict is missing or ambiguous'
    [[ $event_verdict == REJECT ]] || fail 'closure event Verdict mismatch'
    [[ $event_next == closed ]] || fail 'closure event Next mismatch'
    count_exact_line "$artifact" '**Verdict: REJECT.**'
    (( REPLY == 1 )) || fail 'artifact REJECT marker is missing or ambiguous'
    ;;
esac

printf 'PASS %s %s %s %s\n' "$mode" "$pipeline" "$artifact_rel" "$ent_id"
```

#### Fixture runner

```bash
#!/usr/bin/env bash
set -eu

(( $# == 2 )) || { printf 'usage: CHECKER WORKDIR\n' >&2; exit 2; }
checker=$1
work=$2
[[ -f $checker ]] || { printf 'checker missing\n' >&2; exit 2; }
[[ ! -e $work ]] || { printf 'workdir already exists\n' >&2; exit 2; }
mkdir -p -- "$work"

write_lines() {
  local path=$1
  shift
  mkdir -p -- "${path%/*}"
  printf '%s\n' "$@" > "$path"
}

write_status_header() {
  write_lines "$1/STATUS.md" \
    '| pipeline | state | stage | active-artifact | next-action | updated |' \
    '|:--|:--|:--|:--|:--|:--|'
}

make_open() {
  local root=$1
  write_lines "$root/forge/ideas/fixture-root-r01.md" \
    '---' \
    'name: fixture-root' \
    'id: 20260921T152802Z' \
    'tier: idea' \
    'pipeline: 20260921T152802Z' \
    'author: Analyst' \
    'tags: [fixture]' \
    'links: []' \
    'confidence: low' \
    '---' \
    '# Fixture Root'
  write_lines "$root/forge/ideas/unrelated-root-r01.md" \
    '---' \
    'name: unrelated-root' \
    'id: 20260921T000001Z' \
    'tier: idea' \
    'pipeline: 20260921T000001Z' \
    'author: Analyst' \
    'tags: [fixture]' \
    'links: []' \
    'confidence: low' \
    '---' \
    '# Unrelated Fixture Root'
  write_lines "$root/forge/research/fixture-research-r02.md" \
    '---' \
    'name: fixture-research' \
    'id: 20260930T010200Z' \
    'tier: research' \
    'pipeline: 20260921T152802Z' \
    'author: Researcher' \
    'tags: [fixture]' \
    'links:' \
    '  - forge/ideas/fixture-root-r01.md' \
    'confidence: medium' \
    '---' \
    '# Fixture Research'
  write_status_header "$root"
  printf '%s\n' '| 20260921T152802Z | active | evaluate | forge/research/fixture-research-r02.md | Evaluate the bounded fixture. | 2026-09-30T01:02:01Z |' >> "$root/STATUS.md"
  write_lines "$root/logbook/progress.log" \
    '## [ENT-007] | 2026-09-21 15:28 UTC | Analyst | research | ref: forge/ideas/unrelated-root-r01.md | see: 20260921T000001Z' \
    'Pipeline: 20260921T000001Z' \
    'Stage: ideate. Result: PASS.' \
    'Artifact: 20260921T000001Z.' \
    'Next: research.' \
    '' \
    '## [ENT-008] | 2026-09-30 01:02 UTC | Researcher | research | ref: forge/research/fixture-research-r02.md | see: 20260930T010200Z' \
    'Pipeline: 20260921T152802Z' \
    'Stage: research. Result: PASS.' \
    'Artifact: 20260930T010200Z.' \
    'Next: evaluate.'
}

make_closed() {
  local root=$1
  write_lines "$root/forge/ideas/fixture-closed-root-r01.md" \
    '---' \
    'name: fixture-closed-root' \
    'id: 20260921T114301Z' \
    'tier: idea' \
    'pipeline: 20260921T114301Z' \
    'author: Analyst' \
    'tags: [fixture]' \
    'links: []' \
    'confidence: low' \
    '---' \
    '# Fixture Closed Root'
  write_lines "$root/forge/graveyard/fixture-closed-evaluation-r02.md" \
    '---' \
    'name: fixture-closed-evaluation' \
    'id: 20260921T143617Z' \
    'tier: evaluation' \
    'pipeline: 20260921T114301Z' \
    'author: Analyst' \
    'tags: [fixture]' \
    'links:' \
    '  - forge/ideas/fixture-closed-root-r01.md' \
    'confidence: medium' \
    '---' \
    '# Fixture Closed Evaluation' \
    '' \
    '**Verdict: REJECT.**'
  write_status_header "$root"
  write_lines "$root/logbook/progress.log" \
    '## [ENT-005] | 2026-09-21 14:37 UTC | Analyst | review | ref: forge/graveyard/fixture-closed-evaluation-r02.md | see: 20260921T143617Z' \
    'Pipeline: 20260921T114301Z' \
    'Stage: evaluate. Result: PASS.' \
    'Artifact: 20260921T143617Z.' \
    'Verdict: REJECT; pipeline closed.' \
    'Next: closed; STATUS row removed.' \
    '' \
    '## [ENT-006] | 2026-09-21 15:28 UTC | Analyst | research | ref: forge/ideas/later-r01.md | see: 20260921T152802Z' \
    'Pipeline: 20260921T152802Z' \
    'Stage: ideate. Result: PASS.' \
    'Artifact: 20260921T152802Z.' \
    'Next: research.'
}

replace_line() {
  local file=$1 old=$2 new=$3 line output='' count=0
  while IFS= read -r line || [[ -n $line ]]; do
    if [[ $line == "$old" ]]; then
      line=$new
      ((count += 1))
    fi
    output+="$line"$'\n'
  done < "$file"
  (( count == 1 )) || { printf 'mutation replacement count %d for %s\n' "$count" "$file" >&2; exit 2; }
  printf '%s' "$output" > "$file"
}

mutate() {
  local case_id=$1 root=$2
  case "$case_id" in
    M01)
      replace_line "$root/logbook/progress.log" \
        '## [ENT-007] | 2026-09-21 15:28 UTC | Analyst | research | ref: forge/ideas/unrelated-root-r01.md | see: 20260921T000001Z' \
        '## [ENT-008] | 2026-09-21 15:28 UTC | Analyst | research | ref: forge/ideas/unrelated-root-r01.md | see: 20260921T000001Z'
      ;;
    M02)
      replace_line "$root/forge/research/fixture-research-r02.md" 'pipeline: 20260921T152802Z' 'pipeline: 20260921T152803Z'
      ;;
    M03)
      replace_line "$root/forge/research/fixture-research-r02.md" 'tier: research' 'tier: idea'
      ;;
    M04)
      replace_line "$root/logbook/progress.log" \
        '## [ENT-008] | 2026-09-30 01:02 UTC | Researcher | research | ref: forge/research/fixture-research-r02.md | see: 20260930T010200Z' \
        '## [ENT-008] | 2026-09-30 01:02 UTC | Researcher | research | ref: forge/research/missing-r02.md | see: 20260930T010200Z'
      ;;
    M05)
      replace_line "$root/logbook/progress.log" 'Pipeline: 20260921T152802Z' 'Pipeline: 20260921T152803Z'
      ;;
    M06)
      replace_line "$root/logbook/progress.log" 'Stage: research. Result: PASS.' 'Stage: propose. Result: PASS.'
      ;;
    M07)
      replace_line "$root/logbook/progress.log" 'Artifact: 20260930T010200Z.' 'Artifact: 20260921T152802Z.'
      ;;
    M08)
      replace_line "$root/forge/research/fixture-research-r02.md" '  - forge/ideas/fixture-root-r01.md' '  - forge/ideas/missing-root-r01.md'
      ;;
    M09)
      replace_line "$root/STATUS.md" \
        '| 20260921T152802Z | active | evaluate | forge/research/fixture-research-r02.md | Evaluate the bounded fixture. | 2026-09-30T01:02:01Z |' \
        '| 20260921T152802Z | active | evaluate | forge/research/missing-r02.md | Evaluate the bounded fixture. | 2026-09-30T01:02:01Z |'
      ;;
    M10)
      replace_line "$root/STATUS.md" \
        '| 20260921T152802Z | active | evaluate | forge/research/fixture-research-r02.md | Evaluate the bounded fixture. | 2026-09-30T01:02:01Z |' \
        '| 20260921T152802Z | active | propose | forge/research/fixture-research-r02.md | Evaluate the bounded fixture. | 2026-09-30T01:02:01Z |'
      ;;
    M11)
      replace_line "$root/logbook/progress.log" 'Verdict: REJECT; pipeline closed.' 'Verdict: DEFER; pipeline closed.'
      ;;
    valid-open-research|valid-closed-evaluation-reject) ;;
    *) printf 'unknown case %s\n' "$case_id" >&2; exit 2 ;;
  esac
}

matched=0
total=0
run_one() {
  local case_id=$1 mode=$2 pipeline=$3 artifact=$4 artifact_id=$5 ent_id=$6 stage=$7 expected=$8 root output_file output rc actual line output_lines=0
  root="$work/$case_id"
  if [[ $mode == open-research ]]; then
    make_open "$root"
  else
    make_closed "$root"
  fi
  mutate "$case_id" "$root"
  output_file="$root/checker.out"
  if bash --noprofile --norc "$checker" "$root" "$mode" "$pipeline" "$artifact" "$artifact_id" "$ent_id" "$stage" > "$output_file" 2>&1; then
    rc=0
  else
    rc=$?
  fi
  output=$(<"$output_file")
  while IFS= read -r line || [[ -n $line ]]; do
    ((output_lines += 1))
  done < "$output_file"
  if (( rc == 0 )) && (( output_lines == 1 )) && [[ $output == 'PASS '* ]]; then
    actual=PASS
  elif (( rc == 1 )) && (( output_lines == 1 )) && [[ $output == 'FAIL '* ]]; then
    actual=FAIL
  else
    actual=HARNESS_ERROR
  fi
  ((total += 1))
  if [[ $actual == "$expected" ]]; then
    ((matched += 1))
  fi
  printf '%s|%s|%s|%d|%s\n' "$case_id" "$expected" "$actual" "$rc" "$output"
}

printf 'case|expected|observed|exit|checker-output\n'
run_one valid-open-research open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research PASS
run_one valid-closed-evaluation-reject closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md 20260921T143617Z ENT-005 evaluate PASS
run_one M01 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M02 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M03 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M04 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M05 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M06 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M07 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M08 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M09 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M10 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M11 closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md 20260921T143617Z ENT-005 evaluate FAIL

if (( matched == total )); then all_expected=true; else all_expected=false; fi
printf 'SUMMARY|total=%d|matched=%d|all_expected=%s\n' "$total" "$matched" "$all_expected"
(( matched == total ))
```

#### Final static-reader output

```text
VERDICT: ACCEPT

1. Frozen package identity
   - pre-run-spec-v3.md: 77 lines, 4717 bytes, SHA-256 59b19e04c2e060203a41de0f86a1f4d3e8a069e639d44e07d2c2293b9260d686
   - check-transaction.sh: 246 lines, 8716 bytes, SHA-256 822063f44a8cfa64cb4bbb0398acf5b93e00c1a1c4455bd97a56e67f151fed42
   - run-fixtures.sh: 238 lines, 9658 bytes, SHA-256 14f89b62a25d030bbe72494efe43df5c686b978e54971d05be42fb3aeddd8e6f
   - All three files are ASCII.

2. Frozen invariants
   - I01: The checker counts each requested bracketed ENT occurrence on event-header lines, requires exactly one total occurrence, rejects repetition within a header, requires exactly five pipe delimiters for six fields, and validates the identity, time, author, category, ref, and see fields.
   - I02: The artifact pipeline must equal the requested pipeline.
   - I03: Open research artifacts must be direct children of forge/research with tier research. Closed rejection evaluations must be direct children of forge/graveyard with tier evaluation.
   - I04: The selected event ref must equal the supplied artifact path.
   - I05: The selected event Pipeline must equal the supplied pipeline.
   - I06: The selected event Stage must match the mode-bound stage.
   - I07: Event Artifact and header see must both equal the supplied artifact ID.
   - I08: At least one local forge link must resolve to a file with the same pipeline.
   - I09: Open research requires exactly one matching STATUS row with state active, stage evaluate, the selected artifact, and event Next token evaluate.
   - I10: Closed evaluation-REJECT requires no matching STATUS row, one event Verdict of REJECT, event Next token closed, and exactly one artifact line equal to **Verdict: REJECT.**

3. Exact parsing constraints
   - Artifact paths are repository-relative and textually restricted to direct children; nested paths are rejected after mode-specific prefix removal.
   - The closure Next value is reduced to its semantic token before exact comparison, so the fixture form "closed; STATUS row removed." resolves to exactly "closed".
   - Unsupported modes fail explicitly. The checker implements only open-research and closed-evaluation-reject.

4. Positive controls
   - valid-open-research is internally consistent across artifact metadata, same-pipeline link, selected event, and STATUS handoff.
   - valid-closed-evaluation-reject is internally consistent across artifact metadata, same-pipeline link, selected event, absent STATUS row, event verdict, closure token, and artifact verdict marker.
   - No static contradiction would prevent either control from reaching its PASS line.

5. Mutants
   - M01 through M11 each replace exactly one fixture line.
   - Each mutation targets its stated invariant: duplicate ENT, artifact pipeline, tier, event ref, event Pipeline, event Stage, event Artifact, linked path, STATUS artifact, STATUS stage, or closure event verdict.
   - Each mutant has a corresponding checker rejection path.
   - M05 is unique within the generated open progress log because the unrelated event uses pipeline 20260921T000001Z while the selected event alone uses 20260921T152802Z.

6. Harness behavior
   - Setup is fail-fast through set -eu, checked workdir nonexistence, write failures, and exact-one mutation replacement counts.
   - PASS requires exit 0 and exactly one "PASS " line.
   - FAIL requires exit 1 and exactly one "FAIL " line.
   - Every other exit or output shape is HARNESS_ERROR and cannot satisfy a mutant expected to produce FAIL.
   - Combined checker stdout and stderr are preserved in a separate checker.out file for every case. Aggregate display may remove trailing newlines through command substitution, but the raw files retain the original combined output.
   - The final summary and process status require all 13 cases to match their expected classes.

7. Read-only property
   - check-transaction.sh contains no repository write, creation, deletion, rename, permission-change, or external mutation operation. Its only output is the final PASS line or one FAIL line.
   - Fixture creation and checker-output capture are confined to run-fixtures.sh and its caller-supplied new work directory.

8. Limitations
   - This is a static review only. Neither script was executed, and no syntax-check or fixture-run result is claimed.
   - Acceptance is limited to the two frozen transaction shapes, the two supplied controls, and M01-M11. It does not establish support for other Forge lifecycle shapes or exhaustive resistance to adversarial filesystem conditions such as symlink substitution or mid-read permission changes.
   - No files were created or modified during this review.
```

#### Exact commands

```text
bash -n /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r02-20260930T010157Z/check-transaction.sh && bash -n /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r02-20260930T010157Z/run-fixtures.sh && printf 'SYNTAX_OK\n'

bash --noprofile --norc /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r02-20260930T010157Z/run-fixtures.sh /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r02-20260930T010157Z/check-transaction.sh /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r02-20260930T010157Z/fixture-run-v3
```

The syntax command exited 0 with `SYNTAX_OK`. The fixture command exited 0.

#### Raw per-case output files

Each `checker.out` contained exactly one LF-terminated line:

```text
valid-open-research: PASS open-research 20260921T152802Z forge/research/fixture-research-r02.md ENT-008
valid-closed-evaluation-reject: PASS closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md ENT-005
M01: FAIL selected ENT is absent or ambiguous
M02: FAIL artifact pipeline mismatch
M03: FAIL artifact tier does not match research mode
M04: FAIL event ref mismatch
M05: FAIL event Pipeline mismatch
M06: FAIL event Stage mismatch
M07: FAIL event Artifact mismatch
M08: FAIL local artifact link does not resolve
M09: FAIL open pipeline active-artifact mismatch
M10: FAIL open pipeline handoff stage mismatch
M11: FAIL closure event Verdict mismatch
```

#### Aggregate run output

```text
case|expected|observed|exit|checker-output
valid-open-research|PASS|PASS|0|PASS open-research 20260921T152802Z forge/research/fixture-research-r02.md ENT-008
valid-closed-evaluation-reject|PASS|PASS|0|PASS closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md ENT-005
M01|FAIL|FAIL|1|FAIL selected ENT is absent or ambiguous
M02|FAIL|FAIL|1|FAIL artifact pipeline mismatch
M03|FAIL|FAIL|1|FAIL artifact tier does not match research mode
M04|FAIL|FAIL|1|FAIL event ref mismatch
M05|FAIL|FAIL|1|FAIL event Pipeline mismatch
M06|FAIL|FAIL|1|FAIL event Stage mismatch
M07|FAIL|FAIL|1|FAIL event Artifact mismatch
M08|FAIL|FAIL|1|FAIL local artifact link does not resolve
M09|FAIL|FAIL|1|FAIL open pipeline active-artifact mismatch
M10|FAIL|FAIL|1|FAIL open pipeline handoff stage mismatch
M11|FAIL|FAIL|1|FAIL closure event Verdict mismatch
SUMMARY|total=13|matched=13|all_expected=true
```

## Alternatives and Implications

| Alternative | Evidence-supported benefit | Cost or limit |
|:--|:--|:--|
| Do nothing | No code, integration, dependency, or maintenance cost; manual protocol review remains authoritative. | The current executable gates do not inspect the relational transaction contract.[3][5] |
| Explicit manual field checklist | Can cover more lifecycle shapes immediately and remains easy to revise. | Produces no machine evidence that the exact target was checked; still depends on human execution. |
| Frozen two-shape checker | Complete package is inspectable and rerunnable; both controls passed and all eleven declared mutants failed. | Supports only two shapes, adds 246 checker lines plus 238 runner lines, and does not measure maintenance cost or live integration behavior. |
| Broad lifecycle validator | Could attempt wider coverage. | The prior 707-line validator was part of a reverted 43-file system change; this revision supplies no evidence for deployment, locks, monitors, semantic grading, or all lifecycle states.[6] |

The smallest evidence-supported implication is not implementation. It is that an
independent evaluator can now extract and rerun the exact two-shape package
without trusting hashes or this author's runtime narrative. If that evaluator
reproduces the matrix and judges the narrow maintenance surface worthwhile, a
proposal could compare one explicitly limited local checker with the manual
checklist. If the proposal needs another lifecycle shape, automatic target
selection, symlink defense, concurrent-writer protection, CI installation, or
semantic quality claims, the current evidence is insufficient.

The unattended-command pipeline supplies a useful comparison. Its complete
in-report bytes and calls enabled a later evaluator to reproduce three claimed
safe-route outcomes, while explicitly limiting unmeasured chronology and
portability.[7] This revision applies the same preservation method to the
transaction checker; it does not infer that the checker is therefore worth
deploying.

## Response to Feedback and Remaining Questions

1. **Complete durable package:** Answered. The exact v3 specification, checker,
   runner, fixture definitions, mutation overlays, commands, reader output,
   raw case lines, aggregate output, hashes, line counts, and Bash version are
   preserved above. Another evaluator can inspect and rerun them. Scratch paths
   are not required for reconstruction.
2. **Dated pre-run specification and reader evidence:** Partly answered with an
   explicit limitation. A dated specification and unmerged reader output were
   captured before execution, but this post-run commit cannot independently
   prove their chronology or model independence. They are excluded from support
   for the runtime result. No blind or independently dated review claim remains.
3. **Positive controls and claimed scope:** Answered by narrowing. The only
   claimed shapes are open research-to-evaluate and terminal evaluation-REJECT.
   Every other stage/state shape remains unsupported.
4. **Implementation size, dependencies, target, failure, and maintenance:**
   Answered. The checker is 246 Bash lines, uses Bash builtins, requires seven
   explicit target arguments, emits one PASS or FAIL line, and performs no
   writes. The runner is 238 lines and treats other exits or output shapes as
   `HARNESS_ERROR`. The package is narrower than the historical validator but
   not proven cheaper than no change or a manual checklist.

No blocking package-preservation gap remains for the two declared shapes.
Decision-relevant questions remain for evaluation:

- Does an independent extraction and rerun reproduce all thirteen outcomes from
  the committed artifact?
- Is two-shape coverage useful enough for a proposal, or too narrow to justify
  maintaining 484 shell lines?
- Can a proposal keep explicit target arguments and manual semantic review
  without implying automatic target discovery or general lifecycle coverage?
- Would the first required production shape beyond these controls make the
  narrow checker converge toward the reverted validator?

Confidence is medium. It is supported by current gate source inspection, a
complete frozen package, two accepted controls, eleven rejected one-line
mutants, exact outputs, measured size and dependencies, and an unchanged live
repository. It is limited by two positive shapes, rule-derived mutants, one
Bash environment, no independent post-commit rerun yet, no measured maintenance
cost, and no live integration test. Confidence would rise after a separate
evaluator extracts and reruns the committed package with identical results. It
would fall if extraction changes bytes, a valid instance of either claimed
shape fails, a mutant passes, or useful scope requires additional lifecycle or
runtime machinery.

## Sources

1. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- root
   question, bounded negative-fixture plan, support conditions, stop conditions,
   and broad-validator exclusion. [high]
2. `forge/research/evidence-gated-forge-transaction-checker-r01.md` -- prior
   research revision, ten invariants, reported matrix, missing package bytes,
   alternatives, and stated limits. [high]
3. `forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md`
   -- exact REVISE handoff, independently checked current-gate gap, missing
   evidence classes, four blocking questions, correction count, and required
   positive-scope alignment. [high]
4. `forge/protocol.md` -- stage independence, artifact contract, revision links,
   transaction scope, handoff, and write boundary. [high]
   - `logbook/protocol.md` -- exact ENT targeting, append-only event format, and
     artifact-STATUS-event agreement. [high]
   - `LEARNINGS.md` -- current package, fixture, raw-output, and separate-reader
     preservation lesson, with stricter limits on chronology claims. [high]
5. `scripts/validate-ids.sh` -- current ID-only parser and checks; no STATUS,
   event, link, transition, or closure relationship parsing. [high]
   - `.github/workflows/ascii-guard.yml` -- current tracked-text ASCII scan and
     sole invocation of the ID validator. [high]
6. `scripts/validate-forge.py` -- 707-line historical validator at Git commit
   `682fbb4a3184654e62e70fc2d1fa620af2fbee7d`, added within a 43-file system
   change and removed by immediate revert
   `35b8213f39e6d813c00ec1b36776d077a697b27c`; used only as scope and
   maintenance counterevidence. [high]
7. `forge/research/unattended-forge-command-paths-r01.md` -- prior complete
   in-report fixture, call, and output preservation method. [high]
   - `forge/evaluations/unattended-forge-command-paths-evaluation-r01.md` --
     separate reproduction of the preserved package and explicit limits on
     chronology, portability, and decision value. [high]
8. `agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md`
   -- evaluation contracts, accepted-and-rejected auditing, raw artifacts,
   grader limits, and false-pass risk. [medium]
9. `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md`
   -- exact revision evidence, fail-to-pass and pass-to-pass checks, durable
   handoff packages, and bounded meaning of test success. [medium]
10. `agentic-brain:reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md`
    -- exact-target validator defect exposed by negative fixtures; internal
    operational evidence, not independent proof of this run. [medium]
11. PIT. "Basic Concepts," undated; accessed 2026-09-30, Mutation Operators,
    Mutants, and Running the tests sections. Deliberate fault insertion and the
    bounded meaning of a killed mutant were checked.
    https://pitest.org/quickstart/basic_concepts/ [medium]
12. GNU Project. "Bash Reference Manual," edition 5.3, 2025-05-18; accessed
    2026-09-30, Bash features, conditional constructs, and exit-status sections.
    The documented shell is the package dependency; the exercised local version
    was recorded separately.
    https://www.gnu.org/software/bash/manual/bash.html [high]
13. GitHub. "Setting exit codes for actions," undated; accessed 2026-09-30.
    Nonzero action exit status as a failure signal was checked; no GitHub Action
    execution is claimed.
    https://docs.github.com/en/actions/how-tos/create-and-publish-actions/set-exit-codes [high]
