#!/usr/bin/env python3
"""Verify the frozen Group A integration overlay without running math checks."""
from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST.sha256"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    expected: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        checksum, rel = line.split("  ", 1)
        if rel in expected or rel == MANIFEST.name:
            raise AssertionError(f"invalid manifest entry: {rel}")
        expected[rel] = checksum

    actual = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and path != MANIFEST and "replay" not in path.relative_to(ROOT).parts
    }
    if set(expected) != actual:
        raise AssertionError(
            f"inventory mismatch: missing={sorted(set(expected)-actual)}, "
            f"extra={sorted(actual-set(expected))}"
        )
    for rel, checksum in expected.items():
        if digest(ROOT / rel) != checksum:
            raise AssertionError(f"hash mismatch: {rel}")
    print(f"PASS Group A package: {len(expected)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

