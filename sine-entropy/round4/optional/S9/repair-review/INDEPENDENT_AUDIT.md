# S9 repaired growing-radius proof review

## Final verdict

**STATUS: CORRECT.** No critical mathematical gap was found in RESULT.md
Theorems A or B, RESULT.md §§5.1--5.4 or §6, or LAYER_MEASURE.md.

This review addresses correctness only. It makes no novelty claim and does not
rebuild the previously accepted finite `R=3` certificates. The general S-sine
entropy-rate concavity question remains **OPEN**: the negative Jensen result is
for a selected moving-weight count band, not the full signed sum.

## RESULT.md Theorem A (lines 193--479)

**CORRECT.** The proof preserves every quantifier: fixed `c=19/20`, fixed
shifts `1/200,1/40,9/200`, every odd `R>=160001`, exact Fejer degree and
conditioning radius `R`.

The complete conditional predictor obeys `|2q_R-1|<=u(c+2d)` for every
exterior word, hence `phi(q_R)<=M_Du^2`. The `2R`-coordinate DPP count has a
Poisson-binomial law, mean `R+2Ru delta`, and one-sided tails
`exp(-x^2/R)`. At the midpoint, convexity under refinement from one-neighbor to
full conditioning gives `I_R(u,0)>=16u^4 gamma_R^4`; its integral is
`4gamma_R^4[1-(R+1)^(-4)]`. At either endpoint the band is separated from the
mean by at least `Rud` once `u>=w_R/(Rd)`, yielding (13).

The sharper complete-word Schur formula is valid. Row energy is at most
`c^2/4`, while the signed exterior event matrix has inverse norm at most
`2/(1-uD)`. This gives (14a), and for `u<=1/2` the polynomial bound (14b).
Direct integration reproduces the three Gaussian moments (14d). Exact rational
checking gives

```text
endpoint band <= 782426604667123/147456000000000000
midpoint band  > 1/30 - 7/32000
Jensen band    <= -4100517395332877/147456000000000000 < -1/40.
```

Thus the selected-band negative contribution and `N_R^->1/40` follow. No
configuration enumeration, derivative of a tail estimate, or sign assumption
on the remaining layers is used.

## RESULT.md Theorem B (lines 510--558)

**CORRECT.** For bands with `w_R/sqrt(R)->infinity` and `w_R/R->0`, midpoint
mass outside the band and endpoint mass inside the band both vanish. The
reviewed value/integral convergence (16) then makes the band midpoint mass tend
to `D(0)`. The inequality `(-g_{R,k})_+<=A_{R,k}(0)` supplies the matching
upper bound, proving the negative-mass limit. The signed-mass identity gives
the positive-mass limit, and the integrated neighbor lower bound gives
`D(0)>=4(c/pi)^4>0`. This uses convergence of three nonnegative production
values, not the unresolved comparison between them.

## RESULT.md variants

- **§5.1, lines 560--574: CORRECT.** Half-density gauge/complement symmetry
  gives `g_{R,k}=g_{R,2R-k}`. Complement pooling preserves negative mass.
- **§5.2, lines 576--593: CORRECT.** The product term is zero at the midpoint
  and nonnegative at endpoints, so the same selected-band upper bound survives.
  Wider endpoint-band excess tends to zero. Only the claimed `liminf` follows,
  and the text does not overstate it as an exact negative-mass limit.
- **§5.3, lines 595--626: CORRECT.** A symmetric gap below `-1/40` on a
  half-chord `h_R=R^(-1/4)` forces a point with second derivative below
  `-sqrt(R)/20`; otherwise the integral second-difference formula gives the
  contradictory lower bound `-1/40`. This concerns the selected band only.
- **§5.4, lines 628--659: CORRECT.** The legality condition
  `0<d<1/2-c max(rho,1-rho)` is exact for both endpoints. The generalized
  conditional constant is `D=2c max(rho,1-rho)+2d<1`, and the neighbor limit is
  `c sin(pi rho)/pi`. Exact degree equals radius only on the correctly stated
  unbounded subsequence `sin(pi rho R)!=0`; all radii have degree at most `R`.
  Complement symmetry is claimed only at half density.
- **§6, lines 666--703: CORRECT.** With `L=(n-1)/2`, the circular exterior has
  `2L=n-1` coordinates and the same concentration calculation applies. The
  nearest-neighbor magnitude is at least `1/pi`, and the row energy is exactly
  `1/4`. If `n` is a multiple of four and `n>=320004`, then
  `L>=160001.5`, so the §4.6 bounds apply already at the first allowed size.
  The entropy limit is explicitly a reviewed S8 value-transfer import, not a
  finite-Hessian transfer.

## LAYER_MEASURE.md (lines 11--143)

**CORRECT.** Since `E xi_R=u delta` and `Var(M_R)<=R/2`,
`E|xi_R-u delta|<=1/sqrt(8R)`. The pointwise Lipschitz error is
`M_Du^2 Lip(F)/sqrt(8R)`. Its integral against `du/u` is

```text
M_D (1-N^(-2)) Lip(F) / (2 sqrt(8R)),
```

so the prefactor in (M2) is correct. The remaining term is bounded by
`||F||_infinity` times the imported absolute production-integral error and the
true-noise tail.

The midpoint limit is the atom `D_0 delta_0`; endpoint pushforwards have the
stated densities and no atom at zero. They are therefore mutually singular.
Theorem B plus escape control for negative mass justifies weak convergence of
both Jordan parts and convergence of their total variation norms. The text
correctly does not claim convergence in total variation distance.

## Jensen sign and circularity audit

Because `J_R=log2-sum_k A_{R,k}`, its midpoint Jensen gap is exactly
`sum_k g_{R,k}`. Theorem A signs only the selected band. Theorem B identifies
the limiting positive and negative masses separately but does not compare them.
There is therefore no circular inference from the desired entropy-rate
concavity and no claimed negative entropy-rate Jensen gap.

## Reproducibility

The independent bounded checker `check_growing_proofs.py` passed with the
bundled Python runtime. It uses exact rational arithmetic, rigorous Machin
intervals, positive exponential partial sums, direct Gaussian-moment formulas,
and the (M2) integral. It does not recreate the rejected author helper.

```text
PASS_INDEPENDENT_GROWING_PROOF_CHECKS
endpoint_upper=782426604667123/147456000000000000
band_margin=-4100517395332877/147456000000000000
```

RESULT.md lines 359--361 refer to the omitted author
`code/verify_constants.py`; VERIFICATION.md lines 61--67 discloses its absence.
That is a packet-evidence caveat, not a proof gap, because the relevant
inequalities are explicit and were independently checked here.

## Integration documentation gate

**STATUS: CORRECT.** The staged status pages and S9 wrappers preserve the audit
verdict and leave the full fixed-density high-contrast sine entropy-rate target
open. `GROWING_RESULT.md` is byte-identical to the frozen repaired proof. The
wrapper maps the historical `LAYER_MEASURE.md` references to the equations in
that intact file. `FULL_R3_PRODUCTION.md` now points its equation (17) reference
to `GROWING_RESULT.md` and accurately records that the corrupted original
upload was quarantined, its intact replacement passed the separate repair
review, and the finite `R=3` theorem does not depend on the growing obstruction.
