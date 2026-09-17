#!/usr/bin/env python3
"""Replay all round-two evidence without mutating frozen files.

Comparisons are performed on parsed JSON, so LF/CRLF differences are irrelevant.
"""
from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any

ROUND2 = Path(__file__).resolve().parents[1]
ROOT = ROUND2.parent
FROZEN = ROUND2 / "evidence" / "frozen"
REPLAY = ROUND2 / "evidence" / "replay" / "current"
PRIOR_ZIP = ROOT / "round1_unreviewed" / "S13_research_result.zip"
PRIOR_SHA256 = "6fa53dfda43d7c40e3d6c488e12914f59709ea0de2d321eded2eda6fe6622f94"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def compare(expected: Any, actual: Any, path: str = "$") -> list[str]:
    errors: list[str] = []
    if isinstance(expected, bool) or expected is None or isinstance(expected, str):
        if expected != actual:
            errors.append(f"{path}: expected {expected!r}, got {actual!r}")
    elif isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        if not math.isclose(float(expected), float(actual), rel_tol=2e-10, abs_tol=2e-12):
            errors.append(f"{path}: expected {expected!r}, got {actual!r}")
    elif isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            errors.append(f"{path}: list length {len(expected)} != {len(actual)}")
        for i, (left, right) in enumerate(zip(expected, actual)):
            errors.extend(compare(left, right, f"{path}[{i}]"))
    elif isinstance(expected, dict) and isinstance(actual, dict):
        if set(expected) != set(actual):
            errors.append(
                f"{path}: key mismatch expected={sorted(expected)} actual={sorted(actual)}"
            )
        for key in sorted(set(expected) & set(actual)):
            errors.extend(compare(expected[key], actual[key], f"{path}.{key}"))
    else:
        errors.append(
            f"{path}: type/value mismatch expected={type(expected).__name__}:{expected!r} "
            f"actual={type(actual).__name__}:{actual!r}"
        )
    return errors


def run_script(script: str, output: Path) -> None:
    subprocess.run(
        [sys.executable, str(ROUND2 / "scripts" / script), "--output", str(output)],
        check=True,
        cwd=ROOT,
    )


def main() -> int:
    REPLAY.mkdir(parents=True, exist_ok=True)
    generated = {
        "symbolic_checks.json": "symbolic_checks.py",
        "defect_asymptotics.json": "defect_asymptotics.py",
    }
    report: dict[str, Any] = {
        "prior_zip": {},
        "files": {},
        "pass": True,
    }

    prior_hash = sha256(PRIOR_ZIP)
    report["prior_zip"] = {
        "path": str(PRIOR_ZIP.relative_to(ROOT)),
        "expected_sha256": PRIOR_SHA256,
        "actual_sha256": prior_hash,
        "pass": prior_hash == PRIOR_SHA256,
    }
    if prior_hash != PRIOR_SHA256:
        report["pass"] = False

    for name, script in generated.items():
        output = REPLAY / name
        run_script(script, output)
        expected = json.loads((FROZEN / name).read_text(encoding="utf-8"))
        actual = json.loads(output.read_text(encoding="utf-8"))
        errors = compare(expected, actual)
        report["files"][name] = {
            "script": script,
            "frozen_sha256": sha256(FROZEN / name),
            "replay_sha256": sha256(output),
            "semantic_errors": errors,
            "pass": not errors,
        }
        if errors:
            report["pass"] = False

    report_path = REPLAY / "replay_report.json"
    report_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
