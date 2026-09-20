# Source status: tool-visible prefix, truncated at 20000 characters; not a complete manuscript.

# S77 RESULT — Fisher-compensated Toeplitz cut estimate

## Verdict

**PROVED**

1. An exact affine-KL/Bochner identity that combines \(D_F\) and \(C_{\mathrm{acc}}\) *before* any absolute-value estimate.
2. An exact decomposition
   \[
   M''=\mathcal I_{\mathrm{rel}}-\mathcal B,
   \qquad
   \mathcal I_{\mathrm{rel}}
   =E_p\!\left[(\partial_a\ell)^2\right],
   \]
   where \(\mathcal B\) is a signed sum of local Itakura–Saito/Burg rectangle defects formed from the actual likelihood ratios \(p/(p_Ap_B)\).
3. A non-equivalent, directly checkable cut certificate
   \[
   M''\ge \mathcal I_{\mathrm{rel}}-\mathcal B_+,
   \]
   which discards only favorable negative Burg rectangles and retains the relative Fisher term.
4. A hybrid merge-tree theorem that uses this new residual at verified scales and the audited S74 estimate only on the remaining tail.
5. A rigorous obstruction to any uniform estimate
   \[
   -C_{\mathrm{acc}}\le \theta D_F+o(\|K_{AB}\|_{\mathrm{HS}}^2),
   \qquad \theta<1,
   \]
   even for strict two-site contractions.
6. A quantitative two-site replacement:
   \[
   M''\ge
   \frac{3-10u(1-u)}{u^4(1-u)^4}\,d^2>0,
   \]
   for every strict equal-marginal two-site DPP.

**DISPROVED**

A fixed \(\theta<1\) cannot absorb a uniform fraction of the acceleration while leaving only a quartic-in-\(K_{AB}\) residual. The two-site weak-cut limit forces \(-C_{\mathrm{acc}}/D_F\to1\).

**INCOMPLETE**

The global theorem that \(h(a)\) is concave for all \(\rho,c,a\) is not closed. The exact remaining payment is an all-scale Toeplitz estimate for the bad Burg charge introduced below. The new certificate passes the audited six-site point and all finite non-extreme-density tests executed here, but those diagnostics are not an all-size proof.

The accepted starting point is the S71 decomposition \(M''=D_F+C_{\mathrm{acc}}\), with \(D_F\ge0\), together with the S74 bound and exact adjacent merge-tree accounting. citeturn167681view1turn167681view2

---

# 1. The Fisher–Burg cut tool

## Input and hypotheses

Let \(V=A\sqcup B\) be finite and let

\[
K(a)=K_0+aI
\]

be a Hermitian strict contraction throughout a compact interval \(J\), with

\[
\delta I\preceq K(a)\preceq(1-\delta)I,
\qquad a\in J.
\]

Let

\[
p_a(y)=P_{K(a)}(y),
\qquad
q_a(y)=p_{A,a}(y_A)p_{B,a}(y_B).
\]

Thus \(q_a\) is exactly the DPP with block-diagonal kernel
\(K_A(a)\oplus K_B(a)\). It is not an independently chosen approximation.

All \(2^{|V|}\) words have positive mass. For \(I\subseteq V\), write
\(p_{-I}\) and \(q_{-I}\) for the actual deleted-coordinate marginals. Put

\[
\sigma_i=2y_i-1,
\qquad
g(y)=\frac{p(y)}{q(y)},
\qquad
g_{-ij}(y_{-ij})
=\frac{p_{-ij}(y_{-ij})}{q_{-ij}(y_{-ij})}.
\]

Define the scalar nonnegative divergence

\[
\Phi(x,m)
=
2\left[x-m-m\log\frac{x}{m}\right]
=
2m\left[\frac{x}{m}-1-\log\frac{x}{m}\right].
\]

For a function of the two coordinates \(y_i,y_j\), define

\[
\Delta_{ij}f
=
f_{11}+f_{00}-f_{10}-f_{01}.
\]

Finally define

\[
\mathcal I_{\mathrm{rel}}
=
E_p\!\left[(\partial_a\log g)^2\right],
\]

\[
\mathcal B
=
\sum_{i<j}\sum_{y_{-ij}}
q_{-ij}(y_{-ij})
\,
\Delta_{ij}
\Phi\!\left(g(y),g_{-ij}(y_{-ij})\right),
\]

and the bad, unsigned part

\[
\mathcal B_+
=
\sum_{i<j}\sum_{y_{-ij}}
q_{-ij}(y_{-ij})
\left[
\Delta_{ij}
\Phi\!\left(g(y),g_{-ij}(y_{-ij})\right)
\right]_+.
\]

This requires exactly

\[
\binom{|V|}{2}2^{|V|-2}
\]

conditional rectangles. No configurations are discarded.

---

## PROVED THEOREM 1 — exact Fisher–Burg compensation

For every \(a\in J\),

\[
\boxed{
M''(a)
=
\mathcal I_{\mathrm{rel}}(a)-\mathcal B(a).
}
\tag{1}
\]

Moreover, if

\[
S=\partial_a\log p,
\qquad
S_A=\partial_a\log p_A,
\qquad
S_B=\partial_a\log p_B,
\]

then

\[
\boxed{
D_F
=
\mathcal I_{\mathrm{rel}}
-
2E_p[S_AS_B],
}
\tag{2}
\]

and

\[
\boxed{
C_{\mathrm{acc}}
=
2E_p[S_AS_B]-\mathcal B.
}
\tag{3}
\]

The accepted DPP score monotonicity and negative association give

\[
E_p[S_AS_B]\le0,
\qquad
D_F\ge \mathcal I_{\mathrm{rel}}\ge0.
\tag{4}
\]

Thus the excess part

\[
-2E_p[S_AS_B]
\]

of the accepted Fisher defect cancels exactly against the corresponding piece of \(C_{\mathrm{acc}}\). After this cancellation, the true competition is not \(D_F\) versus the whole acceleration, but

\[
\boxed{
\text{relative Fisher }\mathcal I_{\mathrm{rel}}
\quad\text{versus}\quad
\text{signed Burg charge }\mathcal B.
}
\]

This is the requested Fisher-retaining payment.

---

## PROVED COROLLARY 2 — bad-rectangle cut inequality

Since \(\mathcal B\le\mathcal B_+\),

\[
\boxed{
M''\ge \mathcal I_{\mathrm{rel}}-\mathcal B_+.
}
\tag{5}
\]

Consequently, with

\[
\varepsilon_{\mathrm{FB}}(A,B;a)
=
\left[
\mathcal B_+(A,B;a)-\mathcal I_{\mathrm{rel}}(A,B;a)
\right]_+,
\tag{6}
\]

one has

\[
\boxed{
M''_{A,B}(a)\ge-\varepsilon_{\mathrm{FB}}(A,B;a).
}
\tag{7}
\]

This is **strictly weaker** than \(M''\ge0\), because it allows a positive residual.

By contrast,

\[
\mathcal B\le\mathcal I_{\mathrm{rel}}
\]

is exactly equivalent to \(M''\ge0\) and is therefore an **EQUIVALENT_BLOCKER**, not a solved weaker result.

The checkable condition

\[
\boxed{
\mathcal B_+\le\mathcal I_{\mathrm{rel}}
}
\tag{8}
\]

is a strictly stronger sufficient condition for \(M''\ge0\), because it refuses to use cancellation among Burg rectangles.

Combining (7) with the audited S74 estimate gives the never-worse hybrid residual

\[
\widehat\varepsilon(A,B;a)
=
\min\!\left\{
\varepsilon_{\mathrm{FB}}(A,B;a),
\,
B_\delta\|K_{AB}\|_{\mathrm{HS}}^2
\right\},
\tag{9}
\]

and therefore

\[
\boxed{
M''_{A,B}(a)\ge-\widehat\varepsilon(A,B;a).
}
\tag{10}
\]

At a cut where (8) holds, the new cost is zero even when the S74 constant is enormous.

---

# 2. Proof of the exact identity

Dots denote derivatives with respect to the common scalar shift \(a\).

## 2.1 Cofactor equations

For every configuration,

\[
\boxed{
\dot p(y)=\sum_i\sigma_i p_{-i}(y_{-i}),
}
\tag{11}
\]

\[
\boxed{
\ddot p(y)
=
2\sum_{i<j}\sigma_i\sigma_j
p_{-ij}(y_{-ij}).
}
\tag{12}
\]

These follow by differentiating

\[
p(y)
=
(-1)^{|\{i:y_i=0\}|}
\det\!\left(K-\operatorname{diag}(1-y)\right)
\]

and identifying the principal cofactors with deleted-coordinate DPP probabilities.

The same equations hold for \(q\), either directly from its block-diagonal DPP kernel or by differentiating \(p_Ap_B\).

Put

\[
r=p-q.
\]

For \(0\le s\le1\), introduce the exact affine bridge

\[
h_s=q+sr,
\qquad
z_s=\frac{r}{h_s}.
\tag{13}
\]

The bridge is an auxiliary probability law. It is generally **not** a DPP, and no DPP negative-association assertion will be applied to it. Equations (11)–(12) nevertheless hold for \(h_s\) and \(r\) by linearity.

---

## 2.2 KL as an integrated \(\chi^2\) divergence

Let

\[
D_s=D(h_s\|q).
\]

Differentiation in \(s\) gives

\[
D_s''
=
\sum_y\frac{r(y)^2}{h_s(y)}
=:J_s.
\tag{14}
\]

Since \(D_0=D_0'=0\),

\[
\boxed{
M=D(p\|q)
=
\int_0^1(1-s)J_s\,ds.
}
\tag{15}
\]

This is exact because \(D(p\|p_Ap_B)\) is the block mutual information.

---

## 2.3 A discrete Bochner identity

For scalar functions \(r(a),h(a)\), with \(z=r/h\),

\[
\left(\frac{r^2}{h}\right)''
=
2h(\dot z)^2+2z\ddot r-z^2\ddot h.
\tag{16}
\]

The cofactor integration-by-parts identity is

\[
\sum_y f(y)\ddot r(y)
=
2\sum_{i<j}\sum_{y_{-ij}}
r_{-ij}(y_{-ij})\Delta_{ij}f.
\tag{17}
\]

Similarly for \(h_s\). Furthermore,

\[
z_{s,-ij}
:=
\frac{r_{-ij}}{h_{s,-ij}}
=
E_{h_s}[z_s\mid Y_{-ij}].
\tag{18}
\]

Using

\[
\Delta_{ij}(z-z_{-ij})^2
=
\Delta_{ij}z^2-2z_{-ij}\Delta_{ij}z
\]

in (16)–(17) yields

\[
\boxed{
J_s''
=
2E_{h_s}\!\left[(\dot z_s)^2\right]
-
2\sum_{i<j}
E_{h_{s,-ij}}
\!\left[
\Delta_{ij}(z_s-z_{s,-ij})^2
\right].
}
\tag{19}
\]

No sign has been assigned to the rectangle term.

Integrating (19) against \(1-s\) gives

\[
M''
=
\mathcal I_*-\mathcal R_*,
\tag{20}
\]

where

\[
\mathcal I_*
=
2\int_0^1(1-s)
E_{h_s}[(\dot z_s)^2]\,ds,
\tag{21}
\]

and

\[
\mathcal R_*
=
2\int_0^1(1-s)
\sum_{i<j}
E_{h_{s,-ij}}
[
\Delta_{ij}(z_s-z_{s,-ij})^2
]\,ds.
\tag{22}
\]

---

## 2.4 Exact evaluation of the positive term

Write

\[
g=\frac pq,
\qquad
\ell=\log g,
\qquad
d_s(x)=1+s(x-1).
\]

Then

\[
h_s=q\,d_s(g),
\qquad
z_s=\frac{g-1}{d_s(g)},
\qquad
\dot z_s=\frac{\dot g}{d_s(g)^2}
=\frac{g\dot\ell}{d_s(g)^2}.
\]

The elementary integral

\[
2\int_0^1\frac{1-s}{d_s(g)^3}\,ds
=
\frac1g
\tag{23}
\]

therefore gives

\[
\begin{aligned}
\mathcal I_*
&=
\sum_y q(y)g(y)^2\dot\ell(y)^2
\,
2\int_0^1
\frac{1-s}{d_s(g(y))^3}\,ds\\
&=
\sum_y p(y)\dot\ell(y)^2.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal I_*=\mathcal I_{\mathrm{rel}}
=
E_p[(\partial_a\ell)^2].
}
\tag{24}
\]

---

## 2.5 Exact evaluation of the rectangle term

For fixed \(i,j,y_{-ij}\), put

\[
m=g_{-ij}(y_{-ij})
=\frac{p_{-ij}}{q_{-ij}}.
\]

Then

\[
h_{s,-ij}=q_{-ij}d_s(m),
\qquad
z_{s,-ij}=\frac{m-1}{d_s(m)}
\]

and

\[
z_s(g)-z_s(m)
=
\frac{g-m}{d_s(g)d_s(m)}.
\tag{25}
\]

The scalar integral needed in (22) is

\[
\begin{aligned}
&2(g-m)^2
\int_0^1
\frac{1-s}
{d_s(g)^2d_s(m)}
\,ds\\
&\hspace{15mm}
=
2\left[g-m-m\log\frac gm\right]
=
\Phi(g,m).
\end{aligned}
\tag{26}
\]

Substitution into (22) proves

\[
\boxed{
\mathcal R_*=\mathcal B.
}
\tag{27}
\]

Equations (20), (24), and (27) prove (1).

---

## 2.6 Relation to the accepted Fisher defect

The marginal score identity gives

\[
S_A=E_p[S\mid Y_A],
\qquad
S_B=E_p[S\mid Y_B],
\]

and

\[
\partial_a\ell=S-S_A-S_B.
\]

Therefore

\[
\begin{aligned}
\mathcal I_{\mathrm{rel}}
&=
E_p[(S-S_A-S_B)^2]\\
&=
E_p[S^2]-E_p[S_A^2]-E_p[S_B^2]
+2E_p[S_AS_B]\\
&=
D_F+2E_p[S_AS_B].
\end{aligned}
\]

This proves (2). Subtracting (2) from (1) proves (3).

The new identity consequently explains the large six-site cancellation structurally:

\[
\underbrace{D_F}_{\text{accepted Fisher}}
+
\underbrace{C_{\mathrm{acc}}}_{\text{acceleration}}
=
\underbrace{\mathcal I_{\mathrm{rel}}}_{\text{surviving Fisher}}
-
\underbrace{\mathcal B}_{\text{local signed charge}}.
\]

---

# 3. Quantitative interface to the original Shannon entropy rate

Let

\[
F_N(a)=-H_N''(a).
\]

For a cut \(A\sqcup B\),

\[
H_{AB}=H_A+H_B-M_{A,B}
\]

implies

\[
F_{AB}=F_A+F_B+M_{A,B}''.
\tag{28}
\]

Fix a leaf length \(L\), and suppose

\[
F_L(a)\ge f_L
\qquad\text{for every }a\in J.
\tag{29}
\]

For an adjacent equal-block Toeplitz cut with each side of length \(m\), define

\[
e_m(J)
=
\sup_{a\in J}
\widehat\varepsilon(A_m,B_m;a).
\tag{30}
\]

Consider a dyadic merge tree with \(q=2^R\) leaves. At level \(k\), each side of a merge has length

\[
m_k=2^{k-1}L,
\]

and there are \(q/2^k\) such merges.

Use the Fisher–Burg residual for the first \(K\) levels. For the remaining levels, use the audited S74 estimate. Then

\[
\begin{aligned}
F_{qL}(a)\ge{}&
qf_L
-
\sum_{k=1}^K
\frac q{2^k}e_{2^{k-1}L}(J)\\
&-
B_\delta
\sum_{\text{levels }k>K}
\sum_{\text{merges at }k}
\|K_{AB}\|_{\mathrm{HS}}^2.
\end{aligned}
\tag{31}
\]

The accepted once-only charge identity gives exactly

\[
\sum_{\text{levels }k>K}
\sum_{\text{merges}}
\|K_{AB}\|_{\mathrm{HS}}^2
=
\frac{c^2}{2}
\left[
\operatorname{tr}Q_{\rho,qL}^2
-
\frac q{2^K}
\operatorname{tr}Q_{\rho,2^KL}^2
\right].
\tag{32}
\]

Writing

\[
D_{\rho,N}
=
\operatorname{tr}(Q_{\rho,N}-Q_{\rho,N}^2),
\]

division by \(qL\) and passage to the entropy-value limit give the curvature margin

\[
\boxed{
\begin{aligned}
\kappa_{L,K}
={}&
\frac{f_L}{L}
-
\frac1L
\sum_{k=1}^K
2^{-k}e_{2^{k-1}L}(J)\\
&-
\frac{B_\delta c^2}{2^{K+1}L}
D_{\rho,2^KL}.
\end{aligned}
}
\tag{33}
\]

Therefore, for \(a_\lambda=(1-\lambda)a_0+\lambda a_1\),

\[
\boxed{
\begin{aligned}
h(a_\lambda)
&-(1-\lambda)h(a_0)-\lambda h(a_1)\\
&\ge
\frac{\kappa_{L,K}}2
\lambda(1-\lambda)(a_1-a_0)^2.
\end{aligned}
}
\tag{34}
\]

No derivative of an \(o(N)\) entropy error is taken. The curvature is integrated at finite volume first, exactly as in the accepted S74 bridge. The old bound and its exact accumulation were independently audited. citeturn167681view0turn167681view2

### Important special case

If the strong but checkable condition

\[
\mathcal B_+\le\mathcal I_{\mathrm{rel}}
\]

is certified for the first \(K\) levels, then all corresponding \(e_m(J)\) vanish. Only the exponentially suppressed S74 tail remains:

\[
\kappa_{L,K}
=
\frac{f_L}{L}
-
\frac{B_\delta c^2}{2^{K+1}L}
D_{\rho,2^KL}.
\tag{35}
\]

This is the quantitative interface back to the original Shannon entropy.

---

# 4. Why the old quadratic payment is structurally wasteful

## PROVED LEMMA 3 — quartic onset under cut interpolation

Let

\[
K_t=
\begin{pmatrix}
K_A&tX\\
tX^*&K_B
\end{pmatrix},
\qquad
q=P_{K_0}=p_Ap_B.
\]

For a configuration \(y\), write

\[
A_y=K_A-\operatorname{diag}(1-y_A),
\qquad
B_y=K_B-\operatorname{diag}(1-y_B).
\]

Schur complementation gives the exact likelihood ratio

\[
\boxed{
\frac{p_t(y)}{q(y)}
=
\det\!\left(
I-t^2B_y^{-1}X^*A_y^{-1}X
\right).
}
\tag{36}
\]

Hence, for fixed finite dimension,

\[
g_t(y)=1-t^2T_y+O(t^4),
\qquad
T_y=\operatorname{tr}(B_y^{-1}X^*A_y^{-1}X).
\tag{37}
\]

Normalization gives

\[
E_qT=0.
\]

Since

\[
M_t=E_q[g_t\log g_t],
\]

one obtains

\[
\boxed{
M_t
=
\frac{t^4}{2}E_q[T^2]+O(t^6).
}
\tag{38}
\]

On a compact strict-contraction interval, finite-dimensional analyticity permits two \(a\)-derivatives, so

\[
\boxed{
M_t''=O(t^4).
}
\tag{39}
\]

In contrast, \(D_F(t)\) and \(C_{\mathrm{acc}}(t)\) separately start at order \(t^2\). Their complete \(t^2\) cancellation is exactly what (1) exposes:

\[
\mathcal I_{\mathrm{rel}}(t)=O(t^4),
\qquad
\mathcal B(t)=O(t^4).
\tag{40}
\]

Thus an estimate that bounds \(C_{\mathrm{acc}}\) in absolute value at order
\(\|X\|_{\mathrm{HS}}^2\) necessarily throws away the leading Fisher compensation.

---

# 5. Decisive obstruction to a strict \(\theta<1\)

Consider a strict two-site equal-marginal DPP,

\[
K=
\begin{pmatrix}
u&z\\
\bar z&u
\end{pmatrix},
\qquad
d=|z|^2.
\]

At \(u=1/2\), put \(x=4d\in(0,1)\). Direct computation gives

\[
\boxed{
D_F=\frac{8x}{1-x}
=
\frac{32d}{1-4d},
}
\tag{41}
\]

and

\[
\boxed{
C_{\mathrm{acc}}
=
4\log\frac{1-x}{1+x}.
}
\tag{42}
\]

Therefore

\[
D_F=32d+O(d^2),
\qquad
-C_{\mathrm{acc}}=32d+O(d^3),
\]

and

\[
\boxed{
\lim_{d\downarrow0}
\frac{-C_{\mathrm{acc}}}{D_F}=1.
}
\tag{43}
\]

Suppose there were constants \(\theta<1\) and \(C<\infty\) such that, uniformly over these strict two-site cuts,

\[
-C_{\mathrm{acc}}
\le
\theta D_F+C\,d^2.
\tag{44}
\]

Since \(d=\|K_{AB}\|_{\mathrm{HS}}^2\), the last term is quartic in the cross-kernel amplitude. Dividing (44) by \(d\) and sending \(d\downarrow0\) would give

\[
32\le32\theta,
\]

a contradiction.

More generally:

\[
\boxed{
\text{No uniform }\theta<1\text{ estimate can have }
E_{\mathrm{cut}}=o(\|K_{AB}\|_{\mathrm{HS}}^2).
}
\tag{45}
\]

This does **not** disprove:

- \(\theta=1\);
- a \(\theta<1\) estimate with another quadratic residual;
- a special fixed-\(t=1\) inequality using sine-kernel geometry.

It does rule out the natural hope that a fixed fraction of \(D_F\) can be removed while all remaining cost begins at fourth order.

---

# 6. Useful narrower replacement: all equal-marginal two-site laws

## PROVED THEOREM 4

Let

\[
0<u<1,
\qquad
0<d<\min\{u^2,(1-u)^2\},
\qquad
v=u(1-u).
\]

For the equal-marginal two-site DPP,

\[
\boxed{
M''\ge
\frac{3-10v}{v^4}\,d^2>0.
}
\tag{46}
\]

At \(u=1/2\),

\[
\boxed{
M''\ge128d^2.
}
\tag{47}
\]

### Proof

The four probabilities are

\[
p_{11}=u^2-d,
\quad
p_{10}=p_{01}=v+d,
\quad
p_{00}=(1-u)^2-d.
\]

One computes

\[
D_F
=
\frac{4u^2}{u^2-d}
+
\frac{2(1-2u)^2}{v+d}
+
\frac{4(1-u)^2}{(1-u)^2-d}
-
\frac2v,
\tag{48}
\]

and

\[
C_{\mathrm{acc}}
=
2\log
\frac{(u^2-d)((1-u)^2-d)}
{(v+d)^2}.
\tag{49}
\]

Let

\[
\tau=\frac{u}{1-u}.
\]

Because \(d<\min\{u^2,(1-u)^2\}\le v\), all geometric and logarithmic series converge absolutely. Expansion of (48)–(49) gives

\[
M''
=
\sum_{k=2}^\infty A_kd^k,
\tag{50}
\]

where

\[
\boxed{
A_k
=
2v^{-k}
\left[
\left(2-\frac1k\right)
(\tau^k+\tau^{-k})
+
(-1)^k
\left(
\frac{1-4v}{v}+\frac2k
\right)
\right].
}
\tag{51}
\]

The \(k=1\) coefficient cancels exactly.

For even \(k\), every term in the bracket is positive.

For odd \(k\ge3\), observe that

\[
\frac{1-4v}{v}
=
\tau+\tau^{-1}-2
\]

and

\[
\tau^k+\tau^{-k}\ge\tau+\tau^{-1}.
\]

Therefore the bracket in (51) is at least

\[
\begin{aligned}
&
\left(2-\frac1k\right)(\tau+\tau^{-1})
-
\left(\tau+\tau^{-1}-2+\frac2k\right)\\
&=
\left(1-\frac1k\right)
(\tau+\tau^{-1}+2)>0.
\end{aligned}
\]

Thus every \(A_k\), \(k\ge2\), is positive. Finally,

\[
A_2
=
\frac{3-10v}{v^4},
\]

which proves (46).

This theorem supplies a genuine quartic positive payment in the smallest cut. It cannot be added edge by edge in larger blocks, because the certified six-site mixed-coordinate obstruction rules out entrywise positivity.

---

# 7. Actual six-site sine diagnostic

At

\[
\rho=\frac12,\qquad
c=\frac{19}{20},\qquad
a=\frac1{40},
\qquad
A=\{1,2,3\},\ B=\{4,5,6\},
\]

the packet’s interval computation certifies

\[
D_F\approx32.590751960324245,
\]

\[
C_{\mathrm{acc}}\approx-18.840984489970979,
\]

and

\[
M''\approx13.749767470353266.
\]

It also certifies that one mixed diagonal Hessian entry is negative, so an entrywise-positive proof is unavailable. citeturn167681view0

The new decomposition was evaluated here using all 64 actual atom weights:

\[
\mathcal I_{\mathrm{rel}}
=
18.552546427729087,
\]

\[
\mathcal B
=
4.802778957375804,
\]

\[
\mathcal B_+
=
6.188926633071633,
\]

\[
\mathcal B_-
=
1.386147675695830,
\]

and consequently

\[
\mathcal I_{\mathrm{rel}}-\mathcal B
=
13.749767470353283,
\]

while the stronger bad-rectangle certificate gives

\[
\boxed{
M''
\ge
\mathcal I_{\mathrm{rel}}-\mathcal B_+
=
12.363619794657454>0.
}
\tag{52}
\]

Thus the new sufficient condition proves positivity at this floating-point base point even after all favorable negative rectangles are discarded.

It also explains the original \(D_F+C_{\mathrm{acc}}\) numbers:

\[
2E_p[S_AS_B]
=
\mathcal I_{\mathrm{rel}}-D_F
\approx-14.03820553259519,
\]

and

\[
C_{\mathrm{acc}}
=
2E_p[S_AS_B]-\mathcal B
\approx-18.84098448997099.
\]

---

## Additional executed size diagnostics

At the same \((\rho,c,a)=(0.5,0.95,0.025)\), for adjacent equal halves:

| Total size | \(\mathcal I_{\mathrm{rel}}\) | \(\mathcal B_+\) | Certified lower bound \(\mathcal I_{\mathrm{rel}}-\mathcal B_+\) | Direct \(M''\) |
|---:|---:|---:|---:|---:|
| 2 | 1.687554309 | 0.142087295 | 1.545467014 | 1.545467014 |
| 4 | 10.837555116 | 3.209596892 | 7.627958224 | 8.332816280 |
| 6 | 18.552546428 | 6.188926633 | 12.363619795 | 13.749767470 |
| 8 | 26.711057341 | 9.979346940 | 16.731710400 | 19.089609958 |
| 10 | 33.582117835 | 13.621092351 | 19.961025484 | 23.174113761 |
| 12 | 40.475516441 | 17.373081526 | 23.102434914 | 27.049086082 |

A further 45-point scan used

\[
c\in\{0.925,0.9375,0.95\},
\quad
a\in\{0.02,0.025,0.03\},
\quad
N\in\{2,4,6,8,10\}.
\]

Every bad-rectangle certificate was positive. The smallest was

\[
1.3575784131196387
\]

at \(c=0.925,a=0.03,N=2\).

These computations used NumPy double precision and are **not interval certificates**. They are finite diagnostics only. The complete executable source is here:

:chatgpt-content-reference{index="6"}

The script enumerates every word, constructs derivatives from actual deleted marginals, evaluates every conditional rectangle, checks

\[
M''=\mathcal I_{\mathrm{rel}}-\mathcal B,
\]

and runs the stated parameter scan.

---

# 8. Quantified remaining payment at the audited hard point

For

\[
\rho=\frac12,\quad c=0.95,\quad J=[0.02,0.03],
\]

the audited S74 constant is approximately

\[
B_\delta=8.654336163038125\times10^{20},
\]

and its direct two-site merge budget is approximately

\[
-5.806308012581715\times10^{19}.
\]

That failure is a failure of the conservative payment, not evidence of rate nonconcavity. citeturn167681view0

The hybrid formula (33) quantifies what would be needed to eliminate this enormous constant from all but the far tail.

Take \(L=2\). The accepted two
