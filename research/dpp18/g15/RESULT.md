# RL01 PR #122 — adversarially checked partial results

**Classification: OPEN / PARTIAL.** The unrestricted HSEL theorem from cat5779/rl01#122 is neither proved nor disproved here.

This note consolidates two research passes and a later adversarial re-check. The purpose is to separate four things cleanly:

1. results actually proved for the frozen positive-part endpoint fibers;
2. structural facts that hold in all dimensions;
3. obstructions to particular construction principles;
4. the quantitative interface that remains open.

## 1. Frozen setting

Fix \(0<\varepsilon<1/2\). For a commuting input \(x=(K,P)\), with \(P\) rank one and
\[
\varepsilon I\preceq K\preceq(1-\varepsilon)I,
\]
let \(J_x\) be the signed endpoint current from the frozen task and let \(\mathcal H_E(x)\) be the nonnegative endpoint-coupling fiber with exact source and target marginals and capacities
\[
0\le f(S,i)\le 2(J_x(S,i))_+.
\]

The frozen task supplies nonemptiness of every fiber and
\[
\|J_x-J_y\|_1
\le \frac{3}{\varepsilon^2}\|K-L\|_1
+\frac1\varepsilon\|P-Q\|_1.
\tag{1}
\]

Matrix \(\|\cdot\|_1\) is unnormalized trace norm; edge-array \(\|\cdot\|_1\) is entrywise \(\ell^1\).

## 2. A single global candidate: minimum correction from the signed current

Let \(B\) be the oriented incidence matrix of the source-target bipartite graph: every upward cube edge joins the source copy of \(S\) to the target copy of \(S+i\). A correction \(h\) preserves both endpoint marginals exactly iff
\[
Bh=0.
\]

Define
\[
h(J)=
\operatorname*{argmin}_{Bh=0,\,-J\le h\le |J|}
\frac12\|h\|_2^2,
\qquad
\Theta^{\rm corr}(x)=J_x+h(J_x).
\tag{2}
\]

Since \(J+|J|=2J_+\), the box in (2) is exactly
\[
0\le J+h\le 2J_+.
\]
Thus feasible corrections are in bijection with the frozen fiber. Nonemptiness is inherited from the audited max-flow result, and strict convexity gives uniqueness.

For each fixed finite \(E\), the selector is Borel and coordinate-permutation equivariant. What is not known is a dimension-independent Lipschitz modulus for (2) when the projector support is unrestricted.

## 3. Box-constrained circulation lemma

Let a finite graph have connected components with at most \(N\) vertices. Put
\[
Q(j)=\{h:Bh=0,\ -j\le h\le |j|\}.
\]
Whenever \(Q(j),Q(k)\) are nonempty, their minimum-Euclidean-norm corrections satisfy
\[
\|h(j)-h(k)\|_1\le N\|j-k\|_1,
\tag{3}
\]
and hence
\[
\|(j+h(j))-(k+h(k))\|_1
\le (N+1)\|j-k\|_1.
\tag{4}
\]

Proof sketch. Interpolate the lower and upper bounds linearly. On a fixed active face, the active coordinates are affine in the interpolation parameter and the free coordinates solve a minimum-norm incidence equation. Therefore the free derivative lies in the range of the free incidence transpose, so it is a potential flow. After orienting nonzero free edges by sign, potential changes strictly along every directed edge; there is no directed cycle. Decompose into source-to-sink paths. Each path has at most \(N-1\) edges, while total path mass is at most the \(\ell^1\) mass of the active-edge derivative. Integrating over the finitely many active-face intervals gives (3).

This proof uses no Hoffman constant, smallest singular value, or number-of-active-sets factor. The remaining vertex-count factor is explicit.

## 4. Every fixed projector-support bound

Let
\[
D(P)=\{i:P_{ii}>0\}.
\]
If \(i\notin D(P)\), positivity of the rank-one projector forces the whole \(i\)-th row and column of \(P\) to vanish. Hence
\[
J_x(S,i)=0,
\]
and every feasible flow also vanishes in direction \(i\).

Suppose \(|D(P)|,|D(Q)|\le s\). Only
\[
U=D(P)\cup D(Q),\qquad |U|\le2s,
\]
matters. After fixing the outside configuration and the active cardinality level, each relevant bipartite component has at most
\[
\binom{2s+1}{s}
\]
vertices. Applying (4) on disjoint components gives
\[
\boxed{
\|\Theta^{\rm corr}(x)-\Theta^{\rm corr}(y)\|_1
\le
\left(1+\binom{2s+1}{s}\right)
\|J_x-J_y\|_1.
}
\tag{5}
\]

Combining with (1), every fixed support bound has an ambient-dimension-independent selector modulus. The constant grows with \(s\), so this does not prove unrestricted HSEL.

## 5. Support at most three: factor five

On support size at most two, all nontrivial layer graphs are stars, so the marginals force every edge and the correction is zero.

For a three-coordinate support, only the middle layer has a circulation. It is a six-cycle. Label its edges consecutively and put
\[
s=(1,-1,1,-1,1,-1).
\]
Every marginal-preserving correction is \(ts\). The feasible interval is
\[
I(j)=\{t:0\le j_e+s_et\le2(j_e)_+\text{ for all six edges}\}.
\tag{6}
\]
The selector (2) chooses the point of \(I(j)\) nearest zero.

If all \(j_e\ge0\), then \(t(j)=0\). If some \(j_e<0\), its capacity is zero and therefore
\[
t(j)=-s_ej_e.
\tag{7}
\]
Nonemptiness forces all negative edges to prescribe the same value.

For two currents set \(d=t(j)-t(k)\). If \(d>0\), one can choose a distinguished negative edge from the appropriate current so that adding the correction difference reduces the absolute current difference on that edge by exactly \(d\). On each of the other five edges the absolute difference can increase by at most \(d\). The distinguished edge also gives \(d\le\|j-k\|_1\). Thus
\[
\|T(j)-T(k)\|_1\le5\|j-k\|_1.
\tag{8}
\]
The cases \(d<0\) and \(d=0\) follow by symmetry.

Changing supports is also compatible. If one nonzero six-cycle correction lives on a triple \(D\) and the other support \(D'\) differs, choose \(i\in D\setminus D'\). On every six-cycle, the two edges in direction \(i\) carry at least \(2|t|\) total current mass, while the whole correction has mass \(6|t|\). Since the other current is zero in that direction,
\[
\|h\|_1\le3\|(J-J')_{\text{direction }i}\|_1.
\]
Doing the same for the other support, when needed, uses a distinct direction. Hence different supports have factor at most four, and the same-support factor five dominates.

Therefore, on the whole class \(|D(P)|\le3\),
\[
\boxed{
\|\Theta^{\rm corr}(x)-\Theta^{\rm corr}(y)\|_1
\le5\|J_x-J_y\|_1
\le
\frac{15}{\varepsilon^2}\|K-L\|_1
+\frac5\varepsilon\|P-Q\|_1.
}
\tag{9}
\]

In particular \(15/\varepsilon^2\) is a valid combined-distance constant on this restricted class.

## 6. Exact three-coordinate nontrivial example

Take \(\varepsilon=1/5\),
\[
P=\frac13
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix},
\qquad
K=\frac1{210}
\begin{pmatrix}
72&39&-6\\
39&99&-33\\
-6&-33&144
\end{pmatrix}.
\tag{10}
\]
The matrices commute. The three orthogonal eigen-directions
\[
(1,1,1),\quad(1,2,-3),\quad(-5,4,1)
\]
have eigenvalues \(1/2,4/5,1/5\), so the input has the required gap.

In the consecutive middle-cycle order
\[
(\{1\},2),(\{2\},1),(\{2\},3),
(\{3\},2),(\{3\},1),(\{1\},3),
\]
the exact current is
\[
\frac1{1050}(-1,44,164,239,194,74).
\]
The unique capacity-feasible correction gives
\[
\Theta=
\frac1{1050}(0,43,165,238,195,73).
\]
Thus the restricted theorem is genuinely repairing a negative signed current, not merely renaming an already nonnegative one.

## 7. General-dimensional signed energy

Now assume first that \(P=vv^*\) has full coordinate support. On the \(k\to k+1\) layer, for real source and target potentials \(a_S,b_T\), define
\[
\mathcal E_{K,P}^{(k)}(a,b)
=
\sum_{|S|=k}\sum_{i\notin S}
J(S,i)(a_S-b_{S+i})^2.
\tag{11}
\]

Let \(C\) be exterior multiplication by \(v\), let
\[
U=C+C^*,
\]
and let \(\rho_0\) be the marked-mode-empty fermionic endpoint density matrix. Since \(K\) commutes with \(P\), \(\rho_0\) commutes with the marked-mode projection. For diagonal operators \(F,G\) carrying the potentials,
\[
\boxed{
\mathcal E_{K,P}^{(k)}(a,b)
=
\operatorname{tr}\rho_0(F-U^*GU)^2
\ge0.
}
\tag{12}
\]

The current identity behind (12) is the exact outer-algebra representation
\[
J(S,S+i)
=
\operatorname{Re}
\bigl[
U_{S+i,S}(\rho_0U^*)_{S,S+i}
\bigr].
\]

### Equality case

The state \(\rho_0\) is strictly positive on the marked-empty sector. Hence equality in (12) forces
\[
F\psi=U^*GU\psi
\]
there. Particle-number separation then forces \(F\) to preserve that sector, so it commutes with the marked-mode projection. On a full-support marked vector, the latter has nonzero off-diagonal entries between every pair of Johnson-neighbor configurations. Johnson-graph connectivity therefore forces all source potentials to be constant. Every target basis vector has nonzero projection on the marked-occupied sector, forcing all target potentials to have the same constant.

Thus the nullspace of the signed layer Laplacian consists exactly of constants.

## 8. Strict cuts, connectivity, and relative interior

For source family \(\mathcal A\) and target family \(\mathcal B\), the capacity cut slack has the exact decomposition
\[
\boxed{
\operatorname{slack}(\mathcal A,\mathcal B)
=
\mathcal E_{K,P}^{(k)}
(\mathbf1_{\mathcal A},\mathbf1_{\mathcal B})
+
2\sum_{\substack{S\in\mathcal A\\S+i\notin\mathcal B}}
J(S,i)_-.
}
\tag{13}
\]
Here \(J_-\) is the positive magnitude of the negative part.

Therefore every nontrivial cut is strict under full support. It follows that the graph consisting only of positive-current edges is connected and that there is a feasible flow satisfying
\[
0<f_e<2J_e
\]
on every positive-current edge.

This is qualitative strictness only. The minimum cut slack and the distance to the boundary may still decay with dimension.

If the marked vector has zero coordinates, directions outside its support have zero current. Conditioning on the outside configuration decomposes the problem into active-support blocks. The conditional kernel retains the same spectral gap and still commutes with the restricted projector, so the preceding conclusions apply blockwise.

## 9. Dimension-free energy stability

Write
\[
g=\varepsilon(1-\varepsilon).
\]

### Fixed projector

If \(P\) is fixed and both kernels commute with it, let \(B,B'\) be their restrictions to \(v^\perp\). The associated fermionic background states satisfy
\[
e^{-D_0}\sigma_B\preceq\sigma_{B'}\preceq e^{D_0}\sigma_B,
\qquad
D_0=
\frac{\|B-B'\|_1}{\varepsilon(1-\varepsilon)}.
\tag{14}
\]
Consequently every signed layer Laplacian obeys
\[
e^{-D_0}\mathsf L_{K,P}^{(k)}
\preceq
\mathsf L_{L,P}^{(k)}
\preceq
e^{D_0}\mathsf L_{K,P}^{(k)}.
\tag{15}
\]

### Changing projector

Let \(E_x\) be the energy (11) for a fixed cut indicator pair and let \(E_y\) be the same cut energy for another commuting input \(y=(L,Q)\). Then
\[
\boxed{
|\sqrt{E_x}-\sqrt{E_y}|
\le
\frac{\|K-L\|_1}{2g}
+
\left(3+\frac2g\right)\|P-Q\|_1.
}
\tag{16}
\]

The key dimension-free point is the minimal unitary rotating the marked vector of \(P\) to that of \(Q\). It acts nontrivially only on a two-dimensional plane and has eigenvalues \(e^{\pm i\theta}\). In every exterior power, the only nontrivial products remain \(e^{\pm i\theta}\); selecting both gives one. Hence
\[
\|\Gamma(W)-I\|_{\rm op}
=
\|W-I\|_{\rm op},
\]
with no Fock-space dimension factor.

Equation (16) is an unrestricted all-dimensional stability theorem for the signed energy term. It is not a selector theorem.

## 10. Natural entropy-center selector and the exact remaining bottleneck

The strict interior suggests the weighted binary-entropy center
\[
\Theta^{\rm ent}(x)
=
\operatorname*{argmax}_{f\in\mathcal H_E(x)}
\sum_{e:J_e>0}
2J_e\,
h\!\left(\frac{f_e}{2J_e}\right),
\tag{17}
\]
where \(h(t)=-t\log t-(1-t)\log(1-t)\).

It is unique, Borel, permutation equivariant, and locally smooth on each fixed positive-edge stratum. Its potential-variable Hessian is
\[
\mathsf L_c
=
B\operatorname{diag}(c_e)B^*,
\qquad
c_e=
f_e\left(1-\frac{f_e}{2J_e}\right)>0.
\tag{18}
\]

The available structural control concerns the signed-energy form
\[
\mathsf L_J
=
B\operatorname{diag}(J_e)B^*,
\]
not \(\mathsf L_c\). No dimension-free comparison or alternate inverse estimate has been proved that is strong enough to control the output \(\ell^1\) norm.

**This is the current analytic bottleneck.** Strict cuts, relative-interior feasibility, and dimension-free signed-energy stability do not by themselves imply HSEL.

## 11. Selector-independent obstructions to extra construction principles

These examples use genuine admissible DPP inputs, but they are not counterexamples to HSEL.

### 11.1 Exact bit-flip-noise covariance cannot coexist with the frozen capacities

For
\[
K_\eta=\eta I+(1-2\eta)K,
\qquad 0\le\eta<1/2,
\]
let \(\mathcal N_\eta\) independently flip every coordinate except the edge direction. The signed currents obey the exact identity
\[
\boxed{
J_{K_\eta,P}=\mathcal N_\eta J_{K,P}.
}
\tag{19}
\]
The same operator transports the larger nonnegative endpoint fibers without the pointwise \(2J_+\) constraint.

For the exact three-coordinate example above, the frozen capacity fiber is a singleton \(f\). On the edge \((\{1\},2)\),
\[
J_{K_\eta,P}(e)
=
\frac{-1+114\eta+126\eta^2}{1050},
\]
while
\[
(\mathcal N_\eta f)(e)
=
\frac{112\eta+126\eta^2}{1050}.
\]
At \(\eta=1/1000\), the first quantity is negative and the second positive. The transformed frozen capacity is therefore zero on this edge while the noise-transported flow is positive.

So no global selector can satisfy both the frozen capacities and exact noise covariance. HSEL itself does not require noise covariance.

### 11.2 Fixed-degree normalized configuration formulas cannot cover all inputs

For every \(m\ge2\), take coordinates \(0,1,\ldots,m,b\) and
\[
v=(1,m,\ldots,m,m(m+1)),
\qquad
w=(m,1,\ldots,1,-1).
\]
They are orthogonal. Put
\[
P=\frac{vv^*}{\|v\|^2},
\qquad
K=\frac15I+\frac35\frac{ww^*}{\|w\|^2}.
\tag{20}
\]
The spectrum is contained in \(\{1/5,4/5\}\), \(P\) has full support, and \(KP=P/5\).

For every \(S\subseteq\{1,\ldots,m\}\), the normalized current in direction zero is affine in \(|S|\) and is strictly negative whenever \(S\ne\varnothing\). Hence every feasible flow is forced to satisfy
\[
f(S,0)=0\quad(S\ne\varnothing),
\]
while the singleton target fixes \(f(\varnothing,0)>0\). Consequently every feasible flow has normalized slice
\[
\boxed{
\frac{f(S,0)}
{(1/5)^{|S|}(4/5)^{m+1-|S|}}
=
\frac1{4V}
\prod_{j=1}^m(1-x_j).
}
\tag{21}
\]
The unique multilinear representation has degree exactly \(m\).

Thus no dimension-independent fixed-degree normalized configuration-polynomial repair scheme can cover all inputs. The forced mass decays with \(m\), so degree growth alone does not give an \(\ell^1\) instability lower bound.

## 12. Method-specific electrical failure

A natural unconstrained repair solves
\[
B\operatorname{diag}(J_+)B^*u=BJ_-
\]
and sets
\[
f_e^{\rm el}
=
J_{e,+}(1-(B^*u)_e).
\tag{22}
\]
It preserves endpoint marginals, but it need not be nonnegative.

An exact four-coordinate fixed-gap example has one positive-current edge with
\[
J_e=\frac{38209}{3906000}>0
\]
but
\[
f_e^{\rm el}
=
-\frac{
18653791342018742222313531313
}{
82753723846975391293278291516000
}<0.
\]
This kills formula (22), not all selectors.

## 13. Adversarial and computational checks

The companion REVIEW.md re-derives the vulnerable steps and explicitly attacks:

- degeneracy in the box-constrained active-set argument;
- the sign bookkeeping in the six-cycle proof;
- cross-support compatibility;
- the equality case of the signed-energy theorem;
- the noncommuting fermionic density derivative in the fixed-projector comparison;
- possible Fock-space dimension growth under projector rotation;
- the distinction between strict feasibility and a uniform quantitative interior radius;
- the distinction between \(\mathsf L_J\) and the entropy-center Hessian \(\mathsf L_c\);
- whether the noise and high-degree examples are genuinely selector independent for the limited extra principles they claim.

The exact standard-library checkers from the research pass were rerun in the current session.

The bounded-support checker returned
PASS_SCOPED_EXACT_CHECKS and included coordinate permutations, fixed-kernel projector variations, cross-support examples, and abstract six-cycle comparisons.

The continuation checker returned
PASS_EXACT_SCOPED_CHECKS and rechecked layered capacity cuts, strict interior flows on the test instances, signed-Laplacian positivity, bit-flip identities, the high-degree family, and the exact negative electrical witness while preserving endpoint marginals.

A separate floating diagnostic over complex-Hermitian examples found no violation of the proved energy bounds. It is diagnostic only, not proof.

## 14. Final status

The strongest established positive selector result here is the globally coherent support-at-most-three theorem (9), together with the general fixed-support estimate (5).

The strongest unrestricted structural result is the positive signed-energy representation (12) and its dimension-free stability, including changing projectors.

No single unrestricted-support selector has yet been shown to satisfy HSEL with a constant independent of dimension, and no selector-independent finite family of genuine admissible DPP inputs has been produced that forces every selector to violate every fixed constant.

**Therefore cat5779/rl01#122 remains OPEN.**
