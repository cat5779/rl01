# Complete-current derivative correction

The corrected argument is incorporated in [PROOF03.md](PROOF03.md), SHA256 8d955f89fc680d8d02a4259b90866f6bf13be5d54998e2986478fab3383e82a6. This note records the correction to its derivation predecessor. The predecessor's Section 2 paragraphs separately bounding the probability-factor and inverse-factor edge terms do not justify a factor 1/2 for the latter. Those two decomposed terms, considered separately, need not have identical representations from both endpoints. This is a proof-order defect; inequality (4), its constant, and all later estimates remain valid by the following replacement.

Along K_t, with derivative D and d=||D||tr, retain
\[
\dot p(S)=p(S)\alpha_S,\quad
\alpha_S=\operatorname{tr}(M_S^{-1}D),\quad
|\alpha_S|\le d/\varepsilon,\qquad
\dot u^S=-M_S^{-1}D u^S .
\]
Differentiate the two *complete* incident representations of the same edge current. At either endpoint S, the complete derivative is
\[
\dot J_e=\pm p(S)\operatorname{Re}
 [v_i\overline{\alpha_Su_i^S+\dot u_i^S}].
\]
Therefore
\[
\dot J_e^2/w_t(e)
\le(1-\varepsilon)p(S)
 |\alpha_Su_i^S+\dot u_i^S|^2.
\]
This is the same complete dotJ_e at both endpoints, so summing over all vertices legitimately counts each edge twice:
\[
\begin{aligned}
2\|\dot J_t\|_{w_t}^2
&\le(1-\varepsilon)\sum_Sp(S)
 \|\alpha_Su^S+\dot u^S\|_2^2\\
&\le(1-\varepsilon)(2d/\varepsilon^2)^2.
\end{aligned}
\]
The last inequality uses ||u^S||<=epsilon^-1, ||D||op<=d,
||dot u^S||<=d epsilon^-2, and sum_S p(S)=1. Since
\(B_\varepsilon^2=2(1-\varepsilon)/\varepsilon^2\),
\[
\|\dot J_t\|_{w_t}
\le(B_\varepsilon/\varepsilon)d.
\]
This is exactly frozen equation (4). No claim of a separate double-counted estimate for the two decomposed edge terms is retained. The weighted repair, variational inequalities, constant50 and stated constant10 are unaffected.
