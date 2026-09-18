# S68 Cycle13 visible reply receipt

Source: S68; thread 6aad854b-5104-83ee-8084-3aba2ad3b269.
Status: AUTHOR_ONLY, independent review not yet complete. Complete visible reply recovered; downloadable attachments NOT received. Attachment placeholders are not files. Received 2026-09-19 Singapore.

---

**:chatgpt-content-reference{index="3"}**  
:chatgpt-content-reference{index="4"}

包内包含主报告、两份完整证明附录、源码、实际概率缓存、来源快照、检查结果及 SHA-256 清单，共 44 个文件。**362 项有限数值检查全部通过；另外，三个明确模型中的局部反例通过了纯整数区间认证。**

本轮没有证明完整的 \(C(0,1)\)。得到的主要结果是：**补齐二缺陷展开中不可缺少的对角项；证明投影端点二阶常数项的严格负号和 \(n^2\log n\) 增长；给出真实权重下的极点、补偿后有限部分及二阶量传递界。**

## 一、二阶展开必须保留一个同点项

令 \(P=P_0\) 为 full-support 基准律，\(P_A^p\) 为对集合 \(A\) 独立重采样后的真实输出律。定义自然的异点 interaction：
\[
\mathcal J_{ij}(p)
=
D(P_{ij}^p\Vert P)-D(P_i^p\Vert P)-D(P_j^p\Vert P)
-\sum_y
\frac{(P_i^p(y)-P(y))(P_j^p(y)-P(y))}{P(y)}.
\]

那么正确展开是
\[
\boxed{
I(E;Y)
=
\varepsilon\sum_iD(P_i^p\Vert P)
+\varepsilon^2
\left[
\sum_{i<j}\mathcal J_{ij}(p)
-\frac12\sum_i\chi^2(P_i^p\Vert P)
\right]
+\mathcal R_{n,3}.
}
\]

**最后这个对角 \(\chi^2\) 项不能删除。** \(n=1\) 时已经能检出：若基准是 \(\operatorname{Bern}(q)\)，二阶系数为
\[
-\frac{(p-q)^2}{2q(1-q)},
\]
但根本不存在异点 pair。对于 \(n\ge2\)，可以把它按 \(n-1\) 人为分摊到各 pair，不过那会把同点预算混入所有距离，不适合研究距离结构。

固定外部真实输出 \(z\)，记归一化条件表为 \(q_{ab}(z)\)，实际外部质量为 \(m_z\)，并令
\[
\delta_z=q_{10}q_{01}-q_{00}q_{11}.
\]
本轮得到
\[
\boxed{
\mathcal J_{ij}''(p)
=
2\sum_zm_z
\left[
\log\frac{q_{10}q_{01}}{q_{00}q_{11}}
-\delta_z\sum_{a,b}\frac1{q_{ab}}
\right].
}
\]

这里保留了全部实际权重与归一化。它还有一个很强的代数后果：**每个自然 \(\mathcal J_{ij}(p)\) 都是二次多项式，其曲率完全不依赖 \(p\)。**

这个表达式与 S52 的 actual-output Fisher–Bregman skew **精确相同，而非仅仅类似**：局部 skew 乘以 \(2m_z\)，再对真实外部输出求和，就是上式。fileciteturn2file0L350-L384

因此，一阶曲率相消以后，完整二阶预算是
\[
\boxed{
\mathcal L_n
=
\sum_{i<j}\mathcal J_{ij}''
-
\sum_i\mathbb E\frac1{\pi_i(1-\pi_i)},
\qquad
H_{pp}
=
\varepsilon^2\mathcal L_n+\mathcal R_{n,3}''.
}
\]

这也确定了一个研究边界：**稀疏表示并没有在二阶自动绕开 S52 的平均符号难点；不能把负的同点预算从账本中拿掉。**

## 二、投影端点：得到了二阶常数项的符号与增长定理

对全支撑于 \(k\)-粒子层的投影输入，原来的 regular KL 展开不成立，因为单缺陷相对无缺陷的 KL 已经是无穷。

正确做法是按输出偏离 \(k\)-粒子层的距离分层。固定 \(n\)，在 \(p\) 远离 \(0,1\) 的区间内，本轮推得
\[
\boxed{
\begin{aligned}
H_{pp}(\varepsilon,p)
={}&-\varepsilon
\left(\frac{n-k}{p}+\frac{k}{1-p}\right)\\
&+4k(n-k)\varepsilon^2\log(1/\varepsilon)
+\varepsilon^2B_{2,n}''(p)
+O_{n,\mu,p}\!\left(\varepsilon^3(1+|\log\varepsilon|)\right).
\end{aligned}
}
\]

所以，**投影支持奇异情形下，一阶 \(p\)-曲率并不为零**。这与有限 true Toeplitz 的 full-support 相消没有矛盾。

更重要的是，本轮不仅算出了 \(B_{2,n}''\)，还证明了以下结果。

### 常对角半密度投影的严格符号

定义真实输入律上的交换能量
\[
\mathscr D_\mu
=
\sum_x\mu(x)
\sum_{i\in x,\ j\notin x}
\log\frac{\mu(x)}{\mu(x-i+j)}
\ge0.
\]

对任何满粒子层支撑、常对角 \(1/2\) 的秩 \(n/2\) 投影，
\[
\boxed{
B_{2,n}''(1/2)\le -n-2\mathscr D_\mu\le -n<0.
}
\]

这个证明不是逐 pair 判号。它来自**真实插入后验的投影 minor 结构**：插入 \(r\) 个粒子后，给定输出的父配置后验概率不超过 \(2^{-r}\)，因而反向条件熵至少为 \(r\log2\)。

### 循环 Fourier 投影的增长量级

半密度循环模型还满足
\[
\mathscr D_\mu
=
\frac{n^2}{2}\log n-2(n-1)H(\mu).
\]

结合真实一、二插入后的反向条件熵，可以证明
\[
\boxed{
B_{2,n}''(1/2)=-\Theta(n^2\log n),
}
\]
更具体地，
\[
\boxed{
-2+o(1)
\le
\frac{B_{2,n}''(1/2)}{n^2\log n}
\le
-1+o(1).
}
\]

这里没有断言比值极限存在。附录还给出显式常数版本：所有偶数 \(n\ge256\) 都有
\[
-2n^2\log n
\le B_{2,n}''(1/2)
\le-\frac12n^2\log n.
\]

**这说明不能孤立地用正的 \(\varepsilon^2\log(1/\varepsilon)\) 项判断曲率翻号：同一阶的“常数项”本身已经包含负的 \(n^2\log n\) 非一致性。**

## 三、正则化循环 pair 和确实有极点，而且补偿后的有限部分也已算出

令
\[
\mu_\eta
=
\operatorname{DPP}\!\left((1-\eta)\Pi_n+\frac{\eta}{2}I\right),
\]
其中 \(\Pi_n\) 是半密度循环投影。以这个 full-support 输出为基准，定义自然异点和
\[
S_n(\mu_\eta)=\sum_{i<j}\mathcal J_{ij}''.
\]

本轮证明，固定 \(n\) 时，
\[
\boxed{
S_n(\mu_\eta)
=
-\frac{A_n}{\eta}
+n^2\log(1/\eta)
+F_n
+O_n\!\left(\eta(1+|\log\eta|)\right),
}
\]
并且
\[
\boxed{
A_n\ge n,
\qquad
F_n=-\Theta(n^2\log n).
}
\]

\(A_n\) 由真实一错误输出的后验碰撞概率给出；\(F_n\) 则有完全显式的真实一、二错误输出质量公式。附录没有把它们定义成“未知余项”。

这严格排除了
\[
S_n(\mu_\eta)/n=O(\log(1/\eta))
\]
这样的有限循环一致界。

**但不能因此宣布无限 true-sine 的 \(\Gamma_c=O(\log(1/(1-c)))\) 猜想已被证伪。** 上面的展开先固定体积，再取零噪声；原目标需要先处理真实无限体积。两者之间尚缺的二阶传递不能省略。这里需要比“发现了 \(n/\varepsilon\) 主项，所以直接否定 \(\Gamma\) 猜想”更严格地区分对象和量词。

## 四、逐表支付在实际模型中失败，已有精确证书

不只是一般合法二元 DPP 表会出问题。

在 **\(n=8\)、rank \(=4\)、\(c=19/20\) 的真实循环模型**中，取零起始编号的 pair \((1,6)\)，给定外部
\[
(0,2,3,4,5,7)=(1,1,1,0,0,0),
\]
纯整数区间计算认证
\[
\boxed{
0.56496630
<
\log\frac{q_{10}q_{01}}{q_{00}q_{11}}
-\delta\sum_{a,b}\frac1{q_{ab}}
<
0.56496632.
}
\]

然而，同一个 pair 按**全部真实外部概率**求和后，其曲率严格为负，数值约为
\[
\mathcal J_{1,6}''\approx-1.53323606.
\]

true sine 的六点 Toeplitz 模型也有对应的严格可达局部反例，包括 \(c=1\) 和 \(c=19/20\)。

因此，这次把禁止路线收紧到了实际模型内部：**不能要求每个可达条件方块的 skew 非正；局部正贡献与实际平均负号可以同时存在。** 这些有限证书仍不替代无限平均符号证明。

## 五、二阶量传递与 remainder 已给出明确常数，但没有跨过最终极限缺口

对具有共同谱隙的 Hermitian 核
\[
\delta I\le K,\widetilde K\le(1-\delta)I,
\]
本轮证明
\[
\boxed{
\frac{|\mathcal L_n(K)-\mathcal L_n(\widetilde K)|}{n}
\le
2n\delta^{-5}\|K-\widetilde K\|_F.
}
\]

它控制的是**完整二阶 entropy/interaction quantity**，不是仅控制核或熵值；实际概率权重的变化也包含在证明中。

另一方面，令基准单点条件概率地板为 \(\beta>0\)，并设
\[
T=n\varepsilon(1+\beta^{-1})\le\frac14.
\]
则完整展开满足
\[
\boxed{
|\mathcal R_{n,3}''|
\le(2H(P)+10)T^3.
}
\]

这两条界进一步给出了真实 sine 的对数增长窗口结论。施加噪声后，还能在 \(m=O(1/\varepsilon)\) 的窗口上得到多项式周期化传递：精确匹配密度时，误差由
\[
O(\varepsilon^{-8}N^{-2})
\]
控制，故 \(N\varepsilon^4\to\infty\) 足以使这项误差趋零。

**但这是相同 \(m\) 点边缘窗口之间的比较，不是“观察全部外部输出”后的条件量传递；也不是自然尺度上的完整稀疏 remainder 一致性定理。**

因此，本轮没有把 S51 已有的
\[
O\!\left(\frac{\log(1/(1-c))}{1-c}\right)
\]
端点包络改进成纯 logarithmic 界。该既有包络及其适用范围在来源中是明确的。fileciteturn2file1L1358-L1375

最终尚未闭合的部分，现在可以更准确地表述为：**真实无限 sine 输出下的平均符号，以及足以匹配刚性尺度的完整 remainder 控制。** 本包已经把它们之前的二阶账本、支持奇异系数、补偿后有限部分及有限量传递分别写成可复核的证明，没有把这些剩余义务藏进极限交换。

仓库未取得完整 checkout；实际读取的 S51/S52 原文、来源哈希和访问限制均已写入包内 `SOURCE_AUDIT.md`。

