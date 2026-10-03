# 题 1 独立数学与来源审计

日期：2026-10-02

## 总裁决

**PROVED（简单图约定）。** 我逐段复算了 RESULT.md 的标签转换、FUSF 投影核、核随底图的联合 Borel 性、可数指标 DPP 采样器、双弧 pushforward 和 rerooting 接口。最终规则对底图、核与 iid 标记联合 Borel，与所有图同构逐点交换，并且不读取根。证明不使用 unimodularity、amenability、recurrence、transitivity 或有限期望度。

**DISPROVED（无标记多重图、纯顶点 iid）。** 两个顶点之间有两条不可区分平行边时，UST/FUSF 必须均匀选择一条边；固定顶点而交换两条边的自同构固定全部顶点标签，所以任何确定性等变顶点因子只能给两条边相同状态。正文已经显式分离这一边界，没有隐藏 simple 假设。

**INCOMPLETE（新颖性认证）。** 本轮打开的最新指定原文仍把一般 FUSF 因子问题列为开放，且未定位到同量词的公开定理；这不能证明首创性。正文把数学结论与新颖性状态分开，处理正确。

## 承重证明链

### 1. 定义与标签源

**PROVED.** 正文使用 Angel--Ray--Spinka §2.1 的 graph factor 定义：定义域是带标记有根图同构类，映射 measurable、保持底图并对 rerooting 不变。主结论要求一个全局规则，而不是对每个 \(G\) 或每个群作用另选一个零测版本。

**PROVED.** 对局部有限简单图，顶点 iid 可自然地产生弧 iid。每个顶点标签拆成一个 key 和可数 iid 槽；弧 \((v,w)\) 使用 \(w\) 的 key 在 \(N(v)\) 中的秩指定的槽。给定全部 key 后，不同弧使用不同的“尾点--槽”坐标，因此弧标签条件独立同分布。局部有限保证秩有限，简单性保证同一尾点的不同弧有不同头点。key 并列为零测事件，正文的全定义约定仍逐点等变。

**PROVED.** 弧 iid 到顶点 iid 的最小值变换在每个非孤立顶点上正确；不同尾点的弧集合互不相交。单点图没有弧随机源，但其 FUSF 确定为空。

**DISPROVED（无条件标签等价）。** Angel--Ray--Spinka p. 7 关于 vertex/edge/both labels 等价的无保留字面读法不能覆盖所有有限图：简单图 \(K_2\) 的唯一无向边标签在端点交换下固定，不能产生两个 iid 非退化顶点标签；\(K_1\) 没有边随机源。正文只使用已证明的 vertex-to-arc 方向，并单列 \(K_1,K_2\) 与平行边边界。

### 2. FUSF 核与联合 Borel 性

**PROVED.** Benjamini--Lyons--Peres--Schramm Theorem 7.8 给出无限图 transfer-current 行列式公式，其后明确把 FSF 核识别为有限环空间正交补投影。正文在反对称双弧空间写成

\[
K_G=P_G^- - P_{\mathcal C_G},
\]

与选定参考方向后的通常核酉等价。

**PROVED.** 对指定弧 \(a,b\)，半径 \(n\) 球中的有限环流张成有限维空间。有限矩阵、Moore--Penrose 逆和投影矩阵元随有限球类型 Borel；有限环空间递增稠密于全部有限环流闭包，故投影强收敛。于是 \(K_G(a,b)\) 是 Borel 函数的逐点极限，并满足

\[
K_H(\theta a,\theta b)=K_G(a,b).
\]

正文已澄清 \(\mathcal C_n(G,a)\) 只是计算指定矩阵元的有限维逼近，不把依赖 \(a\) 的有限阶段误称为统一 DPP 核。

### 3. 自然且联合 Borel 的可数 DPP 采样器

这是从 fixed-action existence 升级到 universal graph factor 的核心。

1. **PROVED：有限阈值窗口。** 由
   \[
   \sum_y|K_{xy}|^2=(K^2)_{xx}\le K_{xx}\le1
   \]
   可知关系 \(|K_{xy}|\ge1/n\) 的度至多 \(n^2\)。相应半径 \(n\) 球有限、嵌套，并穷尽非零核图的连通分量。不同分量间核为零，DPP 柱概率因式分解。

2. **PROVED：统一协方差界。** 有限 DPP 经 \(e^{h\cdot\eta}\) 倾斜后仍为 DPP；正文的对称核公式允许 \(K\) 或 \(I-K\) 奇异，并覆盖复 Hermitian 项。对新核 \(H\)，
   \[
   \sum_y|\operatorname{Cov}(\eta_x,\eta_y)|
   \le 2H_{xx}(1-H_{xx})\le\tfrac12.
   \]
   因而漂移有与维数、窗口及外场无关的 sup-norm Lipschitz 常数。

3. **PROVED：total Borel 漂移。** 有限配置概率由主子式容斥给出；阈值窗口、有限行列式和有限求和均 Borel。Lusin--Novikov 枚举只用于证明变化纤维上的可测性，实际公式由无序有限集合定义，所以不会破坏任意双射自然性。

4. **PROVED：无限 Picard 解。** Brownian 场在空间指标上几乎必然不有界，但迭代只估计解之间的有界修正。漂移有界且对 bounded differences 为 \(1/2\)-Lipschitz，阶乘界给每个有限时间区间上的一致收敛、路径唯一和对核参数的联合 Borel 性。

5. **PROVED：posterior 与完整历史。** 在 \(X_t=t\eta+B_t\) 中，有限 Gaussian Bayes 与窗口鞅收敛给 snapshot posterior。对有限坐标和有理时刻作 Brownian bridge 分解，再以连续路径的有理时刻生成性和单调类扩张，得到给定完整观察历史的 posterior。正文使用 \(dt\otimes d\mathbb P\) 版本与时间 Fubini，没有对不可数时刻取零测集交。

6. **PROVED：共同 usual filtration 中的 innovations。** 终稿先在原始观察滤过下直接验证鞅增量，再传到完备右连续化；有限变差漂移不改变二次协变差。有限坐标向量的 Lévy 特征给出 Gaussian 增量及其对共同过去的独立性，所以整场 innovations 是产品 Brownian，而不只是两两零协方差。

7. **PROVED：同噪声解码。** 路径唯一性给 \(X=\mathcal Z_K(\beta)\)。整数时刻以 \(m/2\) 阈值解码，每坐标错误概率可求和；Borel--Cantelli 与指标集可数性给全部坐标同时最终正确。坐标级 total Borel 的 Uniform-to-Brownian 映射完成采样器。

8. **PROVED：变化底图的 joint Borel 接口。** 标准有根图空间可取 Borel 编号代表；Angel--Ray--Spinka 正式版 p. 7 footnote 2 也明确调用 canonical representative。编号只用于可测性验证；核、采样器与 OR 映射对所有双射自然，故换代表后输出相同的标记有根图同构类。正文没有把 \(\mathcal G_{**}\) 的自同构轨道商误当作实际顶点纤维。

### 4. 双弧 DPP 忘掉方向

**PROVED.** 反对称等距嵌入 \(T\) 给 \(K_G=TQ_GT^*\)。同一无向边的两弧主块行列式为零，因此两方向不会同时出现。对 \(k\) 条无向边的每个方向选择，主子式等于 \(2^{-k}\det(Q_G)_B\)；把 \(2^k\) 个选择相加得到

\[
\mathbb P(B\subseteq\pi(Y))=\det(Q_G)_B.
\]

所以 OR pushforward 正是 FUSF。OR 在异常输入上也全定义并与同构交换。

### 5. 统一 graph factor 与 root invariance

**PROVED.** 最终映射依次执行 vertex-to-arc、\(G\mapsto K_G\)、自然 DPP sampler 和双弧 OR。四步都 joint Borel，且对任意保持输入标记的图同构逐点交换。规则不读取根，所以换根得到同一无根边配置。该论证逐图成立，再对任意随机有根图分布条件化即可；无须 mass-transport principle。

## 指定原文核对

### Timár, arXiv:2306.15120v2

实际打开 2025-12-16 的 v2 并核对：

- **Theorem 1：** a.s. recurrent 的 unimodular random graph，其 USF 是 factor of iid；
- **Theorem 2(1)：** invariantly amenable URG 的 USF 是 finite-valued finitary fiid；
- **Example 3.1：** FUSF 是 compatible monotone decreasing limit；
- **Theorem 4：** invariantly amenable URG 上 compatible monotone weak limit 是 factor of iid；
- **Corollary 5：** invariantly amenable URG 的 USF 是 factor of iid，特别包括 recurrent 情形；
- 引言在 Theorem 1 后明确说一般 FUSF 是否 factor of iid 仍开放。

正文没有把这些受 invariant amenability/unimodularity 限制的结果写成一般随机图定理。

**PROVED（前向）。** ARS graph factor 可由有限有根标记球在根处以任意小错误逼近；这只用标准 Borel \(\sigma\)-代数的有限球生成性，不需 unimodularity。

**PROVED（有联合前提的反向）。** 若 iid labels、目标 decoration 与底图位于同一个联合 unimodular marked coupling，且同一列局部规则在根处错误概率趋零，则可取可求和子序列。Borel--Cantelli 先给根处最终正确；对坏点集应用该联合 marked law 的 MTP，得到所有顶点同时最终正确，再取逐点极限得到 ARS graph factor。

**DISPROVED（任意耦合的 root-only 弱读法）。** 仅有底图、目标与 iid 三个 marginal 正确，不保证共同耦合 unimodular。固定 \((\mathbb Z,0)\)，令 \(U\) iid，并置

\[
M_v=\mathbf1_{\{U_0<1/2\}}\oplus\bigl(\operatorname{dist}(0,v)\bmod2\bigr).
\]

\(M\) 的 marginal 是两个 proper 2-colorings 的公平混合，因而是 unimodular；根标记由 \(U_0\) 在半径零完美预测。但它不是 graph factor iid：若 \(f(U)\) 是一个 shift-equivariant factor 的原点颜色，则 proper coloring 要求 \(f(TU)=1-f(U)\)，从而 \(f(T^2U)=f(U)\)；Bernoulli shift \(T^2\) 的 ergodicity 迫使 \(f\) a.s. 常数，矛盾。该例只否定刻意的弱字面读法，不断言这是 Timár 的作者本意。

### Angel--Ray--Spinka, EJP 29 (2024), paper 39

实际打开正式 EJP 文本并核对：

- **§2.1：** graph factor、rerooting、顶点函数与对换双根对称的边函数；
- **Theorem 1.4 / 4.1：** 任意 a.s. transient 随机有根图的 WUSF 是 graph factor iid，不要求 unimodularity；
- **Question 6.1：** recurrent unimodular random rooted graph 的 wired UST 问题。

该文没有给一般 FUSF 结论。正文对其标签等价句增加必要边界，没有把该句当作无条件黑箱。

### 公开候选材料

- [prescribed-index DPP 候选定理](https://github.com/cat5779/rl01/pull/85)只冻结 fixed countable \(W\) 与 fixed action 的结论，并明确不包含 varying-graph joint Borel；正文第 4--5 节补出了参数化与自然性链。
- [directed-double-cover 接口审查](https://github.com/cat5779/rl01/pull/91)只处理固定图和可数群作用，并明确标出 full automorphism group 与 varying graph 边界；正文重推 pushforward 并补齐联合 Borel 接口。

这些材料的“状态”没有被当作证明证据。

## 未覆盖边界

- **INCOMPLETE：finitary/finite-valued。** Brownian/Picard 构造没有有限 coding radius 或有限随机位保证；正文未声称这些加强。
- **INCOMPLETE：形式化与新颖性认证。** 当前没有 proof assistant、期刊外审或穷尽前向引用检索。
- **DISPROVED：纯顶点源的无标记多重图推广。** 恢复多重图结论需要 edge/half-edge iid、ports 或其他能区分平行边的输入。

## 最终状态表

| 主张 | 裁决 |
|---|---|
| 任意随机局部有限连通无向简单有根图的 FUSF 是 ARS 意义的 graph factor iid | **PROVED** |
| 规则可统一选取为随底图与标签 joint Borel、全同构自然且 root-free | **PROVED** |
| 主定理无须 unimodularity/amenability/recurrence | **PROVED** |
| 纯顶点 iid 下无条件推广到不可区分平行边 | **DISPROVED** |
| vertex/edge/arc iid 在所有有限图上无保留等价 | **DISPROVED** |
| Timár root-only 弱读法在无联合 unimodular coupling 时反推 graph factor | **DISPROVED** |
| finitary、finite-valued 或首创性 | **INCOMPLETE** |
