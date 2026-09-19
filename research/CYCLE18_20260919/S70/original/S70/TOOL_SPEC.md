# Required interface before construction

This S70 tool must (1) operate on the full, actual, strictly positive spatial
configuration law of the finite compression; (2) bound the second derivative
in the common diagonal shift a at each fixed c, not a derivative along a
parameter path; (3) preserve normalization and all configurations when c and
p vary; (4) keep the extensive Fisher budget and the missing-window boundary
explicit; (5) provide a positive quantitative excess of the stationary local
variational payment over (C-1)d on a closed parameter rectangle.

The proposed construction has two independent reusable parts.

* Block PSD allocation: guarded pair improvements are distributed as
  off-diagonal entries of a positive semidefinite block matrix, with a
  pointwise diagonal budget C at every site. Pair coefficients may be split
  between overlapping blocks. Each block matrix is measurable outside all
  its target bits, so weighted mixed-score identities and conditional-score
  Jensen remain valid. Its fixed variational test is integrated against the
  moving actual law.
* Exact tensor channel transport: at a fixed reference law, use the two local
  generators D=[[-1,-1],[1,1]] and F=[[1,-1],[-1,1]]/2. The moving law is
  product_i(I+s D_i+v F_i) p_reference, where s=(1-c)(p-1/2) and
  v=(c-19/20)/(19/20). Contrast is not nilpotent. This representation supplies
  exact mixed derivatives, scaled polynomial coefficients, normalization,
  and a whole-vector truncation bound.

The finite certificate must additionally verify posterior Gram/Loewner
bounds using mixed parameter corners, every guard word, global and guarded
pair caps, strict block PSD slack, fixed-test sup norms, all 2^22 reference
probabilities, and a continuum (not just mesh) lower bound for payment.

No numerical exploration below is a premise until enclosed by the terminating
outward-interval/exact-rational verifiers.

## Proved relaxation used by the final four-site construction

The original proposal required every block matrix to be measurable outside
all its targets. That restriction is unnecessary. What is required is:
B_ij is independent of bits i and j for i != j; B is measurable in its
entire local window; the diagonal allocations obey the pointwise budget;
and B is PSD for every complete local word. The mixed-score identity is
applied entry by entry before Jensen, and Jensen is conditional on the whole
window, including its target bits. Thus pair guards may retain other target
bits. With constant diagonals, each row is independent of its own target
bit, so the potential still factors into diagonal and pair-cross terms.

This relaxation is proved in the result, not inferred from numerical tests.
The final witness uses four targets 9,10,11,12 and position weights
19/60,11/60,11/60,19/60 times C. Pair improvements at separations 1,2,3 are
split among respectively 3,2,1 translated blocks. This preserves the exact
per-site diagonal and per-edge improvement budgets.
