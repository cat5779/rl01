# Gap audit

## Overall status

`DISPROVED_ROUTE_LEMMA` applies to the explicit Gaussian-completion and sparse-slack closures below. It does not apply to the sine-kernel target, to the cited papers, or to every possible use of localization.

The quantifier “for every projection” in a universal route inequality is refuted by the displayed family. No claim is made that this family is a model for the contiguous Fourier projection when its dimension grows.

## Complete scoped proofs

Theorem G holds for every integer `m>=1`, dimension `n=4m`, rank `k=2m`, fixed `c=19/20`, fixed `a=1/40`, and every deterministic stop `0<T<=T0`, where `T0=1/16837989787238400000000`. For isotropic Gaussian observation of the fixed input, the fully averaged completion excess is strictly greater than `2mT`. Its normalized-posterior common-offset Fisher energy is exactly zero.

Theorem S holds for the same family and channel point, with `ell=m` uniformly sampled occupied pins. Its fully output-averaged entropic-independence slack has second derivative `m^2 delta0/(2m-1)>3n/8`. Its posterior Fisher energy and down-contraction Fisher deficit are zero.

The following are also proved in the artifact, but are supporting facts rather than claimed new concavity results: the channel entropy-functional conversion; the general two-moving-laws, moving-weight KL Hessian formula; the exact external-field projection formula; entropic-independence constant 1 under all required projection tilts and links; the covariance bound under all positive fields; the stationary-posterior midpoint identity; and the sparse-pinning entropy-value contraction.

## Exact failed inequalities

For the Gaussian scheme and the specified reference coupling, define

```text
R_T = H_mu'' - E_Z H_pi_T'',
E_T = integral_0^T E_Z sum_y p_t,y sum_A (partial_a nu_t,y(A))^2/nu_t,y(A) dt.
```

The original Hessian acceleration also has `41.123540034652<A<41.123540034653` at the seed while `E=0`, so `A<=C E` fails directly. The universal claims `R_T<=0` and `R_T<=C E_T` are false for any finite `C`, even if it is allowed to depend on the dimension. They fail after the complete path/output average, not merely on a rare conditional branch.

For occupied pinning define `Phi_ell=I(X;Y)-(k/ell)I(J_ell;Y)` and let `E` and `E_ell` be the full and down-projected normalized-posterior tangent energies. The claims

```text
Phi_ell'' <= 0,
Phi_ell'' <= C E,
Phi_ell'' <= C [E - (k/ell) E_ell]
```

are false for any finite `C`. The counterexamples do not say that `Phi_ell<0`; its entropy-value nonnegativity is retained.

These closures are concrete ways of trying to turn the applicable entropy-conservation/contraction theorem into a common-offset Hessian sign. They are not consequences asserted in the cited literature. The rejected conversion, rather than the input entropy theorem, is the new issue identified here.

## Hypotheses and derivatives audited

All output probabilities come from the full product channel, differentiated as products. The seed has six exact projection input atoms and all 16 outputs. No affine-atom approximation is made. All work is in the strict legal interior.

The Gaussian reference distribution is independent of `a` by construction: the input and Gaussian observation mechanism are fixed. This makes its parameter derivatives zero legitimately. The output weights and normalized channel posteriors still depend on `a`; all three types of terms in equation (23) are retained. Separately, equation (4) and the nonmidpoint noisy-coordinate exact test retain the derivatives of a genuinely changing posterior reference.

In the Gaussian DPP posterior, the isotropic quadratic term is constant on the homogeneous support. Arbitrary nondiagonal quadratic localizations are not claimed to preserve projection DPPs. At finite time all external fields are positive, although not uniformly bounded.

Along occupied pinning, only feasible branches are used, residual rank is reduced correctly, and pinned-site output entropies are included. The law of the ordered pinning schedule is input-dependent in exactly the prescribed uniform-within-input way; its marginal law is independent of `a` because the input law is fixed.

The sparse condition is the operator norm of `Cov diag(Var)^(-1)` on active coordinates, not a spectral-radius substitute. The bound is proved for the required family of at most `ceil(n/4)` signed pins. For this particular bounded-block family it even survives all pins and positive fields, but that stronger fact is established, not assumed as a generic sparse-localization hypothesis.

A dimension-independent inclusion-marginal lower bound is computed for the actual channel posteriors at the certified point. It is not claimed for the unbounded Gaussian tilts. Entropic-independence constant 1 and the quadratic stability argument used on the Gaussian path do not need such a lower bound.

## Exact finite certificate versus analytical extension

The rational seed probability and derivative calculations, log-linear identities, strict sign enclosures, zero first derivatives, and moving-reference checks are exact finite arithmetic.

The finite-time Brownian conclusion additionally requires the written analytical proof: a uniform Lipschitz bound over all six-state priors, Itô isometry, and the explicit stopping bound. The certificate records those constants, but does not mechanically verify stochastic calculus.

The all-`m` conclusions require the written tensorization arguments. A floating `m=2` diagnostic is not the source of the all-dimension theorem.

The negative actual entropy Hessian is exactly certified. Its decimal approximation, if displayed, is only an illustration of the enclosing rational intervals.

## What remains unresolved

Nothing here controls the sign of the full common-offset Hessian for the growing contiguous Fourier projections. No new fixed-density Jensen estimate transfers through the supplied Fourier–Toeplitz value bridge. No derivatives of the limiting entropy rate are taken.

A possible successful estimate may retain output Fisher information, unnormalized-likelihood Dirichlet terms, posterior acceleration, or an explicit signed accumulation over a different localization schedule. These results do not prove that such an estimate is impossible. They show that the specified zero/tangent-only closures are impossible, even under the full favorable projection entropic-independence hypotheses.

The time `T0` is extremely small. Its role is to make the globally averaged obstruction rigorous at an explicit positive time; no claim is made that this provides a useful mixing-time scale. No long-time sign is proved.

The increasing-rank family is a product of four-site blocks. This is a fixed-density **method obstruction**, not fixed-density progress on the sine target. It is not covered by the supplied size-at-most-two block baseline, and the new positive correction estimates do not follow from that baseline. The supplied Fourier endpoint obstruction to branchwise completion is not reused as a proof: the present obstruction is at a fixed interior point, with Gaussian path averaging and a separately computed sparse-pinning average.

## Certification and uncertainty

The proofs are complete as mathematical arguments within the stated scope; the artifact is not independently certified. The only floating calculations are labeled diagnostics. There is no numerical-to-exact promotion without a rational or analytical argument, and no conjectural lemma is inserted into Theorems G or S. The substantive remaining uncertainty is whether independent review will find an error, and the entirely open target-level compensation step.
