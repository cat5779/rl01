# Frozen problem

Let \(X,X_1,X_2,\ldots\) be independent and identically distributed nondegenerate real random variables. Put
\[
S_n=\sum_{i=1}^nX_i,
\qquad
V_n^2=\sum_{i=1}^nX_i^2.
\]
Assume either that \(\mathbb E X\) exists and equals \(0\), or that \(\mathbb E X^2=\infty\).

For \(s\in\mathbb R\) and \(t<0\), define
\[
K(s,t)=\log \mathbb E e^{sX+tX^2},
\qquad
K_{ij}(s,t)=\frac{\partial^2K(s,t)}{\partial\theta_i\partial\theta_j},
\quad (\theta_1,\theta_2)=(s,t).
\]
For \(0<x<1\), let \((a_0,\widehat t_0)\), with \(\widehat t_0<0\), be the saddlepoint pair solving
\[
\frac{\mathbb E\!\left[Xe^{\widehat t_0(-2a_0X/x^2+X^2)}\right]}
     {\mathbb E e^{\widehat t_0(-2a_0X/x^2+X^2)}}=a_0,
\qquad
\frac{\mathbb E\!\left[X^2e^{\widehat t_0(-2a_0X/x^2+X^2)}\right]}
     {\mathbb E e^{\widehat t_0(-2a_0X/x^2+X^2)}}=\frac{a_0^2}{x^2},
\]
and set \(\widehat s_0=-2a_0\widehat t_0/x^2\). Define
\[
\Delta=
\begin{pmatrix}
K_{11}(\widehat s_0,\widehat t_0)&K_{12}(\widehat s_0,\widehat t_0)\\
K_{12}(\widehat s_0,\widehat t_0)&K_{22}(\widehat s_0,\widehat t_0)
\end{pmatrix},
\]
\[
\Lambda_0(x)=\widehat s_0a_0+\frac{\widehat t_0a_0^2}{x^2}
-K(\widehat s_0,\widehat t_0),
\]
\[
\Lambda_1(x)=\frac{2\widehat t_0}{x^2}
+(1,2a_0/x^2)\Delta^{-1}(1,2a_0/x^2)^{\mathsf T},
\]
and
\[
w(x)=\sqrt{2\Lambda_0(x)},
\qquad
v(x)=\left(-\frac{\widehat t_0}{2}\right)^{1/2}
x^{3/2}a_0^{-1}(\det\Delta)^{1/2}\Lambda_1(x)^{1/2}.
\]
Here \(\Phi\) and \(\phi\) are the standard normal distribution function and density.

The quantification is over admissible laws and values of \(x\) for which the displayed saddlepoint is the source's interior saddlepoint and the displayed quantities are finite and real, with \(a_0\ne0\), \(\Delta\) invertible, and \(w,v>0\). No characteristic-function integrability condition may be added.

Prove or disprove both assertions:

1. For every fixed \(0<x<1\), as \(n\to\infty\),
   \[
   \mathbb P\!\left(\frac{S_n}{V_n}\ge x\sqrt n\right)
   =1-\Phi(\sqrt n\,w)
   -\frac{\phi(\sqrt n\,w)}{\sqrt n}
   \left(\frac1w-\frac1v+O(n^{-1/2})\right).
   \]

2. For every deterministic sequence \(a_n\downarrow0\) satisfying \(a_n\sqrt n\to\infty\), the same expansion holds uniformly for \(a_n\le x\le1/2\); the \(O(n^{-1/2})\) term is uniform in \(x\) (but may depend on the fixed law of \(X\)).

The law of \(X\) is fixed before \(n\to\infty\). A proof must cover both parts. A counterexample to either part disproves the ICM question, but it must satisfy every admissibility condition above and must use the source's saddlepoint branch. Finite numerical experiments alone do not decide either asymptotic assertion.
