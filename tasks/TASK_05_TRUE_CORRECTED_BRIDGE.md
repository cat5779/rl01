# 独立任务05：真实输出与修正层律的二阶桥接

本任务完全独立于其它四题。你审查并创造**真实律与指定修正律之间的导数比较机制**；不需要先证明修正律凹性，也不需要假定桥一定成立。合法地推翻一个自然桥接规则也有价值。

## 两套完全固定的律

固定 `c=19/20,n=2k>=4,a_*=(1-c)/2=1/40`；a 在 `(0,1-c)` 内。
循环连续频率投影 `P=UU*`，`U_(j,r)=n^(-1/2)exp(2 pi i j r/n)`，`0<=j<n,0<=r<k`。
输入 k 元集 A 的概率 `nu(A)=det P_A`。真实输出为

\[
Y_a\sim\operatorname{DPP}(aI+cP),\quad
p_a(S)=(-1)^{n-|S|}\det(aI+cP-\operatorname{diag}(1_{S^c})).
\]

也可由给定 A 后独立信道 `P(Y_i=1|A)=a+c1_(i in A)` 构造。
`pi_l=P(|Y|=l)` 满足
`sum_l pi_l t^l=[1-a-c+(a+c)t]^k[1-a+at]^k`；真实层律 `q_l(S)=p_a(S)/pi_l`，`|S|=l`；`u_l(S)=1/binom(n,l)`。

修正模型如下：`T_l^max(S|A)` 在 l<=k 时均匀取 A 的 l 子集，在 l>=k 时均匀取包含 A 的 l 子集。
`r_l^max(S)=sum_A nu(A)T_l^max(S|A)/u_l(S)`。

对 `1<=l<=n-1` 定义
\[
(L_lf)(S)=\frac1{l(n-l)}\sum_{i\in S,j\notin S}[f(S-i+j)-f(S)].
\]

对 `2<=l<=n-2`，`m=min(l,n-l)`，超范围二项式系数取0，

\[
z=\frac{(a+c)(1-a)}{a(1-a-c)},\quad
Z_{n,m}(z)=\sum_j\binom kj\binom k{m-j}z^j,\quad
\alpha_{n,m}=m(m-1)/[k(k-1)],
\]
\[
\theta_{n,l}(z)=\frac{(z-1)^2\sum_j\binom{k-2}j\binom{k-2}{m-2-j}z^j}
{\alpha_{n,m}Z_{n,m}(z)},\quad
\gamma_{2,l}=2(n-1)/[l(n-l)],\quad
\widehat\tau_l=-\log\theta_{n,l}/\gamma_{2,l},
\]
\[
\widehat q_l(S)=u_l(S)[e^{\widehat\tau_l L_l}r_l^{max}](https://github.com/randomcat4/dpp-stationary-entropy/blob/2966743a11041ec8c2adef07ff6cb1f90b7d25da/research_prompts/pro_tasks/S).
\]

已知 `0<theta<1`；在 l=0,1,n-1,n 取 `qhat_l=u_l`。该 corrected law 正且归一，并匹配一个 degree-two pair 势均值；**没有已证全律相等或二阶熵接近**。

## 你要控制的精确缺陷

自然对数，定义

\[
D_l=D(q_l\Vert u_l),\quad\widehat D_l=D(\widehat q_l\Vert u_l),\quad
\epsilon_l=D_l-\widehat D_l,\quad E_n(a)=\sum_l\pi_l(a)\epsilon_l(a).
\]

令 `Phi_n=H(pi)+sum_l pi_l log binom(n,l)`；真实与修正完整熵分别为
`H_n=Phi_n-sum pi_l D_l` 和 `Hhat_n=Phi_n-sum pi_l Dhat_l`。
因此

\[
H_n''-\widehat H_n''=-E_n'',\quad
E_n''=\sum_l[\pi_l''\epsilon_l+2\pi_l'\epsilon_l'+\pi_l\epsilon_l''].\tag{1}
\]

这个式子是输入，不算研究成果。每层静态均匀参考下，任意正归一律 r 有

\[
(D(r_a\Vert u_l))''=\sum_S r_a''\log(r_a/u_l)+\sum_S(r_a')^2/r_a.
\]

真实 conditional jets 由 `p=pi q` 得
`q'=(p'-pi' q)/pi`，`q''=(p''-pi''q-2pi'q')/pi`。
修正 jets 包含 `tau' L`、`tau'' L+(tau')²L²`；中点 tau'=0，但不要因此删式(1)的权重响应。所有数值比较要用完整配置，不能只比较 count 或匹配的势。

## 创造性任务与允许出口

选择一个明确的桥接候选，研究其真假及所需最小结构。可以从以下一个入口开始：

1. 找出真实条件演化相对单钟修正的首个非零、实际被初值激发的未匹配模式；推导其对式(1)的可检查影响。
2. 证明一个有用但比“|E_n''|=o(n)”严格更弱的局部/单侧比较引理。
3. 用合法有限 Fourier 实例否定一个明确的全 n 曲率单侧规则，再设计仅匹配指定模式、误差完全显式的修正。

若能得到 `E_n''>=-epsilon_n n`、`epsilon_n->0`，它可用于将足够强的修正熵上界转移给真实熵；这是升级目标，**不是最低交付门槛**。有限 E'' 非零只否定精确相等，不自动否定 o(n) 渐近。

一个常见陷阱：总速率1 Johnson 层生成元的 j 次谐波特征值为
`gamma_(j,l)=j(n-j+1)/[l(n-l)]`，其中 `1<=l<=n-1,0<=j<=min(l,n-l)`。匹配 degree-two 只固定 exp(-gamma_2 tau)=theta_2；若要识别全律，真实的其它激发模式必须同样满足 `theta_j=theta_2^(gamma_j/gamma_2)`。有模式失配说明律不相等，但**不能直接据此断言 KL 二阶差的符号或尺度**；还要支付熵的非线性与其它模式抵消。

## 最小检验与真实性要求

从 n=4、6 中一个有非零待测模式的规模开始；若模式因对称性消失，再升 n=8，并解释原因。不要求一次枚举所有规模。
比较完整原子微分与层式(1)：全局检查 `sum_S p=1,sum_S p'=sum_S p''=0`；每个 l 层检查 `sum_(|S|=l)q_l=1,sum q_l'=sum q_l''=0`，对 qhat 同样检查。原子 p 在某一层之和是 pi_l，不能误当1。浮点扫描只是找例子；重要符号反例用精确式或控制误差的区间。

不能把值层面 `E_n=o(n)` 直接微分。若改用随 a 移动的参考 v，必须保留

\[
(D(p\Vert v))''=\sum p''\log(p/v)+\sum(p')^2/p
-2\sum p'v'/v-\sum p[v''/v-(v'/v)^2].
\]

例如 `p=(1/2,1/2),v_a=(1/2+a,1/2-a)` 在0有 KL二阶导数4，冻结参考会错误得到0。

交付 `PROVED / DISPROVED / INCOMPLETE`、精确候选和量词、新的完整推导/反例、对式(1)的确切结论，以及剩余模式/尺度义务。已闭合且严格较弱的结构引理也可独立完成；若没有新结果，诚实说明断点，不把“未来需要研究”包装成桥已建成。

本题只到真实**循环**输出与 corrected law 的比较。循环到 Toeplitz/熵率的传递另列；方法反例不意味着真实熵凹性为假。不设固定时长、候选配额或失败次数；不运行哈希、不强制 PR/ZIP。工具故障与数学结果分别报告，无工具也完成正文。
可选背景附件：`../results/S13/PROOF.md`、`S13_TERM_BALANCE.md`、`S13_AUDIT.md`。
