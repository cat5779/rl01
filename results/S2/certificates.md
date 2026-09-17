# Complete proof of the finite arithmetic certificates

These certificates are author-executed exact/rigorously enclosed calculations, not independent audits. They prove the stated **finite comparison obstructions**, not a general curvature theorem. Every binary word is retained separately.

## 1. Complete atoms and both derivatives

For a fixed input law `mu` on `k`-subsets, an output word `T`, and input `S`, let

\[
 L_{S,T}(a)=\prod_{i=1}^n w_i(a),\qquad
 w_i(a)=\begin{cases}a+c1_{i\in S},&i\in T,\\1-a-c1_{i\in S},&i\notin T.\end{cases}
\]

Write `sigma_i=1` for an output one and `-1` for an output zero. Each factor has first derivative `sigma_i` and second derivative zero. Starting with `(L,L',L'')=(1,0,0)`, adjoining a coordinate changes the jet to

\[
 (Lw_i,\ L'w_i+\sigma_i L,\ L''w_i+2\sigma_i L').
 \tag{C1}
\]

This is the exact product rule. Thus

\[
 (q_T,q_T',q_T'')=\sum_S\mu(S)(L_{S,T},L_{S,T}',L_{S,T}'').
 \tag{C2}
\]

All sums are finite and exact. At `a=1/200,c=19/20`, each likelihood factor is one of `1/200,199/200,191/200,9/200`; its derivatives in (C1) are still exactly `±1` and zero. Strict positivity of all factors implies every complete output atom is positive.

Differentiation of the full entropy gives

\[
 H''=-\sum_Tq_T''\log q_T-\sum_T(q_T')^2/q_T,
 \tag{C3}
\]

using `sum q_T'=sum q_T''=0`. Formula (C3) retains output-weight acceleration and Fisher terms. No affine-in-`a` assumption is used. For the fixed physical projections, the input laws are independent of `a`; this is legitimate, whereas freezing their output laws would not be.

## 2. Purely rational projection certificate

The integer frame `W` is displayed in proof.md, (6.1). Its Gram determinant is positive, so `P=W(W^TW)^-1 W^T` is a rank-three projection. Its complete input law is

\[
 \mu(S)=\frac{\det(W_S)^2}{\det(W^TW)},\qquad |S|=3.
\]

For disjoint quadrature rotations at mixing parameter `1/2`, consider an input subset `S`. A rotated pair with both selected rows contributes determinant one after normalization, and a pair with no selected row contributes nothing. Suppose `m` rotated pairs have exactly one selected row. Expand the minor over all choices of whether to replace that selected row by its partner, **retaining the original row order**:

\[
 D_S=\sum_{F\subset[m]}i^{|F|}\det W_{S(F)}.
\]

The physical input atom is exactly

\[
 \mu_{\rm phys}(S)=\frac{(\operatorname{Re}D_S)^2+(\operatorname{Im}D_S)^2}
 {2^m\det(W^TW)}.
 \tag{C4}
\]

All entries in (C4) are rational, in fact integer before division. This proves the atom construction used in `exact_certificate.py`. The checker verifies that every law is normalized and nonnegative, that the first law is exactly its affine permutation mixture, that the second law is not that mixture, and that the third physical law equals the original law.

### Independent determinant reconstruction

The checker does not rely solely on (C4). Let `D` be diagonal with `sqrt(2)` on all rotated rows and one elsewhere. The matrix

\[
 M=D P_{\rm phys}D
\]

has entries in the Gaussian rationals `Q(i)`: the corresponding unnormalized transformed frame replaces each paired row by `W_i+iW_j`. Hence

\[
 \det(P_{\rm phys})_A=\frac{\det M_A}{2^{|A\cap\mathrm{Rot}|}}.
 \tag{C5}
\]

Complex Gaussian elimination over exact rational pairs evaluates (C5), with row pivoting. It is checked against the inclusion moments obtained from (C4), for **every** subset `A`.

Independently, the output inclusion moment has the exact scalar polynomial

\[
 m_A(a)=\det(aI_A+c(P_{\rm phys})_A)
       =\sum_{B\subset A}a^{|A|-|B|}c^{|B|}\det(P_{\rm phys})_B.
 \tag{C6}
\]

Differentiate this polynomial twice and invert the Boolean-lattice inclusion transform. The result agrees with every scalar in (C2): four physical states, 128 complete output words per state, and three jet orders, for 1536 separately reconstructed jet values. Every check uses explicit exceptions rather than `assert`, so optimized-mode replays retain the checks.

## 3. Exact algebra for the actual Fourier fixture

Let

\[
 x=\cos(2\pi/7).
\]

The sum of the seventh roots of unity gives

\[
 1+2\cos(2\pi/7)+2\cos(4\pi/7)+2\cos(6\pi/7)=0.
\]

The double- and triple-angle identities yield

\[
 f(x):=8x^3+4x^2-4x-1=0.
\]

Since `0<2*pi/7<pi/3`, `x>1/2`; also `x<1`. The polynomial derivative `24x^2+8x-4` is positive for `x>1/2`, and `f(1/2)<0<f(1)`. Thus the cosine is exactly the unique root in `(1/2,1)`.

Compute in the rational algebra with basis `1,x,x^2` and reduction

\[
 x^3=1/8+x/2-x^2/2.
 \tag{C7}
\]

The necessary cosine values are

\[
 \cos(0)=1,\quad\cos(2\pi/7)=x,\quad
 \cos(4\pi/7)=2x^2-1,\quad
 \cos(6\pi/7)=1/2-x-2x^2.
\]

These determine every entry of (5.1) exactly. The checker verifies `P_0^2=P_0` and `Tr P_0=3` coefficient-by-coefficient in this algebra.

For each set of rotated pairs, form `M=D P_phys D` as above, now with entries in `Q[x]/(f) + i Q[x]/(f)`. Because `D^2` is diagonal with entries one or two, projection preservation can be checked without square roots as

\[
 M D^{-2} M=M.
 \tag{C8}
\]

The checker verifies (C8) for each physical state. Three-by-three principal determinants, divided by `2^(number of rotated selected rows)`, give all 35 potentially nonzero complete input atoms exactly. All other 93 input words have probability zero. Their sums, first-chord identity, non-affinity at the second step, and final-cycle law identity are checked exactly as coefficient identities.

Formula (C1)--(C2) then gives every complete output jet as an exact three-coefficient rational vector. No approximation enters those coefficients. In the final code and clean replays,
an independent path additionally computes all inclusion minors directly from
`M`, builds (C6) and its two derivatives in the cubic algebra, and performs
Boolean Möbius inversion. Every complete jet agrees coefficient-by-coefficient
with (C2), for all four physical states (1536 scalar algebraic jet values).
Hermitian identities and all unchanged leverages `3/7` are checked explicitly.
This extra reconstruction was added after the first completed Fourier receipt;
the clean final standard and optimized runs include it.

### Root isolation and rational evaluation

Starting from `[1/2,1]`, perform 140 bisections. At each rational midpoint, evaluate `f` exactly and retain the subinterval with opposite endpoint signs. Positivity of `f'` on the initial interval proves the resulting rational interval contains precisely the required root. The optimized replay uses 160 bisections.

For `A+B*x+C*x^2`, interval evaluation uses `x in [l,u]` and `x^2 in [l^2,u^2]`, reversing endpoints for negative coefficients. Ignoring dependence can enlarge the enclosure but cannot invalidate it. Every output probability interval has positive lower endpoint.

## 4. Rigorous logarithm enclosure

For rational `q>0`, choose an integer `e` and rational `r` with `q=2^e r`, `1<=r<=2`. Set `z=(r-1)/(r+1)`, so `0<=z<=1/3`. The exact identity is

\[
 \log r=2\sum_{j=0}^{M-1}\frac{z^{2j+1}}{2j+1}+R_M,
 \quad
 0\le R_M\le\frac{2z^{2M+1}}{(2M+1)(1-z^2)}.
 \tag{C9}
\]

It follows by integrating the geometric series for `1/(1-z^2)`, or by bounding each denominator in the positive tail by `2M+1`. The same expression at `r=2` encloses `log 2`. Add `e log 2` with interval endpoint reversal when `e<0`.

The main certificates use `M=24`; the independent-precision same-author replay uses `M=28`. Neither uses floating logarithms. Rational functions in (C3) are interval-evaluated with positive probability denominators, and all acceleration coefficients retain their signs.

For the Fourier certificate, exact rational sums of many unrelated denominators caused an initial tool timeout (a 200-second limit was requested, but that failed invocation did not record its own completed runtime). The repaired, executed version rounds intermediate intervals **outward** to denominator `2^160`:

\[
 [L,U]\longmapsto
 \left[\frac{\lfloor2^{160}L\rfloor}{2^{160}},
       \frac{\lceil2^{160}U\rceil}{2^{160}}\right].
 \tag{C10}
\]

This prevents denominator explosion without losing containment. It is applied to the log interval and the running entropy/curvature sums. The root enclosure, positive-denominator division, interval squaring, signed products, and (C9)--(C10) together rigorously contain the exact curvature. The timeout log is preserved and is **not** counted as a completed pass. The repaired run and the higher-precision optimized replay both completed normally.

Displayed decimal endpoints are rational outward roundings to denominator `10^12`. The enclosures in proof.md are reproduced by the supplied scripts.

## 5. Exact frozen-common-frame test

The separate six-site isometry is

\[
 U=\begin{pmatrix}
 1/2&14/25&0\\1/2&-14/25&0\\
 1/2&2/25&0\\1/2&-2/25&0\\
 0&12/25&3/5\\0&-9/25&4/5
 \end{pmatrix}.
\]

Its three column Gram matrix is exactly the identity. It is (7.1) with

\[
 f=(1,1,1,1)/2,\quad g=(7,-7,1,-1)/10,
 \quad\beta=9/25,
\]
\[
 B=(3,4)^T/5,\qquad v=(4,-3)^T/5.
\]

The covariance graph is connected: every active-to-outside inner product is nonzero, because the active second-column entries and both outside second-column entries are nonzero. It is not a coordinate direct sum.

The checker verifies all input atoms and the disintegration (7.2) exactly. With the first active quadrature at `t=1/2` and `c=19/20`, its full-entropy curvature differences are enclosed by

\[
\begin{array}{c|c}
 a=1/200&[0.303223255922,0.303223255923]\\
 a=1/40&[0.281623892482,0.281623892483]\\
 a=9/200&[0.276680307136,0.276680307137].
\end{array}
\]

All 64 output atoms and all jet orders are included. These are finite exact checks of the initially frozen question, not a proof over its full parameter family and not the basis for early stopping.

## 6. What the execution evidence establishes

* `exact_certificate.py`: exact rational rank-three reversal, every independent input inclusion moment and complete output jet, cycle identity, and robust rank-four Gram obstruction.
* `exact_fourier7.py`: exact cubic-field projection and atom identities, strict rational root enclosure, and full-entropy comparison/payment signs for the genuine Fourier fixture.
* `exact_common_frame.py`: finite exact tests of the initially frozen shared-frame family; no all-rank sign claim.
* Optimized-mode, increased-precision replays use the same author code with stricter precision. They are reproducibility checks, **not independent mathematical review**.
* Floating-point scripts only helped choose questions and fixtures. A bounded no-hit search has no theorem status.

`README.md` gives the actual reproduction commands. The cumulative archive preserves the earlier ZIP unchanged; its historical claims are not promoted to new reviewed premises.
