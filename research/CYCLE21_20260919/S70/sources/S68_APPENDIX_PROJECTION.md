# 附录 P：支持分层、投影留数与真实插入后验熵

本文采用主报告的重采样模型，而不是把 \(\varepsilon\) 误认为翻位概率。条件于输入 bit=0，翻为 1 的概率为 \(\varepsilon p\)；条件于输入 bit=1，翻为 0 的概率为 \(\varepsilon(1-p)\)。

## P1. 任意正 k-层输入的分层系数

设 \(0<k<n\)，输入律 \(\mu\) 在每个 k-子集上严格正，在其他层为零。记 \(g=n-k\)、\(h=kg\)、\(\bar p=1-p\)、\(r=k\bar p+gp\)。输出概率按 \(\varepsilon\) 展开为

\[
 q_y=\mu_y+\varepsilon v_y+\varepsilon^2w_y+\cdots.
\]

令 \(S_d=\{y:||y|-k|=d\}\)。由于所有 k-子集均有正概率，\(q_y\) 的最低次数**恰好**是 d。所有最低阶系数在 \(0<p<1\) 严格正。

定义以下未归一化的真实输出质量：

\[
 A_y=\sum_{i\in y}\mu(y-i),\quad |y|=k+1;
 \qquad B_y=\sum_{j\notin y}\mu(y+j),\quad |y|=k-1;
\]

\[
 C_y=\sum_{\{i,j\}\subset y}\mu(y-\{i,j\}),\quad |y|=k+2;
\]

\[
 D_y=\sum_{\{i,j\}\subset y^c}\mu(y\cup\{i,j\}),\quad |y|=k-2.
 \tag{P1}
\]

因此

\[
 \sum A_y=g,\quad\sum B_y=k,\quad
 \sum C_y=\binom g2,\quad\sum D_y=\binom k2.
 \tag{P2}
\]

不存在的层按空和处理。另令

\[
 T_y=\sum_{i\in y,j\notin y}\mu(y-i+j),\quad |y|=k,
\]

\[
 \lambda_0(p)=\binom k2\bar p^2+\binom g2p^2+kgp\bar p.
\]

直接按实际翻位数分类，有下列**逐输出**公式：

| 输出层 | \(v_y\) | \(w_y\) |
|---|---|---|
| \(|y|=k\) | \(-r\mu_y\) | \(\lambda_0\mu_y+p\bar p T_y\) |
| \(|y|=k+1\) | \(pA_y\) | \(-p[k\bar p+(g-1)p]A_y\) |
| \(|y|=k-1\) | \(\bar pB_y\) | \(-\bar p[(k-1)\bar p+gp]B_y\) |
| \(|y|=k+2\) | 0 | \(p^2C_y\) |
| \(|y|=k-2\) | 0 | \(\bar p^2D_y\) |

例如 \(k+1\) 层的父配置必由删除一个输出粒子得到；一个翻位的 \(\varepsilon p\) 乘以其余 \(k\) 个 1 与 \(g-1\) 个 0 保持原位的概率，给出该行。距离为 3 的父配置只从三阶开始。零层的二阶项还保留一入一出的所有真实父配置 \(T_y\)，不能删去。

---

## P2. 熵与曲率的分层展开

逐层展开 \(-q_y\log q_y\)，得到

\[
 H(q)=H(\mu)-\varepsilon\log\varepsilon\,A_1(p)
 +\varepsilon B_1(p)-\varepsilon^2\log\varepsilon\,A_2(p)
 +\varepsilon^2B_2(p)+R_{\rm sing}.
 \tag{P3}
\]

具体地，

\[
 A_1=\sum_{S_1}v=r,\qquad
 A_2=\sum_{S_1}w+2\sum_{S_2}w=-2kgp\bar p,
 \tag{P4}
\]

\[
 B_1=-\sum_{S_0}v(1+\log\mu)-\sum_{S_1}v\log v,
 \tag{P5}
\]

\[
 \boxed{
 B_2=-\sum_{S_0}\left[w(1+\log\mu)+\frac{v^2}{2\mu}\right]
 -\sum_{S_1}w(1+\log v)-\sum_{S_2}w\log w.
 }
 \tag{P6}
\]

所有对数的参数在它们实际使用的层上严格正。没有出现 \(\log0\)，没有相减两个无限 KL。

(P4) 也有一个与输入位置分布无关的验证。因为输入粒子数为 k，实际增粒子数 G 和减粒子数 L 条件于任何输入都具有相同分布

\[
 G\sim\operatorname{Bin}(g,\varepsilon p),\qquad
 L\sim\operatorname{Bin}(k,\varepsilon\bar p),
\]

且独立。每个输出的 \(-\log\varepsilon\) 系数是 \(d=|G-L|\)，于是

\[
 \mathbb E|G-L|=\mathbb EG+\mathbb EL-2\mathbb E\min(G,L)
 =\varepsilon r-2kg\varepsilon^2p\bar p+O_n(\varepsilon^3).
\]

### P2.1 全部二階 p 导数

由 (P5) 和 (P2)，

\[
 B_1=r(1-H(\mu))-gp\log p-k\bar p\log\bar p
 -p\sum A\log A-\bar p\sum B\log B,
\]

所以

\[
 B_1''=-g/p-k/\bar p.
 \tag{P7}
\]

对 (P6) 求导，注意 v 对 p 仿射，得到完整的 actual-output 公式

\[
 \boxed{
 \begin{aligned}
 B_2''={}&-\sum_{S_0}w_{pp}(1+\log\mu)-\sum_{S_0}\frac{v_p^2}{\mu}\\
 &-\sum_{S_1}\left[w_{pp}(1+\log v)+2w_p\frac{v_p}{v}
 -w\left(\frac{v_p}{v}\right)^2\right]\\
 &-\sum_{S_2}\left[w_{pp}(1+\log w)+\frac{w_p^2}{w}\right].
 \end{aligned}}
 \tag{P8}
\]

因此

\[
 \boxed{
 H_{pp}=-\varepsilon(g/p+k/\bar p)
 +4kg\varepsilon^2\log(1/\varepsilon)
 +\varepsilon^2B_2''+\partial_p^2R_{\rm sing}.
 }
 \tag{P9}
\]

这说明 projection 支持奇异时，固定 n 的一阶 p-曲率一般不为零。它与 full-support Toeplitz 展开没有矛盾。

### P2.2 n=2 的独立核对

取 \(\mu(10)=\mu(01)=1/2\)，p=1/2。令 \(b=\varepsilon/2-\varepsilon^2/4\)。实际四元输出为

\[
 (q_{00},q_{10},q_{01},q_{11})=(b,1/2-b,1/2-b,b).
\]

完整 p 曲率为

\[
 H_{pp}=4\varepsilon^2\log\frac{1/2-b}{b}-\frac{2\varepsilon^2}{b}
 =-4\varepsilon+4\varepsilon^2\log(1/\varepsilon)-2\varepsilon^2+O(\varepsilon^3).
 \tag{P10}
\]

这同时检查了一阶、对数二阶和常数二阶的系数与符号。

---

## P3. 奇异 remainder 的完全显式 n 依赖

下面的界很粗，但不隐藏体积常数。取 \(p\in[u,1-u]\)、\(0<u\le1/2\)，令

\[
 \mu_*=\min_{|x|=k}\mu(x)>0,\qquad 0<\varepsilon\le1/(2n),
\]

\[
 L_*=\mu_*u^n/2,\quad M=2^n(n+1)^5,
 \quad B_*=2+\log M+|\log L_*|,
\]

\[
 F_*=312B_*M^5L_*^{-4},\qquad
 C_*=2^n(nM+F_*).
 \tag{P11}
\]

则

\[
 \boxed{\max\{|R_{\rm sing}|,|\partial_p^2R_{\rm sing}|\}
 \le C_*\varepsilon^3(1+|\log\varepsilon|).}
 \tag{P12}
\]

**证明。** 对任意 y，令 \(d=||y|-k|\)，并将概率写成

\[
 q_y=\varepsilon^d a_y(\varepsilon,p).
\]

a 是有限多项式。至少有一个距离正好为 d 的父配置，其质量至少 \(\mu_*\)；其 d 次翻位概率每次至少 \(\varepsilon u\)，其余不翻位概率至少 \(1-\varepsilon\)。因此

\[
 a_y\ge\mu_*u^d(1-\varepsilon)^{n-d}\ge L_*.
\]

把每个父配置的乘积转移概率展开，最多有 \(2^n\) 项，父配置权重的总和为 1。对 \(\varepsilon,p\) 的任意混合导数，总阶数不超过 5，其绝对值不超过 \(M\)；其中除去的 \(\varepsilon^d\) 已由所有父配置的翻位数至少 d 保证，没有负幂。

对 \(a\log a\)，总阶数不超过 5 的复合函数求导有至多 Bell(5)=52 个分组，外层导数的绝对值不超过 \(6B_*L_*^{-4}\)，各项内层乘积不超过 \(M^5\)。故所需的全部混合导数由 \(F_*\) 控制，零阶也包含在内。

现在分解

\[
 -q_y\log q_y=-\varepsilon^d\{d\log\varepsilon\,a_y+a_y\log a_y\}.
\]

d=0,1,2 时，对括号里的光滑系数 Taylor 截到总 \(\varepsilon\) 次数 2，且同时对 p 求至多两次导数；所需最高总导数阶为 5。单个输出的余项不超过

\[
 \varepsilon^3(nM|\log\varepsilon|+F_*).
\]

d≥3 时直接用同样的上界。最后对至多 \(2^n\) 个实际输出求和，得 (P12)。证毕。

### P3.1 循环投影下不隐藏的最小正原子

对连续 Fourier 循环投影，主报告式 (6.1) 给出

\[
 \mu_*\ge n^{-k}\left(\frac4n\right)^{k(k-1)}
 =4^{k(k-1)}n^{-k^2}.
 \tag{P13}
\]

因为每个非零圆周距离的正弦至少 \(\sin(\pi/n)\ge2/n\)。也可以先取补投影，用 \(\min(k,n-k)\) 改善该界。把 (P13) 代入 (P11)，即可得到只含 n、k、u 的显式常数。

(P12) 是合法固定体积展开的证据，不是 \(n\asymp1/\varepsilon\) 时展开仍一致的证据；其常数恶化非常快。不能把它粗略的恶化率冒充真实 remainder 的精确增长率。

---

## P4. 正则化投影基准中的极点、有限部分和碰撞后验

固定 \(p_0\in(0,1)\)，令输入为 \(\mu\)，重采样强度为 \(\eta\)。其输出基准律记为 \(\mu_\eta\)。对 DPP 投影输入，这就是

\[
 \mu_\eta=\operatorname{DPP}((1-\eta)P_N+\eta p_0I).
\]

在 \(\eta>0\) 时定义主报告的 full-support 对角预算 \(\mathcal D_n\)、自然异点和 \(S_n\) 和总量 \(\mathcal L_n\)。

### P4.1 对角项的留数

将 \(\mathcal D_n\) 写成所有单点边的实际全局质量之和：若一条边两端概率为 a,b，则该边的贡献为

\[
 (a+b)^2(1/a+1/b)=\frac{(a+b)^3}{ab}.
 \tag{P14}
\]

相邻输出的层距 d 相差 1。若较小层距为 d，则 (P14) 的起始阶为 \(\eta^{d-1}\)。因此仅零层与一层之间的边产生 \(1/\eta\) 极点。零层父配置 x 与其一次增加的输出 S 之间，留数是

\[
 \frac{\mu(x)^2}{p_0 A_S};
\]

一次删除的情形是 \(\mu(x)^2/[(1-p_0)B_T]\)。求和定义

\[
 \alpha_+=\sum_S\frac{\sum_{i\in S}\mu(S-i)^2}{A_S},\quad
 \alpha_-=\sum_T\frac{\sum_{j\notin T}\mu(T+j)^2}{B_T},
\]

\[
 D_{\rm res}=\alpha_+/p_0+\alpha_-/(1-p_0).
 \tag{P15}
\]

它们保留一错误输出的真实质量。于是

\[
 \mathcal D_n(\mu_\eta)=D_{\rm res}/\eta+d_0+O_{n,p_0,\mu}(\eta).
 \tag{P16}
\]

### P4.2 对角项的完全显式有限部分

定义

\[
 \gamma_{++}=\sum_{|S|=k+2}\frac{\sum_{i\in S}A_{S-i}^2}{C_S},\qquad
 \gamma_{--}=\sum_{|T|=k-2}\frac{\sum_{j\notin T}B_{T+j}^2}{D_T},
 \tag{P17}
\]

不存在的层贡献 0。则

\[
 \boxed{d_0=3n-r(p_0)D_{\rm res}-\alpha_+-\alpha_-+
 \gamma_{++}+\gamma_{--}.}
 \tag{P18}
\]

证明：对零层 a=μ+ηv0+⋯ 与一层 b=ηv1+η²w1+⋯ 的边，(P14) 的常数项为

\[
 3\mu+2\mu v_0/v_1-\mu^2w_1/v_1^2.
\]

使用 P1 的显式公式，上升边给 \(3\mu-(r+p_0)\mu^2/(p_0A)\)，下降边给 \(3\mu-(r+1-p_0)\mu^2/((1-p_0)B)\)。全部求和是 (P18) 的前四项。一层到二层的边贡献 \(v_1^2/w_2\)，正好是两个 γ；更外层只有 O(η)。证毕。

还可不借助任何最小原子界地证明

\[
 0\le\alpha_+\le g,\quad0\le\alpha_-\le k,
\]

\[
 0\le\gamma_{++}\le g(g-1),\qquad
 0\le\gamma_{--}\le k(k-1).
 \tag{P19}
\]

例如 \(A_{S-i}\le C_S\)、\(\sum_{i\in S}A_{S-i}=2C_S\)，所以
\(\sum_iA_{S-i}^2/C_S\le2C_S\)；再使用 \(\sum C_S=\binom g2\)。于是当 \(p_0\in[u,1-u]\) 时

\[
 |d_0|\le C_u n^2
 \tag{P20}
\]

可取例如 \(C_u=3+u^{-1}\)。这个有限部分的粗界对所有正 k-层输入都成立，不依赖 \(\mu_*\)。

### P4.3 自然 pair 和的精确极点与有限部分

对于 DPP 输入，由核参数导数的链式法则，

\[
 \mathcal L_n(\mu_\eta)=\eta^{-2}H_{pp}(\eta,p_0).
\]

使用 (P9) 和 \(S_n=\mathcal L_n+\mathcal D_n\)，得到

\[
 \boxed{
 \begin{aligned}
 S_n(\mu_\eta)={}&-A_n(p_0)/\eta+4kg\log(1/\eta)
 +F_n(p_0)+O_{n,p_0,\mu}(\eta(1+|\log\eta|)),\\
 A_n(p_0)={}&(g-\alpha_+)/p_0+(k-\alpha_-)/(1-p_0),\\
 F_n(p_0)={}&B_2''(p_0)+d_0(p_0).
 \end{aligned}}
 \tag{P21}
\]

这给出了一个明确的**补偿后有限部分**，而不是估计裸 inverse moment 后再假设主项消失。

同一个 \(4kg\log(1/\eta)\) 系数也能直接由实际条件表看出：外部输出含 k−1 个粒子的方块中，两个 opposite cells 是正的零层概率，两个同向 cells 是 O(η)，所以 log-odds 为 \(2\log(1/\eta)+O_n(1)\)。这类方块的实际总质量在每个输入上数出 kg 个异占据 pair；再乘有序因子 2，正好得到 4kg。其他外部粒子数没有遗漏一个同阶 log 主项。

### P4.4 常对角投影的留数下界

假设投影矩阵 \(P_N\) 的对角恒为 \(\rho=k/n\)，且其 k-子集行列式均正。对 \(|S|=k+1\)，Gram 矩阵 \((P_N)_S\) 的秩为 k，其伴随矩阵为 \(A_Svv^*\)，v 为单位零向量。因此

\[
 \mu(S-i)/A_S=|v_i|^2.
\]

延拓的 v 属于 \(\ker P_N\)，由正交投影的 Cauchy–Schwarz，

\[
 |v_i|^2=|\langle(I-P_N)e_i,v\rangle|^2\le1-\rho.
\]

从而

\[
 \alpha_+=\sum_S A_S\sum_i|v_i|^4
 \le(1-\rho)\sum_SA_S=g^2/n.
\]

对补投影得到 \(\alpha_-\le k^2/n\)。代入 (P21)，

\[
 \boxed{A_n(p_0)\ge\frac{kg}{n p_0(1-p_0)}.}
 \tag{P22}
\]

在半密度、中点，\(A_n\ge n\)。这严格排除了 \(S_n/n\) 在这些有限循环端点上的统一 logarithmic 界。注意 (P21) 的误差仍是固定 n；不能仅因留数下界对 n 一致，就把整个展开在 n 与 η 的联合尺度上当成一致展开。

---

## P5. 二阶常数项的真实插入/删除后验熵表达

定义四个对数质量和

\[
 L_+=\sum A\log A,\quad L_-=\sum B\log B,
 \quad L_{++}=\sum C\log C,\quad L_{--}=\sum D\log D.
\]

对零层使用 \(v=-r\mu\)、\(w=\lambda_0\mu+p\bar pT\)，对其他四层使用 P1 表格，代入 (P8)，逐项求导得到

\[
 \boxed{
 B_2''(p)=\frac h{p\bar p}-2h\log(p\bar p)-4h-n+\mathcal C_\mu,
 }
 \tag{P23}
\]

其中 d=g−k，

\[
 \mathcal C_\mu=(n^2-n-6h)H(\mu)-2\mathscr D_\mu
 +2(d-1)L_+-2(d+1)L_--2L_{++}-2L_{--}.
 \tag{P24}
\]

这里

\[
 \mathscr D_\mu=\sum_x\mu(x)\sum_{y:\,y=x-i+j}
 \log\frac{\mu(x)}{\mu(y)}.
\]

无向交换边合并后，其每条贡献是
\((\mu(x)-\mu(y))\log(\mu(x)/\mu(y))\ge0\)。

### P5.1 对求导常数的独立核对

零层贡献使用

\[
 \lambda_0''=d^2-n,\quad (p\bar p)''=-2,
\]

\[
 \sum_yT_y\log\mu_y=-hH(\mu)-\mathscr D_\mu.
\]

上升一层的 p 依赖是

\[
 f_+(p)=p[k+(d-1)p],
\]

其熵常数贡献为 \(g f_+(1+\log p)+f_+L_+\)。二阶导数的前一项是

\[
 g[k/p+(d-1)(5+2\log p)].
\]

下降一层交换 p、\(\bar p\) 与 k、g 即可。二上升层贡献
\(-2\binom g2p^2\log p-p^2L_{++}\)，二下降层同理。合并得到 (P23)–(P24)，包括常数 \(-4h-n\)。

### P5.2 真实反向条件熵

取 \(X\sim\mu\)，在 X 的 g 个空位中均匀选择一个并加粒子。输出律为 \(A/g\)。由于

\[
 H(Y_+\mid X)=\log g,
\]

链式恒等式给出

\[
 h_+:=H(X\mid Y_+)=H(\mu)+\log g-H(A/g),
 \quad L_+=-gH(\mu)+g h_+.
 \tag{P25}
\]

同样，

\[
 L_-=-kH(\mu)+k h_-,
\]

\[
 L_{++}=-\binom g2H(\mu)+\binom g2h_{++},\quad
 L_{--}=-\binom k2H(\mu)+\binom k2h_{--}.
 \tag{P26}
\]

代入 (P24)，所有裸的 \(H(\mu)\) 系数精确相消，得到

\[
 \boxed{
 \mathcal C_\mu=-2\mathscr D_\mu
 +2g(d-1)h_+-2k(d+1)h_-
 -g(g-1)h_{++}-k(k-1)h_{--}.
 }
 \tag{P27}
\]

这是真实通道反向信息量的表达。它与随意将条件方块等权平均不同。一般密度下 h 的某些系数有正号，本文没有在所有密度上声称逐项支付。

---

## P5.3 投影几何给出的反向熵下界与一个严格符号结论

对常对角秩 k 投影，设 \(\rho=k/n\)。在真实输入上均匀增加 r 个空位，给定输出 S、\(|S|=k+r\)，父配置由删除某个 r-子集 A 得到。令 V 的列为 \((P_N)_S\) 零空间的一组标准正交基。矩阵的 rank-k 分解及互补 minor 恒等式给出

\[
 \Pr(\text{删除集合}=A\mid S)=\det(V_AV_A^*).
 \tag{P27a}
\]

其归一化可由 \(\sum_{|A|=r}|\det V_A|^2=\det(V^*V)=1\) 直接核查。延拓后的 V 的列都属于 \(\ker P_N\)，所以 \(VV^*\le I-P_N\)。Hadamard 行列式不等式于是给出

\[
 \Pr(A\mid S)\le(1-\rho)^r.
\]

因此不论 S 的实际权重如何，真实反向条件熵都满足

\[
 \boxed{h_{+r}\ge r\log\frac1{1-\rho},\qquad
 h_{-r}\ge r\log\frac1\rho.}
 \tag{P27b}
\]

第二个式子对补投影应用相同论证。这里的点态输入是一个已证明的投影 minor 概率上界，不是被反例否定的 conditional-skew 点态符号假设。

特别地，任何常对角 1/2、满 k-层支撑的秩 n/2 投影都满足

\[
 h_+,h_-\ge\log2,\qquad h_{++},h_{--}\ge2\log2
\]

（相应二插入通道不存在时，其系数本来就是零）。将这些下界代入 (P23)、(P27)，即使不另外假设补集对称，也得到

\[
 \boxed{B_{2,n}''(1/2)\le-n-2\mathscr D_\mu\le-n<0.}
 \tag{P27c}
\]

这是奇异展开的**二阶常数项**的普适符号定理；它既不是每个 pair 的符号定理，也没有删除同阶的正 \(4kg\log(1/\varepsilon)\) 项或第三阶余项。因此不能把 (P27c) 误报为原始熵率凹性已经证明。

---

## P6. 循环 Vandermonde 输入的精确交换能量

连续 Fourier 秩 k 投影律为

\[
 \log\mu(x)=-k\log n+\sum_{a<b}V_{ab}X_aX_b,
 \quad V_{ab}=2\log\left(2\sin\frac{\pi|a-b|}n\right).
 \tag{P28}
\]

定义未归一化交换算子

\[
 (\mathscr A f)(x)=\sum_{i\in x,j\notin x}[f(x-i+j)-f(x)].
\]

对于不同 a,b，按 \((X_a,X_b)=(0,0),(1,0),(0,1),(1,1)\) 四种情况逐一数数，得到

\[
 \mathscr A(X_aX_b)=(k-1)(X_a+X_b)-2(n-1)X_aX_b.
 \tag{P29}
\]

单位根乘积给出

\[
 \prod_{d=1}^{n-1}2\sin(\pi d/n)=n,
 \quad\sum_{b\ne a}V_{ab}=2\log n.
 \tag{P30}
\]

(P30) 可由 \((z^n-1)/(z-1)\) 在 z=1 的值及根分解直接证明。将 (P29) 代入 (P28)，

\[
 \mathscr A\log\mu=-2(n-1)\log\mu-2kg\log n.
\]

因此

\[
 \boxed{\mathscr D_\mu=-\mathbb E_\mu\mathscr A\log\mu
 =2kg\log n-2(n-1)H(\mu).}
 \tag{P31}
\]

这不是 corrected law 的假设，也没有使用连续极限或体积 entropy asymptotics。

---

## P7. 半密度二阶项与补偿后有限部分的增长

设 n 偶数，k=g=n/2。补投影的 Fourier 频率块是原频率块的平移，故与原投影对角酉共轭。孔过程的核为补投影，因此输入律满足 \(\mu(x)=\mu(x^c)\)。于是

\[
 h_+=h_-=h_1,\qquad h_{++}=h_{--}=h_2.
\]

在 p=1/2，(P23)、(P27)、(P31) 给出

\[
 \boxed{
 \begin{aligned}
 B_{2,n}''(1/2)={}&n^2\log2-n-n^2\log n+4(n-1)H(\mu)\\
 &-2n h_1-(n^2/2-n)h_2.
 \end{aligned}}
 \tag{P32}
\]

反向通道给定一个 k+1 粒子输出，至多有 k+1 个父配置；给定 k+2 粒子输出，至多有 \(\binom{k+2}2\) 个父配置。因此

\[
 0\le h_1\le\log(k+1),\quad
 0\le h_2\le\log\binom{k+2}2,
 \quad0\le H(\mu)\le\log\binom nk.
 \tag{P33}
\]

将这些界代入 (P32)，即得主报告 (7.5)–(7.6)。特别地，

\[
 \boxed{-2+o(1)\le B_{2,n}''(1/2)/(n^2\log n)\le-1+o(1).}
 \tag{P34}
\]

因此 \(B_{2,n}''(1/2)=-\Theta(n^2\log n)\)。没有宣称比值极限存在或等于某个常数。


利用更强的 (P27c)，上界还能改进为

\[
 B_{2,n}''(1/2)\le-n-n^2\log n+4(n-1)H(\mu)
 \le-n^2\log n+4n(n-1)\log2-n.
 \tag{P34a}
\]

下界 (主报告 7.5) 对 n≥4 蕴含 \(B_{2,n}''(1/2)\ge-2n^2\log n\)。所以，对于所有偶数 n≥256，已有完全显式的量级界

\[
 \boxed{-2n^2\log n\le B_{2,n}''(1/2)\le-\tfrac12n^2\log n.}
 \tag{P34b}
\]

而 (P27c) 另外证明了它对所有允许的有限 n 都严格为负，不必等待这个渐近阈值。

### P7.1 补偿后 pair 有限部分也有相同量级

由 (P20)，\(d_0=O(n^2)\)。故 (P21) 定义的真正补偿后有限部分

\[
 F_n(1/2)=\lim_{\eta\downarrow0}\left[S_n(\mu_\eta)+A_n(1/2)/\eta-n^2\log(1/\eta)\right]
\]

满足

\[
 \boxed{-2+o(1)\le F_n(1/2)/(n^2\log n)\le-1+o(1).}
 \tag{P35}
\]

这同时揭示了两层非一致性：首先是真实一错误碰撞后验产生的 \(1/\eta\) 极点；其次是去掉该极点与显式 \(\log(1/\eta)\) 项以后，有限部分仍有 \(n^2\log n\) 规模。

### P7.2 哪些结论不能由此推出

(P34)–(P35) 不给出固定 \(\eta>0\)、n→∞ 的熵率曲率，不证明自然匹配尺度正好是 \(1/\eta\)，也不证明无限 true-sine \(\Gamma\) 的 logarithmic 猜想为假。它们证明的是明确的有限投影系数增长，并使“只看二阶正 logarithmic 项”或“只看一阶 p 曲率相消”的推断不再合法。

该分解还给出下一步真正的观测量：真实一错误后验的碰撞概率 \(\alpha_\pm\)、真实一/二插入的反向条件熵 \(h_\pm,h_{\pm\pm}\)、以及完整多缺陷 remainder。它们必须在同一实际输出模型与一致的 n、η 量词下匹配。
