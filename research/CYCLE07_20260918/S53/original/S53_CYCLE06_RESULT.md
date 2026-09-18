# S53 cycle06 — curvature of a moving conditional-expectation projection

**Status: PROVED (scoped, source-relative).**

For the true half-filled sine family
\[
K_x(h)=hI+x\left(Q-\frac12I\right),\qquad 0<x<1,
\]
let
\[
\mathcal F_{x,J}(h)=\frac14\int_0^1 I_h^J(\alpha)\,d\alpha
\]
with the exact principal marginal on the finite observation set \(J\).
For
\[
J_R=\{j\in\mathbb Z:0<|j|\le R\},
\]
this manuscript proves an explicit function \(B_x(R)\downarrow0\) such that,
for every finite \(E\supset J_R\),
\[
\boxed{
\left|\mathcal F_{x,E}''(1/2)-\mathcal F_{x,J_R}''(1/2)\right|
\le B_x(R).}
\]
The rate obtained is
\[
B_x(R)=O_x\!\left(\sqrt{\frac{\log R}{R}}\right).
\]
Hence the directed net of finite curvatures is Cauchy and defines an
exhaustion-independent quantity \(\mathcal F_{x,\infty}''(1/2)\), with the
same radius-\(R\) error bound.  The constants are uniform for
\(0\le x\le c<1\), and
\[
\int_0^1uB_{cu}(R)\,du\longrightarrow0.
\]

This is the requested touching-baseline/Galerkin bridge at half filling and at
the balanced point.  It does **not** prove \(\Gamma>0\), off-midpoint
curvature, all-\(\rho\) entropy-rate concavity, or differentiability of the
limiting Shannon entropy rate.

## Source interfaces actually used

From `S44_RESULT.md`:

1. the hidden posterior after diagonal likelihood tilts is an orthogonal
   projection;
2. for the posterior after all outputs are observed,
   \[
   L\sum_{|j|\ge L}\mathbb E|P_{0j}^{\star}|^2\le V_Q(L),
   \qquad
   V_Q(L)\le\frac{\log L+4}{\pi^2};
   \]
3. the scalar posterior localization
   \[
   \mathbb E(q_\infty-q_R)^2\le
   \eta_x(R):=
   \frac{x^4D_x}{(1-x^2)^2}\frac{V_Q(R+1)}{R+1},
   \qquad D_x=1+\frac{x^2}{(1-x)^2};
   \]
4. the posterior/resolvent dictionary used below.

From `S41_CYCLE05_RESULT.md`:

1. the complete finite curvature kernel \(\mathscr K_{x,E}\);
2. its tail estimate with
   \(C_{\rm tail}(x)=2^{12}(2/(1-x))^{25}\);
3. the repaired directional estimate containing the necessary \(Z_0\) term,
   with \(C_{\rm dir}(x)=2^{26}(2/(1-x))^{36}\);
4. Gronwall stability of \(T_0+W_0+Z_0\) under outside diagonal tilts;
5. the anchor add/remove factor \(s_x^4\),
   \(s_x=\sqrt{(1+x)/(1-x)}\).

The S41 final frozen-functional identification is **not** imported.  The exact
moving-law interface between finite derivatives and \(\mathscr K\) is proved
in Section 4.  The imported manuscripts are author submissions pending
separate review; this document is not an independent certification of their
long finite-kernel ledgers.

---

## 1. Exact moving-Galerkin curvature identity

This is the reusable mechanism, independent of DPP theory.

Fix \(\alpha\), a finite fine state space \(\Omega_M\), and the fixed coarse
subspace \(V_R=L^2(\sigma(Y_{J_R}))\).  Let
\[
p_h=p_{h,\alpha}^M,\qquad d_h=d_h^M,
\qquad
\langle u,v\rangle_h=\sum_{\omega\in\Omega_M}p_h(\omega)u(\omega)v(\omega).
\]
Let \(P_h\) be conditional expectation onto \(V_R\) in the moving inner
product.  Put
\[
f_h=\frac{d_h}{p_h},\qquad g_h=P_hf_h,\qquad e_h=f_h-g_h.
\]
Exact marginalization gives
\[
g_h=f_{*,h,\alpha}^{J_R},
\qquad
I_h^M(\alpha)-I_h^{J_R}(\alpha)=\|e_h\|_h^2.
\]
At a base point \(h_0\) (later \(h_0=1/2\)), write
\[
s=\frac{p'}p,\qquad t=\frac{p''}p,
\qquad u=\frac{d'}p,\qquad v=\frac{d''}p,
\]
and define
\[
k=u-sg,
\qquad z=(I-P)k,
\qquad P=P_{h_0}.
\]
All unlabelled quantities below are evaluated at \(h_0\).

### Theorem 1.1 — covariant Galerkin second variation

\[
\boxed{
\begin{aligned}
\frac{d^2}{dh^2}\left(I_h^M(\alpha)-I_h^{J_R}(\alpha)\right)\Big|_{h_0}
={}&2\|z\|_p^2\\
&+2\langle e,\,v-tg-2sk\rangle_p\\
&+\langle e,(2s^2-t)e\rangle_p .
\end{aligned}}
\tag{1.1}
\]
Moreover
\[
\boxed{z=e'+se,\qquad z\perp_pV_R.}
\tag{1.2}
\]
Equivalently,
\[
\boxed{
D''=2\|e'+se\|_p^2+2\langle e,f''\rangle_p
     +\langle e,(t-2s^2)e\rangle_p,
}
\tag{1.3}
\]
where \(D=I^M-I^{J_R}\).

### Proof

The fine and coarse optimizers satisfy
\[
\langle f,\varphi\rangle_p=\sum d\varphi
\quad(\varphi\text{ arbitrary}),
\qquad
\langle g,\varphi\rangle_p=\sum d\varphi
\quad(\varphi\in V_R).
\]
Thus \(e\perp_pV_R\).  Differentiating the coarse equation gives
\[
\langle g'+sg,\varphi\rangle_p=\langle u,\varphi\rangle_p,
\qquad
\varphi\in V_R,
\]
so
\[
g'=P(u-sg)=Pk.
\tag{1.4}
\]
Since \(f'=u-sf\),
\[
e'+se=f'-g'+se=k-Pk=z,
\]
which proves (1.2), including the derivative of the moving conditional
expectation.

For an optimized quadratic functional
\[
I_h=\sup_a\sum_\omega\{2d_h a-p_h a^2\},
\]
the finite-dimensional envelope identity is
\[
I_h''=2\sum d_h''f_h-\sum p_h''f_h^2
      +2\sum p_h(f_h')^2.
\tag{1.5}
\]
Subtract the coarse identity and lift coarse functions to \(\Omega_M\):
\[
D''=2\langle v,e\rangle_p
     -\langle t(f+g),e\rangle_p
     +2(\|f'\|_p^2-\|g'\|_p^2).
\tag{1.6}
\]
Now \(f'=g'+z-se\), with \(z\perp_pg'\).  Because
\(k=g'+z\),
\[
\|f'\|_p^2-\|g'\|_p^2
=\|z\|_p^2-2\langle sk,e\rangle_p+\|se\|_p^2.
\tag{1.7}
\]
Substitution into (1.6), followed by \(f=g+e\), proves (1.1).
Finally, differentiating \(d=pf\) twice gives
\[
v=tf+2sf'+f'',
\]
which converts (1.1) to (1.3).  Every moving-law, moving-projection,
optimizer, and normalization derivative is present. ∎

After integrating \(\alpha\),
\[
\boxed{
\mathcal F_{x,E}''(1/2)-\mathcal F_{x,J_R}''(1/2)
=\frac14\int_0^1D_{E,R,\alpha}''(1/2)\,d\alpha.}
\tag{1.8}
\]

### First-jet obstruction

The positive term \(2\|z\|^2\) is not the whole curvature.  At
\(\alpha=1/2\), take two atoms with \(p_h(\pm)=1/2\), trivial coarse
sigma-field, and
\[
d_h(\pm)=\pm\left(r+jh+\frac12ch^2\right).
\]
For \(|r|<1\) and small \(h\),
\(P_{1,h}=p_h+d_h/2\) and \(P_{0,h}=p_h-d_h/2\) are probability laws.
The base residual and first optimizer jet depend only on \(r,j\), but
\[
D''(0)=8(j^2+rc),
\]
which can be varied arbitrarily through \(c\).  Therefore no general lemma
can control moving-projection curvature from the base and first jet alone.
This refutes that ansatz, not the true-sine claim.

---

## 2. The explicit bound

Set
\[
s_x=\sqrt{\frac{1+x}{1-x}},
\qquad
\Lambda_x=\frac2{1-x},
\qquad
A_Q(L)=\frac{V_Q(L)}L.
\tag{2.1}
\]
For \(k=1,2,3\), let
\[
L_k(R)=\left\lfloor\frac Rk\right\rfloor+1,
\]
and put
\[
\upsilon(R)=A_Q(L_1(R))+2A_Q(L_2(R))+3A_Q(L_3(R)).
\tag{2.2}
\]
Since \(L_k(R)\ge(R+1)/k\),
\[
\upsilon(R)
\le\frac{14\{\log(R+1)+4\}}{\pi^2(R+1)}.
\tag{2.3}
\]
Retain the S44 quantity
\[
\eta_x(R)=
\frac{x^4D_x}{(1-x^2)^2}A_Q(R+1),
\qquad
D_x=1+\frac{x^2}{(1-x)^2}.
\tag{2.4}
\]
Let
\[
C_{\rm tail}(x)=2^{12}\Lambda_x^{25},
\qquad
C_{\rm dir}(x)=2^{26}\Lambda_x^{36}.
\tag{2.5}
\]
Define
\[
\boxed{
\begin{aligned}
B_x(R)={}&s_x^{12}\bigl(C_{\rm tail}(x)+4\Lambda_x^9\bigr)\upsilon(R)\\
&+s_x^4(s_x^2-1)
 \left(\frac{\sqrt3}{2}C_{\rm dir}(x)
       +5\sqrt2\,\Lambda_x^{11}\right)\sqrt{\upsilon(R)}\\
&+\frac{32}{(1-x^2)^2}\eta_x(R).
\end{aligned}}
\tag{2.6}
\]

### Theorem 2.1 — fixed-anchor true-sine curvature bridge

For every \(0<x<1\), every \(R\ge1\), and every finite observation set
\(E\supset J_R\),
\[
\boxed{
\left|\mathcal F_{x,E}''(1/2)-\mathcal F_{x,J_R}''(1/2)\right|
\le B_x(R).}
\tag{2.7}
\]
Consequently
\[
\mathcal F_{x,\infty}''(1/2)
:=\lim_{E\uparrow\mathbb Z\setminus\{0\}}\mathcal F_{x,E}''(1/2)
\]
exists as a directed-net limit, independently of the exhaustion, and
\[
\boxed{
\left|\mathcal F_{x,\infty}''(1/2)
      -\mathcal F_{x,J_R}''(1/2)\right|
\le B_x(R).}
\tag{2.8}
\]
The remaining sections prove this theorem.

---

## 3. Exact normalization: Fisher integral versus the moving posterior law

Let \(w_h^J\) be the actual exterior law and
\[
q_h^J(z)=\mathbb P_h(Y_0=1\mid Y_J=z).
\]
The center marginal is exactly \(h\), so
\[
P_{(h,1)}^J(z)=w_h^J(z)\frac{q_h^J(z)}h,
\qquad
P_{(h,0)}^J(z)=w_h^J(z)\frac{1-q_h^J(z)}{1-h}.
\tag{3.1}
\]
For positive \(a,b\),
\[
\int_0^1\frac{(a-b)^2}{\alpha a+(1-\alpha)b}\,d\alpha
=(a-b)\log\frac ab.
\tag{3.2}
\]
Therefore \(4\mathcal F\) is the Jeffreys divergence between the two
conditional exterior laws, and
\[
\boxed{
\mathcal F_{x,J}(h)=\mathbb E_{w_h^J}\Phi(h,q_h^J),}
\tag{3.3}
\]
where
\[
\Phi(h,q)=\frac14\frac{q-h}{h(1-h)}
\left(\log\frac q{1-q}-\log\frac h{1-h}\right).
\tag{3.4}
\]
Put
\[
\ell(q)=\log\frac q{1-q},
\qquad
\phi(q)=\left(q-\frac12\right)\ell(q),
\qquad
\chi(q)=2-4q-\ell(q).
\tag{3.5}
\]
At fixed \(q\), direct differentiation gives
\[
\Phi(1/2,q)=\phi(q),
\qquad
\partial_h\Phi(1/2,q)=\chi(q),
\qquad
\partial_h^2\Phi(1/2,q)=8+8\phi(q).
\tag{3.6}
\]
Define
\[
G_J(h)=\mathbb E_{w_h^J}\phi(q_h^J),
\qquad
H_J(h)=\mathbb E_{w_h^J}\chi(q_h^J).
\tag{3.7}
\]
Expanding the integrand before differentiating the moving expectation gives
\[
\boxed{
\mathcal F_{x,J}''(1/2)
=G_J''(1/2)+2H_J'(1/2)+8+8G_J(1/2).}
\tag{3.8}
\]
This is the required normalization correction.  The equality
\(\mathcal F(1/2)=G(1/2)\) alone cannot be differentiated.

---

## 4. Exact finite channel calculus and the complete-kernel interface

For a finite observation set \(E\), encode a word by signs
\(y_i\in\{+1,-1\}\), put \(S_y=\operatorname{diag}(y_i)\), and write the
exact atom law as
\[
w_h^E(y)=(-1)^{n_-(y)}\det B_h(y),
\qquad
B_h(y)=\left(h-\frac12\right)I+\frac12S_y
       +x\left(Q_E-\frac12I\right).
\tag{4.1}
\]
Thus \(B_h'=I\).  Let \(G_h=B_h^{-1}\).  The Schur posterior of the anchor
is
\[
q_h=h-b^*G_hb,
\]
with \(b=xQ_{E0}\), and put \(v=G_hb\).  Define
\[
r_i=y_i-(G_h)_{ii},
\qquad d_i=q_h(y^i)-q_h(y)=-\frac{|v_i|^2}{r_i}.
\tag{4.2}
\]
At \(h=1/2\), the S44 dictionary identifies these objects with entries of the
hidden posterior projection \(P\); in particular
\[
q=\frac12+x\left(P_{00}-\frac12\right),
\qquad
|v_i|\le\Lambda_x|P_{i0}|.
\tag{4.3}
\]
All one- and two-flip posteriors remain in
\([\frac{1-x}{2},\frac{1+x}{2}]\).

For smooth \(f\), define
\[
B_f(q,d)=f(q+d)-f(q)-f'(q)d,
\qquad
\mathcal B_{f,E}=f'(q)+\sum_{i\in E}r_iB_f(q,d_i).
\tag{4.4}
\]

### Lemma 4.1 — exact flip-generator derivative

For any differentiable word functional \(A_h(y)\), with a dot denoting the
fixed-word derivative,
\[
\boxed{
\frac d{dh}\mathbb E_{w_h^E}A_h\Big|_{h=1/2}
=\mathbb E\left[\dot A+
 \sum_{i\in E}r_i\{A(y^i)-A(y)\}\right].}
\tag{4.5}
\]
Consequently,
\[
\boxed{
\frac d{dh}\mathbb E_{w_h^E}f(q_h)\Big|_{h=1/2}
=\mathbb E\mathcal B_{f,E}.}
\tag{4.6}
\]

### Proof

From (4.1),
\[
\frac{w_h'(y)}{w_h(y)}=\operatorname{Tr}G_h.
\]
The determinant lemma and Sherman--Morrison formula give
\[
\frac{w_h(y^i)}{w_h(y)}=-y_ir_i,
\qquad
r_i(y^i)=-\frac1{r_i(y)}.
\tag{4.7}
\]
Changing variables \(y\leftrightarrow y^i\),
\[
\mathbb E\,r_i\{A(y^i)-A(y)\}
=\mathbb E\,(y_i-r_i)A
=\mathbb E\,(G_h)_{ii}A.
\]
Summing over \(i\) proves (4.5).

For \(A_h=f(q_h)\),
\[
\dot q=A_E:=1+\sum_{i\in E}|v_i|^2,
\qquad
r_id_i=-|v_i|^2,
\]
so (4.5) becomes
\[
\mathbb E\left[f'(q)A_E+
 \sum_i r_i\{f(q+d_i)-f(q)\}\right].
\]
Because \(A_E=1-\sum_i r_id_i\), this is exactly
\(\mathbb E\mathcal B_{f,E}\). ∎

The identity (4.6) holds throughout a neighborhood with the corresponding
\(h\)-dependent Schur variables, not merely at one isolated point.  It may
therefore be differentiated.  The fixed-word derivatives are
\[
\dot q=A_E,
\qquad
\dot r_i=R_{i,E}:=\sum_{k\in E}|G_{ki}|^2,
\qquad
\dot d_i=A_E^i-A_E,
\tag{4.8}
\]
where
\[
A_E^i=1+\sum_{k\in E}|v_k^i|^2.
\]
Writing \(\Delta_i=f'(q+d_i)-f'(q)\), application of (4.5) to
\(\mathcal B_{f,E}\) gives
\[
\begin{aligned}
\frac{d^2}{dh^2}\mathbb E f(q_h)\Big|_{1/2}
=\mathbb E\Big[{}&f''(q)A_E+\sum_iR_{i,E}B_f(q,d_i)
 +A_E\sum_i r_iB_{f'}(q,d_i)\\
&+\sum_i r_i\Delta_i(A_E^i-A_E+1)\\
&+\sum_{i,j}r_j\{r_i^jB_f(q+d_j,d_i^j)-r_iB_f(q,d_i)\}\Big].
\end{aligned}
\tag{4.9}
\]
Use
\[
B_{f'}(q,d_i)=\Delta_i-f''(q)d_i,
\qquad
\sum_i r_id_i=1-A_E.
\]
The first, third, and fourth groups in (4.9) reduce exactly to
\[
f''(q)+\sum_i r_iB_{f'}(q,d_i)
+\sum_i r_i\{\Delta_iA_E^i-f''(q)d_iA_E\}.
\]
For \(f=\phi\), this is precisely the complete grouped S41 kernel
\[
\begin{aligned}
\mathscr K_{x,E}
={}&\phi''(q)+\sum_{i\in E}r_iB_{\phi'}(q,d_i)
 +\sum_{i\in E}R_{i,E}B_\phi(q,d_i)\\
&+\sum_{i\in E}r_i\Bigl(
 [\phi'(q+d_i)-\phi'(q)]A_E^i
 -\phi''(q)d_iA_E\Bigr)\\
&+\sum_{i,j\in E}r_j\Bigl(
 r_i^jB_\phi(q+d_j,d_i^j)-r_iB_\phi(q,d_i)\Bigr).
\end{aligned}
\tag{4.10}
\]
Thus the crucial interface is proved from the actual finite atom law:
\[
\boxed{G_E''(1/2)=\mathbb E\mathscr K_{x,E}.}
\tag{4.11}
\]

For a partition \(E=J\sqcup O\), use
\[
T_0=\sum_{o\in O}|P_{o0}|^2,
\qquad
T_i=\sum_{o\in O}|P_{oi}|^2,
\qquad
W_0=\sum_{i\in J}|P_{i0}|^2T_i,
\tag{4.12}
\]
\[
S_i=\sum_{j\in J}|P_{ij}|^2|P_{j0}|^2,
\qquad
Z_0=\sum_{i\in J}T_iS_i,
\qquad
\widetilde U_0=T_0+W_0+Z_0.
\tag{4.13}
\]
The imported finite S41 interfaces are
\[
|\mathscr K_{x,E}-\mathscr K_{x,J}|
\le C_{\rm tail}(x)(T_0+W_0),
\tag{4.14}
\]
\[
\left|\frac d{dt}\mathscr K_{x,J}(P_t)\right|
\le C_{\rm dir}(x)\kappa
\left(\sqrt{T_0}+\sqrt{W_0}+\frac12\sqrt{Z_0}\right),
\tag{4.15}
\]
for an outside diagonal tilt of speed \(\kappa=\|H\|\), and
\[
\widetilde U_0(P_t)\le e^{4\kappa t}\widetilde U_0(P_0).
\tag{4.16}
\]
The \(Z_0\) term is retained throughout.

---

## 5. Fixed-anchor mass transport for the repaired energy

Let \(P^\star\) be the hidden posterior projection after **all** channel
outputs, including the anchor, have been observed at \(h=1/2\).  Its law is
stationary.  Define
\[
T_a(L)=\sum_{|j-a|\ge L}|P^\star_{ja}|^2.
\]
The S44 number-variance interface gives
\[
\mathbb ET_0(L)\le A_Q(L).
\tag{5.1}
\]
Let \(I_R=\{-R,\ldots,R\}\), \(J_R=I_R\setminus\{0\}\), and
\(O_R=\mathbb Z\setminus I_R\).

### Lemma 5.1

\[
\boxed{
\mathbb E\widetilde U_0(P^\star;I_R)\le\upsilon(R).}
\tag{5.2}
\]

### Proof

The direct tail is
\[
\mathbb ET_0\le A_Q(R+1).
\]

For \(W_0\), every path \(0\to i\to o\), \(|o|>R\), has either
\(|i|\ge L_2(R)\) or \(|o-i|\ge L_2(R)\).  Hence
\[
W_0\le T_0(L_2)+\sum_i|P^\star_{i0}|^2T_i(L_2).
\tag{5.3}
\]
Stationarity and Tonelli give
\[
\begin{aligned}
\mathbb E\sum_i|P^\star_{i0}|^2T_i(L)
&=\mathbb E\left[T_0(L)\sum_i|P^\star_{0,-i}|^2\right]\\
&=\mathbb E[T_0(L)P^\star_{00}]
\le\mathbb ET_0(L).
\end{aligned}
\tag{5.4}
\]
Therefore \(\mathbb EW_0\le2A_Q(L_2)\).

For \(Z_0\), expand paths \(0\to j\to i\to o\):
\[
Z_0\le\sum_{|o|>R}\sum_{i,j}
|P^\star_{oi}|^2|P^\star_{ij}|^2|P^\star_{j0}|^2.
\tag{5.5}
\]
At least one of \(|j|,|i-j|,|o-i|\) is at least \(L_3(R)\).
The long first edge contributes at most \(T_0(L_3)\).  The long middle edge
contributes at most
\(\sum_j|P_{j0}|^2T_j(L_3)\), whose expectation is bounded by (5.4).
For the long last edge,
\[
\begin{aligned}
&\mathbb E\sum_{i,j}T_i(L)|P_{ij}|^2|P_{j0}|^2\\
&\quad=\mathbb E\left[
T_0(L)\sum_k|P_{0k}|^2\sum_m|P_{km}|^2\right]\\
&\quad=\mathbb E\left[T_0(L)\sum_k|P_{0k}|^2P_{kk}\right]
\le\mathbb ET_0(L).
\end{aligned}
\tag{5.6}
\]
Thus \(\mathbb EZ_0\le3A_Q(L_3)\), proving (5.2). ∎

Let \(P_R^-\) be the posterior after observing only \(Y_{J_R}\), with the
anchor and outside outputs unobserved.  Starting from \(P^\star\), erase the
outside observations and then the anchor observation.  The outside Gronwall
factor is \(s_x^4\), and the S41 anchor factor is another \(s_x^4\).  Hence
\[
\boxed{
\mathbb E\widetilde U_0(P_R^-;I_R)
\le s_x^8\upsilon(R).}
\tag{5.7}
\]
For the infinite outside erase, first use finite-support diagonal tilts and
pass to the bounded infinite likelihood operator by strong convergence,
Tonelli, and Fatou.  The same estimate controls every finite annulus
\(E\setminus J_R\), uniformly in \(E\supset J_R\).

---

## 6. Localization of the three normalized curvature terms

### 6.1 The complete \(G''\) term

Couple the exact words by first observing \(J_R\) and then revealing
\(E\setminus J_R\) through one simultaneous diagonal-likelihood path.  Its
operator-norm length is at most \(\log s_x\).  At the endpoint, (4.14) and
(4.16) give a tail contribution at most
\[
C_{\rm tail}(x)s_x^4\widetilde U_0(P_R^-).
\]
Along the path,
\[
\sqrt{T_0}+\sqrt{W_0}+\frac12\sqrt{Z_0}
\le\sqrt3\sqrt{\widetilde U_0},
\]
and (4.16) gives
\[
\int_0^1\kappa e^{2\kappa t}\,dt
=\frac{s_x^2-1}{2}.
\]
Using Jensen and (5.7),
\[
\boxed{
\begin{aligned}
|G_E''(1/2)-G_{J_R}''(1/2)|
\le{}&C_{\rm tail}(x)s_x^{12}\upsilon(R)\\
&+\frac{\sqrt3}{2}C_{\rm dir}(x)(s_x^2-1)s_x^4
\sqrt{\upsilon(R)}.
\end{aligned}}
\tag{6.1}
\]

### 6.2 The reference-law correction \(H'\)

By (4.6),
\[
H_J'(1/2)=\mathbb E\mathcal B_{\chi,J}.
\tag{6.2}
\]
On the legal posterior interval, with \(\Lambda=\Lambda_x\),
\[
\|\chi''\|_\infty\le4\Lambda^2,
\qquad
\|\chi'''\|_\infty\le20\Lambda^3,
\qquad
|d_i|\le\Lambda^3p_i^2,
\quad p_i=|P_{i0}|.
\tag{6.3}
\]
The Bregman remainder therefore gives
\[
|\mathcal B_{\chi,E}-\mathcal B_{\chi,J}|
\le2\Lambda^9T_0.
\tag{6.4}
\]

For a differentiable projection path, use the primitive bounds
\[
|\dot q|\le\delta_0,
\qquad
|\dot r_i|\le2\Lambda e_i,
\qquad
|\dot d_i|\le2\Lambda^3p_ih_i+2\Lambda^5p_i^2e_i,
\tag{6.5}
\]
where
\[
\delta_0=\|\dot Pe_0\|,
\qquad
\delta_1=\left(\sum_i p_i^2e_i^2\right)^{1/2},
\qquad
e_i=\|\dot Pe_i\|,
\qquad
h_i=|\dot P_{i0}|.
\]
Differentiating (4.4), using
\(|B_\chi|\le\|\chi''\|d^2/2\),
\(|B_{\chi'}|\le\|\chi'''\|d^2/2\),
\(|\chi'(q+d)-\chi'(q)|\le\|\chi''\||d|\), and
\(\sum p_i^2\le1/4\), gives the explicit bound
\[
\boxed{
\left|\frac d{dt}\mathcal B_{\chi,J}(P_t)\right|
\le5\Lambda^{11}(\delta_0+\delta_1).}
\tag{6.6}
\]
For an outside tilt of speed \(\kappa\),
\[
\delta_0\le\kappa\sqrt{T_0},
\qquad
\delta_1\le\kappa\sqrt{W_0}.
\]
Integrating (6.6) with (4.16), and then combining with (6.4) and (5.7), yields
\[
\boxed{
\begin{aligned}
|H_E'(1/2)-H_{J_R}'(1/2)|
\le{}&2\Lambda_x^9s_x^{12}\upsilon(R)\\
&+\frac{5\sqrt2}{2}\Lambda_x^{11}(s_x^2-1)s_x^4
\sqrt{\upsilon(R)}.
\end{aligned}}
\tag{6.7}
\]

### 6.3 The zeroth-order posterior term

At \(h=1/2\), posterior martingality gives
\[
q_{J_R}=\mathbb E(q_E\mid\sigma(Y_{J_R})).
\]
Since
\[
\phi''(q)=\frac1{2q^2(1-q)^2}
\le\frac8{(1-x^2)^2},
\]
conditional Taylor expansion gives
\[
0\le G_E(1/2)-G_{J_R}(1/2)
\le\frac4{(1-x^2)^2}\mathbb E(q_E-q_{J_R})^2.
\]
The martingale Pythagoras identity and the S44 scalar estimate imply
\[
\mathbb E(q_E-q_{J_R})^2
\le\mathbb E(q_\infty-q_{J_R})^2
\le\eta_x(R).
\]
Hence
\[
\boxed{
8|G_E(1/2)-G_{J_R}(1/2)|
\le\frac{32}{(1-x^2)^2}\eta_x(R).}
\tag{6.8}
\]

### Completion of Theorem 2.1

Subtract (3.8) for \(E\) and \(J_R\).  The constant \(8\) cancels.  Insert
(6.1), twice (6.7), and (6.8).  The resulting right side is exactly
\(B_x(R)\) in (2.6), proving (2.7).  Since the estimate is uniform over every
finite \(E\supset J_R\) and tends to zero with \(R\), the finite curvatures
form a Cauchy directed net, proving (2.8). ∎

---

## 7. Compact-\(x\) control

Fix \(0<c<1\).  Every coefficient in (2.6) is increasing in \(x\), so define
\[
\bar\eta_c(R)=
\frac{c^4\left(1+c^2/(1-c)^2\right)}{(1-c^2)^2}A_Q(R+1)
\]
and
\[
\begin{aligned}
\bar B_c(R)={}&s_c^{12}\bigl(C_{\rm tail}(c)+4\Lambda_c^9\bigr)\upsilon(R)\\
&+s_c^4(s_c^2-1)
 \left(\frac{\sqrt3}{2}C_{\rm dir}(c)
       +5\sqrt2\Lambda_c^{11}\right)\sqrt{\upsilon(R)}\\
&+\frac{32}{(1-c^2)^2}\bar\eta_c(R).
\end{aligned}
\tag{7.1}
\]
Then \(B_x(R)\le\bar B_c(R)\) for \(0\le x\le c\), and
\[
\boxed{
\int_0^1uB_{cu}(R)\,du
\le\frac12\bar B_c(R)\longrightarrow0.}
\tag{7.2}
\]
There is no unpaid \(u=0\) or \(u=1\) endpoint for fixed \(c<1\).

---

## 8. Relation to the S44 optimizer jet and to \(\Gamma\)

S44 supplies
\[
f_{*,\infty}=-\frac{4r_\infty}{1+\theta r_\infty},
\qquad
\dot f_{*,\infty}=\psi_{x,\theta}(r_\infty),
\qquad
\widehat J_R=\psi_{x,\theta}(r_R),
\]
and the exact nonnegative completion discrepancy
\[
\widehat J_R-\dot f_{*,R}
=\frac{16x^2}{1-x^2}
 \frac{\mathcal T_R^{\rm hid}}{(1+\theta r_R)^2}.
\]
This proof never identifies \(\widehat J_R\) with \(\dot f_{*,R}\).
Identity (1.1) explains why the S44 first-jet estimate alone was insufficient:
the moving metric and second normalized load create a signed forcing.  The
forcing is paid here through the exact normalization identity, the complete
finite channel kernel, and the fixed-anchor \(T+W+Z\) estimate.

If a source-specific local quantity is algebraically proved to satisfy
\[
\Gamma(c)=\int_0^1u\,\mathcal F_{cu,\infty}''(1/2)\,du,
\qquad
\Gamma_R^{\rm obs}(c)=\int_0^1u\,\mathcal F_{cu,J_R}''(1/2)\,du,
\]
with the present \(1/4\) normalization and with no omitted prefactor or
reference-law term, then (7.2) gives
\[
|\Gamma(c)-\Gamma_R^{\rm obs}(c)|
\le\frac12\bar B_c(R).
\]
That source-specific identification is not assumed here.  In particular, a
formula using only the frozen \(G''\) kernel must also include
\[
2H'(1/2)+8+8G(1/2)
\]
with its exact signs and prefactors.  S51's noise-flow identification with the
Shannon entropy rate remains outside S53.

---

## 9. Scope ledger

### Proved here

1. The complete finite second derivative of the moving conditional-expectation
   projection error, equations (1.1)--(1.3).
2. A rigorous obstruction showing that base and first optimizer jet alone do
   not determine curvature in a general moving Galerkin problem.
3. The exact Jeffreys/normalization identity (3.3)--(3.8).
4. The actual finite-law derivative operator and the interface
   \(G_E''=\mathbb E\mathscr K_{x,E}\), without assuming S41's final frozen
   identification.
5. A new fixed-anchor mass-transport bound for \(T_0+W_0+Z_0\).
6. The explicit uniform finite-observation bound (2.7), the finite-curvature
   limit, and compact-\(x\) endpoint integrability.

### Not proved here

- positivity of any \(\Gamma(c)\);
- off-midpoint or off-half-filling curvature;
- all-\(\rho\), all-\(a\) Shannon entropy-rate concavity;
- differentiability of the limiting Shannon entropy rate;
- identification of \(\operatorname{Tr}b(K)\) with classical configuration
  entropy.

No finite Toeplitz compression is treated as a projection.  Projection
geometry is used only for the latent posterior of the infinite hidden
projection DPP and its bounded diagonal-likelihood orbit.
