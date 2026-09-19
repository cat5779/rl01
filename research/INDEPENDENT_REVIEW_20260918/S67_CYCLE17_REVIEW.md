# S67 Cycle17 独立数学审查

审查日期：2026-09-19（Asia/Singapore）

## 结论先行

**总裁决：`VERIFIED_SCOPED / MAIN TARGET INCOMPLETE / ARTIFACT REPAIRS REQUIRED`。**

S67 的承重数学链条在其明确范围内成立：

- 实际律权重下的 acceleration Green 表示正确；
- 有界条件 odds 的二元表比较 `J <= 3W/2` 成立；
- reference 到 actual 条件律的 Loewner/likelihood transport 没有冻结错权重；
- signed-resolvent 恒等式保留了有限压缩 leakage 的有利符号；
- 三点 local-score Fisher 下界和有限边界项给出 `Theorem S67-F`；
- pointwise `J <= W` 与逐 pair 实际律平均版都被真实 sine DPP 反例严格推翻；
- diagonal-only 固定分配架构存在严格数值下限，单纯扩大 Fisher 窗口不能闭合；
- 加权 inverse locality 给出的有限窗口判据在明示巨大误差常数下有效。

严格重算得到

\[
\limsup A_{16\,2^N}\le U_3-c_{16}
<0.000702194423281,
\]

但可用预算只有

\[
\gamma_{16}+B_{16}\approx0.000245932000396,
\]

等价地 `U3` 仍比所需 `C*` 高约 `0.000456262422884`。因此 benchmark 熵率弦、整个 `[.02,.03]` 区间以及全参数目标都仍是 **INCOMPLETE**。这不是目标的反例，只是本证明架构未支付缺口。

没有发现阻断上述 scoped theorem 的数学错误。交付物有两项需要修复的复现问题：正文引用了不存在的 `certificates/pair_counterexamples.json`；作者保留的六个 Arb 日志实际都是缺少 `flint` 的退出码 1。二者不改变本次结论，因为审查者在隔离环境重跑了全部程序并发布独立复现材料，但原包不能宣称 Arb 证书已经在作者环境成功执行。

本审查不认证外部新颖性。

## 1. 审查范围与接受输入

完整读取并审查：

- `S67_ACCELERATION_RESULT.md`；
- `README.md` 与可见回复；
- 四个程序及全部随稿 JSON、日志和退出记录；
- `source_inventory.json`；
- 已审 [S64 Cycle11 / PR46](https://github.com/cat5779/rl01/pull/46) 的 KL 长度凸性和 `(D15,D16)` 外推接口。

按任务约束，没有重跑 S64 的 `n=15,16` 全原子计算，也没有重做无关的早期 QWE 工作。接受的外部接口只有：

\[
\mathcal D_M/M\ge\mathcal D_{16}/16+(1-16/M)B_{16},\qquad M\ge16,
\]

以及有限 stopping volume 中完整的 `T_QWE(M)` 熵弦远尾。没有把 determinant tail 当成完整远尾，也没有使用 S63 或 S68。

## 2. 逐结论裁决

| 原稿结论 | 裁决 | 独立核对 |
|---|---|---|
| 有限维 acceleration 的 Green 表示 | **VERIFIED** | 从 multiaffinity 对两个局部对角参数求混合导数，得到 `f_n''=-2 sum E_actual J_ref`；actual exterior 权重保留 |
| Theorem 4.1：有界 odds 下 `J <= 3W/2` | **VERIFIED** | 重建 `W=(r-1)(q+(1-q)/r)`、`q` 下界和 `phi` 的临界点结构；有理符号与指数级数门槛通过 |
| Lemma 5.1：条件 odds squeeze | **VERIFIED** | inverse compression、principal submatrix 与 Schur complement 的方向正确；benchmark 常数 `761/39 < 20` |
| Lemma 6.1：条件矩阵与 configuration likelihood transport | **VERIFIED** | Loewner 次序经删点/Schur 保持；路径导数 trace-norm 上界给 `R^k`，pair 使用 `k=2` |
| signed-resolvent 分配及 leakage | **VERIFIED** | 直接展开 `K=B^{-1}+D` 得到式 (7.1)；`E_n=Q_n-Q_n^2 >= 0` 没有被误删 |
| 三点 local-score Fisher 下界 `d3 >= d*` | **VERIFIED** | score projection、actual/reference 单点 transport、`D02+D1` 分解及全部分母符号核对通过 |
| Theorem S67-F 与边界系数 `beta3` | **VERIFIED** | `n-2` 个三点窗和两个单点边界正确；`R^-2` 与 pair transport 的 `R^2` 正好抵消，边界项为 `3(d*-4)/80000` |
| `U3` 数值、limsup bound 与未闭合差额 | **VERIFIED** | 标准库严格有理区间与 Arb 128/192/256 位结果一致；上界严格高于 cap |
| diagonal-only 固定分配架构 obstruction | **VERIFIED_SCOPED** | actual odds ceiling 给 `Dmax`；最优可得上界的 floor 严格高于 `C*`；不是对真实 acceleration 的下界 |
| compensated identity 与 revelation identities | **VERIFIED_SCOPED** | trapezoid remainder、`S''` 和 pair-bit 统一表示符号正确；原稿没有越界声称它已完成平均补偿 |
| 加权 inverse locality 与有限窗口 criterion | **VERIFIED_SCOPED** | spectral gap、commutator/Schur test、Neumann inverse 和长 pair 尾方向正确；误差常数巨大且原稿明确不声称已有数值 certificate |
| pointwise factor-one `J <= W` | **DISPROVED；反例 VERIFIED** | 四点 `(pair 0,3; exterior 1,0)` 有 `J-W > 0.0007854799701615` |
| 实际律逐 pair 平均 factor-one | **DISPROVED；反例 VERIFIED** | 六点 pair `(0,5)` 有 `EJ-EW > 0.0003790922420416` |
| 六点全部 pair 仍可补偿 | **VERIFIED_SCOPED** | `sum(EW-EJ) > 5.0530794285`；仅为该有限模型，不是全体积定理 |
| benchmark 熵率弦 | **INCOMPLETE** | `U3-C* > 0`，没有正 margin |
| 整个 benchmark 区间 / 全参数猜想 | **INCOMPLETE** | 单一 midpoint chord 的非闭合工具不能推出更强目标 |

## 3. 承重推导审查

### 3.1 实际律权重没有被冻结

对固定 reference `b`，令 `f_n(a)=E_{P_a} log p_b`。配置概率对每个局部对角参数都是多仿射的，因此 pair 混合导数只留下四格系数 `(1,-1,-1,1)`，给出 `-J_b`。把有序 pair 合并后，

\[
f_n''(a)=-2\sum_{i<j}E_{P_{a,-ij}}J^b_{ij}.
\]

再用弦的三角 Green 核积分得到 `C_n`。这里的外部配置始终按 `P_a` 加权，reference `b` 只出现在被评估的 log-likelihood 与条件表中；没有把 actual 权重偷偷换成 reference 权重。

### 3.2 二元表的 `3/2` 比较

令 `r=BC/(AD)`、`q=A+D`，则

\[
W=(r-1)\{q+(1-q)/r\}.
\]

四个单点条件 odds 位于 `[1/M,M]` 推出 `1 <= r <= M^2`，并给出 `q >= 2M/(M^2+2M+r)`。在 `M=20` 时问题归约为 `phi(r)>=0`。审查者重新核对了三次多项式 `P` 的符号、`P'` 的单调性、两个临界点区间及局部最小值的指数级数比较。端点 `r=1` 取零，局部最小值严格为正，之后 `phi` 递增；证明闭合。

这一定理只给 `3/2`，不支持被反例推翻的 factor-one 版本。

### 3.3 transport、resolvent 与三点 Fisher 的拼接

L-ensemble 的 Loewner 球在相同 absent/occupied 条件化下保持，configuration log-likelihood 的路径导数绝对值不超过 `k log R`。因此条件 pair 每格满足 `q_a >= R^-2 q_b`。与 `J_b <= 3W_b/2` 合并后，reference score square 在 actual exterior law下被 `R^2` 支付。

另一方面，score projection 是有限概率模型的条件 Jensen：完整 local score 的 Fisher 不小于任何保留该局部参数的窗口 Fisher。三点 half-density sine marginal 中，两邻点互相 kernel entry 为零，四种外部配置完整进入 `d3`；`D02(x)+D1(x)` 的分母在 `x <= 10^-4`、`.09 < tau < .092` 上均为正，两个部分给出

\[
d_3(a)\ge 2+\frac{2}{1-64\tau^2}=d_*.
\]

在 signed-resolvent trace 预算中，local-score transport 的 `R^-2` 与 pair transport 的 `R^2` 抵消。两个边界站点只用单点 Fisher `>=4`，于是有限边界修正正是

\[
\beta_3/n=\frac{3(d_*-4)}{80000n}.
\]

这一点是 S67-F 最容易出现多余 `R^2` 或漏掉边界因子的地方；原稿处理正确。

### 3.4 架构障碍的正确含义

actual 条件 odds 的统一上界给所有有限窗口 local diagonal Fisher

\[
d_m(a)\le D_{\max}=\frac{2475^2}{97\cdot2378}.
\]

代入同一个 `kappa=3/2`、最坏 likelihood transport 和 square allocation，任何只扩大窗口的改进都不能把该架构的数值上界降到 `C*` 以下。严格重算得到 floor

\[
0.0004691161822867465\ldots>C_*.
\]

有限压缩 leakage 除以 `n` 后趋零，因为 `tr(Q_n-Q_n^2)=O(log n)` 且 `||B||<=40`。所以 leakage 不能在该固定架构的渐近层面消除 floor。

原稿正确地把这称为“best bound within this allocation”的下限；它不是 `C_n/n` 的下限，也没有排除 signed compensation 或其他有限 witness 架构。

### 3.5 有限窗口 reduction

加权 inverse 证明先用 signed matrix 的谱隙 `1/40`，再控制 `W_theta K W_theta^-1-K` 的 Schur norm 小于 `1/80`，得到加权 inverse norm 小于 `80` 和列尾平方 `6400(1+L)^(-1/500)`。由 block inverse identity，删去远外部对条件二点核的误差至多 `6400(1+R)^(-1/1000)`；四格 log-ratio 的统一误差和长 pair 尾随后给出式 (10.8)。

审查还对 scalar commutator bound 做了独立大范围数值压力核对；观察值约 `0.0054`，低于证明使用的 `0.01205366... < 1/80`。这只是辅助检查，接受依据仍是原稿的解析 Schur/Riemann-sum 界。

该 reduction 是合法的有限数据接口，但指数 `1/500,1/1000` 与系数 `6400,204800000` 使现有普通窗口没有实用闭合能力。原稿没有把这些误差说成可忽略。

## 4. 反例边界

四点反例严格推翻逐配置 `J<=W`；六点 pair `(0,5)` 严格推翻同一 pair 在 reference actual law 下的平均版。两者都是完整配置 DPP 计算，不是 count-only 或循环替代模型。

但它们都不是 entropy-rate concavity 的反例。尤其六点全部十五个 pair 的 `EW-EJ` 总和仍严格为正，说明局部坏 pair 可以被其他 pair 补偿。S67 后续保留 compensated identity，正是正确的剩余方向。

## 5. 隔离复现

作者交付记录的真实状态是：

- `rational_core.json`：PASS，退出码 0；但 finalizer 明确写的是“本轮未新鲜验证”；
- 三组 `acceleration_bounds_*.log`：均因 `ModuleNotFoundError: flint` 失败；
- 三组 `pair_counterexamples_*.log`：同样失败；
- 浮点 small-model 检查：退出码 0，只能作一致性检查。

审查者没有修改原始检查点，而是在临时副本中使用 Python 3.12.14、python-flint 0.9.0、NumPy 2.5.3 重跑：

- rational core：普通与 `-O` 均 PASS；
- bounds：128/192/256 位普通模式均 PASS，192 位 `-O` PASS；
- counterexamples：128/192/256 位普通模式均 PASS，192 位 `-O` PASS；
- small models：PASS；
- 审查者独立标准库实现：PASS。

普通与 `-O` 的 192 位输出逐字节相同；严格 sign margins 随精度增加稳定收紧。详细命令、哈希和数值见同目录的 `S67_CYCLE17_REPLAY.md`、`S67_CYCLE17_REPLAY.json` 与 `S67_CYCLE17_REPLAY.py`。

## 6. 交付物问题

### 6.1 缺失的 counterexample JSON

正文第 12.1 节引用 `certificates/pair_counterexamples.json`，但交付目录只有三个失败日志和退出码表，没有该 JSON。反例程序能重新生成完整 JSON，本次也已成功重跑，所以这是可修复的 artifact/provenance 问题，不是反例数学错误。

### 6.2 作者 Arb 运行未成功

原包不能把 128/192/256 位 Arb 日志描述为成功证书；它们只记录缺依赖失败。建议未来 source package 把成功输出 JSON、依赖版本和退出码一起保留。当前正文最后的 rational-core “NOT_VERIFIED_IN_THIS_RUN” 提示是诚实的，不应删除；应在旁边补上实际成功运行的时间与环境，而不是把旧 JSON 的 PASS 当作本轮执行。

### 6.3 来源包不是自包含包

`source_inventory.json` 明确标记 S64、PR46 与 QWE02 文件未包含在该检查点。任务允许接受这些已审接口，本审查也从 PR46 核对了数值和量词；但单独分发 S67 目录时，应把这些对象写成外部依赖，而不是给读者留下“包内可直接找到”的印象。

## 7. 最终范围声明

可接受的新结果是：一个实际律、全配置、全有限体积的 acceleration 上界；一个三点 local-Fisher 改进；两个 factor-one 反例；一个固定 diagonal-only 分配架构的障碍；以及一个常数很差但显式的有限窗口接口。

不可接受为已完成的结果是：benchmark entropy-rate chord、区间凹性、全参数凹性、所有 finite-witness 方法的不可能性，或外部新颖性/优先权。

因此最终状态保持：**S67 scoped mathematics verified；主目标 incomplete；复现 artifact 需修复。**
