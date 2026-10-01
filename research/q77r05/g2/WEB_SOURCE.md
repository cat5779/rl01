PROVED

**Theorem.** For every countable permutation action \(\Gamma\curvearrowright W\) and every commuting Hermitian positive contraction \(Q\) on \(\ell^2(W)\), there is a total Borel, everywhere \(\Gamma\)-equivariant map
\[
F:[0,1]^W\longrightarrow\{0,1\}^W,
\qquad F_*\mathrm{Leb}^W=\mathbf P^Q.
\]
The source is indexed by \(W\). No lower spectral bound or stabilizer hypothesis is needed.

I prove the following sampler criterion and verify its hypotheses for the DPP.

**Sampler criterion.** Suppose an invariant binary law \(\mu\) has an equivariant partition into classes \(C(x)\), with jointly independent restrictions to different classes. Suppose there are finite, increasing, equivariant sets \(x\in E_n(x)\uparrow C(x)\). For every positive external-field tilt of the **actual marginal** \(\mu_{E_n(x)}\), assume
\[
\sum_{z\in E_n(x)}
\left|\operatorname{Cov}(\eta_x,\eta_z)\right|\le L<\infty,
\tag{1}
\]
uniformly in the field, \(x\), and \(n\). Then \(\mu\) has such a total \(W\)-indexed factor.

## 1. Singular complex kernels survive every positive tilt

Let \(0\le K\le I\) be a finite Hermitian kernel. Its generating polynomial is
\[
G_K(z)=\mathbb E\prod_jz_j^{\eta_j}
      =\det(I-K+K\operatorname{diag}z).
\tag{2}
\]
This follows by expanding \(\prod_j[1+(z_j-1)\eta_j]\) and using the inclusion determinants; it is also Lyons’s equation (2.11), which does **not** require \(\|K\|<1\). :chatgpt-content-reference{index="0"}

For an arbitrary finite real field \(h\), put
\[
D=\operatorname{diag}(e^{h_j/2}),\quad U=DK^{1/2},\quad
R=I-K+U^*U.
\]
Writing \(m=\min_j e^{h_j}>0\),
\[
R\ge I-K+mK\ge\min(1,m)I.
\]
Thus
\[
H=UR^{-1}U^*
\tag{3}
\]
is defined even when \(K\) has eigenvalues \(0\) or \(1\). Moreover, \(R\ge U^*U\) implies \(\|UR^{-1/2}\|\le1\), hence \(0\le H\le I\).

For \(V=\operatorname{diag}z\), the determinant identity \(\det(I+AB)=\det(I+BA)\) gives
\[
\frac{G_K(e^hz)}{G_K(e^h)}
=\frac{\det(R+U^*(V-I)U)}{\det R}
=\det(I+H(V-I)).
\tag{4}
\]
Therefore the tilted law is precisely \(\mathbf P^H\).

Differentiating its finite positive partition sum gives
\[
\partial_{h_j}\mathbb E_h\eta_i
=\operatorname{Cov}_h(\eta_i,\eta_j).
\]
For \(p=H_{ii}\), the DPP determinants give variance \(p(1-p)\) and, for \(j\ne i\), covariance \(-|H_{ij}|^2\). Consequently
\[
\begin{aligned}
\sum_j|\operatorname{Cov}_h(\eta_i,\eta_j)|
&=p+(H^2)_{ii}-2p^2\\
&\le2p(1-p)\le\tfrac12.
\end{aligned}
\tag{5}
\]
This proves the required uniform bound, including deterministic bits and complex entries, without inverting \(I-K\).

## 2. The canonical finite sets and component independence

For the infinite kernel,
\[
\sum_y|Q(x,y)|^2=(Q^2)_{xx}\le Q_{xx}\le1.
\]
Thus the graph \(D_n\), joining distinct sites with \(|Q(x,y)|\ge1/n\), has degree at most \(n^2\). Its radius-\(n\) balls \(E_n(x)\) are finite, nested, and equivariant. Every finite path of nonzero kernel entries belongs to some \(D_n\) and has length at most some sufficiently large \(n\). Hence their union is exactly \(C(x)\).

Entries between different components vanish. To prove **sigma-field independence**, not just zero covariance, take finite disjoint occupied and vacant requirements \(A,B\). Inclusion-exclusion gives
\[
\mathbb P(A\subseteq\eta,\ B\cap\eta=\varnothing)
=\sum_{J\subseteq B}(-1)^{|J|}\det Q[A\cup J].
\tag{6}
\]
Each determinant factors over components. The finite sum therefore factors into the corresponding exact-pattern probabilities in those components. Cylinder events generate their sigma-fields; the monotone-class theorem proves joint independence, including independence of one entire component from all the others. Countably many infinite components cause no change.

The marginal on every finite \(E\) has compressed kernel \(Q_E\), again a Hermitian positive contraction. Thus (5) verifies (1) with \(L=1/2\). Invariance follows from the invariant inclusion determinants. All hypotheses of the sampler criterion are now verified.

## 3. The limsup drift and an all-input causal solution

For the general criterion, let \(\mu_{E,h}\) denote the normalized tilt by \(e^{\sum_{z\in E}h_z\eta_z}\). Define exactly as proposed
\[
b^n_{t,x}(y)=
\mathbb E_{\mu_{E_n(x),\,y|_{E_n(x)}-(t/2)\mathbf1}}\eta_x,
\qquad
b_{t,x}(y)=\limsup_n b^n_{t,x}(y).
\tag{7}
\]
Finite partition sums have positive denominators everywhere. Thus \(b\) is jointly Borel in time and the product real-field space, takes values in \([0,1]\), and is exactly equivariant on **every** field.

The covariance derivative and (1) imply
\[
|b^n_{t,x}(y)-b^n_{t,x}(y')|
\le L\max_{z\in E_n(x)}|y_z-y'_z|.
\]
When \(d=\sup_z|y_z-y'_z|<\infty\), both inequalities
\(b^n(y)\le b^n(y')+Ld\) and their reversals hold for every \(n\). Taking limsups therefore gives
\[
\sup_x|b_{t,x}(y)-b_{t,x}(y')|
\le L\sup_z|y_z-y'_z|.
\tag{8}
\]
**The fields themselves need not be bounded.** No everywhere convergence of the finite posteriors is asserted.

Let \(\mathcal C=C_0([0,\infty),\mathbb R)^W\). For any \(w\in\mathcal C\), set \(z^0=w\) and
\[
z^{k+1}_t(x)=w_t(x)+\int_0^t b_{s,x}(z^k_s)\,ds.
\tag{9}
\]
These are scalar coordinatewise Lebesgue integrals; no Bochner measurability in \(\ell^\infty\) is assumed. Joint Borel measurability gives measurable integrands and parameterized integrals. Each coordinate path is continuous.

Since \(0\le b\le1\), each correction \(z^{k+1}_t(x)-w_t(x)\) lies in \([0,t]\). Inequality (8) and induction yield, for every input,
\[
\sup_x\sup_{r\le t}|z^{k+1}_r(x)-z^k_r(x)|
\le\frac{L^kt^{k+1}}{(k+1)!}.
\tag{10}
\]
Thus the iterates converge on every finite horizon, uniformly in their coordinate differences. The limit \(\Phi(w)\) solves
\[
z_t(x)=w_t(x)+\int_0^t b_{s,x}(z_s)\,ds.
\tag{11}
\]
Indeed, (8) permits passage of the integrands to the limit. Rational-time evaluations of every iterate are Borel; they generate the Borel structure of continuous paths. Hence \(\Phi\) is total Borel. Iteration also proves exact equivariance and causality.

For two solutions with the same input, put
\[
D(t)=\sup_x\sup_{r\le t}|z_r(x)-z'_r(x)|.
\]
Their corrections lie in \([0,r]\), so \(D(t)\le t\), and their equations imply
\(D(t)\le L\int_0^tD(s)\,ds\). Iterating this inequality makes \(D(t)=0\).

The uniqueness class is therefore **all coordinatewise continuous solutions, for every input**, without an adaptation or invariant-coupling restriction.

In fact, the total Borel causal map
\[
T_b(v)_t(x)=v_t(x)-\int_0^t b_{s,x}(v_s)\,ds
\tag{12}
\]
satisfies
\[
T_b\Phi=\mathrm{id},\qquad \Phi T_b=\mathrm{id}.
\tag{13}
\]
The construction is an all-input causal bijection of path spaces, not a selection made on a posterior conull set.

## 4. Conditioning on the complete observation past

Independently sample \(\eta\sim\mu\) and iid standard Brownian motions \(B(x)\), and set
\[
X_t(x)=t\eta_x+B_t(x),\qquad
\mathcal H_t^0=\sigma(X_r(z):z\in W,\ 0\le r\le t).
\]
For fixed \(t>0\) and finite \(E\), Gaussian Bayes gives likelihood proportional to
\[
\exp\!\left(\sum_{z\in E}(X_t(z)-t/2)\eta_z\right),
\]
because \(\eta_z^2=\eta_z\). Thus
\[
b^n_{t,x}(X_t)
=\mathbb E[\eta_x\mid X_t(z):z\in E_n(x)].
\tag{14}
\]
The conditioning sigma-fields increase to the endpoint observations on \(C(x)\). Upward conditional-expectation convergence applies to the bounded variable \(\eta_x\), so their almost-sure limit is the conditional mean on that component. These are exactly the hypotheses of Lyons’s Theorem 35.6. :chatgpt-content-reference{index="1"}

Independence of the pairs \((\eta|_C,B|_C)\) across components then gives
\[
b_{t,x}(X_t)=\mathbb E[\eta_x\mid X_t(z):z\in W].
\tag{15}
\]

For this fixed \(t\), the bridges
\[
R^t_r(z)=X_r(z)-(r/t)X_t(z)
=B_r(z)-(r/t)B_t(z),\quad r\le t,
\]
are jointly independent of \((\eta,X_t)\). For finitely many coordinates and times this follows from Gaussian zero cross-covariance with the endpoints and independence from \(\eta\). Countability and rational evaluations of continuous paths extend the independence to the entire bridge family. Since
\[
\mathcal H_t^0=\sigma(X_t,(R^t_r(z))_{r\le t,z\in W}),
\]
we obtain
\[
b_{t,x}(X_t)=\mathbb E[\eta_x\mid\mathcal H_t^0]
\quad\text{a.s. for each deterministic }t.
\tag{16}
\]
At \(t=0\), both sides equal the unconditioned mean.

The left side is bounded and progressively measurable, since \(X\) has continuous adapted coordinates and \(b\) is jointly Borel. Thus (16) also supplies the required \(dt\otimes d\mathbb P\) version. No infinite-product Girsanov density, or simultaneous all-field posterior assertion, is involved.

## 5. Joint Brownian innovations and usual augmentation

Define
\[
\beta_t(x)=X_t(x)-\int_0^t b_{r,x}(X_r)\,dr.
\tag{17}
\]
For bounded \(\mathcal H_s^0\)-measurable \(V\), the increment \(B_t(x)-B_s(x)\) has zero expectation against \(V\): the observed past is contained in the joint past of \(\eta\) and all the Brownian motions. For \(r\ge s\), (16) gives
\[
\mathbb E[V(\eta_x-b_{r,x}(X_r))]=0.
\]
Fubini therefore proves that \(\beta(x)\) is a martingale in the **whole raw observation filtration**.

Let
\[
\mathcal H_t=\bigcap_{u>t}(\mathcal H_u^0\vee\mathcal N)
\]
be its usual augmentation. Each \(\beta(x)\) is continuous, square integrable, and \(L^2\)-continuous, since it differs from \(B(x)\) by a time-Lipschitz drift bounded in absolute value by \(t\). For \(t_n\downarrow t\), with \(t_n<T\), reverse conditional-expectation convergence gives
\[
\begin{aligned}
\mathbb E[\beta_T(x)\mid\mathcal H_t]
&=\lim_n\mathbb E[\beta_T(x)\mid\mathcal H_{t_n}^0\vee\mathcal N]\\
&=\lim_n\beta_{t_n}(x)=\beta_t(x).
\end{aligned}
\tag{18}
\]
The decreasing sigma-fields and integrable terminal variable meet Theorem 35.9’s hypotheses. This proves preservation under augmentation rather than presuming trivial right germs. :chatgpt-content-reference{index="2"}

Finite variation does not change quadratic covariations, so
\[
[\beta(x),\beta(y)]_t=\mathbf1_{\{x=y\}}t.
\tag{19}
\]
Every finite vector \(\beta|_A\) is consequently a continuous local martingale, starting at zero, with bracket \(tI\), in the **same** usual filtration. This is precisely the common-filtration vector Lévy characterization, Sznitman’s Theorem 6.10. :chatgpt-content-reference{index="3"}

Explicitly, Itô’s formula makes
\(\exp(i\theta\cdot\beta_t|_A+|\theta|^2t/2)\) a local martingale. Its modulus is bounded on bounded horizons, so
\[
\mathbb E\!
\left[e^{i\theta\cdot(\beta_t|_A-\beta_s|_A)}\mid\mathcal H_s\right]
=e^{-|\theta|^2(t-s)/2}.
\tag{20}
\]
This proves jointly independent Gaussian future increments relative to the common past. Finite-site and finite-time consistency show that the **entire coordinate paths** \(\beta(x)\) are iid Brownian motions.

There is also no residual augmentation gap in the posterior statement. By (13), \(X=\Phi(\beta)\), and the raw filtrations of \(X\) and \(\beta\) coincide. The completed raw natural filtration of a countable Brownian field is right-continuous: check right-limit conditional expectations first on bounded continuous cylinders involving finitely many sites and times. The conditional Gaussian means converge by path continuity, and their finite covariance matrices converge. Bounded convergence gives \(L^1\) convergence; cylinder density and reverse martingale convergence extend it to every integrable path variable. Applying this to event indicators identifies the right-limit sigma-field with the completed time-\(t\) raw sigma-field. Hence (16) holds with \(\mathcal H_t\) as well, at each deterministic time and in \(dt\otimes d\mathbb P\).

## 6. Recovering the configuration and total Uniform coding

Equations (13) and (17) identify the entire observation path as \(X=\Phi(\beta)\). Since \(\beta\) has product Wiener law, \(\Phi\) sends that law to the law of \(t\eta+B_t\).

For **every** path input define
\[
\Theta(w)_x=\liminf_{n\to\infty}
\mathbf1\{\Phi(w)_n(x)>n/2\}.
\tag{21}
\]
A binary liminf is always defined and binary. Thus \(\Theta\) is total Borel and exactly equivariant. In the observation coupling,
\[
\mathbb P\!\left(\mathbf1\{X_n(x)>n/2\}\ne\eta_x\right)
\le e^{-n/8}.
\tag{22}
\]
Indeed, condition on \(\eta_x\) and apply the Gaussian exponential bound to \(B_n(x)\) at \(\pm n/2\). Summability and Borel–Cantelli, followed by a countable intersection over \(x\), give \(\Theta(\beta)=\eta\) almost surely.

For completeness, a total Borel Uniform-to-Wiener encoder can be constructed without a measurable-selection assumption. Split one Uniform label’s binary digits into countably many independent Uniform streams and Gaussianize them. On each unit interval start with a Gaussian endpoint and recursively fill dyadic midpoints using the average of their endpoints plus an independent Gaussian of variance \(2^{-(m+2)}\) at level \(m\). Consecutive polygonal interpolations differ in supremum norm by
\[
2^{-(m+2)/2}\max_{k<2^m}|G_{m,k}|.
\]
The bound
\(\mathbb P(\max|G_{m,k}|>m+1)\le2^{m+1}e^{-(m+1)^2/2}\)
is summable, proving uniform convergence almost surely. Refining an increment of variance \(\ell\) splits it into
\(\Delta/2\pm\sqrt\ell G/2\), two independent Gaussian increments of variance \(\ell/2\). Thus the continuous limit has Brownian law. Concatenate independent unit intervals. The uniform-Cauchy set is Borel; assign the zero path on its complement and fix binary-expansion endpoint conventions. This produces a total Borel encoder \(e\).

Now
\[
F(u)=\Theta((e(u_x))_{x\in W})
\tag{23}
\]
has the required law. Using the identical encoder at each site and the exact equivariance of all subsequent operations proves \(F(gu)=gF(u)\) on **all** inputs. This completes the sampler criterion and its DPP application.

## 7. The requested stress cases

For the complex singular projection
\[
P=\tfrac12\begin{pmatrix}1&i\\-i&1\end{pmatrix},
\]
a positive tilt gives first-site probability \(p=e^{h_1}/(e^{h_1}+e^{h_2})\). Its covariance absolute row sum is exactly \(2p(1-p)\), attaining \(1/2\). Thus the estimate remains sharp at projections; there is no degenerating coercivity constant. Deterministic coordinates have zero covariance rows. Countably many disconnected projection blocks, even with edge sizes tending to zero, are covered by the proved component independence and rootwise exhaustion.

An explicitly noncommensurated example is the countable group of finitely supported permutations of \(\mathbb N\). Its stabilizer of \(0\) has infinite-index intersection with its conjugate fixing \(1\). Any commuting bounded kernel has constant off-diagonal entries, which square summability forces to vanish; hence \(Q=pI\). The action requires no additional hypothesis. In general, the proof uses only the finite balls produced by the kernel.

Arbitrary spatially unbounded path fields remain valid inputs to (9)–(13): only the bounded corrections and their differences enter the estimates. No posterior conull set is used to define the solver.

The source distinction matters. For \(\Gamma=\mathbb Z\) acting trivially on a singleton, \(Q=[p]\), \(0<p<1\), the stated \(W\)-source supplies a random bit. A regular-\(\mathbb Z\) source could not: its equivariant output would be shift invariant and thus constant by Bernoulli-shift ergodicity. That ergodicity follows by approximating an invariant event with finite-coordinate cylinders and translating them to disjoint coordinates. No regular-source assertion is made here.

The observation mechanism appears in Nam–Sly–Zhang, §2 and Lemma 2.1. Their tree/Ising theorem is not used as a general-action theorem, and no originality conclusion is claimed. :chatgpt-content-reference{index="4"}

### Publication

GitHub publication failed: the GitHub integration was not installed, and `git ls-remote` failed to resolve `github.com`. PR #86 was not updated; nothing was pushed or merged.

The verified archive contains only `research/q77r05/g2/RESULT.md` and `REFERENCES.md`, including expanded details and the external-theorem hypothesis audit:

:chatgpt-content-reference{index="6"}[RESULT.md](sandbox:/mnt/data/q77r05g2-001/research/q77r05/g2/RESULT.md) · :chatgpt-content-reference{index="7"}[REFERENCES.md](sandbox:/mnt/data/q77r05g2-001/research/q77r05/g2/REFERENCES.md) · :chatgpt-content-reference{index="8"}[q77r05g2-001.zip](sandbox:/mnt/data/q77r05g2-001.zip)