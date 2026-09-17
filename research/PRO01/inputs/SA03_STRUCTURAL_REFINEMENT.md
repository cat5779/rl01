> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA03 补充：速率的二次抵消与逐 word 弱耦合首项

**状态：S1–S3 为 PROVED；S4 的复解析升级为 INCOMPLETE 候选。** 同一有符号后验通量的进一步分解，不是第二条模型路线。主报告的 O(1)、体积极限及有效余项不依赖 S4。

## S1. 速率与赔率的精确漂移

D=partial_delta+T，r_i=u(sigma_i-Gii)，o_i=sigma_iGii-1。D sigma_i=-2sigma_i r_i，DGii=0，故

\[
\boxed{Dr_i=2u^2o_i>0\quad(u>0).}                         \tag{S1}
\]

这是 r_i'+T r_i 的完整抵消，不是单独给 r_i' 判正。离散乘积式

\[
D(fg)=fDg+gDf+\sum_jr_j\Delta_jf\Delta_jg
\]

作用于 o_i 时，仅 j=i 的交叉项非零。利用 Delta_iGii=-sigma_iGii^2/o_i，得到

\[
\boxed{Do_i=-2uG_{ii}.}                                   \tag{S2}
\]

Dv=0，同一乘积式还给

\[
\boxed{D\|v\|^2=-u\sum_i{\sigma_i|v_i|^2(G^2)_{ii}\over o_i}.} \tag{S3}
\]

也可由对 Dq=u 求参数导数核对。S1–S2 已在两个相互作用外部位的精确符号脚本中复核；一般维数证明为上述逐位代数。

## S2. 正预算和混合残差

B_i=Breg_psi(q_i,q)，q_i=q(z^i)，d_j^i=q(z^(ij))-q(z^i)，令

\[
C_i=\sum_j[r_j(z)-r_j(z^i)]d_j^i.
\]

比较 z 与 z^i 上的运输，

\[
Dq_i=u+C_i.                                               \tag{S4}
\]

定义明确的二变量链式缺陷

\[
\Xi_{ij}=B_i(z^j)-B_i(z)
 -[\psi'(q_i)-\psi'(q)]d_j^i+\psi''(q)d_i d_j.             \tag{S5}
\]

从而 DB_i=u Breg_(psi')(q_i,q)+[psi'(q_i)-psi'(q)]C_i+sum_j r_j Xi_ij。结合 S1 和乘积式，

\[
\begin{aligned}
\mathcal G_\psi={}&u^2\psi''(q)+2u\mathcal B_{\psi'}
 +\underbrace{2u^2\sum_i o_i B_i}_{\text{凸 psi 时非负}}\\
&+\sum_i r_i[\psi'(q_i)-\psi'(q)]C_i
 +\sum_{ij}r_ir_j\Xi_{ij}
 +\sum_{ij}r_j\Delta_jr_i\Delta_jB_i.
\end{aligned}                                             \tag{S6}
\]

它不是净残差非负的断言。三个混合项及 Bcal_(psi') 的符号仍须支付；同位和不同位翻转全部保留。

### 二变量缺陷的连通界

设 e_ij=Delta_jd_i、D_ij=max(|d_i(z)|,|d_i(z^j)|)。写 Btilde(q,d)=psi(q+d)-psi(q)-psi'(q)d，其 Hessian 满足

\[
|\partial_{qq}\widetilde B|\le M_4d^2/2,\quad
|\partial_{qd}\widetilde B|\le M_3|d|,\quad
|\partial_{dd}\widetilde B|\le M_2.
\]

对增量 (d_j,e_ij) 用二阶 Taylor 积分余项，

\[
\boxed{|\Xi_{ij}|\le M_4D_{ij}^2d_j^2/4
 +M_3D_{ij}|d_j||e_{ij}|+M_2|e_{ij}|^2/2.}                 \tag{S7}
\]

主要部分带连通双差分 e_ij；不带 e_ij 的部分再多两个后验跳跃权重。i=j 时 e_ii=-2d_i，公式仍合法。

a=epsilon^-1>=2、L=a||b|| 时，主报告带权和给出

\[
\sum_{ij}D_{ij}^2d_j^2\le2a^4L^8,\quad
\sum_{ij}D_{ij}|d_j||e_{ij}|\le9a^{11}L^6,\quad
\sum_{ij}|e_{ij}|^2\le8a^{10}L^4.
\]

因此

\[
\left|\sum_{ij}r_ir_j\Xi_{ij}\right|
 \le u^2[M_4a^6L^8/2+9M_3a^{13}L^6+4M_2a^{12}L^4].       \tag{S8}
\]

主报告用另一种分组已经支付完整曲率；本分组供下一步符号比较，不自动宣称更优常数。

## S3. 真实半填充核的逐 word 首项

固定有限 R，x=cu，H=Q_R-I/2，a_i=(Q_R)_i0=p_hat_R(i)，令标量

\[
B_z=\sum_i\sigma_i a_i^2,\qquad S_R^0=\sum_i a_i^4.
\]

此处 a_i 是中心列，不是信道位移；B_z 是标量，不是条件事件矩阵。归一化核 barG=Gcal/u^2 只通过 x 依赖 u,c。

实际半填充 Fejer 核只连接相反奇偶性，Jii=(-1)^i 满足 JHJ=-H，中心列 a 只在奇数位非零。故逐 word

\[
G(-x)=JG(x)J,\quad v(-x)=Jv(x),\quad q_z(-x)=q_z(x),
\quad\overline{\mathcal G}_z(-x)=\overline{\mathcal G}_z(x). \tag{S9}
\]

固定 R 的有限解析展开给

\[
q_z=1/2-2x^2B_z+O_R(x^4),\quad
 d_i=4\sigma_i a_i^2x^2+O_R(x^4),
\]
\[
\bar r_i=-\sigma_i+O_R(x^2),\quad(G^2)_{ii}=4+O_R(x^2),
\quad1+\|v_z\|^2=1+4x^2\|a\|^2+O_R(x^4).
\]

(V14) 的四次系数逐项为：phi''-8 给 256B_z^2；sum_i(G^2)ii B_i 给 256S_R^0；最后双翻位项给 -128S_R^0；其余从六次开始。因此

\[
\boxed{\overline{\mathcal G}_{R,u}(z)
 =8+x^4(256B_z^2+128S_R^0)+O_R(x^6).}                     \tag{S10}
\]

这是明确的正四次局部核，不规定 x 接近 1 时净残差符号。O_R 对固定有限 word 集一致，尚未用于 R 一致结论。

真实 DPP 二点矩还给出精确式

\[
E_x B_z^2=S_R^0-4x^2T_R^0,\quad
T_R^0=\sum_{i\ne j}a_i^2a_j^2|Q_{ij}|^2,\quad0\le T_R^0\le1/64. \tag{S11}
\]

因为 E sigma_i sigma_j=-4x^2|Qij|^2，sum_i a_i^2<=1/4，每行非对角平方和 <=1/4。S10 的四次部分取期望后为 384S_R^0 x^4-1024T_R^0 x^6。**后一项不是完整六次系数**，未展开余项也从六次开始。

## S4. INCOMPLETE：复解析升级候选

仅解析延拓显式局部核，不估计高维复 word 似然。目标引理是

\[
|\overline{\mathcal G}_{R,z}(x)-8|\le C_0|x|^4,
\quad |x|\le1/4,\quad C_0=10\cdot4^{16}+4\cdot4^{11}+256, \tag{S12?}
\]

对 R,z 一致。问号表示尚未纳入已证输入。

已具备条件：实对称核在复 x 下仍有复对称 G，v^T v 给出原范数平方的解析延拓。Neumann 界给 ||G||<=8/3<3、|o_i-1|<=2/3、|q_z-1/2|<=3/64。因此赔率不为零，后验处于同一解析对数分支。在 |q-1/2|<=1/8 上可取复导数界 M2=16、M3=64、M4=512。

精确缺口是逐项重做主报告第 6 节的复数双翻位绝对和：把 Hermitian 乘积换成复对称双线性乘积，同时保留全部行/列模平方估计和两端赔率逆界。不能只说实参数概率不等式解析延拓后仍成立。

若该复数全域界付清，S9 偶性与 Cauchy 估计会给 |x|<=1/8 上

\[
|\overline{\mathcal G}-8-x^4(256B_z^2+128S_R^0)|
 \le{16C_0|x|^6\over1-16|x|^2}.                           \tag{S13?}
\]

再结合 S11 可升级为统一 O(c^6u^8) 的弱噪声余项。本次不计入已证结论，不用它给 Gamma(19/20) 判号；即使完成，也仍只是弱耦合端。
