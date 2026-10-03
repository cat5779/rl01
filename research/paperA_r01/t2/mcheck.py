"""Exact finite check of the unnormalized matrix FK interpolation.

Requires SymPy. Run: python mcheck.py
This checks finite examples and derivative identities, not the infinite theorem.
"""

import sympy as sp


def subsets(mask):
    sub = mask
    while True:
        yield sub
        if sub == 0:
            break
        sub = (sub - 1) & mask


def principal_determinants(kernel):
    size = kernel.rows
    values = {0: sp.Integer(1)}
    for mask in range(1, 1 << size):
        sites = [j for j in range(size) if mask & (1 << j)]
        values[mask] = sp.simplify(kernel.extract(sites, sites).det())
    return values


def increasing_event_masks(size):
    for event in range(1 << (1 << size)):
        valid = True
        for configuration in range(1 << size):
            if not (event & (1 << configuration)):
                continue
            for j in range(size):
                if not (event & (1 << (configuration | (1 << j)))):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            yield event


def verify_direction(kernel, group_size, type_count):
    size = kernel.rows
    assert size == group_size * type_count
    assert kernel == kernel.conjugate().transpose()
    # All principal minors are positive for K and I-K.
    dets = principal_determinants(kernel)
    comp = principal_determinants(sp.eye(size) - kernel)
    assert all(value > 0 for value in dets.values())
    assert all(value > 0 for value in comp.values())
    inverse = kernel.inv()
    # At t=0, a(0)=1 and r=Tr_total(K^-1)-(m-1).
    rate = sp.trace(inverse) / group_size - (type_count - 1)
    assert all(rate >= inverse[j, j] for j in range(size))
    inclusion_slopes = {}
    for mask, determinant in dets.items():
        inclusion_slopes[mask] = sp.simplify(
            sum(dets[mask ^ (1 << j)] for j in range(size)
                if mask & (1 << j)) - rate * mask.bit_count() * determinant
        )
    full = (1 << size) - 1
    pattern_slopes = {}
    probabilities = {}
    for occupied in range(1 << size):
        absent = full ^ occupied
        probabilities[occupied] = sum(
            (-1) ** extra.bit_count() * dets[occupied | extra]
            for extra in subsets(absent)
        )
        pattern_slopes[occupied] = sum(
            (-1) ** extra.bit_count() * inclusion_slopes[occupied | extra]
            for extra in subsets(absent)
        )
    assert sum(probabilities.values()) == 1
    assert all(p > 0 for p in probabilities.values())
    assert sum(pattern_slopes.values()) == 0
    event_count = 0
    for event in increasing_event_masks(size):
        derivative = sum(pattern_slopes[s] for s in range(1 << size)
                         if event & (1 << s))
        assert derivative <= 0
        event_count += 1
    return event_count, rate


def main():
    q = sp.Rational
    a = sp.Matrix([[q(1, 3), sp.I / 12], [-sp.I / 12, q(2, 3)]])
    b = sp.Matrix([[q(1, 12), q(1, 24)], [q(1, 24), -q(1, 12)]])
    kernel = a.row_join(b).col_join(b.row_join(a))
    swap = sp.zeros(4)
    for j in range(4):
        swap[j, (j + 2) % 4] = 1
    assert swap * kernel == kernel * swap
    for name, current in (("Q", kernel), ("I-Q", sp.eye(4) - kernel)):
        count, rate = verify_direction(current, group_size=2, type_count=2)
        assert count == 168
        print(f"{name}: all {count} increasing events have nonpositive derivative; r={rate}")

    # The normalized determinant is too large for homogeneous domination.
    diagonal = sp.diag(q(1, 4), q(3, 4))
    normalized_fk = sp.sqrt(diagonal.det())
    assert normalized_fk > diagonal[0, 0]
    assert 1 - normalized_fk < diagonal[1, 1]
    print("Normalized two-type FK sandwich: disproved by the two one-site events.")
    print("PASS (finite exact verification only)")


if __name__ == "__main__":
    main()
