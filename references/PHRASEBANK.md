# Lu-Xing Yang–Calibrated Phrasebank

Use this as a functional menu, not a copy-and-paste script. Every sentence must remain true, specific, and supported.

## Operational problem

- `[Threat/system] creates a decision problem for [decision maker] because ...`
- `The central challenge is not only [mechanism], but also when and how to allocate [action/resource].`
- `This interaction is shaped by [topology/information/timing/behavior], which makes [simple assumption] inadequate.`

## Literature and gap

- `Existing studies can be grouped into [family A], [family B], and [family C].`
- `However, [family] assumes ..., and therefore cannot represent ...`
- `These studies clarify [what they solve], but leave unresolved [exact object].`
- `The remaining gap is twofold: [modeling gap] and [strategy/evidence gap].`
- `To address these limitations, we ...`

Avoid using `few studies`, `has never been considered`, or `to the best of our knowledge` unless the novelty matrix supports the statement.

## Model and problem formulation

- `We characterize [process] using a [node/degree/aggregate/multilayer] model in which ...`
- `On this basis, we formulate [named problem] to determine ... subject to ...`
- `The state variable [symbol] represents ..., whereas [action] changes ...`
- `The admissible strategy set is defined by [bounds/information/budget/timing].`
- `The objective balances [security/social benefit] against [control/intervention cost].`

## Theory

- `Under Assumptions [X–Y], Theorem [N] establishes ...`
- `The result is a necessary condition for ..., not a sufficient global-optimality guarantee.`
- `The optimality system consists of the state, costate, stationarity, and boundary conditions.`
- `This property provides the numerical stopping criterion used in Algorithm [N].`
- `The scope is limited to [model/strategy class/information structure].`

## Algorithm

- `Based on the derived system, we develop an iterative algorithm that alternates ...`
- `Each update is projected onto [admissible set], and the iteration stops when [residual] is below [tolerance].`
- `The algorithm fails explicitly when [nonconvergence/infeasibility/numerical condition].`
- `The computational cost is reported as a function of [nodes/edges/time steps/iterations].`

## Topology and simulation

- `We evaluate the method on [observed topology], while the dynamics and intervention parameters remain explicitly synthetic.`
- `The study is therefore a real-topology simulation rather than a field calibration.`
- `To assess topology sensitivity, we compare [observed graph] with matched [ER/BA/WS/SBM/configuration] controls.`
- `Scenarios vary graph, parameter, and attack-seed realizations independently.`
- `The node-level deterministic model is checked against [independent solver/Monte Carlo ensemble].`

## Experiments and results

- `Figure [N] compares [methods] under the same [budget/information/trace/horizon].`
- `[Metric] changes from [value] to [value], with [uncertainty] across [instances/seeds].`
- `The improvement arises because [mechanism/control allocation/topology reason].`
- `This result supports [scoped claim] within the tested [graphs/parameters/scenarios].`
- `The conclusion does not imply [field effect/causality/general equilibrium].`

## Discussion and limitations

- `The result is conditional on [assumption/data/topology/information].`
- `A real topology captures observed structure but not unobserved propagation rates or intervention effects.`
- `The current evidence supports comparative simulated performance, not operational effectiveness.`
- `Future work should validate [specific assumption] using [specific data/testbed/design].`

## Conclusion

- `We investigated [decision problem] by integrating [model], [theory], and [algorithm].`
- `The main finding is [strongest verified result], under [scope].`
- `The analysis indicates [bounded security/policy implication].`
- `The principal limitations concern [data/topology/observability/scale/deployment].`

## Connector discipline

Corpus-frequent connectors include `First`, `Second`, `Next`, `Based on`, `On this basis`, `Furthermore`, and `Finally`. Do not repeat the same connector in adjacent sentences or use it more than roughly three times per 500 words.

## Prohibited automatic upgrades

Do not replace:

- `lower mean objective` with `significantly better` without statistics;
- `small residual` with `proved optimal`;
- `tested deviation set` with `Nash equilibrium`;
- `observed topology` with `real-world dynamics`;
- `generated-truth recovery` with `field calibration`;
- `runtime at three sizes` with `universally scalable`.
