# Personal Research Directions

## Research identity

Build decision-centred cyber and network systems research in which an operational security or social-system problem is converted into a closed, auditable chain:

```text
mechanism → intervention/strategy → formal result → verified computation → bounded decision insight
```

Prefer a narrow, defensible contribution with complete theory–code–evidence alignment over a broad framework assembled from fashionable components.

## Portfolio maturity

| Maturity | Directions | Interpretation |
|---|---|---|
| Established publication core | propagation dynamics, threshold/stability analysis, malware/APT defense, optimal control, differential and strategic games | Use as the default intellectual foundation and closest self-prior-work boundary. |
| Current expansion | impulse/hybrid control, cyber propaganda and rumor, awareness/opinion coupling, social-engineering malware, employee security compliance, hierarchical incentive/audit design, cost-effective response | Treat as active combinations with meaningful recent corpus support. |
| Emerging or repository-derived capability | topology-first node simulation, RL/MARL/MPC, attack-graph hybrids, PINN/PIDL, missing-mechanism learning | Add only when the question and data regime require them; do not imply equal corpus maturity. |
| Evidence-enabling layer | observed topology, traces, calibration, emulation, cyber range, hardware-in-loop | Use to close a named validity gap rather than as a standalone novelty claim. |

## Core direction portfolio

### 1. Cyber propagation, containment, and resilience

Study malware, mobile/IoT threats, APTs, social engineering, cyberbullying, rumor, propaganda, awareness, patching, quarantine, backup, and recovery as dynamical decision problems.

- Central question: how do propagation mechanisms, topology, human response, and resource limits change the timing and allocation of defense?
- Preferred formal objects: compartmental or node-level network dynamics, epidemic/awareness coupling, attack graphs, continuous–impulsive systems.
- Minimum evidence: invariants or well-posedness, verified solver, no-defense and simple-policy baselines, topology/parameter sensitivity, bounded security interpretation.
- Boundary: stylized dynamics do not establish observed attack rates or deployment effectiveness.

### 2. Optimal, impulse, and hybrid cyber control

Design cost-effective continuous, sampled, impulse, and hybrid interventions under explicit budgets, timing, and admissibility constraints.

- Central question: when and how should limited security resources be allocated?
- Preferred formal objects: optimal control, Pontryagin systems, impulse timing, hybrid reset maps, direct transcription or forward–backward sweep.
- Minimum evidence: necessary-versus-sufficient status, stationarity/residual checks, independent numerical comparison, grid/tolerance sensitivity, matched budgets.
- Boundary: a converged numerical trajectory is a configured solution, not a global optimality certificate.

### 3. Differential, Stackelberg, coalition, and repeated games

Model adaptive attackers, defenders, service providers, organizations, employees, or social actors with explicit information and strategy classes. The current corpus supports a research-architecture branch that couples organizational incentives and audits, employee compliance responses, and node-level intranet risk in a Stackelberg differential-game formulation.

- Central question: how do strategic timing, leadership, cooperation, or deviation incentives reshape cyber defense?
- Preferred formal objects: open-loop or feedback differential games, Stackelberg games, bilevel leader–follower optimization, FlipIt-style timing, coalition or partition stability, repeated/self-play interaction.
- Minimum evidence: declared solution concept, admissible strategies, response matrix, unilateral deviations or independently solved best responses, exploitability/stability diagnostics.
- Boundary: tested local deviations do not establish a general Nash, Stackelberg, or coalition-stability theorem.

### 4. Topology, heterogeneity, and network-scale intervention

Make node/edge semantics and structural heterogeneity part of the scientific question rather than an implementation detail.

- Central question: which conclusions depend on hubs, communities, direction, weights, temporal structure, or scale?
- Preferred formal objects: node-level and degree-class models, heterogeneous rates/costs, multilayer or temporal graphs, topology-aware controls.
- Minimum evidence: a topology card, deterministic preprocessing, multiple graph instances, matched structural controls, perturbation/rewiring tests, held-out graphs for generalization.
- Boundary: observed topology plus assumed dynamics is real-topology simulation, not real-world validation.

### 5. Feedback learning and multi-agent cyber control

Add RL, MARL, CTDE, self-play, or model-predictive feedback only when sampled observations, adaptation, or unknown opponents are central.

- Central question: can a feedback policy improve decisions under partial observation, stochasticity, or strategic adaptation?
- Preferred formal objects: MDPs, Markov games, hybrid environments, actor–critic or value-based policies, self-play and response analysis.
- Minimum evidence: parity with the canonical continuous model, exact action/event/reward timing, physical metrics beyond reward, matched information/budget/tuning, repeated held-out scenarios, failure retention.
- Boundary: reward improvement does not establish physical effectiveness, equilibrium, robustness, or field performance.

### 6. Physics-informed inverse problems and missing-mechanism learning

Use PINN, PIDL, inverse estimation, or PMP-informed learning when states are sparse/noisy, parameters are unknown, or a mechanistic component is missing.

- Central question: what exact state, parameter, function, or correction is unknown, and is it identifiable from the observation design?
- Preferred formal objects: inverse PINNs, physics-informed dynamic learning, learned corrections, neural control constrained by optimality systems.
- Minimum evidence: explicit observation model, separate data and collocation points, generated-truth recovery tests, held-out nodes/times/graphs, misspecification baselines, independent rollout, identifiability analysis.
- Boundary: residual consistency is not parameter truth; real-data fitting is calibration or effective-rate estimation unless ground truth and identifiability are established.

### 7. Evidence expansion from models to operational systems

Strengthen mechanistic papers through lawful observed topology, traces, calibration, emulation, cyber ranges, or hardware-in-the-loop only when they close a named validity gap.

- Central question: what stronger claim becomes supportable after adding this evidence source?
- Preferred progression: Track A verified numerics → Track B closed-loop simulation → Track C topology/trace evidence → Track D calibration/prediction → Track E measured feasibility.
- Minimum evidence: provenance, licences, data-to-model mapping, splits/leakage checks, uncertainty, failure cases, and a reality ledger.
- Boundary: adding more evidence types is not automatically stronger; select the smallest adequate track.

## Layer-selection doctrine

Start from the Foundation layer. Add another layer only when its scientific trigger is present.

| Trigger | Add | Do not add merely for |
|---|---|---|
| Canonical dynamics, control/game formulation, verified numerics | Foundation | every project already starts here |
| Sampled feedback, stochastic operation, adaptive opponent, repeated interaction | Game learning | fashion, algorithm count, or a stronger-looking title |
| Partial/noisy observations, unknown parameters, missing mechanism, learned optimality system | Physics informed | replacing a solvable mechanistic model with a neural surrogate |
| Observed topology or trace closes a structural/temporal validity gap | Track C | calling synthetic dynamics real-world data |
| Real observations support calibration and held-out prediction | Track D | claiming true parameters without identification |
| Testbed or field measurement supports feasibility | Track E | implying broad deployment or causal effectiveness |

When combining layers, preserve one state order, units system, adjacency convention, action timing, reset map, objective, and reality classification.

## Direction selection gates

Score a proposed direction only after a closest-full-text audit.

1. **Decision value:** identify the actor, action, cost, uncertainty, and consequence.
2. **Exact gap:** state what the closest work cannot represent, solve, verify, or observe.
3. **Minimal mechanism:** isolate the smallest interaction that creates the contribution.
4. **Formal tractability:** define a plausible theorem, optimality, equilibrium, or estimation ladder.
5. **Evidence feasibility:** identify the smallest adequate track and a decisive experiment.
6. **Asset fit:** reuse the three repository layers through pinned interfaces without treating them as novelty.
7. **Journal fit:** make the paper's center of gravity match TIFS, TDSC, TSMC, TNSE, or TCSS.
8. **Kill criteria:** name prior-art, proof, code, data, identifiability, or effect-size outcomes that would stop or narrow the direction.

Prefer a direction when all eight gates have defensible answers. Otherwise keep it as exploratory or record a NO-GO decision.

## Journal alignment

- **TIFS:** lead with adversary capability, security consequence, defender decision, and security-specific evaluation.
- **TDSC:** lead with dependable/secure system behavior, fault/threat scope, guarantees, overhead, and failure modes.
- **TSMC:** lead with integrated system dynamics, stability/feasibility, human–machine or cyber-physical interaction, and system interpretation.
- **TNSE:** lead with network representation, topology, heterogeneity, temporal structure, scale, and network-aware intervention.
- **TCSS:** lead with computational social mechanisms, awareness/opinion/incentives, ethical limits, and policy interpretation.

Verify current official submission rules before final formatting; these mappings describe research fit, not cached author instructions.

## Preferred contribution architecture

Use two to four dependent contributions:

1. formulate the decision problem and model;
2. characterize the formal solution or conditions;
3. develop the reproducible solver, estimator, or policy;
4. provide the evidence design and bounded finding.

Do not split one idea into decorative contributions. Do not claim a standard dataset, public topology, tutorial method, or generic neural component as novelty without a defensible new mapping or evaluation design.

## Personal execution preferences

- Treat supplied research bundles as working packages: unpack, locate the real workspace, and read its current routing files before acting.
- Reuse a supplied framework when it is a good foundation; do not rebuild from scratch without a reason.
- Default to scope lock → audit → validation → execution for a new “direction.”
- Perform writing, derivation, experiments, simulation, and release checks as an end-to-end chain when the request calls for them.
- Preserve adverse literature, failed runs, narrowed claims, pending gates, and NO-GO outcomes.
- Keep authenticated full-text provenance and access boundaries explicit; abstract-only review is not equivalent to full-text verification.
- Validate shipped archives and clean re-extractions, not only the working tree, before claiming a release is ready.

## Current provenance boundary

The style profile is calibrated from a 42-paper owner-provided key corpus, including 20 first/corresponding-author core-voice records and 17 IEEE Transactions papers. Corresponding status is a useful authorship signal but does not prove section-level drafting ownership; many contribution roles remain unconfirmed. The package records derived metrics and paper cards but no copyrighted full text. All 17 owner-priority selected Transactions rows now have private full text; one different-subfield row is explicitly owner-deprioritized. The broader publication universe, section-level voice attribution, venue-specific microstyle, and publisher-final verification of the 2026 TDSC-matched manuscript remain open; do not use `full-corpus-calibrated` until the full audit protocol passes.
