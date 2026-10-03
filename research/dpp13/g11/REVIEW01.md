PASS

# Independent adversarial audit of source.md

## Verdict and exact scope

The proof correctly establishes the **restricted** theorem in task.md. For every finite \(E\), every
\(\varepsilon I\preceq K\preceq(1-\varepsilon)I\), and every rank-one projector \(P\) with
\(|\operatorname{supp}P|\le2\), it constructs a nonnegative unit upward flow with the exact required
divergence and the stronger capacity \(F_{\rm out}(S)\le p_K(S)/\varepsilon\). The construction is
Borel, permutation-equivariant, and satisfies

\[
\|F_{K,P}-F_{L,Q}\|_1
\le C_\varepsilon^{(2)}
(\|K-L\|_1+\|P-Q\|_1),
\]

with the dimension-free constant

\[
C_\varepsilon^{(2)}
=\max\{18,A_\varepsilon\},\qquad
A_\varepsilon=2+(6+4/\varepsilon)d_\varepsilon,\qquad
d_\varepsilon=1+\left(\frac{1-2\varepsilon}{2\varepsilon}\right)^2.
\]

I independently rederived the load-bearing identities below and found no counterexample, missing
support-transition case, or hidden dependence on \(n\).

**The unrestricted theorem for arbitrary full-support rank-one directions remains unproved.**
The overlap argument here is intrinsically a support-at-most-two argument and supplies no control for
two general overlapping supports.

## 1. Exact conditioning

For a kernel \(H\) on a coordinate set \(D\), inclusion-exclusion gives

\[
p_H(A)=(-1)^{|D\setminus A|}\det(H-D_{D\setminus A}).
\tag{A1}
\]

Let \(E=J\sqcup O\), \(T\subseteq O\), and

\[
B_T(K)=K_O-D_{O\setminus T},\qquad
M_T(K)=K_J-K_{JO}B_T(K)^{-1}K_{OJ}.
\]

Because

\[
B_T(K)=(K_O-\tfrac12I)+(\tfrac12I-D_{O\setminus T}),
\]

the second summand has least singular value \(1/2\) and the first has operator norm at most
\(1/2-\varepsilon\). Thus

\[
s_{\min}(B_T(K))\ge\varepsilon,\qquad
\|B_T(K)^{-1}\|_{\rm op}\le\varepsilon^{-1}.
\tag{A2}
\]

In particular \(B_T(K)\) is invertible. Applying the block determinant formula to (A1), with the
parity signs split between \(J\setminus A\) and \(O\setminus T\), yields exactly

\[
p_K(T\cup A)=q_K(T)p_{M_T(K)}(A),\qquad q_K(T)=p_{K_O}(T).
\tag{A3}
\]

No least-configuration-probability denominator appears. The source's positivity sentence should be
read as: (A2) makes the signed determinant nonzero, and (A1) identifies it with a nonnegative
probability, hence \(q_K(T)>0\).

The conditional kernel retains the spectral gap. Conditioning a coordinate in a current block kernel

\[
H=\begin{pmatrix}a&c^*\\c&D\end{pmatrix}
\]

gives \(D-cc^*/a\) after inclusion and \(D+cc^*/(1-a)\) after exclusion. For the former,

\[
x^*(D-cc^*/a)x=\min_z (z,x)^*H(z,x)\ge\varepsilon\|x\|^2,
\]

while its upper bound follows from \(D-cc^*/a\preceq D\preceq(1-\varepsilon)I\).
For exclusion, the lower bound is immediate, and applying the same inclusion argument to \(I-H\)
proves the upper bound. Iteration gives the displayed \(M_T(K)\), hence

\[
\varepsilon I_J\preceq M_T(K)\preceq(1-\varepsilon)I_J.
\tag{A4}
\]

If \(P\) is supported on \(J\), its outside rows and columns vanish, so

\[
M_T(K+hP)=M_T(K)+hP_J.
\]

Differentiating (A3) therefore gives the exact load-bearing identity

\[
b_{K,P}(T\cup A)=q_K(T)b_{M_T(K),P_J}(A).
\tag{A5}
\]

## 2. Conditional-kernel stability is dimension-free

Put \(K_s=K+s(L-K)\), \(H=L-K\), and

\[
W_s=[\,I_J,-K_{s,JO}B_T(K_s)^{-1}\,].
\]

Direct differentiation of the Schur complement gives

\[
\frac d{ds}M_T(K_s)=W_sHW_s^*.
\tag{A6}
\]

The off-diagonal compression bound and (A2) imply

\[
\|K_{s,JO}B_T(K_s)^{-1}\|_{\rm op}
\le\frac{1/2-\varepsilon}{\varepsilon},
\qquad
\|W_s\|_{\rm op}^2\le d_\varepsilon.
\]

By the ideal property of trace norm, integration of (A6) gives

\[
\|M_T(K)-M_T(L)\|_1\le d_\varepsilon\|K-L\|_1.
\tag{A7}
\]

Averaging (A7) against the probability vector \(q_K\) retains the same bound. There is no factor
\(2^{|O|}\); this probability average is exactly where a possible dimension loss is avoided.

## 3. Two-site divergence, mass, feasibility, and nonnegativity

Write

\[
M=\begin{pmatrix}a&z\\\bar z&d\end{pmatrix},\qquad
R=\begin{pmatrix}u&w\\\bar w&t\end{pmatrix},\qquad u+t=1,
\]

and

\[
\gamma=ud+ta-2\operatorname{Re}(\bar zw)
=\operatorname{tr}(R\operatorname{adj}M).
\]

Since the two eigenvalues of \(\operatorname{adj}M\) are those of \(M\) in reverse order,

\[
\varepsilon\le\gamma\le1-\varepsilon.
\tag{A8}
\]

Rank-one affinity and \(\det R=0\) give

\[
b_{M,R}=(\gamma-1,u-\gamma,t-\gamma,\gamma).
\tag{A9}
\]

For

\[
\begin{aligned}
f(\varnothing,1)&=u-x,&f(\varnothing,2)&=t-\gamma+x,\\
f(\{1\},2)&=\gamma-x,&f(\{2\},1)&=x,
\end{aligned}
\]

direct recomputation gives

\[
\begin{aligned}
\operatorname{div}f(\varnothing)&=-(u-x)-(t-\gamma+x)=\gamma-1,\\
\operatorname{div}f(\{1\})&=(u-x)-(\gamma-x)=u-\gamma,\\
\operatorname{div}f(\{2\})&=(t-\gamma+x)-x=t-\gamma,\\
\operatorname{div}f(\{1,2\})&=(\gamma-x)+x=\gamma,
\end{aligned}
\]

and the total edge mass is \(u+t=1\). Thus both the divergence and normalization are exact for every
scalar \(x\).

Let \(c=1/\varepsilon\). Since

\[
0\preceq M+\varepsilon R\preceq I,
\]

nonnegativity of its exact-pattern probabilities and rank-one affinity imply

\[
1-\gamma\le cp_0,\qquad
\gamma-u\le cp_1,\qquad
\gamma-t\le cp_2.
\tag{A10}
\]

If \(\lambda,\mu\in[\varepsilon,1-\varepsilon]\) are the eigenvalues of \(M\), then

\[
p_1+p_2=\lambda(1-\mu)+\mu(1-\lambda)\ge\varepsilon,
\]

so \(\gamma\le1\le c(p_1+p_2)\). These inequalities prove every needed pairwise comparison in

\[
\ell=\max\{0,\gamma-t,\gamma-cp_1\}
\le
U=\min\{u,\gamma,cp_2\}.
\tag{A11}
\]

Indeed:

- \(0\) is at most each upper candidate;
- \(\gamma-t\le u\) follows from \(\gamma\le u+t=1\), while
  \(\gamma-t\le\gamma\) and \(\gamma-t\le cp_2\) follow from \(t\ge0\) and (A10);
- \(\gamma-cp_1\le u\) follows from \(\gamma-u\le cp_1\),
  \(\gamma-cp_1\le\gamma\) from \(p_1\ge0\), and
  \(\gamma-cp_1\le cp_2\) from \(\gamma\le c(p_1+p_2)\).

For \(x\in[\ell,U]\), (A11) is exactly the collection of the four edge nonnegativity constraints and
the two singleton capacity constraints. The empty-state outgoing mass is \(1-\gamma\le cp_0\), and the
full state has no outgoing edge. Therefore

\[
f_{\rm out}(A)\le p_M(A)/\varepsilon
\tag{A12}
\]

for every local state.

The reference value

\[
x_0=ud-\operatorname{Re}(\bar zw)
=\tfrac12(\gamma+ud-ta)
\]

is clipped to \([\ell,U]\). Under exchange of the two coordinates,

\[
x_0'=\gamma-x_0,\qquad
\ell'=\gamma-U,\qquad
U'=\gamma-\ell,
\]

so the clipped value satisfies \(x'=\gamma-x\). The local selector is genuinely permutation-covariant.

For \(R=E_1\), one has \(\gamma=d\), and the lower candidate \(\gamma-t=d\) and upper candidate
\(\gamma=d\) force \(x=d\). For \(R=E_2\), \(0\le x\le u=0\) forces \(x=0\). Hence the local formula
is compatible with both coordinate degenerations.

## 4. Independent Lipschitz constant check

For two two-dimensional rank-one projectors \(R,Q\), the matrix \(R-Q\) is traceless Hermitian, so

\[
|\Delta u|=|\Delta t|\le\tfrac12\delta_R,
\qquad \delta_R=\|R-Q\|_1.
\tag{A13}
\]

The \(2\times2\) adjugate is linear, and trace-norm duality gives

\[
|\Delta\gamma|\le\delta_M+\delta_R,
\qquad \delta_M=\|M-N\|_1.
\tag{A14}
\]

The difference of two probability vectors has total mass zero. Combining this fact with the audited
bound \(\|p_M-p_N\|_1\le2\delta_M\) gives
\(|\Delta p_1|,|\Delta p_2|\le\delta_M\).
Also,

\[
ud-ta-u'd'+t'a'
=u(d-d')-t(a-a')+(u-u')(d'+a'),
\]

whose modulus is at most \(\delta_M+\delta_R\). Thus
\(|\Delta x_0|\le\delta_M+\delta_R\).
Max, min, and scalar interval clipping are \(1\)-Lipschitz in the sup norm of their inputs, yielding

\[
|\Delta x|
\le(1+1/\varepsilon)\delta_M+\tfrac32\delta_R.
\tag{A15}
\]

Summing the four edge differences gives

\[
\begin{aligned}
\|f_{M,R}-f_{N,Q}\|_1
&\le2|\Delta u|+2|\Delta\gamma|+4|\Delta x|\\
&\le(6+4/\varepsilon)\delta_M+9\delta_R.
\end{aligned}
\tag{A16}
\]

The coefficients in the source are therefore valid.

## 5. Lift, capacity, and coordinate compatibility

For a two-set \(J\supseteq\operatorname{supp}(P)\), define

\[
F^J_{K,P}(T\cup A,i)
=q_K(T)f_{M_T(K),P_J}(A,i)
\]

on directions \(i\in J\setminus A\), and put zero mass on directions outside \(J\). Nonnegativity is
immediate. Identity (A5) proves the required divergence configuration by configuration. Local unit
mass gives global mass \(\sum_Tq_K(T)=1\). Equations (A3) and (A12) give

\[
F^J_{K,P,\rm out}(T\cup A)
\le q_K(T)p_{M_T(K)}(A)/\varepsilon
=p_K(T\cup A)/\varepsilon.
\tag{A17}
\]

This is stronger than the required \(2p_K/\varepsilon\) bound.

For \(P=E_i\), cancellation of edges not changing membership of \(j\) yields, for any nonnegative flow
with the required divergence,

\[
\sum_{S:j\notin S}F(S,j)=P_{jj}.
\tag{A18}
\]

Thus every direction \(j\ne i\) has zero total mass and hence every such edge is zero. The divergence at
each \(S\not\ni i\) then uniquely fixes

\[
F_K^{(i)}(S,i)=p_{K_{E\setminus\{i\}}}(S).
\tag{A19}
\]

Consequently every auxiliary two-set lift containing \(i\) agrees with (A19); there is no hidden choice
of auxiliary coordinate. Its kernel Lipschitz constant \(2\) follows from the audited DPP law estimate
after trace-norm compression.

When \(P,Q\) are supported in one common two-set \(J\), splitting the product difference in the lift,
using unit local mass, (A7), and (A16), gives

\[
\|F_{K,P}-F_{L,Q}\|_1
\le A_\varepsilon\|K-L\|_1+9\|P-Q\|_1.
\tag{A20}
\]

The outside-pattern term is a probability-law distance and the conditional-kernel term is a probability
average, so no dimension-dependent number of summands survives.

## 6. Exhaustive audit of changes of support

The allowed support pairs split into exactly three cases.

1. **Union of size at most two.** Use one common two-set in (A20). This includes a genuine
   two-coordinate direction degenerating to a coordinate projector. The case \(n=1\) uses (A19)
   directly.

2. **Disjoint supports.** The representing vectors are orthogonal, so \(PQ=0\) and
   \(\|P-Q\|_1=2\). Two nonnegative flows of unit mass are at \(\ell^1\)-distance at most \(2\).
   Hence the desired estimate holds, even without the kernel term.

3. **Two genuine two-coordinate supports meeting only at \(i\).** Let
   \(\alpha=1-P_{ii}\) and \(\beta=1-Q_{ii}\). The only common contribution to the inner product of
   representing unit vectors is at coordinate \(i\), so

   \[
   \|P-Q\|_1=2\sqrt{\alpha+\beta-\alpha\beta},
   \quad
   \|P-E_i\|_1=2\sqrt\alpha,
   \quad
   \|Q-E_i\|_1=2\sqrt\beta.
   \]

   Since both \(\alpha\) and \(\beta\) are at most
   \(D=\alpha+\beta-\alpha\beta\),

   \[
   \|P-E_i\|_1+\|Q-E_i\|_1
   \le4\sqrt D
   =2\|P-Q\|_1.
\tag{A21}
   \]

   Compare each selector to the unique \(E_i\)-selector at its own kernel via (A20), and compare the
   two coordinate selectors via (A19). This gives

   \[
   \|F_{K,P}-F_{L,Q}\|_1
   \le2\|K-L\|_1+18\|P-Q\|_1.
\tag{A22}
   \]

These cases exhaust all nonempty supports of size at most two. Equations (A20) and (A22), together with
the disjoint-support estimate, prove (DF2) with
\(\max\{18,A_\varepsilon\}\).

## 7. Borelness and permutation covariance

For each fixed finite \(E\), the proved global Lipschitz estimate holds across all restricted support
strata, including their coordinate-projector boundaries. The selector is therefore continuous on the
restricted domain, hence Borel.

Principal blocks, diagonal masks, inversion of the uniformly invertible \(B_T\), exact probabilities,
and the local clipping rule all commute with coordinate relabeling. The local interchange calculation
above handles the only ordering choice on a two-set, and (A19) is manifestly covariant. Hence the
global selector is permutation-equivariant. Every formula uses \(P\) directly, so no phase choice for a
representing vector is present.

## 8. Final checklist

- exact two-site divergence and total mass: **verified**;
- nonnegativity and the stronger \(p_M/\varepsilon\) local capacity: **verified**;
- local Lipschitz estimate: **verified**;
- dimension-free conditional averaging: **verified**;
- conditional trace-norm stability: **verified**;
- compatibility with every auxiliary two-set at coordinate directions: **verified**;
- Borelness and permutation covariance across strata: **verified**;
- disjoint, one-coordinate-overlap, and degeneration comparisons: **verified**.

Two editorial artifacts do not affect this verdict: the inline content-reference markers are not usable
citations, and the final repository-access sentence is extraneous. The mathematical argument is
self-contained relative to the audited inputs.

Restricted support-\(\le2\) theorem: **proved**.

Unrestricted arbitrary-support theorem: **still unproved and not addressed by this proof**.

