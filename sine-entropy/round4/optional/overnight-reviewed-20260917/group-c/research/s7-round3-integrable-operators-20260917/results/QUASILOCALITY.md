# A second spatial estimate: uniformly over all output words

**Author proof, pending independent review.** This supplements PROOF.md.
It does not assert a near-field sign or an endpoint-uniform bound.

## 1. Statement and why the usual inverse-decay citation is insufficient

Use the notation of PROOF.md, and put

\[
 \alpha=\delta/128>0.
\]

For every center o in B, every output y, and every n,rho,

\[
 \boxed{\quad
 \sum_{j\in B}(1+|j-o|)^{2\alpha}|(G_y)_{jo}|^2
 \le4\delta^{-2}.\quad}                            \tag{1.1}
\]

If two complete words agree at all sites at distance less than L from a
one- or two-site set D, the conditional one- or two-site laws on D differ
by explicit O_delta(L^(-2alpha)) bounds below. This controls arbitrary bad
words, not just typical words.

A standard polynomial-decay inverse-closedness theorem with decay exponent
s>dimension cannot simply be applied to the sine kernel's critical 1/|i-j|
bound. The proof here is instead an elementary small weighted-commutator
estimate. It deliberately pays a small exponent depending on the spectral
gap; no uniform 1/|i-j| entry bound is claimed.

## 2. The weighted commutator with an explicit constant

Let w_i=1+|i-o|, W_t=diag(w_i^t). For |t|<=1/4 define

\[
 E_t=W_tQ_BW_t^{-1}-Q_B.
\]

We prove

\[
 \|E_t\|\le64|t|.                                  \tag{2.1}
\]

This also holds on any finite subset of Z. To see it, use the weighted Schur
test with h_i=w_i^(-1/2), and |(Q_B)_ij|<=1/(pi|i-j|) off the diagonal.
At a fixed i put v=w_i. There are at most two sites with any specified
integer value u=w_j. Also |v-u|<=|i-j|. The diagonal contribution is zero.

For u in [v/2,2v], the mean-value bound on r^t, r=v/u, gives

\[
 |r^t-1|r^{1/2}\le2|t||\log r|,
 \qquad |\log v-\log u|\le2|v-u|/v.
\]

Each weighted summand is therefore at most 4|t|/(pi*v). There are at most
4v such sites (including a direct check when v=1), giving 16|t|/pi.

For u<v/2, the weighted summand is bounded by

\[
 \frac{2|t|}{\pi v}(v/u)^{3/4}\log(v/u).
\]

Counting both sites at each u, the sum is at most 64|t|/pi because
x^(-3/4)log(1/x) decreases on (0,1] and

\[
 \frac1v\sum_{u\le v/2}(u/v)^{-3/4}\log(v/u)
 \le\int_0^1 x^{-3/4}\log(1/x)\,dx=16.
\]

For u>2v, the sum is at most

\[
 \frac{4|t|}{\pi v}\sum_{u>2v}F(u/v),\qquad
 F(x)=x^{-5/4}\log x.
\]

Here F is nonnegative and unimodal on [1,infinity), its integral is 16,
and its maximum is (4/5)e^(-1)<1. A mesh of size 1/v has upper Riemann-sum
error at most (total variation of F)/v <=2/v. Thus

\[
 \frac1v\sum_{u>2v}F(u/v)\le18,
\]

and this part costs at most 72|t|/pi. The weighted row sum is consequently
at most 152|t|/pi <64|t|. The same column estimate follows by replacing t by
-t, since E_t^*=E_(-t). The weighted Schur test proves (2.1).

For clarity, the Riemann-sum estimate just used follows on each mesh interval
by bounding the discrepancy between a sampled value and the interval average
by the variation on that interval. Summing gives at most the mesh size times
the total variation. Extending the sum from u>2v to u>=v only increases it.
No unproved inverse-closedness theorem is hidden in this step.

## 3. Weighted inversion and distant changes of a word

The word mask commutes with W_alpha. By (2.1),

\[
 W_\alpha A_y W_\alpha^{-1}=A_y+cE_\alpha,
 \qquad \|cE_\alpha\|\le c\delta/2\le\delta/2.
\]

The gap \(\|A_y^{-1}\|\le\delta^{-1}\) and a Neumann series now give

\[
 \|W_\alpha G_y W_\alpha^{-1}\|\le2/\delta.
\]

Taking the column at o, for which w_o=1, proves (1.1). Since G_y is Hermitian,
the corresponding weighted row estimate holds too.

Let y,y' agree at sites with distance less than L from D, including the
same chosen completion on D. Their difference is supported on sites at
distance at least L from every i in D. The resolvent identity and
Cauchy--Schwarz, with (1.1) at the two row centers, imply

\[
 |(G_y-G_{y'})_{ij}|\le4\delta^{-2}L^{-2\alpha}
 \quad(i,j\in D).                                 \tag{3.1}
\]

Indeed A_y-A_y' is diagonal, of norm at most one, supported only on those
far sites. Each of the two restricted squared row norms is at most
4 delta^(-2)L^(-2alpha).

Choose completion 1 at a single site, or completion 11 on a pair. The Schur
complement identity says that the conditional kernel on D is (G_DD)^(-1).
Both conditional kernels have norm at most one. For a single site this gives

\[
 |u_y-u_{y'}|\le4\delta^{-2}L^{-2\alpha}.            \tag{3.2}
\]

For a pair, the operator norm of the two-by-two block difference in (3.1)
is at most 8 delta^(-2)L^(-2alpha), hence the difference of the conditional
kernels has that same bound. Each of their four probabilities is a degree-two
expression in its two diagonal entries and the squared modulus of its
off-diagonal. The off-diagonal modulus is at most c/2<=1/2. It follows that

\[
 \max_b|p_b^y-p_b^{y'}|\le24\delta^{-2}L^{-2\alpha}.
 \tag{3.3}
\]

For example, the difference of qr-|zeta|^2 is at most three times the kernel
operator-norm difference. The other three atoms satisfy the same bound.

## 4. Discarding distant observations is paid, not a kernel-mixture claim

Fix a set F of observed sites outside D, containing every such site whose
distance from D is less than L. The conditional probability TABLE given Y_F
is the conditional average of the full-outside table over its remaining
completions. Equations (3.2)--(3.3) therefore hold also between any full table
and this coarsened table. This uses linear averaging of probabilities;
it does not average conditional DPP kernels and declare the mixture to have
that kernel.

Both the coarsened and full pair laws are actual conditional DPP laws via the
latent-field argument of PROOF.md. Their four atoms are at least delta^2.
As a function of a two-site probability table p=(A,B,C,D), the pair functional
is

\[
 g(p)=\log\frac{BC}{AD}-(BC-AD)(A^{-1}+B^{-1}+C^{-1}+D^{-1}).
 \tag{4.1}
\]

If the maximum atom difference is epsilon, then
|Delta(BC-AD)|<=2epsilon; the coefficients sum to at most two when the two
product differences are expanded. The logarithmic part changes by at most
4epsilon delta^(-2). The other part changes by at most
8epsilon delta^(-2)+epsilon delta^(-4), since 0<=BC-AD<=1/4.
Consequently

\[
 |g(p)-g(p')|\le13\epsilon\delta^{-4}.
\]

Together with (3.3) this gives the word-uniform and coarsening bounds

\[
 \boxed{\quad |g_{\rm full}-g_F|\le
 312\delta^{-6}L^{-2\alpha}.\quad}                 \tag{4.2}
\]

The one-site function f(u)=1/[u(1-u)] has derivative bounded by delta^(-4)
on [a,a+c]. Therefore

\[
 \boxed{\quad |f(u_{\rm full})-f(u_F)|\le
 4\delta^{-6}L^{-2\alpha}.\quad}                   \tag{4.3}
\]

These statements hold under the actual observations, without losing their
weights when the expectation is taken.

## 5. A fully finite, local curvature approximation

For L>=1 let u^(L) be the conditional probability of the output at 0 given
the other outputs in [-L,L]. For r>=1 let g^(r,L) be the exact pair functional
for the sites 0,r, given all other outputs in [-L,r+L]. All distributions here
are finite marginals of the actual noisy sine process. Set

\[
 \mathcal K_{R,L}(a)=
 -\mathbb E f(u^{(L)})+2\sum_{r=1}^{R-1}\mathbb E g^{(r,L)}.
 \tag{5.1}
\]

Let C(a,c), M and delta be as in PROOF.md. For all positive integers n,R,L,

\[
 \boxed{
 \begin{aligned}
 \left|\frac{H_n''(a)}n-\mathcal K_{R,L}(a)\right|
 \le{}&\frac{C(a,c)}R
 +(4+624(R-1))\delta^{-6}L^{-2\alpha}\\
 &+\frac{\delta^{-2}}n\left[
 4L+M\{8L(R-1)+R(R-1)\}\right].
 \end{aligned}}
 \tag{5.2}
\]

Proof: first discard pair distances >=R using Theorem A. For a site at least
L from the boundary, (4.3) pays its replacement by the local single-site
conditional law. At most 2L sites are boundary sites; the absolute difference
of two single-site f values is at most 2 delta^(-2), costing
4L delta^(-2)/n.

For each distance r<R there are at most 2L boundary pairs. The bound
|g|<=M delta^(-2) follows from PROOF.md (5.6) and the two-site inverse norm
bound. Thus boundary replacement costs at most 4L M delta^(-2)/n before the
factor two for unordered pairs. The missing fraction r/n of pairs costs at
most r M delta^(-2)/n. This remains an upper bound when r>=n and there are no
such pairs. For all other pairs use (4.2). Summing r=1,...,R-1 proves (5.2).

All entries of (5.1) are finite true-law quantities. Formula (5.2) is neither
an independent-block assumption nor a value-to-Hessian inference. The second
error is often very expensive: 2alpha=delta/64 is a small exponent. This is a
qualitative uniform localization theorem with explicit constants, not a claim
that high-contrast numerical certification is already practical.

## 6. Consequences and overlap with reviewed S6

For fixed c and a compact J inside (0,1-c), use its positive minimum delta
in the exponent and bounds. First choose R large, then L so large that
R L^(-delta/64) is small, then n so large that the displayed boundary term is
small. Equation (5.2) shows that H_n''/n is a uniformly Cauchy family on J.
Every local quantity (5.1) is smooth in a. Hence the curvature limit is
continuous on J.

The normalized entropies themselves converge to the stationary entropy rate:
block-entropy subadditivity proves existence of the pointwise limit. The
uniform curvature bound and convergence at two distinct points imply C^2
convergence on each smaller compact interval. Explicitly, subtract the
integral of the uniformly converging second derivatives; the remaining affine
functions have converging coefficients determined by those two points.

Thus a spatially local formula for h'' is supplied by the limits of (5.1), with
(5.2)'s paid errors. The mere existence/C^2 convergence conclusion is NOT
claimed as a new consequence unavailable in the baseline: reviewed S6's
Chebyshev-response lemma combined with reviewed entropy value tails already
provides another route to it. The new content here is the uniform-word
weighted inverse/coarsening bound and the explicit true-law spatial curvature
approximation. None of these establishes that the limit in (5.1) is
nonpositive at all high contrasts.

## 7. Optional stronger distance tail

The entry bound from (1.1), together with the quartic estimate of PROOF.md,
also implies a slightly faster absolute curvature tail. Write

\[
 B(a,c)=\min\left\{\frac{3c^2}{8\delta^4},
                       \frac{3c^2}{2\beta_*^2}\right\}.
\]

For a pair at distance at least R, each completion satisfies
|G_ij|^2<=4 delta^(-2)R^(-2alpha) and |zeta|^2<=|G_ij|^2. Hence

\[
 |g|\le2\delta^{-4}|\zeta|^4
 \le8\delta^{-6}R^{-2\alpha}|G_{ij}|^2.
\]

Averaging and summing the ordered inverse tail from Theorem C gives

\[
 \boxed{\quad
 2\sum_{i<j,\ j-i\ge R}\mathbb E|g_{ij}|
 \le8\delta^{-6}B(a,c)\frac n{R^{1+2\alpha}}.
 \quad}                                            \tag{7.1}
\]

The constants are substantially worse than the logarithmic-odds constant in
Theorem A; (7.1) is not uniformly the better numerical estimate. It is useful
only as an additional large-R summability statement at a fixed positive gap.
