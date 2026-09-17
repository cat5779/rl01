#!/usr/bin/env python3
"""Replay all S13 round-three deterministic checks.

The analytic theorem is in proof.md. This script verifies that the symbolic,
finite-enumeration, and floating diagnostic receipts regenerate byte-for-byte,
and performs simple structural checks on the proof source.
"""
from __future__ import annotations

import collections
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / "evidence" / "frozen"

JOBS = [
    ("symbolic_checks.py", "symbolic_checks.json"),
    ("clock_curvature_receipt.py", "clock_curvature_receipt.json"),
    ("finite_slice_check.py", "finite_slice_check.json"),
    ("central_band_receipt.py", "central_band_receipt.json"),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="s13-round3-replay-") as td:
        outdir = Path(td)
        for script, receipt in JOBS:
            generated = outdir / receipt
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / script), "--output", str(generated)],
                check=True,
            )
            frozen = FROZEN / receipt
            if generated.read_bytes() != frozen.read_bytes():
                print(f"FAIL byte mismatch: {receipt}", file=sys.stderr)
                print(f" generated {sha256(generated)}", file=sys.stderr)
                print(f" frozen    {sha256(frozen)}", file=sys.stderr)
                return 1
            print(f"PASS byte-identical {receipt} {sha256(frozen)}")

    proof = (ROOT / "proof.md").read_text()
    tags = re.findall(r"\\tag\{([^}]+)\}", proof)
    duplicate = [tag for tag, n in collections.Counter(tags).items() if n > 1]
    refs = set(re.findall(r"\((\d+\.\d+[a-z]?)\)", proof))
    missing = sorted(refs - set(tags))
    required = [
        "\\widehat K_n''(a_*)=\\mathcal W_n(c)+\\mathcal C_n(c)",
        "\\liminf_{n\\to\\infty}{\\mathcal C_n(c)\\over n}",
        "{2\\over1-c^2}D_{\\rm pair}(c)",
        "The moving-count term (2.17) is not assigned a",
    ]
    absent = [x for x in required if x not in proof]
    if duplicate or missing or absent:
        print(f"FAIL proof structure duplicate={duplicate} missing={missing} absent={absent}", file=sys.stderr)
        return 1
    print(f"PASS proof structure: {len(tags)} unique equation tags")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
