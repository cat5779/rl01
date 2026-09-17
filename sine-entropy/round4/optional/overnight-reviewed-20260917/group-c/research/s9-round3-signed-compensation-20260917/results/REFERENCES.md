# Primary-source search and hypothesis audit

Search performed during this fresh S9 round, not claimed as an exhaustive
literature review or a priority determination. A bibliographic match alone is
not an imported theorem. Repository premises are separately frozen in
`DEPENDENCY_DELTA.md`.

## Sources read at the relevant theorem or argument

1. R. Lyons and J. E. Steif, *Stationary determinantal processes: phase
   multiplicity, Bernoullicity, entropy, and domination*, arXiv:math/0204324,
   https://arxiv.org/abs/math/0204324 . Proposition 3.4 supplies the stationary
   coupling bound for symbols. The present proof uses it through the reviewed
   repository noise-stability theorem. It does not infer a curvature modulus
   by differentiating that coupling or an entropy continuity bound.
2. A. Soshnikov, *Gaussian limit for determinantal random point fields*,
   arXiv:math/0006037, https://arxiv.org/abs/math/0006037 . The count CLT was a
   relevant starting point. Its scalar limit does not by itself justify
   multiplication by a complete, radius-dependent conditional production
   weight. Main Sections 2-5 instead prove an all-word conditional Lindeberg
   estimate and a quantitative local-weight replacement.
3. E. Hillion and O. Johnson, *A proof of the Shepp-Olkin entropy concavity
   conjecture*, arXiv:1503.01570, https://arxiv.org/abs/1503.01570 . The entropy
   in the count theorem is that of a Bernoulli sum. The S9 target is the entropy
   of the entire labelled configuration. The spatial conditional entropy is
   not removed by this theorem; the growing channel obstruction explicitly
   keeps it.
4. C. Leonard, *On the convexity of the entropy along entropic interpolations*,
   arXiv:1310.1274, https://arxiv.org/abs/1310.1274 . The interpolation is built
   from a fixed Markov reference and endpoint factors. No such representation
   of the actual common-diagonal-shift DPP path has been established here.
   A matching vocabulary about entropy production is not hypothesis matching.
5. E. Hillion, *Entropy along W1,+-geodesics on graphs*, arXiv:1406.5089,
   https://arxiv.org/abs/1406.5089 . Read Definition 2.6, the BB relation (10),
   the canonical-path requirement in Theorem 4.6, and its cube specialization.
   The natural affine-shift flux fails the BB equality by an explicit
   conditional covariance term; see the calculation below. This rejects a
   direct application with that flux, not all possible transport approaches.
6. A. Poinas and F. Lavancier, *Asymptotic approximation of the likelihood of
   stationary determinantal point processes*, arXiv:2103.02310,
   https://arxiv.org/abs/2103.02310 , DOI 10.1111/sjos.12613. Read the introduction
   and the approximation/Fisher-information scope in Sections 3 and 4.4.
   These results concern likelihood approximation and estimation, not the
   exact production-weighted mesoscopic compensation or the sign of the
   complete Shannon entropy Hessian. They are not premises of our finite KL
   comparison; that comparison is proved directly by a fixed spectral channel.

PDF render attempts accompanied the PDF inspection. Some arXiv screenshot
calls returned internal errors; those sources were then read as parsed text.
No claim rests on an unread figure or table.

## Related primary sources screened, not imported as proofs

* P.-M. Samson, *Entropic curvature on graphs along Schrodinger bridges at zero
  temperature*, arXiv:2003.05179 (revised 2022),
  https://arxiv.org/abs/2003.05179 . Abstract and stated scope screened.
  Curvature along the specified bridges does not identify the actual S9 path.
* C. A. N. Biscio and F. Lavancier, contrast estimation for parametric
  stationary DPPs, arXiv:1510.04222,
  https://arxiv.org/abs/1510.04222 . Statistical estimation rather than the
  required entropy sign; not used as a LAN theorem for this family.
* R. Bardenet and M. K. Titsias, DPP inference, arXiv:1507.01154,
  https://arxiv.org/abs/1507.01154 . Inference/likelihood methods screened;
  no applicable common-shift curvature result imported.
* O. Johnson and collaborators' discrete thinning and maximum-entropy work,
  arXiv:0904.1446, 0909.0641, math/0603647, and the review 1510.05390.
  These searches concern scalar ultra-log-concave count laws and thinning.
  They do not justify replacing labelled configuration entropy by count entropy.
* A. Meszaros, arXiv:1905.11459 and 2011.04012, and Lyons--Thom,
  arXiv:1402.0969: entropy/local-approximation questions are relevant context,
  but the screened results do not furnish this affine-shift Hessian sign.
* Entropic independence (arXiv:2106.04105), log-concave polynomial methods
  (arXiv:1807.00929), and Alishahi--Barzegar (arXiv:2006.13923) were screened
  for an averaged layer inequality. No precise applicable inequality closing
  the spatial compensation was found.
* Searches also surfaced quantum/spectral entropy and full-counting-statistics
  papers, including arXiv:2412.20244, 2607.14409 and 2605.11998. Their objects
  are not the complete classical labelled Shannon entropy in this assignment.
  No theorem from them is used, and their titles do not establish a solution.

## Exact obstruction to the natural-flux transport shortcut

For the common shift `K(a)=K_0+aI`, orient every cube edge from 0 to 1 and set
`f(y)=p_a(y)`, `g_i(y_{-i})=p_{a,-i}(y_{-i})`, and
`h_ij(y_{-i,-j})=p_{a,-i,-j}(y_{-i,-j})` on each ordered two-step path.
Multiaffinity of complete-event determinants gives exactly
`f'=-div g` and `g'=-div h`.

Fix the other coordinates, with total probability W, and let the normalized
conditional two-bit table be `(A,B,C,D)` for `(00,10,01,11)`. For the path
`00 -> 10 -> 11`, the BB residual is

`f(10) h - g(00,10) g(10,11) = W^2[B-(A+B)(B+D)]`
`= W^2(BC-AD)`.

A conditional Hermitian DPP has `AD-BC=-|K_ij^conditional|^2`, so the residual
is strictly positive whenever that conditional covariance is nonzero. The
BB equality required for the direct transport substitution is then false.
An inequality in its place is not the cited equality theorem. This does not
exclude another flux, another reference, or a new compensated transport
estimate. Those would require separate constructions and error control.
