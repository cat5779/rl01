# Current result: relative finitary DPP dynamics along a cyclic direction

Start with [CYCLIC.md](CYCLIC.md). On every countable group containing an infinite-order element, it constructs a family of spectral-zero increments and weighted-small convolution backgrounds with a whole-path relative finitary DPP process. The cyclic subgroup need not be central or normal. Relative query count and radius have finite first moments in a constructed proper metric. Composing the separate gapped initial sampler gives joint iid finitarity, without asserting moments for the composed encoding.

The new proof uses the positive sandwich A W A to preserve the cyclic spectral kernel without commutation. An ell_(3/5) estimate and an ordering of inverse-pair coefficients replace the old geometric product-neighborhood argument. In particular it covers F2, whose center is trivial.

The analytic dependencies are [the positive-rate theorem](GENERAL.md), [local updates and finite certificates](LOCAL.md), [the scalar Fourier kernel](FOURIER.md), and [the imported initial sampler](SAMPLER.md). The source and review of the new bridge are [SOURCE12.json](SOURCE12.json) and [REVIEW12.md](REVIEW12.md).

The earlier [central-cyclic construction](CENTER.md) remains a companion for its explicitly proved noncommuting-background examples. Its cyclic and direct-product predecessors are retained in the source lineage, rather than separate current branches. The sandwich construction changes the increment family; it does not assert that every older increment is literally a special case.

An infinite-order element, a constructed increment, weighted-small background, and constructed metric remain restrictions. General ordered DPP factors, arbitrary increments/backgrounds, preassigned-metric bounds, and composed coding moments remain open. The reviews are scoped internal different-author checks in reused contexts, not external acceptance, complete formalization or novelty certification.
