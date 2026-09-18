# S42 harvested response

Status: AUTHOR_SUBMISSION_PENDING_INDEPENDENT_REVIEW. PARTIAL_TEXT: the read tool returned only the first 20,000 characters. The ending is missing; do not claim the complete proof was recovered.
Source task: 6aabf6da-7884-83e8-9433-e9b61e7d474a
Citation markers are preserved as provenance, not independent supporting evidence.

---

# S42 result — a local response-energy correction with an actual-law average-tail bound

## Status

**PROVED:** an explicit nested family of finite-dimensional corrections \(k_{m,\alpha}\), with an exact dimension-free \(L^2\) loss formula. All \(\alpha\)-dependent mixture weights are integrated exactly.

**PROVED:** for the actual noisy sine process, the discarded response tail is controlled by the latent posterior number variance. This replaces the worst-word optimizer approximation by an actual-law bound of order  
\[
O\!\left(\frac{\log m}{m}\right).
\]

**CONDITIONAL ON THE FROZEN, UNREVIEWED VOLUME IDENTIFICATION:** the resulting integrated inequality for \(\Gamma(c)\). The frozen file identifies the infinite curvature integral with \(\Gamma(c)\), but explicitly remains pending independent review. citeturn456176view0turn113648view3

**INCOMPLETE:** I do not obtain an interval-certified positive value of \(\underline\Gamma_m(19/20)\). Therefore this is not yet a proof that \(\Gamma(19/20)>0\).

The new mechanism is nevertheless quantitatively useful: at \(c=19/20\), its rigorous optimizer-loss formula is below \(0.58\) at radius \(m=1023\), below \(0.089\) at \(m=8191\), and decays explicitly thereafter. It does not use the old \(a^{16}\) or \(a^{18}\) worst-word constants.

---

## 1. The correction

Fix the channel correlation \(x\in[0,c]\), with \(h_0=1/2\). For a finite external word \(z\), write
\[
B_z=K_C-\operatorname{diag}(1-z),\qquad
G_z=B_z^{-1},
\]
\[
v_z=G_zb,\qquad
r_z=b^*G_zb=\frac12-q_z .
\]

For an integer \(m\ge0\), let
\[
s_m(z)=\sum_{\substack{j\in C\\0<|j|\le m}} |v_{z,j}|^2,
\qquad
\tau_m(z)=\sum_{\substack{j\in C\\|j|>m}} |v_{z,j}|^2.
\]
Thus
\[
\|v_z\|^2=s_m(z)+\tau_m(z).
\]

Set
\[
\theta=2-4\alpha,\qquad -2\le\theta\le2.
\]

The proposed correction is
\[
\boxed{
k_{m,\alpha}(z)
=
\frac{4\bigl(s_m(z)+4r_z^2\bigr)}
     {(1+\theta r_z)^2}.}
\tag{1.1}
\]

This is not the exact optimizer unless the tail \(\tau_m\) vanishes. For \(m=0\),
\[
k_{0,\alpha}(z)=\frac{16r_z^2}{(1+\theta r_z)^2},
\]
so it is emphatically not the already-refuted zero correction.

The candidate uses only:

1. the scalar posterior offset \(r_z=1/2-q_z\);
2. the local single-site response energies \(|v_{z,j}|^2\) for \(0<|j|\le m\).

Using the one-flip Schur identity,
\[
q(z^j)-q(z)=\frac{\sigma_j(z)|v_{z,j}|^2}{o_j(z)},
\]
the local energy can equivalently be obtained from posterior flip responses:
\[
s_m(z)
=
\sum_{0<|j|\le m}
\sigma_j(z)o_j(z)\,[q(z^j)-q(z)].
\tag{1.2}
\]
Thus no \(G^2\), \(G^3\), \(\operatorname{tr}G\), global score, or connected double-flip term is needed to specify \(k_m\).

The source mechanism is a Galerkin/Rayleigh–Ritz truncation: retain the scalar rank-one mode \(r\) exactly and project the response vector \(v\) onto the physical coordinates \(|j|\le m\). The a posteriori error estimator is the omitted energy \(\tau_m\).

---

## 2. Exact finite theorem

The submission’s touching dual has the exact gap
\[
F''(1/2)-\underline F''[k]
=
\frac12\int_0^1
\mathbb E_{p_{1/2,\alpha}}
\bigl[(k_\alpha-\dot f_{*,\alpha})^2\bigr]\,d\alpha,
\]
and
\[
\dot f_{*,\alpha}
=
4b^*R_{\theta,z}(I+4bb^*)R_{\theta,z}b,
\qquad
R_{\theta,z}=(B_z+\theta bb^*)^{-1}.
\]
The mixture law is
\[
p_\theta(z)=w(z)(1+\theta r_z).
\]
These are the only identities from the new submission needed below; I rederive the specialization rather than relying on its status labels. citeturn105691view1turn507878view0

### Theorem 2.1 — exact local-energy loss

For every finite legal model and every \(m\ge0\),
\[
\boxed{
\dot f_{*,\alpha}(z)-k_{m,\alpha}(z)
=
\frac{4\tau_m(z)}{(1+\theta r_z)^2}.}
\tag{2.1}
\]

Consequently,
\[
\boxed{
F_x''(1/2)-\underline F_{x,m}''
=
8\,\mathbb E_w
\frac{\tau_m^2}{(1-4r^2)^2}.}
\tag{2.2}
\]

In particular:

- \(\underline F_{x,m}''\le F_x''(1/2)\);
- the certificate is monotone in \(m\):
  \[
  \underline F_{x,m+1}''\ge \underline F_{x,m}'';
  \]
- if \(m\) contains every external coordinate, then the certificate is exact;
- the loss contains no factor depending on the ambient dimension.

#### Proof

Sherman–Morrison gives
\[
R_{\theta,z}b
=
\left(G_z-\frac{\theta G_zbb^*G_z}{1+\theta r_z}\right)b
=
\frac{v_z}{1+\theta r_z}.
\]
Similarly,
\[
b^*R_{\theta,z}b
=
\frac{r_z}{1+\theta r_z}.
\]
Therefore
\[
\begin{aligned}
\dot f_{*,\alpha}
&=
4b^*R_{\theta,z}^2b
+16(b^*R_{\theta,z}b)^2\\
&=
\frac{4\bigl(\|v_z\|^2+4r_z^2\bigr)}
     {(1+\theta r_z)^2}.
\end{aligned}
\tag{2.3}
\]
Subtracting (1.1) proves (2.1).

Now insert (2.1) in the touching-dual gap. Since
\[
p_\theta(z)=w(z)(1+\theta r_z),
\]
\[
\begin{aligned}
F_x''-\underline F_{x,m}''
&=
\frac12\int_0^1
\sum_z w(z)(1+\theta r_z)
\frac{16\tau_m(z)^2}{(1+\theta r_z)^4}\,d\alpha\\
&=
8\mathbb E_w\left[
\tau_m^2\int_0^1(1+\theta r)^{-3}\,d\alpha
\right].
\end{aligned}
\]
Because \(\theta=2-4\alpha\),
\[
\begin{aligned}
\int_0^1(1+\theta r)^{-3}\,d\alpha
&=
\frac14\int_{-2}^{2}(1+\theta r)^{-3}\,d\theta\\
&=
\frac1{(1-4r^2)^2}.
\end{aligned}
\]
This proves (2.2). Every moving mixture weight has been retained; none was replaced by its worst-case lower bound. ∎

### Uniformity

For the channel with correlation \(x<1\),
\[
q_z\in\left[\frac{1-x}{2},\frac{1+x}{2}\right],
\qquad |r_z|\le\frac x2.
\]
Hence, uniformly in every word and every \(\alpha\),
\[
1+\theta r_z\ge1-x\ge1-c,
\tag{2.4}
\]
and
\[
1-4r_z^2\ge1-x^2\ge1-c^2.
\tag{2.5}
\]
Thus (1.1) and (2.2) are uniformly legal on the full \(u\)-range \(x=cu\), including the endpoint \(u=0\) by continuity.

The quantities \(r\), \(|v_j|^2\), \(s_m\), and \(\tau_m\) are all dimensionless response energies. No norm is being added to a probability derivative with a different scaling.

---

## 3. Posterior projections under the actual noisy sine law

Let \(Q\) be the latent half-filled sine projection, and let latent spins be
\[
\xi_i=2X_i-1.
\]
Pass them through the binary symmetric channel
\[
\mathbb P(Y_i=y\mid \xi_i=\xi)
=\frac{1+xy\xi}{2}.
\]
The output DPP kernel is
\[
K_x=\frac{1-x}{2}I+xQ
=\frac12I+x\left(Q-\frac12I\right).
\tag{3.1}
\]
This projection-channel representation is also recorded in the submission. citeturn113648view1

### Lemma 3.1 — the latent posterior is again a projection DPP

Given any collection of output observations, define the diagonal likelihood tilt
\[
D_{ii}^2=
\frac{1+xy_i}{1-xy_i}
\]
at observed sites, and \(D_{ii}=1\) at unobserved sites. Then the posterior latent kernel is
\[
\boxed{
\Pi_D
=
DQ\,
\bigl(QD^2Q\vert_{\operatorname{Ran}Q}\bigr)^{-1}
QD.}
\tag{3.2}
\]
It is the orthogonal projection onto \(D\operatorname{Ran}Q\).

#### Finite proof

Write \(Q=UU^*\), where \(U\) is an isometry onto the fixed-rank latent subspace. A projection DPP assigns a configuration \(X\) weight
\[
|\det U_X|^2.
\]
Multiplication by the observation likelihood contributes
\[
\prod_{i\in X}D_{ii}^2=|\det D_X|^2.
\]
Thus the posterior is the volume-sampling law generated by \(DU\), whose normalized kernel is
\[
DU(U^*D^2U)^{-1}U^*D.
\]
This is exactly (3.2).

#### Infinite exhaustion

For \(x\le c<1\),
\[
\sqrt{\frac{1-c}{1+c}}
\le D_{ii}\le
\sqrt{\frac{1+c}{1-c}}.
\tag{3.3}
\]
Let \(D_n\) retain the tilt only on a finite window. Then \(D_n\to D\) strongly, while
\[
QD_n^2Q\vert_{\operatorname{Ran}Q}
\]
is uniformly coercive. Hence its inverse converges strongly, and so do the projections \(\Pi_{D_n}\). Finite-cylinder posterior probabilities converge by the conditional-expectation martingale theorem, identifying the limit with the actual posterior given all observations.

This also proves the required parameter uniformity: no singular posterior tilt appears anywhere for \(x\le c<1\).

---

## 4. Exact conversion of the resolvent tail into a posterior projection tail

Let

- \(\Pi^-\) denote the latent posterior projection given every output except \(Y_0\);
- \(p=\Pi^-_{00}\);
- \(\Pi^+\) denote the posterior after also observing \(Y_0\).

Because
\[
q=\mathbb P(Y_0=1\mid Y_{\ne0})
=\frac12+x\left(p-\frac12\right),
\]
we have
\[
r=-x\left(p-\frac12\right).
\tag{4.1}
\]

Define
\[
T_m^-=\sum_{|j|>m}|\Pi^-_{0j}|^2,
\qquad
T_m^+=\sum_{|j|>m}|\Pi^+_{0j}|^2.
\tag{4.2}
\]

### Lemma 4.1 — exact influence identity

For every external site \(j\),
\[
\boxed{
|v_j|^2
=
\frac{4x^2}{1-x^2}\,|\Pi^-_{0j}|^2.}
\tag{4.3}
\]
Therefore
\[
\boxed{
\tau_m
=
\frac{4x^2}{1-x^2}\,T_m^-.}
\tag{4.4}
\]

#### Proof

Condition first on every output except sites \(0,j\). Let \(\widehat\Pi\) be the resulting latent posterior projection, and put
\[
\mu_j=\mathbb E[\xi_j\mid\cdot],
\qquad
C_{0j}=\operatorname{Cov}(\xi_0,\xi_j\mid\cdot)
=-4|\widehat\Pi_{0j}|^2.
\]
After observing \(Y_j=y\),
\[
\mathbb E[\xi_0\mid Y_j=y,\cdot]
=
\mathbb E[\xi_0\mid\cdot]
+\frac{xyC_{0j}}{1+xy\mu_j}.
\tag{4.5}
\]
It follows that flipping \(y\) changes the output-center posterior by
\[
q_{-y}-q_y
=
-\frac{x^2yC_{0j}}{1-x^2\mu_j^2}.
\tag{4.6}
\]

The conditional output odds ratio is
\[
o_j=\frac{1-xy\mu_j}{1+xy\mu_j}.
\]
The output-DPP Sherman–Morrison identity gives
\[
q_{-y}-q_y=\frac{y|v_j|^2}{o_j}.
\tag{4.7}
\]
Equating (4.6) and (4.7),
\[
|v_j|^2
=
\frac{4x^2|\widehat\Pi_{0j}|^2}
     {(1+xy\mu_j)^2}.
\tag{4.8}
\]

A direct two-spin Bayes calculation also gives
\[
\operatorname{Cov}(\xi_0,\xi_j\mid Y_j=y,\cdot)
=
\frac{1-x^2}{(1+xy\mu_j)^2}C_{0j}.
\]
Since the updated latent law is again a projection DPP,
\[
|\Pi^-_{0j}|^2
=
\frac{1-x^2}{(1+xy\mu_j)^2}
|\widehat\Pi_{0j}|^2.
\]
Combining this with (4.8) proves (4.3). ∎

---

## 5. The center-update inequality

Because \(\Pi^-\) is a projection,
\[
\sum_{j\ne0}|\Pi^-_{0j}|^2
=
p-p^2=:t.
\tag{5.1}
\]
Hence
\[
T_m^-\le t.
\tag{5.2}
\]

Let
\[
b_0=2p-1,
\qquad
d=1-x^2b_0^2=1-4r^2.
\tag{5.3}
\]

After observing \(Y_0=y\), the same covariance-update formula gives
\[
T_m^+(y)
=
\frac{1-x^2}{(1+xyb_0)^2}T_m^-.
\tag{5.4}
\]
Since
\[
\mathbb P(Y_0=y\mid Y_{\ne0})
=\frac{1+xyb_0}{2},
\]
averaging (5.4) over \(Y_0\) yields the exact moving-weight identity
\[
\boxed{
\mathbb E[T_m^+\mid Y_{\ne0}]
=
\frac{1-x^2}{d}\,T_m^-.}
\tag{5.5}
\]

Moreover,
\[
d=(1-x^2)+4x^2t,
\]
so
\[
d-4t=(1-x^2)(1-4t)\ge0.
\]
Thus \(t/d\le1/4\), and
\[
\begin{aligned}
\frac{(T_m^-)^2}{d^2}
&\le
\frac{T_m^-}{d}\frac{t}{d}\\
&\le
\frac{T_m^-}{4d}\\
&=
\frac{1}{4(1-x^2)}
\mathbb E[T_m^+\mid Y_{\ne0}].
\end{aligned}
\tag{5.6}
\]

Combining (2.2), (4.4), and (5.6) gives the first actual-law estimate:
\[
\boxed{
0\le
F_x''-\underline F_{x,m}''
\le
\frac{32x^4}{(1-x^2)^3}\,
\mathbb E T_m^+.}
\tag{5.7}
\]

No supremum over words appears.

---

## 6. Posterior number variance controls the tail

For an interval
\[
I_L=\{1,\ldots,L\},
\qquad
N_{I_L}=\sum_{i\in I_L}X_i,
\]
the conditional latent law is the projection DPP with kernel \(\Pi^+\). Therefore
\[
\operatorname{Var}(N_{I_L}\mid Y)
=
\sum_{\substack{i\in I_L\\j\notin I_L}}
|\Pi^+_{ij}|^2.
\tag{6.1}
\]

Total variance gives
\[
\mathbb E\operatorname{Var}(N_{I_L}\mid Y)
\le
\operatorname{Var}_Q(N_{I_L})
=:V_Q(L).
\tag{6.2}
\]

By stationarity, if
\[
a_k=\mathbb E|\Pi^+_{0k}|^2,
\]
then
\[
\mathbb E\operatorname{Var}(N_{I_L}\mid Y)
=
\sum_{k\ne0}\min(|k|,L)a_k.
\tag{6.3}
\]
Consequently,
\[
L\sum_{|k|\ge L}a_k\le V_Q(L).
\]
Taking \(L=m+1\),
\[
\boxed{
\mathbb E T_m^+
\le
\frac{V_Q(m+1)}{m+1}.}
\tag{6.4}
\]

### Theorem 6.1 — actual-law average-tail certificate

For every stationary half-filled projection \(Q\), every \(0\le x<1\), and every \(m\ge0\),
\[
\boxed{
0\le
F_x''-\underline F_{x,m}''
\le
\frac{32x^4}{(1-x^2)^3}
\frac{V_Q(m+1)}{m+1}.}
\tag{6.5}
\]

This is the main new estimate.

It is an actual-law inequality: the right side comes from expected posterior variance, not a bound valid for every adversarial word.

---

## 7. Explicit sine-kernel tail

For the sine projection,
\[
Q_{0n}=\frac{\sin(\pi n/2)}{\pi n},
\]
and
\[
V_Q(L)
=
2\sum_{n\ge1}\min(n,L)|Q_{0n}|^2.
\]
Therefore
\[
\boxed{
V_Q(L)
=
\frac2{\pi^2}
\left[
\sum_{\substack{1\le n\le L\\n\ {\rm odd}}}\frac1n
+
L\sum_{\substack{n>L\\n\ {\rm odd}}}\frac1{n^2}
\right].}
\tag{7.1}
\]

Using
\[
\sum_{\substack{1\le n\le L\\n\ {\rm odd}}}\frac1n
\le1+\frac12\log L
\]
and
\[
L\sum_{n>L}\frac1{n^2}\le1,
\]
one obtains the elementary bound
\[
\boxed{
V_Q(L)\le\frac{\log L+4}{\pi^2}.}
\tag{7.2}
\]

Thus
\[
F_x''-\underline F_{x,m}''
\le
\frac{32x^4}{(1-x^2)^3}
\frac{\log(m+1)+4}{\pi^2(m+1)}.
\tag{7.3}
\]

---

## 8. Integrated consequence for \(\Gamma(c)\)

The task scaling is \(x=cu\). Because the original perturbation satisfies
\[
\partial_\delta=u\,\partial_h,
\]
the \(du/u\) integral contributes the weight \(u\):
\[
\Gamma(c)=\int_0^1uF_{cu}''\,du
\]
under the frozen infinite-volume identification. The volume file proves this only in its own unreviewed sense; I am using it here as an explicitly conditional input. citeturn456176view0turn113648view3

Let
\[
\underline\Gamma_m(c)
=
\int_0^1u\,\underline F_{cu,m}''\,du,
\tag{8.1}
\]
where the infinite certificate is obtained as the limit of its finite actual-sine cylinder duals.

Then Theorem 6.1 gives
\[
0\le
\Gamma(c)-\underline\Gamma_m(c)
\le
J(c)\frac{V_Q(m+1)}{m+1},
\tag{8.2}
\]
where
\[
\begin{aligned}
J(c)
&=
\int_0^1
u\,\frac{32(cu)^4}{(1-c^2u^2)^3}\,du\\
&=
\boxed{
\frac{16}{c^2}
\left[
\frac1{2(1-c^2)^2}
-\frac2{1-c^2}
-\log(1-c^2)
+\frac32
\right].}
\end{aligned}
\tag{8.3}
\]

Hence the fully explicit sufficient rule is:

> A rigorous computation showing
> \[
> \underline\Gamma_m(19/20)>0
> \]
> proves \(\Gamma(19/20)>0\).

Unlike a direct evaluation of the exact optimizer, this remains a strict one-sided certificate when rounded downward.

---

## 9. Constants at \(c=19/20\)

Here
\[
1-c^2=\frac{39}{400},
\]
and
\[
\boxed{
J(19/20)
=
\frac{6400}{361}
\left[
\frac{80000}{1521}
-\frac{800}{39}
-\log\frac{39}{400}
+\frac32
\right]
=
636.6680653660999\ldots<637.}
\tag{9.1}
\]

Therefore
\[
\boxed{
\Gamma(19/20)-\underline\Gamma_m(19/20)
\le
637\,\frac{V_Q(m+1)}{m+1}}
\tag{9.2}
\]
and, more elementarily,
\[
\boxed{
\Gamma(19/20)-\underline\Gamma_m(19/20)
\le
\frac{637}{\pi^2}
\frac{\log(m+1)+4}{m+1}.}
\tag{9.3}
\]

High-precision evaluations of the rigorous expression \(J(c)V_Q(L)/L\) are:

| \(L=m+1\) | \(V_Q(L)\) | optimizer-loss upper bound |
|---:|---:|---:|
| 256 | 0.7918795353 | 1.9693922334 |
| 512 | 0.8621102213 | 1.0720274351 |
| 1024 | 0.9323407624 | 0.5796792866 |
| 2048 | 1.0025712673 | 0.3116724166 |
| 4096 | 1.0728017631 | 0.1667525935 |
| 8192 | 1.1430322566 | 0.0888344892 |
| 16384 | 1.2132627496 | 0.0471463408 |

The formulas behind the table are rigorous; the displayed decimals are high-precision rounded evaluations, not interval enclosures.

For comparison, the inherited V14/Fejér remainder contains
\[
16a^{16}\{f_c+f_c^2+g_c^2\},\qquad a=\frac2{1-c}=40,
\]
and the quoted curvature-transfer constant is about \(7.35\times10^{28}\). citeturn105691view3

The comparison must be interpreted correctly: (9.2) replaces the **optimizer-approximation tail on the actual infinite sine law**. It does not by itself replace every kernel-change and finite-Fejér-to-sine term in the old remainder.

---

## 10. Exact conditional \(R=1\) benchmark

This section is conditional on the unreviewed S9 inequality
\[
A_1''>
3+\frac{63c^4}{8\pi^4}.
\tag{10.1}
\]
S9 explicitly states that this proves only the \(R=1\) case. citeturn105691view4

For \(R=1\), put
\[
t=\frac{c^2u^2}{\pi^2}.
\]
For all four external words,
\[
\|v\|^2=2t,
\]
while \(r=\pm t\) on the two equal words and \(r=0\) on the two mixed words. Hence the exact \(m=0\) dual loss is
\[
\boxed{
\Delta_{1,0}(u)
=
16t^2
\left[
1+(1-4t^2)^{-2}
\right].}
\tag{10.2}
\]

Since \(u\in[1/2,1]\),
\[
\begin{aligned}
\int_{1/2}^1u\,\Delta_{1,0}(u)\,du
&\le
\frac{21c^4}{8\pi^4}
\left[
1+
\left(1-\frac{4c^4}{\pi^4}\right)^{-2}
\right].
\end{aligned}
\tag{10.3}
\]

Combining (10.1) and (10.3),
\[
\boxed{
\begin{aligned}
\underline A_{1,0}
>
3+\frac{63c^4}{8\pi^4}
-\frac{21c^4}{8\pi^4}
\left[
1+
\left(1-\frac{4c^4}{\pi^4}\right)^{-2}
\right].
\end{aligned}}
\tag{10.4}
\]

At \(c=19/20\), the right side is
\[
3.0204041069988\ldots>3.0204.
\tag{10.5}
\]
The last conservative inequality can be checked using only the rational bound \(\pi<3.1416\).

This is an exact symbolic benchmark for the new correction, conditional on S9’s \(R=1\) lower bound. It is not evidence for the infinite-volume sign.

---

## 11. Finite Fejér diagnostics

I independently enumerated the actual finite atoms for \(R=1,3,5,7\), used the analytic determinant/resolvent jets, and subtracted the exact loss (2.2). The direct curvatures reproduce the submission’s exploratory values. citeturn113648view0

### Pointwise at \(u=1\), \(c=0.95\)

| \(R\) | direct \(F''\) | \(m=0\) certificate | \(m=1\) certificate | \(m=R-1\) certificate |
|---:|---:|---:|---:|---:|
| 1 | 8.4559342574 | 8.1789402257 | 8.4559342574 | 8.1789402257 |
| 3 | 11.9939524638 | 8.8061189784 | 11.8460394819 | 11.9872791256 |
| 5 | 17.0995201986 | 9.2877742915 | 16.3236118530 | 17.0983561011 |
| 7 | 22.9489226744 | 9.5611980355 | 21.0445705947 | 22.9485454516 |

For \(R=1\), \(m=1\) is already the exact correction; the last column is not meaningful as a distinct radius.

### Integrated over the task ranges \(u\in[1/(R+1),1]\)

| \(R\) | direct \(A_R''\) | \(m=0\) certificate | \(m=1\) certificate | \(m=R-1\) certificate |
|---:|---:|---:|---:|---:|
| 1 | 3.072020646684 | 3.027194387011 | 3.072020646684 | 3.027194387011 |
| 3 | 4.267455268114 | 3.860882425046 | 4.254761674266 | 4.266895205448 |
| 5 | 4.896892906580 | 4.032478585421 | 4.834979523836 | 4.896821231080 |
| 7 | 5.409329186481 | 4.073879753022 | 5.266812769059 | 5.409310109495 |

The complete integrated loss sequences, ordered by \(m=0,\ldots,R\), were:

\[
\begin{array}{c|l}
R&\Delta_{R,m}\\ \hline
1&
(0.044826259673,\ 0)\\
3&
(0.406572843069,\ 0.012693593849,\ 0.000560062666,\ 0)\\
5&
(0.864414321160,\ 0.061913382744,\ 0.010391096272,\\
&\qquad 0.001031724864,\ 0.000071675500,\ 0)\\
7&
(1.335449433458,\ 0.142516417422,\ 0.034966505792,\\
&\qquad0.006351165147,\ 0.001452971156,\ 0.000219858941,\\
&\qquad0.000019076985,\ 0).
\end{array}
\]

**Rigor level:** ordinary IEEE double precision, exact atom enumeration, analytic derivatives, and 32-node Gauss–Legendre quadrature. These are diagnostics, not interval certificates. In particular, they do not transfer the sign to \(R=\infty\).

---

## 12. Why this is not the exact optimizer under another name

For the exact infinite projection channel,
\[
K_x(I-K_x)=\frac{1-x^2}{4}I.
\]
Together with the Schur-energy identity, this implies
\[
\|v\|^2=\frac{x^2-4r^2}{1-x^2},
\]
so the exact optimizer can be rewritten as the scalar expression
\[
\frac{4x^2(1-4r^2)}
     {(1-x^2)(1+\theta r)^2}.
\tag{12.1}
\]

I did not use (12.1) as the candidate. It is exact only after one has already passed to the projection channel and therefore does not provide a robust finite-Fejér correction.

As a diagnostic, inserting (12.1) into the actual finite Fejér models at \(u=1,c=0.95\) produces dual losses

\[
655.6664,\quad
583.7382,\quad
526.7264,\quad
480.1539
\]
for \(R=1,3,5,7\), respectively, in ordinary double precision.

By contrast, \(k_m\) is defined by the same formula on every prescribed finite Fejér model and on the sine limit; its discrepancy is the monotone tail energy \(\tau_m\). That finite-volume robustness is the reason for retaining the local response coordinates.

---

## 13. Relation to the zero-correction counterexample

The legal four-site example in the submission gives
\[
\underline F''[0]\approx-9.979790939,
\]
so no claim that the zero correction is universally positive is available. citeturn113648view2

The present radius-zero correction is instead
\[
k_{0,\alpha}=\frac{16r^2}{(1+\theta r)^2}.
\]
Moreover, for every finite model,
\[
\underline F''[k_m]-\underline F''[0]
=
8\mathbb E_w
\frac{(\|v\|^2+4r^2)^2-\tau_m^2}
     {(1-4r^2)^2}
\ge0.
\tag{13.1}
\]
Thus this construction strictly improves the zero correction whenever the retained posterior or local response is nont
