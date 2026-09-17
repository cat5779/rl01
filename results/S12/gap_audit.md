# Gap audit

## What is genuinely new in the resumed round

1. The exact commuting nilpotent generator identity for independent coordinate
   biases is pushed through the complete entropy Hessian, including every
   acceleration and Fisher cross term.
2. The off-diagonal Hessian is reduced exactly to conditional two-site faces
   with the scalar functional
   `Phi=(ad-bc)sum(1/q)-log(ad/bc)`.
3. An exact rational target-benchmark DPP gives `Phi>1/714`; direct sums make the
   positive mixed payment extensive.
4. A separate exact scalar DPP proves a positive fixed-`a` contrast response
   larger than `560/169` per site on the whole centered strip at `c=0.926`.
5. The remaining global payment is isolated as the convexity of total
   correlation under scalar diagonal shifts, equation (7.2) of `proof.md`.

## Assumed reviewed inputs

Only the frozen definitions, the exact DPP channel representation, the reviewed
`c<=37/40` curvature theorem, and value convergence of finite sine blocks are
used to explain why the routes matter.  The exact counterexamples themselves
need none of the reviewed curvature or rate theorems.

## Analytic proof versus certificates

- **Analytic:** all identities and inequalities in `proof.md`.
- **Exact certificate:** rational Loewner checks, atom probabilities, algebraic
  face term, rational lower bounds, and product response bound in
  `evidence/exact_route_certificate.json`.
- **Floating only:** random/Toeplitz Hessian scans and optimization evidence in
  `evidence/floating_diagnostics.json`.  These do not establish any theorem.
- **Old checkpoint:** everything under `old_checkpoint/` is retained solely for
  continuity and is explicitly unreviewed/rejected as completion.

## Exact target-level gap

For a finite DPP along `K(a)=aI+cQ`, prove or refute

```text
TC(a) = sum_i b(K_ii(a)) - H(DPP(K(a)))
TC''(a) >= 0.
```

Equivalently, with `r_i=P(Y_i=1|Y_-i)` and `mu_i=P(Y_i=1)`, prove

```text
2 sum_{i<j} H_ij
 <= sum_i [ E 1/(r_i(1-r_i)) - 1/(mu_i(1-mu_i)) ].
```

Individual mixed terms and their aggregate positive part cannot simply be
assigned sign: the exact direct-sum witness disproves that.  A quantitative
contrast response also cannot have free nonpositive sign: the product witness
forces a positive budget above `560/169` per site at the benchmark.

## What is not claimed

- no proof of the full sine target;
- no counterexample to the sine target;
- no thermodynamic inference from small blocks;
- no derivative interchange with the limiting rate;
- no independent review;
- no claim that total-correlation convexity is true merely because diagnostics
  did not find a violation.
