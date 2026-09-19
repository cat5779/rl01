# S75 — Actual-weight star reveal monotonicity

**PROVED:** a scale-free, actual-law averaged reveal theorem for a **one-center, one-parity star**, valid at half density for **every \(0<c<1\) and every legal \(0<a<1-c\)**. The theorem gives an explicit positive drift, an enumeration-free moment method, and signed spatial truncation within that geometry.

**DISPROVED:** unconditional nonnegative drift of every individual cross pair in arbitrary sine geometry. A three-site true-sine counterexample has been certified using exact-rational interval arithmetic.

**INCOMPLETE:** the full interval-core/two-parity-halo reveal problem, a globally affordable payment returning that geometry to the original Shannon entropy, and the requested entropy-rate concavity theorem. The remaining costs are quantified below.

:chatgpt-content-reference{index="5"} · :chatgpt-content-reference{index="6"} · :chatgpt-content-reference{index="7"}

The proof below is independent of S73. The only accepted results imported from the packet are the score/reveal identities and S72’s comparison and finite-to-rate interfaces. citeturn556790view0turn122528view0

---

## 1. The new tool

### Input class

Let \(j\) be a center and \(E\) a collection of leaves. Consider the kernel
\[
K_{jj}=d,\qquad
K_{ik}=d\,\mathbf 1_{i=k}\quad(i,k\in E),\qquad
K_{ij}=z_i,
\]
where
\[
0<d<1,\qquad u=1-d,\qquad w_i=|z_i|^2,
\qquad
T:=\sum_{i\in E}w_i<\min(d,u)^2.                         \tag{1}
\]

This is a strict Hermitian contraction: its nontrivial eigenvalues are
\[
d\pm\sqrt T.
\]
A countable leaf set is allowed through its consistent finite marginals.

Fix
\[
I=\{j\}\cup C,\qquad A=\{j\}\cup B,\qquad C\subseteq B\subseteq E.
\]
Give the center and leaves opposite parity labels. Thus
\[
\Chi((G_A)_{II})=\sum_{i\in C}f_{ij}(G_A).
\]
A reveal adds a leaf \(r\in E\setminus B\). **No second center is observed.**

Define
\[
C_\star(d)
=\frac{256\{d^{-3}+(1-d)^{-3}\}}{d(1-d)}.                 \tag{2}
\]

### Output inequality

With the **actual** conditional reveal probability
\[
q=\mathbb P(Y_r=1\mid Y_A),
\]
the theorem is
\[
\boxed{
\mathbb E\Delta_\Chi(Y_A)
\ge
C_\star(d)\,w_r^2\sum_{i\in C}w_i^3
\ge0.
}                                                       \tag{3}
\]

Every old word is included. In particular, \(q\) is **not** replaced by \(d\) while conditioning on the observed center.

For \(B\subseteq B'\), with the core fixed, this telescopes:
\[
\boxed{
\begin{aligned}
&\mathbb E\Chi((G_{\{j\}\cup B'})_{II})
-\mathbb E\Chi((G_{\{j\}\cup B})_{II})\\
&\qquad\ge
C_\star(d)
\left(\sum_{i\in C}w_i^3\right)
\left(\sum_{r\in B'\setminus B}w_r^2\right).
\end{aligned}
}                                                       \tag{4}
\]

There is no negative compensator or endpoint correction in this comparison.

### Exact sine-model scope

Take \(\rho=1/2\), choose any integer center \(j\), and allow only leaves of the opposite parity. Then
\[
d=a+\frac c2,\qquad
w_i=\frac{c^2}{\pi^2(i-j)^2},
\qquad
\sum_{i-j\ {\rm odd}}w_i=\frac{c^2}{4}.
\]
Legal \(a\) implies
\[
\min(d,1-d)>\frac c2,
\]
so (1) holds for every legal \(a\) and every \(0<c<1\).

Here \(d\) is the **observed marginal**, not the noise bias
\[
p_{\rm noise}=\frac{a}{1-c}.
\]

The row-sum identity follows directly from the inverse-square sum over odd integers. No finite sine compression is treated as a projection. Sites outside the stated star are **marginalized, not conditioned on**.

---

## 2. Exact two-output averaging

For a conditional two-site kernel
\[
C=
\begin{pmatrix}
\alpha&z\\
\bar z&\beta
\end{pmatrix},
\qquad s=|z|^2,
\]
write its actual four probabilities as
\[
\begin{aligned}
p_{11}&=\alpha\beta-s, &
p_{10}&=\alpha(1-\beta)+s,\\
p_{01}&=(1-\alpha)\beta+s, &
p_{00}&=(1-\alpha)(1-\beta)-s.
\end{aligned}
\]

Define
\[
\mathcal F(\alpha,\beta,s)
=
s\left(
\frac1{p_{11}}+\frac1{p_{10}}+\frac1{p_{01}}+\frac1{p_{00}}
\right)
+\log\frac{p_{11}p_{00}}{p_{10}p_{01}}.                   \tag{5}
\]

### Pair-averaging identity

\[
\boxed{
\mathbb E f_{ij}\!\left(
(C-\operatorname{diag}(1-Y))^{-1}
\right)
=\mathcal F(\alpha,\beta,s).
}                                                       \tag{6}
\]

**Proof.** Let
\[
D_y=\det(C-\operatorname{diag}(1-y)).
\]
Then
\[
D_y=\sigma_i\sigma_jp_y.
\]
For the inverse two-site matrix,
\[
h=\frac{s}{D_y^2},
\qquad
x=\frac{D_y+s}{D_y^2},
\qquad
x-h=\frac1{D_y}.
\]
Consequently,
\[
p_y f_{ij}
=
\frac{s}{p_y}
+\sigma_i\sigma_j
\log\frac{D_y}{D_y+s}.
\]
Summing over the four actual outputs gives the reciprocal term in (5). The independent-cell denominators cancel in the logarithms, leaving
\[
\log\frac{p_{11}p_{00}}{p_{10}p_{01}}.
\]
This proves (6), including the opposite-sign words. \(\square\)

This identity is the first compensation step: the signed fixed-word terms are averaged **before** any envelope is taken.

---

## 3. Complete proof of the star theorem

### 3.1 Exact conditional reduction

The leaf marginal has kernel \(dI\). Hence the leaf outputs are independent Bernoulli\((d)\).

This is independence of a **marginal**. It is not independence conditional on the observed center.

For a selected pair \((i,j)\), condition on the other observed leaves \(B\setminus\{i\}\). The Schur complement gives the pair kernel
\[
\begin{pmatrix}
d&z_i\\
\bar z_i&\beta
\end{pmatrix},
\]
where
\[
\beta
=
d+\sum_{k\in B\setminus\{i\}}
w_k
\left(
\frac{1-Y_k}{1-d}-\frac{Y_k}{d}
\right).                                                \tag{7}
\]
Thus
\[
\mathbb E f_{ij}(G_A)
=
\mathbb E\mathcal F(d,\beta,w_i).                         \tag{8}
\]

Adding a leaf adds an independent summand in (7), **after the two core outputs have been averaged using (6)**. This is a reordering of the exact joint expectation. By the tower property, its change is precisely the expectation of the original actual-\(q\) reveal drift.

### 3.2 Particle-hole reduction

Complementing every output and replacing \(K\) by \(I-K\) sends
\[
G\longmapsto-G.
\]
It leaves \(f\) and \(\Chi\) unchanged, replaces \(d\) by \(1-d\), and preserves every \(w_i\).

It therefore suffices to prove the theorem for \(d\ge1/2\). Write
\[
u=1-d\le d.
\]

Fix \(s=w_i\), and set
\[
t=\beta-\frac12=b+\sum_k\xi_k,
\qquad b=d-\frac12\ge0,
\]
where independently
\[
\xi_k=
\begin{cases}
-w_k/d,&\text{with probability }d,\\[1mm]
w_k/u,&\text{with probability }u.
\end{cases}                                             \tag{9}
\]

Every integer moment of \(\xi_k\) is nonnegative:
\[
\mathbb E\xi_k^\ell
=
w_k^\ell
\left\{
(-1)^\ell d^{1-\ell}+u^{1-\ell}
\right\}
\ge0.                                                   \tag{10}
\]
For \(\ell=1\), it is zero. For positive even \(\ell\), it is positive. For odd \(\ell\ge3\), positivity follows from \(u\le d\).

By independence and the multinomial expansion, every moment of \(t\) is also nonnegative.

### 3.3 Positive Taylor coefficients after actual pair averaging

For
\[
|t|<R_s:=\frac12-\frac{s}{u},
\]
the following expansion is absolutely convergent:
\[
\begin{aligned}
\mathcal F(d,\beta,s)
={}&
\sum_{n\ge2}\frac{n-1}{n}s^n
\Big[
(d\beta)^{-n}+(u(1-\beta))^{-n}\\
&\hspace{25mm}
+(-1)^{n-1}
\{(d(1-\beta))^{-n}+(u\beta)^{-n}\}
\Big].
\end{aligned}                                           \tag{11}
\]

For odd \(n\), the bracket becomes
\[
(d^{-n}+u^{-n})
\left\{
\left(\frac12+t\right)^{-n}
+
\left(\frac12-t\right)^{-n}
\right\},
\]
which has nonnegative even Taylor coefficients and zero odd coefficients.

For even \(n\), it becomes
\[
(d^{-n}-u^{-n})
\left\{
\left(\frac12+t\right)^{-n}
-
\left(\frac12-t\right)^{-n}
\right\}.
\]
The first factor is nonpositive. The second has nonpositive odd Taylor coefficients and zero even coefficients. Their product again has nonnegative coefficients.

Therefore
\[
\boxed{
\mathcal F\left(d,\frac12+t,s\right)
=
\sum_{k\ge0}b_k(d,s)t^k,
\qquad b_k(d,s)\ge0.
}                                                       \tag{12}
\]

Explicitly,
\[
b_k
=
\sum_{\substack{n\ge2\\n+k\ {\rm odd}}}
\frac{n-1}{n}s^n
2^{n+k+1}\binom{n+k-1}{k}
\left\{
u^{-n}+(-1)^k d^{-n}
\right\}.                                               \tag{13}
\]

Retaining only \(n=3,k=2\) gives
\[
b_2(d,s)
\ge
256s^3(d^{-3}+u^{-3}).                                   \tag{14}
\]

### 3.4 The whole actual support lies inside the convergence domain

Let \(S\) be the total weight of all other leaves involved before or after the reveal. From (9),
\[
|t|
\le
r_s:=d-\frac12+\frac Su.
\]
Condition (1) gives \(S+s<u^2\), so
\[
r_s<
\frac12-\frac su
=R_s.                                                   \tag{15}
\]

Thus the Taylor series converges uniformly and absolutely on **the entire support**, not merely on a typical-word event. Expectations and the series can be interchanged.

### 3.5 Actual-law moment cancellation

For the newly added independent increment \(\xi_r\),
\[
\begin{aligned}
\mathbb E\big[(t+\xi_r)^k-t^k\big]
&=
\sum_{\ell=1}^k
\binom{k}{\ell}
\mathbb E t^{k-\ell}\,
\mathbb E\xi_r^\ell\\
&\ge0.
\end{aligned}                                           \tag{16}
\]

Multiplying by the nonnegative coefficients in (12) proves nonnegative unconditional pair drift.

Retaining the \(k=2\) term and using
\[
\mathbb E\xi_r^2=\frac{w_r^2}{du}
\]
gives
\[
\boxed{
\mathbb E\Delta_{f_{ij}}
\ge
C_\star(d)\,w_i^3w_r^2.
}                                                       \tag{17}
\]
Summing over the core leaves proves (3). Successive reveals prove (4). Particle-hole complementation covers \(d<1/2\). \(\square\)

**This is not conditional convexity.** Away from the midpoint, the odd moments of the actual biased Bernoulli increments are part of the proof.

### 3.6 Explicit lower bound without a reveal remainder

Starting each selected pair from its two-site marginal gives
\[
\boxed{
\begin{aligned}
\mathbb E\Chi((G_A)_{II})
\ge{}&
\sum_{i\in C}\mathcal F(d,d,w_i)\\
&+
C_\star(d)
\sum_{i\in C}w_i^3
\sum_{k\in B\setminus\{i\}}w_k^2.
\end{aligned}
}                                                       \tag{18}
\]

Every base term is nonnegative, by (12) evaluated at \(t=d-1/2\), after reflection when necessary. It is strictly positive when \(w_i>0\).

For countably many leaves, (7) converges absolutely because the weights are summable. The strict gap supplies a uniform margin in (15), so bounded convergence extends these comparisons to increasing infinite stars. On a fixed compact legal sine parameter interval, the margins can be chosen uniformly.

---

## 4. An enumeration-free moment tool

Fix a selected pair and work after reflection with \(d\ge1/2\). Let
\[
M_k=\mathbb E t^k.
\]
Initialize
\[
M_k=\left(d-\frac12\right)^k.
\]
Adding a leaf updates the moments by
\[
M_k^{\rm new}
=
\sum_{\ell=0}^k
\binom{k}{\ell}M_{k-\ell}\mu_\ell(w),
\]
where \(\mu_0=1\) and \(\mu_\ell\) is given by (10).

Moments through degree \(D\) cost \(O(D^2)\) arithmetic operations per leaf, rather than \(2^{|B|}\) word evaluations.

For any
\[
r_s<R'<R_s,
\]
set
\[
L_D=\sum_{k=0}^D b_kM_k.
\]
Then
\[
L_D\le\mathbb E\mathcal F(d,\beta,s),
\]
and
\[
\boxed{
0\le
\mathbb E\mathcal F-L_D
\le
\left(\frac{r_s}{R'}\right)^{D+1}
\mathcal F\left(d,\frac12+R',s\right).
}                                                       \tag{19}
\]

Indeed, every omitted expected Taylor term is nonnegative, while its absolute size is at most \(b_kr_s^k\). Sum against the nonnegative generating series at \(R'\).

This is a quantitative approximation theorem, not a renamed unknown. Its gap dependence is explicit: the degree cost can deteriorate as the strict gap closes. No endpoint-uniform cost is claimed.

---

## 5. Spatial truncation inside the star

For a sine star define
\[
e=\min(d,1-d),
\qquad
\gamma_\star=e^2-\frac{c^2}{4}>0.
\]

For a selected pair, the other-leaf weight satisfies
\[
S\le\frac{c^2}{4}-s.
\]
Formula (7) implies
\[
\min(\beta,1-\beta)\ge e-\frac Se.
\]
Hence every independent-cell product in (11) is at least
\[
e\min(\beta,1-\beta)
\ge e^2-S
\ge\gamma_\star+s.
\]

Summing the absolute series gives
\[
|\mathcal F(d,\beta,s)|
\le\frac{4s^2}{\gamma_\star^2}.                           \tag{20}
\]

At the midpoint \(d=1/2\), all even \(n\) in (11) vanish:
\[
0\le
\mathcal F\left(\frac12,\beta,s\right)
\le\frac{4s^3}{\gamma_\star^3}.                           \tag{21}
\]

Because the **unconditional** pair expectations are nonnegative, adding long pairs to a star core has no negative one-sided cost. For integer \(R\ge2\), the omitted two-sided tail is bounded by
\[
\sum_{|i-j|\ge R}\mathbb E f_{ij}(G_{\rm star})
\le
\frac{8c^4}
{3\pi^4\gamma_\star^2(R-1)^3},                           \tag{22}
\]
or, at the midpoint,
\[
\sum_{|i-j|\ge R}\mathbb E f_{ij}(G_{\rm star})
\le
\frac{8c^6}
{5\pi^6\gamma_\star^3(R-1)^5}.                           \tag{23}
\]

These follow by bounding the two-sided inverse-power sums by integrals. They concern **star scores**, not the full two-parity score.

### A certified infinite-star lower bound

At
\[
c=\frac{19}{20},\qquad a=\frac1{40},\qquad d=\frac12,
\]
a nearest center-leaf pair has
\[
s=\frac{c^2}{\pi^2},
\]
and
\[
\mathcal F\left(\frac12,\frac12,s\right)
=
4\left\{
\frac{4s}{1-16s^2}-\operatorname{atanh}(4s)
\right\}.
\]
Using
\[
\sum_{n\in\mathbb Z,\ n\ {\rm odd}}|K(0,n)|^4
=\frac{c^4}{48},
\]
equation (18) gives
\[
\begin{aligned}
\mathbb E f_{\rm nearest}(G_{\rm infinite\ star})
&\ge
\mathcal F\left(\frac12,\frac12,s\right)
+
16384s^3\left(\frac{c^4}{48}-s^2\right)\\
&>0.26275.
\end{aligned}                                           \tag{24}
\]

The final strict inequality was certified by the exact-rational program. **It is not a claim about the full-line inverse score or the standard \(V_{m,L}\).**

---

## 6. Model-valid falsification tests

### 6.1 Unrestricted unconditional pair drift is false

Use
\[
\rho=\frac9{20},
\qquad c=\frac{19}{20},
\qquad a=\frac1{200},
\qquad I=A=\{0,3\},
\qquad r=4.
\]

These are genuine sine principal compressions. They can be embedded in the interval \(\{0,1,2,3,4\}\), with sites \(1,2\) unobserved. The two core sites have opposite parity, so
\[
\Chi=f_{03}.
\]

Set
\[
d=\frac{173}{400},
\qquad
z=-\frac{c\cos(3\pi/20)}{3\pi},
\]
\[
b_0=-\frac{c\sin(\pi/5)}{4\pi},
\qquad
b_3=\frac{c\cos(\pi/20)}{\pi}.
\]
The pair kernels conditional on the reveal are
\[
C_1=
\begin{pmatrix}d&z\\z&d\end{pmatrix}
-\frac1d
\begin{pmatrix}b_0\\b_3\end{pmatrix}(b_0,b_3),
\]
\[
C_0=
\begin{pmatrix}d&z\\z&d\end{pmatrix}
+\frac1{1-d}
\begin{pmatrix}b_0\\b_3\end{pmatrix}(b_0,b_3).
\]

Exact averaging gives
\[
\mathbb E\Delta_\Chi
=
d\,\mathcal F(C_1)
+(1-d)\,\mathcal F(C_0)
-\mathcal F(d,d,z^2),
\]
where \(\mathcal F(C)\) means (5) evaluated using the matrix’s two diagonals and squared off-diagonal.

The certified enclosure is
\[
\boxed{
\mathbb E\Delta_\Chi
\in[-0.000177080,-0.000177078]<0.
}                                                       \tag{25}
\]

Here \(d\) is the marginal reveal probability **after averaging the pair**. The conditional reveal probability given the pair was not frozen. All eight joint configurations are included.

This disproves arbitrary-sine, individual-pair zero-payment monotonicity. It does **not** disprove a full interval-core \(\Phi\) theorem, a summed interval-core \(\Chi\) theorem, or entropy concavity.

### 6.2 Even the star theorem cannot be conditioned on every old background

Take
\[
\rho=\frac12,\qquad
c=\frac{19}{20},\qquad
a=\frac1{2000},\qquad
d=\frac{951}{2000}.
\]

Use center \(0\), core leaf \(7\), old background leaves \(\{-1,1\}\) fixed to \(00\), and reveal leaf \(-3\). Put
\[
w=\frac{c^2}{\pi^2},
\qquad s=\frac w{49},
\qquad v=\frac w9,
\qquad
\beta=d+\frac{2w}{1-d}.
\]

After averaging the core pair, but still conditioning on that background, the drift is
\[
\begin{aligned}
&d\,\mathcal F(d,\beta-v/d,s)\\
&\quad +(1-d)\,\mathcal F(d,\beta+v/(1-d),s)
-\mathcal F(d,\beta,s).
\end{aligned}
\]
Its certified enclosure is
\[
[-0.00000074327,-0.00000074325]<0.                        \tag{26}
\]

Averaging **all four** old-background words instead gives
\[
\boxed{
\mathbb E\Delta_{f_{07}}
\in
[0.000013875271794819793250,\,
 0.000013875271794819793251]
>0.
}                                                       \tag{27}
\]

Thus the theorem genuinely uses actual-weight cancellation. It is not hidden conditional convexity or deletion of unfavorable words.

### Certificate method

The accompanying :chatgpt-content-reference{index="8"} uses standard-library Python only.

Its interval endpoints are integers on a \(10^{-80}\) grid, and every arithmetic operation rounds outward. It encloses \(\pi\) using Machin’s identity and alternating arctangent series. The sine and cosine arguments are at most \(\pi/5<1\), with alternating-series remainder bounds.

For logarithms it uses
\[
\log x
=
2\sum_{k=0}^{M-1}\frac{z^{2k+1}}{2k+1}+R_M,
\qquad
z=\frac{x-1}{x+1},
\]
with
\[
|R_M|
\le
\frac{2|z|^{2M+1}}
{(2M+1)(1-|z|^2)}.
\]

Thus (25)–(27), and the strict numerical inequality in (24), are interval certificates with explicit analytic tails—not rounded numerical signs.

---

## 7. Exact interface to the original Shannon entropy

The theorem eliminates observation loss **while the observed geometry remains a one-center star**. It also controls pair truncation inside that star.

It does **not** eliminate either completion to the full standard halo or the full-score core/pair truncation.

Here is an explicit interface retaining both unpaid terms.

At \(\rho=1/2\), let
\[
I=\{1,2\},\qquad
A_L=[1-L,2+L],
\]
and
\[
A_L^\star
=
\{2\}\cup(A_L\cap\{\text{odd sites}\}).
\]
Let \(\mathcal L_L(a)\) be the explicit right-hand side of (18) for this star and its one core pair.

Define the actual missing-parity energy
\[
\mathscr D_L
=
\mathbb E
\sum_{i\in I}
\sum_{r\in A_L\setminus A_L^\star}
|G_{A_L}(i,r)|^2.
\]

Apply the accepted S72 comparison only to the still-unpaid completion:
\[
V_{2,L}
\ge
\frac12
\left\{
\mathcal L_L(a)
-\Gamma_\Chi\eta_\delta\mathscr D_L
\right\}.                                               \tag{28}
\]
The accepted Ward bound supplies
\[
0\le\mathscr D_L\le2(2/\delta-4).                         \tag{29}
\]
These are applications of the packet’s existing comparison and expected row-energy bounds, not new signs for the missing parity. citeturn556790view0turn628152view0

Insert (28) into the accepted half-density \(c=19/20\) rate interface:
\[
\boxed{
\begin{aligned}
h''(a)\le{}&
-\frac1{50}-\mathcal L_L(a)
+\Gamma_\Chi\eta_\delta\mathscr D_L\\
&+2C_{\log}\widehat\tau(2)
+2\Gamma_\Chi\eta_\delta\widehat\tau(L+1).
\end{aligned}
}                                                       \tag{30}
\]

The terms have distinct roles:

- \(\mathscr D_L\) pays for the missing, nearby opposite-parity observations.
- \(2C_{\log}\widehat\tau(2)\) is the separate **full-score** core/pair truncation.
- The last term is the ordinary far observation tail.

None has been silently signed or removed.

### Remaining numerical budget

For
\[
c=.95,\qquad J=[.02,.03],\qquad\delta=.02,
\]
the two residual envelope payments as \(L\to\infty\) are approximately
\[
2C_{\log}(2/\delta-4)=486.92874,
\]
and
\[
2\Gamma_\Chi\eta_\delta(2/\delta-4)=107488.02023.
\]

Their total is
\[
107974.94896,
\]
before subtracting
\[
\frac1{50}+\mathcal L_\infty(a).
\]

The certified midpoint star lower bound in (24) cannot pay this envelope. This is a failure of this full-entropy certificate, not a counterexample to entropy concavity.

### Legal finite-to-rate passage

All new inequalities are finite-volume comparisons of actual score potentials at fixed \(a\), valid throughout every compact legal parameter interval. Equation (30) uses the already accepted S72 finite-to-rate interface. No entropy-value error is differentiated, and no moving halo/background derivative is dropped. citeturn628152view0turn122528view0

Passing \(L\to\infty\) in this bound is justified by the star convergence proved above, the uniform cap (29), and the vanishing accepted far tail.

For a future success
