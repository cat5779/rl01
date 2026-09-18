# S44 cycle 04 result — projection-completed finite observation jet

**Agent:** S44  
**Date:** 2026-09-18  
**Model scope:** true unsmoothed half-density sine projection channel, \(\rho=1/2\), balanced point \(h=1/2\), \(0<x<1\).  
**Status:** **PROVED (scoped localization theorem); INCOMPLETE (finite \(\Gamma_R^{\rm obs}\) transfer, positivity, and entropy-rate concavity).**

## 1. Executive result

Let \(Q\) be the half-density sine projection on \(\ell^2(\mathbb Z)\),
\[
 Q_{ij}=\frac{\sin (\pi(i-j)/2)}{\pi(i-j)},\qquad Q_{ii}=\frac12,
\]
and let the observed process have kernel
\[
 K_x=\frac12 I+x\Bigl(Q-\frac12I\Bigr),\qquad 0<x<1.
\]
Equivalently, a hidden projection DPP \(X\sim {\rm DPP}(Q)\) is passed through an independent binary symmetric channel of correlation \(x\).

Put
\[
 C=\mathbb Z\setminus\{0\},\qquad C_R=\{j:0<|j|\le R\},
\]
\[
 q_\infty=\mathbb P(Y_0=1\mid Y_C),\qquad
 q_R=\mathbb P(Y_0=1\mid Y_{C_R}),
\]
and \(r_\infty=1/2-q_\infty\), \(r_R=1/2-q_R\).  For
\[
 \theta=2-4\alpha\in[-2,2]
\]
define
\[
 \boxed{
 \psi_{x,\theta}(r)
 =\frac{4x^2(1-4r^2)}{(1-x^2)(1+\theta r)^2}.}
 \tag{1.1}
\]
The **projection-completed radius-\(R\) curvature jet** is the cylinder function
\[
 \boxed{
 \widehat J_{x,\theta,R}(Y_{C_R})=\psi_{x,\theta}(r_R).}
 \tag{1.2}
\]
It is evaluated from the exact sine principal marginal by one \(2R\times2R\) inverse for each retained word.  It contains no full-posterior oracle and no Fejer or cyclic replacement.

The exact infinite Fisher touching optimizer derivative is
\[
 \boxed{
 J_{x,\theta,\infty}
 =\psi_{x,\theta}(r_\infty).}
 \tag{1.3}
\]
Thus the apparently vector-valued response jet closes to one scalar posterior coordinate under the actual projection channel.

Let
\[
 D_x=1+\frac{x^2}{(1-x)^2},
\qquad
 V_Q(L)=\operatorname{Var}_Q N_{\{1,\ldots,L\}}.
\]
Then
\[
 V_Q(L)=\frac2{\pi^2}
 \left(
 \sum_{\substack{1\le n\le L\\ n\ {\rm odd}}}\frac1n
 +L\sum_{\substack{n>L\\ n\ {\rm odd}}}\frac1{n^2}
 \right)
 \le \frac{\log L+4}{\pi^2}.
 \tag{1.4}
\]
The actual-law posterior localization estimate is
\[
 \boxed{
 \mathbb E(r_\infty-r_R)^2
 \le
 \eta_x(R):=
 \frac{x^4D_x}{(1-x^2)^2}
 \frac{V_Q(R+1)}{R+1}.}
 \tag{1.5}
\]
The finite Fisher-dual touching loss paid by replacing the complete infinite jet with (1.2) satisfies
\[
 \boxed{
 \mathcal L^{\rm jet}_{x,R}
 \le
 \mathfrak E_x(R):=
 \frac{128x^8D_x}{(1-x)^8(1+x)^4}
 \frac{V_Q(R+1)}{R+1}.}
 \tag{1.6}
\]
Hence, for every fixed \(x<1\),
\[
 \mathcal L^{\rm jet}_{x,R}
 =O_x\!\left(\frac{\log R}{R}\right).
\]
The constants are uniform on every compact \(0\le x\le c<1\), and the displayed bound degenerates as \(O((1-c)^{-10})\) when \(c\uparrow1\).

The estimate is a complete-curvature estimate, not a bound on \(q\) alone: the exact Fisher touching identity says that the full difference of curvatures, before expanding any moving atom law, is precisely the nonnegative squared error of this optimizer derivative.  Therefore the terms conventionally written as
\[
 w''\phi+2w'\phi'q'+w\{\phi''(q')^2+\phi'q''\}
\]
are all retained.

For \(x=cu\), integration gives the explicit compact-\(c\) **integrated jet-loss budget** (not a bound on \(|\Gamma-\Gamma_R^{\rm obs}|\))
\[
 \boxed{
 \mathfrak E_c^{\rm int\,jet}(R)
 :=\int_0^1u\,\mathfrak E_{cu}(R)\,du
 =C_{\rm jet}(c)\frac{V_Q(R+1)}{R+1},}
 \tag{1.7}
\]
where
\[
 C_{\rm jet}(c)=128\int_0^1
 u\,
 \frac{(cu)^8\left[1+(cu)^2/(1-cu)^2\right]}
 {(1-cu)^8(1+cu)^4}\,du.
 \tag{1.8}
\]
A simple explicit upper bound is
\[
 C_{\rm jet}(c)
 \le
 \frac{64c^8}{(1-c)^8(1+c)^4}
 \left(1+\frac{c^2}{(1-c)^2}\right).
 \tag{1.9}
\]

### Exact error ledger

* **Response-coordinate/optimizer truncation:** zero.  Projection closure sums the complete infinite response energy exactly.
* **Observation-domain jet loss:** bounded by (1.6), with rate \(O_x((\log R)/R)\).
* **Kernel-change error:** zero.  Every finite object is an exact principal marginal of the true sine kernel.
* **Touching-baseline/Galerkin transfer to \(F_{x,R}''\): open.**  The theorem does not bound
  \[
  \underline F_{x,\infty}''[\widehat J_R]
  -\underline F_{x,R}''[\widehat J_R]
  \]
  or, equivalently, \(F_{x,\infty}''-F_{x,R}''\).  The two touching functionals have different zeroth-order optimizers.  A squared-error bound for the first derivative does not determine the second derivative of the non-touching zeroth-order residual.

Consequently, **no finite radius is certified here to prove \(\Gamma(19/20)>0\)**.  There is also **no entropy-rate concavity conclusion**.

---

## 2. Exact finite posterior notation

For an exterior word \(z\), put \(\sigma_i=2z_i-1\), \(S_z=\operatorname{diag}(\sigma_i)\), and
\[
 A=Q-\frac12I.
\]
On \(C\), at \(h=1/2\),
\[
 B_z=\frac12S_z+xA_C,
 \qquad G_z=B_z^{-1},
 \qquad b=xQ_{C0},
\]
\[
 v=G_zb,
 \qquad r=b^*G_zb,
 \qquad q=\frac12-r.
 \tag{2.1}
\]
For \(C_R\), use the corresponding principal matrices
\[
 B_R=P_RB_zP_R,
 \quad G_R=B_R^{-1},
 \quad b_R=P_Rb,
 \quad v_R=G_Rb_R,
 \quad r_R=b_R^*v_R.
 \tag{2.2}
\]
These are the exact conditional data for observing \(z_R\), not a boundary condition imposed on the unobserved word.

Since \(\|A_C\|\le1/2\),
\[
 B_z=\frac12S_z(I+2xS_zA_C),
\]
so the Neumann bound gives, for every word and every principal window,
\[
 \boxed{\|G_z\|,\ \|G_R\|\le\frac2{1-x}.}
 \tag{2.3}
\]
Also
\[
 \|b\|^2=x^2\sum_{j\ne0}|Q_{j0}|^2
 =x^2(Q_{00}-Q_{00}^2)=\frac{x^2}{4}.
 \tag{2.4}
\]

---

## 3. Schur-domain localization on the actual word

Let \(I=C_R\), \(O=C\setminus I\), and extend \(v_R\) by zero to a vector \(\widetilde v_R\in\ell^2(C)\).  The full and finite equations give
\[
 B_{II}v_I+B_{IO}v_O=b_I,
 \qquad B_{II}v_R=b_I,
\]
therefore
\[
 v_I-v_R=-G_RB_{IO}v_O.
 \tag{3.1}
\]
For any orthogonal projection and any partition,
\[
 Q_{I,I^c}Q_{I^c,I}=Q_{II}-Q_{II}^2\le\frac14I.
\]
As \(O\subset I^c\),
\[
 \|Q_{IO}\|\le\frac12,
 \qquad \|B_{IO}\|=x\|Q_{IO}\|\le\frac x2.
 \tag{3.2}
\]
Combining (2.3), (3.1), and (3.2),
\[
 \|v_I-v_R\|
 \le\frac{x}{1-x}\|v_O\|.
\]
Consequently, with
\[
 \tau_R:=\|v_O\|^2=\sum_{|j|>R}|v_j|^2,
\]
we obtain the deterministic same-word estimate
\[
 \boxed{
 \|v-\widetilde v_R\|^2
 \le D_x\tau_R,
 \qquad D_x=1+\frac{x^2}{(1-x)^2}.}
 \tag{3.3}
\]
Since \(r-r_R=b^*(v-\widetilde v_R)\), (2.4) gives
\[
 \boxed{
 |r-r_R|^2\le\frac{x^2D_x}{4}\tau_R.}
 \tag{3.4}
\]
This is the resolvent-domain decomposition promised by the task: no unobserved coordinate is filled with a guessed sign, and the only remaining random error is a true full-response tail.

A direct corollary also controls the first posterior derivative.  Since
\[
 q_\infty'=1+\|v\|^2,
 \qquad q_R'=1+\|v_R\|^2,
 \qquad \|v\|,\|v_R\|\le\frac{x}{1-x},
\]
(3.3) implies
\[
 |q_\infty'-q_R'|^2
 \le\frac{4x^2D_x}{(1-x)^2}\tau_R.
 \tag{3.5}
\]
After averaging, (3.5) has the same \((\log R)/R\) rate as (1.5).  No analogous claim about \(q''\) is used below; the Fisher touching identity bypasses that missing scalar estimate.

---

## 4. Hidden posterior projection and the response dictionary

This is the transferable mechanism.  It combines a Bayesian exponential tilt of a projection process with a Woodbury/Galerkin resolvent identity.

Write \(Q=UU^*\), where \(U:\operatorname{Ran}Q\to\ell^2(\mathbb Z)\) is the canonical isometry.  Given an observed exterior word, set
\[
 d_i^2=\frac{1+\sigma_i x}{1-\sigma_i x}\quad(i\in C),
 \qquad d_0=1,
 \qquad D=\operatorname{diag}(d_i).
 \tag{4.1}
\]
Bayes' formula multiplies a hidden configuration by \(\prod_{i\in X}d_i^2\).  Hence the hidden law conditioned on the exterior output is the projection DPP with kernel
\[
 \boxed{
 \Pi^-=DU(U^*D^2U)^{-1}U^*D.}
 \tag{4.2}
\]
It is an orthogonal projection because
\[
 (\Pi^-)^2
 =DU M^{-1}(U^*D^2U)M^{-1}U^*D
 =\Pi^-,
 \quad M=U^*D^2U.
\]
The bounds \((1-x)/(1+x)\le d_i^2\le(1+x)/(1-x)\) make the infinite operator uniformly invertible.  Finite tilts converge strongly, so (4.2) is also the actual full-exterior posterior projection.

To connect (4.2) with (2.1), write on \(C\)
\[
 B=A_0+xU_CU_C^*,
 \qquad (A_0)_{ii}=\frac{\sigma_i-x}{2}.
\]
Then
\[
 U^*D^2U=I+xU_C^*A_0^{-1}U_C.
\]
Woodbury gives
\[
 G=A_0^{-1}-xA_0^{-1}U_C
 (U^*D^2U)^{-1}U_C^*A_0^{-1}.
\]
In particular, for \(i\in C\),
\[
 \boxed{
 v_i=\frac{2x\sigma_i}{\sqrt{1-x^2}}\,\Pi^-_{i0},}
 \tag{4.3}
\]
and, for distinct \(i,j\in C\),
\[
 \boxed{
 G_{ij}=-\frac{4x\sigma_i\sigma_j}{1-x^2}\,\Pi^-_{ij}.}
 \tag{4.4}
\]
The second identity is not needed for (1.6), but is a reusable dictionary for future localization of the full signed curvature kernel.

Let
\[
 p=\Pi^-_{00}=\mathbb P(X_0=1\mid Y_C).
\]
The binary symmetric channel gives
\[
 q_\infty=\frac{1-x}{2}+xp,
 \qquad r_\infty=x\left(\frac12-p\right).
 \tag{4.5}
\]
Because \(\Pi^-\) is a projection,
\[
 \sum_{j\ne0}|\Pi^-_{0j}|^2=p-p^2.
 \tag{4.6}
\]
Equations (4.3)--(4.6) yield
\[
 \|v\|^2
 =\frac{4x^2}{1-x^2}p(1-p)
 =\frac{x^2-4r_\infty^2}{1-x^2},
 \tag{4.7}
\]
and therefore the exact response closure
\[
 \boxed{
 \|v\|^2+4r_\infty^2
 =\frac{x^2(1-4r_\infty^2)}{1-x^2}.}
 \tag{4.8}
\]

---

## 5. Actual-law response-tail estimate

From (4.3),
\[
 \tau_R
 =\frac{4x^2}{1-x^2}
 T_R^-,
 \qquad
 T_R^-:=\sum_{|j|>R}|\Pi^-_{0j}|^2.
 \tag{5.1}
\]
Now reveal the center output \(Y_0\).  If \(y=2Y_0-1\), \(t=2p-1\), and \(\Pi^+\) denotes the posterior projection after all outputs have been revealed, a one-coordinate likelihood tilt gives
\[
 |\Pi^+_{0j}|^2
 =\frac{1-x^2}{(1+yx t)^2}|\Pi^-_{0j}|^2,
\]
while
\[
 \mathbb P(y\mid Y_C)=\frac{1+yx t}{2}.
\]
Thus, with \(d=1-x^2t^2\le1\),
\[
 \mathbb E(T_R^+\mid Y_C)
 =\frac{1-x^2}{d}T_R^-
 \ge(1-x^2)T_R^-,
 \tag{5.2}
\]
where
\[
 T_R^+=\sum_{|j|>R}|\Pi^+_{0j}|^2.
\]
Hence
\[
 \mathbb ET_R^-\le\frac1{1-x^2}\mathbb ET_R^+.
 \tag{5.3}
\]

For an interval \(I_L\) of length \(L\), conditional projection variance gives
\[
 \operatorname{Var}(N_{I_L}\mid Y)
 =\sum_{i\in I_L,j\notin I_L}|\Pi^+_{ij}|^2.
\]
The law of total variance and stationarity imply
\[
 L\sum_{|j|\ge L}\mathbb E|\Pi^+_{0j}|^2
 \le V_Q(L).
 \tag{5.4}
\]
Taking \(L=R+1\) in (5.1)--(5.4),
\[
 \boxed{
 \mathbb E\tau_R
 \le
 \frac{4x^2}{(1-x^2)^2}
 \frac{V_Q(R+1)}{R+1}.}
 \tag{5.5}
\]
Combining (3.4) and (5.5) proves (1.5).  Combining (3.5) and (5.5) also gives
\[
 \boxed{
 \mathbb E|q_\infty'-q_R'|^2
 \le
 \frac{16x^4D_x}{(1-x)^2(1-x^2)^2}
 \frac{V_Q(R+1)}{R+1}.}
 \tag{5.6}
\]

---

## 6. Closure of the complete Fisher curvature jet

For the affine mixture of the two actual exterior laws conditioned on \(Y_0=1\) and \(Y_0=0\), the Pearson--Fisher quadratic dual is
\[
 \mathcal I_h(\alpha)
 =\sup_f\sum_z\{2d_h(z)f(z)-p_{h,\alpha}(z)f(z)^2\},
\]
with optimizer \(f_{*,h,\alpha}=d_h/p_{h,\alpha}\).  Completing the square gives the exact gap
\[
 \mathcal I_h(\alpha)-\mathcal Q_h(\alpha;f)
 =\mathbb E_{p_{h,\alpha}}(f-f_{*,h,\alpha})^2.
 \tag{6.1}
\]
At \(h_0=1/2\), take a touching path
\[
 f_{h,\alpha}=f_{*,h_0,\alpha}+(h-h_0)k_\alpha.
\]
The gap and its first derivative vanish at \(h_0\), so differentiating (6.1) twice yields the exact curvature loss
\[
 F_x''(1/2)-\underline F_x''[k]
 =\frac12\int_0^1
 \mathbb E_{p_\alpha}(k_\alpha-\dot f_{*,\alpha})^2\,d\alpha.
 \tag{6.2}
\]
This identity is obtained before expanding any atom derivative and therefore retains the complete moving-law curvature.

At \(h=1/2\), write \(\theta=2-4\alpha\),
\[
 R_\theta=(B+\theta bb^*)^{-1}.
\]
The rank-one inverse formula gives
\[
 R_\theta b=\frac{v}{1+\theta r},
 \qquad
 b^*R_\theta b=\frac r{1+\theta r}.
\]
The exact optimizer derivative is
\[
 \dot f_{*,\alpha}
 =4b^*R_\theta(I+4bb^*)R_\theta b
 =\frac{4(\|v\|^2+4r^2)}{(1+\theta r)^2}.
 \tag{6.3}
\]
Substitution of (4.8) into (6.3) proves (1.3).

The same formula is first proved in every finite full exterior and then passed to the infinite exterior.  The resolvent bounds, \(|r|\le x/2\), and (5.5) give bounded convergence.  Thus no formal infinite determinant differentiation is required for the localization statement.

---

## 7. Lipschitz estimate and proof of the jet loss

Put \(y=2r\in[-x,x]\), \(s=\theta/2\in[-1,1]\).  Differentiating (1.1),
\[
 \partial_r\psi_{x,\theta}(r)
 =-\frac{8x^2(4r+\theta)}{(1-x^2)(1+\theta r)^3}
 =-\frac{16x^2}{1-x^2}
 \frac{y+s}{(1+ys)^3}.
 \tag{7.1}
\]
The elementary identity
\[
 (1+ys)^2-(y+s)^2=(1-y^2)(1-s^2)\ge0
\]
shows that \(|y+s|\le1+ys\).  Since \(1+ys\ge1-x\),
\[
 \boxed{
 |\partial_r\psi_{x,\theta}(r)|
 \le L_\psi(x):=
 \frac{16x^2}{(1-x)^3(1+x)}.}
 \tag{7.2}
\]
Therefore
\[
 |J_{x,\theta,\infty}-\widehat J_{x,\theta,R}|
 \le L_\psi(x)|r_\infty-r_R|.
 \tag{7.3}
\]
At \(h=1/2\), the mixture law has density
\[
 p_\theta=w(1+\theta r_\infty)
\]
relative to the actual exterior law \(w\).  Changing variables in (6.2),
\[
 \mathcal L^{\rm jet}_{x,R}
 =\frac18\int_{-2}^2
 \mathbb E_w\!
 \left[(1+\theta r_\infty)
 (J_{x,\theta,\infty}-\widehat J_{x,\theta,R})^2\right]d\theta.
 \tag{7.4}
\]
Use (7.3), then integrate the weight exactly:
\[
 \int_{-2}^2(1+\theta r_\infty)d\theta=4.
\]
Thus
\[
 \mathcal L^{\rm jet}_{x,R}
 \le\frac12L_\psi(x)^2\mathbb E(r_\infty-r_R)^2.
 \tag{7.5}
\]
Equations (1.5), (7.2), and (7.5) give (1.6).

For the integrated bound, the coefficient
\[
 A(x)=\frac{x^8[1+x^2/(1-x)^2]}{(1-x)^8(1+x)^4}
 =\frac{x^8(1-2x+2x^2)}{(1-x)^{10}(1+x)^4}
\]
is increasing on \((0,1)\).  Indeed,
\[
 \frac{A'(x)}{A(x)}
 =\frac8x+\frac{4x-2}{1-2x+2x^2}
 +\frac{10}{1-x}-\frac4{1+x}>0;
\]
for \(x\le1/2\), the second term is at least \(-2\), and for \(x\ge1/2\) it is nonnegative.  This proves (1.9).

---

## 8. The finite jet is an exact projection completion

The object (1.2) is not an arbitrary scalar ansatz.  Let \(\Pi_R^-\) be the hidden posterior projection after observing only \(Y_{C_R}\), and let
\[
 p_R=(\Pi_R^-)_{00}
 =\frac12-\frac{r_R}{x}.
\]
For \(i\in C_R\), the finite response satisfies
\[
 |(v_R)_i|^2
 =\frac{4x^2}{1-x^2}|(\Pi_R^-)_{i0}|^2.
 \tag{8.1}
\]
Define the latent covariance energy not represented by finite output response coordinates,
\[
 \mathcal T_R^{\rm hid}
 :=\sum_{j\notin C_R\cup\{0\}}
 |(\Pi_R^-)_{0j}|^2
 =p_R(1-p_R)-\frac{1-x^2}{4x^2}\|v_R\|^2
 \ge0.
 \tag{8.2}
\]
The exact derivative of the finite-model Fisher optimizer is
\[
 J^{\rm fin}_{x,\theta,R}
 =\frac{4(\|v_R\|^2+4r_R^2)}{(1+\theta r_R)^2}.
 \tag{8.3}
\]
Projection closure gives the identity
\[
 \boxed{
 \widehat J_{x,\theta,R}
 =J^{\rm fin}_{x,\theta,R}
 +\frac{16x^2}{1-x^2}
 \frac{\mathcal T_R^{\rm hid}}
 {(1+\theta r_R)^2}.}
 \tag{8.4}
\]
Every quantity in (8.4) is finite-window computable.  The second term is the explicit correction that completes the finite response coordinates to the full latent projection row.

Equation (8.4) is also the obstruction to an unjustified identification with \(F_{x,R}''\): except when the hidden tail vanishes, the projection-completed jet is not the derivative of the finite marginal optimizer.

---

## 9. Zeroth-order Fisher score localization

The same construction localizes the touching base score.  At \(h=1/2\),
\[
 f_{x,\theta,\infty}
 =-\frac{4r_\infty}{1+\theta r_\infty},
 \qquad
 f_{x,\theta,R}
 =-\frac{4r_R}{1+\theta r_R}.
 \tag{9.1}
\]
Since \(r_R=\mathbb E_w(r_\infty\mid\mathcal F_R)\),
\[
 \boxed{
 \mathbb E_{p_\theta}
 [f_{x,\theta,\infty}\mid\mathcal F_R]
 =f_{x,\theta,R}.}
 \tag{9.2}
\]
Thus the finite score is the exact Hilbert-space/Galerkin projection of the full score.  Moreover,
\[
 f_{x,\theta,\infty}-f_{x,\theta,R}
 =-\frac{4(r_\infty-r_R)}
 {(1+\theta r_\infty)(1+\theta r_R)},
\]
so
\[
 \boxed{
 \mathbb E_{p_\theta}
 (f_{x,\theta,\infty}-f_{x,\theta,R})^2
 \le\frac{16}{(1-x)^3}\eta_x(R).}
 \tag{9.3}
\]
Equations (9.2), (9.3), and (1.6) localize the complete first-order Fisher jet \((f_*,\dot f_*)\).

They still do not, by themselves, compare the second derivatives of the two optimized value functions.  The finite and infinite quadratic duals touch at different zeroth-order optimizers.  Differentiating the nonzero residual between those two bases creates a signed Galerkin-curvature term.  Bounding that term is the precise remaining observation-to-\(\Gamma_R^{\rm obs}\) obligation.

---

## 10. Exact scope and open obligation

### PROVED

1. The full exterior posterior response and the finite observed response can be coupled on the same actual output word by (3.3).
2. Their scalar posteriors satisfy the explicit actual-law \(L^2\) estimate (1.5).
3. The hidden posterior is a projection and gives the response dictionary (4.3)--(4.4).
4. The full optimal Fisher curvature jet closes exactly to (1.3).
5. The finite measurable, projection-completed jet (1.2) pays the complete curvature loss (1.6), at rate \(O_x((\log R)/R)\).
6. The finite base score is the exact conditional-expectation projection of the full score, with error (9.3).
7. No Fejer-to-sine or cyclic-kernel error occurs.

### INCOMPLETE

1. A bound for
   \[
   |F_{x,\infty}''(1/2)-F_{x,R}''(1/2)|
   \]
   or its one-sided analogue.  The missing term is the curvature of the zeroth-order Galerkin residual, not the optimizer-derivative tail already paid in (1.6).
2. A finite, certified positive lower bound for \(\Gamma(19/20)\).
3. Extension away from \(\rho=1/2\) or away from the balanced point.
4. The bridge from local \(\Gamma\)-positivity to concavity of the full Shannon entropy rate on the entire legal \(a\)-interval.

### DISPROVED as a natural shortcut

The identity
\[
 \widehat J_{x,\theta,R}=J^{\rm fin}_{x,\theta,R}
\]
is false in general.  The exact nonnegative discrepancy is (8.4).  Therefore finite posterior closeness cannot be converted into a comparison with \(\Gamma_R^{\rm obs}\) by silently treating the projection-completed jet as the finite-marginal optimizer derivative.

---

## 11. Transferable mechanism

The construction imports two standard mechanisms and makes their DPP hypotheses explicit.

* **Static condensation / Schur-domain decomposition.**  In numerical PDE and domain decomposition, the error of a restricted solve is driven by the omitted part of the full solution through the interface block.  Equation (3.1) is exactly that mechanism; projection geometry supplies the sharp interface norm \(\|Q_{IO}\|\le1/2\).
* **Bayesian projection geometry plus Galerkin duality.**  A diagonal likelihood tilt maps a projection DPP to another orthogonal projection.  Woodbury converts output resolvents into entries of that posterior projection.  The Pearson--Fisher quadratic dual then turns approximation of the optimizer derivative into an exact nonnegative curvature loss.  No positivity of the signed word transport is assumed.

This is reusable beyond the sine kernel whenever (i) the hidden kernel is a projection, (ii) the observation channel is a uniformly nondegenerate coordinatewise binary channel, and (iii) a number-variance bound is available.

---

## 12. Reproducibility

`S44_checks.py` verifies on random finite Fourier projections:

1. the posterior projection formula;
2. the exact response identities (4.3)--(4.4);
3. the full-response scalar closure (4.8);
4. the finite completion identity (8.4);
5. the deterministic Schur localization inequality (3.3);
6. the displayed constants and sine number-variance bound.

The computation is diagnostic only; the proof above is algebraic.

## Source ledger

The task prompt and model conventions were read from:

* `prompts/CYCLE04/S44.md`
* `TARGET.md`
* `research/CYCLE04_20260918/S41_PARTIAL.md` (pending review; used only for comparison and notation, not as a load-bearing proof)
* `research/CYCLE03_20260918/reviews/S42.md` (independently scoped review of the projection/number-variance tail)
* `research/HARVEST_20260918/S17_RESULT.md` (finite Fisher dual; its completion-of-squares argument is reproduced above)
* `results/SA03/SA03_VOLUME_LIMIT.md` and `results/SA03/SA03_EFFECTIVE_REMAINDER.md` (not used to claim an infinite \(\Gamma\) value or sign here)
