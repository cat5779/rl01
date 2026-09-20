# S80 — An actual-law, scale-stable Fisher–Burg payment

## Status

### PROVED

1. **A reusable actual-law payment functional.** For every adjacent equal-block cut and every Jensen tent in the legal bias interval,
   \[
   \left[\int G(a)\bigl(\mathcal B_m(a)-\mathcal I_{\rm rel,m}(a)\bigr)\,da\right]_+
   \le 2S_m^{\rm q}(z)-S_{2m}^{\rm q}(z),
   \]
   where \(z\) is the tent apex and
   \[
   S_n^{\rm q}(a)=\operatorname{tr}h(aI_n+cQ_{\rho,n}),
   \qquad h(t)=-t\log t-(1-t)\log(1-t).
   \]
   The left side uses the **actual finite-block DPP law and actual weights**. The retained Fisher term is not discarded: the integrand is exactly \(\mathcal B-\mathcal I_{\rm rel}=-M''\).

2. **Exact all-scale dyadic payment.** For \(m_k=2^kL\), the quantum upper payments telescope:
   \[
   \sum_{k=0}^{K-1}
   \frac{2S_{m_k}^{\rm q}(z)-S_{2m_k}^{\rm q}(z)}{2m_k}
   =\frac{S_L^{\rm q}(z)}L-\frac{S_{2^KL}^{\rm q}(z)}{2^KL}.
   \]
   Thus every intermediate scale is paid; there is no unverified gap between a seed and a remote cutoff.

3. **An entropy-rate Jensen theorem with an exact finite-seed residual.** If \(H_n(a)\) is the spatial-configuration Shannon entropy of the \(n\)-site DPP compression and
   \[
   \bar H(a)=\lim_{n\to\infty}\frac{H_n(a)}n,
   \]
   then for every compact legal interval \(J\Subset(0,1-c)\), every \(x,y\in J\), every \(0\le\tau\le1\), and \(z=(1-\tau)x+\tau y\),
   \[
   \boxed{
   \bar H(z)-(1-\tau)\bar H(x)-\tau\bar H(y)
   \ge
   \frac{H_L(z)-(1-\tau)H_L(x)-\tau H_L(y)}L
   -R_L^{\rm q}(z)
   }
   \tag{T}
   \]
   for every integer \(L\ge1\), where
   \[
   \boxed{
   R_L^{\rm q}(a)
   =\frac1L\operatorname{tr}h(aI_L+cQ_{\rho,L})
    -\bigl((1-\rho)h(a)+\rho h(a+c)\bigr).
   }
   \tag{R}
   \]
   This is an entropy-value limit, not differentiation of an \(o(n)\) term.

4. **Explicit uniform residual.** Put
   \[
   \Lambda_J=
   \sup_{a\in J,\,0\le t\le1}
   \frac1{(a+ct)(1-a-ct)}<\infty,
   \qquad
   D_{\rho,L}=\operatorname{tr}(Q_{\rho,L}-Q_{\rho,L}^2).
   \]
   Then
   \[
   0\le R_L^{\rm q}(a)
   \le \frac{\Lambda_Jc^2}{2L}D_{\rho,L}
   \quad(a\in J).
   \tag{U}
   \]
   For the sine projection,
   \[
   D_{\rho,n}
   =\frac2{\pi^2}\sum_{r=1}^{n-1}\frac{\sin^2(\pi\rho r)}r
    +\frac{2n}{\pi^2}\sum_{r=n}^{\infty}\frac{\sin^2(\pi\rho r)}{r^2}
   \le \frac2{\pi^2}(\log n+3),
   \tag{D}
   \]
   so the residual is \(O_{J,c}(\log L/L)\).

5. **A complementary actual-word boundary lemma.** For a general finite Hermitian contraction with a uniform spectral gap, the cut log-likelihood and its first two bias derivatives are bounded by the Hilbert–Schmidt mass across the cut, with no volume factor. This isolates the unresolved pointwise term after the exact Fisher payment.

### DISPROVED AS PROOF ROUTES

1. An unweighted pair-by-pair allocation of the full one-coordinate entropy curvature cannot be scale stable: already for a product Bernoulli law it spends the same coordinate curvature in each of the \(n-1\) pairs containing that coordinate, while all mixed rectangle charges are zero.

2. A pointwise value domination \(0\le M(a)\le I^{\rm q}(a)\) cannot by itself imply a local second-derivative domination. Uniformly bounded nonnegative smooth functions can have arbitrarily negative second derivative. The proof below therefore uses a Jensen tent and reports exactly where the missing tent-area factor is lost.

These reject proof mechanisms, not the sine-kernel concavity target.

### INCOMPLETE

The theorem does **not** prove \(\mathcal B_+\le\mathcal I_{\rm rel}\), does not produce a pointwise residual \(e_m(J)\), and does not prove local or full-interval concavity of \(\bar H\). Its residual \(R_L^{\rm q}\) has no factor proportional to the Jensen tent area
\[
\frac12\tau(1-\tau)(y-x)^2.
\]
Consequently (T) is directly useful for certified nondegenerate chords, but dividing it by the tent area as \(y\to x\) is invalid. The remaining obligation is an area-sensitive bound on the actual signed acceleration term described in Section 8.

---

## 1. Setup and the payment functional

Fix \(0<\rho,c<1\). For a finite interval of length \(n\), write
\[
K_n(a)=aI_n+cQ_{\rho,n},\qquad 0<a<1-c.
\]
For adjacent equal blocks \(A,B\), each of length \(m\), let
\[
M_m(a)=H_A(a)+H_B(a)-H_{AB}(a)=2H_m(a)-H_{2m}(a).
\]
The audited actual-law identity is
\[
M_m''(a)=\mathcal I_{\rm rel,m}(a)-\mathcal B_m(a).
\tag{1.1}
\]

For \(x<y\), \(0\le\tau\le1\), and
\[
z=(1-\tau)x+\tau y,
\]
define the Green tent
\[
G_{x,z,y}(t)=
\begin{cases}
\displaystyle\frac{(t-x)(y-z)}{y-x},&x\le t\le z,\\[6pt]
\displaystyle\frac{(z-x)(y-t)}{y-x},&z\le t\le y.
\end{cases}
\tag{1.2}
\]
For every \(C^2\) function \(f\),
\[
f(z)-(1-\tau)f(x)-\tau f(y)
=-\int_x^yG_{x,z,y}(t)f''(t)\,dt.
\tag{1.3}
\]
Its area is
\[
\int_x^yG_{x,z,y}(t)\,dt
=\frac12\tau(1-\tau)(y-x)^2.
\tag{1.4}
\]

Define the **actual Fisher–Burg Jensen charge**
\[
\mathfrak C_m[x,z,y]
:=\int_x^yG_{x,z,y}(a)
\bigl(\mathcal B_m(a)-\mathcal I_{\rm rel,m}(a)\bigr)\,da.
\tag{1.5}
\]
By (1.1) and (1.3), this is not a new formal identity replacing the old unknown: it is exactly the cut mutual-information Jensen gap,
\[
\mathfrak C_m[x,z,y]
=M_m(z)-(1-\tau)M_m(x)-\tau M_m(y).
\tag{1.6}
\]
Since mutual information is nonnegative,
\[
[\mathfrak C_m[x,z,y]]_+\le M_m(z).
\tag{1.7}
\]
The rest of the argument gives a boundary-sized, exactly telescoping upper certificate for the right side.

---

## 2. Finite quasi-free certificate for the actual cut law

This section uses only finite-dimensional objects.

Let \(K\) be a strict Hermitian contraction on a finite set. The gauge-invariant quasi-free density matrix with one-particle correlation \(K\) may be written, after diagonalizing \(K\), as a tensor product of one-mode states with occupations equal to the eigenvalues of \(K\). Its von Neumann entropy is therefore
\[
S(\Gamma_K)=\operatorname{tr}h(K).
\tag{2.1}
\]
Restriction to a coordinate subset \(A\) is again gauge-invariant quasi-free with correlation matrix \(K_A\), hence
\[
S((\Gamma_K)_A)=\operatorname{tr}h(K_A).
\tag{2.2}
\]

Measuring all coordinate occupation projectors produces the determinantal point-process law with kernel \(K\). One finite verification is obtained from the generating function
\[
\mathbb E_K\prod_i z_i^{Y_i}
=\det(I-K+KZ),
\qquad Z=\operatorname{diag}(z_i),
\tag{2.3}
\]
which is both the occupation generating function of \(\Gamma_K\) and the defining finite-DPP generating function. Under the bipartition \(A\cup B\), the product state
\[
\Gamma_{K_A}\otimes\Gamma_{K_B}
\]
measures to the product of the two actual marginal DPP laws.

Let \(\Delta\) be dephasing in the joint occupation basis. Monotonicity of finite-dimensional quantum relative entropy under the completely positive trace-preserving map \(\Delta\) gives
\[
\begin{aligned}
M(A:B)_{\rm classical}
&=D\!\left(\Delta\Gamma_K\,\big\|\,
 \Delta(\Gamma_{K_A}\otimes\Gamma_{K_B})\right)\\
&\le D\!\left(\Gamma_K\,\big\|\,
 \Gamma_{K_A}\otimes\Gamma_{K_B}\right)\\
&=\operatorname{tr}h(K_A)+\operatorname{tr}h(K_B)-\operatorname{tr}h(K).
\end{aligned}
\tag{2.4}
\]
All hypotheses are met by the actual finite DPP. No claim is made that the auxiliary bridge \((1-t)q+tp\) is determinantal, and no negative-association assertion is applied to it.

For the adjacent equal blocks of the Toeplitz compression, (2.4) becomes
\[
M_m(a)\le I_m^{\rm q}(a)
:=2S_m^{\rm q}(a)-S_{2m}^{\rm q}(a),
\tag{2.5}
\]
where
\[
S_n^{\rm q}(a)=\operatorname{tr}h(aI_n+cQ_{\rho,n}).
\tag{2.6}
\]
Combining (1.7) and (2.5) proves the promised actual-law payment:
\[
\boxed{
[\mathfrak C_m[x,z,y]]_+
\le I_m^{\rm q}(z)
=2S_m^{\rm q}(z)-S_{2m}^{\rm q}(z).
}
\tag{2.7}
\]

This is a signed grouping of the complete rectangle charge: all actual words and all pairs already present in \(\mathcal B_m\) remain inside (1.5), and the actual Fisher payment remains with them.

---

## 3. Boundary-size estimate for one quantum cut

Write the \(2m\)-site kernel at fixed \(a\) as
\[
K=\begin{pmatrix}K_A&C\\C^*&K_B\end{pmatrix},
\qquad
K_0=K_A\oplus K_B,
\qquad
E=K-K_0=
\begin{pmatrix}0&C\\C^*&0\end{pmatrix}.
\tag{3.1}
\]
Here \(C=c(Q_{\rho,2m})_{A,B}\). The first variation of the trace spectral function \(\operatorname{tr}h\) at the block-diagonal point in the off-diagonal direction vanishes:
\[
D\operatorname{tr}h(K_0)[E]
=\operatorname{tr}(h'(K_0)E)=0.
\tag{3.2}
\]
For a Hermitian matrix \(X\) whose spectrum lies in the interval
\[
\{a+ct:a\in J,\ 0\le t\le1\},
\]
the divided-difference formula for the Hessian of a trace spectral function yields
\[
-D^2\operatorname{tr}h(X)[E,E]
\le \Lambda_J\|E\|_{\rm HS}^2,
\tag{3.3}
\]
because
\[
-h''(u)=\frac1{u(1-u)}\le\Lambda_J
\]
and every first divided difference of \(h'\) lies between values of \(h''\) on the spectral interval. The segment \(K_0+sE\), \(0\le s\le1\), stays in that operator interval because both endpoints do.

Taylor's formula, (3.2), (3.3), and
\[
\|E\|_{\rm HS}^2=2\|C\|_{\rm HS}^2
\]
give
\[
\begin{aligned}
I_m^{\rm q}(a)
&=\operatorname{tr}h(K_0)-\operatorname{tr}h(K_0+E)\\
&\le\frac{\Lambda_J}{2}\|E\|_{\rm HS}^2
=\Lambda_J\|C\|_{\rm HS}^2.
\end{aligned}
\tag{3.4}
\]
Thus
\[
I_m^{\rm q}(a)
\le\Lambda_Jc^2\|(Q_{\rho,2m})_{A,B}\|_{\rm HS}^2.
\tag{3.5}
\]

For adjacent equal Toeplitz blocks, expanding \(\operatorname{tr}Q_{\rho,2m}^2\) by blocks gives the exact relation
\[
\|(Q_{\rho,2m})_{A,B}\|_{\rm HS}^2
=D_{\rho,m}-\frac12D_{\rho,2m}.
\tag{3.6}
\]
Therefore
\[
\boxed{
I_m^{\rm q}(a)
\le\Lambda_Jc^2
\left(D_{\rho,m}-\frac12D_{\rho,2m}\right).
}
\tag{3.7}
\]
This is already summable with the exact dyadic weights.

---

## 4. Exact dyadic recursion and entropy-rate theorem

For the Shannon block entropies,
\[
H_{2m}=2H_m-M_m.
\tag{4.1}
\]
Let
\[
\mathcal J_f(x,y;\tau)
=f(z)-(1-\tau)f(x)-\tau f(y).
\tag{4.2}
\]
Applying this linear functional to (4.1) gives
\[
\mathcal J_{H_{2m}}
=2\mathcal J_{H_m}-\mathcal J_{M_m}.
\tag{4.3}
\]
By (2.7),
\[
\mathcal J_{M_m}\le I_m^{\rm q}(z).
\tag{4.4}
\]
Consequently
\[
\frac{\mathcal J_{H_{2m}}}{2m}
\ge
\frac{\mathcal J_{H_m}}m
-\frac{I_m^{\rm q}(z)}{2m}.
\tag{4.5}
\]

Set \(m_k=2^kL\) and \(N=2^KL\). Iteration through **every** level gives
\[
\frac{\mathcal J_{H_N}}N
\ge
\frac{\mathcal J_{H_L}}L
-\sum_{k=0}^{K-1}\frac{I_{m_k}^{\rm q}(z)}{2m_k}.
\tag{4.6}
\]
The sum is exact because
\[
\frac{I_m^{\rm q}(z)}{2m}
=\frac{S_m^{\rm q}(z)}m-
 \frac{S_{2m}^{\rm q}(z)}{2m}.
\tag{4.7}
\]
Hence
\[
\sum_{k=0}^{K-1}\frac{I_{m_k}^{\rm q}(z)}{2m_k}
=\frac{S_L^{\rm q}(z)}L-\frac{S_N^{\rm q}(z)}N.
\tag{4.8}
\]
No large \(K\) is selected while intermediate scales are silently assumed.

The stationary Shannon entropy rate exists by block-entropy subadditivity. Section 5 proves
\[
\lim_{N\to\infty}\frac{S_N^{\rm q}(a)}N
=(1-\rho)h(a)+\rho h(a+c).
\tag{4.9}
\]
Taking the value limit in (4.6) along \(N=2^KL\) proves (T) and (R).

A convenient certified-seed corollary is the following. If on the whole chord \([x,y]\)
\[
-H_L''(a)\ge f_L,
\tag{4.10}
\]
then (1.3), (1.4), and (T) give
\[
\mathcal J_{\bar H}(x,y;\tau)
\ge
\frac{f_L}{2L}\tau(1-\tau)(y-x)^2
-R_L^{\rm q}(z).
\tag{4.11}
\]
For a fixed nondegenerate chord, a rigorous finite-block certificate satisfying
\[
\mathcal J_{H_L}(x,y;\tau)\ge L R_L^{\rm q}(z)
\tag{4.12}
\]
closes that rate chord, with all larger dyadic scales already paid.

For interval-uniform use, define
\[
R_L^{\rm q}(J)=\sup_{a\in J}R_L^{\rm q}(a).
\tag{4.13}
\]
Then (T) remains valid with \(R_L^{\rm q}(z)\) replaced by \(R_L^{\rm q}(J)\), and (U) supplies an explicit bound.

---

## 5. Exact sine-kernel residual and its decay

Let \(q_1,\dots,q_n\in[0,1]\) be the eigenvalues of \(Q_{\rho,n}\). Since
\[
\sum_{j=1}^nq_j=\operatorname{tr}Q_{\rho,n}=\rho n,
\tag{5.1}
\]
write
\[
\begin{aligned}
\frac{S_n^{\rm q}(a)}n
&=(1-\rho)h(a)+\rho h(a+c)
  +\frac1n\sum_{j=1}^n r_a(q_j),\\
r_a(q)
&=h(a+cq)-(1-q)h(a)-qh(a+c).
\end{aligned}
\tag{5.2}
\]
Concavity of \(h\) gives \(r_a(q)\ge0\). Also
\[
-\frac{d^2}{dq^2}h(a+cq)
=\frac{c^2}{(a+cq)(1-a-cq)}
\le\Lambda_Jc^2.
\tag{5.3}
\]
The function \(r_a\) vanishes at \(q=0,1\). Comparing it with the parabola
\[
\frac{\Lambda_Jc^2}{2}q(1-q)
\]
therefore gives
\[
0\le r_a(q)\le\frac{\Lambda_Jc^2}{2}q(1-q).
\tag{5.4}
\]
Summation proves
\[
0\le R_n^{\rm q}(a)
\le\frac{\Lambda_Jc^2}{2n}
\sum_{j=1}^nq_j(1-q_j)
=\frac{\Lambda_Jc^2}{2n}D_{\rho,n},
\tag{5.5}
\]
which is (U).

For the sine kernel, put
\[
q_r=\begin{cases}
\rho,&r=0,\\[2pt]
\displaystyle\frac{\sin(\pi\rho r)}{\pi r},&r\ne0.
\end{cases}
\]
The infinite operator is a projection, so
\[
\sum_{r\in\mathbb Z}|q_r|^2=\rho.
\tag{5.6}
\]
Expanding the finite trace defect gives
\[
\begin{aligned}
D_{\rho,n}
&=n\rho-\sum_{|r|<n}(n-|r|)|q_r|^2\\
&=\sum_{0<|r|<n}|r||q_r|^2
  +n\sum_{|r|\ge n}|q_r|^2,
\end{aligned}
\tag{5.7}
\]
which is exactly (D). Finally,
\[
\sum_{r=1}^{n-1}\frac1r\le\log n+1,
\qquad
n\sum_{r=n}^{\infty}\frac1{r^2}\le2
\tag{5.8}
\]
proves the displayed logarithmic upper bound. Equations (5.5)–(5.8) imply (4.9).

There is also an exact telescoping version of the coarse defect bound:
\[
\sum_{k=0}^{K-1}
\frac{\Lambda_Jc^2\bigl(D_{\rho,m_k}-D_{\rho,2m_k}/2\bigr)}{2m_k}
=\frac{\Lambda_Jc^2}{2}
\left(\frac{D_{\rho,L}}L-\frac{D_{\rho,N}}N\right).
\tag{5.9}
\]
Its infinite-level cost is exactly \(\Lambda_Jc^2D_{\rho,L}/(2L)\), agreeing with (5.5).

---

## 6. Actual-word determinant interaction lemma

This lemma is independent of the quantum comparison and records a second reusable tool for the unresolved local problem.

Let a finite Hermitian kernel satisfy
\[
\delta I\le K(a)\le(1-\delta)I
\tag{6.1}
\]
through an interval, and partition its coordinates into \(A,B\). Put
\[
K_0=K_A\oplus K_B,
\qquad
E=K-K_0=
\begin{pmatrix}0&C\\C^*&0\end{pmatrix}.
\tag{6.2}
\]
Assume the common bias shift is \(\partial_aK=I\), so \(E\) is independent of \(a\).

For a word \(y\in\{0,1\}^n\), let \(Z=\{i:y_i=0\}\), \(P_Z\) be its diagonal projection, and
\[
G_y=K-P_Z.
\tag{6.3}
\]
The exact atom formula is
\[
p_K(y)=(-1)^{|Z|}\det G_y.
\tag{6.4}
\]
Let \(J_y=\operatorname{diag}(2y_i-1)\). In the order \(Z^c,Z\),
\[
\frac{J_yG_y+(J_yG_y)^*}{2}
=K_{Z^c,Z^c}\oplus(I-K_{Z,Z})
\ge\delta I.
\tag{6.5}
\]
Hence
\[
\|G_y^{-1}\|_{\rm op}\le\delta^{-1}
\tag{6.6}
\]
for every actual word. The same holds along
\[
K_s=K_0+sE,\qquad0\le s\le1,
\tag{6.7}
\]
because this segment retains the gap.

Let \(p\) be the actual joint atom law and \(q=p_Ap_B\), which is the atom law of \(K_0\). Then
\[
\ell_y=\log\frac{p_y}{q_y}
=\log|\det(G_{0,y}+E)|-\log|\det G_{0,y}|.
\tag{6.8}
\]
The first \(s\)-variation at \(s=0\) vanishes because a block-diagonal inverse times the block-off-diagonal \(E\) has trace zero. Taylor's formula and (6.6) yield
\[
|\ell_y|\le\delta^{-2}\|C\|_{\rm HS}^2.
\tag{6.9}
\]

More generally, for \(r\ge1\) put
\[
F_r(s)=\operatorname{tr}(G_{s,y}^{-r}).
\]
Then \(F_r'(0)=0\), and differentiation plus the Hilbert–Schmidt trace inequality gives
\[
|F_r''(s)|
\le r(r+1)\delta^{-(r+2)}\|E\|_{\rm HS}^2.
\tag{6.10}
\]
Since \(\|E\|_{\rm HS}^2=2\|C\|_{\rm HS}^2\), Taylor's formula gives
\[
|F_r(1)-F_r(0)|
\le r(r+1)\delta^{-(r+2)}\|C\|_{\rm HS}^2.
\tag{6.11}
\]
Using
\[
\partial_a^r\log|\det G|
=(-1)^{r-1}(r-1)!\operatorname{tr}(G^{-r}),
\]
we obtain, for every \(r\ge1\),
\[
\boxed{
|\partial_a^r\ell_y|
\le(r-1)!\,r(r+1)\,
\delta^{-(r+2)}\|C\|_{\rm HS}^2.
}
\tag{6.12}
\]
In particular,
\[
|\ell_y'|\le2\delta^{-3}\|C\|_{\rm HS}^2,
\qquad
|\ell_y''|\le6\delta^{-4}\|C\|_{\rm HS}^2.
\tag{6.13}
\]
The useful gain here is not the bare inverse estimate: it is the exact disappearance of the cut interaction's first block-off-diagonal variation, which leaves boundary Hilbert–Schmidt mass rather than volume.

---

## 7. What the determinant lemma pays in the audited decomposition

Let
\[
S=\partial_a\log p,
\quad
S_A=\partial_a\log p_A,
\quad
S_B=\partial_a\log p_B,
\quad
R=S-S_A-S_B=\ell'.
\tag{7.1}
\]
The marginal score identities give
\[
\mathbb E_p[S\mid Y_A]=S_A,
\qquad
\mathbb E_p[S\mid Y_B]=S_B.
\tag{7.2}
\]
A direct expansion therefore gives
\[
\mathcal I_{\rm rel}
=\mathbb E_pR^2
=\mathbb E_pS^2-
 \mathbb E_pS_A^2-
 \mathbb E_pS_B^2+
 2\mathbb E_p[S_AS_B].
\tag{7.3}
\]
The audited Fisher block is
\[
D_F=\mathcal I_{\rm rel}-2\mathbb E_p[S_AS_B]
=\mathbb E_pS^2-
 \mathbb E_pS_A^2-
 \mathbb E_pS_B^2.
\tag{7.4}
\]
On the other hand, differentiating \(\ell=\log p-\log q\), using normalization of the joint and marginal laws, gives the exact identity
\[
\boxed{D_F=-\mathbb E_p\ell''.}
\tag{7.5}
\]
For the actual DPP, the inherited score covariance satisfies \(\mathbb E_p[S_AS_B]\le0\), so \(D_F\ge0\). Equations (6.12)–(6.13) then imply
\[
0\le D_F\le6\delta^{-4}\|C\|_{\rm HS}^2,
\tag{7.6}
\]
and
\[
\mathcal I_{\rm rel}=\mathbb E_p(\ell')^2
\le4\delta^{-6}\|C\|_{\rm HS}^4.
\tag{7.7}
\]
The latter has the correct quartic interaction scale when one cross entry is weak.

Differentiating the relative entropy itself gives
\[
M''=D_F+\sum_y p_y''\ell_y.
\tag{7.8}
\]
Consequently the audited acceleration remainder is exactly
\[
\boxed{C_{\rm acc}=\sum_y p_y''\ell_y.}
\tag{7.9}
\]
This identifies the local quantity still requiring a signed, scale-stable estimate. Bounding \(|\ell_y|\) and \(\sum_y|p_y''|\) separately would restore a volume-squared loss and is not used here.

---

## 8. Exact remaining deficit

The Jensen theorem pays the integrated local obstruction:
\[
\int G(\mathcal B-\mathcal I_{\rm rel})
=-\int GM''.
\]
It loses local information only at
\[
[\mathcal J_{M_m}]_+\le M_m(z),
\tag{8.1}
\]
which contains no tent-area factor. Since the area is (1.4), the bound obtained by division behaves like
\[
\frac{R_L^{\rm q}(z)}{\tau(1-\tau)(y-x)^2}
\]
and diverges as the chord collapses.

Thus the exact unresolved local obligation can be stated as follows: control
\[
\sum_y p_y''(a)\ell_y(a)
\tag{8.2}
\]
after retaining the paid Fisher block
\[
D_F=-\mathbb E_p\ell'',
\tag{8.3}
\]
by a boundary interaction expression whose dyadic weighted sum is finite and whose integrated form carries the tent area. The determinant lemma proves boundary-size control of \(\ell,\ell',\ell''\), but not the necessary cancellation in (8.2).

For the entropy-rate theorem proved here, the remaining chord deficit is exactly
\[
\boxed{
\Delta_L(x,y;\tau)
=R_L^{\rm q}(z)
-\frac{\mathcal J_{H_L}(x,y;\tau)}L.
}
\tag{8.4}
\]
A nonpositive rigorous enclosure of \(\Delta_L\) proves that chord. No unscanned merge levels remain after this seed comparison.

---

## 9. Half-density calculation and execution status

At \(\rho=1/2\), only odd Fourier separations contribute. Formula (D) gives, exactly,
\[
D_{1/2,6}
=\frac32-\frac{806}{75\pi^2}.
\tag{9.1}
\]
At \(c=0.95=19/20\) and \(a=0.025=1/40\), the pointwise scalar Hessian constant is
\[
\Lambda=\frac1{a(1-a)}=\frac{1600}{39}.
\]
The conservative all-scale residual bound at seed \(L=6\) is therefore
\[
R_6^{\rm q}(a)
\le
\frac{\Lambda c^2}{12}D_{1/2,6}
=\frac{361}{117}
\left(\frac32-\frac{806}{75\pi^2}\right),
\tag{9.2}
\]
which is about \(1.27\) nats per site. This is a rigorous symbolic bound; the decimal is only its ordinary numerical evaluation.

For the compact interval
\[
J=[0.02,0.03],
\]
\[
\Lambda_J=\frac1{0.02\cdot0.98}=\frac{2500}{49},
\]
and the corresponding symbolic uniform bound is
\[
R_6^{\rm q}(J)
\le
\frac{9025}{2352}
\left(\frac32-\frac{806}{75\pi^2}\right),
\tag{9.3}
\]
about \(1.58\) nats per site.

A double-precision eigenvalue evaluation of the **exact** residual formula (R), executed during this research, gave
\[
R_6^{\rm q}(0.025)\approx0.173606
\quad\text{nats per site}.
\tag{9.4}
\]
This is a floating-point diagnostic, not an interval certificate. It is not inferred from the stated six-site certificate for the different quantity \(M''\), and it does not by itself establish any chord or interval sign.

No repository was mutated, no PR was merged, and no external worker or auxiliary agent was used.

---

## 10. Proof dependencies and legal interface

The proved theorem depends on:

* the audited identity \(M''=\mathcal I_{\rm rel}-\mathcal B\);
* finite-dimensional relative-entropy data processing under occupation dephasing;
* the finite quasi-free entropy formula \(S(\Gamma_K)=\operatorname{tr}h(K)\), verified under the strict-contraction hypothesis present here;
* block entropy recursion and stationary entropy-rate existence;
* the sine projection identity used in (5.6).

It does **not** depend on:

* treating a finite Toeplitz compression as a projection;
* identifying Shannon count/configuration entropy with trace binary entropy;
* negative association of the non-DPP bridge \((1-t)q+tp\);
* discarding rare words;
* replacing actual conditional laws by independent surrogates;
* extrapolating a finite floating-point scan to all scales.

The legal interface is:

* **Input:** fixed \(\rho,c\), compact \(J\Subset(0,1-c)\), a seed length \(L\), and either a rigorously enclosed seed Jensen gap or a certified lower bound for \(-H_L''\) on a chord;
* **All-scale output:** inequality (T), with exact residual (R) or uniform explicit residual (U);
* **Scale coverage:** all dyadic levels from \(L\) to infinity, paid by the exact telescope (4.8);
* **Remaining requirement for a chord:** prove \(\Delta_L\le0\);
* **Remaining requirement for local/full interval concavity:** replace (8.1) by an area-sensitive actual-law comparison, equivalently obtain a summable pointwise curvature residual.

