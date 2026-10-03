# Handoff prompt: stable selection inside endpoint-capacity fibers

Prove or disprove the following frozen theorem. Use only the audited inputs below, and do not weaken the quantifiers or replace a global selector by pairwise choices.

Fix \(0<\varepsilon<1/2\). For every finite coordinate set \(E\), let
\[
\mathcal C_E^\varepsilon
=\{(K,P):\varepsilon I\preceq K\preceq(1-\varepsilon)I,
\ P\text{ rank-one projector},\ KP=PK\}.
\]
For \(x=(K,P)\in\mathcal C_E^\varepsilon\), put
\[
\lambda_x=\operatorname{tr}(KP),\qquad A_x=K-\lambda_xP,
\]
\[
\mu_{0,x}=p_{A_x},\qquad \mu_{1,x}=p_{A_x+P}.
\]
For \(S\subseteq E\), let \(D_{S^c}\) be the diagonal projection onto \(E\setminus S\), and for \(i\notin S\) define
\[
J_x(S,i)=-p_K(S)\operatorname{Re}\bigl(P(K-D_{S^c})^{-1}\bigr)_{ii}.
\]

Let \(\mathcal H_E(x)\) be the set of nonnegative upward edge arrays \(f\) satisfying
\[
\sum_{i\notin S}f(S,i)=\mu_{0,x}(S),\qquad
\sum_{i\in T}f(T\setminus\{i\},i)=\mu_{1,x}(T),
\]
and
\[
0\le f(S,i)\le 2(J_x(S,i))_+.
\tag{H}
\]

Determine whether there exist Borel, coordinate-permutation-equivariant selectors
\[
\Theta_E(x)\in\mathcal H_E(x)
\]
and a finite constant \(C_\varepsilon\), independent of \(|E|\), such that for every pair of commuting inputs \(x=(K,P)\), \(y=(L,Q)\),
\[
\|\Theta_E(x)-\Theta_E(y)\|_1
\le C_\varepsilon\bigl(\|K-L\|_1+\|P-Q\|_1\bigr).
\tag{HSEL}
\]

The following facts may be used:

1. \(J_x\) has exact signed source and target marginals \((\mu_{0,x},\mu_{1,x})\), total signed mass one, and is Borel and permutation-covariant.
2. The capacities in (H) satisfy every bipartite max-flow cut, so \(\mathcal H_E(x)\ne\varnothing\).
3. The signed current is dimension-free stable:
   \[
   \|J_x-J_y\|_1\le \frac{3}{\varepsilon^2}\|K-L\|_1+\frac1\varepsilon\|P-Q\|_1.
   \]
   Hence \(2(J_x)_+\) is dimension-free stable.
4. The unique least-Euclidean-norm point of \(\mathcal H_E(x)\) is continuous for each fixed \(E\), but no dimension-independent active-set constant is known.
5. Pairwise repair is known when \(P=Q\). A positive selector is also known on the scalar-complement subclass \(K=a(I-P)+\lambda P\). Neither result supplies consistency when projectors vary.

A positive proof must construct one selector simultaneously on all fibers, prove (HSEL) without a dimension-dependent Hoffman, active-set, or number-of-cuts factor, and handle zero coordinates, support changes, eigenspace degenerations, Borel dependence, and full permutation covariance. Pairwise transport repair is insufficient unless made globally consistent on every finite family of inputs.

A negative proof must be selector-independent for these restricted fibers: construct finite families of admissible commuting inputs for which every choice of feasible flows violates every fixed dimension-free constant. Instability of one optimizer or one circulation is insufficient.

A negative answer here would concern only the positive-part-dominated endpoint fibers and would not by itself disprove a selector in the larger original flow fibers.

Return `PROVED` or `DISPROVED`, followed by a complete supporting argument.
