> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA03 / S9：真实 word 律的有符号后验通量与有界次主阶残差

**日期：2026-09-17。任务：PR #118 / TASK_03_S9_SUBLEADING_RESIDUE.md。**

**数学状态：PROVED（有限恒等式、结构估计、统一有界曲率；附录另证有限极限及有效余项）；INCOMPLETE（极限常数的符号、尖锐 R 余项与真实熵率传递）。**
PROVED 指本文给出证明，不表示已经经过独立审查。R=1 检查不替代成长体积证明。本文不宣称文献上的首次发明。

## 1. 候选工具与域外迁移

在实际外部物理 word 的超立方体上构造固定算子 L、依赖实际概率的通量 T，以及 D=partial_delta+T，使

\[
L^*w=T^*w=w',\qquad Dq=u,\qquad DG_z=0.                 \tag{1.1}
\]

G_z 是完整条件事件矩阵的逆。这里星号表示相对于计数测度的转置伴随；矩阵 b* 则表示复共轭转置。

后验的完整响应被通量精确抵消成 u，非线性链式法则的剩余是离散 Bregman 缺陷，只涉及原 word、一次/二次翻位及矩阵逆的行列，不用高斯近似。

### 1.1 迁移来源和失效条件

Braverman 的 prelimit generator comparison 从有限/离散过程的 Poisson 方程出发，所需 Stein 因子对应有限差分，而不是极限扩散解的导数。[BRA] 本题 w_delta 移动，单选不变律为 w_delta 的生成元不能支付 w'。本文将正出生运输 P 与可逆生成元 A 配对，T=P-A；实际后验 q-h 是漂移缺陷 Poisson 方程的显式中心化解。有限不可约性保证可解性，但本文不借用未核验的一致谱隙或队列模型估计。差分估计由第 6 节另付。

Chafai 的离散 Phi-calculus 保留 Phi(q+d)-Phi(q)-Phi'(q)d。[CHA] 本文迁移的是精确代数缺陷，不是正半群耗散：T 的速率有正有负，T*w=w' 而非 0，不具备正 Dirichlet 型。第 8 节在真实 R=1 模型内否定一个正耗散闭合规则。

新增 DPP 构件是 Schur 补、秩一翻位和中心响应 |G_z b|^2 权重。Bregman 缺陷再提供一层后验影响权重，使双翻位和由行平方和控制，而不是支付外部位数。

### 1.2 加强结论

令 epsilon_c=(1-c)/2、N=R+1。对每个任务指定的正奇数 R，

\[
\boxed{|A_R''(0)-4(1-N^{-2})|
 \le {7c^4\over32\epsilon_c^{18}}(1-N^{-6}),\qquad A_R''(0)=O_c(1).} \tag{1.2}
\]

常数很粗，在 c=19/20 不足以判号。这是有限完整 word 恒等式推出的统一界，严格加强已有 o(R)，不是预设常数阶。

`SA03_VOLUME_LIMIT.md` 另证

\[
A_R''(0)=\Gamma(c)+o(1),\qquad
\Gamma(c)=\int_0^1u\,E_{\infty,u}\overline{\mathcal G}_{\infty,u}\,du. \tag{1.3}
\]

无限核由该附录 (V14) 的绝对可求和公式定义，不把待求极限改名。`SA03_EFFECTIVE_REMAINDER.md` 给出显式有限截断误差，并推出保守的

\[
A_R''(0)=\Gamma(c)+O_c(e^{-\kappa_c^{3/2}(\log R)^{1/4}/16}),
\quad\kappa_c=\min\{1/2,-\log c\}.                         \tag{1.4}
\]

常数与起始范围极大，不宣称最优速率或完整幂次展开。Gamma 的值与符号未定。

## 2. 固定模型和通用物理 word 通量

### 2.1 模型不变

频率空间 R/Z，E=[-1/4,1/4]，rho=1/2，c=19/20，R 为正奇数，N=R+1，

\[
p_R(t)=\sum_{|k|\le R}(1-|k|/N)q_k e^{2\pi ikt},\quad
q_0=1/2,\quad q_k={\sin(\pi k/2)\over\pi k},
\]
\[
f_{R,u,\delta}=1/2+u\{c(p_R-1/2)+\delta\},
\quad u\in[1/N,1],\quad |\delta|<(1-c)/2.
\]

原信道位移为 (1-c)/2+delta。在 {0} union C、C=[-R,R] minus {0} 上使用真实 Toeplitz DPP。n=|C|=2R，

\[
M=\sum_{i\in C}Y_i,\quad X=(M-R)/\sqrt R,
\quad q_z=P(Y_0=1\mid Y_C=z),\quad w_z=P(Y_C=z),
\]
\[
\phi(q)=(q-1/2)\log{q\over1-q},\quad
I_R(u,\delta)=E\phi(q),\quad
A_{R,F}=\int_{1/N}^1E[\phi(q)F(X)]\,{du\over u}.
\]

X 始终按此定义，不随 delta 平移。所有撇号固定 u,R,c 对原 delta 求导。A_R=A_(R,1)，J_R=log2-A_R，不是块熵除以块长。

### 2.2 完整质量导数

z^i 表示翻转物理位 i，sigma_i=2z_i-1，o_i=w_(z^i)/w_z>0。实际概率满足

\[
w_z'=u\sum_i\sigma_i(z)(w_z+w_{z^i}).                    \tag{2.1}
\]

证明：完整 DPP 原子的行列式对角导数的余子式就是删除该位的真实边缘概率。也可给定潜在输入 X，逐位微分成功概率导数为 u 的独立信道乘积，再对 X 平均。独立的是给定输入的噪声，不是物理输出 Y。

定义

\[
(Lg)(z)=-u\sum_i\sigma_i(z)[g(z^i)-g(z)],
\quad r_i=-u\sigma_i o_i,\quad
(Tg)(z)=\sum_i r_i[g(z^i)-g(z)].                           \tag{2.2}
\]

两算子行和为零，但不是正 Markov 生成元。逐边计算

\[
w_{z^i}r_i(z^i)-w_zr_i(z)=u\sigma_i(z)(w_z+w_{z^i}),
\]

故 T*w=w'，同理 L*w=w'。有限超立方体每边两端均保留。

### 2.3 后验精确漂移

暂令 a_z=P(Y0=1,Y_C=z)。联合质量导数为

\[
a_z'=uw_z+u\sum_i\sigma_i(z)(a_z+a_{z^i}).
\]

结合 (2.1) 与 q=a/w，

\[
q_z'=u+u\sum_i\sigma_i o_i(q_{z^i}-q_z),\qquad
\boxed{Dq=q'+Tq=u.}                                      \tag{2.3}
\]

这包含中心导数、外部权重移动及后验分母导数；没有把它们丢进未知误差。这个通量身份适用于一般混合 Bernoulli 加性信道；DPP 结构只在后续估计进入。

### 2.4 对偶分部求和和完整二阶项

逐边重排给出，对任意可微 word 函数 f,g，

\[
{d\over d\delta}E[fg]=E[fDg]+E[g(\partial_\delta+L)f].    \tag{2.4}
\]

因此 (Eg)'=EDg、(Eg)''=ED^2g。由于 T 随 delta 移动，

\[
D^2g=g''+2Tg'+(T'+T^2)g,
\quad (T'+T^2)^*w=w''.
\]

所以它恰好是 sum_z(w_z g_z''+2w_z'g_z'+w_z''g_z)，取 g=phi(q) 恢复题面完整 Hessian。没有删除 T'、score 导数、交叉项或 u 因子。

### 2.5 真正的可逆 Poisson 反项

定义两个正生成元

\[
Pg=\sum_{i:z_i=0}u(1+o_i)[g(z^i)-g(z)],
\]
\[
Ag=\sum_{i:z_i=0}u[g(z^i)-g(z)]
 +\sum_{i:z_i=1}uo_i[g(z^i)-g(z)].                         \tag{2.5}
\]

P 是出生运输，P*w=w'。A 在每个 z_i=0 的边满足 w_z u=w_(z^i)u o_i(z^i)，所以可逆、A*w=0，并且 T=P-A。

u>0 时全 word 严格正，有限 A 不可约，且

\[
-\langle f,Af\rangle_w=u\sum_{\{z,z^i\}:z_i=0}w_z|f(z^i)-f(z)|^2.
\]

零空间恰为常数，中心化右端有唯一均值零 Poisson 解。由 (2.3)，

\[
\boxed{A(q-h)=(\partial_\delta+P)q-u,\quad E(q-h)=0,\quad h=K_{00}.} \tag{2.6}
\]

右端均值为零，因为 P*w=w'、(Eq)'=h'=u。实际后验本身就是具体 Poisson 方程的显式解，不是假设存在一个未知正确子。本文不借用一致谱隙；其非线性差分由下文支付。两个正生成元的差没有正耗散性质。

## 3. DPP 局部量及全 word 边界

先对任意有限 Hermitian 路径 K_delta=K0+u delta I 推导，在评价点假设

\[
\epsilon I\le K\le(1-\epsilon)I,\quad0<\epsilon\le1/2.
\]

不要求有限核为投影。分块定义

\[
h=K_{00},\quad b=K_{C0},\quad B_z=K_C-\operatorname{diag}(1-z),
\quad G_z=B_z^{-1},\quad v_z=G_zb.
\]

b 对 delta 不变，h'=u。完整原子 Schur 补给出

\[
q_z=h-b^*G_zb.                                            \tag{3.1}
\]

### 3.1 所有 word 一致合法

B_z=S_z/2+(K_C-I/2)，S_z=diag(sigma_i)。因为 ||K_C-I/2||<=1/2-epsilon，故 ||B_z x||>=epsilon||x||，从而

\[
\|G_z\|\le\epsilon^{-1}.                                \tag{3.2}
\]

把 K 写成 epsilon I+(1-2epsilon)Q，并用潜在 DPP(Q) 加独立信道表示，可知任何一个未观察位的条件成功率均在 [epsilon,1-epsilon]；该位噪声不能被其它输出消去。所以

\[
q_z\in[\epsilon,1-\epsilon],\quad
{\epsilon\over1-\epsilon}\le o_i\le{1-\epsilon\over\epsilon}.
\]

这包括极小概率 word。由 K-K^2>=0 的中心对角元，

\[
\|b\|^2\le h(1-h)\le1/4.                               \tag{3.3}
\]

### 3.2 一次翻位

行列式引理和秩一更新给出

\[
o_i=\sigma_iG_{ii}-1,\quad r_i=u(\sigma_i-G_{ii}),
\]
\[
G_{z^i}=G_z-{\sigma_i\over o_i}G_ze_ie_i^*G_z,
\quad v_{z^i}=v_z-{\sigma_i\over o_i}v_iG_ze_i,
\]
\[
d_i=q_{z^i}-q_z={\sigma_i|v_i|^2\over o_i},\qquad
r_id_i=-u|v_i|^2,\quad q_z'=u(1+\|v_z\|^2).              \tag{3.4}
\]

于是再次直接验证 Dq=u。更强地，G'=-uG^2，而

\[
TG=\sum_i(-u\sigma_io_i)(-\sigma_i/o_i)Ge_ie_i^*G=uG^2.
\]

故

\[
\boxed{DG_z=0\text{ 逐矩阵元成立}.}                       \tag{3.5}
\]

它抵消整块条件 resolvent 的漂移，不是仅减去计数 score 的高斯主阶。

### 3.3 Schur 能量

令 x=(1,-v_z)，D 只标记外部空位。Schur 方程给出 Kx=(q_z,-Dv_z)，所以

\[
\boxed{x^*K(I-K)x=q_z(1-q_z).}                            \tag{3.6}
\]

kappa=epsilon(1-epsilon) 时，

\[
1+\|v_z\|^2\le{q_z(1-q_z)\over\kappa},\quad
{q_z'\over q_z(1-q_z)}\le{u\over\kappa}.
\]

外部块还有

\[
GK_C(I-K_C)G=(S_zG+GS_z)/2-I.
\]

其 i 对角元为 o_i，故

\[
\boxed{(G^2)_{ii}=\sum_j|G_{ij}|^2\le{o_i\over\kappa}.} \tag{3.7}
\]

这些更尖锐的带权能量式可供改进常数；第 6 节只用粗范数界，使证明不依赖额外优化。

## 4. P1：完整曲率的局部残差

对光滑 psi 定义

\[
\operatorname{Breg}_\psi(p,q)=\psi(p)-\psi(q)-\psi'(q)(p-q),
\quad\mathcal B_\psi(z)=\sum_i r_i\operatorname{Breg}_\psi(q_{z^i},q_z).
\]

即使 psi 凸，Bcal_psi 也可能有符号。由 Dq=u 的精确离散链式展开，

\[
D\psi(q)=u\psi'(q)+\mathcal B_\psi.
\]

定义

\[
\mathcal H=u\phi'(q)+\mathcal B_\phi,
\quad
\boxed{\mathcal G=u^2\phi''(q)+u\mathcal B_{\phi'}+D\mathcal B_\phi.} \tag{4.1}
\]

则 I_R''(u,0)=E Gcal。

### 4.1 余项完全展开

所有系数为

\[
r_i'=u^2(G^2)_{ii},\qquad q_{z^i}'=u(1+\|v_{z^i}\|^2),
\]
\[
\begin{aligned}
D\mathcal B_\phi={}&\sum_i r_i'\operatorname{Breg}_\phi(q_{z^i},q_z)\\
&+\sum_i r_i[(\phi'(q_{z^i})-\phi'(q_z))q_{z^i}'-\phi''(q_z)d_iq_z']\\
&+\sum_jr_j[\mathcal B_\phi(z^j)-\mathcal B_\phi(z)].
\end{aligned}                                             \tag{4.2}
\]

结合 (3.4)，只需原 word 与一次/二次翻位，无须重新计算外层完整 Hessian。

### 4.2 独立位反项

直接微分 phi''(q)=1/[2q^2(1-q)^2]，phi''(1/2)=8。定义

\[
\mathcal R=u^2(\phi''(q)-8)+u\mathcal B_{\phi'}+D\mathcal B_\phi.
\]

有限 R 精确地

\[
\boxed{A_R''(0)=4(1-N^{-2})+\int_{1/N}^1E\mathcal R\,{du\over u}.} \tag{4.3}
\]

这是明确局部量的指定组合，不把 A_R'' 本身定义为 remainder。c=0 时 b=0、全部 d_i=0、Rcal=0，恢复独立 Bernoulli。

## 5. P2：固定层坐标的有限边界通量

F_z=F((|z|-R)/sqrtR) 不依赖 delta。对 (2.4) 连用两次，L 固定，得到

\[
\boxed{{d^2\over d\delta^2}E[F\phi(q)]
 =E[F\mathcal G+2\mathcal H LF+\phi(q)L^2F].}              \tag{5.1}
\]

交叉运输 2Hcal LF 必须保留。没有层内独立或固定层权重假设。

对计数测试数组 F_m，

\[
(LF)_m=u[(n-m)(F_{m+1}-F_m)+m(F_m-F_{m-1})],
\]
\[
(L^2F)_m=u^2[(n-m)(n-m-1)\Delta^2F_m
 +2m(n-m)\Delta^2F_{m-1}+m(m-1)\Delta^2F_{m-2}].           \tag{5.2}
\]

L_i^2=0，不同位 L_i 交换，所以二阶式是有序双删除差分。边缘越界项系数为零。

中心带指示函数的 LF 只支持一步边界，L^2F 只扩展到两步边界。补带 1-F 的两个通量恰取反。**F=1 时两项运输在每个 word 上严格为零**，不需要极限高斯积分为零。

第 6 节证明 Gcal 有一致可积界。因此题面已接受的中心/补带 order-R 曲率完全位于这些显式边界运输中；有界内部项除以 R 消失。已有主阶定理仅用于辨认通量极限，不参与完整余项有界性的证明。

## 6. P3：带权双翻位估计与维度无关的曲率

设 a=epsilon^{-1}>=2、ell=||b||<=1/2、V=||v_z||、L=a ell。全部 word 上 V<=L，o_i,o_i^{-1}<=a，|r_i|<=ua。

### 6.1 一次跳跃及其参数变化

由 (3.4)，

\[
\sum_i|d_i|\le aV^2,\qquad\sum_i d_i^2\le a^2V^4.        \tag{6.1}
\]

令 t=Gv，微分得到

\[
d_i'=u[-{2\sigma_i\over o_i}\operatorname{Re}(v_i\bar t_i)
              +{|v_i|^2(G^2)_{ii}\over o_i^2}].           \tag{6.2}
\]

于是

\[
\sum_i|d_i||d_i'|\le u(2a^3+a^5)V^4\le2ua^5V^4.         \tag{6.3}
\]

第一项用 sum |v_i|^3|t_i|<=||v||^3||t||<=aV^4；第二项用 (G^2)_ii<=a^2、sum |v_i|^4<=V^4，无维数因子。

### 6.2 双翻位的连通权重

i!=j 时

\[
r_i(z^j)-r_i(z)={u\sigma_j\over o_j}|G_{ij}|^2,
\quad |r_i(z^j)-r_i(z)|\le ua|G_{ij}|^2.                  \tag{6.4}
\]

令 e_ij=d_i(z^j)-d_i(z)。同时更新 v_i 与 o_i：

\[
v_i(z^j)=v_i-{\sigma_j\over o_j}G_{ij}v_j,
\quad o_i(z^j)=o_i-{\sigma_i\sigma_j\over o_j}|G_{ij}|^2.
\]

更新前后的赔率逆均 <=a，故

\[
\boxed{|e_{ij}|\le2a^2|G_{ij}||v_i||v_j|
 +a^3|G_{ij}|^2(|v_i|^2+|v_j|^2).}                         \tag{6.5}
\]

没有 G_ij 就没有交叉影响，每条连通路径还带中心响应。进一步

\[
\sum_{i\ne j}|d_i||e_{ij}|\le(2a^4+2a^6)V^4,             \tag{6.6}
\]
\[
\sum_{i\ne j}|e_{ij}|^2\le(12a^6+6a^{10})V^4.            \tag{6.7}
\]

(6.6) 的线性核用 sum_ij |Gij||vi|^3|vj|<=aV^4，平方核用行平方和 <=a^2。(6.7) 将 (6.5) 三项平方以三倍平方和控制，再用 sum_j|Gij|^4<=a^4。

D_ij=max(|d_i(z)|,|d_i(z^j)|)<=|d_i|+|e_ij|，故

\[
\boxed{\sum_{i\ne j}D_{ij}|e_{ij}|\le8a^{10}V^4.}         \tag{6.8}
\]

使用 2a^4+14a^6+6a^10<=8a^10，a>=2。

**关键区别：** 裸 sum_ij |e_ij| 一般不能仅靠算子范数避免维数损失。Bregman 差分实际提供的 D_ij 权重使 (6.8) 成立；本文没有宣称裸双差分和也一致有界。

### 6.3 Bregman 变化

暂取一般 psi in C^4，M_k=sup_[epsilon,1-epsilon]|psi^(k)|，k=2,3,4。B_i=Breg_psi(q+d_i,q)。Taylor 余项给出

\[
|B_i|\le M_2d_i^2/2,\quad
|B_i'|\le M_3d_i^2|q'|/2+M_2|d_i||d_i'|.                 \tag{6.9}
\]

在 (q,d_i) 与 (q+d_j,d_i+e_ij) 之间线段插值，全部后验端点及插值均合法，因此

\[
|B_i(z^j)-B_i(z)|\le M_3|d_j|D_{ij}^2/2+M_2D_{ij}|e_{ij}|. \tag{6.10}
\]

且

\[
\sum_{i\ne j}|d_j|D_{ij}^2\le2a^3L^6.                    \tag{6.11}
\]

因为固定 j 时，原 word 与翻位 word 各自 sum_i d_i^2<=a^2L^4，再用 sum_j|d_j|<=aL^2。

### 6.4 支付三个曲率项

由上式、r_i'=u^2(G^2)_ii、q'<=u(1+L^2)，

\[
|\partial_\delta\mathcal B_\psi|
 \le u^2L^4[M_2(a^4/2+2a^6)+M_3a^3(1+L^2)/2],            \tag{6.12}
\]
\[
|u\mathcal B_{\psi'}|\le u^2M_3a^3L^4/2.                \tag{6.13}
\]

对 i!=j，分解

\[
r_i(z^j)B_i(z^j)-r_i(z)B_i(z)
 =[r_i(z^j)-r_i(z)]B_i(z)+r_i(z^j)[B_i(z^j)-B_i(z)].
\]

第一部分用 (6.4)、第二部分用 (6.8)、(6.10)–(6.11)。i=j 不套双翻位公式，直接界为 uaM_2 d_i^2。于是

\[
\sum_j|\mathcal B_\psi(z^j)-\mathcal B_\psi(z)|
 \le u[M_2(a^3+a^5/2+8a^{11})L^4+M_3a^4L^6],             \tag{6.14}
\]
\[
|T\mathcal B_\psi|\le u^2[9M_2a^{12}L^4+M_3a^5L^6].     \tag{6.15}
\]

没有 n；这是真正的结构子估计，不是再次引用 o(R)。

### 6.5 一般后验函数的比较

定义 Gcal_psi=u^2psi''(q)+u Bcal_(psi')+D Bcal_psi。合并得

\[
|\mathcal G_\psi-u^2\psi''(q)|
 \le u^2L^4[10M_2a^{12}+M_3(a^3+2a^5L^2)]
 \le u^2\ell^4(10M_2a^{16}+M_3a^{11}).                   \tag{6.16}
\]

塔性质 Eq=h 和 |q-h|<=a ell^2 给出真正中心化的 Taylor 界

\[
|E\psi''(q)-\psi''(h)|\le M_4a^2\ell^4/2.
\]

因此

\[
\boxed{|\partial_\delta^2E\psi(q)-u^2\psi''(h)|
 \le u^2\|b\|^4(10M_2a^{16}+M_3a^{11}+M_4a^2/2).}        \tag{6.17}
\]

量词：任意有限维数、任意满足共同谱隙的 Hermitian DPP 核、任意中心、固定对角速度 u，在评价点成立。无需投影、平移不变或层内均匀。

### 6.6 专门化到 phi

D0=q(1-q)，直接微分

\[
\phi''={1\over2D_0^2},\quad
\phi'''={2q-1\over D_0^3},\quad
\phi''''={2\over D_0^3}+{3(2q-1)^2\over D_0^4}.
\]

D0>=epsilon/2，可取 M2<=2a^2、M3<=8a^3、M4<=56a^4。于是

\[
|I''-u^2\phi''(h)|\le u^2\ell^4(20a^{18}+8a^{14}+28a^6)
 \le21a^{18}u^2\ell^4.                                  \tag{6.18}
\]

h=1/2 时 phi'''(h)=0，中心化 Taylor 界不必先取期望，因此更强地

\[
\boxed{|\mathcal G(z)-8u^2|\le21\epsilon^{-18}u^2\|b\|^4
\quad\hbox{每个 word}.}                                  \tag{6.19}
\]

### 6.7 原题 u 因子和积分

在 delta=0，h=1/2、epsilon(u)=(1-cu)/2>=epsilon_c、||b||<=cu/2。最后一式来自 Fejer 符号是 [0,1] 值正压缩、中心对角为 1/2。Fejer 核非负、积分 1，所以它的平滑确为合法真实核。

\[
\boxed{|\mathcal R(z)|\le{21c^4\over16\epsilon(u)^{18}}u^6
 \le C_cu^6,\quad C_c={21c^4\over16\epsilon_c^{18}}.}      \tag{6.20}
\]

保留原 du/u 权重，积分得 C_c(1-N^-6)/6，即 (1.2)。固定测试函数内部项还满足

\[
\left|\int_{1/N}^1E[F\mathcal G]{du\over u}\right|
 \le\|F\|_\infty[4(1-N^{-2})+C_c(1-N^{-6})/6].            \tag{6.21}
\]

### 6.8 严格但很窄的小噪声区

令 x=cu。x<=1/32 时

\[
|\mathcal R|/u^2\le21\,2^{14}{x^4\over(1-x)^{18}}
 \le{21\over64}(32/31)^{18}<{21\over32}.
\]

最后由整数幂比较 (32/31)^18<2。因此

\[
I_R''(u,0)\ge235u^2/32>0\quad(cu\le1/32).               \tag{6.22}
\]

对 R 一致，但原积分还需 u>=1/N，交集可能为空；不能由此判整个 A_R''。

同一合法符号辅助延拓到 0<=u<=1 后，原定义下限仍不变，单独截去的小 u 段满足

\[
\left|\int_0^{1/N}I_R''(u,0){du\over u}-4N^{-2}\right|
 \le C_c/(6N^6).                                         \tag{6.23}
\]

这是小 u 截断误差，不是整个 Fejer/体积误差。

## 7. 固定 R 的小 u 局部系数

这不是 R 渐近拟合，也不是一致可积的幂级数。固定 R，暂将 h,u 分开，K=hI+uH，H=c(Q_R-I/2)，a_i=H_i0，S_R=sum_i|a_i|^4。原导数仍为 partial_delta=u partial_h，在 h=1/2 评价。

Schur 补给出 q-h=-u^2 a*(hI-diag(1-z)+uH_C)^-1 a。先用 E(q-h)=0 中心化。u=0 时真实外部位才是独立 Bernoulli(h)；逆对角元均值 0、平方均值 1/[h(1-h)]，故

\[
E_{h,0}(a^*(hI-\operatorname{diag}(1-z))^{-1}a)^2
 ={S_R\over h(1-h)}.
\]

有限概率和后验在 (h,u)=(1/2,0) 邻域解析，得

\[
\mathcal I(h,u)=\phi(h)+{S_Ru^4\over4[h(1-h)]^3}+O_R(u^5).
\]

余项在固定复 h 邻域解析且一致，故 Cauchy 公式支付两次 h 导数，不是微分仅有实值控制的误差。该有理系数的二阶 h 导数在 1/2 为 384。又由取补集，Ical(h,u)=Ical(1-h,-u)，故在 h=1/2 的二阶 h 导数是 u 的偶解析函数。于是

\[
\boxed{I_R''(u,0)=8u^2+384S_Ru^6+O_R(u^8).}              \tag{7.1}
\]

题目核给出

\[
S_R={2c^4\over\pi^4}\sum_{1\le k\le R,\ k\ {
m odd}}
 {(1-k/N)^4\over k^4}\longrightarrow c^4/48,
\quad384S_R\longrightarrow8c^4.                           \tag{7.2}
\]

用 sum_(k odd)k^-4=pi^4/96（可由 Fourier–Parseval 推导）。**未证明** O_R(u^8) 常数对 R 一致，不能把级数积分到 u=1 或据此判号。小 u 辅助延拓不是原积分域的替换。统一界和 R 极限各有独立证明。

## 8. 真实 R=1 检查与合法负分量

### 8.1 8 个真实原子

R=1，按 (-1,0,1) 排列，

\[
K=\begin{pmatrix}h&k&0\\k&h&k\\0&k&h\end{pmatrix},
\quad h=1/2+u\delta,\quad k=uc/(2\pi),\quad u\in[1/2,1].
\]

只在这个最小模型中，外部两位独立。8 个联合行列式给出

\[
w_z=h^{|z|}(1-h)^{2-|z|},\quad
q_z=h-k^2\sum_{i=1}^2{1\over h-(1-z_i)}.                  \tag{8.1}
\]

t=4k^2=c^2u^2/pi^2、q+=1/2+t，记 F=phi(q+)、P=phi'(q+)、D0=phi''(q+)。delta=0 时四个外部 word 概率均为 1/4，同号后验为 1/2±t，异号为 1/2，

\[
q_z'=u(1+2t),\quad q_z''=-4u^2t\sum_i\sigma_i,
\quad r_i=-u\sigma_i,\quad r_i'=4u^2.
\]

完整 jets 及通量两式均给出

\[
\boxed{I_1''/u^2=4F-4(1+t)P+(1+2t)^2(D_0+8)/2.}          \tag{8.2}
\]

符号 Taylor 展开为 8+48t^2+(128/3)t^3+O(t^4)，不是拟合。

这个最小模型的总和还可直接判正。令 x=2t in (0,1)，

\[
I_1''/(4u^2)={1\over(1-x)^2}+(1+x)^2
 -{2x+x^2\over1-x^2}-\log{1+x\over1-x}.
\]

其常数为 2，一次项 0，二次项 3x^2；偶数 k>=4 的系数为 k，奇数 k>=3 的系数为 k-1-2/k>0。绝对收敛级数给出

\[
I_1''\ge8u^2+48t^2u^2>0,\qquad
A_1''>3+{63c^4\over8\pi^4}.                               \tag{8.3}
\]

只证明 R=1，不提供成长体积判号。

脚本 `small_check_r1.py` 实际执行通过：8 个联合原子、Schur 后验、全部 u 因子、通量伴随、Dq=u、任意形式函数 jets 的二阶恒等式、任意固定测试数组的边界分解。把各 word 的 phi/phi'/phi'' 值先作独立形式符号配系数，避免错误对数分支化简。

`check_resolvent_algebra.py` 只用两个相互作用外部位核对矩阵翻位、能量、DG=0 及 P-A=T；不是实际 Fejer 模型的替代，也未用于推断符号。

### 8.2 DISPROVED：正耗散闭合

令 B_t=t phi'(1/2+t)-phi(1/2+t)。B0=0，B_t'=t phi''(1/2+t)>0，所以合法 t>0 时 B_t>0。直接计算

\[
\mathcal B_\phi(00)=2uB_t,\quad\mathcal B_\phi(11)=-2uB_t,
\quad\mathcal B_\phi(01)=\mathcal B_\phi(10)=0,
\]
\[
\boxed{T\mathcal B_\phi=-4u^2B_t<0\quad\hbox{逐 word}.}  \tag{8.4}
\]

所以 E[T Bcal_phi]>=0 的规则被任务内真实 Fejer DPP 否定。不能迁移正 Markov 半群的耗散符号。这不是总 A_R'' 的反例，也不否定大 R 中心带的已给渐近结论。

## 9. 状态和精确缺口

PROVED：实际 word 双通量、Dq=u、DG=0；完整/加权二阶身份；中心/补带有限边界抵消；带权连通估计；所有正奇数 R 的 O_c(1) 界；固定 R 小 u 系数；真实 R=1 的总正性及负分量；两个附录中的有限极限、实际律变化和保守有效余项。

DISPROVED：将 T Bcal_phi 当作非负耗散的闭合规则，仅在其明确形式下被否定。

INCOMPLETE：Gamma(19/20) 的符号；一般 R 的 A_R''>=0；最优/尖锐误差与首个非零更细项；固定 R 小 u 级数余项的一致性；从 J_R 到真实熵率的导数或固定弦桥接。

完整判号真正剩下的是

\[
\int_{1/N}^1E\mathcal R\,{du\over u}\ge-4(1-N^{-2}),
\]

或极限中 Gamma(c)>0 的有符号下界。Rcal 必须用 (4.2) 的实际核，不能以绝对值估计、小噪声正性或单个分量符号替代。

下一步不必数值相减两个 order-R 带贡献；应研究有界、带符号、具有已证局部稳定性的核的真实期望。附录支付极限及一个保守误差，但不自动给出符号，更不把 Gamma 未经证明称为真实熵率的负 Hessian。

## 10. 计算交接（重型工作未执行）

对给定 (R,u,z)，一次求 G_z，随后用秩一式生成所有 q_(z^j)、q'_(z^j)、r_i(z^j)、d_i(z^j)。局部核可用矩阵分解后的一次/二次条目运算求得；主要困难是实际 word 期望和积分认证。

输入严格取 c=19/20、正奇数 R、u in [1/(R+1),1]、delta=0 的真实 Toeplitz Fejer 完整律。分别记录 u^2(phi''-8)、u Bcal_(phi')、partial_delta Bcal_phi、T Bcal_phi 的期望。核对原始完整 jets 与抵消式；不能换成谱 Bernoulli word。

待区分：总残差是否同号；正项是否支付负通量；带权能量是否显著改善 epsilon^-18 最坏常数。一个分量负不否定总和，一些有限 R 正也不证明成长结论。

等式检查应精确符号或认证区间；有限 R 判号需要包含全部分量和 u 积分误差的最终区间严格离开 0。浮点仅为诊断。渐近拟合不替代余项证明。未执行大规模枚举、密集扫描、长优化、高精度批量认证或旧 S7 证书重算。

## 参考与输入范围

[T03] 本分支 `research_prompts/pro_tasks/TASK_03_S9_SUBLEADING_RESIDUE.md`：固定对象、P1–P3、允许直接使用的主阶结论。

[CS] `research_prompts/pro_tasks/COMMON_STARTER.md`：公共计数运输和完整导数接口；其原有身份不单独计作本次进展。

[AUD] `research_prompts/pro_tasks/sources/S9_AUDIT.md`：旧 S9 审核范围，不覆盖本文新推导。

[BRA] Anton Braverman, *The prelimit generator comparison approach of Stein's method*, arXiv:2102.12027v4 (2021)。迁移有限尺度中心化机制，不借用队列估计作为 DPP 定理。

[CHA] Djalil Chafai, *Binomial-Poisson entropic inequalities and the M/M/∞ queue*, ESAIM Probability and Statistics 10 (2006), 317–339；arXiv:math/0510488v2，Phi-calculus 部分。只迁移离散链式缺陷，不迁移正耗散结论。

外部文献作了针对性机制核查，未完成全面新颖性检索。本文所有 PROVED 均附自包含推导，仍需独立审核。
