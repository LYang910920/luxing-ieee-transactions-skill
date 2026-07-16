from __future__ import annotations

from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.luxing_ieee_skill.linter import lint_text  # noqa: E402


def codes(text: str) -> set[str]:
    return {issue.code for issue in lint_text(text)}


class FullTextDerivedClaimGateTests(unittest.TestCase):
    def test_almost_sure_without_probability_contract_is_flagged(self) -> None:
        manuscript = "The algorithm converges almost surely in 10,000 similar experiments."
        self.assertIn("CLAIM_GATE_ALMOST_SURE", codes(manuscript))

    def test_almost_sure_with_formal_probability_contract_is_not_flagged(self) -> None:
        manuscript = (
            "On the probability space defined above, the independent and identically distributed "
            "noise sequence satisfies the theorem; hence the estimator converges almost surely."
        )
        self.assertNotIn("CLAIM_GATE_ALMOST_SURE", codes(manuscript))

    def test_unrelated_theorem_does_not_release_almost_sure_gate(self) -> None:
        manuscript = (
            "Theorem 2 establishes boundedness of the deterministic state. "
            "The algorithm converges almost surely in 10,000 experiments."
        )
        self.assertIn("CLAIM_GATE_ALMOST_SURE", codes(manuscript))

    def test_complete_probability_context_still_needs_linked_theorem(self) -> None:
        manuscript = (
            "On the probability space above, the noise is independent and identically distributed. "
            "Theorem 2 establishes boundedness of a separate deterministic state. "
            "The algorithm converges almost surely in the reported experiments."
        )
        self.assertIn("CLAIM_GATE_ALMOST_SURE", codes(manuscript))

    def test_uniform_random_function_without_parameterization_is_flagged(self) -> None:
        manuscript = "We randomly and uniformly generate 100 feasible control policies for comparison."
        self.assertIn("BASELINE_RANDOM_FUNCTION_UNDEFINED", codes(manuscript))

    def test_uniform_random_policy_with_finite_contract_is_not_flagged(self) -> None:
        manuscript = (
            "We uniformly sampled policy coefficients on a 21-point time grid using random seed 9 "
            "and piecewise-constant interpolation."
        )
        self.assertNotIn("BASELINE_RANDOM_FUNCTION_UNDEFINED", codes(manuscript))

    def test_unrelated_random_seed_does_not_define_random_function(self) -> None:
        manuscript = (
            "Random seed 9 was used for the epidemic simulator. "
            "We uniformly sampled feasible control policies for comparison."
        )
        self.assertIn("BASELINE_RANDOM_FUNCTION_UNDEFINED", codes(manuscript))

    def test_coefficients_without_resolution_and_reconstruction_are_flagged(self) -> None:
        manuscript = (
            "We uniformly sampled feasible control policies represented by coefficients "
            "on a time grid using random seed 9."
        )
        self.assertIn("BASELINE_RANDOM_FUNCTION_UNDEFINED", codes(manuscript))

    def test_solved_successfully_without_certificate_is_flagged(self) -> None:
        manuscript = "The forward-backward iteration solved the optimal control problem successfully."
        self.assertIn("CLAIM_GATE_SOLVED_SUCCESSFULLY", codes(manuscript))

    def test_solved_successfully_with_independent_certificate_is_not_flagged(self) -> None:
        manuscript = (
            "The method solved the problem successfully; direct collocation served as an independent "
            "solver and yielded a certified optimality gap."
        )
        self.assertNotIn("CLAIM_GATE_SOLVED_SUCCESSFULLY", codes(manuscript))

    def test_unrelated_direct_collocation_does_not_release_solution_gate(self) -> None:
        manuscript = (
            "Direct collocation discretizes a separate benchmark. "
            "The forward-backward iteration solved the optimal control problem successfully."
        )
        self.assertIn("CLAIM_GATE_SOLVED_SUCCESSFULLY", codes(manuscript))

    def test_contrasted_collocation_does_not_certify_solution_claim(self) -> None:
        manuscript = (
            "Direct collocation agrees with a separate benchmark, while the forward-backward "
            "iteration solved our nonconvex optimal control problem successfully."
        )
        self.assertIn("CLAIM_GATE_SOLVED_SUCCESSFULLY", codes(manuscript))


if __name__ == "__main__":
    unittest.main()
