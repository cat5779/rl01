# Central clock-gap asymptotic

**Status: PROVED_HERE / PENDING_INDEPENDENT_REVIEW**

Let `rho_m(r)` be the `m`-step law of the symmetric lazy walk with step
probabilities `b,1-2b,b`, where `b=39/1600`.  The reviewed random-walk formula
is

\[
\theta_m=c^2\frac{k(k-1)}{m(m-1)}
\frac{\rho_{k-2}(k-m)}{\rho_k(k-m)}.                          \tag{1}
\]

For each fixed integer `r`, Fourier inversion and a two-term Laplace expansion
at the unique maximum `t=0` give

\[
\rho_j(r)=\frac1{\sqrt{4\pi bj}}
\left(1+\frac{C_r}{j}+O(j^{-2})\right).                      \tag{2}
\]

To see that the error has the stated order, split the Fourier integral at a
fixed small neighbourhood of zero.  Outside it the characteristic function
has modulus at most `q<1`.  Inside it, expand
`log(1-2b+2b cos t)` through `t^6`, put `t=u/sqrt(j)`, and integrate the
Gaussian times the resulting polynomial; the discarded term is dominated by
`exp(-b u^2/2) O((1+|u|^12)/j^2)`.  This proves (2), with a constant depending
only on fixed `r` and `b`.

Consequently, for `r=0,1`,

\[
\frac{\rho_{k-2}(r)}{\rho_k(r)}
=\sqrt{\frac{k}{k-2}}
\frac{1+C_r/(k-2)+O(k^{-2})}{1+C_r/k+O(k^{-2})}
=1+\frac1k+O(k^{-2}).                                       \tag{3}
\]

Putting `m=k` and `m=k-1` in (1) gives

\[
\theta_k=c^2\left(1+\frac1k+O(k^{-2})\right),                \tag{4}
\]

and

\[
\theta_{k-1}
=c^2\frac{k}{k-2}\left(1+\frac1k+O(k^{-2})\right)
=c^2\left(1+\frac3k+O(k^{-2})\right).                        \tag{5}
\]

Since `s_m=-log(theta_m)/(2(2k-1))`, equations (4)--(5) imply

\[
\boxed{s_k-s_{k-1}=\frac{1}{2k^2}+O(k^{-3}).}                \tag{6}
\]

The raw total jump rate on layer `k-1` is
`(k-1)(k+1)=k^2-1`.  Therefore

\[
(k^2-1)(s_k-s_{k-1})\longrightarrow\frac12.                 \tag{7}
\]

Thus the bridge interval shrinks in raw time but does not become a zero-jump
perturbation.  Its limiting expected number of exchanges is one half.  Any
proof that `E_k` is small must control the entropy cost of this finite exchange
window; the fact `s_k-s_{k-1}->0` alone is insufficient.

