"""Rigorous interval values for the new S64 finite-parameter KL budget."""
from certify_s64 import IV,ONE,ZERO,half_sine_kernel,log_interval,PREC,SCALE,ceildiv
from fractions import Fraction
import json

def exp_positive(x,terms=64):
    """x interval in [0,1/2], positive Taylor sum with geometric tail."""
    assert 0<=x.lo<=x.hi<=SCALE//2
    ans=ONE; term=ONE
    for k in range(1,terms):
        term=term*x/k; ans=ans+term
    # next term, and subsequent ratio <= x/(terms+1)
    nextterm=term*x/terms
    tail=nextterm/(ONE-x/(terms+1))
    return ans+IV(0,tail.hi)

def logdet_pd(A):
    """No-pivot exact-interval LDL elimination; every pivot certified positive."""
    A=[row[:] for row in A]; ans=ZERO
    for i in range(len(A)):
        d=A[i][i]
        assert d.lo>0
        ans=ans+log_interval(d)
        inv=d.reciprocal()
        for j in range(i+1,len(A)):
            for k in range(j,len(A)):
                v=A[j][k]-A[j][i]*inv*A[i][k]
                A[j][k]=A[k][j]=v
    return ans

def Lambda(n,h=Fraction(1,50),a=Fraction(1,40)):
    e=exp_positive(IV.rat(h.numerator,h.denominator)); t=e-ONE
    K=half_sine_kernel(n,a)
    return logdet_pd([[t*K[i][j]+(ONE if i==j else ZERO) for j in range(n)] for i in range(n)])

if __name__=='__main__':
    h=Fraction(1,50); e=exp_positive(IV.rat(h.numerator,h.denominator));t=e-ONE
    lim=(log_interval(ONE+t*IV.rat(1,40))+log_interval(ONE+t*IV.rat(39,40)))/2
    vals={n:Lambda(n)/n for n in (1,2,4,8,16,32,64)}
    out={'h':'1/50','reference_a':'1/40','Lambda_rate':lim.decimal(),
         'Lambda_per_site':{str(n):v.decimal() for n,v in vals.items()},
         'credit_from_1_to_n':{str(n):(vals[1]-v).decimal() for n,v in vals.items()},
         'credit_from_n_to_infinity':{str(n):(v-lim).decimal() for n,v in vals.items()},
         'precision_bits':PREC}
    print(json.dumps(out,indent=2))
