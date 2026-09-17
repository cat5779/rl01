# S4 round 4 reviewed lane

Start with `INDEPENDENT_AUDIT.md`. The accepted author proof is `author/proof.md`; exact certificates are under `receipts/`; provenance records the archive hash and extraction scope.

The untouched author package is preserved at `source/S4_round4_information_payment/`. From that directory, with the designated Python runtime, the original self-check commands are:

```powershell
python 'scripts\verify_manifest.py'
python 'scripts\replay.py' --out-dir 'output\independent-replay'
```

The first command passed with 42 files. The second passed for both exact certificates and the frozen-evidence guard. The staged convenience entry point `code/replay.py` uses `code/` and `receipts/` and writes only to a fresh output directory.

Acceptance is limited to the theorem scopes recorded in `INDEPENDENT_AUDIT.md`.

