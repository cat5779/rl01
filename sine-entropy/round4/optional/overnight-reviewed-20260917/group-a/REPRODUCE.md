# Reproducing the packaged checks

Run these commands from this `group-a` directory.  No command reads the original
ZIP extraction directory or another local checkout.  Generated replay files go
under the named packet's `replay/` directory and are not part of the frozen
package manifest.

The exact checks use Python 3.10 or newer and the standard library unless an
optional dependency is stated.  Set `PYTHONDONTWRITEBYTECODE=1` if invoking an
individual child script directly.

## Package integrity

```text
python verify_package.py
```

This checks every file listed in `MANIFEST.sha256` and rejects missing,
mismatched, or unlisted files.  The manifest excludes itself.

## S1

```text
python s1/code/verify_constants.py
python s1/code/verify_fourier_tail.py
```

The constants replay uses the standard library.  The finite Fourier regression
requires NumPy and writes both outputs to `s1/replay/`.  That finite regression
is implementation evidence, not the proof of the growing-size theorem.

## S2

```text
python s2/code/reproduce.py --out s2/replay
```

The runner locates all three child scripts in `s2/code/`, uses only the standard
library, and executes the regular and optimized exact certificates plus the
finite common-frame check.  Its output directory may be removed after review.

## S11

```text
python s11/code/build_obstruction_certificate.py --output s11/replay/obstruction.json
python s11/code/recheck_obstruction.py s11/replay/obstruction.json
python s11/code/exact_two_site_witness.py
python s11/code/cover_resolution_check.py
python s11/code/audit_document_constants.py
```

These packaged commands use only `s11/code/`, `s11/author/`, and
`s11/receipts/obstruction.json`.  In particular,
`audit_document_constants.py` is bound to the packaged split layout and does
not refer to the original author directory.  All five commands use only the
standard library.

The original optional `derive_low_modes.py` SymPy reconstruction is not shipped
because it is supplementary and the accepted exact certificate does not depend
on it.  Its absence is recorded in `PROVENANCE.md`.

## S12

```text
python s12/code/verify_all.py
```

The exact replay uses `s12/evidence/exact_route_certificate.json` and the
standard library.  If NumPy is installed, the runner also executes the labelled
floating diagnostic and compares it with
`s12/evidence/floating_diagnostics.json`; otherwise it reports an optional
skip.  The floating branch is not theorem evidence.
