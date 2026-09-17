# Candidate ledger and primary-source hypothesis audit

This is a record of the candidates considered in this fresh PR111 round, not
an assertion of an exhaustive literature search or a priority claim. The
reviewed repository baseline is `aaf3e86576a867067701089805c9e5e5a83e44f5`.
No unaccepted output of either previous S7 run is a premise.

## 1. Three initial mechanisms and the two promoted attempts

**Janossy / Tracy–Widom differential identities.** The starting source is
Shinsuke M. Nishigaki, *Tracy-Widom method for Janossy density and joint
distribution of extremal eigenvalues of random matrices*, arXiv:2109.00790v2,
[primary preprint](https://arxiv.org/abs/2109.00790),
[publisher full text](https://academic.oup.com/ptep/article/2021/11/113A01/6384592).
The source starts with a DISCRETE finite projection model before its continuum
extension; it would be incorrect to dismiss it as exclusively a continuum
paper. Its Janossy/Palm formulas and the transformed integrable kernel were
read, including equations (5)–(8). The differential closure additionally
requires the relevant Christoffel–Darboux functions to satisfy the stated
first-order polynomial-coefficient system. Our Q_n is a compression, not a
finite projection, and arbitrary occupied/empty words introduce arbitrary
binary diagonal fields. A single Janossy determinant therefore does not
supply a uniform bound for the moving-law sum of its logarithm.

Decision: retain and reprove the finite full-word/Janossy identity, but do not
import the differential closure. The exact surviving displacement rank is
proved in PROOF.md §2. The replacement quantitative mechanism is the first
promoted attempt below. This is not a theorem that every Tracy–Widom approach
fails.

**Discrete orthogonal polynomials / Riemann–Hilbert recurrence.** Alexei
Borodin and Dmitriy Boyarchenko, *Distribution of the first particle in
discrete orthogonal polynomial ensembles*, arXiv:math-ph/0204001,
[primary preprint](https://arxiv.org/abs/math-ph/0204001), Theorem 3.1(b),(c).
The affine-grid and polynomial weight-ratio hypotheses, and the consequence
for the Lax-matrix degree, were inspected in the paper. Theorem 3.1's page was
also viewed as a PDF screenshot. An arbitrary binary posterior field does
not preserve a bounded degree in this particular Pearson interface.
OBSTRUCTIONS.md §3 supplies an allowed single-one word and proves the degree
lower bound D>=n-3 (or D+D_0>=n-3 with a fixed-degree base ratio).

Decision: the fixed-degree shortcut is rigorously ruled out, while a
2-by-2 problem with growing poles, Uvarov transformations, a different gauge,
and estimates uniform despite growing degree remain possible. No broad
"Riemann–Hilbert is impossible" conclusion is drawn.

**Conditional orthogonal-polynomial ensembles / averaged characteristic
polynomials.** Alexander I. Bufetov, *Conditional measures of determinantal
point processes*, arXiv:1605.01400,
[primary preprint](https://arxiv.org/abs/1605.01400), Theorems 1.4–1.5; and
Alexander I. Bufetov and Pierre Lazag, *A determinantal point process governed
by an integrable projection kernel is Giambelli compatible*,
arXiv:2111.05606, [primary preprint](https://arxiv.org/abs/2111.05606),
Theorems 1.2 and 1.4. These address integrable projection kernels with their
additional growth/rigidity or division-property assumptions and particular
conditional or regularized characteristic-polynomial observables. The
statements and their hypotheses were read. They do not automatically turn a
noisy, complete-word-dependent inverse or logarithm into one of the permitted
fixed observables. The actual posterior normalizer cannot be removed.

Decision: no averaged characteristic-polynomial identity is imported. The
posterior average is instead controlled directly by conditional variance,
with a finite support extension and a paid boundary. The relation between
these sources and such a direct energy bound remains potentially useful.

### Promoted attempt A: spatial dressing plus actual posterior energy

The prospective bound was frozen at observed UTC 17:16:54; the improved
posterior-energy candidate was frozen at 17:26:19. Both are preserved in
CANDIDATE_FREEZE.md. The exact full-word inverse, bounded phase multipliers,
Fourier interval symmetric differences, and conditional-variance contraction
lead to PROOF.md Theorems A–C. The true posterior normalizer and all four
completions are retained. The boundary is paid by a tent, not by treating Q_n
as a projection. This proves a new absolute curvature remainder, not just an
unbounded resolvent representation. The posterior-mean response and the
matching n/R lower bound are corollaries of this same attempt. The refinement
frozen at 18:38:00 couples two actual outside words given local observations.
AVERAGED_LOCALIZATION.md pays its forced common completion and proves an
O(R/L) observation error, avoiding the small weighted exponent. Its complete
finite enclosure retains all boundary and missing-pair terms. These are
refinements of the same attempt, not a third unrelated research program.

Fast falsification/audit checks: complete-word probabilities versus the latent
channel; every completion's inverse identity; nonzero positive-contraction
variance defect; ordered versus unordered pair factors; and the moving-law
mixed Hessian. These were checked analytically and by the exact finite checks.
The proposed stronger entrywise posterior-energy contraction is false on the
actual three-site sine kernel, as proved in OBSTRUCTIONS.md §2.

### Promoted attempt B: word-uniform weighted inverse and coarsening

The second candidate was frozen together with the first. A critical
1/|i-j| matrix cannot be assigned a standard supercritical inverse-decay
citation without checking its exponent. A direct weighted Schur calculation
instead proves a small exponent alpha=delta/128. QUASILOCALITY.md then pays
for deleting distant observations at the level of conditional TABLES and
produces a fully finite true-law local curvature approximation. This is not
an independent-block ansatz or a value-to-Hessian differentiation.

Fast falsification/audit checks: both weighted row and column estimates;
small/large/comparable distance ranges; arbitrary bad words; the norm of the
Schur-complement inverse; missing and boundary pairs when R exceeds n; and
coarsening probabilities rather than averaging DPP kernels. All are included
in the analytical proof. The slow exponent is explicitly retained in the word-uniform theorem.
The growing alternating-word family of OBSTRUCTIONS.md §4 rules out the
stronger uniform C/r bound and even C(log r)^k/r for fixed k. Its lower-bound
exponent is not claimed sharp. The new averaged O(R/L) coarsening estimate
belongs to attempt A and does not contradict this worst-word obstruction.

## 2. Additional screens and rejected shortcuts

**Inverse-closedness at the critical exponent.** Lukas Köhldorfer and Peter
Balazs, *On the inverse-closedness of operator-valued matrices with polynomial
off-diagonal decay*, arXiv:2501.09603,
[primary text](https://arxiv.org/html/2501.09603v1), Theorem II.12. Its
Jaffard-algebra hypothesis requires decay exponent s>d. The sine estimate
here is at s=d=1, so this theorem is not applied. Fang–Shin–Sun,
arXiv:1909.08409, was also screened at the abstract/discovery level; no theorem
from it is used. The small-exponent proof in QUASILOCALITY.md is self-contained.

**de Branges / weighted Paley–Wiener dressing.** Philippe Poulin and Simon
Cowell, *de Branges spaces with bi-Lipschitz phase for large distances*,
arXiv:1306.6199, [primary preprint](https://arxiv.org/abs/1306.6199).
The introduction and Theorem 1.1 were inspected. Norm equivalence to a
Paley–Wiener-type space and a large-distance phase condition do not, without
an additional quantitative argument, give the word-uniform dressed endpoint
bounds needed for a 1/r inverse kernel estimate. Lyubarskii–Seip's *Weighted
Paley-Wiener spaces*, DOI 10.1090/S0894-0347-02-00397-1, was located, but the
publisher PDF fetch was denied; it is not listed as a fully read proof.
Lubinsky's de Branges universality paper, DOI 10.1016/j.jfa.2009.02.021, was
screened at its primary abstract. No published theorem is claimed disproved.
However, the desired extension to a C/r bound uniform over ALL finite output
words is now explicitly refuted by OBSTRUCTIONS.md §4. Weaker-power,
probability-weighted, or suitably restricted bulk statements remain possible.
The principal averaged coarsening estimate no longer needs this extension.

**Entropy continuity from local/tight convergence.** András Mészáros,
*Limiting entropy of determinantal processes*, arXiv:1905.11459,
[primary preprint](https://arxiv.org/abs/1905.11459), Theorem 2.4 and §5,
Theorem 5.1. The projection/tightness hypotheses and the extension through
positive-contraction projection dilations were inspected. These are entropy
VALUE results; they do not directly supply the mixed-curvature tail here.
Russell Lyons and Jeffrey E. Steif, *Stationary determinantal processes:
phase multiplicity, Bernoullicity, entropy, and domination*,
arXiv:math/0204324, [primary preprint](https://arxiv.org/abs/math/0204324),
§6, likewise provides valuable entropy context and continuity, not the
particular all-contrast spatial Hessian estimate used in this packet.

**General entropy and negative-dependence tools.** Eldan–Shamir,
arXiv:2007.13108, Theorem 5, was inspected as an entropy-value route through
tilts/covariance; it is not a sign theorem for our changing channel. The
Shepp–Olkin work of Hillion–Johnson, arXiv:1503.01570, concerns entropy of
Bernoulli SUMS, not the labelled word distribution. Alishahi–Barzegar,
arXiv:2006.13923, was screened as an entropy lower-bound result, not a
curvature theorem. Cossette and coauthors, arXiv:2504.17679, was screened at
the primary abstract for extremal strong-Rayleigh entropy, not adopted as a
channel-shift result. General log-concavity/Markov-chain search results did
not provide the missing signed operator inequality; no inference of absence
from the literature is made.

**Modified log-Sobolev / stochastic-covering tools.** Jonathan Hermon and
Justin Salez, *Modified log-Sobolev inequalities for strong-Rayleigh measures*,
arXiv:1902.02775v2, [primary preprint](https://arxiv.org/abs/1902.02775),
Theorems 2–3, was read, including screenshots of the theorem pages. Theorem 2
provides a suitable normalized flip-swap chain under stochastic covering; it
does not automatically give the same constant for a specified flip-only
Glauber chain. Theorem 3 depends on the stated lower bounds for the generator
rates, including swap-neighbor pairs. A flip-only chain can have zero rates
on such pairs. Neither a dimension-free approximate-tensorization constant
for an arbitrary chosen chain nor the common-shift curvature sign is imported.
This was considered for averaging distant observations. The direct
conditional coupling in AVERAGED_LOCALIZATION.md supplies that average without
a log-Sobolev premise. No claim that such inequalities are generally irrelevant
is made.

**Recent free-fermion Shannon/Rényi and stabilizer results.** The official
arXiv record of 2509.10700v4 (updated 28 August 2026), *Equivalence of Stabilizer
and Shannon Rényi Entropies: Exact Results for Quantum Critical Chains*, was
checked. Its pure-state/doubled-system Rényi observable is not our mixed noisy
Shannon curvature. For Khasseh–Rajabpour, *Hidden Conformal Boundary Data in
Finite-Temperature Stabilizer Entropy*, arXiv:2606.08606,
[primary HTML](https://arxiv.org/html/2606.08606v1), equations (3) and (9) and
their surrounding hypotheses were read: the Pauli-spectrum/all-square-minor
sum at a particular index is not the complete-configuration Shannon sum.
The ground-state quadratic-chain result DOI 10.1103/PhysRevB.105.245109 was
screened at the primary abstract; its logarithmic finite-size correction is
not an extensive mixed-state Hessian. None is used as a hidden entropy
substitution or a replica continuation.

**Midpoint involution/Ward and log-determinant loop expansion.** Direct
algebra at a=(1-c)/2 gives A=(J+c(2P-I))/2 for a finite projection P. The
resulting midpoint Fisher/count-score identities overlap the reviewed
`proofs/stationary-midpoint-fisher-route.md`; they were not promoted as new
results. A convergent log-determinant/Boolean-moment expansion on strict
strips also overlaps reviewed S6's bounded-degree response mechanism. It
provides regularity but no proved all-order sign, so it was not relabelled
as a new solution.

**Reflection and pairwise signs.** Swapping the two conditional coordinates
leaves g unchanged. Reflection therefore does not cancel a positive pair
term merely by exchanging its coordinates. The exact six-site sine witness
in OBSTRUCTIONS.md §1 disproves the stronger averaged-pair nonpositivity
shortcut, while retaining a negative total Hessian at that same point.
The total near-field compensation remains open.

## 3. Reading and verification limits

The cited primary theorem hypotheses were checked in full text where so
stated; entries explicitly marked abstract/discovery-only are not theorem
inputs. PDF screenshot calls were made when reading PDF pages. Some arXiv
PDF renderings returned cache-miss errors; those failures were not treated
as successful visual inspection. Successful screenshots included the
Borodin–Boyarchenko theorem page and the Bufetov conditional-measure opening
pages; Nishigaki's formula reading used the publisher HTML when the PDF
rendering failed. No claim of a complete literature survey, global novelty,
or independent review follows from these searches.
