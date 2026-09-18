# QWE05：泊松跳数提升与有界势比较，支付删除链的非线性插值项

**日期：2026-09-18。任务：randomcat4/dpp-stationary-entropy，PR #126。**  
**完整任务状态：INCOMPLETE。本文新的部分定理：PROVED（作者推导，待独立逐项审查）。**

本文不声称得到实际模型的渐近反例，也不声称证明完整熵率凹性。

## 0. 最强结果与交付边界

严格使用 QWE05 指定的有限循环 Fourier 投影、`c=19/20`、`a*=1/40`、`xi*=1/1520`，以及与真实律共享精确计数权重的指定修正律。令

\[
R_m=D(q_m\Vert\widehat q_m),\qquad
\widehat q_m=u_mg_m.
\]

沿下半层均匀删除链，源文件 CL12 的精确账本为

\[
R_{m+1}-R_m
=\mathcal C_m+\eta_mR_{m,\xi}+\mathcal J_m,
\tag{0.1}
\]

其中 `C_m` 是删点时丢失的**实际反向条件 KL**，`J_m` 是度二匹配插值的完整非线性积分，二者定义见 §1。

本文证明一个此前账本没有支付的上界：存在与 `n,m` 无关的常数 `K`，使所有充分大的偶数 `n`、所有 `4<=m<k=n/2` 满足

\[
\boxed{\mathcal J_m\le K\frac{1+\log n}{n}.}
\tag{0.2}
\]

在 `m<=3` 的有关均匀／度二层，`J_m=0`。因此对任务中精确的非负通量权重

\[
\omega_{n,0}=B_{n,0},\qquad
\omega_{n,m}=B_{n,m}-B_{n,m-1}\quad(1\le m<k),
\]

有

\[
\boxed{
\sum_{m=3}^{k-1}\omega_{n,m}\mathcal J_m
\le K_1\sqrt n(1+\log n)=o(n).
}
\tag{0.3}
\]

这是**单侧上界**，不是绝对值估计。结合 S14 独立审查明确保留的单侧响应支付

\[
\sum_m\omega_{n,m}\eta_mR_{m,\xi}\le K_2\sqrt n,
\]

得到实际任务项的新下界

\[
\boxed{
W_n^{\rm rel}
\ge-2\sum_{m=3}^{k-1}\omega_{n,m}\mathcal C_m
-K_3\sqrt n(1+\log n).
}
\tag{0.4}
\]

这里没有冻结计数权重，也没有把相对熵换成重叠变量的熵。**尚未证明**的一个明确、足够的后续估计是

\[
\boxed{
\sum_{m=3}^{k-1}\omega_{n,m}\mathcal C_m=o(n).
}
\tag{0.5}
\]

(0.5) 是经本次支付后剩下的一个更强充分条件，不宣称它是原目标的必要条件。原目标仍可能利用 `C_m` 与另两项的负向抵消；完整恒等式 (0.1) 保留这种可能。

新增工具还给出：

\[
\chi^2(\mathsf K_m\widehat q_{m+1}\Vert\widehat q_m)=O(n^{-1}),
\tag{0.6}
\]

以及对 CL6 的**全密度、全部模式**源项

\[
\boxed{
\left\langle\frac{(\mathsf B_mg_m)^2}{g_m}\right\rangle_{u_m}
=O(n^{-2}).
}
\tag{0.7}
\]

(0.7) 不依赖初始密度在高谐波上的总 `L²(u_m)` 质量，不是把固定 `j` 的估计直接求和。

---

## 1. 固定对象、归一与原始精确账本

记

\[
C=m(n-m),\quad \nu_2=2(n-1),\quad
\gamma=\nu_2/C,\quad A(\xi)=\xi(1+\xi),\quad d=k-m+1.
\]

`L=L_m` 的总跳率为一；于是 `M=I+L` 是 Markov 转移矩阵。以下内积总是对 `u_m`，概率律与相对均匀密度不混用。

密度删除与概率删除分别是

\[
(\mathsf D_mh)(S)=\frac1{n-m}\sum_{x\notin S}h(S+x),
\quad
(\mathsf K_mp)(S)=\frac1{m+1}\sum_{x\notin S}p(S+x).
\]

设 `p=q_{m+1}`、`p_hat=q_hat_{m+1}`，`P=K_mp`、`P_hat=K_mp_hat`。反向条件概率为

\[
\alpha_p(x\mid S)=\frac{p(S+x)}{(m+1)P(S)}.
\]

定义

\[
\mathcal C_m=\mathbb E_P
D(\alpha_p(\cdot\mid S)\Vert\alpha_{\widehat p}(\cdot\mid S))\ge0.
\tag{1.1}
\]

这是完整配置删点的条件信息，不是只观察 `|S intersection A|` 的 KL。

按任务给定的实际删除关系，令

\[
t_m=\frac1{k-m+y_m+\xi(n-m)},\quad
\eta_m=A(\xi)t_m,\quad y_m=m-\mu_m,
\]

则

\[
\mathsf D_m f_{m+1}=f_m+\eta_m f_{m,\xi}.
\tag{1.2}
\]

以下所有层参数在 `xi=xi*` 取值，除非明确写出其他 `xi`。定义

\[
x=\eta_m\gamma\tau_{m,\xi},\quad
\ell=\eta_m\tau_{m,\xi}=x/\gamma,\quad
h=-\log(1-x)/\gamma.
\tag{1.3}
\]

由度二匹配，`0<x<1` 且

\[
\mathsf D_mg_{m+1}=e^{hL}g_m.
\tag{1.4}
\]

匹配插值为

\[
f_t=f_m+t\eta_m f_{m,\xi},\quad
s(t)=-\log(1-tx)/\gamma,\quad
g_t=e^{s(t)L}g_m,\quad 0\le t\le1.
\tag{1.5}
\]

它不改变任何真实端点或指定修正律。`f_t` 是正密度的凸组合；`g_t` 是正时间热演化。并且

\[
s'(t)=\frac{x}{\gamma(1-tx)},\quad
s''(t)=\gamma(s'(t))^2.
\]

设

\[
Q_t=\left\langle
\frac{(\dot f_t-f_t\dot g_t/g_t)^2}{f_t}
\right\rangle.
\]

完整移动参考 KL 恒等式直接给出

\[
\mathcal J_m=
\int_0^1(1-t)\left[
Q_t-(s'(t))^2
\left\langle f_t-g_t,\frac{L(L+\gamma I)g_t}{g_t}\right\rangle
\right]dt.
\tag{1.6}
\]

KL 链式法则与 Taylor 积分公式给出 (0.1)。式 (1.6) 的参考加速没有被忽略。

---

## 2. 两条机制与最终选择

第一条是逐谐波比较：度零、度二源精确消失，固定高阶模式的删除源是 `O(n^-2)`。但初始完整配置密度的高模式质量不能据此求和，且对数似然是非线性的。这条机制保留作代数检查，不作为总体估计。

第二条来自连续时间 Markov 链的**泊松均匀化**，再结合有限维抛物比较原理和有界似然比下的浓度估计。转移的是：把热流时间微分提升为一个潜在泊松跳数的显式 score；对完整输出作条件期望，然后用 Jensen 或尾积分。它不是把随机热时间混合拿来替换真实 DPP。

单独用泊松提升只能在修正律下控制 score。新加入的关键步骤是 §4 的**实际核多项式似然比上界**。它把修正律下的泊松集中控制合法地迁移到真实／修正匹配插值中，从而支付 (1.6)。这避免把静态 KL 不等式形式微分。

---

## 3. 泊松提升：全模式删除误差与高阶 score

### 引理 3.1：统一的热时间比较

设 `L` 是有限状态空间上相对于概率测度 `u` 可逆的 Markov 生成元，总跳率不超过一；`r` 是任意初始概率密度，`G_T=e^{TL}r`，`T>0`。对以下比值使用其共同可达支持，则对 `h>=0`

\[
\chi^2(uG_{T+h}\Vert uG_T)
\le e^{h^2/T}-1,
\tag{3.1}
\]

\[
D(uG_{T+h}\Vert uG_T)
\le (T+h)\log(1+h/T)-h
\le \frac{h^2}{2T}.
\tag{3.2}
\]

反向 chi-square 同样满足

\[
\chi^2(uG_T\Vert uG_{T+h})\le e^{h^2/(T+h)}-1.
\]

更重要的是，对任意实数 `ell`

\[
\boxed{
\left\langle
\frac{(G_T+\ell LG_T-G_{T+h})^2}{G_T}
\right\rangle
\le e^{h^2/T}-1-\frac{h^2}{T}
+\frac{(h-\ell)^2}{T}.
}
\tag{3.3}
\]

**证明。** 使用

\[
e^{TL}=e^{-T}\sum_{N\ge0}\frac{T^N}{N!}M^N.
\]

先抽 `N~Poisson(T)`，再运行 `N` 步 `M` 并输出状态 `Y`。给定 `N` 的输出通道与 `T` 无关。把 `T` 改成 `T+h`，潜在泊松变量的似然比为

\[
Z_h(N)=e^{-h}(1+h/T)^N.
\]

数据处理给出 (3.1)–(3.2)。具体计算为

\[
\mathbb E Z_h=1,\quad \mathbb E Z_h^2=e^{h^2/T}.
\]

又有

\[
\frac{LG_T(Y)}{G_T(Y)}
=\mathbb E\left[\frac{N-T}{T}\mid Y\right].
\]

对 (3.3) 左侧用条件 Jensen，得到其不超过

\[
\mathbb E\left[1+\ell\frac{N-T}{T}-Z_h(N)\right]^2.
\]

使用

\[
\mathbb E[(N-T)^2]/T^2=1/T,\quad
\mathbb E[(N-T)Z_h(N)]/T=h/T
\]

即得 (3.3)。证明没有最小原子概率，也没有高模式求和。证毕。

### 推论 3.2：对指定 corrected 删除的实际支付

取 `T=tau_m`、`ell=eta_m tau_{m,xi}`、`h` 如 (1.3)，则 (3.3) 左侧就是

\[
\left\langle(\mathsf B_mg_m)^2/g_m\right\rangle.
\]

下文 §4.1 的时钟界与源文件的删除恒等式给出

\[
x\le \frac{M_\xi}{n},\qquad M_\xi=4(1+\xi_*)/\xi_*=6084.
\tag{3.4}
\]

当 `n>=2M_xi=12168` 时，存在仅依赖 `xi*` 的正常数，使

\[
\tau_m\ge a_0m,\quad h\le K m/n,\quad
h-\ell\le K m/n^2,
\quad a_0=\tfrac12\log(1+\xi_*).
\tag{3.5}
\]

于是 `h²/tau=O(m/n²)=O(1/n)`。代入 (3.1)、(3.3)，得到 (0.6)、(0.7)，一致于全部 `2<=m<k`。

注意 (3.3) 精确保留 `h-ell`：把线性热时间与实际增量视为相同会漏掉最后一项。

---

## 4. 实际核的多项式似然比：不是新的正则性假设

本节证明对所有偶数 `n>=40`、`4<=m<=k`，在 `xi*` 有

\[
\boxed{
\frac{f_m(S)}{g_m(S)}\le M_n
:=9\exp\!\left(\frac14+D_0b_0^2\right)n^{2D_0},
\quad D_0=\frac{1000}{261},\quad b_0=\frac{13}{7}.
}
\tag{4.1}
\]

这是完整配置上的逐点上界。常数保守，指数约为 `7.663`；本证明只使用它的对数是 `O(log n)`。尤其没有假设实际 `R_m` 已知为 `O(1)`。

### 4.1 所需时钟事实及证明

固定本层 `d`，`Q_r^(d)` 是归一化 Jacobi 多项式

\[
Q_r^{(d)}(\xi)=P_r^{(d-1,d-1)}(1+2\xi)/P_r^{(d-1,d-1)}(1).
\]

Jacobi 的正权重、零点位于 `(-1,0)` 以及相邻零点交错，保证相邻商 `Q_(r-1)/Q_r` 有正留数 Stieltjes 表示。正留数也由交错零点与正首项逐个计算得到。若

\[
F(\xi)=\sum_i\frac{a_i}{\xi+\lambda_i},\quad a_i>0,\quad0<\lambda_i<1,
\]

则 `-F'/F` 是 `1/(xi+lambda_i)` 的加权均值，并且 `log F` 凸。因此把 `theta_2` 写为两个相邻商的乘积，得到

\[
\frac{C}{(n-1)(1+\xi)}\le\tau_\xi
\le\frac{C}{(n-1)\xi},\qquad
\tau_{\xi\xi}\le0,\qquad \tau_\xi(0)=C/d.
\tag{4.2}
\]

特别地

\[
\frac{C}{n-1}\log(1+\xi)\le\tau(\xi)\le C\xi/d.
\tag{4.3}
\]

这些仅使用标准 Jacobi 零点性质；具体商、归一和不等式在此重新核对。

### 4.2 小噪声锚点，不用 Fourier 最小原子

置 `xi_0=n^-2`。对固定输入集合 `A_0`，令 `r=m-|S intersection A_0|`。真实重叠概率为

\[
w_r=w_0\frac{m_{\underline r}k_{\underline r}}{r!(d)_{\overline r}}z^{-r},
\quad z=(1+\xi)/\xi.
\tag{4.4}
\]

修正核的重叠链从 `r=0` 出发。仅保留“泊松跳数恰为 r，每一步均增加 r”的路径，得到严格下界

\[
\widehat w_r\ge e^{-\tau}\frac{(\tau/C)^r}{r!}
 m_{\underline r}k_{\underline r}.
\tag{4.5}
\]

两核在同一重叠类内部均匀，故它们逐配置的似然比恰为 `w_r/w_hat_r`。

设 `lambda=m(m+2d-1)=m(n-m+1)<=n²`。从 `Q_m` 的系数直接得到

\[
Q_m(\xi)\le e^{\lambda\xi/d},\qquad
Q_m(\xi)-Q_{m-2}(\xi)\ge(\nu_2/d)\xi.
\]

第二式因为对应系数关于多项式次数单调，且一次系数的差等于 `nu_2/d`。于是

\[
\tau(\xi_0)\ge\frac{C\xi_0}{dQ_m(\xi_0)},\qquad
\frac{C}{\tau(\xi_0)z_0}
\le d e^{1/d}<d+2,
\quad \tau(\xi_0)\le1/4.
\]

由 (4.4)–(4.5)，

\[
\frac{w_r}{\widehat w_r}
\le e^{1/4}\frac{(d+2)^r}{(d)_{\overline r}}
\le9e^{1/4}.
\tag{4.6}
\]

最后一个乘积在前两步之后不再增长；粗常数 `9` 已足够。对同一个真实输入先验平均，得到

\[
f_m(\xi_0)\le9e^{1/4}g_m(\xi_0).
\tag{4.7}
\]

没有用 `min det(P_S)`，也没有把输入集合的先验换成均匀分布。

### 4.3 修复后的源公式与有界势

下面先由生成元计算，再用守恒导出矩关系，遵守 S14 的非循环修正。

给定输入，记 `J=|S intersection A_0|`、`mu=EJ`、`X=J-mu`、`v=Var(J)`。真实核 `t_A` 满足

\[
\frac{Lt_A}{t_A}
=\frac{J^2-(m+k+n\xi)J+(1+\xi)mk}{A(\xi)C}.
\tag{4.8}
\]

守恒 `E[(Lt_A)/t_A]=0` 独立给出

\[
y^2+(k-m+n\xi)y+v=mk\xi,\qquad y=m-\mu.
\tag{4.9}
\]

此后才中心化，得到

\[
\frac{(\partial_\xi-\tau_\xi L)t_A}{t_A}
=-\kappa(X^2-v+bX),\qquad \kappa=\frac{\tau_\xi}{AC}.
\tag{4.10}
\]

真实核与修正热时钟在纯度二多项式

\[
H_2(J)=(J-m/2)^2-C/[4(n-1)]
\]

上的匹配给出

\[
b=-\frac{\mu_4-v^2+(2\mu-m)\mu_3}
{\mu_3+(2\mu-m)v}.
\tag{4.11}
\]

这里所需的负实零点与度二匹配可直接从同一个有限多项式核验，而不把它们作为未验证的额外源引理。令

\[
G(z)=\sum_{j=0}^m\binom{k}{j}\binom{k}{m-j}z^j.
\]

Jacobi 的有限级数变换给出

\[
G(z)=\binom{k}{m}(1-z)^m
\frac{P_m^{(d-1,d-1)}((1+z)/(1-z))}{P_m^{(d-1,d-1)}(1)}.
\tag{4.11a}
\]

右侧在 `z=1` 的表观奇点可去。每个 Jacobi 零点 `x_i in (-1,1)` 对应 `z_i=(x_i-1)/(x_i+1)<0`，所以全部 `m` 个根严格负。倾斜后的概率生成函数 `G(zt)/G(z)` 因而分解成 `m` 个 Bernoulli 生成函数。

同时在 `z=(1+xi)/xi`，(4.11a) 给出

\[
G(z)=\binom{k}{m}\xi^{-m}Q_m^{(d)}(\xi).
\]

设 `H_0=nm(m-1)/[4(n-1)]`。在 `Q` 的有限级数中逐项比较，或使用其二阶微分方程后比较系数，得到

\[
H_0Q_{m-2}=(H_0+2mkA)Q_m-kA(1+2\xi)Q_m'.
\tag{4.11b}
\]

作用算子 `[(z partial_z-m/2)^2-C/(4(n-1))]` 于 `G`，再用 `z partial_z=-A partial_xi` 和 (4.11b)，便得 `E H_2=H_0Q_{m-2}/Q_m`。而 `L H_2=-gamma H_2`、初始 `H_2=H_0`，故指定时钟确实在这个条件核上匹配度二。这也验证了 (4.11) 所使用的 `E[(partial_xi-tau_xi L)t_A H_2]=0`。

以上 Bernoulli 分解立即给出

\[
|\mu_3|\le v,\quad \mu_4\le3v^2+v,\quad v\le y.
\]

由 (4.9)，对 `0<xi<=xi*` 有

\[
y/m\le\sqrt{\xi(1+\xi)}-\xi\le1/40,
\quad v\le m\sqrt A,\quad 2\mu-m\ge(19/20)m.
\tag{4.12}
\]

因此当 `m>=4`，(4.11) 的分母严格正，且

\[
|b|\le\frac{(21/20)m+1}{(19/20)m-1}\le13/7=b_0.
\tag{4.13}
\]

另设 `u=2mu-m`、`H=E H_2(J)`。直接微分度二期望，得到

\[
\frac{\tau_\xi}{C}
=\frac{\mu_3+uv}{A\nu_2H},\qquad
H=\frac{u^2}{4}+v-\frac{C}{4(n-1)}
\ge\frac{261}{1600}m^2.
\]

于是

\[
\frac{\tau_\xi}{C}
\le D_0\frac{v}{A(n-1)m},\qquad D_0=1000/261.
\tag{4.14}
\]

完成平方，(4.10) 的右侧不超过

\[
K_m(\xi)=\kappa(v+b_0^2/4)
\le D_0\left[
\frac{m}{(n-1)A}+
\frac{b_0^2}{4(n-1)A^{3/2}}
\right].
\tag{4.15}
\]

对相同先验平均仍有 `f_xi<=tau_xi Lf+K_m f`。有限维正半群比较给出

\[
f_m(\xi_*)\le9e^{1/4}
\exp\!\left(\int_{\xi_0}^{\xi_*}K_m(v)\,dv\right)g_m(\xi_*).
\]

利用 `A>=xi`、`m/(n-1)<=1` 与 `xi_0=n^-2`，

\[
\int_{\xi_0}^{\xi_*}K_m(v)\,dv
\le2D_0\log n+D_0b_0^2.
\]

这就证明了 (4.1)。证毕。

这一引理使用的是有界**上势**加正半群比较，不声称源本身有利，也没有从 `R_m=O(1)` 推出跨层平滑性。

---

## 5. 把泊松 score 从修正律迁移到实际插值

### 引理 5.1：有界似然比下的泊松矩支付

在任意联合概率空间上设 `N~Poisson(T)`。令 `H>=0`、`EH=1`、`H<=M`，`M>=1`。记

\[
u=1+\log(2M).
\]

则

\[
\mathbb E[H(N-T)^2]\le16(Tu+u^2).
\tag{5.1}
\]

**证明。** 泊松的显式矩母函数与 Chernoff 不等式给出

\[
\Pr\{|N-T|>2\sqrt{Tz}+2z\}\le2e^{-z},\quad z\ge0.
\]

加权概率至多是原概率的 `M` 倍。取 `U=log(2M)`，故加权的 `(N-T)²` 随机变量被

\[
8T(U+E)+8(U+E)^2,\qquad E\sim\operatorname{Exp}(1)
\]

在尾分布上支配。取期望即得 (5.1)。这里不要求 `H` 与 `N` 独立。证毕。

若输出真实密度 `f` 相对热密度 `G_T` 满足 `f/G_T<=M`，把 `H` 取为输出的这个似然比。由泊松提升与条件 Jensen，

\[
\mathbb E_f\left(\frac{LG_T}{G_T}\right)^2
\le\mathcal A(T,u),
\quad
\mathbb E_f\left|\frac{L^2G_T}{G_T}\right|
\le\mathcal A(T,u),
\tag{5.2}
\]

其中可取

\[
\mathcal A(T,u)=32\left(\frac uT+\frac{u^2}{T^2}\right).
\]

第二式使用明确的二阶泊松 score

\[
\frac{L^2G_T(Y)}{G_T(Y)}
=\mathbb E\left[
\frac{(N-T)^2-N}{T^2}\mid Y\right].
\]

由 (5.1) 还有 `E_HN<=3T+6u`，故常数 `32` 足够同时覆盖两式。

### 插值所需的似然比上界确实成立

由 (1.2) 的潜在核公式，

\[
0<f_t\le(1+t_m\mu_m)f_m\le A_*f_m,
\quad A_*=1+1/\xi_*=1521.
\]

并由“零跳”项，`g_t>=e^{-s(t)}g_m>=e^{-h}g_m`。结合 (4.1)，

\[
f_t/g_t\le A_*e^hM_n.
\tag{5.3}
\]

所以 (5.2) 可对每个实际 `f_t,g_t` 使用，取

\[
u_m=1+\log(2A_*)+h+\log M_n,
\quad
\mathcal A_m=32\left(\frac{u_m}{\tau_m}
+\frac{u_m^2}{\tau_m^2}\right).
\tag{5.4}
\]

此处 `g_t=e^{(tau_m+s(t))L}r_m^max` 的总热时间至少为 `tau_m`。式 (5.3) 是已经证明的实际核估计，不是作为新假设引入。

---

## 6. 非线性插值项的明确有限维上界

### 定理 6.1

对偶数 `n>=40`、`4<=m<k`，令

\[
S_m=\frac{x}{\gamma(1-x)}=\max_{t\in[0,1]}s'(t).
\]

则

\[
\boxed{
\mathcal J_m
\le2t_m^2v_m
+\frac{S_m^2}{2}
\left[3\mathcal A_m+\gamma\sqrt{\mathcal A_m}\right].
}
\tag{6.1}
\]

右侧全由显式一维重叠矩、指定时钟、`n,m` 和已经给出的常数组成，不含未知高模式总质量或待付 KL 导数。

**证明。** 设 `v=eta_m f_(m,xi)`，则 `f_t=f_0+tv`，并且 `f_t>=(1-t)f_0`。因此

\[
\int_0^1(1-t)\left\langle\frac{v^2}{f_t}\right\rangle dt
\le\left\langle\frac{v^2}{f_0}\right\rangle
\le t_m^2v_m.
\tag{6.2}
\]

最后一步是潜在真实重叠 score `-(J-mu)/A` 的条件 Jensen，即实际真删除的静态 Fisher 支付；这里没有对静态不等式求导。

用 `(a-b)²<=2a²+2b²` 展开 `Q_t`，由 (5.2) 得

\[
Q_t\le2\langle v^2/f_t\rangle
+2(s'(t))^2\mathcal A_m.
\]

又由于 `L` 守恒，

\[
\left\langle f_t-g_t,\frac{L(L+\gamma)g_t}{g_t}\right\rangle
=\mathbb E_{f_t}\frac{L(L+\gamma)g_t}{g_t}.
\]

(5.2) 与 Cauchy–Schwarz 给出其绝对值不超过

\[
\mathcal A_m+\gamma\sqrt{\mathcal A_m}.
\]

将这些代入完整 (1.6)，并使用 `integral_0^1(1-t)dt=1/2`，即得 (6.1)。证毕。

### 一致尺度

由 (4.2)、`eta<=2(1+xi*)/n` 得 (3.4)。当 `n>=12168`，

\[
\tau_m\ge a_0m,\quad
S_m\le2M_\xi m/n,\quad h\le M_\xi,\quad
\gamma\le4/m.
\]

由 (5.4)，`u_m<=K_0+K_1 log n`。因此 (6.1) 第二项不超过

\[
K\frac{m u_m+u_m^2}{n^2}
\le K'\frac{1+\log n}{n}
\]

对所有充分大的 `n` 一致成立。第一项用 `t_m<=2/(xi_* n)`、`v_m<=m/40<=n/80`，得到

\[
t_m^2v_m\le\frac{1}{20\xi_*^2n}=\frac{115520}{n}.
\]

即可。于是 (0.2) 成立。低阶 Fourier 层的恒等匹配给出 `J_3=0`；更低层相同。

本支付没有消耗 S14 已用于 `eta R_xi` 的对偶 Dirichlet 预算。它使用不同的点态比较和泊松矩控制，故不存在同一 Fisher 预算重复支付。

---

## 7. 带精确计数权重的结论，以及中心层

按 S14 已独立核验的计数多项式因子分解，

\[
\Pi''(t)=(1-t)^2B_n(t),\quad
B_n(t)=2kp_0^{k-1}+k(k-1)(1+t)^2p_0^{k-2},
\]

\[
p_0(t)=\tfrac{1-c^2}{4}(1+t^2)+\tfrac{1+c^2}{2}t.
\]

`B` 的系数回文、非负、单峰。因此对实际的补集对称 `R_(n-m)=R_m`，

\[
W_n^{\rm rel}
=-2\sum_{m=0}^{k-1}\omega_{n,m}(R_{m+1}-R_m).
\tag{7.1}
\]

其通量总质量是

\[
\sum_{m=0}^{k-1}\omega_{n,m}=B_{n,k-1}=O_c(n^{3/2}).
\]

代入 (0.2) 得 (0.3)。再使用 S14 审查仅保留的

\[
\sum_m\omega_{n,m}\eta_mR_{m,\xi}\le K\sqrt n
\]

得到 (0.4)。此响应估计始终只按所需方向使用，不写成绝对值或极限等式。

**中心层没有被错误穿越。** 所有删除关系只用到 `m=k-1`，然后由补集对称将上半层汇入 (7.1)。中心二阶差是

\[
\Delta^2R_{k-1}=-2(R_k-R_{k-1}),
\]

故中心 `C_(k-1)>=0` 确实以不利符号出现。本文没有删除该项，也没有把下半层公式粘贴到中心另一侧。

---

## 8. 反证尝试与模型有效的计算

### 8.1 完整 Fourier-DPP 枚举

附带 `qwe05_verify.py` 实际计算 `n=8,10,12,14,16,18` 的全部下半层配置。真实律用中点精确 L-ensemble 矩阵

\[
\Lambda=39P+\frac1{39}(I-P)
\]

的主子式归一；修正律从 `det(P_S)/binom(k,m)` 出发运行指定 Johnson 半群。没有把任意径向模型误当成完整输出。

| n | 中心实际 R_k | 实际 W_n^rel | W_n^rel/n |
|---:|---:|---:|---:|
| 8 | 5.6428e-11 | -1.9467e-9 | -2.4333e-10 |
| 10 | 3.2447e-9 | -1.6001e-7 | -1.6001e-8 |
| 12 | 3.1989e-8 | -2.1056e-6 | -1.7547e-7 |
| 14 | 1.5602e-7 | -1.3066e-5 | -9.3328e-7 |
| 16 | 5.2355e-7 | -5.3844e-5 | -3.3652e-6 |
| 18 | 1.3889e-6 | -1.7068e-4 | -9.4825e-6 |

这些是双精度数值，不是有理区间证书。`n=8` 的严格负号本来已有源文件解析证明；此处只是另一路计算复核。

21 个相邻层检查中，实际 corrected 删除关系的最大逐原子偏差约为 `1.74e-17`；完整加权账本最大绝对偏差约为 `5.43e-15`。新 (3.3) 的左／右比值最大约为 `0.00102`，(3.1) 的左／右比值最大约为 `0.04035`。有限测试没有发现违反新不等式的例子。

这些负值**不能**作为渐近反例。尤其在所测试的很小体积中，`W/n` 的数值趋势不支持凭图形直接宣布它趋于零。

### 8.2 较大体积的潜在核检查：严格区分作用域

另计算 `n=32,...,4096`，以及中心和两个非中心层的给定输入重叠链。中心潜在核的 `D(w||w_hat)` 在 `n=4096` 约为 `0.08954`，`chi²(w||w_hat)` 约为 `0.14387`。

这些数值只用于检验实际条件核和热核构件；它们不是完整 Fourier 输出的 `R_m`，更不是其删除反向信息 `C_m`。本文的渐近证明不依赖这些数值或其拟合极限。

起初普通稀疏矩阵指数在极小尾概率位置返回零，不能据此计算有限 chi-square。附带脚本改用正的对数域泊松均匀化求尾概率，并在主概率质量上与稀疏矩阵指数交叉检查。全部这些检查仍是浮点验证，不冒充严格区间界。

### 8.3 对新增源界、锚点及插值界的直接压力测试

另附 `qwe05_analytic_checks.py`，在 `n=40,64,128,512,2048,4096` 的小层、中心附近及中心层，对 `xi=n^-2` 到 `xi*` 的九个几何间隔参数进行 270 个源／矩／时钟检查；并进行 30 个锚点检查、24 个条件核插值检查。此处仍明确只是给定输入的实际核构件，不把它们当作完整 Fourier 输出。

实测 `|b|` 最大约为 `0.99999977`，低于证明常数 `13/7`；实际源上峰值与 (4.15) 上界之比最大约为 `0.12368`。锚点逐点对数似然比最大约为 `0.10057`，小于已证明的 `log 9+1/4≈2.44723`。直接用插值端点 KL 减去初始 KL 与物理响应计算的 `J`，除以 (6.1) 上界后的最大比值约为 `3.89e-5`。这些保守不等式的数值通过不是证明的替代。

### 8.4 对所需新工具的对抗性检查

- **任意初值／高模式测试：** 引理 3.1 的证明对任意初始密度成立，尤其覆盖高模式质量很大的初值；无需把高模式视为固定次数。
- **移动参考测试：** (3.3) 保留 `h-ell`，(1.6) 与 (6.1) 保留 `s''=gamma(s')²`，没有把 corrected 删除当作与真删除相同的 Markov 演化。
- **扩散剖面陷阱：** 仅 `R>=0`、补集对称和 `R=O(1)` 的反例仍然成立。本文额外证明实际核的点态比较并据此支付实际插值；它不宣称这一支付已经控制反向条件信息。

---

## 9. 精确剩余义务与可复用交接

本次把原先未付的 `C_m+J_m` 中的 `J_m` 真正支付为次线性上界。没有把这个积分重新命名后作为一个新假设。

剩余的一个充分目标是 (0.5)，其中每个 `C_m` 已由 (1.1) 明确定义。在计数通量集中区域，证明实际模型的

\[
\mathcal C_m\le K/n
\]

会足够；但这一逐层条件比 (0.5) 更强，本文没有证明它。

潜在的下一步应针对：给定删点后完整配置 `S`，真实后验的被删站点分布与修正后验的被删站点分布为什么足够接近。仅对给定输入集合的重叠链作数据处理，不能自动约束忘掉输入之后的这个反向条件 KL；本文不作这种交换。

复用本文只需三项接口：

1. `L` 总跳率一、同一实际初值，使用 (3.3) 的全模式源支付。
2. 对真实核的 (4.8)–(4.15) 和小噪声锚点，取得多项式似然比。
3. 将 (5.2) 代入完整移动参考 Hessian，得到明确的 (6.1)。

若后续 `C_m` 无法单独支付，应回到精确 (0.1)、(7.1) 研究其与响应／插值的 signed cancellation，而不能把 (0.5) 当成原目标的等价重写。

---

## 10. 来源、独立性与证明状态

**任务与固定模型：** Google Drive 的 `QWE05_启动提示词.txt`、`QWE05_PACKET.md`，及 GitHub PR #126 的任务元信息。操作指令仅按 packet 根部 `CONTRACT.md`、`TASK.md`；历史附件中的旧任务指令未执行。

**原始而非本次新增：** 真删除关系、度二匹配插值、KL 链式分解与计数 Hessian 因子分解。本文按公式重新检查其用法和归一。

**使用的独立审查范围：** `S14_INDEPENDENT_REVIEW.md` 对计数通量和响应项的单侧支付；没有把 SA05 自审等同于独立认证，也没有使用被撤回的双侧 `O(sqrt n)` 说法。

**本次新增、作者推导待独立审查：** (3.3) 在指定删除源上的全模式支付；(4.1) 的小噪声锚点加有界势比较；有界倾斜的泊松 score 迁移；(6.1)、(0.2)–(0.4) 的实际模型非线性插值支付。

**外部来源的准确作用域：**

- Arne Jensen, *Markoff chains as an aid in the study of Markoff processes*, Scandinavian Actuarial Journal, 1953, Supplement 1, pp. 87–91, DOI `10.1080/03461238.1953.10419459`。只说明泊松均匀化这个外部机制的出处；本文所需恒等式和不等式全部在 §3、§5 推导。没有将其引用成现成的 DPP 跨层定理。
- NIST DLMF §18.5(iii)，式 18.5.7：Jacobi 的有限级数表示。用于识别这里的 `Q_r^(d)`。
- NIST DLMF §18.2(vi)：正交多项式零点与相邻交错。只用于 §4.1 的 Stieltjes 商证明和重叠生成多项式的负实零点。

**不存在的结论：** 原 QWE05 渐近下界没有被完整证明；没有实际模型渐近反例；没有校正律完整曲率符号；没有 Toeplitz 极限桥接；没有熵率极限求导；没有全局熵率凹性定理。

---

## 11. 附件与复现

- `qwe05_verify.py`：完整配置、删除账本、泊松源界与潜在核计算。
- `full_model.csv`：完整 Fourier 模型的小体积结果。
- `deletion_ledger.csv`：21 个实际相邻层的 `C_m`、响应、`J_m` 和新源界。
- `radial_checks.csv`：与完整配置结果分开的潜在核检查。
- `verification_summary.json`、`run.log`：机器可读摘要和实际运行日志。
- `qwe05_analytic_checks.py`：新源界、锚点、时钟和条件核插值的直接压力测试。
- `analytic_source_checks.csv`、`anchor_checks.csv`、`interpolation_checks.csv`、`analytic_check_summary.json`、`analytic_run.log`：上述额外测试数据。

复现命令：

```bash
OPENBLAS_NUM_THREADS=1 python qwe05_verify.py --small-max 18 --radial-max 4096
OPENBLAS_NUM_THREADS=1 python qwe05_analytic_checks.py
```

所需 Python 包：NumPy、SciPy。数值测试并非证明成立的前提。本文数学证明也不以仓库写入、文件导出或任何哈希验收作为成立条件。