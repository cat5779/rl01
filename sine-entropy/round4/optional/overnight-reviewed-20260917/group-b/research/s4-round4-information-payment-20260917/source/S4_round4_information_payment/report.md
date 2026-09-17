# Research report — new completed-information payment

## Outcome

A new complete scoped analytical theorem controls the actual information curvature lost under Gaussian localization. Its separately evaluated Fisher budget gives a new percent-density strong-concavity region for the **true** sine entropy rate. It does not solve the full target. The proof is an author result with exact self-reproduction, not an independently certified result.

## What changed in the method

The previous author theorem estimated an instantaneous Gaussian curvature Q_t'' with a delta^-5 MMSE cost. This round completes the information experiment first and combines the unnormalized acceleration with the off-diagonal part of missing Fisher information before estimation.

Let X~DPP(K), Pr(Y_i=1|X)=a+cX_i, and e_u=c/[g_0(u)g_1(u)]. Write C_Y=Cov(X|Y). The new cost is

    Psi=E_Y sum_i e_(Y_i)^2 (C_Y)_ii.

It is positive even when the sum-score tangent variance vanishes at the homogeneous midpoint. Define

    D=sum_i {(1-K_ii)/[a(1-a)] + K_ii/[(a+c)(1-a-c)]},
    F_marg=sum_i 1/[(a+cK_ii)(1-a-cK_ii)].

The result is

    0 <= I(X;Y_a)'' <= kappa Psi <= kappa(D-F_marg),
    H(DPP(aI+cK))'' <= (kappa-1)D-kappa F_marg.

The constant kappa is explicit and independent of n. It is the minimum of (1-c^4)^(-1/2), theta/(1-exp(-theta)) with theta=log[(a+c)(1-a)/(a(1-a-c))], and 2 when c^2<=23/25.

The useful signed identities are

    I''=A+E,       E=Psi-2S,
    A=2 sum_(i<j) E_(Y_-ij) log[p01 p10/(p00 p11)],
    S=E_Y sum_(i<j) e_(Y_i)e_(Y_j) |(P_Y)_ij|^2.

Here the four probabilities are actual conditional output probabilities. A scalar log-mean bound followed by an exact two-site Bayes rebase gives A<=2kappa S. Therefore I''<=kappa Psi-(kappa-1)E. Every term has a verified relation to the actual channel Hessian; no mixing or KL contraction statement is differentiated into an assumed sign.

## Gaussian localization theorem

Use Z_t=tX+B_t with standard independent Brownian motion and deterministic stopping T. Let J_T=I(Y;Z_[0,T]) and R_T=I(X;Y)-J_T. The Gaussian reference law is a positive DPP field independent of a. The output weights and posterior after Y vary with a and are differentiated fully in the proof.

The new completed remainder satisfies

    0 <= R_T'' <= kappa c^2/tau_min^2
                    min{V(K),0.5 sqrt(nV(K)) exp(-T/8)}.

For a rank-k projection V(K)<=k(1-k/n); for genuine contiguous P_(n,k), equality holds. For Q_n, V(K)=n rho(1-rho). This is a uniform growing-family result, not a block-product extrapolation.

On a compact interior interval, T_n=16log n gives O(n^-1) unnormalized remainder curvature and the corresponding integrated Jensen error. The remainder is only R_T: the main information curvature J_T is not thereby paid at ordinary densities. No nonpositivity of J_T'' or instantaneous Q_t'' is asserted.

## Explicit region that pays the whole entropy curvature

For every finite contraction K with TrK/n<=1/100 or >=99/100, every 37/40<=c<=959/1000, and

    (1-c)/4 <= a <= 3(1-c)/4,

one has H''<=-(11/250)n. The proof uses the factor-two theorem and scalar Fisher bounds, with the rational uniform product estimate (1+2r)(1+95r)<=1989/1000.

For Q_n this holds for every n at the stated fixed densities. Integrating first and passing to the entropy-rate value limit gives the strong Jensen gain

    (11/500) lambda(1-lambda)(a1-a0)^2.

In particular rho=.01, c=.95, a in [.0125,.0375] is covered. This is substantially beyond the preceding author's explicit rho=10^-11 example and outside its displayed delta^5 entropy criterion. It does not prove the outer offset quarters, middle densities, or all c<1.

## Evidence and review boundaries

The exact standard-library rebuild covers 16 DPP fixtures, 1,562 actual pair/extrinsic calculations, and 6,248 compatible posterior rebasings. Two additional exact finite experiments verify changing-reference Fisher terms and both posterior responses away from the midpoint. The scalar inequality and the parameter region are proved on their continua, with rational arithmetic certificates for the constants.

Larger contiguous projections, true Toeplitz blocks, and Gaussian samples are floating diagnostics only. The old positive-excess gate remains positive and satisfies the new bound. The non-DPP gate is excluded by a demonstrated positive covariance, rather than silently treated as a DPP. None of these finite diagnostics supplies a thermodynamic proof.

The mandatory public packet and exact primary theorem statements were read. The archive restates imported definitions, records the author-versus-reviewed distinction, and does not depend on an unavailable proof from any other route. The code reproduces frozen evidence into a separate output directory and compares parsed JSON across LF/CRLF conventions.
