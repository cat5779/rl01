# Frozen sine entropy-rate target


All logarithms are natural, with `0 log 0=0`. Let `b(x)=-x log x-(1-x)log(1-x)`.
For a Hermitian contraction `0<=K<=I` on n labelled sites, `DPP(K)` is the
binary law with `Pr(A subset X)=det K_A`. Its full atom for occupied set S is
`p_K(S)=sum_{B subset [n]\S} (-1)^|B| det K_{S union B}`,
where the empty determinant is 1. Define `H(K)=-sum_S p_K(S)log p_K(S)`.
Do not replace this by entropy of `|X|` or by `Tr b(K)`.

Fix `0<rho<1` and the centered interval `E_rho=[-rho/2,rho/2]` on the circle
of total Haar mass 1. Its true Toeplitz principal block has entries
`(Q_n)_{ii}=rho` and
`(Q_n)_{ij}=sin(pi*rho*(i-j))/(pi*(i-j))` for `i!=j`.
For fixed `0<c<1` and `0<=a<=1-c`, let
`K_n(a)=aI_n+cQ_n`, `H_n(a,c)=H(K_n(a))`, and
`h_rho(a,c)=lim_{n->infinity} H_n(a,c)/n`.
The target is
`h_rho((1-t)a0+t a1,c)>=(1-t)h_rho(a0,c)+t h_rho(a1,c)`
for every legal a0,a1 and `0<=t<=1`. The unresolved range is
`37/40<c<1` at FIXED rho and c as n grows. The endpoint `c=1` has only a=0,
so its entropy value alone does not prove the unresolved theorem.

The exact channel representation is: for any input binary law X, independently
over sites conditional on X, `Pr(Y_i=1|X)=a+cX_i`. For DPP(K) input, the
output is DPP(aI+cK). For a rank-k projection `P=UU*`, `U*U=I_k`, the input
is supported on k-subsets, with `mu(A)=|det U_A|^2`, and full output law
`p_a(S)=sum_{|A|=k} mu(A) (a+c)^|S intersect A|
 (1-a-c)^(k-|S intersect A|) a^(|S|-|S intersect A|)
 (1-a)^(n-k-|S|+|S intersect A|)`.
This formula, not an affine-atom approximation, determines all derivatives.

For interior a, the finite complete entropy identity is
`H''=-sum_S p_a''(S)log p_a(S)-sum_S p_a'(S)^2/p_a(S)`.
For moving expectations, `(sum q_a Phi_a)''=sum(q_a''Phi_a+2q_a'Phi_a'+q_aPhi_a'')`.
All probability acceleration, score/Fisher, layer-weight and reference-law
derivatives must be retained. The first term has no automatic favorable sign.
`Q_n` is not a finite projection; arbitrary unitary changes of spatial basis
do not preserve H. No differentiability of the limiting h is granted.

