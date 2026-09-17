#!/usr/bin/env python3
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST.sha256"

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def main() -> int:
    expected: dict[str, str] = {}
    for line in MANIFEST.read_text().splitlines():
        if not line.strip():
            continue
        sha, rel = line.split("  ", 1)
        expected[rel] = sha
    actual_files = sorted(
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and p.name != MANIFEST.name
    )
    if actual_files != sorted(expected):
        print("FAIL file set mismatch")
        print("missing from disk:", sorted(set(expected) - set(actual_files)))
        print("unlisted on disk:", sorted(set(actual_files) - set(expected)))
        return 1
    bad = []
    for rel in actual_files:
        got = digest(ROOT / rel)
        if got != expected[rel]:
            bad.append((rel, expected[rel], got))
    if bad:
        for rel, exp, got in bad:
            print(f"FAIL {rel}: expected {exp}, got {got}")
        return 1
    print(f"PASS {len(actual_files)} files match MANIFEST.sha256")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
