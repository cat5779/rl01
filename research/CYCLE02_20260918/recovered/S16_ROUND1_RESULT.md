# PRO03 RESULT — A square-root deletion/heat ledger and an \(n^{3/2}\) cancellation obstruction

**Scope:** `CORRECTED_LAW_ONLY`  
**Main target \(|W_n|=O(n)\):** **INCOMPLETE**  
**Comparison of \(W_n+C_n\):** **INCOMPLETE**  
**New local tool and exact weighted representation:** **PROVED**  
**New weighted obstruction theorem:** **PROVED**

This report uses only the packet for PRO03 and the already scoped SA04/S13 inputs named in the assignment. It does not use any result from the other PRO assignments or from an unreviewed SA05 claim. The previous SA04 audit is treated only as validation of the old input identities; it is not validation of the new arguments below.

The principal result is not an \(O(n)\) estimate for \(W_n\). It is a new common-input representation that puts deletion and clock variation in one formula, together with a rigorous obstruction theorem: under the actual \(w_l\) weights, the deletion contribution by itself is of order \(n^{3/2}\), with an explicit positive lower-limit constant. Consequently, any proof that \(W_n=O(n)\) must produce an order-\(n^{3/2}\) cancellation against the Bayes reverse-heat contribution. Separate estimates of the two nonnegative costs cannot succeed.

---

## 1. Fixed notation and inherited facts

Let \(n=2k\ge 4\), \(c=19/20\),
\[
 p=\frac{39}{40},\qquad q=\frac1{40},\qquad b=pq=\frac{39}{1600}.
\]
Let \(\Omega_l=\{S\subset[n]:|S|=l\}\), and let \(u_l\) be uniform on \(\Omega_l\). The original exchange generator is
\[
 (G_l f)(S)=\sum_{i\in S,\ j\notin S}\bigl[f(S-i+j)-f(S)\bigr]
           =l(n-l)L_l f(S),
\]
and \(P_l^s=e^{sG_l}\).

For the packet's maximal-overlap initial law \(q_l^{\max}\), put
\[
 \mu_l(s)=q_l^{\max}P_l^s,
 \qquad F_l(s)=D(\mu_l(s)\Vert u_l).
\]
The prescribed corrected clock is
\[
 s_l=-\frac{\log\theta_{\min(l,n-l)}}{2(n-1)}
 \qquad (2\le l\le n-2),
\]
with the packet's uniform endpoint convention, and
\[
 h(l)=F_l(s_l).
\]
For \(2\le l\le k\), write \(r=l-1\) and
\[
 \delta_l=s_l-s_r>0.
\]
At \(l=2\), the endpoint layer \(r=1\) is uniform and is handled by the existing convention; the new positive-density KL symmetrization below is stated for \(3\le l\le k\).

The prior SA04 input supplies the exact costs
\[
 A_l=F_l(s_l)-F_r(s_l)\ge0,
 \qquad
 E_l=F_r(s_r)-F_r(s_l)\ge0,
\]
and
\[
 d_l:=h(l)-h(l-1)=A_l-E_l.                         \tag{1.1}
\]
The Bayes reverse bridge realizing \(E_l\) is retained below.

The actual count weights supply
\[
 W_n=-2\sum_{l=1}^{k}w_l d_l
    =2\sum_{l=2}^{k}w_l(E_l-A_l),                  \tag{1.2}
\]
where
\[
 w_l=B_{l-1}-B_{l-2}\ge0,
 \qquad \sum_{l=1}^{k}w_l=B_{k-1}.                 \tag{1.3}
\]
The exact generating function is
\[
 \sum_m\frac{B_m}{n(n-1)}t^m
 =\phi(t)^{k-2}\psi_k(t),                           \tag{1.4}
\]
with
\[
 \phi(t)=b+(1-2b)t+bt^2,
 \qquad
 \psi_k(t)=\eta_k+(1-2\eta_k)t+\eta_k t^2,
\]
\[
 \eta_k=\frac{k-1+2b}{2(2k-1)}.
\]

For a positive density \(f\) relative to \(u_l\), write
\[
 \operatorname{Ent}_{u_l}(f)=\mathbb E_{u_l}[f\log f],
 \qquad
 \mathcal I_l(f)=-\langle G_lf,\log f\rangle_{u_l}.
\]
For the heat trajectory, abbreviate
\[
 f_{l,s}=\frac{d\mu_l(s)}{du_l},
 \qquad \mathcal I_l(s)=\mathcal I_l(f_{l,s})=-F_l'(s).
\]
The old proof establishes that \(s\mapsto\mathcal I_l(s)\) is nonincreasing for this random-transposition generator.

---

## 2. Source mechanism and the new construction

### 2.1 Transfer mechanism

The construction comes from three standard finite-state ideas:

1. **Adjoint channels and down-up walks.** A deletion channel between adjacent slices has an adjoint completion channel under the uniform reference measures. The product “completion after deletion” is a down-up Markov operator.
2. **Euler versus semigroup comparison.** In this model the down-up operator is not merely comparable to the exchange semigroup: it is exactly one forward Euler step of the original generator.
3. **Green–Kubo accounting.** Entropy loss over a clock interval is the time integral of entropy production. Placing the Euler identity and this integral on the same ledger produces a half-step correction and an explicit nonlinear defect.

The adjoint/down-up viewpoint is related to the general down-up-walk literature, including entropic-independence methods, but no external contraction theorem is imported here. Every identity used below is proved directly for the present slices.

### 2.2 The deletion density operator

Define the deletion kernel
\[
 D_l(S,T)=\frac1l\mathbf 1\{T\subset S,\ |T|=l-1\}.
\]
Its uniform-reference reverse channel is completion:
\[
 U_l(T,S)=\frac1{n-l+1}\mathbf 1\{T\subset S,\ |S|=l\}.
\]
They satisfy detailed balance
\[
 u_l(S)D_l(S,T)=u_{l-1}(T)U_l(T,S).                \tag{2.1}
\]
On densities, define
\[
 (K_lf)(T)=\frac1{n-l+1}\sum_{x\notin T}f(T+x).   \tag{2.2}
\]
Then \(K_lf\) is the density of \((u_lf)D_l\) relative to \(u_{l-1}\). Its Hilbert-space adjoint is
\[
 (K_l^*g)(S)=\frac1l\sum_{x\in S}g(S-x).          \tag{2.3}
\]

---

## 3. The square-root identity

### Theorem 3.1 — exact down-up Euler identity **[PROVED]**

For every \(2\le l\le n-1\),
\[
 \boxed{
 K_l^*K_l=I+\varepsilon_lG_l,
 \qquad
 \varepsilon_l=\frac1{l(n-l+1)}.
 }                                                   \tag{3.1}
\]

#### Proof

For \(S\in\Omega_l\),
\[
 (K_l^*K_lf)(S)
 =\frac1{l(n-l+1)}
   \sum_{x\in S}\sum_{y\notin S-x}f(S-x+y).
\]
The term \(y=x\) occurs once for each \(x\in S\), contributing \(lf(S)\). The other terms are precisely the ordered exchanges \(x\in S\), \(y\notin S\). Hence
\[
 l(n-l+1)K_l^*K_lf
 =lf+\sum_{x\in S,y\notin S}f(S-x+y).
\]
Since
\[
 G_lf=\sum_{x\in S,y\notin S}f(S-x+y)-l(n-l)f,
\]
the right side equals \(l(n-l+1)f+G_lf\). Division proves (3.1). \(\square\)

### Interpretation

The operator \(K_l\) behaves, at the level of its adjoint square, like a square root of a heat step of length \(\varepsilon_l\):
\[
 K_l^*K_l=I+\varepsilon_lG_l
 \quad\text{whereas}\quad
 (P_l^{\varepsilon_l/2})^*P_l^{\varepsilon_l/2}
 =e^{\varepsilon_lG_l}.
\]
This is an exact finite-\(n\) identity, not a diffusion approximation.

---

## 4. One common input for deletion and clock variation

The old decomposition (1.1) evaluates deletion at the terminal time \(s_l\) and the reverse bridge on layer \(l-1\). The next identity reroutes the same space-time rectangle so that both operations start from one density on layer \(l\).

The maximal-overlap laws and heat semigroups obey
\[
 K_lf_{l,s}=f_{l-1,s},
 \qquad
 K_lP_l^t=P_{l-1}^tK_l.                            \tag{4.1}
\]
For \(3\le l\le k\), set
\[
 f=f_{l,s_{l-1}}.
\]
Then
\[
 f_{l,s_l}=P_l^{\delta_l}f,
 \qquad
 f_{l-1,s_{l-1}}=K_lf.
\]
Therefore:

### Theorem 4.1 — same-input deletion/clock identity **[PROVED]**

For \(3\le l\le k\),
\[
 \boxed{
 d_l=
 \operatorname{Ent}_{u_l}(P_l^{\delta_l}f_{l,s_{l-1}})
 -\operatorname{Ent}_{u_{l-1}}(K_lf_{l,s_{l-1}}).
 }                                                   \tag{4.2}
\]
Equivalently, defining the same-time deletion loss
\[
 \mathsf A_l(t)=F_l(t)-F_{l-1}(t),                 \tag{4.3}
\]
one has the exact two-route identity
\[
 \boxed{
 d_l
 =\mathsf A_l(s_{l-1})-
   \int_{s_{l-1}}^{s_l}\mathcal I_l(t)\,dt
 =\mathsf A_l(s_l)-
   \int_{s_{l-1}}^{s_l}\mathcal I_{l-1}(t)\,dt.
 }                                                   \tag{4.4}
\]
The second integral is exactly the old Bayes reverse-heat cost \(E_l\).

#### Proof

The first equality in (4.2) follows from the two displayed identities above. Add and subtract \(F_l(s_{l-1})\), and use
\[
 F_l(s_{l-1})-F_l(s_l)
 =\int_{s_{l-1}}^{s_l}\mathcal I_l(t)\,dt
\]
to obtain the first route in (4.4). The second route is the old identity
\[
 d_l=[F_l(s_l)-F_{l-1}(s_l)]-[F_{l-1}(s_{l-1})-F_{l-1}(s_l)].
\]
\(\square\)

### Bayes bridge retained

Let
\[
 q^*=\mu_{l-1}(s_{l-1}),\qquad
 H=P_{l-1}^{\delta_l},\qquad
 p^*=q^*H=\mu_{l-1}(s_l).
\]
The positive reverse kernel is
\[
 \mathcal R_l(y,x)=\frac{q^*(x)H(x,y)}{p^*(y)}.     \tag{4.5}
\]
It satisfies \(p^*\mathcal R_l=q^*\), and by reversibility of \(H\),
\[
 \mathbb E_{y\sim p^*}
 D\bigl(\mathcal R_l(y,\cdot)\Vert H(y,\cdot)\bigr)
 =F_{l-1}(s_{l-1})-F_{l-1}(s_l)=E_l.              \tag{4.6}
\]
Thus (4.2) does not replace the Bayes bridge with an invalid negative-time semigroup. It is an alternative exact route around the same rectangle.

---

## 5. The deletion–heat commutator

The common representation also gives a monotonicity fact that was not needed in the old absolute-value proof.

### Lemma 5.1 — entropy-production contraction under deletion **[PROVED]**

For every positive density \(f\) on \(\Omega_l\),
\[
 \mathcal I_{l-1}(K_lf)\le \mathcal I_l(f).        \tag{5.1}
\]
Consequently,
\[
 \mathsf A_l'(t)
 =-\mathcal I_l(t)+\mathcal I_{l-1}(t)\le0,       \tag{5.2}
\]
and
\[
 \boxed{
 \mathsf A_l(s_{l-1})-\mathsf A_l(s_l)
 =\int_{s_{l-1}}^{s_l}
   [\mathcal I_l(t)-\mathcal I_{l-1}(t)]\,dt.
 }                                                   \tag{5.3}
\]

#### Proof

For \(\Psi(a,b)=(a-b)(\log a-\log b)\),
\[
 \mathcal I_l(f)=\frac12\sum_{i<j}
 \mathbb E_{u_l}\Psi(f(S),f((ij)S)).               \tag{5.4}
\]
The deletion density operator commutes with every permutation:
\[
 K_l(f\circ\sigma)=(K_lf)\circ\sigma.
\]
Condition on \(T\in\Omega_{l-1}\), choose a uniform completion \(S\supset T\), and apply joint convexity of \(\Psi\):
\[
 \Psi(K_lf(T),K_lf((ij)T))
 \le
 \mathbb E[\Psi(f(S),f((ij)S))\mid T].
\]
Averaging over uniform \(T\), the completion \(S\) is uniform on \(\Omega_l\). Summing over transpositions proves (5.1). Equation (5.2) follows by differentiating (4.3), and integration gives (5.3). \(\square\)

Equation (5.3) is a genuine deletion/heat commutator identity: the failure of the deletion cost to remain constant under common heat is exactly the integrated entropy-production gap between adjacent layers.

---

## 6. Exact KL symmetrization and the half-step ledger

Fix \(l\) and a positive density \(f\) on \(\Omega_l\). Put \(g=K_lf\). On incidence pairs \(T\subset S\), define the reference edge law
\[
 R(S,T)=u_l(S)D_l(S,T)=u_{l-1}(T)U_l(T,S).         \tag{6.1}
\]
Define two edge laws by their densities relative to \(R\):
\[
 P(S,T)=R(S,T)f(S),
 \qquad
 Q(S,T)=R(S,T)g(T).                                \tag{6.2}
\]
The two laws have the same \(T\)-marginal, namely \(u_{l-1}g\). Their forward and reverse conditional KL costs are
\[
 A(f)=D(P\Vert Q),
 \qquad
 \overline A(f)=D(Q\Vert P).                      \tag{6.3}
\]
The first is exactly the deletion loss:
\[
 A(f)=\operatorname{Ent}_{u_l}(f)
      -\operatorname{Ent}_{u_{l-1}}(K_lf).         \tag{6.4}
\]

### Theorem 6.1 — Jeffreys/entropy-production identity **[PROVED]**

For every positive density \(f\),
\[
 \boxed{
 A(f)+\overline A(f)=\varepsilon_l\mathcal I_l(f).
 }                                                   \tag{6.5}
\]
Hence, with the signed skew
\[
 \Gamma_l(f)=\frac12[A(f)-\overline A(f)],         \tag{6.6}
\]
\[
 \boxed{
 A(f)=\frac{\varepsilon_l}{2}\mathcal I_l(f)
      +\Gamma_l(f).
 }                                                   \tag{6.7}
\]
Moreover,
\[
 |\Gamma_l(f)|\le\frac{\varepsilon_l}{2}\mathcal I_l(f). \tag{6.8}
\]

#### Proof

The Jeffreys divergence is
\[
 A+\overline A
 =\mathbb E_R[(f(S)-g(T))(\log f(S)-\log g(T))].   \tag{6.9}
\]
Conditioning on \(T\), one has \(\mathbb E_R[f(S)\mid T]=g(T)\). Therefore the term involving \(\log g(T)\) vanishes. The remaining term is
\[
 \langle f-K_l^*K_lf,\log f\rangle_{u_l}.
\]
By (3.1), this equals
\[
 -\varepsilon_l\langle G_lf,\log f\rangle_{u_l}
 =\varepsilon_l\mathcal I_l(f).
\]
This proves (6.5) and (6.7). Since both KL divergences in (6.3) are nonnegative, (6.8) follows. \(\square\)

### The skew is a cubic conditional defect

Under \(Q\), let
\[
 U=\frac{f(S)}{g(T)}.
\]
Then \(\mathbb E_Q[U\mid T]=1\), and
\[
 \Gamma_l(f)=\mathbb E_Q\gamma(U),                \tag{6.10}
\]
where
\[
 \gamma(u)=\frac12\bigl[(u+1)\log u-2(u-1)\bigr]. \tag{6.11}
\]
Near \(u=1\),
\[
 \gamma(1+x)=\frac{x^3}{12}+O(x^4).               \tag{6.12}
\]
Thus the first nonlinear obstruction left after the half-step matching is a signed cubic fluctuation of the true completion likelihood ratio. It is not an unnamed remainder: (6.10) is an explicit expectation under the reverse-completion edge law.

### Theorem 6.2 — exact half-step/Green–Kubo ledger **[PROVED]**

For \(3\le l\le k\), let
\[
 f^-=f_{l,s_{l-1}},
 \qquad
 Q_l^{\rm time}=
 \int_{s_{l-1}}^{s_l}
 [\mathcal I_l(s_{l-1})-\mathcal I_l(t)]\,dt\ge0. \tag{6.13}
\]
Then
\[
 \boxed{
 d_l=
 \left(\frac{\varepsilon_l}{2}-\delta_l\right)
 \mathcal I_l(s_{l-1})
 +\Gamma_l(f^-)+Q_l^{\rm time}.
 }                                                   \tag{6.14}
\]
Consequently the complete moving-weight response has the exact representation
\[
 \boxed{
 \begin{aligned}
 W_n={}&-2w_2h(2)\\
 &+2\sum_{l=3}^{k}w_l
 \left[
 \left(\delta_l-\frac{\varepsilon_l}{2}\right)
 \mathcal I_l(s_{l-1})
 -\Gamma_l(f_{l,s_{l-1}})-Q_l^{\rm time}
 \right].
 \end{aligned}
 }                                                   \tag{6.15}
\]
The first term is the genuine \(2\to1\) endpoint contribution; no correction clock is assigned to layer \(1\).

#### Proof

By the first route in (4.4),
\[
 d_l=A(f^-)-\int_{s_{l-1}}^{s_l}\mathcal I_l(t)\,dt.
\]
Insert (6.7), and write
\[
 \int_{s_{l-1}}^{s_l}\mathcal I_l(t)\,dt
 =\delta_l\mathcal I_l(s_{l-1})-Q_l^{\rm time}.
\]
This proves (6.14). Multiply by \(-2w_l\), sum over \(3\le l\le k\), and add the exact endpoint term \(-2w_2d_2=-2w_2h(2)\) to obtain (6.15). \(\square\)

### Terminal-time version retaining the Bayes cost

Let
\[
 \Lambda_l(t)=\mathcal I_l(t)-\mathcal I_{l-1}(t)\ge0,
\]
\[
 R_l^{\rm time}=
 \int_{s_{l-1}}^{s_l}
 [\mathcal I_{l-1}(t)-\mathcal I_{l-1}(s_l)]\,dt\ge0.
\]
Applying (6.7) at \(s_l\) and using the Bayes identity (4.6) gives
\[
 \boxed{
 d_l=
 \left(\frac{\varepsilon_l}{2}-\delta_l\right)
 \mathcal I_{l-1}(s_l)
 +\frac{\varepsilon_l}{2}\Lambda_l(s_l)
 +\Gamma_l(f_{l,s_l})-R_l^{\rm time}.
 }                                                   \tag{6.16}
\]
This is the same cancellation written directly against the reverse-heat cost. Equations (6.14) and (6.16) are the new tool requested in P1.

---

## 7. A quadratic certificate and its limitation

For a density \(f=1+g\), define
\[
 \chi_l^2(f)=\|g\|_{L^2(u_l)}^2.
\]

### Theorem 7.1 — matched half-step certificate in \(\chi^2\) **[PROVED]**

For every density \(f=1+g\),
\[
 \chi_{l-1}^2(K_lf)=
 \langle g,(I+\varepsilon_lG_l)g\rangle_{u_l},     \tag{7.1}
\]
whereas
\[
 \chi_l^2(P_l^{\varepsilon_l/2}f)=
 \langle g,e^{\varepsilon_lG_l}g\rangle_{u_l}.    \tag{7.2}
\]
Therefore
\[
 \boxed{
 0\le
 \chi_l^2(P_l^{\varepsilon_l/2}f)
 -\chi_{l-1}^2(K_lf)
 \le
 \frac{\varepsilon_l^2}{2}\|G_lg\|_{L^2(u_l)}^2.
 }                                                   \tag{7.3}
\]
More generally, if \(2\delta\le\varepsilon_l\), then
\[
 \chi_l^2(P_l^\delta f)\ge\chi_{l-1}^2(K_lf).     \tag{7.4}
\]

#### Proof

Equation (7.1) is (3.1). Self-adjointness of \(G_l\) gives (7.2). On an eigenvector with \(-G_l\)-eigenvalue \(\lambda\ge0\), the difference multiplier is
\[
 e^{-\varepsilon_l\lambda}-(1-\varepsilon_l\lambda)\ge0,
\]
and
\[
 e^{-x}-1+x\le\frac{x^2}{2}\qquad(x\ge0).
\]
This proves (7.3). If \(a=2\delta/\varepsilon_l\le1\), then
\[
 e^{-a x}\ge1-a x\ge1-x,
\]
which proves (7.4). \(\square\)

### Limitation **[INCOMPLETE for KL]**

The operator order in (7.3) does not by itself imply the analogous ordering for relative entropy. The exact KL defect is governed by the cubic skew (6.10) and the entropy-production curvature in (6.13). No sign for their sum is proved here.

As an exploratory warning only, a direct floating-point calculation for the point-mass density on the central slice \((n,l)=(8,4)\) gave
\[
 \operatorname{Ent}_{u_4}(P_4^{1/40}f)
 -\operatorname{Ent}_{u_3}(K_4f)\approx-0.0706449.
\]
This was not interval-certified and is not used as a formal counterexample. Its role was only to prevent an unjustified promotion of the \(\chi^2\) comparison to KL.

---

## 8. The actual central clock is asymptotically the half-step clock

This section proves a local normalization check at the exact middle layer. It does not control the nonlinear defects in (6.14).

The SA04 coefficient identity gives, for \(2\le m\le k\),
\[
 \theta_m=c^2\frac{k(k-1)}{m(m-1)}
 \frac{\rho_{k-2}(k-m)}{\rho_k(k-m)},              \tag{8.1}
\]
where \(\rho_j(r)\) is the probability that a \(j\)-step walk with increment probabilities \((b,1-2b,b)\) at \((-1,0,1)\) is at \(r\).

### Lemma 8.1 — fixed-site local expansion **[PROVED]**

For fixed \(r\in\{0,1\}\), as \(j\to\infty\),
\[
 \rho_j(r)=\frac1{\sqrt{4\pi bj}}
 \left[1+\frac{\beta_b-r^2/(4b)}{j}+O_b(j^{-2})\right],             \tag{8.2}
\]
where \(\beta_b\) is a constant depending only on \(b\). Consequently,
\[
 \frac{\rho_j(1)}{\rho_j(0)}
 =1-\frac1{4bj}+O_b(j^{-2}).                         \tag{8.3}
\]

#### Proof

Fourier inversion gives
\[
 \rho_j(r)=\frac1{2\pi}\int_{-\pi}^{\pi}
 [1-4b\sin^2(t/2)]^j e^{-irt}\,dt.                 \tag{8.4}
\]
Choose a fixed \(\tau>0\). On \(\tau\le |t|\le\pi\), the bracket has modulus at most some \(\zeta_b<1\), so this part is \(O(\zeta_b^j)\). On \(|t|\le\tau\), analyticity gives
\[
 \log[1-4b\sin^2(t/2)]
 =-bt^2+\kappa_b t^4+\lambda_b t^6+O_b(t^8),
\]
and, for fixed \(r\),
\[
 \cos(rt)=1-\frac{r^2t^2}{2}+\frac{r^4t^4}{24}+O_r(t^6).
\]
Split the remaining integral at \(|t|=j^{-2/5}\). Between \(j^{-2/5}\) and \(\tau\), the real part of the logarithm is at most \(-b t^2/2\) for small enough \(\tau\), hence the contribution is \(O(e^{-c_bj^{1/5}})\). On \(|t|\le j^{-2/5}\), put \(t=y/\sqrt j\). Then
\[
 [1-4b\sin^2(t/2)]^j
 =e^{-by^2}
 \left[1+\frac{\kappa_b y^4}{j}
 +O_b\!\left(\frac{1+y^8}{j^2}\right)\right]
\]
under a Gaussian dominating function, and
\[
 \cos(ry/\sqrt j)
 =1-\frac{r^2y^2}{2j}
 +O_r\!\left(\frac{1+y^4}{j^2}\right).
\]
Termwise Gaussian integration is therefore justified, with an \(O_b(j^{-2})\) relative remainder. Since
\[
 \frac{\int_{\mathbb R}y^2e^{-by^2}dy}
      {\int_{\mathbb R}e^{-by^2}dy}=\frac1{2b},
\]
the cosine contributes \(-r^2/(4b)\) to the coefficient of \(j^{-1}\); the quartic characteristic-function term contributes a constant \(\beta_b\) independent of fixed \(r\). This proves (8.2). Division of the cases \(r=1\) and \(r=0\) gives (8.3). \(\square\)

### Proposition 8.2 — center half-step matching **[PROVED]**

At \(l=k\),
\[
 \boxed{
 \delta_k=s_k-s_{k-1}
 =\frac1{2k^2}+O_b(k^{-3})
 =\frac{\varepsilon_k}{2}+O_b(k^{-3}).
 }                                                   \tag{8.5}
\]
Equivalently,
\[
 \frac{2\delta_k}{\varepsilon_k}=1+O_b(k^{-1}).    \tag{8.6}
\]

#### Proof

From (8.1),
\[
 \frac{\theta_k}{\theta_{k-1}}
 =\frac{k-2}{k}
 \frac{\rho_k(1)/\rho_k(0)}
      {\rho_{k-2}(1)/\rho_{k-2}(0)}.               \tag{8.7}
\]
By (8.3), the second factor is \(1+O_b(k^{-2})\). Hence
\[
 -\log\frac{\theta_k}{\theta_{k-1}}
 =\log\frac{k}{k-2}+O_b(k^{-2})
 =\frac2k+O_b(k^{-2}).                              \tag{8.8}
\]
Since \(n=2k\),
\[
 \delta_k=
 \frac{-\log(\theta_k/\theta_{k-1})}{2(2k-1)}
 =\frac1{2k^2}+O_b(k^{-3}).
\]
Finally,
\[
 \frac{\varepsilon_k}{2}
 =\frac1{2k(k+1)}
 =\frac1{2k^2}+O(k^{-3}).
\]
\(\square\)

Using the inherited bounds \(F_k(0)=O(n)\), \(s_{k-1}\asymp n^{-1}\), and monotonicity of entropy production gives \(\mathcal I_k(s_{k-1})=O(n^2)\). Thus the deterministic clock-mismatch term at the single central layer obeys
\[
 \left|\frac{\varepsilon_k}{2}-\delta_k\right|
 \mathcal I_k(s_{k-1})=O(n^{-1}).                  \tag{8.9}
\]
This does **not** show \(d_k=o(1)\), because \(\Gamma_k\) and \(Q_k^{\rm time}\) can still be order one.

---

## 9. A finite-\(n\) pair witness for the deletion cost

The next theorem is the key obstruction result. It shows that deletion is not a small perturbation on the expanding central band.

For adjacent cyclic sites, define
\[
 b_n=|P_{0,1}|^2-\frac1{4(n-1)}
 =\frac1{n^2\sin^2(\pi/n)}-\frac1{4(n-1)}.         \tag{9.1}
\]
For \(l\le k\), put
\[
 \alpha_{n,l}=\frac{l(l-1)}{k(k-1)}.
\]
The inherited exact degree-two identity states that under \(\mu_l(t)\),
\[
 \Pr(0,1\in S)-\frac{l(l-1)}{n(n-1)}
 =-\alpha_{n,l}e^{-2(n-1)t}b_n.                   \tag{9.2}
\]

### Theorem 9.1 — explicit deletion-cost lower bound **[PROVED]**

For every \(2\le l\le k\) and every \(t>0\),
\[
 \boxed{
 \mathsf A_l(t)
 \ge\frac12
 \left[
 \frac{2n(n-1)}{l(n-l+1)}
 \alpha_{n,l}e^{-2(n-1)t}b_n
 \right]^2.
 }                                                   \tag{9.3}
\]
In particular,
\[
 A_l=\mathsf A_l(s_l)
 \ge\frac12
 \left[
 \frac{2n(n-1)}{l(n-l+1)}
 \alpha_{n,l}\theta_{n,l}b_n
 \right]^2.                                        \tag{9.4}
\]
The early-time deletion cost in (6.14) satisfies the analogous formula with \(\theta_{n,l-1}\) in place of \(\theta_{n,l}\).

#### Proof

Let \(S\sim\mu_l(t)\), delete a uniformly chosen \(X\in S\), and put \(T=S-X\). Conditional on \(T\), let \(K_T\) be the true law of the deleted point \(X\); let \(U_T\) be uniform on \(T^c\). Then
\[
 \mathsf A_l(t)=\mathbb E_T D(K_T\Vert U_T).        \tag{9.5}
\]
Use the conditional statistic
\[
 \varphi_T(x)=\mathbf 1\{x-1\in T\}
              +\mathbf 1\{x+1\in T\},
 \qquad 0\le\varphi_T\le2.                       \tag{9.6}
\]
Let \(e_j(t)\) denote the probability that a fixed adjacent edge is fully occupied under \(\mu_j(t)\). Under the true deletion joint law,
\[
 \mathbb E\varphi_T(X)=\frac{2n e_l(t)}{l},        \tag{9.7}
\]
because summing occupied degrees counts each occupied adjacent edge twice. Under the uniform completion reference,
\[
 \mathbb E_{T,U_T}\varphi_T(X)
 =\frac{2(l-1)-2n e_{l-1}(t)}{n-l+1}.              \tag{9.8}
\]
Same-time deletion coherence gives
\[
 e_{l-1}(t)=\frac{l-2}{l}e_l(t),                   \tag{9.9}
\]
since a fixed occupied pair survives deletion with probability \((l-2)/l\). Subtracting (9.8) from (9.7),
\[
 \mathbb E_T\bigl[
 \mathbb E_{K_T}\varphi_T-
 \mathbb E_{U_T}\varphi_T\bigr]
 =\frac{2n(n-1)}{l(n-l+1)}
 \left[e_l(t)-\frac{l(l-1)}{n(n-1)}\right].       \tag{9.10}
\]
By (9.2), the absolute value of the right side is the bracketed quantity in (9.3).

For each \(T\), the range bound in (9.6) gives
\[
 \bigl|\mathbb E_{K_T}\varphi_T-
       \mathbb E_{U_T}\varphi_T\bigr|
 \le2\,\|K_T-U_T\|_{\rm TV}.
\]
Pinsker's inequality, with natural logarithms, gives
\[
 D(K_T\Vert U_T)\ge2\|K_T-U_T\|_{\rm TV}^2
 \ge\frac12
 \bigl(\mathbb E_{K_T}\varphi_T-
       \mathbb E_{U_T}\varphi_T\bigr)^2.
\]
For completeness, the needed finite-alphabet Pinsker bound follows by mapping the alphabet to a set attaining total variation, applying log-sum/data processing to obtain two Bernoulli laws, and using
\[
 x\log\frac{x}{y}+(1-x)\log\frac{1-x}{1-y}
 \ge2(x-y)^2.
\]
For fixed \(y\), the difference between the left side and \(2(x-y)^2\) vanishes with zero first derivative at \(x=y\), while its second derivative is
\(1/[x(1-x)]-4\ge0\).

Average and apply Jensen to the square. Equation (9.10) proves (9.3). At \(t=s_l\), \(e^{-2(n-1)s_l}=\theta_{n,l}\), yielding (9.4). \(\square\)

### Corollary 9.2 — order-one deletion cost on an expanding central band **[PROVED, conditional only on the audited S13 central asymptotic]**

Let
\[
 \mathcal B_n=\{l:|l-k|\le n^{2/3}\}.
\]
The audited S13 input gives, uniformly on \(\mathcal B_n\),
\[
 \theta_{n,l}\to c^2.
\]
Also \(\alpha_{n,l}\to1\), \(b_n\to1/\pi^2\), and
\[
 \frac{2n(n-1)}{l(n-l+1)}\to8.
\]
Therefore
\[
 \boxed{
 \liminf_{n\to\infty}
 \inf_{\substack{2\le l\le k\\|l-k|\le n^{2/3}}}
 A_l
 \ge a_c:=\frac{32c^4}{\pi^4}.
 }                                                   \tag{9.11}
\]
For \(c=19/20\),
\[
 a_c=0.267574614682543\ldots.                       \tag{9.12}
\]

Thus neither \(A_l\) nor its early-time counterpart tends to zero in the central band. Any smallness of \(d_l=A_l-E_l\) must be cancellation with the reverse-heat cost.

---

## 10. Actual \(w_l\)-weighted obstruction

Define the two nonnegative weighted components
\[
 \mathcal D_n=2\sum_{l=2}^{k}w_lA_l,
 \qquad
 \mathcal R_n=2\sum_{l=2}^{k}w_lE_l.               \tag{10.1}
\]
Then
\[
 W_n=\mathcal R_n-\mathcal D_n.                    \tag{10.2}
\]

### Lemma 10.1 — local central limit for the actual \(B\) weight **[PROVED]**

With \(b=39/1600\),
\[
 \boxed{
 B_{k-1}\sim\frac{n^{3/2}}{\sqrt{2\pi b}}.
 }                                                   \tag{10.3}
\]

#### Proof

Center the coefficient law in (1.4). Let \(X_1,\dots,X_{k-2}\) be independent with
\[
 \Pr(X_i=\pm1)=b,
 \qquad \Pr(X_i=0)=1-2b,
\]
and let \(Y\) be independent with the same form and parameter \(\eta_k\). Then
\[
 \frac{B_{k-1}}{n(n-1)}
 =\Pr\left(\sum_{i=1}^{k-2}X_i+Y=0\right).         \tag{10.4}
\]
The variance is
\[
 V_n=2b(k-2)+2\eta_k=(n-4)b+2\eta_k=nb+O(1).       \tag{10.5}
\]
Fourier inversion gives
\[
 \Pr(S_n=0)=\frac1{2\pi}\int_{-\pi}^{\pi}
 [1-4b\sin^2(t/2)]^{k-2}
 [1-4\eta_k\sin^2(t/2)]\,dt.                      \tag{10.6}
\]
On \(|t|\le n^{-2/5}\), logarithmic expansion gives
\[
 [1-4b\sin^2(t/2)]^{k-2}
 [1-4\eta_k\sin^2(t/2)]
 =\exp[-V_nt^2/2+O(nt^4)].                         \tag{10.7}
\]
After \(u=\sqrt{V_n}t\), dominated convergence yields the Gaussian integral. On the complement, \(\sin(|t|/2)\ge |t|/\pi\) and \(b>0\), so the integrand is bounded by \(\exp(-c_bn t^2)\); its contribution is \(o(n^{-1/2})\). Therefore
\[
 \Pr(S_n=0)=\frac{1+o(1)}{\sqrt{2\pi V_n}}
 =\frac{1+o(1)}{\sqrt{2\pi bn}}.
\]
Multiplying by \(n(n-1)\) proves (10.3). \(\square\)

### Theorem 10.2 — the deletion component is \(\Theta(n^{3/2})\) **[PROVED]**

For the specified corrected law,
\[
 \boxed{
 \liminf_{n\to\infty,\ n\ {
m even}}
 \frac{\mathcal D_n}{n^{3/2}}
 \ge
 \frac{64c^4}{\pi^4\sqrt{2\pi b}}.
 }                                                   \tag{10.8}
\]
At \(c=19/20\), \(b=39/1600\), the right side is
\[
 1.36745378603952\ldots.                            \tag{10.9}
\]
Together with the old uniform upper bound on \(A_l\), this implies
\[
 \boxed{\mathcal D_n=\Theta(n^{3/2}).}              \tag{10.10}
\]

#### Proof

Let \(R_n=\lfloor n^{2/3}\rfloor\). Since \(w_l\ge0\), Corollary 9.2 gives
\[
 \mathcal D_n
 \ge2(a_c-o(1))
 \sum_{l=k-R_n+1}^{k}w_l.                           \tag{10.11}
\]
By telescoping,
\[
 \sum_{l=k-R_n+1}^{k}w_l
 =B_{k-1}-B_{k-R_n-1}.                              \tag{10.12}
\]
The packet's Hoeffding bound gives
\[
 B_{k-R_n-1}
 \le n(n-1)\exp\left[-\frac{2R_n^2}{n-2}\right]
 =o(n^{3/2}).                                       \tag{10.13}
\]
Combining (10.3), (10.11), and (10.13),
\[
 \liminf\frac{\mathcal D_n}{n^{3/2}}
 \ge\frac{2a_c}{\sqrt{2\pi b}}
 =\frac{64c^4}{\pi^4\sqrt{2\pi b}}.
\]
For the upper bound, the old estimate \(A_l\le A_*\) and (1.3) give
\[
 \mathcal D_n\le2A_*B_{k-1}=O(n^{3/2}).
\]
\(\square\)

### Exact consequence for the main target **[PROVED as an implication]**

Any estimate
\[
 W_n=O(n)
\]
would force
\[
 \boxed{
 \mathcal R_n=\mathcal D_n+O(n),
 }                                                   \tag{10.14}
\]
so the weighted Bayes reverse-heat contribution must reproduce the deletion contribution through relative error \(O(n^{-1/2})\) at the aggregate scale. It is not enough to prove \(A_l=O(1)\) and \(E_l=O(1)\) separately; both weighted sums are allowed to be order \(n^{3/2}\).

Equivalently, from (6.15), an \(O(n)\) theorem requires an actual-weight estimate on the combined correction
\[
 -2w_2h(2)+2\sum_{l=3}^{k}w_l
 \left[
 \left(\delta_l-\frac{\varepsilon_l}{2}\right)
 \mathcal I_l(s_{l-1})
 -\Gamma_l(f_{l,s_{l-1}})-Q_l^{\rm time}
 \right].                                           \tag{10.15}
\]
This is the smallest remaining mathematical object exposed by the new tool. Asymptotically the endpoint term is negligible: for \(n\ge6\), \(w_2\le B_1\), and (7.6) of the inherited SA04 input with \(R=k-2\) gives
\[
 w_2\le n(n-1)\exp\!\left[-\frac{2(k-2)^2}{n-2}\right].
\]
Since \(h(2)\le A_*\), it is not the central obstruction.

---

## 11. What is paid, what is not, and tail accounting

### P1 — common local representation **[PROVED]**

Paid completely by:

- the exact channel identity \(K_l^*K_l=I+\varepsilon_lG_l\);
- the same-input formula (4.2);
- the two-route rectangle (4.4), which explicitly retains the Bayes reverse bridge;
- the Jeffreys split (6.5)–(6.7);
- the all-layer weighted response (6.15).

No clock was changed. The clock is exactly the coefficient-defined \(s_l\) in the assignment.

### P2 — central regularity or weighted cancellation **[PARTLY PROVED / main cancellation INCOMPLETE]**

Proved:

- exact \(\chi^2\) half-step comparison for every slice;
- center clock matching \(\delta_k=\varepsilon_k/2+O(n^{-3})\);
- an expanding-band order-one lower bound for the actual deletion KL;
- the actual weighted deletion theorem \(\mathcal D_n=\Theta(n^{3/2})\).

Not proved:

- \(|d_l|\le K/\sqrt n\) on a central window;
- \(|d_l|\le K(|l-k|+1)/n\);
- a direct \(O(n)\) bound for the weighted correction (10.15);
- a sign or asymptotic leading term for \(W_n\).

### P3 — every layer, tails, and \(W_n+C_n\) **[PARTLY PROVED / final comparison INCOMPLETE]**

For the new deletion-component theorem, all tails are paid:

- the lower bound discards only nonnegative tail terms;
- the omitted lower-half weight is exponentially small by (10.13);
- the upper bound uses the complete mass \(\sum w_l=B_{k-1}\).

For \(W_n\) itself, the old all-layer \(O(n^{3/2})\) bound remains valid. The new work does not improve that final exponent, because no \(O(n)\) control of (10.15) has been proved.

The information does not suffice to compare \(W_n+C_n\). The packet proves only
\[
 \liminf C_n/n>0,
\]
not an upper bound \(C_n=O(n)\). Moreover, \(W_n\) still has unknown sign and may contain an uncancelled \(n^{3/2}\) component. No conclusion about \(W_n+C_n\), the true output law, or a Toeplitz entropy rate follows.

---

## 12. Boundary and failure checks

### 12.1 Endpoint layers **[PROVED handled by scope]**

The KL symmetrization requires positive densities and is used for \(3\le l\le k\). The \(2\to1\) edge remains governed by the packet's uniform endpoint convention, with \(E_2=0\), \(A_2=h(2)\). Its contribution is included in the exact weighted identity but is irrelevant to the central asymptotic lower bound.

### 12.2 Upper half of the lattice **[PROVED inherited symmetry]**

Particle-hole symmetry gives \(h(n-l)=h(l)\) and \(d_{n-l+1}=-d_l\). The actual \(B_m\) summation has already been reduced exactly to the lower-half weights \(w_l\); no upper-half layers are omitted.

### 12.3 Positive forward heat is still invalid **[DISPROVED by inherited \(n=6\) example]**

The new half-step identity is an operator/accounting statement. It does not assert that deletion followed by a nonnegative amount of heat reaches the adjacent corrected target law. The packet's valid \(n=6\) counterexample continues to rule out that universal forward-clock construction.

### 12.4 Universal KL square-root dominance **[INCOMPLETE; exploratory evidence against]**

The \(\chi^2\) operator inequality is proved. The corresponding KL inequality is not. The signed cubic term \(\Gamma_l\) is the precise place where quadratic operator order can fail to transfer.

### 12.5 No corrected-law-to-DPP transfer **[NOT CLAIMED]**

Every theorem in this report concerns only the specified corrected law. No equality, approximation, stochastic order, or entropy comparison with the true DPP output is established.

---

## 13. Calculations actually performed

### 13.1 Rigorous symbolic calculations used in proofs

The following were carried out algebraically and appear in the proofs:

1. Exact computation of \(K_l^*K_l\).
2. Exact edge-law KL symmetrization and derivation of (6.5).
3. Exact conditional adjacent-neighbor statistic leading to (9.10).
4. Fourier local limit derivation for \(B_{k-1}\).
5. Fixed-site Fourier expansion for the central clock ratio.
6. Numerical evaluation only of explicit closed constants:
   \[
   a_c=\frac{32(19/20)^4}{\pi^4}
   =0.267574614682543\ldots,
   \]
   \[
   \frac{64(19/20)^4}
   {\pi^4\sqrt{2\pi(39/1600)}}
   =1.36745378603952\ldots.
   \]

### 13.2 Exploratory floating-point calculations, not used as proof

A direct state-space computation was run for several small even \(n\), using determinant evaluation for \(q_l^{\max}\), sparse construction of \(G_l\), and numerical matrix-exponential action. Representative central-layer values were:

| \(n\) | central \(d_k\) | \(A_k\) | \(E_k\) | \(W_n\) |
|---:|---:|---:|---:|---:|
| 12 | 0.407053 | 0.412943 | 0.005890 | -38.06284 |
| 14 | 0.469806 | 0.479961 | 0.010156 | -59.07205 |
| 16 | 0.523642 | 0.539415 | 0.015774 | -84.95586 |
| 18 | 0.569583 | 0.592351 | 0.022768 | -115.56587 |

These are ordinary floating-point diagnostics, not interval-certified values. They support neither a theorem about the asymptotic sign nor a fitted growth law. Their only research role was to show that a pointwise small-\(d_l\) conjecture is not visible at these sizes and to motivate the joint ledger.

A separate coefficient calculation showed slow convergence of the center clock to its limiting multiplier; this is consistent with, but not a proof of, Proposition 8.2.

---

## 14. Exact improvement over the previous result

The old result proved
\[
 |d_l|<600,
 \qquad
 |W_n|=O(n^{3/2}),
\]
by separate upper bounds on deletion and reverse-heat costs.

The present report adds four items not contained in that estimate:

1. **An exact square-root channel identity:**
   \[
   K_l^*K_l=I+\frac{G_l}{l(n-l+1)}.
   \]
2. **A common-input, all-weight cancellation formula:** equation (6.15), in which deletion and actual clock variation are compared before taking absolute values.
3. **An explicit nonlinear correction potential:** the signed conditional-likelihood skew \(\Gamma_l\) plus the Green–Kubo curvature \(Q_l^{\rm time}\).
4. **A sharp scale obstruction for separate estimates:**
   \[
   \mathcal D_n=2\sum w_lA_l=\Theta(n^{3/2}),
   \]
   with the explicit lower-limit constant (10.8).

Thus the old \(O(n^{3/2})\) exponent for \(W_n\) is not improved, but the reason is now mathematically localized: an \(O(n)\) theorem must control the weighted cubic/curvature correction in (10.15), or equivalently prove \(\mathcal R_n-\mathcal D_n=O(n)\).

---

## 15. Smallest remaining obstruction

The smallest remaining obstruction is the following concrete statement.

> **Open correction estimate.** Prove, disprove, or asymptotically evaluate
> \[
> -2w_2h(2)+2\sum_{l=3}^{k}w_l
> \left[
> \left(\delta_l-\frac{\varepsilon_l}{2}\right)
> \mathcal I_l(s_{l-1})
> -\Gamma_l(f_{l,s_{l-1}})-Q_l^{\rm time}
> \right].
> \]
> An \(O(n)\) bound would imply \(W_n=O(n)\). A nonzero \(n^{3/2}\) limit would identify the leading moving-weight response.

The difficult part is not the leading quadratic channel behavior: that is exactly matched by (3.1) and controlled in \(\chi^2\). The difficult part is the aggregate of:

- the signed cubic completion-likelihood skew \(\Gamma_l\);
- the entropy-production curvature over one clock interval;
- the small but layer-dependent mismatch between \(\delta_l\) and \(\varepsilon_l/2\).

Any future proof should target these three terms together under the actual \(w_l\) moments. Bounding them one at a time by constants returns to the old \(n^{3/2}\) loss.

---

## 16. Dependency ledger

### Inherited and scoped inputs

- **D1.** Corrected-law definitions, prescribed clock, actual count weights, and the statement that only a positive lower limit for \(C_n/n\) is known: `inputs/TASK.md`.
- **D2.** Deletion coherence, semigroup intertwining, Bayes reverse bridge, the exact identity \(d_l=A_l-E_l\), the exact \(w_l\) representation of \(W_n\), and the finite-\(n\) tail bound: `inputs/SA04_REPORT.md`, as scoped by `SOL_REVIEW.md`.
- **D3.** Exact adjacent degree-two pair mode and uniform central asymptotic \(\theta_{n,l}\to c^2\) on \(|l-k|\le n^{2/3}\): `inputs/sources/S13_PROOF.md`, within the prior scoped audit.

### New self-contained results in this report

- **N1.** The Euler identity (3.1).
- **N2.** Entropy-production contraction under deletion (5.1).
- **N3.** Jeffreys identity and half-step ledger (6.5), (6.14), (6.15).
- **N4.** \(\chi^2\) square-root certificate (7.3).
- **N5.** Center clock half-step asymptotic (8.5).
- **N6.** Finite-\(n\) pair-witness deletion lower bound (9.3).
- **N7.** Actual \(B_{k-1}\) local central limit and weighted deletion theorem (10.3), (10.8).

### External theorem dependence

No load-bearing external theorem is used without proof. The finite-alphabet Pinsker inequality used in Section 9 is reduced there to an elementary binary convexity calculation. The down-up/adjoint terminology is contextual; the required operator and entropy statements are derived directly.

For context only, the use of deletion/down-up channels in entropy contraction is part of the modern entropic-independence literature; see N. Anari, V. Jain, F. Koehler, H. T. Pham, and T.-D. Vuong, *Entropic Independence I*, arXiv:2106.04105. No result from that paper is used in a proof here.

---

## 17. Statement for a later independent reviewer

A fresh reviewer should independently check the following five load-bearing points:

1. For density deletion \(K_l\), verify
   \[
   K_l^*K_l=I+G_l/[l(n-l+1)].
   \]
2. On the incidence edge law, verify
   \[
   D(P\Vert Q)+D(Q\Vert P)=\varepsilon_l\mathcal I_l(f).
   \]
3. Check the signs in the exact response formula (6.15), including the use of the earlier-time density \(f_{l,s_{l-1}}\).
4. Verify the adjacent-neighbor conditional statistic and the factor
   \[
   \frac{2n(n-1)}{l(n-l+1)}
   \]
   in (9.10).
5. Verify that the actual center coefficient obeys
   \[
   B_{k-1}\sim n^{3/2}/\sqrt{2\pi b},
   \]
   and hence that the constant in (10.8) is
   \[
   64c^4/[\pi^4\sqrt{2\pi b}].
   \]

The main \(W_n\) scale and sign remain open. The new theorem is the exact joint ledger plus the proof that the deletion side alone has order \(n^{3/2}\) under the actual weights.
