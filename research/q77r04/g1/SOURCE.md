## 0. Exact scope and relation to the source question

Let Γ be a countable discrete group, let S be a finite nonempty set with m=|S|, and put W=Γ×S. The action is g·(γ,a)=(gγ,a). Let H=ℓ²(W) and let Q∈B(H) be a self-adjoint Γ-equivariant positive contraction, 0≤Q≤I. Define the DPP P^Q on {0,1}^W by

\[
\mathbf P^Q[B\subseteq X]=\det Q[B]
\quad\text{for every finite }B\subseteq W. \tag{0.1}
\]

**Proposed theorem.** There is a measurable Γ-equivariant map from the iid Bernoulli shift [0,1]^Γ into {0,1}^W whose image law is P^Q. More precisely, one spatial iid field of unit-rate Poisson random measures N_x on [0,∞)×[0,1], x∈W, gives an equivariant pure-birth process X with

\[
X_s\subseteq X_t\ (s\le t),\qquad
X_s\sim\mathbf P^{t_sQ},\quad t_s=1-e^{-s},\qquad
X_\infty=\bigcup_{s\ge0}X_s\sim\mathbf P^Q. \tag{0.2}
\]

A finite product of standard Poisson spaces at each γ is a standard atomless probability space, hence can be encoded measurably by one uniform label at γ. The conclusion is a measurable Bernoulli factor, with no finitary coding claim.

The [Lyons–Thom paper](https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf), Theorem 7.3 and Corollary 7.4, explicitly treats R(Γ) and R(Γ,S)≅M_S(R(Γ)) for finite generating S. Its edge action is identified with the free left action on Γ×S by sending (γ,a) to the labelled edge (γ,γa). Question 7.7 then asks for Bernoulli factors of DPPs of equivariant positive contractions. The candidate above covers these finite free-orbit matrix kernels if its proof passes review. It does **not** assert a result for infinitely many orbit types or arbitrary Γ-sets with stabilizers. The derivation below needs only that S is finite and nonempty; S need not generate Γ for the abstract Γ×S theorem.

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

## 4. Finite windows: law and full-past intensity

Assume through Section 6 that Q≥cI for some c>0. Choose finite F_n↑Γ and set W_n=F_n×S. On a finite W_n, compress Q to Q^{[n]}=P_{W_n}Q P_{W_n} acting on ℓ²(W_n). Sample Z_n∼P^{Q^{[n]}} and assign independent Exp(1) arrival clocks E_x to its occupied sites. Let Y_s^n be the born set by s. Independent thinning gives Y_s^n∼P^{t_sQ^{[n]}}.

For x∈W_n let R_x(s)=1_{x∈Z_n,E_x>s} and let H^{[n]}_{s-}=σ(Y_r^n: r<s), the **complete** observed finite past. If η=Y_{s-}^n, the observed birth times of η add no information about as-yet unborn terminal points beyond η: given a terminal set Z_n=T⊇η and those birth times r_y<s, the factor of its likelihood depending on T is (1-t_s)^{|T\setminusη|}; the factor ∏_{y∈η}e^{-r_y} is independent of T. Therefore, for s>0 and x∉η,
\[
\lambda_x^{[n]}(s)
=\mathbb E[R_x(s)\mid H^{[n]}_{s-}]
=\frac{e^{-s}}{t_s}
  \frac{\mu_s^{[n]}(\eta\cup\{x\})}{\mu_s^{[n]}(\eta)}, \tag{4.1}
\]
where μ_s^{[n]}(η) denotes the **exact entire configuration** probability on W_n. The ratio follows by summing over terminal T⊇η∪{x}; multiplying μ_s^{[n]}(η∪{x}) by (1-t_s)/t_s produces the numerator of the conditional expectation. At s=0 the quotient is interpreted by its operator-rate limit; the single time has zero compensator measure.

Since Q^{[n]}≥cI_{W_n}, K_s=t_sQ^{[n]} has a strictly positive finite L-ensemble L_s=K_s(I-K_s)^{-1}. Its exact probabilities are
\[
\mu_s^{[n]}(\eta)=\det(I-K_s)\det L_s[\eta].
\]
The determinant ratio in (4.1) is the Schur complement of L_s at x over η. Shorting is homogeneous under positive scalar multiplication, and A_s^{[n]}=(e^{-s}/t_s)L_s. Thus
\[
\lambda_x^{[n]}(s)
=b_{A_s^{[n]}}(x,Y_{s-}^n),\qquad
A_s^{[n]}=e^{-s}Q^{[n]}(I-t_sQ^{[n]})^{-1}. \tag{4.2}
\]
This is a full-past intensity identity, not only a present-state conditional probability.

## 5. Moving F_n×S shorting and the infinite past

Construct an invariant **weak** process by sampling Z∼P^Q on W and independent Exp(1) arrival clocks; write Y_s for born sites. This process is not yet asserted to be FIID. Its restriction to W_n has the finite law above. Let P_n=P_{W_n}, extend Q_n=P_nQP_n by zero outside W_n, and put A_{s,n}=f_s(Q_n), where f_s is the scalar function from Section 3. Since f_s(0)=0, A_{s,n} is precisely A_s^{[n]} extended by zero. We have Q_n→Q strongly and A_{s,n}→A_s strongly.

For any finite time horizon T and s∈[0,T],
\[
A_{s,n}\ge c_T P_n,\qquad
c_T=\frac{e^{-T}c}{1-(1-e^{-T})c}>0. \tag{5.1}
\]
For a fixed arbitrary η⊆W, possibly infinite, let D_n=P_{\ell²(\eta\cap W_n)}, D=P_{\ell²(\eta)}, and
\[
C_{s,n}=D_nA_{s,n}D_n+I-D_n,\qquad
C_s=DA_sD+I-D.
\]
Then D_n→D strongly, C_{s,n}→C_s strongly, and C_{s,n}≥min(c_T,1)I. The resolvent identity and uniform inverse bound give C_{s,n}^{-1}→C_s^{-1} strongly. The variational minimization (1.2), now using the strict lower bound on the constrained subspace, gives
\[
\mathsf S_{\eta\cap W_n}(A_{s,n})
=A_{s,n}-A_{s,n}D_nC_{s,n}^{-1}D_nA_{s,n}. \tag{5.2}
\]
Every factor is uniformly bounded and has a strong limit, so the right side converges strongly to \mathsf S_\eta(A_s). Consequently, for each fixed x∈W,
\[
b_{A_s^{[n]}}(x,\eta\cap W_n)\longrightarrow b_{A_s}(x,\eta)
\quad\text{once }x\in W_n. \tag{5.3}
\]
This handles both the moving finite window and the moving occupied projection. Fixed-η one-sided continuity from Section 1 is not being substituted for (5.3).

For the weak Y, let H^{(n)}_{s-}=σ(Y_r(x):x∈W_n,r<s), and H_{s-}=σ(Y_r(x):x∈W,r<s). Because W=∪_n W_n is countable, H^{(n)}_{s-}↑H_{s-}. Formula (4.2) gives
\[
\mathbb E[R_x(s)\mid H^{(n)}_{s-}]
=b_{A_s^{[n]}}(x,Y_{s-}\cap W_n)
\quad\text{for fixed }x\in W_n,
\]
where now R_x(s)=1_{x∈Z,E_x>s}. The left side converges by bounded martingale convergence; the right side by (5.3) samplewise. Hence, in a ds⊗dP version,
\[
\lambda_x(s):=\mathbb E[R_x(s)\mid H_{s-}]
=b_{A_s}(x,Y_{s-}). \tag{5.4}
\]
The Borel argument in Section 1 and predictability of Y_{s-} show the right side is H-predictable. For every bounded nonnegative H-predictable test process U_s, the exponential-clock construction gives
\[
\mathbb E\int U_s\,dY_s(x)
=\mathbb E\int U_s R_x(s)\,ds
=\mathbb E\int U_s\lambda_x(s)\,ds.
\]
Therefore (5.4) is the compensator density with respect to the complete natural past, not merely a fixed-time posterior.

## 6. Progressive Poisson completion, joint invariance, and identification

At a true jump (x,s) of Y, reveal a fresh U[0,1] mark V_x **at the jump time only** and give that jump proposal mark u=λ_x(s)V_x. Let M be an independent unit-rate PRM on W×[0,∞)×[0,1]. Retain its proposals with u>λ_x(s), and let N be the union of these virtual proposals with the marked true births. A true jump at λ_x(s)=0 has probability zero by (5.4).

Let G_s be the completed right-continuous filtration generated by Y through s, the real marks progressively revealed through s, and M through s. It does not reveal the latent terminal Z or a future true-jump mark at time zero. Independence of M and the progressive independent marks preserve the unmarked real-jump compensator λ_x(s)ds in G: for simple bounded G-predictable test functions, condition first on the Y-past and on marks revealed at prior jumps; the latter and M-past are conditionally independent of future latent jumps. A monotone-class argument extends the equality to bounded predictable tests. The real marked jumps therefore have G-compensator 1_{0<u≤λ_x(s)}dsdu. Independent thinning of M gives the virtual jumps G-compensator 1_{λ_x(s)<u≤1}dsdu. Their sum N has deterministic G-compensator
\[
\nu(dx\,ds\,du)=\#_W(dx)\,ds\,du. \tag{6.1}
\]

Here is the Poisson characterization at the precision needed for this candidate. Fix finitely many sites and a finite future time interval (t,T]. For bounded deterministic h≥0 supported there, define for t≤r≤T
\[
Z_r=
\exp\!\left[-\int_{(t,r]}h\,dN+
             \int_{(t,r]}(1-e^{-h})\,d\nu\right].
\]
The compensator formula makes Z_r a local martingale. It is bounded above by exp(ν(supp h)) on this finite window, hence is a true martingale. Conditional on G_t,
\[
\mathbb E\left[e^{-\int_{(t,T]}h\,dN}\mid G_t\right]
=\exp\!\left[-\int_{(t,T]}(1-e^{-h})\,d\nu\right]. \tag{6.2}
\]
Given Z, the true exponential clocks are independent and continuous; M is diffuse and independent, so on finite site sets no simultaneous jumps occur. Apply (6.2) first to simple h on disjoint site/mark/time cells, then approximate. It gives independent Poisson future increments of the specified rates relative to G. Finite-site consistency yields that N=(N_x)_{x∈W} is a spatial iid field of PRMs **in the common filtration G**.

The process Y is G-adapted. Real points have u≤λ_x(s), virtual points have u>λ_x(s), and there are no other proposals. Thus, up to the usual null boundary event,
\[
Y_t(x)=\mathbf1\{\exists(s,u)\in N_x:
s\le t,\ u\le b_{A_s}(x,Y_{s-})\}. \tag{6.3}
\]
The law of Y is Γ-invariant. The rate λ is covariant, and the progressive marks and M are iid under the Γ action, so (Y,N) is **jointly invariant**. The Picard solution X(N) from Section 3 is a G-adapted equivariant function of the PRM past; (X,Y) is jointly invariant as well. Both solve (6.3) from ∅ under the same G-PRM. The label-summed uniqueness result from Section 3 yields Y=X(N) almost surely. This does not assume that the weak Y was already adapted to the natural filtration of N. Its extra randomness is removed by pathwise uniqueness.

Independent thinning of the terminal Z gives, for Q≥cI,
\[
X_s\sim Y_s\sim\mathbf P^{t_sQ}
\quad\text{for every finite }s. \tag{6.4}
\]

## 7. One-noise regularization, including every label

For 0<ε≤1 put Q^ε=εI+(1−ε)Q. These equivariant positive contractions satisfy Q^ε≥εI and Q^ε↓Q as ε↓0. Because all are functions of Q, the scalar monotonicity of f_s gives A_s^ε=f_s(Q^ε)↓A_s. Section 1 then gives for each fixed s,x,η
\[
b_{A_s^\varepsilon}(x,\eta)\downarrow b_{A_s}(x,\eta). \tag{7.1}
\]

Build X^ε and X by the **same** PRM N. For a finite horizon T put
\[
D_\varepsilon(T)=\sum_{a\in S}\mathbb P\{
 X^\varepsilon_\cdot(x_a)\ne X_\cdot(x_a)
 \text{ somewhere on }[0,T]\},
\]
and
\[
h_\varepsilon(s)=\sum_{a\in S}
 \mathbb E\left[
 b_{A_s^\varepsilon}(x_a,X_{s-})
 -b_{A_s}(x_a,X_{s-})\right].
\]
All relevant pairs are jointly invariant. Compare thresholds by adding and subtracting b_{A_s^\varepsilon}(x_a,X_{s-}). PRM compensation and the **summed** estimate (2.2) give
\[
D_\varepsilon(T)
\le\int_0^T D_\varepsilon(s)\,ds
  +\int_0^T h_\varepsilon(s)\,ds. \tag{7.2}
\]
Here 0≤h_ε(s)≤m, and (7.1) with bounded convergence gives h_ε(s)→0. Dominated convergence on [0,T] and Grönwall imply D_ε(T)→0. Translation covariance and the finite label set imply convergence in probability of X_T^ε to X_T on every finite B⊂W. Each X_T^ε has P^{t_TQ^ε} law by (6.4), and finite determinants converge to those of t_TQ. Thus
\[
X_T\sim\mathbf P^{t_TQ}. \tag{7.3}
\]

All X_s are monotone functions of the same N. The union X_∞ is measurable and equivariant, since its membership at each x is the supremum over integer times. For finite B⊂W,
\[
\mathbb P[B\subseteq X_\infty]
=\lim_{n\to\infty}\det(t_nQ[B])
=\det Q[B].
\]
These inclusion probabilities determine P^Q, so (0.2) follows subject to fresh review of the whole V3 proof. At s_n=n\log2 the candidate gives a compatible path Q_n=(1−2^{-n})Q. For each a,
\[
\mathbb P[X_\infty(x_a)\ne X_{s_n}(x_a)]
=2^{-n}\langle Q\delta_{x_a},\delta_{x_a}\rangle,
\]
and the sum over a is at most m\,2^{-n}. This is a marginal consequence of the proposed path construction; it is not a finitary stopping certificate.

