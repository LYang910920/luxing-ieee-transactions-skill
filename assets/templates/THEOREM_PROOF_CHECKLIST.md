# Theorem and Proof Checklist

## Statement

- [ ] All symbols defined before use.
- [ ] Assumptions are explicit and minimal.
- [ ] Quantifiers and domains are clear.
- [ ] Necessary/sufficient and local/global scope is stated.
- [ ] Continuous-time result is not silently transferred to a discretization.

## Dependency

- [ ] Lemma/theorem dependency graph is acyclic.
- [ ] No conclusion is assumed in a premise.
- [ ] Boundary, terminal and jump conditions are consistent.
- [ ] Existence/uniqueness/regularity invoked from a cited or proved result.

## Proof

- [ ] The headline step is shown, not hidden behind “straightforward.”
- [ ] Inequality direction and dimensions checked.
- [ ] Edge cases and zero/upper-bound controls checked.
- [ ] Numerical evidence is not used as proof.

## Interpretation

- [ ] Explain operational meaning.
- [ ] State what the theorem does not establish.
- [ ] Map assumptions to code and experiments.
