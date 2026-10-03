INCOMPLETE

No universal-selector obstruction and no proof of the full dimension-free selector theorem has been obtained. The strongest exact continuation is:

1. an affine description of the **entire** flow polytope as a one-point monotone coupling polytope;
2. quantitative fixed-gap regularity of every DPP atom;
3. linear collapse of every flow fiber near a coordinate direction;
4. exact reduction to the coordinate support of the rank-one direction; and
5. a dimension-free Hausdorff estimate whenever the union of the two coordinate supports has bounded size.

Consequently, a pairwise obstruction of the requested kind, if it exists, must involve genuinely delocalized directions with coordinate support tending to infinity. The results below do not settle that remaining case.

## 1. Exact coupling representation of the entire flow polytope

Fix
\[
h=\frac{\varepsilon}{2}.
\]
Since \(K\le(1-\varepsilon)I\) and \(P\le I\),
\[
\varepsilon I\le K+hP\le\left(1-\frac{\varepsilon}{2}\right)I.
\]

Let \(Z=\operatorname{diag}(z_1,\ldots,z_n)\). The DPP generating polynomial is
\[
G_{K+tP}(z)
 =\det\!\left(I-K+KZ+tP(Z-I)\right).
\]
The perturbation \(P(Z-I)\) has rank at most one, so the determinant is affine in \(t\). Coefficientwise,
\[
p_{K+tP}=p_K+t\,b_{K,P}                                      \tag{1.1}
\]
for every \(t\) for which \(K+tP\) is an admissible kernel.

Given \(F\in\mathcal F(K,P)\), define a measure on pairs \((X,Y)\) by
\[
\Pi_F(S,S\cup\{i\})=hF(S,i),                                 \tag{1.2}
\]
and
\[
\Pi_F(S,S)
 =p_K(S)-h\sum_{i\notin S}F(S,i).                            \tag{1.3}
\]
The pointwise capacity constraint gives
\[
hF_{\rm out}(S)
 \le\frac{\varepsilon}{2}\frac{2}{\varepsilon}p_K(S)
 =p_K(S),
\]
so the diagonal masses in (1.3) are nonnegative.

The first marginal is \(p_K\). The second marginal at \(S\) is
\[
\begin{aligned}
\Pi_F(\,\cdot\,,S)
 &=p_K(S)-hF_{\rm out}(S)+hF_{\rm in}(S)\\
 &=p_K(S)+h\,b_{K,P}(S)
 =p_{K+hP}(S),                                                \tag{1.4}
\end{aligned}
\]
using (1.1).

Conversely, suppose \(\Pi\) is a coupling of \(p_K\) and \(p_{K+hP}\) supported on
\[
(S,S)\quad\text{and}\quad(S,S\cup\{i\}).
\]
Set
\[
F(S,i)=h^{-1}\Pi(S,S\cup\{i\}).                              \tag{1.5}
\]
The first marginal identity gives
\[
hF_{\rm out}(S)\le p_K(S),
\]
which is exactly the required capacity constraint. The second-minus-first marginal identity gives
\[
\operatorname{div}F=b_{K,P}.
\]

Moreover, every off-diagonal pair adds exactly one point. Hence its total off-diagonal mass is
\[
\begin{aligned}
\Pi\{X\ne Y\}
 &=\mathbb E_{K+hP}|Y|-\mathbb E_K|X|\\
 &=\operatorname{tr}(K+hP)-\operatorname{tr}K
 =h.
\end{aligned}
\]
Thus the flow in (1.5) has total mass one.

Therefore
\[
\boxed{
\mathcal F(K,P)
\ \longleftrightarrow\
\left\{
\begin{array}{c}
\text{couplings of }p_K\text{ and }p_{K+hP}\\
\text{supported on equality and one-point upward covers}
\end{array}
\right\}}
                                                                    \tag{1.6}
\]
is an affine bijection for \(h=\varepsilon/2\). This represents the entire polytope, not merely a distinguished subpolytope.

## 2. Fixed-gap atom regularity

For \(S\subseteq E\), let
\[
D_S=I_{S^c}.
\]
The exact DPP atom formula is
\[
p_K(S)=(-1)^{|S^c|}\det(K-D_S).                              \tag{2.1}
\]
Put \(J_S=I-2D_S\). Since \(J_S\) is unitary and self-adjoint,
\[
K-D_S
 =\frac12J_S\bigl(I+J_S(2K-I)\bigr).                         \tag{2.2}
\]
The spectral gap gives
\[
\|2K-I\|\le1-2\varepsilon.
\]
It follows from the Neumann bound in (2.2) that
\[
\boxed{\|(K-D_S)^{-1}\|\le\frac1{\varepsilon}.}              \tag{2.3}
\]

Differentiating (2.1),
\[
b_{K,P}(S)
 =p_K(S)\operatorname{tr}\!\left((K-D_S)^{-1}P\right).       \tag{2.4}
\]
For \(P=vv^*\),
\[
\left|\frac{b_{K,P}(S)}{p_K(S)}\right|
 =\left|v^*(K-D_S)^{-1}v\right|
 \le\frac1{\varepsilon}.                                    \tag{2.5}
\]
Combining (1.1) and (2.5), at \(h=\varepsilon/2\),
\[
\boxed{
\frac12
\le\frac{p_{K+hP}(S)}{p_K(S)}
\le\frac32.}                                                  \tag{2.6}
\]

There is also pointwise multiplicative stability in \(K\). Let
\[
K_t=(1-t)K+tL.
\]
Then
\[
\frac{d}{dt}\log p_{K_t}(S)
 =\operatorname{tr}\!\left((K_t-D_S)^{-1}(L-K)\right).
\]
By (2.3),
\[
\left|\frac{d}{dt}\log p_{K_t}(S)\right|
 \le\frac{\|K-L\|_1}{\varepsilon}.
\]
Integrating,
\[
\boxed{
e^{-\|K-L\|_1/\varepsilon}p_K(S)
\le p_L(S)
\le e^{\|K-L\|_1/\varepsilon}p_K(S).}                         \tag{2.7}
\]

The score itself satisfies a pointwise Lipschitz estimate. The resolvent identity gives
\[
(K-D_S)^{-1}-(L-D_S)^{-1}
 =(K-D_S)^{-1}(L-K)(L-D_S)^{-1}.
\]
Therefore
\[
\boxed{
\begin{aligned}
\Big|
&\operatorname{tr}\!\left((K-D_S)^{-1}P\right)
-\operatorname{tr}\!\left((L-D_S)^{-1}Q\right)
\Big|\\
&\qquad\le
\frac{\|P-Q\|_1}{\varepsilon}
+\frac{\|K-L\|_1}{\varepsilon^2}.
\end{aligned}}                                                \tag{2.8}
\]

Finally, adjacent atoms are uniformly comparable. Write
\[
L_K=K(I-K)^{-1}.
\]
Then
\[
p_K(S)=\det(I-K)\det((L_K)_S),
\]
and
\[
\frac{\varepsilon}{1-\varepsilon}I
\le L_K
\le\frac{1-\varepsilon}{\varepsilon}I.
\]
For \(i\notin S\), the ratio \(p_K(S\cup\{i\})/p_K(S)\) is the corresponding Schur complement of \(L_K\). Hence
\[
\boxed{
\frac{\varepsilon}{1-\varepsilon}
\le\frac{p_K(S\cup\{i\})}{p_K(S)}
\le\frac{1-\varepsilon}{\varepsilon}.}                        \tag{2.9}
\]

Thus a fixed-gap DPP cannot resemble a zero-supported alternating path: all atoms are positive, adjacent atoms are uniformly comparable, and every atom changes proportionally to its own mass under a small parameter perturbation.

## 3. Coordinate edge masses are fixed

For every feasible flow and every coordinate \(i\),
\[
\boxed{
\sum_{S:i\notin S}F(S,i)=P_{ii}.}                            \tag{3.1}
\]

To prove this, test the divergence identity against
\[
\phi_i(S)=\mathbf 1_{\{i\in S\}}.
\]
Summation by parts gives
\[
\sum_S\phi_i(S)b_{K,P}(S)
 =\sum_{S,j\notin S}F(S,j)
   \bigl(\phi_i(S\cup\{j\})-\phi_i(S)\bigr)
 =\sum_{S:i\notin S}F(S,i).
\]
On the other hand,
\[
\sum_S\phi_i(S)p_K(S)=K_{ii},
\]
so differentiating in the direction \(P\) gives \(P_{ii}\).

Summing (3.1) over \(i\) also proves directly that
\[
\sum_{S,i\notin S}F(S,i)=\operatorname{tr}P=1.
\]
Thus global normalization is already forced by the divergence equation.

## 4. Coordinate directions have singleton fibers

Let
\[
E_j=e_je_j^*.
\]
Equation (3.1) says that every feasible flow for \((K,E_j)\) has total mass one on \(j\)-edges and zero mass on every other coordinate. Since a \(j\)-edge connects the pair
\[
A,\quad A\cup\{j\},
\qquad A\subseteq E\setminus\{j\},
\]
the divergence determines its mass uniquely. Denote this unique flow by \(U_{K,j}\).

It has the explicit formula
\[
\boxed{
U_{K,j}(A,j)=p_{K_{E\setminus\{j\}}}(A).}                    \tag{4.1}
\]
Indeed, differentiating the exact atom probabilities with respect to \(K_{jj}\) shows that the mass on the pair \(A,A\cup\{j\}\) is the marginal probability that the configuration outside \(j\) equals \(A\).

The audited capacity-vector estimate implies
\[
\|p_A-p_B\|_1\le2\|A-B\|_1
\]
for admissible DPP kernels. Applying this to the principal submatrices gives
\[
\boxed{
\|U_{K,j}-U_{L,j}\|_1
\le2\|K-L\|_1.}                                             \tag{4.2}
\]

## 5. Every fiber collapses linearly near a coordinate direction

Let \(Q=vv^*\), and put
\[
d=\|Q-E_j\|_1,\qquad
\eta=1-Q_{jj}=1-|v_j|^2.
\]
For rank-one projectors, the two nonzero eigenvalues of \(Q-E_j\) are
\[
\pm\sqrt{1-|v_j|^2},
\]
so
\[
d=2\sqrt{\eta}.                                               \tag{5.1}
\]

Take an arbitrary
\[
F\in\mathcal F(K,Q).
\]
Split it according to the coordinate added:
\[
F=F^{(j)}+F^{(\ne j)}.
\]
By (3.1),
\[
\|F^{(\ne j)}\|_1
 =\sum_{i\ne j}Q_{ii}
 =\eta.                                                       \tag{5.2}
\]

Set
\[
H_j=F^{(j)}-U_{K,j}.
\]
Different \(j\)-edges have disjoint pairs of endpoints. Consequently,
\[
\|\operatorname{div}H_j\|_1=2\|H_j\|_1.                     \tag{5.3}
\]
Furthermore,
\[
\operatorname{div}H_j
 =b_{K,Q}-b_{K,E_j}-\operatorname{div}F^{(\ne j)}.
\]
Since the divergence operator has \(\ell^1\)-norm at most two,
\[
\begin{aligned}
\|F-U_{K,j}\|_1
 &=\|H_j\|_1+\|F^{(\ne j)}\|_1\\
 &\le\frac12\|b_{K,Q}-b_{K,E_j}\|_1+2\eta.                   \tag{5.4}
\end{aligned}
\]

The audited signed-repair estimate, with the kernel fixed, supplies a signed edge field \(R\) satisfying
\[
\operatorname{div}R=b_{K,Q}-b_{K,E_j},
\qquad
\|R\|_1\le d.
\]
Therefore
\[
\|b_{K,Q}-b_{K,E_j}\|_1\le2d.
\]
Using \(\eta=d^2/4\) in (5.4),
\[
\boxed{
\sup_{F\in\mathcal F(K,Q)}
\|F-U_{K,j}\|_1
\le d+\frac12d^2
\le2d.}                                                       \tag{5.5}
\]

This controls the entire fiber, not only a specially chosen flow.

Combining (5.5) with (4.2), for arbitrary \(K,L,Q\),
\[
\boxed{
\sup_{F\in\mathcal F(L,Q)}
\operatorname{dist}_1\!\left(F,\mathcal F(K,E_j)\right)
\le
2\bigl(\|K-L\|_1+\|Q-E_j\|_1\bigr).}                         \tag{5.6}
\]
Since \(\mathcal F(K,E_j)\) is a singleton, every preferred pairwise obstruction having one endpoint direction equal to a coordinate projector has ratio at most two.

## 6. Exact reduction to the support of the direction

Let \(P=vv^*\), let
\[
J=\operatorname{supp}v,
\qquad R=E\setminus J.
\]
By (3.1), every feasible flow uses only edges whose added coordinate lies in \(J\). Thus the flow splits into independent blocks indexed by the outside configuration \(T\subseteq R\).

This has an exact DPP interpretation. Put
\[
B_T=K_{RR}-I_{R\setminus T},
\qquad
K^T=K_{JJ}-K_{JR}B_T^{-1}K_{RJ}.                            \tag{6.1}
\]
For \(A\subseteq J\), block determinant factorization in the atom formula gives
\[
\boxed{
p_K(T\cup A)
 =p_{K_{RR}}(T)\,p_{K^T}(A).}                               \tag{6.2}
\]
Because a perturbation supported on \(J\) changes only the \(JJ\)-block,
\[
\boxed{
b_{K,P}(T\cup A)
 =p_{K_{RR}}(T)\,b_{K^T,P_J}(A).}                           \tag{6.3}
\]

The conditional kernel \(K^T\) retains the same spectral gap:
\[
\boxed{
\varepsilon I\le K^T\le(1-\varepsilon)I.}                   \tag{6.4}
\]

For completeness, condition on one coordinate and write
\[
K=
\begin{pmatrix}
a&x^*\\
x&C
\end{pmatrix}.
\]
Conditioning on inclusion gives
\[
K^{(1)}=C-\frac{xx^*}{a}.
\]
The lower bound follows from the Schur complement of \(K-\varepsilon I\), and the upper bound follows from \(K^{(1)}\le C\le(1-\varepsilon)I\).

Conditioning on exclusion gives
\[
K^{(0)}=C+\frac{xx^*}{1-a}.
\]
The lower bound follows from \(K^{(0)}\ge C\ge\varepsilon I\). Applying the preceding inclusion argument to \(I-K\) gives
\[
I-K^{(0)}\ge\varepsilon I,
\]
which is the upper bound. Iteration proves (6.4) for arbitrary \(T\).

Hence adding arbitrarily many inactive coordinates merely forms a mixture of lower-dimensional flow problems. It cannot by itself produce a dimension-dependent obstruction.

## 7. Hausdorff stability for bounded coordinate support

Let \(D_m\) be the divergence matrix and \(R_m\) the outgoing-sum matrix of the directed \(m\)-cube. For right-hand sides \(\beta,c\), define
\[
\mathcal P_m(\beta,c)
 =
 \{x:D_mx=\beta,\ x\ge0,\ R_mx\le c\}.
\]

Because the constraint matrix is fixed when \(m\) is fixed, the polyhedral Hoffman error bound gives a finite constant \(H_m\) such that, whenever \(\mathcal P_m(\beta,c)\) is nonempty,
\[
\boxed{
\begin{aligned}
\operatorname{dist}_1(x,\mathcal P_m(\beta,c))
\le H_m\bigl(&\|D_mx-\beta\|_1+\|x_-\|_1\\
             &+\|(R_mx-c)_+\|_1\bigr).
\end{aligned}}                                               \tag{7.1}
\]
One may obtain \(H_m\) by taking the maximum of the inverse norms associated with the finitely many linearly independent active-constraint submatrices. Thus it depends only on \(m\), not on the right-hand sides.

For a direct sum of any number of \(m\)-cube blocks, apply (7.1) to each block and add the estimates; the same \(H_m\) works.

Now assume the coordinate supports of two rank-one projectors \(P,Q\) are contained in a common set \(J\) with
\[
|J|=m.
\]
Every flow for either parameter pair uses only \(J\)-edges and decomposes into the outside blocks of Section 6.

Write
\[
\Delta_K=\|K-L\|_1,\qquad
\Delta_P=\|P-Q\|_1.
\]
The audited signed-repair estimate gives a signed flow \(R\) such that
\[
\operatorname{div}R=b_{K,P}-b_{L,Q},
\qquad
\|R\|_1\le\frac4{\varepsilon}\Delta_K+\Delta_P.
\]
Since every edge contributes to two divergence coordinates,
\[
\boxed{
\|b_{K,P}-b_{L,Q}\|_1
\le\frac8{\varepsilon}\Delta_K+2\Delta_P.}                   \tag{7.2}
\]

Let
\[
c_K=\frac2{\varepsilon}p_K,\qquad
c_L=\frac2{\varepsilon}p_L.
\]
The audited capacity-vector estimate gives
\[
\boxed{
\|c_K-c_L\|_1
\le\frac4{\varepsilon}\Delta_K.}                             \tag{7.3}
\]

Take any \(F\in\mathcal F(K,P)\) and apply (7.1), block by block, to the target polytopes associated with \((L,Q)\). The source is already nonnegative. Its equality residual is bounded by (7.2). Since \(R_mF\le c_K\),
\[
\|(R_mF-c_L)_+\|_1
\le\|(c_K-c_L)_+\|_1
\le\|c_K-c_L\|_1.
\]
Summing the block estimates yields a target flow \(G\in\mathcal F(L,Q)\) with
\[
\|F-G\|_1
\le H_m\left(
\frac{12}{\varepsilon}\Delta_K+2\Delta_P
\right).
\]
Repeating the argument in the opposite direction proves
\[
\boxed{
d_H^{(1)}
 \bigl(\mathcal F(K,P),\mathcal F(L,Q)\bigr)
\le
H_m\left(
\frac{12}{\varepsilon}\|K-L\|_1
+2\|P-Q\|_1
\right).}                                                    \tag{7.4}
\]

This bound is independent of the ambient dimension \(n\). In particular, if both projectors have support size at most \(s\), their union has size at most \(2s\), and (7.4) applies with \(H_{2s}\).

Therefore an obstruction based on the distance of the entire fibers cannot have uniformly bounded coordinate support.

## 8. Quantitative attraction to a fixed finite support

The preceding exact-support result has a useful approximate version.

Let \(Q=vv^*\), choose \(J\subseteq E\), and write
\[
\eta=\|v_{J^c}\|^2<1,
\qquad
Q_J=\frac{v_Jv_J^*}{\|v_J\|^2}.
\]
The trace distance between the two pure states is
\[
\delta=\|Q-Q_J\|_1=2\sqrt{\eta}.                             \tag{8.1}
\]

For any \(F\in\mathcal F(K,Q)\), (3.1) shows that the total mass of edges whose added coordinate lies outside \(J\) is exactly
\[
\eta.
\]
Delete these edges, obtaining \(F_J\). The deletion changes the divergence by at most \(2\eta\) in \(\ell^1\). The audited repair estimate at fixed \(K\) gives
\[
\|b_{K,Q}-b_{K,Q_J}\|_1\le2\delta.
\]
The remaining flow \(F_J\) is nonnegative and continues to satisfy the same pointwise capacities. Applying the blockwise \(m\)-dimensional Hoffman estimate, where \(m=|J|\), gives
\[
\boxed{
\operatorname{dist}_1
 \bigl(F,\mathcal F(K,Q_J)\bigr)
\le
\eta+H_m(2\delta+2\eta).}                                   \tag{8.2}
\]

Thus flows for directions carrying nearly all their vector mass on a fixed \(m\)-coordinate set lie uniformly near an \(m\)-dimensional fiber.

## 9. The abstract coupling graph still has unbounded conditioning

The preceding results use DPP structure essentially. Without it, the diagonal-plus-cover coupling graph has unbounded condition number.

Let
\[
S_j=\{1,\ldots,j\},\qquad0\le j\le m.
\]
Use row vertices
\[
R_{S_0},\ldots,R_{S_m},
\]
column vertices
\[
C_{S_1},\ldots,C_{S_m},
\]
and the \(2m\) allowed edges
\[
u_j=(R_{S_{j-1}},C_{S_j}),
\qquad
d_j=(R_{S_j},C_{S_j}),
\qquad1\le j\le m.
\]
These form a path alternating between cover and diagonal edges.

Set
\[
a=\frac1{2m}
\]
and put mass \(a\) on every edge. For \(0<\delta<a\), define another coupling by
\[
u_j\longmapsto a+\delta,\qquad
d_j\longmapsto a-\delta.                                    \tag{9.1}
\]
Every column marginal is unchanged because the changes at \(u_j,d_j\) cancel. Every interior row marginal is unchanged because the changes at \(d_j,u_{j+1}\) cancel. Only the endpoints change:
\[
\mu'(S_0)-\mu(S_0)=\delta,\qquad
\mu'(S_m)-\mu(S_m)=-\delta.
\]
Hence the marginal pairs differ by
\[
2\delta
\]
in \(\ell^1\), whereas the two couplings differ by
\[
2m\delta.                                                    \tag{9.2}
\]
All other row and column marginals are zero, so every edge outside this path is forced to have zero mass. The path is a tree, and its edge masses are uniquely determined by its marginals. Thus both coupling fibers are singletons and the ratio is exactly \(m\).

This is not a counterexample to the frozen theorem. Its marginals contain zero atoms, violate the adjacent-atom estimates (2.9), and suppress the additional routes present in the full DPP flow polytopes. It proves only that abstract coupling geometry and marginal \(\ell^1\)-stability are insufficient.

## 10. Selection-theoretic consequences

Suppose a family \(z_n,z_n'\) satisfied
\[
\frac{
\inf\{\|F-G\|_1:
F\in\mathcal F(z_n),\,
G\in\mathcal F(z_n')\}}
{d_n}
\longrightarrow\infty.
\]
For any selector \(\Phi\),
\[
\inf\{\|F-G\|_1:\cdots\}
\le
\|\Phi(z_n)-\Phi(z_n')\|_1.
\]
A dimension-free \(C_\varepsilon\)-Lipschitz selector would therefore imply
\[
\inf\{\|F-G\|_1:\cdots\}
\le C_\varepsilon d_n,
\]
contradicting the displayed divergence. Thus the requested pairwise family would disprove the theorem for every selector.

Likewise, suppose a finite graph of parameter points has the property that every simultaneous choice
\[
F_z\in\mathcal F(z)
\]
violates a proposed \(C\)-Lipschitz bound on at least one graph edge. The values of any \(C\)-Lipschitz selector would constitute a simultaneous choice satisfying every edge bound, a contradiction. Hence a genuine branching or cycle certificate also suffices.

For each fixed \(n\), however, a finite constant exists. Taking \(m=n\) in (7.4) gives a dimension-dependent Hausdorff-Lipschitz bound for the fibers. Applying a finite-dimensional convex-body selector such as the Steiner point, together with equivalence of the ambient \(\ell^1\) and Euclidean norms, gives a finite Lipschitz constant depending on \(n\). Coordinate permutations act by orthogonal permutations of the edge coordinates, so the Steiner selector is permutation-equivariant. It is Lipschitz and therefore Borel.

Thus the unresolved issue is precisely uniformity as \(n\to\infty\).

## 11. Exact remaining gap

A complete resolution requires one of the following.

To obtain **DISPROVED**, one must construct fixed-gap kernels and genuinely delocalized rank-one directions for which either

\[
\frac{
\inf\{\|F-G\|_1:
F\in\mathcal F(K_n,P_n),\,
G\in\mathcal F(L_n,Q_n)\}}
{\|K_n-L_n\|_1+\|P_n-Q_n\|_1}
\longrightarrow\infty,
\]
with the infimum taken over the entire fibers, or a finite branching/cycle configuration trapping every simultaneous selection.

To obtain **PROVED**, one must replace the dimension-dependent constants \(H_m\) by a uniform estimate on the full, delocalized DPP parameter manifold and then construct a globally compatible equivariant selector.

The results above rule out, as standalone universal obstructions:

- a coordinate projector at either endpoint;
- exact coordinate supports of uniformly bounded size;
- padding by inactive coordinates;
- directions uniformly concentrated on a fixed finite coordinate set;
- zero-atom or thin-path coupling reductions;
- global normalization;
- pointwise capacity saturation by itself; and
- disproportionate movement of rare DPP atoms.

They do not control full-support delocalized directions uniformly in \(n\), and they do not furnish a globally compatible dimension-free selection. That is the minimal unresolved gap.
