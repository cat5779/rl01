# SA02 第二轮：共同逆得分矩阵、双侧 Bellman 势与完整块曲率包络

## 状态与范围

**PROVED**：维数无关的共同逆得分矩阵鞅；两侧凸化的矩阵 Bellman 势；以一次共同 Fisher 增益支付整个重叠块的条件域变更；覆盖完整配置熵二阶导数的块包络，空间/观察误差分别为 `O(log m / m)` 和 `O(1/L)`，没有近场度数因子；一般严格通道的全体积曲率上界及一个明确负曲率参数区域。

**INCOMPLETE**：指定 `rho=1/2,c=19/20,a=1/40` 上，全近场的净负支付。下面的上界尚未在这一点被证明为负。尤其不把新的有理局部观测量的符号列作定理前提后宣称完成。

本稿不是旧的“加权度数至多 2”规则的推广。新对象允许完整块中的全部 pair。它也不是全局 sine 熵凹性的证明。所有 a 导数固定 Q,c；当讨论平衡点 `a=(1-c)/2` 时，也只是在该点评价这一 a 导数，不是沿平衡曲线改变 c 求导。

输入是 TASK_02_LOCAL_SIGNED_COMPENSATION.md 中的完整 Hessian 分解、S7 尾界与逆矩阵空间能量界。Q 始终是实际有限 Toeplitz 压缩，不当作有限投影。没有重新计算旧六点证书，没有哈希检查。

## 1. 域外迁移，以及没有迁移的条件

采用两个实际发生作用的来源。

第一，离散 Bochner/Bellman 机制把局部二阶变化嵌入一个共同随机过程，以二次变差支付，而不是分别向每条边收取一整份预算。Caputo–Dai Pra–Posta 的 Bochner 方法需要其可逆性、交换变换及配对测度条件；这些条件不能从本题的负相关性直接推出。因此本文不引用其熵衰减定理来证明 a 曲率，而是重新构造共同得分矩阵鞅，并在一个显式凸域上证明候选势的 Hessian 界。[R1]

第二，矩阵逆二次型的 Gauss 型求积把积分表达转成可验证的有理单侧证书。Li–Sra–Jegelka 的逆矩阵求积工作所依赖的正谱条件不能直接用于本题通常不定的掩码逆矩阵。本文只借鉴“分辨率参数 + 有符号核 + 明确余量”的结构，重新证明每个标量分母的符号及余量方向。[R2]

也核对了两个未能直接闭合的迁移：强 Rayleigh 的 modified log-Sobolev 不等式控制适配 Markov 链的熵耗散，不是本题的固定 Q,c 的 a 二阶导数；图上 W_{1,+} 测地线熵定理另有速度与二阶流兼容条件，不由概率的塔性质提供。[R3,R4] Shepp–Olkin 的计数熵结论不能替换完整标记配置熵。[R5]

不宣称这些组合是首次出现；这里可检查的是下面逐项给出的公式与证明。

## 2. 共同矩阵与两个 Fisher 量

令 V 为有限站点集，

\[
 A_V(Y)=K_V-\operatorname{diag}(1-Y_V),\qquad G_V=A_V(Y)^{-1}.
\]

矩阵 Hermitian，所有真实原子严格正。记

\[
 Z_i=(G_V)_{ii},\quad h_{ij}=|(G_V)_{ij}|^2,\quad
 F_V=\sum_i E Z_i^2,\quad J_V=E\Big(\sum_i Z_i\Big)^2.
\]

这里 `F_V` 是完整分解中的对角 Fisher 总和，`J_V` 是共同 a 方向的完整 Fisher；不可混同。

局部对角扰动给出

\[
 Z_i=\partial_{a_i}\log p_Y
 =\frac{2Y_i-1}{P(Y_i\mid Y_{V\setminus i})}.
\]

因此

\[
 F_V=\sum_i E f(P(Y_i=1\mid Y_{V\setminus i})).
\]

对 i≠j，完整原子关于对角变量的混合导数为

\[
 \partial_{a_i a_j}p_Y=p_Y(Z_iZ_j-h_{ij}).
\]

求和归一化给出

\[
 E Z_iZ_j=E h_{ij},\qquad
 \boxed{J_V=F_V+2\sum_{i<j}E h_{ij}.}                 \tag{2.1}
\]

故跨边能量进入同一个 J_V，不带图度数。等式不是任意负相关表集合的事实，而使用了同一完整 DPP 原子的对角扰动相容性。

本稿后面的通用 Q 推论还用到：完整 Hessian 分解本身不依赖 Toeplitz。只扰动目标 i,j 的对角时，外部边缘概率不变，条件两点核的两个对角分别以斜率 1 变化，非对角不变。因此条件四原子的混合导数依次是 (+1,−1,−1,+1)。将其乘 log 原子求和，得 −log(BC/AD)；再与 (2.1) 合并，即得题面 (1) 的同一分解。这证明其可用于任意固定正收缩 Q，而不是假设 sine 专属公式可任意外推。

## 3. 完整 pair 成本的有符号分辨核

固定 pair 的实际外部输出，条件表记为 P=(A,B,C,D)，边缘 q,r，s=BC−AD≥0。对真实 pair word b 设 ε_b=(2b_i−1)(2b_j−1)，p_b 为该原子，

\[
 D_b=p_b+\varepsilon_b s>0.
\]

D_b 恰是对应单点边缘概率之积。条件 Schur 补及两阶逆矩阵给出

\[
 h_{ij}=s/p_b^2,\qquad
 v_{ij}:=Z_iZ_j=\varepsilon_bD_b/p_b^2,
 \qquad v_{ij}-h_{ij}=\varepsilon_b/p_b.
                                                        \tag{3.1}
\]

定义（t 不是 a）

\[
 S_{ij}(t;Y)=\frac{h_{ij}^{\,2}}{v_{ij}-t h_{ij}},\qquad0\le t\le1.
\]

分母永不为零。ε=1 时为正，ε=−1 时为负。并且

\[
 S'_{ij}(t)=\frac{h_{ij}^3}{(v_{ij}-th_{ij})^2}\ge0.
                                                        \tag{3.2}
\]

令

\[
 \phi(z)=\int_0^1\frac{1-t}{1-tz}\,dt
 =\frac{z+(1-z)\log(1-z)}{z^2},\qquad\phi(0)=1/2.
\]

由 (3.1)，逐 word 有

\[
 \int_0^1(1-t)S_{ij}(t;b)\,dt
 =\frac{s}{p_b^2}+\frac{\varepsilon_b}{p_b}\log\frac{p_b}{D_b}.
\]

乘真实权重 p_b 后求和，四个 log D_b 项抵消。因此得到精确式

\[
 \boxed{g(P)=-E_{b\mid\mathrm{outside}}
                  \int_0^1(1-t)S_{ij}(t;b)\,dt.}         \tag{3.3}
\]

所有边此时都是同一个随机矩阵 G_V 的函数。没有平均条件 DPP 核。

由于 S(t)≥S(0)，定义显式非负余量

\[
 r_{ij}(Y)=\int_0^1(1-t)[S_{ij}(t;Y)-S_{ij}(0;Y)]\,dt\ge0.
\]

其分子式为

\[
 r_{ij}(Y)=\frac{h_{ij}^3}{v_{ij}^2}
   \int_0^1\frac{t(1-t)}{1-t h_{ij}/v_{ij}}\,dt.
\]

于是

\[
 E g(P_{ij})=-\tfrac12 E S_{ij}(0)-E r_{ij}.             \tag{3.4}
\]

## 4. 块势：所有内部边一次进入

对 Hermitian X，假设其对角非零，定义

\[
 \mathfrak T(X)=\sum_{i,j}\frac{|X_{ij}|^4}{X_{ii}X_{jj}}.
                                                        \tag{4.1}
\]

对角项就是 X_ii²。对任意块 I⊂V，仍保留 V 中完整外部条件，定义

\[
 \mathcal C_I^V=-\sum_{i\in I}E Z_i^2
                  +2\sum_{i<j\in I}E g(P_{ij}).
\]

由 (3.4) 得到

\[
 \boxed{\mathcal C_I^V
 =-\tfrac12\sum_{i\in I}E Z_i^2
  -\tfrac12 E\mathfrak T((G_V)_{II})
  -2\sum_{i<j\in I}E r_{ij}.}                          \tag{4.2}
\]

这在完整图上成立，没有 `degree≤2`。负 Fisher 只出现一份：右端显式半份加上势对角中的半份。非对角的全部有符号贡献由一个矩阵势承接。

这仍不意味着 `E mathfrak T≥0`；后者下面保持未证。

## 5. 共同逆得分矩阵鞅：P1 的新接口

若 I⊂A⊂V，则

\[
 \boxed{E[(G_V)_{II}\mid Y_A]=(G_A)_{II}.}             \tag{5.1}
\]

证明：取任意支持在 I×I 上的 Hermitian 扰动 H。严格谱隙保证足够小的实扰动 K+uH 仍为合法核。对有限边缘化等式

\[
 p_A(Y_A)=\sum_{Y_{V\setminus A}}p_V(Y)
\]

求 u 导数，得到

\[
 E[\operatorname{Tr}((G_V)_{II}H)\mid Y_A]
 =\operatorname{Tr}((G_A)_{II}H).
\]

H 任意，故 (5.1) 成立。这里只平均了似然的矩阵得分，不是平均条件核。

固定 I，沿 A=A_0⊂A_1⊂…⊂A_T=V 逐点揭示额外输出，令

\[
 M_t=(G_{A_t})_{II}.
\]

所有过程使用同一滤过 `sigma(Y_A_t)`，目标 I 已经在初始观察中。单步 Schur 补给出

\[
 M_t-M_{t-1}=\zeta_t w_tw_t^*,
\]

其中，在过去条件下，`zeta=1/u` 的概率为 u，`zeta=−1/(1−u)` 的概率为 1−u。故增量均值零、秩一，且

\[
 \|\Delta M_t\|_{HS}^2=(\operatorname{Tr}\Delta M_t)^2.
\]

由鞅差正交，

\[
 \boxed{
 E\|M_T-M_0\|_{HS}^2
 =\sum_t E\|\Delta M_t\|_{HS}^2
 =E(\operatorname{Tr}M_T)^2-E(\operatorname{Tr}M_0)^2.}
                                                        \tag{5.2}
\]

右端是对 I 上共同对角扰动方向的观测 Fisher 增益。全矩阵二次变差只付一次；并没有为各个 pair 另建一条互不相容的揭示路径。

## 6. 显式凸域与双侧 Bellman 势：真正的支付引理

记

\[
 \delta=\min(a,1-a-c),\quad
 \beta_*=\delta(\delta+c),\quad
 \kappa=\frac{c^2}{4\beta_*},\quad
 \bar\kappa=\max(1,\kappa),\quad
 r_\delta=\frac{1-\delta}{\delta},
\]

并定义

\[
 \boxed{\Gamma_{\delta,c}
 =\bar\kappa(6+8r_\delta+3r_\delta^2).}                 \tag{6.1}
\]

### 6.1 真实矩阵落入同一个凸域

对所有相应真实边缘的掩码逆矩阵主块，

\[
 \|X\|\le\delta^{-1},\qquad
 \sigma_i X_{ii}\ge(1-\delta)^{-1},\qquad
 |X_{ij}|^2\le\bar\kappa |X_{ii}X_{jj}|,               \tag{6.2}
\]

其中 σ_i=2Y_i−1，在本次条件平均中固定。

前两项来自严格通道谱隙与真实单点条件概率。第三项：同号 word 的 (3.1) 给出 h/v<1；异号 word 给出

\[
 \frac{h}{|v|}=\frac{s}{q(1-r)}
 \quad\hbox{或}\quad \frac{s}{(1-q)r}.
\]

写条件核 C=aI+cR，R 是正收缩，R_ii=x,R_jj=y，则

\[
 s\le c^2\min\{xy,(1-x)(1-y)\}.
\]

固定 x，商在 y≤1−x 区间递增，在 y≥1−x 区间递减，因此最大值在 y=1−x。于是

\[
 \frac{s}{q(1-r)}
 \le\frac{c^2x(1-x)}{(a+cx)(d+cx)}
 \le\frac{c^2x(1-x)}{(\delta+cx)^2}
 \le\frac{c^2}{4\delta(\delta+c)}.
\]

最后最大点为 x=δ/(2δ+c)。另一异号 word 同理。

固定 σ 后，(6.2) 是凸域：算子范数球与对角半空间是凸的；最后一项等价于

\[
 \begin{pmatrix}
 \sigma_iX_{ii}&X_{ij}/\sqrt{\bar\kappa}\\
 \overline{X_{ij}}/\sqrt{\bar\kappa}&\sigma_jX_{jj}
 \end{pmatrix}\succeq0,
\]

也是凸约束。故真实矩阵及其条件均值之间的线段留在已检查的域内，不要求线段上的矩阵本身为某个条件 DPP 核。

### 6.2 Hessian 界

在该凸域上，对任何 Hermitian 方向 H，

\[
 \boxed{|D^2\mathfrak T(X)[H,H]|
             \le 2\Gamma_{\delta,c}\|H\|_{HS}^2.}      \tag{6.3}
\]

详细估计如下。写 a_i=1/X_ii，b_ij=|X_ij|⁴，对乘积 a_i a_j b_ij 二次求导。记 M=δ^{-1}、ell=(1−δ)^{-1}，M/ell=r_delta。

* b_ij 的二阶导数满足 `|b''|≤12|X_ij|²|H_ij|²`。乘以 `1/|X_ii X_jj|`，全部求和至多 `12 barκ ||H||²`。
* 权重的一阶导数与 b_ij 的一阶导数的交叉项，在交换 i,j 后由行 Cauchy–Schwarz 至多 `16 barκ (M/ell)||H||²`。
* 权重二阶导数的两种单点项至多 `4 barκ (M/ell)²||H||²`；交叉项至多 `2 barκ (M/ell)²||H||²`。这里使用对称非负矩阵 `(|X_ij|²/|X_ii X_jj|)` 的行和上界 `(M/ell)²`。

合计为 `barκ(12+16r+6r²)||H||²`，即 (6.3)。这些常数来自解析不等式，不是拟合。

所以两个势

\[
 \boxed{\mathfrak B_\pm(X)
 =\Gamma_{\delta,c}\|X\|_{HS}^2\pm\mathfrak T(X)}       \tag{6.4}
\]

均在该域上凸。对 (5.1) 使用条件 Jensen，再用 (5.2)，得到完整块的兼容支付关系

\[
 \boxed{
 |E\mathfrak T(M_T)-E\mathfrak T(M_0)|
 \le\Gamma_{\delta,c}
     \sum_t E\|\Delta M_t\|_{HS}^2
 =\Gamma_{\delta,c}\Delta J_I.}                        \tag{6.5}
\]

这是对任意块大小、所有内部 pair 同时成立的 P3。支付系数明确为 Γ，不是 1。不能将 ΓΔJ 隐瞒成一份 Fisher 增益；下面把它作为显式观察误差支付。

## 7. 观察域变更：一次跨域能量，不乘边数

给定 Y_A，独立抽取两个实际完整输出 Y,Y'，二者在 A 上相同。令 O=V\A。由 (5.1) 与条件独立副本恒等式，

\[
 E\|(G_V)_{II}-(G_A)_{II}\|_{HS}^2
 =\tfrac12 E\|(G_V(Y))_{II}-(G_V(Y'))_{II}\|_{HS}^2.
\]

逆矩阵差式给出

\[
 (G_V(Y)-G_V(Y'))_{II}
 =G_V(Y)_{IO}\operatorname{diag}(Y'_O-Y_O)G_V(Y')_{OI}.
\]

利用 `||G_V(Y')||≤δ^{-1}`，得到

\[
 \boxed{
 E\|(G_V)_{II}-(G_A)_{II}\|_{HS}^2
 \le\frac1{2\delta^2}
       E\sum_{i\in I,j\notin A}|(G_V)_{ij}|^2.}        \tag{7.1}
\]

结合 (6.5)，

\[
 |E\mathfrak T((G_V)_{II})-E\mathfrak T((G_A)_{II})|
 \le\frac{\Gamma_{\delta,c}}{2\delta^2}
       E\sum_{i\in I,j\notin A}|(G_V)_{ij}|^2.          \tag{7.2}
\]

同时，单点得分条件 Jensen 给出 `E(G_V)_ii²≥E(G_A)_ii²`。将它与 (4.2) 合并，定义

\[
 Q(I,A)=-\tfrac12 E\left[\sum_{i\in I}(G_A)_{ii}^2
                         +\mathfrak T((G_A)_{II})\right],
\]

则

\[
 \boxed{
 \mathcal C_I^V\le Q(I,A)
  +\frac{\Gamma_{\delta,c}}{4\delta^2}
        E\sum_{i\in I,j\notin A}|(G_V)_{ij}|^2.}        \tag{7.3}
\]

注意没有 `|I|`、内部边数或最大图度数乘在右边的跨域能量前。

## 8. 进入完整 H_n''：随机平移分块与全部边界

令 V=[n]，m,L≥1 为整数。对 θ=0,…,m−1，用无限整数线上平移 θ 的长度 m 网格切分 V，得到分割 pi_theta；边界块允许短于 m。每个块 I 使用

\[
 A_I=(I+[-L,L])\cap V.
\]

每个 θ 下每个站点只属于一个核心块 I。因此 (7.3) 的 Fisher 预算使用一次，且跨域能量求和满足

\[
 \sum_{I\in\pi_\theta}E\sum_{i\in I,j\notin A_I}|G_{ij}|^2
 \le nB_*/L.
\]

一条长度为 r 的边被网格切断的 θ 比例恰为 `min(r/m,1)`。记调和数 H_m^(harm)=Σ_{k=1}^m1/k。由 S7 尾界，

\[
 \begin{aligned}
 2\sum_{i<j}\min((j-i)/m,1)E|g_{ij}|
 &=\frac1m\sum_{k=1}^m2\sum_{j-i\ge k}E|g_{ij}|\\
 &\le nC_*H_m^{(harm)}/m.
 \end{aligned}
\]

故精确保留截断边界的有限版本为

\[
 \boxed{
 \frac{H_n''}{n}\le
 \frac1{mn}\sum_{\theta=0}^{m-1}\sum_{I\in\pi_\theta}Q(I,A_I)
 +\frac{C_*H_m^{(harm)}}m
 +\frac{\Gamma_{\delta,c}B_*}{4\delta^2L}.}             \tag{8.1}
\]

这是完整 H_n'' 的上界，不是删掉其他近场之后的子块估计。

### 平稳、单窗口版本

取 I=[1,m]、A=[1−L,m+L] 的实际无限平稳 sine 边缘，定义

\[
 \boxed{\mathcal U_{m,L}
 =-\frac1{2m}E\left[
       \sum_{i=1}^m(G_A)_{ii}^2
       +\sum_{i,j=1}^m\frac{|(G_A)_{ij}|^4}
                              {(G_A)_{ii}(G_A)_{jj}}
                     \right].}                         \tag{8.2}
\]

该量不含对数，且所有 pair 来自一个实际窗口，非平均核。

令

\[
 \Xi_\delta=\tfrac12[\delta^{-2}+(1-\delta)^2\delta^{-4}].
\]

由行平方和上界，`|Q(I,A)|≤Xi_delta |I|`，`|U_mL|≤Xi_delta`。每个相位下受端点或观察截断影响的核心站点不超过 `2(m+L)`；将这些块与平稳窗口替换的总代价不超过 `4Xi_delta(m+L)`。于是

\[
 \boxed{
 \frac{H_n''}{n}\le\mathcal U_{m,L}
 +\frac{C_*H_m^{(harm)}}m
 +\frac{\Gamma_{\delta,c}B_*}{4\delta^2L}
 +\frac{4\Xi_\delta(m+L)}n.}                            \tag{8.3}
\]

这是与题面式(2)并列的新单侧接口。观察误差没有近场半径乘子；尾项变成 `log m/m`，代价来自随机分块，不是无代价去掉边界。

**必须保留的限制**：这是单侧上包络，不是 `|H_n''/n−U_mL|` 的误差界。式(4.2)的非负余量被舍弃；因此不能声称 m,L→∞ 时 U_mL 自动收敛到实际曲率。新包络与原式(2)也不存在已证的逐点大小次序。

### 指定参数的常数

在 rho=1/2,c=19/20,a=1/40 下，

\[
 \kappa=361/39,\quad r_\delta=39,\quad
 \Gamma_{\delta,c}=587347/13,\quad B_*=1155200/507,
\]

\[
 \frac{\Gamma_{\delta,c}B_*}{4\delta^2}
 =\frac{271401301760000}{6591}\approx4.1177560577\times10^{10}.
\]

因此观察误差仍然需要很大 L 才变小。这不是可直接运行的实用认证尺度。它的已证增益在于消除了边数/半径放大，以及给出真正共同的条件域；不是声称已经在种子参数证明负曲率。

## 9. 全图已支付的曲率估计与一个负曲率区域

令

\[
 \ell(x)=\int_0^1\frac{(1-t)x}{1+tx}\,dt
 =\frac{(1+x)\log(1+x)-x}{x},\qquad\ell(0)=0.
\]

该函数递增。对同号 pair word，S(t)≥0，其贡献只帮助上界；异号时，由 (6.2)，

\[
 -\int_0^1(1-t)S(t)dt
 =h\,\ell(h/|v|)\le h\,\ell(\kappa).
\]

由 (2.1) 得到无图度数限制的全部 pair 支付：

\[
 \boxed{H_n''\le\ell(\kappa)J_V-[1+\ell(\kappa)]F_V.} \tag{9.1}
\]

这是已闭合不等式，不以未知矩阵正性为假设。它比保留有符号矩阵势的版本粗，但可以给出完整负曲率区域。

用实际生成机制 X~DPP(Q)、`Y_i|X~Bern(a+cX_i)`。完整通道得分为

\[
 S_c=\sum_i\frac{Y_i-a-cX_i}{(a+cX_i)(1-a-cX_i)}.
\]

`E(S_c|Y)=Tr G_V`；条件于 X 时各项独立且均值零。因此

\[
 J_V\le\sum_i\left[
 \frac{1-Q_{ii}}{a(1-a)}+
 \frac{Q_{ii}}{(a+c)(1-a-c)}\right].
\]

又由条件 Jensen，`F_V≥Σ_i f(a+cQ_ii)`。对 sine，Q_ii=rho，故

\[
 \boxed{\frac{H_n''}n\le
 \ell(\kappa)\left[\frac{1-\rho}{a(1-a)}
               +\frac{\rho}{(a+c)(1-a-c)}\right]
 -[1+\ell(\kappa)]f(a+c\rho).}                         \tag{9.2}
\]

对所有严格参数、所有 n 成立。右端为负的区域给出完整配置熵的负 a 曲率。

在平衡评价点 a=(1−c)/2，设 β=(1−c²)/4。则 J_V≤n/β、F_V≥4n，κ=c²/(1−c²)，从而

\[
 \boxed{\frac{H_n''}n
 \le\frac4{1-c^2}\big[-\log(1-c^2)-1\big].}           \tag{9.3}
\]

于是对任意有限正收缩 Q（不限于 sine）、任意 n，

\[
 c<\sqrt{1-e^{-1}}\approx0.795060097621
 \Longrightarrow H_n''((1-c)/2)<0.
\]

这不是整个 a 区间的凹性断言。一般参数的区域由 (9.2) 定义；连续性还给出平衡评价点周围的开区域。种子 c=.95 时 (9.3) 的上界约为 `+54.4780677324`，故不能用于种子符号。

## 10. 保留更强有符号内容：矩阵缺口与有理层级

令 M=E ZZ^T 为完整多参数 Fisher 矩阵；M_ii=F_i，M_ij=E h_ij。令 N_ii=0，

\[
 N_{ij}=E_{\mathrm{outside}}
  \frac{s_{ij}}{q_{ij}(1-q_{ij})r_{ij}(1-r_{ij})}.
\]

由四原子直接通分，

\[
 E S_{ij}(0)=M_{ij}-N_{ij}.
\]

定义 T=M−N，则

\[
 \boxed{H_n''=-\tfrac12\operatorname{tr}M
              -\tfrac12\mathbf1^TT\mathbf1
              -2\sum_{i<j}E r_{ij}.}                  \tag{10.1}
\]

因此 `1^T T 1≥0` 是一个不含对数的充分条件，并会给出显式负裕量。它尚未证明；T⪰0 是更强候选，不能从 M⪰0 或真实后验相容性直接推出。和最终 sine 目标之间这里只证明充分方向，未证明等价性或严格强弱的完整分类。

### 两节点改进

在权重 (1−t)dt 下，节点 0、1/2 的权重 1/6、1/3 对二次多项式精确。对 S(t)=h²/(v−ht)，取在 0 插值、在 1/2 匹配函数和一阶导数的二次多项式 P_2。精确余项为

\[
 S(t)-P_2(t)=
 \frac{h^5t(t-1/2)^2}{v(v-h/2)^2(v-ht)}\ge0.
\]

因此

\[
 g(P)\le-\tfrac16 E S(0)-\tfrac13 E S(1/2),
\]

相对只保留 S(0)/2 的上界，每条边在完整 Hessian 中额外保留的非负信用为

\[
 \frac13 E\frac{h^3}{v(v-h/2)}\ge0.
\]

无需再次收取端点 Fisher。这里没有宣称上述新有理势已经具有与 (6.1) 相同的观察域常数；要把此改进放入 (8.3)，须另行控制其 Hessian。

### 单调分辨率层级

对分割 pi:0=t_0<…<t_m=1，权重 omega_k=∫_{t_k}^{t_{k+1}}(1−t)dt，定义完整窗口上界

\[
 U_\pi=-F_V-2\sum_{i<j}\sum_k\omega_k E S_{ij}(t_k).
\]

由 S'≥0，细化分割时 U_pi 单调下降，且 U_pi≥H_n''。

还可证明 `S'(t)≤κ² h`。异号情形由第6节；同号 word 11 用条件核 C 的谱区间 [a,a+c] 及 `s/det C≤c²/[4a(a+c)]`，word 00 对孔核同理。于是

\[
 \boxed{0\le U_\pi-H_n''
 \le\frac{\kappa^2\|\pi\|}{2}(J_V-F_V).}             \tag{10.2}
\]

该误差没有 n² 或边度数因子。平衡点下每站点误差至多

\[
 \frac{\kappa^2c^2}{2\beta}\|\pi\|.
\]

种子常数为 `94091762/59319≈1586.19939648`。这给出有限窗口内的可递进有理曲率证书，不自动降低对全部真实 word 的求和复杂度。对固定有限窗口，层级收敛是已证；对更高层级的统一观察域变更常数，本稿未完成。

## 11. 两个明确失败机制

### 11.1 后验逐行能量不能按单位预算直接支付

曾尝试对两点表要求

\[
 2g(P)\le E_b |R_{ij}|^2
 \left[\frac{G_{ii}^2}{R_{ii}(1-R_{ii})}
       +\frac{G_{jj}^2}{R_{jj}(1-R_{jj})}\right].        \tag{11.1}
\]

如果成立，正收缩 R 的行能量 `Σ_{j≠i}|R_ij|²≤R_ii(1−R_ii)` 就能支付任意度数。这是一个真正有吸引力的候选，但它是假的。

在与种子相同的通道 a=1/40,c=19/20 下，取严格两点条件核

\[
 C=\begin{pmatrix}1/20&\sqrt2/20\\\sqrt2/20&19/20\end{pmatrix}.
\]

其特征值 `1/2±sqrt(83)/20` 严格位于 (1/40,39/40)，故 `(C-aI)/c` 是合法严格潜在核。四原子为 (17,3,363,17)/400。

实际后验给出的 (11.1) 右端精确为

\[
 3044288/4362897.
\]

而

\[
 2g(P)=2\log(1089/289)-4(2/17+1/3+1/363)
\]

严格更大。用 z=400/689 和 `log(1089/289)>2Σ_{k=0}^7 z^{2k+1}/(2k+1)` 即得正有理下界；不是浮点反例。

这是一般严格 DPP 的反例，不是实际 sine 条件表可实现性的证明。它否定一般逐行规则，未否定可能利用特殊 sine 相容性的平均规则。

后验计算中零输出的常数项必须为负：平衡通道

\[
 R=\operatorname{diag}((1-a)/c\text{ if }Y_i=1;
                       -a/c\text{ if }Y_i=0)
      -(\beta/c)J G J.
\]

### 11.2 原始矩阵势不是凸的；共同鞅并不自动给出支付

令

\[
 G_*=\begin{pmatrix}2&-4\\-4&-2\end{pmatrix},\quad
 V=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

有

\[
 \mathfrak T(G_*)=-120,\qquad
 \left.\frac{d^2}{dt^2}\mathfrak T(G_*+tV)\right|_{t=0}=-156,
 \qquad\|V\|_{HS}^2=4.
\]

这可由实际三点 DPP 揭示实现。取 epsilon=1/100，

\[
 K_3=\begin{pmatrix}
 1/10&-1/5&-1/1000\\
 -1/5&9/10&-3/1000\\
 -1/1000&-3/1000&1/2
 \end{pmatrix}.
\]

`K_3-aI` 与 `(a+c)I-K_3` 的所有顺序主子式严格正，因而仍在相同严格通道中。给定 `(Y_1,Y_2)=(1,0)`，粗逆矩阵为 G_*，揭示 Y_3 后主块为

\[
 G_*+epsilon^2\zeta V,\quad
 u=P(Y_3=1\mid Y_1=1,Y_2=0)=12501/25000,
\]

其中 ζ=1/u 或 −1/(1−u)，按真实概率 u、1−u。矩阵平均确实等于 G_*；但

\[
 E\mathfrak T(G_{\mathrm{fine}})-\mathfrak T(G_*)<0.
\]

短脚本精确确认其为负，并确认负增量与矩阵二次变差之比大于 19。epsilon→0 时这一比值趋于 39/2。因此要求单位 Fisher 增益支付该原始势变化的一般规则不成立。第6节必须加入明确的二次凸化，而不能把“矩阵鞅”误当成“任意矩阵势都满足 Jensen”。

这同样不是 sine 特定平均补偿的反例。

这个失败不完全是舍弃积分余量造成的。对同一两点矩阵路径，保留全部对数积分的势为

\[
 \mathfrak T_{\rm exact}(G_*+tV)
 =2t^2+8+4\left[(t-4)^2+(8t-20)
       \log\frac{8t-20}{t^2-4}\right].
\]

其二阶导数为

\[
 \frac{4(6t^5-31t^4-48t^3+576t^2-1184t+816)}
 {(t-2)^2(t+2)^2(2t-5)}.
\]

在 |t|≤1/100 上，分子为正、分母为负，所以该势严格凹；上述两个实际揭示增量均落在此区间。在 t=0，二阶导数为 −204/5。故完整对数势也不满足该条件 word 下的 Jensen，其局部统一二次支付系数至少为 51/10，而不是 1。它仍不排除在不同核心 word 之间转移预算、或利用 sine 特有相容性闭合。

## 12. 未付义务与计算交接

已完成的用途：式(6.5)是真实共同条件域上的、没有度数因子的整块补偿估计；式(8.1)/(8.3)把它嵌入完整 H_n''，并明确全部观察与分块边界；式(9.2)提供无未知符号前提的全体积曲率区域。旧工具只支付度数≤2子图，本稿没有这一限制。

尚未完成的关键义务：证明种子处某一有限 m,L 的 `U_mL` 连同 (8.3) 的全部正误差严格为负，或直接证明 (10.1) 中足够的矩阵平均正性，或用更高有理层级的非负信用闭合。三者均未被藏作已知前提。

计算交接只需辨别以下精确对象：

1. 固定种子或明确紧参数盒，对实际窗口核 K_A 和真实原子，认证 (8.2) 的有理期望，以及 (10.1) 的 `1^T T 1`。所有 word 按 p_Y 加权；不能均匀平均。
2. 区分原始零层、两节点层及分割层的上界是否仍有负裕量。若零层为正而更高层为负，说明主要损失是舍弃积分余量，而非空间误差。
3. 严格区间端点全负才证明该有限证书；跨零记未定。有限窗口正性样本不证明所有 n；一般严格 DPP 的反例不证明 sine 可实现性。
4. 不实现密集扫描、长优化或大规模枚举。当前脚本只做恒等式、两点有理反例和一个三点真实揭示检查。

## 参考来源

[R1] P. Caputo, P. Dai Pra, G. Posta. *Convex Entropy Decay via the Bochner–Bakry–Emery approach*. arXiv:0712.2578.

[R2] C. Li, S. Sra, S. Jegelka. *Gauss quadrature for matrix inverse forms with applications*. arXiv:1512.01904.

[R3] J. Hermon, J. Salez. *Modified log-Sobolev inequalities for strong-Rayleigh measures*. arXiv:1902.02775.

[R4] E. Hillion. *Entropy along W_{1,+}-geodesics on graphs*. arXiv:1406.5089.

[R5] E. Hillion, O. Johnson. *Discrete versions of the transport equation and the Shepp–Olkin conjecture*. arXiv:1303.3381. 另核对其后续完整 Shepp–Olkin 证明所处理的是 Bernoulli 和的计数分布。

输入来源：仓库 randomcat4/dpp-stationary-entropy，PR118 指定分支中的 TASK_02_LOCAL_SIGNED_COMPENSATION.md、S7_PROOF.md、S7_LOCALIZATION.md、S7_ONE_SIDED.md。本稿所有新不等式的证明均在正文给出；参考文献不替代这些证明。
