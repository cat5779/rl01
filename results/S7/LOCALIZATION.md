# Actual-law localization with an O(R/L) observation error

**Author proof; independent review pending.** This is the principal refinement
of the posterior-energy attempt in PROOF.md. It supersedes the very slow
observation-error term in QUASILOCALITY.md (5.2), without using that file's
weighted inverse theorem. It does not prove the sign of the local expression.

## 1. Parameters and statement

Throughout, Q_B is the actual compression of the sine projection to a finite
interval B of n integer sites, K_B=aI+cQ_B, and H_n is the Shannon entropy of
all labelled output configurations. Fix

\[
 0<c<1,\qquad 0<a<1-c,\qquad d=1-a-c,
 \quad\delta=\min(a,d),\quad m=\max(a,d),
\]
\[
 \beta_*=\delta(\delta+c),\qquad
 M=\max\left\{1,\log\frac{(a+c)(1-a)}{ad}\right\}.
\]

The constants already proved in PROOF.md are

\[
 B_* = \min\left\{\frac{3c^2}{8\delta^4},
                         \frac{3c^2}{2\beta_*^2}\right\},
 \qquad
 C_* = \min\left\{\frac{3c^4}{16\delta^8},
                         \frac{3c^2 M}{2\beta_*^2}\right\}.
 \tag{1.1}
\]

In particular, with G_y=(K_B-diag(1-y))^{-1}, their input estimates are

\[
 \mathbb E_Y\sum_{i,j\in B:\ |i-j|\ge L}|(G_Y)_{ij}|^2
 \le \frac{nB_*}{L},                              \tag{1.2}
\]
\[
 2\sum_{i<j:\ j-i\ge R}\mathbb E|g_{ij}|\le\frac{nC_*}{R}.
 \tag{1.3}
\]

All expectations are under the actual noisy sine law. The sum in (1.2) is
ordered; the sum in (1.3) is unordered with its displayed factor two.

For an output conditional probability u write f(u)=1/[u(1-u)]. For a
normalized two-site probability table p=(p00,p10,p01,p11) write

\[
 g(p)=\log\frac{p10\,p01}{p00\,p11}
 -(p10\,p01-p00\,p11)\sum_b\frac1{p_b}.
 \tag{1.4}
\]

Let u^(L) be the output conditional probability at site 0 given all other
outputs in [-L,L]. Let p^(r,L) be the conditional table for sites 0,r given
all other outputs in [-L,r+L]. Define the finite local quantity

\[
 \mathcal K_{R,L}=-\mathbb E f(u^{(L)})
                 +2\sum_{r=1}^{R-1}\mathbb E g(p^{(r,L)}).
 \tag{1.5}
\]

These are exact finite marginals, not independent-block approximations.

**Theorem F.** For all positive integers n,R,L and all 0<rho<1,

\[
\boxed{
\begin{aligned}
 \left|\frac{H_n''(a)}n-\mathcal K_{R,L}(a)\right|
 \le{}&\frac{C_*}{R}
 +\frac{B_*\delta^{-4}}{L}
       \left\{m^{-1}+156(R-1)m^{-2}\right\}\\
 &+\frac{\delta^{-2}}n
       \left[4L+M\{8L(R-1)+R(R-1)\}\right].
\end{aligned}}
 \tag{1.6}
\]

The middle term is an O_(a,c)(R/L) cost for deleting distant observations.
It is the new part of this theorem. It replaces
(4+624(R-1))delta^(-6)L^(-delta/64) in the earlier word-uniform argument.
The estimate is uniform in density and volume at fixed strict channel
parameters. Its constants diverge at the noise boundary.

## 2. Coupling two actual outside words

Let D have k=1 or k=2 sites. Let F be a subset of B\D containing every
outside site whose distance from D is less than L, and let

\[
 V=B\setminus(D\cup F).
\]

Set Z=Y_(B\D). Given Y_F, draw Z and Z' independently from its actual
conditional law. Thus the two outside words agree on F and each has the
correct unconditional outside marginal. No counting measure on words is
introduced.

For an outside word z, let C_z be the conditional kernel on D. Conditioning
the latent DPP by the observed product likelihood, and then using the
unchanged output channel on D, proves

\[
 aI_D\preceq C_z\preceq(a+c)I_D.                 \tag{2.1}
\]

Choose one fixed completion b on D: all ones when a>=d, and all zeros when
d>a. Its conditional probability obeys

\[
 p_b(z)\ge m^k.                                  \tag{2.2}
\]

Indeed it is det(C_z) in the first case and det(I_D-C_z) in the second.
This completion is an algebraic aid, not a replacement for the actual law.
Let G_z^b denote the inverse pencil for the complete word (z,b). The Schur
complement identity gives

\[
 ((G_z^b)_{DD})^{-1}
       =C_z-\operatorname{diag}(1-b)=:S_z.
 \tag{2.3}
\]

The required outside pencil is invertible by the same strict-channel gap
as the full pencil. Both S_z and S_z' have norm at most one; their eigenvalues
lie in [-1,1]. Applying the inverse identity to their inverses yields

\[
 \|C_z-C_{z'}\|
 \le\|(G_z^b-G_{z'}^b)_{DD}\|.                  \tag{2.4}
\]

The two full words differ only on V. Their pencil difference is diagonal,
supported on V, and has norm at most one. Consequently the resolvent
identity and the Hilbert--Schmidt bound imply

\[
 \|(G_z^b-G_{z'}^b)_{DD}\|
 \le\sqrt{T_D(G_z^b)T_D(G_{z'}^b)},\qquad
 T_D(G)=\sum_{i\in D,\ j\in V}|G_{ij}|^2.
 \tag{2.5}
\]

Use Cauchy--Schwarz on the joint (Z,Z') law. Equality of its two marginals,
not any independence after unconditional averaging, gives

\[
 \mathbb E\|C_Z-C_{Z'}\|\le\mathbb E_Z T_D(G_Z^b).
 \tag{2.6}
\]

Finally, (2.2) pays for the fixed completion. Since
p_(z,b)=p_z p_b(z), every nonnegative T satisfies

\[
 \mathbb E_Z T(G_Z^b)
 =\sum_z\frac{p_{(z,b)}}{p_b(z)}T(G_z^b)
 \le m^{-k}\mathbb E_Y T(G_Y).
 \tag{2.7}
\]

In the last step the indicator {Y_D=b} was discarded, so this is an
inequality, not a posterior identity. Combining (2.4)--(2.7) proves

\[
 \boxed{\quad
 \mathbb E\|C_Z-C_{Z'}\|
 \le m^{-k}\mathbb E_Y\sum_{i\in D,j\in V}|(G_Y)_{ij}|^2.
 \quad}                                         \tag{2.8}
\]

## 3. Average probability tables, not kernels

Let P_Z be the full-outside conditional probability table on D and let
P_F be the table conditional only on Y_F. The tower rule gives

\[
 P_F=\mathbb E[P_Z\mid Y_F].                    \tag{3.1}
\]

One must not replace this identity by a claim that conditional DPP kernels
average linearly. They do not. Conditional independence in the construction
of Z' and Jensen's inequality instead give

\[
 \mathbb E\|P_Z-P_F\|_\infty
 \le\mathbb E\|P_Z-P_{Z'}\|_\infty.             \tag{3.2}
\]

For a single site, its conditional probability is the sole diagonal entry
of C, so (2.8) bounds E|u_Z-u_F| with k=1. For two sites, write the conditional
kernel as [[q,zeta],[conj(zeta),r]]. Its four probabilities are

\[
 (1-q)(1-r)-|\zeta|^2,\quad q(1-r)+|\zeta|^2,
 \quad(1-q)r+|\zeta|^2,\quad qr-|\zeta|^2.
\]

By (2.1), |zeta|<=c/2<=1/2. A kernel operator-norm change of epsilon changes
each diagonal by at most epsilon and |zeta|^2 by at most epsilon. Each atom
therefore changes by at most 3epsilon. Equations (2.8) and (3.2) prove

\[
 \mathbb E\|P_Z-P_F\|_\infty
 \le3m^{-2}\mathbb E_Y
                    \sum_{i\in D,j\in V}|(G_Y)_{ij}|^2.
 \tag{3.3}
\]

Every atom of each full or coarsened table is at least delta^2. Both are
actual conditional DPP tables by the latent-field argument; no assertion
about arbitrary mixtures is used. On these tables the following elementary
Lipschitz bounds hold:

\[
 |f(u)-f(v)|\le\delta^{-4}|u-v|,
 \qquad |g(p)-g(p')|\le13\delta^{-4}\|p-p'\|_\infty.
 \tag{3.4}
\]

For completeness, the logarithmic part of g changes by at most
4epsilon delta^(-2). With s=p10 p01-p00 p11 one has 0<=s<=1/4 and
|s-s'|<=2epsilon. The difference in s sum_b 1/p_b is at most
8epsilon delta^(-2)+epsilon delta^(-4). This proves the second estimate;
the first follows by differentiating f on [delta,1-delta]. We intentionally
keep a conservative common delta^(-4) factor.

Combining these estimates gives the actual-law coarsening inequalities

\[
 \mathbb E|f(u_Z)-f(u_F)|
 \le\delta^{-4}m^{-1}\mathbb E_Y
                       \sum_{j\in V}|(G_Y)_{ij}|^2,
 \tag{3.5}
\]
\[
 \mathbb E|g(P_Z)-g(P_F)|
 \le39\delta^{-4}m^{-2}\mathbb E_Y
                     \sum_{i\in D,j\in V}|(G_Y)_{ij}|^2.
 \tag{3.6}
\]

## 4. Summation and boundary accounting

Start with the exact Hessian in PROOF.md:

\[
 H_n''=-\sum_i\mathbb E f(u_i)
             +2\sum_{i<j}\mathbb E g(P_{ij}).     \tag{4.1}
\]

Discard pair distances >=R with the paid error (1.3). For a single site
whose [-L,L] translate lies inside B, sum (3.5). Each V is contained in
{|j-i|>=L}, so (1.2) bounds the total by

\[
 nB_*\delta^{-4}m^{-1}/L.                        \tag{4.2}
\]

For every interior pair i<j with j-i<R, use the translate of [-L,j-i+L]
as its local observed block. Each endpoint occurs in at most 2(R-1) such
pairs, and each V is contained in the distance-L complement of either
endpoint. Therefore the sum of (3.6), including the factor two in (4.1),
is at most

\[
 2\cdot39\cdot2(R-1)\delta^{-4}m^{-2}\frac{nB_*}{L}
 =156(R-1)\delta^{-4}m^{-2}\frac{nB_*}{L}.
 \tag{4.3}
\]

There are at most 2L boundary sites. Since f<=delta^(-2), replacing them
by the local expectation costs at most 4L delta^(-2).
For a fixed distance r<R, at most 2L existing pairs have local windows
not contained in B. The bound |g|<=M delta^(-2), obtained from the
inverse formula in PROOF.md, gives a replacement cost at most
8L M delta^(-2), after including the unordered-pair factor two.
The absent fraction r/n of the distance-r pairs costs an additional
2r M delta^(-2)/n in the normalized expression. When r>=n there are no
such pairs and r/n>=1 remains a valid overestimate. Summing r=1,...,R-1
and dividing (4.2)--(4.3) by n proves (1.6).

This counts the entire Fisher diagonal and the entire mixed pair functional.
It never differentiates an already-averaged object while freezing its law.

## 5. Rate limit and a polynomial finite-volume estimate

On a compact J inside (0,1-c), all constants in (1.6) are uniformly bounded.
Choose R large, then L large compared with R, then n large compared with LR.
Comparison to the same finite function K_(R,L) proves that H_n''/n is uniformly
Cauchy on J. Since these finite functions are continuous, its limit is
continuous. The normalized entropies converge pointwise by stationarity and
block-entropy subadditivity. Integrating the uniformly converging second
derivatives and fixing the affine terms at two distinct points proves that
the limiting entropy rate h is C^2 in the strict interior. This reasoning is
independent of QUASILOCALITY.md.

Taking n to infinity in (1.6) gives the fully finite enclosure

\[
 \boxed{\quad
 |h''(a)-\mathcal K_{R,L}(a)|
 \le\frac{C_*}{R}
 +\frac{B_*\delta^{-4}}L\{m^{-1}+156(R-1)m^{-2}\}.
 \quad}                                         \tag{5.1}
\]

One also obtains an explicit polynomial finite-volume rate by comparing
H_n''/n and h'' through this same K_(R,L). For n>=16, set
R=floor(n^(1/4)) and L=ceil(n^(1/2)). Then R>=n^(1/4)/2,
L>=n^(1/2), L<=2n^(1/2), and R<=n^(1/4). Consequently

\[
 \boxed{\quad
 \left|\frac{H_n''}n-h''\right|
 \le D_*(a,c)n^{-1/4},\qquad
 D_*=4C_*+2B_*\delta^{-4}(m^{-1}+156m^{-2})
                  +\delta^{-2}(8+17M).
 \quad}                                         \tag{5.2}
\]

For example, the boundary term in (1.6) is bounded by
 delta^(-2)[8n^(-1/2)+16M n^(-1/4)+M n^(-1/2)], which is at most the last
term in D_* times n^(-1/4). The two copies of the first two errors in (1.6)
and (5.1) give the other terms. This is a conservative rate, not an optimal
one or a claim of superiority over every existing finite-volume estimate.

## 6. Scope and what still must be proved

The basic C^2 conclusion is not claimed as absent from the reviewed baseline:
S6's response estimate and the reviewed value tails provide another route.
The new statements here are the actual-law coarsening inequalities
(2.8), (3.5)--(3.6), their explicit spatial enclosure (1.6)/(5.1), and its
polynomial realization (5.2).

To conclude concavity, one still needs an upper bound on K_(R,L) that pays
the two positive errors in (5.1), uniformly in the desired high-contrast
parameters. No such near-field sign certificate is supplied. The constants
are large near the channel boundary; no efficient numerical completion is
asserted. In particular, the growing alternating-word obstruction and the
positive averaged six-site pair in OBSTRUCTIONS.md are compatible with this
localization theorem and do not by themselves refute entropy concavity.
