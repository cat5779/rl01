#!/usr/bin/env python3
"""Regenerate and validate all 55 QWE07 moving-law node enclosures."""
from decimal import Decimal
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
EXE = HERE / "density_witness.exe"

proc = subprocess.Popen(
    [str(EXE), "nodes", "0", "55"],
    cwd=HERE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1,
)

rows = {}
raw = []
assert proc.stdout is not None
for line in proc.stdout:
    line = line.rstrip("\r\n")
    raw.append(line)
    print(line, flush=True)
    if not line.startswith("NODE "):
        continue
    parts = line.split()
    j, k, lo, hi, den = map(int, parts[1:6])
    if (j, k) in rows:
        raise ValueError(f"duplicate node {(j, k)}")
    if den != 10**8 or not 0 <= hi - lo <= 2:
        raise ValueError(f"bad node interval: {line}")
    if parts[6:8] != ["leaves", "4194304"]:
        raise ValueError(f"incomplete word coverage: {line}")
    m = re.search(r"mass \[([^,]+),([^]]+)\]", line)
    if m is None or not Decimal(m[1]) <= 1 <= Decimal(m[2]):
        raise ValueError(f"bad mass enclosure: {line}")
    rows[j, k] = (lo, hi, den)

code = proc.wait()
if code != 0:
    raise RuntimeError(f"density_witness nodes exited {code}")
expected = {(j, k) for j in range(11) for k in range(5)}
if set(rows) != expected:
    raise ValueError(f"incomplete node set: {sorted(expected-set(rows))}")

table = "# j k lower_numerator upper_numerator denominator\n" + "".join(
    f"{j} {k} {lo} {hi} {den}\n"
    for (j, k), (lo, hi, den) in sorted(rows.items())
)
(HERE / "fresh_nodes_integer.txt").write_text(table)
(HERE / "fresh_witness_nodes.log").write_text("\n".join(raw) + "\n")

supplied = (HERE / "nodes_integer.txt").read_text().splitlines()
fresh = table.splitlines()
print(f"COMPLETE nodes {len(rows)} leaves_per_node 4194304 max_width 2e-8", flush=True)
print(f"SUPPLIED_INTEGER_TABLE_MATCH {supplied == fresh}", flush=True)
