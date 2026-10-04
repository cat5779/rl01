# Joint iid-factor Bernoulli endpoint below the \(C_3*C_3\) WUSF

Let \(\Gamma=C_3*C_3\) act on its bipartite 3-regular Bass--Serre tree, with edge set identified with the regular \(\Gamma\)-set.  Let \(T\) denote the WUSF edge process and \(B\) the iid Bernoulli\((1/2)\) edge process.

Prove or disprove the endpoint factor statement:

> There is a standard iid source \(U\in[0,1]^\Gamma\) and a measurable \(\Gamma\)-equivariant map \(\Phi(U)=(B,T)\) such that \(B\) has the iid Bernoulli\((1/2)\) law, \(T\) has the WUSF law, and \(B\subseteq T\) almost surely.

A construction must give one common-input equivariant map and verify the complete joint law, not merely separate iid samplers for the two marginals or an invariant coupling.  A disproof must obstruct every iid-equivariant joint map, not only finitary maps, a particular coding architecture, or a finite-state ansatz.

Strict distinctions:

- An invariant monotone coupling does not automatically give a joint iid factor.
- Weak limits of invariant joint laws do not preserve a common-input factor representation.
- Failure of the five-state splitting construction does not obstruct arbitrary factors.
- If the invariant endpoint is impossible, this factor endpoint is also impossible; the converse need not hold.
- Unlike invariant couplings, the class of iid-factor laws is not known here to be weakly closed, so endpoint nonattainment alone need not determine the supremal value of \(p_{\mathrm{iid}}\).

## Deliverable

Return `PROVED` with an explicit measurable equivariant construction and complete law verification, or `DISPROVED` with a universal exact factor obstruction.  State clearly whether the argument determines only attainment at \(1/2\) or the entire supremal threshold.
