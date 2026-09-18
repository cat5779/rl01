# Fresh independent review request

**PENDING_INDEPENDENT_REVIEW.** The author-side exact computations are not an independent proof audit. The old `SOL_REVIEW.md` does not apply to these new claims.

Please review in a fresh context, without treating the previous audit or the report's PROVED labels as conclusions.

## Principal checks

1. Check the fixed-count common-bias Ward identities, including the external posterior denominator, the factor `d=2u delta`, and the actual second mass derivative. Section 2 must not reduce the Hessian to its Fisher term.
2. Check detailed balance of the positive external generator, its explicit magnetization potential, and the Bayes covariance edge-reversal identity. In particular verify the passage from the `(1+o^{-1})/2` weight to the covariance chord in expectation.
3. Check the posterior projection argument and sharp posterior interval `|2q-1|<=c^2`, as well as `kappa_j=(1-c^2)|v_j|^2/c^2`.
4. Check the entropy Hessian row identity against full finite derivatives. The new positive budget is subtracted, not added.
5. Check the exact entropy-production integration and transitive torus approximation. Confirm that the common-gap and strong-convergence hypotheses really pay all grouped V14 double-flip tails, and that the limiting target is the specified true infinite Gamma, not a different entropy functional.
6. Independently verify the scalar chord envelope, its monotonicity, the polynomial majorant, and the Bernstein certificate. The exact endpoint is `sqrt(3)/2`; nothing at `19/20` is claimed positive.
7. Check the all-occupied reference inverse and finite Woodbury formulas. Its cylinder is evaluated under the true finite marginal, not under a law conditioned on the reference exterior. Check the pointwise resolvent error and explicit Neumann tail constants.
8. Independently rerun the rational Hadamard counterexample and verify directed logarithm enclosures. It refutes only a pointwise general-projection closure, not the expected sine sign.

## Requested classification

Report which statements are VERIFIED_SCOPED, defective, or conditional on the frozen interface. Identify any missing limit justification or arithmetic inequality precisely. Do not infer full-contrast positivity from the interval theorem. Do not merge a new review into the old audit file; write a separate review.

## Known open target

The expected chord budget below one at `c=19/20`, and throughout the remaining high-contrast interval, is still unproved. No evaluated finite cutoff certificate settles it.