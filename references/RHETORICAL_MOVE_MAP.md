# Rhetorical Move Map

## Whole-paper move sequence

```text
M1 operational stakes and decision maker
M2 mechanism/topology/information/timing difficulty
M3 closest literature families
M4 modeling gap + intervention/solution/evidence gap
M5 named model/framework/problem
M6 formal solution characterization
M7 algorithm/estimator/policy
M8 decisive evidence
M9 bounded security/policy/operational implication
M10 limitations and external-validity boundary
```

M1–M9 are strongly represented in the current corpus. M10 is a required refinement even when older papers omitted a dedicated limitations section.

## Abstract

| Move | Question answered | Typical length |
|---|---|---:|
| A1 | Why does the problem matter? | 1–2 sentences |
| A2 | What exactly is unresolved? | 1 sentence |
| A3 | What model/framework is proposed? | 1–2 sentences |
| A4 | What control/game/optimization object is solved? | 1 sentence |
| A5 | What is derived or established? | 1–2 sentences |
| A6 | How is it computed? | 1 sentence |
| A7 | Where/how is it evaluated? | 1 sentence |
| A8 | What is the strongest result and implication? | 1–2 sentences |

Do not include A5 or A6 when the paper has no genuine theory or algorithm contribution.

## Introduction

| Move | Required content |
|---|---|
| I1 | threat/system context, affected actor, decision |
| I2 | why existing operational intuition is insufficient |
| I3 | literature family A and limitation |
| I4 | literature family B and limitation |
| I5 | consolidated dual gap |
| I6 | proposed approach and fit |
| I7 | contribution objects in model → theory → algorithm → evidence order |
| I8 | organization, if useful |

## Related work

Organize by the dimensions that determine the current claim:

- mechanism/state representation;
- topology resolution;
- intervention timing;
- control/game/learning solution notion;
- information/observability;
- evidence type.

End each family with a precise boundary, not a generic criticism.

## Model and problem formulation

```text
entities and states
→ units and topology semantics
→ flow/jump/event timing
→ controls/actions and information
→ objective/payoff and budget
→ admissible set
→ solution concept
→ formal problem statement
```

## Theory

```text
assumptions
→ basic invariants/well-posedness
→ theorem/necessary conditions
→ dependency/proof
→ numerical residual or implementation meaning
→ scope and non-guarantees
```

## Algorithm

```text
inputs/configuration
→ initialization
→ state/costate/actor/estimator update order
→ projection/reset/constraints
→ stopping residual
→ complexity/resource use
→ convergence/failure record
```

## Experiments

```text
E1 scientific question and claim
E2 topology/data/simulator provenance
E3 independent sanity/verification
E4 baselines and fairness
E5 primary comparison
E6 ablation/sensitivity
E7 graph/parameter/seed/holdout stress
E8 convergence/scalability/uncertainty/failures
E9 bounded interpretation
```

## Result paragraph

```text
figure/table and metric
→ quantified observation
→ mechanism or strategy explanation
→ claim boundary
```

## Conclusion

```text
decision problem
→ model/theory/algorithm chain
→ strongest verified result
→ implication
→ limitations and specific next step
```
