# S70 — An explicit contrast interval for true configuration entropy

**Status: PROVED for the substantial subrectangle stated below.**  
**Status of the full requested rectangle through `c = .96`: INCOMPLETE.**  
**A separate, precisely scoped obstruction to the fixed witness used here is PROVED.**

Date: 2026-09-19. Task: S70, repository `cat5779/rl01`, PR45,
branch `research/sa-cycle11-pr128-20260918`.

This is a computer-assisted proof with explicit mathematical reductions,
outward-enclosing finite arithmetic, and exact rational continuum closure.
The accompanying source files and integer inputs are part of the certificate;
log messages alone are not premises. The proof uses the true sine-compression
configuration law throughout. It does not use a cyclic approximation, count
entropy, kernel spectral entropy, or an entropy-value error differentiated in a.

## 1. The theorem, its width, and its scope

All logarithms are natural. On the integer lattice,

\[
Q_\rho(i,i)=\rho,\qquad
Q_\rho(i,j)=\frac{\sin(\pi\rho(i-j))}{\pi(i-j)}\quad(i\ne j).
\]

Finite volumes below are indexed by `{0,...,n-1}`; this is just a stationary
translation of the indexing in the task. For any function f define
`Gap_lambda f = f((1-lambda)a_0+lambda a_1)
-(1-lambda)f(a_0)-lambda f(a_1)`.

Put rho = 1/3, b = 1-c, and a = bp. Define

\[
\mathcal R=\left[\frac{19}{20},\frac{1907}{2000}\right]
 \times\left[\frac{21}{50},\frac{12}{25}\right]
 =[.95,.9535]\times[.42,.48]
\]

in the coordinates (c,p). For the actual finite DPP

\[
\pi_{a,c,n}=\operatorname{DPP}(aI+cQ_{1/3,n}),\qquad
H_n(a,c)=-\sum_{y\in\{0,1\}^n}\pi_{a,c,n}(y)\log\pi_{a,c,n}(y),
\]

where Q is the finite compression of the infinite sine projection, the following
holds uniformly:

\[
\boxed{\quad \partial_a^2 H_n(a,c)\le -\frac n{25}+441,
\quad n\ge22,\quad(c,a/(1-c))\in\mathcal R.\quad}                 \tag{1.1}
\]

The derivative in (1.1) is taken with c fixed. It is not a derivative along a
curve with changing contrast.

Consequently, for every fixed c in [.95,.9535], every

\[
a_0,a_1\in[.42(1-c),.48(1-c)],\quad 0\le\lambda\le1,
\]

and the entropy rate h(a,c) = lim H_n(a,c)/n,

\[
\boxed{\quad
\operatorname{Gap}_\lambda h(\cdot,c)
\ge \frac{\lambda(1-\lambda)}{50}(a_1-a_0)^2.
\quad}                                                        \tag{1.2}
\]

There is also a stronger nested theorem:

\[
\boxed{\quad \partial_a^2H_n(a,c)\le -\frac n5+441,
\quad n\ge22,\quad
c\in[.95,.953],\quad p\in[.42,.48].\quad}                        \tag{1.3}
\]

Its entropy-rate chord coefficient is 1/10 instead of 1/50.

The certified contrast width in (1.1) is **7/2000 = .0035**, with the entire
requested p-width **3/50 = .06**. Thus it covers 35 percent of the proposed
contrast extension from .95 to .96, and proves new entropy-rate intervals at
contrasts strictly above .95. The upper-contrast legal bias interval is
[.01953,.02232], not the original fixed-a interval [.021,.024].

At c=.95 the accepted S63 theorem has the smaller boundary constant 399.
There is no claim that (1.1) improves that finite-volume boundary constant.
The advance is the closed, explicitly certified contrast interval; the stronger
nested curvature statement is an additional result. No density extension,
concavity in contrast, or assertion about every legal bias is made.

### Precisely scoped obstruction

Extend the explicit affine cap and the explicit fixed-test potential defined
below as formulas to c=24/25=.96, p=9/20=.45. Their actual-law payment obeys

\[
\boxed{\quad P(c,p)-(C(c,p)-1)d(a,c)<-3.\quad}                  \tag{1.4}
\]

Therefore **this particular witness and affine cap cannot establish a positive
payment margin on the full proposed rectangle through .96**. This is not a
counterexample to entropy-rate concavity, not an impossibility theorem for a
redesigned witness, and not a claim that all cap/PSD hypotheses extend to .96.
The full target remains incomplete.

## 2. Required properties of the reusable tool

The requirements were recorded before the construction in `TOOL_SPEC_INITIAL.md`.
The final relaxation is recorded in `TOOL_SPEC.md`. In mathematical form the tool
must have these five properties:

1. **Actual-law compatibility.** It applies to all configurations of the genuine
   finite compression, including rare configurations and effects of observations
   outside a local test window.
2. **Correct derivative order.** Its conclusion controls the common diagonal
   shift second derivative at fixed c. Contrast transport must be a separate,
   justified multivariate evolution.
3. **Normalization.** Moving the parameters transports the complete normalized
   probability vector, not only selected statistics or sampled configurations.
4. **Scaling and boundary.** A fixed-size local payment competes with an extensive
   complete-data Fisher budget; the missing-window boundary is kept explicitly.
5. **Quantitative payment.** On a closed parameter set the local payment exceeds
   `(C-1)d` by an explicit positive amount, with an explicit upper bound on payment.

The construction combines two reusable ideas. The first is a **pointwise PSD
block allocation with only pairwise endpoint exclusion**, followed by conditional
expectation and variational duality. The second is an **exact signed tensor-channel
transport**, with a Walsh-coordinate implementation and a whole-vector tail bound.
Both are proved below; neither is a generic continuity argument.

## 3. Actual latent law and complete-data information

### 3.1 The exact channel representation

Let X be the stationary DPP with the infinite sine projection Q. Conditional on X,
independently at every site, sample

\[
\mathbb P(Y_i=1\mid X)=a+cX_i.                                 \tag{3.1}
\]

For any finite S, expanding the product gives

\[
\mathbb E\prod_{i\in S}Y_i
 =\sum_{T\subset S}a^{|S|-|T|}c^{|T|}\det Q_T
 =\det(aI+cQ)_S.
\]

Inclusion probabilities determine a binary law by inclusion-exclusion. Hence
(3.1) is exactly the law in the task, on every finite set. This argument never
replaces Q_n by a projection.

For completeness, Q itself is the Fourier multiplier by the indicator of the
arc of length 2 pi rho, hence an orthogonal projection on l2(Z). For every finite
set the quadratic forms of Q_S and I-Q_S are strictly positive: a nonzero finite
trigonometric polynomial cannot vanish on an arc. Thus the finite DPP laws can
be defined by their positive L-ensemble densities. Their determinant inclusion
probabilities are consistent, giving the infinite process. Only this infinite
operator is a projection; its finite compression is not.

On a compact legal parameter set, every n-word satisfies

\[
\pi_{a,c,n}(y)\ge \min(a,1-a-c)^n>0.                            \tag{3.2}
\]

Indeed every conditional channel factor, for either outcome and either latent
bit, is at least that minimum. In particular every finite entropy and every
finite score used below is smooth in the legal interior. No support truncation
is permitted or used.

### 3.2 Common-shift Fisher budget

The complete-data common-a score is

\[
S^{\rm full}=\sum_i
 \frac{Y_i-(a+cX_i)}{(a+cX_i)(1-a-cX_i)}.
\]

Its summands have conditional mean zero and are conditionally independent given
X. Therefore

\[
\mathbb E(S^{\rm full})^2=n\,d(a,c),\qquad
 d(a,c)=\frac{1-\rho}{a(1-a)}+
        \frac{\rho}{(a+c)(1-a-c)}.                             \tag{3.3}
\]

Differentiating the finite sum over X shows that the observed score is the
conditional expectation of this score given Y. Conditional Jensen gives

\[
J_n:=\mathbb E(\partial_a\log\pi_{a,c,n})^2\le n d(a,c).        \tag{3.4}
\]

Here and below every expectation is under the actual current law.

There is also a genuinely multivariate information bound. In the coordinates
(c,p), the channel success parameter for X_i=x is
`b_x=(1-c)p+cx`, with gradient `(x-p,1-c)`. The complete-data Fisher matrix per
site is exactly

\[
\mathcal I(c,p)=\sum_{x=0}^1w_x
 \frac{\binom{x-p}{1-c}(x-p,1-c)}{b_x(1-b_x)},
\quad w_0=1-\rho,\ w_1=\rho.                                  \tag{3.5}
\]

The observed two-parameter Fisher matrix is at most n times (3.5) in Loewner
order, by conditional expectation of any linear combination of the two scores.
The scalar budget (3.3) is the pp entry divided by `(1-c)^2`, as it must be since
`partial_a=(1-c)^{-1} partial_p` with c fixed. Thus there is no coordinate-scaling
ambiguity in the extensive budget.

## 4. Exact score identities and the entropy interface

Temporarily allow distinct diagonal parameters a_i. For a finite observation
word y put

\[
M_y=K-\operatorname{diag}(1-y),\quad G_y=M_y^{-1},\quad Z_i=(G_y)_{ii}.
\]

The full configuration probability is

\[
\pi(y)=(-1)^{\#\{i:y_i=0\}}\det M_y.                            \tag{4.1}
\]

This follows directly by inclusion-exclusion applied to determinant inclusion
probabilities; it also follows from the L-ensemble formula. It is strictly
positive, so M_y is invertible. Differentiating its determinant gives

\[
Z_i=\partial_{a_i}\log\pi(y),\qquad
\frac{\partial_{a_i}\partial_{a_j}\pi}{\pi}
 =Z_iZ_j-|G_{ij}|^2\quad(i\ne j).                              \tag{4.2}
\]

There is a useful direct channel version. Let y^i be the word with bit i flipped
and let `Delta_i g=g(y_i=1)-g(y_i=0)`. Multiaffinity of the channel gives

\[
\partial_{a_i}\pi(y)=(2y_i-1)\pi_{-i}(y_{-i}),\quad
 Z_i=(2y_i-1)\left(1+\frac{\pi(y^i)}{\pi(y)}\right),\quad
 \mathbb E Z_i g=\mathbb E\Delta_i g.                           \tag{4.3}
\]

The last identity holds for any finite test g at the parameters under
consideration. It does not differentiate g. Summing (4.2) over the two target
bits while fixing all other bits proves the weighted identity

\[
\mathbb E\bigl[w(Y_{-\{i,j\}})Z_iZ_j\bigr]
 =\mathbb E\bigl[w(Y_{-\{i,j\}})|G_{ij}|^2\bigr]               \tag{4.4}
\]

for every function w independent of its own two target bits. It may depend on
other targets of a larger block. This distinction is important below.

Write `F_n=sum_i E Z_i^2`. Equation (4.4) with w=1 gives

\[
J_n=F_n+\sum_{i\ne j}\mathbb E|G_{ij}|^2.                      \tag{4.5}
\]

### 4.1 Four-atom pair ratio

Condition on all coordinates except i,j. Denote the conditional probabilities
of `00,10,01,11` by A,B,E,D respectively; the letter E here is just a table atom.
Put

\[
s=BE-AD\ge0,\qquad R=\frac{BE}{AD},\qquad
\alpha=\frac{\log R}{s(A^{-1}+B^{-1}+E^{-1}+D^{-1})},           \tag{4.6}
\]

with alpha=1 at s=0. Positivity and the nonnegative s will also follow explicitly
from the posterior construction in Section 5. The conditional pair kernel has
means q,r and squared off-diagonal magnitude s, so

\[
 A=(1-q)(1-r)-s,\quad B=q(1-r)+s,
\quad E=(1-q)r+s,\quad D=qr-s.                                \tag{4.7}
\]

By the block inverse formula, the target block of G_y is the inverse of the
Schur complement after fixing the other observed coordinates. Formula (4.1)
identifies that Schur complement with the masked conditional pair kernel.
The inverse of this masked two-by-two matrix therefore gives

\[
\mathbb E(|G_{ij}|^2\mid Y_{-\{i,j\}})
 =s(A^{-1}+B^{-1}+E^{-1}+D^{-1}).                              \tag{4.8}
\]

Also `partial_{a_i}partial_{a_j}pi(y)` equals the marginal mass of the other
bits times `(2y_i-1)(2y_j-1)`. Differentiating entropy twice in the common shift,
including the acceleration of the actual probabilities, therefore gives exactly

\[
H_n''=\sum_{i\ne j}\mathbb E_{-\{i,j\}}\log R-J_n.             \tag{4.9}
\]

To check the sign in (4.9), the mixed derivative contributes
`-[log A-log B-log E+log D]=log(BE/AD)`. No same-site second probability derivative
occurs, since each a_i enters multiaffinely. The second term in (4.9) is the full
observed Fisher information, not only its diagonal part.

Suppose every pair has alpha at most C, and selected unordered pairs have the
sharper cap `alpha <= C-delta_ij`, where delta is nonnegative and independent of
its pair's endpoints. Equations (4.5), (4.8), and (4.9) imply

\[
H_n''\le (C-1)J_n-CF_n
              -2\sum_{\{i,j\}}\mathbb E\delta_{ij}|G_{ij}|^2.  \tag{4.10}
\]

Pairs not assigned a guard improvement keep the global cap. All long-range
pairs are retained in (4.10); they are not discarded as a leakage approximation.

### 4.2 PSD block allocation: a reusable theorem

Choose a local window of length m and a target set T inside it. For each
translated window W wholly contained in the n observations, let
`B_W(Y_W)` be a real symmetric matrix indexed by its targets. Assume:

* `B_W(y_W)` is PSD for every complete local word;
* each off-diagonal entry `(B_W)_{ij}` is independent of bits i and j;
* the diagonal entries allocated to any site sum to at most C pointwise;
* for any selected pair, the off-diagonal entries allocated to that pair sum
  to at most delta_ij pointwise, with pair-endpoint-free residual;
* each B_W is measurable in the full local window, not necessarily outside all
  of its target bits.

Then

\[
CF_n+2\sum_{\{i,j\}}\mathbb E\delta_{ij}|G_{ij}|^2
 \ge\sum_W\mathbb E\,Z_{T_W}^{\mathsf T}B_W(Y_W)Z_{T_W}.        \tag{4.11}
\]

**Proof.** Subtract the right side. The remaining diagonal terms have
nonnegative coefficients multiplying `Z_i^2`. By (4.4), the remaining pair
terms equal twice their nonnegative pair-endpoint-free residual coefficients
multiplying `|G_ij|^2`. Their expectations are nonnegative. It would be wrong to
justify (4.11) by pointwise positivity of signed products Z_i Z_j; the weighted
identity is essential. This proves (4.11).

For i in W, marginal differentiation of a finite sum gives the score martingale

\[
\mathbb E(Z_i\mid Y_W)=z_i^W:=\partial_{a_i}\log\pi_W(Y_W).
\]

Since B_W is measurable in **the whole window**, conditional covariance gives

\[
\mathbb E(Z_{T_W}^{\mathsf T}B_WZ_{T_W}\mid Y_W)
 \ge (z^W)^{\mathsf T}B_W z^W.                                \tag{4.12}
\]

For any fixed vector of local test functions f, pointwise PSD completion of the
square and (4.3) give

\[
\mathbb E(z^W)^{\mathsf T}B_Wz^W
\ge\mathbb E\left[2\sum_{i\in T_W}\Delta_i(B_Wf)_i
                     -f^{\mathsf T}B_Wf\right].              \tag{4.13}
\]

This proves the claimed interface even when an entry B_ij depends on a third
target bit. Requiring the entire matrix to exclude every target bit would be
an unnecessary restriction. The preliminary tool proposal had that stronger
restriction; (4.11)-(4.13) are the proof of its relaxation.

For a stationary witness define its actual-law payment

\[
P(c,p)=\mathbb E_{c,p,m} V_{c,p},\qquad
V_{c,p}=2\sum_{i\in T}\Delta_i(Bf)_i-f^{\mathsf T}Bf.            \tag{4.14}
\]

If C>=1 and the block budgets above hold, combining (3.4) and (4.10)-(4.14)
yields

\[
H_n''\le n(C-1)d-(n-m+1)P.                                    \tag{4.15}
\]

Thus the fully quantitative sufficient interface is

\[
P-(C-1)d\ge\eta>0,\qquad P\le M
\quad\Longrightarrow\quad
H_n''\le-\eta n+(m-1)M.                                      \tag{4.16}
\]

This theorem is not imported at new parameters without checking its hypotheses.
Sections 5-9 check every hypothesis on the new contrast rectangle.

## 5. Posterior projection geometry and robust guard comparisons

### 5.1 Posterior Gram formula

The likelihood ratio of one observed channel output, as a function of its latent
bit, is a constant times a diagonal field

\[
d_+(a,c)=\frac{a+c}{a}\quad(Y_i=1),\qquad
 d_-(a,c)=\frac{1-a-c}{1-a}\quad(Y_i=0).                         \tag{5.1}
\]

Unobserved coordinates have field 1. For a bounded positive diagonal field D
let H=Ran(Q) and `M_D=(QDQ)|_H`. It is invertible whenever D is bounded below
by a positive constant. The tilted projection is

\[
P_D=D^{1/2}Q M_D^{-1}Q D^{1/2}.                                \tag{5.2}
\]

One algebraic proof that (5.2) is a projection is to set
A=`D^{1/2}|_H`; then (5.2) is `A(A^*A)^{-1}A^*`. Here is the complete
finite-observation identification. If D differs from I only on a finite set S,
expanding `prod_{i in S}[1+(d_i-1)X_i]` and using the determinant inclusion
probabilities gives

\[
\mathbb E\prod_i d_i^{X_i}
 =\det[I_S+(D_S-I_S)Q_S]=\det_H M_D.
\]

The last determinant is a finite-rank determinant; it equals the displayed
finite determinant by `det(I+AB)=det(I+BA)`. If T is a disjoint set of unobserved
targets and Z has arbitrary positive diagonal marks z_i there, the tilted
generating function is the ratio of the same determinants with D replaced by
DZ. Since D_T=I, the numerator operator is
`M_D+Q Pi_T (Z_T-I_T) Pi_T Q`. The determinant lemma and inversion of M_D
turn the ratio exactly into

\[
\det\{I_T+(Z_T-I_T)[Q M_D^{-1}Q]_{TT}\}.
\]

Comparison of its coefficients proves all conditional target inclusion
probabilities. The same calculation with the factors D^{1/2} inserted identifies
the full tilted kernel (5.2). Thus, conditional on any finite collection of
outputs, the latent process has that kernel; in particular its kernel on
still-unobserved targets is

\[
B_T=[Q M_D^{-1}Q]_{TT}.                                      \tag{5.3}
\]

The output pair, conditional on the other observations, then has kernel
`aI+cB_T` by the same inclusion calculation as (3.1). This proves (4.7) with
`s=c^2 |(B_T)_{ij}|^2>=0`.

All uses of projection algebra in this section are on the infinite Hilbert
space H. Finite matrices in the certificate are compressions, not projections.

### 5.2 Finite formula for infinite exterior comparisons

Let `E=T union O` consist of the targets and a finite guard. Give all coordinates
outside E the constant field d>0, and the coordinates in E specified fields D_E.
Writing V for coordinate restriction from H to E, one has
`VV^*=Q_E` and

\[
M_D=dI_H+V^*(D_E-dI)V.
\]

The identity `(dI+V^*AV)^{-1}V^*=V^*(dI+AVV^*)^{-1}` gives

\[
B_T(d,D_E)
 =\left[Q_E\{dI+(D_E-dI)Q_E\}^{-1}\right]_{TT}.                \tag{5.4}
\]

This is the finite inverse actually used. In particular it does **not** use
`Q_E^2=Q_E`. A constant field on the infinite exterior in (5.4) is an operator
comparison, not conditioning on a probability-zero infinite event.

If `D^(lo) <= D <= D^(hi)` coordinatewise, then by inversion on H,

\[
[QM_{D^{(hi)}}^{-1}Q]_{TT}
\preceq B_T\preceq[QM_{D^{(lo)}}^{-1}Q]_{TT}.                  \tag{5.5}
\]

For fixed rho, comparison with a constant exterior while keeping the one target
field equal to 1 also gives the single-site bounds

\[
L=a+\frac{c\rho}{\rho+d_+(1-\rho)},\qquad
U=a+\frac{c\rho}{\rho+d_-(1-\rho)}.                            \tag{5.6}
\]

For example, on H the single-target comparison operator is
`d I_H+(1-d) q_i q_i^*`, with `||q_i||^2=rho`. Its inverse target quadratic form
is `rho/[d+(1-d)rho]`, proving (5.6).

### 5.3 Explicit multivariate robustness, not continuity

In (c,p), `d_+` increases with c and decreases with p; `d_-` decreases with both
c and p. This follows by differentiating

\[
d_+=1+\frac{c}{(1-c)p},\qquad
 d_-=\frac{(1-c)(1-p)}{1-(1-c)p}.
\]

For a closed rectangle `[c_l,c_h] x [p_l,p_h]`, a uniform **lower** posterior
matrix comes from maximal fields:

\[
\begin{array}{c|c}
\text{location}&\text{field for the lower matrix}\\\hline
\text{target}&1\\
\text{guard bit 1}&d_+(c_h,p_l)\\
\text{guard bit 0}&d_-(c_l,p_l)\\
\text{exterior}&d_+(c_h,p_l).
\end{array}                                                  \tag{5.7}
\]

A uniform **upper** matrix uses minimal fields:

\[
\begin{array}{c|c}
\text{location}&\text{field for the upper matrix}\\\hline
\text{target}&1\\
\text{guard bit 1}&d_+(c_l,p_h)\\
\text{guard bit 0}&d_-(c_h,p_h)\\
\text{exterior}&d_-(c_h,p_h).
\end{array}                                                  \tag{5.8}
\]

Every remaining finite observed field, and every unobserved field 1, lies
between the exterior extremes. Equations (5.4)-(5.8) therefore enclose every
actual posterior compatible with that guard, throughout the parameter cell and
for any surrounding finite volume.

On the certified rectangle all actual fields, including the field 1, obey
the explicit uniform bounds

\[
\frac1{41}<\frac{1209}{48884}=d_-(c_h,p_h)
\le D_{ii}\le d_+(c_h,p_l)=\frac{97303}{1953}<50.
\]

Thus the derivative estimates below can take the uniform numerical value
`mu=1/41`, independently of the number of surrounding observations.

Quantitative derivative control is available as well. If `D>=mu I`, then

\[
\partial_r M_D^{-1}=-M_D^{-1}(\partial_rM_D)M_D^{-1},
\quad \|\partial_r B_T\|\le\frac{\|\partial_rD\|}{\mu^2},
\]

and

\[
\|\partial_r\partial_s B_T\|
\le \frac{2\|\partial_rD\|\|\partial_sD\|}{\mu^3}
    +\frac{\|\partial_r\partial_sD\|}{\mu^2}.                  \tag{5.9}
\]

These follow by differentiating the inverse and using that Q and coordinate
restriction are contractions. Thus the posterior interface has genuine
multivariate derivative bounds. The certificate uses the sharper ordered-field
bounds (5.7)-(5.8), rather than paying their much looser Lipschitz constants.

### 5.4 The valid numerical Loewner radius

Interval inversion of the *single mixed-corner matrix* (5.4), followed by
symmetrization of its off-diagonal interval, gives enclosures of its three real
entries. If their chosen midpoints are x,y,w and their absolute error bounds
are e_x,e_y,e_w, set

\[
\varepsilon=\operatorname{up}(\max(e_x,e_y)+e_w).               \tag{5.10}
\]

The symmetric error matrix has operator norm at most its maximum absolute row
sum, hence at most (5.10). Subtracting epsilon I from a lower midpoint matrix,
or adding it to an upper midpoint matrix, gives rigorous Loewner bounds.
**No factor-two modification is needed.** The implementation always uses the
computed epsilon itself. Increasing an optional abort threshold from `1e-8` to
`1e-6` only permits a slightly wider, explicitly paid enclosure; it never replaces
epsilon by a smaller number or assumes an error away.

## 6. A scalar envelope and the continuum cap certificates

### 6.1 Closed-form reduction of the global pair cap

In the four-atom notation of Section 4 let x=R-1 and h=A+D. Since the four atoms
sum to 1 and `BE=AD+s`, direct algebra gives

\[
\alpha=\frac{\mathcal L(x)}{1+h x},\qquad
\mathcal L(x)=\frac{(1+x)\log(1+x)}x,\quad\mathcal L(0)=1.       \tag{6.1}
\]

Indeed `AD sum(1/atom)=h+(1-h)/R`, and `s=AD(R-1)`.
The function L is increasing because its derivative is
`[x-log(1+x)]/x^2>=0`.

Suppose every conditional one-site odds ratio is in `[ell,r]`, with
`0<ell<1<r` and `ell*r<1`. Then

\[
\alpha\le\max\left\{1,
\sup_{1\le R\le r^2}
\frac{R\log R(1+r+r\ell+\ell R)}
 {(R-1)[r+R(1+\ell+r\ell)]}\right\}.                           \tag{6.2}
\]

Here is a proof, included to specify exactly the scalar enclosure being used.
Scale the four atoms so that B=1 and, after exchanging the two coordinates if
necessary, E=t>=1. Set the rescaled diagonal atoms to A_0,D_0. The odds bounds
imply

\[
A_0\ge t/r,\quad D_0\ge\ell t,\quad A_0D_0=t/R,
\quad 1\le t\le r/(\ell R).
\]

To minimize h, minimize `(A_0+D_0)/(1+t)`. For `R<=r^2`, the unconstrained
minimum `2 sqrt(t/R)/(1+t)` decreases with t>=1 until `t=r^2/R`. Beyond that
point the active lower constraint is `A_0=t/r`, giving
`(t/r+r/R)/(1+t)`, whose derivative has the sign of `1/r-r/R<=0`.
The other lower constraint is satisfied up to `t=r/(ell R)` because `ell r<1`.
Taking that last endpoint gives

\[
h\ge\frac{1+r\ell}{1+r+r\ell+\ell R}.
\]

Substitution into (6.1) gives the displayed fraction in (6.2). If `R>=r^2`,
the same constrained expression is increasing in t; its minimum at t=1 is at
least `1/sqrt(R)`. Thus `h>=1/(1+sqrt(R))` and

\[
\alpha\le\frac{\sqrt R\log R}{R-1}\le1.
\]

For the last inequality put z=sqrt(R)>=1 and differentiate
`z-z^{-1}-2 log z`; its derivative is `(z-1)^2/z^2>=0` and its value at 1 is zero.
This completes the proof of (6.2).

Bounds (5.6) imply the odds bounds with `ell=L/(1-L)`, `r=U/(1-U)`.
For a parameter cell, the certificate lowers L and raises U by interval
arithmetic and mixed-corner bounds on d_+,d_-. It then checks the whole
one-dimensional R interval in (6.2), not finitely many R values.

### 6.2 Global cap used by the new witness

The global cap is

\[
\boxed{C(c,p)=\frac{1303}{1000}+\frac{51}{200}p
                         +8\left(c-\frac{19}{20}\right).}     \tag{6.3}
\]

It is greater than 1 throughout R. `quad_global.cpp` certifies (6.2)<=C on a
140 by 240 cover of the closed parameter rectangle. The cell widths are exactly
`1/40000` in c and `1/4000` in p. On each cell, monotonicity of L(x) in (6.1)
and an interval lower bound for its denominator give a uniform upper bound;
nonaccepted x intervals are bisected until accepted. The recorded complete run
accepted all 33,600 parameter cells, covering 9,201,142 scalar branch nodes,
with no failed cell.

These cells are *intervals with proofs over their interiors and boundaries*;
this is not a grid scan used as an asymptotic theorem.

### 6.3 Guard geometry and its complete cover

For a pair `(i,i+d)`, d=1,2,3, use the ordered eight-site guard

\[
O_{i,d}=\{i+k:-4\le k\le5,\ k\notin\{0,d\}\},                \tag{6.4}
\]

listed in increasing order. Its word integer is the sum of the j-th bit times
2^j, starting with j=0. All 256 guard words are included. Some guards include
other block targets, which is allowed by Section 4.2.

For a given guard word and parameter cell, (5.7)-(5.10) give

\[
\begin{pmatrix}l_x&l_w\\l_w&l_y\end{pmatrix}
 \preceq \begin{pmatrix}x&z\\z&y\end{pmatrix}
 \preceq\begin{pmatrix}u_x&u_w\\u_w&u_y\end{pmatrix}.           \tag{6.5}
\]

The guard verifier bounds alpha over every real symmetric matrix in (6.5).
This is a larger set than the actual posterior set, so success is sufficient.
Its initial box has x in `[l_x,u_x]`, y in `[l_y,u_y]`, and

\[
z\in\left[\frac{l_w+u_w}{2}
 -\frac{\sqrt{(u_x-l_x)(u_y-l_y)}}2,
 \frac{l_w+u_w}{2}
 +\frac{\sqrt{(u_x-l_x)(u_y-l_y)}}2\right].                     \tag{6.6}
\]

To prove (6.6), use the two PSD determinant inequalities from (6.5), add their
square-root bounds, and apply the two-term Cauchy-Schwarz inequality.
Each branch box is safely contracted by those same determinant inequalities:
`(x-l_x)(y-l_y)>=(z-l_w)^2` and
`(u_x-x)(u_y-y)>=(z-u_w)^2`. Impossible boxes are rejected. The code uses only
outward endpoint operations for these contractions and square-root enclosures.

For each remaining box, `q=(1-c)p+cx`, `r=(1-c)p+cy`, and `s=c^2 z^2`
are enclosed at the appropriate multilinear parameter endpoints. The atoms
(4.7) are enclosed, with the additional uniform lower bound

\[
A,B,E,D\ge\bigl[(1-c_h)\min(p_l,1-p_h)\bigr]^2>0.             \tag{6.7}
\]

This is the conditional channel bound, not an assumed determinant error bound.
Equation (6.1) is then bounded above using the upper x and lower denominator.
A box is accepted only if that upper bound is at most the specified guard cap;
otherwise its longest side is bisected. A node limit or interval inversion
ambiguity causes failure, never acceptance.

`quad_guard.cpp` implements this algorithm with a 7 by 6 parameter cover:
c cells of width `1/2000` and p cells of width `1/100`. Thus for each distance
there are exactly `7*6*256=10,752` guard-word parameter cells. The certificate
covers all of them, including rare words and all possible exterior observations.

## 7. The explicit four-target witness

Take m=22, window `{0,...,21}`, and targets

\[
T=\{9,10,11,12\}.
\]

The reference law is the actual 22-site law at

\[
c_*=19/20,\qquad a_*=1/40,\qquad p_*=1/2,
\]

and remains fixed. For i in T define the fixed variational test

\[
f_i(y)=(2y_i-1)\left(1+\frac{\pi_*(y^i)}{\pi_*(y)}\right).     \tag{7.1}
\]

This uses the same reference parameters as S63, now with four target score
components rather than the old pair. It is a test under the current law, not
an assertion that the current score equals f.

Let `(L_z,U_z)` be the 256 supplied S63 integer pairs, reproduced in Appendix A.
Define the new nearest-neighbor caps

\[
\kappa_z(p)=\frac{(3/100-p/20)L_z+(p/20-1/50)U_z}{100}
                         +\frac1{50}.                        \tag{7.2}
\]

The added 1/50 is an explicitly certified robustness allowance. The p/20 here
is the reference-contrast bias coordinate used to interpolate the fixed integer
rows. It is **not** a substitution of p/20 for the actual bias `(1-c)p` in the
probability law.

Let `t2_z` and `t3_z` be the two new nonnegative integer columns in Appendix A,
also stored in `far_tau_integer.txt` and `quad_tau3_integer.txt`. Put

\[
\delta_1=C-\kappa_z(p),\qquad
\delta_2=t2_z/1000,\qquad\delta_3=t3_z/1000.                   \tag{7.3}
\]

The guard certificates establish, uniformly,

\[
\alpha_{i,i+1}\le\kappa_z(p),\quad
\alpha_{i,i+2}\le C-t2_z/1000,\quad
\alpha_{i,i+3}\le C-t3_z/1000.                                \tag{7.4}
\]

They recheck the caps at the new parameters; the source caps are not silently
inherited as true outside their accepted scope.

For positions r=0,1,2,3 in T, define B by

\[
B_{rr}=C\,(19,11,11,19)_r/60,
\qquad
B_{rs}=\frac{\delta_{s-r}}{4-(s-r)}\quad(r<s),                 \tag{7.5}
\]

using the guard of the corresponding actual pair in every entry.

Every diagonal position occurs at most once for a given site among translated
windows, and the four weights sum to 1. Every distance-d pair occurs in at most
4-d translated blocks; its canonical guard and delta are identical in all those
occurrences. Therefore the diagonal and pair budgets of Section 4.2 hold,
including at the boundary. If a guard is not contained in the observation
volume its improvement is not used. Every pair used by a contained 22-window
has its guard contained, since the guard union lies in `{5,...,16}` within the
window.

### 7.1 Strict PSD slack, including guard dependence

The guard union has twelve bits, so B can take at most 4096 distinct word-dependent
forms. For each word B is affine in (c,p). `exact_closure.py` verifies by exact
rational LDL elimination at the four parameter corners that

\[
\boxed{\quad B(c,p,y)\succeq\frac1{200}I_4
\quad\text{for every }(c,p)\in\mathcal R\text{ and every word}.\quad} \tag{7.6}
\]

There are 16,384 checked corner matrices. The PSD cone is convex, so each
interior affine matrix is a convex combination of its four corner matrices.
This is an exact continuum argument, not a mesh inference.

For B-I/200 the smallest LDL pivots over the checked family, by elimination
position, are exactly

\[
\frac{264919}{600000},\quad
\frac{27770519749}{162143400000},\quad
\frac{1857041327595623}{20016784591800000},\quad
\frac{123417153058106747}{8256425588814980000}.
\]

All are strictly positive. These are pivot minima, not eigenvalue estimates;
the certified eigenvalue statement is precisely (7.6). Positivity of all
nearest deltas and nonnegativity of the distance-two/three allocations are
also checked exactly at the parameter corners, hence throughout.

### 7.2 Explicit potential and its parameter dependence

Since every row-i matrix entry is independent of bit i, the potential (4.14)
can be evaluated without differentiating matrix entries in those bit differences.
Set

\[
D_i(y)=2\Delta_i f_i(y)-f_i(y)^2,
\qquad
X_{ij}(y)=2[\Delta_i f_j+\Delta_j f_i-f_i f_j].                 \tag{7.7}
\]

Then

\[
V_{c,p}(y)=\sum_i B_{ii}D_i(y)+\sum_{i<j}B_{ij}(y)X_{ij}(y).
\]

Because (7.5) is affine in the two parameters, so is the whole potential:

\[
V_{c,p}=V_0+(p-1/2)V_P+(c-19/20)V_C.                          \tag{7.8}
\]

The complete-word interval calculation proves

\[
\|f_i\|_\infty<26,\quad
\|V_0\|_\infty\le2418,\quad
\|V_P\|_\infty\le461,\quad
\|V_C\|_\infty\le15266.                                      \tag{7.9}
\]

In particular none of the 2^22 words is replaced by a typical-word estimate.

## 8. Exact two-parameter channel transport

This part of the tool is independent of DPP theory. It applies to any latent
binary joint law observed through common affine Bernoulli channels.

### 8.1 Algebra, normalization, and moving derivatives

Use column probability vectors ordered as `(0,1)`, and define

\[
D=\begin{pmatrix}-1&-1\\1&1\end{pmatrix},\qquad
F=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

Their exact algebra is

\[
D^2=0,\quad F^2=F,\quad DF=0,\quad FD=D.                       \tag{8.1}
\]

Write

\[
s=(1-c)(p-1/2),\quad v=\frac{c-c_*}{c_*},\quad T=I+sD+vF.
\]

For a latent bit x the reference success probability is
`b_*=1/2+c_*(x-1/2)`. Applying T to its Bernoulli column changes it to
`b_*+s+v(b_*-1/2)=(1-c)p+cx`. Conditional independence and linearity therefore
prove the exact full-vector identity

\[
\boxed{\quad \pi_{c,p,m}
 =\prod_{i=1}^m(I+sD_i+vF_i)\pi_{*,m}.\quad}                  \tag{8.2}
\]

Both generators have zero column sum, so every T has column sums 1, and (8.2)
preserves exact normalization. The matrix T can have negative entries when
contrast increases. It is not claimed to be a Markov post-processing kernel.
Positivity of the resulting probability vector follows from the actual latent
channel identity, not from positivity of T.

Let `D_tot=sum_i D_i` and `F_tot=sum_i F_i`. Algebra (8.1) gives

\[
\partial_s\pi=D_{\rm tot}\pi,
\qquad
\partial_v\pi=\frac{F_{\rm tot}-sD_{\rm tot}}{1+v}\pi.         \tag{8.3}
\]

For example, `(F-sD)(I+sD+vF)=(1+v)F`, proving the second identity. Contrast
is not a-only nilpotence in disguise: `F^2=F`, not zero.

An explicit derivative bound, valid for k+l<=m, is

\[
\|\partial_s^k\partial_v^l\pi\|_1
\le (m)_{k+l}\,2^k(1+2|s|+|v|)^{m-k-l}.                     \tag{8.4}
\]

To prove it, differentiate the product (8.2). No site can be differentiated
twice, since its factor is affine. There are `(m)_{k+l}` assignments, each with
k factors of norm `||D||_1=2`, l factors of norm `||F||_1=1`, and the remaining
factors bounded by `1+2|s|+|v|`. The reference vector has l1 norm 1.
Derivatives of total order greater than m vanish in the variables (s,v).

For explicit correct second-order evolution in the physical coordinates, put
e=p-1/2, b=1-c. The chain rule yields

\[
\begin{aligned}
\pi_c&=-e\pi_s+\pi_v/c_*, &\pi_p&=b\pi_s,\\
\pi_{cc}&=e^2\pi_{ss}-2e\pi_{sv}/c_*+\pi_{vv}/c_*^2,
 &\pi_{pp}&=b^2\pi_{ss},\\
\pi_{cp}&=-\pi_s-be\pi_{ss}+b\pi_{sv}/c_*.
\end{aligned}                                                 \tag{8.5}
\]

At fixed c, `partial_a=partial_s`. Thus the entropy derivative in the theorem
has its stated order and normalization.

The moving payment is `P=<pi,V>`, not `<pi_*,V>`. For example,

\[
P_c=\langle\pi_c,V\rangle+\langle\pi,V_C\rangle,\qquad
P_{cp}=\langle\pi_{cp},V\rangle+
       \langle\pi_c,V_P\rangle+\langle\pi_p,V_C\rangle.        \tag{8.6}
\]

There is no missing reference derivative in (8.6): f and pi_* are deliberately
fixed variational data, while **all** derivatives of the actual law and the
affine potential are included. The certificate below evaluates the whole moving
expectation directly rather than estimating it by a frozen-law derivative.

### 8.2 Scaled Walsh coefficients

Set

\[
t=200s,\qquad u=1000(c-c_*),\qquad v=u/950.
\]

Let `H=[[1,1],[1,-1]]`, use its m-fold tensor Walsh transform, and write hats
for transformed vectors. Then `HDH^{-1}` sends a zero subset bit to a one
subset bit with coefficient -2, while `HFH^{-1}=diag(0,1)`.

For every subset S define

\[
\widehat q_0(S)=\widehat\pi_*(S),\qquad
\widehat q_{k+1}(S)=-\frac1{100(k+1)}
                      \sum_{i\in S}\widehat q_k(S\setminus\{i\}).
                                                                  \tag{8.7}
\]

If r=|S|, the coefficient of `t^k u^l` in the transported probability at S is
exactly

\[
\binom{r-k}{l}\frac{\widehat q_k(S)}{950^l}.                   \tag{8.8}
\]

To see this directly, choose the k sites whose D terms raise their subset bits;
the remaining r-k present bits each contribute `(1+v)`. Recursion (8.7) sums
all k choices with the factorial correction. Expanding `(1+v)^{r-k}` proves
(8.8). Equivalently it follows by conjugating each factor of (8.2).

By Parseval, the coefficient for a fixed potential component V_j is

\[
A^{(j)}_{kl}=2^{-m}\sum_{S:|S|\ge k+l}
 \binom{|S|-k}{l}\frac{\widehat q_k(S)\widehat V_j(S)}{950^l}.   \tag{8.9}
\]

Grouping the **products** in this exact sum by |S| is an arithmetic optimization,
not a replacement of spatial configuration entropy by count entropy. The
reference probabilities and all test values retain their full spatial words.
The normalization factor in (8.9) is exactly `1/2^22` in this application.

### 8.3 Whole-vector tail, including moving potential

Let pi_{<=8} be the exact total-degree-eight truncation in (s,v), equivalently
in (t,u). From (8.2), for `w=2|s|+|v|`,

\[
\|\pi-\pi_{\le8}\|_1
\le\sum_{r=9}^m\binom mr w^r
\le \frac{\beta^9}{9!(1-\beta/10)},\qquad \beta=mw<10.         \tag{8.10}
\]

The last inequality bounds the factorial tail geometrically: after r=9 each
successive term has ratio at most beta/10. This bounds the entire vector,
including all rare words, with no differentiated value remainder.

On R, (7.9) gives

\[
\|V\|_\infty\le2418+.08\,(461)+.0035\,(15266),
\qquad
\beta\le22\left(.008+\frac{.0035}{.95}\right).
\]

The product of these bounds and (8.10) is strictly below
`3.476374*10^{-8}` by exact rational comparison. We conservatively declare the
payment remainder to be **1/1,000,000**. This pays the tail after multiplication
by the *moving* potential, not only a probability approximation.

### 8.4 A quantitative continuation theorem

The preceding constructions give the following reusable theorem. Fix a balanced
reference contrast c_*>0, a stationary latent binary law of density rho, a window
length m, and a parameter rectangle with c>=c_*, p<=1/2 strictly inside the legal
region. Suppose the score-pair reduction of Section 4 is available. Choose an
affine cap C and word-dependent affine PSD-block candidate B with the endpoint
exclusions and allocation budgets of Section 4.2, and choose any fixed local f.
Suppose finite posterior comparison/cap certificates cover all selected guard
words and all parameter cells, and the corner matrices have an exact slack
sigma I. Let V=V_0+(p-1/2)V_P+(c-c_*)V_C, with proved component sup norms N_j.

For any truncation degree q<m, compute the **constructed** coefficients (8.7)-
(8.9), with the corresponding scaling of the chosen reference c_*. Let their
outward boxes generate signed lower and upper polynomials P_q^-,P_q^+.
Put

\[
V_{\max}=N_0+\sup|p-1/2|N_P+\sup|c-c_*|N_C,\qquad
\beta=m(2\sup|(1-c)(p-1/2)|+\sup|(c-c_*)/c_*|).
\]

If beta<q+2, the explicit correction

\[
\epsilon_q=V_{\max}\frac{\beta^{q+1}}
 {(q+1)![1-\beta/(q+2)]}                                    \tag{8.11}
\]

pays the entire omitted actual-law vector. If exact Bernstein or other rigorous
continuum inequalities prove

\[
P_q^- -\epsilon_q-(C-1)d\ge\eta>0,\qquad
P_q^+ +\epsilon_q\le M,                                     \tag{8.12}
\]

then the uniform conclusion is `H_n''<=-eta*n+(m-1)M` for n>=m, and the entropy-rate
chord coefficient is eta/2. Parameter rectangles crossing a coefficient sign
boundary may first be split along that boundary; no continuity premise is needed.

**Proof.** The field comparisons and corner convexity certify the entire
moving posterior/PSD interface, not just its reference value. Formula (8.2)
identifies the transported vector with the actual law; (8.7)-(8.9) construct its
coefficients with exact normalization. The proof of (8.10), with 8 replaced by
q, gives (8.11), even though the transport is signed. Thus (8.12) pays the true
expectation in (4.14). The proved allocation/conditional-expectation theorem
(4.16) supplies the finite-volume conclusion, and Section 10 supplies the
finite-chord limit. This is an effective continuation theorem: its input margins,
error terms, derivative formulas and acceptance inequalities are all explicit.

## 9. Finite arithmetic and exact continuum payment

### 9.1 Exact inputs and all-word reference probabilities

At rho=1/3 the only transcendental scalar needed in Q is

\[
\alpha_0=\frac{\sqrt3}{2\pi}.
\]

For nonzero integer d,

\[
Q(d)=0\ (3\mid d),\qquad
Q(d)=\begin{cases}+\alpha_0/d&d\bmod6\in\{1,2\},\\
                 -\alpha_0/d&d\bmod6\in\{4,5\}.
       \end{cases}
\]

Also Q(0)=1/3. `alpha60.txt` contains the exact adjacent rational endpoints
reproduced in Appendix B. `exact_closure.py` independently proves both this
60-decimal enclosure and the 19-decimal guard enclosure by Machin's identity
`pi=16 atan(1/5)-4 atan(1/239)`, alternating-series bounds with 120 and 40 terms,
and exact square comparisons `4 alpha_lo^2 pi_hi^2<3<4 alpha_hi^2 pi_lo^2`.
For the stated Machin identity, the tangent addition formula gives
`tan(4 atan(1/5)-atan(1/239))=1`; the angle lies in (0,pi/2), so it equals
pi/4. This supplies the identity used by the rational enclosure, not a numerical
value of pi imported from a library.

For K_*=`I/40+(19/20)Q_22`, define
`L_*=(I-K_*)^{-1}-I`. The identity

\[
\pi_*(S)=\det(I-K_*)\det(L_*)_S                              \tag{9.1}
\]

computes every reference word. The supplied, preserved
`principal_probability_certificate.cpp` recursively visits every principal
minor using inclusion Schur complements and exclusion compressions. Its
`exact_fixed.hpp` arithmetic has scale 2^192, signed checked 256-bit storage,
and checked 512-bit intermediate products. Division endpoints are obtained by
signed floor and ceiling division; an overflow, nonpositive required pivot, or
ambiguous division fails the computation.

All 2^22 words were recomputed in four disjoint prefixes of the first two bits.
The moving-payment verifier also checks uniqueness, positivity, and completeness
of the resulting word records. Its summed enclosing mass was

`[0.9999999999997312296424676, 1.000000000000268880078793]`.

Normalization itself follows analytically from (9.1); the interval check is an
additional consistency check, not a renormalization. The norm bounds in (7.9)
and all coefficient enclosures were then evaluated over these same full words.

### 9.2 Outward arithmetic and branch correctness

`cert_interval.hpp` uses binary `long double` with 64 significand bits, checks
that format at compile time, and encloses elementary arithmetic by an adjacent
`nextafterl` step toward the required infinity. Division rejects intervals
containing zero. Matrix elimination permits only pivots with a definite sign;
setting eliminated entries to exact zero is the corresponding exact algebraic
simplification. Symmetric entry enclosures may be intersected because they
contain the same exact number.

For logarithms, exact power-of-two range reduction puts the argument in [1,2).
The positive series `log z=2 sum_{j>=0} t^{2j+1}/(2j+1)`,
`t=(z-1)/(z+1)`, is summed with an explicit positive geometric remainder.
The guard-only header uses twelve terms and the matching remainder denominator
`25(1-t^2)`; log 2 uses thirty terms and denominator `61(1-t^2)`. The original
header's local logarithm uses twenty-four terms and its matching denominator.
For tiny x, `L(x)<=1+x/2`, since the derivative of
`x+x^2/2-(1+x)log(1+x)` is `x-log(1+x)>=0`.

Square roots are only used for upper enclosures: an initial library square-root
estimate is raised until its *outward lower squared bound* is at least the input.
Thus correctness is checked by multiplication rather than assumed from a
library root approximation. The code is compiled without fast-math, with
`-frounding-math -ffp-contract=off`; unsupported precision is rejected.
The exact fixed-point to long-double conversion compares the binary mantissa
and exponent against the exact scaled integer and moves the endpoint until its
required enclosure relation is true.

The preserved original arithmetic self-test was also rebuilt and passed
138,828 exact comparisons, including signed fixed-point division and endpoint
conversion. A separate new exact-rational audit checked 20,128 interval
arithmetic, root, and logarithm cases across all four hardware rounding modes. This is a falsification
attempt and implementation check; the elementary enclosure arguments above,
not the number of tests, justify the arithmetic interface.

### 9.3 Coefficients and the signed endpoint rule

`quad_payment.cpp` evaluates (7.7)-(7.8), performs the Walsh recursion, and encloses
all 45 coefficients with k+l<=8 for each of V_0,V_P,V_C. It stores outward
integer bounds with denominator 10^9 in
`quad_payment_coefficients_bivariate.txt`, reproduced in Appendix C.

Throughout R, t<0, u>=0, p-1/2<0, and c-c_*>=0. Therefore the sign of each
monomial multiplying a coefficient is known exactly: it is `(-1)^k` for the
V_0 and V_C parts and `(-1)^{k+1}` for the V_P part. Choose the appropriate
lower/upper coefficient endpoint according to that sign, then subtract/add
the declared remainder 10^-6. This constructs explicit rational polynomials
P_-(c,p),P_+(c,p) satisfying

\[
P_-\le P\le P_+\quad\hbox{throughout the closed rectangle}.    \tag{9.2}
\]

The exact-rational verifier uses normalized coordinates
`c=.95+.0035 x`, `p=.42+.06 y`, with x,y in [0,1]. It clears only a known positive
Fisher denominator. Specifically, with b=1-c,

\[
E=b p(1-p)(1-bp)[1-b(1-p)]>0,
\]

\[
N=\tfrac23(1-p)[1-b(1-p)]+\tfrac13p(1-bp),\qquad d=N/E.
                                                                  \tag{9.3}
\]

For eta=1/25 define

\[
G=E(P_- -1/25)-(C-1)N.                                      \tag{9.4}
\]

This is a rational polynomial of bidegree (12,12). The verifier converts it
exactly to tensor Bernstein coefficients on the **whole** unit square. For a
power polynomial `sum a_ij x^i y^j` of bidegree (d,e), those coefficients are

\[
b_{rs}=\sum_{i\le r,j\le s}a_{ij}
 \frac{\binom ri}{\binom di}\frac{\binom sj}{\binom ej}.
\]

The Bernstein basis functions are nonnegative and sum to 1. Hence the minimum
coefficient is a lower bound at every point of the square. No sampled minimum
is involved.

For the final repaired witness, the exact minimum Bernstein coefficient of G
is greater than

\[
\frac{3062919}{10^{12}}>0.                                  \tag{9.5}
\]

The exact minimum coefficient for `21-P_+` is greater than

\[
\frac{142277124911}{10^{12}}>0.                              \tag{9.6}
\]

Each proof succeeds on a single closed rectangle: neither polynomial required
subdivision. The JSON evidence retains the full rational minima, not merely
the decimal summaries. Thus

\[
\boxed{P-(C-1)d\ge1/25,\qquad P\le21\quad\text{on }\mathcal R.} \tag{9.7}
\]

For the nested rectangle c<=953/1000, the same coefficients, caps and PSD
slack give eta=1/5. Its exact minimum Bernstein coefficient of the analogous G
is greater than `667751932/10^12`, again on one whole rectangle; its tail bound
is below `2.286299*10^{-8}`. This proves the payment needed in (1.3).

### 9.4 Guard repairs and complete coverage

Two concrete certificate problems were found and resolved, rather than treated
as continuity assumptions.

First, the initial distance-three allocation left unclosed guard boxes for words
99,100,152. Refining parameter cells alone did not close all of them. The final
witness reduces t3_z by exactly 20 at those three words, that is, increases their
guard caps by .02. All their 126 parameter-word cells then passed. The other 253
word rows were unchanged. The full payment and all 16,384 PSD corners were
**recomputed with the repaired rows**, producing (9.5)-(9.7).

Second, thirteen nearest-neighbor comparison inverses at word 231 exceeded an
optional numerical radius abort threshold 10^-8. The actual computed radius is
always retained in (5.10). Allowing up to 10^-6 and rechecking every one of that
word's 42 parameter cells closed the entire cover, without changing a cap or
a witness coefficient. This is neither a factor-two repair nor omission of an
inverse error.

The initially completed proof cover used the verified unchanged cells together
with these explicit rechecks. It was then superseded by **clean full-cover runs
of the final source with the final inputs**, all of which completed successfully:

| Distance | Closed parameter-word cells | Failed cells | Posterior branch nodes |
|---|---:|---:|---:|
| 1 | 10,752 | 0 | 214,133,692 |
| 2 | 10,752 | 0 | 178,200,492 |
| 3 | 10,752 | 0 | 130,386,592 |

`verify_coverage.py` checks every exact tuple `(c cell,p cell,word)`, its cap
against the exact final integer rows, uniqueness, and the full prescribed
parameter cover. The successful final logs and exact coverage evidence are
included. These final runs do not require accepting any earlier failed cell.
Failed or exploratory runs are kept separately and are not counted as proof
evidence. The exact PSD and both Bernstein closures were also rerun from the
assembled delivery directory, using the delivered inputs, and passed again.

## 10. Passage to entropy rate, with the boundary retained

Every hypothesis of (4.16) has now been checked with

\[
m=22,\quad\eta=1/25,\quad M=21.
\]

There are exactly n-21 wholly contained translated windows. Therefore

\[
H_n''\le n[(C-1)d-P]+21P\le-n/25+441,
\]

proving (1.1). The same argument with eta=1/5 proves (1.3).

For fixed c and n, a twice differentiable function with second derivative at
most `-k_n` satisfies the finite chord bound

\[
\operatorname{Gap}_\lambda H_n
\ge\frac{k_n}{2}\lambda(1-\lambda)(a_1-a_0)^2,
\quad k_n=\eta n-441.
\]

For example, add `(k_n/2)a^2` to H_n and apply concavity to obtain this inequality;
it is valid even when k_n is negative. Stationarity and the entropy chain rule
give `H_{n+m}<=H_n+H_m`, and `0<=H_n<=n log2`; consequently H_n/n has its usual
finite limit h by the elementary subadditive argument: writing n=qm+r for
fixed m gives `H_n<=q H_m+H_r`, so `limsup H_n/n<=H_m/m` for every m,
whereas `liminf H_n/n>=inf_m H_m/m`. Divide the finite chord
bound by n and pass to the three entropy-value limits at a_0,a_1 and their
convex combination. The term 441/n vanishes, giving (1.2) and its nested analogue.

No second derivative of h is assumed to exist, and no o(n) value error is ever
differentiated. Boundary and all nonlocal interactions were already paid before
taking this limit.

## 11. Falsification attempts and the remaining full-target obstruction

The following attempts were useful checks, not theorem premises based on floating
experiments.

* The original pair-only allocation loses its apparent payment quickly as c
  rises; using its old global cap without rechecking contrast is invalid.
  This motivated sharing diagonal Fisher across a larger PSD block.
* A preliminary three-target construction unnecessarily removed other target
  bits from every guard. Section 4.2 proves the sharper endpoint-only exclusion
  rule and permits the information-preserving four-target construction.
* Coarse distance-three guard boxes failed; finer cells did not universally fix
  them. The three explicit cap repairs described above were then paid under the
  full moving law, not declared harmless because their words were rare.
* The nearest inverse aborts were retained, diagnosed as numerical enclosure
  width rather than a false Loewner formula, and explicitly rechecked with the
  true row-sum error radius.
* `exact_small_tests.py` independently checks 345 exact identities for a genuine
  finite compression of a rational projection (not itself a projection). It
  checks signed tensor transport, Walsh coefficients and normalization, the
  finite score formula, integration by parts, pair weights depending on a third
  bit, and the conditional-score martingale. Its exact input matrix and scope
  are recorded. These are tests of the reusable tool, not a substitute for the
  sine-law continuum certificate.
* `exact_block_test.py` additionally checks the **combined** allocation,
  conditional Jensen, and variational completion on two overlapping three-target
  windows. Each off-diagonal entry explicitly depends on the third target bit.
  Exact nonnegative residuals and equality to conditional-variance and
  completion-of-square terms are verified at three moving-law parameter pairs,
  along with the literal versus factored potential. This tests the relaxed
  block interface itself, not only its component identities.
* `direct_payment_check.cpp` evaluates all 2^22 words by **direct** tensor-channel
  transport at two exact rational parameter pairs, without Walsh aggregation or
  a polynomial tail. It uses the same independently reconstructed reference
  probabilities and fixed-potential construction, so this is a distinct check
  of transport/evaluation, not a wholly independent implementation of every
  preceding component. At (c,p)=(1907/2000,21/50), its outward payment-excess
  enclosure is contained in
  `[0.0402893383954,0.0402893384014]`, confirming the narrow positive margin.
  At (c,p)=(24/25,9/20), it is contained in
  `[-3.277834391895,-3.277834391888]`, confirming the obstruction's sign without
  truncation. Both have enclosing total masses containing 1; no renormalization
  is performed. These point checks do not substitute for the continuum proof.
* The same exact channel test proves `F^2=F!=0` and exhibits negative off-diagonal entries
  of the contrast-increasing T. Thus treating contrast as a-only nilpotence or
  as a stochastic post-processing kernel would be false.

Finally, `exact_obstruction.py` evaluates the final coefficient intervals at
`c=24/25`, `p=9/20`, so `a=9/500=.018`, `t=-2/5`, `u=10`. The whole-vector tail
bound is recomputed **at that point**, not reused from R. It is less than
`2.567247*10^{-7}`. Exact rational arithmetic gives enclosing payments within

\[
23.2006125845<P(.96,.45)<23.3232982830,
\]

and enclosing payment excess within

\[
-3.2838040289< P-(C-1)d < -3.1611183303.
\]

The exact rational endpoints, including coefficient-enclosure uncertainty, are
in `evidence/fixed_witness_obstruction.json`. In particular the clean exact
inequality (1.4) follows. This point is legal and is inside the full ambitious
target. It rules out closing that full target using these same witness formulas
and this same C, even before asking whether their other hypotheses extend there.

**Smallest remaining load-bearing task for the full rectangle:** construct an
admissible replacement cap/allocation/test (or an additional payable witness)
whose actual-law payment satisfies

\[
\inf_{c\in[.9535,.96],\ p\in[.42,.48]}
\{\widetilde P(c,p)-[\widetilde C(c,p)-1]d((1-c)p,c)\}>0,        \tag{11.1}
\]

with its corresponding pair-cap and PSD-budget conditions. Merely refining the
payment computation for the present formulas cannot prove (11.1), because of
(1.4). Nothing here disproves entropy-rate concavity on that remaining region.

## 12. Dependency and scope ledger

| Item | Status and exact use |
|---|---|
| Frozen sine-DPP object and task scope | Taken from the current S70 packet. All parameter claims here use rho=1/3. |
| Accepted S63 theorem | Used as the accepted comparison baseline, not as a hypothesis that an unquantified contrast neighborhood exists. Its old boundary 399 is not silently carried over. |
| Supplied S63 integer guard rows, alpha bracket, probability/interval source | Preserved separately under `original/`. Used as explicit data or finite algorithms; new cap, probability, PSD, and payment obligations are checked here. |
| Latent channel, posterior inverse, scalar cap, score/variational mechanism | Proved explicitly above, with the new endpoint-only block allocation and two-parameter robustness included. |
| New four-target PSD matrices | Exact 16,384 corner checks, giving uniform slack I/200. |
| New contrast-dependent global and guard caps | Outward interval bounds over complete parameter and posterior boxes. No pointwise grid theorem. |
| Moving-law payment | All 2^22 words, exact signed two-parameter transport, outward coefficient boxes, explicit whole-vector tail, exact tensor Bernstein closure. |
| Fisher and boundary | Exact complete-data upper budget; n-21 windows; boundary 441. |
| Entropy rate | Finite chord inequalities followed by entropy-value limits only. |
| S64 acceleration, S55 cyclic bridge, S68 stronger appendix claims | Not used. No claim from those lanes is imported. |
| Finite compression versus projection | Only the infinite Fourier operator Q is used as a projection; every Q_E and Q_22 is a true compression. |
| Outside results | No inaccessible outside result is a premise. Elementary linear algebra, determinant identities, finite probability differentiation, and convergent series are proved or explicitly derived. |
| External novelty | Not certified or claimed. The general tools are reusable irrespective of external priority. |
| Full rectangle through .96 | Incomplete; the present fixed-witness payment obstruction is proved, not an entropy counterexample. |
| Repository mutations and shared status | None. Results are delivered as readable local files and reproducible sources, not as a merged PR or changed shared status. |

## 13. Reproduction and acceptance conditions

Read `README.md` and execute `run_all.sh` in the supplied source package on a
platform with the explicitly checked binary long-double format. The script
rebuilds the actual reference probabilities; verifies all global and guard
cells; computes the full moving-law coefficients; checks the exact PSD,
Bernstein and tail statements; and runs the independent arithmetic/tool tests
and the fixed-witness obstruction check.

Exact inputs are the parameter fractions in this manuscript and the plain-text
integer tables reproduced below. There is no SHA, checksum, hash, ZIP, manifest,
or successful-log-message acceptance gate. Required mathematical conditions are
positive exact pivots, outward containment, complete cell/word coverage, and
positive Bernstein coefficients. An unfinished, failed, missing, or ambiguous
certificate step is not accepted. The sources explain what each successful step
proves and why it proves a continuum statement.

The local probability caches are reproducible intermediate data, not proprietary
inputs. They need not be shipped: the exact source reconstructs all four chunks.
The proof remains readable independently of the archive.

---

## Appendix A. Complete witness integer data

Each row is `z L_z U_z t2_z t3_z`, with guard-word order defined in (6.4).
The first two columns after z are the preserved source inputs; the last two are
the final new allocations, including the three paid repairs.

```text
0 8756 8341 373 350
1 9496 9213 375 350
2 9998 9871 377 350
3 10021 9769 377 350
4 10489 10278 320 335
5 10362 10502 270 279
6 10131 10351 281 289
7 9743 10175 269 268
8 10330 10813 157 135
9 10052 10486 151 92
10 9881 10192 160 83
11 9139 9652 174 81
12 9350 10062 159 102
13 9048 9992 155 89
14 9389 10062 161 91
15 9076 9648 187 101
16 10330 10813 373 203
17 10313 10805 375 161
18 10151 10340 377 156
19 9834 9906 377 188
20 10151 10151 320 156
21 9890 9925 270 173
22 9506 9582 281 162
23 9444 9521 269 188
24 10069 10077 157 117
25 9848 9874 151 118
26 9657 9697 160 146
27 9567 9611 174 253
28 9641 9683 159 208
29 9737 9771 155 278
30 9681 9718 161 271
31 9620 9660 187 278
32 10489 10278 142 138
33 10712 10750 136 138
34 10529 10885 135 145
35 10092 10124 261 286
36 10151 10151 257 279
37 10112 10123 374 350
38 9709 9812 377 350
39 9416 9557 377 350
40 10151 10151 377 350
41 10043 10058 377 350
42 9710 9764 377 350
43 9316 9403 377 350
44 9436 9526 377 350
45 9585 9653 377 350
46 9596 9662 377 350
47 9383 9463 377 350
48 9350 10062 142 350
49 9413 9897 136 350
50 9389 9547 135 350
51 8593 8822 261 350
52 9436 9526 257 350
53 9124 9228 374 350
54 8912 9035 377 350
55 9015 9123 377 350
56 9641 9683 377 350
57 9579 9623 377 350
58 9498 9547 377 350
59 9506 9553 377 350
60 9495 9546 377 350
61 9590 9632 377 350
62 9531 9577 377 350
63 9548 9591 377 350
64 9998 9871 304 81
65 10330 10148 267 86
66 10691 10489 228 77
67 10323 10411 258 113
68 10529 10885 246 120
69 10151 10340 286 197
70 9953 10045 318 298
71 9543 9756 351 350
72 10151 10340 257 339
73 10142 10145 311 350
74 9907 9957 346 350
75 9242 9386 377 350
76 9389 9547 339 350
77 9426 9563 344 350
78 9581 9690 349 350
79 9257 9400 377 350
80 9881 10192 304 350
81 9991 10052 267 350
82 9907 9957 228 350
83 8927 9089 258 350
84 9710 9764 246 350
85 9168 9260 286 350
86 8974 9081 318 350
87 9049 9147 351 350
88 9657 9697 257 350
89 9522 9568 311 350
90 9458 9508 346 350
91 9476 9524 377 350
92 9498 9547 339 350
93 9545 9589 344 350
94 9481 9529 349 350
95 9502 9548 377 350
96 10131 10351 158 117
97 10085 10437 156 119
98 9953 10045 182 149
99 8608 8992 347 326
100 9709 9812 341 317
101 8766 8971 377 350
102 8203 8468 377 350
103 8293 8532 377 350
104 9506 9582 377 350
105 9186 9278 377 350
106 8974 9081 377 350
107 8941 9047 377 350
108 8912 9035 377 350
109 9108 9206 377 350
110 9006 9110 377 350
111 8985 9086 377 350
112 9389 10062 158 350
113 9523 9896 156 350
114 9581 9690 182 350
115 8856 9029 347 350
116 9596 9662 341 350
117 9200 9289 377 350
118 9006 9110 377 350
119 9085 9179 377 350
120 9681 9718 377 350
121 9557 9600 377 350
122 9481 9529 377 350
123 9494 9541 377 350
124 9531 9577 377 350
125 9584 9625 377 350
126 9512 9558 377 350
127 9531 9574 377 350
128 9496 9213 377 303
129 10023 9930 377 294
130 10330 10148 366 277
131 10330 10130 355 270
132 10712 10750 258 265
133 10366 10687 233 244
134 10085 10437 254 262
135 9682 10118 258 255
136 10313 10805 145 139
137 10143 10424 166 135
138 9991 10052 188 148
139 9224 9365 218 170
140 9413 9897 184 151
141 9251 9825 181 145
142 9523 9896 188 148
143 9173 9353 230 181
144 10052 10486 377 287
145 10143 10424 377 297
146 10142 10145 366 332
147 9377 9498 355 350
148 10043 10058 258 350
149 9468 9537 233 350
150 9186 9278 254 350
151 9230 9315 258 350
152 9848 9874 145 317
153 9622 9662 166 337
154 9522 9568 188 344
155 9521 9566 218 350
156 9579 9623 184 350
157 9632 9671 181 350
158 9557 9600 188 350
159 9555 9597 230 350
160 10362 10502 162 156
161 10366 10687 160 157
162 10151 10340 188 196
163 9446 9658 361 350
164 10112 10123 345 350
165 9417 9541 377 350
166 8766 8971 377 350
167 8733 8927 377 350
168 9890 9925 377 350
169 9468 9537 377 350
170 9168 9260 377 350
171 9060 9156 377 350
172 9124 9228 377 350
173 9304 9387 377 350
174 9200 9289 377 350
175 9117 9208 377 350
176 9048 9992 162 350
177 9251 9825 160 350
178 9426 9563 188 350
179 8863 9043 361 350
180 9585 9653 345 350
181 9304 9387 377 350
182 9108 9206 377 350
183 9184 9272 377 350
184 9737 9771 377 350
185 9632 9671 377 350
186 9545 9589 377 350
187 9546 9589 377 350
188 9590 9632 377 350
189 9654 9690 377 350
190 9584 9625 377 350
191 9591 9630 377 350
192 10021 9769 290 82
193 10330 10130 265 87
194 10323 10411 246 80
195 9683 9936 330 139
196 10092 10124 318 146
197 9446 9658 377 257
198 8608 8992 377 350
199 8353 8742 377 350
200 9834 9906 377 350
201 9377 9498 377 350
202 8927 9089 377 350
203 8583 8769 377 350
204 8593 8822 377 350
205 8863 9043 377 350
206 8856 9029 377 350
207 8616 8799 377 350
208 9139 9652 290 350
209 9224 9365 265 350
210 9242 9386 246 350
211 8583 8769 330 350
212 9316 9403 318 350
213 9060 9156 377 350
214 8941 9047 377 350
215 9021 9119 377 350
216 9567 9611 377 350
217 9521 9566 377 350
218 9476 9524 377 350
219 9498 9545 377 350
220 9506 9553 377 350
221 9546 9589 377 350
222 9494 9541 377 350
223 9523 9567 377 350
224 9743 10175 163 207
225 9682 10118 161 210
226 9543 9756 187 235
227 8353 8742 362 350
228 9416 9557 348 350
229 8733 8927 377 350
230 8293 8532 377 350
231 8403 8618 377 350
232 9444 9521 377 350
233 9230 9315 377 350
234 9049 9147 377 350
235 9021 9119 377 350
236 9015 9123 377 350
237 9184 9272 377 350
238 9085 9179 377 350
239 9069 9162 377 350
240 9076 9648 163 350
241 9173 9353 161 350
242 9257 9400 187 350
243 8616 8799 362 350
244 9383 9463 348 350
245 9117 9208 377 350
246 8985 9086 377 350
247 9069 9162 377 350
248 9620 9660 377 350
249 9555 9597 377 350
250 9502 9548 377 350
251 9523 9567 377 350
252 9548 9591 377 350
253 9591 9630 377 350
254 9531 9574 377 350
255 9561 9601 377 350
```

## Appendix B. Exact sine scalar input

The three lines are lower numerator, upper numerator, and common denominator.

```text
275664447710896024755663249156484720698693240183320326399683
275664447710896024755663249156484720698693240183320326399684
1000000000000000000000000000000000000000000000000000000000000
```

## Appendix C. Complete degree-eight payment coefficient boxes

For each row `k l V0_lo V0_hi VP_lo VP_hi VC_lo VC_hi`, all six endpoints
have common denominator 1,000,000,000. Variables and signs are specified in
Sections 8.2 and 9.3. These are enclosures, not rounded exact equalities.

```text
# k l V0lo V0hi VPlo VPhi VClo VChi; denominator 1000000000
0 0 18991269468 18991269469 4193529404 4193529405 144830791329 144830791331
0 1 233483335 233483336 54458566 54458567 1903577245 1903577246
0 2 -78049 -78048 -484 -483 74588 74589
0 3 79 80 27 28 1553 1554
0 4 0 1 0 1 4 5
0 5 0 1 0 1 0 1
0 6 0 1 0 1 0 1
0 7 0 1 0 1 0 1
0 8 0 1 0 1 0 1
1 0 -1302629620 -1302629619 -281344594 -281344593 -10194661569 -10194661568
1 1 10661065 10661066 1929092 1929093 74195831 74195832
1 2 2637 2638 738 739 27476 27477
1 3 1 2 1 2 16 17
1 4 -1 0 0 1 -1 0
1 5 -1 0 -1 0 -1 0
1 6 -1 0 -1 0 -1 0
1 7 -1 0 -1 0 -1 0
2 0 -143516046 -143516045 -31169824 -31169823 -1082812831 -1082812830
2 1 -33918 -33917 -19414 -19413 -769782 -769781
2 2 -85 -84 -41 -40 -1476 -1475
2 3 -1 0 -1 0 -3 -2
2 4 -1 0 -1 0 -1 0
2 5 -1 0 -1 0 -1 0
2 6 -1 0 -1 0 -1 0
3 0 -8362 -8361 101101 101102 2254501 2254502
3 1 -141 -140 106 107 3126 3127
3 2 0 1 0 1 13 14
3 3 0 1 0 1 0 1
3 4 0 1 0 1 0 1
3 5 0 1 0 1 0 1
4 0 4092 4093 830 831 53140 53141
4 1 11 12 4 5 157 158
4 2 0 1 0 1 0 1
4 3 0 1 0 1 0 1
4 4 0 1 0 1 0 1
5 0 -39 -38 -20 -19 -788 -787
5 1 -1 0 -1 0 -3 -2
5 2 -1 0 -1 0 -1 0
5 3 -1 0 -1 0 -1 0
6 0 -1 0 -1 0 0 1
6 1 -1 0 -1 0 0 1
6 2 0 1 0 1 0 1
7 0 0 1 0 1 0 1
7 1 0 1 0 1 0 1
8 0 -1 0 -1 0 -1 0
```
