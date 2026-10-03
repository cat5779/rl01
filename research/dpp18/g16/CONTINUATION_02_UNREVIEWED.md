# Continuation 02 — unreviewed candidate derivations

Date: 2026-10-03

Source target: \`cat5779/rl01#123\`.

## Certification status

**UNREVIEWED CANDIDATE DERIVATIONS.**

Nothing in this file upgrades the main theorem from \`OPEN / INCOMPLETE\`.
The results below were derived in the continuation after the initial breakpoint archive. They have not received an independent mathematical audit. Until such an audit is completed, they must not be copied into \`PROOF_LEDGER.md\` as certified facts.

The most important candidate advances are:

1. a full-fiber fixed-projector repair estimate, stronger in scope than the inherited endpoint-fiber repair;
2. a single globally coherent weighted selector for fixed \(P\) with a dimension-free \(1/2\)-Hölder modulus;
3. a candidate proof of the uniformly bounded coordinate-component theorem for each fixed \(r\);
4. an explicit three-input finite-family inconsistency showing that pairwise optimal distances need not be simultaneously attained;
5. structural obstructions to affine dependence on \(P\), to unconstrained weighted currents, and to arbitrary low-energy repair.

The main varying-projector Lipschitz problem remains unresolved.

---

# 1. Candidate full-fiber repair when the projector is fixed

Let \(P=vv^*\) be fixed and let \(K,L\) be \(\varepsilon\)-gapped Hermitian kernels satisfying
\[
KP=PK,\qquad LP=PL.
\]
Write
\[
K=\lambda P+B,\qquad L=\nu P+B',
\]
on
\[
\mathbb C v\oplus H,\qquad H=v^\perp.
\]
Because this is one common orthogonal decomposition,
\[
\boxed{
\|K-L\|_1=\|B-B'\|_1+|\lambda-\nu|.
}
\tag{1.1}
\]

The inherited result only repairs the smaller endpoint fiber \(\mathcal G(K,P)\). The following candidate argument extends repair to the original full positive fiber \(\mathcal F(K,P)\).

## 1.1 Change only the background

Set
\[
M=\lambda P+B'.
\]
From the inherited fermionic Loewner comparison, with
\[
D_B=\frac{\|B-B'\|_1}{\varepsilon(1-\varepsilon)},
\qquad
c_B=e^{-D_B},
\]
one has
\[
\tau:=\sigma_{B'}-c_B\sigma_B\succeq0,
\qquad
\operatorname{tr}\tau=1-c_B.
\]

Let \(h_B\) be any nonnegative upward one-point coupling associated with the residual state \(\tau\). Its source and target marginals are denoted
\[
\alpha_\tau,\qquad \beta_\tau.
\]
Its total edge mass is \(1-c_B\).

Take an arbitrary
\[
f\in\mathcal F(K,P),
\]
not necessarily in the endpoint subfiber. Define
\[
g_M=c_Bf+h_B.
\tag{1.2}
\]

Its divergence is the correct divergence for \(M\), because the residual source-target difference exactly supplies the background change. Its total mass is one.

For capacity, the atom mixture identity gives
\[
p_M-c_Bp_K
=
(1-\lambda)\alpha_\tau+\lambda\beta_\tau.
\tag{1.3}
\]
Since
\[
(h_B)_{\rm out}=\alpha_\tau
\]
and
\[
\frac{2}{\varepsilon}(1-\lambda)\ge2,
\]
we obtain
\[
\begin{aligned}
(g_M)_{\rm out}
&\le
c_B\frac2\varepsilon p_K+\alpha_\tau\\
&\le
c_B\frac2\varepsilon p_K
+\frac2\varepsilon\bigl[(1-\lambda)\alpha_\tau+\lambda\beta_\tau\bigr]\\
&=
\frac2\varepsilon p_M.
\end{aligned}
\tag{1.4}
\]
Thus
\[
g_M\in\mathcal F(M,P).
\]

Moreover,
\[
\|g_M-f\|_1
\le
(1-c_B)\|f\|_1+\|h_B\|_1
=
2(1-c_B)
\le2D_B.
\tag{1.5}
\]

## 1.2 Change only the marked eigenvalue

Now the background \(B'\) is fixed and only \(\lambda\) changes to \(\nu\). The directional divergence in \(P\) depends on the two endpoint laws and therefore is independent of the marked eigenvalue.

Choose a unit-mass positive endpoint flow \(h\) for the common endpoint pair and set
\[
c_\lambda
=
\min\left\{
1,\frac{\nu}{\lambda},
\frac{1-\nu-\varepsilon/2}{1-\lambda-\varepsilon/2}
\right\}.
\tag{1.6}
\]
All denominators are positive because
\[
\lambda,\nu\in[\varepsilon,1-\varepsilon].
\]

Define
\[
g=c_\lambda g_M+(1-c_\lambda)h.
\tag{1.7}
\]
The divergence and total mass are correct. The two scalar inequalities
\[
\nu-c_\lambda\lambda\ge0,
\]
\[
1-\nu-c_\lambda(1-\lambda)
\ge
\frac{\varepsilon}{2}(1-c_\lambda)
\tag{1.8}
\]
supply the outgoing-capacity slack needed for the second mixture component.

Also
\[
1-c_\lambda
\le
\frac{2|\lambda-\nu|}{\varepsilon},
\]
so
\[
\|g-g_M\|_1
\le
\frac4\varepsilon|\lambda-\nu|.
\tag{1.9}
\]

Combining (1.1), (1.5), (1.9), and
\[
\frac2{\varepsilon(1-\varepsilon)}
\le
\frac4\varepsilon,
\]
gives the candidate directed repair estimate
\[
\boxed{
\forall f\in\mathcal F(K,P)\ \exists g\in\mathcal F(L,P):
\quad
\|f-g\|_1
\le
\frac4\varepsilon\|K-L\|_1.
}
\tag{1.10}
\]
Repeating in the reverse direction would give the same bound for the Hausdorff distance of the two full fibers.

### Audit obligations for Section 1

An independent reviewer should check carefully:

- the exact residual atom identity (1.3);
- that the chosen residual flow \(h_B\) indeed has source marginal \(\alpha_\tau\) and total mass \(1-c_B\);
- the marked-eigenvalue capacity calculation behind (1.8);
- endpoint cases \(\lambda=\nu\), \(\lambda=\varepsilon\), and \(\lambda=1-\varepsilon\).

---

# 2. Candidate globally coherent fixed-\(P\) selector with \(1/2\)-Hölder modulus

The inherited fixed-\(P\) repair theorem is pairwise and pathwise; it does not give one selector on the whole fixed-\(P\) domain. This section proposes one.

## 2.1 Intrinsic edge weights

For an upward edge \(e=(S,i)\), define
\[
\boxed{
w_{K,P}(S,i)
=
P_{ii}\,
p_{K_{E\setminus\{i\}}}(S).
}
\tag{2.1}
\]
Equivalently,
\[
p_{K_{E\setminus\{i\}}}(S)
=
p_K(S)+p_K(S\cup\{i\}),
\]
hence
\[
w_{K,P}(S,i)
=
P_{ii}\bigl[p_K(S)+p_K(S\cup\{i\})\bigr].
\tag{2.2}
\]

Since every reduced DPP law has total mass one,
\[
\sum_{S,i}w_{K,P}(S,i)
=
\sum_iP_{ii}
=
1.
\tag{2.3}
\]

Every feasible flow satisfies the coordinate-mass identity
\[
\sum_{S:i\notin S}f(S,i)=P_{ii}.
\tag{2.4}
\]
Therefore if \(P_{ii}=0\), every \(i\)-edge is forced to carry zero mass.

On the non-forced edges define
\[
\|f\|_{w}^2
=
\sum_e\frac{f_e^2}{w_e}.
\tag{2.5}
\]
Because \(\sum_ew_e=1\), Cauchy-Schwarz gives
\[
\boxed{
\|f\|_1\le\|f\|_w.
}
\tag{2.6}
\]

## 2.2 Uniform energy bound for the signed current

Let
\[
M_S=K-D_{S^c},
\qquad
u^S=M_S^{-1}v.
\]
The signed current on an edge adjacent to \(S\) has the form
\[
J_e
=
\pm p_K(S)\operatorname{Re}(\overline v_i u_i^S).
\tag{2.7}
\]

The spectral gap implies the conditional exact-atom probability of coordinate \(i\), conditional on the other coordinates, lies in \([\varepsilon,1-\varepsilon]\). Consequently,
\[
\frac{J_e^2}{w_e}
\le
(1-\varepsilon)p_K(S)|u_i^S|^2.
\tag{2.8}
\]

Summing over vertices counts each edge twice. Using
\[
\|M_S^{-1}\|_{\rm op}\le\varepsilon^{-1}
\]
gives the candidate uniform energy estimate
\[
\boxed{
\|J\|_w^2
\le
\frac{1-\varepsilon}{2\varepsilon^2}.
}
\tag{2.9}
\]

The inherited positive-part theorem provides a positive endpoint flow
\[
0\le h\le2J_+.
\]
Therefore
\[
\boxed{
\|h\|_w
\le
B_\varepsilon
:=
\frac{\sqrt{2(1-\varepsilon)}}{\varepsilon}.
}
\tag{2.10}
\]

## 2.3 Define one selector on the full original fiber

Define
\[
\boxed{
\Psi_E(K,P)
=
\operatorname*{argmin}_{f\in\mathcal F_E(K,P)}
\frac12
\sum_{e:w_e>0}\frac{f_e^2}{w_e}.
}
\tag{2.11}
\]
The nonnegative constraints and the original outgoing capacities remain in the optimization problem.

After deleting forced zero coordinates, the objective is strictly convex, so the minimizer is unique. The feasible endpoint flow from (2.10) yields
\[
\|\Psi_E(K,P)\|_w\le B_\varepsilon.
\tag{2.12}
\]

## 2.4 Candidate fixed-\(P\) \(1/2\)-Hölder estimate

For the same fixed projector \(P\), let
\[
\delta=\|K-L\|_1.
\]
Along the segment
\[
K_t=(1-t)K+tL,
\]
the candidate differential estimates are
\[
|\partial_t\log w_t(e)|
\le
\frac{\delta}{\varepsilon},
\tag{2.13}
\]
and
\[
\|\dot J_t\|_{w_t}
\le
\frac{B_\varepsilon}{\varepsilon}\delta.
\tag{2.14}
\]
The second estimate follows by differentiating
\[
u_t^S=M_S(K_t)^{-1}v,
\qquad
\dot u_t^S
=
-M_S(K_t)^{-1}(L-K)u_t^S,
\]
and repeating the double-counted energy estimate.

When \(\delta\le\varepsilon\), (2.13) makes the two weighted norms uniformly equivalent, and integration of (2.14) controls the signed-current change in weighted energy.

Combining the full-fiber repair construction from Section 1 with the variational inequalities for the two minimizers gives a candidate estimate of the form
\[
\|\Psi(K,P)-\Psi(L,P)\|_{w_K}^2
\le
C\,B_\varepsilon^2\frac{\delta}{\varepsilon}
\tag{2.15}
\]
with an absolute numerical \(C\). The continuation derivation used the safe value \(C=50\). Consequently,
\[
\boxed{
\|\Psi(K,P)-\Psi(L,P)\|_1
\le
10\,\varepsilon^{-3/2}\,
\|K-L\|_1^{1/2}.
}
\tag{2.16}
\]
For \(\delta\ge\varepsilon\), the trivial bound between two unit-mass nonnegative flows closes the global estimate.

This is a single globally defined rule, so it provides simultaneous consistency for any finite family sharing the same projector, but only at exponent \(1/2\).

## 2.5 Degenerations, Borel dependence and symmetry

For fixed \(E\), when \(P_{ii}\to0\), feasibility gives
\[
f_e\le P_{ii}.
\]
Thus
\[
\frac{f_e^2}{P_{ii}p_{K_{-i}}(S)}
\le
\frac{P_{ii}}{p_{K_{-i}}(S)}
\to0,
\]
using the fixed-gap positivity of reduced atoms.

Together with compactness of the feasible graph and uniqueness of the minimizer, this suggests continuity across support degeneration. The objective and constraints are permutation-natural, so uniqueness would imply exact coordinate-permutation covariance.

### Main unresolved step after Section 2

The proof still only gives
\[
\|\Psi(K,P)-\Psi(L,P)\|^2
\lesssim
\|K-L\|,
\]
not a Lipschitz square estimate
\[
\|\Psi(K,P)-\Psi(L,P)\|^2
\lesssim
\|K-L\|^2.
\]
It also does not compare varying projectors.

---

# 3. Candidate proof for uniformly bounded canonical components

This section concerns the adjacent frozen task represented upstream by \`cat5779/rl01#124\`.

Fix an integer \(r\). Suppose every connected component of the coordinate graph of \(K\) has size at most \(r\). The continuation produced a candidate construction of a global selector with a constant depending on \((\varepsilon,r)\) but not on the ambient number of coordinates.

This does not solve the unrestricted theorem because the constants may grow with \(r\).

## 3.1 Compare incompatible coordinate partitions by common refinement

For a coordinate partition \(\Pi\), let
\[
\mathbb E_\Pi
\]
be the coordinate pinching that deletes all matrix entries crossing two different blocks of \(\Pi\).

Coordinate pinchings are trace-norm contractions and commute with each other.

If \(K\) is block diagonal over \(\Pi\) and \(L\) is block diagonal over \(\Sigma\), define
\[
\widetilde K=\mathbb E_\Sigma K,
\qquad
\widetilde L=\mathbb E_\Pi L.
\tag{3.1}
\]
Then both are block diagonal over the common refinement
\[
\Pi\wedge\Sigma.
\]

Because \(K=\mathbb E_\Pi K\) and \(L=\mathbb E_\Sigma L\),
\[
\boxed{
\begin{aligned}
\|K-\widetilde K\|_1
&\le2\|K-L\|_1,\\
\|L-\widetilde L\|_1
&\le2\|K-L\|_1,\\
\|\widetilde K-\widetilde L\|_1
&\le\|K-L\|_1.
\end{aligned}
}
\tag{3.2}
\]
The final line is
\[
\widetilde K-\widetilde L
=
\mathbb E_\Pi\mathbb E_\Sigma(K-L).
\]

Thus one does not need the potentially huge common coarsening of \(\Pi\) and \(\Sigma\).

## 3.2 Inductively impose exact refinement compatibility

Assume local selectors have already been constructed on all blocks of size \(<n\), with the property that when a block becomes reducible, the \(n\)-block selector agrees exactly with the product of the lower-dimensional selectors.

On the closed reducible subset \(R_n\) of \(n\times n\) kernels, the lower-dimensional product rules define the boundary value
\[
B_n(x).
\]
The pinching comparison (3.2), together with the homogeneous block estimate below, is intended to prove that \(B_n\) is Lipschitz on the whole reducible subset, not merely on each fixed partition stratum.

Extend each edge coordinate off \(R_n\) by McShane:
\[
z_e(x)
=
\inf_{y\in R_n}
\bigl[
B_{n,e}(y)+A_n d(x,y)
\bigr].
\tag{3.3}
\]
Then project the vector \(z(x)\) in Euclidean norm onto the original finite-dimensional flow fiber
\[
\mathcal F_n(x).
\]
On \(R_n\), \(z=B_n\) is already feasible, hence projection fixes it and exact refinement compatibility is retained.

For fixed \(n\), the Euclidean projection onto this fixed-normal polytope is piecewise affine in center and right-hand sides. Each active-set formula has the form
\[
z
-
N_I^{\mathsf T}
(N_IN_I^{\mathsf T})^{-1}
(N_Iz-y_I).
\tag{3.4}
\]
There are finitely many active sets for fixed \(n\); hence a finite Lipschitz constant exists. Dependence on \(n\) is allowed because \(r\) is frozen.

## 3.3 Homogeneous local estimate

For an unnormalized positive rank-at-most-one matrix
\[
X=wR,
\]
define
\[
H(A,X)=w\phi(A,R),
\qquad H(A,0)=0.
\tag{3.5}
\]
If the normalized local selector has Lipschitz constant \(L\), the candidate homogeneous estimate is
\[
\boxed{
\|H(A,X)-H(B,Y)\|_1
\le
L\min(w,z)\|A-B\|_1
+
(1+2L)\|X-Y\|_1.
}
\tag{3.6}
\]
This avoids division by a vanishing block weight.

## 3.4 Global product rule

For a compatible partition \(\Pi\), block \(B\in\Pi\), and \(i\in B\), define
\[
\Psi^\Pi(K,P)(S,i)
=
H(K_B,P_B)(S\cap B,i)
\,
p_{K_{B^c}}(S\setminus B).
\tag{3.7}
\]
Block weights sum to one, and trace-norm pinching controls
\[
\sum_B\|P_B-Q_B\|_1
\]
without a factor equal to the number of blocks.

For a common partition, the candidate global estimate has the form
\[
\|\Psi^\Pi(K,P)-\Psi^\Pi(L,Q)\|_1
\le
(L+\varepsilon^{-1})\|K-L\|_1
+
(1+2L)\|P-Q\|_1.
\tag{3.8}
\]
The three-step pinching comparison (3.2) then compares arbitrary canonical partitions while keeping the constant dependent only on \((\varepsilon,r)\).

### Candidate conclusion

For every fixed \(r\), the bounded-component theorem should hold with some finite
\[
C_{\varepsilon,r},
\]
independent of the ambient coordinate dimension.

### Audit obligations for Section 3

- prove the reducible-boundary rule is globally well defined on intersections of multiple partition strata;
- verify the fixed-dimensional projection lemma with all equality and capacity constraints;
- verify (3.6) at zero block weight;
- recheck that the product-flow divergence and capacity calculations remain exact after the inductive extension.

---

# 4. Candidate exact three-input inconsistency in the full original fibers

This candidate example is intended to prove a genuine finite-family phenomenon stronger than pairwise optimizer instability:

> each pair of fibers attains a smaller optimal distance than is simultaneously attainable by one triple of flows.

The ratio obtained is only \(13/12\), so it does not disprove the dimension-free selector theorem.

Take
\[
0<\eta\le\frac1{10},
\qquad
\varepsilon=\frac25,
\qquad
P=\frac13\mathbf1\mathbf1^{\mathsf T}.
\]
Let
\[
K_0
=
\frac12I
+
\frac{\eta}{21}
\begin{pmatrix}
-11&13&-2\\
13&-2&-11\\
-2&-11&13
\end{pmatrix},
\tag{4.1}
\]
and let
\[
K_a=\sigma^aK_0\sigma^{-a},
\qquad
\sigma=(123).
\tag{4.2}
\]
The claimed spectrum is
\[
\left\{
\frac12-\eta,\frac12,\frac12+\eta
\right\},
\]
and all three kernels commute with the same \(P\).

The pairwise kernel trace distance is
\[
\|K_a-K_b\|_1=2\sqrt3\,\eta
\qquad(a\ne b).
\tag{4.3}
\]

Put
\[
q=\frac14-\eta^2,
\qquad
r=\frac1{12}+\frac{\eta^2}{3}.
\tag{4.4}
\]
A candidate flow \(F_0\) is defined by assigning mass \(q/3\) to the six outermost edges, while the six middle-layer edges
\[
1\to12,\;
2\to12,\;
2\to23,\;
3\to23,\;
3\to13,\;
1\to13
\]
carry
\[
r(1,1,1,1,1,1)
+
\frac{\eta}{21}(-8,-5,3,8,5,-3).
\tag{4.5}
\]
Set
\[
F_a=\sigma^aF_0.
\tag{4.6}
\]

The continuation arithmetic gives the pairwise optimum
\[
\boxed{
\inf_{f_a\in\mathcal F(K_a,P),\,f_b\in\mathcal F(K_b,P)}
\|f_a-f_b\|_1
=
\frac{48\eta}{21}.
}
\tag{4.7}
\]
The lower bound comes from the generic divergence inequality
\[
\|f-g\|_1
\ge
\frac12\|\operatorname{div}f-\operatorname{div}g\|_1,
\tag{4.8}
\]
and an explicit cycle adjustment is claimed to attain equality.

For three simultaneous choices, cyclic averaging reduces the problem to
\[
(g,\sigma g,\sigma^2g)
\]
without increasing the maximum pairwise distance.

The twelve edges split into four three-cycles \(A,B,C,D\). For a cyclically averaged triple,
\[
\|g-\sigma g\|_1
=
2\sum_{O=A,B,C,D}
\operatorname{range}(g|_O).
\tag{4.9}
\]

Use the vertex potential
\[
\phi(\varnothing)=\phi(E)=\frac23,
\]
\[
(\phi(1),\phi(2),\phi(3))=(1,1,0),
\]
\[
(\phi(12),\phi(23),\phi(13))=(0,1,1).
\tag{4.10}
\]
Its gradient on the four cyclic edge orbits is claimed to be
\[
(1/3,1/3,-2/3),
\quad
(-1,0,1),
\quad
(0,-1,1),
\quad
(-1/3,-1/3,2/3).
\tag{4.11}
\]
Each vector sums to zero and has positive mass at most one, so its pairing with an orbit is bounded by that orbit's range.

The candidate divergence pairing is
\[
\sum_Sb_{K_0,P}(S)\phi(S)
=
\frac{26\eta}{21}.
\tag{4.12}
\]
Combining (4.9)–(4.12) yields
\[
\boxed{
\inf_{f_a\in\mathcal F(K_a,P)}
\max_{a<b}\|f_a-f_b\|_1
=
\frac{52\eta}{21}.
}
\tag{4.13}
\]
Thus
\[
\frac{52}{48}=\frac{13}{12}
\]
is the candidate strict finite-family incompatibility ratio.

### Significance

If independently verified, this would rigorously establish that pairwise optimal transports cannot simply be glued into a simultaneous finite-list solution, even for one fixed projector and arbitrarily nearby kernels.

It still does **not** imply divergence of the required global Lipschitz constant.

---

# 5. Candidate obstruction to affine dependence on the projector

This section targets a tempting but overly rigid proof strategy: make the selected flow affine in \(P\).

Let
\[
u=(1,1,1,1)/2,
\qquad
H=u^\perp,
\]
and
\[
K=\frac12I+tuu^*,
\qquad
0<t\le\frac12-\varepsilon.
\tag{5.1}
\]
Every rank-one projector \(P=vv^*\) with \(v\in H\) commutes with \(K\).

Assume an affine flow rule exists on this degenerate eigenspace. After absorbing the constant term into the identity on \(H\), write each edge as
\[
f_e(P)=\operatorname{tr}(A_eP).
\tag{5.2}
\]
Nonnegativity for every pure state in \(H\) implies
\[
A_e\succeq0
\quad\text{on }H.
\tag{5.3}
\]

The coordinate-mass identity requires
\[
\sum_{e\text{ adding }i}A_e
=
(\Pi_He_i)(\Pi_He_i)^*.
\tag{5.4}
\]
The right side has rank one. A sum of positive semidefinite operators equal to a rank-one operator forces every summand to be a nonnegative scalar multiple of that same rank-one operator. Hence every selected edge mass can depend only on
\[
P_{ii}.
\tag{5.5}
\]

Now take
\[
v=(1,1,-1,-1)/2,
\qquad
w=(1,-1,1,-1)/2.
\tag{5.6}
\]
Their rank-one projectors have the same diagonal:
\[
P_{ii}=Q_{ii}=1/4.
\]
Thus an affine rule constrained by (5.5) would produce the same flow.

But the directional derivative of the inclusion probability for \(\{1,2\}\) is claimed to differ:
\[
D_{vv^*}\det K_{\{1,2\}}
=
\frac14,
\]
\[
D_{ww^*}\det K_{\{1,2\}}
=
\frac14+\frac t4.
\tag{5.7}
\]
Therefore their divergences differ, contradiction.

### Candidate conclusion

No globally feasible selector can be affine in \(P\) on this whole degenerate eigenspace.

This does not rule out nonlinear Lipschitz selectors.

---

# 6. Candidate negative example for the unconstrained weighted current

The weighted selector in Section 2 retains nonnegativity in the feasible set. This section records a candidate example showing why one cannot omit that constraint and merely solve the weighted divergence equation.

Take
\[
P=\frac13\mathbf1\mathbf1^{\mathsf T},
\]
\[
K
=
\frac1{740}
\begin{pmatrix}
151&141&78\\
141&448&-219\\
78&-219&511
\end{pmatrix},
\qquad
\varepsilon=\frac1{20}.
\tag{6.1}
\]
The claimed eigenvalues are
\[
\frac12,\quad\frac{19}{20},\quad\frac1{20}.
\]

The unconstrained weighted minimum-energy divergence solution has the electrical form
\[
f=wD^{\mathsf T}\phi.
\tag{6.2}
\]
Ground the empty-set potential at zero and order the other vertices as
\[
(1,2,3,12,23,13,123).
\]
After scaling all weights by \(44400\), let \(L\) be the resulting grounded weighted Laplacian.

The continuation produced the rational approximate potential
\[
\widehat\phi
=
\frac1{100000}
(149100,16660,18750,141495,184487,171998,200715).
\tag{6.3}
\]
The claimed exact residual satisfies coordinatewise absolute value \(<1\).

For
\[
q=(1,1,1,107/100,107/100,107/100,111/100),
\]
the claimed exact multiplication gives
\[
Lq\ge310\mathbf1.
\tag{6.4}
\]
A discrete maximum-principle comparison then gives
\[
|\phi-\widehat\phi|
\le
q/310.
\tag{6.5}
\]

Hence
\[
\phi(12)-\phi(1)
\le
-\frac{7605}{100000}
+
\frac{207}{31000}
=
-\frac{43011}{620000}
<0.
\tag{6.6}
\]
Thus the edge \(1\to12\) carries negative flow.

The continuation also claims all upward potential differences have absolute value \(<2\), which keeps the positive side below the original DPP outgoing capacity. Thus the failure is specifically nonnegativity, not capacity.

### Significance

The explicit weighted optimization in Section 2 must minimize over the actual nonnegative feasible fiber. Replacing that constrained problem by the unconstrained electrical solution is invalid.

---

# 7. Candidate obstruction to arbitrary low-energy repair under varying projectors

A further continuation argument targets a possible proof strategy for varying \(P\):

> perhaps every flow with uniformly bounded weighted energy and strict interior slack can be repaired stably when \(P\) changes.

The candidate counterexample says this stronger statement is false.

At the scalar kernel
\[
K=\frac12I,
\]
one can choose full-support commuting projectors \(P_n,Q_n\) with
\[
\|P_n-Q_n\|_1\to0,
\tag{7.1}
\]
and flows
\[
f_n\in\mathcal H(K,P_n)
\]
such that for a fixed small \(\theta>0\),
\[
(1-2\theta/3)J_{P_n}
\le
f_n
\le
(1+2\theta/3)J_{P_n},
\tag{7.2}
\]
while
\[
\sum_e\frac{f_n(e)^2}{w_{P_n}(e)}
\le
1+\frac{4\theta^2}{9}.
\tag{7.3}
\]
Thus the flows are uniformly interior and arbitrarily close in energy to the canonical minimum as \(\theta\to0\).

Nevertheless the continuation construction claims
\[
\inf_{g\in\mathcal F(K,Q_n)}
\|f_n-g\|_1
\ge
c\theta
\tag{7.4}
\]
for an absolute \(c>0\), uniformly along the dimension-growing family.

The construction uses a balanced signed coordinate partition and inserts a six-edge circulation between three layers. A bounded linear functional detects the circulation in \(f_n\), while the target projector has vanishing mass in one distinguished coordinate and the coordinate-mass identity forces the same functional to vanish asymptotically for every target flow.

### Significance

Even strong relative interior slack plus nearly minimal weighted energy would not be enough to repair *arbitrary* old flows under varying projectors.

This is not a selector-independent obstruction to the original theorem, because a specially chosen selector such as the scalar canonical flow can avoid the inserted circulation.

### Audit status

The detailed finite-\(n\) formulas for this family were not preserved in the initial breakpoint archive. This subsection should therefore be treated as a route note, not as a self-contained proof, until those formulas are reconstructed and checked.

---

# 8. Current mathematical boundary after this continuation

If Sections 1–6 survive independent audit, the breakpoint would sharpen to:

\[
\boxed{
\begin{array}{l}
\text{fixed }P:
\text{ full-fiber pairwise repair is dimension-free;}\\[2mm]
\text{fixed }P:
\text{ one globally coherent selector has a dimension-free }1/2\text{-Hölder modulus;}\\[2mm]
\text{fixed component bound }r:
\text{ a refinement-compatible Lipschitz selector exists with }C_{\varepsilon,r};\\[2mm]
\text{finite-family incompatibility:
pairwise optimal choices need not glue exactly;}\\[2mm]
\text{varying, delocalized }P:
\text{ the dimension-free Lipschitz theorem is still open.}
\end{array}
}
\]

The remaining positive obligation is still to control **one nonlinear selector under varying projectors with exponent one**.

The remaining negative obligation is still to force the Lipschitz ratio of **every** simultaneous choice to diverge.

---

# 9. Review priority

Suggested independent-review order:

1. Section 1: full-fiber fixed-\(P\) repair.
2. Section 4: exact three-input finite-family certificate.
3. Section 5: affine-in-\(P\) obstruction.
4. Section 6: negative edge of unconstrained weighted current.
5. Section 2: weighted selector and \(1/2\)-Hölder estimate.
6. Section 3: bounded-component induction.
7. Section 7: reconstruct the missing explicit formulas before audit.

No section should be promoted to certified status merely because the algebra looks plausible.
