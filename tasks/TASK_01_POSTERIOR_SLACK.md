# 独立任务01：S4 普通密度的真实后验信息支付

你只研究下面一个有边界的创造性问题：**现有已完成信息上界在普通密度浪费了什么可严格利用的余量？** 不需要等待其它任务，不需要解决全局熵凹性。

## 真实输入、信道与全部量

默认 `rho=1/2,c=19/20,a_*=1/40`。可选择实际 n 维 sine Toeplitz 压缩
`Q_ii=1/2,Q_ij=sin(pi(i-j)/2)/(pi(i-j))`，或偶数 n 的连续频率 rank-n/2 循环投影
`P=UU*,U_(j,r)=n^(-1/2)exp(2pi i j r/n),0<=r<n/2`；开头声明选择哪种，不能把二者等同。用 Q 统称你选择的输入正压缩。

`X~DPP(Q)`，条件独立信道 `P(Y_i=1|X)=a+cX_i`，`0<a<1-c`。
记 `g_x(1)=a+cx,g_x(0)=1-a-cx`，`f_y(x)=prod_i g_(x_i)(y_i)`；
`p_y=E f_y(X)`，`nu_y=Law(X|Y=y)`，`C_y=Cov(X|Y=y)`，`R^y` 为这个完整后验的 DPP 核。
于是 `C_ii=R_ii(1-R_ii),C_ij=-|R_ij|²`。
输出完整原子也等于 `(-1)^(n-|y|)det(aI+cQ-diag(1-y))`。
自然对数，所有 a 导数固定 c,Q。

令 `q_i=Q_ii`、`tau_1=a(a+c),tau_0=(1-a)(1-a-c),e_b=c/tau_b`，

\[
\mathcal D=\sum_i\left[\frac{1-q_i}{a(1-a)}+\frac{q_i}{(a+c)(1-a-c)}\right],
\quad F_{marg}=\sum_i\frac1{(a+cq_i)(1-a-cq_i)},
\]
\[
\Psi=E_Y\sum_i e_{Y_i}^2(C_Y)_{ii},\quad
\mathcal E=E_Y e_Y^T C_Y e_Y,\quad
\mathcal S=E_Y\sum_{i<j}e_{Y_i}e_{Y_j}|R^Y_{ij}|^2.
\]

精确地 `mathcal E=Psi-2mathcal S>=0`。
完整 channel score `sigma_y(x)=sum_i(2y_i-1)/g_(x_i)(y_i)`，
真实输出 Fisher `F=sum_y(p_y')²/p_y=mathcal D-mathcal E`。
令 `A=-sum_y p_y''log p_y`，`I=I(X;Y)`，则

\[
I''=A+\mathcal E,\qquad H(Y)''=-\mathcal D+I''.
\]

这些量都对真实完整律取期望，不把后验替换成产品律。

## 已审核输入：你不必重证

令 `theta=log((a+c)(1-a)/(a(1-a-c)))`，

\[
\kappa=\min\{1/\sqrt{1-c^4},\ \theta/(1-e^{-\theta}),\ 2\text{（仅当 }c^2\le23/25\text{）}\}.
\]

已知

\[
0\le I''\le\kappa\Psi-(\kappa-1)\mathcal E,
\qquad \Psi\le\mathcal D-F_{marg}.
\tag{1}
\]

它足以证明一些极端密度区域，普通密度尚不足。`c=19/20,a=1/40` 时可取 kappa=2。

给定 pair 外部实际输出，四原子条件表为 `(A00,A10,A01,A11)`，定义

\[
\Lambda=\log\frac{A10A01}{A00A11},\quad
\Gamma=(A10A01-A00A11)\sum_{(u,v)\in\{0,1\}^2}1/A_{uv}.
\]

有 `A=2sum_(i<j)E Lambda_(ij)`，
`Gamma=E[e_(Y_i)e_(Y_j)|R^Y_ij|²|Y_-ij]`，
`Lambda<=kappa Gamma`。因此精确未使用余量为

\[
\mathcal R_\kappa=2\sum_{i<j}E(\kappa\Gamma_{ij}-\Lambda_{ij})\ge0,
\quad I''=\kappa\Psi-(\kappa-1)\mathcal E-\mathcal R_\kappa.
\tag{2}
\]

仅把这个差命名、计算一个小例子或重新写式(2)，不算新支付。

## 你的研究任务

利用真实 Fourier/sine 后验的空间兼容性，构造一个**不引用未知目标 Hessian 或原差本身**的显式下界 `L(Q,a,c)`，证明
`R_kappa>=L`，或者证明一个直接严格改进式(1)的后验平均不等式。
你可从重叠 pair 不能同时达到标量最坏值、后验谱/协方差约束、某个有限空间图案的强制余量入手。先选一种，至多一个备选。

优先在中点做有限 n 的清晰命题；若完整成长尺度暂时不可得，可证明一个有明确适用域的局部几何引理，并说明它怎样进入式(2)。需要的新假设先写清；改候选必须保留被反驳的版本。

无需强求 L 已大到让 `H''<=0`；普通密度真实模型上的可核查结构性严格改进就有价值。固定小 n 的严格结果只标为有限证书，不冒充维数一致支付。但纯常数拟合、把 `kappa Gamma-Lambda` 自身换名作为 L、或引用“存在某非负补偿项”都不成立。

## 判伪起点

- 在循环固定计数投影中点，e_0=e_1 且 |X| 固定，所以 `mathcal E=0`，归一后验的一阶共同位移 tangent 消失；`Psi` 一般仍正。不能以 `Psi<=C mathcal E` 或 tangent-only 能量闭合。
- 逐 pair 的 `Lambda<=Gamma` 为假。合法二维核 `q=1/100,r=99/100,|z|²=1/250` 有四原子 `(59,41,9841,59)/10000`，`Lambda>4,Gamma<3`。这是一般合法 DPP 的反例，不自动是默认 sine 家族实例。
- 实际六点 sine 在默认参数下也有 `E(Lambda-Gamma)_(1,6)>0.00037`，完整 H''仍在(-50,-49)。因此即使只在目标家族也不能逐 pair 强制非正。
- 两位总熵 `H_2''<=-8` 已是仓库接受的旧结果，不算新创造性成果。若用它，要新增重叠兼容性或不重复消耗的支付机制。

新的候选先在最小合法 n=3/4/6 中与定义核对（循环半密度选项只能取偶数 n；n=3 可用于 Toeplitz 选项）；可以用完整后验枚举或 Schur 完成公式。少量浮点例子只是诊断；关键反例给显式参数、合法性和误差控制。

## 交付

依次给 `PROVED / DISPROVED / INCOMPLETE`，精确新命题，完整证明或满足全部前提的反例，式(1)/(2)改善的具体位置，以及与全局目标之间仍欠的尺度/参数传递。
如果证明未完成，保留已闭合的严格较弱子引理和精确断点，不把“未知但看来为真”算支付。

本题不要求统一 S7/S9/S13，不要求思考固定分钟、制造失败或打包发布；不执行任何哈希检查。工具不可用时交正文和可复制公式/代码，单列工具限制。可选背景：`../results/S4/PROOF.md`、`S4_AUDIT.md`；附件不是起跑条件。
