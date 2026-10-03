PROVED

Write \(E=\{0,1\}^{\Gamma}\), \(x^{g,+}=x\cup\{g\}\), and
\[
L_t f(x)=\sum_{g\in\Gamma}a_g(t,x)\bigl(f(x^{g,+})-f(x)\bigr).
\]
For a cylinder \(f\), the sum is finite. Put
\[
D:=|B_R(e)|<\infty.
\]
The case \(M=0\) is immediate, so assume \(M>0\).

## 1. Infinite Harris construction

Project \(N_g\) onto its time coordinate. This is a Poisson process of rate \(M\). Call its marked points \((s,u,g)\).

For a query \((g,t)\), define its **backward ancestor set** \(\mathcal A(g,t)\) as follows. Include every mark at \(g\) having time \(<t\). Whenever a mark
\[
z=(h,s,u)
\]
has been included, include every mark \((k,r,v)\) with
\[
k\in B_R(h),\qquad r<s,
\]
and iterate.

This cluster depends only on the Poisson field, not on the initial configuration or on which marks are eventually accepted.

A chain of \(n+1\) marks leading to \((g,t)\) has sites
\[
g_0,\ldots,g_n=g,\qquad
g_{j-1}\in B_R(g_j),
\]
and times
\[
0<s_0<\cdots<s_n<t.
\]
There are at most \(D^n\) site sequences. For each fixed sequence, the expected number of such ordered Poisson tuples is
\[
\frac{M^{n+1}t^{n+1}}{(n+1)!}.
\]
Hence the expected total number of all possible ancestor chains is at most
\[
\sum_{n\ge0}
D^n\frac{M^{n+1}t^{n+1}}{(n+1)!}<\infty.
\tag{1}
\]
Every ancestor mark begins at least one such chain. Therefore
\[
|\mathcal A(g,t)|<\infty\quad\text{a.s.}
\tag{2}
\]

In particular \(\mathcal A(g,1)\) is finite a.s. for every \(g\). Since \(\Gamma\) is countable, there is a single probability-one event \(\mathcal G_1\), depending only on the Poisson field, on which
\[
|\mathcal A(g,1)|<\infty\qquad\forall g\in\Gamma.
\tag{3}
\]
Consequently every finite family of space-time queries has a finite joint ancestor cluster.

There is also a probability-one event \(\mathcal G_2\) on which no two potential marks, at the same or different sites, have the same positive time. Indeed each projected process is simple, two independent projected Poisson processes have no common point, and there are countably many site pairs.

Set
\[
\mathcal G=\mathcal G_1\cap\mathcal G_2.
\]

Fix \(N\in\mathcal G\) and **any** initial configuration \(x\in E\). To answer \((g,t)\), order the finite cluster \(\mathcal A(g,t)\) chronologically. At a mark \((h,s,u)\), all marks before \(s\) at every site in \(B_R(h)\) are themselves ancestors, so the entire state
\[
X_{s-}|_{B_R(h)}
\]
has already been determined. Declare \(h\) occupied at \(s\) precisely when it is vacant and
\[
u\le a_h(s,X_{s-}).
\tag{4}
\]
Proceeding chronologically therefore determines the answer.

The determination is consistent for overlapping queries: the value assigned to a mark depends only on that mark's own ancestors and the initial coordinates on the resulting finite site set. Thus two larger ancestor clusters containing the same mark give the same answer.

Hence on the **same** event \(\mathcal G\) the construction works simultaneously for every
\[
x\in E,\quad g\in\Gamma,\quad0\le t\le1.
\]
There is no exceptional set of initial configurations.

Each site has only finitely many potential marks on \([0,1]\), and it changes only at its own marks. Since occupied sites never become vacant and \(a_g=0\) when \(x_g=1\), each coordinate jumps at most once. Thus every coordinate path is càdlàg and pure birth.

The construction is measurable. One way to see this explicitly is to truncate the ancestor recursion after \(n\) generations, assigning arbitrary fixed values to unresolved histories. Each truncated output is a measurable function of finitely many Poisson points and finitely many input coordinates. On \(\mathcal G\) these outputs stabilize because the true ancestor cluster is finite. Their pointwise limit is therefore measurable. Extend the construction off \(\mathcal G\), for example by keeping the initial configuration fixed; since \(\mathcal G\) is invariant, this extension may also be taken equivariant.

Denote the resulting graphical map by
\[
\Phi(x,N).
\tag{5}
\]

## 2. Covariance and pathwise uniqueness

Let
\[
(\gamma x)_g=x_{\gamma^{-1}g},
\qquad
(\gamma N)_g=N_{\gamma^{-1}g}.
\]
Cayley balls are translated into Cayley balls, and covariance of the rates says
\[
a_{\gamma g}(t,\gamma x)=a_g(t,x).
\]
The ancestor construction and rule (4) therefore commute with translations:
\[
\Phi(\gamma x,\gamma N)
=\gamma\Phi(x,N).
\tag{6}
\]

Pathwise uniqueness is equally direct. Suppose \(X,Y\) satisfy the same graphical rule with the same initial configuration and the same Poisson field in \(\mathcal G\). Fix \((g,t)\). Order \(\mathcal A(g,t)\) chronologically. By induction over its marks, \(X\) and \(Y\) agree on every neighborhood state just before each mark, hence make the same decision in (4). Therefore
\[
X_g(t)=Y_g(t).
\]
Since \(g,t\) were arbitrary,
\[
X=Y.
\tag{7}
\]
Thus \(\Phi\) is the unique strong solution driven by the stated common Poisson field.

Because births are a subset of the potential marks and \(\mathcal G_2\) has no equal positive mark times,
\[
\text{no two coordinates have simultaneous positive-time births.}
\tag{8}
\]

Also
\[
\int_0^1a_g(t,X_{t-})\,dt\le M
\tag{9}
\]
pathwise, so all local activities are finite.

## 3. The graphical process solves the martingale problem

Let \(X_0\) be any random initial state independent of the Poisson field, and put
\[
X=\Phi(X_0,N).
\]

If \(f\) is a bounded cylinder supported by finite \(F\), then pathwise
\[
\begin{aligned}
f(X_t)-f(X_0)
={}&
\sum_{g\in F}
\int_{(0,t]\times[0,M]}
\bigl[f(X_{s-}^{g,+})-f(X_{s-})\bigr]\\
&\qquad\qquad\cdot
1_{\{u\le a_g(s,X_{s-})\}}
\,N_g(ds\,du).
\end{aligned}
\tag{10}
\]
The integrands are bounded predictable processes. Compensating the finitely many Poisson integrals gives
\[
M_t^f
=
f(X_t)-f(X_0)-\int_0^tL_sf(X_{s-})\,ds
\tag{11}
\]
as a martingale in the filtration generated by \(X_0,N\). Since \(M^f\) is adapted to the smaller natural filtration of \(X\), the tower property makes it a martingale there as well.

Writing
\[
\nu_t=\Law(X_t),
\]
taking expectations yields
\[
\nu_t(f)-\nu_0(f)
=
\int_0^t\nu_s(L_sf)\,ds.
\tag{12}
\]

It remains to prove that the bounded finite-range forward equation (12) has only one solution for a given initial law. This is the step that identifies \(\nu_t\) with the prescribed DPP law \(\mu_t\).

## 4. Uniqueness of the bounded finite-range forward equation

Let \((\rho_t)\) and \((\widetilde\rho_t)\) be probability-law curves having the same initial law and satisfying
\[
\rho_t(f)-\rho_0(f)
=\int_0^t\rho_s(L_sf)\,ds
\tag{13}
\]
and likewise for \(\widetilde\rho\), for every bounded cylinder \(f\).

Fix a bounded cylinder \(f\), supported on a finite \(F\), and a terminal time \(T\le1\).

Use the finite interaction graph in which \(i\) is adjacent to \(j\) whenever
\[
j\in B_R(i).
\]
Let \(d_R\) be its graph distance and
\[
\Lambda_n=\{i:d_R(i,F)\le n\}.
\tag{14}
\]
Then
\[
|\{i:d_R(i,F)=n\}|\le |F|D^n.
\tag{15}
\]

Freeze all sites outside \(\Lambda_n\) at zero and define the finite-volume generator
\[
L_s^{(n)}\phi(x)
=
\sum_{i\in\Lambda_n}
a_i(s,x_{\Lambda_n}0_{\Lambda_n^c})
\bigl[\phi(x^{i,+})-\phi(x)\bigr].
\tag{16}
\]
This is a bounded time-inhomogeneous generator on a finite state space. Let
\[
u_s^{(n)}(x_{\Lambda_n})
=
E_{s,x_{\Lambda_n}}^{(n)}[f(Y_T)].
\tag{17}
\]
Then \(u^{(n)}\) is absolutely continuous in \(s\), satisfies
\[
u_T^{(n)}=f,
\qquad
\partial_su_s^{(n)}
+L_s^{(n)}u_s^{(n)}=0
\quad\text{a.e.}
\tag{18}
\]

We need an estimate on its sensitivity to a boundary coordinate.

For \(i\in\Lambda_n\), let
\[
\operatorname{osc}_i u
=
\sup\{|u(x)-u(y)|:
x_j=y_j\;\forall j\ne i\}.
\]
Couple two finite-volume graphical processes with the same Poisson field and initial configurations differing only at \(i\). A discrepancy can be newly created at a site \(j\) only at a potential mark of \(j\), and only if immediately beforehand there is already a discrepancy somewhere in \(B_R(j)\). Hence, if the two terminal \(F\)-configurations differ, there must be a chronological causal chain from \(i\) to \(F\).

For a fixed site sequence of length \(k\), the probability of having the required \(k\) ordered potential marks in an interval of length \(T-s\) is at most
\[
\frac{(M(T-s))^k}{k!}.
\]
There are at most \(D^k\) site sequences. Therefore
\[
\operatorname{osc}_i u_s^{(n)}
\le
2\|f\|_\infty
\sum_{k\ge d_R(i,F)}
\frac{(DM(T-s))^k}{k!}.
\tag{19}
\]

Regard \(u_s^{(n)}\) as a cylinder function on \(E\). Since it depends only on \(\Lambda_n\),
\[
(\partial_s+L_s)u_s^{(n)}
=(L_s-L_s^{(n)})u_s^{(n)}.
\tag{20}
\]
For every \(i\) whose \(R\)-neighborhood is contained in \(\Lambda_n\), the two rates in the corresponding summand agree. Thus only
\[
\partial_R\Lambda_n
=
\{i\in\Lambda_n:B_R(i)\not\subset\Lambda_n\}
\]
contributes. Such \(i\)'s have \(d_R(i,F)=n\). Hence, using \(|a_i-a_i^{(n)}|\le M\),
\[
\sup_x
|(\partial_s+L_s)u_s^{(n)}(x)|
\le
M\sum_{i\in\partial_R\Lambda_n}
\operatorname{osc}_i u_s^{(n)}.
\tag{21}
\]
By (15), (19), and \(T-s\le1\),
\[
\begin{aligned}
\sup_{s,x}|(\partial_s+L_s)u_s^{(n)}(x)|
&\le
2M\|f\|_\infty |F|D^n
\sum_{k\ge n}\frac{(DM)^k}{k!}\\
&\le
2M\|f\|_\infty |F|e^{DM}
\frac{(D^2M)^n}{n!}
=: \varepsilon_n,
\end{aligned}
\tag{22}
\]
and
\[
\varepsilon_n\longrightarrow0.
\tag{23}
\]

The forward equation extends to absolutely continuous time-dependent cylinder functions. Indeed on the finite state space \(\{0,1\}^{\Lambda_n}\) write
\[
u_s^{(n)}=\sum_y c_y(s)1_{\{x_{\Lambda_n}=y\}}
\]
with all \(c_y\) absolutely continuous; applying (13) to the finitely many pattern indicators and using the scalar product rule gives
\[
\rho_T(u_T^{(n)})-\rho_0(u_0^{(n)})
=
\int_0^T
\rho_s\bigl((\partial_s+L_s)u_s^{(n)}\bigr)\,ds.
\tag{24}
\]
Since \(u_T^{(n)}=f\),
\[
\left|
\rho_T(f)-\rho_0(u_0^{(n)})
\right|
\le T\varepsilon_n.
\tag{25}
\]
The identical estimate holds for \(\widetilde\rho\). Their initial laws are equal, so
\[
|\rho_T(f)-\widetilde\rho_T(f)|
\le2T\varepsilon_n\longrightarrow0.
\tag{26}
\]
Thus
\[
\rho_T(f)=\widetilde\rho_T(f)
\]
for every bounded cylinder \(f\) and every \(T\). Cylinder functions determine probability laws on \(E\), hence
\[
\rho_T=\widetilde\rho_T\qquad\forall T\in[0,1].
\tag{27}
\]

So the bounded finite-range cylinder forward equation is unique for every initial distribution.

## 5. Identification with the prescribed DPP marginals

Now take
\[
X_0\sim\mu_0
\]
independently of the Poisson field and construct
\[
X=\Phi(X_0,N).
\]
Its one-time laws \(\nu_t\) satisfy (12).

By assumption, the DPP curve satisfies the same cylinder continuity equation:
\[
\mu_t(f)-\mu_0(f)
=
\int_0^t\mu_s(L_sf)\,ds.
\tag{28}
\]
Both curves start from \(\mu_0\). Forward-equation uniqueness therefore gives
\[
\boxed{\Law(X_t)=\nu_t=\mu_t\qquad0\le t\le1.}
\tag{29}
\]

Since \(K_0\) is equivariant, \(\mu_0\) is \(\Gamma\)-invariant. The independent Poisson field is also \(\Gamma\)-invariant, and the map \(\Phi\) is exactly equivariant by (6). Hence the full path law is \(\Gamma\)-invariant.

Thus the Harris prescription gives a unique coordinatewise càdlàg pure-birth **strong** solution, measurable and equivariant in
\[
(X_0,(N_g)_{g\in\Gamma}),
\]
with finite local activity, no simultaneous positive-time births, and precisely the prescribed DPP marginals.

## 6. Supplied iid sampler

Suppose, additionally, that one is already given an equivariant iid-factor sampler
\[
X_0=\Psi(U)
\]
for \(\mu_0\). Keep this iid layer \(U=(U_g)\) independent of a second iid layer \(V=(V_g)\) from which the sitewise Poisson measures \(N_g\) are encoded. Then
\[
(U,V)
\longmapsto
\Phi\bigl(\Psi(U),N(V)\bigr)
\tag{30}
\]
is an equivariant factor of the product iid field. This uses the supplied sampler only; no iid representation of the DPP has been inferred.

Therefore (STR) holds for uniformly bounded finite-range covariant birth rates. The result does not extend here to unbounded rates, infinite-range dependence, varying-rate common-noise limits, or unrestricted strong/factor realizations.
