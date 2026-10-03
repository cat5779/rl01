# Exact three-input consistency gap

The frozen derivation question is resolved in its stated range. Start with [RESULT.md](RESULT.md), then [REVIEW.md](REVIEW.md). [TASK.md](TASK.md) is the unchanged historical question; its original open-status line records the state when the task was issued.

For every `0 < eta <= 1/10`, the pairwise optimum is `48 eta/21`, whereas the simultaneous three-input optimum is `52 eta/21`. Both statements concern the complete twelve-edge positive birth-flow fibers, including all capacity constraints. Their exact ratio is `13/12`.

The result prevents simultaneous attainment of all pairwise optima. It does not show an unbounded selection constant, a failure of the canonical weighted optimizer, or a counterexample to the general flow-selection conjecture. The related [fixed-projector Holder line](https://github.com/cat5779/rl01/pull/123) remains distinct.

The returned proof was preserved byte-for-byte from [tools PR150](https://github.com/randomcat4/dpp-entropy-tools/pull/150), commit `15edc060e32c04d3cd08438ca05905737013ebd0`. Two different-author mathematical reviews and two independently written exact-arithmetic checks agree. These are internal scoped reviews; external referee acceptance, formal certification and novelty are not asserted.

Run `python CHECK.py` with SymPy installed for the symbolic reconstruction. `CHECK2.py` independently uses rational polynomial arithmetic from the Python standard library. Their recorded executed results are included. [SOURCE.json](SOURCE.json) records hashes and provenance.
