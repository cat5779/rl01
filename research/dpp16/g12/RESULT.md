PROVED

Let \(\Pi_\alpha\) denote the coordinate projection onto \(B_\alpha\), and write
\[
P_\alpha:=\Pi_\alpha P\Pi_\alpha,\qquad
w_\alpha=\operatorname{tr}P_\alpha.
\]
Since \(P=vv^*\),
\[
P_\alpha=v_{B_\alpha}v_{B_\alpha}^*.
\]
Thus, when \(w_\alpha>0\),
\[
R_\alpha=\frac{P_\alpha}{w_\alpha}
\]
is a rank-one projector on \(B_\alpha\); when \(w_\alpha=0\), \(P_\alpha=0\).

For \(U\subseteq E\), write
\[
S_\alpha=U\cap B_\alpha,\qquad
T_\alpha=U\setminus B_\alpha.
\]

We prove that
\[
F^{\mathrm{blk}}_{K,P}(T_\alpha\cup S_\alpha,i)
=
w_\alpha\,p_{K_{E\setminus B_\alpha}}(T_\alpha)\,
G_{K_\alpha,R_\alpha}(S_\alpha,i),
\qquad i\in B_\alpha\setminus S_\alpha,
\tag{1}
\]
with the \(\alpha\)-term defined as zero when \(w_\alpha=0\), is a Borel, partition-permutation-equivariant selector and satisfies a dimension-free Lipschitz estimate.

## 1. A uniform local constant

For \(1\le d\le r\), let \(G_{A,R}\) denote the least-Euclidean-norm point of the full positive capacitated flow fiber for a \(d\times d\) kernel \(A\) and rank-one projector \(R\).

By the audited fixed-support result, the following constant is finite:
\[
\Lambda_{\varepsilon,r}
:=
\max_{1\le d\le r}
\sup_{\substack{(A,R)\ne(B,S)\\
\varepsilon I\preceq A,B\preceq(1-\varepsilon)I}}
\frac{\|G_{A,R}-G_{B,S}\|_1}
{\|A-B\|_1+\|R-S\|_1}
<\infty.
\tag{2}
\]
All local estimates below use this one constant.

Every local \(G_{A,R}\) is nonnegative and has total edge mass one, hence
\[
\|G_{A,R}\|_1=1.
\tag{3}
\]

## 2. Product structure of the block DPP

Because
\[
K=\bigoplus_{\alpha}K_\alpha,
\]
the DPP law factors over the blocks:
\[
p_K(U)=\prod_{\alpha}p_{K_\alpha}(S_\alpha).
\tag{4}
\]
Equivalently, for every \(\alpha\),
\[
p_K(U)
=
p_{K_{E\setminus B_\alpha}}(T_\alpha)\,
p_{K_\alpha}(S_\alpha).
\tag{5}
\]

## 3. Exact derivative and disappearance of cross-block entries

For any admissible Hermitian kernel \(A\), the exact atom formula is
\[
p_A(U)
=
(-1)^{|U^c|}
\det(A-I_{U^c}).
\tag{6}
\]
The matrix \(A-I_{U^c}\) is invertible under the fixed-gap assumption. Indeed, if
\[
J_U=I-2I_{U^c},
\]
then
\[
A-I_{U^c}
=
\frac12J_U\bigl(I+J_U(2A-I)\bigr),
\tag{7}
\]
and
\[
\|J_U(2A-I)\|
=
\|2A-I\|
\le1-2\varepsilon<1.
\]

Differentiating (6) at \(K\) in the direction \(P\) gives
\[
b_{K,P}(U)
=
p_K(U)\,
\operatorname{tr}\bigl((K-I_{U^c})^{-1}P\bigr).
\tag{8}
\]

Since \(K\) is block diagonal,
\[
K-I_{U^c}
=
\bigoplus_{\alpha}
\left(K_\alpha-I_{B_\alpha\setminus S_\alpha}\right),
\tag{9}
\]
and therefore its inverse is also block diagonal. Hence
\[
\operatorname{tr}\bigl((K-I_{U^c})^{-1}P\bigr)
=
\sum_\alpha
\operatorname{tr}\left[
\left(K_\alpha-I_{B_\alpha\setminus S_\alpha}\right)^{-1}
P_\alpha
\right].
\tag{10}
\]

This proves directly that the cross-block entries
\[
\Pi_\alpha P\Pi_\beta,\qquad \alpha\ne\beta,
\]
do not contribute: they lie in off-diagonal blocks of the product in (10) and therefore have zero trace.

For \(w_\alpha>0\), \(P_\alpha=w_\alpha R_\alpha\). The local atom derivative is
\[
b_{K_\alpha,R_\alpha}(S_\alpha)
=
p_{K_\alpha}(S_\alpha)
\operatorname{tr}\left[
\left(K_\alpha-I_{B_\alpha\setminus S_\alpha}\right)^{-1}
R_\alpha
\right].
\tag{11}
\]
Using (5), (8), and (10), we obtain the exact decomposition
\[
\boxed{
b_{K,P}(U)
=
\sum_\alpha
w_\alpha\,
p_{K_{E\setminus B_\alpha}}(T_\alpha)\,
b_{K_\alpha,R_\alpha}(S_\alpha).
}
\tag{12}
\]
When \(w_\alpha=0\), \(P_\alpha=0\), and the corresponding term is zero.

## 4. Nonnegativity and exact divergence

Every factor in (1) is nonnegative, so
\[
F^{\mathrm{blk}}_{K,P}\ge0.
\tag{13}
\]

Fix \(U\subseteq E\). For a given block \(B_\alpha\), all edges adding a coordinate in \(B_\alpha\) keep the outside configuration \(T_\alpha\) fixed. Therefore the contribution of the \(\alpha\)-edges to the global divergence at \(U\) is
\[
w_\alpha\,
p_{K_{E\setminus B_\alpha}}(T_\alpha)\,
\operatorname{div}
G_{K_\alpha,R_\alpha}(S_\alpha).
\tag{14}
\]
Since the local selector belongs to the local flow fiber,
\[
\operatorname{div}G_{K_\alpha,R_\alpha}
=
b_{K_\alpha,R_\alpha}.
\tag{15}
\]
Summing (14) over the blocks and using (12),
\[
\operatorname{div}F^{\mathrm{blk}}_{K,P}(U)
=
b_{K,P}(U).
\tag{16}
\]

Thus the exact global divergence constraint holds.

## 5. Total mass one

For a fixed \(\alpha\), summing the \(\alpha\)-component over all outside configurations and all local edges gives
\[
\begin{aligned}
&\sum_{T\subseteq E\setminus B_\alpha}
\sum_{\substack{S\subseteq B_\alpha\\i\in B_\alpha\setminus S}}
w_\alpha\,
p_{K_{E\setminus B_\alpha}}(T)\,
G_{K_\alpha,R_\alpha}(S,i)\\
&\qquad=
w_\alpha
\left(\sum_Tp_{K_{E\setminus B_\alpha}}(T)\right)
\left(\sum_{S,i}G_{K_\alpha,R_\alpha}(S,i)\right)\\
&\qquad=w_\alpha.
\end{aligned}
\tag{17}
\]
Since
\[
\sum_\alpha w_\alpha
=
\sum_\alpha\operatorname{tr}P_\alpha
=
\operatorname{tr}P
=
1,
\tag{18}
\]
the total mass of the global flow is one:
\[
\sum_eF^{\mathrm{blk}}_{K,P}(e)=1.
\tag{19}
\]

## 6. Original pointwise capacity

At \(U\subseteq E\), the outgoing flow along coordinates in \(B_\alpha\) is
\[
w_\alpha\,
p_{K_{E\setminus B_\alpha}}(T_\alpha)\,
\bigl(G_{K_\alpha,R_\alpha}\bigr)_{\mathrm{out}}(S_\alpha).
\tag{20}
\]
The local flow satisfies the original local capacity:
\[
\bigl(G_{K_\alpha,R_\alpha}\bigr)_{\mathrm{out}}(S_\alpha)
\le
\frac2\varepsilon p_{K_\alpha}(S_\alpha).
\tag{21}
\]
Consequently,
\[
\begin{aligned}
\bigl(F^{\mathrm{blk}}_{K,P}\bigr)_{\mathrm{out}}(U)
&\le
\frac2\varepsilon
\sum_\alpha
w_\alpha\,
p_{K_{E\setminus B_\alpha}}(T_\alpha)\,
p_{K_\alpha}(S_\alpha)\\
&=
\frac2\varepsilon
p_K(U)\sum_\alpha w_\alpha\\
&=
\frac2\varepsilon p_K(U).
\end{aligned}
\tag{22}
\]
Thus
\[
\boxed{
F^{\mathrm{blk}}_{K,P}\in\mathcal F_E(K,P).
}
\tag{23}
\]

## 7. The homogeneous local estimate

The normalization \(P_\alpha\mapsto R_\alpha=P_\alpha/w_\alpha\) is potentially singular when \(w_\alpha\) is small. The singularity disappears after multiplying by \(w_\alpha\).

Let \(A,B\) be two local kernels of size at most \(r\), and let
\[
X=xR,\qquad Y=yS
\tag{24}
\]
be nonnegative rank-at-most-one matrices, where \(x,y\ge0\) and, when the scalar is positive, \(R,S\) are rank-one projectors.

Define
\[
\widehat G(A,X)
=
\begin{cases}
xG_{A,R},&x>0,\\
0,&x=0.
\end{cases}
\tag{25}
\]

We claim
\[
\boxed{
\|\widehat G(A,X)-\widehat G(B,Y)\|_1
\le
\Lambda_{\varepsilon,r}\,x\|A-B\|_1
+
(1+2\Lambda_{\varepsilon,r})\|X-Y\|_1.
}
\tag{26}
\]

Assume first \(x,y>0\). By inserting \(xG_{B,R}\),
\[
\begin{aligned}
\|xG_{A,R}-yG_{B,S}\|_1
&\le
x\|G_{A,R}-G_{B,R}\|_1\\
&\quad+
\|xG_{B,R}-yG_{B,S}\|_1\\
&\le
\Lambda_{\varepsilon,r}x\|A-B\|_1\\
&\quad+
|x-y|
+
\Lambda_{\varepsilon,r}\min(x,y)\|R-S\|_1.
\end{aligned}
\tag{27}
\]

Let
\[
D=\|X-Y\|_1=\|xR-yS\|_1.
\]
Since
\[
|x-y|
=
|\operatorname{tr}(X-Y)|
\le D,
\tag{28}
\]
it remains to control the normalized projectors.

Suppose \(x\ge y\). Then
\[
\begin{aligned}
y\|R-S\|_1
&=\|yR-yS\|_1\\
&\le
\|yR-xR\|_1+\|xR-yS\|_1\\
&=(x-y)+D\\
&\le2D.
\end{aligned}
\tag{29}
\]
The case \(y\ge x\) is symmetric. Therefore
\[
\min(x,y)\|R-S\|_1\le2D.
\tag{30}
\]
Substituting (28) and (30) into (27) proves (26).

If, say, \(x=0\), then
\[
\|\widehat G(A,0)-\widehat G(B,Y)\|_1
=
y
=
\|Y\|_1
=
\|X-Y\|_1,
\]
so (26) remains true. The other zero cases are identical.

Thus the weighted local selector is Lipschitz directly in the unnormalized compressed matrices, with no division by small block weights.

## 8. Stability of gapped DPP laws

We use the following dimension-free estimate. If
\[
\varepsilon I\preceq A,B\preceq(1-\varepsilon)I,
\]
then
\[
\boxed{
\|p_A-p_B\|_1
\le
\frac1\varepsilon\|A-B\|_1.
}
\tag{31}
\]

To prove it, put \(A_t=(1-t)A+tB\). For an atom \(S\),
\[
\frac d{dt}p_{A_t}(S)
=
p_{A_t}(S)
\operatorname{tr}\left[
(A_t-I_{S^c})^{-1}(B-A)
\right].
\tag{32}
\]
The factorization (7) gives
\[
\|(A_t-I_{S^c})^{-1}\|_{\mathrm{op}}
\le\frac1\varepsilon.
\tag{33}
\]
Therefore
\[
\left|\frac d{dt}p_{A_t}(S)\right|
\le
\frac1\varepsilon
p_{A_t}(S)\|B-A\|_1.
\tag{34}
\]
Summing over \(S\) and integrating over \(t\in[0,1]\) proves (31).

For each block put
\[
\rho_\beta^K=p_{K_\beta},
\qquad
\rho_\beta^L=p_{L_\beta},
\qquad
\delta_\beta=\|K_\beta-L_\beta\|_1.
\tag{35}
\]
Then
\[
\|\rho_\beta^K-\rho_\beta^L\|_1
\le
\frac1\varepsilon\delta_\beta.
\tag{36}
\]

Because the outside laws are products,
\[
p_{K_{E\setminus B_\alpha}}
=
\bigotimes_{\beta\ne\alpha}\rho_\beta^K,
\qquad
p_{L_{E\setminus B_\alpha}}
=
\bigotimes_{\beta\ne\alpha}\rho_\beta^L.
\]
A telescoping product expansion gives
\[
\left\|
p_{K_{E\setminus B_\alpha}}
-
p_{L_{E\setminus B_\alpha}}
\right\|_1
\le
\sum_{\beta\ne\alpha}
\|\rho_\beta^K-\rho_\beta^L\|_1
\le
\frac1\varepsilon
\sum_{\beta\ne\alpha}\delta_\beta.
\tag{37}
\]

## 9. Global Lipschitz estimate

For \(Q\), define
\[
Q_\alpha=\Pi_\alpha Q\Pi_\alpha,
\qquad
z_\alpha=\operatorname{tr}Q_\alpha,
\]
and, when \(z_\alpha>0\),
\[
S_\alpha=\frac{Q_\alpha}{z_\alpha}.
\]

Let
\[
H_\alpha^{K,P}
=
\widehat G(K_\alpha,P_\alpha)
=
w_\alpha G_{K_\alpha,R_\alpha},
\tag{38}
\]
and similarly
\[
H_\alpha^{L,Q}
=
z_\alpha G_{L_\alpha,S_\alpha}.
\tag{39}
\]
These are local edge vectors of total masses
\[
\|H_\alpha^{K,P}\|_1=w_\alpha,
\qquad
\|H_\alpha^{L,Q}\|_1=z_\alpha.
\tag{40}
\]

The global edge space is the direct sum over the blocks adding the edge. Under the natural product identification,
\[
F^{\mathrm{blk}}_{K,P}
=
\bigoplus_\alpha
\left(
p_{K_{E\setminus B_\alpha}}\otimes
H_\alpha^{K,P}
\right).
\tag{41}
\]
Hence
\[
\begin{aligned}
&\|F^{\mathrm{blk}}_{K,P}-F^{\mathrm{blk}}_{L,Q}\|_1\\
&\quad=
\sum_\alpha
\left\|
p_{K_{E\setminus B_\alpha}}\otimes H_\alpha^{K,P}
-
p_{L_{E\setminus B_\alpha}}\otimes H_\alpha^{L,Q}
\right\|_1\\
&\quad\le
\sum_\alpha
w_\alpha
\left\|
p_{K_{E\setminus B_\alpha}}
-
p_{L_{E\setminus B_\alpha}}
\right\|_1\\
&\qquad+
\sum_\alpha
\|H_\alpha^{K,P}-H_\alpha^{L,Q}\|_1.
\end{aligned}
\tag{42}
\]

### 9.1 Outside-law contribution

Using (37) and \(\sum_\alpha w_\alpha=1\),
\[
\begin{aligned}
&\sum_\alpha
w_\alpha
\left\|
p_{K_{E\setminus B_\alpha}}
-
p_{L_{E\setminus B_\alpha}}
\right\|_1\\
&\quad\le
\frac1\varepsilon
\sum_\alpha w_\alpha
\sum_{\beta\ne\alpha}\delta_\beta\\
&\quad=
\frac1\varepsilon
\sum_\beta\delta_\beta
\sum_{\alpha\ne\beta}w_\alpha\\
&\quad=
\frac1\varepsilon
\sum_\beta(1-w_\beta)\delta_\beta\\
&\quad\le
\frac1\varepsilon
\sum_\beta\delta_\beta\\
&\quad=
\frac1\varepsilon\|K-L\|_1.
\end{aligned}
\tag{43}
\]
The weights \(w_\alpha\) eliminate any dependence on the number of blocks.

### 9.2 Local scaled-selector contribution

Applying (26) block by block,
\[
\begin{aligned}
\sum_\alpha
\|H_\alpha^{K,P}-H_\alpha^{L,Q}\|_1
&\le
\Lambda_{\varepsilon,r}
\sum_\alpha
w_\alpha\|K_\alpha-L_\alpha\|_1\\
&\quad+
(1+2\Lambda_{\varepsilon,r})
\sum_\alpha
\|P_\alpha-Q_\alpha\|_1\\
&\le
\Lambda_{\varepsilon,r}\|K-L\|_1\\
&\quad+
(1+2\Lambda_{\varepsilon,r})
\sum_\alpha
\|P_\alpha-Q_\alpha\|_1.
\end{aligned}
\tag{44}
\]

The final sum is controlled by trace-norm pinching. Let
\[
\mathcal P(X)=\sum_\alpha\Pi_\alpha X\Pi_\alpha.
\]
Then
\[
\mathcal P(P-Q)
=
\bigoplus_\alpha(P_\alpha-Q_\alpha),
\]
and therefore
\[
\sum_\alpha\|P_\alpha-Q_\alpha\|_1
=
\|\mathcal P(P-Q)\|_1.
\tag{45}
\]
Pinching is trace-norm contractive on Hermitian matrices:
\[
\|\mathcal P(X)\|_1\le\|X\|_1.
\tag{46}
\]
For completeness, if
\[
Z=\operatorname{sgn}(\mathcal P(X)),
\]
then \(Z\) is block diagonal and \(\|Z\|_{\mathrm{op}}\le1\), so
\[
\|\mathcal P(X)\|_1
=
\operatorname{tr}(Z\mathcal P(X))
=
\operatorname{tr}(ZX)
\le
\|X\|_1.
\]
Thus
\[
\sum_\alpha\|P_\alpha-Q_\alpha\|_1
\le
\|P-Q\|_1.
\tag{47}
\]

Combining (44) and (47),
\[
\sum_\alpha
\|H_\alpha^{K,P}-H_\alpha^{L,Q}\|_1
\le
\Lambda_{\varepsilon,r}\|K-L\|_1
+
(1+2\Lambda_{\varepsilon,r})\|P-Q\|_1.
\tag{48}
\]

Finally, from (42), (43), and (48),
\[
\boxed{
\begin{aligned}
\|F^{\mathrm{blk}}_{K,P}-F^{\mathrm{blk}}_{L,Q}\|_1
&\le
\left(\frac1\varepsilon+\Lambda_{\varepsilon,r}\right)
\|K-L\|_1\\
&\quad+
(1+2\Lambda_{\varepsilon,r})
\|P-Q\|_1.
\end{aligned}}
\tag{49}
\]

Therefore \((\mathrm{BLIP})\) holds with the exactly defined finite constant
\[
\boxed{
C_{\varepsilon,r}
=
\max\left\{
\frac1\varepsilon+\Lambda_{\varepsilon,r},
\ 1+2\Lambda_{\varepsilon,r}
\right\}.
}
\tag{50}
\]

This constant is independent of \(|E|\) and of the number of blocks.

## 10. Zero-weight blocks and support degeneration

If \(w_\alpha=0\), then \(v_{B_\alpha}=0\) and
\[
P_\alpha=0.
\]
The corresponding global component is defined to be zero.

There is no discontinuity at \(w_\alpha=0\), since
\[
\|w_\alpha G_{K_\alpha,R_\alpha}\|_1=w_\alpha\longrightarrow0.
\tag{51}
\]
More strongly, the homogeneous estimate (26) proves continuity and Lipschitz control directly in the unnormalized compression \(P_\alpha\), without ever dividing by a small weight in an estimate.

Thus arbitrary support degenerations are covered.

## 11. Borel dependence

For \(w_\alpha>0\),
\[
(K_\alpha,P_\alpha)
\longmapsto
w_\alpha G_{K_\alpha,P_\alpha/w_\alpha}
\]
is continuous. At \(w_\alpha=0\), continuity follows from (51), or directly from (26).

The DPP probabilities
\[
K\longmapsto p_{K_{E\setminus B_\alpha}}(T)
\]
are polynomial combinations of determinants and hence continuous. Therefore every edge coordinate of \(F^{\mathrm{blk}}_{K,P}\) is Borel; in fact, the global selector is continuous on the stated parameter domain.

## 12. Partition-permutation equivariance

Let \(\sigma\) be a coordinate permutation carrying the supplied partition
\[
\{B_\alpha\}_{\alpha\in A}
\]
to the relabeled partition
\[
\{\sigma B_\alpha\}_{\alpha\in A}.
\]
Let \(U_\sigma\) be its permutation matrix. Then
\[
K^\sigma=U_\sigma KU_\sigma^*,
\qquad
P^\sigma=U_\sigma PU_\sigma^*.
\]

For each block,
\[
w_{\sigma\alpha}(P^\sigma)=w_\alpha(P),
\qquad
R_{\sigma\alpha}(P^\sigma)
=
U_\sigma R_\alpha(P)U_\sigma^*.
\tag{52}
\]
The local flow fibers are carried to one another by the induced coordinate permutation. Since that action is a Euclidean isometry and the least-Euclidean-norm point is unique,
\[
G_{K^\sigma_{\sigma B_\alpha},
\,R^\sigma_{\sigma B_\alpha}}
(\sigma S,\sigma i)
=
G_{K_\alpha,R_\alpha}(S,i).
\tag{53}
\]
Likewise,
\[
p_{K^\sigma_{E\setminus\sigma B_\alpha}}(\sigma T)
=
p_{K_{E\setminus B_\alpha}}(T).
\tag{54}
\]
Substitution into (1) gives
\[
F^{\mathrm{blk}}_{K^\sigma,P^\sigma}(\sigma U,\sigma i)
=
F^{\mathrm{blk}}_{K,P}(U,i).
\tag{55}
\]
Thus the selector is partition-permutation-equivariant.

Hence \((\mathrm{BSEL})\) is a Borel, partition-permutation-equivariant selector in the full global flow fiber, and it satisfies the dimension-free estimate \((\mathrm{BLIP})\) with \(C_{\varepsilon,r}\) given by (50).

