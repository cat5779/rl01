# Gap audit

**New author status:** proved scoped analytical and exact-computational obstructions, pending independent audit. The word “proved” in this packet does not imply reviewed or merged status.

## Original target obligations

| Obligation | Status in this packet |
|---|---|
| General projection (P2) for `37/40<c<1` | **Unresolved**; neither proved nor disproved |
| Full fixed-density S-sine configuration entropy-rate concavity in that range | **Unresolved**; no target counterexample |
| `sup_(a in J) H_(n,k)''(a) <= o(n)` for growing contiguous Fourier projections | **Unresolved** |
| A projection-compatible path from growing Fourier to a solved absolute-sign reference | **Unresolved** |
| Reviewed finite-cyclic-to-true-block value/Jensen bridge | **Supplied reviewed baseline**, not re-proved or promoted from the prior author artifact; not needed to prove the new obstructions |
| Rank-one/co-rank-one quantitative concavity | **Supplied reviewed baseline**, not claimed as new |
| Reviewed S8 real rank-two four-cycle curvature difference | **Supplied reviewed baseline**, not extended by assumption |

## New results and their exact boundaries

### 1. Two-step affine closure on the specified growing Fourier family

**Disproved.** Theorem 4.1 proves non-DPP representability of the second affine mixture for every odd `n`, `3<=k<=n-4`, the specified reflection pairs, and all strict mixing parameters. It permits arbitrary complex alternative frames and even arbitrary Hermitian-contraction kernels.

**No proof gap identified in the scoped statement.** The conditional Gram argument is fully analytical. Remaining scope: not every pair of steps or every possible path is ruled out. The conditional event can be rare at large dimension, so no uniform approximation/curvature cost is inferred from exact non-representability alone.

### 2. Nonnegative curvature orientation for repeated actual quadrature rotations

**Disproved in the explicitly exhibited rank-three Fourier continuation.** The second actual Pi_(7,3) step has `H_2''-H_1''<-4/5`. Both kernels are projections, diagonals stay `3/7`, outside rows are fixed during the step, and its two endpoints in the local parameter are coordinate-permuted.

**No proof gap identified in the finite certified statement.** It is supported by proved exhaustive rational interval arithmetic, not floating signs. Remaining scope: this does not refute the reviewed S8 theorem, whose real rank-two/four-cycle hypotheses do not hold on that intermediate outside frame. It also does not prove a negative sign on a growing contiguous family.

### 3. Universal sublinear correction between ideal and physical second steps

**Disproved for the stated universal/block-sum version.** Independent copies of the genuine seven-site fixture yield actual-minus-ideal curvature `<-17n/70` at `n=7m`, rank `3m`. The actual second-step curvature gain is `<-4n/35`.

**No proof gap identified in this tensorized comparison.** These kernels are not `Pi_(7m,3m)`. No assertion that every contiguous-Fourier path has extensive cost is made. Other steps could have compensating signs. A specialized signed cancellation estimate remains an open obligation.

### 4. Frozen explicit shared-outside-frame family

**Unresolved, not refuted by the other examples.** The family in proof.md (7.1) was frozen before the diagnostic search. Its rank grows, its outside isometry is arbitrary, and it is not restricted to coordinate products. The exact wedge disintegration and full-law Fisher expression are valid, but no new bound on their second `a` derivative is proved for the full class.

Three exact rank-three fixture tests and 6000 floating trials are not a substitute for a theorem. Their successful signs do not establish composability or a paid path.

### 5. Robust finite distance from the projection class

**Proved for the rational seven-site moment-curve fixture.** The twice-averaged law has TV distance greater than `10^-6` from every rank-three projection law; a complete conditional Gram determinant and a Lipschitz estimate establish this without numerical optimization.

The noisy separation is restricted to candidate laws `DPP(aI+cQ)` with `Q` a rank-three projection. No general lower bound on entropy or curvature follows from this TV fact, and none is used.

## Boundary audit

- Fourier incompatibility requires `0<t,u<1`; at mixing endpoints one of the rank-producing variance terms vanishes. Endpoints are not falsely excluded.
- `3<=k<=n-4`, odd `n`, ensures the specified three nonzero reflection pairs survive the conditioning set.
- Complete input minors can be zero. No logarithm of an input minor is used in the certified curvature calculations.
- The curvature certificates use the strict legal point `a=1/200,c=19/20`. Every complete output atom is strictly positive there.
- Channel injectivity and law non-representability extend to legal `a` endpoints because `c>0`; no endpoint Hessian is asserted.
- Finite entropy and the cycle identity extend continuously; no entropy-rate second derivative is assumed.
- Complete-law acceleration and Fisher terms are retained. No count/spectral replacement, frozen output weights, or differentiation of a value error occurs.

## Independent-review and execution limitations

- The exact algorithms and the analytical proofs have been author-checked and replayed. There has been **no independent audit** in this round.
- One early Fourier rational-sum implementation timed out; its partial log is preserved and not called a pass. Outward interval rounding repaired denominator growth; the repaired standard and optimized replays passed.
- A container network-download attempt failed; public sources were read through the browser. No failed download is reported as a verified source-byte snapshot.
- The old archive is preserved, not newly authenticated as mathematically correct in its entirety.
