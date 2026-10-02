# R11/G13 对抗审查

STATUS: PARTIAL

审查对象：`output.md`，SHA-256
`3C3E775BE4708DD5AACCF97D2A5E90B5C95DF9C3F2EC7E48D78A353D08BD8748`。

## 总裁决

回传把冻结主目标 W 判为 `INCOMPLETE` 是正确的：它证明了普通弱鞅解的候选构造，并准确隔离出任意可数非 amenable 群上的不变固定点缺口；没有把普通弱存在、边缘不变性或一般单调耦合误写成不变路径律。现有文字尚不能升级 W，也不是反例。

普通弱存在的主链基本正确，但第 3 节从 birth-time 紧致极限传递“完整自然滤过鞅问题”写得过快，须补一个标准但不可省略的测试代数/端点论证；补写后未见实质障碍。因此本审查不是全文 `PASS`，也不把该可修补缺口判成路线失败。

| 承重项 | 裁决 | 核验要点 / 最小修正 |
|---|---|---|
| finite-pattern 下界 | PASS | L-ensemble 公式正确。由谱隙自动有 \(0<\varepsilon\le1/2\)，故 \(r=\varepsilon/(1-\varepsilon)\le1\)，而 \(\det(I-K_F)\ge\varepsilon^{|F|}\)、\(\det(L_F[A])\ge r^{|A|}\ge r^{|F|}\)。所给 \(c_F=\varepsilon^{|F|}r^{|F|}\) 虽粗但有效。应在正文补写 \(r\le1\) 这一步。 |
| finite-dimensional conditional rates / forward equation | PASS | (3) 是 \(dt\,\mu_t\) 下的有限坐标条件期望；正分母给 Borel 性与 \(\alpha_i^F\le m/c_F\)。柱函数只看 \(F\)，故 CE 精确化为 (5)。有限状态率矩阵的算子范数有 \(L^1(dt)\) 上界，前向积分方程唯一，因而有限链边缘确为 \(\mu_t^F\)。不需要、也没有声称 projective consistency。 |
| 非一致有限链的 compact birth-time 极限 | PARTIAL | 条件期望鞅收敛 (10)、同一时刻边缘恒等式 (12) 和固定有限块连续逼近足以支撑该路线；但“Consequently”一句没有严格处理历史测试函数的弱收敛。须明确 birth-time 拓扑，先对由有限坐标、有限个**正**确定时刻生成的连续点测试代数传极限，再用单调类扩到 \(\mathcal F_s\)。由于 \(T_i=0\) 有原子，含 \(X_0\) 的测试并非该拓扑的连续测试；需用 \(X_\delta\to X_0\) 的 \(L^1\) 估计 \(P(0<T_i\le\delta)=\delta H(i,i)\) 单独补上。对 \(f(X_s),f(X_t)\) 也应明说正时刻无原子使其为极限律的 a.s. 连续点。最后再以共同的一时边缘和 \(L^1(dt\,\mu_t)\) 误差令 \(m\to\infty\)。 |
| 闭性/紧致性 \(\mathcal S(a,\mu)\) | PARTIAL | 结论可沿上一行同一论证得到，但不能只写“preceding argument also shows”：应逐列写明任意 \(P^k\to P\) 时一时边缘在正时刻的连续点传递、零时刻的 \(\delta\downarrow0\) 修补，以及固定有限柱近似给出的、与 \(k\) 无关的漂移误差。补后 compact/convex 结论成立。 |
| 局部可积与 càdlàg | PASS | 固定边缘加 Tonelli 给 (15)；全局跳时集合至多可数，故 \(X_t=X_{t-}\) 对 \(dt\) a.e.。每坐标单跳，配合可和权重的 dominated convergence，确给产品拓扑下 càdlàg 路径。总跳率可为无穷，不影响有限柱生成元。 |
| 无同时跳 | PASS | 用 \(x_i,x_j,x_ix_j\) 三个柱测试得到连续补偿子；分部积分后共同跳计数 \(S_{ij}\) 是非负递增局部鞅，故恒为零。须保留“局部化后”以及只计 \((0,t]\) 的说明；\(t=0\) 的初始占据不是跳。可数并集排除任意两个乃至无限同时跳。 |
| 非 amenable invariance gap | PASS | \(P\mapsto gP\) 保持同一边缘和鞅问题，但非空 compact convex \(\Gamma\)-空间一般无固定点；有限集穷竭本身不提供不变性。回传没有误用平均。 |
| amenable / weak-uniqueness 限制定理 | PASS | Følner 平均仍在 \(\mathcal S(a,\mu)\)，闭性补写后极限不变；TV 边界估计正确。弱唯一性版本也正确，但附加假设应明确为：给定 \(\mu_0\) 与该生成元，在单调 coordinatewise-càdlàg pure-birth 鞅解类中 law 唯一。两者都不推出独立 Poisson、强解或 iid 因子。 |
| DPP regularization reduction | PASS | 在题面已准许的协变 rate 构造前提下，对 \(K_t^\delta=\delta I+(1-2\delta)(Q_0+t(Q_1-Q_0))\) 应用 W，端点给不变单调耦合；\(\delta\downarrow0\) 时有限行列式连续、序关系与不变性闭，故得到一般 \(Q_0\le Q_1\) 的不变 DPP 耦合。此为“W 会蕴含什么”，不是 W 的证明。 |

## 文献边界

1. **Mester：结论使用合格，但必须换掉占位引用。** Péter Mester, *Invariant monotone coupling need not exist*, Ann. Probab. 41 (2013), 1180–1190, DOI [10.1214/12-AOP767](https://doi.org/10.1214/12-AOP767)，确给出 Cayley 图上的两个不变随机子图：存在普通单调耦合，却不存在不变单调耦合。它只证明“一般不变边缘 + 普通耦合不足”，并非本 W 的反例；回传对此范围限制正确。

2. **Lyons–Thom：需按定理级引用，范围基本准确。** Lyons–Thom, *Invariant Coupling of Determinantal Measures on Sofic Groups*, ETDS 36 (2016), Theorem 5.1 / [arXiv:1402.0969](https://arxiv.org/abs/1402.0969)，对有限生成 sofic 群及 \(\ell^2(\Gamma)\)（并含 Cayley 边空间版本）上的等变正压缩 \(Q_1\le Q_2\) 给 \(\Gamma\)-不变单调 DPP 耦合。因此若 W 加题面 rate 构造可处理任意可数群，它的确严格超出该已引定理的量词。不得反向写成 Lyons–Thom 已证明任意群，也不得据 Mester 声称某个 DPP 对失败。

3. `:chatgpt-content-reference{...}` 不是可审计引用，公开或规范稿中必须删除，替换为上面的作者、题名、定理号/DOI。

## 最小修正后的可登记状态

- 冻结主目标 W：`INCOMPLETE`；任意群不变固定点 (23) 未证，亦无满足全部 DPP/rate 条件的反例。
- 普通 prescribed-generator 弱存在：`PARTIAL_DRAFT_PASS`；补齐第 3 节测试代数、零时刻与闭性三处验缝后可升级为 `CORRECT_SCOPED`。
- amenable W 与 weak-uniqueness W：`CORRECT_RESTRICTED`，必须保留新增假设。
- simultaneous-jump、local-integrability、product-càdlàg：`PASS`，依赖补齐后的普通鞅问题。
- DPP regularization 与文献比较：`PASS_AS_CONSEQUENCE/BOUNDARY`，不计 W 证明或反例。

