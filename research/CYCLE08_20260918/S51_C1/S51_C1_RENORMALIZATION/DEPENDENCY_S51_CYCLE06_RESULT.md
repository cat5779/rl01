# S51 cycle06 — From local noise-flow curvature to actual entropy-rate chords

## Status

**PROVED (for every compact subinterval of the legal interior, hence in particular for all chords contained in the assigned interval \([-d_c,d_c]\), where \(d_c=(1-c)/4\)).**

The result proved here is the requested finite-chord/thermodynamic-limit bridge. This is an author derivation in this response; the numerical checks below are not independent certification. It does **not** prove the sign of the curvature functional. It does not use a finite Toeplitz block as a projection, does not replace configuration entropy by \(\operatorname{Tr} b(K)\), and does not assume differentiability of the entropy rate. The complete moving-law terms are retained.

The proof gives the stronger consequence that the entropy rate is \(C^2\) on the open legal interior and that its classical second derivative is the negative of the actual-law V14 curvature functional. This regularity is derived after the finite-chord identity, not used as an input.

---

# 1. Main theorem

Let \(Q\) be the half-density sine projection on \(\ell^2(\mathbb Z)\),

\[
Q_{ii}=\frac12,\qquad
Q_{ij}=\frac{\sin(\pi(i-j)/2)}{\pi(i-j)}\quad(i\ne j).
\]

Fix \(0<c<1\), put

\[
\delta_{\max}=\frac{1-c}{2},\qquad d_c=\frac{1-c}{4},
\]

and, for \(u\in[0,1]\) and \(|s|<\delta_{\max}\), let

\[
K_{u,s}=\frac12 I+u\left[c\left(Q-\frac12I\right)+sI\right].
\tag{1.1}
\]

Let \(\mu_{u,s}\) be the stationary DPP with kernel \(K_{u,s}\). For a finite block \(A_L=\{1,\dots,L\}\), write \(H_L(u,s)\) for the full configuration Shannon entropy of \(Y_{A_L}\), and set

\[
h_c(s)=\lim_{L\to\infty}\frac1L H_L(1,s).
\tag{1.2}
\]

The limit exists by stationarity and subadditivity.

Let

\[
q_{u,s}=\Pr_{u,s}(Y_0=1\mid Y_{\mathbb Z\setminus\{0\}}),
\qquad
\phi(q)=\left(q-\frac12\right)\log\frac q{1-q},
\tag{1.3}
\]

and

\[
F_\infty(u,s)=\mathbb E_{u,s}\phi(q_{u,s}).
\tag{1.4}
\]

Then the following statements hold.

### Theorem 1.1 — exact value and chord bridge

For every compact interval \(I\Subset(-\delta_{\max},\delta_{\max})\):

1. **Exact entropy-rate value identity.** For every \(s\in I\),
   \[
   \boxed{
   h_c(s)=\log 2-\int_0^1F_\infty(u,s)\,\frac{du}{u}.}
   \tag{1.5}
   \]
   The integrand is \(O_I(u)\) at \(u=0\).

2. **Complete actual-law local curvature.** There is a bounded, jointly continuous, explicitly defined local function
   \[
   \overline{\mathcal G}_\infty(u,s,z),
   \qquad (u,s,z)\in[0,1]\times I\times\{0,1\}^{\mathbb Z\setminus\{0\}},
   \tag{1.6}
   \]
   given by the full V14 formula in Section 5 below, such that
   \[
   \boxed{
   \partial_s^2F_\infty(u,s)
   =u^2\,\mathbb E_{u,s}\overline{\mathcal G}_\infty(u,s,Y_{\ne0}).}
   \tag{1.7}
   \]
   This identity is obtained as a weak/finite-chord limit of exact finite conditional laws. No derivative of an infinite-volume probability density is postulated.

3. Define
   \[
   \boxed{
   \Gamma_c(s)=\int_0^1u\,
   \mathbb E_{u,s}\overline{\mathcal G}_\infty(u,s,Y_{\ne0})\,du.}
   \tag{1.8}
   \]
   Then \(\Gamma_c\) is continuous on \(I\), and every chord contained in \(I\) satisfies
   \[
   \boxed{
   \Delta_\eta h_c(s)
   =-\int_{-\eta}^{\eta}(\eta-|t|)\Gamma_c(s+t)\,dt,}
   \tag{1.9}
   \]
   where \(\Delta_\eta f(s)=f(s+\eta)+f(s-\eta)-2f(s)\).

4. Consequently,
   \[
   h_c\in C^2((-\delta_{\max},\delta_{\max})),
   \qquad
   \boxed{h_c''(s)=-\Gamma_c(s).}
   \tag{1.10}
   \]

Taking \(I\) to be any compact neighborhood of \([-d_c,d_c]\) proves the assigned claim for every chord contained in \([-d_c,d_c]\). For the initially frozen value \(c=19/20\), this is the interval \([-1/80,1/80]\).

At \(s=0\), the function \(\overline{\mathcal G}_\infty(u,0,\cdot)\) is exactly the unsmoothed half-filled V14 object of `SA03_VOLUME_LIMIT.md`, and hence

\[
\boxed{
\Gamma_c(0)=\int_0^1u\,
\mathbb E_{\infty,u}\overline{\mathcal G}_{\infty,u}\,du.}
\tag{1.11}
\]

The expectation and the kernel in (1.11) are under the true unsmoothed sine law.

---

# 2. Reusable tool: weighted finite-jet chord transfer

The bridge used below is not DPP-specific.

### Lemma 2.1 — weighted triangular-kernel transfer

Let \(J\subset\mathbb R\) be open, let \((U,\nu)\) be a measure space, and let
\(f_n:U\times J\to\mathbb R\) be such that \(f_n(u,\cdot)\in C^2(J)\). Put

\[
g_n(u,s)=\partial_s^2 f_n(u,s).
\]

Suppose that there are measurable \(f,g\) such that for every compact \(J_0\Subset J\),

\[
\int_U\sup_{s\in J_0}|f_n(u,s)-f(u,s)|\,d\nu(u)\longrightarrow0,
\tag{2.1}
\]

and

\[
\int_U\sup_{s\in J_0}|g_n(u,s)-g(u,s)|\,d\nu(u)\longrightarrow0.
\tag{2.2}
\]

Assume also that, for every compact \(J_0\Subset J\), \(\int_U\sup_{s\in J_0}|f(u,s)|d\nu(u)<\infty\) and \(\int_U\sup_{s\in J_0}|g(u,s)|d\nu(u)<\infty\). Define

\[
A(s)=\int_U f(u,s)\,d\nu(u),
\qquad
G(s)=\int_U g(u,s)\,d\nu(u).
\tag{2.3}
\]

Then, for every chord \([s-\eta,s+\eta]\Subset J\),

\[
\boxed{
\Delta_\eta A(s)=
\int_{-\eta}^{\eta}(\eta-|t|)G(s+t)\,dt.}
\tag{2.4}
\]

Moreover \(A''=G\) in the sense of distributions. If \(G\) is continuous and \(A\) is continuous, then \(A\in C^2(J)\) and \(A''=G\) classically.

#### Proof

For every \(n\) and every fixed \(u\), the elementary triangular-kernel identity gives

\[
\Delta_\eta f_n(u,s)=
\int_{-\eta}^{\eta}(\eta-|t|)g_n(u,s+t)\,dt.
\tag{2.5}
\]

Integrate with respect to \(\nu\), use Fubini, and then use (2.1)–(2.2). This proves (2.4). For a test function \(\psi\in C_c^\infty(J)\), integration by parts for \(f_n\), followed by the same two convergences, gives

\[
\int_JA(s)\psi''(s)\,ds=
\int_JG(s)\psi(s)\,ds.
\tag{2.6}
\]

Thus \(A''=G\) distributionally. If \(G\) is continuous, subtracting a twice-integrated primitive of \(G\) leaves a distribution with zero second derivative, hence an affine function. Continuity identifies the representative pointwise. ∎

In the application below,

\[
U=(0,1],\qquad d\nu(u)=\frac{du}{u},
\tag{2.7}
\]

\(f_n\) is the exact finite-observation conditional functional, and \(g_n\) is its full moving-law second derivative. The singular measure \(du/u\) is harmless because \(f_n=O(u^2)\) and \(g_n=O(u^2)\).

---

# 3. Uniform non-nullness and the \(u=0\) endpoint

Fix a compact \(I\Subset(-\delta_{\max},\delta_{\max})\), and put

\[
s_*:=\sup_{s\in I}|s|,
\qquad
\varepsilon:=\delta_{\max}-s_*>0.
\tag{3.1}
\]

Because \(Q\) is a projection, \(K_{u,s}\) is the output of the projection DPP \(X\sim\operatorname{DPP}(Q)\) through the coordinatewise channel

\[
\Pr(Y_i=1\mid X_i=0)=\alpha_{u,s}
 =\frac12+u\left(s-\frac c2\right),
\tag{3.2}
\]

\[
\Pr(Y_i=1\mid X_i=1)=\beta_{u,s}
 =\frac12+u\left(s+\frac c2\right).
\tag{3.3}
\]

For \(u\in[0,1]\), \(s\in I\),

\[
\varepsilon\le\alpha_{u,s}\le\beta_{u,s}\le1-\varepsilon.
\tag{3.4}
\]

If \(\mathcal A\) is any sigma-field generated by output coordinates other than zero, then independence of the channel noise at zero gives

\[
\Pr(Y_0=1\mid\mathcal A)
 =\alpha_{u,s}+uc\Pr(X_0=1\mid\mathcal A).
\tag{3.5}
\]

Therefore every finite- or infinite-observation posterior satisfies

\[
q\in[\alpha_{u,s},\beta_{u,s}]\subset[\varepsilon,1-\varepsilon]
\tag{3.6}
\]

and

\[
\left|q-\frac12\right|
 \le u\left(\frac c2+s_*\right).
\tag{3.7}
\]

Since the derivative of the logit is \(1/[q(1-q)]\),

\[
0\le\phi(q)
\le
\frac{(c/2+s_*)^2}{\varepsilon(1-\varepsilon)}u^2
=:C_{0,I}u^2.
\tag{3.8}
\]

This bound is uniform in the observation set and pays the \(u=0\) endpoint in every later \(du/u\) integral.

---

# 4. Exact finite-volume entropy production and the anchor average

Let \(A_L=\{1,\ldots,L\}\). For \(i\in A_L\), define the exact conditional probability under the true \(A_L\)-marginal

\[
q_{L,i}(u,s)=
\Pr_{u,s}(Y_i=1\mid Y_{A_L\setminus\{i\}}),
\tag{4.1}
\]

and

\[
F_{L,i}(u,s)=\mathbb E_{u,s}\phi(q_{L,i}(u,s)).
\tag{4.2}
\]

## 4.1 Bit-flip identity

For fixed \(s\),

\[
K_{u,s}=\frac{1-u}{2}I+uK_{1,s}.
\tag{4.3}
\]

Thus the law on \(A_L\) is obtained from its \(u=1\) law by an independent binary symmetric channel with correlation parameter \(u\). Put \(u=e^{-t}\). The finite probability vector \(p_t(y)\) satisfies

\[
\partial_t p_t(y)=\frac12\sum_{i\in A_L}
[p_t(y^i)-p_t(y)].
\tag{4.4}
\]

Differentiating the actual configuration entropy and pairing the two ends of every edge gives

\[
\frac{d}{dt}H_L(e^{-t},s)
 =\sum_{i\in A_L}\mathbb E\left[
\left(q_{L,i}-\frac12\right)
\log\frac{q_{L,i}}{1-q_{L,i}}\right].
\tag{4.5}
\]

Indeed, for a fixed exterior word with masses \(p_0=w(1-q)\) and \(p_1=wq\), the paired edge contribution is

\[
-\frac12[(p_1-p_0)\log p_0+(p_0-p_1)\log p_1]
=w\phi(q).
\tag{4.6}
\]

Since \(dt/du=-1/u\),

\[
\boxed{
\partial_uH_L(u,s)=-\frac1u\sum_{i=1}^L F_{L,i}(u,s).}
\tag{4.7}
\]

The bound (3.8) permits integration to \(u=0\), where the law is i.i.d. fair Bernoulli and \(H_L(0,s)=L\log2\). Hence

\[
\frac1L H_L(1,s)
=\log2-
\int_0^1\left[\frac1L\sum_{i=1}^LF_{L,i}(u,s)\right]\frac{du}{u}.
\tag{4.8}
\]

## 4.2 The average over all anchors

Let

\[
C_R=\{-R,\ldots,-1,1,\ldots,R\},
\tag{4.9}
\]

let \(q_R=\Pr(Y_0=1\mid Y_{C_R})\), and put

\[
F_R(u,s)=\mathbb E_{u,s}\phi(q_R).
\tag{4.10}
\]

The function \(\phi\) is convex, because

\[
\phi''(q)=\frac1{2q^2(1-q)^2}>0.
\tag{4.11}
\]

If \(\mathcal G\subset\mathcal H\) are observation sigma-fields, conditional Jensen gives

\[
\mathbb E\phi(\mathbb E[Y_0\mid\mathcal G])
\le
\mathbb E\phi(\mathbb E[Y_0\mid\mathcal H]).
\tag{4.12}
\]

Therefore every block anchor satisfies \(F_{L,i}\le F_\infty\), while every anchor at distance at least \(R\) from the boundary satisfies \(F_{L,i}\ge F_R\). Since \(\phi\ge0\),

\[
\left(1-\frac{2R}{L}\right)_+F_R(u,s)
\le
\frac1L\sum_{i=1}^L F_{L,i}(u,s)
\le F_\infty(u,s).
\tag{4.13}
\]

The posteriors \(q_R\) form a bounded martingale as \(R\uparrow\infty\), and hence converge almost surely and in \(L^1\) to the all-exterior posterior. By (3.6), \(\phi\) is bounded and continuous on the common posterior range, so

\[
F_R(u,s)\longrightarrow F_\infty(u,s).
\tag{4.14}
\]

First let \(L\to\infty\) in (4.13), and then \(R\to\infty\). This proves

\[
\frac1L\sum_{i=1}^LF_{L,i}(u,s)	o F_\infty(u,s).
\tag{4.15}
\]

Finally, (3.8) gives a common integrable majorant \(C_{0,I}u\) after division by \(u\). Dominated convergence in (4.8) proves (1.5).

This is the required random-anchor thermodynamic interface; no block anchor was replaced by a center anchor.

---

# 5. The complete finite conditional jet

Fix a finite observation set \(C\subset\mathbb Z\setminus\{0\}\) and a word \(z\in\{0,1\}^C\). Write

\[
\sigma_i=2z_i-1,
\qquad
S_z=\operatorname{diag}(\sigma_i)_{i\in C}.
\tag{5.1}
\]

On \(\{0\}\cup C\), write the kernel in block form. Put

\[
h=K_{00}=\frac12+us,
\quad
b=K_{C0}=ucQ_{C0},
\tag{5.2}
\]

\[
B_z=K_C-\operatorname{diag}(1-z)
 =\frac12S_z+u\left[c\left(Q_C-\frac12I\right)+sI\right],
\quad
G_z=B_z^{-1},
\quad
v_z=G_zb.
\tag{5.3}
\]

The full atom formula is

\[
w_z=\Pr(Y_C=z)=(-1)^{|C|-|z|}\det B_z.
\tag{5.4}
\]

The channel bounds make every \(w_z\) positive. The Schur complement gives the exact conditional probability

\[
\boxed{q_z=h-b^*G_zb.}
\tag{5.5}
\]

For a flip at coordinate \(i\), let \(z^i\) be the flipped word, put

\[
o_i(z)=\frac{w_{z^i}}{w_z},
\qquad
d_i(z)=q_{z^i}-q_z.
\tag{5.6}
\]

## 5.1 Moving-law transport

Vary \(s\), keeping \(u,c,Q\) fixed. Given the latent projection process, every channel success probability has derivative \(u\). Differentiating the actual word probabilities gives

\[
w_z'=u\sum_{i\in C}\sigma_i(z)[w_z+w_{z^i}].
\tag{5.7}
\]

If \(a_z=\Pr(Y_0=1,Y_C=z)\), then the center coordinate contributes an additional \(uw_z\):

\[
a_z'=uw_z+u\sum_{i\in C}\sigma_i(z)[a_z+a_{z^i}].
\tag{5.8}
\]

Define

\[
r_i(z)=-u\sigma_i(z)o_i(z),
\qquad
(Tg)(z)=\sum_{i\in C}r_i(z)[g(z^i)-g(z)],
\tag{5.9}
\]

and

\[
D=\partial_s+T.
\tag{5.10}
\]

Equation (5.7) is exactly \(T^*w=w'\), so for every differentiable word function \(g\),

\[
\frac d{ds}\mathbb E_wg=\mathbb E_wDg.
\tag{5.11}
\]

Dividing (5.8) by \(w_z\) and subtracting the derivative of the denominator gives

\[
q_z'=u+u\sum_i\sigma_i o_i(q_{z^i}-q_z),
\tag{5.12}
\]

and hence the exact cancellation

\[
\boxed{Dq=u.}
\tag{5.13}
\]

This identity contains both the posterior derivative and the derivative of the actual observation law.

For a smooth \(\psi\), let

\[
\operatorname{Breg}_\psi(p,q)
=\psi(p)-\psi(q)-\psi'(q)(p-q),
\tag{5.14}
\]

\[
\mathcal B_\psi(z)=
\sum_i r_i(z)\operatorname{Breg}_\psi(q_{z^i},q_z).
\tag{5.15}
\]

The discrete chain rule and (5.13) give

\[
D\psi(q)=u\psi'(q)+\mathcal B_\psi.
\tag{5.16}
\]

Applying \(D\) once more yields the complete finite curvature

\[
\boxed{
\mathcal G_C
=u^2\phi''(q)+u\mathcal B_{\phi'}+D\mathcal B_\phi.}
\tag{5.17}
\]

Thus

\[
\boxed{
\partial_s^2F_C(u,s)=\mathbb E_{u,s}\mathcal G_C.}
\tag{5.18}
\]

Expanding (5.11) twice shows explicitly that (5.18) is

\[
\sum_z\left
[w_z''\phi(q_z)
+2w_z'\phi'(q_z)q_z'
+w_z\{\phi''(q_z)(q_z')^2+\phi'(q_z)q_z''\}]
\right.
\tag{5.19}
\]

with no frozen weight and no missing score term.

## 5.2 Normalized V14 form

The determinant lemma and the rank-one inverse update give

\[
o_i=\sigma_iG_{ii}-1,
\qquad
r_i=u(\sigma_i-G_{ii}),
\tag{5.20}
\]

\[
G_{z^i}=G_z-\frac{\sigma_i}{o_i}G_ze_ie_i^*G_z,
\qquad
v_{z^i}=v_z-\frac{\sigma_i}{o_i}v_iG_ze_i,
\tag{5.21}
\]

\[
d_i=\frac{\sigma_i|v_i|^2}{o_i}.
\tag{5.22}
\]

Since \(G_z'=-uG_z^2\),

\[
q_z'=uA_z,
\qquad A_z:=1+\|v_z\|^2,
\tag{5.23}
\]

and

\[
r_i'=u^2(G_z^2)_{ii}.
\tag{5.24}
\]

Put

\[
\bar r_i=\frac{r_i}{u}=\sigma_i-G_{ii},
\qquad
\overline{\mathcal B}_\psi
=\sum_i\bar r_i\operatorname{Breg}_\psi(q_{z^i},q_z).
\tag{5.25}
\]

For \(u>0\), divide (5.17) by \(u^2\), differentiate each Bregman term, and use (5.23)–(5.24). The result is

\[
\boxed{
\begin{aligned}
\overline{\mathcal G}_C(z)={}&\phi''(q)
 +\overline{\mathcal B}_{\phi'}\\
&+\sum_i(G^2)_{ii}\operatorname{Breg}_\phi(q_{z^i},q)\\
&+\sum_i\bar r_i\Big(
 [\phi'(q_{z^i})-\phi'(q)]A_{z^i}
 -\phi''(q)d_iA_z\Big)\\
&+\sum_j\bar r_j\big[
 \overline{\mathcal B}_\phi(z^j)
 -\overline{\mathcal B}_\phi(z)\big].
\end{aligned}}
\tag{5.26}
\]

and

\[
\boxed{
\partial_s^2F_C(u,s)
=u^2\mathbb E_{u,s}\overline{\mathcal G}_C(u,s,Y_C).}
\tag{5.27}
\]

At \(u=0\), set \(\overline{\mathcal G}_C=\phi''(1/2)=8\). Formula (5.26) has this continuous extension because \(v=0\), \(q=1/2\), and every flip defect vanishes.

## 5.3 Dimension-free domination

On \(I\), the spectrum of every finite principal kernel lies in \([\varepsilon,1-\varepsilon]\). Put

\[
a=\varepsilon^{-1},
\qquad
\ell=\|b\|\le\frac{uc}{2},
\qquad
L=a\ell.
\tag{5.28}
\]

Then

\[
\|G_z\|\le a,
\qquad
\|v_z\|\le L,
\qquad
\max(o_i,o_i^{-1})\le a.
\tag{5.29}
\]

The rank-one identities imply

\[
\sum_i|d_i|\le a\|v\|^2,
\qquad
\sum_i d_i^2\le a^2\|v\|^4,
\tag{5.30}
\]

and, with \(e_{ij}=d_i(z^j)-d_i(z)\),

\[
|e_{ij}|\le
2a^2|G_{ij}||v_i||v_j|
+a^3|G_{ij}|^2(|v_i|^2+|v_j|^2).
\tag{5.31}
\]

Together with \(\sum_j|G_{ij}|^2=(G^2)_{ii}\le a^2\), these estimates give the connected double-flip bound

\[
\sum_{i\ne j}D_{ij}|e_{ij}|\le8a^{10}\|v\|^4,
\qquad
D_{ij}=\max(|d_i(z)|,|d_i(z^j)|).
\tag{5.32}
\]

Let

\[
M_k=\sup_{q\in[\varepsilon,1-\varepsilon]}|\phi^{(k)}(q)|.
\tag{5.33}
\]

Taylor's formula for the Bregman defects, followed by (5.30)–(5.32), gives the finite-word estimate

\[
\left|
\overline{\mathcal G}_C-\phi''(q)
\right|
\le
L^4\left[10M_2a^{12}+M_3(a^3+2a^5L^2)\right].
\tag{5.34}
\]

The right side is bounded uniformly in \(C,u,s,z\), because \(L\le ac/2\). Therefore there is a finite constant \(B_I\) such that

\[
\boxed{
|\overline{\mathcal G}_C(u,s,z)|\le B_I,
\qquad
|\partial_s^2F_C(u,s)|\le B_Iu^2.}
\tag{5.35}
\]

The point of (5.31)–(5.32) is that no bare volume-sized score sum is estimated. Every double flip carries a connected \(G_{ij}\) factor and center-response factors.

---

# 6. Direct exact-sine local limit, uniformly off the midpoint

This section constructs the infinite kernel from exact sine principal blocks. No Fejér approximation is used.

Let

\[
C_\infty=\mathbb Z\setminus\{0\},
\qquad
\mathcal H=\ell^2(C_\infty),
\qquad
\Omega=\{0,1\}^{C_\infty}.
\tag{6.1}
\]

For \(s\in I\), define

\[
H_s=c\left(Q_{C_\infty}-\frac12I\right)+sI,
\qquad
b^0=cQ_{C_\infty,0}.
\tag{6.2}
\]

Since \(Q\) is a projection and \(Q_{00}=1/2\),

\[
\|H_s\|\le\frac c2+s_*=\frac12-\varepsilon,
\qquad
\|b^0\|^2=c^2(Q_{00}-Q_{00}^2)=\frac{c^2}{4}.
\tag{6.3}
\]

For \(z\in\Omega\), let \(S_z=\operatorname{diag}(2z_i-1)\), and define

\[
G(u,s,z)=\left(\frac12S_z+uH_s\right)^{-1},
\tag{6.4}
\]

\[
v(u,s,z)=G(u,s,z)\,u b^0,
\tag{6.5}
\]

\[
q(u,s,z)=\frac12+us-u(b^0)^*v(u,s,z).
\tag{6.6}
\]

The inverse exists uniformly, because

\[
\left\|2uS_zH_s\right\|\le1-2\varepsilon<1,
\tag{6.7}
\]

and

\[
G=2\sum_{k\ge0}(-2uS_zH_s)^kS_z,
\qquad
\|G\|\le\varepsilon^{-1}=a.
\tag{6.8}
\]

## 6.1 Uniform finite-window convergence

Let \(P_R\) project onto \(C_R\), and set

\[
H_{R,s}=P_RH_sP_R,
\qquad
b_R^0=P_Rb^0.
\tag{6.9}
\]

Embed the finite inverse by

\[
G_R=(S_z/2+uH_{R,s})^{-1}
\tag{6.10}
\]

on all of \(\mathcal H\); on \(C_R^c\) it equals \(2S_z\). Define \(v_R=G_Rub_R^0\) and

\[
q_R=\frac12+us-u(b_R^0)^*v_R.
\tag{6.11}
\]

On \(C_R\), these are exactly the inverse, center response, and posterior obtained by conditioning the true sine DPP on \(Y_{C_R}\). Outside \(C_R\), \(v_R\) vanishes and flips do not change \(q_R\), so extending the finite sums to all indices introduces only zero terms.

We have

\[
H_{R,s}\to H_s\quad\text{strongly, uniformly for }s\in I,
\qquad
b_R^0\to b^0\quad\text{in }\ell^2.
\tag{6.12}
\]

Use the uniformly convergent Neumann series (6.8). For a fixed vector \(x\), the set \(\{S_zx:z\in\Omega\}\) is compact in \(\ell^2\): truncate the tail of \(x\), then only finitely many sign choices remain on the retained coordinates. Uniformly bounded strong convergence is uniform on compact vector sets. Induction over each finite Neumann term, followed by the common geometric tail, therefore gives

\[
\sup_{u\in[0,1],\,s\in I,\,z\in\Omega}
\|v_R(u,s,z)-v(u,s,z)\|\to0.
\tag{6.13}
\]

For every fixed coordinate \(i\), the same argument with \(e_i\) gives

\[
\sup_{u,s,z}
\|(G_R-G)e_i\|\to0.
\tag{6.14}
\]

Consequently

\[
\sup_{u,s,z}|q_R-q|\to0.
\tag{6.15}
\]

The maps \((u,s,z)\mapsto v,G e_i,q\) are continuous when \(\Omega\) has the product topology.

## 6.2 The limit posterior is the actual posterior

For each fixed \(u,s\), \(q_R\) is the bounded conditional-expectation martingale

\[
q_R=\mathbb E_{u,s}[Y_0\mid Y_{C_R}].
\tag{6.16}
\]

It converges almost surely and in \(L^1\) to the all-exterior posterior. By the uniform convergence (6.15), the function \(q(u,s,z)\) in (6.6) is a continuous version of that actual posterior.

## 6.3 Absolute summability and uniform tails of V14

The family of vectors

\[
\{v_R(u,s,z):R\in\mathbb N\cup\{\infty\},u\in[0,1],s\in I,z\in\Omega\}
\tag{6.17}
\]

has compact closure: the limit image is compact by continuity on the compact parameter space, (6.13) is uniform, and finitely many initial \(R\)'s have compact finite-dimensional images. Thus

\[
\tau_m:=\sup_{R,u,s,z}
\sum_{i\notin C_m}|v_{R,i}|^2\longrightarrow0.
\tag{6.18}
\]

For every fixed \(i\), the same reasoning applied to (6.14) gives

\[
\eta_{i,m}:=
\sup_{R,u,s,z}
\sum_{j\notin C_m}|(G_R)_{ji}|^2\longrightarrow0.
\tag{6.19}
\]

The one-flip terms obey

\[
\sup_{R,u,s,z}\sum_{i\notin C_m}|d_i|
\le a\tau_m,
\tag{6.20}
\]

\[
\sup_{R,u,s,z}\sum_{i\notin C_m}d_i^2
\le a^2L_*^2\tau_m,
\qquad L_*:=ac/2.
\tag{6.21}
\]

After expanding the last line of (5.26), every off-diagonal double-flip term is bounded by a fixed constant, depending only on \(I,c\), times a finite sum of the connected nonnegative kernels

\[
|G_{ij}||v_i|^3|v_j|,
\quad
|G_{ij}|^2|v_i|^4,
\quad
|G_{ij}|^2|v_i|^2|v_j|^2,
\quad
|G_{ij}|^4|v_i|^4,
\tag{6.22}
\]

and the versions with \(i,j\) exchanged, together with

\[
|d_j|D_{ij}^2.
\tag{6.23}
\]

Their tails vanish uniformly:

* For the first kernel, an \(i\)-tail is controlled by \(aL_*^2\tau_m\); a \(j\)-tail is controlled by \(aL_*^3\sqrt{\tau_m}\) by Cauchy–Schwarz.
* For the second kernel, the \(i\)-tail is at most \(a^2L_*^2\tau_m\). For a \(j\)-tail, first restrict \(i\) to a fixed finite \(C_\ell\) and use (6.19), then control \(i\notin C_\ell\) by \(a^2L_*^2\tau_\ell\).
* The third kernel has either-coordinate tail at most \(a^2L_*^2\tau_m\).
* The fourth is bounded by \(a^2\) times the second.
* The connected Bregman remainder obeys
  \[
  \sup_{R,u,s,z}
  \sum_{i\notin C_m\ \text{or}\ j\notin C_m}
  |d_j|D_{ij}^2
  \le4a^3L_*^4\tau_m.
  \tag{6.24}
  \]

The diagonal \(i=j\) terms use the one-flip tails (6.20)–(6.21). Hence, if (5.26) is first expanded and then all single and double indices are truncated to \(C_m\), there is a deterministic \(\rho_m\downarrow0\) such that

\[
\sup_{R,u,s,z}
|\overline{\mathcal G}_R-
\overline{\mathcal G}_R^{[m]}|
\le\rho_m.
\tag{6.25}
\]

No estimate of a bare \(\sum_{i,j}|e_{ij}|\) is used.

For fixed \(m\), the truncated expression depends on finitely many entries of \(q_R,v_R,G_Re_i\) and their finitely flipped versions. Equations (6.13)–(6.15), uniformly also after finitely many flips because the supremum is over all words, imply

\[
\sup_{u,s,z}
|\overline{\mathcal G}_R^{[m]}-
\overline{\mathcal G}_\infty^{[m]}|	o0.
\tag{6.26}
\]

Let \(m\to\infty\) after \(R\to\infty\). From (6.25)–(6.26),

\[
\boxed{
\sup_{u\in[0,1],\,s\in I,\,z\in\Omega}
|\overline{\mathcal G}_R(u,s,z)-
\overline{\mathcal G}_\infty(u,s,z)|\to0.}
\tag{6.27}
\]

This proves at once that all sums in the infinite V14 formula are absolutely convergent in the connected grouping used above, that the result is independent of the truncation sequence, and that \(\overline{\mathcal G}_\infty\) is jointly continuous. The bound (5.35) passes to the limit.

## 6.4 Actual-law expectations and moving-law convergence

Let \(\mu_{u,s}^{\mathrm{ext}}\) be the true exterior marginal on \(\Omega\). Since \(\overline{\mathcal G}_R\) depends only on \(C_R\),

\[
\mathbb E_{\mu_{u,s}^{\mathrm{ext}}}
\overline{\mathcal G}_R
\tag{6.28}
\]

is exactly the expectation in the finite conditional identity (5.27). There is no replacement law. Moreover, because the same true infinite law is used for both terms,

\[
\sup_{u,s}
\left|
\mathbb E_{u,s}\overline{\mathcal G}_R-
\mathbb E_{u,s}\overline{\mathcal G}_\infty
\right|
\le
\sup_{u,s,z}|\overline{\mathcal G}_R-
\overline{\mathcal G}_\infty|	o0.
\tag{6.29}
\]

Likewise, (6.15) and the uniform posterior range imply

\[
\sup_{u,s}
|F_R(u,s)-F_\infty(u,s)|\to0.
\tag{6.30}
\]

Cylinder probabilities of \(\mu_{u,s}^{\mathrm{ext}}\) are finite determinant polynomials in entries of \(K_{u,s}\), so the exterior law is weakly continuous in \((u,s)\). Together with the joint continuity and boundedness of \(\overline{\mathcal G}_\infty\), this shows that

\[
(u,s)\longmapsto
\mathbb E_{u,s}\overline{\mathcal G}_\infty(u,s,Y_{\ne0})
\tag{6.31}
\]

is continuous.

---

# 7. Chord transfer and identification with the entropy rate

For every finite \(R\), equations (5.27) and the ordinary finite-dimensional chord identity give

\[
\Delta_\eta F_R(u,s)
=
\int_{-\eta}^{\eta}(\eta-|t|)
\,u^2\mathbb E_{u,s+t}
\overline{\mathcal G}_R(u,s+t,Y_{C_R})\,dt.
\tag{7.1}
\]

We now verify the hypotheses of Lemma 2.1 with \(d\nu=du/u\).

First, by (3.8),

\[
|F_R(u,s)-F_\infty(u,s)|\le2C_{0,I}u^2.
\tag{7.2}
\]

Together with (6.30), dominated convergence gives

\[
\int_0^1
\sup_{s\in I}|F_R(u,s)-F_\infty(u,s)|\frac{du}{u}	o0.
\tag{7.3}
\]

Second, set

\[
g_R(u,s)=u^2\mathbb E_{u,s}\overline{\mathcal G}_R(u,s,Y_{C_R}),
\tag{7.4}
\]

\[
g_\infty(u,s)=u^2\mathbb E_{u,s}\overline{\mathcal G}_\infty(u,s,Y_{\ne0}).
\tag{7.5}
\]

By (6.29),

\[
\int_0^1\sup_{s\in I}|g_R-g_\infty|\frac{du}{u}
\le
\frac12\sup_{u,s,z}
|\overline{\mathcal G}_R-
\overline{\mathcal G}_\infty|	o0.
\tag{7.6}
\]

Lemma 2.1 therefore gives

\[
\Delta_\eta
\left(\int_0^1F_\infty(u,s)\frac{du}{u}\right)
=
\int_{-\eta}^{\eta}(\eta-|t|)
\left[
\int_0^1u\mathbb E_{u,s+t}
\overline{\mathcal G}_\infty(u,s+t)\,du
\right]dt.
\tag{7.7}
\]

Combining (7.7) with the already proved value identity (1.5) gives exactly

\[
\Delta_\eta h_c(s)
=-\int_{-\eta}^{\eta}(\eta-|t|)\Gamma_c(s+t)\,dt.
\tag{7.8}
\]

The domination \(|\overline{\mathcal G}_\infty|\le B_I\) gives

\[
|u\mathbb E\overline{\mathcal G}_\infty|\le B_Iu,
\tag{7.9}
\]

so \(\Gamma_c\) is finite and continuous by dominated convergence. The value identity and (3.8) also show that \(h_c\) is continuous. The distributional conclusion of Lemma 2.1 now gives

\[
h_c''=-\Gamma_c
\tag{7.10}
\]

and continuity of \(\Gamma_c\) upgrades this to classical \(C^2\) regularity. Thus differentiability is a consequence, not an input.

For each fixed \(u\), the same argument without integrating in \(u\) proves (1.7).

---

# 8. Exact matching to the SA03 midpoint V14 object

At \(s=0\),

\[
H_0=c\left(Q_{C_\infty}-\frac12I\right),
\qquad
b^0=cQ_{C_\infty,0},
\tag{8.1}
\]

and

\[
G=(S_z/2+uH_0)^{-1},
\quad
v=Gub^0,
\quad
q=\frac12-u(b^0)^*v.
\tag{8.2}
\]

These are exactly the data in V14 of `results/SA03/SA03_VOLUME_LIMIT.md`. The source's parameter \(x\) is \(x=cu\), while variation in the scalar diagonal parameter is

\[
h=K_{00}=\frac12+us,
\qquad
\partial_s=u\partial_h.
\tag{8.3}
\]

The finite identity (5.27) therefore reads

\[
\partial_s^2F_R(u,0)
=u^2\partial_h^2F_{x,R}(1/2)
=u^2\mathbb E_{u,0}\overline{\mathcal G}_R(u,0).
\tag{8.4}
\]

The expectation in (8.4) is under the actual finite marginal of the exact unsmoothed sine DPP. Passing to the limit uses (6.27)–(6.29), not a frozen reference law:

\[
\partial_s^2F_\infty(u,0)
=u^2\mathbb E_{\infty,u}
\overline{\mathcal G}_{\infty,u}.
\tag{8.5}
\]

After division by \(u\) and integration,

\[
\boxed{
\Gamma_c(0)
=
\int_0^1u\mathbb E_{\infty,u}
\overline{\mathcal G}_{\infty,u}\,du.}
\tag{8.6}
\]

This is the requested identification with the explicit V14 object.

No Fejér approximant appears in the proof. Therefore no Fejér-to-unsmoothed passage is silently assumed. The exact principal blocks \(P_RQP_R\) are used from the start, and finite and infinite local functions are evaluated under the same exact infinite law.

---

# 9. Source interfaces actually used

The proof does not take any predecessor's author label as an axiom.

1. **`TARGET.md`.** Used only for the frozen definition of full configuration entropy and the exact independent-channel representation of DPP kernels. The entropy-production calculation is rederived in Section 4.

2. **`results/SA03/SA03_S9_SIGNED_TRANSPORT.md`.** The finite Schur/transport formulas corresponding to its equations (2.1)–(4.1) and the connected dimension-free estimates corresponding to (6.1)–(6.16) are the relevant interfaces. Sections 5.1–5.3 above rederive the transport cancellation, display the full moving-weight Hessian, and state the rank-one estimates and the resulting uniform bound with their hypotheses verified uniformly on compact \(s\)-intervals.

3. **`results/SA03/SA03_VOLUME_LIMIT.md`.** Its V14 grouping and connected-tail architecture are used as the model for the infinite local object. The new interface established here is stronger in the needed direction: exact sine principal blocks, compact-uniform \(s\)-dependence away from the legal endpoints, and direct actual-law convergence. The source's warning that V14 had not yet been identified with the entropy-rate Hessian is precisely the gap closed by Sections 4 and 7.

4. **`results/SA03/SA03_EFFECTIVE_REMAINDER.md`.** Not used in the proof. Its Fejér quantitative bounds are unnecessary because this argument works directly with exact sine principal blocks.

5. **`research/CYCLE06_20260918/S41/S41_CYCLE05_RESULT.md`.** Not used in the proof. S41 repairs a different finite-observation localization estimate by adding the \(Z_0\) energy, and its theorem is explicitly conditional on the V14 identification. The present argument neither improves its constants nor uses its localization budget. It supplies the missing identification by a value-first/chord-transfer route.

---

# 10. Scope beyond half filling and remaining obligations

## 10.1 What is needed for \(\rho\ne1/2\)

For the centered sine projection \(Q_\rho\), the same bridge mechanism requires only the following replacements:

\[
Q_{\rho,00}=\rho,
\qquad
\|Q_{\rho,C0}\|^2=\rho(1-\rho),
\tag{10.1}
\]

\[
H_{\rho,s}=c(Q_{\rho,C}-I/2)+sI,
\qquad
h_{\rho}(u,s)=\frac12+u[c(\rho-1/2)+s].
\tag{10.2}
\]

Because \(Q_\rho\) is still a projection, \(\|Q_\rho-I/2\|=1/2\), so the same compact-interior inverse bound and the same exact-principal-block strong convergence hold. The finite transport algebra is unchanged. Thus the chord-transfer mechanism itself has no half-density obstruction.

What is not supplied by the cited SA03 source is a named, previously localized/sign-tested \(\rho\)-dependent V14 functional. To extend the source identification beyond \(\rho=1/2\), one must instantiate (5.26) with (10.2), verify the same connected-tail truncation for that kernel, and then redo any \(\rho\)-specific sign or quantitative localization argument. The entropy-rate bridge proved here would then apply verbatim on compact subintervals of the legal interior.

## 10.2 Legal endpoints

The present theorem covers every compact subset of

\[
-\frac{1-c}{2}<s<\frac{1-c}{2},
\tag{10.3}
\]

which is stronger than the assigned interval \([-d_c,d_c]\), but it does not include chords touching the two legal endpoints. At an endpoint one channel level reaches \(0\) or \(1\) at \(u=1\); the common non-nullness constant disappears and the derivatives of \(\phi\) can diverge. Extending (1.9) to endpoint-touching chords requires a new boundary-uniform integrability theorem for the complete V14 kernel, or an approximation argument with a bound strong enough to pass \(s\to\pm(1-c)/2\). That obligation is not claimed here.

## 10.3 Sign

No sign of \(\Gamma_c(s)\) is proved. The exact consequence is now clean:

\[
\Gamma_c(s)\ge0
\quad\Longleftrightarrow\quad
h_c''(s)\le0
\tag{10.4}
\]

at interior points, and nonnegativity on an interval is equivalent to the corresponding entropy-rate chord concavity there. Establishing that sign remains separate.

---

# 11. Final conclusion

The candidate value identity is correct. The complete actual-law finite conditional jet has a compact-uniform exact-sine limit, and the weighted triangular-kernel transfer converts that local limit into the actual entropy-rate chord identity without presupposing differentiability. At the midpoint, the limiting kernel is exactly SA03's unsmoothed V14 object under the true moving law.

Therefore the S51 cycle06 finite-chord/thermodynamic-limit obligation is **PROVED** on the assigned interval.
