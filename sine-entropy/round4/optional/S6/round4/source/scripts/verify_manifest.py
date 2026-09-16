#!/usr/bin/env python3
"""Verify the package hash manifest without changing package evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=None, help="package root; defaults to script parent parent")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    manifest_path = root / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    failures: list[str] = []
    for item in data["files"]:
        rel = item["path"]
        path = root / rel
        if not path.is_file():
            failures.append(f"missing: {rel}")
            continue
        actual_size = path.stat().st_size
        actual_hash = sha256(path)
        if actual_size != item["bytes"]:
            failures.append(f"size mismatch: {rel}: {actual_size} != {item['bytes']}")
        if actual_hash != item["sha256"]:
            failures.append(f"sha256 mismatch: {rel}: {actual_hash} != {item['sha256']}")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"manifest OK: {len(data['files'])} files")


if __name__ == "__main__":
    main()
