# A scoped signed payment on the same alternating cylinder

**Author scoped supplement; not a global near-field or entropy-rate sign.**
This explains concretely why the main positive-exception obstruction must
not be confused with an obstruction to signed grouping.

Keep the exact family and interval of PROOF.md. For one complete word Y,
write g_(i,j)(Y_-{i,j}) for the same leave-two conditional curvature as there.
Let the complete word agree with the alternating reference on
I=[-L0,5+L0], including the three sites 0,1,5, with L0=2,020,000. Then

    g_(0,1)(Y_-{0,1}) + g_(0,5)(Y_-{0,5}) < -5.

This is a pointwise statement on a fixed finite cylinder, uniform over every
remaining output and every containing finite Toeplitz block. It is not a
claim that this inequality holds on the complementary cylinder event.

## Proof and exact scalar check

The alternating reference formulas in PROOF.md (11) apply to lag r=1 or 5
by replacing q5 with 1/(r*pi). The new checker encloses both lag-1 and lag-5
functionals on each of the same 200 closed offset cells, with separate full
radius-1/10000 perturbations of q, r and squared off-diagonal for each pair.
It verifies that their sum is below -5 on every such box. The largest upper
endpoint is approximately -5.58037250624. The sign decision is an integer
comparison; the decimal is not a premise.

For the lag-1 reference Schur matrix, let

    E_min = 9999/40000 + (19/20)^2 (7/22)^2 > 1/3.

The rational pi bounds 3<pi<22/7 give

    ||Sstar_lag1||
        <= (761/1600) (1/200 + 3/5) / E_min
         = 11141801/13216832 < 1.

Here 1/4+(19/20)^2/9 < (3/5)^2 checks the square-root bound.
The same residual proof as PROOF.md (13) applies to D={0,1}: outside I,
every distance from either target is greater than L0, so its Hilbert--Schmidt
tail estimate is unchanged. Thus its inverse-block error is at most 202/L0.
The actual and reference Schur norms are at most one, giving the same
conditional diagonal/off-diagonal error. Also the lag-1 reference off-diagonal
has magnitude less than 1/2, from D0<1/2, q1<1/3 and E_min>1/3; the actual
one has magnitude at most c/2. Hence the squared-off-diagonal error is also
at most 202/L0=1/10000. PROOF.md already provides this for lag 5. The exact
two-box scalar check proves the displayed inequality.

Both conditional pair functionals are functions of the same complete word;
the two missing-site sets are not silently identified. The complete cylinder
fixes all required reference outputs for both of them. Its actual probability
is at least 50^(-(2L0+6)). Thus it contributes a strictly positive lower bound
to the expectation of the negative part of this signed grouping. This does
not sign its complete expectation: the complementary event remains unpaid.

## Replay

    python code/verify_signed_reference.py

The checker recomputes every cell, the two individual g bounds, the sum bound,
and the rational Schur constants. No floating finite-volume extrapolation is
used. This supplementary cylinder payment does not replace the main theorem's
precise vanishing-exception obstruction or claim a solution for K_(R,L).
