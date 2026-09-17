DISPROVED_ROUTE_LEMMA

# S11 resumed: quantitative obstruction to adaptive S6 continuation without signed mode cancellation

## 0. Result, status, and scope

Put

\[
 c_0=\frac{37}{40}=0.925,
 \qquad c_*=\frac{463}{500}=0.926,
 \qquad c_*-c_0=\frac1{1000}.
\]

This resumed attempt does **not** prove or disprove high-contrast entropy
concavity.  It proves two new route lemmas which explain quantitatively why the
rejected microscopic continuation cannot be turned into a macroscopic one by
adaptive subdivision, adaptive strips, or independently sharpening individual
Chebyshev coefficients.

### Theorem A: the complete current split-tail certificate family is intrinsically microscopic

Consider any direct or adaptive continuation chain inside
\(c_0\le d<c\le c_*\) which, at every step, uses the differentiated split-tail
response formula from the rejected checkpoint, but is otherwise allowed to
choose arbitrarily:

* the common spectral gap \(\delta\),
* the outer interval and its length \(\ell\),
* the inner strip and Bernstein parameter \(\sigma\),
* the cutoff \(M\), and
* a fresh choice of all of these parameters at every step.

The family is defined precisely in Section 2.  Every legal member has response
payment

\[
 R(d,c)>
 \frac{366368000000}{1323}\,(c-d)
 >2.769221466\cdot10^8(c-d).
 \tag{0.1}
\]

The constant is certified by a 100-bin exact rational cover of **all** legal
spectral gaps and all admissible cutoffs.  The bound already grants the method
its best possible zero-width inner strip, drops every positive tail term, and
uses the largest possible outer geometry in the whole slab.

Consequently this family can preserve the desired final curvature margin
\(-1/200\) from the reviewed base margin \(-1/50\) only for total contrast width

\[
 c-c_0<
 \frac{3969}{73273600000000}
 <5.417\cdot10^{-11}.
 \tag{0.2}
\]

Even preserving merely a nonpositive curvature bound requires

\[
 c-c_0<
 \frac{1323}{18318400000000}
 <7.223\cdot10^{-11}.
 \tag{0.3}
\]

Thus the previous \(9\cdot10^{-12}\) result was already within a small constant
factor of the ceiling of this entire certificate architecture.  Reoptimizing
or subdividing it cannot approach \(c=0.926\).

### Theorem B: exact independent mode budgets also cannot reach 0.926

A broader class is the **uniform mode-separable S6 family**.  At every step it
may use exact, one-sided, coefficient-specific response bounds, but it must pay
for each Chebyshev mode separately against the single reviewed uniform margin;
negative cancellation between distinct modes is not credited.  Arbitrary gaps,
strips, cutoffs, and adaptive subdivision are allowed.

For the exact two-site contraction

\[
 n=2,\qquad Q=\operatorname{diag}(1,0),
 \tag{0.4}
\]

the first Chebyshev mode has zero contrast response in shift curvature, while
the second mode has the exact response

\[
 \bigl(u_{c,2}-u_{d,2}\bigr)''(x)
 =\frac{120(c-d)(2x-1+c+d)}{(1+\delta)^4}.
 \tag{0.5}
\]

For every legal shift \(0\le x\le1-c\), every
\(c_0\le d<c\le c_*\), and every legal common spectral gap,

\[
 \bigl(u_{c,2}-u_{d,2}\bigr)''(x)
 \ge
 \frac{4177920000}{47458321}(c-d)
 >88.0334(c-d).
 \tag{0.6}
\]

Therefore the second mode alone forces a cumulative noncancelling payment

\[
 \frac{4177920}{47458321}>0.0880>\frac1{50}
 \tag{0.7}
\]

between \(c_0\) and \(c_*\).  Such a certificate cannot even retain sign from
the reviewed \(1/50\) margin, let alone retain the desired \(1/200\) margin.
This conclusion permits exact local mode profiles; it is not an artifact of the
coarse tail envelope.

At the centered shift, the lower coefficient in (0.6) improves to

\[
 \frac{4546560000}{47458321}>95.8011.
 \tag{0.8}
\]

The obstruction is to **noncancelling bookkeeping**, not to entropy concavity.
For the same witness (0.4), the complete normalized entropy response at the
center from \(0.925\) to \(0.926\) is exactly

\[
 F_{c_*}''-F_{c_0}''
 =-\frac{3125000}{8800857}<0.
 \tag{0.9}
\]

This cancellation can be quantified exactly inside one fixed Chebyshev
expansion.  At the same shift, choose the strictly interior gap
\(\delta=1/50\).  Then mode two contributes

\[
 (u_{c_*,2}-u_{c_0,2})''
 =\frac{231250}{2255067}>0,
\]

while mode one has zero response.  Uniform convergence of the twice
differentiated tail therefore gives

\[
 \sum_{m\ge3}(u_{c_*,m}-u_{c_0,m})''
 =-\frac{1009142506250}{2205169132491}
 <-0.4576.
 \tag{0.10}
\]

Thus higher Chebyshev modes cancel the positive second-mode response strongly.
Any continuation proof reaching \(0.926\) must retain signed cross-mode
cancellation or couple the response to a stronger, \(Q\)-dependent base margin.
Independently improving each positive mode budget is insufficient.

## 1. Pinned reviewed inputs

All repository inputs were read at

`191297f3073e60f5954a93ae5e6e94c32447b590`.

The only imported mathematical results used here are:

1. **Reviewed base curvature.**  For every finite Hermitian contraction
   \(0\le Q\le I\), every legal shift, and every \(0\le d\le c_0\),
   \[
   \frac1n\frac{\partial^2}{\partial x^2}
   H(\operatorname{DPP}(xI+dQ))\le-\frac1{50}.
   \tag{1.1}
   \]
2. **Reviewed full-atom expansion.**  On a common spectral strip
   \(\delta I\le xI+sQ\le(1-\delta)I\), put
   \[
   A_{S,s}=xI+sQ-D_{S^c},\quad
   X_{S,s}=\frac{2A_{S,s}^2-(1+\delta^2)I}{1-\delta^2},\quad
   r=\frac{1-\delta}{1+\delta}.
   \tag{1.2}
   \]
   Then
   \[
   F_s(x):=\frac1nH(\operatorname{DPP}(xI+sQ))
   =C_\delta+\sum_{m\ge1}u_{s,m}(x),
   \tag{1.3}
   \]
   \[
   u_{s,m}(x)=\frac{(-1)^m r^m}{mn}
   \mathbb E_s\operatorname{Tr}T_m(X_{S,s}(x)),
   \quad \deg_xu_{s,m}\le2m,
   \quad \|u_{s,m}\|\le\frac{r^m}{m}.
   \tag{1.4}
   \]
   The expectation is under the actual moving full DPP law.
3. **Reviewed nested Bernstein bound.**  For a degree-\(D\) polynomial on an
   outer interval of length \(\ell\), and a concentric inner interval with
   parameter \(0<\sigma\le1\),
   \[
   \|P''\|_{\rm inner}\le\frac4{\ell^2}
   \left(\frac{D^2}{\sigma^2}+\frac D{\sigma^3}\right)
   \|P\|_{\rm outer}.
   \tag{1.5}
   \]
4. **Reviewed sine value bridge.**  Finite normalized entropies of the true sine
   Toeplitz blocks converge in value to the entropy rate.  Thus a proved finite
   Jensen inequality passes by values, without differentiating the limit.

The rejected previous S11 package derived the additional, presently
**unreviewed**, tail estimate

\[
 \|u_{c,m}-u_{d,m}\|
 \le(c-d)r^m(2+a_\delta m),
 \qquad a_\delta=\frac{2\sqrt2\,\delta}{1-\delta^2},
 \tag{1.6}
\]

for \(m>M\), provided

\[
 4\delta^3(2-\delta)(M+1)^2\ge(1-\delta^2)^2.
 \tag{1.7}
\]

The present Theorem A is conditional only on using that declared certificate
formula; it does not promote (1.6) to independently reviewed status.  Theorem B
is proved afresh below from the reviewed expansion and elementary DPP moments.

## 2. The two certificate families

### 2.1 Adaptive differentiated split-tail family

For one step \(h=c-d>0\), this family chooses a common gap \(\delta\), an outer
interval of length \(\ell\), an inner Bernstein parameter \(\sigma\), and an
integer cutoff \(M\) satisfying (1.7).  It uses the value response

\[
 \varepsilon=h\frac{\Lambda_\delta}{2},
 \qquad \Lambda_\delta=\log\frac{1-\delta}{\delta},
 \tag{2.1}
\]

and the response formula

\[
\begin{aligned}
 R={}&\left(\frac{16M^2}{\ell^2\sigma^2}
 +\frac{8M}{\ell^2\sigma^3}\right)(\varepsilon+W)\\
 &+h\left[
 \frac{16}{\ell^2\sigma^2}(2S_2+a_\delta S_3)
 +\frac8{\ell^2\sigma^3}(2S_1+a_\delta S_2)
 \right],
\end{aligned}
\tag{2.2}
\]

where \(W,S_j\ge0\).  We allow fresh parameters at every step.  The only part
used in the obstruction is the positive head-value term

\[
 R\ge\frac{16M^2}{\ell^2\sigma^2}\varepsilon.
 \tag{2.3}
\]

Thus dropping the rest can only make the family look stronger.

### 2.2 Uniform mode-separable family

Fix a step \(d<c\), a target shift set \(J\), and a legal common gap \(\delta\).
A uniform mode-separable certificate supplies nonnegative payments
\(B_m(d,c,J,\delta)\) such that

\[
 (u_{c,m}-u_{d,m})''(x)\le B_m
 \tag{2.4}
\]

for every finite contraction \(Q\) and every \(x\in J\), then concludes

\[
 F_c''(x)\le F_d''(x)+\sum_{m\ge1}B_m.
 \tag{2.5}
\]

The payments may be exact and one-sided; they need not be absolute-value bounds.
They may depend on the step geometry and be reoptimized adaptively.  The standard
complement reduction may first be used, so the active contraction can be taken
to satisfy \(\tau=\operatorname{Tr}Q/n\le1/2\).  What is not allowed is crediting
a negative response of one mode against a positive response of another, or
coupling a mode payment to a stronger \(Q\)-specific base margin.  This precisely
captures uniform coefficientwise triangle accounting.

## 3. Proof of Theorem A

### 3.1 Best-case geometry

For any \(c\ge c_0\), the legal shift interval has length

\[
 1-c\le1-c_0=\frac3{40}=:L_0.
 \tag{3.1}
\]

A common spectral gap forces every outer interval into
\([\delta,1-c-\delta]\).  Hence

\[
 0<\delta\le\frac{L_0}{2}=\frac3{80},
 \qquad
 \ell\le L_0-2\delta,
 \qquad
 0<\sigma\le1.
 \tag{3.2}
\]

Also

\[
 \Lambda_\delta=\log\frac{1-\delta}{\delta}>3.
 \tag{3.3}
\]

Indeed \((1-\delta)/\delta\ge77/3>21\).  The elementary series estimate

\[
 e=1+1+\frac12+\sum_{k\ge3}\frac1{k!}
 <1+1+\frac12+\frac14=\frac{11}{4}
 \tag{3.4}
\]

uses \(k!\ge2\cdot3^{k-2}\) for \(k\ge3\).  Therefore
\(e^3<(11/4)^3=1331/64<21<77/3\), proving (3.3).

Substituting (2.1) into (2.3), and granting \(\sigma=1\), gives

\[
 \frac Rh>
 \frac{24M^2}{\ell^2}.
 \tag{3.5}
\]

### 3.2 Exact optimization over every gap and cutoff

Define

\[
 \Phi(\delta)=\frac{4\delta^3(2-\delta)}{(1-\delta^2)^2}.
 \tag{3.6}
\]

The threshold (1.7) is \(\Phi(\delta)(M+1)^2\ge1\).  On
\(0<\delta<1\), \(\Phi\) is strictly increasing because

\[
 \frac{d}{d\delta}\log\Phi
 =\frac3\delta-\frac1{2-\delta}+\frac{4\delta}{1-\delta^2}>0.
 \tag{3.7}
\]

Indeed the first two terms equal
\((6-4\delta)/(\delta(2-\delta))>0\) on this domain, and the final term is
positive.

Partition \((0,L_0/2]\) into 100 exact bins

\[
 I_i=\left[\frac{iL_0}{200},\frac{(i+1)L_0}{200}\right],
 \qquad0\le i<100.
 \tag{3.8}
\]

For \(\delta\in I_i\), monotonicity implies that the legal cutoff is at least
\(M_i\), the smallest cutoff satisfying (1.7) at the right endpoint of \(I_i\).
Also \(\ell\le L_0-2iL_0/200\).  Therefore every certificate in that bin obeys

\[
 \frac Rh>
 C_i:=\frac{24M_i^2}{(L_0-2iL_0/200)^2}.
 \tag{3.9}
\]

All 100 values are reconstructed exactly by
`scripts/build_obstruction_certificate.py` and independently by
`scripts/recheck_obstruction.py`.  Their exact minimum is

\[
 \min_i C_i=C_{58}
 =\frac{366368000000}{1323},
 \qquad M_{58}=107.
 \tag{3.10}
\]

This proves (0.1).  No floating optimizer, sampled entropy sign, or selected
profile is involved.

### 3.3 Adaptive chains do not escape

For a chain \(c_0=d_0<d_1<\cdots<d_k\le c_*\), the margin must be carried as

\[
 m_k=\frac1{50}-\sum_{j=1}^kR(d_{j-1},d_j).
 \tag{3.11}
\]

Equation (0.1) gives

\[
 \sum_jR(d_{j-1},d_j)
 >\frac{366368000000}{1323}(d_k-c_0).
 \tag{3.12}
\]

This already allows every step to reoptimize all parameters.  At \(d_k=c_*\),
the right side is \(366368000/1323>2.7\cdot10^5\), overwhelmingly larger than
both available budgets \(1/50\) and \(3/200\).  Solving (3.12) against these
budgets gives (0.2)--(0.3).

### 3.4 Quantitative diagnosis of the full declared formula

The exact obstruction above deliberately keeps only one unavoidable positive
term.  A separate floating multiresolution diagnostic, not used in the proof,
optimizes the **complete** formula (2.2) at \(c=0.926\) with the best-case
zero-width centered target.  It finds approximately

\[
 \delta=0.0205796067,\qquad M=162,\qquad R/h=1.118148932\cdot10^9.
\]

The decomposition per unit contrast is

| charge | approximate size | share |
|---|---:|---:|
| head amplification of value coupling \(\varepsilon\) | \(7.542542842\cdot10^8\) | 67.46% |
| head amplification of tail value | \(1.519861719\cdot10^8\) | 13.59% |
| differentiated tail curvature | \(2.119084759\cdot10^8\) | 18.95% |

Thus the dominant loss is the \(M^2/\ell^2\) amplification of a uniform value
modulus, not a badly selected subdivision.  Even deleting the latter two rows
leaves the rigorous family obstruction of Section 3.2.  The diagnostic is
reproducible in `scripts/diagnose_split_tail_optimizer.py`.

## 4. Exact first and second Chebyshev curvatures

This section proves the low-mode identities used in Theorem B.

Let

\[
 K=xI+sQ,\qquad E=D_{S^c},\qquad A=K-E,
 \tag{4.1}
\]

where \(S\sim\operatorname{DPP}(K)\).  The complement indicators in \(E\) form
a DPP with kernel \(R=I-K\), so

\[
 \mathbb E E_{ii}=R_{ii},
 \qquad
 \mathbb E(E_{ii}E_{jj})=R_{ii}R_{jj}-|R_{ij}|^2\quad(i\ne j).
 \tag{4.2}
\]

### 4.1 The quadratic trace

Since \(E^2=E\),

\[
 \operatorname{Tr}A^2
 =\operatorname{Tr}K^2-2\operatorname{Tr}KE+\operatorname{Tr}E.
 \tag{4.3}
\]

Taking expectations gives

\[
 \mathbb E\operatorname{Tr}A^2
 =n-3\operatorname{Tr}K+\operatorname{Tr}K^2
 +2\sum_iK_{ii}^2.
 \tag{4.4}
\]

Substituting \(K=xI+sQ\) yields

\[
 \mathbb E\operatorname{Tr}A^2
 =n(1-3x+3x^2)+s(-3+6x)\operatorname{Tr}Q
 +s^2\left(\operatorname{Tr}Q^2+2\sum_iQ_{ii}^2\right).
 \tag{4.5}
\]

Hence

\[
 \partial_x^2\mathbb E\operatorname{Tr}A^2=6n.
 \tag{4.6}
\]

### 4.2 The quartic trace

Cyclicity of trace and \(E^2=E\) give

\[
\begin{aligned}
 \operatorname{Tr}(K-E)^4={}&\operatorname{Tr}K^4
 -4\operatorname{Tr}K^3E+4\operatorname{Tr}K^2E\\
 &+2\operatorname{Tr}KEKE-4\operatorname{Tr}KE+\operatorname{Tr}E.
\end{aligned}
\tag{4.7}
\]

The only two-point term is

\[
\begin{aligned}
 \mathbb E\operatorname{Tr}KEKE
 ={}&\sum_iK_{ii}^2R_{ii}\\
 &+\sum_{i\ne j}|K_{ij}|^2
 \left(R_{ii}R_{jj}-|K_{ij}|^2\right).
\end{aligned}
\tag{4.8}
\]

Substitute \(K=xI+sQ\) in (4.7)--(4.8), differentiate twice in \(x\), and
collect the trace and diagonal-square invariants.  The exact identity is

\[
\begin{aligned}
 \partial_x^2\mathbb E\operatorname{Tr}A^4
 ={}&n(60x^2-60x+20)
 +60s(2x-1)\operatorname{Tr}Q\\
 &+20s^2\left(2\operatorname{Tr}Q^2+\sum_iQ_{ii}^2\right).
\end{aligned}
\tag{4.9}
\]

The symbolic reconstruction script independently expands every term.

### 4.3 The mode formulas

Write \(D=1-\delta^2\), \(B=1+\delta^2\).  From
\(X=(2A^2-BI)/D\), (4.6), and the coefficient in (1.4),

\[
 u_{s,1}''=-\frac{12r}{D}=-\frac{12}{(1+\delta)^2}.
 \tag{4.10}
\]

This is independent of \(s\), proving

\[
 (u_{c,1}-u_{d,1})''=0.
 \tag{4.11}
\]

Next \(T_2(X)=2X^2-I\).  Put

\[
 \tau=\frac{\operatorname{Tr}Q}{n},\qquad
 q_2=\frac{\operatorname{Tr}Q^2}{n},\qquad
 d_2=\frac{\sum_iQ_{ii}^2}{n}.
 \tag{4.12}
\]

Equations (4.6) and (4.9) give

\[
\begin{aligned}
 u_{s,2}''=\frac4{(1+\delta)^4}\bigl[{}
 &60x^2-60x+20-6(1+\delta^2)\\
 &+60s(2x-1)\tau+20s^2(2q_2+d_2)\bigr].
\end{aligned}
\tag{4.13}
\]

Therefore

\[
 (u_{c,2}-u_{d,2})''
 =\frac{4(c-d)}{(1+\delta)^4}
 \left[60(2x-1)\tau+20(c+d)(2q_2+d_2)\right].
 \tag{4.14}
\]

These are exact identities, not bounds.

## 5. Proof of Theorem B

First note that the witness below is not merely convenient: it maximizes the
mode-two response over the complement-reduced class.  Since \(0\le Q\le I\),

\[
 q_2\le\tau,\qquad d_2\le\tau.
 \tag{5.1}
\]

Indeed \(\operatorname{Tr}Q^2\le\operatorname{Tr}Q\) spectrally and
\(Q_{ii}^2\le Q_{ii}\) term by term.  Throughout the benchmark slab and every
legal shift,

\[
 2x-1+c+d\ge2c_0-1>0.
 \tag{5.2}
\]

Therefore (4.14), (5.1), and \(\tau\le1/2\) imply

\[
 (u_{c,2}-u_{d,2})''
 \le \frac{120(c-d)(2x-1+c+d)}{(1+\delta)^4}.
 \tag{5.3}
\]

Equality is attained by \(n=2\) and \(Q=\operatorname{diag}(1,0)\), for which

\[
 \tau=q_2=d_2=\frac12.
 \tag{5.4}
\]

Thus this witness gives the **exact worst-case local mode-two profile** after
complement reduction, not just a lower test.  Equation (4.14) becomes (0.5).
If \(x\) is legal at contrast \(c\), then
\(x\ge0\), so

\[
 2x-1+c+d\ge c+d-1\ge2c_0-1=\frac{17}{20}.
 \tag{5.5}
\]

A common spectral gap at that point must satisfy

\[
 \delta\le\min\{x,1-c-x\}
 \le\frac{1-c}{2}\le\frac3{80}.
 \tag{5.6}
\]

Thus

\[
 \frac1{(1+\delta)^4}\ge\left(\frac{80}{83}\right)^4.
 \tag{5.7}
\]

Combining (0.5), (5.5), and (5.7) gives

\[
 (u_{c,2}-u_{d,2})''(x)
 \ge120\frac{17}{20}\left(\frac{80}{83}\right)^4(c-d)
 =\frac{4177920000}{47458321}(c-d),
 \tag{5.8}
\]

which is (0.6).  Every uniform nonnegative upper payment for mode two must be at
least its actual value on this witness.  Summing (5.8) over an adaptive chain
proves (0.7).  The strip location, width, cutoff, and subdivision are irrelevant.

At the centered target shift \(x=(1-c)/2\), the factor in (0.5) equals \(d\).
Replacing \(17/20\) by \(c_0=37/40\) proves (0.8).

## 6. The witness has favorable full entropy response

For \(Q=\operatorname{diag}(1,0)\), the DPP input is deterministic and the two
output coordinates are independent with success probabilities \(x+s\) and
\(x\).  Hence

\[
 F_s(x)=\frac12\bigl[b(x+s)+b(x)\bigr],
 \qquad b''(p)=-\frac1{p(1-p)}.
 \tag{6.1}
\]

For every legal \(x\ge0\) and \(s\ge c_0\), \(x+s>1/2\), and \(b''\) is strictly
decreasing there.  Thus

\[
 F_c''(x)-F_d''(x)<0
 \tag{6.2}
\]

whenever \(c>d\).  In particular, at \(c=c_*\) and
\(x=(1-c_*)/2=37/1000\), the two moving probabilities are
\(963/1000\) and \(481/500\), giving the exact value (0.9).  The two
absolute curvatures are

\[
 F_{c_0}''=-\frac{243875000}{8800857},\qquad
 F_{c_*}''=-\frac{1000000}{35631}.
 \tag{6.3}
\]

Thus this witness also has vastly more negative base curvature than the uniform
reviewed margin \(-1/50\).  A certificate that couples response to
same-witness excess margin may exploit this; the uniform mode-separable family
was defined not to do so.

For the fixed expansion gap \(\delta=1/50\), all kernels in a neighborhood of
this shift lie strictly between \(\delta I\) and \((1-\delta)I\).  The reviewed
coefficient envelope and nested Bernstein estimate bound the second derivatives
of the tail by a summable multiple of \(m^3r^m\).  Consequently the series may
be differentiated twice and subtracted termwise.  Equation (0.5) gives

\[
 (u_{c_*,2}-u_{c_0,2})''
 =\frac{120(c_*-c_0)c_0}{(1+1/50)^4}
 =\frac{231250}{2255067}.
 \tag{6.4}
\]

Mode one has zero response by (4.11).  Subtracting (6.4) from (0.9) proves the
exact signed higher-mode identity (0.10).

Equations (0.5) and (6.2) have opposite signs.  Therefore the positive
second-mode response is canceled by modes \(m\ge3\).  Theorem B identifies a
necessary structural feature of any successful continuation certificate:
**signed grouping across modes, or a response/base-margin coupling, is
mandatory.**

## 7. Adaptive strips and legal margin accounting

If a theorem at contrast \(d\) is known on a centered strip of half-width
\(w_d\), and a step to \(c>d\) targets half-width \(w_c\), strip inclusion
requires

\[
 w_c+\frac{c-d}{2}\le w_d.
 \tag{7.1}
\]

The carried margin is

\[
 m_c=m_d-R(d,c),
 \tag{7.2}
\]

and along a chain it is the original margin minus the **sum** of all payments.
Neither theorem permits resetting to \(1/50\).

Theorem A grants \(\sigma=1\), corresponding to a zero-width inner target, and
uses the maximal possible outer length.  Any nontrivial strip has
\(\sigma<1\), so it only increases the response.  Theorem B holds at every
legal shift point and therefore survives arbitrary strip placement.  Adaptive
strips cannot remove either obstruction, while (7.1) imposes an additional loss
not charged in our lower bounds.

## 8. Exact outstanding estimate for a successful continuation

To retain curvature at most \(-1/200\) from the reviewed \(-1/50\) base while
jumping by \(10^{-3}\), a direct or integrated signed response estimate must
cost at most

\[
 \frac3{200}=0.015,
 \tag{8.1}
\]

or average at most \(15\) per unit contrast.  The current split-tail family has
certified average cost above \(2.769\cdot10^8\).  Even exact independent mode
payments have a mode-two floor above \(88.033\).  Therefore a successful
uniform estimate must certify at least

\[
 \frac{3466045185}{47458321}>73.033
 \tag{8.2}
\]

units of signed cancellation per unit contrast against that mode-two payment.
On the centered track the required cancellation is above \(80.801\) per unit.

This is the exact unpaid estimate.  It cannot be supplied by smaller steps,
larger or smaller strips, a reoptimized cutoff, or independently sharper
nonnegative mode profiles.  A new argument must bound a **signed group** of
modes, or relate positive response to excess base curvature for the same
\(Q\).

## 9. Entropy-rate bridge

No new finite curvature region is asserted, so there is no new sine-rate sign
theorem to pass to the limit.  The reviewed bridge remains the correct one: if
a future finite-dimensional argument proves a uniform curvature upper bound on
a shift interval, integrate it to a finite Jensen inequality and then use value
convergence of the true sine blocks.  One must not differentiate the limiting
entropy rate.

## 10. Old/new separation and reproducibility

The previous package is included byte-for-byte under

`prior_checkpoint/S11_quantitative_continuation_REJECTED_UNREVIEWED.zip`

with SHA-256

`7021ca3527428f1cb0f9f085ef61e5daed7f1292abead8567caa65054fb885af`.

It is retained only as an unreviewed checkpoint.  None of its microscopic
rectangles is claimed as completion of this resumed round.

New files in this package reconstruct:

* the complete 100-bin exact obstruction to the adaptive split-tail family;
* the exact first- and second-mode curvature identities;
* the mode-separable obstruction at every legal shift;
* the favorable complete-entropy product witness and exact signed
  `m>=3` cancellation showing that the obstruction is not a target
  counterexample; and
* independent exact replay of every load-bearing rational comparison.

## 11. Claim audit

**Proved analytically:** Theorems A and B, the low-mode identities, legal adaptive
margin accounting, and the favorable full-entropy witness.

**Exact certificate:** all constants in (0.1)--(0.9), every one of the 100 gap
bins, every cutoff floor, both width ceilings, the mode-two floors, and the exact
product response.

**Floating diagnostic only:** the random-matrix finite-difference regression in
`evidence/diagnostics/`; it is not used in any proof.

**Not proved:** concavity at \(c=0.926\), any larger finite curvature region, or
the full sine target.  The new result is a rigorous obstruction to two precisely
defined live continuation families and an exact identification of the missing
signed cancellation estimate.
