INCOMPLETE

The hypotheses are sufficient for **ordinary weak existence with the prescribed marginals**, including coordinatewise càdlàg pure-birth paths, local integrability, and absence of simultaneous jumps. I do not have a proof of the remaining \(\Gamma\)-invariance assertion for an arbitrary countable group, nor a counterexample satisfying the DPP/rate hypotheses. The exact unresolved step is identified below.

### 1. Uniform finite-pattern positivity

Put
\[
E=\{0,1\}^{\Gamma}.
\]
For finite \(F\Subset\Gamma\), let \(K_{t,F}\) be the compression of \(K_t\) to \(\ell^2(F)\). The gap gives
\[
\varepsilon I_F\le K_{t,F}\le (1-\varepsilon)I_F.
\]
For \(A\subset F\), the exact-pattern probability of the finite DPP is
\[
\mu_t(X\cap F=A)
 =\det(I-K_{t,F})\det\!\left(
 [K_{t,F}(I-K_{t,F})^{-1}]_A
 \right).
\]
All eigenvalues of \(I-K_{t,F}\) are at least \(\varepsilon\), while all eigenvalues of
\[
L_{t,F}=K_{t,F}(I-K_{t,F})^{-1}
\]
are at least \(\varepsilon/(1-\varepsilon)\). Hence, uniformly in \(t\),
\[
\mu_t(X_F=y)\ge c_F>0
\qquad(y\in\{0,1\}^F).
\tag{1}
\]
For example one may take
\[
c_F=\varepsilon^{|F|}
 \left(\frac{\varepsilon}{1-\varepsilon}\right)^{|F|}.
\]

Also \(t\mapsto\mu_t\) is weakly continuous: every finite-dimensional DPP probability is a continuous function of the matrix entries of \(K_{t,F}=C_F+tH_F\). Equivariance of \(K_t\) makes every \(\mu_t\) \(\Gamma\)-invariant.

Let
\[
m_i(t)=\int_E a_i(t,x)\,\mu_t(dx).
\]
By covariance and transitivity, the \(m_i\)'s agree; write \(m(t)\). The hypothesis gives
\[
\int_0^1m(t)\,dt<\infty.
\tag{2}
\]

### 2. Canonical finite-dimensional projected equations

For finite \(F\) and \(i\in F\), define
\[
\alpha_i^F(t,y)
 =
 \frac{\displaystyle
 \int_{\{x_F=y\}}a_i(t,x)\,\mu_t(dx)}
 {\mu_t(X_F=y)} .
\tag{3}
\]
This is jointly Borel in \((t,y)\). If \(y_i=1\), it is zero. By (1),
\[
0\le\alpha_i^F(t,y)\le \frac{m(t)}{c_F},
\tag{4}
\]
so every finite-state rate is time-integrable.

If \(\varphi\) is any function on \(\{0,1\}^F\), the assumed cylinder continuity equation becomes
\[
\mu_t^F(\varphi)-\mu_0^F(\varphi)
 =
 \int_0^t
 \mu_s^F\!\left[
 \sum_{i\in F}\alpha_i^F(s,\cdot)
 \bigl(\varphi(\cdot^{\,i,+})-\varphi(\cdot)\bigr)
 \right]ds.
\tag{5}
\]
Thus \(\mu_t^F\) solves the finite-state forward equation for the pure-birth generator
\[
L_t^F\varphi(y)
 =
 \sum_{i\in F}\alpha_i^F(t,y)
 [\varphi(y^{i,+})-\varphi(y)].
\]

Because the finite rate matrix has an \(L^1\)-in-time operator norm by (4), its forward integral equation is unique. Therefore the inhomogeneous finite-state pure-birth chain with initial law \(\mu_0^F\) has, at every time,
\[
\operatorname{Law}(X_t^F)=\mu_t^F.
\tag{6}
\]
It has at most \(|F|\) jumps and no simultaneous jumps.

This does **not** assert projective consistency; indeed the family \(P_F\) need not be projectively consistent.

### 3. Passage to an ordinary infinite-dimensional weak solution

Choose
\[
F_1\subset F_2\subset\cdots,\qquad \bigcup_nF_n=\Gamma.
\]
Represent a monotone binary coordinate path by a birth time
\[
T_i\in B:=[0,1]\cup\{\infty\},
\qquad
X_i(t)=1_{\{T_i\le t\}},
\]
where \(T_i=0\) denotes initial occupancy. The product \(B^\Gamma\) is compact metrizable.

Put the \(F_n\)-chain from §2 on \(B^{F_n}\) and set \(T_i=\infty\) outside \(F_n\). By compactness a subsequence of the resulting laws \(P_n\) converges weakly to some \(P\).

For every fixed \(i\), once \(i\in F_n\),
\[
P_n(T_i=0)=K_0(i,i),
\]
and, for \(0\le s<t\le1\),
\[
P_n(s<T_i\le t)
 =K_t(i,i)-K_s(i,i)
 =(t-s)H(i,i).
\tag{7}
\]
Consequently the limiting birth-time distribution has no atoms in \((0,1]\). For every finite \(S\) and every \(t>0\), evaluation \(T\mapsto X_t^S\) is therefore \(P\)-a.s. continuous. Using (6),
\[
\operatorname{Law}_P(X_t^S)=\mu_t^S.
\tag{8}
\]
At \(t=0\), (7) gives
\[
P(0<T_i\le\delta)=\delta H(i,i),
\]
so comparison with \(X_\delta^S\), followed by \(\delta\downarrow0\), yields the same assertion at zero. Hence
\[
X_t\sim\mu_t\quad\text{for every }t\in[0,1].
\tag{9}
\]

Now introduce the finite measure
\[
\rho(dt,dx)=dt\,\mu_t(dx).
\]
For fixed \(i\),
\[
\alpha_i^{F_n}(t,x_{F_n})
 =
 E_\rho\!\left[a_i(t,X)\mid
 \sigma(t,X_j:j\in F_n)\right].
\]
The increasing \(\sigma\)-fields exhaust
\(\mathcal B([0,1])\otimes\mathcal B(E)\), and \(a_i\in L^1(\rho)\). Therefore
\[
\|\alpha_i^{F_n}-a_i\|_{L^1(\rho)}
 \longrightarrow0.
\tag{10}
\]

Let \(f\) be supported by a finite set \(S\). For large \(n\),
\[
M_t^{n,f}
 =
 f(X_t)-f(X_0)
 -
 \int_0^t\sum_{i\in S}
 \alpha_i^{F_n}(r,X_r)
 \Delta_i f(X_r)\,dr
\tag{11}
\]
is a martingale under \(P_n\).

Fix first \(F_m\supset S\). Since \(P_n(X_r^{F_n}\in\cdot)=\mu_r^{F_n}\),
\[
E_{P_n}\!\int_0^1
 |\alpha_i^{F_n}(r,X_r)-\alpha_i^{F_m}(r,X_r)|\,dr
 =
 \|\alpha_i^{F_n}-\alpha_i^{F_m}\|_{L^1(\rho)}.
\tag{12}
\]
By (10), its \(n\to\infty\) limit is at most
\[
\|a_i-\alpha_i^{F_m}\|_{L^1(\rho)},
\]
which tends to zero as \(m\to\infty\).

For fixed \(m\), \(\alpha_i^{F_m}(t,y)\) is a function of finitely many coordinates and is \(L^1\) in \(t\); (4) supplies an \(L^1(dt)\) majorant on each finite-state atom. Approximate these finitely many time-functions in \(L^1\) by bounded continuous functions. For such an approximation,
\[
T\longmapsto\int_s^t h(r,X_r^{F_m})\,dr
\]
is continuous on birth-time space: if birth times converge, the corresponding binary paths converge for Lebesgue-a.e. \(r\), and dominated convergence applies.

Consequently one may pass (11) to the weak limit after multiplication by any bounded cylinder function of the history up to \(s\). Then (12) and \(m\to\infty\) give
\[
E_P\!\left[
G\left(
f(X_t)-f(X_s)
-\int_s^t L_r f(X_r)\,dr
\right)\right]=0
\tag{13}
\]
for every bounded history-cylinder \(G\). A monotone-class argument gives the martingale property in the natural filtration. Since the set of global jump times is countable pathwise,
\[
L_r f(X_r)=L_r f(X_{r-})
\quad dr\text{-a.e.}
\]
and hence the required form follows:
\[
f(X_t)-f(X_0)
-\int_0^tL_s f(X_{s-})\,ds
\quad\text{is a martingale.}
\tag{14}
\]

Thus **ordinary weak existence is established**.

### 4. Local integrability and path regularity

From (9) and Tonelli,
\[
E_P\int_0^1a_i(t,X_t)\,dt
 =
 \int_0^1m(t)\,dt<\infty.
\tag{15}
\]
Therefore the integral is finite almost surely. The same holds with \(X_{t-}\).

For a cylinder \(f\) supported by \(S\),
\[
|L_tf(x)|
 \le2\|f\|_\infty\sum_{i\in S}a_i(t,x),
\tag{16}
\]
so its compensator is integrable.

The formal jump kernel is
\[
q_t(x,dy)
 =
 \sum_{i\in\Gamma}a_i(t,x)\,
 \delta_{x^{i,+}}(dy).
\tag{17}
\]
It is a Borel \(\sigma\)-finite kernel: each summand is Borel, every coefficient is finite, and there are countably many summands. Its total mass may be infinite, but a cylinder test sees only finitely many coordinates, exactly as (16) records.

Every coordinate has the birth-time form, hence jumps at most once. Moreover, if
\[
d(x,y)=\sum_{n\ge1}2^{-n}|x_{\gamma_n}-y_{\gamma_n}|
\]
for an enumeration \((\gamma_n)\) of \(\Gamma\), then every such monotone path is actually \(d\)-càdlàg: right continuity and existence of left limits follow from coordinatewise convergence plus dominated convergence in the summable weights. Thus no spatially invariant metric is being smuggled into the construction; the weighted metric is used only to describe the product topology.

### 5. Simultaneous jumps do not occur

For a coordinate \(i\), (14) with \(f(x)=x_i\) gives
\[
M_i(t)
 =
 X_i(t)-X_i(0)
 -
 A_i(t),
\qquad
A_i(t)=\int_0^t a_i(s,X_{s-})\,ds,
\tag{18}
\]
a martingale.

For \(i\ne j\), the generator applied to \(x_ix_j\) is
\[
L_t(x_ix_j)
 =a_i(t,x)x_j+a_j(t,x)x_i.
\]
Hence
\[
M_{ij}(t)
 =
 X_i(t)X_j(t)-X_i(0)X_j(0)
 -
 \int_0^t
 [a_iX_{j-}+a_jX_{i-}]\,ds
\tag{19}
\]
is a martingale.

Integration by parts for the two counting processes gives
\[
X_i(t)X_j(t)-X_i(0)X_j(0)
 =
 \int_0^tX_{i-}\,dX_j
 +\int_0^tX_{j-}\,dX_i
 +S_{ij}(t),
\]
where
\[
S_{ij}(t)
 =\sum_{0<s\le t}\Delta X_i(s)\Delta X_j(s).
\]
Using \(dX_i=dM_i+dA_i\) and comparing with (19),
\[
S_{ij}
 =
 M_{ij}
 -\int X_{i-}\,dM_j
 -\int X_{j-}\,dM_i.
\tag{20}
\]
After the usual localization, the right side is a local martingale. But \(S_{ij}\) is nonnegative and nondecreasing with \(S_{ij}(0)=0\). Hence
\[
S_{ij}\equiv0\quad\text{a.s.}
\tag{21}
\]
A countable union over pairs shows that no two coordinates jump simultaneously. In particular, an infinite simultaneous jump is impossible. Equation (7) also shows that there are no jumps at any prescribed deterministic \(t>0\).

These conclusions required neither a Poisson construction nor strong/pathwise uniqueness.

### 6. The exact invariant-existence gap

Let \(\mathcal S(a,\mu)\) be the set of all ordinary path laws just constructed: monotone birth-time laws with marginals \(\mu_t\) satisfying (14).

The preceding approximation argument also shows that \(\mathcal S(a,\mu)\) is closed under weak convergence: because every member has the same one-time marginals, an \(L^1(dt\,\mu_t)\) cylinder approximation of each \(a_i\) gives uniform control of the unbounded martingale drift. Birth-time space is compact, so
\[
\mathcal S(a,\mu)
\]
is a nonempty compact convex set.

For \(g\in\Gamma\), set
\[
(gX)_i=X_{g^{-1}i}.
\]
Covariance
\[
a_{gi}(t,gx)=a_i(t,x)
\]
and invariance of \(\mu_t\) imply that
\[
P\in\mathcal S(a,\mu)\quad\Longrightarrow\quad
gP\in\mathcal S(a,\mu).
\tag{22}
\]
Thus the remaining target is exactly
\[
\boxed{\mathcal S(a,\mu)^\Gamma\ne\varnothing.}
\tag{23}
\]

Nothing in the compactness argument above proves (23). Averaging the orbit \(\{gP\}\) would do so for an amenable group, but there is no such averaging argument for an arbitrary group.

This is not merely a formal objection. Mester constructed invariant processes possessing monotone couplings but **no invariant monotone coupling**, so invariant marginals plus existence of an ordinary monotone coupling do not imply existence of an invariant one on nonamenable Cayley graphs. (P. Mester, *Invariant monotone coupling need not exist*, Ann. Probab. 41 (2013), DOI 10.1214/12-AOP767.) His example is not a counterexample here: its marginals have not been shown to be the required uniformly gapped linear DPPs, and it does not provide the prescribed covariant rate field.

### 7. Restricted invariant theorems

**Restricted theorem A — added hypothesis: \(\Gamma\) is amenable.**  
Take the ordinary law \(P\) above and a Følner sequence \(A_n\). Define
\[
\bar P_n=\frac1{|A_n|}\sum_{g\in A_n}gP.
\]
Each \(\bar P_n\) still has every marginal \(\mu_t\) and satisfies the same martingale problem, because these properties are linear and (22) holds. Compactness gives a weak limit \(\bar P\); closure of the martingale problem follows from the same \(L^1(dt\,\mu_t)\) approximation used above. For every \(h\in\Gamma\),
\[
\|h\bar P_n-\bar P_n\|_{\rm TV}
 \le
 \frac{|hA_n\triangle A_n|}{|A_n|}
 \longrightarrow0.
\]
Thus \(\bar P\) is \(\Gamma\)-invariant. This proves W under amenability.

**Restricted theorem B — added hypothesis: weak uniqueness in law.**  
If the ordinary martingale problem in this pure-birth class has a unique law, then (22) says \(gP\) is another solution with the same initial distribution, so uniqueness gives \(gP=P\) for every \(g\). Thus W also follows from weak uniqueness. No such uniqueness hypothesis is present in W.

Neither restricted argument establishes a strong solution, sitewise-Poisson realization, factor representation, or same-noise construction.

### 8. Why the missing step is substantial even for DPPs

Any invariant solution of W immediately gives, for every \(s<t\),
\[
\operatorname{Law}(X_s,X_t)
\]
as a \(\Gamma\)-invariant monotone coupling of \(\mu_s\) and \(\mu_t\).

In particular, using the motivating covariant rate construction specified in the question, W would yield invariant monotone couplings for uniformly gapped ordered equivariant DPP kernels on **arbitrary** countable groups.

Moreover, the gap restriction would not substantially weaken that conclusion. Given arbitrary equivariant positive contractions
\[
Q_0\le Q_1,
\]
take \(0<\delta<1/2\) and set
\[
K_t^\delta
 =
 \delta I+(1-2\delta)\bigl(Q_0+t(Q_1-Q_0)\bigr).
\]
Then
\[
\delta I\le K_t^\delta\le(1-\delta)I.
\]
If W applies to these regularized paths, its endpoint law is an invariant monotone coupling of
\[
\mathbf P^{K_0^\delta},\qquad
\mathbf P^{K_1^\delta}.
\]
Letting \(\delta\downarrow0\), compactness of \(E\times E\), continuity of finite DPP determinants, closedness of the order relation \(x\le y\), and closedness of invariance give an invariant monotone coupling of
\[
\mathbf P^{Q_0},\qquad\mathbf P^{Q_1}.
\tag{24}
\]

The established Lyons–Thom theorem proves this invariant DPP monotone-coupling conclusion for equivariant positive contractions on finitely generated **sofic** groups. (Lyons--Thom, *Invariant Coupling of Determinantal Measures on Sofic Groups*, ETDS 36 (2016), Theorem 5.1; arXiv:1402.0969.) Thus the arbitrary-group invariance demanded by W would, together with the rate construction in the question, go beyond that theorem. This does not disprove W, but it confirms that (23) cannot be replaced by a routine symmetrization argument.

Therefore the exact minimal unresolved statement is:

\[
\boxed{\text{Show that the particular compact convex }\Gamma
\text{-space }\mathcal S(a,\mu)\text{ has a fixed point}}
\]
using the DPP curve plus the prescribed covariant Eulerian birth flux, **without amenability, weak uniqueness, sofic approximation, or a strong/noise realization**; or construct admissible DPP/rate data for which that fixed-point set is empty.

All other parts of the requested weak-existence statement—ordinary superposition, exact marginals, local integrability, coordinatewise and product-topology càdlàg regularity, one-jump-per-coordinate, the natural-filtration martingale property, and absence of simultaneous jumps—follow from the hypotheses as above.
