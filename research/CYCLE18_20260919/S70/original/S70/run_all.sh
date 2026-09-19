#!/usr/bin/env bash
# Reconstruct the mathematical certificates from readable sources and integers.
# No network, repository write, hash, checksum, or preexisting binary cache is used.
set -euo pipefail
ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
CXX=${CXX:-g++}
PYTHON=${PYTHON:-python3}
THREADS=${THREADS:-4}
OUT=${OUT:-"$ROOT/recomputed"}
if [[ ! "$THREADS" =~ ^[1-9][0-9]*$ ]]; then echo 'THREADS must be a positive integer' >&2; exit 2; fi
mkdir -p "$OUT/work" "$OUT/logs" "$OUT/evidence"
cp "$ROOT"/certificates/*.cpp "$ROOT"/certificates/*.hpp "$ROOT"/certificates/*.py "$ROOT"/certificates/*.txt "$OUT/work/"
cd "$OUT/work"
FLAGS=(-O3 -frounding-math -ffp-contract=off -std=c++17)
for name in principal_probability_certificate arithmetic_selftest arithmetic_audit; do
  "$CXX" "${FLAGS[@]}" "$name.cpp" -o "$name"
done
for name in quad_global quad_guard quad_payment direct_payment_check; do
  "$CXX" "${FLAGS[@]}" -fopenmp "$name.cpp" -o "$name"
done
./arithmetic_selftest > ../logs/arithmetic_selftest.log 2>&1
./arithmetic_audit > ../evidence/arithmetic_cases.tsv
"$PYTHON" arithmetic_audit.py > ../logs/arithmetic_audit.log 2>&1
"$PYTHON" exact_small_tests.py > ../logs/exact_small_tests.log 2>&1
"$PYTHON" exact_block_test.py > ../logs/exact_block_test.log 2>&1
# Prefixes are disjoint exact partitions of all 2^22 configuration words.
for prefix in 0 1 2 3; do
  ./principal_probability_certificate 22 2 "$prefix" "prob22_${prefix}.bin" > "../logs/prob22_${prefix}.log" 2>&1
done
# Every cell is a continuum enclosure, not a sample at its center.
./quad_global 140 240 "$THREADS" 7 > ../logs/global.log 2>&1
for distance in 1 2 3; do
  ./quad_guard "$distance" 7 6 0 10752 "$THREADS" 4000000 7 > "../logs/guard_distance${distance}.log" 2>&1
done
./quad_payment "$THREADS" > ../logs/payment.log 2>&1
./direct_payment_check "$THREADS" > ../logs/direct_payment_check.log 2>&1
"$PYTHON" exact_closure.py --eta 1/25 --output ../evidence/continuum_broad.json > ../logs/continuum_broad.log 2>&1
# The broad-rectangle PSD certificate also applies to this nested rectangle.
"$PYTHON" exact_closure.py --c-upper 953/1000 --eta 1/5 --skip-psd --output ../evidence/continuum_narrow.json > ../logs/continuum_narrow.log 2>&1
"$PYTHON" exact_obstruction.py > ../logs/fixed_witness_obstruction.log 2>&1
"$PYTHON" verify_coverage.py --logs ../logs --output ../evidence/coverage.json > ../logs/coverage.log 2>&1
cp quad_payment_coefficients_bivariate.txt quad_payment_norms_integer.txt ../evidence/
printf 'All required source verifications terminated successfully. Read the source-defined inequalities and exact evidence in %s.\n' "$OUT"
