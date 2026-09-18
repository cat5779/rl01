> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA02 Sol 独立评估与后续路线

> **Provenance / attribution.** 本文件不是 Pro 原交付的一部分。它由本次 Sol 在阅读并独立审计 `SA02_MATRIX_BELLMAN_FULL_BLOCK.md`、以及对照仓库现有 `37/40` 基线后形成。本文最后提出的 `rank-one reveal curvature + posterior-normalized coordinates + retained exact remainder` 路线，是 **Sol 的独立推论与研究建议**，不是 Pro 的结果、结论或建议。

## 1. 用人话说 Pro 工具做了什么

第一版局部补偿把每条 pair 当成一笔局部成本，向两个端点的 Fisher 预算各收半份；因此路径和三角形可结账，但一般高次数近场图会重复消耗中心预算。

第二版改用整个块的共同逆得分矩阵

\[
G_V(Y)=(K_V-\operatorname{diag}(1-Y_V))^{-1},
\]

并把所有 pair 一次性装进矩阵势

\[
\mathfrak T(X)=\sum_{i,j}\frac{|X_{ij}|^4}{X_{ii}X_{jj}}.
\]

核心兼容性是

\[
E[(G_V)_{II}\mid Y_A]=(G_A)_{II},\qquad I\subset A\subset V,
\]

所以扩大真实观察域时，核心主块形成一个矩阵鞅；单步揭示是 rank-one Schur 更新。这样，块内所有边的观察域变化由同一个矩阵二次变差统一支付，而不是按边重复收费。

由此 Pro 得到一个完整块单侧包络，原型为

\[
\frac{H_n''}{n}\le \mathcal U_{m,L}
+\frac{C_*H_m}{m}
+\frac{\Gamma_{\delta,c}B_*}{4\delta^2L}
+O((m+L)/n).
\]

它的结构收益是：块内可含完整图；空间切块误差为 `O(log m/m)`；观察误差为 `O(1/L)`，不再显式乘近场半径或内部图度数。

## 2. 对原定 `(37/40,1)` 目标的真实增益

仓库当前已证明：对任意 Hermitian positive contraction，整个合法 `a` 区间在 `c<=37/40` 上强凹；而 fixed-density sine 在 `c>37/40` 的完整合法区间仍 open。

因此，按“已证明的 contrast 覆盖范围”计，这个工具目前的增益是

\[
\boxed{0}.
\]

它没有把 `37/40` 推到任何更大的明确 universal 或 sine-specific contrast，也没有闭合种子 `rho=1/2,c=19/20,a=1/40`。

但它有真实的结构增益：它消除了旧 S7/第一版补偿中的**重叠次数/高图度数障碍**，把剩余问题改写为“一个共同真实窗口矩阵量是否足够负、以及其观察域变化是否能以可接受常数支付”。这是方法层面的推进，而不是目标区域推进。

## 3. 为什么当前具体版本还不足以攻到 `c->1`

在平衡点 `a=(1-c)/2`，令 `delta=(1-c)/2`。Pro 当前 semiconvexity 支付使用了全方向 Hessian 上界

\[
|D^2\mathfrak T(X)[H,H]|\le 2\Gamma_{\delta,c}\|H\|_{HS}^2,
\]

再配合 `\|G\|\le\delta^{-1}` 等最坏情形控制。其观察误差系数在高对比度处按高次幂爆炸；在种子 `c=19/20,a=1/40`，Pro 给出的系数约为

\[
4.12\times10^{10}.
\]

因此，即使新接口不再乘 block 内边数，当前常数也远未到实用的目标认证尺度。

同一框架的粗全局推论只在平衡点给出

\[
c<\sqrt{1-e^{-1}}\approx0.79506
\]

的通用负曲率区间；这明显弱于仓库已有 `37/40=0.925` 基线。故这个工具若要超过 `37/40`，不能依赖其 universal worst-case 版本，而必须利用 sine-specific / posterior-specific 结构。

## 4. Sol 的判断：当前常数路线接近实用上限，但核心框架没有到头

这里要区分两件事。

### 4.1 当前 `Gamma_{delta,c}` 全方向 semiconvexity 路线

我不建议继续主要投入于把现有常数做小幅优化。原因不是常数“不够漂亮”，而是高对比度处存在尺度级爆炸。若下一步仅是改善若干 Cauchy--Schwarz 常数、增加普通求积节点或扫描更多 `(m,L)`，很难把一个高次 `delta^{-p}` 成本转成接近 `c=1` 的工具。

所以，**当前这个具体支付实现接近它的实用上限**。

### 4.2 共同矩阵鞅 / 整块支付框架

这个核心没有到头。真实揭示增量并非任意 Hermitian 方向，而是

\[
\Delta G=\zeta ww^*,
\]

即特殊 rank-one Schur 更新。因此用“所有 Hermitian `H` 的最坏 Hessian”支付真实路径，很可能是当前最大的结构浪费。

## 5. Sol 提出的下一步路线（不是 Pro 的结论）

> **Attribution.** 本节是 Sol 在独立评估后提出的研究路线。Pro 的第二版没有提出或证明这里的组合策略。若后续使用，应引用为“Sol follow-up proposal”，而不是 Pro 工具的已证内容。

我建议优先研究：

\[
\boxed{
\text{rank-one reveal curvature}
+\text{posterior-normalized coordinates}
+\text{retained exact pair remainder}.
}
\]

具体分三步。

### A. 只沿真实 rank-one reveal direction 控制曲率

不要再证明

\[
|D^2\mathfrak T(X)[H,H]|\le C\|H\|^2
\quad\text{for all Hermitian }H.
\]

而是直接研究

\[
D^2\mathfrak T(G)[ww^*,ww^*],
\]

并利用 `w` 与 `G` 来自同一个 Schur complement / posterior reveal 的代数关系。目标是把支付常数从裸 `\delta^{-p}` 最坏上界降到由实际 posterior row energy、conditional variance 或 Schur slack 控制的量。

若这一项仍不可避免地产生很高阶的 endpoint blow-up，则可视为该框架接近真正硬上限；反之，若能降到约 `O((1-c)^{-2})` 或更温和尺度，则有可能与已有 `37/40` 两预算方法竞争。

### B. 把坐标从裸 inverse score `G` 改成 posterior-normalized 变量

仓库现有 `37/40` 证明的重要特征，是保留 reverse-Bayes/posterior Schur budgets，而不是仅用 `\|G\|\le\delta^{-1}`。因此建议把 Pro 的 block martingale 架构与现有 posterior-normalized quantities 结合。

目标对象可以是 normalized posterior correlation、completion-weighted row energy、Schur slack 或其矩阵版本，使 `c->1` 时变量本身保持有界或只出现低阶奇性。

直观分工是：

- block martingale 负责解决“许多重叠 pair 重复收费”；
- posterior normalization 负责解决“endpoint blow-up”。

这比继续磨当前 `Gamma_{delta,c}` 更可能产生真正的 contrast 增量。

### C. 不要丢弃 exact negative remainder

Pro 的精确块恒等式含有

\[
-2\sum_{i<j}E r_{ij},\qquad r_{ij}\ge0,
\]

但主包络为了简化将其全部舍弃。高对比度恰是 odds-ratio / pair interaction 最强的区域，这个 exact remainder 可能同时变得最有价值。

因此下一版候选势应与 rational/quadrature hierarchy 一起设计，使观察域支付与保留余量同时闭合，而不是先把余量丢掉再用巨大 worst-case 常数补回来。

## 6. 何时判定这条路线真正走到头

我建议设置一个明确的 kill criterion：

1. 已经只沿真实 rank-one reveal direction；
2. 已经使用 posterior-normalized 而不是裸 `G` 坐标；
3. 已经保留至少第一层 exact/quadrature negative remainder；
4. 仍然证明任何共同块观察域支付都必须付类似 `\delta^{-p}`、`p>=4` 或更坏的成本，且没有同阶负余量抵消。

若这四点同时成立，那么对 `c->1`，这条 block-Bellman 路线大概率达到硬上限，应转向别的全局结构。

目前尚未到这个阶段，因此不能把整个工具方向判死。

## 7. 当前推荐的研究优先级

从原定 `(37/40,1)` 目标出发，我会按以下顺序投入：

1. **最高优先级**：推导真实 rank-one reveal 下的 exact directional second variation，并尝试 posterior-normalized 重写；
2. **第二优先级**：将 Pro 已给的两节点/多节点有理 remainder 保留进同一个观察域支付；
3. **第三优先级**：只在前两步获得明显改善后，再做 sine Toeplitz 特有的窗口估计或计算认证；
4. **低优先级**：继续优化现有全方向 `Gamma_{delta,c}` 的数值常数。

## 8. 状态摘要

- Pro 的 full-block matrix Bellman tool：**结构上有真实增益，目标区域上尚无增益**。
- 对 `(37/40,1)`：目前没有新的已证明 contrast 区间。
- 当前 `Gamma_{delta,c}` 实现：高对比度尺度过差，接近实用上限。
- 共同矩阵鞅 / full-block payment 框架：**尚未走到头**。
- 下一条最值得验证的路线：**rank-one reveal curvature + posterior normalization + retained exact remainder**；该路线是 **Sol 的独立推论**，不是 Pro 原交付。
