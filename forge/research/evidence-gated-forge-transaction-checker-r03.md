---
name: evidence-gated-forge-transaction-checker
id: 20260930T031626Z
tier: research
pipeline: 20260921T152802Z
author: Researcher
tags: [agent-systems, forge, verification, state-consistency]
links:
  - forge/ideas/evidence-gated-forge-transaction-checker-r01.md
  - forge/research/evidence-gated-forge-transaction-checker-r01.md
  - forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md
  - forge/research/evidence-gated-forge-transaction-checker-r02.md
  - forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r02.md
  - forge/protocol.md
  - logbook/protocol.md
  - LEARNINGS.md
  - scripts/validate-ids.sh
  - .github/workflows/ascii-guard.yml
  - agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:reflections/2026-09-14_morpheus_coverage-needs-a-selection-order.md
  - agentic-brain:reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - agentic-brain:reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md
  - https://www.gnu.org/software/bash/manual/bash.html
  - https://docs.github.com/en/actions/how-tos/create-and-publish-actions/set-exit-codes
confidence: medium
---
# Research Revision 3: Evidence-Gated Forge Transaction Checker

## Question and Method

This final permitted correction answers the four blocking questions in evaluation
revision 2.[4] It asks whether the exact meaning of the checker result can be
mapped before execution; whether event Result, category, and artifact-event
author agreement can be checked in both retained shapes; whether the corrected
package preserves the two controls and all prior mutants without a harness
error; and whether the resulting two-shape package shows enough advantage over
the manual transaction check to justify further proposal work.

The selected pipeline is `20260921T152802Z`. The root idea author is Analyst and
this research author is Researcher, satisfying the research-stage independence
rule.[1][5] The stage began from clean Forge HEAD
`fd7e5e8a40992a8f49da2f6bda86ac7c4d3fb86b`. The selected input was
`forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r02.md`,
which returned the pipeline to research as corrective cycle 2 of 2.[4]

Before further targeted work, the provisional explanation was that revision 2
had a real target-centered checker but used a generic `PASS` for a narrower
claim and omitted three fields inside both claimed shapes. The disconfirming
conditions were a rejected shape control, an accepted in-scope mutant, a
harness error counted as an expected failure, a checker write, a lifecycle-mode
expansion, or an output still implying complete Forge transaction validity.
This provisional explanation and the field map were frozen before execution in
the specification reproduced below.

The evidence sequence was:

1. read the complete idea, both prior research revisions, both evaluations, the
   current controls, logs, read-only `LEARNINGS.md`, and the canonical research
   and Feynman procedures;
2. query and read the relevant Forge and Brain records in full, then check the
   GNU Bash and GitHub exit-status documentation directly;[3][4][7][8][9][10][11]
3. extract the exact revision-2 checker and runner, verify their original hashes,
   and change only the declared result boundary, category, and authorship logic
   plus their fixtures;
4. freeze specification v4 and obtain two separate static reviews before any
   execution;
5. accept the material finding that generic `PASS` still overclaimed the parser,
   correct two mutation-map attributions, rename the positive cases as shape
   controls, emit `PARTIAL_PASS`, and freeze specification v5;
6. obtain a final separate static `ACCEPT`, run Bash syntax checks, and execute
   the 19-case package once in scratch; and
7. verify all raw case files, package hashes, and unchanged live Forge HEAD and
   working tree.

No production checker, workflow, skill, profile, service, runtime, or live Forge
transaction was installed or changed by the experiment.

## Evidence and Findings

### The prior false-positive finding is exact

The first report and evaluation established the current-gate gap but left the
prototype package unavailable for independent checking.[2] Revision 2 preserved
that package and narrowed its claimed modes.[3]

Evaluation revision 2 independently extracted revision 2's package and
reproduced its thirteen declared classifications. It then changed the open
research event's `Result` from `PASS` to `FAIL`, category from `research` to
`error`, and author from `Researcher` to `Analyst` while leaving the artifact
as authored by Researcher. All three received the checker's generic `PASS`.[4]
Those fields are not additional lifecycle modes: they occur inside the claimed
open-research shape.

The protocol requires actual authorship records and agreement among the selected
artifact, handoff, and event. The logbook contract limits progress categories,
uses an actual-agent header, gives an exact `Stage: <stage>. Result: <result>.`
form, and defines a progress `PASS` as procedural completion.[5] The current
ASCII and ID gates still do not inspect those relationships; their source reads
show byte and frontmatter-ID checks only.[6]

Brain evidence supplies the same bounded design principle without proving this
package. Deterministic gates should remain close to rules they can enforce; a
check supports a claim only when it would fail in the relevant false world; and
accepted outputs as well as failures should be audited for false positives.[7][8]
The current Forge learning states the operational consequence: fixtures must be
derived from the claimed result boundary or the result must be labeled partial.[9]

### The corrected result is deliberately partial

Specification v5 maps thirteen target-centered predicates before execution. It
retains only `open-research` and `closed-evaluation-reject`. It adds three shared
relationships:

- I11 parses the selected Stage/Result line and requires `Result: PASS.`;
- I12 requires the exact frozen category `research` for the open shape and
  `review` for the closed shape; and
- I13 requires a nonempty artifact author and textual equality with the selected
  event author.

Each relationship has one open-shape and one closed-shape mutant. The author
check establishes textual agreement, not the identity of the real actor or
stage independence. The checker therefore emits `PARTIAL_PASS`, not `PASS`.
That output means only that I01-I13 held for the supplied target. It does not
certify complete metadata, template or Sources compliance, source quality,
authorship truth or independence, revision-chain correctness, every board row,
append-only history, or full transaction preservation.[5]

This narrowing answers a material static-review objection before execution. The
same review also found that the synthetic controls are parser-shape controls,
not complete Forge artifacts, and that the local-link and STATUS projections do
not cover the entire protocol. Those findings are reflected in the v5 claim;
they were not hidden by adding more lifecycle modes.

### The frozen package classified all nineteen cases as specified

The v5 specification was 79 lines and 6,411 bytes, the checker 270 lines and
9,680 bytes, the runner 270 lines and 12,170 bytes, and the final static review
9 lines and 795 bytes. Their SHA-256 values were, respectively:

- `ba607ea4d85bac5faf6776732e270a9f085e79a545ba601b3864fa2d4c7050dc`;
- `4d9e097af487e70bd62ea43df249e76ddc5028aff7f890eda5217c5eea63e347`;
- `779f656175469fb4571983fd910003ec702989ad888831bab8bd5a6e37a5345e`;
  and
- `7e2c9870d5f9654a91a877025c9d057d25562881befd2d954e6b5a7b2116755a`.

Both shell files passed `bash -n`. One run under GNU Bash
`5.2.21(1)-release` returned exit 0. Both shape controls returned one
`PARTIAL_PASS` line with exit 0. M01-M17 each returned one `FAIL` line with exit
1. The runner reported `total=19`, `matched=19`, and `all_expected=true`; no case
was classified `HARNESS_ERROR`. A separate post-run `wc -l` found exactly 19
`checker.out` files and one line in every file. Checker and runner hashes were
unchanged after execution. GNU documents the Bash implementation and
conditional/exit-status behavior used here; GitHub separately documents that a
nonzero action exit is a failure signal, although no GitHub Action was run.[10][11]

The live Forge remained at
`fd7e5e8a40992a8f49da2f6bda86ac7c4d3fb86b` with a clean working tree after
the scratch run. One combined post-run hash, raw-output, and repository-state
command was approval-blocked before any component ran. The checks were split
into read-only commands; all completed and are reported above. No approval or
configuration change was attempted.

The package and receipts follow. They are evidence inside this immutable
research artifact, not installable authority or a production implementation.

#### Pre-run specification v5

```text
# Pre-run Specification v5

Recorded: 2026-09-30T03:12:29Z
Revision reason: two separate static reviews found that v4's generic PASS overclaimed full transaction validity and that M03 and M06 were misattributed. The output is now PARTIAL_PASS, controls are named as shape controls, exclusions are explicit, and the mutation map is corrected before execution.
Forge starting HEAD: fd7e5e8a40992a8f49da2f6bda86ac7c4d3fb86b
Pipeline: 20260921T152802Z
Selected stage: research revision 3
Selected input: forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r02.md

## Provisional explanation

The revision-2 checker validated a target-centered subset of artifact-STATUS-event relationships but its generic PASS ignored event Result, category, and authorship agreement and implied more completeness than the parser supplied. A corrected package can remain limited to the same two transaction shapes if it derives the new checks from the claimed field boundary and emits an explicitly partial result. This explanation is provisional, not evidence.

## Gaps and disconfirmation

- A shape-control rejection, an accepted in-scope mutant, a harness error counted as FAIL, an ambiguous target, or a checker write disconfirms the corrected package.
- The supported shapes remain exactly open-research and closed-evaluation-reject. No additional lifecycle mode, automatic target selection, semantic review, deployment control, or live integration is allowed.
- PARTIAL_PASS means only that the listed I01-I13 predicates held for the supplied target. It does not certify complete protocol validity, source quality, template compliance, authorship truth or independence, revision-chain correctness, the entire board, append-only history, transaction preservation, or production readiness.
- Event author equality proves only agreement with artifact frontmatter. It does not prove who actually acted.
- Exact categories research and review are mode-specific accepted forms for these two frozen shapes. The package does not claim to accept every category use allowed elsewhere by logbook/protocol.md.
- The synthetic controls test parser acceptance for the listed predicates. They are not represented as complete Forge artifacts and do not estimate a general false-rejection rate.
- Passing fixtures does not establish economic value or exhaustive coverage.

## Contract-derived partial-result map

Every listed predicate is checked for both controls when applicable. Mutants are assigned from this map before execution.

- I01 target event identity and header shape: the requested bracketed ENT ID occurs once on an event header; the header has exactly six pipe-delimited fields, a nonempty time, one author, one category, one ref, and one see.
- I02 artifact pipeline: artifact pipeline equals the supplied root pipeline.
- I03 mode shape: artifact is a direct child of the mode directory, artifact tier matches the mode, and the supplied completed stage matches the mode.
- I04 event reference: header ref equals the supplied artifact path.
- I05 event pipeline: body Pipeline equals the supplied root pipeline.
- I06 event stage: body Stage equals the mode-bound completed stage.
- I07 artifact identity: artifact id, header see, and body Artifact equal the supplied artifact ID.
- I08 same-pipeline local-artifact witness: at least one frontmatter link beginning forge/ resolves to an artifact whose pipeline equals the supplied root. This is not a claim that every link resolves or that the witness is the correct intellectual input.
- I09 open handoff projection: one selected-pipeline STATUS row has state active, stage evaluate, and the supplied artifact; the selected event's Next semantic token is evaluate. This does not validate unrelated rows or all STATUS columns.
- I10 terminal rejection projection: the selected pipeline is absent from STATUS; one exact artifact REJECT marker and the selected event verdict are REJECT; the selected event's Next semantic token is closed.
- I11 successful result: the selected Stage line has the Stage/Result form and Result is PASS.
- I12 progress category: open-research uses category research and closed-evaluation-reject uses category review in the exact frozen shapes.
- I13 authorship agreement: artifact author is nonempty and selected event author equals it.

Rule sources: forge/protocol.md artifact, authorship, handoff, closure, and transaction rules; logbook/protocol.md progress categories, actual-agent header, Stage/Result format, PASS meaning, and exact reference rules. The partial result intentionally does not claim all rules from either file.

## Fixtures and expected outcomes

Shape controls:

- control-open-research: PARTIAL_PASS; exercises I01-I09 and I11-I13.
- control-closed-evaluation-reject: PARTIAL_PASS; exercises I01-I08 and I10-I13.

Single-line mutants, each expected FAIL:

- M01 duplicate the selected ENT header ID (I01).
- M02 change artifact pipeline (I02).
- M03 change artifact tier (I03).
- M04 change event ref to a missing artifact (I04).
- M05 change selected event Pipeline (I05).
- M06 change event Stage from research to propose (I06).
- M07 change event Artifact to the root idea ID (I07).
- M08 change artifact link to a missing path (I08).
- M09 change STATUS active-artifact to a missing path (I09).
- M10 change STATUS stage from evaluate to propose (I09).
- M11 change closure event verdict from REJECT to DEFER (I10).
- M12 change open event Result from PASS to FAIL (I11).
- M13 change open event category from research to error (I12).
- M14 change open event author from Researcher to Analyst while artifact author remains Researcher (I13).
- M15 change closed event Result from PASS to FAIL (I11).
- M16 change closed event category from review to research (I12).
- M17 change closed event author from Analyst to Researcher while artifact author remains Analyst (I13).

## Frozen package and execution rule

Files:

- pre-run-spec-v5.md
- check-transaction.sh
- run-fixtures.sh

Obtain a final separate static review of the corrected bytes. Correct any material defect before execution and issue another specification revision if needed. Then run Bash syntax checks and the fixture package once. Preserve line counts, byte counts, SHA-256 values, exact commands, raw per-case output, aggregate output, Bash version, and reviewer output. Do not change the live Forge repository during the experiment.
```

#### Corrected read-only checker

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
yaml_scalar "$artifact" author || fail 'artifact author missing or ambiguous'
artifact_author=$REPLY
[[ -n $artifact_author ]] || fail 'artifact author is empty'

case "$mode" in
  open-research)
    [[ $artifact_rel == forge/research/*.md ]] || fail 'artifact path does not match research mode'
    artifact_name=${artifact_rel#forge/research/}
    [[ $artifact_name != */* ]] || fail 'research artifact is not a direct child'
    [[ $artifact_tier == research ]] || fail 'artifact tier does not match research mode'
    [[ $expected_stage == research ]] || fail 'declared stage does not match research mode'
    expected_category=research
    ;;
  closed-evaluation-reject)
    [[ $artifact_rel == forge/graveyard/*-evaluation-*.md ]] || fail 'artifact path does not match closure mode'
    artifact_name=${artifact_rel#forge/graveyard/}
    [[ $artifact_name != */* ]] || fail 'closure artifact is not a direct child'
    [[ $artifact_tier == evaluation ]] || fail 'artifact tier does not match closure mode'
    [[ $expected_stage == evaluate ]] || fail 'declared stage does not match closure mode'
    expected_category=review
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
result_count=0
event_ref=''
event_see=''
event_author=''
event_category=''
event_pipeline=''
event_stage=''
event_result=''
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
      event_author=$REPLY
      [[ -n $event_author ]] || fail 'target event header lacks author'
      trim "$header_category"
      event_category=$REPLY
      [[ -n $event_category ]] || fail 'target event header lacks category'
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
    'Stage: '*)
      stage_payload=${line#Stage: }
      [[ $stage_payload == *'. Result: '* ]] || fail 'event Stage/Result format mismatch'
      event_stage=${stage_payload%%. Result: *}
      event_result=${stage_payload#*. Result: }
      [[ $event_result == *'.' ]] || fail 'event Result terminator missing'
      event_result=${event_result%.}
      ((stage_count += 1))
      ((result_count += 1))
      ;;
    'Artifact: '*) event_artifact=${line#Artifact: }; event_artifact=${event_artifact%.}; ((artifact_count += 1)) ;;
    'Next: '*) event_next=${line#Next: }; event_next=${event_next%%;*}; event_next=${event_next%.}; trim "$event_next"; event_next=$REPLY; ((next_count += 1)) ;;
    'Verdict: '*) event_verdict=${line#Verdict: }; event_verdict=${event_verdict%%;*}; event_verdict=${event_verdict%.}; ((verdict_count += 1)) ;;
  esac
done < "$progress"

(( target_count == 1 )) || fail 'selected ENT is absent or ambiguous'
(( ref_count == 1 )) || fail 'event ref is ambiguous'
(( pipeline_count == 1 )) || fail 'event Pipeline is missing or ambiguous'
(( stage_count == 1 )) || fail 'event Stage is missing or ambiguous'
(( result_count == 1 )) || fail 'event Result is missing or ambiguous'
(( artifact_count == 1 )) || fail 'event Artifact is missing or ambiguous'
(( next_count == 1 )) || fail 'event Next is missing or ambiguous'
[[ $event_ref == "$artifact_rel" ]] || fail 'event ref mismatch'
[[ $event_see == "$artifact_id" ]] || fail 'event see mismatch'
[[ $event_author == "$artifact_author" ]] || fail 'event author mismatch'
[[ $event_category == "$expected_category" ]] || fail 'event category mismatch'
[[ $event_pipeline == "$pipeline" ]] || fail 'event Pipeline mismatch'
[[ $event_stage == "$expected_stage" ]] || fail 'event Stage mismatch'
[[ $event_result == PASS ]] || fail 'event Result mismatch'
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

printf 'PARTIAL_PASS %s %s %s %s\n' "$mode" "$pipeline" "$artifact_rel" "$ent_id"
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
    M12)
      replace_line "$root/logbook/progress.log" 'Stage: research. Result: PASS.' 'Stage: research. Result: FAIL.'
      ;;
    M13)
      replace_line "$root/logbook/progress.log" \
        '## [ENT-008] | 2026-09-30 01:02 UTC | Researcher | research | ref: forge/research/fixture-research-r02.md | see: 20260930T010200Z' \
        '## [ENT-008] | 2026-09-30 01:02 UTC | Researcher | error | ref: forge/research/fixture-research-r02.md | see: 20260930T010200Z'
      ;;
    M14)
      replace_line "$root/logbook/progress.log" \
        '## [ENT-008] | 2026-09-30 01:02 UTC | Researcher | research | ref: forge/research/fixture-research-r02.md | see: 20260930T010200Z' \
        '## [ENT-008] | 2026-09-30 01:02 UTC | Analyst | research | ref: forge/research/fixture-research-r02.md | see: 20260930T010200Z'
      ;;
    M15)
      replace_line "$root/logbook/progress.log" 'Stage: evaluate. Result: PASS.' 'Stage: evaluate. Result: FAIL.'
      ;;
    M16)
      replace_line "$root/logbook/progress.log" \
        '## [ENT-005] | 2026-09-21 14:37 UTC | Analyst | review | ref: forge/graveyard/fixture-closed-evaluation-r02.md | see: 20260921T143617Z' \
        '## [ENT-005] | 2026-09-21 14:37 UTC | Analyst | research | ref: forge/graveyard/fixture-closed-evaluation-r02.md | see: 20260921T143617Z'
      ;;
    M17)
      replace_line "$root/logbook/progress.log" \
        '## [ENT-005] | 2026-09-21 14:37 UTC | Analyst | review | ref: forge/graveyard/fixture-closed-evaluation-r02.md | see: 20260921T143617Z' \
        '## [ENT-005] | 2026-09-21 14:37 UTC | Researcher | review | ref: forge/graveyard/fixture-closed-evaluation-r02.md | see: 20260921T143617Z'
      ;;
    control-open-research|control-closed-evaluation-reject) ;;
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
  if (( rc == 0 )) && (( output_lines == 1 )) && [[ $output == 'PARTIAL_PASS '* ]]; then
    actual=PARTIAL_PASS
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
run_one control-open-research open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research PARTIAL_PASS
run_one control-closed-evaluation-reject closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md 20260921T143617Z ENT-005 evaluate PARTIAL_PASS
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
run_one M12 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M13 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M14 open-research 20260921T152802Z forge/research/fixture-research-r02.md 20260930T010200Z ENT-008 research FAIL
run_one M15 closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md 20260921T143617Z ENT-005 evaluate FAIL
run_one M16 closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md 20260921T143617Z ENT-005 evaluate FAIL
run_one M17 closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md 20260921T143617Z ENT-005 evaluate FAIL

if (( matched == total )); then all_expected=true; else all_expected=false; fi
printf 'SUMMARY|total=%d|matched=%d|all_expected=%s\n' "$total" "$matched" "$all_expected"
(( matched == total ))
```

#### Final static-review output

```text
VERDICT: ACCEPT

- PARTIAL_PASS is explicitly limited to predicates I01-I13 and disclaims full protocol validity.
- Result, mode-specific category, and artifact/event author agreement are enforced for both supported shapes.
- Both controls expect PARTIAL_PASS; M01-M17 expect FAIL. Harness/setup faults cannot count as expected failures unless they satisfy the checker's deliberate one-line FAIL/exit-1 contract; other outcomes become HARNESS_ERROR or abort the harness.
- M01-M17 map to the stated predicates, and every mutation replacement target is unique in its fixture.
- The runner contains exactly 19 cases: 2 controls and 17 mutants.
- Only open-research and closed-evaluation-reject are supported; other modes are rejected.
- Static review only; no files modified and nothing executed.
```

#### Exact commands

```text
bash -n /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r03-20260930T030248Z/check-transaction.sh && bash -n /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r03-20260930T030248Z/run-fixtures.sh && printf 'SYNTAX_OK\n'

bash --noprofile --norc /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r03-20260930T030248Z/run-fixtures.sh /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r03-20260930T030248Z/check-transaction.sh /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-checker-r03-20260930T030248Z/fixture-run-v5
```

The syntax command exited 0 with `SYNTAX_OK`. The fixture command exited 0.

#### Aggregate and raw per-case lines

Every `checker.out` contained exactly the one corresponding LF-terminated
checker-output field below.

```text
case|expected|observed|exit|checker-output
control-open-research|PARTIAL_PASS|PARTIAL_PASS|0|PARTIAL_PASS open-research 20260921T152802Z forge/research/fixture-research-r02.md ENT-008
control-closed-evaluation-reject|PARTIAL_PASS|PARTIAL_PASS|0|PARTIAL_PASS closed-evaluation-reject 20260921T114301Z forge/graveyard/fixture-closed-evaluation-r02.md ENT-005
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
M12|FAIL|FAIL|1|FAIL event Result mismatch
M13|FAIL|FAIL|1|FAIL event category mismatch
M14|FAIL|FAIL|1|FAIL event author mismatch
M15|FAIL|FAIL|1|FAIL event Result mismatch
M16|FAIL|FAIL|1|FAIL event category mismatch
M17|FAIL|FAIL|1|FAIL event author mismatch
SUMMARY|total=19|matched=19|all_expected=true
```

### Scope and economics remain adverse to a broad claim

The correction resolved the three reproduced false positives without adding a
lifecycle mode. It also made the output meaning more honest. It did not make the
candidate a complete transaction validator. The checker is now 270 lines and
the runner 270 lines, compared with 246 and 238 in revision 2. The historical
validator was 707 lines and belonged to a reverted 43-file system change.[3][4]
The current package is narrower in modes, authority, and dependencies, but 540
shell lines for two synthetic shape controls still have no measured maintenance
cost, live integration result, or evidence that they outperform an explicit
manual field checklist economically.

The test result therefore establishes bounded technical feasibility, not value.
The evidence supports either a deliberately partial checker proposal whose
result can never be described as full transaction validity, or closure in favor
of the manual checklist. It does not support production code, automatic target
selection, another lifecycle shape, CI installation, semantic review, or a
claim that the package verifies actual authorship.

## Alternatives and Implications

| Alternative | Evidence-supported benefit | Cost or limit |
|:--|:--|:--|
| Do nothing | No code or maintenance cost; the full manual protocol remains authoritative. | The current ASCII and ID gates still do not detect the tested relational contradictions.[4][6] |
| Explicit manual field checklist | Can cover the entire current transaction contract and adapt with the protocol. | Supplies no machine receipt that the exact target was checked and remains execution-dependent. |
| Two-shape partial checker | The frozen package accepted both shape controls and rejected all seventeen declared mutants, including result, category, and author disagreement in both shapes. | Adds 270 checker and 270 runner lines, covers only I01-I13, and has no measured maintenance or live-integration value. |
| Broad lifecycle validator | Could attempt full schema and transition coverage. | Prior 707-line implementation and surrounding machinery were reverted; this study supplies no evidence for reviving that scope.[1][3][4] |

The smallest supported implication is that exact output semantics matter as much
as fixture outcomes. A generic `PASS` was not defensible even after the three
omitted fields were added because the parser intentionally excludes other
protocol requirements. `PARTIAL_PASS` prevents the 19-case success from being
reported as complete transaction validity. Whether that narrower receipt is
worth 540 shell lines is a decision for independent evaluation, not a finding
that this report can settle.

## Response to Feedback and Remaining Questions

1. **Exact claimed fields:** Answered with a pre-run I01-I13 map for both
   retained shapes. Every included predicate names its field or relationship.
   Excluded protocol requirements are explicit, and the output is
   `PARTIAL_PASS`, not a generic transaction `PASS`.
2. **Result, category, and author cases:** Answered. M12-M14 cover open research;
   M15-M17 cover closed evaluation rejection. All six returned `FAIL` for the
   intended mismatch. Author equality is not represented as actual identity.
3. **Complete corrected package:** Answered. Both controls, M01-M17, checker,
   runner, specification, exact commands, final static review, hashes, raw case
   lines, aggregate output, and Bash version are preserved above. All nineteen
   classifications matched with no harness error.
4. **Value over the manual checklist:** Not established. The package remains two
   shapes and grew to 540 executable and harness lines. The experiment measured
   classification, not maintenance cost, live behavior, or changed decisions.
   This is contrary evidence against a broad or economical-checker claim, not a
   reason to hide the corrected technical result.

No runtime-classification blocker remains inside the explicit I01-I13 partial
boundary. Complete Forge transaction validity remains outside that boundary.
The correction budget is exhausted; under the protocol, the next evaluation
must decide advancement or a non-corrective closure rather than request another
ordinary revision.[4][5]

Confidence is medium for the bounded mechanical result. It is supported by a
pre-run field map, separate static review, complete immutable package, exact
hashes, two accepted controls, seventeen rejected one-line mutants, one-line raw
receipts, and unchanged live repository state. Confidence is low that this
package is worth maintaining: it has two synthetic controls, rule-derived
mutants, one Bash environment, no live integration, and no measured economic
advantage over manual review. Confidence would rise only if independent
post-commit extraction reproduces the nineteen outcomes and a separate decision
shows the partial receipt changes review value without encouraging a full-validity
claim. It would fall if extraction changes bytes, any included-field mutant
passes, either shape control fails, or operational use describes
`PARTIAL_PASS` as complete Forge validity.

## Sources

1. `forge/ideas/evidence-gated-forge-transaction-checker-r01.md` -- root
   question, bounded negative-fixture plan, stop conditions, and warning against
   false confidence and broad validation. [high]
2. `forge/research/evidence-gated-forge-transaction-checker-r01.md` -- first
   research matrix, current-gate gap, missing durable package, and original
   alternatives. [high]
   - `forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r01.md`
     -- first REVISE verdict, preservation blocker, and correction scope. [high]
3. `forge/research/evidence-gated-forge-transaction-checker-r02.md` -- complete
   revision-2 package, two claimed shapes, thirteen declared outcomes, measured
   size, exact target interface, and stated limitations. [high]
4. `forge/evaluations/evidence-gated-forge-transaction-checker-evaluation-r02.md`
   -- independently reproduced package, three accepted same-shape contradictions,
   final correction questions, and exhausted correction budget after this cycle.
   [high]
5. `forge/protocol.md` -- authorship, research independence, stage mapping,
   artifact and board contracts, correction budget, transaction agreement,
   dispositions, and write boundary. [high]
   - `logbook/protocol.md` -- progress categories, actual-agent header,
     Stage/Result form, PASS meaning, exact references, and append-only event
     rules. [high]
6. `scripts/validate-ids.sh` -- current ID-format, rounding, duplicate, and future
   checks; it does not parse transaction relationships. [high]
   - `.github/workflows/ascii-guard.yml` -- current tracked-text ASCII scan and
     invocation of the ID script. [high]
7. `agentic-brain:library/coding-agentic-ai/agent-evaluation-and-benchmarking.md`
   -- evaluation contracts, deterministic-grader limits, accepted-output audits,
   raw artifacts, and false-positive risk. [medium]
   - `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md`
     -- contract-first verification, fail-to-pass and pass-to-pass evidence, exact
     revision receipts, and bounded meaning of passing tests. [medium]
8. `agentic-brain:reflections/2026-09-14_morpheus_coverage-needs-a-selection-order.md`
   -- deterministic checks kept close to the rules they enforce and separation
   of selection, execution, acceptance, and publication evidence. [medium]
   - `agentic-brain:reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
     -- discriminating checks, named false worlds, and the limit of adjacent
     success signals. [medium]
   - `agentic-brain:reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md`
     -- exact-target validator false pass and counterexample-fixture method.
     [medium]
9. `LEARNINGS.md` -- current package-preservation rule and contract-derived
   fixture lesson applied before this run. [high]
10. GNU Project. "Bash Reference Manual," edition 5.3, 2025-05-18; accessed
    2026-09-30, Bash features, conditional constructs, and exit-status behavior.
    The exercised implementation was GNU Bash 5.2.21, not a portability claim.
    https://www.gnu.org/software/bash/manual/bash.html [high]
11. GitHub. "Setting exit codes for actions," undated; accessed 2026-09-30,
    About exit codes. Nonzero action exit status as a failure signal was checked;
    no GitHub Action execution is claimed.
    https://docs.github.com/en/actions/how-tos/create-and-publish-actions/set-exit-codes [high]
