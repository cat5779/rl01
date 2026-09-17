# An exact four-site obstruction to external-field production convexity

This secondary witness rules out a surrogate curvature step, not the actual
sine diagonal-shift target. It was first detected in a complete-atom floating
probe and is proved here by exact rational identities and elementary log
bounds.

Let `U_{jk}=exp(2*pi*i*j*k/4)/2`, `0<=j,k<=3`, be the four-site Fourier
unitary, where `i` is the imaginary unit, and let
`P=U_{:,0:2}U_{:,0:2}*` be its genuine consecutive-mode rank-two projection:

\[
 P=\begin{pmatrix}
 1/2&(1-i)/4&0&(1+i)/4\\
 (1+i)/4&1/2&(1-i)/4&0\\
 0&(1+i)/4&1/2&(1-i)/4\\
 (1-i)/4&0&(1+i)/4&1/2
 \end{pmatrix}.
\]

Take `c=19/20` and `K=(1-c)I/2+cP`. For its complete labelled law `p`, apply
the uniform external field

\[
 p_h(y)=p(y)e^{h(|y|-2)}/\mathbb E_p e^{h(|Y|-2)}.
\]

This is a legal DPP for every finite `h`. At `h=0`, set `v=(1-c^2)/4=39/1600`.
Its actual atom jets are

\[
 p_h'=p(|y|-2),\qquad
 p_h''=p[(|y|-2)^2-4v].
\]

For the center site 0, let

\[
 I(h)=\sum_{w\in\{0,1\}^3}
       \frac{p_h(1,w)-p_h(0,w)}2
       \log\frac{p_h(1,w)}{p_h(0,w)}.
\]

All sixteen atoms, in binary-mask order with bit 0 the center, are the
following integer numerators divided by `2560000`:

```
1521, 29679, 29679, 290321,
29679, 579121, 290321, 29679,
29679, 290321, 579121, 29679,
290321, 29679, 29679, 1521.
```

They follow directly from
`p(y)=(-1)^(4-|y|) det(K-diag(1-y))`; in particular they sum to one and none
is omitted. Substitution in the exact pair second-derivative formula gives

\[
 \boxed{\quad
 I''(0)=\frac{39}{800}
       -\frac{39}{1600}\log\frac{761}{39}
       -\frac{11018319}{256000000}\log\frac{290321}{29679}
       <-\frac1{10}.
 \quad}
\]

The strict bound needs no numerical logarithms. The two log arguments exceed
`16` and `8`, respectively. Since `log2>2/3`, their logarithms exceed `8/3`
and `2`. Therefore the displayed expression is less than

\[
 \frac{39}{800}-\frac{39}{1600}\frac83
        -\frac{11018319}{256000000}\,2
 =-\frac{13098319}{128000000}<-1/10.
\]

This external field is not the fixed-contrast affine shift. If `F(m,c)` is
any smooth functional of the finite projection family
`K=mI+c(P-I/2)`, then at `m=1/2` its field path has

\[
 m_h'=v,\quad c_h'=0,\quad m_h''=0,\quad c_h''=-2cv,
 \qquad F_{hh}=v^2 F_{mm}-2cv F_c.
\]

Consequently one cannot replace `F_mm` by a rescaled `F_hh` while discarding
the contrast-acceleration term. The negative field-production curvature here
is entirely consistent with positive actual-shift production curvature. It
also does not refute the local full-law tilt approximation: an approximation
of laws at the `R^(-1/2)` scale is not an order-one curvature-sign theorem.
