# Gap and scope audit

## Status

`DISPROVED_ROUTE_LEMMA`

The sine target remains open.  This package proves two route obstructions and
nothing stronger.

## Quantifier audit

### Theorem A

- Dimension: every finite `n`.
- Matrix: every Hermitian contraction insofar as the declared split-tail
  certificate is intended to be uniform in `Q`.
- Contrast steps: every `37/40<=d<c<=463/500`.
- Gap: every legal `0<delta<=3/80`.
- Cutoff: every integer satisfying the checkpoint tail threshold.
- Geometry: every legal outer interval and inner strip; the proof grants the
  method strictly better geometry than any nontrivial target strip.
- Adaptation: parameters may be reoptimized independently at every step.
- Conclusion: a lower bound on the payment of that precise certificate family,
  not on the true entropy response.

### Theorem B

- Witness: the exact finite contraction `n=2, Q=diag(1,0)`.
- Contrast steps: every `37/40<=d<c<=463/500`.
- Shift: every legal target shift, not just sampled centers.
- Gap: every common spectral gap legal at that shift.
- Certificate family: exact one-sided, nonnegative, mode-by-mode payments uniform
  over all contractions and shifts in the claimed target set, with no signed
  cancellation between modes and no `Q`-specific excess-margin coupling.
- Conclusion: this family cannot reach width `10^-3` from the reviewed uniform
  margin.

The witness is sufficient because any claimed uniform mode-two payment must
cover its actual positive response.  In fact `q2<=tau`, `d2<=tau`, and
`tau<=1/2` show that this half-density diagonal projection saturates the exact
mode-two maximum after complement reduction.

## Exact versus diagnostic

### Proved analytically

- the best-case geometry and adaptive margin accounting;
- monotonicity of the split-tail threshold factor;
- the 100-bin covering logic;
- exact first- and second-mode curvature identities;
- mode-two obstruction on every legal shift;
- favorable complete-entropy response of the same witness;
- the exact size of the cancellation estimate still required.

### Exact certificate

- all 100 gap bins and cutoff floors;
- the global split-tail coefficient minimum;
- strong-margin and sign-only width ceilings;
- mode-two whole-shift and centered coefficient floors;
- the exact product-witness entropy response;
- independent reconstruction from frozen JSON.

### Floating diagnostics only

- numerical minimization of the full rejected response formula;
- random complex-matrix finite differences of the low-mode identities.

Neither diagnostic is used in a theorem comparison.

## Imported/unreviewed separation

The base `-1/50` theorem, moving-law Chebyshev expansion, nested Bernstein
estimate, S6 rectangle, and value bridge are reviewed packet inputs.

The prior differentiated tail lemma is retained as unreviewed.  Theorem A says:
*even granting that formula, its complete adaptive certificate family remains
microscopic.*  Theorem B and the low-mode algebra do not depend on the old tail
lemma.

## Potential objections checked

1. **Could many tiny steps help?**  No within either family: each legal step has
   a lower bound linear in its own contrast width, so sums telescope to total
   width even under fresh optimization.
2. **Could a narrower or off-center strip help?**  Family A already grants
   `sigma=1`, better than any nonempty inner strip.  Family B's lower bound holds
   at every legal shift.
3. **Could a different cutoff help?**  Family A covers every threshold-admissible
   integer cutoff.  Family B is cutoff-free.
4. **Could complement symmetry help?**  It cannot enlarge the total legal shift
   length beyond `1-c`; Theorem B is pointwise and symmetric bookkeeping does
   not remove its actual positive mode-two response.
5. **Does the two-site witness disprove the target?**  No.  Its complete entropy
   response is favorable; only noncancelling coefficientwise accounting fails.
6. **Does this rule out all continuation methods?**  No.  Signed mode blocks,
   direct entropy-response estimates, and `Q`-dependent excess-margin coupling
   remain open.  On the exact witness the base curvature is
   `-243875000/8800857`, far stronger than `-1/50`, so such coupling is a real
   logical escape rather than a formal caveat.

## Exact remaining target-level gap

For a direct width-`10^-3` continuation ending with margin `1/200`, the total
allowed response is `3/200`.  Any successful argument in this lane must replace
the current bookkeeping by a signed estimate averaging at most `15` per unit
contrast.  Relative to the exact mode-two floor, it must certify at least

```text
3466045185/47458321 ~= 73.0334557137
```

units of cancellation per unit contrast, uniformly over the desired class, or
show that the same contraction has at least that much excess negative base
curvature available to pay the response.

No such estimate is proved here.  Therefore `c=0.926` and the full high-contrast
sine target remain unresolved.
