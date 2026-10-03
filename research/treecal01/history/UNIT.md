# Unit-conductance critical-cluster contraction has the wrong WUSF marginal

Status: the specified unit-resistance method has been disproved; the original endpoint problem remains open.

Disproved statement: the specific conditional unit-conductance quotient-WUSF construction below has upper marginal mu_Q. The optimal invariant joining and joint iid targets remain INCOMPLETE. This argument excludes every implementation with that same conditional quotient-WUSF law; it does not exclude different conditional laws or different conductances.

## 1. Precisely specified method

Let B be independent bond Bernoulli(1/2) on the 3-regular tree. Almost surely every B-cluster is finite: forward exploration is the critical Bin(2,1/2) branching process, whose extinction probability is one. Contract each B-cluster. The resulting graph is a locally finite tree, with one unit-conductance edge for every original closed edge. Conditional on B, sample its wired uniform spanning forest U, and lift

\[
T^*=B\cup\operatorname{lift}(U).
\]

The assertion under test is that T* has the original unit-conductance WUSF law mu_Q. Taking the quotient WUSF is a fully specified probability-law operation. The argument below does not assume an equivariant conditional sampler for a different arbitrary joining.

Fix two edges e1,e2 incident to the same original vertex v. The target marginal satisfies

\[
\mu_Q(e_1,e_2\notin T)=\det(I-Q)[\{e_1,e_2\}]=\frac1{12},
\tag{1}
\]

because the diagonal is 2/3 and the off-diagonal has absolute value 1/6. We show

\[
\mathbb P(e_1,e_2\notin T^*)>\frac{167}{2000}>\frac1{12}.
\tag{2}
\]

The second inequality has exact difference 1/6000.

## 2. An infinite-network resistance variable

Replacing open edges of B by resistance zero and closed edges by resistance one is exactly the quotient network after identifying zero-resistance clusters. Let R be the effective wired resistance from the root of an infinite forward binary half-tree to infinity, using these independent zero/unit resistances. Equivalently, wire finite-depth boundaries, contract zero edges, and take the increasing limit of the effective resistances.

One has

\[
0<R\le1\quad\hbox{almost surely}.
\tag{3}
\]

For the upper bound, replacing all zero resistances by one gives the original binary half-tree, whose resistance is one; Rayleigh monotonicity applies first on finite networks and then on the limit. For strict positivity, the zero cluster at the half-tree root is finite almost surely. Its finite boundary is a cutset consisting of unit-resistance edges. If its size is d, unit flow through that cutset has energy at least 1/d by Cauchy–Schwarz. This also bounds the resistance of all sufficiently deep wired truncations from below.

The two forward branches are independent. Consequently

\[
R\overset d=\frac{(A_1+R_1)(A_2+R_2)}{A_1+A_2+R_1+R_2},
\tag{4}
\]

where A1,A2 are independent uniform elements of {0,1}, R1,R2 are independent copies of R, and the four variables are independent. The identity follows from series and parallel resistance laws on every finite wired truncation, then monotone convergence. No finite expectation of a critical cluster size is used.

## 3. Exact two-edge cylinder of the method

If either e1 or e2 is open in B, the two-edge vacancy event for T* is impossible. Conditional on both being closed, write R1,R2 for the independent resistances beyond these edges. The third arm from v has series resistance A3+R3, with an independent Bernoulli A3 and independent copy R3. Put

\[
c_1=(1+R_1)^{-1},\quad c_2=(1+R_2)^{-1},
\quad c_3=(A_3+R_3)^{-1},\quad C=c_1+c_2+c_3.
\]

Eliminating the three branches to their common wired boundary gives these three conductances from v. The transfer-current complement on the first two **unit-resistance** edges is

\[
\begin{pmatrix}
c_1-c_1^2/C&-c_1c_2/C\\
-c_1c_2/C&c_2-c_2^2/C
\end{pmatrix},
\tag{5}
\]

up to simultaneous sign changes arising from edge orientations. One way to check (5) is to send a unit current across the first edge: the return route consists of its exterior arm in series with the parallel combination of the other two arms. This gives the diagonal; Kirchhoff's law gives the off-diagonal. The same calculation works on finite wired truncations. Their transfer-current matrices converge to the wired matrix, including when a zero cluster first meets a finite boundary. In that case c3=infinity is interpreted by its limit, which yields the same formula.

The infinite-network transfer-current theorem, followed by complementation, identifies the conditional vacancy probability as the determinant of (5). It is

\[
\frac{c_1c_2c_3}{C}
=\frac1{(1+R_1)(1+R_2)+(2+R_1+R_2)(A_3+R_3)}.
\tag{6}
\]

All conditioning here concerns only three specified Bernoulli edges. Remaining half-trees stay independent. Averaging A3 and the probability 1/4 that e1,e2 are closed gives the exact infinite formula

\[
\mathbb P(e_1,e_2\notin T^*)=
\frac18\mathbb E\left[
\frac1{(1+R_1)(1+R_2)+(2+R_1+R_2)R_3}
+\frac1{(1+R_1)(1+R_2)+(2+R_1+R_2)(1+R_3)}
\right].
\tag{7}
\]

Each summand is decreasing in each resistance. We next bound (7) from below without estimating the true resistance distribution numerically.

## 4. Exact one-sided finite distribution

Let M=256 and D=H=2^36=68719476736. We represent a probability law on {0,1/M,...,1} by nonnegative integer masses w0,...,wM summing to D. Start with all mass at 1. This law stochastically dominates R by (3).

For a pair of indices i,j and a,b in {0,M}, define

\[
k(i,j,a,b)=\left\lceil\frac{(i+a)(j+b)}{i+j+a+b}\right\rceil,
\tag{8}
\]

with value zero when the denominator is zero. Dividing by M, this is the parallel-resistance expression of (4), rounded **up** to the grid. Form integer unnormalized masses

\[
C_k=\sum_{i,j=0}^M\sum_{a,b\in\{0,M\}}
w_iw_j\mathbf1\{k(i,j,a,b)=k\}.
\]

Their sum is 4D^2. Set, for k=0,...,M,

\[
F_k=\left\lfloor\frac{\sum_{h\le k}C_h}{4D}\right\rfloor,
\qquad w'_0=F_0,\quad w'_k=F_k-F_{k-1}.
\tag{9}
\]

Then F_M=D. Thus (9) is a probability law whose cumulative distribution function is at most that of the exactly updated grid law: the new law stochastically dominates that grid law. The update (4) is increasing in each input. Induction therefore proves that **every** iterate of (8)–(9) stochastically dominates the actual infinite-network R. Neither convergence of the iteration nor closeness of its distribution is required.

Run exactly 100 iterations. The complete final vector is in grid256.json. Equations (8)–(9) specify it without hidden data; the included ordered verifier reconstructs these integer updates.

For each triple i,j,k, let

\[
d_0=(M+i)(M+j)+(2M+i+j)k,\quad
d_1=d_0+(2M+i+j)M,
\]

and

\[
v_{ijk}=\left\lfloor\frac{M^2H}{d_0}\right\rfloor
+\left\lfloor\frac{M^2H}{d_1}\right\rfloor.
\tag{10}
\]

Both denominators are strictly positive. Since the function in (7) is coordinatewise decreasing and (10) rounds its values down, stochastic domination gives the rigorous lower bound

\[
\mathbb P(e_1,e_2\notin T^*)\ge
\frac{N}{8D^3H},\qquad
N=\sum_{i,j,k=0}^M w_iw_jw_kv_{ijk}.
\tag{11}
\]

This is the infinite bridge: the finite computation bounds an actual infinite resistance satisfying (3)–(4), rather than approximating a finite spanning tree and guessing its limit.

## 5. Integer certificate and conclusion

The exact finite integer result is

\[
N=14952777335680031294141131063220689702158014,
\]

\[
8D^3H=178405961588244985132285746181186892047843328.
\]

In particular,

\[
12N-8D^3H=1027366439915390397407826577461384378052840>0.
\]

The stronger comparison 2000N>167(8D^3H) is also checked in verifygrid01.py. That verifier reconstructs all 100 iterates with **ordered pairs**, independently of the generation program's symmetry reduction, matches the entire vector and final sum, and uses no floating-point operations.

Equations (11) and this exact inequality prove (2), whereas (1) holds for the desired DPP. The conditional unit-conductance quotient-WUSF lift therefore cannot be the desired marginal, independent of how the quotient WUSF is sampled.

This result neither disproves an invariant endpoint joining nor constructs one with the right upper law. It isolates the first failed identity of this concrete cluster-conditioning method. Changing quotient conductances or replacing its WUSF conditional law requires a new argument.

## Sources and review boundary

The classical infinite-network transfer-current determinant is [BLPS, Uniform Spanning Forests, Theorem 7.8](https://rdlyons.pages.iu.edu/pdf/usf.pdf). Its hypothesis is an arbitrary network; here the quotient is locally finite and has unit positive conductances. The network laws and the series/parallel calculations above are derived explicitly. The scoped review of this predecessor is summarized in [../REVIEW.md](../REVIEW.md). This is not a counterexample to the endpoint joining problem.
