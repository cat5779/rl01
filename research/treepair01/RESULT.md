# DISPROVED

The frozen five-state splitting class cannot have the required Bernoulli\((1/2)\) lower marginal.  The contradiction already appears on two adjacent stars and uses neither reflection symmetry, the choice \(\theta=1/4\), nor any global one-endedness assertion.

## 1. One-edge parameters and single-star constraints

Write \(\theta=q(b+)\).  The frozen one-edge equations give

\[
q(b-)=\frac12-\theta,qquad
q(u+)=\frac13-\theta,qquad
q(u-)=\theta-\frac16,qquad q(0)=\frac13.
\]

The Bernoulli lower marginal assigns probability \(1/8\) to the event that all three edges of a fixed star belong to \(B\).  On an A-star, cyclic invariance and the unique-\(+\) constraint therefore give, for a specified incident edge \(e\),

\[
P_A(\hbox{all three are }b, e=b+)=\frac1{24},qquad
P_A(\hbox{all three are }b, e=b-)=\frac1{12}.
\]

On a B-star the unique sign is \(-\), so the two values are interchanged:

\[
P_B(\hbox{all three are }b, e=b+)=\frac1{12},qquad
P_B(\hbox{all three are }b, e=b-)=\frac1{24}.
\]

The all-vacant lower-star event also has probability \(1/8\).  At an A-star its unique \(+\) must then be carried by a \(u+\) edge, hence

\[
3q(u+)\ge\frac18.
\]

At a B-star the analogous inequality is \(3q(u-)\ge1/8\).  Consequently

\[
\frac5{24}\le\theta\le\frac7{24}. \tag{1}
\]

## 2. The adjacent-star five-edge event

Take adjacent vertices of types A and B, with shared edge \(e\).  The union of their stars contains five distinct edges.  By the defining splitting formula, the probability that all five lower edges belong to \(B\) is

\[
\begin{aligned}
S(\theta)
&=\frac{(1/24)(1/12)}{q(b+)}
 +\frac{(1/12)(1/24)}{q(b-)}\\
&=\frac1{576\theta(1/2-\theta)}. \tag{2}
\end{aligned}
\]

On the interval (1),

\[
\frac{35}{576}
\le \theta(1/2-\theta)
\le \frac{36}{576},
\]

and therefore

\[
\frac1{36}\le S(\theta)\le\frac1{35}. \tag{3}
\]

But five distinct iid Bernoulli\((1/2)\) edges must all be occupied with probability

\[
2^{-5}=\frac1{32}.
\]

Since \(1/35<1/32\), (3) contradicts the required lower marginal.  Thus no tables \((q,P_A,P_B)\) in the frozen splitting class can realize the target coupling.

## 3. General lower density

The same calculation can be recorded for iid Bernoulli\((p)\), \(0<p\le1/2\).  Put \(\theta=q(b+)\).  Then

\[
q(b-)=p-\theta,quad q(u+)=\frac13-\theta,quad
q(u-)=\frac13-p+\theta,quad q(0)=\frac13.
\]

The probability supplied by the splitting law for the five-edge all-\(B\) event is

\[
S_p(\theta)=\frac{2p^7}{9\theta(p-\theta)}.
\]

Matching the required iid value \(p^5\) forces

\[
\theta\in\left\{\frac p3,\frac{2p}3\right\}.
\]

The single-star all-vacant event then requires

\[
1-2p\ge(1-p)^3,
\]

which, for \(0<p\le1/2\), is equivalent to

\[
p\le\frac{3-\sqrt5}{2}.
\]

Hence the same splitting class is impossible for every
\(p>(3-\sqrt5)/2\).  No assertion is made at the critical value or below it.

## 4. Scope

This is an exact finite-cylinder obstruction to the frozen conditional-independence class only.  It does not rule out an arbitrary \(\Gamma\)-invariant monotone coupling, does not bound \(p_{\mathrm{inv}}\) or \(p_{\mathrm{iid}}\), and does not address factor realization.
