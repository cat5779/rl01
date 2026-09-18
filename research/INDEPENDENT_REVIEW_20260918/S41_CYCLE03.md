# S41 Cycle 03 独立数学审查报告

## 总评

- **可见正文完整性：PARTIAL_EXPORT。** `S41_PARTIAL.md` 共取得 20,488 字节；第 1–7 节完整可见，第 8 节在“Randomized-window posterior theorem”开头截断。附件未取得，且未读取哈希文件。
- **第 1–7 节主证书：VERIFIED_SCOPED。** 对每个固定 `0<c<1`，可见证明确实构造了真实未平滑 half-filled sine DPP 的有限观测证书

\[
 \left|\Gamma(c)-\Gamma_R^{\mathrm{obs}}(c)\right|
 \le \varepsilon_{\mathrm{obs}}(c;R,m,d),
\]

 其中右端完全显式；取正文指定的 `m(R),d(R)` 后趋于零。
- **精确有限二阶导数：VERIFIED。** `w''`、两个移动权重交叉项、`q'` 和 `q''` 全部保留，没有把移动 DPP word 律误当作固定律。
- **无限 word resolvent 与有限观测比较：VERIFIED_SCOPED。** Neumann 展开给出全 word 一致可逆性；跨块 Hilbert–Schmidt 界经几何尺度迭代确实产生正文的 stretched-exponential `f_c,g_c` 包络。`delta_v,delta_q,delta_G` 的三项误差账本成立。
- **曲率坐标尾与保留核稳定性：VERIFIED_SCOPED。** 可见的 connected-kernel 分组避免了不可求和的裸双差分；正文列出的各项和界足以被 `T_c(m)` 支配。有限保留核的 Lipschitz 常数 `128a^12m^2` 很粗，但代数上足够。
- **概率律与核替换误差为零：VERIFIED。** 有限 word 律是无限 noisy sine DPP 的真实主子矩阵边缘律，并非 Fejer、循环或补造外部 word；因此期望比较只支付 pointwise posterior/resolvent 观测误差。
- **冻结 `Gamma` 接口：VERIFIED_SCOPED。** 本稿的 `overline G` 与冻结文件 `SA03_VOLUME_LIMIT.md` 的 (V14) 相同，且

\[
 F_{x,R}''(1/2)=E_{x,R}\overline{\mathcal G}_{x,R},
 \qquad
 \Gamma(c)=\int_0^1uE_{cu,\infty}\overline{\mathcal G}_{cu,\infty}\,du.
\]

 这认证的是冻结 half-filled、balanced-point 局部曲率泛函；不自动认证真实熵率凹性。
- **响应坐标账本：VERIFIED_BY_PRIOR_REVIEW。** 采用已经独立核验的 S42 Fisher-dual 恒等式；在 `ell=R` 时响应损失严格为零，因此主有限观测证书不依赖响应尾估计。
- **第 8 节 `O(log L/L)` 标量定位：NOT_REVIEWED。** 正文在定理陈述开头即截断；它不能由第 1–7 节自动推出，也不应计入本轮结论。
- **实用性：EFFECTIVE_BUT_EXTREMELY_WEAK。** 误差确实显式且渐近消失，但在 `c=0.95` 附近常数巨大，当前证书主要是存在性/可计算性结果，不是可行的数值判号工具。

## 1. 证据边界

主审材料为

`C:/game/gameproject/showa100/math/rl01-sa-cycle04-20260918/research/CYCLE04_20260918/S41_PARTIAL.md`。

为核对接口，本报告还只读检查了冻结定义文件：

- `results/SA03/SA03_VOLUME_LIMIT.md`；
- `results/SA03/SA03_S9_SIGNED_TRANSPORT.md`。

冻结文件本身仍带有“待独立对抗性审查”标记。本报告只确认 S41 的有限对象收敛到其中**已经定义的同一个** `Gamma(c)`；不把冻结包中其他未审结论一并升级。

## 2. 有限观测对象与精确微分

**状态：VERIFIED。**

在 `C_R={-R,...,-1,1,...,R}` 上，

\[
 K_{x,C_R}(1/2)=\frac{1-x}{2}I+xQ_{C_R}
\]

正是无限 noisy sine DPP 的主子矩阵核。对 word `z`，

\[
 w_z(h)=(-1)^{2R-|z|}\det B_z(h),
 \qquad
 q_z(h)=h-b^*B_z(h)^{-1}b
\]

分别是真实 word 概率和只观察 `C_R` 后的中心后验。

由于 `B'(h)=I`，令 `G=B^{-1}`、`v=Gb`，直接微分给出

\[
 G'=-G^2,
 \quad
 w'=w\operatorname{tr}G,
 \quad
 w''=w\{(\operatorname{tr}G)^2-\operatorname{tr}(G^2)\},
\]

\[
 q'=1+\|v\|^2,
 \qquad
 q''=-2b^*G^3b.
\]

因此

\[
\begin{aligned}
F''(1/2)=\sum_z\{&w''\phi(q)
+2w'\phi'(q)q'\\
&+w[\phi''(q)(q')^2+\phi'(q)q'']\}.
\end{aligned}
\]

这条式子保留了概率加速度和移动律交叉项。另有

\[
 \phi''(q)=\frac1{2q^2(1-q)^2},
\]

与正文一致。

`K_{x,V}(h)` 只需在 `h=1/2` 的邻域合法；因 `x<=c<1` 留有谱隙，所需局部微分没有域问题。

## 3. 有符号曲率核

**状态：VERIFIED_SCOPED。**

写

\[
 B_z=\frac12S_z+A_x,
 \qquad
 G_z=B_z^{-1},
 \qquad
 \bar r_i=\sigma_i-G_{ii}.
\]

矩阵行列式引理给 word 律的精确输运恒等式 `partial_h w=T^*w`。Sherman–Morrison 翻位式给

\[
 Tq=-\sum_i|v_i|^2,
 \qquad
 TG=G^2.
\]

所以对 `D=partial_h+T`，

\[
 Dq=1,
 \qquad
 DG=0.
\]

再对 `D phi(q)` 微分并保留离散 Bregman 缺陷，正好得到正文式 (1) 的 `overline G`。这也是冻结定义 (V14) 的同一分组核；没有调用正 Markov 半群或正 Dirichlet 耗散。

该推导与第 2 节的逐 word 二阶微分互相校验，故

\[
 F_{x,R}''(1/2)=E_{x,R}\overline{\mathcal G}_{x,R}.
\]

## 4. 一致 resolvent 尾包络

**状态：VERIFIED_SCOPED。**

因为

\[
 \|2S_zA_x\|\le x\le c<1,
\]

全无限 word 及所有主压缩都满足

\[
 G_z=2\sum_{k\ge0}(-2S_zA_x)^kS_z,
 \qquad
 \|G_z\|\le a=\frac2{1-c}.
\]

投影恒等式 `||Q_{C0}||^2=1/4` 给 `||v||<=L=c/(1-c)`。独立信道表示同时保证任意条件后验位于

\[
 [1/a,1-1/a],
\]

所以全部 `phi` 导数、赔率和翻位分母都有统一界。

对相距尺度 `t>=2s` 的块，sine 核的 `1/|i-j|` 尾给

\[
 \|(I-P_t)TP_s\|\le4c\sqrt{s/t}.
\]

把 Neumann 词按第一次跨出几何半径 `B,B^2,...` 分组：

- 初始中心列尾贡献不超过 `2sqrt(2)c/[pi(1-c)sqrt(B)]`；
- 逐尺度泄漏的双几何和不超过 `4c^2/[(1-c)^2sqrt(B)]`；
- 剩余长词由 `c^{K+2}/(1-c)` 支付。

这正产生正文的 `V_c`。对 resolvent 列从点源开始同样分组，得到

\[
 \frac{8c}{(1-c)^2\sqrt B}+\frac{2c^{K+1}}{1-c}.
\]

取 `r=sqrt(log s)`、`B=floor(e^r)` 及相应 `K`，便得到正文的

\[
 \|(I-P_s)v\|\le f_c(s),
 \qquad
 \sup_i\|(I-P_s^i)Ge_i\|\le g_c(s).
\]

因此这些 stretched-exponential 包络不是只从旧文件抄来的未证假设。

## 5. 曲率坐标尾和保留核稳定性

**状态：VERIFIED_SCOPED。**

正文把双翻位部分保持为 connected 分组，并用

\[
 K_1=|G_{ij}||v_i|^3|v_j|,
 \quad
 K_2=|G_{ij}|^2|v_i|^4,
\]

\[
 K_3=|G_{ij}|^2|v_i|^2|v_j|^2,
 \quad
 K_4=|G_{ij}|^4|v_i|^4
\]

及带权 connected 项控制。对“至少一个指标在 `C_m` 外”的区域，行平方和、响应尾以及把内指标再分成 `C_{m/2}` 与其补集，确实给出正文列出的 `f_c(m)`、`f_c(m/2)^2` 和 `g_c(m/2)^2` 三类预算。利用 `L<=a/2`、`a>=2`，所有显示系数可被

\[
 T_c(m)=16a^{16}\{f_c(m)+f_c(m/2)^2+g_c(m/2)^2\}
\]

支配。

对保留在 `C_m` 的有限核，秩一更新的局部 Lipschitz 界给每个单指标和双指标项分别至多常数倍 `a^12 Delta`。由于 `|C_m|=2m`，

\[
 8a^3+[31(2m)+10(2m)^2]a^{12}
 \le128a^{12}m^2
\]

对 `m>=2` 成立。常数非常保守，但足以证明正文式 (3)。

## 6. 全外部后验与有限观测后验

**状态：VERIFIED。**

有限对象 `G_R,v_R,q_R` 是对 `z_R` 条件化所得的真正 Schur 补，不是把未观测坐标设为零。把其向量嵌入全空间后，方程相减得到

\[
 B(v-v_R)=(I-P_R)b-(I-P_R)A_xP_Rv_R.
\]

中心列尾、跨块界以及在 `P_d` 内外分割，给

\[
 \|v-v_R\|\le\delta_v.
\]

随后

\[
 |q-q_R|\le L\beta_R+\frac c2\delta_v=\delta_q.
\]

对每个 `i in C_m`，

\[
 B(G-G_R)e_i=-(I-P_R)A_xP_RG_Re_i,
\]

且 `C_d` 外距 `i` 至少 `d-m`，所以

\[
 \|(G-G_R)e_i\|\le\delta_G.
\]

这里 `2m<=d`、`2d<=R` 正是两个几何分割所需的范围条件。结合前节两侧坐标尾和保留核稳定性，得到逐 word 一致比较

\[
 |\overline{\mathcal G}_{x,\infty}(z)
 -\overline{\mathcal G}_{x,R}(z_R)|
 \le E_{\mathrm{obs}}.
\]

## 7. 概率律接口与主证书

**状态：VERIFIED_SCOPED。**

DPP 对子集的限制正是主子矩阵核的 DPP，因此 `z_R` 在无限实际律下的分布等于有限公式中的 `w_{x,R}`。于是无需另付 total variation、Fejer 或循环核误差：

\[
 E_{x,R}\overline{\mathcal G}_{x,R}
 =E_{x,\infty}[\overline{\mathcal G}_{x,R}(z_R)].
\]

令 `x=cu` 并按冻结定义积分，得到

\[
\begin{aligned}
|\Gamma(c)-\Gamma_R^{\mathrm{obs}}(c)|
&\le\int_0^1uE_{\mathrm{obs}}\,du\\
&=\frac12E_{\mathrm{obs}}
=\varepsilon_{\mathrm{obs}}.
\end{aligned}
\]

该接口的作用域必须保持为：half-filled sine、balanced point、冻结局部曲率 `Gamma(c)`。它没有自动完成从局部曲率到真实 full-configuration entropy rate Hessian 的传递。

## 8. 参数极限

**状态：VERIFIED。**

取

\[
 d=\lfloor R^{1/2}\rfloor,
 \qquad
 m=\left\lfloor\exp\left(\frac{\kappa\sqrt{\log R}}{64}\right)\right\rfloor,
\]

并作有限整数调整满足 `2m<=d`、`2d<=R`。则

\[
 T_c(m)\to0,
 \quad
 m^2R^{-1/2}\to0,
 \quad
 m^2R^{-1/4}\to0,
\]

以及

\[
 m^2f_c(d)\to0,
 \qquad
 m^2g_c(d-m)\to0.
\]

因此 `epsilon_obs->0`。正文所写

\[
 O_c\!\left(\exp\{-\kappa^{3/2}(\log R)^{1/4}/16\}\right)
\]

是比直接最慢项更保守的合法摘要；真正有效内容仍是前面显示的有限公式。

## 9. 常数的数值效用

**状态：UTILITY_WARNING。**

在 `c=0.95` 时，

\[
 a=40,
 \quad L=19,
 \quad \kappa=-\log(0.95)\approx0.051293,
\]

且

\[
 V_c\approx1461.11,
 \quad F_c\approx2086.32,
 \quad G_c\approx4339.21.
\]

仅让 `16a^16F_c exp[-kappa sqrt(log m)]` 降到 `1` 以下，就粗略要求

\[
 \log m\gtrsim1.8\times10^6.
\]

若再使用正文给定的缓慢日程 `m(R)`，对应量级约为

\[
 \log R\gtrsim5\times10^{18}.
\]

这不是对定理正确性的反例，却说明证书在 `c=19/20` 附近无法现实地承担有限规模判号。它证明“存在显式有限证书并渐近收敛”，不能替代尖锐的数值下界。

## 10. 截断的第 8 节

**状态：NOT_REVIEWED。**

可见文本只声称另有实际律标量后验的 `O(log L/L)` 定位机制，随后在定理首句截断。由于缺少：

- 随机窗口的完整定义；
- 条件方差/互信息或鞅估计；
- 常数和适用范围；
- 从标量后验到完整 resolvent 数据的桥接；

本轮不能认证该速率。即使完整标量定理成立，它也不会自动替换主证书中 `v,G` 的观测误差。

## 11. 最终裁决

\[
\boxed{
\text{S41 visible Sections 1--7: VERIFIED\_SCOPED}
}
\]

具体认证内容是：冻结 `Gamma(c)` 有一个使用真实 finite sine marginal 的显式有限观测近似，误差由正文 `epsilon_obs` 控制，并对每个固定 `0<c<1` 趋于零。

不认证的内容是：截断第 8 节的 `O(log L/L)` 辅助结果、`Gamma(c)` 的符号、真实熵率 Hessian 的传递，以及任何全 `rho,a` 的最终凹性结论。
