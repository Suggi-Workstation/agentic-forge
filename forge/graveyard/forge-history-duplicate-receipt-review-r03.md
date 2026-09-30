---
name: forge-history-duplicate-receipt-review
id: 20260930T183748Z
tier: final-review
pipeline: 20260930T124036Z
author: Analyst
tags: [agent-systems, forge, retrieval, final-review]
links:
  - forge/proposals/forge-history-duplicate-receipt-r03.md
  - forge/ideas/forge-history-duplicate-receipt-r01.md
  - forge/research/forge-history-duplicate-receipt-r01.md
  - forge/evaluations/forge-history-duplicate-receipt-evaluation-r01.md
  - forge/proposals/forge-history-duplicate-receipt-r01.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r01.md
  - forge/proposals/forge-history-duplicate-receipt-r02.md
  - forge/final-reviews/forge-history-duplicate-receipt-review-r02.md
  - governance/skills/forge-ideate/SKILL.md
  - forge/protocol.md
  - STATUS.md
  - LEARNINGS.md
  - logbook/progress.log
  - logbook/errors.log
  - agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md
  - agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md
  - agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md
  - agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md
  - https://git-scm.com/docs/git-config
  - https://git-scm.com/docs/partial-clone
  - https://git-scm.com/docs/git-cat-file.html
  - https://docs.python.org/3.14/library/resource.html
  - https://docs.python.org/3.14/library/subprocess.html
  - https://docs.python.org/3.14/library/time.html
confidence: high
---
# Final Review: Bounded Reachable-History Receipt R03

## Target and Baseline

Target: `forge/proposals/forge-history-duplicate-receipt-r03.md`, ID
`20260930T180714Z`.[1]

The target author is Researcher. This review was performed by Analyst in a
separate scheduled context that did not inherit the proposal drafting session's
private reasoning. Target-author independence therefore passes.[1][3]

At starting HEAD `db1670f0faf5a3ab3a9c5b773fc10c431607fe79`, the worktree was
clean. The board contained three valid rows: an unselected human-review row for
pipeline `20260930T083956Z`, the selected final-review row for pipeline
`20260930T124036Z`, and an unselected research row for pipeline
`20260930T173859Z`. The selected row named the exact target above.
`progress.log` ended at ENT-017 and `errors.log` ended at ENT-023. Two prior
final-review REVISE verdicts used corrective cycles 1 and 2 of 2; no REFRAME or
human budget extension exists for this pipeline.[2][3]

Before reading the target body, the expected evidence and failure conditions
were recorded in task-owned evaluator scratch. Expected evidence was:

- the same one-skill, scratch-only, separately authorized scope, with current
  retrieval first, exact historical bodies before decisions, truthful unknown
  states, direct rollback, and no implementation authority;
- an operating-system sink boundary that never accepts more body bytes than the
  remaining allowance, including exact-fit, plus-one, mismatch, partial-output,
  and timeout cases;
- one absolute deadline before and after every child command and every
  decision-relevant in-process transition, with no display, classification,
  disposition, or publication after expiry;
- an independently owned fixture ledger and structural bypass check covering
  every oracle-relevant child and in-process operation;
- rejection of every effective shallow, partial, and promisor state before any
  history or object command, with zero network, fetch child, or Git-state write;
  and
- an executable acceptance package covering the exact contracts while leaving
  unexecuted implementation work labeled future.[2][4][6]

Failure conditions were a sink that could exceed the byte ceiling; a late
operation or disposition; an observer that could not expose an omitted call; an
effective promisor configuration that bypassed the clone guard; any lazy fetch,
network access, or object-database write; scope drift; or an unsupported
completion claim. Because the ordinary correction budget was already exhausted,
any remaining blocker required DEFER rather than another REVISE or REFRAME.[3]

## Findings

### R03 substantially answers the four requested design corrections

R03 moves actual body output to a new regular-file sink and sets the body
child's `RLIMIT_FSIZE` before `exec`; retains information-only object preflight;
applies one immutable deadline around commands and typed in-process operations;
adds a harness-owned fixture ledger plus an AST bypass check; and adds an early
shallow/partial/promisor guard. It preserves the evaluated one-skill scope,
current retrieval, exact provenance, full-body decision gate, unknown state,
finite limits, rollback, and separate-authorization boundary.[1][2]

The material interface claims check independently:

- Python defines `RLIMIT_FSIZE` as the maximum file size a process may create
  and exposes `setrlimit()` for soft and hard limits.[10]
- Python warns that `preexec_fn` can deadlock in the presence of threads. R03
  narrows its design to one standalone POSIX process with exactly one live
  Python thread before the body path. Python also documents kill-and-wait
  behavior for `run()` timeout and the process-creation timing limitation that
  R03 retains.[11]
- `monotonic_ns()` uses a clock that cannot go backward and is not affected by
  system-clock updates.[11]
- Git separates `cat-file --batch-check` information from raw body output. On
  the current Git 2.43.0, a NUL-input/NUL-output `-Z --batch-check` probe
  returned the expected OID, `blob`, and 1,103-byte size for `HEAD:STATUS.md`.
  The same Git rejected the newer global `--no-lazy-fetch` option, matching the
  proposal's reason for choosing rejection rather than that switch.[9]

An evaluator-written Git-body sink probe used exact script SHA-256
`b77872f2e2d66434e824f9ad83b383ebaf17c51368dfcdb9be0d8369080fb318`.
For the 1,103-byte `HEAD:STATUS.md` blob, a 1,103-byte child limit exited 0 and
left a 1,103-byte sink; a 1,102-byte limit returned signal 25 and left a
1,102-byte sink. This supports the selected sink primitive on the current host.
It does not validate the future driver, every target filesystem, the ledger, or
the complete acceptance matrix.[1][10][11]

R03 also labels the complete driver, Git sink package, promisor fixture,
external-ledger matrix, root-first display, and final skill bytes as unexecuted
future work. Their absence is not misrepresented as a pass.[1] No blocker was
found in the corrected sink, deadline, external-ledger, rollback, authority, or
scope contracts as written.

### The local-only clone guard omits effective Git configuration scopes

This is blocking. Normative Step 5 says to read only local repository config and
reject local `extensions.partialClone`, `remote.*.promisor`, and
`remote.*.partialCloneFilter` keys. Its matrix tests those key names but does
not test system, global, worktree, or command-scope injection, nor does the
normative child wrapper sanitize those sources.[1]

Git defines five effective configuration scopes: system, global, local,
worktree, and command. Command scope includes `GIT_CONFIG_COUNT`,
`GIT_CONFIG_KEY_<n>`, and `GIT_CONFIG_VALUE_<n>` environment variables as well
as `-c`. A local-only query can therefore return no promisor key while the next
Git child sees one from another effective scope.[7]

Git's partial-clone documentation states that missing objects can be demand
fetched, that the fetch is performed by a `git fetch` subprocess, and that
promisor remotes are configured through `extensions.partialClone` and
`remote.<name>.promisor` plus related filter configuration. Partial clone is
independent of shallow clone.[8]

A disposable Git 2.43.0 fixture reproduced the exact bypass without touching the
Forge clone or contacting an external network:

1. A local `file://` source served a `--filter=blob:none --no-checkout` clone.
   The payload blob initially appeared as missing: `?4dad7cc480d2187958499557dd24242465dbec6d`.
2. The fixture removed every local partial/promisor key.
3. It supplied `remote.origin.promisor=true` only through
   `GIT_CONFIG_COUNT=1`, `GIT_CONFIG_KEY_0`, and `GIT_CONFIG_VALUE_0` to both
   the guard and object child.
4. The proposed local-only key query returned exit 1 and empty stdout. The
   effective all-scope query returned exit 0 and
   `remote.origin.promisor`, `true`.
5. `git cat-file blob 4dad7cc480d2187958499557dd24242465dbec6d`
   returned exit 0 and the payload `promisor-scope-probe`.
6. Git Trace2 recorded a child invocation of `git fetch origin` and a promisor
   `fetch_count` of 1. Four object-database files were added: one `.pack`, one
   `.idx`, one `.rev`, and one `.promisor` file.

The exact evaluator fixture had SHA-256
`5e33e13295c8f27657f68504b54a320f1fe1b3643daaaf4ad698628cee03db39`.
The bytes inside this code fence, excluding the fence, are that complete
fixture:

```python
#!/usr/bin/env python3
import json
import os
import subprocess
import tempfile
from pathlib import Path

SCRATCH = Path('/home/hermes/.hermes/profiles/analyst/cache/scratch')
BASE = Path(tempfile.mkdtemp(prefix='forge-r03-promisor-', dir=SCRATCH))
SRC = BASE / 'source'
CLONE = BASE / 'partial'
TRACE = BASE / 'trace2.json'


def run(args, cwd=None, env=None, check=True):
    completed = subprocess.run(
        args,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and completed.returncode != 0:
        raise RuntimeError({
            'args': args,
            'returncode': completed.returncode,
            'stdout': completed.stdout.decode('utf-8', 'replace'),
            'stderr': completed.stderr.decode('utf-8', 'replace'),
        })
    return completed


run(['git', 'init', '-q', str(SRC)])
run(['git', 'config', 'user.name', 'Probe'], cwd=SRC)
run(['git', 'config', 'user.email', 'probe@example.invalid'], cwd=SRC)
(SRC / 'payload.txt').write_text('promisor-scope-probe\n', encoding='ascii')
run(['git', 'add', 'payload.txt'], cwd=SRC)
run(['git', 'commit', '-q', '-m', 'fixture'], cwd=SRC)
run(['git', 'config', 'uploadpack.allowFilter', 'true'], cwd=SRC)
run(['git', 'config', 'uploadpack.allowAnySHA1InWant', 'true'], cwd=SRC)
blob = run(['git', 'rev-parse', 'HEAD:payload.txt'], cwd=SRC).stdout.decode().strip()
run([
    'git', 'clone', '-q', '--filter=blob:none', '--no-checkout',
    'file://' + str(SRC), str(CLONE),
])
missing_initial = run(
    ['git', 'rev-list', '--objects', '--missing=print', 'HEAD'], cwd=CLONE
).stdout.decode('utf-8', 'replace').splitlines()

for key in (
    'extensions.partialClone',
    'remote.origin.promisor',
    'remote.origin.partialCloneFilter',
):
    run(['git', 'config', '--local', '--unset-all', key], cwd=CLONE, check=False)

objects_before = sorted(
    str(path.relative_to(CLONE / '.git' / 'objects'))
    for path in (CLONE / '.git' / 'objects').rglob('*')
    if path.is_file()
)

env = os.environ.copy()
env.update({
    'GIT_CONFIG_COUNT': '1',
    'GIT_CONFIG_KEY_0': 'remote.origin.promisor',
    'GIT_CONFIG_VALUE_0': 'true',
    'GIT_TRACE2_EVENT': str(TRACE),
})
pattern = r'^(extensions\.partialClone|remote\..*\.(promisor|partialCloneFilter))$'
local_guard = run(
    ['git', 'config', '--local', '--null', '--get-regexp', pattern],
    cwd=CLONE,
    env=env,
    check=False,
)
all_scope = run(
    ['git', 'config', '--null', '--get-regexp', pattern],
    cwd=CLONE,
    env=env,
    check=False,
)
body = run(['git', 'cat-file', 'blob', blob], cwd=CLONE, env=env, check=False)
objects_after = sorted(
    str(path.relative_to(CLONE / '.git' / 'objects'))
    for path in (CLONE / '.git' / 'objects').rglob('*')
    if path.is_file()
)
missing_after = run(
    ['git', 'rev-list', '--objects', '--missing=print', 'HEAD'], cwd=CLONE
).stdout.decode('utf-8', 'replace').splitlines()
trace_text = TRACE.read_text(encoding='utf-8', errors='replace') if TRACE.exists() else ''

result = {
    'base': str(BASE),
    'blob': blob,
    'missing_initial': missing_initial,
    'local_guard_returncode': local_guard.returncode,
    'local_guard_stdout_repr': repr(local_guard.stdout),
    'all_scope_returncode': all_scope.returncode,
    'all_scope_stdout_repr': repr(all_scope.stdout),
    'cat_file_returncode': body.returncode,
    'cat_file_stdout': body.stdout.decode('utf-8', 'replace'),
    'cat_file_stderr': body.stderr.decode('utf-8', 'replace'),
    'objects_added': sorted(set(objects_after) - set(objects_before)),
    'missing_after': missing_after,
    'trace_mentions_fetch': 'fetch' in trace_text,
    'trace_mentions_promisor': 'promisor' in trace_text,
}
print(json.dumps(result, indent=2, sort_keys=True))
```

Its raw stdout was:

```json
{
  "all_scope_returncode": 0,
  "all_scope_stdout_repr": "b'remote.origin.promisor\\ntrue\\x00'",
  "base": "/home/hermes/.hermes/profiles/analyst/cache/scratch/forge-r03-promisor-y_bg58ft",
  "blob": "4dad7cc480d2187958499557dd24242465dbec6d",
  "cat_file_returncode": 0,
  "cat_file_stderr": "",
  "cat_file_stdout": "promisor-scope-probe\n",
  "local_guard_returncode": 1,
  "local_guard_stdout_repr": "b''",
  "missing_after": [
    "963437e2dc8f02eff3eb34862934891576512a32",
    "c18722133b15ba437cb5341a847b913a7a20feea ",
    "4dad7cc480d2187958499557dd24242465dbec6d payload.txt"
  ],
  "missing_initial": [
    "963437e2dc8f02eff3eb34862934891576512a32",
    "c18722133b15ba437cb5341a847b913a7a20feea ",
    "?4dad7cc480d2187958499557dd24242465dbec6d"
  ],
  "objects_added": [
    "pack/pack-cc113cb5060655d605c3309071d92fca95d712fa.idx",
    "pack/pack-cc113cb5060655d605c3309071d92fca95d712fa.pack",
    "pack/pack-cc113cb5060655d605c3309071d92fca95d712fa.promisor",
    "pack/pack-cc113cb5060655d605c3309071d92fca95d712fa.rev"
  ],
  "trace_mentions_fetch": true,
  "trace_mentions_promisor": true
}
```

The two decisive raw Trace2 events were:

```json
{"event":"child_start","sid":"20260930T183605.206732Z-H274f8de2-P001dd1d6","thread":"main","time":"2026-09-30T18:36:05.207247Z","file":"run-command.c","line":726,"child_id":0,"child_class":"?","use_shell":false,"argv":["git","-c","fetch.negotiationAlgorithm=noop","fetch","origin","--no-tags","--no-write-fetch-head","--recurse-submodules=no","--filter=blob:none","--stdin"]}
{"event":"data","sid":"20260930T183605.206732Z-H274f8de2-P001dd1d6","thread":"main","time":"2026-09-30T18:36:05.208030Z","file":"promisor-remote.c","line":48,"repo":1,"t_abs":0.001420,"t_rel":0.001420,"nesting":1,"category":"promisor","key":"fetch_count","value":"1"}
```

The fixture used a local transport, so it does not claim that an external
network connection occurred in this run. It does prove that the specified guard
can miss an effective promisor remote, after which the exact proposed body
command spawns a fetch child and writes new Git objects. With an HTTP or SSH
promisor remote, Git's documented demand-fetch path can also contact that
remote.[7][8]

This contradicts three R03 contracts: clone-state rejection before object
access, zero fetch child, and zero object-database write.[1] The result is not a
new research question and does not invalidate the evaluated history-recovery
value. It is a proposal-only guard defect. Its correction would require another
proposal pass that enumerates or neutralizes every effective configuration
scope in the exact environment inherited by every Git child, then adds system,
global, worktree, command-environment, and `-c` negative fixtures with zero
fetch and zero Git-state mutation. The existing local-key matrix does not cover
that contract.[4][6][7]

### Other review gates pass but cannot overrule the blocker

The target metadata is ordered and complete; its links resolve; its exact
proposal, antecedents, prior corrections, limits, alternatives, implementation
sequence, acceptance matrix, worst failure, rollback, and confidence are
explicit. The proposal adds no implementation authority and does not modify its
target skill.[1][3][5]

Brain prior work supports the nonblocking parts of the design: resource limits
belong at the consuming boundary; deadlines flow downward; traces prove only
instrumented operations; exact repository and revision evidence must survive
private reasoning; and authoritative transitions remain distinct from
self-reported diagnostics.[6] These method sources do not close the effective-
configuration counterexample.

The proposal's medium confidence is proportionate to its unexecuted package,
one-history sample, portability assumptions, and unmeasured economics.[1] The
verdict is high confidence because the blocking route was reproduced against
Git 2.43.0 with an exact negative guard result, an effective command-scope key,
a recorded fetch child, and object-database additions, while official Git
sources independently establish the configuration scopes and demand-fetch
mechanism.[7][8]

## Verdict and Handoff

**Verdict: DEFER. This is a graveyard closure with no next Forge stage. Two of
two ordinary corrective cycles were already used, and no human extension
exists.**

R03 corrects the four named r02 mechanisms in substantial design detail, but it
is not READY because its local-only clone guard does not cover Git's effective
configuration surface. A command-scope promisor key bypassed the guard and made
the exact object command spawn a fetch and mutate the disposable repository.
READY would therefore overstate the proposal's no-network/no-fetch/no-write
contract.[1][7][8]

A further REVISE or REFRAME would exceed the protocol budget. Reopening requires
an explicit human budget extension and a revised exact proposal that:

1. enumerates all effective Git configuration scopes and inherited command
   overrides, or supplies a verified sanitized environment used identically by
   the guard and every later Git child;
2. defines whether configuration inputs are frozen and rechecked before object
   access, without claiming atomicity it does not provide;
3. adds system-, global-, worktree-, `GIT_CONFIG_*`-, and `-c`-scope promisor
   fixtures whose oracle requires zero history/object call after rejection,
   zero remote-helper or fetch child, and zero object, ref, log, `FETCH_HEAD`,
   config, index, or worktree change; and
4. preserves the current sink, deadline, external-ledger, provenance,
   unknown-state, rollback, and separate-authorization contracts.

Confidence in DEFER is high. The remaining defect is an executed contract
counterexample, not an inference from missing tests. Confidence would fall if a
human-authorized revision demonstrated that the guard and all Git children use
one fully specified effective configuration surface and independently passed
the omitted-scope fixtures. That evidence does not exist in the current
proposal.

## Learning Decision

Strengthen the existing high-confidence lesson, `Derive evaluator and checker
controls from the claimed result contract`; do not add a new lesson or raise its
confidence.[4]

- **Selection:** The historical-retrieval question remains worthwhile. The
  blocker concerns one fail-closed implementation contract, not the evaluated
  decision value.
- **Evidence and test design:** The proposal named the right partial/promisor
  keys but tested only a local source. The decisive counterexample placed the
  same key in a different effective scope and observed the prohibited fetch and
  object writes.
- **Process:** Environment-dependent gates must derive controls from the exact
  effective configuration inherited by the consuming operation, not from one
  convenient file or scope.
- **Repetition:** This is another gap in the same pipeline and does not add an
  independent trial. It does show that the existing claimed-result-contract
  lesson needs an explicit configuration-scope consequence.
- **Coverage:** Updating that lesson is non-duplicative, uses checked evidence,
  leaves its existing high confidence unchanged, and grants no governance,
  implementation, or deployment authority.

## Sources

1. `forge/proposals/forge-history-duplicate-receipt-r03.md` -- exact target,
   corrected sink, deadline, ledger, clone guard, acceptance matrix, limits,
   rollback, and no-implementation boundary. [high]
2. `forge/proposals/forge-history-duplicate-receipt-r01.md` -- first design and
   operation-order contract. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r01.md` -- first
     REVISE, pre-body byte and running-command blockers, and correction count.
     [high]
   - `forge/proposals/forge-history-duplicate-receipt-r02.md` -- second design,
     metadata preflight, child deadlines, counters, and trace contract. [high]
   - `forge/final-reviews/forge-history-duplicate-receipt-review-r02.md` -- second
     REVISE, sink, whole-driver, observability, and partial-clone blockers plus
     the exhausted ordinary budget. [high]
3. `forge/protocol.md` -- review independence, dispositions, correction budget,
   board selection, graveyard closure, transaction, and no-implementation rule.
   [high]
   - `STATUS.md` -- selected exact proposal and preserved unselected rows at
     starting HEAD `db1670f0faf5a3ab3a9c5b773fc10c431607fe79`. [high]
   - `logbook/progress.log` -- selected pipeline handoffs through ENT-017 at the
     same starting HEAD. [high]
   - `logbook/errors.log` -- failure record through ENT-023 at the same starting
     HEAD. [high]
4. `LEARNINGS.md` -- package-preservation, claimed-result-contract,
   effective-configuration coverage, historical-identity, and learning-
   admission rules. [high]
5. `governance/skills/forge-ideate/SKILL.md` -- exact proposed production target
   and current live-tree, log, Brain, full-read, and novelty procedure. [high]
6. `agentic-brain:library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md` -- consuming-boundary hard limits, downward deadlines, and trace-derived attribution. [medium]
   - `agentic-brain:library/coding-agentic-ai/agent-observability-and-debugging.md` -- instrumentation coverage, application-owned operations, and absence-of-evidence limits. [medium]
   - `agentic-brain:library/coding-agentic-ai/coding-agent-workflows-from-repository-context-to-a-verified-patch.md` -- exact repository provenance, bounded context, current-state rereading, and revision-specific evidence. [medium]
   - `agentic-brain:library/coding-agentic-ai/durable-agent-execution-checkpointing-idempotency-and-recovery-across-failures.md` -- authoritative state transitions, diagnostic-trace limits, finite recovery, and failure-boundary tests. [medium]
7. Git project. "git-config Documentation," updated 2026-09-28; accessed
   2026-09-30, Scopes and Environment sections. System, global, local, worktree,
   and command configuration sources were checked.
   https://git-scm.com/docs/git-config [high]
8. Git project. "Partial Clone," updated 2026-09-23; accessed 2026-09-30,
   Non-Goals, Handling Missing Objects, Fetching Missing Objects, and Using many
   promisor remotes sections. Shallow independence, promisor keys, demand fetch,
   and fetch-subprocess behavior were checked.
   https://git-scm.com/docs/partial-clone [high]
9. Git project. "git-cat-file Documentation," updated 2026-09-28; accessed
   2026-09-30, Options and Batch Output sections. Information-only metadata,
   raw body output, NUL framing, and object-size behavior were checked.
   https://git-scm.com/docs/git-cat-file.html [high]
10. Python Software Foundation. "resource - Resource usage information," Python
    3.14.7 documentation, 2026-09-18; accessed 2026-09-30, Resource Limits,
    `setrlimit()`, and `RLIMIT_FSIZE`. File-size limit semantics were checked.
    https://docs.python.org/3.14/library/resource.html [high]
11. Python Software Foundation. "subprocess - Subprocess management," Python
    3.14.7 documentation, 2026-09-19; accessed 2026-09-30, `run()`, timeout,
    POSIX `preexec_fn`, and process-creation limits. Thread safety, child
    termination, waiting, and timeout limits were checked.
    https://docs.python.org/3.14/library/subprocess.html [high]
    - Python Software Foundation. "time - Time access and conversions," Python
      3.14.7 documentation, accessed 2026-09-30, `monotonic()` and
      `monotonic_ns()`. Nondecreasing, system-clock-independent elapsed timing
      was checked. https://docs.python.org/3.14/library/time.html [high]
