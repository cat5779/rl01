DISPROVED

Fix \(0<\varepsilon<\tfrac12\). We construct, already for the fixed diagonal kernel
\[
K_m=L_m=\frac12 I,
\]
rank-one projectors \(P_m,Q_m\) with
\[
\|P_m-Q_m\|_1\longrightarrow0,
\]
and a flow \(F_m\in\mathcal F(K_m,P_m)\) whose distance from the **entire** target fiber \(\mathcal F(K_m,Q_m)\) is bounded below by an absolute positive constant. Hence the Hausdorff-to-parameter ratio diverges.

## 1. Flows at \(K=\frac12 I\)

Let the ground set have \(N\) coordinates. For a rank-one projector \(A\), define
\[
C^A(S,j)=2^{-(N-1)}A_{jj},\qquad j\notin S.
\tag{1}
\]

Since \(p_{I/2}(S)=2^{-N}\), the exact atom derivative is
\[
\begin{aligned}
b_{I/2,A}(S)
&=
2^{-N}\operatorname{tr}\!\left(
  \left(\frac12 I-I_{S^c}\right)^{-1}A
\right)\\
&=
2^{-(N-1)}
\left(
\sum_{j\in S}A_{jj}
-
\sum_{j\notin S}A_{jj}
\right).
\end{aligned}
\tag{2}
\]
This is exactly \(\operatorname{div}C^A\). Moreover, the total mass of \(C^A\) on edges adding coordinate \(j\) is \(A_{jj}\), so \(C^A\) has total mass
\[
\sum_j A_{jj}=1.
\]

We shall also use the following identity for arbitrary feasible flows:
\[
\boxed{
\sum_{S:j\notin S}G(S,j)=A_{jj}
\quad
\text{for every }G\in\mathcal F(I/2,A).
}
\tag{3}
\]
Indeed, multiply the divergence equation by
\(\mathbf 1_{\{j\in S\}}\) and sum over \(S\). Every edge except a \(j\)-edge cancels, while a \(j\)-edge contributes its mass once. The other side is
\[
\left.\frac d{dh}\mathbb P_{I/2+hA}(j\in X)\right|_{h=0}
=
\left.\frac d{dh}(I/2+hA)_{jj}\right|_{h=0}
=A_{jj}.
\]

## 2. The parameter family

Let \(m\ge144\), set \(N=m+1\), and relabel the coordinate set as
\[
\{0\}\cup R,\qquad R=\{1,\ldots,m\}.
\]
Put
\[
\mu=2^{-m},
\qquad
a=\frac6{\sqrt m},
\qquad
u=\frac1{\sqrt m}(1,\ldots,1)\in\mathbb R^m.
\]
Define unit vectors
\[
v=(\sqrt a,\sqrt{1-a}\,u),
\qquad
w=(0,u),
\]
and rank-one projectors
\[
P=vv^*,
\qquad
Q=ww^*.
\tag{4}
\]
Thus
\[
P_{00}=a,
\qquad
P_{jj}=\frac{1-a}{m}\quad(j\in R),
\tag{5}
\]
whereas
\[
Q_{00}=0,
\qquad
Q_{jj}=\frac1m\quad(j\in R).
\tag{6}
\]
In particular, \(P\) has full support and \(Q\) has support size \(m\), so both supports are genuinely unbounded.

For rank-one projections onto unit vectors \(v,w\),
\[
\|vv^*-ww^*\|_1
=
2\sqrt{1-|\langle v,w\rangle|^2}.
\]
Here
\[
|\langle v,w\rangle|^2=1-a,
\]
and therefore
\[
\boxed{
\|P-Q\|_1
=
2\sqrt a
=
2\sqrt6\,m^{-1/4}.
}
\tag{7}
\]

Take
\[
K=L=\frac12I_N.
\]
This is admissible for every fixed \(0<\varepsilon<\tfrac12\).

## 3. A bounded radial flow on the \(m\)-cube

For \(0\le k\le m\), define
\[
r_k=
\left(
1-\frac{|2k-m|}{4\sqrt m}
\right)_+.
\tag{8}
\]
For \(T\subseteq R\) and \(j\in R\setminus T\), define an upward flow on the \(m\)-cube by
\[
R(T,j)
=
\frac{(1-a)\mu}{m}\,r_{|T|}.
\tag{9}
\]
It satisfies
\[
0\le R(T,j)\le\frac{(1-a)\mu}{m}.
\tag{10}
\]

Let
\[
d(T)=\operatorname{div}_R R(T).
\]
For \(|T|=k\),
\[
d(T)
=
\frac{(1-a)\mu}{m}
\left(
kr_{k-1}-(m-k)r_k
\right),
\tag{11}
\]
with \(r_{-1}=0\).

The sequence \(r_k\) satisfies
\[
|r_{k-1}-r_k|
\le\frac1{2\sqrt m}.
\tag{12}
\]
Furthermore, if \(r_k>0\), then
\[
|2k-m|<4\sqrt m.
\]
Using
\[
kr_{k-1}-(m-k)r_k
=
k(r_{k-1}-r_k)+(2k-m)r_k,
\]
we obtain
\[
\left|
kr_{k-1}-(m-k)r_k
\right|
\le
\frac12\sqrt m+4\sqrt m
=
\frac92\sqrt m.
\]
Consequently,
\[
|d(T)|
\le
\frac{9(1-a)}{2\sqrt m}\mu
\le
a\mu,
\tag{13}
\]
because \(a=6/\sqrt m\).

Let
\[
M_m
=
\sum_{T\subseteq R}\sum_{j\notin T}R(T,j).
\tag{14}
\]
For \(X\sim\operatorname{Bin}(m,\tfrac12)\),
\[
M_m
=
(1-a)\,
\mathbb E\left[
\frac{m-X}{m}\,r_X
\right].
\tag{15}
\]
Since
\[
\operatorname{Var}(2X-m)=m,
\]
Chebyshev’s inequality gives
\[
\mathbb P\bigl(|2X-m|\le2\sqrt m\bigr)\ge\frac34.
\]
On this event,
\[
r_X\ge\frac12,
\qquad
\frac{m-X}{m}
=
\frac12-\frac{2X-m}{2m}
\ge
\frac12-\frac1{\sqrt m}
\ge\frac14.
\]
Also \(1-a\ge\tfrac12\) when \(m\ge144\). Therefore
\[
\boxed{
M_m\ge
\frac12\cdot\frac34\cdot\frac12\cdot\frac14
=
\frac3{64}.
}
\tag{16}
\]

Thus \(R\) has total mass bounded below independently of dimension, despite having pointwise divergence at most \(a\mu=O(m^{-1/2}\mu)\).

## 4. A feasible source flow with a macroscopic circulation

Represent a full-cube vertex as \((T,x)\), where \(T\subseteq R\) and \(x\in\{0,1\}\) records the state of coordinate \(0\).

For \(P\), the canonical flow (1) has:

\[
C^P((T,x),j)
=
\frac{(1-a)\mu}{m},
\qquad j\in R\setminus T,
\tag{17}
\]
in either layer, and
\[
C^P((T,0),0)=a\mu
\tag{18}
\]
on every vertical edge.

Define a signed edge field \(H\) by
\[
H^0=R,
\qquad
H^1=-R,
\qquad
H^{\mathrm v}(T)=d(T),
\tag{19}
\]
where \(H^0,H^1\) are the horizontal parts in layers \(x=0,1\), and \(H^{\mathrm v}(T)\) is the signed mass on
\[
(T,0)\longrightarrow(T,1).
\]

At a vertex \((T,0)\),
\[
\operatorname{div}H
=
\operatorname{div}_R R(T)-d(T)=0.
\]
At \((T,1)\),
\[
\operatorname{div}H
=
-\operatorname{div}_R R(T)+d(T)=0.
\]
Thus
\[
\operatorname{div}H=0.
\tag{20}
\]

Set
\[
F=C^P+H.
\tag{21}
\]

### Nonnegativity

In layer \(0\), horizontal masses are increased by \(R\).

In layer \(1\), (10) gives
\[
C^P((T,1),j)-R(T,j)\ge0.
\]

On vertical edges, (13) gives
\[
a\mu+d(T)\ge0.
\]
Hence \(F\ge0\).

### Divergence and total mass

By (20),
\[
\operatorname{div}F
=
\operatorname{div}C^P
=
b_{K,P}.
\]
The signed horizontal masses of \(H\) are \(M_m\) and \(-M_m\), while
\[
\sum_Td(T)=0.
\]
Thus \(H\) has total signed edge mass zero, so \(F\) has total mass one.

### Pointwise capacity

Every full-cube atom has probability
\[
p_K(T,x)=2^{-(m+1)}=\frac\mu2.
\]
The prescribed capacity is therefore
\[
\frac2\varepsilon p_K(T,x)
=
\frac\mu\varepsilon.
\tag{22}
\]

In layer \(1\), subtracting \(R\) only decreases the canonical outgoing flow, so
\[
F_{\rm out}(T,1)\le\mu.
\tag{23}
\]

In layer \(0\), writing \(k=|T|\) and using
\[
d(T)=R_{\rm in}(T)-R_{\rm out}(T),
\]
we find
\[
\begin{aligned}
F_{\rm out}(T,0)
&=
\frac{(1-a)\mu}{m}(m-k)
+R_{\rm out}(T)
+a\mu+d(T)\\
&=
\frac{(1-a)\mu}{m}(m-k)
+a\mu+R_{\rm in}(T)\\
&\le
\frac{(1-a)\mu}{m}(m-k)
+a\mu
+\frac{(1-a)\mu}{m}k\\
&=\mu.
\end{aligned}
\tag{24}
\]
Because \(\varepsilon<\tfrac12\),
\[
\mu<\frac\mu\varepsilon.
\]
Thus all capacities hold, and
\[
\boxed{
F\in\mathcal F(K,P).
}
\tag{25}
\]

## 5. Separation from the entire target fiber

Let
\[
G\in\mathcal F(K,Q)
\]
be arbitrary.

From (3) and \(Q_{00}=0\),
\[
\sum_{T\subseteq R}G((T,0),0)=0.
\]
Since \(G\ge0\), every vertical edge of \(G\) is identically zero.

Let \(G^0,G^1\) denote its horizontal parts in the two layers, and define
\[
D^0=G^0-F^0,
\qquad
D^1=G^1-F^1.
\tag{26}
\]

Let \(\beta\) be the divergence on the \(m\)-cube of the constant flow
\[
A(T,j)=\frac\mu m.
\tag{27}
\]
Because \(Q_{jj}=1/m\), the target divergence in each layer is exactly \(\beta\).

The horizontal divergences of \(F\) are
\[
\operatorname{div}_R F^0=(1-a)\beta+d,
\qquad
\operatorname{div}_R F^1=(1-a)\beta-d.
\]
Therefore
\[
\operatorname{div}_R D^0=a\beta-d,
\qquad
\operatorname{div}_R D^1=a\beta+d.
\tag{28}
\]

Use the rank function
\[
\phi(T)=|T|.
\]
Every upward horizontal edge has \(\phi\)-increment one. Hence, for every signed horizontal field \(D\),
\[
\langle\phi,\operatorname{div}D\rangle
=
\sum_eD(e).
\tag{29}
\]

The total mass of \(A\) is
\[
\sum_{T,j\notin T}\frac\mu m
=
\frac12,
\]
and therefore
\[
\langle\phi,\beta\rangle=\frac12.
\tag{30}
\]
Likewise,
\[
\langle\phi,d\rangle
=
\langle\phi,\operatorname{div}R\rangle
=
\sum_eR(e)
=
M_m.
\tag{31}
\]

Applying (29)–(31) to (28) gives
\[
\sum_eD^0(e)=\frac a2-M_m,
\qquad
\sum_eD^1(e)=\frac a2+M_m.
\]
Consequently,
\[
\begin{aligned}
\|D^0\|_1+\|D^1\|_1
&\ge
\left|\frac a2-M_m\right|
+
\left|\frac a2+M_m\right|\\
&=
2\max\left\{\frac a2,M_m\right\}\\
&\ge2M_m.
\end{aligned}
\]
The two horizontal layers are disjoint edge sets, so, by (16),
\[
\boxed{
\|F-G\|_1
\ge
2M_m
\ge
\frac3{32}.
}
\tag{32}
\]
This holds for every \(G\in\mathcal F(K,Q)\). Therefore
\[
d_H^{(1)}
\bigl(
\mathcal F(K,P),\mathcal F(K,Q)
\bigr)
\ge
\inf_{G\in\mathcal F(K,Q)}\|F-G\|_1
\ge
\frac3{32}.
\tag{33}
\]

## 6. Divergence of the Hausdorff ratio

Using (7) and \(K=L\),
\[
\begin{aligned}
\frac{
d_H^{(1)}
\bigl(
\mathcal F(K,P),\mathcal F(L,Q)
\bigr)
}{
\|K-L\|_1+\|P-Q\|_1
}
&\ge
\frac{3/32}{2\sqrt6\,m^{-1/4}}\\
&=
\frac3{64\sqrt6}\,m^{1/4}
\longrightarrow\infty.
\end{aligned}
\tag{34}
\]

Thus there is no finite \(H_\varepsilon\), independent of dimension, for which (HDF) holds.

The obstruction comes from a macroscopic signed circulation placed between the two layers. Its vertical divergence is only \(O(m^{-1/2})\) pointwise, so it fits inside the small distinguished-coordinate mass \(P_{00}=6/\sqrt m\), while its horizontal mass stays bounded below. Removing that coordinate forces every target flow to eliminate the vertical edges, and the rank moment identity then forces a constant amount of horizontal \(\ell^1\) movement.

This proves failure of the full-fiber Hausdorff estimate. It is a directed Hausdorff obstruction arising from a deliberately chosen source flow; by itself it is not an infimum-distance separation between the two fibers and therefore does not independently rule out a selector that avoids this flow.


