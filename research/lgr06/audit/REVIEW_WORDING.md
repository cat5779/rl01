# Independent word-gap audit of the prescribed-W DPP proof

STATUS: CORRECT

## Scope and independence disclosure

## Verdict

The proof establishes the frozen statement with the stated quantifiers. I found
no critical gap in the definitions, endpoint cases, measurability, filtration
argument, all-input construction, or final law identification. In particular,
the result is not inferred from a limit in distribution: the proof constructs all
thresholded approximants from one iid Brownian field and obtains coordinatewise
eventual equality with the target DPP in an auxiliary coupling.

## Word and quantifier risk table

| Risk word or phrase | Exact location | Audit and reproducible reason | Result |
|---|---:|---|---|
| **countable** includes finite and empty | theorem 3–5; proof 12–16 | The empty case is explicitly assigned the unique map. All later arguments also work for finite `W`; finite products and finite component collections need no infinitude. Countability is used legitimately for standard product Borel structures, countable simultaneous null-set intersections, and product-law identification. | Pass |
| **any action**, including arbitrary stabilizers | theorem 3–5; proof 18, 27–30, 141–148, 184–190, 352–359 | No freeness or orbit representative is chosen. Every object is defined canonically from `Q`, coordinatewise operations, and the action convention. If `gamma` fixes `x`, equivariance gives the required stabilizer invariance at `x`; the argument never assumes a free action. | Pass |
| `Q` **commutes** with permutations versus entrywise invariance | theorem 3; proof 18, 27–30 | For the permutation unitary `U_gamma`, `U_gamma Q=Q U_gamma` implies `Q_{gamma x,gamma y}=Q_{xy}`. Hence absolute thresholds, graph distance balls, finite marginal laws, the drift, Picard iterates, and the threshold outputs transform exactly. No signed action or merely law-invariant substitute is used. | Pass |
| Hermitian **positive contraction**, including eigenvalues 0 and 1 | theorem 3–5; proof 61–99 | The tilt uses `M=I-K+K^(1/2)DK^(1/2)` and proves `M >= min(1,d)I`, with `d>0`. It never inverts `K` or `I-K`. The resulting `P=BM^{-1}B*` is Hermitian and `0<=P<=I`, so deterministic coordinates and singular endpoints are covered. | Pass |
| finite tilt kernel algebra | proof 69–99 | The generating polynomial identity is valid for a finite DPP. Since diagonal `D` and `Z` commute, the numerator is `det(M+B*(Z-I)B)`; Sylvester's determinant identity gives `det(I+(Z-I)BM^{-1}B*)`. This is precisely the DPP generating polynomial with kernel `P`. | Pass |
| complex entries in covariance bound | proof 101–121 | For `x != y`, the two-point determinant gives covariance `-|P_xy|^2`, not a real-square expression. Therefore the absolute row sum is `p(1-p)+(P^2)xx-p^2 <= 2p(1-p) <= 1/2`. This yields the claimed dimension-free sup-norm Lipschitz constant. | Pass |
| support component independent of the **entire complement** | proof 33–57 | `Q` has zero cross-block entries between support components. For any finite cylinder on one component and any finite cylinder in its complement, the determinant splits into the two blocks even when the complement cylinder meets several components. Inclusion-exclusion gives cylinder factorization, and a pi-lambda extension gives independence of the two full sigma-fields. The phrase “grouping” at line 53 is terse but the displayed calculation supplies the needed finite-cylinder proof. | Pass |
| threshold balls finite | proof 22–27 | `sum_y |Q_xy|^2=(Q^2)xx<=1`; each incident threshold edge contributes at least `1/n^2`, so degree is at most `n^2`. A finite-radius ball in a finite-degree graph is finite. | Pass |
| threshold balls nested | proof 22–27 | As `n` increases, the threshold `1/n` decreases and the permitted radius also increases. Thus every path of length at most `n` in `D_n` is a path of length at most `n+1` in `D_{n+1}`. | Pass |
| threshold balls exhaustive | proof 33–37 | Every vertex in `C(x)` is joined by one finite path of nonzero entries. Taking `n` at least the path length and large enough that every one of its finitely many edge moduli is at least `1/n` puts the whole path in `D_n`. | Pass |
| threshold balls equivariant | proof 18, 27–30 | Entrywise invariance preserves each `D_n`, and permutation actions preserve graph distance. Therefore `E_n(gamma x)=gamma E_n(x)` exactly, including stabilizers. | Pass |
| `limsup` rather than a genuine limit | proof 125–148 | Each finite posterior map has the same `1/2` Lipschitz bound on bounded field differences. If `|a_n-c_n|<=d`, then `|limsup a_n-limsup c_n|<=d`; applying this coordinatewise proves (10) without requiring convergence. Along the observation process, the upward martingale theorem later shows the actual limit exists almost surely. | Pass |
| drift defined on **all real fields** | proof 125–148 | Every `E_n(x)` is finite, the exponential sums are finite, and the denominator is strictly positive. Hence no boundedness of `y` is needed for definition. Only comparisons with bounded `y-y'` invoke the sup norm. | Pass |
| unbounded input space versus uniform-in-space Picard convergence | proof 150–190 | Although an iid Brownian field is generally not in `ell-infinity(W)`, successive Picard corrections are uniformly bounded: the first correction is at most `T`, and (10) gives the factorial bound (12). Thus only differences enter the spatial supremum. The summable bound gives uniform convergence in `x` and bounded time for every input path field. | Pass |
| parameter integration and path-space Borelness | proof 150–188 | `C` with compact-open topology is Polish and `C^W` is a countable product. The integrands are bounded jointly Borel; parameter integration is Borel, while indefinite integration in time is continuous. Coordinatewise Picard limits are Borel. Rational-time evaluations generate the Borel sigma-field of `C^W`, establishing Borelness of the solution map. Restricting the same recursion to `[0,T]` establishes measurable causality. | Pass |
| **total**, **causal**, **all inputs** | proof 139, 154–188, 332–359 | The drift is total on every real field, Picard iteration is assigned to every `w in C^W`, and uniqueness is pathwise for each input. The exceptional scalar labels in the Brownian encoder are sent to the zero path, so no undefined null set remains. The output is consequently total and Borel, not merely an almost-sure equivalence class. | Pass |
| every group element and every input | proof 184–190, 352–359 | Drift equivariance is pointwise. Induction gives pointwise equivariance of every Picard iterate, uniform convergence preserves it, and the same scalar encoder is used at every site. No group-dependent conull set is intersected; countability of `Gamma` is therefore more than enough. | Pass |
| endpoint versus full observation history | proof 202–250 | Finite Gaussian Bayes first identifies the endpoint posterior. Brownian bridges are jointly independent of `(eta,B_t)` by finite-dimensional Gaussian covariance and cylinder extension. Since bridges plus endpoints generate the full observation history, the endpoint posterior equals the full-history posterior. Joint measurability plus Fubini handles fixed-time exceptional sets. | Pass |
| innovations are jointly iid Brownian paths | proof 252–328 | The posterior identity makes each coordinate a martingale in one raw filtration; downward conditional-expectation convergence preserves this in one usual augmentation. Finite variation does not change brackets, giving bracket `tI` for every finite vector. Vector Levy, or the displayed conditional characteristic function, gives independent Gaussian increments for every finite coordinate vector. Countability then identifies the full product Wiener law. Pairwise covariance alone is not used. | Pass |
| same-noise strong identification | proof 323–328, 361–380 | The auxiliary observation process solves the deterministic integral equation with innovations `beta`. All-input pathwise uniqueness forces `X=Z(beta)`. Thus feeding a product Wiener field to the Borel solution map yields the exact observation-process law, rather than only a weak subsequential law. | Pass |
| one Uniform encodes one Brownian coordinate, including exceptional inputs | proof 332–350 | Binary digits are split into countably many subsequences; the dyadic convention affects a null set only. The midpoint construction has the correct conditional variance. The union bound in lines 340–347 is summable after multiplication by `2^{-k/2}`, so polygonal refinements converge uniformly on every integer interval almost surely. The convergence set is Borel; assigning the zero path off it makes `Psi` total Borel while preserving Wiener pushforward. | Pass |
| threshold ties and convergence | proof 352–378 | Under the same auxiliary coupling, conditional on either binary value of `eta_x`, threshold error is the corresponding Gaussian tail and ties have probability zero. The errors are summable, so Borel–Cantelli gives eventual equality for each vertex; countability gives simultaneous eventual equality at all vertices, without claiming a common stabilization time. | Pass |
| exact DPP law, not only inclusion marginals | proof 380–393 | Same-noise eventual equality already gives the full target field law. Independently, (28) gives every finite inclusion probability, and (29) applies inclusion-exclusion to every disjoint finite one-set/zero-set pair. These finite cylinder probabilities determine the probability measure on `{0,1}^W`. | Pass |

## External inputs and their conditions

1. **Countable DPP existence and uniqueness.** A Hermitian operator satisfying
   `0<=Q<=I` defines the determinantal inclusion probabilities. Uniqueness follows
   because inclusion-exclusion recovers every finite zero/one cylinder. These are
   exactly the hypotheses present at proof lines 3 and 14–16.
2. **Finite Gaussian Bayes.** It is used only on finite `E_n(x)`, at `t>0`, with
   finitely many binary hypotheses and everywhere positive Gaussian densities
   (lines 202–214). The `t=0` value is handled separately at line 248.
3. **Levy upward theorem.** The sigma-fields generated by the nested finite
   endpoint observations increase to the component endpoint sigma-field, and the
   conditioned variable `eta_x` is bounded (lines 211–216).
4. **Levy downward theorem.** It is applied to the fixed integrable random
   variable `beta_t(x)` along a decreasing, cofinal sequence of completed raw
   sigma-fields. The right sides converge in `L1` by (19) (lines 286–299).
5. **Vector Levy characterization.** Every finite coordinate vector is a
   continuous martingale in the same usual filtration, starts at zero, and has
   bracket `tI` (lines 301–321). These are the full hypotheses needed.
6. **Borel–Cantelli.** Only the first lemma is used, so no independence of the
   time-indexed errors is required; summability is supplied by (26).
7. **Cylinder uniqueness.** Both path and binary-field product spaces have
   countable generating cylinder classes because `W` and the rational times are
   countable. The finite-dimensional identities therefore determine the stated
   product Wiener and DPP laws.

## Boundary attacks

- `W=empty`: the stated unique map has the unique input and output law.
- `Q=0` or `Q=I`: the tilt matrix remains invertible by line 79, the drift is
  respectively zero or one on deterministic coordinates, and the threshold
  limit returns the deterministic DPP.
- Infinite-degree support graph: a row may have infinitely many nonzero entries,
  but every threshold graph has finite degree by (1); exhaustivity uses only one
  finite path at a time.
- Nonfree action with a large stabilizer: no transversal or iid labels indexed by
  the group are introduced. All operations commute with the original permutation
  action on `W`.
- Spatially unbounded Brownian realization: no norm of the realization itself is
  taken; only bounded drift corrections and differences are measured uniformly.
- Failure of the finite posterior sequence to converge on an arbitrary input:
  harmless, because the deterministic drift is defined by limsup and retains the
  required Lipschitz bound. Convergence is needed only under the auxiliary
  observation law, where conditional-expectation convergence supplies it.

## Minor noncritical observations

The prose at proof line 53 (“grouping all components except one together”) could
be expanded because there may be infinitely many complementary components. It
is nevertheless justified by the immediately preceding finite-cylinder
determinant calculation: a complement cylinder meets only finitely many
coordinates, and the two-block split `C` versus `W\C` is exact. This is an
expositional compression, not a missing lemma.

The citation placeholders at proof lines 16, 216, 299, and 306 do not identify
bibliographic items inside the anonymous file. This does not create a proof gap:
the invoked results are standard, their exact hypotheses are visible, and those
hypotheses are checked above. It is a presentation issue if the text is intended
for publication.
