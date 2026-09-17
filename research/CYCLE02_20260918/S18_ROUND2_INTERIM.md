# S18 round 2 interim derivation

Status: AUTHOR_SUBMISSION_PENDING_INDEPENDENT_REVIEW. Complete visible message recovered; attachment bodies for the new round-2 certificate are not recovered. This earlier message is followed by the stronger finite-certificate summary in S18_ROUND2_LATEST.md.

---

# PRO02 Round 2 — research result reached

I did **not** obtain the requested complete benchmark curvature certificate. In particular, I have not proved the benchmark sufficient inequality negative, nor replaced it by another fully proved all-volume certificate. The main result remains **INCOMPLETE**.

The work did, however, produce an exact new representation of the unresolved signed matrix term as a discrete score-Jacobian/Bochner form, prove that representation without localization or asymptotics, and prove its positivity in the complete two-site case. It also isolates two substantially sharper sufficient statements for the benchmark. Neither has yet been proved in arbitrary volume.

No concrete defect was found in the Round 1 exact-potential, genuine-reveal, or posterior-storage derivations. Those remain submissions rather than independently certified inputs.

The preserved Round 1 artifacts are:

- :chatgpt-content-reference{index="2"}
- :chatgpt-content-reference{index="3"}
- :chatgpt-content-reference{index="4"}

I was not able to package a new `ROUND2_RESULT.md` before the execution window ended. The complete mathematical result reached in this round follows.

---

# ROUND2_RESULT — The reveal-Jacobian form of the remaining signed term

## 1. Status

**PROVED:** The unsigned matrix \(T=M-N\) left unresolved in old SA02 Section 10 has an exact probabilistic representation

\[
T_{ij}
=
\mathbb E\!\left[
  \bigl(Z_i-\mathbb E[Z_i\mid Y_{-j}]\bigr)
  \bigl(Z_j-\mathbb E[Z_j\mid Y_{-i}]\bigr)
\right].
\]

Equivalently,

\[
T_{ij}
=
\mathbb E\frac{|G_{ij}|^4}{G_{ii}G_{jj}}.
\]

Thus \(T\) is a discrete transposed-Jacobian, or Bochner, form of the full diagonal score vector. This identifies precisely what must be positive and why ordinary Fisher-information positivity does not settle it.

**PROVED:** For every strict two-site DPP,

\[
T\succeq
\operatorname{diag}
\left(
\frac1{K_{11}(1-K_{11})},
\frac1{K_{22}(1-K_{22})}
\right)
\succeq4I.
\]

The proof uses orthogonal score projection and does not require the old all-direction Bellman constant.

**PROVED:** At half filling, the finite sine DPP has product Bernoulli marginals on each parity sublattice. Hence, writing \(t=a-1/40\),

\[
H_n(t)
=
n\,h\!\left(\frac12+t\right)
-
I_t(Y_{\rm even};Y_{\rm odd}),
\]

and therefore

\[
H_n''(1/40)
=
-4n-I_t''(0).
\]

This turns a complete curvature certificate into the exact finite-volume statement \(I_t''(0)\ge0\). It contains every pair, every endpoint, and every actual word weight; no spatial localization is involved.

**INCOMPLETE:** I did not prove either

\[
\mathbf 1^TT\mathbf 1\ge0
\]

or

\[
I_t''(0)\ge0
\]

for arbitrary finite sine windows.

**INCOMPLETE:** Consequently, no all-\(n\) benchmark certificate and no entropy-rate concavity theorem is claimed.

---

## 2. Setup

Let \(K\) be a strict finite DPP kernel, \(0<K<I\). For an actual word \(y\in\{0,1\}^V\), set

\[
A_y=K-\operatorname{diag}(1-y),
\qquad
G_y=A_y^{-1}.
\]

The atom probability is

\[
p_y=(-1)^{|V|-|y|}\det A_y.
\]

Allow independent perturbations of the diagonal entries of \(K\). The score for the \(i\)-th diagonal parameter is

\[
Z_i(y)
=
\partial_{a_i}\log p_y
=
(G_y)_{ii}.
\]

Let

\[
P_jF=\mathbb E[F\mid Y_{V\setminus\{j\}}],
\qquad
D_jF=(I-P_j)F.
\]

Thus \(D_jF\) is the martingale difference associated with hiding or revealing coordinate \(j\).

---

## 3. Exact leave-one-out score identity

### Claim 3.1 — score projection formula: **PROVED**

For every \(i,j\),

\[
\boxed{
P_jZ_i
=
G_{ii}-\frac{|G_{ij}|^2}{G_{jj}},
\qquad
D_jZ_i
=
\frac{|G_{ij}|^2}{G_{jj}}.
}
\tag{3.1}
\]

For \(i=j\), the first expression is zero.

### Proof

Marginalizing coordinate \(j\) gives the DPP with principal kernel \(K_{-j}\). Differentiating the marginal atom probability gives

\[
P_jZ_i
=
\partial_{a_i}\log p_{-j}(Y_{-j})
\]

for \(i\ne j\). The marginal score is the \(ii\)-entry of

\[
(A_y)_{-j,-j}^{-1}.
\]

The principal-inverse identity gives

\[
(A_y)_{-j,-j}^{-1}
=
(G_y)_{-j,-j}
-
\frac{(G_y)_{-j,j}(G_y)_{j,-j}}{(G_y)_{jj}}.
\]

Taking the \(ii\)-entry proves the first formula for \(i\ne j\).

For \(i=j\), the marginal law of \(Y_{-j}\) is independent of \(a_j\), so \(P_jZ_j=0\). The displayed expression agrees because

\[
G_{jj}-\frac{|G_{jj}|^2}{G_{jj}}=0,
\]

as \(G_{jj}\) is real and nonzero on every strict atom.

Subtracting from \(Z_i=G_{ii}\) proves the second identity. ∎

This identity is stronger than a directional Hessian calculation: it is an exact finite conditional projection formula on every atom.

---

## 4. The reveal-Jacobian matrix

Define

\[
\boxed{
\Theta_{ij}
=
\mathbb E[(D_jZ_i)(D_iZ_j)].
}
\tag{4.1}
\]

Using (3.1),

\[
\boxed{
\Theta_{ij}
=
\mathbb E\frac{|G_{ij}|^4}{G_{ii}G_{jj}}.
}
\tag{4.2}
\]

In particular,

\[
\Theta_{ii}=\mathbb E Z_i^2.
\]

Let \(M\) be the full diagonal Fisher matrix,

\[
M_{ij}=\mathbb E Z_iZ_j.
\]

For \(i\ne j\), condition on the actual outside word \(Y_{V\setminus\{i,j\}}\), and denote the conditional table by

\[
(A,B,C,D)=(p_{00},p_{10},p_{01},p_{11}).
\]

Put

\[
q=B+D,\qquad r=C+D,\qquad s=BC-AD\ge0.
\]

Define the matrix \(N\) by \(N_{ii}=0\) and

\[
N_{ij}
=
\mathbb E_{\rm outside}
\frac{s}{q(1-q)r(1-r)}.
\tag{4.3}
\]

### Theorem 4.1 — exact identification of the old matrix gap: **PROVED**

\[
\boxed{\Theta=M-N.}
\tag{4.4}
\]

### Proof

For \(i\ne j\), \(P_jZ_i\) is the score of the conditional marginal law of \(Y_i\), given the pair outside and \(Y_i\) itself. Thus

\[
P_jZ_i=\frac{Y_i-q}{q(1-q)}.
\]

Similarly,

\[
P_iZ_j=\frac{Y_j-r}{r(1-r)}.
\]

Their conditional product has expectation

\[
\frac{\operatorname{Cov}(Y_i,Y_j\mid\text{outside})}
     {q(1-q)r(1-r)}
=
-\frac{s}{q(1-q)r(1-r)}.
\tag{4.5}
\]

Moreover, \(P_iZ_j\) is measurable with respect to \(Y_{-i}\), while

\[
\mathbb E[Z_i\mid Y_{-i}]=0.
\]

Consequently,

\[
\mathbb E[Z_iP_iZ_j]=0,
\qquad
\mathbb E[P_jZ_iZ_j]=0.
\]

Expanding the two martingale differences gives

\[
\begin{aligned}
\Theta_{ij}
&=
\mathbb E[(Z_i-P_jZ_i)(Z_j-P_iZ_j)]\\
&=
M_{ij}+\mathbb E[(P_jZ_i)(P_iZ_j)]\\
&=
M_{ij}-N_{ij}.
\end{aligned}
\]

On the diagonal, \(\Theta_{ii}=\mathbb EZ_i^2=M_{ii}\) and \(N_{ii}=0\). ∎

This is not merely a change of notation. It shows that the unresolved matrix is the contraction

\[
\Theta_{ij}=\langle D_jZ_i,D_iZ_j\rangle_{L^2(p)}
\]

of the discrete Jacobian \((D_jZ_i)_{ij}\). It also exposes the obstruction: the two factors in an off-diagonal entry use different conditional projections.

---

## 5. Interface with the complete entropy Hessian

The exact logarithmic remainder identity gives

\[
\boxed{
H_V''
=
-\frac12\operatorname{tr}M
-\frac12\mathbf1^T\Theta\mathbf1
-2\sum_{i<j}\mathbb E r_{ij},
}
\tag{5.1}
\]

where every \(r_{ij}\ge0\).

Therefore:

### Corollary 5.1 — exact sufficient sign condition: **PROVED**

If

\[
\mathbf1^T\Theta\mathbf1\ge0,
\tag{5.2}
\]

then

\[
H_V''\le-\frac12\operatorname{tr}M.
\tag{5.3}
\]

At the benchmark, every one-site marginal is Bernoulli \(1/2\). Writing

\[
u_i=\mathbb P(Y_i=1\mid Y_{-i}),
\]

one has

\[
M_{ii}
=
\mathbb E\frac1{u_i(1-u_i)}
\ge
\frac1{(\mathbb Eu_i)(1-\mathbb Eu_i)}
=4.
\tag{5.4}
\]

Thus (5.2) would imply the explicit finite-volume certificate

\[
\boxed{H_n''(1/40)\le-2n.}
\tag{5.5}
\]

This route would require no pair-cut tail, observation-domain estimate, or endpoint replacement. All those terms are absent because (5.1) is the exact finite-volume Hessian with its actual word weights.

The stronger statement \(\Theta\succeq0\) is sufficient but is not required.

---

## 6. Complete two-site positivity

For two sites, define the one-coordinate score projections

\[
\bar Z_i=\mathbb E[Z_i\mid Y_i],
\qquad
R_i=Z_i-\bar Z_i.
\]

Because there are only two coordinates,

\[
D_2Z_1=R_1,
\qquad
D_1Z_2=R_2.
\]

Orthogonal projection gives

\[
\mathbb E Z_i^2
=
\mathbb E R_i^2+\mathbb E\bar Z_i^2.
\tag{6.1}
\]

Moreover,

\[
\mathbb E\bar Z_i^2
=
\frac1{K_{ii}(1-K_{ii})}.
\tag{6.2}
\]

### Theorem 6.1 — two-site reveal-Jacobian positivity: **PROVED**

For every strict two-site DPP,

\[
\boxed{
\Theta
=
\operatorname{Cov}
\begin{pmatrix}R_1\\R_2\end{pmatrix}
+
\operatorname{diag}
\left(
\frac1{K_{11}(1-K_{11})},
\frac1{K_{22}(1-K_{22})}
\right).
}
\tag{6.3}
\]

Hence

\[
\boxed{
\Theta\succeq
\operatorname{diag}
\left(
\frac1{K_{11}(1-K_{11})},
\frac1{K_{22}(1-K_{22})}
\right)
\succeq4I.
}
\tag{6.4}
\]

### Proof

The off-diagonal entry of \(\Theta\) is

\[
\Theta_{12}=\mathbb E R_1R_2.
\]

Its diagonal entries satisfy

\[
\Theta_{ii}=\mathbb EZ_i^2
=\mathbb ER_i^2+\mathbb E\bar Z_i^2.
\]

This is exactly (6.3). The first matrix on the right is a covariance matrix and therefore positive semidefinite. Formula (6.2) and \(x(1-x)\le1/4\) give the final bound. ∎

### Why this proof does not immediately extend

For \(n\ge3\), the off-diagonal entry is

\[
\Theta_{ij}
=
\mathbb E
\bigl(Z_i-\mathbb E[Z_i\mid Y_{-j}]\bigr)
\bigl(Z_j-\mathbb E[Z_j\mid Y_{-i}]\bigr).
\]

The residual assigned to \(Z_i\) depends on its partner \(j\). There is no single residual vector \(R\) whose covariance matrix equals \(\Theta\). This is the smallest precise obstruction to extending the two-site proof.

This mechanism is an orthogonal-projection/ANOVA transfer: Fisher scores are projected onto leave-one-coordinate sigma-fields, and the unresolved term is the transpose contraction of the resulting discrete Jacobian. Rank-one DPP entropy concavity only uses the negative Fisher term because each atom is affine in the rank-one parameter; it does not control this multi-coordinate transpose contraction. citeturn752649search3

---

## 7. Half-filling parity reduction

For the sine kernel at density \(1/2\),

\[
Q_{ij}
=
\frac{\sin(\pi(i-j)/2)}{\pi(i-j)},
\qquad
Q_{ii}=\frac12.
\]

If \(i\ne j\) have the same lattice parity, then \(i-j\) is even and

\[
Q_{ij}=0.
\]

At the benchmark,

\[
a+\frac c2
=
\frac1{40}+\frac{19}{40}
=
\frac12.
\]

Partition a finite volume into even and odd sites, \(V=E\sqcup O\). For \(t=a-1/40\),

\[
K_V(t)
=
\begin{pmatrix}
(\frac12+t)I_E & C\\
C^* & (\frac12+t)I_O
\end{pmatrix}.
\tag{7.1}
\]

A diagonal DPP kernel is a product Bernoulli law. Hence both parity marginals are product Bernoulli\((1/2+t)\), and

\[
H(Y_E)=|E|h(1/2+t),
\qquad
H(Y_O)=|O|h(1/2+t).
\]

The entropy identity \(H(E,O)=H(E)+H(O)-I(E;O)\) gives

\[
\boxed{
H_n(t)
=
n h(1/2+t)-I_t(Y_E;Y_O).
}
\tag{7.2}
\]

Since \(h''(1/2)=-4\),

\[
\boxed{
H_n''(1/40)
=
-4n-I_t''(0).
}
\tag{7.3}
\]

### Corollary 7.1 — stronger exact sufficient condition: **PROVED**

If

\[
I_t''(0)\ge0,
\tag{7.4}
\]

then

\[
\boxed{H_n''(1/40)\le-4n.}
\tag{7.5}
\]

Again, this is a complete finite-volume implication: it does not discard long pairs, change observation domains, or replace endpoint blocks.

The missing statement is the local convexity of the parity mutual information under the common diagonal translation. Ordinary nonnegativity of mutual information, complement symmetry, and separate one-coordinate convexity do not themselves imply (7.4).

---

## 8. Computations actually performed

The calculations below were floating-point diagnostics. They were not converted into interval certificates and are not used as proofs.

Exact configuration enumeration with the true DPP atom weights gave:

\[
\begin{array}{c|c}
n&H_n''/n\\ \hline
2&-4.7727335\\
3&-5.9692923\\
4&-6.8559376\\
5&-7.6458939\\
6&-8.2609202\\
8&-9.2421388\\
10&-9.96331\text{ approximately}
\end{array}
\]

The observed parity mutual-information curvature

\[
I_t''(0)=-H_n''-4n
\]

was positive in all these cases.

For actual local windows, the computed exact-potential values included

\[
\mathcal W_{4,2}\approx-10.1330043151,
\]

as in Round 1, and

\[
\begin{aligned}
\mathcal W_{6,0}&\approx-8.2609202065,\\
\mathcal W_{6,2}&\approx-10.9456933983,\\
\mathcal W_{8,2}&\approx-11.4897822530.
\end{aligned}
\]

The expectation became more negative as the observation window increased in every enumerated case, but no theorem of observation monotonicity was proved.

Random strict DPP tests did not find a negative eigenvalue of \(\Theta\). Random tests also supported

\[
\mathbb E\Phi_V(G_V)
\ge
\sum_\alpha
\mathbb E\Phi_{V_\alpha}(G_{V_\alpha})
\]

for partitions \(V=\bigsqcup_\alpha V_\alpha\). These remain conjectural.

Pointwise positivity is unavailable: direct sine enumeration first produced negative individual values of \(\Phi(G_y)\) at \(n=12\). Thus any proof must use the actual word average or a conditional projection identity rather than a wordwise sign.

Relevant diagnostic programs are preserved here:

- :chatgpt-content-reference{index="5"}
- :chatgpt-content-reference{index="6"}
- :chatgpt-content-reference{index="7"}
- :chatgpt-content-reference{index="8"}
- :chatgpt-content-reference{index="9"}
- :chatgpt-content-reference{index="10"}
- :chatgpt-content-reference{index="11"}
- :chatgpt-content-reference{index="12"}

These scripts use actual atom probabilities rather than uniform word averages, but they use ordinary floating-point linear algebra.

---

## 9. Exact improvement and exact limitation

The Round 1 route required proving

\[
\mathcal W_{m,L}
+
\frac{C_*\mathsf h_m}{m}
+
\frac{50251200}{2197}
\left(\frac1m+\frac1L\right)<0.
\]

No such window has been certified.

The Round 2 identities give two alternative, localization-free targets:

\[
\boxed{\mathbf1^T\Theta\mathbf1\ge0}
\tag{9.1}
\]

would yield

\[
H_n''(1/40)\le-2n,
\]

while

\[
\boxed{I_t''(0)\ge0}
\tag{9.2}
\]

would yield

\[
H_n''(1/40)\le-4n.
\]

These implications are proved and contain no \(C_*\), \(A_{\rm ro}\), \(m\), \(L\), pair-cut, observation, or finite-endpoint errors.

What is **not** proved is the sign in either (9.1) or (9.2). Therefore the removal of the localization constants is a conditional reduction, not a completed certificate.

The smallest remaining obstruction can be stated without hiding a finite-window expectation:

> For the finite half-filled sine DPP, prove that the transpose contraction of the leave-one-out score Jacobian,
> \[
> \sum_{i,j}
> \mathbb E[(D_jZ_i)(D_iZ_j)],
> \]
> is nonnegative; equivalently, prove local convexity at zero of the mutual information between the two parity sublattices under common diagonal translation.

The two-site orthogonal-projection proof shows why this is plausible and exactly why it ceases to be automatic when three or more coordinates are present.

---

## 10. Reviewer statement

**Main target: INCOMPLETE.** No benchmark all-volume or entropy-rate certificate is claimed.

**New proved lemma:** For every strict finite DPP, the old signed matrix \(T=M-N\) is exactly the leave-one-out score-Jacobian form

\[
T_{ij}
=
\mathbb E[(D_jZ_i)(D_iZ_j)]
=
\mathbb E\frac{|G_{ij}|^4}{G_{ii}G_{jj}}.
\]

It is positive semidefinite, in fact at least \(4I\), for every strict two-site DPP.

**New exact benchmark reductions:** At the half-filled sine benchmark, either \(\mathbf1^TT\mathbf1\ge0\) or parity-mutual-information convexity would immediately give a complete finite-volume negative-curvature margin, with no localization errors.

**Unproved point requiring fresh review:** neither sign has been established beyond two sites; all larger-window support presently consists of floating-point diagnostics rather than certified computation.
