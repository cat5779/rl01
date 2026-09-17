# Four precise obstructions, not a counterexample to sine entropy concavity

**Author proofs/certificate; independent review pending.** The main packet
status is PROVED_SCOPED_LEMMA because of the positive spatial results in
PROOF.md and QUASILOCALITY.md. The first two statements delimit tempting stronger versions of the route.
The third concerns a specific integrable-method interface. The fourth gives
an explicit growing-volume word family ruling out a uniform bare 1/r inverse
bound. None rules out every possible Riemann-Hilbert method.

## 1. A genuine sine pair can remain positive after actual output averaging

### Certified statement

For the actual six-site Toeplitz compression, take

\[
 n=6,\quad \rho=\frac12,\quad c=\frac{19}{20},\quad a=\frac1{40},
 \qquad (i,j)=(1,6).
\]

With g defined in PROOF.md (1.3), the full outside-word average satisfies

\[
 \boxed{\qquad
 \frac{37}{100000}<\mathbb E g_{1,6}<\frac{39}{100000}.
 \qquad}                                                     \tag{1.1}
\]

At exactly the same parameter point, the complete six-bit entropy obeys

\[
 \boxed{\qquad -50<H_6''(a)<-49.\qquad}                        \tag{1.2}
\]

The decimal displays are approximately 0.000379092242041686 and
-49.565521239251, respectively. The signs and rational bounds above do not
use those decimal displays.

Thus the live sufficient statement "every averaged conditional pair g is
nonpositive for actual sine kernels" is false. Both the conditional-word
and the averaged-pair versions are too strong. This does not disprove finite
entropy concavity, entropy-rate concavity, compensation between different
pairs, or compensation by the diagonal/Fisher contribution.

### Mathematical reduction to rational polynomial arithmetic

At these parameters the output kernel has diagonal 1/2. Set x=c/pi and
 t=x^2. Its off-diagonal entries are

\[
 x\frac{\sin(\pi(i-j)/2)}{i-j}.
\]

The sine factor is exactly 0 or +/-1. A nonzero off-diagonal connects opposite
parities. Any nonzero permutation term in a determinant contains an even
number of these connections: the number crossing from even to odd equals
the number crossing from odd to even. Consequently every complete atom is
an exact rational polynomial P_y(t) of degree at most three. They are obtained
from the signed full-word determinant, not from an inclusion event.

The checker records all 64 polynomial coefficient lists and verifies the
polynomial identity sum_y P_y(t)=1. It evaluates them on one enclosing
rational interval for t and verifies that every atom has positive lower bound.
No zero or small atom is omitted.

For one outside word z, denote its FOUR unconditional complete probabilities
by A,B,C,D in the order 00,10,01,11, and put p_z=A+B+C+D. The contribution of
this outside word to E g is exactly

\[
 p_z\log\frac{BC}{AD}
 -(BC-AD)\left(\frac1A+\frac1B+\frac1C+\frac1D\right).          \tag{1.3}
\]

To check normalization, the conditional determinant difference is
(BC-AD)/p_z^2 and the sum of reciprocal conditional atoms is
p_z(1/A+1/B+1/C+1/D). Multiplication by the actual outside probability p_z
therefore gives (1.3). The certificate sums this expression over all 16
outside words.

For the independent algebraic expression used to check the TOTAL Hessian,
let sigma_i=2y_i-1 and write flips as y^i,y^ij. Diagonal multilinearity gives

\[
 p_y'=\sum_i\sigma_i(p_y+p_{y^i}),
\]
\[
 p_y''=2\sum_{i<j}\sigma_i\sigma_j
  (p_y+p_{y^i}+p_{y^j}+p_{y^{ij}}).
\]

All 64 terms of

\[
 H_6''=-\sum_y p_y''\log p_y-\sum_y(p_y')^2/p_y
\]

are retained. In particular (1.2) was not inferred from the positive pair
or from a particle-count entropy.

### Enclosures for pi and logarithms

Machin's identity is used in the form

\[
 \pi=16\arctan(1/5)-4\arctan(1/239).
\]

One elementary check is tan(4 arctan(1/5))=120/119 and
 tan(4 arctan(1/5)-arctan(1/239))=1. The angle lies in (0,pi/2), so it is
pi/4. For example arctan x lies between x/(1+x^2) and x for x>0, which also
checks the required branch. Twenty terms of each alternating arctangent
series, together with the first omitted term, enclose pi rationally.

For log x, write x=2^k u with 1<=u<2, using rational comparisons. If
z=(u-1)/(u+1), then 0<=z<=1/3 and

\[
 2\sum_{j=0}^{23}\frac{z^{2j+1}}{2j+1}
 \le\log u\le
 2\sum_{j=0}^{23}\frac{z^{2j+1}}{2j+1}
 +\frac{2z^{49}}{49(1-z^2)}.
\]

The same formula encloses log 2. It is combined with k log 2 using interval
arithmetic, including the reversal for a negative k. Every arithmetic
operation is rounded outward to a rational grid of denominator 10^40.
Logarithm monotonicity encloses the logarithm of an interval. Strict rational
endpoint comparisons certify (1.1)--(1.2).

`verify_pair_witness.py` implements these finite steps with the Python
standard library. `checks/pair_witness.json` contains the complete coefficient
and outside-word data. The optimized-mode run is separately recorded in
`checks/pair_witness_optimized.json`. Their mathematical fields agree exactly;
the elapsed-time display is not a mathematical field. These are same-author
checks, not independent review or a replacement for the universal proofs.

## 2. Posterior squared-entry energy is not bounded entry by entry by the prior

This obstruction is entirely analytic and also uses the actual sine kernel.
Let n=3,rho=1/2. Then Q_13=0, Q_12=Q_23=1/pi, Q_22=1/2. First observe only Y_2
through any strict channel with c>0. Its likelihood ratio w is either
(a+c)/a or d/(1-a), both positive and different from one.

The external-field update on the two unobserved endpoints gives

\[
 R_{13}^{Y_2}=-\frac{w-1}{\pi^2[1+(w-1)/2]}\ne0.               \tag{2.1}
\]

Now observe the two remaining output bits. If their positive likelihood
ratios are w_1,w_3, the two-by-two external-field formula updates the
endpoint off-diagonal by the factor

\[
 \frac{\sqrt{w_1w_3}}
 {\det\{I+(\operatorname{diag}(w_1,w_3)-I)R_{\{1,3\}}^{Y_2}\}}>0.
\]

Thus every complete-output posterior has a nonzero endpoint entry. Every
complete word has positive probability, so

\[
 \boxed{\quad \mathbb E_Y|R_{13}^Y|^2>0=|Q_{13}|^2.\quad}       \tag{2.2}
\]

This rules out replacing the proof's conditional-variance quadratic-form
inequality by a false entrywise contraction. It is fully consistent with
PROOF.md (7.3), which is a lower bound with a noise factor, and with the
averaged spatial tail bound.

## 3. Arbitrary binary masks do not preserve bounded-degree Pearson data

The discrete orthogonal-polynomial Riemann-Hilbert route has a genuine
conditional interface: bounded-degree weight-ratio data lead to a
bounded-degree Lax matrix. Borodin--Boyarchenko, *Distribution of the first
particle in discrete orthogonal polynomial ensembles*, math-ph/0204001,
Theorem 3.1(b),(c), explicitly imposes such weight-ratio data. The theorem
also has an affine-grid/orthogonal-polynomial setting; none of that is
silently asserted for the noisy Toeplitz compression.

Here is an obstruction to the proposed extension "all positive binary word
fields preserve a fixed polynomial degree in that weight-ratio interface."
Fix n>=4 and one site 2<=k<=n-1. Use the legal complete word with a single one
at k and zeros elsewhere. Its posterior field is

\[
 w_i=w_0\vartheta^{\mathbf1_{\{i=k\}}},\qquad
 w_0=d/(1-a)>0,\quad
 \vartheta=\frac{(a+c)(1-a)}{ad}>1.
\]

Its adjacent ratios r_i=w_{i+1}/w_i, i=1,...,n-1, are one except at the two
indices k-1 and k, where they are vartheta and vartheta^(-1). Suppose

\[
 r_i=P(i)/Q(i),\qquad \deg P,\deg Q\le D,\quad Q(i)\ne0
\]

at all these nodes. Then P-Q vanishes at n-3 distinct nodes, but cannot
vanish identically because of the two exceptional ratios. Hence

\[
 \boxed{\qquad D\ge n-3.\qquad}                              \tag{3.1}
\]

With a pre-existing rational base weight ratio P_0/Q_0 of degrees at most
D_0 and no zeros or poles at the nodes, the identical argument applies to
P Q_0-Q P_0 and gives D+D_0>=n-3. Reversing adjacent ratios does not alter
the argument, so either Pearson convention is covered.

Every word in this family is allowed and has positive probability under the
strict noisy sine law. The obstruction concerns fixed-degree closure, not a
failure of the exact displacement-rank-two identity, which survives every
word. It also does not rule out a 2x2 Riemann-Hilbert problem with a growing
number of poles, an Uvarov transformation, a different gauge, a uniform
estimate despite growing algebraic degree, or an averaged integrable method.
The latter possibilities remain open; no claim that "integrability is lost"
in all senses is made.


## 4. An allowed alternating-word family forbids a uniform bare 1/r bound

This obstruction is an analytical growing-volume statement, not a numerical
screen and not a fixed-rank example. It arose while checking whether the
weighted-inverse argument could be upgraded by simply assuming bounded
integrable-kernel endpoint functions.

### Statement

Fix ANY 0<c<1, put a=(1-c)/2, and take the actual sine compression at rho=1/2
on the sites B_M={0,...,2M}, M>=1. Use the complete output word that is zero
at even sites and one at odd sites. Let G_M be its full-word inverse.
Then

\[
 \boxed{\quad
 (2M)|(G_M)_{0,2M}|
 \ge \frac{16c^2}{\pi^2(1+c^2)^2}
       \sum_{l=0}^{M-1}\frac1{2l+1}.
 \quad}                                                     \tag{4.1}
\]

In particular no constant C(c), independent of volume and word, can satisfy
|(G_y)_ij|<=C(c)/|i-j| on this family. The same is true of the canonical
posterior kernel, since at this midpoint

\[
 |R^y_{ij}|=\frac{1-c^2}{4c}|(G_y)_{ij}|\quad(i\ne j).
                                                               \tag{4.2}
\]

A stronger, but deliberately non-sharp, elementary power lower bound is
also available. Write

\[
 \eta=\frac{c^2}{\pi^2(1+c^2)}>0,\qquad
 A_c=\frac{4\eta}{1+c^2}\,2^{-\eta}e^{-\eta^2/2}.
\]

Then

\[
 \boxed{\qquad |(G_M)_{0,2M}|\ge A_c(M+1)^{-1+\eta}.
 \qquad}                                                     \tag{4.3}
\]

Thus even a proposed word-uniform bound with exponent p>1-eta fails. No
claim that eta is the optimal exponent is made.

### Exact parity block and exterior-column Gram matrix

Order the even sites before the odd sites. The diagonal of the OUTPUT kernel
is 1/2 at these parameters. A fixed alternating phase gauge on each parity
class makes its even-to-odd block

\[
 T_{rs}=\frac1{\pi(2s+1-2r)},\quad
 0\le r\le M,\quad 0\le s\le M-1.
\]

Consequently the full-word pencil and its even inverse block are

\[
 A_y=\begin{pmatrix}-I/2&cT\\cT^*&I/2\end{pmatrix},\qquad
 (G_M)_{\rm even,even}
 =-\frac12\left(\frac14I+c^2TT^*\right)^{-1}.                 \tag{4.4}
\]

The block square identity proves (4.4) directly; its off-diagonal blocks
cancel. We now use the ambient half-density Fourier projection, not the
false assertion Q_B^2=Q_B. Its same-parity block is I/2 and its off-parity
block T_infinity satisfies T_infinity T_infinity^*=I/4. Therefore

\[
 D:=\frac14I-TT^*
   =\sum_{s\notin\{0,\ldots,M-1\}}t_s t_s^*,\qquad
 0\le D\le I/4,                                             \tag{4.5}
\]

where (t_s)_r=1/[pi(2s+1-2r)]. For every exterior column s<0 or s>=M,
all its entries have the same sign. In this fixed gauge D is consequently
entrywise nonnegative, in addition to being positive semidefinite. This
positivity is the key that permits the lower bound; it is not assumed for
an arbitrary posterior or an arbitrary word.

Set alpha_0=(1+c^2)/4 and lambda=c^2/alpha_0. Then

\[
 \left(\frac14I+c^2TT^*\right)^{-1}
 =\frac1{\alpha_0}\sum_{k=0}^{\infty}(\lambda D)^k,
 \qquad \|\lambda D\|\le\frac{c^2}{1+c^2}<1.                \tag{4.6}
\]

Every summand has nonnegative entries. All exterior sums in (4.5) converge
absolutely, and (4.6) converges in operator norm, so both uses are justified
at each finite M without any thermodynamic interchange.

### Logarithmic endpoint lower bound

The two exterior half-lines give exactly

\[
 \begin{aligned}
 D_{0M}
 &=\frac2{\pi^2}\sum_{l\ge0}
   \frac1{(2l+1)(2M+2l+1)}\\
 &=\frac1{\pi^2M}\sum_{l=0}^{M-1}\frac1{2l+1}.
 \end{aligned}                                             \tag{4.7}
\]

The second equality is the elementary telescoping difference with shift M.
Retaining just k=1 from (4.6) and then using (4.4) gives
|(G_M)_0,2M| >= c^2 D_0M/(2 alpha_0^2), which is (4.1).
The odd harmonic sum diverges, proving the asserted failure of a bare 1/r
bound at a fixed strict noise point.

### Elementary power strengthening by increasing paths

For all r,s in {0,...,M}, the LEFT exterior columns alone imply

\[
 D_{rs}\ge \frac1{\pi^2}\sum_{l\ge0}
 \frac1{(2r+2l+1)(2s+2l+1)}
 \ge\frac{\kappa}{r+s+1},\qquad \kappa=\frac1{2\pi^2}.
                                                               \tag{4.8}
\]

For the second bound compare the positive decreasing summand with its
integral on [0,infinity). If r!=s that integral is
log((2s+1)/(2r+1))/(4(s-r)), and
log v >= 2(v-1)/(v+1) for v>=1 proves the bound. The diagonal follows either
by the same integral or its limit. The logarithmic inequality itself follows
by differentiation from v=1.

In the nonnegative expansion (4.6), restrict to paths
0<r_1<...<r_{k-1}<M. The first edge has weight at least
kappa/(r_1+1); each later edge r<s has weight at least
kappa/[2(s+1)]. Including k=1, this gives

\[
 \sum_{k\ge1}\lambda^k(D^k)_{0M}
 \ge\frac{2\eta}{M+1}\prod_{j=2}^{M}\left(1+\frac\eta j\right),
 \qquad \eta=\lambda\kappa/2.                              \tag{4.9}
\]

Indeed, summing over the subsets of intermediate sites produces precisely
the product in (4.9). These are only some of the paths; entrywise positivity
justifies discarding all other paths. Empty products cover M=1.
Finally,

\[
 \prod_{j=2}^{M}(1+\eta/j)
 \ge\exp\left(\eta\sum_{j=2}^{M}\frac1j
          -\frac{\eta^2}2\sum_{j=2}^{M}\frac1{j^2}\right)
 \ge e^{-\eta^2/2}\left(\frac{M+1}2\right)^\eta.
\]

Here sum_{j=2}^M 1/j >= log((M+1)/2) and sum_{j=2}^M 1/j^2 <=1 follow by
integral comparison. Combining this with (4.4), (4.6), and (4.9) proves (4.3).

### What this forbids, and what it does not

The rank-two commutator [X,G]=-cG[X,Q]G remains exact on every word of this
family. Since one of its entries is (2M)G_0,2M, (4.1) also prevents a
rank-two factorization whose two endpoint factors are both bounded uniformly
in M and word. Thus an algebraically integrable kernel alone does not give
the uniform endpoint estimates needed by that shortcut.

This family has n=2M+1 increasing at the fixed density 1/2, and every word
has positive probability under the strict channel. It is not a cyclic Fourier
projection or a change of the kernel. The obstruction does not address the
probability-weighted size of this rare word, so it does NOT contradict the
averaged O(n/R) theorem, the small weighted exponent already proved, a
sufficiently weaker-power word-uniform bound, or the target entropy
concavity. In fact (4.3) also excludes any uniform bound of the form
C(1+log(1+r))^k/r with fixed finite k: a positive power eventually exceeds
every such logarithmic factor. The increasing-path exponent in (4.3) is only a lower-bound
exponent, not a claimed precise asymptotic.
