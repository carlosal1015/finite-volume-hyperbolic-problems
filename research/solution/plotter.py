#!/usr/bin/env python
"""
Plotter for visualizing hyperbolic problem results with Matplotlib.
"""

from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
import matplotlib.patches as mpatches

from .hyperbolic_problem import HyperbolicProblem
from .solver import Solver


class Plotter:
    """
    Plots model's characteristic functions (f(θ), derivatives)
    and ODE system solutions.
    """

    def __init__(self, model: HyperbolicProblem, solver: Solver):
        """
        Initializes the plotter with a model and a solver instance.
        """
        self.model = model
        self.solver = solver
        plt.style.use("seaborn-v0_8-white")

    def _add_parameter_text(self, ax: Axes, x_pos: float, y_pos: float):
        """
        Adds a text box with key model parameters to the specified axes.
        """
        param_text = (
            r"$m=$"
            + f"{self.model.m:4g}"
            + "\n"
            + r"$q=$"
            + f"{self.model.q:4g}"
            + "\n"
            + r"$\varepsilon=$"
            + f"{self.model.ε:4g}"
            + "\n"
            + r"$\theta_{0}=$"
            + f"{self.model.θ0:4g}"
        )
        ax.text(x=x_pos, y=y_pos, s=param_text, color="black", fontdict={"size": 10})

    def plot_function(
        self,
        func_name: str,
        x_range: Tuple[float, float],
        filename: str,
        position: Tuple[float, float],
        color: str,
        label: str,
        num_points: int = 1000,
    ):
        """
        A generic method to plot a function from the model.
        """
        x_values = np.linspace(start=x_range[0], stop=x_range[1], num=num_points)
        func = getattr(self.model, func_name)
        y_values = func(x_values)

        fig, ax = plt.subplots(layout="constrained")
        ax.plot(
            x_values,
            y_values,
            color=color,
            label=label,
            linewidth=0.7,
            linestyle="solid",
        )
        ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
        ax.set_xlabel(r"$\theta$", fontsize=12)
        ax.legend(loc="best", shadow=True, fontsize=12)
        ax.set_xlim(x_values.min(), x_values.max())
        ax.spines["bottom"].set_color("none")
        ax.spines["top"].set_color("none")
        ax.spines["left"].set_color("none")
        ax.spines["right"].set_color("none")

        self._add_parameter_text(ax, position[0], position[1])

        fig.savefig(filename, transparent=True, bbox_inches="tight")
        plt.close(fig)

    def plot_f(
        self,
        x_range: Tuple[float, float],
        filename: str,
        position: Tuple[float, float],
        num_points: int = 1000,
    ):
        """Plots the flux function f(θ)."""
        self.plot_function(
            func_name="f",
            x_range=x_range,
            filename=filename,
            position=position,
            color="blue",
            label=r"$f\left(\theta\right)$",
            num_points=num_points,
        )

    def plot_fprime(
        self,
        x_range: Tuple[float, float],
        filename: str,
        position: Tuple[float, float],
        num_points: int = 1000,
    ):
        """Plots the first derivative of the flux function, f'(θ)."""
        self.plot_function(
            func_name="fprime",
            x_range=x_range,
            filename=filename,
            position=position,
            color="red",
            label=r"$f^{\prime}\left(\theta\right)$",
            num_points=num_points,
        )

    def plot_fprimeprime(
        self,
        x_range: Tuple[float, float],
        filename: str,
        position: Tuple[float, float],
        num_points: int = 1000,
    ):
        """Plots the second derivative of the flux function, f''(θ)."""
        self.plot_function(
            func_name="fprimeprime",
            x_range=x_range,
            filename=filename,
            position=position,
            color="green",
            label=r"$f^{\prime\prime}\left(\theta\right)$",
            num_points=num_points,
        )

    def plot_ode_solution(
        self,
        X0: List[float],
        t_span: Tuple[float, float],
        filename: str,
        num_points: int = 100,
        all_in_one: bool = False,
    ):
        """
        Plots the solution of the ODE system over a given interval.
        Integration is performed forwards and backwards from a central point.
        """
        t_center = (t_span[0] + t_span[1]) / 2
        t_left, X_left = self.solver.solve_ode(
            X0=X0, t_span=(t_center, t_span[0]), num_points=num_points
        )
        t_right, X_right = self.solver.solve_ode(
            X0=X0, t_span=(t_center, t_span[1]), num_points=num_points
        )

        if all_in_one:
            fig, ax = plt.subplots(layout="constrained")
            fig.suptitle("ODE Solution")

            # Plot theta
            ax.plot(t_left, X_left[:, 0], color="red", linewidth=0.7, label=r"$\theta$")
            ax.plot(t_right, X_right[:, 0], color="red", linewidth=0.7)

            # Plot Sy
            ax.plot(
                t_left,
                X_left[:, 2],
                color="blue",
                linewidth=0.7,
                label=r"$S_{\text{y}}$",
            )
            ax.plot(t_right, X_right[:, 2], color="blue", linewidth=0.7)

            # Plot So
            ax.plot(
                t_left,
                X_left[:, 1],
                color="black",
                linewidth=0.7,
                label=r"$S_{\text{o}}$",
            )
            ax.plot(t_right, X_right[:, 1], color="black", linewidth=0.7)

            ax.set_xlabel(r"$\xi$")
            ax.set_ylabel("Values")
            ax.set_xlim(t_left.min(), t_right.max())
            ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
            for spine in ax.spines.values():
                spine.set_color("none")

            ax.legend(loc="best", shadow=True, fontsize=12)
            fig.savefig(filename, transparent=True, bbox_inches="tight")
            plt.close(fig)
        else:
            fig, (ax0, ax1, ax2) = plt.subplots(
                nrows=3, constrained_layout=True, gridspec_kw={"hspace": 0.1}
            )
            fig.suptitle(
                "ODE Solution with IC at "
                + r"$\theta\left(\frac{1}{2}\right)=\frac{1}{2}$ and "
                + r"$S^{\text{R}}_{\text{o}}\left(\frac{1}{2}\right)=\frac{1}{2}$."
            )

            # Plot theta
            ax0.plot(
                t_left, X_left[:, 0], color="red", linewidth=0.7, label=r"$\theta$"
            )
            ax0.plot(t_right, X_right[:, 0], color="red", linewidth=0.7)
            ax0.set_ylabel(r"$\theta$")

            # Plot Sy
            ax1.plot(
                t_left,
                X_left[:, 2],
                color="blue",
                linewidth=0.7,
                label=r"$S_{\text{y}}$",
            )
            ax1.plot(t_right, X_right[:, 2], color="blue", linewidth=0.7)
            ax1.set_ylabel(r"$S_{\text{y}}$")
            ax1.text(
                0.72,
                0.65,
                r"$S_{\text{y}}=$"
                + r"$\left(S^{\text{R}}_{\text{o}}-S_{\text{o}}\right)$"
                + r"$\frac{S^{\text{L}}_{\text{y}}}{S^{\text{R}}_{\text{o}}}$",
                transform=ax1.transAxes,
                fontsize=10,
            )

            # Plot So
            ax2.plot(
                t_left,
                X_left[:, 1],
                color="black",
                linewidth=0.7,
                label=r"$S_{\text{o}}$",
            )
            ax2.plot(t_right, X_right[:, 1], color="black", linewidth=0.7)
            ax2.set_ylabel(r"$S_{\text{o}}$")

            for ax in [ax0, ax1, ax2]:
                ax.set_xlabel(r"$\xi$")
                ax.set_xlim(t_left.min(), t_right.max())
                ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
                for spine in ax.spines.values():
                    spine.set_color("none")

            fig.legend(
                handles=[ax0.lines[0], ax2.lines[0], ax1.lines[0]],
                bbox_to_anchor=(0.77, 0.85),
                loc="lower center",
                ncol=3,
                shadow=True,
                fontsize=12,
            )
            fig.savefig(filename, transparent=True, bbox_inches="tight")
            plt.close(fig)

        # a, b = 1, 3
        # t_center = 2
        # t1 = np.linspace(t_center, a)
        # t2 = np.linspace(t_center, b)
        # y0 = 2

        # def f1(y, t1):
        #     return y / t1

        # def f2(y, t2):
        #     return y / t2

        # sol1 = odeint(f1, y0, t1)
        # sol2 = odeint(f1, y0, t2)
        # plt.plot(t1, sol1, "red")
        # plt.plot(t2, sol2, "red")

    def plot_phase_portrait(
        self,
        so_range: tuple,
        theta_range: tuple,
        filename: str,
        num_points: int = 1000,
    ):
        """
        Plots the phase portrait in the (So, θ) plane using an implicit equation.
        It plots the zero contour of the equation: So(SoR - So) - f(θ) = 0.
        """
        so_values = np.linspace(so_range[0], so_range[1], num_points)
        theta_values = np.linspace(theta_range[0], theta_range[1], num_points)
        so_grid, theta_grid = np.meshgrid(so_values, theta_values)

        # Calculate f(θ) across the grid
        f_values = self.model.f(theta_grid)  # * 1e8

        fig, ax = plt.subplots(constrained_layout=True)
        ax.set_xlabel(r"$S_{\text{o}}$")
        ax.set_ylabel(r"$\theta$")

        # Plot the contour where the implicit equation is zero
        cntr = ax.contour(
            so_grid,
            theta_grid,
            so_grid * (self.model.SoR - so_grid) - f_values,
            levels=[0],
            linewidths=0.5,
            colors="red",
        )
        ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
        ax.spines["bottom"].set_color("none")
        ax.spines["top"].set_color("none")
        ax.spines["left"].set_color("none")
        ax.spines["right"].set_color("none")

        # Create a Patch for the legend
        legend_patch = mpatches.Patch(
            color="red",
            label=r"$S_{\text{o}}\left(S^{\text{R}}_{\text{o}}-S_{\text{o}}\right)-10^{8}f\left(\theta\right)=0$",
            linewidth=0.1,
            linestyle="-",
        )
        ax.legend(
            handles=[legend_patch],
            shadow=True,
            loc="best",
            # title="Legend",
            fancybox=True,
            fontsize=8,
        )
        fig.savefig(filename, transparent=True, bbox_inches="tight")
        plt.close(fig)

    # def plot_phase_portrait_II(
    #     self, x_range: tuple, filename: str, num_points: int = 1000
    # ):
    #     """
    #     Plots the phase portrait in the (So, θ) plane.
    #     """
    #     theta_values = np.linspace(start=x_range[0], stop=x_range[1], num=num_points)
    #     f_values = self.model.f(theta_values) * 1e8

    #     # Calculate the two branches of the curve So(SoR - So) = f(θ)
    #     discriminant = np.power(self.model.SoR, 2) - 4 * f_values
    #     # Ensure we don't take the square root of negative numbers
    #     valid_indices = discriminant >= 0

    #     So_plus = (self.model.SoR + np.sqrt(discriminant[valid_indices])) / 2
    #     So_minus = (self.model.SoR - np.sqrt(discriminant[valid_indices])) / 2

    #     fig, ax = plt.subplots(constrained_layout=True)
    #     ax.plot(
    #         So_minus, theta_values[valid_indices], "red", label=r"$S^{-}_{\text{o}}$"
    #     )
    #     ax.plot(
    #         So_plus, theta_values[valid_indices], "blue", label=r"$S^{+}_{\text{o}}$"
    #     )
    #     ax.set_xlabel(r"$S_{\text{o}}$")
    #     ax.set_ylabel(r"$\theta$")
    #     ax.set_xlim(So_minus.min(), So_plus.max())
    #     ax.set_ylim(theta_values.min(), theta_values.max())
    #     ax.spines["bottom"].set_color("none")
    #     ax.spines["top"].set_color("none")
    #     ax.spines["left"].set_color("none")
    #     ax.spines["right"].set_color("none")
    #     ax.legend(loc="best", shadow=True, fontsize=12)
    #     ax.grid(True, linestyle="--", linewidth=0.5)
    #     fig.savefig(filename, transparent=True, bbox_inches="tight")
    #     plt.close(fig)
