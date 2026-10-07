# Prompt for Euler

Work on the two frozen mathematical problems in `research/ln01/TASK.md`.
Read `research/ln01/EVIDENCE.md` and then read every cited RL01 file in full,
especially the theorem, proof, and both reviews in `research/q77r05/g4/`.
Check the cited primary sources rather than relying on the project summaries.

Problem A asks for full `Aut(G)` equivariance for every countable connected
locally finite vertex-transitive graph and every `Aut(G)`-invariant DPP kernel.
The existing theorem covers arbitrary actions of countable groups, but
`Aut(G)` may be uncountable.  First determine whether the existing Brownian
observation / posterior-drift construction is already canonical under every
permutation preserving `Q`, or whether its finite exhaustions or exceptional
sets depend essentially on a countable acting group.  A proof must produce
full automorphism equivariance; choosing a countable transitive subgroup is
not a solution.  If the assertion is false, give an explicit graph, kernel,
and stabilizer obstruction or other rigorous counterexample.

Problem B is exactly Lyons--Thom Question 7.6 in the invariant `bar-d` metric.
Do not reuse the weak-star nonclosure counterexample as though it converged in
`bar-d`: the evidence file records a direct `bar-d=1/2` obstruction for that
sequence.  Either prove closure for all countable quasi-transitive actions, or
give an explicit nonamenable action, a sequence of genuine Bernoulli factors,
an explicit `bar-d`-convergent coupling scheme, and a rigorous proof that the
limit is not a Bernoulli factor.  If the full question remains open, isolate
the strongest exact subcase or equivalent obstruction without changing the
quantifiers.

Treat A and B as independent theorem runs.  For each, return one of
`PROVED`, `DISPROVED`, or `INCOMPLETE`, with a self-contained proof or exact
gap.  Explicitly audit: full-group versus subgroup equivariance, null-set
simultaneity for an uncountable group, the source Bernoulli action, orbit
representatives in `bar-d`, invariant joinings, and every cited theorem's
hypotheses.  Separate correctness, prior-art status, and publication value.

Write the complete response into `research/ln01/OUTPUT.md`.  Do not treat an
empty placeholder as an output, do not modify the frozen task, and do not
merge the Draft PR.
