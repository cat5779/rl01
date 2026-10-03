PASS

# Independent counterexample/algebra audit of `source.md`

I audited the frozen statement in `task.md` against the construction in
`source.md`, without using any other audit.  I found no counterexample and no
load-bearing algebraic or quantifier gap.  The proposed selector proves the
restricted theorem, with
\[
C_\varepsilon^{(2)}=
\max\left\{18,\;2+(6+4/\varepsilon)
\left[1+\left(\frac{1-2\varepsilon}{2\varepsilon}\right)^2\right]\right\}.
\]

## 1. Exact conditioning and stability

The exact-pattern identity (3) is correct.  Partitioning the determinant for
`J,O` gives
\[
\det(K-D_{E\setminus(T\cup A)})
=\det B_T(K)\det(M_T(K)-D_{J\setminus A}),
\]
and the three parity signs multiply correctly, so (6) holds for every outside
pattern, not merely almost surely.  The decomposition
\[
B_T=(K_O-\tfrac12I)+(\tfrac12I-D_{O\setminus T})
\]
has a second term with all singular values `1/2`; hence the gap gives
`s_min(B_T)>=epsilon`.  Thus every outside pattern has positive probability and
all inverses used in the construction are defined.

The occupied/absent one-coordinate Schur complements preserve both endpoints
of the spectral gap.  Iterating them is associative and yields exactly the
block Schur complement in (4), so (7) covers arbitrary `T`, including mixed
occupied/absent patterns.  Differentiating the Schur complement really gives
\[
\dot M_T=[I,-K_{JO}B_T^{-1}](L-K)[I,-K_{JO}B_T^{-1}]^*.
\]
The claimed bound on this row operator is dimension-free.  Consequently (8)
is valid pointwise; its probability-averaged form follows without a factor
equal to the number of patterns.

## 2. Two-site algebra and all degeneracies

For the four local probabilities, direct differentiation gives exactly
\[
(\gamma-1,u-\gamma,t-\gamma,\gamma).
\]
Substitution into (12) verifies all four divergences and total edge mass one.
The interval in (13) is precisely the conjunction of the four edge
nonnegativity inequalities and the two nontrivial singleton capacity
inequalities.  The additional inequalities in (14) follow from the valid
kernel `M+epsilon R`, while
\(p_1+p_2\ge\varepsilon\) supplies the only remaining cross-inequality.
Thus the interval is nonempty and the stronger `p_M/epsilon` outgoing bound is
proved.

The clipping rule is compatible with the transposition of the two sites:
`ell' = gamma-U`, `U' = gamma-ell`, `x0' = gamma-x0`, hence `x'=gamma-x`.
The boundary projectors are not merely limiting cases: for `R=E_1` the
interval collapses to `x=d`, and for `R=E_2` it collapses to `x=0`.  Therefore
there is no phase choice, zero-entry ambiguity, or discontinuity when a
two-coordinate projector degenerates to a coordinate projector.

## 3. Lipschitz constants and simultaneous perturbations

For rank-one projectors on two sites, `R-Q` is traceless Hermitian and has
operator norm `||R-Q||_1/2`.  The estimates for `u,t,gamma,x0`, the endpoints,
and clipping therefore give (18) with coefficients
`6+4/epsilon` and `9`.  Max/min/clipping are used with their sup-norm
Lipschitz property, so no unrecorded sum of endpoint errors occurs.

For simultaneous changes of both kernel and direction, the product split in
(24) is exact: the outside-law term costs `||q_K-q_L||_1`, and the conditional
term is averaged against the probability vector `q_K`.  Pointwise stability
of `M_T` then gives the coefficient `d_epsilon`; there is no mixed error and no
dimension-dependent factor.  Compression of `K-L` and of `P-Q` does not
increase trace norm.

## 4. Exhaustion of support configurations

All pairs allowed by the theorem fall into the proof's cases:

1. If the union of supports has at most two coordinates, both selectors can be
   represented using the same auxiliary two-set.  Uniqueness of the coordinate
   flow, proved from the directional-mass identity (23), makes this independent
   of the auxiliary coordinate.
2. If the supports are disjoint, `PQ=0`, hence `||P-Q||_1=2`; two nonnegative
   unit flows are automatically at distance at most two.  This remains valid
   when both `K` and `L` change.
3. If two genuine two-coordinate supports meet in one coordinate `i`, writing
   `alpha=1-P_ii` and `beta=1-Q_ii` gives
   \[
   \|P-Q\|_1=2\sqrt{\alpha+\beta-\alpha\beta}.
   \]
   Each of `||P-E_i||_1` and `||Q-E_i||_1` is at most `||P-Q||_1`, so the
   triangle comparison through the unique coordinate flow yields (27).

The apparently omitted mixed case (one coordinate support versus a genuine
two-coordinate support) is already in case 1 when the coordinate lies in the
two-set, and in case 2 otherwise.  Thus there is no support-switching hole.

## 5. Covariance, measurability, and theorem scope

On each support stratum, all operations are continuous because the inverses
are uniformly separated from singularity.  The global estimates (24)--(27)
also control convergence between strata, so the selector is continuous, hence
Borel, on the full restricted domain for each finite `E`.  An arbitrary
coordinate permutation restricts on the active two-set to either the identity
or the checked transposition; outside conditioning and exact probabilities
commute with the same relabeling.  This proves permutation covariance.

The construction uses the projector matrix `P` itself and never a representing
vector, so vector phase is irrelevant.  The constants depend only on
`epsilon`; no minimum atom probability or ambient dimension enters.  Finally,
the proof stays on `|supp(P)|<=2` and does not silently claim the unrestricted
full-support theorem.

Verdict: the proof meets all eight requirements of the frozen restricted
theorem.  No small-dimensional exact counterexample arises from support
switching, common/disjoint supports, phases, degeneration, simultaneous
`K/L` perturbation, edge-coordinate embedding, covariance, or the claimed
dimension-free constants.
