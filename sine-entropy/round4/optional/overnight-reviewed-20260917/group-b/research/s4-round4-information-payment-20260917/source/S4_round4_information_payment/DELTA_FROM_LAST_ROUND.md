# Delta from the latest result in this conversation

## Provenance before novelty

The mandatory packet was read at commit **c307fe1bcf46b56e4755655c90f60a681979bf13**. Its reviewed S4 baseline is the earlier four-site block-product obstruction to tangent-only localization closures. It does **not** independently review the most recent round-3 MMSE payment theorem in this conversation. That theorem is therefore treated here as a preceding **author claim**, with its exact claim restated below, not an imported reviewed proof premise.

The user's conversation contains the two prior ZIPs. The most recent mounted ZIP was inspected only to understand the exact previous claim and to reuse elementary rational-computation infrastructure. Its proof is not a dependency of the present theorem. The old counterexample proofs and runtimes are not credited as round-4 progress.

## Exact previous author claim

Let X~DPP(K), 0<=K<=I_n, Pr(Y_i=1|X)=a+cX_i, and delta=min(a,1-a-c)>0. Let Z_t=tX+B_t with standard independent Brownian motion, F_t its observation sigma-field, J_T=I(Y_a;F_T), and

    M_t(a)=E Tr Cov(X|Y_a,F_t).

The preceding author theorem asserted

    J_T'' <= (5/4) delta^-5 integral_0^T M_t(a) dt
           = (5/2) delta^-5 I(X;F_T|Y_a),

and hence

    J_T'' <= (5/4)delta^-5 min{T V(K),2H(X|Y_a)},
    V(K)=sum_i K_ii(1-K_ii).

Its completed-information consequence asserted

    H(DPP(aI+cK))'' <= B_K''+(5/2)delta^-5 H(X|Y_a),
    B_K=(n-TrK)b(a)+TrK b(a+c).

A sufficient regional criterion was

    b(TrK/n) <= d^5/[5c(1-c)]

on a in [d,1-c-d], giving curvature <=-n/[2c(1-c)]. The displayed high-contrast example was c=19/20, d=1/80, rho=10^-11 or 1-10^-11. All of these are prior author claims, not this round's results or assumed premises.

That route paid the positive acceleration rather than deleting it, but used a very expensive local-in-time unnormalized-likelihood bound. The delta^-5 cost left ordinary densities and almost all of the useful fixed-density region unpaid.

## Reviewed obstruction retained as a regression gate

For the direct sum of m copies of P_(4,2), at c=19/20 and a=1/40, the reviewed Gaussian information excess is positive for the stated small time interval even though every normalized-posterior common-offset tangent vanishes and total configuration-entropy curvature is negative. Its sparse occupied-pinning counterpart has a positive extensive slack curvature. These are not sine-target counterexamples and not contiguous P_(4m,2m). We neither re-prove nor tensorize them for credit.

## New unpaid estimate chosen at the start of this round

Find a payment for the **completed information correction**, rather than differentiating a fixed-function entropy contraction or paying the instantaneous Q_t'' with a worst-case delta^-5 bound. The candidate required an explicitly estimable weighted posterior uncertainty, compatible output averaging, an improved interior noise cost, and a nontrivial fixed-density region beyond the last example.

The crucial new term is

    Psi=E_Y sum_i [c/(g_0(Y_i)g_1(Y_i))]^2 Var(X_i|Y).

It is different from the tangent energy E_Y Var(sum_i e_(Y_i) X_i |Y). At the homogeneous midpoint the latter is zero by cancellation, while Psi is generally nonzero. Its off-diagonal subtraction is retained exactly.

## What round 4 proves beyond that claim

1. The exact acceleration becomes an actual-average conditional output log-odds sum. A scalar logarithmic-mean estimate and exact two-site Bayes rebasing pay it jointly with the off-diagonal missing Fisher term, giving

       0 <= I(X;Y_a)'' <= kappa Psi <= kappa(D-F_marg).

   This is derived independently from full channel likelihoods. In particular I''<=kappa delta^-2 MMSE(X|Y), with a channel-only bounded kappa at fixed c; along proportional-offset c->1 intervals one may take kappa=O(log(1/delta)). No sharper bound for the instantaneous Q_t'' is asserted.

2. Gaussian conditional information is nonnegative in a-curvature and has an explicit exponentially decaying rank/time payment. At T_n=16log n, its **truncation remainder** has an O(n^-1) unnormalized Hessian/Jensen bound on compact interior offset intervals. This is not mislabeled as the full target defect.

3. An explicit scalar Fisher budget gives H''<=-(11/250)n for densities <=1/100 or >=99/100, contrasts [37/40,959/1000], and the central half of the legal offset interval. It applies to the actual Q_n for every n and gives a new sine-rate Jensen theorem. For c=.95,d=1/80, the old criterion's right side is 1/(19*80^4), whereas b(.01)>=2(.01)(.99)=99/5000; an exact certificate verifies the strict separation. The new one-percent example is therefore not covered by the preceding displayed criterion.

The regional theorem does not contain every tiny-density parameter of the previous author theorem: in particular it does not extend the explicit uniform negative budget to all c<1. Its gain is a substantially larger specified density region and a new completed-information/rank-time estimate.

## Not new, and not claimed

Gaussian I-MMSE conventions, the supplied channel representation, DPP definitions, elementary rational likelihood jets, the old four-site counterexample, and LF/CRLF replay repairs are infrastructure or prior material. No independent review of this package has occurred. There is no claim of literature exhaustion or universal novelty beyond the supplied project baseline.
