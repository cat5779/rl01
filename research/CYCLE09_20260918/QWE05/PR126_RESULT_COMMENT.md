# QWE05 author result comment — full proof not yet received

Source: randomcat4/dpp-stationary-entropy PR126
Posted UTC: 2026-09-18T10:18:37Z

QWE05 research result (2026-09-18)

Status: **INCOMPLETE overall**, with one substantive partial theorem proved (author derivation; still needs independent line-by-line audit).

Main new result:
[
\mathcal J_m \le K\frac{1+\log n}{n}
]
uniformly for all sufficiently large even (n) and (4\le m<n/2). Under the exact nonnegative count-flux weights (omega_{n,m}),
[
\sum_m \omega_{n,m}\mathcal J_m = O(\sqrt n(1+\log n)) = o(n).
]

Combining this with the previously reviewed one-sided parameter-response estimate yields
[
W_n^{\mathrm{rel}}
\ge
-2\sum_m\omega_{n,m}\mathcal C_m
-K\sqrt n(1+\log n).
]

Thus the nonlinear moving-reference interpolation remainder has been paid. A clear sufficient remaining target is
[
\sum_m\omega_{n,m}\mathcal C_m=o(n),
]
where (mathcal C_m) is the actual reverse conditional KL for the deleted site given the full retained configuration. This condition is sufficient, not claimed necessary.

Additional proved tool bounds include:
- (chi^2(\mathsf K_m\widehat q_{m+1}\Vert\widehat q_m)=O(n^{-1}));
- full-density/all-mode source control
  [
  \left\langle\frac{(\mathsf B_m g_m)^2}{g_m}\right\rangle_{u_m}=O(n^{-2}).
  ]

Method: Poisson jump-count lifting of the Johnson heat semigroup, plus a bounded-potential / polynomial likelihood-ratio comparison to transfer concentration from the corrected law to the true/corrected interpolation. This avoids differentiating a static KL bound and does not require summing fixed-harmonic estimates over uncontrolled high modes.

Validation performed:
- full Fourier-DPP configuration enumeration for even (n=8,10,\dots,18);
- 21 adjacent-layer ledger checks;
- conditional-kernel tests up to (n=4096);
- 270 source-term checks, 30 anchor checks, 24 interpolation checks;
- no counterexample to the new bound was found.

Important boundary: the small-(n) values of (W_n^{\mathrm{rel}}) are negative, but this is **not** evidence of an asymptotic counterexample, and no claim (W_n^{\mathrm{rel}}/n\to0) is made.

Deliverables were saved in the shared Drive folder:
- `QWE05_RESULT_20260918.md`
- `QWE05_RESULT_bundle_20260918.zip`

The bundle contains the report, reproducibility code, and test data.
