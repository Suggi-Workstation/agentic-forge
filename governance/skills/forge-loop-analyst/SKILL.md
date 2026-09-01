---
name: forge-loop-analyst
description: "Advance one Analyst gate in the Forge."
user-invocable: false
disable-model-invocation: false
---

# Forge Analyst Loop

The sole autonomous and interactive entrypoint for Analyst work in the
Forge. One invocation performs at most one independent gate.

## Scope Gate -- HARD GATE

WHAT: keep every side effect inside the current agentic-forge git root.

HOW: resolve the root and each target before every side effect. Web reads and
read-only `query-brain-vps` use are allowed. The Analyst never changes a
Researcher artifact.

PASS: verdict artifact, status, log, lock, git index, optional admitted
learning, and commit all belong to this repo.

HALT: scope cannot be proven, target escapes the root, starting tree is
dirty, or any procedure asks for an external write.

POSITION: before every tool call or command with side effects.

## Eligibility

| State | Stage | Skill |
|:--|:--|:--|
| `active` | `evaluate` | `forge-evaluate` |
| `active` | `verify` | `forge-verify` |

Every other cursor is `NO-OP`. Analyst does not ideate, propose, research,
build, implement, or move a human review gate.

## Procedure

1. Resolve and verify the Forge root. Acquire the ignored local lease with
   `python3 scripts/forge-lock.py acquire --owner analyst
   --lease-seconds 7200 --root <root>`. Code 2 is `NO-OP`.
2. Save the token and release only with that token in every exit path. Send a
   heartbeat before and after long source checks.
3. Fetch remote refs read-only. HALT without writes unless the tree is clean
   and `HEAD` equals `origin/main`. Record starting HEAD and a hash of
   `STATUS.md`; the watcher is outside the lease.
4. Read, in order: `ANCHOR.md`, `STATUS.md`, both protocols,
   `LEARNINGS.md`, both log tails, and the complete active parent chain.
5. Confirm Analyst ownership, one active pipeline, parent resolution, and no
   newer verdict already covers the target.
6. Invoke exactly one mapped stage skill. Give it repository artifacts only,
   not Researcher session reasoning. Before its first write, fetch again and
   recheck starting HEAD, `origin/main`, and the status hash; if any moved,
   stop without writes for a fresh run. It writes one immutable verdict
   artifact and returns `PASS`, `HALT-REVISE`, or `HALT-REJECT`.
7. Apply the state transition exactly:
   - PASS evaluation -> `build` / Researcher.
   - PASS verification -> `awaiting-review` / Human.
   - HALT-REVISE -> named return stage/owner; increment `revision`.
   - HALT-REJECT -> record definitive post-mortem and reset to `ready` only
     in the same validated commit.
8. Reset `failure-count`. Append one multiline `review` ENT block to
   `logbook/progress.log` with target, verdict artifact, failed criteria if
   any, and next owner/stage. Set `last-event` to `progress:ENT-NNN`. Update
   `LEARNINGS.md` only if its repeated-evidence admission rule passes.
9. Run `python3 scripts/validate-forge.py` and relevant regression tests.
   Confirm the diff is limited to verdict artifact, status, progress, and an
   admitted learning.
10. Fetch and recheck starting HEAD plus `origin/main`. If either moved,
    restore only this run's edits and stop for a fresh run. Otherwise stage
    exact paths and commit as `Analyst (Hermes Agent)`. Never stage every
    changed path implicitly or push directly. Verify a clean tree, release
    the lease, and stop.

## Failure Transaction

For tool, parse, provenance, or validation failure, do not invent a verdict.
Restore only run-local output, append one `errors.log` ENT block, increment
`failure-count`, set `last-event` to `errors:ENT-NNN`, and commit the safe
error checkpoint. Three consecutive identical root causes set
`state: blocked`. If the checkpoint itself fails, restore it. Release the
lease and HALT.

## Independence Gate -- HARD GATE

PASS only when:

- the Analyst profile, not Researcher, rendered the verdict;
- expected claims and acceptance criteria were extracted before judging the
  target conclusions;
- every load-bearing claim was checked against the parent evidence;
- verdict and return stage are explicit and state-machine valid;
- the Researcher artifact remained byte-unchanged; and
- uncertainty or timeout was not treated as approval.

## Verification -- HARD GATE

- [ ] Scope, lease, clean-start, and ownership gates passed. (PASS / HALT)
- [ ] Exactly one independent gate ran. (PASS / HALT)
- [ ] Verdict artifact, status, and progress ENT block agree. (PASS / HALT)
- [ ] Validator and relevant tests pass. (PASS / HALT)
- [ ] Exact paths committed; no external write or direct push. (PASS / HALT)
- [ ] Lease released on every exit path. (PASS / HALT)

## Related

- `forge/protocol.md`
- `logbook/protocol.md`
- `governance/skills/forge-evaluate/SKILL.md`
- `governance/skills/forge-verify/SKILL.md`
