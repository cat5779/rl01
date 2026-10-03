# 题 1 独立交叉核验

日期：2026-10-02

## 总裁决

**PASS / PROVED.** 我独立重放了 RESULT.md 第 2--5 节的承重链：顶点 iid
生成弧 iid、FUSF 投影核随底图 joint Borel、prescribed-index DPP sampler
对核参数 joint Borel 且对任意索引双射自然、双弧 DPP 忘掉方向得到 FUSF。
当前稿已闭合先前需要澄清的 canonical-representative、MTP 联合法则和多重边
状态空间三处边界；未发现剩余的阻断性缺口。

该裁决只认证当前自包含推导的数学闭合，不认证首次性、穷尽文献检索或形式化验证。

## 1. 随图变化的 Borel 核（**PASS**）

对指定弧 \(a\)，半径 \(n\) 球内的有限环流空间
\(\mathcal C_n(G,a)\) 递增，且其并在全部有限环流的闭包中稠密。有限维投影

\[
 P_{\mathcal C_n}=M(M^*M)^+M^*
\]

的矩阵元只由有限有根球同构类型决定。Moore--Penrose 逆在秩跳变处未必连续，
但在有限矩阵空间上是 Borel，已足够。强极限给

\[
 K_G(a,b)=\lim_n
 \langle(P_G^- -P_{\mathcal C_n})\delta_b,\delta_a\rangle.
\]

所以核矩阵元随带指定弧的图 Borel，并与图同构交换。有限主子式和容斥随即给出
\(G\mapsto\operatorname{FUSF}_G\) 的 Borel probability kernel。

当前第 5.2 节明确采用 Aldous--Lyons §2、printed p. 1461 的 continuous
canonical representative，并由 Angel--Ray--Spinka §2.1 脚注 2 交叉确认。
因此顶点和弧确实组成可数 Borel 纤维，Lusin--Novikov 部分枚举可用于检查所有
有限运算。编号可能随根改变不造成问题：核、sampler 和 OR 映射都对任意索引
双射逐点自然，故输出下降为同一个无标号带根图同构类。

## 2. prescribed-index DPP sampler（**PASS**）

阈值图 \(D_n\) 的度界正确：

\[
 \#\{y:|K_{xy}|\ge1/n\}
 \le n^2\sum_y|K_{xy}|^2
 =n^2(K^2)_{xx}\le n^2.
\]

其半径 \(n\) 球 \(E_n(x)\) 递增并穷尽非零核图中 \(x\) 的分量；不同分量间
核为零，DPP 的有限生成函数因式分解，故分量独立。

有限外场倾斜核

\[
 H=D^{1/2}K_F^{1/2}
 (I-K_F+K_F^{1/2}DK_F^{1/2})^{-1}
 K_F^{1/2}D^{1/2}
\]

覆盖投影核、\(0,1\) 特征值和复 Hermitian 核。由 \(0\le H\le I\) 得

\[
 \sum_y|\operatorname{Cov}(\eta_x,\eta_y)|
 \le2H_{xx}(1-H_{xx})\le\tfrac12.
\]

这个维数无关界足以给漂移在 \(\ell^\infty\) 差上的统一 Lipschitz 控制。
Picard 迭代之间的差自动有界，所以输入路径场不必在索引方向一致有界。

有限窗口 Bayes 权重与 \(X_t=t\eta+B_t\) 一致。窗口鞅收敛、核分量独立和
Brownian bridge 分解给完整历史 posterior；正文又把 innovations 放入同一个
完备右连续滤过，并用有限维条件特征函数识别产品 Brownian 场。整数时刻解码的
单坐标错误概率至多 \(e^{-m/8}\)，对时间可求和；索引集可数，故可同时恢复全部
坐标。所有操作由阈值集合、有限边缘、Picard 极限和逐坐标 Wiener 编码构成，
对任意索引双射逐输入交换。

## 3. unimodularity 边界（**PASS**）

主构造逐确定图成立：条件于任意 \(G\)，弧源是 iid，sampler 输出
\(\mathbf P^{K_G}\)，双弧 OR 输出 FUSF。这里没有交换随机根和其他顶点的期望，
也没有调用 MTP。因此底图法则无需 unimodular、amenable、recurrent、
transient 或有限期望根度。

第 6.1 节现已把反向比较写成正确的条件命题：若
\((G,o,U,M)\) 的**联合标记法则** unimodular，局部预测规则等变，则坏点集
\(S\) 上的质量输送合法，并有

\[
 \mathbb E\#(S\cap B_r(o))
 =\mathbb E[\mathbf1_{\{o\in S\}}|B_r(o)|]=0.
\]

这确实把根处最终正确提升为全图同时正确。当前稿还明确指出，底图、目标和 iid
的 unimodular 边缘不能保证任意联合耦合 unimodular，并用
\(\mathbb Z\) 上公平 proper 2-coloring 的非平稳 root-only 耦合否定刻意的弱读法。
因此先前的 MTP 前提缺口已修复，而且该旁支从未进入主构造。

## 4. 多重边反例（**PASS**）

当前稿采用标准 edge-element multigraph 模型：平行边是边集合中的不同元素，
只是没有 edge/port marks；自同构可固定两个端点而交换平行边，输出分别记录每个
edge element 是否入选。两个顶点、两条平行边的图上，顶点 iid 标签在该交换下
逐点固定，所以任何确定性等变边输出必须给两条边同一状态；UST/FUSF 却必须恰选
一条，两个副本各以概率 \(1/2\) 入选。故纯顶点源全称被反驳。

当前稿同时排除了歧义：若状态空间先把平行边商成一个“重数”坐标，输出只记录
重数，那么从 2 变成 1 可以是确定规则，上述反例不适用。给每个 edge 或
half-edge 独立连续标签后，副本置换几乎必然被打破，双弧 DPP sampler 仍可使用。

## 5. 最终账

| 项目 | 裁决 |
|---|---|
| FUSF 核随底图 joint Borel | **PASS / PROVED** |
| canonical representative 到可数 Borel 纤维 | **PASS / PROVED** |
| DPP sampler 随核 joint Borel | **PASS / PROVED** |
| sampler 对任意索引双射自然 | **PASS / PROVED** |
| 双弧 DPP 忘掉方向得到 FUSF | **PASS / PROVED** |
| 主构造无需 unimodularity | **PASS / PROVED** |
| 第 6.1 节 MTP 的联合标记法则前提 | **PASS / 已修复** |
| root-only 弱读法反例 | **PASS / DISPROVED** |
| 两平行边、纯顶点源反例（edge-element 模型） | **PASS / DISPROVED** |
| 首次性与穷尽文献状态 | **INCOMPLETE / NOT CERTIFIED** |
