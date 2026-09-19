# S64 exact checks

The mathematical statements and their exact scopes are in `../S64_CYCLE11_RESULT.md`.
The overall entropy-rate objective is **INCOMPLETE**. These checks certify finite inputs to the proved KL extrapolation theorem and the actual-sine monotonicity counterexamples.

All mathematical interval arithmetic uses Python integers and rational outward rounding; no external packages are required. Runtime `seconds` fields are measurement metadata only.

- `certify_s64.py` enumerates all full configurations and encloses their Shannon entropy.
- `certify_pair_atoms.py` independently enumerates two complete DPP laws and encloses full-configuration KL and cross entropy.
- `certify_pair.py` performs the separate conditional-chain calculation; the 16-site retained output combines its two first-bit subtrees and its root contribution.
- `kl_budget_check.py` encloses the optional determinant budget using exact-interval LDL elimination.
- `verify_s64.py` recomputes the sign deductions and the two-volume KL budget from retained raw enclosures, and checks the intersections between independent calculation methods. `--recompute` also regenerates all entropy inputs. The atom-pair commands below regenerate the KL inputs used by the verifier.

```bash
python verify_s64.py
python verify_s64.py --recompute
python certify_pair_atoms.py --n 15 --output pair_atoms_n15.json
python certify_pair_atoms.py --n 16 --output pair_atoms_n16.json
python verify_s64.py
python kl_budget_check.py
```

The finite-core inputs are true Toeplitz sine kernels at rho=1/2 and c=19/20. The main chord is [1/50,3/100], not the old [3/200,7/200] chord. The second counterexample chord is [1/50,21/1000].

`finite_chord_certificate.json`, `second_chord_certificate.json`, and `convex_length_certificate.json` contain derived certified intervals. All larger-volume KL payment follows analytically from conditional KL supermodularity; no larger block entropy enumeration or enormous QWE02 cutoff is being claimed.
