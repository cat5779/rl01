"""Exact auxiliary checks for RESULT.md.

This script checks finite algebraic interfaces only.  It is not a proof of the
infinite-dimensional stochastic-domination theorem.
"""

from collections import deque
from fractions import Fraction as F
from itertools import combinations


def determinant(matrix):
    a = [row[:] for row in matrix]
    out = F(1)
    for j in range(len(a)):
        pivot_row = next((k for k in range(j, len(a)) if a[k][j]), None)
        if pivot_row is None:
            return F(0)
        if pivot_row != j:
            a[j], a[pivot_row] = a[pivot_row], a[j]
            out = -out
        pivot = a[j][j]
        out *= pivot
        for k in range(j + 1, len(a)):
            ratio = a[k][j] / pivot
            for ell in range(j + 1, len(a)):
                a[k][ell] -= ratio * a[j][ell]
    return out


def build_tree_prefix(edge_count=9):
    adjacency = {0: []}
    depth = {0: 0}
    edges = []
    frontier = deque([0])
    while len(edges) < edge_count:
        u = frontier.popleft()
        child_count = 3 if u == 0 else 2
        for _ in range(child_count):
            v = len(adjacency)
            adjacency[v] = [u]
            adjacency[u].append(v)
            depth[v] = depth[u] + 1
            frontier.append(v)
            # Bipartite orientation, as in the C3*C3 Bass--Serre tree.
            edges.append((u, v) if depth[u] % 2 == 0 else (v, u))
            if len(edges) == edge_count:
                break
    return adjacency, edges


def distances(adjacency):
    result = {}
    for start in adjacency:
        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            vertex, distance = queue.popleft()
            result[start, vertex] = distance
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, distance + 1))
    return result


def tree_projection_checks():
    adjacency, edges = build_tree_prefix()
    distance = distances(adjacency)

    def green(u, v):
        return F(2, 3) * F(1, 2) ** distance[u, v]

    kernel = []
    for a, b in edges:
        row = []
        for c, d in edges:
            row.append(green(b, d) - green(b, c) - green(a, d) + green(a, c))
        kernel.append(row)

    principal = {0: F(1)}
    connected_count = 0
    for mask in range(1, 1 << len(edges)):
        indices = [i for i in range(len(edges)) if mask >> i & 1]
        value = determinant([[kernel[i][j] for j in indices] for i in indices])
        assert value > 0
        principal[mask] = value

        reached = {indices[0]}
        while True:
            enlarged = reached | {
                i
                for i in indices
                if any(set(edges[i]) & set(edges[j]) for j in reached)
            }
            if enlarged == reached:
                break
            reached = enlarged
        if len(reached) == len(indices):
            m = len(indices)
            assert value == F(1, 2) ** m * (1 + F(m, 3))
            connected_count += 1

    def mixed_pattern(ones, zeros):
        total = F(0)
        subset = zeros
        while True:
            total += (-1) ** subset.bit_count() * principal[ones | subset]
            if subset == 0:
                return total
            subset = (subset - 1) & zeros

    positive_histories = 0
    zero_histories = 0
    minimum_conditional = F(1)
    for i in range(len(edges)):
        previous = (1 << i) - 1
        for ones in range(1 << i):
            zeros = previous ^ ones
            denominator = mixed_pattern(ones, zeros)
            assert denominator >= 0
            if denominator == 0:
                zero_histories += 1
                continue
            conditional = mixed_pattern(ones | (1 << i), zeros) / denominator
            assert F(1, 2) <= conditional <= 1
            minimum_conditional = min(minimum_conditional, conditional)
            positive_histories += 1

    return {
        "tree_edges": len(edges),
        "positive_principal_minors": len(principal) - 1,
        "connected_determinant_checks": connected_count,
        "positive_bfs_histories": positive_histories,
        "zero_probability_histories_skipped": zero_histories,
        "minimum_bfs_conditional": str(minimum_conditional),
    }


def spectral_gap_checks():
    # Trace masses are 1/3 at 1/128 and 2/3 at 1/2.
    fk_cube = F(1, 128) * F(1, 2) ** 2
    assert fk_cube == F(1, 8) ** 3
    assert F(65, 256) > F(1, 8)
    assert F(191, 256) < F(7, 8)
    return {
        "gapped_fk": "1/8",
        "dominated_bernoulli": "65/256",
        "complement_upper_witness": "191/256 < 7/8",
    }


def multi_orbit_trace_checks():
    # Q=diag(1/4,3/4).  The normalized FK is sqrt(3)/4.
    q_low, q_high = F(1, 4), F(3, 4)
    fk_normalized_squared = q_low * q_high
    assert fk_normalized_squared == F(3, 16)
    # sqrt(3)/4 > 1/4, checked without floating point.
    assert fk_normalized_squared > q_low * q_low
    # Hence 1-sqrt(3)/4 < 3/4 as well.
    assert fk_normalized_squared > (1 - q_high) ** 2
    assert q_low == min(q_low, q_high)
    assert q_high == max(q_low, q_high)
    return {
        "exact_lower_threshold": "1/4",
        "exact_upper_threshold": "3/4",
        "normalized_fk_squared": "3/16",
        "normalized_fk_lower_bound_fails": True,
        "normalized_fk_upper_bound_fails": True,
        "unnormalized_fk": "3/16",
    }


def finite_support_checks():
    # Exact rational part of (5.22)--(5.23), with N=255.
    assert 20 * 19**256 * 1024 < 20**256
    epsilon = F(1, 1024)
    assert F(1, 128) - epsilon == F(7, 1024)
    lower_threshold = F(65, 256) - epsilon
    assert lower_threshold == F(259, 1024)
    # log(7/6)>1/7 implies exp(1/7)<7/6; only the final rational
    # comparison is checked here.
    assert F(7, 48) < lower_threshold
    return {
        "polynomial_degree": 255,
        "norm_error_bound": "< 1/1024",
        "kernel_lower_gap": "7/1024",
        "fk_upper_bound": "< 7/48",
        "domination_lower_bound": "259/1024",
    }


def main():
    result = {
        "tree_projection": tree_projection_checks(),
        "spectral_gap": spectral_gap_checks(),
        "multi_orbit_trace": multi_orbit_trace_checks(),
        "finite_support_group_ring": finite_support_checks(),
        "status": "PASS",
        "scope": "finite exact auxiliary checks; not an infinite-dimensional proof",
    }
    for section, values in result.items():
        print(f"{section}: {values}")


if __name__ == "__main__":
    main()
