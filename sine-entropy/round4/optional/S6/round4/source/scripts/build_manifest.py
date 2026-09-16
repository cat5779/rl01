#!/usr/bin/env python3
"""Build the nonrecursive SHA-256 package manifest."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    excluded_names = {"manifest.json", "MANIFEST.sha256"}
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith("output/") or path.name in excluded_names or "__pycache__" in path.parts:
            continue
        mode = path.stat().st_mode & 0o777
        files.append({
            "path": rel,
            "bytes": path.stat().st_size,
            "sha256": digest(path),
            "mode_octal": f"{mode:04o}",
            "read_only": (mode & 0o222) == 0,
        })
    payload = {
        "format": "S6-round4-sha256-manifest-v1",
        "hash_algorithm": "sha256",
        "excluded": ["manifest.json", "MANIFEST.sha256", "output/**", "**/__pycache__/**"],
        "files": files,
    }
    (root / "manifest.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"wrote manifest for {len(files)} files")


if __name__ == "__main__":
    main()
