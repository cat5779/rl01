# Promoted statements frozen before final proof/certification

Frozen UTC: 2026-09-16T13:21:46.236769Z

## Target A: real-q correlated-reference control

For any finite DPP law p=DPP(K) with delta I <= K <= (1-delta) I, prove a dimension-linear subgaussian bound for the full information content -log p(S).  For a disjoint-block reference w built from true marginals, prove on 1/2 <= q <= 3/2 that the exact positive Hölder remainder

    E_q(a) = [log Z_p(q,a)-B(q,a;w_a)]/(q-1)

(continuously extended at q=1) is nonnegative and satisfies

    0 <= E_q(a)/n <= D(p_a||w_a)/n + C_delta |q-1|.

For the stationary Toeplitz law and R|n, use the supplied value tail only to replace D/n by e_R and deduce a uniformly vanishing signed Jensen defect when R -> infinity and q -> 1 in that order or jointly.  All moving-reference a-derivatives must be stated exactly even though the proof of the signed defect is derivative-free.

## Target B: explicit high-contrast curvature band

Re-establish the full-atom Chebyshev expansion used in the latest author package.  Prove an inner-interval Bernstein response estimate.  Combining it with the reviewed theorem H''/n <= -1/50 at c0=37/40, prove for every finite Hermitian contraction Q, after complementing when necessary, an explicit nonempty band c0 < c <= c0+10^(-13) and a fixed centered a-strip of half-width 1/200 on which H(DPP(aI+cQ))''/n <= -1/200.  Then pass the integrated inequality to the sine entropy rate.  Exact constants are to be certified by rational arithmetic.
