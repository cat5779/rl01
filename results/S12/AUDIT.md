# Independent audit of S12

**STATUS: ACCEPTED (scoped).**  Both exact witnesses are valid route
counterexamples.  Neither is an entropy-concavity counterexample.

## Accepted statements

1. The coordinate-bias generators commute and square to zero.  Direct
   differentiation of complete configuration entropy gives the submitted
   diagonal and mixed Hessian formulas.  Grouping a conditioned two-site face
   cancels the outside normalization and yields
   `Phi=(ad-bc) sum(1/q)-log(ad/bc)`.
2. At `c=463/500`, `a=37/1000`, the stated rational matrix `Q` is a strict
   positive contraction and its two-site DPP cells are `(3,2,8,4)/17`.  Hence
   `H_12=log(4/3)-29/102>1/714`.  Coordinate direct sums give
   `2 sum_(i<j)(H_ij)_+>n/714`, while the common-shift curvature of each block
   remains negative.
3. For `Q=(1/100)I`, the complete DPP law is product Bernoulli with
   `p=a+c/100`.  On the full centered strip of half-width `1/200` at the
   benchmark contrast,
   `(1/n) partial_c partial_a^2 H=q(1-2p)/(p^2(1-p)^2)>560/169`.

## Scope limits

- The first witness refutes `H_ij<=0` and an unqualified nonpositive aggregate
  mixed-term route.  Negative diagonal terms still dominate its total shift
  curvature.
- The second witness refutes a free nonpositive fixed-`a` contrast-response
  sign.  It does not preclude a quantitative positive response budget.
- The total-correlation convexity inequality isolated in the author proof is
  neither proved nor disproved.  Deterministic searches with no violation are
  diagnostics only.

## Replay

The exact rational certificate rebuilt byte-for-byte after removal of labelled
floating fields.  Deterministic diagnostics replayed within their stated
tolerance, and the 46-file source manifest passed.  Only the exact certificate
is used for the accepted claims.

