# S63 Cycle13 visible reply receipt

Source: Say S63; thread 6aad30ba-88f4-83e8-ba3e-4bb5c2da4393.
Status: AUTHOR_ONLY, independent review not yet complete. Complete visible reply recovered; downloadable attachments NOT received. Attachment placeholders are not files. Received 2026-09-19 Singapore.

---

# S63 第二轮结果：普通密度、离开平衡点的真分布区间定理

这轮得到的不再是“保留一个未支付的广延余项”的恒等式，而是一个**已经闭合的、体积一致的真分布负曲率子区间定理**。

**PROVED——计算机辅助证明，严格限定作用域。** 对实际正弦 Toeplitz 压缩，取
\[
\rho=\frac13,\qquad c=\frac{19}{20},\qquad
J=\left[\frac{21}{1000},\frac3{125}\right]=[.021,.024].
\]
对每个整数 \(n\ge22\)，完整配置 Shannon 熵满足
\[
\boxed{
H_n''(a)\le-\frac{n}{25}+399
\qquad\text{对所有 }a\in J.
}
\tag{T}
\]
因此，实际熵率存在，并且
\[
\boxed{
\operatorname{Gap}_{\lambda}h_{1/3,19/20}
\ge
\frac1{50}\lambda(1-\lambda)(a_1-a_0)^2
}
\tag{C}
\]
对所有 \(a_0,a_1\in J\)、\(0\le\lambda\le1\) 成立。

**原要求的整个 \([.02,.03]\)：INCOMPLETE。** 上述 \(J\) 是宽度为 \(.003\) 的真子区间，不含平衡点 \(.025\)。不能把这个结果说成整个基准区间、整个合法区间或任意密度的全局定理。

:chatgpt-content-reference{index="5"}

以下给出证明主体、有限证书的确切接口，以及剩余缺口。所有对数均为自然对数。

---

## 1. 依赖与结论账本

状态文件仍将通用全区间基线限定为 \(c\le37/40\)；SA02 没有给出 \(c=.95\) 的判号；S55 的桥只在半密度成立；S61 已完成的是指定半密度、修正时钟下的冻结任务，不包括这里的普通密度真分布结论。citeturn902882view0

本轮实际使用的已审查接口，是 SA02 的有限真分布得分恒等式和条件得分鞅；下面重新推导需要的部分，固定有序／无序配对和概率权重的归一化。citeturn902882view1

| 本轮命题 | 状态 | 作用域 |
|---|---|---|
| 保留两种似然比的后验算子序界 | **PROVED** | 普通密度；实际观测分布 |
| 条件四原子表的一维全局包络 | **PROVED** | 明确的条件概率区间假设 |
| 半正定 Fisher 分配与局部变分支付工具 | **PROVED** | 有限严格通道 DPP；无遗漏的有符号配对 |
| 实际概率向量的幂零多项式演化 | **PROVED** | 保留全部移动概率权重 |
| 本文三个有限证书 | **PROVED，计算机辅助** | 连续参数区间和全部局部配置 |
| 定理 (T)、(C) | **PROVED，严格部分结果** | \(\rho=1/3,c=.95,a\in[.021,.024]\) |
| 整个 \([.02,.03]\) 基准 | **INCOMPLETE** | 两侧剩余区间尚未闭合 |
| 最终所有 \(\rho,c,a\) 的目标 | **INCOMPLETE** | 本文没有给出全局判号 |

这些是本轮提交的证明，不冒充已经获得独立审查接受的仓库结论。

## 2. 精确使用真 Toeplitz 分布，而不是近似转移

令 \(Q\) 为 \(\ell^2(\mathbb Z)\) 上的无限正弦投影，\(Q_{ii}=\rho\)。它是 Fourier 变换下区间指标函数的乘法算子。令
\[
X\sim\operatorname{DPP}(Q),
\]
并在给定 \(X\) 后独立生成
\[
\Pr(Y_i=1\mid X)=a+cX_i.
\]
记
\[
u=a,\quad v=a+c,\quad
d_+=\frac vu,\quad d_-=\frac{1-v}{1-u},
\]
\[
\beta_0=u(1-u),\qquad \beta_1=v(1-v).
\tag{2.1}
\]

对任意有限集合 \(S\)，
\[
\begin{aligned}
\mathbb E\prod_{i\in S}Y_i
&=\sum_{T\subseteq S}a^{|S|-|T|}c^{|T|}\det Q_T\\
&=\det(aI+cQ)_S.
\end{aligned}
\]
所以，对任意有限体积 \(V\)，
\[
Y_V\sim\operatorname{DPP}(aI+cQ_V)
\tag{2.2}
\]
**恰好就是实际 Toeplitz 输出分布**。

这里的投影是无限 \(Q\)，不是有限压缩 \(Q_V\)。有限压缩仅满足
\[
0\preceq Q_V\preceq I.
\]
这条路线没有把有限压缩的泄漏删掉：未观察的无限坐标保留在潜在模型中。因此无需先证明循环模型，再猜测循环到真分布的误差。

### 两种不相等噪声的共同 Fisher 预算

完整数据得分为
\[
S=\sum_{i\in V}
\frac{Y_i-(u+cX_i)}
{(u+cX_i)(1-u-cX_i)}.
\]
给定 \(X\)，各项独立且中心化。实际输出得分是 \(\mathbb E[S\mid Y]\)，故
\[
\boxed{
J_V\le |V|\,d_{\rho,c}(a),\qquad
d_{\rho,c}(a)
=\frac{1-\rho}{\beta_0}+\frac{\rho}{\beta_1}.
}
\tag{2.3}
\]
这约束的是**共同平移 Fisher 信息**，不是计数 Fisher 信息，也不是对角 Fisher 信息。

把普通密度的偏置项显式写出。设
\[
a_*=\frac{1-c}{2},\quad s=a-a_*,
\quad b=\frac{1-c^2}{4},\quad B=b-s^2.
\]
则
\[
\beta_0=B+cs,\qquad \beta_1=B-cs,
\]
以及
\[
\boxed{
d_{\rho,c}(a)
=\frac{B+c(2\rho-1)s}{B^2-c^2s^2}.
}
\tag{2.4}
\]
其中奇项 \(c(2\rho-1)s\) 只有在半密度或平衡点消失。后面的证书支付的是整个有理函数 (2.4)，没有把该项设为零。

## 3. 普通密度的后验序界

观察有限个 \(Y_j\) 后，潜在分布的似然权重为
\[
\prod_j D_j^{X_j},
\qquad
D_j=
\begin{cases}
d_+,&Y_j=1,\\
d_-,&Y_j=0,\\
1,&j\text{ 未观察}.
\end{cases}
\]
令 \(\mathcal H=\operatorname{Ran}Q\)，并在此空间上定义
\[
M_D=(QDQ)|_{\mathcal H}.
\]
因为 \(d_-I\preceq D\preceq d_+I\)，该算子严格正且可逆。实际后验核为
\[
\boxed{
P_D=D^{1/2}Q M_D^{-1}Q D^{1/2}.
}
\tag{3.1}
\]
它是到 \(D^{1/2}\mathcal H\) 的正交投影。

这不仅是代数候选。对有限似然支撑及额外测试坐标使用 DPP 生成行列式，再除以似然归一化常数；利用 \(\det(I+AB)=\det(I+BA)\)，所得生成行列式正是 (3.1)。这里涉及的扰动都只有有限支撑。

### 单点界

保留目标点 \(i\) 未观察。其潜在后验占据率是
\[
\langle Qe_i,M_D^{-1}Qe_i\rangle.
\]
用所有其他字段分别取 \(d_+\)、\(d_-\) 的两个算子比较 \(M_D\)，再应用逆算子序及秩一逆公式，得到
\[
\boxed{
L_*(a)
=a+c\frac{\rho}{\rho+d_+(1-\rho)}
\le \Pr(Y_i=1\mid\text{其他观察})
\le
a+c\frac{\rho}{\rho+d_-(1-\rho)}
=U_*(a).
}
\tag{3.2}
\]
该界对所有有限体积、所有实际观察词同时成立。

### 带局部观察的两点界

设目标对 \(T=\{i,j\}\)，局部观察集合 \(O\) 与目标对不交，\(E=T\cup O\)。固定观察词 \(z\)，在 \(T\) 上取字段 \(1\)，在 \(O\) 上按 \(z\) 取 \(d_+\) 或 \(d_-\)。定义
\[
\mathcal B_d(E,z)=
\left[
Q_E\{dI+(D_E-dI)Q_E\}^{-1}
\right]_{T,T}.
\tag{3.3}
\]
实际潜在后验的两点压缩 \(B_T\) 满足
\[
\boxed{
\mathcal B_{d_+}(E,z)\preceq B_T
\preceq\mathcal B_{d_-}(E,z).
}
\tag{3.4}
\]

证明是将 \(E\) 之外的未知字段分别放到其上下极值，再应用逆算子序。公式 (3.3) 来自
\[
A(dI+A^*HA)^{-1}A^*
=Q_E(dI+HQ_E)^{-1},
\qquad AA^*=Q_E.
\]
这里不要求 \(Q_E\) 是投影或可逆。

无限坐标上的常数字段只用于**有界比较算子**，并没有被解释为一个正概率的无限观察事件。

两种字段 \(d_+(a)\)、\(d_-(a)\) 都随 \(a\) 递减，故两个后验界都随 \(a\) 按 Loewner 序递增。在参数小区间 \([a_-,a_+]\) 上，
\[
\mathcal B_{d_+(a_-)}(a_-,z)
\preceq B_T(a)
\preceq
\mathcal B_{d_-(a_+)}(a_+,z).
\tag{3.5}
\]
这给出的是直接覆盖连续区间的统一界，不是固定 \(n\) 连续性推断。

## 4. 条件四原子表的全局包络

将一个实际条件两点表记为
\[
A=p_{00},\quad B=p_{10},\quad C=p_{01},\quad D=p_{11},
\]
并令
\[
s=BC-AD\ge0.
\]
定义
\[
\alpha=
\frac{\log(BC/AD)}
{s(A^{-1}+B^{-1}+C^{-1}+D^{-1})},
\tag{4.1}
\]
在独立极限处取连续值 \(1\)。

令 \(R=BC/(AD)\)、\(d=A+D\)。直接通分得
\[
\boxed{
\alpha=
\frac{R\log R}{(R-1)\{1+d(R-1)\}}.
}
\tag{4.2}
\]

假设四个单点条件概率均在 \([L,U]\)，其中 \(L<1/2<U\)。置
\[
\ell=\frac L{1-L},\qquad r=\frac U{1-U}.
\]
则
\[
B,C\le rA,\qquad D\ge\ell B,\ell C.
\]
由此得到
\[
\boxed{
\alpha\le
\max\left\{
1,\ 
\sup_{1\le R\le\min(r^2,\ell^{-2})}
\frac{R\log R(1+r+r\ell+\ell R)}
{(R-1)\{r+R(1+\ell+r\ell)\}}
\right\}.
}
\tag{4.3}
\]

**证明。** 交换两个点后，可取 \(C\ge B\)，再缩放为 \(B=1,C=t\ge1\)。固定 \(R\) 时，
\[
1\le t\le\frac r{\ell R},\qquad
A\ge\frac tr,\qquad D\ge\ell t,\qquad AD=\frac tR.
\]
最大化 \(\alpha\) 等价于最小化 \((A+D)/(1+t)\)。

若 \(r\ell\le1\)，先对 \(A\) 最小化：在未触碰约束时得到
\[
\frac{2\sqrt{t/R}}{1+t};
\]
触碰 \(A=t/r\) 后得到
\[
\frac{t/r+r/R}{1+t}.
\]
前者在 \(t\ge1\) 递减，后者导数的符号是 \(R-r^2\)。因此在
\(R\le\min(r^2,\ell^{-2})\) 的区间，两条约束同时饱和给出
\[
d\ge\frac{1+r\ell}{1+r+r\ell+\ell R}.
\]
\(r\ell>1\) 的情形交换两个对角原子即可。

在剩余可行 \(R\) 区间，最小值在 \(t=1\) 取得，进而
\[
d\ge\frac1{1+\sqrt R},\qquad
\alpha\le\frac{\sqrt R\log R}{R-1}\le1.
\]
最后一步来自 \(\log z\le(z-z^{-1})/2\)。证毕。

将 (3.2) 代入，有限连续区间证书证明，在整个 \(J\) 上所有实际条件对均满足
\[
\boxed{
\alpha\le C_0(a),\qquad
C_0(a)=\frac{261}{200}+\frac{51}{10}a.
}
\tag{4.4}
\]
这不是已知为假的“每对都由单位预算支付”。这里允许 \(C_0>1\)，并在下一步真正支付超出的部分。

## 5. 新工具：把有符号项整体装入半正定预算

对有限实际输出分布，引入独立对角参数 \(a_i\)，随后在 \(a_i=a\) 处取值。记
\[
G_V(y)=
\{K_V-\operatorname{diag}(1-y)\}^{-1},
\qquad Z_i=(G_V)_{ii},
\]
\[
F_V=\sum_i\mathbb E Z_i^2,\qquad
J_V=\mathbb E\left(\sum_iZ_i\right)^2.
\]

实际原子概率的行列式公式给出
\[
Z_i=\partial_{a_i}\log p,
\qquad
\partial_{a_i a_j}p
=p(Z_iZ_j-|G_{ij}|^2).
\]
对所有原子求和，得到
\[
\mathbb E Z_iZ_j=\mathbb E|G_{ij}|^2,
\]
以及
\[
J_V=F_V+\sum_{i\ne j}\mathbb E|G_{ij}|^2.
\tag{5.1}
\]

完整熵曲率为
\[
\boxed{
H_V''=
\sum_{i\ne j}
\mathbb E_{\mathrm{rest}}
\log\frac{p_{10}p_{01}}{p_{00}p_{11}}
-J_V.
}
\tag{5.2}
\]
这里的和是**有序对**。它直接来自
\[
H_V''=-\sum_y\frac{p'(y)^2}{p(y)}
-\sum_y p''(y)\log p(y),
\]
所以概率加速度并没有被删除。

对固定的 pair-rest 条件词，逆二阶矩阵公式给出
\[
\mathbb E[|G_{ij}|^2\mid\mathrm{rest}]
=s(A^{-1}+B^{-1}+C^{-1}+D^{-1}).
\tag{5.3}
\]
因此 \(\alpha\) 正是条件对数赔率项与该逆矩阵能量的比值。

### 输入接口

选择一些无序对 \(e=\{i,j\}\)。对每一对提供一个不含目标点的局部观察集合 \(O_e\)，以及非负、仅依赖这些观察的改进量 \(\delta_e\)，满足
\[
\alpha_e\le C_0-\delta_e(Y_{O_e}).
\]
再提供对角分配 \(w_{e,i},w_{e,j}\ge0\)，满足
\[
\sum_{e\ni i}w_{e,i}\le C_0,
\]
\[
B_e=
\begin{pmatrix}
w_{e,i}&\delta_e\\
\delta_e&w_{e,j}
\end{pmatrix}\succeq0.
\tag{5.4}
\]

对包含目标对及其局部观察的有限集合 \(A_e\subseteq V\)，输出接口是
\[
\boxed{
H_V''\le
(C_0-1)J_V
-\sum_e
\mathbb E\!\left[
Z_{A_e,e}^{\mathsf T}B_e Z_{A_e,e}
\right].
}
\tag{5.5}
\]

### 证明

由 (5.1)–(5.3)，
\[
H_V''\le
(C_0-1)J_V-C_0F_V
-2\sum_e\mathbb E[\delta_e|G_{ij}|^2].
\]
因为 \(\delta_e\) 不依赖两个目标位，对条件表应用归一化的混合二阶导数可得
\[
\mathbb E[\delta_e|G_{ij}|^2]
=\mathbb E[\delta_e Z_iZ_j].
\tag{5.6}
\]
这只是一条实际分布下的平均恒等式，**不要求逐词 \(Z_iZ_j\ge0\)**。

利用对角分配约束，
\[
H_V''\le
(C_0-1)J_V
-\sum_e\mathbb E[Z_{V,e}^{\mathsf T}B_eZ_{V,e}].
\]
同一参数族的边缘化给出得分鞅
\[
\mathbb E[Z_{V,e}\mid Y_{A_e}]=Z_{A_e,e}.
\]
由于 \(B_e\) 在该条件下可测且半正定，条件 Jensen 得到 (5.5)。被舍弃的差恰是
\[
\mathbb E\operatorname{Tr}
\!\left(B_e\operatorname{Cov}(Z_{V,e}\mid Y_{A_e})\right)\ge0.
\]

**这一步是新支付的关键。** 不再先对有符号势做局部化、再付巨大的观察域 Hessian 误差；而是先把交叉项和对角项组合成半正定二次型，然后整体条件化。每个站点的对角预算只花一次。

## 6. 变分版本与移动概率权重

令 \(f_e\) 是局部配置上的任意固定二向量函数。配平方给出
\[
Z^{\mathsf T}B_eZ
\ge
2Z^{\mathsf T}B_ef_e-f_e^{\mathsf T}B_ef_e.
\]
定义
\[
\Delta_i g=g(y_i=1)-g(y_i=0).
\]
由 \(\partial_{a_i}p(y)=(2y_i-1)\{p(y)+p(y^i)\}\)，
\[
\mathbb E_a[Z_i g(Y)]
=\mathbb E_a[\Delta_i g(Y)].
\]
因此可将局部二次型支付替换为
\[
\boxed{
P_e(a)=\mathbb E_a V_e(a,Y),
}
\]
\[
\boxed{
V_e=
2\{\Delta_i(B_ef_e)_i+\Delta_j(B_ef_e)_j\}
-f_e^{\mathsf T}B_ef_e.
}
\tag{6.1}
\]

这里始终以实际 \(p_a\) 取期望。\(f_e\) 固定只是变分测试函数固定，**不意味着把参考点的概率分布冻结**；整个推理是逐参数的配平方，不是对一个熵值比较式求二阶导数。

### 本轮的有限见证

取
\[
A=\{0,\ldots,21\},\qquad T=\{10,11\},
\]
\[
O=\{6,7,8,9,12,13,14,15\}.
\]
把该顺序的观察词编码为
\[
z=\sum_{r=0}^7 2^r y_{O_r}.
\]
对每个 \(z\)，提供整数对 \((L_z,U_z)\)，并定义
\[
c_z(a)=
\frac{(3/100-a)L_z+(a-1/50)U_z}{100},
\]
\[
\delta_z=C_0-c_z,\qquad
B_z=
\begin{pmatrix}
C_0/2&\delta_z\\
\delta_z&C_0/2
\end{pmatrix}.
\tag{6.2}
\]
完整的 256 对整数列在正文附录 A，输入文件也直接提供：
:chatgpt-content-reference{index="6"}。

证书证明了，在整个 \(J\) 上，
\[
\alpha_e\le c_z(a),\qquad
0\le\delta_z(a)\le C_0(a)/2.
\tag{6.3}
\]
后一个条件保证 \(B_z\succeq0\)。

取 \(a_*=1/40\)，测试函数为实际 22 点分布的两个局部得分：
\[
f_i(y)=(2y_i-1)
\left(1+\frac{p_{a_*}(y^i)}{p_{a_*}(y)}\right),
\qquad i=10,11.
\tag{6.4}
\]
由于 \(B_z\) 关于 \(a\) 仿射，
\[
V(a,y)=V_0(y)+(a-a_*)V_1(y).
\]

### 实际分布的精确多项式演化

在完整概率向量上定义
\[
(D_i p)(y)=(2y_i-1)\{p(y)+p(y^i)\}.
\]
这些算子满足
\[
D_i^2=0,\qquad D_iD_j=D_jD_i,\qquad
\|D_i\|_{1\to1}=2.
\]
令 \(D=\sum_{i=0}^{21}D_i\)，则多重仿射性给出精确恒等式
\[
\boxed{
p_{a_*+h}
=\prod_i(I+hD_i)p_{a_*}
=e^{hD}p_{a_*}
=\sum_{k=0}^{22}\frac{h^k}{k!}D^kp_{a_*}.
}
\tag{6.5}
\]

这保留了实际概率的一阶变化、二阶加速度以及所有更高阶项。

全配置验证给出
\[
\|V_0\|_\infty\le1500,\qquad
\|V_1\|_\infty\le10000.
\tag{6.6}
\]
令 \(t=200a-5\)，把概率展开截到 \(k=8\)。在 \(|a-a_*|\le1/200\) 上，总余项不超过
\[
1550\,
\frac{(11/50)^9}{9!}
\frac1{1-(11/50)/10}
<10^{-8}.
\tag{6.7}
\]
证明中保守地使用 \(10^{-6}\)。

这是完整概率向量的范数尾界，没有“典型词之外忽略不计”的步骤。

## 7. 有限证书如何形成证明

### 7.1 全局条件表证书

用 60 个闭参数小区间覆盖 \(J\)，每段长度 \(1/20000\)。在每段使用
\[
[L_*(a_-),U_*(a_+)]
\]
扩大的条件概率区间，以及 \(C_0(a_-)\) 这个较小上限。

在当前参数下 \(\ell r<1\)，因此 (4.3) 的非平凡范围是 \(1\le R\le r^2\)。对整个范围做向外舍入的区间细分。全部 **60 段通过，累计 11,364 个区间盒**。

具体上界并不依赖数值极值求解器。设
\[
x=R-1,\qquad
\mathcal L(x)=\frac{(1+x)\log(1+x)}x.
\]
因为
\[
\mathcal L'(x)=\frac{x-\log(1+x)}{x^2}\ge0,
\]
在盒 \([x_-,x_+]\) 上，可用
\[
\frac{\mathcal L(x_+)}{1+d_-x_-}
\]
作为上界，其中 \(d_-\) 是 (4.3) 所给对角原子和的下包围值。不足以证明的盒继续二分，不会被接受。

### 7.2 全部局部观察词的连续证书

对 256 个观察词，以及覆盖 \(J\) 的 6 个长度为 \(1/2000\) 的闭参数区间，分别用 (3.5) 计算后验 Loewner 界 \(L,U\)。

对所有实对称矩阵
\[
B=
\begin{pmatrix}m_1&w\\w&m_2\end{pmatrix},
\qquad L\preceq B\preceq U,
\]
验证其输出表满足
\[
\alpha(B,a)\le \min_{\text{参数小区间}}c_z(a).
\]

三个变量的区间验证保留了
\[
(m_1-L_{11})(m_2-L_{22})\ge(w-L_{12})^2,
\]
\[
(U_{11}-m_1)(U_{22}-m_2)\ge(w-U_{12})^2.
\tag{7.1}
\]
在剩余盒中，取
\[
q=a+cm_1,\quad r=a+cm_2,\quad s=c^2w^2,
\]
\[
A=(1-q)(1-r)-s,\qquad D=qr-s.
\]
实际通道的每个原子至少为
\[
\min(a,1-a-c)^2,
\]
故可将这个正下界与原子区间相交。再由
\[
x=\frac{s}{AD},\qquad d=A+D,\qquad
\alpha=\frac{\mathcal L(x)}{1+dx}
\]
得到盒上界。

**全部 \(256\times6=1,536\) 个观察词／参数段通过。** 加强舍入后的重跑处理了 **66,610,050 个盒，没有未证明的剩余盒**。

### 7.3 完整实际 22 点概率

在参考点定义
\[
K_*=\frac1{40}I+\frac{19}{20}Q_{1/3,22},\qquad
L_*=K_*(I-K_*)^{-1}.
\]
每个实际原子均按
\[
p_{a_*}(y)=
\det(I-K_*)\det(L_*)_{\{i:y_i=1\}}
\tag{7.2}
\]
包围计算。

计算使用带溢出检测的整数定点区间，保留 192 个二进制小数位。通过“删除首坐标／纳入首坐标并取 Schur 补”的递归，覆盖全部
\[
2^{22}=4,194,304
\]
个配置；没有使用浮点 Gray-code 逆矩阵更新作为证明。

正弦输入只需要
\[
\alpha_0=\frac{\sqrt3}{2\pi}.
\]
使用的严格 60 位十进制包围是
\[
\frac{
275664447710896024755663249156484720698693240183320326399683
}{10^{60}}
<\alpha_0<
\frac{
275664447710896024755663249156484720698693240183320326399684
}{10^{60}}.
\]
这由 Machin 公式、反正切交错级数余项和有理平方比较验证，而不是接受数学库的正弦值。

得到
\[
P(a)=\mathbb E_aV(a,Y)
=\sum_{k=0}^{9}A_kt^k+R(a),
\qquad |R(a)|\le10^{-6},
\quad t=200a-5,
\tag{7.3}
\]
其中以下每个端点的共同分母均为 \(10^8\)：

| \(k\) | 下端点分子 | 上端点分子 |
|---:|---:|---:|
| 0 | 1776012226 | 1776012227 |
| 1 | -82943302 | -82943301 |
| 2 | -14608797 | -14608796 |
| 3 | -290978 | -290977 |
| 4 | 1734 | 1735 |
| 5 | -1 | 0 |
| 6 | -1 | 0 |
| 7 | 0 | 1 |
| 8 | 0 | 1 |
| 9 | -1 | 0 |

系数来自
\[
q_0=p_{a_*},\qquad
q_{k+1}=\frac{Dq_k}{200(k+1)},
\]
\[
c_k=\langle q_k,V_0\rangle,\qquad
b_k=\langle q_k,V_1\rangle,
\]
\[
A_0=c_0,\quad
A_k=c_k+b_{k-1}/200\ (1\le k\le8),\quad
A_9=b_8/200.
\]
因此全部权重移动均在被验证的有限运算中。

### 7.4 最终判号是精确有理证明

在 \(J\) 上，
\[
-\frac45\le t\le-\frac15.
\]
所以偶次幂取系数下端点、奇次幂取上端点，再减去 \(10^{-6}\)，即可得到 \(P\) 的下包络 \(\underline P(t)\)。

令
\[
D(a)=a(1-a)(a+c)(1-a-c)>0,
\]
并定义
\[
\begin{aligned}
\mathcal G(a)
={}&D(a)\{\underline P(200a-5)-1/25\}\\
&-(C_0(a)-1)
\left\{\frac23(a+c)(1-a-c)+\frac13a(1-a)\right\}.
\end{aligned}
\]
代入
\[
a=\frac{21}{1000}+\frac3{1000}x,\qquad 0\le x\le1.
\]
所得多项式为 11 次。其 12 个 Bernstein 系数均严格大于 \(1/40000\)。以下是它们的有理下界分子，共同分母为 \(10^9\)：
```text
29091 47114 61938 73573 82033 87328
89474 88485 84380 77175 66890 53546
```
计算使用精确分数。若 \(\mathcal G(x)=\sum_i g_ix^i\)，相应 Bernstein 系数为
\[
b_k=\sum_{i=0}^{k}
g_i\frac{\binom{k}{i}}{\binom{11}{i}}.
\]
Bernstein 基函数在 \([0,1]\) 非负且和为 \(1\)，故
\[
\boxed{
P(a)-(C_0(a)-1)d_{1/3,19/20}(a)
\ge\frac1{25}
\quad(a\in J).
}
\tag{7.4}
\]
同一系数表用 \(|t|\le4/5\) 的绝对系数界还给出
\[
\boxed{P(a)<19.}
\tag{7.5}
\]

这两条是不依赖网格判号的连续区间证书。

## 8. 完成任意体积与真熵率证明

在 \(V=[n]\) 中，对每个完整落在体积内的平移 22 点窗口，选择其中央相邻对。共有
\[
n-21
\]
个这样的窗口。

每条边给两个端点各分配 \(C_0/2\)。每个站点最多属于两条选中边，故对角总预算不超过 \(C_0\)。由平稳性，每个局部变分支付都是同一个 \(P(a)\)。

应用 (5.5)、(6.1)、(2.3)：
\[
H_n''(a)
\le n(C_0(a)-1)d_{1/3,19/20}(a)-(n-21)P(a).
\]
再用 (7.4)、(7.5)：
\[
\begin{aligned}
H_n''(a)
&\le
-n\{P(a)-(C_0(a)-1)d_{1/3,19/20}(a)\}+21P(a)\\
&\le-\frac n{25}+399.
\end{aligned}
\]
这证明了 (T)。

**所有长距离配对已经在完整曲率式 (5.2) 中，经全局包络计入共同 Fisher 预算；没有被截断。** 唯一的有限边界损失，就是缺少的 21 个局部见证。

平稳性给出
\[
H_{n+m}(a)\le H_n(a)+H_m(a),
\]
所以 \(h(a)=\lim_n H_n(a)/n\) 存在。对有限体积曲率界积分，
\[
\operatorname{Gap}_\lambda H_n
\ge
\frac12\left(\frac n{25}-399\right)
\lambda(1-\lambda)(a_1-a_0)^2.
\]
除以 \(n\)，通过熵值极限，即得 (C)。

这里**没有**从值误差对 \(a\) 求二阶导数，也**没有**要求预先证明熵率 \(C^2\)。

### 可复用的输出形式

相同论证给出一个一般接口：对平稳实投影先验、任意固定严格通道参数区间，若一个 \(m\) 点相邻对见证满足上述全局包络、局部后验上界、半正定分配，并且
\[
(C_0-1)d_{\rho,c}+\varepsilon
\le P(a)\le M
\]
在整个参数区间成立，则
\[
\boxed{
H_n''(a)\le-\varepsilon n+(m-1)M
\qquad(n\ge m).
}
\]
对应熵率弦差的系数为 \(\varepsilon/2\)。

输入是明确的有限矩阵、局部观察上界、有限测试函数及有限期望证书；输出已经包含全部配对和边界支付。本轮取
\[
m=22,\qquad \varepsilon=1/25,\qquad M=19
\]
给出了一个真正闭合的实例。

## 9. 已支付的部分与精确剩余缺口

本轮已经支付了两种不相等噪声、普通密度奇项、实际条件表的有符号贡献、全部移动概率权重、全部局部配置、多项式尾、所有长距离配对，以及有限体积边界。投影性质只用于无限正弦先验；达到真 Toeplitz 法律是精确表示，达到熵率是有限弦差的值极限。

还有一个直接的 **PROVED** 推论：
\[
I-Q_{\rho,n}=UQ_{1-\rho,n}U^*,\qquad U_{ii}=(-1)^i,
\]
所以粒子补与对角酉规范变换给出
\[
H_{\rho,c,n}(a)=H_{1-\rho,c,n}(1-c-a).
\]
因此同样的定理适用于
\[
\rho=\frac23,\qquad a\in[.026,.029].
\]
它改变了密度，**不能**用来补上 \(\rho=1/3\) 的上侧区间。

**仍然 INCOMPLETE 的是**
\[
\rho=\frac13,\quad c=.95,\quad
a\in[.02,.021)\ \cup\ (.024,.03].
\]
本文没有提供覆盖这些参数的支付证书，更没有证明所有密度、对比度及合法端点的总目标。此次进展是在新的普通密度高对比度固定区间上闭合完整曲率，而不是宣称对所有现有基线作了全局支配。

## 10. 交付与复核材料

数学正文及复现源码均已生成。**合并 ZIP 尚未生成，正文附录中的 ZIP 打包说明尚未兑现；下面直接提供实际存在的文件。**

:chatgpt-content-reference{index="7"} · :chatgpt-content-reference{index="8"}

验证程序：
:chatgpt-content-reference{index="9"} ·
:chatgpt-content-reference{index="10"} ·
:chatgpt-content-reference{index="11"} ·
:chatgpt-content-reference{index="12"} ·
:chatgpt-content-reference{index="13"}

算术与输入：
:chatgpt-content-reference{index="14"} ·
:chatgpt-content-reference{index="15"} ·
:chatgpt-content-reference{index="16"} ·
:chatgpt-content-reference{index="17"} ·
:chatgpt-content-reference{index="18"} ·
:chatgpt-content-reference{index="19"}

实际验证输出：
:chatgpt-content-reference{index="20"} ·
:chatgpt-content-reference{index="21"} ·
:chatgpt-content-reference{index="22"}

整数计算显式选择了溢出抛错的 checked 类型，而非模整数回绕；其行为已核对 Boost 原始文档。citeturn315020view0 同时，GCC 文档对 `-frounding-math` 本身的保证有限，因此区间实现额外对每个非精确基本运算向外移动一个相邻可表示数，而没有仅靠该编译选项作为证明。citeturn315020view1 四种舍入模式下的 138,828 次精确有理算术对照通过；这是额外审计，不能代替正文的区间包围论证。

**最终判定：新工具及上述真分布子区间定理 PROVED（计算机辅助）；原完整基准与最终全局目标 INCOMPLETE。**

