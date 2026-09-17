# Finite-exchange reduction for the central bridge cost

**Status: PROVED_HERE / PENDING_INDEPENDENT_REVIEW**

Let `r=k-1`, let `mu_k` denote the `r`-layer corrected law at its own time
`s_r`, and put `delta_k=s_k-s_r`.  The raw generator has the constant total
jump rate

\[
\lambda_k=r(n-r)=(k-1)(k+1)=k^2-1.
\]

If `Q_k` is the discrete kernel that performs one uniformly chosen active
occupied--empty swap, then

\[
G_r=\lambda_k(Q_k-I).
\]

Consequently the exact bridge kernel has the Poisson decomposition

\[
e^{\delta_kG_r}
=e^{-\tau_k}\sum_{m\ge0}\frac{\tau_k^m}{m!}Q_k^m,
\qquad \tau_k=\lambda_k\delta_k.                              \tag{1}
\]

The clock-gap result proves `tau_k->1/2`.  Thus the bridge is asymptotically a
finite random number of exchanges, not a macroscopic heat interval and not a
zero-exchange perturbation.

Write `f_k=d mu_k/d u_r`.  The entropy dissipation at the left endpoint is

\[
\mathcal I_k
=-\left.\frac d{ds}D(\mu_ke^{sG_r}\Vert u_r)\right|_{s=0}.
\]

Since `Q_k` is reversible for `u_r`, direct differentiation gives the exact
single-exchange representation

\[
\frac{\mathcal I_k}{\lambda_k}
=\mathbb E_{X\sim\mu_k,\,Y\sim Q_k(X,\cdot)}
  [\log f_k(X)-\log f_k(Y)].                                  \tag{2}
\]

The entropy dissipation is nonincreasing along this exchange semigroup, as
proved in the reviewed SA04 report.  Therefore

\[
E_k
=\int_0^{\delta_k}\mathcal I_k(s)\,ds
\le \delta_k\mathcal I_k(0)
=\tau_k\,\mathcal J_k,                                       \tag{3}
\]

where `J_k=I_k/lambda_k` is the one-exchange entropy loss in (2).

Equation (3) gives a clean sufficient route: because `tau_k->1/2`, the deletion
lower bound would be closed by

\[
\limsup_{k\to\infty}\mathcal J_k<\frac{4c^4}{9}.              \tag{4}
\]

However, exact finite-layer evaluation shows that this crude monotonicity-only
route is not numerically promising.  The observed `J_k` rises from `0.0859` at
`n=6` to `1.0339` at `n=20`, while `4c^4/9` is about `0.3620`.  This does not
disprove (4) asymptotically, but it fails the route's cheapest diagnostic and
shows that the initial dissipation bound discards too much decay inside the
finite exchange window.

The surviving target is therefore the full Poissonized finite-exchange cost in
(1), or its local weak limit, rather than a left-endpoint derivative bound.

