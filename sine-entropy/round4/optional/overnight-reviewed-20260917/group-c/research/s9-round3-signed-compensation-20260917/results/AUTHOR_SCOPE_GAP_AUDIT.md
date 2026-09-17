# Author scope and gap audit

This is an author audit, not independent peer review. The new proofs are
submitted for separate reproduction and mathematical review.

## Hypotheses checked

The main law uses the actual stationary Toeplitz kernel with the degree-R
Fejer symbol, not a cyclic replacement or a projection compression. At half
density R is odd so its literal degree is R. The general-density extension
states the exact-degree subsequence instead of assuming the top coefficient
never vanishes. Contrast is fixed strictly below one, the base shift is
strictly interior, and all radius-dependent and noise-dependent perturbations
are displayed. Constants are not uniformly passed to an endpoint.

The external count has 2R sites; the complete center window has 2R+1 sites;
the localization block has r+1 sites. These three lengths are never identified.
The production is `E phi(q_R)` with complete exterior-word probabilities.
Scalar count diagonalization is used only for the conditional count estimate.

## Proof risks explicitly paid

* Conditional rare words: the conditional kernel rank and trace comparisons
  hold for every word; no inverse-probability or high-probability omission is
  used. Strict strips ensure all relevant complete-event matrices are invertible.
* Moving full predictor: first replace q_R by the predictor in a local context
  under the SAME degree-R process. The integrated Bregman estimate pays the
  difference, and only then is a conditional count CLT multiplied by its
  actual local production weight.
* Changing Fejer kernel and original shift: full-production stability is used
  only after local-to-full comparison, with the explicit `2b(c eta_R+T/sqrt R)`
  modulus. It is not asserted for an isolated finite-center contribution.
* Derivatives: the complex complete-event bound controls the sum of absolute
  complex probabilities by `exp(u^2(Im theta)^2/epsilon^2)`, independently of
  R at the critical scale. Normal-family uniqueness and Cauchy's formula pay
  differentiation. A separate score proof retains `a g+2s g'+g''` and checks
  all three terms. Real value convergence is not used as Hessian convergence.
* Full-law likelihood: the spectral observation channel is fixed in the
  parameter and count preserving, but not entropy preserving. The KL estimate
  uses log-sum/data processing, not a substitution of spectral entropy.
* Count tails: fourth moments control the unbounded quadratic test in the
  score proof; interval boundaries have no limiting Gaussian mass.
* Noise endpoint: all error integrals retain powers of u. The omitted lower
  interval costs at most `M_c/[2(R+1)^2]`; no logarithmic divergence is hidden.

## Exact outcome versus stronger unsupported statements

PROVED (subject to review): weighted critical-scale Gaussian limit, explicit
signed martingale compensation, actual midpoint band curvature and its
complement, finite full-law score/acceleration/KL bounds, and the stated
strict-interior general-density extension.

NOT PROVED: an explicit eventual radius for the new `1/140` inequalities;
nonnegative full production curvature; monotonicity of that curvature with
context or Fejer degree; the order-one next term; fixed-chord sine concavity;
any new all-shift contrast threshold; uniformity as c tends to one; or a
thermodynamic Hessian obtained from an entropy value limit.

The exact R3 baseline and its old certificates were read but not replayed or
claimed as new output. The previous `R>=160001` number belongs to a different
fixed-chord negative-band theorem and is not a threshold for this result.

## Checks and adverse evidence

`verify_exact_identities.py` checks exact finite atoms, first/second mixture
jets, the fixed-channel identities, and rational constants. It verifies the
four-site field obstruction using rational data and elementary logarithm
bounds. These finite checks support algebra, not the asymptotic proof.

Complete-atom floating quadrature at c=19/20 and radii 3,5,7 gave positive
central-band second derivatives approximately 2.203, 4.912, 5.168 for the new
half-sqrt(R) band. Thus these radii are NOT witnesses for the eventual
negative-band theorem. The values are preserved in the diagnostic receipt.
The theoretical proof only asserts an eventual sign. Sixteen quadrature
nodes are not an interval or exact certification of the integral.

The growing bistochastic-channel counterexample is not a DPP channel; the
failure of common-unitary compatibility is proved. It also fails deletion
intertwining, so it does not refute bridges assuming that stronger property.
The Fourier field counterexample concerns a nonlinear external-field path;
it does not contradict the actual affine-shift sign.

## Remaining mathematical obligation

After the leading order-R positive/negative terms cancel, a signed estimate
on the complete subleading aggregate is still required. At a critical chord,
the relevant value scale is 1/R. The reviewed interior value error is not
smaller than that scale. A complete continuation must either control the
subleading signed term with the common-minor compatibility retained, or prove
a fixed nonshrinking-chord inequality and use the existing value bridge.
Neither obligation is declared discharged here.
