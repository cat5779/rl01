# WEB_PRO_03 — Close the true-law dyadic finite-chord sum

Read [COMMON.md](COMMON.md) first.

## Accepted starting point

Use the independently reviewed finite-chord/dyadic identity and the independently reviewed QWE02 boundary-response theorem. Do not re-prove the asymptotic tail.

For a stationary block entropy \(H_L\), put
\[
J_L(a)=2H_L(a)-H_{2L}(a).
\]
Along \(L_j=m2^j\),
\[
\operatorname{Gap}h
=\frac{\operatorname{Gap}H_m}{m}
-\sum_{j\ge0}\frac{\operatorname{Gap}J_{L_j}}{2L_j}.
\]

QWE02 gives, on a fixed interior \(a\)-interval, a true-law bound of the form
\[
|\operatorname{Gap}J_L|
\le C_{I,c}\,\eta^2(2+\log L),
\]
hence a tail
\[
\sum_{j\ge N}
\frac{|\operatorname{Gap}J_{L_j}|}{2L_j}
=O_{I,c}\!\left(
\eta^2\frac{\log L_N}{L_N}
\right).
\]

The unresolved object is the **finite retained signed sum**, not the far tail.

## Single objective

Create a cross-scale compensation theorem for
\[
\sum_{j=0}^{N-1}\frac{\operatorname{Gap}J_{L_j}}{2L_j}
\]
under the actual sine output law.

Do not require every \(\operatorname{Gap}J_L\) to have a favorable sign.

A successful result should combine neighboring scales, a block information identity, or a rigorously certified finite core with an analytic middle-scale envelope so that the whole retained sum is paid.

## Preferred benchmark

Start at
\[
\rho=\frac12,\quad c=\frac{19}{20},
\]
with a fixed nondegenerate chord contained in
\[
a\in\left[\frac1{50},\frac3{100}\right].
\]

Use the already certified first favorable scale as an input where applicable, but do not infer the rest from it.

## Tool-design directions

Good candidates include:

- a monotone or almost-monotone **aggregate** across two consecutive doublings;
- a three-block information identity that couples \(J_L\) and \(J_{2L}\);
- an exact conditional-mutual-information representation with cancellation before absolute values;
- a finite interval-arithmetic core plus a proved analytic comparison that covers all larger retained scales before the QWE02 tail starts.

If using computer assistance, the proof must include a mathematically justified finite covering/certificate interface. A brute-force list of dyadic sizes with no analytic stopping rule is not enough.

## Hard exclusions

Do not:

- assume \(J_L''\ge0\);
- replace the full output law by count statistics;
- differentiate the known entropy-value tail estimate;
- use the QWE02 enormous constant alone to claim a practical finite-core proof;
- discard favorable scales while bounding only the unfavorable ones unless the resulting inequality is still strong enough to close the chord.

## Success criterion

Best: a complete rigorous benchmark chord proof for the true entropy rate.

Stronger: a family of finite-chord inequalities covering every chord in a fixed \(a\)-interval.

Useful partial: a new two-scale or multi-scale theorem that provably reduces the retained signed sum to fewer explicit scales with a quantitative budget.

If a candidate cross-scale monotonicity is false, produce an actual sine-model counterexample and preserve the weaker surviving aggregate statement.
