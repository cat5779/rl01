> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# A one-sided refinement: retain the Fisher gain

**Author proof; independent review pending.** This is a direct corollary of
Theorem F, not a third promoted method or a proof of the target. Convexity of
conditional Fisher information is an elementary input, not a novelty claim.
Its use removes an avoidable positive error from the sign-testing interface.

Use all notation of AVERAGED_LOCALIZATION.md. In particular f(u)=1/[u(1-u)],
K_(R,L) is its actual finite local conditional-table expression, and B_*,C_*,
delta,m,M are the explicitly defined strict-channel constants.

## Corollary G: the finite and limiting upper enclosures

For all positive integers n,R,L,

\[
\begin{aligned}
 H_n''/n\le{}&\mathcal K_{R,L}+C_*/R
 +\frac{156(R-1)B_*\delta^{-4}m^{-2}}L\\
 &+\frac{\delta^{-2}}n
       [4L+M\{8L(R-1)+R(R-1)\}].
\end{aligned}                                                \tag{1}
\]

Consequently,

\[
 \boxed{\quad h_\rho''\le\mathcal K_{R,L}+C_*/R
 +156(R-1)B_*\delta^{-4}m^{-2}/L.\quad}          \tag{2}
\]

Thus the single-site term B_* delta^(-4) m^(-1)/L in the absolute error is
unnecessary for an upper bound. The remaining pair-observation error is
unchanged. Neither term in (2) is claimed to have the sign needed to finish.

**Proof.** For an interior site i, let u_i^B be the conditional probability
given every other output in B and let u_i^L be the conditional probability
given the local window. The local sigma-field is a sub-sigma-field of the
full one, so E[u_i^B|local]=u_i^L. Since

\[
 f(u)=1/u+1/(1-u),\qquad
 f''(u)=2/u^3+2/(1-u)^3\ge32,
\]

conditional Jensen gives E f(u_i^B)>=E f(u_i^L). The negative Fisher diagonal
can therefore be replaced by its local counterpart with no positive cost.
For boundary sites use exactly the paid bound in Theorem F; for all mixed
pairs use that theorem's actual-law coarsening estimate (3.6). Its far-pair
and boundary bounds are unchanged. This proves (1). The already proved
curvature convergence on strict compact intervals gives (2). QED.

## A further negative term, not needed for the finite certificate

Let

\[
 u^\infty=\mathbb P(Y_0=1\mid Y_j,\ j\ne0),\qquad
 V_L=\mathbb E[(u^\infty-u^{(L)})^2].
\]

These variables exist by the bounded martingale convergence theorem applied
to expanding finite observation windows. Both lie in [a,a+c]. One may retain
an additional negative contribution:

\[
 \boxed{\quad h_\rho''\le\mathcal K_{R,L}-16V_L+C_*/R
 +156(R-1)B_*\delta^{-4}m^{-2}/L.\quad}          \tag{3}
\]

To justify this without an uncontrolled infinite-volume differentiation,
apply strong convexity conditionally at each interior site in the FINITE
proof of (1):

\[
 \mathbb E f(u_i^B)-\mathbb E f(u_i^L)
 \ge16\mathbb E[(u_i^B-u_i^L)^2].               \tag{4}
\]

The right side equals 16(E[(u_i^B)^2]-E[(u_i^L)^2]) by the tower rule. For any
fixed N>=L, every site at distance at least N from the boundary has, in the
ordering of sigma-fields, its radius-N local observations contained in its
full B-outside observations, contained in all outside observations. Therefore

\[
 \mathbb E[(u^{(N)})^2]\le\mathbb E[(u_i^B)^2]
                          \le\mathbb E[(u^\infty)^2].
\]

Stationarity is used only for the two endpoint expectations. At most 2N sites
fail this inclusion. First n tends to infinity at fixed N,L; then N tends to
infinity, using bounded L^2 martingale convergence. The normalized sum of
(4) converges to at least 16V_L. Passing through the finite inequality proves
(3). No derivative of a tail limit or kernel-mixture identity was assumed.

For reference the exact scalar Bregman identity is

\[
 f(u)-f(v)-f'(v)(u-v)
 =(u-v)^2\left\{\frac1{uv^2}
       +\frac1{(1-u)(1-v)^2}\right\}.
\]

After conditional averaging its linear term vanishes; the coefficient has
the lower bound 16 by the strong-convexity argument above. This identifies
what the additional negative term measures: information about a single
output supplied by remote observations. It is not a proved compensation for
the near-pair positive terms. V_L is not introduced as a new finite observable
whose value has already been certified. Dropping it yields the fully finite,
usable upper enclosure (2).

## Remaining sign problem

A sufficient finite-block certificate is now

    K_(R,L) + C_*/R + 156(R-1) B_* delta^(-4) m^(-2)/L <= 0.

The manuscript does not prove this uniformly in the requested high-contrast
range. The positive averaged six-site pair still rules out pairwise sign
arguments. The principal new mathematical work remains the quantitative
actual-law spatial bounds; this corollary only avoids wasting the Fisher
term's favorable conditional sign.
