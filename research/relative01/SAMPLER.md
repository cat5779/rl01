# Imported gapped initial-sampler theorem

The relative theorem in this package does not require a new initial sampler: it takes the supplied initial configuration and independent fresh clocks. For its joint-iid corollary we use the following previously reviewed, separately preserved theorem.

For any countable group Gamma and a finite nonempty set S of free coordinate types, an equivariant Hermitian DPP kernel Q on Gamma x S with 0<aI<=Q<=bI<I has an equivariant sampler from one iid uniform label per group coordinate. Each coordinate has an almost-sure finite certificate valid under arbitrary outside completions. This theorem supplies no coding moments, finite-alphabet coding, computable real comparisons, nongapped extension, or arbitrary stabilizer extension.

The frozen source is [the gapped finite-free-type sampler](https://github.com/randomcat4/icm-conjecture-lab/blob/a87f4a939506436c2def371bd791e1228d915c12/research/dppffiid01/NOSOFIC06R02.md), Git blob `7fea8ece86ba4ef16ca04bdc2479e9bebc0dcc98`, SHA256 `f83ea77e5fd0a482ba42786f5a24bd343e0be939ffb6c36630dcf0b7a82b3a09`. Its previously preserved full scope review is colocated as `CODEX_AUDIT06B.md`. This package checks the source identity and its hypotheses, and does not claim a new full audit of that historical proof.

In CENTER.md, Q=I/2+B has the required two-sided gap and one free regular type. Split every iid uniform label into independent sampler and clock channels. A successful relative path query reads finitely many initial coordinates. The finite union of their initial-sampler certificates and the queried clock labels fixes the whole target path under arbitrary completions. This proves the composed finitary conclusion. The relative moment estimates do not automatically pass through the initial sampler.
