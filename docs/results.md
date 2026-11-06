# Results and interpretation

All values below are aggregate values reported in the supplied paper. CSV files in data/paper_reported preserve the reported values and labels; they are not per-sample predictions.

## Severe topology shift

| Estimator | IID voltage RMSE | T4 voltage RMSE | OOD factor at ~10% |
|---|---:|---:|---:|
| WLS-node | 0.0062 | 0.0155 | 2.50 |
| MLP | 0.0080 | 0.0380 | 4.75 |
| GCN | 0.0068 | 0.0300 | 4.41 |
| GraphSAGE | 0.0065 | 0.0275 | 4.23 |
| GAT | 0.0062 | 0.0248 | 4.00 |
| Physics-GAT | 0.0061 | 0.0215 | 3.52 |

Physics-GAT reduces the severe-OOD degradation factor from 4.00x to 3.52x relative to GAT. WLS-node retains the lowest T4 voltage RMSE and the smallest degradation factor in this table. Do not claim Physics-GAT is the absolute-accuracy winner.

## Topology-distance trend

| Model | Slope β1 | 95% CI | R² | Spearman ρ |
|---|---:|---:|---:|---:|
| MLP | 0.165 | [0.145, 0.185] | 0.67 | 0.82 |
| GCN | 0.132 | [0.114, 0.150] | 0.63 | 0.79 |
| GraphSAGE | 0.121 | [0.104, 0.139] | 0.61 | 0.78 |
| GAT | 0.109 | [0.093, 0.126] | 0.58 | 0.75 |
| Physics-GAT | 0.092 | [0.077, 0.108] | 0.56 | 0.72 |
| WLS-node | 0.061 | [0.041, 0.080] | 0.34 | 0.57 |

The paper interprets these associations descriptively rather than causally.

## Physical consistency

Physics-GAT reports lower P mismatch, Q mismatch, measurement residual, and violation-rate ranges than the learned baselines in the paper's common normalization. WLS-node remains a strong physical reference. Consult data/paper_reported/physical_consistency.csv for exact transcribed values.

## Observable-only analysis

The paper reports at least 95% numerically observable retained OOD cases, at most 5% near-unobservable cases, and no unobservable cases after the predefined topology filter. The GAT versus Physics-GAT difference remains in the observable-only subset.

## Main takeaway

IID accuracy on a fixed graph is not sufficient evidence of deployment reliability under reconfiguration. Graph structure reduces degradation relative to a topology-agnostic MLP, and the physics penalty improves the learned estimator's reported OOD robustness and residuals. This does not establish universal superiority over WLS or cross-system generalization.
