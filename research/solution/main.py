#!/usr/bin/env python
"""
Main script for hyperbolic problem simulation: loads parameters,
initializes model/solver/plotter, performs root-finding,
and generates plots for functions, ODE solution, and phase portrait.
"""

from math import trunc

from solution.plotter import Plotter
from solution.solver import Solver
from solution.specific_model import SpecificModel
from solution.utils import (
    display_derived_parameters,
    display_key_values,
    display_parameters_table,
    load_parameters,
)


def main():
    """
    Main function to load parameters, run the simulation, and generate plots.
    """
    # --- 1. Initialization ---
    # Load physical parameters from the specified case file.
    params = load_parameters("angelbeta.toml")
    display_parameters_table(params)

    # Instantiate the model, solver, and plotter.
    # The model calculates derived dimensionless parameters upon initialization.
    model = SpecificModel(**params)
    display_derived_parameters(model)
    solver = Solver(model)
    plotter = Plotter(model, solver)

    # --- 2. Root-Finding Analysis ---
    # Find key points of interest by solving for the roots of model functions.
    print("\n--- Root-Finding Analysis ---")
    fprime_roots = solver.find_fprime_roots(initial_guesses=[0.1, 20])
    fprimeprime_root = solver.find_fprimeprime_root(initial_guess=0.1)

    # A guess for finding a specific root of f(θ).
    goodguess = trunc(1 / model.q) + 0.54
    θM = solver.find_f_root(y_value=1 / 4, initial_guess=goodguess)

    # Find θ3 such that f(θ3) = f(θ1), a key step for shock analysis.
    θ3 = solver.find_f_root(
        y_value=model.f(fprime_roots[0]),
        initial_guess=goodguess - 10,
    )

    # --- 3. Display Key Values ---
    display_key_values(model, fprime_roots, fprimeprime_root, θM, θ3)

    # --- 4. Generate and Save Plots ---
    print("\nGenerating and saving plots...")
    # Plots of f(θ), f'(θ), and f''(θ) over different ranges
    plotter.plot_f(x_range=(0, 1), filename="solution/f.pdf", position=(0.62, 0.00025))
    plotter.plot_fprime(
        x_range=(0, 1), filename="solution/fprime.pdf", position=(0.6, 0.01)
    )
    plotter.plot_fprimeprime(
        x_range=(0, 1), filename="solution/fprimeprime.pdf", position=(0.7, -0.2)
    )

    # Detailed plots of f(θ) over various domains
    plotter.plot_f(x_range=(1, 100), filename="solution/fa.pdf", position=(65, 4e-7))
    plotter.plot_f(
        x_range=(100, 15000), filename="solution/fb.pdf", position=(10000, 1e-5)
    )
    plotter.plot_fprime(
        x_range=(1, 100), filename="solution/fprimea.pdf", position=(60, -1e-6)
    )
    plotter.plot_fprimeprime(
        x_range=(1, 100), filename="solution/fprimeprimea.pdf", position=(60, 0.6e-5)
    )
    # # Plot the solution to the traveling wave ODE system
    plotter.plot_ode_solution(
        X0=[0.5, 0.5],
        t_span=(0, 1),
        filename="solution/ode_solution.pdf",
    )
    # plotter.plot_ode_solution(
    #     X0=[0.5, 0.5],
    #     t_span=(0, 1),
    #     filename="solution/ode_solution_all.pdf",
    #     all_in_one=True,
    # )
    # # Plot the phase portrait
    # plotter.plot_phase_portrait(
    #     so_range=(0, 1), theta_range=(0, 100), filename="solution/phaseportrait.pdf"
    # )
    # print("Plots saved in the 'solution' directory.")


if __name__ == "__main__":
    main()
