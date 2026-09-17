> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA05｜Jacobi–Duhamel 调制相对熵桥接

**任务：** `randomcat4/dpp-stationary-entropy`，PR #118，分支
`research/sine-entropy-tool-3-round-prompts`，`TASK_05_TRUE_CORRECTED_BRIDGE.md`。  
**状态：PROVED（下述结构与局部单侧引理）／DISPROVED（明确的全域规则）／INCOMPLETE（目标级渐近桥接）。**  
所有对数为自然对数。本文没有改变指定的 corrected law；没有使用静态接近推出导数接近。
完整证明适用于任务固定的循环模型，不涉及 Toeplitz 或熵率传递。

## 0. 交付摘要与边界

构造的对象不是单一距离，而是一个三部件工具：

\[
\boxed{\quad
\text{Jacobi 参数残差算子}
\quad+\quad
\text{Duhamel 模式传递}
\quad+\quad
\text{移动图能量中的调制相对熵}.
\quad}                                                     \tag{0.1}
\]

它给出四项新的、可独立使用的结论。

1. **所有模式，而非只有配对势。** 真实条件律的每个 Johnson 模式都有显式乘子，
   满足同一个二阶参数方程。指定修正律的残差恰好因式分解为
   \(L_l(L_l+\gamma_{2,l}I)\widehat r_l\)，常数及度二被精确消去。
   Fourier 补集对称性进一步消去全部奇数模式。因此 \(n=4,6\) 两律其实完全相等；
   首个确实激发的缺陷在 \(n=8,l=4,j=4\)。
2. **精确的非线性误差账本。** 熵差分为高模式对熵梯度的线性偏差与
   \(D(q_l\Vert\widehat q_l)\)。后者的二阶导数包含一个正平方项，
   并完整保留移动参考与移动计数响应。
3. **中点的无条件单侧桥接。** 定义
   \[
   \mathcal L_n(a)=\sum_l\pi_l(a)
       \langle r_l(a)-\widehat r_l(a),\log\widehat r_l(a)\rangle_{u_l},
   \qquad R_l=D(q_l\Vert\widehat q_l).
   \]
   对每个偶数 \(n\ge4\)，任务固定的 \(c=19/20,\ a_*=1/40\) 满足
   \[
   \boxed{
   E_n''(a_*)\ge
   \mathcal L_n''(a_*)+\sum_l\pi_l''(a_*)R_l(a_*)-C_{\rm src},
   \quad C_{\rm src}=\frac{349998584954880000}{2401}.}            \tag{0.2}
   \]
   常数很粗、没有实际小维数数值优势，但**与 \(n\) 无关**。
   更有用的精确可计算常数及无原子下界的图逆范数见 §5。
   因而非线性相对熵的**层内**不利曲率已付成 \(O(1)\)；
   不能把剩下两项删除。
4. **合法的失败出口。** \(n=8\) 排除用正随机 Johnson 时钟混合恢复真实律；
   还解析证明存在合法 \(a_+,a_-\in(0,1/20)\)，使
   \(E_8''(a_+)>0>E_8''(a_-)\)。这是存在型反例，不是已定位的数值参数证书。
   它既不判定中点符号，也不否定 \(o(n)\) 渐近，更不否定真实熵凹性。

**未完成：** \(\mathcal L_n''+\sum_l\pi_l''R_l\ge-o(n)\)、
中点全 \(n\) 曲率符号、以及循环到 Toeplitz 的传递。
(0.2) 没有把所求 Hessian 比较界藏在前提中：右侧只含显式模式/熵梯度 jets、
静态相对熵和已付常数。

## 1. 域外迁移：来源、失效条件与新增构件

### 1.1 相对熵与后验残差，而不是距离的形式微分

PDE 相对熵／调制能量方法将解与一个有缺陷的光滑重构比较：
凸熵提供二次余项，演化方程把余项导数变成耗散与残差配对。
Giesselmann–Makridakis–Pryer 的后验分析 [R1] 是这里的具体来源。
其定理需要凸熵的定量控制、正则参考和受控演化残差；它没有允许
“两个参数族在每一点很近，所以参数 Hessian 很近”。

本题对应为：真实密度 \(f_l\)、参考 \(g_l=\widehat r_l\)、凸函数
\(x\log x\)，以及下文**推导出来**的参数演化残差 \(F_l\)。
直接迁移失效有两点：参数 \(a\) 不是 Johnson 热时间；
参考律及层质量都随 \(a\) 移动。新增构件是
\(\xi=a(1-c-a)/c\) 的精确演化、加速项、模式残差和全部移动权重项。

### 1.2 Duhamel 误差传递

有限维线性演化中的“共同演化＋源项”可把轨道差写成传播子作用于残差的积分。
这里不是预设真实律服从热方程，而是先证明它服从 Jacobi 型二阶参数方程；
把指定单钟修正代入后得到已知源。一个正标量 Green 核将该源传给每个模式。
另一个一阶 Duhamel 公式将真实热残差传给密度差。
标量核的正性不等于整个投影算子保持原子正性，更不等于熵曲率有符号。
一个通用警告是：在三点均匀空间上，\(v=(1,-2,1)\)，
\(B=vv^\top\) 为半正定且 \(B1=0\)，但正密度
\(f=(3/10,9/10,9/5)\) 满足
\(\langle Bf,\log f\rangle_u=(1/10)\log(2/3)<0\)。
因此不能把谱半正定的 \(L(L+\gamma_2 I)\) 自动当成 Markov 熵耗散；
本例仅解释方法障碍，真正固定模型的反例在 §6。

### 1.3 非 DPP 的图能量接口

共同 Markov 演化下，两条移动律之间的 KL 有一个精确耗散。
本文将其写为随两律移动的图 Dirichlet 型能量，并以其对偶范数支付源项。
为了避免最小原子概率导致的指数常数，再用一般强对数凹齐次分布的
down-up 谱隙定理 [R4, Theorem 1.1]，通过逐边比较应用到本题条件律。
该外部定理本身不是熵 Hessian 定理；新增步骤是导通率、Schur 补、
重叠 score 与度二消去。没有新颖性优先权声明。

## 2. 固定模型与候选对象

设 \(n=2k,\ c=19/20,\ a\in(0,1-c)\)，
\[
P_{st}=\frac1n\sum_{r=0}^{k-1}e^{2\pi i r(s-t)/n},\qquad
\nu(A)=\det P_A\quad(|A|=k).
\]
真实输出仍是 \(\operatorname{DPP}(aI+cP)\)，或条件独立信道
\(\Pr(Y_i=1\mid A)=a+c1_{\{i\in A\}}\)。完整原子为
\[
p_a(S)=(-1)^{n-|S|}
 \det(aI+cP-\operatorname{diag}(1_{S^c})).
\]
真实计数权重和条件律由
\[
\sum_{l=0}^n\pi_l(a)t^l
=[1-a-c+(a+c)t]^k[1-a+at]^k,\qquad q_l(S)=p_a(S)/\pi_l
\]
定义。最大重叠核在 \(l\le k\) 时均匀选取 \(A\) 的 \(l\)-子集，
在 \(l\ge k\) 时均匀选取包含 \(A\) 的 \(l\)-集：
\[
r_l^{\max}(S)=\binom nl\sum_A\nu(A)T_l^{\max}(S\mid A).
\]
这不是把输入先验改为均匀律。若 \(l=m\le k\)，也有
\(r_l^{\max}(S)=\binom nl\,\det P_S/\binom kl\)；
上层用补集。比较的完整修正律始终为
\(\widehat p_a(S)=\pi_l(a)\widehat q_l(S)\)，使用**相同真实计数**。
定义
\[
E_n=\sum_l\pi_l[D(q_l\Vert u_l)-D(\widehat q_l\Vert u_l)]
=\widehat H_n-H_n.
\]
所以 \(H_n''-\widehat H_n''=-E_n''\)，这只是任务中的记账输入。

写
\[
N_l=\binom nl,\quad u_l=N_l^{-1},\quad
f_l=q_l/u_l,\quad g_l=\widehat q_l/u_l,\quad
\delta_l=f_l-g_l,\quad C_l=l(n-l),\quad m=\min(l,n-l).
\]
内积均为 \(\langle v,w\rangle_{u_l}=\sum_{|S|=l}u_l(S)v(S)w(S)\)。
\(L_l\) 保持任务的总速率一归一化。用
\[
\nu_j=j(n-j+1),\qquad\gamma_{j,l}=\nu_j/C_l
\]
表示本节的谱数；\(\nu_j\) 与输入概率 \(\nu(A)\) 通过下标区分。

**参数与导数约定。**
\[
\xi=\frac1{z-1}=\frac{a(1-c-a)}c,\qquad
\xi_a=\frac{1-c-2a}{c},\quad \xi_{aa}=-\frac2c,\quad
\xi_*=\frac1{1520}.                                        \tag{2.1}
\]
下标 \(a,\xi\) 明确标明微分变量；无下标的 \(\pi_l',E_n''\) 只指 \(a\) 导数。
以下层对象在 \(\xi=0\) 使用解析延拓值，不把端点零概率计数条件事件
当作已经有定义的普通条件概率。

对 \(m\ge2\)，置 \(d=k-m+1\)，
\[
Q_r^{(d)}(\xi)=
\sum_{s=0}^r
\frac{r_{\underline s}(r+2d-1)^{\overline s}}
     {d^{\overline s}s!}\xi^s,\qquad 0\le r\le m.             \tag{2.2}
\]
本层中省略上标 \(d\)。令 \(\mathsf P_{l,j}\) 为 \(L_l\) 的正交谱投影，
\(v_{l,j}=\mathsf P_{l,j}r_l^{\max}\)。候选的模式数据为
\[
\theta_{l,j}=\frac{Q_{m-j}}{Q_m},\quad
\tau_l=-\frac{\log\theta_{l,2}}{\gamma_{2,l}},\quad
\psi_{l,j}=\theta_{l,2}^{\gamma_{j,l}/\gamma_{2,l}},\quad
e_{l,j}=\theta_{l,j}-\psi_{l,j}.                             \tag{2.3}
\]
这里 \(\tau_l\) 正是题目的 \(\widehat\tau_l\)，不是另造修正律。

完整的候选工具还包含
\[
F_l=f_{l,\xi}-\tau_{l,\xi}L_lf_l,\qquad
R_l=\langle f_l\log(f_l/g_l)\rangle_{u_l},\qquad
\mathcal L_n=\sum_l\pi_l\langle\delta_l,\log g_l\rangle_{u_l}.
                                                               \tag{2.4}
\]
\(F_l\) 可由 (2.2)–(2.3) 或 §5.3 的一维公式直接构造，不是未知余项的命名。

## 3. P1：全模式、必要 jets 与归一

### 定理 3.1（真实的全模式乘子）

对每个任务中的 \(n,l,a\)，
\[
f_l=\sum_{j=0}^{m}\theta_{l,j}v_{l,j},\qquad
g_l=\sum_{j=0}^{m}\psi_{l,j}v_{l,j}.                          \tag{3.1}
\]
\(\theta_{l,0}=\psi_{l,0}=1\)。\(m\le1\) 两律均为均匀律。
对 \(m\ge2\)，(2.3) 的 \(\theta_{l,2}\) 等于任务给定的有理式。

**证明。** 先设 \(l=m\le k\)。给定 \(A\)，层条件核为
\[
T_\xi(S\mid A)=\frac{z^{|A\cap S|}}{Z_{n,m}(z)}.
\]
取互不相交的 \(j\) 对站点并测试
\(h_j(S)=\prod_{r=1}^j(1_{i_r\in S}-1_{o_r\in S})\)。
若某对在 \(A\) 中的状态相同，交换该对使条件期望为零；
否则每对的四项相减贡献 \(z-1\)。因此
\[
\mathbb E[h_j(S)\mid A]=
\frac{(z-1)^j\sum_h\binom{k-j}{h}\binom{k-j}{m-j-h}z^h}
 {Z_{n,m}(z)}\,h_j(A).                                    \tag{3.2}
\]
最大重叠核的同一条件期望为
\(\alpha_jh_j(A)\)，\(\alpha_j=m_{\underline j}/k_{\underline j}\)。
这些成对差多项式张成第 \(j\) Johnson 谐波空间；可用直接换位计算其特征值，
以及 slice 谐波基的维数结论 [R2]。故真正的乘子是 (3.2) 的系数除以
\(\alpha_j\)，这同时比较了该模式空间的全部测试，而非单一势。

二项展开给出
\[
\xi^mZ_{n,m}(1+\xi^{-1})=\binom{k}{m}Q_m^{(d)}(\xi).
\]
把 \(k,m\) 同时改成 \(k-j,m-j\)，\(d\) 不变；
\(\binom{k-j}{m-j}/\binom{k}{m}=\alpha_j\)，得 (2.3)。
上层对 \(S,A\) 同时取补集，用下面的补集对称性，即归到 \(m=n-l\)。
热半群的谱公式给出 \(g_l\)。证毕。

### 定理 3.2（本题的奇数消去与最小维数）

对所有 \(l\)，\(v_{l,j}=0\) 当 \(j\) 为奇数。因此
\[
\delta_l=\sum_{\substack{4\le j\le m\\j\ {\rm even}}}
e_{l,j}v_{l,j}.                                           \tag{3.3}
\]
特别地，\(n=4,6\) 的所有合法 \(a\) 都满足 \(p_a=\widehat p_a\)，故
\(E_n\equiv0\)，包括全部 jets。

**证明。** \(D=\operatorname{diag}((-1)^s)\) 将前半 Fourier 频率移到后半，
故 \(DPD^*=I-P\)。补集 DPP 的核是 \(I-P\)，对角酉共轭不改变主子式，
故 \(\nu(A^c)=\nu(A)\)。在 \(k\)-slice，补集对 \(h_j\) 的作用是
\((-1)^j\)，所以输入全部奇数谐波为零。最大重叠核的 (3.2) 对应式将这一
消去传到每一层。剩余 \(j=0,2\) 精确匹配；\(m\le3\) 无其他模式。证毕。

**归一与正性。** \(v_{l,0}=1\)，其他模式均值为零；所以每层
\(\langle f_l\rangle=\langle g_l\rangle=1\)，一、二阶 jets 的均值均为零。
真实核在信道内部严格正，修正热核严格正。Fourier Vandermonde 公式还给出
\(r_l^{\max}>0\)，故 \(\xi=0\) 附近的 KL 与模式 jets 也是解析的。
这些事实不声称概率原子在 \(n\to\infty\) 时有统一正下界。

**必要 jets。** 直接按 (3.1) 微分：
\[
f_{l,a}=\xi_a\sum_j\theta_{l,j,\xi}v_{l,j},\quad
f_{l,aa}=\xi_a^2\sum_j\theta_{l,j,\xi\xi}v_{l,j}
-\frac2c\sum_j\theta_{l,j,\xi}v_{l,j}.                       \tag{3.4}
\]
\(g_l\) 同式换成 \(\psi\)，或使用
\[
g_{l,a}=\tau_{l,a}L_lg_l,\quad
g_{l,aa}=\tau_{l,aa}L_lg_l+\tau_{l,a}^2L_l^2g_l.            \tag{3.5}
\]
因此中点不只是 \(\tau_{l,a}=0\)，而且
\(f_{l,a}=g_{l,a}=\delta_{l,a}=0\)。
仍有 \(\pi_l''\epsilon_l\)，不可删去。

### 定理 3.3（已知源的二阶残差与 Green 传递）

置
\[
A(\xi)=\xi(1+\xi),\qquad
B_l(\xi)=d(1+2\xi)+2A(\xi)\frac{Q_m'(\xi)}{Q_m(\xi)},\qquad
\mathscr D_l=A\partial_\xi^2+B_l\partial_\xi-C_lL_l .
\]
则
\[
\mathscr D_l f_l=0,\qquad
\mathscr D_l g_l
=A\tau_{l,\xi}^2L_l(L_l+\gamma_{2,l}I)g_l,                 \tag{3.6}
\]
\[
\boxed{\mathscr D_l\delta_l
=-A\tau_{l,\xi}^2L_l(L_l+\gamma_{2,l}I)g_l,\quad
\delta_l(0)=\delta_{l,\xi}(0)=0.}                          \tag{3.7}
\]

**证明。** (2.2) 的系数递推为
\[
\frac{q_{s+1}}{q_s}
=\frac{(r-s)(r+s+2d-1)}{(s+1)(s+d)}.
\]
因此 \(AQ_r''+d(1+2\xi)Q_r'=r(r+2d-1)Q_r\)。
商法则及
\(m(m+2d-1)-(m-j)(m-j+2d-1)=\nu_j\) 给出
\[
A\theta_{l,j,\xi\xi}+B_l\theta_{l,j,\xi}+\nu_j\theta_{l,j}=0. \tag{3.8}
\]
度二方程等价于
\[
A\tau_{l,\xi\xi}+B_l\tau_{l,\xi}
-A\gamma_{2,l}\tau_{l,\xi}^2=C_l.
\]
代入 \(g=e^{\tau L}r^{\max}\) 即得 (3.6)。
由 \(Q_r(0)=1,\ Q_r'(0)=r(r+2d-1)/d\)，真实与修正初始一阶
jets 均为 \(-\nu_j/d\)。证毕。

令 \(M_l=A^dQ_m^2\)。对 \(\xi>t>0\)，定义
\[
G_{l,j}(\xi,t)=
\theta_{l,j}(\xi)\frac{M_l(t)\theta_{l,j}(t)}{A(t)}
\int_t^\xi\frac{ds}{M_l(s)\theta_{l,j}(s)^2}>0.             \tag{3.9}
\]
对 \(y=\theta_jv\)，方程 (3.8) 的非齐次型可写为
\[
(M_l\theta_j^2v')'=\frac{M_l\theta_j}{A}\,{\rm source}.
\]
在零端点选取解析零数据解，二次积分即证明
\[
\boxed{
e_{l,j}(\xi)=
-\gamma_{j,l}(\gamma_{j,l}-\gamma_{2,l})
\int_0^\xi G_{l,j}(\xi,t)A(t)\tau_{l,\xi}(t)^2\psi_{l,j}(t)\,dt .
}                                                        \tag{3.10}
\]
在 \(d=1\) 时核有可积的对数端点行为；\(d>1\) 也可积。
\((M_l\theta_j')'=-\nu_j(M_l/A)\theta_j\) 证明
\(\theta_j'<0\)（\(j>0\)），故 \(\tau_{l,\xi}>0\)。

于是每个 \(j>2\) 都严格满足 \(\theta_j<\psi_j\)；
但这只是**模式系数**顺序。它不给 KL 或 \(E_n''\) 赋号。
解析展开还给出
\[
e_{l,j}=
-\frac{\nu_j(\nu_j-\nu_2)}{2d^2(d+1)}\xi^2+O_{n,l}(\xi^3). \tag{3.11}
\]
余项未声称在 \(n\) 上一致，不把固定 \(\xi_*\) 当作渐近小参数。

一阶残差与 Duhamel 形式为
\[
F_l=\sum_j(\theta_{l,j,\xi}
             +\gamma_{j,l}\tau_{l,\xi}\theta_{l,j})v_{l,j},
\quad
\delta_l(\xi)=\int_0^\xi
e^{[\tau_l(\xi)-\tau_l(t)]L_l}F_l(t)\,dt.                 \tag{3.12}
\]
它在所有未激发模式、常数及度二上为零。
(3.7) 的源只用修正律；(3.12) 的源也有显式真核表达。两种版本可相互审计。

## 4. P2：相同 jets 时消失；移动参考与非线性误差全展开

以下恒等式对任意正的 \(C^2\) 归一密度 \(f_a,g_a\) 都成立。
写 \(\delta=f-g,\ h=\delta/g,\ s=g_a/g\)，则
\[
D(uf\Vert u)-D(ug\Vert u)
=\langle\delta,\log g\rangle_u+R,\qquad
R=\langle g[(1+h)\log(1+h)-h]\rangle_u
=D(uf\Vert ug).                                         \tag{4.1}
\]
精确地
\[
R_a=\langle\delta_a,\log(1+h)\rangle_u
+\langle g_a,\log(1+h)-h\rangle_u,                       \tag{4.2}
\]
\[
\boxed{
R_{aa}=
\langle\delta_{aa},\log(1+h)\rangle_u
+\langle g_{aa},\log(1+h)-h\rangle_u
+\left\langle\frac{(\delta_a-s\delta)^2}{f}\right\rangle_u .
}                                                        \tag{4.3}
\]
这是移动参考的式子；把 \(g_a,g_{aa}\) 冻结会删掉必要项。
证明只需对 (4.1) 连续微分并用
\(h_a=(\delta_a-s\delta)/g\)。正平方项是不能丢失的非线性二阶结构。

线性偏差 \(L_l^{\rm lin}=\langle\delta_l,\log g_l\rangle_{u_l}\) 的 jets 为
\[
(L_l^{\rm lin})_a
=\langle\delta_{l,a},\log g_l\rangle+\langle\delta_l,s_l\rangle,
\]
\[
(L_l^{\rm lin})_{aa}
=\langle\delta_{l,aa},\log g_l\rangle
+2\langle\delta_{l,a},s_l\rangle+\langle\delta_l,s_{l,a}\rangle. \tag{4.4}
\]
在完整配置上，
\[
E_n=\mathcal L_n+\mathcal R_n,\qquad
\mathcal R_n=\sum_l\pi_lR_l=D(p_a\Vert\widehat p_a),\quad
\widehat p_a(S)=\pi_lu_lg_l(S).                            \tag{4.5}
\]
故
\[
E_n''=\mathcal L_n''
+\sum_l\{\pi_l''R_l+2\pi_l'R_{l,a}+\pi_lR_{l,aa}\}.         \tag{4.6}
\]
这与题目式 (1) 完全一致。两族及其所需 jets 相同时，
\(\delta,\delta_a,\delta_{aa}=0\)，以上每个缺陷均为零。
单一度二匹配只消去 (3.3) 以外的密度模式；\(\log g\) 一般仍有高模式。

### 4.1 任意内部点的显式局部 C² 下界

若 \(|h_l|\le\rho_l<1\)，设
\[
\eta_{l,r}^2=\langle(\partial_a^r\delta_l)^2/g_l\rangle,\quad
S_l=\|g_{l,a}/g_l\|_\infty,\quad
T_l=\|(g_{l,aa}/g_l)_+\|_\infty .
\]
由 \(|\log(1+h)|\le|h|/(1-\rho)\) 及
\(0\le h-\log(1+h)\le h^2/[2(1-\rho)]\)，(4.2)–(4.3) 给出
\[
\begin{aligned}
E_n''\ge\mathcal L_n''-\sum_l\frac1{1-\rho_l}\big[
&\tfrac12(\pi_l'')_-\eta_{l,0}^2\\
&+2|\pi_l'|(\eta_{l,0}\eta_{l,1}
                       +\tfrac12 S_l\eta_{l,0}^2)\\
&+\pi_l(\eta_{l,0}\eta_{l,2}+\tfrac12T_l\eta_{l,0}^2)\big].
\end{aligned}                                             \tag{4.7}
\]
这里 \(x_-=\max(-x,0)\)。\(R_l\le\eta_{l,0}^2/[2(1-\rho_l)]\)
可由 \(x\log x\) 的积分二阶余项证明。
这是已闭合的有限维局部引理；没有断言本题存在全 \(n\) 一致的 \(\rho<1\)。
下节中点引理**不需要**这一接近前提。

## 5. P3：中点图能量桥接及与 n 无关的源项支付

### 5.1 移动图能量与无条件单侧引理

固定一层，以下导数为 \(\xi\) 导数。令
\(\ell=\log(f/g)\)，\(Q_{ST}=1/C_l\) 当 \(S,T\) 为 Johnson 邻居。
共同热演化与源项给出
\[
R_\xi=-\tau_\xi\mathcal D(f,g)+\langle F,\ell\rangle_u,      \tag{5.1}
\]
\[
\mathcal D(f,g)=\sum_{S,T}u(S)Q_{ST}f(S)
 \{e^{\ell(T)-\ell(S)}-1-[\ell(T)-\ell(S)]\}\ge0.           \tag{5.2}
\]
为核对移动参考，直接微分 \(R\) 得
\(\langle f_\xi,\log(f/g)\rangle-\langle f,g_\xi/g\rangle\)；
代入共同 \(L\)，使用 \(u(S)Q_{ST}=u(T)Q_{TS}\) 后正好是 (5.1)。

设
\[
K(t)=\int_0^1(1-s)e^{st}\,ds
=\frac{e^t-1-t}{t^2},\quad K(0)=\frac12,
\]
\[
w_{ST}=u(S)Q_{ST}
 [f(S)K(\ell(T)-\ell(S))+f(T)K(\ell(S)-\ell(T))].
\]
定义自伴负半定图算子
\[
(\mathsf A_{f,g}v)(S)=u(S)^{-1}\sum_Tw_{ST}[v(T)-v(S)].
\]
于是 \(\mathcal D=-\langle\ell,\mathsf A_{f,g}\ell\rangle_u\)。
Johnson 图连通、两律正，故其核恰为常数。定义**明确的对偶源能量**
\[
J_l^2=\langle F_l,(-\mathsf A_{f_l,g_l})^\dagger F_l\rangle_{u_l}.
\]
\(F_l\) 均值为零。对偶 Cauchy–Schwarz 和完成平方给出
\[
R_{l,\xi}\le-\tau_{l,\xi}\mathcal D+J_l\sqrt{\mathcal D}
\le \frac{J_l^2}{4\tau_{l,\xi}}.
\]
中点 \(\xi_a=0,\xi_{aa}=-2/c\)，因而
\[
\boxed{
E_n''(a_*)\ge
\mathcal L_n''(a_*)+\sum_l\pi_l''(a_*)R_l(a_*)
-\sum_{\{l:m\ge4\}}\frac{\pi_l(a_*)J_l^2}{2c\tau_{l,\xi}(\xi_*)}.
}                                                        \tag{5.3}
\]
这是原始的精确局部桥接。全部常数/量均已定义；
不需要原子比接近，不假设未知的二阶 KL 稳定性。

中点线性项也完全显式。记
\(U_l=\{j:4\le j\le m,\ j\text{ 偶数}\}\)，则
\[
\begin{aligned}
\mathcal L_n''(a_*)=\sum_l\sum_{j\in U_l}\bigg[
&\left(\pi_l''e_{l,j}-\frac{2\pi_l}{c}e_{l,j,\xi}\right)
       \langle v_{l,j},\log g_l\rangle\\
&-\frac{2\pi_l}{c}\tau_{l,\xi}e_{l,j}
       \langle v_{l,j},L_lg_l/g_l\rangle\bigg]_{\xi=\xi_*}. \end{aligned} \tag{5.4}
\]
这显示未匹配模式如何进入题目式 (1)，并显示为何系数的同号不决定总熵符号。

### 5.2 从移动能量到强对数凹 down-up：避免指数原子常数

由 \(K(t)K(-t)\ge1/4\)，
\[
w_{ST}\ge u(S)Q_{ST}\sqrt{f(S)f(T)}
          \ge Q_{ST}\min(q_l(S),q_l(T)).                  \tag{5.5}
\]
最后一项是以 \(q_l\) 为不变律的 Johnson Metropolis 链导通率。

真实完整 DPP 的 \(L\)-ensemble 矩阵为
\[
\Lambda=(aI+cP)(I-aI-cP)^{-1},
\]
特征值位于
\([\lambda_-,\lambda_+]=[a/(1-a),(a+c)/(1-a-c)]\)，比值
\(\lambda_+/\lambda_-=z\)。条件 \(m\)-层权重正比于 \(\det\Lambda_S\)；
上层先取补集。对 \(s\ne t\)，该投影满足
\[
P_{st}=\frac1n e^{\pi i(k-1)(s-t)/n}
          \frac{\sin(\pi k(s-t)/n)}{\sin(\pi(s-t)/n)} .
\]
用对角元素 \(e^{-\pi i(k-1)s/n}\) 的酉矩阵共轭后，得到实对称矩阵；
所有主子式不变。故可直接应用 [R4] 对实对称正定 \(L\)-ensemble 的强对数凹性结论
及其 down-up 谱隙 \(1/m\)。

这里仍须支付生成元归一化。若相邻状态共有 \(B\)，\(|B|=m-1\)，
令 \(\sigma_i=\det\Lambda_{B+i}/\det\Lambda_B\)。
Schur 补给出 \(\lambda_-\le\sigma_i\le\lambda_+\)。
down-up 非对角转移率为
\[
P^\downarrow(S,T)=\frac1m\frac{\sigma_j}{\sum_{h\notin B}\sigma_h},
\]
而 Metropolis 率为
\(C_l^{-1}\min(1,\sigma_j/\sigma_i)\)。
二者之比不超过
\((n-m)\max(\sigma_i,\sigma_j)/\sum_h\sigma_h\le z\)。
故 Metropolis 连续生成元谱隙至少 \(1/(zm)\)，由 (5.5) 与对偶变分式
\[
\boxed{J_l^2\le zm\,\langle F_l^2/f_l\rangle_{u_l}.}        \tag{5.6}
\]
没有使用 \(\min_S q_l(S)\)。外部谱隙定理只应用于真实条件律，
没有假定 corrected law 也强对数凹。

### 5.3 源的严格一维表达与度二消去

固定输入 \(A\)，令 \(J=|S\cap A|\)，在条件真核下
\[
w_j=\frac{\binom kj\binom k{m-j}z^j}{Z_{n,m}(z)},\quad
\mu=\mathbb E_wJ,\quad X=J-\mu,\quad
v=\mathbb E_wX^2,\quad \mu_r=\mathbb E_wX^r .
\]
令 \(t_A(S)=N_lT_\xi(S\mid A)\)。
重叠的 Johnson 上、下跳率分别为
\[
b_j=\frac{(m-j)(k-j)}{C_l},\qquad
d_j=\frac{j(k-m+j)}{C_l}.
\]
直接计算（不作渐近）得到
\[
\frac{\partial_\xi t_A}{t_A}=-\frac X{A(\xi)},\qquad
\frac{L_lt_A}{t_A}=\frac{X^2-v+\beta X}{A(\xi)C_l},
\quad\beta=2\mu-m-k-n\xi .
\]
所以
\[
\frac{(\partial_\xi-\tau_\xi L_l)t_A}{t_A}
=W(J)=-\kappa[X^2-v+bX],\quad
\kappa=\frac{\tau_\xi}{A(\xi)C_l},\quad
b=\beta+C_l/\tau_\xi.                                   \tag{5.7}
\]
对共同输入先验用条件 Jensen，不需要任何配置枚举：
\[
\boxed{
\langle F_l^2/f_l\rangle_{u_l}
\le\mathbb E_wW^2
=\kappa^2[\mu_4-v^2+2b\mu_3+b^2v].
}                                                        \tag{5.8}
\]
这是只含 \(m+1\) 个重叠值的显式源支付公式；不是把 count 当成完整输出。

还可从匹配直接得到强于粗界的消去。多项式
\[
h_2(J)=(J-m/2)^2-\frac{C_l}{4(n-1)}
\]
是纯度二。真核的热残差与它正交，故 \(\mathbb E_w[W h_2]=0\)，即
\[
b=-\frac{\mu_4-v^2+(2\mu-m)\mu_3}
          {\mu_3+(2\mu-m)v}.                             \tag{5.9}
\]
此式不是额外拟合参数，是 (5.7) 的严格恒等式。
下面给出分母的正下界及统一常数。

### 5.4 显式的 n 一致源支付

以下推导只用初等矩界、正交多项式零点和已验证的 (5.9)。

**时钟界。** \(Q_r^{(d)}(\xi)\) 是
\(P_r^{(d-1,d-1)}(1+2\xi)/P_r^{(d-1,d-1)}(1)\)。
正交权重在 \((-1,0)\) 为正，零点位于该区间并相互交错 [R3]。
故 \(Q_{r-1}/Q_r\) 有正留数的部分分式
\(\sum_i a_i/(\xi+\lambda_i)\)，\(0<\lambda_i<1\)，从而其负对数导数介于
\(1/(1+\xi)\) 与 \(1/\xi\)。把度二商写成相邻两商之积得
\[
\frac{C_l}{(n-1)(1+\xi)}
\le\tau_{l,\xi}\le\frac{C_l}{(n-1)\xi},
\qquad \frac m{\tau_{l,\xi}}\le2(1+\xi).                  \tag{5.10}
\]
正留数也可由相邻正交多项式的交错零点与相同正首项直接验证。

**重叠矩界。** 同一零点事实使 \(Z_{n,m}(z)\) 的全部零点为负实数。
因而 \(Z_{n,m}(zt)/Z_{n,m}(z)\) 是若干 Bernoulli 概率生成函数之积；
这里仅对重叠变量 \(J\) 使用 Poisson-binomial 表示。
它给出
\[
|\mu_3|\le v,\qquad \mu_4\le3v^2+v,\qquad
v\le m-\mu .
\]
由 \(\mathbb E_w[L_lt_A/t_A]=0\)，置 \(y=m-\mu\)，还得到
\[
y^2+(k-m+n\xi)y+v=mk\xi.
\]
除以 \(mk\)，利用 \(m/k\le1\)，可得
\[
0\le y/m\le\sqrt{\xi(1+\xi)}-\xi.
\]
在任务中点右侧为 \(1/40\)，于是
\[
v\le m/40,\qquad 2\mu-m\ge(19/20)m.
\]
对有缺陷的 \(m\ge4\)，(5.9) 的分母至少
\(((19/20)m-1)v>0\)，且
\[
|b|\le
\frac{(21/20)m+1}{(19/20)m-1}\le\frac{13}{7}.             \tag{5.11}
\]
这是支付潜在 \(O(m)\) 线性 score 的关键，不能用无差别矩界替代。

记
\[
\xi_*=\frac1{1520},\quad A_*=\frac{1521}{1520^2},
\quad z_*=1521,\quad
K_W=\frac{(4/7)^2\{2(1/40)^2+(20/7)^2/(160)\}}
                   {A_*^2\xi_*^2}.
\]
因为 \(m/(n-1)\le4/7\)，(5.8)、(5.10)–(5.11) 给出
\[
\mathbb E_wW^2
\le\frac{2m^2/40^2+(20/7)^2m/40}
         {(n-1)^2A_*^2\xi_*^2}\le K_W .
\]
结合 (5.6)、\(\sum_l\pi_l\le1\)，
\[
\sum_{m\ge4}\frac{\pi_lJ_l^2}{2c\tau_{l,\xi}}
\le \frac{z_*(1+\xi_*)}{c}K_W
=\frac{349998584954880000}{2401}=C_{\rm src}.              \tag{5.12}
\]
这证明 (0.2)。此常数约为 \(1.46\times10^{14}\)，保守到不适合小维数诊断；
它的严格价值是无 \(n\) 因子、无隐含最小原子常数。
实际计算应使用 (5.3)、(5.6)、(5.8)，而非此最坏界。

### 5.5 移动权重能付到哪里

式 (0.2) 可进一步写成
\[
E_n''(a_*)\ge\mathcal L_n''(a_*)
-\sum_l(\pi_l''(a_*))_-R_l(a_*)-C_{\rm src}.               \tag{5.13}
\]
如需只用一维静态量，令 \(\widehat w_l\) 为上述重叠 birth-death 链
从 \(J=m\) 出发、运行 \(\tau_l\) 后的分布。
真、修正的给定 \(A\) 核在同一重叠类内都均匀，且输入先验相同，故数据处理给出
\[
R_l\le D(w_l\Vert\widehat w_l).                           \tag{5.14}
\]
这里只把静态 KL 用在 (5.13) 的静态位置，**没有对 (5.14) 微分**。

计数 PGF 的独立 Bernoulli 表示还给出
\[
\sum_l(\pi_l'')_-\le I(a),\quad
I(a)=\frac{k}{(a+c)(1-a-c)}+\frac{k}{a(1-a)},
\quad I(a_*)=\frac{4n}{1-c^2}.                            \tag{5.15}
\]
证明：完整 latent score 为 \(T\)，其 log 加速为 \(V\le0\)；
\(\mathbb ET^2=-\mathbb EV=I\)，所以
\(\sum|\pi_l''|\le\mathbb E|T^2+V|\le2I\)，再用
\(\sum\pi_l''=0\)。这比逐项 \(O(n^2)\) 粗界强，但只给 \(O(n)\)，不是 \(o(n)\)。

中点的权重也能直接核查。若 \(\mu_m\) 是 (5.7) 的重叠均值
（\(m=0\) 时取 \(0\)），则
\[
\frac{\pi_l'}{\pi_l}(a_*)=\frac{4(l-k)}{1-c^2},\qquad
\frac{\pi_l''}{\pi_l}(a_*)=
\frac{16}{(1-c^2)^2}
\left[(l-k)^2-\frac{k(1+c^2)}2+c(2\mu_m-m)\right].         \tag{5.15a}
\]
证明是在计数的独立 Bernoulli 表示中对两个组分别求 score，再条件于总数。
第一式通常不为零。两条完整输出律的中点 score 相同，故完整 Fisher 项
确实相消；这并不使第二式消失，也不能冻结计数权重。

也可保留任务已给出的**有符号**计数运输
\(\sum_l\pi_l''R_l=\sum_rB_r\Delta^2R_r\)。
升级需要真实的跨层平滑/抵消；一个 \(R_l=O(1)\) 的静态界仍不够。

### 5.6 一个带移动权重阻尼的邻域版本

中点并非只能作为孤立点使用。以下公式给出固定 \(n\) 的可检查邻域，
但不声称邻域宽度在 \(n\) 上一致。仍令
\[
Z_l=L_l(L_l+\gamma_{2,l}I)g_l,\qquad
\mathcal Q_l=\left\langle
 \frac{(f_{l,\xi}-f_lg_{l,\xi}/g_l)^2}{f_l}\right\rangle_{u_l}.
\]
由真实和修正的二阶参数方程，移动参考的完整二阶 KL 式恰给出
\[
\boxed{
A R_{l,\xi\xi}+B_lR_{l,\xi}+C_l\mathcal D_l
=A\mathcal Q_l-A\tau_{l,\xi}^2\langle\delta_l,Z_l/g_l\rangle_{u_l}.
}                                                        \tag{5.16}
\]
特别地，右侧是明确的正平方与已知修正残差的配对，不含未定义余项。
推导为：把 \(Af_{\xi\xi}+Bf_\xi=CLf\) 及
\(Ag_{\xi\xi}+Bg_\xi=CLg+A\tau_\xi^2Z\)
代入移动 KL 二阶公式；\(\langle Z\rangle_u=0\) 使 \(f\) 可换成 \(\delta\)。

设 \(\varphi_l=\pi_l'/\pi_l\)，并定义
\[
K_l^{\rm par}=\xi_a^2 B_l/A+2/c,\qquad
\Lambda_l=\xi_a^2(\gamma_{2,l}\tau_{l,\xi}^2-\tau_{l,\xi\xi})
                         +2\tau_{l,\xi}/c,
\]
\[
M_l^{\rm mov}=\Lambda_l-2\varphi_l\xi_a\tau_{l,\xi},\qquad
N_l^{\rm mov}=K_l^{\rm par}-2\varphi_l\xi_a .
\]
将 (5.1)、(5.16) 与所有权重交叉项合并，得到
\[
\begin{aligned}
R_{l,aa}+2\varphi_lR_{l,a}
={}&\xi_a^2\mathcal Q_l+M_l^{\rm mov}\mathcal D_l
-N_l^{\rm mov}\langle F_l,\ell_l\rangle_{u_l}\\
&-\xi_a^2\tau_{l,\xi}^2\langle\delta_l,Z_l/g_l\rangle_{u_l}.
\end{aligned}                                             \tag{5.17}
\]
这是移动权重改变有效耗散系数的明确位置。

若所有有缺陷层满足 \(M_l^{\rm mov}>0\)，对偶完成平方给出
\[
\begin{aligned}
E_n''\ge\mathcal L_n''+\sum_l\pi_l''R_l
-\sum_{\{l:m\ge4\}}\pi_l\bigg[
\frac{(N_l^{\rm mov})^2J_l^2}{4M_l^{\rm mov}}
+\xi_a^2\tau_{l,\xi}^2
       |\langle\delta_l,Z_l/g_l\rangle_{u_l}|
\bigg].                                                  \end{aligned} \tag{5.18}
\]
最后的配对也可用
\(\langle\delta_l^2/g_l\rangle^{1/2}
 \langle Z_l^2/g_l\rangle^{1/2}\) 支付。

这个适用域不是所求熵比较的重述：它只检查已知计数 score、指定时钟及 Jacobi 系数。
在中点 \(M_l^{\rm mov}=2\tau_{l,\xi}/c>0\)，
(5.18) 正好还原 (5.3)。

甚至可以给出明确的邻域宽度。§5.4 的正 Stieltjes 商是严格 log-convex 的：
\(FF''-(F')^2>0\) 由正留数展开和 Cauchy–Schwarz 直接得出。
所以 \(\tau_{l,\xi\xi}<0\)，继而 \(\tau_{l,aa}<0\)，并有
\(\Lambda_l\ge2\tau_{l,\xi}/c\)。
令 \(\eta=\min(a,1-c-a)\)。计数 latent score 的每项绝对值至多 \(1/\eta\)，
故 \(|\varphi_l|\le n/\eta\)。
在
\[
\boxed{|a-a_*|\le\frac1{320n}}                            \tag{5.19}
\]
内，\(\eta\ge1/80\) 且 \(|\varphi_l\xi_a|\le1/(2c)\)，于是所有有缺陷层都满足
\(M_l^{\rm mov}\ge\tau_{l,\xi}/c>0\)。
因此 (5.18) 在这个明确、随 \(n\) 缩小的邻域上无条件成立。
它仍保留已知残差配对，未声称整个右侧为 \(o(n)\)。

若离开该邻域后某层 \(M_l^{\rm mov}\le0\)，不能完成这一步平方，
应保留恒等式或使用 (4.7)。时钟凹性只保证 \(\Lambda_l>0\)，
不保证扣除移动权重后的 \(M_l^{\rm mov}>0\)，也不保证 \(E_n''\) 全域有符号。

## 6. 合法反例与失败机制

### 6.1 n=8 确实激发度四：只用一个原子

令 \(n=8,k=l=4\)，\(S_{\rm even}=\{0,2,4,6\}\)。
同奇偶站点间 \(P_{ij}=0\)，故
\(P_{S_{\rm even}}=\frac12I\)、
\(r_4^{\max}(S_{\rm even})=70/16=35/8\)。

设 \(b_{ij}=1/28-|P_{ij}|^2\)，则行和为零，且
\[
v_{4,2}(S)=\frac{35}{3}\sum_{\{i,j\}\subset S}b_{ij}.       \tag{6.1}
\]
核对系数：均匀四层的二、三、四点概率分别为
\(3/14,1/14,1/70\)，所以 row-zero 配对和与 \(x_ix_j\) 的内积系数是
\(3/14-2/14+1/70=3/35\)。
Fourier DPP 与均匀律的二点差恰为 \(b_{ij}\)，证明 (6.1)。
故 \(v_{4,2}(S_{\rm even})=5/2\)，而
\[
\boxed{v_{4,4}(S_{\rm even})=35/8-1-5/2=7/8\ne0.}         \tag{6.2}
\]
这没有枚举八点完整配置。

本层
\[
Q_4=1+20\xi+90\xi^2+140\xi^3+70\xi^4,\quad
Q_2=1+6\xi+6\xi^2,
\]
\[
\theta_2=Q_2/Q_4,\quad\theta_4=1/Q_4,\quad
\psi_4=\theta_2^{10/7}.
\]
因此合法区间每一点都满足
\[
q_4(S_{\rm even})-\widehat q_4(S_{\rm even})
=\frac1{80}(\theta_4-\psi_4)<0.                           \tag{6.3}
\]
这是全律相等规则的反例，不单凭此断言熵二阶差。

### 6.2 正随机时钟混合修复失败

假设在上述层存在 \(T\ge0\) 的概率分布，使
\(f_4=\mathbb E[e^{TL_4}r_4^{\max}]\)。
两个非零模式要求
\[
\mathbb EX=\theta_2,\qquad
\mathbb EX^{10/7}=\theta_4,\quad X=e^{-\gamma_{2,4}T}.
\]
Jensen 却给
\(\mathbb EX^{10/7}\ge(\mathbb EX)^{10/7}=\psi_4>\theta_4\)，矛盾。
因此“通过正子从属／随机化单钟精确恢复真实律”在合法本题模型失败。

一个独立代数证书是：设 \(t=1/[\xi(1+\xi)]>0\)，则
\(\theta_2=t(t+6)/(t^2+20t+70)\)、
\(\theta_4=t^2/(t^2+20t+70)\)，且
\[
\begin{aligned}
(t+6)^{10}-t^4(t^2+20t+70)^3={}&
210t^8+9520t^7+173460t^6+1665552t^5\\
&+9454760t^4+33592320t^3+75582720t^2\\
&+100776960t+60466176>0.
\end{aligned}                                             \tag{6.4}
\]

### 6.3 两种全域曲率单侧规则都失败，但未定位中点

**定理 6.3。** 固定本题 \(c=19/20,n=8\)，存在
\(a_+,a_-\in(0,1/20)\)，使 \(E_8''(a_+)>0>E_8''(a_-)\)。

**第一步：端点 jets 合拢。** (3.11) 给出逐层解析
\(\delta_l=O(\xi^2)\)，真实及修正密度在 \(\xi=0\) 严格正。
所以 \(\epsilon_l=O(\xi^2)\)，并且这个陈述来自共同的解析 jets，
而不是对一个静态大 \(O\) 界微分。计数权重为多项式。
故 \(E_n\) 有到闭区间的 \(C^2\) 延拓，且
\[
E_n(0)=E_n(1-c)=E_n'(0)=E_n'(1-c)=0.                     \tag{6.5}
\]

**第二步：不能只用模式失配，必须证明熵差不恒为零。**
\(n=8\) 只有 \(l=4\) 有缺陷，并且精确计数权重为
\[
\pi_4(a)=c^4Q_4(\xi),\qquad
E_8(a)=c^4Q_4(\xi)\epsilon_4(\xi).                        \tag{6.6}
\]
为证明解析函数不恒为零，只在这一证明步骤把正的条件核
\(z=1+\xi^{-1}\) 延拓到全部 \(\xi>0\)。
这不是把非物理参数当作反例点。
正性及有限原子数保证 \(\epsilon_4\) 在 \((0,\infty)\) 实解析。
当 \(\xi\to\infty\)，
\[
\theta_2\sim(3/35)\xi^{-2},\quad
\theta_4\sim(1/70)\xi^{-4},\quad
\psi_4\sim(3/35)^{10/7}\xi^{-20/7}.
\]
利用 \(v_2\perp v_4\)、(6.2)，以及
\(D(u(1+h)\Vert u)=\frac12\|h\|_2^2+O(\|h\|_\infty^3)\)，得
\[
\epsilon_4(\xi)=
-\frac12(3/35)^{20/7}\|v_{4,4}\|_{u_4}^2\,\xi^{-40/7}
+o(\xi^{-40/7})<0                                       \tag{6.7}
\]
最终成立。这里两个 KL 的三次余项是 \(O(\xi^{-6})\)，
严格小于主项；已经支付非线性与模式交叉项。
故 \(\epsilon_4\) 不恒为零，实解析唯一性说明它不能在
物理开区间 \((0,\xi_*)\) 恒为零。由 (6.6)，\(E_8\) 在合法 \(a\) 域不恒为零。

**第三步：曲率积分。** (6.5) 给
\(\int_0^{1-c}E_8''(a)\,da=0\)。
若 \(E_8''\) 恒为零，则 \(E_8\) 为仿射且由端点为零，与第二步矛盾；
连续的非零函数积分为零，必同时取正值与负值。证毕。

因此
\[
[\forall n,a:\ E_n''(a)\ge0]\quad\text{和}\quad
[\forall n,a:\ E_n''(a)\le0]
\]
都被这个固定 Fourier 实例否定。此定理不提供 \(a_\pm\) 的数字，
也不判定 \(E_8''(a_*)\)。若需要坐标证书，按计算交接执行。
有限维反例不否定 \(E_n''\ge-o(n)\) 的渐近升级。

## 7. 熵梯度的高模式：剩余义务有可检查的生成机制

令 \(g(t)=e^{tL_l}r_l^{\max}\)，\(h(t)=\log g(t)\)。精确地
\[
h_t=L_lh+\mathcal N(h),\qquad
\mathcal N(h)(S)=\sum_TQ_{ST}
[e^{h(T)-h(S)}-1-(h(T)-h(S))]\ge0.                        \tag{7.1}
\]
若 \(\Pi_{U_l}\) 投影到未匹配偶数模式，则
\[
\Pi_{U_l}h(t)=e^{tL_l}\Pi_{U_l}h(0)+
\int_0^t e^{(t-s)L_l}\Pi_{U_l}\mathcal N(h(s))\,ds.         \tag{7.2}
\]
中层 \(l=k\) 的 Vandermonde 对数是常数加配对势。
循环距离势的行和为常数，故其非恒定部分纯度二，
\(\Pi_{U_k}\log r_k^{\max}=0\)。该层的熵梯度泄漏完全由 (7.2) 的非线性源生成。
其他层的初始高对数模式不得默认消失。
虽然 \(\mathcal N\ge0\)，其高模式投影没有预定符号。

为量化 (5.4)，令
\[
\zeta_{l,0}^2=\sum_{j\in U_l}e_{l,j}^2\|v_{l,j}\|_2^2,\qquad
\zeta_{l,1}^2=\sum_{j\in U_l}e_{l,j,\xi}^2\|v_{l,j}\|_2^2.
\]
则 Cauchy–Schwarz 给出明确但尚未渐近支付的界
\[
\begin{aligned}
|\mathcal L_n''(a_*)|\le\sum_l\big[
&(|\pi_l''|\zeta_{l,0}+2\pi_l\zeta_{l,1}/c)
                    \|\Pi_{U_l}\log g_l\|_2\\
&+(2\pi_l/c)\tau_{l,\xi}\zeta_{l,0}
                    \|\Pi_{U_l}(L_lg_l/g_l)\|_2\big].
\end{aligned}                                             \tag{7.3}
\]
(7.2) 与 (7.3) 说明升级具体欠什么，不把这个界宣布为 \(o(n)\)。

### 7.1 真熵梯度上的直接残差配对其实是次线性的

还可支付一个不同于 (0.2) 的部件。定义普通热熵生产
\[
\mathcal I_l(h)=-\langle L_lh,\log h\rangle_{u_l}\ge0.
\]
Schur 补比较已经证明相邻真原子比位于 \([z^{-1},z]\)，所以
\(|\log f_l(T)-\log f_l(S)|\le\log z\)。
以真条件律为平稳律的 Johnson Metropolis 链，总跳率不超过 \(1\)，
谱隙至少 \(1/(zm)\)。因此
\[
\operatorname{Var}_{q_l}(\log f_l)
 \le \frac{zm}{2}(\log z)^2.
\]
这一步用的是实际真原子的邻边比，不需要 corrected law 的原子比。
因为 \(\langle F_l\rangle_u=0\)，对数可先减去其真条件均值，
Cauchy–Schwarz 与 (5.8) 随即给出
\[
|\langle F_l,\log f_l\rangle_{u_l}|
\le \log z\sqrt{\frac{zm}{2}\langle F_l^2/f_l\rangle_{u_l}}.
                                                               \tag{7.4}
\]
故中点 \(\sum_l\pi_l|\langle F_l,\log f_l\rangle|
\le(\log z_*/2)\sqrt{z_*K_Wn}\)。这是 \(O(\sqrt n)\) 而非 \(O(n)\)。

另一方面，直接对层熵求 \(\xi\) 导数得到完整恒等式
\[
\epsilon_{l,\xi}
=-\tau_{l,\xi}[\mathcal I_l(f_l)-\mathcal I_l(g_l)]
+\langle F_l,\log f_l\rangle_{u_l}.
\]
所以另一个无条件中点比较是
\[
\boxed{
E_n''(a_*)\ge
\sum_l\pi_l''\epsilon_l
+\frac2c\sum_l\pi_l\tau_{l,\xi}
       [\mathcal I_l(f_l)-\mathcal I_l(g_l)]
-\frac{\log z_*}{c}\sqrt{z_*K_Wn}.
}                                                            \tag{7.5}
\]
有缺陷的 \(m\ge4\) 才需计入源；其余层全部为零。
(7.5) 明确支付了真熵梯度上的外力，并保留**两个耗散的差**与移动计数。
不能从 \(\theta_j<\psi_j\) 推出这个非线性耗散差为正。
这一版本与 (0.2) 是替代账本，不把它们的不利项重复相加，也不把
尚未受控的耗散差自动当成 \(o(n)\)。

## 8. 最终数学状态与对题目式 (1) 的确切作用

**PROVED。** 全模式参数方程与显式残差、正 Green 传递、奇数消去、
\(n=4,6\) 全律/全 jets 相等、\(n=8\) 非零度四、完整移动参考 C² 恒等式、
一般局部引理 (4.7)、无接近前提的中点桥接 (5.3)、
无原子最小值的源估计 (5.6)–(5.8)、统一 \(O(1)\) 源支付 (0.2)，
真熵梯度源的 \(O(\sqrt n)\) 支付 (7.4)–(7.5)，以及曲率两种符号的解析存在证明。

**DISPROVED。** “度二匹配使全律相等”、固定 \(n=8\) 的正随机单钟恢复、
以及全合法域的两个相反固定符号规则。
没有把模式不匹配单独当作熵 Hessian 反例。

**INCOMPLETE。** 目标升级精确缩为证明
\[
\mathcal L_n''(a_*)+\sum_l\pi_l''(a_*)R_l(a_*)\ge-o(n).
\]
这是“显式高模式与移动权重”的静态/线性响应问题，
不是已经支付的相对熵层内加速问题。
目前没有该估计，也没有中点全 \(n\) 符号结论。
粗常数 \(C_{\rm src}\) 不能替代前两项；不能把 \(E_n=o(n)\) 形式微分。
本文没有证明真实熵凹性，也没有反驳它。
循环到 Toeplitz/熵率的传递不在本任务内。

**最小验证。** 随附程序只对 \(n=4\) 的 16 个完整原子做精确有理 jets 检查，
并检查 \(n=8\) 的单原子/低次多项式代数。
没有重跑旧六点证书，没有参数扫描，没有哈希校验。
更大配置数、参数坐标认证和尺度优化见独立计算交接。

## 参考文献与来源范围

[R0] 本任务文件 `research_prompts/pro_tasks/TASK_05_TRUE_CORRECTED_BRIDGE.md`；
公共已知恒等式参见同目录 `COMMON_STARTER.md`。
S13 的 corrected-clock 结论只作背景，没有作为本桥已成立的输入。

[R1] Jan Giesselmann, Charalambos Makridakis, Tristan Pryer,
*A posteriori analysis of discontinuous Galerkin schemes for systems of hyperbolic
conservation laws*, arXiv:1405.7616。
使用其相对熵＋演化残差的机制及适用条件，不把其 PDE 定理直接套作参数 Hessian 界。

[R2] Yuval Filmus,
*An orthogonal basis for functions over a slice of the Boolean hypercube*,
arXiv:1406.0142。
用于 slice 谐波空间及 Johnson 谱基的标准事实；本题乘子与残差在正文推导。

[R3] NIST Digital Library of Mathematical Functions，
§18.2(vi)（正交多项式零点与交错），§18.3（Jacobi 正交权重），
§18.5、§18.8（Jacobi 表示与微分方程）。
正文也给出所需系数递推；没有依赖数值查表。

[R4] Nima Anari, Kuikui Liu, Shayan Oveis Gharan, Cynthia Vinzant,
*Log-Concave Polynomials II: High-Dimensional Walks and an FPRAS for Counting Bases
of a Matroid*, arXiv:1811.01816v3，Theorem 1.1 与 §1.3；
后发表于 *Annals of Mathematics* 199 (2024), 259–299。
使用齐次强对数凹 down-up 谱隙 \(1/m\)；逐边比较、对偶图能量和
本题统一源常数不是该外部定理的现成结论。
