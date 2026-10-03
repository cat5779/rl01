# R18 G17 external result audit

Date: 2026-10-03 (Asia/Singapore)

Source: `randomcat4/dpp-entropy-concavity#9`, head
`9342b34c9c1442b1300be9d11859b355a5c18902`.

Audited theorem: for every fixed finite component bound `r`, kernels whose
canonical coordinate components all have size at most `r` admit one Borel,
coordinate-permutation-equivariant nonnegative selector in the original flow
fiber, with a Lipschitz constant depending only on `(epsilon,r)`, not on the
ambient dimension or number of components.

## Verdict

`PASS / CORRECT_SCOPED`.

The proof does not give a constant uniform in `r`, and therefore does not
settle the unrestricted non-diagonal selector problem.

## Checks performed

1. The unit-mass constraint is correctly recovered from exact divergence by
   pairing with configuration cardinality.
2. The local fiber has fixed constraint normals.  The nearest-point map for
   the moving right-hand side is globally Lipschitz on the feasible parameter
   domain: the active-independent-row formulas cover the domain, agree on
   overlaps by uniqueness, and a line segment crosses only finitely many
   convex regions.
3. The matrix `[-I;D;-D;O]` is totally unimodular after the stated row
   operations.  A nonsingular unit minor gives the claimed coarse
   Moore--Penrose bound.  Degenerate faces and lack of strict complementarity
   are not being hidden.
4. Coordinatewise McShane extension, finite permutation averaging, and
   projection back to the exact original fiber preserve the prescribed value
   on every disconnected stratum.  This yields exact, not approximate,
   refinement compatibility.
5. Homogeneous compression of a rank-at-most-one block of the projector
   avoids division by a vanishing block weight.  The zero-weight case and the
   trace-norm estimate for changing compressed projectors are covered.
6. Tensorization gives the exact global divergence because the resolvent is
   block diagonal and cross-block entries of the rank-one direction disappear
   under the trace.  Total mass and the original pointwise outgoing capacity
   are preserved with no component-count loss.
7. Incompatible canonical partitions are compared through the common
   refinement.  Pinching gives the `2+1+2` kernel comparison, and exact
   refinement compatibility identifies intermediate selectors correctly.
8. The induction over local component size is noncircular: the boundary at
   size `n` uses only selectors already constructed through size `n-1`.
   The displayed recurrence closes and yields the stated finite constant
   `10 epsilon^(-2) (r!)^2 2^((r-1)(r+4))`.

## Boundary

This is an internal mathematical audit of the complete 763-line proof.  It is
not a formal proof, field referee report, or novelty certification.  It does
not imply any uniform conclusion as `r` tends to infinity.

