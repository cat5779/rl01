"""Complete-atom floating quadrature; diagnostic only, NOT a certificate."""
from __future__ import annotations
import argparse
import datetime as dt
import json
from pathlib import Path
import numpy as np
from probe_full_radius import evaluate


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--radii',nargs='+',type=int,default=[3,5,7])
    ap.add_argument('--nodes',type=int,default=16)
    args=ap.parse_args()
    start=dt.datetime.now(dt.timezone.utc).isoformat()
    z,w=np.polynomial.legendre.leggauss(args.nodes)
    rows=[]
    for r in args.radii:
        lo=1/(r+1)
        u=(1-lo)*(z+1)/2+lo
        weights=w*(1-lo)/(2*u)
        layers=np.zeros(2*r+1); max_jet_error=0.
        for ui,wi in zip(u,weights):
            q=evaluate(r,.95,0.,float(ui))
            layers += wi*np.array(q['layer_I_d2'])
            max_jet_error=max(max_jet_error,abs(q['mass']-1),abs(q['mass_d1']),abs(q['mass_d2']))
        band=np.abs(np.arange(2*r+1)-r)<=.5*np.sqrt(r)
        row=dict(R=r,nodes=args.nodes,band_counts=np.arange(2*r+1)[band].tolist(),
                 full_d2=float(layers.sum()),band_d2=float(layers[band].sum()),
                 complement_d2=float(layers[~band].sum()),
                 band_d2_div_R=float(layers[band].sum()/r),
                 complement_d2_div_R=float(layers[~band].sum()/r),
                 max_mass_jet_error=max_jet_error)
        rows.append(row); print(row,flush=True)
    result=dict(status='FLOATING_DIAGNOSTIC_NOT_PROOF',started_utc=start,
                ended_utc=dt.datetime.now(dt.timezone.utc).isoformat(),rows=rows)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
