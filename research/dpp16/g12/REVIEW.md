STATUS: PASS

# R16/G12 独立数学初审

## 裁决与认证范围

我完整核对了 `prompt.md` 与 `output.md`，并交叉检查了 R15/G11 的固定支撑
least-Euclidean-norm selector 证明以及 R15/G12b 的对角核显式公式。作者的
`PROVED` 裁决成立。

准确地说：对题面**预先给定**的分块

\[
E=\bigsqcup_{\alpha\in A}B_\alpha,\qquad |B_\alpha|\le r,
\]

以及相对于该分块为 block-diagonal 的统一谱隙核 (K)，公式 (BSEL) 确实给出
原 full positive capacitated birth-flow fiber 中的 Borel、分块置换协变选择器。
而且对同一给定分块上的任意两对 ((K,P),(L,Q))，有

\[
\|F^{\mathrm{blk}}_{K,P}-F^{\mathrm{blk}}_{L,Q}\|_1
\le
\left(\varepsilon^{-1}+\Lambda_{\varepsilon,r}\right)\|K-L\|_1
+
\left(1+2\Lambda_{\varepsilon,r}\right)\|P-Q\|_1,
\]

故可取

\[
C_{\varepsilon,r}
=\max\{\varepsilon^{-1}+\Lambda_{\varepsilon,r},
1+2\Lambda_{\varepsilon,r}\}.
\]

这里 (Lambda_{\varepsilon,r}<\infty) 是有限维局部 least-norm selector 的精确定义
Lipschitz 常数，只依赖 ((\varepsilon,r))。结论不依赖 (|E|) 或块数。本审查
不把它外推到无给定有界分块的一般非对角核。

## 1. 局部输入确实覆盖题面所用的 (G)

R15/G11 证明的是同一个选择规则：在整个原始正容量 flow fiber 上取唯一
least-Euclidean-norm 点。令该结果中的固定支撑上界 (s=r)，再把 ambient
coordinate set 取为单块 (B_\alpha)，则单块上的任意 rank-one projector 的
支撑至多为 (|B_\alpha|\le r)。因此 R15/G11 的估计直接给出

\[
\|G_{A,R}-G_{B,S}\|_1
\le \Lambda_{\varepsilon,r}
(\|A-B\|_1+\|R-S\|_1)
\]

并保证题稿 (2) 的 supremum 有限。这里没有把另一个 selector 偷换成 (G)，
也没有要求常数在 (r\to\infty) 时统一。

当 (r=1) 时，单点局部 fiber 只有质量为一的唯一边流，故 (BSEL) 化为

\[
F_{K,P}(S,i)=P_{ii}p_{K_{E\setminus\{i\}}}(S),
\]

与 R15/G12b 已审计的对角核公式完全一致。

## 2. DPP 导数与 cross-block 项消失

对任意原子 (U\subseteq E)，令

\[
M_U=K-I_{U^c}.
\]

统一谱隙保证 (M_U) 可逆；文稿的恒等式

\[
M_U=\tfrac12J_U\bigl(I+J_U(2K-I)\bigr)
\]

以及 (|2K-I\|_{\mathrm{op}}\le1-2\varepsilon) 足以证明这一点。Jacobi
公式于是给出

\[
b_{K,P}(U)=p_K(U)\operatorname{tr}(M_U^{-1}P).
\]

因为 (K) 与 (I_{U^c}) 都相对于给定分块为 block-diagonal，(M_U^{-1})
也 block-diagonal。因此

\[
\operatorname{tr}(M_U^{-1}P)
=\sum_\alpha
\operatorname{tr}\!left[
(K_\alpha-I_{B_\alpha\setminus S_\alpha})^{-1}P_\alpha
\right].
\]

所有 (Pi_\alpha P\Pi_\beta), (alpha\ne\beta)，确实处在乘积的非对角块，
其迹严格为零；这不是把 (P) 额外假设为 block-diagonal。代入
(P_\alpha=w_\alpha R_\alpha) 与 DPP 块乘积分解，正好得到稿中 (12)：

\[
b_{K,P}(U)=\sum_\alpha
w_\alpha p_{K_{E\setminus B_\alpha}}(T_\alpha)
b_{K_\alpha,R_\alpha}(S_\alpha).
\]

若 (w_\alpha=0)，rank-one 压缩 (P_\alpha=v_{B_\alpha}v_{B_\alpha}^*=0)，
相应项自然为零。

## 3. 全局 fiber 的四项约束

每条全局边的新增坐标恰好属于一个块，所以稿中 (41) 的 edge-space direct
sum 没有重复计数。

1. **非负性。** (w_\alpha\ge0)、outside DPP atom 非负、局部 (G\ge0)，
   因而每条边非负。
2. **精确散度。** 沿 (B_\alpha) 的入边与出边保持 outside pattern
   (T_\alpha) 不变，故该块对顶点 (U) 的散度正是
   (w_\alpha p_{K_{-B_\alpha}}(T_\alpha)
   b_{K_\alpha,R_\alpha}(S_\alpha))。对块求和与上一节的导数分解完全相等。
3. **单位总质量。** 每个局部 (G) 与每个 outside law 的总质量均为一，
   因此第 (alpha) 块全部边的质量为 (w_\alpha)。又
   (sum_\alpha w_\alpha=\operatorname{tr}P=1)。
4. **原点态容量。** 局部容量乘 outside atom 后为
   ((2/\varepsilon)w_\alpha p_K(U))。对块求和并用
   (sum_\alpha w_\alpha=1)，得到恰好
   ((2/\varepsilon)p_K(U))，没有多出块数。

所以构造属于题面要求的**原 full fiber**，而不是某个放宽或 signed 子空间。

## 4. 小块权重不会导致归一化爆炸

这是证明中最承重的一步，稿中 (26) 正确。对

\[
X=xR,\qquad Y=yS
\]

定义 (widehat G(A,X)=xG_{A,R})。当 (x,y>0) 时，若先改变核再改变加权
projector，可得

\[
\|xG_{A,R}-yG_{B,S}\|_1
\le
\Lambda_{\varepsilon,r}x\|A-B\|_1
+|x-y|+
\Lambda_{\varepsilon,r}\min(x,y)\|R-S\|_1.
\]

另一方面，由迹范数与三角不等式，

\[
|x-y|\le\|xR-yS\|_1,
\qquad
\min(x,y)\|R-S\|_1\le2\|xR-yS\|_1.
\]

因此

\[
\|\widehat G(A,X)-\widehat G(B,Y)\|_1
\le
\Lambda_{\varepsilon,r}x\|A-B\|_1
+(1+2\Lambda_{\varepsilon,r})\|X-Y\|_1.
\]

若 (x=0) 或 (y=0)，左端直接等于另一个权重，仍由
(|X-Y|_1) 控制。故后续估计始终作用于未归一化压缩
(P_\alpha=w_\alpha R_\alpha)，从未除以可能趋零的 (w_\alpha)。这也同时
处理了支撑退化。

## 5. outside law 的加权汇总无维数损失

稿中 DPP law 稳定性

\[
\|p_A-p_B\|_1\le\varepsilon^{-1}\|A-B\|_1
\]

是成立的。沿线段 (A_t) 对每个 atom 求导后，上一节的因子分解给出
(|(A_t-I_{S^c})^{-1}|_{\mathrm{op}}\le\varepsilon^{-1})；再用
(|\operatorname{tr}(MH)|\le\|M\|_{\mathrm{op}}\|H\|_1)、对 atom 求和并
积分即可。

令 (delta_\beta=\|K_\beta-L_\beta\|_1)。product law telescoping 给出

\[
\|p_{K_{-B_\alpha}}-p_{L_{-B_\alpha}}\|_1
\le\varepsilon^{-1}\sum_{\beta\ne\alpha}\delta_\beta.
\]

全局流比较中这一项由 (w_\alpha) 加权，所以

\[
\sum_\alpha w_\alpha
\|p_{K_{-B_\alpha}}-p_{L_{-B_\alpha}}\|_1
\le
\varepsilon^{-1}\sum_\beta(1-w_\beta)\delta_\beta
\le\varepsilon^{-1}\|K-L\|_1.
\]

这里使用了 (K-L) block-diagonal，故
(|K-L|_1=\sum_\beta\delta_\beta)。没有把逐块的统一上界再无权相加。

## 6. pinching 与 simultaneous ((K,P)) 估计

将第 4 节的不等式逐块应用于

\[
X=P_\alpha,\qquad Y=Q_\alpha
\]

得到

\[
\sum_\alpha\|H_\alpha^{K,P}-H_\alpha^{L,Q}\|_1
\le
\Lambda_{\varepsilon,r}\|K-L\|_1
+(1+2\Lambda_{\varepsilon,r})
\sum_\alpha\|P_\alpha-Q_\alpha\|_1.
\]

最后一和不是用块数估计，而是

\[
\sum_\alpha\|P_\alpha-Q_\alpha\|_1
=\|\mathcal P(P-Q)\|_1
\le\|P-Q\|_1,
\]

其中 (mathcal P(X)=\sum_\alpha\Pi_\alpha X\Pi_\alpha) 是 pinching。
稿中用 (Z=\operatorname{sgn}(\mathcal P(X))) 的对偶证明正确：(Z) 本身
block-diagonal 且 (|Z|_{\mathrm{op}}\le1)，于是
(operatorname{tr}(Z\mathcal P(X))=operatorname{tr}(ZX)le\|X\|_1)。

把这个局部项与 outside-law 项相加，正好得到稿中 (49)。这同时比较了
(K,L) 与 (P,Q)，并且控制了 (P,Q) 的全部 cross-block 差异；证明没有
错误地把它们先删除再以较小范数替代。

## 7. 零权重、Borel 与分块置换协变

当 (w_\alpha=0) 时相应分量定义为零，而

\[
\|w_\alpha G_{K_\alpha,R_\alpha}\|_1=w_\alpha\to0.
\]

更强地，第 4 节的齐次估计给出关于 ((K_\alpha,P_\alpha)) 的连续性，所以
归一化 (R_\alpha=P_\alpha/w_\alpha) 即使没有极限，也不会破坏 Borel 性。
outside DPP atoms 关于核连续，因此每个全局边坐标连续，特别是 Borel。

若坐标置换把给定分块送到重标记后的分块，局部 fiber 被等距双射到相应局部
fiber。Euclidean norm 与 least-norm 点的唯一性保证局部 (G) 协变；块权重
和 outside product law 也按同一置换重标记。因此全文 (52)--(55) 的协变
论证完整。

## 8. 最终边界

- cross-block (P) 项在 block-diagonal (K) 的原子导数中严格消失：通过；
- 精确散度、非负性、单位质量、原点态容量：通过；
- 小权重齐次估计与零权重退化：通过；
- trace-norm pinching 与 outside weighted sum：通过；
- simultaneous ((K,P)) 估计及仅依赖 ((\varepsilon,r)) 的常数：通过；
- Borel 与 supplied-partition permutation covariance：通过。

最终状态为 **PASS**。认证范围严格限于统一有界、预先给定的 block-diagonal
分解；它不证明 unrestricted non-diagonal selector，不提供 (r\to\infty) 的
统一常数，也不涉及新颖性认证。

