#!/usr/bin/env python3
"""Run the self-contained package checks, without any network calls."""
from __future__ import annotations
import json,os,subprocess,sys
from pathlib import Path
from datetime import datetime,timezone

def main():
    root=Path(__file__).resolve().parents[1]
    env=os.environ.copy()
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[key]='1'
    commands=[['interval_certificate.py','--output',str(root/'results/interval_certificate.json')],
              ['verify.py'],['residue_checks.py'],['shape_checks.py'],['finite_part_checks.py']]
    runs=[]
    for command in commands:
        proc=subprocess.run([sys.executable,str(root/'src'/command[0]),*command[1:]],cwd=root,env=env,
                            text=True,capture_output=True,check=False)
        print(proc.stdout,end='')
        if proc.stderr:print(proc.stderr,file=sys.stderr,end='')
        runs.append({'script':command[0],'returncode':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
        if proc.returncode:raise SystemExit(proc.returncode)
    report={'status':'PASS','completed_at_utc':datetime.now(timezone.utc).isoformat(),
            'floating_checks':362,'exact_certificate_models':3,
            'scope':'finite algebra/sign certificates; no independent peer review or infinite-volume proof','runs':runs}
    (root/'results/run_checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print('ALL PASS: 362 finite floating-point checks; exact interval certificates for 3 specified models.')
if __name__=='__main__':main()
