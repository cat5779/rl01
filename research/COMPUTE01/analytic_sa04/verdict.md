# Current verdict

- Frozen theorem `d_k>=epsilon`: **INCOMPLETE**.
- Strict sublemma `A_k>=c^4/72` and
  `liminf A_k>=2c^4/9>0.1810`:
  **PROVED_HERE, PENDING_INDEPENDENT_REVIEW**.
- Smallest remaining obstruction: prove an explicit upper bound on the actual
  central reverse-clock cost `limsup E_k` below `2c^4/9`,
  or strengthen the witness until it dominates the sharp `E_k` estimate.
- The clock-gap asymptotic is settled: its mean jump count tends to `1/2`, so
  vanishing raw time does not remove the entropy-cost obstruction.
- A bound using only the initial entropy dissipation is too crude on current
  exact diagnostics.  Further work should analyze the complete Poissonized
  finite-exchange channel, not extrapolate the derivative at the left endpoint.
- Paired MCMC at `n=40,60` estimates the actual central increments as
  `0.7588+/-0.0112` and `0.6779+/-0.0141`.  This supports the original positive
  increment conjecture while confirming that comparison against the weak
  constant `2c^4/9` is the wrong closure.
- Research value: the sublemma rules out vanishing of the deletion mechanism
  itself and localises all possible cancellation in the clock term.
