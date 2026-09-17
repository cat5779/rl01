> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。审查入口见对应 results/SAxx/REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# 公共数学起点与范围

这是任务准备材料，不是全局凹性证明。下列有限概率恒等式可直接使用；只重新推导它们不算新的研究成果。

## 1. 两种不能混同的核

固定 `0<rho<1`，真正的 sine Toeplitz 压缩为

\[
(Q_n)_{ii}=\rho,\qquad (Q_n)_{ij}=\frac{\sin(\pi\rho(i-j))}{\pi(i-j)}\quad(i\ne j).
\]

它是正压缩，通常不是有限投影。另一个对象是连续频率的循环投影
`P_(n,r)=UU*`，`U_(j,k)=n^(-1/2)exp(2 pi i j k/n)`，`0<=j<n, 0<=k<r`。
后者是有限 rank-r 投影；不要无证明交换二者。

对任一固定正压缩 Q，`K_a=aI+cQ`，`0<c<1, 0<a<1-c`。
实际输出可由 `X~DPP(Q)` 经独立信道 `P(Y_i=1|X)=a+cX_i` 产生。
独立的是给定 X 的信道噪声，物理输出 Y 通常不独立。

完整原子、熵与二阶导数为

\[
p_a(S)=(-1)^{n-|S|}\det(K_a-\operatorname{diag}(1_{S^c})),\quad
H_n=-\sum_Sp_a(S)\log p_a(S),
\]
\[
H_n''=-\sum_Sp_a''(S)\log p_a(S)-\sum_S(p_a'(S))^2/p_a(S).
\]

严格信道内部原子全部为正。自然对数；所有 a 导数固定 c 和输入核。
熵率全局目标是 `lim H_n/n` 对 a 凹。通用 `c<=37/40`、S6 的极窄条带和 S4 极端密度区域是已有输入，不能重复算推进。

## 2. 真正移动计数的精确运输

设 `pi_m=P(|Y|=m)`、`q_(m,a)=Law(Y||Y|=m)`、`u_m=1/binom(n,m)`，
`D_m=D(q_(m,a)||u_m)`，`mathscr D=sum_m pi_m D_m`。则

\[
H_n=\Phi_n-\mathscr D,\qquad
\Phi_n=H(\pi)+\sum_m\pi_m\log\binom nm.
\]

Q 的特征值为 `lambda_i`。独立 Bernoulli `Z_i` 的成功率取 `b_i=a+c lambda_i`，则 `M=sum_i Z_i` 与真实输出计数同分布：生成函数为 `det(I+(z-1)K_a)`。这只表示计数，绝不把 Y 改成独立位。

对任意 C² 数组 `F_m(a)`，定义 `Delta F_m=F_(m+1)-F_m`；`M_-i`、`M_-ij` 为删掉指定位的 Bernoulli 和。精确地

\[
\frac{d^2}{da^2}\mathbb EF_M
=\mathbb EF_M''+2\sum_i\mathbb E\Delta F'_{M_{-i}}
+\sum_{i\ne j}\mathbb E\Delta^2F_{M_{-ij}}.\tag{CT}
\]

最后是有序和。证明：固定其余位，一次对 b_i 求导得到 `Delta F`；利用 `b_i'=1,b_i''=0` 再总微分即可。所有和有限，包含层内、移动权重与交叉项。

也有

\[
\sum_m\pi_m''F_m=\sum_{m=0}^{n-2}B_m\Delta^2F_m,\qquad
B_m=\sum_{i\ne j}\Pr(M_{-ij}=m)\ge0,
\quad\sum_m B_m=n(n-1).\tag{DF}
\]

因此一般 `Delta²F=O(1)` 只给 O(n²)，不是所需的 O(n)。需要真的平滑/抵消估计。对非零空间 KL，`D_0=D_n=0,D_m>=0` 还说明全域 `Delta²D_m>=0` 不可能。

## 3. 混合 score 与移动参考

对正联合律 `r_a(l,x)=pi_a(l)q_a(x|l)`，令 `t=partial_a log r`、`beta=partial_a t`；边缘 `p_a(x)=sum_l r_a(l,x)`，`s=partial_a log p`。则

\[
s=E[t|x],\quad p''/p=E[\beta+t^2|x],\quad
\partial_as=E[\beta|x]+\operatorname{Var}(t|x),
\]
\[
H''=-E[(\beta+t^2)\log p]-E[t^2]+E\operatorname{Var}(t|x).
\]

令正参考概率 `v_a` 的 score 为 `u=partial_a log v_a`，则

\[
(D(p_a\Vert v_a))''=E[(\beta+t^2)\log(p/v)]
+E[s^2]-2E[su]-E[\partial_a u].
\]

这是恒等式，没有自动有利的符号。参考移动时最后两项不能删。

## 4. 观察揭示的补偿起点

对嵌套输出 sigma-field（不揭示目标点 i），`u_t=P(Y_i=1|F_t)` 是 martingale。
若 `f(u)=1/[u(1-u)]`，则

\[
Ef(u_T)-Ef(u_0)=\sum_t E B_f(u_t,u_{t-1}),
\quad B_f(x,y)=(x-y)^2\left[\frac1{xy^2}+\frac1{(1-x)(1-y)^2}\right]\ge16(x-y)^2.
\]

四原子条件表 `P_t` 同样满足塔性质。对任务02定义的 g，令 `B_g(P,Q)=g(P)-g(Q)-grad g(Q) dot (P-Q)`，则
`Eg(P_T)-Eg(P_0)=sum_t E B_g(P_t,P_(t-1))`，但 `B_g` 可以有符号。
不同目标的揭示过程跳过不同站点，不可把其 sigma-field 默认相同；只能平均条件概率表，不能默认线性平均 DPP 核。

## 5. 已核对的范围边界

- S7：全 Shannon Hessian 定位、空间尾与观察误差已支付；近场总符号未定。
- S9：中心层与补层存在相反的 order-R 项；已证主阶抵消不决定剩余总符号。
- S13：`C_n` 正下界属于指定 corrected law；`W_n` 和真实律比较另欠。
- S4：完整信息支付上界给了极端密度区域；普通密度不足。
- 小维度或固定 R 的严格证书只证明自身作用域；不是成长体积或全参数结论。

源材料的作者历史状态字样不覆盖独立审查的适用范围。此包没有做外部新颖性认证。
