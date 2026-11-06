# Reproducibility status

## What this repository currently provides

- The paper's problem formulation and protocol, documented from the manuscript.
- CSV transcriptions of paper-reported aggregate tables.
- Vector diagrams explaining the benchmark split and Physics-GAT objective.
- A script for plotting the paper-reported aggregate metrics.

## What it does not currently provide

The supplied files did not contain the original implementation or raw benchmark artifacts. This repository therefore does not currently provide:
- Training loops or model classes for MLP, GCN, GraphSAGE, GAT, or Physics-GAT.
- A WLS-node implementation or exact measurement model.
- Topology-generation code, branch lists, or raw 55-bus benchmark inputs.
- Numerical observability and paired-statistics implementations.
- Per-seed logs, per-topology predictions, or model checkpoints.

## Replotting reported values

```bash
pip install -r requirements.txt
python scripts/plot_paper_reported_results.py
```

This re-renders visual summaries from the committed paper-reported CSVs. It does not retrain models, regenerate the dataset, or independently verify the manuscript experiments.

## Release rule

Do not label the benchmark a complete reproduction until the source implementation and licensed benchmark inputs are integrated, tests pass, and a clean environment can regenerate per-topology outputs. Record exact commits, configuration hashes, software versions, seeds, and raw outputs.
