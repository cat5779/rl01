# S79 Cycle31 复现记录

审查日期：2026-09-20（Asia/Singapore）

## 1. 作者源码安全检查

执行前完整检查 `S79_AUTHOR_SECOND_CHAOS_SHELL.py`。它只导入标准库、NumPy 和 mpmath，进行本地组合枚举、矩阵运算和高精度算术；未发现网络访问、子进程、文件写入、动态执行、反序列化或随机采样。随后运行归档副本，而不是运行一个经过改写的版本。

运行环境：Python 3.12.14、NumPy 2.3.5、mpmath 1.3.0。实际输出保存在 `S79_AUTHOR_EXECUTION.log`，退出码为 0。

## 2. 作者计算复现结果

严格区间主结论复现为

\[
H''\in[
10.47453113847398137818526924002716783087495642744639248227461584711737446340842402854,
10.47453113847398137818526924002716783087495642744639248227461584711737446341269181388
],
\]

故 (m=36,c=4/5) 的混合 layer-bistochastic 通道有严格正曲率。作者输出中的壳基线、协方差项、Jeffreys payment 和 gap 也复现：

```text
Hstar=-294.2957856094156
-Cov=6.130529639058225
4rDeltaE=3.661890073400335
gap=2.4686395656578903
```

这些四个数是普通浮点诊断；它们各自没有被冒充为区间证书。严格正曲率由前述高精度 outward interval 承担。

作者的 (m=2,\ldots,7) consecutive-Fourier 表也复现。最大浮点残差为：unitary `1.7763634531418856e-15`，bistochastic/deletion `1.9984014443252818e-15`，curvature `7.389644451905042e-13`，shell identity `5.258016244624741e-13`。它们只是有限尺寸实现诊断，不支持 all-size 外推。

## 3. 独立实现

`s79_independent_check.py` 不导入作者程序，仅使用 Python 标准库；其中：

1. 用 `Decimal` 和向外舍入重新构造 (m=36,c=4/5) 的混合通道曲率区间；
2. 同时计算完全壳随机化基线和二者差的严格区间；
3. 在 (m=3) 建立有理数 layer 通道，独立检查 posterior identity、完整曲率公式、paid-shell 恒等式和相对熵二阶导数关系；
4. 在 (m=4) 用 permutation exterior unitary 做 deletion intertwining 的精确有理数索引检查。

实际结果写入 `S79_INDEPENDENT_CHECK.json`：

\[
H''_{36}\in[10.4745311384739813781852692400271678,\ 10.4745311384739813781852692400271680],
\]

\[
H''_{36}-H''_{\circ,36}
\in[304.7703167478882545413267331336819263,\ 304.7703167478882545413267331336819264].
\]

两个区间下端均严格为正。因此不但总曲率反例成立，S79 针对该通道的 paid-shell 条件也严格失败。

在 (m=3) 检查中，posterior 恒等式的精确有理数残差为 0；其余 Decimal 残差均不超过 (6.3\times10^{-78})。(m=4) permutation-unitary deletion 检查精确通过。程序最终打印 `PASS_INDEPENDENT_S79_CHECKS` 并以 0 退出。

## 4. 证据强度

- **严格证书：** (m=36) 正曲率、壳差严格为正。
- **精确/解析核对：** posterior 恒等式、orientation/full-(a) 中点公式、postprocessing、deletion 索引、Cauchy minor 条件、total-shell 归一化。
- **有限浮点诊断：** 作者的 (m=2,\ldots,7) Fourier 表及残差。
- **未证明：** actual consecutive-Fourier 的 all-size paid-shell、(K'') 控制、finite cyclic 到 true sine rate 的二阶桥。
