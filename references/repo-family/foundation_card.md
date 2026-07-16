# Repository Card — Network Control and Differential Games

## Role in the skill

Use this repository as the mathematical and numerical foundation. It anchors the paper workflow in a declared dynamical mechanism before any learning or data-fitting layer is added.

## Stable doctrines to integrate

- Define state order, units, topology, control timing, reset maps, objectives, and information structure before selecting an algorithm.
- Distinguish aggregate, degree-class, and explicit-node resolutions; justify the chosen resolution.
- Distinguish continuous flow controls, sampled zero-order-hold actions, and true impulses that create jumps.
- Implement the uncontrolled model and independent/simple baselines before a sophisticated solver.
- Verify invariants, bounds, Jacobians, projected stationarity residuals, grid sensitivity, and matched-mean comparisons.
- Treat a numerical FBS fixed point as evidence for the configured problem, not a general proof of global optimality or equilibrium.
- Map every manuscript claim to equations, typed configuration, solver output, manifest rows, and figure-generation commands.

## Capabilities that directly support real-data work

The graph input layer can consume edge lists, adjacency CSV files, GraphML, GEXF, GML, and Pajek/NET files. It can preserve the full graph for empirical degree-distribution analysis while using a reduced subgraph for dense node-level examples. Parameter profiles can also be supplied as arrays or loaded from CSV.

This makes the repository immediately suitable for **real-topology/semi-synthetic studies**. A real graph does not, by itself, make propagation rates or intervention effects empirical; the paper must label which elements are observed and which remain assumed or calibrated.

## Skill integration points

- Model contract and notation dictionary.
- Graph and parameter provenance card.
- Theorem-to-code map.
- Numerical verification checklist.
- Matched-budget and matched-mean baselines.
- Scaling study and sparse-versus-dense implementation audit.
- Real-topology adapter plan.

## Gaps WORK should not hide

- The public examples are controlled research/teaching studies, not operational cyber-risk calibrations.
- The repository has no project-wide permissive licence by default. The public skill should paraphrase doctrines and link/pin sources rather than copy source or tutorial text unless the owner makes a separate licensing decision.
- Real event traces, observed intervention outcomes, and deployment measurements require an additional data/simulation layer.
