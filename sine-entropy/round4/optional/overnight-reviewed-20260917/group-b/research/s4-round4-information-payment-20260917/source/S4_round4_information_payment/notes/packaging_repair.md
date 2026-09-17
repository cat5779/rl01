# Packaging repair — not a mathematical change

The first finalization attempt stopped before creating the final ZIP with `KeyError: utc`. The preserved start record uses the keys `start_utc`, `start_unix`, and `start_monotonic`; the finalizer mistakenly requested `utc` and `monotonic`. The finalizer was corrected to read the actual keys. No start time or mathematical certificate was changed.

A verification command run after that interrupted finalizer reported the expected stale preflight manifest: the newly expanded proof, report, and extracted-replay receipts had not yet been rehashed. This was a packaging-stage mismatch, not a failed parsed-JSON mathematical replay. The completed final archive is rehashed and checked separately.

The timestamp record remains the original captured JSON. This repair is not credited as new research and is included so the unsuccessful finalization is not hidden.
