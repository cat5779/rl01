STATUS: PASS

# Independent adversarial audit of R15/G11

I checked the frozen theorem in `prompt.md` against the complete proof in
`output.md`, using the already audited support-at-most-three argument only as a
comparison point.  The new proof correctly closes the quantifier "for every
fixed finite support bound (s)".  Its selector is a single global least-norm
choice, while the only new (s)-dependence is a finite active-set constant for
cube inequality matrices on at most (2s) coordinates.  I found no dependence
on the ambient dimension and no division by a DPP atom.

## 1. Nonempty fiber and the dilation/coupling argument

Equation (3) follows by testing the divergence against (|S|) and against the
indicator of the event (j\in S).  Hence divergence forces total edge mass

\[
\sum_{S,i\notin S}f(S,i)=\operatorname{tr}P=1
\]

and total mass in direction (j) equal to (P_{jj}).  Because feasible flows
are nonnegative, (P_{jj}=0) kills every edge in direction (j).  For a
rank-one projector this is precisely what is needed outside
(\operatorname{supp}P).

The nonemptiness construction is valid.  With (h=\varepsilon/2) and
(B=K+hP), the map

\[
Vx=(K^{1/2}x,\sqrt h,Px,(I-B)^{1/2}x)
\]

is an isometry because (V^*V=I).  The first-summand and first-two-summand
projections are nested and their ranks differ by one; after completing the
orthonormal family (Ve_i) to a basis, their projection-DPP restrictions to
the distinguished coordinates have kernels (K) and (B).  The standard
codimension-one monotone projection-DPP coupling therefore gives
(X\subseteq Y) and at most one new distinguished point after restriction.
Since every exact atom is affine on a rank-one kernel line,

\[
f(S,i)=h^{-1}\Pr(X=S,Y=S\cup\{i\})
\]

has divergence (b_{K,P}), outgoing mass at most
((2/\varepsilon)p_K(S)), and total mass
(h^{-1}\operatorname{tr}(B-K)=1).  Thus all fibers used in the proof are
nonempty.  Compactness follows from containment in the unit simplex, and the
strictly convex Euclidean objective has a unique minimizer.

The proof of probability stability

\[
\|p_A-p_B\|_1\le 2\|A-B\|_1
\]

is also sound: a nonnegative unit birth flow bounds the derivative in every
rank-one projector direction by (2); spectral decomposition gives the
trace-norm derivative bound in an arbitrary Hermitian direction; integration
works on interior segments, and the displayed regularization handles boundary
kernels.

## 2. Global fixed-normal least-norm Lipschitz lemma

The lemma (6) is correct with one constant for all feasible right-hand sides.
At the minimum (y), KKT optimality gives
(-y=\mathsf A_I^*\lambda), (\lambda\ge0), for active rows.  A conic
representation with minimal positive support uses linearly independent rows,
so

\[
y=\mathsf A_I^*(\mathsf A_I\mathsf A_I^*)^{-1}r_I=L_Ir_I,
\qquad
\|L_I\|_{2\to2}=\sigma_{\min}(\mathsf A_I)^{-1}.
\]

Conversely, (8) is exactly primal feasibility plus the sign condition on the
KKT multiplier.  It defines a convex polyhedral right-hand-side cell; the
zero-solution cell is (r\ge0).  These finitely many cells cover the feasible
right-hand-side domain and their formulas agree on overlaps by uniqueness.
The segment between two feasible right-hand sides stays feasible.  Partitioning
that segment at the finitely many cell endpoints and summing the bounds of the
linear formulas gives (6), because the subsegment lengths add to the length of
the original segment.  Thus the constant is global and is not merely a local
active-set estimate or an unsupported Hausdorff-selection assertion.

## 3. Integer Gram bound for every (m\le 2s)

The flow polytope is exactly the fixed-normal system (9).  Nonnegativity is
encoded by (-I), divergence equality by the two copies
(\mathsf D_m,-\mathsf D_m), and capacity by (\mathsf O_m); normalization is
already forced by divergence.  The number of columns is
(N_m=m2^{m-1}).  All entries are integral, and every row has squared norm at
most (m).

For any independent (k)-row submatrix, (k\le N_m\le N_*), and its Gram
matrix (G) is positive definite and integral.  Hence

\[
\det G\ge1,
\qquad
\operatorname{tr}G\le km\le N_*m_*.
\]

Every eigenvalue is at most the trace, so

\[
\lambda_{\min}(G)\ge(m_*N_*)^{-(k-1)},
\qquad
\sigma_{\min}(\mathsf A_{m,I})^{-1}
\le(m_*N_*)^{(N_*-1)/2}\le H_s.
\]

This proves the required uniform active-set bound over the finite family
(1\le m\le2s).  It depends only on (s), not on (K,P), atom masses, or
(|E|).  The deliberately looser exponent used in (H_s) is harmless.

The local right-hand-side estimate is conservative but valid.  Gap preservation
ensures that (M+\varepsilon R) and (N+\varepsilon Q) are positive
contractions, so rank-one affinity and probability stability imply (11).  The
two divergence blocks and the capacity block then give

\[
\|r(M,R)-r(N,Q)\|_2
\le (12/\varepsilon)\|M-N\|_1+4\|R-Q\|_1.
\]

Combining this with the least-norm lemma and
(\|x\|_1\le\sqrt{N_m}\|x\|_2) proves (12) with the stated
(\Lambda_s), uniformly for every (m\le2s).

## 4. Conditioning, gap preservation, and stability

The matrix (B_T(K)) is uniformly invertible.  Its decomposition into a
diagonal matrix with singular values (1/2) plus a perturbation of operator
norm at most (1/2-\varepsilon) gives
(\|B_T(K)^{-1}\|_{\mathrm{op}}\le\varepsilon^{-1}).  The block determinant
formula yields the exact atom factorization (15).  Because the determinant is
nonzero and is, up to its fixed sign, the probability (q_K(T)), every
(q_K(T)) is strictly positive.

Successive occupied/absent one-coordinate Schur complements preserve both
spectral gap inequalities, so (M_T(K)) remains
(\varepsilon)-gapped.  Differentiating the Schur complement is correctly
written as

\[
\frac d{dt}M_T(K_t)=W_t(L-K)W_t^*.
\]

The off-diagonal compression bound and the inverse bound give
(\|W_t\|_{\mathrm{op}}^2\le d_\varepsilon); trace-norm multiplication and
integration prove the pointwise estimate (17), and hence its probability
average (18).  The outside marginal estimate (19) follows from probability
stability and trace-norm contraction under compression.

If (J\supseteq\operatorname{supp}P), then (P) has no outside or cross
blocks.  Therefore the perturbation (K\mapsto K+hP) leaves (q_K(T)) and
the Schur-complement correction unchanged and adds exactly (hP_J) to the
conditional kernel.  Differentiating the exact factorization gives (20).  No
extra regularity or positive lower bound on (q_K(T)) is used.

## 5. Exact Cartesian-product compatibility

This is an exact decomposition of the whole original fiber, not a specially
chosen subfiber.  For every containing set (J), nonnegativity and (3) first
annihilate all outside directions.  The remaining edges split into blocks
indexed by (T\subseteq E\setminus J).  Equations (15) and (20) transform the
divergence and capacity constraints in block (T) into exactly those of

\[
q_K(T)\,\mathcal F_J(M_T(K),P_J).
\]

The block mass is forced to be (q_K(T)) by the local cardinality identity,
and conversely arbitrary choices in all these scaled local fibers assemble to
a global feasible flow.  Hence (22) is an equality of feasible sets.

The global squared norm is the sum of the block objectives
(q_K(T)^2\|g_T\|_2^2/2).  Since every weight is positive, each block has the
same unique least-norm minimizer as its unscaled local fiber.  This proves (21)
for every (J\supseteq\operatorname{supp}P), including nonminimal (J) and
support-degeneration interfaces.  The selector is consequently one global
choice; no pair-dependent choice is introduced.

## 6. Union support and the final constant

For two admissible directions, the proof sets

\[
J=\operatorname{supp}P\cup\operatorname{supp}Q,
\qquad |J|\le2s,
\]

only after both global selectors have been defined.  Applying the exact product
identity to both inputs in the common blocks gives (24).  The first term is the
outside-marginal distance, while the second is a (q_K)-probability average;
the number of outside patterns never enters.

Using (12), (18), and (19) gives exactly

\[
\|F_{K,P}-F_{L,Q}\|_1
\le
\left(2+\frac{12\Lambda_s d_\varepsilon}{\varepsilon}\right)
\|K-L\|_1
+4\Lambda_s\|P-Q\|_1.
\]

Compression does not change (\|P-Q\|_1), because both projectors are
supported in (J).  Since (d_\varepsilon\ge1) and
(\varepsilon<1/2), the constant in (2) also dominates
(4\Lambda_s).  It therefore proves the requested simultaneous ((K,P))
estimate with no ambient-dimension dependence.

## 7. Measurability, covariance, and exact scope

The global estimate gives continuity, hence Borel dependence, on the full
support-at-most-(s) domain, including limits where support drops.  A coordinate
permutation maps the full fiber bijectively to the relabeled fiber and preserves
the Euclidean objective; uniqueness therefore gives permutation covariance.
Membership in the selected fiber supplies positivity, exact divergence, unit
mass, and the required outgoing capacity.

The citation marker attached to the standard nested-projection coupling is a
presentation artifact and should be replaced in a publication version, but
the coupling is invoked with the correct finite-dimensional nested,
codimension-one hypotheses and the dilation establishes those hypotheses
explicitly.

The proved range is exactly: every fixed finite (s), with a constant allowed
to depend on ((\varepsilon,s)), uniformly in finite (E).  The argument does
not give a constant uniform in (s), does not cover arbitrary unbounded
support, and makes no novelty claim.  Within the frozen theorem's range, the
verdict is **PASS**.

