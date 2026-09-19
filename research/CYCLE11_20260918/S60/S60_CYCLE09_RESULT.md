# S60 cycle09 — rank-one Fisher common-shift comparison

## Status and verdicts

### Main universal question [CF]

**INCOMPLETE.** I did not obtain either an all-dimensional proof of
\[
\frac{d^2}{da^2}F_v(K+aI)\ge 0
\]
or a certified strict-contraction counterexample. No numerical search result is promoted to a theorem.

The principal progress is a pair of exact, reusable reductions and a sharp positive comparison theorem:

1. an **Appell/moment-Gram representation**
   \[
   F_v(A+hI)=m^*G_A(h)^{-1}m,
   \]
   in which the rank-one tangent vector \(m\) is independent of the common shift;
2. a **fixed product-chaos normal form**
   \[
   F_v(A+hI)=\mathbb E_{\pi_{x+h\mathbf 1}}
   \left[\frac{S_h(Y)^2}{R_h(Y)}\right],
   \]
   where all determinant coefficients in \(R_h,S_h\) are independent of \(h\);
3. a **first-chaos comparison theorem** whose own common-shift curvature obeys the sharp bound
   \[
   \frac{d^2}{dh^2}\bigl[d^TC(A+hI)^{-1}d\bigr]
   \ge \frac{32}{n}\|v\|^4.
   \]

The exact remaining operator inequality is displayed in Section 6.

### Paid subcases

* \(n=1\): proved, with the sharp constant \(32\|v\|^4\).
* Every diagonal kernel: proved, with
  \[
  F_v''\ge 32\sum_i|v_i|^4\ge \frac{32}{n}\|v\|^4.
  \]
* More strongly, for a product Bernoulli law, the transported Fisher norm is convex for **every** zero-mass signed tangent, not only a rank-one DPP tangent.
* One nontrivial complex three-site correlated family is checked exactly and remains positive; it is an adversarial check, not a universal theorem.

### Reveal consequence

**Conditional theorem only.** If [CF] is true for all strict finite kernels, then the one-site Jensen inequality for \(\Phi\), and its finite exterior-set iteration under a block-only common shift, follow rigorously. This does not pay the cross-block entropy Hessian, an infinite-volume passage, or the sine entropy-rate theorem.

### Sine posterior statement

**OPEN here.** Neither [CF] nor the weaker averaged reveal inequality for the designated sine posterior family is proved. A generic counterexample to [CF], if later found, would not by itself refute that weaker averaged sine statement.

### Status separation

This S60 result does not alter the original QWE01 author-proof status or the later independent-review status. The main S60 status is the separate **INCOMPLETE** verdict above. No repository-only assertion is used as a proved step below; all mathematical claims used here are proved in this report or explicitly labelled computational/conjectural.

---

## 1. Setup

Write \(A=K+a_0I\) for a fixed strict kernel, and use \(h\) for a further legal common shift. For \(y\in\{0,1\}^n\),
\[
M_y(h)=A+hI-\operatorname{diag}(1-y),\qquad V_y(h)=M_y(h)^{-1}.
\]
For the fixed rank-one direction \(H=vv^*\), define
\[
p_h(y)=(-1)^{n-|y|}\det M_y(h),\qquad
q_h(y)=\left.\partial_t p_{A+hI+tH}(y)\right|_{t=0}.
\]
Then
\[
q_h(y)=p_h(y)u_h(y),\qquad u_h(y)=v^*V_y(h)v\in\mathbb R,
\]
and
\[
F_v(A+hI)=\sum_y\frac{q_h(y)^2}{p_h(y)}=\mathbb E_h[u_h^2].
\]
Complex conjugation is always the Hermitian one; in particular \(H_{ij}=v_i\overline{v_j}\).

The reviewed moving-law identity is
\[
F_v''=\mathbb E\!ig[(s^2-\operatorname{Tr}V^2)u^2-4suz+2z^2+4uw\big],
\]
with \(s=\operatorname{Tr}V\), \(u=v^*Vv\), \(z=v^*V^2v\), and \(w=v^*V^3v\). The work below does not merely repeat this identity.

---

## 2. Exact common-shift transport on the cube

For a signed vector \(r\) on the cube, define
\[
(D_i r)(y)=(2y_i-1)\bigl(r(y^{i=0})+r(y^{i=1})\bigr),
\qquad L=\sum_{i=1}^nD_i.
\]
The operators \(D_i\) commute and satisfy \(D_i^2=0\). Directly from multilinearity of the atom determinant in the diagonal entries,
\[
p_h=e^{hL}p_0,\qquad q_h=e^{hL}q_0.
\]
Thus the law and its rank-one tangent are transported by the same universal cube shear.

The tangent has invariant mass and first moments:
\[
\sum_yq_h(y)=0,
\qquad
\sum_y y_iq_h(y)=|v_i|^2=:d_i.
\]
The second identity follows by differentiating the DPP marginal identity \(\mathbb E(Y_i)=A_{ii}+h\) in the direction \(vv^*\).

This transport is not a generic Markov channel: its matrix has signed entries. Therefore ordinary data processing or generic Fisher-convexity statements do not apply automatically.

---

## 3. Exact Appell/moment-Gram representation

This is the cleanest all-dimensional reduction obtained in S60.

For each subset \(S\subseteq[n]\), define the moving square-free polynomial
\[
\psi_S^{(h)}(y)=\prod_{i\in S}(y_i-h).
\]
DPP inclusion moments satisfy \(\mathbb E_{A+hI}Y_S=\det(A_S+hI_S)\). Expanding both the product and the determinant gives the cancellation identity
\[
\boxed{\quad
\mathbb E_{A+hI}\psi_S^{(h)}(Y)=\det A_S.
\quad}                                                     \tag{3.1}
\]
Indeed,
\[
\sum_{R\subseteq S}(-h)^{|S|-|R|}\det(A_R+hI_R)=\det A_S,
\]
by the principal-minor expansion of \(\det(A_R+hI_R)\) followed by binomial cancellation.

Differentiate (3.1) in the fixed rank-one direction \(H=vv^*\). The resulting tangent moments are also independent of \(h\):
\[
\boxed{\quad
m_S:=\sum_y q_h(y)\psi_S^{(h)}(y)
=\left.\partial_t\det(A_S+t v_Sv_S^*)\right|_{t=0}.
\quad}                                                     \tag{3.2}
\]
Thus \(m_\varnothing=0\), and for nonempty \(S\), since \(A_S>0\),
\[
m_S=\det(A_S)\,v_S^*A_S^{-1}v_S
     =v_S^*\operatorname{adj}(A_S)v_S\ge0.               \tag{3.3}
\]

Let \(G_A(h)\) be the full \(2^n\times2^n\) Gram matrix
\[
G_A(h)_{S,T}=\mathbb E_{A+hI}
  [\psi_S^{(h)}(Y)\psi_T^{(h)}(Y)].                       \tag{3.4}
\]
Strict full support and linear independence of the square-free monomials imply \(G_A(h)>0\).

Because \(u_h=q_h/p_h\) is the Riesz representative of the functional in (3.2), expansion in the complete basis \(\{\psi_S^{(h)}\}\) gives
\[
\boxed{\quad
F_v(A+hI)=m^*G_A(h)^{-1}m.
\quad}                                                     \tag{3.5}
\]
This is exact, not a bound.

There is also an explicit entry formula. Put \(I=S\cap T\) and \(J=S\triangle T\). Since a Bernoulli variable obeys
\[
(Y_i-h)^2=(1-2h)(Y_i-h)+h(1-h),
\]
(3.1) yields
\[
\boxed{
G_A(h)_{S,T}
=\sum_{R\subseteq I}(1-2h)^{|R|}[h(1-h)]^{|I|-|R|}
  \det A_{J\cup R}.                                      \tag{3.6}
}
\]
Consequently, with \(b(h)=G_A(h)^{-1}m\),
\[
\boxed{
F_v''(A+hI)
=2b^*G_A'G_A^{-1}G_A'b-b^*G_A''b.                         \tag{3.7}
}
\]

Formula (3.7) is a finite, explicit inverse-Gram curvature problem. It is substantially more rigid than the original resolvent expectation, because the tangent vector \(m\) is frozen.

### A false shortcut exposed by (3.6)

One cannot prove (3.7) merely by claiming \(G_A''\preceq0\). This fails even for a product law. Take \(n=2\), \(A=(1/10)I\), and the coefficient vector corresponding to \(\psi_{\{1,2\}}\). Then
\[
G_{12,12}(h)=\left(\frac1{10}+\frac45h-h^2\right)^2,
\qquad G_{12,12}''(0)=\frac{22}{25}>0.                    \tag{3.8}
\]
The positive first term in (3.7) is essential.

---

## 4. Fixed product-chaos normal form

A second exact reduction freezes every coefficient under the common shift.

Let
\[
x_i=A_{ii},\qquad D=\operatorname{diag}x,
\qquad B=A-D,
\]
so \(B\) is Hermitian with zero diagonal and is unchanged by \(A\mapsto A+hI\). Let \(\pi_x\) be the independent Bernoulli law with parameters \(x_i\). For \(S\subseteq[n]\), write
\[
r_S(x)=\partial_{x_S}\pi_x
\]
for its signed atom vector.

The DPP probability generating polynomial is
\[
P_A(z)=\det(I-A+AZ)=\det(I+A\operatorname{diag}(z-1)).
\]
Expanding principal minors and then expanding \(\det(D_T+B_T)\) by the diagonal entries gives
\[
\boxed{
 p_A=\sum_{S\subseteq[n]}c_S r_S(x),
 \qquad c_S=\det B_S.                                    \tag{4.1}
}
\]
Equivalently, the DPP common-shift curve is a fixed signed determinant transform of the product curve.

Now split the rank-one direction as
\[
H=vv^*=\operatorname{diag}d+C,
\qquad d_i=|v_i|^2,
\qquad C_{ii}=0.
\]
Let
\[
\dot c_S=D_C\det(B_S)
=\operatorname{Tr}(\operatorname{adj}(B_S)C_S),
\]
with the adjugate formula covering singular \(B_S\). Differentiating (4.1) gives
\[
\boxed{
q_{A,H}=\sum_{T\subseteq[n]}m_T r_T(x),
\qquad
m_T=\dot c_T+\sum_{i\in T}d_i c_{T\setminus\{i\}}.       \tag{4.2}
}
All \(c_S,m_T\) are real and are unchanged by a common diagonal shift.

Define the product score factors
\[
\chi_i^{x}(y)=\frac{y_i-x_i}{x_i(1-x_i)},
\qquad \chi_S^x=\prod_{i\in S}\chi_i^x.
\]
Since \(r_S(x)(y)=\pi_x(y)\chi_S^x(y)\), put
\[
R_x(y)=\sum_Sc_S\chi_S^x(y),
\qquad S_x(y)=\sum_Tm_T\chi_T^x(y).
\]
Then
\[
p_A(y)=\pi_x(y)R_x(y),\qquad q_{A,H}(y)=\pi_x(y)S_x(y),
\]
and hence
\[
\boxed{
F_v(A)=\mathbb E_{\pi_x}\left[\frac{S_x(Y)^2}{R_x(Y)}\right].  \tag{4.3}
}
Along \(A+hI\), only \(x\) changes to \(x+h\mathbf1\); the determinant coefficients \(c,m\) stay frozen.

This normal form is a practical falsification/proof interface. The diagonal case is exactly \(R\equiv1\). The unresolved issue is the determinantal denominator \(R\), not transport of the coefficients.

---

## 5. Sharp first-chaos comparison theorem

Let
\[
X=Y-\operatorname{diag}A,
\]
and let \(C(A)=\operatorname{Cov}_A(Y)\). For a DPP,
\[
C_{ii}=A_{ii}(1-A_{ii}),
\qquad C_{ij}=-|A_{ij}|^2\quad(i\ne j).                   \tag{5.1}
\]
Strict full support implies \(C(A)>0\): a nonzero linear function of \(Y\) cannot be almost surely constant under a law assigning positive mass to every cube point.

The rank-one score satisfies
\[
\mathbb E_A[uX_i]
=\left.\partial_t\mathbb E_{A+t vv^*}Y_i\right|_{t=0}
=|v_i|^2=d_i.                                             \tag{5.2}
\]
Projecting \(u\) onto the linear span of the centered occupations gives the exact Cramér--Rao/least-squares comparison
\[
\boxed{
F_v(A)=\mathbb E[u^2]\ge G_v(A):=d^TC(A)^{-1}d.           \tag{5.3}
}

The comparison functional has strictly positive common-shift curvature. Along \(A+hI\),
\[
C' =\operatorname{diag}(1-2A_{ii}-2h),
\qquad C''=-2I.
\]
Writing \(b=C^{-1}d\), direct inverse differentiation gives
\[
\boxed{
G_v''
=2b^TC'C^{-1}C'b+2b^Tb
=2\|C^{-1/2}C'b\|^2+2\|b\|^2.                            \tag{5.4}
}
\]
In particular \(G_v''>0\) for \(v\ne0\).

There is a dimension-sharp lower bound. Since
\[
C\mathbf1=\operatorname{diag}(A(I-A)),                    \tag{5.5}
\]
and \(0\le A(I-A)\le I/4\), every component of \(C\mathbf1\) lies in \([0,1/4]\). Therefore
\[
\|v\|^2=d^T\mathbf1=b^TC\mathbf1
\le \|b\|\,\frac{\sqrt n}{4}.
\]
Using (5.4),
\[
\boxed{
G_v''(A+hI)\ge\frac{32}{n}\|v\|^4.                      \tag{5.6}
}
\]
The constant is sharp: at \(A+hI=I/2\), with \(|v_i|\) all equal, \(C=I/4\), \(C'=0\), and equality holds.

### What this theorem does and does not prove

It proves a universal, sharp, convex lower comparator for the Fisher information itself. It does **not** permit the inference \(F_v''\ge G_v''\); pointwise domination does not imply domination of second derivatives.

Define the nonlinear-information residual
\[
\mathcal R_v(A)=F_v(A)-d^TC(A)^{-1}d\ge0.                 \tag{5.7}
\]
The sufficient lemma
\[
\mathcal R_v(A+hI)''\ge0                                 \tag{HC}
\]
would imply the stronger bound
\[
F_v''\ge\frac{32}{n}\|v\|^4,
\]
but (HC) is not proved here and may be stronger than [CF].

---

## 6. The precise all-dimensional missing lemma

The Appell reduction identifies a finite operator statement.

### Appell inverse-curvature lemma (unproved)

For every strict DPP kernel \(A\), form \(G_A(h)\) by (3.4)--(3.6). For every rank-one tangent vector
\[
m_S=v_S^*\operatorname{adj}(A_S)v_S,
\qquad m_\varnothing=0,
\]
prove, throughout the legal shift interval,
\[
\boxed{
2b^*G_A'G_A^{-1}G_A'b-b^*G_A''b\ge0,
\qquad b=G_A^{-1}m.                                      \tag{AIC-r1}
}
\]
By (3.5)--(3.7), (AIC-r1) is exactly sufficient for [CF].

A stronger, numerically supported but unproved statement is
\[
\boxed{
(G_A(h)^{-1})''\succeq0
\quad\text{on }\{m:m_\varnothing=0\}.                   \tag{AIC-all}
}
\]
This would settle not only rank-one tangents but every zero-mass signed tangent transported by the common cube shear. It is true for product measures by Section 7. The elementary shortcut \(G_A''\preceq0\) is false by (3.8), so any proof of (AIC-all) must use the full inverse-curvature cancellation in (3.7).

This is the precise unproved lemma left by S60. It has explicit inputs, an explicit finite matrix, and an exact conclusion.

---

## 7. Product laws: an all-tangent convexity theorem

This is stronger than the diagonal rank-one subcase.

Let \(\pi_x\) be the product Bernoulli law with \(0<x_i<1\), and let \(q_x\) be any zero-mass signed vector. The derivative vectors
\[
r_S(x)=\partial_{x_S}\pi_x,\qquad S\subseteq[n],
\]
form a basis. Hence uniquely
\[
q_x=\sum_{\varnothing\ne S\subseteq[n]}\alpha_S r_S(x).  \tag{7.1}
\]
Under common cube transport, the coefficients \(\alpha_S\) remain fixed:
\[
q_{x+h\mathbf1}=\sum_{S\ne\varnothing}\alpha_Sr_S(x+h\mathbf1).
\]
Moreover,
\[
\frac{r_S(x)(y)}{\pi_x(y)}
=\prod_{i\in S}\frac{y_i-x_i}{x_i(1-x_i)}.
\]
Independence and centering make these scores mutually orthogonal, and therefore
\[
\boxed{
\sum_y\frac{q_{x+h\mathbf1}(y)^2}{\pi_{x+h\mathbf1}(y)}
=\sum_{S\ne\varnothing}|\alpha_S|^2
 \prod_{i\in S}\frac1{(x_i+h)(1-x_i-h)}.                 \tag{7.2}
}
Each factor \(g_i(h)=1/[(x_i+h)(1-x_i-h)]\) is positive and log-convex because
\[
(\log g_i)''=\frac1{(x_i+h)^2}+\frac1{(1-x_i-h)^2}>0.
\]
A product of positive log-convex functions is log-convex and hence convex. Every term in (7.2) is therefore convex.

**Theorem.** For a product Bernoulli law, common-shift Fisher convexity holds for every transported zero-mass tangent.

For a diagonal DPP and the rank-one direction \(vv^*\), only singleton coefficients occur, \(\alpha_{\{i\}}=|v_i|^2\). Thus
\[
F_v(A+hI)=\sum_i\frac{|v_i|^4}{(A_{ii}+h)(1-A_{ii}-h)},   \tag{7.3}
\]
and
\[
F_v''\ge32\sum_i|v_i|^4\ge\frac{32}{n}\|v\|^4.         \tag{7.4}
\]
For \(n=1\), explicitly,
\[
F_v''=
\frac{2|v|^4(1-3x+3x^2)}{x^3(1-x)^3}\ge32|v|^4.         \tag{7.5}
\]

---

## 8. Adversarial exact checks

### 8.1 A single configuration can have negative curvature

Termwise convexity is false even for a legal diagonal kernel. Take
\[
A=\operatorname{diag}(4/5,1/5),\qquad v=e_1,
\]
and the full configuration \(y=(1,1)\). Its single atom contribution is
\[
p_y(a)u_y(a)^2=\frac{a+1/5}{a+4/5},
\]
so
\[
\left.\frac{d^2}{da^2}[p_y(a)u_y(a)^2]\right|_{a=0}
=-\frac{75}{32}<0.                                       \tag{8.1}
\]
The other configurations supply the positive compensation in the full diagonal theorem.

### 8.2 The reviewed legal mixed-entry example

For
\[
A=\begin{pmatrix}1/5&1/10\\1/10&3/5\end{pmatrix},
\qquad v=(1,1)^T,
\]
the supplied exact values are
\[
(F_v)_{12}=-\frac{7058578388000000}{3400782877756341}<0,
\]
while
\[
F_v''(A;I)=
\frac{1095440907576040000}{3400782877756341}>0.
\]
This correctly rejects entrywise Hessian positivity as a route to [CF].

For the new first-chaos comparator,
\[
C=\frac1{100}\begin{pmatrix}16&-1\\-1&24\end{pmatrix},
\qquad
C^{-1}d=\begin{pmatrix}2500/383\\1700/383\end{pmatrix},
\]
and exact arithmetic gives
\[
G_v''=\frac{17967160000}{56181887}>0.                    \tag{8.2}
\]
Numerically this is about \(319.8\), while the full curvature is about \(322.1\): the linear-occupation comparator pays most, but not all, of this example.

### 8.3 A correlated complex three-site family

Let
\[
L_\rho=\begin{pmatrix}1&\rho&0\\\rho&1&\rho\\0&\rho&1\end{pmatrix},
\qquad
h=(1,i,1)^T,
\qquad
A=L_\rho(I+L_\rho)^{-1},
\qquad
v=(I+L_\rho)^{-1}h.
\]
For \(t=\rho^2\in[0,1/2)\), direct exact enumeration in the \(L\)-ensemble gives
\[
F_v''=
\frac1{8-4t}\left[
50+60t+44t^2
+\frac{2(-46+148t-30t^2)}{(1-t)^3}
+\frac{90-468t+864t^2}{(1-2t)^3}
\right].                                                  \tag{8.3}
\]
After clearing the positive denominators, the remaining numerator is
\[
N(t)=48-280t+752t^2-1004t^3+944t^4-996t^5
+1144t^6-1104t^7+352t^8.
\]
Writing \(x=2t\in[0,1]\), the degree-eight Bernstein coefficients of \(N(x/2)\) are
\[
48,\ \frac{61}{2},\ \frac{138}{7},\ \frac{1501}{112},\
\frac{1423}{140},\ \frac{569}{64},\ \frac{495}{56},\
\frac{297}{32},\ 9,
\]
all strictly positive. Therefore (8.3) is positive throughout the legal range.

This family was chosen to include nontrivial correlation and a genuinely complex direction. It is a falsification check only; it does not establish [CF].

### 8.4 Floating search status

Adversarial floating searches and joint optimization through dimension six did not produce a common-direction negative value. Their apparent minimum repeatedly approached
\[
A=I/2,\qquad |v_i|=\|v\|/\sqrt n,
\qquad F_v''=32\|v\|^4/n.
\]
This motivates the sharper conjecture
\[
F_v''\ge32\|v\|^4/n,
\]
but the search is not a certificate and is not used in any proof.

---

## 9. Conditional reveal consequence if [CF] is true

Define
\[
\Phi(B)=\left.\partial_a^2H(B+aI)\right|_{a=0}.
\]
Along any legal rank-one line \(B+tww^*\), every atom is affine in \(t\), so
\[
\partial_t^2H(B+tww^*)=-F_w(B+tww^*).
\]
If [CF] holds at every point of the strict rank-one segment, then
\[
\partial_t^2\Phi(B+tww^*)
=-\left.\partial_a^2F_w(B+tww^*+aI)\right|_{a=0}\le0.
\]
Hence \(\Phi\) is concave on that segment.

For one genuine exterior-site reveal, let
\[
A_1=A-\frac{vv^*}{q},\qquad
A_0=A+\frac{vv^*}{1-q},
\qquad
qA_1+(1-q)A_0=A.
\]
Strictness of the joint kernel and its complement gives strict conditional kernels by Schur complements. The entire segment between \(A_1\) and \(A_0\) is strict because \(0<B<I\) is convex. Concavity therefore gives
\[
q\Phi(A_1)+(1-q)\Phi(A_0)\le\Phi(A).                     \tag{9.1}
\]

For a finite exterior set revealed sequentially, condition on the actual history. When only the block receives the common shift:

* the exterior marginal law is independent of that shift;
* each history-dependent conditional probability \(q_h\) is independent of the block shift;
* each history-dependent coupling vector \(v_h\) is also independent of the block shift;
* the posterior block kernel retains the form \(A_h+aI\).

These facts follow by iterating the actual DPP Schur-complement updates: updates of the unrevealed exterior principal block and of the cross-couplings use only previously exposed exterior data, while the block's \(+aI\) term passes through unchanged.

Applying (9.1) at each history and using the tower property yields
\[
\Phi(A)\ge\mathbb E[\Phi(A_{\mathcal E})],                \tag{9.2}
\]
for every finite exterior set \(\mathcal E\). Since the exterior-history probabilities are independent of the block shift, (9.2) is exactly nonnegative common-shift curvature of the finite block-only mutual information.

What is **not** paid by this argument:

1. common shifts of exterior coordinates;
2. cross-block entries of the complete entropy Hessian;
3. passage to an infinite exterior without a separate limiting/uniform-integrability argument;
4. the remaining QWE01 cross-block budget;
5. full sine entropy-rate concavity.

If [CF] is false, an averaged inequality such as (9.2) could still hold for the actual sine posterior reveal distribution because negative states may be compensated by the reveal weights. That is a distinct statement.

---

## 10. Final ledger

| Item | Status |
|---|---|
| Universal [CF] | **INCOMPLETE** |
| Certified strict negative witness | None obtained |
| Appell/moment-Gram identity (3.5) | **PROVED** |
| Fixed determinant/product-chaos normal form (4.3) | **PROVED** |
| First-chaos comparator (5.3) | **PROVED** |
| Sharp comparator curvature (5.6) | **PROVED** |
| Product-law all-tangent convexity (7.2) | **PROVED** |
| Diagonal-kernel rank-one [CF] | **PROVED** |
| Complex correlated family (8.3) | **EXACTLY CHECKED, POSITIVE** |
| Appell inverse-curvature lemma | **OPEN** |
| One-site reveal Jensen inequality | **CONDITIONAL ON [CF]** |
| Finite exterior block-only MI curvature | **CONDITIONAL ON [CF]** |
| Weaker averaged sine-posterior reveal inequality | **OPEN** |
| Full sine entropy-rate conclusion | **NOT ESTABLISHED** |

