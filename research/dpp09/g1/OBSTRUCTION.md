# A common-clock obstruction for oscillating pure-birth rates

## Scope

This example separates within-approximation sensitivity and convergence of forward equations from convergence on a fixed Poisson input. It does not disprove existence of a relative ordered DPP factor. It addresses the explicitly displayed conditions (17)–(18) and a weak or integrated interpretation of convergence of the finite-block forward equations in the accompanying positive-flow manuscript. An additional strong meaning of the word “approximated” would be a new hypothesis and must be stated.

## Proposition

There are scalar, uniformly gapped DPP paths, all starting from the same kernel, and bounded finite-range pure-birth rates with all of the following properties:

1. the within-approximation ordered-interval sensitivity bound holds with a common constant and zero error;
2. the path marginals converge uniformly, and their exact forward equations converge after integration in time;
3. when the processes use the same initial configuration and the same Poisson field, no subsequence of their endpoints converges in probability.

## Proof

Take the trivial group and its one-point configuration space \(\{0,1\}\). For each integer \(n\ge1\), let
\[
B_n=\{t\in[0,1):\{2^nt\}<1/2\},\qquad
\lambda_n(t)=2\mathbf1_{B_n}(t).
\]
Here braces denote fractional part. Each \(B_n\) has Lebesgue measure \(1/2\), and for distinct \(n,m\),
\[
|B_n\cap B_m|=1/4,\qquad |B_n\cup B_m|=3/4.
\]
Set \(a_n(t,x)=\lambda_n(t)(1-x)\). Start every process at the same \(X_0\sim\operatorname{Bern}(1/4)\), independently of one common Poisson random measure \(N\) with intensity \(dt\,du\). A vacant site becomes occupied at the first mark with \(u\le\lambda_n(t)\), and remains occupied thereafter.

Write \(\Lambda_n(t)=\int_0^t\lambda_n(s)\,ds\). The exact occupancy marginal is
\[
p_n(t)=1-\frac34e^{-\Lambda_n(t)},
\qquad p_n'(t)=\lambda_n(t)(1-p_n(t))
\]
almost everywhere. A scalar kernel \(K_t^{(n)}=[p_n(t)]\) has precisely this Bernoulli DPP law. Since \(0\le\Lambda_n(t)\le1\),
\[
\frac14\le p_n(t)\le1-\frac{3}{4e}<\frac34.
\]
Thus the common spectral gap can be \(1/4\). Also \(\sup_t|\Lambda_n(t)-t|\le2^{-n-1}\), so \(p_n\) converges uniformly to \(p(t)=1-\frac34e^{-t}\). The integrated forward equations converge uniformly on time intervals. More precisely, \(\lambda_n\) converges weak-* in \(L^\infty[0,1]\) to 1, and the uniform convergence of \(p_n\) implies
\[
\lambda_n(1-p_n)\ \longrightarrow\ 1-p
\]
weak-* in \(L^\infty[0,1]\). On the one-point space this verifies the forward equations for every test function, not just the occupancy test.

For every random ordered pair \(U\le V\) in \(\{0,1\}\),
\[
\mathbb E\operatorname{osc}_{[U,V]}a_n(t,\cdot)
=\lambda_n(t)\mathbb P(U\ne V)
\le2\mathbb P(U\ne V).
\]
Every such law is invariant under the trivial group. Thus the within-approximation sensitivity condition holds with \(L=2\) and \(\delta_n=0\).

For \(n\ne m\), conditional on \(X_0=0\), the Poisson acceptance sets on \([0,1]\times[0,2]\) have individual area 1 and union area \(3/2\). Consequently,
\[
\begin{aligned}
\mathbb P(X_1^{(n)}\ne X_1^{(m)})
&=\frac34\,2\left(e^{-1}-e^{-3/2}\right)\\
&=\frac32\left(e^{-1}-e^{-3/2}\right)>0.
\end{aligned}
\]
This value is independent of the distinct indices. Hence no subsequence is Cauchy in probability at the endpoint. In particular, uniform convergence of the marginals and of integrated forward equations does not yield convergence of these factors on their common input. \(\square\)

## Consequence for the proposed closure interface

The cross-index estimate (12) of the common-noise closure theorem contains an independent obligation. Taking \(U=V=0\) already forces its error term to dominate \(|\lambda_n-\lambda_m|\), whose integral is 1 whenever \(n\ne m\). The within-index oscillation estimate supplies no such vanishing error. A sufficient selection-stability statement must add a cross-index rate estimate, or another explicit common-input convergence mechanism, rather than appeal only to convergence of forward equations.

The example does not contradict the closure theorem with estimate (12), does not concern the truth of the general ordered-factor target, and does not invalidate the rank-one positive-flow identity.
