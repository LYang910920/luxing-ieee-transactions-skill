# Section Playbooks

## Title

Use the decision/security problem plus the mechanism or solution notion. A colon is appropriate when it separates the problem from a specific method. Gate `optimal`, `robust`, `scalable`, `practical`, and `real-world`.

## Abstract

Target 190–240 words and 8–11 sentences unless the current journal rules differ. Use the move sequence in `RHETORICAL_MOVE_MAP.md`. Include the evidence setting and strongest verified result. Do not write an aspiration, generic benefit, or unsupported novelty claim.

## Introduction

Begin with the decision maker and operational consequence. Explain the difficulty created by topology, adversarial adaptation, timing, information, human behavior, or resource constraints. Synthesize the nearest literature into claim-relevant families. State a dual gap, then introduce the exact formal object. Contributions should name model/problem, theory, algorithm, and evidence.

## Related work

Compare scope, assumptions, topology, timing, solution concept, and evidence. Use full text for the closest papers. Record negative evidence. A novelty statement must correspond to a row in the novelty matrix.

## System model

Define node/entity meaning, state order, units, graph semantics, parameters, flow/jump equations, observation, and interventions. For node-level work, complete `TOPOLOGY_CARD.yaml` and state whether `A[i,j]` means `j` influences `i`.

## Problem formulation

State admissible controls/actions, information structure, bounds, horizon, budget, running/terminal/jump costs, strategy class, and exact solution concept. Do not use `optimal` or `equilibrium` before the object is defined.

## Data and simulation contract

Separate:

```text
observed
derived
calibrated/inferred
assumed
synthetic
counterfactual
```

State topology/data source, preprocessing, split, timing, simulator, random components, verification, validation target, fidelity boundary, and prohibited claims.

## Theory

Use a dependency ladder. Distinguish necessary from sufficient conditions. Link every assumption to code/configuration. Add residuals, special cases, numerical consistency, or counterexample searches.

## Algorithm

Describe input, initialization, update order, projection/reset, stopping criterion, tolerance, complexity, and failure behavior. Report the actual residual used to claim convergence.

## Experimental setup

Declare:

- research question and claim;
- topology/data/simulator provenance;
- graph, parameter, and scenario splits;
- baselines and information/budget fairness;
- metrics and units;
- random seeds/replications;
- hardware/software/commit;
- uncertainty and failure policy.

When real trajectories are unavailable, use the topology-first ladder rather than implying field validation.

## Results

For each figure/table:

1. identify the comparison;
2. report magnitude and uncertainty;
3. explain the model/control/topology mechanism;
4. state the bounded conclusion.

Retain nonconvergent and unfavorable cases. Separate algorithm convergence from scientific outcomes.

## Discussion

Connect results to the decision problem. Distinguish mathematical, numerical, semi-empirical, predictive, and operational evidence. Explain which assumptions could reverse the conclusion.

## Limitations

At minimum discuss:

- model abstraction and parameter uncertainty;
- topology semantics and preprocessing;
- observability/identifiability;
- information and action timing;
- optimality/equilibrium scope;
- simulation fidelity and external validity;
- computational scale;
- data/testbed/deployment limitations.

## Conclusion

Recap the closed chain: decision problem → model → theory → algorithm → evidence. State the strongest verified implication and the main limitations. Do not introduce new claims.
