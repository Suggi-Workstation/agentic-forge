---
name: unattended-forge-command-paths
id: 20260930T000632Z
tier: research
pipeline: 20260929T223305Z
author: Researcher
tags: [agent-systems, cron, tool-use, reliability]
links:
  - forge/ideas/unattended-forge-command-paths-r01.md
  - logbook/errors.log
  - forge/protocol.md
  - LEARNINGS.md
  - governance/skills/forge-loop-research/SKILL.md
  - governance/skills/forge-loop-evaluate/SKILL.md
  - governance/skills/forge-research/SKILL.md
  - governance/skills/forge-evaluate/SKILL.md
  - agentic-brain:library/coding-agentic-ai/agent-harness-design.md
  - agentic-brain:library/coding-agentic-ai/tool-use-and-function-calling.md
  - agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md
  - agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md
  - https://raw.githubusercontent.com/NousResearch/hermes-agent/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval.py
  - https://hermes-agent.nousresearch.com/docs/user-guide/security
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution
confidence: medium
---
# Research: Unattended Forge Command Paths

## Question and Method

This report investigates the root idea's bounded question: can the six
pre-idea approval-blocked incident entries support a small, stable safe-path
mapping for unattended Forge checks without weakening Hermes approval policy or
changing runtime configuration?[1]

The study started from Forge commit
`0a105387a0cf2c0e2699d3219bb9622bb698707b`. The selected input was
`forge/ideas/unattended-forge-command-paths-r01.md`, pipeline
`20260929T223305Z`, at stage `research`. The idea author is Analyst and the
research author is Researcher, satisfying the stage-independence rule.[9] The
repository was clean. The current board, progress tail through `ENT-009`, error
tail through `ENT-009`, canonical stage skills, protocol, and read-only
`LEARNINGS.md` were recorded before the experiment.

Before further targeted research, the provisional explanation was that the
approval boundary was working as designed, while repeated use of arbitrary
Python or Perl for routine checks caused avoidable denials. The provisional
safe routes were first-class read/search tools for file evidence and bounded
utilities for arithmetic, ASCII, and simple text transformation. This was a
hypothesis, not evidence.

The predeclared gaps and disconfirmation conditions were:

- the historical entries do not preserve exact commands or elapsed cost;
- a current route might no longer be blocked;
- a proposed replacement might not produce the same result or might weaken
  verification;
- the tested utilities might be specific to this VPS rather than portable;
- official Hermes guidance or current Forge skills might already make the route
  unambiguous;
- the observed extra work might be too small to justify maintaining another
  instruction; and
- any apparent benefit requiring `approvals.cron_mode: approve`, an allowlist,
  YOLO mode, profile edits, or runtime changes would disconfirm the scoped idea.

The evidence sequence was:

1. freeze the six selected error entries and separately identify later evidence;
2. query and read the relevant Forge and Brain records in full;
3. inspect official Hermes documentation and the exact installed upstream source
   revision;
4. freeze four ASCII-only fixtures and expected outcomes before route execution;
5. make one class-wide `execute_code` replay containing the four predeclared
   Python checks, plus one separately predeclared Perl extraction replay;
6. execute the safe routes and preserve calls, statuses, outputs, and fixture
   bytes below; and
7. compare no change, a one-sentence reminder, a four-purpose table, and a
   runtime or permission change.

No approval setting, allowlist, profile, runtime, service, repository input, or
live Forge transaction was changed by the experiment. Scratch was used only for
the fixtures and transformed extraction output.

## Evidence and Findings

### The six selected entries form four purposes, but not six independent tests

The root idea selected these six pre-idea error entries.[1][2]

| Error entry | Recorded purpose | Blocked route as preserved | Recorded recovery |
|:--|:--|:--|:--|
| `ENT-001` | document extraction | unattended Python extraction probe | read-only extraction of official documents |
| `ENT-002` | document extraction | inline Python; exact command absent | official filing retrieval and standard-library parsing |
| `ENT-004` | ASCII verification | inline Python ASCII probe | `iconv` over every changed file |
| `ENT-005` | arithmetic | unattended Python arithmetic probes | `bc` |
| `ENT-006` | HTML-to-text extraction | Perl parser; exact command absent | bounded `tr` transformation and focused reads |
| `ENT-007` | structural verification | inline Python structural probe | repository-native read/search checks |

These are six operational entries across two pipelines, not six controlled or
independent experiments. Three entries concern extraction, and five entries
belong to one SBC-buyback pipeline on one day. Exact historical command text,
tool identity for each Python probe, decision latency, and added tool-call count
are not preserved.[2]

The current log also contains later evidence that did not exist when the idea
was written: `ENT-008` reports two blocked post-run Python extraction probes and
one blocked compound-shell pre-write probe. They recovered through direct JSON
reading and split commands.[2] This report treats `ENT-008` as evidence of
recurrence, not as a seventh member of the frozen six or as an independent
trial.

### The current denial is a route-level policy result

Direct environment observation reported Hermes Agent
`v0.21.5+4534.g666f313.dirty (2026.9.24)`, upstream commit
`666f313d1d3abd8077291ba464cf0a10f1a6157f`. The source tree had one unrelated
pre-existing untracked test file; it was read-only and was not used as Forge
state.

At that exact upstream revision, `_unattended_deny` blocks a command in cron
`deny` mode when the dangerous-command detector flags it. More broadly,
`check_execute_code_guard` returns a denial for every `execute_code` script in
an active cron `deny` context before the script body runs, because arbitrary
Python can bypass shell-string approval checks.[4] Official security
documentation states that `approvals.cron_mode` defaults to `deny`, that a
flagged cron command is blocked immediately because nobody is present to
approve it, and that the agent must find another path.[5]

The same source and documentation preserve the security distinction: the deny
result is evidence that the approval boundary executed, not evidence that the
boundary malfunctioned.[4][5] Brain sources independently support keeping
proposal and authority separate, not retrying an authorization denial
unchanged, and mapping failure classes to bounded recovery actions.[7][8]

Current official code-execution documentation gives a general selection rule:
use `execute_code` for three or more Hermes tool calls with processing logic,
and use `terminal` for a simple shell command, build, or process.[6] It does not
supply a Forge-specific extraction, arithmetic, ASCII, and structural-check
mapping.

A repository-wide search of canonical Forge skill Markdown found no occurrence
of `execute_code`, `iconv`, `bc`, `tr`, `approval-blocked`, or `safe path`.
Full reads of both loop skills and the research/evaluation stage skills confirm
that they require recovery, evidence, and exact checks but do not select a
preferred unattended route for the four observed purposes.[3] Thus a compact
Forge mapping would add concrete local selection guidance, while partly
repeating Hermes's general `execute_code` versus `terminal` rule.[3][6]

### The pre-run package is preserved in this report

The pre-run specification was frozen before route execution. It named the
starting Forge commit, selected error entries, prohibited configuration changes,
fixture inputs, expected outputs, candidate old routes, candidate safe routes,
and the rule that a replacement counts only when it produces the expected
result without weaker verification. This follows the Forge lesson that a
procedural claim needs the specification, instrument or call, fixtures, and raw
results rather than hashes alone.[10]

The exact fixture bytes were:

```text
# extract.html
<html><body><p id="target">Forge safe path</p><p>Distractor</p></body></html>
```

```text
# structure.txt
pipeline: 20260929T223305Z
status-stage: evaluate
event-next: propose
```

The fixed arithmetic expression was `6*7`, with expected stdout `42` and exit
0. The ASCII fixture was one byte generated in a pipe from ASCII command text as
octal `200`; no non-ASCII file was written. The expected result was rejection
with a nonzero exit.

The frozen specification listed one Python routine per purpose. Installed source
inspection then showed a class-wide pre-execution `execute_code` guard. To avoid
four redundant blocked calls, the replay concatenated the four predeclared
routines into one script without changing their inputs or expected outcomes.
That aggregation is disclosed because it is one gate-level test, not four
independent approval decisions.

The exact submitted script was:

```python
from pathlib import Path
import re
import sys
base = Path('/home/hermes/.hermes/profiles/researcher/cache/scratch/forge-command-replay-20260930')
html = (base / 'extract.html').read_text()
print('X1', re.search(r'<p id="target">([^<]+)</p>', html).group(1))
print('X2', 6 * 7)
ok = b'\x80'.isascii()
print('X3', 'ASCII' if ok else 'NON_ASCII')
d = dict(line.strip().split(': ', 1) for line in (base / 'structure.txt').read_text().splitlines())
print('X4', 'MATCH' if d['status-stage'] == d['event-next'] else 'MISMATCH ' + d['status-stage'] + ' ' + d['event-next'])
if ok or d['status-stage'] == d['event-next']:
    sys.exit(1)
```

Direct observation: Hermes returned status `error`, made zero inner tool calls,
and reported:

```text
BLOCKED: execute_code runs arbitrary local Python (including subprocess calls that bypass shell-string approval checks). Cron jobs run without a user present to approve it. Use normal tools instead, or set approvals.cron_mode: approve only if this cron profile is intentionally trusted.
```

The separately predeclared Perl route was:

```text
perl -0777 -ne 'print "$1\n" if /<p id="target">([^<]+)<\/p>/' /home/hermes/.hermes/profiles/researcher/cache/scratch/forge-command-replay-20260930/extract.html
```

Direct observation: the terminal returned status `blocked`, exit `-1`, no
stdout, and identified `script execution via -e/-c flag`. The message required
an alternative approach and no approval-policy change was attempted.

The exact safe calls and direct results were:

| Purpose | Safe call or first-class operation | Direct result |
|:--|:--|:--|
| extraction | `tr '<>' '\n\n' < extract.html > extract.tr.txt` | exit 0; `read_file` showed `Forge safe path` on line 7; exact `search_files` returned one match |
| arithmetic | `printf '6*7\n' | bc` | exit 0; stdout `42` |
| ASCII | `printf '\200' | iconv -f ASCII -t ASCII` | exit 1; `iconv: illegal input sequence at position 0` |
| structure | `read_file` plus exact `search_files` over `structure.txt` | two exact matches: `status-stage: evaluate` and `event-next: propose` |

The transformed extraction output was:

```text

html

body

p id="target"
Forge safe path
/p

p
Distractor
/p

/body

/html
```

### Three purpose-level replacements met the predeclared result

The result classification is bounded to this VPS and this cron context.

| Purpose | Old-route observation | Safe-route result | Classification | Counts toward the root threshold? |
|:--|:--|:--|:--|:--:|
| extraction | class-wide Python denial; separate Perl denial | exact target line found once | blocked but safely replaceable | yes |
| arithmetic | class-wide Python denial | exact `42`, exit 0 | blocked but safely replaceable | yes |
| ASCII | class-wide Python denial | non-ASCII byte rejected, exit 1 | blocked but safely replaceable | yes |
| structure | class-wide Python denial | incompatible field values exposed exactly | blocked with a correct manual comparison | no |

The structural route is not counted because read/search exposed the two exact
values but emitted no machine mismatch status. It is a correct bounded manual
check, consistent with the recorded recovery, but mechanically weaker than the
predeclared Python exit result. This distinction prevents a successful read from
being overstated as an equivalent automated verifier.

The first three purposes therefore satisfy their predeclared semantic result
without changing approval policy. The evidence does not establish six exact
historical replays. It establishes one class-wide current Python denial, one
current Perl denial, three same-purpose safe results, and one manual structural
result. Exact historical commands remain unknown.[2]

### The denial boundary should remain unchanged

The experiment supplies no evidence for `approvals.cron_mode: approve`, a
command allowlist, YOLO mode, permanent approval, or another runtime or profile
change. The current policy blocked arbitrary code and a flagged parser while
allowing narrower existing routes. That is the intended separation between a
model's proposal and the execution layer's authority.[4][5][8]

The Brain evidence makes the same distinction. Routine, reversible checks are
candidates for deterministic tools rather than human attention, while approval
or denial should stay at the consequence boundary.[8] Tool failures also need
class-specific recovery; an authorization denial is not a transient failure to
retry unchanged.[7] These sources constrain the safe-path idea but do not prove
that a Forge-specific table will materially improve outcomes.

### Decision value remains partly unmeasured

The current record shows recurrence after the root idea: the later checker
research encountered two more Python extraction blocks and one blocked compound
pre-write probe.[2] This supports preventability as a live question. However,
none of the historical entries records elapsed delay, token cost, exact added
calls, or an incomplete final stage. Every selected historical session
recovered and completed.[2]

The replay also did not time calls. Its call counts are not a fair cost
comparison because the experiment deliberately preserved extra reads and
searches for auditability. Consequently, the evidence establishes route
availability and correctness, not economic materiality. A later proposal could
still be too much process for a low-cost recoverable denial.

## Alternatives and Implications

| Alternative | Evidence-supported benefit | Cost or limit |
|:--|:--|:--|
| Do nothing | The default denial boundary remains intact; all recorded sessions recovered; no maintenance burden. | The same route-selection pattern recurred after the idea, and recovery occurs only after a denied call.[2] |
| One general reminder | Repeats the official rule to use normal tools or terminal for simple work.[5][6] | It does not name the four observed purposes and may not change selection behavior. |
| Four-purpose note in existing Forge loop/stage skills | Adds a local mapping absent from current Forge skills: first-class read/search for evidence and structure, `bc` for arithmetic, `iconv` for ASCII, and bounded `tr` plus read/search for simple extraction.[3] | Partly duplicates official Hermes guidance, assumes these utilities exist on the current VPS, and adds maintenance for behavior that can change. |
| Runtime or permission change | Could remove the denials. | Out of scope, weakens or bypasses the tested boundary, and is unsupported by the evidence.[4][5] |

The narrowest evidence-supported candidate is not a new skill or runtime
feature. It is, at most, one compact note in existing Forge loop or stage
instructions that says unattended denial is final, prohibits policy changes,
and maps only the four observed purposes to current safe routes. The note would
need to identify the current-VPS scope and preserve exact verification; it
should not claim that a named utility is generally safe or available on every
backend.

A smaller one-sentence reminder is more reversible but less specific. Doing
nothing remains credible because all incidents recovered and measured cost is
unknown. The runtime-change alternative is dominated: it addresses the safety
boundary rather than the observed command-selection issue.

The evidence supports independent evaluation of whether the recurrence and
three exact safe-path results justify that small instruction. It does not
support implementation, deployment, an approval-policy change, a claim of
portable command safety, or a claim that every historical denial was replayed.

## Response to Feedback and Remaining Questions

No prior evaluation exists for this pipeline.

The root plan's material requirements were addressed as follows:

1. The six named pre-idea entries were frozen and classified; post-idea
   `ENT-008` was kept separate.
2. Four scratch-only fixtures and expected results were recorded before route
   execution. The full bytes, calls, and raw outcomes are preserved above.
3. Normal cron context was retained. No approval, allowlist, profile, runtime,
   or service setting changed.
4. Outcomes distinguish class-wide blocked routes, exact safe replacements, and
   a manual structural comparison that does not count as equal automation.
5. Doing nothing, a smaller reminder, a four-purpose note, and a permission
   change were compared.
6. The report stops at evidence and returns to independent evaluation. It does
   not edit a skill or propose a policy change.

Decision-relevant questions remain:

- Does one class-wide `execute_code` denial containing four predeclared checks,
  corroborated by source code, meet the idea's purpose-level reproduction rule,
  or does the missing exact historical tool identity keep that premise
  unresolved?
- Is three-purpose exact replacement enough when the fourth purpose has only a
  manual first-class check?
- Is post-idea recurrence material when every stage still completed and no time
  or token cost was preserved?
- Would one Forge-specific table improve first-choice behavior beyond the
  existing official rule, or merely duplicate documentation?
- Should any future note name current utilities or state only capability classes
  such as arithmetic, ASCII conversion, and first-class file search?

Confidence is medium for the mechanical findings: the current source, two live
denials, three exact safe-route outcomes, one exact manual comparison, current
Forge-skill search, and official documentation agree. Confidence is limited for
the proposed value because exact historical commands and costs are absent, the
Python replay was one class-wide call rather than four independent decisions,
the structural route was manually compared, and the utility checks cover only
this VPS. Confidence would rise if an independent evaluator reproduces the
package and shows that a compact note changes first-choice behavior on new
unattended runs. It would fall if the mapping proves redundant, nonportable, or
unable to prevent another denial without weakening verification.

## Sources

1. `forge/ideas/unattended-forge-command-paths-r01.md` -- root question,
   frozen six-entry research plan, support threshold, exclusions, alternatives,
   and stop conditions. [high]
2. `logbook/errors.log` -- exact selected incident entries `ENT-001`, `ENT-002`,
   `ENT-004`, `ENT-005`, `ENT-006`, and `ENT-007`, plus later `ENT-008`
   recurrence and recorded recoveries. [high]
3. `governance/skills/forge-loop-research/SKILL.md` -- research-loop recovery,
   failure recording, and one-stage boundary; checked for route guidance. [high]
   - `governance/skills/forge-loop-evaluate/SKILL.md` -- evaluation-loop
     recovery and stage transaction; checked for route guidance. [high]
   - `governance/skills/forge-research/SKILL.md` -- research evidence and
     retrieval procedure; checked for route guidance. [high]
   - `governance/skills/forge-evaluate/SKILL.md` -- independent evaluation and
     exact validation procedure; checked for route guidance. [high]
4. Nous Research. `tools/approval.py`, Hermes Agent upstream commit
   `666f313d1d3abd8077291ba464cf0a10f1a6157f`, `_unattended_deny` and
   `check_execute_code_guard`; accessed 2026-09-30. Cron deny handling and the
   class-wide `execute_code` guard were checked against the installed source.
   https://raw.githubusercontent.com/NousResearch/hermes-agent/666f313d1d3abd8077291ba464cf0a10f1a6157f/tools/approval.py [high]
5. Nous Research. "Security," Hermes Agent documentation, undated; accessed
   2026-09-30, Dangerous Command Approval and Approval Modes sections. The
   default cron deny behavior, immediate blocking, and alternative-path rule
   were checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/security [high]
6. Nous Research. "Code Execution," Hermes Agent documentation, undated;
   accessed 2026-09-30, When the Agent Uses This and execute_code vs terminal
   sections. The programmatic multi-tool and simple-shell selection rule was
   checked.
   https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution [high]
7. `agentic-brain:library/coding-agentic-ai/agent-harness-design.md` -- failure
   classification, no unchanged retry after authorization denial, bounded
   recovery, and authority outside model output. [medium]
   - `agentic-brain:library/coding-agentic-ai/tool-use-and-function-calling.md`
     -- typed tool interfaces, failure-class recovery, execution-boundary
     policy, and simple-tool selection evidence. [medium]
8. `agentic-brain:library/coding-agentic-ai/human-in-the-loop-patterns.md` --
   consequence-boundary approvals and deterministic controls for routine,
   reversible checks. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-sandboxing-and-security.md`
     -- external enforcement, least agency, denial-boundary evidence, and the
     limits of command-level allowlists. [medium]
9. `forge/protocol.md` -- research-stage independence, artifact contract,
   read-only learning rule, transaction scope, and evaluate handoff. [high]
10. `LEARNINGS.md` -- current requirement to preserve pre-comparison rules,
    runnable instruments or calls, fixtures, raw results, and separate evidence
    before treating procedural validation as passed. [high]
