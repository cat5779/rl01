# Ordinary weak realization of a countable pure-birth continuity equation

## Frozen theorem

Let \(\Gamma\) be a countable set and \(E=\{0,1\}^{\Gamma}\) with the product Borel structure. Let \((\mu_t)_{0\le t\le1}\) be weakly continuous probability laws on \(E\). For every \(i\in\Gamma\), let
\[
a_i:[0,1]\times E\to[0,\infty)
\]
be jointly Borel, finite-valued, and zero whenever \(x_i=1\). Assume the local mean activity bound
\[
\int_0^1\int_E a_i(t,x)\,\mu_t(dx)\,dt<\infty
\qquad(i\in\Gamma)
\tag{A}
\]
and the exact cylinder continuity equation
\[
\int f\,d\mu_t-\int f\,d\mu_0
=
\int_0^t\int_E
\sum_i a_i(s,x)\bigl[f(x\cup\{i\})-f(x)\bigr]
\,\mu_s(dx)\,ds
\tag{CE}
\]
for every bounded cylinder function \(f\).

Prove or disprove that there exists a probability law \(P\) on coordinatewise càdlàg pure-birth paths \((X_t)_{0\le t\le1}\) such that:

1. \(X_t\sim\mu_t\) for every \(t\);
2. every coordinate jumps at most once;
3. for every bounded cylinder \(f\),
\[
f(X_t)-f(X_0)-\int_0^t
\sum_i a_i(s,X_{s-})
\bigl[f(X_{s-}\cup\{i\})-f(X_{s-})\bigr]\,ds
\]
is a martingale in the natural path filtration;
4. no two distinct coordinates jump simultaneously almost surely.

No invariance, amenability, equivariance, Poisson representation, pathwise uniqueness, strong solution, or factor-of-iid conclusion is requested.

## Candidate route that must be completed or rejected

For a finite \(F\Subset\Gamma\), set
\[
\alpha_i^F(t,y)
=
\mathbb E_{\mu_t}[a_i(t,X)\mid X_F=y],
\qquad i\in F,
\]
with arbitrary values on zero-probability atoms. The projected laws \(\mu_t^F\) satisfy the finite-state forward equation for these conditional pure-birth rates. One may construct the corresponding \(F\)-chain, embed its birth times in the compact product
\[
([0,1]\cup\{\infty\})^\Gamma,
\]
and take weak limits along an exhaustion \(F_n\uparrow\Gamma\). The finite chains need not be projectively consistent.

A previous candidate argument left three load-bearing details insufficiently explicit:

- passage of the martingale identities against an algebra generating the full natural history \(\sigma\)-field, with unbounded Borel rates controlled only through \(L^1(dt\,\mu_t)\);
- treatment of the atom at birth time \(0\), including recovery of the \(t=0\) marginal and identities whose history tests include time zero;
- a diagonal/closure argument showing that the limiting law solves all cylinder martingale problems simultaneously, rather than only a fixed test along a test-dependent subsequence.

Give a self-contained proof of these steps. If the compact birth-time route fails, identify the precise failure and either repair it by another ordinary superposition theorem whose hypotheses are checked line by line, or give a counterexample satisfying (A) and (CE).

## Optional DPP specialization

It is enough to prove the abstract theorem above. Alternatively, one may add the following specialization, but it must not replace the abstract hypotheses silently.

Let \(\Gamma\) be a countable group,
\[
K_t=C+tH,\qquad
\varepsilon I\le K_t\le(1-\varepsilon)I,
\]
and let \(\mu_t\) be the DPP of \(K_t\). These laws are weakly continuous and every finite pattern has positive probability. A covariant DPP birth-rate field satisfying (A) and (CE) is an intended application.

## Scope and verdict

This theorem is strictly weaker than invariant weak existence. Even a complete proof does not show that \(P\) is \(\Gamma\)-invariant for a nonamenable group. Conversely, failure of an averaging or fixed-point argument is not a counterexample to this ordinary theorem.

Return one of PROVED, DISPROVED, or INCOMPLETE, followed by a complete supporting argument. A proof must verify time measurability, all-time marginals, local integrability, càdlàg realization, the full natural-filtration martingale property, one jump per coordinate, and absence of simultaneous jumps.
