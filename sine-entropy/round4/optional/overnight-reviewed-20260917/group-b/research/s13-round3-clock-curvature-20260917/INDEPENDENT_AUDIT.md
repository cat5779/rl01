# S13 cumulative round 3 independent audit

## Verdict

**ACCEPTED_SCOPED / PARTIAL_OVERALL.** Theorem 3.1, the positive extensive midpoint clock-curvature component, is accepted. The full corrected-law response, the full entropy sign, and the sine entropy target remain unproved because the moving-count term `W_n` is unpaid.

## ACCEPTED

1. **Previously reviewed dependency.** The exact degree-two multiplier, `0<theta_{n,l}<1`, and the positive Bernoulli-Laplace clock matching the single Fourier pair-potential expectation are used under the exact scope of `outputs/overnight-20260917/check1/S13_GATE.md`. That gate is carried forward without a second review. It certifies one scalar degree-two expectation and does not certify equality of laws.
2. **Midpoint chain-rule decomposition.** At `a_*=(1-c)/2`, `z'(a_*)=0`, so the first-clock and cross terms vanish. The decomposition
   `Khat_n''(a_*) = W_n(c)+C_n(c)` retains the actual count weights and isolates
   `C_n=sum_l pi_l[-tauhat_l''] I_l` with the correct sign.
3. **Specialized central-overlap asymptotics.** Uniformly for `|l-n/2|<=n^(2/3)`, the ratio/Laplace argument gives the overlap mean, variance, and third-moment control needed for
   `theta_{n,l}(z_*) -> c^2` and
   `partial_z log theta_{n,l}(z_*) -> (1-c)^3/[2c(1+c)]`.
   Differentiating the finite-`n` correction is justified by the third centered moment bound. Combined with the exact `z''(a_*)`, this yields
   `-tauhat_l''(a_*)/n -> 2/(1-c^2)` uniformly on the central band.
4. **Nonzero averaged mode and extensive slice KL.** The proof correctly avoids the vanished Johnson degree-one component. The adjacent degree-two pair marginal survives translation averaging. Pairing disjoint cycle edges and applying entropy subadditivity gives
   `K_l/n >= J_pair(c)-o(1)` uniformly on the central band.
5. **Slice modified log-Sobolev normalization.** The induction proves
   `Ent_{u_l}(f) <= [2l(n-l)/(n+2)] I_l(f)` for the total-rate-one generator used in the proof. The edge multiplicities and the factor two between the ordered edge form and entropy production are consistent. Consequently `I_l >= D_pair(c)-o(1)` on the central band.
6. **Theorem 3.1.** Count tails are exponentially small by Hoeffding, and every discarded summand of `C_n` is nonnegative. Therefore, for each fixed `0<c<1` along even `n`,
   `liminf C_n(c)/n >= 2 D_pair(c)/(1-c^2) > 0`.
   At `c=19/20`, the stated lower bound `1.4045396549...` is consistent with the formula.

## PARTIAL

1. The accepted theorem is one favorable component of the corrected uniform-divergence response at the symmetric shift. It is not a sign theorem for the complete response.
2. The round-2 saddle, cusp/local-limit, and entropy-comparison assertions remain unreviewed and are not integrated as accepted results.
3. The old random-clock no-go remains only a conditional channel/operator-multiplier obstruction; it is not an averaged-law obstruction.

## CRITICAL GAPS

1. **Full corrected response blocked by `W_n`.** No sign or sharp bound is proved for
   `W_n=sum_l pi_l'' K_l(tauhat_l)`. It can in principle offset the accepted positive component. A center-layer sign is insufficient; the required obligation is the complete average of layer second differences in equation (8.1).
2. **Away from the midpoint.** The `(tauhat_l')^2 I_l'` term is unpaid.
3. These gaps prevent acceptance of a full corrected-divergence sign, an entropy-concavity conclusion, or the main Toeplitz sine target.

## Independent verification path

- Read the full round-3 proof and independently checked the saddle equation, variance scale, differentiated finite-`n` correction, clock-curvature constant, adjacent-pair entropy bound, modified log-Sobolev normalization, and count-tail passage.
- Reused the prior bounded theta/scope gate exactly as instructed, without repeating its review.
- Checked the cumulative archive manifest: all 40 declared files match.
- Re-ran `symbolic_checks.py` using the locally cached SymPy package; the generated JSON is exactly equal as parsed data to the frozen symbolic receipt.
- The package's full replay could not run in the designated Python because SciPy is absent. The blocked jobs are finite/floating diagnostics and are not premises of the analytic theorem. This environment limitation does not widen the accepted scope.

