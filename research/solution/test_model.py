#!/usr/bin/env python
"""
Tests for the model.
"""

import unittest

import numpy as np
from numpy.typing import ArrayLike

from .solver import Solver
from .specific_model import SpecificModel
from .utils import load_parameters


# Original functions for comparison
def original_f(θ: ArrayLike, m, q, ε, θ0) -> ArrayLike:
    return m * θ / (1 - q * θ) * np.exp(ε / (θ + θ0))


def original_fprime(θ: ArrayLike, m, q, ε, θ0) -> ArrayLike:
    return original_f(θ, m, q, ε, θ0) * (1 / θ + q / (1 - q * θ) - ε / (θ0 + θ) ** 2)


class TestModel(unittest.TestCase):
    """
    Test suite for the model.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.params = load_parameters("case1.toml")
        self.model = SpecificModel(**self.params)
        self.solver = Solver(self.model)
        self.θ_test_values = np.array([0.1, 1.0, 10.0, 100.0])

    def test_f(self):
        """
        Test the f(θ) method.
        """
        for θ_val in self.θ_test_values:
            original_result = original_f(
                θ_val,
                self.model.m,
                self.model.q,
                self.model.ε,
                self.model.θ0,
            )
            model_result = self.model.f(θ_val)
            self.assertTrue(np.allclose(original_result, model_result))

    def test_fprime(self):
        """
        Test the fprime(θ) method.
        """
        for θ_val in self.θ_test_values:
            original_result = original_fprime(
                θ_val,
                self.model.m,
                self.model.q,
                self.model.ε,
                self.model.θ0,
            )
            model_result = self.model.fprime(θ_val)
            self.assertTrue(np.allclose(original_result, model_result))

    def test_ode_solver(self):
        """
        Test the ODE solver.
        """
        t, X_s = self.solver.solve_ode(X0=[0.05, 0.05], t_span=(0, 0.25), num_points=10)
        self.assertEqual(t.shape, (10,))
        self.assertEqual(X_s.shape, (10, 3))


if __name__ == "__main__":
    unittest.main()
