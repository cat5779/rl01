# Audit of the paid mesoscopic response bridge

## Result of the audit

No defect was found in the stated fixed-interior bridge. The audit is internal, not an external review. The valid conclusion is only

\[
F_{Q_n}''(a,c)=G_{n,m}''(a,c)+o(n)
\]

uniformly on each fixed interior interval, with the explicit rate in the inherited proof. It does not sign `G''`.

## Checklist

### 1. Full-law mixture identity

For `X~DPP(Q)` and the coordinate channel `Pr(Y_i=1|X_i)=a+cX_i`, all inclusion probabilities of `Y` equal `det(aI+cQ)_A`. Inclusion-exclusion therefore gives equality of the full configuration laws, not merely the count laws.

### 2. Conditional laws and legal direction

Every intermediate kernel is obtained by conditioning the latent input `X`, never by conditioning the observed output. The latent branch weights are independent of `a`. Restricting the conditional remaining kernel to the current block gives a contraction `Q_j^u`, and the local output kernel is exactly `aI+cQ_j^u`; its speed is the legal identity matrix.

### 3. Telescoping multiplicities

At each node,

\[
H(Y_B,Y_C)=H(Y_B)+H(Y_C|X_B)+I(X_B;Y_C|Y_B).
\]

Every nonroot remaining entropy occurs once as a child term and once as the next node's parent term with the same global latent probability. Each local block entropy occurs once. The total remainder is one sum of conditional mutual informations; no diagonal Fisher term is repeated across overlapping pairs.

### 4. Independent value budget

The boundary spectral entropy enters only after proving

\[
I(X_B;Y_C|Y_B)\le I(X_B;X_C)\le Tr b(Q_B).
\]

The contraction case is obtained by a projection dilation whose coordinate marginal is the original complete DPP law. The matrix martingale and trace-entropy concavity give

\[
\sum_u Pr(u)Tr b(Q_j^u)\le Tr b(Q_{B_j}).
\]

### 5. Atom invertibility on the enlarged interval

On `I=[eta/2,1-c-eta/2]`, every singular value of

\[
A_S=aI+cQ-D_{S^c}
\]

lies in `[delta,1-delta]`, `delta=eta/2`. This follows from writing `A_S=(aI+cQ-I/2)+(I/2-D_{S^c})`; the first summand has norm at most `1/2-delta`, and the second has all singular values `1/2`.

### 6. Moving weights are included

The Chebyshev order-`h` term is a polynomial of total degree at most `2h` in `(a,1_S)`. A monomial `a^r prod_{i in V}1_{i in S}` has `r+|V|<=2h`. Its expectation is

\[
a^r det(aI+cQ)_V,
\]

still of degree at most `2h`. Thus the complete atom weights move inside the polynomial response; neither `p''` nor the Fisher term is discarded.

### 7. Constant cancellation

The normalized entropy expansion has the same constant `C_delta` for every contraction. The root dimension is `n`, while the latent-weighted sum of local block dimensions is also exactly `n`. Therefore the constant cancels before differentiation. This is the source of the coefficient budget `2r^h/h`, with no tree-node factor.

### 8. Derivative and tail constants

The low-degree truncation is controlled by an elementary Chebyshev derivative estimate on the smaller interval `I'`. The tail is differentiated term by term under an absolutely summable `h^2r^h` majorant. The exact geometric tails are displayed in `proof.md`; all constants are dimension-free.

### 9. True sine blocks

For a contiguous block of length `m`, the Toeplitz trace defect is

\[
Tr(Q_m-Q_m^2)\le {2\over\pi^2}(\log m+3).
\]

Together with `Tr b(Q_m)<=2 sqrt(m Tr(Q_m-Q_m^2))`, this yields the inherited boundary budget. It is applied directly to the original contraction root, not by differentiating a spectral-mixture value approximation.

## Exact limitation

The bridge pays only

\[
E_{n,m}=F_{Q_n}-G_{n,m}.
\]

The term

\[
G_{n,m}''=\sum_j E_u F_{(Q_n^u)_{B_j}}''
\]

can still be extensive and of unknown sign. Nothing in the response argument bounds it.
