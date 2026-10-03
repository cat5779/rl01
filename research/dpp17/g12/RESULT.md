PROVED

Fix \(0<\varepsilon<\tfrac12\). We construct an explicit selector on the whole matching-block class and prove
\[
\|\Psi_E(K,P)-\Psi_E(L,Q)\|_1
\le C_\varepsilon
\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
\]
with, for example,
\[
\boxed{C_\varepsilon=\frac{80}{\varepsilon^2}+205.}
\]

The key point is to choose the two-coordinate local selector so that it agrees exactly with the diagonal selector when the off-diagonal entry vanishes. This makes the global construction independent of whether a zero-coupled pair is viewed as one two-coordinate block or as two singleton blocks. The changing canonical matchings can then be compared by deleting only those edges that are not common to the two matchings.

---

# 1. A dimension-free stability bound for DPP laws

We first record a standard estimate used below.

For \(S\subseteq E\), put \(D_S=I_{S^c}\). The atom formula is
\[
p_A(S)=(-1)^{|S^c|}\det(A-D_S).
\tag{1}
\]
If
\[
\varepsilon I\preceq A\preceq(1-\varepsilon)I,
\]
then
\[
\|(A-D_S)^{-1}\|_{\mathrm{op}}\le\frac1\varepsilon.
\tag{2}
\]
Indeed, with \(J_S=I-2D_S\),
\[
A-D_S
=
\frac12J_S\bigl(I+J_S(2A-I)\bigr),
\]
and
\[
\|J_S(2A-I)\|_{\mathrm{op}}
\le1-2\varepsilon.
\]

Let \(A_t=(1-t)A+tB\). Differentiating (1),
\[
\frac d{dt}p_{A_t}(S)
=
p_{A_t}(S)
\operatorname{tr}\!\left((A_t-D_S)^{-1}(B-A)\right).
\]
Consequently,
\[
\left|\frac d{dt}p_{A_t}(S)\right|
\le
\frac1\varepsilon
p_{A_t}(S)\|A-B\|_1.
\]
Summing over \(S\) and integrating gives
\[
\boxed{
\|p_A-p_B\|_1
\le
\frac1\varepsilon\|A-B\|_1.
}
\tag{3}
\]

The same inverse estimate also gives, for every rank-one projector \(R\),
\[
|b_{A,R}(S)|
\le
\frac1\varepsilon p_A(S).
\tag{4}
\]

---

# 2. A refinement-compatible selector on a two-coordinate block

Let
\[
A=
\begin{pmatrix}
a&c\\
\overline c&b
\end{pmatrix},
\qquad
\varepsilon I\preceq A\preceq(1-\varepsilon)I,
\tag{5}
\]
and let
\[
R=
\begin{pmatrix}
r_1&\rho\\
\overline\rho&r_2
\end{pmatrix}
=uu^*
\tag{6}
\]
be a rank-one projector. Thus
\[
r_1,r_2\ge0,\qquad r_1+r_2=1.
\]

Name the four upward edges of the two-cube by
\[
x=G(\varnothing,1),\qquad
y=G(\varnothing,2),\qquad
u=G(\{2\},1),\qquad
v=G(\{1\},2).
\tag{7}
\]

## 2.1 The divergence constraints

Put
\[
t=-b_{A,R}(\varnothing).
\tag{8}
\]
Since
\[
p_A(\varnothing)=\det(I-A),
\]
direct differentiation gives
\[
\boxed{
t=(1-b)r_1+(1-a)r_2+2\operatorname{Re}(\overline c\,\rho).
}
\tag{9}
\]

The marginal inclusion probability of coordinate \(i\) is \(A_{ii}\), so its derivative in direction \(R\) is \(r_i\). Therefore every flow with divergence \(b_{A,R}\) must satisfy
\[
x+u=r_1,\qquad y+v=r_2.
\tag{10}
\]
The divergence at \(\varnothing\) gives
\[
x+y=t.
\tag{11}
\]
Hence every such flow is of the form
\[
\boxed{
y=t-x,\qquad
u=r_1-x,\qquad
v=r_2-t+x.
}
\tag{12}
\]

These equations give the full divergence. Indeed,
\[
\operatorname{div}G(\varnothing)=-t=b_{A,R}(\varnothing),
\]
and, using the total-probability and marginal derivative identities,
\[
b_{A,R}(\{1\})=t-r_2,\qquad
b_{A,R}(\{2\})=t-r_1,\qquad
b_{A,R}(\{1,2\})=1-t.
\tag{13}
\]
The flow (12) has precisely these divergences.

## 2.2 The feasible interval

Set
\[
C_1=\frac2\varepsilon p_A(\{1\}),
\qquad
C_2=\frac2\varepsilon p_A(\{2\}).
\tag{14}
\]
The nonnegativity constraints and the outgoing capacities at \(\{1\}\) and \(\{2\}\) are equivalent to
\[
\ell(A,R)\le x\le u(A,R),
\tag{15}
\]
where
\[
\boxed{
\ell
=
\max\{0,\ t-r_2,\ r_1-C_2\},
}
\tag{16}
\]
and
\[
\boxed{
u
=
\min\{r_1,\ t,\ C_1-r_2+t\}.
}
\tag{17}
\]

The capacity at \(\varnothing\) is automatic:
\[
t
=
p_A(\varnothing)
\operatorname{tr}\!\left((I-A)^{-1}R\right)
\le
\frac1\varepsilon p_A(\varnothing)
\le
\frac2\varepsilon p_A(\varnothing).
\tag{18}
\]

We verify that \(\ell\le u\). First,
\[
t\ge0,
\qquad
1-t=b_{A,R}(\{1,2\})\ge0,
\tag{19}
\]
because both \(I-A\) and \(A\) are positive definite and the corresponding determinant derivatives have the indicated signs. Thus \(0\le t\le1\).

By (4),
\[
r_2-t=-b_{A,R}(\{1\})
\le \frac1\varepsilon p_A(\{1\})
\le C_1,
\tag{20}
\]
whenever the left side is positive. Similarly,
\[
r_1-t\le C_2.
\tag{21}
\]

It remains to note that
\[
1-t\le C_1+C_2.
\tag{22}
\]
Indeed, if \(\lambda_1,\lambda_2\in[\varepsilon,1-\varepsilon]\) are the eigenvalues of \(A\), then
\[
p_A(\{1\})+p_A(\{2\})
=
\lambda_1(1-\lambda_2)+\lambda_2(1-\lambda_1)
\ge2\varepsilon(1-\varepsilon).
\]
Therefore
\[
C_1+C_2
\ge4(1-\varepsilon)>1\ge1-t.
\tag{23}
\]
Equations (19)–(23) imply \(\ell\le u\).

## 2.3 The selected point

Define the symmetric reference value
\[
\boxed{
s(A,R)
=
(1-b)r_1+\operatorname{Re}(\overline c\,\rho).
}
\tag{24}
\]
We choose
\[
\boxed{
x(A,R)
=
\operatorname{proj}_{[\ell(A,R),u(A,R)]}s(A,R),
}
\tag{25}
\]
and define \(y,u,v\) from (12). Denote the resulting flow by
\[
G_{A,R}.
\]

By construction it is nonnegative, has exact divergence \(b_{A,R}\), obeys all pointwise capacities, and has total mass
\[
x+y+u+v=t+(1-t)=1.
\tag{26}
\]

Thus
\[
G_{A,R}\in\mathcal F_{\{1,2\}}(A,R).
\tag{27}
\]

---

# 3. Exact compatibility with the diagonal selector

Suppose \(c=0\). Then
\[
t=(1-b)r_1+(1-a)r_2
\]
and
\[
s=(1-b)r_1.
\]
The corresponding four edge masses are
\[
\begin{aligned}
x&=r_1(1-b),&
u&=r_1b,\\
y&=r_2(1-a),&
v&=r_2a.
\end{aligned}
\tag{28}
\]
These satisfy the capacities because, for example,
\[
v=r_2a\le a
\le\frac{2a(1-b)}{\varepsilon}
=\frac2\varepsilon p_A(\{1\}),
\]
and similarly for \(u\). Hence \(s\in[\ell,u]\), so the projection in (25) leaves \(s\) unchanged.

Therefore, whenever \(A=\operatorname{diag}(a,b)\),
\[
\boxed{
G_{A,R}(S,i)
=
R_{ii}\,p_{A_{\{1,2\}\setminus\{i\}}}(S).
}
\tag{29}
\]
This is exactly the previously established diagonal selector.

This identity is the refinement-compatibility property needed when a two-coordinate component breaks into two singleton components.

---

# 4. Permutation covariance of the local selector

Interchanging coordinates \(1\) and \(2\) leaves \(t\) unchanged. The new reference value is
\[
s'=(1-a)r_2+\operatorname{Re}(\overline c\,\rho)
=t-s.
\tag{30}
\]
The feasible interval transforms as
\[
[\ell',u']=[t-u,t-\ell].
\tag{31}
\]
Therefore
\[
\operatorname{proj}_{[\ell',u']}(s')
=
t-\operatorname{proj}_{[\ell,u]}(s).
\tag{32}
\]
Thus the new \(x\)-edge is the old \(y\)-edge, and the remaining three edges are also permuted correctly. Hence \(G_{A,R}\) is covariant under the transposition of the two coordinates.

---

# 5. A uniform local Lipschitz estimate

Let \(A,B\) be two gapped \(2\times2\) kernels and let \(R,S\) be rank-one projectors. Put
\[
\delta_A=\|A-B\|_1,
\qquad
\delta_R=\|R-S\|_1.
\]

From
\[
t(A,R)
=
\operatorname{tr}\!\bigl(\operatorname{adj}(I-A)R\bigr),
\]
and the fact that, in dimension two,
\[
\operatorname{adj}(I-A)-\operatorname{adj}(I-B)
=
(A-B)-\operatorname{tr}(A-B)I,
\]
we obtain
\[
|t(A,R)-t(B,S)|
\le2\delta_A+\delta_R.
\tag{33}
\]

The reference value (24) can be written
\[
s(A,R)=\operatorname{tr}(N(A)R),
\qquad
N(A)=
\begin{pmatrix}
1-b&c/2\\
\overline c/2&0
\end{pmatrix}.
\]
Consequently,
\[
|s(A,R)-s(B,S)|
\le2\delta_A+2\delta_R.
\tag{34}
\]

By (3),
\[
|p_A(\{j\})-p_B(\{j\})|
\le
\frac1\varepsilon\delta_A.
\]
Thus
\[
|C_j(A)-C_j(B)|
\le
\frac{2}{\varepsilon^2}\delta_A.
\tag{35}
\]
Set
\[
\gamma_\varepsilon=\frac2{\varepsilon^2}.
\]
The max/min formulas (16)–(17) now give
\[
|\ell(A,R)-\ell(B,S)|
\le
\gamma_\varepsilon\delta_A+2\delta_R,
\tag{36}
\]
and
\[
|u(A,R)-u(B,S)|
\le
(\gamma_\varepsilon+2)\delta_A+2\delta_R.
\tag{37}
\]

Projection onto a varying interval satisfies
\[
\left|
\operatorname{proj}_{[\ell,u]}s-
\operatorname{proj}_{[\ell',u']}s'
\right|
\le
|s-s'|+\max\{|\ell-\ell'|,|u-u'|\}.
\]
Therefore
\[
|x(A,R)-x(B,S)|
\le
(\gamma_\varepsilon+4)\delta_A+4\delta_R.
\tag{38}
\]

Using
\[
y=t-x,\qquad
u=r_1-x,\qquad
v=r_2-t+x,
\]
we get
\[
\begin{aligned}
\|G_{A,R}-G_{B,S}\|_1
&\le
4|x-x'|+2|t-t'|
+|r_1-r_1'|+|r_2-r_2'|\\
&\le
\left(\frac8{\varepsilon^2}+20\right)\delta_A
+20\delta_R.
\end{aligned}
\]
Thus, with
\[
\boxed{
\Lambda_\varepsilon=\frac8{\varepsilon^2}+20,
}
\tag{39}
\]
we have
\[
\boxed{
\|G_{A,R}-G_{B,S}\|_1
\le
\Lambda_\varepsilon
\bigl(\|A-B\|_1+\|R-S\|_1\bigr).
}
\tag{40}
\]

For a singleton block, the local selector is the unique one-edge flow of mass one, so the same estimate remains valid.

---

# 6. Homogeneous local control without division by small weights

Let
\[
X=xR,\qquad Y=yS
\]
be positive rank-at-most-one matrices, with \(x,y\ge0\). Define
\[
\widehat G(A,X)=
\begin{cases}
xG_{A,R},&x>0,\\
0,&x=0.
\end{cases}
\tag{41}
\]

Then
\[
\boxed{
\begin{aligned}
\|\widehat G(A,X)-\widehat G(B,Y)\|_1
&\le
\Lambda_\varepsilon x\|A-B\|_1\\
&\quad+
(1+2\Lambda_\varepsilon)\|X-Y\|_1.
\end{aligned}
}
\tag{42}
\]

Indeed,
\[
\begin{aligned}
\|xG_{A,R}-yG_{B,S}\|_1
&\le
x\|G_{A,R}-G_{B,R}\|_1\\
&\quad+
\|xG_{B,R}-yG_{B,S}\|_1.
\end{aligned}
\]
The first term is at most
\[
\Lambda_\varepsilon x\|A-B\|_1.
\]
For the second,
\[
\|xG_{B,R}-yG_{B,S}\|_1
\le
|x-y|
+
\Lambda_\varepsilon\min(x,y)\|R-S\|_1.
\tag{43}
\]
Writing \(D=\|X-Y\|_1\),
\[
|x-y|\le D
\tag{44}
\]
and
\[
\min(x,y)\|R-S\|_1\le2D.
\tag{45}
\]
This proves (42), including the cases \(x=0\) or \(y=0\).

---

# 7. The global selector for a compatible matching partition

Call a partition \(\Pi\) of \(E\) into singleton and two-element blocks compatible with \(K\) if every nonzero off-diagonal entry of \(K\) is contained within one of its blocks. A compatible partition is permitted to group two diagonally uncoupled coordinates into one two-element block.

For \(B\in\Pi\), put
\[
P_B=\Pi_BP\Pi_B,
\qquad
w_B=\operatorname{tr}P_B.
\]
When \(w_B>0\), define
\[
R_B=\frac{P_B}{w_B}.
\]

For an edge \(U\to U\cup\{i\}\), let \(B\) be the block containing \(i\), and write
\[
S=U\cap B,\qquad T=U\setminus B.
\]
Define
\[
\boxed{
\Psi^\Pi_E(K,P)(U,i)
=
w_B\,
p_{K_{E\setminus B}}(T)\,
G_{K_B,R_B}(S,i),
}
\tag{46}
\]
with this term equal to zero when \(w_B=0\).

## 7.1 Exact divergence

The atom derivative is
\[
b_{K,P}(U)
=
p_K(U)
\operatorname{tr}\!\left((K-I_{U^c})^{-1}P\right).
\tag{47}
\]
Because \(K\) is block diagonal over \(\Pi\),
\[
(K-I_{U^c})^{-1}
=
\bigoplus_{B\in\Pi}
\left(K_B-I_{B\setminus S_B}\right)^{-1}.
\]
Thus cross-block entries of \(P\) have zero contribution to the trace, and
\[
\boxed{
b_{K,P}(U)
=
\sum_{B\in\Pi}
w_B\,
p_{K_{E\setminus B}}(T_B)\,
b_{K_B,R_B}(S_B).
}
\tag{48}
\]
Since the local selector has divergence \(b_{K_B,R_B}\), (46) has exactly the global divergence \(b_{K,P}\).

## 7.2 Nonnegativity and total mass

All factors in (46) are nonnegative.

For a fixed block \(B\), summing over all outside configurations and all local edges gives
\[
w_B.
\]
Hence
\[
\sum_e\Psi^\Pi_E(K,P)(e)
=
\sum_{B\in\Pi}w_B
=
\operatorname{tr}P
=
1.
\tag{49}
\]

## 7.3 Capacity

At \(U\subseteq E\),
\[
\begin{aligned}
\Psi^\Pi_{\mathrm{out}}(U)
&=
\sum_{B\in\Pi}
w_Bp_{K_{E\setminus B}}(T_B)
(G_{K_B,R_B})_{\mathrm{out}}(S_B)\\
&\le
\frac2\varepsilon
\sum_{B\in\Pi}
w_Bp_{K_{E\setminus B}}(T_B)p_{K_B}(S_B)\\
&=
\frac2\varepsilon p_K(U)\sum_{B\in\Pi}w_B\\
&=
\frac2\varepsilon p_K(U).
\end{aligned}
\tag{50}
\]
Therefore
\[
\Psi^\Pi_E(K,P)\in\mathcal F_E(K,P).
\tag{51}
\]

---

# 8. Independence of zero-edge refinements

Suppose \(B=\{i,j\}\) and \(K_B\) is diagonal. By (29),
\[
G_{K_B,R_B}(S,i)
=
(R_B)_{ii}
p_{K_{\{j\}}}(S\cap\{j\}).
\]
Therefore
\[
\begin{aligned}
&w_Bp_{K_{E\setminus B}}(T)G_{K_B,R_B}(S,i)\\
&\qquad=
P_{ii}\,
p_{K_{E\setminus B}}(T)
p_{K_{\{j\}}}(S\cap\{j\})\\
&\qquad=
P_{ii}\,p_{K_{E\setminus\{i\}}}(U).
\end{aligned}
\tag{52}
\]
This is exactly the contribution obtained when \(\{i\}\) and \(\{j\}\) are treated as separate singleton blocks.

Thus splitting or joining a diagonally uncoupled pair does not change the global flow:
\[
\boxed{
\Psi^\Pi_E(K,P)
\text{ is independent of the chosen compatible matching partition }\Pi.
}
\tag{53}
\]

We may therefore define
\[
\boxed{
\Psi_E(K,P)
=
\Psi^{\Pi_K}_E(K,P),
}
\tag{54}
\]
where \(\Pi_K\) is the canonical component partition of \(G_K\).

---

# 9. Lipschitz control when a common partition is available

Suppose \(K,L\) are both block diagonal over one compatible partition \(\Pi\).

For each block \(B\), write
\[
\delta_B=\|K_B-L_B\|_1.
\]
The outside laws satisfy, by (3),
\[
\left\|
p_{K_{E\setminus B}}
-
p_{L_{E\setminus B}}
\right\|_1
\le
\frac1\varepsilon
\sum_{C\ne B}\delta_C.
\tag{55}
\]

Using the direct-sum decomposition of the global edge space by the block of the added coordinate,
\[
\begin{aligned}
&\|\Psi^\Pi_E(K,P)-\Psi^\Pi_E(L,Q)\|_1\\
&\quad\le
\sum_{B\in\Pi}
w_B
\left\|
p_{K_{E\setminus B}}-
p_{L_{E\setminus B}}
\right\|_1\\
&\qquad+
\sum_{B\in\Pi}
\left\|
\widehat G(K_B,P_B)-
\widehat G(L_B,Q_B)
\right\|_1.
\end{aligned}
\tag{56}
\]

The first term is at most
\[
\frac1\varepsilon\|K-L\|_1,
\tag{57}
\]
because \(\sum_Bw_B=1\).

By (42), the second term is at most
\[
\Lambda_\varepsilon\|K-L\|_1
+
(1+2\Lambda_\varepsilon)
\sum_{B\in\Pi}\|P_B-Q_B\|_1.
\tag{58}
\]
Block pinching is trace-norm contractive on Hermitian matrices:
\[
\sum_{B\in\Pi}\|P_B-Q_B\|_1
\le
\|P-Q\|_1.
\tag{59}
\]
Hence
\[
\begin{aligned}
\|\Psi^\Pi_E(K,P)-\Psi^\Pi_E(L,Q)\|_1
&\le
\left(\frac1\varepsilon+\Lambda_\varepsilon\right)
\|K-L\|_1\\
&\quad+
(1+2\Lambda_\varepsilon)\|P-Q\|_1.
\end{aligned}
\tag{60}
\]

Since
\[
\Lambda_\varepsilon=\frac8{\varepsilon^2}+20,
\]
we may take
\[
\boxed{
C_\varepsilon^{(0)}
=
1+2\Lambda_\varepsilon
=
\frac{16}{\varepsilon^2}+41
}
\tag{61}
\]
and conclude
\[
\boxed{
\|\Psi^\Pi_E(K,P)-\Psi^\Pi_E(L,Q)\|_1
\le
C_\varepsilon^{(0)}
\bigl(\|K-L\|_1+\|P-Q\|_1\bigr).
}
\tag{62}
\]

---

# 10. Comparing incompatible canonical matchings

Let \(M_K\) and \(M_L\) be the matchings formed by the nonzero off-diagonal entries of \(K\) and \(L\). Put
\[
M_0=M_K\cap M_L.
\]

Define \(\widetilde K\) by deleting from \(K\) every off-diagonal entry on an edge of \(M_K\setminus M_L\). Define \(\widetilde L\) analogously by deleting the edges of \(M_L\setminus M_K\).

Both \(\widetilde K\) and \(\widetilde L\) remain \(\varepsilon\)-gapped. Indeed, every retained two-coordinate block is an original gapped block, while every block whose off-diagonal entry is deleted becomes diagonal with diagonal entries still lying in \([\varepsilon,1-\varepsilon]\).

Moreover:

- \(K\) and \(\widetilde K\) are block diagonal over the canonical partition of \(K\);
- \(L\) and \(\widetilde L\) are block diagonal over the canonical partition of \(L\);
- \(\widetilde K\) and \(\widetilde L\) are block diagonal over the common partition consisting of the edges in \(M_0\) and the remaining singleton coordinates.

By the refinement independence (53), the same selector \(\Psi\) is obtained in each of these compatible partitions.

## 10.1 Trace-norm control of the deleted edges

Put
\[
A=K-L.
\]
The edges in \(M_K\setminus M_L\) form a matching, and on each such edge
\[
A_{ij}=K_{ij}.
\]
Choose a Hermitian matrix \(W\), supported on those matching edges, whose \(2\times2\) block on \(\{i,j\}\) is
\[
\begin{pmatrix}
0&e^{i\arg A_{ij}}\\
e^{-i\arg A_{ij}}&0
\end{pmatrix}.
\]
Then
\[
\|W\|_{\mathrm{op}}\le1
\]
and
\[
\operatorname{tr}(WA)
=
2\sum_{\{i,j\}\in M_K\setminus M_L}|K_{ij}|.
\]
By trace-norm duality,
\[
2\sum_{\{i,j\}\in M_K\setminus M_L}|K_{ij}|
\le
\|K-L\|_1.
\]
But the left side is precisely \(\|K-\widetilde K\|_1\). Therefore
\[
\boxed{
\|K-\widetilde K\|_1\le\|K-L\|_1.
}
\tag{63}
\]
Similarly,
\[
\boxed{
\|L-\widetilde L\|_1\le\|K-L\|_1.
}
\tag{64}
\]

Furthermore,
\[
\widetilde K-\widetilde L
=
(K-L)-(K-\widetilde K)+(L-\widetilde L),
\]
so
\[
\boxed{
\|\widetilde K-\widetilde L\|_1
\le3\|K-L\|_1.
}
\tag{65}
\]

## 10.2 The final estimate

Applying the common-partition estimate (62) three times,
\[
\begin{aligned}
\|\Psi_E(K,P)-\Psi_E(L,Q)\|_1
&\le
\|\Psi_E(K,P)-\Psi_E(\widetilde K,P)\|_1\\
&\quad+
\|\Psi_E(\widetilde K,P)-\Psi_E(\widetilde L,Q)\|_1\\
&\quad+
\|\Psi_E(\widetilde L,Q)-\Psi_E(L,Q)\|_1\\
&\le
C_\varepsilon^{(0)}
\Bigl(
\|K-\widetilde K\|_1
+\|\widetilde K-\widetilde L\|_1\\
&\hspace{42mm}
+\|\widetilde L-L\|_1
+\|P-Q\|_1
\Bigr).
\end{aligned}
\]
Using (63)–(65),
\[
\|\Psi_E(K,P)-\Psi_E(L,Q)\|_1
\le
C_\varepsilon^{(0)}
\left(
5\|K-L\|_1+\|P-Q\|_1
\right).
\]
Hence
\[
\boxed{
\|\Psi_E(K,P)-\Psi_E(L,Q)\|_1
\le
C_\varepsilon
\bigl(\|K-L\|_1+\|P-Q\|_1\bigr),
}
\tag{66}
\]
with
\[
\boxed{
C_\varepsilon
=
5C_\varepsilon^{(0)}
=
\frac{80}{\varepsilon^2}+205.
}
\tag{67}
\]

The constant is independent of \(|E|\).

---

# 11. Degenerations, Borel dependence, and equivariance

If \(w_B=0\), then \(P_B=0\), and the \(B\)-component is defined as zero. There is no division singularity because
\[
\|w_BG_{K_B,R_B}\|_1=w_B\longrightarrow0,
\]
and the stronger homogeneous estimate (42) gives direct Lipschitz continuity in the unnormalized matrix \(P_B\).

The formulas involving max, min, and interval projection are continuous on every fixed two-coordinate block. Equation (53) shows that the formulas agree exactly when an off-diagonal entry reaches zero and the canonical partition changes. The global estimate (66) therefore proves that
\[
(K,P)\longmapsto\Psi_E(K,P)
\]
is globally Lipschitz on \(\mathcal M_E^\varepsilon\), and in particular Borel.

Finally, a coordinate permutation carries the canonical matching of \(K\) to the canonical matching of the permuted kernel. The local singleton rule is invariant, the two-coordinate rule is covariant under the transposition by (30)–(32), and the outside DPP laws transform by relabeling. Consequently,
\[
\Psi_E(U_\sigma KU_\sigma^*,U_\sigma PU_\sigma^*)
=
\sigma\Psi_E(K,P).
\tag{68}
\]

Thus \(\Psi_E\) is a Borel, fully coordinate-permutation-equivariant selector belonging to \(\mathcal F_E(K,P)\) for every \(K\in\mathcal M_E^\varepsilon\), and it satisfies the dimension-free estimate \((\mathrm{MATCH})\).
