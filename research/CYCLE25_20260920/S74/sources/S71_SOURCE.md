# S69 / QWE08 — Incomplete proof checkpoint

**The requested all-size inequality for the actual path \(a\mapsto\operatorname{DPP}(aI+cQ)\) remains unresolved.** I have neither proved \(M_{m,n}''\ge 0\) for arbitrary adjacent blocks nor found a counterexample on that actual path. Consequently, this work does not establish half-density entropy-rate concavity throughout \(37/40<c<1\).

The rigorous progress is:

| Result | Status | Scope |
|---|---|---|
| Block mutual information is convex along a positive rank-one kernel line | **PROVED** | Every finite strict Hermitian-contraction DPP; every block partition |
| \(M_{1,1}''\) has an explicit, strictly positive, bias-uniform lower bound | **PROVED** | Actual half-density sine law; every \(0<c<1\), every legal \(a\) |
| Convexity of adjacent-block MI along the **affine mixture of endpoint sine laws** | **DISPROVED** | Exact bootstrap endpoints; adjacent blocks of length 20,000 suffice |
| Binary-entropy-compensated MI convexity along an affine mixture | **PROVED** | Arbitrary finite positive endpoint laws; dimension-free and sharp |
| A finite seed pays a boundary or transfer defect for the actual kernel-shift path | **INCOMPLETE** | No such payment has been established |
| The requested full high-contrast entropy-rate theorem | **INCOMPLETE** | No conclusion from the auxiliary-mixture results |

**Execution limitation.** The resumed tool calls did not return inspectable results. I therefore cannot verify the requested file packaging, numerical executions, or an elapsed-time measurement. I am not supplying unverified download links or presenting floating-point results as certificates. The readable mathematical report and an exact-arithmetic checker are provided below; the checker is marked **unexecuted in this deliverable**.

---

# RESULT.md

## 1. Required properties of the proposed tool

A successful block-information tool for this assignment must provide all of the following:

1. **Actual-law compatibility:** intermediate laws must be the stated finite DPPs, or a proved comparison must connect the auxiliary interpolation to them.
2. **Normalization and moving references:** the joint weights, marginal weights, and their derivatives must all be retained, including rare configurations.
3. **Signed curvature or chord payment:** a proved sign, or an explicit defect that a certified finite-volume seed actually pays.
4. **Size and parameter control:** a summable normalized accumulation, with explicit dependence on \(c,p\), throughout the claimed parameter set.

The first theorem below meets these requirements for **rank-one kernel lines**, but not for the identity-shift direction. The mixture theorem supplies an explicit compensated inequality for a different law. The missing comparison to the assigned path is not concealed.

Throughout,
\[
K_{a,c,N}=aI+cQ_{\rho,N},\qquad
0<a<1-c,\qquad a=(1-c)p.
\]
All entropy is full configuration Shannon entropy in nats.

For adjacent blocks \(A,B\) of lengths \(m,n\),
\[
M_{m,n}=I(Y_A;Y_B)=H_m+H_n-H_{m+n},
\]
and exactly
\[
M_{m,n}''=F_{m+n}-F_m-F_n,\qquad F_N=-H_N''.
\]

## 2. Finite-compression and normalization facts

For every finite vector \(z\),
\[
z^*Q_{\rho,N}z
=
\int_{-\rho/2}^{\rho/2}
\left|\sum_{j=1}^{N}z_je^{2\pi ij\theta}\right|^2\,d\theta.
\]
Thus \(0\preceq Q_{\rho,N}\preceq I\). This proves contraction, **not projection**.

Consequently,
\[
aI\preceq K_{a,c,N}\preceq(a+c)I,
\qquad
\delta:=\min(a,1-a-c)
=(1-c)\min(p,1-p)>0.
\]

For a configuration \(y\), let
\[
D_{\bar y}=\operatorname{diag}(1-y_i),\qquad
R_y=(K-D_{\bar y})^{-1}.
\]
Inclusion-exclusion gives the exact atom formula
\[
P_K(y)=(-1)^{N-|y|}\det(K-D_{\bar y}).
\]

If \(\delta I\preceq K\preceq(1-\delta)I\), then
\[
K-D_{\bar y}
=
\tfrac12\operatorname{diag}(2y_i-1)+(K-\tfrac12 I).
\]
The first summand has all singular values \(1/2\), and the second has norm at most \(1/2-\delta\). Therefore
\[
\|R_y\|\le\delta^{-1},
\qquad
\delta^N\le P_K(y)\le(1-\delta)^N.
\]
In particular, all finite-volume differentiations below include every configuration and are legitimate on compact subintervals of the legal parameter interval.

The non-elementary input in the next proof is **negative association of determinantal measures**: increasing functions supported on disjoint coordinate sets have nonpositive covariance under a Hermitian positive-contraction DPP. The original source is Russell Lyons, *Determinantal probability measures*, arXiv:math/0204325, Theorem 8.1, which states the stronger conditional negative-association property. The finite-function formulation follows from the event formulation by finite layer-cake decomposition. The hypothesis map here is precisely: finite ground set, Hermitian positive contraction, and disjoint increasing block-score functions.

## 3. An all-size rank-one block-information theorem

### Theorem 1

Let
\[
K(t)=K_0+t vv^*
\]
be a strict Hermitian contraction on an interval, and partition its ground set into disjoint blocks \(A_1,\ldots,A_r\). For the actual DPP law define
\[
\mathcal M(t)=\sum_{j=1}^rH(Y_{A_j};t)-H(Y;t).
\]
Then
\[
\boxed{\mathcal M''(t)\ge0.}
\]

If the contraction margin is at least \(\delta\), then
\[
0\le\mathcal M''(t)\le \|v\|^4\delta^{-2}.
\]

### Proof

**Affine atoms.** The rank-one determinant identity implies that every joint atom is affine in \(t\). Every marginal atom is also affine, because its kernel direction is \(v_{A_j}v_{A_j}^*\). Thus all atom second derivatives vanish.

The actual joint and marginal scores are
\[
S(y)=v^*R_yv,\qquad
S_j(y_{A_j})=v_{A_j}^*R^{A_j}_{y_{A_j}}v_{A_j}.
\]
Normalization and differentiation of the actual marginal sum give
\[
ES=ES_j=0,\qquad S_j=E[S\mid Y_{A_j}].
\]

**Increasing scores.** More generally, the score for any positive semidefinite kernel direction \(V\) is \(\operatorname{tr}(R_yV)\). Fix the other coordinates and flip \(y_i=0\) to \(1\). The determinant signs imply
\[
1+(R_0)_{ii}=-\frac{P(y_i=1,y_{-i})}{P(y_i=0,y_{-i})}<0.
\]
Sherman–Morrison gives
\[
R_1-R_0
=
-\frac{R_0e_ie_i^*R_0}{1+(R_0)_{ii}}
\succeq0.
\]
Its trace against \(V\succeq0\) is nonnegative. Hence the joint and marginal scores are increasing.

**Fisher superadditivity with actual weights.** Put
\[
J=ES^2,\quad J_j=ES_j^2,\quad s=\sum_jJ_j,\quad T=\sum_jS_j.
\]
Negative association gives
\[
ET^2=s+2\sum_{i<j}\operatorname{Cov}(S_i,S_j)\le s.
\]
The conditional-score identity gives \(E(ST)=s\). Consequently,
\[
s^2\le J\,ET^2\le Js,
\]
so \(J\ge s\).

For an affine probability family, \(H''=-J\). Applying this to the joint law and its marginals yields
\[
\mathcal M''=J-\sum_jJ_j\ge0.
\]
Finally,
\[
|S|\le \|v\|^2/\delta
\]
gives the stated upper bound. ∎

The integrated consequence is
\[
\operatorname{Gap}_{\lambda}H(Y)
\ge
\sum_j\operatorname{Gap}_{\lambda}H(Y_{A_j})
\]
along this rank-one path.

At a frozen sine base point, \(\|v\|=1\) and \(|t|\le\delta/2\) preserve a contraction margin \(\delta/2\). The curvature bound is then \(4/\delta^2\), independently of volume.

**Limitation:** \(dK/da=I\) has rank \(N\). Convexity in each rank-one coordinate direction does not establish convexity along their sum. The mixed-direction terms remain uncontrolled.

## 4. The actual two-site conjecture, uniformly in bias

### Theorem 2

Consider a strictly positive binary pair with common-shift marginals
\[
u=a+\alpha,\qquad v=a+\beta
\]
and fixed covariance \(-d\), \(d\ge0\). Its atoms are
\[
q_{11}=uv-d,\quad q_{00}=(1-u)(1-v)-d,
\]
\[
q_{10}=u(1-v)+d,\quad q_{01}=(1-u)v+d.
\]
Its mutual information is convex in \(a\), strictly so when \(d>0\).

### Proof

Holding the marginals fixed while differentiating in \(d\),
\[
I(a,0)=I_d(a,0)=0,\qquad
I_{dd}(a,d)=\sum_{x,y}\frac1{q_{xy}(a,d)}.
\]
Therefore
\[
I(a,d)=\int_0^d(d-r)\sum_{x,y}\frac1{q_{xy}(a,r)}\,dr.
\]

Every denominator remains positive. The mixed denominators have second derivative \(-2\) in \(a\), so their reciprocals are strictly convex. For the \(11\) atom,
\[
\partial_a^2\frac1{uv-r}
=
\frac{2[(u+v)^2-(uv-r)]}{(uv-r)^3}>0.
\]
The \(00\) atom has the same property after replacing \(u,v\) by \(1-u,1-v\). Differentiating under the finite positive integral proves the claim. ∎

### An explicit minimum at equal-marginal midpoint

For equal marginals \(u=v=t\), define
\[
C(d)=
\frac{2}{1/4-d}
+4\log\frac{1/4-d}{1/4+d}-8.
\]
Then
\[
I''(t,d)\ge C(d)>0\qquad(0<d<1/4).
\]

To verify the uniform minimum, the second derivative of \(1/(x^2-r)\) is
\[
g_r(x)=\frac{6x^2+2r}{(x^2-r)^3},
\]
and
\[
g_r''(x)=
\frac{24(5x^4+10rx^2+r^2)}{(x^2-r)^5}>0.
\]
Hence \(g_r(t)+g_r(1-t)\ge2g_r(1/2)\). Also,
\[
\partial_t^2\frac{2}{t(1-t)+r}
=
\frac4{[t(1-t)+r]^2}
+\frac{4(1-2t)^2}{[t(1-t)+r]^3}
\ge\frac4{(1/4+r)^2}.
\]
Integration establishes the midpoint minimum. Its strict positivity follows from
\[
C(0)=0,\qquad
C'(d)=\frac{4d}{(1/4-d)^2(1/4+d)}>0.
\]

For the actual half-density adjacent sine pair,
\[
t=a+c/2,\qquad d=c^2/\pi^2.
\]
All atoms are positive throughout \(0<c<1,\ 0<a<1-c\). Thus
\[
\boxed{M_{1,1}''(a)\ge C(c^2/\pi^2)>0}
\]
and
\[
F_2(a)\ge8+C(c^2/\pi^2).
\]
Every legal chord therefore satisfies
\[
\operatorname{Gap}_\lambda H_2
\ge
\frac{8+C(c^2/\pi^2)}2
\lambda(1-\lambda)(a_1-a_0)^2.
\]

This is an all-bias finite seed. **No all-size propagation inequality has been proved, so the seed is not claimed to pay an unknown boundary cost.**

## 5. A certified obstruction to affine endpoint interpolation

Fix distinct legal endpoints and define
\[
\overline P_\lambda=(1-\lambda)P_{a_0}+\lambda P_{a_1}.
\]
This is not the assigned intermediate law
\[
P_{a_\lambda}
=\operatorname{DPP}(a_\lambda I+cQ),
\qquad
a_\lambda=(1-\lambda)a_0+\lambda a_1.
\]

At half density, distinct same-parity sites are independent under every endpoint law because \(Q(i,j)=0\). Under the mixture,
\[
\operatorname{Cov}_{\overline P_\lambda}(Y_i,Y_j)
=
\lambda(1-\lambda)(a_1-a_0)^2>0.
\]
Thus negative association cannot be transferred from the endpoints to their mixture.

A stronger obstruction concerns **the full adjacent-block mutual information**, not merely a pair covariance.

### Theorem 3: label-redundancy bound

Let \(T\) be the binary endpoint label. For arbitrary endpoint laws,
\[
\begin{aligned}
&I_{\overline P_\lambda}(A;B)
-(1-\lambda)I_{P_0}(A;B)-\lambda I_{P_1}(A;B)\\
&\hspace{20mm}=I(T;A)+I(T;B)-I(T;A,B).
\end{aligned}
\]
If each block classifies \(T\) with error at most \(\epsilon\le1/2\), then
\[
\boxed{\operatorname{Gap}_\lambda M_{\mathrm{mixture}}
\ge h_b(\lambda)-2h_b(\epsilon).}
\]

Indeed, if \(E\) is the classification-error indicator, the label is determined by the block and \(E\). Hence
\[
H(T\mid A)\le H(E)\le h_b(\epsilon),
\]
and similarly for \(B\), while \(I(T;A,B)\le h_b(\lambda)\).

### True finite sine count variance, including leakage

At half density,
\[
\operatorname{Var}_a(N_L)
=L\,v(a,c)+c^2D_L,
\]
where
\[
v(a,c)=
(a+c/2)(1-a-c/2)-c^2/4
\]
and
\[
D_L=\operatorname{tr}(Q_L-Q_L^2).
\]
The exact boundary term is
\[
D_L=\frac2{\pi^2}
\left[
\sum_{\substack{1\le r<L\\r\ {\rm odd}}}\frac1r
+
L\sum_{\substack{r\ge L\\r\ {\rm odd}}}\frac1{r^2}
\right].
\]
This follows by expanding \(\operatorname{tr}Q_L^2\) by distances and applying Parseval to the half-interval indicator.

Integral comparison gives
\[
D_L\le\frac{\log L+4}{\pi^2}.
\]
For \(\Delta=a_1-a_0\), classification by the midpoint of the two block-count means therefore has error
\[
\epsilon_L\le
\frac4{L^2\Delta^2}
\left[
L\max_{t=0,1}v(a_t,c)
+\frac{c^2(\log L+4)}{\pi^2}
\right].
\]

### Exact bootstrap instance

Take
\[
\rho=\frac12,\quad c=\frac{19}{20},\quad
a_0=\frac1{50},\quad a_1=\frac3{100},\quad
\lambda=\frac12,\quad L=20000.
\]
These correspond to \(p_0=2/5,\ p_1=3/5\). Both endpoint bulk count variances equal
\[
v(a_t,c)=\frac{487}{20000}.
\]
Using \(\pi>3\) and \(\log20000<10\),
\[
\operatorname{Var}_{a_t}(N_L)
<
487+\frac{361}{400}\frac{14}{9}
=\frac{879127}{1800}.
\]
Since \(L^2\Delta^2=40000\),
\[
\epsilon_L<
\frac{879127}{18000000}<\frac1{20}.
\]
Moreover,
\[
h_b(1/20)<1/5,\qquad \log2>1/2.
\]
The first inequality follows from \(\log20<3\) and
\[
-\frac{19}{20}\log(19/20)<\frac1{20};
\]
the second follows by integrating \(1/x>1/2\) on \([1,2)\).

Consequently,
\[
\boxed{
\operatorname{Gap}_{1/2}
I_{\overline P_\lambda}(Y_{1:L};Y_{L+1:2L})
>\frac1{10}\ {\rm nat}.
}
\]

**Exact scope:** the endpoints are the actual 40,000-site sine laws. The midpoint is their affine mixture. This disproves MI convexity on that interpolation, including on the bootstrap endpoints. **It does not disprove MI convexity on the actual kernel-shift interpolation.**

### Every nontrivial chord has such an obstruction

For any finite DPP contraction,
\[
\operatorname{Var}(N_L)=\operatorname{tr}K_L(I-K_L)\le L/4.
\]
Thus \(\epsilon_L\le1/(L\Delta^2)\).

Set \(\alpha=\min(\lambda,1-\lambda)\). An explicit sufficient size is
\[
L\ge
\left\lceil\frac{16}{\alpha\Delta^2}\right\rceil
=
\left\lceil
\frac{16}{\alpha(1-c)^2(p_1-p_0)^2}
\right\rceil.
\]
Then \(\epsilon_L\le\alpha/16\) and
\[
2h_b(\alpha/16)<h_b(\alpha)=h_b(\lambda).
\]
For example, this last comparison follows from
\[
h_b(x)\le x(\log(1/x)+1),\qquad
h_b(\alpha)\ge\alpha\log(1/\alpha),
\]
and \(7\log(1/\alpha)>4\log2+1\) for \(\alpha\le1/2\).

Thus the **mixture obstruction** covers every nontrivial legal chord, with explicit divergence as \(c\uparrow1\), the biases coalesce, or the mixing weight approaches an endpoint. This is not coverage of the original curvature conjecture.

## 6. A sharp compensated repair for mixtures

### Theorem 4

For arbitrary fixed positive finite endpoint laws,
\[
\boxed{\lambda\mapsto I_{\overline P_\lambda}(A;B)-h_b(\lambda)
\quad\text{is convex}.}
\]

For \(r\) blocks, their total correlation minus \((r-1)h_b(\lambda)\) is convex.

### Proof

All observed atoms are affine. Let \(J,J_A,J_B\) be their Fisher informations in \(\lambda\). Conditional expectation of scores implies
\[
J\ge\max(J_A,J_B).
\]
The complete-data label score is
\[
U(T)=\frac{T}{\lambda}-\frac{1-T}{1-\lambda},
\qquad EU^2=\frac1{\lambda(1-\lambda)}.
\]
Every observed score is a conditional expectation of \(U\), so
\[
J_A,J_B\le\frac1{\lambda(1-\lambda)}.
\]
Therefore
\[
M''=J-J_A-J_B
\ge-\frac1{\lambda(1-\lambda)}
=h_b''(\lambda).
\]
The multi-block version follows by retaining the largest block Fisher term and bounding the remaining \(r-1\) terms. ∎

Its finite-chord form is
\[
\operatorname{Gap}_\lambda M_{\mathrm{mixture}}\le h_b(\lambda).
\]
The coefficient one is sharp: in Theorem 3, both blocks identify the label with vanishing error as their lengths grow, so the mixture MI chord gap converges to \(h_b(\lambda)\).

### A valid thermodynamic consequence—only for mixtures

Exactly,
\[
H_N(\overline P_\lambda)
=(1-\lambda)H_N(P_0)+\lambda H_N(P_1)+I(T;Y_{1:N}),
\]
with
\[
0\le I(T;Y_{1:N})\le h_b(\lambda).
\]
Division by \(N\) gives
\[
h(\overline P_\lambda)
=(1-\lambda)h(P_0)+\lambda h(P_1)
\]
whenever the endpoint rates exist. This is an entropy-value argument, with error at most \(h_b(\lambda)/N\), and no differentiation of an \(o(N)\) term.

It does not establish a statement about \(h(a_\lambda)\) for the actual kernel-shift law.

## 7. The precise unpaid term in the actual problem

For any smooth normalized finite law, write
\[
S=P'/P,\qquad
\ell=\log\frac{P}{P_AP_B}.
\]
Differentiation with the joint and marginal references moving gives
\[
M''
=
\underbrace{ES^2-ES_A^2-ES_B^2}_{\text{Fisher defect}}
+
\underbrace{\sum_yP''(y)\ell(y)}_{\text{acceleration term}}.
\]

For the actual identity shift,
\[
S(y)=\operatorname{tr}R_y,
\]
\[
P''(y)
=
P(y)\left[(\operatorname{tr}R_y)^2-\operatorname{tr}(R_y^2)\right].
\]
The score-monotonicity argument proves that the Fisher defect is nonnegative. It does not sufficiently bound the second term.

The exact remaining inequality is therefore
\[
\begin{aligned}
&\sum_yP_{a,c,m+n}(y)
\left[(\operatorname{tr}R_y)^2-\operatorname{tr}(R_y^2)\right]
\log\frac{P_{a,c,m+n}(y)}
{P_{a,c,m}(y_A)P_{a,c,n}(y_B)}\\
&\hspace{25mm}\ge
-\bigl(J_{m+n}-J_m-J_n\bigr),
\end{aligned}
\]
or an affordable integrated boundary replacement, throughout the stated parameter domain.

**This is an equivalent unresolved signed term—not a new weaker lemma and not progress obtained by renaming a remainder.** No finite-seed payment, S67 Fisher threshold, derivative-limit identification, or Fekete/Dini shortcut is assumed.

## 8. Parameter and execution ledger

| Object | Explicit dependence | Limitation |
|---|---|---|
| Finite sine contraction margin | \(\delta=(1-c)\min(p,1-p)\) | Deteriorates at legal-boundary limits |
| Unit-norm rank-one perturbation | \(|t|\le\delta/2\); curvature at most \(4/\delta^2\) | Different kernel direction |
| Actual two-site curvature | \(C(c^2/\pi^2)>0\) | No all-size propagation |
| Bootstrap mixture obstruction | \(c=19/20,\ a_0=1/50,\ a_1=3/100,\ L=20000\) | Midpoint is not the actual sine DPP |
| General mixture obstruction | \(L\ge\lceil16/[\alpha(1-c)^2(p_1-p_0)^2]\rceil\) | Covers the auxiliary-mixture obstruction only |
| Mixture compensation | \(h_b(\lambda)\), independent of block sizes | No established transfer to actual kernel shift |
| Original rate problem | No proved affordable defect constant | **INCOMPLETE** |

No floating-point diagnostic is used as evidence for a theorem in this checkpoint. Earlier numerical explorations are not presented as retained or regenerated artifacts. The finite obstruction above is analytic; its elementary rational comparisons can be checked by the following source.

## 9. Exact-arithmetic checker

**Execution status: not verified in this deliverable.** The program uses no floating-point arithmetic in its asserted inequalities.

```python
#!/usr/bin/env python3
"""Exact checks for the AFFINE-MIXTURE obstruction, not the actual kernel path."""

from fractions import Fraction as F
from math import factorial
import json


def positive_exp_partial_sum(x: int, degree: int) -> F:
    return sum(
        (F(x**k, factorial(k)) for k in range(degree + 1)),
        F(0),
    )


def main() -> None:
    c = F(19, 20)
    a0, a1 = F(1, 50), F(3, 100)
    rho, weight = F(1, 2), F(1, 2)
    block_length = 20000
    delta = a1 - a0

    assert 0 < a0 < a1 < 1 - c

    mean0, mean1 = a0 + c * rho, a1 + c * rho
    variance_bulk0 = mean0 * (1 - mean0) - c * c / 4
    variance_bulk1 = mean1 * (1 - mean1) - c * c / 4
    assert variance_bulk0 == variance_bulk1 == F(487, 20000)

    # Positive Taylor remainders then prove log(20)<3 and log(20000)<10.
    assert positive_exp_partial_sum(3, 8) > 20
    assert positive_exp_partial_sum(10, 21) > 20000

    # Analytic ingredients in the report:
    # pi>3 and D_L <= (log(L)+4)/pi^2 < 14/9.
    variance_upper = (
        block_length * variance_bulk0 + c * c * F(14, 9)
    )
    error_upper = (
        4 * variance_upper / (block_length**2 * delta**2)
    )

    assert variance_upper == F(879127, 1800)
    assert error_upper == F(879127, 18000000)
    assert error_upper < F(1, 20)

    # The report proves log(2)>1/2 and hb(1/20)<1/5.
    gap_lower = F(1, 2) - 2 * F(1, 5)
    assert gap_lower == F(1, 10)

    pair_covariance = weight * (1 - weight) * delta**2
    assert pair_covariance == F(1, 40000)

    print(json.dumps({
        "object": "Affine mixture of actual endpoint sine laws",
        "not_the_object": "Actual intermediate kernel-shift DPP",
        "block_lengths": [block_length, block_length],
        "count_variance_strict_upper": str(variance_upper),
        "classification_error_strict_upper": str(error_upper),
        "MI_chord_gap_strict_lower_nats": str(gap_lower),
        "same_parity_covariance_in_mixture": str(pair_covariance),
        "original_all_size_conjecture": "UNRESOLVED",
    }, indent=2))


if __name__ == "__main__":
    main()
```

## 10. Resumption boundary

The useful retained ingredients are the all-size **rank-one** theorem, the actual all-bias **two-site** lower bound, and the exact finite adjacent-block ob
