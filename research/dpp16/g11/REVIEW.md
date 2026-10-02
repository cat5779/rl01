STATUS: PASS

# Independent adversarial audit of R16/G11

I checked the complete `output.md` against the frozen problem and against the
fixed-support theorem certified in R15/G11.  The proposed family is a valid
counterexample for the **actual global least-Euclidean-norm selector**.  It
gives a ratio of output edge-flow \(\ell^1\) distance to input trace-norm
distance growing as \(\sqrt n\).  It is fully compatible with R15/G11: that
result allows its constant to depend on the support bound \(s\), whereas this
family has support size \(s=n\) and proves that such constants must grow at
least on the order of \(\sqrt s\).

## 1. Admissibility of the data

For
\[
p=\frac{1+2\varepsilon}{4},\qquad
\tau_n=\frac{p^n}{n},
\]
one has
\[
\varepsilon<p<\frac12<1-\varepsilon,
\]
because \(p-\varepsilon=(1-2\varepsilon)/4>0\).  Hence
\(K_n=L_n=pI_n\) is strictly \(\varepsilon\)-gapped.

The vectors
\[
v_n=n^{-1/2}(1,\ldots,1),
\]
\[
w_n=\left(\sqrt{n^{-1}+\tau_n},
\sqrt{n^{-1}-\tau_n},n^{-1/2},\ldots,n^{-1/2}\right)
\]
are well-defined because \(0<\tau_n<1/n\), and
\[
\|w_n\|_2^2=(n^{-1}+\tau_n)+(n^{-1}-\tau_n)+(n-2)n^{-1}=1.
\]
Thus \(P_n=v_nv_n^*\) and \(Q_n=w_nw_n^*\) are rank-one
projectors.  Every coordinate of both defining vectors is nonzero, so both
projectors have support exactly \(E_n\), of size \(n\).

## 2. Exact derivative and fiber right-hand sides

At the scalar kernel, differentiating the exact-pattern determinant formula
gives, for every Hermitian direction \(R\),
\[
b_{pI,R}(x)=\mu_p(x)\sum_i R_{ii}
\left(\frac{x_i}{p}-\frac{1-x_i}{1-p}\right).
\]
This is correct: at a diagonal base point all off-diagonal directional terms
drop from the first derivative of the determinant.  Since
\[
\operatorname{diag}(Q_n-P_n)=(\tau_n,-\tau_n,0,\ldots,0),
\]
the two unequal patterns of \((x_1,x_2)\) contribute the score difference
\(\pm[p(1-p)]^{-1}\), while \(\mu_p\) contributes \(p(1-p)\).
Therefore the displayed identity
\[
b_{pI,Q_n}(x)-b_{pI,P_n}(x)
=\tau_n(x_1-x_2)\rho_p(x_3,\ldots,x_n)
\]
is exact.  Thus the later correction is checked against the actual DPP birth
derivative, not against a surrogate divergence.

## 3. Why a feasible gradient is the actual unique minimizer

With upward gradient
\(\nabla u(x,i)=u(x+e_i)-u(x)\), the stated divergence convention gives
\[
\operatorname{div}\nabla u(x)
=\sum_i\bigl(u(x)-u(x^{(i)})\bigr)=\mathcal L_nu(x).
\]
For every divergence-free edge flow \(h\), summation by parts gives
\[
\langle\nabla u,h\rangle
=\sum_xu(x)\operatorname{div}h(x)=0.
\]
Consequently, if \(F=\nabla u\) is feasible and \(H\) is any other point of
the same full fiber, then
\[
\|H\|_2^2=\|F\|_2^2+\|H-F\|_2^2.
\]
Hence \(F\) is the unique global least-norm point of that fiber.  This
argument compares with every feasible circulation and does not assume an
active set.  In the constructed examples the nonnegativity and capacity
inequalities are in fact strict, so the inequality faces cannot alter this
identification.

## 4. Baseline selector

The baseline flow
\[
F_n^0(x,i)=\frac1n p^{|x|}(1-p)^{n-1-|x|},\qquad x_i=0,
\]
has direction-wise mass \(1/n\), hence total mass one.  Its incoming-minus-
outgoing divergence is
\[
\frac{|x|}{n}p^{|x|-1}(1-p)^{n-|x|}
-\frac{n-|x|}{n}p^{|x|}(1-p)^{n-1-|x|},
\]
which is exactly \(b_{pI,P_n}(x)\), since
\(\operatorname{diag}P_n=(1/n,\ldots,1/n)\).

It is the gradient of the displayed radial potential \(\psi_n(|x|)\).
Moreover,
\[
(F_n^0)_{\rm out}(x)
=\frac{n-|x|}{n(1-p)}\mu_p(x)
\le\frac1{1-p}\mu_p(x)<\frac2\varepsilon\mu_p(x).
\]
It is therefore feasible, and the gradient orthogonality proves the exact
identity
\[
\Phi_{E_n}(pI,P_n)=F_n^0.
\]

## 5. Correction potential, divergence, and edge norm

Let \(m=n-2\), \(\eta=x_1-x_2\),
\(q(t)=1/2+(p-1/2)t\), and
\[
u_n(x)=\frac{\eta}{2}\int_0^1\rho_{q(t)}(y)\,dt.
\]
The two identities used in the proof are correct:
\[
\mathcal L_2\eta=2\eta,
\qquad
\mathcal L_m\rho_q=(2q-1)\partial_q\rho_q.
\]
Since \(2q(t)-1=2tq'(t)\), integration by parts yields
\[
\mathcal L_nu_n
=\eta\int_0^1\left(\rho_{q(t)}
+t\frac d{dt}\rho_{q(t)}\right)dt
=\eta\rho_p.
\]
Thus \(G_n=\nabla u_n\) has exactly the required correction divergence.

The edge formulas are also correct.  Directions 1 and 2 are respectively
\(+A(y)\) and \(-A(y)\), with
\(A(y)=\frac12\int_0^1\rho_{q(t)}(y)dt\).  For \(j\ge3\),
\[
G_n(x,j)=\frac{(2p-1)\eta}{2}
\int_0^1t\rho_{q(t)}^{(-j)}(x)dt.
\]
Summing absolute values gives exactly one unit from each of directions 1 and
2.  For each \(j\ge3\), the sum of \(|\eta|\) over the four first-coordinate
patterns is 2, the remaining product law sums to one, and
\(\int_0^1t\,dt=1/2\).  Hence
\[
\sum_{x:x_j=0}|G_n(x,j)|=\frac{1-2p}{2}
\]
and therefore
\[
\boxed{\|G_n\|_1=2+\frac{n-2}{2}(1-2p).}
\]
The signed sums are \(+1,-1,0,\ldots,0\), so the total signed edge mass of
\(G_n\) is zero.  Finally \(|A(y)|\le1/2\), and the other directions satisfy
the sharper bound \(|G_n(x,j)|\le(1-2p)/4\), validating the global pointwise
bound \(|G_n(x,i)|\le1/2\).

## 6. Exact feasibility of the perturbed minimizer

Set \(F_n^1=F_n^0+\tau_nG_n\).  The divergence computation above gives
\(\operatorname{div}F_n^1=b_{pI,Q_n}\), and the zero total signed mass of
\(G_n\) preserves total mass one.

Every factor in a baseline edge is at least \(p\), because \(p<1/2\), so
\[
F_n^0(x,i)\ge \frac{p^{n-1}}n.
\]
Using \(\tau_n=p^n/n\) and \(|G_n|\le1/2\),
\[
F_n^1(x,i)\ge\frac{p^{n-1}}n\left(1-\frac p2\right)>0.
\]
For capacity, \(\mu_p(x)\ge p^n\) and there are at most \(n\) outgoing
edges, whence
\[
(F_n^1)_{\rm out}(x)
\le\frac1{1-p}\mu_p(x)+\frac{\tau_n n}{2}
\le\left(\frac1{1-p}+\frac12\right)\mu_p(x)
<\frac52\mu_p(x)<\frac2\varepsilon\mu_p(x).
\]
Thus all inequalities are strict.  Since
\(F_n^1=\nabla(\psi_n+\tau_nu_n)\), the orthogonality argument proves the
second exact selector identity
\[
\Phi_{E_n}(pI,Q_n)=F_n^1.
\]
It follows without linearization or active-set assumptions that
\[
\|\Phi_{E_n}(pI,Q_n)-\Phi_{E_n}(pI,P_n)\|_1
=\tau_n\left(2+\frac{n-2}{2}(1-2p)\right).
\]

## 7. Input distance and divergent quotient

Only two coordinates of \(w_n-v_n\) are nonzero.  Rationalizing each square
root gives
\[
\left|\sqrt{n^{-1}\pm\tau_n}-n^{-1/2}\right|
\le\sqrt n\,\tau_n,
\]
and hence
\(\|w_n-v_n\|_2\le\sqrt{2n}\tau_n\).  The rank-one decomposition
\[
Q_n-P_n=(w_n-v_n)w_n^*+v_n(w_n-v_n)^*
\]
then yields the valid upper bound
\[
\|Q_n-P_n\|_1\le2\sqrt{2n}\tau_n.
\]
Using an upper bound on the denominator is the correct direction for the
desired lower bound.  Since the kernels coincide, cancellation of \(\tau_n\)
gives
\[
\frac{\|\Phi(pI,Q_n)-\Phi(pI,P_n)\|_1}{\|Q_n-P_n\|_1}
\ge
\frac{2+(n-2)(1-2p)/2}{2\sqrt{2n}}
\ge\frac{1-2\varepsilon}{16\sqrt2}\sqrt n
\]
for \(n\ge4\).  The quotient therefore diverges.

## 8. Scope and relation to R15/G11

The counterexample disproves only a support-uniform Lipschitz constant for the
particular global least-norm selector.  It does **not** disprove the existence
of another unrestricted selector: the explicit scalar-kernel selector in the
source remains a positive, stable section.  Nor does it address exact JO or a
strong process.

For a support-at-most-\(s\) theorem, taking \(n=s\) merely forces any valid
constant for this least-norm selector to obey
\[
C_{\varepsilon,s}\ge
\frac{1-2\varepsilon}{16\sqrt2}\sqrt s
\qquad(s\ge4).
\]
This does not contradict R15/G11, whose independently audited proof supplies a
finite but explicitly \(s\)-dependent constant by reducing to a cube on at
most \(2s\) active coordinates.  The quantifier boundary is therefore
consistent: fixed finite \(s\) remains proved, while uniformity over all
support sizes for `(LM)` is disproved.

The R16/G11 verdict is **PASS**.

