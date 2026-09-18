# QWE01 continuation 独立数学审查

日期：2026-09-18

审查对象：

- `QWE01_CONTINUATION_NOT_COMPLETED.md`；
- `exact_mixed_entry.json`；
- `rankone_fisher.py` 与 `fisher_hessian_search.py`；
- 原提交 `randomcat4/dpp-stationary-entropy` PR #122。

作者状态为 `INCOMPLETE`。本报告只裁决已经写出的有限恒等式、账本与中间反例，不把未完成路线提升为定理或主目标反例。

## 总裁决

- **主支付：INCOMPLETE。** 没有证明任务目标 (G_n\ge\varepsilon n-o(n))，没有找到能替代 (T_n) 并闭合真实 sine Toeplitz 完整 Hessian 的证书，也没有目标模型反例。
- **精确 block ledger：VERIFIED_SCOPED。** 完整熵 Hessian 分块后，跨块项确为
  \[
  2\sum_{\text{cross }i<j}
  \mathbb E(\Lambda_{ij}-\Gamma_{ij}).
  \]
  后验块计数方差与缺失 leakage 的恒等式支付同一份跨块 (\Gamma)，没有重复计费。
- **(C_B\) 到 marginal (H_B'') 的替换：OPEN。** 必须证明只改变块内 offset 时
  \[
  I(Y_B;Y_{-B})''\ge0.
  \]
  稿件没有证明，也没有暗称已证。
- **rank-one Fisher 展开：VERIFIED。** 沿 (K+t vv^*) 的完整配置 Fisher 量
  \(F_v=\sum_y p_y(v^*V_yv)^2\) 的共同平移二阶导及逐坐标 Hessian 公式均正确，概率权重导数没有遗漏。
- **对角 Hessian：VERIFIED。** 精确有
  \[
  (F_v)_{ii}=2\mathbb E|(Vv)_i|^4\ge0.
  \]
- **两点 mixed-entry 反例：VERIFIED_SCOPED。** 给定严格收缩二点 DPP 与 (v=(1,1)^T)，精确计算得到
  \[
  (F_v)_{12}
  =-\frac{7058578388000000}{3400782877756341}
  <-2.
  \]
  因此“每个混合 Hessian 元均非负”的通用中间规则为假。
- **反例不能升级。** 该核不是指定 sine 核；更重要的是，在同一精确例中
  \[
  (1,1)\nabla^2F_v(1,1)^T
  =\frac{1095440907576040000}{3400782877756341}
  >0.
  \]
  所以它甚至不反驳该例的共同平移凸性，更不反驳 QWE01 的实际平均支付。
- **浮点搜索：DIAGNOSTIC ONLY。** 复跑找到负 off-diagonal entries 和负 Hessian eigenvalues，也未在所采样的共同方向中找到负值；两者都不是区间证书或一般定理。
- **作用域陈述：CORRECT。** 作者明确区分“否定一个通用逐项 ansatz”与“否定 sine 目标”，没有把有限搜索包装成证明。

建议仓库状态：

> **exact block ledger and Fisher differential formulas: VERIFIED_SCOPED; entrywise mixed-Hessian positivity: DISPROVED; common-shift convexity, sine payment, and main QWE01 target: OPEN / INCOMPLETE.**

## 1. 分块熵 Hessian 账本

令 (B_1,\ldots,B_s) 是不重叠坐标分割，

\[
C_B=\sum_{i,j\in B}
\partial_{a_i}\partial_{a_j}H(Y).
\]

只改变 (B) 内的 diagonal offsets 时，外部 marginal kernel
\(K_{-B,-B}) 不变，所以外部输出 law 不随这些参数变化。因此 (C_B) 可解释为实际外部 law 下 conditional block entropy 的共同方向二阶导，未漏外部测度导数。

对完整配置 (y)，

\[
M_y=K-D_{1-y},\qquad V_y=M_y^{-1},
\]

\[
p_y=(-1)^{n-|y|}\det M_y.
\]

Jacobi 公式给

\[
\partial_{a_i}p_y=p_y(V_y)_{ii},
\]

以及 (i\ne j) 时

\[
\partial_{a_i}\partial_{a_j}p_y
=p_y\bigl((V_y)_{ii}(V_y)_{jj}-|(V_y)_{ij}|^2\bigr).
\]

对所有配置求和并使用概率归一化，得到

\[
\mathbb E(V_Y)_{ii}(V_Y)_{jj}
=\mathbb E|(V_Y)_{ij}|^2.
\]

在冻结 midpoint dictionary 中，右端正是 (\mathbb E\Gamma_{ij})。完整 Shannon 熵的混合导数为

\[
\partial_{a_i}\partial_{a_j}H
=\mathbb E\Lambda_{ij}-\mathbb E\Gamma_{ij}.
\]

因此

\[
\boxed{
H_n''=\sum_BC_B
+2\sum_{\text{cross }i<j}
\mathbb E(\Lambda_{ij}-\Gamma_{ij}).}
\]

这里 (i<j) 的跨块 unordered pair 在共同方向 Hessian 中带因子 2，系数正确。

## 2. 后验方差支付与剩余接口

同一完整后验中，projection-DPP covariance 为

\[
\operatorname{Cov}(X_i,X_j\mid Y)
=-|R_{ij}|^2,qquad i\ne j.
\]

把每个块内的 posterior count variance 求和，并与全局 leakage 分解比较，得到

\[
\sum_Be^2\mathbb E\operatorname{Var}(|X_B|\mid Y)
-E_{\rm miss,n}
=2\sum_{\text{cross }i<j}\mathbb E\Gamma_{ij}.
\]

若使用已给分支 (\Lambda\le(7/4)\Gamma)，则

\[
\begin{aligned}
H_n''
&\le\sum_BC_B
+\frac32\sum_{\text{cross }i<j}\mathbb E\Gamma_{ij}\\
&=\sum_B\left[C_B+rac34e^2
  \mathbb E\operatorname{Var}(|X_B|\mid Y)\right]
-\frac34E_{\rm miss,n}.
\end{aligned}
\]

因此计数方差只使用一次，没有对每块重复支付同一跨块边。

然而

\[
H(Y)=H(Y_B)+H(Y_{-B})-I(Y_B;Y_{-B}),
\]

且只改变块内参数时 (H(Y_{-B})) 为常数，故

\[
C_B=H_B''-I(Y_B;Y_{-B})''.
\]

要推出 (C_B\le H_B'')，确实需要互信息二阶导非负。该接口仍未证明，是账本到局部块定理之间的真实缺口。

## 3. Reveal 比较与 rank-one Fisher 条件

揭示块外一位 (Y_k) 前，块核为 (A)，记

\[
q=\Pr(Y_k=1),\qquad v=K_{B,k}.
\]

揭示后条件核为

\[
A_1=A-vv^*/q,
\qquad
A_0=A+vv^*/(1-q),
\]

且

\[
qA_1+(1-q)A_0=A.
\]

块内共同 diagonal shift 不改变 (q,v)。若核泛函 (K\mapsto H''(K)) 沿该 rank-one 直线凹，则一次 reveal 的 conditional average 不超过未 reveal 值，从而得到所需观察比较。

沿 (K_t=K+t vv^*)，matrix determinant lemma 使每个完整原子 (p_y(t)) 关于 (t) 仿射。于是

\[
\partial_t^2H(K_t)=-F_v(K_t),
\]

其中

\[
F_v(K)=\sum_yp_y(v^*V_yv)^2.
\]

因此 (H'') 的 rank-one 凹性可由 (F_v(K+aI)) 关于共同 shift (a) 的凸性推出。作者没有把这个充分条件误写成已证事实。

## 4. 共同 shift 二阶导

令

\[
s=\operatorname{Tr}V,
\quad u=v^*Vv,
\quad z=v^*V^2v,
\quad w=v^*V^3v.
\]

共同 diagonal shift 下

\[
p'=ps,qquad
p''=p(s^2-\operatorname{Tr}V^2),
\]

\[
u'=-z,qquad u''=2w.
\]

对 (pu^2) 完整微分两次，得到

\[
\boxed{
F_v''=mathbb E\left[
(s^2-\operatorname{Tr}V^2)u^2
-4suz+2z^2+4uw
\right].}
\]

交叉项 (-4suz) 和概率加速度项均已保留。该表达式本身没有明显符号，不能从各原子正性推出期望正性。

## 5. 逐坐标 Fisher Hessian

令

\[
W=Vv,qquad d_i=V_{ii},qquad z_i=|W_i|^2.
\]

使用

\[
\partial_i p=pd_i,
\quad
\partial_{ij}p=p(d_id_j-|V_{ij}|^2),
\]

\[
\partial_i u=-z_i,
\quad
\partial_{ij}u
=2\operatorname{Re}(\overline{W_i}V_{ij}W_j),
\]

可得 (i\ne j)

\[
\begin{aligned}
(F_v)_{ij}=\mathbb E\big[{}&
(d_id_j-|V_{ij}|^2)u^2
-2u(d_iz_j+d_jz_i)\\
&+2z_iz_j
+4u\operatorname{Re}(\overline{W_i}V_{ij}W_j)
\big].
\end{aligned}
\]

对角方向中，(p) 对每个单独 diagonal entry 仿射，全部交叉项精确抵消，留下

\[
\boxed{(F_v)_{ii}=2\mathbb E|W_i|^4\ge0.}
\]

但 Hessian 的对角非负不蕴含 mixed entries 非负，也不蕴含整个 Hessian PSD。

## 6. 二点精确反例

取

\[
K=\begin{pmatrix}1/5&1/10\\1/10&3/5\end{pmatrix},
\qquad v=(1,1)^T.
\]

有

\[
\det K=11/100>0,
\qquad
\det(I-K)=31/100>0,
\]

且对角均严格位于 ((0,1))，所以 (0\prec K\prec I)，附近 rank-one 扰动合法。

按 (00,10,01,11) 排列，稿件列出的 (p,q,p_1,p_2,p_{12},q_1,q_2) 全部由 determinant lemma 精确复算。逐原子使用

\[
\partial_{12}(q^2/p)
=\frac{2q_1q_2}{p}
-\frac{2q(q_1p_2+q_2p_1)}{p^2}
+\frac{2q^2p_1p_2}{p^3}
-\frac{q^2p_{12}}{p^2}
\]

得到

\[
(F_v)_{12}
=-\frac{7058578388000000}{3400782877756341}
=-2.0755745490\ldots<0.
\]

因此通用的 entrywise mixed nonnegativity 命题被严格反驳。

为防止扩大作用域，我另外精确计算同一例：

\[
(F_v)_{11}
=\frac{920389560512500000}{3400782877756341}>0,
\]

\[
(F_v)_{22}
=\frac{189168503839540000}{3400782877756341}>0,
\]

而共同方向为

\[
(F_v)_{11}+2(F_v)_{12}+(F_v)_{22}
=\frac{1095440907576040000}{3400782877756341}>0.
\]

Hessian determinant 在该例也为正。因此这个反例既不否定共同 shift convexity，也不否定 PSD；它只否定每个 mixed entry 必须非负。

## 7. 浮点搜索复现

两个脚本均原样运行。

`rankone_fisher.py` 在所采样的 projection、balanced contraction 与一般 contraction 中没有找到共同方向 (F_v''<0)；这是有限搜索空结果，没有证明力。

`fisher_hessian_search.py` 找到：

- 明显负的 off-diagonal Hessian entries；
- 若干负最小本征值；
- 负的 off-diagonal-entry 总和。

这些使用普通双精度随机核。它们可否定把 Hessian PSD 当作显然事实的研究直觉，但在没有区间或有理重建前，不应写成新的严格通用反例。现有两点有理例已经足够严格否定 entrywise nonnegativity。

## 8. 最终作用域

已验证：

1. 包含跨块项的完整 Hessian ledger；
2. posterior count variance 对跨块 (\Gamma) 的一次性支付；
3. block conditional curvature 与 marginal curvature 之间恰差一个 mutual-information curvature；
4. rank-one Fisher 共同 shift 及逐坐标 Hessian 的完整公式；
5. mixed entry 非负性的精确二点反例。

仍未完成：

- (I(Y_B;Y_{-B})''\ge0)；
- (F_v(K+aI)) 的共同 shift 凸性；
- 真实 sine posterior 平均下可能存在的 state-dependent 补偿；
- (G_n\ge\varepsilon n-o(n))；
- 完整 Shannon Hessian 或熵率凹性；
- 任何针对指定 sine 模型的反例。

因此 PR #122 作为 `INCOMPLETE` 研究记录是准确的。它保存了一个合法账本和一个严格的中间 ansatz 障碍，但没有完成 QWE01 主任务。
