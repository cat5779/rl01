# Cross-category encodings and seed routes

The frozen claim admits the following faithful or one-way encodings.

1. **Binary hypothesis testing — EQUIVALENT for `A_k`.**  Deletion loss is the
   KL divergence between the true deleted-point joint law and uniform refill.
   Native tools: Pinsker, variational KL, chi-square tests, Le Cam witnesses,
   strong data processing.
2. **Association-scheme harmonic analysis — EQUIVALENT.**  Exchange heat is
   diagonal on Johnson degrees; the two-point component has eigenvalue
   `-2(n-1)`.  Native tools: Eberlein polynomials, spherical transforms,
   hypercontractivity, log-Sobolev estimates, spectral projectors.
3. **Statistical mechanics — HEURISTIC for the full claim.**  `d_k` is a
   one-particle surface free-energy increment.  Native tools: DLR limits,
   equivalence of ensembles, cluster expansions, pressure differentiability,
   surface tension.
4. **Local asymptotic statistics — ONE-WAY.**  A limiting local score with
   nonzero testing power yields a positive `A_k` limit.  Native tools: LAN,
   contiguity, Hájek projections, Fisher information, score tests.
5. **Electrical/Dirichlet form representation — ONE-WAY for `E_k`.**  The
   clock cost is integrated entropy dissipation.  Native tools: Thomson
   principles, effective resistance, spectral profiles, Nash inequalities,
   carré du champ.
6. **Stein response — ONE-WAY for `W_n`.**  The `w_l`-weighted difference is a
   discrete response expectation.  Native tools: Stein kernels, exchangeable
   pairs, discrete integration by parts, Edgeworth expansion, zero-biasing.
7. **Optimal transport — ONE-WAY.**  Deleted-point predictability can be
   observed through a bounded transport witness.  Native tools: Kantorovich
   duality, transport-entropy inequalities, entropic transport, contraction.
8. **Toeplitz/saddle-point asymptotics — ONE-WAY for the limiting profile.**
   Principal Fourier minors and count weights become coefficient asymptotics.
   Native tools: strong Szego limits, Fisher--Hartwig analysis, saddle points,
   local central limits, analytic combinatorics.

Promoted first routes: binary hypothesis testing for `A_k`, and
Dirichlet/spectral entropy dissipation for `E_k`.

