# S71 / QWE08 Cycle24 重放记录

## 来源边界

```text
source  C:/game/gameproject/showa100/math/sa-dispatch-20260918/
        harvest/CYCLE24/S71/S71_VISIBLE_RESULT.md
lines   629
tail    SOURCE_PARTIAL_TAIL
cut     §10 Resumption boundary, mid-sentence
```

§1–9、完整证明和完整 Python code fence 均在截断前。没有 ZIP、工具回执或作者执行日志。

## 作者状态与本次状态

- 作者可见稿明确写：`Execution status: not verified in this deliverable.`
- 本审查从可见 code fence 提取 assertion body，保存为 `S71_CYCLE24_EXACT_CHECK.py`。
- 本审查实际运行成功，退出码 `0`。

两种状态不可混写：作者当时未执行；审查者本次已执行。

## 环境与命令

```text
Python 3.12.14
standard library only

python research/INDEPENDENT_REVIEW_20260918/S71_CYCLE24_EXACT_CHECK.py
```

## 实际输出

```json
{
  "object": "Affine mixture of actual endpoint sine laws",
  "not_the_object": "Actual intermediate kernel-shift DPP",
  "block_lengths": [
    20000,
    20000
  ],
  "count_variance_strict_upper": "879127/1800",
  "classification_error_strict_upper": "879127/18000000",
  "MI_chord_gap_strict_lower_nats": "1/10",
  "same_parity_covariance_in_mixture": "1/40000",
  "original_all_size_conjecture": "UNRESOLVED"
}
```

## 独立算术核对

参数为

```text
c=19/20, a0=1/50, a1=3/100, rho=1/2, lambda=1/2, L=20000.
```

两 endpoint 的单站点均值是 `99/200` 与 `101/200`。扣掉 DPP off-diagonal bulk 后，单位长度 count variance 为

```text
487/20000.
```

使用 `pi>3`、`log(20000)<10` 和 `D_L<=(log L+4)/pi²`：

```text
L*v + c² D_L
< 487 + (361/400)*(14/9)
= 879127/1800.
```

均值差为 `L*(a1-a0)=200`，midpoint classifier 的 Chebyshev error 满足

```text
4*(879127/1800)/200²
=879127/18000000
<1/20.
```

再用 `log 2>1/2` 与 `h_b(1/20)<1/5`：

```text
h_b(1/2)-2h_b(error) > 1/2-2/5 = 1/10 nat.
```

mixture 的同 parity pair covariance 是

```text
lambda*(1-lambda)*(a1-a0)² = 1/40000.
```

以上均对应概率律仿射 mixture；没有一步把中点替换成实际 `DPP(a_lambda I+cQ)`。

## 两点 seed sanity check

仅作代数核对，不作为证明输入：

```text
c=19/20
d=c²/pi²                     0.09144236823720985
C(d)                         1.5454670142325355
8+C(d)                       9.545467014232536
```

## 外部定理核对

Russell Lyons, *Determinantal probability measures*, Theorem 8.1 的原文对任意 positive contraction `Q` 声明对应 determinantal measure 具有 conditional negative associations with external fields。这里使用的只是其较弱结论：有限 Hermitian positive-contraction DPP 上，互不相交坐标集支持的递增函数协方差非正。

严格 contraction 不是 Lyons 定理额外要求；它在本稿中用于保证全部 atoms 为正、score 和逆矩阵有定义。
