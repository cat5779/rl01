# S18 round 2 latest certificate summary

Status: AUTHOR_SUBMISSION_PENDING_INDEPENDENT_REVIEW. Complete visible message recovered; attachment bodies for the new round-2 certificate are not recovered. This is the latest message; finite sizes do not imply all-volume or entropy-rate results.

---

# PRO02 Round 2 completed

The strongest unconditional result is now a **complete finite-volume negative-curvature certificate at the benchmark**, together with a rigorously positive first scale-doubling correction. It does **not** yet prove entropy-rate curvature.

The certificate uses the genuine finite sine Toeplitz law and the complete entropy Hessian. Every configuration is weighted by its actual atom probability, as required by the repository definitions. citeturn611742view2turn741728view1turn741728view2

## Deliverables

- :chatgpt-content-reference{index="4"}
- :chatgpt-content-reference{index="5"}
- :chatgpt-content-reference{index="6"}
- :chatgpt-content-reference{index="7"}
- :chatgpt-content-reference{index="8"}

## Main proved results

### Complete six-site certificate

At

\[
\rho=\frac12,\qquad c=\frac{19}{20},\qquad a_0=\frac1{40},
\]

the rigorous enclosure is

\[
\begin{aligned}
H_6''(a_0)\in[&
-49.5655212392509631975961954433188966659964420194298033311591578617869951322091733224295530,\\
&
-49.5655212392509631975961954433188966659964420194298033311591578600903842305248300179011682].
\end{aligned}
\]

Hence

\[
\boxed{H_6''(a_0)<-49.5655<0.}
\]

This is strengthened to a genuine neighborhood result:

\[
\boxed{
H_6''(a)<-2.9218741928215708<0
\quad
\text{for every }
a\in\left[\frac3{200},\frac7{200}\right].
}
\]

Thus the six-site entropy is strictly concave on the radius-\(1/100\) interval around the benchmark, at fixed \(c=19/20\).

### Complete six-coordinate Hessian

Giving every site an independent diagonal shift \(t_i\), the full \(6\times6\) entropy Hessian satisfies

\[
\boxed{
\lambda_{\max}\!\left(
[\partial_{t_i}\partial_{t_j}H_6]_{i,j=1}^{6}
\right)
\le
-4.28991641639140159594241758871650986469.
}
\]

Therefore the finite six-site entropy is locally strictly concave in **every sitewise diagonal direction**, not merely along the common-\(a\) direction.

A useful failure mechanism was also certified:

\[
\partial_{t_1}\partial_{t_6}H_6
>
0.000379092242041686.
\]

So the claim that all mixed entries are nonpositive is **DISPROVED**, even in the exact benchmark sine model. Negative definiteness comes from signed matrix-level cancellation, not from every pair being individually favorable.

### Complete twelve-site certificate

Using all \(2^{12}=4096\) true configurations,

\[
\begin{aligned}
H_{12}''(a_0)\in[&
-126.180128560707956002337296903765124238560242225063762032048899946591367124652864972749594,\\
&
-126.180128560707956002337296903765124238560242225063761643362508466514578457533798632841529].
\end{aligned}
\]

Thus

\[
\boxed{H_{12}''(a_0)<-126.1801<0.}
\]

For this theorem:

- the pair-cut tail is exactly zero;
- the observation-domain change is exactly zero;
- the endpoints are the actual finite Toeplitz endpoints;
- all 4096 words use their true probabilities;
- no stationary interior replacement or numerical differentiation is used.

This directly meets the follow-up’s accounting requirements for a finite-volume result. The assignment explicitly required that such a scope be stated rather than promoted to entropy-rate concavity. citeturn611742view0

## New exact multiscale mechanism

For two adjacent blocks of six sites, define their total correlation

\[
\operatorname{TC}_{6,6}(a)
=
H(Y_{1:6})+H(Y_{7:12})-H(Y_{1:12}).
\]

Stationarity and the exact marginal law give

\[
\operatorname{TC}_{6,6}(a)=2H_6(a)-H_{12}(a).
\]

The certified curvature is

\[
\begin{aligned}
\operatorname{TC}_{6,6}''(a_0)\in[&
27.0490860822060296071449060171273309065673581862041549810441927429405881931154519879824230,\\
&
27.0490860822060296071449060171273309065673581862041553697305842264105986636032049369472576].
\end{aligned}
\]

Therefore

\[
\boxed{\operatorname{TC}_{6,6}''(a_0)>27.0490.}
\]

This means that restoring the exact dependence between the two six-site blocks contributes **additional negative entropy curvature**:

\[
\frac{H_{12}''}{12}
=
\frac{H_6''}{6}
-
\frac{\operatorname{TC}_{6,6}''}{12},
\]

with a certified improvement exceeding

\[
\frac{27.0490}{12}>2.25409
\]

per site.

This is not an absolute boundary estimate or a renamed unpaid window term. It is the exact signed correlation correction, and its first nontrivial scale has been proved favorable.

## New reusable derivative tool

For a word \(y\), give each kernel diagonal an independent displacement \(t_i\), and let \(p_y(\mathbf t)\) be its exact determinant atom. With \(\sigma_i=2y_i-1\),

\[
\boxed{
\partial_{t_i}p_y
=
\sigma_i\,p_{-i}(y_{-i}),
}
\]

and, for \(i\neq j\),

\[
\boxed{
\partial_{t_i}\partial_{t_j}p_y
=
\sigma_i\sigma_j\,p_{-ij}(y_{-ij}),
\qquad
\partial_{t_i}^2p_y=0.
}
\]

Consequently,

\[
\partial_{t_i}\partial_{t_j}H_n
=
-\sum_y
\left[
\frac{(\partial_{t_i}p_y)(\partial_{t_j}p_y)}{p_y}
+
(\partial_{t_i}\partial_{t_j}p_y)\log p_y
\right].
\]

For the common shift,

\[
H_n''
=
-\sum_y
\left[
\frac{\left(\sum_i\sigma_i p_{-i}\right)^2}{p_y}
+
2\left(\sum_{i<j}\sigma_i\sigma_jp_{-ij}\right)\log p_y
\right].
\]

This reconstructs every derivative from compatible **actual marginals of the same finite law**. It avoids incompatible pair posteriors and numerical differentiation.

## Certification method

The proof script uses:

- rational alternating-series bounds in Machin’s formula for \(\pi\);
- directed `Decimal` rounding for all interval arithmetic;
- an explicit positive remainder bound for the atanh logarithm series;
- exact SymPy rational atom polynomials for \(n=6\);
- the finite Janossy identity
  \[
  p_S=\det(I-K)\det\!\left([K(I-K)^{-1}]_S\right)
  \]
  for \(n=12\);
- a verified inverse based on
  \[
  \|I-B(I-K)\|_\infty
  \le1.51725\times10^{-65}<1;
  \]
- interval \(LDL^*\) determinants, with the program aborting whenever a pivot lower bound is not strictly positive;
- exact atom marginalization for every first and mixed derivative.

The twelve-site probability intervals satisfy

\[
\sum_Sp_S
\in
[0.99999999999999999999999999999999999999999999999999999999578699,\,
 1.00000000000000000000000000000000000000000000000000000000421301].
\]

This normalization enclosure is diagnostic; the sign proof uses the individual outward-rounded atom and derivative intervals.

## Precise remaining obstruction

For \(N\) consecutive six-site blocks, define

\[
\operatorname{TC}_N(a)
=
NH_6(a)-H_{6N}(a).
\]

Then exactly,

\[
\frac{H_{6N}''(a)}{6N}
=
\frac{H_6''(a)}6
-
\frac{\operatorname{TC}_N''(a)}{6N}.
\]

A derivative-limit exchange is not needed if one proves a finite-chord statement. For

\[
\Delta_hF(a_0)
=
F(a_0+h)+F(a_0-h)-2F(a_0),
\]

the certified neighborhood gives

\[
\Delta_hH_6(a_0)
\le
-2.9218741928215708\,h^2,
\qquad 0<h\le\frac1{100}.
\]

Thus the explicit all-scale sufficient condition is

\[
\Delta_h\operatorname{TC}_N(a_0)\ge0
\quad
\text{for every }N\ge1,\ 0<h\le\frac1{100}.
\]

It would imply the entropy-rate chord bound

\[
\Delta_h h(a_0)
<
-0.4869790321369284\,h^2.
\]

Round 2 proves the infinitesimal \(N=2\) instance with margin \(27.0490\), but not this uniform all-scale chord condition. Therefore:

- finite \(n=6\) and \(n=12\) benchmark curvature: **PROVED**;
- first exact scale-doubling correction: **PROVED favorable**;
- thermodynamic entropy-rate curvature: **INCOMPLETE**.

This is materially beyond the old scoped result, whose review explicitly did not certify benchmark negative curvature or any large-window certificate. citeturn611742view1

## Preserved Round 1 artifacts

- :chatgpt-content-reference{index="9"}
- :chatgpt-content-reference{index="10"}
- :chatgpt-content-reference{index="11"}

These files were not overwritten or silently upgraded by the Round 2 conclusions.
