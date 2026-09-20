#!/usr/bin/env python3
"""High-precision arithmetic for the S78 log-det barrier interface."""
import mpmath as mp
mp.mp.dps = 80

c = mp.mpf(19) / 20
delta = mp.mpf(1) / 50
s = c**2 / mp.pi**2
A0 = mp.mpf(1) / 4 - s
S2 = c**4 / 48 - s**2
S4 = 17*c**8 / 80640 - s**4
Et2 = 4*S2
Et4 = 48*S2**2 - 32*S4

uniform_payment = 2*mp.log(1/(4*delta*(1-delta)))
base_payment = 2*mp.log(A0/(delta*(1-delta)))
second_moment_correction = Et2/(4*A0**2)
fourth_moment_correction = Et4/(32*A0**4)
payment_D1 = base_payment - second_moment_correction
payment_D2 = payment_D1 - fourth_moment_correction

kappa_s72 = c**2/(4*delta*(delta+c))
C_log = max(mp.mpf(1), mp.log(1+kappa_s72))
tau2 = 2/delta - 4
core_pair_payment = 2*C_log*tau2
old_missing_payment = mp.mpf('107488.0202261590')
old_total = core_pair_payment + old_missing_payment
new_total_D2 = core_pair_payment + payment_D2
star_lower = mp.mpf('0.26275')
interface_upper_residual = -mp.mpf(1)/50 - star_lower + new_total_D2

for name, value in [
    ('s_nearest', s),
    ('A0', A0),
    ('S2_old_weights', S2),
    ('S4_old_weights', S4),
    ('E_t2', Et2),
    ('E_t4', Et4),
    ('uniform_barrier_payment', uniform_payment),
    ('base_Jensen_payment', base_payment),
    ('second_moment_correction', second_moment_correction),
    ('fourth_moment_correction', fourth_moment_correction),
    ('D1_payment', payment_D1),
    ('D2_payment', payment_D2),
    ('core_pair_payment', core_pair_payment),
    ('new_total_D2', new_total_D2),
    ('old_total', old_total),
    ('improvement_factor', old_total/new_total_D2),
    ('benchmark_rhs_using_0.26275', interface_upper_residual),
]:
    print(f'{name} = {mp.nstr(value, 50)}')

# Basic exact-domain checks used by the logarithmic moment series.
T = c**2/4 - s
print('old_weight_sum_T =', mp.nstr(T, 50))
print('series_margin_A0_minus_T =', mp.nstr(A0-T, 50))
assert A0 > T > 0
assert Et2 > 0 and Et4 > 0
assert payment_D2 < payment_D1 < base_payment < uniform_payment
print('PASS_BARRIER_INTERFACE_ARITHMETIC')
