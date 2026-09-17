> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA05｜补充的跨层缺陷传递算子

**PROVED：** 下述完整密度恒等式、严格模式残差、静态 \(\chi^2\) 界及固定模式尺度界。  
**INCOMPLETE：** 它们尚未推出主文剩余的 \(\sum_l\pi_l''R_l\ge-o(n)\)。  
这一补充不改变真实律或指定 corrected law，不把跨层静态接近形式微分。

## 1. 下采样对应一个显式的参数响应

沿用主文记号 \(n=2k,\xi=a(1-c-a)/c,A(\xi)=\xi(1+\xi)\)。
本节只在下半层 \(1\le m<k\) 工作；上半层可用补集另作同向比较，
不跨越中层强行套用“最大重叠初值下采样不变”。

对相对均匀律的密度定义
\[
(\mathsf D_m h)(S)=\frac1{n-m}\sum_{x\notin S}h(S+x),
\qquad |S|=m.
\]
概率通道另记为
\[
(\mathsf K_mq)(S)=\frac1{m+1}\sum_{x\notin S}q(S+x),
\qquad \mathsf K_m(u_{m+1}h)=u_m\mathsf D_mh.
\]
它从一个 \((m+1)\)-集均匀删除一个元素。
密度公式的系数是 \(1/(n-m)\)，概率公式则是 \(1/(m+1)\)。

固定输入 \(A_0\)，令 \(J=|S\cap A_0|\)，
\[
T_m(S\mid A_0)=z^J/Z_{n,m}(z),\qquad
\mu_m=\mathbb E_{T_m}J,\quad v_m=\operatorname{Var}_{T_m}J,\quad y_m=m-\mu_m.
\]
先对下一层核直接下采样：
\[
\widetilde T_m(S\mid A_0)
=\frac{z^J[kz+k-m-(z-1)J]}{(m+1)Z_{n,m+1}(z)}.
\]
归一给出
\[
V_m:=\frac{(m+1)Z_{n,m+1}}{Z_{n,m}}
=kz+k-m-(z-1)\mu_m>0.
\]
置
\[
t_m=\frac{z-1}{V_m}
=\frac1{k-m+y_m+\xi(n-m)},\qquad
\eta_m=A(\xi)t_m.
\]
因为 \(\partial_\xi\log T_m=-(J-\mu_m)/A(\xi)\)，所以
\[
\widetilde T_m=T_m+\eta_m\partial_\xi T_m.
\]
计数条件不改变输入先验 \(\nu\)，按这个共同先验平均，得到完整配置恒等式
\[
\boxed{\mathsf D_m f_{m+1}=f_m+\eta_m f_{m,\xi}.} \tag{CL1}
\]
不是只对计数或某个势成立；它逐个 \(m\)-原子成立。
\(\eta_m\) 只需要一维重叠均值，不依赖输入集合的形状。

同样，\(\mu_{m,\xi}=-v_m/A\)，故
\[
\eta_{m,\xi}
=\frac{1+2\xi}{k-m+y_m+\xi(n-m)}
-\frac{v_m+A(\xi)(n-m)}
 {[k-m+y_m+\xi(n-m)]^2}.                         \tag{CL2}
\]
必要 jets 不必通过差分猜测。若 \(m+2\le k\)，组合两次下采样直接得到
\[
\boxed{
\mathsf D_m\mathsf D_{m+1}f_{m+2}
=f_m+(\eta_m+\eta_{m+1}+\eta_{m+1}\eta_{m,\xi})f_{m,\xi}
+\eta_m\eta_{m+1}f_{m,\xi\xi}.}                 \tag{CL3}
\]
这利用 \(\mathsf D_m\) 与 \(\xi\) 微分可交换，并保留了移动系数的导数。

## 2. 修正律的额外热时间与严格度二消去

本节及 §4 的匹配插值取 \(2\le m<k\)；\(m\le1\) 的均匀层不引入未定义时钟。

写 \(\Omega_m=m(n-m)L_m\)、\(\beta_m=\tau_m/[m(n-m)]\)。
在下半层，最大重叠初值满足
\(\mathsf D_mr_{m+1}^{\max}=r_m^{\max}\)。
而 \(\Omega_m\) 是所有站点换位 \(T_{ij}-I\) 的和，
下采样对站点置换等变，所以
\[
\mathsf D_m\Omega_{m+1}=\Omega_m\mathsf D_m.
\]
因此指定修正律精确满足
\[
\mathsf D_mg_{m+1}=e^{\Delta\beta_m\Omega_m}g_m,
\qquad\Delta\beta_m=\beta_{m+1}-\beta_m.          \tag{CL4}
\]

对 \(m\ge2\)，将 (CL1) 测试在任意度二模式上，得到
\[
\theta_{m+1,2}=\theta_{m,2}+\eta_m\theta_{m,2,\xi}
=\theta_{m,2}(1-x_m),
\quad x_m=\eta_m\gamma_{2,m}\tau_{m,\xi}.
\]
主文已证明 \(\eta_m,\tau_{m,\xi},\theta_{m+1,2}>0\)，故
\[
0<x_m<1,\qquad
\Delta\beta_m=-\frac{\log(1-x_m)}{2(n-1)}>0.      \tag{CL5}
\]
这证明修正律下采样所增加的热时间为正，不需要猜测时钟的层单调性。
逐模式测试合法：可先对任意固定输入的核测试，最大重叠的对应谐波系数非零；
因此不依赖某一具体先验恰好激发了该模式。

由 (CL1)、(CL4) 与 \(g_{m,\xi}=\tau_{m,\xi}L_mg_m\)，密度缺陷满足
\[
\boxed{
\mathsf D_m\delta_{m+1}
=(I+\eta_m\partial_\xi)\delta_m+\mathsf B_mg_m,
\quad
\mathsf B_m=I+\eta_m\tau_{m,\xi}L_m-e^{\Delta\beta_m\Omega_m}.
}                                                        \tag{CL6}
\]
这是一个跨层的缺陷传递算子，源完全由指定修正律、时钟与一维重叠矩给出。

在第 \(j\) Johnson 模式上，\(\mathsf B_m\) 的乘子为
\[
b_{m,j}=1-r_jx_m-(1-x_m)^{r_j},
\qquad r_j=\frac{\gamma_{j,m}}{\gamma_{2,m}}.
\]
所以 \(b_{m,0}=b_{m,2}=0\)，而 \(j>2\) 时 \(b_{m,j}<0\)，
这是 \(t\mapsto(1-t)^{r_j}\) 的严格凸性。
本题奇数模式不激发，故 (CL6) 的有效源仍从度四开始。
\(\mathsf B_m\) 不是被宣称为正 Markov 生成元，其模态符号不决定 KL 的符号。

## 3. 两个有明确 n 依赖的弱稳定性结论

### 3.1 真相邻层下采样的静态 \(\chi^2\) 代价是 \(O(1/n)\)

给定输入的概率比是 \(1-t_m(J-\mu_m)\)。
对共同先验平均并用条件 Jensen，得
\[
\chi^2(\mathsf K_mq_{m+1}\Vert q_m)
:=\sum_{|S|=m}\frac{[(\mathsf K_mq_{m+1})(S)-q_m(S)]^2}{q_m(S)}
\le t_m^2v_m.                                           \tag{CL7}
\]
这里 \(\mathsf K_m\) 是概率通道，\(\mathsf D_m\) 是密度通道；
两者的归一关系已在 §1 指明。

中点 \(v_m\le m/40\)，且
\(t_m^{-1}\ge\xi_*(n-m)\)、\(m\le n/2\)。所以
\[
\boxed{\chi^2(\mathsf K_mq_{m+1}\Vert q_m)
\le\frac1{20\xi_*^2n}=\frac{115520}{n}.}                 \tag{CL8}
\]
这个常数很粗；实际应使用 \(t_m^2v_m\)。
(CL8) 只在其静态位置成立。本文件没有对这个不等式取导数；
所需 jets 使用先证明的恒等式 (CL1)–(CL3)。

### 3.2 固定模式的跨层源有 \(O(n^{-2})\) 界

由
\[
\eta_m\le\frac{1+\xi}{n-m},\qquad
\gamma_{2,m}\tau_{m,\xi}\le\frac2\xi,
\]
可得 \(x_m\le M(\xi)/n\)，其中 \(M(\xi)=4(1+\xi)/\xi\)。
若 \(n\ge2M(\xi)\)，则 \(x_m\le1/2\)。Taylor 积分余项给出
\[
|b_{m,j}|\le r_j(r_j-1)x_m^2
\le\frac{j^2M(\xi)^2}{4n^2}\quad(4\le j\le m).           \tag{CL9}
\]
中点 \(M(\xi_*)=6084\)。这是每个固定 \(j\) 的一致跨层模态估计；
它没有控制初值的高模式总质量，也没有允许把全部 \(j\) 当成固定常数。
因而不能据此直接声称全密度或熵的缺陷为 \(O(n^{-2})\)。

## 4. 精确的跨层 KL 账本与度二匹配插值

### 4.1 删点所丢的 KL 不是零：保留反向条件项

令 \(p=q_{m+1},\widehat p=\widehat q_{m+1}\)，
\[
\alpha_p(x\mid S)=\frac{p(S+x)}{(m+1)(\mathsf K_mp)(S)},
\quad
\alpha_{\widehat p}(x\mid S)
=\frac{\widehat p(S+x)}{(m+1)(\mathsf K_m\widehat p)(S)}.
\]
对联合“删点后的集合＋被删站点”应用 KL 链式分解，得到
\[
R_{m+1}=D(\mathsf K_mp\Vert\mathsf K_m\widehat p)+\mathcal C_m,
\quad
\mathcal C_m=\mathbb E_{\mathsf K_mp}
 D(\alpha_p(\cdot\mid S)\Vert\alpha_{\widehat p}(\cdot\mid S))\ge0.
                                                               \tag{CL10}
\]
此式精确保留数据处理丢掉的反向条件信息。
它并不给 \(\Delta\mathcal C_m\) 赋号。

### 4.2 一个不改变两端实际律的匹配插值

以下 \(t\in[0,1]\) 是辅助插值变量，不是物理 \(a\)，也不是另选 corrected law。
固定本层 \(\xi\)，置
\[
f^{[t]}=f_m+t\eta_m f_{m,\xi},\qquad
b(t)=-\frac{\log(1-tx_m)}{\nu_2},\qquad
g^{[t]}=e^{b(t)\Omega_m}g_m,\quad \nu_2=2(n-1).
\]
真插值是两正概率密度的凸组合，故严格正。
修正插值是正时间的热演化。
两个端点分别是本层两律与下一层两律的实际下采样。
所有 \(t\) 上常数及度二均精确匹配，因为其度二因子均为 \(1-tx_m\)。

写
\[
\delta^{[t]}=f^{[t]}-g^{[t]},\quad
Z^{[t]}=\Omega_m(\Omega_m+\nu_2 I)g^{[t]},\quad
\mathcal Q^{[t]}=
\left\langle\frac{(\partial_tf^{[t]}
-f^{[t]}\partial_tg^{[t]}/g^{[t]})^2}{f^{[t]}}\right\rangle_{u_m}.
\]
由 \(b''=\nu_2(b')^2\)，
\[
\partial_t^2f^{[t]}=0,\qquad
\partial_t^2g^{[t]}=(b')^2Z^{[t]}.
\]
对 \(\mathcal R(t)=D(u_mf^{[t]}\Vert u_mg^{[t]})\)
使用主文的移动参考 Hessian 恒等式，得到
\[
\mathcal R''(t)
=\mathcal Q^{[t]}-(b'(t))^2
 \langle\delta^{[t]},Z^{[t]}/g^{[t]}\rangle_{u_m}.           \tag{CL11}
\]
这里 \(\langle Z^{[t]}\rangle=0\) 使 \(f^{[t]}\) 可换成缺陷 \(\delta^{[t]}\)。
已知源仍严格消去常数及度二，不是把二阶误差重新命名。

由于 \(b'(0)\Omega_m=\eta_m\tau_{m,\xi}L_m\)，
\(\mathcal R'(0)=\eta_mR_{m,\xi}\)。Taylor 的积分恒等式与 (CL10) 合并为
\[
\boxed{
\begin{aligned}
R_{m+1}-R_m={}&\mathcal C_m+\eta_mR_{m,\xi}\\
&+\int_0^1(1-t)\left[
\mathcal Q^{[t]}-(b'(t))^2
 \langle\delta^{[t]},Z^{[t]}/g^{[t]}\rangle_{u_m}
\right]dt .
\end{aligned}}                                                   \tag{CL12}
\]
这是明确的跨层非线性误差账本，包含反向条件信息、真实参数响应、
移动热参考和正平方项。它不是从 (CL8) 的静态接近推出导数接近。

## 5. 对移动计数缺口的实际作用与剩余义务

(CL1)、(CL4) 把下一层下采样得到的两个完整律写成
\(q_m+\eta_mq_{m,\xi}\) 与
\(u_m e^{\Delta\beta_m\Omega_m}g_m\)，并不是本层原始两律。
(CL12) 则精确支付“为什么不能直接用数据处理比较 \(R_{m+1}\) 与 \(R_m\)”。

还不能据此给 \(\Delta^2R_m\) 赋号：
\(\mathcal C_m\) 和 \(\mathcal Q^{[t]}\) 的非负性不保证它们的跨层差非负，
而 \(\langle\delta^{[t]},Z^{[t]}/g^{[t]}\rangle\) 尚无总符号。
主文已付的 \(R_{m,\xi}\) 上界可用于它的正确位置，但不是任意方向的二阶估计。

工具的作用是把跨层缺口变成这些明确对象；
(CL3) 给出二次下采样所需的全部真密度二阶 jets，
(CL9) 给出源在固定模式上的 \(O(n^{-2})\) 界。
还需高模式总质量、反向条件项及非线性积分的跨层预算，
才能控制真实计数加速中的 \(\sum_rB_r\Delta^2R_r\)。
此最后一步本次仍未完成。

## 6. 中心层的精确障碍：n=8 的移动相对熵权重项严格为负

本题的补集对称性给出 \(R_{n-m}=R_m\)，但不会使中心的跨层二阶差消失。
对 \(k\ge3\)，把 (CL12) 的 \(m=k-1\) 记为
\[
R_k-R_{k-1}=\mathcal C_{k-1}+\eta_{k-1}R_{k-1,\xi}
+\mathcal J_{k-1},
\]
其中 \(\mathcal J_{k-1}\) 就是 (CL12) 的显式积分，则
\[
\Delta^2R_{k-1}
=-2[\mathcal C_{k-1}+\eta_{k-1}R_{k-1,\xi}+\mathcal J_{k-1}]. \tag{CL13}
\]
因此反向条件 KL 的非负性在这个中心二阶差里贡献的是不利符号，
不是可无条件删除的有利项。

在合法的 \(n=8,k=4\) 实例中，这个机制完全显露。
所有 \(m\le3\) 层都有 \(f_m=g_m\)，而第 \(4\) 层的度四缺陷严格非零。
由 (CL6)，\(\delta_3=0\)，且 \(g_3\) 只有常数及度二，
故
\[
\mathsf D_3\delta_4=0,\qquad
\mathsf K_3q_4=\mathsf K_3\widehat q_4 .
\]
于是 (CL10) 的下采样 KL 恰为零，而
\[
\boxed{R_4=\mathcal C_3>0.} \tag{CL14}
\]
在 (CL12) 的匹配插值中，\(f^{[t]}=g^{[t]}\) 对所有 \(t\) 成立，
所以 \(R_{3,\xi}=0\)、\(\mathcal J_3=0\)，并有
\(\Delta^2R_3=-2R_4<0\)。
这是**完整条件律**的严格结论，不是重叠变量替代完整输出。

还可直接决定主文里一个真正未支付的项的符号。
主文已证明 \(n=8\) 仅第 \(4\) 层有相对熵缺陷，且
\[
\pi_4(a)=c^4Q_4(\xi),\quad
Q_4=1+20\xi+90\xi^2+140\xi^3+70\xi^4 .
\]
所以在 \(c=19/20,a_*=1/40,\xi_*=1/1520\) 上，
\[
\boxed{
\sum_l\pi_l''(a_*)R_l(a_*)
=-2c^3Q_4'(\xi_*)R_4(\xi_*)<0.} \tag{CL15}
\]
这里 \(R_4>0\) 来自主文已证的全律不相等及 KL 严格性，
而 \(Q_4'>0\) 来自显式正系数，不需要数值计算。

还可给出不含未知 KL 的定量版本。把四层律映到事件
\(S=\{0,2,4,6\}\)，两律的事件概率差为 \(e_4/80\)，
其中 \(e_4=Q_4^{-1}-(Q_2/Q_4)^{10/7}<0\)。
二点 KL 关于第一个概率的二阶导数为 \(1/[x(1-x)]\ge4\)，
所以数据处理与积分余项给出 \(R_4\ge e_4^2/3200\)。因此
\[
\sum_l\pi_l''(a_*)R_l(a_*)
\le-\frac{c^3Q_4'(\xi_*)}{1600}
\left[Q_4(\xi_*)^{-1}
-\left(\frac{Q_2(\xi_*)}{Q_4(\xi_*)}\right)^{10/7}\right]^2<0. \tag{CL16}
\]
这只用一个真实配置事件，不需要层配置枚举。

(CL15) 说明移动权重确实可以给调制相对熵带来不利曲率。
它**不**决定 \(\mathcal L_8''+\sum_l\pi_l''R_l+\sum_l\pi_lR_{l,aa}\)
的总符号，不否定任何 \(n\to\infty\) 的 \(o(n)\) 升级，
也不反驳真实熵凹性。
