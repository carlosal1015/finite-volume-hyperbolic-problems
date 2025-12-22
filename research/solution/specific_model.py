#!/usr/bin/env python
"""
Concrete implementation of HyperbolicProblem for a specific mathematical model.
"""

import numpy as np
from numpy.typing import ArrayLike

from .hyperbolic_problem import HyperbolicProblem


class SpecificModel(HyperbolicProblem):
    """
    Defines specific mathematical formulas for flux (f), its derivatives,
    auxiliary functions (g, h), and the ODE system based on physical parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes the specific model and calculates derived dimensionless parameters.
        """
        super().__init__(**kwargs)

        # --- Intermediate Characteristic Scales ---
        α = 1.0  # Assumed constant
        w = 1  # Assumed constant
        tast = 1 / self.kp  # Characteristic reaction time
        xast = (self.ρg * self.u) / (self.ρres * self.kp)  # Characteristic length

        # --- Derived Dimensionless Groups (Model Coefficients) ---
        self.a1 = (tast * self.uo * self.co * self.ρo) / (self.Cm * xast)
        self.a2 = (tast * self.ug) / (self.φ * xast)
        self.a3 = (tast * self.uo) / (self.φ * xast)
        self.b1 = (self.ρo * self.Qr) / (self.Cm * self.Tres)
        self.b2 = (w * self.ρo) / self.ρg
        self.b3 = 1.0  # Assumed constant
        self.β = (α * tast) / self.Cm
        self.Tast = self.Tres  # Characteristic temperature
        self.c = (self.a2 * self.b3 * self.SyL + self.a3 * self.b2 * self.SoR) / (
            self.b2 * self.SoR + self.b3 * self.SyL
        )

        # --- Key Dimensionless Parameters for the Flux Function f(θ) ---
        self.m = (self.β * self.SoR) / (self.b1 * self.SyL * tast * self.kp)
        self.ε = self.Er / (self.R * self.Tast)  # Dimensionless activation energy
        self.θ0 = self.Tres / self.Tast  # Dimensionless initial temperature
        self.q = (self.a1 * self.b3) / (self.b1 * (self.c - self.a3))

    def f(self, θ: ArrayLike) -> ArrayLike:
        """
        Calculates the flux function f(θ) for the specific model.
        """
        return self.m * θ / (1 - self.q * θ) * np.exp(self.ε / (θ + self.θ0))

    def fprime(self, θ: ArrayLike) -> ArrayLike:
        """
        Calculates the first derivative of the flux function, f'(θ).
        """
        return self.f(θ) * (
            1 / θ + self.q / (1 - self.q * θ) - self.ε / (self.θ0 + θ) ** 2
        )

    def fprimeprime(self, θ: ArrayLike) -> ArrayLike:
        """
        Calculates the second derivative of the flux function, f''(θ).
        """
        # This complex expression is the analytical second derivative of f(θ)
        return -self.f(θ) * (
            (2 * self.ε * self.q) / ((1 - self.q * θ) * (self.θ0 + θ) ** 2)
            - self.ε * (2 + self.ε / (self.θ0 + θ)) / (self.θ0 + θ) ** 3
            + 2 * self.ε / (θ * (self.θ0 + θ) ** 2)
            - 2 * self.q**2 / (1 - self.q * θ) ** 2
            - 2 * self.q / (θ * (1 - self.q * θ))
        )

    def g(self, θ: ArrayLike) -> ArrayLike:
        """
        Calculates g(θ), whose roots are the critical points of f(θ).
        """
        return (1 + self.ε * self.q) * θ**2 + (2 * self.θ0 - self.ε) * θ + self.θ0**2

    def h(self, θ: ArrayLike) -> ArrayLike:
        """
        Calculates h(θ), whose roots are the inflection points of f(θ).
        """
        # This complex polynomial is derived from the condition f''(θ) = 0
        return (
            self.ε**2 * self.q**2 * θ**3
            - 2 * self.ε**2 * self.q * θ**2
            + self.ε**2 * θ
            + 2 * self.ε * self.q**2 * θ**4
            + 2 * self.ε * self.q**2 * θ**3 * self.θ0
            - 2 * self.ε * self.q * θ**3
            + 2 * self.ε * self.q * θ * self.θ0**2
            - 2 * self.ε * θ * self.θ0
            - 2 * self.ε * self.θ0**2
            + 2 * self.q * θ**4
            + 8 * self.q * θ**3 * self.θ0
            + 12 * self.q * θ**2 * self.θ0**2
            + 8 * self.q * θ * self.θ0**3
            + 2 * self.q * self.θ0**4
        )

    def system(self, ξ: float, X: ArrayLike) -> ArrayLike:
        """
        Defines the ODE system for the traveling wave solution.
        """
        θ, So = X[0], X[1]
        Sy = (self.SoR - So) * self.SyL / self.SoR
        # Reaction term using Arrhenius law
        Φ = 1e8 * np.exp(-self.Er / (self.R * self.Tast * (θ + 1)))

        dX = np.empty_like(X)
        # dθ/dξ
        dX[0] = (
            self.β * θ * (self.c - self.a3)
            + (self.a1 * self.b3 * θ - self.b1 * (self.c - self.a3) * So * Sy * Φ)
        ) / ((self.c - self.a1 * So) * (self.c - self.a3))
        # dSo/dξ
        dX[1] = self.b3 * Sy * So * Φ / (self.c - self.a3)

        return dX
