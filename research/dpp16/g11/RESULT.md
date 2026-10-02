DISPROVED

The bound fails for the actual least-norm selector, already when the two kernels are equal to a fixed scalar matrix \(pI\). The counterexample below has
\[
\frac{\|\Phi_{E_n}(K_n,P_n)-\Phi_{E_n}(K_n,Q_n)\|_1}
{\|P_n-Q_n\|_1}
\ge
\frac{1-2\varepsilon}{16\sqrt2}\sqrt n,
\qquad n\ge4.
\tag{1}
\]
Both selected flows will be computed exactly. All their nonnegativity and capacity inequalities are strict.

## 1. The admissible pairs

Fix \(\varepsilon\in(0,1/2)\), and set
\[
p=\frac{1+2\varepsilon}{4}.
\]
Then
\[
\varepsilon<p<\frac12<1-\varepsilon.
\]

For every \(n\ge4\), take
\[
E_n=\{1,\ldots,n\},\qquad K_n=L_n=pI_n,
\qquad \tau_n=\frac{p^n}{n}.
\]
Define real unit vectors
\[
v_n=\frac1{\sqrt n}(1,\ldots,1),
\]
\[
w_n=
\left(
\sqrt{\frac1n+\tau_n},
\sqrt{\frac1n-\tau_n},
\frac1{\sqrt n},\ldots,\frac1{\sqrt n}
\right),
\]
and rank-one projectors
\[
P_n=v_nv_n^*,\qquad Q_n=w_nw_n^*.
\tag{2}
\]
Since \(0<\tau_n<1/n\), both projectors have full support. The kernels are uniformly, strictly \(\varepsilon\)-gapped.

We identify configurations with \(x\in\{0,1\}^n\), and write
\[
\mu_p(x)=p^{|x|}(1-p)^{n-|x|}.
\]

## 2. The DPP derivative at a scalar kernel

The exact-pattern identity is
\[
p_K(S)=(-1)^{|E\setminus S|}
\det\!\left(K-\operatorname{diag}(\mathbf1_{E\setminus S})\right).
\tag{3}
\]
It follows from the defining determinantal inclusion probabilities and inclusion–exclusion.

At \(K=pI\), the matrix inside this determinant is diagonal and invertible. Differentiating its determinant shows that, for any rank-one projector \(R\),
\[
b_{pI,R}(x)
=
\mu_p(x)\sum_{i=1}^n R_{ii}
\left(\frac{x_i}{p}-\frac{1-x_i}{1-p}\right).
\tag{4}
\]
In particular, the derivative at this scalar kernel depends only on the diagonal of \(R\).

Let
\[
\eta(x_1,x_2)=x_1-x_2,\qquad
y=(x_3,\ldots,x_n),
\]
and, on these last \(m=n-2\) coordinates, put
\[
\rho_q(y)=q^{|y|}(1-q)^{m-|y|}.
\]
The diagonal difference in (2) is
\[
\operatorname{diag}(Q_n-P_n)
=(\tau_n,-\tau_n,0,\ldots,0).
\]
Consequently, (4) gives the exact identity
\[
\boxed{
b_{pI,Q_n}(x)-b_{pI,P_n}(x)
=\tau_n\,\eta(x_1,x_2)\rho_p(y).
}
\tag{5}
\]
Indeed, when \(x_1\ne x_2\), the first two coordinates contribute the factor \(p(1-p)\) to \(\mu_p(x)\), which cancels the factor \(1/[p(1-p)]\) in the difference of the two scores. When \(x_1=x_2\), both sides vanish.

## 3. A feasible gradient is the actual least-norm flow

For a vertex function \(u\), define its upward edge gradient by
\[
\nabla u(x,i)=u(x+e_i)-u(x),
\qquad x_i=0.
\]
With the divergence convention in the question,
\[
\operatorname{div}\nabla u(x)
=\sum_{i=1}^n\bigl(u(x)-u(x^{(i)})\bigr)
=:\mathcal L_nu(x),
\tag{6}
\]
where \(x^{(i)}\) is obtained by flipping coordinate \(i\).

Suppose a gradient flow \(F=\nabla u\) is feasible for a given fiber. For any other flow \(H\) in that fiber,
\[
\operatorname{div}(H-F)=0.
\]
Summation by parts gives
\[
\langle F,H-F\rangle
=
\sum_x u(x)\operatorname{div}(H-F)(x)=0.
\]
Therefore
\[
\|H\|_2^2=\|F\|_2^2+\|H-F\|_2^2.
\tag{7}
\]
Thus \(F\) is the unique least-Euclidean-norm point of the full fiber.

We will construct feasible gradients for both inputs in (2). Equation (7) then identifies them with \(\Phi\), without any assumption about which active sets an optimizer might realize.

## 4. The baseline least-norm flow

Define
\[
F_n^0(x,i)
=
\frac1n p^{|x|}(1-p)^{n-1-|x|},
\qquad x_i=0.
\tag{8}
\]
Its divergence is
\[
\begin{aligned}
\operatorname{div}F_n^0(x)
&=
\frac{|x|}{n}p^{|x|-1}(1-p)^{n-|x|}\\
&\quad-
\frac{n-|x|}{n}p^{|x|}(1-p)^{n-1-|x|}\\
&=b_{pI,P_n}(x),
\end{aligned}
\tag{9}
\]
using (4).

For each direction \(i\), the sum of its edge values is \(1/n\), so \(F_n^0\) has total mass one. It is positive, and
\[
(F_n^0)_{\rm out}(x)
=
\frac{n-|x|}{n(1-p)}\mu_p(x)
\le \frac1{1-p}\mu_p(x).
\tag{10}
\]

It is also a gradient. Define
\[
\psi_n(k)=
\frac1n\sum_{r=0}^{k-1}p^r(1-p)^{n-1-r},
\qquad \psi_n(0)=0.
\]
Then
\[
F_n^0=\nabla\bigl(\psi_n(|x|)\bigr).
\]
Since \(1/(1-p)<2<2/\varepsilon\), this flow is feasible, and (7) proves
\[
\boxed{\Phi_{E_n}(pI,P_n)=F_n^0.}
\tag{11}
\]

## 5. An exact gradient correction with growing \(\ell^1\) norm

For \(t\in[0,1]\), set
\[
q(t)=\frac12+\left(p-\frac12\right)t,
\]
and define the vertex potential
\[
u_n(x)
=
\frac{\eta(x_1,x_2)}2
\int_0^1\rho_{q(t)}(y)\,dt.
\tag{12}
\]
Let
\[
G_n=\nabla u_n.
\]

### Exact divergence

On the first two coordinates,
\[
\mathcal L_2\eta=2\eta.
\]
On the last \(m\) coordinates, direct differentiation of the product probability gives
\[
\mathcal L_m\rho_q
=(2q-1)\,\partial_q\rho_q.
\]
Because \(2q(t)-1=2tq'(t)\), this becomes
\[
\mathcal L_m\rho_{q(t)}
=2t\,\frac d{dt}\rho_{q(t)}.
\]
Applying the full Laplacian to (12) and integrating by parts,
\[
\begin{aligned}
\mathcal L_nu_n(x)
&=
\frac{\eta}{2}\int_0^1
\left(2\rho_{q(t)}+\mathcal L_m\rho_{q(t)}\right)dt\\
&=
\eta\int_0^1
\left(\rho_{q(t)}
+t\frac d{dt}\rho_{q(t)}\right)dt\\
&=
\eta\,[t\rho_{q(t)}]_{t=0}^{t=1}\\
&=
\eta\rho_p(y).
\end{aligned}
\]
Thus
\[
\boxed{\operatorname{div}G_n(x)=\eta(x_1,x_2)\rho_p(y).}
\tag{13}
\]

### Edge formulas and exact norm

Put
\[
A(y)=\frac12\int_0^1\rho_{q(t)}(y)\,dt.
\]
The edges in the first two directions are
\[
G_n(x,1)=A(y)\quad(x_1=0),
\qquad
G_n(x,2)=-A(y)\quad(x_2=0).
\tag{14}
\]
For \(j\ge3\), write
\[
\rho_q^{(-j)}(x)
=
\prod_{\substack{\ell=3\\\ell\ne j}}^n
q^{x_\ell}(1-q)^{1-x_\ell}.
\]
Then
\[
G_n(x,j)
=
\frac{(2p-1)\eta(x_1,x_2)}2
\int_0^1 t\,\rho_{q(t)}^{(-j)}(x)\,dt,
\qquad x_j=0.
\tag{15}
\]

All integrands are nonnegative. Summing absolute values in direction \(1\), the two choices of \(x_2\) give
\[
\sum_{x:x_1=0}|G_n(x,1)|
=
2\cdot\frac12\int_0^1\sum_y\rho_{q(t)}(y)\,dt
=1.
\]
Direction \(2\) contributes another \(1\).

For any \(j\ge3\), the sum of \(|\eta|\) over the first two coordinates is \(2\). Summing (15) over the remaining coordinates therefore gives
\[
\begin{aligned}
\sum_{x:x_j=0}|G_n(x,j)|
&=
\frac{1-2p}{2}\cdot2\int_0^1t\,dt\\
&=\frac{1-2p}{2}.
\end{aligned}
\]
Consequently,
\[
\boxed{
\|G_n\|_1
=
2+\frac{n-2}{2}(1-2p).
}
\tag{16}
\]

The signed edge sums in directions \(1,2\) are respectively \(1,-1\); in every other direction the sum is zero, because the two nonzero values of \(\eta\) cancel. Hence
\[
\sum_{x,i:x_i=0}G_n(x,i)=0.
\tag{17}
\]

Finally, the formulas give the pointwise bound
\[
\boxed{|G_n(x,i)|\le\frac12.}
\tag{18}
\]
For the first two directions this follows from \(A(y)\le1/2\). For the remaining directions the sharper bound \((1-2p)/4\le1/4\) follows from (15).

## 6. The perturbed flow is feasible and is exactly what \(\Phi\) selects

Set
\[
F_n^1=F_n^0+\tau_nG_n.
\tag{19}
\]
Equations (5), (9), and (13) show that
\[
\operatorname{div}F_n^1=b_{pI,Q_n}.
\]
Equations (17) and the baseline normalization show that \(F_n^1\) has total mass one.

We check both inequalities of the original fiber explicitly.

### Nonnegativity

Since \(p<1/2\), every factor in (8) is at least \(p\), so
\[
F_n^0(x,i)\ge\frac{p^{n-1}}n.
\]
Using \(\tau_n=p^n/n\) and (18),
\[
\begin{aligned}
F_n^1(x,i)
&\ge\frac{p^{n-1}}n-\frac{\tau_n}{2}\\
&=\frac{p^{n-1}}n\left(1-\frac p2\right)>0.
\end{aligned}
\tag{20}
\]

### Outgoing capacity

Every configuration satisfies \(\mu_p(x)\ge p^n\). By (10) and (18),
\[
\begin{aligned}
(F_n^1)_{\rm out}(x)
&\le \frac1{1-p}\mu_p(x)+\tau_n\frac n2\\
&=\frac1{1-p}\mu_p(x)+\frac{p^n}{2}\\
&\le\left(\frac1{1-p}+\frac12\right)\mu_p(x)\\
&<\frac52\mu_p(x)
<\frac2\varepsilon\mu_p(x).
\end{aligned}
\tag{21}
\]
The last inequality uses \(\varepsilon<1/2\).

Thus \(F_n^1\) belongs to the full original fiber, with strict nonnegativity and strict outgoing-capacity inequalities. It is the gradient of
\[
\psi_n(|x|)+\tau_nu_n(x).
\]
The orthogonality identity (7) now proves
\[
\boxed{\Phi_{E_n}(pI,Q_n)=F_n^1.}
\tag{22}
\]

In particular, this is an exact finite-perturbation computation—not just a derivative of an optimizer. From (11), (16), and (22),
\[
\boxed{
\|\Phi_{E_n}(pI,Q_n)-\Phi_{E_n}(pI,P_n)\|_1
=
\tau_n\left(2+\frac{n-2}{2}(1-2p)\right).
}
\tag{23}
\]

## 7. The input trace distance and the divergent ratio

Only the first two coordinates of \(w_n-v_n\) are nonzero. Rationalizing the square-root differences gives
\[
\left|\sqrt{\frac1n\pm\tau_n}-\frac1{\sqrt n}\right|
=
\frac{\tau_n}
{\sqrt{1/n\pm\tau_n}+1/\sqrt n}
\le\sqrt n\,\tau_n.
\]
Therefore
\[
\|w_n-v_n\|_2\le\sqrt{2n}\,\tau_n.
\]
Using the rank-one decomposition
\[
Q_n-P_n=(w_n-v_n)w_n^*+v_n(w_n-v_n)^*
\]
and the unit norms of \(v_n,w_n\), we obtain
\[
\boxed{
\|Q_n-P_n\|_1\le2\sqrt{2n}\,\tau_n.
}
\tag{24}
\]

Since \(K_n=L_n\), equations (23)–(24) imply
\[
\begin{aligned}
\frac{\|\Phi_{E_n}(K_n,Q_n)-\Phi_{E_n}(L_n,P_n)\|_1}
{\|K_n-L_n\|_1+\|Q_n-P_n\|_1}
&\ge
\frac{2+(n-2)(1-2p)/2}{2\sqrt{2n}}\\
&\ge
\frac{(n-2)(1-2p)}{4\sqrt{2n}}.
\end{aligned}
\tag{25}
\]
For \(n\ge4\), use \(n-2\ge n/2\) and
\[
1-2p=\frac{1-2\varepsilon}{2}
\]
to obtain
\[
\frac{\|\Phi_{E_n}(K_n,Q_n)-\Phi_{E_n}(L_n,P_n)\|_1}
{\|K_n-L_n\|_1+\|Q_n-P_n\|_1}
\ge
\frac{1-2\varepsilon}{16\sqrt2}\sqrt n
\longrightarrow\infty.
\]
This proves (1), so no finite \(C_\varepsilon\) can satisfy (ULM).

## Scope of the disproof

The obstruction is specific to the least-Euclidean-norm selector. It occurs even where all its inequality constraints are strictly inactive: the explicitly identified gradient correction contributes a fixed positive amount of \(\ell^1\) variation in each of the \(n-2\) other coordinate directions.

For comparison, on the same scalar-kernel family, the different flow
\[
\widetilde F_{pI,R}(x,i)
=
R_{ii}\prod_{\ell\ne i}p^{x_\ell}(1-p)^{1-x_\ell},
\qquad x_i=0,
\]
is nonnegative, has the required divergence and mass, and satisfies
\[
\widetilde F_{\rm out}(x)
\le\frac1{1-p}\mu_p(x).
\]
Moreover,
\[
\|\widetilde F_{pI,R}-\widetilde F_{pI,R'}\|_1
=
\sum_i|R_{ii}-R'_{ii}|
\le\|R-R'\|_1.
\]
Thus the counterexample does **not** rule out a different unrestricted selector.

It does show that constants for the particular selector (LM) on support at most \(s\) must grow at least
\[
\frac{1-2\varepsilon}{16\sqrt2}\sqrt s
\qquad(s\ge4).
\]
The frozen uniform-in-support assertion for (LM) is false. \(\square\)

