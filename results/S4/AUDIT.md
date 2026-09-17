# S4 round 4 independent audit

## Verdict

**ACCEPTED_SCOPED.** The finite-dimensional completed-information estimate, its Gaussian-remainder corollary, and the stated extreme-density strong-concavity region are internally complete. They are suitable for integration with the exact quantifiers below. This is not acceptance of the full all-density, all-offset sine entropy-concavity target.

## ACCEPTED

1. **Completed-information payment (Theorem A).** For every finite `n`, Hermitian contraction `0 <= K <= I`, `0 < c < 1`, and interior `0 < a < 1-c`, the proof establishes
   `0 <= I_K''(a) <= kappa Psi_K <= kappa(D-F_marg)` and the sharper signed estimate `I_K'' <= kappa Psi_K-(kappa-1)E_K`.
   The proof keeps the full likelihood acceleration. The exact regrouping of the acceleration into pair log odds is correct; the DPP negative off-diagonal covariance gives the required nonnegative determinant; posterior tilting rebases the pair term to the actual full posterior; and the missing-information identity supplies the signed cancellation.
2. **Entropy Hessian consequence.** Under the same quantifiers,
   `H(DPP(aI+cK))'' <= (kappa-1)D-kappa F_marg` follows from the accepted payment and the exact conditional-channel entropy Hessian.
3. **Gaussian completion remainder (Theorem B).** For deterministic `T >= 0`, the chain-rule remainder `R_T=I(X;Y_a | F_T)` is again a completed information term for a compatible conditional DPP. Hence `0 <= R_T''` and the displayed posterior-variance bound are valid. The scalar Gaussian affinity calculation gives the accepted `exp(-T/8)` estimate. For a rank-`k` projection the stated `min{k(1-k/n), (1/2)sqrt{k(n-k)}e^{-T/8}}` specialization is correct.
4. **Extreme-density finite-volume region (Theorem C).** For every finite `n`, every Hermitian contraction with mean diagonal `r`,
   `37/40 <= c <= 959/1000`, `d=(1-c)/4`, `d <= a <= 3d`, and either `r <= 1/100` or `r >= 99/100`, the proof establishes
   `H(DPP(aI+cK))'' <= -(11/250)n`.
   The arithmetic uses only the accepted Hessian bound, convexity of `1/[x(1-x)]`, and explicit rational inequalities. Complementation correctly supplies the high-density half.
5. **Sine-rate consequence.** For fixed `rho` in `(0,1/100]` or `[99/100,1)`, the same contrast and offset band yields the strong Jensen gain `11/500` after dividing by `n` and passing to the already supplied pointwise entropy-rate limit. No derivative of the limit is assumed.

## PARTIAL

1. The accepted result covers the central half of the legal offset interval and contrasts through `0.959`; it does not cover the two outer offset quarters or all `c<1`.
2. The general completed-information estimate can have a positive entropy-Hessian upper bound at ordinary densities. It therefore does not settle the original all-density target.
3. The `T=16 log n` estimate controls only the localization remainder `I_K-J_T`; it does not pay the main `J_T` curvature outside Theorem C's region.
4. The preceding round's `delta^-5` statement remains an author claim and is not imported by this acceptance.

## CRITICAL GAPS

**None inside Theorems A-C as quantified above.** The missing all-density/all-offset argument is a gap relative to the main research target, not a defect in these scoped theorems.

## Independent verification path

- Read the full proof, including all likelihood derivatives, the scalar log-odds lemma, posterior rebasing, the Gaussian affinity calculation, and the regional arithmetic.
- Re-derived the determinant sign, the factor two in the pair payment, the missing-Fisher cancellation, and the constants in the regional comparison.
- Checked the archive manifest: all 42 declared files match.
- Ran the exact replay in a fresh output directory. Both `exact_check.py` and `moving_reference_check.py` regenerated parsed JSON equal to the frozen receipts; the frozen-evidence write guard passed.
- Numerical and finite certificates were treated as regression evidence only. Acceptance rests on the analytic proof.

