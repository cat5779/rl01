INCOMPLETE

The arbitrary-group fixed-point statement \(W\) is not proved or disproved here. I can, however, reduce the full path-space fixed-point problem exactly to a family of **independent two-time fixed-point problems**, and obtain a new sufficient condition strictly below full weak uniqueness in what it requires of the dynamics.

The key point is that no projective consistency between the invariant two-time choices is needed.

## 1. Segment solution spaces and dynamically admissible endpoint couplings

For \(0\le u<v\le1\), let \(\mathcal S_{u,v}\) denote the laws of coordinatewise càdlàg pure-birth paths on \([u,v]\) which

\[
X_t\sim\mu_t,\qquad u\le t\le v,
\]

and solve the prescribed martingale problem
\[
f(X_t)-f(X_s)-\int_s^t L_r f(X_{r-})\,dr
\]
for every bounded cylinder \(f\), \(u\le s\le t\le v\).

These sets are nonempty: restrict any ordinary global realization, whose existence is one of the audited facts.

Define the set of **dynamically admissible endpoint couplings**
\[
\mathcal E_{u,v}
 :=
 \left\{
 \operatorname{Law}_P(X_u,X_v):P\in\mathcal S_{u,v}
 \right\}.
\tag{1}
\]

Every member of \(\mathcal E_{u,v}\) is a monotone coupling of \(\mu_u,\mu_v\), but in general
\[
\mathcal E_{u,v}
\subsetneq
\{\hbox{all monotone couplings of }\mu_u,\mu_v\}
\]
may occur: membership in \(\mathcal E_{u,v}\) records realizability by the prescribed generator throughout the whole interval.

The diagonal action of \(\Gamma\) preserves \(\mathcal E_{u,v}\).

Here is the useful reduction.

---

## 2. Local endpoint fixed-point theorem

Let
\[
t_k^{(n)}=k2^{-n},\qquad 0\le k\le2^n.
\]

### Theorem

The following are equivalent.

1. \(W\) holds: there exists a \(\Gamma\)-invariant global law in \(\mathcal S(a,\mu)\).

2. For every \(n\ge1\) and every \(1\le k\le2^n\),
\[
\mathcal E_{t_{k-1}^{(n)},t_k^{(n)}}^\Gamma\neq\varnothing.
\tag{2}
\]

More generally, it suffices that (2) hold along any sequence of finite partitions whose mesh tends to zero.

Thus the full path-space fixed point requires **no compatible family of invariant endpoint couplings**: one may choose the invariant coupling independently on every cell and independently again for every refinement.

### Necessity

If \(P\in\mathcal S(a,\mu)\) is invariant, its restriction to \([u,v]\) is invariant. Hence
\[
\operatorname{Law}_P(X_u,X_v)\in\mathcal E_{u,v}^\Gamma.
\]
This proves necessity.

The nontrivial part is sufficiency.

---

## 3. Choose arbitrary segment realizations of the invariant endpoints

Fix \(n\), write
\[
0=t_0<t_1<\cdots<t_m=1,\qquad m=2^n.
\]

For each \(k\), hypothesis (2) gives
\[
\pi_k\in\mathcal E_{t_{k-1},t_k}^\Gamma.
\]
Choose
\[
P_k\in\mathcal S_{t_{k-1},t_k}
\]
whose endpoint law is \(\pi_k\).

Disintegrate \(P_k\) with respect to its initial state:
\[
P_k(d\omega)
 =
 \int_E\mu_{t_{k-1}}(dx)\,R_k(x,d\omega).
\tag{3}
\]

For \(\mu_{t_{k-1}}\)-almost every \(x\), \(R_k(x,\cdot)\) is a martingale solution on the cell starting from \(x\).

Indeed, take a countable determining collection consisting of rational times, cylinder functions from a countable generating algebra, and bounded cylinder tests of the past. Disintegrating each martingale identity with respect to \(X_{t_{k-1}}\), then intersecting the resulting countably many conull sets, gives the assertion; the full martingale property follows by the usual monotone-class extension.

Let
\[
Q_k(x,A)
 :=
 R_k\{X_{t_k}\in A\}.
\tag{4}
\]
Then
\[
\mu_{t_{k-1}}(dx)Q_k(x,dy)=\pi_k(dx,dy).
\tag{5}
\]

Because both \(\pi_k\) and \(\mu_{t_{k-1}}\) are invariant, uniqueness of regular conditional probabilities implies
\[
Q_k(gx,gA)=Q_k(x,A)
\tag{6}
\]
for \(\mu_{t_{k-1}}\)-almost every \(x\), for every \(g\in\Gamma\). Since \(\Gamma\) and a generating algebra of \(E\) are countable, versions can be chosen so that the required identities hold simultaneously on one conull set.

Notice what has **not** been shown or assumed: the whole conditional segment law \(R_k(x,\cdot)\) need not be equivariant. Only its endpoint kernel is.

---

## 4. Concatenate the possibly non-equivariant segment laws

Starting with \(X_0\sim\mu_0\), successively sample the \(k\)-th path segment from
\[
R_k(X_{t_{k-1}},\cdot).
\]
Ionescu–Tulcea gives a global path law \(P^{(n)}\).

Induction gives
\[
X_{t_k}\sim\mu_{t_k}.
\tag{7}
\]
Furthermore, because the distribution entering segment \(k\) is exactly \(\mu_{t_{k-1}}\), the unconditional law of that whole segment is
\[
\int\mu_{t_{k-1}}(dx)R_k(x,\cdot)=P_k.
\]
Consequently
\[
X_t\sim\mu_t
\qquad\text{for every }t\in[0,1].
\tag{8}
\]

The martingale problem also glues. On a single cell it follows from the conditional martingale property of \(R_k\); conditional expectation through successive grid boundaries then gives the martingale identity over a union of cells. Splitting an arbitrary interval at its grid points gives
\[
f(X_t)-f(X_s)
 -
 \int_s^tL_r f(X_{r-})\,dr
\]
as a martingale increment for arbitrary \(s<t\).

Therefore
\[
P^{(n)}\in\mathcal S(a,\mu).
\tag{9}
\]

The construction does **not** make \(P^{(n)}\) invariant, because the interior kernels \(R_k\) can be non-equivariant.

What is invariant is its grid skeleton.

---

## 5. The grid skeleton is invariant

Let
\[
\Lambda_n
 =
 \operatorname{Law}_{P^{(n)}}
 (X_{t_0},X_{t_1},\ldots,X_{t_m}).
\]
By construction,
\[
\Lambda_n
 =
 \mu_0(dx_0)
 Q_1(x_0,dx_1)\cdots Q_m(x_{m-1},dx_m).
\tag{10}
\]

The initial law is invariant and every \(Q_k\) is equivariant almost everywhere relative to the appropriate invariant input law. An induction using (6) therefore gives
\[
g_*\Lambda_n=\Lambda_n
\qquad(g\in\Gamma).
\tag{11}
\]

Thus all non-invariance of \(P^{(n)}\) is confined to motion *inside cells of length \(2^{-n}\)*.

This can be made quantitatively negligible.

---

## 6. Canonical equivariant interpolation of the invariant skeleton

Represent a monotone binary path by its coordinate birth times
\[
T_i\in B:=[0,1]\sqcup\{\infty\},
\]
where
\[
X_i(t)=1_{\{T_i\le t\}},
\]
with \(T_i=0\) for a coordinate occupied initially and \(T_i=\infty\) if it never appears.

Give \(B\) the compact topology obtained, for example, by identifying it with
\[
[0,1]\cup\{2\}\subset\mathbb R,
\qquad \infty\leftrightarrow2.
\]
Then
\[
\Omega:=B^\Gamma
\]
is compact metrizable.

From a monotone grid skeleton define the canonical path \(I_n\) by declaring, coordinatewise,

* \(T_i=0\) if the coordinate is already \(1\) at \(t_0\);
* otherwise \(T_i=t_k\) at the first grid point at which it is \(1\);
* \(T_i=\infty\) if it is still \(0\) at \(t_m\).

The map \(I_n\) is Borel and exactly \(\Gamma\)-equivariant:
\[
I_n(gz)=gI_n(z).
\tag{12}
\]

Define
\[
\widetilde P^{(n)}:=(I_n)_*\Lambda_n.
\]
By (11)-(12),
\[
\widetilde P^{(n)}
\quad\text{is }\Gamma\text{-invariant}.
\tag{13}
\]

It is generally not a solution of the martingale problem; many sites can jump simultaneously at grid points. It is used only as an invariant comparison law.

---

## 7. The solution law is uniformly close to the invariant comparison law

Couple \(P^{(n)}\) and \(\widetilde P^{(n)}\) using their common grid skeleton.

If a coordinate has actual birth time \(T_i\in(t_{k-1},t_k]\), the canonical interpolant gives it birth time \(t_k\). Hence
\[
|T_i-\widetilde T_i|\le2^{-n}.
\tag{14}
\]
Initial and never-born coordinates agree exactly.

Enumerate
\[
\Gamma=\{\gamma_1,\gamma_2,\ldots\}
\]
and put
\[
d(T,S)=
\sum_{j\ge1}2^{-j}
\left|\theta(T_{\gamma_j})-\theta(S_{\gamma_j})\right|,
\]
where \(\theta(t)=t\) and \(\theta(\infty)=2\).

Under the above coupling,
\[
d(T,\widetilde T)\le2^{-n}.
\tag{15}
\]
Therefore the Prokhorov distance satisfies
\[
d_{\rm Pr}\bigl(P^{(n)},\widetilde P^{(n)}\bigr)
\le2^{-n}.
\tag{16}
\]

Compactness of \(B^\Gamma\) gives a subsequence
\[
P^{(n_j)}\Longrightarrow P.
\tag{17}
\]
Equation (16) implies simultaneously
\[
\widetilde P^{(n_j)}\Longrightarrow P.
\tag{18}
\]

Each law on the left of (18) is invariant. Invariance is weakly closed because, for every bounded continuous \(\Phi\),
\[
\int\Phi(g\omega)\,dP
 =
 \lim_j\int\Phi(g\omega)\,d\widetilde P^{(n_j)}
 =
 \lim_j\int\Phi(\omega)\,d\widetilde P^{(n_j)}
 =
 \int\Phi(\omega)\,dP.
\]
Thus
\[
P\text{ is }\Gamma\text{-invariant}.
\tag{19}
\]

It remains only to verify that the weak limit is still a prescribed-generator solution.

---

## 8. Closure of the martingale problem with these fixed marginals

I give the argument because the rates are merely Borel and unbounded globally.

Set
\[
\rho(dt,dx)=dt\,\mu_t(dx).
\]
Covariance and (A) imply, for every \(i\),
\[
a_i\in L^1(\rho).
\tag{20}
\]

If \(f\) depends on the finite set \(F\), then
\[
L_tf(x)
 =
 \sum_{i\in F}a_i(t,x)\Delta_i f(x).
\tag{21}
\]

For every \(i\in F\), choose bounded finite-coordinate approximations
\[
b_i^{(r)}(t,x)
\]
such that
\[
\|a_i-b_i^{(r)}\|_{L^1(\rho)}\to0.
\tag{22}
\]
They may additionally be approximated by finite sums whose time factors are continuous. Cylinder functions generate the Borel \(\sigma\)-field of \(E\), so this is ordinary \(L^1(\rho)\)-density.

Crucially, because every \(P^{(n)}\) has exactly the prescribed one-time marginals,
\[
E_{P^{(n)}}\int_0^1
 |a_i(t,X_t)-b_i^{(r)}(t,X_t)|\,dt
 =
 \|a_i-b_i^{(r)}\|_{L^1(\rho)},
\tag{23}
\]
uniformly in \(n\).

For a bounded finite-coordinate \(b\) with continuous time factors,
\[
\omega\mapsto\int_s^t b(r,X_r(\omega))\,dr
\tag{24}
\]
is continuous on birth-time space: convergence of the finitely many relevant birth times implies convergence of the configurations for Lebesgue-a.e. \(r\), and dominated convergence applies.

History-cylinder factors can also be passed to the limit at every positive deterministic observation time. Indeed, monotonicity and the prescribed one-site marginals give, for every \(i\),
\[
P^{(n)}(T_i\le t)
 =
 \mu_t(x_i=1)
 =
 K_t(i,i)
 =
 C(i,i)+tH(i,i).
\tag{25}
\]
Hence
\[
P(T_i=t)=0,\qquad t\in(0,1],
\tag{26}
\]
and evaluation at any fixed positive time is almost surely continuous for every finite set of coordinates.

At time zero, use
\[
P^{(n)}(0<T_i\le\delta)
 =
 \delta H(i,i).
\tag{27}
\]
For finite \(F\),
\[
P^{(n)}(X_0^F\neq X_\delta^F)
 \le
 \delta\sum_{i\in F}H(i,i),
\tag{28}
\]
uniformly in \(n\); then send first \(n\to\infty\), then \(\delta\downarrow0\). This recovers the initial law \(\mu_0\).

Thus the martingale identities with the \(b_i^{(r)}\)'s pass through (17). Equation (23), followed by \(r\to\infty\), restores the true rates \(a_i\). A monotone-class argument over history-cylinder tests gives the natural-filtration martingale property:
\[
f(X_t)-f(X_0)
-\int_0^tL_s f(X_{s-})\,ds
\quad\text{is a martingale.}
\tag{29}
\]

The replacement of \(X_s\) by \(X_{s-}\) inside the Lebesgue integral is harmless: there are at most countably many jump times globally, since \(\Gamma\) is countable and every coordinate jumps at most once.

The same argument shows
\[
X_t\sim\mu_t
\qquad(0\le t\le1).
\tag{30}
\]

Therefore
\[
P\in\mathcal S(a,\mu).
\tag{31}
\]
Together with (19), this proves the sufficiency direction of the theorem.

---

## 9. A new sufficient hypothesis weaker than full weak uniqueness

The reduction immediately gives the following restricted result.

### Restricted theorem: dyadic endpoint uniqueness

Assume that for every dyadic adjacent pair \(u<v\),

\[
\operatorname{Law}_P(X_u,X_v)
\]
is the same for every
\[
P\in\mathcal S_{u,v}.
\tag{32}
\]

No uniqueness of the path law inside \((u,v)\) is assumed.

Then \(W\) holds.

### Proof

Let the common endpoint law be \(\pi_{u,v}\). If \(g\in\Gamma\) and \(P\in\mathcal S_{u,v}\), covariance implies
\[
g_*P\in\mathcal S_{u,v}.
\]
By endpoint uniqueness,
\[
g_*\pi_{u,v}
 =
 \operatorname{Law}_{g_*P}(X_u,X_v)
 =
 \pi_{u,v}.
\]
Hence
\[
\pi_{u,v}\in\mathcal E_{u,v}^{\Gamma}.
\]
The local endpoint theorem now gives an invariant global solution.

This assumption is substantially less than weak uniqueness in what it asks: different segment solutions may have completely different three-time and full path laws; only their two endpoint coordinates are required to agree. I do not claim here that the two conditions are logically inequivalent within the present DPP class, because I do not have a DPP example separating them.

A still weaker sufficient hypothesis is simply
\[
\mathcal E_{u,v}^{\Gamma}\neq\varnothing
\]
on every cell of partitions with mesh tending to zero; no uniqueness whatsoever is then required.

---

## 10. Exact remaining obstruction

The arbitrary-group target has now been reduced to the following local statement:

\[
\boxed{
\text{For every sufficiently small/dyadic }[u,v],
\quad
\mathcal E_{u,v}^{\Gamma}\neq\varnothing.
}
\tag{33}
\]

No compatibility among the fixed points in (33) needs to be proved.

This is strictly more specific than asking for an invariant monotone coupling of \(\mu_u,\mu_v\). The endpoint coupling must lie in the dynamically admissible subset \(\mathcal E_{u,v}\), i.e. it must be the endpoint law of a solution of the **prescribed Borel rate field** on that interval.

That distinction prevents the known DPP endpoint theorem from completing the proof. Lyons–Thom show that, for ordered equivariant positive contractions on a finitely generated sofic group, the associated DPPs possess an invariant monotone coupling. Their theorem does not say that this coupling belongs to \(\mathcal E_{u,v}\) for a separately prescribed generator \(a\). Consequently even an invariant DPP endpoint coupling cannot simply be inserted into Step 3.

Conversely, Mester constructs invariant random subgraphs on a Cayley graph which admit a monotone coupling but no invariant monotone coupling at all. That verifies that the endpoint fixed-point issue is genuine for general invariant processes, but his example is neither the required uniformly gapped linear DPP curve nor equipped with the present covariant rate field, so it does not disprove \(W\).

Thus a complete resolution of \(W\) still requires one of two things:

\[
\boxed{
\begin{array}{l}
\text{prove that every dynamically admissible DPP endpoint set }
\mathcal E_{u,v}\\
\text{contains an invariant element, for arbitrary countable }\Gamma,
\end{array}}
\tag{34}
\]
or construct admissible DPP/rate data for which
\[
\boxed{\mathcal E_{u,v}^{\Gamma}=\varnothing}
\tag{35}
\]
for some interval.

The new conclusion is that **nothing beyond this local two-time obstruction remains**: once invariant dynamically admissible endpoint laws are available independently on arbitrarily fine cells, the canonical-skeleton argument above forces a \(\Gamma\)-invariant full weak path law with the prescribed generator.
