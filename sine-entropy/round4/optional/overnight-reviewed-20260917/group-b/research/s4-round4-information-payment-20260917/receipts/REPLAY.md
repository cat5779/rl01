# Replay receipt

- `verify_manifest.py`: PASS, 42 files match the package manifest.
- `replay.py` in a fresh output directory: PASS.
- `exact_check.py`: regenerated parsed JSON equals the frozen exact certificate; LF/CRLF portability check passed.
- `moving_reference_check.py`: regenerated parsed JSON equals the frozen certificate; LF/CRLF portability check passed.
- Frozen-evidence write guard: PASS.
- Optional floating diagnostics were not used for acceptance.

