#!/usr/bin/env python3
"""Exact certificate replay, with hash-checked resume for short tool sessions.

Standard library only. No output is called a completed pass unless its child
process returned zero; interrupted jobs without receipts run again.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

NAMES = ['rational', 'fourier7', 'common_frame', 'rational_optimized', 'fourier7_optimized']


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', default='reproduced')
    parser.add_argument('--logs', default=None)
    parser.add_argument('--only', nargs='+', choices=NAMES, default=None)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    out = Path(args.out).resolve()
    logs = Path(args.logs).resolve() if args.logs else out/'logs'
    for directory in [out, logs, out/'job_receipts']:
        directory.mkdir(parents=True, exist_ok=True)
    jobs = [
        ('rational', [], 'exact_certificate.py', ['--out', str(out/'rational')]),
        ('fourier7', [], 'exact_fourier7.py', ['--out', str(out/'fourier7')]),
        ('common_frame', [], 'exact_common_frame.py', ['--out', str(out/'common_exact.json')]),
        ('rational_optimized', ['-O'], 'exact_certificate.py',
         ['--terms', '28', '--out', str(out/'rational_optimized')]),
        ('fourier7_optimized', ['-O'], 'exact_fourier7.py',
         ['--terms', '28', '--bits', '160', '--out', str(out/'fourier7_optimized')]),
    ]
    sources = {name: digest(root/'code'/name) for name in
               ['exact_certificate.py', 'exact_fourier7.py', 'exact_common_frame.py']}
    started = time.monotonic()
    record = {
        'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'python': sys.version, 'platform': platform.platform(),
        'scope': 'same-author exact computational replay, not independent audit',
        'selected_names': args.only or NAMES,
        'resume_requested': args.resume,
        'executed_in_this_invocation': [], 'reused_completed_jobs': [],
        'all_checks_passed': False,
    }

    def completed(name: str) -> dict | None:
        path = out/'job_receipts'/f'{name}.json'
        if not path.exists():
            return None
        info = json.loads(path.read_text())
        if info.get('returncode') != 0 or info.get('source_sha256') != sources:
            return None
        for filename, checksum in info['evidence_sha256'].items():
            p = Path(filename)
            if not p.is_file() or digest(p) != checksum:
                return None
        return info

    status = 0
    for name, flags, script, options in jobs:
        if args.only and name not in args.only:
            continue
        old = completed(name) if args.resume else None
        if old is not None:
            record['reused_completed_jobs'].append(name)
            print('PASS verified prior completion', name, flush=True)
            continue
        command = [sys.executable, *flags, str(root/'code'/script), *options]
        t = time.monotonic()
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        process = subprocess.run(command, cwd=root, text=True, env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = logs/f'{name}.log'
        log.write_text(process.stdout, encoding='utf-8')
        item = {'name': name, 'command': command, 'returncode': process.returncode,
                'runtime_seconds': time.monotonic()-t,
                'finished_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                'source_sha256': sources, 'evidence_sha256': {str(log): digest(log)}}
        if process.returncode == 0:
            outputs = [out/'common_exact.json'] if name == 'common_frame' else [
                out/name/'certificate.json', out/name/'run_receipt.json']
            for p in outputs:
                item['evidence_sha256'][str(p)] = digest(p)
        (out/'job_receipts'/f'{name}.json').write_text(json.dumps(item, indent=2)+'\n')
        record['executed_in_this_invocation'].append(item)
        print(('PASS' if process.returncode == 0 else 'FAIL'), name, flush=True)
        if process.returncode:
            print(process.stdout, file=sys.stderr)
            status = process.returncode
            break
    available = {name: completed(name) for name in NAMES}
    record['completed_names'] = [name for name in NAMES if available[name] is not None]
    if status == 0 and len(record['completed_names']) == len(NAMES):
        rat = json.loads((out/'rational/certificate.json').read_text())
        rat_o = json.loads((out/'rational_optimized/certificate.json').read_text())
        four = json.loads((out/'fourier7/certificate.json').read_text())
        four_o = json.loads((out/'fourier7_optimized/certificate.json').read_text())
        for regular, optimized, keys in [
            (rat, rat_o, ('input_law', 'output_jets')),
            (four, four_o, ('input_law_coefficients', 'complete_output_jets_coefficients')),
        ]:
            for state in regular['states']:
                for key in keys:
                    if regular['states'][state][key] != optimized['states'][state][key]:
                        raise RuntimeError(f'exact replay mismatch in {state}/{key}')
        record['all_checks_passed'] = True
        record['same_exact_laws_and_jets_at_both_precisions'] = True
        print('ALL FIVE JOBS VERIFIED; exact laws and jets agree across precision settings', flush=True)
    record['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    record['invocation_runtime_seconds'] = time.monotonic()-started
    (out/'replay_receipt.json').write_text(json.dumps(record, indent=2)+'\n')
    history = out/'replay_invocations.jsonl'
    with history.open('a') as f:
        f.write(json.dumps(record)+'\n')
    return status


if __name__ == '__main__':
    raise SystemExit(main())
