#!/usr/bin/env python3
"""Render plots from aggregate values transcribed from the paper.

This script does not run PSSE experiments, train estimators, or generate raw data.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "paper_reported"
OUT = ROOT / "assets" / "figures"
ORDER = ["WLS-node", "MLP", "GCN", "GraphSAGE", "GAT", "Physics-GAT"]
COLORS = ["#64748b", "#f97316", "#16a34a", "#0ea5e9", "#8b5cf6", "#14b8a6"]


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(fig: plt.Figure, stem: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{stem}.svg", bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{stem}.png", bbox_inches="tight", dpi=220, facecolor="white")
    plt.close(fig)


def line_plot(name: str, title: str, ylabel: str, labels: list[str]) -> None:
    rows = {r["model"]: r for r in read_csv(name)}
    fig, ax = plt.subplots(figsize=(10, 6), layout="constrained")
    for model, color in zip(ORDER, COLORS):
        y = [float(rows[model][f"T{i}"]) for i in range(5)]
        ax.plot(labels, y, marker="o", lw=2.4, color=color, label=model)
    ax.set_title(title, loc="left", weight="bold")
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Evaluation topology")
    ax.grid(axis="y", alpha=.25)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, ncol=3)
    save(fig, "voltage_rmse_vs_topology" if name == "voltage_rmse.csv" else "angle_rmse_vs_topology")


def plot_ood() -> None:
    rows = {r["model"]: r for r in read_csv("ood_degradation.csv")}
    keys = ["N-1", "N-2", "approximately-5-percent", "approximately-10-percent"]
    labels = ["N-1", "N-2", "~5%", "~10%"]
    fig, ax = plt.subplots(figsize=(10, 6), layout="constrained")
    for model, color in zip(ORDER, COLORS):
        ax.plot(labels, [float(rows[model][k]) for k in keys], marker="o", lw=2.4, color=color, label=model)
    ax.set_title("Relative error inflation under topology shift", loc="left", weight="bold")
    ax.set_ylabel("RMSE_OOD / RMSE_IID")
    ax.set_xlabel("Held-out topology family")
    ax.grid(axis="y", alpha=.25)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, ncol=3)
    save(fig, "ood_degradation")


def plot_slopes() -> None:
    rows = sorted(read_csv("topology_distance_regression.csv"), key=lambda r: float(r["slope_beta1"]), reverse=True)
    models = [r["model"] for r in rows]
    values = np.array([float(r["slope_beta1"]) for r in rows])
    low = np.array([float(r["ci95_lower"]) for r in rows])
    high = np.array([float(r["ci95_upper"]) for r in rows])
    fig, ax = plt.subplots(figsize=(10, 6), layout="constrained")
    ax.bar(models, values, color=[COLORS[ORDER.index(m)] for m in models], width=.68)
    ax.errorbar(np.arange(len(models)), values, yerr=np.vstack((values-low, high-values)),
                fmt="none", ecolor="#0f172a", capsize=4)
    ax.set_title("Topology-distance regression slopes", loc="left", weight="bold")
    ax.set_ylabel("Voltage-RMSE slope, beta_1")
    ax.tick_params(axis="x", rotation=15)
    ax.grid(axis="y", alpha=.25)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "topology_distance_slopes")


def plot_lambda() -> None:
    rows = read_csv("physics_lambda_sweep.csv")
    x = np.arange(len(rows))
    state = [float(r["validation_state_rmse"]) for r in rows]
    residual = [float(r["validation_physics_residual"]) for r in rows]
    fig, left = plt.subplots(figsize=(10, 6), layout="constrained")
    right = left.twinx()
    a, = left.plot(x, state, marker="o", lw=2.5, color="#0e7490", label="Validation state RMSE")
    b, = right.plot(x, residual, marker="s", lw=2.5, color="#d97706", label="Validation physics residual")
    left.set_xticks(x, [f"{float(r['lambda_phys']):g}" for r in rows])
    left.set_xlabel("Physics regularization weight, lambda_phys")
    left.set_ylabel("Validation state RMSE")
    right.set_ylabel("Validation physics residual")
    left.set_title("Physics regularization trade-off", loc="left", weight="bold")
    left.grid(axis="y", alpha=.25)
    left.spines["top"].set_visible(False)
    right.spines["top"].set_visible(False)
    left.legend([a, b], [a.get_label(), b.get_label()], frameon=False)
    save(fig, "physics_lambda_tradeoff")


def plot_physical() -> None:
    rows = {r["model"]: r for r in read_csv("physical_consistency.csv")}
    metrics = ["P_mismatch", "Q_mismatch", "measurement_residual"]
    names = ["P mismatch", "Q mismatch", "Measurement residual"]
    x = np.arange(len(ORDER))
    width = .24
    fig, ax = plt.subplots(figsize=(11, 6), layout="constrained")
    for i, (metric, label, color) in enumerate(zip(metrics, names, ["#0e7490", "#d97706", "#7c3aed"])):
        ax.bar(x + (i-1)*width, [float(rows[m][metric]) for m in ORDER], width, label=label, color=color)
    ax.set_xticks(x, ORDER, rotation=15)
    ax.set_ylabel("Reported normalized mismatch / residual")
    ax.set_title("Physical-consistency metrics reported in Table 5", loc="left", weight="bold")
    ax.grid(axis="y", alpha=.25)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, ncol=3)
    save(fig, "physical_consistency")


def main() -> None:
    labels = ["T0 / IID", "T1 / N-1", "T2 / N-2", "T3 / ~5%", "T4 / ~10%"]
    line_plot("voltage_rmse.csv", "Voltage RMSE rises under topology shift", "Voltage RMSE (p.u.)", labels)
    line_plot("angle_rmse.csv", "Voltage-angle RMSE rises under topology shift", "Angle RMSE (degrees)", labels)
    plot_ood()
    plot_slopes()
    plot_lambda()
    plot_physical()
    print(f"Wrote six paper-reported figures to {OUT}")


if __name__ == "__main__":
    main()
