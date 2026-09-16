# Manifest policy

`manifest.json` records SHA-256 hashes and byte sizes for every immutable package
file except itself, `MANIFEST.sha256`, and the mutable `output/` tree. The ZIP
container hash is reported outside the inner manifest because including it would
be recursive.

`python3 scripts/verify_manifest.py` verifies all listed files. The replay script
then regenerates certificates below a caller-selected output directory and
compares parsed exact JSON fields. The Decimal real-q grid is intentionally not
part of the exact comparison.
