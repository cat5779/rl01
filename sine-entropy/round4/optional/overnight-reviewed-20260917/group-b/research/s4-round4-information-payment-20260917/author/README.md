# S4 round 4 — completed-information payment

**Status: PROVED_SCOPED_LEMMA.** This is a new author proof and self-reproduction package, not an independent certification and not a solution of the full sine target.

## Main new result

For every finite Hermitian-contraction DPP input and every legal interior common-offset channel, the complete input/output information curvature satisfies

    0 <= I(X;Y_a)'' <= kappa(a,c) Psi
       <= kappa(a,c) [D - F_marg].

Here D is the explicitly known complete channel Fisher budget; Psi is the actual-output average of the diagonal posterior variances weighted by individual input-dependent score coefficients. It is NOT the normalized-posterior common-offset tangent energy. The bound retains and pays the unnormalized acceleration. The exact definitions and every proof step are in `proof.md`, Theorem A.

For Gaussian observations Z_t=tX+B_t, stopped at deterministic T, the completed remainder R_T=I(X;Y_a)-I(Y_a;Z_[0,T]) has

    0 <= R_T'' <= kappa c^2/tau_min^2
                     min{ V(K), 0.5 sqrt(n V(K)) exp(-T/8) }.

For a rank-k projection, V(K)<=k(1-k/n); for true contiguous Fourier projections equality holds. For the true Q_n, V(Q_n)=n rho(1-rho). The entire posterior and output-law averages are retained. T_n=16 log n gives a vanishing unnormalized Jensen error for this remainder, not for the entire target.

A separate scalar-channel Fisher budget proves, for all dimensions,

    H(DPP(aI+cK))'' <= -(11/250)n

when 37/40<=c<=959/1000, a lies in [(1-c)/4,3(1-c)/4], and TrK/n<=1/100 or >=99/100. Applied directly to Q_n and integrated before taking the entropy-rate limit, this gives the strong Jensen coefficient 11/500 on the same region. In particular rho=1/100, c=19/20, a in [1/80,3/80] is newly covered beyond the last round's extremely dilute example. Density is fixed and rank grows with n; this is not a fixed-rank result.

The proof does not use the preceding author's delta^-5 MMSE theorem, projection-minor recursion, a branchwise completion sign, a product-entropy equality, or a theorem for arbitrary homogeneous laws.

## Reading order

Start with `DELTA_FROM_LAST_ROUND.md`, `proof.md`, and `gap_audit.md`. `candidate_ledger.md`, `attempts.md`, and the frozen notes retain the scouted and rejected paths. `work_log.md` distinguishes measured research and reproduction time from previous rounds. `sources/reading_record.md` records the precise public commit, mandatory reads, primary theorem hypotheses, and unused optional sources.

## Reproduce exact evidence

Python 3.10+ and the standard library suffice. From this extracted directory:

```sh
python scripts/verify_manifest.py
python scripts/replay.py --out-dir output/replay
```

The checker rebuilds 16 rational fixtures, 1,562 pair/extrinsic checks, and 6,248 exact compatible-posterior rebasings. A separate checker tests two moving-reference experiments at nonmidpoint offsets, including both posterior responses and the actual unconditional output Fisher term. Logarithms use rational series with proved tails. The scalar continuum inequality and the regional parameter arithmetic have exact rational certificates.

`replay.py` compares **parsed JSON**, deliberately tests LF/CRLF equivalence, and refuses to write inside `evidence/`. Its output directory is separate from frozen evidence. File hashes detect byte changes; a changed newline byte is a provenance difference, not a mathematical disagreement. Use the parsed-JSON replay for cross-platform mathematical comparison.

Optional binary64 Fourier/Toeplitz/Gaussian diagnostics require NumPy:

```sh
python -m pip install -r requirements-floating.txt
python scripts/replay.py --out-dir output/replay-with-floating --with-floating
```

These floating results are not exact-compared, and no theorem depends on them. NumPy sampling seeds are recorded; low-order BLAS/platform variations are permitted. The exact checks do not import NumPy.

## Package structure and assurance

- `proof.md`: complete analytical scoped proof with quantifiers, constants, limiting argument, and source matching.
- `evidence/exact_certificate.json`: frozen rational finite and constant certificates.
- `evidence/moving_reference_certificate.json`: exact independent-observation identity checks.
- `evidence/floating_diagnostics.json`: explicitly nonrigorous larger-instance and Gaussian sampling diagnostics.
- `scripts/`: standalone checkers, replay, and manifest verification.
- `evidence/reproduction/`: recorded self-reproduction receipts and logs.
- `manifest.json`: SHA-256 and size manifest of shipped files, excluding itself and runtime output/cache directories.
- `dependency_versions.json`: actual environment; exact and floating requirements are separated.

No external repository, hidden workspace, previous ZIP, live network access, or PR is needed to reproduce the package. Imported mathematical inputs are restated. The full ordinary-density/high-contrast/all-offset sine target remains open here.
