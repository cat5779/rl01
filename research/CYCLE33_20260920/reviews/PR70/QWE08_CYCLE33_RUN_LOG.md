# QWE08 Cycle33 独立运行记录

## 来源

审查来源位于：

`C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE33_20260920/QWE08/`

包含：

- `QWE08_RESULT.md`；
- `certify_qwe08.py`；
- `mi_continuum_certificates.json`。

对应上游为 `randomcat4/dpp-stationary-entropy` PR130，审查对象为用户
指定版本；验收依赖数学内容和 fresh run，而非版本标识。

## 作者严格证书实际重跑

使用工作区 Python 3.12.14，命令等价于：

```text
python certify_qwe08.py --max-n 4 --order 24 --directory <fresh-output>
```

输出：

```text
n 1 F(mid) [4, 4] higher_even_H_negative True uniform_F_lower [3.9999999741982, 3.9999999741982]
n 2 F(mid) [9.5454670142325, 9.5454670142325] higher_even_H_negative True uniform_F_lower [9.5454669213460, 9.5454669213460]
n 3 F(mid) [17.907876884449, 17.907876884449] higher_even_H_negative True uniform_F_lower [17.907876633655, 17.907876633655]
n 4 F(mid) [27.423750308635, 27.423750308635] higher_even_H_negative True uniform_F_lower [27.423749706731, 27.423749706731]
All adjacent splits certified; minimum lower enclosure: [1.5454668697424313269, 1.5454668697424313269]
Elapsed seconds: 0.031000000017229468
```

程序在 fresh directory 中重新生成全部 atom、entropy coefficient 与
acceptance integer；随附 JSON 没有被读取为验收输入。重新生成的最终
证书内容与归档 JSON 一致。

## 区间实现检查

- 端点统一表示为整数除以 \(2^{256}\)。
- 加减乘除和倒数均按上下端点向外取整。
- \(\pi\) 使用 Machin identity，atan 交错余项显式包围。
- log 使用 atanh 级数和正几何余尾；输入先缩放至合法区间。
- conditional DPP recursion 检查每步条件概率严格位于 \((0,1)\)。
- odd Taylor coefficients 必须包含零，否则立即失败。
- 所有 curvature sign 判据比较整数端点；Decimal 只打印结果。

## 独立重放

脚本：

`research/INDEPENDENT_REVIEW_20260918/QWE08_CYCLE33/qwe08_cycle33_replay.py`

输出：

`research/INDEPENDENT_REVIEW_20260918/QWE08_CYCLE33/QWE08_CYCLE33_REPLAY.json`

独立重放没有复用作者的 interval recurrence。它执行：

1. determinant atoms 加 deleted-coordinate marginal derivatives 重建
   common-shift \(M''\)；
2. 10 个随机复 rank-one \(2\times3\) cross blocks 的全部 300 个切割；
3. 五点有限差分交叉检查；
4. 半密度 \(n=2,3\) 的 36 个全合法参数网格实例；
5. 用 `Fraction` 精确提取四点系数 \(-1/27\)；
6. 检查四点 \(D^5=0\) 与 exact shift polynomial；
7. 独立读取归档 JSON 的整数接受不等式。

结果：

```text
PASS_INDEPENDENT_ALGEBRA_AND_FLOATING_CHECKS_AUTHOR_INTERVAL_RUN_SEPARATE
```

关键数值：

- rank-one 定量下界最小浮点 slack：\(1.2414\times10^{-8}\)；
- 五点差分最大误差：\(3.8456\times10^{-8}\)；
- 36 个小 sine 实例最小 \(M''\)：\(1.3176\times10^{-4}\)；
- nilpotent shift polynomial 最大误差：\(4.17\times10^{-17}\)。

浮点部分只排查实现和符号错误。一般 rank-one 定理由审查报告中的
代数证明承担；finite continuum 结论由作者固定点区间程序的 fresh run
承担。
