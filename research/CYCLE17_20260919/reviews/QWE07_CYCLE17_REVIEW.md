# QWE07 Cycle17 独立数学与证书审查

审查日期：2026-09-19

冻结作者源：DPP PR129，commit `6a1eb3ae06bcf5a220cbb55b74ca7aef9ae3f0e4`。

审查对象是 71 个完整源文件，包括 `RESULT.md`、`SUBMISSION_README.md`、全部新证书源码/输入/日志，以及已接受的 S63、SA02 来源。作者的 `PROVED` 标签未被当作证据；本审查重新核对了承重证明，并在隔离目录重新编译和执行了新证书。

## 1. 总裁决

| 层级 | 独立裁决 |
|---|---|
| 冻结有限体积定理 | **VERIFIED_SCOPED** |
| 熵率弦差推论 | **VERIFIED_SCOPED** |
| 正场后验与 nested-subspace transport lemma | **VERIFIED** |
| 密度方向实际律解析主控与二维插值余项 | **VERIFIED** |
| 全局/guard/55 节点/精确 Bernstein 证书 | **VERIFIED_INDEPENDENT_REPLAY** |
| \(\rho=.34\) 与 \(\rho=.5\) 的原见证支付失败 | **VERIFIED_WITNESS_SPECIFIC_OBSTRUCTION** |
| 半密度或全密度凹性 | **NOT PROVED** |

接受的精确结论为：令

\[
c=\frac{19}{20},\qquad
\rho\in\left[\frac13,\frac{1009}{3000}\right],\qquad
a\in\left[\frac{21}{1000},\frac3{125}\right].
\]

对真实无限 sine projection 的有限 Toeplitz 压缩

\[
K_{\rho,a,n}=aI+\frac{19}{20}Q_{\rho,n},
\]

其完整空间配置 Shannon 熵满足

\[
\boxed{H_{\rho,n}''(a)\le-\frac n{25}+399\quad(n\ge22).}
\]

对每个冻结密度，平稳熵率存在，且

\[
\boxed{
\operatorname{Gap}_\lambda h_\rho
\ge \frac1{50}\lambda(1-\lambda)(a_1-a_0)^2
}
\]

对所有 \(a_0,a_1\) 属于上述闭区间、\(\lambda\in[0,1]\) 成立。在 \(p=20a\) 坐标中系数为 \(1/20000\)。密度带宽严格等于 \(.003\)，上端为 \(.336333\ldots\)，不是半密度。

有限体积右侧只在 \(n\ge9976\) 时严格为负；定理对 \(n\ge22\) 给出的是带常数边界项的线性上界。作者正文已经正确说明这一点。

## 2. 依赖边界

本审查复用了 RL01 PR47 已独立接受的 S63 机制：真实通道表示、普通密度 Fisher 预算、pair 比率包络、PSD 对角预算、得分鞅 Jensen、固定测试函数在移动实际律下的变分支付，以及有限见证到熵率弦差的接口。没有重复审计这些无变化部分。

QWE07 必须新支付的部分是密度输运：

1. \(\rho\) 变化会改变所有 sine 非对角元，不能使用 \(a\)-方向的多仿射演化代替；
2. 无限先验是投影，有限 Toeplitz 压缩不是投影；
3. guard 后验包络必须同时覆盖全部外部观察、全部 256 个 guard 词和整个二维参数矩形；
4. 22-site 见证期望必须在每个参数处使用移动实际律；
5. 从 55 个节点到闭矩形必须支付密度余项、偏置余项、节点外包误差和负插值权重。

这些新增义务均在本稿内得到证明并由新证书实现。

## 3. 实际律与有限压缩

令 \(X\) 是无限 sine projection DPP，并在给定 \(X\) 后独立取

\[
\Pr(Y_i=1\mid X)=a+cX_i.
\]

对任意有限 \(S\)，

\[
E\prod_{i\in S}Y_i
=\sum_{T\subseteq S}a^{|S|-|T|}c^{|T|}\det Q_{\rho,T}
=\det(aI+cQ_\rho)_S.
\]

因此每个有限输出边缘恰是 \(\operatorname{DPP}(aI+cQ_{\rho,S})\)。这是实际 Toeplitz 压缩的精确潜变量表示，没有把有限压缩设成投影，也没有使用循环替代。

完整数据共同平移得分在给定 \(X\) 后是独立中心化项之和。观察得分是其关于输出的条件期望，所以

\[
J_V\le |V|d_{\rho,c}(a),\qquad
d_{\rho,c}(a)=
\frac{1-\rho}{a(1-a)}+
\frac{\rho}{(a+c)(1-a-c)}.
\]

普通密度项完整保留；这里没有半密度抵消。

## 4. 正场后验输运

### 4.1 后验投影公式

有限输出观察给潜在配置乘以正场 \(\prod_iD_i^{X_i}\)，其中观察 1、观察 0、未观察分别给 \(d_+,d_-,1\)。在 \(\mathcal H_\rho=\operatorname{Ran}Q_\rho\) 上，

\[
P_D(\rho)=D^{1/2}Q_\rho
\bigl(Q_\rho DQ_\rho|_{\mathcal H_\rho}\bigr)^{-1}
Q_\rho D^{1/2}
\]

是到闭子空间 \(D^{1/2}\mathcal H_\rho\) 的正交投影。因为 \(D\) 有统一正下界，乘法算子可逆且保持闭性。

当 \(\rho\le\sigma\) 时，Fourier 支撑嵌套给

\[
\mathcal H_\rho\subseteq\mathcal H_\sigma,qquad
D^{1/2}\mathcal H_\rho\subseteq D^{1/2}\mathcal H_\sigma,
\]

故

\[
P_D(\rho)\preceq P_D(\sigma).
\]

这个证明没有对无限投影作小范数微扰；事实上不同密度无限投影的算子范数距离为 1。

### 4.2 guard 端点规则

对未观察目标对 \(T\)、有限 guard \(O\) 及 \(E=T\cup O\)，若 \(E\) 外的比较场固定为 \(d>0\)，目标压缩为

\[
\mathcal B_d(\rho,a,z)=
\left[Q_{\rho,E}{dI+(D_E-dI)Q_{\rho,E}\}^{-1}\right]_{T,T}.
\]

这是由坐标限制算子和 push-through inverse identity 得到的有限公式，不要求 \(Q_{\rho,E}\) 是投影或可逆。相应正算子有严格正下界，逆存在。

实际有限观察场在 \(E\) 外逐点落在 \([d_-,d_+]\) 内，未观察位置的场 1 也在此区间。Gram 算子序与逆序给

\[
\mathcal B_{d_+}\preceq B_T\preceq\mathcal B_{d_-}.
\]

又因 \(d_+(a),d_-(a)\) 都随 \(a\) 下降，结合密度的 nested-subspace 序，得到完整矩形端点包络

\[
\mathcal B_{d_+(a_-)}(\rho_-,a_-,z)
\preceq B_T(\rho,a)
\preceq
\mathcal B_{d_-(a_+)}(\rho_+,a_+,z).
\]

比较用的无限常场只定义算子上下界，不被误称为具有正概率的无限观察词。该限定是合法且必要的。

## 5. pair 包络、PSD 分配与移动实际律

全局四原子比率包络沿用 S63 的标量优化，但一站点端点 \(L,U\) 已由新密度矩形重新认证。`density_global.cpp` 覆盖 60 个 bias cells，程序确实只略去已由解析 \(\alpha\le1<C_0\) 支付的 \(R>r^2\) 区域。

局部 guard 程序在目标对 \(\{10,11\}\) 周围使用八个 guard 位，位序与正文一致。实现逐项对应证明：

- `guardmat` 使用真实 endpoint sine 压缩与 \(d_\pm\) 场，不使用有限投影恒等式；
- 区间逆把有限矩阵公式向外包围；
- 对称中点误差采用 \(\max(e_0,e_1)+e_w\)，正是 \(2\times2\) 对称误差矩阵的最大行和上界；
- Loewner order interval 的非对角范围和两个必要 PSD 不等式均被检查；
- 每个实际输出原子用 \(\min(a,1-a-c)^2\) 给严格正下界；
- 未闭合盒只会继续细分或使任务失败，不能被成功日志跳过。

对完整有限输出律，S63 的矩阵恒等式给

\[
H_V''\le(C_0-1)J_V-
\sum_eE[Z_{W_e,e}^{\mathsf T}B_eZ_{W_e,e}].
\]

每个站点最多属于两个选中相邻对，每条边只分配端点对角预算 \(C_0/2\)，所以没有重复收费。guard 词不含目标位，\(B_e\) 对窗口可测且 PSD，条件 Jensen 合法。

固定测试函数来自 \((\rho_*,a_*)=(1/3,1/40)\)，但每个参数处的期望始终是

\[
P(\rho,a)=E_{\rho,a}V(a,Y),
\]

其中权重是该参数的完整实际分布。参考分布只选择测试函数，不替代求期望的分布。`density_witness.cpp` 的递归实际枚举完整词并以当前 sine 核的条件 DPP 概率更新；没有冻结 normalizer。

## 6. 密度解析主控

### 6.1 masked inverse 的统一谱隙

若 \(aI\preceq K\preceq(1-b)I\)，对任意输出词，masked matrix

\[
M_y=K-\operatorname{diag}(1-y)
\]

在区间 \((-b,a)\) 无谱。按 occupied/vacant 分块，occupied 块减去该区间内的 \(\lambda\) 为正，vacant 块为负，其 Schur 补严格负。这给

\[
\|M_y^{-1}\|_{\rm op}\le\frac1{\min(a,b)}.
\]

在当前闭矩形中统一取 \(\min(a,1-a-c)\ge21/1000\)。

### 6.2 完整概率向量的复解析界

对复密度 \(z\)，中心化坐标后

\[
Q_z'=\tfrac12(u_zv_z^{\mathsf T}+v_zu_z^{\mathsf T}),
\]

从而

\[
\|Q_{r+w,m}-Q_{r,m}\|_1
\le m|w|\frac{\sinh(\pi(m-1)|w|)}{\pi(m-1)|w|}.
\]

每个 masked determinant 满足精确比值

\[
p_{r+w}(y)=p_r(y)
\det\{I+G_r(y)c(Q_{r+w,m}-Q_{r,m})\}.
\]

用 \(|\det(I+A)|\le e^{\|A\|_1}\)、统一 masked inverse 界和实际归一化权重 \(p_r(y)\) 求和，得到的是完整概率向量的 \(\ell^1\) 主控，而不是典型词或 inclusion moments 的近似。

对 \(m=22,R=.01\)，精确常数检查给指数小于 11、\(e^{11}<60000\)。结合 \(\|V\|_\infty\le1540\)，Cauchy 公式合法控制 \(P\) 的第 11 阶密度导数。这里求导的是全部移动 sine 实际律，没有借用对角平移导数。

## 7. 闭矩形插值与精确判号

作者使用 11 个密度节点和 5 个 bias 节点。独立检查确认：

1. 密度方向 11 阶余项由上述 Cauchy 界支付；
2. bias 方向利用对角多仿射算子 \(D=\sum_iD_i\)，其 \(\ell^1\) 范数至多 44；因 \(V\) 关于 \(a\) 仿射，第五阶导数界中的两项及系数 5 正确；
3. \(\Lambda_{10}\le32\)、\(\Lambda_4\le3\) 由各网格小区上的 Lagrange 基函数固定符号和精确 Bernstein 细分证明；
4. 所有负 Lagrange 权重均通过 Lebesgue 常数支付；不能把节点下端点直接插值，本稿没有犯此错误；
5. 总误差精确为

\[
\frac{3647592747897}{3906250000000000}
=0.000933783743461632<\frac1{1000}.
\]

将 nodal midpoint 插值多项式代入支付式，乘正分母 \(\beta_0\beta_1\) 后得到 bidegree \((10,8)\) 的有理多项式。重新执行精确算术得到：

- 99 个支付 Bernstein 系数全部正，最小值
  \(17107889404629337/600000000000000000000>0\)；
- 最小的 \(10^{-9}\) 向下整数界为 28513；
- 55 个 \(P\) 上界 Bernstein 系数全部正，最小值
  \(125473547/200000000\)。

故闭矩形上严格有

\[
P(\rho,a)-(C_0(a)-1)d_{\rho,c}(a)\ge\frac1{25},
\qquad P(\rho,a)\le19.
\]

这是真正的连续矩形证书，不是 55 点网格结论。

## 8. 从有限窗口到所有体积和熵率

长度 \(n\) 中有 \(n-21\) 个完整 22-site 平移窗口，中央边互不重复。平稳性使每个窗口的实际支付同为 \(P(\rho,a)\)。因此

\[
\begin{aligned}
H_{\rho,n}''(a)
&\le n(C_0-1)d-(n-21)P\\
&=-n\{P-(C_0-1)d\}+21P\\
&\le-\frac n{25}+399.
\end{aligned}
\]

所有未选 pair 和长程 pair 均由全局包络支付；有限压缩 leakage 没有被丢弃。边界常数正是 \(21\cdot19=399\)。

平稳有限字母过程的块熵次可加，所以 \(H_n/n\) 的值极限存在。先对有限体积二阶界积分得到弦差，再除以 \(n\)，最后在三个参数点分别取熵值极限，即得系数 \(1/50\)。没有假设 \(h\) 二阶可微，也没有对 \(o(n)\) 值误差求导。

## 9. 源码与书面证明对照

没有发现承重的 proof/code mismatch。

| 文件 | 对照结论 |
|---|---|
| `density_sine.hpp` | 有理 \(\pi\) 包络、模约化、degree-23 Taylor 和 \(10^{-20}\) 余项与正文一致 |
| `density_global.cpp` | 60 个 bias cells、完整新密度端点、一维自适应包络与正文一致 |
| `density_guard.cpp` | 256 词×6 根 cells、二维参数细分、Loewner/PSD/原子下界与正文一致 |
| `density_witness.cpp` | 真实条件 DPP 递归、四前缀全覆盖、参考测试重建、55 移动实际律节点与正文一致 |
| `verify_density.py` | 精确常数、Lebesgue/根积界、总余项、二维 Bernstein 判号均可从输入重新生成 |
| coverage/collection/probe scripts | 明确检查 1,536 jobs、256 词、55 节点、每节点 \(2^{22}\) 词及质量包含 1 |

`cert_interval.hpp`、`exact_fixed.hpp`、`arithmetic_selftest.cpp` 和 guard 整数与已接受的 S63 版本在数学内容上相同；文本差异只有末尾空行。`density_guard.cpp` 中有一个未调用的旧 `alpha()` helper，不进入任何计算或证明。

## 10. 独立重放

隔离目录：

`math/sa02-sol-takeover-20260918/QWE07_CYCLE17_REPRODUCTION/`

环境：Windows x86-64，本机无 WSL；使用此前 S63 审核接受的便携 w64devkit GCC 16.2.0、Boost 1.92.0。编译参数保持

```text
-O3 -frounding-math -ffp-contract=off -std=c++17
```

guard 和 witness 另加 `-fopenmp`。64-significand-bit binary `long double` 静态断言实际通过。

从隔离目录执行的等价命令序列为：

```text
g++ -O3 -frounding-math -ffp-contract=off -std=c++17 -I BOOST arithmetic_selftest.cpp -o arithmetic_selftest.exe
g++ -O3 -frounding-math -ffp-contract=off -std=c++17 density_global.cpp -o density_global.exe
g++ -O3 -frounding-math -ffp-contract=off -std=c++17 -fopenmp density_guard.cpp -o density_guard.exe
g++ -O3 -frounding-math -ffp-contract=off -std=c++17 -fopenmp density_witness.cpp -o density_witness.exe
arithmetic_selftest.exe
density_global.exe 1009 3000
python verify_density.py --constants-only
python replay_guard.py
density_witness.exe build
python replay_nodes.py
python collect_nodes.py fresh_witness_nodes.log fresh_nodes_collected.txt
density_witness.exe probe 17 50 3 125
density_witness.exe probe 1 2 3 125
python verify_probes.py
python verify_density.py
```

其中四个 C++ 源和作者 Python verifier 均来自冻结源目录；两个 `replay_*.py` 是本审查新增的隔离驱动，负责直接解析新进程输出、检查完整覆盖并生成 reviewer-owned 表和日志。

### 10.1 先做的 supplied-output 精确后检

在任何新重算之前，精确 Python 后检单独验证了作者给出的：

- 256 词 guard 叶覆盖；
- 55 节点整数表的完整索引和宽度；
- 所有精确 Bernstein 系数与最终支付符号；
- 两个 probe 的有理减法和负 gap；
- \(\rho=1/3\) 五个新节点与已接受 S63 包络相交。

这一步只验证 supplied integer outputs 的内部数学含义，不等于重新生成它们。

### 10.2 新计算重放

随后从冻结 C++ 源重新编译并完成以下独立生成：

| 项目 | 新重放结果 |
|---|---|
| 算术自检 | 138,828 个精确有理比较，四种硬件舍入模式全部 PASS |
| 全局 pair 包络 | 60/60 cells，24,292 个标量盒，PASS |
| guard 包络 | 1,536/1,536 jobs，256 词，1,562 成功叶，零失败 |
| guard 精确覆盖 | 成功叶共 94,459,902 个内部盒，闭矩形完整覆盖 |
| 参考测试重建 | 全部 4,194,304 词；质量区间含 1 |
| 势范数 | \(V_0\le1485.550333<1500\)，\(V_1\le9201.505796<10000\) |
| 移动实际律节点 | 55/55 节点，每节点全部 4,194,304 词，质量区间含 1 |
| 节点整数外包 | 每个宽度至多 \(2\cdot10^{-8}\)，逐项等于 supplied table |
| 精确连续闭合 | 总误差 \(.000933783743461632<.001\)，99+55 Bernstein 系数全正 |
| \(\rho=.34\) probe | 原见证充分支付 gap 位于 \([-0.06194256,-0.06194254]\) |
| \(\rho=.5\) probe | 原见证充分支付 gap 位于 \([-122.92793866,-122.92793864]\) |

参考测试缓存是本次从 4,194,304 个参考词重新生成的约 256 MiB 中间文件；没有使用作者二进制缓存。完整 55 节点重算生成 230,686,720 个配置叶。guard replay driver 直接消费每个新 C++ 进程的输出并在内存中做有理矩形覆盖核验，不读取作者成功日志。

重放脚本和紧凑日志随审查保存；大型可执行文件和二进制缓存不进入审查 PR。

## 11. 见证特定障碍

重新计算 \(a=3/125\) 时：

\[
\rho=\frac{17}{50}:
P-(C_0-1)d\in[-0.06194256,-0.06194254],
\]

\[
\rho=\frac12:
P-(C_0-1)d\in[-122.92793866,-122.92793864].
\]

这严格否定“保持相同 affine \(B_z\) 与相同固定测试 \(f\)，即可把当前充分支付不等式直接延伸到这些点”。即使尚未认证带外 guard caps，这个必要的充分支付式本身已经失败。

它不是 \(H_n''>0\) 的反例，也不是熵率非凹性的证明。重新设计测试函数、PSD 分配或采用其他论证仍可能成功。作者对此作用域限定正确。

## 12. 精确剩余缺口与作用域

已声明矩形内部没有发现未支付的证明义务。尚未完成的是范围扩张：

1. 没有到达 \(\rho=.34\)，更没有到达 \(1/2\)；
2. 没有证明同一见证在当前上端以外的 guard/PSD 条件；
3. 没有证明所有密度、所有对比度或完整合法 bias 区间的凹性；
4. 带外负 payment 只否定当前充分证书；
5. 本审查不认证工具的外部新颖性或优先权。

若继续输运，最小剩余充分不等式仍是：在新密度带上重新认证全局/guard caps 与 PSD 分配后，构造新的测试或分配，使

\[
E_{\rho,a}V_{\rm new}(a,Y)
-(C_{0,\rm new}-1)d_{\rho,c}(a)>0
\]

统一成立，并保持有限上界以支付窗口边界。

## 13. 最终意见

QWE07 不是有限网格外推，也没有把密度变化伪装成共同对角平移。nested-subspace 正场后验序、完整实际概率向量的复解析主控、二维余项账本和精确 Bernstein 闭合组成了一条可独立核验的密度输运链。新 guard 与完整 55 节点计算均已隔离重放。

因此，冻结矩形上的有限体积曲率界与熵率弦差结论升级为 **VERIFIED_SCOPED**。半密度、全密度和全局凹性继续保持 **INCOMPLETE**；两个带外点仅为原见证的 **COUNTEREXAMPLE_WITH_SCOPE**。
