# S64 — Cycle11 result

## Conditional KL supermodularity, a finite-core cross-scale payment, and an actual-sine obstruction

**Overall objective: INCOMPLETE.** This submission does not prove the benchmark entropy-rate chord, a fixed-interval entropy concavity theorem, or the universal whole-interval conjecture.

**New proved tool:** For a common diagonal shift of a finite Hermitian DPP, full-configuration relative entropy is a supermodular function of the observed set. There is an explicit, nonnegative conditional log-determinant budget for the supermodularity defect. For a stationary process, the block relative entropies are consequently convex in block length. Two certified finite volumes then give a quantitative lower bound for the KL component at every larger volume. This is a finite-parameter result, not differentiation of an entropy-value tail.

**New actual-model obstruction:** A specified two-doubling entropy-payment window is not monotone in either direction, even on the corrected benchmark interval. Exact integer-interval certificates give both signs at the same pair of windows for two nondegenerate chords contained in that interval.

The probability-acceleration cost is explicitly retained and remains unpaid. The positive budgets below must not be added together when they bound the same KL increment.

All logarithms are natural. All entropies and relative entropies refer to the complete binary configuration, never only its count.

---

## 1. Scope, sources, and conventions

The model is

\[
 K_n(a)=aI+cQ_{\rho,n},\qquad
 Q_{\rho,n}(i,j)=\begin{cases}\rho&i=j,\\
 \sin(\pi\rho(i-j))/(\pi(i-j))&i\ne j.
 \end{cases}
\]

The finite matrix \(Q_{\rho,n}\) is a compression of an infinite Fourier projection; it is not generally a projection. The proof below never replaces it by one.

For completeness, for a nonzero vector \(x\),

\[
 x^*Q_{\rho,n}x=\int_{-\rho/2}^{\rho/2}
       \left|\sum_j x_j e^{2\pi ijt}\right|^2dt>0,
\]

and the analogous integral over the complementary arc gives \(x^*(I-Q_{\rho,n})x>0\). A nonzero trigonometric polynomial cannot vanish on an arc. Thus \(0\prec Q_{\rho,n}\prec I\), and every finite sine kernel at a legal \(0\le a\le1-c\), \(0<c<1\), is a strict contraction. The finite theorems below apply even at those legal endpoints. Only the inherited QWE02 uniform tail interface is restricted to compact legal interiors.


For a chord \(a_0<a_1\), \(0<\lambda<1\), put

\[
 b=(1-\lambda)a_0+\lambda a_1,\qquad
 \operatorname{Gap}F=F(b)-(1-\lambda)F(a_0)-\lambda F(a_1).
\]

For a midpoint chord with endpoints \(b\pm\eta\),

\[
 \operatorname{Gap}F=-\tfrac12\Delta_\eta F.
\]

The numerical chord used for the new core is

\[
 C_0:\quad \rho=\tfrac12,\ c=\tfrac{19}{20},\quad
 a_0=\tfrac1{50},\ b=\tfrac1{40},\ a_1=\tfrac3{100},\quad \eta=\tfrac1{200}.
\]

No certificate for the old endpoints \(.015,.035\) is used.

### Reviewed-input ledger

All six required raw files were read in the requested order. The archived PR128 proposal and the current S61 review were also read. No required source was unavailable. The branch status memo governs the imported scope.

* **SOURCE_STATUS:** the accepted whole-interval baseline remains \(c\le37/40\); no author-only S59/S60 claim is used. S61 supplies no true-sine cross-scale payment.
* **FAILED_ROUTES:** pointwise/layerwise payment and frozen-reference shortcuts are not used. The new theorem assumes a common diagonal shift, not arbitrary affine complex-kernel variation.
* **S42_REVIEW:** the true-sine finite-chord/value-limit dyadic bridge is used. Its old finite seed is not transferred to the new chord.
* **QWE02_RESULT and QWE02_REVIEW:** the reviewed quadratic true-law far-tail estimate is used only as a final interface. Its asymptotic proof is not redone and its large constant is not treated as a practical middle-scale payment.
* **S47_REVIEW:** the signed diagonal-translation algebra and the need to retain probability acceleration are respected. The erroneous original relative-entropy Hessian formula is not used.
* **S61_REVIEW:** its reviewed frozen cyclic result is acknowledged but is not an input to any new inequality here.

The sole imported probabilistic theorem in the new proof is **negative association of a Hermitian DPP with a positive-contraction kernel**, from Russell Lyons, *Determinantal probability measures*, Theorem 8.1, Section 8, arXiv:math/0204325. That theorem covers positive contractions, not only projections. External-field closure is verified directly below before applying negative association to tilted laws.

Repository sources use the supplied raw base:

`https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle11-pr128-20260918/`

with the repository-relative paths in the task. The external primary source is `https://arxiv.org/html/math/0204325`, Section 8, Theorem 8.1.

---

## 2. A finite-parameter likelihood-ratio lemma

### Claim 2.1 — PROVED: uniform monotone likelihood ratios

**Inputs and hypotheses.** Let \(V\) be finite and let

\[
 K(a)=K_*+aI
\]

be Hermitian with \(0\prec K(a)\prec I\) throughout the interval between two parameters \(u,v\). Let \(P_a^A\) denote the DPP marginal on any \(A\subseteq V\).

For every nonempty \(A\), every \(i\in A\), and every setting of the other coordinates,

\[
 \Delta_i\partial_a\log p_a^A\ge4.                                      \tag{2.1}
\]

Consequently, if \(u>v\),

\[
 \Delta_i\log\frac{p_u^A}{p_v^A}\ge4(u-v).                              \tag{2.2}
\]

If \(u<v\), the same expression is at most \(4(u-v)\); equivalently, the likelihood ratio is increasing in the hole coordinates with minimum log-increment \(4(v-u)\).

The same conclusions hold for \(p_a(A\mid Z=z)\), for any disjoint conditioned set \(Z\) and any of its configurations \(z\).

**Proof.** Strict contraction implies full support: with

\[
 L(a)=K(a)(I-K(a))^{-1}\succ0,
\]

the atom for the occupied set \(S\) is

\[
 p_a(S)=\det(I-K(a))\det L(a)_S>0.
\]

Fix the other coordinates \(R=A\setminus\{i\}\), with configuration \(z\), and put

\[
 M_R(a)=K_R(a)-D_{1-z}.
\]

The atom determinant formula makes \(M_R(a)\) invertible. The conditional occupation probability is its Schur complement:

\[
 q_i(a,z)=K_{ii}(a)-K_{iR}M_R(a)^{-1}K_{Ri}.
\]

The off-diagonal vectors do not vary with \(a\). Thus

\[
 q_i'(a,z)=1+K_{iR}M_R(a)^{-2}K_{Ri}\ge1.
\]

Because \(M_R\) is Hermitian, its inverse square is positive semidefinite. Since \(0<q_i<1\),

\[
 \Delta_i\partial_a\log p_a^A
 =\partial_a\log\frac{q_i}{1-q_i}
 =\frac{q_i'}{q_i(1-q_i)}\ge4.
\]

Integrating proves (2.2), including the reversed inequality when \(u<v\).

For a conditional likelihood ratio, use the common-shift marginal on \(A\cup Z\). The factor \(p_a^Z(z)\) is independent of the coordinates in \(A\) and disappears under \(\Delta_i\). Equivalently, include \(Z=z\) among the fixed coordinates in the Schur-complement proof. No assertion that the conditional kernel itself varies as \(aI\) is required. \(\square\)

---

## 3. External-field reverse tensorization

### Claim 3.1 — PROVED: a normalized-product bound

**Inputs and hypotheses.** Let \(P\) be a full-support law on \(\{0,1\}^U\) that is negatively associated after every external-field tilt. Partition \(U\) into disjoint nonempty blocks \(A_1,\ldots,A_r\). Let positive functions \(r_j\), depending only on \(A_j\), satisfy

\[
 E_P r_j=1,\qquad \Delta_i\log r_j\ge h\quad(i\in A_j),\qquad h\ge0.
\]

Write \(N_A=\sum_{i\in A}Y_i\) and

\[
 \Lambda_A(h)=\log E_Pe^{hN_A}.
\]

Then

\[
 \boxed{\quad
 E_P\prod_{j=1}^r r_j
 \le \exp\left\{\Lambda_U(h)-\sum_{j=1}^r\Lambda_{A_j}(h)\right\}.
 \quad}                                                               \tag{3.1}
\]

**Proof.** Put \(g_j=e^{-hN_{A_j}}r_j\). These functions are positive and increasing. Let \(P_h\) be the tilt of \(P\) by \(e^{hN_U}\). Negative association, iterated over disjoint blocks, gives

\[
 E_{P_h}\prod_jg_j\le\prod_jE_{P_h}g_j.
\]

To compare the latter expectations, start with the field \(h\) on \(A_j\) alone and increase a common field on its complement from zero to \(h\). At every intermediate tilt,

\[
 \frac{d}{dt}E g_j=\operatorname{Cov}(g_j,N_{U\setminus A_j})\le0.
\]

The supports are disjoint and both functions are increasing. Hence

\[
 E_{P_h}g_j
 \le \frac{E_P[e^{hN_{A_j}}g_j]}{E_Pe^{hN_{A_j}}}
 =e^{-\Lambda_{A_j}(h)}.
\]

Multiplying these inequalities and restoring the normalization of \(P_h\) proves (3.1). \(\square\)

**Why every required tilted law is admissible for a DPP.** For a strict Hermitian DPP, the tilt by \(\exp(\sum_i t_iY_i)\) has

\[
 L_t=D_{e^{t/2}}LD_{e^{t/2}}\succ0,
 \qquad K_t=L_t(I+L_t)^{-1}.
\]

This is again a Hermitian strict-contraction DPP. Lyons's negative-association theorem therefore applies to every field used above. Conditioning also preserves the determinantal law and strict contraction, as follows by iterating the one-coordinate Schur complements. The complement process has kernel \(I-K\), so the same proof applies to hole coordinates.

---

## 4. Main tool: conditional KL supermodularity

### Theorem 4.1 — PROVED

**Inputs.** A finite Hermitian common-shift family as in Claim 2.1; parameters \(u,v\); a disjoint decomposition

\[
 V=Z\sqcup A_1\sqcup\cdots\sqcup A_r,\qquad U=V\setminus Z.
\]

Put

\[
 D_A(u\Vert v)=D(P_u^A\Vert P_v^A),\qquad D_\varnothing=0,\qquad h=4(u-v).
\]

For a configuration \(z\) on \(Z\), the actual conditional DPP kernel is explicitly

\[
 K_{v,U\mid z}=K_{v,U}-K_{v,UZ}
       (K_{v,Z}-D_{1-z})^{-1}K_{v,ZU},
\]

with the subtraction omitted when \(Z\) is empty. Define

\[
 \Lambda_{v,A\mid z}(h)
 =\log\det\bigl(I_A+(e^h-1)(K_{v,U\mid z})_A\bigr).
\]

Define the conditional determinant defect

\[
 \mathcal B_v(z;h)
 =\sum_{j=1}^r\Lambda_{v,A_j\mid z}(h)
  -\Lambda_{v,U\mid z}(h).
\]

**Output.**

\[
 \boxed{
 D_V(u\Vert v)+(r-1)D_Z(u\Vert v)
 -\sum_{j=1}^rD_{Z\cup A_j}(u\Vert v)
 \ge E_{P_u^Z}\mathcal B_v(Z;h)\ge0.
 }                                                                    \tag{4.1}
\]

More quantitatively,

\[
 \boxed{
 \mathcal B_v(z;h)
 \ge(1-e^{-|h|})^2
       \sum_{i<j}\|(K_{v,U\mid z})_{A_iA_j}\|_{\rm HS}^2.
 }                                                                    \tag{4.2}
\]

The averaging measure in (4.1) is **the actual moving endpoint law \(P_u^Z\)**, not \(P_v^Z\), a frozen reference law, or a count law.

**Proof of (4.1).** Fix \(z\). Let \(Q=P_u(U\mid z)\), \(P=P_v(U\mid z)\), and let

\[
 r_j=\frac{Q_{A_j}}{P_{A_j}},\qquad
 Z_r=E_P\prod_jr_j,\qquad
 R=P\prod_jr_j/Z_r.
\]

No determinantal or negative-association property is assumed for the auxiliary law \(R\); only its normalization is used. An exact full-law calculation gives

\[
 D(Q\Vert P)-\sum_jD(Q_{A_j}\Vert P_{A_j})
 =D(Q\Vert R)-\log Z_r.                                                \tag{4.3}
\]

For \(u>v\), Claim 2.1 and Claim 3.1 imply

\[
 -\log Z_r\ge\sum_j\Lambda_{v,A_j\mid z}(h)
                     -\Lambda_{v,U\mid z}(h).
\]

The DPP generating-polynomial identity used here is

\[
 E e^{hN_A}=E\prod_{i\in A}(1+(e^h-1)Y_i)
 =\sum_{S\subseteq A}(e^h-1)^{|S|}\det K_S
 =\det(I+(e^h-1)K_A).
\]

For \(u<v\), apply Claim 3.1 to the holes with positive field \(-h\). The additional constants \((-h)|A_j|\) cancel against \((-h)|U|\), giving exactly the same signed-\(h\) determinant defect. The case \(u=v\) is equality.

Since \(D(Q\Vert R)\ge0\), (4.3) proves the pointwise conditional inequality. Average under \(P_u^Z\) and use the exact relative-entropy chain rules

\[
 D_V-D_Z=E_{P_u^Z}D(P_u(U\mid Z)\Vert P_v(U\mid Z)),
\]

\[
 D_{Z\cup A_j}-D_Z
 =E_{P_u^Z}D(P_u(A_j\mid Z)\Vert P_v(A_j\mid Z)).
\]

This proves (4.1), with every moving conditional weight retained.

**Proof of (4.2).** For any strict contraction \(K\) on \(U\), set

\[
 K_0=\bigoplus_j K_{A_j},\quad E=K-K_0,\quad
 K_\theta=K_0+\theta E,\quad t=e^h-1.
\]

The whole path is a strict contraction. Put

\[
 f(\theta)=-\log\det(I+tK_\theta).
\]

The first derivative at zero is zero because \(E\) has zero diagonal blocks. Every eigenvalue of \(I+tK_\theta\) is at most \(M_h=\max(1,e^h)\), so

\[
 f''(\theta)
 =t^2\operatorname{tr}\bigl((I+tK_\theta)^{-1}E
                           (I+tK_\theta)^{-1}E\bigr)
 \ge \frac{t^2}{M_h^2}\|E\|_{\rm HS}^2.
\]

Taylor's integral formula and \(\|E\|_{\rm HS}^2=2\sum_{i<j}\|K_{A_iA_j}\|_{\rm HS}^2\) give

\[
 f(1)-f(0)
 \ge\frac{t^2}{M_h^2}\sum_{i<j}\|K_{A_iA_j}\|_{\rm HS}^2.
\]

Here \(t^2/M_h^2=(1-e^{-|h|})^2\). Apply this to the actual conditional kernel for each \(z\). \(\square\)

### Corollary 4.2 — PROVED: supermodularity and block-length convexity

For every pair of observed sets \(S,T\),

\[
 \boxed{D_{S\cup T}+D_{S\cap T}\ge D_S+D_T.}                            \tag{4.4}
\]

This follows from Theorem 4.1 with conditioned set \(S\cap T\) and the two disjoint differences.

For a stationary common-shift process, write \(D_n=D_{[1,n]}(u\Vert v)\). Taking \(S=[1,n]\), \(T=[2,n+1]\) gives

\[
 \boxed{D_{n+1}-2D_n+D_{n-1}\ge0\qquad(n\ge1).}                        \tag{4.5}
\]

Thus \(d_n=D_n-D_{n-1}\) is nondecreasing. For any certified core size \(m\ge1\) and every integer \(M\ge m\),

\[
 \boxed{\frac{D_M}{M}\ge
 d_m-\frac{m d_m-D_m}{M}
 =\frac{D_m}{m}+
   \left(1-\frac mM\right)\left(d_m-\frac{D_m}{m}\right).}              \tag{4.6}
\]

Here \(d_m-D_m/m\ge0\), since \(D_0=0\) and the successive increments are nondecreasing. Formula (4.6) is an analytic extrapolation to every larger volume from the two inputs \(D_{m-1},D_m\). It is not an enumeration of larger dyadic volumes.

### Corollary 4.3 — PROVED: an explicit three-site sine payment

At half density, take \(Z=\{2\}\), \(A_1=\{1\}\), \(A_2=\{3\}\), and put \(p_a=a+c/2\). Although \(K_{13}=0\), conditioning on the middle bit gives reference cross-kernel entries

\[
 (K_v)_{13\mid Y_2=1}=-\frac{c^2}{\pi^2p_v},\qquad
 (K_v)_{13\mid Y_2=0}=\frac{c^2}{\pi^2(1-p_v)}.
\]

Therefore the actual full-law block divergences satisfy

\[
 D_3+D_1-2D_2\ge
 (1-e^{-4|u-v|})^2\frac{c^4}{\pi^4}
 \left(\frac{p_u}{p_v^2}+\frac{1-p_u}{(1-p_v)^2}\right)>0
\]

whenever \(u\ne v\) and \(c>0\). This follows directly from (4.1)–(4.2), with the two actual endpoint probabilities \(p_u,1-p_u\). At the benchmark reference \(v=1/40\), the parenthesis equals four. This conditional payment detects a coupling that is absent from the unconditional \((1,3)\) kernel entry.

### Corollary 4.4 — PROVED: finite-volume Fisher consequence

For fixed finite observed sets, expand

\[
 D_A(v+\epsilon\Vert v)=\tfrac12\epsilon^2F_A(v)+O(\epsilon^3).
\]

Theorem 4.1 therefore implies supermodularity of the scalar common-shift Fisher information and the conditional quantitative bound

\[
 F_V+(r-1)F_Z-\sum_jF_{Z\cup A_j}
 \ge32E_{P_v^Z}\sum_{i<j}
          \|(K_{v,U\mid Z})_{A_iA_j}\|_{\rm HS}^2.
\]

This concerns the observed-set variable, and in the stationary case the **block-length** variable. It does not assert convexity of Fisher information as a function of \(a\), and no entropy-rate derivative is taken.

---

## 5. Exact entropy-chord interface and what is not paid

### Claim 5.1 — PROVED: full moving-law decomposition

For a fixed chord, define

\[
 \mathcal D_n=(1-\lambda)D(P_{a_0,n}\Vert P_{b,n})
                 +\lambda D(P_{a_1,n}\Vert P_{b,n}),
\]

\[
 \mathcal C_n=E_{P_{b,n}}\log p_{b,n}
 -(1-\lambda)E_{P_{a_0,n}}\log p_{b,n}
 -\lambda E_{P_{a_1,n}}\log p_{b,n}.
\]

Then

\[
 \boxed{\operatorname{Gap}H_n=\mathcal D_n-\mathcal C_n,
 \qquad \mathcal C_n\ge0.}                                            \tag{5.1}
\]

**Proof.** Expanding the definitions of relative entropy gives the equality directly. For the sign, for any fixed function \(f\) on the Boolean cube,

\[
 \frac{d}{da}E_{P_a}f=E_{P_a}Gf,\qquad
 G=\sum_i\Delta_i,
\]

and hence \((E_{P_a}f)''=E_{P_a}G^2f\). One may verify this on the multilinear monomial basis: differentiating \(E\prod_{i\in S}Y_i=\det K_S\) under a common diagonal shift gives the sum of its principal cofactors. Thus the identity preserves every probability derivative; it is not a Markov data-processing assertion.

For the fixed reference kernel \(K_b\),

\[
 \log p_b(S)=\log\det(I-K_b)+\log\det(L_b)_S.
\]

The second term is submodular. Indeed a positive \(2\times2\) Schur complement with diagonal entries \(\alpha,\beta\) and off-diagonal entry \(z\) gives

\[
 \Delta_i\Delta_j\log p_b
 =\log\frac{\alpha\beta-|z|^2}{\alpha\beta}\le0.
\]

Since \(G^2=2\sum_{i<j}\Delta_i\Delta_j\), the function \(a\mapsto E_{P_a}\log p_b\) is concave. Its chord gap is exactly \(\mathcal C_n\), proving the sign. \(\square\)

Fixing \(p_b\) in this exact three-point identity does not freeze the endpoint probability weights: they remain \(P_{a_0,n}\) and \(P_{a_1,n}\). No derivative of a moving reference has been omitted.

### Theorem 5.2 — PROVED, explicitly partial: retained signed-sum payment

For the stationary sine process, put

\[
 s_m=\mathcal D_m-\mathcal D_{m-1},\qquad
 B_m=s_m-\mathcal D_m/m\ge0.
\]

For every integer \(N\ge0\), \(M=m2^N\),

\[
 \boxed{
 \sum_{j=0}^{N-1}\frac{\operatorname{Gap}J_{m2^j}}{2m2^j}
 \le\frac{\mathcal C_M}{M}-\frac{\mathcal C_m}{m}
       -\left(1-\frac mM\right)B_m.
 }                                                                    \tag{5.2}
\]

**Proof.** The weighted average \(\mathcal D_n\) inherits the block-length convexity of each endpoint relative entropy. Apply (4.6), then use (5.1) in the finite telescoping identity

\[
 \sum_{j<N}\frac{\operatorname{Gap}J_{m2^j}}{2m2^j}
 =\frac{\operatorname{Gap}H_m}{m}-\frac{\operatorname{Gap}H_M}{M}.
\]

This gives (5.2). \(\square\)

**A uniform analytic positive certificate.** For the actual sine kernel, let

\[
 A_{\rm chord}=\frac{c^2\sin^2(\pi\rho)}{\pi^2}
 \left[(1-\lambda)(1-e^{-4|a_0-b|})^2
             +\lambda(1-e^{-4|a_1-b|})^2\right]>0.
\]

For every \(m\ge2\), one has \(B_m\ge A_{\rm chord}/m\). Indeed, the unconditioned two-site energy bound gives \(\mathcal D_2-2\mathcal D_1\ge A_{\rm chord}\). Writing \(d_j=\mathcal D_j-\mathcal D_{j-1}\), length convexity yields

\[
 B_m=\frac1m\sum_{j=1}^m(d_m-d_j)
 \ge\frac{d_2-d_1}{m}\ge\frac{A_{\rm chord}}m.
\]

This certifies a positive KL aggregate payment for every nondegenerate legal chord at every fixed \(0<\rho,c<1\). It is not an entropy-concavity statement. The numerical core below substantially strengthens this general positive certificate for \(C_0\).

**Ledger meaning.** The new part is the strictly quantitative, scale-uniform KL payment \((1-m/M)B_m\), obtained from two finite full-law inputs. The theorem does not require a sign for any individual \(\operatorname{Gap}J_L\). It leaves the full acceleration-cost increment \(\mathcal C_M/M-\mathcal C_m/m\) visible. Its sign or an adequate upper bound is not proved here. Consequently (5.2) is not, by itself, a proof that the complete retained sum is paid.

---

## 6. A second explicit budget and its analytic envelope

### Claim 6.1 — PROVED: unconditional determinant payment

For equal stationary blocks of size \(m\) partitioning \([1,M]\), Theorem 4.1 with no conditioned set gives

\[
 \frac{D_M(u\Vert v)}M-\frac{D_m(u\Vert v)}m
 \ge\frac{\Lambda_{v,m}(h)}m-\frac{\Lambda_{v,M}(h)}M,
 \quad h=4(u-v).
\]

Averaging the two endpoints gives a second nonnegative bound \(\mathcal G_{m,M}\) for \(\mathcal D_M/M-\mathcal D_m/m\). In (5.2), one may replace \((1-m/M)B_m\) by

\[
 \max\{(1-m/M)B_m,\ \mathcal G_{m,M}\},
\]

but not by their sum: they pay the same increment.

### Claim 6.2 — PROVED: moderate-constant sine determinant envelope

Let \(K_M=bI+cQ_{\rho,M}\), \(t=e^h-1\), and

\[
 \ell_{\rho,b,c}(h)
 =(1-\rho)\log(1+tb)+\rho\log(1+t(b+c)),
\]

\[
 d=\min\{1+tb,1+t(b+c)\}>0.
\]

For every \(M\ge1\),

\[
 \boxed{
 0\le\frac{\Lambda_{b,M}(h)}M-\ell_{\rho,b,c}(h)
 \le\frac{t^2c^2}{\pi^2d^2}\frac{2+\log M}{M}.
 }                                                                    \tag{6.1}
\]

**Proof.** For \(x\in[0,1]\), let \(g(x)=\log(1+t(b+cx))\). Its difference from the affine secant through its endpoints lies between zero and

\[
 \frac{t^2c^2}{2d^2}x(1-x).
\]

The lower bound is concavity; the upper bound follows by comparing second derivatives and zero endpoint values. Sum over the eigenvalues of \(Q_{\rho,M}\), using \(\operatorname{Tr}Q_{\rho,M}=\rho M\).

The Fourier projection on the whole integer line gives the exact leakage identity

\[
 \operatorname{Tr}(Q_{\rho,M}-Q_{\rho,M}^2)
 =2\sum_{r\ge1}\min(r,M)\frac{\sin^2(\pi\rho r)}{\pi^2r^2}
 \le\frac2{\pi^2}(2+\log M).
\]

This proves (6.1). The leakage is retained, not set to zero. \(\square\)

This is an envelope for the new determinant/KL budget only. It neither re-proves nor substitutes for QWE02's full entropy-chord tail. It supplies an analytic stopping rule for computing this component to a prescribed error, because \((2+\log M)/M\) decreases to zero.

For \(C_0\), the two fields are \(h=\pm1/50\). Complement symmetry makes their determinant defects equal. Certified enclosures are

\[
 \mathcal G_{1,\infty}\in
 [0.000045124027953776463815636693,
  0.000045124027953776463815636694],
\]

\[
 \mathcal G_{16,\infty}\in
 [0.000005763462348515350588248016,
  0.000005763462348515350588248017].
\]

The stronger length-convexity budget from the next section is used for the main benchmark ledger.

---

## 7. A fresh certified finite core, and payment at all larger volumes

### Claim 7.1 — PROVED: corrected-chord certificates

For \(C_0\), complement/gauge symmetry gives

\[
 H_n(a)=H_n(1-c-a),\qquad
 D(P_{.02,n}\Vert P_{.025,n})=D(P_{.03,n}\Vert P_{.025,n}).
\]

To prove the symmetry at finite volume, let \(U_{ii}=(-1)^i\). At half density,

\[
 UQ_{1/2,n}U=I-Q_{1/2,n},\qquad
 I-K_n(a)=UK_n(1-c-a)U.
\]

Diagonal unitary conjugation leaves the DPP law unchanged; complementation replaces \(K\) by \(I-K\). This uses no projection identity for the compression.

Thus the two-endpoint KL average \(\mathcal D_n\) can be certified from the endpoint \(.02\) alone. Exact outward-rounded integer-interval calculations give

\[
 \mathcal D_{15}\in
 [0.004222178605379545187456418024,
  0.004222178605379545187456418025],
\]

\[
 \mathcal D_{16}\in
 [0.004614791086101230763850243729,
  0.004614791086101230763850243730],
\]

\[
 s_{16}=\mathcal D_{16}-\mathcal D_{15}\in
 [0.000392612480721685576393825704,
  0.000392612480721685576393825705],
\]

\[
 \boxed{B_{16}\in
 [0.000104188037840358653653185471,
  0.000104188037840358653653185472].}                                    \tag{7.1}
\]

For the complete entropy and acceleration cost,

\[
 \gamma_{16}:=\frac{\operatorname{Gap}H_{16}}{16}\in
 [0.000141743962555442975188447184,
  0.000141743962555442975188447185],                                    \tag{7.2}
\]

\[
 \frac{\mathcal C_{16}}{16}\in
 [0.000146680480325883947552193048,
  0.000146680480325883947552193049].                                    \tag{7.3}
\]

### Output interface at every larger volume

From the two KL core sizes, without evaluating any larger law, for **every integer \(M\ge16\)**,

\[
 \frac{\mathcal D_M}{M}\ge
 \frac{\mathcal D_{16}}{16}+
 \left(1-\frac{16}{M}\right)B_{16}.                                   \tag{7.4}
\]

For every dyadic \(M=16\,2^N\), the full retained entropy sum from scale 16 obeys

\[
 \sum_{j<N}\frac{\operatorname{Gap}J_{16\,2^j}}{32\,2^j}
 \le\frac{\mathcal C_M}{M}-\frac{\mathcal C_{16}}{16}
       -\left(1-\frac{16}{M}\right)B_{16}.                             \tag{7.5}
\]

For example, the guaranteed KL increase at \(M=32\) is at least \(B_{16}/2\); its limiting guaranteed increase is \(B_{16}\). This is a proved analytic all-larger-scale envelope, not a brute-force table of dyadic sizes.

The first four entropy payments are separately certified as well:

\[
 \sum_{L\in\{1,2,4,8\}}
       \frac{\operatorname{Gap}J_L}{2L}
 \in[-0.000091743129188774522696376117,
     -0.000091743129188774522696376116].                                \tag{7.6}
\]

They are retained with their favorable signs. No entropy payment at \(L\ge16\) is inferred merely from these four signs.

---

## 8. An exact actual-sine obstruction to two-window monotonicity

### Claim 8.1 — DISPROVED: a uniform increasing-window rule

For a chord \(C\), define the favorable payment and two-doubling window

\[
 P_L(C)=-\frac{\operatorname{Gap}_C J_L}{2L},\qquad
 W_L(C)=P_L(C)+P_{2L}(C)
       =\frac{\operatorname{Gap}_CH_{4L}}{4L}
        -\frac{\operatorname{Gap}_CH_L}{L}.
\]

The statement

> For the actual half-density sine kernel at \(c=19/20\), for every nondegenerate midpoint chord contained in \([.02,.03]\) and every dyadic \(L\ge1\), \(W_{2L}(C)\ge W_L(C)\)

is false.

For \(C_0\), the exact certificate gives

\[
 W_4(C_0)-W_2(C_0)\in
 [-0.000000156913645376612354441510,
  -0.000000156913645376612354441509]<0.                                 \tag{8.1}
\]

### Claim 8.2 — DISPROVED: the reverse uniform window rule

The reverse inequality \(W_{2L}(C)\le W_L(C)\), with the same universal quantifiers, is false too. For the same chord,

\[
 W_2(C_0)-W_1(C_0)\in
 [0.000020337268701745119712503472,
  0.000020337268701745119712503473]>0.                                  \tag{8.2}
\]

There is also a sign reversal at the **same** comparison \(W_4-W_2\). For

\[
 C_1:\quad a_0=1/50,\quad a_1=21/1000,\quad b=41/2000,
\]

all still in the requested interval,

\[
 W_4(C_1)-W_2(C_1)\in
 [0.000000003567189615115801038458,
  0.000000003567189615115801038459]>0.                                  \tag{8.3}
\]

**Scope of the disproof.** These statements refute the specified raw two-doubling-window monotonicities, not every possible weighted or almost-monotone aggregate. They do not refute entropy-rate concavity, do not establish that some \(J_L\) has the wrong curvature, and do not use a count-only or cyclic substitute. The surviving weaker statement is the proved conditional KL supermodularity and its all-volume payment (7.4)–(7.5).

### How the finite inequalities are certified

For \(C_0\), the entropy gaps used in (8.1)–(8.2) are enclosed by the following intervals; each right endpoint is the displayed left endpoint plus \(10^{-30}\):

| \(n\) | Lower endpoint of \(\operatorname{Gap}_{C_0}H_n\) |
|---:|---:|
| 1 | 0.000050000833366668452492071068 |
| 2 | 0.000119325383139952791166872321 |
| 4 | 0.000343128881731485840644912580 |
| 8 | 0.000926250778703396183720773679 |
| 16 | 0.002267903400887087603015154952 |

For \(C_1\), the corresponding lower endpoints, again with width \(10^{-30}\), are

| \(n\) | Lower endpoint of \(\operatorname{Gap}_{C_1}H_n\) |
|---:|---:|
| 2 | 0.000001193526582057677259058602 |
| 4 | 0.000003444254061123390766761883 |
| 8 | 0.000009342379615544636002850768 |
| 16 | 0.000022970637852963269816895592 |

The deduction, for example, is the rational interval operation

\[
 W_4-W_2=
 \frac{\operatorname{Gap}H_{16}}{16}
 -\frac{\operatorname{Gap}H_8}{8}
 -\frac{\operatorname{Gap}H_4}{4}
 +\frac{\operatorname{Gap}H_2}{2}.
\]

No numerical derivative is involved.

---

## 9. Mathematical certificate interface

### Claim 9.1 — PROVED: soundness of the finite covering procedure

The certificates use the files in `S64_checks/`. The entropy, KL, and sign calculations are exact rational-interval algorithms implemented with Python arbitrary-precision integers and the standard library. Floating-point numbers are used only for elapsed-runtime metadata, never for probability, logarithm, determinant, or sign decisions.

An interval is stored as \([l,u]2^{-256}\), with integer endpoints. Every addition, multiplication, division, and reciprocal rounds outward by integer floor/ceiling. Division is permitted only after excluding zero.

For the kernel, \(\pi\) is enclosed by Machin's identity

\[
 \pi=16\arctan(1/5)-4\arctan(1/239),
\]

using 96 terms of each alternating rational series and its first-omitted-term remainder. For a positive rational endpoint, normalize it as \(2^e v\), \(1\le v<2\), and put \(z=(v-1)/(v+1)\in[0,1/3)\). The logarithm uses

\[
 \log v=2\sum_{k=0}^{53}\frac{z^{2k+1}}{2k+1}+R,
 \qquad
 0\le R\le\frac{2z^{109}}{109(1-z^2)}.
\]

The same formula at \(z=1/3\) encloses \(\log2\). Monotonicity gives a log enclosure for an interval from its two endpoints.

For a conditional kernel

\[
 K=\begin{pmatrix}q&v^*\\v&B\end{pmatrix},
\]

the next output bit has probabilities \(q\) and \(1-q\), with remaining kernels

\[
 K^{(1)}=B-vv^*/q,\qquad
 K^{(0)}=B+vv^*/(1-q).
\]

The program verifies \(0<q<1\) at every node and traverses **every binary branch**. Induction on this exact conditioning identity shows that every true atom belongs to its computed interval. The number of leaves is checked to be \(2^n\), and the enclosure for their total probability is checked to contain one. The entropy is then the interval sum of \(-p\log p\) over all leaves. This is an exhaustive finite covering of the full configuration space at the specified rational parameters.

The two full-law KL inputs at \(n=15,16\) were calculated independently in two ways:

1. the exact conditional KL chain rule, weighted by the actual endpoint prefix probabilities;
2. the full atom sum \(\sum_y p_u(y)\log(p_u(y)/p_v(y))\).

The resulting intervals intersect and give the same displayed enclosures. Entropy was independently checked by the conditional binary-entropy chain rule and by the full atom sum. For the 16-site chain-rule check, two first-bit subtrees plus the root contribution were combined; this is just an exact partition of the finite sum.

For the optional determinant-budget values, a positive Taylor series with geometric remainder encloses \(e^{1/50}\); outward-rounded LDL elimination, with every pivot verified positive, encloses the log determinant.

This procedure certifies only the stated finite inputs and counterexamples. It does not pretend to cover every parameter in an interval. Its extrapolation to all larger volumes is supplied by Theorem 4.1 and Corollary 4.2, not by sampling sizes.

### Reproduction

From `S64_checks/`:

```bash
python verify_s64.py
python verify_s64.py --recompute
python certify_pair_atoms.py --n 15 --output pair_atoms_n15.json
python certify_pair_atoms.py --n 16 --output pair_atoms_n16.json
python kl_budget_check.py
```

The first command rechecks the exact deductions from retained raw interval enclosures. The second regenerates the entropy inputs before rechecking. The atom-pair commands independently regenerate the full-law KL core. `certify_pair.py` supplies the independent conditional-chain version; its `--prefix 0` and `--prefix 1` options can split a tree, with the omitted root contribution computed separately.

---

## 10. Precise unpaid target ledger

The reviewed QWE02 bound, converted to the present midpoint-gap convention, supplies

\[
 T_{\rm QWE}(M)
 =\frac{\Gamma\eta^2}{2M}(2+\log M+\log2),\qquad
 \Gamma=\frac{32c^2}{\pi^2\delta^{12}},
\]

as an upper bound for the absolute entropy-chord dyadic tail starting at \(M\). On the benchmark interval one may take \(\delta=1/50\). This is an inherited tail bound, not a new middle-scale argument.

Combining the reviewed dyadic bridge with (7.5), for every dyadic \(M\ge16\),

\[
 \boxed{
 \operatorname{Gap}_{C_0}h
 \ge\gamma_{16}
   +\left(1-\frac{16}{M}\right)B_{16}
   -\left(\frac{\mathcal C_M}{M}-\frac{\mathcal C_{16}}{16}\right)
   -T_{\rm QWE}(M).
 }                                                                    \tag{10.1}
\]

The known limiting seed-plus-KL budget is

\[
 \gamma_{16}+B_{16}\in
 [0.000245932000395801628841632656,
  0.000245932000395801628841632657].                                    \tag{10.2}
\]

The remaining obligation is an adequate upper bound on

\[
 \frac{\mathcal C_M}{M}-\frac{\mathcal C_{16}}{16},
\]

with the actual endpoint weights, at a usable finite stopping volume, or uniformly as \(M\to\infty\). No such bound is proved here. Equivalently, (10.1) would close at a finite dyadic \(M\) if

\[
 \frac{\mathcal C_M}{M}
 \le s_{16}-\frac{16s_{16}-\mathcal D_{16}}{M}-T_{\rm QWE}(M).
\]

This is a stated open obligation, not a theorem claiming that the inequality holds. The enormous QWE02 constant is not used to manufacture a practical cutoff. No value-limit estimate is differentiated. No reference-law derivative, leakage, or probability acceleration is dropped.

### Final claim ledger

| Claim | Status | Scope / unpaid part |
|---|---|---|
| Monotone full-law and conditional likelihood ratios | PROVED | Finite strict Hermitian common diagonal shifts |
| External-field normalized-product bound | PROVED | Negatively associated laws under all required tilts |
| Conditional KL supermodularity with determinant/energy payment | PROVED | Full endpoint law and moving conditional weights |
| Stationary block-KL convexity and two-volume extrapolation | PROVED | All larger volumes, not parameter convexity |
| Retained entropy-sum inequality (5.2) | PROVED, partial | Acceleration increment remains explicit and unpaid |
| Sine determinant-budget analytic envelope | PROVED | Only the KL component; not the entropy far tail |
| Corrected-chord core and positive all-scale KL budget | PROVED | Exact finite core \(15,16\), analytic extension for KL |
| Uniform increasing two-window rule | DISPROVED | Actual sine chord \(C_0\), \(W_4<W_2\) |
| Uniform decreasing two-window rule | DISPROVED | Actual sine chord \(C_0\), \(W_2>W_1\); also \(C_1\) at the same window pair |
| Complete benchmark entropy-rate chord payment | INCOMPLETE | No adequate upper bound for the acceleration increment |
| Fixed-interval / universal whole-interval entropy concavity | INCOMPLETE | Not implied by the finite core or the KL theorem |

No repository-wide status file was edited, no work was merged, and no other researcher was contacted.
