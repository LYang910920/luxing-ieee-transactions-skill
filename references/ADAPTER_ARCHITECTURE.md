# Adapter Architecture for Real Topology, Traces, Observations, and Testbeds

## Purpose

The three teaching repositories already provide the canonical mechanism, sampled-control environment, and physics-informed estimation logic. Real data should enter through **thin, explicit adapters**, not through ad hoc preprocessing embedded in a training loop.

```text
raw source
→ immutable source snapshot / checksum
→ adapter contract
→ validated canonical object
→ model / simulator / estimator
→ split-aware evaluation
→ claim ledger
```

The adapter is not a scientific result by itself. Its job is to make provenance, units, timing, missingness, information availability, and failure behavior visible.

## Canonical adapter roles

### 1. Graph adapter

Input examples: edge list, adjacency table, GraphML, GEXF, GML, Pajek/NET, or a documented API export.

Output:

- labelled graph or adjacency matrix;
- directed/undirected and weighted/unweighted semantics;
- model convention, such as `A[i,j]` meaning that node `j` influences node `i`;
- full-graph statistics and any reduced node-level view;
- component/self-loop/multi-edge handling log;
- topology split identifier.

A real graph supplies observed topology. It does not supply propagation rates, intervention effects, or causal outcomes unless those are separately measured.

### 2. Trace/event adapter

Input examples: timestamped flows, alerts, malware connections, attack events, communication events, or platform cascades.

Output:

- ordered exogenous events;
- event type, entity, timestamp and confidence;
- observation available at each decision time;
- labels hidden from the policy during evaluation;
- aggregation/window definition;
- replay scenario and split identifier.

The adapter must prevent future-information leakage. Counterfactual actions must be separated from recorded exogenous events and documented in `TRACE_REPLAY_PLAN.md`.

### 3. Observation/calibration adapter

Input examples: longitudinal counts, node states, telemetry summaries, labels, or sparse measurements.

Output:

- observed state components and masks;
- units, sampling times, node/entity identities and aggregation windows;
- noise/missingness model;
- training/calibration, validation and test masks;
- quantities that are latent or inferred rather than observed.

Preprocessing parameters, imputers, scalers and feature selection must be fitted only on the training/calibration partition.

### 4. Testbed/emulation adapter

Input examples: cyber-range logs, packet captures, device/system telemetry, action acknowledgements and resource measurements.

Output:

- synchronized state/observation/action/event timeline;
- action issue, success/failure and completion times;
- latency, overhead, recovery and safety metrics;
- device/scenario/run identifiers;
- environment configuration and reproducibility record.

A testbed adapter supports claims about the declared testbed. Field generalization remains a separate claim.

## Adapter contract

Every adapter must complete `templates/ADAPTER_CONTRACT.yaml` and include:

- input dataset and schema;
- output model objects;
- unit and time alignment;
- entity/node alignment;
- missingness handling;
- label visibility and future-information policy;
- fit scope;
- validation checks;
- deterministic failure policy;
- source commit and licence review.

## Required validation

At minimum test:

1. schema rejection for malformed or missing required fields;
2. deterministic output for a fixed input/configuration;
3. unit/time conversion on a hand-checkable fixture;
4. no access to held-out labels or future rows;
5. graph direction/weight convention;
6. duplicate, self-loop and missing-entity handling;
7. row/count/checksum reconciliation;
8. explicit failure rather than silent coercion when semantics are ambiguous.

Use tiny synthetic fixtures in this SKILL repository. Do not bundle third-party datasets.

## Integration with the teaching family

- Foundation consumes graph objects, parameter arrays and canonical equations.
- Game learning consumes observation/action/event interfaces and repeated scenarios.
- Physics-informed methods consume observation masks, residual points and calibrated parameterizations.

A cross-layer project must prove that the same entity labels, state order, units, topology convention and time axis survive all adapters. Record the mapping in `REPOSITORY_EVIDENCE_MAP.csv` and `REALITY_LEDGER.csv`.

## Anti-patterns

- loading a CSV directly inside a neural-network loss function;
- using attack labels in the policy observation because they exist in the dataset;
- random row splitting of a temporal trace;
- fitting normalization on the entire dataset;
- deriving both train and test graphs from the same future-complete topology without disclosure;
- interpreting flow labels as node infection states without a defensible aggregation map;
- dropping failed/missing scenarios until the method appears stable;
- calling a trace-replay result an observed intervention effect.
