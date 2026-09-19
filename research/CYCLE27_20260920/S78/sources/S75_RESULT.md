# S75 RESULT — actual-weight star reveal monotonicity

## Status and scope

**PROVED:** a scale-free, actual-law averaged reveal theorem for one-center, one-parity stars. It applies to every `0<c<1` and every legal `0<a<1-c` in the half-density sine model. It includes an explicit positive drift, a polynomial-arithmetic-cost moment tool, and signed spatial truncation inside this geometry.

**DISPROVED:** unconditional nonnegative drift of every individual cross pair in arbitrary sine geometry. A three-site true-sine counterexample has an exact-rational interval certificate. Even the star theorem cannot generally be strengthened to conditioning on an old halo word: a second certified half-density counterexample demonstrates this.

**INCOMPLETE:** averaged drift for the full interval-core/two-parity-halo geometry, a globally affordable payment returning that geometry to the original Shannon entropy, and the requested high-contrast entropy-rate concavity theorem. No result for the full potential Phi is claimed here.

The new theorem concerns Chi, with each cross pair counted once. It does not use S73. All sources used from the supplied packet are the accepted score/reveal identities and the S72 comparison and rate interfaces.

## 1. The tool

### 1.1 Input class

Let `j` be a center and let `E` be a collection of leaves. On any finite subset of `{j} union E`, use the kernel

\[
 K_{jj}=d,\qquad K_{ik}=d\,\mathbf1_{i=k}\ (i,k\in E),
 \qquad K_{ij}=z_i,
\]

where

\[
 0<d<1,\quad u=1-d,\quad w_i=|z_i|^2,
 \qquad T:=\sum_{i\in E}w_i<\min(d,u)^2.                    \tag{1}
\]

Thus the kernel is a strict Hermitian contraction: its nontrivial eigenvalues are `d +- sqrt(T)`. A countable leaf set is permitted through its consistent finite marginals.

Fix a core `I={j} union C` and an observed set `A={j} union B`, with `C subset B subset E`. Give center and leaves opposite parity labels, so that

\[
 \Chi((G_A)_{II})=\sum_{i\in C}f_{ij}(G_A).
\]

A reveal adds a leaf `r in E\B`; no second center is observed.

Define

\[
 C_\star(d)=\frac{256\{d^{-3}+(1-d)^{-3}\}}{d(1-d)}.        \tag{2}
\]

### 1.2 Output: actual-weight signed drift

For the actual conditional probability `q=P(Y_r=1|Y_A)`, the tool proves

\[
\boxed{
 \mathbb E\Delta_\Chi(Y_A)
 \ge C_\star(d)\,w_r^2\sum_{i\in C}w_i^3\ge0.
}                                                         \tag{3}
\]

The expectation includes **every** old word and uses the actual reveal weights. In particular, `q` is not replaced by `d` while conditioning on the observed center.

For `B subset B'`, with the core fixed, (3) telescopes to

\[
\boxed{
 \mathbb E\Chi((G_{\{j\}\cup B'})_{II})
 -\mathbb E\Chi((G_{\{j\}\cup B})_{II})
 \ge C_\star(d)
 \left(\sum_{i\in C}w_i^3\right)
 \left(\sum_{r\in B'\setminus B}w_r^2\right).
}                                                         \tag{4}
\]

There is no negative compensator or endpoint correction in this comparison.

### 1.3 Sine-model scope

Take `rho=1/2`, choose any integer center `j`, and allow only leaves of the opposite parity. Then

\[
 d=a+\frac c2,\qquad
 w_i=\frac{c^2}{\pi^2(i-j)^2},\qquad
 \sum_{i-j\text{ odd}}w_i=\frac{c^2}{4}.
\]

Since legal `a` implies `min(d,1-d)>c/2`, condition (1) holds for every legal `a` and every `0<c<1`. The observed marginal `d` is not the noise bias `p_noise=a/(1-c)`.

The row-sum identity follows from the sum of inverse squares over odd integers. No finite sine compression is treated as a projection. Sites outside the stated star are marginalized, not conditioned on.

## 2. Exact two-output averaging

For a conditional two-site kernel

\[
 C=\begin{pmatrix}\alpha&z\\\bar z&\beta\end{pmatrix},
 \qquad s=|z|^2,
\]

write its actual four probabilities as

\[
 p_{11}=\alpha\beta-s,\quad
 p_{10}=\alpha(1-\beta)+s,\quad
 p_{01}=(1-\alpha)\beta+s,\quad
 p_{00}=(1-\alpha)(1-\beta)-s.
\]

Define

\[
 \mathcal F(\alpha,\beta,s)
 =s\left(\frac1{p_{11}}+\frac1{p_{10}}+
          \frac1{p_{01}}+\frac1{p_{00}}\right)
   +\log\frac{p_{11}p_{00}}{p_{10}p_{01}}.                 \tag{5}
\]

**Two-output averaging identity.**

\[
 \mathbb E f_{ij}((C-\operatorname{diag}(1-Y))^{-1})
 =\mathcal F(\alpha,\beta,s).                              \tag{6}
\]

To prove it, let `D_y=det(C-diag(1-y))`. Then

\[
 D_y=\sigma_i\sigma_jp_y,\quad
 h=\frac{s}{D_y^2},\quad
 x=\frac{D_y+s}{D_y^2},\quad x-h=\frac1{D_y}.
\]

Consequently,

\[
 p_y f_{ij}=\frac{s}{p_y}
 +\sigma_i\sigma_j\log\frac{D_y}{D_y+s}.
\]

Summing the four logarithms gives the log odds ratio in (5): the independent-cell denominators cancel. This proves (6) with actual weights, including opposite-sign words.

## 3. Complete proof of the star theorem

### 3.1 Exact conditional star reduction

The leaf marginal has kernel `d I`, hence the leaf outputs are independent Bernoulli(`d`). This is independence of a **marginal**, not independence conditional on the center.

For a selected pair `(i,j)`, condition on the other observed leaves `B\{i}`. The Schur complement leaves the pair kernel

\[
 \begin{pmatrix}d&z_i\\\bar z_i&\beta\end{pmatrix},\qquad
 \beta=d+\sum_{k\in B\setminus\{i\}}
       w_k\left(\frac{1-Y_k}{1-d}-\frac{Y_k}{d}\right).     \tag{7}
\]

Therefore

\[
 \mathbb E f_{ij}(G_A)=\mathbb E\mathcal F(d,\beta,w_i).     \tag{8}
\]

Adding a leaf adds an independent summand in (7), **after** the two core outputs have been summed as in (6). This is a reordering of the exact joint expectation. By the tower property its change is precisely the expectation of the original `q`-weighted reveal drift.

### 3.2 Particle-hole reduction

Complementing every output and replacing `K` by `I-K` sends `G` to `-G`, leaving `f` and `Chi` unchanged. It replaces `d` by `1-d` and preserves all `w_i`. It suffices to prove the theorem for `d>=1/2`; write `u=1-d<=d`.

Fix `s=w_i`, and set

\[
 t=\beta-\tfrac12=b+\sum_k\xi_k,\qquad b=d-\tfrac12\ge0,
\]

where independently

\[
 \xi_k=\begin{cases}-w_k/d,&\text{with probability }d,\\
                    w_k/u,&\text{with probability }u.
       \end{cases}                                       \tag{9}
\]

Every integer moment of `xi_k` is nonnegative:

\[
 \mathbb E\xi_k^\ell
 =w_k^\ell\{(-1)^\ell d^{1-\ell}+u^{1-\ell}\}\ge0.       \tag{10}
\]

For `ell=1` it is zero. For positive even `ell` it is positive. For odd `ell>=3`, the inequality follows from `u<=d`. By independence and the multinomial expansion, every moment of `t` is nonnegative too.

### 3.3 Positive Taylor coefficients of the averaged pair function

For

\[
 |t|<R_s:=\tfrac12-\frac{s}{u},
\]

all four independent-cell products exceed `s`, and the absolutely convergent expansion is

\[
\begin{aligned}
\mathcal F(d,\beta,s)
={}&\sum_{n\ge2}\frac{n-1}{n}s^n
 \left[(d\beta)^{-n}+(u(1-\beta))^{-n}\right.\\
 &\hspace{34mm}\left.+(-1)^{n-1}
       \{(d(1-\beta))^{-n}+(u\beta)^{-n}\}\right].          \tag{11}
\end{aligned}
\]

For odd `n`, the bracket becomes

\[
 (d^{-n}+u^{-n})\{(\tfrac12+t)^{-n}+(\tfrac12-t)^{-n}\},
\]

which has nonnegative even Taylor coefficients and zero odd coefficients.

For even `n`, it becomes

\[
 (d^{-n}-u^{-n})\{(\tfrac12+t)^{-n}-(\tfrac12-t)^{-n}\}.
\]

The first factor is nonpositive; the second has nonpositive odd Taylor coefficients and zero even coefficients. Their product again has nonnegative coefficients. Thus

\[
 \mathcal F(d,\tfrac12+t,s)=\sum_{k\ge0}b_k(d,s)t^k,
 \qquad b_k(d,s)\ge0.                                    \tag{12}
\]

Explicitly,

\[
 b_k=\sum_{\substack{n\ge2\\n+k\text{ odd}}}
 \frac{n-1}{n}s^n2^{n+k+1}\binom{n+k-1}{k}
 \{u^{-n}+(-1)^k d^{-n}\}.                               \tag{13}
\]

In particular, retaining `n=3,k=2` gives

\[
 b_2(d,s)\ge256s^3(d^{-3}+u^{-3}).                         \tag{14}
\]

### 3.4 The entire actual support lies inside the convergence domain

Let `S` be the total weight of all other leaves involved before or after the reveal. From (9),

\[
 |t|\le r_s:=d-\tfrac12+\frac S u.
\]

By (1), `S+s<u^2`. Therefore

\[
 r_s<\tfrac12-\frac s u=R_s.                              \tag{15}
\]

This proves uniform absolute convergence on the entire support, not just a typical-word subset. Expectations and the Taylor series can consequently be interchanged.

### 3.5 Actual-law moment cancellation gives the drift

For the new independent centered increment `xi_r`,

\[
 \mathbb E[(t+\xi_r)^k-t^k]
 =\sum_{\ell=1}^k\binom{k}{\ell}
       \mathbb E t^{k-\ell}\,\mathbb E\xi_r^\ell\ge0.      \tag{16}
\]

Multiplying by the nonnegative coefficients in (12) proves nonnegative unconditional pair drift. Retaining only `k=2`, using (14) and

\[
 \mathbb E\xi_r^2=\frac{w_r^2}{du},
\]

gives

\[
 \mathbb E\Delta_{f_{ij}}
 \ge C_\star(d)\,w_i^3w_r^2.                             \tag{17}
\]

Summing (17) over the core leaves proves (3); successive reveals prove (4). Particle-hole complementation covers `d<1/2`.

This proof is not a pointwise convexity argument. Odd moments of the actual biased Bernoulli increments are essential away from the midpoint.

### 3.6 An explicit finite-star lower bound

Starting a selected pair from its two-site marginal and revealing the other leaves yields

\[
\boxed{
 \mathbb E\Chi((G_A)_{II})
 \ge\sum_{i\in C}\mathcal F(d,d,w_i)
 +C_\star(d)\sum_{i\in C}w_i^3
                 \sum_{k\in B\setminus\{i\}}w_k^2.
}                                                        \tag{18}
\]

Every base term is nonnegative, by (12) evaluated at `t=d-1/2`, after reflection if needed. If `w_i>0`, the base term is strictly positive. In (17), drift is strictly positive whenever both relevant couplings are nonzero.

For countably many leaves, the series (7) converges absolutely because the weights are summable. The strict gap in (1) supplies the uniform convergence margin in (15). Bounded convergence extends all displayed comparisons to increasing infinite stars. On a fixed compact legal sine parameter interval, these margins can be chosen uniformly.

## 4. A computational tool without all-word enumeration

Fix a selected pair and work after reflection with `d>=1/2`. Let `M_k=E t^k`. Initialize `M_k=(d-1/2)^k`. Adding a leaf updates the moments by

\[
 M_k^{\rm new}=\sum_{\ell=0}^k\binom{k}{\ell}
                   M_{k-\ell}\mu_\ell(w),
\]

where `mu_0=1` and `mu_ell` is (10). Moments through degree `D` cost `O(D^2)` arithmetic operations per leaf, rather than enumeration over its output words.

For any `r_s<R'<R_s`,

\[
 L_D:=\sum_{k=0}^D b_kM_k\le\mathbb E\mathcal F(d,\beta,s),
\]

and

\[
\boxed{
 0\le\mathbb E\mathcal F-L_D
 \le\left(\frac{r_s}{R'}\right)^{D+1}
          \mathcal F(d,\tfrac12+R',s).
}                                                        \tag{19}
\]

Indeed, each omitted expected Taylor term is nonnegative, and its absolute size is at most `b_k r_s^k`. Summing against the nonnegative generating series at `R'` proves (19).

This is a quantitative approximation theorem, not a renamed unknown. Gap dependence is explicit: the degree cost can deteriorate when the strict gap closes. No endpoint-uniform cost is asserted. The coefficients can be obtained from (13), or by differentiating the four rational/logarithmic scalar terms in (5).

## 5. Spatial truncation inside the star

For a sine star set

\[
 e=\min(d,1-d),\qquad \gamma_\star=e^2-\frac{c^2}{4}>0.
\]

For the selected pair, the other-leaf weight is at most `c^2/4-s`. Formula (7) implies that every independent-cell product in (11) is at least `gamma_star+s`. Summing the absolute series therefore gives

\[
 |\mathcal F(d,\beta,s)|\le\frac{4s^2}{\gamma_\star^2}.
                                                               \tag{20}
\]

At the midpoint `d=1/2`, all even `n` in (11) vanish, and the sharper estimate is

\[
 0\le\mathcal F(\tfrac12,\beta,s)
 \le\frac{4s^3}{\gamma_\star^3}.                            \tag{21}
\]

For completeness, the lower bound on the independent-cell products follows from

\[
 \min(\beta,1-\beta)\ge e-S/e,
 \qquad e\min(\beta,1-\beta)\ge e^2-S\ge\gamma_\star+s.
\]

With `x=s/(gamma_star+s)`, the absolute series is bounded by `4 sum_{n>=2} x^n`, and at the midpoint by `4 sum_{n>=3} x^n`; these imply (20) and (21).

Because the unconditional pair expectations are nonnegative, adding long pairs to a star core has no negative one-sided cost. Their two-sided omitted tail, for integer `R>=2`, is at most

\[
 \sum_{|i-j|\ge R}\mathbb E f_{ij}(G_{\rm star})
 \le\frac{8c^4}{3\pi^4\gamma_\star^2(R-1)^3},              \tag{22}
\]

or, at the midpoint,

\[
 \sum_{|i-j|\ge R}\mathbb E f_{ij}(G_{\rm star})
 \le\frac{8c^6}{5\pi^6\gamma_\star^3(R-1)^5}.              \tag{23}
\]

These follow by bounding the two-sided inverse-power sums by integrals. They concern star scores, not the full two-parity score.

As a concrete exact-certificate example, at `c=19/20`, `a=1/40`, a nearest center-leaf pair has `s=c^2/pi^2`, and

\[
 \mathcal F(\tfrac12,\tfrac12,s)
 =4\left\{\frac{4s}{1-16s^2}-\operatorname{atanh}(4s)\right\}.
\]

Using `sum_{odd n in Z} |K(0,n)|^4=c^4/48`, (18) gives

\[
 \mathbb E f_{\rm nearest}(G_{\rm infinite\ star})
 \ge \mathcal F(\tfrac12,\tfrac12,s)
       +16384s^3\left(\frac{c^4}{48}-s^2\right)
 >0.26275.                                                \tag{24}
\]

The last strict inequality has been certified by the exact-rational interval program. It is not a claim about the full-line inverse score or the standard `V_{m,L}`.

## 6. Two model-valid falsification tests

### 6.1 Unrestricted unconditional pair drift is false

Use

\[
 \rho=\frac9{20},\quad c=\frac{19}{20},\quad a=\frac1{200},
 \qquad I=A=\{0,3\},\quad r=4.
\]

These are genuine principal compressions of the sine kernel; they can be embedded in the interval `{0,1,2,3,4}` with the other sites unobserved. The two core sites have opposite parity, so `Chi=f_{03}`.

Let

\[
 d=\frac{173}{400},\quad
 z=-\frac{c\cos(3\pi/20)}{3\pi},\quad
 b_0=-\frac{c\sin(\pi/5)}{4\pi},\quad
 b_3=\frac{c\cos(\pi/20)}{\pi}.
\]

The pair kernels conditional on the revealed output are

\[
 C_1=\begin{pmatrix}d&z\\z&d\end{pmatrix}
       -\frac1d\begin{pmatrix}b_0\\b_3\end{pmatrix}(b_0,b_3),
\]

\[
 C_0=\begin{pmatrix}d&z\\z&d\end{pmatrix}
       +\frac1{1-d}\begin{pmatrix}b_0\\b_3\end{pmatrix}(b_0,b_3).
\]

By exact averaging,

\[
 \mathbb E\Delta_\Chi
 =d\mathcal F(C_1)+(1-d)\mathcal F(C_0)-\mathcal F(d,d,z^2),
\]

where `F(C)` means (5) applied to its two diagonals and squared off-diagonal. The certified enclosure is

\[
\boxed{\mathbb E\Delta_\Chi
 \in[-0.000177080,-0.000177078]<0.}                         \tag{25}
\]

Here `d` is the marginal reveal probability **after averaging the pair**; the actual conditional reveal probability given the pair was not frozen. All eight joint configurations are included.

This refutes arbitrary-sine, individual-pair zero-payment monotonicity. It does not refute a full interval-core Phi theorem, a summed interval-core Chi theorem, or entropy concavity.

### 6.2 Conditioning on an old star background can reverse the sign

Even within half-density stars, the theorem must remain unconditional. Use

\[
 c=\frac{19}{20},\quad a=\frac1{2000},\quad d=\frac{951}{2000}.
\]

Take center `0`, core leaf `7`, old background leaves `{-1,1}` fixed to `00`, and reveal leaf `-3`. Put

\[
 w=\frac{c^2}{\pi^2},\quad s=\frac w{49},\quad v=\frac w9,
 \quad\beta=d+\frac{2w}{1-d}.
\]

After averaging the core pair, but still conditioning on that old background, the drift is

\[
 d\mathcal F(d,\beta-v/d,s)
 +(1-d)\mathcal F(d,\beta+v/(1-d),s)
 -\mathcal F(d,\beta,s).
\]

Its certified enclosure is

\[
 [-0.00000074327,-0.00000074325]<0.                         \tag{26}
\]

Averaging **all four** old-background words gives instead

\[
 \mathbb E\Delta_{f_{07}}
 \in[0.000013875271794819793250,
       0.000013875271794819793251]>0.                      \tag{27}
\]

Thus this is a genuine actual-weight cancellation theorem, not hidden conditional convexity or deletion of unfavorable words.

### 6.3 Certificate method

The accompanying `s75_certificate.py` uses standard-library Python only. Interval endpoints are integers on a `10^-80` grid; every operation rounds outward. It encloses pi using Machin's identity and alternating arctangent series. The sine and cosine arguments are at most `pi/5<1`, with alternating-series error bounds. For logarithms it uses

\[
 \log x=2\sum_{k=0}^{M-1}\frac{z^{2k+1}}{2k+1}+R_M,
 \quad z=\frac{x-1}{x+1},
\]

\[
 |R_M|\le\frac{2|z|^{2M+1}}{(2M+1)(1-|z|^2)}.
\]

Thus (25)--(27) and the last inequality in (24) are interval certificates with explicit analytic tails, not rounded numerical signs.

## 7. Exact interface to the original Shannon entropy

The theorem eliminates observation loss when the entire observed geometry remains a one-center star. It also controls pair truncation inside that star. It does **not** eliminate either full standard-halo completion or the full-score core/pair truncation.

Here is an explicit interface, retaining both unpaid terms.

At `rho=1/2`, let

\[
 I=\{1,2\},\quad A_L=[1-L,2+L],\quad
 A_L^\star=\{2\}\cup(A_L\cap\{\text{odd sites}\}).
\]

Let `L_L(a)` denote the explicit right side of (18) for the one core pair and this star. Define the genuine missing-parity energy

\[
 \mathscr D_L=
 \mathbb E\sum_{i\in I}\sum_{r\in A_L\setminus A_L^\star}
                       |G_{A_L}(i,r)|^2.
\]

The accepted S72 comparison, applied only to the still-unpaid completion, gives

\[
 V_{2,L}\ge\frac12\{L_L(a)-\Gamma_\Chi\eta_\delta\mathscr D_L\}.
                                                               \tag{28}
\]

Its Ward bound gives the explicit uniform payment

\[
 0\le\mathscr D_L\le2(2/\delta-4).                         \tag{29}
\]

Inserting (28) into the accepted half-density `c=19/20` rate interface yields

\[
\boxed{
\begin{aligned}
 h''(a)\le{}&-\frac1{50}-L_L(a)
   +\Gamma_\Chi\eta_\delta\mathscr D_L\\
 &+2C_{\log}\widehat\tau(2)
   +2\Gamma_\Chi\eta_\delta\widehat\tau(L+1).
\end{aligned}}                                             \tag{30}
\]

The `mathscr D_L` term pays the missing, nearby opposite-parity observations. The `2 C_log tauhat(2)` term is the separate full-score pair/core truncation. The last term is the ordinary far observation tail. None has been silently signed or removed.

For `J=[.02,.03]`, `c=.95`, `delta=.02`, the two residual envelope payments as `L` tends to infinity are approximately

\[
 2C_{\log}(2/\delta-4)=486.92874,
\]

\[
 2\Gamma_\Chi\eta_\delta(2/\delta-4)=107488.02023.
\]

Their total is approximately `107974.94896`, before subtracting `1/50+L_infinity(a)`. The certified midpoint star lower bound in (24) cannot pay this envelope. This is a failure of this full-entropy certificate, not a counterexample to entropy concavity.

### Legal finite-to-rate use

All new inequalities above are finite-volume comparisons of actual score potentials at fixed `a`; they hold throughout every compact legal parameter interval. Equation (30) uses the already accepted S72 finite-to-rate interface. No entropy-value error is differentiated, and no moving background derivative is dropped. Passing `L` to infinity in this bound is justified by the star convergence proved above, the uniform cap (29), and the vanishing accepted far tail.

For a future successful finite-volume bound, the safe alternative is to integrate first. If throughout a parameter interval

\[
 (H_N/N)''\le-\mu+b_N,\qquad b_N\longrightarrow0,
\]

then at `a_t=(1-t)x+ty`,

\[
 \frac{H_N(a_t)}N\ge(1-t)\frac{H_N(x)}N+t\frac{H_N(y)}N
       +\frac{\mu-b_N}{2}t(1-t)(y-x)^2.
\]

Passing the entropy values to their rate limit gives the same chord inequality for `h`. The present residual payments do not establish such a positive `mu`.

## 8. Sources and actual run status

The complete supplied packet was successfully read through the web retrieval tool:

`https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle19-harvest-20260919/research/CYCLE25_20260920/S75/PACKET.md`

It contains the S72 visible result, its PR61 independent review, and the earlier S72 task. No S73 manuscript was used. A direct container `curl` attempt failed at DNS resolution; this did not prevent reading the packet through web retrieval. No repository checkout, PR action, shared-status edit, or external-agent execution was performed.

The following commands were actually run successfully in this session:

```
python /mnt/data/S75/s75_certificate.py
python /mnt/data/S75/s75_diagnostics.py
```

The first returned `PASS_EXACT_RATIONAL_INTERVAL_CERTIFICATES`. Its full enclosures are in `S75_CERTIFICATES.json`.

The second returned `PASS_FLOAT_DIAGNOSTICS_NOT_CERTIFICATE`. With seed 7504 it independently compared direct full-word score evaluation against the reduced pair formula on 60 legal stars, through seven total sites, using NumPy 2.3.5. The maximum discrepancy was `5.551115123125783e-16`; the minimum observed drift minus the proved explicit lower bound was `2.96312647326607e-10`. These checks support implementation consistency, not the universal proof.

The proof in Sections 2--5, rather than numerical extrapolation, establishes the star theorem.

## 9. Final separation

**PROVED:** exact pair averaging; actual-weight averaged star reveal monotonicity with explicit positive drift; zero-loss telescoping for that reveal class; a polynomial-arithmetic-cost moment approximation with error bound; nonnegative long-pair additions and quantitative star spatial tails; and the explicit, still-unaffordable original-entropy interface (30).

**DISPROVED:** unrestricted individual-pair averaged positivity in sine geometry; and positivity after conditioning on every old star background, even after averaging the core pair.

**INCOMPLETE:** the full two-parity/interval-core averaged reveal problem; a globally affordable original-Shannon compensator; removal of the full-score core/pair tail; and concavity for every fixed `c in (37/40,1)`, every density, and every legal `a`.
