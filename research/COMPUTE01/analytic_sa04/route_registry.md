# Route registry

## ROUTE-1: bounded testing witness

- Status: **PROVED SUBLEMMA**.
- Category: binary hypothesis testing.
- Key object: `Phi(T,x)=sum_{j in T}|P_xj|^2`, taking values in `[0,1/4]`.
- Result: `A_k >= c^4/72` for every `k>=2`, and
  `liminf A_k>=2c^4/9>0.1810`.
- Remaining bottleneck: this controls `A_k`, not `E_k`.

## ROUTE-2: central entropy-dissipation estimate

- Status: **PROMOTED / INCOMPLETE**.
- Category: reversible Dirichlet forms and association schemes.
- Target lemma: an explicit `limsup E_k<2c^4/9`, or a stronger bound that can
  be paired with R1.
- Fast falsification test: compute a certified or asymptotic lower estimate for
  `E_k`; if it exceeds the R1 constant, the witness must be strengthened.

## ROUTE-3: limiting central profile

- Status: **SCOUT**.
- Category: Toeplitz/local-limit statistical mechanics.
- Target: identify limits of `A_k`, `E_k`, and `d_k` directly.
- Risk: proving existence of the entropy increment may be as hard as the
  original sharp-scale problem.

## ROUTE-4: weighted response without pointwise positivity

- Status: **SCOUT**.
- Category: Stein summation and saddle-point analysis.
- Target: prove a negative `n^(3/2)` limit for `W_n` from a central profile.
- Dependency: requires more than the single-point central bound.
