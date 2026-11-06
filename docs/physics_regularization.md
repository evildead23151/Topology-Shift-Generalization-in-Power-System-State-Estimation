# Physics-GAT: measurement-consistency regularization

Physics-GAT uses the same state-estimation loss as GAT and adds a measurement residual evaluated through the topology-specific physical measurement function.

## Objective

\[
L_{state}=MSE(V,\hat V)+\alpha MSE(\hat\theta,\theta)
\]

\[
L_{phys}=\frac{1}{N}\sum_{i=1}^{N}(h_G(\hat x_i)-z_i)^T W(h_G(\hat x_i)-z_i)
\]

\[
\boxed{L=L_{state}+\lambda_{phys}L_{phys}}
\]

The paper's candidate regularization weights are 1e-4, 1e-3, 1e-2, 1e-1, 1, and 10. The selected value is chosen on validation data only; OOD test performance is not used for selection.

## Reported validation trade-off

| λ_phys | Validation state RMSE | Validation physics residual |
|---:|---:|---:|
| 1e-4 | ≈0.0062 | ≈0.020 |
| 1e-3 | ≈0.0061 | ≈0.016 |
| 1e-2 | ≈0.0060 | ≈0.012 |
| 1e-1 | ≈0.0061 | ≈0.009 |
| 1 | ≈0.0067 | ≈0.007 |
| 10 | ≈0.0085 | ≈0.006 |

The table illustrates a trade-off: stronger regularization lowers the reported physics residual but eventually increases state error. The values are transcribed from the paper's aggregate table, not generated from a new sweep in this repository.
