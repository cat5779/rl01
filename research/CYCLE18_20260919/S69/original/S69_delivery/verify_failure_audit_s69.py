#!/usr/bin/env python3
from fractions import Fraction as F
# Accepted S63 coefficient boxes, denominator 1e8.
raw=[
(1776012226,1776012227),(-82943302,-82943301),(-14608797,-14608796),
(-290978,-290977),(1734,1735),(-1,0),(-1,0),(0,1),(0,1),(-1,0)]

def upper_payment(a):
    t=200*a-5
    total=F(0)
    for k,(lo,hi) in enumerate(raw):
        z=t**k
        total += F(hi if z>=0 else lo,10**8)*z
    return total+F(1,10**6)

def burden(a):
    c=F(19,20)
    C=F(261,200)+F(51,10)*a
    d=F(2,3)/(a*(1-a))+F(1,3)/((a+c)*(1-a-c))
    return (C-1)*d
for a,name in [(F(1,50),'0.02'),(F(13,500),'0.026')]:
    gap=upper_payment(a)-burden(a)
    assert gap<0
    print(f'S63 FIXED WITNESS FAIL a={name} upper_gap {gap} ~ {float(gap):.18g}')
