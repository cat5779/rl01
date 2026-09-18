# Interim separate-review findings

These are progress findings from the two existing sidebar Sol tasks, not final source certification. Their standalone reports/PRs are still being prepared.

## S43 cycle03
The reviewer reports that the actual-weight sign mass M_b, radial KL constant D_c, third logdet difference estimates and central evidence flatness can be independently completed. However, the exported source stops before the count-Stein derivation of A_c and L_c. The negative envelope and -W_n=Theta(n) remain CONDITIONAL / NOT CERTIFIED until that missing load-bearing argument is supplied or reconstructed.

## S42 cycle03
- The stated shrinking-chord scale gives O(eta^2), not o(eta^2); an additional diverging scale factor is needed for little-o, both for interior and endpoint tails.
- The displayed M12 threshold 1.99717043204465e-6 rounds downward from 1.997170432044650508...e-6. A strictly sufficient decimal threshold should be rounded upward, e.g. 1.997170432044651e-6, or kept symbolically. The displayed M13 threshold rounds in a safe direction.
- The reviewer independently reconstructed the first finite chord using Arb over the 6- and 12-site full atom laws:
  Delta_eta J6 = 0.0027861191230098624466234... with a reported interval radius below 2.27e-72.
  Its contribution divided by 12 is 0.000232176593584155203885...
  This pays only the first retained scale. It does not pay the remaining 11 or 12 scales, nor establish an entropy-rate chord.

The new cycle04 prompts already retain the conditional status, correct the little-o issue, and ask for new research rather than another finite-condition restatement.

## S47 cycle04 — separate Sol confirmation
Equation (4) is DISPROVED: it contains an extra E_P[s_Q^2]. The correct identity is E_P[u_P log(P/Q)+(s_P-s_Q)^2-u_Q], matching equation (5). Setting P=Q gives zero in the correct identity but positive Fisher information in the author's equation (4) for a nontrivial family. The finite-volume triangular chord formula survives after correction. No finiteness or vanishing of E_tail was proved, so an infinite E_tail yields only a vacuous lower bound. The reviewer finds no new usable true-sine tail constraint and recommends no PRO renewal for this reformulation. The standalone review is being prepared.
