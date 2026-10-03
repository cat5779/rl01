STATUS: PASS

# 独立逐式审查

## 结论与认证范围

`output.md` 的公式

\[
F_{K,P}(S,i)=P_{ii}\,p_{K_{E\setminus\{i\}}}(S),\qquad i\notin S,
\]

在题面规定的范围内完全成立：对任意有限非空坐标集 \(E\)、任意满足
\(\varepsilon\le k_i\le1-\varepsilon\) 的对角核
\(K=\operatorname{diag}(k_i)\) 和任意 rank-one 投影 \(P\)，它是
\(\mathcal F_E(K,P)\) 中的非负流，并给出 Borel、坐标置换协变的选择器。对
同一坐标集上的任意另一组 \((L,Q)\)，有精确的维数无关估计

\[
\|F_{K,P}-F_{L,Q}\|_1
\le \|P-Q\|_1+2\|K-L\|_1
\le 2\bigl(\|P-Q\|_1+\|K-L\|_1\bigr).
\]

所以作者 verdict `PROVED` 正确，可取通用常数 \(C_\varepsilon=2\)。本审查
只认证**对角核**；不推出一般非对角核上的 selector，也不把整个 fiber 的
Hausdorff 稳定性恢复为真。

## 1. 对角核处的精确 DPP 导数

对原子 \(S\subseteq E\)，令

\[
D_S=K-I_{S^c}.
\]

其对角元在 \(S\) 上为 \(k_i\)，在 \(S^c\) 上为 \(k_i-1\)。谱隙假设使
\(D_S\) 可逆。由

\[
p_K(S)=(-1)^{|S^c|}\det D_S
\]

及 Jacobi 公式，沿 Hermitian 方向 \(P\) 的导数为

\[
\begin{aligned}
b_{K,P}(S)
&=p_K(S)\operatorname{tr}(D_S^{-1}P)\\
&=p_K(S)\left(
  \sum_{i\in S}\frac{P_{ii}}{k_i}
  -\sum_{i\notin S}\frac{P_{ii}}{1-k_i}
  \right).
\end{aligned}
\]

这里没有遗漏 \(P\) 的非对角项：\(D_S^{-1}\) 是对角矩阵，故迹只读取
\(P_{ii}\)。若 \(P=vv^*\)，则 \(P_{ii}=|v_i|^2\)，所以向量代表的整体
相位和各坐标相位均不进入该导数。这也与固定 \(K=I/2\) 的上一轮公式一致。

## 2. 非负性、散度号与总质量

rank-one 投影满足

\[
P_{ii}=|v_i|^2\ge0,\qquad \sum_iP_{ii}=\operatorname{tr}P=1.
\]

因此所有边流量非负。对 \(i\notin S\)，乘积 DPP 给出

\[
p_{K_{E\setminus\{i\}}}(S)=\frac{p_K(S)}{1-k_i},
\]

而对 \(i\in S\)，有

\[
p_{K_{E\setminus\{i\}}}(S\setminus\{i\})
=\frac{p_K(S)}{k_i}.
\]

因此按全文采用的“入流减出流”号约定，

\[
\begin{aligned}
\operatorname{div}F_{K,P}(S)
&=\sum_{i\in S}P_{ii}
  p_{K_{-i}}(S\setminus\{i\})
  -\sum_{i\notin S}P_{ii}p_{K_{-i}}(S)\\
&=p_K(S)\left(
  \sum_{i\in S}\frac{P_{ii}}{k_i}
  -\sum_{i\notin S}\frac{P_{ii}}{1-k_i}
  \right)\\
&=b_{K,P}(S).
\end{aligned}
\]

散度的符号与导数完全相符。又因每个 \(p_{K_{-i}}\) 都是概率律，

\[
\sum_i\sum_{S\subseteq E\setminus\{i\}}F_{K,P}(S,i)
=\sum_iP_{ii}=1.
\]

故总边质量归一化精确成立。

## 3. 点态容量

逐顶点的总出流为

\[
F_{K,P,\mathrm{out}}(S)
=p_K(S)\sum_{i\notin S}\frac{P_{ii}}{1-k_i}.
\]

由于 \(1-k_i\ge\varepsilon\) 且
\(\sum_{i\notin S}P_{ii}\le1\)，

\[
F_{K,P,\mathrm{out}}(S)
\le \frac1\varepsilon p_K(S)
\le \frac2\varepsilon p_K(S).
\]

这比题面原容量多留出一个因子 \(2\)，没有遗漏常数。结合非负性、精确
散度与总质量，确有 \(F_{K,P}\in\mathcal F_E(K,P)\)。

## 4. weighted product-law 估计与同时变化的 \((K,P)\)

对任意有限坐标集 \(J\)，逐坐标替换 Bernoulli 因子并用三角不等式可得

\[
\left\|
\bigotimes_{j\in J}\operatorname{Bern}(k_j)
-\bigotimes_{j\in J}\operatorname{Bern}(\ell_j)
\right\|_1
\le2\sum_{j\in J}|k_j-\ell_j|.
\]

这里单坐标的 \(\ell^1\) 距离正是 \(2|k_j-\ell_j|\)，与其他概率因子
张量积不改变 \(\ell^1\) 范数。于是对每个 \(i\)，

\[
\|p_{K_{-i}}-p_{L_{-i}}\|_1
\le2\sum_{j\ne i}|k_j-\ell_j|.
\]

同时改变 \(P\) 和 \(K\) 时，按
\(|a\mu-b\nu|\le|a-b|\mu+b|\mu-\nu|\) 分解并对全部边求和，得到

\[
\|F_{K,P}-F_{L,Q}\|_1
\le \sum_i|P_{ii}-Q_{ii}|
 +\sum_iQ_{ii}\|p_{K_{-i}}-p_{L_{-i}}\|_1.
\]

第二项的关键加权求和为

\[
\begin{aligned}
\sum_iQ_{ii}\|p_{K_{-i}}-p_{L_{-i}}\|_1
&\le2\sum_iQ_{ii}\sum_{j\ne i}|k_j-\ell_j|\\
&=2\sum_j|k_j-\ell_j|\sum_{i\ne j}Q_{ii}\\
&=2\sum_j|k_j-\ell_j|(1-Q_{jj})\\
&\le2\sum_j|k_j-\ell_j|.
\end{aligned}
\]

这正是避免维数因子的步骤；没有把每个 \(i\) 的统一上界再无权相加。由于
\(K-L\) 对角，最后一和等于 \(\|K-L\|_1\)。

对第一项，令 \(A=P-Q\)，并取
\(D=\operatorname{diag}(\operatorname{sgn}A_{ii})\)（零项取零）。则
\(\|D\|_{\mathrm{op}}\le1\)，由迹范数对偶性

\[
\sum_i|P_{ii}-Q_{ii}|
=\operatorname{tr}(DA)
\le\|A\|_1=\|P-Q\|_1.
\]

故 simultaneous \((K,P)\) 比较确实给出

\[
\|F_{K,P}-F_{L,Q}\|_1
\le\|P-Q\|_1+2\|K-L\|_1,
\]

其常数与 \(|E|\)、投影支撑大小和相位无关。该证明实际上只用 \(P,Q\) 的
对角为非负且迹为一；rank-one 假设当然足够。

## 5. Borel、置换与退化

固定有限 \(E\) 后，每个边坐标都可写成

\[
P_{ii}\prod_{j\in S}k_j
\prod_{\substack{j\notin S\\j\ne i}}(1-k_j),
\]

所以它关于对角参数和投影矩阵连续，因而 Borel。坐标置换 \(\sigma\) 同时把
\(P_{ii}\) 送到 \(P_{\sigma^{-1}i,\sigma^{-1}i}\)，并把删去 \(i\) 后的
乘积律送到删去 \(\sigma^{-1}i\) 后的乘积律，故

\[
F_{K^\sigma,P^\sigma}(S,i)
=F_{K,P}(\sigma^{-1}S,\sigma^{-1}i).
\]

若 \(v_i=0\)，则 \(P_{ii}=0\)，整个 \(i\)-方向流自然为零；公式中没有除以
\(P_{ii}\) 或 \(v_i\)，所以零坐标退化连续通过。空坐标集上不存在 rank-one
投影，无额外情形。核的端点 \(k_i=0,1\) 不在冻结定理的谱隙域内，本审查不把
结论外推到该域。

## 6. 与既有结果的边界

当 \(K=I/2\) 时，本公式化为
\(2^{-(|E|-1)}P_{ii}\)，与上一轮已审查的常数 \(1\) selector 完全一致。
上一轮 HDF 反例由 fiber 中另一个带宏观循环的坏流见证；它不迫使当前显式
selector 选取坏流。因此“整个 fiber 的 Hausdorff 稳定性失败”和“存在一条
稳定截面”可同时成立。

## 最终裁决

- 精确 DPP 原子导数及“只取 \(P\) 对角”的解释：正确；
- 散度号、非负性、总质量：正确；
- 点态容量：正确，且得到更强的 \(1/\varepsilon\) 上界；
- weighted product-law 估计：正确，无维数损失；
- 同时 \((K,P)\) 变化及 trace-norm 对角压缩：正确；
- Borel、置换协变、零坐标退化：正确；
- 裁决：`PASS`，认证通用 \(C_\varepsilon=2\)，仅限 gapped diagonal kernels。

