# Independent audit: balanced-midpoint actual-adjacent identity

STATUS: **CORRECT**

The accepted scope is Theorem 6.1 in `proof.md`: for every probability law on the \(m\)-subsets of \([2m]\), every \(0<c<1\), and \(a_0=(1-c)/2\),

\[
v^2(\Phi-H)''(a_0)
=\sum_l\pi_l\bigl[(l-m)^2-nv\bigr]F_l
+v\sum_{l=0}^{n-1}\mathscr J_l,
\qquad v=(1-c^2)/4.
\]

This is an exact finite-dimensional identity.  It does **not** prove a favorable sign for the right-hand side, midpoint concavity of \(H\), a shift interval, a fixed-chord estimate, a thermodynamic derivative, or the sine entropy-rate target.

## What was checked

1. The factorization \(p_a(S)=B_l(a)w_l(S;R)\) has the correct powers of \(a\), \(1-a\), and \(1-a-c\).
2. For each monomial \(R^{|A\cap S|}\), insertion minus \(R\) times deletion gives \((R+1)(m-l)R^{|A\cap S|}\).  This proves Lemma 3.1 without any DPP assumption.
3. Edge double counting gives
   \(\bar H_l=(l+1)e_{l+1}/e_l\) and
   \(\bar G_l=(n-l+1)e_{l-1}/e_l\).  The factors \(l+1\) and \(n-l+1\) and both endpoint conventions are correct.
4. The likelihood ratio on \(S\subset T\) is exactly \(r_{l+1}(T)/r_l(S)\).  Therefore both formulas for \(\partial_\theta F_l\) have the stated direction and KL sign.
5. At the midpoint, \(R_0=((1+c)/(1-c))^2\), \(v^2\theta''=2c\), and
   \(\sqrt{R_0}/(R_0-1)=v/c\).  These identities give both adjacent normalizers in (5.5) with no missing factor.
6. Differentiating the count probability generating function gives (5.6), including the boundary terms \(\pi_{-1}=\pi_{n+1}=0\).  Multiplying by \(F_l\) and shifting indices gives (6.8).
7. Averaging the upper and lower entropy derivatives gives (6.9).  Its coefficient of \(F_{l+1}-F_l\) is \(v(b_l-a_l)\), exactly cancelling the coefficient \(v(a_l-b_l)\) from (6.8).  The surviving KL coefficients are exactly
   \((l+1)\pi_{l+1}C_l^+ +(n-l)\pi_lC_l^-\).
8. The reference curvature contains both the moving-normalizer term and the count Fisher term.  The common midpoint score is \((l-m)/v\), hence \(\sum_l(\pi_l')^2/\pi_l=n/v\), as used in (6.6).
9. The square-face formula has the correct factor \(2\), sign pattern, and Fisher subtraction.  It is a separate full-atom representation of the same Hessian.

## Exact and numerical replay

- The archive manifest verified all 93 frozen files.
- The frozen exact certificate reproduced semantically with rational arithmetic and formal prime-log coefficient vectors.
- Fourier replay at \(n=4,6,8,10\) had maximum adjacent-identity residual \(6.01\times10^{-16}\), maximum square-face residual \(1.63\times10^{-12}\), and maximum entropy-split residual \(1.82\times10^{-12}\).
- `scripts/audit_non_dpp_check.py` repeats the exact identities for a strictly non-DPP positive rational law with weights
  \((10,1,1,1,1,10)/24\) on the six pairs of four sites.  For a complex rank-2 projection DPP, the three Pluecker product magnitudes must close a triangle; here they are proportional to \(10,1,1\), so \(10>1+1\) is an exact obstruction.  All exact assertions pass for this case.

## Evidence-label correction

The author's second frozen four-site case was labelled `non_dpp_rational_mu`, with pair weights \((1,2,3,4,5,5)/20\).  That label is not justified and is in fact false for complex projection DPPs: the three Pluecker product magnitudes are proportional to \(\sqrt5,\sqrt{10},\sqrt{12}\), which satisfy all strict triangle inequalities, so phases can satisfy the sole Pluecker relation in \(\Lambda^2\mathbb C^4\).  This does not affect Theorem 6.1 or any algebraic assertion in the frozen certificate.  The reviewed proof treats that case only as a general rational homogeneous input and uses the new \(10,1,1\) case for the non-DPP comparison.

## Dependency boundary

The prior round-4 \(O(\sqrt n)\) residual payment is **UNREVIEWED AND RETAINED ONLY FOR PROVENANCE**.  The accepted midpoint theorem does not invoke it.  No conclusion in this review upgrades that residual claim.

The main target sign is still unpaid: neither the central adjacent-payment inequality (8.1) nor the weaker full-entropy inequality (8.2) has been proved.  The target therefore remains **OPEN**.
