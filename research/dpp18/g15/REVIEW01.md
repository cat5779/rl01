# Adversarial review of the RL01 #122 partial-results packet

## Review status

This is an adversarial self/re-review of RESULT.md. It is not an independent external referee report and not formal verification.

The review was aimed specifically at hidden quantifier changes, dimension-dependent constants, invalid active-set reasoning, sign errors in the signed-current energy, and examples that only refute one optimizer while being presented as selector-independent.

Conclusion: no contradiction was found in the claims retained in RESULT.md. Several tempting overclaims are explicitly rejected below. The unrestricted HSEL theorem remains open.

## 1. Scope audit against the frozen task

The frozen task requires one Borel, coordinate-permutation-equivariant selector in the positive-part-dominated endpoint fibers, with a constant independent of ambient dimension and with unrestricted projector support.

The packet does not replace this fiber by the larger original birth-flow fiber, does not assume a common projector, and does not infer a global selector from pairwise repair.

The bounded-support theorem is explicitly restricted. The all-dimensional energy results are not described as selection theorems. The noise and polynomial examples are not described as HSEL counterexamples.

## 2. Minimum-correction selector: exact feasibility

Write \(f=J+h\). Exact source and target marginals are preserved iff the correction has zero sum at every source and every target. With the source-target oriented incidence matrix this is exactly
\[
Bh=0.
\]

Edgewise,
\[
-J\le h\le |J|
\]
is equivalent to
\[
0\le J+h\le J+|J|=2J_+.
\]
Thus feasible corrections are in bijection with the frozen fiber. Nonemptiness is inherited from the audited max-flow theorem, and the Euclidean objective is strictly convex.

No Lipschitz conclusion is inferred from strong convexity alone.

## 3. Box-circulation lemma: active-set and degeneracy attack

The dangerous shortcut would be to invoke a generic Hoffman or active-set condition number and silently assume it is dimension free. The proof in RESULT.md does not do that.

On a fixed face, active coordinates are fixed at affine lower or upper bounds. Free coordinates solve the minimum-norm equality problem. Their derivative therefore belongs to the range of the free incidence transpose and is a potential flow.

Orient each nonzero free derivative edge by its sign. Potential changes strictly along every directed edge, hence no directed cycle can occur. The flow decomposes into simple source-to-sink paths. If the component has at most \(N\) vertices, each path has at most \(N-1\) edges.

The total path mass is one half of the \(\ell^1\) divergence. Each active edge contributes at most twice its absolute derivative to that divergence, so total path mass is at most the active derivative mass. This yields the factor \(N\).

There are finitely many active patterns. Their validity regions are polyhedral; uniqueness makes the affine formulas agree on overlaps. Subdividing an interpolation segment handles degenerate switching points.

The remaining factor is graph size, not an untracked matrix condition number.

## 4. Three-coordinate theorem: sign attack

On the only nontrivial three-coordinate component, every correction is
\[
t(1,-1,1,-1,1,-1).
\]

If all current edges are nonnegative, zero correction is feasible. If an edge \(e\) is negative, its capacity is zero and forces
\[
t=-s_ej_e.
\]
Thus a negative edge fixes the circulation parameter.

For two currents let \(d=t(j)-t(k)>0\). If \(t(j)>0\), choose a negative edge of \(j\) with \(s_e=1\). Then
\[
j_e=-t(j)
\]
and feasibility of the corrected \(k\) gives
\[
k_e\ge-t(k).
\]
Hence \(j_e-k_e\le-d\). Adding \(d\) on this edge reduces the absolute difference by exactly \(d\).

If \(t(j)\le0\), then \(t(k)<0\). Choose a negative edge of \(k\) with \(s_e=-1\). The same argument gives an edge on which the absolute difference decreases by exactly \(d\).

At most five other edges gain \(d\), so total difference gains at most \(4d\). The distinguished edge also gives \(d\le\|j-k\|_1\). Thus the factor five is valid. The case \(d<0\) follows by symmetry.

## 5. Cross-support attack

A nonzero correction under the support-at-most-three hypothesis lives on a three-coordinate support. If supports \(D,D'\) differ, choose \(i\in D\setminus D'\). The second current is identically zero in direction \(i\).

On each six-cycle, a nonzero parameter \(t\) forces every edge magnitude to be at least \(|t|\). In particular the two edges in direction \(i\) carry at least \(2|t|\), while the full correction has mass \(6|t|\). Hence
\[
\|h\|_1
\le3\|(J-J')_{\text{direction }i}\|_1.
\]

If the other correction is also nonzero, use a direction in \(D'\setminus D\); the two direction sets are disjoint. Therefore the sum of correction norms is at most three times the full current difference. Adding the current difference gives factor four across different supports. The factor-five same-support estimate remains the global restricted constant.

## 6. Signed-energy theorem: negative-edge attack

The most suspicious claim is
\[
\sum_eJ_e(\Delta\phi_e)^2\ge0
\]
despite negative current edges.

The proof is not entrywise. In the fermionic endpoint representation,
\[
\mathcal E
=
\operatorname{tr}\rho_0(F-U^*GU)^2.
\]
The square is positive and \(\rho_0\ge0\), so the energy is nonnegative.

The current used in the cross term is exactly the real part of the source-target matrix coefficient
\[
U_{T,S}(\rho_0U^*)_{S,T},
\]
and the two diagonal terms are exactly the source and target marginals. Thus no negative edge is discarded.

## 7. Equality case of signed energy

The state \(\rho_0\) is strictly positive on the marked-empty sector because all unmarked eigenmode occupation probabilities lie strictly between zero and one.

If the energy vanishes, the operator difference vanishes on that sector. Particle-number separation forces the source diagonal operator \(F\) to preserve the marked-empty sector, hence commute with the marked-mode projection.

For full coordinate support, the marked-mode projection has nonzero off-diagonal entries between configurations differing by one coordinate exchange. The Johnson graph is connected, so all source potential values coincide.

The target operator must have the same constant because every target coordinate basis vector has nonzero projection on the marked-occupied sector. This also covers the bottom and top layers.

No additional null directions remain.

## 8. Strict cuts: quantitative overclaim rejected

The exact cut identity is
\[
\operatorname{slack}(\mathcal A,\mathcal B)
=
\mathcal E(\mathbf1_{\mathcal A},\mathbf1_{\mathcal B})
+
2\sum_{\mathcal A\to\mathcal B^c}J_-.
\]

The energy is strictly positive for every nontrivial cut under full support. Thus nontrivial cuts are strict, the positive-current graph is connected, and a relative interior feasible flow exists.

However, the smallest strict slack may tend to zero with dimension. The review found no argument for a uniform interior radius. RESULT.md therefore does not use strict feasibility as a substitute for a Lipschitz bound.

## 9. Fixed-projector density comparison: noncommutativity attack

For a background kernel \(B\) on the orthogonal complement of the marked vector,
\[
\sigma_B
=
\det(I-B)\Gamma(B(I-B)^{-1}).
\]

Along a possibly noncommuting Hermitian path \(B_t\), exterior-power differentiation gives
\[
\sigma_t^{-1/2}\dot\sigma_t\sigma_t^{-1/2}
=
d\Gamma(M_t)-\operatorname{tr}(B_tM_t)I.
\]

This identity was independently checked numerically on small noncommuting matrices during the review.

Every eigenvalue of \(d\Gamma(M_t)\) is a subset sum of eigenvalues of \(M_t\). The scalar \(\operatorname{tr}(B_tM_t)\) lies between the total negative and total positive eigenvalue sums because \(0\preceq B_t\preceq I\). Hence
\[
\left\|
d\Gamma(M_t)-\operatorname{tr}(B_tM_t)I
\right\|_{op}
\le\|M_t\|_1.
\]
This yields the stated dimension-free Loewner comparison without requiring \(B_t\) and \(\dot B_t\) to commute.

## 10. Changing projectors: Fock-dimension attack

Choose phases so marked vectors \(v,w\) have nonnegative inner product. The minimal unitary \(W\) sending \(v\) to \(w\) is identity off their two-dimensional span and has nontrivial eigenvalues \(e^{\pm i\theta}\).

In every exterior power, products involving neither or both nontrivial eigenvectors equal one; products involving exactly one give \(e^{\pm i\theta}\). Therefore
\[
\|\Gamma(W)-I\|_{op}
=
\|W-I\|_{op}
=
\|v-w\|.
\]
There is no hidden Fock-space dimension factor.

Also
\[
\|U_v-U_w\|_{op}=\|v-w\|,
\]
by the canonical anticommutation relation for creation plus annihilation of \(v-w\).

Combining these facts with the fixed-projector square-root-density bound gives the claimed square-root cut-energy stability. The rank-one projector relation after phase alignment safely gives
\[
\|v-w\|\le\|P-Q\|_1.
\]

Again, this controls energy, not a selected flow.

## 11. Entropy center: unresolved inverse problem is genuine

The weighted entropy center is a legitimate unique Borel and equivariant selector. Its potential Hessian is
\[
L_c
=
B\operatorname{diag}
\left(
f_e\left(1-\frac{f_e}{u_e}\right)
\right)
B^*,
\qquad u_e=2J_e.
\]

The proved positive quadratic form is instead the signed-energy matrix
\[
L_J=B\operatorname{diag}(J_e)B^*.
\]

Strict feasibility only says the coefficients in \(L_c\) are positive on positive-current edges. It does not give a dimension-free comparison \(L_c\succeq cL_J\), nor any other uniform inverse bound.

No step in the packet silently identifies these matrices. This is the main unresolved analytic interface.

## 12. Obstruction audit

### Noise covariance

The starting three-coordinate capacity fiber is a singleton. Therefore the bit-flip example is selector independent for the extra demand
\[
\Theta(K_\eta,P)=\mathcal N_\eta\Theta(K,P).
\]
At the transformed input a specific current edge is negative while the transported singleton flow is positive, so exact covariance is impossible.

HSEL does not require this covariance. The example is not a HSEL counterexample.

### High polynomial degree

The fixed-gap family forces every feasible flow to have a normalized coordinate slice proportional to
\[
\prod_{j=1}^m(1-x_j),
\]
so the unique multilinear representation has degree \(m\). This is selector independent for the claim that fixed-degree normalized polynomial formulas cannot cover all inputs.

The forced mass decays with \(m\). No \(\ell^1\) instability follows, so this is not a HSEL counterexample.

### Electrical repair

The electrical candidate preserves endpoint marginals but is exactly negative on a positive-current edge in a four-coordinate example. This is a failure of one formula only.

### Abstract long cycle

The earlier abstract long-cycle family produces large forced ratios but is not a genuine DPP obstruction. Its endpoint structure does not satisfy the genuine DPP constraints used in the frozen theorem. It is therefore excluded from the negative conclusion.

## 13. Computational rerun

The exact scripts were rerun in the current research session instead of relying only on earlier logs.

The bounded-support checker returned
PASS_SCOPED_EXACT_CHECKS.

Its checks include the exact three-coordinate example under all six coordinate permutations, fixed-kernel projector variations, cross-support comparisons, and abstract six-cycle comparisons.

The continuation checker returned
PASS_EXACT_SCOPED_CHECKS.

It rechecks layered max-flow cuts on the test instances, strict interior flows, signed-Laplacian positivity, exact bit-flip identities, the high-degree family, and the exact negative electrical candidate while verifying endpoint marginals remain correct.

A separate floating complex-Hermitian diagnostic was used only to cross-check formulas and was not treated as proof.

## 14. Review conclusion

The retained partial theorems survive the adversarial checks above.

The packet still lacks both acceptable ways to close the frozen theorem:

1. a single unrestricted-support selector with a dimension-free \(\ell^1\) Lipschitz modulus; or
2. a selector-independent finite family of genuine admissible DPP inputs forcing every feasible selection to violate every fixed constant.

Accordingly the only defensible overall status is **OPEN / PARTIAL**.
