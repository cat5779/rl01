#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
CXX=${CXX:-g++}
FLAGS=(-O3 -frounding-math -ffp-contract=off -std=c++17)
"$CXX" "${FLAGS[@]}" arithmetic_selftest.cpp -o arithmetic_selftest
"$CXX" "${FLAGS[@]}" density_global.cpp -o density_global
"$CXX" "${FLAGS[@]}" -fopenmp density_guard.cpp -o density_guard
"$CXX" "${FLAGS[@]}" -fopenmp density_witness.cpp -o density_witness
./arithmetic_selftest | tee fresh_arithmetic_selftest.log
python3 verify_density.py --constants-only | tee fresh_constants.log
./density_global 1009 3000 2>&1 | tee fresh_global.log
./density_guard 0 1536 4 > fresh_guard.log 2>&1
python3 check_guard_coverage.py fresh_guard.log | tee fresh_guard_coverage.log
./density_witness build > fresh_witness_build.log 2>&1
./density_witness nodes 0 55 > fresh_witness_nodes.log 2>&1
python3 collect_nodes.py fresh_witness_nodes.log nodes_integer.txt | tee fresh_nodes_coverage.log
python3 verify_density.py | tee fresh_density_closure.log
./density_witness probe 17 50 3 125 > probe_034.log 2>&1
./density_witness probe 1 2 3 125 > probe_half.log 2>&1
python3 verify_probes.py | tee fresh_probe_obstructions.log
python3 check_reference_overlap.py ../sources/S63_CERTIFICATES/payment_coefficients_integer.txt nodes_integer.txt | tee fresh_reference_overlap.log
printf '%s\n' 'QWE07: complete interval calculations, exact continuum closure, and scope checks passed.'
