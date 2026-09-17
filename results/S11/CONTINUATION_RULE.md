# Legal continuation rule and why subdivision does not repair these families

Let

```text
F_c(a) = H(DPP(a I + c Q))/n.
```

Suppose at contrast `d` one has the certified uniform bound

```text
F_d''(a) <= -m_d < 0       for a in J_d.
```

A response certificate for a step `d -> c` is a number `R(d,c)>=0` satisfying

```text
F_c''(a)-F_d''(a) <= R(d,c)     for a in J_c,
```

where `J_c` is contained in the domain on which the previous theorem and every
auxiliary expansion are valid.  The only legal update is

```text
m_c = m_d - R(d,c).
```

The base margin may not be reset after a step.

## Centered strips

For centered strips

```text
J_d = [(1-d)/2-w_d, (1-d)/2+w_d],
J_c = [(1-c)/2-w_c, (1-c)/2+w_c],
```

inclusion `J_c subset J_d` is equivalent to

```text
w_c + (c-d)/2 <= w_d.
```

A chain `c0=d0<d1<...<dk` therefore satisfies

```text
w_k + (d_k-c0)/2 <= w_0.
```

Any spectral-gap or outer-interval requirements must be intersected with these
nested domains as well.

## Margin across a chain

For a chain, repeated legal updating yields exactly

```text
m_k = m_0 - sum_j R(d_{j-1},d_j).
```

For Family A, the exact cover proves

```text
R(d,c) > C_split (c-d)
```

for every legal profile, even when each step chooses a fresh optimizer.  Hence

```text
sum_j R(d_{j-1},d_j)
  > C_split sum_j(d_j-d_{j-1})
  = C_split(d_k-c0).
```

Subdividing cannot reduce this lower bound.  This is stronger than the earlier
observation that a single frozen additive formula is exactly additive: it
allows arbitrary reoptimization at every step.

For Family B, the actual mode-two response on one fixed contraction obeys

```text
(u_{d_j,2}-u_{d_{j-1},2})'' >= C2(d_j-d_{j-1})
```

at every legal target point.  Nonnegative mode-separable bookkeeping must pay
at least this amount, so the same telescoping lower bound applies independently
of the gap, cutoff, and strip.

## What can escape

The argument does not obstruct a signed block estimate of the form

```text
sum_{m in B} (u_{c,m}-u_{d,m})'' <= small payment
```

because positive and negative modes can then cancel before a nonnegative charge
is assigned.  It also does not obstruct a response bound whose allowed payment
is coupled to excess negative curvature of the same `Q` at the base contrast.
Those are genuinely different continuation rules, not subdivisions of the
families disproved here.
