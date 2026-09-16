PROVED_SCOPED_LEMMA

# S8 round two: a projection-compatible four-cycle curvature comparison

**Author analytic proof; not independently reviewed or formally verified.**
The result below extends the *mechanism* of the reviewed S2 singleton theorem
to a genuinely coupled rank-two family in every ambient dimension. It does
**not** prove general projection concavity or the high-contrast sine entropy-rate
target. No novelty or priority claim is made.

The new step is a positive **two-dimensional complex Gaussian representation
of the interpolation Fisher information**, after an exact four-cycle
cancellation. It is not another circle-to-Toeplitz bridge, the old Johnson
exchange identity, or the false unrestricted homogeneous-law smoothing claim.
Two proposed overextensions are refuted by exact projection examples in
[OBSTRUCTIONS.md](OBSTRUCTIONS.md).

Source baseline: reviewed main `6242dc3206ff196dc15b9dbfb0e41971844cecdc`.
The existing branch incorporated that baseline in merge
`f265c68d798f9d7e6ad2f01ef57fa0745b768e2a`, retaining the updated assignment
and reviewed S8/S9 repairs. Exact dependency distinctions are in
[DEPENDENCY_DELTA.md](DEPENDENCY_DELTA.md). All logarithms are natural.

## 1. Explicit deformation and theorem

Let `n>=4`, let `U` be a **real** `n x 2` isometry, and put

\[
 P=UU^*,\qquad h_r=P_{rr},\qquad
 \mu_{rs}=|\det U_{\{r,s\}}|^2\quad(r\ne s).
\]

These are the complete input atom probabilities of a rank-two projection DPP.
They are not independent free pair weights. Fix four distinct coordinates
`i,j,k,l` and suppose

\[
 h_i=h_j,\qquad
 \mu_{jr}-\mu_{ir}=
 \begin{cases}
 \eta,&r=k,\\
 -\eta,&r=l,\\
 0,&r\notin\{i,j,k,l\}.
 \end{cases}                                      \tag{1}
\]

The case `eta=0` is allowed and gives a zero gain. Write `O` for the complement
of these four coordinates and

\[
 \beta=\left\|\sum_{r\in O}u_r^*u_r\right\|_{\rm op}\le1,
                                                        \tag{2}
\]

where `u_r` is the row of `U`; the empty sum is zero.

Let `S` interchange coordinates `i,j`. On those two coordinates define

\[
 R_s=\sqrt{1-s}\,I_2+i\sqrt{s}\,
          \begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad0\le s\le1,                                   \tag{3}
\]

and extend by the identity elsewhere. Set `U_s=R_s U`, `P_s=U_sU_s^*`.
Here the italic `i` in front of the square root is the imaginary unit.
The deformation is physical, generally changes measured entropy, and stays
inside complex Hermitian rank-two projection DPPs at **every** `s`.

For a fixed `0<c<1`, use the independent channel
`Pr(Y_r=1|X_r)=a+c X_r`, `0<=a<=1-c`, and denote its complete configuration
entropy for input `P_s` by `H_s(a)`. Define

\[
 D_t(a)=H_t(a)-(1-t)H_0(a)-tH_1(a),\qquad 0\le t\le1.
                                                        \tag{4}
\]

**Theorem 1 (four-cycle comparison).** If `c>=beta/4`, then `D_t` is convex
on the closed legal `a` interval. In its interior,

\[
 \boxed{
 D_t''(a)\ge
 2c^3(4c-\beta)\eta^2t(1-t)\ge0.
 }                                                       \tag{5}
\]

The endpoints `P_1` and `P_0` have coordinate-permuted laws, so `H_1=H_0`.
Consequently this is the explicit curvature comparison

\[
 H_t''(a)-H_0''(a)\ge2c^3(4c-\beta)\eta^2t(1-t).
                                                        \tag{6}
\]

It holds for all `c>=1/4` without an extra spectral assumption; when `n=4`
it holds for every `c>0`. The constant in (5) is independent of `n` once
`c,beta,eta,t` are fixed. Neither (5) nor (6) asserts `H_t''<=0`.

## 2. Projection compatibility is preserved, not assumed

The matrix in (3) is unitary and has determinant one. Thus `U_s^*U_s=I_2`.
A minor containing both distinguished rows is unchanged, as is a minor
containing neither. A minor containing just row `i` has the form

\[
 \sqrt{1-s}\,\det U_{\{i,r\}}
     +i\sqrt{s}\,\det U_{\{j,r\}}.
\]

Both original determinants are real. Its squared modulus is therefore
`(1-s)mu_ir+s mu_jr`; the analogous formula holds for row `j`.
For every complete input atom this proves exactly

\[
 \boxed{\mu_s=(1-s)\mu_0+s S_*\mu_0.}                    \tag{7}
\]

No assertion that arbitrary mixtures of projection laws are projections is
being made. Equation (3) is an explicit isometric realization of this
particular chord. It also proves all Pluecker identities simultaneously:
the minors come from the same two columns throughout.

The equality of the two original row norms implies that every `h_r` is
constant along this path. The outside rows are fixed, so (2) is fixed.
The endpoint `s=1` differs from a coordinate swap only by diagonal phases;
these phases cancel from the squared minors. This proves `H_1=H_0`.

## 3. Complete output atoms and all interpolation derivatives

Put `delta=1-c`, `x=a(delta-a)>0`. For any output set `T`, define

\[
 M_T^s=\sum_{r\in T}(u_r^s)^*u_r^s,\quad
 h_T=\operatorname{Tr}M_T^s,\quad
 m_T^s=\det M_T^s=\sum_{\{r,v\}\subset T}\mu^s_{rv}.
\]

The complete output atom is

\[
 \boxed{
 q_s(T)=a^{|T|-2}(1-a)^{n-|T|-2}
       \det(xI_2+cM_T^s)
 =a^{|T|-2}(1-a)^{n-|T|-2}
       (x^2+cxh_T+c^2m_T^s).
 }                                                       \tag{8}
\]

To verify it without changing the entropy object, sum the channel likelihood
over all input pairs. Relative to the all-`Ber(a)` product law, each occupied
input coordinate contributes `(a+c)/a` inside `T` and
`(1-a-c)/(1-a)` outside. Cauchy--Binet turns this weighted sum of squared
minors into

\[
 \det\left(\frac{1-a-c}{1-a}I_2+
             \frac{c}{a(1-a)}M_T^s\right).
\]

Multiplication by `a^{|T|}(1-a)^{n-|T|}` gives (8). This is the probability
of the **entire** output word, including every vacancy. Negative exponents
in the prefactor are harmless in the strict interior; the product formula
before division supplies endpoint continuity.

From (1) and (7),

\[
 m_T^1-m_T^0=\eta(1_{i\in T}-1_{j\in T})
                     (1_{k\in T}-1_{l\in T}).             \tag{9}
\]

In particular `q_s` is affine in `s`. Write `v_T=partial_s q_s(T)` and

\[
 I_s(a)=\sum_T\frac{v_T(a)^2}{q_s(T)}.
\]

Then finite differentiation of the **full** entropy gives

\[
 -\partial_s^2 H_s(a)=I_s(a).                             \tag{10}
\]

This is differentiation in `s`, not in `a`, and no `a`-acceleration term
has been discarded. The final `a` curvature is obtained by differentiating
an exact finite-law entropy difference.

Only outputs selecting exactly one site from each pair in (9) contribute.
Writing them as `A union R`, with
`A in { {i,k},{i,l},{j,k},{j,l} }` and `R subset O`, cancels both powers of
`a(1-a)` and yields

\[
 \boxed{
 I_s(a)=c^4\eta^2\sum_A\sum_{R\subset O}
 \frac{a^{|R|}(1-a)^{|O|-|R|}}
      {\det(xI_2+cM_{A\cup R}^s)}.
 }                                                       \tag{11}
\]

That cancellation is the specific four-cycle feature missing from a generic
higher-rank or unrestricted homogeneous smoothing assertion.

## 4. The new positive Gaussian representation

For a positive Hermitian `2 x 2` matrix `A`,

\[
 \det(A)^{-1}=\int_{\mathbb C^2}e^{-z^*Az}\frac{d^4z}{\pi^2}.
                                                        \tag{12}
\]

Indeed, diagonalize `A` only in this auxiliary integral, use the real
Jacobian one of a unitary transformation, and apply
`integral_C exp(-lambda |z|^2) d^2z/pi=1/lambda`, proved in polar coordinates.
This is not an entropy invariance under a change of physical measurement basis.

Write `R=||z||^2` and `E_r=|u_r^s z|^2`. The common isometry gives
`sum_r E_r=R`. Substitution of (12) into (11) and finite summation give

\[
 \boxed{
 I_s(a)=c^4\eta^2\int_{\mathbb C^2}C_s(z)G_s(a,z)
                       \frac{d^4z}{\pi^2},
 }                                                       \tag{13}
\]

where

\[
 C_s=(e^{-cE_i}+e^{-cE_j})(e^{-cE_k}+e^{-cE_l}),
\quad
 G_s=e^{-xR}\prod_{r\in O}(1-a+ae^{-cE_r}).               \tag{14}
\]

The weight `C_s` is positive and independent of `a`. Unlike the S2 scalar
formula, this representation retains a genuine two-dimensional row geometry
and its common Gram identity. It is valid also when some input minors vanish.

Set `r_v=1-e^{-cE_v}`. Direct logarithmic differentiation gives

\[
 (\log G_s)''=2R-\sum_{v\in O}\frac{r_v^2}{(1-ar_v)^2}.
                                                        \tag{15}
\]

For `u>=0`, Cauchy--Schwarz in the elementary integral gives the sharper
bound

\[
 (1-e^{-u})^2=\left(\int_0^u e^{-v}dv\right)^2
 \le u\int_0^u e^{-2v}dv
 =\frac u2(1-e^{-2u})\le\frac u2.                       \tag{15a}
\]

Also `1-ar_v>=1-a>=c`. The operator inequality in (2), applied to this
**same** vector `z`, gives

\[
 \sum_{v\in O}\frac{r_v^2}{(1-ar_v)^2}
 \le\frac1{2c}\sum_{v\in O}E_v\le\frac\beta{2c} R.
\]

Therefore

\[
 (\log G_s)''\ge(2-\beta/(2c))R,
 \qquad G_s''\ge(2-\beta/(2c))R G_s\ge0                     \tag{16}
\]

when `c>=beta/4`. Positive integration proves convexity of `I_s`.
This can be done with the defining convexity inequality and hence does not
require an exchange of improper derivatives.

For the quantitative statement, each of the four terms in `C_s` is at least
`e^{-cR}`. Jensen's inequality for the exponential gives
`1-a+ae^{-cE_v}>=e^{-acE_v}`. Thus

\[
 C_sG_s\ge4e^{-(c+x+ac)R}\ge4e^{-R},                    \tag{17}
\]

because `c+x+ac=c+a-a^2<=1` on the legal interval. The elementary Gaussian
moment is `integral R e^{-R} d^4z/pi^2=2`. Equations (13), (16), and (17)
now give

\[
 I_s''(a)\ge8c^4(2-\beta/(2c))\eta^2.                      \tag{18}
\]

For completeness, differentiating (13) here is justified on every compact
interior `a` interval: `x` has a positive lower bound, the affine factors
are bounded below by a positive constant, and both derivatives are bounded
by a fixed polynomial in `R` times `e^{-epsilon R}`. There are finitely many
rows for each `n`, and `s` ranges over a compact set of isometries. Such bounds
are integrable in four real dimensions. Dimension-independent domination is
not required for this finite identity; the resulting bound (18) itself is
independent of dimension.

## 5. Green identity: exact complete-entropy curvature difference

For `0<=s,t<=1`, let

\[
 g_t(s)=\min(s,t)(1-\max(s,t)).
\]

The one-dimensional Dirichlet Green identity applied to (10) is

\[
 \boxed{D_t(a)=\int_0^1 g_t(s)I_s(a)\,ds.}              \tag{19}
\]

Both sides vanish at `t=0,1` and have the same second derivative in `t`;
this proves the formula directly. In particular, if

\[
 \mathscr C(q)=-\sum_T q_T''\log q_T
                     -\sum_T(q_T')^2/q_T,
\]

with primes denoting `a` derivatives, the exact curvature difference is

\[
 D_t''=\mathscr C(q_t)-(1-t)\mathscr C(q_0)-t\mathscr C(q_1)
       =\int_0^1 g_t(s) I_s''(a)\,ds.                 \tag{19a}
\]

Both the probability acceleration and the full Fisher term are retained in
this equality; the interpolation Fisher information in (10) is a different
quantity, not a replacement for either term. In particular no unknown remainder has
been introduced. The kernel is nonnegative and
`integral_0^1 g_t(s)ds=t(1-t)/2`. Integrate (18) in (19) to obtain (5).
Alternatively integrate strong convexity inequalities to avoid derivative
interchanges entirely. This completes the theorem.

All finite output atoms are continuous at `a=0,1-c` and `0 log 0=0` is
continuous, so `D_t` and its convexity inequality extend to the closed interval.
No endpoint second derivative or differentiability of an entropy rate is claimed.

## 6. A connected family in arbitrarily large dimension

For every integer `p>=1`, take `n=p+4` and rows

\[
 u_1=(1/2,1/4),\quad u_2=(1/2,-1/4),\quad
 u_3=(1/2,1/2),\quad u_4=(1/2,-1/2),
\]
\[
 u_{4+r}=(0,\sqrt{3/(8p)}),\qquad1\le r\le p.             \tag{20}
\]

The two column norms are one and their inner product is zero. The first pair
has `h_1=h_2=5/16`, and its minor differences are

\[
 \mu_{23}-\mu_{13}=1/8,\quad
 \mu_{24}-\mu_{14}=-1/8,\quad
 \mu_{2r}-\mu_{1r}=0\quad(r>4).
\]

The outside row-energy matrix is `diag(0,3/8)`. Hence `eta=1/8`, `beta=3/8`,
and (5) gives, for **every** `p>=1` and `c>=3/32`,

\[
 \boxed{H_t''-H_0''\ge
 \frac{c^3(4c-3/8)}{32}\,t(1-t).}                         \tag{21}
\]

For `p=1` every one of the ten input pair atoms is positive. For larger `p`,
the extra rows are parallel, but they are not independent coordinate blocks:
each extra row has nonzero covariance with all four displayed rows. The
covariance support graph is connected; across a nonzero edge,
`Cov(X_r,X_v)=-|P_rv|^2` excludes independence. Thus this is not a rank-one direct-sum
repackaging; its two columns share the first four coordinates and the channel
law is not a product over a nontrivial coordinate partition.

The rank remains two as `p` grows, so the density tends to zero. This family
does **not** approximate the fixed-positive-density sine process.

There is a precisely limited positive-density corollary: take coordinate
direct sums of `m` copies of the five-site example. Rank is `2m`, dimension
`5m`, and density is `2/5`. Apply (3) separately within each block, with the
same `t`. Channel independence and entropy additivity give `m` times (21),
an extensive curvature comparison. The intermediate law is a product of
local mixtures, **not** the mixture of two whole-system endpoint laws.
The blocks remain independent, so this corollary still supplies no sine limit
or total entropy sign.

### 6.1 The actual five-site consecutive Fourier projection

The mechanism also applies to a genuine circular sine approximant, not only
to the rational family (20). Let `Pi_{5,2}` project onto Fourier modes `0,1`.
A diagonal coordinate phase gauge followed by a change of the two-column
frame (which leaves the projection itself unchanged) gives the real isometry

\[
 u_r=\sqrt{2/5}\,(\cos(\pi r/5),\sin(\pi r/5)),
 \qquad r=0,1,2,3,4.
\]

The geometric sum of fifth roots of unity proves column orthonormality.
Its compatible pair atoms are

\[
 \mu_{rv}=\frac4{25}\sin^2\!\frac{\pi(r-v)}5,
 \qquad h_r=2/5.
\]

For the swap `i=0,j=1`, the three outside differences, ordered `r=2,3,4`,
are `(-sqrt(5)/25,0,sqrt(5)/25)`. For an elementary exact evaluation,
`1+2 cos(theta)+2 cos(2theta)=0` at `theta=2pi/5` gives
`cos(theta)=(sqrt(5)-1)/4` and `sin^2(pi/5)=(5-sqrt(5))/8`.
Thus the four-cycle condition holds with
`eta^2=1/125`; the one remaining outside row has operator budget `beta=2/5`.
Theorem 1 proves throughout the legal interval, for every `c>=1/10`,

\[
 H_t''-H_0''\ge\frac{8c^3}{125}(c-1/10)t(1-t).           \tag{22}
\]

Cyclic shifts give the same statement for every adjacent swap of the original
Fourier projection. Complementing both input and output transfers this
comparison to its co-rank-two counterpart, using `a -> 1-c-a`.
The phase gauge is harmless because it cancels in every squared minor;
no arbitrary physical basis change is asserted to preserve entropy.

This is a finite Fourier **comparison**, not absolute entropy concavity and
not a fixed-density sequence. Already for `Pi_{6,2}` and the same adjacent
swap the outside difference vector is `(-2,-1,1,2)/36`; its four nonzero
entries require the signed payment not supplied here. There is also no proof
that repeated allowed swaps preserve the real-frame/four-cycle assumptions.

### 6.2 A larger fixed-diagonal four-site comparison (intermediate laws justified)

There is also a useful finite-dimensional extension beyond a real starting
frame. Let `P^0,P^1` be **arbitrary complex rank-two projections on four sites**
with identical diagonals `h_i`. Mix their input laws linearly,
`mu_s=(1-s)mu_0+s mu_1`, and apply the channel. This is always a valid
homogeneous input law. We do **not** assume that this general mixture remains
a projection DPP. Write `delta_ij=mu^1_ij-mu^0_ij`.

The complete output atoms of sizes zero, one, three, and four are unchanged:
for a triple with missing site `r`, its input pair mass is `1-h_r`.
Only the six size-two outputs vary. Their probabilities are exactly

\[
 q_s(\{i,j\})=x^2+cx(h_i+h_j)+c^2\mu^s_{ij}.            \tag{23}
\]

This formula remains valid for the intermediate homogeneous laws by expanding
the two occupied input likelihood factors; it does not require an assumed
intermediate determinant kernel. Projection endpoint constraints and convex
mixing give

\[
 \max(0,h_i+h_j-1)\le\mu^s_{ij}\le h_i h_j.
\]

Consequently (23) factors as `(x+c lambda_1)(x+c lambda_2)` with
`0<=lambda_1,lambda_2<=1`: the discriminant is nonnegative, the sum is
`h_i+h_j`, and the product and the product of the complementary roots are
nonnegative. Each reciprocal factor is log-convex in `a`, because `x''=-2`.
More quantitatively,

\[
 (\log(1/q_s))''
 =\sum_{v=1}^2\left[\frac2{x+c\lambda_v}
              +\frac{(x')^2}{(x+c\lambda_v)^2}\right]\ge4,
\]

using `x+c<=1`. Also `1/q_s>=1`, since it is a probability reciprocal.
Thus `(1/q_s)''>=4` for every legal interior `a` and every `0<c<1`.
The interpolation Fisher information is exactly
`I_s=c^4 sum_{i<j} delta_ij^2/q_s({i,j})`. The same Green identity now proves

\[
 \boxed{
 [H_t-(1-t)H_0-tH_1]''
 \ge2c^4t(1-t)\sum_{i<j}\delta_{ij}^2\ge0.
 }                                                       \tag{24}
\]

This is a fully justified fixed-diagonal four-site slice, with endpoint
continuity as before. It is recorded as an additional finite comparison,
not a priority claim or the main growing-dimension advance. It does not
cover the rotation obstruction, whose diagonals change. Nor does it assert
unrestricted homogeneous smoothing: both equal diagonals and the displayed
projection endpoint inequalities are essential to this proof.

## 7. Scope and gap audit

**Completed:** a nonconstant projection-preserving deformation; exact complete
entropy difference (19); a positive higher-rank representation (13); a proved
curvature sign and explicit dimension-independent margin; connected rank-two
examples for all ambient dimensions; exact adversarial projection certificates.

**Not completed:** general equal-leverage rank-two swaps with more than two
nonzero outside minor differences; unequal-leverage swaps; arbitrary complex
starting frames without a verified affine projection chord; a sequence of
admissible comparisons reaching a solved reference law; a fixed-density
non-block projection theorem; the sine entropy-rate Jensen sign.

In particular, increasing the entropy curvature relative to a starting kernel
does not bound the final curvature above by zero. Neither the reviewed rank-one
theorem nor the already-proved transfer bridge closes that missing step.
The signed multi-edge formula in OBSTRUCTIONS.md names the remaining terms,
but is not itself promoted to a general sign theorem.

The dependence on `beta,eta,c,t` is explicit. The proof fixes a finite dimension
before all differentiations; its final lower bound is uniform over the stated
family. Endpoint passage uses finite-law continuity only. No spectral/count
entropy substitution, infinite-volume derivative exchange, or claim about
`c -> 1` with a nondegenerate legal interval is made.

## 8. Reproduction and evidence level

From the repository root:

```sh
python research/s8-round2-higher-rank-20260916/verify_round2.py \
  --output-dir /tmp/s8-round2-replay
python -O research/s8-round2-higher-rank-20260916/verify_round2.py \
  --output-dir /tmp/s8-round2-replay-optimized
```

Compare the seven JSON files with [certificates/](certificates/). The checker
uses exact rational atom jets and outward 192-bit dyadic logarithm enclosures;
all strict inequalities are rational comparisons. It checks the four-site
rotation, five- and ten-site connected circuit examples (including a low-contrast case),
the fixed-diagonal four-site slice, and the 34-site
Gaussian obstruction. The latter retains all `2^34` complete atoms by explicit
per-atom jets and binomial multiplicities, not by replacing entropy with count
entropy. Written proofs, not these finite checks, establish Theorem 1 for
arbitrary dimension. The run record distinguishes checks, diagnostics,
publication status, and the elapsed-time requirement.
