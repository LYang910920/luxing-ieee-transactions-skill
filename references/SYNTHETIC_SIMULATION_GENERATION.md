# Synthetic Simulation Generation and Validation

## Why synthetic simulation is acceptable

Synthetic simulation is appropriate when the paper's claim concerns a declared model, solution method, control policy, or sensitivity mechanism and suitable field observations do not exist. Its value comes from transparent scenario construction, independent checks, coverage, and reproducibility—not from calling the generated setting realistic.

## Scenario generator contract

Each generated scenario must be reproducible from a machine-readable specification containing:

```yaml
scenario_id: ...
scientific_question: ...
graph:
  source: observed | generated | statistic-matched
  family: ...
  seed: ...
  nodes: ...
  directed: ...
  weighted: ...
  parameters: {}
dynamics:
  model: ...
  parameter_profile: ...
  parameter_seed: ...
  initial_state_rule: ...
  attack_seed_rule: ...
decision:
  information_structure: ...
  action_timing: ...
  budget: ...
  horizon: ...
simulation:
  type: ode | gillespie | monte_carlo | agent_based | event_driven | sampled_closed_loop | hybrid
  numerical_settings: {}
  replications: ...
validation:
  independent_check: ...
  invariants: []
  failure_policy: ...
```

Do not embed undocumented random draws in plotting or training scripts.

## Scenario matrix

Cross, rather than cherry-pick, the scientifically material factors:

```text
topology family/instance
× size/density/community structure
× parameter profile/strength
× initial or attack seed placement
× budget/information condition
× controller/opponent
× random replication
```

Use a fractional design, Latin hypercube, or sensitivity method when the full Cartesian product is computationally infeasible. Record the sampling design and inclusion probabilities.

## Verification before comparison

Before evaluating a proposed method:

1. verify graph loading and adjacency orientation;
2. check state units, bounds, mass/conservation and reset maps;
3. compare analytic Jacobians with finite differences where available;
4. compare NumPy/Torch/sparse/dense forms on small cases;
5. verify no-action and fixed-action trajectories;
6. check time-step, mesh, tolerance, damping, and event-order sensitivity;
7. compare with an independent solver or stochastic ensemble;
8. test deterministic replay under a fixed seed;
9. retain and classify every failed or nonconvergent run.

A smoke run verifies execution; it is not performance evidence.

## Stochastic simulation

For Gillespie, Monte Carlo, agent-based, event-driven, RL, self-play, or trace-replay experiments:

- use independent scenario/training/evaluation seeds;
- report replication count and uncertainty;
- use common random numbers for paired comparisons when justified;
- keep test graphs/scenarios out of tuning and model selection;
- report distributional metrics, not only the best run;
- preserve training failure and catastrophic-policy cases;
- distinguish epistemic model uncertainty from Monte Carlo variation.

## ODE–stochastic consistency check

On bounded graphs and parameter regimes:

1. run the node-probability or mean-field ODE;
2. run a stochastic simulator with many independent realizations;
3. compare ensemble mean and uncertainty bands with the deterministic path;
4. explain approximation error caused by finite size, dependence, or closure;
5. do not present agreement on one configuration as universal equivalence.

## Synthetic observation generation

When testing inverse PINN/PIDL or state estimation:

- generate ground truth with an independent numerical simulator;
- apply a declared observation map;
- hide complete nodes/times/trajectories/graphs;
- inject noise using a documented distribution and seed;
- separate data points from collocation/residual points;
- compare recovered effective quantities, not only training loss;
- test model misspecification and non-identifiability;
- use “recovery on generated truth,” not “real-data calibration.”

## Output and provenance

Every run record should contain:

- repository commit and dirty state;
- scenario specification hash;
- graph/data checksum;
- software/platform/device;
- resolved parameters and seeds;
- solver/training settings;
- convergence and failure status;
- all primary and safety metrics;
- output artifact paths.

Generated raw outputs belong under ignored `artifacts/` or `results/raw/`; only compact derived tables needed for a public reproduction should be tracked when licensing and privacy permit.
