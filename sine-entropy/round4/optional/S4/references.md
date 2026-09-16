# Public primary-source audit

Accessed during this session on 2026-09-16. Only the statements below are used; none supplies a common-offset curvature sign. The proof rederives the needed special cases and then proves its own connecting correction formulas.

## [A] Entropic Independence I

Nima Anari, Vishesh Jain, Frederic Koehler, Huy Tuan Pham, Thuy-Duong Vuong. *Entropic Independence I: Modified Log-Sobolev Inequalities for Fractionally Log-Concave Distributions and High-Temperature Ising Models*. arXiv:2106.04105v2, 5 November 2021.

Version: <https://arxiv.org/abs/2106.04105v2>

Definition 2 normalizes the one-site law by the rank. Theorem 4 identifies `1/alpha` entropic independence with the upper tangent bound for `g_mu(z^alpha)^(1/(k alpha))`; it also characterizes the all-positive-external-field version. Theorem 5 assumes entropic independence for all links. At `alpha=1`, for `ell<=k-1`, its integer-parameter bound gives KL contraction `ell/k` under `D_(k->ell)`.

Theorem 4 was checked in both PDF text and a rendered page image (printed page 5); Theorem 5 was checked on printed pages 6–7, including its sharper integer-parameter formula. The artifact proves constant 1 for projection laws by determinant arithmetic–geometric mean and proves the requisite link contraction directly. It does not use a mixing-time conclusion as a Hessian estimate.

## [CE] Localization Schemes

Yuansi Chen, Ronen Eldan. *Localization Schemes: A Framework for Proving Mixing Bounds for Markov Chains*. arXiv:2203.04163v2, 6 June 2022.

Version: <https://arxiv.org/abs/2203.04163v2>

Definition 29 and Lemma 31 concern mean-displacement control by KL. Equation (27) is the fixed-function stochastic entropy drift with factor `-1/2`. Proposition 39 requires entropic stability along the whole time interval; with deterministic constant `alpha` it gives expected entropy conservation by `exp(-alpha T)`. Lemma 40 assumes `Cov(T_v nu)<=A` for every external field and gives stability constant `||CAC||` for `(1/2)||C(mean difference)||^2`.

The artifact takes `C=I`, proves the all-field projection covariance bound with `A=I/2`, and derives the finite-state entropy drift by Itô's formula. It differentiates the actual channel likelihood only after writing the complete expectation. It does not differentiate an entropy-conservation inequality as though its slack were concave. The covariance is singular on a homogeneous affine slice; the direct log-moment-generating-function proof avoids requiring an inverse covariance.

## [JPV] Entropic independence via sparse localization

Vishesh Jain, Huy Tuan Pham, Thuy-Duong Vuong. *Entropic independence via sparse localization*. arXiv:2604.10902v1, 13 April 2026.

Version: <https://arxiv.org/abs/2604.10902v1>

Definition 2.2 uses at most `ceil(s n)` coordinates. Definitions 3.1–3.2 use the operator norm of `Psi=Cov diag(Var)^(-1)` on active coordinates. Theorem 1.2 assumes base nonzero inclusion marginals at least `b` and sparse influence norm at most `alpha`, giving entropic-independence constant `2alpha/(b s)`. Theorem 1.5 gives the `+/-1` squared-mean bound `(8alpha/s) KL` under the sparse influence hypothesis.

The artifact verifies these hypotheses for its block family, including actual channel posterior tilts. The positive-pinning martingale studied in Theorem S is specified separately; it is not identified with Section 4's different signed jump scheme. Remark 4.2 cautions about a spectral-independence versus operator-norm typo in [CE, v2, Lemma 68]. That statement is not used here.

## What is not attributed to the literature

The explicit common-offset Hessian conversion, the zero-posterior-tangent/nonzero-acceleration mechanism as applied here, both exact seed correction calculations, the explicit positive-time Gaussian average bound, and the sparse block-count tensorization are proved in this artifact. No source is cited as granting their signs. No private research source, unprovided baseline file, or secondary theorem was accessed.
