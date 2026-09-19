#!/usr/bin/env python3
"""Optional semantic manuscript/input audit, not a mathematical acceptance gate.
Compares parsed integer rows, not hashes or file identities. The mathematical
certificates remain the source-defined inequalities described in RESULT.md.
"""
from __future__ import annotations
from pathlib import Path
import argparse,json,re

def text_block(section:str)->str:
    match=re.search(r'```text\n(.*?)\n```',section,re.S)
    if match is None:raise ValueError('Missing readable exact-input block')
    return match.group(1)

def int_rows(text:str)->list[list[int]]:
    return [list(map(int,line.split())) for line in text.splitlines()
            if line.strip() and not line.startswith('#')]

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args();root=args.root;cert=root/'certificates'
    manuscript=(root/'RESULT.md').read_text()
    a=manuscript.split('## Appendix A.')[1].split('## Appendix B.')[0]
    rows=int_rows(text_block(a))
    caps=int_rows((cert/'guard_caps_integer.txt').read_text())
    t2=list(map(int,(cert/'far_tau_integer.txt').read_text().split()))
    t3=list(map(int,(cert/'quad_tau3_integer.txt').read_text().split()))
    assert len(caps)==len(t2)==len(t3)==256
    assert rows==[[z,*caps[z],t2[z],t3[z]] for z in range(256)]
    b=manuscript.split('## Appendix B.')[1].split('## Appendix C.')[0]
    assert list(map(int,text_block(b).split()))==list(map(int,(cert/'alpha60.txt').read_text().split()))
    c=manuscript.split('## Appendix C.')[1]
    coefficients=int_rows(text_block(c))
    assert coefficients==int_rows((cert/'quad_payment_coefficients_bivariate.txt').read_text())
    assert len(coefficients)==45
    candidate=list(map(int,(root/'diagnostics/quad_tau3_candidate_integer.txt').read_text().split()))
    repairs=[[z,candidate[z]-t3[z]] for z in range(256) if candidate[z]!=t3[z]]
    assert repairs==[[99,20],[100,20],[152,20]]
    report={'status':'PROVED exact document/input bookkeeping','witness_rows':256,
            'coefficient_rows':45,'alpha_bracket':'exact three integer lines',
            'candidate_repairs':repairs,
            'scope':'Optional comparison of parsed exact values, not a hash, file-identity, manifest, or mathematical acceptance gate'}
    dest=root/'evidence/document_input_check.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
if __name__=='__main__':main()
