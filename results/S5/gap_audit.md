# Gap audit

## Proven scope

The proof is complete for:

- every even \(n=2m\);
- every probability law on the input \(m\)-subsets;
- every fixed \(0<c<1\);
- the single balanced interior shift \(a_0=(1-c)/2\);
- the actual common-offset channel and actual output layers;
- the exact formulas in Sections 3--7 of `proof.md`.

The true contiguous Fourier projections are a specialization, not an approximation, of this theorem.

## Target-level gaps

1. **No sign theorem for the central payment.**  The weighted Jeffreys production is nonnegative, but the central count covariance is negative.  Neither inequality (8.1) nor the weaker full-entropy inequality (8.2) is proved uniformly in growing dimension.
2. **Only the midpoint is treated.**  Away from the midpoint, \(\theta'\ne0\); the first-order count term, within-layer transport terms, and the preceding round's residual payment re-enter.
3. **No fixed-chord Jensen theorem.**  A pointwise curvature identity at one shift does not imply a nonzero-width Jensen estimate.
4. **No thermodynamic differentiation.**  No differentiability of the entropy rate is assumed or deduced.
5. **No Toeplitz Hessian transfer.**  The supplied Fourier-to-Toeplitz bridge controls values.  It is not differentiated.
6. **No claim that all layers or all edge summands have a favorable sign.**  Only the weighted two-direction Jeffreys sum is nonnegative.

## Exact sufficient inequalities still open

With \(g_l=(l-m)^2-nv\), the exact midpoint identity is

\[
v^2(\Phi-H)''=\sum_l\pi_lg_lF_l+v\sum_l\mathscr J_l.
\]

A sufficient inequality for \((\Phi-H)''\ge0\) is equation (8.1) of `proof.md`.  The exact condition for \(H''\le0\) is the weaker equation (8.2).  Neither is renamed as a theorem.

## Evidence limitations

- `evidence/exact_midpoint.json` proves finite algebraic identities, not an asymptotic sign.
- The dimensions 4 through 20 are floating diagnostics.
- Random searches are falsification tests only.
- The formal convex-mixture obstruction rules out only exact coefficient cancellation with weights in \([0,1]\).  Because the extreme-layer divergences vanish, it is not an entropy-scale obstruction.

## Relation to the prior O(sqrt n) payment

The prior material-response and all-orbit estimates are preserved and restated, but the new midpoint theorem does not depend on their correctness.  Conversely, the midpoint theorem does not replace the residual payment away from \(a_0\).

## Claims deliberately not made

- Full sine entropy-rate concavity.
- Concavity of every conditional layer.
- Convexity of \(\mathcal D\) for every homogeneous input.
- A Markov generator in the channel parameter.
- A common scalar clock.
- A proof from the positive within-slice term alone.
- A conclusion that all transport methods fail.
