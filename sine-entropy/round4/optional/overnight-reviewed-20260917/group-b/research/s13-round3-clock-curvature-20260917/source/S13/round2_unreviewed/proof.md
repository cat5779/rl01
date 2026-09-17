PROVED_SCOPED_LEMMA

# S13 continuation: logarithmic Fourier-potential transfer defect, its curvature boundary layer, and a positive potential-clock repair

## 1. Status and theorem

All logarithms are natural.  This is a new substantive continuation of S13 at
commit `191297f3073e60f5954a93ae5e6e94c32447b590`.  The sine entropy-rate target
remains open.  The earlier six/eight-site theorem and the identity

\[
H''=H(M)''-2n\log n-D_F''                                      \tag{1.1}
\]

are preserved as **author-reported, not independently audited** results.  The
proof below reconstructs every part of (1.1) that it uses.  In particular,
`(E M log n)''=0`; the term `-2n log n` is the curvature of the negative
Fourier-potential expectation, not of the partition term.

Fix `0<c<1`.  Let `n` be even, `k=n/2`, and let `P_(n,k)` be the projection onto
the first `k` cyclic Fourier columns.  Its input law on `k`-subsets is

\[
 \mu_n(A)=n^{-k}\exp U_n(A),\qquad
 U_n(S)=\sum_{\{i,j\}\subset S}\log|e^{2\pi i i/n}-e^{2\pi i j/n}|^2.       \tag{1.2}
\]

Pass this input through the exact homogeneous channel
`Pr(Y_i=1|A)=a+c 1_{i in A}`.  Write `M=|Y|`, `pi_l=Pr(M=l)`, and `q_l` for the
actual conditional law on the `l`-slice.  Let `qtilde_l` be the explicit
mean-overlap Bernoulli--Laplace surrogate defined in Section 2.  The exact
potential-transfer defect is

\[
 \boxed{\Delta_n(a,c)=\sum_{l=0}^n\pi_l(a,c)
 \left(E_{\widetilde q_l}U_n-E_{q_l}U_n\right).}                            \tag{1.3}
\]

The count weights in (1.3) are the **actual moving weights**.  No frozen-layer
or affine-atom approximation is used.

### Theorem 1 (new growing-family size and curvature theorem)

Let

\[
 m(a)=a+\frac c2,\qquad
 x(a)=\min\{m(a),1-m(a)\},\qquad
 z(a,c)=1+\frac{c}{a(1-c-a)}.                                                \tag{1.4}
\]

For `0<x<=1/2` and `z>1`, let `lambda=lambda(x,z)` be the smaller root in
`(0,1)` of

\[
 x(z-1)\lambda^2-(z+1)\lambda+(1-x)(z-1)=0,                                 \tag{1.5}
\]

equivalently

\[
 \lambda(x,z)=\frac{2(1-x)(z-1)}{z+1+
 \sqrt{(z+1)^2-4x(1-x)(z-1)^2}}.                                            \tag{1.6}
\]

Define

\[
\begin{aligned}
 d(x,z)
 &=\lambda^2\left[
 -2\log\lambda-
 \frac{(1-\lambda^2)(1-2x)}{1-x(1+\lambda^2)}\right],                       \tag{1.7}\\
 C(a,c)&=x(a)^2d(x(a),z(a,c)).                                                \tag{1.8}
\end{aligned}
\]

Then:

1. **Uniform value scale.**  On every compact `I subset (0,1-c)`, along even
   `n -> infinity`,

   \[
     \boxed{\sup_{a\in I}\left|\frac{\Delta_n(a,c)}{\log n}-C(a,c)\right|
     \longrightarrow0.}                                                     \tag{1.9}
   \]

   Moreover `C(a,c)>0` throughout the legal interior.  Thus the exact finite
   mismatch grows like `log n`, not like `n` or `n log n`.

2. **Integrated Jensen/weak-curvature scale.**  For every fixed interior chord
   `0<a_0,a_1<1-c`, `a_t=(1-t)a_0+t a_1`,

   \[
   \begin{aligned}
   &(1-t)\Delta_n(a_0,c)+t\Delta_n(a_1,c)-\Delta_n(a_t,c)\\
   &\quad=\big[(1-t)C(a_0,c)+tC(a_1,c)-C(a_t,c)\big]\log n+o(\log n).         \tag{1.10}
   \end{aligned}
   \]

   Hence its normalization by `n` tends to zero.  More generally, for every
   compactly supported `C^2` test function `phi` in the legal interior,

   \[
     \frac1{\log n}\int\phi(a)\Delta_n''(a,c)\,da
     \longrightarrow\int\phi''(a)C(a,c)\,da.                               \tag{1.11}
   \]

   Equation (1.11) is obtained by exact integration by parts at finite `n`; it
   does not differentiate the `o(log n)` value remainder.

3. **Midpoint boundary layer and sign.**  Put
   `a_*=(1-c)/2` and `v_c=(1-c^2)/4`.  For every fixed real `u`,

   \[
    \boxed{
    \frac{\Delta_n''(a_*+u/\sqrt n,c)}{\sqrt n\log n}
    \longrightarrow
    -\frac{4c^2}{\sqrt{2\pi v_c}}e^{-u^2/(2v_c)}
    =-\frac{4c^2\sqrt{2/\pi}}{\sqrt{1-c^2}}
      e^{-2u^2/(1-c^2)}.}                                                    \tag{1.12}
   \]

   In particular `Delta_n(a_*,c)>0` for all sufficiently large even `n`, while

   \[
    \Delta_n''(a_*,c)
    \sim-\frac{4c^2\sqrt{2/\pi}}{\sqrt{1-c^2}}\sqrt n\log n<0.               \tag{1.13}
   \]

   Positivity of the defect therefore does not determine its curvature.  The
   spike is still subextensive after division by `n`: its normalized height is
   `O(log n/sqrt n)`.  Its integrated mass is logarithmic.  Indeed `C` is
   continuous but has derivative jump `-4c^2` at `a_*`, so the distributional
   second derivative in (1.11) contains `-4c^2 delta_(a_*)`.

### Theorem 2 (new positive potential-clock correction and a precise no-go class)

For every layer with `2<=l<=n-2`, let `theta_(n,l)(a,c)` be the exact actual
Johnson degree-two multiplier defined in (2.15), and put

\[
 \widehat\tau_l=-\frac{\log\theta_{n,l}}{\gamma_{2,l}},\qquad
 \gamma_{2,l}=\frac{2(n-1)}{l(n-l)},\qquad
 \widehat q_l=u_l e^{\widehat\tau_lL_l}r_l^{max}.                            \tag{1.14}
\]

On the four layers where the centered degree-two potential vanishes, set
`qhat_l=qtilde_l`.  Then:

1. `0<theta_(n,l)<1`; hence (1.14) is a normalized strictly positive law.
2. It matches the potential **layer by layer**:

   \[
     E_{\widehat q_l}U_n=E_{q_l}U_n.                                         \tag{1.15}
   \]

   Therefore the aggregate corrected defect is exactly zero, with the actual
   `pi_l` retained.
3. On any compact legal `I`, the mean-clock and potential-clock outputs admit a
   coupling with bounded expected Hamming distance.  Consequently

   \[
    |H(\widehat p_a)-H(\widetilde p_a)|=O_I(\log n),                          \tag{1.16}
   \]

   uniformly in `a in I`.  A direct actual-to-corrected coupling also gives

   \[
    |H(p_a)-H(\widehat p_a)|=O_I(\sqrt n\log n).                             \tag{1.17}
   \]

   By applying these value bounds at the two endpoints and the interpolation
   point, the corresponding fixed-chord Jensen-budget differences have the same
   orders.  These are not pointwise Hessian bounds.
4. Let a **positive random forward-clock mixture** on a layer mean

   \[
     q_l^\rho=\int_0^\infty u_l e^{tL_l}r_l^{max}\,\rho(dt)                   \tag{1.18}
   \]

   for a probability law `rho`.  For every compact legal `I` and every
   `eta>0`, uniformly for `a in I` and `eta<=r_l/n<=1/2`, all sufficiently
   large even `n` admit no law (1.18) that simultaneously matches the actual degree-one multiplier and the actual
   degree-two/potential multiplier.  This rules out precisely the positive
   random-time BL class (1.18), not general transports or general positive
   corrections.

Theorems 1--2 are the new results of this round.  They show that the old finite
counterexample is a real algebraic obstruction to exact mean-clock transfer,
but only a logarithmic value obstruction in the thermodynamic family.  The
potential clock repairs that exact mode at sublinear entropy-value cost.  It
does not pay the corrected law's Fourier-reference KL curvature or the full
moving-layer transport budget, so the sine target remains open.

## 2. Exact laws, spectral quantities, and all conventions

### 2.1 Actual channel and count law

For `|A|=k`, conditional on `A`, output bits are independent and

\[
 \Pr(Y_i=1\mid A)=a+c1_{\{i\in A\}}.                                        \tag{2.1}
\]

The count probability generating function is

\[
 \sum_l\pi_l(a,c)t^l
 =[1-a-c+(a+c)t]^k[1-a+at]^k.                                                 \tag{2.2}
\]

Every `pi_l` is positive in the legal interior.  Put

\[
 w=a(1-c-a),\qquad z=1+\frac cw.                                             \tag{2.3}
\]

Given `A` and `M=l`, the exact conditional kernel is

\[
 T_{n,l,z}(A,S)=\frac{z^{|A\cap S|}}{Z_{n,l}(z)},\qquad
 Z_{n,l}(z)=\sum_j\binom kj\binom k{l-j}z^j.                                \tag{2.4}
\]

Impossible binomial coefficients are zero.  Since `Z_(n,l)` is independent of
`A`, the actual conditional output law is

\[
 q_l(S)=\sum_{|A|=k}\mu_n(A)T_{n,l,z}(A,S),\qquad |S|=l.                  \tag{2.4a}
\]

The law of `J=|A intersect S|` under (2.4) will be denoted
`P_(n,l,z)`.

### 2.2 Mean-overlap BL surrogate

On the `l`-slice use

\[
 (L_lf)(S)=\frac1{l(n-l)}\sum_{i\in S}\sum_{j\notin S}
 [f(S-i+j)-f(S)].                                                            \tag{2.5}
\]

The total exit rate is one and `u_l` is reversible.  Given `A`, the
maximal-overlap law chooses a uniform `l`-subset of `A` if `l<=k`, and a
uniform `l`-superset of `A` if `l>=k`; average over the Fourier input to obtain
`q_l^max`, and write its `u_l`-density as `r_l^max=dq_l^max/du_l`.

Let

\[
 r_l=\min(l,n-l),\qquad
 m_l=E_{P_{n,l,z}}J,\qquad
 \lambda_{n,l}=\frac{2m_l-l}{r_l}.                                          \tag{2.6}
\]

For nontrivial layers `0<lambda_(n,l)<1`.  The degree-one BL eigenvalue is

\[
 \gamma_{1,l}=\frac n{l(n-l)}.                                               \tag{2.7}
\]

Indeed, for `f_i(S)=1_(i in S)-l/n`, direct summation in (2.5) gives
`L_l f_i=-n f_i/[l(n-l)]`; no external spectral theorem is being imported.

so the recovered mean clock and law are

\[
 \widetilde\tau_l=-\frac{\log\lambda_{n,l}}{\gamma_{1,l}},\qquad
 \widetilde q_l=u_l e^{\widetilde\tau_lL_l}r_l^{max}.                        \tag{2.8}
\]

Finally `\widetilde p_a(S)=\pi_l\widetilde q_l(S)` for `|S|=l`.  These definitions fix the
divergence orientation, rates, clock, initial law, and parameter domain.

### 2.3 Fourier potential is pure Johnson degree two

For `phi_ij=log|zeta_i-zeta_j|^2`, differentiation of `x^n-1` at a root gives

\[
 \sum_{j\ne i}\phi_{ij}=2\log n.                                            \tag{2.9}
\]

Thus on the `l`-slice

\[
 \overline U_{n,l}(S)=U_n(S)-E_{u_l}U_n
 =\sum_{i<j\in S}\left(\phi_{ij}-\frac{2\log n}{n-1}\right)                 \tag{2.10}
\]

has zero row sums and is a pure Johnson degree-two observable.  Directly
summing swaps gives

\[
 L_l\overline U_{n,l}=-\gamma_{2,l}\overline U_{n,l},\qquad
 \gamma_{2,l}=\frac{2(n-1)}{l(n-l)}.                                        \tag{2.11}
\]

Write

\[
 V_n=E_{\mu_n}U_n-E_{u_k}U_n>0,
 \qquad
 \alpha_{n,l}=\frac{r_l(r_l-1)}{k(k-1)}                                    \tag{2.12}
\]

with `alpha=0` when `r_l<2`.  Uniform subsampling/supersampling and complement
symmetry give

\[
 E_{q_l^{max}}\overline U_{n,l}=\alpha_{n,l}V_n.                             \tag{2.13}
\]

For `l<=k`, put `v_l=Var(J)`.  Exchangeability among the two groups gives the
exact identity

\[
 \boxed{
 \theta_{n,l}=\lambda_{n,l}^2+
 \frac{4(n-1)v_l-l(n-l)(1-\lambda_{n,l}^2)}{n l(l-1)}.}                      \tag{2.14}
\]

Equivalently, directly from (2.4),

\[
 \theta_{n,l}=
 \frac{(z-1)^2\sum_j\binom{k-2}j\binom{k-2}{l-2-j}z^j}
 {\alpha_{n,l}Z_{n,l}(z)}.                                                   \tag{2.15}
\]

For `l>k`, use the identical complementary multiplier.  Explicitly, the
palindromic coefficient identity gives
`Z_(n,n-l)(z)=z^(k-l)Z_(n,l)(z)`, so
`2m_(n,n-l)-(n-l)=2m_(n,l)-l`; the same change of index in (2.15) proves
`theta_(n,n-l)=theta_(n,l)`.  The actual and mean-clock potential expectations
are therefore

\[
\begin{aligned}
 E_{q_l}\overline U_{n,l}&=\alpha_{n,l}\theta_{n,l}V_n,\\
 E_{\widetilde q_l}\overline U_{n,l}
 &=\alpha_{n,l}\lambda_{n,l}^{2(n-1)/n}V_n.                                 \tag{2.16}
\end{aligned}
\]

Subtracting, including the actual moving count weights, proves the exact
spectral/harmonic formula

\[
 \boxed{
 \Delta_n(a,c)=V_n A_n(a,c),\quad
 A_n=\sum_l\pi_l\alpha_{n,l}
 \left(\lambda_{n,l}^{2(n-1)/n}-\theta_{n,l}\right).}                       \tag{2.17}
\]

This is the exact all-even-`n` extension needed for the new analysis.  It is not
an extrapolation from the old six/eight-site signs.

The scalar action used in (2.16) does not require an unquoted representation-
theory theorem.  For a symmetric zero-diagonal matrix `psi` with zero row
sums, put `F(S)=sum_(i<j in S)psi_ij`.  Conditional on `A`, pair inclusion
probabilities depend only on whether a pair is inside `A`, outside `A`, or
crossing.  Zero row sums imply that the three corresponding sums of `psi` are
`F(A)`, `F(A^c)=F(A)` at half density, and `-2F(A)`.  Hence every such
quadratic observable is multiplied by one scalar, which is obtained by testing
`(x_i-x_j)(x_r-x_s)`.  This proves the use of (2.14)--(2.16).  For the maximal
overlap map, each input pair survives with probability `alpha_(n,l)`;
complementation handles `l>k`.  Finally `V_n>0`: the family proportional to
`exp(tU_n)` has derivative of its potential mean equal to `Var_t(U_n)>0`, and
`U_n` is nonconstant on every nontrivial half slice.

### 2.4 Reconstructed Fourier-reference identity and source of `-2n log n`

Let `V_l` be the first `l` columns of the unitary cyclic Fourier matrix.  The
Vandermonde formula and Cauchy--Binet give

\[
 \sum_{|S|=l}e^{U_n(S)}=n^l,\qquad
 \nu_{n,l}(S)=n^{-l}e^{U_n(S)}.                                             \tag{2.18}
\]

For `D_l=D(q_l||nu_(n,l))`, with actual conditional law to reference law,

\[
 D_l=-H(q_l)-E_{q_l}U_n+l\log n.                                            \tag{2.19}
\]

Thus

\[
 H(Y)=H(M)+E[M]\log n-EU_n(Y)-D_F,\qquad
 D_F=\sum_l\pi_lD_l.                                                        \tag{2.20}
\]

The root-discriminant identity (2.9) also gives
`sum_(i<j)phi_ij=n log n`.  Since `EX_i=1/2` and, for `i not=j`,

\[
 E(Y_iY_j)=a^2+ac(EX_i+EX_j)+c^2E(X_iX_j),                                  \tag{2.21}
\]

we obtain

\[
 EU_n(Y)=(a^2+ac)n\log n+c^2EU_n(X),\qquad
 \frac{d^2}{da^2}EU_n(Y)=2n\log n.                                         \tag{2.22}
\]

Also `E M=na+ck`, so `(E M log n)''=0`.  Differentiating (2.20) twice proves

\[
 H''=H(M)''-2n\log n-D_F''.                                                 \tag{2.23}
\]

Every moving reference term is

\[
 D_F''=\sum_l[\pi_lD_l''+2\pi_l'D_l'+\pi_l''D_l],                           \tag{2.24}
\]

with

\[
 D_l'=\sum_Sq_l'\log(q_l/\nu_{n,l}),\qquad
 D_l''=\sum_Sq_l''\log(q_l/\nu_{n,l})+\sum_S(q_l')^2/q_l.                  \tag{2.25}
\]

This explicitly preserves the correction requested in the assignment: the
partition term has zero curvature, while the negative potential contributes
exactly `-2n log n`.

### Proof of (2.14)

For distinct `i,r in A` and `j,s outside A`, set
`h=(x_i-x_j)(x_r-x_s)`.  Conditional on `J`,

\[
\begin{aligned}
 E h={}&\frac{E[J(J-1)]+E[(l-J)(l-J-1)]}{k(k-1)}
       -\frac{2E[J(l-J)]}{k^2}.                                              \tag{2.26}
\end{aligned}
\]

The maximal-overlap expectation is `alpha_(n,l)`.  Substitute
`EJ=l(1+lambda)/2` and `EJ^2=v+(EJ)^2` into (2.26), divide by `alpha`, and
simplify.  This gives (2.14).  Formula (2.15) follows by summing the four choices
in `h`; their weights combine to `(z-1)^2`.  QED.

## 3. Exact Fourier amplitude and its asymptotic constant

At half density the cyclic projection kernel satisfies, for `d not=0 mod n`,

\[
 |P_{0d}|^2=
 \begin{cases}
 [n^2\sin^2(\pi d/n)]^{-1},&d\text{ odd},\\
 0,&d\text{ even}.
 \end{cases}                                                               \tag{3.1}
\]

The Fourier-DPP pair inclusion probability is `1/4-|P_(0d)|^2`; the uniform
`k`-subset pair probability is `(n-2)/[4(n-1)]`.  Since every cyclic distance
occurs `n/2` times among unordered pairs,

\[
 V_n=\frac{n\log n}{4(n-1)}-
 \frac1{2n}\sum_{\substack{1\le d<n\\d\ odd}}
 \frac{\log(4\sin^2(\pi d/n))}{\sin^2(\pi d/n)}.                            \tag{3.2}
\]

Use the exact trigonometric identity

\[
 \sum_{d\ odd}\csc^2(\pi d/n)=\frac{n^2}{4},                               \tag{3.3}
\]

obtained by subtracting the even terms from
`sum_(d=1)^(n-1)csc^2(pi d/n)=(n^2-1)/3`.  Then

\[
 V_n=\frac n4\log n-\frac{T_n}{n}+\frac{n\log n}{4(n-1)},\quad
 T_n=\sum_{d\ odd}\csc^2(\pi d/n)\log(2n\sin(\pi d/n)).                    \tag{3.4}
\]

For `1<=d<=n/2`, `sin(pi d/n)>=2d/n` and
`sin(pi d/n)<=pi d/n`.  These inequalities give a summable dominant sequence
for `T_n/n^2`.  Dominated convergence, with the two endpoints paired, yields

\[
 \frac{T_n}{n^2}\longrightarrow
 \kappa:=\frac2{\pi^2}\sum_{m\ odd}\frac{\log(2\pi m)}{m^2}
 =\frac14\log(2\pi)-\frac{\log2}{12}-\frac{3\zeta'(2)}{2\pi^2}.             \tag{3.5}
\]

Therefore

\[
 \boxed{V_n=n\left(\frac14\log n-\kappa+o(1)\right).}                       \tag{3.6}
\]

A completely explicit uniform bound, useful for domination, is

\[
 0\le T_n\le\frac{n^2}{2}
 \sum_{m=1}^\infty\frac{\log(2\pi m)}{m^2},                                 \tag{3.7}
\]

so `V_n=(n/4)log n+O(n)` without invoking the limit in (3.5).

## 4. Uniform overlap saddle point

The only asymptotic input required for the growing layer is the following
one-dimensional lemma.  It is proved here rather than imported from the
unreviewed S5 summary.

### Lemma 4.1 (uniform lattice Laplace expansion)

Fix compact sets `X subset (0,1/2]` and `Z subset (1,infinity)`.  For even `n`,
`l/n=x in X`, and `z in Z`, let `J` have the law (2.4).  Let `p,q` be the unique
numbers in `(0,1)` satisfying

\[
 p+q=2x,\qquad \frac{p(1-q)}{q(1-p)}=z.                                     \tag{4.1}
\]

Write `lambda=(p-q)/(2x)`, so (1.5)--(1.6) hold, and put

\[
 A=p(1-p),\qquad B=q(1-q),\qquad
 \sigma^2(x,z)=\frac{AB}{2(A+B)}.                                           \tag{4.2}
\]

Uniformly on `X times Z`,

\[
 E J=\frac{np}{2}+O(1),\qquad
 Var(J)=n\sigma^2(x,z)+O(1).                                                 \tag{4.3}
\]

Moreover the coefficient sum, its `z`-derivatives, and its forward
`l`-differences have full uniform asymptotic expansions in integer powers of
`1/n`.  In the notation of (5.1), on each one-sided compact up to `x=1/2`
there is a smooth `b_1(x,z)` such that, for `s=0,1,2`,

\[
 \partial_z^s g_{n,l}(z)=\frac{\partial_z^s f(x,z)}n
 +\frac{\partial_z^s b_1(x,z)}{n^2}+O(n^{-3}),                            \tag{4.3a}
\]

and the same expansion may be forward-differenced twice in `l`, term by term.
All remainders are uniform on the stated compact sets.

#### Proof

Put `j=ny` and use the entropy function
`h(s)=-s log s-(1-s)log(1-s)`.  Uniform Stirling expansion gives

\[
 \binom{k}{j}\binom{k}{l-j}z^j
 =\frac{e^{nF_{x,z}(y)}}{\pi n
 \sqrt{p_y(1-p_y)q_y(1-q_y)}}
 \left(1+\sum_{r=1}^R\frac{a_r(x,y)}{n^r}+O(n^{-R-1})\right),                \tag{4.4}
\]

uniformly whenever `y` stays in a compact subinterval of `(0,x)`, where

\[
 F_{x,z}(y)=\tfrac12h(2y)+\tfrac12h(2x-2y)+y\log z,\quad
 p_y=2y,\ q_y=2x-2y.                                                        \tag{4.5}
\]

The stationary equation is exactly (4.1), with maximizer `y_*=p/2`.  Compactness
keeps `p,q,1-p,1-q` uniformly away from zero.  Also

\[
 F''(y_*)=-2\left(A^{-1}+B^{-1}\right)=-\sigma^{-2}.                         \tag{4.6}
\]

Strict concavity gives a uniform quadratic loss outside a fixed neighborhood.
Inside `|j-ny_*|<=n^(3/5)`, Taylor-expand (4.4) and sum the resulting Gaussian
polynomial terms.  Outside that window the total is
`O(exp(-c n^(1/5)))` times the central mass.  Gaussian sum/integral replacement
has exponentially small error after the same truncation.  Repeating to any
fixed order `R` gives

\[
 \log Z_{n,l}(z)=n\mathcal F(x,z)-\tfrac12\log n+
 G_0(x,z)+\sum_{r=1}^R n^{-r}G_r(x,z)+O(n^{-R-1}),                            \tag{4.7}
\]

uniformly, where `mathcal F=F(y_*)`; every displayed coefficient is smooth on
the compact parameter set.  The same proof after replacing `l` by `l+s`, for
fixed integer `s`, is uniform, so scaled forward differences may be taken in
(4.7).  Differentiation in `z` is justified termwise by the same exponential
tail bound.

Now `EJ=z partial_z log Z` and `Var(J)=(z partial_z)^2 log Z`.  The envelope
theorem gives `z partial_z mathcal F=y_*=p/2`; implicit differentiation of
(4.1), or (4.6), gives
`(z partial_z)^2 mathcal F=AB/[2(A+B)]`.  This proves (4.3).  Substitution of the resulting complete moment expansions
into the exact rational formulas (2.14), (2.15), and (5.1), followed by the
Taylor expansion of `lambda^(2-2/n)`, gives (4.3a).  The same exponentially
small tail majorant justifies the two stated `l`-differences and `z`-
derivatives.  QED.

### Lemma 4.2 (the exact multiplier mismatch)

On the compact sets of Lemma 4.1,

\[
 n\left(\lambda_{n,l}^{2(n-1)/n}-\theta_{n,l}\right)
 \longrightarrow d(x,z)                                                     \tag{4.8}
\]

uniformly, with `d` given by (1.7).  The convergence also holds with the scaled
`l`-differences needed in Section 6.

#### Proof

By Lemma 4.1, `lambda_(n,l)->lambda` and `v_l/n->sigma^2`.  Equation (2.14)
gives

\[
 n(\theta_{n,l}-\lambda_{n,l}^2)\longrightarrow
 \frac{4\sigma^2-x(1-x)(1-\lambda^2)}{x^2}.                                 \tag{4.9}
\]

Using `p=x(1+lambda)`, `q=x(1-lambda)` in (4.2), direct simplification gives

\[
 \frac{4\sigma^2-x(1-x)(1-\lambda^2)}{x^2}
 =\frac{\lambda^2(1-\lambda^2)(1-2x)}{1-x(1+\lambda^2)}.                    \tag{4.10}
\]

Also

\[
 n(\lambda_{n,l}^{2-2/n}-\lambda_{n,l}^2)
 \longrightarrow-2\lambda^2\log\lambda.                                   \tag{4.11}
\]

Subtract (4.9) from (4.11).  The uniform difference statement follows from the
last part of Lemma 4.1.  QED.

The sign is strict.  Since `0<x<=1/2` and `0<lambda<1`,

\[
 0\le\frac{1-2x}{1-x(1+\lambda^2)}\le1,\qquad
 1-\lambda^2<-2\log\lambda.                                                 \tag{4.12}
\]

Hence `d(x,z)>0`.

## 5. Proof of Theorem 1: value and integrated response

Let

\[
 g_{n,l}(z)=\alpha_{n,l}
 (\lambda_{n,l}^{2(n-1)/n}-\theta_{n,l}).                                   \tag{5.1}
\]

On a central band with `x=l/n<=1/2`, Lemma 4.2 and
`alpha_(n,l)->4x^2` give

\[
 n g_{n,l}(z)\longrightarrow f(x,z):=4x^2d(x,z),                            \tag{5.2}
\]

uniformly, with the difference control of Lemma 4.1.  Complement symmetry uses
`x=min(l/n,1-l/n)` on the other half.

Under the actual count law, `M` is the sum of `k` Bernoulli variables of
parameter `a+c` and `k` of parameter `a`; hence

\[
 E(M/n)=m(a),\qquad Var(M/n)=O(1/n),                                        \tag{5.3}
\]

uniformly on compact legal sets.  The required exponential tail bound is
self-contained: for every `t`, exponential Markov applied to
`exp(t(M-EM))`, together with
`log E exp(t(B-EB))<=t^2/8` for a Bernoulli `B`, gives
`Pr(|M-EM|>=epsilon n)<=2exp(-2epsilon^2 n)`.  Hence the probability of
leaving a fixed central band is exponentially small.  Since
`|g_(n,l)|<=1` and `f` is uniformly continuous,

\[
 nA_n(a,c)=E[f(x(M),z(a,c))]+o(1)
 \longrightarrow f(x(a),z(a,c))                                            \tag{5.4}
\]

uniformly on every compact legal `I`.  Combine (2.17), (3.6), and (5.4):

\[
 \frac{\Delta_n}{\log n}\longrightarrow\frac14 f=x^2d=C.                   \tag{5.5}
\]

Strict positivity follows from (4.12).  This proves (1.9).

For a fixed chord, apply (1.9) at its three points to obtain (1.10).  At finite
`n`, `Delta_n` is analytic in the legal interior, so the triangular-kernel
identity is exact:

\[
 (1-t)\Delta_n(a_0)+t\Delta_n(a_1)-\Delta_n(a_t)
 =\int_{a_0}^{a_1}K_t(a)\Delta_n''(a)\,da.                                  \tag{5.6}
\]

For compactly supported `phi`, two integrations by parts give
`int phi Delta_n''=int phi'' Delta_n`.  Uniform (1.9) then proves (1.11).
This is where every `pi_l'` and `pi_l''` is retained without differentiating an
uncontrolled value remainder.

For reference, direct differentiation of the exact spectral expression gives
all moving terms explicitly.  With `r_n=2(n-1)/n` and primes in `a`,

\[
\begin{aligned}
 \Delta_n''=V_n\sum_l\{&\pi_l''g_{n,l}
 +2\pi_l'z'g_{n,l,z}\\
 &+\pi_l[(z')^2g_{n,l,zz}+z''g_{n,l,z}]\}.                                  \tag{5.7}
\end{aligned}
\]

No term in (5.7) is deleted.  Section 6 identifies which part dominates at the
midpoint.

## 6. Proof of the midpoint boundary layer

Put `a_*=(1-c)/2`, `N=n/2`, and

\[
 p=\frac{1+c}{2},\quad q=\frac{1-c}{2},\quad
 z_*=\left(\frac{1+c}{1-c}\right)^2.                                        \tag{6.1}
\]

Then `z'(a_*)=0` and `z''(a_*)=32c/(1-c)^4`.  At `x=1/2`, equation (1.5) gives
`lambda=c`.  Implicit differentiation of (1.5) at fixed `z=z_*` gives

\[
 \lambda_x(1/2,z_*)=-2c.                                                     \tag{6.2}
\]

Differentiating `f=4x^2d` and using (6.2) gives the exact edge slope

\[
 \boxed{f_x(1/2,z_*)=8c^2.}                                                  \tag{6.3}
\]

Because `g_(n,l)=g_(n,n-l)`, the scaled difference expansion in Lemma 4.1 gives

\[
\begin{aligned}
 \Delta_l^2 g_{n,l}\big|_{l=N-1}
 &=g_{n,N+1}-2g_{n,N}+g_{n,N-1}
 =-\frac{2f_x(1/2,z_*)}{n^2}+O(n^{-3}),                                     \tag{6.4}\\
 \Delta_l^2 g_{n,l}&=O(n^{-3})\quad(l\ne N-1)                              \tag{6.5}
\end{aligned}
\]

throughout a fixed central band.

We next retain `pi_l''` exactly.  For independent Bernoulli variables whose
parameters all have derivative one, and any function `h(a,m)`, direct product
differentiation gives

\[
\begin{aligned}
 \frac{d^2}{da^2}Eh(a,M)
 ={}&E h_{aa}(a,M)
 +2\sum_iE\Delta h_a(a,M_{-i})\\
 &+2\sum_{i<j}E\Delta^2h(a,M_{-i,-j}).                                     \tag{6.6}
\end{aligned}
\]

At `a_*`, `h(a,l)=g_(n,l)(z(a))` has `h_a=0` and
`h_aa=z''g_z`.  Therefore

\[
 A_n''(a_*)=z''(a_*)E g_z(M,z_*)
 +2\sum_{i<j}E\Delta^2g(M_{-i,-j},z_*).                                    \tag{6.7}
\]

The first term is `O(1/n)` by Lemma 4.1 and count concentration.

For every pair type (two `p` variables, one of each, or two `q` variables),
`M_{-i,-j}` has variance `nv_c+O(1)`, where `v_c=(1-c^2)/4`, and its mean is
`N-1+u sqrt(n)+O(1)` at `a_*+u/sqrt n`.  Fourier inversion of its Bernoulli
characteristic function gives the uniform local limit

\[
 \Pr_{a_*+u/\sqrt n}(M_{-i,-j}=N-1)
 =\frac{e^{-u^2/(2v_c)}}{\sqrt{2\pi n v_c}}+O(n^{-1}).                       \tag{6.8}
\]

For completeness, each factor has modulus squared
`1-4r(1-r)sin^2(t/2)`.  The two Bernoulli parameters stay uniformly away from
zero and one; their linear variance perturbations cancel between the two
half-blocks, leaving total variance `nv_c+O(1)`.  On
`|t|<=n^{-2/5}`, Taylor expansion of the centered logarithmic characteristic
function gives `-nv_ct^2/2+O(t^2+n|t|^3)`; integrating the error against the
Gaussian costs `O(n^{-1})`.  Outside that interval the modulus is bounded by
`exp(-C n t^2)` near zero and by `exp(-C n^(1/5))` farther away.  The phase
offset is `-u sqrt(n)+O(1)`, so Fourier inversion yields (6.8), uniformly for
the three pair types and fixed `u`.

At `u=0`, insert (6.4)--(6.8) into (6.7); for general fixed `u`,
use the full identity (6.6).  Since `2 times binom(n,2)=n(n-1)`, the cusp
contribution is

\[
 \sqrt n A_n''(a_*+u/\sqrt n)
 \longrightarrow
 -\frac{2f_x(1/2,z_*)}{\sqrt{2\pi v_c}}e^{-u^2/(2v_c)}.                      \tag{6.9}
\]

At `a_*+u/sqrt n`, one has `z'=O(n^{-1/2})` and `z-z_*=O(n^{-1})`.
From (4.3a), `g_z=O(n^{-1})`, `Delta_l g_z=O(n^{-2})`, and smooth
`Delta_l^2g=O(n^{-3})`.  Consequently the `E h_aa` term is `O(n^{-1})`, the
single-sum term in (6.6) is `O(n^{-3/2})`, the aggregate smooth part of the
pair sum is `O(n^{-1})`, and count tails are exponentially small.  All are
`o(n^{-1/2})`; only the cusp probability in (6.8) survives after multiplication
by `sqrt n`.  Finally use (3.6) and (6.3):

\[
 \frac{\Delta_n''}{\sqrt n\log n}
 =\frac{V_n}{n\log n}\sqrt n A_n''
 \longrightarrow
 \frac14\left[-\frac{16c^2}{\sqrt{2\pi v_c}}e^{-u^2/(2v_c)}\right],          \tag{6.10}
\]

which is exactly (1.12).

The one-sided derivative of `C=f/4` at the midpoint is `+2c^2` from the left and
`-2c^2` from the right.  Hence the derivative jump is `-4c^2`, agreeing with
the integral of the Gaussian in (1.12).  This checks the order of limits:
pointwise curvature first sees a `sqrt(n) log n` spike, while every fixed
integrated Jensen response sees only its `log n` mass.

## 7. Positive potential-clock correction

### 7.1 Positivity of the clock

It remains to prove `0<theta<1` without assuming the old finite checks.  Take
`l<=k` and put `y=z-1>0`.  Vandermonde convolution after marking selected
members of `A` gives

\[
 Z_{n,l}(1+y)=\sum_{r=0}^l\binom kr\binom{2k-r}{l-r}y^r.                    \tag{7.1}
\]

Similarly, if `B_l` denotes the numerator sum in (2.15),

\[
 y^2B_l(1+y)=\sum_{r=2}^l
 \binom{k-2}{r-2}\binom{2k-r-2}{l-r}y^r.                                   \tag{7.2}
\]

For `2<=r<=l`, the ratio of the coefficient in (7.2) to that in (7.1) is

\[
 \frac{r(r-1)(2k-l)(2k-l-1)}{k(k-1)(2k-r)(2k-r-1)}.                         \tag{7.3}
\]

The factor `r(r-1)/[(2k-r)(2k-r-1)]` is increasing in `r`.  Consequently every
coefficient of `alpha_(n,l)Z-y^2B` is nonnegative, the top coefficient is zero,
and the coefficients of degrees zero and one are strictly positive.  Thus

\[
 0<(z-1)^2B_l(z)<\alpha_{n,l}Z_{n,l}(z),                                    \tag{7.4}
\]

proving `0<theta<1`.  Complementation handles `l>k`.

The semigroup `e^(tL_l)` is stochastic and irreducible.  Therefore (1.14) is
normalized and strictly positive for `t>0` (with the harmless endpoint-layer
convention already stated).

### 7.2 Exact mode matching

By (2.11)--(2.13),

\[
 E_{\widehat q_l}\overline U_{n,l}
 =e^{-\gamma_{2,l}\widehat\tau_l}\alpha_{n,l}V_n
 =\theta_{n,l}\alpha_{n,l}V_n
 =E_{q_l}\overline U_{n,l}.                                                 \tag{7.5}
\]

Uniform layer means are common, proving (1.15).  Since the count law is also
common, the aggregate potential defect is exactly zero.

The entropy/reference identities now read

\[
\begin{aligned}
 H''&=H(M)''-2n\log n-D_F'',\\
 \widetilde H''&=H(M)''-2n\log n-\Delta_n''-\widetilde D_F'',\\
 \widehat H''&=H(M)''-2n\log n-\widehat D_F''.                              \tag{7.6}
\end{aligned}
\]

Here every Fourier-reference divergence has orientation conditional law to
`nu_(n,l)=n^(-l)e^(U_n)`, and each aggregate second derivative contains
`pi_l D_l''+2pi_l'D_l'+pi_l''D_l`.  Equation (7.6) removes only the exact
potential-transfer defect.  It does not sign or discard any KL, Fisher,
acceleration, or moving-weight term.

### 7.3 Clock distance and entropy budget

Let

\[
 \delta\tau_{n,l}=\widehat\tau_l-\widetilde\tau_l
 =\frac1{\gamma_{2,l}}
 \log\frac{\lambda_{n,l}^{2(n-1)/n}}{\theta_{n,l}}.                         \tag{7.7}
\]

On every central compact, Lemma 4.2 gives

\[
 \delta\tau_{n,l}\longrightarrow
 T(x,z):=\frac{x(1-x)}{2\lambda^2}d(x,z)>0.                                 \tag{7.8}
\]

A crude global estimate makes the tail step explicit.  On a fixed compact
`z in [z_0,z_1] subset (1,infinity)`, for `2<=l<=k`, the exact degree-one
coefficient identity is

\[
 \lambda_{n,l}=\frac{(z-1)A_{n,l}(z)}{\beta_{n,l}Z_{n,l}(z)},\qquad
 A_{n,l}(z)=\sum_j\binom{k-1}j\binom{k-1}{l-1-j}z^j,\quad
 \beta_{n,l}=l/k.                                                         \tag{7.9a}
\]

Both `A_(n,l)` and the degree-two numerator `B_l` in (2.15) contain a positive
coefficient at least one.  Since `Z_(n,l)(z)<=2^n z_1^n` and
`alpha_(n,l),beta_(n,l)<=1`, there is a compact-dependent `C_I` with

\[
 -\log\lambda_{n,l}\le C_I n,\qquad
 -\log\theta_{n,l}\le C_I n.                                           \tag{7.9b}
\]

Also `gamma_1^(-1)<=n/4` and `gamma_2^(-1)<=n^2/[8(n-1)]`.  Thus both clocks
are `O_I(n^2)` on every layer.  Outside a fixed central count band, Hoeffding's
bound is `exp(-c_I n)`, so its contribution to the count-weighted clock
distance is negligible.  Therefore, uniformly on compact legal `I`,

\[
 \sum_l\pi_l|\delta\tau_{n,l}|=T(x(a),z(a,c))+o(1).                          \tag{7.9}
\]

Couple the two heat laws on each layer by running the same BL chain and adding
`|delta tau|` units of time to the earlier endpoint.  The chain has total jump
rate one and each swap changes Hamming distance by at most two, so

\[
 E d_H(\widetilde Y,\widehat Y)
 \le2\sum_l\pi_l|\delta\tau_{n,l}|=O_I(1).                                  \tag{7.10}
\]

For any coupling of binary vectors with `E d_H<=D`,

\[
 |H(X)-H(Y)|\le n b(\min\{D/n,1/2\}).                                       \tag{7.11}
\]

Indeed, with `E_i=1_(X_i not=Y_i)`,
`H(X|Y)<=H(E)<=sum_i b(Pr(E_i=1))<=n b(D/n)`, and symmetrically.  Equations
(7.9)--(7.11) prove (1.16), with leading upper bound
`n b((2T+o(1))/n)=O(log n)`.

For (1.17), condition on `A,l`.  Couple the actual overlap `J` and the potential-
clock overlap `Jhat`; then use common random orderings inside `A` and `A^c`.
The resulting sets have Hamming distance `2|J-Jhat|`.  Lemma 4.1 gives
`Var(J)=O_I(n)`.  For the BL chain, the centered overlap is a degree-one
eigenfunction `g`, and

\[
 \frac d{dt}E g(X_t)^2=-2\gamma_1E g(X_t)^2+2E\Gamma(g),\qquad
 \Gamma(g)\le\frac12.                                                       \tag{7.12}
\]

Hence

\[
 Var(\widehat J)\le\frac{1-e^{-2\gamma_1\widehat\tau}}{2\gamma_1}
 \le\frac1{2\gamma_1}\le\frac n8.                                         \tag{7.13}
\]

The mean difference is `O_I(1)` because
`lambda-theta^(n/[2(n-1)])=O_I(1/n)` by Lemma 4.2.  Therefore
`E|J-Jhat|=O_I(sqrt n)`.  Count tails are exponentially small, and (7.11)
proves (1.17).

### 7.4 No positive random clock can match both live modes

For (1.18), set `X=e^(-gamma_(1,l)T) in [0,1]` and
`r=gamma_2/gamma_1=2(n-1)/n>1`.  Its degree-one and degree-two multipliers are
`E X` and `E X^r`.  If the first equals the actual `lambda_(n,l)`, Jensen's
inequality gives

\[
 E X^r\ge(E X)^r=\lambda_{n,l}^{2(n-1)/n}.                                  \tag{7.14}
\]

Lemma 4.2 and `d>0` imply, uniformly for `a` in a compact legal interval and
`eta<=r_l/n<=1/2`, that for all large even `n`,

\[
 \theta_{n,l}<\lambda_{n,l}^{2(n-1)/n}.                                     \tag{7.15}
\]

Thus (7.14) cannot equal the actual degree-two multiplier.  This proves the
precise no-go statement in Theorem 2.  The deterministic potential clock
chooses to match degree two exactly and under-matches degree one by `O(1/n)`;
it is not claimed to match all harmonics.

## 8. What this pays and what remains unpaid

The new results determine the size and the curvatural effect of the failed
transfer on a genuine growing contiguous-Fourier family:

- exact defect value: `Delta_n=C log n+o(log n)`;
- fixed integrated Jensen response: `O(log n)=o(n)`;
- midpoint pointwise response: a negative `sqrt(n) log n` boundary layer, still
  `o(n)` after normalization;
- exact positive potential-mode repair: zero potential defect;
- repair cost relative to the mean-clock law: `O(log n)` in entropy value;
- direct actual-to-repair entropy-value cost: `O(sqrt(n) log n)` on fixed
  compact interiors.

None of the entropy-value bounds (1.16)--(1.17) is differentiated.  The
weak-curvature statement (1.11) instead comes from exact finite-`n` integration
by parts and uniform value asymptotics.  The remaining target-level obligation
is to control the corrected surrogate's complete Fourier-reference
KL/moving-layer Jensen budget.  In (7.6), `Dhat_F''` still
contains conditional acceleration/cross-entropy, conditional Fisher,
`2pi_l'Dhat_l'`, and `pi_l''Dhat_l`.  Rewriting it as the desired entropy sign
would be tautological.  No claim is made that all transport methods fail.
