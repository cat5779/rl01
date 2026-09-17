# Imported inputs and pinned mandatory-reading ledger

All repository inputs were read at the single immutable commit

`191297f3073e60f5954a93ae5e6e94c32447b590`.

The raw paths and retrieval record are listed in
`source_notes/PINNED_INPUT_LEDGER.md`.  This package restates every imported
mathematical fact needed by the proof; review of the new claims does not require
access to another conversation.

## Mandatory files read

1. `sine-entropy/round4/next/S11.md`
2. `sine-entropy/round4/next/CONTRACT.md`
3. `sine-entropy/round4/TARGET.md`
4. `sine-entropy/round4/KNOWN_RESULTS.md`
5. `sine-entropy/round4/PITFALLS.md`
6. `sine-entropy/round4/optional/S6/round4/source/proof.md`
7. `sine-entropy/round4/optional/S6/round4/SIGN_SECOND_AUDIT.md`
8. `sine-entropy/round4/optional/S6/round4/source/scripts/exact_constants.py`
9. `sine-entropy/round4/optional/S6/round4/INDEPENDENT_AUDIT.md`

No result from S12 is assumed.

## I1. Full configuration entropy and legal channel

For a Hermitian contraction `0<=K<=I` on `n` labelled sites, `DPP(K)` is the
binary law with inclusion probabilities `Pr(A subset X)=det K_A`.  Its full
atom at occupied set `S` is

```text
p_K(S) = sum_{B subset [n]\S} (-1)^|B| det K_{S union B},
```

and `H(K)=-sum_S p_K(S) log p_K(S)`.  This is not `Tr b(K)` and not entropy of
`|X|`.

If `Z~DPP(Q)` and, conditionally on `Z`, output coordinates are independent with

```text
Pr(Y_i=1 | Z)=a+c Z_i,
```

then `Y~DPP(aI+cQ)` whenever `0<=a<=1-c`.

## I2. Reviewed base curvature

For every finite Hermitian contraction `0<=Q<=I`, every `0<=d<=37/40`, and
every legal interior shift `a`,

```text
(1/n) d^2/da^2 H(DPP(aI+dQ)) <= -1/50.
```

This is the only base margin used.

## I3. Reviewed S6 high-contrast rectangle

For every finite Hermitian contraction,

```text
37/40 <= c <= 37/40+10^-13,
|a-(1-c)/2| <= 1/200
```

implies normalized curvature at most `-1/200`.  This microscopic rectangle is a
reviewed baseline, not a new result here.

## I4. Full-atom moving-law Chebyshev expansion

On a common spectral strip

```text
delta I <= aI+sQ <= (1-delta)I,
```

let, for a full atom indexed by `S`,

```text
A_{S,s}=aI+sQ-D_{S^c},
X_{S,s}=[2A_{S,s}^2-(1+delta^2)I]/(1-delta^2),
r=(1-delta)/(1+delta).
```

The normalized full configuration entropy has the exact expansion

```text
F_s(a)=C_delta+sum_{m>=1} u_{s,m}(a),
u_{s,m}(a)=(-1)^m r^m/(mn) E_s Tr T_m(X_{S,s}(a)),
deg_a u_{s,m} <= 2m,
||u_{s,m}|| <= r^m/m.
```

The expectation is under the actual moving DPP atom law.  Moving-law
derivatives are not dropped.

## I5. Reviewed nested Bernstein estimate

If `P` has degree at most `D` on an outer interval of length `ell`, and the
concentric inner interval has Bernstein separation parameter `0<sigma<=1`,
then

```text
||P''||_inner <= 4/ell^2 * (D^2/sigma^2 + D/sigma^3)
                 * ||P||_outer.
```

## I6. Rejected-checkpoint tail formula used only to define Family A

The prior rejected package proposed, for `m>M`,

```text
||u_{c,m}-u_{d,m}||
  <= (c-d) r^m (2+a_delta m),
a_delta=2 sqrt(2) delta/(1-delta^2),
```

under

```text
4 delta^3(2-delta)(M+1)^2 >= (1-delta^2)^2.
```

It combined this with the response formula written explicitly in `proof.md`,
Section 2.1.  The present Theorem A is an obstruction **conditional on choosing
that declared certificate family**.  It does not upgrade the old tail lemma to
independently reviewed status.  Theorem B does not use I6.

## I7. Sine value bridge

For the true Toeplitz sine blocks `Q_n`, normalized finite configuration
entropies converge in value to the entropy rate, with a supplied sublinear value
error.  Therefore a finite-dimensional Jensen inequality may be integrated
first and then passed to the limit by values.  No differentiation of the limit
is imported or used.

## External sources

No new external theorem is needed for the two obstruction proofs.  The nested
Bernstein inequality is imported as part of the reviewed S6 packet.  A possible
adjacent-field signed-summation route was scouted but not used; no literature
claim from that scout is promoted into the proof.
