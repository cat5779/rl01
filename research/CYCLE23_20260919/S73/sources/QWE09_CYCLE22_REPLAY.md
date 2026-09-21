# QWE09 Cycle22 重放记录

## 冻结输入

```text
DPP PR: 131
head: d67db7fdaf8a15b492807745d10ac3b75706690a
QWE09_RESULT.md: 903 lines
Python: 3.12.14
```

全部命令在原件的隔离读取环境运行；没有修改来源文件。

## 作者精确证书重放

命令：

```text
python QWE09_checks.py --certificate
```

真实退出状态：`0`。重新生成的字典与 `QWE09_certificate.json` 的 `certificate` 对象逐项相等：

```text
CERTIFICATE_MATCH True

observed word probability
  [0.014232864029787238,0.014232864029787239]
conditional q
  [0.291967352633421847,0.291967352633421848]
full Jensen gap
  [-0.106585307859143407,-0.106585307859143406]
cross Jensen gap
  [-0.096395465271827624,-0.096395465271827623]
quadratic variation
  [0.170309619791317635,0.170309619791317636]
necessary payment coefficient
  [0.625832574752639508,0.625832574752639509]
```

## 独立 Decimal 实现

`QWE09_CYCLE22_SIX_SITE_CHECK.py` 不导入作者模块，不使用作者 interval 类。它用标准库 `Decimal` 的 100 位精度，从 Machin 公式构造 `pi`，重新完成矩阵求逆、行列式、Schur 更新和 `Phi/Chi` 计算。

真实退出状态：`0`。输出：

```text
observed_probability 0.014232864029787238915201161651713698442594072821271027421506
q                    0.291967352633421847707435426774299914209213916433378595846972
full_gap            -0.106585307859143406958859621438636056727148780549149020847917
cross_gap           -0.096395465271827623462796413536245199120255512632598737375338
variance             0.170309619791317635103084801524650580892559297918639126904372
payment              0.625832574752639508489102948538918382378683111451404516357992
```

这些值全部严格落在作者的 dyadic 区间内。独立 Decimal 运行只是第二实现交叉检查；严格符号证书仍来自已审查的外向整数区间程序。

## 有限恒等式诊断

重新运行作者 diagnostics 至 `n=8`，共 12 个 `(n,a)` 实例，退出状态 `0`：

```text
max |H_second + E Phi|             8.526512829121202e-14
max |H_mixed + E Chi|              1.7763568394002505e-14
max |combined mask identity error| 7.815970093361102e-14
max normalization error            4.440892098500626e-16
max mask normalization error       1.1102230246251565e-16
```

这些浮点诊断不承担一般定理的证明作用。

## 参数盒精确检查

标准库 `Fraction` 重算：

```text
delta      1/50
kappa      9025/776
r_delta    49
Lambda     1486648002527/1204352
alpha max  9025/9999 < 37/40
b min      97/2475
b max      147/2525 < 3/40
```

因此 Theorem 2 的 contraction 缩放和 scalar-shift 合法域与正文一致。
