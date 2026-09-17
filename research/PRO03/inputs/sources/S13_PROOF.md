> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

INCOMPLETE_TARGET__PROVED_SIGNED_COMPONENT

# S13 round 3: an extensive favorable clock-curvature component in the corrected-law divergence response

## 1. Status, scope, and new question

All logarithms are natural.  The complete-configuration sine entropy-rate target
remains open.  This note keeps the half-density cyclic Fourier family, even
`n`, and the exact channel from the pinned target.  It does not promote any
unreviewed round-2 asymptotic theorem to reviewed status.

The new question is narrower and genuinely downstream of the positive
potential-clock construction:

> After retaining the actual moving count weights, can one pay a signed,
> quantitatively nontrivial part of the corrected law's full divergence
> response, rather than merely observing a positive Fisher term?

The answer below is yes.  At the symmetric legal shift, the corrected clock has
strictly negative second response.  Its product with Bernoulli--Laplace entropy
dissipation gives an **explicit favorable linear-in-`n` contribution**.  The
proof includes the actual `pi_l`, proves count-tail control, derives the clock
curvature, lower-bounds entropy production from a nonzero averaged degree-two
pair mode, and reconstructs the slice modified log-Sobolev normalization.
The moving-count term left beside it is still unpaid, so this is not a full sign
for the corrected law or the target.

Fix `0<c<1`, put

\[
 a_*={1-c\over2},\qquad z_* = \left({1+c\over1-c}\right)^2,
 \qquad z''(a_*)={32c\over(1-c)^4}.                                  \tag{1.1}
\]

Let `n=2k`.  The input is the projection DPP for the first `k` cyclic Fourier
columns.  On the `l`-slice, `u_l` denotes the uniform law and

\[
 (L_l f)(S)={1\over l(n-l)}\sum_{i\in S}\sum_{j\notin S}
 [f(S-i+j)-f(S)]                                                       \tag{1.2}
\]

is the total-rate-one Bernoulli--Laplace generator.  The averaged maximal-
overlap density relative to `u_l` is `r_l^max`.  For `2<=l<=n-2`, the exact
actual degree-two multiplier is `theta_(n,l)(z)` and

\[
 \widehat\tau_l(a)=-{\log\theta_{n,l}(z(a,c))\over\gamma_{2,l}},
 \qquad \gamma_{2,l}={2(n-1)\over l(n-l)},
 \qquad
 \widehat q_l(a)=u_l e^{\widehat\tau_l(a)L_l}r_l^{\max}.               \tag{1.3}
\]

The already checked algebraic gate `0<theta<1` makes (1.3) a positive normalized
law and ensures exact layerwise matching of the Fourier pair-potential mean.
Those facts are re-derived where used below.  On `l=0,1,n-1,n` define
`widehat q_l=u_l`; the centered pair-potential and the averaged nonuniform mode
both vanish there, so this endpoint convention is exact for every term used
below.

For completeness, here is the exact finite-`n` multiplier used throughout.  For
`l<=k`, condition on an input `A` and let `J=|A intersect S|` under

\[
 P(J=j)={ {k\choose j}{k\choose l-j}z^j\over Z_{n,l}(z)},\qquad
 Z_{n,l}(z)=\sum_j{k\choose j}{k\choose l-j}z^j.                    \tag{1.4}
\]

Put `lambda=(2EJ-l)/l`, `v=Var(J)`, and
`alpha_(n,l)=l(l-1)/[k(k-1)]`.  Testing the conditional kernel on
`(x_i-x_j)(x_r-x_s)` with `i,r in A`, `j,s notin A`, and using exchangeability
inside the two groups gives

\[
 \theta_{n,l}=\lambda^2+
 {4(n-1)v-l(n-l)(1-\lambda^2)\over nl(l-1)}.                         \tag{1.5}
\]

Indeed, conditional on `J`, the test expectation is

\[
 {E[J(J-1)]+E[(l-J)(l-J-1)]\over k(k-1)}
 -{2E[J(l-J)]\over k^2};                                              \tag{1.6}
\]

substitution of `EJ=l(1+lambda)/2` and `EJ^2=v+(EJ)^2`, followed by division
by the maximal-overlap value `alpha_(n,l)`, yields (1.5).  Equivalently, the
four signed choices in the test combine to

\[
 \theta_{n,l}=
 {(z-1)^2\sum_j{k-2\choose j}{k-2\choose l-2-j}z^j
  \over \alpha_{n,l}Z_{n,l}(z)}.                                    \tag{1.7}
\]

For `l>k`, complement both the output set and the input set.  The complement
input has projection `I-P`; its off-diagonal squared moduli equal those of `P`,
and the minority overlap again has parameter `z`.  Hence
`theta_(n,l)=theta_(n,n-l)`.

Let `phi_ij=log|e^(2pi i i/n)-e^(2pi i j/n)|^2`.  The root-discriminant
identity gives `sum_(j!=i) phi_ij=2 log n`.  Hence the centered potential

\[
 \overline U_{n,l}=U_n-E_{u_l}U_n                                   \tag{1.8}
\]

has zero row sums and is pure Johnson degree two.  Direct swap summation gives

\[
 L_l\overline U_{n,l}=-\gamma_{2,l}\overline U_{n,l}.               \tag{1.9}
\]

The actual conditional kernel multiplies this mode by `theta_(n,l)`, while
maximal overlap supplies its initial amplitude.  Thus the clock in (1.3)
satisfies `exp(-gamma_(2,l) tauhat_l)=theta_(n,l)` and exactly matches
`E U_n` layer by layer.  This proves the matching used later without importing
the round-2 narrative.

Let `pi_l(a,c)=Pr(M=l)` be the **actual** count weights,

\[
 \sum_l\pi_l t^l=[1-a-c+(a+c)t]^k[1-a+at]^k.                         \tag{1.10}
\]

## 2. Exact derivative ledger before any estimate

For fixed `l`, write

\[
 q_{l,t}=u_l e^{tL_l}r_l^{\max},\qquad
 K_l(t)=D(q_{l,t}\Vert u_l).                                          \tag{2.1}
\]

If `r_{l,t}=dq_{l,t}/du_l`, define the entropy production

\[
 \mathcal I_l(t)
 =-K_l'(t)
 =-\langle L_lr_{l,t},\log r_{l,t}\rangle_{u_l}                       \tag{2.2}
\]

\[
 ={1\over2l(n-l)}\sum_Su_l(S)\sum_{S'\sim S}
 (r_{l,t}(S')-r_{l,t}(S))
 (\log r_{l,t}(S')-\log r_{l,t}(S))\ge0.                              \tag{2.3}
\]

Let `U_n` be the cyclic Fourier logarithmic pair-potential and put

\[
 P_l(t)=E_{q_{l,t}}U_n-E_{u_l}U_n=A_{n,l}e^{-\gamma_{2,l}t}.           \tag{2.4}
\]

For the Fourier Gibbs reference `nu_(n,l)(S)=n^{-l}e^{U_n(S)}`, set

\[
 D_l(t)=D(q_{l,t}\Vert\nu_{n,l}).                                     \tag{2.5}
\]

Since

\[
 D_l(t)=K_l(t)-P_l(t)+B_{n,l},\qquad
 B_{n,l}=l\log n-\log{n\choose l}-E_{u_l}U_n,                         \tag{2.6}
\]

we have the exact time derivatives

\[
 \partial_tD_l=-\mathcal I_l+\gamma_{2,l}P_l,\qquad
 \partial_t^2D_l=-\mathcal I_l'-\gamma_{2,l}^2P_l.                   \tag{2.7}
\]

Therefore every chain-rule term is

\[
 \widehat D_l'
 =\widehat\tau_l'(-\mathcal I_l+\gamma_{2,l}P_l),                     \tag{2.8}
\]

\[
 \widehat D_l''
 =\widehat\tau_l''(-\mathcal I_l+\gamma_{2,l}P_l)
 +(\widehat\tau_l')^2(-\mathcal I_l'-\gamma_{2,l}^2P_l),             \tag{2.9}
\]

with all quantities on the right evaluated at `t=widehat tau_l(a)`.
Consequently the full corrected reference response is, **before any bound**,

\[
\begin{aligned}
 \widehat D_F''
 =\sum_l\{&\pi_l''D_l
 +2\pi_l'\widehat\tau_l'(-\mathcal I_l+\gamma_{2,l}P_l)\\
 &+\pi_l[\widehat\tau_l''(-\mathcal I_l+\gamma_{2,l}P_l)
 +(\widehat\tau_l')^2(-\mathcal I_l'-\gamma_{2,l}^2P_l)]\}.
                                                                         \tag{2.10}
\end{aligned}
\]

No Fisher, acceleration, score--layer, or count-acceleration term has been
dropped.

It is useful to combine the same terms relative to the uniform slice law:

\[
 \widehat K_n(a)=\sum_l\pi_l(a,c)K_l(\widehat\tau_l(a)).              \tag{2.11}
\]

Then exactly

\[
\begin{aligned}
 \widehat K_n''=\sum_l\{&\pi_l''K_l-2\pi_l'\widehat\tau_l'\mathcal I_l\\
 &+\pi_l[-\widehat\tau_l''\mathcal I_l
 -(\widehat\tau_l')^2\mathcal I_l']\}.
                                                                         \tag{2.12}
\end{aligned}
\]

To identify the reference terms, note first that `E M=na+ck`, so
`(E M log n)''=0`.  Also, for `i!=j`,

\[
 E(Y_iY_j)=a^2+ac(E X_i+E X_j)+c^2E(X_iX_j).
\]

At half density `E X_i=1/2`, and `sum_(i<j) phi_ij=n log n`; therefore

\[
 E U_n(Y)=(a^2+ac)n\log n+c^2E U_n(X),\qquad
 (E U_n(Y))''=2n\log n.                                             \tag{2.13a}
\]

The Fourier-potential matching and (2.6) now give

\[
 \widehat D_F''=\widehat K_n''-2n\log n-
 \left(\sum_l\pi_l\log{n\choose l}\right)'',                        \tag{2.13}
\]

and hence

\[
 \widehat H''=\Phi''-\widehat K_n'',\qquad
 \Phi=H(M)+\sum_l\pi_l\log{n\choose l}.                              \tag{2.14}
\]

Equation (2.13) preserves the normalization correction: `(E M log n)''=0`,
while the negative Fourier-potential expectation supplies `-2n log n`.

At `a=a_*`, `z'(a_*)=0`; hence

\[
 \widehat\tau_l'(a_*)=0                                                \tag{2.15}
\]

and the exact aggregate becomes

\[
 \boxed{\widehat K_n''(a_*)=\mathcal W_n(c)+\mathcal C_n(c)},          \tag{2.16}
\]

where

\[
 \mathcal W_n(c)=\sum_l\pi_l''(a_*,c)K_l(\widehat\tau_l(a_*)),         \tag{2.17}
\]

\[
 \boxed{\mathcal C_n(c)=\sum_l\pi_l(a_*,c)
 [-\widehat\tau_l''(a_*)]\,\mathcal I_l(\widehat\tau_l(a_*)).}       \tag{2.18}
\]

The new theorem pays (2.18).  The moving-count term (2.17) is not assigned a
sign here.

## 3. New signed theorem

Define

\[
 d_c={c^2\over\pi^2},\qquad p_-(c)={1\over4}-d_c,
 \qquad p_+(c)={1\over4}+d_c,                                         \tag{3.1}
\]

\[
 J_{\rm pair}(c)=\log2+p_-(c)\log p_-(c)+p_+(c)\log p_+(c)>0,          \tag{3.2}
\]

and equivalently

\[
 D_{\rm pair}(c)=2J_{\rm pair}(c)
 =2[p_-\log(4p_-)+p_+\log(4p_+)].                                    \tag{3.3}
\]

### Theorem 3.1 (paid corrected-clock entropy-production component)

For every fixed `0<c<1`, along even `n -> infinity`,

\[
 \boxed{
 \liminf_{n\to\infty}{\mathcal C_n(c)\over n}
 \ge {2\over1-c^2}D_{\rm pair}(c)
 ={4\over1-c^2}J_{\rm pair}(c)>0.}                                   \tag{3.4}
\]

Thus the clock-curvature part of the corrected uniform-divergence response is
favorable and at least extensive.  It enters `widehat D_F''` with the same
positive sign and enters `widehat H''` with the favorable negative sign.

For the requested high-contrast point `c=19/20`,

\[
 d_c=0.09144236823720985\ldots,\qquad
 D_{\rm pair}=0.06847130817780112\ldots,                              \tag{3.5}
\]

and

\[
 \boxed{
 \liminf_{n\to\infty}{\mathcal C_n(19/20)\over n}
 \ge 1.4045396549292533\ldots .}                                    \tag{3.6}
\]

This is not merely positivity of Fisher information: (3.4) multiplies a
proved asymptotic clock-curvature constant by an explicit, mode-certified
modified-log-Sobolev lower bound on entropy production, and then averages with
the actual count law while paying its tails.

## 4. Exact monotonicity and midpoint clock curvature

Take `l<=k`; complementation handles `l>k`.  Put `y=z-1`.  The exact coefficient
expansions are

\[
 Z_{n,l}(1+y)=\sum_{r=0}^lc_r y^r,
 \quad c_r={k\choose r}{2k-r\choose l-r},                              \tag{4.1}
\]

\[
 y^2B_l(1+y)=\sum_{r=0}^lc_rq_r y^r,                                  \tag{4.2}
\]

where `q_0=q_1=0` and, for `r>=2`,

\[
 q_r={r(r-1)(2k-l)(2k-l-1)
 \over k(k-1)(2k-r)(2k-r-1)}.                                        \tag{4.3}
\]

The sequence `q_r` is strictly increasing, and `q_l=alpha_(n,l)`.  If
`R` has probabilities proportional to `c_r y^r`, then

\[
 \theta_{n,l}(1+y)={E q_R\over\alpha_{n,l}},\qquad
 y\partial_y\theta_{n,l}={\operatorname{Cov}(R,q_R)\over\alpha_{n,l}}>0.
                                                                         \tag{4.4}
\]

This re-proves `0<theta<1` and also proves the new fact needed here:

\[
 \partial_z\log\theta_{n,l}(z)>0.                                    \tag{4.5}
\]

At the midpoint,

\[
 -\widehat\tau_l''(a_*)
 ={z''(a_*)\over\gamma_{2,l}}\partial_z\log\theta_{n,l}(z_*)>0.          \tag{4.6}
\]

Let

\[
 \mathcal B_n=\{l:|l-n/2|\le n^{2/3}\}.                              \tag{4.7}
\]

### Lemma 4.1 (specialized central overlap asymptotics)

Uniformly for `l in B_n`, with `r=min(l,n-l)` and overlap law

\[
 P(J=j)={ {k\choose j}{k\choose r-j}z_*^j\over Z_{n,r}(z_*)},          \tag{4.8}
\]

\[
 {2EJ-r\over r}\to c,\qquad
 {\operatorname{Var}(J)\over n}\to {1-c^2\over16},                   \tag{4.9}
\]

and

\[
 \sup_{l\in\mathcal B_n}E|J-EJ|^3=O_c(n^{3/2}).                       \tag{4.10}
\]

Consequently

\[
 \theta_{n,l}(z_*)\to c^2,\qquad
 \partial_z\log\theta_{n,l}(z_*)
 \to {(1-c)^3\over2c(1+c)}                                           \tag{4.11}
\]

uniformly on `B_n`.

#### Proof

Write `x=r/n` and `t=j/n`.  Since `r<=k`, the feasible interval is
`0<=t<=x`.  Define

\[
 \psi_x(t)={1\over2}h(2t)+{1\over2}h(2x-2t)+t\log z_*,               \tag{4.12}
\]

where `h(s)=-s log s-(1-s)log(1-s)`.  Its first two derivatives are

\[
 \psi_x'(t)=
 \log {1-2t\over2t}+
 \log {2x-2t\over1-2x+2t}+\log z_*,                                  \tag{4.13}
\]

\[
 \psi_x''(t)=
 -{1\over t(1-2t)}
 -{1\over (x-t)(1-2x+2t)}<0.                                         \tag{4.14}
\]

For `x` in a fixed neighborhood of `1/2`, there is therefore a unique
maximizer `t_x`, it stays a fixed positive distance from the endpoints, and it
depends smoothly on `x`.  The saddle equation is

\[
 z_*(1/2-t_x)(x-t_x)=t_x(1/2-x+t_x).                                 \tag{4.15}
\]

At `x=1/2`,

\[
 t_{1/2}={1+c\over4},\qquad
 \psi_{1/2}''(t_{1/2})=-{16\over1-c^2}.                              \tag{4.16}
\]

We now give the uniform discrete Laplace step rather than invoking an
uncontrolled limit exchange.  Let

\[
 w_{n,x}(j)={k\choose j}{k\choose r-j}z_*^j,
 \qquad m_x=\lfloor nt_x\rceil.                                      \tag{4.17}
\]

The exact successive-weight ratio is

\[
 R_{n,x}(j):={w_{n,x}(j+1)\over w_{n,x}(j)}
 =z_*{(k-j)(r-j)\over(j+1)(k-r+j+1)}.                                \tag{4.18}
\]

On a fixed central interval containing every `t_x`, Taylor expansion of
`log R_(n,x)(j)` about `j=nt_x`, using (4.15), is uniform and gives

\[
 \log R_{n,x}(j)
 =\psi_x''(t_x){j-nt_x\over n}
 +O_c\!\left({1\over n}+{(j-nt_x)^2\over n^2}\right).               \tag{4.19}
\]

Moreover, direct differencing of (4.18) gives

\[
\begin{aligned}
 \log R_{n,x}(j+1)-\log R_{n,x}(j)
 ={}&\log\!\left(1-{1\over k-j}\right)
 +\log {j+1\over j+2}\\
 &+\log\!\left(1-{1\over r-j}\right)
 +\log {k-r+j+1\over k-r+j+2}.                                      \tag{4.20}
\end{aligned}
\]

Thus, uniformly in `x=1/2+O(n^(-1/3))`, there are constants
`0<eta_c<C_c<infinity` such that, throughout that central interval,

\[
 -{C_c\over n}\le
 \log R_{n,x}(j+1)-\log R_{n,x}(j)
 \le-{\eta_c\over n}.                                                \tag{4.21}
\]

Outside the central interval the strict concavity in (4.14) gives a fixed
one-sided ratio gap.  Since (4.19) also gives `log R_(n,x)(m_x)=O_c(1/n)`,
summing the ratio bounds proves both

\[
 c_c\sqrt n\,w_{n,x}(m_x)
 \le Z_{n,r}(z_*)\le C_c\sqrt n\,w_{n,x}(m_x),                       \tag{4.22}
\]

and the normalized sub-Gaussian estimate

\[
 P\{|J-m_x|\ge s\sqrt n\}\le C_c e^{-\eta_c s^2}
 \quad(s\ge0).                                                       \tag{4.23}
\]

For each bounded real `u`, summing (4.19) from `m_x` to
`m_x+floor(u sqrt(n))` yields, uniformly for `x=1/2+O(n^(-1/3))`,

\[
 \log {w_{n,x}(m_x+\lfloor u\sqrt n\rfloor)\over w_{n,x}(m_x)}
 ={1\over2}\psi_x''(t_x)u^2+o_c(1).                                 \tag{4.24}
\]

Equations (4.22)--(4.24) turn the normalizing sum into a Riemann sum.
The domination (4.23) permits passage of the zeroth, first, second, and third
absolute moments.  Therefore, uniformly on `B_n`,

\[
 {J-nt_x\over\sqrt n}
 \Longrightarrow N\!\left(0,-{1\over\psi_x''(t_x)}\right),          \tag{4.25}
\]

with convergence of moments through order three.  In particular,

\[
 {EJ\over n}=t_x+o_c(1),\qquad
 {\operatorname{Var}(J)\over n}
 =-{1\over\psi_x''(t_x)}+o_c(1),                                    \tag{4.26}
\]

and (4.10) follows from (4.23).  Since `x->1/2` uniformly on `B_n`, (4.16)
and (4.26) prove (4.9).

The exact exponential-family identity is

\[
 \partial_z\lambda_{n,l}={2\operatorname{Var}(J)\over rz},
 \qquad \lambda_{n,l}={2EJ-r\over r}.                                \tag{4.27}
\]

The exact variance formula is

\[
 \theta_{n,l}=\lambda_{n,l}^2+
 {4(n-1)\operatorname{Var}(J)-r(n-r)(1-\lambda_{n,l}^2)
 \over nr(r-1)}.                                                      \tag{4.28}
\]

The correction in (4.28) is `O_c(1/n)`.  Its `z` derivative is `o_c(1)`:
`partial_z Var(J)` is the third centered cumulant divided by `z`, so (4.10)
makes the first differentiated numerator `O_c(n^(5/2))`, while every other
one is `O_c(n^2)`; the denominator is `Theta(n^3)`.  Hence

\[
 \partial_z\theta_{n,l}
 =2\lambda_{n,l}\partial_z\lambda_{n,l}+o_c(1).                      \tag{4.29}
\]

At the limit,

\[
 \lambda=c,\qquad
 \partial_z\lambda={(1-c)^3\over4(1+c)},                             \tag{4.30}
\]

which proves (4.11).  QED.

Using `1/(n gamma_(2,l))->1/8` on `B_n`, (1.1), (4.6), and (4.11) give

\[
 \boxed{
 \sup_{l\in\mathcal B_n}\left|
 {-\widehat\tau_l''(a_*)\over n}-{2\over1-c^2}
 \right|\to0.}                                                        \tag{4.31}
\]

## 5. A nonzero averaged pair mode forces extensive slice KL

The reviewer's scope correction is essential here: the translation-averaged
initial density has zero Johnson degree-one component.  The proof therefore
uses the **nonzero averaged degree-two adjacent-pair mode**, not degree one.

For `l<=k`, maximal-overlap subsampling gives, for distinct sites `i,j`,

\[
 P_{q_l^{\max}}(i,j\in S)
 =\alpha_{n,l}\left({1\over4}-|P_{ij}|^2\right),
 \qquad \alpha_{n,l}={l(l-1)\over k(k-1)}.                             \tag{5.1}
\]

The uniform slice has pair probability `l(l-1)/(n(n-1))`.  Since
`sum_(j!=i)|P_ij|^2=1/4`,

\[
 P_{q_l^{\max}}(i,j\in S)-P_{u_l}(i,j\in S)
 =-\alpha_{n,l}\left(|P_{ij}|^2-{1\over4(n-1)}\right).                \tag{5.2}
\]

The two laws have the same one-site marginals, so (5.2) is purely Johnson
degree two.  Under the corrected heat time it is multiplied exactly by
`theta_(n,l)`.  For adjacent cyclic sites,

\[
 b_n:=|P_{0,1}|^2-{1\over4(n-1)}
 ={1\over n^2\sin^2(\pi/n)}-{1\over4(n-1)}\to{1\over\pi^2}.          \tag{5.3}
\]

For `l>k`, pass to the minority empty set; pair entropy is invariant under
bitwise complementation.  Put `r=min(l,n-l)`, `x=r/n`,

\[
 s_{n,r}={r(r-1)\over n(n-1)},\qquad
 \delta_{n,r}=\theta_{n,r}\alpha_{n,r}b_n.                            \tag{5.4}
\]

The adjacent minority-pair marginal of `widehat q_l(a_*)` is exactly

\[
 (p_{11},p_{10},p_{01},p_{00})
 =(s-\delta,\ x-s+\delta,\ x-s+\delta,\ 1-2x+s-\delta).              \tag{5.5}
\]

Uniformly on `B_n`, Lemma 4.1 and (5.3) imply convergence to

\[
 (p_-,p_+,p_+,p_-),\qquad p_\pm={1\over4}\pm{c^2\over\pi^2}.          \tag{5.6}
\]

The Fourier input, maximal-overlap averaging, and Bernoulli--Laplace heat all
commute with cyclic shifts, so `widehat q_l` is translation invariant.
Partition the cycle into `n/2` disjoint adjacent pairs.  Entropy subadditivity
then yields

\[
 H(\widehat q_l)\le {n\over2}H_{\rm pair}(n,l).                       \tag{5.7}
\]

Therefore

\[
 K_l(\widehat\tau_l)=\log{n\choose l}-H(\widehat q_l)
 \ge\log{n\choose l}-{n\over2}H_{\rm pair}(n,l).                     \tag{5.8}
\]

Stirling's formula and (5.6) give the uniform lower bound

\[
 \boxed{
 \inf_{l\in\mathcal B_n}{K_l(\widehat\tau_l)\over n}
 \ge J_{\rm pair}(c)-o(1).}                                          \tag{5.9}
\]

This is a genuine averaged-law mode statement.  It does not use the vanished
degree-one component.

## 6. Slice modified log-Sobolev inequality with the present normalization

The inequality below is the slice modified log-Sobolev estimate in exactly the
normalization needed here.  A complete induction is included; its result agrees
with Bobkov--Tetali, Proposition 4.7.

### Lemma 6.1

For every positive density `f` on the `l`-slice,

\[
 \operatorname{Ent}_{u_l}(f)
 \le {2l(n-l)\over n+2}\,[-\langle L_lf,\log f\rangle_{u_l}].         \tag{6.1}
\]

#### Self-contained derivation

For `1<p<=2`, let `A_(n,l)(p)` be the best constant in

\[
 \|f\|_p^p-\|f\|_1^p
 \le A_{n,l}(p)\,\mathcal E_g(f,f^{p-1}),                             \tag{6.2}
\]

where

\[
 \mathcal E_g(f,g)=\sum_xu_l(x)\sum_{y\sim x}
 (f(x)-f(y))(g(x)-g(y))                                               \tag{6.3}
\]

uses ordered neighboring pairs.  The one-particle slice is the complete graph.
For it,

\[
 \mathcal E_g(f,f^{p-1})
 =2n[E f^p-(E f)(E f^{p-1})].                                        \tag{6.4}
\]

Since `s -> s^(p-1)` is concave,
`E f^(p-1)<=(E f)^(p-1)`, and hence

\[
 A_{n,1}(p)\le {1\over2n}.                                           \tag{6.5}
\]

For the induction, assume `l>=2` and write
`Omega_i={S:i in S}` with its uniform law `u_i`.  Put
`phi_i=E_(u_i)f`.  Averaging the `(n-1,l-1)` inequality over `i` uses
`n^(-1) sum_i u_i=u_l`.  Every ordered slice edge is contained in exactly
`l-1` of the `Omega_i`, which contributes
`(l-1)A_(n-1,l-1)/l` times the full edge form.

The remaining term is `n^(-1)sum_i phi_i^p-(n^(-1)sum_i phi_i)^p`.
Apply the one-particle inequality to the vector `(phi_i)`.  For `i!=j`, let
`s_ij` exchange coordinates `i,j`.  The function

\[
 R_p(a,b)=(a-b)(a^{p-1}-b^{p-1})                                    \tag{6.6}
\]

is jointly convex for `1<p<=2`.  Indeed, with `t=p-1 in (0,1]`, its diagonal
Hessian entries are

\[
 R_{aa}=t a^{t-2}[(1+t)a+(1-t)b],\qquad
 R_{bb}=t b^{t-2}[(1+t)b+(1-t)a],                                    \tag{6.7}
\]

and

\[
 {\det \nabla^2R_p\over t^2}
 =(1-t^2)a^{t-2}b^{t-2}(a-b)^2-(a^{t-1}-b^{t-1})^2\ge0.              \tag{6.8}
\]

For the last inequality set `a=ub`; after taking square roots it is

\[
 \sqrt{1-t^2}\,u^{t/2-1}|u-1|\ge |u^{t-1}-1|.                        \tag{6.9}
\]

For `0<u<=1`, set

\[
 \Psi_-(u)=\sqrt{1-t^2}\,u^{t/2-1}(1-u)-(u^{t-1}-1).
\]

It has `Psi_-(1)=0`.  After division of `Psi_-'(u)` by the positive factor
`u^(t/2-2)`, the assertion `Psi_-'(u)<=0` is equivalent to

\[
 (1-t)u^{t/2}
 \le \sqrt{1-t^2}\left(1-{t\over2}+{t\over2}u\right),               \tag{6.10}
\]

which is the weighted AM--GM bound
`u^(t/2)<=1-t/2+(t/2)u`, strengthened by
`1-t<=sqrt(1-t^2)`.  For `u>=1`, set

\[
 \Psi_+(u)=\sqrt{1-t^2}\,u^{t/2-1}(u-1)-(1-u^{t-1}).
\]

Again `Psi_+(1)=0`.  Division of its derivative by `u^(t/2-2)` reduces
`Psi_+'(u)>=0` to

\[
 \sqrt{1-t^2}\left({t\over2}u+1-{t\over2}\right)
 \ge (1-t)u^{t/2},                                                   \tag{6.11}
\]

which is the same AM--GM inequality.  The endpoint `t=1` follows by
continuity.  This proves (6.9), hence the Hessian is positive semidefinite.
Therefore

\[
 R_p(\phi_i,\phi_j)
 \le E_{u_i}R_p(f(S),f(s_{ij}S)).                                  \tag{6.12}
\]

Counting the unique ordered coordinate pair that realizes each ordered slice
edge gives

\[
 \sum_{i\ne j}R_p(\phi_i,\phi_j)
 \le {n\over l}\mathcal E_g(f,f^{p-1}).                           \tag{6.13}
\]

Combining these facts yields the recurrence

\[
 A_{n,l}(p)\le {1\over l}
 [A_{n,1}(p)+(l-1)A_{n-1,l-1}(p)].                                 \tag{6.14}
\]

Set `B_(n,l)=lA_(n,l)`.  Iterating (6.14), for `l<=n/2`,

\[
 B_{n,l}\le\sum_{j=0}^{l-1}A_{n-j,1}
 \le\sum_{j=0}^{l-1}{1\over2(n-j)}
 \le {l\over n+2}.                                                 \tag{6.15}
\]

Thus `A_(n,l)<=1/(n+2)`; complementation gives the same result for
`l>n/2`.  Divide (6.2) by `p-1` and let `p` decrease to one:

\[
 \operatorname{Ent}_{u_l}(f)\le{1\over n+2}\mathcal E_g(f,\log f).
                                                                         \tag{6.16}
\]

Finally, (1.2) gives

\[
 \mathcal E_g(f,\log f)=2l(n-l)[-\langle L_lf,\log f\rangle_{u_l}],   \tag{6.17}
\]

which is (6.1).  QED.

Applying Lemma 6.1 to the corrected density and using (5.9), uniformly on
`B_n`,

\[
 \mathcal I_l(\widehat\tau_l)
 \ge {n+2\over2l(n-l)}K_l(\widehat\tau_l)
 \ge D_{\rm pair}(c)-o(1).                                         \tag{6.18}
\]

The factor two is important: `2J_pair=D_pair`.

## 7. Actual count averaging and proof of Theorem 3.1

At `a=a_*`,

\[
 M\overset d=\operatorname{Bin}\left(k,{1+c\over2}\right)
 +\operatorname{Bin}\left(k,{1-c\over2}\right),                      \tag{7.1}
\]

so `EM=n/2`.  Hoeffding's inequality gives

\[
 P(M\notin\mathcal B_n)\le2e^{-2n^{1/3}}.                             \tag{7.2}
\]

Every summand in (2.18) is nonnegative by (2.3) and (4.6).  On the
layers `l=0,1,n-1,n`, translation invariance makes the averaged maximal-overlap
law uniform (or the slice is a singleton), so `K_l=I_l=0`; the endpoint clock
convention is therefore immaterial.  Hence tails may be dropped rather than
bounded in absolute value.  Combining (4.31), (6.18), and
`P(M in B_n)->1`, for every `epsilon>0` and all large even `n`,

\[
 {\mathcal C_n(c)\over n}
 \ge P(M\in\mathcal B_n)
 \left({2\over1-c^2}-\epsilon\right)
 (D_{\rm pair}(c)-\epsilon).                                         \tag{7.3}
\]

Letting `n->infinity` and then `epsilon->0` proves (3.4).

## 8. What is and is not paid

### Paid in this round

1. The complete chain rule (2.10), including `pi D''`, `2pi'D'`, and
   `pi''D`, is explicit.
2. At the midpoint, all first-clock/cross terms vanish for the proved reason
   `z'=0`, not by omission.
3. `partial_z theta>0` is proved exactly, so the clock-curvature sign is exact.
4. The central clock response has the explicit asymptotic
   `-tau_l''/n -> 2/(1-c^2)`.
5. A second, nonzero **averaged** mode is exhibited: the adjacent degree-two
   pair mode.  It gives an extensive KL lower bound.
6. The slice modified log-Sobolev constant is derived with the exact generator
   normalization used here.
7. Actual count tails are paid, and the final coefficient is explicit.

### Still unpaid

1. The moving-count term `W_n=sum pi_l'' K_l` in (2.17) has no proved sign or
   sharp scale.  It can in principle offset the favorable component.  There is
   an exact product-derivative representation that fixes the next obligation.
   Freeze the layer array
   `h(l)=K_l(widehat tau_l(a_*))`.  If `B_i(a)` are the `n` independent
   Bernoulli count bits, each has `d p_i/da=1`.  With
   `N_(ij)=sum_(r notin {i,j}) B_r(a_*)` and
   `Delta^2h(m)=h(m+2)-2h(m+1)+h(m)`, two differentiations give

   \[
    \boxed{\mathcal W_n(c)=
    2\sum_{1\le i<j\le n}E\,\Delta^2h(N_{ij}).}                       \tag{8.1}
   \]

   Thus a proof must control the complete compatibility average of layer second
   differences; a center-layer sign alone is insufficient.
2. The time-Hessian term away from the midpoint, involving
   `(tau_l')^2 I_l'`, is unpaid.
3. No sign is asserted for the full corrected divergence response,
   `widehat H''`, the actual cyclic entropy, or the Toeplitz sine target.
4. The prior round-2 saddle, cusp/local-limit, and entropy-comparison claims
   remain author claims except for the separately reported bounded algebraic
   gate.  Lemma 4.1 here is a new specialized central-overlap proof sufficient
   only for Theorem 3.1.
5. The numerical finite-size cusp observed in `attempts.md` is deliberately
   retained as an unproved candidate and is not used in the theorem.

## 9. Scope repair for the old random-clock no-go

The translation-invariant averaged density `r_l^max` has zero Johnson
degree-one component.  Therefore the previous two-moment Jensen obstruction is
informative only when degree-one **channel/operator multiplier matching is
separately imposed**, for example before averaging over the input `A`.  It does
not rule out matching the averaged law.  This round makes no averaged-law
no-go claim.  Its averaged-law lower bound instead uses the explicitly nonzero
adjacent degree-two mode in Section 5.
