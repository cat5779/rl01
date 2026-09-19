# Visible assistant reply 85eb65a3-ff04-417a-be29-111619552f94

## PROVED: an explicit contrast extension through \(c=.9535\)

The full proposed rectangle through \(c=.96\) remains **INCOMPLETE**, but the following substantial subrectangle is certified:

\[
\boxed{
\rho=\frac13,\qquad
c\in\left[\frac{19}{20},\frac{1907}{2000}\right]=[.95,.9535],
\qquad
p\in\left[\frac{21}{50},\frac{12}{25}\right]=[.42,.48].
}
\]

**Deliverables:** :chatgpt-content-reference{index="2"} · :chatgpt-content-reference{index="3"} · :chatgpt-content-reference{index="4"}

### Exact theorem

With \(a=(1-c)p\), for the **true finite sine-compression configuration law**, uniformly on that rectangle,

\[
\boxed{
\partial_a^2 H_n(a,c)\le -\frac{n}{25}+441
\qquad(n\ge22).
}
\]

The derivative is taken with \(c\) fixed. Consequently, for every fixed \(c\in[.95,.9535]\), every
\[
a_0,a_1\in[.42(1-c),.48(1-c)],
\]
and \(0\le\lambda\le1\),

\[
\boxed{
\operatorname{Gap}_{\lambda}h(\cdot,c)
\ge
\frac{\lambda(1-\lambda)}{50}(a_1-a_0)^2.
}
\]

There is also a **stronger nested theorem** on \(c\in[.95,.953]\), with the same full \(p\)-interval:

\[
\partial_a^2H_n(a,c)\le-\frac n5+441,
\qquad
\operatorname{Gap}_{\lambda}h(\cdot,c)
\ge\frac{\lambda(1-\lambda)}{10}(a_1-a_0)^2.
\]

The certified contrast width is **\(7/2000=.0035\)**: 35% of the proposed extension from \(.95\) to \(.96\), retaining the entire requested \(p\)-width. At the upper contrast, the bias interval is correctly moved to **\([.01953,.02232]\)**.

This extends the packet’s accepted fixed-contrast S63 result to contrasts strictly above \(.95\). It does **not** improve S63’s boundary constant \(399\) at the seed contrast; the new boundary constant is \(441\). citeturn419677view0

## The reusable construction

The proof combines two tools, with their requirements, construction, and interface proved in `RESULT.md`.

**Endpoint-only exclusion for PSD block allocation.** An off-diagonal matrix entry \(B_{ij}\) must exclude its own two endpoint bits, but may depend on another target bit. The weighted mixed-score identity is applied before conditional score-martingale Jensen. This preserves guard information that an unnecessarily target-free allocation would discard.

The final witness uses a 22-site window and targets \(\{9,10,11,12\}\). Its diagonal allocation is
\[
C\,\frac{(19,11,11,19)}{60},
\]
and it shares distance-\(d\) pair payments across \(4-d\) block occurrences. The complete word-dependent matrix satisfies the certified uniform slack
\[
B(c,p,y)\succeq \frac1{200}I_4.
\]

**Exact two-parameter signed channel transport.** From the fixed reference law at \(c_*=.95,\ a_*=.025\), the full probability vector obeys
\[
\pi_{c,p,m}
=\prod_{i=1}^{m}(I+sD_i+vF_i)\pi_{*,m},
\]
where
\[
s=(1-c)(p-\tfrac12),\qquad v=\frac{c-c_*}{c_*},
\]
\[
D=\begin{pmatrix}-1&-1\\1&1\end{pmatrix},
\qquad
F=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

This transport preserves normalization and equals the moving actual law. It can be signed; it is not asserted to be a Markov post-processing kernel. In particular, \(F^2=F\ne0\), so contrast evolution is not justified by shift-only nilpotence. The proof supplies the multivariate derivative formulas, normalization, scaling, and a whole-vector remainder bound.

## Quantitative closure

The new global cap is
\[
C(c,p)=1.303+.255p+8(c-.95).
\]

For the constructed fixed-test, moving-law payment \(P(c,p)\), the continuum certificate proves

\[
\boxed{
P(c,p)-(C(c,p)-1)d((1-c)p,c)\ge\frac1{25},
\qquad P(c,p)\le21.
}
\]

The completed checks are:

| Obligation | Verified coverage |
|---|---|
| Global pair cap | \(33{,}600\) closed parameter cells |
| Guard caps | \(10{,}752\) parameter–word cells at each of distances \(1,2,3\), with all 256 guard words |
| Strict PSD slack | \(16{,}384\) exact rational corner matrices |
| Reference probabilities and payment | All \(2^{22}=4{,}194{,}304\) spatial configurations |

All three **clean final-source guard runs completed with zero failures**. The payment uses 45 bivariate coefficient boxes for each of three potential components. The whole-vector tail payment is below \(3.476374\times10^{-8}\), conservatively paid by \(10^{-6}\). Exact tensor Bernstein inequalities close the payment and upper bound over the entire rectangle—not just a finite parameter grid.

The explicit boundary follows from the \(n-21\) contained windows:

\[
H_n''
\le n(C-1)d-(n-21)P
\le-\frac n{25}+21\cdot21.
\]

The entropy-rate conclusion is obtained by passing **finite chord inequalities** to the entropy-value limits. No \(o(n)\) error is differentiated, and no second derivative of \(h\) is assumed.

A separate direct all-word tensor evaluation, without Walsh expansion or truncation, encloses the payment margin at the narrow corner \((c,p)=(.9535,.42)\) within
\[
[\,0.0402893383954,\;0.0402893384014\,],
\]
consistent with the uniform \(1/25\) certificate.

## What prevents this witness from reaching \(.96\)

There is a **proved obstruction to this particular witness**, not to entropy concavity.

At the legal point
\[
c=.96,\qquad p=.45,\qquad a=.018,
\]
the same final witness formulas satisfy
\[
\boxed{P-(C-1)d<-3.}
\]

The exact coefficient-and-tail certificate proves this inequality. The separate direct full-word calculation gives the tighter enclosure
\[
P-(C-1)d\in
[-3.277834391895,\,-3.277834391888].
\]

Thus merely computing the present witness more accurately cannot close the full target. The remaining load-bearing task is an admissible replacement or supplementary payment satisfying
\[
\inf_{\substack{c\in[.9535,.96]\\p\in[.42,.48]}}
\left\{\widetilde P(c,p)
-[\widetilde C(c,p)-1]d((1-c)p,c)\right\}>0,
\]
together with its corresponding cap and PSD-allocation conditions.

The packet contains complete proofs, all witness rows and coefficient bounds, successful final logs, separately labeled failed attempts, preserved supplied sources, exact tests, and `run_all.sh`. The reference probability caches are reconstructed from source rather than required as attachments. **The explicit \([.95,.9535]\) theorem is proved by the supplied computer-assisted argument; the full \([.95,.96]\) target and independent external acceptance remain unclaimed.**
