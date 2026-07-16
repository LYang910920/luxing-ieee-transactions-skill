---
name: luxing-ieee-transactions
description: Plan, execute, write, audit, revise, and rebut IEEE Transactions research in Lu-Xing Yang's personal research style. Use for TIFS, TDSC, TSMC, TNSE, or TCSS work involving cybersecurity, malware or APT propagation, cyber-social dynamics, optimal or impulse control, differential/Stackelberg/coalition games, network topology, RL/MARL, PINN/PIDL, real-data or simulation evidence, theorem-to-code checks, novelty audits, manuscript drafting, reviewer responses, or requests such as “我的论文风格”, “开始做研究方向”, “写IEEE论文”, and “仔细阅读分析并开始推导、实验和仿真”.
---

# Lu-Xing Yang IEEE Transactions Research

## Mission

Turn one defensible decision problem into an auditable paper chain:

```text
operational problem
→ full-text novelty boundary
→ minimal model and solution notion
→ theorem / algorithm / estimator
→ adequate evidence track
→ reproducible results
→ calibrated IEEE prose
→ claim-by-claim preflight
```

Apply this priority order:

1. Preserve truth, mathematical validity, evidence, ethics, privacy, and copyright.
2. Follow current official journal and disciplinary requirements.
3. Respect the frozen project scope and reproducibility contract.
4. Apply the current personal style profile as a soft guide.
5. Correct rather than imitate historical language defects.

Do not add a dataset, neural module, simulator, player, or theorem merely to make the work appear more sophisticated.

## Route the request

Read only the resources needed for the current task.

| Request | Read first | Produce |
|---|---|---|
| New topic, direction, or supplied research package | `references/PERSONAL_RESEARCH_DIRECTIONS.md`, `references/RESEARCH_PIPELINE.md` | scope lock, research question, claim, kill criteria |
| Personal style, outline, drafting, or revision | `references/PERSONAL_STYLE_PROFILE.md`, `references/RHETORICAL_MOVE_MAP.md`, `references/SECTION_PLAYBOOKS.md` | section plan or evidence-bounded prose |
| Target-journal fit | `references/JOURNAL_OVERLAYS.md`, `references/IEEE_TRANSACTIONS_COMMON.yaml` | venue-specific framing and a dated official-rule check |
| Novelty or literature audit | `references/FULL_CORPUS_AUDIT_PROTOCOL.md`, `references/PUBLICATION_ENTRY_POINTS.md` | search log, closest-work matrix, negative evidence, must-cite list |
| Theorem, optimal control, game, delay, impulse, or cross-paper consistency claim | `references/FULLTEXT_CORPUS_DERIVED_DOCTRINE.md`, `references/QUALITY_GATES.md`, `references/CLAIM_LANGUAGE_RULES.yaml` | mechanism ledger, assumption ladder, proof/code map, residual or deviation checks |
| Topology or no-real-data experiment | `references/EVIDENCE_LADDER_NO_REAL_DATA.md`, `references/TOPOLOGY_FIRST_EXPERIMENT_PROTOCOL.md` | T1–T5 decision, topology card, scenario matrix, claim boundary |
| Real data, traces, calibration, or simulation | `references/REAL_DATA_AND_SIMULATION_PROTOCOL.md`, `references/SIMULATION_VALIDATION.md` | dataset/adapter/split/reality contracts and validation plan |
| RL/MARL or physics-informed extension | `references/PERSONAL_RESEARCH_DIRECTIONS.md`, `references/THREE_REPOSITORY_INTEGRATION.md` | justified layer selection and canonical-model bridge |
| Rebuttal or final review | `references/REBUTTAL_PLAYBOOK.md`, `references/QUALITY_GATES.md` | response ledger or READY / READY WITH WARNINGS / NOT READY decision |

Resolve all paths relative to this skill directory. Treat source papers, repository snapshots, target-journal rules, and project data as external evidence that must be checked rather than assumed.

## Intake and scope lock

Collect or infer only what the supplied materials support:

```yaml
project_name: ...
target_journal: TIFS | TDSC | TSMC | TNSE | TCSS | other
operational_decision: ...
research_question: ...
main_claim: ...
main_claim_type: mechanism | numerical_method | control_performance | game_stability | parameter_recovery | predictive_generalization | operational_feasibility | causal_effect
model_family: ...
solution_notion: ...
primary_evidence_track: A | B | C | D | E
topology_level: T1 | T2 | T3 | T4 | T5 | not_applicable
repository_layers: foundation | game_learning | physics_informed
current_evidence: literature | proof | code | data | simulation | results
output_mode: plan | experiment | manuscript | audit | rebuttal
```

Leave unknown facts as `TBD`, `unverified`, `blocked`, or `not applicable`. Never fill gaps with plausible-looking facts.

For a new direction, freeze:

- one operational decision and one falsifiable research question;
- one minimal model resolution and one solution notion;
- one theorem ladder or estimation target;
- one primary algorithm or solver;
- one sufficient evidence track;
- one decisive experiment plus a bounded supporting set;
- explicit GO, NO-GO, and expansion gates.

Reuse a supplied package or prior direction as a scaffold after re-reading its current README, work prompt, scope files, and evidence state. Treat “仔细阅读分析” plus writing, derivation, experiments, or simulation as end-to-end research work, not a summary request.

## Execute the research pipeline

1. **Anchor the decision.** Define the actor, adversary or uncertainty, action, information, budget, objective, time scale, and evaluation unit.
2. **Audit novelty in full text.** Read the closest work, record papers that weaken the claim, and separate problem, model, theorem, algorithm, data, simulator, and finding novelty.
3. **Freeze the minimal publishable mechanism.** Move optional states, players, neural modules, datasets, and variants to future work unless the headline claim requires them.
4. **Write the scientific contract.** Fix entities, units, topology, timing, actions, information, equations, assumptions, objective, solution concept, and observed/inferred/assumed/synthetic/counterfactual status.
5. **Map theory to implementation.** Link every assumption, state, parameter, constraint, reset, theorem condition, and data field to code, a test, or an explicit limitation.
6. **Build evidence before prose.** Run matched baselines, independent checks, repetitions, uncertainty, sensitivity, holdouts, scalability, and retained-failure analysis as required by the claim.
7. **Draft in dependency order.** Write model/problem → theory → algorithm → evidence. Keep placeholders where evidence is pending.
8. **Audit every headline claim.** Point it to a theorem, figure, table, logged metric, or measured artifact with configuration and scope.
9. **Close honestly.** Preserve adverse results, narrowed claims, unresolved access gates, and NO-GO decisions.

Do not proceed past a gate when the closest paper may already solve the problem, the model cannot express the decision, the evidence track cannot support the claim, theorem assumptions do not map to implementation, or data/licence/privacy constraints remain unresolved.

## Apply the personal research architecture

Use `references/PERSONAL_RESEARCH_DIRECTIONS.md` to select the smallest coherent layer set:

```text
Foundation
  mechanism + canonical equations + control/game formulation + verified numerics
        ↓ only when feedback/adaptation is central
Game learning
  sampled environment + RL/MARL/self-play + repeated deviations
        ↓ only when observations/parameters/mechanisms are incomplete
Physics informed
  inverse estimation + PINN/PIDL + held-out rollout + identifiability
```

Maintain one canonical state equation, notation dictionary, adjacency convention, action timing contract, and objective across all layers. Treat teaching repositories as source-pinned methodological foundations, not new-paper novelty.

## Apply the personal writing style

Load `references/PERSONAL_STYLE_PROFILE.md` for drafting. Preserve this stable macro-signature:

```text
operational cyber/network/social problem
→ mechanism or representation gap
→ intervention or strategic-decision gap
→ named model/framework/problem
→ formal control, game, or estimation object
→ theorem or necessary conditions
→ reproducible solver/estimator/policy
→ comparative and stress-tested evidence
→ bounded cost, timing, topology, or security implication
```

Use these as soft targets, never as content requirements:

- Abstract: about 190–240 words and 8–11 sentences when current journal rules permit.
- Technical sentences: usually 19–26 words; review sentences above 42–45 words; manually inspect every sentence above 60 words.
- Contributions: normally 2–4 items ordered as model/problem → theory → algorithm → evidence.
- Results: figure/table and metric → magnitude plus uncertainty → mechanism → bounded implication.
- Voice: use active `we formulate/derive/establish/develop/evaluate` for owned research actions.

Use phrases from `references/PHRASEBANK.md` functionally, not mechanically. Avoid repeated connectors, forced acronyms, vague utility endings, grammar defects, and unsupported promotional adjectives. Personal style never overrides clearer IEEE English.

The current profile is `expanded-partial-calibration`. A verified 73-paper full-text corpus—42 owner-provided papers plus 31 nonduplicate open-access journal articles—now informs research architecture and quality doctrine. Sentence-level style metrics remain anchored to the role-weighted 42-paper local corpus, including 20 core-voice papers and 17 IEEE Transactions papers. This is not a verified complete-publication corpus, and coauthorship does not prove sentence-level authorship. Keep all of these boundaries visible whenever provenance matters.

## Apply the full-text consistency doctrine

Read `references/FULLTEXT_CORPUS_DERIVED_DOCTRINE.md` before accepting a central model, theorem, control, game, solver, or experiment claim. At minimum:

1. freeze the mechanism, state, unit, timing, information, and reality contracts;
2. distinguish exact equations from closures and persistent-input systems from boundary equilibria;
3. substitute equilibria/roots into the original model and independently check residuals, feasibility, theorem dependencies, and allowed branches;
4. audit delay histories/cohort survival, fractional memory, or impulse reset order when those mechanisms appear;
5. trace the objective through Hamiltonian, adjoint, stationarity/projection, discretization, and reported metric;
6. require solver settings, stopping residuals, refinement or independent checks, and formula-to-axis/sample-count agreement;
7. define random policies and probability spaces, prevent test/future leakage, match baseline budgets/information, and retain failures;
8. register every experiment's model version, parameters, initial history, topology/data split, solver, seeds, figure/table, and allowed conclusion.

Use `assets/templates/CROSS_PAPER_CONSISTENCY_LEDGER.csv` when multiple papers, variants, supplements, or implementations share a claim. Stop or narrow the work when a state leaves its feasible region, an equilibrium fails substitution, a necessary condition is advertised as a global solution, code does not evaluate theorem conditions, or reported axes/counts/semantics contradict the declared model.

## Match claims to evidence

Select the smallest adequate evidence track:

| Track | Evidence | Maximum default claim |
|---|---|---|
| A | mechanistic model, formal result, verified numerics | behavior and conditions under declared assumptions |
| B | stochastic, agent-based, event-driven, or closed-loop simulation | distributional policy behavior under simulator assumptions |
| C | observed topology or trace with simulated/counterfactual dynamics | sensitivity to observed structure or recorded conditions |
| D | real-data calibration plus held-out prediction | fit, effective-rate estimation, and prediction under an observation model |
| E | emulation, cyber range, hardware-in-loop, or field evidence | bounded feasibility and measured operational behavior |

When real propagation or intervention outcomes are unavailable, apply the topology ladder:

- T1: observed topology + synthetic dynamics → `real-topology simulation`;
- T2: observed topology/attributes + mixed calibration/assumptions → `attribute-informed real-topology simulation`;
- T3: temporal graph or trace + counterfactual action → `trace-driven evaluation`;
- T4: generated graph matched to observed statistics → `topology-calibrated synthetic simulation`;
- T5: controlled multi-family generated graphs → `controlled synthetic simulation`.

Never upgrade real topology to real-world validation, synthetic recovery to field calibration, a converged FBS run to global optimality, or tested deviations to a general Nash equilibrium.

Gate strong terms using `references/CLAIM_LANGUAGE_RULES.yaml`. In particular:

- require a dated closest-full-text audit for `first`, `novel`, or `innovative`;
- state necessary/local/configured scope for `optimal` unless stronger proof exists;
- require a defined solution concept and independent deviations or best responses for `equilibrium`;
- require matched budgets, information, tuning, repetitions, and uncertainty for `outperform`;
- require declared shifts and failures for `robust`, size/resource sweeps for `scalable`, and operational mapping for `practical`;
- require a probability space and formal support for `almost surely`, and a finite-dimensional sampling contract or declared measure for random functional policies;
- replace `solved successfully` when only necessary conditions or one converged run exist; require sufficiency, a certified gap, or an independent solver for the stronger wording;
- require an appropriate prospective or causal design for causal language.

Treat static linter findings as conservative screening, not as certificates. A line that escapes a regex still requires the complete theorem, solver, probability, sampling, baseline, and evidence contract in the claim ledger.

## Use the bundled utilities

Run commands through the dependency-free wrapper:

```bash
SKILL_DIR="${CODEX_HOME:-$HOME/.codex}/skills/luxing-ieee-transactions"
python "$SKILL_DIR/scripts/luxing_ieee.py" validate
python "$SKILL_DIR/scripts/luxing_ieee.py" recommend-evidence --claim-type control_performance
python "$SKILL_DIR/scripts/luxing_ieee.py" recommend-topology --availability real_topology
python "$SKILL_DIR/scripts/luxing_ieee.py" new-project --name my-paper --journal TIFS --output /path/to/project
python "$SKILL_DIR/scripts/luxing_ieee.py" audit-evidence /path/to/EVIDENCE_PLAN.json
python "$SKILL_DIR/scripts/luxing_ieee.py" audit-topology /path/to/TOPOLOGY_CARD.yaml
python "$SKILL_DIR/scripts/luxing_ieee.py" check /path/to/manuscript.tex --report /path/to/preflight.md
```

Use templates under `assets/templates/` when a full scaffold is unnecessary. A template containing `TBD` should be flagged, not falsely passed.

## Protect private and licensed material

- Keep paper PDFs, extracted full text, raw graphs/data, PCAPs, checkpoints, review files, and Deakin downloads outside the skill and public release.
- Retain only lawful metadata, hashes, derived metrics, paraphrased paper cards, and short necessary quotations.
- Follow `references/DEAKIN_ACCESS_POLICY.md`; pause for owner-completed login or MFA and never inspect credentials, cookies, tokens, browser storage, or unrelated account data.
- Keep private literature/style corpora separate from novelty evidence and public artifacts.
- Check dataset and repository licences independently; a code licence does not grant rights to a dataset or paper.

## Completion contract

Report:

- the frozen scope and strongest supported claim;
- artifacts created and evidence actually run;
- negative evidence and claim reductions;
- remaining proof, code, data, literature, access, licence, or journal-rule gates;
- a final status of `READY`, `READY WITH WARNINGS`, or `NOT READY` when performing preflight.

Do not call a package, manuscript, theorem, experiment, or corpus complete until the corresponding validation gate has actually passed.
