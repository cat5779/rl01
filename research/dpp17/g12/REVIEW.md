# Independent mathematical audit

STATUS: PASS

## Certified scope

The argument in `RESULT.md` proves the frozen statement in `TASK.md` for the canonical matching-block class \(\mathcal M_E^\varepsilon\): every nonzero off-diagonal component has size at most two, no common matching is supplied for the two kernels, and the Lipschitz constant is independent of \(|E|\). This audit does **not** certify an unrestricted non-diagonal selector, exact JO, any strong process construction, or novelty.

## Checks of the load-bearing steps

1. **DPP atom and derivative bounds.** The atom formula
   \[
   p_A(S)=(-1)^{|S^c|}\det(A-I_{S^c})
   \]
   and the factorization
   \[
   A-I_{S^c}=\tfrac12J_S\bigl(I+J_S(2A-I)\bigr)
   \]
   give \(\|(A-I_{S^c})^{-1}\|_{\rm op}\le \varepsilon^{-1}\). Differentiation, trace-norm duality, summation over atoms, and integration therefore justify both (3) and (4). No dimension factor enters.

2. **Two-coordinate divergence and conjugations.** For
   \(A=\left(\begin{smallmatrix}a&c\\\bar c&b\end{smallmatrix}\right)\) and
   \(R=\left(\begin{smallmatrix}r_1&\rho\\\bar\rho&r_2\end{smallmatrix}\right)\), direct differentiation of \(\det(I-A-sR)\) gives
   \[
   t=(1-b)r_1+(1-a)r_2+2\Re(\bar c\rho).
   \]
   With divergence defined as incoming minus outgoing, the four edge masses satisfy exactly
   \(y=t-x\), \(u=r_1-x\), and \(v=r_2-t+x\). Their divergences at the four vertices are respectively \(-t,t-r_2,t-r_1,1-t\), matching the DPP derivative. The signs and complex conjugations are correct.

3. **Feasible interval.** Nonnegativity and the two nontrivial singleton capacities give precisely
   \[
   \max\{0,t-r_2,r_1-C_2\}\le x\le
   \min\{r_1,t,C_1-r_2+t\}.
   \]
   All nine lower/upper comparisons follow from \(0\le t\le1\),
   \(r_2-t\le C_1\), \(r_1-t\le C_2\), and
   \(1-t\le C_1+C_2\). The last inequality is valid because
   \(p_A(\{1\})+p_A(\{2\})\ge2\varepsilon(1-\varepsilon)\), hence
   \(C_1+C_2\ge4(1-\varepsilon)>1\). The capacity at the empty state follows from \((I-A)^{-1}\preceq \varepsilon^{-1}I\). Thus the projected reference point always defines a positive unit-mass flow in the required fiber.

4. **Refinement compatibility.** When \(c=0\), the reference point already lies in the feasible interval and yields
   \[
   G_{A,R}(S,i)=R_{ii}\,p_{A_{\{1,2\}\setminus\{i\}}}(S).
   \]
   After multiplication by the block weight, this is exactly the singleton formula with coefficient \(P_{ii}\), even when the compressed rank-one matrix has off-diagonal entries. Consequently joining or splitting a zero-coupled pair does not alter any global edge mass. Since every compatible matching partition differs from the canonical one only by such joins/splits among isolated coordinates, (53) is justified.

5. **Local Lipschitz estimate.** The adjugate identity in dimension two has the stated sign:
   \[
   \operatorname{adj}(I-A)-\operatorname{adj}(I-B)
   =(A-B)-\operatorname{tr}(A-B)I.
   \]
   The matrix representation of the reference value also has the correct conjugations. The max/min and moving-interval projection bounds give (38); substitution in the four edge formulas gives a valid (loose) constant
   \(\Lambda_\varepsilon=8\varepsilon^{-2}+20\). The homogeneous estimate is valid at zero weights because
   \(|x-y|\le\|xR-yS\|_1\) and
   \(\min(x,y)\|R-S\|_1\le2\|xR-yS\|_1\).

6. **Global block construction.** A compression \(P_B\) of a rank-one projector is positive of rank at most one, and when nonzero its trace normalization is a rank-one projector. Because the DPP inverse is block diagonal, cross-block entries of \(P\) make zero contribution to the trace, so (48) gives the exact global divergence. Product factorization of DPP atoms gives nonnegativity, total mass \(\sum_B\operatorname{tr}P_B=1\), and the original capacity \((2/\varepsilon)p_K(U)\).

7. **Common-partition comparison.** In (56), the outside-law term is correctly weighted by \(w_B=\operatorname{tr}P_B\); summing \(w_B\sum_{C\ne B}\|K_C-L_C\|_1\) costs no dimension factor. For the local terms, block pinching of the Hermitian matrix \(P-Q\) is trace-norm contractive, which proves (59). The displayed \(C_\varepsilon^{(0)}=16\varepsilon^{-2}+41\) dominates both coefficients for \(0<\varepsilon<1/2\).

8. **Incompatible matchings.** Deleting a noncommon matching edge preserves the spectral gap: an undeleted two-block is unchanged, while a deleted block becomes diagonal with diagonal entries in \([\varepsilon,1-\varepsilon]\). For the deleted edges of \(K\), the Hermitian phase matrix \(W\) is a direct sum of norm-one \(2\times2\) swaps and satisfies
   \[
   \operatorname{tr}(W(K-L))=2\sum_{e\in M_K\setminus M_L}|K_e|.
   \]
   The phase choice and conjugations are correct. Trace-norm duality therefore proves (63), and the identical argument proves (64). The triangle inequality gives (65). Applying the already proved common-partition estimate to the three pairs is legitimate by refinement compatibility and yields the dimension-free factor five.

9. **Measurability and equivariance.** On a fixed two-block the construction uses continuous algebraic operations, max/min, and interval projection. The homogeneous estimate removes the apparent singularity when a block weight vanishes, and refinement compatibility handles support changes when an off-diagonal entry reaches zero. The global Lipschitz estimate implies Borel dependence. Under an internal transposition, \(s\mapsto t-s\) and \([\ell,u]\mapsto[t-u,t-\ell]\), so the local rule is covariant; canonical matchings and outside laws relabel under arbitrary coordinate permutations. This proves full coordinate-permutation equivariance.

## Verdict

No critical gap was found. The explicit selector and the bound
\[
C_\varepsilon=80\varepsilon^{-2}+205
\]
are valid for the frozen canonical matching-block class, uniformly in the finite coordinate set. The constants are intentionally non-sharp but have the stated dependence only on \(\varepsilon\).
