DISPROVED_ROUTE_LEMMA

# Where the adverse count-layer mass goes

This supplement identifies the limiting **signed layer measure**, not merely
its total mass. It explains the growing-family obstruction in RESULT.md.
The S-sine entropy-rate Jensen sign remains undecided. Only the reviewed S9
absolute production-integral approximation is imported; no rate derivative or
new posterior-tail estimate is assumed.

Use the half-density notation of RESULT.md: fixed `0<c<1`,
`a_*=(1-c)/2`, fixed `0<d<(1-c)/2`, `delta in {0,-d,d}`, and odd radii `R`.
Set `D=c+2d<1`, `M_D=D atanh D`, and `N=R+1`.

## 1. Positive measures before forming a Jensen difference

On the normalized exterior-count axis define

\[
 \xi_{R,k}=\frac{k-R}{2R},\qquad
 \mu_R^\delta=\sum_{k=0}^{2R} A_{R,k}(\delta)\,
                                      \delta_{\xi_{R,k}}.
\]

The weights `A` are the **original weighted complete-word productions** of
RESULT.md (6), not count entropy or uniform within-layer probabilities.
For the fixed true sine symbol at shift `a_*+delta`, write `I_delta(s)` for
its full two-sided production at noise time `s`. Define a finite positive
measure by

\[
 \mu^\delta=\int_0^\infty I_\delta(s)\,
                                    \delta_{e^{-s}\delta}\,ds.       \tag{M1}
\]

This is a pushforward of an integrable nonnegative function. It requires no
pointwise differentiability of the entropy rate in the shift.

For every bounded Lipschitz function `F` on `[-1/2,1/2]`,

\[
 \left|\int F\,d\mu_R^\delta-\int F\,d\mu^\delta\right|
 \le \frac{M_D\operatorname{Lip}(F)}{2\sqrt{8R}}
       +\|F\|_\infty\left[A_N(c)+4b(d_R)+\frac{\log2}{N^2}\right].  \tag{M2}
\]

Here `A_N(c)` and `d_R` are exactly the previously reviewed approximation
constants, restated in RESULT.md (1); `d_R` is not the fixed half-chord `d`.

### Proof of (M2)

At any fixed retention `u`, the exterior count has exact mean
`R+2Ru delta`. Its variance is at most `R/2`: the DPP count law is a sum of
`2R` Bernoulli variables, each of variance at most `1/4`. Hence

\[
 \mathbb E|\xi_R-u\delta|\le1/\sqrt{8R}.
\]

The complete conditional bound `0<=phi(q_R)<=M_D u^2` from RESULT.md (8)
therefore gives

\[
 \left|\mathbb E[\phi(q_R)F(\xi_R)]-
              F(u\delta) I_R(f_{a_*+\delta,R,s})\right|
 \le M_D u^2\operatorname{Lip}(F)/\sqrt{8R}.
\]

This does not assert independence between the count and the predictor; it
uses a pointwise upper bound on the latter. Integrating `du/u` over
`[1/N,1]` pays at most the first term in (M2). The reviewed S9 absolute
production-integral approximation pays `A_N(c)+4b(d_R)` for replacing the
noised finite-radius Fejer production by the true one. The omitted true
noise tail costs at most `N^(-2) log2`. Multiplication by the bounded test
function proves (M2). In particular the measures converge weakly.

## 2. The limiting negative mass is an atom, and the positive mass is not

At `delta=0`, (M1) gives

\[
 \mu^0=D_0\delta_0,\qquad D_0=\log2-h(f_{a_*})>0.
\]

For `delta=d`, change variable `x=d e^{-s}` in (M1):

\[
 d\mu^d(x)=\frac{I_d(\log(d/x))}{x}\,dx,
                                    \qquad 0<x\le d.               \tag{M3}
\]

For `delta=-d`, the corresponding density on `[-d,0)` is
`I_{-d}(log(d/|x|))/|x|`. Neither measure has an atom at zero. Indeed
`I_delta(s)<=M_D e^(-2s)` implies the density in (M3) is at most
`M_D x/d^2`, and therefore

\[
 \mu^{\pm d}([-\varepsilon,\varepsilon])
       \le M_D\varepsilon^2/(2d^2)\quad(0\le\varepsilon\le d).
\]

Consequently the limiting signed Jensen measure is

\[
 \nu=\tfrac12(\mu^{-d}+\mu^d)-D_0\delta_0,                    \tag{M4}
\]

with mutually singular positive and negative parts. The negative part has
mass exactly `D_0`, while the positive part has mass
`[log2-h(f_{a_*-d})+log2-h(f_{a_*+d})]/2`.

At finite `R`, write `nu_R=sum_k g_{R,k} delta_(xi_R,k)`. The proof of
RESULT.md Theorem B gives convergence of the total negative mass to `D_0`.
Its wider central bands additionally show that the negative mass outside
any fixed neighborhood of zero tends to zero: it is bounded by the
midpoint production mass outside that neighborhood. Thus

\[
 \nu_R^-\Rightarrow D_0\delta_0,\qquad
 \nu_R^+\Rightarrow\tfrac12(\mu^{-d}+\mu^d),
\]

and the **total variation norms** converge to
`D_0+[D(-d)+D(d)]/2`. This does **not** claim convergence in total variation
distance of the measures. Their finite count grids and the limiting
absolutely continuous endpoint measures in general prevent that stronger
statement.

## 3. Interpretation and remaining sign

The all-layer sum is the mass of (M4):

\[
 \nu([-1/2,1/2])=\tfrac12[D(-d)+D(d)]-D_0.
\]

Comparing these masses is still the original Jensen question. The new
information is that its layerwise negative part is unavoidable and equals
the entire nonzero correlation entropy deficit at the half-density center;
it is not a vanishing approximation error. The result does not rule out a
proof using signed transport between these layers. It also does not claim
that recentering count labels separately at different parameters preserves
a derivative formula without the corresponding moving-weight terms.
