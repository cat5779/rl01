# S5 reviewed checkpoint: balanced-midpoint actual-adjacent identity

Review status: **accepted as a scoped finite-dimensional identity**.

For every homogeneous half-size input law, the reviewed theorem exactly decomposes the balanced-midpoint curvature of \(\Phi-H\) into a moving-count covariance and a weighted Jeffreys production between the actual adjacent output layers.  The proof retains the layer normalizers, reference curvature, count Fisher term, deterministic boundary layers, and the full conditional response.

Start with:

- `INDEPENDENT_AUDIT.md` for the independent verdict and exact coefficient checks;
- `proof.md` for the self-contained theorem and proof;
- `gap_audit.md` for the remaining target-level obligations;
- `INTEGRATION_SUMMARY.md` for merge guidance.

Reproduce the exact certificates from this directory with:

```powershell
python scripts/exact_midpoint_check.py evidence/author_exact_midpoint.replay.json
python scripts/audit_non_dpp_check.py
```

The first frozen rational comparison was mislabelled as non-DPP.  The reviewed materials preserve it as a general homogeneous example and add a Pluecker-certified non-DPP case.  This correction changes no theorem statement.

The central sign inequality and sine entropy-rate target remain open.  The prior round-4 \(O(\sqrt n)\) residual is not a dependency of the accepted theorem and was not reviewed here.
