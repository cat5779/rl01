#!/usr/bin/env python3
"""Rebuild exact evidence into a fresh directory; compare parsed JSON, not newlines."""
from __future__ import annotations
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from math_core import require, safe_output
ROOT=Path(__file__).resolve().parents[1]

def load(p):
    with p.open('r',encoding='utf-8') as f:return json.load(f)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-dir',type=Path,default=ROOT/'output'/'replay')
    ap.add_argument('--with-floating',action='store_true',help='Also run optional NumPy diagnostics; never exact-compare floating output.')
    args=ap.parse_args();out=safe_output(args.out_dir,ROOT)
    start=dt.datetime.now(dt.timezone.utc).isoformat();clock=time.perf_counter()
    runs=[]
    for script,filename in [('exact_check.py','exact_certificate.json'),
                            ('moving_reference_check.py','moving_reference_certificate.json')]:
        cmd=[sys.executable,str(ROOT/'scripts'/script),'--out-dir',str(out)]
        proc=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',check=False)
        (out/(script+'.stdout.log')).write_text(proc.stdout,encoding='utf-8',newline='\n')
        (out/(script+'.stderr.log')).write_text(proc.stderr,encoding='utf-8',newline='\n')
        require(proc.returncode==0,f'{script} returned {proc.returncode}; see output logs')
        actual=load(out/filename);frozen=load(ROOT/'evidence'/filename)
        require(actual==frozen,f'Parsed JSON mathematical mismatch in {filename}')
        # CRLF is intentionally introduced only in the new output directory.
        text=(ROOT/'evidence'/filename).read_text(encoding='utf-8')
        crlf=out/(filename+'.crlf.json')
        crlf.write_bytes(text.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))
        require(load(crlf)==frozen,f'CRLF portability comparison failed for {filename}')
        runs.append(dict(script=script,parsed_json_equal=True,LF_CRLF_equivalent=True))
        print(f'PASS {script}: exact parsed JSON and LF/CRLF compatibility',flush=True)
    # Test that a requested evidence output is rejected before any write.
    guard=subprocess.run([sys.executable,str(ROOT/'scripts'/'exact_check.py'),'--quick',
                          '--out-dir',str(ROOT/'evidence'/'forbidden_output')],
                         capture_output=True,text=True,encoding='utf-8',check=False)
    require(guard.returncode!=0 and 'Refusing to write in frozen evidence' in guard.stderr,
            'Frozen-evidence output guard failed')
    require(not (ROOT/'evidence'/'forbidden_output').exists(),'Guard created an evidence directory')
    if args.with_floating:
        env=dict(os.environ);env['OPENBLAS_NUM_THREADS']='1'
        cmd=[sys.executable,str(ROOT/'scripts'/'floating_checks.py'),'--out-dir',str(out/'floating')]
        proc=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,check=False)
        (out/'floating.stdout.log').write_text(proc.stdout,encoding='utf-8',newline='\n')
        (out/'floating.stderr.log').write_text(proc.stderr,encoding='utf-8',newline='\n')
        require(proc.returncode==0,'Optional floating run failed; see its output log')
        runs.append(dict(script='floating_checks.py',completed=True,assurance='Floating diagnostic; not exact-compared.'))
    report=dict(utc_start=start,utc_end=dt.datetime.now(dt.timezone.utc).isoformat(),
                elapsed_seconds=time.perf_counter()-clock,python=sys.version,
                runs=runs,frozen_evidence_write_guard_passed=True,all_checks_passed=True,
                assurance='Self-reproduction only. It does not independently certify the analytical proof.')
    with (out/'replay_report.json').open('w',encoding='utf-8',newline='\n') as f:
        json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
    print('PASS replay, portability checks, and frozen-evidence write guard',flush=True)
if __name__=='__main__':main()
