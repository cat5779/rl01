# 附录 B：完整 remainder、二阶量传递与增长窗口

本附录独立给出主报告第 5、8 节的定量证明。所有 \(\ell^1\) 距离均为 \(\sum_y|P(y)-Q(y)|\)，即通常 total variation 的两倍。所有对数均为自然对数。

## B1. Full-support 展开的显式 remainder

### B1.1 条件概率地板与各阶系数的 majorant

令 \(P>0\) 为 n 位概率律，

\[
 \beta=\min_{i,z}\min\{P(X_i=0\mid X_{-i}=z),P(X_i=1\mid X_{-i}=z)\}.
\]

必有 \(0<\beta\le1/2\)。给定更少坐标的单点后验，是给定全部外部坐标后验的条件期望，因此同样处于 \([\beta,1-\beta]\)。逐点揭示任意集合 A 可得

\[
 P(y_A\mid y_{A^c})\ge\beta^{|A|}.
 \tag{B1}
\]

记 \(T_A^pP(y)=P(y_{A^c})\prod_{i\in A}r_p(y_i)\)。对 \(r=0,1,2\)，其中 \((k)_r=k(k-1)\cdots(k-r+1)\)，

\[
 \left|\partial_p^r\frac{T_A^pP(y)}{P(y)}\right|
 \le(|A|)_r\beta^{-|A|}.
 \tag{B2}
\]

令 \(M_i=T_i^p-I\)，\(M_A=\prod_{i\in A}M_i\)，各坐标算子相互可交换。由 inclusion–exclusion，若 \(|A|=k\)，

\[
 \left|\partial_p^r\frac{M_AP(y)}{P(y)}\right|
 \le\sum_{B\subseteq A}(|B|)_r\beta^{-|B|}
 =(k)_r\beta^{-r}(1+\beta^{-1})^{k-r}
 \le(k)_r(1+\beta^{-1})^k.
 \tag{B3}
\]

设

\[
 \frac{Q_{\varepsilon,p}}P=1+u,\qquad
 u=\sum_{k=1}^n\varepsilon^k u_k,
 \quad u_k=P^{-1}\sum_{|A|=k}M_AP,
 \quad T=n\varepsilon(1+\beta^{-1}).
\]

于是逐原子有

\[
 |\partial_p^r u_k|\le(k)_r\binom nk(1+\beta^{-1})^k.
 \tag{B4}
\]

以下记 \(v_1=\varepsilon u_1\)、\(v_2=\varepsilon^2u_2\)。由 \(\binom nk\le n^k/k!\)，当 \(T\le1/4\) 时，

\[
 \begin{gathered}
 |u|\le Te^T=:s<1,\qquad |u_p|\le Te^T,\qquad |u_{pp}|\le T^2e^T,\\
 |u-v_1|\le\tfrac12T^2e^T,\qquad
 |u_p-(v_1)_p|\le T^2e^T,\qquad
 |u_{pp}-(v_2)_{pp}|\le T^3e^T,\qquad
 |(v_1)_p|\le T.
 \end{gathered}
 \tag{B5}
\]

这些是所有原子上的界，但只用在已明确给出谱隙损失的 remainder 证明；它们不用于声称 pair 的点态符号。

### B1.2 曲率 remainder

令

\[
 g(u)=(1+u)\log(1+u)-u-u^2/2.
\]

因为 \(\mathbb E_Pu=0\)，

\[
 H(Q)=H(P)-\mathbb E_P[u\log P]-\tfrac12\mathbb E_Pu^2-\mathbb E_Pg(u).
 \tag{B6}
\]

一次系数 \(u_1\) 对 p 仿射，因此其二阶导数为零。二阶熵曲率主项为

\[
 -\mathbb E_P[(v_2)_{pp}\log P]-\mathbb E_P[(v_1)_p^2]
 =\varepsilon^2\mathcal L_n(P).
\]

剩余三部分分别满足：

\[
 |\mathbb E_P[(u_{pp}-(v_2)_{pp})\log P]|
 \le T^3e^T H(P);
 \tag{B7}
\]

\[
 |u_p^2+uu_{pp}-(v_1)_p^2|
 \le T^3(2e^{2T}+e^T);
 \tag{B8}
\]

以及，由

\[
 g'(u)=\log(1+u)-u,\qquad g''(u)=-u/(1+u),
\]

\[
 |g'(u)|\le\frac{s^2}{2(1-s)},\qquad
 |g''(u)|\le\frac{s}{1-s},
\]

得到

\[
 |\partial_p^2g(u)|\le
 T^3\frac{e^{3T}(1+T/2)}{1-Te^T}.
 \tag{B9}
\]

在 \(0\le T\le1/4\)，\(e^T<2\)，且 (B8)、(B9) 括号之和小于 10。可以用 \(e^{1/4}<9/7\) 等有理上界直接验证，也可保留更精确的显式函数。于是

\[
 \boxed{|H_{pp}-\varepsilon^2\mathcal L_n(P)|
 \le(2H(P)+10)T^3.}
 \tag{B10}
\]

由主报告的精确熵—互信息恒等式，此式就是 \(|\mathcal R_{n,3}''|\) 的界。虽然 \(I_{pp}\) 与 \(D_i''\) 单独在 p 的边界有奇异性，它们在 remainder 中的相消是精确代数事实；(B6) 给出 remainder 曲率到 \([0,1]\) 的连续延拓。

### B1.3 互信息值 remainder

令 \(L=\log(1/\beta)\)。由 (B1) 和 KL 的实际条件式，

\[
 0\le D_A\le |A|L.
\]

\(U(\varepsilon)=\sum_Aw_AD_A\) 的 k 次系数是对 D 的 k 阶 Möbius 差分之和，故其绝对值不超过

\[
 \binom nk k2^{k-1}L.
\]

因此 k≥3 的尾项不超过

\[
 \frac L2\sum_{k\ge3}\frac{k(2n\varepsilon)^k}{k!}
 \le2(n\varepsilon)^3e^{2n\varepsilon}L\le4LT^3.
 \tag{B11}
\]

这里 \(1+\beta^{-1}\ge3\)，所以 \(2n\varepsilon\le1/6\)。

另一方面，

\[
 D(Q\Vert P)=\tfrac12\mathbb E_Pu^2+\mathbb E_Pg(u).
\]

由 (B5)，\(\tfrac12|u^2-v_1^2|\le\tfrac14T^3e^T(e^T+1)\)。又因 \(g'''(u)=-(1+u)^{-2}\)，

\[
 |g(u)|\le\frac{|u|^3}{6(1-s)^2}.
\]

这两项在 \(T\le1/4\) 的总和小于 \(4T^3\)。结合 (B11)，证明

\[
 \boxed{|\mathcal R_{n,3}|\le(4L+4)T^3.}
 \tag{B12}
\]

### B1.4 第三阶系数的核对

写 \(Q=P+\varepsilon v+\varepsilon^2w+\varepsilon^3t+\cdots\)。熵的三阶系数是

\[
 -\sum_y t\log P-\sum_y\frac{vw}{P}+\frac16\sum_y\frac{v^3}{P^2}.
\]

v 对 p 仿射，w 至多二次，t 至多三次；两次求导即得主报告式 (5.2)。KL 混合中三缺陷 inclusion–exclusion 再减去上述归一化 KL 项，给出式 (5.1)。这里的“第三阶”按 \(\varepsilon\) 次数计，不按互异坐标的数目计。

---

## B2. 真实权重下的二阶量连续性

### B2.1 概率律到实际条件表的 Lipschitz 界

对正二元表全局质量 \((a,b,c,d)\)，其中顺序是 \((00,10,01,11)\)，置

\[
 m=a+b+c+d,\quad\Delta=bc-ad,
\]

\[
 G(a,b,c,d)=m\log\frac{bc}{ad}
 -\Delta\left(\frac1a+\frac1b+\frac1c+\frac1d\right).
 \tag{B13}
\]

自然 pair 曲率为 \(2\sum_zG(t_z)\)。若每个 cell 至少是 \(\alpha m\)，则

\[
 |\partial_a G|,\ldots,|\partial_dG|
 \le L_G(\alpha):=2\log(1/\alpha)+5/\alpha+1/(4\alpha^2).
 \tag{B14}
\]

证明：log-odds 的绝对值不超过 \(2\log(1/\alpha)\)；对数本身求导支付 \(1/\alpha\)；\(\partial\Delta\) 的绝对值不超过 m，支付 \(4/\alpha\)；最后 \(|\Delta|\le m^2/4\)，支付 \(1/(4\alpha^2)\)。这是对全部四个坐标的统一界。

单点对角贡献的全局函数是

\[
 F(a,b)=(a+b)^2(1/a+1/b).
\]

若 \(a,b\ge\delta(a+b)\)，则

\[
 |\partial_aF|,|\partial_bF|\le L_D(\delta):=4/\delta+1/\delta^2.
 \tag{B15}
\]

这些“cell ≥ 固定比例 × 总质量”的约束构成凸锥；因此两个真实概率表间的线段也在同一个锥内。对每个外部输出 z 使用中值定理，再对 z 求和。每次四元分组只是重新排列全体原子，并没有额外 TV 损失。若两个 n 位律的 full single-site 条件概率均处于 \([\delta,1-\delta]\)，则 pair cell 至少为 \(\delta^2\)，所以

\[
 \boxed{
 \left|\frac{\mathcal L_n(P)-\mathcal L_n(Q)}n\right|
 \le[L_D(\delta)+(n-1)L_G(\delta^2)]\|P-Q\|_1.
 }
 \tag{B16}
\]

n−1 的系数包括无序 pair 的数目和 pair 曲率中的因子 2。

### B2.2 核误差如何传到实际概率误差

假设 \(K,L\) 为 n 阶 Hermitian 核，并有共同谱隙 \(\delta\)：

\[
 \delta I\le K,L\le(1-\delta)I.
\]

令 \(K_t=K+tA\)、\(A=L-K\)、\(0\le t\le1\)。对完整原子 y，

\[
 q_t(y)=(-1)^{n-|y|}\det(K_t-D_y),\quad D_y=\operatorname{diag}(1-y),\quad B_y=(K_t-D_y)^{-1}.
\]

写 \(K_t-D_y=S_y/2+(K_t-I/2)\)，其中 \(S_y\) 是对角 ±1 矩阵。三角不等式给出最小奇异值至少 \(\delta\)，故

\[
 \|B_y\|\le\delta^{-1}.
 \tag{B17}
\]

所有 q_t 均全正。其 score 是 \(\operatorname{Tr}(B_yA)\)。对归一化恒等式两次求导，得到

\[
 \mathcal F_t:=\mathbb E_t[\operatorname{Tr}(B_YA)]^2
 =\mathbb E_t\operatorname{Tr}(B_YAB_YA)
 \le\delta^{-2}\|A\|_F^2.
 \tag{B18}
\]

最后一步使用 \(|\operatorname{Tr}C^2|\le\|C\|_F^2\)；不要求逐原子的 \(\operatorname{Tr}(BABA)\) 有正号。由 Cauchy–Schwarz，

\[
 \sum_y|q_t'(y)|\le\sqrt{\mathcal F_t}.
\]

沿 t 积分得真正的 law-level 界

\[
 \boxed{\|P_K-P_L\|_1\le\min\{2,\delta^{-1}\|K-L\|_F\}.}
 \tag{B19}
\]

此外，沿单个对角条目求导，cofactor/原子比是 \(1/\pi_i\) 或 \(-1/(1-\pi_i)\)，也就是 \((B_y)_{ii}\)。结合 (B17)，所有 full single-site 后验均在 \([\delta,1-\delta]\)。因此 (B16) 的假设已经由核谱隙支付。

### B2.3 最终传递式与截断距离版本

结合 (B16)、(B19)，

\[
 \left|\frac{\mathcal L_n(K)-\mathcal L_n(L)}n\right|
 \le[L_D(\delta)+(n-1)L_G(\delta^2)]
 \min\{2,\delta^{-1}\|K-L\|_F\}.
 \tag{B20}
\]

当 \(0<\delta\le1/2\)，

\[
 L_D(\delta)\le3\delta^{-2},\qquad
 L_G(\delta^2)\le2\delta^{-4},
\]

所以

\[
 \boxed{|\mathcal L_n(K)/n-\mathcal L_n(L)/n|
 \le2n\delta^{-5}\|K-L\|_F.}
 \tag{B21}
\]

若只比较距离不超过 R 的自然异点和

\[
 S_{n,R}=\sum_{i<j,\,j-i\le R}\mathcal J_{ij}'',
\]

pair 数至多 nR，故

\[
 |S_{n,R}(K)/n-S_{n,R}(L)/n|
 \le4R\delta^{-5}\|K-L\|_F.
 \tag{B22}
\]

这并不控制未计入的距离尾；没有隐含一个统一可求和假设。

---

## B3. 一个自包含的有限 sine 谱隙下界

设 \(0<\rho<1\)、\(\tau=\min(\rho,1-\rho)\)。核 \(Q_{\rho,m}\) 是弧 \([-\pi\rho,\pi\rho]\) 上指数函数的 Gram 矩阵。对 \(\sum_{j=0}^{m-1}|c_j|^2=1\) 的多项式

\[
 f(e^{it})=\sum_{j=0}^{m-1}c_je^{ijt},
\]

\[
 c^*Q_{\rho,m}c=\frac1{2\pi}\int_{-\pi\rho}^{\pi\rho}|f(e^{it})|^2\,dt.
 \tag{B23}
\]

全圆 L2 范数为 1，故全圆 supremum 至少为 1。

令 d=m−1≥1。在长度为 \(\pi\tau\) 的内子弧上取 m 个等间隔插值节点 \(z_j\)。相邻角距 \(\pi\tau/d\)，且

\[
 |z_j-z_\ell|\ge2\tau|j-\ell|/d.
\]

Lagrange 插值在整个单位圆给出

\[
 \sup_{|z|=1}|f(z)|
 \le\max_j|f(z_j)|\sum_{j=0}^d
 \frac{(d/\tau)^d}{j!(d-j)!}
 \le(2e/\tau)^d\max_j|f(z_j)|.
 \tag{B24}
\]

这里使用 \(d!\ge(d/e)^d\)，可由 \(\log(d!)\ge\int_1^d\log x\,dx\) 证明。因此至少一个节点有

\[
 |f(z_j)|\ge M_0:=(\tau/(2e))^d.
\]

又由 Cauchy–Schwarz，\(|d f(e^{it})/dt|\le m^{3/2}\)。在这个节点两侧半径

\[
 h=M_0/(2m^{3/2})
\]

的角区间内，\(|f|\ge M_0/2\)。内子弧到全积分弧的边距至少 \(\pi\tau/2\)，而 h 更小，所以整个小区间都在积分弧内。于是

\[
 c^*Q_{\rho,m}c\ge\frac{M_0^3}{8\pi m^{3/2}}=:d_m.
 \tag{B25}
\]

对补弧旋转后应用同一证明，得到

\[
 \boxed{d_mI\le Q_{\rho,m}\le(1-d_m)I,
 \quad d_m=\frac{(\tau/(2e))^{3(m-1)}}{8\pi m^{3/2}}.}
 \tag{B26}
\]

m=1 时可直接取 \(d_1=\tau\)。本界只追求显式而不追求最优；它也独立证明每个有限 true Toeplitz 窗口全支撑。

---

## B4. 周期化核到二阶量，而不是只到熵值

### B4.1 核误差

N 周期、秩 k 的连续 Fourier 投影，在合法的对角相位变换后，其 m 点块核为

\[
 C_{rs}=\frac{\sin(\pi k(r-s)/N)}{N\sin(\pi(r-s)/N)},\quad r\ne s,
 \qquad C_{rr}=k/N.
\]

DPP 配置概率对这种 gauge 不变。取 m≤N/2，令 \(d=r-s\ne0\)、\(x=\pi|d|/N\le\pi/2\)。由

\[
 0\le x-\sin x\le x^3/6,\qquad \sin x\ge2x/\pi,
\]

得到

\[
 \left|\frac1{N\sin x}-\frac1{N x}\right|
 \le\frac{\pi^2|d|}{12N^2}.
\]

密度差产生的误差满足

\[
 \left|\frac{\sin(\pi(k/N)d)-\sin(\pi\rho d)}{\pi d}\right|
 \le|k/N-\rho|.
\]

逐条目再取 Frobenius 范数，

\[
 \boxed{\|C-Q_{\rho,m}\|_F\le
 m|k/N-\rho|+\pi^2m^2/(12N^2)=:e_{m,N}^{\rm bd}.}
 \tag{B27}
\]

### B4.2 无噪声但增长缓慢的边缘窗口

若 \(e_{m,N}^{\rm bd}\le d_m/2\)，Weyl/变分原理给 C 和 Q 的共同谱隙至少 \(d_m/2\)。将其代入 (B21)，

\[
 \boxed{|\mathcal L_m(C)/m-\mathcal L_m(Q_{\rho,m})/m|
 \le64m d_m^{-5}e_{m,N}^{\rm bd}.}
 \tag{B28}
\]

若 k/N=ρ，设 \(a_\rho=\log(2e/\tau)\)，m≤κ logN，则右端不超过常数乘

\[
 m^{21/2}e^{15a_\rho m}N^{-2}.
\]

因此 \(\kappa<2/(15a_\rho)\) 时趋零；谱隙条件本身也在足够大 N 后自动满足。k 只作最近整数匹配时，增加 \(O(m^{19/2}e^{15a_\rho m}/N)\)，取 \(\kappa<1/(15a_\rho)\) 即可。

这是边缘窗口之间的二阶量比较。C 所定义的律是先把循环模型的其他 N−m 个坐标**边缘化**，不是观察它们后再条件化。

### B4.3 有噪声时的多项式匹配窗口

这里还可以避免 (B26) 的指数谱隙损失。取 \(p\in[u,1-u]\)、\(0<u\le1/2\)，并给两个核施加相同噪声：

\[
 K_{\varepsilon,p}=(1-\varepsilon)Q_{\rho,m}+\varepsilon pI,
 \quad L_{\varepsilon,p}=(1-\varepsilon)C+\varepsilon pI.
\]

共同谱隙至少 \(\varepsilon u\)，所以对每个 \(\varepsilon>0\) 有

\[
 \boxed{\frac{|\mathcal L_m(K_{\varepsilon,p})-
 \mathcal L_m(L_{\varepsilon,p})|}{m}
 \le2m(\varepsilon u)^{-5}e_{m,N}^{\rm bd}.}
 \tag{B29}
\]

这个结论可以用于 m 随噪声增长。密度精确匹配时，若 \(m\le C/\varepsilon\)，右端为

\[
 O_{C,u}(\varepsilon^{-8}N^{-2}).
 \tag{B30}
\]

故选择 \(N\varepsilon^4\to\infty\) 就能在 **m 约为 \(1/\varepsilon\)** 的真实有限输出窗口上，把二阶 interaction 的周期化误差压到零。对原来 p 参数的熵曲率还多乘 \(\varepsilon^2\)，相应误差为 \(O(\varepsilon^{-6}N^{-2})\)。

这条多项式传递是真的，但只比较相同 m 点的两个边缘律。它既没有控制 m 窗口到全外部条件表的误差，也不能将完整 N 点循环投影的端点留数直接转移过来，因为此时 N 远大于 m。这两个未支付的操作必须继续区分。

---

## B5. 真实 sine 稀疏展开的对数增长窗口

令 \(P_n=\operatorname{DPP}(Q_{\rho,n})\)。由 (B17) 的 cofactor 论证和 (B26)，\(\beta_n\ge d_n\)。当 \(n\le\kappa\log(1/\varepsilon)\)、\(\kappa<1/(9a_\rho)\) 时，

\[
 T_n=n\varepsilon(1+\beta_n^{-1})
 \le2n\varepsilon d_n^{-1}
 =O_\rho(n^{5/2}\varepsilon e^{3a_\rho n})\to0.
\]

所以 (B10) 在足够小 \(\varepsilon\) 后适用。再除以 \(n\varepsilon^2\)，并用 \(H(P_n)\le n\log2\)，

\[
 \sup_{p\in[0,1]}\left|\frac{H_{pp}}{n\varepsilon^2}-\frac{\mathcal L_n(P_n)}n\right|
 \le C_\rho n^{15/2}\varepsilon e^{9a_\rho n}
 \le C_{\rho,\kappa}\varepsilon^{1-9a_\rho\kappa}(1+\log(1/\varepsilon))^{15/2}.
 \tag{B31}
\]

这是一个有明确量词的增长窗口定理。它证明“先固定 n”可以稍微放宽到指定的对数窗口；它没有证明 \(\mathcal L_n/n\) 本身可求和、可积或收敛，更没有将 (B31) 放宽至 \(n\asymp1/\varepsilon\)。
