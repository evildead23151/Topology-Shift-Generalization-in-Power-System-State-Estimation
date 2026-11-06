# Source implementation status

The source files supplied for this repository update did not include the experiment's Python implementation. This directory is intentionally not populated with placeholder code that would imply working estimators.

When integrating the original implementation, keep separate modules for:
- Measurement and topology-aware power-system model.
- WLS-node reference estimator.
- Topology and operating-point generation.
- MLP, GCN, GraphSAGE, GAT, and Physics-GAT estimators.
- Measurement residual and P/Q mismatch calculations.
- Numerical observability diagnostics.
- Metrics, paired statistics, and experiment logging.

Add unit tests and a minimal end-to-end smoke test before claiming reproducibility.
