# Self-contained assumptions and frozen target

All logarithms are natural and \(0\log0=0\).  For a Hermitian contraction \(0\le K\le I\), \(H(K)\) denotes the entropy of the complete DPP configuration law, not the entropy of its count and not \(\operatorname{Tr}b(K)\).

The frozen target concerns

\[
K_n(a)=aI_n+cQ_n,
\qquad 0\le a\le1-c,
\]

where \(Q_n\) is the Toeplitz principal block of the interval projection with density \(\rho\), and asks for concavity of the limiting complete-configuration entropy rate for fixed \(0<\rho<1\) and fixed \(37/40<c<1\).

For a rank-\(k\) projection input with law \(\mu\) on \(k\)-subsets, the actual output atom is

\[
\begin{aligned}
p_a(S)=\sum_{|A|=k}\mu(A)&(a+c)^{|S\cap A|}
(1-a-c)^{k-|S\cap A|}\\
&\times a^{|S|-|S\cap A|}
(1-a)^{n-k-|S|+|S\cap A|}.
\end{aligned}
\]

The output count law is

\[
M\sim\operatorname{Bin}(k,a+c)+\operatorname{Bin}(n-k,a),
\]

independent of the spatial input law.  With \(\nu_l=p_a(\cdot\mid M=l)\), \(u_l\) uniform on the \(l\)-subsets, and

\[
F_l=D(\nu_l\|u_l),
\qquad
\Phi=H(M)+\sum_l\pi_l\log\binom nl,
\]

one has

\[
H=\Phi-\sum_l\pi_lF_l.
\]

For an interior shift,

\[
H''=-\sum_Sp_a''(S)\log p_a(S)-\sum_S\frac{p_a'(S)^2}{p_a(S)}.
\]

The new theorem in `proof.md` specializes to \(n=2m,k=m,a=(1-c)/2\).  It does not assume differentiability of the limiting entropy rate and does not differentiate any value approximation.
