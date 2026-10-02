# Strong graphical realization for bounded finite-range DPP birth rates

## Frozen theorem

Let \(\Gamma\) be a finitely generated countable group with a fixed finite symmetric generating set and Cayley metric. Let
\[
K_t=C+tH,\qquad 0\le t\le1,
\]
be a \(\Gamma\)-equivariant uniformly gapped DPP path on the regular \(\Gamma\)-set, with one-time laws \(\mu_t\).

Suppose nonnegative covariant pure-birth rates \(a_g(t,x)\) satisfy:

1. \(a_g(t,x)=0\) whenever \(x_g=1\);
2. for some fixed finite radius \(R\), \(a_g(t,x)\) depends only on \(x|_{B_R(g)}\), and is jointly Borel in \((t,x)\);
3. for some finite \(M\), \(0\le a_g(t,x)\le M\) for every \(g,t,x\);
4. \((\mu_t,a)\) satisfies the exact cylinder continuity equation for every bounded cylinder test.

Let \(X_0\sim\mu_0\). Independently attach to every \(g\in\Gamma\) an iid Poisson random measure \(N_g\) on \([0,1]\times[0,M]\) with intensity \(dt\,du\). At a mark \((t,u)\) of \(N_g\), a vacant coordinate \(g\) is born exactly when
\[
u\le a_g(t,X_{t-}).
\]

Prove or disprove that this Harris graphical prescription defines, for every initial configuration outside no exceptional input set needed by the construction, a unique coordinatewise cadlag pure-birth strong solution \(X\), measurable as a \(\Gamma\)-equivariant function of \((X_0,(N_g)_g)\), and that
\[
X_t\sim\mu_t\qquad(0\le t\le1).
\tag{STR}
\]
Equivalently, bounded finite-range covariant rates satisfying the exact DPP continuity equation admit an invariant strong common-Poisson realization. If a fixed equivariant iid factor for \(\mu_0\) is supplied, the whole path must consequently be an equivariant factor of the enlarged iid input.

## Audited input and exact boundary

1. Under mere Borel rates, finite mean local activity and the continuity equation, an ordinary weak prescribed-marginal pure-birth realization is proved. That theorem does not give a common Poisson input or pathwise uniqueness.
2. A complete two-time reduction identifies invariant weak existence with invariant dynamically admissible endpoint laws. The present finite-range theorem should instead build the invariant law directly from an equivariant graphical map.
3. A one-site oscillating-rate example shows that convergence of marginals and integrated forward equations across approximations does not force convergence on one fixed Poisson input. It does not address a single fixed bounded finite-range rate field and cannot by itself disprove (STR).
4. No general claim is available for unbounded rates, infinite-range dependence, varying approximations, or arbitrary Borel nonlocal selectors.

## Exact obligations

A positive proof must construct the infinite graphical process rather than cite a finite-system recipe. Prove that every finite space-time query has an almost surely finite backward dependency cluster despite infinitely many sites; establish simultaneous definition for all coordinates and times, measurability, covariance, pathwise uniqueness, finite local activity and absence of simultaneous positive-time births. Then prove uniqueness of the bounded finite-range martingale problem or forward equation strongly enough that the graphical solution's one-time laws are the prescribed \(\mu_t\); merely observing that \(\mu_t\) satisfies the continuity equation is not sufficient without uniqueness.

The optional iid-factor corollary must keep the initial DPP sampler and the independent Poisson field as separate iid layers and may use only a supplied, already valid equivariant sampler for \(\mu_0\). Do not infer this corollary from weak convergence of path laws.

A negative proof must give data satisfying all four frozen assumptions for which the Harris construction is undefined/nonunique or has a named one-time marginal different from \(\mu_t\). Failure of an approximation sequence, an unbounded-rate example, or an infinite-range example is outside the frozen theorem.

Classify the result only for uniformly bounded finite-range rates. Do not claim the general strong process, general exact JO, or unrestricted factor extraction.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.
