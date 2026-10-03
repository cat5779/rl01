# R10 G9 recovered-result audit

Date: 2026-10-03 (Asia/Singapore)

Audited source: the complete 17-page searchable manuscript
`dpp10_g9_main_proof.pdf`, SHA-256
`a037e9c07dd1630f1c19ab0c1846f7d2655b3afef9f623498071dc1dbc823100`.

## Verdict

`PASS / CORRECT_SCOPED`, with the original unrestricted invariant target still
open.

Under assumptions (A1)--(A3), the manuscript correctly proves:

1. existence of an ordinary weak pure-birth solution with the prescribed
   one-time DPP marginals and cylinder martingale problem;
2. compactness and convexity of the solution set and existence of an invariant
   weak solution for every countable amenable group;
3. the stated conditional strong-extraction theorem, assuming a causal joint
   product-Poisson weak solution and the displayed invariant-coupling
   Lipschitz condition (AL).

It does **not** prove invariant weak existence for arbitrary countable
nonamenable groups.  There the exact remaining step is a fixed-point problem
for the compact convex set of weak solutions.  It also does not derive the
causal product-Poisson representation or (AL) from the selected DPP rates.

## Checks performed

1. The finite projections use the correct conditional rates and the exact-set
   positivity supplied by the uniform spectral gap.  Their forward equations
   reproduce the required finite marginals.
2. Compactness of coordinatewise pure-birth path laws is legitimate because
   each coordinate has at most one jump.  The mean-activity hypothesis gives
   the uniform small-time control needed at `t=0`.
3. The drift limit uses `L1` martingale convergence of the conditional rates,
   followed by interpolation on fixed finite coordinate layers.  This is
   enough for the cylinder martingale identities; it does not assume a
   cross-approximation same-noise estimate.
4. The product martingale calculation rules out simultaneous coordinate jumps
   rather than assuming this path property.
5. The solution set is nonempty, compact, convex, and stable under the group
   action.  Folner averaging therefore gives an invariant solution in the
   amenable case.  No fixed-point theorem is claimed for nonamenable groups.
6. In the conditional interface, causal disintegration over the whole driving
   noise preserves the compensation property for two conditional copies.
   Applying (AL) and Gronwall gives pathwise uniqueness, hence a Dirac
   conditional law.  Countability then permits one common conull set, and the
   exceptional inputs can be filled by a constant path to obtain a total
   all-input equivariant Borel map.

## Boundary

This is an internal mathematical audit, not a formal proof, field referee
report, or novelty certification.  The complete proof is the PDF itself; the
older ZIP is preserved only as an earlier-stage source packet.
