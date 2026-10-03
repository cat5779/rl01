INCOMPLETE

I do not have a universal-selector obstruction or a proof of the full selector theorem. The strongest exact result I can establish is a structural anti-obstruction: every admissible DPP flow polytope contains a uniformly half-capacity-slack subpolytope that is affinely equivalent to a one-point cover-coupling polytope whose two marginals vary dimension-freely in \(\ell ^1\). Thus neither the stated pointwise capacities nor the global normalization can themselves generate the desired obstruction. I also give an exact length-\(m\) alternating-path example showing why this reduction alone cannot prove the theorem: arbitrary cover-coupling polytopes on the same cube graph have condition number \(m\). The remaining gap is precisely to prove that fixed-gap DPP marginals exclude this pathology, or to realize such a pathology inside the full DPP flow polytopes.

### 1. A uniformly half-slack flow always exists

Put
\[
p=p_K,\qquad b=b_{K,P},\qquad P=vv^*,
\]
and define
\[
\alpha=\operatorname{tr}\!\left(P(I-K)^{-1}\right)
      =v^*(I-K)^{-1}v,\qquad r=\alpha^{-1}.
\]
Since
\[
\epsilon I\le I-K\le (1-\epsilon)I,
\]
we have
\[
\frac1{1-\epsilon}\le\alpha\le\frac1\epsilon ,
\qquad
\epsilon\le r\le1-\epsilon. \tag{1}
\]

Moreover \(r\) is exactly the largest \(h\ge0\) for which \(K+hP\le I\). Indeed, with \(A=I-K\),
\[
A-hvv^*\ge0
\iff
I-hA^{-1/2}vv^*A^{-1/2}\ge0
\iff h\alpha\le1.
\]
Consequently
\[
M:=K+rP
\]
is again a positive contraction and \(I-M\) is singular.

For \(0\le h\le r\), let \(p_h=p_{K+hP}\). The DPP generating polynomial is
\[
G_{K+hP}(z)
 =\det\!\bigl(I-(K+hP)+(K+hP)Z\bigr),
\qquad Z=\operatorname{diag}(z_1,\ldots,z_n).
\]
The matrix inside the determinant is
\[
I-K+KZ+hP(Z-I),
\]
and \(P(Z-I)\) has rank at most one. Hence its determinant is affine in \(h\). Every coefficient is therefore affine in \(h\), so, exactly rather than infinitesimally,
\[
p_h(S)=p(S)+h\,b(S),\qquad 0\le h\le r. \tag{2}
\]
In particular, writing
\[
q:=p_M,
\]
we obtain
\[
q=p+r b. \tag{3}
\]

Use the standard rank-one one-point monotone DPP coupling underlying the audited nonemptiness fact. For \(h<r\), \(p\) and \(p_h\) admit a coupling supported on
\[
(S,S)\quad\text{and}\quad(S,S\cup\{i\}).
\]
Letting \(h\uparrow r\) and using compactness of the finite coupling simplex gives such a coupling \(\Gamma\) between \(p\) and \(q\).

Its total off-diagonal mass is determined exactly:
\[
\sum_{S,i\notin S}\Gamma(S,S\cup\{i\})
 =\mathbb E_q|X|-\mathbb E_p|X|
 =\operatorname{tr}(M-K)
 =r. \tag{4}
\]
Define
\[
F(S,i)=\frac1r\,\Gamma(S,S\cup\{i\})
       =\alpha\,\Gamma(S,S\cup\{i\}). \tag{5}
\]
The coupling balance equations and (3) give
\[
\begin{aligned}
&\sum_{i\in S}F(S\setminus\{i\},i)
 -\sum_{i\notin S}F(S,i)\\
&\hspace{35mm}
=\frac{q(S)-p(S)}r=b(S). \tag{6}
\end{aligned}
\]
Equation (4) gives
\[
\sum_{S,i\notin S}F(S,i)=1. \tag{7}
\]
Finally the row marginal of \(\Gamma\) is \(p\), hence
\[
\sum_{i\notin S}F(S,i)
\le\alpha p(S)
\le\frac1\epsilon p(S). \tag{8}
\]
The required capacity is \(2p(S)/\epsilon\). Thus this flow uses at most one half of the available capacity at every vertex.

So if
\[
\mathcal F^{\rm str}(K,P)
 :=
 \left\{F:\operatorname{div}F=b,\ F\ge0,\
    F_{\rm out}(S)\le\alpha p(S)\right\},
\]
then
\[
\varnothing\ne\mathcal F^{\rm str}(K,P)
\subseteq\mathcal F(K,P), \tag{9}
\]
and every member of the smaller set has a factor-two multiplicative capacity margin.

There is in fact an exact affine equivalence. If \(F\in\mathcal F^{\rm str}(K,P)\), define
\[
\Gamma_F(S,S\cup\{i\})=rF(S,i), \tag{10}
\]
and
\[
\Gamma_F(S,S)=p(S)-rF_{\rm out}(S). \tag{11}
\]
The latter is nonnegative because \(r\alpha=1\). Its row marginal is \(p\), while its column marginal is
\[
p(S)-rF_{\rm out}(S)+rF_{\rm in}(S)
 =p(S)+rb(S)=q(S). \tag{12}
\]
Conversely, (5) sends every diagonal-or-cover coupling of \(p,q\) to a member of \(\mathcal F^{\rm str}(K,P)\).

Hence
\[
\boxed{\;
\mathcal F^{\rm str}(K,P)
\ \longleftrightarrow\
\mathcal C(p_K,p_{K+rP}),
\;}
\tag{13}
\]
where \(\mathcal C\) denotes couplings supported only on equality or one-point upward covers.

### 2. The global normalization is not an independent constraint

For any flow with divergence \(b\),
\[
\begin{aligned}
\sum_S |S|\,b(S)
&=\sum_{S,i\notin S}
   F(S,i)\bigl(|S\cup\{i\}|-|S|\bigr)\\
&=\sum_{S,i\notin S}F(S,i). \tag{14}
\end{aligned}
\]
But
\[
\sum_S |S|p_{K+hP}(S)=\operatorname{tr}(K+hP),
\]
so differentiation at \(h=0\) yields
\[
\sum_S|S|b(S)=\operatorname{tr}P=1. \tag{15}
\]
Thus the total-flow normalization follows automatically from the divergence equation. It cannot be the source of a dimension-dependent instability.

### 3. The strong coupling marginals themselves vary dimension-freely

Consider
\[
z=(K,P),\qquad z'=(L,Q),
\]
and put
\[
\Delta_K=\|K-L\|_1,\qquad
\Delta_P=\|P-Q\|_1.
\]

The audited capacity-vector estimate immediately gives
\[
\|p_K-p_L\|_1\le2\Delta_K. \tag{16}
\]

The audited signed-repair estimate gives a signed edge field \(H\) with
\[
\operatorname{div}H=b_{K,P}-b_{L,Q},
\qquad
\|H\|_1\le\frac4\epsilon\Delta_K+\Delta_P.
\]
Since one edge contributes to two vertices,
\[
\|\operatorname{div}H\|_1\le2\|H\|_1,
\]
and therefore
\[
\|b_{K,P}-b_{L,Q}\|_1
\le\frac8\epsilon\Delta_K+2\Delta_P. \tag{17}
\]
Also, because every feasible flow has total mass one,
\[
\|b_{K,P}\|_1\le2. \tag{18}
\]

Write
\[
\alpha=\operatorname{tr}\bigl(P(I-K)^{-1}\bigr),
\qquad
\alpha'=\operatorname{tr}\bigl(Q(I-L)^{-1}\bigr).
\]
The resolvent identity gives
\[
(I-K)^{-1}-(I-L)^{-1}
 =(I-K)^{-1}(K-L)(I-L)^{-1}.
\]
Consequently
\[
|\alpha-\alpha'|
\le \frac1{\epsilon^2}\Delta_K+\frac1\epsilon\Delta_P. \tag{19}
\]
Since \(r=1/\alpha\), \(r'=1/\alpha'\), and
\(\alpha,\alpha'\ge1/(1-\epsilon)\),
\[
|r-r'|
\le(1-\epsilon)^2
 \left(
   \frac1{\epsilon^2}\Delta_K+\frac1\epsilon\Delta_P
 \right). \tag{20}
\]

Using the exact identity
\[
q=p+rb
\]
at both parameters,
\[
\begin{aligned}
\|q-q'\|_1
&\le\|p-p'\|_1
+r\,\|b-b'\|_1
+|r-r'|\,\|b'\|_1\\
&\le
\left[
2+\frac{8(1-\epsilon)}{\epsilon}
 +\frac{2(1-\epsilon)^2}{\epsilon^2}
\right]\Delta_K\\
&\quad+
\frac{2(1-\epsilon)}{\epsilon}\,\Delta_P. \tag{21}
\end{aligned}
\]
All constants are independent of \(n\).

Thus both marginals of the exact cover-coupling representation (13) are dimension-freely Lipschitz in the original parameter metric. The scaling factor \(\alpha\) is dimension-freely Lipschitz as well.

This eliminates two natural obstruction mechanisms: no parameter is forced near the stated upper-capacity boundary, and no large instability is hidden merely in the DPP marginals \(p,q\).

### 4. Nevertheless, sparse cover couplings have genuine \(m\)-fold conditioning in general

The preceding result does not imply a dimension-free Hausdorff estimate for the coupling fibers. There is an exact obstruction already in the abstract cube cover graph.

Let
\[
S_j=\{1,\ldots,j\},\qquad 0\le j\le m.
\]
In the bipartite graph whose left vertices are source subsets and whose right vertices are target subsets, consider the \(2m\)-edge path
\[
R_{S_0}
-C_{S_1}
-R_{S_1}
-C_{S_2}
-\cdots
-C_{S_m}
-R_{S_m}. \tag{22}
\]
For \(j=1,\ldots,m\), the edge
\[
u_j=(R_{S_{j-1}},C_{S_j})
\]
is a one-point cover edge, while
\[
d_j=(R_{S_j},C_{S_j})
\]
is diagonal.

Set
\[
a=\frac1{2m},\qquad 0<\delta<a.
\]
Define a coupling \(\Gamma^0\) by putting mass \(a\) on every \(u_j,d_j\), and zero elsewhere. Define \(\Gamma^1\) by
\[
\Gamma^1(u_j)=a+\delta,\qquad
\Gamma^1(d_j)=a-\delta. \tag{23}
\]
Both have total mass one.

For \(\Gamma^0\), the source marginal is
\[
\mu^0(S_0)=\mu^0(S_m)=a,\qquad
\mu^0(S_j)=2a\quad(1\le j<m),
\]
while the target marginal is
\[
\nu(S_j)=2a=\frac1m,\qquad1\le j\le m.
\]
For \(\Gamma^1\), every target marginal is unchanged because the two changes incident to \(C_{S_j}\) cancel. Every interior source marginal is also unchanged. Only the two endpoints change:
\[
\mu^1(S_0)=a+\delta,\qquad
\mu^1(S_m)=a-\delta. \tag{24}
\]
Hence
\[
\|\mu^1-\mu^0\|_1=2\delta,\qquad
\|\nu-\nu\|_1=0. \tag{25}
\]

Because all other source and target marginals vanish, every permitted edge outside the displayed path is forced to carry zero. The path is a tree, and its marginals determine its edge masses recursively; therefore the coupling polytope for each pair of marginals is a singleton, namely \(\Gamma^0\) or \(\Gamma^1\).

But
\[
\|\Gamma^1-\Gamma^0\|_1=2m\delta. \tag{26}
\]
Thus
\[
\frac{
\inf\{\|\Gamma-\Gamma'\|_1:
 \Gamma\in\mathcal C(\mu^0,\nu),
 \Gamma'\in\mathcal C(\mu^1,\nu)\}}
{\|\mu^0-\mu^1\|_1+\|\nu-\nu\|_1}
=m. \tag{27}
\]
The off-diagonal parts alone differ by
\[
m\delta, \tag{28}
\]
so the same linear amplification persists for the scaled flow part.

Taking, for example, \(\delta=1/(4m)\) makes the marginal perturbation \(1/(2m)\), while the full coupling distance is \(1/2\).

Therefore **there is no dimension-free Hausdorff or Lipschitz-selection theorem for arbitrary cover-coupling marginals even on the Boolean-cube diagonal-plus-cover graph.** Any proof of the frozen theorem must use genuinely DPP-specific information beyond marginal \(\ell^1\)-stability.

### 5. Exact unresolved gap

The path construction (22)–(28) is not a counterexample to the frozen theorem.

First, its source marginals have many zero atoms. A fixed-gap DPP \(p_K\) has strictly positive atoms, and I have not produced fixed-gap kernels \(K_m,L_m\) and rank-one directions whose exact pairs
\[
\bigl(p_K,p_{K+rP}\bigr)
\]
force an alternating path face with the amplification in (27).

Second, even an instability of the strong subpolytopes
\(\mathcal F^{\rm str}(K,P)\) would not by itself be a universal-selector obstruction, because the frozen selector is allowed to use the larger set
\[
\mathcal F(K,P),
\]
whose capacity is twice as large. A valid DISPROVED certificate must lower-bound the distance between the **entire** two flow polytopes, or furnish a finite branching/cycle argument that traps every possible simultaneous selection. I do not have that step.

Conversely, the exact reduction identifies a sufficient route to PROVED. If one can choose, for all DPP pairs in (13), cover couplings \(\Gamma_z\) with a dimension-free Lipschitz bound, then
\[
F_z=\alpha_z\,(\Gamma_z)_{\rm cover}
\]
belongs to \(\mathcal F(K,P)\), and (19), \(1/\epsilon\ge\alpha_z\), and
\(\|(\Gamma_z)_{\rm cover}\|_1=r_z\le1-\epsilon\)
immediately transfer the coupling Lipschitz bound to the required flow bound. Borelness is preserved. Permutation equivariance causes no additional loss: any Borel Lipschitz coupling selector can be symmetrized by
\[
\overline\Gamma_z
=\frac1{n!}\sum_{\pi\in S_n}
 \pi^{-1}\Gamma_{\pi z},
\]
which remains a coupling of the same two marginals, is permutation-equivariant, and has no larger Lipschitz constant.

Thus the unresolved mathematical issue is sharply localized:

\[
\boxed{\text{Does fixed-gap DPP structure prevent the alternating-path
ill-conditioning of cover couplings, or can that pathology be realized
in a way that separates the full flow polytopes?}}
\]

The half-capacity theorem proves that upper-capacity saturation and global normalization cannot supply the obstruction. The explicit path family proves that marginal stability alone cannot supply the positive theorem. I have not closed the remaining DPP-specific gap, so neither PROVED nor DISPROVED is justified.
