# Independent mathematical audit

STATUS: PASS

## Certified scope

The argument in `RESULT.md` proves the frozen statement in `TASK.md` for a **single fixed** covariant rate field that is uniformly bounded and has a fixed finite interaction range.  It constructs a common-Poisson Harris solution, proves pathwise uniqueness and identifies all of its one-time laws from the cylinder continuity equation.  This audit does **not** certify unbounded rates, infinite-range rates, common-noise convergence for varying approximations, arbitrary Borel nonlocal selectors, a general strong process theorem, general exact JO, or novelty.

## Checks of the load-bearing steps

1. **Finite backward ancestor clusters.**  If a chain ending at a fixed query contains (n+1) potential marks, then after fixing its terminal site there are at most (D^n) possible site sequences, and the factorial moment formula for the (possibly repeatedly used) sitewise Poisson processes gives
   \[
   \frac{M^{n+1}t^{n+1}}{(n+1)!}
   \]
   ordered tuples for each sequence in expectation.  Thus the sum in (1) is finite.  Every mark inserted by the recursive ancestor construction lies on at least one such finite chain, so the number of distinct inserted marks is bounded by the total number of chains and is finite almost surely.  Repeated sites do not invalidate the factorial-moment calculation because the times in a chain are strictly ordered.

2. **One good event for all inputs, sites, and times.**  Since \(\mathcal A(g,t)\subseteq\mathcal A(g,1)\), intersecting over the countable set of sites gives one probability-one Poisson event on which every time query has finite ancestry.  This event is independent of the initial configuration, so the chronological recursion works on it for every \(x\in E\), not merely for almost every \(x\) under \(\mu_0\).  Simplicity at one site and absence of common times for each pair of independent site processes, followed by a countable intersection, correctly give the no-tied-positive-marks event.

3. **Consistency, measurability, and covariance.**  At a mark \((h,s,u)\), the recursion has already included all earlier marks at every site of \(B_R(h)\), hence the full neighborhood state at \(s-\) is determined.  Induction over the finite chronological order shows that enlarging a query cluster cannot change an earlier decision, so overlapping queries are consistent.  Finite-depth truncations are measurable functions of finitely many input coordinates and Poisson points and stabilize for each query on the good event.  This proves measurability of all coordinate evaluations; together with coordinatewise càdlàg paths it gives the usual product path-space measurability.  The ancestor rule, acceptance rule, and the good event commute with translations.  Defining the path to remain at its initial value off the good event is also equivariant, so the extension does not spoil covariance.

4. **Pathwise uniqueness and path regularity.**  For two solutions with the same input and noise, induction through the finite ancestor cluster of an arbitrary query forces identical neighborhood states and identical accept/reject decisions at every relevant mark.  Hence the solutions agree at every coordinate and time.  Each coordinate has finitely many potential marks on \([0,1]\), can only move from zero to one, and therefore is càdlàg and pure birth.  On the common no-tie event, accepted births at distinct sites cannot be simultaneous.  The activity bound \(\int_0^1 a_g(t,X_{t-})dt\le M\) is immediate.

5. **Poisson martingale calculation.**  For a cylinder test supported on \(F\), only the finitely many Poisson measures with sites in \(F\) enter its jump identity.  The integrands in (10) are bounded and predictable: \(X_{s-}\) is predictable and \((s,x)\mapsto a_g(s,x)\) is Borel.  Compensation therefore yields (11).  The compensated expression is a function of the observed path and deterministic rate field, so it is adapted to the natural filtration of \(X\); optional projection/tower conditioning transfers the martingale property from the driving filtration.  Taking expectations gives the integrated forward equation (12).  The harmless convention at the Lebesgue-null boundary \(u=0\) has no effect on the compensator or the almost-sure construction.

6. **Finite-volume backward equation.**  For each \(n\), freezing the exterior produces a finite-state, bounded, time-inhomogeneous generator with Borel time coefficients.  Its transition evolution is absolutely continuous and the function \(u_s^{(n)}\) satisfies the backward Kolmogorov equation (18) for almost every \(s\).  No continuity in time beyond the stated Borel boundedness is being silently used.

7. **Boundary oscillation estimate.**  Under the common-noise coupling, a new discrepancy at \(j\) can occur only at a potential mark of \(j\) and only if a discrepancy was already present in \(B_R(j)\).  Consequently a terminal discrepancy in \(F\), starting from a one-site discrepancy at \(i\), supplies a chronological causal chain of length at least \(d_R(i,F)\).  A union bound by expected ordered Poisson tuples gives (19); it does not require any continuity or Lipschitz bound on the rate as a function of the local configuration.  The sphere bound \(|\{i:d_R(i,F)=n\}|\le |F|D^n\) follows by counting length-(n) walks.

8. **Vanishing boundary residual.**  When \(u_s^{(n)}\) is viewed as a cylinder function on the full space, terms outside \(\Lambda_n\) vanish because the function does not depend on them.  For an interior site, the full and frozen rates coincide because its entire \(R\)-neighborhood lies in \(\Lambda_n\).  Only sites at interaction distance exactly \(n\) can contribute.  Combining their oscillations with \(|a_i-a_i^{(n)}|\le M\) yields (21), and
   \[
   D^n\sum_{k\ge n}\frac{(DM)^k}{k!}
   \le e^{DM}\frac{(D^2M)^n}{n!}
   \longrightarrow0.
   \]
   Thus the residual estimate (22) is valid (with the displayed supremum understood as an essential supremum at the null set of times where the backward derivative is not defined).

9. **Time-dependent test extension and uniqueness.**  The integrated cylinder equation makes the probability of every finite pattern an absolutely continuous function of time.  Expanding \(u_s^{(n)}\) in the finitely many pattern indicators, whose coefficients are absolutely continuous, permits the ordinary scalar product rule and proves (24).  Applying the vanishing residual to two law curves with the same initial law gives (26).  Bounded cylinder functions determine probability measures on the countable product \(E\), so the bounded finite-range forward equation has at most one law-valued solution for each initial distribution.  This closes the otherwise essential gap between “both curves satisfy the equation” and equality of their marginals.

10. **Identification of the DPP marginals.**  The graphical law curve and the prescribed DPP curve both start at \(\mu_0\) and satisfy the same integrated cylinder equation.  The uniqueness just proved therefore yields \(\operatorname{Law}(X_t)=\mu_t\) for every \(t\).  No weak-path-law limit or same-input convergence assertion is used.

11. **Supplied iid sampler only.**  The last step assumes, rather than derives, an equivariant iid-factor sampler \(\Psi\) for \(\mu_0\).  It keeps this iid layer independent of a second iid layer encoding the sitewise Poisson measures, and equivariance follows by composition with the already established graphical map.  Hence it does not smuggle in a general iid representation of the initial DPP.

## Verdict

No critical gap was found.  The proof establishes a measurable, equivariant, pathwise unique common-Poisson Harris realization with the prescribed DPP one-time marginals exactly under the frozen **uniformly bounded finite-range** assumptions.  Its forward-equation uniqueness argument is sufficient for this local bounded class and must not be extrapolated to the general strong-process problem.
