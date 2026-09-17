#!/usr/bin/env python3
"""Replay the exact certificate and the optional deterministic diagnostics.

This script never overwrites frozen evidence.  Exact proof fields are compared
as parsed JSON after removing explicitly diagnostic floating-point fields.
"""
from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run_script(script: Path, output: Path) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        [PYTHON, str(script), "--output", str(output)],
        check=True,
        text=True,
        capture_output=True,
        env=env,
    )


def without_float_diagnostics(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            k: without_float_diagnostics(v)
            for k, v in value.items()
            if "float" not in k.lower()
        }
    if isinstance(value, list):
        return [without_float_diagnostics(v) for v in value]
    return value


def assert_finite_tree(value: Any) -> None:
    if isinstance(value, dict):
        for v in value.values():
            assert_finite_tree(v)
    elif isinstance(value, list):
        for v in value:
            assert_finite_tree(v)
    elif isinstance(value, float):
        if not math.isfinite(value):
            raise AssertionError(f"non-finite floating diagnostic: {value!r}")


def compare_floating(replayed: dict[str, Any], frozen: dict[str, Any]) -> None:
    if replayed["schema"] != frozen["schema"]:
        raise AssertionError("floating schema mismatch")
    if replayed["warning"] != frozen["warning"]:
        raise AssertionError("floating warning mismatch")
    if replayed["benchmark_c"] != frozen["benchmark_c"]:
        raise AssertionError("floating benchmark mismatch")

    rr = replayed["toeplitz_half_density"]
    fr = frozen["toeplitz_half_density"]
    if len(rr) != len(fr):
        raise AssertionError("Toeplitz row-count mismatch")
    for got, want in zip(rr, fr, strict=True):
        if (got["n"], got["s"]) != (want["n"], want["s"]):
            raise AssertionError("Toeplitz index mismatch")
        if not math.isclose(
            got["tc_second"], want["tc_second"], rel_tol=2e-11, abs_tol=2e-11
        ):
            raise AssertionError(f"Toeplitz diagnostic mismatch: {got} != {want}")

    gr = replayed["seeded_random_contractions"]
    gw = frozen["seeded_random_contractions"]
    for key in ("seed", "arg_n_trial_s", "samples"):
        if gr[key] != gw[key]:
            raise AssertionError(f"random diagnostic field mismatch: {key}")
    if not math.isclose(
        gr["minimum_tc_second"],
        gw["minimum_tc_second"],
        rel_tol=1e-7,
        abs_tol=2e-11,
    ):
        raise AssertionError("random diagnostic minimum mismatch")
    assert_finite_tree(replayed)


def main() -> int:
    frozen_exact = json.loads(
        (ROOT / "evidence" / "exact_route_certificate.json").read_text(encoding="utf-8")
    )
    if frozen_exact.get("status") != "DISPROVED_ROUTE_LEMMA":
        raise AssertionError("unexpected exact certificate status")

    with tempfile.TemporaryDirectory(prefix="s12-replay-") as td:
        temp = Path(td)
        exact_out = temp / "exact.json"
        run_script(ROOT / "code" / "exact_route_certificate.py", exact_out)
        replayed_exact = json.loads(exact_out.read_text(encoding="utf-8"))
        if without_float_diagnostics(replayed_exact) != without_float_diagnostics(frozen_exact):
            raise AssertionError("exact parsed certificate mismatch")

        print("PASS exact certificate: all rational identities and inequalities replayed")

        try:
            import numpy  # noqa: F401
        except ImportError:
            print("SKIP floating diagnostics: NumPy is not installed (not proof evidence)")
        else:
            floating_out = temp / "floating.json"
            run_script(ROOT / "code" / "floating_diagnostics.py", floating_out)
            replayed_floating = json.loads(floating_out.read_text(encoding="utf-8"))
            frozen_floating = json.loads(
                (ROOT / "evidence" / "floating_diagnostics.json").read_text(
                    encoding="utf-8"
                )
            )
            compare_floating(replayed_floating, frozen_floating)
            print("PASS floating diagnostics: deterministic replay within stated tolerance")

    print("PASS verify_all")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
