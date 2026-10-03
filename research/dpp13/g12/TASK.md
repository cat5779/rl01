# Dimension-free Hausdorff stability of full DPP birth-flow polytopes

## Frozen set-valued theorem

Fix \(0<\varepsilon<1/2\). For finite \(E=\{1,\ldots,n\}\), a Hermitian kernel
\[
\varepsilon I\le K\le(1-\varepsilon)I,
\]
and a rank-one projector \(P\), let \(\mathcal F(K,P)\) be the full polytope of nonnegative upward Boolean-cube edge flows with divergence
\[
b_{K,P}(S)=\left.\frac d{dh}p_{K+hP}(S)\right|_{h=0},
\]
total mass one, and pointwise outgoing capacity
\[
F_{\rm out}(S)\le\frac2\varepsilon p_K(S).
\]

Let \(d_H^{(1)}\) denote Hausdorff distance in edge \(\ell^1\).

Prove or disprove:

> There exists \(H_\varepsilon<\infty\), independent of \(n\), such that
> \[
> d_H^{(1)}\bigl(\mathcal F(K,P),\mathcal F(L,Q)\bigr)
> \le
> H_\varepsilon
> \bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
> \tag{HDF}
> \]
> for all admissible pairs on the same \(E\).

Both directions may have full and genuinely unbounded coordinate support. The infimum in the Hausdorff distance is over the entire target fiber, not a chosen optimizer or a half-capacity subpolytope.

A disproof of (HDF) by a pairwise family automatically disproves every dimension-free Lipschitz selector. A proof of (HDF) is only a set-valued advance; it does not by itself construct a globally compatible permutation-equivariant selector.

## Audited inputs

You may use the following scoped results.

1. With \(h=\varepsilon/2\), the entire flow polytope is affinely equivalent to equality-or-one-point-cover couplings between
   \[
   p_K,\qquad p_{K+hP}.
   \]
   The original capacity is exactly the nonnegativity of the diagonal coupling mass.
2. Fixed-gap DPP atoms have dimension-free multiplicative regularity under trace-norm perturbations, including adjacent-atom ratio bounds depending only on \(\varepsilon\).
3. Coordinate directions have singleton fibers, and every fiber collapses linearly in \(\ell^1\) near a coordinate direction.
4. If
   \[
   |\operatorname{supp}(P)\cup\operatorname{supp}(Q)|\le m,
   \]
   then
   \[
   d_H^{(1)}(\mathcal F(K,P),\mathcal F(L,Q))
   \le
   H_m\left(
   \frac{12}{\varepsilon}\|K-L\|_1
   +2\|P-Q\|_1
   \right),
   \]
   where \(H_m<\infty\) is independent of ambient \(n\) but may depend badly on \(m\).
5. If a direction has tail mass \(\eta\) outside a fixed \(m\)-set, there is an absolute attraction estimate of order
   \[
   \eta+H_m\bigl(4\sqrt\eta+2\eta\bigr).
   \]
   This does not control the ratio to a much smaller parameter distance.
6. A dimension-free signed divergence repair and dimension-free capacity-vector stability are available. They do not preserve nonnegativity automatically.
7. Abstract diagonal-plus-cover coupling graphs can have condition number growing linearly with path length, but known thin-path examples have zero marginals and are not fixed-gap DPP fibers.

## Exact new obligation

Remove the bounded-support dependence \(H_m\), or prove that it cannot be removed within genuine fixed-gap DPP fibers.

A positive proof must explain how fixed-gap atom regularity and the many alternative cube routes prevent long alternating-path amplification uniformly in the support size. A generic finite-dimensional Hoffman bound, division by the least atom, or equivalence of \(\ell^1\) and Euclidean norms is insufficient.

A negative proof must give explicit or exactly parameterized fixed-gap kernels and rank-one projectors such that the ratio in (HDF) diverges. Numerical LP can guide the construction, but the final lower bound must be exact and apply to the entire two fibers.

Do not claim that small tail mass alone settles the problem unless its scale is compared to
\[
\|K-L\|_1+\|P-Q\|_1.
\]
Do not replace pairwise Hausdorff distance by failure of one selector, one convex objective, or one coupling.

## Scope

(HDF) is strictly weaker than the unrestricted selector theorem on the positive side. It is strong enough to refute that theorem on the negative side through a diverging pairwise certificate. Keep this logical asymmetry explicit.

Return exactly one of PROVED, DISPROVED, or INCOMPLETE, followed by a complete supporting argument. If incomplete, give the strongest exact full-support estimate or DPP-realizable obstruction obtained and state precisely why it does not settle (HDF).
