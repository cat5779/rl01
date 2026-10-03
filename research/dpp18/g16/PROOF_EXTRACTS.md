# Reusable proof extracts

These are compact proof skeletons intended to let a future solver resume without re-reading every predecessor PR. Full proofs and audits are in the source files listed in \`SOURCE_MAP.md\`.

## 1. Resolvent signed current

For an exact DPP atom,
\[
p_K(S)=(-1)^{|S^c|}\det(K-D_{S^c}).
\]
Differentiation in direction \(P\) gives
\[
b_{K,P}(S)
=
p_K(S)\operatorname{tr}
\bigl(P(K-D_{S^c})^{-1}\bigr).
\]

Because
\[
K-D_{S^c}
=
(K-\tfrac12I)+(\tfrac12I-D_{S^c}),
\]
the second summand has singular values \(1/2\) and
\[
\|K-\tfrac12I\|_{\rm op}\le\tfrac12-\varepsilon,
\]
hence
\[
\|(K-D_{S^c})^{-1}\|_{\rm op}\le\varepsilon^{-1}.
\]

Now define
\[
J(S,i)
=
-p_K(S)\operatorname{Re}
\bigl(P(K-D_{S^c})^{-1}\bigr)_{ii}.
\]
A determinant-lemma/rank-one inverse calculation on \(T=S\cup\{i\}\) gives an incoming representation
\[
J(S,i)
=
p_K(T)\operatorname{Re}
\bigl(v_i\overline{w_i^T}\bigr),
\qquad
w^T=(K-D_{T^c})^{-1}v.
\]
Summing outgoing and incoming expressions yields the divergence formula.

When \(KP=PK\), \(Kv=\lambda v\). From
\[
(K-D_{S^c})w^S=v
\]
and \(v^*K=\lambda v^*\), one gets the endpoint identities
\[
J_{\rm out}(S)
=
p_K(S)-\lambda b_{K,P}(S)=\mu_0(S),
\]
\[
J_{\rm in}(S)
=
p_K(S)+(1-\lambda)b_{K,P}(S)=\mu_1(S).
\]

For stability, split the difference of
\[
p_K(S)P(K-D_{S^c})^{-1}
\]
into probability, projector, and inverse terms. Use
\[
\sum_i|B_{ii}|\le\|B\|_1,
\]
the resolvent identity and
\[
\|p_K-p_L\|_1\le\frac2\varepsilon\|K-L\|_1
\]
to obtain
\[
\|J_{K,P}-J_{L,Q}\|_1
\le
\frac3{\varepsilon^2}\|K-L\|_1
+
\frac1\varepsilon\|P-Q\|_1.
\]

## 2. Why \(2J_+\) always contains a positive endpoint coupling

Work on fermionic Fock space
\[
\mathscr H=\bigoplus_{k=0}^n\wedge^k\mathbb C^E.
\]
Let \(C\) be exterior multiplication by \(v\),
\[
C^2=0,\qquad C^*C+CC^*=I,
\]
and
\[
U=C+C^*.
\]
Then \(U\) is a self-adjoint unitary.

Represent the DPP state by
\[
\rho=\det(I-K)\Gamma(K(I-K)^{-1}).
\]
Because \(P\) commutes with \(K\), conditioning the marked mode \(v\) to be absent gives a positive trace-one state \(\rho_0\), and the present state is
\[
\rho_1=U\rho_0U^*.
\]
Their configuration diagonals are \(\mu_0,\mu_1\).

Define the signed matrix
\[
q(S,T)
=
\operatorname{Re}
\left[
U_{T,S}(\rho_0U^*)_{S,T}
\right].
\]
Particle-number structure forces \(q\) onto upward one-point edges, and cofactor expansion identifies it with \(J\).

For arbitrary source/target families \(\mathcal A,\mathcal B\), let \(R\) project onto \(\mathcal A\) and
\[
Q=U^*(I-R_{\mathcal B})U.
\]
The projection identity
\[
RQ+QR-(R+Q-I)=(R+Q-I)^2\succeq0
\]
implies
\[
\mu_0(\mathcal A)-\mu_1(\mathcal B)
\le
2\sum_{S\in\mathcal A,\ T\notin\mathcal B}J(S,T)_+.
\]
These are exactly all max-flow cut inequalities for capacities \(2J_+\). Therefore the bipartite network admits a nonnegative coupling
\[
0\le f\le2J_+.
\]

## 3. Fixed-projector repair

Let \(P=vv^*\) be fixed and write \(H=v^\perp\). The endpoint coupling problem depends only on
\[
B=K|_H.
\]
Define on \(\mathscr F(H)\)
\[
\sigma_B
=
\det(I-B)\Gamma(B(I-B)^{-1}).
\]

Along
\[
B_t=B+t(B'-B),
\]
set
\[
M_t=[B_t(I-B_t)]^{-1/2}(B'-B)[B_t(I-B_t)]^{-1/2}.
\]
Differentiating second quantization gives
\[
\sigma_t^{-1/2}\dot\sigma_t\sigma_t^{-1/2}
=
d\Gamma(M_t)-\operatorname{tr}(B_tM_t)I.
\]
Subset-sum control of eigenvalues yields
\[
\left\|
\sigma_t^{-1/2}\dot\sigma_t\sigma_t^{-1/2}
\right\|_{\rm op}
\le
\frac{\|B-B'\|_1}{\varepsilon(1-\varepsilon)}
=:D.
\]
Hence
\[
e^{-D}\sigma_B\preceq\sigma_{B'}\preceq e^D\sigma_B.
\]

Put \(c=e^{-D}\) and
\[
\tau=\sigma_{B'}-c\sigma_B\succeq0.
\]
The residual positive state \(\tau\) has an upward one-point coupling \(h\) by a weighted Hall argument using the creation operator.

For any old coupling \(f\),
\[
g=cf+h
\]
has the new endpoint marginals. Since both \(f\) and \(h/(1-c)\) have total mass one,
\[
\|g-f\|_1
\le2(1-c)\le2D.
\]
This gives
\[
\|g-f\|_1
\le
\frac{2}{\varepsilon(1-\varepsilon)}
\|K-L\|_1.
\]

The proof crucially uses the same marked mode \(v\); it does not compare varying projectors.

## 4. Scalar-complement explicit selector

If
\[
K=a(I-P)+\lambda P,
\]
then the directional derivative in \(P\) is the same as at \(aI\), so define
\[
F(S,i)
=
P_{ii}a^{|S|}(1-a)^{n-1-|S|}.
\]
This is nonnegative and has total mass
\[
\sum_iP_{ii}=1.
\]
The outgoing law is \(p_{a(I-P)}\), giving the stronger endpoint capacity.

For two such pairs,
\[
\|F_{K,P}-F_{L,Q}\|_1
\le
\|P-Q\|_1+2(n-1)|a-c|.
\]
Use
\[
(n-1)a=\operatorname{tr}K-\operatorname{tr}(KP)
\]
to absorb the dimension factor:
\[
(n-1)|a-c|
\le
2\|K-L\|_1+\|P-Q\|_1.
\]
Thus
\[
\|F_{K,P}-F_{L,Q}\|_1
\le
4\|K-L\|_1+3\|P-Q\|_1.
\]

This calculation is a useful model for what a successful general proof must accomplish: an apparently dimension-dependent product-law term is canceled by a trace identity intrinsic to the commuting geometry.

## 5. Finite consistency implies a global selector

Assume a uniform constant \(C_\varepsilon\) works for every finite list.

For fixed \(E\), choose a countable dense set
\[
x_1,x_2,\ldots
\]
of commuting inputs. For every \(N\), choose feasible
\[
f_1^{(N)},\ldots,f_N^{(N)}
\]
satisfying all pairwise bounds.

The finite-dimensional flow simplex is compact. Take a diagonal subsequence so every fixed \(f_j^{(N)}\) converges. The limits satisfy all pairwise Lipschitz inequalities and are feasible because the fiber graph is closed.

The assignment on the dense set extends uniquely to a \(C_\varepsilon\)-Lipschitz map on the full fixed-\(E\) domain. It is automatically Borel.

Finally set
\[
\bar f(x)
=
\frac1{|\operatorname{Sym}(E)|}
\sum_{\sigma\in\operatorname{Sym}(E)}
\sigma^{-1}f(\sigma x).
\]
Convexity/covariance of the fiber preserves feasibility, and the same Lipschitz constant is retained. Thus \(\bar f\) is permutation-equivariant.

This argument explains why pairwise repair is not enough: the hypothesis must already produce mutually compatible choices on arbitrary finite lists.
