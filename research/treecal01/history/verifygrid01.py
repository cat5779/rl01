"""Independent ordered-pair implementation of the finite integer certificate."""
from pathlib import Path
import json,hashlib,time
root=Path(__file__).parent
c=json.loads((root/'grid256.json').read_text(encoding='utf-8'))
M=c['grid'];D=c['probability_denominator'];H=c['function_denominator']
w=[0]*(M+1);w[M]=D
t=time.time()
for _ in range(c['iterations']):
    mass=[0]*(M+1)
    for i in range(M+1):
        if not w[i]:continue
        for j in range(M+1):
            if not w[j]:continue
            z=w[i]*w[j]
            for a,b in [(0,0),(0,M),(M,0),(M,M)]:
                x,y=i+a,j+b
                k=0 if x+y==0 else -(-(x*y)//(x+y))
                mass[k]+=z
    # CDF-floor discretization, reconstructed through differences.
    prefix=[];total=0
    for z in mass:total+=z;prefix.append(total//(4*D))
    assert total==4*D*D and prefix[-1]==D
    w=[prefix[0],*(prefix[i]-prefix[i-1] for i in range(1,M+1))]
assert w==c['upper_resistance_pmf_numerators']
assert sum(w)==D and all(z>=0 for z in w)
N=0
support=[i for i in range(M+1) if w[i]]
for i in support:
    for j in support:
        z=w[i]*w[j]
        for k in support:
            den0=(M+i)*(M+j)+(2*M+i+j)*k
            den1=den0+(2*M+i+j)*M
            v=(M*M*H)//den0+(M*M*H)//den1
            N+=z*w[k]*v
den=8*D**3*H
assert N==c['pair_lower_numerator'] and den==c['pair_lower_denominator']
assert 12*N>den
assert 2000*N>167*den
result={'status':'PROVED','scope':'finite integer certificate only, not independent review of the infinite-network bridge','probability_pmf_matches':True,'pair_sum_matches':True,'lower_bound_exceeds_167_over_2000':True,'margin_over_one_twelfth':12*N-den,'margin_over_167_over_2000':2000*N-167*den,'grid256_sha256':hashlib.sha256((root/'grid256.json').read_bytes()).hexdigest(),'elapsed_seconds':time.time()-t}
(root/'verifygrid01.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result),flush=True)
