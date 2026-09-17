> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA03 定量附录：可计算的体积余项，不假设幂次渐近

**状态：PROVED（下文给出证明，尚未独立审查）。** 本附录量化同一候选的局部逼近，不提供符号或最优速率，不用拟合。

## Q1. 全部显式常数与结论

固定 0<c<1，记

\[
a={2\over1-c},\quad L=ac/2,\quad C_c=21c^4a^{18}/16,
\quad B_c=8+C_c,\quad\kappa_c=\min\{1/2,-\log c\},
\]
\[
V_c={2\sqrt2c\over\pi(1-c)}+{4c^2\over(1-c)^2},
\quad F_c=\sqrt2V_c+{1\over1-c},
\quad G_c={8\sqrt2c\over(1-c)^2}+{2\over1-c}.
\]

定义非增尾包络（s>=1）

\[
f_c(s)=\begin{cases}L,&s<e^4,\\
\min\{L,F_ce^{-\kappa_c\sqrt{\log s}}\},&s\ge e^4,
\end{cases}
\quad
 g_c(s)=\begin{cases}a,&s<e^4,\\
\min\{a,G_ce^{-\kappa_c\sqrt{\log s}}\},&s\ge e^4.
\end{cases}                                               \tag{Q1}
\]

整数 m>=2 时令

\[
T_c(m)=16a^{16}\{f_c(m)+f_c(m/2)^2+g_c(m/2)^2\}.           \tag{Q2}
\]

取整数参数满足

\[
2\le m,\quad2m\le d\le R/2,\quad2m\le M\le R/2.           \tag{Q3}
\]

无需优化参数。定义

\[
D_R(d,m)=2a^2\{R^{-1/2}+\sqrt{2d/R}+f_c(d)+g_c(d-m)\},
\]
\[
E_{\rm ker}(R;m,d)=2T_c(m)+128a^{12}m^2D_R(d,m),
\]
\[
E_{\rm cyl}(M;m)=2T_c(m)+128a^{13}m^2\{f_c(M)+g_c(M-m)\},
\]
\[
\boxed{E_c(R;m,d,M)=E_{\rm ker}(R;m,d)+2E_{\rm cyl}(M;m)
             +{4acB_cM^2\over\pi(R+1)}.}                  \tag{Q4}
\]

此误差只含 R,c 和三个整数，不含未知曲率或概率期望。任务的正奇数 R 上，只要 (Q3) 可满足，

\[
\boxed{|A_R''(0)-\Gamma(c)|\le E_c(R;m,d,M)/2
              +{4\over(R+1)^2}+{C_c\over6(R+1)^6}.}       \tag{Q5}
\]

很小 R 可使用主报告和体积极限附录的粗界。常数非常大；它是可复核的有效余项，不宣称在实用 R 已足够小。

保守推论：存在可计算有限 K(c)，充分大 R 上

\[
\boxed{|A_R''(0)-\Gamma(c)|\le K(c)
 e^{-\kappa_c^{3/2}(\log R)^{1/4}/16}.}                    \tag{Q6}
\]

Q8 给出参数和极大的显式起始范围。它不是最优性或完整幂次展开声明。有限 R 的证书优先使用完全显式 (Q4)–(Q5)。

## Q2. 全 word 的有效列尾

沿用体积极限附录的 H_R^0,H_infty^0,b_R^0,b_infty^0，以及 G=(S_z/2+uH)^-1、v=Gub，u in [0,1]。共同输入为

\[
\|2H\|\le c,\quad H_{ii}=0,\quad|H_{ij}|\le{c\over\pi|i-j|},
\quad\|b\|\le c/2,\quad|b_i|\le{c\over\pi|i|}.           \tag{Q7}
\]

所有估计对有限 R、infinity、u、z 一致。令 T0=-2uS_zH（仅本节的 Neumann 算子，不是主报告 word 运输 T），||T0||<=c。P_s^j0 表示 |i-j0|<=s 的外部坐标投影。s>=1、t>=2s 时

\[
\|(I-P_t^{j_0})T_0P_s^{j_0}\|\le4c\sqrt{s/t}.            \tag{Q8}
\]

证明：每个近端列的远端平方和 <=4/(t-s)<=8/t，近端坐标数 <=3s，乘 4c^2/pi^2 得平方 <=96c^2s/(pi^2t)<16c^2s/t。排除站点 0 只减少项。因此

\[
\|(I-P_t^{j_0})T_0x\|\le c\|(I-P_s^{j_0})x\|
                                      +4c\sqrt{s/t}\|x\|. \tag{Q9}
\]

### 中心响应尾

x0=S_zub，||x0||<=c/2，B>=2 时 tail_B(x0)<=sqrt2 c/(pi sqrtB)。在半径 B,B^2,...,B^(k+1) 上迭代，

\[
\|(I-P_{B^{k+1}}^0)T_0^kx_0\|
 \le{c^k\sqrt2c\over\pi\sqrt B}+{2kc^{k+1}\over\sqrt B}. \tag{Q10}
\]

v=2 sum_(k>=0)T0^k x0。若 B^(K+1)<=s，有限和及几何尾给出

\[
\|(I-P_s^0)v\|\le V_c/\sqrt B+c^{K+2}/(1-c).              \tag{Q11}
\]

### 逆矩阵列尾

改用 x0=S_z e_i，范数 1，支撑 i。以半径 1,B,...,B^K 迭代，B^K<=s 时

\[
\|(I-P_s^i)Ge_i\|\le {8c\over(1-c)^2\sqrt B}
                              +{2c^{K+1}\over1-c}.         \tag{Q12}
\]

这是对列中心 i 一致的尾，不用不成立的 l1 行和界。

s>=e4 时令 r=sqrt(logs)、B=floor(exp r)；中心列式取 K=floor r-1，逆矩阵列式取 K=floor r。半径条件成立，B^-1/2<=sqrt2 exp(-r/2)，c^(floor r+1)<=exp[-(-logc)r]。结合全局范数，

\[
\boxed{\|(I-P_s^0)v\|\le f_c(s),\qquad
       \sup_i\|(I-P_s^i)Ge_i\|\le g_c(s).}                \tag{Q13}
\]

包络在 e4 处允许向下跳；两侧均为合法上界。

## Q3. 归一化曲率核的有限指标截断

将 (V14) 单和限于 i in C_m、双和限于 i,j in C_m，保留 phi''(q)，记 barG^[m]。这还不是有限观察，q,v,G 仍使用全部 word。

**引理 Q3.1：**

\[
\boxed{|\overline{\mathcal G}-\overline{\mathcal G}^{[m]}|
                   \le T_c(m).}                          \tag{Q14}
\]

证明：写 f=f_c(m)、f*=f_c(m/2)、g*=g_c(m/2)。|d_i|<=a|v_i|^2，|d_i'|/u<=2L^2。M2<=2a^2、M3<=8a^3，三个单和尾共 <=2a^10 f^2。

令 gij=|Gij|，并记

\[
K_1=g_{ij}|v_i|^3|v_j|,\quad K_2=g_{ij}^2|v_i|^4,
\quad K_3=g_{ij}^2|v_i|^2|v_j|^2,\quad K_4=g_{ij}^4|v_i|^4.
\]

在 i 不在 C_m 或 j 不在 C_m 的并集上，

\[
\sum K_1\le2aL^3f,\quad
\sum K_2\le2a^2L^2f_*^2+L^4g_*^2,
\]
\[
\sum K_3\le2a^2L^2f^2,\quad
\sum(K_4+K_4^{\rm swapped})\le2a^2\sum K_2.               \tag{Q16}
\]

第二式将 i 分为 |i|<=m/2 和其余部分；前者到 |j|>m 的距离超过 m/2，使用中心一致列尾，后者使用 v 的尾。其它式由 Cauchy–Schwarz 和行平方和。

由主报告的 e_ij 连通界、D_ij<=|d_i|+|e_ij|，二次差分的非对角绝对值由

\[
4a^7K_1+3a^8K_2+26a^8K_3
 +6a^{10}(K_4+K_4^{\rm swapped})+4a^5|d_j|D_{ij}^2         \tag{Q17}
\]

总和控制。最后项的尾 sum |d_j|D_ij^2<=4a^3L^4 f^2。对角 i=j 另付 2a^6L^2f^2。与单和尾合并，L<=a/2、a>=2，所得不超过 16a^16(f+f*^2+g*^2)。没有把不收敛的裸双项拆开估计。

## Q4. 有限指标核的数据稳定性

两个合法条件数据组 (q,v,G,S) 和带波浪组，在 C_m 上的符号 S 相同。令

\[
\Delta=\max\{|q-\tilde q|,\|v-\tilde v\|,
                  \max_{i\in C_m}\|(G-\tilde G)e_i\|\}.
\]

**引理 Q4.1：**

\[
\boxed{|\overline{\mathcal G}^{[m]}
             -\widetilde{\overline{\mathcal G}}^{[m]}|
                     \le128a^{12}m^2\Delta.}              \tag{Q18}
\]

常数核对：赔率下界给 |o_i^-1-otilde_i^-1|<=a^2 Delta。秩一更新依次给出

\[
|d_i-\tilde d_i|\le a^4\Delta/2,\quad
|q(z^i)-\tilde q(z^i)|\le a^4\Delta,
\]
\[
\|v(z^i)-\tilde v(z^i)\|\le a^4\Delta,
\quad\|(G(z^j)-\tilde G(z^j))e_i\|\le2a^4\Delta,
\]
\[
|q(z^{ij})-\tilde q(z^{ij})|\le a^8\Delta.                \tag{Q19}
\]

i=j 时退化为原 q。A_z=1+||v_z||^2<=a^2/2；其翻位值差 <=a^5 Delta。Breg_phi 对两个端点的偏导为 phi'(p)-phi'(q) 和 -phi''(q)(p-q)，所以每个翻位缺陷的差 <=4a^10 Delta；Breg_(phi') 的差 <=16a^11 Delta。

(V14) 基础 phi'' 项差 <=8a^3 Delta；三个单和每个指标差分别可取 20a^12 Delta、5a^12 Delta、6a^12 Delta。第三个先比较组合 (phi'(q_i)-phi'(q))A_i-phi''(q)d_i A，其变化 <=5a^8 Delta，再付速率变化。每个有序双指标差 <=10a^12 Delta。s=2m>=2，所以总差 <=[8a^3+(31s+10s^2)a^12]Delta<=104a^12m^2Delta<=128a^12m^2Delta。全部后验端点合法，无 word 独立假设。

## Q5. Fejer 算子变化

E_R=H_R^0-H_infty^0。|j|<=d<=R/2 时直接分割 Fourier 系数，

\[
\|E_Re_j\|^2\le{8c^2\over\pi^2R}\le{c^2\over R},
\quad\|E_RP_d\|\le c\sqrt{2d/R},\quad\|E_R\|\le c,
\]
\[
\|b_R^0-b_\infty^0\|\le cR^{-1/2}.                       \tag{Q20}
\]

在保留区间内，|i-j|<=R 时每个条目差 <=c/[pi(R+1)]；|i-j|>R 用 1/|i-j| 尾，两部分平方和共 <=4c^2/(pi^2R)。区间外因 |j|<=R/2，再付 <=4c^2/(pi^2R)。中心列更直接。

同一 word 下 resolvent 恒等式给

\[
\|v_R-v_\infty\|\le ac\{R^{-1/2}+L\sqrt{2d/R}+f_c(d)\},
\]
\[
\max_{i\in C_m}\|(G_R-G_\infty)e_i\|
 \le ac\{a\sqrt{2d/R}+g_c(d-m)\}.                         \tag{Q21}
\]

q 用 1/2-ub*v 比较，全部数据误差均 <=D_R(d,m)。加两端截断误差得

\[
\boxed{\sup_{u,z}|\overline{\mathcal G}_{R,u}(z)
 -\overline{\mathcal G}_{\infty,u}(z)|\le E_{\rm ker}(R;m,d).} \tag{Q22}
\]

## Q6. 从有限指标到有限观察

令 z^[M] 在 C_M 上等于 z，窗口外取全 0。两条件矩阵只在窗口外对角相差范数 <=1 的算子。resolvent 恒等式给

\[
\|v(z)-v(z^{[M]})\|\le af_c(M),
\quad\max_{i\in C_m}\|(G(z)-G(z^{[M]}))e_i\|
                          \le ag_c(M-m).                  \tag{Q23}
\]

q 差也 <=af_c(M)。用 (Q18) 和两端 (Q14)，

\[
\boxed{\sup_{u,z}|\overline{\mathcal G}_{\infty,u}(z)
 -\overline{\mathcal G}_{\infty,u}(z^{[M]})|
                                      \le E_{\rm cyl}(M;m).} \tag{Q24}
\]

全 0 只定义一个有限观察函数，不是把真实律条件在无限全 0 事件上，不需要其有正概率。

## Q7. 真实 word 概率变化

有限 s 维 DPP 若 K_t=K0+tE 全程保持谱隙 epsilon，则完整原子微分

\[
\partial_t p_t(z)=p_t(z)\operatorname{Tr}(G_{t,z}E).
\]

由 ||G||<=epsilon^-1，积分半个绝对导数和得到

\[
\operatorname{TV}(P_{K_0},P_{K_1})\le{s\over2\epsilon}\|E\|. \tag{Q25}
\]

是真实 word 概率，不是计数分布。

在 C_M 上，2M<=R，Fejer 与 sine 的每个非对角差 <=c/[pi(R+1)]，维数 2M，线段保留共同谱隙，所以 u 一致地

\[
\operatorname{TV}(P_{R,u}|_{C_M},P_{\infty,u}|_{C_M})
 \le{2acM^2\over\pi(R+1)}.                               \tag{Q26}
\]

有限观察函数 barG_infty(u,z^[M]) 的绝对值 <=B_c。结合 (Q22)、两次 (Q24) 与 (Q26)，

\[
\boxed{\sup_{u\in[0,1]}|E_{R,u}\overline{\mathcal G}_{R,u}
 -E_{\infty,u}\overline{\mathcal G}_{\infty,u}|
                              \le E_c(R;m,d,M).}          \tag{Q27}
\]

对 u du 积分，单独支付小 u 截断，得到 (Q5)。

## Q8. 保守的非幂次速率

令 t=logR、alpha=kappa_c/64，取

\[
d=\lfloor R^{1/2}\rfloor,\quad M=\lfloor R^{1/4}\rfloor,
\quad m=\lfloor e^{\alpha\sqrt t}\rfloor.                 \tag{Q28}
\]

例如 t>=(512/kappa_c)^2 足以保证全部整数约束及所有尾半径 >=e4。此起点极大，仅用于展示可计算性。

log(m/2)>=alpha sqrt(t)/2，故

\[
T_c(m)\le K_1(c)e^{-\kappa_c\sqrt{\alpha/2}\,t^{1/4}}.   \tag{Q29}
\]

log(d-m)>=t/4、log(M-m)>=t/8，因此乘 m^2 的数据误差 <=K_2(c) exp[-kappa_c sqrt(t)/4]；m^2 R^-1/4 更快。真实律项 M^2/(R+1)=O(R^-1/2)。由于 kappa_c sqrt(alpha/2)=kappa_c^(3/2)/sqrt128>kappa_c^(3/2)/16，得到 (Q6)。K1,K2,K 均可由 (Q1)–(Q5) 和所列不等式展开；完全显式 (Q5) 已避免依赖这些压缩常数。

## 剩余范围

此速率不判 Gamma(19/20) 的符号，不给实用判号半径，不识别 1/R 或 logR/R 等更细主项，不能替代截断生产泛函到真实熵率的导数桥接。它只将未知趋零速度改进为明确、可计算但很慢的上界。
