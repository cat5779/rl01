# Positive capacitated repair for rank-one DPP birth flows

## Frozen target

Fix \(0<\varepsilon<1/2\). For every finite set \(E=\{1,\dots,n\}\), every complex Hermitian matrix

\[
\varepsilon I\le K\le(1-\varepsilon)I,
\]

and every rank-one projector \(P=vv^*\), let \(p_K(S)\) be the exact DPP probability and

\[
b_{K,P}(S)=\left.\frac d{dh}p_{K+hP}(S)\right|_{h=0}.
\]

Let \(\mathcal F(K,P)\) be the set of nonnegative upward Boolean-cube edge flows \(F(S,i)\), \(i\notin S\), satisfying

\[
b_{K,P}(S)=\sum_{i\in S}F(S\setminus\{i\},i)-\sum_{i\notin S}F(S,i),
\]

\[
\sum_{S,i\notin S}F(S,i)=1,
\qquad
\sum_{i\notin S}F(S,i)\le \frac2\varepsilon p_K(S).
\tag{1}
\]

Prove or disprove the following selection theorem. There is a constant \(C_\varepsilon<\infty\), independent of \(n\), and a selection

\[
(K,P)\longmapsto F_{K,P}\in\mathcal F(K,P)
\]

which is Borel, depends only on \(P\), commutes with every permutation of \(E\), and satisfies

\[
\|F_{K,P}-F_{L,Q}\|_{\ell^1(\text{edges})}
\le C_\varepsilon\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
\tag{DF}
\]

for every two admissible pairs on the same \(E\). Here \(\|\cdot\|_1\) on matrices is the unnormalized trace norm.

The preferred route is a genuinely nonnegative, capacitated repair or a canonical optimal-transport selector. A counterexample must rule out every selector, not merely one optimizer or tie-breaking rule.

## Audited facts that may be used

1. \(\mathcal F(K,P)\ne\varnothing\). For \(h=\varepsilon/2\), its elements are exactly the off-diagonal masses divided by \(h\) of monotone couplings of \(\operatorname{DPP}(K)\) and \(\operatorname{DPP}(K+hP)\) supported on \((S,S)\) and \((S,S\cup\{i\})\). Feasibility is a standard consequence of nested projection coupling and support-minimal dilation; see Lyons, *Determinantal Probability Measures* (2003), Proposition 10.3.
2. For finite DPPs,

   \[
   W_1(\mu_A,\mu_B)\le\|A-B\|_1,
   \qquad
   \sum_S|p_A(S)-p_B(S)|\le2\|A-B\|_1.
   \tag{2}
   \]

   Boundary kernels follow by \(A_\eta=(1-2\eta)A+\eta I\) and finite-state continuity.
3. Boolean-cube Kantorovich--Rubinstein duality yields a signed upward-edge flow \(G\) with

   \[
   \operatorname{div}G=b_{K,P}-b_{L,Q},
   \qquad
   \|G\|_1\le \frac4\varepsilon\|K-L\|_1+\|P-Q\|_1.
   \tag{3}
   \]

   The capacity vectors also satisfy

   \[
   \sum_S\left|\frac2\varepsilon p_K(S)-\frac2\varepsilon p_L(S)\right|
   \le\frac4\varepsilon\|K-L\|_1.
   \tag{4}
   \]

4. Diagonal kernels and coordinate birth directions admit explicit selectors with constant \(2\). These do not settle the general case.
5. For a fixed non-diagonal \(K\), no selector valid for all rank-one \(P\) can be both positive and linear in \(P\). This is only a method obstruction: nonlinear selectors remain possible.

## Exact new obligation

Turn (3)--(4) into a nonnegative repair satisfying (1), with a dimension-free bound and one globally consistent selector. It is not enough to prove pointwise feasibility, a signed correction, a Hausdorff estimate without a selector, or fixed-\(n\) continuity. Any proposed convex optimizer must be shown to retain a dimension-free modulus even when the feasible flow lies on a high-codimension face with many zero edges.

Do not divide by \(\min_S p_K(S)\), hide an exponential dependence on \(n\), or add finite-range, commuting, diagonal, fixed-direction, or bounded-dimension hypotheses to the frozen conclusion. If the full theorem remains open, isolate a strictly weaker proved lemma that advances the positive-repair step and state whether it is sufficient, necessary, equivalent, or incomparable to (DF).

## Output standard

Return exactly one of `PROVED`, `DISPROVED`, or `INCOMPLETE`, followed by a complete supporting argument. A disproof must give an explicit admissible family with the common spectral gap and a quantitative lower bound applying to every selector. A proof must verify nonnegativity, divergence, capacity, normalization, Borel dependence, permutation covariance, and the dimension-free Lipschitz estimate. Distinguish established sources from new claims.
