"""Exact rational Bernstein certificate; no floating-point decisions."""
from fractions import Fraction as Q
from math import comb
import json
from pathlib import Path

if not __debug__:
    raise RuntimeError("Certificate checks require Python without -O or -OO.")


def upper_poly(r,terms):
    # B_r(rt)=(1-r*t^2)*sum_{k>=0} r^(2k+1)/(2k+1) * sum_{j=0}^{2k} t^j.
    p=[Q(0) for _ in range(2*terms+1)]
    for k in range(terms):
        a=r**(2*k+1)/Q(2*k+1)
        for j in range(2*k+1):p[j]+=a;p[j+2]-=r*a
    tail=r**(2*terms+1)/(1-r*r)
    p[0]+=tail
    return p,tail

def local_bernstein(p,a,b):
    n=len(p)-1;h=b-a
    power=[sum(p[k]*comb(k,j)*a**(k-j)*h**j for k in range(j,n+1)) for j in range(n+1)]
    return [sum(power[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]

def certificate(r,bound,terms=24,pieces=16):
    p,tail=upper_poly(r,terms);p=[-a for a in p];p[0]+=bound
    minima=[]
    for i in range(pieces):
        B=local_bernstein(p,Q(i,pieces),Q(i+1,pieces));minima.append(min(B))
    assert min(minima)>0,(r,bound,min(minima))
    return {'r':str(r),'bound':str(bound),'terms':terms,'pieces':pieces,'tail':str(tail),
            'minimum_Bernstein_coefficient':str(min(minima)),
            'interval_minima':[str(x) for x in minima], 'status':'EXACT_RATIONAL_PASS'}

if __name__=='__main__':
    out=[certificate(Q(3,4),Q(997,1000)),certificate(Q(361,400),Q(1587,1000),terms=80,pieces=32)]
    (Path(__file__).resolve().parents[1] / 'checks' / 'chord_envelope_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    for x in out:print(x['r'], x['bound'], x['status'], 'min coeff ~= ',float(Q(x['minimum_Bernstein_coefficient'])))