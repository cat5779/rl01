## 1. Shorting, measurability, and one-sided continuity

For 0≤A≤I on H and η⊆W, set

\[
\Pi_\eta^A=P_{\overline{A^{1/2}\ell^2(\eta)}},\qquad
\mathsf S_\eta(A)=A^{1/2}(I-\Pi_\eta^A)A^{1/2},\qquad
b_A(x,\eta)=\langle\mathsf S_\eta(A)\delta_x,\delta_x\rangle. \tag{1.1}
\]

The Hilbert-space distance formula gives

\[
\langle\mathsf S_\eta(A)f,f\rangle
=\inf_{g\in\ell^2(\eta)}
  \langle A(f+g),f+g\rangle. \tag{1.2}
\]

Therefore 0≤\mathsf S_\eta(A)≤A≤I, b_A(x,η)=0 for x∈η, and η⊆ζ implies \mathsf S_\eta(A)≥\mathsf S_\zeta(A). Equivariance of A gives b_A(gx,gη)=b_A(x,η).

For each fixed x, the infimum in (1.2), with f=δ_x, can be taken over finite-support rational complex vectors g whose supports lie in η. This countable formula proves Borel measurability in η. Strong measurability of \Pi_\eta^A follows by approximating η with fixed finite exhaustions of W, computing the finite Gram-matrix range projections by Moore–Penrose inverses, and passing to the strong limit. The polar part of a measurable covariant operator T is measurable by
\[
V=\mathrm{s}\!-\!\lim_{r\to\infty}T(T^*T+r^{-1}I)^{-1/2}.
\]
These constructions preserve covariance in the limit.

For later use, if A_j↓A strongly and all are uniformly bounded positive operators, then (1.2) gives, for each f,
\[
\langle\mathsf S_\eta(A_j)f,f\rangle
\downarrow\langle\mathsf S_\eta(A)f,f\rangle
\]
because \inf_j\inf_g=\inf_g\inf_j. Bounded monotone positive-operator convergence gives \mathsf S_\eta(A_j)↓\mathsf S_\eta(A) strongly. This is for fixed η and decreasing A_j only; moving η will be handled separately.

## 2. The finite-label averaged trace estimate

Let (η,ζ) be a *jointly Γ-invariant* pair of random subsets of W. For bounded covariant random operators B, define the nonnormalized finite-label trace

\[
\bar\tau_S(B)
=\sum_{a\in S}\mathbb E\langle B\delta_{(e,a)},\delta_{(e,a)}\rangle. \tag{2.1}
\]

It is a finite tracial functional: after expanding \bar\tau_S(BC), sum over γ∈Γ and b∈S; joint invariance exchanges the origin and γ, while finite partial sums and Cauchy–Schwarz justify the exchange for bounded B,C. Thus \bar\tau_S(BC)=\bar\tau_S(CB). The unnormalized trace is important; normalizing by m would alter the following error budget.

The estimate required by the dynamics is

\[
\boxed{\quad
\sum_{a\in S}\mathbb E
 \left|b_A((e,a),\eta)-b_A((e,a),\zeta)\right|
\le
\sum_{a\in S}\mathbb P[\eta(e,a)\ne\zeta(e,a)] .
\quad} \tag{2.2}
\]

This is a **sum over labels**. It does not imply (and we do not use) the same inequality separately for each a.

For η⊆ζ, let D=P_{\ell²(\zeta\setminus\eta)} and T=(I-\Pi_\eta^A)A^{1/2}D. The closure of ran T is \overline{A^{1/2}\ell²(\zeta)}\ominus\overline{A^{1/2}\ell²(\eta)}. If T=V|T|, then VV*=Π_ζ^A−Π_η^A and V*V≤D. Traciality gives
\[
\bar\tau_S(\Pi_\zeta^A-\Pi_\eta^A)
=\bar\tau_S(VV^*)=\bar\tau_S(V^*V)
\le \bar\tau_S(D)
=\sum_a\mathbb P[(e,a)\in\zeta\setminus\eta]. \tag{2.3}
\]
Since A≤I and P:=Π_ζ^A−Π_η^A is a projection,
\[
\sum_a\mathbb E[b_A((e,a),\eta)-b_A((e,a),\zeta)]
=\bar\tau_S(A^{1/2}PA^{1/2})
=\bar\tau_S(PAP)
\le\bar\tau_S(P). \tag{2.4}
\]
For arbitrary η,ζ, put θ=η∩ζ. Pointwise monotonicity gives
\[
|b_A(x,\eta)-b_A(x,\zeta)|
\le[b_A(x,\theta)-b_A(x,\eta)]
  +[b_A(x,\theta)-b_A(x,\zeta)].
\]
Sum over a and apply (2.3)–(2.4) to both nested pairs. Their difference sets are disjoint, giving (2.2).

## 3. One iid PRM field and Picard construction

For s≥0 define
\[
t_s=1-e^{-s},\qquad
A_s=e^{-s}Q(I-t_sQ)^{-1}. \tag{3.1}
\]
The scalar map f_s(q)=e^{-s}q/[1-(1-e^{-s})q] lies in [0,1] for q∈[0,1], even at q=1. Hence 0≤A_s≤I. The map s↦A_s is norm-continuous on each bounded interval, so (s,η)↦b_{A_s}(x,η) is Borel. For an adapted càdlàg configuration process Y, the threshold b_{A_s}(x,Y_{s-}) is predictable.

Place independent PRMs N_x(ds\,du) of intensity ds du at all x∈W. For X^(0)_s=∅ define recursively
\[
X^{(k+1)}_s(x)
=\mathbf1\{\exists(r,u)\in N_x:\ r\le s,\quad
 u\le b_{A_r}(x,X^{(k)}_{r-})\}. \tag{3.2}
\]
Each iterate is an equivariant measurable function of the PRM past, has a càdlàg path with at most one 0-to-1 change at each x, and all iterates are jointly Γ-invariant.

Write x_a=(e,a) and
\[
D_k(T)=\sum_{a\in S}
 \mathbb P\{\exists s\le T:
 X^{(k+1)}_s(x_a)\ne X^{(k)}_s(x_a)\}. \tag{3.3}
\]
If two updated paths at x_a differ, some common proposal was accepted by just one threshold. Predictable PRM compensation, followed by the **summed** estimate (2.2) on the jointly invariant input pair, yields
\[
D_k(T)\le\int_0^T D_{k-1}(s)\,ds,\qquad
D_0(T)\le m,\qquad
D_k(T)\le m\,T^k/k!. \tag{3.4}
\]
No single-label use of (2.2) occurs. Summability over k, followed by Borel–Cantelli over the countable W and integer T, gives eventual equality of every coordinate path on every compact time interval. Call the limit X. It is an equivariant measurable càdlàg pure-birth function of N.

The fixed-point equation follows by comparing the update of X^(k) with the update of X: the summed proposal-disagreement probability on [0,T] is at most
\[
\int_0^T\sum_a
\mathbb P[X^{(k)}_{s-}(x_a)\ne X_{s-}(x_a)]\,ds\longrightarrow0.
\]
The input paths stabilize and the integrand is bounded by m. Since the updated X^(k) also tends to X, X satisfies (3.2) with its own left limits.

Here is the exact uniqueness class used later. Suppose N is a PRM relative to a **common** filtration G, and U,V are G-adapted, jointly Γ-invariant, càdlàg pure-birth solutions driven by that N from ∅. Let
\[
D_{U,V}(T)=\sum_a\mathbb P\{
 U_\cdot(x_a)\ne V_\cdot(x_a)\text{ somewhere on }[0,T]\}.
\]
Compensation and (2.2) give D_{U,V}(T)≤∫_0^T D_{U,V}(s)ds, so Grönwall gives zero. Countability and right continuity yield indistinguishable paths. V is **not** required in advance to be adapted to the natural filtration of N.

