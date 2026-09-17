# Independent review of `check_seed.py`

## Verdict

**STATUS: CORRECT.**

I found no critical gap in the frozen finite claims.  The script certifies,
with outward rational intervals, the strict bounds

\[
\frac{37}{100000}<E g_{1,6}<\frac{39}{100000},\qquad
-50<H_6''<-49
\]

for the true six-site half-density sine-Toeplitz block at
`c=19/20`, `a=1/40`.  It also checks the complete Shannon diagonal-plus-pair
identity and a nontrivial moving-count second-difference identity.  These are
finite statements only; the checker itself correctly disclaims entropy-rate
concavity.

Reviewed source:
`research_prompts/pro_tasks/checks/check_seed.py`.

Generated receipt:
`research_prompts/pro_tasks/checks/seed_results.json`.

## Execution

I ran the script with the bundled Python 3 runtime.  It exited with code zero
and printed

```text
status: PASS
pair: 0.000379092242041686
H_second: -49.56552123925096
moving_count_identity: true
```

The saved rational intervals are much narrower than the asserted margins:

- `E g_(1,6)` is enclosed near
  `0.000379092242041686013263273641316797`;
- `H_6''` is enclosed near
  `-49.565521239250963197596195443319`;
- the diagonal-plus-pair residual is enclosed in approximately
  `[-5.15e-31, 4.61e-31]`.

## Outward interval audit

The rational interval implementation is sound for every operation used.

1. `floorq` uses Python integer floor division, including for negative
   numerators.  `ceilq(x)=-floorq(-x)` therefore rounds in the correct
   direction.  Addition, subtraction, multiplication, and inversion round
   their lower endpoint down and upper endpoint up.  Every divisor used in the
   accepted run is separated from zero.
2. The Machin formula

   \[
   \pi=16\arctan(1/5)-4\arctan(1/239)
   \]

   is enclosed by adjacent alternating-series partial sums.  Both arguments
   lie in `(0,1)`, so the alternating remainder rule applies with the direction
   used at lines 80--83.
3. For `1<=u<=2`, the logarithm routine uses

   \[
   \log u=2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1},\qquad
   z=\frac{u-1}{u+1}\in[0,1/3].
   \]

   After 32 included terms the first omitted power is `z^65`.  The bound

   \[
   2\frac{z^{65}}{65(1-z^2)}
   \]

   dominates the positive tail because all later denominators are at least
   65.  Range reduction by powers of two is exact, and monotonicity justifies
   evaluating the lower and upper endpoints separately in `log_interval`.
4. The forty-decimal rational grid widens every intermediate interval.  There
   is no conversion to binary floating point in any certified comparison;
   floats appear only in the human-readable `approx_midpoint` field.

## All-atom and normalization audit

At the frozen parameters,

\[
K_{ii}=a+c/2=1/2,
\qquad
K_{ij}=\frac{c\sin(\pi(i-j)/2)}{\pi(i-j)}\quad(i\ne j).
\]

For a word `y`, the code expands

\[
p_y=(-1)^{6-|y|}\det(K-\operatorname{diag}(1-y))
\]

over all 720 permutations.  Even nonzero lags vanish, odd-lag signs agree with
`sin(pi r/2)`, and the remaining powers are even.  Hence each of the 64 atom
probabilities is an exact rational cubic polynomial in
`t=(c/pi)^2`.  The coefficient-wise sum is checked to be exactly
`(1,0,0,0)`, which proves normalization for every `t`, not only the chosen
one.  All 64 evaluated lower bounds are strictly positive before a logarithm
or reciprocal is taken.

I independently rebuilt every event matrix and evaluated its determinant
directly at 80-decimal precision, without using the checker's polynomial
coefficient table.  This gave

```text
sum p_y  = 1 (to 79 decimal places)
min p_y  = 0.0002026089871463685401450561560272215...
sum p_y' = 4.1e-80
sum p_y''= -4.6e-79
```

The tiny derivative sums are decimal roundoff; the checker's exact polynomial
normalization makes them identically zero.

The bit-flip jet formulas at lines 129--133 are also correct.  If
`s_i(y)=2y_i-1`, multilinearity of the determinant in its diagonal gives

\[
p_y'=\sum_i s_i(y)[p_y+p_{y\oplus i}],
\]

\[
p_y''=2\sum_{i<j}s_i(y)s_j(y)
[p_y+p_{y\oplus i}+p_{y\oplus j}+p_{y\oplus i\oplus j}].
\]

Thus all acceleration terms used in the Shannon Hessian are present.

## Shannon Hessian and face decomposition

The direct quantity at line 134 is exactly

\[
H_6''=-\sum_y p_y''\log p_y-\sum_y\frac{(p_y')^2}{p_y}.
\]

For a Boolean two-face with masses `(A,B,C,D)` and total mass
`m=A+B+C+D`, the code uses

\[
g_{ij}=m\log\frac{BC}{AD}
-(BC-AD)\left(\frac1A+\frac1B+\frac1C+\frac1D\right).
\]

It sums every one of the 16 faces for each pair, and `pair(0,5)` is precisely
the labelled pair `(1,6)`.  The diagonal term is

\[
-\sum_i\sum_{y:y_i=0}
\frac{(p_y+p_{y\oplus i})^3}{p_y p_{y\oplus i}}.
\]

The complete identity checked at lines 145--159 is therefore

\[
H_6''=\text{diagonal}+2\sum_{1\le i<j\le6}E g_{ij}.
\]

My independent direct-determinant recomputation obtained

```text
E g_(1,6) = 0.0003790922420416860132632736413167970483...
H_6''      = -49.5655212392509631975961954433188966660...
diagonal   = -39.4593623822310238234550978916349190783...
pair part  = -10.1061588570199393741410975516839775877...
residual   = 1.0e-77
```

These values lie inside the saved outward intervals and independently confirm
both strict target inequalities and the decomposition sign conventions.

## Moving-count identity

For the four affine Bernoulli probabilities
`b_i(a)=a+c lambda_i`, the probability-generating polynomial is multilinear.
For an arbitrary moving test array `f_a(m)`, conditioning after deleting one
or two bits gives the universal identity

\[
\begin{aligned}
\frac{d^2}{da^2}E f_a(M)
={}&E\,\partial_a^2 f_a(M)
+2\sum_i E\,\Delta(\partial_a f_a)(N_i)\\
&+\sum_{i\ne j}E\,\Delta^2f_a(N_{ij}).
\end{aligned}
\]

Lines 185--191 differentiate the count polynomial directly and lines
197--202 implement the right side with ordered pairs.  The chosen function has
nonzero value, first-derivative, and second-derivative parts, so the runtime
test is not a degenerate cancellation.  Both exact rational evaluations equal

\[
356589/2500.
\]

For an additional independence check, I tested the coordinate basis for each
of the five possible value arrays and each of the five first-derivative arrays.
Every basis identity passed exactly, with
`sum pi=1`, `sum pi'=0`, and `sum pi''=0`.  By linearity this covers arbitrary
four-bit moving test arrays.  The count product is legitimate here because a
DPP count has the Poisson-binomial law of its eigenvalues; the code does not
replace the configuration law by a product law.

## Scope retained

The certificate proves one finite true-law obstruction and an exact layer
bookkeeping interface.  It does not prove a growing-`n` sign, entropy-rate
concavity, a true-versus-corrected bridge, or a sign for the spatial KL layer
function.  The source and receipt state this limitation accurately.
