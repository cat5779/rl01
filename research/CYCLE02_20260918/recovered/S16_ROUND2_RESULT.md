# PRO03 ROUND 2 RESULT — central clock crossover, radial cancellation, and the latent-information obstruction

**Scope:** `CORRECTED_LAW_ONLY`  
**Full sign/order of the corrected-law response \(W_n\):** **INCOMPLETE**  
**Negative order-\(n^{3/2}\) claim:** **INCOMPLETE**  
**Strong \(O(n)\) cancellation claim:** **INCOMPLETE**  
**Exact new channel and information decompositions:** **PROVED**  
**Central fixed-latent cancellation under the actual weights:** **PROVED**  
**Finite-size interpretation “\(E_k\ll A_k\) is already asymptotic”:** **DISPROVED**

This report continues the first-round PRO03 work but does not treat that work as independently certified. The load-bearing operator identity is rederived below, and every new conclusion is separated from inherited inputs. The only computational material consulted from the companion computation branch was the C02/SA04 central-scale packet. No SA05 conclusion and no result from either of the other PRO assignments is used.

The main result of this round is an obstruction theorem rather than a proof of either proposed global behavior. It establishes that the tractable birth--death contribution associated with a *fixed* latent \(k\)-set has no order-\(n^{3/2}\) term under the actual weights. The complete corrected-law response admits the exact decomposition
\[
 \boxed{
 W_n=W_n^{\mathrm{rad}}
   +2\sum_{l=2}^{k}w_l\bigl[J_l(s_l)-J_{l-1}(s_{l-1})\bigr],
 }
 \tag{0.1}
\]
where \(J_l(s)=I(A;S_{l,s})\) is mutual information between the projection-DPP latent set \(A\) and the heated \(l\)-set. The radial term satisfies
\[
 \boxed{
 W_n^{\mathrm{rad}}=O_{b,c}\!\left(n\log^{5/2}n\right)
 =o(n^{3/2}).
 }
 \tag{0.2}
\]
Consequently, a nonzero \(n^{3/2}\) limit, positive or negative, can only come from the weighted one-sided layer/clock increment of the latent mutual information. In particular, a negative order-\(n^{3/2}\) response would require that this increment be negative on a set carrying a nonzero fraction of the actual \(w_l\)-mass.

A second result explains why the C02 values through \(n=20\) do not decide that question. If
\[
 a_{n,l}:=\frac{s_l-s_{l-1}}{\varepsilon_l},
 \qquad \varepsilon_l=\frac1{l(n-l+1)},
\]
then \(a_{n,l}=1/2\) is the down--up half-step singled out by the first-round identity. At the exact center,
\[
 \boxed{
 \frac{2(s_k-s_{k-1})}{\varepsilon_k}
 =1+\frac{\frac52-\frac1{4b}}{k}+O_b(k^{-2})
 =1-\frac{7.756410256\ldots}{k}+O(k^{-2}).
 }
 \tag{0.3}
\]
For \(n=20\), however, the exact coefficient clock gives
\[
 \frac{2(s_k-s_{k-1})}{\varepsilon_k}
 =0.0688864090903\ldots,
 \tag{0.4}
\]
so the reverse-heat interval in that computation is only about \(6.9\%\) of the matched half-step. The small reported \(E_k\) is therefore a genuine finite-\(n\) fact, but it is not evidence that \(E_k/A_k\) stays small asymptotically.

---

## 1. Fixed law and notation

Let
\[
 n=2k\ge4,
 \qquad c=\frac{19}{20},
 \qquad p=\frac{39}{40},
 \qquad q=\frac1{40},
 \qquad b=pq=\frac{39}{1600}.
\]
For \(0\le l\le n\), let \(\Omega_l\) be the \(l\)-subsets of \([n]\), and let \(u_l\) be uniform on \(\Omega_l\). On \(\Omega_l\),
\[
 (G_lf)(S)=\sum_{i\in S,\,j\notin S}
 [f(S-i+j)-f(S)],
 \qquad P_l^s=e^{sG_l}.
 \tag{1.1}
\]
The prescribed corrected clock is
\[
 s_l=-\frac{\log\theta_l}{2(n-1)},
 \qquad 2\le l\le k,
 \tag{1.2}
\]
with particle--hole reflection above \(k\) and the packet's uniform endpoint convention. No alternative clock is introduced.

Let \(A\) be the random rank-\(k\) projection-DPP set from the first \(k\) Fourier columns. Conditional on \(A\), choose a uniform \(l\)-subset of \(A\), then run (1.1) for time \(s\). Denote the conditional law by
\[
 \mu_{l,s}^{A}.
\]
Its mixture over \(A\) is precisely the corrected-law heat trajectory
\[
 \mu_{l,s}=q_l^{\max}P_l^s.
\]
Put
\[
 F_l(s)=D(\mu_{l,s}\Vert u_l),
 \qquad h(l)=F_l(s_l).
 \tag{1.3}
\]
For \(2\le l\le k\),
\[
 d_l=h(l)-h(l-1),
 \qquad
 W_n=-2\sum_{l=2}^{k}w_ld_l,
 \tag{1.4}
\]
where
\[
 w_l=B_{l-1}-B_{l-2}\ge0,
 \qquad B_{-1}=0,
 \qquad \sum_{l=1}^{k}w_l=B_{k-1}.
 \tag{1.5}
\]
The actual coefficient law is
\[
 \sum_m\frac{B_m}{n(n-1)}t^m
 =\phi(t)^{k-2}\psi_k(t),
 \tag{1.6}
\]
with
\[
 \phi(t)=b+(1-2b)t+bt^2,
 \qquad
 \psi_k(t)=\eta_k+(1-2\eta_k)t+\eta_kt^2,
 \qquad
 \eta_k=\frac{k-1+2b}{2(2k-1)}.
 \tag{1.7}
\]

The old all-layer estimate \(|d_l|<600\) and hence \(|W_n|=O(n^{3/2})\) remain available. They are not improved merely by the pointwise C02 observations.

---

## 2. Rechecking the down--up identity and exposing the exact Poisson parameter

For a density \(f\) on \(\Omega_l\), define density deletion
\[
 (K_lf)(T)=\frac1{n-l+1}\sum_{x\notin T}f(T+x),
 \qquad T\in\Omega_{l-1}.
 \tag{2.1}
\]
Its uniform-reference adjoint is
\[
 (K_l^*g)(S)=\frac1l\sum_{x\in S}g(S-x).
 \tag{2.2}
\]

### Theorem 2.1 — exact down--up generator identity **[PROVED]**

For every \(2\le l\le n-1\),
\[
 \boxed{
 K_l^*K_l=I+\varepsilon_lG_l,
 \qquad
 \varepsilon_l=\frac1{l(n-l+1)}.
 }
 \tag{2.3}
\]

#### Proof

For \(S\in\Omega_l\),
\[
 (K_l^*K_lf)(S)
 =\frac1{l(n-l+1)}
   \sum_{x\in S}\sum_{y\notin S-x}f(S-x+y).
\]
The terms \(y=x\) contribute \(lf(S)\). Every remaining term is one ordered exchange \(x\in S,y\notin S\). Hence
\[
 l(n-l+1)K_l^*K_lf
 =lf+\sum_{x\in S,y\notin S}f(S-x+y)
 =l(n-l+1)f+G_lf.
\]
Divide by \(l(n-l+1)\). \(\square\)

Let
\[
 M_l:=K_l^*K_l.
\]
For \(\delta_l=s_l-s_{l-1}\), (2.3) gives the exact identity
\[
 \boxed{
 P_l^{\delta_l}
 =e^{a_{n,l}(M_l-I)},
 \qquad
 a_{n,l}:=\frac{\delta_l}{\varepsilon_l}.
 }
 \tag{2.4}
\]
Thus the relevant clock question is not merely whether \(\delta_l\to0\). It is whether the dimensionless Poisson down--up time \(a_{n,l}\) approaches \(1/2\).

For the same-input density
\[
 f_l^-:=\frac{d\mu_{l,s_{l-1}}}{du_l},
\]
the inherited intertwining gives
\[
 d_l
 =\operatorname{Ent}_{u_l}
   \bigl(e^{a_{n,l}(M_l-I)}f_l^-\bigr)
 -\operatorname{Ent}_{u_{l-1}}(K_lf_l^-).
 \tag{2.5}
\]
This is a direct rederivation of the first-round common-input formula.

Define the matched half-step defect
\[
 \Delta_l^{\#}(f)
 :=\operatorname{Ent}_{u_l}
   \bigl(e^{(M_l-I)/2}f\bigr)
 -\operatorname{Ent}_{u_{l-1}}(K_lf).
 \tag{2.6}
\]
For a positive density \(f\), put
\[
 \mathcal J_{l,f}(a)
 :=-\frac{d}{da}
   \operatorname{Ent}_{u_l}
   \bigl(e^{a(M_l-I)}f\bigr)\ge0.
 \tag{2.7}
\]
The nonnegativity is the standard entropy dissipation identity for the reversible Markov kernel \(M_l\), and follows directly by symmetrizing
\(
-\langle(M_l-I)g,\log g\rangle_{u_l}
\).

### Corollary 2.2 — clock-defect/matched-defect split **[PROVED]**

For every \(3\le l\le k\),
\[
 \boxed{
 d_l
 =\Delta_l^{\#}(f_l^-)
 +\int_{a_{n,l}}^{1/2}\mathcal J_{l,f_l^-}(a)\,da.
 }
 \tag{2.8}
\]
The oriented integral convention makes (2.8) valid whether \(a_{n,l}\) is below or above \(1/2\).

#### Proof

Subtract and add the entropy at Poisson time \(1/2\) in (2.5), then integrate (2.7). \(\square\)

Equation (2.8) is useful for Round 2 because it cleanly separates two possible causes of a positive central \(d_l\):

1. a finite-\(n\) clock deficit \(a_{n,l}<1/2\), whose contribution is automatically nonnegative; and
2. the genuinely nonlinear matched defect \(\Delta_l^{\#}\), whose sign is not fixed by the \(L^2\) square-root identity.

No KL ordering is inferred from the first-round \(\chi^2\) comparison.

---

## 3. The prescribed central clock approaches the half-step very slowly

Let \(X\) have
\[
 \Pr(X=1)=\Pr(X=-1)=b,
 \qquad
 \Pr(X=0)=1-2b,
\]
and write
\[
 \rho_j(r)=\Pr(X_1+\cdots+X_j=r).
\]
Direct coefficient extraction from the packet's definition of \(\theta_l\) gives, for \(l=k-r\),
\[
 \boxed{
 \theta_{k-r}
 =c^2\frac{k(k-1)}{(k-r)(k-r-1)}
   \frac{\rho_{k-2}(r)}{\rho_k(r)}.
 }
 \tag{3.1}
\]
This algebraic identity is independently checked here; it is not being accepted merely from a status label.

### Lemma 3.1 — moderate local estimate **[PROVED]**

For every fixed \(D<\infty\), uniformly for integers
\(
|r|\le D\sqrt{j\log j}
\),
\[
 \log\rho_j(r)
 =-\frac12\log(4\pi bj)
  -\frac{r^2}{4bj}
  +O_{b,D}\!\left(\frac{1+\log^2j}{j}\right).
 \tag{3.2}
\]
For fixed \(r\), the sharper expansion
\[
 \rho_j(r)
 =\frac1{\sqrt{4\pi bj}}
  \left[
   1+\frac{\beta_b-r^2/(4b)}{j}
   +O_b(j^{-2})
  \right]
 \tag{3.3}
\]
holds, where \(\beta_b\) is independent of fixed \(r\). In particular,
\[
 \frac{\rho_j(1)}{\rho_j(0)}
 =1-\frac1{4bj}+O_b(j^{-2}).
 \tag{3.4}
\]

#### Proof

Set
\[
 M(z)=\mathbb E e^{zX}=1-2b+2b\cosh z,
 \qquad \Lambda(z)=\log M(z).
\]
For \(x=r/j\), let \(\eta\) be the real solution of
\(
\Lambda'(\eta)=x
\). In the stated range, \(x=o(1)\), and Taylor expansion gives
\[
 \eta=\frac{x}{2b}+O_b(x^3),
 \quad
 \Lambda''(\eta)=2b+O_b(x^2),
 \quad
 x\eta-\Lambda(\eta)
 =\frac{x^2}{4b}+O_b(x^4).
 \tag{3.5}
\]
Exponential tilting and Fourier inversion give
\[
 \rho_j(r)
 =e^{-j[x\eta-\Lambda(\eta)]}
  \frac1{2\pi}\int_{-\pi}^{\pi}
  \exp\!\left\{j[\Lambda(\eta+it)-\Lambda(\eta)-itx]\right\}dt.
 \tag{3.6}
\]
On \(|t|\le j^{-2/5}\), expansion at the saddle gives
\[
 \Lambda(\eta+it)-\Lambda(\eta)-itx
 =-\frac{\Lambda''(\eta)t^2}{2}
  -i\frac{\Lambda'''(\eta)t^3}{6}
  +O_b(t^4).
\]
After \(t=y/\sqrt j\), the odd cubic term has zero first Gaussian integral, while the quartic and squared-cubic terms contribute a relative \(O_b(j^{-1})\) error, uniformly for the present \(\eta\). On the complement, aperiodicity and analyticity give
\[
 \left|rac{M(\eta+it)}{M(\eta)}e^{-itx}\right|
 \le e^{-c_b t^2}
\]
for small \(|t|\), and a strictly smaller-than-one bound away from zero. Therefore
\[
 \rho_j(r)
 =\frac{e^{-j[x\eta-\Lambda(\eta)]}}
        {\sqrt{2\pi j\Lambda''(\eta)}}
   \left[1+O_{b,D}(j^{-1})\right].
 \tag{3.7}
\]
Substituting (3.5), with
\(
jx^4=r^4/j^3=O_D(\log^2j/j)
\), proves (3.2).

For fixed \(r\), one may instead expand the untilted Fourier integral to two further powers after \(t=y/\sqrt j\). The characteristic-function quartic term contributes the same coefficient \(\beta_b\) for every fixed \(r\); the factor \(e^{-irt}\) contributes \(-r^2/(4b)\) at order \(j^{-1}\). This proves (3.3), and division of the \(r=1\) and \(r=0\) cases gives (3.4). \(\square\)

Define
\[
 \zeta_l:=e^{-ns_l}=\theta_l^{k/(2k-1)}.
 \tag{3.8}
\]
The quantity \(\zeta_l\) is the macroscopic retention parameter of the fixed-latent birth--death chain below.

### Proposition 3.2 — central and moderate-window clock asymptotics **[PROVED]**

At the exact center,
\[
 \boxed{
 \frac{2(s_k-s_{k-1})}{\varepsilon_k}
 =1+\frac{\frac52-\frac1{4b}}{k}+O_b(k^{-2}).
 }
 \tag{3.9}
\]
For the present \(b=39/1600\),
\[
 \frac52-\frac1{4b}
 =-7.756410256410\ldots.
 \tag{3.10}
\]
Moreover, uniformly for
\[
 0\le r\le D\sqrt{k\log k},
\]
\[
 \boxed{
 \log\frac{\zeta_{k-r}}{\zeta_k}
 =\frac{r}{k}
  +O_{b,D}\!\left(
    \frac{r^2}{k^2}+\frac{\log^2k}{k}
   \right),
 \qquad
 \zeta_k=c+O_b(k^{-1}).
 }
 \tag{3.11}
\]

#### Proof

At \(r=0,1\), (3.1) gives
\[
 \frac{\theta_k}{\theta_{k-1}}
 =\frac{k-2}{k}
  \frac{\rho_k(1)/\rho_k(0)}
       {\rho_{k-2}(1)/\rho_{k-2}(0)}.
 \tag{3.12}
\]
Use (3.4) to obtain
\[
 -\log\frac{\theta_k}{\theta_{k-1}}
 =\frac2k+\frac{2-1/(2b)}{k^2}+O_b(k^{-3}).
 \tag{3.13}
\]
Since
\[
 \frac{2(s_k-s_{k-1})}{\varepsilon_k}
 =\frac{k(k+1)}{2k-1}
  \left[-\log\frac{\theta_k}{\theta_{k-1}}\right],
\]
expanding the prefactor proves (3.9).

For the window statement, subtract the \(r=0\) version of (3.1) from the general one. Lemma 3.1 gives
\[
 \log\frac{\theta_{k-r}}{\theta_k}
 =\log\frac{k(k-1)}{(k-r)(k-r-1)}
  +O_{b,D}\!\left(
    \frac{r^2}{k^2}+\frac{\log^2k}{k}
   \right)
\]
and the logarithm of the rational prefactor is
\(
2r/k+O((r^2+r)/k^2)
\). Multiplication by \(k/(2k-1)\) proves the first part of (3.11). The case \(r=0\) of (3.1) and (3.3) gives \(\theta_k=c^2[1+O_b(k^{-1})]\), hence \(\zeta_k=c+O_b(k^{-1})\). \(\square\)

### Consequence for the C02 range **[PROVED algebraically; numerical values exploratory]**

The exact coefficient calculation gives the following dimensionless clock ratios:

| \(n\) | \(2(s_k-s_{k-1})/\varepsilon_k\) |
|---:|---:|
| 20 | 0.0688864091 |
| 40 | 0.2277315913 |
| 60 | 0.4084811596 |
| 100 | 0.6784484232 |
| 200 | 0.8913646808 |
| 500 | 0.9651553569 |
| 1000 | 0.9835903094 |

The table was evaluated in binary64 from exact integer coefficient sums. It is not an interval certificate, and no proof below depends on its decimals. Formula (3.9), not the table, proves the limiting half-step statement.

The C02 observation \(E_k\ll A_k\) through \(n=20\) is therefore not being made at a clock close to the asymptotic half-step. The premise that those sizes already test the matched regime is false.

---

## 4. Fixed-latent radial mechanics and an exact mutual-information split

Fix one \(k\)-set \(A\). For \(S\in\Omega_l\), define
\[
 R=|S\setminus A|.
\]
Conditional on \(A\), the initial law is the shell \(R=0\), and the complete-graph exchange chain remains uniform within every shell. The radial chain has rates
\[
 \lambda_R=(l-R)(k-R),
 \qquad
 \mu_R=R(k-l+R).
 \tag{4.1}
\]
Its stationary law is
\[
 \pi_l(R)
 =\frac{\binom{k}{l-R}\binom{k}{R}}{\binom{2k}{l}}.
 \tag{4.2}
\]
Let \(p_{l,s}\) be its law at time \(s\), started at zero, and define the fixed-latent radial entropy
\[
 \mathfrak F_l(s):=D(p_{l,s}\Vert\pi_l).
 \tag{4.3}
\]
This equals \(D(\mu_{l,s}^{A}\Vert u_l)\) and is independent of the particular \(A\).

Under the joint law in which \(A\) has its projection-DPP distribution and \(S\mid A\sim\mu_{l,s}^{A}\), define
\[
 J_l(s):=I(A;S).
 \tag{4.4}
\]

### Theorem 4.1 — exact radial/information decomposition **[PROVED]**

For every \(l\le k\) and every \(s\ge0\),
\[
 \boxed{
 F_l(s)=\mathfrak F_l(s)-J_l(s).
 }
 \tag{4.5}
\]
Consequently, with the packet's own clocks,
\[
 \boxed{
 d_l=d_l^{\mathrm{rad}}-\Delta J_l,
 }
 \tag{4.6}
\]
where
\[
 d_l^{\mathrm{rad}}
 :=\mathfrak F_l(s_l)-\mathfrak F_{l-1}(s_{l-1}),
 \qquad
 \Delta J_l:=J_l(s_l)-J_{l-1}(s_{l-1}).
 \tag{4.7}
\]
For the endpoint convention one may set \(s_1=0\); then
\(
\mathfrak F_1(0)=J_1(0)=\log2
\), so (4.5)--(4.7) still give \(h(1)=0\).

#### Proof

Relative to the product reference \(\Pr(A)u_l(S)\), the joint relative entropy is
\[
 \mathbb E_A D(\mu_{l,s}^{A}\Vert u_l)
 =\mathfrak F_l(s).
\]
The KL chain rule, first marginalizing \(S\), gives
\[
 \mathfrak F_l(s)
 =D(\mu_{l,s}\Vert u_l)+I(A;S)
 =F_l(s)+J_l(s).
\]
This is (4.5); subtract adjacent own-clock identities to obtain (4.6). \(\square\)

The old deletion and reverse-heat costs also split exactly. Define
\[
 A_l^{\mathrm{rad}}
 =\mathfrak F_l(s_l)-\mathfrak F_{l-1}(s_l),
\]
\[
 E_l^{\mathrm{rad}}
 =\mathfrak F_{l-1}(s_{l-1})-
  \mathfrak F_{l-1}(s_l).
\]
Then
\[
 A_l
 =A_l^{\mathrm{rad}}
  -[J_l(s_l)-J_{l-1}(s_l)],
 \tag{4.8}
\]
\[
 E_l
 =E_l^{\mathrm{rad}}
  -[J_{l-1}(s_{l-1})-J_{l-1}(s_l)].
 \tag{4.9}
\]
Both square-bracketed terms are nonnegative: the first by data processing under deletion, and the second by data processing under additional heat. Their *difference* has no predetermined sign:
\[
 \Delta J_l
 =[J_l(s_l)-J_{l-1}(s_l)]
 -[J_{l-1}(s_{l-1})-J_{l-1}(s_l)].
 \tag{4.10}
\]
Thus a positive corrected-law \(d_l\) can be caused either by a positive radial increment or by a negative information commutator \(\Delta J_l\).

This is a narrower obstruction than the original \(A_l-E_l\) decomposition. The large, universal radial part is now explicit and will be shown to cancel below; the unresolved term is the competition between one additional observation of the latent DPP set and the information destroyed by the corresponding extra clock interval.

---

## 5. A continuum potential for the fixed-latent chain

Write
\[
 l=\lambda k,
 \qquad 0<\lambda\le1,
 \qquad
 \zeta=e^{-ns}.
\]
Let
\[
 H(x)=-x\log x-(1-x)\log(1-x)
\]
with the usual endpoint convention, and define
\[
 \boxed{
 \Phi(\lambda,\zeta)
 =2H(\lambda/2)
  -H\!\left(\frac{\lambda(1+\zeta)}2\right)
  -H\!\left(\frac{\lambda(1-\zeta)}2\right).
 }
 \tag{5.1}
\]

### Lemma 5.1 — exact first two moment bounds **[PROVED]**

For the radial chain (4.1),
\[
 \mathbb E R_s
 =\frac l2(1-e^{-ns})
 =\frac{\lambda k}{2}(1-\zeta),
 \tag{5.2}
\]
and
\[
 \operatorname{Var}(R_s)\le\frac k2.
 \tag{5.3}
\]

#### Proof

From (4.1),
\[
 \lambda_R-\mu_R=lk-nR.
\]
Therefore the mean \(m\) solves \(m'=lk-nm\), with \(m(0)=0\), proving (5.2).

For a birth--death chain,
\[
 \frac d{ds}\operatorname{Var}(R_s)
 =-2n\operatorname{Var}(R_s)
  +\mathbb E(\lambda_{R_s}+\mu_{R_s}).
\]
Each of the two rates is at most \(k^2\), so the forcing is at most \(2k^2\). Starting from variance zero and using \(n=2k\) gives (5.3). \(\square\)

### Theorem 5.2 — radial entropy potential **[PROVED]**

Fix compact intervals
\[
 \lambda\in[\lambda_0,1],
 \qquad
 \zeta\in[\zeta_0,\zeta_1]\subset(0,1).
\]
Uniformly over such \(\lambda,\zeta\), with integer \(l=\lambda k\) and \(s=-n^{-1}\log\zeta\),
\[
 \boxed{
 \mathfrak F_l(s)
 =k\Phi(\lambda,\zeta)+O_{\lambda_0,\zeta_0,\zeta_1}(\log k).
 }
 \tag{5.4}
\]

#### Proof

For \(R=xk\), Stirling's bounds applied to (4.2) give, uniformly for every admissible integer \(R\),
\[
 -\log\pi_l(R)
 =k\mathcal I_\lambda(x)+O(\log k),
 \tag{5.5}
\]
where
\[
 \mathcal I_\lambda(x)
 =2H(\lambda/2)-H(\lambda-x)-H(x).
 \tag{5.6}
\]
Since the radial state space has at most \(k+1\) points,
\[
 0\le H(p_{l,s})\le\log(k+1).
\]
Consequently
\[
 \mathfrak F_l(s)
 =k\,\mathbb E\mathcal I_\lambda(R_s/k)+O(\log k).
 \tag{5.7}
\]

By (5.2), the mean of \(R_s/k\) is
\[
 x_*=\frac\lambda2(1-\zeta).
\]
The compact assumptions put \(x_*\) and \(\lambda-x_*\) a fixed positive distance from zero. On a fixed neighborhood of \(x_*\), \(\mathcal I_\lambda\) has uniformly bounded second derivative. Equation (5.3), Taylor's theorem, and \(\mathbb E(R_s/k-x_*)=0\) give an \(O(k^{-1})\) expectation error on that neighborhood.

Outside it, Chebyshev and (5.3) give probability \(O(k^{-1})\). The function \(\mathcal I_\lambda\) is uniformly bounded on its full compact domain, and Cauchy--Schwarz controls the omitted linear term by \(O(k^{-1})\). Thus
\[
 \mathbb E\mathcal I_\lambda(R_s/k)
 =\mathcal I_\lambda(x_*)+O(k^{-1}).
\]
Substituting \(x_*\) into (5.6) gives exactly (5.1), proving (5.4). \(\square\)

At the central corrected limit \((\lambda,\zeta)=(1,c)\), let
\[
 p=\frac{1+c}{2},
 \qquad q=\frac{1-c}{2}.
\]
Then
\[
 \partial_\lambda\Phi(1,c)
 =c\log\frac{1+c}{1-c},
 \tag{5.8}
\]
\[
 \partial_\zeta\Phi(1,c)
 =\log\frac{1+c}{1-c}.
 \tag{5.9}
\]
Therefore
\[
 \boxed{
 -\partial_\lambda\Phi(1,c)
 +c\,\partial_\zeta\Phi(1,c)=0.
 }
 \tag{5.10}
\]
This is the central cancellation mechanism. Moving one layer below \(k\) changes \(\lambda\) by \(-1/k\), while the prescribed clock changes \(\zeta\) by \(+c/k\) to first order. The two directional derivatives cancel exactly.

The two first-order directional contributions in the continuum potential have the common coefficient
\[
 \boxed{
 L_c:=c\log\frac{1+c}{1-c}
 =\frac{19}{20}\log39
 =3.480383563823\ldots.
 }
 \tag{5.11}
\]
Equation (5.11) is a proved derivative of the limiting potential.  The present error term in Theorem 5.2 does **not** by itself prove pointwise convergence of the individual finite-\(n\) costs \(A_k^{\rm rad}\) and \(E_k^{\rm rad}\) to \(L_c\); the later numerical table only diagnoses that expected crossover.

---

## 6. Expanding-window radial cancellation

For own-clock radial entropies, abbreviate
\[
 \mathfrak h_l:=\mathfrak F_l(s_l).
\]

### Theorem 6.1 — central block bound **[PROVED]**

There are constants \(C,k_0\), depending only on the fixed \(b,c\), such that for every \(k\ge k_0\) and every integer
\[
 0\le r\le 2\sqrt{2k\log(2k)},
\]
\[
 \boxed{
 |\mathfrak h_k-\mathfrak h_{k-r}|
 \le C\left(\frac{r^2}{k}+\log^2k\right).
 }
 \tag{6.1}
\]
Equivalently,
\[
 \left|
  \sum_{j=0}^{r-1}d_{k-j}^{\mathrm{rad}}
 \right|
 \le C\left(\frac{r^2}{k}+\log^2k\right).
 \tag{6.2}
\]
In particular, for any \(r_k\to\infty\) with
\(
\log^2k=o(r_k),
\quad r_k\le2\sqrt{2k\log(2k)},
\)
\[
 \frac1{r_k}
 \sum_{j=0}^{r_k-1}d_{k-j}^{\mathrm{rad}}
 \longrightarrow0.
 \tag{6.3}
\]

#### Proof

Set
\[
 \lambda_r=1-r/k,
 \qquad \zeta_r=\zeta_{k-r}.
\]
By Proposition 3.2,
\[
 \log(\zeta_r/\zeta_0)
 =r/k+O\!\left(r^2/k^2+\log^2k/k\right),
 \tag{6.4}
\]
and \(\zeta_0=c+O(k^{-1})\). Hence
\[
 \lambda_r-1=-r/k,
\]
\[
 \zeta_r-\zeta_0
 =cr/k+O\!\left(r^2/k^2+\log^2k/k\right).
 \tag{6.5}
\]
Taylor-expand \(\Phi\) on a fixed compact neighborhood of \((1,c)\). The first-order \(r/k\) terms vanish by (5.10), while (6.5), the quadratic remainder, and \(\zeta_0-c=O(k^{-1})\) give
\[
 |\Phi(1,\zeta_0)-\Phi(\lambda_r,\zeta_r)|
 \le C\left(
  \frac{r^2}{k^2}+\frac{\log^2k}{k}
 \right).
 \tag{6.6}
\]
Apply Theorem 5.2 at the two endpoints. Its two \(O(\log k)\) errors are absorbed by \(O(\log^2k)\), and multiplication of (6.6) by \(k\) proves (6.1). Telescoping proves (6.2), and division by \(r_k\) proves (6.3). \(\square\)

This result is stronger than a pointwise statement at \(l=k\): it controls every central prefix sum on an expanding window at least as wide as the actual \(\sqrt n\) weight scale, with an additional \(\sqrt{\log n}\) margin for tail payment.

It does **not** assert a sign for the individual radial increments. It proves that an order-one radial increment cannot persist with one sign across a positive fraction of the central window.

---

## 7. Actual-weight accounting for the radial contribution

Define
\[
 W_n^{\mathrm{rad}}
 :=-2\sum_{l=2}^{k}w_ld_l^{\mathrm{rad}}.
 \tag{7.1}
\]
We first record coefficient smoothness at the actual weights.

### Lemma 7.1 — first and second differences of \(B_m\) **[PROVED]**

Uniformly in \(m\),
\[
 |B_m-B_{m-1}|\le C_b n,
 \tag{7.2}
\]
\[
 |B_m-2B_{m-1}+B_{m-2}|\le C_b\sqrt n.
 \tag{7.3}
\]

#### Proof

After centering the coefficient in (1.6), Fourier inversion has integrand
\[
 [1-4b\sin^2(t/2)]^{k-2}
 [1-4\eta_k\sin^2(t/2)].
\]
The second factor has modulus at most one, while for \(|t|\le\pi\),
\[
 [1-4b\sin^2(t/2)]^{k-2}
 \le e^{-c_bnt^2}.
\]
One coefficient difference inserts the factor \(|1-e^{it}|\le|t|\), and two differences insert \(|1-e^{it}|^2\le t^2\). Therefore the normalized coefficient bounds are respectively
\[
 O_b\!\left(\int_{-\pi}^{\pi}|t|e^{-c_bnt^2}dt\right)
 =O_b(n^{-1}),
\]
\[
 O_b\!\left(\int_{-\pi}^{\pi}t^2e^{-c_bnt^2}dt\right)
 =O_b(n^{-3/2}).
\]
Multiplication by \(n(n-1)\) proves (7.2) and (7.3). \(\square\)

### Theorem 7.2 — the full radial weighted response is sub-\(n^{3/2}\) **[PROVED]**

For the specified corrected clock and actual weights,
\[
 \boxed{
 W_n^{\mathrm{rad}}
 =O_{b,c}\!\left(n\log^{5/2}n\right)
 =o(n^{3/2}).
 }
 \tag{7.4}
\]
All layers and both the central window and its complement are included.

#### Proof

Let
\[
 R_n=\left\lceil2\sqrt{n\log n}\right\rceil.
\]
For \(0\le r<R_n\), put
\[
 D_r=d_{k-r}^{\mathrm{rad}},
 \quad
 v_r=w_{k-r},
 \quad
 S_t=\sum_{r=0}^{t-1}D_r
 =\mathfrak h_k-\mathfrak h_{k-t}.
\]
By Theorem 6.1,
\[
 |S_t|\le C(t^2/k+\log^2k).
 \tag{7.5}
\]
Discrete Abel summation gives
\[
 \sum_{r=0}^{R_n-1}v_rD_r
 =v_{R_n-1}S_{R_n}
  +\sum_{r=1}^{R_n-1}(v_{r-1}-v_r)S_r.
 \tag{7.6}
\]
By Lemma 7.1,
\[
 |v_r|\le C_bn,
 \qquad
 |v_{r-1}-v_r|\le C_b\sqrt n.
\]
Thus the central part of (7.6) is at most a constant times
\[
 n\left(R_n^2/k+\log^2k\right)
 +\sqrt n\left(
    R_n^3/k+R_n\log^2k
  \right)
 =O(n\log^{5/2}n).
 \tag{7.7}
\]

For the complementary layers, every fixed-latent relative entropy is at most
\(
\log|\Omega_l|\le n\log2
\), hence
\[
 |d_l^{\mathrm{rad}}|\le2n\log2.
 \tag{7.8}
\]
The inherited Hoeffding coefficient estimate and telescoping of the nonnegative \(w_l\)'s give
\[
 \sum_{l=2}^{k-R_n}w_l
 \le B_{k-R_n-1}
 \le n(n-1)
  \exp\!\left[-\frac{2R_n^2}{n-2}\right]
 =O(n^{-6}).
 \tag{7.9}
\]
The tail contribution is therefore \(O(n^{-5})\). Combining it with (7.7), and restoring the factor \(-2\), proves (7.4). \(\square\)

The logarithmic exponent in (7.4) is not claimed sharp. Its only role is to prove that the entire fixed-latent radial mechanics are strictly below the \(n^{3/2}\) scale while paying the actual tails.

---

## 8. The exact remaining source of a possible \(-\Theta(n^{3/2})\) response

Multiply (4.6) by \(-2w_l\) and sum.

### Theorem 8.1 — latent-information response theorem **[PROVED]**

Let
\[
 \mathcal M_n
 :=2\sum_{l=2}^{k}w_l
   [J_l(s_l)-J_{l-1}(s_{l-1})].
 \tag{8.1}
\]
Then
\[
 \boxed{
 W_n=W_n^{\mathrm{rad}}+\mathcal M_n,
 }
 \tag{8.2}
\]
and consequently
\[
 \boxed{
 W_n=\mathcal M_n+o(n^{3/2}).
 }
 \tag{8.3}
\]

In particular:

1. If \(\mathcal M_n=o(n^{3/2})\), then \(W_n=o(n^{3/2})\).
2. If \(W_n\le-\eta n^{3/2}\) along a subsequence for some \(\eta>0\), then
   \[
   \mathcal M_n\le-\eta n^{3/2}+o(n^{3/2})
   \]
   on that subsequence.
3. A positive order-one corrected-law \(d_l\) over the central weight scale, once the radial block cancellation has taken effect, requires the own-clock mutual-information increment \(\Delta J_l\) to be negative on average there.

#### Proof

Equation (8.2) is the weighted sum of (4.6). Equation (8.3) follows from Theorem 7.2. The three consequences are immediate. \(\square\)

This theorem identifies which object must create or prevent central non-vanishing. It is not the fixed-A deletion cost, the fixed-A reverse heat cost, or the first-order clock mismatch: those contributions cancel below the \(n^{3/2}\) scale. It is the DPP-mixture information commutator (4.10).

The theorem also clarifies the relation to the first-round skew/Green--Kubo ledger. Averaging that ledger conditional on \(A\) produces the radial response. The convexity deficit between “average conditional entropy response” and “entropy response of the mixture” is exactly the increment of \(J_l\). Thus the unresolved aggregate of completion skew and entropy-production curvature is not arbitrary: after radial cancellation, its possible leading term is the latent-information response (8.1).

No sign for \(\mathcal M_n\) is proved here. The two nonnegative pieces in (4.10) can occur in either order.

---

## 9. What the C02 observations do and do not establish

The C02 computation reports, at \(n=20\), approximately
\[
 A_k=0.639656,
 \qquad
 E_k=0.031132,
 \qquad
 d_k=0.608524,
 \qquad
 W_n=-150.682781.
\]
Those values are binary64 diagnostics, not interval certificates or asymptotic statements.

The one-dimensional fixed-latent diagnostic at the same prescribed clock gives
\[
 A_k^{\mathrm{rad}}\approx2.305879,
 \qquad
 E_k^{\mathrm{rad}}\approx0.193829,
 \qquad
 d_k^{\mathrm{rad}}\approx2.112049.
\]
Combining these exploratory numbers with the exact identity (4.6) yields
\[
 \Delta J_k\approx1.503525>0
 \qquad(n=20).
 \tag{9.1}
\]
Thus, at \(n=20\), latent mixing substantially *reduces* the positive radial increment; it is not the source of the observed positive \(d_k\).

The proved radial asymptotics show a different large-size picture: the *difference* of the two radial mechanisms has vanishing central block average, while the clock ratio approaches the matched half-step only slowly.  The continuum potential assigns both first-order mechanisms the coefficient \(L_c\); the displayed finite-\(n\) convergence of the individual costs toward that coefficient is exploratory rather than a theorem of this report. Exploratory binary64 radial values are:

| \(n\) | \(2\delta_k/\varepsilon_k\) | \(A_k^{\rm rad}\) | \(E_k^{\rm rad}\) | \(d_k^{\rm rad}\) |
|---:|---:|---:|---:|---:|
| 20 | 0.0689 | 2.3059 | 0.1938 | 2.1120 |
| 100 | 0.6784 | 3.2142 | 2.2158 | 0.9985 |
| 200 | 0.8914 | 3.3670 | 2.9892 | 0.3778 |
| 500 | 0.9652 | 3.4444 | 3.3080 | 0.1364 |
| 1000 | 0.9836 | 3.4634 | 3.3973 | 0.0661 |

These decimals are not used in any proof. They merely illustrate the proved crossover mechanism.

Accordingly, there are two logically distinct possibilities for the corrected law:

* **crossover:** \(\Delta J_l\) also has a vanishing weighted central average, giving \(W_n=o(n^{3/2})\); or
* **persistent cusp:** \(\Delta J_l\) develops a negative order-one central profile, producing \(W_n=-\Theta(n^{3/2})\).

The C02 range does not distinguish them. In fact, because (9.1) has the opposite sign from that required for a persistent positive corrected \(d_l\) once the radial increment vanishes, the negative-order hypothesis would require a later sign crossover in the information commutator. This is possible but not established.

---

## 10. Status of the primary targets

### Target 1: positive central \(d_l\) on actual \(w_l\)-mass

**INCOMPLETE for the corrected law.**

What is proved instead is a genuine obstruction:

* the fixed-latent central prefix sums are \(O(r^2/k+\log^2k)\) over an expanding \(\sqrt{n\log n}\) window;
* their full actual-weight response is \(o(n^{3/2})\);
* therefore any non-vanishing corrected central profile must be carried by the latent-information increment \(-\Delta J_l\).

A result only at \(l=k\) is not used to draw a conclusion about \(W_n\).

### Target 2: control of reverse heat against deletion

**PROVED for the complete fixed-latent radial part; INCOMPLETE for the DPP mixture.**

The continuum potential (5.1) proves exact first-order cancellation between deletion and clock variation at the central boundary. The common cost is \(L_c=c\log((1+c)/(1-c))\). The remaining DPP-mixture term is exactly (4.10), not an unsigned remainder.

The signed first-round completion skew is not assumed favorable. No \(\chi^2\)-to-KL promotion is made.

### Target 3: sign and order of the full \(W_n\)

**INCOMPLETE.**

The full corrected-law response satisfies the sharp scale reduction
\[
 W_n=\mathcal M_n+o(n^{3/2}),
\]
but the sign and scale of \(\mathcal M_n\) remain open. Therefore neither
\[
 W_n=-\Theta(n^{3/2})
\]
nor
\[
 W_n=O(n)
\]
is proved.

All radial tails are paid in Theorem 7.2. The old all-layer \(O(n^{3/2})\) bound still pays the full corrected-law tails.

---

## 11. Boundary and failure checks

### 11.1 Endpoint convention **[PROVED handled]**

At \(l=1\), the mixture law is uniform, so \(h(1)=0\). Conditional on \(A\), a uniformly selected point of \(A\) has KL \(\log2\) from uniform, and its mutual information with \(A\) is the same \(\log2\). Thus (4.5) remains exact with \(s_1=0\). No fictitious reverse clock is assigned to the endpoint.

### 11.2 Full lower half and upper-half symmetry **[PROVED handled]**

The exact formula for \(W_n\) has already paired the particle--hole symmetric upper half into the lower-half weights. Theorem 7.2 treats every lower-half layer, not only a fixed-width center.

### 11.3 Actual tail mass **[PROVED paid]**

The central window is \(R_n\asymp\sqrt{n\log n}\), not fixed width. Equation (7.9) makes the omitted coefficient mass polynomially negligible after multiplication by the worst radial entropy difference.

### 11.4 Positive forward correction **[NOT USED]**

The representation \(P_l^{\delta}=e^{a(M_l-I)}\) is an accounting identity. It does not claim that deletion followed by forward heat maps one corrected target exactly to the next. The inherited \(n=6\) counterexample remains intact.

### 11.5 No true-output or Toeplitz transfer **[NOT CLAIMED]**

The latent set \(A\) is used only to disintegrate the specified corrected law. No equality, approximation, or entropy-rate conclusion for the true DPP output is asserted.

### 11.6 Comparison with \(C_n\) **[INCOMPLETE]**

Even a proof of \(W_n=-\Theta(n^{3/2})\) would not by itself settle \(W_n+C_n\), and the present report does not prove that response. The supplied information gives only a positive lower limit for \(C_n/n\), not a matching upper bound or a sign-dominating constant.

---

## 12. Calculations actually performed

### 12.1 Proof calculations

The following are analytic and are used in the proofs:

1. independent recomputation of \(K_l^*K_l=I+\varepsilon_lG_l\);
2. exact Poissonized down--up formula (2.4) and matched-defect split (2.8);
3. saddle-point/local coefficient estimates (3.2)--(3.4);
4. explicit center clock expansion (3.9);
5. exact KL chain-rule decomposition \(F_l=\mathfrak F_l-J_l\);
6. exact radial mean and variance equations;
7. the radial entropy potential \(\Phi\) and directional cancellation (5.10);
8. expanding-window prefix bound (6.1);
9. Fourier first/second difference bounds for the actual \(B_m\);
10. Abel summation plus the inherited Hoeffding tail estimate proving (7.4).

### 12.2 Exploratory numerical calculations

The accompanying script `round2_radial_clock_diagnostics.py` evaluates:

* exact integer coefficient sums for \(\theta_k,\theta_{k-1}\), followed by binary64 logarithms;
* the one-dimensional fixed-latent birth--death law using sparse matrix-exponential action;
* the radial KL costs at the central two layers.

The accompanying JSON is explicitly marked
`EXPLORATORY_BINARY64_NOT_INTERVAL_CERTIFIED`.
No decimal from it is used to establish a theorem.

No large-\(n\) corrected-law entropy was claimed from Monte Carlo, and no fitted asymptotic exponent was used.

---

## 13. Exact improvement over Round 1

Round 1 proved an explicit common deletion/clock ledger and showed that the weighted deletion cost alone is \(\Theta(n^{3/2})\), but it could not determine whether reverse heat cancels that term.

Round 2 adds:

1. **The exact dimensionless Poisson clock:**
   \[
   P_l^{s_l-s_{l-1}}
   =e^{a_{n,l}(K_l^*K_l-I)}.
   \]
2. **A proved slow-crossover expansion:** the clock reaches the half-step only at rate \(1/k\) with a large coefficient \(1/(4b)-5/2\).
3. **A fixed-latent continuum potential:** \(\mathfrak F_l(s)=k\Phi(\lambda,e^{-ns})+O(\log k)\).
4. **Exact first-order deletion/reverse-heat cancellation:** the directional derivative (5.10) is zero.
5. **An expanding-window, actual-weight theorem:** the entire radial response is \(o(n^{3/2})\), with every tail paid.
6. **A precise remaining obstruction:** any order-\(n^{3/2}\) corrected response is exactly the latent mutual-information response to leading order.

This is a rigorous improvement even though the final sign remains open: the potential \(n^{3/2}\) term has been removed from all universal radial mechanics and localized to one DPP-specific information increment.

---

## 14. Smallest remaining obstruction

The smallest unresolved statement is now:

> **Latent-information cusp problem.** Determine the sign and scale of
> \[
> \mathcal M_n
> =2\sum_{l=2}^{k}w_l
>   [I(A;S_{l,s_l})-I(A;S_{l-1,s_{l-1}})].
> \]
> In particular, decide whether \(\mathcal M_n=o(n^{3/2})\), or whether it has a nonzero negative \(n^{3/2}\) limit.

A proof of a negative order-one profile for the bracket on a region carrying fixed actual \(w_l\)-mass would yield \(W_n=-\Theta(n^{3/2})\). A proof that all central prefix sums of this information increment are \(o(\sqrt n)\), with suitable weighted regularity and tails, would rule out such a term.

This is not merely the original \(d_l\) under a new name. Theorem 7.2 has already removed the full fixed-latent deletion, reverse-heat, clock, and radial fluctuation contribution at the target scale. What remains measures only the convexity deficit generated by mixing over the projection-DPP latent set.

---

## 15. Dependency ledger

### Fixed inputs from the PRO03 packet

* **D1.** Corrected law, coefficient-defined \(\theta_l\), original generator, endpoint convention, and actual \(B_m,w_l\): `inputs/TASK.md` and `inputs/SA04_REPORT.md`.
* **D2.** Same-time deletion coherence, heat/deletion intertwining, and the exact lower-half identity for \(W_n\): `inputs/SA04_REPORT.md`, within the scope described by `SOL_REVIEW.md`.
* **D3.** Nonnegativity of \(w_l\) and the coefficient-tail estimate used in (7.9): Section 7 of `inputs/SA04_REPORT.md`.
* **D4.** C02 decimals are consulted only as exploratory evidence: `COMPUTE01/SA04_CENTRAL_SCALE.md` and its script/JSON outputs.

### Rechecked first-round item

* **R1.** The operator identity \(K_l^*K_l=I+\varepsilon_lG_l\) is independently proved in Theorem 2.1.

### New self-contained results

* **N1.** Exact Poisson parameter and matched-defect formula (2.4), (2.8).
* **N2.** Central and moderate-window clock asymptotics (3.9), (3.11).
* **N3.** Exact radial/mutual-information decomposition (4.5)--(4.10).
* **N4.** Radial entropy potential (5.4) and central directional cancellation (5.10).
* **N5.** Expanding-window radial prefix estimate (6.1).
* **N6.** Actual-weight radial response bound (7.4), including tails.
* **N7.** Leading-scale latent-information response theorem (8.3).

### External theorem dependence

No load-bearing external result is invoked without derivation. Stirling bounds, Fourier inversion, exponential tilting, Taylor's theorem, Chebyshev's inequality, the KL chain rule, and discrete Abel summation are used in their elementary finite forms and are applied explicitly above.

---

## 16. Statement for a fresh independent reviewer

A later reviewer should independently verify these six points:

1. the factor and orientation in
   \[
   P_l^{s_l-s_{l-1}}
   =e^{[(s_l-s_{l-1})/\varepsilon_l](K_l^*K_l-I)};
   \]
2. the coefficient identity (3.1) and the center expansion coefficient
   \(5/2-1/(4b)\);
3. the KL chain-rule identity
   \(F_l=\mathfrak F_l-I(A;S_{l,s})\);
4. the radial rate function and potential
   \[
   \Phi(\lambda,\zeta)
   =2H(\lambda/2)
    -H(\lambda(1+\zeta)/2)
    -H(\lambda(1-\zeta)/2);
   \]
5. the exact directional cancellation
   \(-\Phi_\lambda(1,c)+c\Phi_\zeta(1,c)=0\);
6. the Abel-summation signs and the use of first/second actual-weight differences in Theorem 7.2.

The main corrected-law sign remains open. The strongest new theorem is that the universal fixed-latent radial response is \(o(n^{3/2})\), so any nonzero response at that scale must be generated by the latent DPP mutual-information cusp in (8.1).
