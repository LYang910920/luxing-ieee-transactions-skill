# Research-to-Paper Pipeline

## Deliverable graph

```text
Project Brief
  ↓
Full-Text Novelty Matrix ─────────────→ Claim-Evidence Matrix
  ↓                                         ↓
Scope Lock ───────────────────────────→ Exact Main Claim + Claim Type
  ↓                                         ↓
Evidence Track A–E ───────────────────→ Evidence Plan Audit
  ↓                                         ↓
Repository Layer Selection ───────────→ Repository Evidence Map
  ↓                                         ↓
Model Contract ──→ Data/Simulation Contract ──→ Reality Ledger
  ↓                      ↓                         ↓
Theorem/Proof Map   Dataset/Adapter Cards     Split/Leakage Plan
  ↓                      ↓                         ↓
Theorem-to-Code Map ─→ Verified Solver/Estimator/Environment
  ↓                                      ↓
Matched Baselines ─────────────────→ Experiment Matrix
  ↓                                      ↓
Results Log + Uncertainty ─────────→ Empirical Claim Ledger
  ↓                                      ↓
Figure/Table Plan ────────────────→ Manuscript Outline
  ↓
Draft → Manuscript Linter → Evidence Audit → Independent Technical Audit
  ↓
Rebuttal / Final Preflight / Safe Release
```

## Repository-layer flow

```text
Foundation
  canonical equations, graph/parameter semantics, PMP/FBS/game/impulse baselines
        ↓
Game learning (when feedback/adaptive agents are required)
  sampled environment, action timing, reward, repeated rollouts and deviations
        ↓
Physics-informed (when observations/parameters/mechanisms are incomplete)
  observation masks, residuals, calibration, missing-mechanism learning and rollout
```

Not every project needs every layer. The smallest coherent layer set is preferred.

## Evidence ladders

### Pure mechanistic numerical paper

```text
Track A:
model → theorem/conditions → verified solver → matched baselines → sensitivity/scaling
```

### Closed-loop learning paper

```text
Track A baseline + Track B:
canonical model → sampled environment → policy → repeated held-out simulation → physical metrics
```

### Real-topology or trace-driven paper

```text
Track A/B + Track C:
official topology/trace → adapter → reality ledger → holdout → semi-empirical comparison
```

### Real-data calibration paper

```text
Track D + Track A:
observation model → calibration/identifiability → held-out prediction → independent rollout
```

### Operational feasibility paper

```text
Track E + supporting B/C:
testbed/emulation → measured timing/overhead/failure → repeatability → bounded feasibility claim
```

## Stop conditions

Pause and resolve before advancing when:

- the closest paper may already solve the same problem;
- the proposed contribution is already present in the author's tutorial repositories;
- the model cannot express the operational decision;
- the main claim has no adequate evidence track;
- a dataset cannot map to states, parameters, observations, topology or exogenous events;
- data terms, privacy or leakage remain unresolved;
- simulator action/event timing or fidelity is undefined;
- theorem assumptions cannot be implemented or tested;
- the algorithm has no relevant matched baseline;
- a real-data estimator has no identifiability analysis or held-out validation;
- a game result lacks independent deviation/best-response evidence;
- the result changes materially with plausible mismatch;
- the headline claim has no direct theorem, experiment or measured evidence;
- required data/access/authorization is unavailable.

## Minimum viable paper

A strong paper may be intentionally narrow:

```text
one important decision
+ one justified model
+ one clean formal or estimation result
+ one reproducible solver/estimator/environment
+ one adequate evidence track
+ one decisive matched comparison
+ one honest validity boundary
```

Complexity, a neural module or a famous dataset is not a contribution unless it resolves a verified limitation.
