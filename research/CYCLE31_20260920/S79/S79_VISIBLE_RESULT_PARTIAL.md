# Source status: tool-visible prefix, truncated at 20000 characters; not a complete manuscript.

# S79 result — paid-shell second-chaos identity and a universal obstruction

## Status

The finite consecutive-Fourier midpoint theorem is **not yet proved** for arbitrary \(m\). The main progress is nevertheless structural and all-size:

1. An exact Boolean-number-operator integration by parts converts the conditional Rademacher chaos into an output log-density covariance plus the already audited adjacent-mask Jeffreys energy.
2. Uniformization inside the true \(|T|\)-shell gives an exact **paid-shell identity**
   \[
   H_W''=H_\circ''+\frac{\mathfrak D_W-4r\,\Delta\mathcal E_W}{r^2}.
   \]
   Here \(\mathfrak D_W\) is an explicit signed shell-KL covariance and \(\Delta\mathcal E_W\) is an actual Jeffreys contraction budget, not a guessed uniform reference.
3. Midpoint concavity is false for arbitrary layer-doubly-stochastic channels. An exact interval computation gives a positive-curvature example at \(m=36,c=4/5\).
4. That counterexample violates a cross-layer deletion intertwining satisfied by every exterior-power unitary channel. The actual consecutive-Fourier family additionally has a Cauchy/full-spark structure and complementary-minor symmetry.
5. A fully shell-symmetrized \(2m\)-site comparison law has an explicit all-size, all-\(c\), strictly negative curvature margin. The unresolved target is thereby reduced to two concrete relative-entropy curvature terms.

I use the audited S76 acceleration, \(D\)-sector theorem, and Jeffreys representation as inherited premises. citeturn637393view0turn637393view1

All logarithms below are natural, and unless stated otherwise every derivative is with respect to \(a\) at
\[
a_0=\frac{1-c}{2},\qquad
k=c^2,\qquad
r=\frac{1-k}{4},\qquad
s=\frac{1+k}{4},\qquad
\ell=\log\frac sr.
\]

---

## 1. Exact integration by parts for the second chaos

Put
\[
\sigma_i=2Y_i-1,\qquad \tau_i=2Z_i-1.
\]
For a layer-preserving channel \(W\), define the output density relative to the uniform law on \((y,t)\) by
\[
\Lambda_k(y,t)
=
\sum_z W(z,t)\prod_{i=1}^m(1-k\sigma_i\tau_i),
\qquad
Q_W(y,t)=4^{-m}\Lambda_k(y,t).
\]

Introduce the Boolean number operator acting on the \(y\)-coordinate:
\[
N_y f(y,t)
=
\frac12\sum_{i=1}^m\bigl(f(y,t)-f(y^{(i)},t)\bigr).
\]
Walsh expansion gives the exact identity
\[
N_y\Lambda_k=k\,\partial_k\Lambda_k.
\]

Let
\[
\delta(y,t)=\mathbb E[D\mid Y=y,T=t].
\]

### Lemma 1: exact posterior formula

One has
\[
\boxed{
\delta\,\Lambda_k
=
2mr\,\Lambda_k-\beta N_y\Lambda_k,
\qquad
\beta=\frac{1-k^2}{2k}.}
\]

### Proof

At a fixed input word,
\[
P_k(y,z)=4^{-m}\prod_i(1-k\sigma_i\tau_i).
\]
Since \(D\) is the number of coordinates with \(\sigma_i\tau_i=1\),
\[
\begin{aligned}
k\partial_k\log P_k(y,z)
&=-\frac{kD}{1-k}+\frac{k(m-D)}{1+k}\\
&=\frac{km}{1+k}-\frac{2kD}{1-k^2}.
\end{aligned}
\]
Average this identity over the posterior law of \(Z\) given \((Y,T)\):
\[
\frac{N_y\Lambda_k}{\Lambda_k}
=
\frac{km}{1+k}
-
\frac{2k\delta}{1-k^2}.
\]
Solving for \(\delta\), and using \(2r=(1-k)/2\), proves the formula.

This calculation retains the complete output density and posterior. No \(Y\)-marginal or Hamming layer has been frozen.

---

## 2. The orientation path realizes \(C_X\) exactly

Consider the local pair perturbation
\[
P_\theta(00)=r-\theta,\qquad
P_\theta(11)=r+\theta,\qquad
P_\theta(01)=P_\theta(10)=s.
\]
Equivalently, its one-pair density relative to \(1/4\) is
\[
1-k\sigma_i\tau_i+2\theta(\sigma_i+\tau_i).
\]

At \(\theta=0\),
\[
\frac{\dot P_\theta}{P_0}=\frac Xr,
\qquad
\frac{\ddot P_\theta}{P_0}=\frac{X^2-D}{r^2}.
\]
The second equality is precisely the conditional second-Rademacher chaos
\[
X^2-D=2\sum_{i<j,\ i,j\in E}\epsilon_i\epsilon_j.
\]

Because \(W\) preserves \(|Z|\),
\[
X=|Y|+|Z|-m=|Y|+|T|-m
\]
is output-measurable. Therefore
\[
\dot\Lambda=\frac Xr\Lambda,
\qquad
\ddot\Lambda
=
\frac{X^2-\delta}{r^2}\Lambda.
\]
Using Lemma 1 gives
\[
\boxed{
\ddot\Lambda
=
\frac{X^2-2mr}{r^2}\Lambda
+
\frac{\beta}{r^2}N_y\Lambda.}
\]

Define the adjacent-mask edge energy
\[
\mathcal E_W
=
\left\langle N_y\Lambda,\log\Lambda\right\rangle_0,
\qquad
\langle f\rangle_0=4^{-m}\sum_{y,t}f(y,t).
\]
The audited Jeffreys representation is
\[
\mathcal E_W
=
\frac14\sum_i\mathbb E_{y\sim\mathrm{Unif}}
J\!\left(P_y^W,P_{y^{(i)}}^W\right)
=
\frac{mk\ell}{2}(1-\eta_J).
\]

For entropy,
\[
H''=-\left\langle\ddot\Lambda,\log\Lambda\right\rangle_0
-\left\langle\frac{\dot\Lambda^2}{\Lambda}\right\rangle_0.
\]
Since
\[
\mathbb E_QX^2=2mr,
\]
and the input second chaos is orthogonal to every function of \(D\), the input entropy along the orientation path has curvature \(-2m/r\). Consequently:

### Theorem 2: exact second-chaos decomposition

For every layer-preserving doubly stochastic \(W\),
\[
\boxed{
C_X
=
-\frac1{r^2}\operatorname{Cov}_{Q_W}
       \!\left(X^2,\log\Lambda_k(Y,T)\right)
-\frac{\beta}{r^2}\mathcal E_W.}
\]

Equivalently,
\[
\boxed{
C_X
=
-\frac1{r^2}\operatorname{Cov}_{Q_W}
       \!\left(X^2,\log\Lambda_k\right)
-
4m\ell\,\frac{1+k}{1-k}(1-\eta_J).}
\]

Thus the second chaos consists of:

- a signed output log-density covariance;
- a definite negative payment from the same adjacent-mask Jeffreys energy that appears in S76.

This is an averaged identity under the actual law, not a pointwise bound.

---

## 3. Full \(a\)-curvature in number-operator form

For the actual \(a\)-path, the audited acceleration says
\[
\Lambda_{aa}
=
\left[
\frac{X^2-\delta}{r^2}
+
\frac{\delta-2mr}{rs}
\right]\Lambda.
\]
Substituting Lemma 1 and simplifying gives a particularly useful identity:
\[
\boxed{
\Lambda_{aa}
=
\frac{X^2-2mr}{r^2}\Lambda
+
\frac4r N_y\Lambda.}
\]

Hence the full output entropy curvature is
\[
\boxed{
H_W''
=
-\frac1{r^2}
 \operatorname{Cov}_{Q_W}\!\left(X^2,\log\Lambda_k\right)
-\frac4r\mathcal E_W
-\frac{2m}{r}.}
\tag{3.1}
\]

Algebraically this agrees with
\[
H_W''=C_X-\frac{2m}{r}+4m\ell(1-\eta_J),
\]
but (3.1) exposes the exact mechanism: the second-chaos covariance must be paid by edge entropy dissipation and the independent-pair curvature.

---

# 4. The paid-shell theorem

Define the genuine layer randomizer
\[
W_\circ(z,t)
=
\frac{\mathbf 1_{\{|z|=|t|\}}}{\binom m{|t|}}.
\]
For every layer-stochastic \(W\),
\[
WW_\circ=W_\circ.
\]
Thus \(Q_\circ=Q_WW_\circ\) is an actual postprocessing of \(Q_W\), not an artificial reference law.

Write
\[
N=|T|,\qquad
\mu(y,n)=Q_W(Y=y,N=n).
\]
The distribution \(\mu\) is independent of \(W\), because every admissible channel preserves \(|Z|\).

For \(t\) in the \(n\)-th layer, let
\[
q^W_{y,n}(t)
=
Q_W(T=t\mid Y=y,N=n),
\qquad
u_n(t)=\binom mn^{-1},
\]
and define the conditional shell anisotropy
\[
j_W(y,n)
=
D(q^W_{y,n}\|u_n).
\]

Finally put
\[
\Delta\mathcal E_W
=
\mathcal E_W-\mathcal E_\circ.
\]

Because \(Q_\circ\) is obtained by postprocessing \(Q_W\), contraction of both directions of every adjacent-mask KL divergence gives
\[
\boxed{\Delta\mathcal E_W\ge0.}
\]
More explicitly,
\[
\Delta\mathcal E_W
=
\frac{mk\ell}{2}(\eta_\circ-\eta_W).
\]

## Conditional entropy/reference correction

For fixed \((y,n)\), \(\Lambda_\circ(y,t)\) is constant over the \(n\)-th layer. Therefore
\[
\begin{aligned}
\mathbb E_{Q_W}
 [\log\Lambda_W\mid Y=y,N=n]
&=
\log\Lambda_\circ(y,n)
+
D(q^W_{y,n}\|u_n)\\
&=
\log\Lambda_\circ(y,n)+j_W(y,n).
\end{aligned}
\]
This is the exact reference correction introduced by conditioning. It is neither dropped nor replaced by a global uniform output law.

Since \(X=|y|+n-m\) is constant under this conditional law,
\[
\operatorname{Cov}_{Q_W}(X^2,\log\Lambda_W)
-
\operatorname{Cov}_{Q_\circ}(X^2,\log\Lambda_\circ)
=
\operatorname{Cov}_{\mu}(X^2,j_W).
\]

Define the signed geometric defect
\[
\boxed{
\mathfrak D_W
=
-\operatorname{Cov}_{\mu}(X^2,j_W).}
\]
Only the positive part of \(\mathfrak D_W\) is dangerous: it means the within-shell spatial information \(j_W\) is concentrated preferentially near small \(|X|\).

### Theorem 3: paid-shell second-chaos identity

For every \(m\), every \(0<c<1\), and every layer-doubly-stochastic \(W\),
\[
\boxed{
C_X(W)
=
C_X(W_\circ)
+
\frac{\mathfrak D_W-\beta\Delta\mathcal E_W}{r^2}.}
\tag{4.1}
\]

For the full midpoint curvature,
\[
\boxed{
H_W''
=
H_\circ''
+
\frac{\mathfrak D_W-4r\,\Delta\mathcal E_W}{r^2}.}
\tag{4.2}
\]

Equivalently, let
\[
\mathcal J_W(a)
=
D(Q_W(a)\|Q_\circ(a))
=
H_\circ(a)-H_W(a).
\]
Then
\[
\boxed{
\mathcal J_W''(a_0)
=
\frac{4r\,\Delta\mathcal E_W-\mathfrak D_W}{r^2}
=
\frac1{r^2}\operatorname{Cov}_{\mu}(X^2,j_W)
+\frac4r\Delta\mathcal E_W.}
\tag{4.3}
\]

Thus the precise paid-shell condition is
\[
\boxed{
\mathfrak D_W\le4r\,\Delta\mathcal E_W.}
\tag{PS}
\]
Under (PS),
\[
H_W''\le H_\circ''.
\]

The payment \(\Delta\mathcal E_W\) is a portion of the same audited Jeffreys budget:
\[
\mathcal E_{\mathrm{id}}-\mathcal E_\circ
=
(\mathcal E_{\mathrm{id}}-\mathcal E_W)
+
(\mathcal E_W-\mathcal E_\circ).
\]
The first part is the loss already appearing in the S76 \(D\)-sector; the second part is exactly the payment in (4.2).

---

## 5. Why a generic norm bound cannot close

At midpoint,
\[
X=\sum_{i=1}^m\xi_i,
\]
where
\[
\mathbb P(\xi_i=1)=\mathbb P(\xi_i=-1)=r,
\qquad
\mathbb P(\xi_i=0)=2s.
\]
Hence
\[
\operatorname{Var}(X^2)
=
2mr+(8m^2-12m)r^2.
\]

Also
\[
0\le j_W(y,n)\le\log\binom mn\le m\log2.
\]
Therefore Cauchy–Schwarz gives only
\[
\begin{aligned}
|\operatorname{Cov}(X^2,j_W)|
&\le
\sqrt{\operatorname{Var}(X^2)\operatorname{Var}(j_W)}\\
&\le
\frac{m\log2}{2}
\sqrt{2mr+(8m^2-12m)r^2}\\
&=O_c(m^2).
\end{aligned}
\]
On the other hand,
\[
4r\,\Delta\mathcal E_W
\le4r\mathcal E_W
\le2mrk\ell
=O_c(m).
\]
Thus a generic norm, hypercontractive, or variance estimate immediately loses one power of \(m\). The required cancellation is specifically geometric.

---

# 6. Arbitrary layer-bistochastic channels: exact counterexample

The universal generalization is false.

Take
\[
m=36,\qquad c=\frac45,\qquad
r=\frac9{100},\qquad
s=\frac{41}{100},
\]
and define a layer channel by
\[
W_n=
\begin{cases}
I_n,&n\in\{16,17,18,19,20\},\\[2mm]
\displaystyle \frac1{\binom{36}{n}}\mathbf 1\mathbf 1^{\mathsf T},
&\text{otherwise}.
\end{cases}
\]
Every block is doubly stochastic. The channel is layer-preserving and complement-symmetric.

## Exact finite-sum certificate

For
\[
h=|y|,\qquad n=|z|,\qquad b=|y\cap z|,
\]
put
\[
d=m-h-n+2b,\qquad x=h+n-m,
\]
\[
p_{hnb}=r^d s^{m-d},
\]
and
\[
A_{hnb}
=
\frac{x^2-d}{r^2}
+
\frac{d-2mr}{rs}.
\]
The multiplicity of the atom is
\[
M_{hnb}
=
\binom mh\binom hb\binom{m-h}{n-b}.
\]

For an identity layer,
\[
\mathcal H_{n,\mathrm{id}}''
=
-\sum_{h,b}
M_{hnb}p_{hnb}
\left(
A_{hnb}\log p_{hnb}
+\frac{x^2}{r^2}
\right).
\]

For a mixed layer define
\[
P_{hn}
=
\sum_b
\binom hb\binom{m-h}{n-b}p_{hnb},
\]
\[
P_{hn}^{(2)}
=
\sum_b
\binom hb\binom{m-h}{n-b}p_{hnb}A_{hnb}.
\]
Then
\[
\mathcal H_{n,\mathrm{mix}}''
=
-\sum_h\binom mh
\left[
P_{hn}^{(2)}
\log\frac{P_{hn}}{\binom mn}
+
P_{hn}\frac{x^2}{r^2}
\right].
\]

At \(c=4/5\), every coefficient and every logarithm argument is rational. Eighty-digit interval evaluation gives
\[
\boxed{
H_W''(a_0)\in
[10.4745311384739813781852692400271678308749564,\,
 10.4745311384739813781852692400271678308749565].
}
\]
In particular,
\[
\boxed{H_W''(a_0)>0.}
\]

For comparison, the fully shell-mixed channel has
\[
H_\circ''=-294.2957856094156.
\]
Resolving the two terms in (4.2) gives
\[
\mathfrak D_W=6.130529639058225,
\]
\[
4r\,\Delta\mathcal E_W=3.661890073400335,
\]
so
\[
\mathfrak D_W-4r\,\Delta\mathcal E_W
=2.4686395656578903>0.
\]
Since \(r^2=0.0081\), this produces the curvature increase
\[
\frac{2.4686395656578903}{r^2}
=
304.770316747888\ldots,
\]
which overwhelms the negative shell baseline.

### Consequences

This disproves:

- midpoint entropy concavity for all layer-doubly-stochastic channels;
- the paid-shell inequality (PS) under layer bistochasticity alone;
- any closure using only the individual layer assumptions.

It does **not** disprove the consecutive-Fourier channel, nor even a theorem for arbitrary exterior-power unitary channels.

---

# 7. The missing exterior structure

The counterexample switches abruptly between identity and complete mixing on adjacent particle-number layers. Exterior channels cannot do that.

For an \(m\times m\) unitary \(U\), let
\[
W_n(A,B)=|\det U_{A,B}|^2,
\qquad |A|=|B|=n.
\]
Define the uniform deletion kernel
\[
D_n(A,C)
=
\frac1n\mathbf 1_{\{C\subset A,\ |C|=n-1\}}.
\]

### Theorem 4: exterior deletion intertwining

Every exterior-power unitary channel satisfies
\[
\boxed{
W_nD_n=D_nW_{n-1},
\qquad 1\le n\le m.}
\tag{EC}
\]

Equivalently,
\[
\sum_{B\supset C}|\det U_{A,B}|^2
=
\sum_{A'\subset A}|\det U_{A',C}|^2.
\]

### Proof

Fix \(A\), with \(|A|=n\), and \(C\), with \(|C|=n-1\). For every column \(j\), let
\[
d_j=\det U_{A,C\cup\{j\}},
\]
where \(d_j=0\) for \(j\in C\).

Expanding in the added column,
\[
d_j=\sum_{i\in A}c_iU_{ij},
\]
where the \(c_i\)'s are signed cofactors
\[
c_i=\pm\det U_{A\setminus\{i\},C}.
\]
Since the rows of \(U\) are orthonormal,
\[
\sum_j|d_j|^2
=
\sum_{i\in A}|c_i|^2.
\]
The left side is the sum over \(B\supset C\); the right side is the sum over \(A'\subset A\). Division by \(n\) gives (EC).

The hybrid counterexample fails (EC). At the boundary \(n=16\),
\[
W_{16}=I,\qquad W_{15}=W_{\circ,15}.
\]
For \(C\not\subset A\),
\[
(W_{16}D_{16})(A,C)=0,
\]
whereas
\[
(D_{16}W_{15})(A,C)=\binom{36}{15}^{-1}>0.
\]

Thus the exact counterexample identifies a genuine missing hypothesis: cross-layer exterior coherence.

---

## 8. Consecutive Fourier: Cauchy and full-spark properties

Index even and odd sites by \(a,b\in\{0,\dots,m-1\}\). For the projection onto the first \(m\) Fourier modes,
\[
\begin{aligned}
(U_m)_{ab}
&=
\frac1m\sum_{\ell=0}^{m-1}
e^{\pi i\ell(2(a-b)-1)/m}\\
&=
\frac{2}
 {m\left(1-\omega^{-1}\zeta_a\zeta_b^{-1}\right)},
\end{aligned}
\]
where
\[
\omega=e^{\pi i/m},
\qquad
\zeta_a=e^{2\pi ia/m}.
\]

This is a Cauchy matrix:
\[
(U_m)_{ab}
=
\frac{2/m}{1-x_ay_b},
\qquad
x_a=\omega^{-1}\zeta_a,\quad y_b=\zeta_b^{-1}.
\]
The \(x_a\)'s and \(y_b\)'s are distinct, and \(x_ay_b\ne1\). The Cauchy determinant formula therefore shows that every square minor is nonzero:
\[
\boxed{
|\det (U_m)_{A,B}|^2>0
\quad\text{for every }|A|=|B|.}
\]

Jacobi's complementary-minor identity for a unitary gives
\[
\boxed{
W_n(A,B)
=
W_{m-n}(A^c,B^c).}
\]

Hence the actual family satisfies all of:

- layer bistochasticity;
- exterior deletion coherence (EC);
- strict positivity on every layer;
- particle-hole complementary-minor symmetry.

The arbitrary-channel counterexample satisfies only the first and the last.

A precise remaining geometric conjecture is now
\[
\boxed{
-\operatorname{Cov}_{\mu}
 \left(X^2,j_{U_m}(Y,N)\right)
\le
4r\bigl(\mathcal E_{U_m}-\mathcal E_\circ\bigr)
}
\tag{F-PS}
\]
for every \(m\) and \(0<c<1\).

This is neither a pointwise atom estimate nor a generic norm bound. It is the exact averaged inequality required to show
\[
H_{U_m}''\le H_\circ''.
\]

---

# 9. A strict total-shell benchmark

This section is a comparison theorem only; it is not an identification of count entropy with the full configuration entropy.

Let \(S=|Y|+|T|\), and define \(\widehat Q_a\) by retaining the actual law of \(S\) but making the full \(2m\)-site configuration uniform conditional on \(S\). Its full Shannon entropy is
\[
\widehat H(a)
=
H(S_a)
+
\mathbb E\log\binom{2m}{S_a}.
\]

The one-pair count generating polynomial factors:
\[
v+2qx+ux^2
=
(1-a+ax)(1-a-c+(a+c)x).
\]
Thus
\[
S_a
\overset d=
\sum_{i=1}^m B_i(a)
+
\sum_{i=1}^m \widetilde B_i(a+c),
\]
with all \(2m\) Bernoulli variables independent.

The entropy \(H(S_a)\) is concave along this affine parameter path by the Shepp–Olkin theorem. citeturn637393view4

Let
\[
f(j)=\log\binom{2m}{j}.
\]
Multilinearity of expectations in the Bernoulli parameters gives
\[
\frac{d^2}{da^2}\mathbb Ef(S_a)
=
\sum_{i\ne j}
\mathbb E\bigl[\Delta^2 f(S_{-ij})\bigr].
\]
For \(0\le t\le2m-2\),
\[
\Delta^2f(t)
=
\log
\frac{(2m-t-1)(t+1)}
     {(2m-t)(t+2)}.
\]
Writing \(x=t+1\), the ratio
\[
\frac{x(2m-x)}
 {(x+1)(2m-x+1)}
\]
is maximized at \(x=m\). Therefore
\[
\Delta^2f(t)
\le
2\log\frac{m}{m+1}.
\]
There are \(2m(2m-1)\) ordered pairs, hence:

### Theorem 5: strict total-shell concavity

For every \(m\ge1\), every \(0<c<1\), and every \(0<a<1-c\),
\[
\boxed{
\widehat H''(a)
\le
-4m(2m-1)\log\!\left(1+\frac1m\right)<0.}
\tag{9.1}
\]

After normalization by all \(2m\) sites, the explicit margin tends to \(-4\).

Now define
\[
\mathcal K(a)
=
D(Q_\circ(a)\|\widehat Q_a)
=
\widehat H(a)-H_\circ(a).
\]
Because the shell partitions are nested,
\[
\widehat H(a)-H_W(a)
=
\mathcal K(a)+\mathcal J_W(a).
\]
Therefore
\[
\boxed{
H_W''
=
\widehat H''
-
\mathcal K''
-
\mathcal J_W''.}
\tag{9.2}
\]

Combining (4.3), (9.1), and (9.2), the actual finite cyclic midpoint target reduces to a concrete two-defect obligation:
\[
\mathcal K''(a_0)
+
\frac{4r\,\Delta\mathcal E_W-\mathfrak D_W}{r^2}
\ge0.
\]
Proving the two terms separately nonnegative would be sufficient but is stronger than necessary.

---

# 10. Consecutive-Fourier diagnostics

The following are diagnostics only. They are not used as an all-size proof.

At \(c=0.95\), for the actual consecutive-Fourier exterior channel:

| \(m\) | \(H_{U_m}''\) | \(H_\circ''\) | \(\mathcal J_{U_m}''\) | \(\mathfrak D/(4r\Delta\mathcal E)\) |
|---:|---:|---:|---:|---:|
| 2 | \(-122.9790241\) | \(-122.9790241\) | \(0\) | — |
| 3 | \(-165.7990434\) | \(-163.2149371\) | \(2.5841063\) | \(0.8771849\) |
| 4 | \(-202.7869594\) | \(-194.1550643\) | \(8.6318951\) | \(0.8561251\) |
| 5 | \(-236.2243239\) | \(-218.1276088\) | \(18.0967150\) | \(0.8396198\) |
| 6 | \(-267.4086677\) | \(-236.8313167\) | \(30.5773510\) | \(0.8265936\) |
| 7 | \(-297.1228842\) | \(-251.5330276\) | \(45.5898566\) | \(0.8162022\) |

Thus the paid-shell inequality holds in these tested cases, with a nontrivial margin. The execution also checked:

\[
\max\|UU^*-I\|_\infty
=1.89\times10^{-15},
\]
\[
\max\|W_nD_n-D_nW_{n-1}\|_\infty
=1.89\times10^{-15},
\]
\[
\text{maximum curvature-identity residual}
=7.39\times10^{-13},
\]
\[
\text{maximum paid-shell identity residual}
=5.26\times10^{-13}.
\]

These values reproduce the supplied \(m=2,\ldots,5\) curvature diagnostics and extend the shell comparison through \(m=7\), but no sign is extrapolated to arbitrary \(m\).

---

# 11. Ledger

## PROVED

1. **Exact posterior/number-operator identity**
   \[
   \delta\Lambda=2mr\Lambda-\frac{1-k^2}{2k}N_y\Lambda.
   \]

2. **Exact second-chaos decomposition**
   \[
   C_X
   =
   -r^{-2}\operatorname{Cov}(X^2,\log\Lambda)
   -\beta r^{-2}\mathcal E_W.
   \]

3. **Exact full-curvature number-operator formula**
   \[
   H_W''
   =
   -r^{-2}\operatorname{Cov}(X^2,\log\Lambda)
   -4r^{-1}\mathcal E_W
   -2m/r.
   \]

4. **Paid-shell theorem**
   \[
   H_W''
   =
   H_\circ''
   +
   r^{-2}(\mathfrak D_W-4r\Delta\mathcal E_W).
   \]

5. **Equivalent relative-entropy curvature formula**
   \[
   \mathcal J_W''
   =
   r^{-2}(4r\Delta\mathcal E_W-\mathfrak D_W).
   \]

6. **Generic \(O(m^2)\) estimates are quantitatively insufficient**, whereas the available Jeffreys payment is only \(O(m)\) for fixed \(c\).

7. **Exact arbitrary-channel obstruction:** a valid layer-doubly-stochastic channel at \(m=36,c=4/5\) has
   \[
   H_W''>10.47453113847398.
   \]

8. **Exterior deletion coherence**
   \[
   W_nD_n=D_nW_{n-1}
   \]
   for every exterior-power unitary channel.

9. **Actual consecutive-Fourier structure:** Cauchy form, all minors nonzero, complement-minor symmetry, and deletion coherence.

10. **Strict total-shell benchmark**
    \[
    \widehat H''
    \le
    -4m(2m-1)\log(1+1/m).
    \]

## DISPROVED

1. Midpoint concavity for every layer-doubly-stochastic channel.
2. A universal paid-shell inequality based only on layer bistochasticity.
3. Any argument that treats the Hamming layers independently and ignores cross-layer exterior coherence.

The counterexample does not disprove an arbitrar
