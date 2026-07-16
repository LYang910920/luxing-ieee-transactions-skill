# Node-Level Topology Protocol

## Scope

This protocol prevents a node-level paper from using “network” as an undefined implementation detail. It applies to deterministic, stochastic, learning-based, physics-informed, attack-graph, and continuous–impulsive studies.

## Topology card

Screen candidate graphs in `templates/TOPOLOGY_SOURCE_SCREENING.csv`, then complete `templates/TOPOLOGY_CARD.yaml` before running the main experiment. Record:

- scientific meaning of node and edge;
- graph source, version, citation, terms, and checksum;
- direction, weight, sign, time, layers, and edge multiplicity;
- raw schema and preprocessing;
- component, isolate, self-loop, duplicate-edge, and missing-node policies;
- adjacency convention and normalization;
- node/edge attributes and whether they are observed, inferred, or synthetic;
- graph statistics before and after preprocessing;
- intended and prohibited claims.

## Preprocessing invariants

The graph adapter must deterministically verify:

- node and edge counts;
- no unintended duplicate node identifiers;
- self-loop handling;
- positive/finite weights when required;
- temporal ordering;
- component retention;
- direction preservation;
- adjacency orientation;
- source-to-output checksum lineage.

A top-degree induced subgraph can be useful for bounded dense solvers, but it changes the scientific graph. Report both full-graph statistics and reduced-graph selection, and do not describe the reduced graph as the complete observed network.

## Graph splits

For learning, calibration, or generalization claims, split by the highest-level independent unit:

- complete graph;
- complete temporal snapshot/window;
- complete scenario/capture;
- complete community only when leakage is prevented;
- node/time masks only for interpolation-style questions.

Random edge splitting is usually invalid for a dynamic propagation claim because it changes the graph and leaks neighborhood structure.

## Topology benchmark matrix

Use `GRAPH_BENCHMARK_MATRIX.csv` to state:

- observed or generated source;
- graph family;
- size, density, mean/max degree;
- clustering, assortativity, modularity, spectral radius;
- direction/weight/time features;
- preprocessing and normalization;
- train/tune/test role;
- scenario and parameter seeds;
- manuscript figure/table and claim.

## Perturbation tests

Where relevant, include:

- degree-preserving rewiring;
- random edge deletion/addition;
- weight noise;
- community mixing changes;
- targeted hub removal;
- temporal shuffle;
- node-attribute permutation;
- alternative normalizations.

These tests reveal whether a result follows from the proposed mechanism or from one accidental topology.

## Scalability

A scalability claim needs:

- multiple graph sizes;
- declared sparse/dense representation;
- state dimension and edge count;
- runtime and peak memory;
- solver iterations/episodes;
- accuracy or residual at each size;
- identical scientific tolerances and comparable hardware;
- a clear boundary when the largest observed graph is reduced or sampled.

## Manuscript language

Preferred:

- `node-level simulation on the observed email topology`;
- `controlled simulation on a scale-free graph family`;
- `held-out graph-size evaluation`;
- `topology sensitivity under degree-preserving rewiring`.

Avoid:

- `realistic network` without a documented statistic or source;
- `real-world validation` when only topology is observed;
- `arbitrary topology` when only three graph families were tested;
- `scalable` when only one size or no resource metric is reported.
