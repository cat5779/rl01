# S64 Cycle11 独立数学审查

审查日期：2026-09-19

审查对象：`S64_CYCLE11_RESULT.md`、`S64_checks/` 全部证书与程序、冻结任务及指定的 QWE02/S42/S47 已审来源

## 总裁决

**总体：`VERIFIED_SCOPED / MAIN OBJECTIVE INCOMPLETE`。**

S64 的新承重工具成立：有限 Hermitian strict-contraction DPP 在 common diagonal shift 下，观测集合上的完整配置 KL 是 supermodular；其缺陷有显式非负 conditional log-determinant/HS 能量下界。对平稳过程，这严格推出 block KL 关于**长度**的离散凸性。因此，两个相邻有限体积 (D_{15},D_{16}) 能给出所有 (M\ge16) 的 KL 下界，而不是只给被枚举的 dyadic 尺度。

作者同时正确保留了完整熵弦分解中的 probability-acceleration 增量。当前没有其足够上界，所以 benchmark entropy-rate chord、固定区间凹性和整个合法区间凹性仍为 `INCOMPLETE`。

两种未经加权的 two-doubling window 单调性则被实际 half-density sine 模型严格证伪：同一主弦在相邻窗口上出现相反方向，第二条窄弦又在同一窗口比较处给出反号。这些反例只杀死原始窗口单调性，不杀死加权或带误差的 aggregate。

## 1. Common-shift likelihood ratio

### 裁决：VERIFIED

对 (K(a)=K_*+aI) 且 (0\prec K(a)\prec I)，固定其他坐标配置后，条件占用概率是

\[
q_i(a,z)=K_{ii}(a)-K_{iR}
(K_R(a)-D_{1-z})^{-1}K_{Ri}.
\]

原稿写成减去该逆矩阵项；对 (M_R=K_R-D_{1-z})，微分给

\[
q_i'=1+K_{iR}M_R^{-2}K_{Ri}\ge1.
\]

原子全支撑保证所需逆存在，Hermitian 性保证 (M_R^{-2}\succeq0)。于是

\[
\Delta_i\partial_a\log p_a
=\frac{q_i'}{q_i(1-q_i)}\ge4.
\]

积分后：若 (u>v)，occupation likelihood ratio 的每坐标 log-increment 至少 (4(u-v))；若 (u<v)，相同陈述转到 hole 坐标并保持正余量。对任意条件集 (Z=z)，条件归一因子不依赖剩余坐标，因此同一增量界仍成立。这里没有错误地声称条件核本身仍按 (aI) 平移。

## 2. 外场归一化乘积不等式

### 裁决：VERIFIED_SCOPED

Claim 3.1 的真正假设是：基础律在所有用到的正外场 tilt 后仍负相关；各 (r_j) 正、归一、依赖不交块，并满足 (Delta_i\log r_j\ge h\ge0)。令 (g_j=e^{-hN_{A_j}}r_j)，则 (g_j) 递增。整体 (h)-外场下，负相关给出不同块乘积期望不超过边缘期望乘积；从只倾斜 (A_j) 到再倾斜补集时，

\[
\frac d{dt}E g_j=\operatorname{Cov}(g_j,N_{U\setminus A_j})\le0,
\]

方向正确，因为两函数均递增且支撑不交。

对 strict Hermitian DPP，正外场在 L-ensemble 中变为

\[
L_t=D_{e^{t/2}}LD_{e^{t/2}}\succ0,
\]

从而仍对应 strict positive-contraction DPP。条件化也保持 determinantal 结构；holes 使用补核 (I-K)。Russell Lyons Theorem 8.1 的原始结论确实覆盖 positive contractions，并明确给出 conditional negative association with external fields，而非只覆盖投影。参见 [Lyons 原文](https://numdam.org/item/10.1007/s10240-003-0016-0.pdf)。

因此外部定理的类别、外场闭性及递增/递减方向均满足。负相关本身是经典输入；normalized-product 应用及其 common-shift 接口是本稿的新组合。

## 3. Conditional KL supermodularity

### 裁决：VERIFIED

对给定 (Z=z)，令 (Q=P_u(U\mid z))、(P=P_v(U\mid z))，并以各块边缘 likelihood ratio (r_j=Q_{A_j}/P_{A_j}) 构造归一化乘积律 (R)。精确恒等式

\[
D(Q\Vert P)-\sum_jD(Q_{A_j}\Vert P_{A_j})
=D(Q\Vert R)-\log E_P\prod_jr_j
\]

正确。上一节的乘积不等式控制第二项；(u<v) 时转到 holes，常数 ((-h)|A_j|) 因分块总大小相等而完全抵消。平均时使用的确是 moving actual endpoint law (P_u^Z)，再由 KL 条件链式法则得到

\[
D_V+(r-1)D_Z-\sum_jD_{Z\cup A_j}
\ge E_{P_u^Z}\mathcal B_v(Z;h)\ge0.
\]

没有把平均权重换成 (P_v^Z) 或计数律。

对定量下界，沿 (K_\theta=K_0+\theta E) 考察

\[
f(\theta)=-\log\det(I+tK_\theta).
\]

(f'(0)=0)，因为逆矩阵 block diagonal 而 (E) 只有 off-block；二阶导数是相似变换后 Hermitian 平方的迹。用 (I+tK_\theta\) 的最大特征值界得到

\[
\mathcal B_v(z;h)
\ge(1-e^{-|h|})^2
\sum_{i<j}\|(K_{v,U\mid z})_{A_iA_j}\|_{\rm HS}^2.
\]

系数及 HS 范数的因子二均核对正确。

## 4. 长度凸性及有限核外推

### 裁决：VERIFIED；不可推广到参数凸性

集合 supermodularity 取 (S=[1,n])、(T=[2,n+1])，平稳性给

\[
D_{n+1}-2D_n+D_{n-1}\ge0.
\]

所以增量 (d_n=D_n-D_{n-1}) 随长度不减，并且

\[
\frac{D_M}{M}\ge
\frac{D_m}{m}+\left(1-\frac mM\right)
\left(d_m-\frac{D_m}{m}\right),\qquad M\ge m.
\]

由此 (D_{15},D_{16}) 的认证值确实控制全部整数 (M\ge16)。推理只涉及 block length，不涉及 (a\mapsto D_n(a)) 的凸性，也不能单独交换无限体积极限与参数导数。原稿明确保留了这一边界。

## 5. 完整熵弦账本

### 裁决：VERIFIED_PARTIAL

原稿使用

\[
\operatorname{Gap}H_n=\mathcal D_n-\mathcal C_n,
\qquad \mathcal C_n\ge0.
\]

固定 reference (p_b) 没有冻结 endpoint 权重：两端仍分别由 (P_{a_0},P_{a_1}) 平均。对固定 (f)，common shift 下

\[
\frac d{da}E_{P_a}f=E_{P_a}Gf
\]

可在 multilinear monomial 基上直接验证；而 (log p_b(S)) 的 L-ensemble principal-minor 部分是 submodular，故其期望关于 (a) 凹，从而 (mathcal C_n\ge0)。

长度凸性给出的 retained-sum 界为

\[
\sum_{j<N}\frac{\operatorname{Gap}J_{m2^j}}{2m2^j}
\le
\frac{\mathcal C_M}{M}-\frac{\mathcal C_m}{m}
-\left(1-\frac mM\right)B_m.
\]

其中正 KL budget 与 determinant budget 都支付同一个
(mathcal D_M/M-mathcal D_m/m)，所以只能取两者最大值，不能相加。作者遵守了这一点。

仍未支付的是

\[
\mathcal C_M/M-\mathcal C_{16}/16.
\]

因此该式是严格缩小瓶颈的新工具，不是完整熵率凹性证明。

## 6. Sine determinant envelope

### 裁决：VERIFIED_SCOPED

对 (g(x)=\log(1+t(b+cx)))，凹性使其高于端点割线；二阶导数上界给偏差至多

\[
\frac{t^2c^2}{2d^2}x(1-x).
\]

求和后使用真实 sine compression 的精确 leakage

\[
\operatorname{Tr}(Q-Q^2)
=2\sum_{r\ge1}\min(r,M)
\frac{\sin^2(\pi\rho r)}{\pi^2r^2}
\le\frac2{\pi^2}(2+\log M),
\]

得到声明的 (O((2+\log M)/M)) envelope。它只控制 determinant/KL component，不替代 QWE02 的完整 entropy-chord tail。

## 7. 有限证书与独立复现

### 7.1 证书接口审计

整数区间以 (2^{-256}) 缩放，乘除、倒数均向外取整且除法前排除零。Machin 公式的两条 arctan 交错级数使用首个遗漏项界；log 经 (z=(v-1)/(v+1)\in[0,1/3)) 的 atanh 正级数和几何余项包围。公式的项数、奇偶方向和余项指数均正确。

条件 DPP recursion 在每个节点认证 (0<q<1)，两个 Schur 更新分别对应 bit 0/1。程序遍历全部 (2^n) 叶，检查总概率区间含一；因此 finite entropy 是全配置证书，不是抽样。

### 7.2 实际重算

在隔离副本中实际执行：

- `verify_s64.py --recompute`：重新生成所有主弦及第二弦的 entropy enclosures，再重做窗口符号和 (B_{16}) 推导；
- `certify_pair_atoms.py --n 15` 与 `--n 16`：独立从全部原子重新计算 KL、cross entropy 与 acceleration cost；
- `kl_budget_check.py`：重新计算 (n=1,2,4,8,16,32,64) 的 determinant budget。

重算结果包括

\[
B_{16}\in
[0.000104188037840358653653185471,
 0.000104188037840358653653185472],
\]

\[
D_{15}\in[0.004222178605379545187456418024,
0.004222178605379545187456418025],
\]

\[
D_{16}\in[0.004614791086101230763850243729,
0.004614791086101230763850243730].
\]

这些与随附 chain-rule 证书相交。未逐个重新运行 split-prefix 的 conditional-chain 子树，因为独立 atom 枚举已经重新覆盖同一 (n=15,16) 原始有限输入；其接口和根贡献组合则已静态复核。

## 8. 两窗口反例

### 裁决：DISPROVED（两个原始统一方向）；证书 VERIFIED

主弦参数正确为

\[
C_0:[0.02,0.03],\quad b=0.025,\quad\eta=0.005.
\]

全配置 entropy 区间重算后给出

\[
W_2(C_0)-W_1(C_0)>0,
\qquad
W_4(C_0)-W_2(C_0)<0.
\]

具体第二个差为

\[
[-1.56913645376612354441510\times10^{-7},
 -1.56913645376612354441509\times10^{-7}].
\]

因此“统一递增”和“统一递减”都失败。第二弦

\[
C_1:[0.02,0.021],\quad b=0.0205,\quad\eta=0.0005
\]

又在同一 (W_4-W_2) 比较给严格正号，排除把该窗口对的符号当作 chord-independent 规则。

反例针对真实 sine Toeplitz 全配置律，不是 count-only 或 cyclic substitute；但它不排除 weighted/almost-monotone aggregate，也不反驳 entropy-rate concavity。

## 9. 新颖性与项目分配

| 内容 | 判断 |
|---|---|
| positive-contraction DPP 的 conditional NA with external fields | 经典现成结果（Lyons） |
| common-shift likelihood 的每坐标 (4(u-v)) 余量 | 简洁但有用的有限参数引理 |
| conditional KL supermodularity + determinant/HS 缺陷下界 | 真正的新承重工具；外部新颖性尚未确认 |
| stationary block-KL 长度凸性 | 上述工具的直接新应用 |
| 两体积到所有更大体积的 KL envelope | 有效的新项目接口，不是参数凸性 |
| determinant leakage envelope | 经典 Fourier/leakage 技巧的有效应用 |
| (n=15,16) exact core | 新的模型专用有限证书 |
| raw two-window monotonicity反例 | 新的严格 scoped 障碍 |
| acceleration 上界 | OPEN；仍是下一轮承重任务 |

这会改变下一轮资源分配：无需继续寻找未加权窗口的统一单调方向，也无需枚举更多大体积来“观察” KL 增长。应集中攻击 acceleration increment 的可用上界，或设计能与其抵消的带权 aggregate。

## 10. 最终状态表

| 声明 | 裁决 |
|---|---|
| 全配置及条件 likelihood-ratio 单调性 | VERIFIED |
| 外场 normalized-product bound | VERIFIED_SCOPED |
| conditional KL supermodularity | VERIFIED |
| logdet/HS 定量缺陷系数 | VERIFIED |
| stationary block-KL 长度凸性 | VERIFIED |
| (D_{15},D_{16}) 向全部 (M\ge16) 外推 | VERIFIED |
| 参数 (a) 上的 KL/Fisher 凸性 | NOT CLAIMED / NOT IMPLIED |
| entropy chord 完整 moving-law 分解 | VERIFIED |
| retained signed-sum payment | VERIFIED_PARTIAL |
| 两个 KL budget 相加 | FORBIDDEN；作者正确只取最大值 |
| 主弦 (C_0=.02/.03,\eta=.005) 有限证书 | VERIFIED |
| 统一递增 two-window 规则 | DISPROVED |
| 统一递减 two-window 规则 | DISPROVED |
| benchmark entropy-rate chord | INCOMPLETE |
| fixed-interval / whole-interval concavity | INCOMPLETE |

## 最终意见

S64 值得作为 `VERIFIED_SCOPED` 的分配改变型结果接收。它把 retained signed sum 的 KL 部分从“未知跨尺度行为”提升为由两个有限输入控制的全体积解析预算，同时精确杀死了两个过强的窗口单调性候选。

它没有完成最终目标。后续任何汇总都必须保留 acceleration increment，不得将 KL 长度凸性误读为 entropy 长度凸性、参数凸性或完整 entropy-rate concavity。
