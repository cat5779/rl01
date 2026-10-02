# R17 G11 independent audit

STATUS: PARTIAL_PASS

The author correctly reports `INCOMPLETE`.  The response neither proves the
commuting-class selector theorem `(COM)` nor gives a selector-independent
counterexample.  The restricted and repair lemmas below are reusable, subject
to the scope statements recorded here.  Nothing in this audit upgrades the
full commuting class to solved.

## 1. Signed endpoint current: certified

Let `P=vv*`, `lambda=tr(KP)`, `A=K-lambda P`,
`mu_0=p_A`, and `mu_1=p_{A+P}`.  Rank-one affinity gives

`p_K=(1-lambda)mu_0+lambda mu_1` and
`b_{K,P}=mu_1-mu_0`.

The inverse bound in (4) is correct.  Writing
`M_S=(K-I/2)+(I/2-D_{S^c})`, the second summand has smallest singular value
`1/2` and the first has operator norm at most `1/2-epsilon`; hence
`s_min(M_S)>=epsilon` even though the summands need not commute.

For

`J(S,i)=-p_K(S) Re (P M_S^{-1})_{ii}`,

the determinant derivative gives (6).  If `w^S=M_S^{-1}v`, the rank-one
update `M_{S union {i}}=M_S+e_i e_i*` gives (7).  Consequently the incoming
minus outgoing current at `S` is

`p_K(S) Re <v,w^S> = b_{K,P}(S)`.

Commutation is used exactly where claimed: multiplying
`Kw^S-D_{S^c}w^S=v` by `v*` gives

`sum_{i notin S} conjugate(v_i) w_i^S=lambda <v,w^S>-1`.

This yields the exact signed endpoint marginals (8), total signed mass one,
and not merely the divergence equation.  Complex conjugations and the sign of
the determinant update are consistent.

The incident-edge estimate (9) is also correct: after using (7), its two sums
combine over all coordinates and are bounded by
`p_K(S) ||v||_2 ||w^S||_2 <= p_K(S)/epsilon`.  Summing over vertices counts
each edge twice, so the stated weaker consequence `||J||_1<=1/epsilon` is
valid.

Finally, the stability calculation (12) is valid.  The probability-factor
term costs at most
`epsilon^{-1} ||p_K-p_L||_1`, the inverse term at most
`epsilon^{-2}||K-L||_1`, and the projector term at most
`epsilon^{-1}||P-Q||_1`.  Integrating rank-one spectral directions along the
gapped segment gives the quoted, nonoptimal
`||p_K-p_L||_1 <= (2/epsilon)||K-L||_1`.  Thus the displayed constants in
(12) are safe and dimension-free.

Certified scope: an explicit Borel, permutation-covariant, dimension-free
Lipschitz **signed** endpoint current.  It is not a positive selector.

## 2. Positive-part capacity theorem: certified

The Fock-space construction is sound.  Exterior creation by the unit vector
`v` satisfies the CAR identities, `U=C+C*` is a self-adjoint unitary, and
`N=CC*` is marked-mode occupation.  Since `[K,P]=0`, the Gaussian density

`rho=det(I-K) Gamma(K(I-K)^{-1})`

commutes with `N`; hence `rho_0=(I-N)rho/(1-lambda)` is genuinely positive and
has trace one.  Its diagonal is `mu_0`, while the diagonal of
`C rho_0 C*` is `mu_1`.

For

`q(S,T)=Re[U_{T,S}(rho_0 U*)_{S,T}]`,

summing over `T` and over `S` gives the two diagonals above.  Because
`rho_0 C=0` and `rho_0` preserves particle number, `q` is supported only on
upward one-point edges.  The exterior signs cancel in the cofactor expansion.
Together with

`M_T=(I-K)(L D_T-D_{T^c})`

and `(I-K)^{-1}v=v/(1-lambda)`, this gives
`q(S,S union {i})=J(S,i)`.  No eigenvector phase enters the result.

The cut inequality has the correct direction.  For arbitrary source family
`A` and target family `B`, put `R=R_A` and
`Q=U*(I-R_B)U`.  The identity

`RQ+QR-(R+Q-I)=(R+Q-I)^2 >= 0`

implies

`mu_0(A)-mu_1(B) <= 2 sum_{S in A,T notin B} q(S,T)`.

Replacing the signed sum by the positive parts gives precisely every
source/target cut inequality for the bipartite transportation network with
capacities `2 J_+`.  These are necessary and sufficient max-flow cuts, so a
nonnegative endpoint coupling `0<=f<=2J_+` exists.  Equations (19)--(21) then
follow; in particular
`sum 2J_+=sum J+||J||_1=1+||J||_1`.

Certified scope: every commuting pair has a nonempty positive endpoint fiber
dominated by an explicitly and dimension-freely stable capacity vector.  The
least-Euclidean-norm choice from (22) is Borel and permutation-covariant for
each fixed `E` (fixed-normal Hoffman continuity suffices), but the response
correctly does **not** establish a dimension-independent Lipschitz constant
for this choice.

## 3. Fixed-projector repair: certified, with one compressed corollary

For fixed `P`, both kernels reduce on `H=v^perp` to gapped contractions `B`
and `B'`.  The noncommutative derivative formula (24) is correct.  If
`L=B(I-B)^{-1}`, then

`dot L=(I-B)^{-1} dot B (I-B)^{-1}`

and

`L^{-1/2} dot L L^{-1/2}
 =[B(I-B)]^{-1/2} dot B [B(I-B)]^{-1/2}=M`.

Sandwiching the derivative of each exterior power produces `dGamma(M)`, and
the determinant factor contributes `-tr(BM)I`.  This is a congruence
derivative, not a commutative logarithmic derivative; no commutativity of `B`
and `B'-B` is being assumed.

The spectrum of `dGamma(M)` consists of subset sums of the eigenvalues of
`M`.  For any positive contraction `B`, `tr(BM)` lies between the sum of the
negative eigenvalues and the sum of the positive eigenvalues.  Therefore the
relative derivative has operator norm at most `||M||_1`, and

`||M||_1 <= ||B-B'||_1/[epsilon(1-epsilon)]`.

Congruence gives `-D sigma_t <= dot sigma_t <= D sigma_t`; multiplying by
scalar exponentials and integrating in Loewner order yields (25).  There is no
missing time-ordering or commutativity assumption here.

The residual-state Hall argument is also correct.  For a marked-empty vector,
`C` is isometric.  After deleting a family `A`, only contractivity of `C` is
needed to obtain

`||(I-R_{N(A)})C psi|| <= ||(I-R_A)psi||`.

Taking complements gives the weighted Hall inequalities.  Averaging over a
number-sector decomposition of the positive residual operator is legitimate.
Thus `tau=sigma_{B'}-e^{-D}sigma_B` has an upward one-point coupling, and
`g=e^{-D}f+h` proves (23), including the factor two.

The last sentence of section 4.3 compresses the pathwise-selection argument.
It is valid after spelling it out: choose compatible repairs on dyadic grids,
linearly interpolate only for compactness, take an Arzela--Ascoli/diagonal
subsequence, and use mesh size tending to zero plus closedness of the fiber
graph to recover feasibility at every time.  It remains only a selection along
one fixed-`P` segment; it gives no consistency between segments and no control
when `P` varies.

## 4. Scalar-complement subclass: certified

For `K=a(I-P)+lambda P`, rank-one affinity along `aI+tP` makes
`b_{K,P}=b_{aI,P}`.  The formula

`F(S,i)=P_{ii} a^{|S|}(1-a)^{n-1-|S|}`

is nonnegative, has total mass `sum_i P_{ii}=1`, and has the correct
divergence.  Its outgoing marginal is exactly `p_{a(I-P)}`, so the endpoint
mixture gives the stronger capacity `p_K/epsilon`.

For different projectors the diagonal variation obeys
`sum_i |P_{ii}-Q_{ii}|<=||P-Q||_1`; coupling the remaining `n-1` Bernoulli
coordinates costs at most `2(n-1)|a-c|`.  The identity

`(n-1)a=tr K-tr(KP)`

and trace-norm duality give

`(n-1)|a-c|<=2||K-L||_1+||P-Q||_1`.

Hence (29) is correct.  The `n=1` boundary, the degeneration `a=lambda`, full
coordinate support of `P`, Borel dependence, and permutation covariance are
all covered.

Certified scope: a genuine dimension-free positive selector on the proper
scalar-complement subclass only.  It does not cover a general commuting pair.

## 5. Finite-consistency equivalence: certified

Necessity of (30) is immediate from a global selector.  Conversely, enumerate
a countable dense subset of the fixed-`E` commuting domain.  Apply (30) to
longer finite prefixes and use a diagonal subsequence in the compact flow
simplex.  Every pairwise inequality survives, giving a Lipschitz assignment on
the dense subset.  It extends uniquely to the whole domain, and the closed
graph of the flow fiber preserves feasibility.

Averaging over the finite coordinate-permutation group preserves feasibility
because each fiber is convex and the fiber family is equivariant.  The group
acts isometrically, so the same Lipschitz constant is retained.  This proves
the claimed equivalence.

This equivalence is a reformulation of the unsolved global-consistency step,
not a proof of it.  Pairwise repair for fixed `P`, stable capacities, or
nonempty fibers do not imply simultaneous finite consistency when the
projectors vary.

## Final certification ledger

- `CERTIFIED`: endpoint reduction and signed-current divergence, endpoint
  marginals, absolute bound, and dimension-free stability.
- `CERTIFIED`: positive-part capacity theorem, including the Fock
  representation and the complete family of max-flow cuts.
- `CERTIFIED`: fixed-projector directed repair estimate (23), Gaussian
  Loewner comparison, and residual-state Hall coupling.
- `CERTIFIED_WITH_EXPLICIT_COMPLETION`: existence of a Lipschitz selection
  along each single fixed-`P` affine segment.
- `CERTIFIED`: scalar-complement selector (27)--(29).
- `CERTIFIED`: finite-consistency is equivalent to the fixed-`E` global
  Lipschitz selector problem.
- `NOT_CERTIFIED / STILL OPEN HERE`: the dimension-free Lipschitz modulus for
  the positive selector (22), finite consistency for varying projectors, the
  full commuting-class theorem `(COM)`, and any selector-independent
  disproof.
- `OUT_OF_SCOPE`: unrestricted noncommuting kernels, exact JO, and any strong
  or factor process construction.

Overall, the response contains several valid and potentially useful partial
theorems, but its own `INCOMPLETE` verdict is the only admissible verdict for
the frozen commuting-class target.


