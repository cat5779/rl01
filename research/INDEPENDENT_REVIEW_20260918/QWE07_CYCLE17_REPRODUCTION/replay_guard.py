#!/usr/bin/env python3
"""Independent driver for the QWE07 guard verifier.

It regenerates all 1,536 jobs, parses only mathematical records from the
fresh process output, and checks exact rational rectangle coverage in memory.
No supplied success log is consumed.
"""
from fractions import Fraction as F
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
EXE = HERE / "density_guard.exe"

leaves = {z: [] for z in range(256)}
jobs = set()
total_nodes = 0
total_lines = 0

for first in range(0, 1536, 256):
    last = first + 256
    run = subprocess.run(
        [str(EXE), str(first), str(last), "4"],
        cwd=HERE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    if run.returncode != 0:
        raise RuntimeError(f"guard chunk {first}:{last} exited {run.returncode}\n{run.stdout[-4000:]}")
    chunk_jobs = 0
    chunk_leaves = 0
    chunk_nodes = 0
    for line in run.stdout.splitlines():
        total_lines += 1
        if "FAILED" in line or line.startswith("ERROR"):
            raise RuntimeError(line)
        s = line.split()
        if not s:
            continue
        if s[0] == "JOB":
            j = int(s[1])
            if s[2] != "PROVED" or j in jobs or not first <= j < last:
                raise ValueError(f"bad job record: {line}")
            jobs.add(j)
            chunk_jobs += 1
        elif s[0] == "LEAF":
            z, al, ah, ad, rl, rh, rd = map(int, s[1:8])
            if s[8] != "nodes":
                raise ValueError(f"bad leaf record: {line}")
            nodes = int(s[9])
            l, h, r, t = F(al, ad), F(ah, ad), F(rl, rd), F(rh, rd)
            if not (F(21, 1000) <= l < h <= F(3, 125)):
                raise ValueError(f"bad bias leaf: {line}")
            if not (F(1, 3) <= r < t <= F(1009, 3000)):
                raise ValueError(f"bad density leaf: {line}")
            leaves[z].append((l, h, r, t))
            total_nodes += nodes
            chunk_nodes += nodes
            chunk_leaves += 1
    if chunk_jobs != 256:
        raise ValueError(f"chunk {first}:{last} has {chunk_jobs} job records")
    print(f"CHUNK {first} {last} jobs {chunk_jobs} leaves {chunk_leaves} successful_leaf_nodes {chunk_nodes}")

if jobs != set(range(1536)):
    raise ValueError("incomplete global job coverage")

for z, rects in leaves.items():
    xs = sorted({F(21, 1000), F(3, 125)} | {x for q in rects for x in q[:2]})
    ys = sorted({F(1, 3), F(1009, 3000)} | {y for q in rects for y in q[2:]})
    for x0, x1 in zip(xs, xs[1:]):
        for y0, y1 in zip(ys, ys[1:]):
            x, y = (x0 + x1) / 2, (y0 + y1) / 2
            count = sum(l < x < h and r < y < t for l, h, r, t in rects)
            if count != 1:
                raise ValueError((z, x, y, count))

print(f"COVERAGE PROVED jobs {len(jobs)} words {len(leaves)} leaves {sum(map(len, leaves.values()))}")
print(f"COMPLETED_LEAF_NODES {total_nodes}")
print("All 256 word rectangles exactly cover [21/1000,3/125] x [1/3,1009/3000].")
