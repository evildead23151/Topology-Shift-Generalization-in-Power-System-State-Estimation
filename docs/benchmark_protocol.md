# Benchmark protocol

This document records the experiment design described in the paper. It is a protocol specification, not an implementation claim.

## Network and state-estimation problem

The study uses a published 55-bus distribution-system state-estimation benchmark: 55 buses, 27 lines, 27 transformers, 10 generation buses, 16 load buses, three capacitor banks, 134 measurements, and 109 states. The state contains bus-voltage magnitudes and phase angles, with one reference angle fixed by the slack/reference convention.

The topology-dependent measurement model is:

\[
z=h_G(x)+e,
\]

where G=(V,E) is the network graph, x is the electrical state, and e is measurement noise.

## Original-topology split

| Split | Topology | Operating points |
|---|---|---:|
| Train | T0 | 20,000 |
| Validation | T0 | 3,000 |
| IID test | T0 | 3,000 |

All learned estimators train on T0 only. Normalization statistics are computed from training data only.

## Strictly held-out topology suite

| Family | Shift | Retained topologies | Fresh points/topology | OOD points |
|---|---|---:|---:|---:|
| T1 | N-1 | 10 | 1,000 | 10,000 |
| T2 | N-2 | 10 | 1,000 | 10,000 |
| T3 | Approximately 5% branch modification | 10 | 1,000 | 10,000 |
| T4 | Approximately 10% branch modification | 10 | 1,000 | 10,000 |
| **Total** | **40 held-out topology instances** | **40** | — | **40,000** |

OOD operating points are fresh and are not used for training, validation, normalization, or hyperparameter selection.

## Topology distance

\[
d_{topo}(G,G_0)=\frac{|E(G_0)\triangle E(G)|}{|E(G_0)|}.
\]

This is a structural descriptor, not a complete electrical-distance metric: equal values can correspond to different electrical consequences.

## Compared estimators

1. WLS-node — classical weighted least squares using the common measurement-information budget; primary classical reference.
2. MLP — topology-agnostic feed-forward estimator.
3. GCN — graph convolutional estimator.
4. GraphSAGE — neighborhood aggregation estimator.
5. GAT — graph-attention estimator.
6. Physics-GAT — GAT with a measurement-consistency regularizer.

WLS-all is described as an additional reference but may use more measurements; it is not the primary information-fair comparison.

## Training settings reported

| Setting | Value |
|---|---:|
| Hidden width | Approximately 128 |
| Optimizer | Adam |
| Learning rate | 1e-3 |
| Weight decay | 1e-5 |
| Batch size | 256 where feasible |
| Maximum epochs | 200 |
| Early stopping | Validation-only, patience 20 |
| Seeds | 13, 42, 73, 101, 2026 |
| Physics-weight candidates | 1e-4, 1e-3, 1e-2, 1e-1, 1, 10 |

The selected physics weight is chosen using validation behavior, not OOD test performance.

## Evaluation

**State error:** voltage-magnitude RMSE/MAE and voltage-angle RMSE/MAE.  
**Physical consistency:** measurement reconstruction residual, active-power mismatch, reactive-power mismatch, and constraint-violation rates where applicable.  
**Relative OOD degradation:** R_OOD = RMSE_OOD / RMSE_IID; percentage degradation = 100(R_OOD - 1).  
**Observability:** numerical measurement-Jacobian rank and conditioning; repeat topology-distance trend on the numerically observable subset.  
**Statistics:** identical test examples, five seeds, paired bootstrap confidence intervals, Wilcoxon signed-rank tests, and effect-size reporting.

## Leakage controls reported

T0-only training; fresh OOD operating points; shared measurement information; training-only normalization; five fixed seeds; validation-only physics-weight selection; observable-only re-analysis; and paired test cases.

## Inputs still required for a complete reproduction

The exact benchmark inputs and redistribution terms, measurement map and weights, topology-generation code and retained branch lists, state-estimation solver, model implementations, observability calculations, experiment runner, environment lockfile, and per-topology outputs are not part of this documentation-only update. Do not synthesize or imply these files exist.
