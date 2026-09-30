---
name: bounded-index-freshness-recheck
id: 20260930T101043Z
tier: research
pipeline: 20260930T083956Z
author: Researcher
tags: [agent-systems, retrieval, freshness, reliability]
links:
  - forge/ideas/bounded-index-freshness-recheck-r01.md
  - forge/research/bounded-index-freshness-recheck-r01.md
  - forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md
  - forge/protocol.md
  - forge-index/query.py
  - agentic-brain:governance/skills/query-brain-vps.md
  - agentic-brain:governance/skills/query-forge-vps.md
  - agentic-brain:research/insights/stale-index-problem.md
  - agentic-brain:research/insights/vps-brainclone-plus-index.md
  - https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
  - https://docs.cloud.google.com/storage/docs/retry-strategy
confidence: medium
---
# Research: Bounded Index Freshness Recheck, Corrected Replay

## Question and Method

This revision answers the evaluation's bounded correction: does a complete,
durable replay of the exact current HEAD-lag output contract wait and run a
second freshness command only for that subtype, while every noneligible initial
status halts without either action?[1][3]

Before new targeted source inspection, the provisional explanation was that the
first replay's broad `startswith("STALE -- ")` trigger caused the defect. A
full-string classifier for `STALE -- index at <8 hex>, HEAD at <8 hex>` should
recover the same two observed Forge events while separating all other `STALE`
messages before any wait. The material gaps were exact syntax, case handling,
near-match rejection, preservation of initial faults, observability of waits and
second checks, durable runnable bytes, and the post-event 90-second bound.

The investigation then checked the complete current Forge validator, the current
Brain and Forge query procedures, the live-mirror and stale-index references,
the root and first research revision, the evaluation, the applicable method
lessons, and the two primary retry-guidance pages.[2][3][4][5][6][7][9][10]
The current Forge and Brain indexes both passed their read-only freshness checks
before repository search; no watcher, indexer, rebuild, cron, runtime, skill, or
external repository was changed.

The fixture file below was written with every expected result before the first
classifier execution. The classifier was then written as a separate exact file
and executed with Python 3. The first run and a byte-for-byte second run used the
same preserved files. This ordering tests a frozen contract rather than deriving
fixture expectations from observed classifier output. The package is embedded
in full below; it is evidence for this replay, not an implementation.

## Evidence and Findings

### The eligible syntax is one current validator branch

The current validator emits many distinct `STALE --` messages for missing data,
configuration disagreement, metadata/count disagreement, chunk/vector defects,
and live-corpus mismatch. Only after those checks pass does a heartbeat-HEAD
mismatch emit `STALE -- index at <8 chars>, HEAD at <8 chars>`.[4] The validator
accepts upper- or lower-case hexadecimal in the stored 40-character SHA, while
Git normally supplies lower case; the replay therefore accepts eight hex
characters case-insensitively and rejects nonhex, wrong-width, missing-comma,
and trailing-text near matches.[4]

The current query procedures require exit 0 and output beginning `OK --`, halt
on every other result, and prohibit a manual rebuild.[6] The classifier retains
that final gate. It changes only whether one second measurement is eligible; it
contains no path from a failed second result to a query.

### The corrected replay matches the narrow contract

The preserved run returned `summary=22/22`. The two historical exact Forge
HEAD-lag fixtures alone returned `QUERY_AFTER_RECHECK`. The Brain live-corpus
fixture, missing-index and configuration subtypes, `NO INDEX`, `UNVERIFIED`,
missing watcher, malformed and near-match initial outputs, and a nonzero
`OK --` initial output all returned an initial halt with `waited=false` and
`second_checked=false`. Their original initial message is retained in
`initial_fault`.[2][3]

The persistent exact HEAD-lag control waited once, executed one second check,
and halted. The timeout and missing-second-result controls waited but did not
execute a second check. The changed-state control records a permitted wait after
an exact trigger, detects the changed snapshot before the second command, and
halts with `second_checked=false`. Malformed, unverified, persistent, and
nonzero-exit second results halt after exactly one second check. Only exit 0 plus
a second message beginning `OK --` permits `QUERY_AFTER_RECHECK`.

The classifier SHA-256 is
`095f00ff91dae2d2cb0e7a862149a41d9e37931da469c7636ea912da29834f5f`;
the fixture SHA-256 is
`dfeb190028382e5f956189d06e4db041b925bf7f5510d8ead72929995db1dbeb`;
and the first raw-output SHA-256 is
`f1da6f6ff40ff9f35dd16684bb3a638dcb2ba6f875129fc9cb84ad8925302165`.
A second execution produced the same raw-output hash, and `cmp -s` exited 0.
These results verify the exact preserved classifier against its 22 frozen
fixtures. They do not verify shell-level waiting, a modified query skill, live
snapshot capture, or a population recovery rate.

### Complete runnable package

Create three files from the following code blocks, preserving their final
newlines. Run from their directory:

```text
env -u PYTHONPATH python3 classifier.py fixtures.json > raw-output.txt
sha256sum classifier.py fixtures.json raw-output.txt
env -u PYTHONPATH python3 classifier.py fixtures.json > raw-output-rerun.txt
cmp -s raw-output.txt raw-output-rerun.txt
```

#### `classifier.py`

```python
#!/usr/bin/env python3
"""Replay an exact HEAD-lag-only freshness recheck policy."""

import hashlib
import json
import re
import sys
from pathlib import Path

HEAD_LAG = re.compile(
    r"\ASTALE -- index at [0-9A-Fa-f]{8}, HEAD at [0-9A-Fa-f]{8}\Z"
)
CEILING_SECONDS = 90.0


def result(decision, waited, second_checked, initial_fault):
    return {
        "decision": decision,
        "waited": waited,
        "second_checked": second_checked,
        "initial_fault": initial_fault,
    }


def classify(case):
    initial_fault = case["initial_message"]
    if not case["watcher_present"]:
        return result("HALT_MISSING_WATCHER", False, False, initial_fault)

    if case["initial_rc"] == 0 and initial_fault.startswith("OK --"):
        return result("QUERY_INITIAL_OK", False, False, initial_fault)

    if case["initial_rc"] != 1 or HEAD_LAG.fullmatch(initial_fault) is None:
        return result("HALT_INITIAL_STATUS", False, False, initial_fault)

    elapsed = case.get("elapsed_seconds")
    if elapsed is None or elapsed < 0 or elapsed > CEILING_SECONDS:
        return result(
            "HALT_TIMEOUT_OR_MISSING_RECHECK", True, False, initial_fault
        )

    if not case["state_unchanged"]:
        return result("HALT_STATE_CHANGED", True, False, initial_fault)

    second_rc = case.get("second_rc")
    second_message = case.get("second_message")
    if second_rc is None or second_message is None:
        return result(
            "HALT_TIMEOUT_OR_MISSING_RECHECK", True, False, initial_fault
        )

    if second_rc == 0 and second_message.startswith("OK --"):
        return result("QUERY_AFTER_RECHECK", True, True, initial_fault)

    return result("HALT_RECHECK_STATUS", True, True, initial_fault)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 classifier.py fixtures.json")

    classifier_path = Path(__file__)
    fixtures_path = Path(sys.argv[1])
    fixtures = json.loads(fixtures_path.read_text(encoding="ascii"))

    print(f"classifier_sha256={sha256(classifier_path)}")
    print(f"fixtures_sha256={sha256(fixtures_path)}")

    passed = 0
    for case in fixtures:
        actual = classify(case)
        ok = actual == case["expected"]
        passed += int(ok)
        record = {
            "case": case["name"],
            "expected": case["expected"],
            "actual": actual,
            "pass": ok,
        }
        print(json.dumps(record, sort_keys=True, separators=(",", ":")))

    print(f"summary={passed}/{len(fixtures)}")
    raise SystemExit(0 if passed == len(fixtures) else 1)


if __name__ == "__main__":
    main()
```

#### `fixtures.json`

```json
[
  {
    "name": "event-1-forge-head-lag",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 878347b8, HEAD at f8982b69",
    "elapsed_seconds": 60.7108438,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 170 chunks, built 2026-09-29T23:31:04",
    "expected": {"decision": "QUERY_AFTER_RECHECK", "waited": true, "second_checked": true, "initial_fault": "STALE -- index at 878347b8, HEAD at f8982b69"}
  },
  {
    "name": "event-3-forge-head-lag",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at ee82fca6, HEAD at ccc3bcad",
    "elapsed_seconds": 74.096957,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 348 chunks, built 2026-09-30T05:01:03",
    "expected": {"decision": "QUERY_AFTER_RECHECK", "waited": true, "second_checked": true, "initial_fault": "STALE -- index at ee82fca6, HEAD at ccc3bcad"}
  },
  {
    "name": "event-2-live-corpus-no-second-result",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- live corpus differs from manifest (new=0, changed=1, deleted=0)",
    "elapsed_seconds": null,
    "state_unchanged": true,
    "second_rc": null,
    "second_message": null,
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "STALE -- live corpus differs from manifest (new=0, changed=1, deleted=0)"}
  },
  {
    "name": "persistent-exact-head-lag",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 11111111, HEAD at 22222222",
    "elapsed_seconds": 75.0,
    "state_unchanged": true,
    "second_rc": 1,
    "second_message": "STALE -- index at 11111111, HEAD at 22222222",
    "expected": {"decision": "HALT_RECHECK_STATUS", "waited": true, "second_checked": true, "initial_fault": "STALE -- index at 11111111, HEAD at 22222222"}
  },
  {
    "name": "missing-index-data-stale",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index data missing: vectors.npy",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "STALE -- index data missing: vectors.npy"}
  },
  {
    "name": "metadata-config-stale",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index metadata and build config disagree",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "STALE -- index metadata and build config disagree"}
  },
  {
    "name": "nonhex-head-lag-near-match",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 1234567g, HEAD at abcdef12",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "STALE -- index at 1234567g, HEAD at abcdef12"}
  },
  {
    "name": "short-head-lag-near-match",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 1234567, HEAD at abcdef12",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "STALE -- index at 1234567, HEAD at abcdef12"}
  },
  {
    "name": "missing-comma-head-lag-near-match",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678 HEAD at abcdef12",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "STALE -- index at 12345678 HEAD at abcdef12"}
  },
  {
    "name": "trailing-text-head-lag-near-match",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678, HEAD at abcdef12 now",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "STALE -- index at 12345678, HEAD at abcdef12 now"}
  },
  {
    "name": "uppercase-hex-exact-head-lag",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at ABCDEF12, HEAD at 12345678",
    "elapsed_seconds": 30.0,
    "state_unchanged": true,
    "second_rc": 1,
    "second_message": "STALE -- index at ABCDEF12, HEAD at 12345678",
    "expected": {"decision": "HALT_RECHECK_STATUS", "waited": true, "second_checked": true, "initial_fault": "STALE -- index at ABCDEF12, HEAD at 12345678"}
  },
  {
    "name": "initial-no-index",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "NO INDEX -- run 'python index.py --force' first",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "NO INDEX -- run 'python index.py --force' first"}
  },
  {
    "name": "initial-unverified",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "UNVERIFIED -- heartbeat schema, status, or types invalid",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "UNVERIFIED -- heartbeat schema, status, or types invalid"}
  },
  {
    "name": "missing-watcher-with-exact-head-lag",
    "watcher_present": false,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678, HEAD at abcdef12",
    "elapsed_seconds": 10.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_MISSING_WATCHER", "waited": false, "second_checked": false, "initial_fault": "STALE -- index at 12345678, HEAD at abcdef12"}
  },
  {
    "name": "state-changed-before-second-command",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678, HEAD at abcdef12",
    "elapsed_seconds": 60.0,
    "state_unchanged": false,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_STATE_CHANGED", "waited": true, "second_checked": false, "initial_fault": "STALE -- index at 12345678, HEAD at abcdef12"}
  },
  {
    "name": "exact-head-lag-over-ceiling",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678, HEAD at abcdef12",
    "elapsed_seconds": 90.000001,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_TIMEOUT_OR_MISSING_RECHECK", "waited": true, "second_checked": false, "initial_fault": "STALE -- index at 12345678, HEAD at abcdef12"}
  },
  {
    "name": "exact-head-lag-missing-second-result",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678, HEAD at abcdef12",
    "elapsed_seconds": 60.0,
    "state_unchanged": true,
    "second_rc": null,
    "second_message": null,
    "expected": {"decision": "HALT_TIMEOUT_OR_MISSING_RECHECK", "waited": true, "second_checked": false, "initial_fault": "STALE -- index at 12345678, HEAD at abcdef12"}
  },
  {
    "name": "malformed-second-result",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678, HEAD at abcdef12",
    "elapsed_seconds": 60.0,
    "state_unchanged": true,
    "second_rc": 0,
    "second_message": "fresh now",
    "expected": {"decision": "HALT_RECHECK_STATUS", "waited": true, "second_checked": true, "initial_fault": "STALE -- index at 12345678, HEAD at abcdef12"}
  },
  {
    "name": "unverified-second-result",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678, HEAD at abcdef12",
    "elapsed_seconds": 60.0,
    "state_unchanged": true,
    "second_rc": 1,
    "second_message": "UNVERIFIED -- unreadable index metadata",
    "expected": {"decision": "HALT_RECHECK_STATUS", "waited": true, "second_checked": true, "initial_fault": "STALE -- index at 12345678, HEAD at abcdef12"}
  },
  {
    "name": "second-ok-with-nonzero-exit",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "STALE -- index at 12345678, HEAD at abcdef12",
    "elapsed_seconds": 60.0,
    "state_unchanged": true,
    "second_rc": 1,
    "second_message": "OK -- 1 chunks, built 2026-09-30T00:00:00",
    "expected": {"decision": "HALT_RECHECK_STATUS", "waited": true, "second_checked": true, "initial_fault": "STALE -- index at 12345678, HEAD at abcdef12"}
  },
  {
    "name": "initial-ok",
    "watcher_present": true,
    "initial_rc": 0,
    "initial_message": "OK -- 116 chunks, built 2026-09-30T09:53:04",
    "elapsed_seconds": null,
    "state_unchanged": true,
    "second_rc": null,
    "second_message": null,
    "expected": {"decision": "QUERY_INITIAL_OK", "waited": false, "second_checked": false, "initial_fault": "OK -- 116 chunks, built 2026-09-30T09:53:04"}
  },
  {
    "name": "initial-ok-with-nonzero-exit",
    "watcher_present": true,
    "initial_rc": 1,
    "initial_message": "OK -- 116 chunks, built 2026-09-30T09:53:04",
    "elapsed_seconds": null,
    "state_unchanged": true,
    "second_rc": null,
    "second_message": null,
    "expected": {"decision": "HALT_INITIAL_STATUS", "waited": false, "second_checked": false, "initial_fault": "OK -- 116 chunks, built 2026-09-30T09:53:04"}
  }
]
```

#### `raw-output.txt`

```text
classifier_sha256=095f00ff91dae2d2cb0e7a862149a41d9e37931da469c7636ea912da29834f5f
fixtures_sha256=dfeb190028382e5f956189d06e4db041b925bf7f5510d8ead72929995db1dbeb
{"actual":{"decision":"QUERY_AFTER_RECHECK","initial_fault":"STALE -- index at 878347b8, HEAD at f8982b69","second_checked":true,"waited":true},"case":"event-1-forge-head-lag","expected":{"decision":"QUERY_AFTER_RECHECK","initial_fault":"STALE -- index at 878347b8, HEAD at f8982b69","second_checked":true,"waited":true},"pass":true}
{"actual":{"decision":"QUERY_AFTER_RECHECK","initial_fault":"STALE -- index at ee82fca6, HEAD at ccc3bcad","second_checked":true,"waited":true},"case":"event-3-forge-head-lag","expected":{"decision":"QUERY_AFTER_RECHECK","initial_fault":"STALE -- index at ee82fca6, HEAD at ccc3bcad","second_checked":true,"waited":true},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- live corpus differs from manifest (new=0, changed=1, deleted=0)","second_checked":false,"waited":false},"case":"event-2-live-corpus-no-second-result","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- live corpus differs from manifest (new=0, changed=1, deleted=0)","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at 11111111, HEAD at 22222222","second_checked":true,"waited":true},"case":"persistent-exact-head-lag","expected":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at 11111111, HEAD at 22222222","second_checked":true,"waited":true},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index data missing: vectors.npy","second_checked":false,"waited":false},"case":"missing-index-data-stale","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index data missing: vectors.npy","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index metadata and build config disagree","second_checked":false,"waited":false},"case":"metadata-config-stale","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index metadata and build config disagree","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index at 1234567g, HEAD at abcdef12","second_checked":false,"waited":false},"case":"nonhex-head-lag-near-match","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index at 1234567g, HEAD at abcdef12","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index at 1234567, HEAD at abcdef12","second_checked":false,"waited":false},"case":"short-head-lag-near-match","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index at 1234567, HEAD at abcdef12","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index at 12345678 HEAD at abcdef12","second_checked":false,"waited":false},"case":"missing-comma-head-lag-near-match","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index at 12345678 HEAD at abcdef12","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12 now","second_checked":false,"waited":false},"case":"trailing-text-head-lag-near-match","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12 now","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at ABCDEF12, HEAD at 12345678","second_checked":true,"waited":true},"case":"uppercase-hex-exact-head-lag","expected":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at ABCDEF12, HEAD at 12345678","second_checked":true,"waited":true},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"NO INDEX -- run 'python index.py --force' first","second_checked":false,"waited":false},"case":"initial-no-index","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"NO INDEX -- run 'python index.py --force' first","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"UNVERIFIED -- heartbeat schema, status, or types invalid","second_checked":false,"waited":false},"case":"initial-unverified","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"UNVERIFIED -- heartbeat schema, status, or types invalid","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_MISSING_WATCHER","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":false,"waited":false},"case":"missing-watcher-with-exact-head-lag","expected":{"decision":"HALT_MISSING_WATCHER","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_STATE_CHANGED","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":false,"waited":true},"case":"state-changed-before-second-command","expected":{"decision":"HALT_STATE_CHANGED","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":false,"waited":true},"pass":true}
{"actual":{"decision":"HALT_TIMEOUT_OR_MISSING_RECHECK","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":false,"waited":true},"case":"exact-head-lag-over-ceiling","expected":{"decision":"HALT_TIMEOUT_OR_MISSING_RECHECK","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":false,"waited":true},"pass":true}
{"actual":{"decision":"HALT_TIMEOUT_OR_MISSING_RECHECK","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":false,"waited":true},"case":"exact-head-lag-missing-second-result","expected":{"decision":"HALT_TIMEOUT_OR_MISSING_RECHECK","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":false,"waited":true},"pass":true}
{"actual":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":true,"waited":true},"case":"malformed-second-result","expected":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":true,"waited":true},"pass":true}
{"actual":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":true,"waited":true},"case":"unverified-second-result","expected":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":true,"waited":true},"pass":true}
{"actual":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":true,"waited":true},"case":"second-ok-with-nonzero-exit","expected":{"decision":"HALT_RECHECK_STATUS","initial_fault":"STALE -- index at 12345678, HEAD at abcdef12","second_checked":true,"waited":true},"pass":true}
{"actual":{"decision":"QUERY_INITIAL_OK","initial_fault":"OK -- 116 chunks, built 2026-09-30T09:53:04","second_checked":false,"waited":false},"case":"initial-ok","expected":{"decision":"QUERY_INITIAL_OK","initial_fault":"OK -- 116 chunks, built 2026-09-30T09:53:04","second_checked":false,"waited":false},"pass":true}
{"actual":{"decision":"HALT_INITIAL_STATUS","initial_fault":"OK -- 116 chunks, built 2026-09-30T09:53:04","second_checked":false,"waited":false},"case":"initial-ok-with-nonzero-exit","expected":{"decision":"HALT_INITIAL_STATUS","initial_fault":"OK -- 116 chunks, built 2026-09-30T09:53:04","second_checked":false,"waited":false},"pass":true}
summary=22/22
```

### Evidence boundary

The two positive fixtures are the exact session values already reconstructed in
the first report and independently reproduced by the evaluation. Historical
Forge error and progress records corroborate the initial faults, natural watcher
recovery, and completed stages at commit
`11b0425908ecdd0cc71bb54e483833ac466cdf55`.[2][3][8] They remain two events on
one host, repository, watcher, and operating period, not independent systems.
The Brain live-corpus event still lacks a preserved second result and remains an
initial halt under the narrower trigger.[2]

The 90-second ceiling remains a post-event, unvalidated design assumption. It
contains both observed intervals, 60.7108438 and 74.0969570 seconds, but is not a
prospective percentile or service guarantee.[2][3] AWS describes retries as a
way to absorb transient failures while warning about added load and side effects;
Google conditions retries on retryable status and idempotency and exposes bounded
attempt and timeout controls.[9][10] Those sources support one bounded read-only
attempt in principle. They do not validate this local subtype, ceiling, or
benefit rate.

## Alternatives and Implications

| Alternative | Evidence-supported result | Remaining cost or limit |
|:--|:--|:--|
| Keep immediate HALT | Simplest policy; preserves the current gate and avoids every wait.[6] | Would have ended the two recorded exact HEAD-lag sessions before their later literal `OK --` results.[2] |
| One exact-text HEAD-lag recheck | The preserved 22-case replay recovers both positives; all noneligible initial statuses halt without a wait or second check. | Text-coupled, adds at most 90 seconds, and remains synthetic rather than live-integrated. |
| Structured validator status | Could avoid coupling eligibility to human-readable output. | Requires a larger tool and skill change not researched or tested here. |
| Recheck every `STALE --` | None demonstrated beyond exact HEAD lag. | Delays integrity, compatibility, and corpus faults; contradicted by the current status taxonomy and the evaluation.[3][4] |
| Rebuild, invoke the watcher, or poll repeatedly | Could alter or observe more states. | Exceeds scope, can hide a producer fault, and is not authorized.[1][6][7] |

The correction removes the first replay's trigger-contract defect and makes its
bytes independently recoverable. It does not decide whether the incremental
benefit justifies changing a skill. A fresh evaluator must judge the report
before any proposal, and implementation remains outside the Forge loop.

## Response to Feedback and Remaining Questions

1. **Durable package:** The exact classifier, all fixtures and expected outcomes,
   invocation, complete raw per-case output, and three hashes are embedded above.
   A second local run was byte-identical. Independent evaluator execution is
   still required; this session does not label its own rerun independent.
2. **Exact eligible trigger:** `HEAD_LAG.fullmatch` permits only the current full
   HEAD-lag text with two eight-character hexadecimal fields. Every other initial
   `STALE --` subtype halts with no wait or second command.
3. **Observable actions and near matches:** Every result carries `waited` and
   `second_checked`. Nonhex, short-width, missing-comma, and trailing-text cases
   all halt initially. Missing watcher, changed state, timeout, malformed second
   output, and nonzero exit cases have distinct expectations.
4. **Pre-run expectations:** The fixture JSON, including expected action fields,
   was completed before the first classifier run. The raw output shows only the
   two verified event fixtures reaching `QUERY_AFTER_RECHECK`; the initial fresh
   control separately reaches `QUERY_INITIAL_OK`.
5. **Ceiling claim:** The report retains 90 seconds only as a post-event bounded
   assumption. No recovery rate, percentile, prospective validation, or future
   workload guarantee is claimed.

One implementation-level ambiguity remains: a prose-only skill rule would need
to define how it captures and compares `HEAD` and worktree state around the wait
without creating a transaction race. This replay represents that comparison as
`state_unchanged`; it does not test shell wiring. A proposal should not claim
live validation without a separate acceptance test. Another uncertainty is
whether long-term robustness warrants a structured status from the validator
rather than an exact text classifier; that is a larger alternative, not evidence
against the corrected replay.

Confidence is medium. Confidence is high that the embedded standard-library
classifier and frozen fixtures reproduce the declared 22 outcomes and close the
evaluation's preservation and trigger-boundary blockers. Overall confidence
remains medium because the positives are two same-system historical events, the
ceiling is post-event, and no production skill or live waiting path was tested.
Confidence would rise after an independent extraction/rerun and one prospective
natural HEAD-lag event under a frozen bound. It would fall if the validator's
message contract changes, extraction changes any hash, or shell-level snapshot
handling permits a second command after changed state.

## Sources

1. `forge/ideas/bounded-index-freshness-recheck-r01.md` -- root question,
   fail-closed boundary, research thresholds, and excluded producer actions.
   [high]
2. `forge/research/bounded-index-freshness-recheck-r01.md` -- first event
   reconstruction, exact positive outputs and durations, broad replay, limits,
   and the narrow HEAD-lag recommendation. [high]
3. `forge/evaluations/bounded-index-freshness-recheck-evaluation-r01.md` --
   REVISE verdict, independently reproduced events, trigger-contract defect,
   package-preservation defect, and five bounded correction requirements. [high]
4. `forge-index/query.py` -- current complete validator, `STALE` taxonomy,
   hexadecimal SHA validation, exact HEAD-lag output, and exit-code contract.
   [high]
5. `LEARNINGS.md` -- durable executable/fixture/raw-output requirement and the
   rule to derive controls from each claimed result-contract predicate. [high]
6. `agentic-brain:governance/skills/query-brain-vps.md` -- current Brain
   watcher, literal-OK, immediate-HALT, and no-rebuild procedure. [high]
   - `agentic-brain:governance/skills/query-forge-vps.md` -- matching Forge
     procedure and read-only freshness gate. [high]
7. `agentic-brain:research/insights/stale-index-problem.md` -- consistency over
   liveness and current validator coverage. [medium]
   - `agentic-brain:research/insights/vps-brainclone-plus-index.md` -- natural
     one-minute watcher cadence, watcher ownership, and fail-closed architecture.
     [medium]
8. `logbook/errors.log` -- historical ENT-009, ENT-016, and ENT-018 fault and
   recovery records, verified at Git commit
   `11b0425908ecdd0cc71bb54e483833ac466cdf55`. [high]
   - `logbook/progress.log` -- matching historical stage outcomes at the same
     commit. [high]
9. Amazon Web Services. "Timeouts, retries, and backoff with jitter," Marc
   Brooker, undated; accessed 2026-09-30, Failures Happen and Retries and backoff
   sections. Transient recovery, retry load, waiting, and idempotency were
   checked.
   https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter
   [medium]
10. Google Cloud. "Retry strategy," undated; accessed 2026-09-30, idempotency,
    customization, and anti-pattern sections. Conditional retries, attempt
    limits, and timeout bounds were checked.
    https://docs.cloud.google.com/storage/docs/retry-strategy [high]
