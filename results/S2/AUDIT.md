# Independent audit of S2

**STATUS: ACCEPTED (scoped).**  The two principal route obstructions are
correct.  They do not settle the absolute entropy-curvature sign.

## Accepted statements

1. A rank-two complex projection law gives the submitted real Bloch Gram
   matrix, which is positive semidefinite of rank at most three.  Conditioning a
   rank-`k` projection law on `k-2` included sites produces a rank-two projection
   law.
2. Two independent reflection averages add two positive covariance directions.
   Under the nonzero-support conditions of Theorem 3.1, the conditional Gram
   matrix has rank four for every `t,u in (0,1)`.
3. For every odd `n` and `3<=k<=n-4`, the explicit reflection-invariant
   conditioning set leaves the three required nonzero reflection pairs in the
   consecutive Fourier law.  The first affine chord is realized by the
   quadrature unitary, but the twice-averaged law cannot be any
   Hermitian-contraction DPP.  The fixed-cardinality variance argument correctly
   reduces any hypothetical contraction kernel to a projection.
4. The exact `Pi_(7,3)` certificate at `(a,c)=(1/200,19/20)` verifies the four
   curvature intervals quoted in the group integration summary.  All 128 output
   atoms and both `a` derivatives are retained.  Independent block copies make
   the actual-minus-affine correction extensive at density `3/7`.

## Scope limits

- The rank-four incompatibility is exact but its conditioning event is not
  bounded below uniformly along the growing Fourier sequence.
- The extensive curvature correction uses coordinate direct sums, not the
  growing contiguous Fourier projection family.
- Every individual entropy Hessian in the finite obstruction remains negative.
  The result refutes composability and a universal sublinear replacement cost;
  it is not a counterexample to projection entropy concavity.
- The finite common-outside-frame checks remain finite checks.  The frozen
  all-rank common-frame sign question remains unresolved.

## Replay

All five exact jobs passed from a fresh output directory.  Regular and
optimized runs reconstructed identical laws and jets.  The certificate gives
strict rational log enclosures; floating diagnostics were unnecessary for the
accepted signs.

