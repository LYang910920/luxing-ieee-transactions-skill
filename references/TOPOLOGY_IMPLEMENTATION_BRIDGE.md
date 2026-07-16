# Topology Implementation Bridge Across the Three Repositories

## Purpose

This bridge tells WORK how to turn an acquired or generated graph into a node-level paper experiment without copying the three tutorial repositories into the SKILL. It is an interface contract, not a code fork.

## Canonical topology object

Every project should expose one canonical topology record:

```text
node labels or anonymous stable IDs
edge table or graph object
A[i,j] convention
node/edge attributes
source and checksum
direction, weight, sign and time semantics
preprocessing lineage
full-graph statistics
analysis graph or snapshot selection
```

The preferred model convention is stated explicitly in the Foundation material: `A[i,j]` represents influence/contact from node `j` to node `i`. If a source edge list uses source-to-target matrix convention, transpose or adapt exactly once at the graph boundary and test it.

## Foundation bridge

Use the Foundation layer for topology ingestion, canonical equations and numerical validation.

Relevant pinned interfaces are recorded in `repo_family/repository_manifest.yaml` and include the graph/data, graph-utility, network-model, heterogeneous-parameter and FBS modules.

WORK should implement or call an adapter that can:

1. read edge lists, adjacency matrices and common graph formats;
2. remove or aggregate self-loops/parallel edges according to the topology card;
3. preserve direction and weights;
4. compute full-graph degree and structural statistics;
5. build the canonical node-level adjacency;
6. optionally derive degree-class data without replacing the node-level graph;
7. support dense and sparse paths where the live repository permits;
8. record graph source, version/hash, normalization and preprocessing in the run manifest.

Before optimization or learning, run the uncontrolled and fixed-rule node-level dynamics and verify bounds, mass/conservation, NumPy/Torch agreement where relevant, and time-grid sensitivity.

## Game-learning bridge

The game-learning layer should receive the canonical graph rather than silently generating a new one inside the environment.

For a real-topology or topology-controlled paper, WORK should add an injectable graph interface around the environment construction:

```text
canonical adjacency + node/community attributes
→ environment reset
→ observation construction
→ action-to-rate/reset mapping
→ ODE or event integration
→ reward and physical metrics
```

Required checks:

- a no-action rollout agrees with the Foundation model;
- flow actions do not create state jumps;
- impulse actions change state only through the declared reset map;
- action, graph and parameter seeds are independent and logged;
- learned, rule-based and random policies use the same graph, budget and information;
- held-out graphs/snapshots are never used for training or normalization fitting;
- response matrices and unilateral deviations are reported for game claims.

A policy trained on a generated community graph is not automatically validated on an observed topology. Treat graph transfer as a separate experiment.

## Physics-informed bridge

The physics-informed layer should also receive the canonical graph through an injected adjacency/operator interface.

For real topology with synthetic trajectories:

```text
observed graph
+ declared heterogeneous parameter profile
+ independent numerical simulator
→ sparse/noisy synthetic observations
→ inverse PINN/PIDL training
→ held-out node/time/graph evaluation
```

This supports controlled recovery and observability studies on an empirical structure, not real parameter calibration.

For real observations:

- define which measured fields map to states or observation likelihoods;
- keep topology, observations and parameters in separate provenance records;
- use complete temporal/graph/scenario holdouts;
- compare learned parameters through independent rollout and effective-rate errors;
- state scaling gauges and non-identifiability;
- never use residual consistency alone as parameter truth.

## Large-graph strategy

Choose one and state it explicitly:

### Full sparse node-level simulation

Use when the state equation and solver support sparse adjacency operations. Report full node/edge count, memory, runtime and tolerances.

### Degree-class or other reduced model

Use the full graph only to derive the reduction, such as an empirical degree distribution or mixing matrix. The claim then concerns the reduced model, not individual observed nodes.

### Induced or sampled subgraph

Use only with a scientific or computational rationale. Record the selection rule and both full/reduced statistics. Do not describe a top-degree induced subgraph as the whole observed network.

### Multi-resolution comparison

When feasible, compare degree-level and explicit node-level results under matched parameters and objectives. Differences should be interpreted as representation effects, not solver superiority.

## Synthetic topology bridge

When no observed graph is suitable, generate through a separate topology adapter, not inside the model solver. At minimum support a controlled subset of:

```text
Erdos-Renyi
Barabasi-Albert or another scale-free generator
Watts-Strogatz
stochastic block model
configuration model matched to a degree sequence
```

For topology-sensitive claims use at least two families, multiple sizes and multiple graph seeds. Store generator family/parameters in `SYNTHETIC_SCENARIO_SPEC.yaml` and outcomes in `GRAPH_BENCHMARK_MATRIX.csv`.

## Required project artifacts

```text
topology/TOPOLOGY_SOURCE_SCREENING.csv
topology/TOPOLOGY_ACQUISITION_PLAN.md
topology/TOPOLOGY_CARD.yaml
topology/GRAPH_PREPROCESSING_LOG.csv
topology/GRAPH_BENCHMARK_MATRIX.csv
topology/GRAPH_SPLIT_PLAN.csv
topology/GRAPH_TO_MODEL_MAP.csv
repo_bridge/REPOSITORY_EVIDENCE_MAP.csv
simulation/SYNTHETIC_SCENARIO_SPEC.yaml
simulation/NODE_LEVEL_EXPERIMENT_MATRIX.csv
simulation/SIMULATOR_VALIDATION_MATRIX.csv
```

## Claim wording

Observed topology + synthetic dynamics:

> We evaluate the node-level model on an observed communication topology while generating propagation, attack and intervention processes under the declared parameter ranges.

Generated topology:

> We conduct a controlled multi-family graph study to assess sensitivity to topology, size and heterogeneity under the stated model.

Do not write `real-world attack validation`, `field-proven`, `arbitrary topology` or `operationally effective` unless separate evidence supports those claims.
