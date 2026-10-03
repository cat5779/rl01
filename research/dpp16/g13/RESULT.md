PROVED

Let \(E_m=\{0,1\}^{Q_m}\), \(E=\{0,1\}^{\Gamma}\), and represent every pure-birth path by its birth-time vector. Put
\[
B=[0,1]\sqcup\{\infty\},
\]
topologized as the compact subset \([0,1]\cup\{2\}\subset\mathbb R\), with \(2=\infty\), and
\[
\Omega=B^\Gamma .
\]
If \(T=(T_g)_{g\in\Gamma}\in\Omega\), set
\[
X_t(g)=1_{\{T_g\le t\}}.
\]
Thus every point of \(\Omega\) is coordinatewise càdlàg and pure birth, with at most one jump per coordinate.

Choose positive weights \(w_g\) with \(\sum_gw_g=1\) and use
\[
d(T,S)=\sum_{g\in\Gamma}w_g
|\theta(T_g)-\theta(S_g)|,\qquad
\theta(t)=t,\quad\theta(\infty)=2.
\tag{1}
\]
This makes \(\Omega\) compact metrizable.

## 1. Periodic lifts and compactness

Let
\[
\pi_m:\Gamma\to Q_m=\Gamma/N_m.
\]
A quotient birth-time vector \(\tau\in B^{Q_m}\) has the periodic lift
\[
(\ell_m\tau)_g=\tau_{\pi_m(g)}.
\tag{2}
\]
The map \(\ell_m:B^{Q_m}\to\Omega\) is continuous. Let
\[
\bar P_m=(\ell_m)_*P_m.
\tag{3}
\]
These are the periodic lifts in the statement.

They should not be confused with infinite-volume DPP laws: \(\bar P_m\) is supported on \(N_m\)-periodic paths, and its fixed-time law generally is not \(\mu_t\). Only its finite-coordinate marginals approach those of \(\mu_t\).

The quotient action and lift intertwine:
\[
\ell_m(q\,\tau)=g\,\ell_m(\tau)
\quad\text{whenever }q=\pi_m(g).
\]
Since \(P_m\) is \(Q_m\)-invariant,
\[
g_*\bar P_m=\bar P_m\qquad(g\in\Gamma).
\tag{4}
\]

Compactness of \(\Omega\) yields a subsequence, still denoted \(m\), such that
\[
\bar P_m\Longrightarrow P
\tag{5}
\]
for some probability \(P\) on \(\Omega\). This is exactly local weak convergence of all finite collections of birth-time coordinates.

Coordinate permutations act continuously on \(\Omega\); hence (4)-(5) imply
\[
g_*P=P\qquad(g\in\Gamma).
\tag{6}
\]

Thus every subsequential limit is automatically \(\Gamma\)-invariant.

## 2. Local DPP convergence and deterministic-time atoms

Fix finite \(F\Subset\Gamma\). For all sufficiently large \(m\), the injectivity-radius assumption identifies \(F\) with its image in \(Q_m\).

By hypothesis,
\[
(K_t^{(m)})_F\to(K_t)_F
\tag{7}
\]
uniformly in \(t\). Every probability of a pattern on \(F\) is a finite linear combination of DPP correlation probabilities
\[
\det (K_t)_A,\qquad A\subset F,
\]
and therefore is a continuous polynomial in the entries of the compression. Hence
\[
\sup_{0\le t\le1}
\|\mu_t^{(m),F}-\mu_t^F\|_{\rm TV}\longrightarrow0.
\tag{8}
\]

For a single coordinate \(g\), if \(T_g^{(m)}\) is its lifted birth time,
\[
\bar P_m(T_g^{(m)}\le t)
=\mu_t^{(m)}(x_g=1).
\tag{9}
\]
By (8), these distribution functions converge uniformly to
\[
\mu_t(x_g=1)=K_t(g,g)
=K_0(g,g)+tH(g,g).
\tag{10}
\]
Consequently the \(P\)-law of \(T_g\) is
\[
K_0(g,g)\delta_0
+H(g,g)\,1_{(0,1]}(t)\,dt
+\bigl(1-K_1(g,g)\bigr)\delta_\infty.
\tag{11}
\]
In particular,
\[
P(T_g=t)=0\qquad (0<t\le1).
\tag{12}
\]
Since \(\Gamma\) is countable, no fixed positive deterministic time is a jump time of any coordinate, \(P\)-a.s.

## 3. Recovery of every prescribed one-time marginal

For \(t>0\), the finite-coordinate evaluation
\[
T\mapsto X_t^F
\]
is discontinuous only if \(T_g=t\) for some \(g\in F\), a \(P\)-null event by (12). Hence (5), the a.s.-continuous mapping theorem, and (8) give
\[
\Law_P(X_t^F)
=\lim_m\Law_{\bar P_m}(X_t^F)
=\lim_m\mu_t^{(m),F}
=\mu_t^F.
\tag{13}
\]

Thus \(X_t\sim\mu_t\) for every \(t>0\).

At zero, from (11),
\[
P(X_r^F\ne X_0^F)
\le
\sum_{g\in F}P(0<T_g\le r)
=r\sum_{g\in F}H(g,g)\longrightarrow0.
\tag{14}
\]
Since \(\mu_r^F\to\mu_0^F\) by continuity of \(K_r\), (13)-(14) imply
\[
X_0\sim\mu_0.
\tag{15}
\]

Therefore
\[
X_t\sim\mu_t\qquad(0\le t\le1).
\tag{16}
\]

## 4. The precise \(L^1\) closure consequence of hypotheses 2–3

Fix a bounded cylinder function \(f\), supported on finite \(F\). For large \(m\), regard the same \(f\) as a cylinder function on \(Q_m\). Write
\[
b_m(t,x)=L_t^{(m)}f(x),
\qquad
b(t,x)=L_tf(x).
\tag{17}
\]

Set
\[
\rho_m(dt,dx)=dt\,\mu_t^{(m)}(dx),
\qquad
\rho(dt,dx)=dt\,\mu_t(dx).
\]

The stated \(L^1\) generator convergence, together with the explicit truncation-tail assumption in item 3, has the following standard consequence: there exist bounded functions \(c_r(t,x)\), continuous in \(t\) and depending on finitely many coordinates, such that, writing \(c_r^{(m)}\) for the same local function on \(Q_m\),
\[
\|b-c_r\|_{L^1(\rho)}\longrightarrow0
\tag{18}
\]
and
\[
\lim_{r\to\infty}\limsup_{m\to\infty}
\|b_m-c_r^{(m)}\|_{L^1(\rho_m)}=0.
\tag{19}
\]

For completeness, this is obtained by first truncating \(b,b_m\); the tail clause in item 3 makes the discarded parts uniformly \(L^1\)-small. Hypothesis 2 identifies the truncated local generators in \(L^1\). Bounded Borel local functions are then approximated in \(L^1\) by functions continuous in time (the spatial local state space is finite), and (8) transfers the local \(L^1\) norms between \(\rho_m\) and \(\rho\). Thus (18)-(19) are not an extra assumption; they are precisely the martingale-closure content stipulated in 2–3.

Also
\[
|L_tf(x)|
\le2\|f\|_\infty\sum_{g\in F}a_g(t,x),
\tag{20}
\]
so \(b\in L^1(\rho)\).

## 5. Positive-time martingale closure

Fix
\[
0<s<t\le1
\]
and let
\[
G=\prod_{\ell=1}^k h_\ell(X_{r_\ell}),
\qquad
0<r_\ell\le s,
\tag{21}
\]
where each \(h_\ell\) is a bounded cylinder function.

For large \(m\), all involved finite coordinate sets embed in \(Q_m\). The quotient martingale problem gives
\[
E_{\bar P_m}
G\left[
f(X_t)-f(X_s)
-\int_s^t b_m(q,X_{q-})\,dq
\right]=0.
\tag{22}
\]

For a bounded local \(c(q,x)\), continuous in \(q\),
\[
T\longmapsto\int_s^t c(q,X_q(T))\,dq
\tag{23}
\]
is continuous on \(\Omega\): only finitely many birth-time coordinates occur, and under coordinatewise convergence the associated \(0\)-\(1\) paths converge for Lebesgue-a.e. \(q\); dominated convergence applies.

By (12), the evaluations appearing in \(G,f(X_s),f(X_t)\) are \(P\)-a.s. continuous. Replacing \(b_m\) by \(c_r^{(m)}\) in (22) creates an error bounded by
\[
\|G\|_\infty
\|b_m-c_r^{(m)}\|_{L^1(\rho_m)}.
\tag{24}
\]
For fixed \(r\), weak convergence gives
\[
\begin{aligned}
&\lim_m E_{\bar P_m}
G\left[
f(X_t)-f(X_s)-\int_s^t c_r(q,X_q)dq
\right]\\
&=
E_P
G\left[
f(X_t)-f(X_s)-\int_s^t c_r(q,X_q)dq
\right].
\end{aligned}
\tag{25}
\]
Now let \(r\to\infty\), using (18)-(19), and obtain
\[
E_P
G\left[
f(X_t)-f(X_s)
-\int_s^tL_qf(X_{q-})\,dq
\right]=0.
\tag{26}
\]
The replacement \(X_q\leftrightarrow X_{q-}\) inside Lebesgue integrals is harmless because every birth-time path has only countably many coordinate jump times.

Finite products (21) form an algebra generating the natural path \(\sigma\)-field \(\mathcal F_s\): for \(s>0\), \(X_0\) is recovered from \(X_r\) as \(r\downarrow0\), and arbitrary earlier evaluations are recovered by right continuity. Hence a monotone-class argument extends (26) to every bounded
\[
G\in\mathcal F_s.
\tag{27}
\]

This proves the martingale problem for every positive starting time.

## 6. Time zero

Let \(h(X_0)\) be a bounded cylinder test and \(0<r<t\). From the already established positive-time martingale property,
\[
E_P\!\left[
h(X_r)(M_t^f-M_r^f)
\right]=0,
\tag{28}
\]
where
\[
M_t^f=
f(X_t)-f(X_0)
-\int_0^tL_qf(X_{q-})\,dq.
\]

By (14),
\[
h(X_r)\to h(X_0),
\qquad
f(X_r)\to f(X_0)
\tag{29}
\]
in \(L^1(P)\).

Moreover, using (16) and (20),
\[
E_P\int_0^r|L_qf(X_q)|\,dq
=
\int_0^r\int|L_qf(x)|\,\mu_q(dx)\,dq
\longrightarrow0.
\tag{30}
\]
Therefore
\[
M_r^f\longrightarrow0
\quad\text{in }L^1.
\tag{31}
\]
Since \(M_t^f\in L^1\), boundedness of \(h\) and (29) give
\[
E[(h(X_r)-h(X_0))M_t^f]\to0.
\]
Letting \(r\downarrow0\) in (28),
\[
E[h(X_0)M_t^f]=0.
\tag{32}
\]
Cylinder tests generate \(\mathcal F_0=\sigma(X_0)\), so the martingale property also holds from time zero.

Take finite-pattern indicators as a countable determining family of cylinder functions. They span every bounded function on each finite coordinate set, so by linearity the same limiting law \(P\) satisfies the prescribed martingale problem for every bounded cylinder \(f\).

## 7. Local activity and path support

The limit was taken directly in \(B^\Gamma\). Consequently every sample path is coordinatewise càdlàg and pure birth and every coordinate jumps at most once; no topological closure argument in a Skorokhod space is needed.

For each \(g\),
\[
E_P\int_0^1a_g(t,X_{t-})\,dt
=
\int_0^1\int_Ea_g(t,x)\,\mu_t(dx)\,dt<\infty.
\tag{33}
\]
Hence the local compensator is finite \(P\)-a.s.

The quotient uniform-integrability hypothesis is used in the passage (18)-(19); the target finiteness itself follows from the prescribed target activity assumption and the recovered marginals.

## 8. No simultaneous positive-time births

Apply the limiting martingale problem to
\[
f_i(x)=x_i.
\]
Since \(a_i(t,x)=0\) when \(x_i=1\),
\[
M_i(t)
=
X_i(t)-X_i(0)
-\int_0^t a_i(q,X_{q-})\,dq
\tag{34}
\]
is a martingale.

For \(i\ne j\), applying it to \(x_ix_j\) gives
\[
\begin{aligned}
M_{ij}(t)
={}&X_i(t)X_j(t)-X_i(0)X_j(0)\\
&-\int_0^t
\left[
a_i(q,X_{q-})X_j(q-)
+a_j(q,X_{q-})X_i(q-)
\right]dq
\end{aligned}
\tag{35}
\]
as a martingale.

Define
\[
S_{ij}(t)
=\sum_{0<q\le t}\Delta X_i(q)\Delta X_j(q).
\tag{36}
\]
Integration by parts, followed by substitution from (34), yields
\[
S_{ij}
=
M_{ij}
-\int X_{i-}\,dM_j
-\int X_{j-}\,dM_i.
\tag{37}
\]
Thus \(S_{ij}\) is a local martingale. But it is increasing, nonnegative, starts at \(0\), and is bounded by \(1\). Hence
\[
S_{ij}\equiv0.
\tag{38}
\]
There are countably many pairs, so almost surely no two coordinates jump simultaneously at a positive time.

## 9. Limiting invariant endpoint laws

Fix any \(0\le u<v\le1\). The restriction of \(P\) to \([u,v]\) has marginals \((\mu_t)_{u\le t\le v}\) and solves the same prescribed generator martingale problem there. It is \(\Gamma\)-invariant because \(P\) is. Therefore
\[
\Law_P(X_u,X_v)\in\mathcal E_{u,v}^{\Gamma}.
\tag{39}
\]

This is exactly how finite quotient invariant endpoint laws survive: each \(P_m\) has a \(Q_m\)-invariant endpoint law; after periodic lifting, any path-law subsequential limit is invariant, and the preceding martingale-closure argument proves that its restriction is a genuine target prescribed-generator segment solution. For \(u,v>0\), the lifted endpoint laws themselves converge along the chosen subsequence by (12) and the a.s.-continuous mapping theorem. If \(u=0\), approximate \(X_0\) by \(X_r\), \(r\downarrow0\), using (14), which gives the same endpoint conclusion.

No compatibility in \(m\), between different intervals, or between partition refinements has been used.

Hence the periodic lifts possess a locally weakly convergent subsequence whose limit is a \(\Gamma\)-invariant coordinatewise càdlàg pure-birth weak process with all marginals \(\mu_t\), the exact prescribed generator \(a\), finite local activity, and no simultaneous positive-time jumps. In particular every fixed interval has an invariant dynamically admissible limiting endpoint law.

This is precisely a **residually finite finite-quotient approximation criterion**. It does not prove invariant existence for arbitrary groups, does not construct a strong or factor-of-i.i.d. solution, and does not assert any projective consistency or exact infinite-volume quotient representation.

