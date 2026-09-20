# QWE08 — Adjacent-block mutual-information curvature

**Status: INCOMPLETE for the all-block target; PROVED for a reusable rank-one bipartite class and for the certified finite continuum box below.**

This result concerns the true finite sine-Toeplitz DPP
\[
K_n(a)=aI_n+cQ_{1/2,n},\qquad c=19/20,
\]
with full spatial-configuration Shannon entropy.  No cyclic projection, count entropy, spectral entropy, or frozen output law is substituted for the true law.  The target quantity is
\[
M_{m,n}(a)=H_m(a)+H_n(a)-H_{m+n}(a)
          =I(Y_{[m]};Y_{[m+1,m+n]}),
\]
so
\[
M_{m,n}''(a)=F_{m+n}(a)-F_m(a)-F_n(a),\qquad F_j=-H_j''.
\]

The full claim `M_{m,n}'' >= 0` for every `m,n` on `[.02,.03]` is **not proved or refuted here**.  The main new outputs are:

1. a complete parameter-convexity theorem for every finite common-shift DPP whose off-diagonal part is rank-one bipartite, with an explicit positive curvature lower bound;
2. its application to every true half-density sine block of total size at most three, for every `0<c<1` and every legal `0<a<1-c`;
3. an exact four-site true-sine obstruction showing that the natural coefficientwise/nonnegative-multigraph extension of that theorem fails already at size four;
4. a reusable exact common-shift probability operator and a rigorous interval/Taylor certificate proving the requested true-sine convexity on the full continuum `a in [1/50,3/100]` for every adjacent split with `m+n <= 4`;
5. the correct finite-chord interface to the true entropy-rate limit, avoiding the invalid identification `-h''=lim F_n/n`.

The finite certificate is reproducible from `QWE08_checks/certify_qwe08.py`; it does not use hashes/checksums as acceptance gates.

---

## 1. Frozen model and the legal rate interface

For a stationary finite-alphabet process,
\[
h(a)=\lim_{N\to\infty}\frac{H_N(a)}N
\]
exists as the usual entropy rate.  If one had, on a whole parameter interval,
\[
M_{m,n}''(a)\ge0\quad\text{for all }m,n,
\]
then for any fixed chord `a0,a1` and `0<lambda<1`, defining
\[
\operatorname{Gap}_\lambda f
=f((1-\lambda)a_0+\lambda a_1)
 -(1-\lambda)f(a_0)-\lambda f(a_1),
\]
convexity of `M` gives
\[
\operatorname{Gap}_\lambda H_{m+n}
\ge \operatorname{Gap}_\lambda H_m+
    \operatorname{Gap}_\lambda H_n.
\]
Thus the sequence `G_N=Gap H_N` is superadditive.  Fekete then gives
\[
\lim_{N\to\infty}\frac{G_N}{N}=\sup_N\frac{G_N}{N}.
\]
But the left side is directly
\[
\operatorname{Gap}_\lambda h,
\]
because `H_N(a)/N -> h(a)` at the three fixed chord points.  Hence
\[
\boxed{\operatorname{Gap}_\lambda h
\ge \frac1r\operatorname{Gap}_\lambda H_r}
\]
for every finite seed `r`.  In particular, an interval-uniform finite negative-curvature seed would pass to a true entropy-rate chord without differentiating the entropy-rate limit.

This is the only infinite-volume passage used below.  No statement of the form
\[
-h''=\lim_N F_N/N
\]
is assumed or needed.

---

## 2. A reusable rank-one bipartite convexity theorem

### Theorem 2.1

Let a finite index set be partitioned as `E sqcup O`, and let
\[
B=\begin{pmatrix}0&C\\ C^*&0\end{pmatrix},\qquad \operatorname{rank}C\le1.
\]
For
\[
K(t)=tI+B
\]
assume
\[
\sigma:=\|C\|_{\rm op}<t<1-\sigma.
\]
Let `P_t=DPP(K(t))`.  For any partition of the coordinates `V=A sqcup A^c`,
\[
t\longmapsto I_{P_t}(Y_A;Y_{A^c})
\]
is convex.  If at least one nonzero matrix entry of `C` crosses the `A|A^c` cut, it is strictly convex.

More explicitly, with `v=t(1-t)`,
\[
\boxed{
\frac{d^2}{dt^2}I(Y_A;Y_{A^c})
\ge
\sum_{\substack{e\in E,o\in O\\ e,o\text{ on opposite sides of the cut}}}
|C_{eo}|^4
\left[
\frac{3(1-2t)^2}{v^4}+\frac{2}{v^3}
\right].}
\]

### Proof

Let `q_t` be the product Bernoulli(`t`) law, and define
\[
\xi_i=\frac{Y_i-t}{t(1-t)}=
\begin{cases}
1/t,&Y_i=1,\\
-1/(1-t),&Y_i=0.
\end{cases}
\]
For a word `y`, the complete DPP atom is
\[
p_t(y)=(-1)^{\#\{i:y_i=0\}}
\det(K(t)-D_{1-y}).
\]
Factoring the diagonal matrix with entries `t` on occupied sites and `-(1-t)` on holes gives the exact density identity
\[
\frac{dP_t}{dq_t}(y)
=
\det(I+\operatorname{diag}(\xi(y))B).
\]

Every nonzero principal minor of a bipartite matrix uses the same number of vertices from `E` and `O`.  Since `rank C <= 1`, every balanced minor of order at least four vanishes.  Therefore
\[
\frac{dP_t}{dq_t}=1-U,
\qquad
U=\sum_{e,o}|C_{eo}|^2\xi_e\xi_o.
\]
Because rank one gives
\[
\sum_{e,o}|C_{eo}|^2=\|C\|_{\rm HS}^2=\sigma^2,
\]
and `|xi_i| <= 1/min(t,1-t)`, the strict-contraction hypothesis yields `|U|<1` pointwise.  Also `E_q U=0`.  Hence
\[
D(P_t\|q_t)
=E_q[(1-U)\log(1-U)]
=\sum_{k\ge2}\frac{E_q U^k}{k(k-1)}.
\tag{2.1}
\]

Expand `U^k`.  A monomial is encoded by a bipartite multigraph with `k` edges.  Its nonnegative edge weight is multiplied by
\[
\prod_i\mu_{d_i}(t),
\qquad
\mu_r(t)=E_q\xi_i^r
=t^{1-r}+(-1)^r(1-t)^{1-r},
\]
where `d_i` is the degree of vertex `i` in the multigraph.

Set `x=2t-1`.  For every even `r>=2`, `mu_r` has a power series in `x` with only even powers and nonnegative coefficients.  For every odd `r>=3`, it has only odd powers and nonpositive coefficients; `mu_1=0`.  The number of odd-degree vertices of any finite graph is even.  Consequently every nonzero multigraph contribution to (2.1) is an even power series in `x` with nonnegative coefficients.

Now use
\[
I(Y_A;Y_{A^c})
=D(P_V\|q_V)-D(P_A\|q_A)-D(P_{A^c}\|q_{A^c}).
\tag{2.2}
\]
The marginal kernels are the corresponding principal submatrices of `K(t)`, hence have the same rank-one bipartite form.  In (2.2), every multigraph lying wholly inside `A` or wholly inside `A^c` cancels exactly.  What remains is the sum of multigraphs touching both sides of the cut.  Every remaining term is still an even power series in `x` with nonnegative coefficients.

The expansions converge normally on compact subsets of `sigma<t<1-sigma`: the pointwise bound `|U|<1` is uniform there, so (2.1) and its differentiated power series may be summed termwise.  Since `x` is affine in `t`, the second derivative is nonnegative.

For strictness, retain only the `k=2` term consisting of the same crossing edge used twice.  Since
\[
\mu_2(t)=\frac1{t(1-t)}=v^{-1},
\]
that contribution is
\[
\frac12 |C_{eo}|^4v^{-2}.
\]
Its second derivative is
\[
|C_{eo}|^4
\left[
\frac{3(1-2t)^2}{v^4}+\frac2{v^3}
\right]>0.
\]
All omitted contributions have nonnegative second derivative.  Summing over crossing nonzero edges proves the displayed bound and strict convexity.  ∎

---

## 3. Consequence for the true half-density sine kernel

At half density,
\[
K_n(a)=\left(a+\frac c2\right)I_n
+c\left(Q_{1/2,n}-\frac12I_n\right).
\]
After reordering by parity, the off-diagonal part is bipartite.  For `n<=3`, one parity class contains at most one site, so the bipartite cross block has rank at most one.  Since the true sine compression satisfies `0<Q_{1/2,n}<I`, every legal
\[
0<c<1,\qquad 0<a<1-c
\]
gives a strict contraction.

Every adjacent nontrivial split of a two- or three-site consecutive block is crossed by a nonzero odd-distance sine entry.  Therefore Theorem 2.1 gives
\[
\boxed{M_{m,n}''(a)>0
\quad\text{for all }m,n\ge1,\ m+n\le3,\ 0<c<1,\ 0<a<1-c.}
\]
This is a genuine true-Toeplitz statement and is not restricted to `c=19/20`.

---

## 4. Exact four-site obstruction to coefficientwise positivity

The proof above suggests a tempting extension: expand `f log f` into multigraph monomials and prove every term nonnegative after taking Bernoulli moments.  This stronger mechanism already fails for the true four-site half-density sine kernel.

After parity reordering `E={1,3}`, `O={2,4}`, its bipartite block is
\[
C=s\begin{pmatrix}1&-1/3\\1&1\end{pmatrix},
\qquad s=c/\pi.
\tag{4.1}
\]
For a general real matrix
\[
C=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix},
\]
the density polynomial has the form
\[
f=1-
(\alpha^2x_1y_1+\beta^2x_1y_2+
 \gamma^2x_2y_1+\delta^2x_2y_2)
+(\alpha\delta-\beta\gamma)^2x_1x_2y_1y_2.
\]
Using
\[
(1+u)\log(1+u)
=u+\sum_{k\ge2}\frac{(-1)^ku^k}{k(k-1)},
\]
a direct coefficient extraction gives
\[
[x_1^3x_2^2y_1^2y_2^3](f\log f)
=
\alpha^2\beta^3\gamma\delta^2
(2\alpha\delta+3\beta\gamma).
\tag{4.2}
\]
For completeness, writing
\[
w_1=\alpha^2,\quad w_2=\beta^2,\quad
w_3=\gamma^2,\quad w_4=\delta^2,\quad
V=(\alpha\delta-\beta\gamma)^2,
\]
the same coefficient before simplification is
\[
\frac12w_2^3w_3^2
+3w_1w_2^2w_3w_4
+\frac32w_1^2w_2w_4^2
-Vw_2^2w_3-2Vw_1w_2w_4+\frac12V^2w_2,
\]
which factors exactly as (4.2).

Substituting (4.1) yields
\[
\boxed{
[x_1^3x_2^2y_1^2y_2^3](f\log f)
=-\frac{s^{10}}{27}<0.}
\tag{4.3}
\]

This is a model-valid obstruction, not a counterexample to mutual-information convexity.  After expectation under the Bernoulli reference the associated moment factor is
\[
\mu_3(t)^2\mu_2(t)^2\ge0,
\]
so this term is genuinely negative and must be compensated by other terms if the full curvature is positive.  Therefore any extension of Theorem 2.1 beyond rank one must use a grouping, resummation, or compensation inequality; raw termwise positivity is false already on the true four-site sine compression.

---

## 5. Exact common-shift probability operator

A second reusable tool is independent of the rank-one theorem.

Let `p_a(y)` be the full configuration probabilities of any finite DPP with `K(a)=K_*+aI`.  For coordinate `i`, let `y^i` be the word with bit `i` flipped and define
\[
(D_i p)(y)=(2y_i-1)\,[p(y)+p(y^i)],
\qquad D=\sum_iD_i.
\]
Differentiating the atom determinant with respect to the common diagonal shift gives
\[
\boxed{p_a'=Dp_a.}
\tag{5.1}
\]
The operators `D_i` commute and satisfy `D_i^2=0`, hence on `n` bits
\[
D^{n+1}=0.
\]
Therefore for every center `a_*`, the complete moving law is exactly the degree-`n` polynomial
\[
\boxed{
p_{a_*+z}
=\sum_{k=0}^{n}\frac{z^k}{k!}D^kp_{a_*}.}
\tag{5.2}
\]
This retains all probability acceleration and all rare words.  It is the algebraic core of the finite continuum certificate below.

---

## 6. Rigorous continuum certificate for `m+n <= 4`

Freeze
\[
\rho=\frac12,\qquad c=\frac{19}{20},\qquad
I=[1/50,3/100],\qquad a_*=1/40.
\]
The program `QWE08_checks/certify_qwe08.py` performs outward-rounded fixed-point interval arithmetic with denominator `2^256`.  It recomputes every atom and every Taylor coefficient on each run.  Saved JSON is output evidence only and is never an acceptance gate.

### 6.1 Analytic radius and entropy bound

Put
\[
\delta=1/40,\qquad R=1/50,\qquad r=1/200.
\]
At the center, the true kernel obeys
\[
\delta I\preceq K_n(a_*)\preceq(1-\delta)I.
\]
For a word `y`, let
\[
A_y=K_n(a_*)-D_{1-y}.
\]
By eigenvalue monotonicity, every eigenvalue of `A_y` has absolute value at least `delta`.  Hence every atom polynomial has no zero for `|z|<delta`, so the logarithm branch through the real positive atom is analytic there.

On `|z|=R`, factor the atom determinant through `A_y`.  Since `R/delta=4/5`,
\[
|p_y(a_*+z)|
\le p_y(a_*)\left(1+\frac R\delta\right)^n
=p_y(a_*)\left(\frac95\right)^n.
\]
Also every eigenvalue factor in the logarithmic ratio stays in the disk centered at one with radius `4/5`, giving
\[
|\log p_y(a_*+z)|
\le -\log p_y(a_*)+n\log5.
\]
Summing and using `H_n(a_*)<=n log 2` gives
\[
\boxed{|H_n(a_*+z)|\le
B_n:=n(9/5)^n\log10.}
\tag{6.1}
\]

At half density, complementation combined with the alternating diagonal gauge gives
\[
H_n(a_*+z)=H_n(a_*-z),
\]
so all odd Taylor coefficients vanish.

### 6.2 Cauchy tail

Write
\[
M_{m,n}(a_*+z)=\sum_{j\ge0}b_{2j}z^{2j}.
\]
Truncate through order `2L`, with `L=12`, and set
\[
\tau=(r/R)^2=1/16,\qquad k=L+1.
\]
Cauchy's bound from (6.1), summed over the three entropies, gives the following uniform remainder for the second derivative on `|z|<=r`:
\[
\begin{aligned}
T_{m,n}={}&
\frac{B_m+B_n+B_{m+n}}{R^2}\tau^L\\
&\times\left[
\frac{4k^2-2k}{1-\tau}
+\frac{(8k-2)\tau}{(1-\tau)^2}
+\frac{4\tau(1+\tau)}{(1-\tau)^3}
\right].
\end{aligned}
\tag{6.2}
\]
Thus it suffices to certify
\[
b_4,b_6,\ldots,b_{24}\ge0,
\qquad 2b_2-T_{m,n}>0.
\tag{6.3}
\]

The code computes the exact law polynomial from (5.2), obtains entropy coefficients by formal power-series division/logarithm inside interval arithmetic, verifies complement symmetry, and then checks (6.3) for every adjacent split.

### 6.3 Certified result

The exact command is

```bash
python QWE08_checks/certify_qwe08.py --max-n 4 --order 24
```

A fresh rerun produced

```text
n 1 F(mid) [4, 4] higher_even_H_negative True
n 2 F(mid) [9.5454670142325, 9.5454670142325] higher_even_H_negative True
n 3 F(mid) [17.907876884449, 17.907876884449] higher_even_H_negative True
n 4 F(mid) [27.423750308635, 27.423750308635] higher_even_H_negative True
All adjacent splits certified; minimum lower enclosure:
[1.5454668697424313269, 1.5454668697424313269]
```

Therefore
\[
\boxed{
M_{m,n}''(a)>1.5454668697424
}
\]
for every `a in [1/50,3/100]` and every adjacent split with `m+n<=4`.

The certificate is a continuum proof, not a grid scan.  The JSON file records the integer interval endpoints and even Taylor coefficient enclosures used by the check.

---

## 7. Falsification attempts and boundaries

The independent packet audit already reports broad floating-point true-Toeplitz probes with no finite counterexample, but those probes are not used as proof.  The present work additionally found the exact four-site negative coefficient (4.3), which kills the strongest obvious coefficientwise route.

Two other tempting routes remain invalid:

* finite Toeplitz half-density conditionals are contractions, not projections; projection identities from cyclic or infinite parity models cannot be inserted without leakage terms;
* superadditivity of `F_n` would give a Fekete limit of `F_n/n`, but by itself does not identify that limit with `-h''`.  The valid route is the finite chord argument in Section 1.

The existing dimension-free QWE02 bound controls `|M_{m,n}''|` by cross-boundary Hilbert--Schmidt energy on a gapped interval, but at the frozen small gap its `delta^{-12}` constant is far too large to pay the positive finite seeds here.  It is therefore an asymptotic response tool, not a sign closure for QWE08.

---

## 8. Smallest remaining inequality

The unresolved load-bearing statement is still
\[
\boxed{M_{m,n}''(a)\ge0
\quad\text{for all }m,n\ge1,
\ a\in[1/50,3/100]}
\tag{8.1}
\]
for the true sine-Toeplitz law at `rho=1/2,c=19/20`.

The rank-one proof shows exactly what fails at size four: determinant-loop terms create negative multigraph coefficients.  A successful all-size proof must therefore establish a compensation inequality after grouping those loop terms.  Equivalently, one needs a signed average inequality strong enough to dominate the explicit negative coefficient family, while preserving the moving-law Fisher and probability-acceleration terms.

A weaker result sufficient for the entropy-rate goal would be an almost-superadditive finite-chord inequality
\[
\operatorname{Gap}H_{m+n}
\ge \operatorname{Gap}H_m+\operatorname{Gap}H_n-e_{m,n}
\]
whose aggregate defect along a tiling/dyadic scheme is sublinear or summable with an explicit constant small enough to be paid by a finite certified seed.  A generic `O(m+n)` defect is not enough.

---

## 9. Dependency and scope ledger

**Used from the packet:** the frozen model, the independently audited warning that adjacent-block MI curvature is unproved, the true entropy-rate/value-limit interface, and the distinction between true Toeplitz and cyclic/infinite projection models.

**Not imported as a theorem:** any author-only finite monotonicity observation, any fitted convergence exponent, any claim that `Gamma_n=F_n/n` is monotone, or any derivative exchange at the entropy-rate limit.

**New here:** Theorem 2.1 and its proof; the true four-site coefficient obstruction (4.3); the exact common-shift probability operator (5.1)-(5.2); and the finite continuum certificate implementation/proof interface in Section 6.

**Final status:** `INCOMPLETE` for the all-size adjacent-block convexity and the resulting full entropy-rate interval conclusion.  The finite and rank-one statements above are proved within their stated scope.