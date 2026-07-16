# Lecture-to-Paper Blueprints

These blueprints show how the three repository layers can produce stronger IEEE Transactions studies without adding unnecessary complexity.

## Blueprint 1 — Theory-first control on real topology

```text
real network topology
→ Foundation graph/degree/node model
→ optimal-control or differential-game formulation
→ theorem/necessary conditions
→ FBS or direct solver
→ matched synthetic-topology and homogeneous baselines
→ topology sensitivity and scalability
```

Minimum paper claims:

- a new formulation or theoretical/numerical result;
- performance under specified real topologies;
- no field-calibration claim unless rates and outcomes are observed.

Best suited to: TSMC, TNSE, TIFS/TDSC when the security mechanism is central.

## Blueprint 2 — Feedback learning with trace-driven stress

```text
canonical continuous model
→ sampled MDP/Markov game
→ FBS/rule/random baselines
→ learned feedback policy
→ real event trace drives arrivals, attack modes, observation gaps, or failures
→ held-out time/scenario evaluation
→ deviation and failure diagnostics
```

Minimum paper claims:

- closed-loop performance in the declared simulator;
- performance for held-out trace conditions;
- no claim that the unobserved intervention outcome was actually realized.

## Blueprint 3 — Real-data calibration plus counterfactual control

```text
real longitudinal observations
→ data-to-model and observation map
→ inverse estimation / constrained PINN
→ held-out forecast and misspecification audit
→ parameter/latent uncertainty
→ calibrated mechanistic simulator
→ FBS and/or learned control
→ counterfactual policy sensitivity
```

Minimum paper claims:

- calibration/predictive validity within the dataset;
- counterfactual model-based results;
- explicit separation from causal effectiveness.

## Blueprint 4 — Partial model + PIDL + adaptive defense

```text
known mechanistic core
+ learned regularized correction
→ known-only / correction / flexible-model ablation
→ held-out trace or trajectory validation
→ corrected simulator
→ adaptive feedback policy
→ robustness to correction uncertainty
```

Minimum paper claims:

- predictive value of the correction under held-out data;
- improved simulated decision performance under uncertainty;
- no statement that the learned correction is the unique causal mechanism.

## Blueprint 5 — Testbed feasibility bridge

```text
Foundation or calibrated model
→ sampled policy environment
→ emulator/cyber-range adapter
→ action delay, overhead, success/failure measurements
→ simulator re-calibration
→ repeated testbed scenarios
→ feasibility and scope-limited operational interpretation
```

This is the appropriate route when the main contribution includes implementation timing, packet/system overhead, or device constraints that an ODE-only study cannot establish.

## Selection rule

Use one primary blueprint. A second blueprint is justified only when it closes a named reviewer-facing gap, such as topology realism, feedback operation, sparse-data calibration, or implementation feasibility.
