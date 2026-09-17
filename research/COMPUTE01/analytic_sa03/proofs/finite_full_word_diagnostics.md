# Finite full-word diagnostics

**Status: FINITE COMPUTATION / NOT AN ASYMPTOTIC PROOF**

For every quadrature node, all `2^(2R)` physical exterior words were
enumerated with their determinantal probabilities.  The four columns below
are the integrated residual pieces; `baseline=4(1-(R+1)^-2)`.

| R | baseline | curvature | Bregman phi-prime | parameter derivative | signed transport | total A_R'' |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3.000000 | 0.045284 | 0.002159 | 0.046985 | -0.022407 | 3.072021 |
| 3 | 3.750000 | 0.277426 | 0.038545 | 0.399047 | -0.197562 | 4.267455 |
| 5 | 3.888889 | 0.488060 | 0.097244 | 0.818502 | -0.395802 | 4.896893 |
| 7 | 3.937500 | 0.661465 | 0.161312 | 1.234137 | -0.585085 | 5.409329 |
| 9 | 3.960000 | 0.805635 | 0.224454 | 1.628644 | -0.760619 | 5.858114 |

The `R=1` integrand agrees with the independent symbolic formula to less than
`2e-10` at every node.  The sign message is not componentwise: transport is
negative and increasingly costly, while the parameter-derivative block is
the largest positive correction.

At `R=9,u=1`, exhaustive enumeration also supplies a counterexample to
wordwise positivity.  The average normalized kernel is `29.1338266712`, but
the word `001010011001101011` has value `-1.9552822249`.  Thus only an
expectation-level compensation route survives.
