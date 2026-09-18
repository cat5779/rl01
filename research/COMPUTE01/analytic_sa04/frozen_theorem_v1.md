# Frozen theorem v1

Status: frozen by the main instance.  A proof attempt may not modify the
premises.  Proof and verification instances must not modify, add, or
reinterpret them.

## Objects and definitions

Use exactly the corrected SA04 objects and clocks in `assumptions.md`.  Put
`n=2k` and `d_k=A_k-E_k`.

## Intended claim

There exist explicit constants `epsilon>0` and `k_0` such that for every
integer `k>=k_0`,

\[
d_k\ge epsilon.
\]

## Success standard

A proof must separately lower-bound `A_k`, upper-bound `E_k`, preserve the
original clock, and give explicit constants whose difference is positive.

## Allowed information

The reviewed SA04 report, exact Fourier projection identities, elementary
information inequalities, reversible-chain calculations, and explicitly
proved local-limit or spectral estimates.

## Forbidden shortcuts

- replacing `s_k` by a fitted or total-rate-one clock;
- treating finite computations as the all-`k` proof;
- assuming `A_k-E_k` has a sign;
- renaming the desired bound as an unproved lemma;
- transferring the result to the true output entropy rate.

## Non-claims

Version 1 does not assert a limit for `d_k`, a leading constant for `W_n`, or
the sign of `W_n+C_n`.
