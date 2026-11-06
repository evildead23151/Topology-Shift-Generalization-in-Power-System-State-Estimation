#!/usr/bin/env python3
"""Validate schema and internal consistency of paper-reported aggregate CSVs.

This does not verify the original experiments; it checks repository transcription
and derived OOD ratios only.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "paper_reported"
MODELS = {"WLS-node", "MLP", "GCN", "GraphSAGE", "GAT", "Physics-GAT"}


def rows(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    voltage = {r["model"]: r for r in rows("voltage_rmse.csv")}
    factors = {r["model"]: r for r in rows("ood_degradation.csv")}
    assert set(voltage) == MODELS
    assert set(factors) == MODELS
    for model in MODELS:
        iid, t4 = float(voltage[model]["T0"]), float(voltage[model]["T4"])
        observed = float(factors[model]["approximately-10-percent"])
        expected = t4 / iid
        assert abs(observed - expected) < 0.015, (model, observed, expected)
    assert len(rows("angle_rmse.csv")) == 6
    assert len(rows("topology_distance_regression.csv")) == 6
    assert len(rows("physical_consistency.csv")) == 6
    assert len(rows("physics_lambda_sweep.csv")) == 6
    assert len(rows("benchmark_controls.csv")) == 8
    assert len(rows("closest_work_positioning.csv")) == 5
    print("Paper-reported CSV schema and severe-OOD ratio checks passed.")


if __name__ == "__main__":
    main()
