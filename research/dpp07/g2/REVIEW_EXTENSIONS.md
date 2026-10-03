# §6–§7 独立对抗核验

## 裁决

### §6：CORRECT

在文中固定的右平移约定
\[
(R_gf)(x)=f(xg)
\]
下，
\[
T_a=R_a-I,\qquad
\Delta=T_a^*T_a+T_b^*T_b
=4I-R_a-R_a^*-R_b-R_b^*
\]
完全一致。把 Cayley 树的有向边分成
\((g,ga)\) 与 \((g,gb)\) 两个左不变轨道后，梯度是列算子
\(\nabla=(T_a,T_b)^{\mathsf T}\)，故梯度投影
\(\nabla\Delta^{-1}\nabla^*\) 在第一边轨道上的对角压缩恰为
\[
K=T_a\Delta^{-1}T_a^*.
\]
第一边轨道由 \(g\mapsto(g,ga)\) 与一份标量正则表示等距等变识别；这里没有隐藏的二重迹标度。于是该压缩的规范迹就是
\(\tau(K)=\langle K\delta_1,\delta_1\rangle\)，而不是两类边上的未归一化迹。

从全边 DPP 的普通随机序支配限制到 \(a\)-边坐标，得到
\(p_-(K)\ge 1/3\)。连续的 \(n\) 条 \(a\)-边在全树中是连通边集，故 §3 的行列式公式直接给出
\[
\det K[F_n]=3^{-n}(1+n/2).
\]
若 \(\operatorname{Bern}(p)\le_{\rm st}\mu_K\)，全占据柱事件给
\(p^n\le \det K[F_n]\)，取 \(n\) 次根并令 \(n\to\infty\) 得
\(p\le1/3\)。因此
\[
p_-(K)=1/3.
\]

注入性也成立：
\[
\langle Kf,f\rangle
=\|\Delta^{-1/2}T_a^*f\|^2,
\]
而 \(T_a^*f=0\) 表示 \(f\) 在每个无限右 \(\langle a\rangle\)-轨道上为常数；平方可和迫使这些常数全为零。另一方面，对
\(f_N=N^{-1/2}\sum_{j=1}^N\delta_{a^j}\)，
\(\|T_a^*f_N\|^2=2/N\)，从而
\[
0\le \langle Kf_N,f_N\rangle
\le \|\Delta^{-1}\|\,2/N\to0.
\]
所以 \(K\) 注入但不有界可逆。

FK 行列式部分亦成立。这里必须使用解析延拓
\[
\Delta_\tau(X)=\exp\!\left(\int_0^\infty\log t\,d\mu_{|X|}(t)\right),
\]
允许值为零；它对有限因子中的任意有界算子仍满足乘法性。原始 Fuglede–Kadison 论文已明确证明解析延拓对任意（包括奇异）因子保持
\(\Delta_\tau(XY)=\Delta_\tau(X)\Delta_\tau(Y)\)。因此不能把 \(T_a\) 当成可逆元，但可以合法地写
\[
\Delta_\tau(K)
=\Delta_\tau(T_a)\Delta_\tau(\Delta^{-1})\Delta_\tau(T_a^*).
\]
\(R_a\) 的谱分布为圆周 Haar 测度，因为
\(\tau(R_a^m)=0\) 对每个 \(m\ne0\)；且
\[
\int_0^{2\pi}\log|e^{it}-1|\,\frac{dt}{2\pi}=0,
\]
其对数奇点可积，故
\(\Delta_\tau(T_a)=\Delta_\tau(T_a^*)=1\)。

对四正则树的邻接算子，径向 resolvent 计算给
\[
L(z)=\tau\log(zI-\mathcal A)
=-\log u-\log(1-u^2),
\quad
z=u^{-1}+3u.
\]
在 \(z=4\) 时 \(u=1/3\)，所以
\[
\Delta_\tau(\Delta)=e^{L(4)}=\frac{27}{8},
\qquad
\Delta_\tau(K)=\frac8{27}.
\]
综上
\[
0<\operatorname{FK}(K)=\frac8{27}<\frac13=p_-(K),
\]
是严格、无核且非有界可逆的自由群反例。

### §7：CORRECT（数学范围）

对任意正收缩 \(Q\) 与有限非空 \(F\)，压缩的算子 Jensen/解算子不等式给
\[
\tau\log(Q+\varepsilon I)
\le |F|^{-1}\log\det(Q[F]+\varepsilon I).
\]
令 \(\varepsilon\downarrow0\)（扩展实数意义）得到
\[
\operatorname{FK}(Q)\le
\delta(Q):=\inf_F\det Q[F]^{1/|F|}.
\]
全占据柱事件则给 \(p_-(Q)\le\delta(Q)\)。

右 Følner 公式与本文右卷积约定严格相容。令
\(q(g)=Q(g,1)\)。左等变性给
\(Q(x,y)=q(y^{-1}x)\)，因此
\[
\frac{\|(I-P_F)QP_F\|_{\rm HS}^2}{|F|}
=\sum_{g\in\Gamma}|q(g)|^2
\frac{|\{y\in F:yg\notin F\}|}{|F|}.
\]
右 Følner 性使每个固定 \(g\) 的比例趋零，而
\(q\in\ell^2(\Gamma)\) 提供可和支配，故该式趋零。

矩收敛论证也闭合。若 \(R=PQP\)、
\(M_k=PQ^kP-R^k\)，则
\[
M_{k+1}=RM_k+PQ(I-P)Q^kP.
\]
并且
\[
\|PQ(I-P)Q^kP\|_1
\le \|(I-P)QP\|_2\,\|(I-P)Q^kP\|_2
\le k\sqrt2\,\|(I-P)QP\|_2^2,
\]
其中最后一步来自
\([Q^k,P]=\sum_{j=0}^{k-1}Q^j[Q,P]Q^{k-1-j}\) 与
\(\|[Q,P]\|_2=\sqrt2\|(I-P)QP\|_2\)。对固定 \(k\) 归纳即得归一化矩收敛；对
\(\log(t+\varepsilon)\) 的多项式逼近给出正则化行列式极限。

奇异端点没有遗漏。未正则化量满足
\[
\tau\log Q
\le |F_n|^{-1}\log\det Q[F_n]
\le |F_n|^{-1}\log\det(Q[F_n]+\varepsilon I).
\]
若 \(\tau\log Q> -\infty\)，两侧夹逼；若
\(\tau\log Q=-\infty\)，对每个固定 \(\varepsilon>0\) 先取上极限，再令
\(\varepsilon\downarrow0\)，便得到上极限为 \(-\infty\)。所以包括零行列式在内，均有
\[
|F_n|^{-1}\log\det Q[F_n]\longrightarrow\tau\log Q.
\]
因而对可数 amenable 群
\[
\delta(Q)=\operatorname{FK}(Q),\qquad
p_-(Q)\le\operatorname{FK}(Q),\qquad
p_+(Q)\ge1-\operatorname{FK}(I-Q).
\]
这些只是无条件必要性。若假设 (D) 正好提供反向的两条普通随机序支配，则与上述必要性合并才得到等号；§7 本身没有证明 (D)，也没有把必要性误写成充分性。

## CRITICAL GAPS（仅先行文献归属范围）

§7 的 Følner 行列式结论不应作为新的普遍定理归于本文。Li–Thom 的 Theorem 1.4 已对每个可数离散 amenable 群、每个 Følner 网以及群 von Neumann 代数中的任意正元素证明
\[
\det_{\mathcal N\Gamma}(g)
=\inf_F\det(g_F)^{1/|F|}
=\lim_F\det(g_F)^{1/|F|},
\]
明确包含奇异端点。本文的 §7 给出一条可成立的自包含证明路线，但若稿件暗示该普遍行列式逼近本身为新结果，则属于实质性归属错误；应明确引用并说明这里是在复证/专门化既有定理。该归属缺口不推翻 §7 的数学结论，也不影响 §6 的新反例核验。

## 原始来源

1. B. Fuglede and R. V. Kadison, *Determinant Theory in Finite Factors*, Ann. of Math. 55 (1952), 520–530，尤其第 5 节对奇异算子的解析延拓及任意乘积的乘法性：<https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1952_DeterminantTheoryInFiniteFactors.pdf>。
2. H. Li and A. Thom, *Entropy, Determinants, and L2-Torsion*, J. Amer. Math. Soc. 27 (2014), Theorem 1.4（预印本正文含完整定理与证明）：<https://www.math.buffalo.edu/~hfli/entdettor17.pdf>。

