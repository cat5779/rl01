# Dependency versions

The exact proof replay uses Python 3.11 or later and only the standard library:

- `argparse`, `fractions`, `hashlib`, `json`, `math`, `pathlib`, `subprocess`,
  `tempfile`.

The optional deterministic floating diagnostic uses NumPy.  Its output is not
proof evidence.  Packaging was performed on Linux with Python 3.13.5.

All text files are UTF-8 with LF line endings.  JSON comparison is parsed rather
than byte-sensitive to line endings.
