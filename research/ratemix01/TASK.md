# Derivation task: a DPP-compatible obstruction to finite mean local mixtures

Prove or refute the three explicit claims below. This task concerns the boundary of a finite mean local-dependency hypothesis; it does not ask for a general process-existence theorem.

## Frozen data

Let Gamma=F_2=<a,b> be the free group, with regular left translation. Write e for its identity, E={0,1}^Gamma, x^{g,+} for setting coordinate g to 1, and p(t)=1/4+t/4 on [0,1]. Let mu_t be the product Ber(p(t)) law; equivalently it is the uniformly gapped DPP of K_t=p(t)I.

For n>=1 put

    W_n={b^m: 2^n-1 <= m <= 2^{n+1}-2},
    c_n=2^{-n-6},
    F_{n,g}(x)=product_{w in W_n} x_{gw},
    q(t)=p'(t)/(1-p(t))=1/[4(1-p(t))].

Define the candidate covariant pure-birth rates

    A_g(t,x)=(1-x_g)[ q(t)
        + sum_{n>=1} c_n { (p(t)-x_{ga})F_{n,g}(x)
                        -(p(t)-x_{ga^{-1}})F_{n,ga^{-1}}(x) } ].

No claim about these formulas may be accepted merely from their appearance. Check them.

## Claims to prove or refute

1. A is jointly Borel, covariant, uniformly bounded, nonnegative, vanishes at occupied sites, and is spatially continuous for every t, uniformly in t.
2. For every bounded cylinder f and all t in [0,1], the exact continuity equation holds:

       mu_t(f)-mu_0(f)
       = integral_0^t mu_s(sum_g A_g(s,x)[f(x^{g,+})-f(x)]) ds.

   The sum is over the finite support of f. The complete justification must cover the countably many translated perturbations and justify every interchange. One possible route is a signed Boolean-square circulation on the pair (g,ga), conditional on its exterior, but the identity itself must be proved.
3. For each fixed t, there exists no representation of A_e(t,.) of the form

       A_e(t,x)=sum_k lambda_k B_k(x|V_k),

   where V_k is finite, e in V_k, lambda_k>=0, 0<=B_k<=1, and sum_k lambda_k|V_k|<infinity. Allow arbitrary countably many V_k and B_k; do not merely show that the displayed W_n representation has infinite dependency cost. Suggested diagnostic: coordinate oscillation osc_j(A_e)=sup{|A_e(x)-A_e(y)|: x_l=y_l for all l!=j} and the sum over j.

## Acceptance and usefulness

A valid affirmative answer supplies all three complete proofs with exact constants or stated finite bounds and no hidden generic configuration assumptions. A negative answer supplies a specific failed claim and a valid countercalculation. Nonexistence of this mixture must not be called nonexistence of a strong or invariant weak process: those conclusions are outside the task.

If the three claims hold, this gives a bounded continuous exact-DPP rate field excluded by the finite mean local-dependency hypothesis, so that sufficient condition cannot be mistaken for a theorem for all bounded DPP rates. It does not disprove the general invariant weak-existence question and does not enlarge the endpoint DPP kernel family beyond the diagonal path.

## Deliverable

Add `research/ratemix01/RESULT.md` to this branch, preserving this frozen task. Begin with `PROVED`, `DISPROVED`, or `INCOMPLETE`. Give a self-contained derivation, exact scope, and any genuine failure. Do not infer a general nonexistence result from failure of the mixture representation.
