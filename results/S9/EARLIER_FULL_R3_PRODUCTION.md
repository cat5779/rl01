PROVED_SCOPED_LEMMA

> Independently accepted only at the finite R=3 scope. See [reviewed definitions and scope](EARLIER_RESULT.md) and the [independent audit](EARLIER_INDEPENDENT_AUDIT.md). The cover omitted by the source upload has been independently rebuilt and is supplied in compressed form under reviewed/. Author-era verification wording below is historical.

# A positive full-production theorem on the entire high-contrast R=3 family

This is a finite aligned-family result, not the sine entropy-rate theorem.
It uses full center production with all changing exterior-word weights.
The outward cover and fresh replay of all its accepted leaves have completed.
This positive result does not depend on the growing-layer obstruction. The intact growing proof was subsequently accepted in the separate repair review.

## Statement

Let `E=[-1/4,1/4]`, `37/40<=c<=1`, `0<=a<=1-c`, and
`f_(a,3)=a+c(F_3*1_E)`. For the true radius-three center production of its
noised law, with retention `u=e^(-s)`,

\[
 \boxed{\quad \partial_a^2 I_3(f_{a,3,s})\ge6e^{-2s}
                                      \quad(0\le s<\infty).\quad}  \tag{P1}
\]

At `c=1` the original legal shift interval has one point; derivatives refer
to the legal polynomial-kernel extension described below and give only the
vacuous original chord assertion there. For `c<1` every legal shift is covered.

Consequently the **assigned truncated** functional obeys

\[
 J_3''(a)\le-45/16,
\]

\[
 \boxed{\quad
 J_3((1-t)a_0+ta_1)-(1-t)J_3(a_0)-tJ_3(a_1)
 \ge\frac{45}{32}t(1-t)(a_1-a_0)^2.
 \quad}                                                       \tag{P2}
\]

The untruncated radius-three noise functional, separately defined with time
upper limit infinity, has curvature at most `-3`. Neither functional is
`H_7/7`, nor is either identical to the true entropy rate.

## 1. One rational auxiliary kernel box covers all contrasts

Set `c_*=5pi/16`. Write `B` for the seven-site rational matrix with lag-one
entry `45/192`, lag-three entry `-5/192`, and every other entry zero, including
the diagonal. Its Toeplitz polynomial is

\[
 b_*(\theta)=\frac{15}{32}\cos(2\pi\theta)
                  -\frac5{96}\cos(6\pi\theta).
\]

With `x=cos(2pi theta)`, this is `5x/8-5x^3/24`, so `||B||<=5/12`.
Consider the entire auxiliary box

\[
 K(v,z)=\tfrac12I+v(B+zI),\qquad
 0\le v\le21/20,\quad |z|\le1/24.                            \tag{P3}
\]

Every kernel in this box is strictly legal, since

\[
 \tfrac12-\frac{21}{20}\left(\frac5{12}+\frac1{24}\right)
           =\frac3{160}>0.
\]

Values `v>1` in this **auxiliary matrix box** are not interpreted as negative
noise times or inverse stochastic channels. They are ordinary legal kernels.

For an actual contrast `c` and shift `delta=a-(1-c)/2`, put

\[
 v=u\,c/c_*,\qquad z=(c_*/c)\delta.
\]

The actual noised seven-site kernel is exactly `K(v,z)`. Moreover

\[
 v\le1/c_*<21/20,
 \qquad |z|\le c_*\frac{1-c}{2c}
          \le\frac{3c_*}{74}<\frac1{24}.
\]

The elementary bounds `20/21<5*pi/16<1` were independently checked in the review; the second
maximum uses the actual contrast range `c>=37/40`. Thus (P3) covers all
required original contrasts and shifts without a floating parameter search.

## 2. Polynomial scaled jets retain every noise factor

The complete probabilities of (P3) are the exact bivariate polynomials (17)
in GROWING_RESULT.md, with `u,delta` there replaced by `v,z`. Every monomial is
`C_kl v^k z^l` with `k>=l`. Hence the three layers

\[
 p_y,\qquad r_y=\partial_zp_y/v,\qquad
             t_y=\partial_z^2p_y/v^2
\]

are polynomials, including their extensions at `v=0`. For each center pair
`x,y`, the full scaled curvature is

\[
 \frac{x+y}{2}\left(\frac{r_x}{x}-\frac{r_y}{y}\right)^2
 +\frac{\log(x/y)+1-y/x}{2}\,t_x
 +\frac{\log(y/x)+1-x/y}{2}\,t_y.                              \tag{P4}
\]

Summing (P4) over **all 64 pairs** equals
`partial_z^2 I_3(K(v,z))/v^2` for `v>0`, with a continuous extension at zero.
There is no division by an interval containing zero. At `v=0` the expression
is exactly `8`; this is independently checked using the fair complete law,
whose scaled jets are `2^(-7)`, `2M_y/2^7`, and `4(M_y^2-7)/2^7`.

The `t_x,t_y` terms are all atom accelerations. They are not discarded or
assumed positive. Formula (P4) is also the fully expanded moving-weight
formula, not the Hessian of an affine mixture of probabilities.

## 3. Exact full-box certificate

The frozen `outputs/full_r3_highcontrast_cover.json` is an adaptive binary
partition of `[0,21/20] x [0,1/24]`. All complete atoms are positive on each
accepted rectangle; the outward lower bound for the sum (P4) is at least `6`.
The cover contains **2922** accepted leaves and **5843** total
nodes, with no pending region. Failed parent enclosures remain in the file.

The checker reconstructs all 128 integer event polynomials and uses 128-bit
directed dyadic arithmetic with the same 48-term, explicitly remainder-bounded
logarithm as the paired-layer certificate. Every split is a checked exact
midpoint subdivision. A partial partition cannot receive the success status.
Fresh leaf replays are recorded separately and bind the certificate bytes.

The complete law has the exact symmetry `I_3(K(v,-z))=I_3(K(v,z))`:
`I-K(v,z)` is a physical diagonal gauge of `K(v,-z)`, because `B` has only
odd lags. Occupancy complementation sends `q` to `1-q`, and `phi` is invariant
under that operation. Thus the nonnegative-z cover also proves the negative-z
half of (P3), not by an arbitrary unitary entropy rotation.

This is an author exact finite certificate, pending independent review.
Separate direct determinant/Leibniz/Mobius checks and fresh executions are
supporting verification, not a second reviewer or a formal proof assistant.

## 4. Return to the original parameter and integrate

For fixed original `u,c`, `v` is independent of `a`, and
`partial_a=(c_*/c)partial_z`. Therefore the certified lower bound gives

\[
 \partial_a^2 I_3(f_{a,3,s})
   \ge(c_*/c)^2\,6v^2=6u^2,
\]

which is (P1). This cancellation is why both noise powers in the scaled jets
are indispensable. Integrating over the assigned time interval `[0,log4]`
gives `6 int_0^(log4) exp(-2s) ds =45/16`. Integrating the resulting finite
second-derivative inequality over a legal chord gives (P2).

All differentiations here are of finite, strictly positive complete atom
functions. Their scaled extensions on the compact box are continuous, giving
an integrable `O(u^2)` majorant. This also justifies the stated untruncated
radius-three bound. No entropy-rate derivative-limit exchange occurs.

## 5. What this does not close

The theorem signs the **full** aligned `J_3`, for the entire remaining contrast
range and legal shifts. It does not prove the same assertion for `J_R` with
unbounded `R`. The fixed-radius approximation error does not vanish, so (P2)
by itself cannot sign the actual sine entropy-rate gap. The original upload of the growing adverse-layer obstruction was corrupted
and was quarantined. Its intact replacement is now accepted in the separate
repair review; this positive finite-radius result does not depend on it.
