PROVED_SCOPED_LEMMA

# S5 check3: exact actual-adjacent cancellation at the balanced midpoint

## 0. Status and scope

This document proves a new finite-dimensional theorem for the **actual** common-offset channel.  It treats the complete moving-count term, the actual conditional response, the reference entropy, and the full-atom Fisher term at the balanced midpoint

\[
 n=2m,\qquad k=m,\qquad a_0=\frac{1-c}{2},\qquad 0<c<1.
\]

The theorem applies to **every law on the input \(m\)-subsets**, hence in particular to every rank-\(m\) projection DPP and to the genuine contiguous Fourier projections \(P_{n,n/2}\).  It rewrites the full midpoint curvature budget as a count covariance plus a nonnegative weighted Jeffreys production between the compatible actual laws on consecutive output layers.

This is a complete scoped theorem.  It is **not** a proof of the sine entropy-rate target.  The signed central count covariance is not yet paid by the adjacent-layer production uniformly in growing \(n\).  The precise remaining inequalities are stated in Section 8.

## 1. Prior author checkpoint, restated but not counted as new

The preceding author package proposed the mean-overlap clock and obtained the actual-law decomposition

\[
H''=\Phi''-\sum_l\pi_l(2s_l^2\mathcal C_l-s_l'J_l)-W_{\rm core}-\mathcal E_n,
\qquad
W_{\rm core}=\sum_l[-2\pi_l's_lJ_l+\pi_l''F_l].
\]

That package is preserved under `prior_round4/` and as its original ZIP under `prior_archives/`.  Its key endpoint-sensitive estimates are restated here because the present round was instructed to expose them before advancing.

With \(\theta=\log R\), actual conditional density \(r\), Bernoulli--Laplace generator \(L\), and mean-overlap clock speed \(\sigma=\partial_\theta\tau\), define

\[
\xi=\partial_\theta r-\sigma Lr,
\qquad
\Xi=\partial_\theta\xi-\sigma L\xi,
\]
\[
\eta=r_a'-sLr=\theta'\xi,
\qquad
\zeta=\eta_a'-sL\eta=\theta''\xi+(\theta')^2\Xi.
\]

For one fixed input set, let the conditional overlap be \(J\), put \(x=J-\mathbb E J\), let \(v_J=\operatorname{Var}J\), \(t_3=\kappa_3/v_J\), and

\[
Q_2(x)=x^2-t_3x-v_J,
\qquad
A=\frac{(R-1)^2v_J}{Rn h},
\]

where \(h=\mathbb EJ-kl/n\).  The claimed exact material tangent is

\[
\frac{\xi_A}{r_A}=A Q_2.
\]

The material response retained all degree-four terms:

\[
\begin{aligned}
\frac{\Xi_A}{r_A}={}&A^2Q_2^2
+A^2[U_R(2x-t_3)+T_R]Q_2\\
&+A[(t_3-U_R+v_J/h)x^2
+(-\kappa_4/v_J-T_R+U_Rv_J/h)x
+v_J(v_J/h-2t_3)].
\end{aligned}
\]

The stated weighted bounds were

\[
\|\xi\|_{F,r}^2\le (R-1)^2\left(\frac1{32}+\frac1{8n}\right),
\qquad
\|\Xi\|_{F,r}\le M_R.
\]

The endpoint-orbit issue in the prior all-orbit estimate was handled by using both forward and backward complete-orbit couplings.  For

\[
g_A(j)=\mathbb E[\log r(S)\mid |S|=l,\ |A\cap S|=j],
\]

the claimed bound was, for every available second difference including the edge-adjacent ones,

\[
|\Delta^2g_A(j)|\le \frac{8C_{\rm mix}}{d},
\qquad
C_{\rm mix}=96R^2(R-1)^2,
\]

where \(d=\min(k,n-k,l,n-l)\).  One of the two orbit orientations has every relevant group size at least \((d+2)/2\); thus atypical overlap orbits were not removed.  When the overlap diameter is one, \(Q_2\equiv0\).

These statements led to

\[
|\delta_l|=|\langle\log r_l,\eta_l\rangle|\le
4|\theta'|(R-1)C_{\rm mix}=:\chi
\]

and

\[
2\sum_l|\pi_l'\delta_l|
\le 2\chi\sqrt{n\,i_{k/n}},
\]

and, on a fixed legal interior compact set,

\[
|\mathcal E_n|
\le 3\alpha^2+\sqrt n\,[B_0+2\chi\sqrt{i_{k/n}}].
\]

At the midpoint \(\theta'=0\), so \(s_l=\eta_l=0\), but \(\eta_l'\) need not vanish; the preceding package retained it.  The theorem below does **not** assume these provisional estimates.  It gives an independent exact evaluation of the full midpoint budget.  In the accepted notation it evaluates

\[
\sum_l\bigl[\pi_lF_l''+2\pi_l'F_l'+\pi_l''F_l\bigr]
=\sum_l[\pi_lF_l''+\pi_l''F_l]
\]

at \(a_0\), so the result combines the intrinsic/acceleration response with the complete moving-count core rather than estimating only one of them.

## 2. Channel factorization on actual output layers

Let \(\mu\) be any probability law on the \(m\)-subsets of \([n]\), with \(n=2m\).  For a legal interior \(a\), define

\[
R(a)=\frac{(a+c)(1-a)}{a(1-a-c)}.
\]

For an output set \(S\) of size \(l\), the channel atom factors as

\[
p_a(S)=B_l(a)w_l(S;R),
\]

where

\[
B_l(a)=(1-a-c)^m a^l(1-a)^{m-l},
\qquad
w_l(S;R)=\sum_{|A|=m}\mu(A)R^{|A\cap S|}.
\]

Write

\[
e_l(R)=\sum_{|S|=l}w_l(S;R),
\qquad
\pi_l(a)=B_l(a)e_l(R(a)),
\]

and let the actual conditional law and density relative to the uniform law \(u_l\) be

\[
\nu_l(S)=\frac{w_l(S)}{e_l},
\qquad
r_l(S)=\binom nl\nu_l(S).
\]

Its relative entropy is

\[
F_l=\sum_{|S|=l}\nu_l(S)\log r_l(S).
\]

The extreme layers are deterministic: \(F_0=F_n=0\).  No limiting convention is needed in the interior because every channel atom is strictly positive.

## 3. Exact compatible insertion and deletion laws

For \(|S|=l\), define the actual insertion and deletion ratios

\[
h_i(S)=\frac{w_{l+1}(S\cup\{i\})}{w_l(S)},\quad i\notin S,
\qquad
H_l(S)=\sum_{i\notin S}h_i(S),
\]

\[
g_i(S)=\frac{w_{l-1}(S\setminus\{i\})}{w_l(S)},\quad i\in S,
\qquad
G_l(S)=\sum_{i\in S}g_i(S).
\]

### Lemma 3.1: exact affine relation

For every homogeneous input law and every \(S\),

\[
\boxed{
H_l(S)-R G_l(S)=n+(R-1)m-(R+1)l.
}
\tag{3.1}
\]

**Proof.**  Fix one input \(A\), put \(j=|A\cap S|\), and first apply insertion/deletion to the monomial \(R^j\).  The insertion sum is

\[
R^j[(m-j)R+(m-l+j)],
\]

while \(R\) times the deletion sum is

\[
R^jR[(l-j)+j/R].
\]

Their difference is

\[
R^j[m(R+1)-(R+1)l]
=R^j[n+(R-1)m-(R+1)l].
\]

Summing with weights \(\mu(A)\) and dividing by \(w_l(S)\) proves (3.1).  Every insertion and deletion type is present.  \(\square\)

Averaging under \(\nu_l\) gives

\[
\bar H_l:=\mathbb E_{\nu_l}H_l=(l+1)\frac{e_{l+1}}{e_l},
\qquad
\bar G_l:=\mathbb E_{\nu_l}G_l=(n-l+1)\frac{e_{l-1}}{e_l}.
\tag{3.2}
\]

Define the compatible actual deletion and insertion marginals

\[
\widehat\nu_l(S)=\nu_l(S)\frac{H_l(S)}{\bar H_l},
\qquad
\check\nu_l(S)=\nu_l(S)\frac{G_l(S)}{\bar G_l}.
\tag{3.3}
\]

Double counting edges shows

\[
\widehat\nu_l=D^{\rm unif}_{l+1\to l}\nu_{l+1},
\qquad
\check\nu_l=I^{\rm unif}_{l-1\to l}\nu_{l-1}.
\tag{3.4}
\]

Here the first kernel deletes a uniformly selected occupied element, and the second inserts a uniformly selected unoccupied element.  These are the actual adjacent layers of the same channel law, not auxiliary slice flows.

### Lemma 3.2: exact \(\theta=\log R\) response

For \(0<l<n\), and with the evident one-sided formulas at the two extremes,

\[
\boxed{
\partial_\theta\nu_l
=\frac{\bar H_l}{R-1}(\nu_l-\widehat\nu_l)
=\frac{R\bar G_l}{R-1}(\nu_l-\check\nu_l).
}
\tag{3.5}
\]

**Proof.**  For a monomial with overlap \(j\), the insertion numerator is

\[
R^j[mR+m-l-(R-1)j].
\]

Therefore

\[
\partial_\theta\log w_l
=\frac{mR+m-l-H_l}{R-1}.
\]

Subtracting its \(\nu_l\)-mean gives the first formula in (3.5).  The deletion calculation gives

\[
\partial_\theta\log w_l=\frac{R(l-G_l)}{R-1},
\]

which gives the second formula.  \(\square\)

## 4. Edge KL identities for the actual layers

Let

\[
E_l=\{(S,T): |S|=l,\ |T|=l+1,\ S\subset T\}.
\]

On this common edge space define probability laws

\[
\mathsf A_l(S,T)=\frac{\nu_{l+1}(T)}{l+1},
\qquad
\mathsf B_l(S,T)=\frac{\nu_l(S)}{n-l}.
\tag{4.1}
\]

Because

\[
\frac{\binom n{l+1}}{\binom nl}=\frac{n-l}{l+1},
\]

the exact edge likelihood ratio is

\[
\log\frac{\mathsf A_l(S,T)}{\mathsf B_l(S,T)}
=\log r_{l+1}(T)-\log r_l(S).
\tag{4.2}
\]

Put

\[
C_l^+=D(\mathsf A_l\|\mathsf B_l),
\qquad
C_l^-=D(\mathsf B_l\|\mathsf A_l).
\tag{4.3}
\]

### Lemma 4.1: exact directional entropy derivatives

\[
\boxed{
\partial_\theta F_l
=\frac{\bar H_l}{R-1}
[F_l-F_{l+1}+C_l^+]
}
\tag{4.4}
\]

and

\[
\boxed{
\partial_\theta F_l
=\frac{R\bar G_l}{R-1}
[F_l-F_{l-1}+C_{l-1}^-].
}
\tag{4.5}
\]

**Proof.**  Since \(\sum_S\partial_\theta\nu_l(S)=0\),

\[
\partial_\theta F_l
=\sum_S(\partial_\theta\nu_l(S))\log r_l(S).
\]

Insert the first expression from (3.5).  Under \(\widehat\nu_l\), the expectation of \(\log r_l\) equals \(F_{l+1}-C_l^+\) by (4.2).  This gives (4.4).  The insertion marginal similarly has

\[
\mathbb E_{\check\nu_l}\log r_l=F_{l-1}-C_{l-1}^-,
\]

which gives (4.5).  \(\square\)

These identities retain the layer normalizers and both orientations of every adjacent edge.

## 5. Balanced midpoint algebra

Set

\[
a_0=\frac{1-c}{2},
\qquad
v=\frac{1-c^2}{4},
\qquad
R_0=\left(\frac{1+c}{1-c}\right)^2.
\tag{5.1}
\]

The count generating function is

\[
\sum_{l=0}^n\pi_lz^l
=[v+(1-2v)z+vz^2]^m.
\tag{5.2}
\]

Hence

\[
\mathbb EM=m,
\qquad
\operatorname{Var}M=nv.
\tag{5.3}
\]

Direct differentiation gives

\[
\theta'(a_0)=0,
\qquad
v^2\theta''(a_0)=2c.
\tag{5.4}
\]

The adjacent normalizers satisfy

\[
\boxed{
\frac{\pi_l\bar H_l}{R_0-1}
=\frac vc(l+1)\pi_{l+1},
\qquad
\frac{\pi_lR_0\bar G_l}{R_0-1}
=\frac vc(n-l+1)\pi_{l-1}.
}
\tag{5.5}
\]

Indeed \(B_{l+1}/B_l=a_0/(1-a_0)=R_0^{-1/2}\), while

\[
\frac{\sqrt{R_0}}{R_0-1}=\frac vc.
\]

### Lemma 5.1: exact count Stein identity

For every \(0\le l\le n\), with \(\pi_{-1}=\pi_{n+1}=0\),

\[
\boxed{
\begin{aligned}
v^2\pi_l''(a_0)
={}&\pi_l[(l-m)^2-nv]\\
&+v[n\pi_l-(n-l+1)\pi_{l-1}-(l+1)\pi_{l+1}].
\end{aligned}
}
\tag{5.6}
\]

**Proof.**  At the midpoint every full channel atom has score

\[
\frac{p_a'(S)}{p_a(S)}\bigg|_{a_0}=\frac{|S|-m}{v};
\tag{5.7}
\]

this follows already at the complete-data level because the overlap terms cancel.  Differentiating the two-binomial count generating function, or equating coefficients after two derivatives, gives (5.6).  The exact checker verifies (5.6) coefficient by coefficient over the rationals in two independent input examples.  \(\square\)

## 6. Main theorem: full moving-count/adjacent cancellation

Define the full spatial divergence from the uniform conditional references

\[
\mathcal D(a)=\sum_{l=0}^n\pi_l(a)F_l(a)=\Phi(a)-H(a).
\tag{6.1}
\]

For each boundary \(0\le l<n\), define the weighted actual-adjacent Jeffreys production

\[
\boxed{
\mathscr J_l
=(l+1)\pi_{l+1}C_l^+
+(n-l)\pi_l C_l^-.
}
\tag{6.2}
\]

It is nonnegative.  In raw full-atom form it is

\[
\boxed{
\mathscr J_l
=\sum_{\substack{|S|=l,\ T=S\cup\{i\}}}
[p(T)-p(S)]
[\log r_{l+1}(T)-\log r_l(S)].
}
\tag{6.3}
\]

Individual summands in (6.3) need not be nonnegative; nonnegativity follows from the two KL divergences in (6.2).

### Theorem 6.1: balanced actual-adjacent curvature identity

For every law \(\mu\) on the \(m\)-subsets of \([2m]\), every \(0<c<1\), and the midpoint \(a_0=(1-c)/2\),

\[
\boxed{
 v^2\mathcal D''(a_0)
 =\sum_{l=0}^n\pi_l[(l-m)^2-nv]F_l
 +v\sum_{l=0}^{n-1}\mathscr J_l.
}
\tag{6.4}
\]

Consequently, retaining the reference term,

\[
\boxed{
 v^2H''(a_0)
 =v^2\Phi''(a_0)
 -\sum_{l=0}^n\pi_l[(l-m)^2-nv]F_l
 -v\sum_{l=0}^{n-1}\mathscr J_l.
}
\tag{6.5}
\]

The reference curvature is exactly

\[
\boxed{
\Phi''(a_0)
=-\sum_l\pi_l''(a_0)\log\frac{\pi_l}{\binom nl}
-\frac nv.
}
\tag{6.6}
\]

Thus the full count Fisher term \(n/v\), both derivatives of the moving count law, and the complete actual conditional response are present.

**Proof.**  At \(a_0\), \(\theta'=0\), so \(F_l'(a_0)=0\) and

\[
\mathcal D''(a_0)
=\sum_l\pi_l''F_l
+\theta''(a_0)\sum_l\pi_l\partial_\theta F_l.
\tag{6.7}
\]

Put

\[
a_l=(l+1)\pi_{l+1},
\qquad
b_l=(n-l)\pi_l.
\]

Multiplying (5.6) by \(F_l\), summing, and shifting indices gives

\[
\begin{aligned}
v^2\sum_l\pi_l''F_l
={}&\sum_l\pi_l[(l-m)^2-nv]F_l\\
&+v\sum_{l=0}^{n-1}(a_l-b_l)(F_{l+1}-F_l).
\end{aligned}
\tag{6.8}
\]

Now average the two exact representations (4.4) and (4.5), use (5.5), and shift the lower expression by one layer.  This gives

\[
2c\sum_l\pi_l\partial_\theta F_l
=v\sum_{l=0}^{n-1}
[(b_l-a_l)(F_{l+1}-F_l)+\mathscr J_l].
\tag{6.9}
\]

Since \(v^2\theta''(a_0)=2c\), adding (6.8) and (6.9) cancels **every** raw layer-difference term and proves (6.4).  Equation (6.5) follows from \(H=\Phi-\mathcal D\).  Finally, the general moving-reference formula for \(H(\pi)+\sum_l\pi_l\log\binom nl\) gives the first term in (6.6); (5.7) and (5.3) give

\[
\sum_l\frac{(\pi_l')^2}{\pi_l}
=\frac{\mathbb E(M-m)^2}{v^2}=\frac nv.
\]

This proves (6.6).  \(\square\)

### Corollary 6.2: explicit signed part

The second term in (6.4) is a genuine compatible-adjacent production and obeys

\[
\mathscr J_l\ge0.
\tag{6.10}
\]

A fully elementary coarse-graining proof of Pinsker's bound gives the optional quantitative estimate

\[
\mathscr J_l
\ge \frac{(l+1)\pi_{l+1}+(n-l)\pi_l}{2}
\|\mathsf A_l-\mathsf B_l\|_1^2.
\tag{6.11}
\]

Indeed, coarse-grain to the set where \(\mathsf A_l\ge\mathsf B_l\); the resulting binary relative entropy is at least twice the squared total-variation distance by one-variable convexity, yielding \(D(P\|Q)\ge\|P-Q\|_1^2/2\).  Apply this to both directed KL terms.  No sign is assigned to the covariance term in (6.4).

## 7. Direct full-atom square-face formula

The adjacent identity was compared with a second exact representation.  For a pair \(i<j\) and a fixed output word \(z\) on the other \(n-2\) coordinates, write

\[
p_{ab}^{ij}(z)=\Pr(Y_i=a,Y_j=b,Y_{-ij}=z),
\qquad
p_{\bullet\bullet}^{ij}(z)=\sum_{a,b}p_{ab}^{ij}(z).
\]

### Proposition 7.1

For every homogeneous input law at the balanced midpoint,

\[
\boxed{
H''(a_0)
=-2\sum_{i<j}\sum_z p_{\bullet\bullet}^{ij}(z)
\log\frac{p_{00}^{ij}(z)p_{11}^{ij}(z)}
{p_{01}^{ij}(z)p_{10}^{ij}(z)}
-\frac nv.
}
\tag{7.1}
\]

**Proof.**  The derivative of one binary channel row with respect to \(a\) is \((-1,+1)\), independent of the input bit.  Therefore

\[
p_a''(y)=2\sum_{i<j}(-1)^{1-y_i}(-1)^{1-y_j}
 p_{\bullet\bullet}^{ij}(y_{-ij}).
\tag{7.2}
\]

Substitute (7.2) into

\[
H''=-\sum_y p''(y)\log p(y)-\sum_y\frac{p'(y)^2}{p(y)}.
\]

The four signs on every square face produce the logarithm in (7.1).  The common score (5.7) gives the Fisher term \(n/v\).  \(\square\)

The exact checker proves, as formal rational linear combinations of logarithms of primes, that (7.1), the direct full-atom Hessian, and (6.4) agree for the genuine \(P_{4,2}\) input at \(c=19/20\), and for a separate rational homogeneous input.  The independent audit adds a rigorously non-DPP positive rational case in `evidence/strict_non_dpp_exact.json`.

## 8. What remains unpaid

Put

\[
g_l=(l-m)^2-nv,
\qquad
\mathcal C=\{l:|l-m|<\sqrt{nv}\}.
\]

Equation (6.4) separates the favorable tails from the central negative coefficient.  The exact inequality sufficient for \(\mathcal D''(a_0)\ge0\) is

\[
\boxed{
 v\sum_l\mathscr J_l
\ge
\sum_{l\in\mathcal C}\pi_l[nv-(l-m)^2]F_l
-
\sum_{l\notin\mathcal C}\pi_l[(l-m)^2-nv]F_l.
}
\tag{8.1}
\]

The target only requires the weaker midpoint inequality

\[
\boxed{
\sum_l\pi_lg_lF_l+v\sum_l\mathscr J_l
\ge v^2\Phi''(a_0),
}
\tag{8.2}
\]

because (6.5) would then give \(H''(a_0)\le0\).  The right-hand side of (8.2) is negative, but no uniform proof of (8.1) or (8.2) for growing contiguous Fourier projections is supplied here.

The cancellation in (6.4) is important quantitatively.  On the growing Fourier diagnostics, the count covariance and adjacent production have opposite signs and are individually substantially larger than their remainder.  Proving only \(\mathscr J_l\ge0\), or only a positive within-slice term, is therefore insufficient.

## 9. True contiguous Fourier specialization

For even \(n\), take the genuine contiguous Fourier projection \(P_{n,n/2}\).  Its input law is

\[
\mu(A)=|\det U_A|^2,
\qquad
U_{j,q}=n^{-1/2}e^{2\pi i jq/n},
\quad 0\le q<n/2.
\]

Theorem 6.1 applies for every even \(n\) and every \(0<c<1\), in particular at the requested \(c=19/20\).  For a projection input one may also evaluate

\[
w_l(S)=\det(I+(R-1)P_S)
\tag{9.1}
\]

by Cauchy--Binet, but determinant structure was not needed to prove the theorem.

Floating enumeration for \(c=19/20\) gives the following diagnostics:

| \(n\) | count covariance | \(v\sum\mathscr J_l\) | \(v^2\mathcal D''\) |
|---:|---:|---:|---:|
| 4 | -0.005162477405 | 0.005543609993 | 0.000381132588 |
| 6 | -0.020206373726 | 0.022462828170 | 0.002256454444 |
| 8 | -0.042486842432 | 0.048582922963 | 0.006096080531 |
| 10 | -0.070037912759 | 0.081926364669 | 0.011888451909 |
| 16 | -0.172839981910 | 0.211454089779 | 0.038614107869 |
| 18 | -0.211480226089 | 0.261258228935 | 0.049778002847 |
| 20 | -0.251561598199 | 0.313263503094 | 0.061701904896 |

These are floating diagnostics, not an all-\(n\) sign theorem.  They do show that the new identity is operating on the correct scale and that the actual adjacent production, rather than a within-slice surrogate, pays the observed negative count covariance in the tested family.

A pointwise midpoint identity does not by itself yield a fixed-chord Jensen estimate.  No such integration is claimed.

## 10. Exact obstruction to one formal cancellation mechanism

A secondary proof attempt chose convex weights \(t_l\in[0,1]\) between (4.4) and (4.5), seeking to cancel every coefficient generated by the count covariance before estimating the KL defects.  Let

\[
C_l=-\sum_{j=0}^l\pi_jg_j,
\qquad
\sum_l\pi_lg_l=0.
\]

Layerwise cancellation of the coefficient of \(F_{l+1}-F_l\) would require

\[
C_l+2v[(1-t_{l+1})(n-l)\pi_l-t_l(l+1)\pi_{l+1}]=0.
\tag{10.1}
\]

At \(l=0\), feasibility implies

\[
m^2-nv\le2vn,
\qquad\text{hence}\qquad m^2\le3nv=6mv.
\]

For \(n=2m\ge4\), this would require \(m\le6v\le3/2\), impossible.  Thus no convex layerwise mixture can formally cancel all count coefficients in this manner.

This is only an obstruction to that exact coefficient-cancellation ansatz.  Since \(F_0=0\), and for the equal-diagonal Fourier family also \(F_1=0\), it is not an entropy-scale obstruction to approximate weighted cancellation.  It is not a counterexample to the sine target.

## 11. Verification classes

**Analytically proved in this round**

1. The actual insertion/deletion identity (3.1), marginals (3.4), and response equation (3.5).
2. The two exact directional entropy identities (4.4)--(4.5).
3. The count Stein identity and the complete cancellation theorem (6.4)--(6.6).
4. The full-atom square-face formula (7.1).
5. The scoped formal-mixture obstruction in Section 10.

**Exact finite certificate**

`evidence/author_exact_midpoint.json`, generated by `scripts/exact_midpoint_check.py`, uses rational channel jets and formal prime-log coefficient vectors.  It checks the count Stein identity, the full adjacent theorem, the edge Jeffreys representation, and the square-face/full-atom equality for a genuine \(P_{4,2}\) case and a distinct rational homogeneous case.  `scripts/audit_non_dpp_check.py` supplies the separate Pluecker-certified non-DPP case.  Decimal fields are labelled diagnostics only.

**Floating diagnostics**

The small direct-channel checks and the \(n=16,18,20\) principal-minor enumerations are in `evidence/`.  They test identities and scales only.

**Unproved**

The central payment (8.1), the weaker full-entropy payment (8.2), any open interval of shifts around the midpoint, and the fixed-density sine entropy-rate target.
