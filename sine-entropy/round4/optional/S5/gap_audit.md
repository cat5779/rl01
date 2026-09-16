# Gap audit

## Scope of the status

The package status is **PROVED_SCOPED_LEMMA**, not a claim about the sine entropy-rate target. The proof text is complete for the statements explicitly labelled complete proof; the two finite seeds have exact, reproducible certificates. The authoring agent checked its own derivations and ran its own programs. No separate reviewer or external certification has yet been supplied.

## Claims that are proved

| Claim | Quantifiers / dependencies | What is new relative to the prompt |
|---|---|---|
| Actual slice continuity velocity, covariant acceleration, full weighted entropy identity | Every positive full path, including all homogeneous inputs and the true nonprojection Toeplitz DPP channel; actual count laws specified separately; legal interior; fixed normalized BL generator | An exact pathwise connecting formula with every weight, reference, score/Fisher, and acceleration term retained |
| Single-mode acceleration identity `acc=B+beta'J` | Every positive path `r=1+lambda f` in a fixed reversible eigenmode; `beta=lambda'/(gamma lambda)` | Pays the actual time-change acceleration rather than importing a geodesic/heat conclusion |
| `acc>=B>=kappa E` for rank-one/co-rank-one projections | Every dimension, every choice of projection weights, every `0<c<1`, every legal interior layer | An unpaid geometric correction on a class genuinely closed under conditioning; not a new full-entropy concavity theorem |
| Same acceleration sign for uniform-marginal rank-two laws | All such homogeneous pair laws; includes rank-two Fourier projections | An additional scoped correction, used in the exact counterexample; no claim of minor closure |
| No single BL clock when degrees 2 and 4 both have nonzero input moments | Middle slice, `n=2k`, `k>=4`, any `0<c<1`, no nonempty open interval | An analytic obstruction allowing reversing clocks, not just the midpoint reversal |
| True-Fourier growth lift | `P_(8m,4m)` for every positive odd `m`, fixed density 1/2, every fixed `0<c<1` | The no-clock obstruction persists on a genuine increasing-dimensional Fourier subsequence, not merely unrelated homogeneous laws |

All stated constants and parameter values are given in `proof.md`. The count decomposition and concavity of `Phi` are supplied baselines, not counted as progress.

## Exact finite evidence and what it does not say

`evidence/fourier6_certificate.json` proves that for the genuine projection `P_(6,2)`, `c=1/2`, `a=49/100`, the aggregate non-Bochner remainder lies strictly between `-184/1000` and `-183/1000`. Every nonconstant conditional layer has favorable acceleration, and `H''<-37`.

This disproves the universal sufficient lemma `R_tr>=0`. It is **not** a target counterexample and is **not** a high-contrast counterexample. In particular it does not contradict the supplied finite concavity result for `c<=37/40`.

`evidence/clock_certificate.json` proves exact Fourier8 harmonic moments, kernel identities, and a nonzero rational clock mismatch at `c=19/20`, `a=1/100`. Its growing true-Fourier extension is an analytic proof using a principal-marginal identity and centered DPP moments. This rules out a fixed BL heat-clock representation, not all velocity fields, all metrics, all generators, or a transport proof retaining acceleration.

The second arithmetic implementation checks the exported nine-log remainder using an alternating logarithm series and powers of `3/2`, rather than the generator's atanh series and powers of `2`. It is an internal arithmetic cross-check, not external review. Neither interval overlap with zero nor small floating residuals are used as a proof of an exact equality.

## Endpoint and degeneracy limitations

The formulas are differentiated only in the legal interior, where all output atoms and count weights are positive, even for deterministic input. Conditional kernels and entropy values have justified endpoint limits, including layers whose weights vanish. A limiting conditional distribution on a zero-weight layer is an interior-path convention.

No finite endpoint value is asserted for an individual Fisher, Bochner, acceleration, or full-Hessian summand. Integrated convexity of the proved single-mode layer entropies extends to the closed interval by continuity. Full-entropy endpoint concavity would require an interior full-entropy result first.

## Projection-minor compatibility

The primary acceleration family includes all rank-one/co-rank-one, zero, and identity projections. Its occupied and unoccupied children are the actual projections from the prompt's formulas; closure is proved explicitly in Section 5.3.

The ancillary uniform-marginal rank-two class is **not** asserted to be closed under conditioning. The true-Fourier growth lift uses a principal marginal to compute moments; it does **not** call that marginal a projection or identify it with a conditional projection minor. The no-clock obstruction is not claimed at every node of a latent conditioning tree.

## Unresolved estimates blocking the target

For rank proportional to dimension we do not have a uniform lower bound for the aggregate remainder strong enough to prove `H''<=0`, or a finite Jensen bound with sublinear loss. Even nonnegative acceleration in every slice would not by itself pay the changing layer weights.

The displayed condition `R_tr>=Phi''-Bcal` is exactly the original finite curvature problem rewritten; it is not a theorem or new conjectural reduction. The more restrictive claim `R_tr>=0` is false in its universal form. A version confined to `37/40<c<1` remains unproved and undisproved here; finite scans are not evidence sufficient for such a conclusion.

The selected harmonic amplitudes in the growing no-clock family decay as `m^-2` and `m^-4`. We do not prove a uniform entropy cost for the exact mismatch, so an approximate heat-clock argument with quantitatively paid errors is not excluded.

No finite concavity result for the growing cyclic Fourier family, no uniform endpoint neighborhood, and no fixed-interior thermodynamic Jensen estimate is obtained. Consequently the supplied cyclic-to-Toeplitz and entropy value-tail bounds cannot yet transfer a new sign result. We do not differentiate the entropy-rate limit or the supplied value-error estimates.

## Respect for the supplied failures

Nothing in the proof assumes the false coordinate-completion inequality `(C)`, a favorable excess at every conditioning-tree node, universal conditional-layer entropy concavity, atomwise log-concavity, or universal concavity for arbitrary homogeneous input. The rank-one geometric theorem does not repair `(C)`. The Fourier6 counterexample deliberately retains layer derivatives rather than repeating their omission. The Fourier clock obstruction concerns a different, explicitly stated claim from the supplied failures.

## Floating computations and reproducibility limitations

Archived general edge-solve and large/lumped scans are floating diagnostics. They support algebra debugging and candidate selection only. Extremely small probabilities in the large lumped scan can underflow; spurious-looking extreme results are retained and not treated as certified. The small smoke comparisons have explicit residuals and reproducible inputs.

One early random rank-two candidate search was performed in-session without freezing its exact input sample stream. Its recorded search parameters are preserved in `attempts.md`, but it is not offered as reproducible evidence and no mathematical claim depends on it. A separate, fully specified random rank-three smoke case is archived and reproducible. This is an explicit provenance limitation, not a silently reconstructed original run.

## Conjectures

No conjecture is being promoted to a proved conclusion. Universal high-rank acceleration positivity and high-contrast-only aggregate positivity were exploratory candidates, remain unresolved in this work, and are not assumed in any theorem or certificate.
