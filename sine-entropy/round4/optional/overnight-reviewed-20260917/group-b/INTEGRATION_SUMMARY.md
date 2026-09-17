# Group B integration summary

## S4 — ACCEPTED_SCOPED

Integrate `research/s4-round4-information-payment-20260917/`.

- ACCEPTED: Theorems A and B for every finite Hermitian contraction and every legal interior channel parameter, with the exact completed-information and Gaussian-remainder bounds stated in the author proof.
- ACCEPTED: Theorem C for `r<=0.01` or `r>=0.99`, `c in [0.925,0.959]`, and `a in [(1-c)/4,3(1-c)/4]`, including `H''<=-(11/250)n` and the sine-rate Jensen gain `11/500`.
- PARTIAL: This is a central-offset, extreme-density region. It does not settle ordinary densities, the outer offset quarters, or all `c<1`.
- CRITICAL GAPS: none inside the accepted scoped statements; the global target remains open.
- Verification: archive safety/hash recorded; 42-file manifest passed; exact and moving-reference replays passed.

## S13 — ACCEPTED_SCOPED / PARTIAL_OVERALL

Integrate `research/s13-round3-clock-curvature-20260917/`.

- ACCEPTED: for fixed `0<c<1` along even `n`, the midpoint clock-curvature component satisfies
  `liminf C_n(c)/n >= 2 D_pair(c)/(1-c^2)>0`.
- ACCEPTED dependencies: only the previously reviewed theta algebra, strict `0<theta<1`, and one-potential positive-clock matching from `S13_GATE.md`.
- ACCEPTED new work: uniform central-overlap asymptotics, extensive adjacent-pair KL, slice modified log-Sobolev normalization, and actual count-tail averaging.
- PARTIAL: only one favorable component at the midpoint is paid.
- CRITICAL GAP: `W_n=sum pi_l''K_l` is unsigned and can offset the favorable component; away from the midpoint `(tau_l')^2 I_l'` is also unpaid. Do not claim a full corrected-response sign, entropy concavity, or the sine target.
- Verification: archive safety/hash recorded; 40-file cumulative manifest passed; independent symbolic replay matched the frozen JSON. Full diagnostic replay was blocked by absent SciPy and was not used as a proof premise.

## S5 — MISSING

No new S5 archive exists under the supplied directory. Do not integrate or relabel the older `S5_actual_channel_transport.zip` as a new result.

## Root-document wording constraints

- Keep `ACCEPTED_SCOPED`, `PARTIAL`, and `CRITICAL GAPS` separate.
- Preserve the exact parameter ranges and even-`n`/fixed-`c` quantifiers.
- Do not promote S13's component theorem to a sign for `Khat_n''`, `Dhat_F''`, `Hhat''`, or the original entropy target.
- Do not import S13 round-1, round-2, or exploration artifacts as reviewed results.

