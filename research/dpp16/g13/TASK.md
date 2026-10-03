# Finite-quotient local-endpoint approximation for invariant DPP birth processes

## Frozen theorem

Let (Gamma) be a finitely generated residually finite group with a descending sequence of finite-index normal subgroups
[
Gamma=N_0ge N_1ge N_2gecdots,
qquad
igcap_mN_m={e},
]
whose quotient Cayley graphs (Q_m=Gamma/N_m) have injectivity radii tending to infinity.

On the regular (Gamma)-set, let
[
K_t=C+tH,qquad 0le tle1,
]
be an equivariant uniformly gapped DPP path. Let (a_g(t,x)) be finite-valued jointly Borel covariant pure-birth rates satisfying the exact cylinder continuity equation and finite mean local activity. Ordinary prescribed-marginal weak solutions exist.

Assume that for every (m) there is a (Q_m)-invariant pure-birth path law (P_m) on ({0,1}^{Q_m}) with one-time DPP marginals (mu_t^{(m)}) and generator rates (a^{(m)}). Assume the following local convergence hypotheses:

1. for every finite (FsubsetGamma), after identifying (F) with its image in (Q_m) for all large (m),
[
(K_t^{(m)})_F	o(K_t)_F
]
uniformly in (t), hence the quotient DPP marginals converge locally to (mu_t);

2. for every coordinate (g), every bounded cylinder (f), and every compact time interval, the local generators satisfy
[
L_t^{(m)}f(x|_{Q_m})	o L_tf(x)
]
in (L^1(dt,mu_t^{(m)})) under the same local identification;

3. the local activities are uniformly integrable:
[
sup_mint_0^1!int a_e^{(m)}(t,x),mu_t^{(m)}(dx),dt<infty,
]
and the generator convergence in item 2 includes the truncation tails needed for martingale closure.

Prove or disprove that the periodic lifts of (P_m) have a locally weakly convergent subsequence whose limit is a (Gamma)-invariant prescribed-generator weak pure-birth path law for ((mu_t,a)).

Equivalently, under these explicit approximation hypotheses, the local dynamically admissible endpoint sets in the two-time fixed-point reduction contain invariant elements and the arbitrary-group obstruction disappears for this residually finite approximation scheme.

## Audited input

A complete theorem already shows that a global invariant prescribed-generator weak law exists if and only if invariant dynamically admissible endpoint laws exist independently on all cells of some partitions with mesh tending to zero. Its proof closes disintegration, pasting, compact birth-time interpolation, fixed-marginal (L^1) martingale closure, time zero, path support, and no simultaneous positive-time jumps.

This task is not to repeat that reduction. It is to prove that finite invariant quotient solutions survive the local limit with the exact prescribed generator.

## Exact obligations

A positive proof must specify the compact local birth-time topology, construct the periodic lifts without confusing global periodicity with the target infinite DPP law, prove tightness and (Gamma)-invariance of every subsequential limit, recover every one-time DPP marginal, and pass all natural-filtration cylinder martingale identities to the limit using the stated (L^1) generator convergence and uniform integrability. It must also recover coordinatewise pure-birth càdlàg paths, finite local activity, and no simultaneous positive-time jumps from the limit problem, including the time-zero argument.

Explain exactly how a quotient invariant endpoint law on each fixed interval yields an invariant element of the limiting dynamically admissible endpoint set. No projective consistency in (m), between cells, or between partition refinements may be assumed.

A negative proof must give data satisfying all three approximation hypotheses and finite quotient solutions, but for which every local weak limit fails a named required property. Merely observing that quotient continuity equations need not follow automatically from the infinite equation does not disprove the frozen theorem: their solutions and the convergence hypotheses are assumed here.

Classify the scope precisely. This theorem would be a residually finite approximation criterion, not the full arbitrary-group result, not a strong factor construction, and not exact JO.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.

