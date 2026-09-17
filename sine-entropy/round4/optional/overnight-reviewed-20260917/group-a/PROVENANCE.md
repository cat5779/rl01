# Provenance and replay record

Review date: 2026-09-17.  Repository baseline used for dependency lookup:
`aaf3e86576a867067701089805c9e5e5a83e44f5`.

The archives were inspected before extraction.  Absolute paths, parent
traversals, drive-qualified members, and symbolic links were rejected; all four
archives passed.  Extraction receipts are preserved under each packet's
`receipts/` directory.

| Packet | Source archive | SHA-256 |
|---|---|---|
| S1 | `S1_cumulative_round4_check2.zip` | `28cf8ca4be573856d6888a00e41db3315c9c20f4ec603d125e20d04291a7f39f` |
| S2 | `S2_check1_cumulative.zip` | `d3b12be8102857bf46351add1b3494201f97a75678f3ef2e0265ee00c4b7ea0f` |
| S11 | `S11_resumed_continuation_obstruction.zip` | `f09442bea9390a234bb07448c0e01424b2c5860e340d94460eadeb6eabfa068a` |
| S12 | `S12_structural_route_obstructions.zip` | `fbe109ca236d0a352a9cb2dadc0a6a3e3f53c17c82a7afbc03091d173168946f` |

Independent replay used
`[LOCAL_USER]/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.

- S1: `verify_constants.py` and `verify_fourier_tail.py` passed.  The latter is
  a finite floating regression and was not treated as a general proof.
- S2: all five jobs in `reproduce.py` passed; the regular and optimized exact
  laws and jets agreed.  The fresh receipt is in `s2/receipts/replay_receipt.json`.
- S11: the package validator rebuilt and independently rechecked the exact
  certificate, checked the two-site witness, document constants, refined cover,
  old-checkpoint hash, and package manifest.  The optional SymPy reconstruction
  could not run because SymPy is absent from the specified runtime; its algebra
  was checked directly in the proof review and it is not needed by the exact
  standard-library certificate.
- S12: the exact certificate, deterministic floating diagnostics, and manifest
  replay passed.  Only exact rational fields were used as theorem evidence.

Files under `author/` and `code/` are preserved source excerpts.  Their own
status labels do not override the independent dispositions in this directory.

## Packaged layout

The integration overlay is self-contained.  `REPRODUCE.md` gives commands from
the group root, and `MANIFEST.sha256` covers every frozen file.  The S2 runner
locates its children under packaged `s2/code/`; S11's document audit reads the
packaged `s11/author/` and `s11/receipts/` paths; S12 carries both exact and
diagnostic frozen evidence under `s12/evidence/`.  Replays write only to
packet-local `replay/` directories, which are deliberately outside the frozen
manifest.
