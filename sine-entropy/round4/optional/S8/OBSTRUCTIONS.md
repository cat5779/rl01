DISPROVED_ROUTE_LEMMA

# Exact limits of the higher-rank balancing mechanism

These are **method** obstructions for genuine rank-two projection DPPs, not
counterexamples to entropy concavity or the sine-rate target. The positive
four-cycle theorem is in [RESULT.md](RESULT.md). All coordinates in this note
are numbered from one; the checker and JSON masks use zero-based indices.
Evidence level: author proofs and exact finite certificates, not independent
review or a literature-priority claim.

## 1. Even a monotone leverage-balancing physical rotation can reverse the curvature order

### The precise false proposal

Consider a real coordinate rotation affecting only two rows of a projection.
Suppose their diagonal imbalance decreases monotonically during the rotation,
and the complete channel entropy at the final projection is greater than at
the initial projection. The proposed extension of S2 would conclude that this
entropy gain is convex in the channel offset `a`.

That implication is false, even for a full-support rank-two projection on
four sites at a strictly interior high-contrast parameter.

### Exact projection data

Let

\[
 W=\begin{pmatrix}-7&-4\\6&-3\\-2&4\\5&0\end{pmatrix},
 \quad W^*W=\begin{pmatrix}114&2\\2&41\end{pmatrix},
 \quad\det(W^*W)=4670,
\]
\[
 P=W(W^*W)^{-1}W^*,\qquad
 R=\frac1{13}\begin{pmatrix}12&5\\-5&12\end{pmatrix}
       \oplus I_2,\qquad Q=RPR^* .                       \tag{A1}
\]

Both kernels are exactly Hermitian projections of rank two. Their input
pair atoms are the squared minors of `W` and `RW`, divided by 4670.
All six are positive. Thus no free-pair or non-DPP substitute is involved.

For `P`, the first diagonal difference and off-diagonal entry are

\[
 d=P_{11}-P_{22}=1147/4670>0,\qquad r=P_{12}=-174/2335<0.
\]

Along `R(theta)` from zero to `theta_*=arctan(5/12)<pi/4`, the difference is
`d(theta)=d cos(2theta)+2r sin(2theta)`. Its derivative is strictly negative
throughout this interval, and its final value is

\[
 d(\theta_*)=52973/789230>0.                             \tag{A2}
\]

The absolute diagonal imbalance therefore decreases monotonically, without
crossing zero. This is stronger than checking only a smaller endpoint imbalance.

### Certified complete-entropy signs

At `c=19/20`, `a=1/200`, exact rational logarithm enclosures give

\[
 H_Q-H_P\in[0.006986083032,\ 0.006986083033],
\]
\[
 \boxed{H_Q''-H_P''\in[-1.737115357632,\ -1.737115357631].} \tag{A3}
\]

The individual Hessians are negative:

\[
 H_P''\in[-373.866400431115,-373.866400431114],
\]
\[
 H_Q''\in[-375.603515788747,-375.603515788746].             \tag{A4}
\]

The file [rotation.json](certificates/rotation.json) stores all sixteen complete
atoms and their first two `a` derivatives for both kernels, with only duplicate
jet triples interned. It also stores all input minors, the frame, rotation,
and exact diagonal data. The checker obtains the jets both by direct channel
products and independently from the rank-two determinant formula.

This refutes the specified **real-rotation curvature comparison**, not the
projection-compatible affine quadrature chord of RESULT.md. The real rotation
in (A1) is not that chord. No statement that entropy increases monotonically
at every intermediate angle is needed or asserted; its endpoint increase is
certified, and leverage balancing is monotone along the whole angle interval.

## 2. The exact signed extension beyond a four-cycle

Let `U` be a real rank-two isometry with `h_i=h_j`, but remove the two-support
condition (1) of RESULT.md. Keep the same projection-preserving quadrature
swap `U_s`, and define, for every outside coordinate,

\[
 d_r=\mu_{jr}-\mu_{ir},\qquad\sum_{r\notin\{i,j\}}d_r=0.
                                                        \tag{B1}
\]

The zero sum follows by summing pair atoms incident to the two equal-leverage
sites. With `R=||z||^2`, `E_r=|u_r^s z|^2`, and `x=a(1-c-a)`, the interpolation
Fisher information has the exact positive representation

\[
 I_s(a)=c^4\int_{\mathbb C^2} e^{-xR}
 (e^{-cE_i}+e^{-cE_j})
 \frac{\mathbb E_{B_a}\left[
       (\sum_r d_r X_r)^2e^{-c\sum_r E_rX_r}\right]}
      {a(1-a)}\,\frac{d^4z}{\pi^2}.                     \tag{B2}
\]

Here `B_a` is the product `Ber(a)` law on **all** outside coordinates.
This follows from (8), (12) of RESULT.md; no output context is omitted.
The extra factor `1/[a(1-a)]` is real and cannot be discarded.

For binary `X` and a zero-sum vector `d`, the algebraic identity

\[
 (\sum_r d_rX_r)^2
 =-\sum_{r<v}d_rd_v(X_r-X_v)^2                           \tag{B3}
\]

is verified by comparing the coefficients of `X_r` and `X_rX_v`.
The Bernoulli expectation of a term on the right, including its exponential
weight, cancels `a(1-a)` exactly. Thus

\[
 I_s(a)=-c^4\sum_{r<v}d_rd_v J_{rv,s}(a),                \tag{B4}
\]

where

\[
 J_{rv,s}(a)=\int e^{-xR}(e^{-cE_i}+e^{-cE_j})
 (e^{-cE_r}+e^{-cE_v})
 \prod_{w\notin\{i,j,r,v\}}(1-a+ae^{-cE_w})
 \frac{d^4z}{\pi^2}.                                    \tag{B5}
\]

Each `J` is convex for `c>=1/4` by the same common-isometry estimate proved in
RESULT.md. But the coefficients `-d_rd_v` are negative for same-sign pairs.
The four-cycle theorem has only two nonzero, opposite `d` entries, so all
surviving coefficients are positive. A general equal-leverage swap does not.

Equations (B2)--(B5) are a surviving **signed** formulation, not a proof of its
sign. The next obligation would be an integrated comparison paying the
same-sign terms. Neither simply dropping them nor requiring the full density
in (B2) to be pointwise convex is legitimate, as the next example proves.

## 3. Pointwise convexity fails even after summing every outside word

### A connected genuine projection, not a free homogeneous law

Put `L=31`, `n=L+3=34`, and take rows

\[
 u_1=(1,1)/2,\qquad u_2=(1,-1)/2,\qquad
 u_3=(3,4)/\sqrt{50},
\]
\[
 u_{3+r}=(-4,3)/\sqrt{50L},\qquad1\le r\le L.            \tag{C1}
\]

The first two row outer products sum to `I_2/2`; the remaining rows have
outer-product sum `I_2/2`. Hence `U^*U=I_2` exactly. The first two leverages
are `1/2`, so the full quadrature chord stays inside projection DPPs.
The covariance graph is connected: both first rows have nonzero inner products
with both outside row directions. The outside clones are parallel but are
not independent coordinate components.

The actual compatible minor differences are

\[
 d_3=\eta=6/25,\qquad d_{3+r}=-\eta/L.                  \tag{C2}
\]

All Pluecker relations come from (C1); the checker additionally verifies their
raw two-row determinant identities for all 46,376 coordinate quadruples.

### Exact negative second derivative of the summed Gaussian density

Fix

\[
 s=1/2,\quad c=19/20,\quad a=1/1000,\quad
 z=(12/5,16/5)\in\mathbb R^2\subset\mathbb C^2.           \tag{C3}
\]

Then `R=16`; after the quadrature rotation, `E_1=E_2=4`, while `E_3=8`
and every clone energy is zero. Set `epsilon=exp(-38/5)`. Summing all outside
words in (B2), **before** taking a derivative, gives the density

\[
 2c^4\eta^2e^{-19/5}\, e^{-16x}\,[p_0+a d_0],
\quad p_0=\epsilon+1/L,\quad
 d_0=(1-\epsilon)(1-1/L).                               \tag{C4}
\]

To check the sum explicitly, let `B=X_3` and `K` count occupied clones under
`B_a`. They are independent, `B~Ber(a)`, `K~Bin(L,a)`. The square in (B2) is
`eta^2(B-K/L)^2` and its exponential weight is `epsilon^B`. Using the exact
first and second binomial moments gives

\[
 \frac{\mathbb E[(B-K/L)^2\epsilon^B]}{a(1-a)}=p_0+a d_0.
\]

The sign of the `a` second derivative of (C4) is therefore the sign of

\[
 \mathcal B=[32+256(1-c-2a)^2](p_0+a d_0)
            -32(1-c-2a)d_0.                             \tag{C5}
\]

A positive exponential series through degree 80, with its geometric tail
bound, proves `1900<exp(38/5)<2000`. Thus
`1/2000<epsilon<1/1900`. Formula (C5) is affine in `epsilon`, so evaluation
at these rational endpoints gives the exact enclosure

\[
 \mathcal B\in\left[
 -\frac{1170389439}{3027343750},
 -\frac{2218586678}{5751953125}\right]
 \subset(-\infty,-3/8).                                 \tag{C6}
\]

All omitted factors in the second derivative are strictly positive.
Consequently the **entire outside-word-summed Gaussian density** in (B2)
has strictly negative `a` curvature at this point. Continuity makes the sign
negative on an open neighborhood in `C^2`; this is not an isolated
measure-zero-vector artifact.

This disproves the proposed pointwise-convex Gaussian-density extension for
general equal-leverage rank-two swaps. It does not exclude other positive
representations or a proof retaining cancellation across Gaussian vectors.

### The actual integrals and full entropy do not have that negative sign

The exact certificate also checks the complete 34-site law. At (C3),

\[
 I_{1/2}''(a)\in[464.200658347954,464.200658347955],
\]
\[
 H_{1/2}''-H_0''\in[228.711913173143,228.711913173144].     \tag{C7}
\]

Both complete entropy Hessians are negative; their enclosures are in
[the 34-site receipt restoration note](certificates/GAUSSIAN_RECEIPT.md). Thus (C6) is a failure of
a **pointwise sufficient condition**, while the integral and the actual
curvature comparison in this fixture are positive. It supplies no negative
C1, projection-entropy, or sine-rate witness.

## 4. Certificate arithmetic and complete-atom accounting

For each fixture the rank-two atom polynomial is differentiated exactly.
Writing `q=B F`, `B=a^alpha(1-a)^beta`, `F=x^2+cxh+c^2m`, the checker uses

\[
 A=\alpha/a-\beta/(1-a),\quad
 A'=-\alpha/a^2-\beta/(1-a)^2,
\]
\[
 q'=B(F'+AF),\qquad q''=B(F''+2AF'+(A^2+A')F).
\]

The complete Hessian is always
`-sum q'' log q - sum (q')^2/q`. For (C7), with `v=q_1-q_0`, the additional
rational identity is

\[
 \left(\frac{v^2}{q}\right)''
 =\frac{2(v'-v q'/q)^2}{q}+\frac{2vv''}{q}
                         -\frac{v^2q''}{q^2}.           \tag{D1}
\]

There are 256 classes `(first three bits, clone count)` for (C1). Each stored
jet is the probability and derivatives of **one full output atom** in its
class; its multiplicity is `binom(31,k)`. The entropy sum uses that
multiplicity outside `p log p`, not a logarithm of the class mass. This
lossless encoding covers all `2^34` atoms at each of `s=0,1/2,1`.

All 256 representative inclusion moments of the middle law are independently
reconstructed from the atom sums and checked at derivative orders zero, one,
and two: 768 exact identities. Clone permutation symmetry then covers every
inclusion set, not just sets of small size. The input projection condition is
checked by the exact weighted Gram identity, independently of normalization.

Logarithms are range reduced to `[1,2]`, and their atanh series is evaluated
with outward 192-bit dyadic rational arithmetic for 64 terms. The remainder
is bounded using `z<17/50`. Signed range-reduction corrections and signed
acceleration coefficients are interval-propagated. The exponential enclosure
uses the positive Taylor series and a geometric bound on the tail ratio.
All displayed decimal endpoints are outward-rounded rationals of denominator
`10^12`; no floating value certifies a sign.

## 5. Failure ledger and surviving scope

| Proposal | Disposition | What survives |
|---|---|---|
| Monotone real coordinate leverage balancing implies convex complete-entropy gain | Disproved by (A1)--(A4), with genuine full-support projection endpoints | The specially constructed affine quadrature chord is different and remains valid |
| The rank-two Gaussian Fisher density, after summing all outside words, is pointwise convex in `a` | Disproved by the connected 34-site example (C1)--(C6) | Integrated signed comparisons such as (B4) remain open; this fixture has positive actual integrals |
| Every coefficient in (B4) may be treated as nonnegative | Algebraically false for more than two nonzero zero-sum entries | Four-cycle support has one positive coefficient and yields the proved theorem |
| Generic homogeneous transposition smoothing | Already disproved in reviewed S2; not retried as a theorem | Actual isometric minor constraints are kept here |
| Universal latent completion (C) | Already disproved in reviewed S3; not used | No completion assumption enters the Gaussian proof |
| Another transfer bridge, old Johnson identity, or finite no-hit search closes sine concavity | Not a valid new sign argument | Existing bridges can be used only after a suitable new finite sign estimate |

Bounded floating searches were used only to locate candidate deformations and
test formulas. Their no-hit results are not theorem evidence. A large-clone
floating diagnostic underflowed and stopped at dimension 66; it was not counted
as a pass. The exact 34-site grouped certificate replaces floating evidence
for every displayed obstruction sign. No unbounded search or sleeping was used.
