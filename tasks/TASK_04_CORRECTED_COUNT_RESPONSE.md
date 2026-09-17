# 独立任务04：S13 修正律的移动计数响应

你研究一个已经完全定义的修正模型中的 W 项。不要等待其它任务，不要假设此模型等于真实 DPP 输出，也不承担最终熵凹性证明。

## 完整定义

固定 `c=19/20`，`n=2k>=4` 为偶数，`a_*=(1-c)/2=1/40`。
在 n 个循环站点上，`P=UU*`，`U_(j,r)=n^(-1/2)exp(2 pi i j r/n)`，`0<=j<n,0<=r<k`。
输入 k 元子集 A 的概率是 `nu(A)=det P_A`。对每个 l 层，`u_l(S)=1/binom(n,l)`。

定义最大重叠转移 `T_l^max(S|A)`：若 l<=k，则在 A 的 l 子集中均匀选 S；若 l>=k，则在包含 A 的 l 子集中均匀选 S。令
`q_l^max(S)=sum_A nu(A)T_l^max(S|A)`，`r_l^max=q_l^max/u_l`。

对 `1<=l<=n-1`，总速率为1的 Bernoulli–Laplace 生成元为

\[
(L_l f)(S)=\frac1{l(n-l)}\sum_{i\in S,j\notin S}[f(S-i+j)-f(S)].
\]

对 `2<=l<=n-2` 设 `m=min(l,n-l)`，

\[
z(a,c)=\frac{(a+c)(1-a)}{a(1-a-c)},\quad
Z_{n,m}(z)=\sum_j\binom kj\binom k{m-j}z^j,\quad
\alpha_{n,m}=\frac{m(m-1)}{k(k-1)},
\]
\[
\theta_{n,l}(z)=\frac{(z-1)^2\sum_j\binom{k-2}j\binom{k-2}{m-2-j}z^j}
{\alpha_{n,m}Z_{n,m}(z)},\qquad
\gamma_{2,l}=\frac{2(n-1)}{l(n-l)}.
\]

超出范围的二项式系数为0。已知严格合法 a 区间上 `0<theta<1`。定义

\[
\widehat\tau_l(a)=-\log\theta_{n,l}(z(a,c))/\gamma_{2,l},\quad
\widehat q_{l,a}(S)=u_l(S)[e^{\widehat\tau_l(a)L_l}r_l^{max}](https://github.com/randomcat4/dpp-stationary-entropy/blob/2966743a11041ec8c2adef07ff6cb1f90b7d25da/research_prompts/pro_tasks/S).
\]

在 `l=0,1,n-1,n` 约定 `qhat_l=u_l`。这是正概率律。
只匹配指定 degree-two 势的均值，未证明所有模式共用此钟或 qhat 等于真实条件输出。

实际输出计数权重由

\[
\sum_l\pi_l(a,c)t^l=[1-a-c+(a+c)t]^k[1-a+at]^k
\]

定义。全部对数自然底。令

\[
K_l(t)=D(u_le^{tL_l}r_l^{max}\Vert u_l),\quad
h_n(l)=K_l(\widehat\tau_l(a_*)),\quad
W_n=\sum_l\pi_l''(a_*,c)h_n(l).
\]

**h_n 在 W 中冻结于 a_*；W 仅是移动权重项，不是完整二阶导数。**

## 已付输入

`Khat_n(a)=sum_l pi_l(a)K_l(tauhat_l(a))` 满足

\[
\widehat K_n''(a_*)=W_n+C_n,\quad
C_n=\sum_l\pi_l[-\widehat\tau_l'']\mathcal I_l,
\quad\mathcal I_l=-K_l'(\widehat\tau_l)\ge0.
\]

中点 `tauhat_l'=0`。已审结论只有

\[
\liminf_{n\to\infty,\ n\ even}C_n/n\ge\frac{2D_{pair}(c)}{1-c^2}>0,
\]

其中 `p_±=1/4±c²/pi²`，`D_pair=2[p_-log(4p_-)+p_+log(4p_+)]`。
这**不是**已证 `C_n=Theta(n)` 上下界，不能未经上界就断言某个 W 的增长必压倒 C。

给出可直接使用的计数运输：取 k 个 `Ber(a_*+c)` 与 k 个 `Ber(a_*)` 独立谱计数位；删去 i,j 后的和为 N_ij。则

\[
W_n=\sum_{i\ne j}E\Delta^2h_n(N_{ij})
=\sum_{m=0}^{n-2}B_m\Delta^2h_n(m),\quad
B_m=\sum_{i\ne j}P(N_{ij}=m),\quad\sum_mB_m=n(n-1).
\]

`Delta²h(m)=h(m+2)-2h(m+1)+h(m)`。证明是计数生成多项式逐因子两次微分；这部分不用重做，也不算新的成果。

## 你的创造性问题

利用最大重叠初值、层间删除/增加关系与实际层 clock，证明一个此前未给定的 **h_n 层间正则性或实际 B_m 加权估计**，或给出否定一个明确此类规则的反例。优先研究中央 `|m-k|=O(sqrt(n))` 的离散曲率，再清楚标出尾部还需什么。

可探索 `W_n` 的真实符号和尺度，包括 O(n)、n log n、n^(3/2) 或其它尺度，但不预设其中任何一种。已有小 n 的负值是探索证据，不能把拟合当成已知 cusp。若选择层间 intertwining，必须核对相邻层时钟比较方向。

独立有效成果可以是：明确中央窗口上的新局部定理；一个完整加权估计；一个成长族尺度障碍；或精确反例否定某个全 n 的层间比较规则。无需达到 `W+C>=0` 才算进展。只证某一中央层的符号，不能说已经支付整个 W。

## 快速判伪与边界

- 先对最小可算的 n=4、6 或8，比较 `sum pi''h` 与有序删除对表达式；最多先做两个规模，避免枚举本身吃掉研究任务。
- 端层 `h_n(0)=h_n(n)=0` 且 h>=0，所以除非全零，不能有全域 `Delta²h>=0`。
- 一个通用警报：四计数位成功率 `(3/4,3/4,1/4,1/4)`，数组 `h=(0,1,3,1,0)`，则 `pi''=(11/4,1,-15/2,1,11/4)`，`sum pi''h=-41/2`。这是代数测试数组，不是断言实际 h_n 长这样。
- 有限反例可以否定“所有 n”命题；不能仅凭一个有限值否定渐近 o(n)。

输出 `PROVED / DISPROVED / INCOMPLETE`、新命题与量词、完整推导或合法反例、对 W 的确切影响、剩余尾部/clock/尺度义务。写明 `CORRECTED_LAW_ONLY`；真实输出比较及循环到 Toeplitz 传递均不属于已经完成的成果。

不设固定时长、候选数或失败数；不运行哈希、不要求 PR/ZIP。工具不可用也交付正文，工具失败与数学状态分别报告。需要背景时可读附件 `../results/S13/PROOF.md`、`S13_TERM_BALANCE.md`、`S13_AUDIT.md`；未审核的旧渐近猜测不作为前提。
