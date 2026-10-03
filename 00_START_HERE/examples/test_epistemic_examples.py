"""Synthetic teaching checks only. These are not tests of ARK's physical validity.
Run: python -m unittest discover -s 00_START_HERE/examples -v
"""
import math
import unittest


def inverse_prediction(a: float) -> float:
    """The candidate law a*b=1; input provenance must be audited separately."""
    if not math.isfinite(a) or a == 0:
        raise ValueError("a must be finite and nonzero")
    return 1.0 / a


def reconstructed_target(target: float) -> float:
    """Deliberately returns supplied target information, not a prediction."""
    return inverse_prediction(inverse_prediction(target))


def calibrate(x_ref: float, y_ref: float) -> float:
    if not math.isfinite(x_ref) or not math.isfinite(y_ref) or x_ref == 0:
        raise ValueError("reference values must be finite and x_ref nonzero")
    return y_ref / x_ref


def linear_prediction(x: float, k: float) -> float:
    if not math.isfinite(x) or not math.isfinite(k):
        raise ValueError("inputs must be finite")
    return k * x


def coupled_solution(x: float, z: float) -> tuple[float, float]:
    if not math.isfinite(x) or not math.isfinite(z):
        raise ValueError("inputs must be finite")
    return (x + z) / 2.0, (x - z) / 2.0


def difference_uncertainty(u1: float, u2: float, covariance: float = 0.0) -> float:
    if not all(math.isfinite(t) for t in (u1, u2, covariance)):
        raise ValueError("uncertainty inputs must be finite")
    if u1 < 0 or u2 < 0 or abs(covariance) > u1 * u2:
        raise ValueError("invalid standard uncertainties or covariance")
    variance = u1 * u1 + u2 * u2 - 2 * covariance
    return math.sqrt(max(0.0, variance))


class EpistemicTeachingExamples(unittest.TestCase):
    def test_measured_input_inverse(self):
        self.assertAlmostEqual(inverse_prediction(4.0), 0.25)
        self.assertAlmostEqual(0.04 / 4.0**2, 0.0025)

    def test_direct_target_change_does_not_change_predictor(self):
        predictions = [inverse_prediction(4.0) for target in (0.251, 9.0)]
        self.assertEqual(predictions, [0.25, 0.25])
        # The target is deliberately absent from the predictor signature.

    def test_reconstruction_returns_even_a_wrong_target(self):
        for target in (0.251, 9.0, -3.0):
            self.assertAlmostEqual(reconstructed_target(target), target)

    def test_calibration_and_transfer_are_separate(self):
        k = calibrate(2.0, 6.0)
        self.assertEqual(linear_prediction(2.0, k), 6.0)
        self.assertEqual(linear_prediction(5.0, k), 15.0)

    def test_coupled_solution_satisfies_both_constraints(self):
        u, v = coupled_solution(10.0, 4.0)
        self.assertEqual((u, v), (7.0, 3.0))
        self.assertEqual(u + v, 10.0)
        self.assertEqual(u - v, 4.0)

    def test_branch_ambiguity_is_not_unique_prediction(self):
        roots = (-math.sqrt(4.0), math.sqrt(4.0))
        self.assertEqual(roots, (-2.0, 2.0))
        self.assertTrue(all(root**2 == 4.0 for root in roots))

    def test_common_equilibrium_different_response(self):
        delta0, rate, time = 1.0, 2.0, 1.0
        stable = delta0 * math.exp(-rate * time)
        unstable = delta0 * math.exp(rate * time)
        self.assertLess(stable, delta0)
        self.assertGreater(unstable, delta0)

    def test_covariance_changes_difference_uncertainty(self):
        u = difference_uncertainty(0.0025, 0.003)
        self.assertAlmostEqual(u, 0.003905124837953327)
        self.assertLess(difference_uncertainty(0.0025, 0.003, 0.000003), u)

    def test_invalid_inputs_do_not_become_silent_numbers(self):
        for value in (0.0, math.inf, math.nan):
            with self.assertRaises(ValueError):
                inverse_prediction(value)
        with self.assertRaises(ValueError):
            difference_uncertainty(1.0, 1.0, 2.0)


if __name__ == '__main__':
    unittest.main()
