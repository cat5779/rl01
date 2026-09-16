#!/usr/bin/env python3
"""Exact S8 round-two regressions, not an all-parameter proof.

Standard library only; all atom jets and log/exp enclosures are rational.
Grouped fixtures preserve complete atoms with multiplicities. No floats,
network, random search, subprocesses or assertion-dependent checks.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json

BITS, TERMS = 192, 64
SCALE = 1 << BITS


def require(condition, message):
    if not condition:
        raise ValueError(message)


def floor_scaled(x):
    return (x.numerator*SCALE)//x.denominator


def enclose(x):
    return F(floor_scaled(x), SCALE), F(-floor_scaled(-x), SCALE)


def add(x, y):
    return enclose(x[0]+y[0])[0], enclose(x[1]+y[1])[1]


def scale(x, a):
    if a < 0:
        return scale((-x[1], -x[0]), -a)
    return enclose(a*x[0])[0], enclose(a*x[1])[1]


def mul(x, y):
    terms = [u*v for u in x for v in y]
    return enclose(min(terms))[0], enclose(max(terms))[1]


def log_mantissa(m):
    require(1 <= m <= 2, 'log mantissa outside [1,2]')
    z = enclose((m-1)/(m+1))
    z2, power, result = mul(z, z), z, (F(0), F(0))
    for j in range(TERMS):
        result = add(result, scale(power, F(2, 2*j+1)))
        power = mul(power, z2)
    upper_z = F(17, 50)
    require(z[1] < upper_z, 'atanh remainder bound invalid')
    tail = 2*upper_z**(2*TERMS+1)/((2*TERMS+1)*(1-upper_z**2))
    return result[0], enclose(result[1]+tail)[1]


LOG2 = log_mantissa(F(2))


@lru_cache(maxsize=None)
def log_interval(q):
    require(q > 0, 'log of nonpositive atom')
    e = q.numerator.bit_length()-q.denominator.bit_length()
    m = q/(F(2)**e)
    if m < 1:
        e, m = e-1, 2*m
    if m >= 2:
        e, m = e+1, m/2
    require(1 <= m < 2, 'range reduction failed')
    return add(log_mantissa(m), scale(LOG2, F(e)))


def decimal_interval(interval, digits=12):
    den = 10**digits
    lo, hi = interval
    return {'lower_numerator': (lo.numerator*den)//lo.denominator,
            'upper_numerator': -((-hi.numerator*den)//hi.denominator), 'denominator': den}


def entropy(rows, derivative=0):
    out = (F(0), F(0))
    for multiplicity, p, p1, p2 in rows:
        require(p > 0, 'nonpositive interior probability')
        if derivative == 0:
            term = scale(log_interval(p), -p)
        elif derivative == 2:
            term = add(scale(log_interval(p), -p2), enclose(-p1*p1/p))
        else:
            raise ValueError('only entropy or full Hessian supported')
        out = add(out, scale(term, F(multiplicity)))
    return out


def difference(x, y):
    return add(x, (-y[1], -y[0]))


def det2(v, w):
    return v[0]*w[1]-v[1]*w[0]


def channel_jet(n, mu, a, c):
    rows = []
    for mask in range(1 << n):
        total = [F(0), F(0), F(0)]
        for (i, j), weight in mu.items():
            v, v1, v2 = F(1), F(0), F(0)
            for site in range(n):
                success = a+c*int(site in (i, j))
                f, slope = ((success, F(1)) if mask >> site & 1
                            else (1-success, F(-1)))
                v, v1, v2 = v*f, v1*f+v*slope, v2*f+2*v1*slope
            for degree, term in enumerate((v, v1, v2)):
                total[degree] += weight*term
        rows.append((1, *total))
    return rows


def atom_jet(n, size, h, minor, a, c):
    x, xp = a*(1-c-a), 1-c-2*a
    f = x*x+c*x*h+c*c*minor
    f1, f2 = xp*(2*x+c*h), 2*xp*xp-4*x-2*c*h
    alpha, beta = size-2, n-size-2
    prefactor = a**alpha*(1-a)**beta
    score = F(alpha)/a-F(beta)/(1-a)
    score1 = -F(alpha)/a**2-F(beta)/(1-a)**2
    return (prefactor*f, prefactor*(f1+score*f),
            prefactor*(f2+2*score*f1+(score*score+score1)*f))


def full_from_minors(n, mu, a, c):
    h = [sum((v for ij, v in mu.items() if i in ij), F(0)) for i in range(n)]
    rows = []
    for mask in range(1 << n):
        chosen = [i for i in range(n) if mask >> i & 1]
        minor = sum((mu[(i, j)] for i, j in combinations(chosen, 2)), F(0))
        rows.append((1, *atom_jet(n, len(chosen), sum(h[i] for i in chosen), minor, a, c)))
    return rows


def normalization(rows):
    require(sum(m*p for m, p, _, _ in rows) == 1, 'mass not one')
    require(sum(m*p1 for m, _, p1, _ in rows) == 0, 'first mass jet')
    require(sum(m*p2 for m, _, _, p2 in rows) == 0, 'second mass jet')


def serialize_full(systems, encoding):
    triples, lookup, maps = [], {}, []
    for rows in systems:
        current = []
        for m, *jet in rows:
            key = tuple(jet)
            if key not in lookup:
                lookup[key] = len(triples)
                triples.append([str(v) for v in jet])
            current.append([m, lookup[key]])
        maps.append(current)
    return {'encoding': encoding, 'jet_order': ['p', 'partial_a_p', 'partial_a2_p'],
            'jet_classes': triples, 'systems': maps}


def raw_frame_law(w):
    gram = [[sum(F(v[i])*F(v[j]) for v in w) for j in range(2)] for i in range(2)]
    determinant = gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0]
    require(determinant > 0, 'rank deficient frame')
    mu = {(i, j): F(det2(w[i], w[j]))**2/determinant
          for i, j in combinations(range(len(w)), 2)}
    require(sum(mu.values()) == 1, 'Cauchy-Binet normalization')
    return mu, gram


def rotation_certificate():
    w = [[F(-7), F(-4)], [F(6), F(-3)], [F(-2), F(4)], [F(5), F(0)]]
    rotated = [[(12*w[0][q]+5*w[1][q])/13 for q in range(2)],
               [(-5*w[0][q]+12*w[1][q])/13 for q in range(2)], *w[2:]]
    mu, gram = raw_frame_law(w)
    nu, gram2 = raw_frame_law(rotated)
    require(gram == gram2, 'physical rotation must preserve column Gram')
    require(all(v > 0 for v in (*mu.values(), *nu.values())), 'full input support')
    h = [sum(v for ij, v in mu.items() if i in ij) for i in range(4)]
    h2 = [sum(v for ij, v in nu.items() if i in ij) for i in range(4)]
    require(0 < h2[0]-h2[1] < h[0]-h[1], 'not leverage balancing')
    determinant = gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0]
    offdiag = (w[0][0]*(gram[1][1]*w[1][0]-gram[0][1]*w[1][1])
               +w[0][1]*(-gram[1][0]*w[1][0]+gram[0][0]*w[1][1]))/determinant
    require(offdiag < 0, 'monotone real rotation condition')
    a, c = F(1, 200), F(19, 20)
    first, second = channel_jet(4, mu, a, c), channel_jet(4, nu, a, c)
    for rows, law in ((first, mu), (second, nu)):
        normalization(rows)
        require(rows == full_from_minors(4, law, a, c), 'independent atom jets')
    gain = difference(entropy(second), entropy(first))
    h0, h1 = entropy(first, 2), entropy(second, 2)
    curvature = difference(h1, h0)
    require(gain[0] > F(6, 1000), 'entropy increase not certified')
    require(curvature[1] < -F(17, 10), 'rotation route obstruction not certified')
    require(h0[1] < 0 and h1[1] < 0, 'do not confuse route with target')
    return {'status': 'PASS_EXACT_PROJECTION_ROTATION_OBSTRUCTION',
            'a': str(a), 'c': str(c), 'frame': [[str(v) for v in r] for r in w],
            'rotation': {'numerator': [[12, 5], [-5, 12]], 'denominator': 13},
            'source_offdiagonal_01': str(offdiag),
            'monotonicity': 'd>0, r<0, 0<=angle<=atan(5/12)<pi/4, final d>0; d(angle) strictly decreases.',
            'gram': [[str(v) for v in r] for r in gram],
            'input_minors': {str(ij): str(v) for ij, v in mu.items()},
            'rotated_input_minors': {str(ij): str(v) for ij, v in nu.items()},
            'diagonal_before': list(map(str, h)), 'diagonal_after': list(map(str, h2)),
            'entropy_gain': decimal_interval(gain), 'curvature_gain': decimal_interval(curvature),
            'source_hessian': decimal_interval(h0), 'rotated_hessian': decimal_interval(h1),
            'full_atoms': serialize_full([first, second],
                'Each system is masks 0,...,15; bit i=(mask>>i)&1; entries are [multiplicity,jet_class].')}


def weighted_frame(v, weights, clones):
    # Last row type occurs 'clones' times, each with the stated squared row scale.
    multiplicities = [1]*(len(v)-1)+[clones]
    gram = [[sum(F(m)*w*r[i]*r[j] for m, w, r in zip(multiplicities, weights, v))
             for j in range(2)] for i in range(2)]
    require(gram == [[1, 0], [0, 1]], 'weighted frame is not an isometry')
    h = [w*(r[0]**2+r[1]**2) for w, r in zip(weights, v)]
    mu = [[weights[i]*weights[j]*det2(v[i], v[j])**2
           for j in range(len(v))] for i in range(len(v))]
    expanded = v[:-1]+[v[-1]]*clones
    checks = 0
    for i, j, k, l in combinations(range(len(expanded)), 4):
        u = expanded
        require(det2(u[i], u[j])*det2(u[k], u[l])
                -det2(u[i], u[k])*det2(u[j], u[l])
                +det2(u[i], u[l])*det2(u[j], u[k]) == 0, 'Pluecker compatibility')
        checks += 1
    return h, mu, checks


def grouped_rows(h, mu, clones, a, c, theta):
    explicit = len(h)-1
    n = explicit+clones
    perm = [1, 0]+list(range(2, len(h)))
    mixed = [[(1-theta)*mu[i][j]+theta*mu[perm[i]][perm[j]]
              for j in range(len(h))] for i in range(len(h))]
    require(h[0] == h[1], 'equal-leverage swap condition')
    rows = []
    for mask in range(1 << explicit):
        chosen = [i for i in range(explicit) if mask >> i & 1]
        for k in range(clones+1):
            ht = sum((h[i] for i in chosen), F(0))+k*h[-1]
            mt = sum((mixed[i][j] for i, j in combinations(chosen, 2)), F(0))
            mt += k*sum((mixed[i][-1] for i in chosen), F(0))
            rows.append((comb(clones, k), *atom_jet(n, len(chosen)+k, ht, mt, a, c)))
    normalization(rows)
    return rows


def polynomial_jet(coeffs, a):
    return tuple(sum((coef*F(1 if d == 0 else degree if d == 1 else degree*(degree-1))
                      *a**(degree-d) for degree, coef in coeffs.items() if degree >= d), F(0))
                 for d in range(3))


def all_grouped_inclusion_jets(rows, h, mu, clones, a, c, theta):
    explicit = len(h)-1
    perm = [1, 0]+list(range(2, len(h)))
    mixed = [[(1-theta)*mu[i][j]+theta*mu[perm[i]][perm[j]]
              for j in range(len(h))] for i in range(len(h))]
    checked = 0
    for target in range(1 << explicit):
        chosen = [i for i in range(explicit) if target >> i & 1]
        for r in range(clones+1):
            size = len(chosen)+r
            ht = sum((h[i] for i in chosen), F(0))+r*h[-1]
            mt = sum((mixed[i][j] for i, j in combinations(chosen, 2)), F(0))
            mt += r*sum((mixed[i][-1] for i in chosen), F(0))
            coeffs = {size: F(1)}
            if size >= 1:
                coeffs[size-1] = c*ht
            if size >= 2:
                coeffs[size-2] = c*c*mt
            expected = polynomial_jet(coeffs, a)
            actual = [F(0), F(0), F(0)]
            for mask in range(1 << explicit):
                if mask & target != target:
                    continue
                for k in range(r, clones+1):
                    _, *jet = rows[mask*(clones+1)+k]
                    mult = comb(clones-r, k-r)
                    for d in range(3):
                        actual[d] += mult*jet[d]
            require(tuple(actual) == expected, 'grouped inclusion-jet cross-check')
            checked += 3
    return checked


def circuit_certificate(clones, a=F(1, 200), c=F(19, 20), t=F(1, 2)):
    v = [[2, 1], [2, -1], [2, 2], [2, -2], [0, 1]]
    weights = [F(1, 16)]*4+[F(3, 8*clones)]
    h, mu, pluecker = weighted_frame(v, weights, clones)
    eta = mu[1][2]-mu[0][2]
    require(eta == F(1, 8), 'circuit eta')
    require(mu[1][3]-mu[0][3] == -eta, 'circuit closure')
    require(mu[1][4]-mu[0][4] == 0, 'spectator leakage')
    first, middle, last = [grouped_rows(h, mu, clones, a, c, s) for s in (F(0), t, F(1))]
    for row0, rowt, row1 in zip(first, middle, last):
        require(row0[0] == rowt[0] == row1[0], 'multiplicity changed')
        require(all(rowt[d] == (1-t)*row0[d]+t*row1[d] for d in (1, 2, 3)), 'affine atom chord')
    checks = all_grouped_inclusion_jets(middle, h, mu, clones, a, c, t)
    if clones == 1:
        law = {(i, j): mu[i][j] for i, j in combinations(range(5), 2)}
        direct = channel_jet(5, law, a, c)
        for mask in range(16):
            for k in range(2):
                require(first[mask*2+k] == direct[mask+(k<<4)], 'five-site channel cross-check')
    h0, ht = entropy(first, 2), entropy(middle, 2)
    gain = difference(ht, h0)
    beta = F(3, 8)
    theoretical = 2*c**3*(4*c-beta)*eta**2*t*(1-t)
    require(gain[0] > theoretical, 'finite fixture fails proved comparison margin')
    return {'status': 'PASS_EXACT_CONNECTED_CIRCUIT_FIXTURE', 'n': clones+4,
            'rank': 2, 'clones': clones, 'raw_rows': v,
            'squared_row_scales': list(map(str, weights)), 'eta': str(eta), 'beta': str(beta),
            'a': str(a), 'c': str(c), 'mixing_parameter': str(t),
            'pluecker_checks': pluecker, 'inclusion_jet_equalities': checks,
            'curvature_gain': decimal_interval(gain), 'proved_lower_bound': str(theoretical),
            'source_hessian': decimal_interval(h0), 'mixed_hessian': decimal_interval(ht),
            'full_atoms': serialize_full([first, middle, last],
                'Systems: s=0,t,1 for the stored mixing_parameter. Index=mask*(clones+1)+k; mask=0,...,15 describes sites 0..3; k=0,...,clones. Each entry represents binom(clones,k) complete atoms, not a count probability.')}


def fixed_diagonal_four_certificate():
    w0 = [[5, 0], [0, 5], [3, 4], [-4, 3]]
    w1 = [[5, 0], [0, 5], [4, 3], [-3, 4]]
    mu, _ = raw_frame_law(w0)
    nu, _ = raw_frame_law(w1)
    h0 = [sum(v for ij, v in mu.items() if i in ij) for i in range(4)]
    h1 = [sum(v for ij, v in nu.items() if i in ij) for i in range(4)]
    require(h0 == h1 == [F(1, 2)]*4, 'fixed diagonal fixture')
    a, c, t = F(1, 200), F(19, 20), F(1, 3)
    middle_law = {ij: (1-t)*mu[ij]+t*nu[ij] for ij in mu}
    systems = [channel_jet(4, law, a, c) for law in (mu, middle_law, nu)]
    for rows, law in zip(systems, (mu, middle_law, nu)):
        normalization(rows)
        require(rows == full_from_minors(4, law, a, c), 'fixed diagonal full-law identity')
    curvature = difference(entropy(systems[1], 2),
                    add(scale(entropy(systems[0], 2), 1-t), scale(entropy(systems[2], 2), t)))
    lower = 2*c**4*t*(1-t)*sum((nu[ij]-mu[ij])**2 for ij in mu)
    require(curvature[0] > lower, 'four-site fixed-diagonal margin')
    return {'status': 'PASS_EXACT_FIXED_DIAGONAL_FOUR_SITE_COMPARISON',
            'a': str(a), 'c': str(c), 'mixing_parameter': str(t),
            'source_frames': [w0, w1], 'diagonals': list(map(str, h0)),
            'curvature_gain': decimal_interval(curvature), 'proved_lower_bound': str(lower),
            'full_atoms': serialize_full(systems, 'Systems s=0,1/3,1; masks 0,...,15, bit i=(mask>>i)&1.')}


def exponential_interval(x, degree=80):
    require(x >= 0 and degree+2 > x, 'invalid positive exponential tail')
    term, total = F(1), F(1)
    for k in range(1, degree+1):
        term *= x/k
        total += term
    next_term = term*x/(degree+1)
    return total, total+next_term/(1-x/F(degree+2))


def fisher_second(first, middle, last):
    out = (F(0), F(0))
    for r0, rt, r1 in zip(first, middle, last):
        m, p, p1, p2 = rt
        v, v1, v2 = (r1[d]-r0[d] for d in (1, 2, 3))
        term = 2*(v1-v*p1/p)**2/p+2*v*v2/p-v*v*p2/(p*p)
        out = add(out, scale(enclose(term), F(m)))
    return out


def gaussian_obstruction():
    clones = 31
    v = [[1, 1], [1, -1], [3, 4], [-4, 3]]
    weights = [F(1, 4), F(1, 4), F(1, 50), F(1, 50*clones)]
    h, mu, pluecker = weighted_frame(v, weights, clones)
    eta = mu[1][2]-mu[0][2]
    require(eta == F(6, 25), 'Gaussian eta')
    require(mu[1][3]-mu[0][3] == -eta/clones, 'Gaussian clone differences')
    a, c, t = F(1, 1000), F(19, 20), F(1, 2)
    exp_lo, exp_hi = exponential_interval(F(38, 5))
    require(exp_lo > 1900 and exp_hi < 2000, 'exponential enclosure not certified')
    eps_interval = (F(1, 2000), F(1, 1900))
    radius, xp = F(16), 1-c-2*a
    def bracket(eps):
        p0 = eps+F(1, clones)
        d = (1-eps)*(1-F(1, clones))
        return (2*radius+radius*radius*xp*xp)*(p0+a*d)-2*radius*xp*d
    values = [bracket(eps) for eps in eps_interval]
    bracket_interval = (min(values), max(values))
    require(bracket_interval[1] < -F(3, 8), 'summed Gaussian pointwise obstruction')
    first, middle, last = [grouped_rows(h, mu, clones, a, c, s) for s in (F(0), t, F(1))]
    for r0, rt, r1 in zip(first, middle, last):
        require(all(rt[d] == (r0[d]+r1[d])/2 for d in (1, 2, 3)), 'Gaussian affine chord')
    checks = all_grouped_inclusion_jets(middle, h, mu, clones, a, c, t)
    h0, ht = entropy(first, 2), entropy(middle, 2)
    gain, i2 = difference(ht, h0), fisher_second(first, middle, last)
    require(gain[0] > 228 and i2[0] > 464, 'signed integral compensation not certified')
    require(h0[1] < 0 and ht[1] < 0, 'not an entropy target counterexample')
    return {'status': 'PASS_EXACT_SUMMED_GAUSSIAN_ROUTE_OBSTRUCTION', 'n': 34, 'rank': 2,
            'raw_rows': v, 'squared_row_scales': list(map(str, weights)), 'clones': clones,
            'a': str(a), 'c': str(c), 'mixing_parameter': str(t),
            'gaussian_vector': ['12/5', '16/5'], 'gaussian_radius_squared': '16',
            'exp_degree': 80, 'epsilon_enclosure': list(map(str, eps_interval)),
            'local_second_derivative_bracket': list(map(str, bracket_interval)),
            'local_bracket_upper_bound': '-3/8', 'pluecker_checks': pluecker,
            'inclusion_jet_equalities': checks, 'curvature_gain': decimal_interval(gain),
            'fisher_second_derivative': decimal_interval(i2),
            'source_hessian': decimal_interval(h0), 'mixed_hessian': decimal_interval(ht),
            'full_atoms': serialize_full([first, middle, last],
                'Systems: s=0,1/2,1. Index=mask*32+k, mask=0,...,7 describes sites 0..2, k=0,...,31. Multiplicity binom(31,k) counts individual complete atoms; each stored jet is per atom. Covers all 2^34 atoms in every system.')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for name, factory in (('rotation', rotation_certificate),
                          ('circuit_n5', lambda: circuit_certificate(1)),
                          ('circuit_n10', lambda: circuit_certificate(6)),
                          ('circuit_lowcontrast_n5', lambda: circuit_certificate(1, F(1,4), F(1,8), F(1,3))),
                          ('fixed_diagonal_n4', fixed_diagonal_four_certificate),
                          ('gaussian_n34', gaussian_obstruction)):
        result = factory()
        text = json.dumps(result, indent=2, sort_keys=True)+'\n'
        (args.output_dir/(name+'.json')).write_text(text, encoding='utf-8')
        results[name] = {'status': result['status'], 'sha256': hashlib.sha256(text.encode()).hexdigest(),
                         'curvature_gain': result['curvature_gain']}
        print(result['status'], flush=True)
    summary = {'status': 'PASS_EXACT_S8_ROUND2', 'arithmetic': 'Fraction and outward dyadic rational intervals',
               'log_bits': BITS, 'log_terms': TERMS,
               'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'scope': 'Finite certificates and algebraic regressions; the all-dimensional theorem is proved in RESULT.md. Sine target remains unproved.',
               'fixtures': results}
    (args.output_dir/'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print('PASS_EXACT_S8_ROUND2', flush=True)


if __name__ == '__main__':
    main()
