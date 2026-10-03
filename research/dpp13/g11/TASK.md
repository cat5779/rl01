# Dimension-free positive selector for two-coordinate rank-one directions

## Frozen restricted theorem

Fix \(0<\varepsilon<1/2\). For every finite \(E=\{1,\ldots,n\}\), every Hermitian
\[
\varepsilon I\le K\le(1-\varepsilon)I,
\]
and every rank-one projector \(P=vv^*\), let
\[
b_{K,P}(S)=\left.\frac d{dh}p_{K+hP}(S)\right|_{h=0}.
\]
Let \(\mathcal F(K,P)\) be the polytope of nonnegative upward Boolean-cube edge flows satisfying
\[
b_{K,P}(S)
=
\sum_{i\in S}F(S\setminus\{i\},i)
-
\sum_{i\notin S}F(S,i),
\]
\[
\sum_{S,i\notin S}F(S,i)=1,
\qquad
\sum_{i\notin S}F(S,i)\le \frac2\varepsilon p_K(S).
\]

Write
\[
\operatorname{supp}(P)=\{i:P_{ii}>0\}.
\]

Prove or disprove the following restricted statement:

> There is a constant \(C_\varepsilon^{(2)}<\infty\), independent of \(n\), and a Borel permutation-equivariant selection
> \[
> (K,P)\longmapsto F_{K,P}\in\mathcal F(K,P)
> \]
> on the domain \(|\operatorname{supp}(P)|\le2\), depending only on \(P\), such that
> \[
> \|F_{K,P}-F_{L,Q}\|_1
> \le
> C_\varepsilon^{(2)}
> \bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
> \tag{DF2}
> \]
> whenever both \(P,Q\) have support at most two.

The theorem must compare different supports, including two supports meeting in one coordinate, disjoint supports, and degeneration from a two-coordinate direction to a coordinate projector.

This is a restricted theorem only. It does not settle the unrestricted selector problem for full-support rank-one directions.

## Candidate mechanism to verify or replace

A candidate proof conditions on the outside pattern. If \(J\subset E\) is the one- or two-coordinate support of \(P\), \(O=E\setminus J\), and \(T\subset O\), the exact DPP law factors as
\[
p_K(T\cup A)=p_{K_O}(T)\,p_{M_T(K)}(A),
\qquad A\subset J,
\]
for a conditional kernel \(M_T(K)\) on \(J\) that retains the spectral gap.

On a genuine two-site system, every unit upward flow has one scalar degree of freedom. A candidate selector clips a permutation-covariant reference scalar to the exact feasibility interval. The intended proof must verify:

1. the two-site formula has the exact divergence and total mass;
2. clipping gives nonnegativity and the outgoing bound, preferably the stronger \(p_M(A)/\varepsilon\);
3. the two-site selector is Lipschitz in \((M,P)\) with a constant depending only on \(\varepsilon\);
4. conditioning and averaging over \(T\) lift the selector without summing a dimension-dependent number of errors;
5. the conditional kernels satisfy a probability-averaged trace-norm stability estimate;
6. coordinate directions are compatible with every auxiliary two-set;
7. the definition is Borel and permutation-equivariant across changing support strata;
8. pairs with disjoint or one-coordinate-overlap supports obey (DF2).

A previous truncated candidate proposed
\[
C_\varepsilon^{(2)}
=
\max\left\{
18,\,
2+(6+4/\varepsilon)
\left[1+\left(\frac{1-2\varepsilon}{2\varepsilon}\right)^2\right]
\right\}.
\]
This constant is not an input: check it line by line, improve it, or replace it with any finite dimension-free \(C_\varepsilon^{(2)}\).

## Audited inputs

You may use:

- finite DPP probabilities are affine along a rank-one line;
- \(\|p_A-p_B\|_1\le2\|A-B\|_1\);
- coordinate birth directions have a unique explicit nonnegative selector with Lipschitz constant \(2\);
- every individual flow polytope is nonempty;
- a signed dimension-free repair exists, but signed repair alone does not prove this theorem.

Do not divide by the least configuration probability, hide dependence on \(n\), or infer the result from failure/success of one convex optimizer.

## Verdict

Return exactly one of PROVED, DISPROVED, or INCOMPLETE, followed by a complete supporting argument. Keep the complete proof under 18,500 characters if possible so no load-bearing tail is lost. PROVED requires all eight items above. DISPROVED requires an obstruction applying to every selector on the restricted domain.
