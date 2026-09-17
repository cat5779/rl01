#!/usr/bin/env python3
"""Check that load-bearing exact constants in Markdown match frozen JSON."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AUTHOR=ROOT/'author'
data=json.loads((ROOT/'receipts/obstruction.json').read_text(encoding='utf-8'))
texts={p.name:p.read_text(encoding='utf-8') for p in [AUTHOR/'proof.md',AUTHOR/'README.md',AUTHOR/'PARAMETER_REGION.md',AUTHOR/'gap_audit.md']}
alltext='\n'.join(texts.values())
# Normalize simple LaTeX rational displays to a/b for comparison with JSON.
alltext=re.sub(r"-?\\frac\{([0-9]+)\}\{([0-9]+)\}",
               lambda m: ("-" if m.group(0).startswith("-") else "")+m.group(1)+"/"+m.group(2),
               alltext)
assert data['source_commit'] in (AUTHOR/'IMPORTED_INPUTS.md').read_text(encoding='utf-8')
keys=[
 data['split_tail_adaptive_family']['minimum_coefficient'],
 data['split_tail_adaptive_family']['strong_margin_width_ceiling'],
 data['uniform_mode_separable_family']['whole_legal_shift_coefficient_floor'],
 data['uniform_mode_separable_family']['whole_shift_payment_for_c0_to_c_star'],
 data['uniform_mode_separable_family']['base_full_curvature_at_witness'],
 data['uniform_mode_separable_family']['target_full_curvature_at_witness'],
 data['uniform_mode_separable_family']['full_entropy_center_response'],
 data['uniform_mode_separable_family']['signed_group_m2_response'],
 data['uniform_mode_separable_family']['signed_group_modes_m_ge_3_response'],
]
missing=[x for x in keys if x not in alltext]
assert not missing, missing
assert texts['proof.md'].splitlines()[0]=='DISPROVED_ROUTE_LEMMA'
assert texts['README.md'].splitlines()[0]=='DISPROVED_ROUTE_LEMMA'
print('DOCUMENT_CONSTANTS_MATCH_FROZEN_CERTIFICATE')
