# FK path construction: first candidate, incomplete

Assume H only when  
\[
p=\exp \tau(\log Q)=0.
\]
For every fixed \(Q\), there is a total Borel, all-input \(\Gamma\)-equivariant iid map producing \((X,Y)\) with
\[
X\sim \operatorname{Ber}(p)^\Gamma,\qquad
Y\sim\mu_Q,\qquad
X\subseteq Y.
\]

For \(0<p<1\), H is not used. If
\[
\varepsilon I\le Q\le(1-\varepsilon)I,
\]
the construction is a pure-birth path reaching \(\mu_Q\) at finite path time. Without an endpoint spectral gap, the path is constructed on every compact interval before the endpoint and \(Y\) is its increasing union. The construction is for each fixed kernel, using regular-\(\Gamma\) noise; no simultaneous measurable grand coupling or finitary property is asserted.

## 1. The FK path and its finite flow

Suppose \(0<p<1\). Put
\[
a_t=\frac{p}{\operatorname{FK}(Q+tI)},\qquad
K_t=a_t(Q+tI),\qquad
r_t=a_t\tau(K_t^{-1})
     =\tau((Q+tI)^{-1}).
\]
Then
\[
a_t'=-r_ta_t,\qquad
K_t'=a_tI-r_tK_t. \tag{1}
\]

Let \(M=\|Q\|\). The spectral integral gives
\[
\log \frac{\operatorname{FK}(Q+tI)}p
 =\int\log(1+t/\lambda)\,d\nu_Q(\lambda)
 \ge \log(1+t/M),
\]
so
\[
0<K_t\le MI\le I.
\]
For every \(t>0\), \(K_t\) has a two-sided spectral gap unless \(Q=I\). Moreover,
\[
K_t\longrightarrow pI\quad(t\to\infty),
\qquad
K_t\longrightarrow Q\quad(t\downarrow0) \tag{2}
\]
in norm.

For finite \(F\subset\Gamma\), write \(K_t^F=P_FK_tP_F\). For every \(B\subseteq F\),
\[
\frac d{dt}\det K_t^F[B]
 =
a_t\sum_{i\in B}\det K_t^F[B\setminus\{i\}]
-r_t|B|\det K_t^F[B]. \tag{3}
\]

For a finite DPP with \(L=K(I-K)^{-1}\), expansion of
\(\det(I-K+KZ)\) gives
\[
\mathbf P[X=\eta]=\det(I-K)\det L[\eta].
\]
Hence, if \(q_i(\eta)\) is the conditional occupation probability at \(i\) given the entire exterior configuration,
\[
\frac{q_i}{1-q_i}=\lambda_L(i,\eta), \tag{4}
\]
where \(\lambda_L(i,\eta)\) is the Schur complement.

Equation (3) is the forward equation for deaths with rate
\[
d_t(i,\eta)=r_t-\frac{a_t}{q_i},
\]
and, after reversing \(t\), for births with rate
\[
c_t(i,\eta)=\frac{r_tq_i-a_t}{1-q_i}. \tag{5}
\]
Indeed,
\[
\mathbf E\!\left[
 \frac{\mathbf 1_{\{B\subseteq X\}}}{q_i(X_{\ne i})}
 \right]
 =
\mathbf P[B\setminus\{i\}\subseteq X],
\]
and, conditionally on the exterior,
\[
\mathbf E[
 \mathbf1_{\{i\notin X\}}c_t(i,X)
 \mid X_{\ne i}]
 =r_tq_i-a_t.
\]

## 2. Canonical full-exterior conditional probabilities

For positive invertible \(L\), define
\[
\lambda_L(x,\eta)
 =
\left\langle
 L^{1/2}(I-\Pi_\eta^L)L^{1/2}\delta_x,\delta_x
\right\rangle,
\qquad
\Pi_\eta^L=P_{\overline{L^{1/2}\ell^2(\eta)}}. \tag{6}
\]
Equivalently,
\[
\lambda_L(x,\eta)
 =
\inf_{h\in\ell^2(\eta)}
 \langle L(\delta_x+h),\delta_x+h\rangle.
\]

If \(D_\eta\) is the coordinate projection, then
\[
\mathsf S_\eta(L)
 =
L-LD_\eta
  (D_\eta LD_\eta+I-D_\eta)^{-1}
  D_\eta L. \tag{7}
\]
Thus \(\eta\mapsto\lambda_L(x,\eta)\) is a total Borel, covariant, product-continuous function.

For
\[
L_t=K_t(I-K_t)^{-1},
\]
put
\[
q_t(x,\eta)
 =
\frac{\lambda_{L_t}(x,\eta)}
      {1+\lambda_{L_t}(x,\eta)}. \tag{8}
\]
This is an all-input version of
\[
\mathbf P_{\mu_{K_t}}
 [X_x=1\mid X_{\Gamma\setminus\{x\}}].
\]

To prove this, compress to finite \(F_n\uparrow\Gamma\). The finite conditional probabilities are given by (8). Uniform spectral gaps imply strong convergence of the corresponding \(L_{t,n}\), and formula (7), including the moving projections \(D_{X\cap F_n}\), gives samplewise convergence of the Schur complements. Bounded martingale convergence then identifies the limit with conditioning on the entire exterior.

Shorting decreases as the occupied set grows, and
\[
\lambda_{L_t}(x,\Gamma\setminus\{x\})
 =
\frac{1}
 {\langle L_t^{-1}\delta_x,\delta_x\rangle}
 =
\frac{a_t}{r_t-a_t}. \tag{9}
\]
Therefore
\[
q_t(x,\eta)\ge \frac{a_t}{r_t},
\]
so the birth rate is nonnegative. In odds form,
\[
c_t(x,\eta)
 =
(r_t-a_t)\lambda_{L_t}(x,\eta)-a_t,
\qquad x\notin\eta. \tag{10}
\]

Now use reverse time
\[
s=(1+t)^{-1},\qquad
t_s=s^{-1}-1,\qquad
\beta_s(x,\eta)=s^{-2}c_{t_s}(x,\eta), \tag{11}
\]
with rate zero when \(x\in\eta\).

## 3. Covariant transport sensitivity

Let \(\eta\subseteq\zeta\), set
\[
D=P_{\ell^2(\zeta\setminus\eta)},\qquad
T=(I-\Pi_\eta^L)L^{1/2}D=V|T|,
\]
and
\[
P=VV^*=\Pi_\zeta^L-\Pi_\eta^L.
\]
For \(x\notin\zeta\),
\[
\lambda_L(x,\eta)-\lambda_L(x,\zeta)
 =
\|V^*L^{1/2}\delta_x\|^2. \tag{12}
\]

Since
\[
PL^{-1/2}(I-D_\zeta)=0,
\]
for any scalar \(\ell>0\),
\[
V^*L^{1/2}\delta_x
 =
V^*L^{-1/2}(L-\ell I)\delta_x.
\]
For \(y\in\zeta\setminus\eta\), define
\[
w(x,y)=
\left|
 \left\langle
 V^*L^{-1/2}(L-\ell I)\delta_x,\delta_y
 \right\rangle
\right|^2.
\]
Its row sum equals (12), and both its row and column sums are at most
\[
\kappa(L)
 =
\|L^{-1}\|\,\|L-\ell I\|^2. \tag{13}
\]
Indeed,
\[
\sum_{x\notin\zeta}w(x,y)
 =
\|(I-D_\zeta)(L-\ell I)L^{-1/2}V\delta_y\|^2.
\]

For arbitrary pairs, compare each configuration with their intersection. Taking
\[
\ell=\frac{p}{1-p},
\]
multiplying by \(r_t-a_t\), and adding a source-site diagonal term when precisely one configuration occupies the source produces covariant Borel coefficients \(A_s\), supported on the mismatch set, such that
\[
|\beta_s(x,U)-\beta_s(x,V)|
 \le
\sum_{y:U_y\ne V_y}
 A_s(x,y;U,V), \tag{14}
\]
with both row and column sums at most
\[
C_s
 =
s^{-2}\left(
 \overline c_{t_s}
 +2(r_{t_s}-a_{t_s})\kappa(L_{t_s})
\right), \tag{15}
\]
where
\[
\overline c_t=\sup_{x\notin\eta}c_t(x,\eta).
\]

The polar part is Borel because
\[
V=\operatorname{s-lim}_{n\to\infty}
T(T^*T+n^{-1}I)^{-1/2}.
\]

For every jointly invariant pair \((U,V)\), mass transport and Tonelli now give
\[
\mathbf E|\beta_s(e,U)-\beta_s(e,V)|
 \le
C_s\mathbf P[U_e\ne V_e]. \tag{16}
\]
No amenability or invariant mean is used.

## 4. Finite-block-flow criterion

We prove the abstract passage from finite conditional flows to an iid process.

Let \(\rho_s(x,\eta)\), defined for \(x\notin\eta\), be nonnegative, bounded, covariant, jointly continuous and decreasing in \(\eta\). Suppose it has a transport estimate of the form (14), with
\[
C\in L^1[0,S].
\]
Let \((\nu_s)_{0\le s\le S}\) be invariant laws with positive finite-cylinder probabilities,
\[
\nu_0=\operatorname{Ber}(p)^\Gamma,
\]
and suppose every cylinder function \(f\) satisfies
\[
\frac d{ds}\nu_s(f)
 =
\int\sum_x
 \mathbf1_{\{x\notin\eta\}}\rho_s(x,\eta)
 [f(\eta\cup\{x\})-f(\eta)]
 \,d\nu_s(\eta). \tag{17}
\]

Then there is an equivariant iid pure-birth process with marginals \(\nu_s\).

Choose finite \(D_n\uparrow\Gamma\). For ordered configurations \(L\le U\), define finite-range envelope rates by filling the unseen exterior with zero for the upper rate and one for the lower rate:
\[
\overline\rho_s^n(x;L,U)
 =
\rho_s\bigl(x,(L\cap xD_n)\setminus\{x\}\bigr),
\]
\[
\underline\rho_s^n(x;L,U)
 =
\rho_s\!\left(
 x,\bigl((U\cap xD_n)\cup(\Gamma\setminus xD_n)\bigr)
 \setminus\{x\}
 \right). \tag{18}
\]
Drive lower and upper processes from the same Bernoulli field by common Poisson proposals. Finite interaction range and bounded rates give a nonexplosive equivariant construction, and
\[
L^n\le U^n.
\]

Joint continuity on the compact configuration space implies
\[
\omega_n(S):=
\sup_{\substack{s\le S,\;\eta_e=\zeta_e=0\\
                 \eta|_{D_n}=\zeta|_{D_n}}}
|\rho_s(e,\eta)-\rho_s(e,\zeta)|
\longrightarrow0. \tag{19}
\]

Let \(p_n(T)\) be the probability that the two root paths differ somewhere before \(T\). A discrepancy can be created only by a proposal between the two thresholds. When both source sites are vacant, the threshold gap is bounded by two tail errors plus the rate difference for the actual ordered configurations. Compensation, (14), and mass transport yield
\[
p_n(T)
 \le
2T\omega_n(T)+\int_0^TC_sp_n(s)\,ds,
\]
hence
\[
p_n(T)
 \le
2T\omega_n(T)
\exp\!\left(\int_0^TC_s\,ds\right)
\longrightarrow0. \tag{20}
\]

Exact marginal identification requires more than weak convergence. For finite \(F\), define
\[
\widehat\rho_{s,F,x}(\xi)
 =
\mathbf E_{\nu_s}
 [\rho_s(x,X)\mid X_F=\xi],
\qquad \xi_x=0. \tag{21}
\]
Conditioning (17) shows that \(\nu_s|_F\) is exactly the law of the finite pure-birth chain with rates (21).

Couple this chain to \((L^n,U^n)\). Whenever the order holds on \(xD_n\), monotonicity gives
\[
\underline\rho_s^n
 \le
\widehat\rho_{s,F,x}
 \le
\overline\rho_s^n. \tag{22}
\]
An order violation at an interior point must be preceded by a chronological proposal chain from the boundary. If the dependency degree is \(d_n\), rates are bounded by \(B\), and the point is \(k\) dependency steps from the boundary, this probability is at most
\[
\sum_{j\ge k}\frac{(Bd_nT)^j}{j!}. \tag{23}
\]
Exhausting \(\Gamma\) by finite \(F\) therefore gives, for finite \(B_0\),
\[
\left\|
 \mathcal L(L_s^n|_{B_0})-\nu_s|_{B_0}
\right\|_{\mathrm{TV}}
\le |B_0|p_n(S). \tag{24}
\]

Represent each pure-birth coordinate by its birth time. Compactness gives an invariant weak subsequential limit of \((L^n,U^n)\). Equation (20) makes the two limiting paths equal; call the common path \(W\). Equation (24) gives
\[
W_s\sim\nu_s.
\]

The lower compensator differs in mean from the full rate by at most
\[
\int_0^T
 \bigl(\omega_n(s)+C_sp_n(s)\bigr)\,ds
\longrightarrow0. \tag{25}
\]
Passing finite-coordinate martingale identities to the limit proves that \(W\) has intensity
\[
\rho_s(x,W_{s-}).
\]

Progressively mark every true birth uniformly below its intensity and independently add Poisson points above that intensity, up to a common rate bound. Their union \(N\) has deterministic compensator
\[
\#_\Gamma(dx)\,ds\,du.
\]
On each finite site/time window,
\[
\exp\!\left[
 -\int h\,dN+\int(1-e^{-h})\,d\nu
\right]
\]
is a bounded martingale. Its conditional Laplace formula proves that \(N\) is an iid Poisson field in the common right-continuous filtration.

The infinite total spatial rate causes no gap: every martingale used here is restricted to finitely many sites. Such compensated counts are dominated on compact times by an integrable finite-window Poisson count. If \(A\in\mathcal G_s^+\), choose \(s_k\downarrow s\); \(L^1\)-right continuity gives
\[
\mathbf E[\mathbf1_A M_t]
 =
\lim_k\mathbf E[\mathbf1_A M_{s_k}]
 =
\mathbf E[\mathbf1_A M_s],
\]
so usual augmentation preserves the martingale property. The conditional Laplace identity also shows that \(N\) is independent of \(W_0\).

Now perform Picard iteration from \((W_0,N)\). If two successive invariant iterates differ at the root by time \(T\), (16) gives
\[
D_{k+1}(T)
 \le
\int_0^TC_sD_k(s)\,ds,
\qquad
D_k(T)\le\frac{A(T)^k}{k!},
\]
where
\[
A(T)=\int_0^TC_s\,ds.
\]
Borel–Cantelli gives compact-time coordinatewise stabilization and a fixed point. The same estimate proves uniqueness among jointly invariant, adapted, càdlàg pure-birth solutions driven by the same Poisson field and initial configuration. Therefore the strong solution equals \(W\), proving the criterion.

## 5. Verification at the scalar entrance

Take
\[
\nu_s=\mu_{K_{t_s}},
\qquad
\nu_0=\operatorname{Ber}(p)^\Gamma.
\]
Equations (3)–(10), with
\[
\frac{dt}{ds}=-s^{-2},
\]
give (17) first for inclusion monomials and hence for every cylinder function. Positive cylinder probabilities follow from the two-sided spectral gap for \(s<1\).

It remains to control \(s=0\). Put
\[
u=t^{-1},\qquad
m=\tau(Q),\qquad
\ell=\frac p{1-p}.
\]
Norm functional calculus gives
\[
a_t=pu-pmu^2+O(u^3),
\qquad
r_t=u-mu^2+O(u^3),
\]
\[
K_t=pI+pu(Q-mI)+O(u^2),
\]
and
\[
L_t=\ell I+uG+O(u^2),
\qquad
G=\frac{p}{(1-p)^2}(Q-mI),
\qquad
\tau(G)=0.
\]
Equivariance makes the diagonal of \(G\) zero. Formula (7) then gives, uniformly over \(x\notin\eta\),
\[
\lambda_{L_t}(x,\eta)=\ell+O(u^2). \tag{26}
\]
Indeed, the constrained off-diagonal vector is
\[
uD_\eta G\delta_x+O(u^2),
\]
so the Schur-complement subtraction is quadratic.

Consequently
\[
\sup_{x,\eta}c_t(x,\eta)=O(u^3),
\qquad
(r_t-a_t)\kappa(L_t)=O(u^3). \tag{27}
\]
Since
\[
u=\frac{s}{1-s},
\]
the time-changed rates and \(C_s\) are \(O(s)\). Set \(\beta_0=0\). All hypotheses of the criterion therefore hold on every
\[
[0,S],\qquad S<1.
\]

Thus one increasing equivariant iid path satisfies
\[
Z_0\sim\operatorname{Ber}(p)^\Gamma,
\qquad
Z_s\sim\mu_{K_{t_s}}.
\]

If \(Q\) is two-sided gapped, all estimates extend through \(s=1\), and
\[
Z_1\sim\mu_Q.
\]
For arbitrary \(0<p<1\), define
\[
X=Z_0,\qquad
Y=\bigcup_{s<1}Z_s.
\]
For every finite \(B\),
\[
\mathbf P[B\subseteq Y]
 =
\lim_{s\uparrow1}\det K_{t_s}[B]
 =
\det Q[B].
\]
Hence
\[
Y\sim\mu_Q,\qquad X\subseteq Y.
\]

If \(p=0\), take \(X=\varnothing\) and use H once to sample \(Y\sim\mu_Q\). If \(p=1\), then \(\log Q\le0\) and \(\tau(\log Q)=0\); faithfulness of the group trace implies \(Q=I\), so take
\[
X=Y=\Gamma.
\]

Finally, split every iid uniform label into an initial Bernoulli bit and a marked Poisson process. The Picard iterates are total Borel and exactly equivariant. On the invariant conull set where every coordinate stabilizes on every rational compact horizon and the limiting path satisfies the graphical equation, output its entrance and terminal configurations. Off this set output
\[
(\varnothing,\varnothing).
\]
This gives a total, all-input equivariant factor.

Thus \(\mu_Q\) stochastically dominates
\[
\operatorname{Ber}(\operatorname{FK}(Q))^\Gamma.
\]
Applying the result to \(I-Q\) and taking complements gives the corresponding upper domination. These are the two inequalities formulated as Lyons’s Conjecture 5.7; the survey also notes that invariant monotone couplings do not follow from stochastic domination for arbitrary invariant measures. [Lyons, ICM survey](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf)
