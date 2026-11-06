# Problem formulation and methodology

## State estimation on a graph

Represent the electrical network as G=(V,E). The static state is

\[
x=[V_1,\ldots,V_n,\theta_1,\ldots,\theta_n]^T,
\]

with one angle fixed by the reference-bus convention. Measurements obey

\[
z=h_G(x)+e,
\]

where h_G contains nonlinear voltage, power-injection, and branch-flow equations. The graph subscript matters: a changed topology changes the mapping from the physical state to measurements.

## Classical reference

The weighted least-squares estimator solves

\[
\hat{x}_{WLS}=\arg\min_x (z-h_G(x))^T W(z-h_G(x)).
\]

The primary comparison is WLS-node, which receives the same information budget as the learned estimators. This avoids confounding the comparison by giving WLS additional measurements.

## Learned estimator and structural shift

The learned mapping is written as

\[
\hat{x}=f_\theta(G,z).
\]

The training graph is fixed at G0, while evaluation includes held-out graphs:

\[
P_{train}(G,z,x)\ne P_{test}(G,z,x).
\]

The study does not claim a new GNN architecture. Its experimental focus is strict topology-disjoint evaluation and the change in estimator reliability as structural distance increases.

## Physics-GAT

Physics-GAT retains the GAT state loss and adds a weighted measurement-consistency residual. The exact objective is documented in [physics regularization](physics_regularization.md). The physics term is evaluated as a robustness intervention and consistency constraint, not as proof that neural estimation universally replaces WLS.

## Evaluation dimensions

- **State accuracy:** voltage-magnitude and phase-angle estimation error.
- **Structural robustness:** error inflation as the test graph moves away from G0.
- **Physical consistency:** reconstructed-measurement residual and power mismatch.
- **Observability:** whether the measurement Jacobian sufficiently constrains the state.

A topology shift can alter electrical structure, while loss of observability can independently make estimation ill-conditioned. The paper therefore repeats the topology-distance analysis on an observable subset.
