# S41 cycle04 独立审查

日期：2026-09-18

审查对象：完整附件 `recovered/S41_cycle04/S41_CYCLE04_RESULT.md`（完整到 §10 Computational checks）及配套 `S41_CYCLE04_checks.py`。同时与先前首 20000 字符的聊天导出 `S41_CYCLE04_PARTIAL.md` 比较；两版主要是章节重排，附件没有补出聊天版中省略的 complete connected/marked 通项展开。旧 cycle03 慢速有限观测证书只按既有独立审查作为作用域依赖，本报告不重审旧整稿。

## 总裁决

S41 cycle04 的概率与投影骨架是可信的：latent posterior 仍为投影 DPP，Schur 数据字典、outside diagonal flow、观察 anchor 的能量比较、随机 anchor 平均以及附件 §6 从有限 posterior 输运到 full posterior 的逻辑均可独立核对。

但是新速率的唯一承重点——附件 Lemma 5.1（聊天版 Lemma 8.1/8.2）——尚未得到完整证明。正文只列出若干 prototype monomial、若干总和上界和一个覆盖性断言，随后直接给出 `2^28 a_c^28`。它没有展示：

1. 完整 connected expansion；
2. expansion 中每个单项到 prototype 的逐项覆盖表；
3. 全部一次、二次翻位量及 Bregman 余项的 marked 导数展开；
4. 每类项的数量、系数和幂次为何确被最终常数吸收；
5. 无限指标核的绝对收敛/Cauchy 定义如何从这些未展开项推出。

因此 `O_c(sqrt(log N/N))` 的 Theorem A 目前是**条件性结论**，不能标为已经独立验证。即使以后补齐两引理，在 `c=.95` 时常数也超过 `10^53`，简单误差系数约为 `10^55.8`；这只会给渐近存在性，不会给可实际判号的尺度，更不会完成熵率凹性。

## 分项状态

| 项目 | 状态 | 结论 |
|---|---|---|
| §1–3 有限 actual-sine 对象与完整 moving-law 二阶导数 | **VERIFIED_SCOPED** | `w''`、交叉项、`q''` 均保留。分组核 (3.2) 与冻结 V14 的同一性依赖旧来源。 |
| §4 latent posterior projection | **VERIFIED_SCOPED** | 对角似然倾斜后仍是投影到 `D_J Ran(Q)`。 |
| §4 Schur 数据字典 (4.2)–(4.4) | **VERIFIED_SCOPED** | 可由块逆直接验证；另有有限精确检查。 |
| §5 边界能量 `U=T+W` | **VERIFIED** | `T<=1/4`、`W<=1/16`、`U<1` 正确。 |
| §6 outside diagonal flow | **VERIFIED** | 投影导数及 `U(t)<=e^{3ht}U(0)` 正确。 |
| §7 anchor 更新 | **VERIFIED_SCOPED** | `U(P^-)<=s_x^4 U(P^+)` 的流估计成立。 |
| Lemma 5.1 complete-jet tail（聊天版 8.1） | **GAP** | prototype 上界不能替代完整 expansion 与覆盖证明。 |
| Lemma 5.1 directional/marked bound（聊天版 8.2） | **GAP** | marked monomial 只被概述，关键导数与项数账本缺失。 |
| §6.1 随机 anchor 与条件计数方差 | **VERIFIED** | 平均边界能量确被 `2s_x^4 V_Q(N)/N` 控制。 |
| §6.2 full posterior 与 finite marginal 接口 | **VERIFIED_CONDITIONAL** | 若 Lemma 5.1 成立，则 (6.6)–(6.9) 及最终速率正确。 |
| Theorem A | **GAP / CONDITIONAL** | 核心 Lemma 5.1 的两个部分未完整证明。 |
| §7 响应坐标误差账本 | **VERIFIED_CONDITIONAL** | 公式及与 observation loss 分账正确；主界仍依赖 Lemma 5.1。 |
| §8–9 benchmark 与范围声明 | **VERIFIED_SCOPED** | 明确认定常数不可实算判号且不推出最终凹性。 |
| §10 作者计算检查 | **VERIFIED_AS_DIAGNOSTIC** | self-test 与 V14 检查运行通过，但不覆盖 Lemma 5.1。 |
| 最终熵率凹性 | **NOT PROVED** | 本稿自身亦未给出该结论。 |

## 1. 有限 actual-sine 对象与 moving-law 导数

有限观测核

\[
K_x(h)=hI+x(Q-I/2)
\]

是无限 noisy sine 输出的真实主边缘，不是循环或 Fejer 替代。对观察字 `z`，`B'=I`，故

\[
G'=-G^2,
\quad w'=w\operatorname{tr}G,
\quad w''=w[(\operatorname{tr}G)^2-\operatorname{tr}G^2],
\]

\[
q'=1+\|v\|^2,
\qquad q''=-2b^*G^3b.
\]

代入 `F=sum w phi(q)` 得正文 (3.1)，其中概率加速度、移动权重交叉项和 posterior 加速度均未丢失。

正文 (3.2) 是冻结 V14 的分组写法；旧 cycle03 审查已确认有限导数与该分组在有限系统上一致。本轮不把冻结来源中仍待独立审查的其他结论一并升级。

## 2. latent posterior projection 与 Schur 字典

对 observed word `y_j=±1`，似然比等于 `s_x^{2y_j}`。给一粒子子空间表示 `Q=UU*`，对角似然倾斜后的投影为

\[
\Pi_J=D_JU(U^*D_J^2U)^{-1}U^*D_J,
\]

即投影到 `D_J Ran(Q)`。这是纯投影 DPP 在正对角权重下的标准精确更新，不涉及有限 Toeplitz 压缩被误当作投影。

在 balanced channel 下，把直接 Schur 补中的

\[
B=K_{x,J}(1/2)-\operatorname{diag}(1-z)
\]

与后验投影公式联立，可验证

\[
q=\frac12+x(\Pi_{00}-1/2),
\]

\[
v_j=\frac{2x}{\sqrt{1-x^2}}y_j\Pi_{j0},
\]

\[
G=\frac2{1-x^2}[S-xS(2\Pi_J-I)S].
\]

由最后一式及 `2Pi-I` 的酉自伴性，

\[
\|G\|\le\frac2{1-x}\le a_c.
\]

其余 posterior interval、`v` 与 flip denominator 的统一界与此兼容。

## 3. 边界能量与 outside flow

对投影 `P`，

\[
T_0=\sum_{k\notin I}|P_{k0}|^2
\le P_{00}(1-P_{00})\le1/4.
\]

又因 `T_j<=P_jj(1-P_jj)<=1/4`，

\[
W_0=\sum_{j\in J}|P_{j0}|^2T_j
\le\frac14P_{00}(1-P_{00})\le1/16.
\]

所以 `U_0=T_0+W_0<=5/16`。

对 `P_t` 投影到 `e^{tH}Ran(P_0)`，直接微分得到

\[
\dot P=(I-P)HP+PH(I-P).
\]

若 `H` 支持于 outside `O`，则对 `i in I`

\[
\dot Pe_i=(I-2P)HPe_i,
\quad
\|\dot Pe_i\|\le\|H\|\sqrt{T_i}.
\]

由此可得

\[
|T_0'|\le2hT_0,
\qquad
|W_0'|\le hT_0+3hW_0,
\]

并由 Gronwall 得 `U(t)<=e^{3ht}U(0)`。积分 anchor column 的导数也给出 (6.4)。这些步骤没有隐藏体积因子。

## 4. 观察 anchor

只缩放 anchor 坐标，`|eta|<=log s_x`。此时

\[
\dot P_{k0}=\eta(1-2P_{00})P_{k0},
\quad
\dot P_{0j}=\eta(1-2P_{00})P_{0j},
\]

且

\[
E_O\dot Pe_j=-2\eta P_{0j}E_OPe_0.
\]

这些恒等式给 `|U'|<=4|eta|U`，沿完整 anchor update 积分即得

\[
U(P^-)\le s_x^4U(P^+).
\]

常数方向正确。

## 5. Lemma 5.1 尾界部分的缺口

正文给出 primitive 界 (8.3)–(8.9)，并列出

\[
K_1=g_{ij}p_i^3p_j,
\quad K_2=g_{ij}^2p_i^4,
\quad K_3=g_{ij}^2p_i^2p_j^2,
\quad K_4=g_{ij}^4p_i^4
\]

和一个 connected remainder。可见的 Cauchy–Schwarz/行平方和估计与 `T_0,W_0` 的量纲相符；例如 superficially linear 的 `K_1` 确可通过 `sqrt(T_0W_0)` 变成二次边界能量。

问题不在这些 prototype 界本身，而在“它们覆盖完整核”的步骤没有写出。式 (3.2) 的最后一组包含

\[
\sum_j\bar r_j[\overline B_\phi(z^j)-\overline B_\phi(z)],
\]

展开后涉及有序双指标、翻位后的 `o_i^{-1}`、`v_i(z^j)`、`G_{ij}`、Bregman 两端点变化以及对角退化项。正文只说“substitution into the complete connected expansion”，但没有显示该 expansion，也没有给出每个系数如何落入 `K_1`–`K_4` 或 `|d_j|D_{ij}^2`。

旧冻结文件同样只给一个汇总型 connected 上界，并带待独立审查状态；不能用引用标记替代本轮新引理的证明。没有覆盖表，就无法排除遗漏一个只有单个 boundary factor、产生 `sqrt(U)` 或体积因子的项。

此外，`K_{x,Z\setminus{0}}` 的无限指标定义需要先由完整 expansion 的绝对可求和性建立。把结论写成 tail bound 本身不能同时充当其未展开的定义。

因此附件 Lemma 5.1 的 (5.1)（聊天版 Lemma 8.1）状态为 **GAP**，而不是已证。

## 6. Lemma 5.1 directional 部分的缺口

正文对 `q,v,G,d_j` 的 primitive directional estimates 是合理的，`delta_0,delta_1` 也正好在 outside flow 下化为 `h sqrt(T_0)` 与 `h sqrt(W_0)`。

但从这些 primitive 界到 (8.17) 的核心步骤仍被一句话跳过：

> 每个 differentiated connected term 都是前述 prototype 加一个 marked derivative factor。

这不足以证明完整 directional bound。至少必须列出并界定：

- `o_j^{-1}` 及翻位后 denominator 的导数；
- `G^j,v^j,q^j,A_{z^j}` 的全部导数项；
- Bregman 对两个端点和对底点的导数；
- `B_phi(z^j)-B_phi(z)` 展开后的二次翻位 marked 项；
- 对角 `i=j` 的退化项；
- 每一 prototype 的乘法因子数和总项数。

正文只给四个 prototype 的最终数字及总称 `2^22 a_c^27`，没有提供可逐项复算的来源。任意再大的 `2^28a_c^28` 都不能证明“没有漏项”。因此附件 Lemma 5.1 的 (5.2)（聊天版 Lemma 8.2）也是 **GAP**。

## 7. 随机 anchor 平均

这部分在不依赖 Lemma 5.1 的层面成立。对观察完整 `Y_I` 后的 posterior projection，

\[
\sum_{i\in I}T_i=\operatorname{Var}(N_I\mid Y_I).
\]

同时

\[
\sum_{i\in I}W_i
=\sum_{j\in I}T_j\sum_{i\ne j}|\Pi_{ji}|^2
\le\sum_{j\in I}T_j.
\]

全方差公式给

\[
E\operatorname{Var}(N_I\mid Y_I)
\le\operatorname{Var}_Q(N_I)=V_Q(N).
\]

结合 anchor update，并利用平移不变性把 `N` 个 anchor 位置识别为同一固定区间内的 `N` 个站点，得到

\[
\frac1N\sum_rEU_0(\Pi_r^-;I_{N,r})
\le2s_x^4\frac{V_Q(N)}N.
\]

这里没有把期望界误写成逐 word 界，也没有额外体积因子。

## 8. full posterior 与真实 finite marginal

从 `Pi_r^-` 同时 reveal outside 输出，可写成支持于 `O` 的 bounded diagonal flow，`||H||=log s_x`。若 Lemma 5.1 的 directional 部分成立，积分得附件 (6.6)；若其 tail 部分成立，full posterior 的 omitted-coordinate tail 得附件 (6.7)。配合上一节的线性期望界和 Jensen，即得 (6.8)、(6.9)。所有 `s_x` 次幂和系数均核对一致。

有限 `F_{x,N,r}` 使用的正是无限 actual law 在 `J_{N,r}` 的真实 marginal；posterior `Pi_r^-` 也正是条件于该 finite word 的 posterior。因此附件 §6 没有 Fejer-to-sine、循环核或 fictitious exterior word 误差。

所以附件 §6 的接口是 **VERIFIED_CONDITIONAL**：它没有新的独立缺口，但完全依赖未证明的 Lemma 5.1。

另用一个七维、秩三的精确有理投影，在 `x=3/5` 下枚举五点区间的全部输出字与全部 anchor。SymPy 精确算术逐项验证了 posterior projection、Schur 字典、anchor inequality、outside-flow directional inequality、条件计数方差及随机 anchor 平均；所有断言通过。该检查只验证附件 §3–4、§6 的有限代数，不覆盖 Lemma 5.1。

复现命令：

```powershell
uv run --with sympy python research/CYCLE04_20260918/checks/verify_s41_projection_dictionary.py
```

## 9. 速率与实用性

若补齐 Lemma 5.1，两项误差分别为 `O(V_Q(N)/N)` 和 `O(sqrt(V_Q(N)/N))`，而 half-filled sine 满足 `V_Q(N)<= (log N+4)/pi^2`，故声明的

\[
O_c\!\left(\sqrt{\frac{\log N}{N}}\right)
\]

速率随后成立。

但在 `c=.95`，`a_c=40`，

\[
C_{jet}=2^{28}40^{28}>10^{53.28}.
\]

简单误差界在乘入 `s_c^{7/2}` 后的前置系数约为 `10^{55.8}`。即使两引理最终补全，要把右端压到常数量级也需天文尺度 `N`。这不反驳渐近定理，但说明它不是当前 benchmark 的可执行判号证书。

更重要的是，本定理只比较冻结的 balanced、half-filled 局部曲率泛函 `Gamma(c)` 与有限 observation object。它没有证明 `Gamma(c)` 的符号，也没有完成到真实 full-configuration Shannon 熵率 Hessian 的全部传递，更没有覆盖一般 `rho,a`。

## 10. 完整附件与计算检查

完整附件已取得，正文到 §10 Computational checks 结束；不存在继续等待的缺页。附件 §7 将响应坐标损失与 observation loss 分开，误差账本和“全保留时响应损失为零”均与先前独立核验的有限公式一致。§8 明确报告 `N=8` 时 analytic remainder 约 `4.60e55`，不声称判号；§9 也明确列出未覆盖的一般 `rho,a` 与熵率二阶导接口，范围声明正确。

作者代码经检查后实际运行：

```powershell
uv run --with numpy --with mpmath python S41_CYCLE04_checks.py --self-test --check-v14 --N 5
```

结果为 `self-tests passed`，直接有限二阶导与 V14 期望完全一致到显示精度，posterior 字典误差约 `1e-14`，flow diagnostics 通过。代码没有实现 Lemma 5.1 的完整 connected expansion，也没有检查全部 marked monomial；其自身文档亦只把结果标为非严格浮点 diagnostics。因此运行结果支持附件 §2–4 的有限代数，不修复 §5 缺口。

本报告不认证 `PROVED_SCOPED` 作者标签；在补齐 Lemma 5.1 前，Theorem A 状态为 `GAP / CONDITIONAL`。

## 最终结论

\[
\boxed{
\text{投影/平均/输运骨架成立；complete-jet 尾与 directional bound 未证。}
}
\]

需要的最小补件不是更大的常数，而是 Lemma 5.1（聊天版 8.1/8.2）的完整代数展开、逐项 prototype 覆盖表及 marked 导数账本。只有补件通过后，才能把 `O_c(sqrt(log N/N))` 从条件结论升级为 `VERIFIED_SCOPED`。
