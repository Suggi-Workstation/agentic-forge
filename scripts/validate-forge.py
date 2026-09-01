#!/usr/bin/env python3
"""Validate the Agentic Forge workflow contract without side effects."""

import argparse
import hashlib
import re
import sys
from pathlib import Path


EXPECTED_SKILLS = {
    "forge-build",
    "forge-evaluate",
    "forge-ideate",
    "forge-loop-analyst",
    "forge-loop-feynman",
    "forge-loop-researcher",
    "forge-propose",
    "forge-research",
    "forge-verify",
}

STAGE_DIRS = {
    "ideas": ("idea", "Researcher"),
    "proposals": ("proposal", "Researcher"),
    "research": ("research", "Researcher"),
    "evaluations": ("evaluation", "Analyst"),
    "builds": ("build", "Researcher"),
    "verifications": ("verification", "Analyst"),
    "graveyard": ("graveyard", None),
}

STATUS_FIELDS = [
    "state",
    "pipeline",
    "research-path",
    "stage",
    "owner",
    "active-artifact",
    "revision",
    "failure-count",
    "last-verdict",
    "last-event",
    "next-action",
    "blocker",
    "updated",
]

STAGE_OWNERS = {
    "ideate": "Researcher",
    "propose": "Researcher",
    "research": "Researcher",
    "evaluate": "Analyst",
    "build": "Researcher",
    "verify": "Analyst",
    "review": "Human",
}

ARTIFACT_KEYS = {
    "name",
    "id",
    "pipeline",
    "research_path",
    "stage",
    "owner",
    "status",
    "parent",
    "supersedes",
    "confidence",
    "created",
}

PARENT_STAGES = {
    "idea": set(),
    "proposal": {"idea", "evaluation", "verification"},
    "research": {"proposal", "evaluation", "verification"},
    "evaluation": {"research"},
    "build": {"evaluation", "verification"},
    "verification": {"build"},
    "graveyard": {"idea", "proposal", "research", "evaluation", "build", "verification"},
}

ARTIFACT_SECTIONS = {
    "idea": (
        "## Research Path", "## Research Question", "## Hypothesis",
        "## Why This Matters", "## Prior Work and Non-Duplication",
        "## Claims to Test", "## Expected Build", "## Kill Criteria",
        "## Initial Confidence",
    ),
    "proposal": (
        "## Research Question", "## Decision This Research Will Inform",
        "## Claim and Evidence Map", "## Method", "## Source Strategy",
        "## Counter-Hypotheses", "## Acceptance Tests",
        "## Kill Criteria and Stop Conditions",
        "## Worst Failure and Prevention", "## Execution Bound",
    ),
    "research": (
        "## Method Execution", "## Source Register", "## Findings by Claim",
        "## Contradictory Evidence and Counter-Hypotheses",
        "## Acceptance Tests and Kill Criteria",
        "## Gaps, Limitations, and Method Deviations",
        "## Research Conclusion", "## Updated Confidence",
    ),
    "evaluation": (
        "## Verdict", "## Pre-Read Acceptance Baseline", "## Claim Audit",
        "## Method and Coverage Audit", "## Build Feasibility",
        "## Failed Criteria", "## Return Stage",
        "## Rejection Root Cause and Revival Conditions",
        "## What Was Rejected", "## Failed Gate and Evidence",
        "## Provenance Chain", "## Analyst Confidence",
    ),
    "build": (
        "## Decision", "## Evidence Trace", "## Design or Framework",
        "## Simplest Viable Form", "## Implementation Sequence",
        "## Acceptance and Regression Tests",
        "## Worst Failure and Prevention", "## Risks and Rollback",
        "## Alternatives Rejected", "## Limitations and Open Questions",
        "## Human Decisions Required", "## Provenance Chain",
    ),
    "verification": (
        "## Verdict", "## Pre-Read Acceptance Baseline",
        "## Claim Traceability", "## Design Consistency Audit",
        "## Test and Rollback Audit", "## Safety and Confinement Audit",
        "## Failed Criteria", "## Return Stage",
        "## Rejection Root Cause and Revival Conditions",
        "## What Was Rejected", "## Failed Gate and Evidence",
        "## Provenance Chain", "## Analyst Confidence",
    ),
    "graveyard": (
        "## What Was Rejected", "## Failed Gate and Evidence",
        "## Root Cause", "## Reuse or Revival Conditions",
        "## Provenance Chain",
    ),
}

ID_RE = re.compile(r"^\d{8}T\d{6}Z$")
CREATED_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
ARTIFACT_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*-r\d{2}\.md$")
ENT_RE = re.compile(
    r"^## \[ENT-(\d{3,})\] \| "
    r"\d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC \| "
    r"([^|]+) \| ([a-z-]+)(?: \|.*)?$"
)

LOG_ARCHIVE_HASHES = {
    "scripts/logbook-archive.py":
        "9508a05a0b939102e903e0d4c8672df33257d5f20265d3c3c2cfa456ea19f378",
    ".github/workflows/logbook-archive.yml":
        "9a36c21e3a91fc3deb6a8c5c4861f6842e8e42174bd7334f65a83d7342d3a22b",
}

SKILL_FORBIDDEN = {
    "JOURNAL.md": re.compile(r"JOURNAL\.md"),
    "old progress path": re.compile(r"logs/progress\.log"),
    "old insight stage": re.compile(r"forge/insights|forge-insight"),
    "old validation stage": re.compile(r"forge/validations|forge-validate"),
    "old actor": re.compile(r"\bNeo\b"),
    "different-model dependency": re.compile(r"different model", re.IGNORECASE),
    "direct brain path": re.compile(r"/srv/brain"),
    "direct investing path": re.compile(r"/srv/investing"),
    "profile path": re.compile(r"/home/hermes"),
    "direct push": re.compile(r"git push"),
    "stage-all": re.compile(r"git add -A"),
    "old brain skill": re.compile(r"query-brain(?!-vps)"),
    "literal patch marker": re.compile(r"^\+", re.MULTILINE),
}

TEXT_SUFFIXES = {
    ".md", ".log", ".py", ".sh", ".yml", ".yaml", ".txt", ".json"
}
TEXT_NAMES = {".gitignore", ".gitattributes"}


class Contract:
    def __init__(self, root):
        self.root = root.resolve()
        self.errors = []
        self.artifacts = {}
        self.status = {}
        self.log_ids = {"progress": set(), "errors": set()}

    def error(self, message):
        self.errors.append(message)

    def require(self, relative):
        path = self.root / relative
        if not path.exists():
            self.error(f"missing required path: {relative}")
        return path

    def read_ascii(self, path):
        try:
            return path.read_text(encoding="ascii")
        except UnicodeDecodeError:
            self.error(f"non-ASCII text: {path.relative_to(self.root)}")
        except OSError as exc:
            self.error(f"cannot read {path.relative_to(self.root)}: {exc}")
        return ""

    def frontmatter(self, path):
        text = self.read_ascii(path)
        lines = text.splitlines()
        if not lines or lines[0] != "---":
            self.error(f"missing frontmatter: {path.relative_to(self.root)}")
            return {}, text
        try:
            end = lines.index("---", 1)
        except ValueError:
            self.error(f"unterminated frontmatter: {path.relative_to(self.root)}")
            return {}, text

        values = {}
        for line in lines[1:end]:
            if not line or line[0].isspace() or ":" not in line:
                continue
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
        return values, text

    def validate_ascii_and_symlinks(self):
        for path in self.root.rglob("*"):
            if ".git" in path.parts or "__pycache__" in path.parts:
                continue
            if path.is_symlink():
                try:
                    path.resolve().relative_to(self.root)
                except ValueError:
                    self.error(f"symlink escapes repository: {path.relative_to(self.root)}")
                continue
            if not path.is_file():
                continue
            if path.suffix in TEXT_SUFFIXES or path.name in TEXT_NAMES:
                data = path.read_bytes()
                if any(byte > 127 for byte in data):
                    self.error(f"non-ASCII byte: {path.relative_to(self.root)}")

    def validate_layout(self):
        required = [
            "ANCHOR.md",
            "STATUS.md",
            "LEARNINGS.md",
            "README.md",
            "forge/protocol.md",
            "logbook/protocol.md",
            "logbook/progress.log",
            "logbook/errors.log",
            "scripts/forge-lock.py",
            "scripts/forge-status-monitor.py",
            "scripts/logbook-archive.py",
            "tests/test-forge-system.py",
        ]
        for relative in required:
            self.require(relative)
        for directory in list(STAGE_DIRS) + ["archive"]:
            self.require(f"forge/{directory}")
        if (self.root / "JOURNAL.md").exists():
            self.error("forbidden duplicate state file: JOURNAL.md")
        for relative in ("forge/insights/.gitkeep", "forge/validations/.gitkeep"):
            if (self.root / relative).exists():
                self.error(f"stale stage path: {relative}")
        ignore = self.read_ascii(self.require(".gitignore"))
        if ".forge-lock/" not in ignore:
            self.error(".gitignore must ignore .forge-lock/")
        if ".forge-lock.guard" not in ignore:
            self.error(".gitignore must ignore .forge-lock.guard")

    def validate_control_files(self):
        anchor = self.read_ascii(self.root / "ANCHOR.md")
        for token in (
            "## Eternal Mission",
            "## Optional Research Path A -- Agent Systems",
            "## Optional Research Path B -- Value-Investing Systems",
            "forge/builds/",
        ):
            if token not in anchor:
                self.error(f"ANCHOR missing required token: {token}")

        status_path = self.root / "STATUS.md"
        status_text = self.read_ascii(status_path)
        if len(status_text) > 2000:
            self.error("STATUS.md exceeds 2000-character hot-context budget")
        status = {}
        order = []
        for line in status_text.splitlines():
            if ":" not in line or line.startswith(("---", "#")):
                continue
            key, value = line.split(":", 1)
            if key in STATUS_FIELDS:
                status[key] = value.strip()
                order.append(key)
        if order != STATUS_FIELDS:
            self.error(f"STATUS field order/schema mismatch: {order}")
            return
        self.status = status

        state = status["state"]
        stage = status["stage"]
        owner = status["owner"]
        if state not in {"ready", "active", "awaiting-review", "blocked"}:
            self.error(f"invalid STATUS state: {state}")
        if STAGE_OWNERS.get(stage) != owner:
            self.error(f"invalid stage/owner pair: {stage}/{owner}")
        if status["research-path"] not in {
            "none", "agent-systems", "value-investing-systems"
        }:
            self.error(f"invalid research path: {status['research-path']}")
        if status["last-verdict"] not in {
            "none", "PASS", "HALT-REVISE", "HALT-REJECT"
        }:
            self.error(f"invalid last verdict: {status['last-verdict']}")
        if status["last-event"] != "none" and not re.match(
            r"^(progress|errors):ENT-\d{3,}$", status["last-event"]
        ):
            self.error("last-event must be none or <log>:ENT-NNN")
        numeric = {}
        for key in ("revision", "failure-count"):
            try:
                numeric[key] = int(status[key])
                if numeric[key] < 0:
                    raise ValueError
            except ValueError:
                numeric[key] = -1
                self.error(f"STATUS {key} must be a non-negative integer")
        if not CREATED_RE.match(status["updated"]):
            self.error("STATUS updated must be YYYY-MM-DDTHH:MM:SSZ")

        if state == "ready":
            expected = {
                "pipeline": "none",
                "research-path": "none",
                "stage": "ideate",
                "owner": "Researcher",
                "active-artifact": "none",
            }
            for key, value in expected.items():
                if status[key] != value:
                    self.error(f"ready STATUS requires {key}: {value}")
            if status["failure-count"] != "0" or status["blocker"] != "none":
                self.error("ready STATUS requires zero failures and no blocker")
        elif state == "active":
            if not ID_RE.match(status["pipeline"]):
                self.error("active STATUS pipeline must be an artifact ID")
            active = self.root / status["active-artifact"]
            if not active.is_file():
                self.error("active STATUS artifact does not resolve")
        elif state == "awaiting-review":
            if stage != "review" or owner != "Human":
                self.error("awaiting-review requires review/Human")
        elif state == "blocked":
            if numeric["failure-count"] < 3 or status["blocker"] == "none":
                self.error("blocked STATUS requires three failures and a blocker")

        learnings = self.read_ascii(self.root / "LEARNINGS.md")
        if len(learnings) > 12000:
            self.error("LEARNINGS.md exceeds 12000-character budget")
        if len(re.findall(r"^## \[LRN-", learnings, re.MULTILINE)) > 12:
            self.error("LEARNINGS.md exceeds twelve active lessons")

    def validate_skills(self):
        skills_root = self.root / "governance" / "skills"
        actual = {
            path.parent.name
            for path in skills_root.glob("*/SKILL.md")
            if path.is_file()
        }
        if actual != EXPECTED_SKILLS:
            missing = sorted(EXPECTED_SKILLS - actual)
            extra = sorted(actual - EXPECTED_SKILLS)
            self.error(f"skill set mismatch: missing={missing} extra={extra}")

        for name in sorted(EXPECTED_SKILLS & actual):
            path = skills_root / name / "SKILL.md"
            fm, text = self.frontmatter(path)
            if fm.get("name") != name:
                self.error(f"skill name/path mismatch: {name}")
            expected_frontmatter = {
                "name",
                "description",
                "user-invocable",
                "disable-model-invocation",
            }
            if set(fm) != expected_frontmatter:
                self.error(
                    f"{name} frontmatter must contain only "
                    f"{sorted(expected_frontmatter)}"
                )
            if fm.get("user-invocable") != "false":
                self.error(f"{name} must set user-invocable: false")
            if fm.get("disable-model-invocation") != "false":
                self.error(f"{name} must set disable-model-invocation: false")
            description = fm.get("description", "")
            if len(description) > 60 or not description.endswith("."):
                self.error(f"{name} description violates 60-char sentence rule")
            for label, pattern in SKILL_FORBIDDEN.items():
                if pattern.search(text):
                    self.error(f"forbidden skill token ({label}): {name}")

        for loop in ("forge-loop-researcher", "forge-loop-analyst"):
            text = self.read_ascii(skills_root / loop / "SKILL.md")
            for token in (
                "## Scope Gate -- HARD GATE",
                "query-brain-vps",
                "NO-OP",
                "starting HEAD",
                "status hash",
                "origin/main",
            ):
                if token not in text:
                    self.error(f"{loop} missing loop contract token: {token}")

        template_stages = {
            "forge-ideate": "idea",
            "forge-propose": "proposal",
            "forge-research": "research",
            "forge-evaluate": "evaluation",
            "forge-build": "build",
            "forge-verify": "verification",
        }
        for skill, stage in template_stages.items():
            path = skills_root / skill / "assets" / "template.md"
            fm, text = self.frontmatter(path)
            if fm.get("stage") != stage:
                self.error(f"{skill} template stage mismatch")
            if re.search(r"^\+", text, re.MULTILINE):
                self.error(f"{skill} template contains a literal patch marker")
            for token in (
                "pipeline:", "research_path:", f"stage: {stage}",
                "owner:", "status: complete", "parent:", "supersedes:",
                "confidence:", "created:",
            ):
                if token not in text:
                    self.error(f"{skill} template missing token: {token}")

    def parse_log(self, path):
        text = self.read_ascii(path)
        lines = text.splitlines()
        entries = []
        header_indexes = []
        in_comment = False
        seen_entry = False

        for index, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("<!--"):
                in_comment = True
            if in_comment:
                if "-->" in stripped:
                    in_comment = False
                continue
            match = ENT_RE.match(line)
            if match:
                seen_entry = True
                header_indexes.append(index)
                entries.append((int(match.group(1)), match.group(2).strip(), match.group(3)))
                if index > 0 and lines[index - 1].strip():
                    self.error(
                        "missing blank line before ENT entry: "
                        f"{path.relative_to(self.root)}"
                    )
                continue
            if not seen_entry and stripped:
                self.error(
                    f"non-ENT content before first entry: {path.relative_to(self.root)}"
                )
                break
            if line.startswith("## [ENT-") and not match:
                self.error(f"malformed ENT header: {path.relative_to(self.root)}:{index + 1}")

        for position, start in enumerate(header_indexes):
            end = header_indexes[position + 1] if position + 1 < len(header_indexes) else len(lines)
            body = [line for line in lines[start + 1:end] if line.strip()]
            if len(body) < 2:
                self.error(f"ENT body must have multiple lines: {path.relative_to(self.root)}")

        base = path.name.split("-", 1)[0].replace(".log", "")
        allowed = {"progress": {"research", "review", "general"}, "errors": {"error"}}
        for _, _, category in entries:
            if base in allowed and category not in allowed[base]:
                self.error(f"invalid {base} category: {category}")
        return [entry[0] for entry in entries]

    def validate_logs(self):
        archive_dir = self.root / "logbook" / "archive"
        for base in ("progress", "errors"):
            ids = []
            for path in sorted(archive_dir.glob(f"{base}-*.log")):
                ids.extend(self.parse_log(path))
            ids.extend(self.parse_log(self.root / "logbook" / f"{base}.log"))
            self.log_ids[base] = set(ids)
            if ids:
                expected = list(range(1, max(ids) + 1))
                if ids != expected:
                    self.error(f"{base}.log ENT sequence mismatch: {ids}")

        last_event = self.status.get("last-event", "none")
        if last_event != "none" and ":ENT-" in last_event:
            base, raw_id = last_event.split(":ENT-", 1)
            if not raw_id.isdigit() or int(raw_id) not in self.log_ids.get(base, set()):
                self.error(f"STATUS last-event does not resolve: {last_event}")

        for relative, expected in LOG_ARCHIVE_HASHES.items():
            path = self.root / relative
            actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else "missing"
            if actual != expected:
                self.error(f"logbook archive mirror drift: {relative}")

    def validate_artifacts(self):
        for directory, (expected_stage, expected_owner) in STAGE_DIRS.items():
            for path in sorted((self.root / "forge" / directory).glob("*.md")):
                if not ARTIFACT_NAME_RE.match(path.name):
                    self.error(f"invalid artifact filename: {path.relative_to(self.root)}")
                fm, text = self.frontmatter(path)
                missing = ARTIFACT_KEYS - set(fm)
                if missing:
                    self.error(
                        f"artifact missing keys {sorted(missing)}: "
                        f"{path.relative_to(self.root)}"
                    )
                    continue
                artifact_id = fm["id"]
                file_match = re.match(r"^(.+)-r(\d{2})\.md$", path.name)
                if file_match and fm["name"] != file_match.group(1):
                    self.error(f"artifact name/file mismatch: {path.relative_to(self.root)}")
                if not ID_RE.match(artifact_id):
                    self.error(f"invalid artifact id: {path.relative_to(self.root)}")
                if artifact_id in self.artifacts:
                    self.error(f"duplicate artifact id: {artifact_id}")
                self.artifacts[artifact_id] = (path, fm)
                if fm["stage"] != expected_stage:
                    self.error(f"artifact stage/path mismatch: {path.relative_to(self.root)}")
                if expected_owner and fm["owner"] != expected_owner:
                    self.error(f"artifact owner/path mismatch: {path.relative_to(self.root)}")
                if fm["status"] != "complete":
                    self.error(f"artifact status must be complete: {path.relative_to(self.root)}")
                for heading in ARTIFACT_SECTIONS[expected_stage]:
                    if not re.search(
                        rf"^{re.escape(heading)}\s*$", text, re.MULTILINE
                    ):
                        self.error(
                            "artifact missing required section "
                            f"{heading}: {path.relative_to(self.root)}"
                        )
                if fm["research_path"] not in {"agent-systems", "value-investing-systems"}:
                    self.error(f"invalid artifact research_path: {path.relative_to(self.root)}")
                if not CREATED_RE.match(fm["created"]):
                    self.error(f"invalid artifact created timestamp: {path.relative_to(self.root)}")
                elif ID_RE.match(artifact_id):
                    id_day = f"{artifact_id[:4]}-{artifact_id[4:6]}-{artifact_id[6:8]}"
                    if not fm["created"].startswith(id_day):
                        self.error(
                            "artifact id/created date mismatch: "
                            f"{path.relative_to(self.root)}"
                        )
                if file_match:
                    revision = int(file_match.group(2))
                    if revision == 1 and fm["supersedes"] != "none":
                        self.error(f"r01 artifact cannot supersede: {path.relative_to(self.root)}")
                    if revision > 1 and fm["supersedes"] == "none":
                        self.error(
                            "revision must supersede prior artifact: "
                            f"{path.relative_to(self.root)}"
                        )
                try:
                    confidence = float(fm["confidence"])
                    if not 0.0 <= confidence <= 1.0:
                        raise ValueError
                except ValueError:
                    self.error(f"invalid artifact confidence: {path.relative_to(self.root)}")

        for artifact_id, (path, fm) in self.artifacts.items():
            stage = fm["stage"]
            if stage == "idea":
                if fm["parent"] != "root" or fm["pipeline"] != artifact_id:
                    self.error(f"idea root/pipeline mismatch: {path.relative_to(self.root)}")
            else:
                parent = self.artifacts.get(fm["parent"])
                if not parent:
                    self.error(f"artifact parent missing: {path.relative_to(self.root)}")
                elif parent[1]["stage"] not in PARENT_STAGES[stage]:
                    self.error(f"invalid parent stage: {path.relative_to(self.root)}")
                elif parent[1]["pipeline"] != fm["pipeline"]:
                    self.error(
                        "artifact parent belongs to another pipeline: "
                        f"{path.relative_to(self.root)}"
                    )
                idea = self.artifacts.get(fm["pipeline"])
                if not idea or idea[1]["stage"] != "idea":
                    self.error(f"artifact pipeline idea missing: {path.relative_to(self.root)}")
            supersedes = fm["supersedes"]
            if supersedes != "none":
                prior = self.artifacts.get(supersedes)
                if not prior or prior[1]["stage"] != stage:
                    self.error(f"invalid supersedes link: {path.relative_to(self.root)}")
                elif (
                    prior[1]["pipeline"] != fm["pipeline"]
                    or prior[1]["name"] != fm["name"]
                ):
                    self.error(
                        "supersedes crosses artifact identity: "
                        f"{path.relative_to(self.root)}"
                    )

        for relation, terminal in (("parent", "root"), ("supersedes", "none")):
            reported = set()
            for start in self.artifacts:
                seen = []
                current = start
                while current in self.artifacts:
                    if current in seen:
                        cycle = tuple(seen[seen.index(current):] + [current])
                        signature = tuple(sorted(cycle))
                        if signature not in reported:
                            self.error(
                                f"provenance cycle in {relation}: "
                                + " -> ".join(cycle)
                            )
                            reported.add(signature)
                        break
                    seen.append(current)
                    next_id = self.artifacts[current][1][relation]
                    if next_id == terminal:
                        break
                    current = next_id

        state = self.status.get("state")
        if state in {"active", "awaiting-review"}:
            relative = self.status.get("active-artifact", "none")
            active_path = (self.root / relative).resolve()
            active = next(
                (
                    fm for path, fm in self.artifacts.values()
                    if path.resolve() == active_path
                ),
                None,
            )
            if not active:
                self.error("active STATUS artifact does not match a Forge artifact")
            else:
                if active["pipeline"] != self.status.get("pipeline"):
                    self.error("active STATUS artifact does not match pipeline")
                if active["research_path"] != self.status.get("research-path"):
                    self.error("active STATUS artifact does not match research path")
                cursor = str(self.status.get("stage", ""))
                if state == "awaiting-review":
                    allowed_parent_stages = {"verification"}
                else:
                    cursor_targets = {
                        "propose": "proposal",
                        "research": "research",
                        "evaluate": "evaluation",
                        "build": "build",
                        "verify": "verification",
                    }
                    target_stage = cursor_targets.get(cursor, "")
                    allowed_parent_stages = PARENT_STAGES.get(target_stage, set())
                if active["stage"] not in allowed_parent_stages:
                    self.error("active STATUS artifact does not match cursor stage")

    def validate_gold_targets(self):
        gold = self.read_ascii(self.root / "forge-index" / "gold-queries.yaml")
        config = self.read_ascii(self.root / "forge-index" / "config.yaml")
        targets = re.findall(r'^\s*gold_file:\s*"([^"]+)"', gold, re.MULTILINE)
        exclude_block = config.split("exclude_dirs:", 1)[-1].split(
            "exclude_patterns:", 1
        )[0]
        excluded_dirs = set(re.findall(r'^\s+-\s+"([^"]+)"', exclude_block, re.MULTILINE))
        if not targets:
            self.error("forge-index gold set is empty")
        for target in targets:
            if not (self.root / target).is_file():
                self.error(f"forge-index gold target missing: {target}")
            if target.split("/", 1)[0] in excluded_dirs:
                self.error(f"forge-index gold target is excluded: {target}")

    def run(self):
        self.validate_layout()
        self.validate_ascii_and_symlinks()
        self.validate_control_files()
        self.validate_skills()
        self.validate_logs()
        self.validate_artifacts()
        self.validate_gold_targets()
        return self.errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)

    contract = Contract(args.root)
    errors = contract.run()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FORGE CONTRACT HALT: {len(errors)} error(s)")
        return 1

    print(
        "FORGE CONTRACT PASS: layout, state, skills, logs, artifacts, "
        "scope, and index targets agree"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
