# Independent audit of S3 check 3

## Verdict

**ACCEPTED, strictly scoped.** The mesoscopic bridge, the two-bit scalar payment, and the pooled per-atom obstruction survive first independent review. The main sine entropy-rate concavity theorem remains unproved and undisproved.

The source archive hash matched the supplied SHA-256. All 150 ZIP members passed traversal, absolute-path, and symbolic-link screening. The archive manifest covered 149 payload files and verified with zero mismatches before replay. Only inspected mathematical certificate scripts were executed.

## 1. Mesoscopic bridge

### Exact condition block

Let `Q_*` and all `Q_alpha` be finite Hermitian contractions. Let `w_alpha>=0` be independent of `a`, and assume

`sum_alpha w_alpha dim(Q_alpha)=dim(Q_*)=n`.

Fix `0<c<1` and `0<eta<(1-c)/2`. Put `I=[eta/2,1-c-eta/2]` and `I'=[eta,1-c-eta]`. For

`g(a)=n^(-1)(F_(Q_*)(a,c)-sum_alpha w_alpha F_(Q_alpha)(a,c))`,

if `0<epsilon<=log 2` and `||g||_(C(I))<=epsilon`, the proof gives

`sup_(a in I') |g''(a)| <= C_(c,eta) epsilon[1+log(1/epsilon)]^3`.

The zero-gap case is separate and immediate: `g=0` on an interval, hence `g''=0`. This removes the harmless undefined `log(1/0)` edge in the author's asymptotic display.

### Why the proof closes

For every output atom, the determinant matrix has all singular values in `[eta/2,1-eta/2]`. The entropy per coordinate therefore has an absolutely convergent Chebyshev expansion. The order-`h` trace term has total degree at most `2h` in `a` and the atom indicators. Under the moving DPP law, each indicator monomial is replaced by `det(aI+cQ)_V`, so the moving weights are included and the degree remains at most `2h`.

The common constant cancels only because of the weighted-dimension identity. The coefficient budget is then `2r^h/h`, with no factor for the number of latent nodes. An interior Chebyshev derivative estimate controls the truncated polynomial, while the differentiated tail is summable against `h^2 r^h`. Taking the displayed logarithmic truncation yields the claimed response rate.

For the ordered latent-prefix decomposition, all branch probabilities depend only on the latent input and hence are independent of `a`. The local kernels move exactly as `aI+cQ_j^u`. The remainder is a sum of conditional mutual informations and obeys

`0<=E(a,c)<=B:=sum_j Tr b(Q_(B_j))`.

Thus `g=E/n` and `epsilon=B/n`. Since `x[1+log(1/x)]^3 -> 0`, `B=o(n)` gives `F''-G''=o(n)` uniformly on every fixed interior interval. The finite sine Toeplitz application uses the previously accepted trace-defect estimate; that old dependency was not re-reviewed.

### Exact limitation

This is a finite-dimensional response result followed by an `n -> infinity` estimate. It does not prove a continuous Fourier theorem directly. It pays only the outside-block information remainder. The sign and scale of the conditioned leaf sum `G''` remain open.

## 2. Two-bit scalar payment

For a binary input pair with covariance `-d<=0`, the symmetric channel produces output covariance parameter `z=c^2 d`. Interpolating the output table from independence to covariance `z` preserves feasibility because it is the channel image of the corresponding convex interpolation of input tables.

For the log-odds `h(t)`, direct differentiation gives the sum of the four reciprocal cell probabilities. Conditioning either output coordinate shows that the other remains the output of the same symmetric channel applied to a posterior Bernoulli input. Its conditional success probability therefore lies in `[epsilon,1-epsilon]`. This proves both one-coordinate derivative bounds; averaging and integrating gives Lemma 5.1 with its full quantifiers.

The optional replacement of output variances by latent variances is in the safe direction because

`q(1-q)=x(1-x)+epsilon(1-epsilon)(1-4x(1-x)) >= x(1-x)`.

No global Fisher allocation follows from this scalar lemma.

## 3. Pooled per-atom obstruction

The exact certificate constructs the rational graph projection `P=V(I+T^T T)^(-1)V^T`, verifies `P^2=P`, rank `3`, and positivity of the selected atom. It reduces the pointwise defect to one rational term plus one logarithm of a positive rational. Exact power-of-two range reduction and rational atanh-series bounds certify

`1.2248629717184887 < Delta < 1.2248629717184890`,

so `Delta>6/5`. Block diagonal direct sums copy every within-block term and annihilate cross-block inverse entries, giving `Delta_k=k Delta>6k/5` for every integer `k>=1`.

Independent replay returned:

- exact projection and defect certificate: `PASS`;
- full 64-atom rational-log Hessian: `-1093.227099888518... < -1000`;
- direct versus decomposed 80-digit Hessian difference: about `5.61e-77`.

This rejects the proposed pointwise pooled payment only. The full expected Hessian of the base law is strongly negative, and the repeated bad atom has probability equal to a product of the base atom probability. The construction is a finite direct sum, not a contiguous finite Fourier family and not a continuous Fourier object. No expected or sine-law counterexample is accepted.

## Critical open obligation

For the true finite sine Toeplitz compression, consecutive blocks of size `floor(sqrt(n))`, and exact latent-prefix conditional kernels, prove on each fixed interior interval either

`sup_a G_(n,m)''(a,c)<=o(n)`

or a finite-Jensen replacement of the same scale. Small finite Fourier searches are diagnostics only. The bad-atom construction cannot discharge or refute this obligation.
