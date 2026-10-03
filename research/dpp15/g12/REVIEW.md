STATUS: PASS

# 独立对抗审查

## 结论

`source.md` 的显式流

\[
\Phi_E(P)(S,i)=2^{-(n-1)}P_{ii},\qquad i\notin S,
\]

确实对每个非空有限坐标集 (E)、每个 rank-one 投影 (P) 给出
\(\mathcal F_E(P)\) 中的一个点，并且组成 Borel、坐标置换协变的族。其精确
Lipschitz 估计为

\[
\|\Phi_E(P)-\Phi_E(Q)\|_1
=\sum_i|P_{ii}-Q_{ii}|
\le \|P-Q\|_1.
\]

所以冻结题面中的“不存在维数无关选择器”命题确实为假，作者 verdict
`DISPROVED` 正确；可取 (C_\varepsilon=1)。以下核验只针对固定
\(K=I/2\)，不推出一般 (K) 的正选择结论。

## 1. (I/2) 处的 DPP 导数

对任意 (S\subseteq E)，DPP 原子概率写成

\[
p_K(S)=(-1)^{|S^c|}\det(K-I_{S^c}).
\]

在 (K=I/2) 时，矩阵 (K-I_{S^c}) 可逆，在 (S) 上的对角元为
(+1/2)，在 (S^c) 上为 (-1/2)。因此

\[
p_{I/2}(S)=2^{-n},\qquad
(I/2-I_{S^c})^{-1}=2I_S-2I_{S^c}.
\]

Jacobi 公式于是给出沿 (P) 的精确导数

\[
\begin{aligned}
b_{I/2,P}(S)
&=p_{I/2}(S)\operatorname{tr}
  \bigl((I/2-I_{S^c})^{-1}P\bigr)\\
&=2^{-(n-1)}
  \left(\sum_{i\in S}P_{ii}-\sum_{i\notin S}P_{ii}\right).
\end{aligned}
\]

这里没有遗漏非对角项：逆矩阵是对角矩阵，所以迹只读取 (P) 的对角。
因此任意复相位以及坐标为零的退化情形都不影响该公式。

## 2. 非负性与散度

rank-one 投影可写为 (P=vv^*)，其中 \(\|v\|_2=1\)，所以

\[
P_{ii}=|v_i|^2\ge0,\qquad \sum_iP_{ii}=\operatorname{tr}P=1.
\]

故每条边上的 \(\Phi_E(P)\) 非负。采用题面约定的“入流减出流”散度，在
顶点 (S) 有

\[
\begin{aligned}
\operatorname{div}\Phi_E(P)(S)
&=\sum_{i\in S}\Phi_E(P)(S\setminus\{i\},i)
  -\sum_{i\notin S}\Phi_E(P)(S,i)\\
&=2^{-(n-1)}
  \left(\sum_{i\in S}P_{ii}-\sum_{i\notin S}P_{ii}\right)\\
&=b_{I/2,P}(S).
\end{aligned}
\]

这逐点满足完整 fiber 的散度等式，而非只满足某个聚合矩条件。

## 3. 总质量

固定 (i) 后，恰有 (2^{n-1}) 个 (S\subseteq E\setminus\{i\})。因此

\[
\sum_{S\subseteq E}\sum_{i\notin S}\Phi_E(P)(S,i)
=\sum_i2^{n-1}2^{-(n-1)}P_{ii}
=\operatorname{tr}P=1.
\]

故题面要求的总边质量归一化精确成立。

## 4. 点态容量常数

在任意 (S) 的总出流为

\[
\Phi_E(P)_{\rm out}(S)
=2^{-(n-1)}\sum_{i\notin S}P_{ii}
\le 2^{-(n-1)}.
\]

另一方面，题面容量上界在 (K=I/2) 处正是

\[
\frac2\varepsilon p_{I/2}(S)
=\frac2\varepsilon 2^{-n}
=\frac{2^{-(n-1)}}\varepsilon.
\]

因冻结范围 (0<\varepsilon<1/2) 特别蕴含 \(\varepsilon<1\)，有

\[
2^{-(n-1)}\le \frac{2^{-(n-1)}}\varepsilon.
\]

所以容量约束逐顶点成立。这里常数没有少一个 (2)：右端确为
\((2/\varepsilon)2^{-n}=2^{-(n-1)}/\varepsilon\)。事实上这一容量核验只需
\(\varepsilon\le1\)，故题面的更强范围足够。

结合前述非负性、散度、总质量和容量，可确认

\[
\Phi_E(P)\in\mathcal F_E(P).
\]

## 5. 维数无关的迹范数估计

每个对角差 (P_{ii}-Q_{ii}) 在全部 (i)-方向边上重复
(2^{n-1}) 次，因此

\[
\|\Phi_E(P)-\Phi_E(Q)\|_1
=\sum_i|P_{ii}-Q_{ii}|.
\]

令 (A=P-Q)。这是 Hermitian 矩阵。取对角矩阵
(D=\operatorname{diag}(\operatorname{sgn}A_{ii})\)，并在零对角处取 (0)，
则 \(\|D\|_{\rm op}\le1\)，且

\[
\operatorname{tr}(DA)=\sum_i|A_{ii}|.
\]

迹范数与算子范数对偶性给出

\[
\sum_i|A_{ii}|
=|\operatorname{tr}(DA)|
\le\|D\|_{\rm op}\|A\|_1
\le\|A\|_1.
\]

这也可视为对角条件期望（pinching）对 Schatten (1)-范数的压缩性。因而

\[
\|\Phi_E(P)-\Phi_E(Q)\|_1\le\|P-Q\|_1
\]

成立，常数既不依赖 (n=|E|)，也不依赖 \(\varepsilon\)。

## 6. Borel 性、置换协变与退化情形

在每个固定有限维空间中，\(\Phi_E\) 的所有坐标都是 (P) 的对角元的线性
函数，故连续并因而 Borel。若 \(U_\sigma\) 是坐标置换矩阵，则

\[
(U_\sigma P U_\sigma^*)_{ii}=P_{\sigma^{-1}i,\sigma^{-1}i},
\]

从而

\[
\Phi_E(U_\sigma P U_\sigma^*)(S,i)
=\Phi_E(P)(\sigma^{-1}S,\sigma^{-1}i).
\]

这正是题面要求的坐标置换协变。定义直接使用投影矩阵而不是单位向量代表，
所以整体相位没有选择问题；若某个 (P_{ii}=0)，相应方向所有边流量为零，
上述所有等式仍成立。空坐标集上不存在 rank-one 投影，故无额外边界义务。

## 7. 与上一轮 HDF 反例的逻辑关系

上一轮证书证明全 fiber 的有向 Hausdorff 距离可以由一个特意加入宏观循环的
坏流见证而失去维数无关控制，但没有迫使 selector 选取那个坏流。本稿给出的
canonical flow 正好显式展示 selector 可以避开坏流，并且随 (P) 以常数 (1)
变化。因此：

- HDF 的维数无关稳定性仍然为假；
- 冻结的 every-selector 非存在命题为假；
- 两个结论没有矛盾，因为一个控制整个 fiber，另一个只要求选出一条良好截面。

## 最终裁决

- 精确 DPP 导数：正确；
- 非负、散度与总质量：正确；
- 容量常数：正确，且未遗漏因子 (2)；
- trace-norm 对角压缩：正确；
- Borel 与坐标置换协变：正确；
- 冻结命题 verdict：`DISPROVED` 正确，可取 (C_\varepsilon=1)；
- 作用域：只认证 (K=I/2)，不扩展到一般核 (K)。


