# 平衡线优势边界复核记录

日期：2026-09-18。

## 已执行检查

1. `verify_c37_midpoint_pair.py`
   - `c=37/40, gamma=3/2`: PASS；
   - 多项式次数 `(5,5,21)`，777 个非零项；
   - Bernstein 正叶 249，精确删除叶 238，最大深度 21；
   - `gamma=149/100` 的严格有理障碍：PASS。
2. `verify_midpoint_interval.py`
   - 平衡线 `37/40<=c<=937/1000, gamma=199/100`: PASS；
   - 多项式次数 `(8,5,5,21)`，3245 个非零项；
   - Bernstein 正叶 609，精确删除叶 842，最大深度 25；
   - `c=15/16, gamma=2` 的严格有理障碍：PASS。
3. `c95_sine_pair_obstruction.py`
   - 256-bit Arb：PASS；
   - `g-2(K+D)=0.018961732864724365...`，球半径小于 `3e-74`；
   - 后验的上下 determinant cap 均严格为正。
4. `c37_sine_reveal.py`
   - 八点真实 sine reveal 的点态负 defect：PASS；
   - defect `-0.0264831116075124...`；
   - defect/二次变差 `-0.655207814812598...`；
   - 同一揭示序的六层实际律平均漂移全部为正。
5. `c37_comparison.py`
   - 新式 `m=6565` 首次使正误差小于 1；
   - S18 `m=82676` 首次使正误差小于 1；
   - 核心尺度比例 `12.5934501142`。
6. `enumerate_phi.py --c 0.925 4,2 6,3 8,4`
   - `W-U` 分别为 `-0.437716...,-0.593176...,-0.686851...`；
   - 小窗口中精确势比旧四次势更负，但这不替代一般窗口证明。

## 核心证书 SHA256

- `verify_c37_midpoint_pair.py`: `44875C1B3618169E406CF4D0181D071BAF0B6E49F92C2656EAE6CCB29A0DAADD`
- `verify_midpoint_interval.py`: `D3CD622393EF712DECB057FA9D257483834267A45C0DF8C162BB9228E42EA9A0`
- `c95_sine_pair_obstruction.py`: `5916485BDE9425E479D4A4F62F5C3C56118D3C7006416244C0EB34D7AFF0AFFC`

## 证据等级

- 两个 Bernstein 检查从精确有理控制网开始，所有后续非平凡平均
  向下舍入；它们是符号证书，不是抽样。
- Arb 检查使用包含真值的区间球；最终正 margin 与球半径相隔七十余
  个十进制数量级。
- `c37_sine_reveal.py` 的点态实例使用 90 位高精度，但实际律平均正
  漂移只登记为有限数值证据，不升级为一般引理。
