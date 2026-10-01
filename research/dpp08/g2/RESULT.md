# Critical tree-percolation extraction: route obstructions

The endpoint invariant joining and joint-iid targets remain INCOMPLETE. The scoped auxiliary mathematical claims below pass one independent mathematical review. The separate finite certificate is not included or certified.

INCOMPLETE

**The endpoint joint factor is not established here. Neither is the weaker existence—or nonexistence—of a \(\Gamma\)-invariant monotone joining at \(p=1/2\).** No positive subcritical interval for the required WUSF marginal is proved.

There are, however, rigorous obstructions to two proposed routes. The rooted Wilson joining cannot itself be invariant, for a reason detectable from the unrooted pair. The wired minimal spanning forest gives an equivariant joint iid extension of critical percolation, but an exact two-edge calculation shows that its marginal is not \(\mu_Q\).

I also give an explicit finite-dimensional criterion equivalent to invariant existence. The first unresolved statement is feasibility of **every** system in that criterion, including its translation constraints. The separate claimed first-window certificate is not included in the present scope.

## 1. Classical inputs and their scope

The supplied connected-cylinder formula already proves that \(1/2\) is an upper bound for every coupling notion in the question. Indeed, any monotone coupling with Bernoulli parameter \(p\) gives
\[
p^m\le 2^{-m}(1+m/3)
\]
for arbitrarily large connected edge sets, whence \(p\le1/2\). The issue is attaining this bound invariantly or as a joint factor, not its necessity.

BLPS, Section 11, assigns independent walks to vertices and uses a parent-before-child enumeration. Its percolation edge is present when the child’s walk hits its parent; on \(T_3\) that probability is \(1/2\). Their proof supplies the ordinary coupling and one-endedness of the WUSF here. It does not assert invariance of this pair. 

Lyons–Thom, Theorem 5.1, assumes a sofic group and
\[
0\le Q_1\le Q_2\le I
\]
in its regular or Cayley-edge equivariant operator algebra, and concludes an invariant monotone coupling. The required order fails here: for nonzero \(v\in\ker Q\),
\[
\langle Qv,v\rangle=0<\tfrac12\|v\|^2.
\]
Thus this theorem does not apply to \((I/2,Q)\); its conclusion is also not a joint factor assertion. 

Ray–Spinka, Theorems 2.3–2.4, require invariant decoupling together with the full finite-history conditional lower bound, or the corresponding Holley-type comparison. Here that lower bound is zero, by the supplied occupied-complement conditioning limit. For a positive-density Bernoulli lower process the corresponding conditional probability remains \(p>0\), so the necessary comparison in those theorems fails. This failure supplies no obstruction to ordinary or invariant domination itself. 

## 2. A necessary structural property of every invariant joining

### Critical clusters: finite, without an integrable size bound

Beyond an initial edge, critical bond-percolation exploration has offspring law \(\operatorname{Bin}(2,1/2)\). Its extinction probability is the smallest solution of
\[
s=((1+s)/2)^2,
\]
which is one. Thus all \(B\)-clusters are finite almost surely, simultaneously by countability.

Their mean size is nevertheless infinite. At distance \(k\ge1\) from a fixed vertex, the expected number of vertices in its cluster is
\[
3\,2^{k-1}2^{-k}=3/2.
\]
Nothing below assumes integrability of cluster size.

### Proposition: infinitely many branching clusters are necessary

Suppose \((B,T)\) is a \(\Gamma\)-invariant monotone joining with the required marginals. Contract each finite \(B\)-cluster inside its \(T\)-component. Orient the quotient toward the component’s unique end.

**Every quotient component must have infinitely many vertices with at least two incoming edges, almost surely.**

**Proof.** A finite connected set \(C\) of \(n\) vertices in a one-ended tree has exactly one boundary edge directed toward the end. Every vertex has one outgoing edge, and its \(n-1\) internal edges account for \(n-1\) of those outgoing edges. Hence each contracted cluster has outdegree one.

The quotient is an infinite locally finite tree. Contraction preserves ends: the preimage of a finite quotient vertex set is finite, and rays lift through the finite connected clusters. Thus every quotient component is one-ended.

Suppose a quotient component has finitely many branching vertices. If that finite set is nonempty, select all of it. Otherwise the component has maximum degree two; being infinite and one-ended, it is a ray, and we select its unique endpoint. Either rule selects a nonempty finite set of quotient vertices without choosing a root.

Lift this selection to a nonempty finite set \(S(K)\) of original vertices in the corresponding infinite \(T\)-component \(K\). Let \(D(K)\) be the finite nonempty set of \(T\)-edges incident to \(S(K)\).

Every edge of \(K\) sends mass \(1/|D(K)|\) to every edge of \(D(K)\). Components not satisfying the supposition send no mass. This is a measurable equivariant transport: connectivity, finiteness, and the one-ended orientation are Borel properties.

Edges form the regular \(\Gamma\)-set, so invariance and reindexing give
\[
\mathbb E\sum_{g\in\Gamma}f(e,g)
=
\mathbb E\sum_{g\in\Gamma}f(g,e).
\]
Outgoing mass is at most one. Every edge in a selected \(D(K)\) receives infinite mass. If such a component occurs with positive probability, countability and edge transitivity imply that the identity edge belongs to a selected set with positive probability. Expected incoming mass is then infinite, a contradiction. \(\square\)

This is **not** a contradiction to the target. A different joining may have the branching that the proposition requires.

## 3. Why the rooted Wilson joining is not invariant

Consider precisely the BLPS construction with fixed vertex root \(o\). For \(v\ne o\), include its parent edge in \(B\) when the independent walk assigned to \(v\) eventually hits its parent. Use those walks in Wilson’s algorithm, with parents preceding children. This gives \(B\sim\operatorname{Bern}(1/2)\) and \(B\subseteq T\). 

In this construction, every edge of \(T\setminus B\), oriented toward its \(T\)-component’s end, points **away from \(o\)**.

To verify this, consider the parent edge of a vertex \(v\).

If \(v\) has not yet been visited when it is processed, its entire forward subtree is unvisited: an earlier path could enter that subtree only by passing through \(v\). Its parent is already in the forest. Therefore, if the parent edge is added by \(v\)’s walk, that walk hits the parent, and the edge belongs to \(B\).

Otherwise, if the parent edge was added before \(v\) was processed, it lies on an earlier loop-erased path entering the forward subtree from outside. Its orientation points away from \(o\). It cannot first be added after \(v\) has been processed, since both endpoints are then already in the forest.

Now contract the finite \(B\)-clusters. The ambient contracted tree is still rooted at the cluster containing \(o\). Every remaining quotient edge points from a parent cluster toward a child cluster. Consequently each quotient vertex has indegree at most one. Section 2 gives outdegree exactly one.

Each quotient component is therefore a ray or a bi-infinite path; one-endedness excludes the latter. In particular, each component has a unique source cluster, recoverable from \((B,T)\) **after forgetting \(o\)**.

The mass transport of Section 2 rules out invariance of this pair law.

Thus the problem is not merely that the algorithm was described using a root. Its output pair has an observable property incompatible with invariance. This disproves only this rooted coupling, not the existence of a different coupling with branching quotients.

## 4. A joint iid endpoint construction with the wrong marginal

The wired minimal spanning forest provides a useful comparison. Write it as \(M\), to distinguish it from the wired **uniform** spanning forest \(T\).

### Construction

Give edges iid Uniform labels \(U_e\), and put
\[
B_e=\mathbf1\{U_e\le1/2\}.
\]
Delete \(e\) from \(M\) exactly when both components of \(T_3\setminus\{e\}\), starting from their respective endpoints, contain an infinite ray whose labels are all smaller than \(U_e\). On a tree this is the wired-minimal-forest rule: \(e\) is maximal on a bi-infinite extended cycle. 

The rule is total Borel and equivariant. By local finiteness, existence of such a ray is equivalent to existence of such a path of every finite length, a countable Borel condition.

Almost surely \(B\subseteq M\): deleting an edge of label at most \(1/2\) would imply an infinite critical Bernoulli cluster. The WMSF one-end theorem assumes a unimodular quasi-transitive graph and \(\theta(p_c)=0\), both satisfied by \(T_3\). Thus \(M\) has one-ended components. The construction commutes with all tree automorphisms and therefore with the specified edge-regular \(\Gamma\)-action. 

Replacing both outputs by the empty configuration on the invariant Borel null set where the asserted almost-sure properties fail gives an everywhere equivariant monotone map without changing either law.

### Exact two-edge discrepancy

Let \(e_1,e_2,e_3\) be the three edges at a vertex. In the forward binary tree beyond \(e_i\), let \(Z_i\) denote the threshold for an infinite open ray, excluding \(e_i\). The three arms are independent, and \(Z_i\) is independent of \(U_i\).

For \(1/2<t<1\),
\[
q(t):=\mathbb P(Z_i<t)=\frac{2t-1}{t^2}.
\]
Indeed, survival satisfies
\[
q=1-(1-tq)^2,
\]
whose nonzero solution is the displayed one. Hence the threshold
\(H_i=\max(U_i,Z_i)\) for a ray through the whole arm satisfies
\[
\mathbb P(H_i<t)=tq(t)=\frac{2t-1}{t}.
\]

On \(U_1>U_2\), both \(e_1,e_2\) are deleted precisely when
\[
Z_1<U_1,\qquad Z_2<U_2,\qquad H_3<U_2.
\]
The first arm cannot provide a ray below \(U_2\), so the third arm is necessary for deleting \(e_2\). Conversely, these conditions also provide the alternate ray needed to delete \(e_1\). Threshold equalities have probability zero.

Therefore
\[
\begin{aligned}
\mathbb P(e_1,e_2\notin M)
&=2\int_{1/2}^{1}q(v)\,[vq(v)]
       \left(\int_v^1q(u)\,du\right)dv\\
&=2\int_{1/2}^{1}
 \frac{2v-1}{v^2}\frac{2v-1}{v}
 \left(1-2\log v-\frac1v\right)dv\\
&=8(\log2)^2-16\log2+\frac{22}{3}.
\end{aligned}
\]

For the required determinantal law, \(Q(e_1,e_2)=1/6\), so
\[
\mu_Q(e_1,e_2\notin T)
=\det(I-Q)[\{e_1,e_2\}]=\frac1{12}.
\]
The difference is
\[
8(1-\log2)^2-\frac34>0.
\]
For an exact bound, the series for \(2\operatorname{arctanh}(1/3)\) gives
\[
\log2\le
\frac23+\frac2{81}+\frac2{1215}+\frac1{6804}
=\frac{23581}{34020}<\frac{1387}{2000}.
\]
Consequently the difference exceeds
\[
8(613/2000)^2-\frac34=\frac{769}{500000}>0.
\]

Thus an equivariant one-ended extension of critical iid clusters is possible, but **this extension does not have the required WUSF law**. Equal expected degrees and one-endedness cannot identify that marginal.

## 5. An explicit criterion equivalent to invariant existence

Let
\[
F_n=\{g\in\Gamma:\ell(g)\le n\}.
\]
Define a finite rational linear feasibility problem \(\mathcal L_n\).

There is a nonnegative variable \(w_n(b,t)\) for every
\(b\subseteq t\subseteq F_n\). Require, for every \(A\subseteq F_n\),
\[
\sum_{A\subseteq b\subseteq t\subseteq F_n}w_n(b,t)=2^{-|A|},
\tag{1}
\]
and
\[
\sum_{\substack{b\subseteq t\subseteq F_n\\A\subseteq t}}
w_n(b,t)=\det Q[A].
\tag{2}
\]
The empty set gives normalization. Inclusion-exclusion shows that these equations specify the complete finite marginal laws of \(B\) and \(T\).

Add the following **partial-translation equations**. For every \(g\) with
\[
D_g:=F_n\cap g^{-1}F_n\ne\varnothing,
\]
and every pattern in the three-state alphabet
\[
\{(0,0),(0,1),(1,1)\}^{D_g},
\]
require its probability to equal that of its translate on \(gD_g\). There are only finitely many relevant \(g\), namely a subset of \(F_nF_n^{-1}\). These equations also imply their counterparts on every subset of \(D_g\).

### Proposition

A \(\Gamma\)-invariant endpoint monotone joining exists **if and only if**
\[
\mathcal L_n\text{ is feasible for every }n.
\tag{3}
\]

**Proof.** Restriction of an invariant joining proves necessity.

Conversely, choose a feasible law in each window and extend it outside \(F_n\) by the constant state \((0,0)\). The countable product of the three-state alphabet is compact metrizable. A diagonal subsequence of finite-cylinder probabilities therefore gives a limiting probability law.

For any fixed finite set, equations (1)–(2) eventually apply, so the limiting law has the required marginals. For any fixed translated cylinder, the cylinder and its translate eventually both lie in the window; the partial-translation equations therefore give invariance in the limit. Support on the three-state alphabet gives \(B\subseteq T\). No compatibility between the separately chosen window laws is needed. \(\square\)

Ordinary domination proves feasibility of (1)–(2) **without** the partial-translation equations. It does not establish their simultaneous compatibility.

> **First unresolved statement:** For every \(n\), \(\mathcal L_n\), including all its partial-translation equations, is feasible.

No proof of this statement and no infeasible window are obtained here.

For
\[
F_1=\{e,a,a^2,b,b^2\},
\]
a separate finite certificate was claimed, but that certificate is not included in this manuscript. Its feasibility and the claimed list of weights are outside the verified scope. No finite-window certificate is used in the arguments above.

Even proving (3) would yield an invariant law by compactness, **not a joint iid factor**.

## 6. The endpoint, subcritical limits, and factor realization remain distinct

If invariant monotone joinings were constructed for some sequence
\(p_j\uparrow1/2\), compactness would give an invariant endpoint joining. The lower finite marginals converge to Bernoulli \(1/2\), the upper marginal stays \(\mu_Q\), and invariance and inclusion pass to the limit. No common coupling across the parameters would be necessary.

No such sequence is constructed here. In particular, the minimal-forest construction in Section 4 is not a subcritical or endpoint result for the specified upper marginal.

For the stronger factor target, neither this compactness argument nor separate iid samplers supplies the missing equivariant joint sampler. Total-Borel completion is a subsequent, simpler issue: given an already Borel almost-surely equivariant monotone map, intersect its equivariance and monotonicity sets over all group translates. Countability gives an invariant Borel conull set. Using the constant pair \((\varnothing,\varnothing)\) outside that set makes the map total and everywhere equivariant without altering its law. This repairs a sampler; it does not construct one.

**Conclusion:** the ordinary optimal threshold remains \(1/2\). The invariant endpoint joining and the stronger joint regular-iid realization remain unresolved in this work. The proved obstructions concern the rooted Wilson joining and the wired-minimal-forest substitute, not the existence assertions themselves.
