# Contributing

Contributions should preserve the benchmark's topology-disjoint evaluation and information-fair comparison.

Before submitting changes:
1. State whether each artifact is paper-derived, newly generated, or independently reproduced.
2. Preserve T0-only training/validation and keep OOD test data out of model selection.
3. Record seeds, exact branch sets, measurement maps/weights, normalization statistics, software versions, and configuration hashes.
4. Add tests for state/measurement conventions, topology identity, and metric calculations.
5. Do not add benchmark data unless redistribution rights and provenance are documented.
6. Do not claim reproduction based only on plotting aggregate paper tables.

When reporting a result, identify the paper section/table/figure or link the exact experiment run.
