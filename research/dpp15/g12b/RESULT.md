PROVED

Fix a finite coordinate set \(E\), write \(n=|E|\), and let
\[
K=\operatorname{diag}(k_i)_{i\in E},
\qquad
\varepsilon\le k_i\le 1-\varepsilon.
\]
For every rank-one projector \(P\), define
\[
F_{K,P}(S,i)
=
P_{ii}\,p_{K_{E\setminus\{i\}}}(S),
\qquad i\notin S.
\tag{1}
\]
We prove that this is a Borel, coordinate-permutation-equivariant member of \(\mathcal F_E(K,P)\), and that
\[
\|F_{K,P}-F_{L,Q}\|_1
\le
2\bigl(\|K-L\|_1+\|P-Q\|_1\bigr).
\tag{2}
\]
Thus one may take the universal constant
\[
\boxed{C_\varepsilon=2.}
\]

## 1. Product form of the diagonal DPP

Because \(K\) is diagonal, its DPP consists of independent Bernoulli coordinates:
\[
p_K(S)
=
\prod_{j\in S}k_j
\prod_{j\notin S}(1-k_j).
\tag{3}
\]
For \(i\notin S\),
\[
p_{K_{E\setminus\{i\}}}(S)
=
\prod_{j\in S}k_j
\prod_{\substack{j\notin S\\j\ne i}}(1-k_j)
=
\frac{p_K(S)}{1-k_i}.
\tag{4}
\]
For \(i\in S\),
\[
p_{K_{E\setminus\{i\}}}(S\setminus\{i\})
=
\frac{p_K(S)}{k_i}.
\tag{5}
\]

## 2. Exact derivative at a diagonal kernel

For an arbitrary Hermitian DPP kernel \(A\), the exact atom probability has the determinantal expression
\[
p_A(S)
=
(-1)^{|S^c|}
\det\!\left(A-I_{S^c}\right),
\tag{6}
\]
where \(I_{S^c}\) is the coordinate projection onto \(S^c\).

Fix \(S\subseteq E\) and put
\[
D_S=K-I_{S^c}.
\]
Because \(K\) is diagonal,
\[
(D_S)_{ii}
=
\begin{cases}
k_i,&i\in S,\\
k_i-1,&i\notin S.
\end{cases}
\tag{7}
\]
The gap assumptions imply that \(D_S\) is invertible. Differentiating (6) in the direction \(P\) gives
\[
b_{K,P}(S)
=
p_K(S)\operatorname{tr}(D_S^{-1}P).
\tag{8}
\]
Since \(D_S^{-1}\) is diagonal,
\[
\operatorname{tr}(D_S^{-1}P)
=
\sum_{i\in S}\frac{P_{ii}}{k_i}
+
\sum_{i\notin S}\frac{P_{ii}}{k_i-1}.
\]
Therefore
\[
\boxed{
b_{K,P}(S)
=
p_K(S)
\left(
\sum_{i\in S}\frac{P_{ii}}{k_i}
-
\sum_{i\notin S}\frac{P_{ii}}{1-k_i}
\right).
}
\tag{9}
\]

This also explains exactly why the off-diagonal entries of \(P\) do not enter: the derivative is
\[
\operatorname{tr}(D_S^{-1}P),
\]
and \(D_S^{-1}\) is diagonal. Hence only \(P_{ii}\) appears. In particular, if
\[
P=vv^*,
\]
then \(P_{ii}=|v_i|^2\), so all phases of the coordinates of \(v\) disappear.

## 3. Nonnegativity

For a rank-one projector \(P=vv^*\),
\[
P_{ii}=|v_i|^2\ge0.
\tag{10}
\]
The marginal DPP law \(p_{K_{E\setminus\{i\}}}\) is nonnegative. Hence
\[
F_{K,P}(S,i)\ge0
\tag{11}
\]
for every upward edge \(S\to S\cup\{i\}\).

## 4. Exact divergence

At a vertex \(S\subseteq E\), the incoming flow is
\[
\begin{aligned}
F_{\mathrm{in}}(S)
&=
\sum_{i\in S}
F_{K,P}(S\setminus\{i\},i)\\
&=
\sum_{i\in S}
P_{ii}\,
p_{K_{E\setminus\{i\}}}(S\setminus\{i\})\\
&=
p_K(S)\sum_{i\in S}\frac{P_{ii}}{k_i},
\end{aligned}
\tag{12}
\]
where the last equality follows from (5).

Similarly, the outgoing flow is
\[
\begin{aligned}
F_{\mathrm{out}}(S)
&=
\sum_{i\notin S}
F_{K,P}(S,i)\\
&=
\sum_{i\notin S}
P_{ii}\,
p_{K_{E\setminus\{i\}}}(S)\\
&=
p_K(S)\sum_{i\notin S}\frac{P_{ii}}{1-k_i},
\end{aligned}
\tag{13}
\]
using (4).

Consequently,
\[
\begin{aligned}
\operatorname{div}F_{K,P}(S)
&=
F_{\mathrm{in}}(S)-F_{\mathrm{out}}(S)\\
&=
p_K(S)
\left(
\sum_{i\in S}\frac{P_{ii}}{k_i}
-
\sum_{i\notin S}\frac{P_{ii}}{1-k_i}
\right)\\
&=
b_{K,P}(S)
\end{aligned}
\tag{14}
\]
by (9).

Thus the divergence constraint holds exactly.

## 5. Total mass

For each fixed \(i\), \(p_{K_{E\setminus\{i\}}}\) is a probability law on \(2^{E\setminus\{i\}}\). Therefore
\[
\sum_{S\subseteq E\setminus\{i\}}
F_{K,P}(S,i)
=
P_{ii}.
\tag{15}
\]
Summing over \(i\),
\[
\begin{aligned}
\sum_{i\in E}
\sum_{S\subseteq E\setminus\{i\}}
F_{K,P}(S,i)
&=
\sum_{i\in E}P_{ii}\\
&=
\operatorname{tr}P\\
&=1.
\end{aligned}
\tag{16}
\]

## 6. Pointwise outgoing capacity

From (13),
\[
F_{\mathrm{out}}(S)
=
p_K(S)
\sum_{i\notin S}\frac{P_{ii}}{1-k_i}.
\tag{17}
\]
Since \(1-k_i\ge\varepsilon\),
\[
F_{\mathrm{out}}(S)
\le
\frac{p_K(S)}{\varepsilon}
\sum_{i\notin S}P_{ii}.
\tag{18}
\]
Because \(P\) is a rank-one projector,
\[
\sum_{i\notin S}P_{ii}\le\operatorname{tr}P=1.
\]
Hence
\[
F_{\mathrm{out}}(S)
\le
\frac1\varepsilon p_K(S)
\le
\frac2\varepsilon p_K(S).
\tag{19}
\]
In fact, the rule uses at most half of the prescribed capacity.

Equations (11), (14), (16), and (19) prove
\[
\boxed{F_{K,P}\in\mathcal F_E(K,P).}
\tag{20}
\]

## 7. Product-law stability

Let
\[
L=\operatorname{diag}(\ell_i)_{i\in E}
\]
be another diagonal kernel with the same spectral gap, and let \(Q\) be another rank-one projector.

We first prove the needed product-law estimate. For a finite index set \(J\), let
\[
\mu_{\mathbf k}
=
\bigotimes_{j\in J}\operatorname{Bernoulli}(k_j),
\qquad
\mu_{\boldsymbol\ell}
=
\bigotimes_{j\in J}\operatorname{Bernoulli}(\ell_j).
\]
Choose an ordering \(J=\{j_1,\ldots,j_r\}\) and introduce the intermediate product laws
\[
\mu^{(t)}
=
\left(
\bigotimes_{s\le t}\operatorname{Bernoulli}(\ell_{j_s})
\right)
\otimes
\left(
\bigotimes_{s>t}\operatorname{Bernoulli}(k_{j_s})
\right),
\qquad 0\le t\le r.
\]
Then
\[
\|\mu_{\mathbf k}-\mu_{\boldsymbol\ell}\|_1
\le
\sum_{t=1}^r
\|\mu^{(t)}-\mu^{(t-1)}\|_1.
\tag{21}
\]
The two laws in the \(t\)-th summand differ only in coordinate \(j_t\). Tensoring with a probability measure preserves the \(\ell^1\)-norm, while
\[
\left\|
\operatorname{Bernoulli}(k_{j_t})
-
\operatorname{Bernoulli}(\ell_{j_t})
\right\|_1
=
|k_{j_t}-\ell_{j_t}|
+
|(1-k_{j_t})-(1-\ell_{j_t})|
=
2|k_{j_t}-\ell_{j_t}|.
\]
Therefore
\[
\boxed{
\|\mu_{\mathbf k}-\mu_{\boldsymbol\ell}\|_1
\le
2\sum_{j\in J}|k_j-\ell_j|.
}
\tag{22}
\]

Applied on \(J=E\setminus\{i\}\), this yields
\[
\boxed{
\left\|
p_{K_{E\setminus\{i\}}}
-
p_{L_{E\setminus\{i\}}}
\right\|_1
\le
2\sum_{j\ne i}|k_j-\ell_j|.
}
\tag{23}
\]

## 8. Weighted dimension-free comparison

For every edge \((S,i)\),
\[
\begin{aligned}
&
\left|
P_{ii}p_{K_{E\setminus\{i\}}}(S)
-
Q_{ii}p_{L_{E\setminus\{i\}}}(S)
\right|\\
&\quad\le
|P_{ii}-Q_{ii}|\,
p_{K_{E\setminus\{i\}}}(S)
+
Q_{ii}
\left|
p_{K_{E\setminus\{i\}}}(S)
-
p_{L_{E\setminus\{i\}}}(S)
\right|.
\end{aligned}
\tag{24}
\]
Summing first over \(S\subseteq E\setminus\{i\}\) and then over \(i\), we obtain
\[
\begin{aligned}
\|F_{K,P}-F_{L,Q}\|_1
&\le
\sum_i|P_{ii}-Q_{ii}|\\
&\quad+
\sum_iQ_{ii}
\left\|
p_{K_{E\setminus\{i\}}}
-
p_{L_{E\setminus\{i\}}}
\right\|_1.
\end{aligned}
\tag{25}
\]

For the second term, (23) gives
\[
\begin{aligned}
&\sum_iQ_{ii}
\left\|
p_{K_{E\setminus\{i\}}}
-
p_{L_{E\setminus\{i\}}}
\right\|_1\\
&\quad\le
2\sum_iQ_{ii}\sum_{j\ne i}|k_j-\ell_j|\\
&\quad=
2\sum_j|k_j-\ell_j|
\sum_{i\ne j}Q_{ii}\\
&\quad=
2\sum_j|k_j-\ell_j|(1-Q_{jj})\\
&\quad\le
2\sum_j|k_j-\ell_j|.
\end{aligned}
\tag{26}
\]
This is the essential weighted estimate: the \(Q_{ii}\) weights sum to one, so no factor \(|E|\) occurs.

Since \(K-L\) is diagonal,
\[
\sum_j|k_j-\ell_j|=\|K-L\|_1.
\tag{27}
\]

For the projector term, put \(A=P-Q\). It is Hermitian. Let
\[
D=\operatorname{diag}(d_i),
\qquad
d_i=
\begin{cases}
\operatorname{sgn}(A_{ii}),&A_{ii}\ne0,\\
0,&A_{ii}=0.
\end{cases}
\]
Then \(\|D\|_{\mathrm{op}}\le1\), and trace-norm duality gives
\[
\sum_i|P_{ii}-Q_{ii}|
=
\operatorname{tr}(DA)
\le
\|D\|_{\mathrm{op}}\|A\|_1
\le
\|P-Q\|_1.
\tag{28}
\]

Combining (25)–(28),
\[
\boxed{
\|F_{K,P}-F_{L,Q}\|_1
\le
\|P-Q\|_1+2\|K-L\|_1.
}
\tag{29}
\]
In particular,
\[
\boxed{
\|F_{K,P}-F_{L,Q}\|_1
\le
2\bigl(\|K-L\|_1+\|P-Q\|_1\bigr).
}
\tag{30}
\]

This bound is independent of \(n\), the supports of \(P,Q\), and the coordinate phases.

## 9. Zero-coordinate degenerations and phases

If \(P=vv^*\) and \(v_i=0\), then
\[
P_{ii}=0,
\]
so every edge adding coordinate \(i\) receives zero flow:
\[
F_{K,P}(S,i)=0.
\]
No division by \(P_{ii}\), \(v_i\), or \(|v_i|\) occurs. Thus the construction extends continuously across zero-coordinate degenerations.

Replacing \(v\) by \(e^{\mathrm i\theta}v\), or changing individual coordinate phases while changing the off-diagonal entries of \(P\), does not affect the diagonal weights \(P_{ii}=|v_i|^2\). The derivative formula at a diagonal kernel and the selector both depend only on these diagonal weights.

## 10. Borel dependence

For fixed \(E\),
\[
F_{K,P}(S,i)
=
P_{ii}
\prod_{j\in S}k_j
\prod_{\substack{j\notin S\\j\ne i}}(1-k_j).
\tag{31}
\]
This is a polynomial in the diagonal entries of \(K\) and linear in the diagonal entries of \(P\). Hence
\[
(K,P)\longmapsto F_{K,P}
\]
is continuous, and therefore Borel.

## 11. Coordinate-permutation covariance

Let \(\sigma\) be a permutation of \(E\), with permutation matrix \(U_\sigma\). Define
\[
K^\sigma=U_\sigma K U_\sigma^*,
\qquad
P^\sigma=U_\sigma P U_\sigma^*.
\]
Then
\[
(P^\sigma)_{ii}
=
P_{\sigma^{-1}i,\sigma^{-1}i}.
\tag{32}
\]
The product DPP law transforms as
\[
p_{K^\sigma_{E\setminus\{i\}}}(S)
=
p_{K_{E\setminus\{\sigma^{-1}i\}}}
(\sigma^{-1}S).
\tag{33}
\]
Therefore
\[
\begin{aligned}
F_{K^\sigma,P^\sigma}(S,i)
&=
(P^\sigma)_{ii}
p_{K^\sigma_{E\setminus\{i\}}}(S)\\
&=
P_{\sigma^{-1}i,\sigma^{-1}i}
p_{K_{E\setminus\{\sigma^{-1}i\}}}
(\sigma^{-1}S)\\
&=
F_{K,P}(\sigma^{-1}S,\sigma^{-1}i).
\end{aligned}
\tag{34}
\]
This is exactly coordinate-permutation equivariance.

Hence the explicit rule \((\mathrm{DSEL})\) is a dimension-free Borel, coordinate-permutation-equivariant selector for all gapped diagonal kernels, with the universal Lipschitz constant
\[
\boxed{C_\varepsilon=2.}
\]

