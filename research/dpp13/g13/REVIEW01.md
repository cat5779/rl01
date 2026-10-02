PARTIAL

# R13/G13 独立数学审查

审查对象：`source.md`（SHA-256
`9C68BA67F9A2F25DD3D46E0799948E02F39FB6DB58082D12E36D87015F0E94D5`），相对冻结题面
`task.md`（SHA-256
`562693B5C31326096BC7A2DF126C482DA91B91DB97CC9A913E18838E9905CB7E`）。

## 总裁决

原稿把任意群不变路径律的固定点问题约化为细分区间上的**动态可实现两端点耦合**固定点，主结构是正确而且有实际推进的；尤其，“每一层细分重新独立选择端点固定点，无须跨层 projective consistency”这一点不是偷换量词。非可和群上的平均也没有被暗用：不变性来自不变网格骨架的等变插值，再由与真正解的统一小网格距离传给共同弱极限。

但是，当前文字还不是该约化定理的完整证明。它只恢复了弱极限的初始边缘，没有真正写出从正时刻历史测试到时刻零自然滤过鞅恒等式的极限；更重要的是，“无同时正时刻跳”并非 birth-time 弱拓扑下的闭性质，原稿完全没有从极限鞅问题重新推出这一点。拼接处的确定时刻跳和条件解的共同满测集也只被略写。这些缺口均有标准且看起来可闭合的补法，未发现反例或方向性错误，因此裁决为 `PARTIAL`，不是 `FAIL`。

冻结主目标 (W) 仍严格是 `INCOMPLETE`：原稿既没有证明任意可数群上的局部端点固定点必存在，也没有构造满足全部 DPP/rate 条件而无不变解的反例。

## 1. 双向 two-time 约化

令 
\[
\mathcal E_{u,v}=\{\operatorname{Law}_P(X_u,X_v):P\in\mathcal S_{u,v}\},
\]
其中必须保留“由给定 Borel 生成元在整个 ([u,v]) 上动态实现”这一限定。原稿的核心候选定理是：

> (W) 成立，当且仅当在某一列网格趋零的有限分割上，每个相邻小区间的
> (mathcal E_{u,v}) 都含有一个对角 (Gamma)-不变元。

该陈述的两个方向如下。

### 必要性：PASS

不变全路径律限制到任意 ([u,v]) 仍是不变区间解，其两端点律当然属于
(mathcal E_{u,v}^{\Gamma})。这里得到的其实比 dyadic 条件更强：每个区间都有不变动态可实现端点律。

### 充分性主链：PASS，以下述闭性补证为条件

1. 对每个小区间任选 (pi_k\in\mathcal E_{t_{k-1},t_k}^{\Gamma})，再任选实现它的区间解 (P_k)。不同区间和不同细分层之间均可独立选择。
2. 将 (P_k) 按初值解体为 (R_k(x,d\omega))。对自然滤过鞅恒等式使用可数决定族并按 (X_{t_{k-1}}) 再解体，可得对 (mu_{t_{k-1}})-几乎处处 (x)，(R_k(x,cdot)) 是从 (x) 出发的区间解。
3. 两端点核 (Q_k(x,dy)) 是不变耦合 (pi_k) 关于第一坐标的正则条件分布。由 (pi_k) 和 (mu_{t_{k-1}}) 的不变性及条件分布唯一性，对每个 (g) 有
   
   \[
   Q_k(gx,gA)=Q_k(x,A)
   \]
   
   对 (mu_{t_{k-1}})-几乎处处 (x) 成立。群与柱生成代数均可数，故可取共同满测集；做网格骨架积分时，几乎处处等变已经足够，不需要全点版本。
4. 依次用 (R_k) 拼接会保持每个时刻的精确边缘和生成元鞅问题。虽然区间内部条件律可不等变，网格骨架的 Markov 乘积只用 (Q_k)，因而整体骨架不变。
5. 把每个坐标的真实出生时刻向右推到首次出现的网格点，所得插值 (I_n) 是精确等变的；其像律 (widetilde P^{(n)}) 不变。真实律 (P^{(n)}) 与该像律可在同一骨架上耦合，使每个有限出生时刻移动不超过网格宽度，故在加权 birth-time 乘积度量下
   
   \[
   d_{\mathrm{Pr}}(P^{(n)},\widetilde P^{(n)})\le |\Pi_n|.
   \]
6. (B=[0,1]\sqcup\{\infty\}) 取 (infty) 为孤立点时是紧可度量空间，故 (B^\Gamma) 紧。任取 (P^{(n_j)}\Rightarrow P)，同一距离估计给
   (widetilde P^{(n_j)}\Rightarrow P)。坐标平移是 (B^\Gamma) 上的同胚，不变概率律集合弱闭，所以 (P) 不变。

因此约化并没有把“不变边缘”误当“不变路径律”，也没有使用 amenability。真正需要补完的是最后一步：证明这个共同弱极限仍属于题面要求的 ordinary solution class。

## 2. 紧性、闭图与不变性审计

| 环节 | 裁决 | 理由 |
|---|---|---|
| birth-time 紧性 | PASS | 每个坐标只有一个出生时刻，(B^\Gamma) 为可数紧空间乘积；这里不需要总跳率可和。 |
| 不变性闭性 | PASS | (widetilde P^{(n)}) 精确不变且与 (P^{(n)}) 的 Prokhorov 距离趋零；对每个固定 (g)，推前映射连续，所以共同极限不变。没有对非可和群做轨道平均。 |
| 固定边缘 | PASS_AFTER_DETAIL | 正时刻 (t) 上，单坐标出生分布为 (C(i,i)+tH(i,i))，无正时刻原子；有限块评价因而是极限律的几乎处处连续映射，可传递 (mu_t)。(t=0) 应由 (X_\delta\to X_0) 逐路径及 (mu_\delta\Rightarrow\mu_0) 恢复，而不能直接调用评价连续性。原稿思路足够，但 (28) 后的措辞应明确采用这一论证。 |
| Borel 无界漂移的闭性 | PASS_AFTER_DETAIL | 对 (ho(dt,dx)=dt\,\mu_t(dx))，协变性和 (A) 给每个 (a_i\in L^1(\rho))。 bounded finite-coordinate、continuous-time 因子在 (L^1(\rho)) 中稠密；固定边缘把近似误差精确转成与 (n) 无关的 (L^1) 误差。相应时间积分是 birth-time 拓扑下连续泛函。这里确实给出了避免“Borel 率下闭图当然成立”这一错误的正确机制。 |
| 正时刻自然历史鞅问题 | PASS_AFTER_DETAIL | 对有限个正确定时刻的历史柱测试，端点评价在极限律下几乎处处连续；先传 bounded approximants，再用统一 (L^1(\rho)) 误差恢复真率，最后以单调类扩张。需要明说先对有理时刻决定族证明，再用 càdlàg 与漂移的 (L^1) 连续性扩到任意 (s<t)。 |
| 时刻零自然历史鞅问题 | GAP-1 | 原稿只说 (28) “recovers the initial law”，这不足以证明 (M_t^f) 关于 (mathcal F_0) 的鞅恒等式。应先对 (r>0) 证明，以 (h(X_r)) 测试 (M_t^f-M_r^f)，再令 (r\downarrow0)。由 coordinatewise 右连续性和 (int_0^r\sum_{i\in F}E[a_i(s,X_s)]ds\to0)，有 (M_r^f\to0) 于 (L^1)，且 (h(X_r)\to h(X_0))。补上此段后可闭合。 |
| 无同时正时刻跳 | GAP-2 | 该性质不是弱闭的；不同坐标的两个跳时可以在极限中碰合。原稿从 (29) 直接写 (P\in\mathcal S(a,\mu))，漏掉题面明确要求的这一项。补法是对 (x_i,x_j,x_ix_j) 使用已传递的鞅问题。若 (A_i(t)=\int_0^t a_i(s,X_{s-})ds)，则有限变差分部积分与乘积柱函数的补偿式表明 (sum_{0<s\le t}\Delta X_i(s)\Delta X_j(s)) 是非负递增局部鞅，故恒为零；再对可数坐标对取并。必须把这个论证写入，而不能声称闭性自动保留。 |

综上，紧性和不变性没有被偷用；“解集合闭”也有正确的固定边缘 (L^1) 核心，但当前稿件尚缺 GAP-1、GAP-2，因而不能把完整闭图结论登记为已经证明。

## 3. 拼接步骤的剩余技术义务

原稿第 3--4 节的拼接结论可成立，但正式稿还应补以下共同满测集细节。

1. 可数决定族除鞅恒等式外，还应同时包含区间漂移的绝对可积性、初值确为 (x)、单调/单跳支撑；所有例外集取并后再定义 (R_k) 的无关版本。
2. 每个正 dyadic 边界 (t_k) 上不能产生额外跳。由固定连续一时边缘，任一坐标在确定时刻 (t_k>0) 跳的概率为零；对可数坐标、有限边界取并即可。这样相邻段连接不会制造边界同时跳。
3. 全局过去给定边界状态后，新段按 (R_k) 条件独立抽取；据此，区间内的条件鞅恒等式才可通过塔式条件期望提升到拼接后的完整自然滤过。原稿提到该思路，但应写出一次测试函数计算。

这些是可修补的技术缺口，不破坏 two-time reduction 的方向。

## 4. 可复用定理与强度分类

### 可复用候选定理 A：局部端点固定点约化

在补齐上述闭性和普通性检查后，可登记：对题面给定的线性 DPP 曲线和 pure-birth Borel rate field，(W) 等价于在任一网格趋零的有限分割列上，每个相邻区间的动态可实现端点集合 (mathcal E_{u,v}) 含不变元。各区间、各层固定点无须相容。

相对 (W) 的分类：`EQUIVALENT_REDUCTION`，不是 (W) 的证明，也不是反例。它把剩余义务精确压缩到两时刻，但 (mathcal E_{u,v}) 的定义仍含整个小区间的生成元可实现性，不能替换成“所有单调端点耦合”。

### 可复用候选定理 B：dyadic endpoint-law uniqueness

若每个 dyadic 相邻区间内，所有 prescribed-generator 区间解具有相同两端点律，则该共同端点律因协变性而不变；候选定理 A 随即给出 (W)。

相对 (W) 的分类：`SUFFICIENT_RESTRICTED_RESULT`。它只要求 endpoint-law uniqueness，不要求区间内部三时刻或全路径唯一。

不过原稿标题中的“strictly below full weak uniqueness”应降格表述。形式上 endpoint-only 条件内容更少；但要从题面所说的**全局** weak uniqueness 推到每个局部 (mathcal S_{u,v}) 的端点唯一，还需补一个“任意局部解可用既有全局解的前后条件律延拓为全局解”的拼接引理。并且原稿已承认没有本 DPP 类中的分离例，所以目前不能声称两条件在逻辑上严格不等价。安全表述是“endpoint-only sufficient hypothesis, potentially weaker; no strict separation proved”。

## 5. 任意群正面、反面与文献边界

- **任意群正面没有闭合。** 原稿没有证明任一 (mathcal E_{u,v}^{\Gamma}) 非空；它只证明“若细网格每格非空，则全局不变解存在”。因此不得把约化定理写成 arbitrary-group (W) 已证。
- **任意群反面也没有闭合。** 没有给出 uniformly gapped linear equivariant DPP path、finite-valued covariant Borel rate、精确 CE 与 (A) 全部成立而固定点为空的实例。
- Mester 例只说明一般不变过程的普通单调耦合不保证不变耦合，不能放入本题作 DPP/rate 反例。
- Lyons--Thom 的不变 DPP 端点耦合即使适用，也只落在全部单调耦合集；未证明它属于动态可实现子集 (mathcal E_{u,v})。原稿在这一点上的范围限制正确。

## 6. 精确剩余缺口

要把本回传升级为 `PASS`，最少需要：

1. 补齐正时刻历史决定族到完整自然滤过的单调类与时刻连续性论证；
2. 以 (r\downarrow0) 的 (L^1) 论证证明时刻零的鞅恒等式，而不只是初始边缘；
3. 从 (x_i,x_j,x_ix_j) 的极限鞅问题重新推出无同时正时刻跳；
4. 在段拼接处明写共同满测集、确定网格时刻无跳和塔式条件期望计算；
5. 将“strictly weaker”改为未获分离的 endpoint-only sufficient condition，或另给严格分离证明；
6. 保持最终总状态为 `INCOMPLETE`，直到证明所有所需小区间的动态端点固定点，或给出满足题面全部条件的反例。

当前可登记状态：

- arbitrary-group (W)：`INCOMPLETE`；
- local two-time fixed-point equivalence：`PARTIAL / CORE_SOUND / CLOSURE_DETAILS_PENDING`；
- dyadic endpoint-law uniqueness sufficient theorem：`PARTIAL / FOLLOWS_AFTER_CORE_COMPLETION`；
- amenable 或 full weak-uniqueness 已知推论：未被本稿冒充为主结果；
- arbitrary-group DPP counterexample：`NOT PROVIDED`。
