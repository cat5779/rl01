# Independent S9 round-two audit

Frozen PR head: `2d05b8bd52ef36bb2f7071c019dfea46ce50226d`

## Verdict

The original full S-sine entropy-rate concavity target remains **OPEN**, exactly as the packet says. This audit found no quantum-entropy substitution, count-entropy substitution, or finite-radius-to-rate inference in the units accepted below.

The packet is not acceptable as a single proved theorem package because its main proof file is corrupt in the frozen Git blob. The valid units separate as follows.

| Claim | Verdict | Reason |
|---|---|---|
| `FULL_R3_PRODUCTION.md`: for the half-density radius-three Fejer family, every `37/40 <= c <= 1`, every legal shift and every noise time, `partial_a^2 I_3 >= 6 exp(-2s)`; hence assigned `J_3'' <= -45/16` | **CORRECT** | The analytic reduction is sound and a fresh exact cover rebuilt from committed source completed with 5,843 nodes, 2,922 leaves and zero pending boxes. |
| Exact `R=3` paired exterior-layer integrated curvature `< -1/150`, full integrated production curvature `>4`, and complete seven-site entropy curvature `<0` | **CORRECT** | Fresh 2,048-cell all-atom computation and a separate complete-entropy computation reproduced all three signs. |
| Exact atom polynomials, determinant jets, scaled jets and the `u=0` extension used by the finite results | **CORRECT** | Independent algorithms in the committed checkers passed 4,660 and 2,824 grouped comparisons. |
| RESULT Theorem A: fixed `rho=1/2`, `c=19/20`, central-band Jensen contribution `<-1/40` for every odd `R>=160001` | **CRITICAL_GAPS** | The statement survives before the corruption, but its proof is in the missing/corrupt span. The constants receipt is not a proof of the analytic inequalities that produce it. |
| RESULT Theorem B: limits of total negative and positive layer mass | **CRITICAL_GAPS** | Its statement and proof are in the missing/corrupt span. Downstream summaries cannot replace the proof. |
| Open-density extension, growing circular-Fourier extension, and any other all-radius claim in RESULT sections 4--6 | **CRITICAL_GAPS** | The relevant source span is absent. The recovered bit-shifted tail begins only near the end of section 6 and is nonauthoritative. |
| `LAYER_MEASURE.md` | **CORRECT CONDITIONALLY / QUARANTINED** | The measure argument is sound conditional on RESULT Theorem B, the stated pointwise production bound, and the accepted first-round absolute production-integral approximation. Its finite signed-part convergence therefore cannot be integrated until Theorem B is restored and checked. |
| Claim that the compact packet's cover-replay and certificate-guard commands run directly | **CRITICAL REPRODUCIBILITY GAP, not a mathematical refutation** | The two full cover JSON files and the eight aligned segment JSON files are omitted. `check_cover_replays.py` fails immediately with `FileNotFoundError`, and `test_certificate_guards.py` lacks its inputs. Fresh reconstruction repairs the mathematical evidence, but the documentation must not describe these commands as directly runnable from the compact packet without a reconstruction step. |

## Source integrity

All 44 downloaded files match `snapshot.json` in byte count and SHA-256. Strict UTF-8 decoding of every `.md`, `.py`, and `.json` file found exactly one failure:

```text
RESULT.md: 15009 bytes
first strict UTF-8 error: byte 7501, invalid start byte
non-whitespace C0/DEL control bytes: 45
```

The readable prefix ends immediately after Theorem A equation (7), at `There is no claim that the sum`. A two-bit realignment recovers readable text only near the end of section 6. That tail is useful for diagnosing transport corruption, but it does not recover the missing proof and was not treated as authoritative evidence.

Minimum repair: replace `RESULT.md` with the complete original bytes in valid UTF-8, bind the replacement to a new Git blob, and rerun an independent review of Theorems A and B and sections 4--6. Do not silently reconstruct the missing span from summaries or the shifted tail.

## Independent check of the accepted positive theorem

Put `c_* = 5 pi / 16`. The auxiliary box

```text
K(v,z) = I/2 + v(B+zI),  0 <= v <= 21/20,  |z| <= 1/24
```

is strictly legal: `||B|| <= 5/12` and its spectral margin is

```text
1/2 - (21/20)(5/12+1/24) = 3/160.
```

For an original contrast and shift,

```text
v = u c/c_*,  z = (c_*/c)(a-(1-c)/2).
```

The inequalities `20/21 < c_* < 1` and `c>=37/40` place every requested point in this box. The alternating diagonal gauge sends `B` to `-B`; combined with occupancy complementation it proves `I_3(K(v,z))=I_3(K(v,-z))`, so the nonnegative-`z` cover suffices.

The committed polynomial engine retains the scaled first and second shift jets. Formula (P4) is the exact Hessian of the full moving-weight production, including both atom accelerations. The fresh high-contrast reconstruction produced

```text
classification: AUTHOR_FULL_R3_PRODUCTION_CONVEXITY_CERTIFICATE_NOT_RATE
nodes: 5843
leaves: 2922
pending: 0
minimum scaled-curvature lower:
  510432570398364968770764783276382728089
  ------------------------------------------------
   85070591730234615865843651857942052864
  = 6.000106029789776...
```

Thus `partial_z^2 I_3 / v^2 >= 6`. Since `partial_a=(c_*/c)partial_z`, the factors cancel exactly and give `partial_a^2 I_3 >= 6u^2`. Integrating over `[0,log 4]` gives `J_3''<=-45/16`; integrating over `[0,infinity)` gives the separately stated `-3`. The compact scaled extension supplies the required `O(u^2)` majorant, so no entropy-rate derivative-limit exchange occurs.

The regenerated cover has SHA-256

```text
D4A7C186C31110E0D3B2D9A4A4BA0744B446466C1F300D7E534C723B9A115D6A
```

It cannot be byte-compared with the omitted author cover because execution-time metadata is included in the JSON. Its mathematical tree independently reproduces the author counts and bound. Reloaded complete-structure validation passed, and fresh recomputation of the first and last saved leaves passed. The seven wide-cover tamper guards all rejected their mutations.

## Other exact reconstructions

The full 2,048-cell `R=3` aligned computation rebuilt from source with all 128 atoms and both derivative layers. It returned strict all-atom positivity, negative paired-layer curvature and positive full curvature. Its full curvature interval was

```text
[4.267649730085, 4.489398095299].
```

The paired-layer interval was exactly

```text
[-29531988480838598423146394969568190569 / 340282366920938463463374607431768211456,
 -1247566093130078539313779059906589543 / 170141183460469231731687303715884105728],
```

whose upper endpoint is below `-1/150`. The separate complete-entropy computation returned

```text
H_7'' in [-32.045785638019, -31.138133309497].
```

Eight freshly generated 256-cell segments then passed all ten aligned-certificate mutation guards. These are finite radius-three statements only.

## Layer-measure review

For fixed `delta`, the exterior count is a DPP count, hence a sum of `2R` Bernoulli variables. At half density its mean is `R+2Ru delta` and its variance is at most `R/2`, giving

```text
E |(M_R-R)/(2R) - u delta| <= 1/sqrt(8R).
```

Multiplying this by the pointwise bound `phi(q_R)<=M_D u^2` and integrating `du/u` yields the first term of (M2). The accepted first-round *absolute* production-integral approximation legitimately remains valid after multiplication by bounded `F`, and the true tail is at most `N^-2 log 2`. The pushforward formula for `mu^delta`, its density for `delta=+/-d`, absence of an atom at zero, and mutual singularity with `D_0 delta_0` are correct.

The final weak convergence of the positive and negative parts uses RESULT Theorem B's negative-mass limit. Because that theorem's proof is missing, this last step is logically conditional rather than independently certified here.

## Exact commands and outcomes

Python used:

```text
python
```

From the packet directory:

```text
python code/check_exact_atoms.py --output <audit>/exact_atoms.json
  PASS_EXACT_FULL_ATOMS_AND_JETS 4660 comparisons

python -O code/check_scaled_jets.py --output <audit>/scaled_jets.json
  PASS_SCALED_JETS_AND_FAIR_LIMIT 2824

python code/certify_full_r3.py --state <audit>/full_r3_highcontrast_rebuilt.json \
  --profile highcontrast --fresh --max-nodes 10000
  completed: 5843 nodes, 2922 leaves, 0 pending, 197.806 seconds

python code/certify_full_r3.py --state <audit>/full_r3_highcontrast_rebuilt.json --check-structure
  PASS_COMPLETE_COVER_STRUCTURE

python code/certify_aligned.py --cells 2048 --delta 1/10000 \
  --output <audit>/aligned_full_rebuilt.json
  AUTHOR_FULL_COVER; all three strict tests true

python code/certify_finite_entropy.py --output <audit>/finite_entropy_rebuilt.json
  PASS_FINITE_COMPLETE_ENTROPY_NOT_RATE

python code/test_certificate_guards.py --root <audit>/guard_inputs \
  --output <audit>/aligned_guard_results.json
  PASS_CERTIFICATE_NEGATIVE_TESTS 10
```

The committed `check_cover_replays.py` was also executed against the packet and failed because `outputs/full_r3_cover.json` is absent. This failure is recorded rather than hidden.

## Final integration transcription gate

**STATUS: CORRECT.** The staged integration boundary was checked after the review fixes. Its active `RESULT.md` uses the correct `192^(-7)` normalization for the integer atom-polynomial coefficients. `FULL_R3_PRODUCTION.md` treats the growing adverse-layer material only as an unreviewed, quarantined author claim and derives the elementary bounds `20/21 < 5*pi/16 < 1` from the independent review rather than from a quarantined receipt. The combined S8/S9 index distinguishes the accepted fixed `R=3`, `rho=1/2` Jensen sign from the still-missing all-radius/asymptotic fixed-positive-density sign. No staged passage accepts Theorems A/B, the open-density extension, the growing circular extension, or a finite-radius-to-entropy-rate transfer.

Public-copy note: the local runtime executable path is replaced by `python`; mathematical review and acceptance boundaries are unchanged.
