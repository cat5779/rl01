PROVED

# Refinement-compatible selectors for uniformly bounded canonical components

## Theorem and scope

Fix \(0<\varepsilon<1/2\). For every integer \(r\ge1\), the statement
**(BCOMP)** in PR #124 holds. One (deliberately nonoptimal) admissible constant is

\[
\boxed{
C_{\varepsilon,r}
=\frac{10}{\varepsilon^2}(r!)^2\,2^{(r-1)(r+4)}.
}
\tag{1}
\]

More explicitly, for a finite coordinate set \(E\), let
\(\mathcal B_{E,r}^{\varepsilon}\) be the Hermitian kernels satisfying
\(\varepsilon I\preceq K\preceq(1-\varepsilon)I\) whose graph

\[
G_K=(E,\{\{i,j\}:i\ne j,\ K_{ij}\ne0\})
\]

has every connected component of size at most \(r\). There are Borel,
coordinate-permutation-equivariant maps into the original fibers (3) such that,
for every \(K,L\in\mathcal B_{E,r}^{\varepsilon}\) and every two rank-one
orthogonal projectors \(P,Q\),

\[
\|\Psi_{E,r}(K,P)-\Psi_{E,r}(L,Q)\|_1
\le C_{\varepsilon,r}
       \bigl(\|K-L\|_1+\|P-Q\|_1\bigr).
\]

The selectors below are defined by one recursive construction, and their
restrictions agree when the component-size bound is increased. No constant
uniform in \(r\) is asserted. In particular, this does not prove the
unrestricted dimension-free non-diagonal selector theorem.

The only non-elementary DPP input needed is **pointwise nonemptiness of the
stated local positive capacitated fibers**. This follows already from audited
input 1 of the task, applied to a single supplied block of the relevant fixed
size. We do not assume that the supplied-partition selector has any refinement
compatibility. All extension, refinement, and incompatible-partition arguments
are supplied below.

The argument is a mathematical proof, not a claim of external referee approval,
formal verification, or novelty certification. Its source task is
`research/dpp18/g17/TASK.md` at commit
`8f7f8d0460f7e6c59f2ae47d3ca631629601922b`.

## 1. Notation and elementary DPP estimates

For a finite coordinate set \(B\), write

\[
\mathscr E_B=\{(S,i): S\subseteq B,\ i\in B\setminus S\}.
\]

Flows are real vectors on \(\mathscr E_B\). All flow and probability-vector
norms denoted by \(\|\cdot\|_1\) are entrywise \(\ell^1\) norms. Matrix
\(\|\cdot\|_1\) is the **unnormalized Schatten trace norm**.

Let \(D_B\) be the incoming-minus-outgoing incidence matrix and \(O_B\) the
outgoing-sum matrix:

\[
(D_BF)(S)=\sum_{i\in S}F(S\setminus\{i\},i)
             -\sum_{i\notin S}F(S,i),\qquad
(O_BF)(S)=\sum_{i\notin S}F(S,i).
\tag{2}
\]

Put \(c=2/\varepsilon\), and let
\(b_{K,P}=\left.\frac{d}{dt}p_{K+tP}\right|_{t=0}\).
The task's fiber is

\[
\mathcal F_B(K,P)=
\{F\ge0:D_BF=b_{K,P},\;\mathbf1^TF=1,\;O_BF\le c p_K\}.
\tag{3}
\]

### 1.1 The unit-mass equation is redundant

The first DPP marginals give

\[
\sum_S |S|p_K(S)=\operatorname{tr}K,
\qquad
\sum_S |S|b_{K,P}(S)=\operatorname{tr}P=1.
\]

Every upward edge increases cardinality by one. Hence, for every real flow,

\[
\sum_S|S|(D_BF)(S)=\sum_{(S,i)\in\mathscr E_B}F(S,i).
\]

Consequently exact divergence already implies total mass one. We may omit the
mass row when describing the fiber by a fixed inequality matrix, without
changing the fiber. In particular every point of (3) has \(\|F\|_1=1\).

### 1.2 Uniform estimates for probabilities and derivatives

For \(S\subseteq B\), let \(J_S=I_{B\setminus S}\). The exact atom formula is

\[
p_K(S)=(-1)^{|B\setminus S|}\det(K-J_S).
\tag{4}
\]

For completeness, inclusion--exclusion gives
\(p_K(S)=\sum_{T\subseteq B\setminus S}(-1)^{|T|}\det K_{S\cup T}\).
Expanding the determinant in (4) in the diagonal terms of \(-J_S\) gives
exactly this sum.

If \(\varepsilon I\preceq K\preceq(1-\varepsilon)I\), then

\[
\|(K-J_S)^{-1}\|_{\mathrm{op}}\le\varepsilon^{-1}.
\tag{5}
\]

Indeed, writing \(U_S=I-2J_S\),

\[
K-J_S=\tfrac12U_S[I+U_S(2K-I)],
\qquad \|U_S(2K-I)\|_{\mathrm{op}}\le1-2\varepsilon.
\]

The Neumann-series estimate proves (5). In particular the inverse exists,
including when some off-diagonal entries of \(K\) vanish.

Differentiating (4) in a Hermitian direction \(H\) gives

\[
D p_K[H](S)=p_K(S)\operatorname{tr}((K-J_S)^{-1}H).
\]

Integrating along the segment between two gapped kernels yields

\[
\|p_K-p_L\|_1\le\varepsilon^{-1}\|K-L\|_1.
\tag{6}
\]

For a rank-one projector \(P\), a further kernel derivative is

\[
D_Kb_{K,P}[H](S)=p_K(S)
\left[
\operatorname{tr}(M^{-1}H)\operatorname{tr}(M^{-1}P)
-\operatorname{tr}(M^{-1}HM^{-1}P)
\right],\quad M=K-J_S.
\]

Its absolute value is at most
\(2\varepsilon^{-2}p_K(S)\|H\|_1\). Linearity in the direction also gives
\(\|b_{K,P}-b_{K,Q}\|_1\le\varepsilon^{-1}\|P-Q\|_1\). Thus

\[
\boxed{
\|b_{K,P}-b_{L,Q}\|_1
\le2\varepsilon^{-2}\|K-L\|_1
  +\varepsilon^{-1}\|P-Q\|_1.
}
\tag{7}
\]

No minimum atom probability is used in these estimates.

## 2. A relative Lipschitz selection device for these finite fibers

This section establishes the finite-dimensional extension tool, including
behavior on degenerate faces of the fiber.

### 2.1 Projection onto polyhedra with fixed normals

Let \(A\) be a fixed real matrix with \(m\) columns, and write

\[
C(u)=\{z\in\mathbb R^m:Az\le u\},\qquad
\pi(y,u)=\operatorname*{argmin}_{z\in C(u)}\|z-y\|_2^2
\]

when \(C(u)\ne\varnothing\). Then \(\pi\) is Lipschitz jointly in \((y,u)\)
on the entire feasible parameter domain. More precisely, it has Euclidean
Lipschitz constant at most

\[
\kappa_A=
\max\left(1,\max_{I:\,A_I\text{ has independent rows}}
                         \|A_I^\dagger\|_{\mathrm{op}}\right),
\tag{8}
\]

where \(A_I^\dagger=A_I^T(A_IA_I^T)^{-1}\).

**Proof.** At the minimizing point, the vector \(y-\pi(y,u)\) belongs to the
cone generated by the active constraint normals. This is the elementary
normal-cone characterization of a nearest point in a polyhedron. It follows
also by separating this finite generated cone: a separating direction would
be feasible for a sufficiently small step and would strictly decrease the
squared distance.

The conic representation can be reduced to a linearly independent subset of
active normals. To see this, if the normals in a positive representation are
dependent, subtract a suitable multiple of a nonzero linear dependence from
the coefficients until one positive coefficient becomes zero, preserving
nonnegativity; repeat.

For such an independent subset \(I\), define

\[
\lambda_I(y,u)=(A_IA_I^T)^{-1}(A_Iy-u_I),
\qquad
q_I(y,u)=y-A_I^T\lambda_I(y,u).
\tag{9}
\]

The region

\[
\Omega_I=\{(y,u):\lambda_I(y,u)\ge0,\;Aq_I(y,u)\le u\}
\]

is a closed convex polyhedron. On this region, \(A_Iq_I=u_I\), and the
normal-cone criterion proves \(\pi=q_I\). Include \(I=\varnothing\) with
\(q_I=y\). These finitely many regions cover the feasible parameter domain.

The affine map

\[
q_I=(I-A_I^\dagger A_I)y+A_I^\dagger u_I
\]

has Lipschitz constant at most \(\max(1,\|A_I^\dagger\|_{\mathrm{op}})\):
its two displayed summands have orthogonal ranges. The feasible parameter
domain is convex, since feasible witnesses can be interpolated. Any line
segment in it has a finite subdivision into the regions \(\Omega_I\). The
affine formulas agree at overlaps by uniqueness of the projection. Summing
the Lipschitz estimates over that subdivision proves (8). This proof does not
assume strict complementarity, an interior feasible point, or a stable active
set. \(\square\)

### 2.2 A quantitative bound for the flow constraint matrix

For \(|B|=n\), set \(m_n=n2^{n-1}\), the number of upward edges. By Section
1.1 the original fiber has the representation

\[
\mathcal F_B(K,P)=\{F:A_nF\le u_n(K,P)\},
\]

where

\[
A_n=\begin{pmatrix}-I\\D_B\\-D_B\\O_B\end{pmatrix},
\qquad
u_n(K,P)=\begin{pmatrix}0\\b_{K,P}\\-b_{K,P}\\c p_K\end{pmatrix}.
\tag{10}
\]

The coefficient matrix is fixed: only the right-hand side changes with the
kernel and direction.

The matrix \(A_n\) is **totally unimodular**. Here is a direct determinant
proof, so no integrality theorem is needed. Identity rows can be eliminated
from any square minor by expansion. Opposite duplicate incidence rows give
zero determinants; otherwise their signs can be changed, leaving a minor of
\([D_B;O_B]\). Whenever both the incidence row and outgoing row at a vertex
are present, add the outgoing row to the incidence row. Then negate all
outgoing rows. In every edge column there is now at most one entry \(-1\)
(at its source) and at most one entry \(+1\) (at its destination). Every
square matrix with that property has determinant \(0\) or \(\pm1\): expand
at a column with at most one nonzero entry, or, if every column has both
entries, use the zero column sums. This proves the claim for every minor.

For any \(q\) independent rows of \(A_n\), choose a nonsingular \(q\)-column
minor. Its determinant is \(\pm1\), and its inverse has entries in
\(\{0,\pm1\}\), by the cofactor formula. Placing that inverse in the
corresponding rows gives a right inverse of Euclidean operator norm at most
\(q\le m_n\). The Moore--Penrose right inverse has no larger operator norm.
Consequently

\[
\kappa_{A_n}\le m_n.
\tag{11}
\]

Equations (6)--(7) also imply, with
\(d((K,P),(L,Q))=\|K-L\|_1+\|P-Q\|_1\),

\[
\begin{aligned}
\|u_n(K,P)-u_n(L,Q)\|_2
&\le2\|b_{K,P}-b_{L,Q}\|_1+c\|p_K-p_L\|_1\\
&\le6\varepsilon^{-2}\|K-L\|_1+2\varepsilon^{-1}\|P-Q\|_1\\
&\le6\varepsilon^{-2}d((K,P),(L,Q)).
\end{aligned}
\tag{12}
\]

### 2.3 Preserving an already prescribed Lipschitz section

Let \(X_n\) be the compact space of gapped \(n\)-coordinate kernels and
rank-one projectors, with metric \(d\). Suppose a nonempty closed,
permutation-invariant subset \(Z\subseteq X_n\) has a permutation-equivariant
section

\[
h(z)\in\mathcal F_{[n]}(z),\qquad
\|h(z)-h(z')\|_1\le Ld(z,z').
\]

For every edge coordinate \(e\), define the scalar McShane extension

\[
\widetilde h_e(x)=\inf_{z\in Z}\{h_e(z)+L d(x,z)\}.
\tag{13}
\]

The infimum is over a nonempty compact set. Each coordinate is
\(L\)-Lipschitz and equals \(h_e\) on \(Z\): the lower inequality follows
from the Lipschitz estimate for \(h_e\), and the upper inequality follows by
choosing \(z=x\). Thus \(\widetilde h\) is Euclidean
\(\sqrt{m_n}L\)-Lipschitz.

Average the extension over the finite permutation group:

\[
H(x)=\frac1{n!}\sum_{\sigma\in\mathfrak S_n}
                       \sigma^{-1}\widetilde h(\sigma x).
\tag{14}
\]

This makes \(H\) equivariant without increasing its Euclidean Lipschitz
constant, and leaves \(H=h\) on \(Z\). Finally set

\[
f_n(x)=\pi(H(x),u_n(x)).
\tag{15}
\]

Nonemptiness of the local fibers makes this well-defined. It is a section of
the *original* fiber, including its original capacity and unit mass. Since
projection fixes feasible points, it agrees exactly with \(h\) on \(Z\).
Uniqueness of the Euclidean projection and permutation invariance of its
metric imply equivariance. Equations (8), (11), and (12) give

\[
\boxed{
\|f_n(x)-f_n(x')\|_1
\le\left(m_n^2 L+6m_n^{3/2}\varepsilon^{-2}\right)d(x,x').
}
\tag{16}
\]

In deriving (16), use \(\|v\|_1\le\sqrt{m_n}\|v\|_2\), and bound the
Euclidean norm of a pair by the sum of the two norms. In particular this
relative extension remains Lipschitz at arbitrary intersections of fiber
faces and of the prescribed boundary strata.

## 3. Tensorization and exact refinement compatibility

We now describe how compatible local selectors give a global selector, and
prove the required uniform estimates.

Suppose, for \(1\le j\le r\), that equivariant local sections \(f_j\) of the
full \(j\)-coordinate fibers have Lipschitz constants at most \(a\), and are
**refinement-compatible** in the following exact sense: whenever a local
kernel is block diagonal over a proper partition, its selected flow is the
tensorization of the smaller-block selectors described below.

### 3.1 Homogeneous local flows

For a positive semidefinite rank-at-most-one matrix \(V\) on a local block,
put \(w=\operatorname{tr}V\) and define

\[
\widehat f_B(K,V)=
\begin{cases}
w f_{|B|}(K,V/w),&w>0,\\
0,&w=0.
\end{cases}
\tag{17}
\]

The transport from \([|B|]\) to \(B\) is independent of the chosen labeling,
by permutation equivariance. A nonzero \(V/w\) is a rank-one projector.
The flow (17) has nonnegative entries, divergence \(b_{K,V}\), mass \(w\),
and outgoing bound \(cw p_K\).

For rank-at-most-one positive matrices \(V=wR\), \(W=vT\),

\[
\|\widehat f_B(K,V)-\widehat f_B(L,V)\|_1
\le a w\|K-L\|_1,
\tag{18}
\]

and

\[
\|\widehat f_B(K,V)-\widehat f_B(K,W)\|_1
\le(1+2a)\|V-W\|_1.
\tag{19}
\]

For (19), use unit mass and positivity to obtain

\[
\|w f(K,R)-v f(K,T)\|_1
\le|w-v|+a\min(w,v)\|R-T\|_1,
\]

then use
\(|w-v|\le\|V-W\|_1\) and
\(\min(w,v)\|R-T\|_1\le2\|V-W\|_1\).
If either weight is zero, the claim follows directly from the mass of the
other flow. Thus no inverse of a small block weight occurs.

### 3.2 Tensorization over a supplied partition

Let \(\alpha\) be a partition over which \(K\) is block diagonal, with
\(|B|\le r\) for every \(B\in\alpha\). Set
\(P_B=\Pi_BP\Pi_B\), \(w_B=\operatorname{tr}P_B\).
For \(i\in B\) define

\[
\mathcal T_\alpha(K,P)(S,i)
=\widehat f_B(K_B,P_B)(S\cap B,i)
                 \prod_{C\in\alpha,\,C\ne B}p_{K_C}(S\cap C).
\tag{20}
\]

The product over no blocks is one. Although \(P\) need not be block diagonal,
its cross-block entries do not contribute to \(b_{K,P}\). Indeed, (4) gives

\[
b_{K,P}(S)=p_K(S)\operatorname{tr}((K-I_{E\setminus S})^{-1}P),
\]

and the inverse is block diagonal. Therefore

\[
b_{K,P}(S)
=\sum_{B\in\alpha}b_{K_B,P_B}(S\cap B)
                     \prod_{C\ne B}p_{K_C}(S\cap C).
\tag{21}
\]

The divergence of (20) is exactly (21). Positivity is immediate. Summing
(20) over all edges gives \(\sum_Bw_B=\operatorname{tr}P=1\). At each
configuration,

\[
\begin{aligned}
(\mathcal T_\alpha(K,P))_{\rm out}(S)
&\le c\sum_B w_B p_{K_B}(S\cap B)
                           \prod_{C\ne B}p_{K_C}(S\cap C)\\
&=c p_K(S).
\end{aligned}
\tag{22}
\]

Thus (20) belongs to the original global fiber with no capacity enlargement.

### 3.3 Independence of a coarser supplied partition

If a block \(B\) is itself split, refinement compatibility of its local
selector expands the \(B\)-term of (20) into its subblock terms. For
\(w_B>0\), the normalized compression on a subblock \(C\subseteq B\) has
weight \(w_C/w_B\). The factor \(w_B\) in (17) cancels that denominator.
The outside probability factors multiply to exactly the outside factor for
\(C\). If \(w_B=0\), all its subblock weights are zero. This proves equality
of the two tensorizations, not merely an estimate.

It follows by refinement to canonical components that (20) is independent
of which partition into blocks of size at most \(r\) is supplied. In
particular it equals the tensorization over the canonical component
partition of \(K\). Denote that one global selector by \(\Psi_r(K,P)\).

### 3.4 The common-partition Lipschitz estimate

Assume \(K,L\) are block diagonal over the same \(\alpha\), and put
\(\delta_B=\|K_B-L_B\|_1\). Then
\(\sum_B\delta_B=\|K-L\|_1\). At fixed \(P\), (18), (6), and the unit
mass of outside probabilities give

\[
\begin{aligned}
\|\mathcal T_\alpha(K,P)-\mathcal T_\alpha(L,P)\|_1
&\le a\sum_Bw_B\delta_B
 +\varepsilon^{-1}\sum_Bw_B\sum_{C\ne B}\delta_C\\
&\le\max(a,\varepsilon^{-1})\|K-L\|_1.
\end{aligned}
\tag{23}
\]

For changing projectors at a fixed kernel, (19) gives

\[
\begin{aligned}
\|\mathcal T_\alpha(K,P)-\mathcal T_\alpha(K,Q)\|_1
&\le(1+2a)\sum_B\|\Pi_B(P-Q)\Pi_B\|_1\\
&\le(1+2a)\|P-Q\|_1.
\end{aligned}
\tag{24}
\]

The last inequality is trace-norm contractivity of coordinate pinching.
Thus, with

\[
A=\max(\varepsilon^{-1},1+2a),
\]

we have

\[
\|\mathcal T_\alpha(K,P)-\mathcal T_\alpha(L,Q)\|_1
\le A(\|K-L\|_1+\|P-Q\|_1).
\tag{25}
\]

The number of blocks does not enter. In (23) its potential contribution is
removed by \(\sum_B w_B=1\); in (24) it is removed by trace-norm pinching.

## 4. Incompatible canonical partitions: a five-unit comparison

Let \(\alpha\) and \(\beta\) be the canonical component partitions of
\(K\) and \(L\), respectively, each with block sizes at most \(r\). Their
union can be arbitrarily large. We do not use a common coarsening.

Let \(\gamma=\alpha\wedge\beta\) be their common refinement into nonempty
intersections. For a coordinate partition \(\eta\), write

\[
\mathcal P_\eta X=\sum_{B\in\eta}\Pi_BX\Pi_B.
\]

Coordinate pinchings commute and satisfy
\(\mathcal P_\alpha\mathcal P_\beta=\mathcal P_\gamma\).
They preserve the spectral gap and contract the trace norm: they are
averages of conjugations by diagonal sign unitaries.

Define

\[
K_0=\mathcal P_\gamma K=\mathcal P_\beta K,
\qquad
L_0=\mathcal P_\gamma L=\mathcal P_\alpha L.
\tag{26}
\]

For \(\delta=\|K-L\|_1\),

\[
\begin{aligned}
\|K-K_0\|_1
 &=\|(I-\mathcal P_\beta)(K-L)\|_1\le2\delta,\\
\|L-L_0\|_1
 &=\|(I-\mathcal P_\alpha)(L-K)\|_1\le2\delta,\\
\|K_0-L_0\|_1
 &=\|\mathcal P_\gamma(K-L)\|_1\le\delta.
\end{aligned}
\tag{27}
\]

The pair \((K,K_0)\) has common partition \(\alpha\), the pair
\((K_0,L_0)\) has common partition \(\gamma\), and the pair \((L_0,L)\)
has common partition \(\beta\). All these blocks have size at most \(r\).
Even when an intermediate kernel has further disconnected blocks, Section
3.3 identifies its selector with the appropriate supplied-partition formula.
Applying (25) along these three comparisons gives

\[
\boxed{
\|\Psi_r(K,P)-\Psi_r(L,Q)\|_1
\le5A\|K-L\|_1+A\|P-Q\|_1
\le5A\,d((K,P),(L,Q)).
}
\tag{28}
\]

The projectors themselves are **not** pinched as inputs: they remain the
original rank-one \(P\) and \(Q\) on all three legs. Pinching their difference
is used only for the norm estimate (24).

Sections 3--4 prove the following reusable conclusion: any compatible local
family through size \(r\), with maximum local Lipschitz constant \(a\),
produces a selector on the entire bounded-canonical-component class with
constant \(5\max(\varepsilon^{-1},1+2a)\).

## 5. Constructing compatible local selectors by induction

We now construct the local family required above. This is the step that
supplies quantitative compatibility at *every* splitting stratum.

For \(n=1\), the unique flow has its single edge equal to one. This is a
constant local section, equivariant and trivially refinement-compatible.
It satisfies the capacity since \(1-K_{11}\ge\varepsilon\).
Sections 3--4 give the global diagonal case. Set, for convenience,

\[
B_1=10\varepsilon^{-2}.
\]

This is larger than the bound \(5/\varepsilon\) obtained from (28).
We maintain the stronger induction invariant

\[
B_k\ge5\max\left(\varepsilon^{-1},
                     1+2\max_{1\le j\le k}a_j\right),
\qquad a_1=0,
\]

in addition to the global Lipschitz bound. The invariant holds at \(k=1\).

Inductively suppose compatible local sections have been constructed through
size \(n-1\), and their global selector has Lipschitz constant at most
\(B_{n-1}\), uniformly in the ambient coordinate set.

In the local parameter space \(X_n\), let

\[
Z_n=\{(K,P)\in X_n: G_K\text{ is disconnected}\}.
\]

This is a nonempty compact permutation-invariant set: reducible kernels form
a finite union of closed block-diagonal loci. On \(Z_n\), define

\[
h_n(K,P)=\Psi_{n-1}(K,P).
\tag{29}
\]

Every canonical component here has size at most \(n-1\), so the definition
uses only previously constructed local sections. Sections 3--4 show that
\(h_n\) is a feasible, equivariant section and is \(B_{n-1}\)-Lipschitz,
including between points on incompatible splitting strata.

Apply Section 2.3 with \(Z=Z_n\), \(L=B_{n-1}\). This defines the local
section \(f_n\) on all of \(X_n\), and gives the finite constant

\[
a_n=m_n^2B_{n-1}+6m_n^{3/2}\varepsilon^{-2}.
\tag{30}
\]

It agrees *exactly* with (29) whenever the kernel is reducible. If a proper
partition is supplied at such a kernel, its tensorization using the smaller
local sections equals (29) by their existing refinement compatibility.
Thus \(f_n\) has exact compatibility with every proper refinement, not just
with one chosen splitting.

More quantitatively, for any proper coordinate partition \(\eta\) of the
local block and any gapped kernel \(K\),

\[
\boxed{
\|f_n(K,P)-\mathcal T_\eta(\mathcal P_\eta K,P)\|_1
\le a_n\|K-\mathcal P_\eta K\|_1.
}
\tag{31}
\]

Indeed the local value at \(\mathcal P_\eta K\) is exactly the tensorization,
and (31) is the already proved local Lipschitz estimate. The same \(a_n\)
works simultaneously for all proper partitions, including their intersections.

### Closing the constants

For \(n\ge2\), define

\[
B_n=16m_n^2B_{n-1}.
\tag{32}
\]

These numbers dominate all the global constants produced by the induction.
To verify this explicitly, let \(a_{<n}\) be the maximum of the previous
local constants. The strengthened induction invariant gives
\(B_{n-1}\ge5\max(\varepsilon^{-1},1+2a_{<n})\).
Equation (30) therefore dominates \(a_{<n}\). Since
\(m_n\ge4\) and \(B_{n-1}\ge10\varepsilon^{-2}\),

\[
a_n\le1.3\,m_n^2B_{n-1}.
\]

Hence

\[
5(1+2a_n)\le5+13m_n^2B_{n-1}\le16m_n^2B_{n-1}=B_n,
\]

and also \(5\varepsilon^{-1}\le B_n\). Equation (28) closes the induction.
Solving (32), using \(m_n=n2^{n-1}\), yields

\[
B_r
=10\varepsilon^{-2}\,16^{r-1}
        \prod_{n=2}^r(n2^{n-1})^2
=10\varepsilon^{-2}(r!)^2\,2^{(r-1)(r+4)},
\]

which is (1).

## 6. The selector and all requested properties

For each finite nonempty \(E\), transport the local maps from \([n]\) to
its blocks using any bijections; local equivariance makes the result
independent of those choices. For \(K\in\mathcal B_{E,r}^\varepsilon\),
let \(\alpha(K)\) be its canonical component partition, and define

\[
\boxed{\Psi_{E,r}(K,P)=\mathcal T_{\alpha(K)}(K,P).}
\tag{33}
\]

For an empty coordinate set there are no rank-one projectors, so the claim
is vacuous.

* **Nonnegativity and exact divergence:** equations (17), (20), and (21).
* **Unit total mass and original outgoing capacity:** equations (22) and
  \(\sum_B\operatorname{tr}P_B=1\). The local projection also has unit mass
  by Section 1.1; no relaxed fiber is used.
* **Exact refinement compatibility:** the recursive boundary identity (29),
  the cancellation of all normalization weights in Section 3.3, and the
  quantitative estimate (31).
* **Simultaneous Lipschitz stability:** equations (28), (30), and (32), with
  the constant (1), independent of \(|E|\) and the number of components.
* **Borel dependence:** follows from the proved Lipschitz estimate on each
  parameter domain, including all splitting interfaces.
* **Full coordinate-permutation covariance:** scalar extension is
  symmetrized in (14); the unique Euclidean projection is equivariant;
  homogeneous compression and tensorization commute with coordinate
  bijections; and canonical components are transported by those bijections.
* **Classification:** all fixed \(r\ge1\) are positive. The constants grow
  with \(r\); no unrestricted dimension-free conclusion follows.

This completes the proof of (BCOMP). \(\square\)

The construction is an exact variational definition of a single selector;
it is not asserted to be computationally efficient. In particular, the
compact-domain infima in (13) are part of the definition, not approximations
by a finite grid. The supplementary script does not implement those infima.

## Source boundary

The task, its allowed supplied-partition theorem, and the original fiber
constraints are the repository inputs. The relative extension construction,
its compatibility induction, the fixed-normal projection proof and
quantitative bound, and the common-refinement comparison are established in
this document. Relevant repository records are PR #124 (the frozen task),
PR #102 (the full-fiber definition and pointwise feasibility), PR #117 (the
supplied-partition theorem), and PR #120 (the previously known matching-block
case). No result from another branch is silently imported with enlarged scope.