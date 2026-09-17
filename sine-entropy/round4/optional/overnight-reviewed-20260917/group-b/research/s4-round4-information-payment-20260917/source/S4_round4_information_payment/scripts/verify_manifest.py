#!/usr/bin/env python3
"""Verify shipped SHA-256 manifest. Runtime output/ and Python caches are excluded."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    errors=[]
    for entry in manifest['files']:
        p=ROOT/entry['path']
        if not p.is_file():errors.append(f"missing {entry['path']}");continue
        raw=p.read_bytes()
        if len(raw)!=entry['bytes'] or hashlib.sha256(raw).hexdigest()!=entry['sha256']:
            errors.append(f"hash/size mismatch {entry['path']}")
    expected={entry['path'] for entry in manifest['files']}
    extra=[]
    for p in ROOT.rglob('*'):
        if not p.is_file():continue
        rel=p.relative_to(ROOT)
        if rel.as_posix()=='manifest.json' or 'output' in rel.parts or '__pycache__' in rel.parts:continue
        if rel.as_posix() not in expected:extra.append(rel.as_posix())
    errors.extend('unmanifested '+x for x in extra)
    if errors:raise SystemExit('\n'.join(errors))
    print(f"PASS SHA-256 manifest: {len(expected)} files")
if __name__=='__main__':main()
