# Limitations and claim boundaries

1. **One primary network.** The quantitative study centers on one published 55-bus distribution benchmark; it should not be generalized to all distribution or transmission systems without replication.
2. **Topology distance is incomplete.** Branch-set symmetric difference is a compact structural descriptor, but equal distances can have different electrical consequences. The reported regression is descriptive, not causal.
3. **Uncertainty is not established.** The paper does not claim calibrated predictive uncertainty as an established result.
4. **WLS remains a serious baseline.** The neural estimators do not replace model-based estimation merely by matching IID error. The paper emphasizes robustness changes, not universal neural superiority.
5. **Paper reporting and implementation reproducibility are separate.** This repository documents aggregate values and visualizes them; raw data and experiment code are needed for end-to-end reproduction.

## Safe summary

On the reported 55-bus study, Physics-GAT reduces severe topology-OOD degradation relative to GAT and improves physical-residual metrics among learned models, while WLS-node remains a strong classical reference. Broader deployment claims require cross-system replication.
