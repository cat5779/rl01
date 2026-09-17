# Replay receipt

- Cumulative package `verify_manifest.py`: PASS, 40 files match `MANIFEST.sha256`.
- `symbolic_checks.py`: PASS with locally cached SymPy; generated JSON equals the frozen JSON as parsed data.
- Full `replay.py`: BLOCKED by missing SciPy in the designated local Python runtime.
- Affected jobs: central-band numerical receipt, clock-curvature numerical receipt, and small finite-slice enumeration. These are diagnostic receipts; the analytic proof does not depend on them.
- No package dependency was downloaded from the network.

