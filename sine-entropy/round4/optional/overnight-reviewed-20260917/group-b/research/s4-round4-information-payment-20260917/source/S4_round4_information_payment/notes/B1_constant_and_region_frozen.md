# B1: explicit constant / region freeze (before full proof and regression)

Let e_u=c/[g_0(u)g_1(u)], C_Y=Cov(X|Y), and Psi=E sum_i e_(Y_i)^2 (C_Y)_ii. Define D=(n-TrK)/[a(1-a)]+TrK/[(a+c)(1-a-c)].

Promoted candidate B1, explicit strengthened target:
If 0<c<=sqrt(23/25) and 0<a<1-c, then for every Hermitian contraction DPP,
  0 <= I(X;Y_a)'' <= 2 Psi <= 2[D - sum_i 1/((a+c K_ii)(1-a-c K_ii))].
For Gaussian Z_t=tX+B_t at any deterministic T, J_T=I(Y;Z_[0,T]) satisfies
  J_T'' <= I(X;Y)'',
and the remaining correction has a rank/time bound
  0 <= I(X;Y)''-J_T'' <= (2c^2/tau_min^2) min(V(K), (sqrt(n V(K))/2) exp(-T/8)).
Here tau_min=min(a(a+c),(1-a)(1-a-c)). No sign for J_T'' or its time derivative is asserted.

Proof route to test: exact unnormalized pair acceleration is a positive log-odds sum; signed missing Fisher is diagonal covariance minus twice weighted edges; a scalar four-cell inequality log odds <= 2 d sum(1/p) when p00+p11>=1/25 permits their combination before discarding terms. The channel enforces p00+p11 >=(1-c^2)/2. Exact DPP tilt covariance rebases all pairs to one compatible posterior.

Proposed new regional consequence: for 37/40<=c<=959/1000, d=(1-c)/4, a in [d,3d], and r=TrK/n in [0,1/100] or [99/100,1],
  H(DPP(aI+cK))'' <= -(11/250)n.
Reason for these constants: c/[d(1-d)]<=95; a(1-a)/[(a+c)(1-a-c)]<=3; hence D/n times (a+cr)(1-a-cr) <=(1+2r)(1+95r)<=1989/1000, giving -11/250 after using the output marginal variance <=1/4. Complementation supplies the high-density case.

This is a new candidate, not an assumed theorem. It changes neither the full target nor the unavailable endpoint/ordinary-density gates. The all-time correction is not the old delta^-5 local-Q theorem under a new name: it works on a completed information functional and uses the retained Fisher off-diagonal term and log-odds acceleration.
