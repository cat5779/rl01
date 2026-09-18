# Intake provenance

Visible assistant reply recovered from its original chat on 2026-09-19. This is AUTHOR_ONLY discussion, not an independent mathematical review. Truncated: false. S62 is actively being revised by its author at the user's request; do not treat the initial output as final. Numeric claims in S52 were not accompanied by original scripts/data and are unverified.

---

我把两边结论压成一份可直接交给 Pro 的研究指令，重点是把“已经确认的结构”与“下一步必须证明的东西”分开，不再继续扩散文献路线。

:::writing{variant="document" id="41863" title="Sine-DPP 高对比端点路线：综合结论与下一步任务"}
当前最值得推进的路线不是继续改写 \(\Gamma_c\)、继续做 scalar envelope，也不是直接购买 Wegner/分数矩等外部工具，而是围绕一个新的、目前看来确实没有在仓库中出现过的精确重参数化展开：把信道
\[
\Pr(Y_i=1\mid X_i)=a+cX_i
\]
写成稀疏重采样模型。令
\[
\varepsilon=1-c,\qquad p=\frac{a}{1-c},
\]
独立取缺陷集合 \(E\subset[n]\)，每个位以概率 \(\varepsilon\) 进入 \(E\)；若 \(i\notin E\)，则 \(Y_i=X_i\)，若 \(i\in E\)，则丢弃 \(X_i\) 并重新采样 \(Y_i\sim{\rm Bern}(p)\)。这是与原信道完全相同的概率律，不是近似。由此有精确恒等式
\[
H_n(p)=n\varepsilon\,b(p)+\mathbb E_E H(X_{E^c})+I_p(E;Y),
\]
其中第二项与 \(p\) 无关，因此
\[
H_n''(p)
=
-\frac{n\varepsilon}{p(1-p)}
+
I_p''(E;Y),
\]
也就是说目标熵凹性严格等价于
\[
I_p''(E;Y)\le \frac{n\varepsilon}{p(1-p)}.
\]
这是真正的新对象，因为它在做任何不等式之前就把过去各路线中的 \(1/(1-c)\) 大主项拆出来了；后续工作应围绕 \(I_p(E;Y)\) 的稀疏缺陷展开，而不是再对原 \(\Gamma_c\)、\(R_n\)、\(W_n+C_n\) 做第八种重写。

固定有限 \(n\) 时，一阶缺陷项已经可以严格算清。设 \(P_0\) 是无缺陷输出律，\(P_i^p\) 是只在第 \(i\) 位重采样后的输出律，则
\[
I_{\varepsilon,p}(E;Y)
=
\varepsilon\sum_iD(P_i^p\Vert P_0)+O_n(\varepsilon^2).
\]
若输入律在该有限块上 full support，记
\[
\pi_i(x_{-i})=\Pr(X_i=1\mid X_{-i}=x_{-i}),
\]
则
\[
b(p)+D({\rm Bern}(p)\Vert{\rm Bern}(\pi_i))
=
-p\log\pi_i-(1-p)\log(1-\pi_i),
\]
右边关于 \(p\) 完全仿射。因此
\[
\frac{d^2}{dp^2}D(P_i^p\Vert P_0)=\frac1{p(1-p)},
\]
从而 \(I_p''\) 的 \(O(\varepsilon)\) 主项与显式注入熵曲率
\[
-\frac{n\varepsilon}{p(1-p)}
\]
逐项精确抵消。数值也支持这一点：一般 \(\rho\) 下一阶系数虽强烈依赖 \(p\)，但其二阶差分为数值零；在 \(\rho=1/2\) 时粒子–空穴对称甚至使该一阶系数对 \(p\) 为常数。故高对比端点的曲率确实是至少二缺陷阶的效应。这里必须保留一个重要警告：上述展开是固定 \(n\)、\(\varepsilon\downarrow0\) 的 regular expansion；循环 projection DPP 在 \(c=1\) 时有固定粒子数、支持集退化，单缺陷相对无缺陷的 KL 可变成无穷，因此绝不能未经证明交换 \(n\to\infty\) 与 \(\varepsilon\to0\)。正确说法不是“\(c\to1\) 不是微扰区”，而是“它对固定 \(n\) 是微扰区，但很可能不是对 \(n\) 一致的微扰区”。

仓库事实也需要修正：S51 C1 已经明确从 \(c=1\) 端点反向展开，并已给出经审查的
\[
|\Gamma_x(0)|=O\!\left(\frac{\log(1/(1-x))}{1-x}\right)
\]
型端点包络，所以“此前从未从 \(c=1\) 往回做”是错误的；真律侧经认证等价的 \(\Gamma\) 表达式大约是四类而不是七类，\(W_n+C_n\) 属于 corrected law，与真律量相差有控制但不为零的 \(\Psi_n\)，dyadic chord 也是独立路线，不能全部算作同一量的等价写法。不过“现有路线陷在同一类平均化工具盆地”这个诊断仍成立，而且 Ward–Stein 在 \(c=19/20\) 的上界
\[
1600/39=1/b
\]
恰好就是平凡 \(J\ge0\) 上界，说明该区间对 \(\Gamma\) 的真实尺度几乎没有分辨率。

高对比的非一致性目前有一组非常重要的数值迹象，应当作为待证明的现象而不是已知定理。对越来越大的有限窗口，最优外部预测概率 \(\pi_R\) 的条件熵 \(\mathbb E\,b(\pi_R)\) 明显趋零，说明单点刚性确实在发生；但现有数据更像
\[
\mathbb E b(\pi_R)\approx 0.537\,R^{-0.281}
\]
而不是纯 \(1/\log R\)，所以不能把“最优预测器方差 \(\sim1/\log R\)”作为现成文献结论。另一方面
\[
\mathbb E[-\log\pi_R]
\]
近似按 \(\log R\) 发散，这说明一阶缺陷系数虽然在 \(p\)-曲率上精确消失，其数值大小却随窗口发散，故朴素 \(\varepsilon\)-展开不一致。若自然匹配尺度确实为 \(R\sim1/\varepsilon\)，那么这种 \(\log R\) 发散会留下
\[
O(\log(1/\varepsilon))
\]
级的高对比 remainder，这使“\(\Gamma_c\) 可能只有 logarithmic divergence”仍是一个值得检验的猜想，但目前绝非定理；它最多说明现有 \(O(\log(1/\varepsilon)/\varepsilon)\) 端点包络可能还能改善一个 \(\varepsilon\) 因子。

因此随机 Schrödinger/Wegner 路线目前不应作为主攻方向。它原本想控制的
\[
\mathbb E\frac1{\pi(1-\pi)}
\]
在有限窗口实验中快速发散，经验上约从 \(127\to440\to1795\)，尾指数还在下降，和 \(R^2\) 量级相容；也就是说朴素 inverse-moment 正是坏对象。若 \(R\sim1/\varepsilon\)，这会产生 \(\varepsilon^{-2}\) 级爆炸，正对应仓库中一直悬而未决的自然 \(\kappa_x^2\) 一致可积性障碍。这里未来若有工具，只能是“补偿后的 inverse moment / weak-* precompactness”，不能直接估裸的 \(1/[\pi(1-\pi)]\)。相反，real-stable / generating-polynomial 一侧有一个免费且正确的输入：对 \(z\in[0,1]^n\)，
\[
a\longmapsto \log\det(I-K_a(I-Z))
\]
是凹的，因为它就是正定仿射矩阵的 log-det；但从母函数凹性到 Shannon entropy 参数凹性的桥目前完全没有证明。淬火–退火方向在小 \(n\) 数值上暂未被否定，但它是比原目标更强的充分条件，且余量较薄，不宜优先投入。Costa/bosonic Gaussian 的类比也只能当证明风格启发，不能宣称已有“固定透射率下对环境噪声参数凹”的现成定理。

下一步应集中完成一个明确的“二缺陷展开定理”，而不是继续寻找更多宏观类比。目标是在固定有限 \(n\) 下把
\[
I_{\varepsilon,p}(E;Y)
\]
严格展开到二阶：
\[
I_{\varepsilon,p}(E;Y)
=
\varepsilon\sum_i D(P_i^p\Vert P_0)
+
\varepsilon^2\sum_{i<j}\mathcal J_{ij}(p)
+
\mathcal R_{n,3}(\varepsilon,p),
\]
其中必须给出 \(\mathcal J_{ij}(p)\) 的显式 actual-output 公式，保留真实概率权重、归一化和所有支持集问题，并计算
\[
\mathcal J_{ij}''(p).
\]
首要问题不是马上证明其逐 pair 符号，而是判断
\[
\frac1n\sum_{i\ne j}\mathcal J_{ij}''(p)
\]
在 sine/cyclic DPP 中是否存在可求和的距离结构、Ward 型抵消或其他真实权重下的平均符号；若逐 pair 符号失败，应立即转向平均和，不得再次建立点态充分条件。与此同时需要跟踪三阶 remainder 对 \(n\) 的依赖，以判断 \(\varepsilon\)-展开何时失去一致性。真正的端点答案将取决于二缺陷相互作用增长与刚性剖面之间的匹配，而不是单缺陷项，因为一阶 \(p\)-曲率已经精确为零。

建议 Pro 当前只做三件事。第一，完整推导并证明上述二缺陷系数 \(\mathcal J_{ij}\)，最好把它整理为 mutual-information interaction、KL inclusion–exclusion 或 Bregman/cross-ratio 的显式形式，并检查它是否与 S52 的 Fisher–Bregman compensator 存在直接代数联系。第二，在 cyclic projection 与 true finite Toeplitz full-support 两种模型中分别分析该系数，明确 projection endpoint 的支持奇异性如何通过 \(\varepsilon>0\) 正则化，绝不默认两个极限可交换。第三，给出一个真正可证明的 finite-volume 剖面或 transfer inequality：周期化 kernel 的局部/\(\ell^2\) 误差可以是多项式小，但必须证明这如何传到二阶 entropy/interaction quantity；仅有 kernel convergence、entropy \(o(n)\) 或有限 \(n\) 正号都不足够。若这三步中发现二缺陷和本身重新产生 \(n/\varepsilon\) 级主项，则立即把“\(\Gamma_c=O(\log(1/\varepsilon))\)”作为被证伪猜想处理；若二缺陷和只有 logarithmic nonuniformity，则继续尝试证明比现有 S51 端点包络少一个 \(1/\varepsilon\) 的高对比界。

目前最可信的研究判断可以概括为：新的实质增量已经不是“又一种 \(\Gamma\) 写法”，而是稀疏重采样表示加上一阶缺陷 \(p\)-曲率精确相消；最关键的未知量是二缺陷干涉及其随窗口/距离的增长；裸 inverse-moment 工具大概率方向错误；刚性是非一致展开的核心机制，但其定量剖面尚未证明；下一 cycle 应以“显式二缺陷系数 + remainder 的 \(n\)-一致性/失效尺度”为唯一主任务。
:::

如果你愿意，我还可以再把它压成一个更像 **Pro 任务书/Prompt** 的版本，直接用“目标—禁止事项—必须交付的定理—失败时输出什么”这种格式。

