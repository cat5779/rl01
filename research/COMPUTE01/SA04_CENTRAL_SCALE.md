# SA04 central-layer scale diagnostic

**Status: EXPLORATORY / CORRECTED_LAW_ONLY**

This note implements the numerical task in
`results/SA04/COMPUTATION_HANDOFF.md`.  It preserves the report's original
times `s_l` and records the two terms

\[
A_l=F_l(s_l)-F_{l-1}(s_l),\qquad
E_l=F_{l-1}(s_{l-1})-F_{l-1}(s_l)
\]

separately before forming `d_l=A_l-E_l`.  The values below use binary64
arithmetic and are not an interval certificate or an asymptotic theorem.

## Reduction used

For a fixed latent `k`-set `A`, the heat flow of a uniform `l`-subset of `A`
depends only on

\[
R=|S\cap A^c|.
\]

In original time its birth and death rates are

\[
\lambda_R=(l-R)(k-R),\qquad
\mu_R=R(k-l+R).
\]

The code exponentiates this `(l+1)`-state reversible chain.  It then mixes over
the Fourier projection DPP without enumerating latent sets: for each output
set `S`, the coefficients of

\[
\det(I-P_S+zP_S)
\]

give the law of `|A intersect S|`.  Cyclic output-set orbits reduce duplicate
principal-submatrix eigensolves.  Finally, (7.1) is evaluated with exact
`Fraction` coefficients to obtain `B_m` and `w_l=B_{l-1}-B_{l-2}`.

## Central-layer data

| `n` | `A_k` | `E_k` | `d_k` | `sqrt(n)d_k` | `W_n` | `W_n/n^(3/2)` |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 0.156578236 | 0.000224409 | 0.156353827 | 0.382987096 | -3.807993163 | -0.259101117 |
| 8 | 0.251684252 | 0.001088585 | 0.250595667 | 0.708791582 | -10.669975386 | -0.471550747 |
| 10 | 0.337195962 | 0.002908887 | 0.334287074 | 1.057108547 | -21.968807363 | -0.694714687 |
| 12 | 0.412942886 | 0.005889731 | 0.407053156 | 1.410073495 | -38.062840517 | -0.915649634 |
| 14 | 0.479961230 | 0.010155713 | 0.469805517 | 1.757851282 | -59.072052484 | -1.127690722 |
| 16 | 0.539415149 | 0.015773608 | 0.523641541 | 2.094566165 | -84.955861911 | -1.327435342 |
| 18 | 0.592350695 | 0.022767925 | 0.569582770 | 2.416535035 | -115.565866813 | -1.513285335 |
| 20 | 0.639656090 | 0.031131594 | 0.608524496 | 2.721404278 | -150.682781443 | -1.684684712 |

On this finite range, the central difference does not display the proposed
`n^(-1/2)` decay: `sqrt(n)d_k` increases throughout.  The bridge term is much
smaller than the deletion term, so the data also do not show the strong
`A_k-E_k` cancellation in candidate three.  They point toward candidate two
as the next analytic target: seek a non-vanishing central `d_k` limit or a
uniform lower bound on an appropriate central subsequence.

This is evidence for choosing the next lemma, not a proof that the sufficient
`O(n^(-1/2))` condition fails asymptotically and not a proof of the scale or
sign of `W_n`.

## Regression checks

Across `n=6,8,...,20`:

- the largest projection idempotence residual is below `4.1e-16`;
- the largest reconstructed layer-density mean error is below `7.8e-15`;
- exact-Fraction construction gives zero reported `B`-mass error;
- `W_n=-2 sum_l w_l d_l` and the direct `sum_m B_m Delta^2 h(m)` agree to
  at worst `5.7e-14`.

Detailed layer records are in `sa04_central_scale_result.json` (`n<=16`) and
`sa04_central_scale_large_result.json` (`n=18,20`).

