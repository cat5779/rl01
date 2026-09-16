PROVED_SCOPED_LEMMA

# Reviewed definitions, accepted units, and quarantined upload

This is an integration scope record, not a reconstruction of the missing
author proof. All entropies are complete-configuration Shannon entropies.
The full sine entropy-rate concavity problem remains unresolved.

## Accepted finite-radius theorem

Let `E=[-1/4,1/4]`, `f_(a,3)=a+c(F_3*1_E)`, `37/40<=c<=1`,
`0<=a<=1-c`, and `f_(a,3,s)=1/2+exp(-s)(f_(a,3)-1/2)`.
For the seven-site window `[-3,3]`, put

`phi(q)=(q-1/2) log(q/(1-q))`,
`I_3(f)=E_f phi(Pr_f(Y_0=1 | Y_[-3,3] excluding 0))`,
`J_3(a)=log 2-int_0^(log 4) I_3(f_(a,3,s)) ds`.

The separately complete [proof](FULL_R3_PRODUCTION.md) and independently
reconstructed rational cover establish `partial_a^2 I_3>=6 exp(-2s)` and
`J_3''<=-45/16`. Its untruncated finite-radius functional has curvature `<=-3`.
At `c=1`, the original legal shift domain is a singleton; the derivative uses
the stated legal auxiliary kernel extension and implies only vacuous chords.
No assertion identifies J_3 with H_7/7 or with the entropy rate.

## Exact finite-atom interface used in the accepted proof

For an output word y, `p_y=(-1)^(number of zero coordinates) det(K-diag(1-y))`.
The auxiliary kernel is `K(v,z)=I/2+v(B+zI)`, where B has lag-one entry
`45/192`, lag-three entry `-5/192`, and other entries zero. The exact integer
polynomials generated in `code/atom_polynomials.py` have the form

`p_y(v,z)=192^(-7) sum_(0<=l<=k<=7) C_(y,k,l) v^k z^l`.

The independent atom/jet and scaled-jet checks verify all coefficients and
the actual first and second derivative layers, including v=0. These are the
polynomials referred to as equation (17) in the original proof text.
For a center pair with atom masses x,y, its complete weighted production is
`F(x,y)=(y-x)log(y/x)/2`. Its exact second derivative is

`F''=(x+y)(x'/x-y'/y)^2/2`
`    +(log(x/y)+1-y/x)x''/2 +(log(y/x)+1-x/y)y''/2`.

This retains all weight and acceleration terms. The scaled version and all
64 center pairs are used by the accepted cover; no atomwise sign is assumed.

## Additional accepted finite certificates

At `c=5*pi/16`, `a=(1-c)/2+delta`, `|delta|<=1/10000`, radius3, and the
assigned time interval `[0,log4]`, the independently rebuilt 2048-cell cover
gives negative integrated curvature of the paired exterior-count layers 1+5
and positive curvature of the full production integral. The complete H_7
curvature on the same delta interval is strictly negative. Exact rational
enclosures are in `reviewed/aligned_full_rebuilt.json` and
`reviewed/finite_entropy_rebuilt.json`. These are route tests, not a rate
counterexample. Their rebuilt data include all complete atoms and derivatives.

## Not accepted from this upload

Theorem A's claimed negative count-band bound for every odd R>=160001,
Theorem B and dependent signed-layer limits, and the advertised open-density
and growing circular extensions await an intact proof.
The corrupted author proof is not part of this public packet. No inferred
replacement proof is accepted. See INDEPENDENT_AUDIT.md for the missing-proof boundary.
