# Uniform-in-support stability of the global least-norm DPP birth-flow selector

## Frozen problem

Fix (0<arepsilon<1/2). For every finite coordinate set (E), every Hermitian kernel
[
arepsilon Ipreceq Kpreceq(1-arepsilon)I,
]
and every rank-one projector (P), let (mathcal F_E(K,P)) be the full polytope of nonnegative upward Boolean-cube edge flows having divergence (b_{K,P}), total mass one, and outgoing capacity
[
F_{m out}(S)le (2/arepsilon)p_K(S).
]
Define the single global selector
[
oxed{
Phi_E(K,P)
=
operatorname*{argmin}_{finmathcal F_E(K,P)}
rac12sum_{S,i
otin S} f(S,i)^2.
}
	ag{LM}
]

Prove or disprove that there is a finite (C_arepsilon), independent of both (|E|) and (|operatorname{supp}P|), such that
[
|Phi_E(K,P)-Phi_E(L,Q)|_1
le
C_arepsilonigl(|K-L|_1+|P-Q|_1igr)
	ag{ULM}
]
for every two admissible pairs on the same (E).

## Audited input

For every fixed finite support bound (s), this exact same global least-norm selector satisfies (ULM) with a finite constant (C_{arepsilon,s}) independent of (|E|). The proof uses exact conditioning/product compatibility and reduces comparison to at most (2s) active coordinates; an integer-Gram bound then produces a very large (s)-dependent constant.

The entire flow fibers do not have a dimension-free Hausdorff modulus, already at (K=L=I/2). That does not disprove (ULM), because a stable section may coexist with unstable circulations elsewhere in the fibers. At (K=I/2) an explicit different selector with constant one is known.

## Exact obligations

A positive proof must remove the support-size dependence for the selector (LM), not replace it by another selector. It must control simultaneous changes of (K) and (P), all support degenerations, and every finite (E), and must explain why the exponentially large Boolean-cube active-set constants do not enter.

A negative proof must give a concrete sequence of dimensions and admissible pairs for which the ratio in (ULM) diverges for the actual unique least-norm selector (LM). It is not enough to exhibit two far-apart points of the fibers, a bad circulation that (LM) does not choose, or an active-set matrix with a small singular value without proving that the corresponding active set is realized by the DPP fibers and drives the minimizer.

Classify the result narrowly: disproving (ULM) for (LM) would not disprove the existence of some other unrestricted selector; proving (ULM) would settle only the positive selector target, not exact JO or a strong process.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.

