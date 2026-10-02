# R11/G12 独立对抗审查

**总裁决：PARTIAL。** 原稿把冻结目标标为 INCOMPLETE 是正确的；它既没有普适 selector 反例，也没有完整正定理。式 (1)--(21)、强子多面体与 cover-coupling 的仿射等价、以及一般 cover-coupling 单例纤维的 \(m\)-条件数基本通过。唯一实质数学错误是式 (28) 后把未归一化 cover 部分的放大误称为归一化 flow 的放大。最小修正后，这仍是一项可复用的局部结果，但不改变 R1b 状态。

## 逐项裁决

1. **端点 \(r\)、one-point coupling 与 half-capacity：PASS。** 令 \(A=I-K\)，秩一 Schur 补给出

   \[
   K+hP\le I\iff h\,v^*A^{-1}v\le1,
   \]

   故 \(r=1/\operatorname{tr}(P(I-K)^{-1})\in[\varepsilon,1-\varepsilon]\) 确为最大端点。对 \(h<r\) 的 one-point 单调耦合取有限单纯形极限，端点 \(M=K+rP\) 仍得到 diagonal-or-cover 耦合。其 off-diagonal 总质量由基数期望差精确等于 \(r\)。除以 \(r\) 后，散度为 \(b\)、总质量为 \(1\)，且

   \[
   F_{\rm out}(S)\le p_K(S)/r=\alpha p_K(S)\le p_K(S)/\varepsilon,
   \]

   即原容量 \(2p_K(S)/\varepsilon\) 的一半。这里没有把端点奇异性偷换成严格谱隙。

2. **\(p_h\) 的精确仿射性：PASS。** 生成行列式中的 \(hP(Z-I)\) 秩至多一，所以整个行列式以及每个 \(z\)-系数对 \(h\) 都是仿射的；因此 \(p_{K+hP}=p_K+h\,b_{K,P}\) 在 \([0,r]\) 上精确成立，不只是导数近似。

3. **强流子多面体、归一化冗余与边缘稳定：PASS。** 式 (10)--(13) 的正反映射确为仿射双射；由散度乘以 \(|S|\) 求和可自动得到总流量 \(1\)。式 (16)--(21) 的常数和量词正确：已审 signed repair 只在这里用于控制 \(b-b'\)，没有被冒充非负流；\(\alpha,r,q=p+rb\) 的 resolvent 估计均与维数无关。

4. **alternating path 的 coupling 单例与 \(m\) 放大：PASS（仅 coupling 层）。** 正支撑上的允许边恰是所列 \(2m\)-边树，故两组边缘各自唯一决定 \(\Gamma^0,\Gamma^1\)。于是

   \[
   \|\Gamma^1-\Gamma^0\|_1=2m\delta,
   \qquad
   \|\mu^1-\mu^0\|_1=2\delta,
   \]

   式 (27) 的比值 \(m\) 正确。这只证明一般 diagonal-plus-cover coupling 纤维不能仅由边缘 \(\ell^1\) 距离获得维数无关 Hausdorff 界。

5. **“scaled flow 同样放大”：FAIL。** 对原稿的均匀基线 \(a=1/(2m)\)，两耦合的 cover 总质量分别为

   \[
   r_0=ma=\tfrac12,
   \qquad
   r_1=m(a+\delta)=\tfrac12+m\delta.
   \]

   按式 (5) 真正归一化成总质量一的 flow 后，每条 cover 边均为

   \[
   F^0(u_j)=a/r_0=1/m,
   \qquad
   F^1(u_j)=(a+\delta)/r_1=1/m.
   \]

   因而 \(F^0=F^1\)，不是线性放大。式 (28) 只描述未归一化 off-diagonal coupling 质量。

   **最小修正有两种：**（a）删除式 (28) 后的 flow 推论，只保留 coupling-level 反例；或（b）改用非均匀 cover 基线。比如 \(m\) 为偶数，前 \(m/2\) 条 \(u_j\) 取 \(3/(4m)\)，后 \(m/2\) 条取 \(1/(4m)\)，所有 \(d_j\) 取 \(1/(2m)\)，再作同样的 \(u_j\mapsto u_j+\delta,\ d_j\mapsto d_j-\delta\)。若 \(t=m\delta<1/2\)，归一化 flow 距离为

   \[
   \|F^1-F^0\|_1=\frac{t}{1+2t},
   \]

   而边缘扰动仍为 \(2\delta=2t/m\)，比值为 \(m/[2(1+2t)]\)。这修复一般 cover-flow 层的线性放大，但仍完全不是 DPP 反例。

6. **与冻结 DPP 目标的量词：PASS。** 原稿明确承认路径边缘有大量零原子、未实现为固定谱隙 DPP 对；也明确承认即使强子多面体不稳定，selector 仍可使用容量更大的完整 \(\mathcal F(K,P)\)。因此它没有把一般 cover-coupling 反例误报成 DPP 全流多面体反例。冻结目标的普适 selector 证伪证书仍缺失。

7. **symmetrization：PASS。** 对每个固定 \(n\)，

   \[
   \bar\Gamma_z=\frac1{n!}\sum_{\pi\in S_n}\pi^{-1}\Gamma_{\pi z}
   \]

   仍有边缘 \(p_K,p_{K+rP}\)，保持 diagonal-or-cover 支撑；置换作用保持参数度量与 coupling 的 \(\ell^1\) 距离，故 Borel 性、等变性和 Lipschitz 常数均无损。这里应把 \(\pi^{-1}\Gamma_{\pi z}\) 明说为对两坐标同时 push-forward，但没有数学缺口。

## 范围与最小公开表述

- 可接受的新局部结论：每个有隙 DPP flow polytope 含一个非空 half-capacity strong 子多面体，并与端点 DPP 的 one-point cover-coupling polytope 仿射等价；其两边缘与缩放因子对 \((K,P)\) 维数无关稳定。
- 可接受的一般障碍：任意 cover-coupling（修正后也可说归一化 cover-flow）仅凭边缘稳定不能获得维数无关条件数。
- 不可接受的升级：这不是固定谱隙 DPP 家族的全流多面体分离，不否定所有 selector，也未证明 (DF)。
- “容量不能产生障碍”应缩为：**排除了任何依赖单个 fiber 被迫贴住上容量面的论证**；half-slack 点的存在并不排除容量与跨参数几何共同造成的选择障碍。

**最终状态：PARTIAL；冻结定理仍 INCOMPLETE。** 修正式 (28) 后的 flow 断言并收窄上述容量措辞，即为最小必要修订。

