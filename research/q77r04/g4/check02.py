"""Independent exact-arithmetic audit of source.md, equations (10)--(11).

This verifies finite examples only; the general proof is audited in audit02.md.
No non-standard packages or input from other audit files are used.
"""
from fractions import Fraction as F
from itertools import combinations
import json

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def tr(a):
    return [list(row) for row in zip(*a)]

def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]

def add(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]

def inverse(a):
    n = len(a)
    aug = [row[:] + ident for row, ident in zip(a, eye(n))]
    for j in range(n):
        pivot = next(k for k in range(j, n) if aug[k][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        scale = aug[j][j]
        aug[j] = [x / scale for x in aug[j]]
        for i in range(n):
            if i != j:
                scale = aug[i][j]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]

def determinant(a):
    a = [row[:] for row in a]
    answer = F(1)
    for j in range(len(a)):
        pivot = next((k for k in range(j, len(a)) if a[k][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            answer = -answer
        scale = a[j][j]
        answer *= scale
        for i in range(j + 1, len(a)):
            factor = a[i][j] / scale
            a[i] = [x - factor * y for x, y in zip(a[i], a[j])]
    return answer

def subsets(n):
    return [tuple(c) for k in range(n + 1) for c in combinations(range(n), k)]

def minor(a, s):
    return determinant([[a[i][j] for j in s] for i in s])

def diagonal(values):
    return [[F(values[i]) if i == j else F(0)
             for j in range(len(values))] for i in range(len(values))]

def mixed_root(values):
    n = len(values)
    v = [F(i + 1) for i in range(n)]
    vv = sum(x * x for x in v)
    h = [[F(i == j) - 2 * v[i] * v[j] / vv
          for j in range(n)] for i in range(n)]
    return mul(mul(h, diagonal(values)), h)

roots = {
    "zero": diagonal([0, 0]),
    "identity": diagonal([1, 1]),
    "deterministic_mixed": diagonal([0, 1, F(1, 2)]),
    "rank_one_projection": [[F(1, 2), F(1, 2)],
                            [F(1, 2), F(1, 2)]],
    "mixed_01": mixed_root([0, 1, F(1, 2), F(1, 3)]),
    "mixed_projection": mixed_root([0, 1, 0, 1]),
    "interior": mixed_root([F(1, 4), F(1, 2), F(2, 3), F(3, 4)]),
}
root_fields = [
    [F(1)] * 4,
    [F(1, 2), F(2), F(1, 3), F(3)],
    [F(3), F(1, 3), F(5, 2), F(2, 5)],
    [F(1, 100), F(100), F(1, 7), F(7)],
]

cases = []
total_inclusions = 0
for name, square_root in roots.items():
    n = len(square_root)
    k = mul(square_root, square_root)
    all_sets = subsets(n)
    probabilities = {}
    for s in all_sets:
        probabilities[s] = sum(
            ((-1) ** (len(t) - len(s)) * minor(k, t)
             for t in all_sets if set(s).issubset(t)), F(0))
    assert sum(probabilities.values()) == 1
    assert min(probabilities.values()) >= 0
    for field_index, root_field in enumerate(root_fields):
        r = root_field[:n]
        d = [x * x for x in r]
        weights = {}
        for s in all_sets:
            weight = probabilities[s]
            for i in s:
                weight *= d[i]
            weights[s] = weight
        normalizer = sum(weights.values())
        assert normalizer > 0
        tilted = {s: weight / normalizer for s, weight in weights.items()}
        b = mul(diagonal(r), square_root)
        m = add(add(eye(n), k, -1), mul(tr(b), b))
        assert determinant(m) == normalizer
        p = mul(mul(b, inverse(m)), tr(b))
        assert p == tr(p)
        assert all(minor(p, s) >= 0 for s in all_sets)
        assert all(minor(add(eye(n), p, -1), s) >= 0 for s in all_sets)
        for s in all_sets:
            actual = sum((weight for t, weight in tilted.items()
                          if set(s).issubset(t)), F(0))
            assert actual == minor(p, s)
            total_inclusions += 1
        rows = []
        p2 = mul(p, p)
        for x in range(n):
            row_sum = F(0)
            for y in range(n):
                both = sum((weight for t, weight in tilted.items()
                            if x in t and y in t), F(0))
                covariance = both - p[x][x] * p[y][y]
                expected = (p[x][x] * (1 - p[x][x]) if x == y
                            else -p[x][y] ** 2)
                assert covariance == expected
                row_sum += abs(covariance)
            assert row_sum == p[x][x] * (1 - p[x][x]) + p2[x][x] - p[x][x] ** 2
            assert row_sum <= F(1, 2)
            rows.append(str(row_sum))
        cases.append({"kernel": name, "field": field_index,
                      "dimension": n, "row_absolute_sums": rows})

print(json.dumps({"status": "PASS", "arithmetic": "fractions.Fraction",
                  "kernels": len(roots), "tilts": len(cases),
                  "inclusion_identities": total_inclusions,
                  "scope": "finite algebra only; not a proof of the factor theorem",
                  "cases": cases}, ensure_ascii=False, indent=2))
