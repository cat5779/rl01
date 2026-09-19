# QWE09 ROUND2 — concavity attack checkpoint

Date: 2026-09-19. Repository: randomcat4/dpp-stationary-entropy, PR131.

## Findings first

1. **The target concavity question is still open, but several tempting stronger routes have now been falsified.** No new entropy-rate concavity theorem is claimed in this checkpoint.

2. **Actual-model zero-payment Jensen remains false.** The first-round strict six-site true sine-Toeplitz certificate at `rho=1/2, c=19/20, a=1/40` gives:

   - `Delta_Phi in [-0.106585307859143407, -0.106585307859143406]`
   - `Delta_Chi in [-0.096395465271827624, -0.096395465271827623]`
   - quadratic variation `Q in [0.170309619791317635, 0.170309619791317636]`

   Hence a one-step payment coefficient for the complete potential must exceed about `0.6258326` on this word. This is a counterexample to uncharged conditional Jensen, not to entropy concavity.

3. **Wordwise negativity is false in the true Toeplitz model.** In direct true half-density sine-Toeplitz finite probes, every tested pointwise complete-potential value remained nonnegative through `n=11`, but at `n=12` the minimum was approximately `-6.3854`, with 14 negative output words. Larger tested volumes produced more negative words. Therefore a proof that requires every output word to have the favorable sign cannot establish the target.

4. **Pairwise mixed-curvature negativity is false for general bipartite projection/contraction models.** A random bipartite projection/contraction probe produced a positive individual even-odd pair contribution of approximately `0.157821`. Therefore the target cannot be reduced to proving every even-odd pair contribution is separately nonpositive in the ambient contraction class.

5. **The aggregate mixed direction remains numerically promising.** In 320 random bipartite projection/contraction Hessian probes, the common curvature direction stayed negative in the tested samples, while the largest aggregate mixed-parity Hessian encountered was only at numerical-zero scale (about `1e-14`). This is diagnostic evidence only; it is not a sign theorem.

6. **The first-round transfer mechanism has not yet shown a fatal contradiction in the second-round audit, but its constants are too loose to certify `c=.95, a in [.02,.03]`.** The load-bearing items still deserving independent proof audit are the dimension-independent Hessian summation, the observation-domain compensation, and the effective all-exterior rate.

7. **The most plausible next structural target is aggregate parity compensation, not pointwise or pairwise sign.** The route now being pursued is a bound on the full even-odd mixed curvature (or an equivalent parity-conditioned ensemble quantity) that uses the joint bipartite geometry and retains the conditional-information remainder.

## What the probes rule out

### A. No wordwise sign proof

A sufficient statement of the form

`Phi(G_y) >= 0 for every actual output word y`

is incompatible with the true Toeplitz finite model. The `n=12` negative words appear in the actual model, not in an arbitrary table relaxation.

This does **not** imply `E Phi(G_Y) < 0` or failure of entropy concavity. It only removes a stronger pointwise mechanism.

### B. No universal pair-by-pair mixed sign in the ambient bipartite class

A statement of the form

`each even-odd pair contribution <= 0`

fails for general random bipartite projections/contractions. Positive individual pairs can coexist with a favorable aggregate mixed Hessian.

Thus any successful proof must permit compensation between pairs, between words, or through a matrix/ensemble inequality.

### C. No free conditional Jensen

The rigorous six-site example already shows that the complete log-curvature potential can decrease after revealing an additional coordinate. A valid martingale/Bellman route must pay this decrease by a quadratic-variation or Fisher-type term. The first-round manuscript uses such a payment; the second round is testing whether the remaining mixed term can be controlled sharply enough for the target interval.

## Current structural decomposition being attacked

At half density, define the two-shift entropy

`H_n(s,t) = H(DPP(c Q_n + s P_E + t P_O)).`

Along the common shift `s=t=a`,

`H_n''(a) = H_ss(a,a) + 2 H_st(a,a) + H_tt(a,a).`

The accepted contrast-`37/40` finite-contraction baseline pays the two pure parity directions after the observed-parity conditioning rewrite. The remaining obstruction is therefore quantitative control of the aggregate mixed term `H_st(a,a)`, equivalently the full even-odd part of the complete curvature potential under the actual law.

The second-round probes indicate that the needed statement, if true, is likely an **aggregate** bipartite inequality. Both stronger candidates have been falsified:

- every actual word has favorable sign;
- every even-odd pair has favorable sign.

## Candidate proof interfaces

1. **Bipartite matrix inequality.** Seek a bound on the complete mixed log-curvature potential as a single function of the cross block, rather than a sum of independently signed pairs.

2. **Conditional-expectation geometry.** Use the actual inverse-score matrix martingale to compare coarse and fine parity observations, but retain the necessary quadratic payment demonstrated by the six-site counterexample.

3. **Parity-conditioned contraction representation.** For finite Toeplitz windows, use the correct positive contraction

   `B_x = I/2 + (1/2) U* diag(1-2x) U`

   with `U` merely contractive. Do not replace it by a projection. The exact unitary/projection representation belongs only to the full infinite projection or matching finite cyclic projection.

4. **Combined conditional-information accounting.** Work with

   `H(Y_O | Y_E) = E_{X_E} H(Y_O | X_E) + I(X_E ; Y_O | Y_E)`

   so the information remainder is differentiated together with the ensemble term. No separate concavity of the information term is assumed.

## Numerical status and scope

The random projection/contraction tests and the `n=12` wordwise test were exploratory finite computations. They are useful falsification evidence but are **not** interval certificates, all-`n` theorems, or entropy-rate statements.

The current runtime no longer retains the temporary round-2 probe scripts from the interrupted session, so this checkpoint records the recoverable outputs and their logical role only. The strict six-site Jensen obstruction remains reproducible from the committed first-round certificate code.

## Current verdict

**DISPROVED:** wordwise favorable sign as a universal true-Toeplitz proof mechanism; pairwise favorable mixed sign in the general bipartite projection/contraction class; zero-payment conditional Jensen for the complete potential.

**SUPPORTED ONLY NUMERICALLY:** favorable sign of the aggregate mixed direction across the tested bipartite ensembles.

**INCOMPLETE:** strict entropy-rate concavity for `rho=1/2, c=19/20, a in [1/50,3/100]`.

The next load-bearing goal is a proved aggregate parity-mixed curvature inequality with explicit slack large enough to combine with the pure-parity baseline and the finite-to-true response transfer.
