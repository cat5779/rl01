"""Restore the independently rebuilt cover; no network or third-party packages."""
from pathlib import Path
import argparse,base64,gzip,hashlib,json
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
root=Path(__file__).resolve().parent
binding=json.loads((root/'cover_binding.json').read_text(encoding='utf-8'))
packed=base64.b64decode((root/'full_r3_highcontrast.json.gz.b64').read_text(encoding='ascii'),validate=False)
if hashlib.sha256(packed).hexdigest()!=binding['gzip_sha256']:raise SystemExit('Compressed hash mismatch')
raw=gzip.decompress(packed)
if hashlib.sha256(raw).hexdigest()!=binding['raw_sha256']:raise SystemExit('Cover hash mismatch')
cover=json.loads(raw)
if cover['summary']['leaves']!=2922 or cover['summary']['pending']!=0:raise SystemExit('Incomplete/wrong cover')
a.output.parent.mkdir(parents=True,exist_ok=True)
with a.output.open('xb') as f:f.write(raw)
print('PASS_RESTORED_INDEPENDENT_COVER',binding['raw_sha256'])
