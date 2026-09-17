PROVED_SCOPED_LEMMA

# S6 round 4: an explicit high-contrast curvature band and real-q control with correlated block references

## 0. Status and exact contribution

The full sine entropy-rate concavity target for every fixed `37/40<c<1`, every
`0<rho<1`, and the entire legal `a` interval is **not** proved or disproved.
This package proves two new scoped results.

1. **A genuine high-contrast sign theorem, uniform in dimension and in the input
   contraction.**  Put
   
   \[
   c_0=\frac{37}{40},\qquad c_1=\frac{37}{40}+10^{-13}.
   \]
   
   For every finite Hermitian contraction `0<=Q<=I`, every `c_0<=c<=c_1`, and
   every
   
   \[
   \left|a-\frac{1-c}{2}\right|\le \frac1{200},
   \]
   
   the actual full-configuration entropy satisfies
   
   \[
   \boxed{\quad \frac1n\frac{\partial^2}{\partial a^2}
   H(\operatorname{DPP}(aI+cQ))\le-\frac1{200}.\quad}                 \tag{0.1}
   \]
   
   The interval has fixed length `1/100`, independent of `n` and `Q`; the
   contrast interval has fixed positive width `10^(-13)`.  In particular, for
   every fixed `rho` and every `c` in this high-contrast band, the true sine
   entropy rate is strongly concave on that centered strip, with Jensen bonus
   `t(1-t)(a_1-a_0)^2/400`.

2. **A positive real-q correlated-reference approximation retaining spatial
   dependence.**  On any fixed spectral strip `delta I<=K<= (1-delta)I`, the
   exact information content of a DPP is uniformly subgaussian on scale `n`.
   For the product `w_(a,n,R)` of the true consecutive `R`-site marginals, define
   
   \[
   B_{n,R}(q,a)=q\log\sum_S p_{a,n}(S)
   w_{a,n,R}(S)^{(q-1)/q}
   \]
   
   and, for `q!=1`,
   
   \[
   E_{n,R}(q,a)=\frac{\log Z_n(q,a)-B_{n,R}(q,a)}{q-1},
   \qquad E_{n,R}(1,a)=D(p_{a,n}\|w_{a,n,R}).
   \]
   
   With `Lambda_delta=log((1-delta)/delta)`, for the true Toeplitz law, `R|n`,
   `a in [delta,1-c-delta]`, and `1/2<=q<=3/2`,
   
   \[
   \boxed{\quad
   0\le \frac{E_{n,R}(q,a)}n
   \le \frac{c}{R}\operatorname{Tr}b(Q_R)
        +2880\Lambda_\delta^2|q-1|.\quad}                            \tag{0.2}
   \]
   
   This is a proved open-real-q estimate, not an integer-replica continuation.
   It yields the same right side as a uniform bound on the absolute signed
   Jensen defect of `E_(n,R)/n`.  Thus the exact correlated Hölder remainder has
   vanishing Jensen error when first (or jointly) `R->infinity` and `q->1`,
   uniformly in all multiples `n` of `R`.

The first theorem advances the target on a nonempty all-density high-contrast
region.  The second advances the latest local result from control only at the
`q=1` derivative to a uniform interval of real `q` around one.  Neither result
uses a spectral/von Neumann entropy as a substitute for measured configuration
entropy.

**Analytical proof:** all universally quantified statements in Sections 1--8.

**Exact certificate:** `evidence/certificates/high_contrast_constants.json` is
produced by rational arithmetic and certifies the numerical constants in (0.1).
`evidence/certificates/finite_coupled_check.json` exactly checks the atom law,
L-ensemble law, and the information/log-likelihood flip bounds in a coupled
three-site example.

**Floating diagnostic only:** the noninteger-q grid in the latter certificate.
It is not used in any proof.

## 1. Imported inputs and frozen target

The target, definitions, and reviewed inputs are those in the public packet at
commit

`c307fe1bcf46b56e4755655c90f60a681979bf13`.

Only the following reviewed mathematical inputs are used.

* For every finite Hermitian contraction `Q` and every `0<=d<=37/40`,
  
  \[
  \frac{d^2}{da^2}H(\operatorname{DPP}(aI+dQ))\le-\frac n{50}
                                                                    \tag{1.1}
  \]
  
  in the legal interior.
* For the true Toeplitz blocks, the rate exists and
  
  \[
  0\le \frac{H_n(a,c)}n-h_\rho(a,c)
  \le e_n(c):=\frac c n\operatorname{Tr}b(Q_n),                    \tag{1.2}
  \]
  
  with `Tr b(Q_n)=O_rho((log n)^2)`.
* The exact channel identity: an input DPP with kernel `Q`, followed independently
  at each site by success probability `a+cX_i`, gives
  `DPP(aI+cQ)`.

The full atom, rather than an inclusion probability or a spectral entropy, is
always

\[
p_K(S)=\sum_{B\subseteq[n]\setminus S}(-1)^{|B|}\det K_{S\cup B},
\qquad H(K)=-\sum_Sp_K(S)\log p_K(S).                               \tag{1.3}
\]

The bounded-degree expansion in the preceding local package was not part of the
reviewed public baseline.  It is therefore re-established in Sections 2--3
before being used.  Its re-proof is a dependency, not this round's claimed new
advance.

## 2. Re-established full-atom expansion

Fix `0<delta<1/2`, a finite Hermitian contraction `Q`, and an amplitude `0<d<1`.
On an interval `J` on which

\[
\delta I\le K(x):=xI+dQ\le(1-\delta)I,                              \tag{2.1}
\]

write `p_x` for the complete DPP law and `f_(Q,d,n)(x)=H(K(x))/n`.

### Lemma 2.1: the configuration-dependent Hermitian pencil

For a configuration `S`, put

\[
A_S(x)=K(x)-D_{S^c},                                                \tag{2.2}
\]

where `D_(S^c)` is the diagonal projection onto the empty sites.  Diagonal
multilinearity gives

\[
(-1)^{n-|S|}\det A_S(x)
 =\sum_{B\subseteq S^c}(-1)^{|B|}\det K(x)_{S\cup B}=p_x(S).        \tag{2.3}
\]

Let `m=n-|S|`.  From (2.1),

\[
\delta I-D_{S^c}\le A_S(x)\le(1-\delta)I-D_{S^c}.                  \tag{2.4}
\]

The upper comparison matrix has its first `m` ordered eigenvalues equal to
`-delta`; the lower comparison matrix has its remaining `n-m` eigenvalues equal
to `delta`.  Eigenvalue monotonicity therefore gives exactly `m` eigenvalues of
`A_S` in `[-1+delta,-delta]` and `n-m` in `[delta,1-delta]`.  Hence

\[
p_x(S)=|\det A_S(x)|>0,
\qquad \delta^2I\le A_S(x)^2\le(1-\delta)^2I.                     \tag{2.5}
\]

Consequently the measured entropy has the exact full-configuration form

\[
f_{Q,d,n}(x)
=-\frac1{2n}\mathbb E_{p_x}\operatorname{Tr}\log A_S(x)^2.         \tag{2.6}
\]

The matrix inside the expectation depends on the actual spatial configuration;
(2.6) is not `Tr b(K)`.

### Lemma 2.2: averaging does not create dimension-dependent degree

If `F(x,y_1,...,y_n)` is a polynomial of total degree at most `D`, reduce it on
the Boolean cube to a sum of monomials
`x^j product_(i in V)y_i` with `j+|V|<=D`.  The DPP inclusion identity gives

\[
\mathbb E_{p_x}\prod_{i\in V}Y_i=\det(xI+dQ)_V,                   \tag{2.7}
\]

which has degree at most `|V|` in `x`.  Thus

\[
\deg_x\mathbb E_{p_x}F(x,Y)\le D.                                 \tag{2.8}
\]

All nonproduct spatial determinants remain in (2.7); no independence is imposed.

### Lemma 2.3: Chebyshev series with dimension-free coefficients

Set

\[
r=\frac{1-\delta}{1+\delta},\quad
X_S=\frac{2A_S^2-(1+\delta^2)I}{1-\delta^2},\quad
C_\delta=\log\frac2{1+\delta}.                                    \tag{2.9}
\]

The spectrum of `X_S` lies in `[-1,1]`.  If `T_m` is the Chebyshev polynomial,
the scalar identity

\[
-\frac12\log u=C_\delta+
\sum_{m\ge1}\frac{(-1)^m r^m}{m}
T_m\!\left(\frac{2u-(1+\delta^2)}{1-\delta^2}\right)              \tag{2.10}
\]

holds absolutely for `delta^2<=u<=1`.  It follows by writing
`u=((1+delta)^2/4)(1+2r cos(theta)+r^2)` and expanding the two logarithms
`log(1+r exp(+-i theta))`.

Functional calculus, (2.6), and Lemma 2.2 give

\[
f_{Q,d,n}(x)=C_\delta+\sum_{m\ge1}u_{Q,d,n,m}(x),                 \tag{2.11}
\]

\[
u_{Q,d,n,m}(x)=\frac{(-1)^m r^m}{mn}
\mathbb E_{p_x}\operatorname{Tr}T_m(X_S(x)),                      \tag{2.12}
\]

with the dimension-free bounds

\[
\boxed{
\deg_x u_{Q,d,n,m}\le2m,
\qquad \|u_{Q,d,n,m}\|_{C(J)}\le\frac{r^m}{m}.}                  \tag{2.13}
\]

The expectation in (2.12) moves with `x`; Lemma 2.2 is precisely what includes
all derivatives of that moving law while controlling its degree.

## 3. New response estimate on a nested interval

The previous local package used a whole-interval Markov inequality, costing four
powers of the truncation degree.  The following interior estimate costs two and
is the first new connecting step of this round.

### Lemma 3.1: interior Bernstein bound

Let `P` be a polynomial of degree at most `D` on an interval `I` of length
`ell`.  Let `I'` be the concentric subinterval whose endpoints are a distance
`mu` from the respective endpoints of `I`, where `0<mu<ell/2`, and set

\[
\sigma=\frac{2\sqrt{\mu(\ell-\mu)}}\ell.                           \tag{3.1}
\]

Then

\[
\boxed{
\|P''\|_{C(I')}\le\frac4{\ell^2}
\left(\frac{D^2}{\sigma^2}+\frac D{\sigma^3}\right)
\|P\|_{C(I)}.}                                                     \tag{3.2}
\]

**Proof.**  Write `x=x_0+(ell/2)cos theta` and
`T(theta)=P(x)`.  This is a trigonometric polynomial of degree at most `D`.
Bernstein's trigonometric inequality gives
`||T'||_infty<=D||T||_infty`; applying it to `T'` gives
`||T''||_infty<=D^2||T||_infty`.  On `I'`, `|sin theta|>=sigma`, and

\[
P''(x)=\frac{T''(\theta)}{(\ell/2)^2\sin^2\theta}
       -\frac{\cos\theta\,T'(\theta)}{(\ell/2)^2\sin^3\theta}.
\]

Taking absolute values proves (3.2).  The imported inequality is exactly
Queffelec--Zarouf, Theorem 1.1; its hypotheses match because `T` is a
trigonometric polynomial of degree at most `D`.  QED.

### Lemma 3.2: value-to-curvature response in the full-atom class

Suppose on `I` that

\[
g(x)=\sum_{m\ge1}v_m(x),\qquad
\deg v_m\le2m,\qquad \|v_m\|_{C(I)}\le A\frac{r^m}{m},             \tag{3.3}
\]

and `||g||_(C(I))<=epsilon`.  For an integer `M>=1`, define

\[
V_M=\frac{r^{M+1}}{(M+1)(1-r)},\quad
S_{0,M}=\frac{r^{M+1}}{1-r},                                      \tag{3.4}
\]

\[
S_{1,M}=\frac{r^{M+1}((M+1)-Mr)}{(1-r)^2}.                         \tag{3.5}
\]

Then on the concentric inner interval of Lemma 3.1,

\[
\begin{split}
\|g''\|_{C(I')}
\le{}&\left[\frac{16M^2}{\ell^2\sigma^2}
            +\frac{8M}{\ell^2\sigma^3}\right]
       (\epsilon+A V_M)\\
&+A\left[\frac{16S_{1,M}}{\ell^2\sigma^2}
         +\frac{8S_{0,M}}{\ell^2\sigma^3}\right].                \tag{3.6}
\end{split}
\]

**Proof.**  The partial sum through `M` has degree at most `2M` and norm at most
`epsilon+A V_M`.  Apply (3.2).  Apply (3.2) separately to every tail term and
sum, using `sum_(m>M)r^m=S_(0,M)` and
`sum_(m>M)m r^m=S_(1,M)`.  The derivative series converges uniformly on `I'`,
so termwise differentiation is justified.  QED.

For a difference of two normalized DPP entropies satisfying the same gap,
Lemma 2.3 gives (3.3) with `A=2`.

## 4. Proof of the explicit high-contrast theorem

Let

\[
c_0=\frac{37}{40},\quad c_1=c_0+10^{-13},\quad
\delta_0=\frac9{500},\quad w=\frac1{200}.                          \tag{4.1}
\]

Fix `c in [c_0,c_1]`, `n`, and a Hermitian contraction `Q`.  Put
`qbar=Tr(Q)/n`.

If `qbar<=1/2`, set `Q_*=Q` and `x=a`.  If `qbar>1/2`, set
`Q_*=I-Q` and `x=1-a-c`.  The complement of `DPP(K)` is `DPP(I-K)`: indeed its
inclusion probabilities follow from the void identity

\[
\Pr(X\cap A=\varnothing)=\sum_{B\subseteq A}(-1)^{|B|}\det K_B
=\det(I-K_A).                                                      \tag{4.2}
\]

Therefore in both cases

\[
H(\operatorname{DPP}(aI+cQ))
=H(\operatorname{DPP}(xI+cQ_*)),\qquad
\frac1n\operatorname{Tr}Q_*\le\frac12,                            \tag{4.3}
\]

and the second `a` derivative equals the second `x` derivative.  The centered
strip is invariant under `a -> 1-a-c`.

Define

\[
F_d(x)=\frac1nH(\operatorname{DPP}(xI+dQ_*)),\qquad d\in\{c,c_0\}.
\]

Use the common outer interval

\[
I_c=[\delta_0,1-c-\delta_0]                                      \tag{4.4}
\]

and its concentric inner interval

\[
I'_c=\left[\frac{1-c}{2}-w,\frac{1-c}{2}+w\right].                \tag{4.5}
\]

Both `xI+cQ_*` and `xI+c_0Q_*` have spectra in
`[delta_0,1-delta_0]` on `I_c`, so Lemma 2.3 applies to both.

### 4.1 Exact value coupling in contrast

Generate one input `X~DPP(Q_*)` and use common independent uniforms at every
site for the channels with amplitudes `c` and `c_0`.  The two outputs differ at
site `i` with probability `(c-c_0)(Q_*)_(ii)`.  If `D_i` is the binary mismatch,
then one output is determined by the other and `D`.  Hence

\[
|H(Y_c)-H(Y_{c_0})|
\le\max\{H(Y_c|Y_{c_0}),H(Y_{c_0}|Y_c)\}
\le\sum_i b(\Pr(D_i=1)).                                         \tag{4.6}
\]

Concavity of `b` and `Tr(Q_*)/n<=1/2` give

\[
\|F_c-F_{c_0}\|_{C(I_c)}
\le b\left(\frac{c-c_0}{2}\right)\le 2\cdot10^{-12}.             \tag{4.7}
\]

For the last inequality, `y<=(c_1-c_0)/2=5*10^(-14)` and

\[
b(y)\le y(1-\log y).
\]

At the upper endpoint,
`1-log y=1+log 2+13 log 10<1+1+13*(5/2)=69/2`; therefore
`b(y)<1.725*10^(-12)<2*10^(-12)`.  The elementary inequalities
`log 2<1` and `log 10<5/2` follow respectively from `e>2` and from the first
five Taylor terms of `exp(5/2)`, whose sum already exceeds ten.

### 4.2 Exact response constants

The outer length obeys

\[
\ell=1-c-2\delta_0\ge\frac{39}{1000}-10^{-13}
>\frac{389}{10000}.                                                \tag{4.8}
\]

For the centered inner interval,

\[
\sigma^2=1-\left(\frac{2w}{\ell}\right)^2
>1-\left(\frac{100}{389}\right)^2
>\left(\frac{24}{25}\right)^2.                                   \tag{4.9}
\]

The final strict inequality is the integer comparison
`141321*625-151321*576=1164729>0`.

Apply Lemma 3.2 to `g=F_c-F_(c_0)` with

\[
r=\frac{1-\delta_0}{1+\delta_0}=\frac{491}{509},\quad
A=2,\quad M=768,\quad \epsilon=\frac1{500000000000}.              \tag{4.10}
\]

Replacing `ell` and `sigma` by the lower bounds in (4.8)--(4.9), the right side
of (3.6) is the exact rational number recorded in the certificate, with outward
interval

\[
0.014503101814653298
\le \mathcal R
\le0.014503101814653299<\frac3{200}.                               \tag{4.11}
\]

No floating arithmetic is used for the comparison with `3/200`.

The reviewed low-contrast theorem (1.1) gives `F_(c_0)''<=-1/50`.  Therefore,
throughout `I'_c`,

\[
F_c''\le F_{c_0}''+|F_c''-F_{c_0}''|
\le-\frac1{50}+\frac3{200}=-\frac1{200}.                          \tag{4.12}
\]

Using (4.3) proves (0.1).

### 4.3 Consequence for the sine entropy rate

For fixed `rho`, fixed `c in [c_0,c_1]`, `a_0,a_1 in I'_c`, and `0<=t<=1`,
finite-dimensional integration of (0.1) gives

\[
\frac{H_n(a_t,c)}n\ge(1-t)\frac{H_n(a_0,c)}n
+t\frac{H_n(a_1,c)}n
+\frac1{400}t(1-t)(a_1-a_0)^2,                                   \tag{4.13}
\]

where `a_t=(1-t)a_0+ta_1`.  Taking `n->infinity` using the supplied value
convergence (1.2), without differentiating the limit, yields

\[
\boxed{
h_\rho(a_t,c)\ge(1-t)h_\rho(a_0,c)+t h_\rho(a_1,c)
+\frac1{400}t(1-t)(a_1-a_0)^2.}                                  \tag{4.14}
\]

## 5. Strong-Rayleigh concentration of full atom information

This section proves the second new result.  Let `K` satisfy

\[
\delta I\le K\le(1-\delta)I,
\qquad 0<\delta<\frac12,                                          \tag{5.1}
\]

and let `p=DPP(K)` on `n` labelled sites.  Put

\[
\Lambda_\delta=\log\frac{1-\delta}{\delta}.                       \tag{5.2}
\]

### Lemma 5.1: exact Hamming Lipschitz bound for `-log p`

The L-ensemble matrix `L=K(I-K)^(-1)` has spectrum in

\[
\left[\frac\delta{1-\delta},\frac{1-\delta}{\delta}\right].       \tag{5.3}
\]

For `i notin S`, the atom ratio is the Schur complement

\[
\frac{p(S\cup\{i\})}{p(S)}
=\frac{\det L_{S\cup\{i\}}}{\det L_S}.                            \tag{5.4}
\]

A principal submatrix of `L` obeys the same operator bounds.  The reciprocal of
the relevant diagonal entry of its inverse, hence the Schur complement in
(5.4), lies in the interval (5.3).  Therefore

\[
|\log p(S\cup\{i\})-\log p(S)|\le\Lambda_\delta.                 \tag{5.5}
\]

Thus both `log p` and the information content `-log p` are
`Lambda_delta`-Lipschitz in Hamming distance.

### Lemma 5.2: the law is strong Rayleigh

The multiaffine generating polynomial is

\[
G(z_1,\ldots,z_n)=\frac{\det(I+LZ)}{\det(I+L)},
\qquad Z=\operatorname{diag}(z_1,\ldots,z_n).                     \tag{5.6}
\]

If all `Im z_i>0` and `det(I+LZ)=0`, a nonzero vector `v` would satisfy
`(L^(-1)+Z)v=0`.  Taking the imaginary part of
`v^*(L^(-1)+Z)v` gives `sum_i Im(z_i)|v_i|^2>0`, a contradiction.
Hence `G` is real stable and `p` is strong Rayleigh in the definition used by
Pemantle--Peres.

### Lemma 5.3: a dimension-linear moment-generating-function bound

Pemantle--Peres, Theorem 3.2, states that for a strong Rayleigh law and a
Hamming-1-Lipschitz function `F`, with `mu=E|S|`,

\[
\Pr(|F-EF|>u)\le5\exp\left[-\frac{u^2}{16(u+2\mu)}\right],         \tag{5.7}
\]

and its stated remark permits the denominator to be replaced by `48n`.
Scaling gives, for an `L_F`-Lipschitz function,

\[
\Pr(|F-EF|>u)\le5\exp\left[-\frac{u^2}{48nL_F^2}\right].          \tag{5.8}
\]

For `u>nL_F` the left side is zero, so (5.8) holds for every `u>=0`.

Let `X=F-EF` and `v=48nL_F^2`.  Integrating (5.8),

\[
E|X|^{2k}\le5k!v^k.                                                \tag{5.9}
\]

For an independent copy `X'`,
`E exp(sX)<=E exp(s(X-X'))` because `E exp(-sX)>=1`.  The difference is
symmetric and

\[
E|X-X'|^{2k}\le5\,4^k k!v^k.                                     \tag{5.10}
\]

Since `(2k)!>=(k!)^2`,

\[
E e^{s(X-X')}
\le1+5(e^{4vs^2}-1)\le e^{20vs^2}.                               \tag{5.11}
\]

The last inequality follows from `5y-4<=y^5` for `y>=1`.  Therefore

\[
\boxed{
0\le\log E\exp(s(F-EF))\le960nL_F^2s^2,
\qquad s\in\mathbb R.}                                            \tag{5.12}
\]

The lower bound is Jensen's inequality on an ordinary positive probability
space.

## 6. Exact correlated-reference remainder and every moving-reference derivative

Partition the sites into disjoint consecutive blocks and let `w_a` be the
product of the **true block marginals**.  Every block marginal is a DPP with a
principal submatrix of `K(a)`, so it obeys the same spectral strip.  Flipping one
site changes exactly one block factor.  Lemma 5.1 gives

\[
\operatorname{Lip}(\log p_a)\le\Lambda_\delta,
\qquad \operatorname{Lip}(\log w_a)\le\Lambda_\delta.             \tag{6.1}
\]

For `q>0`, put `t=q-1`, `s=t/q`,

\[
Z(q,a)=\sum_Sp_a(S)^q,
\quad B(q,a;w_a)=q\log\sum_Sp_a(S)w_a(S)^s,                        \tag{6.2}
\]

and `pi_(q,a)(S)=p_a(S)^q/Z(q,a)`.  Direct substitution gives the exact positive
relative-entropy remainder

\[
\boxed{
\log Z(q,a)-B(q,a;w_a)
=(q-1)D_{1/q}(\pi_{q,a}\|w_a).}                                   \tag{6.3}
\]

No integer replicas or analytic-continuation choice occurs.  In particular

\[
E(q,a):=\frac{\log Z-B}{q-1}=D_{1/q}(\pi_{q,a}\|w_a)\ge0          \tag{6.4}
\]

for `q!=1`, and its continuous value at one is

\[
E(1,a)=D(p_a\|w_a).                                                \tag{6.5}
\]

For completeness, all `a` derivatives of the moving reference are as follows.
Let

\[
u=\log p_a,\quad v=\log w_a,\quad
\sigma=u_a,\quad\kappa=u_{aa},\quad
\theta=v_a,\quad\zeta=v_{aa},                                    \tag{6.6}
\]

and let

\[
\eta_{q,a}(S)=
\frac{p_a(S)w_a(S)^s}{\sum_Tp_a(T)w_a(T)^s}.                       \tag{6.7}
\]

Then, at every finite `n`,

\[
\partial_a\log Z=qE_\pi\sigma,
\qquad
\partial_a^2\log Z=qE_\pi\kappa+q^2\operatorname{Var}_\pi(\sigma),\tag{6.8}
\]

\[
\partial_a B=qE_\eta(\sigma+s\theta),                             \tag{6.9}
\]

\[
\partial_a^2B=qE_\eta(\kappa+s\zeta)
+q\operatorname{Var}_\eta(\sigma+s\theta).                       \tag{6.10}
\]

Thus the exact remainder curvature is the difference of (6.8) and (6.10); no
reference score, acceleration, covariance, or escort motion is omitted.  At
`q=1`, differentiating (6.5), and using the normalization identity
`E_p(kappa+sigma^2)=0`, gives

\[
D''=E_p\left[(\kappa+\sigma^2)(u-v)
+\sigma^2-2\sigma\theta-\zeta\right].                             \tag{6.11}
\]

For the disjoint-block reference, `v`, `theta`, and `zeta` are the sums of the
true block log probabilities, scores, and accelerations respectively.

## 7. New open-real-q estimate

Let

\[
A(S)=\log p_a(S),\qquad C(S)=\log w_a(S),
\]

and write

\[
\psi_F(z)=\log E_{p_a}\exp(z(F-E_{p_a}F)).                         \tag{7.1}
\]

Equations (6.1) and (5.12) give

\[
0\le\psi_A(z),\psi_C(z)\le960n\Lambda_\delta^2z^2.               \tag{7.2}
\]

Expanding the two exact positive sums in (6.2),

\[
\log Z=tE A+\psi_A(t),
\qquad
B=tE C+q\psi_C(t/q).                                               \tag{7.3}
\]

Since `D(p||w)=E(A-C)`, (7.3) yields

\[
E(q,a)-D(p_a\|w_a)
=\frac{\psi_A(t)-q\psi_C(t/q)}t.                                  \tag{7.4}
\]

For `1/2<=q<=3/2`,

\[
\boxed{
|E(q,a)-D(p_a\|w_a)|
\le2880n\Lambda_\delta^2|q-1|.}                                  \tag{7.5}
\]

This is uniform in dimension and on the entire declared spectral strip.  As a
related consequence, define the ordinary Renyi divergence by
`D_q(p||w)=(q-1)^(-1) log sum_S p(S)^q w(S)^(1-q)`.  Because
`log(p/w)` is `2 Lambda_delta`-Lipschitz,

\[
|D_q(p_a\|w_a)-D(p_a\|w_a)|
\le3840n\Lambda_\delta^2|q-1|                                    \tag{7.6}
\]

for the same `q` interval.  Equation (7.6) follows by applying (5.12) directly
to the centered log likelihood ratio.  Both estimates retain the complete
spatial likelihood ratio.

## 8. Toeplitz blocks and the signed finite Jensen defect

Now fix `0<rho<1`, `0<c<1`, and `0<delta<(1-c)/2`.  Let

\[
J_\delta=[\delta,1-c-\delta].                                     \tag{8.1}
\]

For `R|n`, let `w_(a,n,R)` be the product of the consecutive true `R`-site
marginals of `p_(a,n)`.  Stationarity and the exact block cross entropy give

\[
D(p_{a,n}\|w_{a,n,R})
=\frac nR H_R(a,c)-H_n(a,c).                                      \tag{8.2}
\]

This is not the one-site product tangent; every within-block correlation through
radius `R-1` is retained.  From the supplied value tail (1.2),

\[
0\le\frac1nD(p_{a,n}\|w_{a,n,R})
=\frac{H_R}{R}-\frac{H_n}{n}
\le e_R(c)=\frac cR\operatorname{Tr}b(Q_R).                       \tag{8.3}
\]

Combining (6.4), (7.5), and (8.3) proves the advertised bound

\[
\boxed{
0\le\frac{E_{n,R}(q,a)}n
\le e_R(c)+2880\Lambda_\delta^2|q-1|,}                            \tag{8.4}
\]

uniformly for `a in J_delta`, `1/2<=q<=3/2`, and every multiple `n` of `R`.

For `a_t=(1-t)a_0+ta_1`, every value in (8.4) lies in the same interval
`[0,U_(R,q)]`.  Therefore the **signed finite Jensen defect** obeys

\[
\boxed{
\left|\frac1n\left(E_{n,R}(q,a_t)
-(1-t)E_{n,R}(q,a_0)-tE_{n,R}(q,a_1)\right)\right|
\le e_R(c)+2880\Lambda_\delta^2|q-1|.}                            \tag{8.5}
\]

The order of limits is explicit: fix `rho,c,delta`; let `R->infinity` and
`q=q_R->1`, while `n` may be any multiple of `R`.  The right side tends to zero
because the supplied Toeplitz estimate gives `e_R=O((log R)^2/R)`.  One may also
first take `n->infinity` at fixed `R,q`, since the bound is uniform in `n`.
There is no interchange of a `q` derivative with a thermodynamic limit.

At `q=1`, `-partial_q B(1,a)=(n/R)H_R(a,c)` and the derivative of the exact
remainder is the KL in (8.2).  Estimate (8.5) extends this correlated approximation
to a full real-q neighborhood.  It still does not supply the sign of the block
entropy's `a`-Jensen defect at general high contrast.

## 9. Source audit and what is genuinely new

1. **Pemantle--Peres.**  R. Pemantle and Y. Peres, *Concentration of Lipschitz
   functionals of determinantal and other strong Rayleigh measures*,
   arXiv:1108.0687v3.  The imported statement is exactly Theorem 3.2 and its
   following `48n` remark: strong Rayleigh law, Hamming-1-Lipschitz function,
   and the displayed two-sided tail.  Lemmas 5.1--5.2 verify those hypotheses
   for the actual full DPP atom law.  The information-content application,
   the explicit MGF constant, and the correlated real-q remainder estimates
   (7.5)--(8.5) are the connecting steps proved here, not statements from that
   paper.

2. **Queffelec--Zarouf.**  H. Queffelec and R. Zarouf, *On Bernstein's
   inequality for polynomials*, arXiv:1903.10801v1.  The imported statement is
   Theorem 1.1, `||T'||_infinity<=D||T||_infinity` for a degree-`D`
   trigonometric polynomial.  The nested-interval formula (3.2), its application
   to the full-atom Chebyshev series, and the contrast-transport theorem are new
   connections proved here.

3. **Borcea--Branden--Liggett.**  *Negative dependence and the geometry of
   polynomials*, arXiv:0707.2340, supplies the surrounding strong-Rayleigh
   framework.  No unproved theorem from it is needed: stability of the precise
   L-ensemble polynomial is proved directly in Lemma 5.2.

4. **Cluster-expansion scout.**  Bissacot--Fernandez--Procacci,
   *On the convergence of cluster expansions for polymer gases*,
   arXiv:1002.3261, was consulted as the distant-field candidate.  No polymer
   activity and summability criterion was established for the real-q
   principal-minor pressure at fixed high contrast, so no theorem from it is
   imported and no claim of impossibility is made.

## 10. Remaining target-level gap

The general interval `37/40<c<1` and the full legal `a` interval remain open.
The explicit contrast band in (0.1) is extremely narrow and the proved `a`
strip stays away from both endpoints.  The response constants deteriorate as
the spectral gap closes.

The real-q result (8.5) gives a rigorously vanishing signed error for the
correlated reference remainder, but it does not give the missing sign of the
finite-`R` block entropy Jensen defect at arbitrary high contrast.  Equivalently,
a target proof still needs either:

* a high-contrast sign theorem for the growing block entropies with an error
  compatible with (8.5), or
* a stronger representation whose signed main term is controlled directly
  across the entire legal interval.

No saddle point, replica symmetry, quantum entropy, pair-correlation truncation,
or unproved derivative/limit interchange is used.
