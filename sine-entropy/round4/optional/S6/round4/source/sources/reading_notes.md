# Public-source reading notes

## Handoff packet actually read

Snapshot commit:
`c307fe1bcf46b56e4755655c90f60a681979bf13`

Mandatory raw files read:

* `sine-entropy/round4/S6.md`
* `sine-entropy/round4/TARGET.md`
* `sine-entropy/round4/KNOWN_RESULTS.md`
* `sine-entropy/round4/PITFALLS.md`
* `sine-entropy/round4/CONTRACT.md`
* `sine-entropy/round4/READING_MAP.md`

Optional lane evidence read as needed:

* `sine-entropy/round4/optional/S6/proof.md`
* `sine-entropy/round4/optional/S6/gap_audit.md`

The optional proof supplied the reviewed older S6 obstruction only; it did not
contain the latest local Round 3 theorem.

## Primary source 1: concentration

Robin Pemantle and Yuval Peres,
*Concentration of Lipschitz functionals of determinantal and other strong
Rayleigh measures*, arXiv:1108.0687v3 (2013),
https://arxiv.org/abs/1108.0687 .

Imported result: **Theorem 3.2** and its immediately following remark.  Exact
hypotheses: a strong Rayleigh probability measure on the Boolean lattice, mean
`mu=E N`, and a Hamming-1-Lipschitz real function.  Exact two-sided conclusion:

`P(|f-Ef|>a) <= 5 exp[-a^2/(16(a+2mu))]`,

with the denominator replaceable by `48n` because `a,mu<=n`.

New connecting work not in the source: proving the full DPP information content
is `Lambda_delta`-Lipschitz through L-principal-minor ratios; deriving the
explicit MGF constant; and applying it to the exact correlated Holder/Renyi
remainder.

## Primary source 2: approximation theory

Herve Queffelec and Rachid Zarouf,
*On Bernstein's inequality for polynomials*, arXiv:1903.10801v1 (2019),
https://arxiv.org/abs/1903.10801 .

Imported result: **Theorem 1.1**, the sup-norm inequality
`||T'||_infinity <= D ||T||_infinity` for a trigonometric polynomial of degree
at most `D`.

New connecting work not in the source: the nested real-interval second-derivative
bound, its use on the exact full-atom Chebyshev series, and the high-contrast
transport theorem.

## Context source: strong Rayleigh

Julius Borcea, Petter Branden, and Thomas Liggett,
*Negative dependence and the geometry of polynomials*, arXiv:0707.2340,
https://arxiv.org/abs/0707.2340 .

The package uses the terminology/definition only.  Stability of the exact
L-ensemble generating polynomial is proved directly, so no theorem from this
source is an unverified bridge.

## Scouted but not imported: cluster expansion

Rodrigo Bissacot, Roberto Fernandez, and Aldo Procacci,
*On the convergence of cluster expansions for polymer gases*,
arXiv:1002.3261,
https://arxiv.org/abs/1002.3261 .

The source was checked for abstract/subset-polymer convergence criteria.  No
activity map satisfying a high-contrast summability condition was proved, so no
result from it is used.
