# Gap audit

## Claim audit

### Theorem 1: exact defect size and curvature

- **Definitions paid:** actual `pi_l`, exact conditional kernel, actual `q_l`,
  mean-clock `qtilde_l`, Fourier potential, generator normalization, all clocks,
  and compact parameter domain are explicit.
- **Exact identity paid:** `Delta_n=V_n A_n` is finite-`n` and includes every
  count layer.
- **Growing estimate paid:** both factors have proved uniform asymptotics.
- **Moving derivatives paid:** the weak limit uses exact finite-`n` integration
  by parts; the midpoint theorem uses exact product differentiation and local
  count probabilities.
- **Limit order paid:** value limit, weak curvature, and pointwise
  `n^{-1/2}` boundary-layer limit are stated separately.
- **Scope:** even `n`, density `1/2`, fixed `0<c<1`, compact legal interiors.

### Theorem 2: positive correction

- **Normalization/positivity paid:** coefficientwise inequality gives
  `0<theta_l<1`, and forward irreducible BL heat is stochastic and positive.
- **Moment matching paid:** degree-two action is exact layer by layer.
- **Error budget paid:** explicit couplings give entropy-value bounds; these are
  not used as curvature bounds.
- **Negative class paid:** the no-go quantifies over every probability law on
  nonnegative BL time, even if it depends on `n,l,a`.
- **Scope boundary:** no statement about all positive transports.

## Unproved / unpaid steps

1. **No independent audit.**  All new claims are author proofs and checks.
2. **Target remains open.**  No sign is proved for the actual sine entropy-rate
   Jensen defect over the full high-contrast range.
3. **Corrected reference curvature is unpaid.**  A useful signed bound on
   `Dhat_F''`, or directly on its integrated Jensen response, is still needed.
4. **General density is unpaid.**  The exact half-density complement symmetry
   drives the midpoint cusp calculation.
5. **Endpoints are unpaid.**  Uniform asymptotics are only on compact legal
   interiors.
6. **No curvature inference from value couplings.**  The `O(log n)` and
   `O(sqrt n log n)` entropy differences are only values and fixed-chord
   budgets.
7. **Toeplitz transfer not invoked as a conclusion.**  The reviewed bridge may
   be used only after a target-level signed cyclic estimate is obtained.

## Coordinator's strongest next request

Ask for a signed, fixed-chord estimate for the **complete corrected
Fourier-reference divergence**

`J[Dhat_F]=(1-t)Dhat_F(a0)+tDhat_F(a1)-Dhat_F(a_t)`

on a declared high-contrast compact interior, with all
`pi_l`, `pi_l'`, `pi_l''`, conditional Fisher, and conditional acceleration
terms retained.  A meaningful next theorem would show that this term, together
with the explicit count and `-2n log n` contributions, has a strictly favorable
extensive margin plus `o(n)` error.  An independent audit should first verify
the exact multiplier formula, uniform saddle expansion, and midpoint local
limit in Theorem 1.
