# Parameter benchmark and certified continuation ceilings

## Benchmark slab

All new estimates concern

```text
c0 = 37/40 = 0.925
c* = 463/500 = 0.926
c* - c0 = 1/1000.
```

The legal shift interval at contrast `c` is `0 <= a <= 1-c`.  A centered strip
has the form

```text
J(c,w) = { a : |a-(1-c)/2| <= w }
```

and is nonempty only when `0 <= w <= (1-c)/2`.

No positive new entropy-curvature region is claimed.  Instead, this file records
exact upper ceilings on the contrast width reachable by two specified
certificate families.

## Reviewed margin ledger

The reviewed base theorem supplies

```text
F_d'' <= -1/50          for d <= c0.
```

To finish with `F_c'' <= -1/200`, the total response budget is

```text
1/50 - 1/200 = 3/200.
```

To retain sign only, the budget is `1/50`.

## Family A: differentiated split-tail certificate

The exact cover proves that every legal profile in the family has

```text
R(d,c) > C_split (c-d),
C_split = 366368000000/1323
        ~= 276922146.6364.
```

This statement already gives the family:

- the largest possible shift-domain length in the slab, `3/40`;
- the best possible Bernstein parameter `sigma=1`, corresponding to a
  zero-width inner target;
- arbitrary spectral gap and threshold-admissible cutoff;
- a fresh optimizer at every step; and
- deletion of every positive tail term except the unavoidable head-value term.

Exact total-width ceilings are

```text
strong final margin 1/200:
  (3/200)/C_split = 3969/73273600000000
                   ~= 5.4166848633e-11

sign only:
  (1/50)/C_split = 1323/18318400000000
                  ~= 7.2222464844e-11.
```

A nonzero target strip has `sigma<1` and can only worsen these ceilings.

## Family B: uniform mode-separable certificate

For `n=2, Q=diag(1,0)`, exact mode-two response gives, uniformly over every
legal shift and every common gap,

```text
(u_{c,2}-u_{d,2})'' >= C2 (c-d),
C2 = 4177920000/47458321
   ~= 88.0334557137.
```

Consequently any certificate that pays nonnegative mode budgets separately has
ceilings

```text
strong final margin 1/200:
  (3/200)/C2 = 47458321/278528000000
             ~= 0.0001703898

sign only:
  (1/50)/C2 = 47458321/208896000000
            ~= 0.0002271864.
```

Both are strictly below the benchmark width `0.001`.  This obstruction is
independent of cutoff choice and applies pointwise, so adaptive strip placement
cannot evade it.

## Legal strip inclusion

If a theorem at `d` is known on `J(d,w_d)` and the next theorem is targeted on
`J(c,w_c)`, then the target must lie inside the old domain:

```text
w_c + (c-d)/2 <= w_d.
```

Thus a chain ending at `c*` loses at least `(c*-c0)/2=1/2000` of centered-strip
half-width before any analytic buffer is charged.  Neither obstruction relies
on this additional loss.

## Exact unpaid estimate at c*=0.926

The benchmark jump has response budget `3/200`, i.e. average budget `15` per
unit contrast.  Mode two alone costs at least `C2`.  A successful signed
argument must therefore recover at least

```text
C2 - 15 = 3466045185/47458321
        ~= 73.0334557137
```

per contrast unit through cross-mode cancellation or a same-witness excess
base margin.  This is the exact outstanding estimate; no claimed region is
hidden behind it.
