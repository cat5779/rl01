# S74 Cycle26 独立数学审查

审查日期：2026-09-20（Asia/Singapore）

## 总裁决

**`VERIFIED_ANALYTIC_CORE / AUTHOR_INTERVAL_CERTIFICATE_REPLAYED / PAID_REGION_VALID_BUT_EXTREMELY_NARROW / MAIN_TARGET_INCOMPLETE`。**

正文的承重解析链通过独立验缝：cofactor 分部积分、条件 odds 表示、梯度算子范数、pinching/sign-conjugation cut 插值、无维度的二次 cut bound、相邻 merge tree 的单次收费、有限体积积分后再取熵值极限的弦桥，以及极稀疏/极稠密产品区域的显式常数，均成立。

需要一项正文级表述修补：`F_N` 在 (22) 前没有定义。全部后续符号只有在

\[
F_N(a):=-H_N''(a)
\]

时一致。按此定义，(22)–(25) 的方向和系数正确；这是缺失定义，不是证明断裂。

补交的 `certify_mixed.py` 已完成静态安全审查并实际执行，退出码 0。由于作者源码把输出硬编码到 Linux 路径，本审查只重定向这一写出动作到系统临时文件，区间算术源码保持原样。重放 JSON 与补交的 `certificate.json` 逐字段完全一致。

作者程序的 65 位定点区间运算符合外向取整要求：有理数、乘法、倒数和除法分别向下/向上包围；Machin 公式的两个 arctan 使用交错级数下一项余项；log 先缩放到 \([1,2]\)，再使用 atanh 正项级数及

\[
\frac{2z^{171}}{171(1-z^2)}
\]

尾界。division-free subset recurrence 对每个 determinant 做区间传播。程序在基点和整个 \([0,10^{-10}]^2\) diagonal rectangle 上各枚举 64 个 atoms，并逐个断言严格正；矩形输入使用 interval diagonal，因依赖丢失只会扩大包围，不会漏掉参数点。

精确重放得到

\[
\mathcal M_{uv}(0,0)approx-0.00037909224204168601326327,
\]

\[
D_F\approx32.59075196032424485594,
\quad C_{\rm acc}\approx-18.84098448997097910461,
\]

\[
M_{3,3}''\approx13.74976747035326575133.
\]

这些区间与正文完全一致。作者程序还统一证明整个小矩形上

\[
\mathcal M_{uv}(u,v)<-3/10000,
\qquad 0\le u,v\le10^{-10},
\]

从而 rectangle defect 小于 \(-3\times10^{-24}\)。独立 80 位 Decimal 重建和 SolA PR63 仍作为不同实现的交叉核对，而不再承担 exact interval 证书。

正文没有把有限 Toeplitz compression 当成投影，也没有把一个负的 mixed Hessian 元素误写成 common identity direction 反例。全 \((0.925,1)\)、全部密度和全部合法偏置仍开放。

## 分项裁决

| 对象 | 裁决 | 说明 |
|---|---|---|
| cofactor 一、二阶恒等式 | CORRECT | 对角二阶为零，交叉二阶是删除两坐标的真实 marginal |
| (5) cofactor IBP | CORRECT | common identity 二阶导给出有序交叉项的两倍 |
| (7) acceleration 的 \(W-W_0\) 表示 | CORRECT | block 内 marginal reference 保留，cross-block marginal 差分为零 |
| masked resolvent gap | CORRECT | \(\frac12\operatorname{diag}s+(K-I/2)\) 的最小奇异值至少 \(\delta\) |
| 条件 odds 与 \(b_i\) 界 | CORRECT | 原 word 和 flip word 各给出 \(q_i\ge\delta\)、\(1-q_i\ge\delta\) |
| (10) \(W\) 的 odds 表示 | CORRECT | 同 bit 用 odds ratio，异 bit 用其倒数，\(\sigma\) 恰好修正方向 |
| (14) 梯度算子范数 | CORRECT | off-diagonal 主项、三次 remainder、diagonal 项都无尺寸因子 |
| cut interpolation | CORRECT | 是核插值，由 sign conjugation 的凸组合保 gap；不是概率律混合 |
| (15)–(19) 二次 cut bound | CORRECT | diagonal trace-norm 和 cross HS-norm 配对系数正确 |
| \(B_\delta\le6\delta^{-12}\) | CORRECT | 直接代入 \(r\ge\delta\)，最坏系数小于 6 |
| merge-tree 总收费 (21) | CORRECT | 每个不同叶的无序 pair 只在最低共同祖先 cut 收费一次 |
| finite seed 到 rate chord | CORRECT_WITH_DEFINITION_REPAIR | 需先定义 \(F_N=-H_N''\)；积分罚系数为 cost 的一半 |
| leakage 公式与上界 | CORRECT | 使用无限符号 Parseval；有限 \(Q_{\rho,N}\) 仍仅为 contraction |
| 一点 seed 区域 (28) | CORRECT | 对每个固定 \(c,\rho\) 和固定正 gap 紧区间成立 |
| 产品区域 (29)–(30) | CORRECT_EXACT | \(\delta=1/50\)，\(\kappa_1\ge27353/8192\) |
| 半密度两点 seed 预算 | CORRECTLY_FAILS_THIS_BUDGET | 只说明最坏 word 常数过贵，不说明 rate concavity 失败 |
| 六点 mixed coordinate 负号 | VERIFIED_EXACT_INTERVAL | 作者整数定点区间程序已由审查者执行，基点及整个小矩形均通过 |
| 六点 \(C_{\rm acc}<0\)、\(M''>0\) | VERIFIED_EXACT_INTERVAL | 输出区间与下载证书、独立实现和 PR63 一致；不是 common-direction 反例 |
| 全高对比度、任意 \(\rho\) | INCOMPLETE | 已证区域的密度宽度约 \(\delta^{12}\)，极窄 |

## 1. 冻结对象与证据边界

完整读取 `S74_VISIBLE_RESULT.md` 全部 783 行。正文正常结束于 §7 final ledger，没有截尾。初审时附件缺失；随后收到承重的 `certify_mixed.py` 与 `certificate.json`，现已补做安全审查和实际重放。

本审查采用以下证据分层：

1. 正文中可逐式复核的一般证明，独立判断正确性；
2. 作者整数定点 interval checker，认证 §6 的严格区间和小矩形 uniform sign；
3. 自行编写的标准库程序，复核有理常数、merge identity 和六点中心值；
4. SolA PR63 只用于交叉核对同一六点基点的 \(D_F,C_{\rm acc},M''\) 数值，不把其浮点扫描升级为区间证明。

S73 不作为 S74 的证明输入。S71 只提供任务明确允许接受的 common identity Fisher inequality \(D_F\ge0\)。

## 2. Cofactor IBP 与 acceleration 表示

实际 DPP atom 可写成 masked determinant。沿单个对角坐标求导，cofactor 正是删除该坐标后的实际 marginal，因此

\[
\partial_iP_K(y)=s_iP_{K_{-i}}(y_{-i}),
\]

\[
\partial_i\partial_jP_K(y)
=s_is_jP_{K_{-\{i,j\}}}(y_{-\{i,j\}}),\quad i\ne j,
\]

且 \(\partial_i^2P=0\)。common identity 二阶导为所有 \(i\ne j\) 项之和，于是对冻结的 \(g\)，

\[
\sum_yP''(y)g(y)=2\sum_{i<j}\mathbb E\Delta_{ij}g.
\]

令 \(\ell=\log P_K-\log P_{K_A}-\log P_{K_B}\)。对同一 block 内的 pair，\(\Delta_{ij}\ell\) 保留 joint conditional odds 减 marginal conditional odds；对 cross-block pair，两个 marginal 项的 mixed difference 为零。block diagonal 核 \(K^{(0)}=K_A\oplus K_B\) 的 \(W\) 正好收集两个 marginal odds。因此

\[
C_{\rm acc}=2\mathbb E_{P_K}[W(K,Y)-W(K^{(0)},Y)]
\]

成立，没有丢弃 moving marginal reference。

## 3. 条件 odds 与梯度界

masked matrix 为

\[
K-\operatorname{diag}(1-y)
=\tfrac12\operatorname{diag}(s)+(K-I/2).
\]

第一项的全部奇异值为 \(1/2\)，第二项算子范数至多 \(1/2-\delta\)，所以 inverse 的算子范数至多 \(\delta^{-1}\)。

由 cofactor 比值

\[
R_{ii}=s_i/q_i,
\]

原 word 给出 \(q_i\ge\delta\)，flip word 给出 \(1-q_i\ge\delta\)。于是

\[
r\le b_i=(1-q_i)/q_i\le r^{-1},
\qquad r=\delta/(1-\delta).
\]

两次 determinant lemma 给出 pair rectangle ratio。若 bits 相同，它就是 conditional odds ratio；若 bits 不同，它是 reciprocal。故

\[
W(K,y)=\sum_{i<j}\sigma_{ij}
\log(1-\sigma_{ij}x_{ij})
\]

且 denominator 统一不小于 \(r^2\)。

梯度 off-diagonal 项分成

\[
-\operatorname{offdiag}(DRD)
\]

和 remainder。前者算子范数至多 \(2r^{-2}\delta^{-1}\)。remainder 每项至多 \(r^{-6}|R_{ij}|^3\)，而

\[
\sum_j|R_{ij}|^3
\le\max_j|R_{ij}|\sum_j|R_{ij}|^2
\le\delta^{-3}.
\]

Hermitian row-sum bound因此给出 \(r^{-6}\delta^{-3}\)。diagonal 项由 row-square bound 给出 \(r^{-5}\delta^{-2}\)。三项合计正是 \(L_\delta\)，不含 block size。

复方向没有遗漏：对 Hermitian differential，两个 off-diagonal trace 项组合成所需的 \(2\operatorname{Re}(\overline{R}_{ij}dR_{ij})\)。

## 4. Cut interpolation 与二次依赖

令 \(U=I_A\oplus(-I_B)\)。则

\[
K_t=K_A\oplus K_B+tE
=\frac{1+t}{2}K+\frac{1-t}{2}UKU^*.
\]

两个端点有相同 contraction gap，凸组合保持 gap。这是 kernel path，不是 endpoint probability laws 的 affine mixture。

block resolvent 方程给出

\[
\|(R_t)_{AB}\|_{HS}\le t\delta^{-2}\|X\|_{HS}.
\]

再由 \(R_t'=-R_tER_t\)，两个 diagonal blocks 的 trace-norm 总和至多 \(4t\delta^{-3}\|X\|_{HS}^2\)，cross block HS-norm 至多 \(\delta^{-2}\|X\|_{HS}\)。同时

\[
\|(G_t)_{AB}\|_{HS}
\le tr^{-4}\delta^{-2}\|X\|_{HS}.
\]

diagonal 以 operator/trace norm 配对，cross block 以 HS norm 配对，得到

\[
\left|\frac d{dt}W(K_t,y)\right|
\le t(4L_\delta\delta^{-3}+2r^{-4}\delta^{-4})\|X\|_{HS}^2.
\]

积分后再乘 (7) 的因子 2，恰得

\[
|C_{\rm acc}|\le B_\delta\|X\|_{HS}^2.
\]

用 \(r\ge\delta\) 展开：

\[
B_\delta\le
8\delta^{-6}+2\delta^{-8}+4\delta^{-10}+4\delta^{-12}.
\]

括出 \(\delta^{-12}\) 后的系数在 \(0<\delta\le1/2\) 上小于 6，所以正文常数成立。

## 5. Merge tree、leakage 与弦系数

对相邻叶的任意 binary merge tree，每一对位于不同叶的无序 sites 只在最低共同祖先处分居 cut 两侧。因此

\[
\sum_{\rm merges}\|K_{AB}\|_{HS}^2
=\frac{c^2}{2}
[\operatorname{tr}Q_{\rho,qL}^2-q\operatorname{tr}Q_{\rho,L}^2].
\]

这里的 \(1/2\) 正好把 trace-square 中的两个方向变成一个无序 pair，没有逐 scale 重复收费。

正文应在此显式定义 \(F_N=-H_N''\)。由

\[
M''=F_{A\cup B}-F_A-F_B
\]

和 cut bound 才得到 (22)。若 pointwise cost 为 \(C\)，积分成弦时罚项为 \(C\lambda(1-\lambda)\Delta^2/2\)，所以 (22) 中的 \(B c^2/2\) 在 entropy gap 中变成 \(B c^2/4\)；正文系数正确。

有限 sine compression 没有被当成投影。正文只使用

\[
\frac1N\operatorname{tr}Q_{\rho,N}^2\to\rho,
\]

它来自 Toeplitz 系数平方和与无限 Fourier indicator 的 Parseval。除以 \(qL\) 后，trace difference 的极限是

\[
\rho-\operatorname{tr}Q_{\rho,L}^2/L
=D_{\rho,L}/L.
\]

因此 (24)–(25) 的 leakage 系数无误。整个过程先在有限体积积分，再使用 \(H_N/N\) 的熵值极限；没有求 \(H_N''/N\) 的极限，也不需要 \(h\in C^2\)。

## 6. 极稀疏/极稠密高对比度区域

一点 marginal 参数是 \(t=a+c\rho\)，故

\[
F_1=1/[t(1-t)]\ge4,
\qquad D_{\rho,1}=\rho(1-\rho).
\]

由 \(B_\delta\le6\delta^{-12}\)，

\[
\kappa_1\ge4-3c^2\delta^{-12}\rho(1-\rho).
\]

因此 (28) 的 strict condition 确实给出正 chord coefficient。量词是：先固定 \(c,\rho\) 和 compact legal \(J\)，以该 \(J\) 的统一 gap \(\delta\) 得到其内部全部 chords；它不是端点一致或全部 legal biases 的结论。

在产品区域 (29)，对所有参数统一可取

\[
\delta_{\rm uniform}=1/50\le\min\{a,1-a-c\}
\]

作为统一下界；各点实际 gap 不小于 \(1/50\)，最坏角点达到该值。又

\[
\rho(1-\rho)\le\min(\rho,1-\rho)\le10^{-21}.
\]

精确计算得到

\[
4-3(19/20)^2 50^{12}10^{-21}
=27353/8192,
\]

故弦系数为 \(27353/16384\)。该产品区域真实成立，但密度距 \(0\) 或 \(1\) 只有 \(10^{-21}\)，应保持 `PROVED, NARROW SCOPE`。

## 7. 半密度两点 seed 的预算失败范围

独立重算

\[
B_{1/50}=865433616303812500000
\]

以及 \(c=19/20\) 的 (31)，得到

\[
\kappa_2\approx-5.8063080125817152161\times10^{19}.
\]

这与正文一致。更一般地，在高对比度合法参数内，最大可用 gap 小于 \(3/80\)，正文给出的粗下界已足以说明该**特定**两点 seed 加最坏 word 常数无法支付 leakage。

该失败只限定这一预算组合。它没有证明半密度 rate curvature 为负，也没有排除更强 seed、Fisher–acceleration cancellation 或更便宜的平均常数。正文明确保留了这个边界，处理正确。

## 8. 六点 mixed coordinate 与 common direction

作者 interval checker 已标记 `EXECUTED_BY_REVIEWER`。其 `IV` 类型以整数端点表示 \(10^{-65}\) 网格：`//` 产生下界，`ceildiv` 产生上界；负区间倒数先取正后反号，四端点乘法覆盖符号变化。所有除法点均先由 atom positivity 或 \(z<1\) 断言排除零。

Machin \(\pi\) 包围包含在相邻的第 55 位小数端点内。`log_iv` 利用 log 单调性分别计算输入区间两端；每个端点缩放至 \([1,2]\)，atanh 展开只累加正项并把几何尾上界加到上端。行列式用 subset Laplace recurrence，无除法和 pivot 分支。

`atoms(6)` 对全部 64 个基点 atoms 逐个断言下端大于零并验证总质量区间包含 1。`atoms(6,rect=True)` 把第 1、6 个 diagonal coordinates 各替换为 \([0,10^{-10}]\) 增量，再次对全部 64 个 interval atoms 做同样检查。由这些 atom 区间生成的 marginal cofactor 导数、Fisher 项和 log 项虽有 dependency overestimation，但仍包含每个共同参数点，因此 uniform mixed bound 有效。

本审查另从实际六点半密度 sine kernel 重新枚举 64 个 atoms，用 cofactor marginals 计算 \(\partial_1P,\partial_6P,\partial_1\partial_6P\)，得到相同中心值。独立实现中的最小 atom 约 \(2.02609\times10^{-4}\)。

同一独立实现重建 common identity 分解，数值与作者区间及 PR63 同一点结果一致。证据关系必须保持：

- 负的 \(\mathcal M_{uv}\) 只否定“每个 mixed diagonal 元素都非负”；
- \(C_{\rm acc}<0\) 说明 acceleration 本身不可要求非负；
- 同一点 \(D_F+C_{\rm acc}>0\)，所以它不是 \(M''<0\) 或 common identity convexity 的反例；
- directed interval checker 承担严格符号；80 位 Decimal 与 PR63 只承担跨实现核对。

## 9. 精确剩余义务

1. 把 worst-word \(B_\delta\) 替换为能利用输出平均、局部 cut 结构或 Fisher cancellation 的可支付常数。
2. 在固定正密度，特别是 \(\rho=1/2\)，找到满足
   \[
   f_L>B_\delta c^2D_{\rho,L}/2
   \]
   的 seed，或证明更强的直接 rate chord inequality。
3. 覆盖 \(74/77<c<1\) 以及一般 \(\rho\) 时，不能把当前极窄 density theorem 写成全高对比度结论。
4. 保持对象边界：有限 Toeplitz compression 是 contraction；negative mixed coordinate 不是总方向反例。

最终状态：**S74 证明了一个真实、全尺寸、无维度但常数极保守的 acceleration cut bound，并把累计成本精确压到 leakage；它由此得到一个正确但极窄的 rate-concavity 产品区域，没有解决原全区间问题。**
