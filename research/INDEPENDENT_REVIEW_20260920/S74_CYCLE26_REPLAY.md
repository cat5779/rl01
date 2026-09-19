# S74 Cycle26 独立复现记录

复现日期：2026-09-20（Asia/Singapore）

## 1. 作者 interval checker 实际重放

用户后补 `certify_mixed.py` 和 `certificate.json`。静态检查确认程序没有网络、子进程、动态执行、反序列化或输入读取；唯一写操作是硬编码的 `/mnt/data/S74/certificate.json`。

为保持作者计算源码原样并避免在 Windows 根目录造路径，审查运行通过 `runpy` 执行原文件，只用受限 `open` wrapper 把该一个输出路径重定向到系统临时文件。Python 进程退出码为 0，全部断言通过。实际标准输出见 `S74_CYCLE26_AUTHOR_INTERVAL_REPLAY.log`。

重放结果与下载的 `certificate.json` 逐字段完全一致。

### 外向区间审计

- `IV.q` 使用 floor/`ceildiv` 包围有理数；乘法检查四个端点；倒数按符号分支并反向端点；所有后续运算保持外向。
- `arctan_inv` 的第 90 项截断后按下一项符号和大小加入交错级数余项。Machin 线性组合继续用区间减法。
- `log_atanh_unit` 在 \(1\le x\le2\) 上使用正项 atanh 展开，85 项后的上尾由
  \[
  2z^{171}/[171(1-z^2)]
  \]
  包住；`log_iv` 利用单调性分别包围输入区间两端。
- determinant 是 division-free subset Laplace recurrence，全部矩阵项使用同一 interval 类型。
- `atoms(6)` 和 `atoms(6,rect=True)` 分别枚举基点与矩形上的 64 个 interval atoms；两轮均逐 atom 断言下端严格正，并验证总质量区间包含 1。
- rectangle 模式对第 1、6 个 diagonal entries 各加入 \([0,10^{-10}]\)。dependency 丢失只使区间变宽，因此输出包含每个 \((u,v)\) 参数点。

实际证明的 uniform bound 为

\[
\mathcal M_{uv}(u,v)<-3/10000
\quad(0\le u,v\le10^{-10}),
\]

从而双积分 rectangle defect 小于 \(-3\times10^{-24}\)。

## 2. 独立程序

执行：

```text
python -B research/INDEPENDENT_REVIEW_20260920/S74_CYCLE26_INDEPENDENT_CHECK.py
```

环境为 Python 3.12.14，仅用标准库。进程退出码 0。实际标准输出见 `S74_CYCLE26_INDEPENDENT_CHECK.log`。

## 3. 精确有理复算

由正文 (1) 直接计算：

\[
B_{1/50}=865433616303812500000,
\]

\[
6(1/50)^{-12}=1464843750000000000000,
\]

所以 \(B_{1/50}\le6\delta^{-12}\)。产品区域得到

\[
\kappa_1\ge27353/8192,
\qquad \kappa_1/2\ge27353/16384.
\]

半密度两点候选预算独立算得约

\[
-5.8063080125817152161\times10^{19},
\]

确认该预算不支付。

## 4. Merge-tree 诊断

程序在半密度 8 点 Toeplitz compression 上取四个长度 2 的相邻 leaves，用平衡 binary tree 收费。所得

\[
\sum_{\rm cuts}\|Q_{AB}\|_{HS}^2
\]

与

\[
\tfrac12[\operatorname{tr}Q_8^2-4\operatorname{tr}Q_2^2]
\]

在 80 位精度下一致。一般性结论仍由 pair 的最低共同祖先计数证明承担，数值只检查实现。

## 5. 六点独立重建

以 Machin 公式在 Decimal 中构造 \(\pi\)，建立

\[
K=\tfrac12I+\frac{19}{20\pi}T.
\]

程序直接枚举 64 个 masked determinants，使用删除坐标的实际 marginal 实现 cofactor 导数。检查结果：

- 总概率在 80 位精度下为 1；
- 全部 atoms 为正；
- mixed coordinate 为负；
- `C_acc` 为负；
- `D_F+C_acc` 为正。

独立中心值逐位进入正文声称区间，并与 PR63 的 `D_F,C_acc,M''` 浮点输出一致。

本实现使用高精度 Decimal，但没有 outward rounding 和解析 remainder enclosure。因此它只作跨实现核对；严格区间由已经重放的作者 checker 承担。

## 6. 证据结论

- 一般 cut theorem、merge accounting 和 rate bridge：由解析审查支持。
- 产品区域系数：由精确有理计算支持。
- 六点符号与小矩形：作者 directed fixed-point interval checker 已实际重放，退出码 0；独立 Decimal 和 PR63 提供交叉核对。
- 全高对比度和全部密度：没有证书。
