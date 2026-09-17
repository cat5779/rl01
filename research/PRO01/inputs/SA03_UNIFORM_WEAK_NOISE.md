> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA03 后续完成：复数局部核控制与统一弱耦合余项

**状态：PROVED（本文给出证明，尚未独立审查）。** 本文付清 `SA03_STRUCTURAL_REFINEMENT.md` S4 原先单列的复解析缺口。此前“固定 R 小 u 余项尚未一致化”的状态由本文更新。核心有限抵消、O(1) 界、体积极限及有效 R 误差不依赖这一步。

小参数是 x=cu，即弱耦合/低有效对比度，不是物理信道噪声较小。仅延拓显式局部核，不延拓高维概率律，也不直接解析延拓实概率不等式。原题仍固定 c=19/20；下述 cu<=1/8 与 u>=1/(R+1) 相交。辅助延拓到 u=0 不改变 A_R 的定义。

## W1. 奇数子格的真实边缘

令 H=Q_R-I/2、a_i=(Q_R)_i0=p_hat_R(i)，B_z=sum_i sigma_i a_i^2，S_R^0=sum_i a_i^4。半填充 Fejer 核在非零偶数距离的系数为零，a_i 只在奇数 i 非零，奇数站点集合 O 的核限制恰为 I/2。所以 delta=0 时，真实边缘 Y_O 是独立公平 Bernoulli 位，对所有合法实 x 都成立。完整外部 word 仍不独立，q 仍使用全部外部位。

\[
\boxed{E_xB_z^2=S_R^0.}                                  \tag{W1}
\]

结构补充 S11 的 T_R^0 在本题为零：a_i a_j 非零时 i,j 同为奇数，而 i!=j 的 Q_ij=0。S11 的非负上界没有错，但此处可完全消去该项。B_z 的整个边缘分布是确定权重 a_i^2 的独立 Rademacher 和；这不是 q 的独立表示。

## W2. 复对称解析核

固定有限 R 和 word z，允许复 x、|x|<=1/4，定义

\[
G=(S_z/2+xH_C)^{-1},\quad b=xa,\quad v=Gb,
\quad q=1/2-b^TG b,\quad o_i=\sigma_iG_{ii}-1,
\quad\rho_i=\sigma_i-G_{ii}.
\]

H_C 实对称、范数 <=1/2，G 复对称。转置 T 没有共轭；v^T v 是实轴上 ||v||^2 的解析延拓，不把复欧氏范数当作解析函数。

Neumann 展开在全部 word 及翻位上给出

\[
\|G\|\le8/3<3,\quad|o_i-1|\le\|G-2S_z\|
 \le2|x|/(1-|x|)\le2/3,
\]
\[
|o_i|\le5/3,\quad|o_i^{-1}|\le3,
\quad|q-1/2|\le3|x|^2/4\le3/64.                           \tag{W2}
\]

因此没有赔率零点。所有后验在同一复圆盘，phi=(q-1/2)[log q-log(1-q)] 取该盘的解析分支。更大圆盘 |q-1/2|<=1/8 上有 |q(1-q)|>=15/64，显式导数公式给

\[
M_2=16,\qquad M_3=64,\qquad M_4=512.                      \tag{W3}
\]

后验之间的线段仍在圆盘内，复 Taylor 积分合法。

## W3. 逐项支付复数双翻位

取 a_*=4、ell=||b||<=|x|/2、L=a_*ell。点号表示固定 x 的 h 导数，在 h=1/2 评价。直接微分及秩一式给

\[
\dot q=1+v^Tv,\quad\dot G=-G^2,\quad\dot\rho_i=(G^2)_{ii},
\quad d_i={\sigma_i v_i^2\over o_i},
\]
\[
\dot d_i=-{2\sigma_i v_i(Gv)_i\over o_i}
 +{v_i^2(G^2)_{ii}\over o_i^2},\quad
\Delta_j\rho_i={\sigma_jG_{ij}^2\over o_j}\ (i\ne j).      \tag{W4}
\]

这是复对称双线性身份。取模后使用 |(G^2)_ii|<=a_*^2、|v^Tv|<=||v||^2、||Gv||<=a_*||v||，得到 V=||v|| 时

\[
\sum|d_i|\le a_*V^2,\quad\sum|d_i|^2\le a_*^2V^4,
\quad\sum|d_i||\dot d_i|\le2a_*^5V^4.                    \tag{W5}
\]

更新 v_i,o_i，并使用 |(v_i+d v_i)^2-v_i^2|<=2|v_i||d v_i|+|d v_i|^2，

\[
|e_{ij}|\le2a_*^2|G_{ij}||v_i||v_j|
 +a_*^3|G_{ij}|^2(|v_i|^2+|v_j|^2),\quad e_{ij}=\Delta_jd_i.
\]

全部行/列模平方和 <=a_*^2。Cauchy–Schwarz 逐项给

\[
\sum_{i\ne j}|d_i||e_{ij}|\le(2a_*^4+2a_*^6)V^4,
\quad\sum_{i\ne j}|e_{ij}|^2\le(12a_*^6+6a_*^{10})V^4,
\]
\[
\sum_{i\ne j}D_{ij}|e_{ij}|\le8a_*^{10}V^4,
\quad\sum_{i\ne j}|d_j|D_{ij}^2\le2a_*^3L^6.              \tag{W6}
\]

D_ij=max(|d_i(z)|,|d_i(z^j)|)。最后一式分别使用两个翻位数据组的统一 ||v||<=L，不使用复概率或正性。

令 Bi=Breg_phi(q+d_i,q)、barB_psi=sum_i rho_i Breg_psi(q_i,q)、Theta=sum_i rho_i Delta_i。复 Taylor 积分给

\[
|B_i|\le M_2|d_i|^2/2,\quad
|\dot B_i|\le M_3|d_i|^2|\dot q|/2+M_2|d_i||\dot d_i|,
\]
\[
|B_i(z^j)-B_i(z)|\le M_3|d_j|D_{ij}^2/2+M_2D_{ij}|e_{ij}|. \tag{W7}
\]

将 W4–W7 分别代入单和、速率导数和双和，不使用 Hermitian 正能量或概率期望，

\[
|\partial_h\bar B_\phi|\le L^4[M_2(a_*^4/2+2a_*^6)
 +M_3a_*^3(1+L^2)/2],
\]
\[
|\bar B_{\phi'}|\le M_3a_*^3L^4/2,
\quad|\Theta\bar B_\phi|\le9M_2a_*^{12}L^4+M_3a_*^5L^6.   \tag{W8}
\]

双和按 [Delta_j rho_i]Bi+rho_i(zj)[Delta_jBi] 分组；i=j 单独以 a_*M2|di|^2 控制。

归一化核的解析延拓为 barG=phi''q+barB_(phi')+partial_h barB_phi+Theta barB_phi。W8 给

\[
|\bar G-\phi''q|\le\ell^4(10M_2a_*^{16}+M_3a_*^{11}).
\]

又 phi'''(1/2)=0、|q-1/2|<=a_*ell^2，故 |phi''q-8|<=M4 a_*^2 ell^4/2。代入 W3、ell<=|x|/2，

\[
\boxed{|\bar G_{R,z}(x)-8|\le C_0|x|^4,
\quad C_0=10\cdot4^{16}+4\cdot4^{11}+256,
\quad|x|\le1/4.}                                         \tag{W9}
\]

量词对 R、word、复 x 一致，原 S4 的缺口至此付清。

## W4. 统一余项和真实期望

实际半填充核的子格共轭使 barG_z(x) 逐 word 偶解析；结构补充 S10 的有限 Taylor 代数给四次系数 P_z=256B_z^2+128S_R^0。对 (barG-8)/x^4 在半径 1/4 的圆上用 W9 与 Cauchy 系数估计，偶性去掉奇次项，得

\[
\boxed{|\bar G_{R,z}(x)-8-P_zx^4|
 \le{16C_0|x|^6\over1-16|x|^2}\quad(|x|<1/4).}            \tag{W10}
\]

实 x=cu<=1/8 时，在原真实 word 律下取期望，用 W1，

\[
\boxed{|I_R''(u,0)-8u^2-384S_R^0c^4u^6|
 \le{16C_0c^6u^8\over1-16c^2u^2}.}                        \tag{W11}
\]

这升级了原固定 R 余项。R=1 的四个真实外部 word 的四次系数另有精确符号检查；统一性来自本证明，不来自小算。

c/N<=1/8 时，辅助小 u 截断满足

\[
\boxed{\left|\int_0^{1/N}I_R''{du\over u}-{4\over N^2}
 -{64S_R^0c^4\over N^6}\right|
 \le{2C_0c^6\over N^8(1-16c^2/N^2)}.}                     \tag{W12}
\]

这不是整个 Fejer/体积误差。辅助小对比度 0<c<=1/8 时，先对有限 R 的整个 u 积分使用 W11，再由已证体积极限和 S_R^0->1/48，

\[
\boxed{|\Gamma(c)-4-\tfrac43c^4|
 \le{2C_0c^6\over1-16c^2}.}                               \tag{W13}
\]

W13 不以较小 c 替换任务的 c=19/20，也不外推至高对比度。

## W5. 最终缺口

S4 复解析升级和固定 R 小 u 余项一致性现已支付。仍未支付 Gamma(19/20) 的符号、u 接近 1 时的有符号预算、尖锐 R 误差/首个非零更细项、J_R 到真实熵率的二阶或固定弦桥接。C0 很大；主要价值是统一余项与系数，不宣称实用正性范围超过主报告小 u 界。没有增加重型计算。
