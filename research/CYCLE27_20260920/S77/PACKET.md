# S77 — Cycle27 mathematical research

## Research here; no Work routing

You must NOT attempt to route, redirect, hand off, or instruct the user to use Work, another task/chat, or another agent. This is mathematical derivation in THIS chat. A checkout or external execution environment is not a prerequisite. If access/export fails, use these explicit objects and deliver readable complete mathematics in chat.

Think for at least 120 minutes, unless you achieve major progress earlier. Do not invent elapsed time or idle to fill it. Major progress requires a proved reusable tool, a decisive model-valid obstruction with a useful replacement, or a closed theorem; a survey, renamed remainder or favorable numerical samples is insufficient.

Frozen original target: Q_rho(i,i)=rho, Q_rho(i,j)=sin(pi*rho*(i-j))/(pi*(i-j)); K_N=aI+cQ_rho,N, 0<rho,c<1, 0<a<1-c. Q_N is a true finite compression, a contraction generally NOT a projection. H_N is full configuration Shannon entropy in nats, h=lim H_N/N. The goal is h concave in a for every fixed rho,c and all legal a, particularly the entire c in(37/40,1). Derivatives hold rho,c fixed. On a compact legal interval J set delta=min_(a in J) min(a,1-a-c)>0. Constants need not be uniform at c=1, but their dependence and proved coverage must be explicit. A narrow parameter region or midpoint theorem is not completion of the global target.

Construct a TOOL with explicit input, hypotheses, output inequality, falsification tests and a quantitative interface back to ORIGINAL Shannon entropy. Theory and transferable mechanisms from other fields are central; check original-source hypotheses. Do not add hidden assumptions, discard rare words, replace actual weights by independent substitutes, differentiate o(N) entropy-value errors, or substitute count/spectral entropy. A useful intermediate theorem is welcome if its remaining gap is honestly stated. Label new lemmas KNOWN/PROVED/OPEN/EQUIVALENT_BLOCKER. Do not present an equivalent reformulation as a solved weaker lemma.

Return English RESULT.md or full in-chat proof with PROVED/DISPROVED/INCOMPLETE separated, exact scope and remaining payment. Computational claims need reproducible source and actual execution status; finite diagnostics are not all-size proofs. No hash/SHA/checksum acceptance gate, no delegation, shared-state edits or PR merges.

## S77 ownership: Fisher-compensated cut estimate after S74

S76 is already working on the cyclic exterior-channel overlap budget. S78 owns lifting S75 stars to multiple centers. Your task is the ACTUAL TOEPLITZ block-information route, using audited S74 (RL01 PR64) and S71 (PR60), not either neighboring task.

For adjacent A,B put M=H_A+H_B-H_AB, F_N=-H_N''. For P=P_K(y), R_y=(K-diag(1-y))^-1, S=tr R_y and ell=log(P/(P_A P_B)),
M''=D_F+C_acc,
D_F=E S^2-E(E[S|Y_A])^2-E(E[S|Y_B])^2>=0,
C_acc=E[((tr R)^2-tr(R^2))*ell].
The Fisher inequality is accepted via score monotonicity and DPP negative association. The acceleration is NOT nonnegative: for a two-site equal-marginal law with marginal u=a+c*rho, d=|K_12|^2 and r=u(1-u)+d, C_acc=2log(1-d/r^2)<0. PR63's945-model diagnostic found negative C_acc but positive M'' throughout; max(-C_acc/D_F) about.683214 is NOT a universal theorem.

S74 supplies a new accepted representation and size-free cut bound. For sigma_i=2y_i-1 and b_i=sigma_i R_ii-1,
W(K,y)=sum_(i<j) sigma_i sigma_j log[1-sigma_i sigma_j |R_ij|^2/(b_i b_j)],
C_acc=2 E_P[W(K,Y)-W(K_A directsum K_B,Y)].
For every strict Hermitian contraction along the common scalar shift,
|C_acc|<=B_delta ||K_AB||_HS^2,
B_delta=4L_delta/delta^3+2/(r_delta^4 delta^4)<=6delta^-12,
r_delta=delta/(1-delta),
L_delta=2/(r_delta^2 delta)+1/(r_delta^5 delta^2)+1/(r_delta^6 delta^3).
The proof uses the actual kernel interpolation K_t=diag(K_A,K_B)+t offdiag(K_AB), not a probability mixture. It preserves delta by sign conjugation/pinching. The complete proof is attached.

Its exact accumulated charge is important: for q leaves of length L,
sum_merges ||K_AB||_HS^2=(c^2/2)[tr Q_(qL)^2-q tr Q_L^2].
Writing D_rho,L=tr(Q_L-Q_L^2), a seed F_L>=f_L throughout J gives a rate chord bound with curvature margin
kappa_L=f_L/L-B_delta*c^2*D_rho,L/(2L).
This follows by integrating finite-volume curvature then taking entropy-value limits, with no derivative-limit shortcut. D_rho,L=O(log L). Merely increasing L without controlling f_L is not a certificate.

At rho=.5,c=.95,J=[.02,.03], B_delta about8.65e20 makes the two-site margin about-5.81e19. The theorem is valid but presently pays only extreme densities, e.g.min(rho,1-rho)<=1e-21 on c[.925,.95],a[.02,.03]. A small numerical constant improvement would not change this bottleneck.

## New obligation

Build a relative or signed cut inequality that RETAINS D_F while estimating C_acc, rather than taking a wordwise absolute gradient and discarding all Fisher compensation. One candidate output is
D_F+C_acc >= -B_eff(c,rho,J) ||K_AB||_HS^2
with an affordable B_eff derived from actual weights; another is
-C_acc <= theta D_F + E_cut,
with theta<=1 and a rigorously affordable accumulated E_cut. These are candidates to prove or refute, not premises. A sharper exact decomposition into locally paid Fisher/odds terms is welcome. State which lemma is strictly weaker than full M''>=0 and how its residual sums through the ACCEPTED merge-tree formula.

Promising seeds include a weighted cofactor integration-by-parts pairing between the cut odds change and conditional-score variance; a variational projection/Dirichlet representation that pays the negative log-odds term before bounding gradients; or a scale-dependent cut interpolation with signed relative entropy derivatives. Exploit actual sine geometry if a general-contraction claim is false. Do not restart S74's absolute-norm proof with only cosmetically improved constants.

Known obstruction at the genuine six-site sine base point rho=.5,c=.95,a=.025,A=1:3,B=4:6: the mixed diagonal Hessian entry for sites1 and6 is negative (about-.000379092), while D_F about32.59075, C_acc about-18.84098 and M'' about13.74977. Thus entrywise positivity of all coordinate rectangle defects is false; full-direction compensation remains possible. The author's exact interval attachments have now arrived and are undergoing independent replay; the analytic theorem is already audited. Do not depend on un-replayed last decimal digits.

Success requires a genuinely improved structural payment with explicit parameter/size costs and a tested path to a non-extreme-density rate certificate, or a decisive obstruction to the proposed relative inequality plus a useful narrower replacement. If a new bound still cannot pay even the audited seed, show the remaining deficit; do not claim closure. Do not infer rate nonconcavity from failure of this sufficient method.


# Source attachments


## S74_RESULT.md
Source: research/CYCLE26_20260920/S74/S74_VISIBLE_RESULT.md

# RESULT.md — Quadratic-cut acceleration control and an actual-law rate bridge

:chatgpt-content-reference{index="2"} · :chatgpt-content-reference{index="3"} · :chatgpt-content-reference{index="4"}

**The unrestricted all-density high-contrast target remains INCOMPLETE.** The results obtained here are an all-size actual-law acceleration estimate, exact accounting of its accumulation through blocking, a paid but extremely narrow high-contrast entropy-rate theorem, and a certified obstruction to entrywise positivity of mixed diagonal information derivatives.

The principal estimate is
\[
\boxed{|C_{\mathrm{acc}}|\le B_\delta\|K_{AB}\|_{\mathrm{HS}}^2,
\qquad B_\delta\le 6\delta^{-12}.}
\]
Its cost telescopes into the finite-compression leakage
\[
\operatorname{tr}(Q_{\rho,L}-Q_{\rho,L}^2).
\]
This is a proved bound on the unresolved term, not an equivalent reformulation.

The accepted Fisher inequality \(D_F\ge0\) and the audited two-site seed are used as inputs from the supplied packet. Neither S71 nor the affine-mixture obstruction is re-proved; S73 is not used. citeturn351960view0turn374335view0

---

## 1. The mathematical tool

### Input class

Let
\[
K(a)=T+aI,\qquad
\delta I\preceq K(a)\preceq(1-\delta)I
\quad(a\in J),
\]
where \(T\) is Hermitian, \(J\) is a compact interval, and \(0<\delta\le1/2\).

Partition the finite ground set into blocks \(A,B\), and put
\[
X=K_{AB}=T_{AB}.
\]
Thus the cross-block matrix is independent of \(a\). All entropies below are full configuration Shannon entropies in nats.

Define
\[
r=\frac{\delta}{1-\delta},
\]
\[
L_\delta=
\frac{2}{r^2\delta}
+\frac{1}{r^5\delta^2}
+\frac{1}{r^6\delta^3},
\]
and
\[
\boxed{
B_\delta=\frac{4L_\delta}{\delta^3}
+\frac{2}{r^4\delta^4}.
}
\tag{1}
\]

### Output inequality

For the actual DPP law,
\[
\boxed{
|C_{\mathrm{acc}}(a)|
\le B_\delta\|X\|_{\mathrm{HS}}^2.
}
\tag{2}
\]
Consequently, using the accepted \(D_F\ge0\),
\[
\boxed{
M''(a)\ge-B_\delta\|X\|_{\mathrm{HS}}^2.
}
\tag{3}
\]

The constant is independent of the block sizes. It is conservative in the contraction gap.

The proof below retains every mixed coordinate contribution and every configuration.

---

## 2. Cofactor integration by parts

Write \(s_i=2y_i-1\). Differentiation with respect to the single diagonal coordinate \(K_{ii}\) gives
\[
\partial_iP_K(y)
=s_iP_{K_{-i}}(y_{-i}),
\]
and, for \(i\ne j\),
\[
\partial_i\partial_jP_K(y)
=s_is_jP_{K_{-\{i,j\}}}(y_{-\{i,j\}}).
\tag{4}
\]
Also \(\partial_i^2P_K(y)=0\).

These are cofactor identities for the actual atoms. The deleted-coordinate probabilities are the actual DPP marginals.

For a function \(g\), define
\[
\Delta_{ij}g(z)
=g(1,1,z)+g(0,0,z)-g(1,0,z)-g(0,1,z).
\]
Along the common identity shift, (4) implies
\[
\sum_yP_K''(y)g(y)
=
2\sum_{i<j}
\mathbb E_{Y_{-\{i,j\}}}\Delta_{ij}g.
\tag{5}
\]
Here \(g\) is frozen when applying this identity.

Define the conditional log-odds potential
\[
W(K,y)=\sum_{i<j}\Delta_{ij}\log P_K(y).
\tag{6}
\]
Each summand is independent of the displayed pair of bits, so its expectation under the deleted-coordinate marginal equals its expectation under the full law.

Let
\[
K^{(0)}=K_A\oplus K_B.
\]
Apply (5) to
\[
\ell=\log P_K-\log P_{K_A}-\log P_{K_B}
\]
in the accepted acceleration formula. This gives
\[
\boxed{
C_{\mathrm{acc}}
=
2\mathbb E_{P_K}
\big[W(K,Y)-W(K^{(0)},Y)\big].
}
\tag{7}
\]

For pairs inside a block, this subtracts the corresponding marginal conditional log odds. For cross-block pairs, the marginal differences vanish. Thus the moving marginal references have not been discarded.

Identity (7) is preparatory. The substantive estimate is the following pointwise cut bound.

---

## 3. A dimension-independent pointwise cut estimate

### 3.1 Masked resolvents and conditional odds

Fix a configuration \(y\), and write
\[
R=\bigl(K-\operatorname{diag}(1-y)\bigr)^{-1},
\qquad
b_i=s_iR_{ii}-1.
\]
The masked matrix equals
\[
\frac12\operatorname{diag}(s_i)
+\left(K-\frac12I\right).
\]
Its smallest singular value is at least \(\delta\), hence
\[
\|R\|_{\mathrm{op}}\le\delta^{-1}.
\tag{8}
\]

If
\[
q_i=P(Y_i=y_i\mid Y_{-i}=y_{-i}),
\]
the first cofactor identity gives
\[
R_{ii}=\frac{s_i}{q_i}.
\]
Applying (8) both before and after flipping bit \(i\) proves
\[
\delta\le q_i\le1-\delta,
\qquad
r\le b_i=\frac{1-q_i}{q_i}\le r^{-1}.
\tag{9}
\]
This holds for every word.

For \(i\ne j\), put
\[
\sigma_{ij}=s_is_j,
\qquad
x_{ij}=\frac{|R_{ij}|^2}{b_ib_j}.
\]
If \(y^i\) and \(y^{ij}\) denote the corresponding flipped words, the determinant lemma gives
\[
\frac{P(y)P(y^{ij})}{P(y^i)P(y^j)}
=1-\sigma_{ij}x_{ij}.
\]
When the two bits agree, this is the conditional odds ratio; otherwise it is its reciprocal. Therefore
\[
\boxed{
W(K,y)=
\sum_{i<j}\sigma_{ij}
\log(1-\sigma_{ij}x_{ij}).
}
\tag{10}
\]

For \(\sigma_{ij}=1\), the ratio is a ratio of two one-site conditional odds. By (9), it is at least \(r^2\). For \(\sigma_{ij}=-1\), the denominator is \(1+x_{ij}\ge1\). Thus
\[
1-\sigma_{ij}x_{ij}\ge r^2.
\tag{11}
\]

### 3.2 An operator-norm bound for the gradient

Treat the right side of (10) as a function of the Hermitian matrix \(R\), with the signs fixed. Its differential is
\[
dW=\operatorname{tr}(G\,dR),
\]
where, for \(i\ne j\),
\[
G_{ij}
=
-\frac{R_{ij}}
{b_ib_j(1-\sigma_{ij}x_{ij})},
\tag{12}
\]
and
\[
G_{ii}
=
\frac{s_i}{b_i}
\sum_{j\ne i}
\frac{x_{ij}}{1-\sigma_{ij}x_{ij}}.
\tag{13}
\]

I claim
\[
\boxed{\|G\|_{\mathrm{op}}\le L_\delta.}
\tag{14}
\]

Let \(D=\operatorname{diag}(b_i^{-1})\). Split the off-diagonal part of \(G\) into
\[
-\operatorname{offdiag}(DRD)
\]
and a remainder. The first part has operator norm at most
\[
2\|D\|_{\mathrm{op}}^2\|R\|_{\mathrm{op}}
\le 2r^{-2}\delta^{-1}.
\]

Using
\[
\frac1{1-\sigma x}-1
=\frac{\sigma x}{1-\sigma x},
\]
the remainder has entries bounded by
\[
r^{-6}|R_{ij}|^3.
\]
For every row,
\[
\sum_j|R_{ij}|^3
\le
\left(\max_j|R_{ij}|\right)\sum_j|R_{ij}|^2
\le\delta^{-3}.
\]
The Hermitian remainder therefore has operator norm at most
\[
r^{-6}\delta^{-3}.
\]

Finally, (13) gives
\[
|G_{ii}|
\le r^{-5}\sum_j|R_{ij}|^2
\le r^{-5}\delta^{-2}.
\]
Adding the three estimates proves (14).

This step replaces the apparent number of mixed terms by operator and row-square bounds. No factor of the number of sites remains.

### 3.3 Quadratic dependence on the cut

At a fixed \(a\), consider
\[
K_t=K_A\oplus K_B+tE,
\qquad
E=
\begin{pmatrix}
0&X\\
X^*&0
\end{pmatrix},
\qquad 0\le t\le1.
\]
For \(U=I_A\oplus(-I_B)\),
\[
K_t=\frac{1+t}{2}K+\frac{1-t}{2}UKU^*.
\]
Every \(K_t\) therefore has the same contraction margin \(\delta\).

This is an interpolation of kernels. It is **not** an affine mixture of endpoint probability laws.

Write
\[
R_t=\bigl(K_t-\operatorname{diag}(1-y)\bigr)^{-1},
\qquad x=\|X\|_{\mathrm{HS}}.
\]
The block resolvent equation gives
\[
(R_t)_{AB}
=-t(R_0)_{AA}X(R_t)_{BB},
\]
so
\[
\|(R_t)_{AB}\|_{\mathrm{HS}}
\le t\delta^{-2}x.
\tag{15}
\]

Because \(R_t'=-R_tER_t\),
\[
\|(R_t')_{AA}\|_1+\|(R_t')_{BB}\|_1
\le4t\delta^{-3}x^2.
\tag{16}
\]
For example,
\[
(R_t')_{AA}
=-(R_t)_{AA}X(R_t)_{BA}
 -(R_t)_{AB}X^*(R_t)_{AA},
\]
and each term is bounded using (8), (15), and
\[
\|UV\|_1\le\|U\|_{\mathrm{HS}}\|V\|_{\mathrm{HS}}.
\]

Also
\[
\|R_t'\|_{\mathrm{HS}}
\le\delta^{-2}\|E\|_{\mathrm{HS}}
=\sqrt2\,\delta^{-2}x.
\]
Since the two off-diagonal blocks of a Hermitian matrix have equal Hilbert–Schmidt norm,
\[
\|(R_t')_{AB}\|_{\mathrm{HS}}
\le\delta^{-2}x.
\tag{17}
\]

Equations (11), (12), and (15) imply
\[
\|(G_t)_{AB}\|_{\mathrm{HS}}
\le r^{-4}\|(R_t)_{AB}\|_{\mathrm{HS}}
\le tr^{-4}\delta^{-2}x.
\tag{18}
\]

Pair the diagonal blocks of \(\operatorname{tr}(G_tR_t')\) using operator/trace norms, and the off-diagonal blocks using Hilbert–Schmidt norms. Equations (14), (16)–(18) yield
\[
\left|\frac{d}{dt}W(K_t,y)\right|
\le
\left(
4tL_\delta\delta^{-3}
+2tr^{-4}\delta^{-4}
\right)x^2.
\]
Integration gives the pointwise bound
\[
\boxed{
|W(K,y)-W(K^{(0)},y)|
\le
\left(
2L_\delta\delta^{-3}
+r^{-4}\delta^{-4}
\right)\|X\|_{\mathrm{HS}}^2.
}
\tag{19}
\]

Taking the expectation in (7) proves (2). The accepted Fisher inequality proves (3).

Finally, \(r\ge\delta\) implies
\[
\begin{aligned}
B_\delta
&\le
8\delta^{-6}+4\delta^{-10}
+4\delta^{-12}+2\delta^{-8}\\
&=
\delta^{-12}
\left(4+4\delta^2+2\delta^4+8\delta^6\right)
\le6\delta^{-12},
\end{aligned}
\tag{20}
\]
because \(\delta\le1/2\).

This completes the all-size acceleration estimate.

---

## 4. Exact accumulation through blocking

Fix a leaf size \(L\), and merge \(q\) adjacent leaves into an interval of length \(qL\).

Every unordered pair of sites in different leaves lies across exactly one cut in a binary merge tree: the cut at its lowest common ancestor. Therefore
\[
\boxed{
\sum_{\text{merges}}\|K_{AB}\|_{\mathrm{HS}}^2
=
\frac{c^2}{2}
\left[
\operatorname{tr}Q_{\rho,qL}^2
-q\operatorname{tr}Q_{\rho,L}^2
\right].
}
\tag{21}
\]
Thus every mixed cross-leaf contribution is charged once, not once per scale.

Applying (3) at every merge, with the same \(B_\delta\), gives
\[
F_{qL}(a)\ge qF_L(a)
-\frac{B_\delta c^2}{2}
\left[
\operatorname{tr}Q_{\rho,qL}^2
-q\operatorname{tr}Q_{\rho,L}^2
\right].
\tag{22}
\]

The finite sine compression is a contraction, not generally a projection. Writing
\[
q_r=\frac{\sin(\pi\rho r)}{\pi r},
\qquad q_0=\rho,
\]
we have
\[
\frac1N\operatorname{tr}Q_{\rho,N}^2
=
\sum_{|r|<N}
\left(1-\frac{|r|}{N}\right)|q_r|^2
\longrightarrow
\sum_{r\in\mathbb Z}|q_r|^2=\rho.
\tag{23}
\]
The last equality is Parseval for the indicator of a Fourier interval of length \(\rho\); square summability justifies dominated convergence.

Define
\[
D_{\rho,L}
=\operatorname{tr}(Q_{\rho,L}-Q_{\rho,L}^2),
\]
and, with \(c,\rho\) fixed,
\[
\operatorname{Gap}_\lambda f
=f((1-\lambda)a_0+\lambda a_1)
-(1-\lambda)f(a_0)-\lambda f(a_1),
\qquad \Delta=a_1-a_0.
\]

Integrate (22) while the volume is finite:
\[
\begin{aligned}
\operatorname{Gap}_\lambda H_{qL}
\ge{}&
q\operatorname{Gap}_\lambda H_L\\
&-\frac{B_\delta c^2}{4}
\left[
\operatorname{tr}Q_{\rho,qL}^2
-q\operatorname{tr}Q_{\rho,L}^2
\right]
\lambda(1-\lambda)\Delta^2.
\end{aligned}
\]
Divide by \(qL\), then use the entropy-value limits and (23). This proves the actual-law bridge
\[
\boxed{
\operatorname{Gap}_\lambda h
\ge
\frac{\operatorname{Gap}_\lambda H_L}{L}
-\frac{B_\delta c^2D_{\rho,L}}{4L}
\lambda(1-\lambda)\Delta^2.
}
\tag{24}
\]

In particular, a certified seed \(F_L(a)\ge f_L\) on the entire compact interval gives
\[
\boxed{
\operatorname{Gap}_\lambda h
\ge\frac{\kappa_L}{2}\lambda(1-\lambda)\Delta^2,
\qquad
\kappa_L=
\frac{f_L}{L}
-\frac{B_\delta c^2D_{\rho,L}}{2L}.
}
\tag{25}
\]

**The payment condition is \(\kappa_L>0\), not merely \(f_L>0\).**

No limit of \(H_N''/N\) was taken. No monotonicity of \(F_N/N\) for every \(N\), and no Dini argument, is used. The conclusion is a rate chord inequality; it does not require twice differentiability of \(h\).

For completeness, the leakage is explicitly
\[
D_{\rho,L}
=\frac2{\pi^2}
\left[
\sum_{r=1}^{L-1}\frac{\sin^2(\pi\rho r)}r
+
L\sum_{r\ge L}\frac{\sin^2(\pi\rho r)}{r^2}
\right],
\]
and
\[
D_{\rho,L}\le
\min\left\{
L\rho(1-\rho),
\frac2{\pi^2}(\log L+3)
\right\}.
\tag{26}
\]
The final accumulated penalty is exactly the one in (25), rather than an unspecified logarithmic error per merge.

---

## 5. A paid high-contrast region

### One-site seed

The observed marginal is
\[
t=a+c\rho,
\]
not the noise bias \(p_{\mathrm{noise}}=a/(1-c)\). Hence
\[
F_1(a)=\frac1{t(1-t)}\ge4,
\qquad
D_{\rho,1}=\rho(1-\rho).
\]
Equations (20) and (25) give
\[
\boxed{
\kappa_1\ge
4-3c^2\delta^{-12}\rho(1-\rho).
}
\tag{27}
\]

Therefore, for every fixed \(c\in(37/40,1)\) and every fixed compact legal interval \(J\), the tool proves strict rate concavity on the explicit density region
\[
\boxed{
\rho(1-\rho)<\frac{4\delta^{12}}{3c^2}.
}
\tag{28}
\]
For example,
\[
\min\{\rho,1-\rho\}
\le\frac{2\delta^{12}}{3c^2}
\]
implies \(\kappa_1\ge2\).

### An exact product-domain budget

Consider
\[
\frac{37}{40}\le c\le\frac{19}{20},
\qquad
\frac1{50}\le a\le\frac3{100},
\qquad
0<\min\{\rho,1-\rho\}\le10^{-21}.
\tag{29}
\]
The common contraction margin is \(\delta=1/50\). Exact rational arithmetic gives
\[
4-3\left(\frac{19}{20}\right)^2 50^{12}10^{-21}
=\frac{27353}{8192}
=3.3389892578125.
\]
Thus, for each fixed \(c,\rho\) in this region and every chord in the displayed \(a\)-interval,
\[
\boxed{
\operatorname{Gap}_\lambda h
\ge
\frac{27353}{16384}
\lambda(1-\lambda)(a_1-a_0)^2.
}
\tag{30}
\]

This is a genuine full-configuration entropy-rate certificate. The product region follows from a uniform analytic bound, not from multiplying independently audited numerical rectangles.

**Its density width is extremely small.** Equation (28) supplies corresponding regions for every fixed high contrast and compact interior parameter interval, but does not cover every density or all legal biases at a fixed positive density.

### The half-density two-site seed is not paid

At half density,
\[
D_{1/2,2}=\frac12-\frac2{\pi^2}>0.
\]
Using the accepted seed gives the candidate
\[
\kappa_2=
\frac{8+C(c^2/\pi^2)}2
-\frac{B_\delta c^2}{4}
\left(\frac12-\frac2{\pi^2}\right).
\tag{31}
\]

For \(c=19/20\), \(J=[1/50,3/100]\),
\[
B_\delta\approx8.654336163038125\times10^{20},
\]
and (31) is approximately
\[
-5.806308012581715\times10^{19}.
\]
The budget fails decisively.

Indeed, the audited bias-uniform two-site lower bound does not pay this conservative constant anywhere in the high-contrast range. There,
\[
\delta<3/80<1/4,\qquad r<1,
\]
so \(B_\delta>16384\). Also
\[
\frac{c^2}{4}\left(\frac12-\frac2{\pi^2}\right)>\frac1{20},
\]
whereas
\[
\frac{8+C(c^2/\pi^2)}2<\frac{36}{5}.
\]
Thus this particular seed budget is negative throughout that range.

Failure of this sufficient budget is not failure of rate concavity.

---

## 6. Certified actual-sine obstruction to entrywise mixed positivity

Take
\[
N=6,\quad \rho=\frac12,\quad c=\frac{19}{20},
\quad a=\frac1{40},
\]
with
\[
A=\{1,2,3\},\qquad B=\{4,5,6\}.
\]
This is the actual midpoint sine kernel
\[
K=\frac12I+\beta T,\qquad \beta=\frac{19}{20\pi},
\]
where \(T_{ii}=0\), \(T_{ij}=0\) at nonzero even distances, and
\[
T_{ij}=\frac{(-1)^{(|i-j|-1)/2}}{|i-j|}
\]
at odd distances.

Let \(\mathcal M(u,v)\) be actual DPP block information at
\[
K(u,v)=K+ue_1e_1^*+ve_6e_6^*.
\]
The base point is exactly the frozen sine law. Away from the base point, these are diagonal-coordinate perturbations, not common-identity sine shifts.

Since the directions are in different blocks,
\[
\mathcal M_{uv}(0,0)
=
\sum_y\frac{(\partial_1P_y)(\partial_6P_y)}{P_y}
+\sum_y(\partial_1\partial_6P_y)\log P_y.
\tag{32}
\]

The executed directed-integer interval certificate proves
\[
\boxed{
-0.0003790922420416860133
<
\mathcal M_{uv}(0,0)
<
-0.0003790922420416860132.
}
\tag{33}
\]

It also proves, uniformly for \(0\le u,v\le\varepsilon=10^{-10}\),
\[
-0.0003791099694534979385
<
\mathcal M_{uv}(u,v)
<
-0.0003790745146298547933
<-\frac3{10000}.
\]
Therefore
\[
\boxed{
\begin{aligned}
&\mathcal M(\varepsilon,\varepsilon)
-\mathcal M(\varepsilon,0)
-\mathcal M(0,\varepsilon)
+\mathcal M(0,0)\\
&\hspace{35mm}<-3\times10^{-24}.
\end{aligned}}
\tag{34}
\]

This falsifies the shortcut that every mixed diagonal rectangle defect can be taken nonnegative. It does **not** falsify positive semidefiniteness of the full diagonal Hessian or convexity in the common identity direction.

At precisely the same sine base point, the certificate gives
\[
32.5907519603242448559425
<D_F<
32.5907519603242448559426,
\]
\[
-18.8409844899709791046131
<C_{\mathrm{acc}}<
-18.8409844899709791046130,
\]
and hence
\[
\boxed{
13.7497674703532657513294
<M_{3,3}''
<
13.7497674703532657513295.
}
\tag{35}
\]
Thus this is **not** a finite sine counterexample to \(M''\ge0\).

### Certification method and actual execution

:chatgpt-content-reference{index="5"} was executed successfully. It uses Python integers and directed fixed-point intervals at 65 decimal places—not floating-point signs.

Its \(\pi\) enclosure uses Machin’s identity
\[
\pi=16\arctan(1/5)-4\arctan(1/239),
\]
with 90 alternating-series terms and a signed next-term remainder. Determinants use a division-free subset recurrence. Every one of the 64 six-site atoms is included and certified positive. Derivatives use (4) and actual marginal sums.

Logarithms are rescaled to \(1\le x\le2\), then evaluated through
\[
\log x=2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},
\qquad z=\frac{x-1}{x+1}.
\]
After 85 terms, the positive remainder is bounded by
\[
\frac{2z^{171}}{171(1-z^2)}.
\]
All arithmetic is rounded outward. Interval diagonals give the uniform rectangle certificate. The strictness of the printed decimal bounds was separately checked.

A separate executed diagnostic tested the odds representation, acceleration identity, and resolvent gradient on 34 finite kernels. Its maximum absolute acceleration-identity residual was about \(1.42\times10^{-14}\); its maximum normalized gradient residual was about \(3.26\times10^{-10}\). These are floating-point diagnostics, not proofs. The all-size theorem rests on the analytic argument above.

---

## 7. Hypothesis map and final ledger

| Ingredient | Exact role and scope |
|---|---|
| Accepted S71 input | Supplies \(D_F\ge0\) for the actual common identity direction. |
| Cofactor/odds argument | Finite strict Hermitian contractions; every configuration retained. |
| Cut interpolation | Preserves the same gap by pinching and sign conjugation; no probability-mixture substitution. |
| Rate transfer | Fixed \(c,\rho\), a compact legal \(a\)-interval, a uniform \(B_\delta\), and entropy-value limits after integration. |
| Paid high-contrast theorem | Requires the explicit density/gap condition (28); no unrestricted coverage is asserted. |
| Mixed-direction obstruction | An actual six-site sine base point; independent diagonal directions test the stronger polarized claim. |

| Result | Status |
|---|---|
| Dimension-independent quadratic cut-energy control of actual acceleration | **PROVED** |
| Exact accumulated cost over adjacent merge trees | **PROVED** |
| Finite-seed-to-rate chord bridge (24)–(25) | **PROVED** |
| Sparse/dense high-contrast rate region (28)–(30) | **PROVED, NARROW SCOPE** |
| Entrywise nonnegative mixed diagonal rectangles at sine base points | **DISPROVED by executed interval certificate** |
| All-size \(M_{m,n}''\ge0\) on the frozen common identity path | **INCOMPLETE; not disproved** |
| High-contrast half-density propagation from the accepted two-site seed | **INCOMPLETE; this budget does not pay it** |
| Every density and every legal interior bias for every \(37/40<c<1\) | **INCOMPLETE** |

The substantive structural result is the pointwise estimate (19), followed by the exact total charge (21). The remaining high-contrast difficulty is obtaining enough **Fisher–acceleration cancellation** to replace the conservative worst-word constant, or producing an affordable seed that pays the leakage penalty in (25).


## S74_REVIEW_PR64.md
Source: research/CYCLE26_20260920/reviews/PR64/S74_CYCLE26_REVIEW.md

# S74 Cycle26 独立数学审查

审查日期：2026-09-20（Asia/Singapore）

## 总裁决

**`VERIFIED_ANALYTIC_CORE / PAID_REGION_VALID_BUT_EXTREMELY_NARROW / AUTHOR_INTERVAL_ATTACHMENT_NOT_REPLAYED / MAIN_TARGET_INCOMPLETE`。**

正文的承重解析链通过独立验缝：cofactor 分部积分、条件 odds 表示、梯度算子范数、pinching/sign-conjugation cut 插值、无维度的二次 cut bound、相邻 merge tree 的单次收费、有限体积积分后再取熵值极限的弦桥，以及极稀疏/极稠密产品区域的显式常数，均成立。

需要一项正文级表述修补：`F_N` 在 (22) 前没有定义。全部后续符号只有在

\[
F_N(a):=-H_N''(a)
\]

时一致。按此定义，(22)–(25) 的方向和系数正确；这是缺失定义，不是证明断裂。

§6 的三个导出附件未提供，本审查没有执行作者的 directed-integer interval checker，也不认证其精确小数区间。独立 80 位 Decimal 重建得到

\[
\mathcal M_{uv}(0,0)approx-0.00037909224204168601326327,
\]

\[
D_F\approx32.59075196032424485594,
\quad C_{\rm acc}\approx-18.84098448997097910461,
\]

\[
M_{3,3}''\approx13.74976747035326575133.
\]

这些中心值严格落在作者声称区间内；其中后三项还与 SolA PR63 的独立有限枚举一致。但该重建不是 outward interval certificate，因此 §6 的精确区间状态记为 `CORROBORATED_NOT_REPLAYED`，而不是“作者 checker 已执行”。

正文没有把有限 Toeplitz compression 当成投影，也没有把一个负的 mixed Hessian 元素误写成 common identity direction 反例。全 \((0.925,1)\)、全部密度和全部合法偏置仍开放。

## 分项裁决

| 对象 | 裁决 | 说明 |
|---|---|---|
| cofactor 一、二阶恒等式 | CORRECT | 对角二阶为零，交叉二阶是删除两坐标的真实 marginal |
| (5) cofactor IBP | CORRECT | common identity 二阶导给出有序交叉项的两倍 |
| (7) acceleration 的 \(W-W_0\) 表示 | CORRECT | block 内 marginal reference 保留，cross-block marginal 差分为零 |
| masked resolvent gap | CORRECT | \(\frac12\operatorname{diag}s+(K-I/2)\) 的最小奇异值至少 \(\delta\) |
| 条件 odds 与 \(b_i\) 界 | CORRECT | 原 word 和 flip word 各给出 \(q_i\ge\delta\)、\(1-q_i\ge\delta\) |
| (10) \(W\) 的 odds 表示 | CORRECT | 同 bit 用 odds ratio，异 bit 用其倒数，\(\sigma\) 恰好修正方向 |
| (14) 梯度算子范数 | CORRECT | off-diagonal 主项、三次 remainder、diagonal 项都无尺寸因子 |
| cut interpolation | CORRECT | 是核插值，由 sign conjugation 的凸组合保 gap；不是概率律混合 |
| (15)–(19) 二次 cut bound | CORRECT | diagonal trace-norm 和 cross HS-norm 配对系数正确 |
| \(B_\delta\le6\delta^{-12}\) | CORRECT | 直接代入 \(r\ge\delta\)，最坏系数小于 6 |
| merge-tree 总收费 (21) | CORRECT | 每个不同叶的无序 pair 只在最低共同祖先 cut 收费一次 |
| finite seed 到 rate chord | CORRECT_WITH_DEFINITION_REPAIR | 需先定义 \(F_N=-H_N''\)；积分罚系数为 cost 的一半 |
| leakage 公式与上界 | CORRECT | 使用无限符号 Parseval；有限 \(Q_{\rho,N}\) 仍仅为 contraction |
| 一点 seed 区域 (28) | CORRECT | 对每个固定 \(c,\rho\) 和固定正 gap 紧区间成立 |
| 产品区域 (29)–(30) | CORRECT_EXACT | \(\delta=1/50\)，\(\kappa_1\ge27353/8192\) |
| 半密度两点 seed 预算 | CORRECTLY_FAILS_THIS_BUDGET | 只说明最坏 word 常数过贵，不说明 rate concavity 失败 |
| 六点 mixed coordinate 负号 | CORROBORATED_NOT_REPLAYED | 独立高精度重建同号同中心值；作者 exact interval 附件缺失 |
| 六点 \(C_{\rm acc}<0\)、\(M''>0\) | CROSS_CHECKED_DIAGNOSTIC | 与独立实现及 PR63 一致；不是 common-direction 反例 |
| 全高对比度、任意 \(\rho\) | INCOMPLETE | 已证区域的密度宽度约 \(\delta^{12}\)，极窄 |

## 1. 冻结对象与证据边界

完整读取 `S74_VISIBLE_RESULT.md` 全部 783 行。正文正常结束于 §7 final ledger，没有截尾。三个导出附件没有下载，按任务要求不以此阻塞解析证明审查。

本审查采用以下证据分层：

1. 正文中可逐式复核的一般证明，独立判断正确性；
2. 自行编写的标准库程序，复核有理常数、merge identity 和六点中心值；
3. SolA PR63 只用于交叉核对同一六点基点的 \(D_F,C_{\rm acc},M''\) 数值，不把其浮点扫描升级为区间证明；
4. 未取得的作者 interval checker 及其日志只记为作者声明。

S73 不作为 S74 的证明输入。S71 只提供任务明确允许接受的 common identity Fisher inequality \(D_F\ge0\)。

## 2. Cofactor IBP 与 acceleration 表示

实际 DPP atom 可写成 masked determinant。沿单个对角坐标求导，cofactor 正是删除该坐标后的实际 marginal，因此

\[
\partial_iP_K(y)=s_iP_{K_{-i}}(y_{-i}),
\]

\[
\partial_i\partial_jP_K(y)
=s_is_jP_{K_{-\{i,j\}}}(y_{-\{i,j\}}),\quad i\ne j,
\]

且 \(\partial_i^2P=0\)。common identity 二阶导为所有 \(i\ne j\) 项之和，于是对冻结的 \(g\)，

\[
\sum_yP''(y)g(y)=2\sum_{i<j}\mathbb E\Delta_{ij}g.
\]

令 \(\ell=\log P_K-\log P_{K_A}-\log P_{K_B}\)。对同一 block 内的 pair，\(\Delta_{ij}\ell\) 保留 joint conditional odds 减 marginal conditional odds；对 cross-block pair，两个 marginal 项的 mixed difference 为零。block diagonal 核 \(K^{(0)}=K_A\oplus K_B\) 的 \(W\) 正好收集两个 marginal odds。因此

\[
C_{\rm acc}=2\mathbb E_{P_K}[W(K,Y)-W(K^{(0)},Y)]
\]

成立，没有丢弃 moving marginal reference。

## 3. 条件 odds 与梯度界

masked matrix 为

\[
K-\operatorname{diag}(1-y)
=\tfrac12\operatorname{diag}(s)+(K-I/2).
\]

第一项的全部奇异值为 \(1/2\)，第二项算子范数至多 \(1/2-\delta\)，所以 inverse 的算子范数至多 \(\delta^{-1}\)。

由 cofactor 比值

\[
R_{ii}=s_i/q_i,
\]

原 word 给出 \(q_i\ge\delta\)，flip word 给出 \(1-q_i\ge\delta\)。于是

\[
r\le b_i=(1-q_i)/q_i\le r^{-1},
\qquad r=\delta/(1-\delta).
\]

两次 determinant lemma 给出 pair rectangle ratio。若 bits 相同，它就是 conditional odds ratio；若 bits 不同，它是 reciprocal。故

\[
W(K,y)=\sum_{i<j}\sigma_{ij}
\log(1-\sigma_{ij}x_{ij})
\]

且 denominator 统一不小于 \(r^2\)。

梯度 off-diagonal 项分成

\[
-\operatorname{offdiag}(DRD)
\]

和 remainder。前者算子范数至多 \(2r^{-2}\delta^{-1}\)。remainder 每项至多 \(r^{-6}|R_{ij}|^3\)，而

\[
\sum_j|R_{ij}|^3
\le\max_j|R_{ij}|\sum_j|R_{ij}|^2
\le\delta^{-3}.
\]

Hermitian row-sum bound因此给出 \(r^{-6}\delta^{-3}\)。diagonal 项由 row-square bound 给出 \(r^{-5}\delta^{-2}\)。三项合计正是 \(L_\delta\)，不含 block size。

复方向没有遗漏：对 Hermitian differential，两个 off-diagonal trace 项组合成所需的 \(2\operatorname{Re}(\overline{R}_{ij}dR_{ij})\)。

## 4. Cut interpolation 与二次依赖

令 \(U=I_A\oplus(-I_B)\)。则

\[
K_t=K_A\oplus K_B+tE
=\frac{1+t}{2}K+\frac{1-t}{2}UKU^*.
\]

两个端点有相同 contraction gap，凸组合保持 gap。这是 kernel path，不是 endpoint probability laws 的 affine mixture。

block resolvent 方程给出

\[
\|(R_t)_{AB}\|_{HS}\le t\delta^{-2}\|X\|_{HS}.
\]

再由 \(R_t'=-R_tER_t\)，两个 diagonal blocks 的 trace-norm 总和至多 \(4t\delta^{-3}\|X\|_{HS}^2\)，cross block HS-norm 至多 \(\delta^{-2}\|X\|_{HS}\)。同时

\[
\|(G_t)_{AB}\|_{HS}
\le tr^{-4}\delta^{-2}\|X\|_{HS}.
\]

diagonal 以 operator/trace norm 配对，cross block 以 HS norm 配对，得到

\[
\left|\frac d{dt}W(K_t,y)\right|
\le t(4L_\delta\delta^{-3}+2r^{-4}\delta^{-4})\|X\|_{HS}^2.
\]

积分后再乘 (7) 的因子 2，恰得

\[
|C_{\rm acc}|\le B_\delta\|X\|_{HS}^2.
\]

用 \(r\ge\delta\) 展开：

\[
B_\delta\le
8\delta^{-6}+2\delta^{-8}+4\delta^{-10}+4\delta^{-12}.
\]

括出 \(\delta^{-12}\) 后的系数在 \(0<\delta\le1/2\) 上小于 6，所以正文常数成立。

## 5. Merge tree、leakage 与弦系数

对相邻叶的任意 binary merge tree，每一对位于不同叶的无序 sites 只在最低共同祖先处分居 cut 两侧。因此

\[
\sum_{\rm merges}\|K_{AB}\|_{HS}^2
=\frac{c^2}{2}
[\operatorname{tr}Q_{\rho,qL}^2-q\operatorname{tr}Q_{\rho,L}^2].
\]

这里的 \(1/2\) 正好把 trace-square 中的两个方向变成一个无序 pair，没有逐 scale 重复收费。

正文应在此显式定义 \(F_N=-H_N''\)。由

\[
M''=F_{A\cup B}-F_A-F_B
\]

和 cut bound 才得到 (22)。若 pointwise cost 为 \(C\)，积分成弦时罚项为 \(C\lambda(1-\lambda)\Delta^2/2\)，所以 (22) 中的 \(B c^2/2\) 在 entropy gap 中变成 \(B c^2/4\)；正文系数正确。

有限 sine compression 没有被当成投影。正文只使用

\[
\frac1N\operatorname{tr}Q_{\rho,N}^2\to\rho,
\]

它来自 Toeplitz 系数平方和与无限 Fourier indicator 的 Parseval。除以 \(qL\) 后，trace difference 的极限是

\[
\rho-\operatorname{tr}Q_{\rho,L}^2/L
=D_{\rho,L}/L.
\]

因此 (24)–(25) 的 leakage 系数无误。整个过程先在有限体积积分，再使用 \(H_N/N\) 的熵值极限；没有求 \(H_N''/N\) 的极限，也不需要 \(h\in C^2\)。

## 6. 极稀疏/极稠密高对比度区域

一点 marginal 参数是 \(t=a+c\rho\)，故

\[
F_1=1/[t(1-t)]\ge4,
\qquad D_{\rho,1}=\rho(1-\rho).
\]

由 \(B_\delta\le6\delta^{-12}\)，

\[
\kappa_1\ge4-3c^2\delta^{-12}\rho(1-\rho).
\]

因此 (28) 的 strict condition 确实给出正 chord coefficient。量词是：先固定 \(c,\rho\) 和 compact legal \(J\)，以该 \(J\) 的统一 gap \(\delta\) 得到其内部全部 chords；它不是端点一致或全部 legal biases 的结论。

在产品区域 (29)，对所有参数统一可取

\[
\delta_{\rm uniform}=1/50\le\min\{a,1-a-c\}
\]

作为统一下界；各点实际 gap 不小于 \(1/50\)，最坏角点达到该值。又

\[
\rho(1-\rho)\le\min(\rho,1-\rho)\le10^{-21}.
\]

精确计算得到

\[
4-3(19/20)^2 50^{12}10^{-21}
=27353/8192,
\]

故弦系数为 \(27353/16384\)。该产品区域真实成立，但密度距 \(0\) 或 \(1\) 只有 \(10^{-21}\)，应保持 `PROVED, NARROW SCOPE`。

## 7. 半密度两点 seed 的预算失败范围

独立重算

\[
B_{1/50}=865433616303812500000
\]

以及 \(c=19/20\) 的 (31)，得到

\[
\kappa_2\approx-5.8063080125817152161\times10^{19}.
\]

这与正文一致。更一般地，在高对比度合法参数内，最大可用 gap 小于 \(3/80\)，正文给出的粗下界已足以说明该**特定**两点 seed 加最坏 word 常数无法支付 leakage。

该失败只限定这一预算组合。它没有证明半密度 rate curvature 为负，也没有排除更强 seed、Fisher–acceleration cancellation 或更便宜的平均常数。正文明确保留了这个边界，处理正确。

## 8. 六点 mixed coordinate 与 common direction

作者声称的 interval checker 附件不可用，故不能标记 `EXECUTED_BY_REVIEWER`。本审查从实际六点半密度 sine kernel 重新枚举 64 个 atoms，用 cofactor marginals 计算 \(\partial_1P,\partial_6P,\partial_1\partial_6P\)，得到负的 mixed coordinate 中心值。所有 atoms 在 80 位计算中为正，最小值约 \(2.02609\times10^{-4}\)。

同一独立实现重建 common identity 分解，数值与作者区间及 PR63 同一点结果一致。证据关系必须保持：

- 负的 \(\mathcal M_{uv}\) 只否定“每个 mixed diagonal 元素都非负”；
- \(C_{\rm acc}<0\) 说明 acceleration 本身不可要求非负；
- 同一点 \(D_F+C_{\rm acc}>0\)，所以它不是 \(M''<0\) 或 common identity convexity 的反例；
- 80 位 Decimal 是强诊断，不替代缺失的 directed interval certificate。

## 9. 精确剩余义务

1. 若要正式接纳 §6 的精确 decimal intervals，仍需取得并运行作者的 outward interval checker，或另写可审计的独立区间实现。
2. 把 worst-word \(B_\delta\) 替换为能利用输出平均、局部 cut 结构或 Fisher cancellation 的可支付常数。
3. 在固定正密度，特别是 \(\rho=1/2\)，找到满足
   \[
   f_L>B_\delta c^2D_{\rho,L}/2
   \]
   的 seed，或证明更强的直接 rate chord inequality。
4. 覆盖 \(74/77<c<1\) 以及一般 \(\rho\) 时，不能把当前极窄 density theorem 写成全高对比度结论。
5. 保持对象边界：有限 Toeplitz compression 是 contraction；negative mixed coordinate 不是总方向反例。

最终状态：**S74 证明了一个真实、全尺寸、无维度但常数极保守的 acceleration cut bound，并把累计成本精确压到 leakage；它由此得到一个正确但极窄的 rate-concavity 产品区域，没有解决原全区间问题。**


## ACCELERATION_PR63.md
Source: research/CYCLE26_20260920/diagnostics/PR63/S71_ACCELERATION_DIAGNOSTIC.md

# S71 acceleration 项真实正弦有限诊断

## 结论

**`C_acc >= 0` 被严格证伪；有限网格内没有发现 `M''<0`。**

最小反例就是两个相邻单点块，不需要大规模枚举。对任意实际两点正弦
Toeplitz 压缩，记

\[
u=a+c\rho,
\qquad
d=c^2\left(\frac{\sin(\pi\rho)}{\pi}\right)^2>0,
\]

四个原子为

\[
p_{11}=u^2-d,quad
p_{00}=(1-u)^2-d,quad
p_{10}=p_{01}=u(1-u)+d=:r.
\]

共同 identity shift 下，四个原子的二阶导分别是
\((2,2,-2,-2)\)。边缘原子的二阶导为零，故

\[
\begin{aligned}
C_{\rm acc}
&=2\log\frac{p_{11}}{u^2}
+2\log\frac{p_{00}}{(1-u)^2}
-4\log\frac r{u(1-u)}\\
&=2\log\frac{p_{11}p_{00}}{r^2}.
\end{aligned}
\]

直接展开得到

\[
p_{11}p_{00}=r^2-d,
\]

所以在全部合法严格参数上

\[
\boxed{C_{\rm acc}=2\log(1-d/r^2)<0.}
\]

因此，S74 不应尝试证明 acceleration 项单独非负。正确的候选结构是：
它是一个负的反曲率项，但可能始终由非负 Fisher 缺陷支付。

来源对象为
`C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE24_20260919/S71/S71_VISIBLE_RESULT.md`。
本诊断没有重跑 PR58/PR61 的 reveal 枚举，也没有修改其数学裁决。

## 1. 冻结量

对相邻块 \(A,B\)，完整联合律为实际有限 DPP

\[
K_{a,c,N}=aI+cQ_{\rho,N},
\qquad N=|A|+|B|.
\]

对输出 word \(y\)，令

\[
R_y=(K-\operatorname{diag}(1-y))^{-1},
\quad S_y=\operatorname{tr}R_y,
\quad T_y=S_y^2-\operatorname{tr}(R_y^2).
\]

程序只计算 S71 已定位的三个量：

\[
D_F=\mathbb ES^2-\mathbb ES_A^2-\mathbb ES_B^2,
\]

\[
C_{\rm acc}
=\mathbb E\left[T_Y\log\frac{P(Y)}{P_A(Y_A)P_B(Y_B)}\right],
\]

\[
M''=D_F+C_{\rm acc}.
\]

## 2. 安全实现与独立交叉核对

第一条计算路径用真实全输出权重

\[
P(y)=(-1)^{N-|y|}
\det(K-\operatorname{diag}(1-y))
\]

和 resolvent 公式

\[
P'=PS,
\qquad P''=PT.
\]

第二条独立路径不使用 \(\operatorname{tr}R\) 生成导数。对每个 word，
把 Hermitian 矩阵

\[
B_y=cQ-\operatorname{diag}(1-y)
\]

的特征值重建成标量多项式

\[
P_y(a)=(-1)^{N-|y|}\det(aI+B_y),
\]

直接微分该多项式得到 \(P_y',P_y''\)，再计算

\[
H''=-\sum_yP_y''\log P_y-sum_y\frac{(P_y')^2}{P_y},
\]

最终以 \(H_A''+H_B''-H_{A\cup B}''\) 交叉核对 \(M''\)。

全部 945 个 block 案例中：

- 概率归一误差至多 \(1.23\times10^{-15}\)；
- 一、二阶总质量误差至多 \(5.45\times10^{-15}\)、
  \(3.02\times10^{-14}\)；
- decomposition 与直接 resolvent 熵曲率误差至多
  \(3.42\times10^{-13}\)；
- resolvent 与行列式多项式熵曲率误差至多
  \(1.37\times10^{-12}\)。

最坏 masked matrix 条件数约 999；稀有原子的多项式概率相对误差至多
\(3.12\times10^{-9}\)，但承重的熵二阶交叉误差仍在上述
\(10^{-12}\) 量级。

## 3. 精确两点证书

取最简单的半密度中点实例

\[
\rho=\frac12,qquad c=\frac{93}{100},qquad
a=\frac{1-c}{2}=\frac7{200}.
\]

此时 \(u=1/2\)、\(d=c^2/\pi^2\)，于是

\[
C_{\rm acc}
=4\log\frac{1/4-d}{1/4+d}<0,
\]

而

\[
D_F=\frac2{1/4-d}-8=\frac{32d}{1-4d}>0.
\]

二者之和为

\[
M''(d)=\frac2{1/4-d}
+4\log\frac{1/4-d}{1/4+d}-8.
\]

它满足 \(M''(0)=0\)，且

\[
\frac{d}{dd}M''(d)
=\frac{4d}{(1/4-d)^2(1/4+d)}>0,
\]

所以这个最小模型同时严格证明

\[
C_{\rm acc}<0,qquad D_F>0,qquad M''>0.
\]

附带的标准库精确检查器只用 \(3<\pi<22/7\) 和

\[
x<\operatorname{atanh}x<\frac{x}{1-x^2}
\quad(0<x<1)
\]

给出有理包围

\[
-3.60839<C_{\rm acc}<-2.80199,
\qquad
4.31240<D_F<4.99546.
\]

实际双精度全输出值为

\[
D_F=4.317750545584095,
\]

\[
C_{\rm acc}=-2.928389960160608,
\]

\[
M''=1.389360585423488.
\]

负 acceleration 消耗了约 \(67.82\%\) 的 Fisher 缺陷，但没有翻转
总曲率。

## 4. 有限扫描

扫描严格限定为：

- \(\rho\in\{1/4,1/2,3/4\}\)；
- \(c\in\{.93,.95,.99\}\)；
- \(p=a/(1-c)\in\{.1,.25,.5,.75,.9\}\)；
- 21 个平衡或不平衡相邻分割，最大总长度 10；
- 每个模型枚举全部 \(2^N\) 个真实输出 word。

结果：

| 项目 | 结果 |
|---|---:|
| block 案例数 | 945 |
| \(C_{\rm acc}<0\) | 945 |
| \(M''<0\) | 0 |
| \(C_{\rm acc}\) 范围 | \([-80.1884,-2.34236]\) |
| \(D_F\) 范围 | \([4.13662,399.157]\) |
| \(M''\) 范围 | \([1.38936,318.969]\) |
| 最大支付比例 \(-C_{\rm acc}/D_F\) | 0.683214 |

按总长度汇总：

| \(N\) | 案例数 | 最小 \(M''\) | 最大 \(-C_{\rm acc}/D_F\) | 最负 \(C_{\rm acc}\) |
|---:|---:|---:|---:|---:|
| 2 | 45 | 1.38936 | 0.678222 | -4.38700 |
| 3 | 90 | 2.35386 | 0.611240 | -8.33964 |
| 4 | 135 | 2.62862 | 0.655872 | -16.0086 |
| 5 | 90 | 3.88819 | 0.675996 | -22.9593 |
| 6 | 225 | 3.60719 | 0.683214 | -33.0960 |
| 7 | 90 | 6.63029 | 0.675336 | -42.5752 |
| 8 | 135 | 6.79059 | 0.668633 | -54.7546 |
| 10 | 135 | 10.5017 | 0.679901 | -80.1884 |

最接近吃完 Fisher 缺陷的测试点是

\[
(\rho,c,p;m,n)=(.25,.93,.9;3,3),
\]

其中

\[
D_F=16.2302320497,quad
C_{\rm acc}=-11.0887128090,quad
M''=5.14151924068.
\]

最负的 \(C_{\rm acc}\) 出现在

\[
(\rho,c,p;m,n)=(.25,.99,.1;5,5),
\]

但此处 \(D_F=399.15745\) 足以支付 \(C_{\rm acc}=-80.18833\)，
所以它不是最接近总曲率反例的点。

## 5. 对 S74 最有价值的假设

有限证据支持的方向不是

\[
C_{\rm acc}\ge0,
\]

而是以下二层结构：

\[
C_{\rm acc}\le0
\quad\text{以及}\quad
-C_{\rm acc}\le D_F.
\]

第一层在相邻两单点块上已经严格成立；945 个测试点全部同号，但这仍
不能升级为任意块定理。第二层正好等价于 \(M''\ge0\)，所以不能只改名
后当作新引理。真正可能有用的加强应把它局部化，例如：

1. 把 \(-C_{\rm acc}\) 表成跨边界 pair/条件协方差预算；
2. 证明该预算由 \(D_F\) 中对应的跨块 score 投影支付；
3. 或在固定谱隙紧集上证明严格比例
   \(-C_{\rm acc}\le(1-\varepsilon)D_F\)，并明确
   \(\varepsilon(\delta,\rho,c)\) 的退化方式。

网格中最大的已观察比例约 0.683，并没有逼近 1；这是值得追踪的
定量信号，但绝不是比例定理。

## 6. 作用域

- **严格证伪：** acceleration 项单独非负；反例已在真实相邻两点
  sine DPP 上解析成立。
- **有限诊断支持：** 所列 945 个实际模型均有 \(M''>0\)，且
  Fisher 缺陷支付负 acceleration。
- **未证明：** 任意块、任意尺寸、连续参数上的 \(M''\ge0\)；
  \(C_{\rm acc}\le0\) 的一般块版本；任何固定比例支付；熵率凹性。

## 7. 重放

```powershell
python research/INDEPENDENT_REVIEW_20260918/S71_ACCELERATION_DIAGNOSTIC_CYCLE25/s71_acceleration_scan.py `
  --output research/INDEPENDENT_REVIEW_20260918/S71_ACCELERATION_DIAGNOSTIC_CYCLE25/S71_ACCELERATION_SCAN.json

python research/INDEPENDENT_REVIEW_20260918/S71_ACCELERATION_DIAGNOSTIC_CYCLE25/s71_two_site_certificate.py `
  --output research/INDEPENDENT_REVIEW_20260918/S71_ACCELERATION_DIAGNOSTIC_CYCLE25/S71_TWO_SITE_CERTIFICATE.json
```
