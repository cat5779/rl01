"""Small finite DPP diagnostic. Floating point is a probe, not a proof."""
from pathlib import Path
import json, math, time
import numpy as np

OUT = Path(__file__).resolve().parent
RNG = np.random.default_rng(761205)

def upsets(n):
    if n == 0:
        return [0, 1]
    old = upsets(n - 1)
    half = 1 << (n - 1)
    return [a | (b << half) for a in old for b in old if a & ~b == 0]

def law(q):
    n = q.shape[0]
    inc = np.ones(1 << n)
    for mask in range(1, 1 << n):
        ix = [i for i in range(n) if mask >> i & 1]
        inc[mask] = np.linalg.det(q[np.ix_(ix, ix)]).real
    prob = inc.copy()
    for i in range(n):
        for mask in range(1 << n):
            if not mask >> i & 1:
                prob[mask] -= prob[mask | (1 << i)]
    return inc, prob

def maxflow(qprob, p, n):
    """Maximum monotone coupling mass with unnormalized residual edges."""
    m = 1 << n
    adj = [[] for _ in range(2*m+2)]
    src, sink = 2*m, 2*m+1
    def edge(x, y, cap):
        adj[x].append([y, float(cap), len(adj[y])])
        adj[y].append([x, 0., len(adj[x])-1])
    for x in range(m):
        k = x.bit_count()
        edge(src, x, p**k * (1-p)**(n-k))
        edge(m+x, sink, max(0., qprob[x]))
        for y in range(m):
            if x & ~y == 0:
                edge(x, m+y, 2.)
    flow = 0.
    while True:
        levels = [-1]*len(adj)
        levels[src] = 0
        queue = [src]
        for x in queue:
            for y, cap, rev in adj[x]:
                if cap > 1e-14 and levels[y] < 0:
                    levels[y] = levels[x]+1
                    queue.append(y)
        if levels[sink] < 0:
            break
        ptr = [0]*len(adj)
        def send(x, f):
            if x == sink: return f
            while ptr[x] < len(adj[x]):
                e = adj[x][ptr[x]]
                y, cap, rev = e
                if cap > 1e-14 and levels[y] == levels[x]+1:
                    sent = send(y, min(f, cap))
                    if sent > 1e-14:
                        e[1] -= sent
                        adj[y][rev][1] += sent
                        return sent
                ptr[x] += 1
            return 0.
        while True:
            f = send(src, 2.)
            if f <= 1e-14: break
            flow += f
    return flow

def sample(n, j):
    if j % 4 == 0:
        x = RNG.integers(-4, 5, size=(n,n)).astype(float)
        r = x@x.T + np.eye(n)
        q = r/(np.linalg.eigvalsh(r)[-1]+1)
    else:
        z = RNG.normal(size=(n,n))
        if j % 4 == 2: z = z + 1j*RNG.normal(size=(n,n))
        u, _ = np.linalg.qr(z)
        vals = RNG.uniform(.001,.999,n)
        q = (u*vals)@u.conj().T
    return q

records=[]
start=time.time()
for n in range(1,6):
    ups=upsets(n)
    m=1<<n
    mat=np.array([[(u>>j)&1 for j in range(m)] for u in ups],dtype=float)
    sizes=np.array([j.bit_count() for j in range(m)])
    for j in range(100):
        q=sample(n,j)
        inc, prob=law(q)
        powers=np.array([mask.bit_count() for mask in range(1,m)])
        delta=float(np.min(np.maximum(inc[1:],0)**(1/powers)))
        ber=delta**sizes*(1-delta)**(n-sizes)
        gaps=mat@(prob-ber)
        k=int(np.argmin(gaps))
        mingap=float(gaps[k])
        flow=maxflow(prob,delta,n)
        low,high=0.,delta
        if mingap < -1e-10:
            target=mat@prob
            for _ in range(42):
                mid=(low+high)/2
                if np.min(target-mat@(mid**sizes*(1-mid)**(n-sizes))) >= -1e-13:
                    low=mid
                else: high=mid
        else: low=high=delta
        r=dict(n=n,index=j,delta=delta,pminus_interval=[low,high],gap=delta-low,
               min_upset_gap=mingap,flow_at_delta=flow,prob_min=float(prob.min()),
               mass_error=float(abs(prob.sum()-1)),upsets=len(ups))
        if mingap < -1e-10:
            r.update(qreal=q.real.tolist(),qimag=q.imag.tolist(),witness_upset=ups[k],
                     witness_states=[x for x in range(m) if ups[k]>>x&1])
        records.append(r)
    print('n',n,'tested',100,'strict_gaps',sum(r['n']==n and r['gap']>1e-8 for r in records),flush=True)
out=dict(seed=761205,method='all upward-closed events; independent monotone max-flow at delta; 42 bisection iterations for violations',
         status='NUMERICAL_PROBE_NOT_PROOF',numpy=np.__version__,seconds=time.time()-start,records=records)
(OUT/'finite01.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('TOTAL',len(records),'largest_gap',max(r['gap'] for r in records), 'seconds',out['seconds'])
