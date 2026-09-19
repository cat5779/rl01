# S67 — Actual-law acceleration: a proved uniform bound, a finite-window reduction, and the remaining deficit

<!-- S67_LOCAL_FISHER_SUPPLEMENT_BEGIN -->

## Strengthened result: finite local-score allocation (PROVED; rate objective still INCOMPLETE)

This section records the strongest bound obtained during the final verification pass. The all-volume bound in the body below remains valid but is weaker. No positive entropy-rate chord, interval theorem, or all-parameter theorem is asserted.

Write
\[
 c_{16}=\mathcal C_{16}/16,\qquad s=b(1-b)=39/1600,
 \qquad \kappa=3/2,
 \qquad \tau=(c/\pi)^2.
\]
Define the explicit constant
\[
 d_*:=2+\frac{2}{1-64\tau^2}.
\]
For the benchmark chord, let the Green weight and likelihood-transport factor be
\[
 G(a)=\begin{cases}\tfrac12(a-a_0),&a_0\le a\le b,\\
 \tfrac12(a_1-a),&b\le a\le a_1,
 \end{cases}
\]
\[
 R(a)=\begin{cases}(1-a)/(39a),&a\le b,\\
 (a+c)/(39(1-a-c)),&a\ge b.
 \end{cases}
\]
Thus \(\int G=1/80000\), and reflection about \(b\) preserves \(R\).

Let
\[
 U_0:=\kappa\int_{a_0}^{a_1}G(a)
        \left(\frac{R(a)^3}{s}-4R(a)\right)da,
\]
\[
 U_3:=\kappa\int_{a_0}^{a_1}G(a)
        \left(\frac{R(a)^3}{s}-d_*\right)da,
 \qquad
 \beta_3:=\frac{3(d_*-4)}{80000}.
\]
All these constants are explicit, not new unknown acceleration remainders. Exact rational arithmetic, using series enclosures for \(\pi\) and \(\log(5/4)\), verifies
\[
 0<U_3<U_0<0.000887,\qquad U_3<0.000850,
 \qquad 0<\beta_3<0.000087.
\]
The tighter numerical enclosures are recorded in `certificates/rational_core.json`; `code/verify_rational_core.py` reproduces them using only the Python standard library.

**Theorem S67-F.** For every integer \(n\ge3\), for the frozen benchmark parameters and the full configuration laws,
\[
 \frac{\mathcal C_n}{n}
 \le \min\{U_0,U_3+\beta_3/n\}.
 \tag{F.1}
\]
In fact, the nonnegative finite-compression leakage term in (F.8) below can be subtracted from both members of this minimum. Consequently, for every \(M\ge16\),
\[
 A_M\le \min\{U_0,U_3+\beta_3/M\}-c_{16},
 \tag{F.2}
\]
and
\[
 \limsup_{N\to\infty}A_{16\,2^N}
 \le U_3-c_{16}
 <0.000703319519674116052447806952.
 \tag{F.3}
\]
This is **not** within the reviewed available budget
\[
 \gamma_{16}+B_{16}
 \in[0.000245932000395801628841632655,
       0.000245932000395801628841632657].
\]
More decisively, the exact calculation gives \(U_3-C_*>0\), where
\[
 C_*:=c_{16}+\gamma_{16}+B_{16}
 \in[0.000392612480721685576393825703,
       0.000392612480721685576393825706].
\]
Thus even the tighter computed value of \(U_3\), not just its rounded upper bound, fails to pay the obligation. An upper bound exceeding the cap is a limitation of this proof, **not a disproof of the desired chord**.

### F.1. Reusable local-score projection lemma

Let \(P_\theta\) be a strictly positive finite probability model, differentiable in a scalar parameter \(\theta_i\), and let \(X_W\) be a marginal that retains this parameter. Write \(s_i(X)=\partial_i\log p_\theta(X)\) and \(s_i^W(X_W)=\partial_i\log p_{\theta,W}(X_W)\). Differentiating the finite marginal sum gives
\[
 E_\theta[s_i(X)\mid X_W]=s_i^W(X_W).
 \tag{F.4}
\]
Conditional Jensen therefore gives
\[
 E_\theta s_i(X)^2\ge E_\theta(s_i^W(X_W))^2.
 \tag{F.5}
\]
This is the classical score-projection/data-processing property of Fisher information, proved here to specify its exact scope. It concerns a **local diagonal parameter**, not the scalar parameter changing every diagonal simultaneously.

For a DPP, put \(B_a(x)=(K_{a,n}-D_x)^{-1}\), where \((D_x)_{ii}=1-x_i\). The local score is \((B_a)_{ii}\). If the fully conditional reference probability of the observed bit is \(p_b(x_i\mid x_{-i})\), then
\[
 (B_b)_{ii}=\frac{2x_i-1}{p_b(x_i\mid x_{-i})}.
\]
The one-bit case of the likelihood-transport lemma proved in the body yields
\[
 R(a)^{-1}\le
 \frac{p_a(x_i\mid x_{-i})}{p_b(x_i\mid x_{-i})}
 \le R(a).
\]
Hence, **pointwise in the full actual configuration**,
\[
 |(B_b)_{ii}|^2\ge R(a)^{-2}|(B_a)_{ii}|^2.
 \tag{F.6}
\]
Combining (F.5) and (F.6) converts any finite-window lower bound on the actual local diagonal Fisher information into a lower bound on the full-volume reference-score square. Neither law is frozen incorrectly: (F.5) is evaluated under the actual law \(P_a\), and (F.6) is pointwise before taking that expectation.

### F.2. An analytic three-site input throughout the actual chord

Choose a central site and its two nearest neighbors. At \(\rho=1/2\), the two exterior sites have zero mutual kernel entry and therefore independent Bernoulli marginals with parameter
\[
 p=a+c/2\in[0.495,0.505].
\]
Let \(k\) be the number of occupied exterior sites. Their actual probability is
\(\binom2k p^k(1-p)^{2-k}\), and the central conditional probability is
\[
 r_k=p-\tau\left(\frac{k}{p}-\frac{2-k}{1-p}\right).
\]
The three-site diagonal Fisher information for the central **local diagonal** parameter is exactly
\[
 d_3(a)=\sum_{k=0}^2
 \binom2k\frac{p^k(1-p)^{2-k}}{r_k(1-r_k)}.
 \tag{F.7}
\]
All four exterior configurations are included; the multiplicity two for \(k=1\) is explicit.

We now prove \(d_3(a)\ge d_*\) on the whole actual chord. Set
\[
 x=(2p-1)^2\in[0,10^{-4}],\qquad v=p(1-p)=(1-x)/4,
\]
\[
 E(x)=(1-8\tau)^2-(2+16\tau)x+x^2.
\]
Elementary algebra decomposes (F.7) as
\[
 d_3(a)=D_{02}(x)+D_1(x),
\]
\[
 D_{02}(x)=
 \frac{2(1+x+8\tau)}{1-x+8\tau}
 +\frac{128\tau^2(1+x-8\tau)}{(1-x+8\tau)E(x)},
\]
\[
 D_1(x)=\frac{2v^3}{v^3-x\tau(v+\tau)}.
\]
The rational enclosure \(0.09<\tau<0.092\) is sufficient for every sign used here. On the stated range, \(1+x-8\tau>0\), \(1-x+8\tau>0\), \(E(x)>0\), and \(E'(x)<0\). For example,
\(E(x)\ge0.264^2-3.472\cdot10^{-4}>0\).
Also \(v^3-x\tau(v+\tau)>0\), either from the positive conditional probabilities or directly from \(v\ge0.249975\) and \(x\tau(v+\tau)\le10^{-4}\cdot0.092\cdot0.342\).

Each positive ratio in \(D_{02}\) increases with \(x\): its numerator increases and its positive denominator decreases. Thus
\[
 D_{02}(x)\ge D_{02}(0)=\frac{2}{1-64\tau^2}.
\]
The nonnegative subtraction in the denominator of \(D_1\) gives \(D_1(x)\ge2\). Therefore \(d_3(a)\ge d_*\), as claimed. This proof is analytic and uniform in \(a\); no differentiation of an entropy-value asymptotic error and no endpoint expansion is used.

### F.3. Full-volume allocation, including the finite boundary and leakage

For each of the \(n-2\) interior sites, use its three-site window in (F.5). For either boundary site, the one-site marginal Fisher information is \(1/[p(1-p)]\ge4\). Equations (F.5)–(F.7) give
\[
 \frac1n\sum_iE_a|(B_b)_{ii}|^2
 \ge R(a)^{-2}\left[(1-2/n)d_*+8/n\right].
\]
The signed-resolvent identity proved below is
\[
 sB_b^2+c^2B_b(Q_n-Q_n^2)B_b
   =\tfrac12(S_xB_b+B_bS_x)-I.
\]
The same actual-law one-bit transport gives
\(E_a[(S_x)_{ii}(B_b)_{ii}]\le1+R(a)\). The bounded-odds binary inequality and two-bit transport give
\[
 \sum_{i<j}E_{a,-ij}J^b_{ij}
 \le\kappa R(a)^2\sum_{i<j}E_a|(B_b)_{ij}|^2.
\]
Insert these estimates in the exact Green representation of \(\mathcal C_n\). The result is
\[
 \frac{\mathcal C_n}{n}
 \le U_3+\frac{\beta_3}{n}-\Lambda_n,
 \tag{F.8}
\]
where
\[
 \Lambda_n=\frac{\kappa c^2}{sn}
 \int_{a_0}^{a_1}G(a)R(a)^2
 E_a\operatorname{tr}\!\left[B_b(Q_n-Q_n^2)B_b\right]da\ge0.
\]
This proves the asserted finite boundary coefficient and retains finite-compression leakage with its correct favorable sign. Dropping \(\Lambda_n\), or taking the minimum with the independently proved \(U_0-\Lambda_n\) estimate, proves (F.1)–(F.3).

More generally, an odd window of length \(m\) with a certified actual local diagonal Fisher lower bound \(d_m(a)\ge4\) gives the verifiable sufficient estimate
\[
 \frac{\mathcal C_n}{n}
 \le\kappa\int G(a)\left[
 \frac{R(a)^3}{s}-d_m(a)
 +\frac{m-1}{n}(d_m(a)-4)\right]da-\Lambda_n,
 \qquad n\ge m.
\]
This is a finite-input score-allocation mechanism, not an assumption equivalent to the unknown \(A_n\). Larger windows have not been certified here to close the target.


### F.3a. PROVED obstruction to closing by larger Fisher windows alone

The preceding finite-input mechanism has a rigorous limitation. Throughout the actual chord, the infinite-compression conditional-odds bounds give
\[
 \ell_+(a)=\tfrac12\left(\frac{a}{1-a}
                    +\frac{a+c}{1-a-c}\right),\qquad
 \ell_-(a)=\tfrac12\left(\frac{1-a}{a}
                    +\frac{1-a-c}{a+c}\right).
\]
The first increases and the second decreases with \(a\). Consequently,
\[
 \max\{\ell_+(a),\ell_-(a)\}
 \le M_{\rm act}:=2378/97
 \qquad(a\in[0.02,0.03]).
\]
Every fully conditional actual occupation probability, in every finite window, therefore lies in
\[
 [\eta_{\rm act},1-\eta_{\rm act}],\qquad
 \eta_{\rm act}=97/2475.
\]
It follows that every actual local diagonal Fisher information obeys
\[
 d_m(a)\le D_{\max}:=
 \frac{1}{\eta_{\rm act}(1-\eta_{\rm act})}
 =\frac{2475^2}{97\cdot2378}.
\]
Thus the asymptotic scalar right-hand side of the local-score allocation, even with arbitrarily large windows or the exact full-volume diagonal Fisher information, cannot be smaller than
\[
 U_{\rm diag,floor}
 :=\frac32\left(\frac{I_3}{s}-\frac{D_{\max}}{80000}\right)
 >0.000469
 > C_*.
\]
This is a lower bound on the **best numerical bound obtainable by this particular allocation**, not a lower bound on \(\mathcal C_n/n\). It rules out closing the chord by improving only \(d_m\) while retaining the present \(\kappa=3/2\), the worst-case likelihood transport, and the same square allocation.

Retaining the favorable leakage term does not remove this asymptotic obstruction. Indeed,
\[
 \operatorname{tr}(Q_n-Q_n^2)
 =\sum_{i\in[1,n],\,j\notin[1,n]}|Q(i,j)|^2
 \le\frac{2}{\pi^2}
 \left(\sum_{d=1}^{n-1}\frac1d
       +n\sum_{d\ge n}\frac1{d^2}\right)=O(\log n).
\]
The uniform bound \(\|B_b\|\le40\) gives
\(\operatorname{tr}(B_b(Q_n-Q_n^2)B_b)
\le1600\operatorname{tr}(Q_n-Q_n^2)\), uniformly in the configuration and actual parameter. Therefore \(\Lambda_n\to0\). This argument proves a value-level boundary estimate only; it is not a differentiated entropy asymptotic.

A successful continuation of this route must improve the joint pair comparison or transport, for example by bounding the signed compensated terms **together**, rather than merely enumerating a larger Fisher window. The direct local-pair criterion in the body is not subject to this diagonal-only obstruction, but its explicit localization errors remain too large for a claimed practical certificate.

### F.4. Exact numerical evaluation and the unchanged tail obligation

Put \(\ell=\log(5/4)\). With \(a_0=1/50\), \(b=1/40\), define
\[
 I_1=\frac{(1+a_0)(b-a_0)-(b^2-a_0^2)/2-a_0\ell}{39},
\]
\[
 I_3=\frac{\frac{a_0}{2}(b^{-2}-a_0^{-2})
 -(1+3a_0)(b^{-1}-a_0^{-1})-3(1+a_0)\ell
 +(3+a_0)(b-a_0)-(b^2-a_0^2)/2}{39^3}.
\]
Then \(U_0=\kappa(I_3/s-4I_1)\) and
\(U_3=\kappa(I_3/s-d_*/80000)\).
The independent rational verifier encloses \(\pi\) by Machin's formula with alternating arctangent remainders, and encloses \(\ell\) by the positive atanh series at \(1/9\). In particular it checks the rational brackets
\[
 3.14159265358979323846<\pi<3.14159265358979323847,
\]
\[
 0.223143551314209755766<\ell<0.223143551314209755767.
\]
Every arithmetic acceptance test in that program is an exact rational comparison. Outward rational-grid rounding is used internally to prevent denominator growth; it does not introduce floating-point acceptance tests.

At a finite stopping volume \(M\), the only asserted entropy-rate lower bound is still the reviewed **full**-chord interface
\[
 \operatorname{Gap}h\ge\gamma_{16}+(1-16/M)B_{16}
 -\bigl[\min\{U_0,U_3+\beta_3/M\}-c_{16}\bigr]
 -T_{\rm QWE}(M).
\]
The full \(T_{\rm QWE}(M)\) has not been replaced by a determinant tail or assumed numerically small. Direct passage along all volumes using (F.8) and accepted KL length convexity gives only the negative lower bound \(C_*-U_3\). It supplies no positive \(\delta\).

**Strength of the result.** The benchmark chord remains **INCOMPLETE**. The theorem for every chord on \([0.02,0.03]\) remains **INCOMPLETE**. The all-\(\rho\), all-\(c\), all-legal-\(a\) objective remains **INCOMPLETE**. In particular, the fact that the three-site Fisher input holds throughout the actual chord does not turn the midpoint-specific acceleration theorem into a theorem for every reference point in the interval.

<!-- S67_LOCAL_FISHER_SUPPLEMENT_END -->


**Status of the entropy-rate assignment: INCOMPLETE.**  
**Status of the inequalities proved below: PROVED.**  
**Status of the proposed factor-one conditional-pair comparison: DISPROVED, including an actual-law averaged counterexample.**

This manuscript concerns full binary configuration entropy, with natural logarithms. It does not identify that entropy with count entropy, fermionic/trace entropy, or a cyclic determinant correction. It does not claim that the benchmark chord, the whole benchmark interval, or the all-parameter objective has been closed.

## 1. Result in brief

For the frozen benchmark

\[
 \rho=\tfrac12,\qquad c=\tfrac{19}{20},\qquad
 a_0=\tfrac1{50},\quad a_1=\tfrac3{100},\quad
 b=\tfrac1{40},\quad\lambda=\tfrac12,
\]

I prove an explicit bound, uniform in every finite volume,

\[
 \frac{\mathcal C_n}{n}\le U_{\rm S67}<0.000887.                 \tag{1.1}
\]

The exact expression for the upper bound is

\[
 U_{\rm S67}=\frac32\int_{1/50}^{1/40}(x-1/50)
 \left\{\frac1s\left(\frac{1-x}{39x}\right)^3
                 -4\frac{1-x}{39x}\right\}\,dx,
 \qquad s=\frac{39}{1600}.                                  \tag{1.2}
\]

The interval-arithmetic output accompanying this manuscript evaluates (1.2); it is approximately \(8.86\times10^{-4}\). This is an **upper bound**, not an estimate of the true limiting acceleration.

Consequently, with the accepted interval for \(\mathcal C_{16}/16\),

\[
 A_n\le U_{\rm S67}-\frac{\mathcal C_{16}}{16}
 <0.000740319519674116052447806952.                           \tag{1.3}
\]

The required positive-chord interface is much smaller:

\[
 \gamma_{16}+B_{16}
 \in[0.000245932000395801628841632655,
      0.000245932000395801628841632657].                       \tag{1.4}
\]

Equivalently, the reviewed interface would be paid by an eventual upper bound on \(\mathcal C_n/n\) strictly below

\[
 C_*:=\frac{\mathcal C_{16}}{16}+\gamma_{16}+B_{16}
 \in[0.000392612480721685576393825703,
      0.000392612480721685576393825706].                       \tag{1.5}
\]

**The bound in (1.2) exceeds (1.5). No positive \(\delta\) is established.**

There are two substantive tools here, rather than a renaming of \(A_n\).

1. A bounded-conditional-odds inequality allocates conditional log-odds cost to cross-Fisher squares. A Schur-complement likelihood-stability estimate then transports those squares under the **actual intermediate law**, not frozen reference weights. A signed-resolvent identity keeps the finite-compression leakage with its favorable sign and supplies (1.1).
2. A weighted Schur/Neumann argument gives a configuration-uniform locality bound for the signed inverse of the sine kernel. It converts the all-volume acceleration problem into explicitly specified **finite-window expectations plus explicit errors**, in (10.8). Its constants are enormous. The finite certificate needed to pay that criterion has not been supplied.

The second reduction is a weaker, verifiable sufficient input, not an equivalent restatement involving an unknown entropy rate. It also makes clear why merely asserting that a tail is small would be unacceptable.

## 2. Source packet, accepted inputs, and scope

The source branch is `research/sa-cycle11-pr128-20260918` in `cat5779/rl01`, source PR45. The following actual files were retrieved and read in the research run, rather than treating PR summaries as their contents:

- `research/CYCLE12_20260919/reviews/S64_CYCLE11_REVIEW.md`, the separately reviewed PR46 scope;
- `research/CYCLE12_20260919/S64/S64_CYCLE11_RESULT.md`, including its closure interface;
- all five files in `research/CYCLE12_20260919/S64/S64_checks/`: `README.md`, `verify_s64.py`, `check_results.txt`, `main_chord_020_030_n15_16.json`, and `raw_window_counterexamples_n4_n8.json`;
- the CYCLE11, CYCLE12, and CYCLE13 `SOURCE_STATUS.md` files specified in the assignment;
- `prompts/CYCLE13/S67.md`;
- additionally, `research/CYCLE08_20260918/QWE02/QWE02_TRUE_ENTROPY_DYADIC_TAIL.md` for the full-tail interface.

An initial browser request to the raw review encountered an HTTP rate-limit response; subsequent direct raw-file retrieval succeeded. The supporting source-retrieval record records the requests. This work does **not** claim to have independently rerun the accepted exhaustive n=15/16 certificate program. Its code and certificate files were read; their reviewed intervals are accepted inputs. New small-model counterexamples and the new bound constants have separate verification programs.

The accepted numerical inputs are

\[
\begin{aligned}
 B_{16}&\in[.000104188037840358653653185471,
             .000104188037840358653653185472],\\
 \gamma_{16}&\in[.000141743962555442975188447184,
                  .000141743962555442975188447185],\\
 \mathcal C_{16}/16&\in[.000146680480325883947552193048,
                         .000146680480325883947552193049].
\end{aligned}                                                \tag{2.1}
\]

Conditional KL supermodularity and KL convexity in **length** are accepted from PR46. In particular,

\[
 \mathcal D_M/M\ge\mathcal D_{16}/16+(1-16/M)B_{16},\quad M\ge16.
                                                               \tag{2.2}
\]

Nothing below reproves (2.2), adds the determinant budget to it, or uses the author-only S63 claim. The accepted universal reference remains \(c\le37/40\); it is not upgraded by the present non-closing estimate.

For a finite stopping volume the admissible interface remains

\[
 \operatorname{Gap}h\ge\gamma_{16}+(1-16/M)B_{16}
                         -A_M-T_{\rm QWE}(M).                  \tag{2.3}
\]

Here \(T_{\rm QWE}\) is the reviewed **full entropy-chord** far-tail, not merely a determinant tail. This manuscript never sets it to zero or assumes its large constant is harmless at a practical volume. The direct uniform bound and the locality reduction below concern \(\mathcal C_n\) itself, so their proofs do not require evaluating (2.3).

## 3. Model, notation, and the finite-volume diagonal response

Let

\[
 Q_n(i,j)=\begin{cases}\rho&i=j,\\
 \sin(\pi\rho(i-j))/(\pi(i-j))&i\ne j,
 \end{cases}\qquad K_{a,n}=aI+cQ_n.
\]

Throughout the benchmark, \(0<a<a+c<1\). Every configuration has positive probability. The finite compression satisfies

\[
 0\le Q_n\le I,\qquad E_n:=Q_n-Q_n^2\ge0;                    \tag{3.1}
\]

it is not replaced by a projection.

For a configuration \(x\in\{0,1\}^n\), let

\[
 D_x=\operatorname{diag}(1-x_i),\quad S_x=I-2D_x,
 \quad B_a(x)=(K_{a,n}-D_x)^{-1}.
\]

The configuration determinant is

\[
 p_a(x)=\det(S_x)\det(K_{a,n}-D_x)>0.                        \tag{3.2}
\]

More generally, allow separate local diagonal parameters. The determinant is multiaffine in them. Differentiating (3.2) at an interior kernel gives

\[
 \partial_i\log p=B_{ii},\quad
 \partial_i\partial_j\log p=-|B_{ij}|^2,\quad
 \frac{d^2p_a}{da^2}/p_a=(\operatorname{tr}B_a)^2
                                      -\operatorname{tr}(B_a^2).
                                                               \tag{3.3}
\]

The last display retains the square term. It is not permissible to discard it in an entropy differentiation.

Fix a reference \(b\), and condition on all sites except \(i,j\). The reference conditional DPP kernel has the form

\[
 L=\begin{pmatrix}u&z\\\bar z&v\end{pmatrix},\qquad t=|z|^2.
\]

Write its four probabilities as

\[
 A=uv-t,\quad B=u(1-v)+t,\quad C=(1-u)v+t,
 \quad D=(1-u)(1-v)-t.                                     \tag{3.4}
\]

In this section the letters \(A,B,C,D\) in (3.4) are scalar probabilities; the signed inverse is always written with indices or an argument when confusion is possible. Define

\[
 J=\log\frac{BC}{AD}\ge0,
 \qquad W=t\left(\frac1A+\frac1B+\frac1C+\frac1D\right).       \tag{3.5}
\]

Let \(J^b_{ij}(\xi)\) denote (3.5) for reference exterior configuration \(\xi\). For

\[
 f_n(a)=\mathbb E_{P_{a,n}}\log p_{b,n},
\]

multiaffinity and summation over the pair give the exact identity

\[
 f_n''(a)=-2\sum_{i<j}
             \mathbb E_{P_{a,[n]\setminus\{i,j\}}}J^b_{ij}.   \tag{3.6}
\]

**Proof.** The exterior marginal is independent of the two local diagonal parameters. Their mixed derivative of the four pair probabilities is \((1,-1,-1,1)\). Therefore the mixed derivative of the expectation of the fixed function \(\log p_b\) is \(\log(AD/BC)=-J\). Pure local second derivatives vanish. Summing ordered distinct pairs proves (3.6). The exterior expectation in (3.6) is at \(a\), not at \(b\). ∎

For a general chord define the nonnegative Green kernel

\[
 G(a)=\begin{cases}(1-\lambda)(a-a_0),&a_0\le a\le b,\\
                   \lambda(a_1-a),&b\le a\le a_1.
       \end{cases}
\]

Integration by parts twice gives

\[
 \mathcal C_n=2\int_{a_0}^{a_1}G(a)
       \sum_{i<j}\mathbb E_{P_{a,-ij}}J^b_{ij}\,da.           \tag{3.7}
\]

This is a finite-chord identity. No endpoint/volume limit interchange or endpoint perturbation expansion is used.

## 4. A bounded-odds binary inequality

### Theorem 4.1 — a reusable factor-three-halves comparison

Let \((A,B,C,D)\) be a strictly positive binary-pair law, ordered as in (3.4), with negative covariance, so \(t=BC-AD\ge0\). Suppose every one-bit conditional odds ratio lies between \(1/20\) and \(20\). Then

\[
                       J\le\frac32 W.                      \tag{4.1}
\]

This is an inequality for binary tables; it does not assume a determinantal model.

**Proof.** The case \(t=0\) is immediate. Put

\[
 r=BC/(AD)>1,\qquad q=A+D.
\]

Since the four probabilities sum to one,

\[
 W=(r-1)\{q+(1-q)/r\}.                                     \tag{4.2}
\]

More generally let the odds bound be \(M\). Write

\[
 A=\sqrt{AD}\,e^u,\quad D=\sqrt{AD}\,e^{-u},\quad
 B=\sqrt{rAD}\,e^v,\quad C=\sqrt{rAD}\,e^{-v}.
\]

The four adjacent log ratios imply

\[
 |u|+|v|\le\log M-\tfrac12\log r,
 \qquad 1\le r\le M^2.
\]

Consequently

\[
 q\ge\frac{1}{1+\sqrt r\cosh(\log M-\tfrac12\log r)}
      =\frac{2M}{M^2+2M+r}.                                \tag{4.3}
\]

For completeness, the minimization in (4.3) follows from
\(\cosh(T-x)/\cosh x=\cosh T-\sinh T\tanh x\le\cosh T\).

Use \(M=20\). Equations (4.2)–(4.3) reduce (4.1) to

\[
 \phi(r):=\frac32\frac{(r-1)(41r+400)}{r(r+440)}-\log r\ge0,
 \qquad 1\le r\le400.                                      \tag{4.4}
\]

The derivative has the sign of

\[
 P(r)=-2r^3+51283r^2-384800r+528000.                         \tag{4.5}
\]

On \([1,400]\), \(P'\) is strictly increasing because
\(P''=102566-12r>0\). Exact rational evaluations show

\[
 P(1)>0,\quad P(2)<0,\quad P(5.69)<0,\quad P(5.70)>0,
 \quad P(400)>0.
\]

Thus \(\phi\) has one interior maximum and one interior minimum; the latter is in \((5.69,5.70)\). The rational function

\[
 w(r)=(r-1)(41r+400)/[r(r+440)]
\]

is increasing, since its derivative has numerator
\(17681r^2+800r+176000>0\). At the interior minimum,

\[
 \phi(r)\ge\tfrac32w(5.69)-\log(5.70)
            >\tfrac32w(5.69)-\tfrac74>0.                   \tag{4.6}
\]

The last inequality is rational. To justify the preceding strict inequality without a floating-point logarithm, the first seven nonnegative terms of the exponential series give
\(e^{7/4}>\sum_{k=0}^6(7/4)^k/k!>57/10\).
Finally \(\phi(1)=0\). This proves (4.4) and the theorem. ∎

### 4.2 Why the coefficient and hypotheses matter

The coefficient one is false in the actual sine model. The supporting interval certificates give both a four-site conditional counterexample and a six-site counterexample after averaging over the actual reference exterior law; see Section 12.

The conditional-odds hypothesis cannot simply be deleted from Theorem 4.1. For example,

\[
 (A,B,C,D)=\frac1{1021}(10,1,1000,10)
\]

is the law of the positive-contraction DPP kernel

\[
 K=\frac1{1021}\begin{pmatrix}11&30\\30&1010\end{pmatrix}.
\]

Here \(J=\log10>2\), whereas
\(W=10809/10210\), so \((3/2)W<2\). Its largest conditional odds is 100, not 20. This is a generic two-site DPP counterexample outside the theorem's hypotheses; it is not presented as a sine-kernel counterexample.

## 5. A sharper conditional-odds bound for the finite sine compression

### Lemma 5.1 — compression and Schur-complement squeeze

For a positive contraction \(K_n\), put \(L_n=K_n(I-K_n)^{-1}\). For the compression of the infinite two-level operator \(K_\infty=aI+cQ\), operator convexity of inversion gives

\[
 L_n\le (K_\infty(I-K_\infty)^{-1})_{[n]},\qquad
 L_n^{-1}\le (K_\infty^{-1}-I)_{[n]}.                       \tag{5.1}
\]

The respective diagonal bounds are

\[
 \ell_+=(1-\rho)\frac a{1-a}+\rho\frac{a+c}{1-a-c},\qquad
 \ell_-=(1-\rho)\frac{1-a}{a}+\rho\frac{1-a-c}{a+c}.          \tag{5.2}
\]

Every fully conditioned one-site odds \(\omega\) satisfies

\[
                        1/\ell_-\le\omega\le\ell_+.        \tag{5.3}
\]

**Proof.** The inequality \((PAP)^{-1}\le PA^{-1}P\) on the compressed subspace follows from the Schur-complement variational formula for a positive operator. Apply it to \(A=I-K_\infty\) and \(A=K_\infty\), then subtract the identity, to obtain (5.1). Since \(Q\) is an infinite projection, functions of \(K_\infty\) have the two spectral values used in (5.2); their diagonals use \(Q(i,i)=\rho\).

For exterior occupied set \(S\), the conditional odds at site \(i\) is the Schur complement
\(L_{ii}-L_{iS}L_{SS}^{-1}L_{Si}\). It is at most \(L_{ii}\). It is at least the Schur complement over all other sites, namely \(1/(L^{-1})_{ii}\). Equations (5.1)–(5.2) prove (5.3). All arguments are finite-compression inequalities, not an assertion that \(Q_n^2=Q_n\). ∎

At the benchmark reference,

\[
 \ell_+=\ell_-=M=\frac{761}{39}<20,
 \qquad \eta:=\frac1{1+M}=\frac{39}{800}.                   \tag{5.4}
\]

Thus **every configuration**, including exceptional and very unlikely ones, has reference one-site conditional probability in \([\eta,1-\eta]\). Every conditional pair meets Theorem 4.1.

The model-specific improvement from the generic spectral edge \(1/40\) to the conditional edge \(39/800\) is important. A general kernel merely satisfying \((1/40)I\le K\le(39/40)I\) need not have this stronger conditional bound.

## 6. Actual-law transport without freezing weights

### Lemma 6.1 — Schur stability and configuration likelihood stability

Suppose two positive L-ensemble matrices satisfy

\[
 R^{-1}L\le\widetilde L\le RL,\qquad R\ge1.                 \tag{6.1}
\]

The same inequalities hold for their conditional L matrices after the same occupied/absent observations. For a conditional law on \(k\) remaining sites, every configuration probability obeys

\[
 R^{-k}p_L(x)\le p_{\widetilde L}(x)\le R^k p_L(x).          \tag{6.2}
\]

**Proof.** Excluding absent sites takes a principal submatrix. Conditioning occupied sites takes a Schur complement. Both operations preserve Loewner order and positive scalar homogeneity, by the variational formula
\(v^*\operatorname{Schur}(L)v=\inf_w(v,w)^*L(v,w)\).

To prove (6.2), join the two conditional matrices by

\[
 L(t)=L^{1/2}\exp(tH)L^{1/2},\quad
 H=\log(L^{-1/2}\widetilde L L^{-1/2}),\quad\|H\|\le\log R.
\]

The whitened derivative has operator norm at most \(\log R\). For a configuration with occupied set \(S\),

\[
 \frac d{dt}\log p_{L(t)}(S)
 =\operatorname{tr}\{[P_S-K(t)]E(t)\},
\]

where \(P_S\) is the orthogonal projection onto the columns of
\(L(t)^{1/2}\) indexed by \(S\),
\(K(t)=L(t)^{1/2}(I+L(t))^{-1}L(t)^{1/2}\), and
\(E(t)=L(t)^{-1/2}L'(t)L(t)^{-1/2}\).
Both \(P_S\) and \(K(t)\) lie between zero and the identity. Hence
\(\|P_S-K(t)\|_1\le k\), and the absolute derivative is at most
\(k\log R\). Integrate from zero to one. ∎

For the benchmark, the commuting spectral functions of \(Q_n\) imply

\[
 R(a)^{-1}L_b\le L_a\le R(a)L_b,
\]

where

\[
 R(a)=\begin{cases}
 (1-a)/(39a),& a\le b,\\
 (a+c)/[39(1-a-c)],& a\ge b.
 \end{cases}                                               \tag{6.3}
\]

One way to verify (6.3) is to integrate the logarithmic derivative
\(1/[x(1-x)]\) of the spectral odds. On the left half of the chord its maximum is at the lower spectral endpoint; on the right it is at the upper endpoint. Thus

\[
                    1\le R(a)\le49/39.                     \tag{6.4}
\]

For any fixed pair exterior, let \(q_a,q_b\) be the **actual** and reference conditional four-cell laws. Lemma 6.1 gives

\[
                       q_a(x_i,x_j)\ge R(a)^{-2}q_b(x_i,x_j).
                                                               \tag{6.5}
\]

This local comparison is independent of volume. It is not a global likelihood-ratio comparison with an exponentially growing factor in \(n\).

## 7. Signed-resolvent square allocation, including leakage

At the reference, set \(s=b(1-b)=39/1600\), \(B=B_b(x)\). The finite compression obeys

\[
 K_b^2-K_b=-sI-c^2E_n.
\]

Substitute \(K_b=B^{-1}+D_x\), multiply on both sides by \(B\), and simplify. The result is the exact matrix identity

\[
 sB^2+c^2BE_nB=\tfrac12(S_xB+BS_x)-I.                       \tag{7.1}
\]

In particular,

\[
 s\sum_j|B_{ij}|^2+c^2(BE_nB)_{ii}=S_{ii}B_{ii}-1.          \tag{7.2}
\]

The leakage term is nonnegative and has not been suppressed by treating the compression as a projection.

Condition on all sites except \(i\). Let \(r\) and \(q\) be the reference and actual conditional probabilities at site \(i\). Then

\[
 B_{ii}=\begin{cases}1/r&x_i=1,\\-1/(1-r)&x_i=0.
 \end{cases}
\]

By Lemma 6.1, the corresponding one-site odds differ by at most \(R=R(a)\). Both probability ratios are in \([1/R,R]\), and one of them is at most one. Therefore

\[
 \mathbb E_a[S_{ii}B_{ii}\mid X_{-i}]
       =q/r+(1-q)/(1-r)\le1+R,                             \tag{7.3}
\]

and

\[
 \mathbb E_a[B_{ii}^2\mid X_{-i}]
 \ge R^{-1}\{1/r+1/(1-r)\}\ge4/R.                          \tag{7.4}
\]

Taking expectations in (7.1) and subtracting the diagonal squares gives

\[
 2\sum_{i<j}\mathbb E_a|B_{ij}|^2
 \le n(R/s-4/R)-\frac{c^2}{s}\mathbb E_a\operatorname{tr}(BE_nB).
                                                               \tag{7.5}
\]

For a reference conditional pair, direct inversion of its four signed two-by-two matrices shows

\[
 |B_{ij}(x)|^2=t/q_b(x_i,x_j)^2,
 \qquad W^b_{ij}=\sum_{x_i,x_j}q_b(x_i,x_j)|B_{ij}(x)|^2.
\]

Use (6.5), average over the **actual** exterior law, and apply Theorem 4.1. With \(\kappa=3/2\),

\[
 \sum_{i<j}\mathbb E_{a,-ij}J^b_{ij}
 \le\kappa R^2\sum_{i<j}\mathbb E_a|B_{ij}|^2.              \tag{7.6}
\]

Combining (3.7), (7.5), and (7.6) proves the sharper finite-volume inequality

\[
\begin{split}
 \frac{\mathcal C_n}{n}\le{}&
 \kappa\int_{a_0}^{a_1}G(a)\{R(a)^3/s-4R(a)\}\,da\\
 &-\frac{\kappa c^2}{sn}\int_{a_0}^{a_1}
 G(a)R(a)^2\mathbb E_a\operatorname{tr}(B_bE_nB_b)\,da.
\end{split}                                                  \tag{7.7}
\]

Dropping only the displayed **favorable** term yields (1.1)–(1.2). The actual-law probabilities have been retained throughout; (6.5), (7.3), and (7.4) are the explicit price of changing their weights.

### 7.1 Evaluation and what it does not prove

For direct reproduction, antiderivatives for (1.2) are

\[
\begin{aligned}
 F_1(x)&=\{(1+a_0)x-x^2/2-a_0\log x\}/39,\\
 F_3(x)&=\{a_0/(2x^2)-(1+3a_0)/x
             -3(1+a_0)\log x+(3+a_0)x-x^2/2\}/39^3.
\end{aligned}
\]

Then

\[
 U_{\rm S67}=\frac32\{[F_3(b)-F_3(a_0)]/s
                              -4[F_1(b)-F_1(a_0)]\}.        \tag{7.8}
\]

The new verification program checks the rational parts exactly and evaluates (7.8) using Arb balls at several precisions. It also checks that the upper bound exceeds the required cap (1.5). Even replacing \(\kappa=3/2\) by a hypothetical \(\kappa=1\), without improving the rest of this allocation, would still not pay the reviewed interface. Thus improving that one coefficient is not by itself a closure plan.

Combining the accepted length bound with (7.8) gives a rigorous but **negative** lower bound

\[
 \operatorname{Gap}h\ge C_*-U_{\rm S67},                    \tag{7.9}
\]

with outward endpoints chosen from (1.5). This follows directly by taking the limit of the finite entropy chords and using the uniform bound; no derivative of an entropy-value error is taken. A negative lower bound is not a proof of concavity.

## 8. A compensated identity that retains favorable pair contributions

The factor-three-halves inequality is deliberately coarse. The following exact refinement explains one available form of compensation.

Keep \(u,v\) fixed in (3.4), replace \(t\) by \(\tau\in[0,t]\), and put

\[
 S(\tau)=1/A(\tau)+1/B(\tau)+1/C(\tau)+1/D(\tau),
 \quad V=\frac{t}{u(1-u)v(1-v)}.
\]

Then

\[
 J=\int_0^tS(\tau)\,d\tau
   =\frac12(W+V)-\mathcal R,
\quad
 \mathcal R=\frac12\int_0^t\tau(t-\tau)S''(\tau)\,d\tau.      \tag{8.1}
\]

Here

\[
 S''(\tau)=2\sum_{x_i,x_j}q_\tau(x_i,x_j)^{-3}\ge512,
 \qquad \mathcal R\ge\frac{128}{3}t^3.                     \tag{8.2}
\]

**Proof.** Differentiate \(J(\tau)=\log[B(\tau)C(\tau)/(A(\tau)D(\tau))]\). Its derivative is \(S\), and \(tS(0)=V\), \(tS(t)=W\). The trapezoidal integration identity with its exact second-derivative remainder gives (8.1). Jensen's inequality applied to the four positive probabilities summing to one yields \(\sum q^{-3}\ge256\), proving (8.2). ∎

Thus

\[
 J-W=\tfrac12(V-W)-\mathcal R.                              \tag{8.3}
\]

The unfavorable term and favorable remainder are kept together. Dropping \(V-W\) when it is positive is precisely the false factor-one step. No bound on the averaged \(V-W\) sufficient for the benchmark has been established here.

Two further exact revelation identities help delimit, but do not solve, that issue. For a DPP with separate local diagonal parameters, observing a new site with conditional success probability \(r\) adds

\[
 \mathbb E\frac{r_i r_j}{r(1-r)}\ge0                        \tag{8.4}
\]

to the cross-Fisher information for already observed sites \(i,j\). Indeed the new score is the old score plus
\((X_k-r)r_i/[r(1-r)]\); conditional orthogonality gives (8.4). The conditional-kernel formula gives
\(r_i=|[(K_T-D_T)^{-1}K_{Tk}]_i|^2\ge0\).

Also, revealing a site with conditional diagonal \(r\), and writing \(h=K_{ik}K_{kj}\), gives

\[
 r|z-h/r|^2+(1-r)|z+h/(1-r)|^2
       =|z|^2+|h|^2/[r(1-r)].                              \tag{8.5}
\]

Neither (8.4) nor (8.5) implies monotonicity of the compensated quantity \(W-\mathbb E J\). The actual-law averaged counterexample in Section 12 blocks that inference. These are score/covariance revelation identities, not a second proof of the accepted KL length theorem.

### 8.1 A common-configuration signed representation

There is also an exact representation in a single full reference signed inverse, which avoids giving different pair terms unrelated conditioning conventions. For a full configuration let

\[
 T_i=|B_b(x)_{ii}|-1>0,\qquad
 X_{ij}=\frac{|B_b(x)_{ij}|^2}{T_iT_j},\qquad
 \sigma_i=2x_i-1.
\]

Then, for every pair,

\[
 J^b_{ij}(x_{-ij})
   =-\sigma_i\sigma_j\log(1-\sigma_i\sigma_jX_{ij}).        \tag{8.6}
\]

When the two bits agree, \(0\le X_{ij}<1\). When they disagree, \(X_{ij}\ge0\) can exceed one; replacing the latter logarithm by the former would be an error.

To prove (8.6), use the four-cell table (3.4). For a 11 or 00 configuration, \(X_{ij}=t/(BC)=1-e^{-J}\). For a 10 or 01 configuration, \(X_{ij}=t/(AD)=e^J-1\). These equalities follow either by direct two-by-two inversion or by the rank-two determinant update. In particular \(T_i=p_b(x^i)/p_b(x)\), and

\[
 \frac{p_b(x^{ij})}{p_b(x)}
       =T_iT_j-\sigma_i\sigma_j|B_b(x)_{ij}|^2>0.
\]

The elementary integral remainder for \(\log(1+x)\) yields the signed rational upper bound

\[
 J^b_{ij}(x_{-ij})\le X_{ij}
       +\frac{\sigma_i\sigma_j X_{ij}^2}
                    {2(1-\sigma_i\sigma_jX_{ij})}.          \tag{8.7}
\]

Indeed, for agreeing bits integrate \(t/(1-t)\le t/(1-X_{ij})\); for disagreeing bits integrate \(t/(1+t)\ge t/(1+X_{ij})\). Thus the second term in (8.7) is favorable for disagreeing bits and unfavorable for agreeing bits. Averaging (8.6) or (8.7) uses the actual full law \(P_a\), because the left side is independent of the pair bits. No sufficient all-volume bound on the signed sum in (8.7) is asserted here. The representation is supplied as a concrete compensation interface alongside, not instead of, the proved uniform bound.

## 9. A configuration-uniform locality lemma for the signed inverse

The following tool applies beyond DPP laws. It uses a gapped self-adjoint matrix with off-diagonal decay at the borderline inverse-distance rate and an arbitrary diagonal perturbation that commutes with the weights.

### Lemma 9.1 — weighted inverse bound at the benchmark

For every finite sine compression, every configuration, every site \(i\), and
\(\theta=1/1000\),

\[
 \sum_j(1+|j-i|)^{2\theta}|B_b(x)_{ji}|^2\le6400.            \tag{9.1}
\]

In particular,

\[
 \sum_{|j-i|>L}|B_b(x)_{ji}|^2
           \le6400(1+L)^{-1/500}.                          \tag{9.2}
\]

**Proof, spectral gap.** Set \(\alpha=1/40\). Since
\(\alpha I\le K_b\le(1-\alpha)I\), the spectrum of
\(K_b-D_x\) avoids \((-\alpha,\alpha)\). To see this, order occupied sites first. For a candidate eigenvalue \(|z|<\alpha\), the occupied diagonal block of \(K_b-D_x-zI\) is positive definite, while the empty diagonal block is negative definite. Its Schur complement is negative definite as well. Thus the matrix is invertible. Consequently

\[
                         \|B_b\|\le40.                    \tag{9.3}
\]

**Proof, weighted commutator.** Fix the center \(i\), put \(w_j=1+|j-i|\), and let \(W_\theta=\operatorname{diag}(w_j^\theta)\). The diagonal \(D_x\) commutes with this weight. For \(j\ne k\),

\[
 |K_b(j,k)|\le\frac{c}{\pi|j-k|}.
\]

Apply the weighted Schur test to
\(W_\theta K_bW_\theta^{-1}-K_b\), with auxiliary Schur weight \(w_j^{-1/2}\). Its row sums are bounded by

\[
 \frac{2c}{\pi}\sum_{y\ge1,\,y\ne x}\frac1x
 \frac{|(y/x)^{-\theta}-1|(y/x)^{-1/2}}{|1-y/x|},
 \qquad x=w_j.
\]

There are at most two lattice sites at a given distance; also
\(|w_j-w_k|\le|j-k|\). If the two weights coincide, the numerator is zero. The column estimate is the same calculation with \(\theta\) replaced by \(-\theta\).

Split the scalar sum into \(y/x\le1/2\), \(1/2<y/x<1\), \(1<y/x\le2\), and \(y/x>2\). Using
\(|z^{\pm\theta}-1|\le\theta\max(1,z^{\pm\theta})|\log z|\), monotone right-Riemann sums, and

\[
 \int_0^1z^{-p}\log(1/z)\,dz=(1-p)^{-2},\quad
 \int_1^\infty z^{-1-p}\log z\,dz=p^{-2},
\]

gives, for both row and column sums at this \(\theta\),

\[
 C_\theta\le\frac{2c}{\pi}\theta
       \left\{\frac2{(1/2-\theta)^2}+2^{\theta+1/2}+9\right\}.
                                                               \tag{9.4}
\]

For clarity, the four contributions before the outer factor can be bounded by
\(2\theta/(1/2-\theta)^2\), \(\theta2^{\theta+1/2}\), \(\theta\), and \(8\theta\); for the transposed matrix the first and last bounds interchange and the smaller near-one exponent is harmless. The relevant tail integrands are decreasing on \([2,\infty)\) at \(\theta=1/1000\).

Using \(\pi>3\), \(c=19/20\), and \(2^{\theta+1/2}<2\),

\[
 C_\theta\le\frac{19}{30}\frac1{1000}
       \left\{\frac2{(499/1000)^2}+11\right\}
 =\frac{90041209}{7470030000}<\frac1{80}.                    \tag{9.5}
\]

Thus the weighted matrix differs from the unweighted one by less than half the spectral gap. The Neumann inverse estimate gives

\[
 \|W_\theta B_b W_\theta^{-1}\|
 \le(\alpha-C_\theta)^{-1}<80.
\]

Apply this operator to the centered basis vector, whose weight is one, to obtain (9.1). Equation (9.2) follows immediately. Every estimate is uniform in the exterior configuration and finite volume. ∎

## 10. An explicit finite-window sufficient input

The locality bound produces an actual finite-data criterion. Its poor constants are stated, not hidden.

Fix integers \(L\ge1\) and \(R\ge1\). Let

\[
 \Lambda=[-R,L+R]\cap\mathbb Z.
\]

For \(1\le d\le L\), define the finite, completely specified expectation

\[
 j_{d,L,R}(a)=
 \mathbb E_{P_{a,\Lambda\setminus\{0,d\}}}
 \left[J^{b,\Lambda}_{0d}(X_{\Lambda\setminus\{0,d\}})\right].
                                                               \tag{10.1}
\]

The conditional log odds in (10.1) are computed using the reference kernel compressed to \(\Lambda\); the expectation is the actual law at \(a\). This is a finite sum of determinantal probabilities times logarithms. Its integral over the fixed chord can, in principle, be enclosed using interval arithmetic. It is not an unknown infinite-volume law.

### 10.1 Error caused by discarding the exterior

Compare a full signed inverse with the inverse on a subwindow \(W\). For a column indexed by \(i\in W\), the block equation gives

\[
 B_{\mathrm{full},Wi}-B_{W,i}
       =-B_W K_{W,W^c}B_{\mathrm{full},W^ci}.                \tag{10.2}
\]

If the center is at distance at least \(R\) from the removed sites, (9.2), (9.3), and \(\|K_{W,W^c}\|\le1\) imply a column-norm error at most

\[
                    3200(1+R)^{-1/1000}.                   \tag{10.3}
\]

Set both pair bits to occupied when reading the two-by-two inverse block. That block is the inverse of the conditional pair kernel. Both conditional kernels are between \(\alpha I\) and \((1-\alpha)I\); this spectral squeeze follows by the same positive/negative Schur argument, or by sequential conditional-kernel updates. Hence the difference of their kernels has operator norm at most

\[
                    6400(1+R)^{-1/1000}.                   \tag{10.4}
\]

If this kernel error is \(e\), the four probability errors in (3.4) are at most \(4e,5e,5e,6e\). Each of the probabilities is at least \(\alpha^2\). The mean-value inequality for the logarithm therefore gives

\[
 |J^{b,\mathrm{full}}_{ij}-J^{b,W}_{ij}|
 \le\varepsilon_R:=
 \min\{2\log(761/39),\ 204800000(1+R)^{-1/1000}\}.           \tag{10.5}
\]

The first bound in the minimum follows from the one-site conditional odds squeeze. No random exceptional configuration is excluded.

### 10.2 Long-pair contribution

Use (7.6) pairwise and (9.2). For every \(n,a\),

\[
 \frac1n\sum_{i<j:\,|i-j|>L}\mathbb E_{a,-ij}J^b_{ij}
 \le\frac{\kappa}{2}R(a)^2\,6400(1+L)^{-1/500}.             \tag{10.6}
\]

For the pairs with distance at most \(L\), translate the window \(\Lambda\). All but a boundary set of \(O(L(L+R))\) pairs have an admissible translated window. For fixed \(L,R\), the normalized contribution of those boundary pairs vanishes as \(n\to\infty\), since \(J\le2\log(761/39)\). Marginal consistency of the DPP identifies the local expectations with (10.1). Thus

\[
 \limsup_{n\to\infty}\frac1n\sum_{i<j}\mathbb E_{a,-ij}J^b_{ij}
 \le\sum_{d=1}^{L}j_{d,L,R}(a)+L\varepsilon_R
       +\frac{\kappa}{2}R(a)^2\,6400(1+L)^{-1/500}.          \tag{10.7}
\]

The corresponding integrated inequality follows directly from the finite-volume estimates and their uniform boundary bound; no interchange of an uncontrolled limit and a derivative is involved. In particular,

\[
\boxed{
 \limsup_{n\to\infty}\frac{\mathcal C_n}{n}\le
 2\int_{a_0}^{a_1}G(a)
 \left\{\sum_{d=1}^{L}j_{d,L,R}(a)+L\varepsilon_R
       +\frac{\kappa}{2}R(a)^2\,6400(1+L)^{-1/500}\right\}\,da.
}                                                           \tag{10.8}
\]

### 10.3 What would constitute a certificate, and what is missing

A sufficient, finite, verifiable input is: exhibit integers \(L,R\), an interval enclosure of the finite integral in (10.8), and \(\delta>0\), such that the right side is at most the **lower endpoint** of (1.5) minus \(\delta\). This would prove the benchmark chord through the accepted length interface. It would not prove all chords on the interval.

No such enclosure is supplied here. The error constants make a practical application of (10.8) unattractive: the powers are only \(1/500\) and \(1/1000\), while the coefficients are 6400 and 204800000. In particular, substituting an ordinary finite window and announcing that these errors are negligible would be false. This is a mathematically valid reduction, not a numerical closure.

The useful unresolved research problem is now more specific: substantially improve the square-localization/allocation constants or prove an averaged compensation that preserves (8.3), sufficiently to obtain a finite certificate below (1.5). The present manuscript does not presume that either improvement holds.

## 11. Dependency ledger and classical provenance

| Item | Status and provenance | Used for |
|---|---|---|
| Full-law identity \(\operatorname{Gap}H_n=\mathcal D_n-\mathcal C_n\) | Accepted definition/identity; compatible with the new finite-chord derivation | Rate interface |
| PR46 KL length convexity and extrapolation | ACCEPTED INPUT, not reproved | (2.2), (7.9) |
| n=15/16 numerical intervals | ACCEPTED INPUT, original code read, not claimed rerun | (1.3)–(1.5) |
| Full QWE02 entropy-chord tail | ACCEPTED INPUT; not evaluated as small | (2.3) only |
| Multiaffine response and actual-law Green integral | PROVED here | (3.6)–(3.7) |
| Binary bounded-odds factor \(3/2\) | PROVED here, rational sign proof | (7.6) |
| Infinite-operator conditional-odds squeeze for finite compressions | PROVED here using classical inverse compression and Schur variational facts | (5.4) |
| Conditional likelihood stability in a Loewner/Thompson ball | PROVED here | Actual weights in (6.5)–(7.6) |
| Signed-resolvent identity with contraction leakage | PROVED here | Uniform acceleration bound |
| Compensated trapezoid formula | PROVED; classical trapezoid remainder applied to the pair table | Retains favorable/unfavorable terms |
| Cross-Fisher/covariance revelation identities | PROVED; classical conditional score orthogonality plus DPP update signs | Delimits possible compensation arguments |
| Weighted inverse localization and finite-window criterion | PROVED here; classical Schur test and Neumann inverse mechanism | (9.1), (10.8) |
| Factor-one conditional and averaged comparisons | DISPROVED by small actual-model interval certificates | Failure tests |
| Positive benchmark entropy-rate chord | INCOMPLETE | No positive \(\delta\) |

The constituent tools of matrix inversion, Schur complements, conditional Fisher information, and quadrature remainders are classical. The particular allocation and explicit constants are derived here for this assignment. **No claim of external novelty or priority is made.** Proving a useful statement in this manuscript and establishing its novelty in the literature are separate questions.

## 12. Adversarial checks and numerical evidence

### 12.1 Actual-model counterexamples

The files `certificates/pair_counterexamples.json` and `code/verify_counterexamples.py` contain the configurations, parameters, Arb intervals, and the exact program for two failed stronger statements:

\[
 J^b_{ij}(\xi)\le W^b_{ij}(\xi),                             \tag{12.1}
\]

and

\[
 \mathbb E_{P_{b,-ij}}J^b_{ij}\le
                  \mathbb E_{P_{b,-ij}}W^b_{ij}.            \tag{12.2}
\]

The first counterexample is a four-site sine law; the second is a six-site sine law at the benchmark reference. Their certificate records, including pair indices and exterior conventions, are reproduced in the appended computation record. These are full configuration-law computations, not eigenvalue/count surrogates. The averaged test sums over every exterior configuration with its actual probability.

The programs use exact rational model parameters and interval evaluation of \(\pi\), sine, determinants, inverses, and logarithms. Increasing precision is an internal consistency check; the mathematical certification is the strict sign of the resulting enclosing interval. No probabilistic sampling or decimal plot is used to establish these counterexamples.

### 12.2 Checks on the new bound

`code/verify_s67_bounds.py` checks:

- all rational signs used in the proof of Theorem 4.1, including its critical-point enclosure and exponential-series comparison;
- the exact conditional-odds constant, the odds-transport factor, and the weighted-commutator rational bound;
- outward evaluations of (7.8) and the accepted budget intervals at multiple Arb precisions;
- the strict **failure** of this bound to pay (1.5), including the observation that changing only \(3/2\) to one would still be insufficient.

The computation record distinguishes accepted inputs from newly checked constants. The n=15/16 source certificate is not relabeled as a new S67 exhaustive computation.

### 12.3 Parameter boundaries and failed extensions

The uniform proof in Sections 5–7 is stated for the benchmark reference and chord. At half filling and centered reference, its scalar odds step would remain applicable when
\((1+c^2)/(1-c^2)\le20\), or \(c\le\sqrt{19/21}\). That observation is **not** an entropy-concavity theorem on this larger c-range; the budget comparison still has to be paid.

For a different filling, the two quantities \(\ell_+,\ell_-\) in (5.2) generally differ. For a different reference, the simple symmetric quadratic identity (7.1) changes. At legal endpoints with zero spectral margin, the inverse/likelihood bounds used here cease to be uniform. The weighted locality constants also depend on a positive signed spectral gap. No assertion is made that the same numerical constants survive those changes.

The locality proof does not claim exponential decay. Its very small algebraic exponent is explicit. The proof does not discard finite boundary pairs; it bounds their count before passing to the limit. The use of the infinite projection in (5.1) is only for an operator compression inequality; all finite leakage in (7.1) remains present.

## 13. Handoff

**Benchmark chord \((.02,.03)\), \(\lambda=1/2\), \(\rho=1/2\), \(c=.95\): INCOMPLETE.** There is a proved all-volume upper bound on its actual-law acceleration, but it is above the reviewed budget. No positive entropy-rate chord is claimed.

**Every chord on \([.02,.03]\) at the benchmark \(\rho,c\): INCOMPLETE.** A proof for the single benchmark chord would not by itself establish this stronger statement; even that single-chord certificate is absent here.

**All \(\rho\), all \(c\), all legal \(a\): INCOMPLETE.** The accepted \(c\le37/40\) baseline remains the reference. No use is made of the unreviewed S63 claim or S68's separate endpoint expansion.

The next usable mathematical interface is (10.8), or a genuinely sharper version of (7.7) that controls the actual-law weights and the signed compensation in (8.3). The required numerical cap is (1.5). A new computation must exhibit its margin below that cap, or retain the full far-tail in (2.3) if it works only at a finite stopping volume.

## 14. Reproduction

From the delivered directory, with `python-flint` installed:

```sh
python code/verify_s67_bounds.py --precision 192 --output certificates/recheck_bounds_192.json
python code/verify_counterexamples.py
```

The first command is a lightweight verification of the new inequalities' constants and the non-closure comparison. The second verifies the supplied small actual-model counterexamples according to the program's included entry point. Neither command is a claim to re-run PR46's n=16 exhaustive program. The mathematical manuscript and its code are valid deliverables independently of whether a ZIP is used to transport them.

<!-- S67_FINAL_RATIONAL_AUDIT_BEGIN -->

## Final independent rational audit and strengthened-result ledger

The final local-score supplement strengthens the earlier uniform bound while leaving all entropy-rate objectives incomplete. The original S64 n15/n16 program was read, not independently rerun; its reviewed intervals remain accepted inputs. Later tool stdout was not consistently visible during the final writing continuation, so the execution record below is preserved directly from generated files rather than reconstructed from memory. The complete analytic derivations, explicit program, and actual run status are separate parts of this handoff.

| Claim | Status | Dependency and scope |
|---|---|---|
| Local-score projection | PROVED | Finite differentiation and conditional Jensen; classical information processing |
| Three-site Fisher minimum throughout the actual chord | PROVED | Exact half-filled sine marginal, all exterior weights, algebra in (F.7) |
| Improved finite-volume acceleration bound with boundary coefficient | PROVED | Binary 3/2 inequality, actual-law transport, signed-resolvent square identity, local-score projection |
| Diagonal-only refinement obstruction | PROVED | Actual conditional-odds ceiling and vanishing value-level compression leakage; not an entropy-rate counterexample |
| Positive benchmark entropy-rate chord | INCOMPLETE | The explicit improved upper bound still exceeds the reviewed cap |
| All chords in the benchmark interval; ultimate all-parameter objective | INCOMPLETE | No extension is asserted |

**Independent standard-library rational program status:** `NOT_VERIFIED_IN_THIS_RUN`.

**Execution limitation:** this finalizer did not establish a fresh successful rational-core execution. Do not treat the numerical display as independently verified by this run. The supplied proof and program remain available; inspect `certificates/rational_core.log`.

Execution diagnostic: `JSON status='PASS'; exit='0'; fresh=False`.

**Timing limitation:** usable start/end timestamps were not both available. No elapsed-duration claim is made.

<!-- S67_FINAL_RATIONAL_AUDIT_END -->
