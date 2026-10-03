# Frozen problem

Let \(X_1,X_2,\ldots\) be independent and identically distributed real random variables, and let \(h:\mathbb R^2\to\mathbb R\) be a symmetric Borel-measurable kernel. Assume that
\[
\theta=\mathbb E h(X_1,X_2)
\]
is finite. Define the centered kernel and its first Hoeffding projection by
\[
\bar h(x,y)=h(x,y)-\theta,
\qquad
g(x)=\mathbb E[\bar h(x,X_2)].
\]
Let
\[
0<\sigma_1^2=\mathbb E g(X_1)^2<\infty.
\]

For \(n\ge3\), define
\[
U_n=\binom n2^{-1}\sum_{1\le i<j\le n}h(X_i,X_j),
\]
\[
q_i=\frac1{n-1}\sum_{\substack{1\le j\le n\\j\ne i}}h(X_i,X_j),
\qquad
R_n^2=\frac{4(n-1)}{(n-2)^2}\sum_{i=1}^n(q_i-U_n)^2.
\]
On \(R_n>0\), let
\[
T_n=\frac{\sqrt n\,(U_n-\theta)}{R_n}.
\]
For definiteness, set \(T_n=0\) on \(R_n=0\); equivalently, all positive-threshold events require \(R_n>0\). This convention prevents undefined ratios and does not supply an extra regularity assumption.

The theorem immediately preceding the ICM question assumes that for some \(c_0>0\),
\[
\bar h(x_1,x_2)^2
\le c_0\bigl[\sigma_1^2+g(x_1)^2+g(x_2)^2\bigr]
\tag{D}
\]
for all \(x_1,x_2\) in the stated pointwise sense. The problem is to remove (D), not to replace it by an unstated analogue.

Prove or disprove that, under only the hypotheses above, both conclusions always hold:

1. For every deterministic sequence \(x_n\to\infty\) with \(x_n=o(n^{1/2})\),
   \[
   \log\mathbb P(T_n\ge x_n)\sim-\frac{x_n^2}{2}.
   \]

2. If in addition \(\mathbb E|g(X_1)|^3<\infty\), then
   \[
   \frac{\mathbb P(T_n\ge x)}{1-\Phi(x)}=1+o(1)
   \]
   uniformly for \(x\in[0,o(n^{1/6}))\), where \(\Phi\) is the standard normal distribution function. Concretely, this means uniformity on every deterministic range \(0\le x\le b_n\) with \(b_n/n^{1/6}\to0\).

The distribution of \(X_1\) and the kernel \(h\) are fixed before \(n\to\infty\). A proof must establish both conclusions. A counterexample to either conclusion disproves the ICM question, but must satisfy every frozen hypothesis. Finite experiments alone cannot decide these asymptotic statements.
