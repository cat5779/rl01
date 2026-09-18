# S14 visible conversation harvest — 2026-09-18

Status: AUTHOR_SUBMISSION_PENDING_INDEPENDENT_REVIEW.
This captures visible response text, not the downloadable attachment bodies. Attachment-card references and source citations are retained as provenance; they are not accessible proof files or independent certification. The newest available substantive response is first.

# SA05 follow-up delivered

## Status

- **Previous independent audit:** `INCOMPLETE_REVIEW` — unchanged.
- **§§5.3–5.4 circularity repair:** **PROVED in this follow-up**, pending later independent review.
- **Exact midpoint count-transport tool:** **PROVED in this follow-up**, pending later independent review.
- **Deletion-chain/modulated-entropy identity:** **PROVED in this follow-up**, pending later independent review.
- **Unconditional target**
  \[
  \mathcal L_n''(a_*)+\sum_l\pi_l''(a_*)R_l(a_*)\ge-o(n):
  \]
  **INCOMPLETE**.
- **Actual SA05 asymptotic counterexample:** **NOT FOUND / NOT CLAIMED**.
- **Claim that symmetry, nonnegativity, and layerwise \(O(1)\) alone control the moving-count Hessian:** **DISPROVED** by a rigorous diffusive-scale profile obstruction.

The original proof itself identifies the same unpaid target and warns that the layerwise \(O(1)\) source payment does not settle the moving-weight and linear-response terms. citeturn226639view0

---

# 1. Non-circular repair of §§5.3–5.4

The source first presents the already centered formula in its equation (5.7), but only later obtains the moment identity by taking its expectation. That ordering is circular because the vanishing constant in (5.7) already uses the moment identity. citeturn494358view0

For \(l=m\le k\), let
\[
J=|S\cap A|,\qquad
z=\frac{1+\xi}{\xi},\qquad
A(\xi)=\xi(1+\xi),
\]
and let
\[
b_j=\frac{(m-j)(k-j)}{C_l},\qquad
d_j=\frac{j(k-m+j)}{C_l},\qquad C_l=m(n-m).
\]

Because \(t_A(j+1)/t_A(j)=z\) and \(t_A(j-1)/t_A(j)=z^{-1}\), the correct starting point is the **uncentered** identity
\[
\boxed{
\frac{L_lt_A}{t_A}
=
\frac{J^2-(m+k+n\xi)J+(1+\xi)mk}
     {A(\xi)C_l}.}
\]

No moment relation enters this calculation.

Conservativity of the Johnson generator gives
\[
0=\left\langle 1,L_lt_A\right\rangle_{u_l}
 =\mathbb E_w\!\left[\frac{L_lt_A}{t_A}\right].
\]
Writing
\[
\mu=\mathbb E_wJ,\qquad
v=\operatorname{Var}_w(J),\qquad
y=m-\mu,
\]
one obtains independently
\[
\mu^2+v-(m+k+n\xi)\mu+(1+\xi)mk=0,
\]
or equivalently
\[
\boxed{
y^2+(k-m+n\xi)y+v=mk\xi.}
\]

Only now may one substitute \(J=\mu+X\), \(X=J-\mu\). The constant term is then \(-v\), yielding
\[
\boxed{
\frac{L_lt_A}{t_A}
=
\frac{X^2-v+\beta X}{A(\xi)C_l},
\qquad
\beta=2\mu-m-k-n\xi.}
\]

The normalization and parameter derivatives also close directly:
\[
(\log z)_\xi=-\frac1{A(\xi)},\qquad
\mu_\xi=-\frac v{A(\xi)},
\]
hence
\[
\boxed{\frac{\partial_\xi t_A}{t_A}=-\frac X{A(\xi)}}
\]
and
\[
\boxed{
\frac{\partial_{\xi\xi}t_A}{t_A}
=
\frac{X^2-v+(1+2\xi)X}{A(\xi)^2}.}
\]

Both expressions have zero expectation, as normalization requires.

At
\[
a_*=\frac1{40},\qquad \xi_*=\frac1{1520},
\qquad \xi_a(a_*)=0,\qquad \xi_{aa}(a_*)=-\frac2c,
\]
this gives
\[
(t_A)_a=0,\qquad
\frac{(t_A)_{aa}}{t_A}
=\frac{2X}{cA(\xi_*)},
\]
and, for the corrected heat clock,
\[
\tau_a(a_*)=0,\qquad
\tau_{aa}(a_*)=-\frac2c\tau_\xi(\xi_*).
\]

The degree-two orthogonality leading to the original equation (5.9) is then legitimate. With
\[
W=X^2-v+\mathfrak bX,
\]
and
\[
h_2(J)=X^2+(2\mu-m)X+\text{constant},
\]
the relation \(\mathbb E_w[Wh_2]=0\) gives
\[
\boxed{
\mathfrak b=
-\frac{\mu_4-v^2+(2\mu-m)\mu_3}
       {\mu_3+(2\mu-m)v}.}
\]

Thus the valid logical order is
\[
\boxed{
\text{uncentered generator}
\Longrightarrow
\text{moment identity}
\Longrightarrow
\text{centered generator}
\Longrightarrow
\text{degree-two cancellation}.}
\]

---

# 2. Exact midpoint count-Hessian factorization

Put
\[
s=a-a_*.
\]
Pair one Bernoulli from each of the two channel groups. Its count probability-generating function is exactly
\[
p_s(t)
=p_0(t)+s(t^2-1)+s^2(1-t)^2,
\]
where
\[
p_0(t)=\rho(1+t^2)+bt,\qquad
\rho=\frac{1-c^2}{4},\qquad
b=\frac{1+c^2}{2}.
\]

Since the full count PGF is \(\Pi_s(t)=p_s(t)^k\),
\[
\boxed{
\Pi_0''(t)=(1-t)^2B_n(t)}
\]
with
\[
\boxed{
B_n(t)=
2kp_0(t)^{k-1}
+k(k-1)(1+t)^2p_0(t)^{k-2}.}
\]

Writing
\[
B_n(t)=\sum_{r=0}^{n-2}B_{n,r}t^r,
\]
coefficient extraction yields, for every real sequence \(h_0,\dots,h_n\),
\[
\boxed{
\sum_{l=0}^n\pi_l''(a_*)h_l
=
\sum_{r=0}^{n-2}B_{n,r}\Delta^2h_r,}
\qquad
\Delta^2h_r=h_r-2h_{r+1}+h_{r+2}.
\]

The polynomial \(B_n\) is palindromic and real-rooted with positive coefficients. Its lower-half coefficients are consequently increasing. Define
\[
\omega_{n,0}=B_{n,0},\qquad
\omega_{n,m}=B_{n,m}-B_{n,m-1}\ge0.
\]

For every complement-symmetric layer sequence \(h_{n-l}=h_l\),
\[
\boxed{
\sum_l\pi_l''(a_*)h_l
=
-2\sum_{m=0}^{k-1}
\omega_{n,m}\bigl(h_{m+1}-h_m\bigr).}
\]

This is the new weighted-transport correction: the moving count Hessian is not an arbitrary signed sum but a positive-weight transport of adjacent layer increments.

The kernel has the quantitative bounds
\[
\sum_{m=0}^{k-1}\omega_{n,m}=B_{n,k-1}=O_c(n^{3/2})
\]
and
\[
\sum_{m=0}^{k-w-1}\omega_{n,m}
=B_{n,k-w-1}
\le n(n-1)e^{-w^2/(n-2)}.
\]

Thus only a diffusive neighborhood of the middle layer contributes materially, and every tail passage used in the report has an explicit exponentially small bound.

---

# 3. Exact representation of the unpaid midpoint combination

Define
\[
\lambda_l=
\langle f_l-g_l,\log g_l\rangle_{u_l},
\qquad
\epsilon_l=\lambda_l+R_l.
\]
Then
\[
\epsilon_l
=D(q_l\Vert u_l)-D(\widehat q_l\Vert u_l).
\]

For
\[
U_n:=
\mathcal L_n''(a_*)
+\sum_l\pi_l''(a_*)R_l(a_*),
\]
the midpoint chain rule gives the exact identity
\[
\boxed{
U_n=
\sum_l\pi_l''(a_*)\epsilon_l(\xi_*)
-\frac2c\sum_l\pi_l(a_*)\lambda_{l,\xi}(\xi_*).}
\]

Applying the positive transport formula,
\[
\boxed{
U_n=
-2\sum_{m=0}^{k-1}\omega_{n,m}
   (\epsilon_{m+1}-\epsilon_m)
-\frac2c\sum_l\pi_l\lambda_{l,\xi}.}
\]

For \(m\ge3\), inserting CL12 gives
\[
R_{m+1}-R_m
=
\mathcal C_m+\eta_mR_{m,\xi}+\mathcal J_m,
\]
where \(\mathcal C_m\) is the reverse conditional deletion KL and
\[
\mathcal J_m
=
\int_0^1(1-t)
\left[
\mathcal Q^{[t]}
-(b'(t))^2
\left\langle
\delta^{[t]},\frac{Z^{[t]}}{g^{[t]}}
\right\rangle
\right]dt.
\]
The source explicitly warns that neither \(\Delta^2R_m\) nor this nonlinear remainder has a predetermined favorable sign. citeturn438514view2turn438514view3

Consequently,
\[
\boxed{
\begin{aligned}
U_n={}&
-2\sum_{m=3}^{k-1}\omega_{n,m}
\bigl[
\lambda_{m+1}-\lambda_m
+\mathcal C_m
+\eta_mR_{m,\xi}
+\mathcal J_m
\bigr]\\
&-\frac2c\sum_l\pi_l\lambda_{l,\xi}.
\end{aligned}}
\]

This formula retains:

- the actual moving layer weights;
- the reverse conditional KL with its adverse sign;
- the physical parameter response;
- the positive interpolation square;
- the moving-reference residual pairing;
- the cross-layer linear entropy increment; and
- the separate averaged \(\xi\)-response.

No static KL or \(\chi^2\) estimate is differentiated.

---

# 4. One previously unpaid term is now \(O(\sqrt n)\)

The already audited graph-energy estimate gives
\[
R_{m,\xi}
\le\frac{J_m^2}{4\tau_{m,\xi}}
\le K_R
\]
uniformly at the midpoint, while
\[
\eta_m\le\frac{2(1+\xi_*)}{n}.
\]
Therefore
\[
\boxed{
\eta_mR_{m,\xi}\le\frac{K_0}{n}}
\]
for an explicit \(n\)-independent constant
\[
K_0=z_*(1+\xi_*)^2K_W.
\]

Since the total flux mass is \(O(n^{3/2})\),
\[
2\sum_m\omega_{n,m}\eta_mR_{m,\xi}
=O(\sqrt n).
\]

Set
\[
\Gamma_m=
\lambda_{m+1}-\lambda_m+\mathcal C_m+\mathcal J_m.
\]
The resulting sharp lower bound is
\[
\boxed{
\begin{aligned}
U_n\ge{}&
-2\left(\sum_{m=3}^{k-1}\omega_{n,m}\Gamma_m\right)_+\\
&-\frac2c
 \left(\sum_l\pi_l\lambda_{l,\xi}\right)_+
-O_c(\sqrt n).
\end{aligned}}
\]

Define the two remaining signed aggregate budgets
\[
\mathfrak A_n=
\left(
\sum_{m=3}^{k-1}\omega_{n,m}
[\lambda_{m+1}-\lambda_m+\mathcal C_m+\mathcal J_m]
\right)_+,
\]
\[
\mathfrak B_n=
\left(\sum_l\pi_l\lambda_{l,\xi}\right)_+.
\]

Combining with the old midpoint bridge gives
\[
\boxed{
E_n''(a_*)
\ge
-2\mathfrak A_n
-\frac2c\mathfrak B_n
-O_c(\sqrt n)
-C_{\rm src}.}
\]

Hence
\[
\mathfrak A_n=o(n),
\qquad
\mathfrak B_n=o(n)
\]
would prove the desired comparison.

These two estimates are **not proved**. They are now exposed as signed first-order budgets rather than a hidden second-derivative lemma. The local sufficient conditions below are stronger but independently checkable.

---

# 5. New deletion-chain modulated-entropy identity

Let
\[
p=q_{m+1},\quad \widehat p=\widehat q_{m+1},
\quad P=\mathsf K_mp,\quad \widehat P=\mathsf K_m\widehat p.
\]

KL chain rule for the retained \(m\)-set and the deleted point gives
\[
\epsilon_{m+1}
=
\epsilon_m^\downarrow+\mathcal H_m^{\rm del},
\]
where
\[
\mathcal H_m^{\rm del}
=
\mathbb E_P D(\alpha_p\Vert u^S)
-
\mathbb E_{\widehat P}D(\alpha_{\widehat p}\Vert u^S).
\]

This signed deletion-information defect expands exactly as
\[
\begin{aligned}
\mathcal H_m^{\rm del}
={}&\mathcal C_m\\
&+\mathbb E_P\sum_x
(\alpha_p-\alpha_{\widehat p})
\log\frac{\alpha_{\widehat p}}{u^S}\\
&+\sum_S(P-\widehat P)(S)
D(\alpha_{\widehat p}(\cdot\mid S)\Vert u^S).
\end{aligned}
\]

Thus the reverse conditional KL is retained, together with the two signed linear terms that can potentially cancel it.

For the actual CL12 interpolation, define
\[
\Phi_m(t)
=
D(u_mf^{[t]}\Vert u_m)
-
D(u_mg^{[t]}\Vert u_m).
\]
Then
\[
\Phi_m(0)=\epsilon_m,\qquad
\Phi_m(1)=\epsilon_m^\downarrow,\qquad
\Phi_m'(0)=\eta_m\epsilon_{m,\xi},
\]
and
\[
\Phi_m''(t)
=
\left\langle\frac{\dot f^{[t]\,2}}{f^{[t]}}\right\rangle
-
\left\langle\frac{\dot g^{[t]\,2}}{g^{[t]}}\right\rangle
-
\langle\ddot g^{[t]},\log g^{[t]}\rangle.
\]

Therefore
\[
\boxed{
\epsilon_{m+1}-\epsilon_m
=
\mathcal H_m^{\rm del}
+\eta_m\epsilon_{m,\xi}
+\int_0^1(1-t)\Phi_m''(t)\,dt.}
\]

Subtracting CL12 produces
\[
\boxed{
\lambda_{m+1}-\lambda_m
+\mathcal C_m+\mathcal J_m
=
\mathcal H_m^{\rm del}
+\eta_m\lambda_{m,\xi}
+\int_0^1(1-t)\Phi_m''(t)\,dt.}
\]

This is the transferable modulated-relative-entropy mechanism requested in the assignment. It gives a precise target for future estimates without assigning an unjustified sign.

---

# 6. Proved conditional routes to \(-o(n)\)

Two routes are established.

### Central one-step route

For
\[
|m-k|\le n^{2/3},
\]
if
\[
(\epsilon_{m+1}-\epsilon_m)_+
\le \frac{A_n}{n},
\qquad A_n=O(1),
\]
and
\[
\left(\sum_l\pi_l\lambda_{l,\xi}\right)_+=o(n),
\]
then
\[
U_n\ge-o(n).
\]

The noncentral contribution is
\[
O\!\left(n^3e^{-n^{1/3}+o(1)}\right),
\]
so no tail is left implicit.

A sufficient expanded version is
\[
\bigl(
\lambda_{m+1}-\lambda_m+\mathcal C_m+\mathcal J_m
\bigr)_+
\le \frac{A}{n},
\]
because the remaining \(\eta_mR_{m,\xi}\) costs only \(K_0/n\).

### Macroscopic-profile route

If a symmetric \(H\in C^2([0,1])\) satisfies
\[
\max_{|l-k|\le n^{2/3}}
|\epsilon_l-H(l/n)|\longrightarrow0,
\]
then
\[
\sum_l\pi_l''\epsilon_l=o(n).
\]

Together with
\[
\left(\sum_l\pi_l\lambda_{l,\xi}\right)_+=o(n),
\]
this also proves \(U_n\ge-o(n)\).

The static profile is never differentiated; the response remains a separate hypothesis.

---

# 7. Diffusive obstruction and exact diagnostic

Let
\[
\sigma_n^2=\frac{n(1-c^2)}4.
\]

For every even \(H\in C_b^2(\mathbb R)\) with uniformly continuous \(H''\),
\[
h_{n,l}=H\!\left(\frac{l-k}{\sigma_n}\right)
\]
satisfies
\[
\boxed{
\frac1n\sum_l\pi_l''h_{n,l}
\longrightarrow
\frac4{1-c^2}\mathbb E[H''(Z)]
=
\frac4{1-c^2}\mathbb E[(Z^2-1)H(Z)].}
\]

Taking
\[
H(x)=e^{-x^2/2}
\]
gives
\[
\boxed{
\sum_l\pi_l''
\exp\!\left[-\frac{(l-k)^2}{2\sigma_n^2}\right]
=
-\frac{\sqrt2}{1-c^2}n+o(n).}
\]

The profile is symmetric, nonnegative, and bounded by one. It may also be made exactly zero on all layers \(m\le3\) and their complements without changing the limit.

Therefore
\[
\text{symmetry}+\text{nonnegativity}+O(1)
\]
does **not** imply
\[
\sum_l\pi_l''h_l=o(n).
\]

This is not asserted to be an actual SA05 KL profile.

The report also proves an exact actual-profile diagnostic. Put
\[
G_n(r)=\sigma_n^2\Delta^2\epsilon_{n,r}.
\]
If \(G_n\) is uniformly bounded and converges locally on the diffusive scale to a bounded continuous \(G\), and if
\[
\frac1n\sum_l\pi_l\lambda_{n,l,\xi}\longrightarrow\beta,
\]
then
\[
\boxed{
\frac{U_n}{n}
\longrightarrow
\frac4{1-c^2}\mathbb E[G(Z)]
-\frac{2\beta}{c}.}
\]

Under those exact hypotheses, a strictly negative right-hand side would be a valid asymptotic obstruction to the hoped-for lower bound. No such limiting profile or response value has been established for the actual Fourier-DPP sequence.

---

# 8. \(n=8\) certificate and scope

The new transport formula reproduces the existing center-layer obstruction exactly:
\[
\omega_{8,3}
=B_{8,3}-B_{8,2}
=c^3Q_4'(\xi_*)
=\frac{1766316767}{102400000}>0,
\]
and hence
\[
\sum_l\pi_l''R_l
=-2\omega_{8,3}R_4
=-2c^3Q_4'(\xi_*)R_4<0.
\]
This agrees with CL14–CL15 and retains the unfavorable reverse conditional KL rather than deleting it. citeturn438514view3

Source-level inspection of the supplied rational interval certificate confirms the certified intervals
\[
E_8''(1/200)
\in[-0.00037268948828,-0.00037268948827],
\]
\[
E_8''(1/50)
\in[0.00034554219606,0.00034554219607],
\]
\[
E_8''(1/40)
\in[0.00044081523988,0.00044081523989].
\]
The certificate uses rational interval propagation; the separate 256-atom binary64 calculation is explicitly only a regression cross-check. These are three finite \(n=8\) signs, not an asymptotic midpoint theorem. citeturn494358view5

I inspected but did not re-execute the interval script. No conclusion in the report depends on extending its finite scope.

---

# Deliverables

:chatgpt-content-reference{index="6"}

:chatgpt-content-reference{index="7"}

:chatgpt-content-reference{index="8"}

:chatgpt-content-reference{index="9"}

---

# SA05 独立审计已交付

**总评：`INCOMPLETE_REVIEW`。**

指定重点中的 Jacobi–Duhamel 方程、移动参考相对熵二阶恒等式、强对数凹谱隙的生成元归一，以及跨层 CL1–CL12，均未发现致命代数错误。但这些结果只控制了部分二阶账本；目标级结论仍缺少
\[
\mathcal L_n''(a_*)+\sum_l\pi_l''(a_*)R_l(a_*)\ge-o(n),
\]
所以层内统一 \(O(1)\) 源预算不能解释成完整 \(E_n''(a_*)=O(1)\)。作者正文也明确承认这一目标及中点全 \(n\) 符号尚未证明。citeturn865312view1turn865312view2turn509251view2

审计确认静态 KL/\(\chi^2\) 界没有被直接微分，跨层二阶式 CL3 保留了移动系数导数；同时，合法 \(n=8\) 中心层例子给出
\[
R_4=\mathcal C_3>0,\qquad
\Delta^2R_3=-2R_4<0,\qquad
\sum_l\pi_l''(a_*)R_l(a_*)<0,
\]
因此反向条件 KL 和移动计数项不能无条件删除或视为有利项。citeturn709002view1turn709002view2turn709002view3

本次另发现一处可修复的新证明文本缺口：`SA05_PROOF.md` §5.3–§5.4 先写出已经中心化的 \(L_lt_A/t_A\)，随后再借其期望推导用于中心化的矩恒等式，当前书写构成循环；报告中给出了应先保留的未中心化公式。citeturn603945view0turn603945view1

报告未读取其他 SA、S13 附件、`SA05_AUDIT.md` 或 `WORK_RECORD.md`；代码和 JSON 仅阅读、未复跑，符合入口规定的独立范围。citeturn938797view0

:chatgpt-content-reference{index="5"}
