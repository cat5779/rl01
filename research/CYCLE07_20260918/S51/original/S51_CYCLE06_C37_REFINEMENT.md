# S51 cycle06 continuation — a bivariate full-atom response tool and an actual high-contrast sine strip

## Status

**PROVED_SCOPED, relative to the independently reviewed SA02 balanced-line interface stated in Section 1.**

The new steps below are proved in full.  They are author derivations and have not
received independent certification.  The arithmetic is checked by
`S51_CYCLE06_C37_REFINEMENT_checks.py` using exact rational arithmetic.

The principal new finite-volume result is the following.  Let `Q_n` be the true
half-density sine Toeplitz principal block and let

\[
f_n(a,c)=\frac1n H\bigl(\operatorname{DPP}(aI_n+cQ_n)\bigr),
\qquad m(c)=\frac{1-c}{2}.
\]

Put

\[
c_0=\frac{37}{40},\qquad
c_*=\frac{937}{1000},\qquad
c^\sharp=c_*+3\cdot10^{-13}.
\]

Then, for every `n`, every

\[
c_0\le c\le c^\sharp,
\qquad |a-m(c)|\le10^{-9},
\]

one has

\[
\boxed{\quad \partial_a^2 f_n(a,c)\le-\frac1{200}.\quad}       \tag{0.1}
\]

Consequently the true half-density sine entropy rate is strongly concave on
this strip:

\[
\boxed{
 h_{1/2}(a_t,c)
 \ge (1-t)h_{1/2}(a_0,c)+t h_{1/2}(a_1,c)
 +\frac1{400}t(1-t)(a_1-a_0)^2,
}                                                               \tag{0.2}
\]

whenever `a_0,a_1` lie in the displayed strip and
`a_t=(1-t)a_0+t a_1`.

This improves the certified contrast frontier in two different senses:

1. the earlier universal high-contrast strip stopped at
   `37/40+10^(-13)`;
2. the independently reviewed SA02 result reached `937/1000` only on the
   one-dimensional balanced line.

Result (0.1) reaches strictly beyond `937/1000` and has a genuine open
`a`-strip.  Its `a`-width is small; it is not claimed to contain the older,
wider strip near `37/40`.

The mechanism is reusable.  It has three pieces:

* a **bivariate full-atom Chebyshev response lemma**, which differentiates in
  `c` directly and therefore avoids the old
  `Delta c log(1/Delta c)` entropy-coupling loss;
* the exact **half-density complement--gauge symmetry**, which kills the third
  `a` derivative on the balanced line;
* a **fourth-order curvature thickening lemma**, which turns a balanced-line
  curvature margin into an actual two-dimensional strip with quadratic,
  rather than linear, transverse loss.

---

# 1. Source interfaces actually used

Only two pre-existing mathematical interfaces are used.

### Interface B: reviewed balanced-line curvature

The independent SA02 review verifies, relative to its frozen pair/row
identities, that for the finite full-configuration entropy,

\[
\partial_a^2 f_n(m(c),c)\le-\frac1{50},
\qquad \frac{37}{40}\le c\le\frac{937}{1000}.                    \tag{1.1}
\]

We use (1.1) only for the true half-density sine blocks, a specialization of
that interface.  We do not import the unreviewed large-window sign proposal.

### Interface V: value convergence for true sine blocks

For fixed legal `(a,c)`, the true Toeplitz block entropies satisfy

\[
f_n(a,c)\longrightarrow h_{1/2}(a,c).                            \tag{1.2}
\]

Only values are passed to the limit.  No differentiability of the entropy rate
is used to prove (0.2).

Everything else, including all moving-law parameter derivatives used in the
continuation, is established below.

---

# 2. Bivariate full-atom Chebyshev expansion

The first tool works for every finite Hermitian contraction, not merely for the
sine block.

## Lemma 2.1 — complete moving-law bivariate expansion

Let `0<=Q<=I` on `n` labelled sites and set

\[
K(a,c)=aI+cQ,
\qquad
f(a,c)=\frac1nH(\operatorname{DPP}(K(a,c))).
\]

Let `R=I_a\times I_c` be a rectangle on which

\[
\delta I\le K(a,c)\le(1-\delta)I,
\qquad 0<\delta<\frac12.                                         \tag{2.1}
\]

Put

\[
r=\frac{1-\delta}{1+\delta}.
\]

Then on `R`, uniformly and absolutely,

\[
f(a,c)=C_\delta+\sum_{m\ge1}u_m(a,c),                            \tag{2.2}
\]

where

\[
\deg_{(a,c)}^{\rm total}u_m\le2m,
\qquad
\|u_m\|_{C(R)}\le\frac{r^m}{m}.                                 \tag{2.3}
\]

The polynomial `u_m` already contains all derivatives of the moving DPP law.
There is no frozen reference expectation.

### Proof

For a configuration `S`, let

\[
A_S(a,c)=K(a,c)-D_{S^c}.
\]

Diagonal multilinearity gives the exact full atom

\[
p_{a,c}(S)=(-1)^{n-|S|}\det A_S(a,c)=|\det A_S(a,c)|.             \tag{2.4}
\]

The spectral gap (2.1) and eigenvalue interlacing give

\[
\delta^2I\le A_S(a,c)^2\le I.
\]

Hence the full configuration entropy, not `Tr b(K)`, is

\[
f(a,c)
=-\frac1{2n}\mathbb E_{a,c}\operatorname{Tr}\log A_Y(a,c)^2.     \tag{2.5}
\]

Define

\[
X_Y=\frac{2A_Y^2-(1+\delta^2)I}{1-\delta^2}.
\]

Its spectrum lies in `[-1,1]`.  The scalar Chebyshev identity

\[
-\frac12\log u
=C_\delta+\sum_{m\ge1}\frac{(-1)^m r^m}{m}
T_m\!\left(\frac{2u-(1+\delta^2)}{1-\delta^2}\right)             \tag{2.6}
\]

therefore yields

\[
u_m(a,c)=\frac{(-1)^m r^m}{mn}
\mathbb E_{a,c}\operatorname{Tr}T_m(X_Y).                         \tag{2.7}
\]

The norm bound in (2.3) follows from `|T_m|<=1` on `[-1,1]`.

It remains to pay the moving law.  Before Boolean reduction,
`Tr T_m(X_Y)` is a polynomial of total degree at most `2m` in
`(a,c,Y_1,...,Y_n)`, because `A_Y` is affine and `X_Y` is quadratic.  Boolean
reduction writes every monomial as

\[
a^p c^q\prod_{i\in V}Y_i,
\qquad p+q+|V|\le2m.
\]

Under the actual DPP law,

\[
\mathbb E_{a,c}\prod_{i\in V}Y_i
=\det(aI+cQ)_V,                                                   \tag{2.8}
\]

which is a polynomial of total degree `|V|` in `(a,c)`.  Thus averaging under
the moving law preserves the total-degree bound `2m`.  This proves (2.3) and
the lemma.  \(\square\)

---

# 3. Direct mixed response in contrast

For an interval `I=[A,B]` of length `ell` and a subset `E\Subset I`, define

\[
\sigma(E;I)
=\inf_{x\in E}\frac{2\sqrt{(x-A)(B-x)}}{\ell}.                   \tag{3.1}
\]

This is the minimum sine of the Chebyshev angular coordinate on `E`.

## Lemma 3.1 — bivariate `aac` Bernstein bound

Let `P(a,c)` be a polynomial of degree at most `D` in each variable on
`I_a\times I_c`.  Let `E_a\Subset I_a` and `E_c\Subset I_c`, with lengths
`ell_a,ell_c` for the outer intervals and angular margins
`sigma_a,sigma_c`.  Then

\[
\boxed{
\|\partial_c\partial_a^2P\|_{E_a\times E_c}
\le\frac8{\ell_c\ell_a^2}
\left(
 \frac{D^3}{\sigma_c\sigma_a^2}
 +\frac{D^2}{\sigma_c\sigma_a^3}
\right)\|P\|_{I_a\times I_c}.
}                                                               \tag{3.2}
\]

### Proof

For a univariate polynomial on an interval of length `ell`, write
`x=x_0+(ell/2)cos(theta)`.  Trigonometric Bernstein gives

\[
\|P'\|_E\le\frac{2D}{\ell\sigma}\|P\|_I                         \tag{3.3}
\]

and

\[
\|P''\|_E\le\frac4{\ell^2}
\left(\frac{D^2}{\sigma^2}+\frac D{\sigma^3}\right)\|P\|_I.     \tag{3.4}
\]

Apply (3.4) in `a`, uniformly for every `c` in the full outer `c` interval.
For fixed `a` in `E_a`, apply (3.3) in `c` to the polynomial
`partial_a^2P(a,c)`.  Multiplying the two estimates gives (3.2).  \(\square\)

## Corollary 3.2 — dimension-free full-entropy mixed response

Under Lemma 2.1,

\[
\boxed{
\|f_{aac}\|_{E_a\times E_c}
\le
\frac{64S_2(r)}{\ell_c\ell_a^2\sigma_c\sigma_a^2}
+
\frac{32S_1(r)}{\ell_c\ell_a^2\sigma_c\sigma_a^3},
}                                                               \tag{3.5}
\]

where

\[
S_1(r)=\sum_{m\ge1}mr^m=\frac r{(1-r)^2},
\quad
S_2(r)=\sum_{m\ge1}m^2r^m=\frac{r(1+r)}{(1-r)^3}.                \tag{3.6}
\]

Indeed, use `D=2m` and `||u_m||<=r^m/m` in (3.2).  The resulting derivative
series is dominated by a summable multiple of `(m^2+m)r^m`, so termwise
mixed differentiation is justified.

The important difference from the older contrast coupling is that (3.5) is a
direct Lipschitz estimate for the curvature itself:

\[
|f_{aa}(a,c)-f_{aa}(a,c')|\le L|c-c'|.                            \tag{3.7}
\]

There is no binary-entropy modulus `|c-c'| log(1/|c-c'|)`.

---

# 4. Exact half-density complement--gauge symmetry

Let `Q_n` be the true half-density sine block.  Define the diagonal sign matrix

\[
D=\operatorname{diag}((-1)^j).
\]

Because the off-diagonal sine coefficient vanishes for nonzero even
separations and changes sign for odd separations,

\[
DQ_nD=I-Q_n.                                                      \tag{4.1}
\]

Diagonal unitary conjugation leaves every principal minor unchanged, hence
leaves the DPP law unchanged.  Also the complement of `DPP(K)` is
`DPP(I-K)`.  Therefore

\[
\begin{aligned}
I-(aI+cQ_n)
&=(1-a-c)I+c(I-Q_n)\\
&=D\bigl((1-a-c)I+cQ_n\bigr)D,
\end{aligned}
\]

and the configuration complement is a bijection.  Consequently

\[
\boxed{f_n(a,c)=f_n(1-a-c,c).}                                   \tag{4.2}
\]

Writing `a=m(c)+s`, the function is even in `s`.  In particular,

\[
\boxed{f_{n,aaa}(m(c),c)=0}                                      \tag{4.3}
\]

for every finite `n` and every legal interior `c`.

This cancellation is special to half density.  It does not follow merely from
non-nullness or from a pointwise posterior comparison.

---

# 5. Fourth-order curvature thickening

## Lemma 5.1 — interior fourth derivative bound

Let `P` be a polynomial of degree at most `D` on an interval of length `ell`.
On an inner set with angular margin `sigma`,

\[
\boxed{
\begin{aligned}
\|P^{(4)}\|
\le\frac{16}{\ell^4}\Bigg[&
\frac{D^4+11D^2}{\sigma^4}
+\frac{6D^3+6D}{\sigma^5}\\
&+\frac{15D^2}{\sigma^6}
+\frac{15D}{\sigma^7}
\Bigg]\|P\|.
\end{aligned}
}                                                               \tag{5.1}
\]

### Proof

With `x=x_0+h cos(theta)`, `h=ell/2`, and `T(theta)=P(x)`, direct
differentiation gives

\[
P^{(4)}(x)=\frac1{h^4\sin^4\theta}
\left[
T^{(4)}-6\cot\theta\,T^{(3)}
+\left(-11+\frac{15}{\sin^2\theta}\right)T''
+\left(6\cot\theta-\frac{15\cos\theta}{\sin^3\theta}\right)T'
\right].                                                        \tag{5.2}
\]

Trigonometric Bernstein gives `||T^(k)||<=D^k||T||` for
`1<=k<=4`.  Use `|sin theta|>=sigma` and `|cos theta|<=1` in (5.2).
This is exactly (5.1).  \(\square\)

## Corollary 5.2 — fourth derivative of full configuration entropy

With the notation of Lemma 2.1, define

\[
S_0=\frac r{1-r},\quad
S_1=\frac r{(1-r)^2},\quad
S_2=\frac{r(1+r)}{(1-r)^3},\quad
S_3=\frac{r(1+4r+r^2)}{(1-r)^4}.                                 \tag{5.3}
\]

Then

\[
\boxed{
\begin{aligned}
\|f_{aaaa}\|\le\frac{16}{\ell^4}\Bigg[&
\frac{16S_3+44S_1}{\sigma^4}
+\frac{48S_2+12S_0}{\sigma^5}\\
&+\frac{60S_1}{\sigma^6}
+\frac{30S_0}{\sigma^7}
\Bigg].
\end{aligned}
}                                                               \tag{5.4}
\]

This follows from (5.1) with `D=2m`, the bound `||u_m||<=r^m/m`, and
termwise summation.

If `g(a)=f_{aa}(a,c)` and `g'(m(c))=0` by (4.3), Taylor's theorem now gives

\[
\boxed{
|f_{aa}(m(c)+s,c)-f_{aa}(m(c),c)|
\le\frac12\|f_{aaaa}\|\,s^2.
}                                                               \tag{5.5}
\]

This quadratic transverse loss is the main half-density gain.

---

# 6. Explicit continuation past `937/1000`

Set

\[
c_*=\frac{937}{1000},
\qquad \Delta_c=3\cdot10^{-13}.
\]

Use the bivariate rectangle

\[
I_c=\left[0,\frac{471}{500}\right],
\qquad
I_a=\left[\frac{17}{1000},\frac{41}{1000}\right].                \tag{6.1}
\]

For every Hermitian contraction `Q`, this rectangle has the spectral gap

\[
\frac{17}{1000}I\le aI+cQ\le\frac{983}{1000}I.                   \tag{6.2}
\]

Thus

\[
r=\frac{983}{1017}.
\]

On the moving midpoint segment

\[
c_*\le c\le c_*+\Delta_c,
\qquad a=m(c),                                                    \tag{6.3}
\]

the `a` angular margin satisfies

\[
\sigma_a^2\ge\frac{551}{576}>\left(\frac{39}{40}\right)^2.     \tag{6.4}
\]

For the `c` coordinate,

\[
\ell_c\sigma_c
=2\sqrt{c\left(\frac{471}{500}-c\right)}
>\frac{17}{125}.                                                  \tag{6.5}
\]

Also

\[
S_1(r)<865,
\qquad S_2(r)<50871.                                              \tag{6.6}
\]

Substitution into (3.5), with `ell_a=3/125`, gives the exact rational bound

\[
\boxed{
|f_{n,aac}(a,c)|<4.5\cdot10^{10}
}                                                               \tag{6.7}
\]

uniformly in `n` and on (6.3).

Define the balanced curvature

\[
\kappa_n(c)=f_{n,aa}(m(c),c).
\]

The chain rule and (4.3) give

\[
\kappa_n'(c)
=f_{n,aac}(m(c),c)-\frac12f_{n,aaa}(m(c),c)
=f_{n,aac}(m(c),c).                                               \tag{6.8}
\]

At `c=c_*`, Interface B gives `kappa_n(c_*)<=-1/50`.  Hence for
`c_*<=c<=c_*+Delta_c`,

\[
\kappa_n(c)
\le-\frac1{50}+(4.5\cdot10^{10})(3\cdot10^{-13})
=-\frac{13}{2000}.                                                \tag{6.9}
\]

For `c<=c_*`, Interface B is stronger, so (6.9) holds throughout

\[
\frac{37}{40}\le c\le c_*+3\cdot10^{-13}.                        \tag{6.10}
\]

This is already a strict extension of the reviewed balanced-line endpoint.

---

# 7. Opening the line into a strip

For the fourth derivative use

\[
\delta_4=\frac{73}{5000},
\qquad
c_{\rm out}=\frac{9371}{10000},                                  \tag{7.1}
\]

and the common outer `a` interval

\[
I_4=
\left[\frac{146}{10000},\frac{483}{10000}\right],
\qquad \ell_4=\frac{337}{10000}.                                 \tag{7.2}
\]

For every `c` in (6.10) and every `a` in `I_4`,

\[
\delta_4I\le aI+cQ_n\le(1-\delta_4)I.                            \tag{7.3}
\]

Every point with

\[
|a-m(c)|\le10^{-9}                                                \tag{7.4}
\]

has angular margin in `I_4` strictly larger than `93/100`.  Here

\[
r_4=\frac{4927}{5073}
\]

and the exact geometric sums satisfy

\[
S_0<34,
\quad S_1<1173,
\quad S_2<80314,
\quad S_3<8250807.                                                \tag{7.5}
\]

Formula (5.4) therefore gives

\[
\boxed{
|f_{n,aaaa}(a,c)|<2.3\cdot10^{15}
}                                                               \tag{7.6}
\]

uniformly in `n` and on the strip (7.4).

Combining (5.5), (6.9), and (7.6), for `|s|<=10^(-9)`,

\[
\begin{aligned}
f_{n,aa}(m(c)+s,c)
&\le-\frac{13}{2000}
 +\frac12(2.3\cdot10^{15})(10^{-9})^2\\
&=-\frac{107}{20000}
<-\frac1{200}.
\end{aligned}                                                     \tag{7.7}
\]

This proves (0.1).

---

# 8. Entropy-rate and S51-kernel consequences

For fixed `c` in the new range, integrate (0.1) between two points in the
strip.  For every `n`,

\[
f_n(a_t,c)
\ge(1-t)f_n(a_0,c)+t f_n(a_1,c)
+\frac1{400}t(1-t)(a_1-a_0)^2.                                   \tag{8.1}
\]

Using only value convergence (1.2) gives (0.2).  No derivative of the limiting
rate has been assumed.

Combining (0.2) with the S51 finite-chord bridge proved earlier in this cycle,

\[
h_c''(s)=-\Gamma_c(s),
\qquad s=a-m(c),                                                   \tag{8.2}
\]

gives the local actual-law V14 sign consequence

\[
\boxed{
\Gamma_c(s)\ge\frac1{200}
\quad\text{for}\quad
\frac{37}{40}\le c\le\frac{937}{1000}+3\cdot10^{-13},
\quad |s|\le10^{-9}.
}                                                               \tag{8.3}
\]

This identifies the sign of the same complete moving-law kernel appearing in
the S51 bridge; it is not a corrected-law or frozen-weight surrogate.

---

# 9. Why this is structurally better than the old RL01 continuation

The earlier S6 continuation compared entropy **values** at contrasts `c` and
`c_0`, obtaining

\[
\|f_c-f_{c_0}\|\lesssim b((c-c_0)/2)
\asymp(c-c_0)\log\frac1{c-c_0},                                  \tag{9.1}
\]

and then recovered curvature with a separate value-to-curvature theorem.  The
logarithmic modulus forced an extremely short contrast interval.

The present tool differentiates the complete full-atom Chebyshev series in
`c` before taking any comparison.  The moving probability law is incorporated
by the bivariate Boolean-degree lemma, yielding the linear curvature modulus

\[
|f_{aa}(a,c)-f_{aa}(a,c')|\le L|c-c'|.                            \tag{9.2}
\]

At half density, exact complement--gauge symmetry further changes the loss in
the transverse offset from `O(|s|)` to `O(s^2)`.  These are genuine structural
improvements, not a retuning of the S6 truncation parameter.

The verified posterior obstruction near `c=19/20` refutes a uniform
componentwise `gamma<2` pair ansatz, but it does not refute (9.2), the symmetry
cancellation, or an actual-law averaged sign theorem.  The present result does
not demand componentwise positivity.

---

# 10. Remaining obligation for the interval `(37/40,1)`

The new analytic continuation is not the main high-contrast sign engine.  It
is a **seed amplifier**:

> Any new balanced-line interval on which one proves a finite-volume margin
> `f_aa(m(c),c)<=-kappa` can now be converted, with explicit constants, into an
> open two-dimensional strip and can be continued a short explicit distance in
> `c`.

To make macroscopic progress beyond `0.937`, one still needs a new balanced-line
seed there.  Because the old pointwise pair comparison has an actual sine
posterior counterexample at `c=0.95`, that seed must use actual-law averaging,
the retained exact pair remainder, or the complete V14/Bellman cancellation;
it cannot be obtained by reinstating the disproved componentwise ansatz.

For `rho!=1/2`, the identity `DQ_rho D=I-Q_rho` is replaced by a relation to a
kernel of complementary density.  Thus `f_aaa(m(c),c)=0` is no longer automatic
at fixed `rho`.  Extending the quadratic thickening to all densities requires
either a paired `(rho,1-rho)` argument or a direct controlled third-derivative
cancellation.

The precise scoped advance established here is therefore:

\[
\boxed{
\text{balanced line through }0.937
\quad\longrightarrow\quad
\text{actual sine strip through }0.937+3\cdot10^{-13}.
}
\]
