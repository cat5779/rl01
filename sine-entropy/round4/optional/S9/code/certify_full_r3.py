#!/usr/bin/env python3
"""Adaptive exact cover of full R=3 production curvature on the whole channel.
Targets I_delta_delta/u^2 >= 6 on [0,1] x [0,1/100]. The scaled jets have
polynomial extensions at u=0; no division by u or dropped probability terms.
Checkpoints retain every split/failure and never certify a partial cover.
"""
from __future__ import annotations
import argparse,json,time,hashlib
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from atom_polynomials import build,POSITIONS,DEN,N,center_curvature
from dyadic import IV,horner,SCALE,BITS,TERMS


def need(x,msg):
    if not x:raise ArithmeticError(msg)


def scaled_coefficients(C,delta):
    ans=[]
    for row in C:
        by=[[IV.point(0)for _ in range(N+1)]for _ in range(3)]
        for j in range(3):
            for k in range(j,N+1):
                coeff=[Q(0)]*(N+1)
                for v,(kk,l) in zip(row,POSITIONS):
                    if kk==k and l>=j:
                        coeff[l-j]=Q(v*(1 if j==0 else l if j==1 else l*(l-1)),DEN)
                by[j][k-j]=horner(coeff,delta)
        ans.append(by)
    return ans


@lru_cache(maxsize=4096)
def cached_coefficients(d0,d1):
    return scaled_coefficients(build(),IV.bounds(Q(d0),Q(d1)))


def bound(C,box):
    u0,u1,d0,d1=map(Q,box);u=IV.bounds(u0,u1);delta=IV.bounds(d0,d1)
    coeffs=cached_coefficients(box[2],box[3])
    jets=[[horner(co,u)for co in row]for row in coeffs]
    lower=min(row[0].lo for row in jets)
    if lower<=0:return {'positive':False,'min_atom_lower':str(Q(lower,SCALE))}
    ls,F,A=center_curvature(jets);total=sum(ls)
    return {'positive':True,'min_atom_lower':str(Q(lower,SCALE)),
            'scaled_curvature':total.rational(),'scaled_Fisher':F.rational(),
            'scaled_acceleration':A.rational(),'proved':Q(total.lo,SCALE)>=6}


def initial(profile='narrow'):
    need(profile in ('narrow','highcontrast'),'unknown certificate profile')
    uhi,dhi=('1','1/100') if profile=='narrow' else ('21/20','1/24')
    return {'schema':1,'classification':'PARTIAL_COVER_NOT_A_CERTIFICATE',
            'profile':profile,'R':3,'c':'5*pi/16','u_domain':['0',uhi],'delta_domain':['0',dhi],
            'target_scaled_curvature_lower':'6','bits':BITS,'log_terms':TERMS,
            'denominator':str(DEN),'positions':POSITIONS,
            'atom_polynomials':[[str(z)for z in row]for row in build()],
            'nodes':{},'pending':[{'path':'','box':['0',uhi,'0',dhi]}],
            'execution_chunks':[]}


def validate_structure(s,complete=False):
    expected=initial(s.get('profile','narrow'))
    for k in ['schema','R','c','u_domain','delta_domain','target_scaled_curvature_lower','bits','log_terms','denominator','positions','atom_polynomials']:
        # Positions are tuples in fresh Python but lists in persisted JSON.
        need(json.dumps(s[k])==json.dumps(expected[k]),'input mismatch: '+k)
    pending={p['path']:p['box']for p in s['pending']}
    need(len(pending)==len(s['pending']),'duplicate pending box')
    seen=set()
    def visit(path,box):
        need(path not in seen,'duplicate cover path');seen.add(path)
        if path in pending:
            need(path not in s['nodes'] and pending[path]==box,'pending box differs from cover');return
        need(path in s['nodes'],'missing cover node')
        node=s['nodes'][path];need(node['box']==box,'wrong node box')
        if node['kind']=='leaf':
            need(node['bound']['positive'] and Q(node['bound']['min_atom_lower'])>0,'leaf positivity')
            need(Q(node['bound']['scaled_curvature'][0])>=6,'leaf target')
            return
        need(node['kind']=='split' and node['axis']in ['u','delta'],'invalid cover split')
        vals=list(map(Q,box));i=0 if node['axis']=='u' else 2;mid=(vals[i]+vals[i+1])/2
        left=vals[:];right=vals[:];left[i+1]=mid;right[i]=mid
        visit(path+'0',list(map(str,left)));visit(path+'1',list(map(str,right)))
    visit('',s['u_domain']+s['delta_domain'])
    need(seen==set(s['nodes'])|set(pending),'unreachable cover records')
    if complete:need(not pending,'cover is incomplete')


def run(state,max_nodes):
    validate_structure(state);C=build();start=time.time();before=len(state['nodes'])
    for _ in range(max_nodes):
        if not state['pending']:break
        item=state['pending'].pop();path=item['path'];box=item['box'];z=bound(C,box)
        if z.get('proved'):
            state['nodes'][path]={'kind':'leaf','box':box,'bound':z}
        else:
            vals=list(map(Q,box));u0,u1,d0,d1=vals
            axis='u' if (u1-u0)*(Q(5,12)+d1)>=u1*(d1-d0) else 'delta'
            i=0 if axis=='u' else 2;mid=(vals[i]+vals[i+1])/2
            left=vals[:];right=vals[:];left[i+1]=mid;right[i]=mid
            state['nodes'][path]={'kind':'split','axis':axis,'box':box,'bound':z}
            state['pending'].extend([{'path':path+'1','box':list(map(str,right))},{'path':path+'0','box':list(map(str,left))}])
        if len(state['nodes'])>30000:break
    state['execution_chunks'].append({'new_nodes':len(state['nodes'])-before,'elapsed_seconds':time.time()-start})
    validate_structure(state)
    leaves=[n for n in state['nodes'].values()if n['kind']=='leaf']
    state['summary']={'nodes':len(state['nodes']),'leaves':len(leaves),'pending':len(state['pending']),
        'minimum_scaled_curvature_lower':str(min(Q(n['bound']['scaled_curvature'][0])for n in leaves))if leaves else None}
    if not state['pending']:
        state['classification']='AUTHOR_FULL_R3_PRODUCTION_CONVEXITY_CERTIFICATE_NOT_RATE';validate_structure(state,True)
    return state


def replay_leaves(state,begin,end):
    validate_structure(state,True);leaves=sorted(k for k,v in state['nodes'].items()if v['kind']=='leaf')
    if end is None:end=len(leaves)
    need(0<=begin<end<=len(leaves),'invalid replay range')
    C=build();start=time.time()
    for path in leaves[begin:end]:
        node=state['nodes'][path]
        need(bound(C,node['box'])==node['bound'],'fresh outward leaf mismatch: '+path)
    return {'status':'PASS_FRESH_FULL_R3_LEAVES','profile':state.get('profile','narrow'),
            'begin_leaf':begin,'end_leaf':end,'total_leaves':len(leaves),
            'elapsed_seconds':time.time()-start,
            'scope':'Same-author fresh arithmetic replay; no entropy-rate sign or independent review.'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--state',type=Path,required=True);p.add_argument('--max-nodes',type=int,default=256)
    p.add_argument('--profile',choices=['narrow','highcontrast'],default='narrow');p.add_argument('--fresh',action='store_true');p.add_argument('--check-structure',action='store_true')
    p.add_argument('--replay',action='store_true');p.add_argument('--begin-leaf',type=int,default=0);p.add_argument('--end-leaf',type=int);p.add_argument('--receipt',type=Path)
    a=p.parse_args()
    s=initial(a.profile) if a.fresh or not a.state.exists() else json.loads(a.state.read_text())
    if a.replay:
        r=replay_leaves(s,a.begin_leaf,a.end_leaf)
        r['certificate_sha256']=hashlib.sha256(a.state.read_bytes()).hexdigest()
        if a.receipt:a.receipt.write_text(json.dumps(r,indent=2)+'\n')
        print(r);raise SystemExit
    if a.check_structure:
        validate_structure(s,True);print('PASS_COMPLETE_COVER_STRUCTURE');raise SystemExit
    s=run(s,a.max_nodes);a.state.write_text(json.dumps(s,indent=2)+'\n')
    print(s['classification'],s['summary'],s['execution_chunks'][-1],flush=True)
