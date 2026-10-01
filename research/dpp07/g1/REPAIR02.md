# Directed repair of the common iid coupling proof

STATUS: PROVED — revised proof candidate; fresh full verification required.

The replacement manuscript is `proof02.md`. The frozen mathematical statement is unchanged: one fixed equivariant complex Hermitian positive contraction on the regular orbit of an arbitrary countable group; the Bernoulli parameter is its Fuglede–Kadison determinant; both output configurations come from one regular iid source; the map is total Borel and equivariant on every input; H is permitted only when the determinant is zero.

## 1. The joint Poisson completion gap

**Input:** `REVIEW01.md`, Critical gap 1, concerning the old proof's Section 4.

Coordinate compensators do not imply independent Poisson coordinates. In particular, repeating one Poisson process at two sites has the right individual compensators and the wrong joint jump law. The replacement proof does not use the claimed completion theorem or attempt to infer a joint Poisson law from coordinate intensities.

**Replacement:** `proof02.md`, Section 6, begins with an independent Bernoulli field and independent sitewise Poisson random measures. Picard iteration is performed directly on this space. The covariant mean sensitivity bound gives summable factorial bounds for whole-coordinate-path disagreements. Compact-time stabilization produces the strong graphical solution, and an additional compensation/dominated-convergence argument proves the fixed-point equation. This avoids relying on unproved preservation of an acceptance inequality under a threshold limit.

The conditional independence of the noise from the initial field is part of its construction. No weak process is first constructed and subsequently equipped with noise.

## 2. The finite-chain comparison gap

**Input:** `REVIEW01.md`, Critical gap 2, concerning the old equations (22)–(24).

**Replacement:** Sections 7–8 explicitly construct four processes on one space: the strong solution, the lower and upper cross-dependent envelopes, and the finite conditional chain. The conditional chain uses the same restricted Bernoulli field and the same site proposals. Its finite forward equation identifies its one-time law exactly with the desired marginal.

The comparison is proved by tracing a proposed order violation backwards through the finite dependency neighborhood. Each interior violation requires a strictly earlier local violation. An infinite chain has probability zero by the factorial-moment bound (23). For a finite conditional chain, the tracing can terminate at its dependency boundary; (30) retains this error explicitly.

The resulting estimate is
\[
\|\mathcal L(Z_s|_{B_0})-\nu_s|_{B_0}\|_{\rm TV}
\le |B_0|p_n(S)+\varepsilon_{F,n,B_0}(S).
\]
The limit order is fixed: first hold the dependency range, test sites, and horizon fixed and exhaust the group by finite sets; then increase the dependency range. This proves the one-time marginals of the already constructed strong solution. The argument uses cross-dependent envelopes and does not assume attractiveness of decreasing birth rates.

## 3. The weak-limit martingale gap

**Input:** `REVIEW01.md`, Critical gap 2, concerning the old equation (25) and the following martingale-limit sentence.

**Replacement:** The weak-limit passage is removed in full. Thus there is no unproved transfer of martingale identities against historical tests, no undeclared path topology for a weak limit, and no need to infer the absence of simultaneous jumps after weak convergence. All processes used in the replacement argument are directly driven by the original independent proposals. The factorial chain argument explicitly uses their absence of simultaneous proposal times, proved by countability and diffuse Poisson times.

## 4. Other expansions of the argument

The replacement is a complete manuscript rather than a patch. In addition to the three repairs above it writes out the following points.

- **Strict spectral upper gap:** The FK bound gives a strict upper gap at positive path time even when the original kernel has norm one. Equality would force spectral distribution concentrated at one and hence the excluded case (p=1).
- **Full exterior conditional version:** The finite compressed kernels are extended with a fixed gapped scalar; strong convergence, uniformly bounded inverses, the shorting formula, and martingale convergence identify the canonical continuous conditional odds.
- **Source occupancy:** Vacant-site rates and full rates are distinguished. The transport matrix includes the source-site diagonal term where exactly one source is occupied.
- **Mass transport:** The incoming/outgoing identity is written for the regular countable group action; no invariant mean or amenability assumption is used.
- **Scalar entrance:** The norm expansion, the zero diagonal of the first-order term, uniform shorting estimate, and cancellation of the first two powers are all displayed. The time-changed rates and sensitivity constant are (O(s)), including uniformly over exterior configurations.
- **One path on all compact horizons:** The same global Poisson field and the same Picard iterates are used on ([0,1)). Compact restrictions agree by construction.
- **Endpoint without a gap:** The final configuration is an increasing union. Convergence of finite inclusion probabilities identifies its DPP law without constructing a rate at the singular endpoint.
- **All-input map:** A total sitewise noise decoder, a countable Borel stabilization/fixed-point event, and an invariant fallback are specified. The output inclusion holds even on exceptional inputs.
- **Boundary cases:** H is used exactly at (p=0). The (p=1) branch follows from faithfulness and is deterministic.

The original algebraic claims (1)–(18) and entrance/endpoint claims (26)–(27) have been rederived in the new numbering. The old finite-flow claims (19)–(24) are replaced by the quantified construction in Sections 6–8. The old weak-compensator equation (25) is no longer used. No premise has been strengthened and no group or kernel subclass has been substituted.

## 5. Verification boundary and remaining work

The author of this revision considers the stated proof chain complete and reports a **proof candidate**, not an independent correctness certificate. The whole replacement manuscript needs a fresh full review, particularly its Picard fixed-point passage, backward-chain comparison with nonlocal middle dynamics, finite forward-law identification, and totalization. A failure in any of those steps must be resolved before upgrading the proof's reviewed status.

No formal proof of the infinite-dimensional probability construction has been produced. No new literature search or novelty conclusion is part of this repair. The prior manuscript and its adverse audit remain separate evidence and are not overwritten.
