# 题 1：随机有根图上的 FUSF 是否为 graph factor of iid？

四条主线的英文数学稿见 [paperA.md](paperA.md)；新增的原文核查见 [sources01.md](sources01.md)，独立可读性复核见 [read01.md](read01.md)。本文件保留题 1 的完整专题证明。

## 结论与状态

### 主结论（简单图约定）

**PROVED.** 设 \((G,o)\) 是任意随机的、局部有限、连通、无向**简单**有根图；其分布只须是下述标准 Borel 有根图空间上的概率测度。给定 \(G\)，在每个顶点放一个独立的 \(\operatorname{Unif}[0,1]\) 标签。存在一个与有根同构相容、对换根不变且联合 Borel 的图因子 \(\Phi\)，使得
\[
  \mathcal L\bigl(\Phi(G,o,U)\mid G,o\bigr)=\operatorname{FUSF}_G.
\]
更强地，规则本身不使用 \(o\)：若把同一带标签图从另一顶点重新取根，所得无根边配置完全相同。结论对每个确定的局部有限连通简单图逐图成立，所以底图的分布不必 unimodular。

### 若允许不可区分的平行边

**DISPROVED.** 若“graph”包括没有额外 edge/port marks 的多重图，同时 graph factor 的随机源严格限定为顶点 iid，则上述全称命题为假。这里采用通常的 multigraph configuration space：两条平行边是两个独立 edge elements，允许自同构交换它们，森林输出也分别记录每个 edge element 是否入选；若只记录边重数而把平行边先商掉，那是另一个输出空间。最小反例是两个顶点之间有两条平行边的有限图：FUSF 就是均匀生成树，必须以概率 \(1/2\) 选择两条边中的每一条；但交换这两条平行边、固定两个顶点的图自同构固定所有顶点标签，因此任何确定性等变顶点因子都必须给两条边相同状态，不可能恰选一条。

若在多重图中另给每条边或每条 half-edge/arc 独立标签，下面的 DPP 采样部分仍适用；失败的是“只用顶点标签却要打破平行边置换对称性”这一步。

### 新颖性与公开状态

**INCOMPLETE / NOT CERTIFIED.** 本文给出完整数学闭合链，但没有领域专家外审、全文形式化或穷尽前向引用检索，因而不声称首次证明。检索到的最新原始陈述中，Timár 的 arXiv:2306.15120v2（2025-12-16）仍明确写道一般 FUSF 是否为 factor of iid 是开放的；本结论若经外部认证，会回答其在简单图 graph-factor 解释下的全量词问题。

---

## 1. 精确定义

### 1.1 有根同构与 Borel 空间

记 \(\mathcal G_*\) 为局部有限、连通、无向简单图与一个根 \(o\) 的有根同构类空间；\(\mathcal G_{**}\) 类似，但带有有序的两个指定顶点。若顶点、边或弧带有 Polish 空间 \(M\) 中的标记，则记相应空间为 \(\mathcal G_*^M\)、\(\mathcal G_{**}^M\)。

两个带标记有根图 \((G,o,m)\)、\((H,p,n)\) 有根同构，是指存在图同构 \(\theta:G\to H\)，满足 \(\theta(o)=p\)，并保持所有相应标记。空间取局部拓扑及其 Borel \(\sigma\)-代数：半径越来越大的有根球同构，且球内标记越来越接近。局部有限性使每个有限半径球有限；这些空间是标准 Borel 空间。

### 1.2 顶点、边与弧标签

对图 \(G=(V,E)\)：

* **顶点 iid**：\(U=(U_v)_{v\in V}\)，条件于 \(G\) 独立同分布为 \(\operatorname{Unif}[0,1]\)；
* **边 iid**：\(X=(X_e)_{e\in E}\)，条件于 \(G\) 独立同分布；
* **弧 iid**：令
  \[
    A(G)=\{(v,w):\{v,w\}\in E\},
  \]
  两个方向视为不同坐标；\(Y=(Y_a)_{a\in A(G)}\) 条件于 \(G\) 独立同分布。

“iid”总是指在给定底图后的条件分布。一个 \([0,1]\) 标签可用固定的 total Borel 数位拆分映射编码成可数多个独立 \([0,1]\) 标签；dyadic 点和端点采用固定二进制表示，零测例外不会使映射失去全定义性。

### 1.3 rerooting 与 graph factor

图因子是一个 Borel 映射
\[
  \Phi:\mathcal G_*^M\longrightarrow \mathcal G_*^N,
  \qquad [G,o,m]\longmapsto [G,o,m'],
\]
它保持底图，并且输出不依赖根的位置：若以同一 \((G,m)\) 的另一顶点 \(v\) 为根，则输出仍是同一个无根标记 \(m'\)。

等价地，顶点输出由某个 Borel \(F([G,v,m])\) 给出，边输出由对交换两根对称的 Borel 函数
\[
  F'([G,u,v,m])=F'([G,v,u,m])
\]
给出。这个定义自动蕴含有根同构自然性：每个保持输入标记的同构也保持输出标记。

随机标记 \((G,o,M)\) 是 **graph factor of iid**，若存在顶点 iid 标记 \(U\) 和这样的 \(\Phi\)，使 \(\Phi(G,o,U)=(G,o,M)\) a.s.。这是 Angel--Ray--Spinka 2024 第 2.1 节的正式定义。

### 1.4 unimodularity

随机有根（可带标记）图的分布 \(\mu\) 称为 unimodular，如果对每个非负 Borel mass transport \(f\) 都有
\[
 \int\sum_{x\in V(G)} f(G,o,x)\,d\mu
 =
 \int\sum_{x\in V(G)} f(G,x,o)\,d\mu.
 \tag{MTP}
\]
本证明不用 (MTP)。若输入底图是 unimodular，则加 iid 标记仍 unimodular，而 graph factor 保持 unimodularity；这只说明输出的附加性质，不是构造 FUSF 的前提。

### 1.5 FUSF 与其 DPP 核

对有限连通图，FUSF 是均匀生成树。对无限局部有限连通图，取任意递增有限连通 exhaustion \(G_n\uparrow G\)，\(\operatorname{UST}(G_n)\) 的边柱事件极限存在且与 exhaustion 无关，定义 \(\operatorname{FUSF}_G\)。

用弧空间给出无定向选择的规范版本。令 \(R:A(G)\to A(G)\) 为反向弧 involution，\(\bar a=Ra\)。在普通 \(\ell^2(A(G))\) 中令
\[
 H_G^-:=\{f:f(\bar a)=-f(a)\},\qquad P^-_G=(I-R)/2.
\]
每条有限有向简单环给出一个反对称环流向量；令 \(\mathcal C_G\) 为这些向量张成空间的闭包，并置
\[
 \mathcal H_G:=H_G^-\cap \mathcal C_G^\perp,
 \qquad K_G:=P_{\mathcal H_G}=P_G^- - P_{\mathcal C_G}.
 \tag{1}
\]
于是 \(K_G\) 是 \(\ell^2(A(G))\) 上的 Hermitian 正投影。BLPS 的无限图 Transfer Current Theorem 7.8 说明，无向边 FUSF 是有限环空间正交补投影的 DPP；式 (1) 是其不选参考方向的双弧写法。

---

## 2. 标签模型的精确比较

### 2.1 顶点 iid \(\Rightarrow\) 弧 iid（简单局部有限图）

**PROVED.** 把每个 \(U_v\) Borel 拆成
\[
 (A_v,B_{v,0},B_{v,1},\ldots),
\]
其中全部坐标在 iid 输入下相互独立且均匀。对弧 \((v,w)\)，令
\[
 r_v(w)=\#\{z\sim v:A_z<A_w\},\qquad
 Y_{(v,w)}=B_{v,r_v(w)}.
 \tag{2}
\]
有并列时仍按 (2) 定义，所以映射对所有输入 total 且等变；在概率一的“所有顶点 key 互异”事件上，同一尾点发出的不同弧使用不同槽，不同尾点使用不同顶点的槽。条件于全部 key，所有所选槽仍相互独立均匀，故 \(Y\) 是弧 iid。局部有限性恰用于保证 \(r_v(w)<\infty\)，简单性恰用于保证同一尾点的不同弧有不同头点。

同理，把无向边分配给 key 较小的端点，再用另一端在该端点邻居 key 中的排名选槽，可得边 iid。

### 2.2 弧 iid \(\Rightarrow\) 顶点 iid（非平凡连通图）

**PROVED.** 若 \(d(v)\ge1\)，令 \(M_v\) 为所有从 \(v\) 发出弧标签的最小值，定义
\[
 U_v=1-(1-M_v)^{d(v)}.
\]
从不同顶点发出的弧集合不交，因此 \((U_v)\) 独立；最小次序统计的分布函数给出每个 \(U_v\sim\operatorname{Unif}[0,1]\)。单顶点无边图没有弧随机源，但其 FUSF 是确定空集。

所以，在非平凡局部有限连通简单图上，顶点 iid 与有向弧 iid 对 graph-factor 构造确实等价。

### 2.3 边 iid 与顶点 iid 并非无条件等价

**DISPROVED（全体图上的字面全称）.** 在简单图 \(K_2\) 上只有一个无向边标签。交换两个顶点保持该边标签不变；任何等变地产生的两个顶点标记必须相同，故不能得到两个独立非退化顶点标签。单顶点图给出更平凡的无边源障碍。

**PROVED（连通简单图且至少三个顶点）.** 反方向的边源到顶点源也可在这一范围构造。把每条边标签拆成连续 edge-name 和两个独立 streams。每个顶点以其有限 incident edge-name 集合的排序元组作为 vertex signature。全局 edge-name 互异的概率一事件上，相邻顶点 signature 相同当且仅当连通分量是 \(K_2\)，故这里每条边的两端可由 signature 规范排序，并把两个 streams 分配给两端。每个顶点选择 incident edge-name 最小的边，读取分给自己的 stream。条件于 names，不同顶点读取不同的“边--端点”stream 坐标，即使相邻两顶点选中同一条边也读取它的两个独立 streams，因此所得顶点标签 iid。零测并列事件统一输出常数即可保持 total Borel 和等变。

因此 Angel--Ray--Spinka 第 2.1 节“vertex/edge/both labels 都等价”的句子若被读成包括所有有限图、所有输出类型的无保留全称，字面上不成立；在其许多简单非退化应用中可用上述转换修复。本文主证明只需要 2.1 的顶点 \(\Rightarrow\) 弧方向。

---

## 3. FUSF 核随底图联合 Borel

这是固定图结论升级为随机图 graph factor 时不能省略的承重步骤。

### 命题

**PROVED.** 在带两个指定弧的局部有限连通简单图空间上，
\[
  (G,a,b)\longmapsto K_G(a,b)
\]
是 Borel，并且对每个图同构 \(\theta:G\to H\)，
\[
 K_H(\theta a,\theta b)=K_G(a,b).
 \tag{3}
\]

### 证明

固定弧 \(a\)，令 \(\mathcal C_{n}(G,a)\) 为所有完全包含在尾点 \(t(a)\) 的半径 \(n\) 球中的有限环流所张成的空间。该球有限，所以环流候选有限，\(\mathcal C_n\) 有限维。把这些向量排成有限矩阵，正交投影可写成
\[
 P_{\mathcal C_n}=M(M^*M)^+M^*,
\]
其中 \({}^+\) 是 Moore--Penrose 逆。无需在无标号有限球中作不自然的次序选择：投影与环向量的排列和定向无关，而每个带指定弧的有限球只有可数多个组合同构类型；每个类型上的相应矩阵系数固定。因此有限球、其全部有限环、有限矩阵运算和 Moore--Penrose 逆共同给出 Borel 函数；重复环或线性相关不影响公式。

连通性保证每个有限环最终落入这些球，故
\[
 P_{\mathcal C_n}\xrightarrow[n\to\infty]{\rm strong}P_{\mathcal C_G}.
\]
于是
\[
 K_G(a,b)
 =\lim_{n\to\infty}
 \langle(P^-_G-P_{\mathcal C_n(G,a)})\delta_b,\delta_a\rangle,
 \tag{4}
\]
是 Borel 函数的逐点极限。所有对象只由有根有限球和环空间定义，故同构自然性 (3) 逐个 \(n\) 成立，极限后仍成立。\(\square\)

这里的 \(\mathcal C_n(G,a)\) 只是在计算指定矩阵元 \(K_G(a,b)\) 时所用的逐坐标有限维逼近；并未声称对同一个 \(n\) 它在所有 \(a\) 上组成全局有限阶段 DPP 核。最终的 \(K_G\) 才是统一的正投影核。

特别地，每个有限指定边集的 FUSF 包含概率是 \(K_G\) 的相应有限主子式（在第 5.1 节的双弧表示下等价）；每个精确有限 \(0/1\) 柱事件再由有限容斥得到。因此这些柱概率随有根图 Borel，且柱事件生成森林配置空间的 Borel \(\sigma\)-代数。故 \(G\mapsto\operatorname{FUSF}_G\) 本身是一个 Borel probability kernel。**PROVED.**

---

## 4. 一个自然且可参数化的 DPP 因子引理

### 引理（prescribed-index DPP sampler）

**PROVED.** 对任意可数集 \(W\) 和 Hermitian 正压缩 \(0\le K\le I\)，存在 total Borel 映射
\[
  \mathfrak S_K:[0,1]^W\to\{0,1\}^W
\]
把产品 Lebesgue 测度推到 \(\mathbf P^K\)。而且该构造对所有双射自然：若 \(\theta:W\to W'\)，则对每个输入 \(u\)
\[
 \mathfrak S_{\theta K\theta^{-1}}(\theta u)
 =\theta\mathfrak S_K(u).
 \tag{5}
\]
若 \((s,x,y)\mapsto K_s(x,y)\) 是标准 Borel 参数族，且 \(W_s\) 是可数 Borel 纤维，则 \((s,u)\mapsto\mathfrak S_{K_s}(u)\) 也可取为联合 Borel。

若 \(W=\varnothing\)，取唯一空映射；以下假定 \(W\ne\varnothing\)。

以下给出承重证明链，而不把“已有审查通过”当作数学证据。

### 4.1 有限阈值窗口

令 \(D_n\) 在不同 \(x,y\) 间连边当且仅当 \(|K_{xy}|\ge1/n\)，令 \(E_n(x)\) 为 \(D_n\) 中以 \(x\) 为中心的半径 \(n\) 球。因为
\[
 \sum_y|K_{xy}|^2=(K^2)_{xx}\le K_{xx}\le1,
\]
\(D_n\) 的度至多 \(n^2\)，故 \(E_n(x)\) 有限。它们随 \(n\) 递增，并穷尽非零核图中 \(x\) 的连通分量。不同分量间 \(K\) 为零；主子式和容斥因式分解说明 DPP 在这些完整分量上联合独立。

在 Borel 参数族中，关系 \(|K_{xy}|\ge1/n\) 是 Borel 且局部有限；有限长度路径、有限球及其对称有限集合运算因此 Borel。

更明确地说，Lusin--Novikov 定理给可数 Borel 纤维 \(W_s\) 的可数个 Borel 部分枚举。用这些枚举只作可测性验证：有界长度路径关系是有限次 Borel 关系合成，局部有限的 \(E_n(x)\) 可由部分枚举列出，(7) 中的有限配置、有限行列式和有限求和遂都是 Borel。不同枚举给出同一个由集合 \(E_n(x)\) 定义的公式；算法本身没有采用枚举次序。因此这个验证不会削弱 (5) 对任意双射的逐点自然性。

### 4.2 任意外场下的维数无关协方差界

设 \(K_F\) 是任意有限压缩，\(h\in\mathbb R^F\)。用密度 \(e^{h\cdot\eta}\) 倾斜有限 DPP 后仍为 DPP，且新核仍是 Hermitian 正压缩。一个不要求 \(K_F\) 或 \(I-K_F\) 可逆的公式是
\[
 D=\operatorname{diag}(e^{h_z}),\quad
 M=I-K_F+K_F^{1/2}DK_F^{1/2},\quad
 H=D^{1/2}K_F^{1/2}M^{-1}K_F^{1/2}D^{1/2}.
\]
因 \(M\ge \min(1,\min D_{zz})I>0\) 且 \(M\ge K_F^{1/2}DK_F^{1/2}\)，有 \(0\le H\le I\)。生成多项式和 \(\det(I+AB)=\det(I+BA)\) 验证倾斜律正是 \(\mathbf P^H\)。这覆盖投影核、特征值 \(0,1\)、复 Hermitian 项和确定坐标。

若 \(p=H_{xx}\)，DPP 的一、二点主子式给出
\[
 \operatorname{Var}(\eta_x)=p(1-p),\qquad
 \operatorname{Cov}(\eta_x,\eta_y)=-|H_{xy}|^2\quad(y\ne x).
\]
故
\[
 \sum_y|\operatorname{Cov}(\eta_x,\eta_y)|
 =p(1-p)+(H^2)_{xx}-p^2
 \le2p(1-p)\le\tfrac12.
 \tag{6}
\]

### 4.3 total Borel 漂移与 Picard 解

记 \(\mu_F\) 为 \(\mathbf P^K\) 在有限 \(F\) 上的实际边缘。对所有实场 \(y\in\mathbb R^W\) 定义
\[
 b^n_{t,x}(y)=
 \frac{\sum_{\sigma\in\{0,1\}^{E_n(x)}}
 \sigma_x\mu_{E_n(x)}(\sigma)
 e^{\sum_z(y_z-t/2)\sigma_z}}
 {\sum_{\sigma\in\{0,1\}^{E_n(x)}}
 \mu_{E_n(x)}(\sigma)
 e^{\sum_z(y_z-t/2)\sigma_z}},
 \quad b_{t,x}(y)=\limsup_n b^n_{t,x}(y).
 \tag{7}
\]
分母严格正。有限配置概率由
\[
 \mu_F(\eta|_F=1_S)
 =\sum_{S\subseteq T\subseteq F}(-1)^{|T\setminus S|}\det K_T
\]
给出，所以 (7) 对 \((K,t,y,x)\) 联合 Borel。由 (6) 沿线段积分，若 \(y-y'\in\ell^\infty(W)\)，则
\[
 \sup_x|b_{t,x}(y)-b_{t,x}(y')|
 \le\tfrac12\|y-y'\|_\infty.
 \tag{8}
\]

对每个（不要求空间有界的）连续路径场 \(w\) 作 Picard 迭代
\[
 Z^{0}=w,\qquad
 Z^{k+1}_t(x)=w_t(x)+\int_0^t b_{s,x}(Z^k_s)\,ds.
 \tag{9}
\]
只对迭代差使用 \(\ell^\infty\) 范数；由 (8)
\[
 \sup_{x,s\le T}|Z^{k+1}_s(x)-Z^k_s(x)|
 \le \frac{(1/2)^kT^{k+1}}{(k+1)!}.
\]
故 (9) 对每个输入在有界时间区间一致收敛，给出唯一解 \(Z=\mathcal Z_K(w)\)。Borel 参数积分、逐次极限和有理时刻坐标说明 \((K,w)\mapsto\mathcal Z_K(w)\) 联合 Borel。所有公式只使用核、有限集合和坐标运算，故满足 (5) 的自然性。

### 4.4 法则识别和同噪声解码

在辅助空间取 \(\eta\sim\mathbf P^K\) 与 iid Brownian 场 \(B\) 独立，令
\[
 X_t(x)=t\eta_x+B_t(x).
\]
有限 Gaussian Bayes、\(E_n(x)\) 向完整核分量递增以及不同分量独立，给出
\[
 b_{t,x}(X_t)=\mathbb E[\eta_x\mid X_t(z),z\in W].
\]
Brownian bridge场与 \((\eta,B_t)\) 独立，所以右边也是给定完整观察历史的后验。联合可测性和时间 Fubini 避免对不可数时刻取概率一事件交。

把这一步展开如下。令
\[
 \mathcal F_t^0=\sigma\{X_r(z):0\le r\le t,\ z\in W\}.
\]
对有限坐标集和有理时刻，分解
\(X_r(z)=(r/t)X_t(z)+[B_r(z)-(r/t)B_t(z)]\)。方括号内的有限 Brownian bridge 向量与 \((\eta,(X_t(z))_{z\in W})\) 独立。先对有限坐标柱事件验证，再用有理时刻生成连续路径的 Borel \(\sigma\)-代数，并作两次单调类扩张，得到
\[
 m_t(x):=b_{t,x}(X_t)=\mathbb E[\eta_x\mid\mathcal F_t^0]
 \tag{9a}
\]
对 \(dt\otimes d\mathbb P\) 几乎处处成立。这里有限窗口 posterior 是
\(\mathbb E[\eta_x\mid X_t(z),z\in E_n(x)]\)；向上鞅收敛、核分量之间的独立性和 \(E_n(x)\) 穷尽分量给出 (9a)。因此只需要时间 Fubini 选取一个共同的 \(dt\otimes d\mathbb P\) 版本，不需要声称每个实数时刻的零测例外同时消失。

创新过程
\[
 \beta_t(x)=X_t(x)-\int_0^t b_{s,x}(X_s)\,ds
\]
先是原始滤过 \((\mathcal F_t^0)\) 下的连续鞅。事实上，对 \(0\le s<t\) 和有界 \(A\in\mathcal F_s^0\)，条件 Fubini 与 (9a) 给
\[
\begin{aligned}
 \mathbb E[\mathbf1_A(\beta_t(x)-\beta_s(x))]
 &=\mathbb E[\mathbf1_A(B_t(x)-B_s(x))]\\
 &\quad+\int_s^t
   \mathbb E[\mathbf1_A(\eta_x-m_r(x))]\,dr=0.
\end{aligned}
\tag{9b}
\]
第一项为零，因为 Brownian 增量独立于 \((\eta,B_{[0,s]})\)；第二项为零，因为
\(A\in\mathcal F_s^0\subseteq\mathcal F_r^0\) 且 \(m_r(x)=\mathbb E[\eta_x\mid\mathcal F_r^0]\)。被积量有界，故条件 Fubini 合法。

现在令 \((\mathcal F_t)\) 为 \(X\) 的完备右连续化。取 \(s_k\downarrow s\)。对 \(A\in\mathcal F_s=\bigcap_k\mathcal F_{s_k}^0\)（补零集后理解），原始鞅等式在 \(s_k\) 成立；downward martingale convergence 连同
\[
 \mathbb E|\beta_{s_k}(x)-\beta_s(x)|
 \le \sqrt{s_k-s}+(s_k-s)\longrightarrow0
\]
把它传到 \(s\)。故 \(\beta(x)\) 是同一个 usual filtration 下的连续鞅。

又因
\(\beta(x)=B(x)+\int_0^\cdot(\eta_x-m_r(x))dr\)，第二项连续且有限变差，有限变差项与任何连续半鞅的二次协变差为零，从而
\[
 [\beta(x),\beta(y)]_t=[B(x),B(y)]_t
 =\mathbf1_{x=y}t.
\tag{9c}
\]
对任意有限不同坐标 \(x_1,\ldots,x_d\) 和 \(\lambda\in\mathbb R^d\)，Itô 公式表明
\(\exp\{i\lambda\cdot\beta_t+\tfrac12|\lambda|^2t\}\) 在每个有限时间区间是复鞅。因此
\[
 \mathbb E[e^{i\lambda\cdot(\beta_t-\beta_s)}\mid\mathcal F_s]
 =e^{-|\lambda|^2(t-s)/2}.
\tag{9d}
\]
这同时给出有限向量增量的标准 Gaussian 法则及其对过去的独立性，而非只给两两零协方差。有限维 L\'evy 特征与 \(W\) 的可数性遂说明整场 \(\beta\) 是产品 Brownian。路径唯一性又给 \(X=\mathcal Z_K(\beta)\)，不是仅有弱收敛。

定义
\[
 \mathfrak S_K(w)_x=\liminf_{m\to\infty}
 \mathbf1\{\mathcal Z_K(w)_m(x)>m/2\}.
 \tag{10}
\]
在上述耦合中，每个 \(m\) 的错误概率至多 \(e^{-m/8}\)。Borel--Cantelli 和 \(W\) 可数性说明 (10) 同时恢复全部 \(\eta_x\)。最后用一个固定 total Borel 映射把每站 \([0,1]\) 标签送到 Brownian 路径；例如数位拆成独立正态并作 dyadic bridge，在不收敛的 Borel 零测集输出零路径。由此得到引理。\(\square\)

---

## 5. 应用于 FUSF，并闭合 joint-Borel 缝

### 5.1 双弧 DPP 忘掉方向恰为 FUSF

固定任意参考方向，只用于本段验算。令 \(Q_G\) 为参考定向无向边空间上“有限环空间正交补”的投影，并定义等距嵌入
\[
 (Tf)(e^+)=f(e)/\sqrt2,\qquad (Tf)(e^-)=-f(e)/\sqrt2.
\]
则式 (1) 的规范弧核满足 \(K_G=TQ_GT^*\)。对同一边的两弧，\(2\times2\) 主块为
\[
 \frac{Q_G(e,e)}2
 \begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\]
行列式为零，所以弧 DPP 几乎必然不会同时选择两个方向。

令 \(\pi(y)_e=y_{e^+}\lor y_{e^-}\)。若 \(B\) 含 \(k\) 条无向边，每种方向选择 \(\sigma\in\{+,-\}^k\) 的弧主矩阵为 \(\frac12D_\sigma(Q_G)_BD_\sigma\)，其行列式为 \(2^{-k}\det(Q_G)_B\)。把 \(2^k\) 个互斥方向选择相加，得到
\[
 \mathbb P(B\subseteq\pi(Y))=\det(Q_G)_B.
\]
由 BLPS Theorem 7.8 和 DPP 柱事件唯一性，\(\pi(Y)\sim\operatorname{FUSF}_G\)。OR 映射在所有输入上定义且与同构交换。

### 5.2 联合 Borel 图因子

从顶点 iid \(U\) 用 (2) 得到弧 iid \(Y\)。用第 3 节的联合 Borel 核 \(K_G\)，再把第 4 节的联合 Borel sampler 应用于 \((G,K_G,Y)\)，最后用 \(\pi\) 忘掉方向。定义
\[
 \Phi(G,U):=\pi\bigl(\mathfrak S_{K_G}(Y(G,U))\bigr).
 \tag{11}
\]

式 (11) 是同一个统一规则，而不是“对每个固定图任选一个 factor”。其每一步都联合 Borel。若 \(\theta:G\to H\) 是保持顶点标签的同构，则：

1. 邻居 key 排名给 \(Y(H,\theta U)=\theta Y(G,U)\)；
2. 第 3 节给 \(K_H=\theta K_G\theta^{-1}\)；
3. DPP sampler 的自然性 (5) 给相应弧输出相同；
4. OR 映射与 \(\theta\) 交换。

这里还有一个容易被商空间记号遮住的可测性细节。验证 joint Borel 时，取 Aldous--Lyons §2、printed p. 1461 构造的连续 canonical representative（Angel--Ray--Spinka 正式版 p. 7 脚注 2 也明确引用这一代表选择）；于是每个代表的顶点集、弧集是真正的可数 Borel 纤维，可在第 4.1 节所述 Lusin--Novikov 部分枚举中检查所有有限运算。不能把 \(\mathcal G_{**}\) 中的双根同构类直接当作某个图的顶点纤维：根固定自同构会把同一轨道中的不同顶点压成一个双根同构类。编号在这里仅用于证明可测性。若换一个编号代表，两者间的图同构是弧集之间的双射，(3)、(5) 及 OR 的自然性说明输出代表同一个有根标记图同构类。因此最终规则不依赖编号选择。

所以
\[
 \Phi(H,\theta U)=\theta\Phi(G,U)
\]
对每个输入成立，不需要对不可数多个自同构取概率一交。因为 (11) 不使用根，rerooting 保持输出。条件于每个 \(G\)，第 2.1 节给弧 iid，第 4 节给弧 DPP \(\mathbf P^{K_G}\)，第 5.1 节给 FUSF。这证明主结论。

---

## 6. 与两篇指定原文的量词对照

### 6.1 Timár, arXiv:2306.15120v2

Timár 在第 2 节把 \(\mathcal G_*\)、\(\mathcal G_{**}\) 与 (MTP) 写明；在 quasi-transitive 固定图情形，把 factor of iid 定义成从顶点 \([0,1]^V\) 到子图的 measurable、automorphism-equivariant coding。对一般 URG，他给出“根及其 incident edges 可由越来越大有根标记球以任意小错误判定”的操作性版本。

我们的 \(\Phi\) 是标准 Borel graph factor，因而也满足这个操作性版本：局部标记球生成完整 Borel \(\sigma\)-代数；对根星上的有限二进制输出，关于半径 \(R\) 信息的条件期望鞅收敛，阈值化后错误概率趋零。根度虽不一致有界，但局部有限保证根星逐样本有限，再以截断处理即可。

反向需要比“底图法则 unimodular”更精确的耦合前提。**PROVED（条件式）.** 若 Timár 的操作性表述由同一个**联合 unimodular marked coupling** \((G,o,U,M)\) 实现，其中 \(U\) 是 iid 标签、\(M\) 是目标 decoration，且对每个 \(\varepsilon>0\) 有一个只看有限有根 \(U\)-标记球、对有根同构不变的共同局部规则，预测根及 incident edges 的错误概率小于 \(\varepsilon\)，则它推出 ARS graph factor。确实，取错误概率可求和的子序列 \(\varepsilon_k\)。Borel--Cantelli 说明根处预测最终等于目标。将第 \(k\) 个规则从每个顶点重新取根后应用，得到同一个全图规则；令 \(S\) 为“预测没有最终正确”的顶点集。它是上述**联合 marked law** 中的等变随机顶点集，且 \(\mathbb P(o\in S)=0\)。对每个 \(r\)，向距离不超过 \(r\) 的 \(S\)-点送单位质量，联合 marked law 的 MTP 给
\[
 \mathbb E\#(S\cap B_r(o))
 =\mathbb E[\mathbf1_{\{o\in S\}}|B_r(o)|]=0,
\]
故由 \(r\in\mathbb N\) 可数，\(S=\varnothing\) a.s.。于是每个顶点预测都最终正确；一条边的两个端点极限一致。取这些局部规则的逐点 \(\liminf\)，在异常输入上用两个端点极限的对称 AND 约定，即得 total Borel、换根相容的 graph factor。

这里不能只由“底图 marginal 是 URG、目标 decorated marginal 是 unimodular、iid marginal 正确”推断上述联合耦合 unimodular；两个 unimodular marginals 的任意 coupling 未必联合 unimodular。事实上，把 hands-on 句子弱读成“允许任意耦合，只要求根处可预测”时，反向为 **DISPROVED**。取固定 Cayley 图 \((\mathbb Z,0)\)，令 \(U\) 为顶点 iid，并在这个非平稳联合耦合中定义二元 vertex decoration
\[
 M_v=\mathbf1_{\{U_0<1/2\}}\oplus\bigl(|v|\bmod2\bigr).
\]
目标 \(M\) 的 marginal 是两个 proper 2-colorings 的公平混合，因而作为 marked rooted graph law 是 unimodular；且 \(M_0=\mathbf1_{\{U_0<1/2\}}\)，根标记由半径零完美预测。但它不是 graph factor of iid：若存在通常的 shift-equivariant Bernoulli factor 并令 \(f(U)\) 为原点颜色，则 proper coloring 迫使 \(f(TU)=1-f(U)\)，从而 \(f(T^2U)=f(U)\)。Bernoulli shift \(T^2\) 是 ergodic：两个有限坐标柱事件在充分远的偶数平移后独立，再用柱事件逼近即得 mixing，故每个 \(T^2\)-不变事件概率为 \(0\) 或 \(1\)。于是 \(f\) 必须 a.s. 为常数，与前式矛盾。这里输出可直接看作 vertex percolation，不涉及 incident-edge 状态。这个例子只否定上述刻意的弱读法；不把它归为 Timár 原文的作者意图。

前向“Borel graph factor \(\Rightarrow\) 根处局部可逼近”为 **PROVED**，且不需要 unimodularity；这也是本文主定理与 Timár 开放问题对照真正用到的方向。至于 Timár 的简短 prose 是否把“共同联合 unimodular coupling”隐含在 hands-on 说法中，原文没有另列形式定义，故纯文本语义判断保持 **INCOMPLETE**，不影响以上两个精确数学命题。

v2 的精确定理编号与范围是：

* Theorem 1：a.s. recurrent 的 unimodular random graph 的 USF 是 factor of iid；
* Theorem 2(1)：invariantly amenable URG 的 USF 是 finite-valued finitary factor of iid（第 (2) 款是 \(\mathbb Z^d\) 唯一 Gibbs 区间的 Ising 模型，与本题对象不同）；
* Theorem 4：invariantly amenable URG 上每个 compatible monotone weak limit 是 factor of iid；FUSF 在其定义后的例子中是 compatible monotone decreasing limit；
* Corollary 5：invariantly amenable URG 的 USF 是 factor of iid，特别包括 a.s. recurrent URG；在这个范围 free=wired；
* 引言随后明确说 full generality 的 FUSF factor-of-iid 问题开放。

本文的量词是“每个 Borel 随机局部有限连通简单有根图”，不要求 invariant amenability、unimodularity 或 recurrence，因此若主证明获外部认证，它与 Timár 的开放全量词一致且更强；它不是只对每个固定群作用分别存在 factor 的陈述。

### 6.2 Angel--Ray--Spinka, EJP 29 (2024), paper 39

其第 2.1 节的正式 graph factor 定义正是“marked rooted graph 空间上的 measurable map，保持底图且对 rerooting 不变”，并等价写成顶点函数 \(F\) 与交换两根对称的边函数 \(F'\)。式 (11) 逐项满足这一正式定义。

其 Theorem 1.4（正文重述为 Theorem 4.1）证明：任意 a.s. transient 的随机有根图，其 WUSF 是 graph factor of iid；不要求 unimodularity。Question 6.1 问 recurrent unimodular random rooted graph 的 wired UST 是否为 graph factor，后来由 Timár 的 amenable/recurrent 结果回答。该文没有证明一般 FUSF graph factor。

其“顶点、边或二者上的 iid 标记等价”需按第 2 节加边界限定：非平凡简单图上 vertex 与 directed-arc 源等价；vertex 与 unoriented-edge 源在简单连通至少三点时也可互换；\(K_1\)、\(K_2\) 及无 edge ports 的平行边给出字面反例。这个标签模型边界不影响本文简单图上的正构造，因为我们显式从顶点 iid 生成弧 iid。

---

## 7. 全部假设用途表

| 假设 | 用途 | 可否删除 |
|---|---|---|
| 连通 | 有根球穷尽全图；FUSF按一个连通分量表述 | 可逐连通分量推广，但随机根看不到其它分量时需另定全局对象 |
| 局部有限 | 有限有根球、有限邻居排名、顶点到弧 iid | DPP sampler 只需可数索引，但 vertex-to-arc 构造和标准 graph space 需此条件 |
| 统一度上界 | 未使用；只须每个顶点邻居有限；sampler 的阈值图 \(D_n\) 另由正压缩恒等式自动有度界 \(n^2\) | 可完全删除 |
| 简单 | 不同邻居区分同尾弧；排除平行边置换反例 | 不能在纯顶点源下无条件删除；加 edge/half-edge iid 可修复 |
| 无向 | 采用 FUSF 与反向弧 involution | 是对象定义的一部分 |
| 可数 | 产品路径场、同时 Borel--Cantelli、DPP 索引 | 由连通+局部有限自动推出 |
| 随机有根图的 Borel 法则 | 定义条件 iid 与联合图因子 | 必需的测度论框架 |
| unimodular | 未使用 | 可完全删除；只保证输出仍 unimodular |
| amenable / invariantly amenable | 未使用 | 可完全删除 |
| recurrent / transient | 未使用 | 可完全删除 |
| FUSF=WUSF | 未使用；核取有限环闭包正交补，而非 star projection | 不要求，两者可以不同 |
| 有限期望根度 | 未使用 | 可完全删除 |
| transitive / quasi-transitive / 群作用 | 未使用 | 可完全删除 |
| finitary 或有限值 coding | 未声称 | 本构造没有给出这些加强 |

---

## 8. 最终裁决账

| 承重主张 | 状态 |
|---|---|
| FUSF 是有限环空间正交补投影 DPP | **PROVED**（BLPS Theorem 7.8） |
| 规范双弧核忘掉方向恰给 FUSF | **PROVED** |
| \((G,a,b)\mapsto K_G(a,b)\) joint Borel | **PROVED** |
| \(G\mapsto\operatorname{FUSF}_G\) 是 Borel probability kernel | **PROVED** |
| prescribed-index DPP sampler 对核参数 joint Borel 且对任意双射自然 | **PROVED** |
| 简单局部有限图上顶点 iid 生成弧 iid | **PROVED** |
| 统一规则 (11) 是 ARS 意义的 graph factor | **PROVED** |
| ARS graph factor 推出 Timár 根处小误差操作表述 | **PROVED**（无需 unimodularity） |
| Timár 根处操作表述反推 ARS graph factor | **PROVED（若共同耦合的联合 marked law unimodular）；DISPROVED（允许任意非联合-unimodular耦合的弱读法）** |
| 任意随机局部有限连通简单有根图的 FUSF 是 graph factor iid | **PROVED** |
| 主定理是否需要 unimodularity/amenability/recurrence | **PROVED：无须这些假设** |
| 无标记多重图、纯顶点源下的同一全称 | **DISPROVED**（两点两平行边） |
| 顶点/无向边/弧 iid 在所有有限图上无保留等价 | **DISPROVED**（\(K_1,K_2\)；平行边） |
| 本结果为首次、已获领域外审或形式化认证 | **INCOMPLETE / NOT CERTIFIED** |
