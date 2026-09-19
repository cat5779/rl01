# S72 handoff: the verified QWE09 interface

This page distills the completed Cycle22 audit. It is not a new proof and does
not enlarge the accepted parameter range.

## Exact interface

On a compact legal interval (J\subset(0,1-c)), the gap and constants are

\[
\delta=\min_{a\in J}\min\{a,1-a-c\},\qquad
\kappa=\frac{c^2}{4\delta(\delta+c)},\qquad
r_\delta=\frac{1-\delta}{\delta},
\]

\[
C_H=\max\!\left\{2+7(1+\kappa)\bar\kappa r_\delta^2,
14(1+\kappa)\bar\kappa\right\},\qquad
\Lambda=\frac{C_H}{2},
\]

where \(\bar\kappa=\max\{1,\kappa\}\), and

\[
\tau(R)=\min\!\left\{\delta^{-2},
\frac{2c^2}{\pi^2\delta^4}\frac{H_{R-1}+2}{R}\right\}.
\]

The independently verified observation error is exactly

\[
\boxed{\epsilon_{m,L}
=C_{\log}\tau(m)+\frac{\Lambda}{2\delta^2}\tau(L+1)},
\qquad C_{\log}=\max\{1,\log(1+\kappa)\}.
\]

It yields \(|h''-W_{m,L}|\le\epsilon_{m,L}\). At half density, after importing
only the accepted S55 Section 8 arbitrary-contraction baseline, it also yields

\[
h''\le-\frac1{50}-2V_{m,L}+2\epsilon_{m,L}.
\]

These statements are uniform only at fixed positive \(\delta\); they are not
uniform as an endpoint is approached or as \(c\to1\).

## Why the present constant is not yet useful

For \(c=19/20\) and \(J=[1/50,3/100]\), one has \(\delta=1/50\) and

\[
\Lambda=\frac{1486648002527}{1204352}\approx1.234397\times10^6.
\]

The observation multiplier is
\(\Lambda/(2\delta^2)\approx1.542996\times10^9\). The uncapped harmonic-tail
prefactor in \(\tau\) is
\(2c^2/(\pi^2\delta^4)\approx1.143030\times10^6\). Their product is

\[
1.763690\times10^{15},
\]

before multiplication by \((H_L+2)/(L+1)\). This is the source of the current
cost; it is not a fitted numerical error. In particular, the short-window
values \(V_{2,2}\approx0.55166\) and \(W_{2,2}\approx-8.67913\) do not pay the
rigorous remainder.

## Minimum useful improvement

The smallest theorem-facing deliverable is a fixed pair \((m,L)\), uniform for
all \(a\in[1/50,3/100]\), such that

\[
V_{m,L}(a)-\epsilon_{m,L}(a)>-\frac1{100}.
\]

For an explicit strict margin \(\eta>0\), it is enough to prove
\(V_{m,L}-\epsilon_{m,L}\ge-1/100+\eta/2\). A sharper witness value without a
commensurate reduction of the certified observation/tail error does not close
the target. A baseline-independent alternative is the corresponding uniform
negative certificate for \(W_{m,L}+\epsilon_{m,L}\).

## Six-site obstruction: exact scope

At \(\rho=1/2\), \(c=19/20\), and \(a=1/40\), the reachable observation word
\((0,0,0,1,1)\) has positive probability. Its genuine one-site posterior split
has both complete- and cross-potential Jensen gaps strictly negative. The
necessary quadratic payment coefficient lies in

\[
[0.625832574752639508,0.625832574752639509]>5/8.
\]

This refutes **zero-payment conditional Jensen only**. It does not refute a
paid Hessian comparison, determine the actual-law average over all words,
determine \(V_{m,L}\), or provide a counterexample to entropy-rate concavity.

## Evidence separation and input locations

Proof inputs are the frozen 903-line `QWE09_RESULT.md` from DPP PR131 at
`d67db7fdaf8a15b492807745d10ac3b75706690a`, especially lines 19--70 for the
constants, lines 74--128 for Theorems 1--2, lines 424--674 for the Hessian,
martingale, tail, and limiting arguments, lines 727--755 for the two-shift
baseline transfer, and lines 820--869 for the six-site certificate. The only
imported theorem is the accepted arbitrary-contraction statement in
`S55_REVIEW.md`, Section 8.

The 256-bit outward dyadic certificate is proof evidence for the six-site
strict signs. `QWE09_CYCLE22_SIX_SITE_CHECK.py` is an independent 100-digit
Decimal cross-check. The finite-\(n\) NumPy residuals and the displayed
short-window values are diagnostics only: they test implementation identities
but prove neither the continuum comparison nor the target sign.
