# Existing evidence and exact boundaries

## GitHub material already in `cat5779/rl01`

1. PR 85, merged: `A W-indexed determinantal factor theorem`.
   - `research/q77r05/g4/THEOREM.md`
   - `research/q77r05/g4/PROOF.md`
   - `research/q77r05/g4/REVIEW01.md`
   - `research/q77r05/g4/REVIEW02.md`
   - https://github.com/cat5779/rl01/pull/85

   The frozen theorem covers every countable set `W`, every **countable**
   group acting on `W`, and every commuting Hermitian positive contraction.
   It allows stabilizers and arbitrarily many orbits.  It does not assert
   equivariance under an uncountable full automorphism group.

2. PR 84, merged: scope and consequences of Lyons--Thom Question 7.7.
   - `research/q77r04/g6/RESULT.md`
   - `research/q77r04/g6/REVIEW01.md`
   - `research/q77r04/g6/SOURCE_REVIEW.md`
   - https://github.com/cat5779/rl01/pull/84

3. PR 82, merged: a scoped nonunimodular `BS(2,3)` DPP factor theorem.
   - `research/q77r04/g4/RESULT.md`
   - reviews in the same directory
   - https://github.com/cat5779/rl01/pull/82

## Local evidence not previously uploaded to GitHub

The run `C:/game/ai4math/math/2026-10-04_fiidclosure01/` proves only that
finite-alphabet FIID laws need not be **weak-star** closed.  Its main files are:

- `frozen_theorem_v1.md`;
- `proofs/routec.md`;
- `verifications/routec_audit.md`;
- `verdict.md`.

For `Gamma=C3*C3` and `t=ab`, the approximants are

`X_n(g)=sgn((2n+1)^(-1/2) sum_{k=-n}^n Z_{g t^k})`.

They converge in finite-cylinder law to independent fair signs copied along
the left cosets of `<t>`.  The limit is not FIID because it is not mixing.
This does **not** answer Question 7.6.  In fact, for every invariant joining
of an approximant with the limit, the limit bit at the identity is
`<t>`-invariant while the approximant marginal is `<t>`-ergodic.  Conditional
expectation therefore makes the two fair bits independent, so their mismatch
probability is `1/2`.  Thus this sequence stays at `bar-d=1/2` from its weak
limit.

## Primary sources

- Lyons--Thom, *Invariant Coupling of Determinantal Measures on Sofic
  Groups*, especially Questions 7.5--7.7 and Section 8:
  https://arxiv.org/abs/1402.0969
- OpenAI, *The free uniform spanning forest is a factor of IID*:
  https://github.com/openai/math/blob/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026.pdf

The OpenAI strongly-Rayleigh theorem treats the regular action on a countable
group and explicitly does not assert an extension to an arbitrary action on
another countable index set.  Its separate FUSF theorem gives a universal
graph-isomorphism-equivariant rule for FUSF, not for every invariant DPP.

## Non-negotiable distinctions

- A countable transitive subgroup of `Aut(G)` is not the full automorphism
  group.
- Equivariance under a countable dense subgroup does not extend through a
  merely Borel map without a new argument.
- Weak-star convergence is weaker than `bar-d` convergence.
- A weak limit of factor laws is not automatically a common-input factor.
- A theorem for DPPs or strongly-Rayleigh laws does not prove closure of the
  entire factor class.
