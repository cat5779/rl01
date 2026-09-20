#!/usr/bin/env python3
import mpmath as mp
mp.mp.dps = 50

delta = mp.mpf(1) / 50
c = mp.mpf(19) / 20
kappa_pair = (1 - 2*delta)**2 / (4*delta*(1-delta))
theta_pair = (1 - 2*delta)**2
Aplus = 1 + kappa_pair + 2*max(kappa_pair - 1, 0)
Mpair = 2*(Aplus + 1 + 3*theta_pair) / delta**2
matrix_cap = Mpair / 4

kappa_s72 = c**2 / (4*delta*(delta+c))
C_log = max(mp.mpf(1), mp.log(1+kappa_s72))
tau2 = 2/delta - 4
core_pair_payment = 2*C_log*tau2
new_residual = matrix_cap + core_pair_payment

print('kappa_pair =', mp.nstr(kappa_pair, 30))
print('theta_pair =', mp.nstr(theta_pair, 30))
print('M_pair      =', mp.nstr(Mpair, 30))
print('M_pair/4    =', mp.nstr(matrix_cap, 30))
print('2*C_log*tauhat(2) =', mp.nstr(core_pair_payment, 30))
print('new_asymptotic_residual =', mp.nstr(new_residual, 30))
print('PASS_INTERFACE_ARITHMETIC')
