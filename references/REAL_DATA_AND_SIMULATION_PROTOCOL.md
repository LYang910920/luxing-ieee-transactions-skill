# Real-Data and Simulation Protocol

## 1. Begin with the claim, not the dataset

Write the exact claim and classify it as one of:

```text
mechanism
numerical method
control performance
approximate game stability
parameter/effective-rate calibration
predictive generalization
operational feasibility
causal effect
```

Select an evidence track from `EVIDENCE_TRACKS.md`. A dataset is admitted only when it measures or constrains an object needed by that claim.

## 2. Create a dataset card

For every external dataset record:

- canonical title and provider;
- official source, access date, version, DOI if any, and local checksum;
- licence/terms, citation requirement, redistribution status, and access restrictions;
- raw entities, units, timestamps, labels, topology, and sampling process;
- missingness, censoring, aggregation, class imbalance, and known collection artefacts;
- privacy, sensitive fields, ethics, and de-identification status;
- intended role: topology, event trace, observation model, parameter calibration, validation, or testbed benchmark.

Never commit restricted raw data to the SKILL repository. Store only cards, hashes, scripts, and derived aggregates when permitted.

## 3. Build the data-to-model map

Populate `DATA_TO_MODEL_MAP.csv` before fitting anything. Each row must connect:

```text
raw field or event
→ transformation/aggregation
→ model state, parameter, control, observation, exogenous input, or evaluation metric
→ unit and time scale
→ justification
→ uncertainty and leakage risk
```

Examples:

- timestamped malicious flows may define an exogenous attack-arrival process;
- host communication edges may define a real topology;
- flow labels may define observation likelihood or validation labels;
- telemetry may constrain latent compromise or workload proxies;
- an IDS label is not automatically an infected-state compartment.

If no defensible mapping exists, use the data only as a benchmark for a separate task or exclude it.

## 4. Distinguish four uses of real data

### Topology only

The graph is observed; dynamics, parameters, initial conditions, and controls are assumed or synthetic. Call this `real-topology simulation`.

### Trace replay

Recorded timestamps/events drive arrivals, exogenous modes, observations, or failures. Interventions are counterfactual unless the trace contains action/outcome data. Call this `trace-driven evaluation`.

### Calibration

Observed trajectories or aggregates estimate effective parameters or latent states. Use `calibrated` or `estimated`; reserve `recovered true parameter` for known synthetic truth or independently established ground truth.

### External validation

A model fitted elsewhere predicts a held-out time window, node set, graph, device, organization, or scenario. Define the shift explicitly.

## 5. Split before preprocessing

Choose splits that match the intended generalization claim:

- temporal: train/calibrate on earlier windows, test on later windows;
- node/host/device: hold out entire entities;
- graph/site/organization: hold out independent networks;
- scenario/capture: hold out complete attack or benign scenarios;
- parameter/topology seed: for synthetic or semi-synthetic studies.

Fit normalization, feature selection, imputation, label aggregation, and graph reduction on the training/calibration partition only. Record all split indices.

## 6. Calibrate and validate separately

A defensible real-data mechanistic study normally has:

1. a mechanistic model validated numerically without data;
2. a declared observation model;
3. parameter/latent-state estimation on calibration data;
4. identifiability or partial-identification analysis;
5. independent rollout on held-out data;
6. misspecification baselines, including homogeneous or reduced models;
7. uncertainty intervals or repeated fits;
8. residual maps and failure cases;
9. only then, counterfactual control or game simulation.

The counterfactual policy stage must propagate calibration uncertainty and model mismatch where feasible.

## 7. Simulation contract

Every simulator must record:

- simulator class: deterministic ODE, stochastic process, agent-based, discrete-event, trace replay, emulation, or testbed;
- state/action/event timing and units;
- graph/topology source;
- exogenous-event source;
- randomness, seeds, common-random-number policy, and replication count;
- warm-up, horizon, termination, reset, and failure behavior;
- verification against equations or known special cases;
- validation target and fidelity boundary;
- policy information, budget, and tuning parity;
- output logs, run manifest, and version/commit.

Use `SIMULATION_CONTRACT.yaml`.

## 8. Verification and validation

### Verification: did we implement the declared model correctly?

Examples:

- equation parity across NumPy/Torch or dense/sparse paths;
- mass, nonnegativity, bounds, and reset-map checks;
- analytic Jacobian versus finite difference;
- deterministic special cases;
- event ordering and interval-cost accounting;
- trace parser and timestamp alignment tests;
- packet/emulator configuration sanity.

### Validation: is the model/simulator adequate for the claimed use?

Examples:

- held-out trajectory or event statistics;
- degree, temporal, cascade, or traffic distribution matching;
- forecast error by host/node/time/scenario;
- testbed measurements of latency and action success;
- sensitivity to uncertain parameters and alternative observation maps.

A simulator can be verified but invalid for a particular claim. Report both.

## 9. Policy comparison rules

All methods must use, unless the research question explicitly differs:

- the same topology and event trace;
- the same observed information;
- the same action bounds and budget;
- the same horizon and cost accounting;
- the same test partitions;
- comparable tuning opportunity;
- common random numbers or paired scenarios when appropriate;
- repeated seeds/scenarios with uncertainty.

Training reward is not a physical outcome. Report exposure, peak/final adverse state, cost, budget, violations, runtime, and failure rate.

## 10. Counterfactual and causal wording

Allowed with calibrated or trace-driven simulation:

- `under the calibrated model`;
- `in counterfactual simulations`;
- `for the recorded trace conditions`;
- `the policy reduced simulated exposure by ...`;
- `the result suggests a candidate intervention pattern`.

Not allowed without a causal or prospective design:

- `the intervention caused ...`;
- `the strategy is effective in real deployments`;
- `the model recovers the true operational rate`;
- `the policy prevents attacks in practice`.

## 11. Minimum artefacts

```text
evidence/EVIDENCE_PLAN.json
data/DATASET_CARD.yaml
data/ADAPTER_CONTRACT.yaml
data/DATASET_DECISION_MATRIX.csv
data/DATA_TO_MODEL_MAP.csv
data/REAL_DATA_SPLIT_PLAN.csv
data/REALITY_LEDGER.csv
simulation/SIMULATION_CONTRACT.yaml
simulation/TRACE_REPLAY_PLAN.md
planning/EMPIRICAL_CLAIM_LEDGER.csv
reports/evidence_audit.md
```
