# Evidence Tracks: Numerical, Simulation, Real Data, and Testbed

A paper does not become stronger merely by adding more evidence types. Select the **smallest evidence track that can support the main claim**, then add a second track only when it closes a documented validity gap.

## Track A — Mechanistic numerical evidence

Typical components:

- ODE/network model;
- theorem or optimality conditions;
- FBS/direct optimization/numerical solver;
- invariant, residual, grid, and baseline checks;
- synthetic graphs or parameter sweeps.

Supports:

- mathematical mechanism;
- existence/necessary-condition results under assumptions;
- numerical behavior of the configured model;
- algorithmic convergence or efficiency under tested settings.

Does not support by itself:

- field calibration;
- operational effectiveness;
- causal intervention effects;
- broad equilibrium or robustness claims.

Primary repository layer: Foundation.

## Track B — Stochastic, agent-based, or closed-loop simulation

Typical components:

- repeated randomized rollouts;
- sampled controls or impulses;
- stochastic arrivals, failures, delays, or observations;
- agent-based or event-driven transitions;
- feedback policy or multi-agent learning;
- uncertainty across seeds and scenarios.

Supports:

- closed-loop policy behavior;
- distributional performance under declared simulator assumptions;
- sensitivity to stochasticity and adaptive opponents;
- simulation-based game diagnostics.

Primary repository layer: Game learning, with the Foundation mechanism.

## Track C — Real-topology or trace-driven semi-empirical simulation

Typical components:

- real communication/social/Internet graph with synthetic or calibrated dynamics;
- real temporal traces used for event arrivals, observations, attack modes, or replay;
- synthetic interventions over real topology or recorded exogenous events;
- topology and trace holdouts.

Supports:

- sensitivity to real structural or temporal patterns;
- performance on recorded trace conditions;
- stronger external validity than purely synthetic topology.

Mandatory wording boundary:

- `real-topology simulation`, `trace-driven evaluation`, or `semi-empirical study`;
- not `real-world validated control` unless intervention effects were actually observed or tested.

Primary repository layers: Foundation graph loader + Game learning simulator; Physics-informed layer when traces calibrate parameters or observations.

## Track D — Real-data calibration and predictive validation

Typical components:

- observed longitudinal, node, flow, telemetry, or cascade data;
- explicit data-to-model mapping;
- inverse estimation or constrained calibration;
- temporal/node/topology holdouts;
- uncertainty and misspecification baselines;
- independent forward rollouts.

Supports:

- fit and prediction under the specified observation model;
- effective-rate or parameter calibration;
- data-informed counterfactual simulation, with explicit causal limits.

Does not automatically support:

- structural parameter truth;
- causal treatment effects;
- deployment effectiveness;
- global identifiability.

Primary repository layer: Physics-informed, anchored to Foundation and optionally followed by Game learning.

## Track E — Emulation, cyber range, hardware-in-the-loop, or field evidence

Typical components:

- packet/system/network emulation;
- controlled cyber-range experiments;
- real devices or hardware-in-the-loop;
- measured latency, overhead, action success, recovery, and failure;
- prospective or operational study with permissions and ethics.

Supports:

- implementation feasibility under testbed conditions;
- system-level overhead and timing;
- limited operational claims proportional to the design.

Field or causal claims require an appropriate study design, access authorization, safety review, privacy/ethics checks, and an explicit counterfactual strategy. Simulation alone cannot establish them.

## Recommended combinations

| Main claim | Minimum track | Strong extension |
|---|---|---|
| New control/game formulation | A | C for topology realism |
| Feedback policy advantage | B + A baseline | C or E |
| Approximate game stability | B + independent deviations | A best-response check |
| Parameter/effective-rate estimation | D + A solver | C topology/trace transfer |
| Missing-mechanism correction | D | B counterfactual simulation |
| Real-topology scalability | C + A | multiple topology families |
| Operational feasibility | E | B/C for stress coverage |
| Causal intervention effect | appropriate field/quasi-experimental design | mechanistic simulation as supporting, not primary, evidence |

## Stop rules

Stop and redesign when:

- the dataset cannot be mapped to model states, observations, parameters, or exogenous inputs;
- real topology is being used to imply real intervention effects;
- training and test points leak across time, nodes, hosts, or scenarios;
- a simulator has not been verified against the canonical equations;
- policy comparisons use different budgets, information, traces, or random conditions;
- a real-data model has no held-out validation or misspecification baseline;
- a counterfactual control claim is written as an observed causal result.
