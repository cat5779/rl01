# Route registry

## ROUTE-1: bounded testing witness

- Status: **PROVED SUBLEMMA**.
- Category: binary hypothesis testing.
- Key object: `Phi(T,x)=sum_{j in T}|P_xj|^2`, taking values in `[0,1/4]`.
- Result: `A_k >= c^4/72` for every `k>=2`, and
  `liminf A_k>=2c^4/9>0.1810`.
- Remaining bottleneck: this controls `A_k`, not `E_k`.

## ROUTE-2: central entropy-dissipation estimate

- Status: **PARTLY BLOCKED / REDIRECTED**.
- Category: reversible Dirichlet forms and association schemes.
- Proved reduction: the bridge is a Poisson number of exchanges with mean
  tending to `1/2`.
- Failed subroute: the left-endpoint dissipation bound would require
  `limsup J_k<4c^4/9`; finite exact values already rise above that threshold.
- Redirected target: control the full finite-exchange entropy cost or its local
  weak limit, retaining dissipation decay within the bridge.

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
