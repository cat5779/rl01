# S70 reproducible proof packet

## Result

`RESULT.md` is the self-contained English proof, including all 256 witness rows,
all 45 three-component coefficient boxes, the full scope/dependency ledger,
falsification attempts, and the remaining full-target inequality.

**Proved:** rho=1/3, c in [19/20,1907/2000]=[.95,.9535], p in [21/50,12/25]=[.42,.48],
a=(1-c)p. For every n>=22,

`d^2 H_n / da^2 <= -n/25 + 441`.

This yields the true configuration-entropy-rate chord lower bound
`lambda(1-lambda)(a1-a0)^2/50` for every fixed c and both legal bias endpoints
in [.42(1-c),.48(1-c)]. The c-width is .0035, with the full requested p-width.

**Also proved:** on the nested c interval [.95,.953], the curvature coefficient
improves to 1/5 and the rate chord coefficient to 1/10, with the same boundary 441.

**Not proved:** the entire proposed contrast rectangle through .96. The precise
fixed-witness obstruction at c=.96,p=.45 is independently enclosed by exact
rational arithmetic: this witness's payment excess is less than -3. This is not
an entropy-concavity counterexample.

## Contents and source provenance

`original/S63_CERTIFICATES/` preserves the supplied S63 sources and integer data
used or adapted here. They are separate from every new or modified verifier.
`original/SOURCE_PROVENANCE.md` identifies the public packet and individual source
locations and records that these are transcriptions of supplied text, not a claim
to have cloned or modified the repository. The full supplied packet remains the
authoritative original; unrelated source attachments are not copied into this
focused output archive.

`certificates/` contains the executable mathematical verifiers and exact inputs.
`evidence/` contains exact rational results and complete coefficient/norm data.
`logs/` records successful final proof runs. `diagnostics/` contains the explicitly
failed or superseded guard attempts and their exact changed rows; these are not
accepted certificate cells. `TOOL_SPEC_INITIAL.md` preserves the requirements
written before construction; `TOOL_SPEC.md` also states the proved endpoint-only
relaxation used by the final block.

The package does not contain the 160 MiB reference probability cache. All four
chunks are reconstructed by the supplied exact principal-minor program. No
network, source checkout, repository write permission, or binary attachment is
needed for reproduction.

## Reconstruct everything

From this directory run:

```bash
bash run_all.sh
```

Optional environment choices are `CXX`, `PYTHON`, `THREADS` (positive integer;
default 4), and `OUT` (default `./recomputed`). For example:

```bash
THREADS=2 CXX=g++ PYTHON=python3 OUT="$PWD/recomputed" bash run_all.sh
```

The script copies readable source and integer files into a fresh working output
area and does not change the preserved originals. It uses a C++17 compiler with
OpenMP and Boost.Multiprecision headers, and Python 3.10 or later with its standard
library. No NumPy, SciPy, plotting, external solver, or third-party Python package
is required for the mathematical certificates.

The C++ interval implementation explicitly requires binary long double with 64
significand bits. An unsupported format fails at compilation. The reference
run used GCC 14.2.0, Python 3.13.5, the checked 256/512-bit Boost integer backends,
and 192 fractional bits for principal-minor intervals. The tested compilation
options are:

```text
-O3 -frounding-math -ffp-contract=off -std=c++17
```

OpenMP verifiers additionally use `-fopenmp`. Do not use fast-math. Different
thread reduction orders can change the last outward integer endpoints; correctness
is assessed by rerunning the interval and exact-rational inequalities, not by
requiring identical bytes or a matching checksum.

## Each proof obligation and its verifier

| Verifier/input | Mathematical obligation |
|---|---|
| `alpha60.txt`, `exact_closure.py` | Sine scalar enclosure by exact Machin/alternating-series/square inequalities, including the guard's coarser rational bracket. |
| `principal_probability_certificate.cpp`, `exact_fixed.hpp` | All 2^22 exact-reference configuration probabilities, using the true finite compression and L-ensemble principal minors. |
| `arithmetic_selftest.cpp` | Preserved-source exact audit of primitive rounding, signed fixed division and conversion. |
| `arithmetic_audit.cpp/.py` | New exact audit of the guard header, including root and shortened-log enclosures in four rounding modes. |
| `quad_global.cpp` | Global scalar pair cap C=1.303+.255p+8(c-.95), over 33,600 closed parameter cells and continuous scalar intervals. |
| `quad_guard.cpp` | Three distances, all 256 guard words, 42 parameter cells per word; all compatible posterior matrices and exterior observations enclosed. |
| `guard_caps_integer.txt` | Supplied 256 (L,U) rows, used in the new kappa(p) formula with an explicit +.02 allowance and rechecked over new parameters. |
| `far_tau_integer.txt`, `quad_tau3_integer.txt` | Final new distance-two and distance-three allocation numerators, denominator 1000. |
| `quad_payment.cpp` | Fixed reference scores at targets 9,10,11,12; affine potential norms; full-law signed tensor transport; all degree-eight Walsh coefficient boxes with exact 2^-22 normalization. |
| `exact_closure.py` | All 16,384 PSD corner matrices with slack I/200; complete-vector tail; exact tensor Bernstein payment and upper bound over a closed rectangle. |
| `exact_small_tests.py` | Exact rational checks of transport, Walsh coefficients, score identities, third-bit weights, and marginal score martingales. Not an asymptotic theorem. |
| `exact_block_test.py` | Exact rational checks of the combined endpoint-only PSD allocation/Jensen/variational argument with two overlapping target-dependent blocks. Not an asymptotic theorem. |
| `direct_payment_check.cpp` | Independent all-word direct tensor evaluation at two exact parameter pairs, without Walsh aggregation or truncation; checks the near-boundary positive margin and the negative fixed-witness margin. |
| `exact_obstruction.py` | Full-law fixed-witness payment obstruction at c=.96,p=.45 with a separately recomputed tail. Not an entropy counterexample. |
| `verify_coverage.py` | Exact parameter/word/input bookkeeping and complete recorded covers; not a replacement for the source algorithms proving their inequalities. |

## Direct commands and exact parameters

Within the working source directory, the essential calls are:

```bash
./principal_probability_certificate 22 2 0 prob22_0.bin
./principal_probability_certificate 22 2 1 prob22_1.bin
./principal_probability_certificate 22 2 2 prob22_2.bin
./principal_probability_certificate 22 2 3 prob22_3.bin
./quad_global 140 240 4 7
./quad_guard 1 7 6 0 10752 4 4000000 7
./quad_guard 2 7 6 0 10752 4 4000000 7
./quad_guard 3 7 6 0 10752 4 4000000 7
./quad_payment 4
./direct_payment_check 4
python3 exact_closure.py --eta 1/25 --output ../evidence/continuum_broad.json
python3 exact_closure.py --c-upper 953/1000 --eta 1/5 --skip-psd --output ../evidence/continuum_narrow.json
python3 exact_obstruction.py
```

For `quad_guard`, arguments mean: distance, c-cell count, p-cell count, first job,
exclusive last job, threads, maximum posterior-box nodes per job, contrast width
in units of 1/2000. An optional last comma-separated list restricts guard words
for a local recheck; a restricted run is never by itself the complete cover.
The full commands above do not restrict words.

For `quad_global`, arguments mean: c-cell count, p-cell count, threads, contrast
width in units of 1/2000. Its interval endpoints are rational expressions in
these integer arguments. The final cover is c=.95+ic/40000 and p=.42+ip/4000.

`quad_payment_coefficients_bivariate.txt` has all 45 (k,l) rows with k+l<=8 and
six integer endpoints, common denominator 10^9. The actual expectation combines
its three components as V0+(p-.5)VP+(c-.95)VC, with t=200(1-c)(p-.5) and
u=1000(c-.95). `quad_payment_norms_integer.txt` contains 2418,461,15266.
Those output bounds are reproduced for immediate exact closure but are regenerated
from every reference word by a full run. The direct checker has two compiled-in
exact rational inputs: (c,p)=(1907/2000,21/50) and (24/25,9/20). It uses the same
reference probability records and fixed-potential construction but applies each
2-by-2 signed channel factor directly to the entire probability vector. Its
pointwise checks are additional falsification tests, not the continuum argument.

The optional `python3 verify_document_inputs.py` checks the manuscript's parsed
integer tables against the executable inputs and records the three exact cap
repairs. It does not compare hashes or require matching file bytes, and it is
not a substitute for any mathematical verifier.

## Acceptance and limitations

Read the proof of each algorithm in RESULT.md. Each branch verifier either proves
a continuous cell or reports an error/failure; it never accepts a numerical center
sample as a cell theorem. Exact PSD and Bernstein checks use Python Fractions.
The probability records include every word exactly once, and no renormalization,
rare-word trimming, or cyclic substitution occurs.

A run is incomplete if a required verifier aborts, lacks a cell or word, or fails
a mathematical inequality. Printed success strings are not a proof. No hash,
checksum, SHA, manifest, archive-integrity, or matching-file-identity gate is used.
The sources and exact input rows are the reproducible evidence.

Repository files and shared status were not modified. The output is a local
proof/source packet ready for independent review, not an independently reviewed
or accepted upstream result. External novelty is not asserted.
