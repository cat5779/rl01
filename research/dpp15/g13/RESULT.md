PROVED

Let \(I\) be the countable coordinate set, \(E=\{0,1\}^I\), and let \(\mathcal S_{u,v}\) be the ordinary prescribed-marginal pure-birth martingale solutions on \([u,v]\). Thus
\[
\mathcal E_{u,v}
=\{\Law_P(X_u,X_v):P\in\mathcal S_{u,v}\}.
\]

**Necessity.** If \(P\) is a global \(\Gamma\)-invariant solution, then its restriction to every \([u,v]\) lies in \(\mathcal S_{u,v}\), and \(\Law_P(X_u,X_v)\) is diagonally \(\Gamma\)-invariant. Hence the local condition holds for every partition.

We prove sufficiency.

### 1. Conditional segment solutions on one conull set

Fix a partition
\[
\Pi:\quad0=t_0<t_1<\cdots<t_m=1
\]
such that each cell has an invariant
\[
\pi_k\in\mathcal E_{t_{k-1},t_k}^{\Gamma}.
\]
Choose independently
\[
P_k\in\mathcal S_{t_{k-1},t_k}
\]
with endpoint law \(\pi_k\), and disintegrate at the left endpoint:
\[
P_k(d\omega)
=\int_E\mu_{t_{k-1}}(dx)\,R_k(x,d\omega).
\tag{1}
\]

There is one \(\mu_{t_{k-1}}\)-conull Borel set \(D_k\) on which simultaneously:

1. \(R_k(x)(X_{t_{k-1}}=x)=1\);
2. \(R_k(x)\) is supported on coordinatewise càdlàg pure-birth paths, hence each coordinate jumps at most once;
3. for every \(i\in I\),
\[
E_{R_k(x)}
\int_{t_{k-1}}^{t_k}a_i(r,X_{r-})\,dr<\infty;
\tag{2}
\]
4. every bounded-cylinder martingale identity holds in the segment natural filtration.

Indeed, (1)–(2) follow by disintegrating probability-one events. For (3), the unconditional expectations are finite because \(X_r\sim\mu_r\) and \(X_{r-}=X_r\) for Lebesgue-a.e. \(r\), then intersect over countably many \(i\).

For (4), let \(\mathscr C\) be the countable family of finite-pattern indicators and
\[
\mathbb D_k=(\mathbb Q\cap[t_{k-1},t_k])\cup\{t_{k-1},t_k\}.
\]
Use a countable algebra of history-cylinder indicators at times in \(\mathbb D_k\). For \(p<q\) in \(\mathbb D_k\), \(f\in\mathscr C\), such a history test \(G\in\mathcal F_p\), and every bounded Borel \(\phi\),
\[
E_{P_k}\phi(X_{t_{k-1}})G(M_q^f-M_p^f)=0.
\]
Hence
\[
E[G(M_q^f-M_p^f)\mid X_{t_{k-1}}]=0.
\]
Disintegrating and intersecting the countably many exceptional sets gives the identities on one \(D_k\). Monotone class gives all bounded \(\mathcal F_p\)-tests for \(p\in\mathbb D_k\).

For arbitrary \(s<t\), choose \(p_n\in\mathbb D_k\) decreasing to \(s\), and \(q_n\in\mathbb D_k\) decreasing to \(t\) (take \(q_n=t_k\) if \(t=t_k\)). By (2),
\[
E_{R_k(x)}\int_s^{s+h}|L_rf(X_{r-})|\,dr\to0,
\]
while \(f(X_{s+h})\to f(X_s)\) in \(L^1\). Thus \(M_{p_n}^f\to M_s^f\) and \(M_{q_n}^f\to M_t^f\) in \(L^1\). Since \(\mathcal F_s\subset\mathcal F_{p_n}\), the full natural-filtration identity follows. Finite linear combinations of \(\mathscr C\) are exactly all bounded cylinder functions.

For any segment solution and coordinate \(i\), pure birth and the prescribed marginals imply, whenever \(s<t\) lie in the segment,
\[
P(s<T_i\le t)
=K_t(i,i)-K_s(i,i)
=(t-s)H(i,i).
\tag{3}
\]
Thus \(P(T_i=r)=0\) for every fixed positive \(r\) in the segment. Since \(I\) is countable, no positive deterministic time—in particular no positive grid boundary—is a jump time.

### 2. Pasting

Set
\[
Q_k(x,A)=R_k(x)\{X_{t_k}\in A\}.
\tag{4}
\]
By Ionescu–Tulcea, paste the \(R_k\)'s: conditionally on the complete past at \(t_{k-1}\), sample the next segment from \(R_k(X_{t_{k-1}},\cdot)\). Call the resulting law \(P^\Pi\).

Inductively \(X_{t_{k-1}}\sim\mu_{t_{k-1}}\), hence \(X_{t_{k-1}}\in D_k\) a.s. The unconditional law of segment \(k\) is exactly \(P_k\), so
\[
X_t\sim\mu_t,\qquad0\le t\le1.
\tag{5}
\]
The splice is coordinatewise càdlàg and pure birth; (3) also removes any positive-time grid-boundary ambiguity.

For \(s<t\) in one cell and a simple global-history test \(G=G_0G_1\), where \(G_0\) depends on earlier segments and \(G_1\) on the current segment through time \(s\),
\[
E_{P^\Pi}G(M_t^f-M_s^f)
=
E\!\left[
G_0\,E_{R_k(X_{t_{k-1}})}
\{G_1(M_t^f-M_s^f)\}
\right]=0.
\tag{6}
\]
Monotone class gives every bounded \(\mathcal F_s\)-test. If \([s,t]\) crosses grid points, split its martingale increment into cell increments and apply (6) successively with the tower property. Hence
\[
P^\Pi\in\mathcal S_{0,1}.
\tag{7}
\]

### 3. Invariant endpoint laws give an invariant skeleton

Since
\[
\pi_k(dx,dy)
=\mu_{t_{k-1}}(dx)Q_k(x,dy)
\tag{8}
\]
and both \(\pi_k\) and \(\mu_{t_{k-1}}\) are invariant, uniqueness of regular conditional probabilities gives, for every \(g\in\Gamma\),
\[
Q_k(gx,gA)=Q_k(x,A)
\quad
\text{for }\mu_{t_{k-1}}\text{-a.e. }x.
\tag{9}
\]
Because \(\Gamma\) and a determining algebra of \(E\) are countable, the relations can be taken simultaneously on one conull set.

The grid skeleton therefore has law
\[
\Lambda^\Pi(dx_0,\ldots,dx_m)
=
\mu_0(dx_0)\prod_{k=1}^mQ_k(x_{k-1},dx_k),
\tag{10}
\]
and induction using (9) shows
\[
g_*\Lambda^\Pi=\Lambda^\Pi .
\tag{11}
\]
The skeleton is monotone a.s., since every adjacent endpoint pair comes from a pure-birth segment.

### 4. Exactly equivariant interpolation

Let
\[
B=[0,1]\sqcup\{\infty\}\cong[0,1]\cup\{2\},
\qquad
\Omega=B^I.
\]
A point \(T=(T_i)\) represents
\[
X_i(t)=1_{\{T_i\le t\}},
\]
with \(T_i=0\) for initial occupancy and \(T_i=\infty\) for no birth. Thus \(\Omega\) is compact metrizable and every point is a coordinatewise càdlàg pure-birth path.

Choose \(w_i>0\), \(\sum_iw_i=1\), and put
\[
d(T,S)=\sum_{i\in I}w_i
|\theta(T_i)-\theta(S_i)|,
\qquad
\theta(t)=t,\quad\theta(\infty)=2.
\tag{12}
\]

From a monotone grid skeleton define \(I_\Pi\) coordinatewise: use time \(0\) if the coordinate is already \(1\) at \(t_0\); otherwise use the first grid time at which it is \(1\); otherwise use \(\infty\). This rule commutes exactly with coordinate permutations:
\[
I_\Pi(gz)=gI_\Pi(z).
\tag{13}
\]
Hence
\[
\widetilde P^\Pi:=(I_\Pi)_*\Lambda^\Pi
\tag{14}
\]
is exactly \(\Gamma\)-invariant.

Couple \(P^\Pi\) and \(\widetilde P^\Pi\) using the true path and its own grid skeleton. If \(T_i\in(t_{k-1},t_k]\), interpolation moves it to \(t_k\); \(0\) and \(\infty\) are unchanged. Thus, writing
\[
|\Pi|=\max_k(t_k-t_{k-1}),
\]
we have pathwise
\[
d(T,\widehat T)\le|\Pi|,
\qquad
d_{\rm Pr}(P^\Pi,\widetilde P^\Pi)\le|\Pi|.
\tag{15}
\]

### 5. Fine partitions and all one-time marginals

Take the assumed partitions \(\Pi_n\) with \(|\Pi_n|\to0\), making all invariant endpoint choices independently. Write
\[
P_n=P^{\Pi_n},\qquad
\widetilde P_n=\widetilde P^{\Pi_n}.
\]
Compactness of \(\Omega\) gives, along a subsequence,
\[
P_n\Rightarrow P.
\tag{16}
\]
By (15), also \(\widetilde P_n\Rightarrow P\). Since every \(\widetilde P_n\) is invariant and coordinate permutations act continuously on \(\Omega\),
\[
P\ \text{is }\Gamma\text{-invariant}.
\tag{17}
\]

For each coordinate \(i\), all \(P_n\) have the same birth-time law:
\[
P_n(T_i=0)=K_0(i,i),\qquad
P_n(0<T_i\le t)=tH(i,i),
\]
\[
P_n(T_i=\infty)=1-K_1(i,i).
\tag{18}
\]
The projection \(T\mapsto T_i\) is continuous, so (18) holds under \(P\). In particular
\[
P(T_i=t)=0\qquad(t>0).
\tag{19}
\]

For finite \(F\Subset I\) and \(t>0\), \(T\mapsto X_t^F\) is therefore \(P\)-a.s. continuous. Hence
\[
\Law_P(X_t^F)
=
\lim_n\Law_{P_n}(X_t^F)
=
\mu_t^F.
\tag{20}
\]
At \(t=0\),
\[
P(X_r^F\ne X_0^F)
\le r\sum_{i\in F}H(i,i)\to0.
\tag{21}
\]
Finite-dimensional DPP probabilities depend continuously on the finite compression of \(K_t=C+tH\); consequently \(\mu_r^F\to\mu_0^F\). From (20)–(21),
\[
X_t\sim\mu_t
\qquad\forall t\in[0,1].
\tag{22}
\]

### 6. Closure for finite-valued unbounded Borel rates

Fix a bounded cylinder \(f\), supported on finite \(F\), and set
\[
b_f(t,x)=L_tf(x).
\]
Then
\[
|b_f(t,x)|
\le2\|f\|_\infty\sum_{i\in F}a_i(t,x),
\]
so, for
\[
\rho(dt,dx)=dt\,\mu_t(dx),
\]
we have \(b_f\in L^1(\rho)\).

Jointly continuous bounded functions \(c(t,x)\) depending on finitely many spatial coordinates are \(L^1(\rho)\)-dense. Choose \(b_f^{(r)}\) of this type with
\[
\|b_f^{(r)}-b_f\|_{L^1(\rho)}\to0.
\tag{23}
\]
Because every \(P_n\), and by (22) also \(P\), has the same one-time marginals,
\[
E_{P_n}\int_0^1
|b_f^{(r)}(q,X_q)-b_f(q,X_q)|\,dq
=
\|b_f^{(r)}-b_f\|_{L^1(\rho)},
\tag{24}
\]
and the same identity holds for \(P\). A birth-time path has only countably many jump times, so \(X_q\) and \(X_{q-}\) are interchangeable inside these Lebesgue integrals.

For bounded continuous cylinder \(c\),
\[
T\longmapsto\int_s^t c(q,X_q(T))\,dq
\tag{25}
\]
is continuous on \(\Omega\): only finitely many coordinates occur, their indicators converge for Lebesgue-a.e. \(q\), and dominated convergence applies.

Fix \(0<s<t\). Let \(G\) be a finite product of bounded cylinder evaluations at positive times \(\le s\). By (19), all those evaluation functionals, as well as \(f(X_s),f(X_t)\), are \(P\)-a.s. continuous. Replace \(b_f\) by \(b_f^{(r)}\) in the \(P_n\)-martingale identity, let \(n\to\infty\) using (25), then let \(r\to\infty\) using (24). This gives
\[
E_PG\left[
f(X_t)-f(X_s)
-\int_s^tL_qf(X_{q-})\,dq
\right]=0.
\tag{26}
\]

For fixed \(s>0\), the countable algebra generated by \(X_s\) and positive rational evaluations before \(s\) generates \(\mathcal F_s\) modulo \(P\): evaluations at times \(r<s\) are recovered by right limits, \(X_0=\lim_{r\downarrow0}X_r\), and \(X_s=X_{s-}\) a.s. by (19). Hence monotone class extends (26) to every bounded \(G\in\mathcal F_s\).

To close time zero explicitly, let \(h(X_0)\) be a bounded cylinder function. For \(0<r<t\), (26) gives
\[
E[h(X_r)(M_t^f-M_r^f)]=0.
\tag{27}
\]
By (21),
\[
h(X_r)\to h(X_0),\qquad
f(X_r)\to f(X_0)
\]
in \(L^1\) (and a.s.). Moreover
\[
E\int_0^r|b_f(q,X_q)|\,dq
=
\int_0^r\int|b_f(q,x)|\,\mu_q(dx)\,dq
\to0.
\tag{28}
\]
Thus \(M_r^f\to0\) in \(L^1\). Since \(M_t^f\in L^1\),
\[
E[(h(X_r)-h(X_0))M_t^f]\to0.
\]
Letting \(r\downarrow0\) in (27),
\[
E[h(X_0)M_t^f]=0.
\tag{29}
\]
Cylinder functions generate \(\mathcal F_0=\sigma(X_0)\), so the natural-filtration martingale property holds also from time \(0\).

Finite-pattern indicators form a countable determining family and span every bounded cylinder function on each finite coordinate set. Hence this same \(P\) satisfies the martingale problem for every bounded cylinder \(f\). Also
\[
E_P\int_0^1a_i(t,X_{t-})\,dt
=
\int_0^1\int a_i(t,x)\,\mu_t(dx)\,dt<\infty.
\tag{30}
\]

### 7. Path support and simultaneous jumps

Since \(P\) lives on \(\Omega=B^I\), every coordinate is càdlàg pure birth and jumps at most once. In any summable product metric the full path is also càdlàg, by dominated convergence over coordinates.

It remains to derive absence of simultaneous positive-time jumps from the limiting martingale problem. Applying it to \(x_i\) gives
\[
M_i(t)
=
X_i(t)-X_i(0)
-\int_0^ta_i(s,X_{s-})\,ds
\tag{31}
\]
as a martingale. For \(i\ne j\), applying it to \(x_ix_j\) gives
\[
M_{ij}(t)
=
X_i(t)X_j(t)-X_i(0)X_j(0)
-\int_0^t
\bigl[
a_i(s,X_{s-})X_j(s-)
+a_j(s,X_{s-})X_i(s-)
\bigr]ds
\tag{32}
\]
as a martingale.

Let
\[
S_{ij}(t)
=
\sum_{0<r\le t}\Delta X_i(r)\Delta X_j(r).
\]
Integration by parts and (31)–(32) give
\[
S_{ij}
=
M_{ij}
-\int X_{i-}\,dM_j
-\int X_{j-}\,dM_i.
\tag{33}
\]
Hence \(S_{ij}\) is a local martingale. It is also increasing, bounded by \(1\), and starts at \(0\); therefore \(S_{ij}\equiv0\). Countability of \(I\) implies that almost surely no two coordinates jump simultaneously at any positive time.

Thus the local invariant-endpoint condition along any one sequence of finite partitions of mesh tending to zero produces a global \(\Gamma\)-invariant prescribed-generator weak path law, with all prescribed DPP marginals, the full natural-filtration martingale problem, local integrability, coordinatewise càdlàg pure-birth paths, and no simultaneous positive-time jumps. Combined with necessity, this proves (TFP). The invariant endpoint choices may be made independently between cells and refinements; no projective consistency is used. This is only the stated two-time reduction and does not assert that the local invariant endpoint elements exist for arbitrary groups.

