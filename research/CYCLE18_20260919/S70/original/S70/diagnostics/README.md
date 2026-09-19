# Failed and superseded certificate attempts — NOT proof evidence

These files make the two actual guard repairs inspectable. They are not used
as successful cells in the final-source complete cover under `../logs/`.

`quad_tau3_candidate_integer.txt` is the unmodified candidate distance-three
allocation. The final `../certificates/quad_tau3_integer.txt` differs only at
zero-based word rows 99, 100, and 152, each reduced by exactly 20. Thus their
final guard caps increase by exactly 20/1000. Every subsequent payment, norm,
PSD and exact continuum calculation uses the final rows, not this candidate.

`quad_guard_distance3_full.log` is the old full candidate run: it failed 56
parameter-word cells. All failed words belong to {99,100,152}. It is not a
proof of that candidate. `quad_guard_distance3_repaired.log` checks all 126
parameter-word cells of those three words with the repaired input. The other
253 rows did not change. A complete clean final-source rerun supersedes both.

`quad_guard_nearest_extension.log` contains 13 inverse-radius aborts at word
231 under the original optional 1e-8 abort threshold. These are recorded errors,
not successes. `quad_guard_nearest_inverse_recheck.log` rechecks every one of
that word's 42 cells with the true computed error radius retained and a 1e-6
abort threshold. The final full-source rerun uses the latter threshold for all
words, always paying the actual row-sum radius in its Loewner bounds.

`quad_guard_refined.cpp` is a superseded three-word-only verifier used during
repair attempts; its filtering and old numerical abort threshold are visible
in the source. It is not called by the final `run_all.sh`. These diagnostic
runs do not assert an entropy counterexample and are not an independent theorem
about any parameter grid.

For a repeat of the historical unclosed-candidate cases, work in a disposable
copy of `../certificates/`, build `quad_guard`, replace only its distance-three
input by this directory's candidate table, and run
`./quad_guard 3 7 6 0 10752 4 2000000 7`.
For the nearest inverse abort diagnostic, change only the visible optional
`eps>1e-6L` abort test in that disposable source to `eps>1e-8L` and run
`./quad_guard 1 7 6 6144 10752 4 2000000 7`.
The two successful focused rechecks using the final source and final inputs are
`./quad_guard 3 7 6 0 10752 4 2000000 7 99,100,152` and
`./quad_guard 1 7 6 0 10752 4 2000000 7 231`.
These historical diagnostics are optional; the accepted mathematical proof uses
the clean complete final-input runs with a four-million-node safety limit.
