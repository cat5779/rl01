# QWE09_RESULT — Parity ensembles with a paid conditional-information curvature remainder

Date: 2026-09-19. Repository: randomcat4/dpp-stationary-entropy, PR131.


## Round-2 findings first

The concavity attack continued after the first-round manuscript. The following are the new findings; exploratory items are explicitly not promoted to proofs.

- The strict six-site true sine-Toeplitz obstruction to zero-payment conditional Jensen remains valid and reproducible from the committed certificate.
- A true Toeplitz pointwise-sign route fails: finite probes stayed favorable through `n=11`, but at `n=12` the minimum complete-potential value was about `-6.3854`, with 14 negative output words.
- A universal pair-by-pair mixed-sign route also fails in the ambient bipartite projection/contraction class: a random probe produced a positive individual even-odd pair contribution of about `0.157821`.
- The aggregate mixed direction remains numerically promising: across 320 random bipartite projection/contraction Hessian probes, the tested common curvature direction remained negative, and the largest aggregate mixed-parity Hessian was only at numerical-zero scale (about `1e-14`).
- Therefore the next viable target is an aggregate parity-mixed curvature inequality with compensation across words/pairs, not a wordwise or pairwise sign theorem.
- The main interval theorem remains **INCOMPLETE** for `rho=1/2, c=19/20, a in [1/50,3/100]`.

Details, scope warnings, and the exact logical role of the probes are recorded in `results/ROUND2_FINDINGS.md`. The interrupted round-2 temporary probe scripts are not currently retained, so those probes are logged as diagnostics rather than reproducible certificates.

## Repository-copy status

This is a self-contained, compact transcription of the first-round manuscript delivered in the research conversation. The original longer manuscript and its numerical diagnostics remain preserved in that conversation. The mathematical assertions below are AUTHOR CLAIMS pending adversarial proof audit, not independently accepted repository theorems. In particular, the exact-log Hessian bound, observation-domain payment, and effective all-exterior passage are the next audit targets. The user's next instruction is to attempt concavity itself. No merge or change to the repository's accepted status is requested.

**PROVED in the author's first-round manuscript:** an explicit dimension-independent quadratic payment for the complete logarithmic curvature potential; a deterministic mask-uniform averaged resolvent tail; a two-sided effective finite-observation-to-true-Toeplitz second-response comparison; correct finite and infinite parity formulations.

**DISPROVED:** zero-payment conditional Jensen for the complete potential, at an actual positive-probability six-site sine-Toeplitz word at rho=1/2, c=19/20, a=1/40.

**INCOMPLETE:** strict entropy-rate concavity throughout rho=1/2, c=19/20, a in [1/50,3/100]. Neither a local Jensen counterexample nor a finite numerical sign decides that question. No enlargement of the accepted concavity region is claimed.

All entropy below is actual spatial-configuration Shannon entropy in natural units. A finite Toeplitz compression is not a projection.

## 1. Quantitative statement

Fix 0<c<1 and a compact interval J inside (0,1-c). Define

\[
\delta=\min_{a\in J}\min(a,1-a-c)>0,\quad
\kappa=\frac{c^2}{4\delta(\delta+c)},\quad
\bar\kappa=\max(1,\kappa),\quad r_\delta=(1-\delta)/\delta.
\]

Set

\[
 C_H=\max\{2+7(1+\kappa)\bar\kappa r_\delta^2,\,14(1+\kappa)\bar\kappa\},
 \quad\Lambda=C_H/2,
\]
\[
 C_{\log}=\max\{1,\log(1+\kappa)\},\quad B_*=C_{\log}\delta^{-2},
\]
\[
 \tau(R)=\min\left\{\delta^{-2},
 \frac{2c^2}{\pi^2\delta^4}\frac{H_{R-1}+2}{R}\right\},\qquad
 H_k=\sum_{j=1}^k j^{-1},\ H_0=0.
\tag{1.1}
\]

For the actual finite output kernel K_A=aI+cQ_A and actual word Y_A, write

\[
 G_A=(K_A-\operatorname{diag}(1-Y_A))^{-1}.
\]

For a Hermitian matrix X in the domains proved below, put

\[
 h_{ij}=|X_{ij}|^2,\quad v_{ij}=X_{ii}X_{jj},\quad
 f_{ij}(X)=h_{ij}+(v_{ij}-h_{ij})\log(1-h_{ij}/v_{ij}),
\]
\[
 \Phi(X)=\sum_iX_{ii}^2+\sum_{i\ne j}f_{ij}(X),\qquad
 \Chi(X)=\sum_{i\in E,j\in O}f_{ij}(X).
\tag{1.2}
\]

The Phi pair sum is ordered. Chi counts each even-odd pair once. At h=0 the pair term is zero. All displayed logarithms have positive arguments on the actual matrices and all interpolation segments used below.

Take I=[1,m], A=[1-L,m+L] in the infinite stationary process and define witnesses using its actual finite marginal on A:

\[
 W_{m,L}=-m^{-1}\mathbb E\Phi((G_A)_{II}),\qquad
 V_{m,L}=m^{-1}\mathbb E\Chi((G_A)_{II}),
\]
\[
 \epsilon_{m,L}=C_{\log}\tau(m)+\frac{\Lambda}{2\delta^2}\tau(L+1).
\tag{1.3}
\]

**Theorem 1 (author claim with proof below).** For every true sine-Toeplitz interval of length n and every a in J,

\[
 \left|H_n''/n-W_{m,L}\right|
 \le\epsilon_{m,L}+4B_*(m+L)/n.
\tag{1.4}
\]

This holds for any fixed rho in (0,1), with the same constants. At half density, introduce separate even and odd shifts

\[
 \mathscr H_n(s,t)=H(\operatorname{DPP}(cQ_n+sP_E+tP_O)),\quad
 F_{eo,n}(a)=\partial_s\partial_t\mathscr H_n(a,a).
\]

Then

\[
 \left|-F_{eo,n}/n-V_{m,L}\right|
 \le\epsilon_{m,L}+4B_*(m+L)/n.
\tag{1.5}
\]

Consequently H_n''/n converges locally uniformly, h is C^2 on the legal interval, and

\[
 |h''-W_{m,L}|\le\epsilon_{m,L}.
\tag{1.6}
\]

This is a second-response comparison, not differentiation of a value error.

**Theorem 2 (baseline-dependent sufficient interface).** Use only the accepted finite-contraction baseline recorded in the packet's S55_REVIEW, Section 8:

\[
 \frac{d^2}{db^2}H(\operatorname{DPP}(bI+(37/40)R))
 \le-\dim(R)/50,\quad0\le R\le I,\quad0<b<3/40.
\tag{1.7}
\]

At rho=1/2, c=19/20, a in [1/50,3/100], let p=a+c/2, e_n=|E|, and

\[
 \mathcal B_n=\mathbb E_{X_E}H(Y_O\mid X_E)+I(X_E;Y_O\mid Y_E).
\]

Then

\[
 \mathcal B_n''\le\frac{e_n}{p(1-p)}-\frac n{50}
 -2nV_{m,L}+2n\epsilon_{m,L}+8B_*(m+L),
\tag{1.8}
\]
\[
 h''\le-1/50-2V_{m,L}+2\epsilon_{m,L}.
\tag{1.9}
\]

The full conditional-information curvature is included. The right side has NOT been certified negative on the target interval.

## 2. Actual output law, support, and conditioning

For X~DPP(Q), independently generate Pr(Y_i=1|X)=a+cX_i. For finite S,

\[
 \mathbb E\prod_{i\in S}Y_i
 =\sum_{T\subseteq S}a^{|S|-|T|}c^{|T|}\det Q_T
 =\det(aI+cQ)_S.
\]

Inclusion-exclusion proves that the output is exactly DPP(K), K=aI+cQ, and its full atom is

\[
 p_V(y)=(-1)^{|V|-|y|}\det(K_V-\operatorname{diag}(1-y)).
\tag{2.1}
\]

Arbitrary finite output conditioning preserves the form K_cond=aI+cR with 0<=R<=I. Indeed, write the latent block as a site of diagonal r, coupling u, and remaining block R_0. Output 1 gives R_0-c uu*/(a+cr), positive because c/(a+cr)<=1/r and the latent Schur complement is positive; its upper bound by I is immediate. Output 0 gives R_0+c uu*/(1-a-cr), bounded above by I because c/(1-a-cr)<=1/(1-r) and the hole Schur complement is positive. The cases r=0 or r=1 have u=0. Iterate. Every realized next-output probability is at least delta, proving full support.

The infinite sine kernel is

\[
 Q_\rho(i,j)=\frac1{2\pi}\int_{-\pi\rho}^{\pi\rho}e^{\mathrm i(i-j)\theta}\,d\theta.
\]

It is the Fourier-multiplier orthogonal projection on the arc. Its finite principal matrices are positive contractions, not generally projections.

## 3. Finite parity ensembles and the complete information remainder

At rho=1/2,

\[
 Q_{EE}=I_E/2,\quad Q_{OO}=I_O/2,\quad U=2Q_{EO},\quad\|U\|\le1.
\]

The norm bound follows from 0<=Q<=I and the off-diagonal block form of Q-I/2. It does not imply U*U=I.

The latent-even vector is iid fair. Conditioning on its word x gives

\[
 B_x=I_O/2+\tfrac12U^*\operatorname{diag}(1-2x)U,\qquad0\le B_x\le I.
\tag{3.1}
\]

This is the Schur complement of the even masked diagonal block. For two true sites, B_x=1/2 +/- 2/pi^2, neither 0 nor 1: the conditional kernel is not a projection.

Construct the channel from uniforms independent across sites and independent of X. Given X_E, Y_E uses only X_E and the even uniforms, which are independent of the odd latent vector and odd uniforms. Hence Y_E is conditionally independent of Y_O given X_E. The chain rule therefore gives

\[
 H(Y_E,Y_O)=|E|h_b(p)+\mathbb E_{X_E}H(\operatorname{DPP}(aI+cB_{X_E}))
 +I(X_E;Y_O\mid Y_E),\quad p=a+c/2.
\tag{3.2}
\]

The latent weights are 2^{-|E|}, independent of a. This does not make the information term concave.

The observed-even vector is iid Bernoulli(p). For its word y put

\[
 w_y=p^{|y|}(1-p)^{|E|-|y|},\quad
 C=cQ_{EO}=cU/2,\quad D_y=\operatorname{diag}(p-1+y).
\]

The actual conditional odd-output kernel is

\[
 M_y=pI-C^*D_y^{-1}C
 =pI+\frac{c^2}{4}U^*\operatorname{diag}\left(\frac{1-y}{1-p}-\frac yp\right)U.
\tag{3.3}
\]

Thus the combined remainder is exactly

\[
 \mathcal B_V=H(Y_O\mid Y_E)=\sum_yw_yH(\operatorname{DPP}(M_y)).
\tag{3.4}
\]

This is an observed-mask ensemble with moving actual weights, not a uniform latent ensemble with I'' discarded. The posterior latent-even coordinates given y are independent with probabilities (a+c)/(2p) for y_i=1 and (1-a-c)/(2(1-p)) for y_i=0. Equation (3.3) was obtained by actual DPP conditioning, not by the false general rule that mixing DPPs equals taking a DPP of the averaged kernel.

The exact contrast-squared representation is

\[
 \alpha(p)=c^2/[4p(1-p)],\quad b(p)=p-c^2/(4p),
\]
\[
 R_y(p)=U^*\operatorname{diag}(1-y)U+(1-p)(I-U^*U),\quad
 M_y=bI+\alpha R_y,\quad0\le R_y\le I.
\tag{3.5}
\]

The upper bound follows by replacing diag(1-y) by I, obtaining (1-p)I+pU*U<=I. The leakage (1-p)(I-U*U) cannot be dropped in a finite true window.

For the target slice,

\[
 p\in[99/200,101/200],\quad\alpha\le9025/9999<903/1000<37/40,
\]
\[
 97/2475\le b\le147/2525<3/40.
\tag{3.6}
\]

Nevertheless b, alpha, R_y and w_y all move in the common a direction. If F_y(a)=H(DPP(M_y(a))), k=|y|, then

\[
 s_y=k/p-(|E|-k)/(1-p),\quad w_y'=w_ys_y,
\]
\[
 w_y''=w_y\{s_y^2-k/p^2-(|E|-k)/(1-p)^2\},
\]
\[
 M_y'=I+C^*D_y^{-2}C,\quad M_y''=-2C^*D_y^{-3}C,
\]
\[
 \mathcal B_V''=\sum_y(w_yF_y''+2w_y'F_y'+w_y''F_y).
\tag{3.7}
\]

Every term in (3.7) is retained in the subsequent complete-response bound.

## 4. Infinite and cyclic projection statements, with their quantifiers

For the infinite half-density projection, Q^2=Q gives Q_EO Q_OE=I_E/4 and Q_OE Q_EO=I_O/4. Hence U=2Q_EO is unitary. This uses the infinite projection identity.

Choose finite E_r increasing to all evens. Conditioning on X_{E_r} gives on the odd subspace

\[
 B_{x,r}=I/2+\tfrac12U^*P_{E_r}\operatorname{diag}(1-2x)P_{E_r}U.
\]

For each fixed sequence x this converges strongly to

\[
 B_x=U^*\operatorname{diag}(1-x)U,
\tag{4.1}
\]

which is a projection. Entrywise convergence also follows from Cauchy-Schwarz for the absolutely convergent column products. For each finite odd cylinder the conditional probability given X_{E_r} is a bounded martingale. Its determinant formula converges to the cylinder probability of DPP(B_x). Martingale convergence and intersection of the countably many cylinder probability-one sets prove that DPP(B_{X_E}) is an almost-sure regular conditional odd law given all latent evens. Defining a kernel for every sequence is distinct from claiming conditional probability at a positive-mass arbitrary infinite word.

Exactly the same exhaustion for observed-even conditioning gives

\[
 M_y=pI-\frac{c^2}{4}U^*\operatorname{diag}((p-1+y)^{-1})U.
\tag{4.2}
\]

The inverses are uniformly bounded. This observed conditional kernel is gapped, not necessarily a projection.

For a finite odd set F, all-even conditioning gives the legitimate finite-alphabet identity

\[
 H(Y_F\mid Y_E)=H(Y_F\mid X_E)+I(X_E;Y_F\mid Y_E).
\]

No infinite entropy is subtracted. A separate rate formulation uses m consecutive even-odd cells:

\[
 A_m=H(Y_{O_m}\mid X_{E_m}),\quad B_m=H(Y_{O_m}\mid Y_{E_m}),\quad I_m=B_m-A_m.
\]

Stationarity of (X_{2k},Y_{2k+1}) and entropy subadditivity imply existence of A_m/m after subtracting m log 2; similarly B_m/m converges after subtracting the observed-even marginal entropy. Thus I_m/m converges and

\[
 h=\tfrac12h_b(p)+\tfrac12\lim_m A_m/m+\tfrac12\lim_m I_m/m.
\tag{4.3}
\]

No separate convergence of A_m''/m or I_m''/m is asserted. The comparison controls their combination.

For 2m cyclic sites, the Fourier projection onto modes 0,...,m-1 has both parity blocks I_m/2, by the root-of-unity sum. Its exact projection identity makes U unitary. Conditioning on all m cyclic evens gives the finite version of (4.1). Neither this finite cyclic identity nor a cyclic finite sign is substituted for a true Toeplitz theorem.

## 5. Exact logarithmic curvature and dimension-independent payment

### 5.1 Scores and ratio bounds

Let A_Y=K-diag(1-Y), G=A_Y^{-1}, sigma_i=2Y_i-1. Since

\[
 A_Y=\tfrac12\operatorname{diag}(\sigma)+K-I/2,
 \quad\|K-I/2\|\le1/2-\delta,
\]

the reverse triangle inequality gives ||G||<=delta^{-1}. Separate diagonal differentiation gives

\[
 Z_i=G_{ii}=\partial_{a_i}\log p_Y
 =\frac{\sigma_i}{\Pr(Y_i\mid Y_{-i})},\qquad
 \sigma_iZ_i\ge\ell_0=(1-\delta)^{-1}.
\tag{5.1}
\]

For i!=j, condition on all other output coordinates. Write the conditional kernel as C=aI+cR, 0<=R<=I, with diagonals q,r and squared off-diagonal s. Its table is

\[
 \pi_{11}=qr-s,\quad\pi_{10}=q(1-r)+s,\quad
 \pi_{01}=(1-q)r+s,\quad\pi_{00}=(1-q)(1-r)-s.
\]

For the realized pair, epsilon=sigma_i sigma_j and D its corresponding product of marginal probabilities, two-by-two inversion gives

\[
 h=|G_{ij}|^2=s/\pi^2,\quad v=G_{ii}G_{jj}=\varepsilon D/\pi^2,
 \quad D=\pi+\varepsilon s,\quad v-h=\varepsilon/\pi.
\tag{5.2}
\]

For word 11, h/(v-h)=s/det C. If lambda_1<=lambda_2 are its eigenvalues,

\[
 s/\det C\le(\lambda_2-\lambda_1)^2/(4\lambda_1\lambda_2)
 \le c^2/[4\delta(\delta+c)]=\kappa.
\]

The final bound maximizes the increasing function (t-1)^2/(4t), t>=1, using lambda_2/lambda_1<=(a+c)/a<=(delta+c)/delta. Word 00 uses I-C. Thus same-sign words have 0<=h/v<=theta=kappa/(1+kappa)<1.

For word 10, write q=a+cx, r=a+cy. Positivity of R and I-R gives s<=c^2 min(xy,(1-x)(1-y)). With z=1-y,

\[
 \frac{s}{q(1-r)}\le
 \frac{c^2\min\{x(1-z),(1-x)z\}}{(\delta+cx)(\delta+cz)}.
\]

For x<=z this decreases in z, so the maximum occurs at z=x; the other region is symmetric. The remaining maximum of c^2 x(1-x)/(delta+cx)^2 occurs at x=delta/(2delta+c) and equals kappa. Word 01 is symmetric. Hence opposite-sign words have 0<=h/|v|<=kappa. These bounds hold for every principal core of every relevant masked inverse.

### 5.2 Complete configuration Hessian

Separate diagonal affinity of the atom determinant gives

\[
 p_i=pZ_i,\quad p_{ij}=p(Z_iZ_j-|G_{ij}|^2)\ (i\ne j),\quad p_{ii}=0.
\]

Normalization yields E Z_iZ_j=E|G_ij|^2 for distinct i,j. Therefore

\[
 H_{a_i a_i}=-\mathbb EZ_i^2,
\]
\[
 H_{a_i a_j}=\mathbb E_{\rm exterior}
 \left[\log\frac{\pi_{10}\pi_{01}}{\pi_{00}\pi_{11}}-s\sum_b1/\pi_b\right].
\tag{5.3}
\]

For the second formula the exterior marginal is fixed under perturbations at i,j; conditional kernel diagonals change with slope 1, off-diagonal is fixed, and the four mixed atom derivatives are (+1,-1,-1,+1) in order (00,10,01,11). This accounts for acceleration as well as Fisher.

By (5.2),

\[
 f_{ij}(G)=s/\pi^2+(\varepsilon/\pi)\log(\pi/D).
\]

Multiplication by the actual conditional probability pi and summation gives

\[
 \mathbb E[f_{ij}(G)\mid\mathrm{exterior}]
 =s\sum_b1/\pi_b-\log\frac{\pi_{10}\pi_{01}}{\pi_{00}\pi_{11}},
\]

because the alternating sum of log D_b vanishes for products of one-site marginals. Consequently

\[
 H_n''=-\mathbb E\Phi(G_n),\qquad F_{eo,n}=-\mathbb E\Chi(G_n).
\tag{5.4}
\]

The common Fisher E(tr G)^2 equals sum_i E Z_i^2+sum_{i!=j}E|G_ij|^2; it is not the diagonal Fisher alone.

### 5.3 A common convex domain

Fix the already observed core signs sigma. Consider the Hermitian matrices X satisfying

\[
 \|X\|\le\delta^{-1},\quad u_i=\sigma_iX_{ii}\ge\ell_0,
 \quad |X_{ij}|^2\le\gamma_{ij}u_i u_j,
\tag{5.5}
\]

where gamma_ij=theta for equal signs and kappa otherwise. This domain is convex: the last constraint is positivity of the affine matrix with diagonal u_i,u_j and off-diagonal X_ij/sqrt(gamma_ij). It contains all actual core score matrices and their conditional means. Same-sign arguments 1-h/v are at least 1/(1+kappa); opposite-sign arguments are at least 1. Thus all interpolation logarithms are legal.

### 5.4 Hessian bound for the complete logarithm

**Lemma 3.** On (5.5), for Hermitian direction D,

\[
 |D^2\Phi(X)[D,D]|\le C_H\|D\|_{HS}^2,
 \qquad |D^2\Chi(X)[D,D]|\le C_H\|D\|_{HS}^2.
\tag{5.6}
\]

Proof. For one pair let u=sigma_i X_ii, v=sigma_j X_jj, s=uv, h=|X_ij|^2, r=h/s and epsilon=sigma_i sigma_j. Define psi(z)=z+(1-z)log(1-z), g_epsilon(r)=epsilon psi(epsilon r). Then f=s g(r), g'=-log(1-epsilon r), g''=epsilon/(1-epsilon r). With L_*=1+kappa,

\[
 |g''|\le L_*,\quad |g'|\le L_*r,\quad|g-rg'|\le L_*r^2/2,
\]

by integration from g(0)=g'(0)=0. Along the matrix line write du=sigma_i D_ii, dv=sigma_j D_jj, dx=D_ij. Then

\[
 s'=vdu+udv,\quad s''=2du\,dv,\quad
 h'=2\Re(\overline{X_{ij}}dx),\quad h''=2|dx|^2,
\]
\[
 f''=(g-rg')s''+g'h''+\frac{g''}{s}(h'-rs')^2.
\]

Using (x+y+z)^2<=3(x^2+y^2+z^2) gives

\[
 |f''|\le L_*\left[r^2|du\,dv|+14r|dx|^2
 +3r^2(v/u)du^2+3r^2(u/v)dv^2\right].
\tag{5.7}
\]

There is no neighbor-count factor. Indeed, r_ij<=bar-kappa and row energy sum_j|X_ij|^2<=delta^{-2} imply

\[
 \sum_{j\ne i}r_{ij}^2\le\bar\kappa r_\delta^2,
 \qquad\sum_{j\ne i}r_{ij}^2u_j/u_i\le\bar\kappa r_\delta^2.
\]

The second uses r_ij^2 u_j/u_i=r_ij |X_ij|^2/u_i^2. Sum (5.7) over ordered pairs. Its first term is bounded by L_* bar-kappa r_delta^2 sum_i D_ii^2 using |D_ii D_jj|<=(D_ii^2+D_jj^2)/2. The last two terms contribute at most six times that quantity. The off-diagonal part contributes at most 14 L_* bar-kappa sum_{i!=j}|D_ij|^2. The diagonal squares in Phi add 2 sum_i D_ii^2. The maximum defining C_H proves (5.6). Chi uses only a subset of the same positive majorants. QED.

Thus Lambda||X||_HS^2 +/- Phi(X), and likewise with Chi, are convex on each fixed-sign domain. No series truncation of the logarithm is used.

### 5.5 Matrix martingale and observation payment

For I subset A subset V,

\[
 \mathbb E[(G_V)_{II}\mid Y_A]=(G_A)_{II}.
\tag{5.8}
\]

Proof: perturb K by a small real parameter times any Hermitian matrix supported on I x I; the gap makes this legal. Differentiate the exact marginalization identity p_A=sum p_V, divide by p_A, and use the determinant score tr(GD). Arbitrary Hermitian directions identify the matrix entries. This averages the score, not a conditional kernel.

Taylor's theorem and (5.6), with cancellation of the linear term in (5.8), give for Psi=Phi or Chi

\[
 |\mathbb E[\Psi((G_V)_{II})\mid Y_A]-\Psi((G_A)_{II})|
 \le\Lambda\mathbb E[\|(G_V)_{II}-(G_A)_{II}\|_{HS}^2\mid Y_A].
\tag{5.9}
\]

All matrices lie in the same fixed-sign convex domain. Given Y_A, take independent actual extensions Y,Y'. The inverse identity is

\[
 G(Y)-G(Y')=G(Y)\operatorname{diag}(Y'-Y)G(Y').
\]

The diagonal difference is supported outside A with norm at most 1, and ||G(Y')||<=delta^{-1}. Therefore

\[
 \|(G(Y)-G(Y'))_{II}\|_{HS}^2
 \le\delta^{-2}\sum_{i\in I,j\in V\setminus A}|G(Y)_{ij}|^2.
\]

Conditional variance is one half the mean squared independent-copy difference. Integrating (5.9) proves the full-block payment

\[
 |\mathbb E\Psi((G_V)_{II})-\mathbb E\Psi((G_A)_{II})|
 \le\frac{\Lambda}{2\delta^2}
 \mathbb E\sum_{i\in I,j\in V\setminus A}|G_V(i,j)|^2.
\tag{5.10}
\]

This is the manuscript's equation (5.24). Every internal pair is paid together, without edge count or degree loss.

The variance is also a single observed Fisher gain: successively reveal exterior outputs. A Schur complement gives each core-matrix increment zeta vv*, with zeta=1/q with probability q and zeta=-1/(1-q) otherwise. Its mean is zero and its squared Hilbert-Schmidt norm equals its squared trace. Orthogonality of martingale differences gives

\[
 \mathbb E\|(G_V)_{II}-(G_A)_{II}\|_{HS}^2
 =\mathbb E(\operatorname{tr}(G_V)_{II})^2-
 \mathbb E(\operatorname{tr}(G_A)_{II})^2.
\tag{5.11}
\]

### 5.6 Magnitude control

For 0<=r<1, 0<=psi(r)<=r. For r>=0,

\[
 0\le\psi(-r)/r=((1+r)\log(1+r)-r)/r\le\log(1+r).
\]

Therefore |f_ij(X)|<=C_log |X_ij|^2, and on a core I,

\[
 |\Phi(X)|\le C_{\log}\|X\|_{HS}^2\le B_*|I|,\qquad
 |\Chi(X)|\le B_*|I|.
\tag{5.12}
\]

## 6. A physical-scale averaged inverse tail

**Lemma 4.** For every true finite sine-Toeplitz interval V of size n, every actual word, and every integer R>=1,

\[
 n^{-1}\sum_{i,j\in V}\min(|i-j|/R,1)|G_V(i,j)|^2\le\tau(R).
\tag{6.1}
\]

In particular the normalized energy at distances at least R is at most tau(R).

Proof. Randomly shift a length-R interval grid by a uniform integer in {0,...,R-1}, and assign independent Rademacher signs to its cells. Let D be the resulting diagonal sign matrix on V. This is auxiliary proof randomness, not the actual DPP mask. The observation mask commutes with D, so

\[
 [G,D]=-G[K,D]G,\qquad\|[G,D]\|_{HS}^2\le\delta^{-4}\|[K,D]\|_{HS}^2.
\]

Sites at distance r lie in different cells with probability w_R(r)=min(r/R,1). Their conditional expected squared sign difference is 2. Average and cancel 2 to obtain

\[
 \sum_{i,j}w_R(|i-j|)|G_{ij}|^2
 \le\delta^{-4}\sum_{i,j}w_R(|i-j|)|K_{ij}|^2.
\tag{6.2}
\]

Since |K_ij|<=c/(pi|i-j|) off the diagonal, the right side divided by n is at most

\[
 \frac{2c^2}{\pi^2\delta^4}
 \left(H_{R-1}/R+\sum_{r=R}^\infty r^{-2}\right)
 \le\frac{2c^2}{\pi^2\delta^4}\frac{H_{R-1}+2}{R}.
\]

The alternative bound n^{-1}||G||_HS^2<=delta^{-2} gives the minimum in tau. QED. This proves an averaged physical tail, not an unproved entrywise inverse decay claim.

## 7. Effective finite-to-true and all-exterior passage

### 7.1 Finite response comparison

Partition V=[1,n] into the intersections of a uniformly shifted length-m grid with V. Their cores are disjoint; only two endpoint cores can be shortened. Splitting Phi into within-core pieces leaves crossing pair terms. Their absolute sum is at most C_log times crossing inverse energy. The crossing probability is min(|i-j|/m,1), so Lemma 4 pays n C_log tau(m). Chi is a subset and obeys the same bound.

For every full core whose length-L halo lies inside V, apply (5.10). Disjointness of the cores bounds the sum of all its exterior-energy costs by

\[
 n\frac{\Lambda}{2\delta^2}\tau(L+1),
\]

because every omitted site lies at distance at least L+1. The number of sites in shortened or halo-truncated exceptional cores is at most min(n,2(m+L)). For each exceptional core of size r, replace its expectation by r/m times the canonical stationary core expectation; both are bounded in magnitude by B_*r. This costs at most 4B_*(m+L).

For nonexceptional cores, stationarity gives the canonical expectation. Translation by one site swaps parity but leaves Chi's unordered even-odd sum unchanged. Combining the three errors proves (1.4)-(1.5) using (5.4). All actual words, including rare ones, enter their exact probabilities.

### 7.2 Identifying the entropy-rate Hessian

Stationarity and subadditivity imply H_n/n -> h pointwise. Given a tolerance, first choose m,L so epsilon_mL is small, then n large so the boundary term is small. Equation (1.4) makes H_n''/n uniformly Cauchy on J, with continuous limit g.

For f_n=H_n/n and distinct u,v in J,

\[
 f_n(v)-f_n(u)=(v-u)f_n'(u)+\int_u^v(v-t)f_n''(t)\,dt.
\]

Pointwise value convergence and uniform second-derivative convergence make f_n'(u) converge. Applying the same integral formula to arbitrary arguments identifies h as C^2 with h''=g. Overlapping compact legal intervals cover the open legal interval. Taking n to infinity in (1.4) proves (1.6). The mixed responses converge similarly; no two-variable infinite Hessian is assumed to name that limit.

### 7.3 Finite chords

For a_0<a_1, a_lambda=(1-lambda)a_0+lambda a_1, define

\[
 T_\lambda(t)=\begin{cases}
 (1-\lambda)(t-a_0),&a_0\le t\le a_\lambda,\\
 \lambda(a_1-t),&a_\lambda\le t\le a_1.
 \end{cases}
\]

Integration by parts gives Gap_lambda f=-integral T_lambda f'', and integral T_lambda=lambda(1-lambda)(a_1-a_0)^2/2. Therefore

\[
 \left|\operatorname{Gap}_\lambda(H_n/n)+\int T_\lambda W_{m,L}\right|
 \le\frac{\lambda(1-\lambda)(a_1-a_0)^2}{2}
 \left(\epsilon_{m,L}+4B_*(m+L)/n\right).
\tag{7.1}
\]

Taking limits of the three entropy values gives the same inequality for h without the boundary term. A continuum bound W_mL+epsilon_mL<=-eta implies Gap_lambda h>=eta lambda(1-lambda)(a_1-a_0)^2/2. A finite parameter grid is not such a continuum certificate.

### 7.4 Literal all-exterior object

On the actual infinite output space define

\[
 \mathsf A=K-\operatorname{diag}(1-Y),\qquad\mathsf G=\mathsf A^{-1}.
\]

For every sequence, S=diag(2Y-1) gives

\[
 \mathsf A=\tfrac12 S(I+2S(K-I/2)),\quad\|2S(K-I/2)\|\le1-2\delta<1.
\]

The inverse series converges and ||mathsf G||<=delta^{-1}. For interval projections P_N and u=mathsf G z, the exact Galerkin identity is

\[
 G_NP_Nz-P_Nu=G_NP_N\mathsf A(I-P_N)u.
\]

Its norm tends to zero, bounded by delta^{-1}||mathsf A|| ||(I-P_N)u||. Thus zero-extended finite inverses converge strongly to mathsf G, including each fixed row in l^2 by Hermitian symmetry. Bounded convergence in (5.8) gives for finite I subset A

\[
 \mathbb E[\mathsf G_{II}\mid Y_A]=(G_A)_{II}.
\tag{7.2}
\]

This is an actual score martingale identity (the longer manuscript's (7.11)).

The stationary infinite row obeys

\[
 \mathbb E\sum_r w_R(|r|)|\mathsf G(0,r)|^2\le\tau(R).
\tag{7.3}
\]

To justify passage from the finite averaged bound, fix B and Z_r=mathsf G(0,r), |r|<=B. Let

\[
 d_{N,r}=\mathbb E|Z_r-\mathbb E[Z_r\mid Y_{[-N,N]}]|^2\longrightarrow0.
\]

If an interval C contains [-N,N], (7.2) and L^2 projection yield

\[
 0\le\mathbb E|Z_r|^2-\mathbb E|G_C(0,r)|^2\le d_{N,r}.
\]

Apply the expected finite averaged bound to [1,n]. The n-2N interior rows, after translation, each contribute at least the truncated infinite row energy minus sum_{|r|<=B}w_R d_Nr. First n -> infinity, then N -> infinity proves the truncated (7.3). Monotone convergence as B increases proves the whole sum. No stationary root estimate is inferred merely by selecting one finite row.

For fixed I=[1,m], A=[1-L,m+L], take increasing finite supersets in (5.10). Row l^2 convergence, uniform norm bounds and continuity justify bounded convergence. Stationarity and (7.3) give

\[
 \frac1m|\mathbb E\Psi(\mathsf G_{II})-\mathbb E\Psi((G_A)_{II})|
 \le\frac{\Lambda}{2\delta^2}\tau(L+1),\quad\Psi=\Phi,\Chi.
\tag{7.4}
\]

This is an explicit fixed-core finite-observation-to-all-exterior second-response bound. Sending L to infinity in (1.6) yields

\[
 \left|h''+m^{-1}\mathbb E\Phi(\mathsf G_{II})\right|\le C_{\log}\tau(m).
\tag{7.5}
\]

Spatial truncation and reducing the observation domain are separately paid.

Finally, r_n=floor(sqrt(n)) in (1.4) and (1.6) gives

\[
 \sup_{a\in J}|H_n''/n-h''|
 \le2\epsilon_{r_n,r_n}+8B_*r_n/n
 =O_{\delta,c}(\log(n+1)/\sqrt n).
\tag{7.6}
\]

This is the longer manuscript's (7.16). It is fixed-gap, not a joint endpoint/noise result.

## 8. Correct-weight parity evaluation and the baseline-dependent bound

For an observation halo A, split into even word y and odd word z. With D_y,C,M_y,w_y as above, put

\[
 S_{y,z}=M_y-\operatorname{diag}(1-z),\quad T_{y,z}=S_{y,z}^{-1},
 \quad q_y(z)=(-1)^{|O|-|z|}\det S_{y,z}.
\]

All q_y(z)>0 and their sum is 1. Block inversion gives

\[
 G_{OO}=T,\quad G_{EO}=-D_y^{-1}CT,\quad
 G_{EE}=D_y^{-1}+D_y^{-1}CTC^*D_y^{-1},\quad G_{OE}=G_{EO}^*.
\tag{8.1}
\]

Thus

\[
 W_{m,L}=-m^{-1}\sum_yw_y\sum_zq_y(z)\Phi(G(y,z)_{II}),
\]
\[
 V_{m,L}=m^{-1}\sum_yw_y\sum_zq_y(z)\Chi(G(y,z)_{II}).
\tag{8.2}
\]

These are finite normalized actual-law sums, not equally weighted output words or averaged kernels.

Since B_n=H_n-e_n h_b(p),

\[
 B_n''=H_n''+e_n/[p(1-p)].
\]

Combining (3.7) and (1.4) controls all three moving-mask derivative terms by the finite reference W_mL+e_n/[np(1-p)] with error epsilon_mL+4B_*(m+L)/n. This is the combined conditional-information second-response interface; no separate I'' sign is assumed.

For Theorem 2, hold the even shift s fixed and differentiate only odd shift t. Write p_e=s+c/2, p_o=t+c/2. The conditional kernel is

\[
 M_y(s,t)=\left(p_o-c^2/(4p_e)\right)I+\alpha(p_e)R_y(p_e).
\tag{8.3}
\]

Now the even mask weights, alpha and R_y are fixed; only the scalar changes with slope 1. At s=t=a in the target interval, (3.6) rewrites M_y=bI+(37/40)R_y' with R_y'=alpha R_y/(37/40) a contraction and 0<b<3/40. This remains legal in a t-neighborhood, so the explicitly imported baseline gives

\[
 \mathscr H_{tt}(a,a)\le-|O|/50.
\]

Conditioning on odds instead gives mathscr H_ss<=-|E|/50. This argument uses finite contractions with the leakage retained. Unequal parity sizes do not cause an error. Then

\[
 H_n''=\mathscr H_{ss}+2\mathscr H_{st}+\mathscr H_{tt}
 \le-n/50-2\mathbb E\Chi(G_n).
\tag{8.4}
\]

Apply (1.5) to obtain (1.8)-(1.9). The mixed signed contribution has not been silently dropped; it is the actual finite witness V with the paid error.

## 9. Exact remaining sign obligation

A sufficient certificate is to find m,L>=1 and eta>0 such that for EVERY a in [1/50,3/100],

\[
 V_{m,L}(a)-\epsilon_{m,L}\ge-1/100+\eta/2.
\tag{9.1}
\]

Then H_n''<=-eta n+8B_*(m+L), and finite chords imply

\[
 \operatorname{Gap}_\lambda h\ge\eta\lambda(1-\lambda)(a_1-a_0)^2/2
\]

for every chord inside the target interval. No additional cyclic or all-exterior transfer remains after (9.1). The baseline-independent alternative is

\[
 \sup_{a\in J}(W_{m,L}(a)+\epsilon_{m,L})\le-\eta.
\tag{9.2}
\]

Neither inequality is proved here.

The constants are deliberately conservative. At delta=1/50,

\[
 \kappa=9025/776,\quad\Lambda=1486648002527/1204352,
 \quad C_{\log}=\log(9801/776).
\]

Lambda is about 1.234397e6, B_* about 6340.218, the uncapped tail prefactor about 1.143030e6, and the observation multiplier Lambda/(2delta^2) about 1.542996e9. Their product is about 1.763690e15 before (H_L+2)/(L+1). Small-halo negative samples do not overcome that error. These are analytic constants, not fitted errors, and they diverge as the channel gap closes.

## 10. Falsification and reproducible exact inputs

### 10.1 Moving weights cannot be frozen

At two true half-density sites put r=c^2/pi^2, x=4r and p=a+c/2. Conditional odd probabilities are M_1=p-r/p and M_0=p+r/(1-p), weighted by p and 1-p. At p=1/2, L_x=log((1+x)/(1-x))>0, so F_1'=(1+x)L_x and F_0'=-(1+x)L_x. Consequently

\[
 2\sum_yw_y'F_y'=4(1+x)L_x>0.
\]

The other terms give

\[
 \sum_yw_yF_y''=-4(1+x)/(1-x)-4xL_x,
\]
\[
 B_2''=-4(1+x)/(1-x)+4L_x,\quad H_2''=-8/(1-x)+4L_x.
\]

Thus the moving-weight term is positive even at the target contrast, while the total may remain negative.

### 10.2 The information term is not universally concave

At two sites and midpoint, let x=4c^2/pi^2, q=4/pi^2. The latent-conditioned odd entropy has second derivative -4/(1-qx), while the even marginal contributes -4. Hence the information remainder has

\[
 \mathcal I''=4+4/(1-qx)-8/(1-x)+4\log((1+x)/(1-x)).
\]

For c=1/2, a=1/4, x=1/pi^2<1/2 and q=4x. Using log((1+x)/(1-x))>=2x gives

\[
 \mathcal I''\ge16x^2-8x^2/(1-x)=8x^2(1-2x)/(1-x)>0.
\]

This disproves universal separate information concavity. It is not a counterexample at c=.95, nor to total entropy concavity.

### 10.3 Actual target-model conditional Jensen obstruction

Take true sites V={0,1,2,3,4,5}, rho=1/2, c=19/20, a=1/40. Observe A={0,1,2,3,4} with word y=(0,0,0,1,1), retain core I={2,3}, and reveal site 5. Let t=19/(20pi). The coarse masked matrix and coupling are

\[
 A_y=\begin{pmatrix}
 -1/2&t&0&-t/3&0\\
 t&-1/2&t&0&-t/3\\
 0&t&-1/2&t&0\\
 -t/3&0&t&1/2&t\\
 0&-t/3&0&t&1/2
 \end{pmatrix},\qquad b=(t/5,0,-t/3,0,t)^T.
\]

Put G=A_y^{-1}, M=G_II, v=(Gb)_I, q=1/2-b*Gb. The conditional fine matrices are M_1=M+vv*/q and M_0=M-vv*/(1-q), with actual probabilities q and 1-q. The coarse event probability is -det A_y>0. Define

\[
 \Delta_\Phi=q\Phi(M_1)+(1-q)\Phi(M_0)-\Phi(M),
\]
\[
 \Delta_\Chi=q\Chi(M_1)+(1-q)\Chi(M_0)-\Chi(M),\quad
 \mathcal Q=\|v\|^4/[q(1-q)].
\]

The standard-library directed integer-interval code certifies the rational decimal enclosures:

| Quantity | Outward interval |
|---|---|
| Pr(Y_A=y) | [0.014232864029787238, 0.014232864029787239] |
| q | [0.291967352633421847, 0.291967352633421848] |
| Delta_Phi | [-0.106585307859143407, -0.106585307859143406] |
| Delta_Chi | [-0.096395465271827624, -0.096395465271827623] |
| Q | [0.170309619791317635, 0.170309619791317636] |

Thus uncharged conditional Jensen for Phi or Chi fails inside the target model. A bound Delta_Phi>=-lambda Q requires lambda>5/8 for this word. This does not decide unconditional average monotonicity, the sign of V_mL, or entropy-rate concavity.

### 10.4 Why the certificate is mathematical evidence

The code stores intervals [l,u] as integers representing [l*2^-256,u*2^-256]. Every product and reciprocal uses integer outward rounding. Gaussian elimination permits only pivots whose intervals exclude zero. Induction through elementary operations encloses the exact determinants, inverse, Schur complements and potentials.

Pi is enclosed by Machin's identity pi=16 atan(1/5)-4 atan(1/239), using 96 alternating-series terms and a signed next-term bound. The identity follows from tan(2 atan(1/5))=5/12, tan(4 atan(1/5))=120/119 and subtraction of atan(1/239), with the angle in the correct quadrant.

For positive x, z=(x-1)/(x+1), |z|<=r<1, the logarithm uses

\[
 \log x=2\sum_{k=0}^{N-1}\frac{z^{2k+1}}{2k+1}+R_N,\qquad
 |R_N|\le\frac{2r^{2N+1}}{(2N+1)(1-r^2)},\quad N=384.
\]

The bound is the geometric tail after replacing later denominators by 2N+1. All constants and series operations are rational/dyadic. No library logarithm or pi enters the certificate. The displayed mathematical enclosures, the explicit inputs and algorithm are the evidence; a success message or checksum is not a proof.

## 11. Diagnostics and dependency ledger

The original delivered QWE09_checks.py provides a certificate mode and optional NumPy diagnostics. The diagnostics compare direct determinant jets, the complete-potential Hessian identities, and the full moving-weight conditional-odd jets. At n=2,4,6,8,10,12 and a=.02,.025,.03, the recorded floating discrepancies were below 7e-13. These are implementation checks, not continuum or volume certificates.

Recorded midpoint values (true Toeplitz):

| n | H_n'' | F_eo,n |
|---|---:|---:|
| 2 | -9.545467014232536 | -0.154930011623128 |
| 4 | -27.423750308635196 | -1.849316335469222 |
| 6 | -49.565521239251000 | -4.453338813257326 |
| 8 | -73.937110575228860 | -7.541810390559879 |
| 10 | -99.633052607314370 | -10.920435146909073 |
| 12 | -126.180128560707830 | -14.486433623466134 |

The local floating witness W_2,2(1/40) is about -8.67912856656642 and V_2,2 about 0.5516625753138781. Their rigorous transfer error above is far too large to certify the target sign.

Dependencies and scope:

- TASK, CONTRACT, TARGET from the Drive packet specify the frozen model and obligations.
- CLAUDE_CYCLE16_AUDIT supplies motivation and model distinctions; all needed parity formulas are rederived above.
- SA02_FULL_BLOCK supplies the credited inverse-score/Bellman strategy. Every identity and bound actually used here is rederived above; its original rational potential is not silently substituted for the full logarithm.
- The accepted arbitrary finite-contraction contrast-37/40 baseline with margin 1/50, recorded in S55_REVIEW Section 8, is imported ONLY for Theorem 2 and the separate-shift argument. The general transfer does not use it.
- S55 qualitative cyclic-to-true transfer is not used for a quantitative rate.
- S68 provides the scope caution that finite marginal convergence is not all-exterior conditional-response control. No sparse-defect expansion, endpoint pole, or joint-noise theorem is imported.
- The rho=1/3 S63 theorem is not transferred to half density; S64 length-KL convexity is not used as bias-curvature convexity.
- No RIP, Gaussian integration by parts, spectral/entropic independence, or count-entropy theorem is imported. No external priority/novelty claim is made.

## Final first-round scope

The first-round manuscript supplies proofs of the exact-log block payment, physical averaged tail, effective second-response and finite-chord interface, legitimate parity conditioning, and a target-slice sufficient inequality. The proofs remain author claims pending adversarial audit.

The target interval concavity is INCOMPLETE. The unresolved mathematical obligation is (9.1) or (9.2), or a stronger structural sign argument replacing them. The user's second round asks to attack that sign rather than count the interface itself as completion. Original source attachments and the accepted repository status are left unchanged.
