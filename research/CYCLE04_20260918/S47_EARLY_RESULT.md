# Cycle04 early harvest — S47

AUTHOR_CLAIMS_PENDING_SEPARATE_SOL_REVIEW. Complete visible response acquired; attachment bodies not acquired. S45 reports an artifact-write failure. S47 explicitly leaves the requested vanishing tail unproved. Original citation tokens preserved, not independently resolved evidence.

---

## S47 cycle-04 — result

**Status: INCOMPLETE for the requested true-sine chord-sensitive tail. PROVED for a new exact signed finite-chord response calculus that isolates the remaining all-scale obligation.**

I read the frozen target and the cycle-04 prompt. The target remains concavity of the **full-configuration Shannon entropy rate** \(h_\rho(a,c)\) for every fixed \(0<\rho,c<1\) over the entire legal interval \(0\le a\le1-c\); no differentiability of the rate is assumed. citeturn1view0 The cycle-04 assignment specifically asks for an \(\eta^2\)-sensitive replacement for S42's unsigned \(O(\log L/L)\) tail and correctly warns that differentiating its quantum upper bound is invalid. citeturn0view0

I found an exact parameter-translation mechanism which seems useful beyond this cycle. It **does pay the quadratic chord factor exactly**, but I have not completed the decisive true-sine estimate showing that its adverse boundary curvature is \(o(L)\) (ideally \(O(\log L)\)). Therefore I do not claim the benchmark chord or the ultimate theorem.

### 1. Signed nilpotent translation of the actual law

For the latent sine process \(X\), the true output channel is

\[
W_a(x,1)=a+cx,\qquad
W_a(x,0)=1-a-cx .
\]

Introduce

\[
T_t=
\begin{pmatrix}
1-t&t\\
-t&1+t
\end{pmatrix}
=I+tD,
\qquad
D=
\begin{pmatrix}
-1&1\\
-1&1
\end{pmatrix}.
\]

Two elementary identities are crucial:

\[
D^2=0,
\qquad
\boxed{W_aT_t=W_{a+t}}.
\]

The second is an exact matrix identity, with **no approximation and no assumption on the latent law**.

Therefore, if \(p_a^{(n)}\) denotes the complete \(n\)-word distribution of the output,

\[
\boxed{
p_{a+t}^{(n)}
=
p_a^{(n)}T_t^{\otimes n}.
}
\tag{1}
\]

Writing \(D_i\) for \(D\) acting on coordinate \(i\),

\[
G_n=\sum_{i=1}^nD_i.
\]

The \(D_i\)'s commute and square to zero, so

\[
T_t^{\otimes n}
=
\prod_i(I+tD_i)
=
\exp(tG_n).
\]

Consequently,

\[
\boxed{
\partial_a^r p_a^{(n)}
=
p_a^{(n)}G_n^r
}
\tag{2}
\]

whenever the derivatives are evaluated in the legal interior.

This is a **signed translation semigroup**, not a Markov semigroup: \(T_t\) has the negative entry \(-t\) when \(t>0\). Thus ordinary data processing cannot simply be applied to it.

This also exposes exactly why the parameter response is subtler than adding ordinary noise.

### 2. It preserves the complete moving-law entropy Hessian

Let \(p=p_a^{(n)}\). From (2),

\[
p'=pG_n,\qquad p''=pG_n^2.
\]

Differentiating the actual full Shannon entropy gives

\[
\boxed{
H_n''(a)
=
-\sum_y(pG_n^2)(y)\log p(y)
-\sum_y\frac{(pG_n)(y)^2}{p(y)}.
}
\tag{3}
\]

Thus the probability-acceleration term survives exactly. This agrees with the frozen target's warning that the Fisher term alone is not the entropy Hessian. citeturn1view0

### 3. Signed boundary-information curvature

Take adjacent \(L\)-blocks \(A,B\), and set

\[
P=P_a^{AB},\qquad
Q=P_a^A\otimes P_a^B,
\qquad
J_L(a)=D(P\|Q).
\]

Marginalization commutes with (1). Hence **both** \(P\) and \(Q\) evolve under

\[
G=G_A+G_B:
\qquad
P'=PG,\quad P''=PG^2,\quad
Q'=QG,\quad Q''=QG^2.
\]

Define

\[
s_P=P'/P,\quad u_P=P''/P,
\qquad
s_Q=Q'/Q,\quad u_Q=Q''/Q .
\]

Direct differentiation of relative entropy gives

\[
\boxed{
B_L(a):=J_L''(a)
=
\mathbb E_P\!\left[
u_P\log\frac PQ
+(s_P-s_Q)^2
-(u_Q-s_Q^2)
\right].
}
\tag{4}
\]

Equivalently,

\[
\begin{aligned}
B_L
={}&
\sum P''\log(P/Q)
+\sum\frac{(P')^2}{P}
-2\sum\frac{P'Q'}Q\\
&-\sum\frac{PQ''}{Q}
+\sum P\frac{(Q')^2}{Q}.
\end{aligned}
\tag{5}
\]

I call \(B_L\) the **signed boundary-information curvature**.

Unlike a quantum MI majorant, (4) is an identity for the actual measured sine-word distribution. Every moving-law score and acceleration term is retained.

### 4. The missing \(\eta^2\) factor is now exact

For every chord contained in a strict-interior interval,

\[
\boxed{
\Delta_\eta J_L(a)
=
\int_{-\eta}^{\eta}
(\eta-|t|)\,
B_L(a+t)\,dt.
}
\tag{6}
\]

Hence any uniform finite-volume estimate

\[
B_L(u)\ge-E_L
\]

on the chord immediately gives

\[
\boxed{
\Delta_\eta J_L(a)\ge-\eta^2E_L.
}
\tag{7}
\]

There is no limiting differentiation here. Equation (6) is a finite-volume identity first, and only afterwards can it be inserted into the entropy-rate telescope.

This is precisely the quadratic factor absent from S42's unsigned value tail. S42's existing construction instead controls \(J_L\) itself through the sine projection's boundary number variance \(V_\rho(L)=O(\log L)\). citeturn1view1

### 5. Exact all-scale tail criterion

S42 established the dyadic finite-chord identity

\[
\Delta_\eta h(a)
=
\frac{\Delta_\eta H_m(a)}m
-
\sum_{j\ge0}
\frac{\Delta_\eta J_{m2^j}(a)}
     {2m2^j}.
\] citeturn1view1


Start the discarded ladder at \(L\). Define

\[
\boxed{
E_{\rm tail}(L)
=
\sum_{j=0}^{\infty}
\frac{
\sup_{u\in[a-\eta,a+\eta]}
[-B_{2^jL}(u)]_+
}{
2^{j+1}L
}.
}
\tag{8}
\]

Equations (6)–(8) give the rigorous finite-chord inequality

\[
\boxed{
\sum_{j=0}^{\infty}
\frac{\Delta_\eta J_{2^jL}(a)}
     {2^{j+1}L}
\ge
-\eta^2E_{\rm tail}(L).
}
\tag{9}
\]

Thus the cycle-04 target would follow on a strict-interior compact interval from

\[
\boxed{E_{\rm tail}(L)\longrightarrow0.}
\tag{10}
\]

For example, the actual-sine curvature estimate

\[
[-B_L(a)]_+\le C_{\rho,c,I}\log L
\tag{11}
\]

would yield immediately

\[
E_{\rm tail}(L)
=
O_{\rho,c,I}\!\left(\frac{\log L}{L}\right),
\]

and therefore

\[
\boxed{
\text{discarded signed tail}
\ge
-\eta^2
O_{\rho,c,I}\!\left(\frac{\log L}{L}\right).
}
\tag{12}
\]

That would be stronger in the small-chord direction than the unsigned S42 remainder.

### 6. What can already be controlled uniformly

Suppose the parameter interval is strictly interior:

\[
\varepsilon\le a,\qquad a+c\le1-\varepsilon .
\]

Conditioned on the latent sine configuration, every output bit has success probability in \([\varepsilon,1-\varepsilon]\). Conditioning additionally on every other output bit merely changes the posterior mixture over the latent bit. Therefore

\[
\boxed{
\varepsilon
\le
P_a(Y_i=1\mid Y_{-i})
\le
1-\varepsilon .
}
\tag{13}
\]

In particular neighboring atom ratios obey the dimension-free bound

\[
\frac{\varepsilon}{1-\varepsilon}
\le
\frac{p(y^{(i)})}{p(y)}
\le
\frac{1-\varepsilon}{\varepsilon}.
\tag{14}
\]

This controls each **local** signed score in (4).

It is nevertheless insufficient to finish (10): summing such estimates naively costs volume, and the mixed \(D_iD_j\) acceleration can cost still more. The missing argument must exploit the determinantal cross-boundary cancellation of the sine process rather than only strict positivity.

### 7. Why the quantum majorant still cannot be differentiated

S42 proves a value inequality of the form

\[
J_L(a)\le J_L^{\rm q}(a)
\le C(a,c)V_\rho(L),
\]

where for the sine projection \(V_\rho(L)=O(\log L)\). citeturn1view1

But this gives no implication

\[
J_L''\le (J_L^{\rm q})''
\quad\text{or}\quad
J_L''\ge (J_L^{\rm q})''.
\]

Indeed, the exact shift \(T_t\) above is signed rather than stochastic. So neither ordinary data processing nor differentiation of the pointwise quantum domination supplies (11).

A potentially useful next object is therefore the **measurement curvature defect**

\[
\mathcal D_L(a)
=
I_{\rm quantum}(A:B)-J_L(a).
\]

Its value is nonnegative, but what is actually required is control of its *curvature*. Nonnegativity alone gives no such result.

### 8. Precise unpaid theorem

The remaining all-scale mathematical obligation is now narrower:

> **Boundary-curvature theorem sought.**  
> For every fixed \(0<\rho,c<1\) and strict-interior compact \(I\subset(0,1-c)\), prove
> \[
> J_L''(a)\ge-e_{\rho,c,I}(L)
> \]
> uniformly for \(a\in I\), where
> \[
> \sum_{j\ge0}
> \frac{e_{\rho,c,I}(2^jL)}{2^{j+1}L}
> \to0.
> \]
> The desirable sine-scale estimate is \(e(L)=O(\log L)\).

That theorem plus (9) is exactly the requested chord-sensitive bridge.

Endpoints remain separate: the algebraic translation (1) still holds, but atoms can vanish and Hessians can diverge. Endpoint completion therefore needs a genuinely finite-chord/one-sided integrable estimate rather than silently extending the strict-interior Hessian argument.

### Conclusion

**PROVED:** the actual sine output family admits an exact signed nilpotent translation \(p_{a+t}=p_aT_t^{\otimes n}\); this yields the complete moving-law boundary-information curvature (4) and the exact quadratic-chord tail inequality (9).

**INCOMPLETE:** I have **not** proved \(E_{\rm tail}(L)\to0\) for the true sine process. In particular, I have not converted S42's \(O(\log L)\) *value* bound into an \(O(\log L)\) adverse-curvature bound. The benchmark entropy-rate chord and the full \(0<c<1\) concavity theorem therefore remain open. This avoids the erroneous step of differentiating S42's quantum majorization.

Files:

:chatgpt-content-reference{index="7"}  
:chatgpt-content-reference{index="8"}  
:chatgpt-content-reference{index="9"}
