# Independent mathematical audit

## Status: CRITICAL_GAPS

The full dimension-free selector theorem is correctly left **INCOMPLETE**. Nothing in the submission proves or disproves (DF), and the two restricted selectors do not change that status.

Most of the mathematical core in Sections 1, 3, 4, 5, and 7 checks out. There are, however, two definite statement/proof gaps and one source-integrity gap that must be repaired before the document can be accepted as correct in its present form:

1. Section 2 states the (W_1) estimate for arbitrary finite DPP kernels, including boundary positive contractions, but the proof given only treats interior kernels and omits the limiting argument.
2. Section 6 literally denies a positive linear direction selector for an arbitrary fixed (K). That is false for diagonal (K), where Section 4 itself gives such a selector. The proof only rules out a scheme valid when a fixed kernel has a nonzero off-diagonal entry (and hence also rules out a single such scheme over the whole kernel class).
3. All five literature citations are unresolved `unresolved citation` placeholders rather than usable primary-source citations.

These are local repairs. They do not undermine the signed-flow estimate, either (C=2) restricted selector, or the weighted-rate estimate.

## Section-by-section verification

### 1. Exact coupling reformulation — correct

The exact-configuration identity

\[
p_K(S)=(-1)^{|S^c|}\det(K-I_{S^c})
\]

is valid, and the determinant is affine along the rank-one line (K+hP). With (h=\epsilon/2), the displayed capacity is exactly what is needed for

\[
\Pi(S,S)=p_K(S)-h\operatorname{out}_F(S)\ge 0.
\]

The first and second marginal calculations are correct. Conversely, a coupling supported on the diagonal and one-point upward pairs has (h\operatorname{out}_F(S)\le p_K(S)), hence yields the required capacity after division by (h).

The normalization also follows from divergence:

\[
\sum_S |S|b_{K,P}(S)
=\sum_{S,i\notin S}F(S,i)
=\left.\frac d{dh}\operatorname{Tr}(K+hP)\right|_{h=0}=1.
\]

The optimal-transport-face characterization is correct. Equality in

\[
d_H^2\ge d_H\ge |Y|-|X|
\]

together with the known one-point monotone coupling forces (d_H\in\{0,1\}) and (d_H=|Y|-|X|) almost surely, which is exactly the support in (2).

### 2. Dimension-free (W_1)/TV estimate — correct result, incomplete boundary proof

For interior positive contractions, the proof is sound. If (H=B-A=H_+-H_-), compactness of the segment (A_t=A+tH) inside (0<C<I) supplies a uniform spectral margin. A sufficiently fine partition therefore makes

\[
C=A_t+\delta H_+
\]

a positive contraction, with (A_t\le C) and (A_{t+\delta}\le C). Noncommutative Loewner-order stochastic domination then gives the stated increment bound, and summation yields

\[
W_1(\mu_A,\mu_B)\le \lVert A-B\rVert_1.
\]

The stated theorem nevertheless includes boundary kernels, while line 106 explicitly switches to “interior positive contractions” and never returns to the boundary. The missing repair is short but necessary. For (0<\eta<1/2), set

\[
A_\eta=(1-2\eta)A+\eta I,
\qquad
B_\eta=(1-2\eta)B+\eta I.
\]

Then (A_\eta,B_\eta) are interior positive contractions, so

\[
W_1(\mu_{A_\eta},\mu_{B_\eta})
\le (1-2\eta)\lVert A-B\rVert_1.
\]

On the finite state space, every exact DPP probability is a polynomial in the kernel entries, hence (mu_{A_\eta}\to\mu_A) and (mu_{B_\eta}\to\mu_B) in total variation. Therefore (W_1) converges and letting (eta\downarrow0) proves (3) on the boundary. Alternatively, the statement can be restricted to interior kernels, which is enough for the later applications in this submission.

Once (3) is established, (5) follows correctly from (d_H\ge\mathbf 1_{S\ne T}).

### 3. Signed-flow repair — correct, with one useful explicit sentence

Equation (6) has the right constants because (h=\epsilon/2):

\[
\frac1h\bigl(2\lVert K-L\rVert_1+h\lVert P-Q\rVert_1\bigr)
=\frac4\epsilon\lVert K-L\rVert_1+\lVert P-Q\rVert_1.
\]

The Kantorovich–Rubinstein/min-cost-flow step is valid. For completeness, it would help to state explicitly that

\[
\sum_S(b_{K,P}(S)-b_{L,Q}(S))=0,
\]

because each derivative of total probability is zero. Thus the signed demand is in the range of the cube incidence matrix. Fixing every cube edge in its upward orientation loses nothing because the coefficients are signed. The dual Lipschitz norm is exactly the minimum (ell^1) mass of such a signed edge flow, proving (7).

The capacity-vector estimate (8) is correct. The slack example with (h_0=3\epsilon/4) is admissible since (K+h_0P\le(1-\epsilon/4)I), and it gives (4/(3\epsilon)) as stated. The document correctly explains why row slack alone does not repair negative edge coordinates.

### 4. Diagonal-kernel selector — correct

For diagonal (K), differentiating the product Bernoulli law gives the displayed (b_{K,P}), and

\[
F_{K,P}(S,i)=p_K(S)\frac{P_{ii}}{1-k_i}
\]

has exactly the required incoming and outgoing terms. Its total mass is (sum_iP_{ii}=1), and its row sum is at most (p_K(S)/\epsilon).

For a fixed edge label (i), cancellation of (1-k_i) makes the edge component (P_{ii}\mu_k^{(i)}). The product coupling bound and trace-norm contractivity of diagonal pinching give

\[
\lVert F_{K,P}-F_{L,Q}\rVert_1
\le 2\lVert K-L\rVert_1+\lVert P-Q\rVert_1
\le 2D.
\]

Borel dependence, dependence only on (P=vv^*), and permutation equivariance are all immediate from the formula.

### 5. Coordinate direction selector — correct

Testing divergence against (mathbf 1_{i\in S}) gives total (i)-edge mass (P_{ii}). For (P=E_{jj}), nonnegativity therefore kills every edge label other than (j), so the flow is unique. The inclusion transform

\[
\sum_{A\supseteq B}F(A,j)=\det K_B
\]

correctly identifies

\[
F_{K,e_j}(A,j)=p_{K_{E\setminus\{j\}}}(A).
\]

For (L=K(I-K)^{-1}), every eigenvalue lies in

\[
\left[\frac\epsilon{1-\epsilon},\frac{1-\epsilon}{\epsilon}\right].
\]

The Schur complement in (14) lies in the same interval because it is the reciprocal of a diagonal entry of the inverse of the relevant principal submatrix. Thus the conditional absence probability is at least (epsilon), proving (15).

For the same coordinate, compression plus (5) gives (16). For distinct coordinate projectors, the two flows have disjoint edge labels and distance (2), while the projector trace distance is (2). Hence the union of these coordinate-direction cases has a dimension-free (C=2). The formula is also Borel and permutation equivariant on this restricted domain; one sentence saying so would make the “full restricted theorem” wording fully explicit.

### 6. Positive-linear direction obstruction — quantifier is false as written

The first sentence currently says:

> There cannot be a selector which, for fixed (K), is simultaneously positive and linear in the direction matrix (P).

Read literally for an arbitrary fixed (K), this is false. If (K) is diagonal, Section 4 supplies exactly such a positive linear map:

\[
F_{K,P}(S,i)=p_K(S)\frac{P_{ii}}{1-k_i}.
\]

The proof in Section 6 establishes the following narrower and correct statement:

> If a fixed admissible kernel (K) has a nonzero off-diagonal entry, then no flow selector valid for every rank-one direction (P) can be both positive and linear in (P). Consequently, no selector over the full kernel class can be positive and linear in (P) for every fixed (K).

Indeed, positivity represents every edge functional as (operatorname{Tr}(A_{S,i}P)) with (A_{S,i}\succeq0). Testing coordinate indicators gives

\[
\sum_{S:i\notin S}A_{S,i}=E_{ii}.
\]

Every positive-semidefinite summand of the rank-one matrix (E_{ii}) is a nonnegative multiple of (E_{ii}), so the whole flow depends only on the diagonal of (P). For a non-diagonal (K), choose indices (r\ne s) with (K_{rs}\ne0) and unit vectors supported on (r,s), with equal coordinate magnitudes but two phases chosen so that

\[
\operatorname{Re}(K_{rs}P_{sr})
\]

differs. Their projectors have the same diagonal, while the derivative of (det K_{\{r,s\}}), hence the corresponding divergence data, differs. This is the required contradiction.

A concrete two-dimensional witness is

\[
K=\begin{pmatrix}1/2&t\\ t&1/2\end{pmatrix},
\qquad
P_\pm=\frac12\begin{pmatrix}1&\pm1\\ \pm1&1\end{pmatrix},
\]

with (0<t<1/2) chosen inside the spectral-gap range. The two projectors have identical diagonals, but

\[
b_{K,P_\pm}(\{1,2\})=\frac12\mp t.
\]

The final sentence correctly classifies this as a method obstruction only. It does not disprove nonlinear selectors or (DF).

### 7. Weighted intrinsic-rate estimate — correct, conditional on (DF)

Strict spectral gaps make every exact configuration probability positive. The algebra in (17) is correct:

\[
\begin{aligned}
\sum_Sp_K(S)\sum_{i\notin S}|r_{K,P}-r_{L,Q}|
&\le \lVert F_{K,P}-F_{L,Q}\rVert_1\\
&\quad+\sum_S\frac{|p_K(S)-p_L(S)|}{p_L(S)}\operatorname{out}_{L,Q}(S)\\
&\le C_\epsilon D+\frac2\epsilon\sum_S|p_K(S)-p_L(S)|\\
&\le C_\epsilon D+\frac4\epsilon\lVert K-L\rVert_1\\
&\le\left(C_\epsilon+\frac4\epsilon\right)D.
\end{aligned}
\]

No extra explicit factor of (n) appears; the unnormalized trace norm may itself grow with volume, exactly as the submission notes. The warnings about common randomness, invariant/per-site control, tightness or consistency, and identification of limiting marginals are appropriate. The text does not overclaim an infinite-volume result.

## Source audit

The mathematical attributions are plausible, but the source file does not contain usable citations. Each `unresolved citation{...}` token must be replaced by a normal citation to a primary source, with the theorem or proposition supporting the particular claim.

Suitable primary sources are:

1. Russell Lyons, *Determinantal Probability Measures* (2003), especially Proposition 10.3 for nested projection couplings: https://numdam.org/item/10.1007/s10240-003-0016-0.pdf
2. Julius Borcea, Petter Brändén, and Thomas M. Liggett, *Negative Dependence and the Geometry of Polynomials*, JAMS 22 (2009), Theorem 4.13 and Proposition 4.15 for noncommutative Loewner-order stochastic domination, and Proposition 3.5 for the strongly Rayleigh property: https://www.ams.org/journals/jams/2009-22-02/S0894-0347-08-00618-8/S0894-0347-08-00618-8.pdf
3. Russell Lyons and Andreas Thom, *Invariant Coupling of Determinantal Measures on Sofic Groups* (primary preprint; see in particular Theorem 2.1 and the main invariant-coupling result): https://arxiv.org/abs/1402.0969
4. Jesper Møller and Eliza O'Reilly, *Couplings for determinantal point processes and their reduced Palm distributions with a view to quantifying repulsiveness*: https://arxiv.org/abs/1806.07347

The Lyons citation supports the stated known feasibility input only together with the projection-dilation reduction specified in the frozen problem. It should not be phrased as though Proposition 10.3 alone directly states the full positive-contraction rank-one claim.

## Minimum repairs required for acceptance

1. Add the (A_\eta,B_\eta) continuity argument at the end of Section 2, or restrict (3) and (5) there to interior positive contractions.
2. Replace the opening claim of Section 6 by the non-diagonal/full-class quantifier quoted above, and explicitly note that diagonal (K) admits the linear selector from Section 4.
3. Replace every unresolved citation placeholder by a theorem-level primary citation.
4. Keep the headline and final target status **INCOMPLETE**. The submission contains no basis for `PROVED` or `DISPROVED` on (DF).
