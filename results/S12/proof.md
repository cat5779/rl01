DISPROVED_ROUTE_LEMMA

# Exact complete-law bias Hessian and two benchmark route obstructions

## 1. Scope

This document does **not** prove or disprove the frozen sine entropy-rate target.
It proves a complete-law structural reduction and then gives two exact,
dimension-extensive counterexamples to natural sign mechanisms that would have
continued the reviewed `c<=37/40` curvature theorem for free:

1. **Conditional-face sign route.**  It is false that every off-diagonal entry
   of the entropy Hessian with respect to independent additive output biases is
   nonpositive for a DPP, even at `c=0.926` and the centered shift.  The failure
   can be repeated by direct sums, so the positive mixed payment is `Theta(n)`.
2. **Free one-sided contrast route.**  It is false that
   `partial_c partial_a^2 H(DPP(aI+cQ)) <= 0` throughout the centered target
   strip.  At `c=0.926`, a scalar contraction gives a strictly positive
   per-site derivative, uniformly over the whole strip
   `|a-(1-c)/2|<=1/200`.

Both witnesses retain the actual complete configuration law.  Neither is a
counterexample to entropy concavity: their total `a`-curvatures remain negative.

The exact global estimate left open is stated in Section 7.

## 2. The complete-law coordinate-bias generators

Write configurations as `y=(y_1,...,y_n) in {-1,+1}^n`, with `+1` meaning
occupied.  Start from any binary input law and let the output coordinates be
conditionally independent, with independent additive bias parameters `a_i`:

\[
 \Pr(Y_i=+1\mid X_i)=a_i+cX_i.
\]

The same formulas follow directly from multilinearity of DPP atoms when the
output kernel is `diag(a_i)+cQ`.  Let `y^i` be `y` with coordinate `i` flipped
and define

\[
 (L_i p)(y):=y_i\bigl(p(y)+p(y^i)\bigr).                 \tag{2.1}
\]

Differentiating the one-site channel factor, before any summation over input
configurations, gives the exact identity

\[
 \partial_{a_i}p=L_i p.                                  \tag{2.2}
\]

The operators commute and are nilpotent:

\[
 L_iL_j=L_jL_i,\qquad L_i^2=0.                            \tag{2.3}
\]

Thus all score and acceleration terms of the moving law remain present.  In
particular, on the diagonal line `a_1=...=a_n=a`, with `L=sum_i L_i`,

\[
 p_a'=Lp,\qquad p_a''=L^2p=2\sum_{i<j}L_iL_jp.            \tag{2.4}
\]

For `H(p)=-sum_y p(y)log p(y)`, differentiation of the complete finite sum gives

\[
 H_{ii}=-\sum_y\frac{(L_ip(y))^2}{p(y)},                 \tag{2.5}
\]

and, for `i!=j`,

\[
 H_{ij}=-\sum_y (L_iL_jp)(y)\log p(y)
         -\sum_y\frac{(L_ip)(y)(L_jp)(y)}{p(y)}.          \tag{2.6}
\]

Equation (2.6) includes both the probability acceleration and Fisher cross term.

## 3. Exact two-site conditional-face formula

Fix `i!=j` and an outside configuration `z`.  Let `T_z` be its marginal mass and
write the normalized two-site conditional table as

\[
\begin{array}{c|cc}
 & y_j=+1 & y_j=-1\\ \hline
 y_i=+1 & a&b\\
 y_i=-1 & c&d
\end{array},
\qquad a,b,c,d>0,\quad a+b+c+d=1.                         \tag{3.1}
\]

Grouping the four terms of (2.6) gives

\[
 H_{ij}=\sum_z T_z\,\Phi(a_z,b_z,c_z,d_z),                \tag{3.2}
\]

where

\[
 \boxed{\displaystyle
 \Phi(a,b,c,d)
 =(ad-bc)\left(\frac1a+\frac1b+\frac1c+\frac1d\right)
 -\log\frac{ad}{bc}.}                                    \tag{3.3}
\]

Here is the algebra, including the normalization layer.  On a face,
`L_iL_jp(y)=y_iy_jT_z`; the `log T_z` terms cancel because
`sum_{y_i,y_j}y_iy_j=0`.  Also, the four Fisher-cross terms are

\[
 \frac{(a+b)(a+c)}a
 -\frac{(a+b)(b+d)}b
 -\frac{(a+c)(c+d)}c
 +\frac{(b+d)(c+d)}d.
\]

Placing them over `abcd` and using `a+b+c+d=1` gives

\[
 \sum_{y_i,y_j}
 y_iy_j\frac{q_{y_i\bullet}q_{\bullet y_j}}{q_{y_iy_j}}
 =-(ad-bc)\left(\frac1a+\frac1b+\frac1c+\frac1d\right).  \tag{3.4}
\]

Substitution in (2.6) proves (3.2)--(3.3), with no discarded normalization,
score, or acceleration term.

The diagonal entries have the exact conditional-Fisher form

\[
 -H_{ii}
 =\mathbb E_{Y_{-i}}
 \frac1{r_i(Y_{-i})(1-r_i(Y_{-i}))}\ge4,                 \tag{3.5}
\]

where `r_i(z)=Pr(Y_i=+1|Y_{-i}=z)`.

For orientation, a normalized two-site DPP with marginal kernel

\[
 K^{(2)}=\begin{pmatrix}u&w\\ \bar w&v\end{pmatrix},
\]

has the four cells in (3.1)

\[
\begin{aligned}
 a&=uv-|w|^2,\\
 b&=u(1-v)+|w|^2,\\
 c&=(1-u)v+|w|^2,\\
 d&=(1-u)(1-v)-|w|^2,
\end{aligned}                                             \tag{3.6}
\]

and hence

\[
 ad-bc=-|w|^2\le0.                                        \tag{3.7}
\]

The logarithmic term in (3.3) has the opposite sign, so (3.7) does not sign
`Phi`.  The obstruction below already occurs for an unconditional two-site
DPP, so no closure theorem for conditioned DPPs is needed anywhere in the
proof.

## 4. Exact positive mixed face at `c=0.926`

Set

\[
 c_*:=\frac{463}{500},\qquad a_*:=\frac{1-c_*}{2}=\frac{37}{1000},
\]

and

\[
 K_*:=\frac1{17}\begin{pmatrix}5&2\\2&11\end{pmatrix}.   \tag{4.1}
\]

The eigenvalues of `K_*` are `(8+-sqrt(13))/17`.  Since `sqrt(13)<4`,

\[
 \frac{37}{1000}<\frac4{17}<\lambda_{\min}(K_*)
 \le\lambda_{\max}(K_*)<\frac{12}{17}<\frac{963}{1000}.
\]

Therefore

\[
 Q_*:=\frac{K_*-a_*I}{c_*}                                \tag{4.2}
\]

is a positive contraction and `K_*=a_*I+c_*Q_*`.  Explicitly,

\[
 Q_*=\begin{pmatrix}
 4371/15742&1000/7871\\
 1000/7871&10371/15742
 \end{pmatrix}.                                           \tag{4.3}
\]

The complete DPP atom probabilities are

\[
 (a,b,c,d)=\frac1{17}(3,2,8,4).                           \tag{4.4}
\]

Indeed `a=det K_*=3/17`, `b=K_{11}-det K_*=2/17`,
`c=K_{22}-det K_*=8/17`, and `d=1-tr K_*+det K_*=4/17`.
In (3.3),

\[
 (ad-bc)\sum\frac1{q_{xy}}=-\frac{29}{102},
 \qquad \frac{ad}{bc}=\frac34,
\]

so

\[
 \boxed{H_{12}=\Phi=\log\frac43-\frac{29}{102}>\frac1{714}>0.} \tag{4.5}
\]

The final strict inequality is elementary and exact.  For `x>0`,

\[
 \log(1+x)>\frac{2x}{2+x},                                \tag{4.6}
\]

because the derivative of the left side minus the right side is
`x^2/((1+x)(2+x)^2)>0`.  At `x=1/3`, (4.6) gives
`log(4/3)>2/7`, and `2/7-29/102=1/714`.

This is a route obstruction, not a target counterexample.  The two diagonal
entries are

\[
 H_{11}=-\frac{1979}{408},\qquad H_{22}=-\frac{449}{102}, \tag{4.7}
\]

and the complete common-shift curvature is

\[
 H''=H_{11}+H_{22}+2H_{12}
 =2\log\frac43-\frac{4007}{408}<0.                        \tag{4.8}
\]
Indeed, `log(1+x)<x` gives `2 log(4/3)<2/3<4007/408`.

## 5. The failure is dimension-extensive

For any `m>=1`, take the direct sum of `m` copies of `Q_*`.  It is again a
positive contraction, and `DPP(a_*I+c_*Q_*^{\oplus m})` is the product of the
`m` complete two-site DPP laws above.  Cross-block Hessian entries vanish, while
each block contributes the positive mixed term (4.5).  With `n=2m`,

\[
 2\sum_{i<j}(H_{ij})_+
 =2m\left(\log\frac43-\frac{29}{102}\right)
 >\frac{m}{357}=\frac{n}{714}.                            \tag{5.1}
\]

Consequently, neither a pointwise claim `H_ij<=0` nor an aggregate claim
`sum_{i<j}H_ij<=0` can be the missing high-contrast payment theorem.  The
obstruction persists at fixed contrast and fixed centered shift as dimension
grows.

## 6. Exact failure of a free one-sided contrast sign on the whole strip

Now take the scalar contraction

\[
 Q=qI_n,\qquad q:=\frac1{100}.                             \tag{6.1}
\]

The DPP is a product Bernoulli law with parameter `p=a+cq`, and therefore

\[
 \frac1n\partial_a^2H=-\frac1{p(1-p)}.                    \tag{6.2}
\]

At fixed `a`,

\[
 \boxed{\displaystyle
 \frac1n\partial_c\partial_a^2H
 =\frac{q(1-2p)}{p^2(1-p)^2}.}                            \tag{6.3}
\]

Fix `c=c_*` and parameterize the centered strip by

\[
 a=\frac{1-c_*}{2}+s=\frac{37}{1000}+s,
 \qquad |s|\le\frac1{200}.                                \tag{6.4}
\]

Then

\[
 p=\frac{2313}{50000}+s
 \in\left[\frac{2063}{50000},\frac{2563}{50000}\right]
 \subset\left(0,\frac{13}{250}\right).                   \tag{6.5}
\]

Thus (6.3) is strictly positive over the **entire** centered strip.  Moreover,
using `1-p<1`, `p<13/250`, and `1-2p>112/125`, one obtains the uniform exact
lower bound

\[
 \boxed{\displaystyle
 \frac1n\partial_c\partial_a^2H>\frac{560}{169}>3.31.}    \tag{6.6}
\]

Hence the reviewed negative curvature at `c=37/40` cannot be transported by a
free sign `partial_c partial_a^2H<=0`, even for independent DPPs.  A successful
one-sided response theorem must include a positive budget of at least the scale
shown in (6.6).  This does not rule out a quantitative upper bound strong enough
to reach `c=0.926`.

## 7. Exact unpaid global payment

Let `mu_i=Pr(Y_i=+1)` and let `r_i(Y_{-i})` be the full conditional probability
from (3.5).  Define the total correlation

\[
 \operatorname{TC}(p):=\sum_i b(\mu_i)-H(p).
\]

Combining (3.2) and (3.5) gives the exact identity

\[
 \operatorname{TC}''
 =\sum_i\left[
   \mathbb E\frac1{r_i(1-r_i)}-\frac1{\mu_i(1-\mu_i)}
  \right]
 -2\sum_{i<j}H_{ij}.                                      \tag{7.1}
\]

Thus the following global payment, not the false facewise sign, would close the
finite-dimensional target with a large margin:

\[
 2\sum_{i<j}H_{ij}
 \le\sum_i\left[
   \mathbb E\frac1{r_i(1-r_i)}-\frac1{\mu_i(1-\mu_i)}
  \right].                                                \tag{7.2}
\]

Indeed, (7.2) is exactly `TC''>=0`; then

\[
 H''\le\sum_i b''(\mu_i)\le-4n.                           \tag{7.3}
\]

Deterministic floating tests in this package found no DPP violation of (7.2),
but they are not proof evidence.  Establishing (7.2), or finding a DPP
counterexample to it, is the precise remaining structural estimate exposed by
this round.

## 8. Bridge and target-level conclusion

No thermodynamic bridge is asserted from the finite witnesses: they are route
counterexamples, not sine-kernel examples.  Conversely, if (7.2) were proved for
all finite DPPs, finite integration of (7.3), followed by the reviewed
value-convergence theorem, would give the sine entropy-rate Jensen inequality
without differentiating the limiting rate.  That implication is recorded only
to identify why (7.2) is live; (7.2) itself remains unproved.

The full `37/40<c<1` target therefore remains open.
