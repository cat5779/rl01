PROVED

Let \(E=\{0,1\}^{\Gamma}\), with \(\Gamma\) countable. For \(i\in\Gamma\) write
\[
D_i f(x):=f(x\cup\{i\})-f(x).
\]
If \(f\) is a cylinder function depending on \(D\Subset\Gamma\), then \(D_i f\equiv0\) for \(i\notin D\).

We construct a law on birth times and prove directly that one weak limit solves all cylinder martingale problems.

---

## 1. Conditional finite-dimensional rates and their \(L^1\) convergence

Fix an increasing exhaustion
\[
F_1\subset F_2\subset\cdots,\qquad \bigcup_nF_n=\Gamma .
\]

For finite \(F\Subset\Gamma\), \(y\in\{0,1\}^F\), and \(i\in F\), put
\[
p_y^F(t):=\mu_t\{x_F=y\},
\]
and
\[
b_{i,y}^F(t)
:=
\int_{\{x_F=y\}}a_i(t,x)\,\mu_t(dx).
\]

Because \(t\mapsto\mu_t\) is weakly continuous and cylinder atoms are clopen, \(p_y^F\) is continuous. Since \((t,x)\mapsto a_i(t,x)\) is nonnegative Borel and \(t\mapsto\mu_t\) is a Borel probability kernel, \(b_{i,y}^F\) is Borel. Moreover,
\[
\sum_y\int_0^1 b_{i,y}^F(t)\,dt
=
\int_0^1\!\int_E a_i(t,x)\,\mu_t(dx)\,dt<\infty .
\]
Hence every \(b_{i,y}^F(t)\) is finite for a.e. \(t\).

After redefining on a Lebesgue-null set of times, set
\[
\alpha_i^F(t,y)
=
\begin{cases}
b_{i,y}^F(t)/p_y^F(t),&p_y^F(t)>0,\\
0,&p_y^F(t)=0 .
\end{cases}
\tag{1}
\]
The null-set redefinition is harmless in every continuity equation and martingale compensator below. Since \(a_i=0\) on \(\{x_i=1\}\),
\[
\alpha_i^F(t,y)=0\qquad\text{if }y_i=1.
\]

Let
\[
m(dt,dx):=dt\,\mu_t(dx).
\]
For fixed \(i\), whenever \(i\in F_n\), extend
\[
\alpha_i^n(t,x):=\alpha_i^{F_n}(t,x_{F_n})
\]
to \([0,1]\times E\).

Then \(\alpha_i^n\) is a version of
\[
\mathbb E_m\!\left[a_i\mid
\mathcal B([0,1])\otimes\sigma(X_j:j\in F_n)\right].
\]
Indeed this follows by testing against sets
\(B\times\{X_{F_n}=y\}\).

The sigma-fields increase to the full product sigma-field. Since \(a_i\in L^1(m)\) by (A), Lévy's upward theorem gives
\[
\|\alpha_i^n-a_i\|_{L^1(m)}\longrightarrow0.
\tag{2}
\]

This \(L^1\) convergence is the key estimate that replaces every boundedness or continuity assumption on the rates.

---

## 2. Projected forward equations

Take \(F\Subset\Gamma\) and let \(f\) depend only on \(F\). Then (CE) reduces to the coordinates \(i\in F\).

In particular, for the indicator of the atom \(y\in\{0,1\}^F\),
\[
p_y^F(t)-p_y^F(0)
=
\int_0^t
\left[
\sum_{\substack{i\in F\\y_i=1}}
b_{i,y-e_i}^F(s)
-
\sum_{\substack{i\in F\\y_i=0}}
b_{i,y}^F(s)
\right]ds .
\tag{3}
\]

Thus all \(p_y^F\) are absolutely continuous and satisfy the finite-state forward equation with edge fluxes
\[
q_{y,i}(t):=p_y^F(t)\alpha_i^F(t,y)
=b_{i,y}^F(t),
\qquad y_i=0.
\tag{4}
\]

We next record a finite-state realization lemma, including the zero-mass-state issue.

---

## 3. Finite-state pure-birth realization lemma

Consider a finite acyclic directed graph \(S\), with probability masses \(p_y(t)\), nonnegative integrable edge fluxes \(q_{y,z}(t)\), and
\[
p_y'(t)
=
\sum_{z\to y}q_{z,y}(t)-\sum_{y\to z}q_{y,z}(t)
\tag{5}
\]
a.e. Suppose \(q_{y,z}(t)=0\) whenever \(p_y(t)=0\).

Set
\[
\lambda_{y,z}(t)=
\begin{cases}
q_{y,z}(t)/p_y(t),&p_y(t)>0,\\
0,&p_y(t)=0,
\end{cases}
\qquad
\lambda_y(t)=\sum_{y\to z}\lambda_{y,z}(t).
\tag{6}
\]

Then there is a time-inhomogeneous pure-jump chain \(Y\) with marginals \(p(t)\), whose transition intensities are \(\lambda_{y,z}\); consequently, for every \(g:S\to\mathbb R\),
\[
g(Y_t)-g(Y_0)
-\int_0^t
\sum_{Y_s\to z}
\lambda_{Y_s,z}(s)\,[g(z)-g(Y_s)]\,ds
\tag{7}
\]
is a martingale.

Here is a direct construction.

For one state \(y\), write
\[
b_y(t)=\sum_{z\to y}q_{z,y}(t),\qquad
c_y(t)=\sum_{y\to z}q_{y,z}(t)=p_y(t)\lambda_y(t).
\]
Then
\[
p_y'=b_y-\lambda_y p_y.
\tag{8}
\]

For
\[
S_y(u,t):=\exp\!\left(-\int_u^t\lambda_y(s)\,ds\right),
\]
with \(e^{-\infty}=0\), the variation-of-constants formula
\[
p_y(t)
=
p_y(0)S_y(0,t)
+
\int_0^t S_y(u,t)b_y(u)\,du
\tag{9}
\]
holds even though \(\lambda_y\) need not be globally integrable.

To see this rigorously, put \(\lambda_y^{(k)}=\lambda_y\wedge k\). From (8),
\[
p_y'
+\lambda_y^{(k)}p_y
=
b_y-(\lambda_y-\lambda_y^{(k)})p_y.
\]
The usual bounded-coefficient formula yields (9) with an additional error bounded by
\[
\int_0^t
c_y(s)\mathbf1_{\{\lambda_y(s)>k\}}\,ds,
\]
which tends to zero by dominated convergence. Then \(k\to\infty\).

The arrival measure into \(y\) is
\[
A_y(du)
=
p_y(0)\delta_0(du)+b_y(u)\,du.
\]
For \(A_y\)-a.e. arrival time \(u\), the rate \(\lambda_y\) is locally integrable immediately after \(u\):

* if \(u=0\) carries mass, then \(p_y(0)>0\), and continuity makes \(p_y\) bounded below near \(0\);
* on \(\{p_y=0\}\), a nonnegative absolutely continuous function has derivative \(0\) a.e.; since \(c_y=0\) there, (8) implies \(b_y=0\) a.e. there. Thus \(b_y(u)\,du\)-a.e. arrival occurs where \(p_y(u)>0\), again giving local integrability.

Therefore an arrival at \(u\) may be followed by a departure at \(v>u\) with cause-specific density
\[
S_y(u,v)\lambda_{y,z}(v)\,dv,
\]
and by no departure before time \(1\) with the remaining survival probability.

By (9), total occupancy at time \(t\) generated by all arrivals is exactly \(p_y(t)\). Hence the total departure flux along \(y\to z\) is
\[
\lambda_{y,z}(t)p_y(t)\,dt
=
q_{y,z}(t)\,dt.
\tag{10}
\]

Because the graph is acyclic, we construct trajectories recursively by rank: first the minimal-rank states, then the next rank, etc. Formula (10) shows that the arrivals generated from the preceding rank are exactly the prescribed incoming fluxes. There are only finitely many ranks, hence no explosion.

The usual hazard calculation also gives the compensated edge-counting martingales and hence (7).

Applying this lemma to \(S=\{0,1\}^{F_n}\), with edges \(y\to y\cup\{i\}\), produces a finite pure-birth chain \(X^{(n)}\) with
\[
X_t^{(n)}\sim\mu_t^{F_n}
\qquad\forall\,t,
\tag{11}
\]
and, for every \(F_n\)-cylinder \(f\),
\[
f(X_t^{(n)})-f(X_0^{(n)})
-
\int_0^t
\sum_{i\in F_n}
\alpha_i^n(s,X_{s-}^{(n)})D_i f(X_{s-}^{(n)})\,ds
\tag{12}
\]
is a martingale.

---

# 4. Compact birth-time space

Let
\[
K=[0,1]\sqcup\{\infty\},
\]
where \(\infty\) is isolated. Thus \(K\) is compact metrizable.

Encode a pure-birth path by birth times
\[
\tau_i=
\begin{cases}
0,&X_0(i)=1,\\
t,&X_{t-}(i)=0,\ X_t(i)=1,\\
\infty,&\text{no birth}.
\end{cases}
\]
Then
\[
X_t(i)=\mathbf1_{\{\tau_i\le t\}}.
\tag{13}
\]

For \(i\notin F_n\), set \(\tau_i^{(n)}=\infty\). Let \(P_n\) be the resulting law on
\[
\Omega:=K^\Gamma.
\]
Since \(\Gamma\) is countable, \(\Omega\) is compact metrizable. Hence some single subsequence, still called \(P_n\), satisfies
\[
P_n\Rightarrow P.
\tag{14}
\]

No further, test-dependent subsequence will be extracted.

Define \(X\) from the limiting birth times by (13). Every coordinate is nondecreasing, càdlàg, and has at most one positive-time jump.

---

# 5. Recovery of every marginal, including \(t=0\)

Fix \(i\), and write
\[
p_i(t)=\mu_t\{x_i=1\}.
\]
This is continuous.

For all sufficiently large \(n\),
\[
P_n(\tau_i\le t)=p_i(t).
\tag{15}
\]
Moreover, because \(p_i\) is continuous,
\[
P_n(\tau_i<t)
=
\lim_{u\uparrow t}p_i(u)=p_i(t)
\qquad(t>0).
\tag{16}
\]

For \(0\le t<1\), the set \([0,t]\subset K\) is closed. Hence
\[
p_i(t)\le P(\tau_i\le t).
\]
For \(\varepsilon>0\), \([0,t+\varepsilon)\) is open, so
\[
P(\tau_i\le t)
\le
P(\tau_i<t+\varepsilon)
\le
\liminf_nP_n(\tau_i<t+\varepsilon)
=
p_i(t+\varepsilon).
\]
Letting \(\varepsilon\downarrow0\),
\[
P(\tau_i\le t)=p_i(t).
\tag{17}
\]
For \(t=1\), \([0,1]\) is clopen in \(K\), so (17) also holds.

Consequently,
\[
P(\tau_i=t)=0\qquad(0<t\le1),
\tag{18}
\]
because \(p_i\) is continuous.

Now fix finite \(D\Subset\Gamma\) and \(t>0\). The map
\[
\tau\mapsto X_t^D
\]
is discontinuous only if \(\tau_i=t\) for some \(i\in D\); by (18) this is a \(P\)-null set. Therefore (14) implies
\[
\mathcal L_P(X_t^D)
=
\lim_n\mathcal L_{P_n}(X_t^D)
=
\mu_t^D.
\tag{19}
\]

The time \(0\) atom requires separate treatment. For every fixed finite \(D\),
\[
X_\delta^D\longrightarrow X_0^D
\qquad(\delta\downarrow0)
\]
pointwise on \(\Omega\). Thus
\[
\mathcal L_P(X_0^D)
=
\lim_{\delta\downarrow0}\mathcal L_P(X_\delta^D)
=
\lim_{\delta\downarrow0}\mu_\delta^D
=
\mu_0^D.
\tag{20}
\]
The last equality is weak continuity of \(\mu_t\).

Since cylinder laws determine probability measures on \(E\),
\[
X_t\sim\mu_t\qquad\forall\,t\in[0,1].
\tag{21}
\]

This proves condition 1 and, at the same time, resolves the possible leakage of positive birth times into the atom at \(0\).

---

# 6. Local integrability and measurability in the limit

For each path there are only countably many coordinate jump times, because \(\Gamma\) is countable. Hence
\[
X_{s-}=X_s
\qquad\text{for Lebesgue-a.e. }s
\tag{22}
\]
on every path.

The map
\[
(s,\tau)\mapsto X_{s-}(\tau)
\]
is Borel coordinatewise; indeed its \(j\)-th coordinate is, for \(s>0\),
\[
\mathbf1_{\{\tau_j<s\}}.
\]
It is also predictable for the natural filtration. Therefore
\[
(s,\tau)\mapsto a_i(s,X_{s-}(\tau))
\]
is Borel/predictable.

By (21), (22), Tonelli, and (A),
\[
E_P\!\int_0^1a_i(s,X_{s-})\,ds
=
\int_0^1\!\int_Ea_i(s,x)\,\mu_s(dx)\,ds
<\infty.
\tag{23}
\]
Thus all compensators appearing below are finite a.s. and integrable.

---

# 7. Closure of the martingale identities

Fix a bounded cylinder \(f\), depending on \(D\Subset\Gamma\).

For \(i\in D\), write
\[
c_i(x)=D_if(x).
\]
It suffices to prove the martingale increment identity.

Fix
\[
0<r<t\le1,
\]
and let \(H\) be any bounded cylinder history functional depending on finitely many coordinates at finitely many **positive** times
\[
0<u_1,\dots,u_k\le r.
\tag{24}
\]

For all sufficiently large \(n\), the finite chain identity gives
\[
E_{P_n}
\left[
H\left(
f(X_t)-f(X_r)
-
\int_r^t
\sum_{i\in D}
\alpha_i^n(s,X_s)c_i(X_s)\,ds
\right)
\right]=0.
\tag{25}
\]
We used \(X_s\) instead of \(X_{s-}\); for each finite chain they differ only at finitely many times, hence not in a Lebesgue integral.

We pass every term to the limit.

## 7.1 Endpoint terms

The functional
\[
H\,[f(X_t)-f(X_r)]
\]
is bounded. Its discontinuities are contained in finitely many sets
\[
\{\tau_j=u_\ell\},\quad
\{\tau_j=r\},\quad
\{\tau_j=t\}.
\]
All those have \(P\)-measure \(0\) by (18).

Hence
\[
E_{P_n}H[f(X_t)-f(X_r)]
\longrightarrow
E_PH[f(X_t)-f(X_r)].
\tag{26}
\]

## 7.2 A continuity fact for time integrals

Fix \(m\) and any bounded Borel
\[
g:[r,t]\times\{0,1\}^{F_m}\to\mathbb R.
\]
Then
\[
J_g(\tau)
=
\int_r^t g(s,X_s^{F_m}(\tau))\,ds
\tag{27}
\]
is a continuous function of \(\tau\in\Omega\).

Indeed, if \(\tau^{(k)}\to\tau\), then for a.e. \(s\) none of the finitely many limiting birth times in \(F_m\) equals \(s\). For each such \(s\),
\[
X_s^{F_m}(\tau^{(k)})
=
X_s^{F_m}(\tau)
\]
eventually. Dominated convergence proves (27).

Notice that **no continuity in \(s\)** of \(g\) is required. This is why merely Borel rates cause no problem once they are truncated.

## 7.3 Unbounded-rate passage

Fix \(i\in D\). Put
\[
R_n
=
E_{P_n}\left[
H\int_r^t
\alpha_i^n(s,X_s)c_i(X_s)\,ds
\right].
\]

Let \(m\) be large enough that \(D\) and all coordinates used by \(H\) belong to \(F_m\). For \(n\ge m\),
\[
\begin{aligned}
&\left|
R_n-
E_{P_n}\left[
H\int_r^t
\alpha_i^m(s,X_s)c_i(X_s)\,ds
\right]
\right|
\\
&\quad\le
\|H\|_\infty\|c_i\|_\infty
\int_r^t
E_{P_n}
|\alpha_i^n(s,X_s)-\alpha_i^m(s,X_s)|\,ds.
\end{aligned}
\]
Because \(P_n\)'s \(F_n\)-marginal at time \(s\) is \(\mu_s^{F_n}\),
\[
\int_r^t
E_{P_n}
|\alpha_i^n-\alpha_i^m|(s,X_s)\,ds
\le
\|\alpha_i^n-\alpha_i^m\|_{L^1(m)}.
\tag{28}
\]

By (2), the right side is uniformly small for large \(m,n\).

Now hold \(m\) fixed and truncate
\[
\alpha_i^{m,L}:=\alpha_i^m\wedge L.
\]
By §7.2,
\[
\tau\mapsto
\int_r^t
\alpha_i^{m,L}(s,X_s)c_i(X_s)\,ds
\]
is continuous and bounded. Multiplying by \(H\) gives a bounded \(P\)-a.s. continuous functional. Therefore
\[
\begin{aligned}
&E_{P_n}\left[
H\int_r^t
\alpha_i^{m,L}(s,X_s)c_i(X_s)\,ds
\right]
\\
&\qquad\longrightarrow
E_P\left[
H\int_r^t
\alpha_i^{m,L}(s,X_s)c_i(X_s)\,ds
\right].
\end{aligned}
\tag{29}
\]

The truncation error is uniformly controlled:
\[
\begin{aligned}
&E_{P_n}
\int_r^t
\alpha_i^m(s,X_s)
\mathbf1_{\{\alpha_i^m>L\}}\,ds
\\
&\qquad=
\int_r^t\!\int_E
\alpha_i^m(s,x)
\mathbf1_{\{\alpha_i^m(s,x)>L\}}
\,\mu_s(dx)\,ds,
\end{aligned}
\tag{30}
\]
for every \(n\ge m\), because the integrand only sees \(F_m\).

The same equality holds under \(P\) by (21). Since \(\alpha_i^m\in L^1(m)\), the right side tends to \(0\) as \(L\to\infty\).

Thus, for fixed \(m\),
\[
\begin{aligned}
&E_{P_n}\left[
H\int_r^t
\alpha_i^m(s,X_s)c_i(X_s)\,ds
\right]
\\
&\qquad\longrightarrow
E_P\left[
H\int_r^t
\alpha_i^m(s,X_s)c_i(X_s)\,ds
\right].
\end{aligned}
\tag{31}
\]

Finally, by (2) and the marginal identity (21),
\[
\begin{aligned}
&E_P\int_r^t
|\alpha_i^m(s,X_s)-a_i(s,X_s)|
\,|c_i(X_s)|\,ds
\\
&\qquad\le
\|c_i\|_\infty
\|\alpha_i^m-a_i\|_{L^1(m)}
\longrightarrow0.
\end{aligned}
\tag{32}
\]

Combining (28), (31), and (32),
\[
R_n\longrightarrow
E_P\left[
H\int_r^t
a_i(s,X_s)c_i(X_s)\,ds
\right].
\tag{33}
\]

Since \(D\) is finite, summing over \(i\in D\) and using (26) in (25) gives
\[
E_P\left[
H\left(
f(X_t)-f(X_r)
-
\int_r^t
\sum_{i\in D}
a_i(s,X_s)D_if(X_s)\,ds
\right)
\right]
=0.
\tag{34}
\]

By (22), \(X_s\) may be replaced by \(X_{s-}\) in the Lebesgue integral.

This is the load-bearing closure argument for merely \(L^1\), Borel, unbounded rates.

---

# 8. The full natural history sigma-field

Let
\[
\mathcal F_r=\sigma(X_u:0\le u\le r)
\]
be the natural filtration.

For \(r>0\), let \(\mathcal A_r\) be the algebra of bounded functions depending on finitely many coordinates at finitely many times belonging to \((0,r]\).

It generates \(\mathcal F_r\). The only point needing comment is time \(0\). But for every coordinate,
\[
X_0(i)
=
\lim_{k\to\infty}X_{r/k}(i)
\tag{35}
\]
pointwise, because a birth time is either \(0\), strictly positive, or \(\infty\). Thus \(X_0\) is measurable with respect to positive-time observations arbitrarily close to zero.

Fix \(f,r,t\) with \(0<r<t\). The increment in parentheses in (34) is integrable by (23). Therefore
\[
\nu(A)
:=
E_P\!\left[
\mathbf1_A(M_t^f-M_r^f)
\right]
\]
defines a finite signed measure on \(\mathcal F_r\).

Equation (34) says \(\nu=0\) on the finite-history cylinder algebra generating \(\mathcal F_r\). The monotone-class theorem gives
\[
E_P[H(M_t^f-M_r^f)]=0
\tag{36}
\]
for every bounded \(\mathcal F_r\)-measurable \(H\).

So the martingale identity already allows arbitrary histories containing \(X_0\).

Equivalently, for an explicit time-zero history test one can replace \(X_0\) by \(X_{r/k}\), use (34), and let \(k\to\infty\); bounded convergence applies because the martingale increment is integrable.

---

# 9. The martingale identity starting at \(0\)

Define
\[
M_t^f
=
f(X_t)-f(X_0)
-
\int_0^t
\sum_{i\in D}
a_i(s,X_{s-})D_if(X_{s-})\,ds.
\tag{37}
\]

We have proved the martingale increment property for \(0<r<t\).

Let \(r_k\downarrow0\). Since \(X\) is coordinatewise right-continuous,
\[
f(X_{r_k})\to f(X_0)
\]
a.s. and in \(L^1\).

Also, from (23),
\[
E_P
\left|
\int_0^{r_k}
\sum_{i\in D}
a_i(s,X_{s-})D_if(X_{s-})\,ds
\right|
\longrightarrow0.
\]
Hence
\[
M_{r_k}^f\longrightarrow0
\qquad\text{in }L^1.
\tag{38}
\]

For \(H\in L^\infty(\mathcal F_0)\), \(H\in\mathcal F_{r_k}\); thus (36) gives
\[
E[H(M_t^f-M_{r_k}^f)]=0.
\]
Using (38),
\[
E[HM_t^f]=0.
\tag{39}
\]

Therefore \(M^f\) is an integrable martingale in the **full natural path filtration**, for every bounded cylinder \(f\).

This proves condition 3.

---

# 10. Why there is no test-dependent diagonal defect

The weakly convergent subsequence (14) was chosen once, before fixing \(f,r,t,H\).

For every subsequent arbitrary test, convergence follows from:

1. the same \(L^1(m)\) convergence (2);
2. the same exact one-time marginals of \(P_n\);
3. weak convergence of that already fixed subsequence;
4. truncation estimates (28)–(32).

No new subsequence is extracted anywhere.

Thus the resulting single law \(P\) solves **all** cylinder martingale problems simultaneously. There is no diagonal gap. If desired, one may reduce to a countable determining family of cylinder indicators and rational times and then use linearity/monotone classes, but the argument above is stronger: it works for an arbitrary test directly on the fixed limit law.

---

# 11. Absence of simultaneous jumps

It remains to prove condition 4; this does not have to be preserved topologically from the approximating finite chains.

Fix distinct \(i,j\).

Apply the already established martingale property to
\[
f_i(x)=x_i.
\]
Since \(a_i(s,x)=0\) when \(x_i=1\),
\[
X_i(t)-X_i(0)
-
A_i(t),
\qquad
A_i(t)=\int_0^t a_i(s,X_{s-})\,ds,
\tag{40}
\]
is a martingale.

Now use
\[
f_{ij}(x)=x_ix_j.
\]
Its generator is
\[
a_i(s,x)x_j+a_j(s,x)x_i,
\]
again because \(a_i=0\) if \(x_i=1\). Hence
\[
X_i(t)X_j(t)-X_i(0)X_j(0)
-
\int_0^t
\bigl[
X_{j-}(s)a_i(s,X_{s-})
+
X_{i-}(s)a_j(s,X_{s-})
\bigr]\,ds
\tag{41}
\]
is a martingale.

For the finite-variation càdlàg processes \(X_i,X_j\), integration by parts gives
\[
\begin{aligned}
X_i(t)X_j(t)-X_i(0)X_j(0)
&=
\int_0^t X_{i-}\,dX_j
+\int_0^t X_{j-}\,dX_i
\\
&\quad+
\sum_{0<s\le t}\Delta X_i(s)\Delta X_j(s).
\end{aligned}
\tag{42}
\]

Using (40), the expectations of the first two stochastic integrals are respectively
\[
E\int_0^tX_{i-}(s)a_j(s,X_{s-})\,ds,
\]
and
\[
E\int_0^tX_{j-}(s)a_i(s,X_{s-})\,ds.
\]

Taking expectations in (42) and comparing with the expectation of (41) therefore yields
\[
E\sum_{0<s\le t}
\Delta X_i(s)\Delta X_j(s)=0.
\tag{43}
\]
The summand is nonnegative. Hence
\[
\sum_{0<s\le1}
\Delta X_i(s)\Delta X_j(s)=0
\qquad P\text{-a.s.}
\tag{44}
\]

Thus \(i\) and \(j\) never jump simultaneously. Since \(\Gamma\) is countable, there are only countably many pairs, so
\[
P\bigl(
\exists i\ne j,\ \exists s>0:
\Delta X_i(s)=\Delta X_j(s)=1
\bigr)=0.
\tag{45}
\]

The value \(\tau_i=0\) encodes initial occupation \(X_0(i)=1\); it is not a jump occurring after the path starts.

---

Hence the limiting law \(P\) satisfies all four requirements:

\[
\boxed{
\begin{array}{l}
X_t\sim\mu_t\quad\forall t\in[0,1],\\
\text{each coordinate is càdlàg pure-birth and jumps at most once},\\
\text{every bounded cylinder martingale problem has rate }a_i,\\
\text{distinct coordinates have no simultaneous positive-time jumps.}
\end{array}}
\]

The compact birth-time route therefore works under exactly (A) and (CE); no invariance, amenability, bounded-rate hypothesis, projective consistency of the finite chains, or stronger superposition theorem is needed.
