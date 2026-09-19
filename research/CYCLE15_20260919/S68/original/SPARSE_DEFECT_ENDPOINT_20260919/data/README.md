# 实际 Toeplitz 概率缓存

文件名 `P_sine_rho<RHO>_n<N>.npy` 编码 n 位 true sine Toeplitz DPP 的完整配置概率。索引 y 是整数，坐标 i 是 y 的第 i 个最低有效 bit（从 0 开始）。不是循环投影，不是 corrected law，不是等权条件表。

这些概率由 mpmath 条件核递归生成：rho=1/2 的 n=2,4,...,16 使用 70 位十进制，n=18 使用 80 位；rho=1/4 的 n=4,8,12,14 使用 70 位。随后转换成 float64 保存。统计量也用 float64 的真实概率权重求和。

未剪裁非正概率、未添加人工地板、未静默归一化。缓存没有保留全部 70/80 位文本，故它们不是区间认证数据；重新生成方式在 `src/profile.py`。严格有限符号认证由独立的 `src/interval_certificate.py` 完成，不依赖这些缓存。

原生成参数与结果在 `results/toeplitz_precision_profile.json`。其中 `elapsed_seconds` 只是各段程序当时的实测执行信息，不是本轮研究用时，也不支持关于思考时间的声称。
