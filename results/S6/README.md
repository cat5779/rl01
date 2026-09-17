# S6 round four: reviewed narrow high-contrast sign and real-q block error

**Scoped acceptance. The full sine entropy-rate concavity target remains OPEN.**

The [original proof](PROOF.md) is preserved byte-for-byte, together with
its original package, manifests, finite evidence, attempts, and claimed timing.
The [full independent audit](AUDIT.md) covers both mathematical
results and reproduction. A [second fresh audit](https://github.com/cat5779/rl01/blob/7f081d311ced85cbf850605646808425f6b70129/sine-entropy/round4/optional/S6/round4/SIGN_SECOND_AUDIT.md) checks
the actual high-contrast sign theorem independently.

## Accepted statements

For every finite Hermitian contraction Q and all n, contrast
`c in [37/40,37/40+10^(-13)]` and shifts `|a-(1-c)/2|<=1/200` satisfy
`H(DPP(aI+cQ))''/n<=-1/200`. Integrating first and passing entropy values to
the limit gives the corresponding sine-rate strong Jensen inequality, for
every fixed density, with bonus `t(1-t)(a_1-a_0)^2/400`.

The proof re-establishes an exact full-atom Hermitian-pencil expansion,
dimension-independent polynomial-degree cancellation, and a nested-interval
value-to-curvature bound. These pay a contrast perturbation from the reviewed
37/40 margin. They do not simply differentiate an arbitrary entropy value error.

For the product w of true consecutive R-block marginals, the positive real-q
remainder E defined in source/proof.md satisfies
`0<=E/n<=c Tr b(Q_R)/R+2880 log((1-delta)/delta)^2 |q-1|`
throughout `q in [1/2,3/2]`, n divisible by R, and the stated fixed interior
spectral/shift strip. Its absolute finite Jensen defect obeys the same bound.
The vanishing limit requires both R->infinity and q->1. The reference retains
within-block spatial dependence and includes every moving-reference term.

## Scope limits

The contrast extension has width only 10^(-13) and shift interval length 1/100.
It does not raise the all-shift universal 37/40 threshold or settle arbitrary
high contrast. The real-q theorem leaves the growing-block main-term sign open.
No formal Lean certificate, global novelty/priority certification, or complete
field-method exhaustion is claimed. Earlier local round-three claims were not
granted as assumptions: required ingredients are re-proved in this source.

## Reproduction

From source/, run `python scripts/replay.py --output-dir <fresh-output-path>`.
The Python scripts use the standard library. Exact rational checks support the
constants; finite atom and Decimal q examples do not replace universal proofs.
Current integration hashes are in the repository root MANIFEST.sha256;
source/manifest.json and source/MANIFEST.sha256 retain the author archive hashes.
See the audit for verifier limitations and independent checks.

## Provenance and timing

SOURCE.json identifies the original ZIP by SHA-256. The author's measured
research interval is 26 minutes 31.447 seconds; the author invokes the contract's
completed-nontrivial-result exception, not a 90-minute run. The scoped results
pass independent review, but the detailed account of time spent is self-reported.
