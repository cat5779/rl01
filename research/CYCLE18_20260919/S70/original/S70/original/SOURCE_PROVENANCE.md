# Preserved original sources and provenance

The supplied task is S70 in repository `cat5779/rl01`, PR45, branch
`research/sa-cycle11-pr128-20260918`, task date 2026-09-19.

The authoritative self-contained packet was read directly through the web tool:

```text
https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle11-pr128-20260918/research/CYCLE16_20260919/S70/PACKET.md
```

The startup prompt was read at:

```text
https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle11-pr128-20260918/prompts/CYCLE16/S70.md
```

`S63_CERTIFICATES/` preserves the supplied text/data used or adapted in this
proof, separately from the new implementations:

```text
alpha60.txt
arithmetic_selftest.cpp
cert_interval.hpp
exact_fixed.hpp
global_ratio_certificate.cpp
guard_caps_integer.txt
guard_certificate.cpp
payment_certificate.cpp
principal_probability_certificate.cpp
```

The individual original files were supplied beneath this public source prefix:

```text
https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle11-pr128-20260918/research/CYCLE16_20260919/S70/sources/S63_CERTIFICATES/
```

These local copies were transcribed from the supplied text attachments/public
raw sources. This is not a claim to have cloned, checked out, written to, or
modified the repository. No byte-identity or checksum acceptance gate is used.
The original `PACKET.md` was readable on the web, but downloading its complete
bytes into the container failed; this focused archive therefore does not claim
to include an unmodified complete packet or unrelated supplied attachments.
The new `RESULT.md` states all mathematical objects and dependencies it uses and
contains a complete proof of the reductions needed for the new certificate.

The files under `../certificates/` are the executable proof sources. The original
arithmetic and principal-probability programs were reused; new/modified files
are explicitly named `quad_*`, `cert_interval_fast.hpp`, `exact_*`,
`arithmetic_audit.*`, `direct_payment_check.cpp`, and `verify_coverage.py`.
The initial and final tool specifications are kept at the package root.

The S70 packet's current accepted-scope statements govern comparison with S63.
Historical PROVED labels, old review diagnoses, or author log messages are not
independent evidence for the new result. In particular the original row-sum
Loewner error bound is valid; no factor-two repair is made here.
