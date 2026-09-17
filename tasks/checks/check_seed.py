"""Independent finite seed checks. Python 3 standard library only.

Exact rational polynomial identities and outward-rounded rational intervals.
This certifies one six-site obstruction, not entropy-rate concavity.
"""
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path

GRID = 10**40

def floorq(x):
    return F((x.numerator * GRID) // x.denominator, GRID)

def ceilq(x):
    return -floorq(-x)

class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("reversed interval")
    def __add__(self, other):
        o = other if isinstance(other, I) else I(other)
        return I(floorq(self.lo+o.lo), ceilq(self.hi+o.hi))
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))
    def __rsub__(self, other):
        return I(other) + -self
    def __mul__(self, other):
        o = other if isinstance(other, I) else I(other)
        values = [self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(floorq(min(values)), ceilq(max(values)))
    __rmul__ = __mul__
    def inv(self):
        if self.lo <= 0 <= self.hi:
            raise ValueError("division interval contains zero")
        return I(floorq(1/self.hi),ceilq(1/self.lo))
    def __truediv__(self, other):
        return self * (other if isinstance(other,I) else I(other)).inv()
    def __rtruediv__(self, other):
        return I(other) * self.inv()
    def display(self):
        return {"lower_rational":str(self.lo),"upper_rational":str(self.hi),
                "approx_midpoint":float((self.lo+self.hi)/2)}

def log_unit(u):
    # 1 <= u <= 2; positive atanh series, with rigorous geometric tail.
    z=(I(u)-1)/(I(u)+1)
    z2=z*z
    term=z
    result=I(0)
    for j in range(32):
        result += 2*term/F(2*j+1)
        term=term*z2
    tail=2*term/F(65)/(1-z2)
    return I(result.lo,ceilq(result.hi+tail.hi))

LOG2=log_unit(F(2))

def log_point(x):
    if x <= 0:
        raise ValueError("log nonpositive")
    k=0
    while x < 1:
        x*=2
        k-=1
    while x >= 2:
        x/=2
        k+=1
    return log_unit(x)+k*LOG2

def log_interval(x):
    return I(log_point(x.lo).lo,log_point(x.hi).hi)

def arctan_enclosure(x, terms=32):
    s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    other=s+(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return I(min(s,other),max(s,other))

def polynomial_atoms(n):
    # At half density and midpoint K diagonal=1/2, off diagonal is
    # x*sin(pi*(i-j)/2)/(i-j), x=c/pi. Odd powers cancel exactly.
    atoms=[]
    for word in range(1<<n):
        coefficients=[F(0) for _ in range(n+1)]
        for perm in permutations(range(n)):
            inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
            coefficient=F((-1)**(inversions+n-word.bit_count()))
            degree=0
            for i,j in enumerate(perm):
                if i==j:
                    coefficient*= F(1 if (word>>i)&1 else -1,2)
                elif (i-j)%2==0:
                    coefficient=F(0)
                    break
                else:
                    coefficient*=F(1 if (i-j)%4==1 else -1,i-j)
                    degree+=1
            coefficients[degree]+=coefficient
        if any(coefficients[1::2]):
            raise AssertionError("unexpected odd power")
        atoms.append(coefficients[::2])
    summed=[sum(row[j] for row in atoms) for j in range(n//2+1)]
    if summed != [F(1)]+[F(0)]*(n//2):
        raise AssertionError("normalization polynomial")
    return atoms

def evaluate(coeffs,t):
    out=I(0)
    for c in reversed(coeffs):
        out=out*t+c
    return out

def six_site():
    n=6
    pi=16*arctan_enclosure(F(1,5))-4*arctan_enclosure(F(1,239))
    t=(I(F(19,20))/pi)*(I(F(19,20))/pi)
    coeffs=polynomial_atoms(n)
    p=[evaluate(row,t) for row in coeffs]
    if min(q.lo for q in p)<=0:
        raise AssertionError("atom positivity")
    p1=[]
    p2=[]
    for y in range(1<<n):
        signs=[1 if (y>>i)&1 else -1 for i in range(n)]
        p1.append(sum((signs[i]*(p[y]+p[y^(1<<i)]) for i in range(n)),I(0)))
        p2.append(sum((2*signs[i]*signs[j]*(p[y]+p[y^(1<<i)]+p[y^(1<<j)]+p[y^(1<<i)^(1<<j)])
                       for i in range(n) for j in range(i+1,n)),I(0)))
    h2=sum((-p2[y]*log_interval(p[y])-p1[y]*p1[y]/p[y] for y in range(1<<n)),I(0))
    def pair(i,j):
        outside=[k for k in range(n) if k not in (i,j)]
        total=I(0)
        for z in range(1<<(n-2)):
            base=sum(((z>>k)&1)<<site for k,site in enumerate(outside))
            A,B,C,D=[p[base|mask] for mask in (0,1<<i,1<<j,(1<<i)|(1<<j))]
            mass=A+B+C+D
            total+=mass*log_interval(B*C/(A*D))-(B*C-A*D)*(1/A+1/B+1/C+1/D)
        return total
    witness=pair(0,5)
    diagonal=I(0)
    for i in range(n):
        for y in range(1<<n):
            if not (y>>i)&1:
                p0,p_one=p[y],p[y|(1<<i)]
                mass=p0+p_one
                diagonal-=mass*mass*mass/(p0*p_one)
    pair_h2=diagonal+2*sum((pair(i,j) for i in range(n) for j in range(i+1,n)),I(0))
    residual=h2-pair_h2
    if not (F(37,100000)<witness.lo<=witness.hi<F(39,100000)):
        raise AssertionError("pair bracket")
    if not (F(-50)<h2.lo<=h2.hi<F(-49)):
        raise AssertionError("Hessian bracket")
    if not residual.lo<=0<=residual.hi:
        raise AssertionError("Hessian identity disagreement")
    return {"fixture":"actual_sine_n6_rho_half_c_19_over_20_a_1_over_40",
            "status":"RATIONAL_INTERVAL_CERTIFICATE",
            "pair_1_6":witness.display(),"H_second":h2.display(),
            "pair_decomposition_residual":residual.display(),
            "all_atom_lower_bounds_positive":True,
            "normalization_polynomial_exact":True,
            "coefficients_in_t_c_over_pi_squared":[list(map(str,row)) for row in coeffs]}

def moving_count_check():
    # Arbitrary n=4 eigenvalues in [0,1]; no product surrogate for configurations.
    a,c=F(1,40),F(19,20)
    eigenvalues=[F(0),F(1,5),F(4,5),F(1)]
    b=[a+c*t for t in eigenvalues]
    def distribution(indices):
        out=[F(1)]
        for i in indices:
            new=[F(0)]*(len(out)+1)
            for m,v in enumerate(out):
                new[m]+=v*(1-b[i]);new[m+1]+=v*b[i]
            out=new
        return out
    n=len(b)
    pi=distribution(range(n))
    pi1=[F(0)]*(n+1);pi2=[F(0)]*(n+1)
    # Differentiate factors of the probability generating polynomial directly.
    for i in range(n):
        for m,v in enumerate(distribution([j for j in range(n) if j!=i])):
            pi1[m]-=v;pi1[m+1]+=v
        for j in range(n):
            if i==j:continue
            for m,v in enumerate(distribution([k for k in range(n) if k not in (i,j)])):
                pi2[m]+=v;pi2[m+1]-=2*v;pi2[m+2]+=v
    # A moving layer test function with nonzero first and second derivatives.
    f=[F(m*m)+a*m**3+a*a*(m+1) for m in range(n+1)]
    f1=[F(m**3)+2*a*(m+1) for m in range(n+1)]
    f2=[F(2*(m+1)) for m in range(n+1)]
    direct=sum(pi2[m]*f[m]+2*pi1[m]*f1[m]+pi[m]*f2[m] for m in range(n+1))
    transported=sum(pi[m]*f2[m] for m in range(n+1))
    for i in range(n):
        transported+=2*sum(v*(f1[m+1]-f1[m]) for m,v in enumerate(distribution([j for j in range(n) if j!=i])))
        for j in range(n):
            if i!=j:
                transported+=sum(v*(f[m+2]-2*f[m+1]+f[m]) for m,v in enumerate(distribution([k for k in range(n) if k not in (i,j)])))
    if direct!=transported or sum(pi1)!=0 or sum(pi2)!=0:
        raise AssertionError("moving count transport identity")
    return {"status":"EXACT_RATIONAL_IDENTITY","direct":str(direct),"transported":str(transported),
            "note":"arbitrary moving test function; does not prove a sign for spatial KL"}

if __name__=="__main__":
    report={"six_site":six_site(),"moving_count":moving_count_check(),
            "scope":"finite obstruction and interface identities only; no global concavity claim"}
    destination=Path(__file__).with_name("seed_results.json")
    destination.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"PASS","pair":report["six_site"]["pair_1_6"]["approx_midpoint"],
                      "H_second":report["six_site"]["H_second"]["approx_midpoint"],
                      "moving_count_identity":True,"output":str(destination)},indent=2))
