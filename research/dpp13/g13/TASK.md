# Fixed-point problem for invariant weak DPP birth dynamics

## Frozen target W

Let \(\Gamma\) be a countable group acting on itself by left translation and set
\[
E=\{0,1\}^{\Gamma}.
\]
Let
\[
K_t=C+tH,\qquad 0\le t\le1,
\]
be a translation-equivariant Hermitian path on \(\ell^2(\Gamma)\) with
\[
\varepsilon I\le K_t\le(1-\varepsilon)I
\]
for some \(0<\varepsilon<1/2\), and let \(\mu_t\) be the DPP of \(K_t\).

Suppose \(a_i(t,x)\in[0,\infty)\) is a jointly Borel, finite-valued, covariant pure-birth rate field:
\[
a_{gi}(t,gx)=a_i(t,x),\qquad
a_i(t,x)=0\ \text{if }x_i=1.
\]
Assume
\[
\int_0^1\int_E a_e(t,x)\,\mu_t(dx)\,dt<\infty
\tag{A}
\]
and, for every bounded cylinder function \(f\),
\[
\int f\,d\mu_t-\int f\,d\mu_0
=
\int_0^t\int_E
\sum_i a_i(s,x)
\bigl[f(x\cup\{i\})-f(x)\bigr]
\,\mu_s(dx)\,ds.
\tag{CE}
\]

It is now established that (A) and (CE) admit at least one ordinary coordinatewise càdlàg pure-birth weak martingale realization with one-time marginals \(\mu_t\), at most one jump per coordinate, and no simultaneous positive-time jumps.

Prove or disprove:

> There is such a realization whose full path law is \(\Gamma\)-invariant.

This is invariant weak existence only. Do not add or claim a strong solution, independent sitewise Poisson representation, pathwise uniqueness, factor of iid, all-input equivariance, or same-noise approximation convergence.

## Exact fixed-point obligation

Let \(\mathcal S(a,\mu)\) be the set of ordinary path laws with the required marginals and martingale generator. Covariance makes \(\mathcal S(a,\mu)\) a \(\Gamma\)-space. The problem is to prove
\[
\mathcal S(a,\mu)^\Gamma\ne\varnothing
\tag{FP}
\]
using the special DPP curve and rate structure, or to construct admissible DPP/rate data for which the fixed-point set is empty.

Averaging an orbit is invalid for a nonamenable group. The facts that every \(\mu_t\) is invariant and that an ordinary solution exists do not by themselves prove (FP).

## Audited boundary facts

You may use the following.

1. The ordinary weak realization theorem under (A) and (CE) is proved. It includes natural-filtration closure, the time-zero atom, and absence of simultaneous jumps.
2. For amenable \(\Gamma\), Følner averaging of an ordinary solution proves invariant weak existence.
3. If the ordinary martingale problem is unique in law within the pure-birth class, covariance forces invariance.
4. Mester's invariant monotone-coupling example shows that invariant marginals plus an ordinary monotone coupling need not yield an invariant coupling on a nonamenable Cayley graph. It is not a DPP counterexample and does not supply the present rate field.
5. Lyons--Thom prove invariant monotone couplings for ordered equivariant DPP kernels in their sofic setting. This does not automatically give a continuous-time path law with the prescribed rates.
6. For the motivating rank-one DPP construction, covariant one-point couplings provide rates satisfying (A) and (CE); this rate construction alone is not a path-law fixed point.

## Acceptable outcomes

A positive proof must give a genuinely covariant or canonical construction and verify the prescribed generator, not merely the endpoint order.

A disproof must retain all of the following: a uniformly gapped linear equivariant DPP path, finite-valued covariant Borel rates, exact cylinder equation, integrable mean local activity, and nonexistence of every invariant weak solution.

If the full arbitrary-group target remains open, do not repeat the already known amenable or weak-uniqueness corollaries as the main result. Instead prove one new sharply stated advance, for example:

- an invariant realization under a nonamenable structural hypothesis weaker than weak uniqueness;
- a canonical extremal/Markov selection theorem that forces a fixed point for this DPP solution space;
- a sofic approximation theorem that preserves the prescribed Borel generator, with every approximation and closure step checked;
- or an exact DPP-specific obstruction showing why a proposed fixed-point route fails.

Classify every restricted result against W.

## Verdict

Return exactly one of PROVED, DISPROVED, or INCOMPLETE, followed by a complete supporting argument. Do not use ordinary weak existence, invariant one-time marginals, or endpoint invariant coupling as a substitute for an invariant full path law with the stated martingale generator.
