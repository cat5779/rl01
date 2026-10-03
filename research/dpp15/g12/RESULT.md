DISPROVED

Let \(E=\{1,\dots,n\}\) and
\[
K_E=\frac12 I_E.
\]
For every rank-one projector \(P\), define the upward edge flow
\[
\boxed{\;
\Phi_E(P)(S,i)=2^{-(n-1)}P_{ii},
\qquad S\subseteq E,\ i\notin S.
\;}
\tag{1}
\]

This gives a globally defined Borel, coordinate-permutation-equivariant selector, and it satisfies
\[
\|\Phi_E(P)-\Phi_E(Q)\|_1\le \|P-Q\|_1.
\tag{2}
\]
Thus \((\mathrm{NS0})\) holds with the dimension-free constant
\[
C_\varepsilon=1.
\]

We verify every assertion.

## 1. Exact divergence at \(K=I/2\)

For a DPP kernel \(K\), the atom at \(S\subseteq E\) can be written as
\[
p_K(S)=(-1)^{|S^c|}\det(K-I_{S^c}),
\tag{3}
\]
where \(I_{S^c}\) is the diagonal projection onto \(S^c\).

At \(K=\frac12I\),
\[
K-I_{S^c}
=
\operatorname{diag}
\left(
\frac12\mathbf 1_{\{i\in S\}}
-\frac12\mathbf 1_{\{i\notin S\}}
\right),
\]
so
\[
p_{I/2}(S)=2^{-n}.
\tag{4}
\]
Moreover,
\[
\left(\frac12I-I_{S^c}\right)^{-1}
=
2I_S-2I_{S^c}.
\tag{5}
\]

Differentiating (3) in the direction \(P\) gives
\[
b_{I/2,P}(S)
=
p_{I/2}(S)
\operatorname{tr}
\left[
\left(\frac12I-I_{S^c}\right)^{-1}P
\right].
\tag{6}
\]
Using (4) and (5),
\[
\boxed{\;
b_{I/2,P}(S)
=
2^{-(n-1)}
\left(
\sum_{i\in S}P_{ii}
-
\sum_{i\notin S}P_{ii}
\right).
\;}
\tag{7}
\]

Although \(P\) may have arbitrary complex phases in its off-diagonal entries, the derivative at the scalar diagonal kernel \(I/2\) depends only on the diagonal numbers \(P_{ii}\).

## 2. Nonnegativity

A rank-one projector has the form
\[
P=vv^*
\]
for a unit vector \(v\in\mathbb C^n\). Therefore
\[
P_{ii}=|v_i|^2\ge0,
\qquad
\sum_{i=1}^nP_{ii}=\operatorname{tr}P=1.
\tag{8}
\]
It follows immediately from (1) that
\[
\Phi_E(P)(S,i)\ge0.
\tag{9}
\]

This remains valid when some coordinates of \(v\) vanish: all edges in such a coordinate simply receive zero mass. The definition is directly in terms of \(P\), so it is unaffected by replacing \(v\) with \(e^{\mathrm i\theta}v\).

## 3. Divergence

At a vertex \(S\), the incoming mass is
\[
\sum_{i\in S}\Phi_E(P)(S\setminus\{i\},i)
=
2^{-(n-1)}\sum_{i\in S}P_{ii},
\tag{10}
\]
while the outgoing mass is
\[
\sum_{i\notin S}\Phi_E(P)(S,i)
=
2^{-(n-1)}\sum_{i\notin S}P_{ii}.
\tag{11}
\]
Consequently,
\[
\begin{aligned}
\operatorname{div}\Phi_E(P)(S)
&=
\sum_{i\in S}\Phi_E(P)(S\setminus\{i\},i)
-
\sum_{i\notin S}\Phi_E(P)(S,i)\\
&=
2^{-(n-1)}
\left(
\sum_{i\in S}P_{ii}
-
\sum_{i\notin S}P_{ii}
\right)\\
&=b_{I/2,P}(S),
\end{aligned}
\tag{12}
\]
by (7).

## 4. Total mass

For each fixed coordinate \(i\), there are exactly \(2^{n-1}\) subsets \(S\subseteq E\) not containing \(i\). Therefore
\[
\begin{aligned}
\sum_{S\subseteq E}\sum_{i\notin S}\Phi_E(P)(S,i)
&=
\sum_{i=1}^n
\sum_{S\subseteq E\setminus\{i\}}
2^{-(n-1)}P_{ii}\\
&=
\sum_{i=1}^nP_{ii}\\
&=1.
\end{aligned}
\tag{13}
\]

## 5. Pointwise outgoing capacities

For every \(S\subseteq E\),
\[
\begin{aligned}
\Phi_E(P)_{\mathrm{out}}(S)
&=
2^{-(n-1)}\sum_{i\notin S}P_{ii}\\
&\le 2^{-(n-1)}.
\end{aligned}
\tag{14}
\]
On the other hand, since \(p_{I/2}(S)=2^{-n}\),
\[
\frac2\varepsilon p_{I/2}(S)
=
\frac{2^{-(n-1)}}{\varepsilon}.
\tag{15}
\]
Because \(0<\varepsilon<\frac12\), in particular \(\varepsilon<1\), so
\[
2^{-(n-1)}
\le
\frac{2^{-(n-1)}}{\varepsilon}.
\tag{16}
\]
Combining (14)–(16),
\[
\Phi_E(P)_{\mathrm{out}}(S)
\le
\frac2\varepsilon p_{I/2}(S).
\tag{17}
\]

Equations (9), (12), (13), and (17) prove
\[
\boxed{\Phi_E(P)\in\mathcal F_E(P)}
\tag{18}
\]
for every rank-one projector \(P\).

## 6. Dimension-free Lipschitz estimate

From (1),
\[
\begin{aligned}
\|\Phi_E(P)-\Phi_E(Q)\|_1
&=
\sum_{i=1}^n
\sum_{S\subseteq E\setminus\{i\}}
2^{-(n-1)}
|P_{ii}-Q_{ii}|\\
&=
\sum_{i=1}^n|P_{ii}-Q_{ii}|.
\end{aligned}
\tag{19}
\]

For completeness, let
\[
A=P-Q.
\]
It is Hermitian. Choose a diagonal matrix
\[
D=\operatorname{diag}(d_1,\ldots,d_n),
\qquad
d_i=
\begin{cases}
\operatorname{sgn}(A_{ii}),&A_{ii}\ne0,\\
0,&A_{ii}=0.
\end{cases}
\tag{20}
\]
Then \(\|D\|_{\mathrm{op}}\le1\), and
\[
\sum_i|A_{ii}|=\operatorname{tr}(DA).
\tag{21}
\]
Trace-norm/operator-norm duality yields
\[
\sum_i|A_{ii}|
=
|\operatorname{tr}(DA)|
\le
\|D\|_{\mathrm{op}}\|A\|_1
\le
\|A\|_1.
\tag{22}
\]
Thus
\[
\boxed{\;
\|\Phi_E(P)-\Phi_E(Q)\|_1
\le
\|P-Q\|_1.
\;}
\tag{23}
\]

The constant is \(1\), independent of \(n\) and independent of \(\varepsilon\).

## 7. Borel measurability and permutation equivariance

The map
\[
P\longmapsto \Phi_E(P)
\]
is linear in the diagonal entries of \(P\), hence continuous and therefore Borel.

Let \(\sigma\) be a coordinate permutation and \(U_\sigma\) its permutation matrix. The natural actions are
\[
P\longmapsto U_\sigma P U_\sigma^*
\tag{24}
\]
and
\[
(\sigma F)(S,i)
=
F(\sigma^{-1}S,\sigma^{-1}i).
\tag{25}
\]
Since
\[
(U_\sigma P U_\sigma^*)_{ii}
=
P_{\sigma^{-1}i,\sigma^{-1}i},
\tag{26}
\]
we have
\[
\begin{aligned}
\Phi_E(U_\sigma P U_\sigma^*)(S,i)
&=
2^{-(n-1)}
P_{\sigma^{-1}i,\sigma^{-1}i}\\
&=
\Phi_E(P)(\sigma^{-1}S,\sigma^{-1}i)\\
&=
(\sigma\Phi_E(P))(S,i).
\end{aligned}
\tag{27}
\]
Hence the selector is coordinate-permutation-equivariant.

Therefore the asserted nonexistence statement is false: the family (1) satisfies all requirements of \((\mathrm{NS0})\) with
\[
\boxed{C_\varepsilon=1.}
\]



