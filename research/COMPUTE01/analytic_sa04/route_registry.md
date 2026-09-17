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

- Status: **ACTIVE SCOUT**.
- Category: Toeplitz/local-limit statistical mechanics.
- Target: identify limits of `A_k`, `E_k`, and `d_k` directly.
- New paired diagnostics: `d_k=0.7588+/-0.0112` at `n=40`,
  `0.6779+/-0.0141` at `n=60`, and `0.5714+/-0.0161` at `n=80`.
  The corresponding `sqrt(n)d_k` values are `4.80,5.25,5.11`.  They support a
  positive inverse-root central profile, not a dimension-free positive limit,
  even though `E_k` has already outgrown the conservative analytic lower bound
  for `A_k`.
- Risk: proving existence of the entropy increment may be as hard as the
  original sharp-scale problem.

## ROUTE-4: weighted response without pointwise positivity

- Status: **REDIRECTED TO INVERSE-ROOT REGULARITY**.
- Category: Stein summation and saddle-point analysis.
- Target: prove `|A_l-E_l|<=K/sqrt(n)` on the expanded central window and
  combine it with the existing tail estimate to obtain `W_n=O(n)`.
- The former target of a negative `n^(3/2)` limit relied on a constant-size
  central cusp and is now numerically disfavored.  The eventual sign of `W_n`
  remains open even if the `O(n)` bound closes.
- Dependency: requires a window estimate, not only the single central layer.
