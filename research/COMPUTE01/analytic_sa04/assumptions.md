# Assumptions and fixed conventions

- `n=2k>=4`, `c=19/20`, `a*=1/40`.
- `P` is the rank-`k` projection onto the first `k` Fourier modes of the
  `n`-cycle; the latent `k`-set has projection-DPP law `det P_A`.
- `G_l=sum_{i<j}(T_ij-I)` is the unnormalised exchange generator.
- `s_l=-log(theta_l)/(2(n-1))`; no alternative clock is allowed.
- `F_l(s)=D(q_l^max exp(sG_l)||u_l)` and `h(l)=F_l(s_l)`.
- `A_l=F_l(s_l)-F_{l-1}(s_l)` and
  `E_l=F_{l-1}(s_{l-1})-F_{l-1}(s_l)`.
- All logarithms are natural.  Total variation is
  `TV(P,Q)=sup_A |P(A)-Q(A)|`.
- Finite numerical observations may falsify or select a route but do not prove
  the growing-`n` statement.

