# R11/G12 第二次完整回传独立对抗审查

**总裁决：PARTIAL。** `source02.md` 正确保持 `INCOMPLETE`，没有把本轮结果误报为普适 selector 的证明或反例。其最主要的新承重结论——整个 flow polytope 的精确 coupling 表示、fixed-gap 原子正则性、坐标方向单点纤维、近坐标纤维坍缩、精确支撑约化，以及固定支撑维数下与 ambient `n` 无关的 Hausdorff 稳定性——均可通过。第 9 节也已经修复第一次回传的归一化错误，只在 coupling 层陈述 thin-path 条件数。

需要修正的是第 8、11 节及开头摘要对“排除了哪些反例”的概括。现有证明只排除若干 **pairwise entire-fiber separation** 机制；它没有排除一般有限 branching/cycle 的全局选择不相容，也没有证明“支撑近似集中”在与参数距离无关的量词下不能产生反例。第 11 节把一个充分正面路线写成了必要路线，也应收窄。

本审查只读 `source02.md` 正文；末尾所指未取得 ZIP 未读取、未认证，也不影响对完整正文的裁决。

## 1. 整个 flow polytope 的 coupling 表示：PASS

取 `h=ε/2` 时，`K+hP` 仍满足

\[
\varepsilon I\le K+hP\le (1-\varepsilon/2)I.
\]

由于 `P(Z-I)` 秩至多一，生成行列式逐系数关于 `t` 仿射，故

\[
p_{K+tP}=p_K+t b_{K,P}.
\]

映射

\[
\Pi_F(S,S\cup\{i\})=hF(S,i),\qquad
\Pi_F(S,S)=p_K(S)-hF_{\rm out}(S)
\]

确实把原容量

\[
F_{\rm out}(S)\le (2/\varepsilon)p_K(S)
\]

精确变成对角质量非负。两边缘分别为 `p_K` 与 `p_{K+hP}`。反向以 `F=h^{-1}\Pi_{off}` 恢复散度和原容量；off-diagonal 总质量由基数期望差精确为 `h tr(P)=h`，所以恢复的 flow 总质量为一。因而 (1.6) 覆盖的是冻结任务中的**整个** flow polytope，不只是第一次回传的 half-capacity 子多面体。全局归一化也可由散度乘 `|S|` 求和独立推出。

## 2. fixed-gap atom regularity：PASS

因

\[
K-D_S=\tfrac12J_S\bigl(I+J_S(2K-I)\bigr),
\qquad \|2K-I\|\le1-2\varepsilon,
\]

Neumann 估计给出

\[
\|(K-D_S)^{-1}\|\le1/\varepsilon
\]

且常数与 `n,S` 无关。由 Jacobi 公式得到 (2.4)--(2.6)；沿 `K_t=(1-t)K+tL` 积分得到 (2.7)。resolvent identity 与 trace/operator norm 对偶给出 (2.8)，量词覆盖任意同一 `n` 上的 fixed-gap `K,L` 和秩一投影 `P,Q`。

`L_K=K(I-K)^{-1}` 的谱落在

\[
[\varepsilon/(1-\varepsilon),(1-\varepsilon)/\varepsilon],
\]

而相邻原子比是相应主子矩阵的 Schur complement；其倒数是逆矩阵的一个对角元，故仍落在同一区间，(2.9) 正确。这里的常数只依赖 `ε`，不依赖维数。不过这些估计只控制单个原子及 score 的相对变化；不能据此单独排除由许多原子和多面体面结构共同造成的全局选择障碍。

## 3. coordinate edge masses 与 singleton fibers：PASS

以 `1_{i\in S}` 测试散度，得到每个可行非负 flow 都满足

\[
\sum_{S:i\notin S}F(S,i)=P_{ii}.
\]

当 `P=E_j` 时，非负性迫使所有非 `j` 边为零。不同 `j` 边连接互不相交的二点对，因此散度逐对唯一确定边质量，纤维为 singleton。余子式计算给出

\[
U_{K,j}(A,j)=p_{K_{E\setminus\{j\}}}(A).
\]

主子矩阵压缩不增 trace norm，结合已审 DPP law 的 `l1` 稳定性，(4.2) 的常数二成立。

## 4. near-coordinate fiber collapse：PASS

对 `Q=vv^*`，令 `d=\|Q-E_j\|_1=2\sqrt{1-|v_j|^2}`、`η=1-|v_j|^2`。由坐标边总质量恒等式，非 `j` 边总质量恰为 `η`。`j` 边差 `H_j=F^{(j)}-U_{K,j}` 支撑在互不相交的端点对上，故

\[
\|\operatorname{div}H_j\|_1=2\|H_j\|_1.
\]

再用冻结任务允许的 signed repair，仅在控制 divergence difference 的地方使用它，得到

\[
\sup_{F\in\mathcal F(K,Q)}\|F-U_{K,j}\|_1
\le d+\tfrac12d^2\le2d.
\]

与 (4.2) 合并即得 (5.6)。因此**pairwise entire-fiber separation** 若一端恰为 coordinate projector，比例有维数无关上界；这里没有把 signed flow 冒充非负 flow。

## 5. support reduction：PASS

若 `J=supp(v)`、`R=E\setminus J`，坐标边总质量恒等式迫使 flow 只使用 `J` 标号边，故按外部配置 `T\subseteq R` 分块。fixed gap 保证

\[
B_T=K_{RR}-I_{R\setminus T}
\]

可逆。对 atom determinant 作 Schur complement，确得

\[
p_K(T\cup A)=p_{K_{RR}}(T)p_{K^T}(A),
\]

且因 `P` 只在 `JJ` 块上，导数同样因子化为 (6.3)。逐坐标 inclusion/exclusion conditioning 的公式正确；从 `K-εI\succeq0` 及 `I-K-εI\succeq0` 的 Schur complement 可得

\[
\varepsilon I\le K^T\le(1-\varepsilon)I.
\]

所以 inactive coordinates 只产生若干带权的固定 `|J|` 维块，不会改变每块的谱隙。

## 6. bounded-support Hausdorff stability：PASS（精确限域）

固定 `m` 后，`D_m,R_m` 是固定有限矩阵。标准 Hoffman error bound 给出有限 `H_m`，只依赖 `m` 和所选范数，不依赖右端 `β,c`。对任意多个 `m`-cube blocks 分别应用并把 `l1` 误差相加，仍可使用同一个 `H_m`。

当 `supp(P)\cup supp(Q)\subseteq J`、`|J|=m` 时，每个目标块非空。把源 flow 代入目标块，等式残差由 signed-repair 推出的

\[
\|b_{K,P}-b_{L,Q}\|_1
\le(8/\varepsilon)\|K-L\|_1+2\|P-Q\|_1
\]

控制；容量超限由

\[
\|c_K-c_L\|_1\le(4/\varepsilon)\|K-L\|_1
\]

控制。故双向应用 Hoffman 界得到

\[
d_H^{(1)}(\mathcal F(K,P),\mathcal F(L,Q))
\le H_m\left((12/\varepsilon)\|K-L\|_1+2\|P-Q\|_1\right).
\]

常数只依赖 `ε` 与共同支撑大小 `m`，不依赖 ambient `n`；若两方向各自支撑至多 `s`，可取 `m\le2s`。因此它严格排除了 bounded exact support 的 **pairwise fiber-distance certificate**。

但该结论本身尚未构造在所有不同支撑之间全局兼容的 selector，不能直接升级为“排除 bounded-support 的一切 branching/cycle certificate”。

## 7. attraction to fixed support：PASS 公式；PARTIAL 解释

删除 `J^c` 标号边的质量恰为 `η=\|v_{J^c}\|^2`，散度改变量至多 `2η`；纯态 trace distance 为 `δ=2\sqrt η`。在 fixed `K` 下用 score/signed-repair 控制 `b_{K,Q}-b_{K,Q_J}`，再对保留下来的 `J`-边逐块应用 `H_m`，得到

\[
\operatorname{dist}_1(F,\mathcal F(K,Q_J))
\le \eta+H_m(2\delta+2\eta).
\]

该式正确，但它是一个**绝对吸引界**。若待比较参数距离 `d_n` 比 `\sqrt{\eta_n}` 更快趋零，右端除以 `d_n` 仍可能发散。因此它只在例如

\[
\sqrt{\eta_n}=O(d_n)
\]

这类相对尺度条件下排除 pairwise 放大；仅说“质量大多集中在固定有限集合”不足以排除所有 selector 反例。开头所谓反例必须“genuinely delocalized”，以及第 11 节“directions uniformly concentrated on a fixed finite coordinate set 已被排除”，均超出已证量词。严格可登记的必要条件只有：pairwise fiber-separation 反例的**精确坐标支撑大小必须无界**；更强的定量 delocalization 尚未证明。

## 8. abstract thin path：PASS（仅 coupling 层）

第 9 节不再把 off-diagonal coupling 归一化后误称为原 flow。所列 `2m` 条正支撑边形成交替路径树；列边缘保持不变，只有两个端点行边缘分别改变 `±δ`。零边缘迫使其它允许边质量为零，树上边质量由边缘唯一决定。因此

\[
\|\Pi^1-\Pi^0\|_1=2m\delta,
\qquad
\|\text{marginals}^1-\text{marginals}^0\|_1=2\delta.
\]

比值确为 `m`。它只证明一般 diagonal-plus-cover coupling 几何不能仅靠 marginal `l1` 稳定性得到无维数条件数。其边缘有零原子，不满足 fixed-gap DPP 的 (2.9)，也没有实现为完整 DPP flow polytope；故不是冻结目标反例。这一版已避开第一次回传的 flow-normalization 错误。

## 9. fixed-`n` Steiner point：PASS（常数依赖 `n`）

在 (7.4) 取 `m=n`，得到每个固定 `n` 上的 fiber Hausdorff-Lipschitz 性。edge space 维数为 `N=n2^{n-1}`；Euclidean Hausdorff 距离不超过 `l1` Hausdorff 距离，Steiner point 对 Euclidean Hausdorff 距离有有限维 Lipschitz 常数，再以

\[
\|x\|_1\le\sqrt N\|x\|_2
\]

转回 `l1`。因此确有一个有限但可依赖 `n` 的 Lipschitz selector。Steiner point 对正交变换协变，而坐标置换在 edge space 上是正交置换，故 selector permutation-equivariant；Lipschitz 也蕴含 Borel。此处不能抽取任何 `n` 一致常数，原文没有这样声称。

## 10. universal counterexample mechanisms：PARTIAL / 未全部排除

本轮已排除或压缩的精确机制是：

1. 一端为 coordinate projector 的 pairwise fiber separation；
2. 两端 exact coordinate support 的并集大小一致有界时的 pairwise fiber separation；
3. 仅靠 padding inactive coordinates 制造的上述 pairwise 放大；
4. fixed-gap DPP 原子中的零支撑 alternating path；
5. 把全局 normalization 当作独立自由度；
6. 仅凭一个 fiber 被迫贴住容量上界面的论证；
7. 仅凭单个 rare atom 相对参数不受控移动的论证。

尚未排除：

- full-support 或 support-size 无界方向的 pairwise separation；
- tail mass 很小但比参数距离大得多的 near-support 序列；
- 各 pairwise fiber 距离都受控、但任何同时选择都会在某条边失败的 branching/cycle certificate；
- permutation-equivariance 与全局兼容性造成的 `n` 一致选择障碍；
- 容量、非负性和多参数 face transitions 共同造成的障碍。

因此用户要求的“所有 universal counterexample mechanisms”并未被排除，只排除了上列若干类。第 10 节自己保留 branching/cycle 证书作为可能反例是正确的；第 11 节的总括必须与此保持一致。

## 11. “exact remaining gap” 的最小修正

原文写道，要得到 `PROVED`，“必须”把 `H_m` 替换成 full delocalized manifold 上的统一界，再构造 selector。统一 Hausdorff 界当然是一条充分路线，但不是冻结定理的逻辑必要条件：一个稳定 selector 可能存在，即使整个 fiber set-valued map 没有统一 Hausdorff 模量。应改为：

> One sufficient positive route is a dimension-free Hausdorff estimate followed by a globally compatible equivariant selector. More generally, it suffices to construct such a selector directly.

反面也应写成“足够的 disproof certificates 包括 pairwise fiber separation 或 branching/cycle trapping”，而不是声称它们穷尽所有否定方式。

## 可登记的最强精确结论

可登记为经本轮正文独立审查通过的局部结果：

> 对固定 `0<ε<1/2`，冻结任务的完整非负容量 flow polytope 与 `DPP(K)` 到 `DPP(K+(ε/2)P)` 的 equality-or-one-point-cover couplings 仿射等价。fixed-gap atoms 具有只依赖 `ε` 的逐点乘法正则性。coordinate directions 的 fiber 为显式 singleton，且所有 fibers 在 coordinate direction 附近线性坍缩。若两个 rank-one directions 的坐标支撑并集大小为 `m`，则完整 fibers 的 `l1` Hausdorff 距离满足 (7.4)，常数只依赖 `ε,m` 而与 ambient `n` 无关。近有限支撑时仅有 (8.2) 的绝对吸引界。一般 abstract cover-coupling thin path 仍可有线性条件数，但这只发生在 coupling 层，不能作为 fixed-gap DPP 反例。

## 最终状态

- `source02.md` 自报 `INCOMPLETE`：**PASS**。
- 新核心局部定理：**PASS_SCOPED**。
- “已排除所有 universal counterexample mechanisms”：**FAIL**。
- 整体回传：**PARTIAL**。
- 冻结 `(DF)`：仍为 **INCOMPLETE**；既未 `PROVED`，也未 `DISPROVED`。

最小必要修订只有三项：把“genuinely delocalized”降为“exact support size unbounded”，或补上 tail mass 相对参数距离的量词；把 (8.2) 的排除范围改为绝对吸引/相对尺度版本；把第 11 节的“must”改成“one sufficient route”，并明确 branching/cycle 与其它全局兼容障碍仍开放。

