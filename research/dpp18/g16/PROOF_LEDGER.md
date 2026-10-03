# Proof ledger

This file records only results already supported by the upstream DPP research record and its audits. It is not a new proof of the frozen theorem.

## A. Endpoint reduction on the commuting class

For a commuting pair \((K,P)\), write \(P=vv^*\),
\[
\lambda=\operatorname{tr}(KP),\qquad A=K-\lambda P.
\]
Then
\[
Kv=\lambda v,\qquad Av=0,
\]
and with
\[
\mu_0=p_A,\qquad \mu_1=p_{A+P},
\]
rank-one affinity gives
\[
p_K=(1-\lambda)\mu_0+\lambda\mu_1,
\qquad
b_{K,P}=\mu_1-\mu_0.
\]

Let \(\mathcal G(K,P)\) be the nonnegative upward edge flows satisfying exact endpoint marginals
\[
\sum_{i\notin S}f(S,i)=\mu_0(S),\qquad
\sum_{i\in T}f(T\setminus\{i\},i)=\mu_1(T).
\]
Then every \(f\in\mathcal G(K,P)\) lies in the original flow fiber and satisfies the stronger capacity
\[
f_{\rm out}(S)=\mu_0(S)
\le \frac{p_K(S)}{1-\lambda}
\le \varepsilon^{-1}p_K(S).
\]

Source: #119, \`research/dpp17/g11/RESULT.md\`, §§1–2; review certifies the reduction.

## B. Explicit signed endpoint current

For \(S\subseteq E\), let \(D_{S^c}\) be the diagonal projection onto \(E\setminus S\) and
\[
M_S(K)=K-D_{S^c}.
\]
The gap gives
\[
\|M_S(K)^{-1}\|_{\rm op}\le \varepsilon^{-1}.
\]

Define
\[
J_{K,P}(S,i)
=
-p_K(S)\operatorname{Re}\bigl(PM_S(K)^{-1}\bigr)_{ii},
\qquad i\notin S.
\]

Certified properties:

1. \(\operatorname{div}J_{K,P}=b_{K,P}\).
2. \(J\) has exact source/target endpoint marginals \((\mu_0,\mu_1)\).
3. Total signed edge mass is one.
4.
   \[
   \|J_{K,P}\|_1\le \varepsilon^{-1}.
   \]
5. Dimension-free stability:
   \[
   \boxed{
   \|J_{K,P}-J_{L,Q}\|_1
   \le
   \frac{3}{\varepsilon^2}\|K-L\|_1
   +
   \frac1\varepsilon\|P-Q\|_1.
   }
   \]

Source: #119 §§2 and review §1.

## C. Positive-part capacity theorem

For every commuting pair there exists
\[
f\in\mathcal G(K,P)
\]
with
\[
\boxed{
0\le f(S,i)\le 2J_{K,P}(S,i)_+.
}
\]

The proof is not a generic transport fact. It uses the Fock-space representation of the two endpoint states and the projection identity
\[
RQ+QR-(R+Q-I)=(R+Q-I)^2\succeq0
\]
to obtain all bipartite max-flow cuts.

Useful consequences:
\[
\sum_{S,i}2J(S,i)_+
=
1+\|J\|_1
\le 1+\varepsilon^{-1},
\]
and
\[
\boxed{
\|2(J_{K,P})_+-2(J_{L,Q})_+\|_1
\le
\frac6{\varepsilon^2}\|K-L\|_1
+\frac2\varepsilon\|P-Q\|_1.
}
\]

Thus the constrained positive fibers
\[
\mathcal H(K,P)
=
\{f\in\mathcal G(K,P):0\le f\le2J_{K,P,+}\}
\]
are always nonempty and their defining data have dimension-free \(\ell^1\) moduli.

What is *not* certified: a dimension-free Lipschitz section of \(\mathcal H\).

Source: #119 §3 and review §2; frozen as a standalone selector task in #122.

## D. Fixed-projector positive repair

If
\[
KP=PK,\qquad LP=PL,
\]
then for every
\[
f\in\mathcal G(K,P)
\]
there is
\[
g\in\mathcal G(L,P)
\]
such that
\[
\boxed{
\|f-g\|_1
\le
\frac{2}{\varepsilon(1-\varepsilon)}
\|K-L\|_1.
}
\]

The estimate is symmetric after swapping the two kernels.

Core mechanism: on \(H=v^\perp\), compare the fermionic background states \(\sigma_B,\sigma_{B'}\) by
\[
e^{-D}\sigma_B\preceq\sigma_{B'}\preceq e^D\sigma_B,
\qquad
D=\frac{\|B-B'\|_1}{\varepsilon(1-\varepsilon)},
\]
then couple the positive residual state by a weighted Hall argument.

This gives Lipschitz selection along any single fixed-\(P\) affine segment, but does not give consistency across different projectors or across different segments.

Source: #119 §4 and review §3.

## E. Complete selectors on restricted classes

### E1. Scalar-complement class

For
\[
K=a(I-P)+\lambda P
\]
with \(a,\lambda\in[\varepsilon,1-\varepsilon]\),
\[
F_{K,P}(S,i)
=
P_{ii}\,a^{|S|}(1-a)^{n-1-|S|}.
\]
This is a Borel permutation-equivariant positive selector and
\[
\boxed{
\|F_{K,P}-F_{L,Q}\|_1
\le
4\|K-L\|_1+3\|P-Q\|_1.
}
\]

Source: #119 §5.

### E2. Diagonal kernels

For diagonal
\[
K=\operatorname{diag}(k_i),
\]
the explicit rule
\[
F_{K,P}(S,i)
=
P_{ii}\,p_{K_{E\setminus\{i\}}}(S)
\]
is a Borel permutation-equivariant selector with universal constant
\[
\boxed{C_\varepsilon=2.}
\]

Source: #115; independent review PASS.

### E3. Fixed scalar kernel \(K=I/2\)

The frozen nonexistence claim at \(K=I/2\) was disproved. The canonical rule
\[
\Phi_E(P)(S,i)=2^{-(|E|-1)}P_{ii}
\]
is a dimension-free Borel equivariant selector with constant \(1\).

Source: #113.

### E4. Canonical matching-block kernels

If every nonzero off-diagonal coordinate component has size at most two, there is an explicit refinement-compatible selector. The audited global estimate is
\[
\boxed{
C_\varepsilon=80\varepsilon^{-2}+205.
}
\]

Key structural fact: when a two-coordinate block becomes diagonal, the local selector agrees exactly with the diagonal selector, so changing canonical matchings can be handled by deleting only noncommon matching edges.

Source: #120; independent review PASS.

## F. Entire-fiber support facts

For every feasible flow,
\[
\boxed{
\sum_{S:i\notin S}F(S,i)=P_{ii}.
}
\]
Consequences:

- coordinate directions have singleton fibers;
- every fiber collapses linearly near a coordinate projector;
- if \(P=vv^*\), every feasible flow only uses added coordinates in \(\operatorname{supp}v\);
- bounded common coordinate support gives a dimension-free ambient-dimension bound, though the constant may depend on the support size.

Source: #103, \`research/dpp11/g12/RESULT02.md\`.

## G. Finite-consistency equivalence

The full commuting selector problem is equivalent to the following finite-list property:

There is \(C_\varepsilon\), independent of \(E\), such that for every finite list
\[
x_1,\dots,x_m
\]
of commuting inputs, one can choose
\[
f_a\in\mathcal F_E(x_a)
\]
simultaneously with
\[
\|f_a-f_b\|_1
\le
C_\varepsilon d(x_a,x_b)
\]
for all \(a,b\).

Conversely, assuming this finite consistency:
1. enumerate a countable dense subset of the fixed-\(E\) commuting domain;
2. apply finite consistency to longer prefixes;
3. use compactness and a diagonal subsequence;
4. extend the resulting Lipschitz assignment uniquely;
5. use closedness of the fiber graph for feasibility;
6. average over \(\operatorname{Sym}(E)\) to enforce permutation covariance.

Source: #119 §6; independent review certifies the equivalence.

## H. Certified negative boundaries

### H1. Full-fiber Hausdorff stability is false

#109 constructs \(K=L=I/2\), nearby rank-one projectors \(P_m,Q_m\), and a deliberately chosen
\[
F_m\in\mathcal F(K,P_m)
\]
whose distance from the whole target fiber stays macroscopic.

This disproves a uniform directed/full Hausdorff theorem, but **not** the existence of a selector that avoids \(F_m\).

### H2. Global least-Euclidean-norm selector is not dimension-free

#116 gives a scalar-kernel family with
\[
\frac{
\|\Phi(K_n,P_n)-\Phi(K_n,Q_n)\|_1
}{
\|P_n-Q_n\|_1
}
\gtrsim_\varepsilon \sqrt n.
\]
All relevant inequality constraints can be strictly inactive. Therefore active-set changes are not the only problem.

However the same scalar family admits a different explicit stable selector, so this is not an every-selector obstruction.

## Current certified conclusion

The full commuting theorem remains open after all items above. The unresolved variable is genuinely global coherence when projectors vary, especially for delocalized directions with support increasing with dimension.
