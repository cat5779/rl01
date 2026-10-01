# Independent adversarial audit of the LG response

STATUS: **CORRECT**

## Scope of the verdict

No critical mathematical gap was found in the claims made in the response, with particular scrutiny of the FUSF interface in Section 2, the finite-overlap estimates (5), (6), and (9), the \(F_2\times F_2\) stress test, the relative-cost identities (14)--(16), the extension infimum (17)--(19), and the equivalence in (21). The Section 6 quotient calculation was also checked for consistency with the compression convention.

This verdict has the following exact boundary.

- It accepts the response's status **INCOMPLETE**: the Lyons--Gaboriau target is neither proved nor disproved.
- It does not prove H77. Every construction of a Bernoulli FUSF subrelation, and every later statement using its lift, remains conditional on H77 exactly as stated.
- It does not certify novelty. `PROVED_HERE` is read only as “a proof is supplied here.”
- It does not turn the group-cost infimum into fixed price. The response correctly distinguishes those quantifiers.

## 1. FUSF interface and multigraph conventions

The edge-occurrence set \(E=\Gamma\times[d]\) is a free \(\Gamma\)-set under left translation. Treating occurrences as unoriented edges is legitimate. If \(s_i^2=e\), the occurrences \((g,i)\) and \((gs_i,i)\) are different parallel edges; together they form a two-edge cycle, so a forest cannot contain both. Thus involutions do not create an edge stabilizer or a duplicated graphing edge.

For \(Q_F=P_{\mathcal C^\perp}\), a finite cycle vector lies in the kernel of its compression, so the corresponding inclusion determinant vanishes. For finite nonempty \(K\), the finitely supported cut gradient \(d1_K\) lies in \(\mathcal C^\perp\), is supported on the edge boundary, and is fixed by the boundary compression. Hence the boundary-avoidance determinant vanishes. Taking the countable union over finite \(K\) proves that every FUSF component is infinite.

On an essentially free Bernoulli base, the partial maps attached to the event \((e,i)\in F\) reproduce the forest graphing under the coordinate map \(g\mapsto g^{-1}x\). Base freeness is exactly what is needed to prevent unintended orbit identifications; freeness of the forest factor is neither used nor claimed. The graphing is a treeing, and its cost is the free-label trace \(\sum_i Q_F((e,i),(e,i))=1+\beta_1^{(2)}(\Gamma)\). This part is conditional on H77 only at the factor-realization step.

## 2. Finite-overlap theorem

Let \(W_x\) denote independent full random walks started at the indicated vertices. The elementary range-intersection bound is
\[
\Pr(\operatorname{Ran}W_x\cap\operatorname{Ran}W_y\ne\varnothing)
\le \sum_u G_0(x,u)G_0(y,u)
=h(x^{-1}y).
\]
Since \(G_0\) is bounded on \(\ell^2\), \(G_0^2\delta_e\in\ell^2\), so \(h\in\ell^2(\Gamma)\).

For (9), run Wilson's algorithm rooted at infinity with initial order
\[
e,\ z,\ s,\ zs.
\]
On the event
\[
e\leftrightarrow z,\qquad s\leftrightarrow zs,\qquad e\not\leftrightarrow s,
\]
the first connection forces \(\operatorname{Ran}W_e\cap\operatorname{Ran}W_z\ne\varnothing\), while the second forces \(\operatorname{Ran}W_s\cap\operatorname{Ran}W_{zs}\ne\varnothing\). Later Wilson walks cannot merge two already constructed components. These two range events depend on disjoint pairs of independent walks, hence their probabilities multiply. The starting-point difference in the second pair is
\[
s^{-1}(zs)=s^{-1}zs,
\]
which is the required conjugate. No right-translation invariance of the Cayley network is used.

Repeated seeds are fully covered. If \(z=e\), the desired estimate is the trivial bound by \(h(e)^2\ge1\). If \(z=s\) or \(z=s^{-1}\), the event contradicts \(e\not\leftrightarrow s\) and is empty. Thus (9) holds for every \(z\). Summing gives
\[
\sum_z h(z)h(s^{-1}zs)\le \|h\|_2^2
\]
by Cauchy--Schwarz, since conjugation is a bijection. This proves (5).

For two independent WUSFs, the two connection events are independent across the two forest samples, and the two-seed estimate gives
\[
\mathbb E|C_{F_1}(e)\cap C_{F_2}(e)|
=\sum_z\Pr(e\leftrightarrow z)^2
\le\sum_z h(z)^2,
\]
which is (6). This does not assert independence of connection events inside one forest.

The orbit-coordinate calculation is also correct: with \(\phi_s(x)=s^{-1}x\), the \(E_{\phi_s}\)-class of \(x\) is indexed by
\[
\{g:g\in C_F(e),\ gs\in C_F(s)\}
=C_F(e)\cap C_F(s)s^{-1}.
\]
Finite expectation on the positive-measure disconnection event therefore gives finite \(E_{\phi_s}\)-classes there. The mass-transport lower bound in (10) rules out complete sections of arbitrarily small measure for those finite classes.

## 3. The \(F_2\times F_2\) stress test

The direct graphing argument for fixed price one is valid. Keep the full \(a\)-map. Restrict the commuting \(c,d\)-maps to small complete sections for the \(a\)-orbit relation, which recovers their full maps by conjugating along powers of \(a\). Once the full \(c\)-map is available, restrict \(b\) to a small complete section for the \(c\)-orbit relation and recover the full \(b\)-map by commutation. This gives cost \(1+\varepsilon\), while aperiodicity gives the lower bound one.

Consequently \(\beta_1^{(2)}(F_2\times F_2)=0\). The wired projection is below the free projection and their trace difference is \(\beta_1^{(2)}\); faithfulness of the group trace therefore gives FUSF = WUSF. For the standard product Cayley network, the walk operator is the average of the two four-regular-tree walk operators, each of norm \(\sqrt3/2\), so its norm is strictly below one. Hence (5) applies to this FUSF. The example correctly separates failure of the finite-intersection certificate from the existence of unrestricted cheap graphing repairs.

## 4. Relative-cost compression

The projection argument behind (14) preserves cost. Choose a Borel root map \(r:X\to A\) with graph in \(S\), and partition it into countably many injective partial pmp pieces. For a repair map \(\psi\), split its domain simultaneously according to an injective source piece of \(r\) and an injective target piece on \(\psi(D)\). On each such piece the projected map
\[
r\circ\psi\circ(r|_D)^{-1}
\]
is a partial pmp bijection on \(A\), with domain measure exactly \(\mu(D)\). Projecting an alternating \(S\)/repair path gives an \(S|A\)/projected-repair path, so the projected maps generate \(R|A\). Conversely, an induced repair on \(A\), together with \(S\), repairs all of \(R\) by moving both endpoints to roots. This proves both inequalities in (14), without normalized measure.

The ordinary compression identity in the same convention is
\[
C_\mu(R|A)=C_\mu(R)-1+\mu(A).
\]
Combining it with (14) yields the upper bound in (15); adjoining a chosen cost-\(c\) graphing of \(S\) to an arbitrary repair gives the lower bound. When \(c=1\), the bounds coincide and give (16). There is no illicit claim that normalization makes the residual cost small.

For Section 6, the component-label bins are \(R\)-complete but not \(S\)-complete. Applying ordinary compression separately to the \(n\) bins and summing gives
\[
C(T_n)=n\bigl(C(R)-1+1/n\bigr)=1+n(C(R)-1),
\]
so the stated amplification direction is correct.

## 5. Extensions and the group infimum

If \(Y\to X\) is an equivariant extension and the base action on \(X\) is free, the map from each \(Y\)-orbit to its base orbit is bijective. A partial base-relation map can therefore be partitioned by its unique implementing group element and lifted on each piece with the same domain measure. A word in the lifted graphing has the required group element because the base action is free. Thus
\[
C(R_Y)\le C(R_X),
\]
and the same class-bijective lifting works for relative repairs.

For every free action \(a\), the product \(B\times a\) is an extension of both \(B\) and \(a\). Hence
\[
C(\Gamma)\le \inf_{Y\to B}C(R_Y)\le C(R_{B\times a})\le C(R_a).
\]
Taking the infimum over \(a\) proves (18). A countable product with a sequence of actions approaching \(C(\Gamma)\) indeed attains the infimum. This is an infimum over extensions of the Bernoulli action; it does not say that every free action has the same cost.

When \(\beta=0\), the lifted forest subrelation has cost one, so (16) applies separately to every extension:
\[
\rho(R_Y:S_F^Y)=C(R_Y)-1.
\]
Taking the extension infimum and using (18) proves (19). This statement remains conditional on the H77 construction of \(S_F\).

## 6. Equivalent blocker (21)

The two directions have the correct quantifiers.

- If (21) holds, retain a rooted subforest of \(S_F^Y\) leading to \(A\), of cost \(1-\mu(A)\), and add the full graphing of \(R_Y|A\). The result generates \(R_Y\) with cost at most \(1+\beta+\varepsilon\). The universal lower bound then gives \(C(\Gamma)=1+\beta\).
- Conversely, if \(C(\Gamma)=1+\beta\), (18) supplies an extension \(Y\to B\) with cost arbitrarily close to that value. Choose an \(S_F^Y\)-complete marker section and apply ordinary compression. An induced graphing arbitrarily close to the induced cost satisfies (21).

Thus (21) is genuinely equivalent to the desired group-cost equality, conditional on H77. The response correctly says that none of its preceding arguments constructs the graphing required by (21).

## Primary sources checked

- D. Gaboriau, [*Coût des relations d'équivalence et des groupes*](https://perso.ens-lyon.fr/gaboriau/Travaux-Publi/Cout/Cout.pdf), Invent. Math. 139 (2000), 41--98: graphing cost, treeings, cost, and compression framework.
- D. Gaboriau, [*Invariants \(\ell^2\) de relations d'équivalence et de groupes*](https://www.numdam.org/item/10.1007/s102400200002.pdf), Publ. Math. IHÉS 95 (2002), 93--150: the \(\ell^2\)-Betti lower bound for cost and the free-action identification.
- M. Abért and B. Weiss, [*Bernoulli actions are weakly contained in any free action*](https://arxiv.org/abs/1103.1063), especially Theorem 1 and Corollary 2: Bernoulli actions have maximal cost among free actions of a finitely generated group.
- I. Benjamini, R. Lyons, Y. Peres, and O. Schramm, [*Uniform spanning forests*](https://doi.org/10.1214/aop/1008956321), Ann. Probab. 29 (2001), 1--65, especially Theorem 5.1: Wilson's algorithm rooted at infinity and the free/wired forest framework.
- R. Lyons, [*Determinantal probability measures*](https://pmihes.centre-mersenne.org/articles/10.1007/s10240-003-0016-0/), Publ. Math. IHÉS 98 (2003), 167--212: determinantal measures associated with projections and their spanning-forest applications.
- M. E. B. Bekka and A. Valette, [*Group cohomology, harmonic functions and the first \(L^2\)-Betti number*](https://doi.org/10.1023/A:1017974406074), Potential Anal. 6 (1997), 313--326: the property-(T) input for vanishing first \(L^2\)-Betti number.
