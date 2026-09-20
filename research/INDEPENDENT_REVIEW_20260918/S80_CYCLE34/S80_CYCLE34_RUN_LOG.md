# S80 Cycle34 独立运行记录

## 来源完整性

- 来源：`CYCLE34_20260920/S80/S80_RESULT.md`。
- 大小：21436 字节、774 行。
- 正文完整，不是可见前缀或截断稿。
- 没有随附作者计算程序；数值部分由独立脚本重建。
- 源文件含五个控制字符，破坏五处 LaTeX 命令显示；预期公式可由上下文
  唯一恢复，数学审查按恢复后的 `\big`、`\frac` 进行。

## 独立脚本

脚本：

`research/INDEPENDENT_REVIEW_20260918/S80_CYCLE34/s80_cycle34_replay.py`

输出：

`research/INDEPENDENT_REVIEW_20260918/S80_CYCLE34/S80_CYCLE34_REPLAY.json`

运行环境：Python 3.12.14、NumPy 2.3.5。

脚本执行：

1. 对 \(n=2,4,6\) 的九个 adjacent cuts 独立枚举 DPP atoms，比较
   classical MI 与 quasi-free quantum MI；
2. 对 \(\rho=.37,c=.81,a=.07,L=3,K=5\) 检查 quantum telescope；
3. 独立核对
   \(D_{1/2,6}=3/2-806/(75\pi^2)\) 与 direct trace；
4. 复算 \(R_6^{\rm q}(.025)\)、pointwise/uniform scalar bounds；
5. 枚举六点 64 个 words，检查 \(\ell,\ell',\ell''\) bounds、
   \(D_F=-E\ell''\) 与 quartic \(\mathcal I_{\rm rel}\) bound；
6. 计算 benchmark chord 的 finite seed 与 theorem (T) 浮点下界。

## 结果

总状态：

`PASS_INDEPENDENT_FLOATING_AND_EXACT_CONSTANT_CHECKS`

关键输出：

- 九个 dephasing checks 的最小 quantum-minus-classical slack：
  0.32369280967173397；
- telescope error：0.0；
- \(D_{1/2,6}\) 闭式与 direct trace 差：
  \(2.22\times10^{-16}\)；
- \(R_6^{\rm q}(.025)\)：0.17360594686589215；
- symbolic pointwise upper bound 普通求值：1.268544784082455；
- uniform \(J\) upper bound 普通求值：1.5775907710209103；
- benchmark six-site seed gap per site：0.0001034358898574；
- theorem (T) 对该 seed 的浮点下界：-0.17350251097603475；
- 六点 \(D_F\) 与 \(-E\ell''\) 的差：
  \(7.11\times10^{-15}\)。

除 \(D_{1/2,6}\) 的符号代数外，这些均为普通双精度复核，不是区间
证书。它们只验证公式、常数、归一和量级；一般定理由审查报告中的证明
承担。尤其 \(R_6^{\rm q}\) 与 benchmark chord 没有被升级为严格数值
判号。
