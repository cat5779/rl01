# Independent mathematical audit

## Verdict

**OVERALL STATUS: INCOMPLETE.**

The main target is not proved or disproved. The audited text does not establish a
\(\Gamma\)-invariant monotone joining at \(p=1/2\), does not establish a joint
regular-iid factor at that endpoint, and does not construct a positive
subcritical interval for the required WUSF marginal.

**STATUS OF THE SCOPED RESULTS: CORRECT.** The necessary quotient-branching
condition, the non-invariance of the particular rooted Wilson pair, the WMSF
joint-iid comparison with its exact wrong two-edge marginal, and the finite-LP
equivalence with invariant existence are all supported by complete arguments in
the audited text. None of these results is an existence obstruction for all
invariant joinings.

This audit covers the mathematical body supplied for review. It does **not**
audit the separate appendix or its claimed 70-weight \(F_1\) certificate.

## CORRECT: actually established results

### 1. Endpoint necessity and critical clusters

For every connected edge set \(F\) of size \(m\), monotonicity gives
\[
 p^m=\mathbb P(F\subseteq B)\leq \mathbb P(F\subseteq T)
 =2^{-m}(1+m/3).
\]
Taking \(m\)-th roots and then \(m\to\infty\) gives \(p\leq 1/2\).
This proves necessity only, as the text states.

At \(p=1/2\), exploration beyond the first edge is a critical
\(\operatorname{Bin}(2,1/2)\) Galton--Watson process. Its extinction probability
is one. Countability gives simultaneous finiteness of all clusters. The expected
cluster size is nevertheless infinite because every sphere of radius \(k\geq1\)
contributes expected size
\(3\,2^{k-1}2^{-k}=3/2\). No integrability of cluster size is used later.

### 2. Necessary infinite branching after contraction

Let \((B,T)\) be any invariant monotone joining with the required marginals.
Contract the finite connected \(B\)-clusters inside every one-ended component
of \(T\), and orient quotient edges toward that component's unique end.

The proof that each quotient vertex has one outgoing edge is correct. If a
cluster has \(n\) vertices, the \(n-1\) internal tree edges account for exactly
\(n-1\) of the \(n\) outgoing vertex edges, leaving exactly one outgoing
boundary edge. Contraction of finite connected sets preserves local finiteness,
the tree property, infinitude, and the number of ends.

If a quotient component had only finitely many vertices of indegree at least
two, then either that nonempty finite branching set could be selected, or, when
there are no such vertices, the one-ended degree-at-most-two component would be
a ray and its unique endpoint could be selected. Lifting the selected quotient
vertices gives a nonempty finite vertex set \(S(K)\) in the original component.
Sending one unit of mass from every edge of \(K\), equally divided among the
finite nonempty set of \(T\)-edges incident to \(S(K)\), gives outgoing mass at
most one but infinite incoming mass at every selected edge. Since the edge set
is a regular \(\Gamma\)-set, the mass-transport identity applies. If any bad
component occurred with positive probability, countability and edge
transitivity would put the identity edge in a selected set with positive
probability, contradicting equality of expected incoming and outgoing mass.

Thus every quotient component has infinitely many vertices with at least two
incoming edges almost surely. This is a necessary shape constraint, not a
contradiction to the desired joining.

### 3. The rooted Wilson pair is observably non-invariant

The use of the BLPS tree coupling is accurate. With a fixed root \(o\), take a
parent-before-child enumeration and independent walks \(X_v\). The edge from
\(v\) to its parent belongs to the Bernoulli process when \(X_v\) hits that
parent. On the 3-regular tree this has probability \(1/2\), independently over
vertices. BLPS proves that each Bernoulli component lies in a WSF component;
because the ambient graph is itself a tree, this component inclusion implies
edgewise inclusion \(B\subseteq T\).

The orientation argument is also correct. If \(v\) is unvisited when it is
processed, its forward subtree is unvisited. If its parent edge is added by
\(v\)'s walk, then the walk hits the parent and that edge lies in \(B\). If the
parent edge was added earlier, the earlier loop-erased path entered the forward
subtree from outside and then continued toward infinity, so the edge points
away from \(o\) toward the WSF component's end. It cannot first be added later,
after both endpoints are already in the Wilson forest. Hence every edge of
\(T\setminus B\), oriented toward its component end, points away from \(o\).

After contracting the finite \(B\)-clusters, every quotient vertex has indegree
at most one and outdegree exactly one. Each infinite component is therefore a
ray or a bi-infinite path; one-endedness excludes the latter. Its unique source
cluster is measurable from the unrooted pair \((B,T)\). This violates the
necessary infinite-branching property above, so the law of this particular pair
is not invariant. The argument does not rule out another invariant joining.

### 4. WMSF is an equivariant joint-iid comparison, but has the wrong marginal

For iid edge labels \(U_e\), the wired minimal spanning forest deletes \(e\)
exactly when \(e\) is maximal on a bi-infinite simple path, equivalently when
both sides of \(T_3\setminus\{e\}\) contain rays with labels below \(U_e\).
The rule is Borel and equivariant. Setting \(B_e=\mathbf 1\{U_e\leq1/2\}\)
gives critical iid percolation. If an edge of label at most \(1/2\) were deleted,
there would be an infinite critical open ray, an event of probability zero;
countability gives \(B\subseteq M\) almost surely. The hypotheses of the WMSF
one-end theorem hold for \(T_3\): it is unimodular and quasi-transitive, and
\(\theta(p_c)=\theta(1/2)=0\).

The two-edge calculation is exact. In each forward binary arm, let \(Z_i\) be
the threshold for an infinite ray. For \(1/2<t<1\),
\[
 q(t):=\mathbb P(Z_i<t)=\frac{2t-1}{t^2},
 \qquad
 \mathbb P(\max(U_i,Z_i)<t)=tq(t)=\frac{2t-1}{t}.
\]
On \(U_1>U_2\), simultaneous deletion of adjacent \(e_1,e_2\) is exactly
\[
 Z_1<U_1,\qquad Z_2<U_2,\qquad \max(U_3,Z_3)<U_2.
\]
Independence of the three arms therefore gives
\[
 \mathbb P(e_1,e_2\notin M)
 =2\int_{1/2}^1 q(v)\,vq(v)
       \left(\int_v^1q(u)\,du\right)dv
 =8(\log2)^2-16\log2+\frac{22}{3}.
\]
Numerically this is approximately \(0.08660255572\).

For the target DPP, adjacent edges have
\(Q(e_i,e_i)=2/3\) and \(Q(e_1,e_2)=1/6\), so
\[
 \mu_Q(e_1,e_2\notin T)
 =\det\begin{pmatrix}1/3&-1/6\\-1/6&1/3\end{pmatrix}
 =\frac1{12}.
\]
Their difference is
\[
 8(1-\log2)^2-\frac34>0.
\]
The rational upper bound on \(\log2\) in the text yields the stated explicit
positive lower bound \(769/500000\). Thus the WMSF construction is a valid
equivariant joint-iid monotone extension of critical Bernoulli percolation, but
its upper marginal is not \(\mu_Q\).

### 5. The finite LP is equivalent to invariant joining existence

For each finite word ball \(F_n\), the variables \(w_n(b,t)\),
\(b\subseteq t\subseteq F_n\), describe the exact three-state law. Equation
(1) specifies all inclusion probabilities of the lower process, and equation
(2) specifies all inclusion probabilities of the upper process. Finite
inclusion--exclusion therefore fixes the Bernoulli and DPP marginals completely.
The partial-translation equations equate every three-state pattern on
\(D_g=F_n\cap g^{-1}F_n\) with its translate on \(gD_g\); marginalizing these
equations gives the same equality on every smaller domain.

Necessity follows by restricting an invariant joining. Conversely, for every
\(n\) choose any feasible law, extend it outside \(F_n\) by state \((0,0)\), and
take a weakly convergent subsequence in the compact space of probability laws
on the three-state product space. Every fixed finite marginal equation and
every fixed translated-cylinder equality eventually occurs inside the
corresponding word ball, so the limit has the required marginals, is invariant,
and is supported on \(B\subseteq T\). Compatibility between the separately
chosen finite-window laws is unnecessary. Hence
\[
 \text{an invariant monotone endpoint joining exists}
 \quad\Longleftrightarrow\quad
 \mathcal L_n\text{ is feasible for every }n.
\]

This equivalence is correct, but it does not prove the feasibility assertion.
It also yields only an invariant law, not a joint factor of iid.

## Primary-source audit

The cited conditions are represented accurately.

- Benjamini--Lyons--Peres--Schramm, *Uniform Spanning Forests*, Section 11:
  the proof of Theorem 11.1 uses independent vertex walks, the
  parent-before-child order, and the percolation edge event that the child's
  walk hits its parent; it states that each resulting percolation component is
  contained in a WSF component.
  <https://rdlyons.pages.iu.edu/pdf/usf.pdf>
- Lyons--Thom, *Invariant coupling of determinantal measures on sofic groups*,
  Theorem 5.1 assumes \(0\leq Q_1\leq Q_2\leq I\) and concludes an invariant
  monotone coupling. Here \((1/2)I\nleq Q\), since \(Q\) is a nonidentity
  projection and a nonzero vector in \(\ker Q\) violates the order. The theorem
  does not assert a common iid factor.
  <https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf>
- Ray--Spinka, *Characterizations of amenability through stochastic domination
  and finitary codings*, Theorems 2.3--2.4: the former requires invariant
  decoupling and gives the conditional lower parameter \(p_*(X)\); the latter
  additionally uses the full finite-history Holley comparison \(X\succeq_*Y\).
  A zero conditional lower infimum for the WUSF process cannot dominate a
  positive Bernoulli conditional probability through these criteria. Failure of
  their sufficient hypotheses is not a nonexistence theorem.
  <https://arxiv.org/abs/2304.13784>
- Lyons--Peres--Schramm, *Minimal Spanning Forests*: WMSF deletes edges maximal
  on extended cycles, and Theorems 1.1/3.12 give one-ended WMSF components on
  unimodular quasi-transitive graphs when \(\theta(p_c)=0\).
  <https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf>

## CRITICAL_GAPS relative to the target

1. **Invariant existence remains exactly open (source lines 202--220).** No proof is given that every
   \(\mathcal L_n\), including all partial-translation equations, is feasible;
   no infeasible \(n\) is produced either. Calling the systems equivalent to
   invariant existence does not discharge this obligation.
2. **The claimed 70-weight \(F_1\) certificate is unreviewed here (source lines 222--226).** Its appendix
   and verifier were not supplied in the audited evidence. Even if correct, one
   finite window would not imply feasibility for every \(n\).
3. **The factor target remains strictly stronger and open (source lines 228 and 230--237).** Compactness of laws
   loses the common iid realization. No equivariant relative sampler or other
   common regular-iid construction for \((B,T)\) is provided.
4. **No subcritical range is established for the required upper marginal (source lines 232--235).** The
   WMSF comparison has a different upper law and therefore supplies no such
   range for \(\mu_Q\).
5. **No general nonexistence conclusion follows from the two route failures (source lines 71, 91, 168, and 239).**
   The rooted Wilson calculation rejects one root-dependent coupling, and the
   WMSF calculation rejects one equivariant factor with the wrong marginal.
   Neither is a counterexample to invariant joining existence or joint-factor
   existence.

## Final classification

- Necessary optimal upper bound \(p\leq1/2\): **CORRECT**.
- Necessary infinitely-branching quotient condition: **CORRECT**.
- Rooted Wilson pair is not \(\Gamma\)-invariant: **CORRECT**.
- WMSF gives a joint iid monotone comparison but not the WUSF marginal:
  **CORRECT**.
- Finite-LP feasibility for every level is equivalent to invariant joining
  existence: **CORRECT**.
- The attached \(F_1\) 70-weight certificate: **NOT REVIEWED**.
- Invariant endpoint joining: **UNRESOLVED**.
- Joint regular-iid endpoint factor: **UNRESOLVED**.
- Overall target: **INCOMPLETE**.
