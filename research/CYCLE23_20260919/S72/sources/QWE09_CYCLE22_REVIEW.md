# QWE09 Cycle22 独立数学审查

审查日期：2026-09-19（Asia/Singapore）  
冻结来源：DPP PR131，提交 `d67db7fdaf8a15b492807745d10ac3b75706690a`

## 总裁决

**`VERIFIED_SCOPED / MAIN TARGET INCOMPLETE / QUANTITATIVE INTERFACE NOT YET USEFUL`。**

QWE09 的五个承重结论均通过独立验缝：

1. §5.4 的完整对数势 `Phi/Chi` 具有正文声称的维数无关 Hessian 界；
2. inverse-score 矩阵鞅、观察域二次补偿和 §6 mask-uniform 平均 resolvent 尾成立；
3. Theorem 1 的 (1.4)、(1.5)、合法 `C²` 极限以及固定谱隙下 `O_{delta,c}(log(n+1)/sqrt(n))` 速率成立；
4. Theorem 2 在明确导入 S55 §8 任意 contraction 基线的条件下成立，两个 separate shift 的使用合法；
5. 六点真实 sine-Toeplitz 反例得到原区间代码和独立 100 位 Decimal 实现的双重复现。它只反驳零支付条件 Jensen，不反驳熵凹性。

没有证明 `rho=1/2,c=19/20,a in [1/50,3/100]` 上熵率严格凹，也没有证明整个 `c in (37/40,1)`。作者保留 `INCOMPLETE` 是正确的。

正确性和实际效用必须分开：在 `delta=1/50` 时，`Lambda` 约为 `1.234397e6`，观察误差的合成前因子约为 `1.763690e15`。因此现有短窗数值无法支付该误差；本稿提供的是合法定量接口，不是目标符号证书。

本审查不认证外部新颖性。

## 分项裁决

| 承重对象 | 裁决 | 说明 |
|---|---|---|
| §5.4 Lemma 3，`Phi` Hessian | CORRECT | 透视函数二阶式、对角/非对角项及 ordered-pair 求和方向正确 |
| §5.4 Lemma 3，`Chi` Hessian | CORRECT | `Chi` 只取相同非负 majorant 的子集，常数无需增大 |
| 固定符号凸域 | CORRECT | 实际矩阵、条件均值及其插值线段都在同一合法对数域内 |
| score martingale (5.8) | CORRECT | 来自真实边缘化恒等式的 Hermitian 方向微分，不是平均条件核 |
| 观察域支付 (5.9)-(5.10) | CORRECT | 独立副本方差恒等式与 inverse difference 只收一次全块二次变差 |
| Lemma 4 平均 inverse tail | CORRECT | 随机网格、Rademacher cell signs 和 commutator 方向正确，mask-uniform |
| Theorem 1 (1.4) | CORRECT | crossing、halo、短端块和全部实际 word 均已计费 |
| mixed comparison (1.5) | CORRECT | `F_eo=-E Chi` 的符号和 parity 平移不变性正确 |
| `C²` 极限与 (7.6) | CORRECT_FIXED_GAP | 仅为 `O_{delta,c}`；不得升级为端点或 `c->1` 联合速率 |
| literal all-exterior passage | CORRECT_WITH_MINOR_CLARIFICATION | 行尾论证应显式取 `N>=B`，不改变结论或常数 |
| Theorem 2 (1.8)-(1.9) | CORRECT_CONDITIONAL_ON_S55 | 两个单独 shift 各使 mask 权重及 contraction 固定，基线可合法调用 |
| 六点 Jensen 反例 | VERIFIED_EXACT | 正概率实际 word；`Delta_Phi,Delta_Chi<0` |
| 半密度 `.95` 目标符号 | INCOMPLETE | (9.1)/(9.2) 均未证明 |
| 整个高对比度区间 | INCOMPLETE | 本稿没有参数覆盖论证 |

## 1. 审查对象与边界

完整读取：

- `QWE09_RESULT.md` 全部 903 行；
- `QWE09_checks.py`、`QWE09_certificate.json`、`ROUND1_STATUS.md`；
- 共同来源中的 `S55_REVIEW.md` §8 与 `SA02_FULL_BLOCK.md`；
- Cycle20 的当前范围和方法去重记录。

远端 DPP PR131 的 head 在审查时仍是冻结提交 `d67db7f...`。没有假定外部对话中的更长稿补齐任何步骤，也没有以附件排版或 checksum 作为验收门槛。

## 2. Lemma 3：完整对数势的 Hessian

正文第 424-438 行把单个 pair 写成

\[
f=s g_\varepsilon(r),\qquad
s=u_i u_j,\qquad r=|X_{ij}|^2/s,
\]

其中 `u_i=sigma_i X_ii>0`。对同号 word，`r<=kappa/(1+kappa)<1`；对异号 word，`r<=kappa`，且对数参数是 `1+r>0`。因此同一固定符号域覆盖全部实际 core 矩阵。

直接微分得到

\[
f''=(g-rg')s''+g'h''+\frac{g''}{s}(h'-rs')^2.
\]

使用

\[
|g''|\le1+\kappa,\quad
|g'|\le(1+\kappa)r,\quad
|g-rg'|\le(1+\kappa)r^2/2
\]

以及 `h'=2 Re(conj(X_ij)D_ij)`，可得正文 (5.7)。其中 off-diagonal 的系数 `14r` 来自 `2r` 与平方展开的 `12r`，没有遗漏复方向交叉项。

维数无关性来自两条行能量估计：

\[
\sum_{j\ne i}r_{ij}^2\le\bar\kappa r_\delta^2,
\qquad
\sum_{j\ne i}r_{ij}^2u_j/u_i\le\bar\kappa r_\delta^2.
\]

第一条使用 `u_i,u_j>=1/(1-delta)` 和 `sum_j|X_ij|²<=delta^-2`；第二条使用
`r_ij²u_j/u_i=r_ij|X_ij|²/u_i²`。对 ordered pairs 求和后，对角方向总系数恰为

\[
2+7(1+\kappa)\bar\kappa r_\delta^2,
\]

非对角方向为 `14(1+kappa)bar-kappa`。这与 `C_H` 一致。`Chi` 只保留 even-odd pair，使用的是同一组绝对值 majorant 的子集。

固定符号域的 pair 约束等价于一个 `2x2` PSD 仿射矩阵，因此域为凸集。实际细矩阵和条件均值具有相同 core signs，插值段不会离开对数合法域。Lemma 3 裁决为 `CORRECT`。

## 3. inverse-score 鞅与观察域补偿

第 461-468 行的

\[
E[(G_V)_{II}\mid Y_A]=(G_A)_{II}
\]

由对真实原子边缘化恒等式沿任意 Hermitian `I x I` 扰动微分得到。严格通道 gap 保证双向小扰动仍合法；实部、虚部 Hermitian 基方向足以识别全部矩阵元。

Lemma 3 给出双侧 Hessian 界，Taylor 线性项因 score martingale 消失，从而得到 (5.9)。独立条件扩展满足

\[
G(Y)-G(Y')=G(Y)\operatorname{diag}(Y'-Y)G(Y').
\]

右侧 diagonal difference 只支撑在 `V\A`，再用 `||G||<=delta^-1` 和独立副本方差恒等式，得到 (5.10) 的 `Lambda/(2delta²)`。没有 pair 数或邻居数因子。

逐站点揭示时每个矩阵鞅增量均为秩一 `zeta vv*`，所以其 Hilbert-Schmidt 平方等于 trace 平方；鞅差正交证明 (5.11)。该解释正确，但 (5.10) 本身已足够，不依赖额外符号假设。

## 4. Lemma 4：mask-uniform 平均 resolvent 尾

随机平移长度 `R` 网格，并给不同 cell 独立 Rademacher signs。真实 observation mask 与 diagonal sign matrix `D` 对易，因此

\[
[G,D]=-G[K,D]G,\qquad
||[G,D]||_{HS}^2\le\delta^{-4}||[K,D]||_{HS}^2.
\]

距离 `r` 的两点落入不同 cell 的概率恰为 `min(r/R,1)`；不同 cell 的 sign-square difference 条件期望为二。两侧相同因子抵消，给出 (6.2)。使用

\[
|K_{ij}|\le c/(\pi|i-j|)
\]

并对每行的两个方向求和，得到正文的调和尾常数。替代界 `n^-1||G||_HS²<=delta^-2` 也正确。因此 Lemma 4 对每个实际 mask 成立，而不是只在输出平均后成立。

## 5. Theorem 1 与全部边界

随机平移的长度 `m` 分块使一条距离 `r` 的 pair 被切断的概率为 `min(r/m,1)`，所以 crossing pair 总成本由 `n C_log tau(m)` 支付。

对 halo 完整的 core 使用 (5.10)。core 彼此不交，因此外部能量总和不重复计算，并由距离至少 `L+1` 的 Lemma 4 尾支付。缩短或 halo 截断的异常 core 总站点数至多 `2(m+L)`；实际 core 和按 `r/m` 缩放的标准平稳 core 各自至多 `B_*r`，故总边界成本是 `4B_*(m+L)`。

除以 `n` 即得 (1.4)。半密度 mixed response 用 `F_eo=-E Chi`，奇偶平移交换不改变 unordered cross-pair 势，故 (1.5) 同样成立。

由 (1.4)，先选 `m,L` 再令 `n` 大，可得 `H_n''/n` 在任意紧合法 `J` 上一致 Cauchy。正文第 582-588 行使用两个固定点的 Taylor 公式，从函数值极限和二阶导一致极限恢复一阶导基点，再识别 `h in C²`；没有对熵值误差求导。

取 `m=L=floor(sqrt(n))`，分别使用有限比较和熵率比较，得到

\[
\sup_{a\in J}|H_n''/n-h''|
\le2\epsilon_{r_n,r_n}+8B_*r_n/n
=O_{\delta,c}(\log(n+1)/\sqrt n).
\]

这是固定正 gap 的速率，不能外推为 `delta->0` 或 `c->1` 一致速率。

### 全外部 passage 的小表述缺口

第 648-660 行先固定截断半径 `B`，再使用观察窗口 `[-N,N]`。要让所有 `|r|<=B` 坐标属于有限 interval，应显式写“随后取 `N>=B`”。证明本来就令 `N->infinity`，加入这一条件不改任何不等式、常数或量词，故记为 `MINOR CLARIFICATION`，不是 critical gap。

## 6. Theorem 2：S55 基线与两个 shift

审查按任务要求接受 S55 §8 的有限 contraction 基线：

\[
\partial_b^2H(\operatorname{DPP}(bI+(37/40)R))
\le-\dim(R)/50.
\]

在目标区间，`p in [99/200,101/200]`。精确重算得到

\[
\alpha_{max}=\frac{9025}{9999}<\frac{37}{40},
\]

\[
b_{min}=\frac{97}{2475},\qquad
b_{max}=\frac{147}{2525}<\frac3{40}.
\]

固定 even shift `s`、只微分 odd shift `t` 时，even mask 权重、`alpha(p_e)` 和 `R_y(p_e)` 全部固定；只有 scalar `b=p_o-c²/(4p_e)` 以斜率一变化。因此把 `alpha R_y` 缩放成 `(37/40)R'_y` 后，S55 基线可以逐 mask 使用。反向条件化并固定 `t`，同理得到 even-shift 二阶界。矩形 parity blocks 可以不等大，只改变维数 `|E|,|O|`。

最后

\[
H_n''=\mathscr H_{ss}+2\mathscr H_{st}+\mathscr H_{tt}
\le-n/50-2E\Chi(G_n),
\]

再由 (1.5) 得到 (1.8)-(1.9)。完整 conditional-information curvature 没有被丢弃；它已包含在 `B_n=H_n-|E|h_b(p)` 和 mixed response 中。

Theorem 2 因而是正确的**充分接口**，但右端尚未证明为负。

## 7. 六点真实 Jensen 反例

原标准库 256-bit dyadic interval 程序退出码为零，重新生成的 certificate 与归档 JSON 完全一致：

```text
Pr(Y_A=y)  in [0.014232864029787238, 0.014232864029787239]
q          in [0.291967352633421847, 0.291967352633421848]
Delta_Phi  in [-0.106585307859143407,-0.106585307859143406]
Delta_Chi  in [-0.096395465271827624,-0.096395465271827623]
Q          in [0.170309619791317635, 0.170309619791317636]
-Delta_Phi/Q in [0.625832574752639508,0.625832574752639509]
```

审查者另写一份不使用原 interval 类的 100 位 Decimal 实现，从 Machin 公式重建 `pi`，独立做 Gaussian elimination、Schur update 和两个势。其中心值全部落在上述严格区间中。

观察 word 有严格正概率，fine matrices 以真实条件概率 `q,1-q` 平均回 coarse matrix，但两个 Jensen gap 都严格为负。因此 zero-payment conditional Jensen 被实际目标模型反驳。该结果没有给出无条件平均符号，也没有计算实际熵曲率，不能写成熵凹性反例。

## 8. 定量效用与剩余义务

在目标紧区间 `delta=1/50,c=19/20`：

\[
\kappa=9025/776,\qquad r_\delta=49,\qquad
\Lambda=1486648002527/1204352\approx1.234397\times10^6.
\]

正文给出的观察误差合成量级约 `1.763690e15*(H_L+2)/(L+1)`。因此浮点短窗值 `V_{2,2}≈0.55166`、`W_{2,2}≈-8.67913` 不能支付严格误差；它们只检查实现。

真正剩余的 continuum 义务仍是证明某个固定 `m,L` 在整个参数区间满足 (9.1)，或证明 baseline-independent 的 (9.2)，或提供更强结构符号。当前没有任何一项完成。

所以最终状态是：**接口正确，反例正确，目标凹性未解决，整个高对比度区间未解决。**
