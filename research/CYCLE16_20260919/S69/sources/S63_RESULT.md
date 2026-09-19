# S63 — Cycle11 result, second research round

## Verdict and exact scope

**PROVED (computer-assisted, with outward interval and exact-rational certificates):** for the actual sine Toeplitz compression, with

\[
\rho=\frac13,\qquad c=\frac{19}{20},\qquad
J=\left[\frac{21}{1000},\frac3{125}\right]=[.021,.024],
\]

the complete-configuration entropy satisfies, for every integer \(n\ge22\),

\[
\boxed{\quad H_n''(a)\le-\frac{n}{25}+399
\quad\text{for every }a\in J.\quad} \tag{T}
\]

Consequently the actual entropy rate exists and, for every \(a_0,a_1\in J\) and \(0\le\lambda\le1\),

\[
\boxed{\quad
\operatorname{Gap}_\lambda h_{1/3,19/20}
\ge\frac1{50}\lambda(1-\lambda)(a_1-a_0)^2.
\quad} \tag{C}
\]

This is a **strictly scoped partial theorem**. The benchmark asked for the entire interval \([.02,.03]\); the theorem proves the proper subinterval \([.021,.024]\), of fixed width .003. It does not contain the balanced shift \(a_*=.025\). The full benchmark interval and the ultimate all-density, all-contrast, whole-legal-interval objective remain **INCOMPLETE**. No counterexample to those objectives is claimed.

A further **PROVED** corollary, by an explicitly density-changing complement transformation, gives (T) for \(\rho=2/3\) on \([.026,.029]\). This does not extend the \(\rho=1/3\) theorem to its upper half.

The new reusable mechanism is **guarded posterior order + positive-semidefinite Fisher allocation + an actual-law variational polynomial certificate**. It does not require a cyclic-to-Toeplitz approximation, an observation-Hessian estimate, or a spatial tail truncation. The local finite witness is not itself a curvature sign scan.

All logarithms are natural. Thus the displayed constants use nats.

## 1. Dependency ledger

The nine required packet files were read in the specified order. `sources/S61_REVIEW.md` was also checked. `SOURCE_STATUS.md` governs inherited facts. It states that the accepted universal whole-interval baseline remains \(c\le37/40\), that SA02 has no \(c=.95\) sign, that S55's bridge is half-density only, and that S61's completed result is restricted to its frozen half-density corrected-clock task.

The only reviewed mathematical interfaces used below are the finite actual-law determinant/score identities and conditional score martingale from `sources/SA02_FULL_BLOCK.md` and `sources/SA02_REVIEW.md`. Their hypotheses are a finite DPP and a strict spectral gap. Here these hold uniformly because \(0\preceq Q_{\rho,n}\preceq I\) and \(a\in J\subset(0,1-c)\). Short derivations are included to fix all normalizations.

The earlier S63 response is **author-only** and is not used as an inherited theorem. No S55 general-density bridge, no S61 generalization, and no QWE06 true-law obstruction is assumed. No unfinished S59/S60 work was sought.

| Claim | Status | Role and unpaid scope |
|---|---|---|
| Posterior order bounds with both likelihood ratios | PROVED | Controls actual conditional pair tables; valid at ordinary density |
| Flat-diagonal scalar pair envelope | PROVED | Gives an explicit one-dimensional bound, not pairwise payment by 1 |
| PSD Fisher-allocation/variational interface | PROVED | Pays signed pair terms jointly and localizes without a curvature error |
| Actual-law nilpotent polynomial evolution | PROVED | Retains all probability derivatives, including acceleration |
| Three finite certificate interfaces in Section 7 | PROVED, computer-assisted | Continuum posterior bounds and the complete 22-site actual law |
| Theorem (T) and chord theorem (C) | PROVED, partial scope | Entire fixed subinterval J, all n >= 22 / the true rate |
| Density-complement corollary | PROVED | Density 2/3 on [.026,.029], not density 1/3 there |
| Full [.02,.03] benchmark | INCOMPLETE | No payment certificate supplied on the two remaining pieces |
| Ultimate all-rho/all-c/all-a theorem | INCOMPLETE | No general sign assertion |

The status and review files are public on branch `research/sa-cycle11-pr128-20260918` of `cat5779/rl01`. This manuscript does not edit repository-wide status or assert independent acceptance of its own result.

## 2. Exact true-law model and unequal noises

Let \(Q\) be a real orthogonal projection on \(\ell^2(\mathbb Z)\), with constant diagonal \(Q_{ii}=\rho\). Let \(X\) be its DPP. Given \(X\), independently generate

\[
\Pr(Y_i=1\mid X)=a+cX_i,
\qquad u=a,\quad v=a+c,\quad 0<u<v<1.
\]

For every finite set \(S\),

\[
E\prod_{i\in S}Y_i
=\sum_{T\subseteq S}a^{|S|-|T|}c^{|T|}\det Q_T
=\det(aI+cQ)_S. \tag{2.1}
\]

Thus the restriction to any finite \(V\) is exactly \(\operatorname{DPP}(aI+cQ_V)\). For the sine kernel, the infinite operator is the Fourier multiplier by the indicator of an arc of length \(2\pi\rho\). Its matrix entries are exactly the stated sine coefficients. This proves both the projection property of the **infinite** operator and the contraction property of its finite compressions.

In particular, (2.1) is an exact representation of the true Toeplitz output. The finite compression \(Q_V\) is never called a projection.

The two likelihood ratios and two channel variances are

\[
d_+=\frac vu,\qquad d_-=\frac{1-v}{1-u},\qquad
\beta_0=u(1-u),\quad\beta_1=v(1-v). \tag{2.2}
\]

Here \(d_-<1<d_+\). The ratios are not identified with each other or replaced by a balanced normalization.

For any finite latent law independent of \(a\), the complete-data score is

\[
S=\sum_i\frac{Y_i-(u+cX_i)}{(u+cX_i)(1-u-cX_i)}.
\]

Conditional on \(X\), its summands have mean zero and are independent. The actual output score is \(E[S\mid Y]\), so conditional Jensen gives

\[
J_V:=E(\partial_a\log p_a(Y))^2
\le \sum_{i\in V}\left\{\frac{1-E X_i}{\beta_0}+\frac{E X_i}{\beta_1}\right\}.
\]

For constant density this is

\[
\boxed{J_V\le |V|\,d_{\rho,c}(a),\qquad
 d_{\rho,c}(a)=\frac{1-\rho}{\beta_0}+\frac\rho{\beta_1}.} \tag{2.3}
\]

This is an upper bound for the **common-shift** Fisher information, not an identification with diagonal Fisher information or count Fisher information.

### The density-odd term is explicit

Write \(a_*=(1-c)/2\), \(s=a-a_*\), \(b=(1-c^2)/4\), and \(B=b-s^2\). Then

\[
\beta_0=B+cs,\qquad\beta_1=B-cs,
\qquad
\boxed{d_{\rho,c}(a)=\frac{B+c(2\rho-1)s}{B^2-c^2s^2}.} \tag{2.4}
\]

The odd numerator \(c(2\rho-1)s\) vanishes at half density or at balance, but not on the ordinary-density interval proved here. The final certificate pays the **whole rational function (2.4)**. It never suppresses this term. The actual-law polynomial below likewise has a nonzero odd coefficient.

## 3. Posterior order with a finite observed guard

### 3.1 Projection posterior formula

For a finite collection of observations, Bayes' rule multiplies the latent DPP weight by \(\prod_j D_j^{X_j}\), where \(D_j=d_+\) for an observed 1, \(D_j=d_-\) for an observed 0, and \(D_j=1\) at unobserved sites.

Let \(\mathcal H=\operatorname{Ran}Q\). The compression

\[
M_D=(QDQ)|_{\mathcal H}
\]

is bounded and strictly positive, since the diagonal entries of \(D\) are bounded above and away from zero. The posterior kernel is

\[
P_D=D^{1/2}Q M_D^{-1}Q D^{1/2}. \tag{3.1}
\]

It is the orthogonal projection onto \(D^{1/2}\mathcal H\). The identity \(P_D^2=P_D\) follows by inserting \(QDQ=M_D\) on \(\mathcal H\). To verify that it is the posterior kernel, apply the finite DPP generating identity \(E\prod_j(1+f_jX_j)=\det(I+\operatorname{diag}(f)Q)\) to the finite support of the likelihood and additional test variables, and divide by the likelihood normalizer. The determinant quotient equals the generating determinant with kernel (3.1), by \(\det(I+AB)=\det(I+BA)\). Thus this is the actual posterior, not a comparison law.

### 3.2 One-site bounds

Leave site \(i\) unobserved and put \(q_i=\Pr(Y_i=1\mid\text{the other observations})\). On \(\mathcal H\), the two comparison operators are

\[
d_\pm I+(1-d_\pm)(Qe_i)(Qe_i)^*.
\]

They sandwich the actual Gram operator. Inversion reverses positive-operator order, and the rank-one inverse formula gives

\[
\boxed{
L_*=a+c\frac\rho{\rho+d_+(1-\rho)}
\le q_i\le
U_*=a+c\frac\rho{\rho+d_-(1-\rho)}.
} \tag{3.2}
\]

The inversion-order assertion follows, for example, by conjugating \(0<A\le B\) by \(A^{-1/2}\), inverting the resulting operator \(\ge I\), and conjugating back.

### 3.3 Two-site guarded bounds

Let \(T=\{i,j\}\), let \(O\) be a finite observed guard disjoint from \(T\), and write \(E=T\cup O\). Fix the guard word \(z\). Define \(D_E\) to have entries 1 on \(T\), and the appropriate \(d_+,d_-\) on \(O\). For \(d>0\), put

\[
\mathcal B_d(E,z)
=
\left[Q_E\{dI+(D_E-dI)Q_E\}^{-1}\right]_{T,T}. \tag{3.3}
\]

Then the actual latent posterior compression \(B_T\), after **all** the other observations in the finite volume, obeys

\[
\boxed{\mathcal B_{d_+}(E,z)\preceq B_T
\preceq\mathcal B_{d_-}(E,z).} \tag{3.4}
\]

To prove this, replace every unknown field outside \(E\) first by \(d_+\), then by \(d_-\). The actual field is between these bounds; an unobserved field is exactly 1 and is included. Apply inverse order to the Gram operators. If \(A:\mathcal H\to\mathbb R^E\) is coordinate restriction, \(AA^*=Q_E\), and the push-through identity is

\[
A\{dI+A^*(D_E-dI)A\}^{-1}A^*
=Q_E\{dI+(D_E-dI)Q_E\}^{-1}.
\]

This proves (3.3)–(3.4) even when \(Q_E\) is singular. The constant fields on infinitely many sites are only bounded **comparison operators**; no infinite-product likelihood or positive-probability infinite observation word is asserted.

Both functions \(d_+(a)=1+c/a\) and \(d_-(a)=1-c/(1-a)\) decrease with \(a\). Hence both bounding matrices in (3.4) increase in Loewner order with \(a\). On a parameter cell \([a_-,a_+]\), the uniform enclosure is therefore

\[
\mathcal B_{d_+(a_-)}(a_-,z)\preceq B_T(a)
\preceq\mathcal B_{d_-(a_+)}(a_+,z). \tag{3.5}
\]

This will certify intervals directly, not infer them from fixed-volume continuity.

## 4. A scalar conditional-table envelope

For a conditional two-site table write

\[
A=p_{00},\quad B=p_{10},\quad C=p_{01},\quad D=p_{11},\qquad
s=BC-AD\ge0.
\]

Temporarily these capital letters denote atoms, not an operator. All atoms are positive in the strict channel. Define

\[
\alpha(A,B,C,D)
=\frac{\log(BC/AD)}{s(A^{-1}+B^{-1}+C^{-1}+D^{-1})}, \tag{4.1}
\]

with its continuous value 1 at independence. Set \(R=BC/(AD)\), \(x=R-1\), and \(d=A+D\). Direct algebra gives

\[
\alpha=\frac{R\log R}{(R-1)(1+d(R-1))}
=\frac{(1+x)\log(1+x)/x}{1+dx}. \tag{4.2}
\]

Suppose all four one-site conditional probabilities belong to \([L,U]\), where \(L<1/2<U\), and set

\[
\ell=\frac L{1-L},\qquad r=\frac U{1-U}.
\]

Negative association implies, in particular,

\[
B,C\le rA,\qquad D\ge\ell B,\ell C. \tag{4.3}
\]

The following explicit scalar bound is **PROVED**:

\[
\boxed{
\alpha\le\max\left\{1,
\sup_{1\le R\le\min(r^2,\ell^{-2})}
\frac{R\log R(1+r+r\ell+\ell R)}
{(R-1)\{r+R(1+\ell+r\ell)\}}
\right\}.} \tag{4.4}
\]

Only feasible \(R\le r/\ell\) are relevant; the displayed upper endpoint is no larger than \(r/\ell\).

**Proof.** By interchanging the sites, assume \(C\ge B\), and rescale \(B=1,C=t\ge1\). At fixed \(R\), constraints (4.3) say

\[
1\le t\le r/(\ell R),\quad A\ge t/r,\quad D\ge\ell t,
\quad AD=t/R.
\]

Maximizing (4.2) is equivalent to minimizing \((A+D)/(1+t)\). For fixed \(t\), minimize \(A+t/(RA)\) over \(t/r\le A\le1/(\ell R)\). If \(R\le\min(r^2,\ell^{-2})\), the subsequent minimum over \(t\) is attained when both displayed atom constraints saturate. One way to check the last statement is to assume \(r\ell\le1\): until \(t=r^2/R\) the minimum is \(2\sqrt{t/R}/(1+t)\), decreasing for \(t\ge1\); thereafter it is \((t/r+r/R)/(1+t)\), whose derivative has the sign of \(R-r^2\). The other regime exchanges the two diagonal atoms. Thus

\[
d\ge\frac{1+r\ell}{1+r+r\ell+\ell R},
\]

which gives the fraction in (4.4). For larger \(R\), the minimum is attained at \(t=1\), so \(B=C\) and \(d\ge1/(1+\sqrt R)\). Then \(\alpha\le\sqrt R\log R/(R-1)\le1\); the final inequality is \(\log z\le(z-z^{-1})/2\) with \(z=\sqrt R\). This proves (4.4). At \(R=1\), take the limit. \(\square\)

Using (3.2) in (4.4) gives a density-dependent global pair envelope. It is not the false claim that each pair can be paid by its own unit Fisher budget.

## 5. Reusable PSD Fisher-allocation interface

This theorem only needs a finite strict-channel DPP \(K=aI+cQ_V\) with \(0\preceq Q_V\preceq I\). Projection structure is needed to **supply** the posterior envelopes, not for the following inference.

Put

\[
G_V(y)=\{K-\operatorname{diag}(1-y)\}^{-1},\qquad Z_i=(G_V)_{ii},
\quad F_V=\sum_i E Z_i^2.
\]

The determinant mass formula and differentiation in independent diagonal shifts give

\[
Z_i=\partial_{a_i}\log p,
\quad E Z_iZ_j=E|G_{ij}|^2\ (i\ne j),
\quad J_V=F_V+\sum_{i\ne j}E|G_{ij}|^2. \tag{5.1}
\]

The actual entropy Hessian is

\[
\boxed{H_V''=\sum_{i\ne j}E_{Y_{V\setminus\{i,j\}}}
\log\frac{p_{10}p_{01}}{p_{00}p_{11}}-J_V.} \tag{5.2}
\]

Indeed, \(p''\) is the sum of the mixed derivatives \(\partial_{a_i a_j}p\), \(i\ne j\); the unmixed derivatives vanish by multi-affinity. Substituting in \(H''=-\sum(p')^2/p-\sum p''\log p\) and summing the four pair words gives (5.2). This explicitly retains probability acceleration.

For a fixed pair-rest word,

\[
E[|G_{ij}|^2\mid\text{rest}]
=s(A^{-1}+B^{-1}+C^{-1}+D^{-1}). \tag{5.3}
\]

This follows by inverting the conditional masked 2 by 2 matrix: its off-diagonal inverse has squared modulus \(s/p_{bc}^2\). Thus \(\alpha\) is exactly the ratio of the pair term in (5.2) to (5.3).

### Inputs of the allocation tool

Supply a scalar \(C_0(a)\ge1\) such that every actual conditional pair has \(\alpha\le C_0\). Select a graph of pairs \(e=\{i,j\}\). For each selected pair supply a guard \(O_e\), disjoint from \(e\), and a guard-measurable nonnegative improvement \(\delta_e\) such that

\[
\alpha_e\le C_0-\delta_e(Y_{O_e}).
\]

Supply nonnegative guard-measurable diagonal allocations \(w_{e,i},w_{e,j}\) satisfying, pointwise,

\[
\sum_{e\ni i}w_{e,i}\le C_0,
\qquad B_e=
\begin{pmatrix}w_{e,i}&\delta_e\\\delta_e&w_{e,j}\end{pmatrix}\succeq0. \tag{5.4}
\]

Let \(A_e\subseteq V\) contain both the pair and its guard. Then the proved output is

\[
\boxed{
H_V''\le (C_0-1)J_V-
\sum_e E[Z_{A_e,e}^{\mathsf T}B_e Z_{A_e,e}],
} \tag{5.5}
\]

where \(Z_{A_e,e}\) is the vector of the two actual marginal scores in \(A_e\).

**Proof.** Equations (5.1)–(5.3) give

\[
H_V''\le (C_0-1)J_V-C_0F_V
-2\sum_e E[\delta_e|G_{ij}|^2].
\]

Because \(\delta_e\) depends on neither target bit, normalization of the conditional pair table gives

\[
E[\delta_e|G_{ij}|^2]=E[\delta_e Z_iZ_j]. \tag{5.6}
\]

This is an actual-law identity. It does not require pointwise positivity of \(Z_iZ_j\). Allocation (5.4) now bounds the last two terms by \(-\sum_e E[Z_e^{\mathsf T}B_eZ_e]\), without using a site diagonal more than once.

Finally marginalization of the same parametric law gives the score martingale

\[
E[Z_{V,e}\mid Y_{A_e}]=Z_{A_e,e}.
\]

Since \(B_e\) is measurable in that conditioning and is PSD, conditional Jensen yields (5.5). Equivalently, the discarded difference is the trace of \(B_e\) times a conditional covariance and is nonnegative. There is no signed-potential Hessian error to estimate. \(\square\)

### A variational version that is safe under moving probabilities

Let \(f_e\) be any fixed two-vector function on the local words, and put \(g_e=B_e f_e\). Completing the square gives

\[
Z^{\mathsf T}B_e Z\ge2Z^{\mathsf T}B_ef_e-f_e^{\mathsf T}B_ef_e.
\]

For a function \(g\), let \(\Delta_i g=g(y_i=1)-g(y_i=0)\), holding the other bits fixed. The multi-affine score identity gives

\[
E_a[Z_i g(Y)]=E_a[\Delta_i g(Y)].
\]

Consequently (5.5) remains true with each local quadratic expectation replaced by

\[
\boxed{
P_e(a)=E_a V_e(a,Y),\qquad
V_e=2\{\Delta_i(B_ef_e)_i+\Delta_j(B_ef_e)_j\}
-f_e^{\mathsf T}B_ef_e.} \tag{5.7}
\]

The expectation is always under \(p_a\), not under the law at which \(f_e\) was chosen. No derivative of a comparison law is discarded: the inference is a pointwise variational inequality at each \(a\), not differentiation of an entropy comparison.

## 6. The local witness and exact evolution of its actual law

Take

\[
C_0(a)=\frac{261}{200}+\frac{51}{10}a,
\qquad A=\{0,\ldots,21\},\qquad T=\{10,11\},
\]

and guard \(O=\{6,7,8,9,12,13,14,15\}\). Its bit order is precisely the increasing order displayed. For each guard word \(z=\sum_{r=0}^7 2^r y_{O_r}\), use the integer pair \((L_z,U_z)\) listed in Appendix A and define

\[
c_z(a)=100\left\{\left(\frac3{100}-a\right)\frac{L_z}{10000}
+\left(a-\frac1{50}\right)\frac{U_z}{10000}\right\},
\quad\delta_z(a)=C_0(a)-c_z(a),
\]

\[
B_z(a)=\begin{pmatrix}C_0(a)/2&\delta_z(a)\\
\delta_z(a)&C_0(a)/2\end{pmatrix}. \tag{6.1}
\]

All these matrices are PSD on \(J\); this is an exact rational endpoint check because their two eigenvalues are affine in \(a\).

Choose the fixed test vector from the actual 22-site law at \(a_*=1/40\):

\[
f_i(y)=(2y_i-1)\left(1+\frac{p_{a_*}(y^i)}{p_{a_*}(y)}\right),
\qquad i=10,11. \tag{6.2}
\]

This equals its diagonal-shift score, but only its being a fixed function is needed in (5.7). Since \(B_z(a)\) is affine, so is the potential:

\[
V(a,y)=V_0(y)+(a-a_*)V_1(y).
\]

For every coordinate define the constant linear operator on the complete probability vector by

\[
(D_i p)(y)=(2y_i-1)\{p(y)+p(y^i)\}.
\]

The \(D_i\) commute, \(D_i^2=0\), and \(\|D_i\|_{1\to1}=2\). Put \(D=\sum_{i=0}^{21}D_i\). Exact multi-affinity gives

\[
\boxed{
p_{a_*+h}=\prod_i(I+hD_i)p_{a_*}
=e^{hD}p_{a_*}
=\sum_{k=0}^{22}\frac{h^k}{k!}D^kp_{a_*}.} \tag{6.3}
\]

Thus every moving weight, its first derivative, its acceleration, and all higher terms remain in the calculation.

Set \(t=200a-5\), \(q_k=(D/200)^kp_{a_*}/k!\). For \(|h|\le1/200\),

\[
\|q_k\|_1\le\frac{(11/50)^k}{k!}.
\]

The complete-word certificate verifies \(\|V_0\|_\infty\le1500\), \(\|V_1\|_\infty\le10000\). Truncating (6.3) after \(k=8\) therefore has error at most

\[
1550\frac{(11/50)^9}{9!}\frac1{1-(11/50)/10}
<10^{-8}<10^{-6}. \tag{6.4}
\]

This is a rigorous whole-vector tail bound, not a typical-word or typical-count argument.

## 7. Finite certificates and their verification

The following statements are all **PROVED by the supplied terminating outward-interval / exact-rational computations**. Floating optimization was used only to suggest witness coefficients; several suggested bounds failed verification and were enlarged. No optimizer result is a premise of the proof.

### 7.1 Global pair certificate

For every \(a\in J\), insert (3.2) into (4.4). The result is at most \(C_0(a)\). The verifier covers \(J\) by 60 closed cells of length \(1/20000\). On each it uses the expanded conditional interval \([L_*(a_-),U_*(a_+)]\) and the lower value \(C_0(a_-)\). Here \(\ell r<1\), so the nontrivial scalar range is \(1\le R\le r^2\). Outward interval subdivision covers this entire range. There are 11,364 processed boxes in total; all 60 cells pass.

For completeness, the scalar upper evaluation used in the verifier is elementary. Put \(x=R-1\), \(d(R)=(1+r\ell)/(1+r+r\ell+\ell R)\). On a box \([x_-,x_+]\), use

\[
\frac{\mathcal L(x_+)}{1+d_-x_-},\qquad
\mathcal L(x)=\frac{(1+x)\log(1+x)}x,
\]

where \(d_-\) is a downward enclosure. \(\mathcal L\) is increasing because \(\mathcal L'(x)=(x-\log(1+x))/x^2\ge0\). A box is discarded only if this upper bound is below the certified cap; otherwise it is bisected.

### 7.2 Guarded pair certificate

For each of the 256 words and each of six closed parameter cells of width \(1/2000\), compute the two endpoint matrices in (3.5). Let their rigorous outward Loewner enclosures be \(L,U\). The verifier proves, for every real symmetric

\[
B=\begin{pmatrix}m_1&w\\w&m_2\end{pmatrix},\qquad L\preceq B\preceq U,
\]

and every \(a\) in that parameter cell, that its output table has \(\alpha\le\min_{\text{cell}}c_z(a)\). Thus \(\alpha\le c_z(a)\) for the actual pair. All 1,536 word/cell combinations pass.

The continuum verifier uses only three scalar variables. Initial diagonal intervals are \([L_{11},U_{11}]\), \([L_{22},U_{22}]\). Its off-diagonal interval has center \((L_{12}+U_{12})/2\) and half-width \(\sqrt{(U_{11}-L_{11})(U_{22}-L_{22})}/2\). This follows from \(B=L+(U-L)^{1/2}T(U-L)^{1/2}\), \(0\preceq T\preceq I\).

Each box is pruned or tightened using exactly

\[
(m_1-L_{11})(m_2-L_{22})\ge(w-L_{12})^2,
\quad
(U_{11}-m_1)(U_{22}-m_2)\ge(w-U_{12})^2. \tag{7.1}
\]

For example, the first inequality gives a lower bound on \(m_1\) from the minimum possible squared distance of \(w\) to \(L_{12}\) and the maximum possible \(m_2-L_{22}\). The analogous three diagonal bounds and two square-root bounds on \(w\) are applied three times. These only remove points that violate (7.1).

For the remaining box, form interval bounds on

\[
q=a+cm_1,\quad r=a+cm_2,\quad s=c^2w^2,
\quad A=(1-q)(1-r)-s,\quad D=qr-s.
\]

Every actual channel atom is at least \(\min(a,1-a-c)^2\), so this lower bound may be intersected with the atom intervals. Put \(x_-=s_-/(A_+D_+)\), \(x_+=s_+/(A_-D_-)\), \(d_-=A_-+D_-\), and use \(\mathcal L(x_+)/(1+d_-x_-)\). If it is not below the cap, bisect the longest remaining coordinate interval. Successful termination covers the continuum, including all guard words and all parameter values in the cell.

The trigonometric input has no unverified library evaluation. At density 1/3, off-diagonal entries are 0 or \(\pm\alpha_0/k\), where \(\alpha_0=\sqrt3/(2\pi)\). The guard verifier uses

\[
\frac{2756644477108960247}{10^{19}}
<\alpha_0<
\frac{2756644477108960248}{10^{19}}.
\]

These bounds, and the narrower 60-decimal-place bounds used below, are checked with exact fractions using \(\pi=16\arctan(1/5)-4\arctan(1/239)\), alternating-series remainders, and rational square comparisons. Logarithms are enclosed by range reduction and the positive \(2\operatorname{atanh}\) series with a geometric remainder. Square roots are only initial guesses until their upper enclosure is verified by an outward square comparison.

### 7.3 Complete actual-law finite payment certificate

For \(K_*=\frac1{40}I+\frac{19}{20}Q_{1/3,22}\), set

\[
L_*=K_*(I-K_*)^{-1},\qquad
p_{a_*}(y)=\det(I-K_*)\det(L_*)_{\{i:y_i=1\}}. \tag{7.2}
\]

Every one of the \(2^{22}=4,194,304\) probabilities is enclosed, using signed, checked multiprecision integers with 192 fractional bits. A recursion excludes the first index by deleting its row/column, or includes it by multiplying the current weight by its positive pivot and taking the Schur complement. This recursively enumerates all principal minors in (7.2), without a Gray-code inverse update. Inverse formation and all Schur operations use outward exact-integer division. Overflow is an error, not modular arithmetic. The conversion of each probability endpoint to a binary endpoint is checked by an exact integer comparison.

The finite expectations from (6.3) give

\[
\boxed{
P(a)=E_aV(a,Y)
=\sum_{k=0}^{9}A_k t^k+R(a),\qquad
|R(a)|\le10^{-6},\quad t=200a-5,
} \tag{7.3}
\]

with the following **rational enclosures**, all having denominator \(10^8\):

| k | lower numerator | upper numerator |
|---:|---:|---:|
|0|1776012226|1776012227|
|1|-82943302|-82943301|
|2|-14608797|-14608796|
|3|-290978|-290977|
|4|1734|1735|
|5|-1|0|
|6|-1|0|
|7|0|1|
|8|0|1|
|9|-1|0|

The coefficient calculation uses \(q_0=p_{a_*}\), \(q_{k+1}=Dq_k/[200(k+1)]\), \(c_k=\langle q_k,V_0\rangle\), \(b_k=\langle q_k,V_1\rangle\), and \(A_0=c_0\), \(A_k=c_k+b_{k-1}/200\) for \(1\le k\le8\), \(A_9=b_8/200\). No mass or configuration is omitted.

### 7.4 Exact rational closure on the continuous interval

Here \(-4/5\le t\le-1/5\). Define \(\underline P(t)\) by taking the lower coefficient endpoint for even powers, the upper endpoint for odd powers, and subtracting \(10^{-6}\). Then \(P(a)\ge\underline P(200a-5)\).

Let

\[
D(a)=a(1-a)(a+c)(1-a-c)>0,
\]

\[
G(a)=D(a)\{\underline P(200a-5)-1/25\}
-(C_0(a)-1)\left\{\frac23(a+c)(1-a-c)+\frac13a(1-a)\right\}.
\]

After \(a=21/1000+(3/1000)x\), \(G\) has degree 11. Every Bernstein coefficient is strictly larger than \(1/40000\). Explicit lower-bound numerators for them, with common denominator \(10^9\), are

```
29091 47114 61938 73573 82033 87328
89474 88485 84380 77175 66890 53546
```

These are verified using exact fractions: if \(G(x)=\sum_i g_ix^i\), the degree-11 Bernstein coefficients are \(b_k=\sum_{i=0}^k g_i\binom{k}{i}/\binom{11}{i}\). Since the Bernstein basis is nonnegative and sums to one on \([0,1]\), this is a continuous-interval proof, not a mesh sign test. It proves

\[
\boxed{P(a)-(C_0(a)-1)d_{1/3,19/20}(a)\ge\frac1{25}
\quad(a\in J).} \tag{7.4}
\]

The absolute-coefficient bound from the same table, using \(|t|\le4/5\), also proves \(P(a)<19\).

The supplied verifier uses an extra outward adjacent binary number after each elementary floating operation; its enclosures do not depend merely on a compiler promise to respect a nondefault rounding mode. The principal probabilities and final Bernstein test use checked integers/exact fractions. The published rational coefficient box and the final conclusion survived the strengthened arithmetic rerun. An additional 138,828 exact-rational arithmetic comparisons passed in all four hardware rounding modes, including signed integer division and binary probability-endpoint conversions; this is an audit check in addition to, not a substitute for, the outward-arithmetic proof.


### 7.5 Reusable finite-witness-to-rate theorem — PROVED

Let a stationary real projection DPP of constant density \(\rho\) be observed through the strict unequal-noise channel on a compact parameter interval \(I\). Supply an integer \(m\ge2\), a consecutive target pair inside an \(m\)-site window, an external finite guard inside that window, a global envelope \(C_0(a)\ge1\), and guard caps

\[
C_0(a)/2\le c_z(a)\le C_0(a)
\]

that bound every compatible actual conditional pair ratio. All nonselected pairs must also obey the global envelope. Put \(\delta_z=C_0-c_z\), choose any fixed two-vector test \(f\) on the \(m\)-site words, and form \(V\) by (5.7) with diagonals \(C_0/2\) and off-diagonal \(\delta_z\). These are explicit finite inputs; in particular the expectation below is under the actual \(m\)-site law.

If certified constants \(\varepsilon>0\) and finite \(M\) satisfy, for every \(a\in I\),

\[
(C_0(a)-1)d_{\rho,c}(a)+\varepsilon
\le P(a):=\sum_{y\in\{0,1\}^m}p_a(y)V(a,y)\le M,
\]

then, for every integer \(n\ge m\),

\[
\boxed{H_n''(a)\le-\varepsilon n+(m-1)M.}
\]

The stationary actual entropy rate consequently has every chord gap at least
\(\frac\varepsilon2\lambda(1-\lambda)(a_1-a_0)^2\) on \(I\).

**Proof.** Translate the same witness through the \(n-m+1\) admissible windows. The associated consecutive pairs are distinct and each site belongs to at most two. Their PSD matrices use at most the full diagonal budget \(C_0\). Equations (5.5)–(5.7) and (2.3) give
\(H_n''\le n(C_0-1)d-(n-m+1)P\), which is the displayed result. Subadditivity and finite-chord integration give the rate statement exactly as in Section 8. Thus this interface pays all pairs and the finite boundary; it contains no unknown extensive remainder. The finite hypotheses are instantiated and proved above for the benchmark subinterval. \(\square\)

## 8. Completion of the true-law finite-volume and rate proofs

For each consecutive pair \(e=\{i,i+1\}\) whose translated 22-site window lies in \(V=[n]\), use the translated guard and local witness above. There are exactly \(n-21\) such pairs for \(n\ge22\). Give each incident site the allocation \(C_0/2\). No site belongs to more than two selected edges, so the pointwise diagonal budget in (5.4) is respected. The matrices (6.1) are PSD. Stationarity makes every variational expectation equal to the same \(P(a)\).

Apply (5.5)–(5.7), then (2.3) and (7.4):

\[
\begin{aligned}
H_n''(a)
&\le n(C_0(a)-1)d_{1/3,19/20}(a)-(n-21)P(a)\\
&=-n\{P(a)-(C_0(a)-1)d_{1/3,19/20}(a)\}+21P(a)\\
&\le-\frac n{25}+399.
\end{aligned}
\]

This proves (T). All long-range pairs were already included in (5.2) and charged through the full common Fisher term. They were not truncated. The only finite-boundary loss is the explicitly missing 21 translated witnesses. There is no count-layer exception, corrected law, or Toeplitz projection leakage term hidden in this deduction.

Stationarity gives \(H_{n+m}\le H_n+H_m\), so \(h(a)=\lim H_n(a)/n\) exists by subadditivity. Integrating (T) twice on a chord gives

\[
\operatorname{Gap}_\lambda H_n
\ge\frac12\left(\frac n{25}-399\right)
\lambda(1-\lambda)(a_1-a_0)^2.
\]

Divide by \(n\) and pass to the value limit. This proves (C). No \(C^2\) regularity of the entropy rate is inferred or required.

### Density-complement corollary

For \(U_{ii}=(-1)^i\), the finite sine matrices satisfy

\[
I-Q_{\rho,n}=UQ_{1-\rho,n}U^*.
\]

Taking particle complements changes \(K\) to \(I-K\), and a diagonal unitary gauge does not change DPP probabilities. Therefore

\[
H_{\rho,c,n}(a)=H_{1-\rho,c,n}(1-c-a).
\]

The second derivatives agree under this affine reflection. Applying (T) yields the stated \(\rho=2/3\), \([.026,.029]\) corollary. This uses a density-complement pair, not a half-density symmetry assumption.

## 9. What changed from the previous incomplete result

The earlier S63 response left an extensive actual-law conditional log-odds term unpaid. Here it is not renamed: a global posterior envelope charges all pairs, and guard-dependent nearest-pair improvements are combined with diagonal Fisher terms into PSD matrices. The signed cross-products are retained inside these matrices. Conditional Jensen then moves the **entire nonnegative quadratic** to a finite actual marginal without the large observation-Hessian cost of a signed potential.

The finite test is converted into an explicit polynomial under the moving actual probability vector. Its coefficient intervals and rational Bernstein certificate pay the complete off-midpoint budget on J. The comparison does not assert that a fixed-reference law has the same derivatives; it does not differentiate a value approximation.

Parameters controlling extension are explicit: the density-dependent endpoints (3.2), both likelihood ratios in (3.3), the local projection compression \(Q_E\), the scalar global pair envelope (4.4), PSD allocation (5.4), and the full unequal-noise budget (2.3)/(2.4). A future extension must supply new certificates or inequalities for the remaining parameter region. The present theorem does not assert that these same witnesses work on all of [.02,.03].

## 10. Arithmetic and source audit

The proof imports no unproved displacement-convexity, count-entropy, or conditional-table theorem. Inverse order, posterior normalization, conditional Jensen, score identities, nilpotent probability evolution, and the finite certificate reductions are proved above.

For the implementation, the Boost primary documentation for `cpp_int_backend` was checked: the chosen `checked` fixed-width types throw on overflow rather than reducing modulo a power of two. The GCC primary documentation explicitly warns that `-frounding-math` alone is not an absolute guarantee against every relevant optimization. Accordingly, the final interval helper additionally moves every elementary computed endpoint outward by one adjacent representable number, uses volatile elementary results and disables contraction. Exact comparison verifies probability-endpoint conversions. Transcendental library outputs are not accepted without the elementary enclosures described above.

The proof is computer-assisted and is submitted for independent review; it is not labelled independently reviewed. Its finite certificate data, verification algorithms, and successful outputs accompany this manuscript. No numerical optimizer, unsigned floating sign scan, or author-only packet claim is a mathematical premise.

## Appendix A. Complete rational guard-cap data

Each row gives an index range followed by its successive \((L_z,U_z)\) integer pairs. The bit order and affine interpolation are exactly those of Section 6. These values are merely explicit candidate data; their validity is supplied by the continuum verification in Section 7.2, not by their manner of discovery.

```text
000-007: 8756,8341 9496,9213 9998,9871 10021,9769 10489,10278 10362,10502 10131,10351 9743,10175
008-015: 10330,10813 10052,10486 9881,10192 9139,9652 9350,10062 9048,9992 9389,10062 9076,9648
016-023: 10330,10813 10313,10805 10151,10340 9834,9906 10151,10151 9890,9925 9506,9582 9444,9521
024-031: 10069,10077 9848,9874 9657,9697 9567,9611 9641,9683 9737,9771 9681,9718 9620,9660
032-039: 10489,10278 10712,10750 10529,10885 10092,10124 10151,10151 10112,10123 9709,9812 9416,9557
040-047: 10151,10151 10043,10058 9710,9764 9316,9403 9436,9526 9585,9653 9596,9662 9383,9463
048-055: 9350,10062 9413,9897 9389,9547 8593,8822 9436,9526 9124,9228 8912,9035 9015,9123
056-063: 9641,9683 9579,9623 9498,9547 9506,9553 9495,9546 9590,9632 9531,9577 9548,9591
064-071: 9998,9871 10330,10148 10691,10489 10323,10411 10529,10885 10151,10340 9953,10045 9543,9756
072-079: 10151,10340 10142,10145 9907,9957 9242,9386 9389,9547 9426,9563 9581,9690 9257,9400
080-087: 9881,10192 9991,10052 9907,9957 8927,9089 9710,9764 9168,9260 8974,9081 9049,9147
088-095: 9657,9697 9522,9568 9458,9508 9476,9524 9498,9547 9545,9589 9481,9529 9502,9548
096-103: 10131,10351 10085,10437 9953,10045 8608,8992 9709,9812 8766,8971 8203,8468 8293,8532
104-111: 9506,9582 9186,9278 8974,9081 8941,9047 8912,9035 9108,9206 9006,9110 8985,9086
112-119: 9389,10062 9523,9896 9581,9690 8856,9029 9596,9662 9200,9289 9006,9110 9085,9179
120-127: 9681,9718 9557,9600 9481,9529 9494,9541 9531,9577 9584,9625 9512,9558 9531,9574
128-135: 9496,9213 10023,9930 10330,10148 10330,10130 10712,10750 10366,10687 10085,10437 9682,10118
136-143: 10313,10805 10143,10424 9991,10052 9224,9365 9413,9897 9251,9825 9523,9896 9173,9353
144-151: 10052,10486 10143,10424 10142,10145 9377,9498 10043,10058 9468,9537 9186,9278 9230,9315
152-159: 9848,9874 9622,9662 9522,9568 9521,9566 9579,9623 9632,9671 9557,9600 9555,9597
160-167: 10362,10502 10366,10687 10151,10340 9446,9658 10112,10123 9417,9541 8766,8971 8733,8927
168-175: 9890,9925 9468,9537 9168,9260 9060,9156 9124,9228 9304,9387 9200,9289 9117,9208
176-183: 9048,9992 9251,9825 9426,9563 8863,9043 9585,9653 9304,9387 9108,9206 9184,9272
184-191: 9737,9771 9632,9671 9545,9589 9546,9589 9590,9632 9654,9690 9584,9625 9591,9630
192-199: 10021,9769 10330,10130 10323,10411 9683,9936 10092,10124 9446,9658 8608,8992 8353,8742
200-207: 9834,9906 9377,9498 8927,9089 8583,8769 8593,8822 8863,9043 8856,9029 8616,8799
208-215: 9139,9652 9224,9365 9242,9386 8583,8769 9316,9403 9060,9156 8941,9047 9021,9119
216-223: 9567,9611 9521,9566 9476,9524 9498,9545 9506,9553 9546,9589 9494,9541 9523,9567
224-231: 9743,10175 9682,10118 9543,9756 8353,8742 9416,9557 8733,8927 8293,8532 8403,8618
232-239: 9444,9521 9230,9315 9049,9147 9021,9119 9015,9123 9184,9272 9085,9179 9069,9162
240-247: 9076,9648 9173,9353 9257,9400 8616,8799 9383,9463 9117,9208 8985,9086 9069,9162
248-255: 9620,9660 9555,9597 9502,9548 9523,9567 9548,9591 9591,9630 9531,9574 9561,9601
```

## Appendix B. Reproduction

The companion `S63_CERTIFICATES.zip` contains the complete source, inputs, and certificate outputs. Run from its extracted directory. The four probability subtrees contain every 22-bit word once; generated binary probability caches need not be shipped. The verifier fails on an unproved interval box, invalid or zero pivot, incomplete word coverage, arithmetic overflow, or insufficient payment. The final sign is checked again using only Python standard-library exact fractions. See its README for commands and arithmetic requirements.
