# Research checkpoint

## Outcome

This round advances beyond the provisional \(O(\sqrt n)\) actual transport-residual payment by replacing the unresolved midpoint transport bookkeeping with an exact identity using the **actual compatible adjacent output layers**.

At half density, \(n=2m\), and the balanced midpoint \(a_0=(1-c)/2\), write

\[
\mathcal D(a)=\Phi(a)-H(a)=\sum_l\pi_l(a)F_l(a),
\qquad v=(1-c^2)/4.
\]

For each boundary \(l\leftrightarrow l+1\), define edge laws

\[
\mathsf A_l(S,T)=\nu_{l+1}(T)/(l+1),
\qquad
\mathsf B_l(S,T)=\nu_l(S)/(n-l),
\]

on \(S\subset T\), and

\[
\mathscr J_l=(l+1)\pi_{l+1}D(\mathsf A_l\|\mathsf B_l)
 +(n-l)\pi_lD(\mathsf B_l\|\mathsf A_l).
\]

The new exact theorem is

\[
v^2\mathcal D''(a_0)
=\sum_l\pi_l[(l-m)^2-nv]F_l
+v\sum_l\mathscr J_l.
\]

Equivalently,

\[
v^2H''(a_0)=v^2\Phi''(a_0)
-\sum_l\pi_l[(l-m)^2-nv]F_l
-v\sum_l\mathscr J_l,
\]

with

\[
\Phi''(a_0)
=-\sum_l\pi_l''\log(\pi_l/\binom nl)-n/v.
\]

This is the requested full moving-count/reference/intrinsic checkpoint at one nonshrinking high-contrast point in shift space.  It does not drop \(\pi_l''F_l\), count Fisher, normalizers, deterministic layers, or the actual conditional response.


## Prior-versus-new dependency table

| Item | Status on entry | Used by the new theorem? | This round's contribution |
|---|---|---:|---|
| Exact disintegration \(H=\Phi-\sum_l\pi_lF_l\) | Reviewed baseline | Yes | Retained without alteration |
| Full actual transport identity | Reviewed/provisional prior S5 input | No | The midpoint proof is an independent finite-sum derivation |
| \(O(\sqrt n)\) residual payment | Provisional latest author result | No | Restated explicitly; neither assumed nor re-proved |
| Positive within-slice Fourier budget | Provisional latest author result | No | Not used, because it does not pay the moving count law |
| Fourier-to-Toeplitz value bridge | Reviewed baseline | No for the theorem | Mentioned only in the target-level gap audit |
| Actual consecutive-layer laws | Not previously supplied in this form | Yes | Derived exactly, including normalizers and both directions |
| Midpoint count/adjacent cancellation | New | — | Proved in Theorem 6.1 |
| Central payment inequality | Open | — | Isolated exactly as the next obligation |

## Mechanism

The actual conditional weights are

\[
w_l(S)=\sum_A\mu(A)R^{|A\cap S|}.
\]

Their insertion and deletion ratios satisfy the exact identity

\[
H_l(S)-RG_l(S)=n+(R-1)m-(R+1)l.
\]

This gives two equal formulas for \(\partial_\theta\nu_l\), one through uniform deletion of the actual layer \(l+1\), the other through uniform insertion from the actual layer \(l-1\).  Differentiating \(F_l\) produces neighboring entropy differences plus the two directed edge KL divergences.  At the balanced midpoint, the count Stein identity produces precisely the opposite neighboring entropy differences.  Averaging the two directions cancels all of them, leaving the count covariance and weighted Jeffreys production above.

## Fourier evidence

For the genuine contiguous \(P_{n,n/2}\) family at \(c=0.95\), direct finite calculations give positive \(v^2\mathcal D''\) through \(n=20\).  For example, at \(n=20\),

\[
-0.251561598199+0.313263503094=0.061701904896.
\]

The first number is the moving-count covariance and the second is the actual-adjacent production.  This is a floating diagnostic, not an all-\(n\) proof.

## Exact remaining issue

The unproved central payment is

\[
v\sum_l\mathscr J_l
\ge
\sum_{|l-m|<\sqrt{nv}}\pi_l[nv-(l-m)^2]F_l
-
\sum_{|l-m|\ge\sqrt{nv}}\pi_l[(l-m)^2-nv]F_l.
\]

That inequality would prove \(\mathcal D''(a_0)\ge0\).  Full entropy concavity at the midpoint needs only the weaker lower bound by \(v^2\Phi''(a_0)\), recorded exactly in `proof.md`.

No fixed-chord conclusion follows from this pointwise midpoint result.  No target-level theorem is claimed.
