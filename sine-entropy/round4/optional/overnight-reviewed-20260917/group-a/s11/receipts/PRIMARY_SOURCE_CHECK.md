# Primary-source check for the imported Bernstein ingredient

The new obstruction proofs do not import any new external theorem.  Their only
literature-level analytic ingredient is the nested polynomial derivative bound
already proved and reviewed in S6.  For provenance, the primary source used in
that reviewed proof is:

H. Queffélec and R. Zarouf, *On Bernstein's inequality for polynomials*,
arXiv:1903.10801v1, Theorem 1.1.

The exact primary statement used is the trigonometric Bernstein inequality

```text
||T'||_infinity <= D ||T||_infinity
```

for a trigonometric polynomial of degree at most `D`.  Applying it again to
`T'` gives `||T''||_infinity<=D^2||T||_infinity`.  Under

```text
x=x0+(ell/2) cos(theta),
```

a degree-`D` algebraic polynomial becomes a degree-at-most-`D` trigonometric
polynomial.  On an inner interval where `|sin(theta)|>=sigma`, the chain rule
produces the reviewed nested bound

```text
||P''|| <= 4/ell^2 (D^2/sigma^2 + D/sigma^3) ||P||.
```

Not supplied by that paper are the DPP full-atom expansion, the contrast
response, the adaptive-family obstruction, the low-mode identities, or the
signed cancellation witness.  Those connections are respectively reviewed
packet inputs or proved in this package.
