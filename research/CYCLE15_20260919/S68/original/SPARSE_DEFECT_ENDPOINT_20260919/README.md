# 稀疏缺陷端点研究包

**日期：2026-09-19（Asia/Singapore）。目标：rl01 的真实配置熵凹性问题。**

## 先读什么

`RESULT.md` 是主报告；`APPENDIX_BOUNDS.md` 给出全部 remainder、谱隙和二阶量传递的证明；`APPENDIX_PROJECTION.md` 给出投影支持分层、留数、补偿后有限部分以及二阶常数项的符号和增长证明。

这不是完整 C(0,1) 的证明，也不是其反例。证明为本轮作者推导；随包的区间证书严格认证有限反例，浮点检查只辅助核对代数，不能替代体积极限证明。

## 最重要的结果

1. **完整二缺陷账本。** 自然异点 interaction 之外，互信息二阶系数还必须保留 `-1/2 sum_i chi²(P_i^p || P0)`；n=1 已能检出遗漏。自然 pair 曲率恰好是 S52 actual-output Bregman skew 的两倍，且不依赖 p。
2. **真实可达局部反例。** 纯整数区间证书分别认证：true sine Toeplitz n=6 的 c=1 与 c=19/20，以及 cyclic n=8、rank=4、c=19/20 的实际条件 skew 为正。对应 pair 的全实际权重平均仍为负。禁止把局部反例扩大成整体凹性反例。
3. **奇异投影端点。** 固定 n 的熵曲率有非零的一阶 `-epsilon[(n-k)/p+k/(1-p)]`，以及二阶 logarithmic 项。正则化基准的自然 pair 和存在显式负 `1/eta` 留数，常对角投影给出随 n 的留数下界。
4. **二阶常数项的实质结果。** 常对角 1/2 的满层支撑投影满足 `B2''(1/2) <= -n - 2 D_swap < 0`。对连续 Fourier 循环投影，`B2''(1/2) = -Theta(n² log n)`；补偿后的 pair 有限部分有相同量级。证明使用真实插入后验熵和 Vandermonde 交换能量。
5. **量词明确的 remainder / transfer。** 给出 full-support 与奇异层展开的显式常数；共同谱隙下，归一化完整二阶量差不超过 `2n delta^(-5) ||K-L||_F`。由此得到无噪声的对数增长窗口，以及有噪声时自然 m≈1/epsilon 窗口的多项式周期化传递。后者仍是边缘窗口之间的比较，不是 all-exterior 或完整熵率的传递。

无限 true-sine 的纯 logarithmic Gamma 猜想没有在本包中被证伪或证明。被明确证伪的是有限循环自然 pair 和的统一 logarithmic 版本。不能交换这两个量词。

## 包内文件

| 文件/目录 | 用途 |
|---|---|
| `RESULT.md` | 自包含主报告、结论和边界 |
| `APPENDIX_BOUNDS.md` | regular remainder、score/概率传递、有限 sine 谱隙、增长窗口 |
| `APPENDIX_PROJECTION.md` | 奇异展开、所有实际输出系数、留数和有限部分、后验熵、增长定理 |
| `SOURCE_AUDIT.md` | 读取的来源、未取得的仓库范围、原始来源 SHA-256 |
| `STATUS.json` | 各项结论的证明/精确认证/数值/未解决状态 |
| `src/interval_certificate.py` | **仅 Python 标准库**的纯整数区间证书 |
| `src/defects.py` | 实际输出概率、重采样 jets、pair 系数及曲率的核心实现 |
| `src/verify.py` | 124 项有限浮点代数与 remainder 检查 |
| `src/residue_checks.py` | 90 项实际留数检查 |
| `src/shape_checks.py` | 94 项后验熵、几何符号与循环增长检查 |
| `src/finite_part_checks.py` | 54 项补偿后有限部分检查 |
| `src/profile.py` | 高精度 sine 概率递归 / 实际距离剖面；支持缓存数据复算 |
| `src/run_checks.py` | 本包检查入口 |
| `results/` | 上述检查的实际输出及数值剖面 |
| `data/` | 真实 Toeplitz 概率缓存及精度说明 |
| `sources/` | 实际读到的 S51 C1、S52 原始文件；不表示外部独立认证 |
| `MANIFEST.json` | 包内文件哈希和字节数；不递归包含自身 |

## 复核方式

先解压并进入本目录。阅读证明、查看所有预计算结果或运行精确区间证书都不需要访问仓库或联网。

### 不安装第三方库：运行精确有限反例证书

```sh
python src/interval_certificate.py --output results/interval_certificate_recomputed.json
```

证书使用整数向外舍入、Machin 的 pi 区间、带严格尾界的 log 级数，以及整数平方根。`decimal_display_only` 只是显示；符号判断使用整数分子，不使用浮点小数。

### 完整浮点检查

测试环境为 Python 3.13.5、NumPy 2.3.5。所有一般检查需要 NumPy；高精度概率重算另需 mpmath 1.3.0。环境版本列于 `requirements.txt`。没有打包 Python 解释器或第三方二进制。

```sh
python src/run_checks.py
```

本轮执行结果：**362 项有限浮点检查通过，另有三个明确模型中的纯整数区间认证通过。** 这些数字不是独立审稿次数，也不等于无限体积定理。

### 从已提供的实际概率重算距离剖面

```sh
python src/profile.py --cached --rho 0.5 --ns 2,4,6,8,10,12,14,16,18 \
  --output results/toeplitz_cached_recomputed.json
python src/profile.py --cached --rho 0.25 --ns 4,8,12,14 \
  --output results/toeplitz_quarter_cached_recomputed.json
```

### 从核重新生成概率

```sh
python src/profile.py --rho 0.5 --ns 2,4,6,8,10,12 --dps 80 \
  --output results/toeplitz_from_kernel_recomputed.json
```

这是 `2^n` 全枚举。程序遇到非正概率或不合法条件核会报错，**不裁剪负概率、不把小概率替换成地板、不静默归一化**。70/80 位概率生成后，存储及统计求和仍使用 float64；相关剖面明确标记为数值诊断，不是区间证书。

## 必须保留的模型区分

- `epsilon` 是重采样概率；中点实际翻位概率是 `epsilon/2`。
- 自然 pair 和 `S_n` 用无序对 `i<j`；有序 `i!=j` 会多一个因子 2。
- `eta` 是正则化投影基准的噪声，`p0` 是其注入参数；此后定义 pair 系数时的附加参数 p 不是 p0。
- true Toeplitz 压缩在 c=1 仍 full support；完整有限循环 projection 在 c=1 只有固定粒子层支撑。
- m 点边缘窗口不是给定其余 N-m 点后的条件窗口。
- `B2''` 是奇异熵展开的二阶常数项；不是完整熵曲率，更不是 Gamma。

## 本轮未完成的核心问题

没有证明 all-exterior actual-weighted pair 和的无限距离可求和性；没有在 n≈1/epsilon 的联合尺度上控制完整稀疏展开 remainder；没有把有限循环支持奇异系数传成无限 true-sine 熵率曲率；没有消除原问题的 signed-average 难点。

本包给出的是这些问题之前必须有的正确账本、可达反例、精确奇异系数、真实补偿后对象和有限量传递，而不是将它们标记为已闭合。
