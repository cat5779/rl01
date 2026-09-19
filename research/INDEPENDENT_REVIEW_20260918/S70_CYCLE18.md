# S70 Cycle18 independent review

Date: 2026-09-19

## Verdict

`VERIFIED_SCOPED`.

The S70 source package proves, for the genuine finite sine-compression DPP at
`rho=1/3`, the following two finite-volume estimates:

1. for `c in [19/20,1907/2000]`, `p in [21/50,12/25]`,
   `a=(1-c)p`, and every `n>=22`,

   `d_a^2 H_n(a,c) <= -n/25 + 441`;

2. on the nested rectangle `c in [19/20,953/1000]` with the same p range,

   `d_a^2 H_n(a,c) <= -n/5 + 441`.

Consequently the corresponding fixed-c entropy-rate chord inequalities have
coefficients `1/50` and `1/10`.  The proof is for full configuration entropy of
the true sine compression.  It is not a cyclic, count-entropy, or kernel-spectral
calculation.

This verdict does **not** cover the full requested rectangle through `c=.96`,
does not cover other densities or p outside `[.42,.48]`, and does not close the
whole contrast interval `(37/40,1)`.  The supplied fixed witness is rigorously
obstructed at `(c,p)=(.96,.45)`.

## Mathematical audit

The load-bearing reductions were checked independently from the manuscript and
source rather than inferred from successful log messages.

* The latent Bernoulli channel gives the exact finite law
  `DPP(a I + c Q_n)` even though the finite compression `Q_n` is not a
  projection.  Projection identities are used only for the infinite Fourier
  projection before compression.
* The complete-data Fisher budget is
  `(1-rho)/(a(1-a)) + rho/((a+c)(1-a-c))`.  Data processing gives the required
  observed-score upper bound, and the coordinate conversion is correctly taken
  at fixed c: `d/da=(1-c)^(-1)d/dp`.
* The endpoint-only PSD allocation lemma is valid.  A pair coefficient needs to
  exclude only its two endpoint bits for the weighted mixed-score identity; it
  may depend on the other target bits.  Conditional Jensen is then applied to
  the entire random PSD block after conditioning on its full window.  In the
  actual four-target construction the diagonal entries are constant on the
  word and each row-i off-diagonal entry excludes bit i, so the displayed
  factored potential is legitimate.
* The posterior guard uses the infinite-projection positive-field tilt and the
  correct finite compression inverse.  It does not replace `Q_E` by a
  projection.  The interval inverse pays its computed row-sum error as a
  Loewner radius; the optional abort threshold is not used as the radius.
* The signed two-parameter channel transport is exact.  With
  `D^2=0`, `F^2=F`, `DF=0`, and `FD=D`, the full probability vector is
  transported by the tensor product of `I+sD+vF`.  It is correctly treated as
  a signed algebraic transport, not as a Markov kernel.  All probability and
  affine-witness derivatives enter the moving payment.
* The degree-eight remainder is a whole-vector l1 bound.  The exact rational
  closure pays `10^-6`, while the regenerated upper bound is below
  `3.476374e-8` on the broad rectangle.
* The boundary term is volume-uniform: 21 missing translates times the proved
  payment ceiling 21 gives 441.  The entropy-rate statement follows by taking
  limits of finite chord inequalities; no entropy-value error is
  differentiated.

I found no missing sign, endpoint-measurability, double-spending, or
finite-compression/projection substitution in these steps.

## Independent regeneration

The complete readable package was copied to an isolated working directory.  I
rebuilt all seven C++ programs from source using GCC 16.2, Boost 1.92,
`-O3 -frounding-math -ffp-contract=off -std=c++17`, and OpenMP only where the
source requests it.  Python checks used the standard-library `Fraction`
implementation.  Pre-existing binaries, probability caches, and success logs
were not acceptance premises.

Fresh results:

| obligation | independently regenerated result |
|---|---:|
| interval arithmetic self-test | 138,828 exact comparisons, all four rounding modes |
| arithmetic audit | 20,128 checks |
| finite exact identity tests | 345 checks |
| endpoint-only PSD/Jensen unit test | 3 parameter cases, 2 windows per case |
| n=22 reference probabilities | all 4,194,304 words; mass interval contains 1 |
| global continuum cap | 33,600/33,600 cells; 9,201,142 nodes |
| distance-1 guard | 10,752/10,752 cells; 214,133,692 nodes |
| distance-2 guard | 10,752/10,752 cells; 178,200,492 nodes |
| distance-3 guard | 10,752/10,752 cells; 130,386,592 nodes |
| payment | all 4,194,304 words; mass interval contains 1 |
| PSD corners | 16,384 exact rational matrices |

The regenerated norm ceilings are `(2418,461,15266)`.  The regenerated 45
coefficient rows agree line by line with the supplied integer enclosure file.
The exact broad closure has positive Bernstein floor at least
`3062919/10^12`; the nested closure has floor at least
`667751932/10^12`.  Complete-cover bookkeeping independently recovers the
source node counts shown above.

As an independent pointwise backstop, direct summation over all 4,194,304 words
gives payment excess

`[0.0402893383975284, 0.0402893383992349]`

at `(c,p)=(.9535,.42)` and

`[-3.27783439189249, -3.27783439189059]`

at `(c,p)=(.96,.45)`.  Exact rational coefficient transport separately encloses
the latter excess in

`[-3.28380402880326, -3.16111833035501]`.

## Scope of the advance and remaining obstacle

The new endpoint-only block allocation is a genuine methodological advance: it
keeps a four-target PSD quadratic intact through score-martingale conditioning,
and it certifies a nonzero contrast strip above `.95`.  The advance is therefore
stronger than a single-parameter numerical sign.

It is not yet a closing method for `(37/40,1)`.  Three distinct gaps remain:

1. the current theorem is local in density (`rho=1/3`) and in channel bias
   (`p in [.42,.48]`);
2. it does not itself bridge the whole contrast region between the universal
   `37/40` baseline and `.95`;
3. the present cap/witness loses by more than 3 already at `.96`, so finer
   subdivision or tighter arithmetic cannot repair it.  A replacement
   state-dependent cap/allocation/test, or an additional payable witness, is
   mathematically necessary.  Approaching `c=1` also introduces a singular
   Fisher scale of order `(1-c)^(-1)`, requiring a renormalized or adaptive
   construction rather than a fixed `.95` witness.

Thus S70 should be retained as a verified local theorem and reusable tool, with
the full high-contrast problem still marked `INCOMPLETE`.

