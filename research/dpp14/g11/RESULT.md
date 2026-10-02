PROVED

Set
\[
d_\varepsilon
=1+\left(\frac{1-2\varepsilon}{2\varepsilon}\right)^2,
\qquad
H=1152^{96},
\qquad
\Lambda=\sqrt{192}\,H.
\]
The following explicit, nonoptimal constant works:
\[
\boxed{C_\varepsilon^{(3)}
=2+\frac{12\Lambda d_\varepsilon}{\varepsilon}.}
\tag{1}
\]

The selector is the unique least-Euclidean-norm point of the **entire original flow fiber**:
\[
\boxed{
F_{K,P}
=\underset{f\in\mathcal F_E(K,P)}{\operatorname{argmin}}
\frac12\sum_{S,i\notin S}f(S,i)^2.
}
\tag{2}
\]
Its exact factorization over inactive coordinates will make this one choice compatible across all support strata. The finite-dimensional estimate will be applied on the union of two supports, which has at most six coordinates.

## 1. DPP and flux preliminaries

Matrix norms with subscript \(1\) are unnormalized trace norms; vector and edge norms with that subscript are sums of absolute values. Let \(D_A\) denote the diagonal projection onto \(A\). Inclusion-exclusion gives
\[
p_K(S)
=\sum_{A\subseteq E\setminus S}(-1)^{|A|}\det K_{S\cup A}
=(-1)^{|E\setminus S|}\det(K-D_{E\setminus S}).
\tag{3}
\]
Thus probabilities are polynomial in the kernel and affine along rank-one lines. Their derivative is linear in the direction.

### Nonemptiness

We include the nonemptiness argument to specify precisely the fibers being selected. Nested projection subspaces differing by one dimension admit a monotone projection-DPP coupling whose configurations differ by exactly one point, by Lyons’s projection-coupling theorem.

Put \(h=\varepsilon/2\), \(B=K+hP\), and consider the isometry
\[
Vx=\bigl(K^{1/2}x,\sqrt h\,Px,(I-B)^{1/2}x\bigr)
\]
into
\[
\mathbb C^E\oplus\operatorname{ran}P\oplus\mathbb C^E.
\]
The first summand and the first two summands are nested subspaces of dimension difference one. Their projections compressed by \(V\) are \(K\) and \(B\).

Complete the vectors \(Ve_i\) to an orthonormal coordinate basis and restrict the coupled projection DPPs to these original coordinates. Their restricted kernels are \(K,B\), giving a coupling \(X\subseteq Y\) with \(|Y\setminus X|\le1\). Therefore
\[
f(S,i)=h^{-1}\mathbb P(X=S,\ Y=S\cup\{i\})
\]
is nonnegative, has divergence
\[
(p_B-p_K)/h=b_{K,P},
\]
and has outgoing mass at most \(p_K(S)/h=(2/\varepsilon)p_K(S)\). Its total mass is
\[
h^{-1}\mathbb E(|Y|-|X|)
=h^{-1}\operatorname{tr}(B-K)=1.
\]
Consequently every fiber used below is nonempty.

### Mass and inactive directions

For any signed edge flow with divergence \(b_{K,P}\), summing the divergence against \(|S|\) and against \(\mathbf1_{\{j\in S\}}\) gives
\[
\boxed{
\sum_{S,i\notin S}f(S,i)=1,
\qquad
\sum_{S:j\notin S}f(S,j)=P_{jj}.
}
\tag{4}
\]
The right sides are the derivatives of
\(\mathbb E_K|X|=\operatorname{tr}K\) and
\(\mathbb P_K(j\in X)=K_{jj}\).

Thus normalization is redundant once divergence is imposed. If \(f\ge0\) and \(P_{jj}=0\), every edge in direction \(j\) vanishes. Nonnegative fibers lie in a unit simplex and are compact, so (2) exists and is unique.

### Probability stability

We will use
\[
\boxed{\|p_A-p_B\|_1\le2\|A-B\|_1}
\tag{5}
\]
for arbitrary positive contractions. Here is a derivation from the preceding nonemptiness argument.

For every interior kernel \(K\) and rank-one projector \(R\), a nonnegative unit flow with divergence \(b_{K,R}\) gives
\[
\|b_{K,R}\|_1\le2.
\]
For interior \(A,B\), write
\[
B-A=\sum_j\lambda_jR_j
\]
spectrally. Integrating derivatives on the gapped segment from \(A\) to \(B\), and using linearity in the direction, gives
\[
\|p_A-p_B\|_1\le2\sum_j|\lambda_j|
=2\|A-B\|_1.
\]
For boundary kernels, apply this to
\((1-2t)A+tI,(1-2t)B+tI\), and let \(t\downarrow0\) using (3). This proves (5).

## 2. Conditioning and uniform conditional-kernel stability

Let \(J\subseteq E\) contain \(\operatorname{supp}P\), put \(O=E\setminus J\), and fix \(T\subseteq O\). Define
\[
\begin{aligned}
B_T(K)&=K_O-D_{O\setminus T},\\
M_T(K)&=K_J-K_{JO}B_T(K)^{-1}K_{OJ},\\
q_K(T)&=p_{K_O}(T).
\end{aligned}
\tag{6}
\]
For empty \(O\), set \(M_T(K)=K\) and \(q_K(\varnothing)=1\).

The inverse is well-defined: writing
\[
B_T(K)
=(K_O-\tfrac12I)+(\tfrac12I-D_{O\setminus T})
\]
and using the reverse triangle inequality gives
\[
\|B_T(K)^{-1}\|_{\mathrm{op}}\le\varepsilon^{-1}.
\]
Equation (3) then also gives \(q_K(T)>0\), without requiring a quantitative lower bound for this probability.

The conditioning identities are
\[
\begin{aligned}
p_K(T\cup A)&=q_K(T)p_{M_T(K)}(A),\\
\varepsilon I_J&\preceq M_T(K)\preceq(1-\varepsilon)I_J.
\end{aligned}
\tag{7}
\]
The factorization follows from the block determinant formula in (3). For completeness, gap preservation can be checked one coordinate at a time. For
\[
H=\begin{pmatrix}a&c^*\\c&D\end{pmatrix},
\]
the occupied and absent conditional kernels are respectively
\[
D-\frac{cc^*}{a},
\qquad
D+\frac{cc^*}{1-a}.
\]
The first has upper bound \((1-\varepsilon)I\), and
\[
x^*(D-cc^*/a)x
=\min_{z\in\mathbb C}(z,x)^*H(z,x)
\ge\varepsilon\|x\|^2.
\]
The second is at least \(D\succeq\varepsilon I\); applying the preceding lower-bound argument to \(I-H\) gives its upper bound. Iterating these pinning steps, associativity of Schur complements gives exactly (6), proving (7).

In fact, conditional stability holds for every pattern:
\[
\boxed{
\|M_T(K)-M_T(L)\|_1
\le d_\varepsilon\|K-L\|_1.
}
\tag{8}
\]
Set \(K_s=K+s(L-K)\) and
\[
W_s=[\,I_J,\,-K_{s,JO}B_T(K_s)^{-1}\,].
\]
Differentiating (6) gives
\[
\frac d{ds}M_T(K_s)=W_s(L-K)W_s^*.
\]
Since
\[
\|K_{s,JO}\|_{\mathrm{op}}
\le\|K_s-\tfrac12I\|_{\mathrm{op}}
\le\tfrac12-\varepsilon,
\]
we have
\[
\|W_s\|_{\mathrm{op}}^2
\le1+\left(\frac{1/2-\varepsilon}{\varepsilon}\right)^2
=d_\varepsilon.
\]
Trace-norm multiplication and integration prove (8). Its average against any probability vector has the same bound. Also, (5) and trace-norm compression imply
\[
\|q_K-q_L\|_1\le2\|K-L\|_1.
\tag{9}
\]

Because \(P\) has zero rows and columns outside \(J\), its perturbation changes neither the outside marginal nor the cross blocks in (6). Hence
\[
\boxed{
\begin{aligned}
M_T(K+hP)&=M_T(K)+hP_J,\\
b_{K,P}(T\cup A)
&=q_K(T)b_{M_T(K),P_J}(A).
\end{aligned}}
\tag{10}
\]

## 3. A fixed-inequality least-norm selection lemma

Let \(\mathsf A\) be a fixed real matrix with \(d\) columns. For every right-hand side \(r\) for which
\[
Q(r)=\{x:\mathsf A x\le r\}\ne\varnothing,
\]
let \(s(r)\) be its unique least-Euclidean-norm point. Define
\[
H_{\mathsf A}
=\max_I\sigma_{\min}(\mathsf A_I)^{-1},
\tag{11}
\]
where \(I\) ranges over nonempty linearly independent subsets of rows. Then
\[
\boxed{
\|s(r)-s(r')\|_2
\le H_{\mathsf A}\|r-r'\|_2.
}
\tag{12}
\]
If there are no nonzero rows, the selector is zero and the assertion is immediate.

Here is a proof that includes degenerate active sets. At \(y=s(r)\), first-order optimality expresses \(-y\) as a nonnegative combination of active row normals. Indeed, every \(z\) satisfying
\(\mathsf A_i z\le0\) for active rows is a feasible direction for sufficiently small positive steps, so
\(\langle-y,z\rangle\le0\). The polar of this finite inequality cone is the cone of its row normals.

Choose a representation with a minimal number of positive coefficients. Its rows are linearly independent: otherwise a dependence could be subtracted, with a suitable sign and maximal allowed coefficient, to remove one positive coefficient while preserving nonnegativity. Thus, unless \(y=0\),
\[
-y=\mathsf A_I^*\lambda,\qquad
\lambda\ge0,\qquad
\mathsf A_Iy=r_I.
\]
Consequently,
\[
y=L_Ir_I,\qquad
L_I=\mathsf A_I^*(\mathsf A_I\mathsf A_I^*)^{-1},
\qquad
\|L_I\|_{\mathrm{op}}
=\sigma_{\min}(\mathsf A_I)^{-1}.
\tag{13}
\]

Conversely, this formula is the unique minimizer whenever
\[
\mathsf A L_Ir_I\le r,
\qquad
-(\mathsf A_I\mathsf A_I^*)^{-1}r_I\ge0.
\tag{14}
\]
For a feasible \(z\), the resulting multiplier satisfies
\[
\langle y,z-y\rangle
=-\lambda^*\mathsf A_I(z-y)\ge0,
\]
which proves sufficiency.

Conditions (14) define a closed convex polyhedral region of right-hand sides. Include also \(r\ge0\), where the minimizer is zero. These finitely many regions cover every feasible right-hand side, and their formulas agree on overlaps by uniqueness.

The segment between feasible \(r,r'\) stays feasible by interpolating feasible witnesses. Its intersection with each region is an interval. Subdivide at the finitely many interval endpoints. On each subsegment one formula (13) applies, with operator norm at most \(H_{\mathsf A}\). Summing the subsegment estimates proves (12).

In particular, no interpolated right-hand side is required to be DPP data.

### A numerical bound for the cube matrices

On an \(m\)-coordinate cube, let
\[
N_m=m2^{m-1}
\]
be the number of edge variables. Write \(\mathsf D_m\) for divergence and \(\mathsf O_m\) for outgoing sums. By (4), the original flow fiber is precisely
\[
\mathsf A_m f\le r(M,R),
\qquad
\mathsf A_m=
\begin{bmatrix}
-I\\ \mathsf D_m\\-\mathsf D_m\\\mathsf O_m
\end{bmatrix},
\qquad
r(M,R)=
\begin{bmatrix}
0\\b_{M,R}\\-b_{M,R}\\(2/\varepsilon)p_M
\end{bmatrix}.
\tag{15}
\]
No separate normalization row is needed.

The matrix has integer entries, and every row has squared Euclidean norm at most \(m\). For \(m\le6\), an independent \(k\)-row submatrix has \(k\le N_m\le192\). Its Gram matrix \(G\) is positive definite with integer entries, so
\[
\det G\ge1,\qquad
\operatorname{tr}G\le km\le1152.
\]
All its eigenvalues are at most \(1152\), giving
\[
\lambda_{\min}(G)\ge1152^{-(k-1)}
\]
and therefore
\[
\boxed{
\sigma_{\min}(\mathsf A_{m,I})^{-1}
\le1152^{(k-1)/2}
\le1152^{96}=H.
}
\tag{16}
\]
This is a numerical bound uniform over every matrix used below. Neither atom probabilities nor the ambient dimension enter it.

## 4. Uniform local Lipschitz selection up to six coordinates

Let \(M,N\) have gap \(\varepsilon\) on the same \(m\le6\) coordinates, and let \(R,Q\) be rank-one projectors. Write
\[
\delta_M=\|M-N\|_1,\qquad
\delta_R=\|R-Q\|_1.
\]
Both \(M+\varepsilon R\) and \(N+\varepsilon Q\) are positive contractions. Rank-one affinity and (5) give
\[
\begin{aligned}
\|b_{M,R}-b_{N,Q}\|_1
&=\varepsilon^{-1}
\|(p_{M+\varepsilon R}-p_M)
 -(p_{N+\varepsilon Q}-p_N)\|_1\\
&\le(4/\varepsilon)\delta_M+2\delta_R.
\end{aligned}
\tag{17}
\]
Also,
\[
\|(2/\varepsilon)(p_M-p_N)\|_1
\le(4/\varepsilon)\delta_M.
\]
Thus the Euclidean difference of the right-hand sides in (15) is at most
\[
2\|b_{M,R}-b_{N,Q}\|_1
 +(2/\varepsilon)\|p_M-p_N\|_1
\le(12/\varepsilon)\delta_M+4\delta_R.
\]
Applying (12), (16), and
\(\|x\|_1\le\sqrt{N_m}\|x\|_2\) proves
\[
\boxed{
\|F_{M,R}-F_{N,Q}\|_1
\le\Lambda\left(
\frac{12}{\varepsilon}\|M-N\|_1
+4\|R-Q\|_1\right),
\qquad m\le6.
}
\tag{18}
\]
This includes all support degeneracies on these coordinate sets.

The argument uses fixed inequality normals—not a general assertion that nearest-point selection is Lipschitz under arbitrary Hausdorff perturbations.

## 5. Exact product compatibility of the global selector

The essential interface statement is that **for every \(J\) containing \(\operatorname{supp}P\)**, not only its minimal support, selector (2) satisfies
\[
\boxed{
F_{K,P}(T\cup A,i)
=q_K(T)F_{M_T(K),P_J}(A,i),
\qquad i\in J\setminus A,
}
\tag{19}
\]
and vanishes on directions outside \(J\).

To prove this, (4) first annihilates every direction outside \(J\). All remaining edges split into disjoint blocks, one for each fixed outside pattern \(T\). By (7) and (10), the nonnegativity, divergence, and capacity constraints in this block are exactly those of
\[
q_K(T)\,\mathcal F_J(M_T(K),P_J).
\]
The block mass is forced to be \(q_K(T)\) by its divergence and the local version of (4). Consequently, normalization does not couple different blocks. Conversely, choosing any member of each such scaled local fiber gives a member of the full fiber. The full fiber is therefore exactly this embedded Cartesian product.

Writing a block as \(q_K(T)g_T\), the objective in (2) becomes
\[
\frac12\sum_Tq_K(T)^2\|g_T\|_2^2.
\]
Every \(q_K(T)\) is positive. The blocks minimize independently, and multiplication of a block objective by \(q_K(T)^2\) does not change its minimizer. This proves (19).

Thus this is one global choice compatible with every auxiliary coordinate set. At a coordinate projector, only edges in that coordinate survive, and their divergence fixes every edge, giving the unique coordinate flow. At a two-coordinate direction, lifting through any containing triple or larger set gives exactly the same selector.

No estimate here involves an inverse atom probability.

## 6. Global modulus and all support interfaces

Take arbitrary allowed \((K,P),(L,Q)\) on the same \(E\), and set
\[
J=\operatorname{supp}P\cup\operatorname{supp}Q.
\]
Then \(1\le |J|\le6\). Formula (19) represents both already-defined selectors in the same edge blocks.

Each local flow is nonnegative of mass one. Splitting the products therefore gives
\[
\begin{aligned}
\|F_{K,P}-F_{L,Q}\|_1
&\le\|q_K-q_L\|_1\\
&\quad+\sum_Tq_K(T)
 \|F_{M_T(K),P_J}-F_{M_T(L),Q_J}\|_1\\
&\le
\left(2+\frac{12\Lambda d_\varepsilon}{\varepsilon}\right)
\|K-L\|_1
+4\Lambda\|P-Q\|_1.
\end{aligned}
\tag{20}
\]
Here we used (8), (9), and (18). Restriction to \(J\) leaves the trace norm of \(P-Q\) unchanged. The sum is a probability average, with total weight one—not a count of outside patterns.

Because \(d_\varepsilon\ge1\) and \(\varepsilon<1/2\), constant (1) dominates both coefficients in (20). Hence
\[
\boxed{
\|F_{K,P}-F_{L,Q}\|_1
\le C_\varepsilon^{(3)}
\bigl(\|K-L\|_1+\|P-Q\|_1\bigr).
}
\]

This comparison covers triples meeting in two, one, or zero coordinates: their unions have at most four, five, or six coordinates respectively. It also covers nested supports, degeneration to two or one coordinates, arbitrary complex phases, and simultaneous changes of both inputs. The selector itself does not use the pair-dependent set \(J\); that set is used only to prove its modulus.

For every finite \(E\), (20) proves continuity on the entire allowed domain, hence Borel dependence. A coordinate permutation maps each full fiber onto the permuted fiber and preserves the objective in (2). Uniqueness yields
\[
F_{U_\sigma K U_\sigma^*,\,U_\sigma P U_\sigma^*}
(\sigma S,\sigma i)
=F_{K,P}(S,i).
\]
Only the matrix \(P\) is used, so changing the global phase of a representing vector changes nothing.

Finally, membership in the original fiber gives nonnegativity, exact divergence, mass one, and the required outgoing capacity. Every constant in (20) is independent of \(|E|\). The proof uses the bounded union size six and does not establish the unrestricted arbitrary-support theorem. \(\square\)


