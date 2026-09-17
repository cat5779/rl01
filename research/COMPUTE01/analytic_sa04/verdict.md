# Current verdict

- Frozen theorem `d_k>=epsilon`: **INCOMPLETE AND NOW NUMERICALLY DISFAVORED**.
- Strict sublemma `A_k>=c^4/72` and
  `liminf A_k>=2c^4/9>0.1810`:
  **PROVED_HERE, PENDING_INDEPENDENT_REVIEW**.
- Smallest scale obstruction: prove `|A_l-E_l|<=K/sqrt(n)` throughout the
  expanded central window.  The older attempt to bound `E_k` below the constant
  `2c^4/9` is contradicted by the finite diagnostics and is no longer the target.
- The clock-gap asymptotic is settled: its mean jump count tends to `1/2`, so
  vanishing raw time does not remove the entropy-cost obstruction.
- A bound using only the initial entropy dissipation is too crude on current
  exact diagnostics.  Further work should analyze the complete Poissonized
  finite-exchange channel, not extrapolate the derivative at the left endpoint.
- Paired MCMC at `n=40,60,80` estimates the actual central increments as
  `0.7588+/-0.0112`, `0.6779+/-0.0141`, and `0.5714+/-0.0161`.
  Their inverse-root rescalings are `4.80,5.25,5.11`; this supports eventual
  positivity and the `n^-1/2` line, while disfavoring a constant positive lower
  bound.  Comparison against the weak constant `2c^4/9` is also the wrong closure.
- The follow-up values `sqrt(n)d_k=4.32+/-0.18` at `n=100` and
  `4.18+/-0.22` at `n=120` reinforce the inverse-root scale but show that the
  apparent `5.1105` constant at `n=80` was not stabilized.
- At `n=100`, offsets `2,4,6,8` give the bounded rescaled window profile
  `6.98,6.19,5.18,4.32`.  This is the first direct evidence for the version-2
  window theorem, not only its central-layer specialization.
- Research value: the sublemma rules out vanishing of the deletion mechanism
  itself, while the new scaling data show that cancellation with the clock term
  is likely accurate to inverse-root order.
