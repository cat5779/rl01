PROVED

Put
\[
d_\varepsilon
=1+\left(\frac{1-2\varepsilon}{2\varepsilon}\right)^2,
\qquad
A_\varepsilon=2+(6+4/\varepsilon)d_\varepsilon.
\]
The proposed constant is valid:
\[
\boxed{C_\varepsilon^{(2)}=\max\{18,A_\varepsilon\}.}
\tag{1}
\]
In fact, the selector constructed below satisfies the stronger outgoing bound
\[
F_{K,P,\mathrm{out}}(S)\le \frac1\varepsilon p_K(S).
\]

Throughout, matrix trace norms are unnormalized, and the norm of an edge flow is the sum of its absolute edge values. Write \(E_i=e_ie_i^*\). We use the audited estimate
\[
\|p_H-p_{H'}\|_1\le2\|H-H'\|_1.
\tag{2}
\]
Empty determinants and empty-pattern probabilities equal one.

## 1. Conditioning preserves the gap and is uniformly stable

For a matrix on a coordinate set \(D\), let \(D_U\) denote the diagonal projection onto \(U\subseteq D\). Inclusion-exclusion gives
\[
p_H(A)=(-1)^{|D\setminus A|}
       \det(H-D_{D\setminus A}).
\tag{3}
\]
Indeed, both sides expand as
\(\sum_{V\subseteq D\setminus A}(-1)^{|V|}\det H_{A\cup V}\).

Fix \(J\subseteq E\), \(1\le |J|\le2\), put \(O=E\setminus J\), and take \(T\subseteq O\). Define
\[
\begin{aligned}
B_T(K)&=K_O-D_{O\setminus T},\\
M_T(K)&=K_J-K_{JO}B_T(K)^{-1}K_{OJ},\\
q_K(T)&=p_{K_O}(T).
\end{aligned}
\tag{4}
\]
For \(O=\varnothing\), the correction term is zero. Otherwise,
\[
B_T(K)
=(K_O-\tfrac12 I)+(\tfrac12 I-D_{O\setminus T}).
\]
The second summand has all singular values \(1/2\), while the first has operator norm at most \(1/2-\varepsilon\). Therefore
\[
\boxed{\|B_T(K)^{-1}\|_{\mathrm{op}}\le\varepsilon^{-1}.}
\tag{5}
\]
In particular, \(q_K(T)>0\), since (3) expresses this nonnegative probability as a nonzero signed determinant. The block determinant formula gives
\[
p_K(T\cup A)=q_K(T)p_{M_T(K)}(A),
\qquad A\subseteq J.
\tag{6}
\]

We verify that the conditional kernel retains the original gap:
\[
\varepsilon I_J\preceq M_T(K)\preceq(1-\varepsilon)I_J.
\tag{7}
\]
Condition one coordinate at a time. For a gapped block matrix
\[
H=\begin{pmatrix}a&c^*\\c&D\end{pmatrix},
\]
the occupied and absent conditional kernels, obtained from (3), are respectively
\[
D-\frac{cc^*}{a},
\qquad
D+\frac{cc^*}{1-a}.
\]
The first is at most \(D\preceq(1-\varepsilon)I\), and
\[
x^*(D-cc^*/a)x
=\min_{z\in\mathbb C}(z,x)^*H(z,x)
\ge\varepsilon\|x\|^2.
\]
The second is at least \(D\succeq\varepsilon I\). Applying the same lower-bound argument to \(I-H\) shows that the complement of the second is at least \(\varepsilon I\), proving its upper bound. Successive Schur complementation—equivalently, Gaussian elimination of \(B_T(K)\)—gives exactly (4). This proves (7).

We also have the pointwise and probability-averaged estimates
\[
\boxed{
\begin{aligned}
\|M_T(K)-M_T(L)\|_1
&\le d_\varepsilon\|K-L\|_1,\\
\sum_Tq_K(T)\|M_T(K)-M_T(L)\|_1
&\le d_\varepsilon\|K-L\|_1.
\end{aligned}}
\tag{8}
\]
To prove them, set \(K_s=K+s(L-K)\), \(H=L-K\), and, in block order \(J,O\),
\[
W_s=[\,I_J,\,-K_{s,JO}B_T(K_s)^{-1}\,].
\]
Direct differentiation of (4) gives
\[
\frac{d}{ds}M_T(K_s)=W_sHW_s^*.
\]
Since
\[
\|K_{s,JO}\|_{\mathrm{op}}
\le\|K_s-\tfrac12I\|_{\mathrm{op}}
\le\tfrac12-\varepsilon,
\]
equation (5) yields
\[
\|W_s\|_{\mathrm{op}}^2
=1+\|K_{s,JO}B_T(K_s)^{-1}\|_{\mathrm{op}}^2
\le d_\varepsilon.
\]
Thus
\[
\|W_sHW_s^*\|_1
\le\|W_s\|_{\mathrm{op}}^2\|H\|_1
\le d_\varepsilon\|H\|_1.
\]
Integrating proves the first estimate in (8); averaging against the probability vector \(q_K\) proves the second.

If \(P\) is supported on \(J\), its rows and columns outside \(J\) vanish. Consequently,
\[
M_T(K+hP)=M_T(K)+hP_J,
\]
and differentiating (6) gives
\[
\boxed{
b_{K,P}(T\cup A)
=q_K(T)b_{M_T(K),P_J}(A).
}
\tag{9}
\]
The outside probability vector does not change with \(h\).

## 2. An explicit positive two-site selector

Write
\[
M=\begin{pmatrix}a&z\\\bar z&d\end{pmatrix},
\qquad
R=\begin{pmatrix}u&w\\\bar w&t\end{pmatrix},
\qquad u+t=1,
\]
where \(M\) has gap \(\varepsilon\) and \(R\) is a rank-one orthogonal projector. Set
\[
\eta=ad-|z|^2,
\]
\[
(p_0,p_1,p_2,p_{12})
=(1-a-d+\eta,\ a-\eta,\ d-\eta,\ \eta),
\]
and
\[
\gamma
=ud+ta-2\operatorname{Re}(\bar zw)
=\operatorname{tr}(R\operatorname{adj}M).
\]
The eigenvalues of \(\operatorname{adj}M\) are those of \(M\) in reverse order, so
\[
\varepsilon\le\gamma\le1-\varepsilon.
\tag{10}
\]
Since \(\det R=0\), differentiating the four probabilities gives
\[
b_{M,R}=(\gamma-1,\ u-\gamma,\ t-\gamma,\ \gamma).
\tag{11}
\]

Every flow with this divergence has the form
\[
\begin{aligned}
f(\varnothing,1)&=u-x,
&
f(\varnothing,2)&=t-\gamma+x,\\
f(\{1\},2)&=\gamma-x,
&
f(\{2\},1)&=x.
\end{aligned}
\tag{12}
\]
Its divergence is exactly (11), and its total mass is \(u+t=1\).

Put \(c=1/\varepsilon\), and define
\[
\ell=\max\{0,\gamma-t,\gamma-cp_1\},
\qquad
U=\min\{u,\gamma,cp_2\}.
\tag{13}
\]
We prove that this interval is nonempty and encodes all nonnegativity and singleton capacity constraints. The empty-state capacity holds independently of \(x\).

Indeed,
\[
0\preceq M+\varepsilon R\preceq I.
\]
Nonnegativity of its probabilities, using rank-one affinity, gives
\[
1-\gamma\le cp_0,\qquad
\gamma-u\le cp_1,\qquad
\gamma-t\le cp_2.
\tag{14}
\]
If \(\lambda,\mu\in[\varepsilon,1-\varepsilon]\) are the eigenvalues of \(M\), then
\[
\begin{aligned}
p_1+p_2
&=\lambda(1-\mu)+\mu(1-\lambda)\\
&\ge\varepsilon(1-\mu)+\varepsilon\mu
=\varepsilon.
\end{aligned}
\]
Hence \(\gamma\le1\le c(p_1+p_2)\).

Every lower candidate in (13) is at most every upper candidate. For \(0\), this is positivity. For \(\gamma-t\), use \(\gamma\le u+t\), \(t\ge0\), and (14). For \(\gamma-cp_1\), use (14), \(p_1\ge0\), and \(\gamma\le c(p_1+p_2)\). Therefore \(\ell\le U\).

For \(x\in[\ell,U]\), the inequalities
\[
0\le x\le\min(u,\gamma),\qquad x\ge\gamma-t
\]
make all four edges nonnegative. The remaining interval constraints give
\[
\gamma-x\le cp_1,\qquad x\le cp_2.
\]
The empty outgoing mass is \(1-\gamma\le cp_0\), and the full state has no outgoing edges. Thus
\[
f_{\mathrm{out}}(A)\le\varepsilon^{-1}p_M(A)
\quad\text{for every }A\subseteq\{1,2\}.
\tag{15}
\]

Choose
\[
x_0=ud-\operatorname{Re}(\bar zw)
=\tfrac12(\gamma+ud-ta),
\]
\[
\boxed{x=\min\{U,\max\{\ell,x_0\}\},}
\tag{16}
\]
and then use (12). Denote the resulting flow by \(f_{M,R}\).

Under interchange of the two coordinates, \(\gamma\) is unchanged and
\[
\ell'=\gamma-U,\qquad
U'=\gamma-\ell,\qquad
x_0'=\gamma-x_0.
\]
Clipping therefore gives \(x'=\gamma-x\), precisely the transformation required for (12) to commute with coordinate interchange.

For \(R=E_1\), (13) forces \(x=d\), giving only
\[
f(\varnothing,1)=1-d,\qquad f(\{2\},1)=d.
\]
For \(R=E_2\), it forces \(x=0\), giving only
\[
f(\varnothing,2)=1-a,\qquad f(\{1\},2)=a.
\]
Thus the rule includes both coordinate limits.

## 3. The two-site Lipschitz estimate

Consider \((M,R)\) and \((N,Q)\), and write
\[
\delta_M=\|M-N\|_1,\qquad
\delta_R=\|R-Q\|_1.
\]
Use primes for the second pair and \(\Delta\) for differences.

The traceless Hermitian two-by-two matrix \(R-Q\) has operator norm \(\delta_R/2\). Hence
\[
|\Delta u|=|\Delta t|\le\delta_R/2.
\]
The adjugate is linear in dimension two, and
\[
\|\operatorname{adj}H\|_{\mathrm{op}}
=\|H\|_{\mathrm{op}}
\]
for Hermitian two-by-two \(H\). Splitting the difference of
\(\operatorname{tr}(R\operatorname{adj}M)\), using \(\|R\|_1=1\) and
\(\|\operatorname{adj}N\|_{\mathrm{op}}\le1\), gives
\[
|\Delta\gamma|\le\delta_M+\delta_R.
\tag{17}
\]

A probability-vector difference has total mass zero, so any single coordinate has absolute value at most half its sum norm. Equation (2) gives
\[
|\Delta p_1|,\ |\Delta p_2|\le\delta_M.
\]
Also,
\[
ud-ta-u'd'+t'a'
=u(d-d')-t(a-a')+(u-u')(d'+a').
\]
Its absolute value is at most \(\delta_M+\delta_R\), since \(u+t=1\) and \(a'+d'\le2\). By (16) and (17),
\[
|\Delta x_0|\le\delta_M+\delta_R.
\]

Maxima and minima are 1-Lipschitz for the maximum norm of their arguments. Applying this to (13) gives
\[
|\Delta\ell|
\le(1+c)\delta_M+\tfrac32\delta_R,
\qquad
|\Delta U|
\le c\delta_M+\delta_R.
\]
Applying it again to (16) yields
\[
|\Delta x|
\le(1+c)\delta_M+\tfrac32\delta_R.
\]
Finally, (12) implies
\[
\begin{aligned}
\|f_{M,R}-f_{N,Q}\|_1
&\le2|\Delta u|+2|\Delta\gamma|+4|\Delta x|\\
&\le(6+4/\varepsilon)\delta_M+9\delta_R.
\end{aligned}
\]
Thus
\[
\boxed{
\|f_{M,R}-f_{N,Q}\|_1
\le(6+4/\varepsilon)\|M-N\|_1+9\|R-Q\|_1.
}
\tag{18}
\]

## 4. Lifting and compatibility with coordinate directions

Let \(J\) be any two-set containing \(\operatorname{supp}(P)\), and put \(O=E\setminus J\). Define
\[
\boxed{
F^J_{K,P}(T\cup A,i)
=q_K(T)f_{M_T(K),P_J}(A,i)
}
\tag{19}
\]
for \(T\subseteq O\), \(A\subseteq J\), and \(i\in J\setminus A\). Give every edge direction outside \(J\) mass zero. The two-site interchange identity makes (19) independent of the ordering of \(J\).

Every factor is nonnegative. Equation (9) and the local divergence identity give the required divergence at every configuration \(T\cup A\). Since each conditional flow has mass one,
\[
\sum_{S,i\notin S}F^J_{K,P}(S,i)
=\sum_Tq_K(T)=1.
\]
Equations (6) and (15) give
\[
\begin{aligned}
F^J_{K,P,\mathrm{out}}(T\cup A)
&\le\varepsilon^{-1}q_K(T)p_{M_T(K)}(A)\\
&=\varepsilon^{-1}p_K(T\cup A).
\end{aligned}
\tag{20}
\]

For a coordinate projector \(E_i\), define
\[
F_K^{(i)}(S,i)=p_{K_{E\setminus\{i\}}}(S),
\qquad
F_K^{(i)}(S,j)=0\quad(j\ne i).
\tag{21}
\]
The one-site versions of (6) and (9) verify its divergence. It is nonnegative of mass one. Conditional absence of \(i\) has probability at least \(\varepsilon\), by (7), so it also satisfies (20). Equation (2) and trace-norm compression give
\[
\boxed{
\|F_K^{(i)}-F_L^{(i)}\|_1\le2\|K-L\|_1.
}
\tag{22}
\]

For completeness, any nonnegative flow with divergence \(b_{K,P}\) satisfies
\[
\sum_{S:j\notin S}F(S,j)
=\sum_{S:j\in S}b_{K,P}(S)
=P_{jj}.
\tag{23}
\]
The first equality follows by cancellation of edges not changing membership of \(j\); the second differentiates the DPP marginal
\(\mathbb P(j\in X)=K_{jj}\).

For \(P=E_i\), equation (23) forces all directions except \(i\) to vanish. At a configuration \(S\) not containing \(i\), the divergence then forces exactly (21). Consequently, (21) is unique, and **every auxiliary two-set lift (19) agrees with it**.

Define the global selector by (19) on a genuine two-coordinate support, and by (21) on a coordinate support. This also covers \(n=1\). Whenever a two-set contains the support, the global selector equals its lift (19).

Now suppose both \(P,Q\) are supported in the same two-set \(J\). Write
\[
\delta_K=\|K-L\|_1,\qquad
\delta_P=\|P-Q\|_1.
\]
Splitting the products in (19), using unit mass of the local flows, gives
\[
\begin{aligned}
\|F_{K,P}-F_{L,Q}\|_1
&\le\|q_K-q_L\|_1\\
&\quad+\sum_Tq_K(T)
 \|f_{M_T(K),P_J}-f_{M_T(L),Q_J}\|_1\\
&\le2\delta_K
 +(6+4/\varepsilon)d_\varepsilon\delta_K
 +9\delta_P\\
&=A_\varepsilon\delta_K+9\delta_P.
\end{aligned}
\tag{24}
\]
Here we used (2), (8), and (18). Restricting \(P-Q\) to \(J\) leaves its trace norm unchanged.

The outside-pattern sum is a probability average. No factor counting the patterns appears.

## 5. Changing supports, Borel dependence, and covariance

If the union of the supports has at most two elements, (24) applies; for \(n=1\), use (22).

If the supports are disjoint, \(PQ=0\) and \(\|P-Q\|_1=2\). Nonnegative unit flows have sum-norm distance at most two, so
\[
\|F_{K,P}-F_{L,Q}\|_1\le\|P-Q\|_1.
\tag{25}
\]

The remaining case consists of two genuine two-coordinate supports meeting only at \(i\). Set
\[
\alpha=1-P_{ii},\qquad \beta=1-Q_{ii}.
\]
For rank-one projectors,
\[
\|P-Q\|_1=2\sqrt{1-\operatorname{tr}(PQ)}.
\]
Indeed, \(P-Q\) has at most two nonzero eigenvalues, which are \(s,-s\), and
\[
2s^2=\operatorname{tr}((P-Q)^2)=2-2\operatorname{tr}(PQ).
\]
In the present support configuration,
\[
\begin{aligned}
\|P-Q\|_1&=2\sqrt{\alpha+\beta-\alpha\beta},\\
\|P-E_i\|_1&=2\sqrt\alpha,\\
\|Q-E_i\|_1&=2\sqrt\beta.
\end{aligned}
\]
Since
\[
\alpha+\beta-\alpha\beta\ge\max\{\alpha,\beta\},
\]
we have
\[
\|P-E_i\|_1+\|Q-E_i\|_1
\le2\|P-Q\|_1.
\tag{26}
\]

Compare each direction with \(E_i\) at its own kernel using (24), and compare the coordinate flows using (22). The triangle inequality gives
\[
\begin{aligned}
\|F_{K,P}-F_{L,Q}\|_1
&\le9\|P-E_i\|_1
 +2\delta_K
 +9\|Q-E_i\|_1\\
&\le2\delta_K+18\delta_P.
\end{aligned}
\tag{27}
\]
Together, (24), (25), and (27) prove
\[
\boxed{
\|F_{K,P}-F_{L,Q}\|_1
\le C_\varepsilon^{(2)}
\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
}
\]
with (1), including degeneration to coordinate projectors and comparisons across different support strata.

For every fixed finite \(E\), this global Lipschitz estimate makes the selector continuous on its entire domain, hence Borel.

Finally, let \(\sigma\) be a coordinate permutation, represented by \(U_\sigma\). Principal blocks, the diagonal masks in (4), matrix inversion, and exact probabilities commute with relabeling. The local clipping rule commutes with interchange of its two coordinates, as verified after (16), and (21) is manifestly covariant. Therefore
\[
F_{U_\sigma K U_\sigma^*,\,U_\sigma P U_\sigma^*}
(\sigma S,\sigma i)
=
F_{K,P}(S,i).
\]
Every formula uses \(P\) itself; no choice of a representing vector or its phase is made.

Thus the selector satisfies nonnegativity, exact divergence, normalization, the stronger capacity \(p_K/\varepsilon\), Borel dependence, permutation covariance, and the stated dimension-free modulus. All inverse estimates are controlled by \(\varepsilon\), not by the least configuration probability. This proves the restricted theorem only. \(\square\)

