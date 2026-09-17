# S18 复现记录

状态：`SUPPORTED_SCOPED`。

## 输入身份

- `RESULTS18`：完整 16 节正文，SHA256 `0B7F486029604266A2E092BEC98B12F9C02B7A618392E70F27E52484339C355B`。
- `PRO02_checks S18`：正文声明的 `PRO02_checks.py`，SHA256 `EE2F53C56E7DE33F8A9AF4A1B7C7B216F727C4EA081919D4752E46E7002BD2DF`。
- 正文标题、主常数、两个枚举值和合法障碍与 `harvest/S18.md` 完全对应。

## 执行命令

```text
C:\Users\UIO\.local\bin\uv.exe run --with mpmath --with numpy --with sympy python "C:\Users\UIO\Desktop\20260907\PRO02_checks S18"
```

退出码为零。关键输出：

```text
symbolic_rank_one_identity=true
new_A=50251200/2197
n6_probability_sum=1.0
n6_Hpp=-49.5655212392509631975961954433
n6_minus_E_Phi=-49.5655212392509631975961954433
n6_identity_error=9.9568244e-60
W_4_2=-10.13300431506280689245412
random_minimum_Jensen_slack=4.73054600573e-05
obstruction_finite_defect_over_qv=-0.525556206741
```

## 解析审计

通过：

1. (5.3)、(5.6) 的秩一 Hessian 与相反符号界；
2. (5.12)--(5.18) 的权重、无序 pair 计数和 `Gamma_ro`；
3. (6.6) 的储备残差和通道方差恒等式；
4. (9.7)、(9.14) 的有序方向、块数与端点归一化。

限制：没有重新认证 S18 显式导入的全部 S7/SA02 旧事实；有限随机测试不构成一般证明；没有大窗口负号证书。
