# S77 — Cycle27 mathematical research

## Research here; no Work routing

You must NOT attempt to route, redirect, hand off, or instruct the user to use Work, another task/chat, or another agent. This is mathematical derivation in THIS chat. A checkout or external execution environment is not a prerequisite. If access/export fails, use these explicit objects and deliver readable complete mathematics in chat.

Think for at least 120 minutes, unless you achieve major progress earlier. Do not invent elapsed time or idle to fill it. Major progress requires a proved reusable tool, a decisive model-valid obstruction with a useful replacement, or a closed theorem; a survey, renamed remainder or favorable numerical samples is insufficient.

Frozen original target: Q_rho(i,i)=rho, Q_rho(i,j)=sin(pi*rho*(i-j))/(pi*(i-j)); K_N=aI+cQ_rho,N, 0<rho,c<1, 0<a<1-c. Q_N is a true finite compression, a contraction generally NOT a projection. H_N is full configuration Shannon entropy in nats, h=lim H_N/N. The goal is h concave in a for every fixed rho,c and all legal a, particularly the entire c in(37/40,1). Derivatives hold rho,c fixed. On a compact legal interval J set delta=min_(a in J) min(a,1-a-c)>0. Constants need not be uniform at c=1, but their dependence and proved coverage must be explicit. A narrow parameter region or midpoint theorem is not completion of the global target.

Construct a TOOL with explicit input, hypotheses, output inequality, falsification tests and a quantitative interface back to ORIGINAL Shannon entropy. Theory and transferable mechanisms from other fields are central; check original-source hypotheses. Do not add hidden assumptions, discard rare words, replace actual weights by independent substitutes, differentiate o(N) entropy-value errors, or substitute count/spectral entropy. A useful intermediate theorem is welcome if its remaining gap is honestly stated. Label new lemmas KNOWN/PROVED/OPEN/EQUIVALENT_BLOCKER. Do not present an equivalent reformulation as a solved weaker lemma.

Return English RESULT.md or full in-chat proof with PROVED/DISPROVED/INCOMPLETE separated, exact scope and remaining payment. Computational claims need reproducible source and actual execution status; finite diagnostics are not all-size proofs. No hash/SHA/checksum acceptance gate, no delegation, shared-state edits or PR merges.

## S77 ownership: Fisher-compensated cut estimate after S74

S76 is already working on the cyclic exterior-channel overlap budget. S78 owns lifting S75 stars to multiple centers. Your task is the ACTUAL TOEPLITZ block-information route, using audited S74 (RL01 PR64) and S71 (PR60), not either neighboring task.

For adjacent A,B put M=H_A+H_B-H_AB, F_N=-H_N''. For P=P_K(y), R_y=(K-diag(1-y))^-1, S=tr R_y and ell=log(P/(P_A P_B)),
M''=D_F+C_acc,
D_F=E S^2-E(E[S|Y_A])^2-E(E[S|Y_B])^2>=0,
C_acc=E[((tr R)^2-tr(R^2))*ell].
The Fisher inequality is accepted via score monotonicity and DPP negative association. The acceleration is NOT nonnegative: for a two-site equal-marginal law with marginal u=a+c*rho, d=|K_12|^2 and r=u(1-u)+d, C_acc=2log(1-d/r^2)<0. PR63's945-model diagnostic found negative C_acc but positive M'' throughout; max(-C_acc/D_F) about.683214 is NOT a universal theorem.

S74 supplies a new accepted representation and size-free cut bound. For sigma_i=2y_i-1 and b_i=sigma_i R_ii-1,
W(K,y)=sum_(i<j) sigma_i sigma_j log[1-sigma_i sigma_j |R_ij|^2/(b_i b_j)],
C_acc=2 E_P[W(K,Y)-W(K_A directsum K_B,Y)].
For every strict Hermitian contraction along the common scalar shift,
|C_acc|<=B_delta ||K_AB||_HS^2,
B_delta=4L_delta/delta^3+2/(r_delta^4 delta^4)<=6delta^-12,
r_delta=delta/(1-delta),
L_delta=2/(r_delta^2 delta)+1/(r_delta^5 delta^2)+1/(r_delta^6 delta^3).
The proof uses the actual kernel interpolation K_t=diag(K_A,K_B)+t offdiag(K_AB), not a probability mixture. It preserves delta by sign conjugation/pinching. The complete proof is attached.

Its exact accumulated charge is important: for q leaves of length L,
sum_merges ||K_AB||_HS^2=(c^2/2)[tr Q_(qL)^2-q tr Q_L^2].
Writing D_rho,L=tr(Q_L-Q_L^2), a seed F_L>=f_L throughout J gives a rate chord bound with curvature margin
kappa_L=f_L/L-B_delta*c^2*D_rho,L/(2L).
This follows by integrating finite-volume curvature then taking entropy-value limits, with no derivative-limit shortcut. D_rho,L=O(log L). Merely increasing L without controlling f_L is not a certificate.

At rho=.5,c=.95,J=[.02,.03], B_delta about8.65e20 makes the two-site margin about-5.81e19. The theorem is valid but presently pays only extreme densities, e.g.min(rho,1-rho)<=1e-21 on c[.925,.95],a[.02,.03]. A small numerical constant improvement would not change this bottleneck.

## New obligation

Build a relative or signed cut inequality that RETAINS D_F while estimating C_acc, rather than taking a wordwise absolute gradient and discarding all Fisher compensation. One candidate output is
D_F+C_acc >= -B_eff(c,rho,J) ||K_AB||_HS^2
with an affordable B_eff derived from actual weights; another is
-C_acc <= theta D_F + E_cut,
with theta<=1 and a rigorously affordable accumulated E_cut. These are candidates to prove or refute, not premises. A sharper exact decomposition into locally paid Fisher/odds terms is welcome. State which lemma is strictly weaker than full M''>=0 and how its residual sums through the ACCEPTED merge-tree formula.

Promising seeds include a weighted cofactor integration-by-parts pairing between the cut odds change and conditional-score variance; a variational projection/Dirichlet representation that pays the negative log-odds term before bounding gradients; or a scale-dependent cut interpolation with signed relative entropy derivatives. Exploit actual sine geometry if a general-contraction claim is false. Do not restart S74's absolute-norm proof with only cosmetically improved constants.

Known obstruction at the genuine six-site sine base point rho=.5,c=.95,a=.025,A=1:3,B=4:6: the mixed diagonal Hessian entry for sites1 and6 is negative (about-.000379092), while D_F about32.59075, C_acc about-18.84098 and M'' about13.74977. Thus entrywise positivity of all coordinate rectangle defects is false; full-direction compensation remains possible. The author's exact interval attachments have now arrived and are undergoing independent replay; the analytic theorem is already audited. Do not depend on un-replayed last decimal digits.

Success requires a genuinely improved structural payment with explicit parameter/size costs and a tested path to a non-extreme-density rate certificate, or a decisive obstruction to the proposed relative inequality plus a useful narrower replacement. If a new bound still cannot pay even the audited seed, show the remaining deficit; do not claim closure. Do not infer rate nonconcavity from failure of this sufficient method.
