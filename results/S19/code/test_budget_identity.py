#!/usr/bin/env python3
"""Exact author tests of the four actual completion weights in W.

This reconstructs the posterior directly from the full two-bit latent law,
rather than using the determinant inverse used by the main derivation.
No logarithm, random sampling, or floating sign test is used.
"""
from fractions import Fraction as F
import unittest


def cases():
    for a in [F(1,50),F(21,1000),F(1,40),F(29,1000),F(3,100)]:
        c=F(19,20)
        for x in [F(1,10),F(1,3),F(1,2),F(4,5)]:
            for y in [F(1,5),F(2,5),F(1,2),F(9,10)]:
                for scale in [F(1,7),F(2,3)]:
                    z=min(x*y,(1-x)*(1-y))*scale
                    yield a,c,x,y,z


def quantities(a,c,x,y,z):
    q=a+c*x;r=a+c*y;s=c*c*z
    p=[(1-q)*(1-r)-s,q*(1-r)+s,(1-q)*r+s,q*r-s]
    beta=[(1-a)*(1-a-c),a*(a+c)]
    ri=[x+c*z/(1-r),x-c*z/r]
    rj=[y+c*z/(1-q),y-c*z/q]
    return q,r,s,p,beta,ri,rj


class BudgetIdentityTests(unittest.TestCase):
    def test_complete_actual_bayes_weights(self):
        for a,c,x,y,z in cases():
            q,r,s,p,beta,ri,rj=quantities(a,c,x,y,z)
            latent=[(1-x)*(1-y)-z,x*(1-y)+z,(1-x)*y+z,x*y-z]
            W=F(0);direct=F(0)
            for u in (0,1):
                for v in (0,1):
                    mass=[]
                    for xi in (0,1):
                        for xj in (0,1):
                            ti=a+c*xi;tj=a+c*xj
                            elli=ti if u else 1-ti
                            ellj=tj if v else 1-tj
                            mass.append((xi,xj,latent[xi+2*xj]*elli*ellj))
                    total=sum(w for _,_,w in mass)
                    self.assertEqual(total,p[u+2*v])
                    px=sum(w*xi for xi,xj,w in mass)/total
                    py=sum(w*xj for xi,xj,w in mass)/total
                    pxy=sum(w*xi*xj for xi,xj,w in mass)/total
                    energy=px*py-pxy
                    self.assertEqual(energy,z*beta[u]*beta[v]/total**2)
                    direct+=total*energy*(1/(4*beta[u]*ri[v]*(1-ri[v]))
                                       +1/(4*beta[v]*rj[u]*(1-rj[u])))
                    W+=z/total*(beta[v]/(4*ri[v]*(1-ri[v]))
                               +beta[u]/(4*rj[u]*(1-rj[u])))
            self.assertEqual(direct,W)
    def test_four_row_rational_formula(self):
        for a,c,x,y,z in cases():
            q,r,s,p,beta,ri,rj=quantities(a,c,x,y,z)
            W=sum((z/p[u+2*v]*(beta[v]/(4*ri[v]*(1-ri[v]))
                               +beta[u]/(4*rj[u]*(1-rj[u])))
                   for u in (0,1) for v in (0,1)),F(0))
            # Rows with the target bit varying, the other bit fixed.
            rows=[(p[0],p[1],beta[0]),(p[2],p[3],beta[1]),
                  (p[0],p[2],beta[0]),(p[1],p[3],beta[1])]
            four_rows=F(0)
            for P0,P1,beta_other in rows:
                S=P0+P1;N=P1-a*S;M=(a+c)*S-P1
                self.assertGreater(N,0);self.assertGreater(M,0)
                four_rows+=s*beta_other*S**3/(4*P0*P1*N*M)
            self.assertEqual(W,four_rows)


if __name__=='__main__':unittest.main(verbosity=2)
