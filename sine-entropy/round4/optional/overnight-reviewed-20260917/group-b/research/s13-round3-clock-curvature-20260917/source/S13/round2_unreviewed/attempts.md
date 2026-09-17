# Attempts and retained failures

## A. Exact all-`n` defect

1. Reconstructed the actual overlap kernel and the mean-overlap BL surrogate.
2. Centered the Fourier pair potential and verified it is a pure Johnson
   degree-two observable.
3. Derived the true degree-two multiplier in two independent forms: a
   mean/variance identity and a positive binomial-coefficient ratio.
4. Obtained the exact aggregate formula with the actual `pi_l`.
5. Initial hypothesis “the finite obstruction may be extensive” failed: the
   central layer multiplier gap is `d/n`, while the Fourier input amplitude is
   `n log n`; count averaging leaves a logarithmic defect.

## B. Curvature

1. Rejected the invalid inference that positive `Delta_n` means positive
   `Delta_n''`.
2. Used exact Bernoulli product differentiation to retain `pi_l'` and
   `pi_l''`.
3. Found that complement symmetry creates a cusp at the middle layer.  Its
   discrete second difference is `-2f_x/n^2`; the count local limit amplifies it
   to a `sqrt(n)log n` negative boundary layer.
4. Checked the integrated mass against the derivative jump of the limiting
   coefficient `C`; both give `-4c^2`.

## C. Positive repair

1. A generic “degree-two correction” was rejected because no positivity or
   normalization was available.
2. The deterministic potential clock survived: exact coefficient comparison
   proves `0<theta_l<1`, so forward BL heat realizes the multiplier.
3. A random-clock attempt to match degree one and two simultaneously failed by
   Jensen's inequality.  The failure is recorded only for that exact live
   class.

## D. Remaining direct route

After exact potential matching, the reference-KL curvature still contains all
moving-layer, Fisher, and acceleration terms.  No signed estimate was found in
this round.  The proof stops at this honest boundary rather than differentiating
value errors or restating the target.
