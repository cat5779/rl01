# High-contrast resummation: what closes and what a local route cannot prove

**STATUS.**  This note gives three rigorous results.

1. For the uniform fixed-cardinality law, the entire high-contrast posterior
   is summed exactly by output cardinality and input--output overlap.  The
   apparently superextensive
   \(k(n-k)d^2|\log d|\) exchange term is the first coefficient of a finite
   hypergeometric partition function, not a volume-uniform approximation.
2. A positive-density family of cyclic Fourier projection DPPs has output
   entropy concave for every contrast.  The family consists of Fourier combs;
   it includes a half-density antipodal projection in every even dimension.
3. The exact weighted local-row criterion used in
   `stationary-weighted-energy-route.md` cannot cover any contrast above one
   half: for every \(c>1/2\) its unrestricted local constant diverges as a
   channel endpoint is approached.  This is a failure of that sufficient
   condition, not a counterexample to entropy concavity.

The note does **not** prove the stationary contiguous-sine conjecture for
\(c>1/2\).  Section 7 states the remaining global obstruction precisely.
All logarithms are natural, and
\(h(t)=-t\log t-(1-t)\log(1-t)\) denotes binary entropy.

## 1. High-contrast channel and notation

Write

\[
 c=1-d,\qquad a=db,\qquad 0<d<1,\quad 0<b<1.
 \tag{1.1}
\]

Thus a coordinate is retained with probability \(1-d\), and with probability
\(d\) it is replaced by an independent Bernoulli-\(b\) bit.  If the input
\(X\) has exactly \(k\) ones, put

\[
 u=1-d(1-b)=a+c,\quad \delta=d(1-b)=1-a-c,
 \quad v=db=a,\quad w=1-db=1-a.
 \tag{1.2}
\]

For an input set \(S\), an output set \(T\), and
\(j=|S\cap T|\), \(\ell=|T|\), the channel likelihood is

\[
 \Pr(T\mid S)
 =u^j\delta^{k-j}v^{\ell-j}w^{n-k-\ell+j}
 =\delta^k v^\ell w^{n-k-\ell}\theta^j,
 \tag{1.3}
\]

where

\[
 \theta={uw\over\delta v}>0,
 \qquad R=\theta^{-1}
 ={d^2b(1-b)\over[1-d(1-b)](1-db)}.
 \tag{1.4}
\]

The strict channel interior is used in (1.2)--(1.4).  All closed-interval
entropy statements below follow by continuity, with \(0\log0=0\).

## 2. Exact difference-set resummation for the uniform slice

Let \(X\) be uniform on the \(k\)-subsets of \([n]\).  Conditional on a fixed
output \(T\) of size \(\ell\), all input sets having the same overlap with
\(T\) have the same posterior weight.  Define

\[
 Z_{n,k,\ell}(\theta)
 =\sum_j {\ell\choose j}{n-\ell\choose k-j}\theta^j,
 \tag{2.1}
\]

where the sum is over
\(\max(0,k+\ell-n)\le j\le\min(k,\ell)\).

> **Proposition 2.1 (exact all-order posterior).**
> For every output \(T\) with \(|T|=\ell\),
> \[
>  \Pr(X=S\mid Y=T)
>  ={\theta^{|S\cap T|}\over Z_{n,k,\ell}(\theta)},
>  \qquad |S|=k,
>  \tag{2.2}
> \]
> and therefore
> \[
>  H(X\mid Y=T)
>  =\log Z_{n,k,\ell}(\theta)
>   -{\theta Z_{n,k,\ell}'(\theta)\over
>          Z_{n,k,\ell}(\theta)}\log\theta.
>  \tag{2.3}
> \]

**Proof.**  The uniform prior cancels from Bayes' formula, and (1.3) leaves
only \(\theta^{|S\cap T|}\).  There are
\({\ell\choose j}{n-\ell\choose k-j}\) inputs at overlap \(j\), which proves
(2.1)--(2.2).  Substitution into
\(-\sum_S p_S\log p_S\) proves (2.3).  \(\square\)

For the same-cardinality output sector \(\ell=k\), put
\(r=k-|S\cap T|\).  The exact exchange partition function is

\[
 \mathcal Z_{n,k}(R)
 =\sum_{r=0}^{\min(k,n-k)}
   {k\choose r}{n-k\choose r}R^r.
 \tag{2.4}
\]

Equation (2.3) becomes

\[
 \boxed{
 H(X\mid Y=T)
 =\log\mathcal Z_{n,k}(R)
  -{R\mathcal Z_{n,k}'(R)\over\mathcal Z_{n,k}(R)}\log R,
 \qquad |T|=k.}
 \tag{2.5}
\]

This is the requested all-order resummation by output difference-set size.
It includes every number of simultaneous exchanges; no condition such as
\(nd\ll1\) is present.

### 2.1 Recovery of the nonuniform Taylor coefficient

For fixed \(n,k\), (2.4)--(2.5) and \(R=d^2b(1-b)(1+O(d))\) give

\[
 \begin{aligned}
 H(X\mid Y=T)
  ={}&k(n-k)d^2b(1-b)
       \bigl[1-2\log d-\log(b(1-b))\bigr]\\
    &+O_{n,k,b}(d^3|\log d|+d^4|\log d|).
 \end{aligned}
 \tag{2.6}
\]

In particular, the leading logarithmic term is exactly

\[
 2k(n-k)d^2b(1-b)|\log d|,
 \tag{2.7}
\]

which agrees with the exchange coefficient isolated in
`stationary-high-contrast-uniform-route.md`.  Since the coefficient in
(2.7) is quadratic in \(n\) at fixed density, the expansion (2.6) is not
uniform in volume.  Formula (2.5), rather than a finite truncation of it, is
the correct object before taking \(n\to\infty\).

### 2.2 Thermodynamic posterior formula

Let \(k_n/n\to\rho\in(0,1)\) and \(\ell_n/n\to\lambda\in(0,1)\).  Stirling's
formula and the finite Laplace principle applied to (2.1) give

\[
 {1\over n}\log Z_{n,k_n,\ell_n}(\theta)
 \longrightarrow
 \max_x\left\{
 \lambda h\!\left({x\over\lambda}\right)
 +(1-\lambda)h\!\left({\rho-x\over1-\lambda}\right)
 +x\log\theta\right\},
 \tag{2.8}
\]

on the interval
\(\max(0,\rho+\lambda-1)\le x\le\min(\rho,\lambda)\).
The maximizer \(x_*\) is unique in the interior and satisfies

\[
 \theta(\lambda-x_*)(\rho-x_*)
 =x_*(1-\lambda-\rho+x_*).
 \tag{2.9}
\]

Concentration of the one-dimensional Gibbs weights in (2.1), followed by
(2.3), yields

\[
 {1\over n}H(X\mid Y=T_n)
 \longrightarrow
 \lambda h\!\left({x_*\over\lambda}\right)
 +(1-\lambda)h\!\left({\rho-x_*\over1-\lambda}\right).
 \tag{2.10}
\]

For \(\lambda=\rho\), writing \(e=\rho-x_*\), equation (2.9) reads

\[
 R(\rho-e)(1-\rho-e)=e^2.
 \tag{2.11}
\]

Thus the typical number of exchanges is order \(n\), rather than order one,
for fixed \(d>0\).  Equations (2.7) and (2.10) rigorously exhibit the
noncommutation of the fixed-volume small-\(d\) expansion and the
thermodynamic limit.

## 3. Complete output entropy for the uniform slice

Let \(L=|Y|\).  Under the uniform \(k\)-slice input,

\[
 L\ \stackrel{d}=\ \operatorname{Bin}(k,a+c)
      +\operatorname{Bin}(n-k,a),
 \tag{3.1}
\]

with the two binomials independent, and conditional on \(L=\ell\) the output
is uniform on the \(\ell\)-slice.  Hence

\[
 H(Y)=H(L)+\mathbb E\log{n\choose L}.
 \tag{3.2}
\]

The first term is concave in \(a\) by the Hillion--Johnson proof of the
Shepp--Olkin theorem.  For completeness, if
\(\psi(\ell)=\log{n\choose\ell}\), direct differentiation of the independent
Bernoulli product in (3.1) gives

\[
 {d^2\over da^2}\mathbb E\psi(L)
 =2\sum_{i<j}\mathbb E\Delta^2\psi(L_{-ij}),
 \tag{3.3}
\]

and

\[
 \Delta^2\psi(s)
 =\log{(n-s-1)(s+1)\over(n-s)(s+2)}<0.
 \tag{3.4}
\]

Therefore:

> **Theorem 3.1 (all-contrast uniform-slice class).**
> For every \(n,k\) and \(0\le c\le1\), the complete output entropy from a
> uniform \(k\)-subset input is concave in \(a\) on \([0,1-c]\).

This theorem was already available elsewhere in the package.  Its role here
is sharper: (2.5) identifies exactly how its high-contrast exchange sector
must be resummed.  If \(k_n/n\to\rho\), then from (3.1)--(3.2),

\[
 {1\over n}H(Y)\longrightarrow h(a+c\rho).
 \tag{3.5}
\]

The limiting posterior entropy obtained by the chain rule is consequently

\[
 h(\rho)+(1-\rho)h(a)+\rho h(1-a-c)-h(a+c\rho),
 \tag{3.6}
\]

which is finite per site for every fixed \(d\).  Formula (3.6) is the
all-cardinality counterpart of the single-layer saddle point (2.10).

## 4. A positive-density all-contrast Fourier class

Fix integers \(L\ge2\), \(m\ge1\), and put \(n=Lm\).  On the cyclic group
\(\mathbb Z/n\mathbb Z\), take the Fourier frequency comb

\[
 F_{L,m}=\{0,L,2L,\ldots,(m-1)L\}.
 \tag{4.1}
\]

Let \(P_{L,m}\) be its cyclic Fourier projection.  The geometric sum gives

\[
 (P_{L,m})_{xy}
 ={1\over n}\sum_{r=0}^{m-1}e^{2\pi iLr(x-y)/n}
 =\begin{cases}
  1/L,&x\equiv y\pmod m,\\
  0,&\text{otherwise}.
 \end{cases}
 \tag{4.2}
\]

After ordering the sites into the \(m\) classes modulo \(m\), this is a
direct sum of \(m\) copies of the rank-one projection \(J_L/L\).  Its DPP
therefore chooses one site uniformly and independently in each \(L\)-site
block.  The product channel preserves the block factorization.

> **Theorem 4.1 (Fourier-comb projection DPP).**
> For every \(L,m\) and every \(0\le c\le1\),
> \[
> a\longmapsto H(\operatorname{DPP}(aI+cP_{L,m}))
> \tag{4.3}
> \]
> is concave on \([0,1-c]\).  More exactly,
> \[
> {1\over Lm}H(\operatorname{DPP}(aI+cP_{L,m}))
> ={1\over L}F_{L,1,c}(a),
> \tag{4.4}
> \]
> where \(F_{L,1,c}\) is the uniform-singleton output entropy from Theorem
> 3.1.  Hence the normalized statement is exactly uniform in \(m\), at the
> fixed positive density \(1/L\).

The complement projection gives the same conclusion at density \(1-1/L\).
For \(L=2\), (4.2) is the half-density antipodal Fourier projection: its DPP
chooses one point independently from every antipodal pair.  Thus Theorem 4.1
is an all-contrast, half-density, equal-diagonal Fourier result in every even
dimension.  It is not the contiguous-frequency sine projection: its
correlations sit at distances of order the cycle size, so it supplies no
local stationary-sine limit.

## 5. Exact posterior closure for every projection DPP

The overlap resummation has a determinantal analogue.  Let \(P=VV^*\) be a
rank-\(k\) orthogonal projection, where \(V^*V=I_k\), and let its projection
DPP be the input.  For an output set \(T\), define the diagonal matrix

\[
 D_T(\theta)=I+(\theta-1)I_T.
 \tag{5.1}
\]

By (1.3), the posterior weight of a \(k\)-set \(S\) is proportional to

\[
 \det(P_S)\theta^{|S\cap T|}
 =\det\!\left[
 (D_T(\theta)^{1/2}PD_T(\theta)^{1/2})_S\right].
 \tag{5.2}
\]

Cauchy--Binet gives the exact normalizer

\[
 \sum_{|S|=k}\det(P_S)\theta^{|S\cap T|}
 =\det(V^*D_T(\theta)V)
 =\det(I_T+(\theta-1)P_T).
 \tag{5.3}
\]

Consequently:

> **Proposition 5.1 (posterior projection closure).**
> Conditional on the complete output \(Y=T\), the input is again a
> rank-\(k\) projection DPP.  Its kernel is
> \[
> Q_T=D_T^{1/2}V(V^*D_TV)^{-1}V^*D_T^{1/2}.
> \tag{5.4}
> \]

Equation (5.3) resums all input--output differences into a \(k\times k\)
determinant and is valid in every dimension.  Unlike the uniform-slice case,
however, the posterior entropy contains the geometry of the minors
\(\det(P_S)\).  It is not determined by \(|S\cap T|\).  Controlling the
curvature of the average entropy of (5.4), uniformly for contiguous Fourier
projections, is precisely the global information missing from a
difference-count argument.

## 6. A rigorous half-contrast barrier for the weighted local-row criterion

We use the notation of `stationary-weighted-energy-route.md`.  For a feasible
posterior two-site block

\[
 R_D=\begin{pmatrix}x&\xi\\\bar\xi&y\end{pmatrix},
 \qquad z=|\xi|^2\le\min\{xy,(1-x)(1-y)\},
 \tag{6.1}
\]

put \(q=a+cx\), \(r=a+cy\), \(s=c^2z\), and

\[
 \begin{array}{ll}
 p_{00}=(1-q)(1-r)-s,&p_{10}=q(1-r)+s,\\
 p_{01}=(1-q)r+s,&p_{11}=qr-s.
 \end{array}
 \tag{6.2}
\]

Let

\[
 \alpha_0=(1-a)(1-a-c),\qquad \alpha_1=a(a+c),
 \quad \beta_{ij}=\alpha_i\alpha_j,
 \tag{6.3}
\]

\[
 J=\sum_{u\in\{0,1\}^2}{\beta_u^2\over p_u^3},
 \qquad
 g=\Lambda(s)-s\Lambda'(s),
 \quad
 \Lambda(s)=\log{p_{10}p_{01}\over p_{11}p_{00}}.
 \tag{6.4}
\]

The local quantity used in that route is

\[
 W_u={g_+\beta_u\over zJp_u^2},
 \qquad \mathfrak W(a,c)=\sup\max_u W_u.
 \tag{6.5}
\]

Its sufficient condition for entropy concavity is \(\mathfrak W<16\).

> **Proposition 6.1 (endpoint divergence above one half).**
> For every fixed contrast \(1/2<c<1\),
> \[
>  \sup_{0<a<1-c}\mathfrak W(a,c)=+\infty.
> \tag{6.6}
> \]

**Proof.**  Fix \(c>1/2\), choose \(y\in(1/(2c),1)\), and put
\(r_0=cy>1/2\).  Fix \(\lambda>0\), let
\(a=\varepsilon\downarrow0\), and set

\[
 x=\lambda\varepsilon,\qquad z=\mu\varepsilon.
 \tag{6.7}
\]

where \(\mu>0\) will be chosen small.  If \(\mu<\lambda y\), then (6.1)
holds for all sufficiently small \(\varepsilon\).  Take \(u=10\), and define

\[
 M=1+c\lambda,\qquad \gamma=c^2\mu,\qquad
 A=M(1-r_0)+\gamma,\qquad B=Mr_0-\gamma.
 \tag{6.8}
\]

Then \(q=M\varepsilon\), \(r\to r_0\), \(s=\gamma\varepsilon\), and

\[
 {p_{10}\over\varepsilon}\longrightarrow A,
 \qquad {p_{11}\over\varepsilon}\longrightarrow B,
 \qquad p_{00}\to1-r_0,\quad p_{01}\to r_0.
 \tag{6.9}
\]

Choose \(\gamma>0\) small enough that \(A<B\).  Holding \(q,r\) fixed when
differentiating \(\Lambda\), equation (6.4) gives

\[
 g\longrightarrow G(\gamma)
 =\log{A r_0\over B(1-r_0)}
  -\gamma\left({1\over A}+{1\over B}\right).
 \tag{6.10}
\]

Here \(A\) and \(B\) depend affinely on \(\gamma\).  At \(\gamma=0\),
\(G(0)=0\), and direct differentiation gives

\[
 G'(\gamma)=\gamma\left({1\over A^2}-{1\over B^2}\right)>0
 \tag{6.11}
\]

as long as \(0<\gamma<M(2r_0-1)/2\), which is exactly the condition
\(A<B\).  Thus \(G(\gamma)>0\).  Choose
\(\mu=\gamma/c^2\) still smaller if necessary so that
\(\mu<\lambda y\).

Finally,

\[
 \alpha_0\to1-c,\qquad \alpha_1\sim c\varepsilon,
 \qquad
 J\sim {c^2(1-c)^2\over A^3}\,{1\over\varepsilon}.
 \tag{6.12}
\]

Combining (6.5), (6.7)--(6.12) yields

\[
 W_{10}\sim
 {G(\gamma)A\over\mu c(1-c)}\,{1\over\varepsilon}
 \longrightarrow+\infty.
 \tag{6.13}
\]

This proves (6.6).  \(\square\)

As an exact rational checkpoint, take

\[
 c={3\over5},\qquad \lambda=10,\qquad y={9\over10},
 \qquad \mu={9\over10}.
 \tag{6.14}
\]

For this choice,

\[
 G(\gamma)=\log{443\over368}-{2625\over14176}>0.
 \tag{6.15}
\]

Indeed, with \(t=75/368\), the alternating series for \(\log(1+t)\) gives

\[
 G(\gamma)>t-{t^2\over2}+{t^3\over3}-{t^4\over4}
       -{2625\over14176}
 ={8272631925\over32497877123072}>0.
 \tag{6.16}
\]

Equation (6.13) then specializes to
\(W_{10}\sim(443/27)G(\gamma)/\varepsilon\).

The feasible block (6.7) disproves neither finite nor stationary entropy
concavity.  It proves that the route which takes a supremum over every local
positive-contraction block before enforcing global compatibility cannot
reach any complete legal interval with \(c>1/2\).  Any successful
high-contrast argument must retain a global constraint linking many such
blocks, such as the common posterior projection
(5.4), translation invariance, or Fourier minor identities.

## 7. What remains for the contiguous sine projection

The exact results above separate the problem into two parts.

1. **Combinatorial proliferation is solved.**  Difference counts can be
   resummed exactly by (2.1) for the uniform slice and by the determinant
   (5.3) for every projection DPP.  The coefficient in (2.7) is therefore not
   itself evidence of positive entropy curvature.
2. **Spatial minor entropy is unsolved.**  For a contiguous Fourier
   projection, posterior probabilities within a fixed overlap layer are
   proportional to unequal minors \(\det(P_S)\).  Neither (2.5) nor the
   one-dimensional saddle point sees this variation.
3. **The unrestricted local supremum is too large.**  Proposition 6.1 rules
   out the direct extension of the current weighted local-row certificate to
   high contrast.

A sufficient new statement would be a volume-uniform curvature bound for

\[
 \mathbb E_T H(\operatorname{DPP}(Q_T)),
 \tag{7.1}
\]

with \(Q_T\) from (5.4), in which the output law of \(T\) and the Fourier
geometry are kept together.  Bounding each \(T\), each pair, or each exchange
order separately loses exactly the compatibility needed after Proposition
6.1.  Establishing the required bound for the contiguous half-density Fourier
projection would close the high-contrast sine branch; no such bound is proved
here.

## 8. Numerical evidence, kept separate from the proof

The analytic-jet program
`computations/stationary/stationary_fourier_probe.py` was run
through \(n=10\).  It checked 453 cyclic Fourier frequency sets, 20,385
offset-channel parameter points (including \(c=0.6,0.9,0.99\)), and 5,889
fixed-density resampling points.  No positive complete-entropy curvature was
found.  This is finite double-precision evidence only.  It is consistent with
the conjecture and does not repair the missing uniform bound (7.1).

## 9. Result ledger

- **PROVED:** exact all-order posterior resummation (2.1)--(2.5) for uniform
  fixed-cardinality input.
- **PROVED:** the thermodynamic overlap saddle point (2.8)--(2.10) and the
  resulting noncommutation of the small-noise and large-volume expansions.
- **PROVED, USING THE KNOWN SHEPP--OLKIN THEOREM:** all-contrast concavity for
  uniform fixed-cardinality inputs.
- **PROVED:** the positive-density cyclic Fourier-comb projection theorem,
  including half density for every even dimension and every contrast.
- **PROVED:** exact posterior projection closure (5.3)--(5.4).
- **PROVED ROUTE OBSTRUCTION:** for every \(c>1/2\), the weighted unrestricted
  local-row constant diverges at the channel endpoint; that sufficient
  condition cannot prove any full legal high-contrast interval.
- **NUMERICAL ONLY:** the finite Fourier screen through \(n=10\).
- **OPEN:** the volume-uniform spatial-minor entropy curvature for contiguous
  Fourier/sine projections, and hence every new stationary conclusion for
  \(c>1/2\).
