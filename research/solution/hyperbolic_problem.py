#!/usr/bin/env python
"""
Abstract base class for hyperbolic problems,
defining core mathematical functions and ODE system.
"""

from abc import ABC, abstractmethod

from numpy.typing import ArrayLike


class HyperbolicProblem(ABC):
    """
    Abstract base class for a hyperbolic conservation law model,
    defining core mathematical functions and the system of ODEs.
    Subclasses must provide concrete implementations.
    """

    def __init__(self, **kwargs):
        """
        Initializes the model with a variable set of parameters.
        Parameters passed as keyword arguments are set as attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractmethod
    def f(self, θ: ArrayLike) -> ArrayLike:
        """
        Represents the flux function f(θ) of the conservation law.
        """
        pass

    @abstractmethod
    def fprime(self, θ: ArrayLike) -> ArrayLike:
        """
        Represents the first derivative of the flux function, f'(θ).
        """
        pass

    @abstractmethod
    def fprimeprime(self, θ: ArrayLike) -> ArrayLike:
        """
        Represents the second derivative of the flux function, f''(θ),
        used for convexity.
        """
        pass

    @abstractmethod
    def g(self, θ: ArrayLike) -> ArrayLike:
        """
        Auxiliary function, typically related to f'(θ), for root-finding (g(θ)=0 at critical points).
        """
        pass

    @abstractmethod
    def h(self, θ: ArrayLike) -> ArrayLike:
        """
        Auxiliary function, typically related to f''(θ), for root-finding (h(θ)=0 at inflection points).
        """
        pass

    @abstractmethod
    def system(self, ξ: float, X: ArrayLike) -> ArrayLike:
        """
        Defines the system of ODEs for traveling wave solutions,
        to be used by an ODE solver.
        """
        pass
