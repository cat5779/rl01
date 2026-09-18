# WEB_PRO_04 — High-contrast endpoint route with all-order posterior resummation

Read [COMMON.md](COMMON.md) first.

## Motivation

The final contrast range is \(0<c<1\). Small extensions of the current threshold do not by themselves explain the regime \(c\uparrow1\).

Use
\[
c=1-\varepsilon,\qquad a=\varepsilon t,
\qquad 0<t<1.
\]

Do not assume \(n\varepsilon\ll1\). Fixed-volume low-noise Taylor series are known to become nonuniform at positive density because the number of exchanges is order \(n\).

The repository already contains an exact all-orders hypergeometric resummation for the **uniform fixed-cardinality** input. That model is a guide and a comparison law, not the true contiguous Fourier projection.

## Single objective

Construct a volume-uniform, all-orders posterior comparison for the actual fixed-density contiguous Fourier projection and use it to prove a genuine high-contrast true-law concavity region.

A concrete first target is:

for every fixed \(\rho\in(0,1)\) and every fixed \(\delta\in(0,1/2)\), prove that there exists
\[
\varepsilon_0(\rho,\delta)>0
\]
such that for
\[
0<\varepsilon<\varepsilon_0,\qquad
t\in[\delta,1-\delta],
\]
the actual sine entropy rate is concave in \(a=\varepsilon t\), preferably with a quantitative Jensen margin.

It is acceptable to start with \(\rho=1/2\) if the method clearly retains the density parameter.

## Exact identity worth exploiting

For a projection-DPP input \(X\) of fixed size \(k\) passed through the copy/refresh channel, conditional independence gives an exact entropy ledger of the form
\[
H(Y)=H(X)
+(n-k)b(\varepsilon t)
+k\,b(\varepsilon(1-t))
-H(X\mid Y).
\]

The independent noise terms are explicit. The difficulty is the actual posterior entropy \(H(X\mid Y)\).

Build an all-order tool for the posterior rather than truncating by the number of exchange errors.

## Promising directions

Possible mechanisms:

- compare the true Fourier-minor posterior to the uniform-slice hypergeometric posterior by a spatial relative entropy or transport cost;
- derive a cluster/polymer representation whose **activity is volume-uniform after resummation** rather than termwise in the number of exchanges;
- exploit strong Rayleigh / stable-polynomial structure only where its exact hypotheses hold;
- prove a posterior entropy Jensen bound directly from a finite-volume variational principle.

Any comparison must retain actual Fourier minor weights. A statement about only the overlap count is insufficient unless the conditional spatial entropy defect is separately paid.

## Endpoint and parameter discipline

A theorem only for \(t\in[\delta,1-\delta]\) is useful, but keep the \(\delta\)-dependence explicit. State exactly what remains near \(t=0,1\).

Do not let \(\rho\) tend to zero with \(\varepsilon\) and call that a fixed-density theorem.

Do not replace the actual projection by a uniform \(k\)-slice unless the comparison error is proved at the needed Jensen scale.

## Success criterion

Best: a high-contrast theorem with \(c\) arbitrarily close to one at every fixed positive density and on a nondegenerate rescaled \(t\)-interval.

Useful partial: a new volume-uniform posterior comparison that converts the actual Fourier-minor problem to the known all-orders uniform-slice formula plus an explicit \(o(n)\) Jensen error.

A finite-\(n\) low-noise expansion without uniform remainder is not progress toward this task.
