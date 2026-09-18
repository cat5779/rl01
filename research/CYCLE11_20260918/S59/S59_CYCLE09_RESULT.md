# S59 Cycle 09 — actual-law conditional-table compensation tool

**Frozen benchmark:** half-density sine projection, \(c=19/20\),
\[
b=\frac{1-c^2}{4}=\frac{39}{1600},\qquad
m:=2b=\frac{39}{800},\qquad
R:=\frac{1-m}{m}=\frac{761}{39}.
\]

**Author status:** new, not independently reviewed.

## 1. Verdict by claim

| Claim | Status | Exact scope |
|---|---|---|
| \(\Gamma_{19/20}(0)>0\) | **INCOMPLETE** | The sign is not proved. |
| Weighted-reveal compensation identity, Theorem 1 below | **PROVED** | Actual infinite sine output law at the frozen midpoint; nonnegative Borel test functions; infinite spatial sum retained by Tonelli. |
| Bellman/secant interface, Corollary 2 | **PROVED** | Any tablewise secant majorant satisfying the stated assumptions gives the displayed actual-law expectation bound. |
| Four-sided posterior-box envelope \(r(p)\le 59/40\) | **PROVED** | Every actual two-point conditional table at \(c=19/20\); proof uses all four full-posterior bounds, not arbitrary normalized tables. |
| Quantitative actual-law bound \(\int r\,d\nu\le1.238281301637970\ldots\) | **PROVED** | Uses the new envelope, the reviewed exact \(\nu\)-mass, Jensen, and the reviewed sine linear-prediction bound on \(\mathbb ED\). |
| Local “cemetery Bellman” choice \(\Phi_*(q)=1/(q(1-q)-b)\) works on every channel-legal table | **DISPROVED** | Exact rational counterexample is a BSC image of a legal two-site DPP and obeys the same four posterior bounds. It is **not** claimed to occur under the infinite sine conditional law. |
| The local BSC/posterior-box relaxation permits \(r>1.47\) | **PROVED** | Same exact witness, with a rational lower certificate for \(\log 6\). |
| Finite cyclic values in the check output prove an infinite statement | **DISPROVED / NOT CLAIMED** | They are diagnostics only. S55’s reviewed transfer is not redone and supplies no sign or effective rate. |

The new normalized budget is
\[
b\Gamma_{19/20}(0)
=1-\int r\,d\nu
\ge -0.2382813016379701288\ldots .
\]
Thus the remaining unpaid amount needed for the desired sign is exactly
\[
0.2382813016379701288\ldots
\]
in the normalized \(b\Gamma\) budget.

---

## 2. Reviewed inputs and dependency boundary

The proof below takes the following reviewed facts as inputs and does not reprove their transfer:

1. For the full exterior posterior
   \(q=\Pr(Y_0=1\mid Y_{\mathbb Z\setminus\{0\}})\),
   \(D=q(1-q)\), there is a posterior vector \(v\) satisfying the projection Ward identity
   \[
   D=b(1+\|v\|_2^2).
   \tag{2.1}
   \]
2. Flipping exterior coordinate \(i\), with actual conditional flip odds \(o_i\), gives
   \[
   q(z^i)-q(z)=\frac{\sigma_i|v_i(z)|^2}{o_i(z)}.
   \tag{2.2}
   \]
3. The continuous posterior version obeys
   \[
   m\le q\le1-m,
   \qquad m=2b=\frac{39}{800}.
   \tag{2.3}
   \]
   By translation, the same bound holds for the full posterior at every site.
4. For the reviewed conditional tables,
   \[
   bJ=\int r\,d\nu,
   \qquad
   b\Gamma=1-\int r\,d\nu,
   \qquad
   \nu(\mathrm{all})=1-b\mathbb E\frac1D.
   \tag{2.4}
   \]
5. For the half-density sine law,
   \[
   \mathbb ED\le
   M:=\frac{c^2}{2\log((1+c^2)/(1-c^2))}
   =\frac{361}{800\log(761/39)}.
   \tag{2.5}
   \]

All required source files listed in the task were accessible. Their exact repository paths are recorded in Section 10.

---

## 3. Conditional-table coordinates

Fix \(i\ne0\) and condition on
\[
W_i:=Y_{\mathbb Z\setminus\{0,i\}}.
\]
Write
\[
s_i=\Pr(Y_i=1\mid W_i),
\]
\[
q_{i,0}=\Pr(Y_0=1\mid W_i,Y_i=0),
\qquad
q_{i,1}=\Pr(Y_0=1\mid W_i,Y_i=1),
\]
and
\[
a_i:=q_{i,0}-q_{i,1}\ge0.
\]
The four atoms are
\[
\begin{aligned}
p_{10}&=(1-s_i)q_{i,0},&
 p_{00}&=(1-s_i)(1-q_{i,0}),\\
p_{11}&=s_iq_{i,1},&
 p_{01}&=s_i(1-q_{i,1}).
\end{aligned}
\tag{3.1}
\]
Consequently
\[
\Delta_i=s_i(1-s_i)a_i.
\tag{3.2}
\]
Put
\[
h(q):=\frac1{q(1-q)}.
\]
A direct substitution into the reviewed definition of \(E_i\) gives
\[
\boxed{
E_i=a_i\{s_i h(q_{i,0})+(1-s_i)h(q_{i,1})\}.}
\tag{3.3}
\]
Also
\[
\boxed{
\ell_i
=\operatorname{logit}(q_{i,0})-
  \operatorname{logit}(q_{i,1})
=\int_{q_{i,1}}^{q_{i,0}}h(u)\,du.}
\tag{3.4}
\]
Thus \(\ell_i/a_i\) is a secant average of \(h\), while \(E_i/a_i\) is an actual-law, state-dependent endpoint quadrature.

---

## 4. New reusable tool: weighted-reveal compensation

### Theorem 1 — weighted-reveal identity (**PROVED**)

Let \(\phi:(0,1)\to[0,\infty]\) be Borel. Then, as an equality in \([0,\infty]\),
\[
\boxed{
\sum_{i\ne0}
\mathbb E\!
\left[
 a_i\{s_i\phi(q_{i,0})+(1-s_i)\phi(q_{i,1})\}
\right]
=
\mathbb E\!\left[
\phi(q)\left(\frac{D}{b}-1\right)
\right].}
\tag{4.1}
\]
If either side is finite, so is the other. A signed \(\phi\) is also allowed whenever the two sides are absolutely integrable.

#### Proof

Fix \(i\) and condition on \(W_i\). On the branch \(Y_i=0\), the full exterior posterior is \(q_{i,0}\), the probability of that branch is \(1-s_i\), and the actual flip odds are
\[
o_i=\frac{s_i}{1-s_i}.
\]
Since the DPP influence is negative, flipping \(Y_i:0\to1\) changes the root posterior by \(-a_i\). The reviewed flip formula (2.2) therefore gives
\[
|v_i|^2=o_i a_i=\frac{s_i}{1-s_i}a_i
\qquad(Y_i=0).
\tag{4.2}
\]
On the branch \(Y_i=1\), the flip odds are \((1-s_i)/s_i\), and similarly
\[
|v_i|^2=\frac{1-s_i}{s_i}a_i
\qquad(Y_i=1).
\tag{4.3}
\]
Average \(\phi(q)|v_i|^2\) over the two actual branches:
\[
\begin{aligned}
\mathbb E[\phi(q)|v_i|^2\mid W_i]
&=(1-s_i)\phi(q_{i,0})\frac{s_i}{1-s_i}a_i
  +s_i\phi(q_{i,1})\frac{1-s_i}{s_i}a_i\\
&=a_i\{s_i\phi(q_{i,0})+(1-s_i)\phi(q_{i,1})\}.
\end{aligned}
\tag{4.4}
\]
Because \(\phi\ge0\), Tonelli permits summation before expectation. The pointwise Ward identity (2.1) gives
\[
\sum_{i\ne0}|v_i|^2=\frac{D}{b}-1.
\tag{4.5}
\]
Summing (4.4) over \(i\ne0\) proves (4.1). ∎

### Two exact moments supplied by the tool

Taking \(\phi\equiv1\) gives the new jump-mass identity
\[
\boxed{
\sum_{i\ne0}\mathbb E a_i
=\frac{\mathbb ED}{b}-1.}
\tag{4.6}
\]
Taking \(\phi=h=1/D\), and using (3.3), gives
\[
\sum_{i\ne0}\mathbb E E_i
=\mathbb E\left(\frac1b-\frac1D\right),
\tag{4.7}
\]
which recovers the reviewed \(\nu\)-mass formula after multiplication by \(b\). The point of Theorem 1 is that (4.7) is only one member of an entire test-function family.

### Corollary 2 — Bellman/secant interface (**PROVED**)

Suppose a Borel function \(\Phi\ge0\) satisfies, for every actual conditional table with \(a_i>0\),
\[
\frac{\ell_i}{a_i}
\le s_i\Phi(q_{i,0})+(1-s_i)\Phi(q_{i,1}).
\tag{4.8}
\]
Then
\[
\boxed{
bJ(c)\le
\mathbb E[(D-b)\Phi(q)].}
\tag{4.9}
\]

Indeed, multiply (4.8) by \(a_i\), sum and apply (4.1):
\[
J(c)\le
\mathbb E\left[\Phi(q)\left(\frac{D}{b}-1\right)\right].
\]
Multiplying by \(b\) gives (4.9).

This is the promised reusable interface. Its inputs are a pointwise secant certificate and the actual posterior law; its output is a single paid actual-law expectation. It does not rename \(\Gamma\), and a proposed positive compensator must pay through the right-hand side of (4.9).

---

## 5. All four posterior bounds and the exact table domain

For the root site, both \(q_{i,0}\) and \(q_{i,1}\) are full posteriors after all other outputs have been revealed, hence lie in \([m,1-m]\). Reverse the roles of sites \(0\) and \(i\). The two quantities
\[
\Pr(Y_i=1\mid W_i,Y_0=0)
=\frac{p_{01}}{p_{00}+p_{01}},
\]
\[
\Pr(Y_i=1\mid W_i,Y_0=1)
=\frac{p_{11}}{p_{10}+p_{11}}
\]
are also full posteriors, so they too lie in \([m,1-m]\).

This four-sided box is stronger than merely requiring a normalized negatively associated table.

Let
\[
t=e^{\ell}=\frac{p_{10}p_{01}}{p_{00}p_{11}}\ge1,
\qquad
x=\frac{p_{10}}{p_{00}},
\qquad
y=\frac{p_{01}}{p_{00}}.
\tag{5.1}
\]
Then
\[
\frac{p_{11}}{p_{00}}=\frac{xy}{t}.
\tag{5.2}
\]
The four posterior odds are
\[
x,rac{x}{t},y,\frac{y}{t}.
\]
Since each lies in \([1/R,R]\),
\[
\boxed{
1\le t\le R^2,
\qquad
\frac{t}{R}\le x,y\le R.}
\tag{5.3}
\]
Moreover
\[
U=p_{00}+p_{11}
=\frac{1+xy/t}{1+x+y+xy/t}.
\tag{5.4}
\]

### Lemma 3 — minimum possible agreement mass (**PROVED**)

For fixed \(t\in[1,R^2]\), under (5.3),
\[
\boxed{
U\ge U_{\min}(t):=
\frac{2}{2+R+t/R}
=\frac{2R}{R^2+2R+t}.}
\tag{5.5}
\]
Equality occurs at \((x,y)=(R,t/R)\) or \((t/R,R)\).

#### Proof

Differentiate (5.4):
\[
\operatorname{sgn}\frac{\partial U}{\partial x}
=\operatorname{sgn}(y^2-t),
\qquad
\operatorname{sgn}\frac{\partial U}{\partial y}
=\operatorname{sgn}(x^2-t).
\tag{5.6}
\]
For fixed \(y<\sqrt t\), \(U\) decreases with \(x\), so its minimum on that horizontal segment is at \(x=R\). For fixed \(y>\sqrt t\), it increases with \(x\), so the minimum is at \(x=t/R\). On the edge \(x=R\), (5.6) shows that \(U\) increases with \(y\), because \(R^2\ge t\); hence the edge minimum is \(y=t/R\). On the edge \(x=t/R\), \(U\) decreases with \(y\), because \((t/R)^2\le t\); hence the edge minimum is \(y=R\). Substitution gives (5.5). ∎

---

## 6. Certified table envelope \(r\le59/40\)

The reviewed algebra gives
\[
E=(1-t^{-1})[1+(t-1)U].
\tag{6.1}
\]
For fixed \(t\ge1\), this is increasing in \(U\). Lemma 3 therefore yields
\[
E\ge A_R(t):=
\frac{(t-1)\{R^2+(2R+1)t\}}
{t(R^2+2R+t)}.
\tag{6.2}
\]
Thus
\[
r=\frac{\log t}{E}
\le\frac{\log t}{A_R(t)}.
\tag{6.3}
\]
It remains to prove the following one-dimensional statement.

### Lemma 4 — scalar certificate (**PROVED**)

For \(R=761/39\) and every \(1\le t\le R^2\),
\[
\boxed{
\log t\le\frac{59}{40}A_R(t).}
\tag{6.4}
\]

#### Exact calculus certificate

Set
\[
F(t)=\frac{59}{40}A_R(t)-\log t.
\]
Then \(F(1)=0\), and direct exact differentiation gives
\[
F'(t)=
\frac{P(t)}{40t^2(1521t+638479)^2},
\tag{6.5}
\]
where
\[
\begin{aligned}
P(t)={}&-92537640t^3+2169131175861t^2\\
&-16202277858802t+21815639220581.
\end{aligned}
\tag{6.6}
\]
The denominator in (6.5) is positive. The exact rational Sturm algorithm gives the following variation counts for \(P\):

| point | value | Sturm variations |
|---|---:|---:|
| \(1\) | \(1\) | 3 |
| \(a_1\) | \(110133/62500=1.762128\) | 3 |
| \(b_1\) | \(1762129/10^6=1.762129\) | 2 |
| \(a_2\) | \(5709301/10^6=5.709301\) | 2 |
| \(b_2\) | \(2854651/500000=5.709302\) | 1 |
| \(R^2\) | \(579121/1521\) | 1 |

Hence \(P\) has exactly one root in \((a_1,b_1)\), exactly one root in \((a_2,b_2)\), and no other root in \([1,R^2]\). Since \(P(1)>0\), \(F\) increases, then decreases, then increases. Its only possible minima on \([1,R^2]\) are \(t=1\) and the second critical point \(\tau_2\in(a_2,b_2)\).

To certify the latter minimum without floating-point logarithms, use
\[
z=\frac{x-1}{x+1},
\qquad
\log x=2\sum_{k=0}^{20}\frac{z^{2k+1}}{2k+1}+\mathcal R_{20},
\]
with
\[
0<\mathcal R_{20}
<\frac{2z^{43}}{43(1-z^2)}.
\tag{6.7}
\]
Here \(A_R\) is increasing, since
\[
A_R'(t)=\frac{R^4+2R^3t^2+2R^3+4R^2t^2+2R^2t+4Rt^2+t^2}{t^2(R^2+2R+t)^2}>0.
\tag{6.8a}
\]
Because \(A_R\) and \(\log\) are increasing,
\[
F(\tau_2)
\ge \frac{59}{40}A_R(a_2)-\log b_2.
\tag{6.8}
\]
Substituting the rational upper bound (6.7) for \(\log b_2\), exact rational arithmetic gives
\[
\frac{59}{40}A_R(a_2)-\log b_2
>\frac{709}{10^7}>0.
\tag{6.9}
\]
The accompanying standard-library checker prints the positive exact numerator and denominator of the difference in (6.9). Therefore both candidate minima are nonnegative, proving (6.4). ∎

### Theorem 5 — posterior-box envelope (**PROVED**)

Every actual conditional table at \(c=19/20\) satisfies
\[
\boxed{r(p)\le\frac{59}{40}.}
\tag{6.10}
\]
For \(\ell=0\), this follows by the continuous convention \(r=1\). For \(\ell>0\), combine (6.3) and Lemma 4. ∎

A numerical maximization of the certified one-dimensional envelope gives approximately
\[
\sup \frac{\log t}{A_R(t)}
=1.47493979095754\ldots,
\]
so \(59/40\) has a small but rigorously certified margin. This decimal is diagnostic; the proof is (6.5)–(6.9).

---

## 7. Quantitative insertion into the actual-law budget

By Theorem 5 and the reviewed measure identity,
\[
\int r\,d\nu
\le\frac{59}{40}\nu(\mathrm{all}).
\tag{7.1}
\]
By Jensen,
\[
\mathbb E\frac1D\ge\frac1{\mathbb ED}.
\]
Using (2.5),
\[
\nu(\mathrm{all})
=1-b\mathbb E\frac1D
\le1-\frac b{\mathbb ED}
\le1-\frac bM.
\tag{7.2}
\]
At the frozen constants,
\[
\frac bM
=\frac{39}{722}\log\frac{761}{39}.
\tag{7.3}
\]
Therefore
\[
\boxed{
\int r\,d\nu
\le B_{59}:=
\frac{59}{40}
\left(1-\frac{39}{722}\log\frac{761}{39}\right).}
\tag{7.4}
\]
Numerically,
\[
\boxed{
B_{59}=1.238281301637970128812527956869\ldots .}
\tag{7.5}
\]
Consequently
\[
\boxed{
b\Gamma_{19/20}(0)
\ge-0.238281301637970128812527956869\ldots,}
\tag{7.6}
\]
\[
\boxed{
\Gamma_{19/20}(0)
\ge-9.77564314412185143846268541002\ldots .}
\tag{7.7}
\]
This does not prove the desired sign. It is, however, a strict new estimate. The reviewed endpoint estimate at the same \(c\) gives the much larger upper allowance
\[
bJ\le
\frac{(1+c^2)^2}{2}\log\frac{1+c^2}{1-c^2}
=5.37690631490615748\ldots .
\tag{7.8}
\]
The new argument reduces that upper allowance to \(1.2382813016\ldots\), paying
\[
5.3769063149\ldots-1.2382813016\ldots
=4.1386250132\ldots
\]
of the previous crude unsigned budget.

---

## 8. Boundary attack: an exact failure of the local target Bellman function

A tempting use of Corollary 2 is
\[
\Phi_*(q)=\frac1{q(1-q)-b}.
\tag{8.1}
\]
If (4.8) held with this \(\Phi_*\), then
\[
(D-b)\Phi_*(q)=1
\]
and (4.9) would prove \(bJ\le1\), hence \(\Gamma\ge0\). The candidate is false even in a tightly constrained local relaxation.

Take \(t=6\), \(R=761/39\), and
\[
Z=2+R+\frac6R.
\]
Define the exact table
\[
(p_{00},p_{01},p_{10},p_{11})
=\frac1{647605}(29679,9126,579121,29679).
\tag{8.2}
\]
Its cross-ratio is exactly \(6\), so \(\ell=\log6\). Its relevant posteriors are
\[
q_0=\frac{761}{800},
\qquad
q_1=\frac{761}{995},
\qquad
s=\frac{7761}{129521}.
\tag{8.3}
\]
The two reverse posteriors are \(234/995\) and \(39/800\). Thus all four full-posterior coordinates lie in
\([39/800,761/800]\).

For this table, the right side of the proposed secant inequality, after multiplication by \(a=q_0-q_1\), is exactly
\[
a\{s\Phi_*(q_0)+(1-s)\Phi_*(q_1)\}
=\frac{19311189939680}{11811914073463}
=1.634890824600993\ldots .
\tag{8.4}
\]
But
\[
\log6=\log2+\log3>\frac23+1=\frac53,
\tag{8.5}
\]
because the first positive atanh term gives \(\log2>2/3\), and \(e<3\) gives \(\log3>1\). Exact subtraction gives
\[
\frac53-
\frac{19311189939680}{11811914073463}
=
\frac{1126000548275}{35435742220389}>0.
\tag{8.6}
\]
Hence (4.8) fails for \(\Phi_*\).

The witness is also an independent binary-symmetric-channel image, with crossover \(1/40\), of a legal two-site DPP. One exact latent table is
\[
\left(
\frac{4445961}{187028324},
\frac{2428961}{187028324},
\frac{175707441}{187028324},
\frac{4445961}{187028324}
\right).
\tag{8.7}
\]
Its covariance deficit is positive, and both \(H\) and \(I-H\) have nonnegative determinants for the associated \(2\times2\) kernel, so it is a valid two-site DPP law. Passing its two bits independently through the \(1/40\) BSC gives (8.2) by exact arithmetic.

This is **not** an infinite-sine counterexample. It proves a narrower and useful obstruction: the output channel, negative association, and all four posterior-box constraints do not by themselves validate the pointwise cemetery Bellman function.

For the same witness,
\[
E=\frac{944395}{777126},
\]
and the first six positive terms in the atanh series give
\[
\log6>2\sum_{k=0}^{5}\frac{(5/7)^{2k+1}}{2k+1}
=\frac{350059324760}{195755347557}.
\]
Moreover
\[
\frac{350059324760}{195755347557}
-\frac{147}{100}\frac{944395}{777126}
=\frac{267387402840979}{144882447833886840}>0.
\]
Therefore
\[
\frac{\log6}{E}>\frac{147}{100}.
\tag{8.8}
\]
Thus any universal pointwise coefficient on this local relaxation must exceed \(1.47\). A sign proof must therefore use actual distributional rarity or compensation, not merely shrink the universal table constant to near \(1\).

---

## 9. What the new tool does and what remains missing

### What is now paid

1. **Infinite spatial sum:** Theorem 1 keeps the full sum over \(i\ne0\). Nonnegativity and Tonelli pay the interchange.
2. **Actual measure:** Every expectation in (4.1) is under the correct full-exterior or pair-exterior actual law. No arbitrary table collection replaces it.
3. **Singular weight:** The choice \(\phi=1/D\) is retained exactly; it is bounded at fixed \(c\) by the reviewed posterior interval.
4. **Four endpoint constraints:** The \(59/40\) envelope uses posterior bounds at both sites and both revealed values.
5. **A reusable interface:** A future Bellman, transport, or moment certificate only has to prove (4.8); its average is then automatically paid by (4.9).

### What remains unpaid

The present insertion uses only a uniform table coefficient and the one scalar moment bound \(\mathbb ED\le M\). It does not quantify how often the near-extremal boundary family occurs under the actual sine posterior law, nor how high-\(r\) tables are paired with low-\(r\) tables beyond the Ward reveal identity.

To close the sign through Corollary 2, one needs either:

- a nonconstant \(\Phi\) satisfying (4.8) on the **actual support** and
  \[
  \mathbb E[(D-b)\Phi(q)]<1,
  \]
  or
- an averaged version of (4.8) using an additional actual-law statistic that detects the joint position of \((q_{i,0},q_{i,1},s_i)\).

The exact witness in Section 8 shows why the missing statistic cannot be only the four posterior interval bounds plus channel legality. A likely sufficient statistic must control the frequency of the cross-corner regime
\[
(x,y)\approx(R,t/R),
\]
which is precisely where \(U\) is smallest and \(r\) is largest.

No claim is made here that such a statistic is impossible; only that it has not yet been proved and is necessary for this route.

---

## 10. Sources and files

Required sources accessed successfully from branch
`research/sa-cycle09-s59-s60-20260918`:

- `research/CYCLE09_20260918/sources/S51_C1_AUTHOR.md`
- `research/CYCLE09_20260918/reviews/S51_C1_REVIEW.md`
- `research/CYCLE09_20260918/reviews/S55_CYCLE08_REVIEW.md`

Optional source also accessed:

- `research/CYCLE09_20260918/sources/S55_CYCLE08_AUTHOR.md`

The S55 material is used only to respect the already-reviewed transfer boundary and for finite-cycle context. No new sign or convergence-rate claim is attributed to it.

Accompanying files:

- `S59_CYCLE09_checks.py`: exact rational Sturm/log certificates, exact failure witness, numerical constants, and optional genuine finite cyclic projection diagnostics.
- `S59_CYCLE09_CHECKS_OUTPUT.txt`: exact-certificate output.
- `S59_CYCLE09_CHECKS_WITH_CYCLES.txt`: same checks plus finite cyclic diagnostics through \(n=14\).

The finite cyclic diagnostics are not used in any infinite-volume theorem above.
