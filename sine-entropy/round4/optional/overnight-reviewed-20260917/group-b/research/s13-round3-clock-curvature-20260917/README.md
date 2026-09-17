# S13 round 3 reviewed lane

Start with `INDEPENDENT_AUDIT.md`. The accepted new unit is `author/proof.md`, Theorem 3.1 only with its supporting lemmas. The prior theta/scope gate used as a dependency is preserved at `provenance/S13_GATE.md`.

The untouched cumulative package is preserved under `source/S13/`. From `source/S13/`, the package integrity command is:

```powershell
python 'verify_manifest.py'
```

It passed with 40 files. With NumPy 2.3.5, SciPy 1.17.0, and SymPy 1.14.0 installed, the full round-3 diagnostic replay command is:

```powershell
python 'round3_author_result\scripts\replay.py'
```

The designated runtime used for this audit lacked SciPy, so that full diagnostic command was not recorded as executed. The symbolic job was executed independently and matched the frozen JSON as parsed data. These receipts are diagnostics; the acceptance rests on the analytic proof.

Directories named `round1_unreviewed`, `round2_unreviewed`, and `exploration_unproved` are retained only to preserve the cumulative archive and are excluded from the accepted result.

