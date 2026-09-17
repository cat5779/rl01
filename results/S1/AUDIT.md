# Independent audit of S1

**STATUS: PARTIAL.**  The new actual-output tail theorem is correct in its
stated scope.  Its use as an entropy-curvature reduction depends on a preserved
check-1 identity that this new-claim audit did not certify.

## Accepted statements

1. For a positive definite `L` with `mI<=L<=MI`, the normalized conditioned
   pair correlations used in the submission are bounded by
   `((kappa-1)/(kappa+1))^2`, and each relevant normalized row-square sum is at
   most `kappa-1`.  The proof correctly applies the spectral bounds to Schur
   complements and inverse principal matrices.
2. For the even-size contiguous rank-`n/2` Fourier projection at `c=19/20` and
   `a in [1/50,3/100]`, the submitted output `L`-ensemble formulas are valid and
   `kappa<=4753/3`.  The actual outside count is the stated equal mixture of two
   sums of independent binomials.  Conditioning on the input value at the
   removed site shifts the mean by exactly `+-c/2`, so the Bernstein tail (6.6)
   follows without replacing the spatial output law by a product law.
3. The pointwise constants imply (7.3)--(7.7) by multiplication with that
   actual count-tail probability.  With the explicit `u_(n,gamma)`, the
   exponent is at least `gamma log n`, so the total tail is
   `O(n^(1-gamma))` for every fixed `gamma>1`.

## Scope withheld

- The preserved check-1 all-odds identity, including its identification of the
  submitted star variables with `H_n''`, was not a new result in this packet and
  has no independent reviewed counterpart on the pinned main baseline.  This
  audit therefore accepts the new tail theorem as a standalone conditional
  component, not the full curvature decomposition.
- Even granting that identity, the count-central band carries probability
  tending to one and has no sign estimate.  The packet proves neither
  `H_n''<=o(n)` nor a finite or limiting Jensen inequality.
- The finite `n=4,6,8,10` regression checks implementation consistency only.

## Replay

`code/verify_constants.py` and `code/verify_fourier_tail.py` both passed in the
fresh review environment.  High-precision constants agree with the preserved
JSON.  The written Bernstein and matrix inequalities, rather than the finite
regression, support the accepted general statement.

