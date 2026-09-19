# S67 Cycle17 独立数学审查

审查日期：2026-09-19（Asia/Singapore）

## 总裁决

**`VERIFIED_SCOPED / MAIN TARGET INCOMPLETE / ARTIFACT REPAIRS REQUIRED`。**

完整读取并审查 `S67_ACCELERATION_RESULT.md`、可见回复、四个程序和全部随稿记录后，没有发现推翻 S67 scoped theorem 的数学错误。以下链条成立：

1. full-configuration acceleration 的 Green 表示保留 actual exterior 权重；
2. 条件 odds 有界时二元表满足 `J <= 3W/2`；
3. L-ensemble Loewner/likelihood transport 在相同条件化下成立；
4. signed-resolvent 恒等式保留有限压缩 leakage 的有利符号；
5. local-score Fisher 的条件投影和 half-density 三点解析下界正确；
6. 两个边界站点给出的有限修正恰为 `beta3/n`；
7. diagonal-only 固定分配架构存在严格 floor；
8. weighted inverse locality 给出有效但常数极差的有限窗口判据；
9. pointwise 与逐 pair actual-law average 的 factor-one 比较都被真实 sine DPP 反例严格推翻。

重算得到

\[
U_3\in[0.00084887490360597234118593986866945,
        0.00084887490360597234118593986866946],
\]

\[
\limsup A_{16\,2^N}\le U_3-c_{16}
<0.000702194423281.
\]

但 `gamma16+B16` 只有约 `0.000245932000396`，等价地

\[
U_3-C_*>0.000456262422884.
\]

因此 benchmark entropy-rate chord、整个 `[.02,.03]` 区间和全参数目标仍为 **INCOMPLETE**。上界超过 cap 只说明当前证明架构未闭合，不是熵率凹性的反例。

本审查不认证外部新颖性。

## 逐项裁决

| 对象 | 裁决 | 说明 |
|---|---|---|
| acceleration Green identity | VERIFIED | pair 混合导数给 `-J_b`，期望始终按 `P_a` 加权 |
| binary `3/2` inequality | VERIFIED | `r,q` 归约、三次多项式临界点和指数级数门槛均通过 |
| conditional odds squeeze | VERIFIED | inverse compression 与 Schur complement 方向正确，`761/39<20` |
| actual/reference transport | VERIFIED | configuration law 比值为 `R^k`；pair 使用 `k=2` |
| signed-resolvent allocation | VERIFIED | `E_n=Q_n-Q_n^2>=0` 未被当成零 |
| three-site Fisher bound | VERIFIED | 四种外部配置全部进入，`D02+D1` 分解的分母与单调性正确 |
| Theorem S67-F | VERIFIED | local-score 的 `R^-2` 与 pair transport 的 `R^2` 抵消；边界因子正确 |
| diagonal-only obstruction | VERIFIED_SCOPED | 是该固定 allocation 的最好上界 floor，不是实际 acceleration 下界 |
| finite-window criterion | VERIFIED_SCOPED | locality/长 pair 尾方向正确；没有有限 certificate 支付巨大误差 |
| pointwise `J<=W` | DISPROVED | 四点裕量 `J-W>0.0007854799701615` |
| pairwise actual-law average `EJ<=EW` | DISPROVED | 六点 pair `(0,5)` 有 `EJ-EW>0.0003790922420416` |
| 六点 all-pair compensation | VERIFIED_SCOPED | `sum(EW-EJ)>5.0530794285`，不能外推到所有体积 |
| benchmark entropy-rate chord | INCOMPLETE | `U3-C*>0` |
| interval / universal objective | INCOMPLETE | 不由本次单弦工具推出 |

## 承重推导核对

### actual 权重与 `3/2` 比较

配置概率对各局部对角参数多仿射。对固定 reference `b` 的 `E_{P_a} log p_b` 求二阶导，得到

\[
f_n''(a)=-2\sum_{i<j}E_{P_{a,-ij}}J^b_{ij}.
\]

这里没有把 actual exterior law 换成 reference law。

对正二元表写 `r=BC/(AD)`、`q=A+D`，有

\[
W=(r-1)\{q+(1-q)/r\}.
\]

四个 one-bit conditional odds 落在 `[1/M,M]` 时，`q` 有显式下界。取 `M=20` 后只需验证 `phi(r)>=0`。审查重新核对了 `P,P',P''` 的符号结构、两个临界点区间和 `e^(7/4)>5.7` 的有理级数证书；证明闭合。

### 三点 Fisher 与边界

half-density 时中央点两侧邻点的互相 kernel entry 为零，所以 exterior 是两个独立 Bernoulli，四种配置的 exact local Fisher 为稿中 `d3(a)`。令 `x=(2p-1)^2<=10^-4` 后，`D02(x)` 不小于 `D02(0)`，而 `D1(x)>=2`，故

\[
d_3(a)\ge d_*=2+\frac2{1-64(c/\pi)^4}.
\]

完整 local score 的 Fisher 经条件 Jensen 不小于窗口 Fisher。reference/actual 单点条件概率 transport 给 `R^-2`；pair comparison 则支付 `R^2`。二者在 signed-resolvent 分配中消掉，因此 `n-2` 个三点窗口和两个单点边界产生

\[
\mathcal C_n/n\le U_3+\beta_3/n-\Lambda_n,
\qquad \beta_3=3(d_*-4)/80000.
\]

没有漏掉额外 `R^2`，leakage `Lambda_n>=0` 的符号也正确。

### 固定架构的 floor

actual 条件 odds ceiling 给所有窗口 Fisher 上界

\[
D_{\max}=2475^2/(97\cdot2378).
\]

在同一个 `kappa=3/2`、最坏 transport 和 square allocation 中，最优数值上界仍不小于

\[
0.0004691161822867465\ldots>C_*.
\]

又因 `tr(Q_n-Q_n^2)=O(log n)`、`||B||<=40`，归一化 leakage 渐近消失。因此单纯增大 local Fisher window 不能闭合这个固定架构。该结论不排除 signed compensation、改进 joint pair transport 或其他 finite witness 方法。

### locality 与有限窗口接口

signed matrix 的谱隙为 `1/40`。加权 commutator 的 Schur bound 小于 `1/80`，Neumann 估计给 weighted inverse norm `<80`，从而列尾平方不超过 `6400(1+L)^(-1/500)`。block inverse identity、条件二点核稳定性和全局 odds 下界随后给出 exterior discard error 与 long-pair tail。

该 reduction 在量词上有效，但 `1/500,1/1000` 的指数和 `6400,204800000` 的系数使现有普通窗口无法实际闭合。S67 明确保留了这一限制。

## 反例范围

四点反例证明某个条件外部配置下 `J>W`。六点反例进一步证明 pair `(0,5)` 在 reference actual exterior law 下仍有 `EJ>EW`。二者都来自完整 DPP 配置律，不是 count entropy 或循环替代。

但六点全部十五个 pair 的总和仍满足 `sum EW > sum EJ`。因此这些反例只杀死 factor-one 的逐配置/逐 pair 平均捷径，不是 entropy-rate concavity 的反例，也没有杀死跨 pair 补偿。

## 隔离复现

作者交付包的真实运行状态：

- rational core：留存 JSON 为 PASS，退出码 0；finalizer 正确声明它不是本轮 fresh run；
- bounds 的 128/192/256 位日志：全部因缺少 `flint` 退出 1；
- counterexamples 的 128/192/256 位日志：全部因缺少 `flint` 退出 1；
- small-model 浮点检查：退出 0，但不是严格证书。

本次在原始源码之外的临时副本安装 `python-flint 0.9.0`，完成：

- `verify_rational_core.py` 普通与 `-O`：PASS；
- `verify_s67_bounds.py` 128/192/256 位：PASS；192 位 `-O`：PASS；
- `verify_counterexamples.py` 128/192/256 位：PASS；192 位 `-O`：PASS；
- `check_small_models.py`：PASS；
- 独立标准库 80 位实现：PASS。

三组 192 位普通/`-O` JSON 分别逐字节相同。`-O` 只验证输出不依赖断言副作用，不替代普通模式的断言接受门槛。

按任务要求，S64/PR46 的 `n=15,16` finite KL core 与 QWE02 完整远尾接口直接接受，没有重跑无关计算。

## 交付物问题

1. 正文引用 `certificates/pair_counterexamples.json`，实际包中不存在；只有三个缺依赖失败日志。程序本次能成功生成相应 JSON，所以这是 artifact/provenance 缺件，不是反例错误。
2. 原包不能把 Arb 日志描述成成功证书；应保留成功输出、依赖版本和退出码。
3. `source_inventory.json` 标记 S64/PR46/QWE02 文件不在检查点内。单独分发时应把它们明确列为外部依赖。

## 发布

公开审查、机器可读结果与独立 replay 程序已置于 RL01 新分支 `review/s67-cycle17-20260919` 的 `research/INDEPENDENT_REVIEW_20260918/`，仅包含本次审查材料，不修改 S67 原稿、网页任务或仓库根状态文件。

