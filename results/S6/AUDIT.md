# Independent audit of S6 round 4

## Verdict

The frozen deliverable was audited as an anonymous proof, without granting the prior round-3 author claim. The only imported mathematical inputs granted were the explicit reviewed assumptions in the public packet.

**Result 1 — high-contrast full-configuration sign theorem: CORRECT.**

The proof establishes, for every finite Hermitian contraction `0 <= Q <= I`, every dimension `n`, every

`37/40 <= c <= 37/40 + 10^(-13)`, and every `|a-(1-c)/2| <= 1/200`, that

`H(DPP(aI+cQ))''/n <= -1/200`.

**CRITICAL_GAPS for Result 1: none found.**

**Result 2 — positive real-q correlated-reference remainder and signed finite Jensen defect: CORRECT.**

For the true Toeplitz law, disjoint consecutive true `R`-site marginal blocks, `R | n`, `a in [delta,1-c-delta]`, and `q in [1/2,3/2]`, the proof establishes

`0 <= E_(n,R)(q,a)/n <= (c/R) Tr b(Q_R) + 2880 Lambda_delta^2 |q-1|`,

including the continuous `q=1` value and the stated absolute bound for the signed finite Jensen defect.

**CRITICAL_GAPS for Result 2: none found.**

This audit makes no novelty or priority claim.

## Result 1 proof audit

The claimed statement is at `proof.md` lines 11–36, and its proof is at lines 130–480.

1. **Full-atom determinant representation (lines 141–181): correct.** Diagonal multilinearity gives the atom formula with the stated sign. The two Loewner comparisons force exactly `n-|S|` negative eigenvalues and `|S|` positive eigenvalues of `A_S`; hence every atom is positive on the spectral strip and `-log p_x(S) = -(1/2) Tr log A_S(x)^2`.

2. **Moving-expectation degree cancellation (lines 183–244): correct.** After Boolean reduction, a monomial `x^j product_(i in V) y_i` has `j+|V| <= D`. Its DPP expectation is `x^j det(xI+dQ)_V`, of degree at most `j+|V|`. Thus averaging the configuration-dependent Chebyshev polynomial does not introduce dimension-dependent degree. This directly addresses the moving-law risk in the public target.

3. **Chebyshev series (lines 201–244): correct.** The scalar logarithm identity follows from the two absolutely convergent expansions of `log(1+r exp(±i theta))`, with `r=(1-delta)/(1+delta)`. Functional calculus is valid because the spectrum stays in `[-1,1]`. The degree bound `2m` and norm envelope `r^m/m` follow as stated.

4. **Nested Bernstein estimate (lines 246–326): correct.** Under `x=x_0+(ell/2)cos(theta)`, direct differentiation yields the displayed formula for `P''`. Applying the trigonometric Bernstein inequality twice gives line 268. Splitting the Chebyshev series at `M`, bounding the partial sum by `epsilon + A V_M`, and summing the differentiated tail gives exactly line 315. The derivative tail is uniformly summable on the nested interval.

5. **Contrast coupling and complement reduction (lines 328–412): correct.** Complementing converts `Q` to `I-Q` when needed and preserves the centered strip and second derivative. In the common-uniform monotone coupling, mismatches occur only when the DPP input bit is one, with probability `(c-c0)(Q_*)_ii`. The mismatch vector determines either output from the other, so the entropy difference is bounded by the sum of binary entropies. Concavity of `b` and `Tr(Q_*)/n <= 1/2` give the uniform value perturbation used later.

6. **Imported margin and constants (lines 413–460): correct.** Public `KNOWN_RESULTS.md` lines 10–12 supply exactly `F_(c0)'' <= -1/50` for every finite Hermitian contraction at `c0=37/40`. The exact rational certificate verifies the geometry and response bound `R < 3/200`; therefore `F_c'' <= -1/50 + 3/200 = -1/200`. No unreviewed round-3 premise is used.

7. **Passage to the rate (lines 462–480): correct.** The finite-dimensional strong-concavity inequality is integrated before taking `n -> infinity`. The public value-tail convergence is sufficient; no derivative-limit interchange occurs.

The most useful scoped unit is the dimension-uniform sign theorem for arbitrary Hermitian contractions on a nonempty contrast band and an `a` interval of fixed width. The missing general goal remains substantial: the proof does not cover `37/40+10^(-13) < c < 1`, does not cover the rest of the legal `a` interval, and its response constants deteriorate as the spectral gap closes.

## Result 2 proof audit

The claimed statement is at `proof.md` lines 38–69, and its proof is at lines 482–785.

1. **Hamming Lipschitz information bound (lines 497–521): correct.** On the spectral strip, `L=K(I-K)^(-1)` has spectrum in `[delta/(1-delta),(1-delta)/delta]`. The one-site atom ratio is a Schur complement of a principal submatrix of `L`; the same spectral bounds apply, giving Lipschitz constant `Lambda_delta` for `±log p`.

2. **Strong-Rayleigh hypothesis (lines 523–536): correct.** The L-ensemble generating polynomial is multiaffine with nonnegative coefficients. If every `Im z_i>0`, the imaginary part of `v*(L^(-1)+Z)v` rules out a zero. Thus the actual nonhomogeneous DPP law is real stable and strong Rayleigh.

3. **External concentration theorem and MGF conversion (lines 538–586): correct.** Pemantle–Peres Theorem 3.2 applies to a general, not necessarily homogeneous, strong-Rayleigh law and a Hamming-1-Lipschitz function. It gives the stated two-sided tail with mean `mu=E|S|`; the immediately following remark permits denominator `48n`. Scaling, moment integration, symmetrization, and the factorial bound yield `log E exp(s(F-EF)) <= 960 n L_F^2 s^2`. All constants check.

4. **Positive remainder identity (lines 588–626): correct.** Substitution into the order-`1/q` Rényi divergence gives exactly `(log Z-B)/(q-1)=D_(1/q)(pi_q || w) >= 0`. Its limit at `q=1` is `D(p||w)`.

5. **Moving-reference derivatives (lines 628–672): correct.** The scores, accelerations, escort motion, and covariance terms are all present. The second derivative of `B` uses the moving density proportional to `p w^s` and contains both `kappa+s zeta` and the full variance of `sigma+s theta`.

6. **Open-real-q estimate (lines 674–729): correct.** Writing both exact sums as centered cumulant generating functions gives line 706. For `q in [1/2,3/2]`, the two MGF bounds contribute at most `960 n Lambda_delta^2 |q-1|(1+1/q)`, hence the advertised constant `2880`.

7. **Toeplitz block step and Jensen defect (lines 731–785): correct.** The product of true disjoint block marginals has cross entropy `(n/R)H_R`, so its KL divergence is `(n/R)H_R-H_n`. The reviewed value-tail bound gives the upper bound `(c/R)Tr b(Q_R)`. Since each normalized remainder value lies in `[0,U]`, its signed three-point Jensen combination lies in `[-U,U]`, proving line 773.

The useful scoped unit is a positive, noninteger-real-`q` remainder estimate that retains every within-block correlation and is uniform in multiples `n` of `R`. It does not prove the missing sign of the block entropy Jensen defect, and therefore does not extend the full sine entropy-rate concavity target beyond Result 1's narrow band.

## Primary-source checks

The external statements were checked against the primary arXiv versions.

- Pemantle–Peres, [arXiv:1108.0687v3](https://arxiv.org/pdf/1108.0687), Theorem 3.2: for a general strong-Rayleigh measure on the Boolean cube with `mu=EN` and a Hamming-1-Lipschitz function, `P(|f-Ef|>a) <= 5 exp(-a^2/(16(a+2mu)))`. The following remark states that, because `a,mu <= n`, the denominator may be replaced by `48n`. These are exactly the conditions and statement imported at proof lines 540–551.
- Queffélec–Zarouf, [arXiv:1903.10801v1](https://arxiv.org/pdf/1903.10801), Theorem 1.1: for a trigonometric polynomial of degree at most `D`, `||T'||_infinity <= D ||T||_infinity`. Applying it again to `T'` gives the `D^2` second-derivative bound used at proof lines 271–284.

The stripped public packet is not itself a Git checkout, so the textual commit label in proof lines 90–94 could not be resolved locally. Its actual `TARGET.md` and `KNOWN_RESULTS.md` contents were checked directly, and the imported mathematical assumptions match them exactly.

## Reproduction and tamper receipts

The requested runtime was CPython 3.12.14.

- A fresh replay from the supplied source passed: 22 manifest files verified; exact constant fields matched; finite exact algebra fields matched; the floating `q` grid was not used as proof. Receipt: `work/s96-latest/S6/audit/replay_fresh/replay_report.json`.
- The snapshot ZIP SHA-256 is `5a1374e828fec0522c4667897d4423cab271a38e584fda202e46cf331a1d14cd`, exactly matching `snapshot.json`. A separate extraction replay passed, and all 22 listed source files matched the archive extraction. Receipt: `work/s96-latest/S6/audit/snapshot_replay/replay_report.json`.
- Changing listed `proof.md` caused both size and SHA-256 failures, with verifier exit code 1.
- Adding an unlisted file was not rejected. Replacing `MANIFEST.sha256` by an invalid all-zero anchor was also not rejected; both verifier runs exited 0. Thus `verify_manifest.py` verifies listed content against `manifest.json`, but does not enforce closed-world file coverage or authenticate `manifest.json` against `MANIFEST.sha256`.
- This limitation does not affect this audit's frozen input because the independently recorded snapshot hash matches the available ZIP, that ZIP was separately extracted and replayed, and the source's listed files match the extraction. It should be fixed before treating the inner verifier alone as a tamper-evident distribution mechanism.

The exact certificates support constant arithmetic and finite algebra only. The universal conclusions rest on the analytical proof above, not on the computations.

## Fresh-review recommendation

A second fresh reviewer is warranted for Result 1 because it advances the actual target region and its load-bearing new step is subtle: Lemmas 2.2 and 3.2 turn a uniformly tiny entropy-value perturbation into a dimension-free curvature perturbation while the DPP reference law moves with `a`. The reviewer should independently rederive the total-degree cancellation, the Chebyshev coefficient envelope, the nested Bernstein tail constants, and the interval geometry. Result 2's highest-risk point for any additional review is the tail-to-MGF conversion and its use for `log w`, though this audit found it correct.

## Final integration scope gate

**STATUS: CORRECT; no wording corrections required.** The S6 sections in the staged `README.md`, `CLAIMS.md`, `STATIONARY_STATUS.md`, and `STATIONARY_REVIEW_GUIDE.md`, together with `research/s6-round4-reviewed-20260916/README.md`, accurately preserve the reviewed scope: the full high-contrast target remains OPEN; the contrast extension has width exactly `10^(-13)`; the sign theorem applies only on `|a-(1-c)/2|<=1/200`; the real-q error vanishes only with `R->infinity` and `q->1`; and the all-shift imported margin remains the reviewed `c<=37/40`, modulus `1/50` result. The staged source has the same 28-file relative set as the frozen source and every file is byte-for-byte identical. Distribution coverage is assigned to the repository-root manifest, while the packet README expressly points readers to the independent audit for the inner verifier limitation. The timing statement is correctly qualified as an author-invoked completed-nontrivial-result exception and a self-reported detailed duration. The second fresh sign audit records `STATUS: CORRECT` within its stated Sections 1–4 scope; it was treated as a supplied review result and was not re-audited here.
