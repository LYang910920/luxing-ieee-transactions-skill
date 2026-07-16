# Topology-First Experiment Protocol When Real Propagation Data Are Unavailable

## Principle

A lack of real propagation or attack–defense trajectories does not block a rigorous node-level paper. It changes the evidence claim. Acquire or construct the network topology first, declare all synthetic/assumed dynamics, and validate the simulator across graph families, seeds, sizes, parameters, and independent numerical representations.

## Evidence ladder

Use the highest feasible rung and label it exactly.

| Level | Topology | Dynamics/parameters | Permitted label |
|---|---|---|---|
| T1 | observed real network | declared synthetic or assumed | real-topology simulation |
| T2 | observed real network plus empirical node/edge attributes | partly calibrated, partly assumed | attribute-informed real-topology simulation |
| T3 | temporal/contact network or timestamped trace | recorded exogenous events plus counterfactual controls | temporal-network or trace-driven simulation |
| T4 | synthetic graph matched to observed statistics or degree sequence | synthetic/assumed | topology-calibrated synthetic simulation |
| T5 | fully synthetic graph and dynamics | synthetic/assumed | controlled synthetic simulation |

Do not call T1–T5 “real-world validation” unless the observed outcomes and intervention effects are genuinely measured and validated.

## Mandatory node-level graph contract

Every node-level study must specify:

```yaml
graph_role: contact | communication | influence | dependency | attack-path | other
directed: true | false
weighted: true | false
signed: true | false
temporal: true | false
multilayer: true | false
adjacency_semantics: "A[i,j] means j influences i"
node_unit: ...
edge_unit: ...
self_loop_policy: ...
parallel_edge_policy: ...
isolated_node_policy: ...
component_policy: ...
weight_transformation: ...
normalization: none | row | max-degree | spectral | other
timestamp_handling: ...
node_attribute_provenance: ...
```

If the domain uses the opposite adjacency convention, state and test the conversion.

## Topology acquisition route

1. Define what an edge means in the scientific mechanism.
2. Search an official dataset source or repository for a network with compatible semantics.
3. Record licence/terms, citation, version/date, checksum, node/edge schema, direction, weights, time fields, and privacy concerns.
4. Preserve a raw immutable copy outside Git.
5. Build a deterministic preprocessing script.
6. Produce a topology card and preprocessing log.
7. Compare the retained graph statistics with the original source description.
8. Hold out complete graphs/snapshots when claiming topology generalization.

A convenient graph is not automatically a valid graph. An email, social-follow, router, attack-graph, and physical-contact edge imply different mechanisms.

## Synthetic topology suite

When no suitable observed topology is available, use a structured graph suite rather than one arbitrary network:

- Erdős–Rényi for homogeneous random connectivity;
- Barabási–Albert or another scale-free generator for hub effects;
- Watts–Strogatz for clustering and short paths;
- stochastic block model for communities;
- configuration model for a declared degree sequence;
- directed/weighted/signed extensions when the mechanism needs them;
- temporal/activity-driven variants when timing is central.

Vary:

- graph family;
- graph seed;
- size and average degree;
- clustering/modularity;
- degree heterogeneity;
- direction/weight distribution;
- community imbalance;
- temporal burstiness when applicable.

Use matched mean degree, density, or degree sequence when the research question compares topology effects.

## Node-level dynamics generation

Acceptable simulation modes include:

- deterministic node-probability ODEs;
- continuous-time Markov-chain or Gillespie simulation;
- discrete-time Monte Carlo;
- agent-based or discrete-event simulation;
- sampled closed-loop/RL environments;
- continuous–impulsive hybrid simulation.

At least one independent representation should be used on bounded cases. For example, compare a node-probability ODE against a Monte Carlo ensemble, or compare a sampled environment's no-action trajectory with the canonical continuous model.

## Parameter and initial-condition generation

Every generated quantity must appear in `REALITY_LEDGER.csv`.

Parameter profiles may include:

- homogeneous;
- degree-correlated;
- community-correlated;
- feature-conditioned;
- seeded lognormal, Beta, or bounded distributions;
- matched-mean homogeneous controls;
- calibrated effective rates, when data support them.

Initial attack/propagation seeds should include more than one placement rule:

- uniform random;
- high degree;
- high betweenness or centrality;
- community-targeted;
- multiple dispersed seeds;
- adversarially selected within a declared candidate set.

Do not hide a favorable seed-placement choice inside the default configuration.

## Experimental minimum

A serious topology-first node-level paper should normally include:

1. no-control or no-defense sanity case;
2. independent solver or simulator consistency check;
3. at least two topology families, or one observed topology plus matched synthetic controls;
4. multiple graph seeds and parameter seeds;
5. matched-budget baselines;
6. topology/parameter sensitivity;
7. held-out graph or size when claiming generalization/scalability;
8. runtime, memory, state dimension, invariant error, and convergence/residual diagnostics;
9. uncertainty intervals and retained failed runs;
10. claim language limited to the tested model/topology/parameter domain.

## Baselines

Select from:

- no intervention;
- uniform allocation;
- random allocation with the same budget;
- degree-based;
- risk/parameter-based;
- community-based;
- oracle or full-information upper bound;
- continuous FBS/direct optimization;
- fixed or rule-based policy;
- learned policy with matched observation and tuning opportunity.

A baseline is unfair when it receives less information, less budget, a shorter tuning budget, or a different graph/trace.

## Recommended metrics

Scientific state:

- time-integrated adverse state/exposure;
- peak and final adverse state;
- time to threshold or extinction when defined;
- spread/reach and affected-node distribution.

Decision quality:

- objective/payoff;
- control/impulse/action cost;
- budget use;
- response time;
- unilateral-deviation gain for game claims.

Numerical and computational:

- invariant, bound, mass, and nonnegativity errors;
- fixed-point/stationarity/residual norms;
- iteration count;
- runtime, memory, and state dimension;
- convergence/failure rate.

Structural:

- degree-stratified and community-stratified outcomes;
- hub versus nonhub effects;
- topology perturbation and degree-preserving rewiring sensitivity;
- graph-size transfer.

## Claim boundary

Use language such as:

> Under the specified node-level model, topology preprocessing, parameter ranges, and intervention budget, the proposed strategy reduced the time-integrated adverse state across the tested observed and synthetic graphs.

Do not infer:

- calibrated real attack rates;
- field effectiveness;
- causal intervention effects;
- general robustness;
- a general Nash equilibrium;
- operational deployability.

Those claims require stronger evidence tracks.
