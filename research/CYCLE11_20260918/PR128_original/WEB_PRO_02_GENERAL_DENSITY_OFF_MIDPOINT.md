# WEB_PRO_02 — Ordinary density and off-midpoint true-law theorem

Read [COMMON.md](COMMON.md) first.

## Why this task exists

Most hard-progress infrastructure is concentrated at half density and the balanced shift. The final theorem is for every fixed
\[
0<\rho<1,\qquad 0<c<1,
\]
and the entire legal \(a\)-interval.

Do not spend this round proving another half-density midpoint lemma.

## First benchmark

Use
\[
\rho=\frac13,\qquad c=\frac{19}{20},\qquad
a\in\left[\frac1{50},\frac3{100}\right].
\]

Work first with the finite cyclic projection if an exact projection identity is essential, then pay the transfer to the true sine Toeplitz law. If a reviewed general-density true-law bridge already exists at launch time, inherit it.

For a projection input \(Q\), the output kernel
\[
K=aI+cQ
\]
satisfies the exact quadratic relation
\[
K^2-(2a+c)K+a(a+c)I=0.
\]
At half density/balance several odd or centered terms vanish. At ordinary density or off midpoint they do not.

## Single objective

Create a weighted Ward / posterior / conditional-table identity that retains the **two unequal channel noises** and the nonzero bias terms, and use it to prove a new true-law interval theorem at the benchmark above.

The desired conclusion is either
\[
H_n''(a,c)\le-\varepsilon n+o(n)
\quad\text{uniformly for }a\in I,
\]
or the corresponding finite-chord inequality.

The new mechanism must expose exactly which terms disappear only at half density and how they are paid away from it.

## Required generality

Keep \(\rho,c,a\) symbolic for as long as practical. A benchmark theorem at \(\rho=1/3,c=.95\) is acceptable as the first closure, but the derivation should identify the parameters controlling extension to arbitrary fixed \(\rho\in(0,1)\).

If the method uses a cyclic projection identity, explicitly separate:

- projection-exact terms;
- finite Toeplitz leakage;
- the value/chord or curvature transfer used to reach the true sine law.

Do not call the finite Toeplitz compression a projection.

## Useful mechanism seeds

You may try:

- a biased exchangeable-pair / Stein identity with the correct nonzero score mean;
- a two-noise posterior normalization rather than the balanced \(b=(1-c^2)/4\) normalization;
- a conditional-table moment problem whose constraints depend on the actual density;
- a decomposition that couples a density-complement pair instead of requiring exact half-density symmetry.

Any imported tool must be proved for the actual law used here.

## Hard exclusions

Do not:

- infer the result from particle-hole symmetry at \(\rho=1/2\);
- freeze a reference law whose \(a\)-dependence contributes at second order;
- use count entropy or \(\operatorname{Tr}b(K)\) as the target Shannon entropy;
- treat a midpoint sign plus fixed-\(n\) continuity as a volume-uniform interval.

## Success criterion

Best: a genuine ordinary-density, fixed-width, high-contrast true-law theorem.

Useful partial: a new exact ordinary-density identity plus a dimension-consistent signed inequality that removes one of the extra off-midpoint terms and clearly states the one remaining term.

A generic counterexample outside the sine/projection observation geometry does not refute the requested theorem; label it only as a mechanism obstruction.
