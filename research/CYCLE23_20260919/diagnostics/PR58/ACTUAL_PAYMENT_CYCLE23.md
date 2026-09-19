# QWE09 actual-word reveal payment diagnostic — Cycle23

Date: 2026-09-19

## Status

`FLOATING ACTUAL-LAW DIAGNOSTIC / NOT A SIGN CERTIFICATE`.

This diagnostic supplies bounded evidence for a prospective S72 observation-payment
tool.  It is not a second QWE09 review, does not replace the exact six-site
counterexample, and does not prove entropy concavity or nonconcavity.

The main empirical conclusion is sharp enough to guide the next lemma:

* conditional zero-payment Jensen fails on actual positive-probability words, as
  QWE09 proved;
* after averaging with the complete actual coarse-word law, every tested
  single-reveal `E DeltaPhi` and `E DeltaChi` is positive;
* the global Hessian constant `Lambda ~= 1.234397e6` is enormously larger than
  the curvature seen along actual reveal increments.  The largest tested
  wordwise negative ratios are only `3.64464` for Phi and `1.76020` for Chi;
  actual-weighted negative-part ratios are at most `0.00331876` and `0.00701216`.

Thus the dominant loss in the present Lambda payment is evidence for irrelevant
matrix directions in the full convex domain, not chiefly rare words or the
physical observation distance.

## 1. Frozen variables and actual law

All models are genuine finite sine-Toeplitz DPPs at `rho=1/2`:

\[
 Q_{ij}=\frac{\sin(\pi(i-j)/2)}{\pi(i-j)},\qquad Q_{ii}=\frac12,
 \qquad K=aI+cQ.
\]

Here `p` in the diagnostic input is the legal channel-noise coordinate

\[
 p_{\rm noise}=\frac{a}{1-c}\in\{1/4,1/2,3/4\},
 \qquad a=(1-c)p_{\rm noise},
\]

not the output marginal.  The output marginal is
`mu=a+c/2`.  Contrasts are `c in {.95,.99}` and volumes are
`n in {6,8,10,12}`.

The revealed site is `r=n-1`, the coarse observed set is
`A={0,...,n-2}`, and two core/halo geometries are used:

* `balanced_pair`: `I={n/2-1,n/2}`;
* `balanced_triple`: `I={n/2-1,n/2,n/2+1}`.

In both cases every site of `A\I` is an actually observed halo site.  Increasing
n moves the reveal away from the core while retaining the full intervening
observations.

For every one of the `2^(n-1)` coarse words y, the program uses the actual atom

\[
 P_A(y)=(-1)^{|A|-|y|}\det\{K_A-\operatorname{diag}(1-y)\}.
\]

All atoms were positive.  Across the whole run the smallest was
`1.13288e-11`, total-mass error was at most `1.56e-15`, and the unconditional
reveal marginal reconstructed from conditional probabilities agreed with
`a+c/2` to `6.67e-16`.

## 2. Single-reveal formulas

Put

\[
 B_y=K_A-\operatorname{diag}(1-y),\quad G_y=B_y^{-1},\quad
 b=K_{A,r},\quad q=K_{rr}-b^*G_yb.
\]

The coarse core score is `M=(G_y)_II` and `v=(G_y b)_I`.  Schur inversion gives
the two actual fine scores

\[
 M_1=M+\frac{vv^*}{q},\qquad
 M_0=M-\frac{vv^*}{1-q},
\]

with actual conditional probabilities q and 1-q.  Hence

\[
 qM_1+(1-q)M_0=M
\]

and the single-reveal quadratic variation is exactly

\[
 \mathcal Q(y)
 =q\|M_1-M\|_{HS}^2+(1-q)\|M_0-M\|_{HS}^2
 =\frac{\|v\|^4}{q(1-q)}.
\]

For `Psi in {Phi,Chi}` the measured Taylor remainder is

\[
 \Delta\Psi(y)=q\Psi(M_1)+(1-q)\Psi(M_0)-\Psi(M).
\]

`Phi` and `Chi` are evaluated from QWE09's complete logarithmic pair potential,
with `Chi` retaining only opposite-parity pairs.  The largest numerical
martingale residual in the complete run was `2.85e-14`.

## 3. Independent recovery of the six-site word

For

\[
 n=6,\ c=.95,\ a=.025,\quad
 A=\{0,1,2,3,4\},\quad y=(0,0,0,1,1),\quad I=\{2,3\},\ r=5,
\]

the independent floating implementation gives

| quantity | independent value | QWE09 certified enclosure |
|---|---:|---:|
| `P_A(y)` | 0.014232864029787238 | [.014232864029787238,.014232864029787239] |
| q | 0.2919673526334219 | [.291967352633421847,.291967352633421848] |
| `DeltaPhi` | -0.10658530785914078 | [-.106585307859143407,-.106585307859143406] |
| `DeltaChi` | -0.09639546527182619 | [-.096395465271827624,-.096395465271827623] |
| Q | 0.17030961979131762 | [.170309619791317635,.170309619791317636] |

The small floating displacement is consistent with double precision, and every
value lies within `5e-15` of the strict dyadic interval.  The original
`QWE09_checks.py --certificate` was also rerun and reproduced the exact
intervals.  This preserves the counterexample's scope: it refutes wordwise
zero-payment Jensen, not unconditional average monotonicity.

## 4. Actual-weighted results

There are 48 `(n,c,p_noise,geometry)` records and 16,320 distinct coarse words
before the two geometry evaluations.  For every record,

\[
 E\Delta\Phi>0,\qquad E\Delta\Chi>0.
\]

The signed ratios satisfy

\[
 0.7770679\le\frac{E\Delta\Phi}{E\mathcal Q}\le0.9559112,
\]

\[
 0.0940343\le\frac{E\Delta\Chi}{E\mathcal Q}\le0.1870236.
\]

The negative part is much smaller:

| potential | largest `E(-DeltaPsi)_+ / E Q` | largest wordwise `(-DeltaPsi)_+/Q` |
|---|---:|---:|
| Phi | 0.00331875237 | 3.64463733 |
| Chi | 0.00701215368 | 1.76019146 |

The wordwise maxima occur at n=12,c=.99.  Their actual probabilities are
`1.43e-5` for Phi and `1.10e-6` for Chi.  They are real words, not fabricated
matrices, but they do not control the actual-weighted payment.

The negative sign itself is not purely rare:

* Phi-negative words carry between 2.6% and 23.5% of actual mass;
* Chi-negative words carry roughly 64%--72% of actual mass.

Nevertheless the rarest 1% of actual probability mass carries at most 6.9% of
the Phi negative expectation and 4.5% of the Chi negative expectation; the
rarest 5% carries at most 23.8% and 11.9%, respectively.  Thus rare words amplify
the worst conditional ratio, but do not explain the average sign.

Observation distance mainly reduces the scale of both `E Q` and `E DeltaPsi`.
Averaging descriptively over the tested parameters and applicable geometries:

| nearest reveal distance | mean `E Q` | mean `E DeltaPhi` | mean `E DeltaChi` |
|---:|---:|---:|---:|
| 1 | 12.7845 | 10.7876 | 2.02449 |
| 2 | 5.40206 | 4.87452 | 0.80905 |
| 3 | 4.10868 | 3.76869 | 0.72262 |
| 4 | 2.93245 | 2.72766 | 0.48839 |
| 5 | 1.73112 | 1.63882 | 0.29815 |

The ratios remain of the same order.  Distance is already substantially encoded
by the quadratic variation; it is not the source of the six-order global
Hessian constant.

## 5. Candidate weighted inequalities

The following are candidates for proof, not conclusions from floating data.

### Candidate A: actual-weighted negative-part payment

For one actual reveal and a fixed core/halo geometry,

\[
 E_A[(-\Delta\Phi)_+]\le\lambda_\Phi E_A\mathcal Q,
 \qquad
 E_A[(-\Delta\Chi)_+]\le\lambda_\Chi E_A\mathcal Q.
\]

Any constants covering the tested family must satisfy at least

\[
 \lambda_\Phi\ge0.003318752368588861,
 \qquad
 \lambda_\Chi\ge0.0070121536779326355.
\]

Natural first certification targets are `lambda_Phi=1/300` and
`lambda_Chi=1/140`.  They are only slightly above the observed minima and are
still about eight orders of magnitude below QWE09's global Lambda.

### Candidate B: signed actual reveal gain

The data support the stronger signed inequalities

\[
 E_A\Delta\Phi\ge\eta_\Phi E_A\mathcal Q,
 \qquad
 E_A\Delta\Chi\ge\eta_\Chi E_A\mathcal Q.
\]

The largest constants not already contradicted by this tested family are the
observed minima `0.7770679253` and `0.0940343041`.  Conservative first targets
would be `eta_Phi=3/4` and `eta_Chi=9/100`.  Even proving the zero versions would
remove the observation payment after actual-word averaging while remaining
fully compatible with the certified six-point negative word.

A wordwise replacement is less attractive: the tested family already forces
coefficients at least `3.64464` and `1.76020`.  Those are still tiny compared
with the global Lambda, which is evidence that the convex-domain Hessian proof
pays for irrelevant matrix directions, but actual averaging offers a much
larger gain.

## 6. Scope and next rigorous step

No random matrix, clipped word, or frozen artificial weight enters the data.
Every displayed average uses the normalized actual coarse-word law, and every
fine pair is weighted by its actual conditional q and 1-q.

The computations stop at n=12 and at two declared geometries.  They do not
certify a continuum in c or p, all cores, multiple reveal orderings, or an
entropy-rate sign.  There is no finite-volume entropy nonconcavity evidence.

The most economical rigorous next step is to interval-certify Candidate A on a
minimal parameter cell and one reveal geometry, retaining actual word weights.
If that succeeds, a martingale reveal sum can replace the global-Lambda Taylor
payment.  If it fails, the stored worst actual word supplies a concrete target
for a minimal dyadic interval counterexample without leaving the sine model.

