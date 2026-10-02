# Dimension-free selector for uniformly bounded block-diagonal DPP kernels

## Frozen theorem

Fix (0<arepsilon<1/2) and an integer (rge1). Let a finite coordinate set be supplied with a partition
[
E=igsqcup_{alphain A} B_alpha,
qquad 1le |B_alpha|le r.
]
Let
[
K=igoplus_{alphain A}K_alpha,
qquad
arepsilon Ipreceq Kpreceq(1-arepsilon)I,
]
and let (P=vv^*) be an arbitrary rank-one projector, with no support bound.

For each block put
[
w_alpha=|v_{B_alpha}|_2^2=operatorname{tr}P_{B_alpha},
]
and, when (w_alpha>0),
[
R_alpha=w_alpha^{-1}P_{B_alpha}.
]
Thus (R_alpha) is a rank-one projector on (B_alpha). Let
[
G_{K_alpha,R_alpha}
]
be the unique least-Euclidean-norm point of the full positive capacitated birth-flow fiber on (B_alpha). Define a global flow by
[
oxed{
F^{mathrm{blk}}_{K,P}(Tcup S,i)
=
w_alpha,
p_{K_{Esetminus B_alpha}}(T),
G_{K_alpha,R_alpha}(S,i)
}
	ag{BSEL}
]
when (iin B_alphasetminus S), (Ssubseteq B_alpha), and (Tsubseteq Esetminus B_alpha); the (alpha)-term is zero when (w_alpha=0).

Prove or disprove that (BSEL) is a Borel, partition-permutation-equivariant member of the full fiber (mathcal F_E(K,P)), and that there is a finite (C_{arepsilon,r}), independent of (|E|) and the number of blocks, such that
[
|F^{mathrm{blk}}_{K,P}-F^{mathrm{blk}}_{L,Q}|_1
le
C_{arepsilon,r}
igl(|K-L|_1+|P-Q|_1igr)
	ag{BLIP}
]
whenever (K,L) are gapped and block diagonal for the same supplied partition and (P,Q) are arbitrary rank-one projectors.

## Audited input

The local least-norm selector is dimension-free for every fixed support bound, hence uniformly Lipschitz on blocks of size at most (r). For (r=1), (BSEL) reduces to the audited diagonal formula
[
F_{K,P}(S,i)=P_{ii}p_{K_{Esetminus{i}}}(S)
]
with universal constant two.

The DPP of a block-diagonal kernel is the product of its block DPP laws. At a block-diagonal kernel, cross-block entries of (P) do not contribute to the atom derivative, but this must be proved rather than assumed.

## Exact obligations

A positive proof must verify exact divergence, unit mass, nonnegativity, and the original pointwise capacity. It must prove the simultaneous ((K,P)) estimate without dividing uncontrollably by small (w_alpha). In particular, establish an appropriate inequality controlling
[
w_alpha G_{K_alpha,R_alpha}
-
z_alpha G_{L_alpha,S_alpha}
]
directly by the unnormalized compressed rank-one matrices (P_{B_alpha}), (Q_{B_alpha}), and show that summing over blocks is controlled by trace-norm pinching rather than the number of blocks. Product-law changes in the outside coordinates must also be summed with the weights (w_alpha).

Treat (w_alpha=0), support degeneration, Borel dependence, and covariance under permutations carrying the supplied partition to the relabeled partition. Give an explicit or exactly defined finite (C_{arepsilon,r}).

A negative proof must identify an actual failure of (BSEL) or construct a dimension-growing violation of (BLIP). Instability of unrelated flows elsewhere in the full fiber is not enough.

This theorem concerns a supplied uniformly bounded block decomposition. Do not claim the unrestricted non-diagonal theorem.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.

