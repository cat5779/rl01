# Term balance and sign ledger

All logarithms are natural.  The divergence orientation is always
`D(q || nu)`, conditional output law to Fourier Gibbs reference.

## 1. Actual law

On the `l`-slice,

`nu_(n,l)(S)=n^(-l) exp(U_n(S))`, `sum_|S|=l exp(U_n(S))=n^l`.

Let `D_l=D(q_l||nu_(n,l))` and `D_F=sum_l pi_l D_l`.  Then exactly

`H=H(M)+E[M] log n-E U_n(Y)-D_F`.

For half-density projection input,

`E U_n(Y)=(a^2+ac)n log n+c^2 E U_n(X)`.

Therefore

`(E[M] log n)''=0`, `(E U_n(Y))''=2n log n`, and

`H''=H(M)''-2n log n-D_F''`.

The aggregate reference curvature is

`D_F''=sum_l (pi_l D_l''+2 pi_l' D_l'+pi_l'' D_l)`,

where

`D_l'=sum_S q_l' log(q_l/nu_l)`,

`D_l''=sum_S q_l'' log(q_l/nu_l)+sum_S (q_l')^2/q_l`.

The second summand is conditional Fisher and is nonnegative; the acceleration /
cross-entropy summand has no automatic sign.  Neither moving-weight term may be
discarded.

## 2. Mean-overlap surrogate

Define

`Delta_n=sum_l pi_l(E_qtilde_l U_n-E_q_l U_n)`.

Its exact second response, with `g_l(z)=alpha_l(lambda_l^(2-2/n)-theta_l)`, is

`Delta_n''=V_n sum_l [pi_l'' g_l+2 pi_l' z' g_(l,z)
 +pi_l((z')^2 g_(l,zz)+z'' g_(l,z))]`.

Thus

`Htilde''=H(M)''-2n log n-Delta_n''-Dtilde_F''`.

This round proves:

- `Delta_n=C log n+o(log n)` on compact interiors;
- `Delta_n''(a_*+u/sqrt n)~ -K_c(u) sqrt(n) log n`;
- the weak/integrated second response is `log n` times the distributional
  curvature of `C`.

No sign is inferred from `Delta_n>0` alone.

## 3. Potential-clock corrected surrogate

The corrected layer law is

`qhat_l=u_l exp(tauhat_l L_l) r_l^max`,

`tauhat_l=-log(theta_l)/gamma_(2,l)`.

It satisfies `E_qhat_l U_n=E_q_l U_n` layer by layer, so

`Hhat''=H(M)''-2n log n-Dhat_F''`.

The potential defect is exactly absent, but

`Dhat_F''=sum_l [pi_l Dhat_l''+2 pi_l' Dhat_l'+pi_l''Dhat_l]`

is entirely live.  In transport language it includes:

- conditional Fisher / metric Hessian;
- covariant acceleration / cross-entropy response;
- score–layer interaction `2 pi_l' Dhat_l'`;
- layer acceleration `pi_l'' Dhat_l`;
- count entropy curvature already isolated in `H(M)''`.

The rearrangement `Dhat_F'' >= H(M)''-2n log n` would merely restate the desired
entropy sign and is not used as a lemma.

## 4. Scales established this round

| Quantity | Proved scale on compact interiors |
|---|---:|
| `V_n` | `n(1/4 log n-kappa+o(1))` |
| aggregate multiplier `A_n` | `4C/n+o(1/n)` |
| `Delta_n` | `C log n+o(log n)` |
| fixed-chord / weak defect response | `O(log n)` with exact leading `C` |
| midpoint `Delta_n''` | `-K_c(0) sqrt(n) log n(1+o(1))` |
| mean-clock vs potential-clock expected Hamming distance | `O(1)` |
| mean-clock vs potential-clock entropy value | `O(log n)` |
| actual vs potential-clock expected Hamming distance | `O(sqrt n)` |
| actual vs potential-clock entropy value | `O(sqrt n log n)` |
| corrected KL/moving-layer curvature | **unpaid** |
