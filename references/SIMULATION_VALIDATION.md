# Simulation Verification, Validation, and Reporting

## Simulation taxonomy

| Type | Main object | Typical use | Primary risk |
|---|---|---|---|
| Deterministic numerical rollout | ODE/network trajectory | theorem/solver and control analysis | discretization or implementation error |
| Stochastic process | random transitions/arrivals | uncertainty and rare-event behavior | too few replications or misspecified noise |
| Agent-based simulation | heterogeneous agents and interactions | emergent behavior, local rules, adaptive actors | unvalidated micro-rules |
| Discrete-event simulation | timestamped queues/events | response timing, incidents, resource contention | event-order and service-time assumptions |
| Trace-driven replay | recorded event sequence | semi-empirical policy stress | counterfactual and label leakage |
| Network/system emulation | packets, hosts, services | overhead, latency, feasibility | testbed representativeness |
| Cyber range/hardware-in-loop | controlled operational stack | end-to-end behavior | safety, access, reproducibility, scope |

## Verification checklist

- State, action, event, and observation shapes are tested.
- The no-action simulation matches the canonical model.
- Flow-only controls do not create jumps; impulses create only declared jumps.
- Costs are integrated or charged at the correct times.
- Deterministic seeds reproduce identical runs.
- Stochastic seeds vary only the intended random components.
- Common random numbers are documented for paired policy comparisons.
- Extreme and zero-input cases behave as expected.
- Numerical and event-time resolutions are refined until conclusions stabilize.
- Failures, divergence, invalid states, and constraint violations remain in the log.

## Validation checklist

- Identify the statistic or phenomenon that the simulator must reproduce.
- Define the independent data or benchmark used for validation.
- Compare distributions, not only averages, where stochastic behavior matters.
- Validate separately across topology, timing, intensity, and observation dimensions.
- Use held-out networks, devices, scenarios, or time windows.
- Report where the simulator fails and how that limits the paper's claims.

## Replication and uncertainty

- Deterministic solvers require grid/tolerance/initialization sensitivity, not artificial seed repetition.
- Stochastic, agent-based, learning, and trace-sampling studies require repeated independent runs.
- Use paired seeds or common random numbers when comparing policies under the same scenario; also test independent scenarios.
- Report interval estimates or empirical distributions together with effect sizes.
- Retain failed or nonconvergent seeds; do not silently rerun until success.

## Trace-replay rules

- Split by complete time windows or scenarios before any feature construction.
- Do not use future labels, post-event features, or test-window statistics in the policy observation.
- State whether the trace controls only arrivals/observations or also defines transitions.
- A policy action not present in the trace is counterfactual and requires a response model.
- Evaluate sensitivity to alternative response models.

## Emulation/testbed rules

- Record hardware, network, software images, traffic generation, background load, and clock synchronization.
- Separate model parameters from measured system parameters.
- Measure action delay, success/failure, overhead, packet loss, and recovery.
- Use safe isolated environments and appropriate authorization.
- Do not infer production effectiveness from one small testbed without an explicit representativeness argument.
