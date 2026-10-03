# Joint iid coupling at the Fuglede–Kadison parameter

## Current mathematical scope

For a fixed countable group acting regularly on itself and a fixed equivariant complex Hermitian positive contraction Q, there is a joint regular-iid construction of X~Bern(FK(Q)) and Y~DPP(Q) with X contained in Y. The map is total Borel and equivariant on every input, and containment holds on every input.

The positive-FK branch is constructed directly. At FK(Q)=0, the proof explicitly invokes the marginal-sampling hypothesis H for that fixed Q. At FK(Q)=1 the construction is deterministic. The statement covers singular terminal kernels but does not assert a grand coupling, measurable dependence on all kernels, a finitary code, or a theorem for arbitrary stabilizer actions.

Two full mathematical audits accept the frozen revised proof. This is an internal proof-review result, not completed human domain review, formal verification, or novelty certification.

## Manuscripts and checks

- [Readable proof](proof03.md): the reviewed argument with only the status line and one missing typesetting backslash corrected.
- [Frozen revised proof](proof02.md): the exact version examined by both full reviews; its original candidate-status marker is retained.
- [First full review](REVIEW02.md) and [second full review](REVIEW03.md).
- [Repair explanation](REPAIR02.md): direct independent-noise construction and finite conditional-chain comparison.
- [Prior methods and attribution boundary](SOURCES.md).
- [Earlier incomplete candidate](proof01.md) and [its critical-gap report](REVIEW01.md), retained as superseded mathematics.

The source bits and independent Poisson proposals are inputs, not noise inferred from coordinate compensators. Marginals are identified by a common coupling with finite conditional chains and two dependency envelopes, with the spatial boundary removed before the envelope range tends to infinity.

The theorem gives the FK lower coupling for each fixed kernel. Complementation gives an upper coupling separately. It does not automatically give a common three-level sandwich, the coupling for every ordered pair of kernels, or extraction at a true optimal threshold larger than FK(Q). These remain distinct questions.
