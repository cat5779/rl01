# Universal obstruction test for dimension-free DPP flow selection

## Frozen theorem under attack

Fix \(0<\varepsilon<1/2\). For a finite set \(E=\{1,\dots,n\}\), a Hermitian kernel

\[
\varepsilon I\le K\le(1-\varepsilon)I,
\]

and a rank-one projector \(P=vv^*\), define

\[
b_{K,P}(S)=\left.\frac d{dh}p_{K+hP}(S)\right|_{h=0},
\]

where \(p_K\) is the exact DPP law. Let \(\mathcal F(K,P)\) be the set of nonnegative upward Boolean-cube flows satisfying

\[
b_{K,P}(S)=\sum_{i\in S}F(S\setminus\{i\},i)-\sum_{i\notin S}F(S,i),
\]

\[
\sum_{S,i\notin S}F(S,i)=1,
\qquad
\sum_{i\notin S}F(S,i)\le\frac2\varepsilon p_K(S).
\tag{1}
\]

The theorem to attack asserts that one can select \(F_{K,P}\in\mathcal F(K,P)\), Borel and permutation-equivariantly, with

\[
\|F_{K,P}-F_{L,Q}\|_1
\le C_\varepsilon\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
\tag{DF}
\]

for a constant independent of \(n\).

## Required disproof certificate

Disprove (DF) only by an obstruction that applies to **every** selector. The cleanest acceptable certificate is an explicit uniformly gapped family of pairs \(z_n=(K_n,P_n)\), \(z'_n=(L_n,Q_n)\) such that, with

\[
d_n=\|K_n-L_n\|_1+\|P_n-Q_n\|_1,
\]

one has

\[
\frac{
\inf\{\|F-G\|_1:F\in\mathcal F(K_n,P_n),\ G\in\mathcal F(L_n,Q_n)\}
}{d_n}\longrightarrow\infty.
\tag{2}
\]

An equally explicit finite-cycle or branching certificate is acceptable if it proves that, for every simultaneous choice \(F_j\in\mathcal F(z_j)\), at least one nearby parameter pair violates every dimension-free Lipschitz constant. State and prove the exact selection-theoretic implication.

Every matrix, projector, configuration family, cut, and lower-bound constant must be explicit. Keep a fixed spectral gap, rank one, the pointwise capacities, and the global normalization. A numerical linear program may locate a candidate but is not a final certificate; convert it to an exact rational or symbolic family and prove the relevant min-cut or dual inequality.

## Audited facts and exclusions

The following are already known and must not be repackaged as a disproof:

1. Each \(\mathcal F(K,P)\) is nonempty by the standard one-point monotone DPP coupling.
2. The divergence data have a signed dimension-free repair:

   \[
   \inf_{\operatorname{div}G=b_{K,P}-b_{L,Q}}\|G\|_1
   \le\frac4\varepsilon\|K-L\|_1+\|P-Q\|_1.
   \tag{3}
   \]

3. The capacity vectors are \(\ell^1\)-stable:

   \[
   \sum_S\left|\frac2\varepsilon p_K(S)-\frac2\varepsilon p_L(S)\right|
   \le\frac4\varepsilon\|K-L\|_1.
   \tag{4}
   \]

4. Diagonal kernels and coordinate birth directions have explicit selectors with constant \(2\).
5. For fixed non-diagonal \(K\), a selector linear and positive in \(P\) is impossible. This only rules out a POVM-type method; it does not obstruct nonlinear selectors.
6. Discontinuity or bad conditioning of one entropic, quadratic, lexicographic, or minimum-norm optimizer is not a universal selection obstruction.

Thus a genuine counterexample must arise from the geometry of the entire nonnegative capacitated flow sets, not from the signed divergence equation alone or from a chosen rule.

## If no disproof is obtained

Do not switch to an unrelated positive proof. Return `INCOMPLETE` with the strongest exact obstruction or anti-obstruction established. Useful partial outcomes include a proven dimension-free Hausdorff estimate between the exact DPP flow polytopes, a theorem excluding all pairwise-separation certificates of the form (2), or an explicit small-dimensional family that forces a new face transition together with a rigorous bound showing why it still falls short of a universal obstruction. Classify the result as sufficient, necessary, equivalent, stronger, or incomparable to (DF).

## Output standard

Return exactly one of `DISPROVED`, `PROVED`, or `INCOMPLETE`, followed by a complete argument. Use `DISPROVED` only with a universal-selector certificate. Use `PROVED` only if the full selection theorem itself is proved despite the adversarial assignment. Distinguish mathematical correctness from novelty and cite primary sources precisely.
