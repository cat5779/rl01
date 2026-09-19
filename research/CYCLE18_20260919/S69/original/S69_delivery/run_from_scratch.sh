#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
THREADS="${THREADS:-8}"
CXX="${CXX:-g++}"
BASE=(-O3 -frounding-math -ffp-contract=off -std=c++17)
OMP=(-fopenmp)
mkdir -p build logs

compile() { "$CXX" "${BASE[@]}" "$@"; }
compile global_ratio_certificate_s69.cpp -o build/global_ratio_certificate_s69
compile "${OMP[@]}" guard_certificate_s69.cpp -o build/guard_certificate_s69
compile principal_probability_certificate.cpp -o build/principal_probability_certificate
compile "${OMP[@]}" payment_prepare_s69.cpp -o build/payment_prepare_s69
compile "${OMP[@]}" payment_step_s69.cpp -o build/payment_step_s69
compile "${OMP[@]}" payment_extract_integer_s69.cpp -o build/payment_extract_integer_s69
compile global_ratio_probe_026_tight.cpp -o build/global_ratio_probe_026_tight
compile "${OMP[@]}" guard_probe_026_tight.cpp -o build/guard_probe_026_tight
compile principal_probability_certificate_026.cpp -o build/principal_probability_certificate_026
compile "${OMP[@]}" score_ceiling_026_tight.cpp -o build/score_ceiling_026_tight

./build/global_ratio_certificate_s69 > logs/global_ratio_s69.log 2>&1

GUARD_LOGS=()
for cell in $(seq 0 10); do
  start=$((cell*256)); finish=$(((cell+1)*256))
  log="logs/guard_full_cell${cell}.log"
  ./build/guard_certificate_s69 11 -1 "$THREADS" 5000000 "$start" "$finish" > "$log" 2>&1
  GUARD_LOGS+=("$log")
done
./check_guard_logs.py 0-10 "${GUARD_LOGS[@]}" | tee logs/check_guard_full.log

pids=()
for k in 0 1 2 3; do
  ./build/principal_probability_certificate 22 2 "$k" "./prob22_${k}.bin" > "logs/probability_${k}.log" 2>&1 &
  pids+=("$!")
done
for p in "${pids[@]}"; do wait "$p"; done

./build/payment_prepare_s69 | tee logs/payment_prepare_s69.log
for k in 0 1 2 3 4 5 6 7; do
  ./build/payment_step_s69 "$k" | tee "logs/payment_step_${k}.log"
done
for k in 0 1 2 3 4 5 6 7; do
  ./build/payment_extract_integer_s69 "$k" | tee "logs/payment_extract_integer_${k}.log"
done
./assemble_payment_coefficients_s69.py | tee logs/assemble_payment_coefficients_s69.log
./verify_rational_s69.py | tee logs/verify_rational_s69.log
./verify_failure_audit_s69.py | tee logs/verify_failure_audit_s69.log

./build/global_ratio_probe_026_tight > logs/global_ratio_probe_026_tight.log 2>&1
PROBE_LOGS=()
for start in 0 64 128 192; do
  finish=$((start+64)); log="logs/guard_probe_026_${start}_${finish}.log"
  ./build/guard_probe_026_tight "$start" "$finish" "$THREADS" 5000000 > "$log" 2>&1
  PROBE_LOGS+=("$log")
done
./check_guard_logs.py 11 "${PROBE_LOGS[@]}" | tee logs/check_guard_probe_026.log
./verify_tight_probe_026.py | tee logs/verify_tight_probe_026.log

pids=()
for k in 0 1 2 3; do
  ./build/principal_probability_certificate_026 22 2 "$k" "./prob26_${k}.bin" > "logs/probability26_${k}.log" 2>&1 &
  pids+=("$!")
done
for p in "${pids[@]}"; do wait "$p"; done
./build/score_ceiling_026_tight | tee logs/score_ceiling_026_tight.log

echo "S69 FULL SOURCE RERUN PASS"
