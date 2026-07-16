# IEEE Transactions Quality Gates

A failed item marked **blocking** stops claim freezing, manuscript finalization or release until resolved. `Not applicable` requires a one-line justification.

## Gate 0 — Identity, target and current rules

- [ ] Correct target journal, article type and submission stage.
- [ ] Current official author instructions checked and dated.
- [ ] Template, anonymization, supplementary, data/code, disclosure and ethics rules verified.
- [ ] No stale page-limit, fee or policy assumption copied from memory.

## Gate 1 — Research question, claim type and scope

- [ ] One operational decision problem is stated.
- [ ] Main research question is falsifiable.
- [ ] Main claim is written exactly and assigned a claim type.
- [ ] Model resolution and solution concept are justified.
- [ ] Optional complexity is excluded or clearly secondary.
- [ ] Main claim is no broader than assumptions, evidence track and evaluation.

## Gate 2 — Novelty and citation integrity

- [ ] Closest full texts read.
- [ ] Negative/overlapping evidence logged.
- [ ] Novelty separated into problem, model, theory, algorithm, simulator, data, evaluation design and finding.
- [ ] The owner's prior tutorial/repository components are treated as prior artefacts, not silently relabelled as new contributions.
- [ ] `First/novel/innovative` has dated search support.
- [ ] Every citation exists and supports the exact sentence.
- [ ] References, DOI, year, venue and author order verified.

## Gate 3 — Three-repository integration

- [ ] Required Foundation, Game-learning and Physics-informed layers are selected explicitly.
- [ ] Repository source paths and pinned commits are recorded.
- [ ] State names/order, units, topology convention, timing, action semantics and objectives remain consistent across layers.
- [ ] Repository-derived doctrine is paraphrased and traced; tutorial prose/code/figures are not copied into the SKILL or manuscript without a separate rights review.
- [ ] Reference implementations are not claimed as manuscript novelty.
- [ ] Repository licence/notice changes have been checked before release.

## Gate 4 — Model and theory

- [ ] States, units, topology, observations, actions and constraints are defined.
- [ ] Each state and cumulative quantity has one stable semantic meaning: stock, probability, event flow, integral, or unique entity count.
- [ ] Flow, event and reset maps are dimensionally and logically consistent.
- [ ] Boundary directions, conservation identities, persistent inputs and zero/upper-control cases preserve the declared feasible set.
- [ ] Exact dynamics are separated from mean-field, independence, moment-closure, continuum or agent-level approximations.
- [ ] Assumptions have physical/operational meaning.
- [ ] Theorem ladder has no circular dependency.
- [ ] Every closed-form/numerical root is substituted into the original equations, screened for feasibility and checked by residual.
- [ ] Extra threshold/sign conditions are simplified against prior assumptions; redundant or contradictory conditions are removed.
- [ ] Bifurcation names require branch, transversality/normal-form and stability-exchange evidence, not root counting alone.
- [ ] Necessary versus sufficient, local versus global, continuous versus sampled and open-loop versus feedback scope is explicit.
- [ ] Proof sketches do not skip the step that carries the headline claim.

## Gate 5 — Evidence-track adequacy

- [ ] Primary Track A, B, C, D or E is selected and justified.
- [ ] The chosen track is sufficient for the exact main claim.
- [ ] Stronger evidence is not implied when only a weaker track is present.
- [ ] Secondary tracks close a documented validity gap rather than decorate the paper.
- [ ] `EVIDENCE_PLAN.json` passes with no blocking or unresolved major findings.

## Gate 6 — Data provenance, mapping and leakage

Required whenever real topology, traces, observations or testbed measurements are used.

- [ ] Official source, provider, version/DOI/checksum and access date recorded.
- [ ] Licence/terms, citation and redistribution rules checked.
- [ ] Privacy, sensitive-data, malware and ethics risks reviewed.
- [ ] Collection environment, sampling process, units, timestamps, entities and labels documented.
- [ ] Every raw field/event maps to a model state, parameter, observation, topology element or exogenous input.
- [ ] `REALITY_LEDGER.csv` separates observed, inferred/calibrated, assumed, generated and counterfactual quantities.
- [ ] Adapter contract records schema, unit/time/entity alignment, missingness, label visibility and failure policy.
- [ ] Temporal/node/host/graph/capture/scenario splits match the intended claim.
- [ ] Preprocessing, scaling, imputation and feature selection are fitted on training/calibration data only.
- [ ] Future, duplicate, entity, graph and label leakage have been audited.
- [ ] Data limitations and selection bias are stated.

**Blocking:** a real source with unknown terms, no model mapping, no defensible holdout or unaudited leakage.

## Gate 7 — Simulation and testbed validity

Required whenever simulation, replay, emulation or a testbed is used.

- [ ] Simulator type and canonical mechanism are declared.
- [ ] Observation → action → event/reset → flow/integration → reward/measurement order is explicit.
- [ ] Sampled actions, continuous-time controls and impulses are not conflated.
- [ ] Delay histories, waiting-cohort survival/exit, impulse ordering, reset feasibility and non-Zeno behavior are explicit when applicable.
- [ ] Random components, distributions, seeds and scenario generation are documented.
- [ ] Equation, invariant, parser/event and special-case verification checks pass.
- [ ] Validation target and fidelity boundary are explicit.
- [ ] Stochastic/learning/replay studies use adequate independent repetitions or scenarios.
- [ ] Failed, divergent and non-improving runs are retained.
- [ ] Each figure/table records the exact model version, theorem/condition, parameters, initial state/history, seed, legend and expected endpoint.
- [ ] Common random numbers or paired scenarios are used where they improve fairness.
- [ ] Trace replay separates recorded exogenous events from simulated counterfactual effects and hides future labels.
- [ ] Testbed work records environment, device/scenario/run, action success/failure, latency, overhead and recovery.

**Blocking:** undefined action/event timing, no fidelity boundary, or a replay/testbed claim that exceeds measured quantities.

## Gate 8 — Algorithm, estimator and code

- [ ] Every theorem assumption and data transformation is implemented, tested or named as a mismatch.
- [ ] Objective/payoff, Hamiltonian, adjoint, stationarity condition, projection and implementation share one symbol/sign ledger.
- [ ] State, control, adjoint, delayed and advanced-time indices match the mathematical update time exactly.
- [ ] Projection, constraints, discretization, stopping criteria and failure handling are specified.
- [ ] Grid, integrator, interpolation, relaxation, maximum iterations, residuals and convergence diagnostics are reported where applicable.
- [ ] No-control, deterministic, fixed, random/rule and relevant domain baselines exist.
- [ ] An independent solver, rollout, oracle or special case checks headline results where applicable.
- [ ] Closed-form branches, derived coefficients and gradients have symbolic or numerical unit tests.
- [ ] `Optimal/equilibrium/recovery` claims have independent evidence for the declared notion.
- [ ] Seeds, resolved configs, environment, data version/hash and commit/archive identifier are recorded.
- [ ] Figure and table generation is reproducible.

## Gate 9 — Experimental fairness and uncertainty

- [ ] Budgets, observations, horizons, traces and tuning opportunities are matched across methods.
- [ ] Zero/no-action and simple constant policies are included unless a documented reason makes them inapplicable.
- [ ] Random functional controls/policies have a finite-dimensional parameterization or declared measure, plus grid/basis, distribution, smoothness/interpolation and seeds.
- [ ] Baselines are relevant and competently tuned.
- [ ] Ablations map to contribution claims.
- [ ] Sensitivity/robustness covers key parameters, topology, observation and model mismatch.
- [ ] Sensitivity curves are not called robustness without out-of-design evaluation; structural monotonicity is not presented as empirical or causal evidence.
- [ ] Cross-size and cross-horizon objectives report per-entity/per-time or otherwise justified normalization.
- [ ] Nested feasible sets, direct objective scaling and parameter-role coupling are identified before interpreting monotone scans.
- [ ] Complete time/node/host/graph/capture/scenario axes are held out where required.
- [ ] Uncertainty is reported across seeds, instances, fits or measurement windows.
- [ ] Scalability includes size, runtime/memory and hardware context.
- [ ] Failure cases and non-improvements are reported.
- [ ] Probability-one language has an explicit probability space and theorem/statistical design; many successful runs alone are insufficient.
- [ ] Every result claim points to a logged metric, figure, table or theorem.

## Gate 10 — Game and control-specific claims

- [ ] FBS/PMP results are scoped as necessary conditions/configured numerical solutions unless stronger conditions are proved.
- [ ] Terminal transversality, trajectory endpoints and numerical boundary handling agree.
- [ ] Pointwise control caps, cumulative budgets, state/resource constraints and forced lower bounds are distinguished.
- [ ] Feedback and open-loop policies are not compared as if they solve the identical information problem without disclosure.
- [ ] Game claims use response matrices plus unilateral deviations or independently solved best responses.
- [ ] Approximate stability/exploitability is scoped to the tested policy/opponent set.
- [ ] Reward improvement is accompanied by physical/system metrics.
- [ ] Intervention cost, running cost and impulse cost are accounted for consistently.
- [ ] Information-gathering controls have an evidence/belief state; a memoryless instantaneous effect is not mislabeled as testing, learning or sensing.

## Gate 11 — Calibration, prediction and causal language

- [ ] The unknown object and observation model are explicit.
- [ ] Observed points and residual/collocation points are separated.
- [ ] Identifiability or partial-identification limitations are assessed.
- [ ] Real-data fitting is described as calibration/effective-rate estimation unless true parameters are independently known.
- [ ] Residual consistency is not used as proof of parameter truth.
- [ ] Held-out prediction/rollout and misspecification baselines are reported.
- [ ] Counterfactual control results are not described as observed treatment effects.
- [ ] Test-set or future-label tuning, threshold selection and preprocessing leakage are excluded and documented.
- [ ] Operational feasibility uses Track E measurements.
- [ ] Causal wording is supported by a prospective, randomized, quasi-experimental or otherwise defensible causal design.

## Gate 12 — Writing architecture and author style

- [ ] Abstract contains gap, model/problem, theory/algorithm, evidence track, evaluation and bounded result.
- [ ] Introduction ends with verifiable contributions.
- [ ] Related work compares mechanisms and evidence, not only topics.
- [ ] Data/simulation contract is visible when material.
- [ ] Model precedes dense derivation.
- [ ] Results use observation → interpretation → uncertainty/claim boundary.
- [ ] Textual curve directions, limits, equilibrium labels, experiment numbers and figure captions are checked against generated artifacts.
- [ ] “Cumulative” is defined as an integral, event count or deduplicated entity count, with units.
- [ ] Conclusion includes limitations and introduces no new claim.
- [ ] Acronyms are necessary, defined and readable.
- [ ] Sentence rhythm is varied; no cluster of 45+ word sentences.
- [ ] Connectors express real logic and are not repeated mechanically.
- [ ] Legacy errors listed in the style profile are absent.
- [ ] Personal style never overrides clearer IEEE English.

## Gate 13 — Claim language

- [ ] `first` / `novel` / `innovative` evidence-gated.
- [ ] `optimal` scoped to the proved or computed notion.
- [ ] `equilibrium` verified under the declared solution concept.
- [ ] `significant` defined statistically or materially with numbers.
- [ ] `scalable` supported by scaling evidence.
- [ ] `robust` scoped to measured shifts or accompanied by a formal guarantee.
- [ ] `practical` supported by constraints, timing and implementation/testbed evidence.
- [ ] `outperform` based on fair repeated comparison.
- [ ] `real-world validated` avoided for real-topology or trace-driven simulation.
- [ ] `recovered parameters` avoided for unidentifiable real-data calibration.
- [ ] `causal` matches the study design.
- [ ] `almost surely` or probability-one language has an explicit probability contract and formal support.
- [ ] `uniform random function/control/policy` has a finite-dimensional sampling contract or declared measure.
- [ ] `solved successfully` is replaced or supported by sufficiency, a certified gap, or an independent solver.

## Gate 14 — Ethics, access and release

- [ ] No fabricated content or hidden closest prior work.
- [ ] Data, malware, human/social and operational implications handled appropriately.
- [ ] AI/tool use disclosed as required by current policy.
- [ ] No copyrighted paper PDF, tutorial source, raw dataset, PCAP, checkpoint or confidential review file in Git/release.
- [ ] No nested copies of the three tutorial repositories.
- [ ] No password, cookie, token, browser state or unrelated personal data.
- [ ] Release manifest and checksums inspected.

## Decision

- Any failed novelty, validity, citation, data licence/privacy, leakage, simulator timing/fidelity, copyright, credential or claim–evidence item is **blocking**.
- Reproducibility, uncertainty, limitations or language failures are at least **major warnings** and normally block submission until resolved.
