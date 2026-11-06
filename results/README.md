# Results provenance

The CSVs under data/paper_reported/ contain aggregate values transcribed from the supplied manuscript:

| CSV | Source | Contents |
|---|---|---|
| voltage_rmse.csv | Table 1 | Voltage RMSE across T0–T4 |
| angle_rmse.csv | Table 1 | Voltage-angle RMSE across T0–T4 |
| ood_degradation.csv | Table 2 | Relative OOD degradation factors |
| topology_distance_regression.csv | Table 3 | Slopes, confidence intervals, R², Spearman rho, p-values |
| physics_lambda_sweep.csv | Table 4 | Validation state-error / physics-residual trade-off |
| physical_consistency.csv | Table 5 | P/Q mismatch, measurement residual, violation rates |
| benchmark_controls.csv | Table 6 | Frozen controls and scientific purpose |
| closest_work_positioning.csv | Table 7 | Positioning summary reported in the paper |

These are paper-reported aggregates, not raw observations, independent reruns, or per-seed/per-topology outputs.
