# Forest subrelations, relative cost, and an intersection obstruction

The group-cost target remains INCOMPLETE. The statements below retain their explicit H77 conditions; the equivalent reformulation at the end is not an upper-bound proof. See REVIEW.md for the mathematical checks.

# INCOMPLETE — even conditional on H77

The group-cost equality is not proved or disproved here. The results below establish the FUSF interface, compute the relevant relative cost, and refute an aperiodic-intersection bridge—even on the known equality case \(F_2\times F_2\). They leave an exact upper-bound obstruction, explicitly identified rather than assumed.

“PROVED_HERE” means that a proof is supplied, not a claim of bibliographic priority. Statements involving a Bernoulli FUSF subrelation are **conditional on H77**. The relation-theoretic lemmas and forest-law estimates do not themselves require H77.

## 1. Target and comparison directions

Put \(\beta=\beta_1^{(2)}(\Gamma)\), \(c=1+\beta\), and define
\[
C(\Gamma)=\inf_{a\text{ essentially free pmp}}C(R_a).
\]
Graphing cost is the sum of the domain measures of its partial pmp bijections. Restrictions below use the **original, unnormalized measure**.

**KNOWN — Gaboriau [G00, G02].** For every essentially free pmp action of an infinite countable group,
\[
C(R_a)\ge 1+\beta. \tag{1}
\]
A treeing realizes the cost of the subrelation it generates. Nonergodic actions are covered by ergodic decomposition; they are not excluded from the infimum.

**KNOWN — Abért–Weiss [AW].** For the infinite finitely generated groups in this task, the Bernoulli action \(B\) satisfies
\[
B\preceq a,\qquad C(R_a)\le C(R_B). \tag{2}
\]
Thus Bernoulli cost is **maximal**, not the group infimum. Proving \(C(R_B)\le c\) would, by (1)–(2), prove cost \(c\) for **every** free action and hence fixed price. Group-cost equality alone does not give that conclusion.

Subrelation inclusion supplies neither cost comparison in general: a cyclic subrelation has cost one inside a free \(F_2\)-action of cost two, whereas a coordinate-\(F_2\) subrelation has cost two inside a free \(F_2\times F_2\)-action of cost one.

## 2. FUSF-to-subrelation interface

**PROVED_HERE, conditional on H77.** There is a locally finite, aperiodic treeable subrelation
\[
S_F\subseteq R_B,\qquad C(S_F)=c. \tag{3}
\]

Choose generators \(s_1,\ldots,s_d\ne e\). Use the undirected **multigraph** with oriented edge occurrences
\[
E=\Gamma\times[d],\qquad (g,i):g\longrightarrow gs_i.
\]
Left translation preserves orientations and is free on \(E\). For an involution, \((g,i)\) and \((gs_i,i)\) are distinct parallel edges. This avoids orientation signs and edge stabilizers without converting arbitrary coset-indexed noise.

Let \(\mathcal C\) be the closed finite-cycle space. **KNOWN [BLPS, L03]:** the FUSF kernel is \(Q_F=P_{\mathcal C^\perp}\). H77 supplies its \(E\)-indexed factor. Splitting each regular-\(\Gamma\) uniform into \(d\) uniforms supplies exactly this noise on a Bernoulli action. The **base action** is essentially free; no freeness of the forest factor is asserted.

A finite cycle has inclusion determinant zero because its cycle vector gives a kernel vector of the corresponding compression. For finite nonempty \(K\subset\Gamma\), the cut gradient \(d1_K\) is a nonzero, finitely supported vector in \(\mathcal C^\perp\). The boundary compression of \(Q_F\) therefore has eigenvalue one, so its avoidance determinant is zero. Countably many \(K\) show that all forest components are infinite.

**KNOWN [L14]:**
\[
\operatorname{Tr}_\Gamma Q_F=1+\beta,
\qquad \mathbb E\deg_F(e)=2+2\beta. \tag{4}
\]
The dimension decomposition is the closed gradient space, of dimension one for an infinite group, plus reduced first \(L^2\)-homology, of dimension \(\beta\). The free-label trace is a **sum**, not an average.

Restrict \(x\mapsto s_i^{-1}x\) to the event that \((e,i)\) is present. Under the orbit identification \(g\mapsto g^{-1}x\), this graphing is exactly \(F(x)\). Freeness prevents extra identifications, and parallel pairs cannot both occur. It is a treeing of cost
\[
\sum_iQ_F((e,i),(e,i))=c.
\]
This proves (3). It does **not** prove that \(S_F\) generates \(R_B\).

## 3. The strongest attempted bridge fails its tests

### A sufficient intersection criterion

**PROVED_HERE.** For a partial pmp map \(\phi\) in \(R\), define on its domain
\[
E_\phi=\{(x,y):xSy\text{ and }\phi(x)S\phi(y)\}.
\]
Suppose \(S\) together with maps \(\phi_i\) generates \(R\), and the \(E_{\phi_i}\) have complete sections \(A_i\) with arbitrarily small \(\sum_i\mu(A_i)\). Then arbitrarily cheap additive completion exists: use only \(\phi_i|A_i\).

Indeed, choose \(y\in A_i\) in the \(E_{\phi_i}\)-class of \(x\). Then
\[
x\ S\ y\ \xrightarrow{\phi_i|A_i}\ \phi_i(y)\ S\ \phi_i(x).
\]
The restricted maps therefore recover all the generators.

The question is whether FUSF supplies these sections. It does not do so automatically.

### Finite-overlap theorem

**PROVED_HERE; no H77 needed for this forest-law assertion.** Let \(F\) be WUSF on a Cayley network whose symmetric walk operator satisfies \(\|P\|<1\). Set
\[
G_0=(I-P)^{-1},\qquad
h(g)=\langle G_0^2\delta_e,\delta_g\rangle\ge0.
\]
Then \(h\in\ell^2(\Gamma)\), and for every \(s\ne e\),
\[
\boxed{\mathbb E\!\left[
1_{\{e\not\leftrightarrow s\}}
|C_F(e)\cap C_F(s)s^{-1}|
\right]\le\|h\|_2^2.} \tag{5}
\]
For two independent WUSFs,
\[
\mathbb E|C_{F_1}(e)\cap C_{F_2}(e)|\le\|h\|_2^2. \tag{6}
\]

**Proof.** Independent walks from \(x,y\) have range-intersection probability at most
\[
\sum_zG_0(x,z)G_0(y,z)=h(x^{-1}y), \tag{7}
\]
the expected number of pairs of coincident visits. Boundedness of \(G_0\) gives \(h\in\ell^2\).

**KNOWN [BLPS]:** Wilson’s algorithm rooted at infinity constructs WUSF on a transient locally finite network. A finite initial seed order can be prescribed, and later walks never merge two already constructed components. Using seeds \(x,y\) therefore gives
\[
\mathbb P(x\leftrightarrow y)\le h(x^{-1}y). \tag{8}
\]

Now prescribe seeds \(e,z,s,zs\), with four independent full walks. On
\[
\{e\leftrightarrow z,\ s\leftrightarrow zs,\ e\not\leftrightarrow s\},
\]
the second walk must meet the first walk’s range, and the fourth must meet the third walk’s range. An already incorporated seed gives the same intersection at time zero. These two range-intersection events use disjoint pairs of independent walks. Hence
\[
\mathbb P(e\leftrightarrow z,\ s\leftrightarrow zs,\ e\not\leftrightarrow s)
\le h(z)h(s^{-1}zs). \tag{9}
\]
For repeated seeds, \(z=e\) is bounded by \(h(e)^2\ge1\), while \(z=s\) or \(s^{-1}\) makes the event empty.

Summing (9) and applying Cauchy–Schwarz proves (5), because conjugation is a bijection. The conjugated argument is essential: right multiplication has **not** been assumed to preserve the Cayley graph. Independence and (8) prove (6). \(\square\)

Since \(h\) tends to zero off finite sets, (8) excludes almost-sure connectedness. If every generator pair \((e,s)\) were almost surely connected, invariance and countability would imply connectedness. Thus some generator satisfies
\[
\mathbb P(e\not\leftrightarrow s)>0.
\]

For a free-action realization and \(\phi_s(x)=s^{-1}x\), the \(E_{\phi_s}\)-class at \(x\), in coordinates \(g\mapsto g^{-1}x\), is exactly
\[
C_F(e)\cap C_F(s)s^{-1}.
\]
Equation (5) makes this class finite on a positive-measure set. The set \(\{x:x\not S\phi_s(x)\}\) is \(E_{\phi_s}\)-invariant. Every complete section \(A\) of the finite classes satisfies
\[
\mu(A)\ge
\int_{\operatorname{Fin}(E_{\phi_s})}
\frac{1}{|[x]_{E_{\phi_s}}|}\,d\mu(x)>0, \tag{10}
\]
by averaging over each finite pmp class.

Thus the proposed small-section condition fails for a Cayley generator. Equation (6) also refutes automatic aperiodicity of the intersection of independent forest subrelations. Wilson’s enumeration here proves a law estimate; it is not an equivariant coding claim.

### Required stress tests

**KNOWN / PROVED_HERE applications.** On the standard Cayley tree of \(F_r\), \(Q_F=I\), so \(S_F=R_B\); treeing minimality gives cost \(r\). This is not a disconnected-repair test.

For
\[
F_2\times F_2=\langle a,b\rangle\times\langle c,d\rangle,
\]
its known fixed price one has a direct proof. Include the full \(a\)-map, of cost one. Restrict \(c,d\) to arbitrarily small \(a\)-orbit-complete sections; commutation recovers their full maps. Then restrict \(b\) to a small \(c\)-orbit-complete section; commutation recovers \(b\). The resulting graphing costs at most \(1+\epsilon\); aperiodicity gives the lower bound. The marker construction below supplies the small sections. This rederives a known class, not a new cost result.

By (1), this group has \(\beta=0\). The wired projection \(P_\star\) is below \(Q_F\), with difference of trace \(\beta\). Positivity and covariance make this trace faithful, so
\[
\beta=0\quad\Longrightarrow\quad\text{FUSF}=\text{WUSF}. \tag{11}
\]
Here the projection descriptions and trace difference are the standard spanning-forest inputs. [BLPS, L14]

The four-regular-tree walk has norm at most \(\sqrt3/2\): orient toward a fixed end and write adjacency as \(U+U^*\), where the three-child summation operator has norm at most \(\sqrt3\). The product walk is the average of its two factor walks, so also has norm below one. Consequently (5) applies to this FUSF. The intersection bridge fails even though cheap repair exists **in the unrestricted graphing sense**, as the relative-cost identity below confirms.

For infinite property-(T) groups, **KNOWN [BV97]** gives \(\beta=0\). A Kazhdan gap in the regular representation, followed by making a finite-generator symmetric walk lazy, gives \(\|P\|<1\). Holding times do not change WUSF. Thus the same intersection obstruction applies; it does not prove cost one for arbitrary property-(T) groups.

For other disconnected FUSFs, (3) still concerns only their component subrelation. The WUSF bound is not transferred to FUSF without establishing equality of kernels. No connectivity conclusion is drawn from FIID or operator approximation.

## 4. Compression: what shrinking sections actually does

Define additive relative cost by
\[
\rho_\mu(R:S)=
\inf\{C_\mu(\Psi):S\vee R_\Psi=R\}.
\]
Repair maps may use arbitrary long group words; they need not be Cayley edges or a DPP.

**PROVED_HERE — small sections.** A locally finite graphing with infinite components has complete Borel sections of arbitrarily small measure.

Choose a Borel maximal set \(A\) with mutual graph distances greater than \(2r\). It can be constructed by a countable proper Borel coloring of the distance-\(2r\) graph and greedy selection. Such a coloring follows by assigning each vertex a binary prefix distinguishing it from its finitely many neighbors, including the prefix length in the color.

Maximality gives completeness. The radius-\(r\) balls about selected vertices are disjoint, and each contains at least \(r+1\) vertices. Counting-measure symmetry of a pmp relation gives
\[
(r+1)\mu(A)\le1. \tag{12}
\]
This is a many-point marker section, not a transversal, and uses no amenability.

**PROVED_HERE — ordinary compression.** For a finite-cost pmp relation and an \(R\)-complete set \(A\),
\[
C_\mu(R|A)=C_\mu(R)-1+\mu(A). \tag{13}
\]

Take a finite-cost graphing \(\Theta\). Its degree is finite almost everywhere; discard the saturation of the exceptional null set. At each vertex outside \(A\), select one edge decreasing distance to \(A\). These selected edge occurrences form a forest with one \(A\)-root per component and cost \(1-\mu(A)\).

Remove those occurrences from \(\Theta\). Partition the root map into countably many injective partial pmp pieces, split each remaining edge domain according to the pieces at both endpoints, and project its endpoints to their roots. Domain measures are preserved on each piece. The projected maps generate \(R|A\), with total cost at most
\[
C(\Theta)-1+\mu(A).
\]
Taking infima proves one inequality. Conversely, the rooted forest together with any graphing of \(R|A\) generates \(R\), proving the other.

In normalized measure,
\[
C_{\mu/\mu(A)}(R|A)
=1+\frac{C_\mu(R)-1}{\mu(A)}.
\]
The residual cost is not made small by normalization.

**PROVED_HERE — relative compression.** If \(A\) is \(S\)-complete, then
\[
\boxed{\rho_\mu(R:S)=\rho_\mu(R|A:S|A).} \tag{14}
\]

Choose a root map \(r:X\to A\) inside \(S\), identity on \(A\), and partition it into injective partial pmp pieces. Split every repairing map \(\psi\) by its source and target pieces. On a split domain \(D\), project it to
\[
r\circ\psi\circ(r|_D)^{-1}.
\]
Its domain measure is \(\mu(D)\); total cost does not increase. Every \(S\)-step projects into \(S|A\), and every repair step projects to one of these maps. Conversely, a repair on \(A\), together with \(S\), repairs all of \(R\) by moving endpoints to their roots. This proves both inequalities.

If \(S\) has a graphing of cost \(c\) and the small sections above, then
\[
\max\{0,C(R)-c\}\le\rho(R:S)\le C(R)-1. \tag{15}
\]
The lower bound comes from adjoining a repair to that graphing. For the upper bound, use (14), add a full graphing of \(R|A\), and apply (13) as \(\mu(A)\to0\).

In particular,
\[
\boxed{c=1\quad\Longrightarrow\quad
\rho(R:S)=C(R)-1.} \tag{16}
\]
Thus every such cost-one subrelation in an **already-known cost-one ambient relation** admits arbitrarily cheap completion. This explains why finite overlap on \(F_2\times F_2\) obstructs the proposed certificate, not all repairs.

## 5. Extensions recover the correct group infimum

**PROVED_HERE.** If \(Y\to X\) is an equivariant pmp extension of an essentially free action, each orbit maps bijectively to its base orbit. Partition a partial full-relation map according to the unique group element implementing it, and lift those pieces. The lift is a partial pmp bijection of the same domain measure.

Lifted graphings generate the full extension relation: base freeness forces a lifted word reaching the desired base endpoint to be the desired group element. Hence
\[
C(R_Y)\le C(R_X). \tag{17}
\]
The same argument lifts relative repairs.

For any free action \(a\), the product \(B\times a\) extends both factors. Therefore
\[
\boxed{\inf_{Y\to B}C(R_Y)=C(\Gamma).} \tag{18}
\]
The lower bound is definitional; the upper bound follows from (17). A countable product of \(B\) with actions approaching the infimum even attains it. No fixed-price conclusion follows from this attainment.

The lifted \(S_F^Y\) remains a treeing of cost \(c\) with infinite classes.

**EQUIVALENT_BLOCKER, conditional on H77, when \(\beta=0\).** Equations (16) and (18) give
\[
\boxed{\inf_{Y\to B}\rho(R_Y:S_F^Y)=C(\Gamma)-1.} \tag{19}
\]
Allowing arbitrary extensions and arbitrary long-word repairs removes the unintended Bernoulli/fixed-price target, but leaves exactly the desired group-cost upper bound.

**STRONGER_BLOCKER, conditional on H77.** Proving \(\rho(R_B:S_F)=0\) would instead prove fixed price \(c\), by (1)–(2).

For positive \(\beta\), vanishing of the extension infimum of relative repair cost is sufficient for the group target. Necessity is not asserted: retaining the original forest can be an extra constraint.

## 6. A faithful quotient re-encoding also preserves the obstruction

**PROVED_HERE.** An extension with iid labels on forest components exists without random-kernel DPP coding. On each finite vertex set, use its Borel connectivity partition and give its distinct blocks independent uniforms. These consistent finite-dimensional laws define an equivariant Borel probability kernel on the countable product. The extension is pmp and is free if the base is free.

It supplies no vertex representative per component. An aperiodic pmp relation cannot have a measurable complete transversal \(D\): arbitrarily many disjoint relation-images of \(D\) have equal measure, forcing \(\mu(D)=0\); its countable saturation would then be null.

Let \(R,S\) now denote the **extension** relations, without asserting unchanged ambient cost. Suppose every \(R\)-class contains infinitely many \(S\)-classes. Splitting component labels into \(n\) equal bins gives sets \(A_i\) of measure \(1/n\), each \(R\)-complete almost surely. They are not \(S\)-complete. For
\[
T_n=\bigsqcup_{i=1}^nR|A_i,
\]
compression and additivity give
\[
C(T_n)=1+n(C(R)-1). \tag{20}
\]
Thus component-label compression amplifies the residual cost rather than supplying a cheap generating quotient.

## 7. Exact smallest unclosed step

**EQUIVALENT_BLOCKER, conditional on H77.** The requested target is equivalent to the following statement:

For every \(\epsilon>0\), there are a free extension \(Y\to B\), an \(S_F^Y\)-complete set \(A\), and a graphing \(\Psi\) of the **full induced relation** \(R_Y|A\) such that
\[
\boxed{C_\mu(\Psi)\le\beta+\mu(A)+\epsilon.} \tag{21}
\]

**Sufficiency.** Keep only a rooted forest inside \(S_F^Y\) leading to \(A\), of cost \(1-\mu(A)\), and add \(\Psi\). This generates \(R_Y\) with cost at most \(1+\beta+\epsilon\). Taking the group infimum and using (1) proves equality.

**Necessity.** If \(C(\Gamma)=1+\beta\), (18) gives an extension with cost within \(\epsilon/2\) of this value. Choose an \(S_F^Y\)-complete marker section and apply (13). A graphing within \(\epsilon/2\) of the induced cost satisfies (21).

This endpoint permits deleting and replacing forest edges, arbitrary partial full-relation maps, and arbitrary free extensions. It is not restricted to connected DPP approximants. It is also explicitly an **equivalent blocker**, not a proved new hypothesis.

H77 supplies the treeing and its dimension budget, but no argument above produces the full induced graphing required in (21). Equality of closed \(L^2\) spans is not finite-path generation of an equivalence relation. At \(\beta=0\), (19) identifies the precise residual gap; for positive \(\beta\), (21) allows the less restrictive edge-replacement route. Neither gap is closed.

**Target status: INCOMPLETE.** The interface conditional on H77, the compression and extension identities, and the finite-overlap obstruction are established above. None is presented as a solution of the target.

### Primary references

The cited inputs are Gaboriau, *Coût des relations d’équivalence et des groupes*, Invent. Math. **139** (2000), 41–98 [G00]; Gaboriau, *Invariants \(l^2\) de relations d’équivalence et de groupes*, Publ. Math. IHÉS **95** (2002), 93–150 [G02]; Abért–Weiss, *Bernoulli actions are weakly contained in any free action*, ETDS **33** (2013), 323–333 [AW]; Benjamini–Lyons–Peres–Schramm, *Uniform spanning forests*, Ann. Probab. **29** (2001), 1–65 [BLPS]; Lyons, *Determinantal probability measures*, Publ. Math. IHÉS **98** (2003), 167–212 [L03]; Lyons’s ICM2014 *Determinantal Probability: Basic Properties and Conjectures* [L14]; and Bekka–Valette, *Group cohomology, harmonic functions and the first \(L^2\)-Betti number*, Potential Anal. **6** (1997), 313–326 [BV97].

