# S74 Cycle26 独立复现记录

复现日期：2026-09-20（Asia/Singapore）

## 1. 作者附件状态

三个导出附件未出现在本地来源目录中。本审查没有作者 checker 的可执行源，故没有作者程序的安全扫描、命令、退出码或原始日志。正文中“executed successfully”只记录为作者声明。

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

本实现使用高精度 Decimal，但没有 outward rounding 和解析 remainder enclosure。因此它是独立数值重建，不是对作者 interval certificate 的替代执行。

## 6. 证据结论

- 一般 cut theorem、merge accounting 和 rate bridge：由解析审查支持。
- 产品区域系数：由精确有理计算支持。
- 六点符号：强力独立 corroboration；exact interval 附件仍未重放。
- 全高对比度和全部密度：没有证书。
