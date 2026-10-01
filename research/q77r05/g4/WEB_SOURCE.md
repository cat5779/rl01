# PROVED

Let \(W\) be any countable set, let \(\Gamma\) act on \(W\) by permutations, and let \(Q\) be a Hermitian positive contraction commuting with that action. There exists a **total Borel, exactly \(\Gamma\)-equivariant** map
\[
F:[0,1]^W\longrightarrow\{0,1\}^W,
\qquad
F_*(\operatorname{Leb}^{\otimes W})=\mathbf P^Q.
\]

The construction below uses precisely \(W\)-indexed randomness.

If \(W=\varnothing\), use the unique map. Otherwise write
\[
Q_{xy}=\langle Q\delta_y,\delta_x\rangle,\qquad \mu=\mathbf P^Q.
\]
Countable-set DPP existence applies because \(0\le Q\le I\). Inclusion-exclusion gives uniqueness and all finite pattern probabilities. In particular, \(\mu\) is invariant, and its marginal \(\mu_E\) on a finite set \(E\) is the DPP with kernel \(Q_E\). These are the countable-set facts in Lyons–Thom, Section 2; no soficity-dependent theorem is used. :chatgpt-content-reference{index="0"}

Throughout, permutation actions on fields mean \((\gamma y)_x=y_{\gamma^{-1}x}\).

## 1. Canonical finite sets and component independence

Let \(D_n\) join distinct \(x,y\) when \(|Q_{xy}|\ge 1/n\), and let \(E_n(x)\) be its radius-\(n\) ball at \(x\). Since
\[
\sum_y|Q_{xy}|^2=(Q^2)_{xx}\le Q_{xx}\le1,
\tag{1}
\]
every degree in \(D_n\) is at most \(n^2\). Thus \(E_n(x)\) is finite. The graphs increase with \(n\), so the balls are nested. Commutation with the action gives
\[
E_n(\gamma x)=\gamma E_n(x).
\tag{2}
\]

Let \(C(x)\) be the component of \(x\) in the graph of nonzero off-diagonal entries of \(Q\). Every finite path in this graph appears in some \(D_n\) and has length at most \(n\) for sufficiently large \(n\). Therefore
\[
\bigcup_n E_n(x)=C(x).
\tag{3}
\]
No local finiteness of the full support graph is assumed.

The operator is block diagonal over these components. To prove independence explicitly, take finitely many distinct components \(C_i\) and disjoint finite \(A_i,B_i\subset C_i\). Inclusion-exclusion and block determinants give
\[
\begin{aligned}
&\mu\{\eta|_{A_i}=1,\ \eta|_{B_i}=0\text{ for every }i\}\\
&=\sum_{J_i\subset B_i}(-1)^{\sum_i|J_i|}
  \det Q_{\bigcup_i(A_i\cup J_i)}\\
&=\prod_i\left(\sum_{J_i\subset B_i}(-1)^{|J_i|}
  \det Q_{A_i\cup J_i}\right).
\end{aligned}
\tag{4}
\]
The empty determinant is one. Cylinder events generate the component sigma-fields, so the pi-lambda theorem extends this factorization to their independence.

The same calculation, grouping all components except one together, proves that
\[
\eta|_C\ \text{is independent of}\ \eta|_{W\setminus C}.
\]
This is independence from the **entire complement**, as required for the posterior argument.

## 2. Finite tilts, including singular and complex kernels

Let \(K\) be any finite Hermitian positive contraction with DPP law \(\nu\). For \(h\in\mathbb R^E\), define
\[
\nu_h(\sigma)
=\frac{e^{h\cdot\sigma}\nu(\sigma)}
       {\mathbb E_\nu e^{h\cdot\sigma}},
\qquad
m_x(h)=\mathbb E_{\nu_h}\sigma_x.
\]
Set
\[
D=\operatorname{diag}(e^{h_z}),\quad
B=D^{1/2}K^{1/2},\quad
M=I-K+B^*B,\quad
P=BM^{-1}B^*.
\tag{5}
\]
For \(d=\min_z e^{h_z}>0\),
\[
M\ge I-K+dK\ge\min(1,d)I>0.
\]
Also \(M\ge B^*B\), so \(BM^{-1/2}\) is a contraction and \(0\le P\le I\). Neither \(K\) nor \(I-K\) is inverted.

For diagonal \(Z=\operatorname{diag}(z_x)\), expansion of
\(\prod_x[1+(z_x-1)\sigma_x]\) gives
\[
\mathbb E_\nu\prod_xz_x^{\sigma_x}
=\det\bigl(I+K^{1/2}(Z-I)K^{1/2}\bigr).
\]
Because \(D\) and \(Z\) commute, the tilted generating polynomial is
\[
\begin{aligned}
\mathbb E_{\nu_h}\prod_xz_x^{\sigma_x}
&=\frac{\det(M+B^*(Z-I)B)}{\det M}\\
&=\det(I+(Z-I)BM^{-1}B^*)\\
&=\det(I+(Z-I)P).
\end{aligned}
\tag{6}
\]
The middle equality uses \(\det(I+UV)=\det(I+VU)\). Thus the tilted law is a DPP with Hermitian-contraction kernel \(P\), including when \(K\) has eigenvalues zero or one.

Differentiating the finite normalized sum yields
\[
\partial_{h_y}m_x(h)
=\operatorname{Cov}_{\nu_h}(\sigma_x,\sigma_y).
\]
Writing \(p=P_{xx}\), the one- and two-point determinants give covariance \(p(1-p)\) for \(y=x\), and \(-|P_{xy}|^2\) otherwise. Consequently,
\[
\begin{aligned}
\sum_y|\partial_{h_y}m_x(h)|
&=p(1-p)+(P^2)_{xx}-p^2\\
&\le2p(1-p)\le\frac12.
\end{aligned}
\tag{7}
\]
Integrating along a line segment proves the dimension-independent bound
\[
|m_x(h)-m_x(h')|
\le\frac12\|h-h'\|_\infty.
\tag{8}
\]
All of this applies to complex Hermitian kernels and deterministic coordinates.

## 3. A total drift and a causal all-input solution

For \(t\ge0\), \(y\in\mathbb R^W\), and \(E=E_n(x)\), define
\[
b^n_{t,x}(y)=
\frac{
\sum_{\sigma\in\{0,1\}^{E}}\sigma_x\mu_E(\sigma)
 e^{\sum_{z\in E}(y_z-t/2)\sigma_z}
}{
\sum_{\sigma\in\{0,1\}^{E}}\mu_E(\sigma)
 e^{\sum_{z\in E}(y_z-t/2)\sigma_z}
},
\qquad
b_{t,x}(y)=\limsup_n b^n_{t,x}(y).
\tag{9}
\]
Every denominator is positive. These definitions apply to **every real field**, not just bounded fields or fields sampled from an observation law.

Each finite expression is jointly Borel in \((t,y)\), takes values in \([0,1]\), and is equivariant. Its limsup has the same properties. From (8), whenever \(y-y'\) is bounded,
\[
\sup_x|b_{t,x}(y)-b_{t,x}(y')|
\le L\sup_z|y_z-y'_z|,
\qquad L=\frac12.
\tag{10}
\]
Indeed, take limsups in the two finite inequalities with \(y,y'\) interchanged. No infinite-volume tilted probability measure is being assumed.

Let
\[
\mathcal C=\{w\in C([0,\infty),\mathbb R):w(0)=0\}
\]
with the compact-open topology. For **every** \(w\in\mathcal C^W\), define
\[
Z^{(0)}_t(x)=w_t(x),\qquad
Z^{(k+1)}_t(x)
=w_t(x)+\int_0^t b_{s,x}(Z^{(k)}_s)\,ds.
\tag{11}
\]
These are coordinatewise Lebesgue integrals of bounded Borel functions. Inductively, each coordinate is continuous in time and jointly Borel in \((t,w)\). Parameter integration preserves measurability, and countability of \(W\) makes the field-valued evaluation map Borel.

Equation (10) gives, for every input and every finite \(T\),
\[
\sup_{x,\,0\le t\le T}
|Z^{(k+1)}_t(x)-Z^{(k)}_t(x)|
\le\frac{L^kT^{k+1}}{(k+1)!}.
\tag{12}
\]
The first bound is \(T\); induction integrates \(L\) times the previous bound. The series is summable, so the iterates converge uniformly in \(x\) and time on bounded intervals. The limit \(Z=\mathcal Z(w)\) has continuous coordinates, and (10) permits passage through the integrals:
\[
Z_t(x)=w_t(x)+\int_0^t b_{s,x}(Z_s)\,ds.
\tag{13}
\]

For uniqueness, every solution satisfies \(0\le Z_t(x)-w_t(x)\le t\). Two solutions with the same input therefore have a finite measurable difference
\[
D(t)=\sup_x|Z_t(x)-Z'_t(x)|\le t,
\qquad
D(t)\le L\int_0^tD(s)\,ds.
\]
Iteration gives \(D(t)\le L^kt^{k+1}/(k+1)!\) for all \(k\), hence \(D(t)=0\).

The solution map
\[
\mathcal Z:\mathcal C^W\longrightarrow\mathcal C^W
\]
is Borel: rational-time coordinate evaluations are Borel and generate the output Borel sigma-field. It is **causal measurably**: the same recursion on \([0,T]\) constructs a Borel map from restricted input paths to restricted output paths, compatible with the full construction. Every iterate and its limit commute with every \(\gamma\), on every input.

Only differences of fields are bounded here. Brownian fields themselves are not assumed to belong to \(\ell^\infty(W)\).

## 4. The full observation posterior

For law identification only, take \(\eta\sim\mu\), independent of iid Brownian paths \(B(x)\), and define
\[
X_t(x)=t\eta_x+B_t(x),\qquad
\mathcal F_t^0=\sigma(X_s(z):0\le s\le t,\ z\in W).
\tag{14}
\]
These auxiliary variables are not additional inputs to the factor.

For finite \(E\) and \(t>0\), the conditional Gaussian density of \(X_t|_E\), given \(\eta|_E=\sigma\), has its \(\sigma\)-dependent factor
\[
\exp\!\left(
\sum_{z\in E}X_t(z)\sigma_z
-\frac t2\sum_{z\in E}\sigma_z
\right).
\]
Here \(\sigma_z^2=\sigma_z\). Finite Bayes’ formula gives
\[
b^n_{t,x}(X_t)
=\mathbb E[\eta_x\mid X_t(z):z\in E_n(x)].
\tag{15}
\]

The conditioning sigma-fields increase to the endpoint observations on \(C(x)\). Since \(\eta_x\) is bounded, Lévy’s upward conditional-expectation theorem applies and gives almost-sure convergence to that component posterior. :chatgpt-content-reference{index="1"}

By Section 1 and independence of the noise,
\[
(\eta|_{C(x)},B|_{C(x)})
\quad\text{is independent of}\quad
(\eta|_{W\setminus C(x)},B|_{W\setminus C(x)}).
\]
Thus
\[
b_{t,x}(X_t)
=\mathbb E[\eta_x\mid X_t(z):z\in W]
\quad\text{almost surely}.
\tag{16}
\]

Now fix \(t>0\). The bridges satisfy
\[
X_s(z)-\frac{s}{t}X_t(z)
=B_s(z)-\frac{s}{t}B_t(z),
\qquad 0\le s\le t.
\]
The entire bridge field is independent of
\((\eta,(B_t(z))_{z\in W})\): finite bridge/endpoint Gaussian cross covariances vanish, and \(B\) is independent of \(\eta\). Cylinder independence extends to the path sigma-fields, which are generated by countably many coordinates and times.

Bridges and endpoints generate \(\mathcal F_t^0\). Therefore
\[
b_{t,x}(X_t)
=\mathbb E[\eta_x\mid\mathcal F_t^0]
\quad\text{almost surely}.
\tag{17}
\]
At \(t=0\), both sides equal \(Q_{xx}\).

These identities hold for each fixed time and vertex. The bounded jointly measurable process \(b_{t,x}(X_t)\) permits Fubini in time; no intersection over uncountably many fixed-time probability-one events is required.

## 5. Independent innovations and the usual filtration

Define
\[
\beta_t(x)
=X_t(x)-\int_0^t b_{s,x}(X_s)\,ds.
\tag{18}
\]
The integrand is progressive: \(X\) has continuous adapted coordinates and \(b\) is jointly Borel. The processes \(\beta(x)\) are continuous and adapted, with
\[
\|\beta_t(x)-\beta_s(x)\|_2
\le\sqrt{|t-s|}+|t-s|.
\tag{19}
\]
Indeed, \(\beta(x)=B(x)+\int(\eta_x-b_{s,x}(X_s))\,ds\), and the latter integrand lies in \([-1,1]\). Thus \(\beta(x)\) is square-integrable and \(L^1\)-continuous.

For \(u<v\), Brownian increments have zero conditional mean given \(\mathcal F_u^0\), since
\[
\mathcal F_u^0
\subseteq \sigma(\eta,B_s(z):s\le u,\ z\in W).
\]
Conditional Fubini, (17), and the tower property give
\[
\begin{aligned}
\mathbb E[\beta_v(x)-\beta_u(x)\mid\mathcal F_u^0]
&=(v-u)\mathbb E[\eta_x\mid\mathcal F_u^0]\\
&\quad-\int_u^v
\mathbb E[b_{s,x}(X_s)\mid\mathcal F_u^0]\,ds
=0.
\end{aligned}
\tag{20}
\]
Thus every \(\beta(x)\) is a martingale for the same raw filtration.

Let \(\mathcal N\) contain all ambient null sets, and set
\[
\overline{\mathcal F}_t^0=\mathcal F_t^0\vee\mathcal N,
\qquad
\mathcal F_t=\bigcap_{r>t}\overline{\mathcal F}_r^0.
\tag{21}
\]
This filtration is complete and right-continuous. To check that the martingale property survives, fix \(s<t\) and choose \(s_k\downarrow s\), with \(s_k<t\). Then
\[
\mathbb E[\beta_t(x)\mid\overline{\mathcal F}_{s_k}^0]
=\beta_{s_k}(x).
\]
Lévy’s downward theorem applies to conditional expectations of the fixed integrable variable \(\beta_t(x)\). The left side converges in \(L^1\) to
\(\mathbb E[\beta_t(x)\mid\mathcal F_s]\); by (19), the right side converges to \(\beta_s(x)\). Hence all coordinates remain martingales for this one usual filtration. :chatgpt-content-reference{index="2"}

Since \(\beta(x)-B(x)\) has continuous finite variation, quadratic covariations satisfy
\[
[\beta(x),\beta(y)]_t=\mathbf1_{\{x=y\}}t.
\tag{22}
\]
For any finite list of distinct vertices, the corresponding vector \(\beta\) is a continuous martingale starting at zero with bracket \(tI\). These are the hypotheses of the vector Lévy characterization. :chatgpt-content-reference{index="3"}

In detail, Itô’s formula makes
\[
\exp\!\left(i\theta\cdot\beta_t+\frac12|\theta|^2t\right)
\]
a local martingale. Its modulus is bounded on each fixed time interval, so it is a true martingale, giving
\[
\mathbb E\!\left[
e^{i\theta\cdot(\beta_t-\beta_s)}
\mid\mathcal F_s
\right]
=e^{-|\theta|^2(t-s)/2}.
\tag{23}
\]
Thus every finite vector has independent Gaussian increments and independent coordinate **paths**, not merely zero pairwise covariance. Countability of \(W\) implies that \((\beta(x))_{x\in W}\) has product Wiener law.

By (18), \(X\) solves (13) with input \(\beta\). The pathwise uniqueness already proved gives
\[
X=\mathcal Z(\beta).
\tag{24}
\]
Consequently, applying \(\mathcal Z\) to iid Brownian paths on \(W\) gives exactly the observation-process law (14). No infinite-product Girsanov density or weak-to-strong existence theorem is needed.

## 6. One Uniform per vertex and the same-noise limit

Fix a total Borel map
\[
\Psi:[0,1]\longrightarrow\mathcal C
\]
sending Lebesgue measure to Wiener measure. Here is a direct construction sufficient to verify totality.

Use terminating binary expansions at dyadic points, and a fixed digit sequence at \(1\). Split the digits into countably many disjoint subsequences, giving independent Uniform variables under Lebesgue measure. Apply the normal quantile, defining it to be zero at exceptional endpoints. Use disjoint normals for successive unit-interval increments and dyadic bridge midpoints. On a dyadic interval \([a,b]\), assign the midpoint the average of its endpoints plus \(\sqrt{b-a}\,G/2\).

At refinement level \(k\) in a unit interval, the interpolant changes in sup norm by at most
\[
2^{-k/2-1}\max_{j<2^k}|G_{k,j}|.
\]
The probability that the maximum exceeds \(k+1\) is at most
\[
2^{k+1}e^{-(k+1)^2/2},
\]
a summable sequence. Thus the interpolants converge uniformly almost surely, simultaneously on all countably many unit intervals. Gaussian midpoint conditioning verifies Brownian finite-dimensional distributions; independent unit segments concatenate to Brownian motion on \([0,\infty)\).

The set where the successive sup-norm differences are summable on every unit interval is Borel and has full measure. Take the continuous limit there and the zero path on its complement. Rational-time evaluations establish that \(\Psi\) is total Borel.

For every \(u\in[0,1]^W\), put \(w(x)=\Psi(u_x)\) and define
\[
f_n(w)_x=\mathbf1_{\{\mathcal Z(w)_n(x)>n/2\}},
\qquad
F(u)_x=\liminf_{n\to\infty}f_n(w)_x.
\tag{25}
\]
A binary liminf always belongs to \(\{0,1\}\). All these maps are Borel. They commute with the action on **every input**, including exceptional labels: the encoding is identical at every site, and \(\mathcal Z\) is exactly equivariant.

In the auxiliary coupling, (24) implies
\[
\mathbb P\{f_n(\beta)_x\ne\eta_x\}
=\mathbb P\{N(0,1)>\sqrt n/2\}
\le e^{-n/8}.
\tag{26}
\]
Conditional on either value of \(\eta_x\), the error is the appropriate one-sided tail of \(B_n(x)\); ties have probability zero.

The bound is summable. Borel–Cantelli gives eventual equality for each vertex, and countability gives this simultaneously at every vertex. No common finite stabilization time is asserted.

Crucially, the input is the **same iid field \(\beta\)** for every \(n\). In particular,
\[
\mathbb P\{f_{n+1}(\beta)_x\ne f_n(\beta)_x\}
\le e^{-n/8}+e^{-(n+1)/8}.
\tag{27}
\]
This proves a same-noise limit, not merely convergence of distributions. For every finite \(S\), the coupling error on \(S\) at time \(n\) is at most \(|S|e^{-n/8}\).

Since \(\beta\) has product Wiener law and \(\Psi\) encodes that law site by site, the pushforward in (25) is \(\mu\). In particular,
\[
\boxed{\mathbb P\{F(U)|_S=1\}=\det Q_S}
\tag{28}
\]
for every finite \(S\subset W\). For disjoint finite \(A,B\subset W\), the complete pattern probabilities are
\[
\boxed{
\mathbb P\{F(U)|_A=1,\ F(U)|_B=0\}
=\sum_{J\subset B}(-1)^{|J|}\det Q_{A\cup J}.
}
\tag{29}
\]
These identify exactly \(\mathbf P^Q\) and prove the frozen statement. \(\square\)

## Attribution and source distinction

Nam–Sly–Zhang, arXiv:2012.09484v2, Section 2.2, equations (2.3)–(2.4) and Lemma 2.1, supply the observation strategy: posterior-mean drift, the weak observation solution \(t\tau+B_t\), and recovery of spins from a Brownian-driven solution. Their spins are \(\pm1\), so the quadratic likelihood term is constant; for the present \(0/1\) variables, it produces the essential \(-t/2\) in (9). Their tree/Ising convergence estimates and main theorem are not applied here. :chatgpt-content-reference{index="4"}

The generating polynomial, singular-safe tilt, and covariance bound are finite DPP algebra, derived in Section 2. The threshold exhaustion was proposed in the seed and verified in Section 1. The generalization established here is their combination with component independence, a total infinite drift, a causal all-input solution, and a same-noise factor for the arbitrary action in the statement. No priority, finitary-coding, or isomorphism assertion is made.

The source distinction is substantive. For example, let \(\Gamma=\mathbb Z^2\) act on \(W=\mathbb Z\) through the first coordinate, and take \(Q=pI\), \(0<p<1\). The \(W\)-indexed factor is simply coordinatewise thresholding. A regular \(\Gamma\)-indexed factor cannot produce this law: its output coordinate would be invariant under the vertical shift, while that shift on the regular iid source is mixing, hence ergodic. Mixing follows by separating finite-coordinate cylinder events and then approximating arbitrary events. An invariant output bit must therefore be deterministic, contradicting its required Bernoulli-\(p\) law.

## Delivery

:chatgpt-content-reference{index="6"}[**q77r05g4-001.zip**](sandbox:/mnt/data/q77r05g4-001.zip) contains only files under `research/q77r05/g4/`, including :chatgpt-content-reference{index="7"}[RESULT.md](sandbox:/mnt/data/research/q77r05/g4/RESULT.md), :chatgpt-content-reference{index="8"}[REFERENCES.md](sandbox:/mnt/data/research/q77r05/g4/REFERENCES.md), the detailed supplement, and exact finite checks. The checks passed for eight kernels and thirty-two positive tilts; they supplement the proof rather than replace it.

**PR #85 was not updated, and no separate PR was opened.** The GitHub connector was not installed, and the read-only Git access attempt failed with `Could not resolve host: github.com`. No remote changes or merges were made.