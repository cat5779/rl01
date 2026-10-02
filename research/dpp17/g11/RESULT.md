INCOMPLETE

I have not established (COM), and I have not obtained a selector-independent counterexample. There is, however, a positive capacitated repair result on the whole commuting class: an explicit, dimension-free Lipschitz **signed** endpoint coupling admits a nonnegative endpoint coupling bounded by twice its positive part. There is also a dimension-free positive repair estimate when the projector is fixed.

Neither result supplies the required globally consistent Lipschitz selection. Below are complete proofs, together with an actual dimension-free selector on a proper full-support subclass and a precise formulation of the remaining gap.

## 1. Endpoint coupling reduction

Fix a commuting pair \((K,P)\), write \(P=vv^*\) with \(\|v\|=1\), and set
\[
\lambda=\operatorname{tr}(KP),\qquad A=K-\lambda P.
\]
Then
\[
Kv=\lambda v,\qquad Av=0,\qquad
\varepsilon\le\lambda\le1-\varepsilon.
\]
Define the two endpoint laws
\[
\mu_0=p_A,\qquad \mu_1=p_{A+P}.
\]
Rank-one affinity gives
\[
\boxed{
p_K=(1-\lambda)\mu_0+\lambda\mu_1,\qquad
b_{K,P}=\mu_1-\mu_0.
}
\tag{1}
\]

Let \(\mathcal G(K,P)\) consist of nonnegative upward edge flows satisfying the stronger marginal equalities
\[
\sum_{i\notin S}f(S,i)=\mu_0(S),
\qquad
\sum_{i\in T}f(T\setminus\{i\},i)=\mu_1(T).
\tag{2}
\]
Every such flow has the required divergence and total mass one. Moreover,
\[
\boxed{
f_{\rm out}(S)=\mu_0(S)
\le\frac{p_K(S)}{1-\lambda}
\le\frac1\varepsilon p_K(S).
}
\tag{3}
\]
Thus \(\mathcal G(K,P)\subseteq\mathcal F_E(K,P)\), with a stronger capacity bound.

A uniformly Lipschitz selector in these endpoint fibers would suffice for (COM). This is only a sufficient reduction: a selector for the original fibers need not satisfy (2).

## 2. An explicit signed endpoint coupling with a uniform modulus

For \(S\subseteq E\), let \(D_{\bar S}\) be the diagonal projection onto \(E\setminus S\), and put
\[
M_S(K)=K-D_{\bar S}.
\]
The spectral gap implies
\[
\boxed{\|M_S(K)^{-1}\|_{\rm op}\le\varepsilon^{-1}.}
\tag{4}
\]
Indeed,
\[
M_S(K)
=(K-\tfrac12I)+(\tfrac12I-D_{\bar S}),
\]
where the second summand has every singular value \(1/2\), and the first has operator norm at most \(1/2-\varepsilon\).

Define
\[
\boxed{
J_{K,P}(S,i)
=-p_K(S)\operatorname{Re}\bigl(PM_S(K)^{-1}\bigr)_{ii},
\qquad i\notin S.
}
\tag{5}
\]
This formula uses \(P\), not a choice of its phase. It is coordinate-permutation covariant.

### Divergence and endpoint marginals

The exact-pattern determinant identity is
\[
p_K(S)=(-1)^{|\bar S|}\det M_S(K).
\]
Consequently,
\[
b_{K,P}(S)
=p_K(S)\operatorname{tr}\bigl(PM_S(K)^{-1}\bigr).
\tag{6}
\]

Write \(w^S=M_S(K)^{-1}v\). If \(T=S\cup\{i\}\), the determinant lemma and the rank-one inverse formula give
\[
J_{K,P}(S,i)
=p_K(T)\operatorname{Re}\bigl(v_i\overline{w_i^T}\bigr).
\tag{7}
\]
Combining the incoming expression (7) with the outgoing expression (5) proves
\[
\operatorname{div}J_{K,P}=b_{K,P}.
\]

Commutation gives more. From
\[
Kw^S-D_{\bar S}w^S=v
\]
and \(v^*K=\lambda v^*\), we obtain
\[
\sum_{i\notin S}\overline v_iw_i^S
=\lambda v^*w^S-1.
\]
Hence
\[
\begin{aligned}
J_{\rm out}(S)
&=p_K(S)-\lambda b_{K,P}(S)=\mu_0(S),\\
J_{\rm in}(S)
&=p_K(S)+(1-\lambda)b_{K,P}(S)=\mu_1(S).
\end{aligned}
\tag{8}
\]
Thus \(J\) is an exact signed endpoint coupling, of total mass one.

### Absolute bounds

Cauchy–Schwarz and (4) give
\[
\boxed{
\sum_{i\notin S}|J(S,i)|
+\sum_{i\in S}|J(S\setminus\{i\},i)|
\le\frac1\varepsilon p_K(S).
}
\tag{9}
\]
In particular,
\[
\|J_{K,P}\|_1\le\varepsilon^{-1}.
\tag{10}
\]

For a self-contained, nonoptimal stability constant, first note that the signed-flow construction and its divergence identity are valid algebraically without commutation. They imply
\[
\|b_{H,R}\|_1\le 2/\varepsilon
\]
for every \(\varepsilon\)-gapped \(H\) and rank-one projector \(R\). Spectrally decomposing a Hermitian direction and integrating along the gapped segment between \(K,L\) therefore yields
\[
\|p_K-p_L\|_1\le\frac2\varepsilon\|K-L\|_1.
\tag{11}
\]

For any matrix \(B\),
\[
\sum_i|B_{ii}|\le\|B\|_1.
\]
Using this inequality, (4), the resolvent identity, and (11) in (5) gives
\[
\boxed{
\|J_{K,P}-J_{L,Q}\|_1
\le
\frac3{\varepsilon^2}\|K-L\|_1
+\frac1\varepsilon\|P-Q\|_1.
}
\tag{12}
\]
Indeed, changing the probability factor costs at most
\(\varepsilon^{-1}\|p_K-p_L\|_1\); changing \(P\) costs at most
\(\varepsilon^{-1}\|P-Q\|_1\); and changing the inverse costs at most
\(\varepsilon^{-2}\|K-L\|_1\).

These estimates do not involve the least configuration probability.

## 3. Positive-part capacity theorem

The signed coupling in (5) can have negative edges. Nevertheless:

> **Positive-part capacity lemma.** For every commuting pair, there exists
> \[
> f\in\mathcal G(K,P)
> \quad\text{such that}\quad
> \boxed{0\le f(S,i)\le2J_{K,P}(S,i)_+.}
> \tag{13}
> \]

The proof uses a projection cut inequality also appearing in capacitated quantum-flow feasibility arguments; the particular positive-current capacity in (13) follows by retaining the signed real part before taking its positive part.

### 3.1 A finite-dimensional operator representation

Let
\[
\mathscr H=\bigoplus_{k=0}^{n}\bigwedge^k\mathbb C^E
\]
with its configuration basis \(\{|S\rangle:S\subseteq E\}\). Let \(C\) be exterior multiplication by \(v\). Then
\[
C^2=0,\qquad C^*C+CC^*=I.
\]
Thus
\[
U=C+C^*
\]
is a self-adjoint unitary. Put \(N=CC^*\), the projection onto states in which the marked mode \(v\) is occupied.

For a positive matrix \(L\), write
\[
\Gamma(L)=\bigoplus_{k=0}^{n}\bigwedge^k L.
\]
Set
\[
L=K(I-K)^{-1},\qquad
\rho=\det(I-K)\Gamma(L).
\]
In the configuration basis,
\[
\rho_{S,T}
=
\begin{cases}
\det(I-K)\det L_{S,T},&|S|=|T|,\\
0,&|S|\ne|T|.
\end{cases}
\]
In an eigenbasis of \(K\), this is the density matrix of independently occupied modes with their respective eigenvalue probabilities. In particular, \(\rho\) is positive of trace one, and its configuration diagonal is \(p_K\).

Because \(P\) commutes with \(K\), define
\[
\rho_0=\frac{(I-N)\rho}{1-\lambda},
\qquad
\rho_1=C\rho_0C^*=U\rho_0U^*.
\tag{14}
\]
These are positive trace-one matrices. Their configuration diagonals are respectively \(\mu_0,\mu_1\): in the eigenmode description, the marked mode is fixed absent or present, while all other occupation probabilities remain unchanged.

Define a signed matrix, with source \(S\) and target \(T\), by
\[
q(S,T)=
\operatorname{Re}\!\left[
U_{T,S}(\rho_0U^*)_{S,T}
\right].
\tag{15}
\]
Its source and target marginals are \(\mu_0,\mu_1\).

Moreover, \(\rho_0C=0\), so \(\rho_0U=\rho_0C^*\). Since \(\rho_0\) preserves particle number, (15) vanishes unless \(T=S\cup\{i\}\). It is therefore supported on upward cube edges.

For \(T=S\cup\{i\}\), expansion by cofactors gives
\[
q(S,T)
=
\frac{p_K(T)}{1-\lambda}
\operatorname{Re}\!\left[
v_i\overline{(L_T^{-1}v_T)_i}
\right].
\tag{16}
\]
To identify this with (5), observe that
\[
M_T(K)=(I-K)(LD_T-D_{\bar T}).
\]
Since \((I-K)^{-1}v=v/(1-\lambda)\), solving \(M_T(K)w=v\) and restricting its rows to \(T\) gives
\[
w_T=\frac1{1-\lambda}L_T^{-1}v_T.
\]
Equations (7) and (16) consequently show that
\[
q(S,S\cup\{i\})=J_{K,P}(S,i).
\tag{17}
\]

### 3.2 Every required capacity cut holds

Take arbitrary source and target families \(\mathcal A,\mathcal B\). Let \(R\) be the coordinate projection onto \(\mathcal A\), and set
\[
Q=U^*(I-R_{\mathcal B})U.
\]
Both \(R,Q\) are orthogonal projections. The identity
\[
RQ+QR-(R+Q-I)=(R+Q-I)^2\succeq0
\]
gives
\[
\begin{aligned}
\mu_0(\mathcal A)-\mu_1(\mathcal B)
&=\operatorname{tr}\rho_0(R+Q-I)\\
&\le2\operatorname{Re}\operatorname{tr}(\rho_0RQ)\\
&=2\sum_{\substack{S\in\mathcal A\\T\notin\mathcal B}}q(S,T)\\
&\le2\sum_{\substack{S\in\mathcal A,\ T\notin\mathcal B\\
T=S\cup\{i\}}}J(S,i)_+.
\end{aligned}
\tag{18}
\]

Consider the finite bipartite network with source supplies \(\mu_0(S)\), target demands \(\mu_1(T)\), and edge capacities \(2J(S,i)_+\). Equation (18) is exactly its family of max-flow cut inequalities. A flow of total mass one therefore exists, proving (13).

### 3.3 What this proves—and what it does not

Every flow supplied by (13) satisfies the original requirements, including the stronger capacity (3). It also obeys the pointwise repair bound
\[
|f(S,i)-J(S,i)|\le |J(S,i)|.
\tag{19}
\]
The capacity vector itself has uniformly bounded mass:
\[
\sum_{S,i}2J(S,i)_+
=1+\|J\|_1
\le1+\varepsilon^{-1},
\tag{20}
\]
and a dimension-free modulus:
\[
\boxed{
\|2(J_{K,P})_+-2(J_{L,Q})_+\|_1
\le
\frac6{\varepsilon^2}\|K-L\|_1
+\frac2\varepsilon\|P-Q\|_1.
}
\tag{21}
\]

One can consequently define a single positive selector on the entire commuting class by minimizing the Euclidean norm over
\[
\mathcal H(K,P)=
\left\{
f\in\mathcal G(K,P):0\le f\le2(J_{K,P})_+
\right\}.
\tag{22}
\]
This fiber is nonempty and compact, and the minimizer is unique. For fixed \(E\), its inequalities have fixed normals and continuous right-hand sides. The fixed-normal least-norm selection lemma gives continuity; uniqueness and invariance of the objective give coordinate-permutation covariance. Thus this construction is Borel and includes zero-coordinate and eigenvalue degenerations.

**The unresolved point is its dimension-free Lipschitz modulus.** Bounds (12) and (21) control the data, not a dimension-independent active-set constant. No such constant for the selector in (22) is established here.

## 4. Dimension-free positive repair when the projector is fixed

There is a stronger stability statement for the endpoint fibers when the same \(P\) is used at both inputs.

> **Fixed-projector repair lemma.** Suppose \(KP=PK\) and \(LP=PL\). For every \(f\in\mathcal G(K,P)\), there exists \(g\in\mathcal G(L,P)\) with
> \[
> \boxed{
> \|f-g\|_1
> \le
> \frac{2}{\varepsilon(1-\varepsilon)}\|K-L\|_1.
> }
> \tag{23}
> \]
> The same assertion holds with the two inputs interchanged.

This is a statement about the smaller endpoint fibers. It does not contradict the audited failure of a dimension-free Hausdorff modulus for the full original fibers.

### 4.1 Multiplicative comparison of background states

Fix \(v\), put \(H=v^\perp\), and let
\[
B=K|_H,\qquad B'=L|_H.
\]
The endpoint fibers depend on these background kernels and on \(P\), but not on the marked eigenvalues.

On \(\mathscr F(H)=\bigoplus_k\wedge^kH\), define
\[
\sigma_B=\det(I-B)\Gamma\!\left(B(I-B)^{-1}\right).
\]
Let \(B_t=B+t(B'-B)\), \(\sigma_t=\sigma_{B_t}\), and
\[
M_t=[B_t(I-B_t)]^{-1/2}(B'-B)[B_t(I-B_t)]^{-1/2}.
\]
Differentiating exterior powers gives
\[
\sigma_t^{-1/2}\dot\sigma_t\sigma_t^{-1/2}
=
d\Gamma(M_t)-\operatorname{tr}(B_tM_t)I.
\tag{24}
\]
Here \(d\Gamma(M)\) acts on \(\wedge^kH\) by the sum of \(M\) acting in the \(k\) tensor positions.

For clarity, (24) follows by differentiating the scalar determinant factor and using
\[
\Gamma(L_t)^{-1/2}\frac d{dt}\Gamma(L_t)\Gamma(L_t)^{-1/2}
=d\Gamma(L_t^{-1/2}\dot L_tL_t^{-1/2}),
\]
where \(L_t=B_t(I-B_t)^{-1}\). The matrix inside \(d\Gamma\) is \(M_t\), and the logarithmic derivative of the scalar factor is
\(-\operatorname{tr}(B_tM_t)\).

The eigenvalues of \(d\Gamma(M_t)\) are subset sums of the eigenvalues of \(M_t\). Also, because \(0\preceq B_t\preceq I\), the number \(\operatorname{tr}(B_tM_t)\) lies between the sum of the negative eigenvalues of \(M_t\) and the sum of its positive eigenvalues. Therefore
\[
\left\|
\sigma_t^{-1/2}\dot\sigma_t\sigma_t^{-1/2}
\right\|_{\rm op}
\le\|M_t\|_1
\le D,
\]
where
\[
D=\frac{\|B-B'\|_1}{\varepsilon(1-\varepsilon)}.
\]
Equivalently,
\[
-D\sigma_t\preceq\dot\sigma_t\preceq D\sigma_t.
\]
Multiplying by the appropriate scalar exponentials and integrating in Loewner order yields
\[
\boxed{
e^{-D}\sigma_B\preceq\sigma_{B'}\preceq e^D\sigma_B.
}
\tag{25}
\]
Only the one-particle spectral gap enters this bound.

### 4.2 Positive residual states admit one-point couplings

The following fact applies beyond Gaussian states. Let \(\tau\ge0\) be a number-preserving operator supported on the marked-empty subspace. Define
\[
\alpha(S)=\langle S|\tau|S\rangle,\qquad
\beta(T)=\langle T|C\tau C^*|T\rangle.
\]
Then \(\alpha,\beta\) admit an upward one-point coupling of total mass \(\operatorname{tr}\tau\).

To prove this, work separately on each particle-number sector. For a family \(\mathcal A\) of \(k\)-sets, let \(N(\mathcal A)\) be its neighbors under the nonzero creation edges of \(C\). Their coordinate projections satisfy
\[
(I-R_{N(\mathcal A)})CR_{\mathcal A}=0.
\]
For every marked-empty vector \(\psi\), \(C\) is an isometry, and hence
\[
\begin{aligned}
\|(I-R_{N(\mathcal A)})C\psi\|
&=\|(I-R_{N(\mathcal A)})C(I-R_{\mathcal A})\psi\|\\
&\le\|(I-R_{\mathcal A})\psi\|.
\end{aligned}
\]
Subtracting squared norms from \(\|\psi\|^2=\|C\psi\|^2\) gives
\[
\|R_{N(\mathcal A)}C\psi\|^2
\ge\|R_{\mathcal A}\psi\|^2.
\]
Averaging against \(\tau\) proves
\[
\beta(N(\mathcal A))\ge\alpha(\mathcal A).
\]
These are the weighted Hall inequalities, so a one-point coupling exists.

### 4.3 Repairing an arbitrary old coupling

Set \(c=e^{-D}\). By (25),
\[
\tau=\sigma_{B'}-c\sigma_B\succeq0,\qquad
\operatorname{tr}\tau=1-c.
\]
Choose a one-point coupling \(h\) for the residual state \(\tau\), as just proved. Given any \(f\in\mathcal G(K,P)\), define
\[
g=cf+h.
\]
Its endpoint marginals are precisely those for \(B'\), so
\(g\in\mathcal G(L,P)\). Furthermore,
\[
\|g-f\|_1
\le(1-c)\|f\|_1+\|h\|_1
=2(1-e^{-D})
\le2D.
\]
Since \(\|B-B'\|_1\le\|K-L\|_1\), this proves (23).

As a consequence, every single affine, fixed-\(P\) background segment admits a Lipschitz selection with this dimension-free constant. One obtains it by successive repairs on finer meshes, followed by a uniformly convergent subsequence in the finite-dimensional unit simplex. Closedness of the fiber graph gives feasibility of the limit.

This pathwise conclusion does **not** make selections on different segments consistent. Nor does (23) compare different projectors.

## 5. A complete selector on the scalar-complement subclass

There is a genuine dimension-free selector on the proper subclass
\[
K=a(I-P)+\lambda P,
\qquad a,\lambda\in[\varepsilon,1-\varepsilon].
\tag{26}
\]
These kernels may be non-diagonal, and \(P\) may have full support.

Define
\[
\boxed{
F_{K,P}(S,i)
=
P_{ii}\,a^{|S|}(1-a)^{n-1-|S|},
\qquad i\notin S.
}
\tag{27}
\]
Rank-one affinity along the line \(aI+tP\) shows
\[
b_{K,P}=b_{aI,P}.
\]
At the scalar kernel, direct differentiation gives the divergence of (27). The flow is nonnegative, and each direction \(i\) has total mass \(P_{ii}\); hence total mass is one.

Its outgoing mass is the lower endpoint law:
\[
F_{\rm out}(S)=p_{a(I-P)}(S).
\]
Therefore (3) supplies the stronger capacity \(p_K(S)/\varepsilon\).

For two pairs of the form (26), with scalar-complement parameters \(a,c\), a product Bernoulli coupling gives
\[
\|F_{K,P}-F_{L,Q}\|_1
\le\|P-Q\|_1+2(n-1)|a-c|.
\tag{28}
\]
For \(n\ge2\),
\[
(n-1)a=\operatorname{tr}K-\operatorname{tr}(KP),
\]
so
\[
(n-1)|a-c|
\le2\|K-L\|_1+\|P-Q\|_1.
\]
Consequently,
\[
\boxed{
\|F_{K,P}-F_{L,Q}\|_1
\le4\|K-L\|_1+3\|P-Q\|_1.
}
\tag{29}
\]
For \(n=1\), the sole edge has mass one.

The formulas recover \(a\) continuously from \((K,P)\), remain valid when \(a=\lambda\), use no eigenvector choice, and commute with every coordinate permutation. Thus they give a Borel, permutation-equivariant selector with constant \(4\) on (26), including all support degenerations and simultaneous variation of both inputs.

This is a proper restricted result: in (26), the restriction of \(K\) to \(v^\perp\) is scalar. A general commuting pair has no such restriction.

## 6. Exact remaining gap

A precise equivalent formulation of (COM) is the following finite-consistency assertion.

There must exist \(C_\varepsilon\), independent of \(E\), such that for **every finite list** of commuting inputs
\[
x_1,\ldots,x_m,\qquad x_a=(K_a,P_a),
\]
there are flows \(f_a\in\mathcal F_E(x_a)\) satisfying simultaneously
\[
\boxed{
\|f_a-f_b\|_1
\le C_\varepsilon
\bigl(\|K_a-K_b\|_1+\|P_a-P_b\|_1\bigr)
\quad\text{for every }a,b.
}
\tag{30}
\]

Necessity is immediate. Conversely, for fixed \(E\), apply (30) to successively longer initial segments of a countable dense set of commuting inputs. Compactness of the fibers and a diagonal subsequence produce compatible values on the whole dense set. The Lipschitz bound extends them uniquely to the entire domain. Feasibility passes to the limit because the fiber graph is closed.

The extension is Lipschitz and therefore Borel. Averaging it over coordinate permutations,
\[
\overline f(x)=
\frac1{|\operatorname{Sym}(E)|}
\sum_{\sigma\in\operatorname{Sym}(E)}
\sigma^{-1}f(\sigma x),
\]
preserves feasibility and the same Lipschitz constant, and enforces exact permutation covariance. This proves the equivalence.

The positive-part capacity theorem establishes nonempty, explicitly dominated positive fibers whose data are uniformly Lipschitz. The fixed-projector repair lemma establishes dimension-free pairwise repair in a smaller family of fibers. **Neither establishes (30) for arbitrary commuting inputs with varying projectors.**

No family violating (30) is established here either. In particular, negative entries of the explicit signed current, or instability of a particular optimizer, are not selector-independent counterexamples. The full commuting-class theorem remains unresolved in this argument.


