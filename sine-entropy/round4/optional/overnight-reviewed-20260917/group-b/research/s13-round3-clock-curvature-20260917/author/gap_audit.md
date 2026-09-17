# Gap audit

## Paid theorem components

1. **Definitions:** actual count weights, corrected law, generator normalization,
   theta, clock, KL, entropy production, and midpoint are explicit.
2. **Full chain rule first:** all `pi_l D_l''`, `2pi_l'D_l'`, and `pi_l''D_l`
   terms are displayed before specializing or bounding.
3. **Exact midpoint simplification:** `z'(a_*)=0` proves `tau_l'=0`; cross and
   time-Hessian terms do not disappear by assumption.
4. **Clock sign:** the binomial-coefficient representation makes
   `partial_z theta` a strictly positive covariance.
5. **Uniform growing-layer asymptotic:** an exact ratio proof supplies Gaussian
   domination, normalization, moment convergence, and the explicit limit
   `-tau_l''/n -> 2/(1-c^2)` on `|l-n/2|<=n^(2/3)`.
6. **Correct averaged mode:** the proof uses an adjacent Johnson degree-two
   pair mode, whose amplitude is nonzero after input averaging. It does not use
   the vanished degree-one mode.
7. **Entropy production:** pair entropy subadditivity gives extensive slice KL;
   the reconstructed slice mLSI converts it to a uniform positive lower bound
   on `I_l`.
8. **Actual count tails:** Hoeffding gives `2 exp(-2 n^(1/3))`; all omitted tail
   summands are nonnegative.
9. **Explicit constant:** the final lower coefficient is closed-form and
   numerically evaluated for `c=19/20`.

## Unpaid steps

1. `W_n=sum_l pi_l''K_l` is not signed. The finite diagnostics show a sizeable
   negative value but do not determine its asymptotic scale or aggregate sign.
2. No theorem controls `(tau_l')^2 I_l'` away from the symmetric shift.
3. No sign is proved for `Khat_n''`, `Dhat_F''`, `Hhat''`, the actual cyclic law,
   or the true Toeplitz target.
4. The theorem is only half density, even `n`, fixed `0<c<1`, and one symmetric
   shift. It is not a compact-shift-family theorem.
5. The round-two defect/cusp/value estimates remain unreviewed; this round uses
   only the bounded reviewer gate and independently reconstructed ingredients.
6. Deterministic scripts are self-checks, not external certification.

## Next exact obligation

Determine the sign and scale of

`W_n(c)=sum_l pi_l''(a_*,c)K_l(tauhat_l(a_*))`.

A useful next theorem must either:

- prove `W_n=o(n)` or `W_n>=-alpha(c)n` with
  `alpha(c)<2D_pair(c)/(1-c^2)`, yielding a net favorable midpoint sign; or
- prove a growing-family adverse asymptotic, such as a nonzero
  `-n^(3/2)` middle-layer cusp, which would rigorously obstruct this corrected
  clock mechanism in its present form.

Freeze `h(l)=K_l(tauhat_l(a_*))`.  The exact product-derivative identity is

`W_n=2 sum_(i<j) E Delta^2 h(N_ij)`,

where `N_ij` is the count with Bernoulli sites `i,j` deleted.  The continuation
must control this complete compatibility average of layer second differences;
one central finite calculation is not enough.
