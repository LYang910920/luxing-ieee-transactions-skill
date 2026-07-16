# Repository Card — Cyber Control and Game Learning

## Role in the skill

Use this repository when the research question requires feedback decisions, sampled actions, learning, multiple strategic agents, or simulation-based policy evaluation.

## Stable doctrines to integrate

- Convert the continuous model to an MDP or Markov game explicitly; do not describe learning as a direct replacement for PMP.
- Define the order: pre-action observation, action choice, optional jump/reset, zero-order-hold flow parameters, ODE integration, interval reward.
- Keep running costs and one-time impulse costs separate.
- Match method to action and information structure: small discrete actions, parameterized/continuous actions, decentralized actors, centralized critics, or attacker-defender self-play.
- Always retain no-action, fixed, rule-based, budget-matched random, degree/risk, and oracle-style baselines where appropriate.
- Evaluate on held-out graph and parameter seeds, and report physical metrics in addition to training reward.
- For games, report response matrices and unilateral-deviation diagnostics. A rising reward curve or a finite policy response matrix is not an equilibrium proof.

## How it extends beyond one deterministic numerical trajectory

The sampled environments support repeated rollouts, randomized graph/state seeds, policy comparisons, multi-agent interaction, and held-out evaluation. This is a simulation layer rather than a single ODE/FBS solution. It can be extended to:

- stochastic attack arrivals or action failures;
- agent-based or event-driven state transitions;
- real-topology environments;
- trace-driven attack intensity, observation noise, or intervention schedules;
- testbed/emulation measurements for latency, overhead, and action feasibility.

## Required adapters for semi-empirical or empirical studies

- External adjacency/topology injection instead of only synthetic community-graph construction.
- A trace adapter that converts timestamped events into exogenous arrivals, observations, or attack modes without leaking future labels.
- A data-defined observation model and missingness/noise process.
- A common environment interface so every policy sees the same state, budget, horizon, and randomness.
- A policy-free replay baseline and an off-policy evaluation warning when counterfactual actions are not observed.

## Claim boundaries

- Held-out simulator performance supports generalization under the tested simulator shifts, not robustness guarantees.
- Trace replay supports performance on recorded event sequences, not prospective operational effectiveness.
- Approximate game stability must be scoped to the tested opponent/policy set unless best responses are solved independently.
