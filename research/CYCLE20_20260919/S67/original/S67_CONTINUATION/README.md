# S67 continuation delivery

Main manuscript: `S67_ACCELERATION_CONTINUATION_RESULT.md`.
An identical copy named `S67_ACCELERATION_RESULT.md` preserves the original requested manuscript basename within this continuation folder; the previous delivery outside this folder is not overwritten.

## Result

PROVED analytic acceleration bound: limsup C_n/n <= 110333/166400000.
INCOMPLETE entropy-rate objective: this upper bound does not meet the reviewed cap.
The finite-window Fisher input 20.75 is a conditional sufficient criterion, not a verified model fact.

## Reproduce

From this directory:

```bash
python code/verify_exact.py
python code/check_small_actual_sine.py
```

The first program uses only the Python standard library and exact rational acceptance comparisons. The second uses optional mpmath for actual-sine diagnostics and does not produce interval certificates.

Do not equate the presence of a script with a successful execution. Consult `certificates/delivery_execution_report.json`, each exit-status file, stderr, and the program-generated JSON output. No hash, archive, or packaging check is a mathematical acceptance gate.

The original exhaustive S64 n=15/16 program was not rerun. Its independently reviewed intervals are accepted inputs. The new manuscript does not certify 120 minutes of active research: the resumed context did not preserve an inspectable continuous timer, and verifier runtime is not research-session duration.

## Recorded execution summary

{
  "generated_utc": "2026-09-19T06:28:11.506695+00:00",
  "research_duration_minutes": "NOT_CERTIFIED",
  "requested_research_duration_minutes": 120,
  "reason": "The resumed visible context does not supply a complete independently inspectable continuous active-research timer. Execution wall seconds are not substituted for it.",
  "entropy_rate_objective": "INCOMPLETE",
  "proved_acceleration_C_upper_fraction": "110333/166400000",
  "new_verification_status": "PASS",
  "actual_sine_diagnostic_status": "PASS_DIAGNOSTIC_NOT_CERTIFICATE",
  "original_n15_n16_verifier": "NOT_RERUN",
  "repository_writes": "NONE",
  "hash_or_zip_acceptance_gate": "NONE",
  "exact_verification_exit_status": "0",
  "exact_verification_wall_seconds": 0.024223699999993187,
  "exact_A_limsup_upper_interval": {
    "lower": "0.00051637841390488528321703772123076923076923076923076923076923076923",
    "upper": "0.00051637841390488528321703772123076923076923076923076923076923076924"
  },
  "conditional_finite_input_status": "UNVERIFIED: not asserted for any finite window or infinite model",
  "small_actual_sine_exit_status": "0",
  "small_actual_sine_wall_seconds": 2.210642929999949
}
