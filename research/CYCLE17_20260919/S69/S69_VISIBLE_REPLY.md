# Visible assistant reply 9fb22162-9dbd-4c75-8245-61ec053a960b

# S69 result

**Verdict: INCOMPLETE for the full target \(I=[0.02,0.03]\), with a PROVED, materially enlarged connected interval.**

For

\[
\rho=\frac13,\qquad c=\frac{19}{20},\qquad
K=\left[\frac1{50},\frac{51}{2000}\right]=[0.02,0.0255],
\]

the complete-configuration entropy satisfies

\[
\boxed{
H_n''(a)\le -\frac{n}{1000}+399
\quad\text{for every }n\ge22,\ a\in K.
}
\]

Consequently,

\[
\boxed{
\operatorname{Gap}_\lambda h_{1/3,19/20}
\ge
\frac1{2000}\lambda(1-\lambda)(a_1-a_0)^2
}
\]

for all \(a_0,a_1\in K\) and \(0\le\lambda\le1\).

This expands the accepted interval from width \(0.003\) to width \(0.0055\): it closes the entire lower gap \([0.02,0.021)\) and extends the upper endpoint from \(0.024\) to \(0.0255\). The stronger pre-existing S63 modulus on \([0.021,0.024]\) remains intact. The inherited S63 result and its finite-witness-to-rate interface are documented in the supplied sources. citeturn579816view0turn616826view3

The proof uses the new affine global cap

\[
\bar C(a)=\frac{6501}{5000}+\frac{2067}{400}a,
\]

with the existing 256 guarded nearest-pair caps, a retuned PSD allocation, and the actual 22-site score test at \(a_*=0.025\). The moving law is evaluated over all \(2^{22}=4{,}194{,}304\) configurations. The final exact certificate proves

\[
P(a)-(\bar C(a)-1)d_{1/3,19/20}(a)\ge\frac1{1000},
\qquad P(a)<19
\]

throughout \(K\). It uses outward interval arithmetic, direct integer enclosures of the expectation sums, a whole-vector nilpotent tail bound, and exact degree-12 Bernstein positivity—not sampled interpolation.

A separate exact obstruction certificate was completed at \(a=0.026\). With the legal near-tight cap

\[
C^\dagger(a)=\bar C(a)+\frac1{1000},
\]

the global cap, all 256 guard bounds, and all PSD conditions continue to hold on \([0.0255,0.026]\). Nevertheless, the score-matched maximum over **every** two-vector test on the same 22-site nearest-neighbour allocation obeys

\[
P_{\max}^{22}(0.026)
-(C^\dagger(0.026)-1)d(0.026)
\le -0.09633473233730599320.
\]

Thus merely changing or optimizing the test function cannot bridge the upper gap at \(0.026\) within this architecture. The smallest exact additional payment required there is at least \(0.096334732337306\). The result also proves a reusable three-site PSD frame lemma for combining nearest and distance-two improvements without double-spending diagonal Fisher budget; its distance-two guard/payment instantiation remains the principal unfinished route toward \(0.03\).

Files:

- :chatgpt-content-reference{index="2"}
- :chatgpt-content-reference{index="3"}
- :chatgpt-content-reference{index="4"}

The archive excludes only the large generated binary probability and derivative caches; `run_from_scratch.sh` regenerates them from the included readable sources and exact inputs.
