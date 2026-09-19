# QWE07 Cycle17 independent reproduction

This directory contains only reviewer-generated build products, replay logs, and exact closure outputs. The author package remains unchanged under `math/sa-dispatch-20260918/harvest/CYCLE17/QWE07/original/`.

The C++ programs are compiled directly from the frozen author sources with the previously accepted portable x86-64 GCC/Boost toolchain. Runtime integer inputs are copied textually for isolated execution; generated witness caches and logs are not treated as supplied evidence.

## Environment

- Windows x86-64; no WSL.
- w64devkit GCC 16.2.0.
- Boost 1.92.0 for the arithmetic self-test.
- `-O3 -frounding-math -ffp-contract=off -std=c++17`; add `-fopenmp` for guard and witness programs.

## Replay order

1. Compile `arithmetic_selftest.cpp`, `density_global.cpp`, `density_guard.cpp`, and `density_witness.cpp` from the frozen author source directory, placing executables here.
2. Run `arithmetic_selftest.exe`, `density_global.exe 1009 3000`, and the author's `verify_density.py --constants-only`.
3. Run `python replay_guard.py`. This launches all 1,536 fresh guard jobs in six chunks and verifies the exact rational rectangle cover in memory.
4. Run `density_witness.exe build`. This regenerates `witness_cache.bin` from all `2^22` reference words.
5. Run `python replay_nodes.py`. This evaluates all 55 moving-law nodes, checks all `2^22` words and normalization at each node, and writes `fresh_witness_nodes.log` plus `fresh_nodes_integer.txt`.
6. Run the two witness probes and the author's exact postchecks.

## Committed evidence

The review PR should contain this README, the two replay drivers, compact build/guard/postcheck logs, the complete fresh 55-node log, and the regenerated integer node table. Executables and `witness_cache.bin` are deliberately excluded because they are reproducible build products.
