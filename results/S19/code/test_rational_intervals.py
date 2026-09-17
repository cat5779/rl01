#!/usr/bin/env python3
"""Exact author tests for rational arithmetic and scalar certificate coverage."""
from fractions import Fraction as F
import random
import unittest
from verify_reference_payment import I,S,pi_enclosure,log_interval,certify


def contains(i,x):return F(i.lo,S)<=x<=F(i.hi,S)

def fraction_log_bounds(x,terms=120):
    k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def bounds(u):
        z=(u-1)/(u+1)
        v=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
        return v,v+2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    a,b=bounds(x);l,h=bounds(F(2))
    return (a+k*l,b+k*h) if k>=0 else (a+k*h,b+k*l)

class RationalTests(unittest.TestCase):
    def test_arithmetic_contains_exact_values(self):
        rng=random.Random(19)
        for _ in range(200):
            x=F(rng.randint(-1000,1000),rng.randint(1,200))
            y=F(rng.randint(1,1000),rng.randint(1,200))
            self.assertTrue(contains(I.of(x)+y,x+y))
            self.assertTrue(contains(I.of(x)-y,x-y))
            self.assertTrue(contains(I.of(x)*y,x*y))
            self.assertTrue(contains(I.of(x)/y,x/y))
            self.assertTrue(contains(I.of(x).square(),x*x))
    def test_log_against_unrounded_fraction_series(self):
        for x in (F(1,100),F(1,2),F(1),F(3,2),F(2),F(7),F(250)):
            lo,hi=fraction_log_bounds(x)
            result=log_interval(I.of(x))
            self.assertLessEqual(F(result.lo,S),lo)
            self.assertGreaterEqual(F(result.hi,S),hi)
    def test_pi_known_rational_bracket(self):
        p=pi_enclosure()
        self.assertGreater(F(p.lo,S),F(3141592653589793238462643383279502,10**33))
        self.assertLess(F(p.hi,S),F(3141592653589793238462643383279503,10**33))
    def test_certificate_all_cells(self):
        x=certify()
        self.assertEqual(x['status'],'PASS')
        self.assertEqual(len(x['rows']),200)
        self.assertEqual(F(x['rows'][0]['a_lo']),F(1,50))
        self.assertEqual(F(x['rows'][-1]['a_hi']),F(3,100))
        for a,b in zip(x['rows'],x['rows'][1:]):
            self.assertEqual(F(a['a_hi']),F(b['a_lo']))
        self.assertGreater(int(x['minimum_excess_lower_dyadic'])*12,S)

if __name__=='__main__':unittest.main(verbosity=2)
