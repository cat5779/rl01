# Cycle04 early harvest — S45

AUTHOR_CLAIMS_PENDING_SEPARATE_SOL_REVIEW. Complete visible response acquired; attachment bodies not acquired. S45 reports an artifact-write failure. S47 explicitly leaves the requested vanishing tail unproved. Original citation tokens preserved, not independently resolved evidence.

---

# S45 Cycle 04 — corrected-law clock response

**Status: PROVED — CORRECTED_LAW_ONLY.**

I obtained a sharper clock entropy-production tool. It does not yet decide \(W_n+C_n\), but it improves the rigorous upper coefficient for \(C_n/n\) from about \(8.43\times10^5\) to about \(4.996\times10^2\), while preserving the exact prescribed clock, actual \(\pi_l\)-weights, endpoints, and complementary tails.

The frozen identity is
\[
\widehat K_n''(a_*)=W_n+C_n,\qquad
C_n=\sum_l\pi_l(a_*)[-s_l''(a_*)]\,I_l^G(s_l),
\]
with
\[
s_l=-\frac{\log\theta_{n,l}(z_*)}{2(n-1)}.
\]
These normalizations and the midpoint disappearance of the first-clock terms are part of the frozen model. citeturn2view0turn4view1

## 1. New tool: pay the clock with entropy actually dissipated

Let a finite reversible Markov semigroup have
\[
F(s)=D(uP_sf\Vert u),\qquad I(s)=-F'(s).
\]
For the symmetric-exclusion semigroup here, \(I(s)\) is nonincreasing; the existing proof follows from joint convexity of
\[
\Psi(x,y)=(x-y)(\log x-\log y)
\]
and commutation of the heat semigroup with coordinate transpositions. citeturn3view0

Consequently,
\[
sI(s)
\le\int_0^sI(t)\,dt
=F(0)-F(s).                                      \tag{1}
\]

The previous \(C_n=O(n)\) argument discarded \(F(s)\) and used only
\[
sI(s)\le F(0).                                    \tag{2}
\]
Indeed that loss is explicit in the reviewed proof. citeturn5view1

Now suppose
\[
s(z)=-\frac{\log\theta(z)}{\Lambda}.
\]
At the symmetric point \(z'(a_*)=0\),
\[
-s''(a_*)
=\frac{z''(a_*)}{\Lambda}\partial_z\log\theta(z_*).
\]
Since
\[
s_*=\frac{-\log\theta(z_*)}{\Lambda},
\]
multiplying (1) by \((-s'')/s\) gives the sharper **entropy-drop clock inequality**
\[
\boxed{
[-s''(a_*)]I(s_*)
\le
z''(a_*)
\frac{\partial_z\log\theta(z_*)}{-\log\theta(z_*)}
\,[F(0)-F(s_*)].
}                                                   \tag{3}
\]

This is a genuine terminal-clock estimate rather than a renamed remainder: it replaces the complete initial entropy budget by precisely the entropy dissipated over the prescribed interval.

There is also an exact differential interpretation:
\[
\partial_zF(s(z))
=
\frac{\partial_z\log\theta(z)}{\Lambda}I(s(z)),
\]
so the left side of (3) is exactly \(z''(a_*)\partial_zF(s(z_*))\).

## 2. Exact actual-model aggregation

Apply (3) to every layer with
\[
G_l=l(n-l)L_l,\qquad
\Lambda=2(n-1),
\]
and write
\[
R_{n,l}(z)=
\frac{\partial_z\log\theta_{n,l}(z)}
{-\log\theta_{n,l}(z)}.
\]

Then the actual corrected-law acceleration satisfies

\[
\boxed{
C_n
\le
z''(a_*)\sum_l\pi_l(a_*)R_{n,l}(z_*)
\bigl[F_l(0)-F_l(s_l)\bigr].
}                                                   \tag{4}
\]

No \(l(n-l)\) factor has been lost: its cancellation is exactly the conversion between \(L_l\)-time and \(G_l\)-time. citeturn2view3

The prescribed endpoint layers have zero entropy production, so (4) includes them without assigning fictitious clocks.

## 3. Central clock coefficient

Take
\[
\mathcal B_n=\{|l-n/2|\le n^{2/3}\}.
\]
The established central coefficient asymptotics are uniform:
\[
\theta_{n,l}(z_*)\longrightarrow c^2,
\]
and
\[
\partial_z\log\theta_{n,l}(z_*)
\longrightarrow
\frac{(1-c)^3}{2c(1+c)}.                            \tag{5}
\]
Also
\[
z''(a_*)=\frac{32c}{(1-c)^4}.                       \tag{6}
\]
These statements were proved by the overlap saddle calculation rather than by replacing the prescribed clock with a limiting half-step. citeturn6view0

Therefore
\[
z''R_{n,l}
\longrightarrow
A_c:=
\boxed{
\frac{8}{(1-c^2)(-\log c)}
}                                                    \tag{7}
\]
uniformly throughout \(\mathcal B_n\).

## 4. A strictly smaller entropy budget

Let \(m=\min(l,n-l)\). The existing all-layer bound is
\[
F_l(0)\le m\log2.                                   \tag{8}
\]
It follows directly from the projection-DPP maximal-overlap law and Hadamard's determinant inequality. citeturn3view0

Hence centrally,
\[
F_l(0)\le\frac n2\log2+o(n).                        \tag{9}
\]

But unlike the old clock proof, we retain the terminal entropy. The adjacent-pair mode theorem gives uniformly on \(\mathcal B_n\)
\[
F_l(s_l)
\ge nJ_{\rm pair}(c)-o(n),                          \tag{10}
\]
where
\[
J_{\rm pair}(c)
=\log2+p_-\log p_-+p_+\log p_+,
\qquad
p_\pm=\frac14\pm\frac{c^2}{\pi^2}.
\]
The proof uses actual adjacent spatial pairs and entropy subadditivity, not a radial count surrogate. citeturn6view0

Thus
\[
\boxed{
F_l(0)-F_l(s_l)
\le
n\left(\frac{\log2}{2}-J_{\rm pair}(c)\right)+o(n).
}                                                    \tag{11}
\]

This is the quantitative gain.

## 5. Actual \(\pi_l\) weights and complementary tails

At \(a_*\),
\[
M\overset d=
\operatorname{Bin}\!\left(k,\frac{1+c}{2}\right)
+
\operatorname{Bin}\!\left(k,\frac{1-c}{2}\right),
\]
so \(EM=n/2\), and
\[
P(M\notin\mathcal B_n)
\le2e^{-2n^{1/3}}.                                  \tag{12}
\]
This is the actual count law, not an auxiliary Gaussian replacement. citeturn4view0

On the complementary tail, use the already-proved uniform quotient bound
\[
0\le R_{n,l}(z_*)
\le
\frac{2}{(z_*-1)\beta(z_*)},
\]
together with
\[
0\le F_l(0)-F_l(s_l)\le F_l(0)\le\frac n2\log2.
\]
The tail in (4), divided by \(n\), is therefore exponentially small. The uniform quotient estimate itself is all-layer. citeturn3view1

Combining (4), (7), (11), and (12) proves the new theorem:

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\ {\rm even}}}
\frac{C_n(c)}n
\le
\frac{8}{(1-c^2)(-\log c)}
\left[
\frac{\log2}{2}-J_{\rm pair}(c)
\right].
}                                                    \tag{13}
\]

This holds for every fixed \(0<c<1\) in the frozen half-density corrected-law model.

## 6. Numerical coefficient at \(c=19/20\)

Here
\[
D_{\rm pair}
=0.06847130817780112\ldots,
\qquad
J_{\rm pair}
=0.03423565408890056\ldots,
\]
the established values from the S13 mode theorem. citeturn4view1

Furthermore,
\[
A_{19/20}
=
\frac8{(1-(19/20)^2)(-\log(19/20))}
=
1599.64929199784\ldots .
\]

Hence
\[
\boxed{
\limsup_{n\to\infty}\frac{C_n}{n}
\le
499.631158492115\ldots .
}                                                    \tag{14}
\]

The independently established lower result remains
\[
\boxed{
\liminf_{n\to\infty}\frac{C_n}{n}
\ge1.4045396549292533\ldots .
}                                                    \tag{15}
\] citeturn4view1

So the current unconditional rigorous window is
\[
1.40454\ldots
\le\liminf C_n/n
\le\limsup C_n/n
\le499.63116\ldots .
\]

The old all-layer upper coefficient was
\[
843421.3677805\ldots,
\]
so (14) reduces that coefficient by roughly three orders of magnitude. citeturn2view3

## 7. What this says about \(W_n+C_n\)

S43's new claim
\[
\limsup W_n/n\le-2.689614884862
\]
is explicitly marked pending review in the Cycle-04 assignment, so I do not use it as a theorem. citeturn0view0

**Conditionally** on that claim, (14) yields only
\[
\limsup\frac{W_n+C_n}{n}
\le
496.941543607253\ldots ,
\]
which does not determine the sign.

This identifies the remaining bottleneck more precisely. Merely controlling **total entropy dissipated during the clock interval** cannot presently compare the two terms: one needs information local to the terminal clock—effectively a sharp bound/asymptotic for
\[
\frac{I_l^G(s_l)}{n^2}
\]
or a compensated identity pairing that terminal production directly with the \(B_m\)-weighted layer curvature.

That diagnosis agrees with the earlier S13 observation that the sharp coefficient bottleneck is terminal entropy production rather than tails or normalization. citeturn5view0

## Scope ledger

**PROVED:** the entropy-drop clock corrector (3); the exact actual-layer inequality (4); all central/tail bookkeeping; and the explicit limiting envelope (13), including (14) at \(c=19/20\).

**INCOMPLETE:** a coefficient sharp enough to determine \(W_n+C_n\); existence of \(\lim C_n/n\); S43's pending signed \(W_n\) result; and any passage from the corrected cyclic law to the true sine-Toeplitz DPP.

The ultimate target remains the full-configuration Shannon entropy rate of
\[
K_n(a)=aI+cQ_n
\]
for **every fixed \(0<\rho<1\), every \(0<c<1\), and every legal \(0\le a\le1-c\)**. The frozen corrected-law midpoint result above does not narrow that target. citeturn1view0

I attempted to create `S45_RESULT.md`, `S45_checks.py`, and `S45_result.zip`, but the artifact runtime rejected writes to the existing S45 paths with a permissions error. The complete result and proof are therefore preserved above; the file-delivery failure does not affect the mathematical status.
