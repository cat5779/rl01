#!/usr/bin/env python3
"""Replay exact certificates into a fresh output directory.

Frozen evidence is never overwritten. JSON is parsed structurally, so line-ending
or key-order differences are irrelevant.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def compare_exact_constants(frozen: dict, replay: dict) -> None:
    for key in ("certificate_type", "parameters", "checks", "exact", "outward_decimal_intervals"):
        if frozen[key] != replay[key]:
            raise AssertionError(f"exact-constant certificate field differs: {key}")


def compare_finite_exact(frozen: dict, replay: dict) -> None:
    # Decimal logarithms are diagnostics and may differ in terminal digits across
    # Python/libmpdec versions. Only exact algebraic fields are certification.
    for key in ("certificate_type", "classification", "example", "exact_checks", "exact_ranges"):
        if frozen[key] != replay[key]:
            raise AssertionError(f"finite exact certificate field differs: {key}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    out = Path(args.output_dir)
    if not out.is_absolute():
        out = (root / out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    run([sys.executable, "scripts/verify_manifest.py", "--root", str(root)], root)

    exact_out = out / "high_contrast_constants.replay.json"
    finite_out = out / "finite_coupled_check.replay.json"
    run([sys.executable, "scripts/exact_constants.py", "--output", str(exact_out)], root)
    run([sys.executable, "scripts/finite_dpp_check.py", "--output", str(finite_out)], root)

    exact_frozen = load(root / "evidence/certificates/high_contrast_constants.json")
    finite_frozen = load(root / "evidence/certificates/finite_coupled_check.json")
    compare_exact_constants(exact_frozen, load(exact_out))
    compare_finite_exact(finite_frozen, load(finite_out))

    report = {
        "status": "PASS",
        "manifest_files_verified": len(load(root / "manifest.json")["files"]),
        "exact_constant_fields_match": True,
        "finite_exact_fields_match": True,
        "floating_q_grid_used_as_proof": False,
    }
    (out / "replay_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
