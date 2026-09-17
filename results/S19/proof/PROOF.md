# A positive-density obstruction to a vanishing-exception double-budget repair

**Status: DISPROVED_ROUTE_LEMMA — author proof and author exact certificate;
not independently reviewed.** This is not a counterexample to entropy
concavity. It does not prove the sign of the complete signed near field.

Frozen family throughout this note:

\[
 Q_B=T_B(\mathbf1_{[-1/4,1/4]}),\quad
 K_B(a)=aI+\frac{19}{20}Q_B,\quad
 a\in J=[1/50,3/100],\quad B=\{0,\ldots,n-1\}.
\]

These are genuine contiguous Toeplitz compressions, not finite projections
or independent products. Write \(c=19/20\), \(d=1-a-c\), and
\(\delta=\min(a,d)\ge1/50\). All output averages below are under the
complete labelled law \(\operatorname{DPP}(K_B(a))\). Logarithms are natural.

## 1. The specific aggregate rule being ruled out

For a pair \(i,j\), condition on **all other outputs in B**. Its conditional
output kernel and four probabilities are

\[
 C_Z=\begin{pmatrix}q&\zeta\\\bar\zeta&r\end{pmatrix},\quad s=|\zeta|^2,
\]
\[
 A=(1-q)(1-r)-s,\quad B_1=q(1-r)+s,\quad
 C_1=(1-q)r+s,\quad D=qr-s.
\]

Use the order \((00,10,01,11)\) and let

\[
 g_Z=\log\frac{B_1C_1}{AD}
       -s\left(A^{-1}+B_1^{-1}+C_1^{-1}+D^{-1}\right).       \tag{1}
\]

This is the exact acceleration **minus mixed Fisher** contribution. It is
not the acceleration term alone.

The corresponding conditional input kernel has diagonal entries
\(x=(q-a)/c\), \(y=(r-a)/c\), and squared off-diagonal \(z=s/c^2\).
Put

\[
 \beta_0=(1-a)d,\qquad\beta_1=a(a+c),
\]
\[
 r_i^0=x+\frac{cz}{1-r},\quad r_i^1=x-\frac{cz}{r},\qquad
 r_j^0=y+\frac{cz}{1-q},\quad r_j^1=y-\frac{cz}{q}.
\]

Define the **existing combined two-budget quantity**, with all four actual
completion weights already summed, by

\[
 W_Z=\sum_{u,v\in\{0,1\}}\frac{z}{p_{uv}}
 \left\{\frac{\beta_v}{4r_i^v(1-r_i^v)}
            +\frac{\beta_u}{4r_j^u(1-r_j^u)}\right\}.       \tag{2}
\]

It is the conditional \(\mathcal K+\mathcal D\) from the reviewed
`proofs/stationary-double-budget-route.md`, not S7's scalar table
\(\mathcal K_{R,L}\). The two uses of the letter K must not be confused.

For a fixed coefficient \(\gamma\le2\), a natural proposed repair of the
failed pointwise comparison is the following **vanishing-exception rule**:

\[
 \mathsf{VE}_\gamma:\qquad
 \sum_{i<j}\mathbb E[(g_{ij,+}-\gamma W_{ij})_+]=o(n).       \tag{3}
\]

The same proposal can be made just for near pairs \(j-i<R\), with
\(R\ge6\), or for S7's locally conditioned tables as \(R,L\to\infty\).
This note disproves all these stated vanishing-exception versions. It does
**not** disprove a signed estimate for \(\sum(g-\gamma W)\), or a
nonvanishing exception allowance that is paid by a separate negative margin.

Why (3) is a relevant payment rule: let
\(\mathcal I_n=\sum_i\mathbb E[t_i(1-t_i)]^{-1}\), where
\(t_i=\Pr(Y_i=1\mid Y_{-i})\). The exact finite Hessian and the reviewed
combined budget are

\[
 H_n''=-\mathcal I_n+2\sum_{i<j}\mathbb E g_{ij},\qquad
 \sum_{i<j}\mathbb E W_{ij}\le\mathcal I_n/4.               \tag{4}
\]

Consequently (3), for \(0\le\gamma<2\), would give
\(H_n''\le-(1-\gamma/2)\mathcal I_n+o(n)\). At \(\gamma=2\) it
would give an asymptotically nonpositive upper bound. Thus (3) is a concrete
local-to-global sufficient rule, not a reformulation of the desired answer.

To make the actual-law derivative in (4) explicit, temporarily assign each
site its own diagonal shift. For the mixed derivative in sites i,j, the
outside marginal is independent of those two shifts. Its conditional Schur
kernel has q and r affine with the corresponding slopes one, while its
off-diagonal is independent of them. The four mixed probability derivatives
are \((1,-1,-1,1)\). Differentiating their complete entropy gives the
logarithm in (1) from probability acceleration and the reciprocal term in
(1) from mixed Fisher information. A repeated one-site derivative is
\(-[t_i(1-t_i)]^{-1}\). Summing every coordinate partial and both orders
of each mixed partial proves (4)'s Hessian identity. Holding the outside law
fixed is justified only for those coordinate partials; this is not freezing
the moving law in the common-shift derivative.

For completeness, the budget in (4) is seen directly from the common full
input-posterior kernel \(R^Y\). Its directed row satisfies
\(\sum_{j\ne i}|R^Y_{ij}|^2\le R^Y_{ii}(1-R^Y_{ii})\).
Divide by \(4\beta_{Y_i}r_i(1-r_i)\) and average \(Y_i\) with its actual
conditional law. Bayes' rule gives

\[
 \mathbb E\left[\left.
 \frac{R^Y_{ii}(1-R^Y_{ii})}{\beta_{Y_i}}
 \right|Y_{-i}\right]
 =\frac{r_i(1-r_i)}{t_i(1-t_i)}.
\]

Each unordered pair joins its two directed rows exactly once, yielding
(4). Formula (2) follows from
\(|R^{uv}_{ij}|^2=z\beta_u\beta_v/p_{uv}^2\). These are the inherited
budgets; their re-display here is for a self-contained definition, not a
new claim of credit.

## 2. The new theorem

Set the explicit, fixed buffer and cylinder length

\[
 L_0=2\,020\,000,\qquad N_0=2L_0+4=4\,040\,004,\qquad
 \kappa=\frac1{12}\,50^{-N_0}>0.                            \tag{5}
\]

**Theorem.** Uniformly for every \(a\in J\), every integer n>=1, and every
\(\gamma\le2\),

\[
 \boxed{\quad
 \sum_{i=0}^{n-6}
  \mathbb E[(g_{i,i+5,+}-\gamma W_{i,i+5})_+]
 \ge (n-2L_0-5)_+\,\kappa .\quad}                         \tag{6}
\]

An empty sum is zero. In particular the lower limit after division by n
is at least \(\kappa\), not zero. For \(n\ge4L_0+10\) the right side is
at least \(n\kappa/2\). Since distance 5 is a near pair for every \(R\ge6\),
(6) applies unchanged as a lower bound for the corresponding near-pair
positive-exception sum, even when R grows with n.

There is also a direct statement for the **exact S7 tables**. Let
\(p^{(5,L)}\) be the table for \(0,5\) conditioned on every other output in
\([-L,5+L]\), and construct \(W^{(5,L)}\) by (2). For every \(L\ge L_0\),

\[
 \boxed{\quad
 \mathbb E[(g(p^{(5,L)})_+-\gamma W^{(5,L)})_+]\ge\kappa.
 \quad}                                                    \tag{7}
\]

Thus the obstruction persists in the limit order used in S7: n first, then
large R and L, or along any choice with \(R\ge6\), \(L\ge L_0\). It is
not an isolated small-volume contraction and it does not disappear at the
actual growing-table scale.

The constant is deliberately conservative and extremely small. The theorem
rules out **o(n)** exceptions, not a practically large positive-curvature
mass. No positive sign of the total entropy Hessian follows from (6).

## 3. An explicit infinite alternating reference

Let P be the ambient half-density Fourier projection on \(\ell^2(\mathbb Z)\):

\[
 P_{ii}=1/2,\qquad P_{ij}=q_{i-j}
 =\frac{\sin(\pi(i-j)/2)}{\pi(i-j)}\quad(i\ne j).
\]

Let \(S=2P-I\) and \(J_{ii}=(-1)^i\). Then

\[
 S^*=S,\quad S^2=I,\quad J^2=I,\quad JS=-SJ.                \tag{8}
\]

The last identity follows because every nonzero off-diagonal of S joins
opposite parities. Only the **ambient** operator in (8) is a projection
construction; no identity \(Q_B^2=Q_B\) is used.

Put \(t=a-1/40\), so \(|t|\le1/200\). For the alternating word with
output 1 at even sites and 0 at odd sites, its infinite inverse pencil is

\[
 A_* =tI+\tfrac12J+\tfrac c2 S,
 \qquad
 G_* =A_*^{-1}=
 \frac{\tfrac12J+\tfrac c2S-tI}{D_0},\qquad
 D_0=\frac{1+c^2}{4}-t^2.                                  \tag{9}
\]

This is a bounded operator identity, not conditioning on a probability-zero
infinite word. It is only a deterministic reference for finite pencils.
We have

\[
 D_0\ge1189/2500>19/40,\qquad \|A_*\|<1.                   \tag{10}
\]

Take the target pair \(D=\{0,5\}\), completed as \((1,0)\). Write
\(q_5=1/(5\pi)\) and \(E_0=1/4+c^2q_5^2-t^2\). Direct 2 by 2 inversion
of \((G_*)_{DD}\), followed by adding \(\operatorname{diag}(0,1)\), gives

\[
 C_*^{\rm alt}=\begin{pmatrix}q_*&\zeta_*\\\zeta_*&r_*\end{pmatrix},
\]
\[
 q_* =\frac{D_0(1/2+t)}{E_0},\qquad
 r_* =1+\frac{D_0(-1/2+t)}{E_0},\qquad
 \zeta_* =\frac{D_0 c q_5}{E_0}.                            \tag{11}
\]

The superscript distinguishes this matrix from S7's error constant \(C_*\).

**Certified scalar margin.** On the whole closed interval J, and on the
following entire perturbation box around (11),

\[
 |q-q_*|\le10^{-4},\quad |r-r_*|\le10^{-4},\quad
 |s-\zeta_*^2|\le10^{-4},
\]

one has positive atoms, valid reverse-Bayes denominators, and

\[
 \boxed{\qquad g(q,r,s)-2W(a;q,r,s)>1/12.\qquad}            \tag{12}
\]

Section 7 describes the complete rational certificate. As orientation only,
the unperturbed excess is approximately 0.1386405881 at a=0.02 and 0.03,
and 0.1472386103 at a=0.025. None of these floating numbers is used to
establish (12).

## 4. Uniform finite-volume stability near that one background

This is the step that converts a special word into a genuine growing-family
obstruction. It is **not** a word-uniform inverse-entry estimate.

Let a finite interval B contain
\(I=[-L,5+L]\), and let a complete finite word y agree with the alternating
reference on I. Its values on \(B\setminus I\) are arbitrary. Define

\[
 A_y=aI_B+cQ_B-\operatorname{diag}(1-y),\qquad G_y=A_y^{-1}.
\]

Every such pencil has \(\|G_y\|\le\delta^{-1}\le50\). One elementary
proof partitions the sites according to y and multiplies A_y on the left
by the corresponding sign matrix. The Hermitian part becomes the block
matrix with diagonal blocks \((K_B)_{11}\) and \((I-K_B)_{00}\), each at
least \(\delta I\). Therefore the least singular value of A_y is at least
\(\delta\). This argument does not assert that A_y is positive definite.

**Reference stability lemma.** For every such B and y,

\[
 \boxed{\quad
 \|(G_y)_{DD}-(G_*)_{DD}\|\le202/L.\quad}                  \tag{13}
\]

**Proof.** For any vector x supported on D put \(v=G_*x\), and split v
into \(v_B\) and \(v_O\), with O the complement of B in \(\mathbb Z\).
The difference
\(E=(A_y-(A_*)_{BB})\) is diagonal, has norm at most one, and is supported
on \(B\setminus I\). Since \(A_*v=x\), the residual is

\[
 r=A_yv_B-x=Ev_B-(A_*)_{BO}v_O.                             \tag{14}
\]

Writing \(x=A_yv_B-r\) and expanding the quadratic form gives the exact
identity

\[
 \langle x,G_yx\rangle-\langle x,G_*x\rangle
 =-\langle v_B,r\rangle+\langle r,G_yr\rangle.              \tag{15}
\]

The outside equation
\((A_*)_{OB}v_B+(A_*)_{OO}v_O=0\) also gives

\[
 \langle v_B,r\rangle
 =\langle v_B,Ev_B\rangle+
   \langle v_O,(A_*)_{OO}v_O\rangle.
\]

Consequently, with \(T=\|v_{I^c}\|^2\), (10) implies

\[
 |\langle v_B,r\rangle|\le T,\qquad
 \|r\|^2\le2T.
\]

Thus the absolute value of (15) is at most \(101T\). On \(I^c\) the
identity and J terms in (9) vanish when applied to x, so

\[
 \begin{aligned}
 T&\le\|x\|^2\|\mathbf1_{I^c}G_*\mathbf1_D\|_{\rm HS}^2\\
 &\le\|x\|^2\frac{4c^2}{\pi^2 D_0^2}
                  \sum_{r=L+1}^\infty r^{-2}\\
 &\le\frac{2}{L}\|x\|^2.
 \end{aligned}                                             \tag{16}
\]

The final bound uses \(\sum_{r>L}r^{-2}\le1/L\), \(\pi>3\), and
\(4/(9(19/40)^2)=6400/3249<2\). The estimate intentionally includes
zero even-lag coefficients in an upper bound. Taking all unit x in the
Hermitian quadratic-form estimate proves (13). QED.

Now let Z be an outside word on \(B\setminus D\) agreeing with the
alternating reference on \(I\setminus D\). Complete its two missing bits
as (1,0) only as an algebraic device. The conditional output kernel satisfies

\[
 S_Z=C_Z-\operatorname{diag}(0,1)=((G_y)_{DD})^{-1},
 \qquad\|S_Z\|\le1.                                      \tag{17}
\]

Indeed, the unchanged output channel applied to the input posterior gives
\(aI\preceq C_Z\preceq(a+c)I\). For these finite sine compressions the
input and its complement are strictly positive: a nonzero finite Fourier
polynomial has positive squared integral on each of the two frequency
intervals. A positive external-field reweighting of its L-ensemble is again
a DPP with a positive-contraction kernel. This proves the conditional strip
used in (17), without a finite-projection assumption.

For \(S_*=(G_*)_{DD}^{-1}\), formula (11) gives \(\|S_*\|<1\) as well.
For an entirely rational bound, use

\[
 \|S_*\|\le
 \frac{761/1600}{9999/40000}\left(\frac1{200}+\frac{51}{100}\right)
 =\frac{1959575}{1999800}<1.
\]

Here \(\sqrt{1/4+c^2q_5^2}<51/100\) follows from \(q_5<1/15\).
The inverse identity and (13) now yield

\[
 \|C_Z-C_*^{\rm alt}\|
 \le\|S_Z\|\,\|(G_*)_{DD}-(G_y)_{DD}\|\,\|S_*\|
 \le202/L.                                                \tag{18}
\]

Also \(|\zeta_Z|\le c/2<1/2\), while the elementary bounds
\(D_0<1/2\), \(E_0>1/5\), \(q_5<1/15\) give
\(|\zeta_*|<1/6\). Therefore

\[
 \big||\zeta_Z|^2-|\zeta_*|^2\big|
 \le(|\zeta_Z|+|\zeta_*|)|\zeta_Z-\zeta_*|
 \le202/L.                                                \tag{19}
\]

Taking \(L=L_0\) in (18)–(19) gives exactly the perturbation radius in
(12). Thus **every** finite outside word extending that fixed cylinder,
regardless of its remaining bits or the volume n, has

\[
 g_Z-2W_Z>1/12.                                            \tag{20}
\]

## 5. The actual-law probability payment and extensivity

Generate \(X_B\sim\operatorname{DPP}(Q_B)\) and conditionally independent
output bits with
\(\Pr(Y_i=1\mid X_i)=a+cX_i\). This generates exactly
\(\operatorname{DPP}(aI+cQ_B)\), as is verified by expanding the principal
minor for each output inclusion event.

For either prescribed output bit and either value of its latent input bit,
the channel likelihood is at least \(\delta\ge1/50\). Hence any prescribed
pattern on k sites, with all other output bits summed rather than fixed,
has actual probability at least \(50^{-k}\). In particular,

\[
 \Pr\{Y_{I\setminus D}\hbox{ is the specified alternating pattern}\}
 \ge50^{-(2L_0+4)}.                                       \tag{21}
\]

No probability is assigned to the infinite alternating word. No uniform
measure on output words is substituted. This finite-cylinder lower bound
is why an exponentially rare **whole-volume** word is not being mistaken
for a positive-density obstruction.

On this event (20) holds, and \(W_Z\ge0\). Thus for every \(\gamma\le2\)
the expected positive exception for this pair is at least \(\kappa\).
Translate the pair and its cylinder to every i for which
\([i-L_0,i+5+L_0]\subseteq B\). There are \((n-2L_0-5)_+\) such i.
Linearity of expectation proves (6). The cylinders may overlap heavily;
no independence assertion is made or needed.

Apply the same argument with the finite interval \([-L,5+L]\) to obtain
(7). This also proves that taking the local conditioning radius to infinity
does not turn the exception allowance into a vanishing one. QED.

## 6. Consequences and limits

The exact near-field expression in S7 still contains the **signed** sum
\(2\sum_{r<R}\mathbb E g(p^{(r,L)})\). The theorem does not determine that
sum. It rules out upgrading the old pointwise comparison to the true sine
family merely by declaring its violations negligible after actual averaging.
The violation occurs at a fixed spatial separation and survives every
sufficiently large local conditioning radius.

Negative pairs, unused row-budget slack, or another explicitly quantified
nonzero allowance may still compensate it. In fact the alternating reference
has strongly negative nearest-pair contributions. That observation is a
diagnostic reason not to confuse the positive exception mass with a positive
full Hessian. No claim about a maximal legal interval, other densities, or
cyclic approximations is made.

The full sine entropy-rate target is still open in this packet. S7's original
Theorems A–F and Corollary G are unchanged. The new statement concerns one
specific proposed aggregate payment, not all possible signed groupings.

## 7. Exact finite certificate and analytic checks

`code/verify_reference_payment.py` uses only the Python standard library.
It covers J with 200 closed rational cells of width 1/20000 and expands the
reference q, r, and squared off-diagonal by the full radius 1/10000 on each
cell. It encloses the expression (1) minus twice (2), including every
completion. It also verifies positive atoms, positive input contraction
caps, and strict reverse-Bayes probabilities on every enlarged cell.

The arithmetic is interval arithmetic with integer endpoints on the dyadic
grid of denominator \(2^{120}\). Each multiplication and reciprocal is
rounded outward. The bound on pi comes from
\(\pi=16\arctan(1/5)-4\arctan(1/239)\), using 32 alternating terms and
the next term as a remainder bound. The tangent identity fixes the branch:
\(\tan(4\arctan(1/5))=120/119\) and
\(4\arctan(1/5)-\arctan(1/239)\in(0,\pi/2)\) has tangent 1.

Logarithms use power-of-two range reduction and

\[
 \log u=2\sum_{k=0}^{39}\frac{z^{2k+1}}{2k+1}+\mathcal R,
 \quad z=\frac{u-1}{u+1}\in[0,1/3],\quad
 0\le\mathcal R\le\frac{2z^{81}}{81(1-z^2)}.
\]

The saved `checks/reference_payment.json` contains all 200 cell enclosures,
pi endpoints, source hash, actual timestamps and runtime. The minimum lower
endpoint is approximately 0.08632587284, strictly above 1/12 by an integer
comparison. Floating-point displays are not part of the sign decision.

`code/verify_analytic_constants.py` separately checks the rational constants
in (10), (13), (16), and (18)–(21), the cutoff count and the comparison with
the inherited one-sided refund. `code/test_dpp.py` and the floating diagnostics
are implementation checks, not premises of the theorem. No missing S7
six-site script or historical author-only receipt is a premise.
