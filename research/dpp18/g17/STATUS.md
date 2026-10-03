# Status

`PROVED / CORRECT_SCOPED / MAIN_AUDIT_PASS`

For every fixed finite canonical component bound `r`, there is one Borel,
coordinate-permutation-equivariant nonnegative selector in the original flow
fiber whose Lipschitz constant depends only on `(epsilon,r)`, not on the
ambient dimension or the number of components.

The complete proof is in `RESULT.md`.  `REVIEW01.md` is the review bundled with
the returned packet; `REVIEW02.md` is the independent main audit.

The theorem is **not** uniform as `r` tends to infinity.  Its explicit coarse
constant grows like
`10 epsilon^(-2) (r!)^2 2^((r-1)(r+4))`; therefore it does not settle the
unrestricted delocalized selector problem.

No formal verification, field referee report, or novelty certification is
claimed.  This Draft PR is not approved for merge.
