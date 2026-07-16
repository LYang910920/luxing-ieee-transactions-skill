# Theorem and Proof Checklist

## Statement

- [ ] All symbols defined before use.
- [ ] Assumptions are explicit and minimal.
- [ ] Quantifiers and domains are clear.
- [ ] Necessary/sufficient and local/global scope is stated.
- [ ] Continuous-time result is not silently transferred to a discretization.

## Mechanism and admissibility

- [ ] Every state has one stable semantic meaning and unit.
- [ ] Flow, event, reset, delayed, and forced-input terms preserve the declared feasible set.
- [ ] Boundary directions, conservation identities, and zero/upper-control cases are checked mechanically.
- [ ] Exact dynamics are distinguished from mean-field, independence, moment-closure, or continuum approximations.
- [ ] Delay histories, cohort survival/exit, impulse ordering, reset feasibility, and non-Zeno conditions are explicit when applicable.

## Equilibrium, branch, and condition audit

- [ ] The claimed equilibrium still exists under every persistent input or forced intervention.
- [ ] Each closed-form or numerical root is substituted into the original equations and checked for feasibility and residual.
- [ ] Additional sign or threshold conditions are simplified against earlier assumptions to detect redundancy or contradiction.
- [ ] A bifurcation label is supported by a branch parameter, transversality or normal form, and stability exchange—not only root counting.
- [ ] Small-delay or perturbation results include a frequency/domain bound and an explicit remainder or approximation error.

## Dependency

- [ ] Lemma/theorem dependency graph is acyclic.
- [ ] No conclusion is assumed in a premise.
- [ ] Every cited condition actually belongs to the named lemma/theorem and uses the same model version.
- [ ] Boundary, terminal and jump conditions are consistent.
- [ ] Existence/uniqueness/regularity invoked from a cited or proved result.

## Proof

- [ ] The headline step is shown, not hidden behind “straightforward.”
- [ ] Inequality direction and dimensions checked.
- [ ] Edge cases and zero/upper-bound controls checked.
- [ ] Numerical evidence is not used as proof.

## Theory-to-algorithm interface

- [ ] Objective, Hamiltonian/payoff, adjoint, stationarity condition, projection, and code share one symbol and sign ledger.
- [ ] State, control, adjoint, delayed, and advanced-time indices are checked at the exact update time used in code.
- [ ] Terminal transversality and jump conditions match the published trajectory and numerical boundary treatment.
- [ ] The solver reports discretization, tolerances, residuals, failure behavior, and an independent check where the claim requires it.

## Interpretation

- [ ] Explain operational meaning.
- [ ] State what the theorem does not establish.
- [ ] Map assumptions to code and experiments.
