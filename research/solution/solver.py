#!/usr/bin/env python
"""
Numerical solver for hyperbolic problems using SciPy.
"""

from typing import List, Tuple

import numpy as np
from numpy.typing import ArrayLike
from scipy.integrate import odeint, solve_ivp
from scipy.optimize import fsolve

from .hyperbolic_problem import HyperbolicProblem


class Solver:
    """
    Performs numerical operations on a HyperbolicProblem model,
    finding roots of characteristic equations and solving ODEs for traveling waves.
    """

    def __init__(self, model: HyperbolicProblem):
        """
        Initializes the solver with a specific hyperbolic model instance.
        """
        self.model = model

    def find_fprime_roots(self, initial_guesses: List[float]) -> np.ndarray:
        """
        Finds roots of f'(θ) = 0 (critical points of f(θ)) using model's g(θ).
        """
        return fsolve(self.model.g, initial_guesses)

    def find_fprimeprime_root(self, initial_guess: float) -> float:
        """
        Finds root of f''(θ) = 0 (inflection point of f(θ)) using model's h(θ).
        """
        return fsolve(self.model.h, [initial_guess])[0]

    def find_f_root(self, y_value: float, initial_guess: float) -> float:
        """
        Finds θ such that f(θ) equals a specific y_value.
        """

        def func_to_solve(θ: ArrayLike) -> ArrayLike:
            """Closure for the root-finding problem."""
            return self.model.f(θ) - y_value

        return fsolve(func_to_solve, [initial_guess])[0]

    def solve_ode(
        self, X0: list, t_span: Tuple[float, float], num_points: int
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Solves the system of ODEs defined in the model, dX/dξ = system(ξ, X).
        Also calculates `Sy` based on the solution.
        """
        t = np.linspace(start=t_span[0], stop=t_span[1], num=num_points)
        # Use solve_ivp to solve the system defined in the model
        sol = solve_ivp(
            fun=self.model.system,
            t_span=t_span,
            y0=X0,
            t_eval=t,
            first_step=t[1] - t[0],  # Ensure the first step is positive
        )
        X = sol.y.T

        # Calculate the dependent variable Sy based on the solution for So
        Sy = ((self.model.SoR - X[:, 1]) * self.model.SyL / self.model.SoR)[
            np.newaxis
        ].T
        # Append Sy to the solution matrix
        X = np.hstack((X, Sy))

        return sol.t, X
