# Evidence Ladder When Real Attack/Propagation Data Are Unavailable

## Decision rule

Do not postpone the entire study while searching indefinitely for an ideal dataset. Freeze the claim first, then choose the highest feasible evidence design.

```text
Can observed intervention outcomes be obtained?
  yes → Track D/E as appropriate
  no
    Can a timestamped trace or temporal graph be obtained?
      yes → Track C trace-driven counterfactual simulation
      no
        Can a semantically compatible observed topology be obtained?
          yes → Track C real-topology simulation
          no
            Can an observed degree/size/community distribution be obtained?
              yes → T4 statistic-matched synthetic simulation
              no → T5 controlled multi-family synthetic simulation
```

At every lower rung, narrow the claim rather than decorating the study with stronger adjectives.

## Minimum publishable package by rung

### Real-topology simulation

- official topology source and licence;
- topology card and deterministic adapter;
- explicit synthetic parameter/dynamics declaration;
- matched synthetic graph controls;
- multiple parameter and attack-seed scenarios;
- topology perturbations and uncertainty;
- node-level baseline comparisons.

### Trace-driven counterfactual simulation

- timestamp and entity mapping;
- prevention of future-label leakage;
- separation of recorded exogenous events from simulated intervention effects;
- replay order and response assumptions;
- scenario holdout;
- uncertainty and fidelity boundary.

### Statistic-matched synthetic simulation

- documented target statistics;
- generator/fitting method;
- goodness-of-match table;
- multiple generated instances;
- sensitivity to unmatched statistics;
- no claim of observed real topology.

### Fully controlled synthetic simulation

- multiple graph families;
- multiple sizes and seeds;
- broad parameter/initial-condition design;
- independent solver/simulator check;
- matched baselines and uncertainty;
- explicit statement that conclusions are model-conditional.

## Stop conditions

Pause or redesign when:

- no graph semantics match the model;
- the only available dataset would require inventing a state mapping;
- licensing or privacy terms are unresolved;
- a proposed claim requires observed intervention outcomes that cannot be obtained;
- results disappear under a reasonable topology or parameter perturbation;
- an algorithm only works on one favorable seed;
- the main result depends on unreproducible manual preprocessing.
