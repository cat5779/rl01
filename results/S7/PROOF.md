# S7: averaged spatial control of the actual entropy Hessian

**Author proof, pending independent review.** The full sine entropy-rate
concavity target is not asserted. This file proves an absolute far-pair
curvature bound, not the sign of its remaining near-pair part.

## 1. Frozen statement

Let B={1,...,n}, n>=1, and let E be one interval of normalized measure
0<rho<1 on the frequency circle. Write Q_B=T_B(1_E), the actual finite
Toeplitz compression, and

\[
 K_B=aI+cQ_B,\qquad 0<c<1,\quad a>0,\quad d=1-a-c>0.
\]

Set

\[
 \delta=\min(a,d),\quad \beta_*=\delta(\delta+c),\quad
 \vartheta=\frac{(a+c)(1-a)}{ad}=1+\frac c{ad},\quad
 M=\max\{1,\log\vartheta\}.
 \tag{1.1}
\]

All entropies are natural-log Shannon entropies of all labelled binary words.
For each i<j, condition on the actual outside output word
Z=Y_{B\setminus\{i,j\}}. Its two-site conditional kernel is denoted

\[
 C^{ij,Z}=\begin{pmatrix}q&\zeta\\\bar\zeta&r\end{pmatrix},
 \qquad s=|\zeta|^2.
\]

Its four probabilities are

\[
 p_{00}=(1-q)(1-r)-s,\quad p_{10}=q(1-r)+s,\quad
 p_{01}=(1-q)r+s,\quad p_{11}=qr-s.
 \tag{1.2}
\]

With the diagonals q,r fixed when differentiating in v, define

\[
 \Lambda(v)=\log\frac{[q(1-r)+v][(1-q)r+v]}
 {[qr-v][(1-q)(1-r)-v]},\qquad
 g_{ij}(Z)=\Lambda(s)-s\Lambda'(s).
 \tag{1.3}
\]

### Theorem A: paid absolute far-pair curvature

For every positive integer R,

\[
 \boxed{
 2\sum_{\substack{i<j\in B\\j-i\ge R}}
       \mathbb E|g_{ij}(Z)|
 \le \frac nR\,C(a,c),\qquad
 C(a,c)=\min\left\{
 \frac{3c^4}{16\delta^8},
 \frac{3c^2M}{2\beta_*^2}\right\}.
 }
 \tag{1.4}
\]

The expectation retains every actual outside word. The absolute value is
inside that expectation, so this also controls the total absolute far-pair
mass, not merely its signed sum.
The constant is independent of n and rho. It is uniform on each fixed compact
subset of the strict (a,c) channel domain. No endpoint-uniform assertion is
made. R>n is vacuous.

The exact identity to which (1.4) applies is

\[
 H_B''(a)=-\sum_{i\in B}\mathbb E\frac1{u_i(1-u_i)}
       +2\sum_{i<j\in B}\mathbb E g_{ij}(Z),
 \quad u_i=\mathbb P(Y_i=1\mid Y_{B\setminus\{i\}}).
 \tag{1.5}
\]

In particular, retain the diagonal term and the pairs j-i<R in (1.5), calling
their sum N_{B,R}(a). Then

\[
 |H_B''(a)-N_{B,R}(a)|\le n C(a,c)/R.                 \tag{1.6}
\]

This is strictly weaker than concavity: it leaves the sign of N_{B,R} unpaid.
The terms in N_{B,R} still condition on the full outside word; a pair-distance
cutoff is not, by itself, a conditioning-radius cutoff.

### Theorem B: the actual posterior energy bound used in A

Generate X_B~DPP(Q_B) and pass its bits independently through
Pr(Y_i=1|X_i)=a+cX_i. Let R^Y be a Hermitian positive-contraction kernel for
X_B conditional on the complete Y_B. Then

\[
 \boxed{\quad
 \mathbb E_Y\sum_{\substack{i,j\in B\\|i-j|\ge R}}|R^Y_{ij}|^2
 \le \frac{3n}{2R}.\quad}                            \tag{1.7}
\]

The sum in (1.7) is ordered. The expectation is the actual output law, not a
uniform-word, count-layer, typical-word, or auxiliary-field average. The
constant is uniform in the noise parameters. This theorem uses the ambient
Fourier projection only after extending a finitely supported test function;
Q_B itself is never treated as a projection.

### Theorem C: a word-uniform inverse bound

For the complete word y put

\[
 A_y=K_B-\operatorname{diag}(1-y),\qquad G_y=A_y^{-1}.
\]

Every word satisfies

\[
 \boxed{\quad
 \sum_{\substack{i,j\in B\\|i-j|\ge R}}|(G_y)_{ij}|^2
 \le \frac{3nc^2}{8\delta^4R}.\quad}                 \tag{1.8}
\]

The posterior identity also gives the different, averaged bound

\[
 \mathbb E_Y\sum_{|i-j|\ge R}|(G_Y)_{ij}|^2
 \le \frac{3nc^2}{2\beta_*^2R}.                     \tag{1.9}
\]

The improvement from delta^(-4) to beta_*^(-2) in the latter estimate is
important at high contrast; it is paid by actual posterior averaging, not a
pointwise assertion about every inverse.

## 2. Complete words and surviving integrable structure

A diagonal phase gauge centers E and preserves every configuration
probability. We may therefore write

\[
 q_r=\frac{\sin(\pi\rho r)}{\pi r}\quad(r\ne0),\qquad q_0=\rho,
 \qquad (Q_B)_{ij}=q_{i-j}.                          \tag{2.1}
\]

### 2.1 Occupied AND empty sites

Diagonal multilinearity gives, with S={i:y_i=1},

\[
 p_y=(-1)^{n-|S|}\det A_y
 =\sum_{T\subseteq B\setminus S}(-1)^{|T|}\det(K_B)_{S\cup T}.
 \tag{2.2}
\]

Thus p_y is the complete word, not an inclusion probability. Since the strict
channel gives a positive likelihood to every output for every latent input,
p_y>0. The usual finite Janossy form is equivalently

\[
 p_y=\det(I-K_B)\det\bigl([K_B(I-K_B)^{-1}]_S\bigr).  \tag{2.3}
\]

For completeness, (2.3) follows by expanding
\(\det(I-K_B+ZK_B)\) in the diagonal variables Z and factoring I-K_B.
No continuum Janossy theorem is invoked.

The matrix pencil and its spectral gap already occur in reviewed S6,
source/proof.md, Lemma 2.1. Here is a direct gap check. Order the occupied
sites before the empty sites, and set J=diag(2y-1). The Hermitian part of

\[
 JA_y=\begin{pmatrix}(K_B)_{SS}&(K_B)_{S,S^c}\\
                  -(K_B)_{S^c,S}&I-(K_B)_{S^c,S^c}\end{pmatrix}
\]

is at least delta I. Consequently \(\|A_yv\|\ge\delta\|v\|\), and

\[
 \|G_y\|\le\delta^{-1}.                            \tag{2.4}
\]

This pre-existing gap is an input/re-proof, not this round's claimed advance.

### 2.2 The exact posterior, with its actual normalizer

Put alpha_1=a, alpha_0=1-a, sigma_b=2b-1, and

\[
 D_{ii}=\frac{\alpha_{y_i}+\sigma_{y_i}c}{\alpha_{y_i}}.
\]

Then

\[
 p_y=\prod_i\alpha_{y_i}\,\det(I+(D-I)Q_B),\qquad
 R^y=D^{1/2}Q_B[I+(D-I)Q_B]^{-1}D^{1/2}.             \tag{2.5}
\]

Indeed the conditional likelihood is
\(\prod_i\alpha_{y_i}D_{ii}^{X_i}\). The DPP generating determinant proves
the normalizer; external-field weighting proves the displayed posterior.
One elementary proof of the latter is to use L=Q_B(I-Q_B)^(-1), replace L
by D^(1/2)LD^(1/2), and form L_y(I+L_y)^(-1). Approximation covers arbitrary
positive contractions. The resulting kernel is Hermitian and lies in [0,I].
The same argument applies when only some coordinates are observed, by putting
D_ii=1 at unobserved coordinates.

Let H=diag(sigma_{y_i} alpha_{y_i}) and
\(B_\beta=\operatorname{diag}(\beta_i)\), where
\(\beta_i=\alpha_{y_i}(\alpha_{y_i}+\sigma_{y_i}c)\).
Since A_y=H+cQ_B and D-I=cH^(-1), the inverse identity gives

\[
 G_y=H^{-1}-cJ B_\beta^{-1/2}R^y B_\beta^{-1/2}J.
 \tag{2.6}
\]

In particular, for i!=j,

\[
 |(G_y)_{ij}|^2=\frac{c^2|R^y_{ij}|^2}{\beta_i\beta_j},\qquad
 \beta_i\ge\min\{a(a+c),d(1-a)\}=\beta_* .          \tag{2.7}
\]

This is compatible with the reviewed complete-posterior/reverse-Bayes
identities. It does not change the averaging law.

### 2.3 What integrability survives an arbitrary word

Let X=diag(i), u_i=exp(i*pi*rho*i), v_i=exp(-i*pi*rho*i). Then

\[
 [X,Q_B]=\frac{uu^*-vv^*}{2\pi\mathrm i},\qquad
 [X,G_y]=-cG_y[X,Q_B]G_y.                            \tag{2.8}
\]

Both commutators have rank at most two. In the posterior formula,

\[
 [X,R^y]=D^{1/2}[I+Q_B(D-I)]^{-1}[X,Q_B]
              [I+(D-I)Q_B]^{-1}D^{1/2}.             \tag{2.9}
\]

Thus the displacement rank also survives the actual positive posterior
field. This follows by differentiating Q(I+(D-I)Q)^(-1) under diagonal
conjugation, or just by the inverse commutator identity.

An explicit zero-diagonal discrete integrable matrix is also available. Let
mu=a+c*rho and C_y=diag(mu if y_i=1, mu-1 if y_i=0). Then

\[
 A_y=C_y(I+L_y),\qquad L_y=c C_y^{-1}(Q_B-\rho I),\qquad
 (L_y)_{ij}=\frac{f_y(i)^Tg(j)}{i-j}\quad(i\ne j),
\]

where

\[
 f_y(i)=\frac c{(C_y)_{ii}}
   \binom{e^{\mathrm i\pi\rho i}}{e^{-\mathrm i\pi\rho i}},\quad
 g(j)=\frac1{2\pi\mathrm i}
   \binom{e^{-\mathrm i\pi\rho j}}{-e^{\mathrm i\pi\rho j}},
 \quad f_y(i)^Tg(i)=0.                              \tag{2.10}
\]

The diagonal of L_y is zero. Its word-dependent row factor need not preserve
a self-adjoint positive-kernel formulation or a bounded-degree differential
system. Nevertheless, algebraically (2.10) is exact, and

\[
 p_y=\mu^{|y|}(1-\mu)^{n-|y|}\det(I+L_y),\quad
 H_B= n b(\mu)-\mathbb E_{p_y}\log\det(I+L_y).        \tag{2.11}
\]

Here det(I+L_y)>0. The second term is kept exactly and can be extensive.
Neither (2.8) nor (2.11) alone is a new entropy bound. The paid estimates are
proved next.

## 3. Bounded phases and the word-uniform tail

For U_theta=diag(exp(i*theta*j)), the diagonal mask commutes with U_theta, so

\[
 [U_\theta,G_y]=-cG_y[U_\theta,Q_B]G_y,\quad
 \|[U_\theta,G_y]\|_{\rm HS}^2
 \le c^2\delta^{-4}\|[U_\theta,Q_B]\|_{\rm HS}^2.   \tag{3.1}
\]

Parseval and the symmetric difference of a circle interval give

\[
 F(\theta):=\sum_{r\in\mathbb Z}|q_r|^2|e^{\mathrm i r\theta}-1|^2
 =|E\triangle(E+\theta/(2\pi))|
 \le\frac{|\theta|}{\pi}\quad(|\theta|\le\pi).
 \tag{3.2}
\]

The normalized measure convention in (3.2) is essential. Hence
\(\|[U_\theta,Q_B]\|_{\rm HS}^2\le nF(\theta)\).
Average (3.1) uniformly on [-pi/R,pi/R]. If |i-j|>=R, the averaged multiplier
on |(G_y)_ij|^2 is

\[
 2\left(1-\frac{\sin(\pi(i-j)/R)}{\pi(i-j)/R}\right)
 \ge 2(1-1/\pi)\ge4/3.                             \tag{3.3}
\]

The average of |theta|/pi is 1/(2R). Dividing by 4/3 proves (1.8).
Using the unbounded coordinate X instead would give a volume-squared bound;
the bounded phases and their scale-dependent average are the new spatial step.

## 4. Actual posterior averaging, including the boundary payment

### 4.1 Conditional variance controls the posterior Dirichlet form

For any finite positive-contraction DPP kernel R and any complex vector f,
its elementary one- and two-point covariances give

\[
 \operatorname{Var}\!\left(\sum_i f_iX_i\right)
 =\frac12\sum_{i,j}|R_{ij}|^2|f_i-f_j|^2
  +\sum_i |f_i|^2(R-R^2)_{ii}
 \ge\frac12\sum_{i,j}|R_{ij}|^2|f_i-f_j|^2.          \tag{4.1}
\]

Variance here means E|Z-EZ|^2. The last term is nonnegative; it is NOT omitted
by pretending that a finite compression is a projection.

Take any finitely supported f on Z, and a finite interval W containing its
support and B. Generate X_W~DPP(Q_W), but observe only the noisy Y_B. The
posterior is a DPP with a positive-contraction kernel R_W^Y by (2.5), with
unit fields on W\B. The conditional law of X_B is the same as in Theorem B.
In particular its pair covariances, and hence |(R_W^Y)_ij|^2 for i,j in B,
are those of R^Y. Conditional-variance contraction and (4.1) imply

\[
 \mathbb E_Y\sum_{i,j\in B}|R^Y_{ij}|^2|f_i-f_j|^2
 \le 2\operatorname{Var}_{Q_W}\!\left(\sum_i f_iX_i\right).
 \tag{4.2}
\]

Extend f by zero outside W. The ambient convolution operator P with multiplier
1_E is a projection. Its row identity
\(\sum_j|q_{i-j}|^2=\rho\) now gives, exactly,

\[
 2\operatorname{Var}_{Q_W}\!\left(\sum_i f_iX_i\right)
 =\mathcal E_P(f):=\sum_{i,j\in\mathbb Z}|q_{i-j}|^2|f_i-f_j|^2.
 \tag{4.3}
\]

Only this ambient identity uses a projection. Equations (4.1)--(4.3) prove
(4.2) without any infinite conditional-kernel or tail-triviality assumption.

### 4.2 A plateau with a paid boundary

Define a real nonnegative tent g on the integers by g_i=1 for 0<=i<=n,
linear increase from 0 to 1 on [-n,0], linear decrease from 1 to 0 on [n,2n],
and zero elsewhere. In particular g=1 on B. Direct finite sums give

\[
 \|g\|_2^2=\frac{5n}{3}+\frac1{3n}\le2n,\qquad
 \|\nabla g\|_2^2=\frac2n.                         \tag{4.4}
\]

The Fourier form of its energy, (3.2), Cauchy--Schwarz, and
\(|\theta|\le(\pi/2)|e^{\mathrm i\theta}-1|\) on [-pi,pi] give

\[
 \begin{aligned}
 \mathcal E_P(g)
 &=\int_{-\pi}^{\pi}|\widehat g(\theta)|^2F(\theta)\frac{d\theta}{2\pi}\\
 &\le\frac1\pi\|g\|_2
       \left(\int_{-\pi}^{\pi}\theta^2|\widehat g(\theta)|^2
                    \frac{d\theta}{2\pi}\right)^{1/2}\\
 &\le\frac12\|g\|_2\|\nabla g\|_2\le1.
 \end{aligned}                                    \tag{4.5}
\]

Thus the cutoff boundary costs at most one, uniformly in n and rho. A sharp
indicator cutoff would instead introduce an avoidable logarithmic boundary
cost.

For f_theta(i)=g_i exp(i*theta*i), the exact scalar identity

\[
 |g_i e^{\mathrm i\theta i}-g_j e^{\mathrm i\theta j}|^2
 =(g_i-g_j)^2+g_ig_j|e^{\mathrm i\theta i}-e^{\mathrm i\theta j}|^2
\]

and \(\sum_i g_i g_{i-r}\le\|g\|_2^2\) yield

\[
 \mathcal E_P(f_\theta)\le1+2n|\theta|/\pi.         \tag{4.6}
\]

Apply (4.2), use g=1 on B, and average theta on [-pi/R,pi/R]. For 1<=R<=n,
the right side is at most 1+n/R<=2n/R. The lower multiplier bound (3.3)
therefore proves (1.7). For R>n the sum is empty. Applying (2.7) proves (1.9).
No observation, word, or cardinality layer has been dropped from the average.

## 5. The precise bridge to the full entropy Hessian

### 5.1 Derivation, not an entropy-value differentiation shortcut

Temporarily give each kernel diagonal its own shift a_i. For the mixed
partial in coordinates i,j, the outside marginal law is independent of a_i,a_j.
Its two-site conditional kernel has diagonals affine with slopes one in these
two variables and an off-diagonal independent of them. This follows directly
by Schur complement in the complete-word determinant (2.2). Differentiating
all four atoms (1.2) gives the mixed entropy derivative

\[
 \partial_{a_i}\partial_{a_j}H_B
 =\mathbb E_Z[\Lambda(s)-s\Lambda'(s)].             \tag{5.1}
\]

Here the probability-acceleration term is Lambda(s), and the mixed Fisher
term is -s Lambda'(s). For clarity, the four mixed atom derivatives are
(+1,-1,-1,+1) in the order (00,10,01,11), so the acceleration contribution is
log(p10*p01/(p00*p11)). The mixed Fisher sum is s times the sum of the four
reciprocal atoms, as direct substitution verifies. For i=j, the conditional
one-bit entropy has second derivative -1/[u_i(1-u_i)]. Summing the diagonal partials
and both orders of every mixed partial proves (1.5).

All these are derivatives of the genuine finite law. The outside law is held
fixed only for the appropriate two coordinate partials; the full common-shift
Hessian is their complete sum.

The latent construction also proves

\[
 aI\le C^{ij,Z}\le(a+c)I,
\]

because the unobserved output pair is the same channel applied to the
positive-contraction posterior input pair. Its conditional one-bit
probabilities all lie in [a,a+c]. In particular

\[
 p_{11}\ge a^2,\quad p_{00}\ge d^2,\quad
 p_{10},p_{01}\ge ad.                              \tag{5.2}
\]

### 5.2 Completion averaging of the inverse

For any complete word y extending Z, the Schur complement of A_y on {i,j}
is C^{ij,Z}-diag(1-y_i,1-y_j). The two-by-two inverse formula therefore gives

\[
 |(G_y)_{ij}|^2=\frac{s}{p(y_i,y_j\mid Z)^2}.
\]

Averaging over its FOUR actual completions, rather than uniformly, yields

\[
 \boxed{\quad
 \mathbb E[|(G_Y)_{ij}|^2\mid Z]
 =s\left(\frac1{p_{00}}+\frac1{p_{10}}+
         \frac1{p_{01}}+\frac1{p_{11}}\right)
 =s\Lambda'(s).\quad}                             \tag{5.3}
\]

Thus the spatial inverse estimates control a specific term of the exact
acceleration/Fisher combination.

### 5.3 A scalar bound retaining that combination

Abbreviate A=p00, B=p10, C=p01, D=p11 within this paragraph, and put
xi=s/(AD), u=A+D. The identity BC=AD+s gives

\[
 g=\frac{\xi^2}{1+\xi}[T(\xi)-u],\qquad
 s\Lambda'(s)=\frac{\xi(1+u\xi)}{1+\xi},\qquad
 T(\xi)=\int_0^1\frac{1-t}{1+\xi t}\,dt.           \tag{5.4}
\]

At s=0, g=0. For s>0, if g<=0 then |g|/[s Lambda']<=1. If g>0, the ratio is
at most xi*T(xi), and

\[
 \xi T(\xi)=\log(1+\xi)+\frac{\log(1+\xi)}\xi-1
 \le\log(1+\xi).                                  \tag{5.5}
\]

The conditional-odds strip implies

\[
 1+\xi=\frac{BC}{AD}
 =\frac{\operatorname{odds}(Y_i=1\mid Y_j=0,Z)}
        {\operatorname{odds}(Y_i=1\mid Y_j=1,Z)}
 \le\vartheta.
\]

Combining with (5.3),

\[
 |g_{ij}(Z)|\le M\,\mathbb E[|(G_Y)_{ij}|^2\mid Z]. \tag{5.6}
\]

Sum the ordered pairs and use (1.9). This proves the second constant in (1.4).
It is not a bound on the acceleration alone with the Fisher term discarded.

### 5.4 A separate quartic estimate

Scaling the off-diagonal of C from zeta to zero preserves its spectral strip.
Along this scaling the four atom bounds (5.2) therefore remain valid. Since
Lambda(0)=0,

\[
 g=-\int_0^s v\Lambda''(v)\,dv,\qquad
 |\Lambda''(v)|\le(a^{-2}+d^{-2})^2\le4\delta^{-4}.
\]

Hence |g|<=2 delta^(-4) s^2. Also |zeta|<=c/2, so
|g|<=c^2 s/(2 delta^4). The completion identity preceding (5.3), with
p(y_i,y_j|Z)<=1, gives s<=|(G_y)_ij|^2 for every completion. Now use (1.8).
This proves the first constant in (1.4). Taking the better of two separately
proved bounds completes Theorem A.

## 6. Integrated interpretation and the exact remaining gap

Fix c and a compact interval J inside (0,1-c), and let C_J=sup_{a in J}C(a,c).
Choose any twice-antiderivative F_{B,R} of N_{B,R} on J. Its two arbitrary
affine constants do not affect a Jensen difference. Integrating (1.6) twice
shows that the absolute difference between the Jensen gaps of H_B and F_B,R
at a0,a1 in J and t in [0,1] is at most

\[
 \frac{n C_J}{2R}\,t(1-t)(a_1-a_0)^2.              \tag{6.1}
\]

This is a finite true-law statement; no thermodynamic derivative has been
exchanged with a limit. Dividing by n makes its error vanish as R tends to
infinity. To settle the full sine target by this route one still needs a
nonpositive normalized near-pair curvature, or an adequate integrated signed
bound for its antiderivative, at growing R. No such sign is proved here.

In particular this theorem does not raise the universal 37/40 contrast
threshold, does not treat a=0 or d=0 by the divergent constants above, and does
not turn finite pair-distance truncation into an independent-block model.


## 7. Exact posterior mean and sharpness of the energy order

The posterior in (2.5) has a fixed canonical phase gauge. In that gauge put

\[
 \tau=\sqrt{a(a+c)}+\sqrt{d(1-a)}.
\]

### Proposition D: the mean-kernel response

For every finite Hermitian positive contraction Q (not only the sine Q_B),
under the full actual output average,

\[
 \boxed{\quad
 \mathbb E_Y R^Y=\tau^2 Q+(1-\tau^2)\operatorname{diag}(Q).
 \quad}                                                   \tag{7.1}
\]

No word-dependent gauge change is allowed inside this matrix expectation.
The subsequent squared-entry conclusion is gauge invariant. This identity
is rederived here; no priority claim for the general identity is made.

**Proof.** The diagonal assertion is the law of total expectation for X_i.
For i!=j use the cofactor C_ji(A_y), so that (2.2) and (2.6) give

\[
 p_y R^y_{ij}=-\frac{\sqrt{\beta_{y_i}\beta_{y_j}}}{c}
    \left(\prod_{k\ne i,j}\sigma_{y_k}\right)C_{ji}(A_y).
                                                               \tag{7.2}
\]

This cofactor contains neither diagonal entry A_ii nor A_jj, because column i
and row j were deleted. Summing the two endpoint bits in (7.2) therefore
produces the factor tau^2. On the other coordinates the signed sum is the
successive finite difference between diagonal values a+cQ_kk and
 a+cQ_kk-1. Cofactors are multilinear in those diagonal variables. This
finite difference selects the coefficient of their complete product.
That coefficient in C_ji is -c Q_ij: in the determinant before differentiating
with respect to A_ji, the unique contributing permutation fixes every other
coordinate and transposes i,j. Substitution in (7.2) proves (7.1).
Approximation, or the same cofactor argument, covers singular Q. QED.

Jensen's inequality now gives the entrywise LOWER bound

\[
 \mathbb E_Y|R^Y_{ij}|^2\ge\tau^4|Q_{ij}|^2\quad(i\ne j).       \tag{7.3}
\]

It does not give an entrywise upper bound; an explicit failure of such an
upper bound is recorded in OBSTRUCTIONS.md.

### Corollary E: n/R is the optimal order for the posterior energy

Take the actual half-density sine compression, rho=1/2. For every integer
R>=1 and every n>=4R, (7.3) implies

\[
 \boxed{\quad
 \mathbb E_Y\sum_{|i-j|\ge R}|R^Y_{ij}|^2
 \ge\frac{\tau^4}{8\pi^2}\frac nR.
 \quad}                                                    \tag{7.4}
\]

Indeed q_r is zero at nonzero even r and has squared modulus
1/(pi^2 r^2) at odd r. Among R,...,2R-1 there are at least R/2 odd integers.
For these r, n-r>=n/2 and r<=2R. In the ordered sum
2 sum_r (n-r)|q_r|^2, their contribution is at least n/(8 pi^2 R).
This proves (7.4).

At every fixed strict channel, tau>0. Thus the n/R order in Theorem B cannot
be replaced uniformly in n by n*o(1/R), even at the single fixed density 1/2.
This sharpness assertion is about posterior squared-entry energy only.
It does NOT rule out faster decay of the entropy-curvature tail: the quartic
cancellation in g gives precisely such a refinement in QUASILOCALITY.md.
