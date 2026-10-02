# 题 2 第二独立数学核验

核验对象为最终版 `RESULT.md` 与 `mcheck.py`。本文件不采用作者自评、PR review 状态或脚本的 `PASS` 字样作为数学证据；脚本只用于复算有限维实例。总体裁决：**承重结论通过独立核验，未发现阻断性数学缺口。**

## 1. 任意可数群上的 FK 双侧支配

**VERIFIED / PROVED.** 第 2 节的插值证明闭合。

1. 对有限严格正压缩 \(0<C<I\)，\(L=C(I-C)^{-1}\) 的 Schur 补给出完整外部配置 \(A\) 下的条件 odds。其变分式随 \(A\) 增大而下降，在 \(A=V\setminus\{i\}\) 时给
   \[
   q_i(A)\ge (C^{-1})_{ii}^{-1}.
   \]
   inclusion indicators \(1_{\{B\subseteq X\}}\) 确为 \(2^V\) 上函数空间的基；对方向 \(I-rC\) 求导后得到式 (2.6)。当 \(r\ge\max_i(C^{-1})_{ii}\) 时，每个递增函数的导数非正。
2. 对单轨道群核，路径
   \[
   K_t=\frac{D(Q)}{D(Q+tI)}(Q+tI)
   \]
   保持 \(D(K_t)=D(Q)\)，满足 \(0<K_t<I\)，并在范数中趋于 \(D(Q)I\)。直接微分给
   \(K_t'=a_t(I-r_tK_t)\) 与 \(r_t=\tau(K_t^{-1})\)。逆压缩不等式
   \((P_VK_tP_V)^{-1}\le P_VK_t^{-1}P_V\) 和单轨道对角元恒定性恰好验证有限维引理的假设；因此所有有限支撑递增柱函数的期望沿路径下降。
3. \(Q_\eta=(Q+\eta I)/(1+2\eta)\) 的极限正确覆盖 \(D(Q)=0\)、非满秩和谱端点；有限柱概率是主子式的有限多项式，足以传递随机序。无限维“非满秩”被正确解释为 \(\ker Q\ne0\)：这蕴含 \(D(Q)=0\)，反向不成立；在非 amenable 情形 \(D(Q)=0\) 也不蕴含 \(p_-(Q)=0\)。补集 DPP 的核为 \(I-Q\)，所以同一个下支配证明给出上支配。

所以“不需要 sofic”的加强有证明支撑，而不是从原猜想的群范围外推。

## 2. 有限群、amenable 群与子群诱导

**VERIFIED / PROVED.** 有限群中全占据事件给 \(p^{|\Gamma|}\le\det Q\)，与第 2 节合并即得逐点等号。Amenable 情形所需的 Li--Thom Theorem 1.4 确实对正的 \(g\in M_d(\mathcal N\Gamma)\) 给出有限压缩行列式的 infimum/Følner 极限，并允许奇异正元素；因此式 (4.1)--(4.3) 的端点量词正确。

对子群 \(H\le\Gamma\)，把卷积系数零延拓后，算子按陪集分块，DPP 是陪集上独立积。限制耦合给一个方向，在各陪集独立复制耦合给反方向，故 \(D\) 与 \(p_\pm\) 都保持。该段只给一类可处理核，没有误写成非 amenable 群的全分类。

## 3. Bass--Serre 树投影反例

**VERIFIED / DISPROVES POINTWISE OPTIMALITY.** 第 5.1 节的反例成立。

* \(C_d*C_d\) 的 Bass--Serre 树为 \(d\)-正则树；边作用自由传递，且从第一类顶点指向第二类的方向被左作用保持。因此边空间是一份无符号扭曲的正则表示。
* \(\|\mathcal A\|\le2\sqrt{d-1}<d\) 使 \(\Delta=dI-\mathcal A\) 可逆。给出的
  \(G(u,v)=cr^{\operatorname{dist}(u,v)}\)，其中
  \(r=(d-1)^{-1}\)、\(c=(d-1)/(d(d-2))\)，满足极点内外的差分方程，且列属于 \(\ell^2\)。于是
  \(\Pi=\nabla\Delta^{-1}\nabla^*\) 是梯度空间投影，\(\Pi(e,e)=2/d\)。有限支撑无散流在树上必为零，所以每个有限压缩 \(\Pi[S]\) 正定，条件化公式合法。
* 在 BFS 次序中，当前边前向子树的几何衰减势函数之梯度 \(h\) 位于
  \(H_S\)，在当前边绝对值为 \(1\)，且
  \(\|h\|^2=1+(d-2)=d-1\)。故每个正概率前序历史的条件占据概率至少
  \(1/(d-1)\)。逐坐标共同 Uniform 的顺序构造由此给普通随机序支配；不需要把耦合声称为不变耦合。
* 对含 \(m\) 条边的有限连通子树，关联矩阵最大子式恒等式与树 AR(1) 行列式给
  \[
  \det\Pi[F]=(d-1)^{-m}\left(1+\frac{d-2}{d}m\right).
  \]
  令 \(m\to\infty\) 的全占据事件迫使反向界，故
  \(p_-(\Pi)=1/(d-1)\)。顶点全星压缩有特征值 \(1\)，其全空概率为零，故
  \(p_+(\Pi)=1\)。投影迹为 \(2/d<1\)，所以 \(D(\Pi)=0\)。在 \(d=3\) 得到原 sofic 范围内的严格反例；补核给严格上界反例。

谱隙扰动 \(\widehat Q=(I+63\Pi)/128\) 的 union-plus-thinning 计算也正确：被支配的 Bernoulli 参数为 \(65/256\)，而迹谱计算给 \(D(\widehat Q)=1/8\)。因此失败不只发生在零谱端点。

## 4. 显式有限支撑群代数反例

**VERIFIED / PROVED.** 新增第 5.3 节正确闭合了“原投影不是有限传播”的边界。

令 \(q=\|\mathcal A\|/3\le2\sqrt2/3<19/20\)。截断 Neumann 多项式
\[
 p_N(\Delta)=\frac13\sum_{k=0}^N(\mathcal A/3)^k
\]
是有限传播实自伴算子；与有限传播的 \(\nabla,\nabla^*\) 合成后，在自由传递边轨道上对应有限支撑群环元。对 \(N=255\)，几何级数余项、\(\|\nabla\|^2=\|\Delta\|<6\) 和系数 \(63/128\) 给
\[
 \varepsilon_N=\|Q_N-\widehat Q\|
 <20(19/20)^{256}<1/1024.
\]
于是 \(Q_N\) 是满秩严格正压缩，且
\[
 Q_N\ge L_N=(1/128-\varepsilon_N)I+(63/128)\Pi.
\]
令 \(s=1/2-\varepsilon_N\)、\(q_0=(1/128-\varepsilon_N)/s\)。先与
\(\operatorname{Ber}(q_0)\) 作并、再以 \(s\) 稀疏化，所得核恰为 \(L_N\)；对
\(\operatorname{Ber}(1/2)\preceq\mu_\Pi\) 作同样操作给
\[
 p_-(L_N)\ge65/256-\varepsilon_N>259/1024.
\]
有限压缩上的 DPP 算子序支配再传到全部递增柱事件，故
\(p_-(Q_N)\ge p_-(L_N)\)。另一方面共同下谱界为 \(7/1024\)，log 的 resolvent 积分给
\(\|\log Q_N-\log\widehat Q\|<1/7\)，从而
\[
 D(Q_N)<e^{1/7}/8<7/48<259/1024<p_-(Q_N).
\]
所以这里确有一个明确的 \(\mathbb C(C_3*C_3)\) 满秩有限支撑反例。

## 5. 非归一化 finite-type 矩阵推广

**VERIFIED / PROVED.** 设 \(m=|S|\)、\(\tau_S(I)=m\)、
\(\Delta_S(Q)=\exp\tau_S(\log Q)\)。第 7.1 节的修正路径
\[
 a_t=\frac{(1+t)^{m-1}\Delta_S(Q)}{\Delta_S(Q+tI)},
 \qquad K_t=a_t(Q+tI)
\]
满足 \(K_0=Q\)、\(K_t\to\Delta_S(Q)I\) 及 \(0<K_t<I\)。微分所得
\[
 r_t=\frac{\sum_s h_s(t)-(m-1)/(1+t)}{a_t}
\]
不是归一化对角平均；由于每个 \(h_s(t)\ge(1+t)^{-1}\)，它逐轨道控制
\(\langle K_t^{-1}\delta_{(e,s)},\delta_{(e,s)}\rangle\)。逆压缩后有限维导数引理适用于混合多个标签轨道的任意有限窗口。因此同形非归一化双侧界有效，奇异核再由正则化得到。

两个对角例分别证明这一界在“只依赖单个 \(\Delta_S\) 数值”的类上一元意义下锋利，但不逐点最优。平凡群上的
\(Q=\operatorname{diag}(1/4,3/4)\) 有真实阈值 \((1/4,3/4)\)，而归一化迹候选给 \(\sqrt3/4\) 与 \(1-\sqrt3/4\)，同时违反下边和上边。Amenable 多轨道的必要界
\(p_-(Q)\le\Delta_S(Q)^{1/m}\) 则由 Li--Thom 的矩阵版压缩行列式和全占据事件正确推出；与充分界合并得到正文 (7.2b) 的夹逼，特别是 amenable 情形 \(\Delta_S(Q)=0\Rightarrow p_-(Q)=0\)。正文没有误称多轨道夹逼一般取等。

## 6. `mcheck.py` 复算

**VERIFIED.** 在带 SymPy 的独立 Python 环境重跑，输出为：

```text
Q: all 168 increasing events have nonpositive derivative; r=6071/1545
I-Q: all 168 increasing events have nonpositive derivative; r=6071/1545
Normalized two-type FK sandwich: disproved by the two one-site events.
PASS (finite exact verification only)
```

代码确实枚举四点 Boolean lattice 的全部 168 个递增事件，使用有理数和复 Hermitian 精确算术，分别检查 \(Q\) 与 \(I-Q\) 的初始导数，并以两个单点事件否定归一化 two-type 公式。它只核验有限维接口和符号，没有被用于替代无限群证明。

## 7. 剩余边界与来源说明

**INCOMPLETE（正文已正确保留）.** 一般非 amenable 群/核的逐点阈值分类、以及允许同时依赖 \((D(Q),D(I-Q))\) 的最佳统一改进，均未由这些论证解决。有限窗口量
\(\delta(Q)\) 满足 \(D(Q)\le\delta(Q)\) 和 \(p_-(Q)\le\delta(Q)\)，但全占据事件不足以刻画一般随机序；正文没有越界。

**来源链接已核对。** `REFERENCES.md` 已把失效的旧链接替换为本次实际打开的
<https://arxiv.org/pdf/1202.1213>。独立核对 arXiv v2 的 Theorem 1.4：它对可数 amenable 群和任意正的 \(g\in M_d(\mathcal N\Gamma)\) 给出正文所用的有限压缩行列式 infimum/Følner 极限，包含奇异正元素。

## 最终裁决

| 承重项 | 独立裁决 |
|---|---|
| 任意可数群 FK 双侧普通随机序支配 | **VERIFIED / PROVED** |
| 有限群与可数 amenable 群逐点等号 | **VERIFIED / PROVED** |
| \(C_3*C_3\) 树投影及补核反例 | **VERIFIED / DISPROVED pointwise optimality** |
| 满秩、有限支撑群代数反例 | **VERIFIED / DISPROVED pointwise optimality** |
| 非归一化 finite-type 同形界 | **VERIFIED / PROVED** |
| 归一化 finite-type 同形界 | **VERIFIED / DISPROVED** |
| `mcheck.py` 所述有限精确检查 | **VERIFIED / PASS** |
| 一般非 amenable 逐点分类与二元统一最优界 | **INCOMPLETE** |
