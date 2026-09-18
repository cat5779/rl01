# QWE06 result: fixed-window folded transport, derivative-tail payment, and a typical negative-damping obstruction

Date: 2026-09-18

Repository: \`randomcat4/dpp-stationary-entropy\`  
Branch: \`research/external-qwe06-fixed-window-moving-reference-20260918\`  
Task: \`research_tasks/external_20260918/QWE06/TASK.md\`

## Status

**Main target: INCOMPLETE.**

This submission does **not** prove
\[
\inf_{a\in I} B_n(a)\ge -r_n,\qquad r_n/n\to0,
\]
on a fixed-width interval, and it does **not** give an actual-model asymptotic counterexample to that statement.

It proves three reusable partial results for the exact cyclic Fourier model and the prescribed corrected law:

1. an exact folded count-flux identity whose transport weights are nonnegative on the full task interval;
2. an \(o(1)\) payment for the rare-count contribution with the full first/second moving-reference derivatives retained;
3. a new actual-model method obstruction: for every fixed off-midpoint bias, asymptotically one half of the **typical count mass** lies on layers where the old layerwise damping coefficient \(M_l\) is negative.

The last statement is a counterexample to the proposed intermediate rule “bad damping occurs only in rare layers.” It is **not** a counterexample to entropy concavity, to \(B_n\ge-o(n)\), or to the fixed-density sine target.

All new claims below are author proofs pending a separate claim-by-claim independent audit.

## 1. Model and notation

Keep exactly the task model:
\[
n=2k,\qquad c=\frac{19}{20},\qquad
a_*= \frac{1-c}{2}=\frac1{40},\qquad
I=\left[\frac1{50},\frac3{100}\right].
\]
Let
\[
\xi=\frac{a(1-c-a)}c,\qquad
h=\xi_a=\frac{1-c-2a}{c},\qquad
\xi_{aa}=-\frac2c .
\]
For layer \(l\), write \(m=\min(l,n-l)\), \(C_l=l(n-l)\), and retain the task objects
\[
R_l=D(q_l\Vert u_l g_l),\qquad
\varphi_l=\pi_l'/\pi_l,
\]
with the prescribed degree-two matched Johnson heat reference \(g_l\).

The target term is
\[
B_n(a)=\sum_l\pi_l(a)\left[R_{l,aa}(a)+2\varphi_l(a)R_{l,a}(a)\right].
\]

The task's moving-energy coefficient is
\[
M_l=\Lambda_l-2\varphi_l h\,\tau_{l,\xi}.
\]

## 2. Result A: exact folded positive count flux

Let
\[
G_a(t)=[1-a-c+(a+c)t]^k[1-a+at]^k .
\]
Differentiating gives
\[
\partial_aG_a(t)=(t-1)K_a(t),
\]
where
\[
K_a(t)=k\bigl(A_t^{k-1}B_t^k+A_t^kB_t^{k-1}\bigr),
\]
\(A_t=1-a-c+(a+c)t\), \(B_t=1-a+at\).

Write
\[
\kappa_r=[t^r]K_a(t).
\]
Because \(K_a\) is a sum of probability generating polynomials for “leave one Bernoulli out” counts,
\[
\kappa_r\ge0,\qquad \sum_r\kappa_r=n,
\qquad
\pi_l'=\kappa_{l-1}-\kappa_l .
\]

Use complement symmetry \(R_l=R_{n-l}\) and fold to \(0\le m\le k\):
\[
\varpi_m=
\begin{cases}
\pi_m+\pi_{n-m},&m<k,\\
\pi_k,&m=k.
\end{cases}
\]

A direct summation by parts gives the exact identity
\[
\boxed{
B_n(a)=
h^2\sum_{m=0}^{k}\varpi_mR_{m,\xi\xi}
-\frac2c\sum_{m=0}^{k}\varpi_mR_{m,\xi}
+\sum_{m=0}^{k-1}\omega_m
\bigl(R_{m+1,\xi}-R_{m,\xi}\bigr).
}
\tag{2.1}
\]

The folded flux weights are
\[
\boxed{
\omega_m=2h\bigl(\kappa_m-\kappa_{n-1-m}\bigr).
}
\tag{2.2}
\]

For \(a\in I\), the pair-count distribution in \(K_a\) has mean on the same side of \(k-\tfrac12\) as \(-h\). The coefficient sequence is strictly log-concave/unimodal with the corresponding reflection order, hence
\[
\boxed{\omega_m\ge0\qquad(0\le m<k,\ a\in I).}
\tag{2.3}
\]
Moreover,
\[
\sum_{m=0}^{k-1}\omega_m\le 2|h|n.
\tag{2.4}
\]

This is useful because the count score is no longer bounded layer-by-layer by a worst-case \(|\varphi_l|\); it has been converted into a nonnegative transport measure acting on adjacent \(R_{\xi}\)-increments.

No sign is asserted for \(R_{m+1,\xi}-R_{m,\xi}\).

## 3. Result B: the rare-count part is fully paid

The true count law is a sum of \(k\) independent \(\mathrm{Bern}(a+c)\) variables and \(k\) independent \(\mathrm{Bern}(a)\) variables. Its mean is
\[
\mu_n(a)=n(a+c/2).
\]

For the window
\[
\mathcal T_n(a)=\{|l-\mu_n(a)|\le n^{2/3}\},
\]
Hoeffding gives uniformly on \(I\)
\[
\Pr\{L\notin\mathcal T_n(a)\}\le 2e^{-2n^{1/3}}.
\tag{3.1}
\]

The nontrivial part is that one cannot differentiate a static concentration statement. Instead, the prescribed heat reference is controlled directly.

For
\[
g_\tau=e^{\tau L}r^{\max}
=e^{-\tau}\sum_{j\ge0}\frac{\tau^j}{j!}(I+L)^jr^{\max},
\]
fix a target state \(S\) and normalize the summands. This defines a posterior jump count \(J_S\). Then
\[
\mathbb E[2^{J_S}]
=e^\tau\frac{g_{2\tau}(S)}{g_\tau(S)}.
\tag{3.2}
\]

Counting **all shortest Johnson paths** and using the task clock bounds yields polynomial-in-\(n\), uniform-on-\(I\) estimates for the first two posterior jump moments. Consequently
\[
\left|\frac{g_\xi}{g}\right|=O_I(n),\qquad
\left|\frac{g_{\xi\xi}}g\right|=O_I(n^2).
\tag{3.3}
\]

Together with the determinant formula for the true law and the corresponding polynomial bounds for \(f\), this gives an explicit
\[
T_n=O_I(n^3)
\]
such that
\[
\left|
R_{l,aa}+2\frac{\pi_l'}{\pi_l}R_{l,a}
\right|\le T_n
\]
on every nondegenerate layer.

Therefore
\[
\boxed{
\sup_{a\in I}
\left|
\sum_{l\notin\mathcal T_n(a)}
\pi_l
\left(
R_{l,aa}+2\frac{\pi_l'}{\pi_l}R_{l,a}
\right)
\right|
\le 2T_ne^{-2n^{1/3}}
=o(1).
}
\tag{3.4}
\]

Thus a fixed-window proof no longer needs to fear the count tails. The remaining problem is genuinely on typical layers.

## 4. Result C: typical negative damping at every fixed off-midpoint bias

This is the main obstruction found in this submission.

Let \(L\sim\pi(a)\) and define
\[
\rho(a)=a+\frac c2,\qquad
v(a)=\frac{1-c^2}{4}-(a-a_*)^2.
\]
Then
\[
\mathbb E L=n\rho(a),\qquad \mathrm{Var}(L)=nv(a).
\]

### 4.1 Count-score local limit

For every fixed \(K<\infty\), uniformly for \(a\in I\) and
\[
x=\frac{l-n\rho(a)}{\sqrt{nv(a)}}\in[-K,K],
\]
Fourier inversion for the pair-Bernoulli characteristic function gives
\[
\pi_l=
\frac{\phi(x)}{\sqrt{nv(a)}}
\left(1+O_{I,K}(n^{-1/2})\right),
\tag{4.1}
\]
and, differentiating the same Fourier integral with respect to \(a\),
\[
\boxed{
\varphi_l=
\frac{l-n\rho(a)}{v(a)}+O_{I,K}(1).
}
\tag{4.2}
\]
Hence
\[
\frac{\varphi_L}{\sqrt n}
\Rightarrow
\frac{Z}{\sqrt{v(a)}}.
\tag{4.3}
\]

The latent independent-Bernoulli score also gives
\[
\sum_l\pi_l\varphi_l^2=O_I(n),
\tag{4.4}
\]
which supplies the needed uniform integrability.

### 4.2 The clock term is only order one after normalization

Using the Jacobi/Stieltjes representation of the task clock,
\[
\frac1{1+\xi}\le v_r\le\frac1\xi,\qquad
0<-\frac{\tau_{\xi\xi}}{\tau_\xi}\le\frac2\xi .
\]
Therefore, uniformly on the task interval and all defective layers,
\[
\boxed{
\frac2c
\le
\frac{\Lambda_l}{\tau_{l,\xi}}
\le
\frac2c+\frac{4h^2}{\xi}.
}
\tag{4.5}
\]

So \(\Lambda_l/\tau_{l,\xi}=O_I(1)\), while the count-score term in
\[
\frac{M_l}{\tau_{l,\xi}}
=
\frac{\Lambda_l}{\tau_{l,\xi}}-2h\varphi_l
\tag{4.6}
\]
is order \(\sqrt n\) on typical fluctuations whenever \(h\ne0\).

### 4.3 Theorem

For every fixed
\[
a\in I\setminus\{a_*\},
\]
\[
\boxed{
\Pr\{\min(L,n-L)\ge4,\ M_L(a)<0\}
\longrightarrow\frac12.
}
\tag{4.7}
\]

The same limit holds after adding the typical-window restriction
\[
|L-n\rho(a)|\le n^{2/3}.
\tag{4.8}
\]

**Proof.**
Divide (4.6) by \(\sqrt n\). By (4.5), the first term vanishes. By (4.3),
\[
\frac{M_L}{\tau_{L,\xi}\sqrt n}
\Rightarrow
-\frac{2h}{\sqrt{v(a)}}Z.
\]
For fixed \(a\ne a_*\), the limit is a nondegenerate centered Gaussian and has no atom at zero, so its negative probability tends to \(1/2\). The \(m\le3\) layers and the complement of (4.8) have probability tending to zero. QED.

A weighted strengthening is
\[
\boxed{
\frac1{\sqrt n}\sum_l\pi_l
\left(-\frac{M_l}{\tau_{l,\xi}}\right)_+
\longrightarrow
\frac{2|h|}{\sqrt{2\pi v(a)}}.
}
\tag{4.9}
\]

This is a statement about the **damping coefficient**, not a linear lower bound for \(B_n\): the factors \(\mathcal D_l\), the positive square \(\mathcal Q_l\), and the signed source/residual pairings remain present.

### 4.4 Critical scale

If
\[
a_n=a_*+\frac{\beta}{\sqrt n},\qquad \beta\ne0,
\]
then \(h=-2\beta/(c\sqrt n)\), and
\[
\frac{M_L}{\tau_{L,\xi}}
\Rightarrow
\frac2c+\frac{4\beta}{c\sqrt{v_*}}Z,
\qquad
v_*=\frac{1-c^2}{4}.
\]
Hence
\[
\boxed{
\Pr(M_L<0)
\longrightarrow
\Phi\left(-\frac{\sqrt{v_*}}{2|\beta|}\right).
}
\tag{4.10}
\]

At the exact midpoint, \(h=0\) and \(M_l/\tau_{l,\xi}=2/c>0\). This identifies the actual crossover scale for typical layerwise positivity as \(n^{-1/2}\), not a fixed-width neighborhood.

## 5. Relation to the repository's existing obstruction catalog

The repository already contains related but different method obstructions:

- the S9 growing-layer result proves macroscopic negative mass for certain **moving count-layer Jensen contributions** in actual growing Fourier families;
- S11/S12 rule out specified separated nonnegative budgets;
- the earlier SA05/QWE06 source only guaranteed \(M_l>0\) in an explicit \(O(1/n)\) neighborhood and warned that \(M_l\le0\) may occur outside it.

This submission's theorem (4.7) is more specific to the present moving-reference interface:

> for the actual QWE06 count law, at every fixed \(a\ne a_*\), asymptotically one half of the typical count probability lies on layers where the precise coefficient \(M_l\) is negative.

I did not find this exact prevalence theorem in the current accepted repository summaries or the source packet. It should therefore be treated as a **new method obstruction pending independent audit**, not as a restatement of the accepted S9 obstruction.

The two statements are compatible: S9 concerns the sign/mass of a different layer contribution; (4.7) concerns the sign of the coefficient multiplying the Johnson dissipation in the QWE06 moving-reference identity.

## 6. Remaining exact budget

The task's source estimate gives the one-sided bound
\[
R_{m,\xi}\le K_R
\]
uniformly on the fixed interval; no lower bound or absolute \(O(1)\) estimate is claimed.

Combining it with (2.1), the derivative-tail payment, and the nonnegative folded flux leaves a typical signed budget of the form
\[
\mathfrak C_n(a)=
h^2\sum_{\text{typical }m}\varpi_mR_{m,\xi\xi}
+
\sum_{\text{typical edges }m}\omega_m
(R_{m+1,\xi}-R_{m,\xi}).
\tag{6.1}
\]

A sufficient remaining estimate is
\[
\boxed{
\inf_{a\in I}\mathfrak C_n(a)\ge-o(n).
}
\tag{6.2}
\]

A stronger local sufficient condition would be
\[
(R_{m,\xi\xi})_-\le A_n=o(n),
\qquad
(R_{m+1,\xi}-R_{m,\xi})_-\le G_n=o(1)
\tag{6.3}
\]
uniformly on the typical window. The present work does not prove (6.2) or (6.3).

## 7. Numerical falsification checks

Floating-point diagnostics were run on the exact finite cyclic model, not on a generic signed layer sequence.

For \(a=0.02\), the defective-layer probability mass with \(M_l<0\) was:

| \(n\) | probability mass |
|---:|---:|
| 400 | 0.209447 |
| 4,000 | 0.400948 |
| 10,000 | 0.437041 |
| 40,000 | 0.468442 |

This is consistent with the proved limit \(1/2\).

Full-configuration checks for \(n=8,10,12,14,16,18,22\) and
\(a\in\{0.02,0.0225,0.025,0.0275,0.03\}\) were also used to compare:

- the original count-derivative expression for \(B_n\);
- the folded transport identity (2.1);
- the complete moving-reference interface.

Observed residuals were at ordinary floating precision. These checks are regression/falsification diagnostics, not interval certificates or independent verification.

## 8. Interpretation

This submission is **negative for one proof strategy, neutral for the conjecture, and positive for localization of the remaining gap**.

It proves that a proof based on “\(M_l\) is positive on all important layers” cannot extend from the midpoint to any fixed off-midpoint bias: the failure occurs on typical layers with asymptotic probability \(1/2\), not only in exponentially rare tails.

At the same time, the rare-count contribution itself is now paid with all derivatives retained, and the count-score cross term has been reorganized into an exact nonnegative folded transport. The remaining obstruction is therefore sharply localized to signed typical-layer response, not to count tails or omitted moving-reference derivatives.

No full entropy-rate or Toeplitz conclusion is claimed.
