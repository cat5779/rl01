# Verified public primary sources

## Erbar–Maas–Tetali

Matthias Erbar, Jan Maas, and Prasad Tetali, *Discrete Ricci curvature bounds for Bernoulli–Laplace and random transposition models*, arXiv:1409.8605.

- Abstract: https://arxiv.org/abs/1409.8605
- Original paper PDF inspected: https://arxiv.org/pdf/1409.8605
- Section 1.2 and Theorem 1.1, printed page 3: displayed exchange rate `1/[l(n-l)]`, uniform reversible measure, curvature lower bound `(n+2)/[2l(n-l)]`.
- Equations (2.1) and (2.2), printed page 5: logarithmic-mean continuity equation and relative entropy.
- Equation (2.3), printed page 6: the Bochner form, including its factors of `1/2`, the edge pairing, and the two partial derivatives of the logarithmic mean.
- Theorem 2.2, printed page 7: finite irreducible reversible setting, positive densities, equivalence with the Bochner Hessian inequality.

The displayed transition rates fix the normalization used in the proof. We did not infer normalization from the paper's verbal waiting-time sentence. PDF text and page screenshots were inspected. Positive curvature is only used for the explicitly computed slice Hessian, never as an automatic sign of the full parameter second derivative.

## Erbar–Maas

Matthias Erbar and Jan Maas, *Ricci curvature of finite Markov chains via convexity of the entropy*, arXiv:1111.2687.

- Abstract: https://arxiv.org/abs/1111.2687
- Author-hosted original paper inspected: https://www.janmaas.org/papers/Ricci.pdf
- Proposition 3.4, printed page 19: geodesic equations for the density and potential. The potential equation contains one half of the logarithmic-mean-derivative quadratic edge expression.
- Proposition 4.3, printed pages 20–21: Hessian of relative entropy equals the Bochner form.

The source uses a Markov kernel and generator `K-I`. The proof translates this to the explicitly normalized slice generator. Constants in a potential are irrelevant to both the gradient and the acceleration pairing.

## Supplied project inputs, not external discoveries

The original prompt supplies the channel representation, count decomposition and concavity of `Phi`, solved low-contrast and rank-one baselines, conditioning-minor formulas and their known failures, true Toeplitz definition, Fourier-to-Toeplitz value bridge, entropy value-tail estimate, and endpoint continuity modulus. These are not counted as new results and were not sought in private files.

The combinatorial harmonic eigenfunction identities, conditional-kernel multipliers, rank-one/rank-two channel multipliers, centered determinant moment identity, and Fourier growth lift used here are proved directly in `proof.md`; no additional unverified external theorem is invoked for them.

Sources were accessed during the measured work session on 2026-09-16 UTC. No private workspace, connector data, or prior private document was accessed. Reproducing the finite certificates is offline and does not require downloading these papers.

## Hillion–Johnson: count entropy only

Erwan Hillion and Oliver Johnson, *A proof of the Shepp–Olkin entropy concavity conjecture*, arXiv:1503.01570. Primary full text: https://arxiv.org/html/1503.01570v1 ; abstract: https://arxiv.org/abs/1503.01570 .

Theorem 1.2 states concavity of the entropy of a sum of finitely many independent Bernoulli variables in their full probability-parameter vector in `[0,1]^n`. The paragraph following the theorem explicitly reduces to affine parameter paths. This hypothesis was verified before applying it in proof Section 2.3 to the count of the actual nonprojection Toeplitz DPP, whose Bernoulli success parameters are `a+c eta_j`. No conclusion about full configuration entropy is imported from this result. The count use is part of the supplied baseline perspective, not counted as new progress.
