# S19 reviewed route obstruction

This directory stages the independently checked S19 increment from PR115 at
`9ca8e58d5ff92d06bd13b968bacb52a4dfada95d`.

**Status: ACCEPTED_SCOPED / ROUTE_OBSTRUCTION.**  The accepted theorem rules
out the specific vanishing-exception repair

`sum E[(g_+ - gamma W)_+] = o(n)` for every fixed `gamma <= 2`

on the stated half-density Toeplitz family and channel interval.  It does not
give the sign of the signed near field, the full Hessian, or the entropy-rate
target.  The supplementary signed-cylinder inequality is also accepted only
at its stated pointwise cylinder scope.

Read `INDEPENDENT_AUDIT.md` for the mathematical decision and
`INTEGRATION_SUMMARY.md` for integration boundaries.  The copied proof and
standard-library replay code are under `proof/` and `code/`.

Replay from this directory with the configured Python interpreter:

```text
python code/verify_reference_payment.py --output reference-payment.json
python code/verify_analytic_constants.py
python code/verify_signed_reference.py --output signed-reference.json
python code/test_budget_identity.py
python code/test_rational_intervals.py
```

