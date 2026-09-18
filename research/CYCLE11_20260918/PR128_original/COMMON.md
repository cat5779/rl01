# COMMON — requirements for the next four Web Pro tasks

## Ultimate mathematical target

For the actual sine Toeplitz kernel
\[
Q_{\rho,n}(i,j)=
\begin{cases}
\rho,&i=j,\\
\dfrac{\sin(\pi\rho(i-j))}{\pi(i-j)},&i\ne j,
\end{cases}
\]
prove, for every fixed
\[
0<\rho<1,\qquad 0<c<1,
\]
that the complete-configuration Shannon entropy rate
\[
h_{\rho,c}(a)
=\lim_{n\to\infty}\frac1n
H\!\left(\operatorname{DPP}(aI+cQ_{\rho,n})\right)
\]
is concave for the whole legal interval
\[
0\le a\le1-c.
\]

The finite Toeplitz compression is generally **not** a projection. \(\operatorname{Tr}b(K)\) is not this classical configuration entropy. A corrected cyclic law is not the true Toeplitz output.

## Current baseline and inheritance rule

At the time this package is written, the accepted universal whole-interval threshold remains \`c <= 37/40\`. Treat later independently reviewed improvements as inherited inputs if they exist at launch time.

Before doing new work:

1. read the current repository status and the newest independent reviews relevant to your task;
2. read the shared/public counterexample and failed-route area once;
3. do not re-prove an already independently accepted theorem merely because it sits on an unmerged branch;
4. do not treat an author-only claim as accepted without its review.

The shared counterexample area already records failures of pointwise pair payment, layerwise positivity, nodewise completion signs, frozen/reference shortcuts, value-to-Hessian differentiation, and general-complex-kernel concavity. Mention the relevant obstruction when needed; do not spend the round reproducing the catalogue.

## Research standard

This is a mathematical research assignment. Create a reusable mathematical tool or prove/refute a sharply stated load-bearing claim.

Acceptable outputs include:

- a full theorem that closes the stated bottleneck;
- a strictly scoped theorem that removes a real part of the remaining burden;
- an exact/model-valid obstruction that kills a proposed mechanism and identifies the surviving weaker target.

Not acceptable as the main output:

- renaming the unknown remainder;
- a generic identity equivalent to the target;
- a numerical sign scan without a proof/certificate;
- a tiny threshold improvement obtained only by tuning old constants;
- a statement that silently drops moving probability weights, probability acceleration, tails, leakage, endpoint layers, or reference-law derivatives.

Use computation when it clarifies the mathematics. Exact or interval computation may certify finite claims. Floating diagnostics are discovery evidence only.

## Finite chords are allowed and often preferred

For
\[
\operatorname{Gap}_{\lambda}F
=F((1-\lambda)a_0+\lambda a_1)
-(1-\lambda)F(a_0)-\lambda F(a_1),
\]
a finite-volume result
\[
\operatorname{Gap}_{\lambda}H_n\ge-o(n)
\]
combined with an already justified value-limit bridge can prove the corresponding entropy-rate concavity statement. You do not have to prove \(C^2\) regularity if a rigorous finite-chord route is cleaner.

## Default benchmark

Unless your task says otherwise, begin at
\[
\rho=\frac12,\qquad c=\frac{19}{20},
\]
and use a fixed nondegenerate legal \(a\)-interval such as
\[
\left[\frac1{50},\frac3{100}\right].
\]

A midpoint-only statement is not a fixed-interval statement. A fixed-\(n\) continuity argument does not create a volume-uniform interval.

## Delivery

Return a readable proof before optional packaging. For every new claim state:

- \`PROVED\`, \`DISPROVED\`, or \`INCOMPLETE\`;
- exact hypotheses and quantifiers;
- what prior reviewed inputs are used;
- where the new argument enters the target ledger;
- what remains unpaid.

Do not merge your own work or edit repository-wide status files.
