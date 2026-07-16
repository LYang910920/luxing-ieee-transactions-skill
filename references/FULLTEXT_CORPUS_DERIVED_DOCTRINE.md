# Full-Text Corpus-Derived Research Doctrine

## Purpose and evidence boundary

This doctrine converts recurring lessons from a 73-paper verified-full-text working corpus into executable research checks. The corpus combines 42 owner-provided papers with 31 nonduplicate open-access journal articles associated with ORCID `0000-0002-9229-5787`. Every in-scope item was handled as a full-text deep-reading unit before synthesis.

The 73-paper corpus strengthens research architecture, mathematical quality control, solver disclosure, experiment design, and claim calibration. It does **not** establish a complete publication universe, personal authorship of every sentence, or permission to redistribute source PDFs, extracted text, equations, tables, or figures. Sentence-level style targets continue to use the role-weighted 42-paper local corpus, especially the 20-paper core-voice subset.

Apply the following checks before treating a result as manuscript-ready. A failed gate should narrow the claim, trigger an implementation or proof repair, or produce a visible `NO-GO`; it should not be hidden by stronger prose.

## 1. Claim-maturity ledger

Classify every important statement as one of:

```text
proposed → formally defined → proved/characterized → implemented
→ numerically verified → independently checked → empirically validated
```

- Never move a claim to the right merely because a paper contains a theorem, converged trajectory, or real network.
- Record whether a result is necessary, sufficient, local, global, asymptotic, finite-horizon, configured, simulated, or measured.
- Map each headline claim to a theorem, residual, independent computation, figure/table, data split, or measured artifact.
- Preserve counterexamples, unsupported branches, and failed parameter regions in the same ledger.

Use `assets/templates/CROSS_PAPER_CONSISTENCY_LEDGER.csv` when several papers, model variants, supplements, or code paths share a claim.

## 2. Mechanism, state, unit, and closure contract

Before deriving thresholds or controls, freeze a mechanism ledger:

```text
entity → state/compartment → transition/event → source → destination
→ rate or probability → unit → information available at action time
```

Required checks:

- distinguish instantaneous state, transition count, cumulative event count, unique affected entity, probability, rate, and cost;
- prove or numerically falsify nonnegativity, conservation, simplex/box invariance, and admissible reset behavior at every boundary;
- confirm that persistent external inputs do not make a claimed zero or disease-free equilibrium impossible;
- separate an exact stochastic expectation equation from an independence, pair, degree, moment, or mean-field closure;
- state the approximation and test closure error instead of presenting the closed ODE as exact;
- keep parameter meanings monotone and dimensionally consistent across equations, text, code, figures, and supplements.

A topology can be observed while the dynamics, rates, interventions, and outcomes remain synthetic. Record those layers separately in the reality ledger.

## 3. Equilibria, roots, thresholds, and theorem dependencies

For every equilibrium, threshold, bifurcation, or closed-form solution:

1. substitute it into the original, unreduced equations;
2. verify domain, sign, denominator, ordering, and constraint feasibility;
3. compute a residual with an independent symbolic or numerical route;
4. simplify theorem conditions to detect redundancy, contradiction, or automatic implication;
5. distinguish an attracting or invariant manifold from an exact model reduction;
6. track the full dependency chain to a valid source rather than citing a theorem by resemblance;
7. test all algebraic branches that are allowed by the declared parameter domain.

A plotted branch is not a bifurcation classification. Require equilibrium continuation or equivalent branch evidence, stability on the relevant sides, and the nondegeneracy/transversality conditions for the named bifurcation.

## 4. Delay, fractional, impulse, and hybrid systems

### Delay systems

- Define a complete nonnegative history on the entire maximum-delay interval.
- Audit delayed inflow against cohort survival and all competing exits during the delay.
- Prove nonnegative invariance on boundary faces; a delayed loss term can violate positivity even when the undelayed model is valid.
- Shared delays identify joint effects unless the design separately varies them.
- For a small-delay approximation, declare a delay bound, frequency/time-scale bound, approximation remainder, and validation against the original DDE.
- Check advanced-time adjoint terms and terminal-window truncation explicitly.

### Fractional systems

- State the derivative definition, initial-data contract, dimensional interpretation, and numerical memory scheme.
- Do not transfer integer-order stability or control results without verifying the fractional assumptions.
- Report memory truncation, step-size sensitivity, and convergence checks.

### Impulse and hybrid systems

- State pre-event flow, event trigger/time, pre-jump state, reset ordering, post-jump state, and action feasibility.
- Prove reset-map invariance and rule out infeasible simultaneous actions, event-order ambiguity, and Zeno accumulation.
- Distinguish a memoryless transition rate from an explicit residence-time or delayed mechanism.

## 5. Objectives, constraints, Hamiltonians, and optimal-control claims

Maintain a symbol-and-sign ledger from the scientific objective to the implementation:

```text
scientific cost/payoff → mathematical objective → Hamiltonian
→ state equations → adjoint equations → stationarity/projection
→ discrete update → reported metric
```

Required checks:

- differentiate the actual Hamiltonian with respect to every control and unit-test the sign, bounds, and projection;
- verify state/control/adjoint indexing at the same time and, for delays, at advanced times;
- distinguish pointwise caps from integral budgets and path constraints;
- treat terminal transversality as a boundary condition, not a claim that an adjoint or control must be monotone;
- use total or constraint-aware derivatives when parameters change feasible sets, equilibria, or optimized controls;
- separate a parameter's physical role from an imposed cap, price, or weighting role;
- state existence assumptions and whether the pointwise minimizer is unique;
- label Pontryagin conditions as necessary unless convexity or another sufficiency argument is verified;
- never equate one forward–backward sweep convergence trace with global optimality.

Qualitative wishes such as “smooth,” “slowly varying,” or “small change” must appear as mathematical ramp, variation, switching, or regularization constraints if they matter to feasibility.

## 6. Games, hierarchical decisions, and adaptive opponents

- Define players, information, strategy classes, timing, leader/follower order, payoff units, and solution concept.
- Recompute best responses independently where possible and report unilateral deviation gain or exploitability.
- A fixed rival strategy is a response experiment, not automatically a strategic equilibrium.
- A finite set of local perturbations does not establish global Nash, Stackelberg, coalition, or evolutionary stability.
- For learning or self-play, report response diversity, held-out opponents, exploitability, and physical outcomes in addition to reward.
- Random infinite-dimensional strategies require a stated probability measure or finite-dimensional parameterization; “uniformly random function” is otherwise undefined.

## 7. Theory-to-code and solver contract

Complete `assets/templates/THEOREM_TO_CODE_MAP.csv` before trusting a computational theorem illustration. At minimum record:

- model version and equation-to-state mapping;
- parameter values, units, initial state/history, topology, and event order;
- discretization, integrator, interpolation, projection, stopping rule, maximum iterations, and random seeds;
- theorem-condition evaluation in code;
- residuals for dynamics, algebraic roots, constraints, stationarity, and equilibrium deviations;
- an independent solver, refinement, limiting case, or conservation check;
- iteration count, runtime, communication, and memory when complexity or scalability is claimed.

Formula-defined sample/window counts must match the implementation and plotted axes. Complexity includes outer iterations, inner solves, communication, and convergence behavior—not only one update formula.

## 8. Baselines, probability, fairness, and uncertainty

- Always include a zero-intervention/no-defense baseline when the model permits it.
- Match information, budgets, feasible actions, tuning effort, stopping rules, and evaluation scenarios.
- Do not prefilter the candidate family using the test outcomes used for final comparison.
- Define how random functions, controls, networks, or initial conditions are sampled.
- Reserve “almost surely” or probability-one language for a stated probability space and a supporting formal result.
- Separate seed variability, parameter uncertainty, structural sensitivity, adversarial shift, and statistical significance.
- Report the number of repetitions, interval construction, exclusions, failures, and retained adverse runs.
- “Always” requires a quantified domain or theorem, not a small collection of curves.

## 9. Objective scale and intervention semantics

- Normalize or explicitly explain objective comparisons across network sizes, horizons, populations, and sampling frequencies.
- Recognize that an undiscounted integral can grow mechanically with the horizon.
- Recognize that increasing a pointwise cap creates nested feasible sets; monotonic improvement can be structural rather than empirical discovery.
- Define whether cumulative quantities count repeated events or unique entities.
- For information-gathering actions such as testing, sensing, or diagnosis, include an evidence, belief, observation, or deployment state if the claimed mechanism depends on acquired information.
- Use a ratio-direction check: confirm which quantity is numerator, denominator, benefit, and cost before interpreting monotonicity.

## 10. Robustness, sensitivity, and causal boundaries

Keep these separate:

- **structural result:** follows from equations or feasible-set nesting;
- **sensitivity:** response to declared parameter changes;
- **uncertainty:** distribution induced by a declared sampling model;
- **robustness:** performance under named shifts, perturbations, or adversaries;
- **causal effect:** requires a defensible intervention/comparison design.

Parameter sweeps alone do not establish robustness, generalization, or causal effectiveness. Record known failure regions and the strongest supported boundary.

## 11. Data, topology, provenance, and leakage

- Record observed, inferred, assumed, synthetic, generated-truth, and counterfactual elements separately.
- A real background trace with synthetic attacks is mixed evidence, not fully real-world validation.
- Select thresholds, windows, clusters, hyperparameters, and stopping rules on training/validation data only.
- Do not use future samples in a feature window unless the operational decision is explicitly retrospective.
- Report detection delay and the information available at decision time.
- Distinguish a globally computed grouping step from genuinely distributed online operation; disclose global time, communication, and memory costs.

## 12. Experiment, figure, and supplement registry

For each experiment, record:

```text
experiment ID → model/equation version → theorem/claim → parameters/units
→ initial state or history → topology/data split → solver/configuration
→ seeds/repetitions → baseline/budget → figure/table → allowed conclusion
```

Then verify:

- text descriptions match plotted direction, endpoints, legends, axes, units, and equilibrium targets;
- formula-defined counts match code and figure axes;
- supplements use the same time axis, dimensions, symbols, and model version;
- every “converges to zero,” “best,” “faster,” or “lower cost” statement is numerically checkable from the cited artifact;
- data/code availability statements match what is actually released.

## Family-specific minimum gates

| Family | Minimum additional gate |
|---|---|
| Epidemic/malware/rumor dynamics | positivity, invariant region, threshold substitution, exact-vs-closure label |
| Delay dynamics | history, cohort survival, delayed boundary positivity, original-DDE comparison |
| Fractional dynamics | derivative/memory contract, dimensional interpretation, memory-scheme convergence |
| Optimal control | objective–Hamiltonian–adjoint–projection ledger, sufficiency boundary, independent solver |
| Differential/Stackelberg games | information/strategy class, best-response residual, exploitability/deviation test |
| Impulse/hybrid control | event order, reset feasibility, non-Zeno check, continuous–discrete consistency |
| Topology/network intervention | node/edge semantics, preprocessing, multiple graphs, structural perturbations |
| Detection/learning | leakage-free splits, operational timing, held-out shifts, calibration and failure cases |
| Real/mixed data | provenance and reality ledger, observation model, uncertainty, permitted claim class |

## Mandatory `NO-GO` examples

Stop or narrow the paper when any headline result depends on:

- an equilibrium that is not a solution of the original equations;
- a state leaving its declared feasible or nonnegative region;
- an adjoint/control update that does not differentiate the implemented objective;
- theorem conditions or branches that the code never evaluates;
- a formula, time axis, sample count, or objective scale incompatible with the reported figure;
- test-set tuning or future information unavailable at decision time;
- an undefined random strategy or unsupported probability-one statement;
- a necessary condition presented as a global optimum or a converged run presented as an equilibrium proof;
- evidence described as real-world, causal, robust, or scalable beyond its provenance and tested domain.

When repair is possible, record the failed gate, correction, rerun, and changed claim in the cross-paper consistency ledger.
