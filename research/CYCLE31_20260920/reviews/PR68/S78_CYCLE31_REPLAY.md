# S78 Cycle31 独立复现记录

复现日期：2026-09-20（Asia/Singapore）

## 1. 环境与命令

环境：Python 3.12.14，只使用标准库。

高精度诊断：

```text
python -B research/INDEPENDENT_REVIEW_20260920/S78_CYCLE31/s78_replay.py
```

退出码 0；标准输出归档于 `S78_CYCLE31_REPLAY.json`。

严格区间证书：

```text
python -B research/INDEPENDENT_REVIEW_20260920/S78_CYCLE31/s78_interval_certificate.py
```

退出码 0，末行：

```text
PASS_INDEPENDENT_S78_INTERVAL_CERTIFICATE
```

结构化输出归档于 `S78_CYCLE31_INTERVAL_CERTIFICATE.json`。

## 2. 区间证书方法

证书不读取作者附件。它首先用

\[
\pi=16\arctan(1/5)-4\arctan(1/239)
\]

和交错级数的下一项定向构造 \(\pi\) 的有理上下界，再把端点转换为外向取整 Decimal 区间。随后对真实 sine 主压缩的：

- configuration determinant；
- 条件 pair Schur complement；
- 四个实际 cell 概率；
- \(\mathcal F\)、\(\ell\) 和 logarithm；
- 全部实际 word 概率加权；

逐步外向取整。每个枚举概率和每个 pair cell 的严格正性都在程序中断言。

星形部分用 Bernoulli 数的有理公式计算偶 zeta 值，以 Rademacher cumulants 和 Bell recurrence 生成到 42 阶矩。第 21 项以后的级数用全 support 比值 \(T/A_0<1\) 和第 42 阶矩支付。

## 3. 严格结果

### 中心加入

\[
\mathbb E\Delta f_{0,-3}
\in[-0.001933130713983040159308864984082,
-0.001933130713983040159308864984081]<0.
\]

\[
\mathbb E\Delta(\mathcal F-\ell)
\in[0.1562671222889906119470844149006591,
0.1562671222889906119470844149006592]>0.
\]

### 双中心叶加入

\[
\mathbb E\Delta\Chi
\in[-4.912434017602194,-4.912434017602193]\times10^{-7}<0.
\]

### 星形 spectral-floor barrier

\[
\begin{aligned}
D_{\star,\infty}^{\rm floor}\in[&3.7456951075302371445688510467130,\\
&3.7456952529240383889998002404104].
\end{aligned}
\]

三项均包含可见续稿的显示值。

## 4. 其他独立诊断

直接枚举验证了终端 barrier 差与两个 reverse KL 之和相反，100 位计算的残差为 `-6E-100`。

对第一交互量词，固定 \(p=0,i=1\) 时，\(|b_{qi}|^4R^4\) 随 \(R=10,20,40,80\) 保持有界；但取 \(i=q+1\) 时

```text
|b_{q,i}|^4 = 0.00836170670882948278865987417596...
```

完全不随 \(R\) 衰减。这给出“固定 pair”限定的显式必要性。

## 5. 证据边界

严格区间只认证这里列出的两个有限反例、补偿符号和星形矩 barrier。一般秩一平方和、逐揭示望远镜、reverse-KL 与固定-pair barrier 由 review 中的解析推导承担。有限枚举不证明 growing-core 或 entropy-rate 结论。

作者的四个导出 certificate programs 未取得，因此没有运行、比对或声称复现其文件级输出。
