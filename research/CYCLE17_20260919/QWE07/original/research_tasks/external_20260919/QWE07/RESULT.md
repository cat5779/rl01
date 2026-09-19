# QWE07 — Certified density transport for actual configuration entropy

**Status: PROVED, computer-assisted, on the explicit rectangle below.**

**Not proved:** extension to density $1/2$, or the all-density/all-legal-bias concavity conjecture. The failure of an unchanged finite witness, documented below, is not a counterexample to that conjecture.

Repository context: `randomcat4/dpp-stationary-entropy`; the QWE07 task branch is PR129 (`research/external-qwe07-density-transport-20260919`). The original Drive packet was used as the source of the task and mathematical inputs. This submission adds only the QWE07 result/support package to that task branch and does not modify repository-wide shared status. It is a new, internally checked submission, not a claim of independent external review or priority.

## 0. Exact result

For the infinite sine projection and its **actual finite compression**, write

$$
Q_\rho(i,j)=\begin{cases}\rho,&i=j,\\
\dfrac{\sin(\pi\rho(i-j))}{\pi(i-j)},&i\ne j,
\end{cases}\qquad
K_{\rho,a,n}=aI+\frac{19}{20}Q_{\rho,n}.
$$

Let $H_{\rho,n}(a)$ be the full spatial-configuration Shannon entropy of
$\operatorname{DPP}(K_{\rho,a,n})$, in natural units. Define

$$
\boxed{\mathcal R=\left[\frac13,\frac{1009}{3000}\right]
\times\left[\frac{21}{1000},\frac3{125}\right].}
$$

The density interval has width exactly $3/1000$. Its upper endpoint is
$0.336333333\ldots$. Since $p=a/(1-c)=20a$, the bias interval is exactly
$p\in[0.42,0.48]$, as requested.

**Theorem.** For every $(\rho,a)\in\mathcal R$ and every integer $n\ge22$,

$$
\boxed{\frac{\partial^2}{\partial a^2}H_{\rho,n}(a)
\le-\frac{n}{25}+399.}\tag{T}
$$

For every fixed density in this interval, the stationary entropy rate
$h_\rho(a)=\lim_{n\to\infty}H_{\rho,n}(a)/n$ exists and satisfies

$$
\boxed{\operatorname{Gap}_\lambda h_\rho
\ge\frac1{50}\lambda(1-\lambda)(a_1-a_0)^2}\tag{C}
$$

for all $a_0,a_1\in[21/1000,3/125]$ and $\lambda\in[0,1]$, where

$$
\operatorname{Gap}_\lambda f
=f((1-\lambda)a_0+\lambda a_1)
-(1-\lambda)f(a_0)-\lambda f(a_1).
$$
In the $p$ coordinate the coefficient is $1/20000$, not $1/50$.
The finite-volume upper bound becomes strictly negative for $n\ge9976$;
it does not assert negative curvature for every $n\ge22$.

This turns the accepted fixed-density interval into a genuine two-parameter
rectangle, retaining its curvature and boundary constants. It does not use
particle-hole symmetry to interpolate densities.

## 1. Required properties of the transport tool

The tool must meet five requirements before being applied.

1. **Actual-law compatibility.** Every finite expectation must use the moving
   DPP law. A reference law may select a test function, but cannot replace its
   evaluation law. Every configuration, including rare ones, must be included.
2. **Correct derivative order.** Entropy curvature is a second derivative in
   $a$ at fixed $\rho,c$. Density transport must account for all moving sine
   entries; it cannot use the diagonal-shift evolution as a density derivative.
3. **Normalization and posterior validity.** The infinite projection prior,
   its positive-field posterior, and finite compression must remain distinct.
   Both noise likelihood ratios and all determinant normalizers must be kept.
4. **Scaling.** The transported certificate must imply a negative term
   proportional to $n$, with an explicit finite boundary payment, rather than
   a fixed-volume sign or a differentiated entropy-value approximation.
5. **Quantitative payment.** Operator enclosures, interpolation remainders,
   nodal errors, and the full-data Fisher budget must have explicit constants.

The construction has two new parts: nested-subspace posterior transport, and
an analytic majorant for finite actual-law expectations. A tensor interpolation
certificate then interfaces these parts with the S63 PSD score allocation.

## 2. Density geometry: finite trace control, not infinite norm continuity

The infinite operator $Q_\rho$ is the Fourier multiplier by
$1_{[-\pi\rho,\pi\rho]}$. Thus its range $\mathcal H_\rho$ is nested as $\rho$
increases, and $Q_\rho$ is an orthogonal projection. Every finite compression is
only a positive contraction.

For a finite consecutive set of $m$ sites,

$$
\partial_\rho Q_{\rho,m}(i,j)=\cos(\pi\rho(i-j))
=u_\rho(i)u_\rho(j)+v_\rho(i)v_\rho(j),\tag{2.1}
$$

where $u_\rho(i)=\cos(\pi\rho i)$ and $v_\rho(i)=\sin(\pi\rho i)$.
Consequently this derivative is PSD, has rank at most two, and has trace $m$.
For $\sigma\ge\rho$,

$$
Q_{\sigma,m}-Q_{\rho,m}\succeq0,\qquad
\|Q_{\sigma,m}-Q_{\rho,m}\|_1=m(\sigma-\rho),\tag{2.2}
$$

where $\|\cdot\|_1$ here denotes the nuclear/trace norm of a matrix.
In contrast,

$$
\|Q_\sigma-Q_\rho\|_{\rm op}=1\quad(0<\rho<\sigma<1).\tag{2.3}
$$

Indeed the difference is the nonzero projection onto the added Fourier arcs.
An infinite-operator small-norm perturbation argument is therefore unavailable.
The transport below avoids it.

The finite compression leakage is exactly

$$
Q_{\rho,V}-Q_{\rho,V}^2
=Q_{\rho,V,V^c}Q_{\rho,V^c,V}\succeq0.\tag{2.4}
$$

It is not set to zero anywhere in this proof. All finite probabilities use
$Q_{\rho,V}$ itself, and the infinite projection enters only through an exact
latent representation and comparison operators.

## 3. Exact latent law and density-stable posterior bounds

### 3.1 The unequal-noise representation and Fisher budget

Let $X$ be the DPP of the infinite projection. Given $X$, independently draw
$Y_i$ with $\Pr(Y_i=1\mid X)=a+cX_i$, where $c=19/20$.
For every finite $S$,

$$
E\prod_{i\in S}Y_i
=\sum_{T\subseteq S}a^{|S|-|T|}c^{|T|}\det Q_{\rho,T}
=\det(aI+cQ_\rho)_S.\tag{3.1}
$$

Inclusion moments determine a binary law, so this is exactly the finite
Toeplitz DPP, not an approximation. Set

$$
u=a,\quad v=a+c,\quad d_+=\frac va,\quad
 d_-=\frac{1-v}{1-a},\quad
 \beta_0=a(1-a),\quad\beta_1=v(1-v).
$$

The complete-data common-shift score is

$$
S=\sum_{i\in V}\frac{Y_i-a-cX_i}{(a+cX_i)(1-a-cX_i)}.
$$

Its summands are conditionally independent and centered given $X$. The output
score is $E[S\mid Y_V]$. Conditional Jensen therefore gives

$$
\boxed{J_V\le |V|d_{\rho,c}(a),\qquad
 d_{\rho,c}(a)=\frac{1-\rho}{\beta_0}+\frac\rho{\beta_1}.}\tag{3.2}
$$

The density-dependent, unequal-noise budget is kept in full. In particular,
no half-density cancellation is imposed.

### 3.2 Positive-field posterior and nested-subspace lemma

For finitely many observations, Bayes' rule tilts the latent law by
$\prod_i D_i^{X_i}$, where an observed 1 gives $D_i=d_+$, an observed 0 gives
$D_i=d_-$, and an unobserved site gives $D_i=1$.
For a bounded positive diagonal $D$, bounded away from zero, put

$$
P_D(\rho)=D^{1/2}Q_\rho
\bigl(Q_\rho DQ_\rho|_{\mathcal H_\rho}\bigr)^{-1}
Q_\rho D^{1/2}.\tag{3.3}
$$

This is the orthogonal projection onto $D^{1/2}\mathcal H_\rho$:
its range is that closed subspace, it is self-adjoint, and multiplication shows
$P_D^2=P_D$. For a finite-support likelihood, the DPP generating identity
$E\prod_i(1+f_iX_i)=\det(I+\operatorname{diag}(f)Q_\rho)$, divided by the
likelihood normalizer, verifies that (3.3) is the actual posterior kernel.
One obtains the displayed formula by the determinant identity
$\det(I+AB)=\det(I+BA)$ and inversion on $\mathcal H_\rho$.

**Nested-subspace lemma.** For the same fixed field $D$,

$$
\rho\le\sigma\quad\Longrightarrow\quad P_D(\rho)\preceq P_D(\sigma).
\tag{3.4}
$$

**Proof.** An invertible bounded map preserves inclusion and closedness of
subspaces. Hence $D^{1/2}\mathcal H_\rho\subseteq D^{1/2}\mathcal H_\sigma$.
Orthogonal projections onto nested subspaces are ordered. This proves (3.4)
without differentiating an infinite projection. The same proof works for any
nested family of closed subspaces, not just sine projections. $\square$

### 3.3 Guarded endpoint transport

Let $T$ be an unobserved target pair and $O$ a finite guard. Write $E=T\cup O$.
For a guard word $z$, let $D_E$ have entries 1 on $T$ and the corresponding
$d_+,d_-$ on $O$. If the field outside $E$ is the constant $d>0$, its target
compression is

$$
\mathcal B_d(\rho,a,z)
=\left[Q_{\rho,E}\{dI+(D_E-dI)Q_{\rho,E}\}^{-1}\right]_{T,T}.
\tag{3.5}
$$

To derive this, let $A:\mathcal H_\rho\to\mathbb R^E$ be coordinate restriction.
Then $AA^*=Q_{\rho,E}$, and the push-through inverse identity gives

$$
A\{dI+A^*(D_E-dI)A\}^{-1}A^*
=Q_{\rho,E}\{dI+(D_E-dI)Q_{\rho,E}\}^{-1}.
$$

This does not require $Q_{\rho,E}$ to be a projection or invertible.
The inverse on the right exists: its determinant agrees with that of
$d(I-Q_{\rho,E})+Q_{\rho,E}^{1/2}D_EQ_{\rho,E}^{1/2}$, which is strictly positive.

All unknown fields lie between $d_-$ and $d_+$. Inverse order on the positive
Gram operator therefore bounds the actual latent target posterior $B_T$ by

$$
\mathcal B_{d_+}(\rho,a,z)\preceq B_T\preceq
\mathcal B_{d_-}(\rho,a,z).\tag{3.6}
$$

The constant fields on infinitely many sites are comparison operators, not
assertions about positive-probability infinite observation words.

Both $d_+(a)$ and $d_-(a)$ decrease with $a$. At fixed density, the associated
Gram operators decrease, and their target inverse compressions increase.
The target fields remain exactly 1 in this argument; no general monotonicity
of the entire posterior projection in the field $D$ is asserted.
Combining this with (3.4) proves the **rectangle endpoint rule**:

$$
\boxed{
\mathcal B_{d_+(a_-)}(\rho_-,a_-,z)
\preceq B_T(\rho,a)\preceq
\mathcal B_{d_-(a_+)}(\rho_+,a_+,z)
}\tag{3.7}
$$

for every $(\rho,a)\in[\rho_-,\rho_+]\times[a_-,a_+]$ and every compatible
finite-volume exterior observation. Thus only finite endpoint sine matrices
need numerical enclosures; the continuum transport is an operator theorem.

The same one-site argument, with a rank-one inverse, gives

$$
L(\rho,a)=a+c\frac\rho{\rho+d_+(1-\rho)},\qquad
U(\rho,a)=a+c\frac\rho{\rho+d_-(1-\rho)}.\tag{3.8}
$$

Every one-site probability conditional on any finite collection of other
observations lies in this interval. Its rectangle enclosure uses
$L(\rho_-,a_-)$ and $U(\rho_+,a_+)$.

## 4. Scalar pair envelopes and their certified density extension

For a conditional pair table, write its positive atoms as $A,B,C,D$, with
$A+B+C+D=1$, $s=BC-AD\ge0$, $R=BC/(AD)=1+x$, and $d=A+D$.
Define the continuous pair ratio

$$
\alpha=\frac{\log(BC/AD)}{s(A^{-1}+B^{-1}+C^{-1}+D^{-1})}
=\frac{\mathcal L(x)}{1+dx},\qquad
\mathcal L(x)=\frac{(1+x)\log(1+x)}x,\quad\mathcal L(0)=1.
\tag{4.1}
$$

The second expression follows by direct multiplication using the normalization
of the four atoms. Independence has continuous value $\alpha=1$.

Suppose all four single-site conditional probabilities lie in $[L,U]$.
Put $\ell=L/(1-L)$ and $r=U/(1-U)$. The regime checked below is
$\ell<1<r$ and $\ell r<1$. The constraints include
$B,C\le rA$ and $D\ge\ell B,\ell C$.
For $1\le R\le r^2$ they imply

$$
d\ge\frac{1+r\ell}{1+r+r\ell+\ell R}.\tag{4.2}
$$

Here is a proof of the optimization used in this bound. Exchange the sites
so that $C\ge B$, and rescale $B=1,C=t\ge1$. At fixed $R$ one must minimize
$(A+D)/(1+t)$ under

$$
1\le t\le\frac r{\ell R},\qquad
\frac tr\le A\le\frac1{\ell R},\qquad D=\frac t{RA}.
$$

Until $t=r^2/R$, the minimizing expression is
$2\sqrt{t/R}/(1+t)$, decreasing for $t\ge1$.
Thereafter it is $(t/r+r/R)/(1+t)$, whose derivative has the sign of
$R-r^2$. Thus for $R\le r^2$ the minimum is at $t=r/(\ell R)$.
Normalizing again yields (4.2). For $R>r^2$, the latter expression is
increasing, so its minimum is at $t=1$. Arithmetic-geometric mean then gives
$d\ge1/(1+\sqrt R)$, and

$$
\alpha\le\frac{\sqrt R\log R}{R-1}\le1.
$$

The last inequality follows from $2\log z\le z-z^{-1}$ for $z\ge1$, whose
derivative comparison is immediate. Infeasible values of $R$ need no treatment.

We use the same affine global cap as S63,

$$
C_0(a)=\frac{261}{200}+\frac{51}{10}a.\tag{4.3}
$$

`density_global.cpp` encloses (3.8) on each of 60 closed bias cells, using the
entire new density interval. It proves the scalar maximum from (4.1)–(4.2)
is at most the lower value of $C_0$ on the cell. All 60 cells pass; the final
run processes 24,292 scalar boxes.

For the local pair take the 22-site window $W=\{0,\ldots,21\}$,
$T=\{10,11\}$, and guard $O=\{6,7,8,9,12,13,14,15\}$ in this bit order.
The 256 integer pairs $(L_z,U_z)$ in Appendix A define

$$
c_z(a)=\frac{(3/100-a)L_z+(a-1/50)U_z}{100},\qquad
\delta_z(a)=C_0(a)-c_z(a).\tag{4.4}
$$

`density_guard.cpp` proves $\alpha\le c_z(a)$ for every guard word throughout
the new rectangle. It starts with six bias cells for each of the 256 words,
uses the rectangle endpoint rule, and adaptively subdivides parameter cells
when the scalar matrix-box proof has not closed. A failed or unresolved box
is never accepted.

### What a guard-box proof checks

Interval inverses in (3.5) enclose all entries. A symmetric midpoint matrix
$C$ with entry errors $e_0,e_1,e_w$ has operator error at most
$\varepsilon=\max(e_0,e_1)+e_w$, by the maximum absolute row sum. Thus
$C-\varepsilon I$ and $C+\varepsilon I$ are safe Loewner endpoints. No extra
factor two is needed or inserted.

For the resulting endpoints $L,U$, write
$B=\begin{pmatrix}m_1&w\\w&m_2\end{pmatrix}$.
The initial diagonals lie between those of $L,U$; the off-diagonal lies in

$$
\frac{L_{12}+U_{12}}2
\ \pm\ \frac12\sqrt{(U_{11}-L_{11})(U_{22}-L_{22})}.
$$

This follows by writing the order interval as
$(L+U)/2+(U-L)^{1/2}S(U-L)^{1/2}/2$, with $-I\preceq S\preceq I$.
The verifier prunes or tightens boxes only with the necessary inequalities

$$
(m_1-L_{11})(m_2-L_{22})\ge(w-L_{12})^2,\quad
(U_{11}-m_1)(U_{22}-m_2)\ge(w-U_{12})^2.
$$

For a remaining box it encloses
$q=a+cm_1$, $r=a+cm_2$, $s=c^2w^2$,
$A=(1-q)(1-r)-s$, and $D=qr-s$.
Every actual channel atom is at least $\min(a,1-a-c)^2$, so intersecting with
this lower bound is valid. Then

$$
x_-\le\frac{s}{AD}\le x_+,\qquad d_-=A_-+D_-,\qquad
\alpha\le\frac{\mathcal L(x_+)}{1+d_-x_-}.
$$

The monotonicity $\mathcal L'(x)=(x-\log(1+x))/x^2\ge0$ justifies this upper
bound. The program accepts only when it is at most the minimum of $c_z$ over
the parameter cell. Otherwise it subdivides. These tests cover the entire
Loewner order interval, not samples from it.

The completed guard-run coverage and counts are recorded in Section 9.

## 5. PSD allocation and the actual-law variational interface

This section supplies the inference from the finite certificates to curvature.
It also fixes all ordered-pair factors and normalizations.

For the actual finite law on $V$, let

$$
G(Y)=\{K-\operatorname{diag}(1-Y)\}^{-1},\quad Z_i=G_{ii},\quad
F_V=\sum_iEZ_i^2,\quad J_V=E\left(\sum_iZ_i\right)^2.
$$

The full atom is
$p(Y)=(-1)^{|V|-|Y|}\det(K-\operatorname{diag}(1-Y))$.
Differentiate in independent diagonal shifts $a_i$:

$$
Z_i=\partial_{a_i}\log p,\qquad
\partial_{a_i a_j}p=p(Z_iZ_j-|G_{ij}|^2)\quad(i\ne j).
$$

Summing the last identity over all words yields

$$
EZ_iZ_j=E|G_{ij}|^2,\qquad
J_V=F_V+\sum_{i\ne j}E|G_{ij}|^2.\tag{5.1}
$$

The common-shift second derivative includes the full probability acceleration:

$$
H_V''=-J_V-\sum_Yp''(Y)\log p(Y)
=\sum_{i\ne j}E_{Y_{V\setminus\{i,j\}}}\log\frac{BC}{AD}-J_V.
\tag{5.2}
$$

Indeed pure diagonal second derivatives vanish; for a fixed pair-rest word
the mixed derivative has the four signs $(+,-,-,+)$ times its rest mass.
Its logarithmic sum is $\log(AD/BC)$. This proves (5.2), with ordered pairs.
Inverting the conditional masked $2\times2$ matrix also gives

$$
E[|G_{ij}|^2\mid\text{rest}]=s(A^{-1}+B^{-1}+C^{-1}+D^{-1}).
\tag{5.3}
$$

Use the global cap on all pairs, and the improvement $\delta_z$ on selected
consecutive pairs. Since their guards contain neither target bit,
normalization after differentiation gives the weighted identity

$$
E[\delta_z|G_{ij}|^2]=E[\delta_z Z_iZ_j].\tag{5.4}
$$

This is an expectation identity, not pointwise positivity of $Z_iZ_j$.
For each selected pair allocate $C_0/2$ of each endpoint's diagonal budget and
put

$$
B_z(a)=\begin{pmatrix}C_0(a)/2&\delta_z(a)\\
\delta_z(a)&C_0(a)/2\end{pmatrix}.\tag{5.5}
$$

Exact endpoint checks give $\delta_z\ge0$ and $B_z\succeq0$ on the full bias
interval. The smallest certified lower eigenvalue is $1169/10000$.
Each site belongs to at most two selected consecutive pairs, so no diagonal
budget is used twice. Equations (5.1)–(5.4) imply

$$
H_V''\le(C_0-1)J_V-\sum_eE[Z_{V,e}^{\mathsf T}B_eZ_{V,e}].
$$

For a window $W_e$ containing the pair and its guard, differentiation of the
same marginalization identity gives
$E[Z_{V,e}\mid Y_{W_e}]=Z_{W_e,e}$.
Since $B_e$ is measurable in that window and PSD, conditional Jensen yields

$$
H_V''\le(C_0-1)J_V-
\sum_eE[Z_{W_e,e}^{\mathsf T}B_eZ_{W_e,e}].\tag{5.6}
$$

Choose a fixed two-vector function $f$ on 22-site words. Completing the square
and using $E[Z_i g]=E[\Delta_i g]$, where
$\Delta_i g=g(y_i=1)-g(y_i=0)$, gives the lower variational payment

$$
P(\rho,a)=E_{\rho,a}V(a,Y),\qquad
V=2\{\Delta_{10}(B_zf)_{10}+\Delta_{11}(B_zf)_{11}\}-f^{\mathsf T}B_zf.
\tag{5.7}
$$

To verify the score identity, pair words differing in bit $i$ and use
$\partial_{a_i}p(y)=(2y_i-1)(p(y)+p(y^i))$.
This identity is applied at each actual parameter; it does not differentiate
$g$ or an entropy comparison. The law in (5.7) is always the moving actual law.

The fixed test is exactly the S63 test, chosen at $\rho_*=1/3$, $a_*=1/40$:

$$
f_i(y)=(2y_i-1)\left(1+\frac{p_{\rho_*,a_*}(y^i)}{p_{\rho_*,a_*}(y)}\right),
\qquad i=10,11.\tag{5.8}
$$

Because $B_z$ is affine in $a$,

$$
V(a,y)=V_0(y)+(a-a_*)V_1(y).
$$

The new full-word calculation independently encloses this same exact test and
proves $\|V_0\|_\infty<1500$ and $\|V_1\|_\infty<10000$.
Thus $\|V(a,\cdot)\|_\infty\le1540$ on the requested bias interval.

## 6. Reusable analytic majorant for moving-density expectations

### 6.1 Masked inverses retain the strict spectral gap

Suppose $aI\preceq K\preceq(1-b)I$, with $a,b>0$.
For any word, partition occupied and vacant coordinates. For
$\lambda\in(-b,a)$, the occupied diagonal block of
$K-\operatorname{diag}(1-y)-\lambda I$ is positive definite, and the vacant
block is negative definite. Its Schur complement is negative definite.
The matrix is therefore invertible. Since it is Hermitian, this proves

$$
\|(K-\operatorname{diag}(1-y))^{-1}\|_{\rm op}
\le\frac1{\min(a,b)}.\tag{6.1}
$$

The empty-block cases are immediate. Here $b=1-a-c$, so the uniform bound is
$1000/21$.

### 6.2 Complex finite-law bound

**General finite-law transport lemma.** Let $K(z)$ be an analytic family of
$m\times m$ matrices, with $K(r)$ a Hermitian strict contraction at a real
center $r$. Put
$\varepsilon=\min\{\lambda_{\min}(K(r)),1-\lambda_{\max}(K(r))\}>0$.
For the analytic masked-determinant word masses, the calculation below proves

$$
\sum_y|p_z(y)|\le
\exp\left(\frac{\|K(z)-K(r)\|_1}{\varepsilon}\right).
$$

A fixed test expectation is bounded by the right-hand side times its supremum
norm. No positivity or Hermiticity is required away from the real center.
The lemma applies to any finite analytic kernel family meeting the stated
real-center gap hypothesis. We now specialize its perturbation term to sine
kernels and prove the bound.

Extend the sine entries to an entire function of a complex density $z$.
Center the site coordinates at $(m-1)/2$ and write

$$
Q'_z=\tfrac12(u_zv_z^{\mathsf T}+v_zu_z^{\mathsf T}),\qquad
u_z(j)=e^{i\pi z(j-(m-1)/2)},\quad
v_z(j)=e^{-i\pi z(j-(m-1)/2)}.
$$

The symmetry of the centered coordinates gives

$$
\|Q'_z\|_1\le m\cosh(\pi(m-1)|\Im z|).
$$

Integration along the segment from a real $r$ to $r+w$ yields

$$
\boxed{\|Q_{r+w,m}-Q_{r,m}\|_1
\le m|w|\frac{\sinh(\pi(m-1)|w|)}{\pi(m-1)|w|}.}\tag{6.2}
$$

For any complex matrix $A$,

$$
|\det(I+A)|\le\prod_j(1+s_j(A))\le e^{\|A\|_1}.
$$

One proof expands the determinant as
$\sum_k\operatorname{Tr}(\wedge^kA)$ and bounds each trace by the nuclear norm
of the corresponding exterior power; its singular values are products of
singular values of $A$.

Let $p_z(y)$ denote the analytic masked-determinant extension of the actual
word mass. At any real center $r$,

$$
p_{r+w}(y)=p_r(y)\det\{I+G_r(y)c(Q_{r+w,m}-Q_{r,m})\}.
$$

Using (6.1), summing with the **normalized actual weights** $p_r(y)$, and then
using (6.2), gives

$$
\boxed{
\sum_y|p_{r+w}(y)|
\le\exp\left[
\frac{cm|w|}{\varepsilon}
\frac{\sinh(\pi(m-1)|w|)}{\pi(m-1)|w|}
\right],\quad \varepsilon=\min(a,1-a-c).
}\tag{6.3}
$$

Consequently, for any fixed finite test $V$, its actual-law expectation has
this majorant multiplied by $\|V\|_\infty$.
This is the reusable analytic transport estimate. It controls the complete
probability vector, not just typical words or inclusion moments.

### 6.3 Explicit specialization

Take $m=22$ and complex radius $R=1/100$.
Since $21\pi/100<33/50$ and
$\sinh(33/50)/(33/50)<27/25$,

$$
\frac{(19/20)22R}{21/1000}\frac{27}{25}
=\frac{1881}{175}<11.
$$

Exact positive-series arithmetic proves $e^{11}<60000$. Thus, uniformly for
real centers in the density interval and all requested biases,

$$
|P(r+w,a)|\le1540\cdot60000\quad(|w|\le1/100).
\tag{6.4}
$$

Cauchy's formula gives
$|\partial_\rho^{11}P|/11!\le1540\cdot60000/R^{11}$.
These are density derivatives of the full sine law. No diagonal-shift formula
has been used for them.

## 7. A continuum certificate from actual-law nodal expectations

### 7.1 Exact grid and interpolation operators

Use the 55 rational nodes

$$
\rho_j=\frac13+\frac{3j}{10000}\quad(0\le j\le10),\qquad
 a_k=\frac{84+3k}{4000}\quad(0\le k\le4).
\tag{7.1}
$$

Let $t=(\rho-1/3)/(3/1000)$ and $x=(a-21/1000)/(3/1000)$.
Write $\ell_j^{(N)}$ for the Lagrange basis on $0,1/N,\ldots,1$.
Appendix B gives rational lower and upper enclosures for every nodal
expectation, with width at most $2\cdot10^{-8}$. Let $m_{jk}$ be their exact
rational midpoints and set

$$
T(t,x)=\sum_{j=0}^{10}\sum_{k=0}^4
m_{jk}\ell_j^{(10)}(t)\ell_k^{(4)}(x).\tag{7.2}
$$

This is an interpolation of moving **actual expectations**, not an assertion
that the density dependence is a polynomial.

### 7.2 Density remainder

Exact rational Bernstein subdivisions prove

$$
\sup_{t\in[0,1]}\left|\prod_{j=0}^{10}(t-j/10)\right|
\le\frac1{200000},\qquad \Lambda_{10}\le32.
\tag{7.3}
$$

Here $\Lambda_N=\sup\sum_j|\ell_j^{(N)}|$.
The Lagrange remainder and (6.4) give the density interpolation error

$$
E_\rho=1540\cdot60000\left(\frac3{10}\right)^{11}\frac1{200000}
=\frac{40920957}{50000000000}=0.00081841914.
\tag{7.4}
$$

### 7.3 Bias remainder, used only in the bias direction

For a complete probability vector define

$$
(D_i p)(y)=(2y_i-1)(p(y)+p(y^i)),\qquad D=\sum_{i=0}^{21}D_i.
$$

Multi-affinity in independent diagonal shifts gives
$\partial_a^k p=D^kp$, with $\|D\|_{1\to1}\le44$.
As $V$ is affine in $a$,

$$
|\partial_a^5 P|
\le44^5\cdot1540+5\cdot44^4\cdot10000
=441375784960.
$$

Exact Bernstein bounds also prove

$$
\sup_{x\in[0,1]}\left|\prod_{k=0}^4(x-k/4)\right|\le\frac1{250},
\qquad\Lambda_4\le3.
$$

Hence the bias interpolation error is at most

$$
E_a=\frac{441375784960}{5!}\left(\frac3{1000}\right)^5\frac1{250}
=\frac{27276183}{7629394531250}.
\tag{7.5}
$$

### 7.4 Total error, including negative interpolation weights

First interpolate in density, then replace each nodal bias function by its
bias interpolant. The error is $E_\rho+\Lambda_{10}E_a$.
Replacing exact node values by the midpoints adds at most
$\Lambda_{10}\Lambda_4\cdot10^{-8}$.
Thus all signed interpolation weights and all moving laws are accounted for:

$$
\boxed{
|P(\rho,a)-T(t,x)|
\le E_\rho+32E_a+96\cdot10^{-8}
=\frac{3647592747897}{3906250000000000}
<\frac1{1000}.}\tag{7.6}
$$

The Lebesgue bounds are important: interpolating lower node endpoints alone
would be invalid because some Lagrange weights are negative.

### 7.5 Exact bivariate payment

Put $D(a)=\beta_0\beta_1>0$. The exact rational polynomial

$$
G(t,x)=D(a)\left\{T(t,x)-\frac1{1000}-\frac1{25}\right\}
-(C_0(a)-1)\{(1-\rho)\beta_1+\rho\beta_0\}
\tag{7.7}
$$

has bidegree at most $(10,8)$.
Every coefficient in its degree-$(10,8)$ tensor Bernstein basis is positive.
Likewise every degree-$(10,4)$ Bernstein coefficient of
$19-1/1000-T$ is positive. The exact arrays and downward rational bounds are
supplied in the certificate files; the minimum bounds are reported in Section 9.

For clarity, if $G(t,x)=\sum g_{ij}t^ix^j$, its Bernstein coefficient is

$$
b_{kl}=\sum_{i\le k,\,j\le l}g_{ij}
\frac{\binom{k}{i}}{\binom{10}{i}}
\frac{\binom{l}{j}}{\binom{8}{j}}.
$$

The tensor Bernstein basis is nonnegative and sums to one on the rectangle.
The auxiliary root-product bounds are verified by exact rational subdivision
using the same basis. For each Lebesgue bound, every Lagrange basis function
has constant sign between successive grid nodes, so its absolute value there
is a signed polynomial. The script fixes that sign at the interval midpoint
and certifies the resulting polynomial sum on the whole closed interval.
Thus this is a continuum sign proof. Together with (7.6), it proves

$$
\boxed{P(\rho,a)-(C_0(a)-1)d_{\rho,c}(a)\ge\frac1{25},
\qquad P(\rho,a)\le19}\tag{7.8}
$$

uniformly on $\mathcal R$.

## 8. Completion of the all-volume and entropy-rate proofs

Translate the 22-site test through the $n-21$ complete windows of $[n]$.
Their central consecutive pairs are distinct and each site has at most two
incidences. Stationarity makes each actual variational payment equal to
$P(\rho,a)$. Equations (3.2), (5.6), and (7.8) give

$$
\begin{aligned}
H_{\rho,n}''(a)
&\le n(C_0-1)d_{\rho,c}(a)-(n-21)P(\rho,a)\\
&=-n\{P-(C_0-1)d\}+21P\\
&\le-\frac n{25}+399.
\end{aligned}
$$

This proves (T). All nonselected and long-range pairs were charged by the
global envelope, not removed. The only boundary payment is the 21 missing
windows. There is no unpriced finite-compression leakage or extensive remainder.

Stationarity and the finite alphabet give
$H_{n+m}\le H_n+H_m$, so the entropy-rate value limit exists by subadditivity.
Integrating the finite-volume second-derivative bound on a chord gives

$$
\operatorname{Gap}_\lambda H_{\rho,n}
\ge\frac12\left(\frac n{25}-399\right)
\lambda(1-\lambda)(a_1-a_0)^2.
$$

Divide by $n$ and pass to the three entropy-value limits to obtain (C).
No differentiability of $h$ is assumed, and no $o(n)$ entropy-value error is
differentiated.

## 9. Computational certificates, exact inputs, and internal checks

### 9.1 Sine enclosure at every new density

`density_sine.hpp` uses the following rational bracket, proved by
`verify_density.py`:

$$
\frac{3141592653589793238}{10^{18}}<\pi<
\frac{3141592653589793239}{10^{18}}.
$$

The bracket is checked by exact alternating-series bounds in Machin's identity
$\pi=16\arctan(1/5)-4\arctan(1/239)$.
For completeness, if $\theta=\arctan(1/5)$ and $\phi=\arctan(1/239)$,
then $\tan(2\theta)=5/12$, $\tan(4\theta)=120/119$, and
$\tan(4\theta-\phi)=1$. The angle lies in $(0,\pi/2)$, giving the identity.
For rational arguments, integer modular reduction and reflection reduce
$\sin(\pi p/q)$ to $|\pi p/q|\le\pi/2<8/5$.
The degree-23 Taylor polynomial has error at most
$(8/5)^{25}/25!<10^{-20}$, verified with exact fractions.
The remaining arithmetic is outward interval arithmetic.
No value of $\sqrt3/(2\pi)$ is substituted at a new density.

### 9.2 Complete actual probabilities and reference-test construction

`density_witness.cpp` uses sequential conditional DPP probabilities.
For a current conditional kernel $K$, let $q=K_{00}$. The two child weights
are multiplied by $q$ and $1-q$, and the remaining kernels are respectively

$$
K^{(1)}=K_{RR}-K_{R0}K_{0R}/q,\qquad
K^{(0)}=K_{RR}+K_{R0}K_{0R}/(1-q).
$$

These follow from the DPP determinant generating identity, or its block Schur
complement. They are actual conditional output kernels. The latent-channel
representation implies $a\le q\le a+c$ at every node; intersecting an interval
diagonal with these bounds is therefore sound.

The binary recursion enumerates every complete word exactly once. All four
prefixes of the first two bits are processed, every leaf has a positive lower
probability, and the total mass interval contains one. The reference test is
constructed from these enclosed probabilities using (5.8), not from an
unverified inverse or an optimizer. Every nodal expectation is subsequently
summed over the same complete set of $2^{22}$ configurations.

The build run encloses the reference total mass in
$[0.9999999999999094645,1.0000000000000905489]$ and gives
$\|V_0\|_\infty\le1485.550333$,
$\|V_1\|_\infty\le9201.505796$.
The exact bounds used in the proof remain 1500 and 10000.

### 9.3 Run ledger

All runs below were completed in this session. The environment was x86-64,
GCC 14.2.0, Python 3.13.5, with four OpenMP threads for the guard and
whole-word programs. No independent second reviewer is claimed.

| Certificate | Completed result |
|---|---|
| Global pair envelope | 60/60 closed bias cells; 24,292 scalar boxes |
| Guarded pair envelope | 1,536/1,536 root word/cell jobs; zero failures; 1,562 accepted leaves; 26 parameter splits; 97,947,085 inner boxes including parent attempts |
| Guard coverage audit | Exact rational union checked for all 256 words; interior-disjoint closed leaves cover the entire rectangle; 94,459,902 boxes in successful leaves |
| Reference test | All 4,194,304 words; positive probability lower bounds; mass interval contains 1; both uniform potential bounds verified |
| Moving-law nodes | All 55 nodes, each with all 4,194,304 words; positive lower bounds and mass normalization; every rounded interval has width at most $2/10^8$ |
| Continuum interpolation allowance | Exact total $3647592747897/3906250000000000=0.000933783743461632<1/1000$ |
| Payment polynomial | All 99 tensor Bernstein coefficients positive; minimum exact coefficient $17107889404629337/600000000000000000000$; every coefficient is at least $28513/10^9$ |
| Upper-payment polynomial | All 55 tensor Bernstein coefficients positive; minimum $125473547/200000000=0.627367735$ |
| Reference cross-check | All five new nodes at $\rho=1/3$ overlap the S63 polynomial enclosures; this comparison is diagnostic, not a premise of the new certificate |
| Outside probes | Complete actual-law expectations at $(\rho,a)=(17/50,3/125)$ and $(1/2,3/125)$; exact rational negative sufficient-payment gaps |

The raw execution logs, full exact coefficient arrays, and coverage scripts
are included. Their summaries are not substitutes for the source algorithms
and enclosure proofs above.

The arithmetic helper is the supplied S63 outward helper, unchanged. It uses
64-significand-bit binary `long double`, an outward adjacent representable
number after elementary operations, volatile elementary results, and disabled
floating contraction/reassociation. Logarithms use a positive atanh series
with a geometric tail. Square-root upper bounds are checked by outward
squaring. The arithmetic self-test additionally passes 138,828 exact-rational
comparisons in all four rounding modes. This is an audit in addition to the
enclosure argument, not a replacement for it.

### 9.4 Reproduction

The companion directory `certificates/` contains all new source files, exact
inputs, generated rational coefficient arrays, and run records. It also
contains the unchanged arithmetic dependencies. The PR129 task branch already
contains the governing `PACKET.md` and `sources/` tree, so this submission does
not duplicate those source files.

Run from `certificates/` on an x86-64 C++17 environment with GCC, Boost headers,
and OpenMP:

```sh
set -eu
CXX=${CXX:-g++}
FLAGS='-O3 -frounding-math -ffp-contract=off -std=c++17'
$CXX $FLAGS arithmetic_selftest.cpp -o arithmetic_selftest
$CXX $FLAGS density_global.cpp -o density_global
$CXX $FLAGS -fopenmp density_guard.cpp -o density_guard
$CXX $FLAGS -fopenmp density_witness.cpp -o density_witness
./arithmetic_selftest
python3 verify_density.py --constants-only
./density_global 1009 3000
./density_guard 0 1536 4 > guard_run.log 2>&1
python3 check_guard_coverage.py guard_run.log
./density_witness build
./density_witness nodes 0 55 > nodes_run.log
python3 collect_nodes.py nodes_run.log nodes_integer.txt
python3 verify_density.py
./density_witness probe 17 50 3 125 > probe_034.log
./density_witness probe 1 2 3 125 > probe_half.log
python3 verify_probes.py
```

The local binary test cache is a regenerated intermediate, not a supplied
mathematical input. The proof is in the finite algorithms, their interval
invariants, the exact data, and the rational closure—not in recognizing a
success string. The coverage checks concern mathematical word/node/parameter
coverage, not file hashes or checksums.

## 10. Falsification attempts and precise limits

**Infinite-operator perturbation.** A putative estimate
$\|Q_{\rho+\delta}-Q_\rho\|_{\rm op}=O(\delta)$ is false by (2.3).
The nested-subspace rule, rather than such an estimate, is load-bearing here.

**Diagonal density evolution.** Density variation is not a common diagonal
shift. At $\rho=1/3$, the derivative of the nearest off-diagonal entry is
$1/2$, not zero. For the two-site atom

$$
p_{11}=(a+c\rho)^2-c^2Q_\rho(0,1)^2,
$$

the true density derivative is
$2c(a+c\rho)-2c^2Q_\rho(0,1)\cos(\pi\rho)$.
An a-only evolution would omit the second, nonzero term.

**Coarse guard transport.** Some coarse parameter boxes did not close, and a
200,000-node inner limit was insufficient even for several valid caps.
Those failures were not treated as counterexamples. The final verifier uses
larger inner budgets, outward sine entries, and parameter subdivision, and
only its completed coverage is used for (T).

**Unchanged witness beyond the proved band.** The actual-law probe values and
the resulting exact sufficient-inequality obstruction are:

In both rows $a=3/125$, and the same affine matrix $B_z$ and fixed test $f$
are used exactly as in (5.5) and (5.8). Every displayed decimal endpoint is
a terminating rational; all intervals are outward.

| Density | Actual expectation $P$ | $P-(C_0-1)d_{\rho,c}$ |
|---|---|---|
| $17/50=0.34$ | $[17.71884993,\ 17.71884994]$ | $[-0.06194256,\ -0.06194254]$ |
| $1/2$ | $[-105.36618178,\ -105.36618177]$ | $[-122.92793866,\ -122.92793864]$ |

The exact Fisher payments subtracted in the two rows are, respectively,
$219737025/12358112$ and $651090475/37074336$.
`verify_probes.py` checks the subtraction with rational arithmetic.
Validity of these particular global/guard caps outside the proved rectangle
is **not** asserted; the displayed payment inequality already fails even
before trying to justify those additional hypotheses.

Thus simply carrying the unchanged test and allocation to half density cannot
prove the desired theorem. This is an obstruction to that finite variational
certificate, not to actual entropy-rate concavity, and not to a redesigned
witness, different allocation, or other argument. The present density endpoint
is certified, not claimed optimal.

**Remaining inequality for further transport.** After supplying valid global
and guarded caps at a new density, the outstanding sufficient inequality is
precisely

$$
E_{\rho,a}V_{\rm new}(a,Y)
-(C_{0,\rm new}(\rho,a)-1)
\left\{\frac{1-\rho}{a(1-a)}+
\frac\rho{(a+19/20)(1-a-19/20)}\right\}>0
$$

uniformly over the proposed extension, with PSD allocation and a finite upper
bound on the expectation. Nothing here asserts that this inequality is
necessary for entropy concavity. No unpaid inequality remains inside
$\mathcal R$.

## 11. Dependency and scope ledger

| Item | Status and use |
|---|---|
| Drive `TASK.md`, `CONTRACT.md`, `TARGET.md`, `SOURCE_STATUS.md` | Governing task and accepted-scope inputs; preserved in the original packet |
| `sources/S63_RESULT.md`, Sections 2–8 | Source of the latent/score allocation framework and candidate 22-site test; inference and normalizations rederived above |
| `sources/S63_REVIEW.md` | Accepted fixed-density scope and withdrawn guard-factor diagnosis; not treated as a density certificate |
| `sources/SA02_FULL_BLOCK.md`, `sources/SA02_REVIEW.md` | Supporting actual-law score identities; no unproved half-density sign or curvature bridge imported |
| S63 guard integer data | Exact candidate cap data, independently re-certified on the new density rectangle |
| S63 fixed-density payment polynomial | Not used to certify the new nodal expectations or density remainder |
| Nested-subspace endpoint rule, analytic finite-law majorant, tensor remainder | Proved in this submission |
| New global, guard, whole-word, and bivariate rational certificates | Executed and internally checked; exact inputs and source supplied |
| Theorem (T), entropy-rate chord (C) | PROVED on the declared rectangle only |
| Fixed unchanged-witness payment in the documented outside probes | DISPROVED for that certificate only |
| Reaching $\rho=1/2$; all-density/all-contrast/all-legal-bias theorem | INCOMPLETE; no actual-model counterexample claimed |

No outside mathematical result is invoked without a proof or an embedded,
explicitly scoped source. No cyclic-law replacement, count entropy, spectral
trace entropy, all-exterior truncation, or differentiation of an entropy-value
error is used. This submission owns density transport only.

## Appendix A. Exact guard-cap integers

For word $z=\sum_{r=0}^7 2^r y_{O_r}$, the following successive rows are
$(L_z,U_z)$ in the definition (4.4).

```text
8756 8341
9496 9213
9998 9871
10021 9769
10489 10278
10362 10502
10131 10351
9743 10175
10330 10813
10052 10486
9881 10192
9139 9652
9350 10062
9048 9992
9389 10062
9076 9648
10330 10813
10313 10805
10151 10340
9834 9906
10151 10151
9890 9925
9506 9582
9444 9521
10069 10077
9848 9874
9657 9697
9567 9611
9641 9683
9737 9771
9681 9718
9620 9660
10489 10278
10712 10750
10529 10885
10092 10124
10151 10151
10112 10123
9709 9812
9416 9557
10151 10151
10043 10058
9710 9764
9316 9403
9436 9526
9585 9653
9596 9662
9383 9463
9350 10062
9413 9897
9389 9547
8593 8822
9436 9526
9124 9228
8912 9035
9015 9123
9641 9683
9579 9623
9498 9547
9506 9553
9495 9546
9590 9632
9531 9577
9548 9591
9998 9871
10330 10148
10691 10489
10323 10411
10529 10885
10151 10340
9953 10045
9543 9756
10151 10340
10142 10145
9907 9957
9242 9386
9389 9547
9426 9563
9581 9690
9257 9400
9881 10192
9991 10052
9907 9957
8927 9089
9710 9764
9168 9260
8974 9081
9049 9147
9657 9697
9522 9568
9458 9508
9476 9524
9498 9547
9545 9589
9481 9529
9502 9548
10131 10351
10085 10437
9953 10045
8608 8992
9709 9812
8766 8971
8203 8468
8293 8532
9506 9582
9186 9278
8974 9081
8941 9047
8912 9035
9108 9206
9006 9110
8985 9086
9389 10062
9523 9896
9581 9690
8856 9029
9596 9662
9200 9289
9006 9110
9085 9179
9681 9718
9557 9600
9481 9529
9494 9541
9531 9577
9584 9625
9512 9558
9531 9574
9496 9213
10023 9930
10330 10148
10330 10130
10712 10750
10366 10687
10085 10437
9682 10118
10313 10805
10143 10424
9991 10052
9224 9365
9413 9897
9251 9825
9523 9896
9173 9353
10052 10486
10143 10424
10142 10145
9377 9498
10043 10058
9468 9537
9186 9278
9230 9315
9848 9874
9622 9662
9522 9568
9521 9566
9579 9623
9632 9671
9557 9600
9555 9597
10362 10502
10366 10687
10151 10340
9446 9658
10112 10123
9417 9541
8766 8971
8733 8927
9890 9925
9468 9537
9168 9260
9060 9156
9124 9228
9304 9387
9200 9289
9117 9208
9048 9992
9251 9825
9426 9563
8863 9043
9585 9653
9304 9387
9108 9206
9184 9272
9737 9771
9632 9671
9545 9589
9546 9589
9590 9632
9654 9690
9584 9625
9591 9630
10021 9769
10330 10130
10323 10411
9683 9936
10092 10124
9446 9658
8608 8992
8353 8742
9834 9906
9377 9498
8927 9089
8583 8769
8593 8822
8863 9043
8856 9029
8616 8799
9139 9652
9224 9365
9242 9386
8583 8769
9316 9403
9060 9156
8941 9047
9021 9119
9567 9611
9521 9566
9476 9524
9498 9545
9506 9553
9546 9589
9494 9541
9523 9567
9743 10175
9682 10118
9543 9756
8353 8742
9416 9557
8733 8927
8293 8532
8403 8618
9444 9521
9230 9315
9049 9147
9021 9119
9015 9123
9184 9272
9085 9179
9069 9162
9076 9648
9173 9353
9257 9400
8616 8799
9383 9463
9117 9208
8985 9086
9069 9162
9620 9660
9555 9597
9502 9548
9523 9567
9548 9591
9591 9630
9531 9574
9561 9601
```

## Appendix B. Complete rational nodal expectations

Each row is `j k lower_numerator upper_numerator denominator` for
$P(\rho_j,a_k)$ at (7.1). The interpolation uses the exact midpoint of each
row, with a proved error at most $10^{-8}$.

```text
# j k lower_numerator upper_numerator denominator
0 0 1833166929 1833166930 100000000
0 1 1823833375 1823833376 100000000
0 2 1813868159 1813868160 100000000
0 3 1803265306 1803265307 100000000
0 4 1792018865 1792018866 100000000
1 0 1833908419 1833908420 100000000
1 1 1824371603 1824371604 100000000
1 2 1814201570 1814201571 100000000
1 3 1803392354 1803392355 100000000
1 4 1791938010 1791938011 100000000
2 0 1834574382 1834574383 100000000
2 1 1824834011 1824834012 100000000
2 2 1814458871 1814458872 100000000
2 3 1803443004 1803443005 100000000
2 4 1791780474 1791780475 100000000
3 0 1835164655 1835164656 100000000
3 1 1825220436 1825220437 100000000
3 2 1814639901 1814639902 100000000
3 3 1803417099 1803417100 100000000
3 4 1791546100 1791546101 100000000
4 0 1835679071 1835679072 100000000
4 1 1825530716 1825530717 100000000
4 2 1814744500 1814744501 100000000
4 3 1803314478 1803314479 100000000
4 4 1791234731 1791234732 100000000
5 0 1836117465 1836117466 100000000
5 1 1825764686 1825764687 100000000
5 2 1814772504 1814772505 100000000
5 3 1803134982 1803134983 100000000
5 4 1790846208 1790846209 100000000
6 0 1836479670 1836479671 100000000
6 1 1825922181 1825922182 100000000
6 2 1814723750 1814723751 100000000
6 3 1802878449 1802878450 100000000
6 4 1790380372 1790380373 100000000
7 0 1836765518 1836765519 100000000
7 1 1826003036 1826003037 100000000
7 2 1814598075 1814598076 100000000
7 3 1802544717 1802544718 100000000
7 4 1789837063 1789837064 100000000
8 0 1836974839 1836974840 100000000
8 1 1826007082 1826007083 100000000
8 2 1814395314 1814395315 100000000
8 3 1802133623 1802133624 100000000
8 4 1789216119 1789216120 100000000
9 0 1837107465 1837107466 100000000
9 1 1825934153 1825934154 100000000
9 2 1814115300 1814115301 100000000
9 3 1801645003 1801645004 100000000
9 4 1788517378 1788517379 100000000
10 0 1837163226 1837163227 100000000
10 1 1825784080 1825784081 100000000
10 2 1813757868 1813757869 100000000
10 3 1801078692 1801078693 100000000
10 4 1787740678 1787740679 100000000
```

## Appendix C. Downward Bernstein numerators

The following 11 rows, each of length 9, are downward lower bounds for the
Bernstein coefficients of (7.7), with common denominator $10^9$.
They correspond to density index $k=0,\ldots,10$ and bias index
$l=0,\ldots,8$. Every entry is positive. The complete exact fractions, and the
upper-payment coefficient array, are supplied in the companion files.

```text
28513 53291 71786 84030 90058 89912 83642 71302 52953
33963 58094 75930 87503 92849 92014 85046 72003 52944
38929 62409 79583 90482 95145 93617 85948 72198 52431
43410 66237 82743 92963 96940 94719 86352 71896 51412
47400 69567 85408 94953 98242 95321 86245 71076 49887
50906 72418 87582 96439 99034 95417 85642 69766 47852
53917 74759 89252 97430 99334 95013 84524 67931 45309
56441 76621 90432 97918 99123 94100 82905 65600 42254
58469 77975 91108 97905 98412 92682 80773 62750 38687
60004 78838 91285 97388 97193 90755 78132 59392 34607
61044 79200 90960 96366 95467 88318 74980 55520 30012
```
