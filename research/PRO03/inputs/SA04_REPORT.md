> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA04：时钟修正的跨层热桥与完整计数响应界

**CORRECTED_LAW_ONLY**  
**PROVED_SCOPED / INCOMPLETE_SHARP_SCALE_AND_SIGN**

## 0. 模型、冻结约定和结论

只研究任务指定的修正律。固定
\[
c=19/20,\quad p=39/40,\quad q=1/40,\quad b=pq=39/1600,
\quad z=(p/q)^2=1521,\quad n=2k\ge4.
\]
站点为循环上的 n 个点。令 P 为前 k 个离散 Fourier 列生成的正交投影，
输入 k 元集的概率为 \(\nu(A)=\det P_A\)。令 \(u_l\) 为 l 层均匀律。
\(q_l^{\max}\) 在 l<=k 时先抽 A 再均匀抽其 l 元子集；在 l>=k 时均匀补点到 l 元集。

任务的总速率一 Bernoulli–Laplace 生成元为
\[
 L_l f(S)=\frac1{l(n-l)}\sum_{i\in S,j\notin S}[f(S-i+j)-f(S)].
\]
对 2<=l<=n-2，令 m=min(l,n-l)，
\[
 Z_m(z)=[t^m](1+t)^k(1+zt)^k,\qquad
 a_j=[t^j](1+t)^{k-2}(1+zt)^{k-2},
\]
\[
 \alpha_{n,m}=\frac{m(m-1)}{k(k-1)},\qquad
 \theta_m=\frac{(z-1)^2a_{m-2}}{\alpha_{n,m}Z_m(z)}.
\]
只在这里定义的修正模型内使用这些乘子。记
\[
 G_l=l(n-l)L_l,\quad P_l^s=e^{sG_l},\quad
 s_l=\frac{\widehat\tau_l}{l(n-l)}
     =-\frac{\log\theta_{\min(l,n-l)}}{2(n-1)},
\]
\[
 \mu_l(s)=q_l^{\max}P_l^s,\qquad
 F_l(s)=D(\mu_l(s)\Vert u_l),\qquad h(l)=F_l(s_l).
\]
在端层 0,1,n-1,n 仍采用任务的均匀律约定，不为端层虚构实际修正时钟。
其中 \(F_1(s)=F_{n-1}(s)=0\) 对任意辅助热时间成立。
所有 h(l) 冻结于 a*=1/40。

实际计数权重为
\[
 \sum_l\pi_l(a,c)t^l=[1-a-c+(a+c)t]^k[1-a+at]^k,
\qquad W_n=\sum_l\pi_l''(a_*,c)h(l).
\]
使用任务已给出的恒等式
\[
 W_n=\sum_{m=0}^{n-2}B_m\Delta^2h(m),\qquad
 \sum_m B_m=n(n-1).
\]
本报告不将该已给定恒等式重新计为成果。

### 主定理（本报告证明的量词）

对上述指定修正律的每个偶数 n>=4：

**(i) 实际时钟的比较。** 对 3<=l<=k，
\[
 0<s_l-s_{l-1}\le
 \frac{\log(l/(l-2))}{2(n-1)}.                 \tag{T1}
\]

**(ii) 精确跨层运输。** 每对相邻修正层存在明确的 Markov 核及耦合，
两端边缘恰为相应修正律，且
\[
 \mathbb E|S\triangle T|\le1+2\log3.          \tag{T2}
\]
这只是一个构造性上界，不宣称该耦合最优。

**(iii) 全层熵差。** 定义
\[
 \beta_*=2\log(761/760),
\quad A_*=\log\frac{24}{1-e^{-3\beta_*/8}},
\quad E_*=\frac{2\log2\log3}{\beta_*}.
                                                        \tag{T3}
\]
对 1<=l<=k，
\[
 -E_*\le h(l)-h(l-1)\le A_*;
\quad A_*<11,\quad E_*<600.                \tag{T4}
\]
由粒子空穴对称，对所有 1<=l<=n 有
\[
 |h(l)-h(l-1)|<600.                         \tag{T5}
\]

**(iv) 完整带符号加权估计。** 记 \(B_*=B_{k-1}\)，则
\[
 -2A_* B_*\le W_n\le2E_* B_*,               \tag{T6}
\]
并且
\[
 B_*\le n(n-1)\min\left\{1,
 \frac{\sqrt\pi}{2\sqrt{2(n-2)b}}\right\}
 \le\frac{15\sqrt\pi}{\sqrt{39}}n^{3/2}.    \tag{T7}
\]
因此得到全 n 的 \(W_n=O(n^{3/2})\) 上界意义结论，所有层均已包括，
不是中央截断结论，没有被隐去的尾部。

这些上界不证明 \(W_n\) 的实际增长阶，也不证明其全 n 符号。
任务已付的 \(\liminf C_n/n>0\) 不含 C_n 的上界；本报告没有将其升级为 Theta(n)。
下文的逆向桥成本记为 \(\mathsf E_l\)，与任务的加速度项 \(C_n\) 完全不同。

## 1. 域外迁移方案与候选工具

### 1.1 源机制及条件

使用三个来自一般有限 Markov 链而非 DPP 专属结构的机制：

* 排列作用产生的同一原始交换半群，与等变删除核精确交换。
* 一维出生死亡核的 TP2 性保持似然比序；这里用于比较两个不同步数的反射随机游走。
* 对可逆热核作 Bayes 时间反演，把“需要逆向热流”的错误线性操作替换成一个依赖目标律的正 Markov 核。

此外，以 KL 的条件分解和凸性控制删除损失，而不是由 Wasserstein 距离直接控制熵。
本报告给出上述机制在所需有限模型中的证明，不借用未经检验的曲率定理。
不宣称机制或组合首次出现于文献。

### 1.2 对应与失效条件

源对象的共同生成元对应 \(G_l=l(n-l)L_l\)，而不是题面各层速率一的 \(L_l\)。
源对象的同一时间对应原始时间 s，而实际修正模型使用各自的 \(s_l\)。

同钟删除后再正向加热，只有当目标时钟不早于已到达时钟时才可行。
本题向外删除时恰好相反：\(s_l>s_{l-1}\)。所以单纯套用 intertwining 会把时钟方向写反。
逆向桥保持正性和目标边缘，但不保持均匀参考律。故不能再对该桥直接套用
“相对均匀律 KL 必收缩”的论证。

新增构件是：实际时钟双向比较、可量化的逆向桥、删除/桥成本分账，
以及使用实际 B 权重的正系数一阶差分证书。

## 2. P1：共同半群、删除关系与正确层权重

令
\[
 D_l(S,T)=\frac1l\mathbf1\{T\subset S,\ |T|=l-1\}.
\]
对 l<=k，均匀抽子集再均匀删一点仍是均匀抽较小子集，因此
\[
 q_l^{\max}D_l=q_{l-1}^{\max},\qquad u_lD_l=u_{l-1}.              \tag{2.1}
\]
对每个置换 sigma，删除与 sigma 等变。又
\[
 G_l=\sum_{i<j}(T_{ij}-I)
\]
作用在 l 元集函数上；两点同占据或同空缺的项自动为零。因此用同一随机置换实现热流，得
\[
 P_l^sD_l=D_lP_{l-1}^s.                                         \tag{2.2}
\]
于是
\[
 \widehat q_lD_l=\mu_{l-1}(s_l),                                \tag{2.3}
\]
并非未经修正的 \(\widehat q_{l-1}\)。

### 2.1 把跨层耦合提升到实际计数分布

第 4 节构造每条边的耦合 \(J_l(S,T)\)，其边缘分别为
\(\widehat q_l,\widehat q_{l+1}\)。设 \(\pi_l=\pi_l(a_*,c)>0\)，取
\[
 \kappa_l=\frac{\pi_l\pi_{l+1}}{\pi_l+\pi_{l+1}}.
\]
从 (l,S) 向 (l+1,T) 的速率设为
\[
 \frac{\kappa_l}{\pi_l}\frac{J_l(S,T)}{\widehat q_l(S)},
\]
反向速率设为
\[
 \frac{\kappa_l}{\pi_{l+1}}\frac{J_l(S,T)}{\widehat q_{l+1}(T)}.
\]
不存在的端边速率为零。每个条件核归一化；两方向的平衡流均为
\(\kappa_lJ_l(S,T)\)。因此这是以
\[
 \Pi(l,S)=\pi_l\widehat q_l(S)
\]
为可逆律的明确出生死亡层提升。它保留实际层权重，不用均匀层权重替代。
这是一件分析工具，不是对原通道动力学的认定。

## 3. P2：实际时钟的双向比较

### 3.1 靠近中央时原始钟严格变长

令 \(f(t)=(1+t)(1+zt)=1+(z+1)t+zt^2\)，\(a_j=[t^j]f^{k-2}\)。
对 2<=m<=k，直接对 \(f^k\) 求二阶导数，得到
\[
 \frac{(z-1)^2}{\theta_m}
 =(z+1)^2+\frac{2z}{k-1}
 +z(z+1)\left(4+\frac2{k-1}\right)\frac{a_{m-3}}{a_{m-2}}
 +z^2\left(4+\frac2{k-1}\right)\frac{a_{m-4}}{a_{m-2}}.           \tag{3.1}
\]
负下标系数置零。多项式 \(f^{k-2}\) 是正一次因子的乘积，其系数对数凹。
所用系数事实也可由二点对数凹序列的卷积保持对数凹归纳得到。
因此 \(a_{j-1}/a_j\) 和 \(a_{j-2}/a_j\) 随 j 增加，式 (3.1) 的右边随 m 增加。
在 3<=m<=k 时严格增加。这证明
\[
 \theta_m<\theta_{m-1},\qquad s_m>s_{m-1}.                      \tag{3.2}
\]
特别地
\[
 \theta_2=\frac{(z-1)^2}{(z+1)^2+2z/(k-1)}
 \le\left(\frac{z-1}{z+1}\right)^2,
\quad -\log\theta_m\ge\beta_* .                               \tag{3.3}
\]

### 3.2 反射出生死亡核给出相邻钟差的另一侧

设 \(\rho_j(r)\) 为 j 步对称随机游走的概率：一步为 -1,0,1，概率分别为
b,1-2b,b。系数换元给出精确关系
\[
 \theta_m=c^2\frac{k(k-1)}{m(m-1)}
             \frac{\rho_{k-2}(k-m)}{\rho_k(k-m)}.               \tag{3.4}
\]
例如此式来自
\(\pi_m=(pq)^k(q/p)^m Z_m(z)\)，并注意
\((z-1)^2q^4=c^2\)。

绝对值游走在非负整数上的转移核 Q 为
\[
 Q(0,0)=1-2b,\quad Q(0,1)=2b,
\]
\[
 Q(r,r-1)=b,\quad Q(r,r)=1-2b,\quad Q(r,r+1)=b\quad(r\ge1).
\]
Q 为 TP2：可能非平凡的相邻主二阶子式分别为
\((1-2b)^2-2b^2\) 和 \((1-2b)^2-b^2\)，均非负；其余需检查的子式直接非负。
这里使用 b<=1/4。TP2 核保持似然比序，因为输出的任意二阶差可展开为
\[
 \sum_{a<b}(\mu_a\nu_b-\mu_b\nu_a)
             (Q_{ai}Q_{bj}-Q_{aj}Q_{bi})\ge0\quad(i<j).        \tag{3.5}
\]
乘积核也保持该性质。

由 \(\delta_0\preceq_{lr}\delta_0Q^2\)，右乘 \(Q^{k-2}\) 得
\(\delta_0Q^{k-2}\preceq_{lr}\delta_0Q^k\)。正半轴概率仅比 rho 多同一个因子 2，
故 \(\rho_{k-2}(r)/\rho_k(r)\) 随 r 不增。将 r=k-m 代回 (3.4)，得到
\[
 \frac{m-2}{m}\le\frac{\theta_m}{\theta_{m-1}}\le1.             \tag{3.6}
\]
这证明 (T1)，并且没有假设层半群在各自实际钟上交换。

### 3.3 跳数尺度

对 r=l-1>=2，令 \(\delta_l=s_l-s_r\)。由 (3.6)，
\[
 r(n-r)\delta_l\le
 \frac{r(n-r)}{2(n-1)}\log\frac{r+1}{r-1}\le\log3.             \tag{3.7}
\]
最后一步用 \(r\log((r+1)/(r-1))\) 在 r>=2 上递减，最大值为 2 log3。
因而原始钟差虽然不能忽略，但只对应有界的平均实际交换次数。

## 4. P1–P2：逆向热桥、运输成本与边界

对 3<=l<=k，令 r=l-1，
\[
 q_r^*=\widehat q_r=\mu_r(s_r),\quad H_l=P_r^{\delta_l},\quad
 p_r^*=q_r^*H_l=\mu_r(s_l).
\]
定义 Bayes 逆向核
\[
 \mathcal R_l(y,x)=\frac{q_r^*(x)H_l(x,y)}{p_r^*(y)}.           \tag{4.1}
\]
正性保证分母非零。逐行求和为 1，且 \(p_r^*\mathcal R_l=q_r^*\)。因此
\[
 \mathcal T_l=D_l\mathcal R_l,\qquad
 \widehat q_l\mathcal T_l=\widehat q_{l-1}.                    \tag{4.2}
\]
这是正 Markov 核，而不是负时间算子 \(e^{-\delta_lG_r}\)。

在联合律
\(\widehat q_l(S)D_l(S,y)\mathcal R_l(y,x)\) 下，(x,y) 的边缘恰为
\(q_r^*(x)H_l(x,y)\)。把它补上正向热路径，实际交换次数的期望是
\(r(n-r)\delta_l\)。由于每次交换使对称差至多增加 2，删除产生对称差 1，
\[
 \mathbb E|S\triangle x|\le1+2r(n-r)\delta_l\le1+2\log3.
                                                                    \tag{4.3}
\]

### 4.1 精确桥成本

H_l 对均匀律可逆，即 H_l(x,y)=H_l(y,x)。所以
\[
 \mathbb E_{y\sim p_r^*}D(\mathcal R_l(y,\cdot)\Vert H_l(y,\cdot))
 =F_r(s_r)-F_r(s_l)=:\mathsf E_l\ge0.                          \tag{4.4}
\]
证明是将对数比写成 \(\log q_r^*(x)-\log p_r^*(y)\)，再求联合期望。
这给出了时钟误差的具体概率对象和精确成本，而非为未知余项换名。

### 4.2 删除成本与分账

由 (2.1) 的数据处理不等式，
\[
 \mathsf A_l=F_l(s_l)-F_r(s_l)\ge0.
\]
若给删除后的集合 T 补回一点，均匀参考条件律是 n-r 个候选点上的均匀律，故
\[
 \mathsf A_l=\mathbb E_T
 D(\text{实际补点条件律}\Vert\operatorname{Unif}(T^c)).         \tag{4.5}
\]
于是
\[
 d_l:=h(l)-h(l-1)=\mathsf A_l-\mathsf E_l.                      \tag{4.6}
\]
两个成本分别非负，差的符号没有被假定。

### 4.3 端层与粒子空穴

P 的对角元均为 1/2，故 \(q_1^{\max}=u_1\)，\(F_1(s)=0\)。
在 2->1 直接使用 D_2，设 \(\mathsf E_2=0\)、\(\mathsf A_2=h(2)\)；
1->0 直接删除，熵差为零。

此半密度 Fourier 投影满足 \(I-P=DPD^*\)，其中 \(D_{jj}=(-1)^j\)。
投影体积律的补集也是补投影体积律，因而 \(\nu(A^c)=\nu(A)\)。
也可直接用 Fourier Vandermonde 公式和
\(\prod_{j\ne i}|e^{2\pi i i/n}-e^{2\pi i j/n}|=n\) 验证两补集的概率相等。
因此
\[
 \widehat q_{n-l}(S^c)=\widehat q_l(S),\quad h(n-l)=h(l),
 \quad d_{n-l+1}=-d_l.                                        \tag{4.7}
\]
补集将下半区的耦合变为上半区耦合；需要反向边时取该联合律的条件分布。
归一、端层和 (4.3) 的成本均保留。

## 5. P3：删除收益的全层、无维数上界

这里不能从 (4.3) 的运输距离直接推出熵差。本节另行支付条件熵。

### 5.1 删除损失的凸性降低到固定初始集合

对任意层律 mu，令 \(J_\mu(S,T)=\mu(S)D_l(S,T)\)，
\(p_\mu=\mu D_l\)。删除损失等于
\(D(J_\mu\Vert p_\mu U_{\rm fill})\)。两个参数都线性依赖 mu，
由 KL 联合凸性，此损失是 mu 的凸函数。

所以，将 \(\widehat q_l\) 写成对 A 的混合后，只需控制固定 A 的
“均匀 l 子集再热化”律。固定 A 的上界与 A 的位置无关。

删除后的 r=l-1 元集 T 满足同钟关系，其分布是从 A 的均匀 r 子集出发的热流。
令 \(R=|T\cap A^c|\)，\(d=k-r\ge1\)。给定 T，实际补点概率在两组内分别均匀，
两组大小为
\[
 k-|T\cap A|=d+R,\qquad k-R.
\]
因此无论组间质量如何，条件 KL 至多
\[
 \log\frac{n-r}{\min(d+R,k-R)}.                               \tag{5.1}
\]

### 5.2 一个可核验的出生死亡比较

R 的原始时间生成元出生率、死亡率为
\[
 \lambda_R=(r-R)(k-R),\qquad \mu_R=R(k-r+R),                    \tag{5.2}
\]
初态 R=0。此链在反射 \(R\mapsto r-R\) 下对称。
任意同一连续时间出生死亡链可将两有序初态保持有序耦合：相遇后同步，
相遇前一步跳不能跨越。因此从 0 出发的 \(R_s\) 随机小于从 r 出发的链，后者
分布为 \(r-R_s\)。故
\[
 \mathbb E\frac1{k-R_s}\le\mathbb E\frac1{d+R_s}.              \tag{5.3}
\]

若 r<floor(k/2)，(5.1) 直接至多 log3。
否则令 \(h_0=\lfloor k/2\rfloor\)。比较链 J 的率为
\[
 \lambda_J(x)=(h_0-x)k/2,\qquad \mu_J(x)=kx.
\]
在相等状态 x<=h_0，真实出生率不小于比较链，真实死亡率不大于比较链。
所以 \(R_s\ge J_s\) 可有序耦合。比较链是 h_0 个独立二态链之和，
\[
 J_s\sim\operatorname{Bin}\left(h_0,\frac{1-e^{-3ks/2}}3\right).
\]
记其成功率为 v_s。利用 d>=1 和精确恒等式
\[
 \mathbb E\frac1{1+\operatorname{Bin}(h_0,v_s)}
 =\frac{1-(1-v_s)^{h_0+1}}{(h_0+1)v_s}
 \le\frac1{(h_0+1)v_s},                                      \tag{5.4}
\]
再用 (5.3)、log 的凹性、n-r<=2k 和 h_0+1>=k/2，得到
\[
 \mathsf A_l\le\log\frac{24}{1-e^{-3ks_l/2}}.
\]
由 (3.3)，\(3ks_l/2\ge3\beta_*/8\)，故
\[
 0\le\mathsf A_l\le A_* .                                   \tag{5.5}
\]
在 l=2，也可直接用下一节的初值界得到 \(h(2)\le2\log2<A_*\)。

常数不需拟合：\(\log(761/760)\ge1/761\)，故
\(1-e^{-3\beta_*/8}\ge3/3047\)，从而
\(A_*\le\log24376<11\)。

## 6. P3：逆向桥熵成本的全层界

### 6.1 所需的初始熵界

有限投影体积律的包含概率满足
\[
 \mathbb P(S\subset A)=\det P_S.
\]
可由 Cauchy–Binet 比较
\(\det(U^*\operatorname{diag}(1+t_i)U)\)
的多项式系数直接证明，不需额外概率假设。
因此
\[
 q_r^{\max}(S)=\frac{\det P_S}{\binom kr},\qquad
 r_r^{\max}(S)\le\frac{\binom{2k}r}{2^r\binom kr}.             \tag{6.1}
\]
这里仅使用 Hadamard 不等式及 \(P_{ii}=1/2\)。
又
\(\binom{2k}r/\binom kr\le4^r\)：乘积因子
\((2k-j)/(k-j)\) 随 j 增加，其前 r 项的平均对数不大于前 k 项；
后者的乘积为 \(\binom{2k}k\le4^k\)。所以
\[
 F_r(0)\le r\log2\quad(0\le r\le k).                         \tag{6.2}
\]

### 6.2 为什么可以用熵耗散随原始时间递减

写 \(\mathcal I_r^G(s)=-F_r'(s)\)。这不是任意 Markov 链都可不加说明使用的步骤。
本题 G 是所有换位之和，故热核与每个置换算子交换。
函数
\(\Psi(x,y)=(x-y)(\log x-\log y)\)
联合凸。对每一换位使用 Jensen，再对换位求和，得到
\[
 \mathcal I_r^G(P_r^t f)\le\mathcal I_r^G(f).
\]
其精确归一为
\[
 \mathcal I_r^G(f)=\frac12\sum_{i<j}
 \mathbb E_{u_r}\Psi(f(S),f((ij)S)).                           \tag{6.3}
\]
于是
\[
 s\mathcal I_r^G(s)\le\int_0^s\mathcal I_r^G(t)dt
 =F_r(0)-F_r(s)\le F_r(0).                                   \tag{6.4}
\]

### 6.3 支付实际钟差

对 l>=3、r=l-1，由 (3.6)、(6.2)–(6.4)，
\[
 \begin{aligned}
 \mathsf E_l
 &=\int_{s_r}^{s_l}\mathcal I_r^G(s)\,ds\\
 &\le\frac{s_l-s_r}{s_r}F_r(0)\\
 &\le\frac{r\log2\log((r+1)/(r-1))}{\beta_*}
 \le E_*.
 \end{aligned}                                               \tag{6.5}
\]
由 \(\beta_*\ge2/761\)、\(\log2<7/10\)、\(\log3<11/10\)，
\[
 E_*\le761\log2\log3<585.97<600.
\]
结合 (4.6)、(5.5) 和端层/补集处理，(T4)–(T5) 得证。

## 7. 实际 B 权重：正系数一阶差分证书

以下不再对已给定的 W 做逐项二阶差分绝对值估计；那样只能得到 O(n^2)。

### 7.1 B 的精确正系数分解

令
\[
 A(t)=q+pt,\quad C(t)=p+qt,\quad
 \phi(t)=A(t)C(t)=b+(1-2b)t+bt^2.
\]
按有序删除对属于高/低两组分类，得到
\[
 \sum_mB_mt^m
 =\phi(t)^{k-2}\{k(k-1)[A(t)^2+C(t)^2]+2k^2\phi(t)\}.
\]
令
\[
 \eta_k=\frac{k-1+2b}{2(2k-1)},\qquad
 \psi(t)=\eta_k+(1-2\eta_k)t+\eta_kt^2.
\]
则
\[
 \boxed{\quad\sum_m\frac{B_m}{n(n-1)}t^m
 =\phi(t)^{k-2}\psi(t).\quad}                                \tag{7.1}
\]
有 \(b\le\eta_k\le1/4\)。因此这些都是对称、中心概率至少 1/2 的三点分布。
它们的卷积对称且单峰，故
\[
 B_m=B_{n-2-m},\qquad B_0\le\cdots\le B_{k-1}.                \tag{7.2}
\]
单峰性也可由每个二次多项式具有负实根、其系数对数凹及卷积保持性得到。

设 \(B_{-1}=0\)，并定义
\[
 w_l=B_{l-1}-B_{l-2}\ge0\quad(1\le l\le k),
 \qquad\sum_{l=1}^k w_l=B_{k-1}.                              \tag{7.3}
\]
对已给定的 W 做一次离散分部求和，再用 (4.7)，精确得到
\[
 \boxed{\quad W_n=-2\sum_{l=1}^k w_l d_l
       =2\sum_{l=2}^k w_l(\mathsf E_l-\mathsf A_l).\quad}     \tag{7.4}
\]
这是实际计数权重下的带符号运输成本证书。所有系数 w_l 非负，
每个成本都有具体条件概率或桥的 KL 表示，并已有上界。
它不声称每个离散曲率或每个熵差有固定符号。
由 (5.5)、(6.5)，立即得到 (T6)。

### 7.2 中央权重的有限 n 上界

(7.1) 对应的计数变量方差为
\[
 V_B=(n-4)b+2\eta_k\ge(n-2)b.
\]
中心化特征函数的绝对值不超过
\[
 \exp[-2V_B\sin^2(t/2)].
\]
在 |t|<=pi 上使用 \(\sin(|t|/2)\ge |t|/\pi\)，再把 Gaussian 积分延长到实线，得
\[
 \frac{B_{k-1}}{n(n-1)}
 \le\frac1{2\pi}\int_{-\pi}^{\pi}e^{-2V_Bt^2/\pi^2}dt
 \le\frac{\sqrt\pi}{2\sqrt{2V_B}}.                            \tag{7.5}
\]
加上概率不超过 1，即得 (T7) 的第一式。对 n>=4，
\((n-1)/\sqrt{n(n-2)}\le3/(2\sqrt2)\)，代入 b=39/1600 得第二式。
这一步是有限 n 的不等式，不是局部中心极限定理或拟合。

### 7.3 如需进一步收紧到 O(n)，具体还欠什么

本报告的完整 O(n^(3/2)) 界没有未付尾部。不过更尖锐尺度尚未证明。
一个明确的充分条件是让中央带上的熵差缩小到 O(n^(-1/2))。

具体地，对整数 0<=R<=k，(7.3) 给出
\[
 \sum_{l=1}^{k-R}w_l=B_{k-R-1}.
\]
(7.1) 可分解为 n-2 个独立 Bernoulli 位的和，其均值为 k-1。
因此 Hoeffding 给出
\[
 B_{k-R-1}\le n(n-1)e^{-2R^2/(n-2)}.                          \tag{7.6}
\]
于是该尾区对 W 的绝对贡献至多
\(2\max(A_*,E_*)n(n-1)e^{-2R^2/(n-2)}\)。
选择 R 为 \(\sqrt{(n-2)\log n/2}\) 的向上取整（超过 k 时取 k），尾部已是 O(n)。
若能在剩余带内证明 \(|d_l|\le K/\sqrt n\)，则 (7.4)–(7.5) 给出 W=O(n)。
这个中央熵差条件目前 **INCOMPLETE**，不能用当前的常数界替代。
固定 R/sqrt(n) 的中央窗口不能仅凭集中性就把 O(n) 所需的尾部消去。

## 8. 合法的小尺度反例与失败机制

### 8.1 n=6 否定“删除后再正向热化”的全 n 规则

直接系数运算给出
\[
 \theta_{6,2}=\frac{(z-1)^2}{z^2+3z+1},\qquad
 \theta_{6,3}=\frac{(z-1)^2}{z^2+8z+1}.
\]
所以
\[
 s_3-s_2=\frac1{10}\log\frac{z^2+8z+1}{z^2+3z+1}>0.           \tag{8.1}
\]
n=6 的 \(r_2^{\max}\) 非恒定，且因单点边缘均匀，它在二层上的非恒定部分是
纯 Johnson degree two。其原始特征值为 10。
非恒定性可直接检查：相邻点的 \(|P_{ij}|^2=1/9\)，距离二的 \(|P_{ij}|^2=0\)，
故两类二点子式不同。

因此对任何 t>=0，
\[
 (\widehat q_3D_3)P_2^t=\mu_2(s_3+t)\ne\mu_2(s_2)=\widehat q_2,
\]
因为非零二阶模式的乘子分别为 \(e^{-10(s_3+t)}\) 和 \(e^{-10s_2}\)。
这个精确反例否定所述“所有 n 的正向钟修正”规则。
它不否定本报告的 Bayes 逆向桥，也不否定任意可能的非热型跨层核。

### 8.2 n=4 否定“W_n 对所有 n 非负”

这是第二个、用途不同的最小有理数诊断，不进行配置规模升级。
n=4 只有二层可能非均匀。记
\[
 \theta=\frac{(z-1)^2}{z^2+4z+1}.
\]
四个相邻对的修正密度为 \(1-\theta/4\)，两个对顶对的密度为
\(1+\theta/2\)。所以
\[
 h(2)=\frac23(1-\theta/4)\log(1-\theta/4)
      +\frac13(1+\theta/2)\log(1+\theta/2)>0.                  \tag{8.2}
\]
其余 h 为零。由实际 B 系数
\(B_0=B_2=2+4b\)、\(B_1=8-8b\)，得到完整的该实例响应
\[
 \boxed{W_4=(-12+24b)h(2)=-\frac{2283}{200}h(2)<0.}           \tag{8.3}
\]
这是指定修正律的反例，不是任意构造的测试数组。
它只否定全 n 非负性，不判定渐近符号、o(n) 或真实尺度。

## 9. 状态、对瓶颈的作用与剩余义务

**PROVED**：共同原始钟 intertwining；实际钟的单调性和相邻差界；
精确、归一、可嵌入实际层权重的逆向热桥；有界跨层对称差成本；
删除/桥 KL 分账；全层维数无关的熵差界；完整的实际 B 加权 O(n^(3/2)) 界。

**DISPROVED**：删除后仅增加非负均匀 BL 时间即可恢复所有相邻修正层的规则；
W_n 对所有偶数 n>=4 非负的规则。反例分别为 n=6、n=4。

**INCOMPLETE**：W 的真实全 n/渐近符号；尖锐增长阶或首项常数；
中央二阶差分的 O(1/n) 级控制；加权成本的进一步抵消；W+C 的符号。

与任务的实质关系是：不再仅有无条件的 \(h\ge0\) 和零端层，
而有了可跨所有层使用的 Lipschitz 正则性，以及将总量 n(n-1) 的曲率权重
降为中央权重 O(n^(3/2)) 的带符号证书。它排除了更大的绝对增长上界需求，
但并未证明 n^(3/2) 是实际阶。

真实 DPP 输出与修正律的比较、完整熵凹性、循环到 Toeplitz 的传递均不在本报告的已完成范围。
外部文献机制提供构造方向；所有需要的具体有限模型断言均在文内证明。

### 附注：式 (7.6) 不需额外集中性黑箱

对一个 Bernoulli 变量 X，记 g(t)=log E exp(t(X-EX))。
在指数倾斜律下 g''(t)=Var_t(X)<=1/4，且 g(0)=g'(0)=0，故 g(t)<=t^2/8。
对 n-2 个独立位相乘，并在左尾用 t=-4R/(n-2)，即得 (7.6)。
