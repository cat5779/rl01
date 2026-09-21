# S71 acceleration 项真实正弦有限诊断

## 结论

**`C_acc >= 0` 被严格证伪；有限网格内没有发现 `M''<0`。**

最小反例就是两个相邻单点块，不需要大规模枚举。对任意实际两点正弦
Toeplitz 压缩，记

\[
u=a+c\rho,
\qquad
d=c^2\left(\frac{\sin(\pi\rho)}{\pi}\right)^2>0,
\]

四个原子为

\[
p_{11}=u^2-d,quad
p_{00}=(1-u)^2-d,quad
p_{10}=p_{01}=u(1-u)+d=:r.
\]

共同 identity shift 下，四个原子的二阶导分别是
\((2,2,-2,-2)\)。边缘原子的二阶导为零，故

\[
\begin{aligned}
C_{\rm acc}
&=2\log\frac{p_{11}}{u^2}
+2\log\frac{p_{00}}{(1-u)^2}
-4\log\frac r{u(1-u)}\\
&=2\log\frac{p_{11}p_{00}}{r^2}.
\end{aligned}
\]

直接展开得到

\[
p_{11}p_{00}=r^2-d,
\]

所以在全部合法严格参数上

\[
\boxed{C_{\rm acc}=2\log(1-d/r^2)<0.}
\]

因此，S74 不应尝试证明 acceleration 项单独非负。正确的候选结构是：
它是一个负的反曲率项，但可能始终由非负 Fisher 缺陷支付。

来源对象为
`C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE24_20260919/S71/S71_VISIBLE_RESULT.md`。
本诊断没有重跑 PR58/PR61 的 reveal 枚举，也没有修改其数学裁决。

## 1. 冻结量

对相邻块 \(A,B\)，完整联合律为实际有限 DPP

\[
K_{a,c,N}=aI+cQ_{\rho,N},
\qquad N=|A|+|B|.
\]

对输出 word \(y\)，令

\[
R_y=(K-\operatorname{diag}(1-y))^{-1},
\quad S_y=\operatorname{tr}R_y,
\quad T_y=S_y^2-\operatorname{tr}(R_y^2).
\]

程序只计算 S71 已定位的三个量：

\[
D_F=\mathbb ES^2-\mathbb ES_A^2-\mathbb ES_B^2,
\]

\[
C_{\rm acc}
=\mathbb E\left[T_Y\log\frac{P(Y)}{P_A(Y_A)P_B(Y_B)}\right],
\]

\[
M''=D_F+C_{\rm acc}.
\]

## 2. 安全实现与独立交叉核对

第一条计算路径用真实全输出权重

\[
P(y)=(-1)^{N-|y|}
\det(K-\operatorname{diag}(1-y))
\]

和 resolvent 公式

\[
P'=PS,
\qquad P''=PT.
\]

第二条独立路径不使用 \(\operatorname{tr}R\) 生成导数。对每个 word，
把 Hermitian 矩阵

\[
B_y=cQ-\operatorname{diag}(1-y)
\]

的特征值重建成标量多项式

\[
P_y(a)=(-1)^{N-|y|}\det(aI+B_y),
\]

直接微分该多项式得到 \(P_y',P_y''\)，再计算

\[
H''=-\sum_yP_y''\log P_y-sum_y\frac{(P_y')^2}{P_y},
\]

最终以 \(H_A''+H_B''-H_{A\cup B}''\) 交叉核对 \(M''\)。

全部 945 个 block 案例中：

- 概率归一误差至多 \(1.23\times10^{-15}\)；
- 一、二阶总质量误差至多 \(5.45\times10^{-15}\)、
  \(3.02\times10^{-14}\)；
- decomposition 与直接 resolvent 熵曲率误差至多
  \(3.42\times10^{-13}\)；
- resolvent 与行列式多项式熵曲率误差至多
  \(1.37\times10^{-12}\)。

最坏 masked matrix 条件数约 999；稀有原子的多项式概率相对误差至多
\(3.12\times10^{-9}\)，但承重的熵二阶交叉误差仍在上述
\(10^{-12}\) 量级。

## 3. 精确两点证书

取最简单的半密度中点实例

\[
\rho=\frac12,qquad c=\frac{93}{100},qquad
a=\frac{1-c}{2}=\frac7{200}.
\]

此时 \(u=1/2\)、\(d=c^2/\pi^2\)，于是

\[
C_{\rm acc}
=4\log\frac{1/4-d}{1/4+d}<0,
\]

而

\[
D_F=\frac2{1/4-d}-8=\frac{32d}{1-4d}>0.
\]

二者之和为

\[
M''(d)=\frac2{1/4-d}
+4\log\frac{1/4-d}{1/4+d}-8.
\]

它满足 \(M''(0)=0\)，且

\[
\frac{d}{dd}M''(d)
=\frac{4d}{(1/4-d)^2(1/4+d)}>0,
\]

所以这个最小模型同时严格证明

\[
C_{\rm acc}<0,qquad D_F>0,qquad M''>0.
\]

附带的标准库精确检查器只用 \(3<\pi<22/7\) 和

\[
x<\operatorname{atanh}x<\frac{x}{1-x^2}
\quad(0<x<1)
\]

给出有理包围

\[
-3.60839<C_{\rm acc}<-2.80199,
\qquad
4.31240<D_F<4.99546.
\]

实际双精度全输出值为

\[
D_F=4.317750545584095,
\]

\[
C_{\rm acc}=-2.928389960160608,
\]

\[
M''=1.389360585423488.
\]

负 acceleration 消耗了约 \(67.82\%\) 的 Fisher 缺陷，但没有翻转
总曲率。

## 4. 有限扫描

扫描严格限定为：

- \(\rho\in\{1/4,1/2,3/4\}\)；
- \(c\in\{.93,.95,.99\}\)；
- \(p=a/(1-c)\in\{.1,.25,.5,.75,.9\}\)；
- 21 个平衡或不平衡相邻分割，最大总长度 10；
- 每个模型枚举全部 \(2^N\) 个真实输出 word。

结果：

| 项目 | 结果 |
|---|---:|
| block 案例数 | 945 |
| \(C_{\rm acc}<0\) | 945 |
| \(M''<0\) | 0 |
| \(C_{\rm acc}\) 范围 | \([-80.1884,-2.34236]\) |
| \(D_F\) 范围 | \([4.13662,399.157]\) |
| \(M''\) 范围 | \([1.38936,318.969]\) |
| 最大支付比例 \(-C_{\rm acc}/D_F\) | 0.683214 |

按总长度汇总：

| \(N\) | 案例数 | 最小 \(M''\) | 最大 \(-C_{\rm acc}/D_F\) | 最负 \(C_{\rm acc}\) |
|---:|---:|---:|---:|---:|
| 2 | 45 | 1.38936 | 0.678222 | -4.38700 |
| 3 | 90 | 2.35386 | 0.611240 | -8.33964 |
| 4 | 135 | 2.62862 | 0.655872 | -16.0086 |
| 5 | 90 | 3.88819 | 0.675996 | -22.9593 |
| 6 | 225 | 3.60719 | 0.683214 | -33.0960 |
| 7 | 90 | 6.63029 | 0.675336 | -42.5752 |
| 8 | 135 | 6.79059 | 0.668633 | -54.7546 |
| 10 | 135 | 10.5017 | 0.679901 | -80.1884 |

最接近吃完 Fisher 缺陷的测试点是

\[
(\rho,c,p;m,n)=(.25,.93,.9;3,3),
\]

其中

\[
D_F=16.2302320497,quad
C_{\rm acc}=-11.0887128090,quad
M''=5.14151924068.
\]

最负的 \(C_{\rm acc}\) 出现在

\[
(\rho,c,p;m,n)=(.25,.99,.1;5,5),
\]

但此处 \(D_F=399.15745\) 足以支付 \(C_{\rm acc}=-80.18833\)，
所以它不是最接近总曲率反例的点。

## 5. 对 S74 最有价值的假设

有限证据支持的方向不是

\[
C_{\rm acc}\ge0,
\]

而是以下二层结构：

\[
C_{\rm acc}\le0
\quad\text{以及}\quad
-C_{\rm acc}\le D_F.
\]

第一层在相邻两单点块上已经严格成立；945 个测试点全部同号，但这仍
不能升级为任意块定理。第二层正好等价于 \(M''\ge0\)，所以不能只改名
后当作新引理。真正可能有用的加强应把它局部化，例如：

1. 把 \(-C_{\rm acc}\) 表成跨边界 pair/条件协方差预算；
2. 证明该预算由 \(D_F\) 中对应的跨块 score 投影支付；
3. 或在固定谱隙紧集上证明严格比例
   \(-C_{\rm acc}\le(1-\varepsilon)D_F\)，并明确
   \(\varepsilon(\delta,\rho,c)\) 的退化方式。

网格中最大的已观察比例约 0.683，并没有逼近 1；这是值得追踪的
定量信号，但绝不是比例定理。

## 6. 作用域

- **严格证伪：** acceleration 项单独非负；反例已在真实相邻两点
  sine DPP 上解析成立。
- **有限诊断支持：** 所列 945 个实际模型均有 \(M''>0\)，且
  Fisher 缺陷支付负 acceleration。
- **未证明：** 任意块、任意尺寸、连续参数上的 \(M''\ge0\)；
  \(C_{\rm acc}\le0\) 的一般块版本；任何固定比例支付；熵率凹性。

## 7. 重放

```powershell
python research/INDEPENDENT_REVIEW_20260918/S71_ACCELERATION_DIAGNOSTIC_CYCLE25/s71_acceleration_scan.py `
  --output research/INDEPENDENT_REVIEW_20260918/S71_ACCELERATION_DIAGNOSTIC_CYCLE25/S71_ACCELERATION_SCAN.json

python research/INDEPENDENT_REVIEW_20260918/S71_ACCELERATION_DIAGNOSTIC_CYCLE25/s71_two_site_certificate.py `
  --output research/INDEPENDENT_REVIEW_20260918/S71_ACCELERATION_DIAGNOSTIC_CYCLE25/S71_TWO_SITE_CERTIFICATE.json
```
