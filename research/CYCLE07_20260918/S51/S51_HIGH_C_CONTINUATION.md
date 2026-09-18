# S51 high-contrast continuation — full visible answer, UNDER REVIEW

Source chat: Say S51
Source message: ba292c40-7446-4cae-854a-a7fc0ddf9660
The complete visible answer (14,638 characters) was captured on 2026-09-18. Downloadable MD/Python/ZIP artifacts are not yet present. Author labels below are not independent certification. This is a separate manuscript from the first cycle06 entropy-rate bridge.

--- BEGIN AUTHOR TEXT ---

# S51 continuation: a genuine improvement in the \(c\)-direction

## Status: **PROVED\_SCOPED**

The refinement produces a new finite-volume and entropy-rate theorem for the **true half-density sine family**:

\[
c_0=\frac{37}{40},\qquad
c_*=\frac{937}{1000},\qquad
c^\sharp=c_*+3\cdot10^{-13}.
\]

Let \(Q_n\) be the true \(n\times n\) half-density sine Toeplitz block and define the normalized full configuration entropy

\[
f_n(a,c)
=
\frac1n H\!\left(\operatorname{DPP}(aI_n+cQ_n)\right),
\qquad
m(c)=\frac{1-c}{2}.
\]

Then, for every \(n\),

\[
\boxed{
\partial_a^2f_n(a,c)\le -\frac1{200}
}
\tag{1}
\]

whenever

\[
\boxed{
\frac{37}{40}\le c\le
\frac{937}{1000}+3\cdot10^{-13},
\qquad
|a-m(c)|\le10^{-9}.
}
\tag{2}
\]

Consequently, for the actual half-density sine entropy rate,

\[
\boxed{
\begin{aligned}
h_{1/2}(a_t,c)
\ge{}&(1-t)h_{1/2}(a_0,c)+t h_{1/2}(a_1,c)\\
&+\frac1{400}t(1-t)(a_1-a_0)^2,
\end{aligned}
}
\tag{3}
\]

for \(a_0,a_1\) in the strip (2) and \(a_t=(1-t)a_0+ta_1\).

This is strictly better in the requested \(c\)-direction:

- RL01’s previous open-strip result stopped at
  \[
  c=\frac{37}{40}+10^{-13}
  \]
  with \(|a-m(c)|\le1/200\). citeturn562762view0
- The independently reviewed SA02 result reached
  \[
  c=\frac{937}{1000}
  \]
  only on the one-dimensional balanced line \(a=m(c)\). citeturn646141view0turn646141view2
- The new result reaches **strictly past \(937/1000\)** and opens that line into a genuine two-dimensional strip.

It is not a set-theoretic superset of the older wide strip near \(37/40\), since the new transverse width is smaller. It is, however, a real extension of the certified contrast frontier and a structurally stronger continuation mechanism.

---

# 1. The new mechanism

The improvement has three parts.

First, instead of comparing entropy values at two contrasts and paying the binary-entropy modulus

\[
\Delta c\log\frac1{\Delta c},
\]

we differentiate a **bivariate full-atom Chebyshev expansion** directly. This yields a linear response bound for the curvature itself:

\[
\left|
\partial_a^2f_n(a,c)-\partial_a^2f_n(a,c')
\right|
\le L|c-c'|.
\tag{4}
\]

Second, at half density the true sine block has an exact complement–gauge symmetry. This forces

\[
\partial_a^3f_n(m(c),c)=0.
\tag{5}
\]

Third, because the first transverse derivative of the curvature vanishes, moving away from the balanced line costs \(O(s^2)\), not \(O(|s|)\):

\[
\partial_a^2f_n(m(c)+s,c)
\le
\partial_a^2f_n(m(c),c)
+
\frac12M_4s^2.
\tag{6}
\]

These are not adjustments to the old numerical truncation. They replace the old value-coupling step with a direct parameter-response theorem and exploit an exact symmetry absent from the previous scheme.

---

# 2. Bivariate full-atom expansion

Let \(0\le Q\le I\) be any finite Hermitian contraction and put

\[
K(a,c)=aI+cQ,
\qquad
f(a,c)=\frac1nH(\operatorname{DPP}(K(a,c))).
\]

Suppose that on a rectangle \(R=I_a\times I_c\),

\[
\delta I\le K(a,c)\le(1-\delta)I,
\qquad 0<\delta<\frac12.
\tag{7}
\]

For a configuration \(S\), define

\[
A_S(a,c)=K(a,c)-D_{S^c}.
\]

The exact full atom is

\[
p_{a,c}(S)
=
(-1)^{n-|S|}\det A_S(a,c)
=
|\det A_S(a,c)|.
\tag{8}
\]

Thus the normalized full Shannon entropy is

\[
f(a,c)
=
-\frac1{2n}
\mathbb E_{a,c}
\operatorname{Tr}\log A_Y(a,c)^2.
\tag{9}
\]

This is the configuration entropy; no replacement by \(\operatorname{Tr}b(K)\) is made.

Set

\[
r=\frac{1-\delta}{1+\delta},
\qquad
X_Y=
\frac{2A_Y^2-(1+\delta^2)I}{1-\delta^2}.
\]

The spectrum of \(X_Y\) lies in \([-1,1]\). The scalar Chebyshev identity gives

\[
f(a,c)
=
C_\delta+\sum_{m\ge1}u_m(a,c),
\tag{10}
\]

where

\[
u_m(a,c)
=
\frac{(-1)^m r^m}{mn}
\mathbb E_{a,c}\operatorname{Tr}T_m(X_Y)
\tag{11}
\]

and

\[
\boxed{
\|u_m\|_{C(R)}\le\frac{r^m}{m}.
}
\tag{12}
\]

The important new point is that \(u_m\) is a **bivariate polynomial of total degree at most \(2m\)**.

Indeed, before taking expectation,

\[
\operatorname{Tr}T_m(X_Y)
\]

is a polynomial of total degree at most \(2m\) in

\[
a,\ c,\ Y_1,\ldots,Y_n.
\]

After Boolean reduction, its monomials have the form

\[
a^pc^q\prod_{i\in V}Y_i,
\qquad
p+q+|V|\le2m.
\]

Under the actual moving DPP law,

\[
\mathbb E_{a,c}\prod_{i\in V}Y_i
=
\det(aI+cQ)_V,
\tag{13}
\]

which is a polynomial of total degree \(|V|\) in \((a,c)\). Therefore averaging under the moving law preserves the \(2m\) total-degree bound.

This is where all reference-law and probability-weight derivatives are paid. No expectation has been frozen.

---

# 3. Direct \(aac\) response lemma

For an interval \(I=[A,B]\) of length \(\ell\) and an inner subset \(E\Subset I\), define its Chebyshev angular margin by

\[
\sigma(E;I)
=
\inf_{x\in E}
\frac{2\sqrt{(x-A)(B-x)}}{\ell}.
\tag{14}
\]

Let \(P(a,c)\) have degree at most \(D\) in each variable on
\(I_a\times I_c\). If the inner regions have angular margins
\(\sigma_a,\sigma_c\), then

\[
\boxed{
\begin{aligned}
\|\partial_c\partial_a^2P\|
\le
\frac8{\ell_c\ell_a^2}
\left(
\frac{D^3}{\sigma_c\sigma_a^2}
+
\frac{D^2}{\sigma_c\sigma_a^3}
\right)
\|P\|.
\end{aligned}
}
\tag{15}
\]

To see this, write \(x=x_0+(\ell/2)\cos\theta\). Trigonometric Bernstein gives

\[
\|P'\|_E
\le
\frac{2D}{\ell\sigma}\|P\|_I,
\tag{16}
\]

and

\[
\|P''\|_E
\le
\frac4{\ell^2}
\left(
\frac{D^2}{\sigma^2}
+
\frac D{\sigma^3}
\right)
\|P\|_I.
\tag{17}
\]

Apply (17) in \(a\), uniformly over the full outer \(c\)-interval, and then apply (16) in \(c\).

Using \(D=2m\) and (12), summation over the full entropy series yields

\[
\boxed{
\|f_{aac}\|
\le
\frac{64S_2(r)}
{\ell_c\ell_a^2\sigma_c\sigma_a^2}
+
\frac{32S_1(r)}
{\ell_c\ell_a^2\sigma_c\sigma_a^3},
}
\tag{18}
\]

where

\[
S_1(r)=\sum_{m\ge1}mr^m
=
\frac r{(1-r)^2},
\]

\[
S_2(r)=\sum_{m\ge1}m^2r^m
=
\frac{r(1+r)}{(1-r)^3}.
\tag{19}
\]

The derivative series is dominated by a summable multiple of
\((m^2+m)r^m\), so the mixed differentiation is justified locally uniformly.

This is the first reusable improvement over S6:

\[
\boxed{
|f_{aa}(a,c)-f_{aa}(a,c')|
\le L|c-c'|
}
\tag{20}
\]

rather than deriving curvature from a value difference of order
\(\Delta c\log(1/\Delta c)\).

---

# 4. Exact half-density symmetry

For the half-density sine block, let

\[
D=\operatorname{diag}((-1)^j).
\]

The entries of \(Q_n\) satisfy

\[
DQ_nD=I-Q_n.
\tag{21}
\]

Indeed:

- the diagonal entries of both sides are \(1/2\);
- nonzero even separations have zero sine coefficient;
- at odd separations, multiplication by \((-1)^{i-j}\) changes the sign.

Diagonal unitary conjugation leaves every principal minor unchanged, and therefore leaves the DPP law unchanged.

The complement of \(\operatorname{DPP}(K)\) is \(\operatorname{DPP}(I-K)\). Moreover,

\[
\begin{aligned}
I-(aI+cQ_n)
&=(1-a-c)I+c(I-Q_n)\\
&=D\bigl((1-a-c)I+cQ_n\bigr)D.
\end{aligned}
\]

Since configuration complementation is a bijection preserving Shannon entropy,

\[
\boxed{
f_n(a,c)=f_n(1-a-c,c).
}
\tag{22}
\]

Writing

\[
a=m(c)+s,
\qquad
m(c)=\frac{1-c}{2},
\]

we obtain exact evenness in \(s\). Hence

\[
\boxed{
f_{n,aaa}(m(c),c)=0.
}
\tag{23}
\]

This is a finite-block identity; it does not use a projection approximation or a limiting argument.

---

# 5. Fourth-order thickening

For a degree-\(D\) univariate polynomial \(P\), again put

\[
x=x_0+h\cos\theta,
\qquad h=\frac{\ell}{2},
\qquad T(\theta)=P(x).
\]

Direct differentiation gives

\[
\begin{aligned}
P^{(4)}(x)
=
\frac1{h^4\sin^4\theta}
\Bigg[
&T^{(4)}
-6\cot\theta\,T^{(3)}\\
&+\left(-11+\frac{15}{\sin^2\theta}\right)T''\\
&+\left(
6\cot\theta-
\frac{15\cos\theta}{\sin^3\theta}
\right)T'
\Bigg].
\end{aligned}
\tag{24}
\]

Using

\[
\|T^{(k)}\|_\infty\le D^k\|T\|_\infty
\]

and \(|\sin\theta|\ge\sigma\), one obtains

\[
\boxed{
\begin{aligned}
\|P^{(4)}\|
\le\frac{16}{\ell^4}\Bigg[
&\frac{D^4+11D^2}{\sigma^4}
+\frac{6D^3+6D}{\sigma^5}\\
&+\frac{15D^2}{\sigma^6}
+\frac{15D}{\sigma^7}
\Bigg]\|P\|.
\end{aligned}
}
\tag{25}
\]

Applying this to the full-entropy expansion gives

\[
\boxed{
\begin{aligned}
\|f_{aaaa}\|
\le\frac{16}{\ell^4}\Bigg[
&\frac{16S_3+44S_1}{\sigma^4}
+\frac{48S_2+12S_0}{\sigma^5}\\
&+\frac{60S_1}{\sigma^6}
+\frac{30S_0}{\sigma^7}
\Bigg],
\end{aligned}
}
\tag{26}
\]

where

\[
S_0=\frac r{1-r},
\qquad
S_3=\frac{r(1+4r+r^2)}{(1-r)^4},
\tag{27}
\]

and \(S_1,S_2\) are as in (19).

By (23), Taylor’s theorem now gives the quadratic curvature transfer

\[
\boxed{
\left|
f_{aa}(m(c)+s,c)-f_{aa}(m(c),c)
\right|
\le
\frac12\|f_{aaaa}\|s^2.
}
\tag{28}
\]

Without the half-density symmetry the corresponding loss would start with
\(|s|\|f_{aaa}\|\).

---

# 6. Extending the midpoint beyond \(937/1000\)

The source interface used here is the independently reviewed SA02 balanced-line result

\[
f_{n,aa}(m(c),c)\le-\frac1{50},
\qquad
\frac{37}{40}\le c\le\frac{937}{1000}.
\tag{29}
\]

The review explicitly notes that this result covers the balanced line only and does not extend to all \(a\). citeturn646141view1turn646141view2

For the mixed derivative, use the rectangle

\[
I_c=\left[0,\frac{471}{500}\right],
\qquad
I_a=\left[\frac{17}{1000},\frac{41}{1000}\right].
\tag{30}
\]

Throughout this rectangle,

\[
\frac{17}{1000}I
\le aI+cQ_n
\le
\frac{983}{1000}I.
\tag{31}
\]

Thus

\[
r=\frac{983}{1017}.
\]

On the moving midpoint segment

\[
\frac{937}{1000}
\le c\le
\frac{937}{1000}+3\cdot10^{-13},
\qquad a=m(c),
\]

the angular margins satisfy

\[
\sigma_a^2
\ge
\frac{551}{576}
>
\left(\frac{39}{40}\right)^2,
\tag{32}
\]

and

\[
\ell_c\sigma_c
=
2\sqrt{c\left(\frac{471}{500}-c\right)}
>
\frac{17}{125}.
\tag{33}
\]

Also,

\[
S_1(r)<865,
\qquad
S_2(r)<50871.
\tag{34}
\]

Substituting into (18), with \(\ell_a=3/125\), gives

\[
\boxed{
|f_{n,aac}(a,c)|<4.5\cdot10^{10}.
}
\tag{35}
\]

Define

\[
\kappa_n(c)=f_{n,aa}(m(c),c).
\]

By the chain rule,

\[
\kappa_n'(c)
=
f_{n,aac}(m(c),c)
-\frac12f_{n,aaa}(m(c),c).
\]

The second term vanishes by exact symmetry, so

\[
\kappa_n'(c)=f_{n,aac}(m(c),c).
\tag{36}
\]

Starting from (29) at \(c=937/1000\), we get

\[
\begin{aligned}
\kappa_n(c)
&\le
-\frac1{50}
+
(4.5\cdot10^{10})(3\cdot10^{-13})\\
&=
-\frac{13}{2000}.
\end{aligned}
\tag{37}
\]

For \(c\le937/1000\), the source bound \(-1/50\) is stronger. Hence

\[
\boxed{
\kappa_n(c)\le-\frac{13}{2000}
}
\tag{38}
\]

throughout

\[
\frac{37}{40}
\le c\le
\frac{937}{1000}+3\cdot10^{-13}.
\]

This already extends the balanced-line contrast endpoint.

---

# 7. Opening the extended line into an actual strip

For the fourth derivative, take

\[
\delta_4=\frac{73}{5000},
\qquad
c_{\rm out}=\frac{9371}{10000},
\]

and the common outer interval

\[
I_4=
\left[
\frac{146}{10000},
\frac{483}{10000}
\right],
\qquad
\ell_4=\frac{337}{10000}.
\tag{39}
\]

For every contrast in the new range and every \(a\in I_4\),

\[
\delta_4I
\le aI+cQ_n
\le(1-\delta_4)I.
\]

Every point satisfying

\[
|a-m(c)|\le10^{-9}
\]

has angular margin greater than \(93/100\).

Here

\[
r_4=\frac{4927}{5073},
\]

and the exact geometric sums obey

\[
S_0<34,\qquad
S_1<1173,\qquad
S_2<80314,\qquad
S_3<8250807.
\tag{40}
\]

Formula (26) therefore yields

\[
\boxed{
|f_{n,aaaa}(a,c)|<2.3\cdot10^{15}.
}
\tag{41}
\]

Combining (28), (38), and (41), for \(|s|\le10^{-9}\),

\[
\begin{aligned}
f_{n,aa}(m(c)+s,c)
&\le
-\frac{13}{2000}
+
\frac12(2.3\cdot10^{15})(10^{-9})^2\\
&=
-\frac{107}{20000}\\
&<
-\frac1{200}.
\end{aligned}
\tag{42}
\]

This proves the finite-volume theorem (1).

---

# 8. Entropy rate and the S51 local kernel

Integrating (1) in finite volume gives

\[
\begin{aligned}
f_n(a_t,c)\ge{}&
(1-t)f_n(a_0,c)+tf_n(a_1,c)\\
&+\frac1{400}t(1-t)(a_1-a_0)^2.
\end{aligned}
\tag{43}
\]

The true Toeplitz entropy values converge to the entropy rate; this value convergence is an established interface and does not require differentiating the limit. The frozen target also emphasizes that the unresolved problem concerns the true full configuration entropy, rather than \(\operatorname{Tr}b(K)\). citeturn543621view1

Passing \(n\to\infty\) in (43) proves (3).

Combining this with the S51 finite-chord bridge from the previous result,

\[
h_c''(s)=-\Gamma_c(s),
\qquad
s=a-\frac{1-c}{2},
\]

gives the actual complete-kernel sign statement

\[
\boxed{
\Gamma_c(s)\ge\frac1{200}
}
\tag{44}
\]

for

\[
\frac{37}{40}
\le c\le
\frac{937}{1000}+3\cdot10^{-13},
\qquad
|s|\le10^{-9}.
\]

This is the complete moving-law V14 quantity identified in S51, not a corrected-law or frozen-weight surrogate.

---

# 9. What this changes strategically

The old pointwise pair mechanism cannot simply be pushed through the whole remaining interval. The independent review verifies an actual reachable sine posterior at \(c=19/20\) for which

\[
g-2(\mathcal K+\mathcal D)>0,
\]

so a uniform componentwise \(\gamma<2\) ansatz fails there. That does not disprove entropy concavity; it disproves that particular pointwise payment scheme. citeturn646141view2

The new tool separates the problem into two cleaner modules:

1. **Seed sign problem.** Prove a negative balanced-line curvature margin on a new contrast interval, using actual-law averaging, the retained exact pair remainder, or the complete V14/Bellman cancellations.

2. **Deterministic amplification.** Once a seed interval is available, the bivariate response lemma continues it slightly in \(c\), while half-density symmetry opens it quadratically into an \(a\)-strip.

Thus the next genuinely load-bearing target is no longer “prove the whole two-dimensional region directly.” It is:

\[
\boxed{
\text{obtain one new averaged balanced-line seed beyond }0.937.
}
\]

Any such seed can now be promoted automatically to an open entropy-rate region.

For \(\rho\ne1/2\), the exact identity \(DQ_\rho D=I-Q_\rho\) is replaced by a relation involving complementary density \(1-\rho\). Therefore the vanishing of \(f_{aaa}\) at fixed \(\rho\) is no longer automatic. Extending the quadratic thickening to all densities requires either a coupled \((\rho,1-\rho)\) argument or a new direct third-derivative cancellation.

The current advance is precisely

\[
\boxed{
\text{reviewed balanced line through }0.937
\ \longrightarrow\
\text{actual sine strip through }0.937+3\cdot10^{-13}.
}
\]

The exact rational checks give

\[
L_{aac}=4.410084\ldots\times10^{10}<4.5\times10^{10},
\]

\[
M_4=2.260171\ldots\times10^{15}<2.3\times10^{15},
\]

and the final normalized curvature upper bound

\[
-\frac{107}{20000}=-0.00535<-\frac1{200}.
\]

These checks verify the displayed arithmetic, not the source interfaces or the proof independently.

:chatgpt-content-reference{index="6"}

:chatgpt-content-reference{index="7"}

:chatgpt-content-reference{index="8"}
