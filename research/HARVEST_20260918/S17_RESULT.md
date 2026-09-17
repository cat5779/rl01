> AUTHOR SUBMISSION — PENDING INDEPENDENT REVIEW. Full user-supplied Markdown text; reported numerical evidence is not independently reproduced here.

# PRO01 RESULT — A rank-one Fisher/Doob certificate for the SA03 infinite local curvature

**Branch studied:** `research/pro01-sa03-sign`  
**Scope:** only `research/PRO01/` and the SA03 inputs listed in `PROMPT.md`  
**Benchmark:** \(c=19/20\)  
**Research status:** the sign of \(\Gamma(19/20)\) is **INCOMPLETE**. The main output is a new exact one-sided certificate and a dimension-free local correction formula. No entropy-rate conclusion is claimed.

---

## 0. Executive statement

### Main target

> **INCOMPLETE.** I did not prove either \(\Gamma(19/20)>0\) or \(\Gamma(19/20)<0\).

### Strongest new result

> **PROVED.** For every finite Fejér model, the curvature admits an exact variational lower certificate built from the true conditional DPP laws. For any explicitly chosen correction \(k\), the difference between the true curvature and the certificate is an explicit nonnegative \(L^2\) norm. Combining the certificate with the already established effective volume remainder gives
> \[
> \boxed{\Gamma(c)\ge \underline A_{R,k}(c)-\varepsilon_R(c;m,d,M),}
> \]
> where every term on the right is finite and computable, and \(\varepsilon_R\) contains no unknown target quantity.

The certificate is obtained by interpolating the two actual external laws conditioned on \(Y_0=1\) and \(Y_0=0\). The interpolation is itself an exact rank-one DPP path. The relevant Pearson/Fisher term has a quadratic dual. An approximate correction can therefore only lose a known-sign quantity.

### Local form of the remaining obstruction

> **PROVED.** At half filling the normalized finite-volume curvature has the exact decomposition
> \[
> \boxed{F_x''(1/2)=8+B_x+S_x,\qquad B_x\ge0,}
> \]
> where \(x=cu\), \(B_x\) is an explicit nonnegative boundary term and \(S_x\) is an explicit actual-law edge/plaquette term containing all changing weights, single flips and double flips. It uses a Doob transform of the signed transport; no positive Markov dissipation is assumed.

After the verified volume passage,
\[
\boxed{\Gamma(c)=4+B(c)+S(c),\qquad B(c):=\int_0^1uB_{cu}\,du\ge0.}
\]
Thus the smallest remaining sign obstruction in this representation is the lower bound
\[
S(19/20)>-4-B(19/20).
\]
The stronger but sufficient estimate \(S(19/20)>-4\) would settle positivity.

### Boundary theorem

> **PROVED.** With only one external site, the curvature is always at least the independent value \(8\), with strict inequality when the off-diagonal correlation is nonzero.

### Failed simple certificate

> **DISPROVED.** The zero-correction version of the variational certificate is not nonnegative for every legal half-filled bipartite DPP. A four-site rational counterexample is given below and was evaluated with interval arithmetic. This prevents promoting the simplest numerical pattern into a theorem.

### Numerical work

> **EXPLORATORY, NOT CERTIFIED.** Exact word enumeration in double precision for Fejér \(R=1,3,5,7\) at \(c=0.95\) gave positive direct curvature, positive \(B_x\), and positive residual \(S_x\). These calculations do not establish the infinite-volume sign and are not used in a proof.

---

## 1. Fixed notation and the target

Fix a finite site set
\[
V=\{0\}\sqcup C
\]
and a Hermitian DPP kernel
\[
K(h)=hI+H,
\]
where \(H\) is independent of \(h\), \(H_{00}=0\), and the interval of \(h\) under discussion keeps the spectrum of \(K(h)\) in \((0,1)\). In the Fejér model,
\[
h=\frac12+u\delta,\qquad H=xH_R^0,\qquad x=cu.
\]
I suppress the fixed \(R,u\) subscripts until Section 7.

For an external word \(z\in\{0,1\}^C\), write
\[
D_z=\operatorname{diag}(1-z_i)_{i\in C},\qquad
B_z(h)=K_C(h)-D_z,
\]
\[
G_z(h)=B_z(h)^{-1},\qquad b=H_{C0}.
\]
The true external atom and the true center posterior are
\[
w_h(z)=(-1)^{|C|-|z|}\det B_z(h),
\]
\[
q_h(z)=\mathbb P_h(Y_0=1\mid Y_C=z)
      =h-b^*G_z(h)b.                                      \tag{1.1}
\]
Define
\[
\phi(q)=\left(q-\frac12\right)\log\frac q{1-q},
\qquad F(h)=\sum_z w_h(z)\phi(q_h(z)).                    \tag{1.2}
\]
For the Fejér problem,
\[
A_R''(0)=\int_{1/(R+1)}^1 u\,F_{R,u}''(1/2)\,du.          \tag{1.3}
\]
The established volume theorem identifies
\[
\Gamma(c)=\int_0^1u\,\mathbb E_{\infty,u}
                  [\overline{\mathcal G}_{\infty,u}]\,du
          =\lim_{R\to\infty}A_R''(0).                    \tag{1.4}
\]
The expectation in (1.4) is under the true unsmoothed infinite sine DPP.

Two elementary derivatives used below are
\[
\phi''(q)=\frac1{2q^2(1-q)^2},\qquad \phi''(1/2)=8.       \tag{1.5}
\]

---

## 2. Conditional laws and the exact rank-one interpolation

### Proposition 2.1 — conditional DPP laws

> **PROVED.** Let
> \[
> P_{+,h}(z)=\mathbb P_h(Y_C=z\mid Y_0=1),\qquad
> P_{-,h}(z)=\mathbb P_h(Y_C=z\mid Y_0=0).
> \]
> Then they are DPP atom laws on \(C\) with kernels
> \[
> K_{+,h}=K_C(h)-\frac{bb^*}{h},\qquad
> K_{-,h}=K_C(h)+\frac{bb^*}{1-h}.                         \tag{2.1}
> \]
> For every \(\alpha\in[0,1]\), the mixture
> \[
> p_{h,\alpha}=\alpha P_{+,h}+(1-\alpha)P_{-,h}           \tag{2.2}
> \]
> is again exactly a DPP atom law, with kernel
> \[
> K_{h,\alpha}=K_C(h)+\theta(h,\alpha)bb^*,
> \qquad
> \theta(h,\alpha)=\frac{h-\alpha}{h(1-h)}.              \tag{2.3}
> \]

#### Proof

Let
\[
r_h(z)=b^*G_z(h)b=h-q_h(z).                               \tag{2.4}
\]
By the matrix determinant lemma,
\[
P_{+,h}(z)=w_h(z)\left(1-\frac{r_h(z)}h\right),
\]
\[
P_{-,h}(z)=w_h(z)\left(1+\frac{r_h(z)}{1-h}\right).       \tag{2.5}
\]
Consequently
\[
p_{h,\alpha}(z)
=w_h(z)\left[1+\frac{h-\alpha}{h(1-h)}r_h(z)\right].     \tag{2.6}
\]
The determinant lemma applied to \(B_z(h)+\theta bb^*\) gives precisely (2.6), proving (2.3). Since (2.2) is a convex mixture of probability laws, the rank-one kernel in (2.3) is legal throughout \(\alpha\in[0,1]\). ∎

### Proposition 2.2 — exact conditional-divergence identity

> **PROVED.** For all legal \(h\),
> \[
> F(h)=\phi(h)+\frac h2D(P_{+,h}\Vert P_{-,h})
>                  +\frac{1-h}{2}D(P_{-,h}\Vert P_{+,h}). \tag{2.7}
> \]

#### Proof

For a fixed external word, Bayes' formula gives
\[
\frac{q_h(z)}{1-q_h(z)}
=\frac h{1-h}\frac{P_{+,h}(z)}{P_{-,h}(z)}.               \tag{2.8}
\]
Multiply the logarithm of (2.8) by
\[
w_h(z)\left(q_h(z)-\frac12\right)
=\frac12\big[hP_{+,h}(z)-(1-h)P_{-,h}(z)\big]
\]
and sum over \(z\). The prior-odds term sums to \(\phi(h)\); the remaining two terms are the two directed KL divergences in (2.7). ∎

At \(h=1/2\), this reduces to
\[
F(1/2)=\frac14\big[D(P_+\Vert P_-)+D(P_-\Vert P_+)\big], \tag{2.9}
\]
so the value is one quarter of the Jeffreys divergence of the two actual conditional external laws.

---

## 3. Fisher-mixture representation and its quadratic dual

Set
\[
d_h(z)=P_{+,h}(z)-P_{-,h}(z),
\]
\[
\mathcal I_h(\alpha)=\sum_z\frac{d_h(z)^2}{p_{h,\alpha}(z)}.\tag{3.1}
\]
This is the Fisher information of the affine mixture path \(\alpha\mapsto p_{h,\alpha}\).

### Theorem 3.1 — exact Fisher integral

> **PROVED.** With \(G(h):=F(h)-\phi(h)\),
> \[
> \boxed{
> G(h)=\frac12\int_0^1
> \big[h(1-\alpha)+(1-h)\alpha\big]\mathcal I_h(\alpha)
> \,d\alpha.}                                             \tag{3.2}
> \]

#### Proof

Let
\[
\mathscr H_h(\alpha)=\sum_zp_{h,\alpha}(z)
                                      \log p_{h,\alpha}(z).
\]
Because \(p_{h,\alpha}\) is affine in \(\alpha\),
\[
\mathscr H_h''(\alpha)=\mathcal I_h(\alpha).               \tag{3.3}
\]
The Bregman formulas for the two directed KL divergences are
\[
D(P_+\Vert P_-)=\int_0^1(1-\alpha)\mathcal I_h(\alpha)d\alpha,
\]
\[
D(P_-\Vert P_+)=\int_0^1\alpha\mathcal I_h(\alpha)d\alpha.\tag{3.4}
\]
Substitution into (2.7) proves (3.2). ∎

### Theorem 3.2 — sign-preserving quadratic dual

> **PROVED.** For each \(h,\alpha\),
> \[
> \mathcal I_h(\alpha)
> =\sup_f\sum_z\big[2d_h(z)f(z)-p_{h,\alpha}(z)f(z)^2\big],\tag{3.5}
> \]
> with unique optimizer
> \[
> f_{*,h,\alpha}(z)=\frac{d_h(z)}{p_{h,\alpha}(z)}.         \tag{3.6}
> \]
> Moreover, the exact gap is
> \[
> \mathcal I_h(\alpha)-\mathcal Q_h(\alpha;f)
> =\sum_zp_{h,\alpha}(z)\big(f(z)-f_{*,h,\alpha}(z)\big)^2.\tag{3.7}
> \]

#### Proof

Complete the square in each atom:
\[
\frac{d^2}{p}-\big(2df-pf^2\big)=p\left(f-\frac dp\right)^2.\qedhere
\]

### Corollary 3.3 — a finite curvature lower certificate

Fix \(h_0=1/2\). Choose any explicitly specified function
\[
k_\alpha:\{0,1\}^C\to\mathbb R
\]
and define the touching test path
\[
f_{h,\alpha}=f_{*,h_0,\alpha}+(h-h_0)k_\alpha.            \tag{3.8}
\]
Set
\[
\mathcal Q_h(\alpha)=
\sum_z\big[2d_h(z)f_{h,\alpha}(z)
       -p_{h,\alpha}(z)f_{h,\alpha}(z)^2\big],             \tag{3.9}
\]
\[
\underline F''[k]
=8+\left.\frac12\frac{d^2}{dh^2}\right|_{h=1/2}
\int_0^1\big[h(1-\alpha)+(1-h)\alpha\big]
                 \mathcal Q_h(\alpha)\,d\alpha.           \tag{3.10}
\]
Then
\[
\boxed{F''(1/2)\ge\underline F''[k].}                     \tag{3.11}
\]
More precisely,
\[
\boxed{
F''(1/2)-\underline F''[k]
=\int_0^1c_0(\alpha)
   \sum_zp_{1/2,\alpha}(z)
   \big(k_\alpha(z)-\dot f_{*,\alpha}(z)\big)^2d\alpha,} \tag{3.12}
\]
where
\[
c_0(\alpha)=\frac12,
\qquad
\dot f_{*,\alpha}=\left.\partial_h f_{*,h,\alpha}\right|_{h=1/2}.
\]

#### Proof

Apply (3.7) to the path (3.8). At \(h=h_0\), the gap and its first derivative vanish. Its second derivative is twice the displayed squared \(L^2\) error. Multiplying by the positive coefficient in (3.2) and differentiating twice yields (3.12). ∎

This is the first sign tool. It is a Rayleigh–Ritz/Stein-control-variate principle: an approximate correction never creates an uncontrolled signed error.

### Explicit optimal correction

At \(h=1/2\), put
\[
\theta=2-4\alpha,
\qquad R_{\theta,z}=(B_z+\theta bb^*)^{-1}.                \tag{3.13}
\]
Then
\[
f_{*,\alpha}(z)=-4b^*R_{\theta,z}b.                      \tag{3.14}
\]
At fixed \(\alpha\),
\[
\left.\partial_hK_{h,\alpha}\right|_{1/2}=I+4bb^*=:E,
\]
so
\[
\boxed{\dot f_{*,\alpha}(z)=4b^*R_{\theta,z}ER_{\theta,z}b.}\tag{3.15}
\]
No Poisson equation and no unknown constant is hidden in (3.15). A local or low-rank approximation to (3.15) can be inserted into (3.10), and (3.12) gives the exact nonnegative loss.

---

## 4. Change of variables and the rank-one score

For general legal \(h\), change from \(\alpha\) to
\[
\theta=\frac{h-\alpha}{h(1-h)}.
\]
The endpoints are
\[
-\frac1h\le\theta\le\frac1{1-h}.                          \tag{4.1}
\]
Define
\[
a_\theta(z)=1+\theta r_h(z),
\qquad p_\theta(z)=w_h(z)a_\theta(z),                      \tag{4.2}
\]
\[
g_\theta(z)=\frac{r_h(z)}{1+\theta r_h(z)}
             =\partial_\theta\log p_\theta(z),            \tag{4.3}
\]
\[
J(h,\theta)=\mathbb E_{p_\theta}[g_\theta^2]
=\sum_zw_h(z)\frac{r_h(z)^2}{1+\theta r_h(z)}.             \tag{4.4}
\]

### Proposition 4.1 — exact \(\theta\)-representation

> **PROVED.**
> \[
> \boxed{
> G(h)=\int_{-1/h}^{1/(1-h)}
> \left(1+\frac{(2h-1)\theta}{2}\right)J(h,\theta)d\theta.}\tag{4.5}
> \]

#### Proof

From (2.5),
\[
d_h(z)=-\frac{w_h(z)r_h(z)}{h(1-h)}.
\]
The Jacobian is \(d\alpha=-h(1-h)d\theta\), while
\[
h(1-\alpha)+(1-h)\alpha
=h(1-h)[2+(2h-1)\theta].
\]
Substitute these expressions into (3.2). ∎

At \(h=1/2\), \(\theta\in[-2,2]\), and
\[
J_\theta(h,\theta)=-\mathbb E_{p_\theta}[g_\theta^3].     \tag{4.6}
\]

---

## 5. Doob transform of the signed word transport

This section is the dimension-free localization step.

For a flip at coordinate \(i\in C\), write
\[
z^i=z\text{ with bit }i\text{ flipped},
\quad \sigma_i(z)=2z_i-1,
\quad o_i(z)=\frac{w_h(z^i)}{w_h(z)}.                      \tag{5.1}
\]
Define signed rates and their operator by
\[
\varrho_i(z)=-\sigma_i(z)o_i(z),
\qquad
(Tf)(z)=\sum_i\varrho_i(z)[f(z^i)-f(z)].                  \tag{5.2}
\]
The rates are not nonnegative.

### Lemma 5.1 — actual-law transport and frozen posterior offset

> **PROVED.**
> \[
> \partial_hw_h=T^*w_h,                                   \tag{5.3}
> \]
> and for the material derivative
> \[
> D:=\partial_h+T
> \]
> one has
> \[
> Dq_h=1,
> \qquad Dr_h=0.                                           \tag{5.4}
> \]

#### Proof

Multilinearity of the atom determinant in the common diagonal \(h\) gives
\[
\partial_hw_h(z)=\sum_i\sigma_i(z)\big[w_h(z)+w_h(z^i)\big].\tag{5.5}
\]
A direct calculation using \(w(z)o_i(z)=w(z^i)\) shows that the right side of (5.5) is \(T^*w\).

For the posterior, let
\[
A_h(z)=w_h(z)q_h(z),\qquad B_h(z)=w_h(z)(1-q_h(z))
\]
be the two full joint slices. Applying the same multilinear derivative to the full word, the center-coordinate term in \(A_h'\) is \(A_h+B_h=w_h\). The external-coordinate terms are exactly transported by \(T\). Dividing by \(w_h\) gives \((\partial_h+T)q_h=1\). Since \(r_h=h-q_h\), (5.4) follows. ∎

### Lemma 5.2 — exact signed Doob transform

For fixed \(\theta\), define
\[
\varrho_i^\theta(z)
=\varrho_i(z)\frac{a_\theta(z^i)}{a_\theta(z)},
\]
\[
(T^\theta f)(z)=\sum_i\varrho_i^\theta(z)[f(z^i)-f(z)].  \tag{5.6}
\]
Then
\[
\boxed{\partial_hp_\theta=(T^\theta)^*p_\theta,}          \tag{5.7}
\]
\[
\boxed{(\partial_h+T^\theta)g_\theta=0.}                  \tag{5.8}
\]

#### Proof

Because \(Da_\theta=\theta Dr_h=0\), expanding the adjoint of (5.6) gives (5.7).

For (5.8), use the exact difference identity
\[
g_\theta(z^i)-g_\theta(z)
=\frac{r_h(z^i)-r_h(z)}{a_\theta(z^i)a_\theta(z)}.        \tag{5.9}
\]
Multiplication by \(\varrho_i^\theta\) cancels \(a_\theta(z^i)\), so
\[
T^\theta g_\theta
=\frac{Tr_h}{a_\theta^2}.
\]
Also \(\partial_hg_\theta=(\partial_hr_h)/a_\theta^2\). Equation (5.8) is therefore equivalent to \(Dr_h=0\). ∎

The transform is called “Doob” only in the algebraic sense. Since \(\varrho_i^\theta\) may be negative, it is not a Markov generator.

### Theorem 5.3 — local first and second derivatives of \(J\)

Define
\[
\Gamma_\theta(z)
=\sum_i\varrho_i^\theta(z)
           [g_\theta(z^i)-g_\theta(z)]^2.                 \tag{5.10}
\]
Then
\[
\boxed{J_h(h,\theta)=\mathbb E_{p_\theta}[\Gamma_\theta].}\tag{5.11}
\]
Define
\[
\mathcal K_\theta
=\partial_h\Gamma_\theta+T^\theta\Gamma_\theta.          \tag{5.12}
\]
Then
\[
\boxed{J_{hh}(h,\theta)=\mathbb E_{p_\theta}[\mathcal K_\theta].}\tag{5.13}
\]

#### Proof

Differentiate \(J=\mathbb E_{p_\theta}g_\theta^2\), use (5.7), and move the adjoint onto \(g^2\):
\[
J_h=\mathbb E_{p_\theta}
 [\partial_h(g^2)+T^\theta(g^2)].
\]
The algebraic carré-du-champ identity
\[
T^\theta(g^2)-2gT^\theta g
=\sum_i\varrho_i^\theta(\Delta_i g)^2
\]
together with (5.8) proves (5.11). Differentiate (5.11) once more and use (5.7), which gives (5.13). ∎

### Fully expanded single/double-flip form

At \(h=1/2\), put
\[
G_z=(S_z/2+H_C)^{-1},\qquad v_z=G_zb,
\qquad r_z=b^*G_zb.                                       \tag{5.14}
\]
At fixed word,
\[
\dot r_z:=\partial_hr_z=-b^*G_z^2b=-\|v_z\|^2,
\qquad
\dot g_\theta(z)=\frac{\dot r_z}{a_\theta(z)^2}.         \tag{5.15}
\]
The determinant ratio gives
\[
\varrho_i(z)=\sigma_i(z)-(G_z)_{ii},
\qquad
\dot\varrho_i(z)=(G_z^2)_{ii}.                            \tag{5.16}
\]
Writing \(a=a_\theta(z)\), \(a_i=a_\theta(z^i)\),
\[
\dot\varrho_i^\theta
=\frac{a_i}{a}\dot\varrho_i
 +\varrho_i\frac{a_i}{a}\theta
 \left(\frac{\dot r_i}{a_i}-\frac{\dot r}{a}\right).   \tag{5.17}
\]
Hence
\[
\boxed{
\begin{aligned}
\mathcal K_\theta(z)={}&
 \sum_i\dot\varrho_i^\theta(z)(\Delta_i g_\theta)^2\\
&+2\sum_i\varrho_i^\theta(z)
             \Delta_i g_\theta\,\Delta_i\dot g_\theta\\
&+\sum_j\varrho_j^\theta(z)
             [\Gamma_\theta(z^j)-\Gamma_\theta(z)].
\end{aligned}}                                            \tag{5.18}
\]
The last line contains the complete connected double-flip terms \(z^{ij}\). No term from changing weights has been dropped.

---

## 6. Positive boundary term and the exact residual

Differentiate (4.5) twice at \(h=1/2\). The moving endpoints satisfy
\[
a(h)=-1/h,\quad b(h)=1/(1-h),
\]
\[
a'(1/2)=b'(1/2)=4,
\quad a''(1/2)=-16,
\quad b''(1/2)=16.
\]
A direct Leibniz calculation gives
\[
\begin{aligned}
G''(1/2)={}&32[J(2)+J(-2)]
 +8[J_h(2)-J_h(-2)]\\
&+16[J_\theta(2)-J_\theta(-2)]
 +\int_{-2}^2[J_{hh}(\theta)+2\theta J_h(\theta)]d\theta.\tag{6.1}
\end{aligned}
\]
Using (4.6), (5.11), and (5.13), define
\[
\boxed{
B_x=16\mathbb E_{p_2}[g_2^2(2-g_2)]
   +16\mathbb E_{p_{-2}}[g_{-2}^2(2+g_{-2})],}             \tag{6.2}
\]
\[
\boxed{
S_x=8\big(\mathbb E_{p_2}\Gamma_2
           -\mathbb E_{p_{-2}}\Gamma_{-2}\big)
 +\int_{-2}^2\mathbb E_{p_\theta}
       [\mathcal K_\theta+2\theta\Gamma_\theta]d\theta.}\tag{6.3}
\]

### Theorem 6.1 — exact local decomposition

> **PROVED.**
> \[
> \boxed{F_x''(1/2)=8+B_x+S_x.}                            \tag{6.4}
> \]
> Moreover,
> \[
> \boxed{B_x\ge0.}                                        \tag{6.5}
> \]

#### Proof of the sign in (6.5)

At half filling,
\[
r=\frac12-q\in(-1/2,1/2).
\]
For \(\theta=2\),
\[
g_2=\frac r{1+2r}<\frac14,
\]
so \(2-g_2>0\). For \(\theta=-2\),
\[
g_{-2}=\frac r{1-2r}>-\frac14,
\]
so \(2+g_{-2}>0\). Both expectations in (6.2) are therefore nonnegative. ∎

### Infinite-volume consequence

For each finite symmetric window, (6.4) is exact. The endpoint term (6.2) can be rewritten as an expectation under \(w\) of a bounded continuous rational function of \(r=1/2-q\). The posterior gap
\[
q\in[(1-c)/2,(1+c)/2]
\]
keeps its denominators at least \(1-c\). Therefore the established posterior convergence gives a separate limit \(B_x\ge0\).

Define the infinite residual by the controlled finite-window limit
\[
S_x:=F_x''(1/2)-8-B_x.                                     \tag{6.6a}
\]
Equivalently, \(S_x\) is the limit of the complete finite expression (6.3), with the edge and plaquette sums truncated symmetrically before the window is enlarged. The existence of this *combined* limit follows from the established V14 volume theorem together with the bounded limit of \(B_x\). I do **not** claim a new term-by-term absolute-tail bound for the separated pieces of (6.3); the rigorous effective tail used later remains Q14/Q5.

Thus
\[
\boxed{
\Gamma(c)=4+B(c)+S(c),
\quad B(c)=\int_0^1uB_{cu}du\ge0,
\quad S(c)=\int_0^1uS_{cu}du.}                            \tag{6.6}
\]

> **INCOMPLETE.** I did not prove a sufficient lower bound on \(S(19/20)\). The signed nature of \(\varrho_i^\theta\) means that neither \(\Gamma_\theta\) nor \(\mathcal K_\theta\) is pointwise nonnegative.

---

## 7. Effective finite certificate under the actual probability law

This section records the rigorous remainder needed to turn the variational lower bound into a finite sign test.

### 7.1 Existing explicit volume remainder

For \(0<c<1\), define
\[
a=\frac2{1-c},\qquad
C_c=\frac{21c^4a^{18}}{16},\qquad
B_c=8+C_c,
\]
\[
\kappa_c=\min\{1/2,-\log c\},
\]
\[
V_c=\frac{2\sqrt2c}{\pi(1-c)}+\frac{4c^2}{(1-c)^2},
\]
\[
F_c=\sqrt2V_c+\frac1{1-c},
\qquad
G_c=\frac{8\sqrt2c}{(1-c)^2}+\frac2{1-c}.                 \tag{7.1}
\]
For \(s\ge1\), let
\[
f_c(s)=
\begin{cases}
ac/2,&s<e^4,\\
\min\{ac/2,F_ce^{-\kappa_c\sqrt{\log s}}\},&s\ge e^4,
\end{cases}
\]
\[
g_c(s)=
\begin{cases}
a,&s<e^4,\\
\min\{a,G_ce^{-\kappa_c\sqrt{\log s}}\},&s\ge e^4.
\end{cases}                                                \tag{7.2}
\]
For integer \(m\ge2\),
\[
T_c(m)=16a^{16}
\{f_c(m)+f_c(m/2)^2+g_c(m/2)^2\}.                         \tag{7.3}
\]
For
\[
2\le m,
\qquad2m\le d\le R/2,
\qquad2m\le M\le R/2,                                    \tag{7.4}
\]
set
\[
D_R(d,m)=2a^2\{R^{-1/2}+\sqrt{2d/R}+f_c(d)+g_c(d-m)\},
\]
\[
E_{\rm ker}(R;m,d)=2T_c(m)+128a^{12}m^2D_R(d,m),
\]
\[
E_{\rm cyl}(M;m)=2T_c(m)+128a^{13}m^2
                   \{f_c(M)+g_c(M-m)\},
\]
\[
E_c(R;m,d,M)=E_{\rm ker}(R;m,d)+2E_{\rm cyl}(M;m)
            +\frac{4acB_cM^2}{\pi(R+1)}.                  \tag{7.5}
\]
The existing effective-remainder theorem gives
\[
\boxed{
|A_R''(0)-\Gamma(c)|\le
\varepsilon_R(c;m,d,M),}                                  \tag{7.6}
\]
where
\[
\boxed{
\varepsilon_R=\frac12E_c(R;m,d,M)
 +\frac4{(R+1)^2}+\frac{C_c}{6(R+1)^6}.}                  \tag{7.7}
\]
This is a true-word-law estimate. It includes kernel change, finite observation, changing atom weights and the single/double-flip V14 kernel. It contains no \(\Gamma\) on the right.

At \(c=19/20\), \(a=40\) and the conservative constant \(C_c\) is approximately \(7.35\times10^{28}\). Thus (7.7) is rigorous but not numerically useful at modest \(R\).

### 7.2 New one-sided finite representation

For each \(R,u\), choose any explicit correction \(k_{R,u,\alpha}(z)\) and form the finite certificate (3.10). Define
\[
\underline A_{R,k}(c)
=\int_{1/(R+1)}^1u\,
   \underline F_{R,u}''[k]\,du.                            \tag{7.8}
\]
Every object in (7.8) is finite:

* the sum is over the actual \(2^{2R}\) external words;
* \(p_{h,\alpha}\) is the exact rank-one DPP mixture (2.3);
* both integrals are one-dimensional;
* derivatives are finite determinant/resolvent derivatives;
* interval quadrature can be used after \(k\) is fixed.

By (3.11),
\[
A_R''(0)\ge\underline A_{R,k}(c).                          \tag{7.9}
\]
Combining (7.9) with (7.6) gives the promised sign-preserving representation:
\[
\boxed{
\Gamma(c)\ge
\underline A_{R,k}(c)-\varepsilon_R(c;m,d,M).}            \tag{7.10}
\]

> **PROVED.** Formula (7.10) is a rigorously controlled finite lower representation. Its error does not depend on the unknown target. It uses the actual finite Fejér DPP law, not an independent-word surrogate.

The exact loss from a nonoptimal \(k\) is the nonnegative integral in (3.12). Therefore a correction may be designed numerically and then frozen and checked rigorously; no statistical fit is part of the proof after freezing.

### 7.3 Direct spatial truncation of the infinite V14 kernel

Let \(\overline{\mathcal G}^{[m]}\) be V14 with its single sum restricted to \(|i|\le m\) and its double sum restricted to \(|i|,|j|\le m\), while retaining the actual full posterior and actual full word law. Define
\[
\Gamma^{[m]}(c)=\int_0^1u\,
 \mathbb E_{\infty,u}[\overline{\mathcal G}^{[m]}]du.      \tag{7.11}
\]
The established pointwise Q14 bound yields immediately
\[
\boxed{|\Gamma(c)-\Gamma^{[m]}(c)|\le\frac12T_c(m).}      \tag{7.12}
\]
This is a two-sided tail bound and again contains no unknown target.

### What is and is not improved

* **Improved:** the curvature evaluation can be replaced by a one-sided variational certificate. Approximation of the correction has an exact nonnegative error rather than an uncontrolled signed error.
* **Improved:** the optimizer derivative is explicit, (3.15), and the Doob formula (5.18) removes global score traces and displays the connected edge/plaquette obstruction.
* **Not improved:** the inherited Fejér-to-sine constant \(\varepsilon_R\) remains extremely conservative at \(c=0.95\).
* **Not completed:** no interval evaluation of (7.10) at a sufficiently large \(R\) was carried out.

---

## 8. A completely solved boundary case

Consider two sites, center \(0\) and one external site \(1\), with
\[
K(h)=\begin{pmatrix}h&a\\ \bar a&h\end{pmatrix}.
\]
Let
\[
\rho=4|a|^2\in[0,1).
\]

### Theorem 8.1 — one-neighbour positivity

> **PROVED.**
> \[
> \boxed{
> F''(1/2)=
> \frac{8(1+\rho^2)}{(1-\rho)^2(1+\rho)}
> -4\log\frac{1+\rho}{1-\rho}.}                           \tag{8.1}
> \]
> In particular,
> \[
> F''(1/2)\ge8,
> \]
> with equality only at \(a=0\).

#### Proof

The external marginal is Bernoulli\((h)\), and
\[
q_h(1)=h-\frac{|a|^2}{h},
\qquad
q_h(0)=h+\frac{|a|^2}{1-h}.                               \tag{8.2}
\]
Hence
\[
F(h)=h\phi(q_h(1))+(1-h)\phi(q_h(0)).                     \tag{8.3}
\]
Twice differentiating (8.3) at \(h=1/2\) and substituting \(\rho=4|a|^2\) gives (8.1). Let \(D(\rho)=F''(1/2)-8\). Direct differentiation gives
\[
D'(\rho)=\frac{16\rho(\rho+3)}{(1-\rho)^3(1+\rho)^2}>0
\quad(0<\rho<1),                                          \tag{8.4}
\]
while \(D(0)=0\). ∎

This theorem shows that the first nontrivial spatial interaction cannot create negative curvature. It does not control multi-site plaquette terms.

---

## 9. A legal counterexample to the zero-correction rule

A tempting choice in (3.8) is \(k\equiv0\). This gives a valid lower bound, but it need not be nonnegative.

At \(h=1/2\), define
\[
H=\begin{pmatrix}0&A\\A^T&0\end{pmatrix},
\qquad
A=\begin{pmatrix}
3/10&9/25\\
-3/10&11/100
\end{pmatrix}.                                             \tag{9.1}
\]
The kernel is \(K=I/2+H\).

### Legality

\[
\frac14I-AA^T=
\begin{pmatrix}
0.0304&0.0504\\
0.0504&0.1479
\end{pmatrix}.                                             \tag{9.2}
\]
Its leading principal minor is positive and its determinant is exactly
\[
\frac{489}{250000}>0.                                     \tag{9.3}
\]
Thus \(\|A\|<1/2\), so every eigenvalue of \(K\) lies strictly in \((0,1)\). The example is a legal real, half-filled, bipartite DPP.

For \(k=0\), the exact dual gap simplifies to
\[
\Delta_0
=8\sum_zw(z)
 \frac{\big(\|G_zb\|^2+4r_z^2\big)^2}
      {(1-4r_z^2)^2}.                                      \tag{9.4}
\]
The zero-correction certificate is
\[
\underline F''[0]=F''-\Delta_0.                           \tag{9.5}
\]

### Certified evaluation

Using 80-decimal interval arithmetic over all eight external words gave
\[
F''\in
[570.9797664033960690267784100974783,
 570.9797664033960690267784100974784],
\]
\[
\Delta_0\in
[580.9595573424739127154649339362824,
 580.9595573424739127154649339362825],
\]
therefore
\[
\boxed{
\underline F''[0]\in
[-9.979790939077843688686523838805,
 -9.979790939077843688686523838804].}                      \tag{9.6}
\]

> **DISPROVED.** “The zero-correction dual certificate is nonnegative for every legal half-filled bipartite DPP.”

The true curvature in this example is positive. What fails is the proposed simple certificate, not the main sign claim.

---

## 10. Projection-channel factorization: useful but not closed

The infinite sine kernel is a half-filled projection. Let \(Q\) be a projection with diagonal \(1/2\), write latent spins \(X_i=2\mathbf1_{i\in X}-1\), and pass them independently through
\[
\mathbb P_{t,x}(Y_i=y\mid X_i=\xi)
=\frac{1+y(t+x\xi)}2.                                     \tag{10.1}
\]
At \(t=0\), this is the BSC of correlation \(x\); its output DPP kernel is
\[
K=(1-x)I/2+xQ=I/2+x(Q-I/2).                               \tag{10.2}
\]
If the finite latent projection has rank exactly half the number of sites, then \(\sum_iX_i=0\). For any output word \(y\), set
\[
T(y)=\sum_i y_i,
\qquad R(y,X)=\sum_i y_iX_i.
\]
The four channel pair counts imply the exact factorization
\[
\mathbb P_{t,x}(y\mid X)
=C(t,x)\exp\{\alpha(t,x)T(y)+\beta(t,x)R(y,X)\},          \tag{10.3}
\]
where
\[
\alpha(t,x)=\frac14\log
\frac{(1+t)^2-x^2}{(1-t)^2-x^2},                           \tag{10.4}
\]
\[
\beta(t,x)=\frac14\log
\frac{(1+x)^2-t^2}{(1-x)^2-t^2}.                           \tag{10.5}
\]
Thus an asymmetric channel is exactly a symmetric BSC with a stronger effective correlation, followed by a uniform output field.

Let \(x_t=\tanh\beta(t,x)\). Then
\[
\alpha'(0,x)=\frac1{1-x^2},
\qquad x_t'(0)=0,
\qquad x_t''(0)=\frac{2x}{1-x^2}.                          \tag{10.6}
\]
If \(\mathcal F(\alpha,x)\) denotes the posterior functional after a uniform output field \(\alpha\) is applied to the symmetric BSC output at correlation \(x\), then
\[
\boxed{
F_{tt}(0,x)=
\frac{1}{(1-x^2)^2}\mathcal F_{\alpha\alpha}(0,x)
+\frac{2x}{1-x^2}F_x(0,x).}                               \tag{10.7}
\]
At \(t=0\), \(F\) is the Jeffreys divergence between the joint output law and the product of its center and external marginals. Adding further BSC noise is a common stochastic map on both measures, so the log-sum inequality gives
\[
F_x(0,x)\ge0.                                              \tag{10.8}
\]

> **PROVED.** Equations (10.3)–(10.8).

> **INCOMPLETE.** The field curvature \(\mathcal F_{\alpha\alpha}(0,x)\) can be negative, even for legal finite DPPs. Therefore (10.7) does not by itself prove the sign. It is also not volume-safe in its naive count form because the field score contains the total count. This route was not used to claim positivity.

This failed route is nevertheless informative: the desired sign is a balance between a potentially negative uniform-field curvature and a nonnegative noise-information derivative. It explains why a pure “positive Markov dissipation” import is insufficient.

---

## 11. Exploratory Fejér computations

These computations used the exact finite atom determinants and analytic \(h\)-derivatives
\[
\frac{w_h'}{w_h}=\operatorname{tr}G,
\qquad
\frac{w_h''}{w_h}=(\operatorname{tr}G)^2-\operatorname{tr}G^2,
\]
\[
q_h'=1+b^*G^2b,
\qquad
q_h''=-2b^*G^3b.                                          \tag{11.1}
\]
No independent-word surrogate was used.

### Pointwise at \(u=1\), \(c=0.95\)

| \(R\) | direct \(F''(1/2)\) | \(B_x\) | \(S_x\) |
|---:|---:|---:|---:|
| 1 | 8.4559342574 | 0.2816236383 | 0.1743106191 |
| 3 | 11.9939524638 | 1.9295142475 | 2.0644382164 |
| 5 | 17.0995201986 | 3.7774548147 | 5.3220653839 |
| 7 | 22.9489226744 | 5.5735664416 | 9.3753562328 |

The equality \(F''=8+B_x+S_x\) held to floating-point precision.

### Integrated finite Fejér curvature

| \(R\) | \(A_R''(0)\) | baseline \(4(1-(R+1)^{-2})\) | \(\int uB_{cu}du\) | \(\int uS_{cu}du\) |
|---:|---:|---:|---:|---:|
| 1 | 3.07202065 | 3.00000000 | 0.04528427 | 0.02673637 |
| 3 | 4.26745527 | 3.75000000 | 0.27742586 | 0.24002941 |
| 5 | 4.89689291 | 3.88888889 | 0.48805977 | 0.51994425 |
| 7 | 5.40932919 | 3.93750000 | 0.66146537 | 0.81036381 |

Quadrature used Gauss–Legendre nodes and ordinary double precision. These numbers are **exploratory**. They show that the residual \(S\) is not merely a tiny numerical cancellation in the first four odd Fejér volumes, but they do not control \(R\to\infty\).

---

## 12. Why the new tool is different from the old V14 formula

The existing V14 formula already gives an exact absolutely summable local kernel. Its obstruction is that several signed pieces must cancel, while conservative absolute values introduce powers such as \((1-c)^{-18}\).

The new construction changes the organization:

1. **Conditional rank-one geometry.** The two center-conditioned external laws lie on one exact rank-one DPP mixture path.
2. **One-sided duality.** A candidate correction gives a lower bound, and its error is a positive \(L^2\) norm.
3. **Explicit optimizer derivative.** Equation (3.15) replaces an unproved Poisson-solvability assumption by a concrete resolvent expression.
4. **Signed Doob localization.** Equations (5.7)–(5.18) remove global score traces and expose only connected edge/plaquette terms.
5. **Positive boundary extraction.** The whole endpoint contribution \(B_x\) has a proved sign.

What remains signed is exactly \(S_x\), not an unnamed remainder.

---

## 13. Transfer mechanism and its limitation

The source mechanisms are classical but all load-bearing identities were derived above.

### Quadratic dual / Stein control variate

The identity
\[
\sum d^2/p=\sup_f\{2\langle d,f\rangle-\langle p,f^2\rangle\}
\]
is the Pearson-Fisher quadratic dual. The correction \(k\) is a Stein-type control variate. Its hypotheses here are only positivity of the mixture atoms and differentiability. The new DPP ingredient is that the optimizer and its derivative are explicit rank-one resolvents.

### Doob transform

Multiplying a transported law by a positive harmonic weight normally produces a Doob \(h\)-transform. Here \(a_\theta=1+\theta r\) is transported because \(Dr=0\). This yields (5.7). What fails under transfer is positivity: the original transport rates are signed, so the transformed rates remain signed. Consequently the carré-du-champ in (5.10) is an identity, not a nonnegative dissipation.

### Statistical-mechanics field/noise split

Equation (10.3) separates an asymmetric local channel into a uniform field and a strengthened symmetric coupling. The transfer fails to close because the uniform-field curvature can be negative and its naive score carries total-count factors. The local rank-one/Doob tool avoids that hidden dimension.

No claim of literature novelty is made.

---

## 14. Dependency ledger

| Claim | Status | Dependencies |
|---|---|---|
| Conditional kernels (2.1), rank-one mixture (2.3) | **PROVED here** | determinant lemma only |
| Conditional-divergence identity (2.7) | **PROVED here** | Bayes formula |
| Fisher integral (3.2) | **PROVED here** | one-dimensional Bregman identity |
| Quadratic dual and exact gap (3.5)–(3.12) | **PROVED here** | completion of squares |
| Explicit optimizer derivative (3.15) | **PROVED here** | rank-one DPP path and inverse derivative |
| Signed Doob transport (5.7)–(5.8) | **PROVED here** | actual atom derivative and \(Dq=1\); the latter is also established in `SA03_S9_SIGNED_TRANSPORT.md` |
| Local edge/plaquette formula (5.18) | **PROVED here** | differentiation of (5.10) |
| Positive boundary decomposition (6.4)–(6.6) | **PROVED here**; the separated infinite residual is defined by the controlled combined limit | V14 volume theorem and bounded convergence for the endpoint term |
| Effective finite inequality (7.10) | **PROVED here from existing input** | Q1–Q5 effective remainder plus (3.11) |
| One-neighbour theorem | **PROVED here** | direct two-site differentiation |
| Zero-correction counterexample | **DISPROVED here** | exact legality check and interval enumeration |
| \(\Gamma(19/20)>0\) | **INCOMPLETE** | requires lower control of \(S(19/20)\) or a positive finite certificate beating (7.7) |
| Entropy-rate Hessian sign | **UNRESOLVED / OUT OF SCOPE** | no bridge from this local production functional to normalized block entropy was proved |

No other PRO assignment or its results were read or used.

---

## 15. Smallest remaining obstruction

The remaining problem is no longer “control all terms in V14” in an undifferentiated way. It is one of the following equivalent concrete tasks:

1. prove
   \[
   S(19/20)>-4-B(19/20);
   \]
2. find an explicit local correction \(k\) for which
   \[
   \underline A_{R,k}(19/20)>
   \varepsilon_R(19/20;m,d,M)
   \]
   at some finite certified parameter set;
3. sharpen the actual-law Fejér-to-sine remainder enough that an interval evaluation of the certificate becomes decisive.

The first is an analytic edge/plaquette inequality. The second is a finite interval-computation certificate. The third is a quantitative volume problem. None requires assuming positivity, a power-law asymptotic, an independent-word law, or an unproved Poisson solution.

---

## 16. Statement for a later independent reviewer

Please check the following four points independently:

1. the coefficients and moving endpoints in (4.5) and (6.1);
2. the adjoint calculation in (5.7) and the cancellation in (5.8);
3. the exact nonnegative dual gap (3.12), including its factor \(c_0(\alpha)=1/2\);
4. the use of the inherited effective remainder in passing from (7.9) to (7.10).

A successful check certifies a reusable one-sided sign tool and the decomposition \(\Gamma=4+B+S\). It does **not** certify the sign of \(\Gamma(19/20)\), because no lower bound on \(S(19/20)\) or decisive finite interval evaluation is supplied here.

---

## 17. Reproducibility record

The following calculations were actually performed:

* exact finite-word enumeration formulas for \(w,w',w'',q,q',q''\);
* direct checks of the rank-one change of variables and the identities \(J_h=\mathbb E\Gamma_\theta\) and (6.4) on finite legal DPPs;
* exploratory Fejér enumeration for \(R=1,3,5,7\) at \(c=0.95\);
* 80-decimal interval enumeration of the four-site counterexample in Section 9.

The following were **not** performed:

* a certified large-\(R\) evaluation of (7.10);
* a certified infinite-volume numerical value for \(\Gamma(19/20)\);
* any computation using an independent-word replacement;
* any entropy-rate derivative calculation.
