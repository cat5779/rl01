"""Rigorous sine-posterior obstruction to the old pair comparison at c=19/20.

The computation uses Arb balls (via python-flint), not ordinary floating
point.  In the ten-site half-density sine Toeplitz marginal, condition the
outside of pair (3,6) on the displayed legal output word.  The resulting
two-site latent posterior is a strict positive contraction, but its exact
pair contribution satisfies ``g > 2 (K + D)``.  Hence the old pointwise
two-budget route cannot close at this sine state with any gamma<2.
"""

from __future__ import annotations

from flint import arb, arb_mat, ctx


ctx.prec = 256
N = 10
C = arb(19) / 20
A0 = arb(1) / 40
PAIR = [3, 6]
OUTSIDE = [0, 1, 2, 4, 5, 7, 8, 9]
WORD = [1, 0, 1, 1, 0, 0, 1, 0]


def sine_kernel(n: int) -> arb_mat:
    q = arb_mat(n, n)
    pi = arb.pi()
    for i in range(n):
        for j in range(n):
            r = i - j
            if r == 0:
                value = arb(1) / 2
            elif r % 2 == 0:
                value = arb(0)
            else:
                # sin(pi*r/2) is exactly +/-1 for odd integer r.
                sign = 1 if r % 4 == 1 else -1
                value = arb(sign) / (pi * r)
            q[i, j] = value
    return q


def omega(r):
    return (r - arb(1) / 2) ** 2 / (r * (1 - r))


def main() -> None:
    q = sine_kernel(N)
    k = arb_mat(N, N)
    for i in range(N):
        for j in range(N):
            k[i, j] = C * q[i, j] + (A0 if i == j else 0)

    outside_block = arb_mat([[k[i, j] for j in OUTSIDE] for i in OUTSIDE])
    for i, bit in enumerate(WORD):
        outside_block[i, i] -= 1 - bit
    cross = arb_mat([[k[i, j] for j in OUTSIDE] for i in PAIR])
    pair_block = arb_mat([[k[i, j] for j in PAIR] for i in PAIR])
    conditional_output = pair_block - cross * outside_block.inv() * cross.transpose()
    posterior = (
        conditional_output - arb_mat([[A0, 0], [0, A0]])
    ) / C

    x, y = posterior[0, 0], posterior[1, 1]
    z = posterior[0, 1] * posterior[1, 0]
    lower_cap = x * y - z
    upper_cap = (1 - x) * (1 - y) - z
    assert x > 0 and y > 0 and 1 - x > 0 and 1 - y > 0
    assert lower_cap > 0 and upper_cap > 0

    s = C * C * z
    q0, r0 = A0 + C * x, A0 + C * y
    atom00 = (1 - q0) * (1 - r0) - s
    atom10 = q0 * (1 - r0) + s
    atom01 = (1 - q0) * r0 + s
    atom11 = q0 * r0 - s
    assert atom00 > 0 and atom10 > 0 and atom01 > 0 and atom11 > 0

    alpha = A0 * (A0 + C)
    k_energy = 2 * alpha * z * (
        1 / atom00 + 1 / atom10 + 1 / atom01 + 1 / atom11
    )
    ri0 = x + C * z / (1 - r0)
    ri1 = x - C * z / r0
    rj0 = y + C * z / (1 - q0)
    rj1 = y - C * z / q0
    d_energy = alpha * z * (
        (omega(ri0) + omega(rj0)) / atom00
        + (omega(ri0) + omega(rj1)) / atom10
        + (omega(ri1) + omega(rj0)) / atom01
        + (omega(ri1) + omega(rj1)) / atom11
    )
    pair_term = (atom10 * atom01 / (atom00 * atom11)).log() - s * (
        1 / atom00 + 1 / atom10 + 1 / atom01 + 1 / atom11
    )
    margin = pair_term - 2 * (k_energy + d_energy)
    assert margin > 0

    print("c=19/20 finite-sine gamma=2 obstruction: PASS")
    print(f"pair={PAIR} outside={OUTSIDE} word={WORD}")
    print(f"posterior={posterior}")
    print(f"lower determinant cap={lower_cap}")
    print(f"upper determinant cap={upper_cap}")
    print(f"pair term={pair_term}")
    print(f"K+D={k_energy + d_energy}")
    print(f"g-2(K+D)={margin} > 0")


if __name__ == "__main__":
    main()
