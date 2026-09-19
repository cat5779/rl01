# S73 RESULT — parity-ensemble sign functional and exact obstruction

## Scope and status

This note treats the half-density case \(\rho=1/2\).  It does **not**
claim the full infinite sine-process concavity theorem.  It supplies:

1. a legitimate all-even conditional projection law, without conditioning
   on a prescribed probability-zero infinite word;
2. an exact finite cyclic representation of the **combined**
   parity-ensemble term and conditional-information remainder;
3. a determinant/overlap representation whose hidden overlap is
   conditionally Poisson-binomial;
4. a compensated second-derivative identity retaining all moving weights,
   normalization, Fisher loss, acceleration, and third-cumulant terms;
5. an exact actual-cyclic obstruction to the stronger conjecture that the
   bistochastic entropy gain is concave;
6. a strict four-site midpoint concavity theorem despite that obstruction;
7. a rederivation of the effective-contrast range showing that the accepted
   contraction baseline applies on the whole legal bias interval whenever
   \[
      \frac{37}{40}<c\le \frac{74}{77}.
   \]

The remaining infinite-volume sign is isolated explicitly in Sections 7–9.

Throughout, logarithms are natural and \(h_b\) is binary entropy in nats.

---

## 1. Source and hypothesis map

The accepted QWE09 input used here is only the following.

* True finite sine compressions are contractions, not projections.
* At half density the finite conditional odd kernels have the exact
  contraction form
  \[
  M_y=bI+\alpha R_y,\qquad
  b=p-\frac{c^2}{4p},\qquad
  \alpha=\frac{c^2}{4p(1-p)},\qquad 0\le R_y\le I,
  \]
  including the leakage term when the parity block is only a contraction.
* The correct observed-mask weights move with \(p=a+c/2\), and all three
  terms \(wF''+2w'F'+w''F\) must be retained.
* The fixed-positive-gap second-response transfer identifies the true
  entropy-rate curvature and the mixed parity response from finite actual-law
  witnesses.
* The only baseline imported is
  \[
  \frac{d^2}{db^2}H(\operatorname{DPP}(bI+(37/40)R))
     \le-\frac{\dim R}{50},
  \quad 0\le R\le I,\quad 0<b<3/40.
  \]

Repository source: `research/CYCLE23_20260919/S73/PACKET.md`, especially
lines 1035–1101, 1127–1239, 1241–1260, 1586–1643.

No Gaussian, spin-glass, z-measure, RIP, or endpoint-uniform theorem is
imported.  The new arguments below use only DPP spectral sampling,
Cauchy–Binet, elementary entropy differentiation, and finite conditional
expectation.

---

## 2. Legitimate unitary all-even conditioning

### Theorem 2.1 — finite/infinite bipartite projection disintegration

Let \(E,O\) be finite sets of the same size, or countably infinite sets, and
let \(U:\ell^2(O)\to\ell^2(E)\) be unitary.  Put
\[
 Q=\frac12\begin{pmatrix}I_E&U\\ U^*&I_O\end{pmatrix}.
\]
Then \(Q\) is an orthogonal projection.  If \(X\sim\operatorname{DPP}(Q)\),
then:

1. \(X_E\) is iid fair Bernoulli;
2. a regular conditional law of \(X_O\) given \(X_E=x\) is
   \[
      \operatorname{DPP}(P_x),\qquad
      P_x=U^*\operatorname{diag}(1-x)U.
   \]

In the countably infinite case this statement is almost sure as a regular
conditional distribution.  It does not assert that the event
\(\{X_E=x\}\) has positive probability.

#### Proof

The restriction \(Q_{EE}=I/2\) makes \(X_E\) iid fair.

For every \(x\), \(\operatorname{diag}(1-x)\) is an orthogonal projection, so
\(P_x\) is an orthogonal projection.  On a discrete countable space it
therefore defines a DPP.  Its finite-cylinder probabilities are measurable
in \(x\): each matrix entry is an absolutely convergent column product by
Cauchy–Schwarz.

Construct a joint law by first sampling iid fair \(X_E\), then sampling
\(X_O\mid X_E=x\) from \(\operatorname{DPP}(P_x)\).  It is enough to compare
all finite inclusion correlations.  For finite \(A\subset E\),
\(B\subset O\), Cauchy–Binet gives
\[
\begin{aligned}
 \mathbb E\!\left[\prod_{i\in A}X_i\det(P_X)_B\right]
 &=\sum_{\substack{S\subset E\setminus A\\|S|=|B|}}
      |\det U_{S,B}|^2\,2^{-|A|-|S|}\\
 &=2^{-|A|-|B|}
   \det\!\left(I_B-U_{A,B}^*U_{A,B}\right).
\end{aligned}
\]
On the other hand, the block determinant formula gives
\[
 \det Q_{A\cup B}
 =2^{-|A|-|B|}
   \det\!\left(I_B-U_{A,B}^*U_{A,B}\right).
\]
Thus every finite inclusion correlation agrees with that of
\(\operatorname{DPP}(Q)\), which determines the finite-dimensional law.
The constructed kernel \(x\mapsto\operatorname{DPP}(P_x)\) is therefore a
version of the regular conditional law. \(\square\)

### Application to the half-density sine projection

For the infinite half-density sine projection,
\[
 Q_{EE}=Q_{OO}=I/2,\qquad U=2Q_{EO}.
\]
The identity \(Q^2=Q\) gives \(UU^*=U^*U=I\).  Theorem 2.1 therefore applies.
For a finite true Toeplitz compression, by contrast, the parity block is only
a contraction and the conditional kernel is not a projection.  Nothing
below replaces a true finite Toeplitz kernel by a projection.

### Observed all-even conditioning

Let \(0<c<1\), \(0<a<1-c\), and independently observe
\[
 \Pr(Y_i=1\mid X_i)=a+cX_i,\qquad p=a+c/2.
\]
Theorem 2.1 and the product posterior of \(X_E\) imply that a regular
conditional odd-output law given all observed evens \(Y_E=y\) is the DPP
with kernel
\[
 M_y=U^*\operatorname{diag}(q_{y_i})U,
\]
where
\[
 q_1=p-\frac{c^2}{4p},\qquad
 q_0=p+\frac{c^2}{4(1-p)}.
\]
Equivalently,
\[
 M_y=bI+\alpha U^*\operatorname{diag}(1-y)U,
 \quad b=p-\frac{c^2}{4p},\quad
 \alpha=\frac{c^2}{4p(1-p)}.
\]
This is the unitary, full-infinite counterpart of the accepted finite
contraction formula.  It is obtained as a regular conditional law, not by
conditioning on an arbitrarily chosen infinite word.

---

## 3. Exact cyclic representation of the combined remainder

Fix \(m\ge1\) and a unitary \(U\in\mathbb C^{m\times m}\).  The cyclic
consecutive-Fourier projection on \(2m\) sites has
\[
 Q=\frac12\begin{pmatrix}I&U\\U^*&I\end{pmatrix}.
\]

Given the even latent word \(x\), the odd latent projection is
\(U^*\operatorname{diag}(1-x)U\).  Spectral sampling of the noisy odd DPP
introduces a binary spectral subset \(Z\): conditional on \(x\),
\[
 \Pr(Z_i=1\mid x_i)=a+c(1-x_i).
\]
The odd spatial output, denoted \(T\), is obtained from \(Z\) through
\[
 W_U(z,t)=
 \begin{cases}
   |\det U_{z,t}|^2,&|z|=|t|,\\
   0,&|z|\ne|t|.
 \end{cases}
\]
Cauchy–Binet and unitarity show that every Hamming-layer block of \(W_U\)
is doubly stochastic.

After averaging the iid fair \(x_i\), the pairs \((Y_i,Z_i)\) are iid with
table
\[
 q_a(y,z)=
 \begin{pmatrix}
 v&q\\ q&u
 \end{pmatrix}_{y,z},
\]
where
\[
 d=\frac{c^2}{4},\qquad
 u=p^2-d=a(a+c),
\]
\[
 v=(1-p)^2-d=(1-a)(1-a-c),\qquad
 q=p(1-p)+d.
\]
The determinant is parameter-independent:
\[
 uv-q^2=-d=-\frac{c^2}{4}.
\]

### Theorem 3.1 — exact combined law

Generate iid pairs \((Y_i,Z_i)\) with table \(q_a\), then sample
\(T\) from \(W_U(Z,\cdot)\).  The resulting \((Y,T)\) is exactly the
even/odd observed configuration of the \(2m\)-site cyclic projection model.

Consequently,
\[
 H(Y,T)=H(Y,Z)+G_{m,U}(a,c),
\]
where
\[
 G_{m,U}=H(Y,T)-H(Y,Z)\ge0.
\]
The term \(G_{m,U}\) is the entropy increase caused by the exterior-power
measurement.  This identity already combines the parity ensemble and the
conditional-information remainder; no separate sign is assigned to the
two terms in the original latent decomposition.

Because \(W_U\) preserves every Hamming layer and is doubly stochastic,
iid Bernoulli-\(p\) is stationary.  Hence both \(Y\) and \(T\) are iid
Bernoulli-\(p\), and
\[
 H(Y,T)=2m h_b(p)-I(Y;T).
\]
With separate even/odd biases \(p_e,p_o\), the same construction gives
\[
 H(Y,T)=m h_b(p_e)+m h_b(p_o)-I_{m,U}(p_e,p_o).
\]
Thus the mixed parity response is exactly
\[
 -\partial_{p_e}\partial_{p_o}H
   =\partial_{p_e}\partial_{p_o}I_{m,U}.
\]
This is the structural sign quantity corresponding to the QWE09 witness
\(V\).

---

## 4. Overlap determinant and Poisson-binomial posterior

For words \(y,z\), put
\[
 A=|y|+|z|,\qquad B=|y\cap z|,
\]
and define
\[
 \theta=\log(q/v),\qquad
 \gamma=\log(uv/q^2)<0.
\]
Then
\[
 \Pr(Y=y,Z=z)=v^m e^{\theta A+\gamma B}.
\]

Since \(W_U\) preserves \(|z|\), \(A=|y|+|t|\) is output-measurable.  The
output atom has the exact form
\[
 \Pr(Y=y,T=t)
 =v^m e^{\theta(|y|+|t|)} Z_{y,t}(\gamma),
\]
where
\[
 Z_{y,t}(\gamma)
 =\sum_{|z|=|t|}|\det U_{z,t}|^2e^{\gamma|y\cap z|}.
\]

### Theorem 4.1 — determinant formula

Let \(P_y=\operatorname{diag}(y)\) and
\[
 A_{y,t}=(U^*P_yU)_{t,t}.
\]
Then
\[
 Z_{y,t}(\gamma)
 =\det\!\left(I_t+(e^\gamma-1)A_{y,t}\right).
\]
Every eigenvalue \(\lambda_j\) of \(A_{y,t}\) lies in \([0,1]\).

#### Proof

Use Cauchy–Binet with
\(D_y(\gamma)=\operatorname{diag}(e^{\gamma y_i})\):
\[
 \sum_{|z|=|t|}|\det U_{z,t}|^2\prod_{i\in z}e^{\gamma y_i}
 =\det[(U^*D_y(\gamma)U)_{t,t}].
\]
Since \(D_y(\gamma)=I+(e^\gamma-1)P_y\), the stated form follows.
\(\square\)

### Corollary 4.2 — hidden overlap is Poisson-binomial

Conditioned on \(O=(Y,T)=(y,t)\), the overlap \(B=|y\cap Z|\) has the law of
a sum of independent Bernoulli variables with parameters
\[
 r_j=\frac{e^\gamma\lambda_j}
          {1+(e^\gamma-1)\lambda_j}.
\]
Indeed,
\[
 \mathbb E[e^{\tau B}\mid O]
 =\frac{Z_{y,t}(\gamma+\tau)}{Z_{y,t}(\gamma)}
 =\prod_j\bigl(1-r_j+r_je^\tau\bigr).
\]

Write its first three cumulants as
\[
 \mu=\sum_jr_j,\qquad
 \kappa_2=\sum_jr_j(1-r_j),
\]
\[
 \kappa_3=\sum_jr_j(1-r_j)(1-2r_j).
\]
In particular,
\[
 \kappa_2\ge0,\qquad |\kappa_3|\le\kappa_2.
\]
This is a genuine payment: the third-cumulant term below never requires an
independent absolute bound.

---

## 5. Entropy gain as a relative entropy

Let \(X=(Y,Z)\), \(O=(Y,T)\), \(P_a(x)=\Pr(X=x)\), and
\(Q_a(o)=\Pr(O=o)\).  Put
\[
 J_a(x,o)=P_a(x)W_U(x,o),\qquad
 \widetilde J_a(x,o)=Q_a(o)W_U(x,o).
\]
Column stochasticity of \(W_U\) makes \(\widetilde J_a\) a probability law.
Therefore
\[
 G_{m,U}=D(J_a\Vert\widetilde J_a).
\]
The information density is
\[
 R(x,o)=\log\frac{P_a(x)}{Q_a(o)}
       =\gamma B-\log Z_o(\gamma).
\]
Its output-conditional mean is
\[
 \psi_o=\mathbb E[R\mid O=o]
       =\gamma\mu_o-\log Z_o(\gamma)\ge0.
\]
Equivalently, \(\psi_o\) is the KL divergence between the overlap-tilted
posterior on \(z\) and the un-tilted column weights
\(|\det U_{z,t}|^2\).

---

## 6. The compensated curvature identity

Define the input score and acceleration
\[
 S=\frac{P_a'}{P_a},\qquad
 \mathcal A=\frac{P_a''}{P_a}.
\]
Then
\[
 \frac{Q_a'}{Q_a}=\mathbb E[S\mid O],\qquad
 \frac{Q_a''}{Q_a}=\mathbb E[\mathcal A\mid O].
\]

### Theorem 6.1 — exact full payment

For every \(m\), every unitary \(U\), every \(0<c<1\), and every
\(0<a<1-c\),
\[
 \boxed{
 G_{m,U}''=
 \mathbb E[\mathcal A R]
 +\mathbb E\operatorname{Var}(S\mid O).
 }
\]

#### Proof

For any positive finite law \(P_a\),
\[
 H(P_a)''
 =-\mathbb E\!\left[\frac{P_a''}{P_a}\log P_a\right]
  -\mathbb E\!\left[\left(\frac{P_a'}{P_a}\right)^2\right].
\]
Apply this to \(P_a\) and \(Q_a=P_aW_U\), pull output expectations back to
\(J_a\), and subtract:
\[
\begin{aligned}
 G''
 &=\mathbb E\!\left[\mathcal A(\log P_a-\log Q_a)\right]
   +\mathbb E[S^2-(\mathbb E[S\mid O])^2]\\
 &=\mathbb E[\mathcal AR]
   +\mathbb E\operatorname{Var}(S\mid O).
\end{aligned}
\]
\(\square\)

This identity shows why ordinary data processing is insufficient:
the Fisher-information loss is only one term; the acceleration-weighted
information density remains.

### Theorem 6.2 — overlap-cumulant form

Let
\[
 C_1=\partial_a\{m\log v+\theta A\},\qquad
 C_2=\partial_a^2\{m\log v+\theta A\}.
\]
Because \(A\) is output-measurable,
\[
 S=C_1+\gamma'B.
\]
Hence
\[
 \mathbb E\operatorname{Var}(S\mid O)
 =(\gamma')^2\mathbb E\kappa_2.
\]
Furthermore, with
\[
 \overline{\mathcal A}
 =\mathbb E[\mathcal A\mid O]
 =(C_1+\gamma'\mu)^2+C_2+\gamma''\mu+(\gamma')^2\kappa_2,
\]
one has the exact pointwise conditional identity
\[
\begin{aligned}
 \mathbb E[\mathcal AR\mid O]
 ={}&\overline{\mathcal A}\,\psi\\
 &+\gamma(2C_1\gamma'+\gamma'')\kappa_2\\
 &+\gamma(\gamma')^2(2\mu\kappa_2+\kappa_3).
\end{aligned}
\]
Thus
\[
\boxed{
\begin{aligned}
G_{m,U}''
=\mathbb E\big[&
 \overline{\mathcal A}\,\psi\\
&+\{\;(\gamma')^2+
 \gamma(2C_1\gamma'+\gamma''+2(\gamma')^2\mu)\;\}\kappa_2\\
&+\gamma(\gamma')^2\kappa_3
\big].
\end{aligned}}
\]

#### Proof

The first statement follows from conditional variance.  For the second,
use
\[
 \mathcal A=(C_1+\gamma'B)^2+C_2+\gamma''B
\]
and the posterior identities
\[
 \mathbb E[BR\mid O]=\mu\psi+\gamma\kappa_2,
\]
\[
 \mathbb E[B^2R\mid O]
 =(\mu^2+\kappa_2)\psi
  +\gamma(2\mu\kappa_2+\kappa_3).
\]
Collect terms. \(\square\)

All moving mask weights and normalization effects are inside
\(C_1,C_2,\gamma',\gamma''\).  No derivative is silently frozen.

---

## 7. Symmetric-bias specialization and exact unpaid quantity

Let
\[
 a_0=\frac{1-c}{2},\qquad p=\frac12,
\]
and put
\[
 r=\frac{1-c^2}{4},\qquad s=\frac{1+c^2}{4}.
\]
Then
\[
 u=v=r,\qquad q=s,
\]
\[
 \gamma=2\log\frac{1-c^2}{1+c^2}<0,\qquad
 \gamma'=0,
\]
\[
 \gamma''
 =-\frac{64c^2}{(1+c^2)(1-c^2)^2}<0.
\]

The score of one pair is nonzero only on \(00\) and \(11\).  For \(m\)
pairs,
\[
 S=\frac{|Y|+|Z|-m}{r}.
\]
Since \(W_U\) preserves \(|Z|=|T|\), this score is already measurable from
\(O=(Y,T)\).  Therefore
\[
 \operatorname{Var}(S\mid O)=0
\]
identically.  The Fisher-loss payment vanishes at the midpoint.

The exact curvature becomes
\[
 \boxed{
 G_{m,U}''(a_0,c)
 =\mathbb E[\overline{\mathcal A}\,\psi]
  +\gamma\gamma''\,\mathbb E\kappa_2.
 }
\]
The second term is nonnegative, but the first term has no pointwise sign.

The iid-pair input curvature is
\[
 h_{\rm pair}''(a_0,c)
 =4\log(s/r)-\frac2r.
\]
Hence the cyclic observed entropy has
\[
 \boxed{
 H(Y,T)''
 =m\left(4\log(s/r)-\frac2r\right)
  +\mathbb E[\overline{\mathcal A}\,\psi]
  +\gamma\gamma''\,\mathbb E\kappa_2.
 }
\]

Thus the exact midpoint inequality still required for a general unitary is
\[
 \mathbb E[\overline{\mathcal A}\,\psi]
 +\gamma\gamma''\,\mathbb E\kappa_2
 \le
 m\left(\frac2r-4\log(s/r)\right).
\]
This is the precise unpaid quantity.  It is a determinant-eigenvalue
functional with a Poisson-binomial posterior, not the original unexpanded
conditional-information remainder.

---

## 8. Exact actual-cyclic obstruction

### Theorem 8.1 — entropy-gain concavity is false

Take the \(2m=4\)-site cyclic consecutive-Fourier projection, so \(m=2\)
and the Hamming-one block of \(W_U\) is the uniform \(2\times2\)
bistochastic matrix.  At \(a=(1-c)/2\), for every \(0<c<1\),
\[
 \boxed{
 G_{2,U}''=
 8s\log\frac{(r^2+s^2)^2}{4r^2s^2}>0.
 }
\]

#### Proof

Only the Hamming-one spectral layer is changed.  For \(y=00\) or \(11\),
the two Hamming-one input atoms are both \(rs\), so the uniform layer
channel changes nothing.  For each of \(y=01,10\), the two input atoms are
\(r^2\) and \(s^2\), while both output atoms equal
\[
 C=\frac{r^2+s^2}{2}.
\]
At the midpoint all first derivatives of these atoms vanish.  Their second
derivatives are
\[
 (r^2)''=4r-2=-4s,\qquad (s^2)''=-4s,\qquad C''=-4s,
\]
using \(r+s=1/2\).  Hence the changed input atoms contribute
\[
 8s\log r^2+8s\log s^2
\]
to their entropy second derivative, while the four changed output atoms
contribute \(16s\log C\).  Their difference is
\[
 16s\log C-8s\log(r^2s^2)
 =8s\log\frac{(r^2+s^2)^2}{4r^2s^2}.
\]
Since \(r,s>0\) and \(r\ne s\), \(r^2+s^2>2rs\), so the logarithm is
strictly positive. \(\square\)

This is a counterexample in the actual cyclic half-density projection
model, not in an unrelated projection.  It disproves the sufficient lemma
“the bistochastic entropy gain is concave.”  It does **not** disprove
concavity of the total observed entropy or of the infinite sine entropy
rate.

At \(c=19/20\), \(a=1/40\),
\[
 r=\frac{39}{1600},\qquad s=\frac{761}{1600},
\]
and
\[
 G''=\frac{761}{200}
 \log\frac{84286283041}{880843041}>0.
\]
The sign is certified by the exact integer inequality
\[
 84286283041>880843041.
\]

Numerically,
\[
 H(Y,Z)''=-140.33399040870776,
\]
\[
 G''=17.354966340795745,
\]
\[
 H(Y,T)''=-122.97902406791202.
\]

The midpoint Fisher-loss term is exactly zero, so this positive gain
curvature is entirely an acceleration/overlap effect.  Consequently,
a Fisher-information data-processing argument alone cannot pay the parity
remainder.

### Theorem 8.2 — total four-site midpoint curvature remains negative

For the same \(m=2\) cyclic model and every \(0<c<1\),
\[
 H(Y,T)''\big|_{a=(1-c)/2}<0.
\]

#### Proof

Set \(x=s/r=(1+c^2)/(1-c^2)>1\).  Since \(r+s=1/2\),
\[
 H(Y,T)''
 =8\log x-8(1+x)
 +\frac{8x}{1+x}\log\frac{x^2+1}{2x}.
\]
Now
\[
 \frac{x^2+1}{2x}<x,\qquad
 \log x<\frac{x-x^{-1}}2\quad(x>1).
\]
Therefore
\[
 H(Y,T)''
 <16\log x-8(1+x)
 <-8-\frac8x<0.
\]
\(\square\)

This is a restricted closure theorem: the first nontrivial cyclic model is
strictly concave at the symmetric bias even though the proposed
zero-payment gain-concavity mechanism fails.

---

## 9. Effective-contrast range over the whole legal bias interval

The accepted contraction baseline can be applied only after checking the
actual effective contrast and scalar shift.

At half density, complementing the observed configuration sends
\(a\) to \(1-c-a\).  The complementary projection \(I-Q_{1/2}\) is
diagonally unitarily equivalent to \(Q_{1/2}\) (Fourier shift by \(\pi\)),
so Shannon entropy is unchanged.  It is therefore enough to take
\[
 p\in(c/2,1/2].
\]
Then
\[
 b(p)=p-\frac{c^2}{4p}
\]
is increasing, so
\[
 0<b(p)\le\frac{1-c^2}{2}<\frac3{40}
 \qquad(c>37/40).
\]
Also \(p(1-p)\) is increasing on this interval, hence
\[
 \alpha(p)=\frac{c^2}{4p(1-p)}
 \le\frac{c}{2-c}.
\]
Therefore
\[
 \alpha(p)\le\frac{37}{40}
 \quad\hbox{for every legal }p
\]
if and only if
\[
 c\le\frac{74}{77}.
\]

### Theorem 9.1 — corrected baseline interval

For
\[
 \frac{37}{40}<c\le\frac{74}{77}
\]
and every legal \(a\), the accepted arbitrary-contraction baseline applies
to both parity-diagonal second partial derivatives.

More precisely, with separate parity shifts \(s,t\), hold the even shift
fixed.  The conditional odd kernel is
\[
 M_y(s,t)
 =\left(p_o-\frac{c^2}{4p_e}\right)I
  +\alpha(p_e)R_y(p_e).
\]
The observed-even weights do not move in \(t\).  Replacing \(R_y\) by
\((40\alpha/37)R_y\) puts the kernel in the baseline form, and differentiation
in \(t\) is exactly differentiation in its scalar shift.  Hence
\[
 H_{tt}\le-\frac{|O|}{50}.
\]
Swapping parity gives
\[
 H_{ss}\le-\frac{|E|}{50}.
\]
Thus
\[
 H''_{\rm common}
 =H_{ss}+2H_{st}+H_{tt}
 \le-\frac n{50}+2H_{st}.
\]
After the accepted mixed-response transfer,
\[
 \boxed{
 h''(a,c)\le-\frac1{50}-2v(a,c),
 }
\]
where \(v=-\lim H_{st}/n\) is the true mixed parity response represented by
the QWE09 \(V\)-witness.

Consequently \(v\ge-1/100\) would suffice for concavity on this whole
\(c\)-range, and \(v\ge0\) would give a strict \(1/50\) margin.

For \(c>74/77\), the effective contrast exceeds \(37/40\) near a legal
endpoint, so the accepted baseline cannot be invoked there.  This is the
exact parameter-extension gap; it is not legitimate to reuse the
\(c=.95\) constant without this check.

---

## 10. Interface to the true sine entropy rate

The finite cyclic exterior channel is an exact finite projection model and
a valid source of structural identities and counterexamples.  It is not,
by itself, a replacement for a finite Toeplitz compression.

For the true half-density sine process:

1. Theorem 2.1 gives the legitimate all-even unitary conditional law.
2. The accepted finite formula retains the contraction leakage
   \((1-p)(I-U^*U)\).
3. The accepted QWE09 second-response theorem transfers actual finite
   curvature and mixed parity response to fixed-gap infinite quantities.
4. Therefore a sign theorem for the limiting overlap functional, or a
   uniform cyclic-to-Hilbert argument with an explicit paid error, can be
   inserted into the QWE09 interface without differentiating an entropy
   value approximation.

What remains is one of the following.

* Prove the full compensated inequality from Theorem 6.2 per site for the
  Hilbert/Cauchy parity unitary.
* Prove the mixed-information supermodularity
  \[
     \partial_{p_e}\partial_{p_o}I(Y;T)\ge-1/100
  \]
  on the baseline range, with the stronger sign \( \ge0 \) preferred.
* For \(c>74/77\), additionally replace the unavailable
  \(37/40\)-contrast diagonal baseline or prove the full common-direction
  inequality directly.

No statement in this note transfers a finite negative numerical curvature
to the infinite true law without the accepted response interface.

---

## 11. Computational checks and exact inputs

The companion file `s73_checks.py` was executed in this session.

Exact input:
\[
 c=19/20,\qquad a=1/40,\qquad m=2.
\]
It used rational arithmetic to obtain
\[
 \frac{84286283041}{880843041}>1.
\]
Only the final logarithm was evaluated in floating point; the sign is
exact.

Double-precision cyclic diagnostics at \(c=.95,a=.025\) were:

| parity size \(m\) | input \(H''(Y,Z)\) | output \(H''(Y,T)\) | gain \(G''\) |
|---:|---:|---:|---:|
| 1 | -70.166995204354 | -70.166995204354 | 0 |
| 2 | -140.333990408708 | -122.979024067912 | 17.354966340796 |
| 3 | -210.500985613062 | -165.799043433719 | 44.701942179343 |
| 4 | -280.667980817415 | -202.786959378902 | 77.881021438514 |

The compensated identity residuals were between \(0\) and
\(3.6\times10^{-13}\).  An off-midpoint check
\((m,c,a)=(3,.95,.023)\) gave
\[
 G''=44.911559117443,
\]
split as
\[
 44.770270602074+0.141288515369,
\]
with residual \(1.7\times10^{-13}\).

These floating-point checks are diagnostics, not infinite-volume
certificates.  The four-site obstruction sign is exact.

---

## 12. Final classification

### PROVED

1. The all-even random-projection conditional law has a legitimate
   almost-sure formulation; no probability-zero word is conditioned on.
2. The cyclic parity problem is exactly an iid binary-pair source followed
   by the exterior-power bistochastic channel \(W_U\).
3. The output atoms have an exact overlap determinant.
4. The hidden overlap conditioned on the output is Poisson-binomial.
5. The entropy-gain curvature has the exact compensated identity in
   Theorems 6.1–6.2, with every moving-weight and cross term retained.
6. At the symmetric bias the Fisher-loss term vanishes identically.
7. The accepted contraction baseline covers every legal bias whenever
   \(37/40<c\le74/77\).
8. The four-site cyclic total entropy is strictly concave at the symmetric
   bias for every \(0<c<1\).

### DISPROVED

1. “The exterior-channel entropy gain is concave in \(a\)” is false.
2. “Fisher-information loss alone pays the parity remainder” is false:
   at the symmetric bias the Fisher loss is exactly zero while the
   four-site gain curvature is strictly positive.
3. A finite true Toeplitz conditional kernel may not be treated as a
   projection; the unitary formula belongs to full-infinite conditioning
   or a genuine cyclic projection.

### INCOMPLETE

1. The sign of the compensated overlap functional per site for the
   infinite Hilbert/Cauchy unitary.
2. The mixed-information bound \(v\ge-1/100\), or the stronger \(v\ge0\),
   needed to close the accepted baseline range.
3. A replacement for the diagonal contraction baseline on
   \(c>74/77\) near legal endpoints.
4. Extension from \(\rho=1/2\) to arbitrary density.

The conjecture that the true sine entropy rate is concave is neither proved
nor refuted here.
