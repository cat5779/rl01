# WEB_PRO_01 — True-law full-block payment with retained exact remainder

Read [COMMON.md](COMMON.md) first.

## Scope

Work on the **actual sine/Toeplitz output law**, not a corrected law.

Before starting, read the newest independent dispositions of the current S59/S60 work. In particular, do not redo the universal rank-one Fisher question if S60 has already settled it, and do not merely restate S59's conditional-table average if it already closed that subproblem.

Useful frozen inputs include the PR118 full-block matrix construction and its Sol assessment, plus the independently reviewed QWE01 block ledger.

## Fixed benchmark

Start with
\[
\rho=\frac12,\qquad c=\frac{19}{20},
\qquad a\in I:=\left[\frac1{50},\frac3{100}\right].
\]

For a finite actual Toeplitz block let
\[
G_V(Y)=\bigl(K_V-\operatorname{diag}(1-Y_V)\bigr)^{-1},
\qquad Z_i=(G_V)_{ii}.
\]

The full-block construction gives an exact internal curvature identity of the form
\[
\mathcal C_I^V
=-\frac12\sum_{i\in I}\mathbb EZ_i^2
-\frac12\mathbb E\mathfrak T((G_V)_{II})
-2\sum_{i<j\in I}\mathbb E r_{ij},
\]
where the pair remainders satisfy \(r_{ij}\ge0\). It also gives the genuine reveal martingale
\[
\mathbb E[(G_V)_{II}\mid Y_A]=(G_A)_{II}
\]
whose one-step increments are rank-one Schur updates
\[
\Delta G=\zeta ww^*.
\]

The previous universal Bellman payment threw away the negative remainder and paid actual rank-one motion with a worst-case all-Hermitian Hessian constant that blows up badly near \(c=1\).

## Single objective

Construct a **true-path full-block inequality** that keeps at least one layer of the exact negative remainder and uses only the actual rank-one reveal directions.

A target result of the right strength is
\[
H_n''(a,c)\le-\varepsilon_{I,c}n+o(n)
\quad\text{uniformly for }a\in I,
\]
or an equivalent finite-chord theorem.

A weaker result is still useful if it proves a dimension-consistent signed saving that can be inserted explicitly into the block ledger and is not already implied by the old universal Bellman constant.

## What to try

A promising combination is:

1. normalize the inverse-score coordinates by actual posterior variances/Schur slack so the basic variables do not inherit a high power of \(\delta^{-1}\), where \(\delta=\min(a,1-a-c)\);
2. compute the exact second variation of the block potential **only** along the actual direction \(ww^*\);
3. retain the exact \(r_{ij}\) term or a finite quadrature lower layer of it while paying the observation-domain change.

The key question is whether the same posterior geometry that creates the large reveal curvature also creates a comparable negative remainder.

## Hard exclusions

Do not:

- demand a good sign for each pair, atom, reveal node, or layer;
- replace the Toeplitz compression by a finite projection;
- spend Fisher mass separately for every overlapping pair;
- drop the probability-acceleration part of the Shannon Hessian;
- return only a smaller numerical version of the old universal \(\Gamma_{\delta,c}\).

## Success criterion

Best: a fixed-width actual-law interval at \(c=19/20\) with volume-uniform negative curvature or nonnegative Jensen gap.

Good partial success: a theorem showing an actual rank-one reveal payment with strictly better endpoint scaling **and** an explicit retained negative remainder that removes a genuine term from the remaining ledger.

If the route fails, give a model-valid obstruction to the combined rank-one/normalized/remainder mechanism, not merely a bad arbitrary Hermitian direction.
