# Why count-preserving layer bistochasticity cannot pay the remaining sign

**Author theorem, subject to independent review.** This is a counterexample
to a possible spectral-observation-channel proof step, not to DPP entropy
concavity. It is included because `SCORE_COMPENSATION.md` legitimately uses a
fixed, count-preserving spectral channel. The theorem below identifies a
property of that channel that is insufficient to control the next-order sign.

## 1. The candidate bridge and its precise failure

The spectral construction of a DPP observes independent Bernoulli eigenmodes
through a channel whose `k`th cardinality block is the matrix
`|det U_{A,S}|^2`, `|A|=|S|=k`. Every such block is doubly stochastic.
A tempting strengthening of the finite score argument would be:

> Any fixed channel that preserves count and is doubly stochastic on every
> count layer preserves entropy concavity along a common affine shift of
> independent Bernoulli input parameters.

This statement is false, even with two complementary input eigenvalues,
fixed contrast, rank proportion `1/2`, and growing dimension. Here is a
complete counterexample and its leading curvature asymptotic.

Fix `0<c<1`, put

\[
 \alpha=(1-c)/2,\quad \beta=(1+c)/2,\quad
 v=\alpha\beta>0,\quad n=2r.
\]

The labelled input has `r` independent `Ber(beta+delta)` coordinates and `r`
independent `Ber(alpha+delta)` coordinates. All its parameters are shifted by
the same `delta`, and `|delta|<alpha`. Define a fixed stochastic channel:

* If the input has cardinality `r`, output that very configuration.
* At every other cardinality `k`, output a uniformly chosen `k`-subset,
  independently of the input configuration inside that layer.

Each layer is either the identity matrix or the all-uniform matrix. Thus the
channel preserves count exactly and is doubly stochastic on every layer.
Denote the full labelled output entropy by `H_n^out(delta)`.

### Theorem

\[
 \boxed{\quad
 \frac{(H_n^{\rm out})''(0)}{n^{3/2}}
 \longrightarrow
 \frac{\log2-b(\alpha)}{v\sqrt{2\pi v}}>0.
 \quad} \tag{1.1}
\]

In particular the proposed bridge fails for all sufficiently large even `n`,
for every fixed nonzero contrast `c`. The theorem does not replace the full
entropy by count entropy: the calculation below retains the entire spatial
conditional entropy, and it is precisely that term which creates the sign.

## 2. Exact complete-entropy decomposition

Let `M` be the input and output count, let `pi_k(delta)=Pr_delta(M=k)`, and
write `H_r(delta)=H(Z|M=r)` for the input's full spatial entropy on the middle
layer. Introduce the entropy of the completely exchangeable output

\[
 H_n^{\rm sym}(\delta)=H(M)+\sum_{k=0}^n\pi_k(\delta)\log\binom nk,
\]

and the middle-layer spatial deficit

\[
 D_r(\delta)=\log\binom nr-H_r(\delta).
\]

The defined channel gives the exact identity

\[
 H_n^{\rm out}(\delta)=H_n^{\rm sym}(\delta)-\pi_r(\delta)D_r(\delta).
 \tag{2.1}
\]

At zero, complementing all coordinates and interchanging the two input groups
leaves the model invariant and changes `delta` to `-delta`. In particular
`pi_r'(0)=D_r'(0)=0`, so

\[
 (H_n^{\rm out})''(0)
 =(H_n^{\rm sym})''(0)-\pi_r''(0)D_r(0)-\pi_r(0)D_r''(0).
 \tag{2.2}
\]

We will prove

\[
 \pi_r(0)\sim(2\pi nv)^{-1/2},\quad
 \frac{\pi_r''(0)}{n\pi_r(0)}\to-1/v,\quad
 \frac{D_r(0)}n\to\log2-b(\alpha),
 \tag{2.3}
\]

\[
 D_r''(0)=O_c(n),\qquad
 |(H_n^{\rm sym})''(0)|=O_c(n\log(n+1)).
 \tag{2.4}
\]

These estimates inserted into (2.2) give (1.1). All constants below are for
fixed `c<1`; no uniform `c->1` assertion is intended.

## 3. Count probability and its actual affine-shift derivative

Pair one coordinate from each group. The centered pair count has characteristic
function

\[
 \psi_\delta(t)=1-2v(1-\cos t)+2i\delta\sin t
                         -2\delta^2(1-\cos t).
\]

Therefore Fourier inversion and differentiation of this finite polynomial give

\[
 \pi_r(0)=\frac1{2\pi}\int_{-\pi}^{\pi}\psi_0(t)^r dt,
\]
\[
 \pi_r''(0)=\frac1{2\pi}\int_{-\pi}^{\pi}
 \left[-4r(r-1)\sin^2t\,\psi_0(t)^{r-2}
       -4r(1-\cos t)\,\psi_0(t)^{r-1}\right]dt.
 \tag{3.1}
\]

Because `0<v<1/4`, `psi_0(t)=1-2v(1-cos t)` is positive and strictly below
one away from zero modulo `2pi`. Near zero,
`psi_0(t)=1-vt^2+O_c(t^4)`. The change of variables `t=z/sqrt(r)` in (3.1)
and dominated convergence give

\[
 \sqrt r\,\pi_r(0)\to\frac1{2\sqrt{\pi v}},\qquad
 \frac{\pi_r''(0)}{r\pi_r(0)}\to-2/v.
\]

Here are explicit domination details. For `|t|<=pi`,
`1-cos t>=2t^2/pi^2` and `1-x<=exp(-x)` imply
`psi_0(t)^m<=exp(-4vm t^2/pi^2)`. Also `sin^2 t<=t^2` and
`1-cos t<=t^2/2`. For `r>=4`, the rescaled integrands are bounded by a fixed
constant times `(1+z^2)exp(-2v z^2/pi^2)`. The first derivative integral's
leading term uses
`int z^2 exp(-v z^2)dz / int exp(-v z^2)dz=1/(2v)`;
the other term is lower order after division by `r pi_r(0)`.
Thus the first two limits of (2.3) are proved, retaining the true parameter
acceleration `-4(1-cos t)` rather than using the exponential-tilt path.

## 4. The middle layer's full spatial entropy and curvature

Let `J` be the occupied count among the first, `beta`-probability group.
For a labelled input word in the middle layer, its probability at displacement
`delta` is

\[
 p_\delta(z)=(\beta^2-\delta^2)^J
                        (\alpha^2-\delta^2)^{r-J}.
 \tag{4.1}
\]

The multiplicity of a given `J=j` is `binom(r,j)^2`; it is not discarded.
At zero,

\[
 \log p_0(z)=2J\log\beta+2(r-J)\log\alpha.
\]

Unconditionally, `J/r->beta` with exponentially small deviation tails.
Conditioning on `M=r` divides those tail bounds only by
`pi_r(0)~const/sqrt(r)`. Thus
`E[J|M=r]/r->beta`. Using the exact conditional entropy formula

\[
 H_r(0)=-\mathbb E[\log p_0(Z)\mid M=r]+\log\pi_r(0)
\]

gives `H_r(0)/n->b(alpha)`. Also
`log binom(n,r)/n->log2`, for example from
`2^n/(n+1)<=binom(n,r)<=2^n`. This proves the third limit of (2.3).

Each middle-layer word has zero first derivative at zero. Its second log
probability, from (4.1), is

\[
 -\frac{2r}{\alpha^2}+B J,
 \qquad B=2(\alpha^{-2}-\beta^{-2})=2c/v^2.
\]

After normalizing within the middle layer the atom acceleration is
`B(J-E[J|M=r])`. Consequently the actual spatial entropy derivative is

\[
 H_r''(0)=-2B\log(\beta/\alpha)\operatorname{Var}(J\mid M=r),
\]
\[
 D_r''(0)=\frac{4c\log(\beta/\alpha)}{v^2}
                        \operatorname{Var}(J\mid M=r)\ge0.
 \tag{4.2}
\]

To bound its size, conditional independent Bernoulli coordinates with a
fixed total have pairwise nonpositive covariances. An elementary verification
suffices here: write their odds as positive weights, remove two coordinates,
and let `e_j` be the elementary symmetric polynomials of the remaining
weights. The covariance numerator is a positive factor times
`e_{r-2}e_r-e_{r-1}^2<=0`, by Newton's inequality (with the harmless boundary
terms set to zero). Hence

\[
 \operatorname{Var}(J\mid M=r)
 \le\sum_{i=1}^r\operatorname{Var}(Z_i\mid M=r)\le r/4.
\]

Equation (4.2) is therefore `O_c(n)` as claimed. This calculation explicitly
keeps the moving spatial law; replacing it by a uniform middle layer would
remove the counterexample.

## 5. Bounding the exchangeable entropy curvature without assuming its sign

At zero the latent common-shift score is

\[
 S=(M-r)/v,
\]

and its log derivative is

\[
 T=-n/v-v^{-2}\sum_i(1-2\lambda_i)(Z_i-\lambda_i),
 \quad \lambda_i\in\{\alpha,\beta\}.
\]

The count score is exactly `S`, and its atom acceleration is
`a_M=E[S^2+T|M]`. Independence and fourth-moment expansion show

\[
 \|a_M\|_2\le C_c n,
 \qquad \mathbb ES^2=n/v.
 \tag{5.1}
\]

For clarity, one may take

\[
 C_c=(\sqrt3+1)/v+(1+c)/v^{3/2},
\]

since `E(M-r)^4<=3n^2v^2+nv`, and the fluctuation part of `T` has variance
`c^2n/v^3`. Also `E a_M=0`, by normalization.

The full exchangeable atom logarithm is
`ell(M)=log pi_M-log binom(n,M)`. Its centered `L^2` norm is only logarithmic,
not extensive. First, for any probability distribution on `m` points,

\[
 \mathbb E(\log p_X)^2
 \le(\log m)^2+2\log m+2.
 \tag{5.2}
\]

Indeed `Pr(-log p_X>t)<=min(1,m exp(-t))`; integrate its tail against `2t`.
Second, set `g(k)=log binom(n,r)-log binom(n,k)>=0`. The elementary type bounds

\[
 \binom nk\ge\frac{e^{n b(k/n)}}{n+1},\qquad
 \binom nr\le2^n
\]

imply

\[
 g(k)\le4\log2\,(k-r)^2/n+\log(n+1).
 \tag{5.3}
\]

The first type bound follows because `k` is a mode of `Bin(n,k/n)`, whose
largest probability is at least `1/(n+1)`. For the entropy inequality used
in (5.3), the binary-entropy power series gives
`log2-b((1+x)/2)<=x^2 log2` for `|x|<=1`.

Equations (5.2)--(5.3) and the fourth moment bound imply

\[
 \|\ell(M)+\log\binom nr\|_2=O_c(\log(n+1)).
\]

The exact finite entropy second derivative is thus bounded by

\[
 |(H_n^{\rm sym})''(0)|
 =| -\mathbb E[a_M\ell(M)]-\mathbb ES^2 |
 \le C_c n\,O_c(\log(n+1))+n/v.
\]

This proves (2.4) without assuming a sign for `H_n^sym` and completes the
proof of Theorem (1.1).

## 6. Why this is not a DPP counterexample

For `n>=4`, this particular channel cannot be the simultaneous exterior-power
channel of a single unitary. Its one-particle block is the uniform matrix, so
such a unitary would have `|U_ij|^2=1/n`. Its middle exterior-power block is
the identity, so every coordinate `r`-dimensional subspace would be invariant
under `U`. Intersecting all such coordinate subspaces containing a fixed
coordinate axis shows that each axis is itself invariant. The unitary would
therefore be diagonal, contradicting the uniform one-particle block.

Thus the proof step is delimited exactly: fixedness, count preservation,
layerwise double stochasticity, complementary input eigenvalues, and fixed
positive rank density are **not enough**. A successful DPP argument has to
use the compatibility of the minors of one common unitary, or another
property not shared by this channel. The finite score and local-likelihood
estimates in `SCORE_COMPENSATION.md` remain valid; this theorem explains why
those estimates alone cannot pay the entropy curvature sign.

One stronger property is deliberately not disproved here: commutation with
uniform deletion. For the constructed channel, deleting from an unchanged
middle-layer set produces only its own subsets, whereas deleting first and
then applying the uniform (r-1)-layer channel produces all (r-1)-subsets.
Thus this channel does not commute with deletion. A proposed bridge using
that additional property is not refuted merely by the present example.

The floating table produced by `probe_spectral_layer_bridge.py` is an author
diagnostic of the asymptotic formula, not its proof or an independent review.
The theorem itself is the analytic argument above.
