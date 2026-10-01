# Independent audit of the oscillating-rate example

STATUS: CORRECT

## Verification

For $n<m$, each component interval of $B_n$ has length $2^{-n-1}$, which is an integer multiple of the period $2^{-m}$ of $\mathbf 1_{B_m}$. Exactly half of each such component lies in $B_m$. Hence

\[
|B_n|=\frac12,\qquad |B_n\cap B_m|=\frac14,\qquad
|B_n\cup B_m|=\frac34.
\]

The rate satisfies $0\le \lambda_n\le2$, $\int_0^1\lambda_n=1$, and its primitive obeys

\[
0\le \Lambda_n(t)-t\le 2^{-n-1}.
\]

Consequently $p_n(t)=1-\frac34e^{-\Lambda_n(t)}$ is the exact occupied-site probability of the stated pure-birth process and converges uniformly to $p(t)=1-\frac34e^{-t}$. Moreover

\[
\frac14\le p_n(t)\le 1-\frac{3}{4e}<\frac34,
\]

so every scalar DPP kernel $K_t^{(n)}=[p_n(t)]$ has the common two-sided spectral gap $1/4$, including at the endpoints.

For any dyadic step function $h$, $\int h(\lambda_n-1)=0$ for all sufficiently large $n$. Dyadic step functions are dense in $L^1[0,1]$, while $\|\lambda_n-1\|_\infty\le1$; therefore $\lambda_n\rightharpoonup^*1$ in $L^\infty$. Uniform convergence of $p_n$ then gives

\[
\lambda_n(1-p_n)\rightharpoonup^*1-p.
\]

For an arbitrary test function $f:\{0,1\}\to\mathbb R$, the forward-equation right-hand side is

\[
(f(1)-f(0))\lambda_n(t)(1-p_n(t)),
\]

so the claim covers every test function on the one-point configuration space. Its time integral converges uniformly in the upper endpoint because it equals

\[
(f(1)-f(0))(p_n(t)-p_n(0)).
\]

For every ordered random pair $U\le V$, the interval oscillation is exactly $\lambda_n(t)\mathbf 1_{\{U\ne V\}}$. Thus the asserted common sensitivity constant $L=2$ and zero error are valid without an independence assumption on $U,V$.

Let

\[
A_n=\{(t,u):0\le t<1,\ t\in B_n,\ 0<u\le2\}.
\]

For $n\ne m$, $|A_n|=|A_m|=1$, $|A_n\cap A_m|=1/2$, and $|A_n\cup A_m|=3/2$. Conditional on $X_0=0$, the event $\{X_1^{(n)}=1,X_1^{(m)}=0\}$ is exactly $\{N(A_m)=0,\ N(A_n\setminus A_m)\ge1\}$, and the reverse event is obtained by exchanging $n,m$. Independence on disjoint regions gives

\[
\mathbb P(X_1^{(n)}\ne X_1^{(m)}\mid X_0=0)
=2e^{-1}(1-e^{-1/2})
=2(e^{-1}-e^{-3/2}).
\]

Multiplying by $\mathbb P(X_0=0)=3/4$ yields

\[
\mathbb P(X_1^{(n)}\ne X_1^{(m)})
=\frac32(e^{-1}-e^{-3/2})>0,
\]

uniformly over all distinct indices. Hence every subsequence fails to be Cauchy in probability and therefore cannot converge in probability on this common input.

Finally, $\int_0^1|\lambda_n-\lambda_m|\,dt=1$ for $n\ne m$, so the example does not satisfy a vanishing cross-index rate estimate. Its valid conclusion is exactly the stated limited one: within-index sensitivity together with marginal and weak or time-integrated forward-equation convergence does not force convergence for a fixed Poisson input. It neither refutes a closure theorem that assumes an independent cross-index estimate nor addresses existence of the ordered DPP factor.
