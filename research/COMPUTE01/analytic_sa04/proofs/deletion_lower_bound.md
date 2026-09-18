# Dimension-free lower bound for the central deletion loss

**Status: PROVED_HERE / PENDING_INDEPENDENT_REVIEW**

Let `n=2k>=4`, let `mu` be the corrected `k`-layer law at the original time
`s_k`, and let `nu=mu D_k` be its uniform deletion to layer `k-1`.  Form two
laws on pairs `(T,x)` with `|T|=k-1` and `x notin T`:

\[
J(T,x)=\frac{\mu(T\cup\{x\})}{k},\qquad
R(T,x)=\frac{\nu(T)}{k+1}.
\]

The standard chain rule calculation gives

\[
D(J\Vert R)=F_k(s_k)-F_{k-1}(s_k)=A_k.                 \tag{1}
\]

Put `w_ij=|P_ij|^2` and use the bounded statistic

\[
\Phi(T,x)=\sum_{j\in T}w_{xj}.
\]

Because `P` is a projection with `P_ii=1/2`,

\[
0\le\Phi\le\sum_{j\ne x}|P_{xj}|^2
=(P^2)_{xx}-|P_{xx}|^2=\frac14.                      \tag{2}
\]

## Pair law at the corrected clock

For distinct `i,j`, applying the raw exchange generator to
`1_{i,j subset S}` gives

\[
G_k 1_{i,j\subset S}
=(k-1)(1_{i\in S}+1_{j\in S})-2(n-1)1_{i,j\subset S}.
\]

The one-point marginals remain `1/2`, so if
`M_ij=P_mu(i,j in S)` and

\[
u_2=\frac{k(k-1)}{n(n-1)}=\frac{k-1}{2(2k-1)},
\]

then, using `exp[-2(n-1)s_k]=theta_k` and the DPP pair probability
`1/4-w_ij`,

\[
M_{ij}=u_2+\theta_k\left(\frac{1}{4(2k-1)}-w_{ij}\right).     \tag{3}
\]

Write

\[
S_1=\sum_{i\ne j}w_{ij},\qquad S_2=\sum_{i\ne j}w_{ij}^2,
\qquad Q=\sum_{i\ne j}w_{ij}M_{ij}.
\]

Under `J`, the point `x` is uniformly deleted from `S`, hence

\[
E_J\Phi=Q/k.                                                  \tag{4}
\]

Under `R`, `x` is uniform in the `k+1` point complement of `T`.  Since uniform
deletion gives

\[
P(j\in T)=\frac{k-1}{2k},\qquad
P(i,j\in T)=\frac{k-2}{k}M_{ij},
\]

we obtain

\[
E_R\Phi=\frac1{k+1}\left[\frac{k-1}{2k}S_1-\frac{k-2}{k}Q\right]. \tag{5}
\]

Substituting (3) into (4)--(5), the uniform component cancels and gives

\[
E_J\Phi-E_R\Phi
=\frac{\theta_k}{k(k+1)}\left(\frac{S_1}{4}-(2k-1)S_2\right). \tag{6}
\]

## Fourier sums

Projection idempotence gives `S_1=n/4=k/2`.  For the half-band Fourier
projection, nonzero off-diagonal entries occur at odd cyclic distances and

\[
|P_{0d}|^2=\frac{1}{(2k)^2\sin^2(\pi d/(2k))}.
\]

Using

\[
\sum_{d=1}^{m-1}\csc^4(\pi d/m)=\frac{m^4+10m^2-11}{45}
\]

and subtracting the even distances from the full `2k` sum yields

\[
S_2=2k\left(\frac1{48}+\frac1{24k^2}\right)
=\frac{k}{24}+\frac1{12k}.                                  \tag{7}
\]

Equations (6)--(7) therefore imply

\[
|E_J\Phi-E_R\Phi|
=\theta_k\frac{(k-1)(k^2-k+1)}{12k^2(k+1)}.                  \tag{8}
\]

The random-walk representation in the reviewed report gives

\[
\theta_k=c^2\frac{\rho_{k-2}(0)}{\rho_k(0)}\ge c^2.          \tag{9}
\]

Indeed the symmetric lazy-step law is unimodal, convolution preserves
unimodality, and `rho_k(0)` is an average of values of `rho_{k-2}`, whose
maximum is at zero.  Also, for every `k>=2`,

\[
\frac{(k-1)(k^2-k+1)}{12k^2(k+1)}\ge\frac1{48}.              \tag{10}
\]

Finally, a `[0,1/4]`-valued statistic satisfies
`TV(J,R)>=4|E_J Phi-E_R Phi|`.  Pinsker's inequality in natural logarithms,
`D(J||R)>=2TV(J,R)^2`, and (1), (8)--(10) give

\[
\boxed{A_k\ge 32(c^2/48)^2=\frac{c^4}{72}}
\qquad(k\ge2).                                               \tag{11}
\]

At `c=19/20`, this explicit bound is

\[
A_k\ge\frac{130321}{11520000}>0.01131.
\]

There is also a stronger asymptotic consequence.  From the Fourier integral

\[
\rho_m(0)=\frac1{2\pi}\int_{-\pi}^{\pi}
  (1-2b+2b\cos t)^m\,dt
\]

the elementary local Laplace estimate gives
`rho_m(0)~(4 pi b m)^(-1/2)`.  Hence
`rho_{k-2}(0)/rho_k(0)->1`, so `theta_k->c^2`.  The rational factor in (8)
converges to `1/12`.  Therefore Pinsker also yields

\[
\boxed{\liminf_{k\to\infty}A_k\ge\frac{2c^4}{9}}
=\frac{130321}{720000}>0.1810.                              \tag{12}
\]

This proves that the same-clock deletion loss cannot vanish.  It does not yet
prove `d_k>0`, because an upper bound below this constant is still required for
the reverse-clock cost `E_k`.
