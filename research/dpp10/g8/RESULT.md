REVIEW NOTE: The primary theorem remains INCOMPLETE. This text includes the local boundary, quantifier, sign-convention and citation corrections listed in STATUS.md. The independent report reviews the received version; no separate full review of this edited text is claimed.

# INCOMPLETE

I do not have a proof or a counterexample to the full dimension-free selection statement (DF). What can be proved is substantially stronger than fixed-\(n\) continuity at the level of the *data* of the flow problem: both the DPP laws and the divergence perturbations admit dimension-free \(L^1\)/transport estimates. The unresolved step is to convert the resulting **signed** dimension-free repair into a **nonnegative, source-capacitated, globally consistent equivariant selection**. I also obtain two nontrivial restricted cases with explicit dimension-free selectors.

Throughout write \(P=vv^*\), \(Q=ww^*\).

## 1. Exact coupling reformulation

For every \(S\subseteq E\),

\[
p_K(S)=(-1)^{|S^c|}\det(K-I_{S^c}).
\]

Hence, because a determinant is affine under a rank-one perturbation,

\[
p_{K+hP}(S)=p_K(S)+h\,b_{K,P}(S)
\tag{1}
\]

exactly, whenever \(K+hP\) is a positive contraction.

Fix

\[
h=\frac{\epsilon}{2},\qquad \mu=p_K,\qquad \nu=p_{K+hP}.
\]

Given an admissible flow \(F\), define

\[
\Pi(S,S\cup\{i\})=hF(S,i),
\]

and

\[
\Pi(S,S)=p_K(S)-h\sum_{i\notin S}F(S,i).
\]

The capacity bound makes the last quantity nonnegative. The first marginal is \(p_K\), while, using the divergence equation and (1),

\[
\Pi_2(T)
=p_K(T)-h\,\mathrm{out}_F(T)+h\,\mathrm{in}_F(T)
=p_K(T)+hb_{K,P}(T)
=p_{K+hP}(T).
\]

Thus admissible flows are exactly the couplings of
\(\operatorname{DPP}(K)\) and \(\operatorname{DPP}(K+hP)\) supported on

\[
(S,S),\qquad (S,S\cup\{i\}).
\tag{2}
\]

Conversely every such coupling gives the required flow after division of its off-diagonal mass by \(h\). Moreover,

\[
\sum_{S,i\notin S}F(S,i)
=\sum_S |S|\,b_{K,P}(S)
=\frac{d}{dh}\operatorname{Tr}(K+hP)\Big|_{0}
=1,
\]

so the mass normalization actually follows from the divergence equation.

There is also an optimal-transport characterization. For every coupling \((X,Y)\),

\[
d_H(X,Y)^2\ge d_H(X,Y)\ge |Y|-|X|.
\]

Since \(E|Y|-E|X|=h\), the minimum possible expected squared Hamming distance is \(h\), and equality holds exactly for couplings supported as in (2). Thus the feasible-flow polytope is precisely an optimal-transport face.

The existence of at least one such coupling is part of the known DPP monotone-coupling theory, not a new claim here; Lyons' 2003 paper contains the projection/dilation construction relevant to the stated feasibility input. [Lyons, Proposition 10.3](https://numdam.org/item/10.1007/s10240-003-0016-0.pdf)

## 2. A dimension-free \(W_1\) estimate for finite DPPs

Let \(\mu_A\) denote the DPP with kernel \(A\), and put Hamming distance on \(2^E\). Then

\[
\boxed{W_1(\mu_A,\mu_B)\le \|A-B\|_1.}
\tag{3}
\]

This has no dependence on \(n\).

First suppose \(A\le B\). General Loewner-order stochastic domination for determinantal measures gives a coupling \(X\subseteq Y\). The noncommutative stochastic domination used here follows from Borcea–Brändén–Liggett, Theorem 4.13 and Proposition 4.15. [Borcea-Branden-Liggett, Theorem 4.13 and Proposition 4.15](https://www.ams.org/journals/jams/2009-22-02/S0894-0347-08-00618-8/S0894-0347-08-00618-8.pdf) Hence

\[
E\,d_H(X,Y)
=E(|Y|-|X|)
=\operatorname{Tr}(B-A).
\]

Therefore

\[
W_1(\mu_A,\mu_B)\le\operatorname{Tr}(B-A)=\|B-A\|_1.
\tag{4}
\]

Now let \(A,B\) be arbitrary interior positive contractions and write

\[
H=B-A=H_+-H_-.
\]

Along \(A_t=A+tH\), choose a sufficiently fine partition so that for each increment \(\delta\),

\[
C=A_t+\delta H_+
\]

remains a positive contraction. Then

\[
A_t\le C,\qquad A_{t+\delta}\le C.
\]

Applying (4) twice,

\[
\begin{aligned}
W_1(\mu_{A_t},\mu_{A_{t+\delta}})
&\le
W_1(\mu_{A_t},\mu_C)+W_1(\mu_C,\mu_{A_{t+\delta}})\\
&\le\delta\operatorname{Tr}H_+
+\delta\operatorname{Tr}H_-\\
&=\delta\|H\|_1.
\end{aligned}
\]

Summing gives (3) for interior kernels. For arbitrary positive contractions, set A_delta=(1-2delta)A+delta I and B_delta=(1-2delta)B+delta I, with 0<delta<1/2. Their DPP probabilities converge entrywise to those of A and B by the finite determinant formulas. On the finite configuration space W_1 is continuous, so letting delta decrease to zero proves (3) for all positive contractions, including boundary kernels.

Since \(d_H(S,T)\ge {\bf1}_{S\ne T}\),

\[
\boxed{
\sum_S|p_A(S)-p_B(S)|
=2\,d_{\rm TV}(\mu_A,\mu_B)
\le2\|A-B\|_1.
}
\tag{5}
\]

This particular deduction is all that is needed below. Borcea–Brändén–Liggett's broader framework places determinantal measures in the strongly Rayleigh class. [Borcea-Branden-Liggett, Proposition 3.5](https://www.ams.org/journals/jams/2009-22-02/S0894-0347-08-00618-8/S0894-0347-08-00618-8.pdf)

## 3. The divergence data themselves have a dimension-free signed repair

Using (1) with \(h=\epsilon/2\), for every Hamming-1-Lipschitz \(\phi\),

\[
\langle\phi,b_{K,P}\rangle
=
\frac{E_{K+hP}\phi-E_K\phi}{h}.
\]

Consequently

\[
\begin{aligned}
|\langle\phi,b_{K,P}-b_{L,Q}\rangle|
&\le \frac1h\Big(
W_1(\mu_{K+hP},\mu_{L+hQ})
+W_1(\mu_K,\mu_L)\Big)\\
&\le\frac1h
\Big(\|K-L+h(P-Q)\|_1+\|K-L\|_1\Big)\\
&\le
\frac4\epsilon\|K-L\|_1+\|P-Q\|_1.
\end{aligned}
\tag{6}
\]

The finite-graph Kantorovich–Rubinstein/min-cost-flow duality on the Boolean cube now gives a **signed** upward-edge flow \(G\) satisfying

\[
\operatorname{div}G=b_{K,P}-b_{L,Q}
\]

and

\[
\boxed{
\sum_{S,i\notin S}|G(S,i)|
\le
\frac4\epsilon\|K-L\|_1+\|P-Q\|_1.
}
\tag{7}
\]

Coefficients of \(G\) are allowed to be negative; an upward orientation merely fixes one orientation of each cube edge.

The capacity vectors are dimension-free stable as well. By (5),

\[
\begin{aligned}
\sum_S\left|
\frac2\epsilon p_K(S)-\frac2\epsilon p_L(S)
\right|
&\le
\frac4\epsilon\|K-L\|_1.
\end{aligned}
\tag{8}
\]

Thus neither the divergence equations nor the right sides of the outgoing-capacity constraints cause an obvious dimension blow-up.

### The missing step

Starting with an admissible \(F_{K,P}\), (7) supplies a small signed correction; because div G=b_(K,P)-b_(L,Q), the corrected flow for the second divergence is F_(K,P)-G. But

\[
F_{K,P}-G
\]

need not be nonnegative, and even after repairing negative coordinates its row sums need not obey the new capacities. Individual feasibility gives no lower bound on the mass of each edge: admissible flows can lie on high-codimension faces with many zero edges.

There is some aggregate slack. For example one may perform the known rank-one coupling at \(h_0=3\epsilon/4\), obtaining a feasible flow with

\[
\operatorname{out}(S)\le
\frac{1}{h_0}p_K(S)
=\frac{4}{3\epsilon}p_K(S)
<
\frac2\epsilon p_K(S).
\]

But that is only row-sum slack; it is not an edgewise interior-point estimate and therefore does not absorb an arbitrary signed \(G\).

What remains unproved is a dimension-free positive-repair/selection principle of the following strength: construct, in one globally compatible manner,

\[
F(K,P)\in\mathcal F(K,P)
\]

such that the signed estimate (7) can always be realized while preserving \(F\ge0\) and the row capacities, with \(O_\epsilon(D)\) change where

\[
D=\|K-L\|_1+\|P-Q\|_1.
\]

Even a dimension-free Hausdorff estimate between the polytopes would not by itself automatically supply a dimension-free Lipschitz **single-valued**, Borel, permutation-equivariant selector in \(\ell^1\). This is the exact unresolved part of the full theorem.

I have no family proving that this step is impossible, so this is not a disproof.

## 4. Full restricted theorem: diagonal kernels

Suppose

\[
K=\operatorname{diag}(k_1,\ldots,k_n),
\qquad
\epsilon\le k_i\le1-\epsilon,
\]

and put

\[
a_i=P_{ii}=|v_i|^2,\qquad \sum_i a_i=1.
\]

Then

\[
p_K(S)=
\prod_{i\in S}k_i
\prod_{i\notin S}(1-k_i),
\]

and direct differentiation gives

\[
b_{K,P}(S)
=p_K(S)
\left(
\sum_{i\in S}\frac{a_i}{k_i}
-
\sum_{i\notin S}\frac{a_i}{1-k_i}
\right).
\]

Define

\[
\boxed{
F_{K,P}(S,i)
=p_K(S)\frac{a_i}{1-k_i},
\qquad i\notin S.
}
\tag{9}
\]

For \(i\in S\),

\[
F(S\setminus\{i\},i)
=p_K(S)\frac{a_i}{k_i},
\]

so (9) has exactly the required divergence.

Furthermore,

\[
\sum_{S,i\notin S}F(S,i)
=\sum_i a_i=1,
\]

and

\[
\operatorname{out}(S)
\le \frac1\epsilon p_K(S),
\tag{10}
\]

which is twice as strong as required.

This is Borel, depends only on \(P\), and is permutation-equivariant.

It is also dimension-free Lipschitz. For fixed \(i\), let
\(\mu_k^{(i)}\) be the product Bernoulli law on \(E\setminus\{i\}\).
Then the \(i\)-edge component of (9) is simply

\[
a_i\mu_k^{(i)}.
\]

For another diagonal \(L=\operatorname{diag}(l_i)\) and \(c_i=Q_{ii}\),

\[
\begin{aligned}
\|F_{K,P}-F_{L,Q}\|_1
&\le
\sum_i|a_i-c_i|
+\sum_i c_i
\|\mu_k^{(i)}-\mu_l^{(i)}\|_1.
\end{aligned}
\]

A common-uniform coupling of product Bernoullis gives

\[
\|\mu_k^{(i)}-\mu_l^{(i)}\|_1
\le2\sum_{j\ne i}|k_j-l_j|.
\]

Therefore

\[
\|F_{K,P}-F_{L,Q}\|_1
\le
\sum_i|a_i-c_i|
+2\sum_j|k_j-l_j|.
\]

Diagonal pinching is trace-norm contractive, so

\[
\sum_i|a_i-c_i|
\le\|P-Q\|_1.
\]

Hence

\[
\boxed{
\|F_{K,P}-F_{L,Q}\|_1
\le
2\|K-L\|_1+\|P-Q\|_1
\le2D.
}
\tag{11}
\]

Thus the frozen theorem is true, with \(C=2\), on the class of diagonal kernels, for completely arbitrary \(v,w\).

## 5. Full restricted theorem: coordinate birth directions, arbitrary kernels

Now let \(v=e_j\), while \(K\) is arbitrary.

For every admissible flow, testing the divergence equation against
\({\bf1}_{j\in S}\) gives

\[
\sum_{S:j\notin S}F(S,j)
=
\sum_S{\bf1}_{j\in S}b(S)
=
\frac d{dh}K_{jj}\Big|_{K+hE_{jj}}
=1.
\tag{12}
\]

Testing against \({\bf1}_{i\in S}\) for \(i\ne j\) gives total mass zero on all \(i\)-edges. Nonnegativity therefore forces

\[
F(S,i)=0\qquad(i\ne j).
\]

So the admissible flow is unique.

Put \(R=E\setminus\{j\}\). For \(A\subseteq R\), set

\[
q(A)=F(A,j)=b(A\cup\{j\}).
\]

For every \(B\subseteq R\),

\[
\begin{aligned}
\sum_{A\supseteq B}q(A)
&=
\sum_{T\supseteq B\cup\{j\}}b(T)\\
&=
\left.
\frac d{dh}
\det(K_{B\cup\{j\}}+hE_{jj})
\right|_{h=0}\\
&=\det K_B.
\end{aligned}
\]

These are exactly the inclusion probabilities of the DPP with kernel \(K_R\); Möbius inversion therefore yields

\[
\boxed{
F_{K,e_j}(A,j)=p_{K_R}(A).
}
\tag{13}
\]

It remains to verify the capacity. Let

\[
L=K(I-K)^{-1}.
\]

Its eigenvalues lie in

\[
\left[\frac{\epsilon}{1-\epsilon},
      \frac{1-\epsilon}{\epsilon}\right].
\]

For a fixed configuration \(A\subseteq R\), the \(L\)-ensemble formula gives the conditional odds

\[
\frac{p_K(A\cup\{j\})}{p_K(A)}
=
L_{jj}-L_{jA}L_A^{-1}L_{Aj}.
\tag{14}
\]

The Schur complement in (14) lies in the same interval: it is the reciprocal of a diagonal entry of the inverse of the relevant principal matrix. Consequently

\[
\Pr(j\notin X\mid X\cap R=A)\ge\epsilon.
\]

Since

\[
p_{K_R}(A)=p_K(A)+p_K(A\cup\{j\}),
\]

we get

\[
F(A,j)=p_{K_R}(A)\le\frac1\epsilon p_K(A).
\tag{15}
\]

Again this is stronger than required.

For the same coordinate \(j\), (5) and compression contractivity give

\[
\begin{aligned}
\sum_A|F_{K,e_j}(A,j)-F_{L,e_j}(A,j)|
&=
\sum_A|p_{K_R}(A)-p_{L_R}(A)|\\
&\le2\|K_R-L_R\|_1\\
&\le2\|K-L\|_1.
\end{aligned}
\tag{16}
\]

For two distinct coordinate directions \(e_i,e_j\), the two flows have total mass one on disjoint edge types, hence their distance is \(2\), while

\[
\|e_ie_i^*-e_je_j^*\|_1=2.
\]

Thus this entire restricted class also has a dimension-free \(C=2\).

## 6. An exact obstruction to one tempting method

For a fixed kernel K with a nonzero off-diagonal entry, there cannot be a selector simultaneously positive and linear in the direction matrix P. Thus no such scheme works for the full kernel class. Diagonal K does admit the positive-linear selector in Section 4.

Indeed suppose

\[
F_{K,P}(S,i)=\operatorname{Tr}(A_{S,i}P),
\qquad A_{S,i}\ge0.
\]

For every flow, testing against the coordinate indicator as above gives

\[
\sum_{S:i\notin S}F(S,i)=P_{ii}.
\]

Hence, for every \(P\),

\[
\sum_{S:i\notin S}\operatorname{Tr}(A_{S,i}P)
=\operatorname{Tr}(E_{ii}P),
\]

so

\[
\sum_{S:i\notin S}A_{S,i}=E_{ii}.
\]

Positive-semidefinite summands of the rank-one matrix \(E_{ii}\) must themselves be multiples of \(E_{ii}\). Thus such a flow could depend only on the diagonal entries \(P_{ii}\).

But \(b_{K,P}\) generally depends on off-diagonal entries of \(P\). For \(n=2\),

\[
b_{K,P}(\{1,2\})
=
K_{22}P_{11}+K_{11}P_{22}
-K_{12}P_{21}-K_{21}P_{12}.
\]

Taking \(K_{12}\ne0\) and two rank-one projectors with the same diagonal but different off-diagonal phase gives different \(b\). Contradiction.

This rules out a natural positive-linear/POVM-type construction, but it is only a **method obstruction**, not an obstruction to nonlinear selections such as the one requested in (DF).

## 7. What (DF) would imply for intrinsic rates

Assume the frozen theorem were true, and write

\[
r_{K,P}(S,i)=\frac{F_{K,P}(S,i)}{p_K(S)}.
\]

All configuration probabilities are positive under the spectral gap assumption.

Let

\[
D=\|K-L\|_1+\|P-Q\|_1.
\]

Then the \(p_K\)-weighted mean rate difference satisfies

\[
\begin{aligned}
&\sum_Sp_K(S)
 \sum_{i\notin S}
 |r_{K,P}(S,i)-r_{L,Q}(S,i)|\\
&\quad =
\sum_{S,i\notin S}
\left|
F_{K,P}(S,i)
-\frac{p_K(S)}{p_L(S)}F_{L,Q}(S,i)
\right|\\
&\quad\le
\|F_{K,P}-F_{L,Q}\|_1\\
&\qquad+
\sum_S
\frac{|p_K(S)-p_L(S)|}{p_L(S)}
\operatorname{out}_{L,Q}(S)\\
&\quad\le
C_\epsilon D
+\frac2\epsilon\sum_S|p_K(S)-p_L(S)|\\
&\quad\le
C_\epsilon D+\frac4\epsilon\|K-L\|_1.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_Sp_K(S)\sum_{i\notin S}|r_{K,P}-r_{L,Q}|
\le
\left(C_\epsilon+\frac4\epsilon\right)D.
}
\tag{17}
\]

The same calculation works with \(p_L\) as the weighting measure.

So **no additional explicit factor of \(n\)** is needed here: the needed DPP total-variation input is precisely (5). In particular, dividing naïvely by the smallest configuration probability would introduce an artificial exponentially bad dependence that (17) avoids.

There are nevertheless separate infinite-volume obligations. The trace norm in \(D\) is unnormalized and may itself grow with volume. One still has to convert finite-volume estimates into translation-invariant/per-site control, realize approximants on an appropriate common random input, establish tightness/consistency, and identify limiting marginals. Existing invariant DPP coupling results illustrate that invariance is an additional structure, rather than a consequence of a finite \(L^1\) selector estimate. [Lyons-Thom](https://arxiv.org/abs/1402.0969) Thus (DF), even if proved, would not by itself settle a general invariant ordered-iid coupling construction.

For related coupling context, Møller–O'Reilly prove one-point-difference couplings between DPPs and reduced Palm processes; this is structurally related but does not provide the quantitative Lipschitz selector required here. [Moller-OReilly](https://arxiv.org/abs/1806.07347)

**Bottom line.** There is no demonstrated dimension-dependent obstruction in the divergence or DPP-probability data: (3), (5), (7), and (8) are dimension-free, and two substantial restricted classes admit explicit \(C=2\) selections. The unresolved load-bearing step is a dimension-free, globally compatible **positive capacitated selection/repair theorem** for the Boolean-cube transportation face. I do not have either that theorem or an explicit family forcing its failure, so the frozen primary target remains **INCOMPLETE**.