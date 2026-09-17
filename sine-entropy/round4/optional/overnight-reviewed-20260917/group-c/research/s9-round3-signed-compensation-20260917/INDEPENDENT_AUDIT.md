# Independent audit — S9 / PR113

## Verdict

**ACCEPTED_SCOPED / PARTIAL_OVERALL.** The critical-scale compensation and
finite full-law score units are accepted at frozen head
`f60563fbe6cfa8fbc6778733282931b6774bad2c` against baseline
`aaf3e86576a867067701089805c9e5e5a83e44f5`. The subleading complete sign and
the sine entropy-rate concavity target remain open.

## Accepted statements and exact scope

1. At `rho=1/2`, fixed `0<c<1`, center shift `a_*=(1-c)/2`, odd
   `R -> infinity`, aligned Fejer degree/conditioning radius `R`, and uniformly
   for `theta` in a fixed compact set, Theorem 1's production-weighted complete
   law converges in bounded-Lipschitz distance to the stated Gaussian mixture
   with density `int I_0(u) gamma_(v(u))(x-2u theta) du/u`. The local predictor
   replacement, every-word conditional count estimate, Fejer defect, changing
   kernel/shift, and small-noise tail are all paid.
2. Theorem 2's symmetrized signed limit and martingale translation coupling are
   accepted. For every fixed `theta != 0` and `b>0`, the centered interval has
   strictly negative limiting mass and its complement has exactly the opposite
   positive mass. The stated quadratic cost belongs to the constructed
   coupling; no optimal-transport claim is inferred.
3. Theorem 3's derivative passage is accepted. The complete-event determinant
   bound supplies a locally bounded holomorphic family, so Cauchy's formula,
   rather than differentiation of a real CLT error, yields
   `A_(R,F)''(0)/R -> int F d eta_c`. For the band `|M_R-R|<=b sqrt(R)` and its
   complement the accepted curvatures are `-R C_b(c)+o(R)` and
   `+R C_b(c)+o(R)`. At `c=19/20`, `b=1/2`, the exact lower bound
   `C_b(c)>1/140` is accepted. The full leading order cancels, so only
   `A_(R,1)''(0)=o(R)` follows.
4. `SCORE_COMPENSATION.md` Theorems A and B are accepted for every finite
   Hermitian contraction with trace `n/2` and every legal strict parameter in
   their statement. They concern the full labelled law: the score and atom
   acceleration estimates, fixed count-preserving spectral observation
   channel, and full-law KL comparison do not replace configuration entropy
   by count entropy.
5. The strict-interior fixed-density extension is accepted with its
   noise-adapted count center. It is uniform only on fixed compact shift scales
   at fixed `rho,c,a_0`; the band generally depends on `u`. The degree is at
   most `R`, with exact alignment on the stated unbounded subsequence.
6. The analytic layer-bistochastic obstruction and the exact four-site
   external-field obstruction are accepted in their explicitly limited scope.
   Neither is a DPP counterexample to the sine target.

## Partial and critical gaps

- **PARTIAL:** the positive and negative order-`R` production pieces cancel at
  leading order. No sign is proved for the complete subleading aggregate, no
  eventual radius is made explicit, and no fixed-chord entropy-rate sign or
  new all-shift contrast threshold follows.
- **CRITICAL GAP for the global target:** the reviewed value-transfer errors
  and the new weighted-CLT error are not `o(1/R)` at the critical chord. They
  cannot pay the order-`1/R` Jensen margin. A compatible signed subleading
  estimate or a fixed nonshrinking-chord argument is still required.
- Floating probes are retained as diagnostics only and carry no proof weight.

## Verification performed

`verify_exact_identities.py` was inspected for safety and rerun with Python
3.13.5, SymPy 1.14.0. All exact assertions passed: two 16-atom score cases,
first/second full-law jets, the fixed-channel identities, the exact external
field witness, `C_(1/2)(19/20)>1/140`, and the formula for `phi''`. The frozen
author receipt was restored after the replay; the replay changed only runtime
timestamps. The asymptotic conclusions were accepted from the analytic proof,
not from finite probes.

