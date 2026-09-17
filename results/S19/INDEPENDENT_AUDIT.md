# Independent audit — S19 / PR115

## Verdict

**STATUS: CORRECT within the frozen route-obstruction scope.**  The accepted
claim is a positive-density obstruction to an `o(n)` allowance for the
positive exceptions of the existing combined two-budget comparison.  It is
not a counterexample to sine entropy concavity and does not sign the complete
near field.

## Load-bearing checks

1. The infinite alternating operator is used only as a deterministic
   reference.  With `S=2P-I` and parity `J`, the relations `S^2=J^2=I` and
   `JS=-SJ` give the displayed inverse pencil exactly.  No finite Toeplitz
   compression is treated as a projection.
2. For a finite word agreeing with the reference on the fixed cylinder, the
   residual identity pays both arbitrary output changes outside the cylinder
   and the compression boundary.  The uniform inverse norm is justified by
   the signed Hermitian-part argument, and the Fourier tail gives
   `||(G_y)_DD-(G_*)_DD|| <= 202/L`.
3. The two-by-two inverse identity transfers this to the conditional output
   kernel.  At `L0=2,020,000`, the diagonal entries and squared off-diagonal
   all lie in the full radius-`1/10000` box used by the certificate.
4. The 200 closed rational cells cover all
   `a in [1/50,3/100]`.  Outward dyadic arithmetic verifies positive atoms,
   valid reverse-Bayes denominators, and `g-2W>1/12` throughout every enlarged
   cell.  The minimum certified lower numerator is
   `114746766939865001106342296761429388` on the `2^120` grid.
5. On this event `W>=0` and `g>0`, so
   `(g_+-gamma W)_+ >= g-2W > 1/12` for every `gamma<=2`.  This is the required
   positive-part and expectation direction; it does not replace a signed
   expectation by its positive part.
6. The prescribed output pattern has `2L0+4=4,040,004` sites after removing
   the target pair.  Conditioning on the latent input gives true probability
   at least `50^-4040004`.  Translating the cylinder and summing expectations
   uses only linearity, so overlapping cylinders require no independence.
7. The same finite-block argument gives the exact S7 local-table claim for
   every `L>=L0`.  The lower bound is tiny but fixed, hence it defeats `o(n)`;
   it does not provide an effective curvature margin.

The signed supplement was checked separately.  The lag-1 and lag-5 boxes give
`g_(0,1)+g_(0,5)<-5` on the specified complete cylinder.  This is a pointwise
signed payment on that cylinder only; the complementary event and the full
expectation remain unpaid.

## Executed verification

All five delivered checks passed with the configured Python runtime.  The
three certificate programs also passed under `python -O`.  Source SHA256
values matched the compact author receipt:

- `verify_reference_payment.py`: `90ade3b00c775c9accdc6c2a41a8ede4726e4d4bb5a779c3fe9e2b033c0c11c0`
- `verify_analytic_constants.py`: `8dc3e1ba2e92d3c08ccf84352aa31c454e0ffe9bd370d084faeb71ef2393d70e`
- `verify_signed_reference.py`: `af95473861e10ebcd59a3fe53813fbcc1ec0f6e0db4b8b87ff308137e9af76ae`

No novelty review or second mathematical review was performed.

